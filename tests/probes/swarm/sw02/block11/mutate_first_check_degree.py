#!/usr/bin/env python3
"""mutate_first_check_degree.py: must-fail mutants of the S-06 module Rule30FirstCheckDegree (L1629).

Prediction (written before the first run): each mutant is rejected. Counterfactual: an accepted mutant means the
proof step it touches does not carry the claim. Record searched: GC2807 (the carried XP-1.1 scope, the n = 1 Walsh guard and the phase comparison).
M1 top coefficient n + 1 mod 2; M2 omitted coefficient n mod 2; M3 the other phase law for the kit phase;
M4 degree n at every n; M5 the Walsh law from n = 1; M6 the survivor parity at n = 0; M7 zs without its negation.

Run from the kit's lean/ directory: python3 -I PATH/mutate_first_check_degree.py MODULE OUTDIR
"""
import os
import subprocess
import sys

src, out = sys.argv[1], sys.argv[2]
base = open(src, encoding='utf-8').read()
M = [
    ('M1', "coeff (List.replicate n true) (check n) = decide (n % 2 = 1) := by",
     "coeff (List.replicate n true) (check n) = decide (n % 2 = 0) := by"),
    ('M2', "coeff (true :: false :: List.replicate (n - 2) true) (check n) = decide (n % 2 = 0) := by",
     "coeff (true :: false :: List.replicate (n - 2) true) (check n) = decide (n % 2 = 1) := by"),
    ('M3', "    coeff (List.replicate n true) (otherCheck n) = true := by",
     "    coeff (List.replicate n true) (check n) = true := by"),
    ('M4', "    IsDegree n (check n) (if n % 2 = 1 then n else n - 1) := by",
     "    IsDegree n (check n) n := by"),
    ('M5', "theorem walsh_mod_four (n : Nat) (hn : 2 ≤ n) :",
     "theorem walsh_mod_four (n : Nat) (hn : 1 ≤ n) :"),
    ('M6', "theorem first_check_parity (n : Nat) (hn : 1 ≤ n) : firstCheck n % 2 = n % 2 := by",
     "theorem first_check_parity (n : Nat) (hn : 0 ≤ n) : firstCheck n % 2 = n % 2 := by"),
    ('M7', "  | k + 2, t => xor (zs a (k + 1) (t + 1)) (!recon a k t)",
     "  | k + 2, t => xor (zs a (k + 1) (t + 1)) (recon a k t)"),
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
