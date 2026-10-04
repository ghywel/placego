#!/bin/bash
# THE TIME OF A SET OF SHADERS (2026-10-01, the trust gate's cost): probes/cost/timing.sh's method for any number of labels --
# an ffv1 FILE source (made once from SRC), -f null (no encoder), every label INTERLEAVED over the rounds so thermal drift
# and warm-up cancel, linear beside as the pipeline's floor. 24 -> 60. MoltenVK's defaults (a timing run: this script does
# not source mvk-env.sh). One GPU job at a time; run alone.
#
#   timeset.sh <outdir> <src: a .raw gray16le 1280x720 24 fps, or a video> "<label>:<glsl> ..." [rounds=3]
# A video is cut to 3 s from 10 s in at 1280x720, 24 fps; a .raw is taken whole up to 3 s.
set -u
OUT="${1:?outdir}"; SRC="${2:?source}"; SET="${3:?label:path ...}"; ROUNDS="${4:-3}"
FF="${FFMPEG:-$HOME/np-build/ffmpeg/ffmpeg}"
mkdir -p "$OUT"; cd "$OUT" || exit 1
S="src-$(basename "${SRC%.*}").mkv"
if [ ! -s "$S" ]; then
  case "$SRC" in
    *.raw) "$FF" -y -hide_banner -loglevel error -f rawvideo -pix_fmt gray16le -s 1280x720 -r 24 -i "$SRC" -t 3 -c:v ffv1 "$S" || exit 1 ;;
    *)     "$FF" -y -hide_banner -loglevel error -ss 10 -i "$SRC" -t 3 -an -vf "scale=1280:720,fps=24" -c:v ffv1 "$S" || exit 1 ;;
  esac
fi
read -r -a L <<< "linear:- $SET"
for e in "${L[@]}"; do n="${e%%:*}"; [ "$n" = linear ] || cp -f "${e#*:}" "$n.glsl"; : > "t-$n.txt"; done
now() { python3 -c 'import time; print(time.time())'; }
echo "#### $(date +%T) $S, $ROUNDS rounds, interleaved"
for r in $(seq 1 "$ROUNDS"); do
  for e in "${L[@]}"; do
    n="${e%%:*}"
    if [ "$n" = linear ]; then MIX="frame_mixer=linear"; else MIX="frame_mixer=custom_n:custom_shader_path=$n.glsl"; fi
    s=$(now)
    "$FF" -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk -i "$S" \
      -vf "format=yuv420p,libplacebo=fps=60:$MIX" -f null - 2> "err-$n.txt" || echo "  $n FAILED"
    grep -q "compile status" "err-$n.txt" && echo "  $n: A COMPILE ERROR (libplacebo fell back to its own mixer)"
    python3 -c "print(f'{$(now) - $s:.3f}')" >> "t-$n.txt"
  done
done
for e in "${L[@]}"; do
  n="${e%%:*}"
  python3 -c "
import statistics; v = [float(x) for x in open('t-$n.txt').read().split()]; m = statistics.median(v)
print(f'  {\"$n\":12s} {1000 * m / 180:6.2f} ms/frame   (runs, s: {v})')"
done
