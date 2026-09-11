#!/bin/bash
# Hawking radiation, rendered as far as the mathematics honestly allows (2026-09-08): the hovering approach film,
# the mode film, the chart; encode and copy to hot-drops. CPU only; run alone.
set -u
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs
export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH"
NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; G="$NP/eyes/blackhole"; HD="${HOT_DROPS:-/e/nframe-project/hot-drops}"
cd "$G"
echo "########## HAWKRENDER start $(date +%T)"
python hawkapproach.py hawk_approach 240 960 2000 40 2.02 2>&1 | tee hawk_approach.log
python hawkmode.py hawk_mode 240 960 1080 16 2>&1 | tee hawk_mode.log
python hawkchart.py hawk_chart.ppm 2>&1 | tee hawk_chart.log
echo "########## encode $(date +%T)"
ffmpeg.exe -y -hide_banner -loglevel error -f rawvideo -pix_fmt rgb24 -s 1920x1040 -r 24 -i hawk_approach/frames.rgb -vf format=yuv420p -c:v h264_mf -b:v 20M -movflags +faststart "$HD/hawking-approach-hover-40M-to-2.02M-10s.mp4" && echo "  approach: $(stat -c %s "$HD/hawking-approach-hover-40M-to-2.02M-10s.mp4") bytes"
ffmpeg.exe -y -hide_banner -loglevel error -f rawvideo -pix_fmt rgb24 -s 1920x1080 -r 24 -i hawk_mode/frames.rgb -vf format=yuv420p -c:v h264_mf -b:v 20M -movflags +faststart "$HD/hawking-mode-dipole-quadrupole-10s.mp4" && echo "  mode: $(stat -c %s "$HD/hawking-mode-dipole-quadrupole-10s.mp4") bytes"
for f in hawk_approach/still_r*.ppm; do
  b=$(basename "$f" .ppm); r=${b#still_r}
  ffmpeg.exe -y -hide_banner -loglevel error -i "$f" "$HD/hawking-approach-r${r}M.png" && echo "  still r = $r"
done
ffmpeg.exe -y -hide_banner -loglevel error -i hawk_mode/still_mid.ppm "$HD/hawking-mode-frame120.png" && echo "  mode still"
ffmpeg.exe -y -hide_banner -loglevel error -i hawk_chart.ppm "$HD/hawking-spectrum-chart.png" && echo "  chart"
ls -la "$HD" | grep hawking
echo "HAWKRENDER DONE $(date +%T)"
