#!/bin/bash
# Content drawn on twos, scored exactly (2026-09-19). The owner's question of the day: other players interpolate
# cartoon and anime; ours struggles; what are we missing? One candidate is not an estimator mechanism at all but
# the CADENCE: animation is often drawn at 12 drawings a second and delivered at 24 (each drawing held for two
# frames, "on twos"). A shader that sees the pair (A, A) outputs a hold and then moves across the next pair
# (A, B), so the output judders at twelve holds and twelve moves a second, however good the estimator. The
# record says a cel shot on twos cannot be SCORED by decimate-and-reconstruct (hold wins, because the deleted
# frames are duplicates of the ones kept). It can be scored here, because the ladder's truth is the scene's
# motion itself: the native 60 fps render of a continuous motion is the exact answer for ANY source of it.
#
# Three sources of one scene, one truth:
#   ones   the scene at 24 fps                          -> 60      (the ladder as it is: the reference)
#   twos   the scene at 12 fps, each frame doubled to 24 -> 60      (what an on-twos file does to us today)
#   dedup  the scene at 12 fps                          -> 60      (the ceiling: a perfect duplicate remover
#                                                                    would hand the shader this; 5x, doubled motion)
# scored by the same psnr against the same 60 fps truth, for hold, linear and the shaders given. The prize of
# cadence handling is dedup minus twos; whether the shader is up to the doubled motion is dedup against ones.
#
#   ./twos.sh [case ...]            default: L1_trans_8px O5_osc_textured A5_accel_tex_a067 R3_rot_tex
#   SHADERS="a.glsl b.glsl" ./twos.sh ...   shaders to run (default: the recommendation and the quad-propagated)
#   SRCS="lossy lossy-mpd" ./twos.sh ...   only these sources (the summary still reads every column that exists)
#
# Reading it: analyze.py excludes every fifth output frame as a passthrough. On the twos source that exclusion
# still removes the frames the hook copies, but half of THOSE are the duplicates, whose true frame is a moved
# one -- so the twos column is, if anything, flattered. The numbers to compare are the rows against each other.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS="$(cd "$HERE/../.." && pwd)"
. "$TESTS/scenes.sh"
FFMPEG="${FFMPEG:-${FFDIR:-$HOME/np-build/ffmpeg}/ffmpeg}"
PY="${PY:-$HOME/np-build/venv/bin/python3}"
NP_SCRATCH="${NP_SCRATCH:-$(cd "$TESTS/../../.." && pwd)/np-scratch}"
OUTROOT="${OUTROOT:-$NP_SCRATCH/twos}"; mkdir -p "$OUTROOT"
SHADERS="${SHADERS:-$TESTS/../shaders/bidirectional-interpolation-variational-propagated.glsl $TESTS/../shaders/quaddirectional-interpolation-propagated.glsl}"
CASES=("$@"); [ ${#CASES[@]} -gt 0 ] || CASES=(L1_trans_8px O5_osc_textured A5_accel_tex_a067 R3_rot_tex)

run() {   # <out dir> <mode label> <source lavfi or file> <truth lavfi> <filter chain> <vk?>
  local out="$1" mode="$2" src="$3" truth="$4" chain="$5" hw="" fmt="-f lavfi"
  [ "$6" = vk ] && hw="-init_hw_device vulkan=vk -filter_hw_device vk"
  [ -f "$src" ] && fmt=""                                   # a file source (the lossy encode) instead of a lavfi one
  ( cd "$out" && "$FFMPEG" -y -hide_banner -loglevel error $hw $fmt -i "$src" -f lavfi -i "$truth" \
      -filter_complex "[0:v]${chain}[ip];[ip]format=yuv420p[i2];[i2][1:v]psnr=stats_file=$mode.log[o]" -map "[o]" -f null - ) 2>"$out/$mode.err" \
    && [ "$(grep -c "hook skipped" "$out/$mode.err")" -le 2 ] && ! grep -q "compile status .error" "$out/$mode.err" \
    && printf "  %-28s ok\n" "$mode" || printf "  %-28s FAILED (see $out/$mode.err)\n" "$mode"
}
sc() {   # the ladder's scenes, the edge series included (scenes.sh serves those from scene_edge)
  local s; s="$(scene "$1" "$2")"; [ "$s" != UNKNOWN_CASE ] || s="$(scene_edge "$1" "$2")"; echo "$s"
}
for CASE in "${CASES[@]}"; do
  S24="$(sc "$CASE" 24)"; S12="$(sc "$CASE" 12)"; S60="$(sc "$CASE" 60)"; S8="$(sc "$CASE" 8)"
  [ "$S24" != "UNKNOWN_CASE" ] || { echo "unknown case: $CASE" >&2; continue; }
  echo "== $CASE"
  # The lossy file of the twos source: what an on-twos film file looks like -- the held drawings are no longer
  # byte-identical (the encoder perturbs them), which is what a duplicate detector must cope with.
  LOSSY="$OUTROOT/$CASE/twos-lossy.mp4"
  for try in 1 2 3; do   # the hardware encoder refuses now and then straight after a run of Vulkan renders; asked again it obliges
    [ -s "$LOSSY" ] && break
    "$FFMPEG" -y -hide_banner -loglevel error -f lavfi -i "$S12,fps=24" -c:v h264_videotoolbox -b:v 4M -pix_fmt yuv420p "$LOSSY" </dev/null 2>"$OUTROOT/$CASE/lossy-encode.err" || sleep 2
  done
  [ -s "$LOSSY" ] || { echo "  the lossy encode of $CASE failed ($(head -c 200 "$OUTROOT/$CASE/lossy-encode.err")); its two columns will be empty" >&2; }
  # The dropper: this build has no mpdecimate, so the select filter's scene score does it -- a frame whose
  # difference from the last kept one is below the threshold is dropped, and the kept frames keep their
  # timestamps, so the hook interpolates across the gap by time. 0.002 separates the synthetic files'
  # duplicates (0.000000-0.000004) from their moves (0.0076); a real encode of real anime needs a detector
  # that reads the cadence pattern, not an absolute threshold (held drawings scored 0.0056 there, small
  # moves 0.0126 -- measured 2026-09-19).
  DROP="select='eq(n,0)+gt(scene,${DROP_T:-0.002})',"
  for src in ${SRCS:-ones twos threes dedup mpd lossy lossy-mpd}; do   # SRCS="lossy lossy-mpd" to fill columns in
    out="$OUTROOT/$CASE/$src"; mkdir -p "$out"
    pre=""
    case $src in
      ones)      in="$S24" ;;
      twos)      in="$S12,fps=24" ;;                       # each 12 fps frame held for two 24 fps frames
      threes)    in="$S8,fps=24" ;;                        # each 8 fps frame held for three (a threes run needs a window longer than four)
      dedup)     in="$S12" ;;                              # the ceiling: the duplicates never existed
      mpd)       in="$S12,fps=24"; pre="$DROP" ;;         # the dropper in front of the interpolator, exact duplicates
      lossy)     in="$LOSSY" ;;                            # the twos source after a real encoder
      lossy-mpd) in="$LOSSY"; pre="$DROP" ;;              # the dropper on the encoder's near-duplicates
    esac
    run "$out" hold   "$in" "$S60" "${pre}fps=60" sw
    run "$out" linear "$in" "$S60" "${pre}libplacebo=fps=60:frame_mixer=linear" vk
    for sh in $SHADERS; do
      cp -f "$sh" "$out/_$(basename "$sh")"
      run "$out" "$(basename "${sh%.glsl}" | sed 's/-interpolation//')" "$in" "$S60" "${pre}libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_$(basename "$sh")" vk
    done
  done
done
echo; echo "== summary (PSNR Y mean over the scored output frames; the truth is the native 60 fps render in every row)"
"$PY" - "$OUTROOT" "${CASES[@]}" <<'PY'
import sys, os, re, statistics
root, cases = sys.argv[1], sys.argv[2:]
def mean_psnr(path):
    v = []
    for line in open(path, errors="replace"):
        m = re.search(r"psnr_y:([0-9.]+|inf)", line); n = re.match(r"n:(\d+)", line)
        if m and n:
            k = int(n.group(1))
            if k > 5 and k % 5 != 1: v.append(99.0 if m.group(1) == "inf" else float(m.group(1)))   # the hook's passthrough instants excluded, as analyze.py does
    return statistics.mean(v) if v else float("nan")
for c in cases:
    srcs = ("ones", "twos", "threes", "dedup", "mpd", "lossy", "lossy-mpd")
    modes = sorted({f[:-4] for s in srcs for f in os.listdir(os.path.join(root, c, s)) if f.endswith(".log") and not f.startswith("_") and not f.startswith("._")})
    print(f"\n{c}")
    print(f"  {'mode':30s} {'ones':>8s} {'twos':>8s} {'threes':>8s} {'dedup':>8s} {'mpd':>8s} {'lossy':>8s} {'lossy-mpd':>10s}   {'prize':>7s}")
    for m in modes:
        vals = []
        for s in srcs:
            p = os.path.join(root, c, s, m + ".log")
            vals.append(mean_psnr(p) if os.path.exists(p) else float("nan"))
        prize = vals[3] - vals[1]
        print(f"  {m:30s} " + " ".join(f"{v:8.2f}" for v in vals[:6]) + f" {vals[6]:10.2f}   {prize:+7.2f}")
PY
