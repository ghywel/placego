#!/bin/sh
# dev_compile_horizon.sh (Local, L1170): one DEVELOPMENT compile of the G135 assembly draft UniformHorizon.lean. Not
# release evidence; the release check is a separately frozen and agreed stage B. It copies the validated objects of
# integration stage A (L1169) into a fresh library, compiles DenominatorBootstrap and the five stage-B modules in
# dependency order, then the draft, on Lean 4.35 with the pipeline kit's prebuilt builds and no lake. For
# OppositeCarryArcs it compiles a SCRATCH COPY with the one-line L1168 fix (`push_cast at heq` after the `change`),
# because GPT owns that source; likewise FiniteHorizonSelection gets core-only replacements for Mathlib's
# `by_contra` and `le_of_not_gt` (the file has no imports). Every module's output is printed; the first failure stops. Invoke as
#   SHARP_LEAN=<lean> KIT_ROOT=<kit> STAGE_A_LIB=<stage A lib> sh dev_compile_horizon.sh HORIZON_DIR
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
: "${SHARP_LEAN:?}"; : "${KIT_ROOT:?}"; : "${STAGE_A_LIB:?}"
mkdir "$CAPPED_OUT/src" "$CAPPED_OUT/lib"
cp "$STAGE_A_LIB"/*.olean "$STAGE_A_LIB"/*.ilean "$CAPPED_OUT/lib/" 2>/dev/null || cp "$STAGE_A_LIB"/*.olean "$CAPPED_OUT/lib/"
for name in DenominatorBootstrap FiniteHorizonSelection ContinuantSequence OppositeArcStrip OppositeCarryArcs \
    ActualOppositeCarry UniformHorizon; do
  cp "$1/$name.lean" "$CAPPED_OUT/src/$name.lean"
done
python3 - "$CAPPED_OUT/src/OppositeCarryArcs.lean" <<'PY'
import sys
p = sys.argv[1]; s = open(p).read()
old = "  change (((h : Int)-(k : Int) : Int) : ℝ)*alpha-(A : ℝ) = _ at heq\n"
assert s.count(old) == 1, 'dev patch anchor not found'
if old + "  push_cast at heq\n" in s:
    print('no dev patch needed: the source already has the L1168 fix (GC2161)')
else:
    open(p, 'w').write(s.replace(old, old + "  push_cast at heq\n"))
    print('DEV PATCH applied to the scratch copy of OppositeCarryArcs (L1168 fix)')
PY
python3 - "$CAPPED_OUT/src/FiniteHorizonSelection.lean" <<'PY'
import sys
p = sys.argv[1]; s = open(p).read()
fixes = [("  by_contra hnot\n  have ha2", "  apply Classical.byContradiction\n  intro hnot\n  have ha2"),
         ("le_of_not_gt h,hn", "(by omega),hn")]
for old, new in fixes:
    if s.count(old) == 1:
        s = s.replace(old, new); print("DEV PATCH (core-only names, L1170):", old.split(chr(10))[0].strip())
open(p, "w").write(s)
PY
shasum -a 256 "$CAPPED_OUT"/src/*.lean
lp="$CAPPED_OUT/lib:$KIT_ROOT/equivalents/.lake/build/lib/lean:$KIT_ROOT/lean/.lake/build/lib/lean"
for d in "$KIT_ROOT"/.lake/packages/*/.lake/build/lib/lean; do lp="$lp:$d"; done
export LEAN_PATH="$lp"
"$SHARP_LEAN" --version
for name in DenominatorBootstrap FiniteHorizonSelection ContinuantSequence OppositeArcStrip OppositeCarryArcs \
    ActualOppositeCarry UniformHorizon; do
  echo "== $name"
  if "$SHARP_LEAN" -j1 --root="$CAPPED_OUT/src" -o "$CAPPED_OUT/lib/$name.olean" "$CAPPED_OUT/src/$name.lean"; then
    echo "DEV_OK $name"
  else
    rm -f "$CAPPED_OUT/lib/$name.olean"; echo "DEV_FAIL $name"; exit 1
  fi
done
echo DEV_COMPILE_HORIZON_DONE
