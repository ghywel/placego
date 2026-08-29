#!/bin/bash
# Render inspectable frames for one benchmark case: what the shader produced,
# what it should have produced, and an amplified difference between them.
#
#   ./visuals.sh <case-name> [shader-path] [frame-number]
#
# Frame 23 by default: mid-interval (not one of the every-5th passthrough
# frames) and past the startup frame-hold.
#
# Point [shader-path] at interpolate-debug-grid.glsl instead to get the flow
# field itself rather than the final image -- that is how the ambiguous-
# texture failure in TESTING.md was localised.

set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. "$HERE/scenes.sh"

FFMPEG="${FFMPEG:-ffmpeg}"
OUTROOT="${OUTROOT:-${TMPDIR:-/tmp}/interp-bench}"

CASE="${1:?usage: visuals.sh <case> [shader] [frame-n]}"
SHADER="${2:-$HERE/../bidirectional-interpolation.glsl}"
N="${3:-23}"
OUT="$OUTROOT/$CASE"
mkdir -p "$OUT"

S24="$(scene "$CASE" 24)"; S60="$(scene "$CASE" 60)"
[ "$S24" = "UNKNOWN_CASE" ] && { echo "unknown case: $CASE" >&2; exit 2; }

# what the shader produced
"$FFMPEG" -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk \
  -f lavfi -i "$S24" \
  -filter_complex "[0:v]libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=$SHADER,format=yuv420p,select='eq(n\,$N)'[o]" \
  -map "[o]" -fps_mode passthrough -frames:v 1 -q:v 2 "$OUT/shader.jpg" 2>/dev/null

# what it should have produced
"$FFMPEG" -y -hide_banner -loglevel error \
  -f lavfi -i "$S60" \
  -filter_complex "[0:v]select='eq(n\,$N)'[o]" \
  -map "[o]" -fps_mode passthrough -frames:v 1 -q:v 2 "$OUT/truth.jpg" 2>/dev/null

# amplified |shader - truth|
"$FFMPEG" -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk \
  -f lavfi -i "$S24" -f lavfi -i "$S60" \
  -filter_complex "[0:v]libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=$SHADER,format=yuv420p[a];[a][1:v]blend=all_mode=difference,eq=gamma=1.5:contrast=4.0,select='eq(n\,$N)'[o]" \
  -map "[o]" -fps_mode passthrough -frames:v 1 -q:v 2 "$OUT/diff.jpg" 2>/dev/null

# stock linear blend, for side-by-side comparison
"$FFMPEG" -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk \
  -f lavfi -i "$S24" \
  -filter_complex "[0:v]libplacebo=fps=60:frame_mixer=linear,format=yuv420p,select='eq(n\,$N)'[o]" \
  -map "[o]" -fps_mode passthrough -frames:v 1 -q:v 2 "$OUT/linear.jpg" 2>/dev/null

echo "wrote: $OUT/{shader,truth,diff,linear}.jpg"
