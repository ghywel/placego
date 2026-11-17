#!/bin/bash
# A child's arm against a still room, scored where it is (2026-09-27, from the party recording: NFRAME-LIMITS.md
# "The field on real bodies"). On real bodies the recommendation's field reads a moving arm at gain 0.7 up to 24 px
# per frame and loses it past that, a growing share snapping to zero, where the coarse search's reach (~23 px) ends
# and nothing -- the global seed included, the frame's dominant motion being zero -- carries it further. K1 puts
# that on the ladder: a textured limb sweeping across a STATIC textured wall at 12 -> 60 px per source frame over the
# second; K2 is the same limb over a flat dark wall, the control (the party app's bench: the cliff moves with the
# still background's texture).
#
#   ./limb.sh [case]            default K1_limb_sweep_wall;  SHADERS="a.glsl b.glsl" to choose the files
#
# The score: PSNR Y inside a box that FOLLOWS the limb (its 48 x 200 plus 64 px either side and 32 above and
# below: the limb and its halo), per output frame against the native 60 fps render, then the mean by the limb's
# speed at the output instant (px per SOURCE frame, from the scene's own law); hold and linear beside. A whole-frame
# PSNR would be the still wall's, which every mode gets right.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS="$(cd "$HERE/../.." && pwd)"
. "$TESTS/scenes.sh"
FFMPEG="${FFMPEG:-${FFDIR:-$HOME/np-build/ffmpeg}/ffmpeg}"
PY="${PY:-$HOME/np-build/venv/bin/python3}"
NP_SCRATCH="${NP_SCRATCH:-$(cd "$TESTS/../../.." && pwd)/np-scratch}"
OUTROOT="${OUTROOT:-$NP_SCRATCH/limb}"
CASE="${1:-K1_limb_sweep_wall}"
SH="$TESTS/../shaders"
SHADERS="${SHADERS:-$SH/bidirectional-interpolation-variational-propagated.glsl $SH/bidirectional-interpolation-variational-propagated-global-cage.glsl $SH/quaddirectional-interpolation-propagated.glsl}"
S24="$(scene_edge "$CASE" 24)"; S60="$(scene_edge "$CASE" 60)"
[ "$S24" != UNKNOWN_CASE ] && [ -n "$S24" ] || { echo "unknown case: $CASE" >&2; exit 1; }
# the box that follows the limb: x = 100 + 288 t + 576 t^2 (the case's law), less the margin
ROI="crop=w=176:h=264:x='100+288*t+576*t*t-64':y=228"
out="$OUTROOT/$CASE"; mkdir -p "$out"
run() {   # <mode label> <filter chain> <vk?>
  local mode="$1" chain="$2" hw=""
  [ "$3" = vk ] && hw="-init_hw_device vulkan=vk -filter_hw_device vk"
  ( cd "$out" && "$FFMPEG" -y -hide_banner -loglevel error $hw -f lavfi -i "$S24" -f lavfi -i "$S60" \
      -filter_complex "[0:v]${chain}[ip];[ip]format=yuv420p,${ROI}[i2];[1:v]${ROI}[t2];[i2][t2]psnr=stats_file=$mode.log[o]" -map "[o]" -f null - ) </dev/null 2>"$out/$mode.err" \
    && [ "$(grep -c "hook skipped" "$out/$mode.err")" -le 3 ] && ! grep -q "compile status .error" "$out/$mode.err" \
    && printf "  %-48s ok\n" "$mode" || printf "  %-48s FAILED (see $out/$mode.err)\n" "$mode"
}
echo "== $CASE"
run hold   "fps=60" sw
run linear "libplacebo=fps=60:frame_mixer=linear" vk
for sh in $SHADERS; do
  cp -f "$sh" "$out/_$(basename "$sh")"
  run "$(basename "${sh%.glsl}" | sed 's/-interpolation//')" "libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_$(basename "$sh")" vk
done
echo; echo "== PSNR Y in the box following the limb, by the limb's speed at the output instant (px per SOURCE frame; passthrough instants excluded)"
"$PY" - "$out" <<'PY'
import sys, os, re, statistics
out = sys.argv[1]
def load(p):
    d = {}
    for line in open(p, errors="replace"):
        m = re.search(r"psnr_y:([0-9.]+|inf)", line); n = re.match(r"n:(\d+)", line)
        if m and n: d[int(n.group(1))] = 99.0 if m.group(1) == "inf" else float(m.group(1))
    return d
modes = [f[:-4] for f in sorted(os.listdir(out)) if f.endswith(".log") and not f.startswith("_") and not f.startswith("._")]
order = ["hold", "linear"] + [m for m in modes if m not in ("hold", "linear")]
logs = {m: load(os.path.join(out, m + ".log")) for m in order if m in modes}
def speed(n):                      # output n (1-based) at t = (n-1)/60 s; v = 288 + 1152 t px/s; per source frame /24
    t = (n - 1) / 60.0
    return (288 + 1152 * t) / 24.0
bands = [(12, 18), (18, 24), (24, 30), (30, 36), (36, 42), (42, 48), (48, 54), (54, 61)]
print("  " + "band px/frame".ljust(14) + "".join(m[:34].ljust(36) for m in logs))
for lo, hi in bands:
    row = []
    for m in logs:
        v = [x for n, x in logs[m].items() if n > 5 and n % 5 != 1 and lo <= speed(n) < hi]
        row.append(f"{statistics.mean(v):6.2f} (n={len(v):2d})" if v else "   -")
    print("  " + f"{lo:2d}-{hi:2d}".ljust(14) + "".join(r.ljust(36) for r in row))
PY
