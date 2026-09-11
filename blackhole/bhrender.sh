#!/bin/bash
# The black hole: encode the traced frames to an mp4 for the eyes, then put it through the human reading
# (picture | velocity, auto scale, the propagated quad at N:N) as a second file.
set -u
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs
export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH"
SC="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; G="$NP/eyes/blackhole"; HD="${HOT_DROPS:-/e/nframe-project/hot-drops}"
cd "$G"
echo "########## BHRENDER start $(date +%T)"
ffmpeg.exe -y -hide_banner -loglevel error -f rawvideo -pix_fmt rgb24 -s 1280x720 -r 24 -i full/frames.rgb -vf format=yuv420p -c:v h264_mf -b:v 16M -movflags +faststart "$HD/blackhole-disc-10s.mp4" && echo "  picture: $(stat -c %s "$HD/blackhole-disc-10s.mp4") bytes"
ffmpeg.exe -y -hide_banner -loglevel error -f rawvideo -pix_fmt rgb24 -s 1280x720 -r 24 -i full/frames.rgb -frames:v 1 -update 1 -vf "select='eq(n\,120)'" "$HD/blackhole-disc-frame120.png" && echo "  still written"
sed '/^\/\/!PARAM read_view/,/^$/ s/^0$/1/' "$SC/shaders/quaddirectional-interpolation-propagated.glsl" > read1.glsl
ffmpeg.exe -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk -i "$HD/blackhole-disc-10s.mp4" -i "$HD/blackhole-disc-10s.mp4" \
  -filter_complex "[0:v]format=yuv420p[a];[1:v]libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=read1.glsl[b];[a][b]hstack=inputs=2,format=yuv420p[o]" \
  -map "[o]" -r 24 -c:v h264_mf -b:v 20M -movflags +faststart "$HD/blackhole-disc-picture-velocityreading.mp4" 2>err_read \
  && echo "  reading: $(stat -c %s "$HD/blackhole-disc-picture-velocityreading.mp4") bytes" || { echo "  reading FAILED"; tail -2 err_read; }
echo "BHRENDER DONE $(date +%T)"
