#!/bin/bash
# compile_all.sh [shader ...]: render three frames through every shader and fail on any compile or link error. The
# generators do not compile GLSL, so a rebuilt file can be well formed and still not build (2026-10-04: 14 files
# called a function L3 had deleted, and only an impossible -83% render time showed it).
set -u
HERE="$(cd "$(dirname "$0")/../.." && pwd)"; . "$HERE/mvk-env.sh"
FF=${FFMPEG:-ffmpeg}; SRC=${COMPILE_SRC:-/tmp/nframe-identity/L2_trans_16px.mkv}
[ $# -gt 0 ] && files=("$@") || files=("$HERE"/../shaders/*.glsl "$HERE"/../shaders/animation/*.glsl)
ok=0; bad=0
for f in "${files[@]}"; do
  e=$($FF -nostdin -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk -i "$SRC" \
        -vf "libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=$f" -frames:v 3 -f null - 2>&1 | grep -c -i "error")
  if [ "$e" = 0 ]; then ok=$((ok+1)); else bad=$((bad+1)); echo "  FAILS  $(basename "$f")"; fi
done
echo "COMPILE DONE: $ok build, $bad fail"
