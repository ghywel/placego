#!/bin/sh
# Stage A2b (Local, L1115): the universal-start submission form, compiled under `import Rule30PrizeKit` and checked by
# the unchanged Check.lean. Invoke from the pipeline kit root through `lake env`; no library targets or dependency
# rebuilds. All new artifacts stay under CAPPED_OUT.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
submission_source=$1
python3 - "$submission_source" <<'PY'
from pathlib import Path
import hashlib, os, sys
out = Path(os.environ['CAPPED_OUT'])
source = Path(sys.argv[1]).read_bytes()
checker = Path('Check.lean').read_bytes()
expected_source = '17fdfbcb8833b77ee5a511d9f50f52997cf6c25429dbacb63b1b17c1e63fde30'
expected_checker = 'b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905'
for name, data, expected in [('submission', source, expected_source), ('checker', checker, expected_checker)]:
    digest = hashlib.sha256(data).hexdigest()
    print(name, 'sha256', digest, flush=True)
    if digest != expected:
        raise SystemExit('REFUSED: frozen ' + name + ' digest mismatch')
# The module's root is the single file Rule30Submission; the output lib comes first on LEAN_PATH, so this
# Rule30Submission.olean is found before any other copy on the kit's path.
(out / 'src').mkdir()
(out / 'lib').mkdir()
(out / 'src' / 'Rule30Submission.lean').write_bytes(source)
(out / 'Check.lean').write_bytes(checker)
PY
export LEAN_PATH="$CAPPED_OUT/lib${LEAN_PATH:+:$LEAN_PATH}"
lean -j1 --root="$CAPPED_OUT/src" -o "$CAPPED_OUT/lib/Rule30Submission.olean" "$CAPPED_OUT/src/Rule30Submission.lean"
lean -j1 --root="$CAPPED_OUT" --run "$CAPPED_OUT/Check.lean" Rule30Submission --claim partial \
  --headline Rule30Submission.universal_start \
  --headline Rule30Submission.universal_start_finite \
  --headline Rule30Submission.universal_start_profiles \
  --headline Rule30Submission.cert \
  > "$CAPPED_OUT/check.json"
python3 - <<'PY'
from pathlib import Path
import json, os
p = Path(os.environ['CAPPED_OUT']) / 'check.json'
raw = p.read_text()
print(raw, end='')
# `lean --run Check.lean` prints its own deprecation warning before the JSON line; parse its single JSON line.
json_lines = [line for line in raw.splitlines() if line.startswith('{')]
if len(json_lines) != 1:
    raise SystemExit('FAIL: expected exactly one checker JSON line')
result = json.loads(json_lines[0])
if result.get('module') != 'Rule30Submission':
    raise SystemExit('FAIL: checker module name')
expected = {'Rule30Submission.' + x for x in ['universal_start', 'universal_start_finite', 'universal_start_profiles', 'cert']}
actual = result.get('headlines', [])
if result.get('verdict') != 'pass' or result.get('replay', {}).get('ok') is not True:
    raise SystemExit('FAIL: checker replay/verdict')
if result.get('importsStatements') is not True or result.get('newAxioms'):
    raise SystemExit('FAIL: official import/new axiom guard')
if {h.get('name') for h in actual} != expected or len(actual) != 4 or any(h.get('ok') is not True for h in actual):
    raise SystemExit('FAIL: exact four headline outcomes')
print('UNIVERSAL_START_SUBMISSION_CHECK_PASS')
PY
