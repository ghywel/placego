#!/bin/sh
# Finite-horizon components on Lean 4.35 (Local, L1158, for GPT's GC2142 plan): FiniteHorizonBounds and
# DenominatorBootstrap (core only) and MechanicalCarry (prebuilt Mathlib), each compiled on its own, one after another,
# with no lake. Every file is compiled even if an earlier one fails, so each gets its own 4.35 outcome; the stage passes
# only when all three print exactly their axiom reports (16 in all), with standard axioms only. Invoke as
#   SHARP_LEAN=<toolchain lean> KIT_ROOT=<pipeline kit root> sh check_finite_horizon_435.sh SOURCE_DIR
# under run_capped.py --track-tree.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
: "${SHARP_LEAN:?select the installed 4.35 compiler explicitly}"
: "${KIT_ROOT:?the pipeline kit root with prebuilt .lake/packages}"
python3 - "$1" <<'PY'
from pathlib import Path
import hashlib, os, sys
pins = {'FiniteHorizonBounds': 'ceafe8f929b8a5d62ab2e8a0ea3b7ac7eb9cd3c589018e7f24191d12a8ffd7c9',
        'DenominatorBootstrap': 'c9c8cbe4b3eb9b46cb7f87e32c26668c6a4245bd82a1a7d5a2ef6e2c4d4ae729',
        'MechanicalCarry': 'cf618c8591d4a6de353fa76713f2ed328874fb4cefe32aba001f2ff13fa224f5'}
out = Path(os.environ['CAPPED_OUT']) / 'src'
out.mkdir()
for name, expected in pins.items():
    data = (Path(sys.argv[1]) / (name + '.lean')).read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    print(name, 'sha256', digest, flush=True)
    if digest != expected:
        raise SystemExit('REFUSED: frozen digest mismatch for ' + name)
    (out / (name + '.lean')).write_bytes(data)
PY
path=""
for d in "$KIT_ROOT"/.lake/packages/*/.lake/build/lib/lean; do
  [ -d "$d" ] || { echo "FAIL: missing package build $d"; exit 1; }
  path="$path${path:+:}$d"
done
export LEAN_PATH="$path"
"$SHARP_LEAN" --version
for name in FiniteHorizonBounds DenominatorBootstrap MechanicalCarry; do
  if "$SHARP_LEAN" -j1 "$CAPPED_OUT/src/$name.lean" > "$CAPPED_OUT/$name.txt" 2>&1; then
    echo "$name exit 0"
  else
    echo "$name exit $?" ; echo "COMPILE_FAILED $name" >> "$CAPPED_OUT/failures.txt"
  fi
done
python3 - <<'PY'
from pathlib import Path
import os, re
out = Path(os.environ['CAPPED_OUT'])
heads = {'FiniteHorizonBounds': ['future_break', 'equal_of_zero_carry', 'first_carry', 'next_carry',
                                 'denominator_growth', 'zero_horizon_control'],
         'DenominatorBootstrap': ['four_steps', 'final_deadline', 'final_visit_contradiction'],
         'MechanicalCarry': ['difference_identity', 'carry_as_floor', 'carry_positive', 'carry_negative',
                             'nonzero_positive', 'nonzero_negative', 'half_open_endpoint_controls']}
line_re = re.compile(r"^'([\w.]+)' (?:depends on axioms: \[(.*)\]|does not depend on any axioms)$")
bad = []
if (out / 'failures.txt').exists():
    bad += (out / 'failures.txt').read_text().split('\n')
for name, hs in heads.items():
    text = (out / (name + '.txt')).read_text()
    print('== ' + name); print(text, end='')
    expected, seen = [name + '.' + h for h in hs], []
    for line in text.splitlines():
        if not line.strip():
            continue
        m = line_re.fullmatch(line)
        axioms = {a.strip() for a in ((m.group(2) or '') if m else '').split(',') if a.strip()}
        if not m or m.group(1) not in expected or not axioms <= {'propext', 'Classical.choice', 'Quot.sound'}:
            bad.append('%s: unexpected line: %s' % (name, line)); continue
        seen.append(m.group(1))
    if sorted(seen) != sorted(expected):
        bad.append('%s: %d of %d axiom reports, or repeats' % (name, len(seen), len(expected)))
    else:
        print('PART_PASS ' + name, flush=True)
bad = [b for b in bad if b.strip()]
if bad:
    raise SystemExit('FAIL:\n' + '\n'.join(bad))
print('FINITE_HORIZON_435_PASS (16 heads)', flush=True)
PY
