#!/bin/sh
# split_probe.sh (Local, L1114): does the split certificate's peak memory stay at one group's, and does candidate v3
# (Rule30UniversalStart-v3.lean, sha256 cc3ef77b...) elaborate apart from its sixteen kernel evaluations?
# v3 is the frozen f9843a95 source with two changes: `∃ m : Nat` in universal_start_finite (the frozen source's only
# elaboration error, found by cert_cost_probe.sh), and `cert` split into sixteen 16-case `decide +kernel` declarations
# cert_0000 ... cert_1111, assembled by an explicit match.
# Two derived variants are compiled in sequence, one Lean process each, timed with /usr/bin/time -l:
#   S1: cert_0000 evaluated, the other fifteen groups `sorry`;
#   S3: cert_0000, cert_0001 and cert_0010 evaluated, the other thirteen `sorry`.
# Neither proves `cert`. No checker runs. This is a probe, not the certificate stage.
# Prediction: both compile with no error, exactly 15 and 13 sorry warnings; S1 near the cost probe's V16 (625 MB,
# 2.3 s); S3 within about 100 MB of S1 (memory released between declarations), about 2 s longer.
# Counterfactual: an error means the fix or the assembly is wrong; S3 at about S1 + 600 MB means memory accumulates
# across declarations and a split does not bound the peak.
# Record searched: L1114's cost probe (V0 317 MB / 1.17 s, V1 336 MB, V16 625 MB / 2.34 s), the stage 3 receipt.
# Caps: CPU 120 per process, wall 300, RSS 3072 MiB, file 16, disk 64, launch 5120, ongoing 1024, swap 256.
# Invoke from the pipeline kit root, under run_capped.py, through `lake env sh split_probe.sh <v3 source>`.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
python3 - "$1" <<'PY'
from pathlib import Path
import hashlib, os, sys
out = Path(os.environ['CAPPED_OUT'])
source = Path(sys.argv[1]).read_text()
digest = hashlib.sha256(source.encode()).hexdigest()
print('source sha256', digest, flush=True)
if digest != 'cc3ef77b5a350cb198616ebb5df147f9388bd6958985749a41d195ee9c3ce63e':
    raise SystemExit('REFUSED: candidate source digest')
groups = [a + b + c + d for a in '01' for b in '01' for c in '01' for d in '01']
(out / 'src' / 'UniversalStartSplit').mkdir(parents=True)
(out / 'lib' / 'UniversalStartSplit').mkdir(parents=True)
for name, kept in (('S1', {'0000'}), ('S3', {'0000', '0001', '0010'})):
    text = source
    for g in groups:
        if g in kept:
            continue
        head = 'theorem cert_' + g + ' :'
        i = text.index(head)
        j = text.index('  decide +kernel\n', i)
        text = text[:j] + '  sorry\n' + text[j + len('  decide +kernel\n'):]
    (out / 'src' / 'UniversalStartSplit' / (name + '.lean')).write_text(text)
PY
export LEAN_PATH="$CAPPED_OUT/lib${LEAN_PATH:+:$LEAN_PATH}"
for v in S1 S3; do
  echo "== $v"
  /usr/bin/time -l lean -j1 --root="$CAPPED_OUT/src" -o "$CAPPED_OUT/lib/UniversalStartSplit/$v.olean" \
    "$CAPPED_OUT/src/UniversalStartSplit/$v.lean" > "$CAPPED_OUT/$v.out" 2> "$CAPPED_OUT/$v.time" || echo "$v FAILED"
  echo "sorry warnings: $(grep -c "declaration uses .sorry." "$CAPPED_OUT/$v.out" || true)"
  echo "errors: $(grep -c "error" "$CAPPED_OUT/$v.out" || true)"
  grep -v "declaration uses .sorry." "$CAPPED_OUT/$v.out" | head -20 || true
  grep -E "real|maximum resident set size" "$CAPPED_OUT/$v.time"
done
echo SPLIT_PROBE_DONE
