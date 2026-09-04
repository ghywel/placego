#!/bin/bash
# Scan source material for moments likely to contain an interpolation defect.
#
#   ./prospect.sh <source> [start-seconds] [duration-seconds] [shader]
#
# Renders the source through a flow visualiser build of the production shader
# and ranks moments by how badly the flow field disagrees with itself. Prints
# a shortlist of timestamps and a ready-to-run clip.sh line for each.
#
# This is the fast-and-literal half of a two-stage process. It finds data
# perturbation, which correlates with visible defects but is not the same
# thing; a human still decides whether each candidate is a real problem or
# statistical noise. Expect false positives -- that is the tool working, not
# failing. What it removes is the need to watch everything.
#
# The flow render is PIPED straight into the analyser rather than written out.
# At 1920x1038 a 60-second clip is 3886 output frames, which is 21.6 GB of raw
# RGB and a large intermediate file even compressed. Nothing is stored: frames
# are consumed one at a time and only per-frame scalars are kept.
#
# COST is dominated by rendering. On a real GPU expect faster than real time;
# under software Vulkan expect roughly 30x real time, so scan scenes rather
# than films, or leave it running. The start and duration arguments exist for
# exactly that.
#
#   ./prospect.sh clip.mp4                  # whole clip
#   ./prospect.sh film.mkv 1800 120         # 2 minutes at 30:00
#
# Set FFMPEG/FFPROBE to point at the patched build.

set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FFMPEG="${FFMPEG:-ffmpeg}"
FFPROBE="${FFPROBE:-ffprobe}"
OUTFPS="${OUTFPS:-60}"
PY="${PY:-python3}"
command -v "$PY" >/dev/null 2>&1 || PY=python
WORK="${WORK:-${TMPDIR:-/tmp}/interp-prospect}"

SRC="${1:?usage: prospect.sh <source> [start-seconds] [duration-seconds] [shader]}"
START="${2:-0}"
DUR="${3:-}"
SHADER="${4:-$HERE/../shaders/bidirectional-interpolation-variational.glsl}"

[ -f "$SRC" ] || { echo "no such file: $SRC" >&2; exit 1; }
[ -f "$SHADER" ] || { echo "no such shader: $SHADER" >&2; exit 1; }
mkdir -p "$WORK"

field() {
  "$FFPROBE" -v error -select_streams v:0 -show_entries "stream=$1" \
    -of default=noprint_wrappers=1:nokey=1 "$SRC" | head -1
}
FPS_R="$(field r_frame_rate)"
W="$(field width)"
H="$(field height)"
[ -n "$FPS_R" ] && [ -n "$W" ] || { echo "could not probe $SRC" >&2; exit 1; }
FPS_N="${FPS_R%%/*}"; FPS_D="${FPS_R##*/}"
[ "$FPS_N" = "$FPS_D" ] && FPS_D=1
SRCFPS=$(awk -v n="$FPS_N" -v d="$FPS_D" 'BEGIN{printf "%.6f", n/d}')

echo "source   $(basename "$SRC")  ${W}x${H}  ${SRCFPS} fps"
echo "shader   $(basename "$SHADER")"
echo "window   from ${START}s${DUR:+ for ${DUR}s}"
echo

# Rewrite only the final hook() of the real shader, so what gets analysed is
# exactly what production computes rather than a re-implementation.
$PY "$HERE/flowvis.py" "$SHADER" "$WORK/vis.glsl" >/dev/null || exit 1

SEEK=(); [ "$START" != "0" ] && SEEK=(-ss "$START")
LIMIT=(); [ -n "$DUR" ] && LIMIT=(-t "$DUR")

# The flow field is COMPUTED at half resolution and upsampled, so analysing it
# at full resolution is pure oversampling. Subsampling by DECIMATE cuts the
# piped bytes and the analysis cost by its square -- at 2 that is 21.6 GB down
# to 5.4 GB on a 60-second 1920x1038 clip, and the analysis is what dominates
# the wall clock once a real GPU is doing the rendering.
#
# `flags=neighbor` matters: averaging would dilute exactly the isolated
# outlier vectors this is looking for, whereas subsampling preserves their
# values. The radius is scaled to match, so the neighbourhood keeps the same
# extent in source pixels and the numbers stay comparable across settings.
DECIMATE="${DECIMATE:-2}"
AW=$((W / DECIMATE)); AH=$((H / DECIMATE))
RADIUS=$(awk -v d="$DECIMATE" 'BEGIN{r=int(6/d); print (r<2)?2:r}')
SCALEF=""
[ "$DECIMATE" != "1" ] && SCALEF=",scale=${AW}:${AH}:flags=neighbor"
echo "analysis grid ${AW}x${AH} (decimate ${DECIMATE}), neighbourhood radius ${RADIUS}"
echo
# Always persist the measurements. A scan costs minutes of GPU time and would
# otherwise exist only as text in a terminal; saved, it can be re-ranked with
# different parameters for free (prospect.py --load) and compared against a
# later scan of the same material after a shader change.
SAVE="${SAVE:-$WORK/$(basename "${SRC%.*}").scan}"

echo "scanning (rendering and analysing in one pass)..."
T0=$(date +%s)

# The shader is referenced by BARE NAME from its own directory: an absolute
# path cannot be used inside an ffmpeg filter argument on Windows, because the
# drive-letter colon is ffmpeg's option separator. Relative works on both.
( cd "$WORK" && "$FFMPEG" -hide_banner -loglevel error \
    -init_hw_device vulkan=vk -filter_hw_device vk \
    "${SEEK[@]}" -i "$SRC" "${LIMIT[@]}" \
    -vf "libplacebo=fps=${OUTFPS}:frame_mixer=custom_n:custom_shader_path=vis.glsl,format=rgb24${SCALEF}" \
    -map 0:v:0 -an -sn -dn -f rawvideo - ) |
  FFMPEG="$FFMPEG" FFPROBE="$FFPROBE" $PY "$HERE/prospect.py" --stream \
    --width "$AW" --height "$AH" --radius "$RADIUS" \
    --source "$SRC" --src-fps "$SRCFPS" --out-fps "$OUTFPS" --offset "$START" \
    --progress 600 --save "$SAVE"
rc=$?

T1=$(date +%s)
echo
echo "  scan took $((T1 - T0))s"
exit $rc
