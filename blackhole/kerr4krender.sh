#!/bin/bash
set -u
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs
export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH"
NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; G="$NP/eyes/blackhole"; HD="${HOT_DROPS:-/e/nframe-project/hot-drops}"
cd "$G"
echo "########## KERR4KRENDER start $(date +%T)"
ffmpeg.exe -y -hide_banner -loglevel error -f rawvideo -pix_fmt rgb24 -s 3840x2160 -r 24 -i full4k_jp/frames.rgb -vf format=yuv420p -c:v h264_mf -b:v 48M -maxrate 64M -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv -movflags "+faststart+write_colr" "$HD/blackhole-johannsenpsaltis-4k-10s.mp4" && echo "  4k: $(stat -c %s "$HD/blackhole-johannsenpsaltis-4k-10s.mp4") bytes"
ffmpeg.exe -y -hide_banner -loglevel error -f rawvideo -pix_fmt rgb24 -s 3840x2160 -r 24 -i full4k_jp/frames.rgb -vf "select='eq(n\,120)'" -frames:v 1 -update 1 "$HD/blackhole-johannsenpsaltis-4k-frame120.png" && echo "  still: $(stat -c %s "$HD/blackhole-johannsenpsaltis-4k-frame120.png") bytes"
echo "KERR4KRENDER DONE $(date +%T)"
