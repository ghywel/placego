#!/bin/sh
# Finite-horizon integration, stage B (Local, L1173; GPT's GC2165 plan): six modules (DenominatorBootstrap and the
# five GC2148/GC2159 modules, 25 heads) compiled in dependency order into a fresh output library that first receives
# stage A's 13 objects, each copied only after its digest matches the L1169 receipt inventory (no stage-A rebuild).
# Lean 4.35, the pipeline kit's prebuilt Mathlib, equivalents and lean builds, no lake. Each module's output must be
# exactly its own `#print axioms` reports, standard axioms only; the first failure stops the stage and deletes that
# object. Invoke as
#   SHARP_LEAN=<lean> KIT_ROOT=<kit> STAGE_A_LIB=<stage A lib> sh check_horizon_integration_b.sh HORIZON_DIR
# under run_capped.py --track-tree.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
: "${SHARP_LEAN:?select the installed 4.35 compiler explicitly}"
: "${KIT_ROOT:?the pipeline kit root with prebuilt builds}"
: "${STAGE_A_LIB:?the accepted stage A output library}"
MODULES="DenominatorBootstrap FiniteHorizonSelection ContinuantSequence OppositeArcStrip OppositeCarryArcs ActualOppositeCarry"
python3 - "$1" "$STAGE_A_LIB" <<'PY'
from pathlib import Path
import hashlib, json, os, sys
horizon, alib = Path(sys.argv[1]), Path(sys.argv[2])
objects = {
 "ActualCarrySpacing.olean": "c8166684f47203e955e6268d7781ab876ddd4bb1f1bb7aabe6d79a0c7df5eb66",
 "ActualContinuants.olean": "8f55f2caca30dec40f94b563514a0d8e10c66ecc3a1c12d49b58e31eb8029dd5",
 "ArcBreakBounds.olean": "48c36b7523beb10602646c9102e1c77c0d2a5478a07bd62bb12d4f1d3ae34e1d",
 "ArcBreakSequence.olean": "c683609e3af6c616445f80d2a990f4bcd32dd631561741ee009bfa8463be429d",
 "ArcContinuantsDraft.olean": "36b100804fdd31545a51bb5b90fd71673719da37e77e4f77e5745767b356e8d8",
 "ArcCoverDraft.olean": "4ba756c6476aa81f094ec7acffd0e27afd5b7b1b9baf4cfe33f1cb05c40db78b",
 "ArcDeterminantDraft.olean": "6e6b17632f7436f85f043b6f6608474bf730c75a562c9d26a15a54e88653dc74",
 "ArcRotationDraft.olean": "bc6d79c9cbf12e1ed10deb21d6a774464ee2fd5d8eea8d4d8836ba9a76cae8a8",
 "ArcStepCodeDraft.olean": "315adc5d8a6df69981275466ce0254612a3b54f688de313de4e189bce1603c94",
 "CarryReturnSpacing.olean": "86750af7063e00867ff8a44b1c14bcdd36a16a79009b11767486ea25754e65c2",
 "FiniteHorizonBounds.olean": "fb472c9e76d1f3ed212df2dab24d153fb607c4bfc15378b24fd698d439eb590e",
 "MechanicalCarry.olean": "861c510464432d8377bb10f5fa94cab419d75783bdf533c100ec10067301a4bc",
 "SharpAdjacentReturn.olean": "bd397fdaa5f631f3ce7bf2bb587f5087427cfee901980c9cbfeaf2531547c0cc"
}
pins = [["DenominatorBootstrap", "c9c8cbe4b3eb9b46cb7f87e32c26668c6a4245bd82a1a7d5a2ef6e2c4d4ae729"], ["FiniteHorizonSelection", "87e28fe781a06684e24db3d0707c74e96579248e7948383681083b64e523f88a"], ["ContinuantSequence", "430d45dbd2cfe47ec9740a047f544f0d1887f897ca46c1dd85ec5076f9d3afbb"], ["OppositeArcStrip", "3151c0511b5aac522279e1d6f6be8b825715b1837d890da86aa9d0df769b6d93"], ["OppositeCarryArcs", "7f47629a93f59263274399abd1785d9e9dbe9f842b0fc2789fc16d48c4eb8e7f"], ["ActualOppositeCarry", "0c02e7ae932cffe44e5d160a329243b026b29cc8771e7d4934395aa6cf58ec25"]]
out = Path(os.environ['CAPPED_OUT'])
(out / 'src').mkdir(); (out / 'lib').mkdir()
for name, digest in objects.items():
    data = (alib / name).read_bytes()
    if hashlib.sha256(data).hexdigest() != digest:
        raise SystemExit('REFUSED: stage A object digest mismatch for ' + name)
    (out / 'lib' / name).write_bytes(data)
print('STAGE_A_OBJECTS_OK', len(objects), flush=True)
expected = {}
for name, digest in pins:
    data = (horizon / (name + '.lean')).read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    if actual != digest:
        raise SystemExit('REFUSED: frozen digest mismatch for ' + name + ' ' + actual)
    (out / 'src' / (name + '.lean')).write_bytes(data)
    expected[name] = [l.split()[2] for l in data.decode().splitlines() if l.startswith('#print axioms ')]
(out / 'expected.json').write_text(json.dumps(expected, indent=1) + '\n')
print('SOURCES_OK', sum(len(v) for v in expected.values()), 'axiom reports expected', flush=True)
PY
path="$CAPPED_OUT/lib:$KIT_ROOT/equivalents/.lake/build/lib/lean:$KIT_ROOT/lean/.lake/build/lib/lean"
for d in "$KIT_ROOT"/.lake/packages/*/.lake/build/lib/lean; do
  [ -d "$d" ] || { echo "FAIL: missing package build $d"; exit 1; }
  path="$path:$d"
done
export LEAN_PATH="$path"
"$SHARP_LEAN" --version
for name in $MODULES; do
  if ! "$SHARP_LEAN" -j1 --root="$CAPPED_OUT/src" -o "$CAPPED_OUT/lib/$name.olean" "$CAPPED_OUT/src/$name.lean" \
      > "$CAPPED_OUT/$name.txt" 2>&1; then
    cat "$CAPPED_OUT/$name.txt"; rm -f "$CAPPED_OUT/lib/$name.olean"; echo "FAIL: compile $name"; exit 1
  fi
  python3 - "$name" <<'PY' || { rm -f "$CAPPED_OUT/lib/$name.olean"; exit 1; }
from pathlib import Path
import json, os, re, sys
name, out = sys.argv[1], Path(os.environ['CAPPED_OUT'])
want = json.loads((out / 'expected.json').read_text())[name]
text = (out / (name + '.txt')).read_text()
print('== ' + name); print(text, end='')
line_re = re.compile(r"^'([\w.]+)' (?:depends on axioms: \[(.*)\]|does not depend on any axioms)$")
seen = []
for line in text.splitlines():
    if not line.strip():
        continue
    m = line_re.fullmatch(line)
    axioms = {a.strip() for a in ((m.group(2) or '') if m else '').split(',') if a.strip()}
    if not m or m.group(1) not in want or not axioms <= {'propext', 'Classical.choice', 'Quot.sound'}:
        raise SystemExit('FAIL: ' + name + ': unexpected line: ' + line)
    seen.append(m.group(1))
if sorted(seen) != sorted(want):
    raise SystemExit('FAIL: ' + name + ': %d of %d axiom reports, or repeats' % (len(seen), len(want)))
print('MODULE_PASS ' + name, flush=True)
PY
done
echo 'HORIZON_INTEGRATION_B_PASS (6 modules)'
