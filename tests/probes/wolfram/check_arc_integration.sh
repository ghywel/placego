#!/bin/sh
# GC2099: full current-toolchain arc integration, exact source/unchanged checker, no dependency/library build.
# Invoke via lake env from the ALREADY MATERIALIZED compatible kit root. One stage only; first failure ends it.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
arc_full_source=$1
python3 - "$arc_full_source" <<'PREP'
from pathlib import Path
import hashlib,json,os,sys
expected = {'ArcBreakBounds': 'cbb2f4ba2a384a9b9cb077f4b5c9242339237864bc47af70f0afddaf5b78f1a6', 'ArcBreakSequence': '7d6f45508ce456e11cefa1e305580f8d1195f26e5cd1375e9cd9e96dd53ffdfe', 'ArcDeterminantDraft': 'aa2402bddf84deac9c38f3383fb55b57e6f088a1453b02dd465b128d99fa083a', 'ArcCoverDraft': '58268dd3a9e52652fe904d390c51b2354b6eae90bde99fd06e12c4e60958d5f4', 'ArcStepCodeDraft': 'b207135e62cb7e8dde7f4e79ecb1f20f6825001efdae997536ce60dc0f6dafe5', 'ArcTailBounds': 'c66c73e83c9ed52799f3143be46f5e6d880da055007b82b751f7f7f68d649f35', 'ArcContinuantsDraft': '7c32512f60fb003c598d86d31474109e700edac3991528b1e3522cba4ea79fab', 'ArcRotationDraft': 'd8390f81fa3f19da78f37008d30101270b6885e0658993cd326907820c955aee', 'ArcRule30BridgeDraft': '4f644cc44e1365dd7b9292a64dbd14a5984ed2758506a3cab072dcb15f63d6b1', 'ArcEndpointDraft': 'e9da94e4fff13dc76776b31e5c9c1fb354ebd2b5167237b2a60aaa4470b41a8c', 'ArcIntervalCodeDraft': '685d4188889f8782d59b11d3c16962a6444a3a7e5408d0883b35d376ab687f1b', 'ArcRule30ExclusionDraft': '5b94c35026a6b691fa51254111d443d26934799458f3d40140cd57af1dcab839'}
root=Path(sys.argv[1]);out=Path(os.environ['CAPPED_OUT']);src=out/'src';lib=out/'lib'
src.mkdir();lib.mkdir()
for name,digest in expected.items():
    data=(root/(name+'.lean')).read_bytes()
    if hashlib.sha256(data).hexdigest()!=digest:raise SystemExit('REFUSED: frozen source '+name)
    (src/(name+'.lean')).write_bytes(data)
checker=Path('Check.lean').read_bytes()
if hashlib.sha256(checker).hexdigest()!='b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905':
    raise SystemExit('REFUSED: unchanged checker digest')
(out/'Check.lean').write_bytes(checker)
(out/'sources.json').write_text(json.dumps(expected,indent=2)+'\n')
print('ARC_INTEGRATION_SOURCES_OK',flush=True)
PREP
export LEAN_PATH="$CAPPED_OUT/lib${LEAN_PATH:+:$LEAN_PATH}"
for arc_full_module in ArcBreakBounds ArcBreakSequence ArcDeterminantDraft ArcCoverDraft ArcStepCodeDraft ArcTailBounds ArcContinuantsDraft ArcRotationDraft ArcRule30BridgeDraft ArcEndpointDraft ArcIntervalCodeDraft ArcRule30ExclusionDraft; do
    lean -j1 --root="$CAPPED_OUT/src" -o "$CAPPED_OUT/lib/$arc_full_module.olean" "$CAPPED_OUT/src/$arc_full_module.lean"
done
lean -j1 --root="$CAPPED_OUT" --run "$CAPPED_OUT/Check.lean" ArcRule30ExclusionDraft --claim partial \
    --headline ArcRule30Exclusion.no_visible_rotation \
    --headline ArcRule30Exclusion.no_eventual_visible_rotation \
    --headline ArcRule30Exclusion.no_visible_endpoint_variant \
    --headline ArcRule30Exclusion.no_visible_interval_union > "$CAPPED_OUT/check.json"
python3 - <<'GUARD'
from pathlib import Path
import json,os,re
out=Path(os.environ['CAPPED_OUT']);text=(out/'out.txt').read_text()
expected=set(['ArcBreakBounds.label_collision', 'ArcBreakBounds.break_envelope', 'ArcBreakBounds.spacing_bound', 'ArcBreakBounds.next_denominator_covers_window', 'ArcBreakSequence.future_break', 'ArcBreakSequence.sequence_break', 'ArcBreakSequence.sequence_strict', 'ArcBreakSequence.labelled_spacing_bound', 'ArcDeterminant.spacing_of_bezout', 'ArcDeterminant.no_short_return', 'ArcCover.same_interval_return', 'ArcCover.short_return', 'ArcCover.no_repeat_of_cover', 'ArcStepCode.crossing', 'ArcStepCode.break_has_lift', 'ArcStepCode.lift_cover', 'ArcStepCode.no_repeat_bound', 'ArcTailBounds.shift_repeat_bound', 'ArcTailBounds.eventual_transfer', 'ArcTailBounds.uniform_eventual_transfer', 'ArcTailBounds.finite_single_hits_cutoff', 'ArcTailBounds.finite_single_hits_eventual', 'ArcDeterminant.continuant_bezout', 'ArcDeterminant.continuant_error_lt_next', 'ArcRotation.denominator_next', 'ArcRotation.previous_margin', 'ArcRotation.next_covers_window', 'ArcRotation.no_repeat_at_large_digit', 'ArcRotation.repeat_bound_fails', 'ArcRotation.no_uniform_repeat_bound', 'ArcRule30Bridge.repeat_bound', 'ArcEndpoint.hit_unique', 'ArcEndpoint.eventual_agreement', 'ArcIntervalCode.member_shift', 'ArcIntervalCode.member_constant', 'ArcIntervalCode.code', 'ArcRule30Exclusion.no_visible_rotation', 'ArcRule30Exclusion.no_eventual_visible_rotation', 'ArcRule30Exclusion.no_visible_endpoint_variant', 'ArcRule30Exclusion.no_visible_interval_union'])
rows=re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]",text)
standard={'propext','Classical.choice','Quot.sound'}
if len(rows)!=40 or {name for name,_ in rows}!=expected:raise SystemExit('FAIL: exact40 axiom outputs')
if re.search(r'(?m)^.*\b(?:warning|error):',text):raise SystemExit('FAIL: compiler diagnostic retained')
for name,axes in rows:
    if not {a.strip() for a in axes.split(',') if a.strip()}<=standard:raise SystemExit('FAIL: nonstandard axiom '+name)
raw=(out/'check.json').read_text();print(raw,end='')
objects=[json.loads(line) for line in raw.splitlines() if line.startswith('{')]
if len(objects)!=1:raise SystemExit('FAIL: unique checker JSON')
c=objects[0]
headlines={'ArcRule30Exclusion.'+n for n in ['no_visible_rotation','no_eventual_visible_rotation','no_visible_endpoint_variant','no_visible_interval_union']}
h=c.get('headlines',[])
if c.get('module')!='ArcRule30ExclusionDraft' or c.get('verdict')!='pass' or c.get('replay',{}).get('ok') is not True:
    raise SystemExit('FAIL: checker module/verdict/replay')
if c.get('importsStatements') is not True or c.get('newAxioms')!=[]:raise SystemExit('FAIL: official-import/new-axiom guard')
if len(h)!=4 or {x.get('name') for x in h}!=headlines or any(x.get('ok') is not True for x in h):
    raise SystemExit('FAIL: exact4 checker headlines')
declared=c.get('declared',[])
if len(declared)<4 or any(x.get('standardAxioms') is not True for x in declared):
    raise SystemExit('FAIL: own declaration axiom guard')
result={'status':'PASS','headline_count':40,'axioms':{name:axes for name,axes in rows},'checker':c,
        'scope':'actual normalized finite-left Rule30, irrational rotation, explicit large-digit condition; not prize/all-irrational'}
(out/'integration-check.json').write_text(json.dumps(result,indent=2)+'\n')
print('ARC_FULL_INTEGRATION_PASS',flush=True)
GUARD
