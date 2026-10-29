#!/bin/sh
# Invoke from the existing kit root through `lake env`; no library targets or dependency rebuilds.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
universal_start_source=$1
python3 - "$universal_start_source" <<'PY'
from pathlib import Path
import hashlib, os, sys
out = Path(os.environ['CAPPED_OUT'])
source = Path(sys.argv[1]).read_bytes()
checker = Path('Check.lean').read_bytes()
expected_source = '32cd904f9247b5f651e18494e1fd5bc7e4a212c76977989e28808f2f11fbc724'
expected_checker = 'b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905'
for name, data, expected in [('module', source, expected_source), ('checker', checker, expected_checker)]:
    digest = hashlib.sha256(data).hexdigest()
    print(name, 'sha256', digest, flush=True)
    if digest != expected:
        raise SystemExit('REFUSED: frozen ' + name + ' digest mismatch')
# L1112: compiled under the root UniversalStartCert, so the output lib holds no `Ruliology/` to shadow the kit's
# built package (Lean commits to the first LEAN_PATH entry holding a module's root directory). The module's name
# comes from its path; its declaration names come from its unchanged `namespace`.
module_dir = out / 'src' / 'UniversalStartCert'
module_dir.mkdir(parents=True)
(out / 'lib' / 'UniversalStartCert').mkdir(parents=True)
(module_dir / 'Rule30UniversalStart.lean').write_bytes(source)
(out / 'Check.lean').write_bytes(checker)
PY
export LEAN_PATH="$CAPPED_OUT/lib${LEAN_PATH:+:$LEAN_PATH}"
lean -j1 --root="$CAPPED_OUT/src" \
  -o "$CAPPED_OUT/lib/UniversalStartCert/Rule30UniversalStart.olean" \
  "$CAPPED_OUT/src/UniversalStartCert/Rule30UniversalStart.lean"
lean -j1 --root="$CAPPED_OUT" --run "$CAPPED_OUT/Check.lean" \
  UniversalStartCert.Rule30UniversalStart --claim partial \
  --headline Ruliology.CellularAutomata.Rule30UniversalStart.universal_start \
  --headline Ruliology.CellularAutomata.Rule30UniversalStart.universal_start_finite \
  --headline Ruliology.CellularAutomata.Rule30UniversalStart.universal_start_profiles \
  --headline Ruliology.CellularAutomata.Rule30UniversalStart.cert \
  > "$CAPPED_OUT/check.json"
python3 - <<'PY'
from pathlib import Path
import json, os
p = Path(os.environ['CAPPED_OUT']) / 'check.json'
raw = p.read_text()
print(raw, end='')
# L1112: `lean --run Check.lean` prints its own deprecation warning before the JSON line; parse its single JSON line.
json_lines = [line for line in raw.splitlines() if line.startswith('{')]
if len(json_lines) != 1:
    raise SystemExit('FAIL: expected exactly one checker JSON line')
result = json.loads(json_lines[0])
if result.get('module') != 'UniversalStartCert.Rule30UniversalStart':
    raise SystemExit('FAIL: checker module name')
prefix = 'Ruliology.CellularAutomata.Rule30UniversalStart.'
expected = {prefix + x for x in ['universal_start', 'universal_start_finite', 'universal_start_profiles', 'cert']}
actual = result.get('headlines', [])
if result.get('verdict') != 'pass' or result.get('replay', {}).get('ok') is not True:
    raise SystemExit('FAIL: checker replay/verdict')
if result.get('importsStatements') is not True or result.get('newAxioms'):
    raise SystemExit('FAIL: official import/new axiom guard')
if {h.get('name') for h in actual} != expected or len(actual) != 4 or any(h.get('ok') is not True for h in actual):
    raise SystemExit('FAIL: exact four headline outcomes')
print('UNIVERSAL_START_CHECK_PASS')
PY
