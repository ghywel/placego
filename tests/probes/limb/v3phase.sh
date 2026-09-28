#!/bin/bash
# V3 (square stairs, 24-px period, moving 12 px a frame: half a period, so the patch interior cannot tell up from
# down and only its edges can) started at several offsets against the coarse grid: does the COMMITTED shader keep the
# right basin at every start, or does its score depend on the start? (limblevels' per-frame view found the energy
# channel's V3 loss to be a basin flip at frame 11 held for the rest of the clip.) Whole-frame PSNR Y against the
# 60-fps truth over the interpolated frames, as bench.sh scores; three runs per start (the Mac wanders).
#   ./v3phase.sh "label:path ..." [case law base step]   default V3_stairs_sq24_v12 '100+288*T' 100 4
#   (any _rect ladder case: its position law as scenes.sh writes it, the law's base offset, the offset step)
#   ./v3phase.sh "..." B1_alias_over_pan '100+288*t' 100 4     an edge case (scene_edge; overlay's law is in t)
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS="$(cd "$HERE/../.." && pwd)"
NP="${NP_SCRATCH:-$(cd "$TESTS/../../.." && pwd)/np-scratch}"
G="$NP/limb/v3phase"; mkdir -p "$G"
FF="${FFMPEG:-$HOME/np-build/ffmpeg/ffmpeg}"
. "$TESTS/scenes.sh"
read -r -a SET <<< "vp:$TESTS/../shaders/bidirectional-interpolation-variational-propagated.glsl ${1:-}"
CASE="${2:-V3_stairs_sq24_v12}"; LAW="${3:-100+288*T}"; BASE="${4:-100}"; STEP="${5:-4}"
REST="${LAW#"$BASE"}"                       # '+288*T'
for i in 0 1 2 3 4 5; do
  off=$(( BASE + i * STEP ))
  S24="$(scene "$CASE" 24)"; S60="$(scene "$CASE" 60)"
  case "$S24" in ""|UNKNOWN_CASE*) S24="$(scene_edge "$CASE" 24)"; S60="$(scene_edge "$CASE" 60)";; esac   # an edge case
  [ "${S24/"$LAW"/}" != "$S24" ] || { echo "law $LAW not found in $CASE"; exit 1; }
  NEW="$off$REST"
  # UP=1: the same motion mirrored (the patch starts 288 px lower and moves UP), so a tie broken by the sign of
  # the search's scan order shows itself: a mechanism that holds V3 moving down and loses it moving up is a coin
  # that happens to land on one face
  [ -n "${UP:-}" ] && NEW="$((off + 288))${REST/+/-}"
  S24="${S24//"$LAW"/$NEW}"; S60="${S60//"$LAW"/$NEW}"
  line="$CASE start $off${UP:+ (up)}:"
  for s in "${SET[@]}"; do
    lab="${s%%:*}"; f="${s#*:}"; cp -f "$f" "$G/_$lab.glsl"
    vals=""
    for run in 1 2 3; do
      ( cd "$G" && "$FF" -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk -f lavfi -i "$S24" -f lavfi -i "$S60" \
          -filter_complex "[0:v]libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_$lab.glsl[ip];[ip]format=yuv420p[i2];[i2][1:v]psnr=stats_file=$lab-$CASE-$off${UP:+up}-$run.log[o]" -map "[o]" -f null - ) </dev/null 2>/dev/null
      v=$(python3 -c "
import re
d={}
for ln in open('$G/$lab-$CASE-$off${UP:+up}-$run.log'):
    m=re.search(r'psnr_y:([0-9.]+|inf)',ln); n=re.match(r'n:(\d+)',ln)
    if m and n: d[int(n.group(1))]=99.0 if m.group(1)=='inf' else float(m.group(1))
v=[x for n,x in d.items() if n>5 and (n-1)%5!=0]
print(round(sum(v)/len(v),2))")
      vals="$vals $v"
    done
    line="$line   $lab [$vals ]"
  done
  echo "$line"
done
