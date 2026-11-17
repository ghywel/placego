#!/bin/sh
# Invoke through the already built compatible Mathlib project's lake env. No library/dependency build.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
arc_component_dir=$1
python3 - "$arc_component_dir" <<'PY_PREP'
from pathlib import Path
import hashlib, os, sys
out = Path(os.environ['CAPPED_OUT'])
source_dir = Path(sys.argv[1])
expected = {'ArcBreakBounds': 'cbb2f4ba2a384a9b9cb077f4b5c9242339237864bc47af70f0afddaf5b78f1a6', 'ArcBreakSequence': '7d6f45508ce456e11cefa1e305580f8d1195f26e5cd1375e9cd9e96dd53ffdfe', 'ArcDeterminantDraft': 'aa2402bddf84deac9c38f3383fb55b57e6f088a1453b02dd465b128d99fa083a', 'ArcCoverDraft': '58268dd3a9e52652fe904d390c51b2354b6eae90bde99fd06e12c4e60958d5f4', 'ArcStepCodeDraft': 'b207135e62cb7e8dde7f4e79ecb1f20f6825001efdae997536ce60dc0f6dafe5'}
src = out / 'src'
lib = out / 'lib'
src.mkdir()
lib.mkdir()
for name, digest in expected.items():
    data = (source_dir / (name + '.lean')).read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    print(name, 'sha256', actual, flush=True)
    if actual != digest:
        raise SystemExit('REFUSED: frozen source mismatch ' + name)
    (src / (name + '.lean')).write_bytes(data)
PY_PREP
export LEAN_PATH="$CAPPED_OUT/lib${LEAN_PATH:+:$LEAN_PATH}"
for arc_component in ArcBreakBounds ArcBreakSequence ArcDeterminantDraft ArcCoverDraft ArcStepCodeDraft; do
  lean -j1 --root="$CAPPED_OUT/src" -o "$CAPPED_OUT/lib/$arc_component.olean" "$CAPPED_OUT/src/$arc_component.lean"
done
python3 - <<'PY_GUARD'
from pathlib import Path
import json, os, re
out = Path(os.environ['CAPPED_OUT'])
text = (out / 'out.txt').read_text()
expected = {
    'ArcBreakBounds.label_collision', 'ArcBreakBounds.break_envelope',
    'ArcBreakBounds.spacing_bound', 'ArcBreakBounds.next_denominator_covers_window',
    'ArcBreakSequence.future_break', 'ArcBreakSequence.sequence_break',
    'ArcBreakSequence.sequence_strict', 'ArcBreakSequence.labelled_spacing_bound',
    'ArcDeterminant.spacing_of_bezout', 'ArcDeterminant.no_short_return',
    'ArcCover.same_interval_return', 'ArcCover.short_return', 'ArcCover.no_repeat_of_cover',
    'ArcStepCode.crossing', 'ArcStepCode.break_has_lift', 'ArcStepCode.lift_cover', 'ArcStepCode.no_repeat_bound'
}
rows = re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", text)
standard = {'propext', 'Classical.choice', 'Quot.sound'}
if len(rows) != 17 or {name for name, _ in rows} != expected:
    raise SystemExit('FAIL: exact17 headline axiom outputs missing/duplicated')
for name, axes in rows:
    used = {a.strip() for a in axes.split(',') if a.strip()}
    if not used <= standard:
        raise SystemExit('FAIL: nonstandard axiom for ' + name)
result = {'status': 'PASS', 'headlines': {name: axes for name, axes in rows},
          'scope': 'conditional components only; actual CF and physical Rule30 assembly absent'}
(out / 'component-check.json').write_text(json.dumps(result, indent=2) + '\n')
print('ARC_COMPONENT_CHECK_PASS', flush=True)
PY_GUARD
