#!/bin/bash
# A handful of ladder or edge cases through a set of shaders on libplacebo, RUNS runs each, the mean psnr_y over the
# interpolated frames as bench.sh scores them -- the quick look between a gate's reading and the next gate, when a few
# cases moved and the question is which part of a change moved them. Cases named with an "up" suffix (V3up, B1up)
# are the mirrored motion, as v3phase.sh's UP=1 makes it.
#   RUNS=2 ./cases.sh "label:path ..." A6_accel_tex_a133 O5_osc_textured B1up ...
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS="$(cd "$HERE/../.." && pwd)"
NP="${NP_SCRATCH:-$(cd "$TESTS/../../.." && pwd)/np-scratch}"
G="$NP/limb/cases"; mkdir -p "$G"
FF="${FFMPEG:-$HOME/np-build/ffmpeg/ffmpeg}"
PY="${PY:-$HOME/np-build/venv/bin/python3}"
RUNS="${RUNS:-2}"
read -r -a SET <<< "$1"; shift
. "$TESTS/scenes.sh"
SCORER='
import re, sys
d = {}
for ln in open(sys.argv[1]):
    m = re.search(r"psnr_y:([0-9.]+|inf)", ln); n = re.match(r"n:(\d+)", ln)
    if m and n: d[int(n.group(1))] = 99.0 if m.group(1) == "inf" else float(m.group(1))
v = [x for n, x in d.items() if n > 5 and (n - 1) % 5 != 0]
print("%.2f" % (sum(v) / len(v)))
'
printf "%-22s" case; for s in "${SET[@]}"; do printf "%16s" "${s%%:*}"; done; echo
for C in "$@"; do
  base="$C"; up=""
  case "$C" in V3up) base=V3_stairs_sq24_v12; up=1;; B1up) base=B1_alias_over_pan; up=1;; esac
  S24="$(scene "$base" 24)"; S60="$(scene "$base" 60)"
  case "$S24" in ""|UNKNOWN_CASE*) S24="$(scene_edge "$base" 24)"; S60="$(scene_edge "$base" 60)";; esac
  if [ -n "$up" ]; then
    P1='100+288*T'; P2='100+288*t'
    S24="${S24//"$P1"/388-288*T}"; S60="${S60//"$P1"/388-288*T}"
    S24="${S24//"$P2"/388-288*t}"; S60="${S60//"$P2"/388-288*t}"
  fi
  line="$(printf "%-22s" "$C")"
  for s in "${SET[@]}"; do
    lab="${s%%:*}"; cp -f "${s#*:}" "$G/_$lab.glsl"; tot=""
    for run in $(seq 1 "$RUNS"); do
      ( cd "$G" && "$FF" -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk \
          -f lavfi -i "$S24" -f lavfi -i "$S60" \
          -filter_complex "[0:v]libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_$lab.glsl[ip];[ip]format=yuv420p[i2];[i2][1:v]psnr=stats_file=$lab-$C-$run.log[o]" \
          -map "[o]" -f null - ) </dev/null 2>/dev/null
      tot="$tot $("$PY" -c "$SCORER" "$G/$lab-$C-$run.log")"
    done
    line="$line $(printf "%15s" "$("$PY" -c "import sys; v=[float(x) for x in sys.argv[1:]]; print('%.2f' % (sum(v)/len(v)))" $tot)")"
  done
  echo "$line"
done
