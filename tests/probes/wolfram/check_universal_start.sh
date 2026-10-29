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
expected_source = 'b62c3d583be2555189a259325faa64314633531ffe8b080d0f50a2c405f74ad2'
expected_checker = 'b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905'
for name, data, expected in [('module', source, expected_source), ('checker', checker, expected_checker)]:
    digest = hashlib.sha256(data).hexdigest()
    print(name, 'sha256', digest, flush=True)
    if digest != expected:
        raise SystemExit('REFUSED: frozen ' + name + ' digest mismatch')
module_dir = out / 'src' / 'Ruliology' / 'CellularAutomata'
module_dir.mkdir(parents=True)
(out / 'lib' / 'Ruliology' / 'CellularAutomata').mkdir(parents=True)
(module_dir / 'Rule30UniversalStart.lean').write_bytes(source)
(out / 'Check.lean').write_bytes(checker)
PY
export LEAN_PATH="$CAPPED_OUT/lib${LEAN_PATH:+:$LEAN_PATH}"
lean -j1 --root="$CAPPED_OUT/src" \
  -o "$CAPPED_OUT/lib/Ruliology/CellularAutomata/Rule30UniversalStart.olean" \
  "$CAPPED_OUT/src/Ruliology/CellularAutomata/Rule30UniversalStart.lean"
lean -j1 --root="$CAPPED_OUT" --run "$CAPPED_OUT/Check.lean" \
  Ruliology.CellularAutomata.Rule30UniversalStart --claim partial \
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
result = json.loads(raw)
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
