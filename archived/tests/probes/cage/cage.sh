#!/bin/bash
# The cage (2026-09-21): thin bright vertical bars nine pixels apart, drifting half a pixel a frame with the
# scene, and the same behind a crossing figure -- from a film (10:16: a white railing behind a market crowd,
# its bars bending and breaking in the interpolation; measured 9 px apart, 3 px wide, 80 levels of contrast,
# the camera drifting a fraction of a pixel a frame). C1_cage_drift and C2_cage_drift_occluded in scenes.sh.
# Scored against the native 60 fps render on the WHOLE frame and on the cage's own rectangle, because the
# cage is a small part of the frame and a whole-frame figure hides it -- which is how his eye found what the
# ladder's mean had not. C3_bars_spin_drift (his suggestion) is the same bars at every angle: the grid rotating
# about its origin while the origin translates; its region is the disc the bars fill.
#
#   ./cage.sh [case ...]            SHADERS="a.glsl b.glsl" as in twos.sh (default: the recommendation and -global)
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS="$(cd "$HERE/../.." && pwd)"
. "$TESTS/scenes.sh"
FFMPEG="${FFMPEG:-${FFDIR:-$HOME/np-build/ffmpeg}/ffmpeg}"
PY="${PY:-$HOME/np-build/venv/bin/python3}"
NP_SCRATCH="${NP_SCRATCH:-$(cd "$TESTS/../../.." && pwd)/np-scratch}"
OUTROOT="${OUTROOT:-$NP_SCRATCH/cage}"
CASES=("$@"); [ ${#CASES[@]} -gt 0 ] || CASES=(C1_cage_drift C2_cage_drift_occluded C3_bars_spin_drift)
SHADERS="${SHADERS:-$TESTS/../shaders/bidirectional-interpolation-variational-propagated.glsl $TESTS/../shaders/bidirectional-interpolation-variational-propagated-global.glsl}"
region() {   # the case's own rectangle: the cage (it drifts 24 px over the two seconds; the box has room), or C3's disc
  case "$1" in C3_*) echo "crop=650:630:340:60" ;; *) echo "crop=520:360:390:145" ;; esac
}
sc() { local s; s="$(scene "$1" "$2")"; [ "$s" != UNKNOWN_CASE ] || s="$(scene_edge "$1" "$2")"; echo "$s"; }
run() {   # <out> <mode> <chain> <vk?>
  local out="$1" mode="$2" chain="$3" hw=""
  [ "$4" = vk ] && hw="-init_hw_device vulkan=vk -filter_hw_device vk"
  ( cd "$out" && "$FFMPEG" -y -hide_banner -loglevel error $hw -f lavfi -i "$S24" -f lavfi -i "$S60" \
      -filter_complex "[0:v]${chain}[ip];[ip]format=yuv420p,split[a][a2];[1:v]split[b][b2];[a][b]psnr=stats_file=$mode.log[o];[a2]$REGION[ra];[b2]$REGION[rb];[ra][rb]psnr=stats_file=$mode-cage.log[o2]" \
      -map "[o]" -f null - -map "[o2]" -f null - ) </dev/null 2>"$out/$mode.err" \
    && [ "$(grep -c "hook skipped" "$out/$mode.err")" -le 3 ] && ! grep -q "compile status .error" "$out/$mode.err" \
    && printf "  %-44s ok\n" "$mode" || printf "  %-44s FAILED (see $out/$mode.err)\n" "$mode"
}
for CASE in "${CASES[@]}"; do
  S24="$(sc "$CASE" 24)"; S60="$(sc "$CASE" 60)"
  [ "$S24" != UNKNOWN_CASE ] || { echo "unknown case: $CASE" >&2; continue; }
  out="$OUTROOT/$CASE"; mkdir -p "$out"
  REGION="$(region "$CASE")"
  echo "== $CASE"
  run "$out" hold   "fps=60" sw
  run "$out" linear "libplacebo=fps=60:frame_mixer=linear" vk
  for sh in $SHADERS; do
    cp -f "$sh" "$out/_$(basename "$sh")"
    run "$out" "$(basename "${sh%.glsl}" | sed 's/-interpolation//')" "libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_$(basename "$sh")" vk
  done
done
echo; echo "== PSNR Y (the passthrough instants excluded): the whole frame, and the cage's rectangle"
"$PY" - "$OUTROOT" "${CASES[@]}" <<'PY'
import sys, os, re, statistics
root, cases = sys.argv[1], sys.argv[2:]
def mean_psnr(path):
    v = []
    for line in open(path, errors="replace"):
        m = re.search(r"psnr_y:([0-9.]+|inf)", line); n = re.match(r"n:(\d+)", line)
        if m and n and int(n.group(1)) > 5 and int(n.group(1)) % 5 != 1:
            v.append(99.0 if m.group(1) == "inf" else float(m.group(1)))
    return (statistics.mean(v), min(v)) if v else (float("nan"), float("nan"))
for c in cases:
    d = os.path.join(root, c)
    modes = sorted({f[:-4] for f in os.listdir(d) if f.endswith(".log") and not f.endswith("-cage.log") and not f.startswith("._")})
    print(f"\n{c}\n  {'mode':46s} {'frame':>7s} {'min':>7s}   {'cage':>7s} {'min':>7s}")
    for m in modes:
        a = mean_psnr(os.path.join(d, m + ".log")); b = mean_psnr(os.path.join(d, m + "-cage.log"))
        print(f"  {m:46s} {a[0]:7.2f} {a[1]:7.2f}   {b[0]:7.2f} {b[1]:7.2f}")
PY
