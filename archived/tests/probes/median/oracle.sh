#!/bin/bash
# Does REAL content want different shaders? (2026-09-09, the planning question.)
#
# The synthetic ladder says perfect per-case selection over the eight existing shaders would buy +1.02 dB
# over always using the best single file -- but the ladder's cases are PURE, one structure each, while a real
# frame contains several at once and their gains and losses cancel inside it. That is exactly what the median
# experiment showed: +-8 dB across pure cases, +0.00 to +0.06 dB across fifteen real segments.
#
# So measure the thing the ladder cannot answer: five shaders across the same real segments, per segment, on
# two live-action films and a cartoon. If the winner changes with the content and the spread is worth having,
# targeting has headroom on real material and the family-tree plan is justified. If one file wins nearly
# everywhere and the spread is small, it is not.
# One GPU job at a time.
set -u
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs
export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH" FFMPEG="$FFDIR/ffmpeg.exe" FFPROBE="$FFDIR/ffprobe.exe"
SC="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"; NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; G="$NP/median"
cd "$SC/tests"
echo "########## ORACLE-ON-FILM start $(date +%T)"
LABELS=(vp2 prop2 quadp tri quint)
FILES=(bidirectional-interpolation-variational-propagated.glsl
       bidirectional-interpolation-propagated.glsl
       quaddirectional-interpolation-propagated.glsl
       tridirectional-interpolation-propagated.glsl
       quintdirectional-interpolation-propagated.glsl)
run() {
  local src="$1" tag="$2"; shift 2
  echo "  -- $tag: $(basename "$src"), ${#LABELS[@]} shaders x $# segments [$*]"
  export OUTROOT="$G/oracle_$tag"; rm -rf "$OUTROOT"; mkdir -p "$OUTROOT"
  local i
  for i in "${!LABELS[@]}"; do
    local t0=$(date +%s)
    bash ./realbench.sh "$src" "${LABELS[$i]}" "$SC/shaders/${FILES[$i]}" "$@" < /dev/null 2>&1 \
      | grep -iE "FAIL|ALARM" | head -2 | sed "s/^/    [$tag ${LABELS[$i]}] /"
    echo "     ${LABELS[$i]} $(( $(date +%s) - t0 )) s"
  done
  echo "  == $tag"; python ./realanalyze.py "${LABELS[@]}" 2>&1 | grep -E "^PSNR" | head -9
}
run "$NP/avengers.mp4"        avengers 600 1800 3000 4200 5400 7200
run "$NP/backtothefuture.mkv" bttf     600 1800 3000 4200 5400 6600
run "$NP/bluey.mkv"           bluey    60 120 180 240 300 360
echo "ORACLE-ON-FILM DONE $(date +%T)"
