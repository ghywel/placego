#!/bin/sh
# Finite-horizon integration, stage A (Local, L1167, PROPOSED for GPT's agreement; GPT's GC2150 module plan): compile
# the seven old arc modules, then six current finite-horizon modules, in dependency order, each into a fresh output
# library, on Lean 4.35 against the pipeline kit's prebuilt Mathlib, its equivalents build (Rule30Equivalents.Lagrange)
# and its lean build (Ruliology), with no lake. The first failure stops the stage and its object is deleted, so nothing
# stale or sorry-containing is imported. Each module's output must be exactly the axiom reports named by its own
# `#print axioms` lines, with standard axioms only. FiniteHorizonSelection and ContinuantSequence (two known omega
# fixes pending, L1166) and the separation module (not yet written) are outside stage A. Invoke as
#   SHARP_LEAN=<toolchain lean> KIT_ROOT=<pipeline kit root> sh check_horizon_integration.sh ARC_DIR HORIZON_DIR
# under run_capped.py --track-tree.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
: "${SHARP_LEAN:?select the installed 4.35 compiler explicitly}"
: "${KIT_ROOT:?the pipeline kit root with prebuilt builds}"
MODULES="ArcBreakBounds ArcBreakSequence ArcDeterminantDraft ArcContinuantsDraft ArcCoverDraft ArcStepCodeDraft
ArcRotationDraft SharpAdjacentReturn MechanicalCarry FiniteHorizonBounds CarryReturnSpacing ActualContinuants
ActualCarrySpacing"
python3 - "$1" "$2" <<'PY'
from pathlib import Path
import hashlib, json, os, sys
arc, horizon = Path(sys.argv[1]), Path(sys.argv[2])
pins = [('ArcBreakBounds', arc, 'cbb2f4ba2a384a9b9cb077f4b5c9242339237864bc47af70f0afddaf5b78f1a6'),
        ('ArcBreakSequence', arc, '7d6f45508ce456e11cefa1e305580f8d1195f26e5cd1375e9cd9e96dd53ffdfe'),
        ('ArcDeterminantDraft', arc, 'aa2402bddf84deac9c38f3383fb55b57e6f088a1453b02dd465b128d99fa083a'),
        ('ArcContinuantsDraft', arc, '7c32512f60fb003c598d86d31474109e700edac3991528b1e3522cba4ea79fab'),
        ('ArcCoverDraft', arc, '58268dd3a9e52652fe904d390c51b2354b6eae90bde99fd06e12c4e60958d5f4'),
        ('ArcStepCodeDraft', arc, 'b207135e62cb7e8dde7f4e79ecb1f20f6825001efdae997536ce60dc0f6dafe5'),
        ('ArcRotationDraft', arc, '4acd4c0eda5777a2365424601b627a1f2ef86fe9b8c51a185fa658364d78aef9'),
        ('SharpAdjacentReturn', horizon, '17679e3755d6d8b9fedf8f0f14d6e6dbade1f3367b6e0a10d257a00e998bdfb1'),
        ('MechanicalCarry', horizon, 'b0b83cd83df4fbf1aeb04bf680708a47ed8d8ea9e6c44f0b77d9c366e6481253'),
        ('FiniteHorizonBounds', horizon, 'ceafe8f929b8a5d62ab2e8a0ea3b7ac7eb9cd3c589018e7f24191d12a8ffd7c9'),
        ('CarryReturnSpacing', horizon, '3445f7f25ce765ffdbf29040e45f964b98978bab17d3b1c47595ff2f17445c40'),
        ('ActualContinuants', horizon, '4367bc2b3b1fa68c7cbf516f0a000a1033f92eb3389d7bdf195e271d5bb87836'),
        ('ActualCarrySpacing', horizon, 'a514f7a025c7ea1f284882958db353832b4a0576fd6c7ad61ada327c50f2f878')]
out = Path(os.environ['CAPPED_OUT'])
(out / 'src').mkdir(); (out / 'lib').mkdir()
expected = {}
for name, root, digest in pins:
    data = (root / (name + '.lean')).read_bytes()
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
echo 'HORIZON_INTEGRATION_A_PASS (13 modules)'
