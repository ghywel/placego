#!/bin/bash
# Has an animation-motivated fix polluted the general path? (2026-09-09, his question.)
# The coarse vector median entered the general shader at bd92eea explicitly to fix a cartoon face defect.
# It was gated then on ONE film clip and an older shader; the recommendation has changed twice since and the
# ladder has grown from ~30 cases to 42. So: the CURRENT recommendation with its two Q-level median passes,
# against the same file generated with none, on the whole ladder. One GPU job at a time.
set -u
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs
export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH" FFMPEG="$FFDIR/ffmpeg.exe" FFPROBE="$FFDIR/ffprobe.exe"
SC="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"; NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; G="$NP/median"
export OUTROOT="$G/ladder"; mkdir -p "$OUTROOT"
cd "$SC/tests"
echo "########## MEDIAN LADDER start $(date +%T) at $(cd $SC && git rev-parse --short HEAD)"
for pair in "vp $SC/shaders/bidirectional-interpolation-variational-propagated.glsl" "vpnm $G/vp-nomedian.glsl"; do
  set -- $pair; t0=$(date +%s)
  bash ./bench.sh all "$2" "$1" < /dev/null 2>&1 | grep -iE "FAIL|error" | head -3 | sed "s/^/    [$1] /"
  echo "  $1 done in $(( $(date +%s) - t0 )) s ($(date +%T))"
done
python ./analyze.py --variants 2>&1 | tee "$G/ladder-table.txt" | head -50
echo "MEDIAN LADDER DONE $(date +%T)"
