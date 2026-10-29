#!/bin/sh
# Prefix-period bridge validation (Local, L1142, for GPT's GC2118 source). Compiles the staging dependency
# RightProfilesDraft, then PrefixPeriodBridge, each in isolation; prints the axioms of the six bridge theorems from a
# separate file; and compiles one mutated bridge whose guard p % 4 = 0 is weakened to p % 2 = 0. The mutant must fail at
# the eta step, because p = 2 admits the single seed's genuine 11011. Core imports only. Invoke from the pipeline kit
# root through `lake env sh check_prefix_bridge.sh DRAFT BRIDGE`, under run_capped.py --track-tree.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
python3 - "$1" "$2" <<'PY'
from pathlib import Path
import hashlib, os, sys
out = Path(os.environ['CAPPED_OUT'])
pins = [('draft', sys.argv[1], 'd1441055e32e7b4c0a623d14c86d63f6866d1a60bc4ad47a382cf627fcb3d28e'),
        ('bridge', sys.argv[2], '6eac3d793e56b0b37d94065d173592e71cab25dd5763369b6df0d1e390c4e2bd')]
data = {}
for name, path, expected in pins:
    data[name] = Path(path).read_bytes()
    digest = hashlib.sha256(data[name]).hexdigest()
    print(name, 'sha256', digest, flush=True)
    if digest != expected:
        raise SystemExit('REFUSED: frozen ' + name + ' digest mismatch')
# Roots RightProfilesDraft and PrefixPeriodBridge are not kit roots, so no output olean shadows the kit (L1112).
for d in ('src', 'lib', 'm/src'):
    (out / d).mkdir(parents=True)
(out / 'src' / 'RightProfilesDraft.lean').write_bytes(data['draft'])
(out / 'src' / 'PrefixPeriodBridge.lean').write_bytes(data['bridge'])
heads = ['prefix_append', 'antiperiod_of_minimal_double', 'prefix_1101_closes', 'no_11011', 'diagonals_step',
         'actual_no_11011']
(out / 'src' / 'BridgeAxioms.lean').write_text(
    'import PrefixPeriodBridge\n' + ''.join('#print axioms Rule30PrefixPeriodBridge.' + h + '\n' for h in heads))
old, new = b'(hp4 : p % 4 = 0)', b'(hp4 : p % 2 = 0)'
if data['bridge'].count(old) != 3:
    raise SystemExit('REFUSED: expected exactly three guard binders')
(out / 'm' / 'src' / 'PrefixPeriodBridge.lean').write_bytes(data['bridge'].replace(old, new))
PY
lean --version
export LEAN_PATH="$CAPPED_OUT/lib:$LEAN_PATH"
src="$CAPPED_OUT/src"
lean -j1 --root="$src" -o "$CAPPED_OUT/lib/RightProfilesDraft.olean" "$src/RightProfilesDraft.lean" \
  > "$CAPPED_OUT/draft-compile.txt" 2>&1 || { cat "$CAPPED_OUT/draft-compile.txt"; echo 'FAIL: draft compile'; exit 1; }
lean -j1 --root="$src" -o "$CAPPED_OUT/lib/PrefixPeriodBridge.olean" "$src/PrefixPeriodBridge.lean" \
  > "$CAPPED_OUT/bridge-compile.txt" 2>&1 || { cat "$CAPPED_OUT/bridge-compile.txt"; echo 'FAIL: bridge compile'; exit 1; }
lean -j1 --root="$src" "$src/BridgeAxioms.lean" \
  > "$CAPPED_OUT/bridge-axioms.txt" 2>&1 || { cat "$CAPPED_OUT/bridge-axioms.txt"; echo 'FAIL: axiom file'; exit 1; }
# The mutant writes no olean, so it cannot shadow the real bridge.
if lean -j1 --root="$CAPPED_OUT/m/src" "$CAPPED_OUT/m/src/PrefixPeriodBridge.lean" > "$CAPPED_OUT/mutant-compile.txt" 2>&1; then
  cat "$CAPPED_OUT/mutant-compile.txt"; echo 'FAIL: the p % 2 = 0 mutant compiled'; exit 1
fi
python3 - <<'PY'
from pathlib import Path
import os, re
out = Path(os.environ['CAPPED_OUT'])
standard = {'propext', 'Classical.choice', 'Quot.sound'}
line_re = re.compile(r"^'([\w.]+)' (?:depends on axioms: \[(.*)\]|does not depend on any axioms)$")
def axiom_lines(name, names):
    text = (out / name).read_text()
    print(text, end='')
    lines = [l for l in text.splitlines() if l.strip()]
    if len(lines) != len(names):
        raise SystemExit('FAIL: expected exactly %d axiom lines in %s' % (len(names), name))
    seen = []
    for l in lines:
        m = line_re.match(l)
        if not m or m.group(1) not in names:
            raise SystemExit('FAIL: unexpected output line in ' + name + ': ' + l)
        seen.append(m.group(1))
        got = {a.strip() for a in (m.group(2) or '').split(',') if a.strip()}
        if not got <= standard:
            raise SystemExit('FAIL: nonstandard axioms in ' + name + ': ' + l)
    if sorted(seen) != sorted(names):
        raise SystemExit('FAIL: missing or repeated axiom names in ' + name)
axiom_lines('draft-compile.txt', ['Rule30RightProfiles.' + h for h in
    ['shift_law', 'rightDiag_shift_law', 'E_mod4', 'eta_false_of_antiperiod', 'eta_four',
     'eta_false_of_period_half', 'running_shift']])
bridge = (out / 'bridge-compile.txt').read_text()
if bridge.strip():
    print(bridge)
    raise SystemExit('FAIL: compiler output for the bridge')
axiom_lines('bridge-axioms.txt', ['Rule30PrefixPeriodBridge.' + h for h in
    ['prefix_append', 'antiperiod_of_minimal_double', 'prefix_1101_closes', 'no_11011',
     'diagonals_step', 'actual_no_11011']])
mutant = (out / 'mutant-compile.txt').read_text()
print(mutant, end='')
error_lines = [line for line in mutant.splitlines() if re.search(r'\berror(?:\[[^\]]+\])?:', line)]
errs = []
for line in error_lines:
    match = re.search(r'PrefixPeriodBridge\.lean:(\d+):\d+: error(?:\[[^\]]+\])?:', line)
    if not match:
        raise SystemExit('FAIL: unrecognized mutant error: ' + line)
    errs.append(int(match.group(1)))
if not errs or any(not 89 <= n <= 91 for n in errs):
    raise SystemExit('FAIL: the mutant must fail only at the eta step (lines 89 to 91); errors at %s' % errs)
print('MUTANT_REJECTED_AT', sorted(set(errs)), flush=True)
PY
echo PREFIX_BRIDGE_CHECK_PASS
