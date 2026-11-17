#!/usr/bin/env python3
"""mutate_radius_two_clock.py: must-fail mutants of the S-07 kit module Rule30RadiusTwoClock (L1626).

Prediction (written before the first run): each mutant is rejected. Counterfactual: an accepted mutant means the
proof step it touches does not carry the claim. Record searched: GC2804 (the carried scope and its negative controls).
R1 the seed with black cells 0 and 3; R2 block rule 90 (the centre term dropped); R3 the clock claimed as t even;
R4 the band on odd positions; R5 the rule claimed right-permutive.

Run from the kit's lean/ directory: python3 -I PATH/mutate_radius_two_clock.py MODULE OUTDIR
"""
import os
import subprocess
import sys

src, out = sys.argv[1], sys.argv[2]
base = open(src, encoding='utf-8').read()
M = [
    ('R1', 'def seed02 : Int → Bool := fun i => decide (i = 0 ∨ i = 2)', 'def seed02 : Int → Bool := fun i => decide (i = 0 ∨ i = 3)'),
    ('R2', '  | t + 1, j => xor (xor (xor (z t (j - 1)) (z t j)) (z t (j + 1))) (src t j)',
     '  | t + 1, j => xor (xor (z t (j - 1)) (z t (j + 1))) (src t j)'),
    ('R3', '    evolN p q seed02 t (-1) = decide (t % 2 = 1) ∧ evolN p q seed02 t (-2) = decide (t % 2 = 1) := by',
     '    evolN p q seed02 t (-1) = decide (t % 2 = 0) ∧ evolN p q seed02 t (-2) = decide (t % 2 = 1) := by'),
    ('R4', 'def E (n : Nat) (j : Int) : Bool := decide (j % 2 = 0 ∧ -2 * (n : Int) ≤ j ∧ j ≤ 2 * (n : Int) - 2)',
     'def E (n : Nat) (j : Int) : Bool := decide (j % 2 = 1 ∧ -2 * (n : Int) ≤ j ∧ j ≤ 2 * (n : Int) - 2)'),
    ('R5', '    (∃ a b c d, xor a (g p q b c d false) = xor a (g p q b c d true)) ∧',
     '    (∀ a b c d, xor a (g p q b c d false) ≠ xor a (g p q b c d true)) ∧'),
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
