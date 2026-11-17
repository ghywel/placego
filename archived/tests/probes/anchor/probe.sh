#!/bin/bash
# Where is the reading standing? (2026-09-09.) Build scratch copies of the tailed shaders with the reading's
# machine acceleration selected and its full scale raised so a strong oscillation does not saturate, render
# O5_osc_textured through them at N:N and at 24 -> 60, and find the measurement instant with phaseprobe.py.
#
#   probe.sh <tag>          # e.g. "before" or "after"; results land in <tag>-result.txt
#
# The scratch shaders are the REPO's current files with three constants changed, so this measures whatever is
# committed at the time it runs. Velocity is measured too and must not move: it is computed from the straddle
# pair and never touches the anchor.
set -u
TAG="${1:?usage: probe.sh <tag>}"
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs
export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH" FFMPEG="$FFDIR/ffmpeg.exe"
SC="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; G="$NP/anchor"
. "$SC/tests/scenes.sh"
SRC="$(scene O5_osc_textured 24)"; SRC="${SRC//:d=1,/:d=4,}"
cd "$G"
echo "########## PROBE $TAG start $(date +%T) at $(cd $SC && git rev-parse --short HEAD)"

# read_view's default is the bare number line ending its //!PARAM block; ffmpeg cannot set shader params.
mkfield() {  # <shader stem> <read_view> <acc fs> <out file>
  python - "$SC/shaders/$1.glsl" "$2" "$3" "$4" <<'PY'
import pathlib, re, sys
src, view, accfs, dst = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
t = pathlib.Path(src).read_text(encoding="utf-8")
t, n = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>" + view + "\n", t)
assert n == 1, f"read_view default: {n} substitutions"
t, n = re.subn(r"^const float READ_MACHINE_FS_ACC = 2\.0;$", "const float READ_MACHINE_FS_ACC = " + accfs + ";", t, flags=re.M)
assert n == 1, f"READ_MACHINE_FS_ACC: {n} substitutions"
pathlib.Path(dst).write_text(t, encoding="utf-8", newline="\n")
print(f"  {pathlib.Path(dst).name}: read_view {view}, acc FS {accfs}")
PY
}

for stem in quaddirectional-interpolation-propagated quintdirectional-interpolation-propagated sextdirectional-interpolation-propagated; do
  short=$(echo "$stem" | cut -c1-4)
  mkfield "$stem" 5 16.0 "$G/${short}_acc.glsl" || exit 1
  mkfield "$stem" 4 16.0 "$G/${short}_vel.glsl" || exit 1
done

render() {  # <shader file> <out fps> <dir>
  rm -rf "$3"; mkdir -p "$3"
  ( cd "$G" && ffmpeg.exe -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk \
      -f lavfi -i "$SRC" -vf "libplacebo=fps=$2:frame_mixer=custom_n:custom_shader_path=$(basename "$1"),format=rgb48le" \
      -frames:v 48 "$3/f%03d.png" ) 2>"$G/err_$(basename "$3")"
  local n; n=$(ls "$3" 2>/dev/null | wc -l)
  echo "  $(basename "$3"): $n frames"
  [ "$n" -ge 40 ] || { echo "  RENDER SHORT -- see err_$(basename "$3")"; head -2 "$G/err_$(basename "$3")"; }
}

: > "$TAG-result.txt"
for short in quad quin sext; do
  for rate in 24 60; do
    render "$G/${short}_acc.glsl" "$rate" "$G/${short}_acc_$rate"
    render "$G/${short}_vel.glsl" "$rate" "$G/${short}_vel_$rate"
    { echo "---- $short at 24 -> $rate"
      python phaseprobe.py "$G/${short}_acc_$rate" acc 16.0 24 "$rate" 20 15.708 600 210 300
      python phaseprobe.py "$G/${short}_vel_$rate" vel 32.0 24 "$rate" 20 15.708 600 210 300
    } >> "$TAG-result.txt" 2>&1
  done
done
cat "$TAG-result.txt"
echo "PROBE $TAG DONE $(date +%T)"
