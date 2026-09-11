#!/bin/bash
# Encode the three metrics' frames: one mp4 each, a triptych video (Schwarzschild | Kerr 0.9 | Johannsen-Psaltis),
# a triptych still of frame 60, and the triptych through the human reading.
set -u
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs
export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH"
SC="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; G="$NP/eyes/blackhole"; HD="${HOT_DROPS:-/e/nframe-project/hot-drops}"
cd "$G"
echo "########## KERRRENDER start $(date +%T)"
for m in schwarzschild kerr jp; do
  ffmpeg.exe -y -hide_banner -loglevel error -f rawvideo -pix_fmt rgb24 -s 960x540 -r 24 -i full_$m/frames.rgb -vf format=yuv420p -c:v h264_mf -b:v 10M -movflags +faststart "$HD/blackhole-$m-5s.mp4" && echo "  $m: $(stat -c %s "$HD/blackhole-$m-5s.mp4") bytes"
done
ffmpeg.exe -y -hide_banner -loglevel error -f rawvideo -pix_fmt rgb24 -s 960x540 -r 24 -i full_schwarzschild/frames.rgb -f rawvideo -pix_fmt rgb24 -s 960x540 -r 24 -i full_kerr/frames.rgb -f rawvideo -pix_fmt rgb24 -s 960x540 -r 24 -i full_jp/frames.rgb \
  -filter_complex "[0:v][1:v][2:v]hstack=inputs=3,format=yuv420p[o]" -map "[o]" -r 24 -c:v h264_mf -b:v 24M -movflags +faststart "$HD/blackhole-triptych-schwarzschild-kerr09-johannsenpsaltis-5s.mp4" && echo "  triptych: $(stat -c %s "$HD/blackhole-triptych-schwarzschild-kerr09-johannsenpsaltis-5s.mp4") bytes"
ffmpeg.exe -y -hide_banner -loglevel error -ss 2.5 -i "$HD/blackhole-triptych-schwarzschild-kerr09-johannsenpsaltis-5s.mp4" -frames:v 1 -update 1 "$HD/blackhole-triptych-frame60.png" && echo "  still written"
sed '/^\/\/!PARAM read_view/,/^$/ s/^0$/1/' "$SC/shaders/quaddirectional-interpolation-propagated.glsl" > read1.glsl
ffmpeg.exe -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk -i "$HD/blackhole-triptych-schwarzschild-kerr09-johannsenpsaltis-5s.mp4" \
  -vf "libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=read1.glsl,format=yuv420p" -r 24 -c:v h264_mf -b:v 24M -movflags +faststart "$HD/blackhole-triptych-velocityreading-5s.mp4" 2>err_tri \
  && echo "  triptych reading: $(stat -c %s "$HD/blackhole-triptych-velocityreading-5s.mp4") bytes" || { echo "  reading FAILED"; tail -2 err_tri; }
echo "KERRRENDER DONE $(date +%T)"
