#!/bin/bash
# Measure how much of a shader's output is decided by arithmetic noise rather
# than by the image.
#
#   ./tieprobe.sh [shader-path] [case...]
#
# Renders two ULP-probed builds of the same shader (see tieprobe.py) that differ
# only in the seed of a perturbation far below any meaningful cost difference,
# and reports how much the two outputs disagree. A frame that disagrees is a
# frame whose block match was decided by a tie the estimator had no rule for.
#
# Two numbers, because they answer different questions:
#
#   differ  - frames that are not bit-identical (framemd5). Strict: a single
#             flipped texel counts the whole frame. Answers "is the estimator
#             deterministic under perturbation", which is the property itself.
#   worst   - lowest per-frame PSNR between the two renders, dB. Answers "and
#             does it MATTER", which frame counts cannot. This is the number
#             comparable to the macOS measurements in BUILDANDUSAGE.md, where
#             deviations reached 39 dB -- catastrophic, not cosmetic. A frame
#             that differs in one texel by one LSB lands near 90 dB; a frame
#             whose warp was built on the wrong motion vector lands far below.
#
# Run this on a bit-reproducible platform -- Linux or Windows. It is the local
# stand-in for macOS, where the same perturbation arrives for free from a
# non-reproducible MoltenVK path and needs no probe at all. Confirm first that
# the platform really is reproducible by rendering the UNPROBED shader twice and
# comparing framemd5, or this measures the platform instead of the shader.
#
# Requires: an ffmpeg built against a libplacebo carrying frame-mix-hook.patch.
# Software Vulkan (Mesa lavapipe) is fine; this measures correctness, not speed.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. "$HERE/scenes.sh"

FFMPEG="${FFMPEG:-ffmpeg}"
PYTHON="${PYTHON:-python3}"
SHADER="${1:-$HERE/../bidirectional-interpolation.glsl}"
shift 2>/dev/null || true
OUT="${OUTROOT:-${TMPDIR:-/tmp}}/tieprobe"
EPS="${EPS:-1e-6}"
FRAMES="${FRAMES:-60}"
# Below this, a disagreement is real damage rather than a rounding difference.
HARM="${HARM:-60}"

# The tie-prone content classes, ordered as the macOS measurements ordered them
# (BUILDANDUSAGE.md): static, aperiodic noise, flat interiors, real texture.
CASES="${*:-L0_static M1_noise_large L6_flat_large L7_textured_large}"

mkdir -p "$OUT" || exit 1
"$PYTHON" "$HERE/tieprobe.py" "$SHADER" "$OUT/_probe_a.glsl" 1 "$EPS" || exit 1
"$PYTHON" "$HERE/tieprobe.py" "$SHADER" "$OUT/_probe_b.glsl" 2 "$EPS" || exit 1

echo
printf "%-22s %7s %7s %9s %7s   %s\n" case frames differ worst "<${HARM}dB" "shader: $(basename "$SHADER")"
printf -- "---------------------------------------------------------------------\n"

total=0; totaldiff=0; totalharm=0; globalworst=""
for CASE in $CASES; do
  S24="$(scene "$CASE" 24)"
  if [ "$S24" = "UNKNOWN_CASE" ]; then echo "unknown case: $CASE" >&2; continue; fi
  for v in a b; do
    # Run from $OUT with a bare shader filename: an absolute path inside a
    # filter argument is unusable on Windows (the colon in "C:" is ffmpeg's own
    # option separator) and a POSIX path is unusable by a native binary. Same
    # reasoning as bench.sh, at more length there.
    #
    # ONE output per render, and both numbers derived from it afterwards.
    # Asking a single render for framemd5 and rawvideo together measurably
    # changes the result -- the shader caches flow per source pair, so a second
    # output's effect on frame pacing changes what is cached when. Two outputs
    # moved the count by a frame or two, which is the same size as the effect
    # being measured. Do not "optimise" these back into one command.
    ( cd "$OUT" && "$FFMPEG" -y -hide_banner -loglevel error \
        -init_hw_device vulkan=vk -filter_hw_device vk \
        -f lavfi -i "$S24" \
        -vf "libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_probe_$v.glsl,format=yuv420p" \
        -frames:v "$FRAMES" -c:v rawvideo -f nut "$CASE.$v.nut" ) 2>"$OUT/$CASE.$v.err"
    # framemd5 off the stored frames: no GPU, and identical by construction to
    # what the render would have emitted directly.
    ( cd "$OUT" && "$FFMPEG" -y -hide_banner -loglevel error \
        -i "$CASE.$v.nut" -f framemd5 "$CASE.$v.md5" ) 2>/dev/null
  done
  n=$(grep -c '^[0-9]' "$OUT/$CASE.a.md5" 2>/dev/null || echo 0)
  if [ "$n" = "0" ]; then
    printf "%-22s %7s %7s %9s %7s   see %s\n" "$CASE" - - - - "$OUT/$CASE.a.err"
    head -3 "$OUT/$CASE.a.err" >&2
    continue
  fi
  d=$(diff "$OUT/$CASE.a.md5" "$OUT/$CASE.b.md5" | grep -c '^<' || true)

  worst=inf; harm=0
  if [ "$d" -gt 0 ]; then
    # From $OUT with bare filenames, for the same reason the renders above are:
    # stats_file= is a path embedded in a filter argument, which MSYS2 will not
    # path-convert and a native ffmpeg.exe cannot open in POSIX form.
    ( cd "$OUT" && "$FFMPEG" -y -hide_banner -loglevel error \
        -i "$CASE.a.nut" -i "$CASE.b.nut" \
        -lavfi "psnr=stats_file=$CASE.psnr.log" -f null - ) 2>/dev/null
    read -r worst harm <<<"$(awk -v h="$HARM" '
      match($0, /psnr_y:[0-9.]+/) {
        v = substr($0, RSTART+7, RLENGTH-7) + 0
        if (w == "" || v < w) w = v
        if (v < h) c++
      }
      END { printf "%s %d", (w == "" ? "inf" : sprintf("%.1f", w)), c+0 }
    ' "$OUT/$CASE.psnr.log")"
    if [ "$worst" != inf ]; then
      if [ -z "$globalworst" ] || awk "BEGIN{exit !($worst < $globalworst)}"; then
        globalworst=$worst
      fi
    fi
  fi
  printf "%-22s %7d %7d %9s %7d\n" "$CASE" "$n" "$d" "$worst" "$harm"
  rm -f "$OUT/$CASE.a.nut" "$OUT/$CASE.b.nut"
  total=$((total + n)); totaldiff=$((totaldiff + d)); totalharm=$((totalharm + harm))
done

printf -- "---------------------------------------------------------------------\n"
printf "%-22s %7d %7d %9s %7d\n" TOTAL "$total" "$totaldiff" "${globalworst:-inf}" "$totalharm"
echo
echo "Two seeds of a ${EPS} relative perturbation -- a few float32 ULP, far below"
echo "any real cost difference. 'differ' counts frames the perturbation was"
echo "allowed to decide; 'worst' is how badly the worst of them was decided."
