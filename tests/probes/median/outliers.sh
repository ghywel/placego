#!/bin/bash
# The instrument the median was actually justified with (2026-09-09).
#
# PSNR on the cartoon moved by 0.03 dB when the medians were removed, which does NOT mean the median is
# doing nothing: the commit that introduced it (bd92eea) says so in its own words -- "measured with a metric
# built to see this specifically, since frame-averaged metrics cannot". The defect is a few hundred pixels on
# a handful of frames. flowoutliers.py measures it directly: how far each pixel's flow sits from the median
# of its neighbourhood, so a contiguous motion boundary survives and an isolated false match does not.
#
# Render the FLOW of each shader (flowvis.py replaces only the final hook, so every pass upstream is exactly
# what that shader computes) on the cartoon and on a live-action clip, then score both.
# One GPU job at a time. NB flowoutliers.py loads the WHOLE clip as float32 (a 20 s 720p render at
# 48 fps asked for 3.4 GiB and died), so the probes are 4 s at the source rate: ~96 frames.
set -u
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs
export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH" FFMPEG="$FFDIR/ffmpeg.exe" FFPROBE="$FFDIR/ffprobe.exe"
SC="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"; NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; G="$NP/median"
cd "$G"
echo "########## OUTLIERS start $(date +%T)"
for pair in "vp $SC/shaders/bidirectional-interpolation-variational-propagated.glsl" "vpnm $G/vp-nomedian.glsl"; do
  set -- $pair
  python "$SC/tests/flowvis.py" "$2" "$G/vis_$1.glsl" >/dev/null || { echo "  flowvis $1 FAILED"; exit 1; }
done
probe() {  # <tag> <source> <start> <seconds>
  local tag="$1" src="$2" ss="$3" dur="$4"
  ffmpeg.exe -y -hide_banner -loglevel error -ss "$ss" -t "$dur" -i "$src" -vf "fps=24,format=yuv420p" -c:v ffv1 "$G/src_$tag.mkv" || return 1
  local v
  for v in vp vpnm; do
    ( cd "$G" && ffmpeg.exe -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk \
        -i "src_$tag.mkv" -vf "libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=vis_$v.glsl,format=yuv420p" \
        -c:v ffv1 "flow_${tag}_$v.mkv" ) 2>"$G/err_${tag}_$v"
    echo "  == $tag / $v"
    python "$SC/tests/flowoutliers.py" "$G/flow_${tag}_$v.mkv" 6 3.0 2>&1 | grep -iE "outlier|deviation|frames" | head -4
  done
}
probe cartoon "$NP/bluey.mkv" 60 4
probe live    "$NP/avengers.mp4" 1800 4
echo "OUTLIERS DONE $(date +%T)"
