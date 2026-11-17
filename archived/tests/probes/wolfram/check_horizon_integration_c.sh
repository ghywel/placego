#!/bin/sh
# Finite-horizon integration, stage C (Local, L1174, PROPOSED; GPT's GC2165 plan): the assembly, four modules
# (UniformHorizon, RecodedHorizon, ArcRule30BridgeDraft, PhysicalHorizon; 21 heads), compiled in dependency order into
# a fresh output library that first receives stage B's 19 objects (A's 13 and B's 6), each copied only after its
# digest matches the L1174 receipt inventory. Lean 4.35, the pipeline kit's prebuilt builds, no lake; stage A's
# per-module gates. Invoke as
#   SHARP_LEAN=<lean> KIT_ROOT=<kit> STAGE_B_LIB=<stage B lib> sh check_horizon_integration_c.sh HORIZON_DIR ARC_DIR
# under run_capped.py --track-tree.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
: "${SHARP_LEAN:?select the installed 4.35 compiler explicitly}"
: "${KIT_ROOT:?the pipeline kit root with prebuilt builds}"
: "${STAGE_B_LIB:?the stage B output library}"
MODULES="UniformHorizon RecodedHorizon ArcRule30BridgeDraft PhysicalHorizon"
python3 - "$1" "$2" "$STAGE_B_LIB" <<'PY'
from pathlib import Path
import hashlib, json, os, sys
dirs = {'H': Path(sys.argv[1]), 'A': Path(sys.argv[2])}
blib = Path(sys.argv[3])
objects = {
 "ActualCarrySpacing.olean": "c8166684f47203e955e6268d7781ab876ddd4bb1f1bb7aabe6d79a0c7df5eb66",
 "ActualContinuants.olean": "8f55f2caca30dec40f94b563514a0d8e10c66ecc3a1c12d49b58e31eb8029dd5",
 "ActualOppositeCarry.olean": "43b84823b7c83363ffb46dc8a10fcaf5b821f328d925e75a3ecbecc787f61832",
 "ArcBreakBounds.olean": "48c36b7523beb10602646c9102e1c77c0d2a5478a07bd62bb12d4f1d3ae34e1d",
 "ArcBreakSequence.olean": "c683609e3af6c616445f80d2a990f4bcd32dd631561741ee009bfa8463be429d",
 "ArcContinuantsDraft.olean": "36b100804fdd31545a51bb5b90fd71673719da37e77e4f77e5745767b356e8d8",
 "ArcCoverDraft.olean": "4ba756c6476aa81f094ec7acffd0e27afd5b7b1b9baf4cfe33f1cb05c40db78b",
 "ArcDeterminantDraft.olean": "6e6b17632f7436f85f043b6f6608474bf730c75a562c9d26a15a54e88653dc74",
 "ArcRotationDraft.olean": "bc6d79c9cbf12e1ed10deb21d6a774464ee2fd5d8eea8d4d8836ba9a76cae8a8",
 "ArcStepCodeDraft.olean": "315adc5d8a6df69981275466ce0254612a3b54f688de313de4e189bce1603c94",
 "CarryReturnSpacing.olean": "86750af7063e00867ff8a44b1c14bcdd36a16a79009b11767486ea25754e65c2",
 "ContinuantSequence.olean": "53e20668babd1f7f46be58365c2034a313dac8b2e6046b30f079157cebfdbb9a",
 "DenominatorBootstrap.olean": "f5c9957f608cdd4f861ed969ba33df4e3a61c41600afde0c0b7dd301676fa409",
 "FiniteHorizonBounds.olean": "fb472c9e76d1f3ed212df2dab24d153fb607c4bfc15378b24fd698d439eb590e",
 "FiniteHorizonSelection.olean": "accab76bdf9eebed23f84073d5f1b8b6edd604651b58d0fc3a23e9187e41dd72",
 "MechanicalCarry.olean": "861c510464432d8377bb10f5fa94cab419d75783bdf533c100ec10067301a4bc",
 "OppositeArcStrip.olean": "72951e7573614a908647267efeaf6f39e0ecb6eb01e83b58d004ca825bc639c8",
 "OppositeCarryArcs.olean": "09e8ae499734c3bfba22d0012d686105171ed20b9c07756d1372f399b1b887b3",
 "SharpAdjacentReturn.olean": "bd397fdaa5f631f3ce7bf2bb587f5087427cfee901980c9cbfeaf2531547c0cc"
}
pins = [["UniformHorizon", "H", "1331e5cf924cd3186e75a749b096e9fe3f622bb6bcef2a1256a9b71808c8b351"], ["RecodedHorizon", "H", "ab75fa0fa094e39cd4dc91215ceb4647c1d62fa95ae4fababb15084866d99cf1"], ["ArcRule30BridgeDraft", "A", "4f644cc44e1365dd7b9292a64dbd14a5984ed2758506a3cab072dcb15f63d6b1"], ["PhysicalHorizon", "H", "79fe5a747cba2673bf1f896f31824c48826c4c30554d7dc3c3b650bc4bf24e7b"]]
out = Path(os.environ['CAPPED_OUT'])
(out / 'src').mkdir(); (out / 'lib').mkdir()
for name, digest in objects.items():
    data = (blib / name).read_bytes()
    if hashlib.sha256(data).hexdigest() != digest:
        raise SystemExit('REFUSED: stage B object digest mismatch for ' + name)
    (out / 'lib' / name).write_bytes(data)
print('STAGE_B_OBJECTS_OK', len(objects), flush=True)
expected = {}
for name, where, digest in pins:
    data = (dirs[where] / (name + '.lean')).read_bytes()
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
echo 'HORIZON_INTEGRATION_C_PASS (4 modules)'
