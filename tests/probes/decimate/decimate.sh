#!/usr/bin/env bash
# Reverse interpolation through the libplacebo hook: the output rate BELOW the source rate (2026-09-11).
#
#   ./decimate.sh <shader.glsl> [<case> ...]          default cases: L1_trans_8px O5_osc_textured
#   data: $NP_SCRATCH/decimate/<case>/   (renders and per-frame psnr logs)
#
# The question (the owner, 2026-09-11): a target rate below the source -- "it wouldn't be right to simply drop
# frames for non-integer multiples and I can't see a reason this can't be reversed (interpolate to remove frames
# instead of adding them)". The hook is a function of the output instant: frame-mix-hook.patch hands the shader
# a window of source frames around each output time with their relative times, and never the ratio, so nothing
# in the shader knows whether the output is denser or sparser than the source. What has to be TESTED is the
# host: whether libplacebo's queue delivers the window when vsyncs are sparser than frames, and what the
# picture reads. The Metal host has the same question (metal-demo/prep/decimate_check.sh); this is the
# libplacebo side, which is the source of truth.
#
# Method, bench.sh's own: the 60 fps and 24 fps (or 30 fps) renders of one scene from tests/scenes.sh are the
# same function of t sampled at two rates, so output frame k of a 60 -> 24 run sits at t = k/24 s, which IS
# frame k of the 24 fps render -- the analytic truth for that instant, through the same rgb48le hop. Scored
# with ffmpeg's psnr behind format=yuv420p (psnr_y), the first five frames skipped. Three columns, as in
# bench.sh: hold (ffmpeg's own fps filter -- frame dropping), linear (stock libplacebo), the shader.
#
# What to expect:
#   60 -> 24  ratio 2.5: even k land ON a source frame (phase 0) and should read at the passthrough level
#             (about 75-77 dB, the rgb48le/fp16 round trip); odd k sit half way between two source frames
#             (phase 0.5) and should read at the shader's interpolation quality for the case. Hold gets the
#             even frames exact and the odd ones a whole half-frame wrong; linear blends the odd ones.
#   60 -> 30  integer: every output is phase 0 -- frame dropping, arrived at by the same rule and not by a
#             special case; all three columns should sit at the passthrough level.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS="$(cd "$HERE/../.." && pwd)"
export PATH="/opt/homebrew/bin:$PATH"
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"
FFMPEG="${FFMPEG:-$([ -x "$FFDIR/ffmpeg" ] && echo "$FFDIR/ffmpeg" || echo ffmpeg)}"
NP_SCRATCH="${NP_SCRATCH:-$(cd "$TESTS/../.." && pwd)/../np-scratch}"
OUTROOT="$NP_SCRATCH/decimate"
SHADER="${1:?usage: decimate.sh <shader.glsl> [case ...]}"; shift
CASES="${*:-L1_trans_8px O5_osc_textured}"
[ -f "$SHADER" ] || { echo "no shader at $SHADER"; exit 1; }
. "$TESTS/scenes.sh"

summarise() {  # <stats file> <label>
  python3 - "$1" "$2" <<'PY'
import sys, re
vals = []
for line in open(sys.argv[1]):
    m = re.search(r"n:(\d+) .*?psnr_y:([0-9.]+|inf)", line)
    if m: vals.append((int(m.group(1)), float("inf") if m.group(2) == "inf" else float(m.group(2))))
vals = [(n, v) for n, v in vals if n > 5]
def mean(xs):
    xs = [min(x, 99.0) for x in xs]          # inf (bit-exact) capped so a mean exists
    return sum(xs) / len(xs) if xs else float("nan")
ev = [v for n, v in vals if (n - 1) % 2 == 0]; od = [v for n, v in vals if (n - 1) % 2 == 1]
print("  %-10s frames %3d   all %6.2f   even-k %6.2f   odd-k %6.2f   min %6.2f" %
      (sys.argv[2], len(vals), mean([v for _, v in vals]), mean(ev), mean(od), min(v for _, v in vals)))
PY
}

for c in $CASES; do
  OUT="$OUTROOT/$c"; mkdir -p "$OUT"
  S60="$(scene "$c" 60)"
  [ "$S60" = "UNKNOWN_CASE" ] && { echo "unknown case: $c"; continue; }
  cp -f "$SHADER" "$OUT/_shader.glsl"          # bare name inside the filter argument, as bench.sh does
  for out in 24 30; do
    STRUTH="$(scene "$c" $out)"
    echo "== $c  60 -> $out  ($(basename "$SHADER"))"
    _run() { # <mode> <chain> <needs-vulkan>
      local mode="$1" chain="$2" hw=""
      [ "$3" = "vk" ] && hw="-init_hw_device vulkan=vk -filter_hw_device vk"
      # shellcheck disable=SC2086
      ( cd "$OUT" && "$FFMPEG" -y -hide_banner -loglevel error $hw \
          -f lavfi -i "$S60" -f lavfi -i "$STRUTH" \
          -filter_complex "[0:v]${chain}[ip];[ip]format=yuv420p[i2];[i2][1:v]psnr=stats_file=${mode}_$out.log[o]" \
          -map "[o]" -f null - ) 2>"$OUT/${mode}_$out.err" \
        && [ "$(grep -c "hook skipped" "$OUT/${mode}_$out.err")" -le 2 ] \
        && ! grep -q "compile status .error" "$OUT/${mode}_$out.err" \
        && summarise "$OUT/${mode}_$out.log" "$mode" \
        || { echo "  $mode FAILED:"; head -3 "$OUT/${mode}_$out.err"; }
    }
    _run hold   "fps=$out"                                                          sw
    _run linear "libplacebo=fps=$out:frame_mixer=linear"                            vk
    _run shader "libplacebo=fps=$out:frame_mixer=custom_n:custom_shader_path=_shader.glsl" vk
  done
done
echo "DECIMATE DONE"
