#!/bin/bash
# MoltenVK REPEATS at the bit level (2026-10-01): BUILDANDUSAGE.md's "outstanding stress test". The Mac wander was
# solved on 2026-09-30 by two MoltenVK switches (tests/mvk-env.sh), measured on the ladder's PSNR to the hundredth.
# The original finding of 2026-08-30 was at the bit level: framemd5, the same render twice, frames that differ. This
# repeats that measurement with MoltenVK's defaults and with the switches, on the paths it used -- stock linear, a
# trivial one-pass hook, the base interpolator -- and on to the recommendation and the player's High tier.
#
#   repeatpairs.sh <outdir> [case...]        (default cases: L0_static L7_textured_large M2_period40)
#   RUNS=8 FFMPEG=... PATHS="linear smoke base rec high" DITHER=<libplacebo dithering: blue (default) | ordered_fixed | none>
#
# Each render is reduced to a SIGNATURE (the md5 of its frames' md5s) and the renders are grouped by it. A first
# version compared runs in pairs and read one odd render as "every frame differs" (2026-10-01): the odd renders are
# whole-render variants, so the question is how many variants there are, how often each comes, and how far an odd
# one is from the majority. For each odd variant: frames that are not bit-identical to the majority render (framemd5),
# and the worst per-frame PSNR between them (a one-LSB texel lands near 90 dB; a warp built on the wrong vector far
# below). The two settings are interleaved run by run, so neither gets a warmer machine. One GPU job at a time.
set -u
OUT="${1:?outdir}"; shift; mkdir -p "$OUT"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SH="$HERE/../shaders"
FF="${FFMPEG:-$HOME/np-build/ffmpeg/ffmpeg}"
RUNS="${RUNS:-8}"
PATHS="${PATHS:-linear smoke base rec high}"
CASES="${*:-L0_static L7_textured_large M2_period40}"
. "$HERE/scenes.sh"
mix() { case "$1" in
  linear) echo "frame_mixer=linear${DITHER:+:dithering=$DITHER}";;
  *)      echo "frame_mixer=custom_n:custom_shader_path=$1.glsl${DITHER:+:dithering=$DITHER}";; esac; }
cp -f "$SH/nframe-smoketest.glsl" "$OUT/smoke.glsl"
cp -f "$SH/bidirectional-interpolation.glsl" "$OUT/base.glsl"
cp -f "$SH/bidirectional-interpolation-variational-propagated.glsl" "$OUT/rec.glsl"
cp -f "$SH/bidirectional-interpolation-variational-propagated-global-cage-energy-carry-adopt-lattice.glsl" "$OUT/high.glsl"
render() {  # <setting> <case> <path> <run>: a lossless file, its framemd5, its signature
  local set=$1 c=$2 p=$3 r=$4 S24 n="$1-$2-$3-$4"
  S24="$(scene "$c" 24)"
  local -a E=(-u MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS -u MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE)
  [ "$set" = on ] && E=(MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS=0 MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE=1)
  ( cd "$OUT" && env "${E[@]}" "$FF" -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk \
      -f lavfi -i "$S24" -vf "libplacebo=fps=60:$(mix "$p"),format=yuv420p" -c:v ffv1 "r-$n.mkv" ) 2> "$OUT/err-$n.txt" \
    || { echo "  RENDER FAILED $n"; head -3 "$OUT/err-$n.txt"; return 1; }
  grep -q "compile status" "$OUT/err-$n.txt" && echo "  $p: A COMPILE ERROR (libplacebo fell back to its own mixer)"
  "$FF" -v error -i "$OUT/r-$n.mkv" -f framemd5 -c:v rawvideo "$OUT/r-$n.md5"
  grep -v '^#' "$OUT/r-$n.md5" | awk -F, '{print $NF}' | md5 | cut -c1-8 > "$OUT/r-$n.sig"
}
printf "%-4s %-18s %-7s %s\n" set case path "variants (renders each); each odd one against the majority: frames differing / total, worst PSNR"
for c in $CASES; do
  [ "$(scene "$c" 24)" = UNKNOWN_CASE ] && { echo "unknown case $c"; continue; }
  for p in $PATHS; do
    for r in $(seq 1 "$RUNS"); do for set in off on; do render "$set" "$c" "$p" "$r" || continue 3; done; done
    for set in off on; do
      line=$(cd "$OUT" && cat r-$set-$c-$p-*.sig | sort | uniq -c | sort -rn | awk '{printf "%s%s(%s)", (NR>1?" ":""), $2, $1}')
      major=$(cd "$OUT" && cat r-$set-$c-$p-*.sig | sort | uniq -c | sort -rn | head -1 | awk '{print $2}')
      mref=""; for r in $(seq 1 "$RUNS"); do [ "$(cat "$OUT/r-$set-$c-$p-$r.sig")" = "$major" ] && { mref=$r; break; }; done
      odd=""
      for v in $(cd "$OUT" && cat r-$set-$c-$p-*.sig | sort -u); do
        [ "$v" = "$major" ] && continue
        for r in $(seq 1 "$RUNS"); do [ "$(cat "$OUT/r-$set-$c-$p-$r.sig")" = "$v" ] && break; done
        res=$(python3 - "$OUT/r-$set-$c-$p-$mref.md5" "$OUT/r-$set-$c-$p-$r.md5" <<'PY'
import sys
a, b = ([l.split(',')[-1].strip() for l in open(f) if not l.startswith('#')] for f in sys.argv[1:])
print(sum(x != y for x, y in zip(a, b)) + abs(len(a) - len(b)), len(a))
PY
)
        "$FF" -v error -i "$OUT/r-$set-$c-$p-$mref.mkv" -i "$OUT/r-$set-$c-$p-$r.mkv" \
          -lavfi "[0:v][1:v]psnr=stats_file=$OUT/p-$set-$c-$p-$r.log" -f null - 2>/dev/null
        w=$(python3 -c "
import re; v=[float(m) for m in re.findall(r'psnr_avg:([0-9.]+)', open('$OUT/p-$set-$c-$p-$r.log').read())]
print(f'{min(v):.2f}' if v else 'inf')")
        odd="$odd  [$v: ${res% *}/${res#* } ${w} dB]"
      done
      printf "%-4s %-18s %-7s %s%s\n" "$set" "$c" "$p" "$line" "$odd"
    done
    rm -f "$OUT"/r-*-"$c"-"$p"-*.mkv
  done
done
