#!/usr/bin/env python3
"""mutate_not_absorption.py: must-fail mutants of the S-05 kit module Rule30EtherThreeNotAbsorption (L1623).

Prediction (written before the first run): each mutant is rejected. Counterfactual: an accepted mutant means the
kernel check it touches does not carry the claim. Record searched: L1622, BN-L1's controls.
N1 the witness x0 plus one (st_i0 must fail); N2 one bit of the trap's strip table flipped (the check must fail);
N3 the apartness test claimed for t001 against itself; N4 the rule30-open half placed at state 24.

Run from the kit's lean/ directory: python3 -I PATH/mutate_not_absorption.py MODULE OUTDIR
"""
import os
import re
import subprocess
import sys

src, out = sys.argv[1], sys.argv[2]
base = open(src, encoding='utf-8').read()
R = re.search(r'def trap001fifteen_R : Nat := (\d+)', base).group(1)
sys.set_int_max_str_digits(100000)
M = [
    ('N1', 'def x0 : Nat := 266113541000008', 'def x0 : Nat := 266113541000009'),
    ('N2', 'def trap001fifteen_R : Nat := ' + R, 'def trap001fifteen_R : Nat := ' + str(int(R) ^ (1 << 1000))),
    ('N3', 'theorem fifteen_apart_t001 : disjointB trap001fifteen t001 47 = true := by decide +kernel',
     'theorem fifteen_apart_t001 : disjointB t001 t001 47 = true := by decide +kernel'),
    ('N4', 'trap001fifteen.st 25 = 196676618523018 ∧ trap001fifteen.lab 25 = 3',
     'trap001fifteen.st 24 = 196676618523018 ∧ trap001fifteen.lab 24 = 3'),
]
os.makedirs(out, exist_ok=True)
lake = os.path.expanduser('~/.elan/bin/lake')
ok = True
for name, a, b in M:
    assert base.count(a) == 1, (name, base.count(a))
    f = os.path.join(out, 'mut_%s.lean' % name)
    open(f, 'w', encoding='utf-8').write(base.replace(a, b))
    r = subprocess.run([lake, 'env', 'lean', f], capture_output=True, text=True, timeout=600)
    errs = [l for l in (r.stdout + r.stderr).splitlines() if ': error' in l]
    v = 'REJECTED' if r.returncode != 0 and errs else 'ACCEPTED'
    ok = ok and v == 'REJECTED'
    print(name, v, 'first error at line', errs[0].split(':')[1] if errs else '-', (errs[0].split(': error', 1)[1].strip()[:90] if errs else ''), flush=True)
print('ALL REJECTED' if ok else 'SOME ACCEPTED')
