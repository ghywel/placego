#!/usr/bin/env python3
"""mutate_unrestricted_closing.py: must-fail mutants of the S-23 module Rule30UnrestrictedClosing (Cloud's K-08).

Prediction (written before the first run): each mutant is rejected. Counterfactual: an accepted mutant means the
statement or data it touches does not carry the claim. Record searched: GPT's K-08 comparison (GC2853) and Local's
carry (L1654); Cloud's LN-03.1 and section 11.3; kit Rule30ZeroBoundary; open PR52 (HomoclinicClosing, AllPastClosing).
M1 one bit of rowA flipped; M2 one bit of rowB's period flipped; M3 the old fixed-point reading G C = C;
M4 the mismatch at 14q+4 instead of 14q+3; M5 fB without its two leading whites; M6 the one-tick values swapped.

Run from the kit's lean/ directory: python3 -I PATH/mutate_unrestricted_closing.py MODULE OUTDIR
"""
import os
import subprocess
import sys

src, out = sys.argv[1], sys.argv[2]
base = open(src, encoding='utf-8').read()
M = [
    ('M1', "if d = 0 then false else [1, 0, 1, 1, 1, 1, 1].getD", "if d = 0 then false else [1, 0, 1, 1, 0, 1, 1].getD"),
    ('M2', "[0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0].getD", "[0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1].getD"),
    ('M3', "theorem two_C : ∀ k, zrow rowC 2 k = rowA k := by", "theorem two_C : ∀ k, zrow rowC 2 k = rowC k := by"),
    ('M4', "theorem differ_AB : ∀ q, rowA (14 * q + 3) ≠ rowB (14 * q + 3) := by", "theorem differ_AB : ∀ q, rowA (14 * q + 4) ≠ rowB (14 * q + 4) := by"),
    ('M5', "def fB (s : Nat) : Bool := decide (2 ≤ s ∧ s % 2 = 0)", "def fB (s : Nat) : Bool := decide (s % 2 = 0)"),
    ('M6', "zrow rowA 1 (14 * q + 4) = false ∧ zrow rowB 1 (14 * q + 4) = true := by", "zrow rowA 1 (14 * q + 4) = true ∧ zrow rowB 1 (14 * q + 4) = false := by"),
]
os.makedirs(out, exist_ok=True)
lake = os.path.expanduser('~/.elan/bin/lake')
ok = True
for name, a, b in M:
    assert base.count(a) == 1, (name, base.count(a))
    f = os.path.join(out, 'mut_%s.lean' % name)
    open(f, 'w', encoding='utf-8').write(base.replace(a, b))
    r = subprocess.run([lake, 'env', 'lean', f], capture_output=True, text=True, timeout=900)
    errs = [l for l in (r.stdout + r.stderr).splitlines() if ': error' in l]
    v = 'REJECTED' if r.returncode != 0 and errs else 'ACCEPTED'
    ok = ok and v == 'REJECTED'
    print(name, v, 'first error at line', errs[0].split(':')[1] if errs else '-',
          (errs[0].split(': error', 1)[1].strip()[:90] if errs else ''), flush=True)
print('ALL REJECTED' if ok else 'SOME ACCEPTED')
