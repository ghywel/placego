#!/bin/bash
# The control that must NOT move: an ordinary interpolated render through the picture path (read_view 0,
# TRI_DIAG 0). The edited line is guarded by `TRI_DIAG != 0`, so this must be byte-identical across the fix.
set -u
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs
export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH"
SC="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; G="$NP/anchor"
. "$SC/tests/scenes.sh"
S="$(scene O5_osc_textured 24)"
cp -f "$SC/shaders/quaddirectional-interpolation-propagated.glsl" "$G/_pic.glsl"
( cd "$G" && ffmpeg.exe -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk \
    -f lavfi -i "$S" -vf "libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_pic.glsl,format=rgb48le" \
    -frames:v 40 -f rawvideo "$G/picture_$1.raw" ) 2>"$G/err_pic_$1"
echo "  picture_$1.raw: $(stat -c %s "$G/picture_$1.raw") bytes  md5 $(md5sum "$G/picture_$1.raw" | cut -c1-32)"
