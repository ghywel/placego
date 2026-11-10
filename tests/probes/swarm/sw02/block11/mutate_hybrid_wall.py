#!/usr/bin/env python3
"""mutate_hybrid_wall.py: must-fail mutants of the S-08 hybrid module Rule30HybridWall (L1636).

Prediction (written before the first run): each mutant is rejected. Counterfactual: an accepted mutant means the
proof step it touches does not carry the claim. Record searched: GC2804 and GC2815 (the carried BR-3.1 scope, its domain repair and the semiconjugacy).
M1 the width-6 list without 61; M2 the semiconjugacy with one step of P; M3 the coefficient family with c(4m+1) = c(4m+3);
M4 rule 150 at even depths; M5 no immortal row of width 2; M6 the even-time constant without b(0).

Run from the kit's lean/ directory: python3 -I PATH/mutate_hybrid_wall.py MODULE OUTDIR
"""
import os
import subprocess
import sys

src, out = sys.argv[1], sys.argv[2]
base = open(src, encoding='utf-8').read()
M = [
    ('M1', "    Immortal (rowOf n) ↔ n = 3 ∨ n = 11 ∨ n = 53 ∨ n = 61 := by",
     "    Immortal (rowOf n) ↔ n = 3 ∨ n = 11 ∨ n = 53 := by"),
    ('M2', "theorem D_P_P (x : Row × Row) : D (P (P x)) = P (D x) := by",
     "theorem D_P_P (x : Row × Row) : D (P x) = P (D x) := by"),
    ('M3', "  c 1 = true ∧ ∀ m, c (4 * m + 3) = false ∧ c (4 * m + 1) = c (4 * m + 2)",
     "  c 1 = true ∧ ∀ m, c (4 * m + 3) = false ∧ c (4 * m + 1) = c (4 * m + 3)"),
    ('M4', "  else xor (x (k + 1)) (xor (if 2 ≤ k then x (k - 1) else false) (if k % 2 = 1 then x k else false))",
     "  else xor (x (k + 1)) (xor (if 2 ≤ k then x (k - 1) else false) (if k % 2 = 0 then x k else false))"),
    ('M5', "theorem not_immortal_width_one {x : Row} (hx : WidthLE 1 x) : ¬ Immortal x := by",
     "theorem not_immortal_width_one {x : Row} (hx : WidthLE 2 x) : ¬ Immortal x := by"),
    ('M6', "    (iter P (2 * s) x).1 0 = if s = 0 then x.1 0 else xor (x.1 0) (x.2 0) := by",
     "    (iter P (2 * s) x).1 0 = if s = 0 then x.1 0 else x.1 0 := by"),
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
