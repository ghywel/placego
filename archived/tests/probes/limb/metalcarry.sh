#!/bin/bash
# THE CARRY ON METAL (2026-09-28): the lockstep's own picture and ladder checks run the RECOMMENDATION, where the carry
# never engages, so they cannot see whether the carry's scans -- one invocation per line, each writing its own storage,
# read two passes later -- do on the Metal engine what they do on libplacebo. This renders cases where the carry DOES
# engage (V3, B1, both ways) and a few where it must not (L1, O5, V1, M3) through the demo's engine with each graph,
# and through libplacebo with the same GLSL, scored the same way (psnr_y over the interpolated frames, the passthrough
# asserted). The Metal engine is deterministic; libplacebo on this Mac is not (the propagated family's wander), so
# the libplacebo column is the median of three runs.
#
#   QUADDEMO=<NFrameDemo>/.build/release/QuadDemo ./metalcarry.sh <outroot> "label:graphdir:glsl ..." [cases]
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS="$(cd "$HERE/../.." && pwd)"
FF="${FFMPEG:-$HOME/np-build/ffmpeg/ffmpeg}"
PY="${PY:-$HOME/np-build/venv/bin/python3}"
QUAD="${QUADDEMO:?set QUADDEMO to the CLI of the demo engine}"   # (no apostrophe in a :? word: bash 3.2 reads it as a quote)
OUT="${1:?outroot}"; mkdir -p "$OUT"
read -r -a SET <<< "${2:?label:graphdir:glsl ...}"
CASES="${3:-V3_stairs_sq24_v12 V3up B1_alias_over_pan B1up L1_trans_8px O5_osc_textured V1_bars_sine24_v6 M3_period16_trap}"
. "$TESTS/scenes.sh"
# $1 log -> the mean psnr_y over the interpolated frames (analyze.py's rule: n > 5, not a passthrough); the
# passthrough frame (n 1) must read >= 60 dB or the comparison path is broken, and the score says so
SCORER='
import re, sys
d = {}
for ln in open(sys.argv[1]):
    m = re.search(r"psnr_y:([0-9.]+|inf)", ln); n = re.match(r"n:(\d+)", ln)
    if m and n: d[int(n.group(1))] = 99.0 if m.group(1) == "inf" else float(m.group(1))
v = [x for n, x in d.items() if n > 5 and (n - 1) % 5 != 0]
first = d.get(1, 0.0)
print("%.2f" % (sum(v) / len(v)) + ("" if first >= 60 else " PASSTHROUGH-%s" % first))
'
score() { "$PY" -c "$SCORER" "$1"; }
printf "%-26s" case; for s in "${SET[@]}"; do l="${s%%:*}"; printf "%22s" "$l metal|placebo"; done; echo
for C in $CASES; do
  base="$C"; up=""
  case "$C" in *up) base="${C%up}"; [ "$base" = "V3" ] && base=V3_stairs_sq24_v12; [ "$base" = "B1" ] && base=B1_alias_over_pan; up=1;; esac
  S24="$(scene "$base" 24)"; S60="$(scene "$base" 60)"
  case "$S24" in ""|UNKNOWN_CASE*) S24="$(scene_edge "$base" 24)"; S60="$(scene_edge "$base" 60)";; esac
  if [ -n "$up" ]; then          # mirrored as v3phase.sh does it: start 288 px lower, move up
    P1='100+288*T'; P2='100+288*t'
    S24="${S24//"$P1"/388-288*T}"; S60="${S60//"$P1"/388-288*T}"
    S24="${S24//"$P2"/388-288*t}"; S60="${S60//"$P2"/388-288*t}"
  fi
  D="$OUT/$C"; mkdir -p "$D"
  "$FF" -y -v error -f lavfi -i "$S24" -pix_fmt rgb48le -f rawvideo "$D/src24.raw"
  "$FF" -y -v error -f lavfi -i "$S60" -pix_fmt rgb48le -f rawvideo "$D/truth60.raw"
  line="$(printf "%-26s" "$C")"
  for s in "${SET[@]}"; do
    lab="${s%%:*}"; rest="${s#*:}"; g="${rest%%:*}"; glsl="${rest#*:}"
    "$QUAD" --graph "$g" --input "$D/src24.raw" --export "$D/out.raw" --size 1280x720 >/dev/null 2>"$D/$lab.err" \
      || { line="$line $(printf "%22s" "RENDER FAILED")"; continue; }
    ( cd "$D" && "$FF" -y -v error -f rawvideo -pix_fmt rgb48le -video_size 1280x720 -framerate 60 -i out.raw \
        -f rawvideo -pix_fmt rgb48le -video_size 1280x720 -framerate 60 -i truth60.raw \
        -lavfi "[0:v]format=yuv420p[a];[1:v]format=yuv420p[b];[a][b]psnr=stats_file=$lab-metal.log" -f null - ) 2>/dev/null
    rm -f "$D/out.raw"
    m="$(score "$D/$lab-metal.log")"
    cp -f "$glsl" "$D/_$lab.glsl"
    pv=""
    for run in 1 2 3; do
      ( cd "$D" && "$FF" -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk \
          -f lavfi -i "$S24" -f lavfi -i "$S60" \
          -filter_complex "[0:v]libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_$lab.glsl[ip];[ip]format=yuv420p[i2];[i2][1:v]psnr=stats_file=$lab-pl$run.log[o]" \
          -map "[o]" -f null - ) </dev/null 2>/dev/null
      pv="$pv $(score "$D/$lab-pl$run.log" | cut -d' ' -f1)"
    done
    p="$(echo $pv | tr ' ' '\n' | sort -n | sed -n 2p)"
    line="$line $(printf "%22s" "$m | $p")"
  done
  rm -f "$D/src24.raw" "$D/truth60.raw" "$D"/._*
  echo "$line"
done
