#!/bin/bash
# Re-run ONLY the zero-seed ablation, now that the variant genuinely differs from the control.
set -u
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs
export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH" FFMPEG="$FFDIR/ffmpeg.exe" FFPROBE="$FFDIR/ffprobe.exe"
SC="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"; NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; G="$NP/ablate"
cd "$SC/tests"
echo "########## RESEED start $(date +%T)"
export OUTROOT="$G/ladder"
rm -f "$OUTROOT"/*/noseed.log
bash ./bench.sh all "$G/noseed.glsl" noseed < /dev/null 2>&1 | grep -iE "FAIL|error" | head -2
python ./analyze.py --variants 2>&1 | tee "$G/ladder-table.txt" | head -4
for pair in "avengers.mp4 avengers 600 3000 5400" "backtothefuture.mkv bttf 600 3000 5400" "bluey.mkv bluey 60 180 300"; do
  set -- $pair; src=$1; tag=$2; shift 2
  export OUTROOT="$G/real_$tag"
  rm -f "$OUTROOT"/*/noseed.log 2>/dev/null
  bash ./realbench.sh "$NP/$src" noseed "$G/noseed.glsl" "$@" < /dev/null 2>&1 | grep -iE "FAIL|ALARM" | head -2
  echo "  -- $tag"; python ./realanalyze.py vp noseed novar nomed 2>&1 | grep -E "^PSNR MEAN"
done
echo "RESEED DONE $(date +%T)"
