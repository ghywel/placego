#!/bin/sh
# overlay_probe.sh (Local, L1112): why the universal-start stage 2 compile could not see the kit, and whether a
# symlink overlay of the kit's built Ruliology package inside CAPPED_OUT fixes it. A two-line probe module stands in
# for the certificate module; nothing of the certificate is compiled or evaluated.
#
# Lean resolves a module's package root to the FIRST search-path entry that holds a directory named after the
# module's root (here `Ruliology`). An output lib that has its own `Ruliology/` and comes first on LEAN_PATH
# therefore hides the kit's built package.
#   A (control): the stage 2 layout, an empty output lib first. Predicted: the compile fails with
#     "object file ... Rule30Prize.olean ... does not exist".
#   B (overlay): an output lib whose Ruliology tree mirrors the kit's, with real directories and every file a
#     symlink. Predicted: the probe module compiles into it, and the unchanged Check.lean passes on the probe headline.
# Counterfactual: if A passes, the diagnosis is wrong; if B fails, the overlay design is rejected and its diagnostic kept.
# Record searched: L1109, GC2081, receipts/local-gc2081-stage2.json; Lean's SearchPath.findWithExt (first root wins).
# Caps: CPU 60 per process, wall 120, RSS 3072 MiB, file 16, disk 16, launch 4096, ongoing 1024, swap 128.
# Invoke from the pipeline kit root, under run_capped.py, through `lake env sh overlay_probe.sh`.
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
kit = next(Path(p) for p in os.environ['LEAN_PATH'].split(':')
           if (Path(p) / 'Ruliology' / 'CellularAutomata' / 'Rule30Prize.olean').is_file())
probe = '''module

public import Ruliology.CellularAutomata.Rule30Prize
public import Ruliology.CellularAutomata.Rule30Realization

@[expose] public section

namespace Ruliology.CellularAutomata.OverlayProbe

theorem probe : True := trivial

end Ruliology.CellularAutomata.OverlayProbe
'''
for layout in ('a', 'b'):
    src = out / layout / 'src' / 'Ruliology' / 'CellularAutomata'
    src.mkdir(parents=True)
    (src / 'OverlayProbe.lean').write_text(probe)
    (out / layout / 'lib' / 'Ruliology' / 'CellularAutomata').mkdir(parents=True)
(out / 'Check.lean').write_bytes(checker)
links = 0
lib = out / 'b' / 'lib'
for f in kit.iterdir():
    if f.name.startswith('Ruliology.'):
        (lib / f.name).symlink_to(f); links += 1
for root, dirs, files in os.walk(kit / 'Ruliology'):
    rel = Path(root).relative_to(kit)
    (lib / rel).mkdir(parents=True, exist_ok=True)
    for name in files:
        (lib / rel / name).symlink_to(Path(root) / name); links += 1
print('overlay symlinks', links, flush=True)
PY
m=Ruliology/CellularAutomata/OverlayProbe
echo "== A: stage 2 layout (control)"
if LEAN_PATH="$CAPPED_OUT/a/lib:$LEAN_PATH" lean -j1 --root="$CAPPED_OUT/a/src" \
    -o "$CAPPED_OUT/a/lib/$m.olean" "$CAPPED_OUT/a/src/$m.lean"; then
  echo "A_UNEXPECTED_PASS"
else
  echo "A_FAILED_AS_PREDICTED"
fi
echo "== B: symlink overlay"
export LEAN_PATH="$CAPPED_OUT/b/lib:$LEAN_PATH"
lean -j1 --root="$CAPPED_OUT/b/src" -o "$CAPPED_OUT/b/lib/$m.olean" "$CAPPED_OUT/b/src/$m.lean"
ls "$CAPPED_OUT/b/lib/Ruliology/CellularAutomata/" | grep OverlayProbe
lean -j1 --root="$CAPPED_OUT" --run "$CAPPED_OUT/Check.lean" Ruliology.CellularAutomata.OverlayProbe --claim partial \
  --headline Ruliology.CellularAutomata.OverlayProbe.probe > "$CAPPED_OUT/check.json" || true
cat "$CAPPED_OUT/check.json"
python3 - <<'PY'
import json, os
r = json.load(open(os.path.join(os.environ['CAPPED_OUT'], 'check.json')))
ok = r.get('verdict') == 'pass' and r.get('replay', {}).get('ok') is True
print('B_OVERLAY_CHECK_PASS' if ok else 'B_OVERLAY_CHECK_FAIL', flush=True)
PY
