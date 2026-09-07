#!/bin/bash
# A genuine "I want to watch this interpolated" render, in one command: a stretch of real footage through a
# shipped shader to 60 fps, as a playable mp4 in the renders folder. Not a test; no truth, no numbers.
#
#   ./watch.sh <source> <start-seconds> <minutes> [shader] [label]
#
# shader defaults to the recommended picture shader (bidirectional-interpolation-variational-propagated.glsl);
# for cel-animated content use bidirectional-interpolation-animation.glsl; for 4K sources use
# bidirectional-interpolation-variational-propagated-4k.glsl. The output goes to $HOTDROPS (default
# E:/nframe-project/hot-drops) as watch-<label>-60fps.mp4; the label defaults to the shader's short name,
# so the file never carries the source's title. Full source resolution, H.264, at a bitrate that scales
# with the frame: 12 Mbit/s at 1080p, four times that at 4K, capped at 48 (BITRATE_M overrides, in Mbit/s).
# Ten-bit sources are rendered at ten bits and delivered at eight (the encoder's format).
#
# Paths with brackets ([TGx] and the like) defeat the MSYS shell's path conversion, so the source is
# passed to ffmpeg in Windows form via cygpath when that is available.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FFMPEG="${FFMPEG:-ffmpeg}"
FFPROBE="${FFPROBE:-ffprobe}"
SRC="${1:?usage: watch.sh <source> <start-seconds> <minutes> [shader] [label]}"
START="${2:?start seconds}"; MIN="${3:?minutes}"
SHADER="${4:-$HERE/../shaders/bidirectional-interpolation-variational-propagated.glsl}"
LABEL="${5:-$(basename "$SHADER" .glsl | sed 's/bidirectional-interpolation-//; s/interpolation-//')}"
OUT="${HOTDROPS:-E:/nframe-project/hot-drops}"
W="${TMPDIR:-/tmp}/interp-watch"; mkdir -p "$W" "$OUT"
cp -f "$SHADER" "$W/_watch.glsl" || exit 1
command -v cygpath >/dev/null 2>&1 && SRCW="$(cygpath -w "$SRC")" || SRCW="$SRC"
DUR=$(awk -v m="$MIN" 'BEGIN{printf "%.0f", m * 60}')
DIMS=$("$FFPROBE" -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$SRCW" 2>/dev/null | head -1)
PW="${DIMS%%,*}"; PH="${DIMS##*,}"
BR="${BITRATE_M:-$(awk -v w="${PW:-1920}" -v h="${PH:-1080}" 'BEGIN{b = 12 * w * h / 2073600; if (b < 12) b = 12; if (b > 48) b = 48; printf "%d", b}')}"
MAXR=$(awk -v b="$BR" 'BEGIN{printf "%d", b * 4 / 3}')
echo "watch: ${MIN} min from ${START}s through $(basename "$SHADER") at ${PW:-?}x${PH:-?}, ${BR} Mbit/s -> $OUT/watch-$LABEL-60fps.mp4"
( cd "$W" && "$FFMPEG" -y -hide_banner -loglevel error -stats -init_hw_device vulkan=vk -filter_hw_device vk \
    -ss "$START" -t "$DUR" -i "$SRCW" -sn \
    -vf "libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_watch.glsl,format=yuv420p" \
    -c:v h264_mf -b:v "${BR}M" -maxrate "${MAXR}M" -c:a aac -b:a 192k -movflags +faststart "$OUT/watch-$LABEL-60fps.mp4" ) 2>"$W/watch.err" \
  && echo "done: $(stat -c %s "$OUT/watch-$LABEL-60fps.mp4") bytes" || { echo "failed:"; tail -3 "$W/watch.err"; exit 1; }
