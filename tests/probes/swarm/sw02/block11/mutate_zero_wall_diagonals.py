#!/usr/bin/env python3
"""mutate_zero_wall_diagonals.py: must-fail mutants of the S-12 module Rule30ZeroWallDiagonals (L1637).

Prediction (written before the first run): each mutant is rejected. Counterfactual: an accepted mutant means the
proof step it touches does not carry the claim. Record searched: GC2702, GC2817, GC2819 (the carried CP-3.2 scope, the entry guard and the word witnesses).
M1 the entry guard one step early; M2 the second diagonal black from time 0; M3 the factor count rising by exactly 1;
M4 the two-run lemma with M >= L + q; M5 a right-special factor of every length for every word;
M6 the complexity bound without the aperiodicity hypothesis.

Run from the kit's lean/ directory: python3 -I PATH/mutate_zero_wall_diagonals.py MODULE OUTDIR
"""
import os
import subprocess
import sys

src, out = sys.argv[1], sys.argv[2]
base = open(src, encoding='utf-8').read()
M = [
    ('M1', "theorem E_entry (L : Nat → Bool) (m j t : Nat) (h : j + 2 ≤ m + t) :",
     "theorem E_entry (L : Nat → Bool) (m j t : Nat) (h : j + 1 ≤ m + t) :"),
    ('M2', "    (hfin : ∀ k, m < k → L k = false) (t : Nat) : E L m 1 (t + 1) = true := by",
     "    (hfin : ∀ k, m < k → L k = false) (t : Nat) : E L m 1 t = true := by"),
    ('M3', "    factorCount f (n + 1) = factorCount f n + rightSpecialCount f n := by",
     "    factorCount f (n + 1) = factorCount f n + 1 := by"),
    ('M4', "theorem two_run {f : Nat → Bool} {q a b L M : Nat} (hq : 0 < q) (hM : L + q + 1 ≤ M)",
     "theorem two_run {f : Nat → Bool} {q a b L M : Nat} (hq : 0 < q) (hM : L + q ≤ M)"),
    ('M5', "theorem rightSpecialCount_pos {f : Nat → Bool} (hnp : ¬ EventuallyPeriodic f) (n : Nat) :",
     "theorem rightSpecialCount_pos {f : Nat → Bool} (hnp : True) (n : Nat) :"),
    ('M6', "theorem complexity_of_bounded_lag {f : Nat → Bool} (hnp : ¬ EventuallyPeriodic f)",
     "theorem complexity_of_bounded_lag {f : Nat → Bool} (hnp : True)"),
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
