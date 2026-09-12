#!/usr/bin/env bash
# The rotation host gap's control (2026-09-12). The tier's batch read Metal 3-5 dB above libplacebo on the
# rotation scenes and within a decibel elsewhere, the gap growing with the level of the reading -- the shape
# of a floor. The libplacebo chain quantises the source to 8 bits (format=yuv420p, the P10 dither fix) while
# Metal reads the 16-bit raw. This feeds BOTH hosts the same 8-bit-EXACT source -- every 16-bit sample
# rounded to a multiple of 257, so the value is representable in 8 bits and the yuv420p step adds nothing
# new -- and scores Metal against the truth as before. If Metal drops to libplacebo's level, the gap is the
# source's 8 bits; if it stays, the gap is elsewhere. (A first try through limited-range yuv and back
# carried a rounding bias that cost 16 dB even on the static scene: this control avoids any yuv step.)
#
#   ./hostgap.sh <outroot> [scenes...]     STEM=quaddirectional-interpolation-propagated; FFMPEG PYTHON QUADDEMO GRAPHS
set -u
OUT="$1"; shift
SCENES="${*:-static bounce-constant spin-constant spin-accelerating spin-pendulum}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"; TESTS="$(cd "$HERE/../.." && pwd)"
FFMPEG="${FFMPEG:-ffmpeg}"; PY="${PYTHON:-python3}"; QUAD="${QUADDEMO:?}"; GRAPHS="${GRAPHS:?}"
STEM="${STEM:-quaddirectional-interpolation-propagated}"; W=1280; H=720
mkdir -p "$OUT"
printf '%-20s %10s %10s %10s %10s\n' scene "metal16" "metal8" "placebo8" "placebo16src"
for sc in $SCENES; do
  d="$OUT/$sc"; mkdir -p "$d"
  "$PY" "$TESTS/masters.py" "$sc" --size ${W}x${H} --frames 96 --src-fps 24 --out-fps 60 --settle 0 --bg flat \
        --export-source "$d/src16.raw" --export-truth "$d/truth60.raw" > /dev/null
  "$PY" - "$d/src16.raw" "$d/src8.raw" <<'PY'
import sys, numpy as np
a = np.fromfile(sys.argv[1], dtype="<u2")
np.rint(a / 257.0).astype(np.uint16).__mul__(257).astype("<u2").tofile(sys.argv[2])   # 8-bit-exact levels in 16 bits
PY
  score() { "$FFMPEG" -y -v error -f rawvideo -pix_fmt rgb48le -s ${W}x${H} -r 60 -i "$1" -f rawvideo -pix_fmt rgb48le -s ${W}x${H} -r 60 -i "$d/truth60.raw" \
              -lavfi "[0:v]format=yuv420p[a];[1:v]format=yuv420p[b];[a][b]psnr=stats_file=$2" -f null - 2>/dev/null; "$PY" "$HERE/reading.py" "$2" "$TESTS" | cut -d' ' -f1; }
  pl() { ( cd "$d" && "$FFMPEG" -y -v error -init_hw_device vulkan=vk -filter_hw_device vk -f rawvideo -pix_fmt rgb48le -s ${W}x${H} -r 24 -i "$1" \
              -f rawvideo -pix_fmt rgb48le -s ${W}x${H} -r 60 -i truth60.raw \
              -filter_complex "[0:v]${2}libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_s.glsl[ip];[ip]format=yuv420p[a];[1:v]format=yuv420p[b];[a][b]psnr=stats_file=$3" -f null - ) 2>/dev/null; "$PY" "$HERE/reading.py" "$d/$3" "$TESTS" | cut -d' ' -f1; }
  cp -f "$TESTS/../shaders/$STEM.glsl" "$d/_s.glsl"
  "$QUAD" --graph "$GRAPHS/$STEM" --input "$d/src16.raw" --src-fps 24 --out-fps 60 --size ${W}x${H} --export "$d/m16.raw" > /dev/null 2>&1
  m16=$(score "$d/m16.raw" "$d/m16.psnr"); rm -f "$d/m16.raw"
  "$QUAD" --graph "$GRAPHS/$STEM" --input "$d/src8.raw" --src-fps 24 --out-fps 60 --size ${W}x${H} --export "$d/m8.raw" > /dev/null 2>&1
  m8=$(score "$d/m8.raw" "$d/m8.psnr"); rm -f "$d/m8.raw"
  p8=$(pl src8.raw "format=yuv420p," p8.psnr)            # the batch's chain, on the 8-bit-exact source
  p16=$(pl src16.raw "" p16.psnr)                        # libplacebo fed the 16-bit source directly (its dither trap, for the record)
  printf '%-20s %10s %10s %10s %10s\n' "$sc" "$m16" "$m8" "$p8" "$p16"
  rm -f "$d/src16.raw" "$d/src8.raw" "$d/truth60.raw" "$d/_s.glsl"
done
