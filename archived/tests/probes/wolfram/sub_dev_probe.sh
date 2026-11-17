#!/bin/sh
# sub_dev_probe.sh (Local, L1115): does the universal-start submission form elaborate under `import Rule30PrizeKit`
# (core catalog, Rule30Problem3 and Rule30Equivalents, so Mathlib's simp set is active)? The catalog module passed
# stage 4 with core imports only. This development compile replaces each of the sixteen `decide +kernel` groups by
# `sorry`, so no certificate case is evaluated and no checker runs.
# Prediction: exactly 16 sorry warnings and no error; peak RSS under 4 GB.
# Counterfactual: any error is a proof step that behaves differently under Mathlib (or a name clash under
# `open Ruliology.CellularAutomata`); it is kept, and the fix must be made in both forms before any frozen stage.
# Record searched: stage 4 receipt; GC2081 (the submission form was never validated); right-profiles stage A2.
# Caps: CPU 300 per process, wall 600, RSS 6144 MiB, file 16, disk 64, launch 6144, ongoing 1024, swap 512.
# Invoke from the pipeline kit root, under run_capped.py, through `lake env sh sub_dev_probe.sh <submission form>`.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
python3 - "$1" <<'PY'
from pathlib import Path
import hashlib, os, sys
out = Path(os.environ['CAPPED_OUT'])
source = Path(sys.argv[1]).read_text()
digest = hashlib.sha256(source.encode()).hexdigest()
print('submission sha256', digest, flush=True)
if digest != 'b3e35ffff16638cfc97fad318d3331a67798436a6fa645c06795784a13f21290':
    raise SystemExit('REFUSED: submission form digest')
n = source.count('  decide +kernel\n')
if n != 16:
    raise SystemExit('REFUSED: expected 16 certificate groups, found ' + str(n))
(out / 'Rule30SubmissionDev.lean').write_text(source.replace('  decide +kernel\n', '  sorry\n'))
PY
status=0
/usr/bin/time -l lean -j1 "$CAPPED_OUT/Rule30SubmissionDev.lean" > "$CAPPED_OUT/dev.out" 2> "$CAPPED_OUT/dev.time" || status=$?
echo "lean exit $status"
echo "sorry warnings: $(grep -c "declaration uses .sorry." "$CAPPED_OUT/dev.out" || true)"
echo "errors: $(grep -c ": error" "$CAPPED_OUT/dev.out" || true)"
grep -v "declaration uses .sorry." "$CAPPED_OUT/dev.out" | head -40 || true
grep -E "real|maximum resident set size" "$CAPPED_OUT/dev.time"
[ "$status" -eq 0 ] || exit "$status"
echo SUB_DEV_PROBE_CLEAN_EXIT
