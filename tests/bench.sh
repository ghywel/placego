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
SHADER_DEFAULT="$HERE/../shaders/bidirectional-interpolation.glsl"

run_case() {
  local CASE="$1" SHADER="$2" LABEL="$3"
  local OUT="$OUTROOT/$CASE"
  mkdir -p "$OUT"

  local S24 S60
  S24="$(scene "$CASE" 24)"; S60="$(scene "$CASE" 60)"
  if [ "$S24" = "UNKNOWN_CASE" ]; then echo "unknown case: $CASE" >&2; return 2; fi

  # A path embedded INSIDE a filter argument is a portability trap, and both
  # the stats file and the shader are embedded. On Windows, MSYS2 does not
  # path-convert them -- its heuristic only fires on standalone arguments --
  # so a POSIX path reaches a native ffmpeg.exe that cannot open it. Converting
  # it would be no better: the colon in "C:" is ffmpeg's own option separator,
  # so the parser splits the argument and reports "No option name near ...".
  # Escaping the colon, quoting the value, and disabling conversion were all
  # measured and all fail. A RELATIVE path is the only form that works, and it
  # behaves identically on Linux -- so run from $OUT and make both relative.
  # Computing a relative path is not enough on MSYS2, because its POSIX root
  # "/" is C:\msys64 while "/c" is a virtual mount of C:\ -- so a POSIX
  # relative path between the two is meaningless to a native ffmpeg.exe. The
  # reliable answer is to remove the path entirely: copy the shader next to
  # the output and refer to it by bare name. Shaders are single self-contained
  # files with no includes, so a copy is exact, and it costs a few hundred KB.
  local SHREL="$SHADER"
  if [ -f "$SHADER" ] && cp -f "$SHADER" "$OUT/_shader.glsl" 2>/dev/null; then
    SHREL=_shader.glsl
  fi

  _run() { # <mode> <filter-chain> <needs-vulkan>
    local mode="$1" chain="$2" hw=""
    [ "$3" = "vk" ] && hw="-init_hw_device vulkan=vk -filter_hw_device vk"
    # shellcheck disable=SC2086
    ( cd "$OUT" && "$FFMPEG" -y -hide_banner -loglevel error $hw \
      -f lavfi -i "$S24" -f lavfi -i "$S60" \
      -filter_complex "[0:v]${chain}[ip];[ip]format=yuv420p[i2];[i2][1:v]psnr=stats_file=$mode.log[o]" \
      -map "[o]" -f null - ) 2>"$OUT/$mode.err" \
      && echo "  $mode ok" || echo "  $mode FAILED (see $OUT/$mode.err)"
  }

  # Baselines are properties of the content, not the shader, so only compute
  # them once per case rather than on every shader variant re-run.
  [ -s "$OUT/hold.log" ]   || _run hold   "fps=60"                               sw
  [ -s "$OUT/linear.log" ] || _run linear "libplacebo=fps=60:frame_mixer=linear"  vk
  _run "$LABEL" "libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=$SHREL" vk
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
