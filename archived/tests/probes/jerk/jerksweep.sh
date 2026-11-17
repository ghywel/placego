#!/bin/bash
# WHERE DOES JERK BECOME READABLE? (2026-09-09, his question.)
#
# The ladder has no cubic term in any of its 42 motion laws: every case is constant, linear, quadratic
# (jerk exactly zero) or a sinusoid (jerk present but rigidly tied to acceleration by the single parameter
# omega). So jerk magnitude has never been laddered the way the A-series ladders acceleration.
#
# Four TEXTURED oscillation cases already exist with identical geometry -- a 300x300 TEX_M2 square at y=210 --
# differing only in amplitude and frequency, which gives a free jerk sweep spanning about eight to one:
#
#   case               A    omega     v px/f   a px/f^2   j px/f^3
#   O6_osc_tex_gentle  40   6.2832    10.47      2.74       0.72
#   O9_osc_tex_fast     6  18.850      4.71      3.70       2.91
#   O10_osc_tex_tiny    4  25.133      4.19      4.39       4.59
#   O5_osc_textured    20  15.708     13.09      8.57       5.61
#
# Score the reading tail's machine JERK on each against the analytic third derivative, and the machine
# ACCELERATION beside it as the control that should stay strong throughout. The full scales are raised so a
# peak of 5.6 px/frame^3 does not saturate the +-FS encoding.
# One GPU job at a time.
set -u
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs
export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH" FFMPEG="$FFDIR/ffmpeg.exe"
SC="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"; NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; G="$NP/jerk"; M="$SC/tests/probes/snap"
mkdir -p "$G"; cd "$G"
. "$SC/tests/scenes.sh"
echo "########## JERK SWEEP start $(date +%T)"

# read_view 5 = machine acceleration, 6 = machine jerk. Raise both full scales so nothing clips.
mk() {  # <read_view> <out>
  python - "$SC/shaders/quaddirectional-interpolation-propagated.glsl" "$1" "$2" <<'PY'
import pathlib, re, sys
src, view, dst = sys.argv[1], sys.argv[2], sys.argv[3]
t = pathlib.Path(src).read_text(encoding="utf-8")
t, n = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>" + view + "\n", t); assert n == 1, n
t, n = re.subn(r"^const float READ_MACHINE_FS_ACC = 2\.0;$", "const float READ_MACHINE_FS_ACC = 16.0;", t, flags=re.M); assert n == 1, n
t, n = re.subn(r"^const float READ_MACHINE_FS_JERK = 2\.0;$", "const float READ_MACHINE_FS_JERK = 8.0;", t, flags=re.M); assert n == 1, n
pathlib.Path(dst).write_text(t, encoding="utf-8", newline="\n")
PY
}
mk 5 "$G/acc.glsl" || exit 1
mk 6 "$G/jerk.glsl" || exit 1
echo "  shaders built (acc FS 16, jerk FS 8)"

probe() {  # <case> <A> <omega>
  local c="$1" A="$2" OM="$3"
  local S; S="$(scene "$c" 24)"; S="${S//:d=1,/:d=4,}"
  local f
  for f in acc jerk; do
    rm -rf "$G/${c}_$f"; mkdir -p "$G/${c}_$f"
    ( cd "$G" && ffmpeg.exe -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk -f lavfi -i "$S" \
        -vf "libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=$f.glsl,format=rgb48le" -frames:v 60 "$G/${c}_$f/f%03d.png" ) 2>"$G/err_${c}_$f"
    local n; n=$(ls "$G/${c}_$f" | wc -l); [ "$n" -ge 50 ] || { echo "  $c/$f SHORT ($n frames)"; head -2 "$G/err_${c}_$f"; }
  done
  echo "--- $c  (A=$A, omega=$OM)"
  python "$M/snapcheck.py" 2 "$G/${c}_acc"  16 "$A" "$OM" 600 210 300 40 2>&1 | grep -E "^==|gain"
  python "$M/snapcheck.py" 3 "$G/${c}_jerk"  8 "$A" "$OM" 600 210 300 40 2>&1 | grep -E "^==|gain"
}
{ probe O6_osc_tex_gentle 40 6.2832
  probe O9_osc_tex_fast    6 18.850
  probe O10_osc_tex_tiny   4 25.133
  probe O5_osc_textured   20 15.708
} 2>&1 | tee "$G/sweep.txt"
echo "JERK SWEEP DONE $(date +%T)"
