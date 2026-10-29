#!/bin/sh
# rename_probe.sh (Local, L1112): the second test of a repaired universal-start layout. A two-line probe module
# stands in for the certificate module; nothing of the certificate is compiled or evaluated.
#
# Lean resolves a module's package root to the FIRST search-path entry that holds a directory named after the
# module's root. Stage 2's output lib had its own `Ruliology/`, first on LEAN_PATH, and so hid the kit's built
# package. A module's name comes from its file path under --root, not from its text, and declaration names come
# from its `namespace`. So the same bytes compiled at `UniversalStartCert/...` keep their declaration names and
# cannot shadow `Ruliology`.
#   A (control): the stage 2 layout. Predicted: the compile fails with "object file ... Rule30Prize.olean ... does
#     not exist".
#   B (renamed root): src/UniversalStartCert/OverlayProbe.lean compiled to lib/UniversalStartCert/. Predicted: it
#     compiles, and the unchanged Check.lean, given module UniversalStartCert.OverlayProbe and the probe's
#     namespaced headline, returns verdict pass with a successful replay.
# Counterfactual: if A passes, the diagnosis is wrong; if B fails, the renamed-root design is rejected and its
# diagnostic kept.
# Record searched: L1109, GC2081, receipts/local-gc2081-stage2.json, the overlay probe's DISK_STOP (run_capped
# sizes files through symlinks); Check.lean's only module condition is importing Rule30Prize (statementModule).
# Caps: CPU 60 per process, wall 120, RSS 3072 MiB, file 16, disk 16, launch 4096, ongoing 1024, swap 128.
# Invoke from the pipeline kit root, under run_capped.py, through `lake env sh rename_probe.sh`.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
python3 - <<'PY'
from pathlib import Path
import hashlib, os
out = Path(os.environ['CAPPED_OUT'])
checker = Path('Check.lean').read_bytes()
digest = hashlib.sha256(checker).hexdigest()
print('checker sha256', digest, flush=True)
if digest != 'b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905':
    raise SystemExit('REFUSED: Check.lean digest')
probe = '''module

public import Ruliology.CellularAutomata.Rule30Prize
public import Ruliology.CellularAutomata.Rule30Realization

@[expose] public section

namespace Ruliology.CellularAutomata.OverlayProbe

theorem probe : True := trivial

end Ruliology.CellularAutomata.OverlayProbe
'''
for layout, root in (('a', 'Ruliology/CellularAutomata'), ('b', 'UniversalStartCert')):
    (out / layout / 'src' / root).mkdir(parents=True)
    (out / layout / 'src' / root / 'OverlayProbe.lean').write_text(probe)
    (out / layout / 'lib' / root).mkdir(parents=True)
(out / 'Check.lean').write_bytes(checker)
PY
echo "== A: stage 2 layout (control)"
m=Ruliology/CellularAutomata/OverlayProbe
if LEAN_PATH="$CAPPED_OUT/a/lib:$LEAN_PATH" lean -j1 --root="$CAPPED_OUT/a/src" \
    -o "$CAPPED_OUT/a/lib/$m.olean" "$CAPPED_OUT/a/src/$m.lean" > "$CAPPED_OUT/control-A.txt" 2>&1; then
  echo "A_UNEXPECTED_PASS"
  exit 1
else
  python3 - <<'PY_CONTROL'
from pathlib import Path
import os
text = (Path(os.environ['CAPPED_OUT']) / 'control-A.txt').read_text()
print(text, end='')
if 'object file' not in text or 'Rule30Prize.olean' not in text or 'does not exist' not in text:
    raise SystemExit('FAIL: control A did not give the predicted import diagnostic')
print('A_FAILED_AS_PREDICTED', flush=True)
PY_CONTROL
fi
echo "== B: renamed root"
m=UniversalStartCert/OverlayProbe
export LEAN_PATH="$CAPPED_OUT/b/lib:$LEAN_PATH"
lean -j1 --root="$CAPPED_OUT/b/src" -o "$CAPPED_OUT/b/lib/$m.olean" "$CAPPED_OUT/b/src/$m.lean"
ls "$CAPPED_OUT/b/lib/UniversalStartCert/"
lean -j1 --root="$CAPPED_OUT" --run "$CAPPED_OUT/Check.lean" UniversalStartCert.OverlayProbe --claim partial \
  --headline Ruliology.CellularAutomata.OverlayProbe.probe > "$CAPPED_OUT/check.json"
cat "$CAPPED_OUT/check.json"
python3 - <<'PY'
import json, os
r = json.load(open(os.path.join(os.environ['CAPPED_OUT'], 'check.json')))
heads = r.get('headlines', [])
ok = (r.get('verdict') == 'pass' and r.get('replay', {}).get('ok') is True
      and r.get('importsStatements') is True and not r.get('newAxioms')
      and len(heads) == 1
      and heads[0].get('name') == 'Ruliology.CellularAutomata.OverlayProbe.probe'
      and heads[0].get('ok') is True)
print('B_RENAMED_CHECK_PASS' if ok else 'B_RENAMED_CHECK_FAIL', flush=True)
if not ok:
    raise SystemExit(1)
PY

# GC2083 amendment: fail on unexpected control success, wrong control diagnostic or checker/headline failure.
# Eleven owned process lifetimes expected (time/Lake/shell/setup Python/control Lean/control Python/B Lean/
# ls/checker Lean/cat/result Python), at most4 live; conservative660childCPU at60/process, not aggregate60CPU.
# If the previously frozen probe already ran, retain its exact output/JSON; do not rerun only for these guards.
