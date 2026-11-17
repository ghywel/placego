#!/bin/bash
# The fast pan over fine texture, scored against the speed (2026-09-19). From a film: a tracking shot along a
# sandstone wall whose texture crosses the frame faster and faster, and the picture goes "from smooth to weird"
# as it does (the owner, 6:29-6:34 of the film; the wall measured 12 -> 38 px per source frame by phase
# correlation, tests/probes/dig/panspeed.py). The ladder holds the fact as two points -- L3 at 23 px inside the
# reach, L4 at 40 px beyond it -- and this puts the ramp between them: W1_wall_pan_ramp, a textured ground
# panning 8 -> 40 px per source frame over two seconds under a static textured subject, so the knee is a number
# and a mechanism can be measured against it.
#
#   ./pan.sh [case]                  default W1_wall_pan_ramp;  SHADERS="a.glsl b.glsl" as in twos.sh
#
# The output: PSNR Y per output frame against the native 60 fps render, then the mean by speed band (the speed
# at each output instant, from the scene's own law), hold and linear beside.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS="$(cd "$HERE/../.." && pwd)"
. "$TESTS/scenes.sh"
FFMPEG="${FFMPEG:-${FFDIR:-$HOME/np-build/ffmpeg}/ffmpeg}"
PY="${PY:-$HOME/np-build/venv/bin/python3}"
NP_SCRATCH="${NP_SCRATCH:-$(cd "$TESTS/../../.." && pwd)/np-scratch}"
OUTROOT="${OUTROOT:-$NP_SCRATCH/pan}"
CASE="${1:-W1_wall_pan_ramp}"
SHADERS="${SHADERS:-$TESTS/../shaders/bidirectional-interpolation-variational-propagated.glsl $TESTS/../shaders/quaddirectional-interpolation-propagated.glsl}"
sc() { local s; s="$(scene "$1" "$2")"; [ "$s" != UNKNOWN_CASE ] || s="$(scene_edge "$1" "$2")"; echo "$s"; }
S24="$(sc "$CASE" 24)"; S60="$(sc "$CASE" 60)"
[ "$S24" != UNKNOWN_CASE ] || { echo "unknown case: $CASE" >&2; exit 1; }
out="$OUTROOT/$CASE"; mkdir -p "$out"
run() {   # <mode label> <filter chain> <vk?>
  local mode="$1" chain="$2" hw=""
  [ "$3" = vk ] && hw="-init_hw_device vulkan=vk -filter_hw_device vk"
  ( cd "$out" && "$FFMPEG" -y -hide_banner -loglevel error $hw -f lavfi -i "$S24" -f lavfi -i "$S60" \
      -filter_complex "[0:v]${chain}[ip];[ip]format=yuv420p[i2];[i2][1:v]psnr=stats_file=$mode.log[o]" -map "[o]" -f null - ) </dev/null 2>"$out/$mode.err" \
    && [ "$(grep -c "hook skipped" "$out/$mode.err")" -le 3 ] && ! grep -q "compile status .error" "$out/$mode.err" \
    && printf "  %-44s ok\n" "$mode" || printf "  %-44s FAILED (see $out/$mode.err)\n" "$mode"
}
echo "== $CASE"
run hold   "fps=60" sw
run linear "libplacebo=fps=60:frame_mixer=linear" vk
for sh in $SHADERS; do
  cp -f "$sh" "$out/_$(basename "$sh")"
  run "$(basename "${sh%.glsl}" | sed 's/-interpolation//')" "libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_$(basename "$sh")" vk
done
echo; echo "== PSNR Y by the ground's speed at the output instant (px per SOURCE frame; the passthrough instants excluded)"
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
logs = {m: load(os.path.join(out, m + ".log")) for m in modes}
def speed(n):                      # output n (1-based) at t = (n-1)/60 s; v = 192 + 384 t px/s; per source frame /24
    t = (n - 1) / 60.0
    return (192 + 384 * t) / 24.0
bands = [(8, 12), (12, 16), (16, 20), (20, 24), (24, 28), (28, 32), (32, 36), (36, 41)]
print("  " + "band px/frame".ljust(16) + "".join(m.ljust(30) for m in modes))
for lo, hi in bands:
    row = []
    for m in modes:
        v = [x for n, x in logs[m].items() if n > 5 and n % 5 != 1 and lo <= speed(n) < hi]
        row.append(f"{statistics.mean(v):6.2f} (n={len(v):2d})" if v else "   -")
    print("  " + f"{lo:2d}-{hi:2d}".ljust(16) + "".join(r.ljust(30) for r in row))
PY
