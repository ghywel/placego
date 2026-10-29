#!/bin/sh
# GC2105: single-file whole-proof kernel replay. Existing4.35 materialized environment only.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
arc_submission_source=$1
python3 - "$arc_submission_source" <<'PREP'
from pathlib import Path
import hashlib,os,sys
src=Path(sys.argv[1]).read_bytes()
if hashlib.sha256(src).hexdigest()!='56d226a644ffc0c061239fc6daccdd88ba4a69efc9507939994b685411fe9594':
 raise SystemExit('REFUSED: frozen submission source')
checker=Path('Check.lean').read_bytes()
if hashlib.sha256(checker).hexdigest()!='b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905':
 raise SystemExit('REFUSED: unchanged checker')
out=Path(os.environ['CAPPED_OUT']);(out/'src').mkdir();(out/'lib').mkdir()
(out/'src/Rule30Submission.lean').write_bytes(src);(out/'Check.lean').write_bytes(checker)
print('ARC_SUBMISSION_SOURCE_OK',flush=True)
PREP
export LEAN_PATH="$CAPPED_OUT/lib${LEAN_PATH:+:$LEAN_PATH}"
lean -j1 --root="$CAPPED_OUT/src" -o "$CAPPED_OUT/lib/Rule30Submission.olean" "$CAPPED_OUT/src/Rule30Submission.lean"
lean -j1 --root="$CAPPED_OUT" --run "$CAPPED_OUT/Check.lean" Rule30Submission --claim partial \
 --headline Rule30Submission.ArcRule30Exclusion.no_visible_rotation \
 --headline Rule30Submission.ArcRule30Exclusion.no_eventual_visible_rotation \
 --headline Rule30Submission.ArcRule30Exclusion.no_visible_endpoint_variant \
 --headline Rule30Submission.ArcRule30Exclusion.no_visible_interval_union > "$CAPPED_OUT/check.json"
python3 - <<'GUARD'
from pathlib import Path
import ast,json,os,re
out=Path(os.environ['CAPPED_OUT']);text=(out/'out.txt').read_text()
src=(out/'src/Rule30Submission.lean').read_text()
expected=set(re.findall(r'^#print axioms (\S+)\s*$',src,re.M))
rows=re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]",text)
standard={'propext','Classical.choice','Quot.sound'}
if len(expected)!=40 or len(rows)!=40 or {name for name,_ in rows}!=expected:
 raise SystemExit('FAIL: exact40 expected standard axiom outputs')
if re.search(r'(?m)^.*\b(?:warning|error):',text):raise SystemExit('FAIL: compiler diagnostic')
for name,axes in rows:
 if not {a.strip() for a in axes.split(',') if a.strip()}<=standard:raise SystemExit('FAIL: nonstandard axiom '+name)
raw=(out/'check.json').read_text();print(raw,end='')
objects=[json.loads(line) for line in raw.splitlines() if line.startswith('{')]
if len(objects)!=1:raise SystemExit('FAIL: unique checker JSON')
c=objects[0]
heads={'Rule30Submission.ArcRule30Exclusion.'+x for x in ['no_visible_rotation','no_eventual_visible_rotation','no_visible_endpoint_variant','no_visible_interval_union']}
h=c.get('headlines',[]);decl=c.get('declared',[]);replay=c.get('replay',{})
if c.get('module')!='Rule30Submission' or c.get('verdict')!='pass' or replay.get('ok') is not True:
 raise SystemExit('FAIL: module/verdict/kernel replay')
if c.get('importsStatements') is not True or c.get('newAxioms')!=[]:raise SystemExit('FAIL: official import/new axioms')
if len(h)!=4 or {x.get('name') for x in h}!=heads or any(x.get('ok') is not True or x.get('typeMatches') is not True or x.get('found') is not True for x in h):
 raise SystemExit('FAIL: exact4 headlines found/ok/type-matching')
if len(decl)<40 or any(x.get('standardAxioms') is not True for x in decl) or replay.get('constants',0)<40:
 raise SystemExit('FAIL: whole submitted proof declaration/replay guard')
result={'status':'PASS','headline_count':40,'checker':c,'scope':'normalized finite-left clock, explicit large-digit finite-step rotation; no all-irrational/prize claim'}
(out/'submission-check.json').write_text(json.dumps(result,indent=2)+'\n')
print('ARC_SINGLE_FILE_PASS',flush=True)
GUARD
