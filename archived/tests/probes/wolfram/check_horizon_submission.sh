#!/bin/sh
# check_horizon_submission.sh (Local, L1179, PROPOSED; GC2171's requirements): the one official-checker stage for the
# single-file finite-horizon submission. Two Lean workload children, in order: compile the frozen Rule30Submission.lean
# into a fresh, empty library under the root Rule30Submission; then run the kit's unchanged Check.lean on that module
# with --claim partial and exactly the eight agreed headlines. Lean 4.35, the pipeline kit's prebuilt builds, no lake.
#
# CPU envelope. run_capped.py's --cpu sets each process's limit; each Lean workload child inherits it (600 s), so the
# Lean workload is bounded by 1200 s. The version query runs under 5 s, and each of the two Python guards under its own
# 60 s, so the whole workload is bounded by 1325 s plus this shell. The supervisor is outside that budget.
#
# L1182 repair: Check.lean calls `initSearchPath (← findSysroot)`, and findSysroot reads LEAN_SYSROOT or else runs
# `lean --print-prefix` from PATH. The first stage (cd761042) set neither, so its checker child failed. The runner now
# sets LEAN_SYSROOT from the pinned compiler, as `lake env` does, so no third Lean process starts.
#
# A refusal or failure ends the stage, with its packet retained; there is no retry. Invoke as
#   SHARP_LEAN=<lean> KIT_ROOT=<kit> sh check_horizon_submission.sh SOURCE ASSEMBLY_JSON
# under run_capped.py --track-tree.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
: "${SHARP_LEAN:?select the installed 4.35 compiler explicitly}"
: "${KIT_ROOT:?the pipeline kit root with prebuilt builds}"
(ulimit -t 60; python3 - "$1" "$2" "$KIT_ROOT/Check.lean") <<'PREP'
from pathlib import Path
import hashlib, json, os, re, sys
SOURCE = '791e45ed1aef3955035989f1443f43a3427ea82b0cb01a8ad088bc221ec57110'
ASSEMBLY = '266d6cd69586c37dd988c504b50cf9c558fd06c4c777ce2b184d6eb0bdd8b3e8'
CHECKER = 'b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905'
HEADLINES = ['Rule30Submission.' + x for x in [
    'UniformHorizon.uniform_horizon', 'UniformHorizon.uniform_horizon_witness', 'RecodedHorizon.uniform_horizon_all',
    'RecodedHorizon.recoded_horizon', 'PhysicalHorizon.piece_bound', 'PhysicalHorizon.reset_step',
    'PhysicalHorizon.first_disagreement', 'PhysicalHorizon.disagreement_step']]
def pinned(p, digest, what):
    data = Path(p).read_bytes()
    if hashlib.sha256(data).hexdigest() != digest:
        raise SystemExit('REFUSED: ' + what + ' digest mismatch')
    return data
src = pinned(sys.argv[1], SOURCE, 'submission source')
assembly = json.loads(pinned(sys.argv[2], ASSEMBLY, 'assembly manifest'))
checker = pinned(sys.argv[3], CHECKER, 'Check.lean')
text = src.decode()
heads = re.findall(r'^#print axioms (\S+)\s*$', text, re.M)
if len(heads) != 99 or len(set(heads)) != 99 or heads != assembly['printed_heads']:
    raise SystemExit('REFUSED: the printed heads are not the manifest\'s 99')
if assembly['proposed_headlines'] != HEADLINES or not set(HEADLINES) <= set(heads):
    raise SystemExit('REFUSED: the headlines are not the eight agreed ones')
if 'import Ruliology.CellularAutomata.Rule30Prize' not in text.splitlines():
    raise SystemExit('REFUSED: the official statement module is not imported')
if re.search(r'\b(?:sorry|admit|native_decide|bv_decide|skipKernelTC)\b', text):
    raise SystemExit('REFUSED: a forbidden token')
# The actual eight types, as source text: the partial checker accepts any statement, so retain what each one says.
signatures = {}
for full in HEADLINES:
    space, short = full.split('.')[1:]
    body = text[text.index('\nnamespace ' + space + '\n'):text.index('\nend ' + space + '\n')]
    found = re.findall(r'^theorem ' + re.escape(short) + r'(\s.*?) :=', body, re.M | re.S)
    if len(found) != 1:
        raise SystemExit('REFUSED: no unique source signature for ' + full)
    signatures[full] = 'theorem ' + short + re.sub(r'\s+', ' ', found[0]).rstrip()
out = Path(os.environ['CAPPED_OUT'])
(out / 'src').mkdir(); (out / 'lib').mkdir()
(out / 'src' / 'Rule30Submission.lean').write_bytes(src)
(out / 'Check.lean').write_bytes(checker)
(out / 'expected.json').write_text(json.dumps({'heads': heads, 'headlines': HEADLINES, 'signatures': signatures},
                                               indent=1, ensure_ascii=False) + '\n')
print('HORIZON_SUBMISSION_SOURCE_OK', len(heads), 'printed heads,', len(HEADLINES), 'headlines', flush=True)
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
  --headline Rule30Submission.UniformHorizon.uniform_horizon \
  --headline Rule30Submission.UniformHorizon.uniform_horizon_witness \
  --headline Rule30Submission.RecodedHorizon.uniform_horizon_all \
  --headline Rule30Submission.RecodedHorizon.recoded_horizon \
  --headline Rule30Submission.PhysicalHorizon.piece_bound \
  --headline Rule30Submission.PhysicalHorizon.reset_step \
  --headline Rule30Submission.PhysicalHorizon.first_disagreement \
  --headline Rule30Submission.PhysicalHorizon.disagreement_step \
  > "$CAPPED_OUT/check.json" 2> "$CAPPED_OUT/check.err"
echo $? > "$CAPPED_OUT/checker.rc"
set -e
(ulimit -t 60; python3 -) <<'GUARD'
from pathlib import Path
import json, os, re
out = Path(os.environ['CAPPED_OUT'])
expected = json.loads((out / 'expected.json').read_text())
heads, headlines = expected['heads'], expected['headlines']
standard = {'propext', 'Classical.choice', 'Quot.sound'}
# The compiler's output must be exactly the 99 axiom reports, in source order, each possibly wrapped over lines.
text = (out / 'compile.txt').read_text()
print(text, end='')
report = re.compile(r"'([^'\s]+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)(?:\n|\Z)")
pos, seen = 0, []
while pos < len(text):
    m = report.match(text, pos)
    if not m:
        raise SystemExit('FAIL: unexpected compiler text at offset %d: %r' % (pos, text[pos:pos + 200]))
    if not {a.strip() for a in (m.group(2) or '').split(',') if a.strip()} <= standard:
        raise SystemExit('FAIL: nonstandard axioms in the report for ' + m.group(1))
    seen.append(m.group(1)); pos = m.end()
if seen != heads:
    raise SystemExit('FAIL: %d axiom reports; the 99 printed heads, in order and without repeats, were expected'
                     % len(seen))
print('COMPILER_REPORTS_OK', len(seen), flush=True)
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
    raise SystemExit('FAIL: exactly the eight headlines, each found, ok and with standard axioms')
declared = c.get('declared', [])
names = [x.get('name') for x in declared]
if len(set(names)) != len(names) or any(x.get('standardAxioms') is not True for x in declared):
    raise SystemExit('FAIL: a declared constant is repeated or not standard')
if not set(heads) <= set(names) or not len(names) <= replay.get('constants', 0):
    raise SystemExit('FAIL: a printed head is not declared, or fewer constants replayed than declared')
result = {'status': 'PASS', 'printed_heads': len(heads), 'declared': len(names), 'replayed_constants':
          replay['constants'], 'checker_notice': rest, 'headline_signatures': expected['signatures'],
          'signature_note': 'source text of the eight headlines; the partial checker accepts any statement',
          'checker': c, 'scope': 'explicit finite horizon for mechanical words and finite-width recodings; '
          'conditional bounds beside a genuine Rule 30 clock; no density, realizability or prize claim'}
(out / 'submission-check.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
print('HORIZON_SINGLE_FILE_PASS', len(names), 'declared,', replay['constants'], 'replayed', flush=True)
GUARD
