#!/bin/sh
# finite_past_dev_435.sh (Local, L1228; first frozen at L1225, 42c0f035, which FAILED): the Lean 4.35 development
# stage for Package B (finite past), agreed in GC2295 after L1219, re-pinned to GPT's GC2299 repair. Three Lean children, in order, against the pipeline kit's prebuilt core (its Rule30Prize,
# Rule30Realization and Rule30Jen sources are byte-identical to verifier kit 19540bf's):
#   1. compile GPT's assembled single file (Rule30Submission.lean, 0072d264) into a fresh, empty library;
#   2. compile GPT's positive guard module, which must print exactly its 23 axiom reports, for exactly the names of
#      its own `#print axioms` lines and in that order, each standard (GC2299);
#   3. compile GPT's expected-rejection control, which must FAIL with a type mismatch at deliberately_false (lines 11-12),
#      after 1 and 2 have passed. An import or other failure does not count.
# The final guard exits 1 on FAIL, so the supervisor's exit code carries the verdict (GC2299).
# Development evidence only: not the official checker, not a release check, no retry. Invoke as
#   SHARP_LEAN=<lean> KIT_ROOT=<kit> sh finite_past_dev_435.sh FOLDER
# under run_capped.py --track-tree.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
: "${SHARP_LEAN:?select the installed 4.35 compiler explicitly}"
: "${KIT_ROOT:?the pipeline kit root with prebuilt builds}"
(ulimit -t 60; python3 - "$1") <<'PREP'
from pathlib import Path
import hashlib, os, re, sys
pins = {'Rule30Submission.lean': '0072d264545110cb46f036bb73769127246ebc4eca951613f60917fcc0259229',
        'FinitePastValidationGuard.lean': '3060610526333fad0829dfa82288979bac1ee9203d042a83835c2bc42a5b452e',
        'FinitePastExpectedRejection.lean': 'b87d6eee0098a9fd0108bbfee9677a9771e2d4fd46327fbd41cd8443e513c5db'}
out = Path(os.environ['CAPPED_OUT']); (out / 'src').mkdir(); (out / 'lib').mkdir()
for name, digest in pins.items():
    data = (Path(sys.argv[1]) / name).read_bytes()
    if hashlib.sha256(data).hexdigest() != digest:
        raise SystemExit('REFUSED: digest mismatch for ' + name)
    text = data.decode()
    if re.search(r'\b(?:sorry|admit|native_decide|bv_decide|skipKernelTC)\b', text):
        raise SystemExit('REFUSED: a forbidden token in ' + name)
    (out / 'src' / name).write_bytes(data)
print('FINITE_PAST_DEV_SOURCES_OK', flush=True)
PREP
export LEAN_PATH="$CAPPED_OUT/lib:$KIT_ROOT/lean/.lake/build/lib/lean"
[ -e "$KIT_ROOT/lean/.lake/build/lib/lean/Rule30Submission.olean" ] && { echo "REFUSED: another Rule30Submission object on the path"; exit 1; }
LEAN_SYSROOT=$(dirname "$(dirname "$SHARP_LEAN")"); export LEAN_SYSROOT
c() { "$SHARP_LEAN" -j1 --root="$CAPPED_OUT/src" "$@"; }
set +e
c -o "$CAPPED_OUT/lib/Rule30Submission.olean" "$CAPPED_OUT/src/Rule30Submission.lean" > "$CAPPED_OUT/1-assembly.txt" 2>&1; echo $? > "$CAPPED_OUT/1.rc"
if [ "$(cat "$CAPPED_OUT/1.rc")" = 0 ]; then
  c -o "$CAPPED_OUT/lib/FinitePastValidationGuard.olean" "$CAPPED_OUT/src/FinitePastValidationGuard.lean" > "$CAPPED_OUT/2-guard.txt" 2>&1; echo $? > "$CAPPED_OUT/2.rc"
  if [ "$(cat "$CAPPED_OUT/2.rc")" = 0 ]; then
    c "$CAPPED_OUT/src/FinitePastExpectedRejection.lean" > "$CAPPED_OUT/3-rejection.txt" 2>&1; echo $? > "$CAPPED_OUT/3.rc"
  fi
fi
set -e
(ulimit -t 60; python3 -) <<'GUARD'
from pathlib import Path
import json, os, re
out = Path(os.environ['CAPPED_OUT'])
def read(n): p = out / n; return p.read_text() if p.exists() else None
standard = {'propext', 'Classical.choice', 'Quot.sound'}
res = {'assembly_rc': read('1.rc'), 'guard_rc': read('2.rc'), 'rejection_rc': read('3.rc'), 'reasons': []}
a = read('1-assembly.txt') or ''
res['assembly_output'] = a.replace(str(out), 'CAPPED_OUT')
if (res['assembly_rc'] or '').strip() != '0': res['reasons'].append('assembly did not compile')
elif a.strip(): res['reasons'].append('assembly compile printed something')
g = read('2-guard.txt') or ''
reports = re.findall(r"'([^'\s]+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)", g)
res['guard_reports'] = [[n, sorted(x.strip() for x in ax.split(',') if x.strip())] for n, ax in reports]
rest = re.sub(r"'([^'\s]+)' (?:depends on axioms: \[[^\]]*\]|does not depend on any axioms)", '', g).strip()
if res['guard_rc'] is None: res['reasons'].append('guard not reached')
elif res['guard_rc'].strip() != '0': res['reasons'].append('guard did not compile')
else:
    expected = re.findall(r'^#print axioms (\S+)\s*$', (out / 'src' / 'FinitePastValidationGuard.lean').read_text(), re.M)
    res['guard_expected_names'] = expected
    if len(expected) != 23: res['reasons'].append('the pinned guard has %d print lines, not 23' % len(expected))
    if [n for n, _ in reports] != expected: res['reasons'].append('guard report names differ from its print lines')
    if len(reports) != 23: res['reasons'].append('guard printed %d axiom reports, not 23' % len(reports))
    if any(not set(ax) <= standard for _, ax in res['guard_reports']): res['reasons'].append('nonstandard axioms in a guard report')
    if rest: res['reasons'].append('guard printed other text')
res['guard_other_text'] = rest.replace(str(out), 'CAPPED_OUT')
r = (read('3-rejection.txt') or '').replace(str(out), 'CAPPED_OUT')
res['rejection_output'] = r
if res['rejection_rc'] is None: res['reasons'].append('rejection control not reached')
else:
    errs = re.findall(r'FinitePastExpectedRejection\.lean:(\d+):\d+: error', r)
    if res['rejection_rc'].strip() == '0': res['reasons'].append('rejection control compiled')
    elif not errs or not set(errs) <= {'11', '12'} or 'mismatch' not in r or 'unknown module' in r.lower() or 'unknown package' in r.lower():
        res['reasons'].append('rejection control failed, but not exactly by the intended mismatch at lines 11-12')
res['status'] = 'PASS' if not res['reasons'] else 'FAIL'
(out / 'dev-result.json').write_text(json.dumps(res, indent=1, ensure_ascii=False) + '\n')
print('FINITE_PAST_DEV_' + res['status'], json.dumps(res['reasons']), flush=True)
if res['status'] != 'PASS':
    raise SystemExit(1)
GUARD
