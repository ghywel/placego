#!/bin/bash
# The energy channel's render cost on this Mac, by cost/timing.sh's method: an ffv1 FILE source rendered once (a lavfi
# source is up to 70% of a naive shader time), output to -f null (no encoder timed), the shaders INTERLEAVED over three
# rounds so thermal drift and warm-up cancel. 720p, 24 -> 60, O5_osc_textured over 3 s. One GPU job at a time.
#   ./timing.sh "label:path ..."        the control (vp) is added first
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS="$(cd "$HERE/../.." && pwd)"
NP="${NP_SCRATCH:-$(cd "$TESTS/../../.." && pwd)/np-scratch}"
G="$NP/limb/timing"; mkdir -p "$G"
FF="${FFMPEG:-$HOME/np-build/ffmpeg/ffmpeg}"
. "$TESTS/scenes.sh"
SRC="$G/src.mkv"
if [ ! -s "$SRC" ]; then
  S="$(scene O5_osc_textured 24)"; S="${S//:d=1,/:d=3,}"
  "$FF" -y -hide_banner -loglevel error -f lavfi -i "$S" -c:v ffv1 "$SRC" || exit 1
fi
read -r -a SET <<< "vp:$TESTS/../shaders/bidirectional-interpolation-variational-propagated.glsl ${1:-}"
: > "$G/raw.txt"
for round in 1 2 3; do
  for s in "${SET[@]}"; do
    lab="${s%%:*}"; f="${s#*:}"; cp -f "$f" "$G/_$lab.glsl"
    t0=$(python3 -c 'import time; print(time.time())')
    ( cd "$G" && "$FF" -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk -i src.mkv \
        -vf "libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_$lab.glsl" -f null - ) </dev/null 2>"$G/$lab.err"
    t1=$(python3 -c 'import time; print(time.time())')
    echo "$round $lab $(python3 -c "print(round($t1 - $t0, 3))")" >> "$G/raw.txt"
  done
done
python3 - "$G/raw.txt" <<'PY'
import sys, statistics, collections
d = collections.defaultdict(list)
for ln in open(sys.argv[1]):
    r, lab, s = ln.split(); d[lab].append(float(s))
base = statistics.median(d["vp"])
for lab, v in d.items():
    m = statistics.median(v)
    print(f"  {lab:12} median {m:6.3f} s over {len(v)} rounds ({min(v):.3f}-{max(v):.3f})  x{m / base:.3f} of vp")
PY
