#!/bin/bash
# Toolchain smoke test: does everything in this directory work HERE?
#
#   export FFMPEG=/path/to/ffmpeg FFPROBE=/path/to/ffprobe
#   ./smoke.sh
#
# The harness is meant to be the same on Linux and on Windows/MSYS2. That is
# easy to claim and easy to get wrong, because the ways it breaks on Windows
# are not obvious -- absolute paths cannot appear inside ffmpeg filter
# arguments (the drive-letter colon is ffmpeg's option separator), paths
# embedded in filter strings are not path-converted by MSYS2 at all, and
# MSYS2's POSIX root is not the Windows root so a relative path spanning the
# two is meaningless to a native binary.
#
# So rather than assume portability, exercise every tool and report per-tool
# pass/fail. Runs in a couple of minutes on a real GPU, longer under software
# Vulkan. Needs no source video: everything is generated.
#
# Exits non-zero if any tool fails.

set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FFMPEG="${FFMPEG:-ffmpeg}"
FFPROBE="${FFPROBE:-ffprobe}"
W="${W:-${TMPDIR:-/tmp}/interp-smoke}"
PY="${PY:-python3}"
command -v "$PY" >/dev/null 2>&1 || PY=python

pass=0; fail=0
ok()   { printf '  \033[32mPASS\033[0m  %s\n' "$*"; pass=$((pass+1)); }
bad()  { printf '  \033[31mFAIL\033[0m  %s\n' "$*"; fail=$((fail+1)); }
note() { printf '        %s\n' "$*"; }
head2() { printf '\n\033[1m-- %s\033[0m\n' "$*"; }

rm -rf "$W"; mkdir -p "$W" || { echo "cannot create $W"; exit 1; }

# ---------------------------------------------------------------------------
head2 "environment"
printf '  %-10s %s\n' "uname" "$(uname -s 2>/dev/null || echo unknown)"
printf '  %-10s %s\n' "MSYSTEM" "${MSYSTEM:-<not MSYS2>}"
printf '  %-10s %s\n' "ffmpeg" "$("$FFMPEG" -version 2>/dev/null | head -1 | cut -c1-60)"
printf '  %-10s %s\n' "python" "$($PY -V 2>&1)"
printf '  %-10s %s\n' "workdir" "$W"
for m in numpy; do
  v=$($PY -c "import $m;print($m.__version__)" 2>/dev/null)
  printf '  %-10s %s\n' "$m" "${v:-MISSING}"
done

# ---------------------------------------------------------------------------
head2 "1. scenes.sh -- synthetic sources, no media needed"
# shellcheck disable=SC1091
if . "$HERE/scenes.sh" 2>/dev/null && S24="$(scene L1_trans_8px 24)" && [ -n "$S24" ]; then
  ok "scenes.sh sources and produces a scene"
else
  bad "scenes.sh could not be sourced"; S24=""
fi

if [ -n "$S24" ] && "$FFMPEG" -y -v error -f lavfi -i "$S24" -c:v ffv1 "$W/src.mkv" 2>/dev/null; then
  N=$("$FFPROBE" -v error -count_frames -select_streams v:0 \
      -show_entries stream=nb_read_frames -of default=noprint_wrappers=1:nokey=1 "$W/src.mkv")
  ok "rendered a $N-frame synthetic source"
else
  bad "could not render a synthetic source"
fi

# ---------------------------------------------------------------------------
head2 "2. clip.sh -- frame-exact cutting, addressed by time"
if [ -s "$W/src.mkv" ] && bash "$HERE/clip.sh" "$W/src.mkv" '#12' 5 "$W/cut.mkv" >"$W/clip.log" 2>&1; then
  got=$("$FFPROBE" -v error -count_frames -select_streams v:0 \
        -show_entries stream=nb_read_frames -of default=noprint_wrappers=1:nokey=1 "$W/cut.mkv")
  # independent ground truth: decode from frame 0, no seek at all
  "$FFMPEG" -y -v error -i "$W/src.mkv" \
    -vf "select='between(n\,7\,17)',setpts=PTS-STARTPTS" -fps_mode passthrough \
    -map 0:v:0 -an -c:v ffv1 "$W/truth.mkv" 2>/dev/null
  "$FFMPEG" -v error -i "$W/cut.mkv"   -f framemd5 -c:v rawvideo "$W/a.md5" 2>/dev/null
  "$FFMPEG" -v error -i "$W/truth.mkv" -f framemd5 -c:v rawvideo "$W/b.md5" 2>/dev/null
  if [ "$got" = 11 ] && diff -q <(grep -v '^#' "$W/a.md5") <(grep -v '^#' "$W/b.md5") >/dev/null 2>&1; then
    ok "clip.sh is frame-exact ($got frames, bit-identical to an unseeked decode)"
  else
    bad "clip.sh output does not match an unseeked decode"; note "got $got frames, expected 11"
  fi
else
  bad "clip.sh failed"; note "$(tail -2 "$W/clip.log" 2>/dev/null)"
fi

# ---------------------------------------------------------------------------
head2 "3. gen_variational.py -- generated shader is byte-identical here"
# A strong portability check: the production shader is generated, so if this
# platform produces the same bytes, the generator and its inputs agree.
PROD="$HERE/../shaders/bidirectional-interpolation-variational.glsl"
if $PY "$HERE/gen_variational.py" "16,12,8,4" 0.3 0.08 "$W/regen.glsl" 0 "2,2,2,0" >/dev/null 2>&1; then
  strip() { awk 'p{print} /^\/\/ =====/{c++} c==2 && !p{p=1}' "$1"; }
  if diff -q <(strip "$W/regen.glsl") <(strip "$PROD") >/dev/null 2>&1; then
    ok "regenerated shader body is byte-identical to the committed one"
  else
    bad "regenerated shader differs from the committed one"
    note "$(diff <(strip "$W/regen.glsl") <(strip "$PROD") | head -3)"
  fi
else
  bad "gen_variational.py failed"
fi

# ---------------------------------------------------------------------------
head2 "4. flowvis.py -- build a flow visualiser from the production shader"
if $PY "$HERE/flowvis.py" "$PROD" "$W/vis.glsl" >/dev/null 2>&1 && [ -s "$W/vis.glsl" ]; then
  ok "flowvis.py rewrote the final hook()"
else
  bad "flowvis.py failed"
fi

# ---------------------------------------------------------------------------
head2 "5. the shader actually runs here"
# Shaders are addressed by BARE NAME from their own directory. An absolute
# path cannot be used inside a filter argument on Windows at all.
if [ -s "$W/vis.glsl" ] && [ -s "$W/src.mkv" ] &&
   ( cd "$W" && "$FFMPEG" -y -v error -init_hw_device vulkan=vk -filter_hw_device vk \
       -i src.mkv -vf "libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=vis.glsl,format=yuv420p" \
       -c:v ffv1 flow.mkv ) 2>"$W/vis.err"; then
  N=$("$FFPROBE" -v error -count_frames -select_streams v:0 \
      -show_entries stream=nb_read_frames -of default=noprint_wrappers=1:nokey=1 "$W/flow.mkv")
  ok "flow visualiser rendered $N frames through Vulkan"
else
  bad "flow visualiser did not render"; note "$(head -2 "$W/vis.err" 2>/dev/null)"
fi

# ---------------------------------------------------------------------------
head2 "6. flowoutliers.py -- the metric that needs numpy"
if [ -s "$W/flow.mkv" ] &&
   FFMPEG="$FFMPEG" FFPROBE="$FFPROBE" $PY "$HERE/flowoutliers.py" "$W/flow.mkv" 6 3.0 >"$W/fo.log" 2>&1; then
  ok "flowoutliers.py ran"
  note "$(grep -E 'outlier pixels' "$W/fo.log" | head -1 | sed 's/^ *//')"
else
  bad "flowoutliers.py failed"; note "$(tail -2 "$W/fo.log" 2>/dev/null)"
fi

# ---------------------------------------------------------------------------
head2 "7. prospect.py -- ranking, on the same flow render"
if [ -s "$W/flow.mkv" ] &&
   FFMPEG="$FFMPEG" FFPROBE="$FFPROBE" $PY "$HERE/prospect.py" "$W/flow.mkv" \
     --source "$W/src.mkv" --src-fps 24 >"$W/pr.log" 2>&1; then
  ok "prospect.py ran"
  note "$(grep -E 'output frames at' "$W/pr.log" | head -1 | sed 's/^ *//')"
else
  bad "prospect.py failed"; note "$(tail -2 "$W/pr.log" 2>/dev/null)"
fi

# ---------------------------------------------------------------------------
head2 "8. bench.sh + analyze.py -- ground truth against baselines"
if OUTROOT="$W/bench" FFMPEG="$FFMPEG" FFPROBE="$FFPROBE" \
   bash "$HERE/bench.sh" L1_trans_8px "$PROD" smoke >"$W/bench.log" 2>&1 &&
   grep -q "smoke ok" "$W/bench.log"; then
  R=$(OUTROOT="$W/bench" $PY "$HERE/analyze.py" --variants 2>/dev/null | grep L1_trans_8px)
  ok "bench.sh completed"
  note "$(echo "$R" | sed 's/^ *//')"
else
  bad "bench.sh failed"; note "$(grep -iE 'fail|error' "$W/bench.log" | head -2)"
fi

# ---------------------------------------------------------------------------
head2 "9. visuals.sh -- inspectable frames"
if OUTROOT="$W/bench" FFMPEG="$FFMPEG" FFPROBE="$FFPROBE" \
   bash "$HERE/visuals.sh" L1_trans_8px "$PROD" 23 >"$W/vis2.log" 2>&1; then
  # Count exactly, not "more than zero". A weaker check passed on both
  # platforms while one image was silently missing on Linux and two on
  # Windows -- the difference image used `eq`, which is a GPL filter absent
  # from builds without --enable-gpl.
  n=$(find "$W/bench" -name '*.jpg' 2>/dev/null | wc -l)
  if [ "$n" -eq 4 ]; then ok "visuals.sh wrote all 4 inspectable frames"
  else bad "visuals.sh wrote $n images, expected 4 (shader, truth, diff, linear)"
       note "missing: $(cd "$W/bench" 2>/dev/null && for f in shader truth diff linear; do
              find . -name "$f.jpg" -print -quit | grep -q . || printf '%s ' "$f"; done)"; fi
else
  bad "visuals.sh failed"; note "$(tail -2 "$W/vis2.log" 2>/dev/null)"
fi

# ---------------------------------------------------------------------------
head2 "10. tieprobe.py -- a probed build still compiles and runs"
# Deliberately not a full tieprobe.sh run: that is eight renders and this is a
# toolchain check, not a measurement. What can silently break per-platform is
# the injected GLSL itself -- it uses floatBitsToUint and unsigned arithmetic,
# which a different shader compiler could reject. So: generate one probed
# build and put it through Vulkan.
if $PY "$HERE/tieprobe.py" "$PROD" "$W/probed.glsl" 1 1e-6 >/dev/null 2>&1 &&
   [ -s "$W/probed.glsl" ] && [ -s "$W/src.mkv" ] &&
   ( cd "$W" && "$FFMPEG" -y -v error -init_hw_device vulkan=vk -filter_hw_device vk \
       -i src.mkv -vf "libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=probed.glsl,format=yuv420p" \
       -frames:v 6 -f null - ) 2>"$W/probe.err"; then
  ok "probed build compiled and rendered"
else
  bad "probed build failed"; note "$(head -2 "$W/probe.err" 2>/dev/null)"
fi

# ---------------------------------------------------------------------------
head2 "11. scenecheck.sh -- the ladder's ground-truth property holds"
# Only the analytic scenes, and only a couple of them: this is a check that the
# tool runs and that scenes which are supposed to be exact still are, not a
# sweep of the whole ladder. The overlay-based cases are pixel-quantised by
# construction (see TESTING.md) and would report as such, which is expected
# rather than a failure, so they are not useful as a pass/fail signal here.
# The assertion is "no POSITIONAL failure", not "bit-identical everywhere".
# A rectangle scene legitimately reports "exact to rounding": the two rates
# compute t a ULP apart and a coverage value sitting exactly on a rounding
# boundary can tip, worth a max delta of 1 on an edge texel. Demanding
# bit-identical here would fail on that and teach nobody anything. What must
# never happen is the object being in a different PLACE at the same instant.
if OUTROOT="$W" FFMPEG="$FFMPEG" bash "$HERE/scenecheck.sh" \
     A1_accel_8mean F1_fourier_edge R1_rot_const >"$W/scenechk.log" 2>&1 &&
   ! grep -q POSITIONAL "$W/scenechk.log"; then
  ok "scenes are ground truth at both rates, none positionally wrong"
else
  bad "scenecheck.sh failed, or a scene's ground truth is positionally wrong"
  note "$(grep -E 'POSITIONAL|MISMATCH|NO OUTPUT' "$W/scenechk.log" | head -2)"
fi

# ---------------------------------------------------------------------------
printf '\n\033[1m== %d passed, %d failed\033[0m\n' "$pass" "$fail"
[ "$fail" = 0 ] || exit 1
