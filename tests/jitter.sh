#!/bin/bash
# Render a clip through the shader and look for TEMPORAL defects.
#
#   ./jitter.sh <source> [start-seconds] [duration-seconds] [shader]
#
# The companion to prospect.sh, which measures the flow field and is blind to
# anything that goes wrong in time rather than in space -- judder, stutter, or
# flow that is uniform but wrong. This measures the rendered output instead.
#
# Reads greyscale at reduced size: temporal artefacts are about how the whole
# frame advances, not about fine detail, and it keeps the pipe cheap.
#
# Set FFMPEG/FFPROBE to point at the patched build.

set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FFMPEG="${FFMPEG:-ffmpeg}"
FFPROBE="${FFPROBE:-ffprobe}"
OUTFPS="${OUTFPS:-60}"
PY="${PY:-python3}"
command -v "$PY" >/dev/null 2>&1 || PY=python
WORK="${WORK:-${TMPDIR:-/tmp}/interp-jitter}"

SRC="${1:?usage: jitter.sh <source> [start-seconds] [duration-seconds] [shader]}"
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
FPS_R="$(field r_frame_rate)"; W="$(field width)"; H="$(field height)"
[ -n "$FPS_R" ] || { echo "could not probe $SRC" >&2; exit 1; }
FPS_N="${FPS_R%%/*}"; FPS_D="${FPS_R##*/}"
[ "$FPS_N" = "$FPS_D" ] && FPS_D=1
SRCFPS=$(awk -v n="$FPS_N" -v d="$FPS_D" 'BEGIN{printf "%.6f", n/d}')

AW=$((W / 2)); AH=$((H / 2))
echo "source   $(basename "$SRC")  ${W}x${H}  ${SRCFPS} fps"
echo "shader   $(basename "$SHADER")"
echo "grid     ${AW}x${AH} grey"
echo

# The shader is copied beside the work directory and used by bare name: an
# absolute path cannot appear in an ffmpeg filter argument on Windows.
cp -f "$SHADER" "$WORK/sh.glsl"

SEEK=(); [ "$START" != "0" ] && SEEK=(-ss "$START")
LIMIT=(); [ -n "$DUR" ] && LIMIT=(-t "$DUR")
SAVE="${SAVE:-$WORK/$(basename "${SRC%.*}").jitter}"

echo "rendering and measuring..."
T0=$(date +%s)
( cd "$WORK" && "$FFMPEG" -hide_banner -loglevel error \
    -init_hw_device vulkan=vk -filter_hw_device vk \
    "${SEEK[@]}" -i "$SRC" "${LIMIT[@]}" \
    -vf "libplacebo=fps=${OUTFPS}:frame_mixer=custom_n:custom_shader_path=sh.glsl,format=gray,scale=${AW}:${AH}" \
    -map 0:v:0 -an -sn -dn -f rawvideo - ) |
  $PY "$HERE/jitter.py" --width "$AW" --height "$AH" \
    --out-fps "$OUTFPS" --src-fps "$SRCFPS" --offset "$START" \
    --progress 600 --save "$SAVE"
rc=$?
T1=$(date +%s)
echo
echo "  took $((T1 - T0))s"
exit $rc
