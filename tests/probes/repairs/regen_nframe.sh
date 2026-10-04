#!/bin/bash
# regen_nframe.sh <outdir>: rebuild the eight N-frame shaders with the generators as they stand, into <outdir>, and
# say for each whether its body (after the generated header, as smoke.sh compares) matches the committed file.
# REPAIRS.md lead L1 (2026-10-04): the control before a generator change, and the check after it.
set -u
OUT=${1:?outdir}; mkdir -p "$OUT"
S="$(cd "$(dirname "$0")/../../.." && pwd)"          # scripts/
PY=${PY:-$HOME/np-build/venv/bin/python3}
cd "$S"
strip() { awk 'p{print} /^\/\/ =====/{c++} c==2 && !p{p=1}' "$1"; }
run() { local name=$1; shift; env "$@" > "$OUT/$name.log" 2>&1 || { echo "  FAILED $name: $(tail -1 "$OUT/$name.log")"; return 1; }; }
run quaddirectional-interpolation $PY tests/gen_quaddirectional.py "$OUT/quaddirectional-interpolation.glsl" bidirectional-interpolation.glsl
for v in seeded propagated animation; do
  run quaddirectional-interpolation-$v $PY tests/gen_quaddirectional.py "$OUT/quaddirectional-interpolation-$v.glsl" bidirectional-interpolation-$v.glsl
done
run quaddirectional-interpolation-propagated-cadence CADENCE=1 $PY tests/gen_quaddirectional.py "$OUT/quaddirectional-interpolation-propagated-cadence.glsl" bidirectional-interpolation-propagated.glsl
run quintdirectional-interpolation-propagated $PY tests/gen_quintdirectional.py "$OUT/quintdirectional-interpolation-propagated.glsl" bidirectional-interpolation-propagated.glsl
run sextdirectional-interpolation-propagated $PY tests/gen_sextdirectional.py "$OUT/sextdirectional-interpolation-propagated.glsl" bidirectional-interpolation-propagated.glsl
run human-reading-quad $PY tests/gen_quaddirectional.py "$OUT/human-reading-quad.glsl" bidirectional-interpolation-propagated.glsl \
  && run human-reading-quad-tail $PY tests/add_human_reading.py "$OUT/human-reading-quad.glsl" --default 1
for f in "$OUT"/*.glsl; do
  n=$(basename "$f")
  if diff -q <(strip "$f") <(strip "shaders/$n") >/dev/null; then echo "  same     $n"
  else echo "  DIFFERS  $n ($(diff <(strip "$f") <(strip "shaders/$n") | grep -c '^[<>]') lines)"; fi
done
