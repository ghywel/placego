#!/bin/sh
# Lemma R full check (Local, L1131): the catalog module and the submission form of Rule30RingOrbits, each compiled in
# isolation and checked by the unchanged Check.lean with its eight headlines. Core imports only. Invoke from the pipeline
# kit root through `lake env sh check_ring_orbits.sh CATALOG SUBMISSION`, under run_capped.py --track-tree.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
python3 - "$1" "$2" <<'PY'
from pathlib import Path
import hashlib, os, sys
out = Path(os.environ['CAPPED_OUT'])
pins = [('catalog', sys.argv[1], '61fbff78da7c93e345d789a35396de373b42c25040eb66e227a5460af4a34e24'), ('submission', sys.argv[2], '23a3be9f7d008bcdeb0d9e4ffbc037d593457ad97e0064da35f323578d473a96'),
        ('checker', 'Check.lean', 'b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905')]
data = {}
for name, path, expected in pins:
    data[name] = Path(path).read_bytes()
    digest = hashlib.sha256(data[name]).hexdigest()
    print(name, 'sha256', digest, flush=True)
    if digest != expected:
        raise SystemExit('REFUSED: frozen ' + name + ' digest mismatch')
# The catalog module compiles under the root RingOrbitsCert, so no output Ruliology/ shadows the kit's package (L1112).
(out / 'c' / 'src' / 'RingOrbitsCert').mkdir(parents=True)
(out / 'c' / 'lib' / 'RingOrbitsCert').mkdir(parents=True)
(out / 'c' / 'src' / 'RingOrbitsCert' / 'Rule30RingOrbits.lean').write_bytes(data['catalog'])
(out / 's' / 'src').mkdir(parents=True)
(out / 's' / 'lib').mkdir(parents=True)
(out / 's' / 'src' / 'Rule30Submission.lean').write_bytes(data['submission'])
(out / 'Check.lean').write_bytes(data['checker'])
PY
heads="orbit_eq_iff encode_walk decode_ring decode_encode encode_decode ring_fixed ring_period_two alternating_even"
base_path="$LEAN_PATH"
for part in c s; do
  if [ "$part" = c ]; then
    mod=RingOrbitsCert.Rule30RingOrbits; file=RingOrbitsCert/Rule30RingOrbits; prefix=Ruliology.CellularAutomata.Rule30RingOrbits
  else
    mod=Rule30Submission; file=Rule30Submission; prefix=Rule30Submission
  fi
  export LEAN_PATH="$CAPPED_OUT/$part/lib:$base_path"
  lean -j1 --root="$CAPPED_OUT/$part/src" -o "$CAPPED_OUT/$part/lib/$file.olean" "$CAPPED_OUT/$part/src/$file.lean" \
    > "$CAPPED_OUT/$part-compile.txt" 2>&1
  args=""
  for h in $heads; do args="$args --headline $prefix.$h"; done
  lean -j1 --root="$CAPPED_OUT" --run "$CAPPED_OUT/Check.lean" $mod --claim partial $args > "$CAPPED_OUT/$part-check.json"
  python3 - "$part" "$mod" "$prefix" "$heads" <<'PY'
from pathlib import Path
import json, os, sys
part, mod, prefix, heads = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4].split()
out = Path(os.environ['CAPPED_OUT'])
compile_text = (out / (part + '-compile.txt')).read_text()
if compile_text.strip():
    print(compile_text)
    raise SystemExit('FAIL: compiler output for ' + part)
raw = (out / (part + '-check.json')).read_text()
print(raw, end='')
lines = [line for line in raw.splitlines() if line.startswith('{')]
if len(lines) != 1:
    raise SystemExit('FAIL: expected exactly one checker JSON line for ' + part)
r = json.loads(lines[0])
expected = {prefix + '.' + h for h in heads}
got = r.get('headlines', [])
if r.get('module') != mod or r.get('verdict') != 'pass' or r.get('replay', {}).get('ok') is not True:
    raise SystemExit('FAIL: module/verdict/replay for ' + part)
if r.get('importsStatements') is not True or r.get('newAxioms'):
    raise SystemExit('FAIL: official import/new axiom guard for ' + part)
if {h.get('name') for h in got} != expected or len(got) != len(expected) or any(h.get('ok') is not True for h in got):
    raise SystemExit('FAIL: exact headline outcomes for ' + part)
if any(d.get('standardAxioms') is not True for d in r.get('declared', [])):
    raise SystemExit('FAIL: nonstandard declared constant for ' + part)
print('PART_PASS', part, flush=True)
PY
done
echo RING_ORBITS_CHECK_PASS
