#!/bin/sh
# both_dev_probe.sh (Local, L1115): development compiles of the universal-start release candidate after one tactic
# reorder (`first | omega | simp [loop, St.m]` in loop_spec's zero case, which Mathlib's unusedTactic linter flagged in
# sub_dev_probe.sh). Both forms are compiled with their sixteen `decide +kernel` groups replaced by `sorry`, so no
# certificate case is evaluated and no checker runs:
#   C: the catalog module (sha256 12068af9...) under the root UniversalStartDev, core imports only;
#   S: the submission form (sha256 17fdfbcb...) under `import Rule30PrizeKit`, with Mathlib active.
# Prediction: each exits 0 with exactly 16 sorry warnings, no other warning and no error.
# Counterfactual: an error or another warning in either form is kept and fixed before any frozen stage.
# Record searched: sub_dev_probe.sh's result (16 sorry, 0 errors, one unused-omega linter warning at loop_spec).
# Caps: CPU 300 per process, wall 600, RSS 6144 MiB, file 16, disk 64, launch 6144, ongoing 1024, swap 512.
# Invoke from the pipeline kit root, under run_capped.py, through `lake env sh both_dev_probe.sh <catalog> <submission>`.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
python3 - "$1" "$2" <<'PY'
from pathlib import Path
import hashlib, os, sys
out = Path(os.environ['CAPPED_OUT'])
expected = ['12068af9b91a37602211ffb0ceb7c9d8e64e13371c938719adf4916bbfda0fae',
            '17fdfbcb8833b77ee5a511d9f50f52997cf6c25429dbacb63b1b17c1e63fde30']
targets = [out / 'src' / 'UniversalStartDev' / 'Rule30UniversalStart.lean', out / 'Rule30SubmissionDev.lean']
(out / 'src' / 'UniversalStartDev').mkdir(parents=True)
for path, digest, target in zip(sys.argv[1:3], expected, targets):
    text = Path(path).read_text()
    actual = hashlib.sha256(text.encode()).hexdigest()
    print(Path(path).name, 'sha256', actual, flush=True)
    if actual != digest:
        raise SystemExit('REFUSED: digest ' + Path(path).name)
    if text.count('  decide +kernel\n') != 16:
        raise SystemExit('REFUSED: expected 16 certificate groups')
    target.write_text(text.replace('  decide +kernel\n', '  sorry\n'))
PY
fail=0
for v in C S; do
  if [ "$v" = C ]; then
    file="$CAPPED_OUT/src/UniversalStartDev/Rule30UniversalStart.lean"; root="--root=$CAPPED_OUT/src"
  else
    file="$CAPPED_OUT/Rule30SubmissionDev.lean"; root="--root=$CAPPED_OUT"
  fi
  status=0
  /usr/bin/time -l lean -j1 "$root" "$file" > "$CAPPED_OUT/$v.out" 2> "$CAPPED_OUT/$v.time" || status=$?
  sorries=$(grep -c "declaration uses .sorry." "$CAPPED_OUT/$v.out" || true)
  warnings=$(grep -c ": warning" "$CAPPED_OUT/$v.out" || true)
  errors=$(grep -c ": error" "$CAPPED_OUT/$v.out" || true)
  echo "== $v: exit $status, sorry $sorries, warnings $warnings, errors $errors"
  grep -v "declaration uses .sorry." "$CAPPED_OUT/$v.out" | head -30 || true
  grep -E "real|maximum resident set size" "$CAPPED_OUT/$v.time"
  if [ "$status" -ne 0 ] || [ "$sorries" -ne 16 ] || [ "$warnings" -ne 16 ] || [ "$errors" -ne 0 ]; then fail=1; fi
done
[ "$fail" -eq 0 ] || { echo BOTH_DEV_PROBE_FAIL; exit 1; }
echo BOTH_DEV_PROBE_CLEAN
