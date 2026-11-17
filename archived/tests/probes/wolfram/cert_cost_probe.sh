#!/bin/sh
# cert_cost_probe.sh (Local, L1114): what one case and one 16-case group of the universal-start certificate cost the
# kernel, measured before any split certificate is designed. Stage 3 (receipts/local-gc2084-stage3.json) was stopped at
# 4.3 GB group RSS, about 11 s into the module compile, with RSS rising about 250 MB/s; the development compiles
# without the certificate took about 1 s.
#
# Three derived copies of the frozen source (f9843a95...) are compiled in sequence, one Lean process each, under the
# root UniversalStartCost (no Ruliology/ in the output lib). Each is timed with /usr/bin/time -l for its own maximum RSS:
#   V0: `cert` proved by `sorry` (the baseline: every other declaration of the module);
#   V1: V0 plus one case, `certOK false false false false false false false false = true`, by `decide +kernel`;
#   V16: V0 plus the 16 cases `∀ b3 b4 b5 b6, certOK false false false false b3 b4 b5 b6 = true`, by `decide +kernel`.
# None of them proves `cert`; this is a cost measurement, not a certificate stage, and no checker runs.
# Prediction: V0 about 1 s and under 1 GB; V1 under 0.5 s and 100 MB above V0; V16 about 16 times V1's increment.
# Counterfactual: V1 above 1 GB or 10 s means the per-case loop itself is too costly (a bit-packed design, not a
# split); V16 above about 3 GB means a 16-way split is not enough; V16 far from 16 x V1 means the cost is not
# per-case linear.
# Record searched: L1106 (the certificate design), GC2078/GC2084 (the stage reads), the stage 3 receipt.
# Caps: CPU 300 per process, wall 600, RSS 3584 MiB, file 16, disk 64, launch 5120, ongoing 1024, swap 256.
# Invoke from the pipeline kit root, under run_capped.py, through `lake env sh cert_cost_probe.sh <frozen source>`.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
python3 - "$1" <<'PY'
from pathlib import Path
import hashlib, os, sys
out = Path(os.environ['CAPPED_OUT'])
source = Path(sys.argv[1]).read_text()
digest = hashlib.sha256(source.encode()).hexdigest()
print('source sha256', digest, flush=True)
if digest != 'f9843a955ae423071484e07b55138a8bd43e4c6b3e22eeb3964ea73fbb333138':
    raise SystemExit('REFUSED: frozen source digest')
cert = ('theorem cert : ∀ p b0 b1 b2 b3 b4 b5 b6 : Bool, certOK p b0 b1 b2 b3 b4 b5 b6 = true := by\n'
        '  decide +kernel\n')
assert source.count(cert) == 1
stub = cert.replace('decide +kernel', 'sorry')
extra = {
    'V0': '',
    'V1': ('\ntheorem cert_one : certOK false false false false false false false false = true := by\n'
           '  decide +kernel\n'),
    'V16': ('\ntheorem cert_16 : ∀ b3 b4 b5 b6 : Bool, certOK false false false false b3 b4 b5 b6 = true := by\n'
            '  decide +kernel\n'),
}
(out / 'src' / 'UniversalStartCost').mkdir(parents=True)
(out / 'lib' / 'UniversalStartCost').mkdir(parents=True)
for name, add in extra.items():
    (out / 'src' / 'UniversalStartCost' / (name + '.lean')).write_text(source.replace(cert, stub + add))
PY
export LEAN_PATH="$CAPPED_OUT/lib${LEAN_PATH:+:$LEAN_PATH}"
for v in V0 V1 V16; do
  echo "== $v"
  /usr/bin/time -l lean -j1 --root="$CAPPED_OUT/src" -o "$CAPPED_OUT/lib/UniversalStartCost/$v.olean" \
    "$CAPPED_OUT/src/UniversalStartCost/$v.lean" > "$CAPPED_OUT/$v.out" 2> "$CAPPED_OUT/$v.time" || echo "$v FAILED"
  grep -v "declaration uses 'sorry'" "$CAPPED_OUT/$v.out" | head -20 || true
  grep -E "real|maximum resident set size" "$CAPPED_OUT/$v.time"
done
echo CERT_COST_PROBE_DONE
