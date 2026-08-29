#!/bin/bash
# Ground-truth benchmark for a PL_HOOK_FRAME_MIX interpolation shader.
#
#   ./bench.sh <case-name> [shader-path] [output-label]
#   ./bench.sh all         [shader-path]
#
# See TESTING.md for what this measures and why. In short: for the synthetic
# scenes in scenes.sh, a native 60fps render is the exact correct answer for
# a 24->60 interpolation of the 24fps render, so error is measurable.
#
# Three modes are always compared, because a PSNR figure on its own says
# nothing about whether a motion-compensated shader is worth its cost:
#
#   hold   - zero-order hold (frame duplication). No interpolation. The floor.
#   linear - stock libplacebo linear blend. What you get WITHOUT this project.
#   shader - the shader under test. Must clearly beat 'linear' to be earning
#            its complexity.
#
# Requires: an ffmpeg built against a libplacebo carrying frame-mix-hook.patch
# (see ../README.md). Software Vulkan (Mesa lavapipe) is fine and needs no
# GPU -- this measures correctness, not speed. Set FFMPEG= to point at it.

set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. "$HERE/scenes.sh"

FFMPEG="${FFMPEG:-ffmpeg}"
OUTROOT="${OUTROOT:-${TMPDIR:-/tmp}/interp-bench}"
SHADER_DEFAULT="$HERE/../bidirectional-interpolation.glsl"

run_case() {
  local CASE="$1" SHADER="$2" LABEL="$3"
  local OUT="$OUTROOT/$CASE"
  mkdir -p "$OUT"

  local S24 S60
  S24="$(scene "$CASE" 24)"; S60="$(scene "$CASE" 60)"
  if [ "$S24" = "UNKNOWN_CASE" ]; then echo "unknown case: $CASE" >&2; return 2; fi

  _run() { # <mode> <filter-chain> <needs-vulkan>
    local mode="$1" chain="$2" hw=""
    [ "$3" = "vk" ] && hw="-init_hw_device vulkan=vk -filter_hw_device vk"
    # shellcheck disable=SC2086
    "$FFMPEG" -y -hide_banner -loglevel error $hw \
      -f lavfi -i "$S24" -f lavfi -i "$S60" \
      -filter_complex "[0:v]${chain}[ip];[ip]format=yuv420p[i2];[i2][1:v]psnr=stats_file=$OUT/$mode.log[o]" \
      -map "[o]" -f null - 2>"$OUT/$mode.err" \
      && echo "  $mode ok" || echo "  $mode FAILED (see $OUT/$mode.err)"
  }

  # Baselines are properties of the content, not the shader, so only compute
  # them once per case rather than on every shader variant re-run.
  [ -s "$OUT/hold.log" ]   || _run hold   "fps=60"                               sw
  [ -s "$OUT/linear.log" ] || _run linear "libplacebo=fps=60:frame_mixer=linear"  vk
  _run "$LABEL" "libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=$SHADER" vk
}

CASE="${1:?usage: bench.sh <case|all> [shader] [label]}"
SHADER="${2:-$SHADER_DEFAULT}"
LABEL="${3:-shader}"

if [ "$CASE" = "all" ]; then
  for c in $ALL_CASES; do echo "=== $c ==="; run_case "$c" "$SHADER" "$LABEL"; done
else
  run_case "$CASE" "$SHADER" "$LABEL"
fi
echo "results under $OUTROOT -- summarise with: ./analyze.py"
