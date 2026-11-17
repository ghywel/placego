#!/bin/sh
# GC2093: compile the exact core-only finite-tail component; no Mathlib/Wolfram or dependency setup.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
arc_tail_lean=$1
python3 - <<'CHECK_SOURCE'
from pathlib import Path
import hashlib, os
expected = {'ArcBreakBounds': 'cbb2f4ba2a384a9b9cb077f4b5c9242339237864bc47af70f0afddaf5b78f1a6', 'ArcBreakSequence': '7d6f45508ce456e11cefa1e305580f8d1195f26e5cd1375e9cd9e96dd53ffdfe', 'ArcTailBounds': 'c66c73e83c9ed52799f3143be46f5e6d880da055007b82b751f7f7f68d649f35'}
root = Path('reports/wolfram-agents/submissions/arc-codes')
out = Path(os.environ['CAPPED_OUT'])
for name, digest in expected.items():
    data = (root / (name + '.lean')).read_bytes()
    if hashlib.sha256(data).hexdigest() != digest:
        raise SystemExit('REFUSED: source digest ' + name)
    (out / (name + '.lean')).write_bytes(data)
CHECK_SOURCE
cd "$CAPPED_OUT"
export LEAN_PATH="$CAPPED_OUT${LEAN_PATH:+:$LEAN_PATH}"
"$arc_tail_lean" -o ArcBreakBounds.olean ArcBreakBounds.lean
"$arc_tail_lean" -o ArcBreakSequence.olean ArcBreakSequence.lean
"$arc_tail_lean" -o ArcTailBounds.olean ArcTailBounds.lean
printf '%s\n' ARC_TAIL_COMPILE_PASS
