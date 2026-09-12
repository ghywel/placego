#!/usr/bin/env bash
# The identity check for the master tier (2026-09-12): tests/masters.py against the Metal demo engine's
# own exports, scene by scene, to the last 16-bit level. The engine is the demo's; this file is the
# record's -- they must agree, or one of them is wrong.
#
#   ./identity.sh <outdir> [WxH] [scenes...]        needs $QUADDEMO (the demo CLI) and python3 + numpy
#   N=<source frames> (6)   TEXTURE=<name>   BG=flat|textured   -- passed to both sides
#
# For each scene: N source frames at 24 fps and the 60 fps truth of those, from both; prints the largest
# absolute difference in 16-bit levels and the count of differing samples. 0 / 0 is identity; a level or
# two on a handful of samples is libm (the two hosts' sin/cos differ in the last bit and the rounding to
# 16 bits sometimes lands either side); anything more is a law that does not match.
set -u
OUT="$1"; SIZE="${2:-640x360}"; shift; shift 2>/dev/null || true
SCENES="${*:-bounce-constant bounce-oscillating bounce-hardjerk bounce-gravity bounce-masses breathe breathe-spin spin-constant spin-accelerating spin-pendulum roll-12 roll-12-fast roll-wagon static}"
QUAD="${QUADDEMO:?set QUADDEMO to the demo CLI}"
PY="${PYTHON:-python3}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
N="${N:-6}"
EXTRA="${TEXTURE:+--texture $TEXTURE} ${BG:+--bg $BG}"
mkdir -p "$OUT"
W=${SIZE%x*}; H=${SIZE#*x}
for sc in $SCENES; do
  "$QUAD" --scene "$sc" --frames "$N" --src-fps 24 --out-fps 60 --size "$SIZE" --settle 0 $EXTRA \
          --export-source "$OUT/$sc.eng.src" --export-truth "$OUT/$sc.eng.truth" > /dev/null 2>&1 || { echo "$sc: engine export failed"; continue; }
  "$PY" "$HERE/../../masters.py" "$sc" --size "$SIZE" --frames "$N" --src-fps 24 --out-fps 60 --settle 0 $EXTRA \
          --export-source "$OUT/$sc.py.src" --export-truth "$OUT/$sc.py.truth" > /dev/null || { echo "$sc: masters.py failed"; continue; }
  "$PY" "$HERE/identity_diff.py" "$OUT" "$sc" "$W" "$H"
  rm -f "$OUT/$sc".{eng,py}.{src,truth}
done
