#!/bin/bash
# Report interpolation error AT EDGES separately from everywhere else.
#
#   ./edgeerror.sh <segment> [variant...]
#
# Run realbench.sh first -- this reads the rendered outputs it leaves in
# OUTROOT. See edgeerror.py's docstring for why a whole-frame metric is not
# enough, especially for flat-shaded animation.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FFMPEG="${FFMPEG:-ffmpeg}"
OUTROOT="${OUTROOT:-${TMPDIR:-/tmp}/interp-real}"
TMP="${TMPDIR:-/tmp}/interp-edge"
mkdir -p "$TMP"

S="${1:?usage: edgeerror.sh <segment> [variant...]}"
shift
VARIANTS=("$@")
[ ${#VARIANTS[@]} -eq 0 ] && VARIANTS=(linear gen1 gen5 gen6)

# synthesised frames only (the retained ones are passthrough for every mode)
SEL="between(n,0,71)*eq(mod(n,2),1)"

dump() { # <src> <dst> [extra filter]
  "$FFMPEG" -y -hide_banner -loglevel error -i "$1" \
    -vf "setpts=N/TB,select='$SEL',format=gray${3:+,$3}" \
    -fps_mode passthrough -f rawvideo "$2" 2>/dev/null
}

dump "$OUTROOT/ref_$S.mkv" "$TMP/ref.raw"
dump "$OUTROOT/ref_$S.mkv" "$TMP/edge.raw" "sobel"
for v in "${VARIANTS[@]}"; do
  [ -s "$OUTROOT/o_${v}_$S.mkv" ] && dump "$OUTROOT/o_${v}_$S.mkv" "$TMP/$v.raw"
done

W=$("$FFMPEG" -hide_banner -loglevel error -i "$OUTROOT/ref_$S.mkv" -f null - 2>&1 >/dev/null; \
    "${FFPROBE:-ffprobe}" -v error -select_streams v:0 -show_entries stream=width -of csv=p=0 "$OUTROOT/ref_$S.mkv")
H=$("${FFPROBE:-ffprobe}" -v error -select_streams v:0 -show_entries stream=height -of csv=p=0 "$OUTROOT/ref_$S.mkv")
W="$W" H="$H" python3 "$HERE/edgeerror.py" "$TMP" "${VARIANTS[@]}"
