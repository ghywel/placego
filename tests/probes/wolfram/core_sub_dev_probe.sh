#!/bin/sh
# core_sub_dev_probe.sh (Local, L1117): does the core-import universal-start submission candidate
# (Rule30Submission-core.lean, sha256 409e7c59...) elaborate? It is the reviewed submission form 17fdfbcb... with
# `import Rule30PrizeKit` replaced by `import Ruliology.CellularAutomata.Rule30Prize` and
# `import Ruliology.CellularAutomata.Rule30Realization` (the kit README allows Ruliology.* imports; Check.lean requires
# only the statement module). This development compile replaces each of the sixteen `decide +kernel` groups by `sorry`,
# so no certificate case is evaluated and no checker runs.
# Prediction: exactly 16 sorry warnings, no other warning and no error; about 1.2 s and under 400 MB, as the catalog.
# Counterfactual: an error means the candidate needs more than the two core imports; it is kept.
# Record searched: kit README line 86 and Check.lean's statementModule; A2b (4.55 GB with Rule30PrizeKit).
# Caps: CPU 120 per process, wall 300, RSS 2048 MiB, file 16, disk 32, launch 4096, ongoing 1024, swap 256.
# Invoke from the pipeline kit root, under run_capped.py, through `lake env sh core_sub_dev_probe.sh <core candidate>`.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
python3 - "$1" <<'PY'
from pathlib import Path
import hashlib, os, sys
out = Path(os.environ['CAPPED_OUT'])
source = Path(sys.argv[1]).read_text()
digest = hashlib.sha256(source.encode()).hexdigest()
print('submission sha256', digest, flush=True)
if digest != '409e7c5961243d0bd649bfc5854929d02db2e68b19edf7743dd8bffb93607559':
    raise SystemExit('REFUSED: submission form digest')
n = source.count('  decide +kernel\n')
if n != 16:
    raise SystemExit('REFUSED: expected 16 certificate groups, found ' + str(n))
(out / 'Rule30SubmissionCoreDev.lean').write_text(source.replace('  decide +kernel\n', '  sorry\n'))
PY
status=0
/usr/bin/time -l lean -j1 "$CAPPED_OUT/Rule30SubmissionCoreDev.lean" > "$CAPPED_OUT/dev.out" 2> "$CAPPED_OUT/dev.time" || status=$?
echo "lean exit $status"
echo "sorry warnings: $(grep -c "declaration uses .sorry." "$CAPPED_OUT/dev.out" || true)"
echo "errors: $(grep -c ": error" "$CAPPED_OUT/dev.out" || true)"
echo "warnings: $(grep -c ": warning" "$CAPPED_OUT/dev.out" || true)"
grep -v "declaration uses .sorry." "$CAPPED_OUT/dev.out" | head -40 || true
grep -E "real|maximum resident set size" "$CAPPED_OUT/dev.time"
[ "$status" -eq 0 ] || exit "$status"
echo CORE_SUB_DEV_PROBE_CLEAN_EXIT
