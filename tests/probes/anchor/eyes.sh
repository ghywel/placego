#!/bin/bash
# For his eyes: the reading before and after the anchor fix, side by side at N:N on the oscillating textured
# square, where the old anchor stood a full source interval early. Left = before, right = after.
set -u
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs
export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH"
SC="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"; NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; G="$NP/anchor"; HD="${HOT_DROPS:-/e/nframe-project/hot-drops}"
. "$SC/tests/scenes.sh"
S="$(scene O5_osc_textured 24)"; S="${S//:d=1,/:d=5,}"
# read_view 2 = the painted acceleration reading, which is what the anchor moves
for tag in before after; do
  src="$G/_prefix.glsl"; [ "$tag" = after ] && src="$SC/shaders/quaddirectional-interpolation-propagated.glsl"
  python - "$src" "$G/_eyes_$tag.glsl" <<'PY'
import pathlib, re, sys
t = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
t, n = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>2\n", t)
assert n == 1
pathlib.Path(sys.argv[2]).write_text(t, encoding="utf-8", newline="\n")
PY
done
ffmpeg.exe -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk \
  -f lavfi -i "$S" -f lavfi -i "$S" \
  -filter_complex "[0:v]libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=_eyes_before.glsl,drawbox=x=0:y=0:w=1280:h=44:color=black@0.6:t=fill[a];[1:v]libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=_eyes_after.glsl,drawbox=x=0:y=0:w=1280:h=44:color=black@0.6:t=fill[b];[a][b]hstack,format=yuv420p[o]" \
  -map "[o]" -r 24 -c:v h264_mf -b:v 20M -movflags +faststart "$HD/reading-anchor-before-after-24fps.mp4" 2>"$G/err_eyes"
echo "  $(stat -c %s "$HD/reading-anchor-before-after-24fps.mp4" 2>/dev/null) bytes"
ffmpeg.exe -y -hide_banner -loglevel error -i "$HD/reading-anchor-before-after-24fps.mp4" -vf "select=eq(n\,60)" -frames:v 1 -update 1 "$HD/reading-anchor-before-after-frame60.png" 2>>"$G/err_eyes"
