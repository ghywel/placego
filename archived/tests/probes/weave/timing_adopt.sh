#!/bin/bash
# ENERGY-TRANSFER.md stage 1c, A5: what OUTLINE_ADOPT costs, by probes/cost/timing.sh's method on a Mac.
# - The source is an ffv1 FILE rendered once (a lavfi source is up to 70% of a naive shader time).
# - The output goes to -f null, so no encoder is timed.
# - The labels are INTERLEAVED over three rounds, so thermal drift and driver warm-up cancel.
# 720p, 24 -> 60, the ladder's O5_osc_textured, 3 s (180 output frames). MoltenVK's own defaults (this script does not
# source mvk-env.sh: a timing run). One GPU job at a time; run alone.
#   timing_adopt.sh <variant.glsl> [rounds=3]
# BASE=<glsl> times the variant against another base (since 2026-10-01 the adopted default is the player's); SRC=<raw
# gray16le 1280x720 24 fps> times on that source instead of O5 (wrapped as ffv1 once, beside the default source).
set -u
V="${1:?the variant}"; ROUNDS="${2:-3}"
FF="${FFMPEG:-$HOME/np-build/ffmpeg/ffmpeg}"
SC="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
G="${NP_SCRATCH:-$(cd "$SC/../.." && pwd)/np-scratch}/weave/timing"; mkdir -p "$G"   # np-scratch beside the checkout
. "$SC/tests/scenes.sh"
if [ ! -s "$G/src.mkv" ]; then
  S="$(scene O5_osc_textured 24)"; S="${S//:d=1,/:d=3,}"
  "$FF" -y -hide_banner -loglevel error -f lavfi -i "$S" -c:v ffv1 "$G/src.mkv" || exit 1
fi
SRCMKV=src.mkv
if [ -n "${SRC:-}" ]; then
  SRCMKV="src-$(basename "${SRC%.*}").mkv"
  if [ ! -s "$G/$SRCMKV" ]; then
    case "$SRC" in
      *.raw) "$FF" -y -hide_banner -loglevel error -f rawvideo -pix_fmt gray16le -s 1280x720 -r 24 -i "$SRC" \
               -t 3 -c:v ffv1 "$G/$SRCMKV" || exit 1 ;;
      *)     "$FF" -y -hide_banner -loglevel error -ss 10 -i "$SRC" -t 3 -an -vf "scale=1280:720,fps=24" \
               -c:v ffv1 "$G/$SRCMKV" || exit 1 ;;                    # a real clip: 3 s from 10 s in, 720p24
    esac
  fi
fi
cp -f "${BASE:-$SC/shaders/bidirectional-interpolation-variational-propagated-global-cage-energy-carry.glsl}" "$G/default.glsl"
cp -f "$V" "$G/adopt.glsl"
cd "$G" || exit 1
LABELS=(linear default adopt)
rm -f times-*.txt                                          # bash 3.2 (macOS): no associative arrays; one file per label
echo "########## TIMING $(date +%T): source $SRCMKV $(stat -f %z "$SRCMKV") bytes, $ROUNDS rounds, interleaved"
for r in $(seq 1 "$ROUNDS"); do
  for L in "${LABELS[@]}"; do
    if [ "$L" = linear ]; then MIX="frame_mixer=linear"; else MIX="frame_mixer=custom_n:custom_shader_path=$L.glsl"; fi
    s=$(python3 -c 'import time; print(time.time())')
    "$FF" -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk -i "$SRCMKV" \
      -vf "format=yuv420p,libplacebo=fps=60:$MIX" -f null - 2> "err-$L.txt" || { echo "  $L FAILED"; cat "err-$L.txt"; }
    grep -q "compile status" "err-$L.txt" && echo "  $L: A COMPILE ERROR (libplacebo fell back to its own mixer)"
    e=$(python3 -c 'import time; print(time.time())')
    python3 -c "print(f'{$e - $s:.3f}')" >> "times-$L.txt"
    echo "  round $r  $L  $(python3 -c "print(f'{$e - $s:.3f}')") s"
  done
done
echo "########## medians (s for 180 output frames; ms per output frame)"
for L in "${LABELS[@]}"; do
  python3 -c "
import statistics; v = [float(x) for x in open('times-$L.txt').read().split()]; m = statistics.median(v)
print(f'  {\"$L\":8s} {m:7.3f} s   {1000 * m / 180:6.2f} ms/frame   (runs: {v})')"
done
