#!/usr/bin/env bash
# P3 acceptance, part 1: the ladder, through the EXISTING methodology.
#
#   ./accept.sh [OUTROOT] [ffmpeg-quad-outroot]
#
# For every synthetic case: render the 24 fps source (rgb48le raw, the
# same lavfi scene definitions bench.sh uses), interpolate 24->60 through
# the native Metal engine, and score against the 60 fps ground truth with
# ffmpeg's psnr filter behind a format=yuv420p convert -- bench.sh's
# exact comparison, so the numbers are commensurable. Logs land as
# metal.log per case; if an existing bench OUTROOT is given (e.g. the
# ffmpeg+MoltenVK quad run), its hold/linear/shader logs are copied in
# so `analyze.py --variants` prints the port side by side with the
# pipeline it must match. WHAT PASSES: metal within the platform's own
# run-to-run wobble (~0.25 dB) of the ffmpeg quad column.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS="$HERE/../tests"
OUTROOT="${1:-$HOME/np-work/bench-metal}"
FFQUAD="${2:-$HOME/np-work/bench-quad}"
FFMPEG="${FFMPEG:-$HOME/np-build/ffmpeg/ffmpeg}"
QUAD="$HERE/.build/release/QuadDemo"
[ -x "$QUAD" ] || { echo "build first: (cd $HERE && swift build -c release)"; exit 1; }
. "$TESTS/scenes.sh"

for CASE in $ALL_CASES; do
  D="$OUTROOT/$CASE"; mkdir -p "$D"
  S24="$(scene "$CASE" 24)"; S60="$(scene "$CASE" 60)"
  [ "$S24" = "UNKNOWN_CASE" ] && { echo "unknown case $CASE"; continue; }
  "$FFMPEG" -y -v error -f lavfi -i "$S24" -pix_fmt rgb48le -f rawvideo "$D/src24.raw"
  # Truth goes through the SAME rgb48le hop as the port's input/output, so
  # any range/matrix conversion is common-mode and cancels. Without this,
  # every metal frame -- including verbatim source copies -- scored a flat
  # ~45 dB: the comparison lying, exactly the trap TESTING.md warns about.
  "$FFMPEG" -y -v error -f lavfi -i "$S60" -pix_fmt rgb48le -f rawvideo "$D/truth60.raw"
  ( cd "$HERE" && ./.build/release/QuadDemo --input "$D/src24.raw" \
      --export "$D/metal60.raw" --size 1280x720 2>/dev/null )
  ( cd "$D" && "$FFMPEG" -y -v error \
      -f rawvideo -pix_fmt rgb48le -video_size 1280x720 -framerate 60 -i metal60.raw \
      -f rawvideo -pix_fmt rgb48le -video_size 1280x720 -framerate 60 -i truth60.raw \
      -lavfi "[0:v]format=yuv420p[a];[1:v]format=yuv420p[b];[a][b]psnr=stats_file=metal.log" -f null - )
  # The passthrough assert: output frame 1 is a verbatim copy of source
  # frame 0, so anything but a near-infinite score means the comparison
  # path is broken -- fail loudly rather than produce confident nonsense.
  P1=$(awk 'NR==1{for(i=1;i<=NF;i++) if ($i ~ /^psnr_avg:/) print substr($i,10)}' "$D/metal.log")
  case "$P1" in
    inf|1[0-9][0-9]*) : ;;
    *) [ "${P1%%.*}" -ge 70 ] 2>/dev/null || \
         echo "  WARNING $CASE: passthrough frame scores $P1 dB -- comparison suspect" ;;
  esac
  # lay the ffmpeg-pipeline columns alongside for the side-by-side table
  if [ -d "$FFQUAD/$CASE" ]; then
    cp -f "$FFQUAD/$CASE/hold.log" "$FFQUAD/$CASE/linear.log" "$D/" 2>/dev/null
    cp -f "$FFQUAD/$CASE/shader.log" "$D/quad_ffmpeg.log" 2>/dev/null
  fi
  rm -f "$D/src24.raw" "$D/metal60.raw" "$D/truth60.raw"
  echo "  $CASE done"
done

echo
PATH="/opt/homebrew/bin:$PATH" \
PYTHONPATH="${PYTHONPATH:-$(echo "$HOME"/np-build/venv/lib/python*/site-packages)}" \
OUTROOT="$OUTROOT" python3 "$TESTS/analyze.py" --variants
