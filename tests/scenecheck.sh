#!/bin/bash
# Verify that a scene's 60fps render really IS ground truth for its 24fps one.
#
#   ./scenecheck.sh [case...]        (default: every case in ALL_CASES)
#
# The whole ladder rests on one property: the scene's motion is a pure
# function of t, so rendering it at 60fps gives exactly what a perfect 24->60
# interpolation of the 24fps render would produce. That property is a claim
# about how the scene was WRITTEN, and nothing enforces it. A scene that
# accidentally depends on frame index, on a filter's internal state, or on a
# duration that truncates differently at the two rates still renders happily
# and still produces a full table of confident, meaningless dB figures.
#
# This checks it directly. At 24->60 every second source frame coincides in
# time with every fifth output frame (2/24 == 5/60 == 1/12 s), so those frames
# must be BIT-IDENTICAL between the two renders.
#
# The comparison is a byte compare of the selected frames, deliberately not a
# psnr. An earlier version of this script paired the two streams with
# select + setpts and psnr, and reported most of the existing ladder as broken
# -- which was a bug in the check, not in the ladder: psnr pairs by timestamp
# through framesync, and two streams whose frame durations differ do not pair
# the way the arithmetic says they should. Extracting both sides to rawvideo
# and running cmp removes timestamps from the question entirely. If you are
# tempted to reintroduce psnr here for a nicer dB figure, don't.
#
# Run it after adding or editing a scene. This is the synthetic-ladder
# equivalent of the passthrough assertion realbench.sh makes on real footage,
# and it exists for the same reason: a misaligned benchmark does not fail, it
# lies.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. "$HERE/scenes.sh"

FFMPEG="${FFMPEG:-ffmpeg}"
OUT="${OUTROOT:-${TMPDIR:-/tmp}}/scenecheck"
CASES="${*:-$ALL_CASES}"

mkdir -p "$OUT" || exit 1
printf "\n%-22s %8s   %s\n" case frames verdict
printf -- "-----------------------------------------------------------\n"

bad=0; quant=0; round=0
for CASE in $CASES; do
  S24="$(scene "$CASE" 24)"; S60="$(scene "$CASE" 60)"
  if [ "$S24" = "UNKNOWN_CASE" ]; then echo "unknown case: $CASE" >&2; bad=1; continue; fi

  # Every 2nd frame of the 24fps render, every 5th of the 60fps one.
  ( cd "$OUT" && "$FFMPEG" -y -hide_banner -loglevel error -f lavfi -i "$S24" \
      -vf "select='not(mod(n\,2))'" -fps_mode passthrough -pix_fmt yuv420p -f rawvideo "$CASE.a.raw" ) 2>"$OUT/$CASE.err"
  ( cd "$OUT" && "$FFMPEG" -y -hide_banner -loglevel error -f lavfi -i "$S60" \
      -vf "select='not(mod(n\,5))'" -fps_mode passthrough -pix_fmt yuv420p -f rawvideo "$CASE.b.raw" ) 2>>"$OUT/$CASE.err"

  sa=$(wc -c <"$OUT/$CASE.a.raw" 2>/dev/null || echo 0)
  sb=$(wc -c <"$OUT/$CASE.b.raw" 2>/dev/null || echo 0)
  FSZ=$((1280 * 720 * 3 / 2))
  n=$((sa / FSZ))
  if [ "$sa" = 0 ] || [ "$sb" = 0 ]; then
    printf "%-22s %8s   NO OUTPUT -- see %s\n" "$CASE" - "$OUT/$CASE.err"; bad=1
  elif [ "$sa" != "$sb" ]; then
    printf "%-22s %8s   *** FRAME COUNT MISMATCH (%s vs %s bytes) ***\n" "$CASE" "$n" "$sa" "$sb"; bad=1
  elif cmp -s "$OUT/$CASE.a.raw" "$OUT/$CASE.b.raw"; then
    printf "%-22s %8d   exact -- bit-identical\n" "$CASE" "$n"
  else
    # MAGNITUDE, not just presence. A 1-level difference on an anti-aliased
    # edge texel is the last bit of a rounding and means nothing; a 2px
    # displacement of the whole object is a broken scene. Both show up as
    # "not identical", so the check has to tell them apart or it is useless.
    #
    # cmp -l prints values in OCTAL, hence strtonum("0"...). Getting that
    # wrong reads 377 as 377 and quietly understates every delta.
    read -r nb mx nf <<<"$(cmp -l "$OUT/$CASE.a.raw" "$OUT/$CASE.b.raw" 2>/dev/null | awk -v fsz="$FSZ" '
      { d = strtonum("0"$2) - strtonum("0"$3); if (d < 0) d = -d
        nb++; if (d > mx) mx = d; fr[int(($1 - 1) / fsz)] = 1 }
      END { nf = 0; for (k in fr) nf++; printf "%d %d %d", nb+0, mx+0, nf }')"
    if [ "${mx:-0}" -le 2 ]; then
      printf "%-22s %8d   exact to rounding -- %s bytes, max delta %s, %s of %d frames\n" \
        "$CASE" "$n" "$nb" "$mx" "$nf" "$n"
      round=$((round + 1))
    else
      printf "%-22s %8d   *** POSITIONAL -- %s bytes, max delta %s, %s of %d frames ***\n" \
        "$CASE" "$n" "$nb" "$mx" "$nf" "$n"
      quant=$((quant + 1))
    fi
  fi
  rm -f "$OUT/$CASE.a.raw" "$OUT/$CASE.b.raw"
done
printf -- "-----------------------------------------------------------\n"
if [ "$bad" != 0 ]; then
  echo "STRUCTURAL FAILURES above -- those scenes do not render as a matched"
  echo "pair at all, and no benchmark number for them means anything."
elif [ "$quant" != 0 ]; then
  echo "$quant scene(s) POSITIONAL -- the object is in a different place at the"
  echo "same instant depending on the frame rate, so the 60fps render is not"
  echo "ground truth for the 24fps one. That is what a scene built with overlay"
  echo "does: overlay snaps its object to a whole EVEN pixel (yuv420p chroma"
  echo "alignment), so a true position of 3.2px is rendered at 2. Rebuild the"
  echo "scene analytically with _rect or _blob. See TESTING.md."
elif [ "$round" != 0 ]; then
  echo "$round scene(s) exact to rounding, the rest bit-identical. Nothing to fix."
  echo
  echo "A max delta of 1 on an anti-aliased edge texel is the last bit of a"
  echo "rounding, not a displacement: the two rates compute t a ULP apart, so a"
  echo "coverage value sitting exactly on a rounding boundary can tip. It is"
  echo "~89 dB of difference on one frame in twelve, far below anything this"
  echo "ladder resolves. Contrast the overlay scenes it replaced, which put the"
  echo "whole object 2px out."
else
  echo "all scenes exact: the 60fps render is bit-identical ground truth"
fi
exit "$bad"
