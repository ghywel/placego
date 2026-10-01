#!/bin/bash
# The residual after the MoltenVK switches (2026-10-01): now and then a whole render comes out one or two levels off
# on every frame (60/60 frames, 63-68 dB, chroma-heavy), with the SAME signature with the switches on or off: a
# second fixed state, not noise. libplacebo dithers its 8-bit output with a blue-noise lookup texture by default;
# `ordered_fixed` needs no texture and `none` does not dither. N renders of stock linear per method, switches on,
# grouped by whole-render signature. If blue shows the odd state and the other two never do, the dither texture is it.
#
#   dithervariants.sh <outdir> [case=L0_static]      N=40 METHODS="blue ordered_fixed none"
set -u
OUT="${1:?outdir}"; C="${2:-L0_static}"; mkdir -p "$OUT"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
FF="${FFMPEG:-$HOME/np-build/ffmpeg/ffmpeg}"; N="${N:-40}"; METHODS="${METHODS:-blue ordered_fixed none}"
. "$HERE/scenes.sh"; . "$HERE/mvk-env.sh"
S24="$(scene "$C" 24)"
for r in $(seq 1 "$N"); do
  for m in $METHODS; do                       # interleaved, so no method gets a warmer machine
    "$FF" -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk -f lavfi -i "$S24" \
      -vf "libplacebo=fps=60:frame_mixer=linear:dithering=$m,format=yuv420p" -f framemd5 -c:v rawvideo - 2>/dev/null \
      | grep -v '^#' | awk -F, '{print $NF}' | md5 | cut -c1-8 >> "$OUT/$C-$m.sigs"
  done
done
for m in $METHODS; do
  echo "$C $m: $(sort "$OUT/$C-$m.sigs" | uniq -c | sort -rn | awk '{printf "%s(%s) ", $2, $1}')"
done
