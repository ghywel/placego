#!/bin/bash
# The FULL variational is where bd92eea's cartoon fix actually lives (medians at S, E and Q). The
# recommendation carries only the Q pair, and its flow proved identical with and without them (2 pixels in
# 104 million differing by one quantisation step). So test the file that HAS the feature: 2,2,2,0 against
# 0,0,0,0, on the whole ladder and then on the cartoon it was built for and on live action.
# One GPU job at a time.
set -u
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs
export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH" FFMPEG="$FFDIR/ffmpeg.exe" FFPROBE="$FFDIR/ffprobe.exe"
SC="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"; NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; G="$NP/median"
VAR="$SC/shaders/bidirectional-interpolation-variational.glsl"
VARNM="$G/var-nomedian.glsl"
cd "$SC/tests"
echo "########## VARIATIONAL MEDIAN start $(date +%T)"

export OUTROOT="$G/ladder2"; mkdir -p "$OUTROOT"
for lab in var varnm; do
  [ "$lab" = var ] && sh="$VAR" || sh="$VARNM"
  t0=$(date +%s)
  bash ./bench.sh all "$sh" "$lab" < /dev/null 2>&1 | grep -iE "FAIL|error" | head -3 | sed "s/^/    [$lab] /"
  echo "  $lab done in $(( $(date +%s) - t0 )) s ($(date +%T))"
done
python ./analyze.py --variants 2>&1 | tee "$G/ladder2-table.txt" | head -6

# segments passed as positional arguments; no environment-variable prefix on a function call
run() {
  local src="$1" tag="$2"; shift 2
  echo "  -- $tag: $(basename "$src"), segments [$*]"
  export OUTROOT="$G/real2_$tag"; rm -rf "$OUTROOT"; mkdir -p "$OUTROOT"
  local lab sh
  for lab in var varnm; do
    [ "$lab" = var ] && sh="$VAR" || sh="$VARNM"
    bash ./realbench.sh "$src" "$lab" "$sh" "$@" < /dev/null 2>&1 \
      | grep -iE "FAIL|ALARM" | head -2 | sed "s/^/    [$tag $lab] /"
  done
  echo "     logs: $(find "$OUTROOT" -name '*.log' | wc -l)"
  python ./realanalyze.py var varnm 2>&1 | grep -E "MEAN"
}
run "$NP/bluey.mkv"    bluey    60 120 180 240 300
run "$NP/avengers.mp4" avengers 600 1800 3000 4200 5400
echo "VARIATIONAL MEDIAN DONE $(date +%T)"
