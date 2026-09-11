#!/usr/bin/env bash
# The round-trip on unified memory, in the record's own terms, re-runnable on any Mac (2026-09-11).
#
#   ./readback.sh <clip.mp4> [shader.glsl] [seconds]
#       default shader: ../../../shaders/tridirectional-interpolation-propagated.glsl; default 20 s of input
#   data: $NP_SCRATCH/uma/
#
# BUILDANDUSAGE.md § "Unified memory: the round-trip stops mattering" measured four chains on the M2 by hand
# (the commands were logged on that machine and quoted in the doc); this is the same measurement as a script,
# so the table can gain a column per machine. 24 -> 60 at the clip's native size, software decode (the
# videotoolbox <-> vulkan derive is ENOSYS, so every chain pays the same decode), ffmpeg's own end-of-run fps:
#
#   shader, downloaded each frame    libplacebo=...            -f null -      (the API-level round trip every frame)
#   shader, kept in Vulkan           libplacebo=...,format=vulkan             (no readback at all)
#   linear, downloaded               frame_mixer=linear
#   linear, kept                     frame_mixer=linear,format=vulkan
#
# The readback penalty -- downloaded against kept -- is the number. On a discrete GPU behind a bus it was 35 %
# on the shader path and 60 % on linear (RX 6600 over Thunderbolt); on the M2 it read 0 within noise and 22 %.
# Interleaved (never A-then-B: feedback_harness_traps), two rounds after a warm-up, the median reported.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS="$(cd "$HERE/../.." && pwd)"
export PATH="/opt/homebrew/bin:$PATH"
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"
FFMPEG="${FFMPEG:-$([ -x "$FFDIR/ffmpeg" ] && echo "$FFDIR/ffmpeg" || echo ffmpeg)}"
NP_SCRATCH="${NP_SCRATCH:-$(cd "$TESTS/../.." && pwd)/../np-scratch}"
OUT="$NP_SCRATCH/uma"; mkdir -p "$OUT"
CLIP="${1:?usage: readback.sh <clip.mp4> [shader.glsl] [seconds]}"
CLIP="$(cd "$(dirname "$CLIP")" && pwd)/$(basename "$CLIP")"
SHADER="${2:-$TESTS/../shaders/tridirectional-interpolation-propagated.glsl}"
SECS="${3:-20}"
[ -f "$CLIP" ] || { echo "no clip at $CLIP"; exit 1; }
[ -f "$SHADER" ] || { echo "no shader at $SHADER"; exit 1; }
cp -f "$SHADER" "$OUT/_shader.glsl"
cd "$OUT" || exit 1

run() { # <label> <filter chain> -> fps
  local label="$1" chain="$2"
  local err="$OUT/$label.err"          # its own statement: bash 3.2 (macOS) does not see $label within the same `local`
  "$FFMPEG" -y -hide_banner -loglevel info -stats -init_hw_device vulkan=vk -filter_hw_device vk \
    -t "$SECS" -i "$CLIP" -vf "$chain" -an -f null - 2> "$err"
  if grep -q "compile status .error" "$err"; then echo "  $label: SHADER COMPILE ERROR (see $err)"; return 1; fi
  tr '\r' '\n' < "$err" | grep -oE 'fps= *[0-9.]+' | tail -1 | grep -oE '[0-9.]+'
}

S="libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_shader.glsl"
L="libplacebo=fps=60:frame_mixer=linear"
declare -a LABELS=(shader_downloaded shader_kept linear_downloaded linear_kept)
declare -a CHAINS=("$S" "$S,format=vulkan" "$L" "$L,format=vulkan")

echo "clip    $CLIP"
echo "shader  $(basename "$SHADER")   input $SECS s, 24->60 at native size, $($FFMPEG -version | head -1 | cut -d' ' -f3)"
echo "warm-up"; run warmup "$L" > /dev/null
declare -a R1 R2          # indexed: macOS bash 3.2 has no -A
for round in 1 2; do
  for i in 0 1 2 3; do
    f="$(run "${LABELS[$i]}" "${CHAINS[$i]}")" || f="FAILED"
    [ "$round" = 1 ] && R1[$i]="$f" || R2[$i]="$f"
    printf '  round %d  %-18s %8s fps\n' "$round" "${LABELS[$i]}" "$f"
  done
done
echo
printf '%-22s %10s %10s %10s\n' "chain" "round 1" "round 2" "median"
for i in 0 1 2 3; do
  med="$(python3 -c "import sys; a=sorted(float(x) for x in sys.argv[1:]); print('%.1f' % ((a[0]+a[1])/2))" "${R1[$i]}" "${R2[$i]}" 2>/dev/null || echo "?")"
  printf '%-22s %10s %10s %10s\n' "${LABELS[$i]}" "${R1[$i]}" "${R2[$i]}" "$med"
done
python3 - "${R1[0]}" "${R2[0]}" "${R1[1]}" "${R2[1]}" "${R1[2]}" "${R2[2]}" "${R1[3]}" "${R2[3]}" <<'PY'
import sys
v = [float(x) for x in sys.argv[1:]]
med = lambda a, b: (a + b) / 2
sd, sk, ld, lk = med(v[0], v[1]), med(v[2], v[3]), med(v[4], v[5]), med(v[6], v[7])
print()
print("readback penalty, shader path: %+.1f %%   (downloaded %.1f vs kept %.1f fps)" % (100 * (sk - sd) / sk, sd, sk))
print("readback penalty, linear path: %+.1f %%   (downloaded %.1f vs kept %.1f fps)" % (100 * (lk - ld) / lk, ld, lk))
print("(RX 6600 over Thunderbolt: 35 % and 60 %; M2: 0 within noise and 22 %; M5 2026-09-11: +2 % and 38 %)")
PY
echo "READBACK DONE"
