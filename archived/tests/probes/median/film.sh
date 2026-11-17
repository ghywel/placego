#!/bin/bash
# The film side of the median question (2026-09-09): the recommendation with its two Q-level median passes
# against the same file with none, on LIVE ACTION and on the CARTOON the median was built for.
#
# The cartoon is the control that must move the OTHER WAY. If removing the median helps film and hurts the
# cartoon, the feature works and is mispriced for film -- a fork, as PROP_DISAGREE already is. If it hurts
# both, there is no pollution. If it helps both, it has outlived its purpose.
#
# Segments are passed as arguments, not through an environment variable prefixing a function call: that form
# is subtle in bash and would silently fall back to realbench's defaults.
# One GPU job at a time; run after the ladder.
set -u
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs
export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH" FFMPEG="$FFDIR/ffmpeg.exe" FFPROBE="$FFDIR/ffprobe.exe"
SC="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"; NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; G="$NP/median"
cd "$SC/tests"
echo "########## MEDIAN FILM start $(date +%T)"

run() {  # <source> <tag> <segments...>
  local src="$1" tag="$2"; shift 2
  local segs="$*"
  echo "  -- $tag: $(basename "$src"), segments [$segs]"
  export OUTROOT="$G/real_$tag"; rm -rf "$OUTROOT"; mkdir -p "$OUTROOT"
  local pair
  for pair in "vp $SC/shaders/bidirectional-interpolation-variational-propagated.glsl" "vpnm $G/vp-nomedian.glsl"; do
    set -- $pair
    bash ./realbench.sh "$src" "$1" "$2" $segs < /dev/null 2>&1 \
      | grep -iE "FAIL|ALARM|error" | head -2 | sed "s/^/    [$tag $1] /"
  done
  echo "     logs written: $(find "$OUTROOT" -name '*.log' | wc -l) (expect 2 per segment plus the baselines)"
  python ./realanalyze.py vp vpnm 2>&1 | grep -vE "^$" | head -14
}

run "$NP/avengers.mp4"          avengers  600 1800 3000 4200 5400
run "$NP/backtothefuture.mkv"   bttf      600 1800 3000 4200 5400
run "$NP/bluey.mkv"             bluey     60 120 180 240 300
echo "MEDIAN FILM DONE $(date +%T)"
