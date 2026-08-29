#!/bin/bash
# Screen a source video for segments carrying genuine per-frame motion.
#
#   ./screen.sh <source-video> [seconds...]
#
# Animation is frequently drawn "on twos" -- each drawing held for 2 video
# frames -- and often switches between twos and ones WITHIN one episode
# (dialogue on twos, action on ones). A segment on twos is useless for
# decimate-and-reconstruct benchmarking: half the frames the interpolator is
# asked to reconstruct are duplicates of frames it was already given, which
# flatters every mode equally and hides real differences.
#
# Held drawings do NOT show as byte-identical, because lossy re-encoding
# perturbs them -- they show as very high PSNR against the previous frame.
# So compare frame n against frame n-1 and look at the distribution.
set -u
FFMPEG="${FFMPEG:-ffmpeg}"
SRC="${1:?usage: screen.sh <source-video> [seconds...]}"
shift
CANDS="${*:-30 60 90 120 150 180 210 240 270 300 330 360 390 420}"
RATE="${RATE:-24000/1001}"
T="${TMPDIR:-/tmp}/interp-screen"
mkdir -p "$T"

printf "%8s %10s %12s  %s\n" "start" "held/71" "median dB" "verdict"
for s in $CANDS; do
  "$FFMPEG" -y -hide_banner -loglevel error -ss "$s" -t 3 -i "$SRC" -map 0:v:0 \
    -filter_complex "[0:v]split=2[x][y];[x]select='gte(n\,1)',setpts=N/TB,format=yuv420p[a];[y]select='lt(n\,71)',setpts=N/TB,format=yuv420p[b];[a][b]psnr=stats_file=$T/d_$s.log[o]" \
    -map "[o]" -f null - 2>/dev/null || continue
  python3 - "$s" "$T" <<'PY'
import sys, os, re, statistics
s, T = sys.argv[1], sys.argv[2]
p = os.path.join(T, f"d_{s}.log")
v = []
for line in open(p):
    m = re.search(r"psnr_y:([0-9.]+|inf)", line)
    if m:
        v.append(999.0 if m.group(1) == "inf" else float(m.group(1)))
if not v:
    sys.exit()
held = sum(1 for x in v if x > 45)
verdict = ("ON TWOS - avoid" if held > len(v) * 0.3 else
           "some holds" if held > len(v) * 0.1 else "GOOD - full motion")
print(f"{s:>8} {held:>6}/{len(v):<3} {statistics.median(v):>12.2f}  {verdict}")
PY
done
echo
echo "Pick 'GOOD - full motion' segments for realbench.sh. A high median dB"
echo "means little changes between frames; low means lots of motion."
