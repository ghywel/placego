#!/usr/bin/env python3
"""mutate_planted_survivor.py: must-fail mutants of the S-08 plant module Rule30PlantedSurvivor (L1628).

Prediction (written before the first run): each mutant is rejected. Counterfactual: an accepted mutant means the
proof step it touches does not carry the claim. Record searched: GC2804 (the carried BR-3.2 scope and repairs).
P1 no extra row in the table; P2 sites at even depths; P3 the width lemma without excluding trunc (2 L - 1);
P4 the extra row from 2 L <= W; P5 the fixed row trunc (2 L + 1).

Run from the kit's lean/ directory: python3 -I PATH/mutate_planted_survivor.py MODULE OUTDIR
"""
import os
import subprocess
import sys

src, out = sys.argv[1], sys.argv[2]
base = open(src, encoding='utf-8').read()
TABLE = "      cnt (2 ^ W) (fun Y => survZ (ofNat Y) t) + (if 2 * L - 1 ≤ W ∧ 2 * ((W + 1) / 2) ≤ t then 1 else 0) := by"
M = [
    ('P1', TABLE, "      cnt (2 ^ W) (fun Y => survZ (ofNat Y) t) + 0 := by"),
    ('P2', "def site (L k : Nat) : Bool := decide (k % 2 = 1 ∧ 2 * L + 1 ≤ k)",
     "def site (L k : Nat) : Bool := decide (k % 2 = 0 ∧ 2 * L + 1 ≤ k)"),
    ('P3', "    (hne : ¬ ∀ k, 1 ≤ k → y k = trunc (2 * L - 1) k) : Fin_ W (psiInv L y) := by",
     "    (hne : True) : Fin_ W (psiInv L y) := by"),
    ('P4', TABLE, TABLE.replace("2 * L - 1 ≤ W", "2 * L ≤ W")),
    ('P5', "theorem T_fixed (L : Nat) : ∀ k, 1 ≤ k → T L (trunc (2 * L - 1)) k = trunc (2 * L - 1) k := by",
     "theorem T_fixed (L : Nat) : ∀ k, 1 ≤ k → T L (trunc (2 * L + 1)) k = trunc (2 * L + 1) k := by"),
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
    print(name, v, 'first error at line', errs[0].split(':')[1] if errs else '-',
          (errs[0].split(': error', 1)[1].strip()[:90] if errs else ''), flush=True)
print('ALL REJECTED' if ok else 'SOME ACCEPTED')
