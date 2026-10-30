#!/bin/sh
# check_gate_clocks_submission.sh (Local, L1217): the one official-checker stage for the single-file gate-clock
# submission (Package A). Adapted from check_horizon_submission.sh (L1179/L1182). Two Lean workload children, in
# order: compile the frozen Rule30Submission.lean into a fresh, empty library under the root Rule30Submission; then run
# the kit's unchanged Check.lean on that module with --claim partial and exactly the five headlines. Lean 4.35, the
# pipeline kit's prebuilt core (its Rule30Prize and Rule30Jen sources are byte-identical to the verifier kit 19540bf's),
# no lake. The source prints no axioms: the compiler's output must be empty.
#
# CPU envelope as in the horizon runner: each Lean child inherits run_capped.py's per-process --cpu.
# A refusal or failure ends the stage, with its packet retained; there is no retry. Invoke as
#   SHARP_LEAN=<lean> KIT_ROOT=<kit> sh check_gate_clocks_submission.sh SOURCE
# under run_capped.py --track-tree.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
: "${SHARP_LEAN:?select the installed 4.35 compiler explicitly}"
: "${KIT_ROOT:?the pipeline kit root with prebuilt builds}"
(ulimit -t 60; python3 - "$1" "$KIT_ROOT/Check.lean") <<'PREP'
from pathlib import Path
import hashlib, json, os, re, sys
SOURCE = '14372c1de82d95341d0d79d4101552683f8b24e9be332712da44600d8b262eb6'
CHECKER = 'b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905'
HEADLINES = ['Rule30Submission.' + x for x in ['prefix_period_iff', 'prefix_window_bound', 'prefix_window_le_B', 'prefixExp_le_B', 'affine_prefix_bound']]
def pinned(p, digest, what):
    data = Path(p).read_bytes()
    if hashlib.sha256(data).hexdigest() != digest:
        raise SystemExit('REFUSED: ' + what + ' digest mismatch')
    return data
src = pinned(sys.argv[1], SOURCE, 'submission source')
checker = pinned(sys.argv[2], CHECKER, 'Check.lean')
text = src.decode()
if re.findall(r'^#print', text, re.M):
    raise SystemExit('REFUSED: the source prints')
if [l for l in text.splitlines() if l.startswith('import ')] != ['import Ruliology.CellularAutomata.Rule30Prize']:
    raise SystemExit('REFUSED: the imports are not exactly the official statement module')
if re.search(r'\b(?:sorry|admit|native_decide|bv_decide|skipKernelTC)\b', text):
    raise SystemExit('REFUSED: a forbidden token')
signatures = {}
for full in HEADLINES:
    short = full.split('.')[1]
    # The statement ends at its first ` :=` or at its first equation clause (`| ...`), whichever comes first
    # (GC2294: prefix_period_iff is defined by equations, and a ` :=` search ran on into its proof).
    found = re.findall(r'^theorem ' + re.escape(short) + r'(\s.*?)(?: :=|\n\s*\|(?!\|))', text, re.M | re.S)
    if len(found) != 1:
        raise SystemExit('REFUSED: no unique source signature for ' + full)
    signatures[full] = 'theorem ' + short + re.sub(r'\s+', ' ', found[0]).rstrip()
out = Path(os.environ['CAPPED_OUT'])
(out / 'src').mkdir(); (out / 'lib').mkdir()
(out / 'src' / 'Rule30Submission.lean').write_bytes(src)
(out / 'Check.lean').write_bytes(checker)
(out / 'expected.json').write_text(json.dumps({'headlines': HEADLINES, 'signatures': signatures},
                                               indent=1, ensure_ascii=False) + '\n')
print('GATE_SUBMISSION_SOURCE_OK', len(HEADLINES), 'headlines', flush=True)
PREP
lp="$CAPPED_OUT/lib:$KIT_ROOT/equivalents/.lake/build/lib/lean:$KIT_ROOT/lean/.lake/build/lib/lean"
for d in "$KIT_ROOT"/.lake/packages/*/.lake/build/lib/lean; do
  [ -d "$d" ] || { echo "REFUSED: missing package build $d"; exit 1; }
  lp="$lp:$d"
done
# The checker must replay this stage's object: no other directory on the path may hold a Rule30Submission object.
old_ifs=$IFS; IFS=:
for d in $lp; do
  [ "$d" = "$CAPPED_OUT/lib" ] && continue
  [ -e "$d/Rule30Submission.olean" ] && { echo "REFUSED: another Rule30Submission object on the path"; exit 1; }
done
IFS=$old_ifs
[ -z "$(ls -A "$CAPPED_OUT/lib")" ] || { echo "REFUSED: the output library is not empty"; exit 1; }
export LEAN_PATH="$lp"
case "$SHARP_LEAN" in */bin/lean) ;; *) echo "REFUSED: SHARP_LEAN is not a toolchain's bin/lean"; exit 1 ;; esac
LEAN_SYSROOT=$(dirname "$(dirname "$SHARP_LEAN")")
[ -f "$LEAN_SYSROOT/lib/lean/Init.olean" ] || { echo "REFUSED: no Lean library under the compiler's root"; exit 1; }
export LEAN_SYSROOT
echo LEAN_SYSROOT_SET
(ulimit -t 5; "$SHARP_LEAN" --version)
if ! "$SHARP_LEAN" -j1 --root="$CAPPED_OUT/src" -o "$CAPPED_OUT/lib/Rule30Submission.olean" \
    "$CAPPED_OUT/src/Rule30Submission.lean" > "$CAPPED_OUT/compile.txt" 2>&1; then
  cat "$CAPPED_OUT/compile.txt"; echo "FAIL: compile"; exit 1
fi
echo COMPILE_DONE
set +e
"$SHARP_LEAN" -j1 --root="$CAPPED_OUT" --run "$CAPPED_OUT/Check.lean" Rule30Submission --claim partial \
  --headline Rule30Submission.prefix_period_iff \
  --headline Rule30Submission.prefix_window_bound \
  --headline Rule30Submission.prefix_window_le_B \
  --headline Rule30Submission.prefixExp_le_B \
  --headline Rule30Submission.affine_prefix_bound \
  > "$CAPPED_OUT/check.json" 2> "$CAPPED_OUT/check.err"
echo $? > "$CAPPED_OUT/checker.rc"
set -e
(ulimit -t 60; python3 -) <<'GUARD'
from pathlib import Path
import json, os, re
out = Path(os.environ['CAPPED_OUT'])
expected = json.loads((out / 'expected.json').read_text())
headlines = expected['headlines']
standard = {'propext', 'Classical.choice', 'Quot.sound'}
# The source prints nothing, so the compiler's output must be empty.
text = (out / 'compile.txt').read_text()
print(text, end='')
if text.strip():
    raise SystemExit('FAIL: the compiler printed something')
print('COMPILER_SILENT', flush=True)
# The checker's output: one JSON object, and at most its own known deprecation notice about Check.lean line 124.
NOTICE = ('CAPPED_OUT/Check.lean:124:17: warning: `Lean.Environment.replay` has been deprecated: Use '
          '`Lean.Kernel.Environment.replay` instead\n\nNote: The updated constant has a different type:\n'
          '  Std.HashMap Name ConstantInfo → Kernel.Environment → IO Kernel.Environment\ninstead of\n'
          '  Std.HashMap Name ConstantInfo → Environment → IO Environment\n\nNote: The updated constant is in a '
          'different namespace. Dot notation may need to be changed (e.g., from `x.replay` to '
          '`Kernel.Environment.replay x`).')
raw, err = (out / 'check.json').read_text(), (out / 'check.err').read_text()
rc = int((out / 'checker.rc').read_text())
print(raw, end=''); print(err, end='')
lines = raw.splitlines()
objects = [l for l in lines if l.startswith('{')]
rest = '\n'.join(l.rstrip() for l in [l for l in lines if not l.startswith('{')] + err.splitlines())
rest = rest.replace(str(out), 'CAPPED_OUT').strip()
if len(objects) != 1:
    raise SystemExit('FAIL: %d checker JSON objects' % len(objects))
if rest not in ('', NOTICE):
    raise SystemExit('FAIL: unexpected checker text')
c = json.loads(objects[0])
replay = c.get('replay', {})
if rc != 0 or c.get('module') != 'Rule30Submission' or c.get('claim') != 'partial' or c.get('verdict') != 'pass' \
        or c.get('reasons') != [] or replay.get('ok') is not True:
    raise SystemExit('FAIL: checker exit, module, claim, verdict or kernel replay')
if c.get('importsStatements') is not True or c.get('newAxioms') != []:
    raise SystemExit('FAIL: official statement import or new axioms')
if c.get('official') != [] or c.get('verifiedTargets') != []:
    raise SystemExit('FAIL: an official prize target is declared')
h = c.get('headlines', [])
if [x.get('name') for x in h] != headlines or any(
        x.get('found') is not True or x.get('ok') is not True or x.get('typeMatches') is not True
        or x.get('problems') != [] or not set(x.get('axioms', ['?'])) <= standard for x in h):
    raise SystemExit('FAIL: exactly the five headlines, each found, ok and with standard axioms')
declared = c.get('declared', [])
names = [x.get('name') for x in declared]
if len(set(names)) != len(names) or any(x.get('standardAxioms') is not True for x in declared):
    raise SystemExit('FAIL: a declared constant is repeated or not standard')
if not set(headlines) <= set(names) or not len(names) <= replay.get('constants', 0):
    raise SystemExit('FAIL: a headline is not declared, or fewer constants replayed than declared')
result = {'status': 'PASS', 'declared': len(names), 'replayed_constants':
          replay['constants'], 'checker_notice': rest, 'headline_signatures': expected['signatures'],
          'signature_note': 'source text of the five headlines; the partial checker accepts any statement',
          'checker': c, 'scope': 'half-rate prefix-period bound for every two-input gate family, exact prefix periods, '
          'logarithmic affine bound; no lower bound, density, centre-column or prize claim'}
(out / 'submission-check.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
print('GATE_SINGLE_FILE_PASS', len(names), 'declared,', replay['constants'], 'replayed', flush=True)
GUARD
