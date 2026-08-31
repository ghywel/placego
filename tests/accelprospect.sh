#!/bin/bash
# Rank real footage by ACCELERATION, using the tridirectional field itself.
#
#   ./accelprospect.sh <source> [start-seconds] [duration-seconds] [segment-seconds]
#
# WHY THIS IS THE SAME TOOL TWICE. The correction a 3-frame shader applies is
# a/8 px at mid-interval, which is exactly "how far a 2-frame shader misplaces
# this texel". So the acceleration field is simultaneously the shader's output
# and a DEFECT DETECTOR for every 2-frame interpolator, including the
# production one. Ranking a film by it answers two questions at once: where is
# there real acceleration to measure, and where is bidirectional interpolation
# most likely to be visibly wrong.
#
# It is also self-validating. If the field is meaningful, the segments it ranks
# highest should be the segments where the tridirectional shader beats the
# bidirectional one by the most -- and that is a falsifiable prediction rather
# than a hope. Confirm with realbench.sh on the top and bottom segments.
#
# METHOD. TRI_DIAG=4 renders |a| as linear luma, so a whole-frame average is
# proportional to mean acceleration. signalstats reduces each frame to YAVG
# and YMAX, which are printed as metadata and summarised per segment. Nothing
# is written to disk.
#
#   YAVG -> how much of the frame is accelerating
#   YMAX -> whether anything in it is accelerating hard
#
# Both matter and they rank differently: a small fast-moving object scores low
# on YAVG and high on YMAX. The summary prints both, sorted by YAVG.
#
# PERFORMANCE NOTES, since this runs over feature-length sources:
#   - Input seeking (-ss BEFORE -i) so a seek into the middle of a 3GB file
#     does not decode everything preceding it.
#   - Output at the SOURCE frame rate, not 60: the acceleration field is a
#     function of the 3-frame window, so sampling faster than the source
#     re-reads the same field and buys nothing.
#   - The stats run on a downscaled copy. signalstats at full 1920x808 is
#     pure CPU and would become the bottleneck on a GPU that renders the
#     shader at over 100fps.
#   - -an -sn drops audio and subtitles before they are decoded.
#   - No intermediate files, so the exFAT source pool is read once and never
#     written to.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

FFMPEG="${FFMPEG:-ffmpeg}"
SRC="${1:?usage: accelprospect.sh <source> [start] [duration] [segment]}"
START="${2:-0}"
DUR="${3:-300}"
SEG="${4:-10}"
SHADER="${SHADER:-$HERE/../tridirectional-interpolation.glsl}"
FS="${ACCEL_DIAG_FS:-2.0}"
WORK="${WORK:-${TMPDIR:-/tmp}}/accelprospect"

mkdir -p "$WORK" || exit 1
# The shader is referenced by BARE NAME from $WORK: a path inside an ffmpeg
# filter argument is unusable on Windows (the drive-letter colon is ffmpeg's
# own option separator) and a POSIX path is unusable by a native binary.
sed -e "s/const int TRI_DIAG = 0;/const int TRI_DIAG = 4;/" \
    -e "s/const float ACCEL_DIAG_FS = 2.0;/const float ACCEL_DIAG_FS = $FS;/" \
    "$SHADER" > "$WORK/_scan.glsl" || exit 1
grep -q "TRI_DIAG = 4" "$WORK/_scan.glsl" || { echo "shader patch failed" >&2; exit 1; }

RATE="$("${FFPROBE:-ffprobe}" -v error -select_streams v:0 \
        -show_entries stream=r_frame_rate -of csv=p=0 "$SRC")"
echo "source    $(basename "$SRC")  @ $RATE fps"
echo "scanning  ${START}s .. $((START + DUR))s in ${SEG}s segments, "\
"full scale ${FS} px/interval^2"
echo

( cd "$WORK" && "$FFMPEG" -hide_banner -loglevel error \
    -init_hw_device vulkan=vk -filter_hw_device vk \
    -ss "$START" -t "$DUR" -i "$SRC" -an -sn \
    -vf "libplacebo=fps=$RATE:frame_mixer=custom_n:custom_shader_path=_scan.glsl,scale=320:-2:flags=fast_bilinear,format=gray,signalstats,metadata=print:file=stats.txt" \
    -f null - ) 2>"$WORK/scan.err" || { echo "scan failed:"; head -3 "$WORK/scan.err"; exit 1; }

awk -v seg="$SEG" -v start="$START" -v rate_s="$RATE" -v fs="$FS" '
  BEGIN { split(rate_s, r, "/"); fps = r[2] ? r[1]/r[2] : r[1] }
  # metadata=print writes "frame:N  pts:P  pts_time:T", so the frame number
  # is inside field 1, not field 2. Reading $2 silently pins every frame to
  # segment 0 and reports the whole scan as one row.
  /^frame:/ { split($1, f, ":"); n = f[2] + 0 }
  /lavfi\.signalstats\.YAVG/ { split($0, a, "="); yavg = a[2] + 0 }
  /lavfi\.signalstats\.YMAX/ { split($0, a, "="); ymax = a[2] + 0
    s = int((n / fps) / seg)
    sum[s] += yavg; if (ymax > peak[s]) peak[s] = ymax; cnt[s]++ }
  END {
    printf "%-10s %-10s %12s %12s\n", "segment", "t(s)", "mean |a|", "peak |a|"
    printf "%s\n", "---------------------------------------------------"
    for (s in cnt) {
      # Luma 0..255 maps linearly onto 0..fs px/interval^2.
      printf "%-10d %-10.1f %12.4f %12.4f\n", s, start + s*seg,
             (sum[s]/cnt[s]) * fs / 255.0, peak[s] * fs / 255.0
    }
  }' "$WORK/stats.txt" | { read -r h1; read -r h2; echo "$h1"; echo "$h2"; sort -k3 -gr; }

echo
echo "Ranked by mean |a| (px/interval^2). The top segments are where a 2-frame"
echo "shader misplaces content most -- cut those with clip.sh and A/B them."
