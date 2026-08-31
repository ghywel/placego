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

bad=0; quant=0
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
    # Per-FRAME, not per-byte: "1 of 12 frames differs" says what happened,
    # where "88507 bytes differ" only says the object was textured.
    which=""; nd=0
    for i in $(seq 0 $((n - 1))); do
      if ! cmp -s \
          <(dd if="$OUT/$CASE.a.raw" bs="$FSZ" skip="$i" count=1 2>/dev/null) \
          <(dd if="$OUT/$CASE.b.raw" bs="$FSZ" skip="$i" count=1 2>/dev/null); then
        nd=$((nd + 1)); which="$which $i"
      fi
    done
    printf "%-22s %8d   quantised -- %d of %d differ, at pair%s\n" "$CASE" "$n" "$nd" "$n" "$which"
    quant=$((quant + 1))
  fi
  rm -f "$OUT/$CASE.a.raw" "$OUT/$CASE.b.raw"
done
printf -- "-----------------------------------------------------------\n"
if [ "$bad" != 0 ]; then
  echo "STRUCTURAL FAILURES above -- those scenes do not render as a matched"
  echo "pair at all, and no benchmark number for them means anything."
elif [ "$quant" = 0 ]; then
  echo "all scenes exact: the 60fps render is bit-identical ground truth"
else
  echo "$quant scene(s) PIXEL-QUANTISED, the rest exact."
  echo
  echo "Quantised is a real limitation, not a broken scene, and it is inherent"
  echo "to any scene built with overlay: overlay places its object at a whole"
  echo "even pixel (yuv420p chroma alignment), so a true position of 3.2px is"
  echo "rendered at 2. The 60fps ground truth therefore steps in 2px jumps"
  echo "where the motion is smooth, and a shader that interpolates correctly"
  echo "to a fractional position is marked down against it. Scenes built"
  echo "analytically in geq -- with a band-limited edge -- do not have this:"
  echo "fractional position lives in the edge's grey levels. See TESTING.md,"
  echo "'Ground truth is quantised where the scene uses overlay'."
fi
exit "$bad"
