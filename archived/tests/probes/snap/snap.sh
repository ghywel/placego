#!/bin/bash
# Is the quint's snap row a readable field? (2026-09-08; the prediction is in PREDICTION.md, written first.)
# O5_osc_textured -- a 300x300 TEXTURED square oscillating, A = 20 px at Omega = 15.708 rad/s, which is the
# record's own field-calibration scene -- through the quint's machine modes at N:N: acceleration (TRI_DIAG 2,
# FS 16), jerk (5, FS 8), snap (10, FS 8, the scratch variant). The full scales are the ones fieldaccept.sh
# uses for this scene, and they must EXCEED the peak truth or the encoding saturates (acceleration peaks at
# 8.6 px/frame^2, jerk 5.6, snap 3.7). Frames 1..48 as rgb48le PNG, scored by snapcheck.py.
# One GPU job; do not run beside another.
set -u
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs
export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH" FFMPEG="$FFDIR/ffmpeg.exe"
SC="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"; NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; S="$NP/metal-prep/snap"
. "$SC/tests/scenes.sh"
SRC="$(scene O5_osc_textured 24)"; SRC="${SRC//:d=1,/:d=3,}"
echo "########## SNAP start $(date +%T)"
for v in acc jerk snap; do
  rm -rf "$S/$v"; mkdir -p "$S/$v"
  ( cd "$S" && ffmpeg.exe -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk -f lavfi -i "$SRC" \
      -vf "libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=quint-$v.glsl,format=rgb48le" -frames:v 48 "$S/$v/f%03d.png" ) 2>"$S/err_$v"
  echo "  $v: $(ls "$S/$v" | wc -l) frames ($(date +%T))"; grep -i "error\|vkAllocate" "$S/err_$v" | head -2
done
# O5: _rect '600+20*sin(15.708*T)' '210' 300 300 -> left edge x, top y, side; eroded 40 px
cd "$S" && { python "$HERE/snapcheck.py" 2 "$S/acc"  16 20 15.708 600 210 300 40
             python "$HERE/snapcheck.py" 3 "$S/jerk"  8 20 15.708 600 210 300 40
             python "$HERE/snapcheck.py" 4 "$S/snap"  8 20 15.708 600 210 300 40; } 2>&1 | tee snap-result.txt
echo "SNAP DONE $(date +%T)"
