#!/usr/bin/env python3
"""mutate_wall_deadlines.py: must-fail mutants of the S-18 module Rule30WallDeadlines (L1642).

Prediction (written before the first run): each mutant is rejected. Counterfactual: an accepted mutant means the
proof step it touches does not carry the claim. Record searched: Cloud CL773 and the triage report section 10 (the carried BR-6.1 deadlines).
M1 rule 90 white two ticks earlier; M2 rule 90 black one tick longer; M3 Fibonacci white at the even numbers;
M4 rule 150 white two ticks earlier; M5 rule 150 black one even tick longer; M6 the wall case reading depth 2.

Run from the kit's lean/ directory: python3 -I PATH/mutate_wall_deadlines.py MODULE OUTDIR
"""
import os
import subprocess
import sys

src, out = sys.argv[1], sys.argv[2]
base = open(src, encoding='utf-8').read()
M = [
    ('M1', "    ∃ s, 2 * s ≤ kstar W - 1 ∧ zr h90 L (2 * s) 1 = false := by",
     "    ∃ s, 2 * s ≤ kstar W - 3 ∧ zr h90 L (2 * s) 1 = false := by"),
    ('M2', "    ∀ s, 2 * s + 2 ≤ kstar W → zr h90 L (2 * s) 1 = true := by",
     "    ∀ s, 2 * s + 1 ≤ kstar W → zr h90 L (2 * s) 1 = true := by"),
    ('M3', "theorem fib2_mod (k : Nat) : fib2 k = decide (k % 3 ≠ 0) := by",
     "theorem fib2_mod (k : Nat) : fib2 k = decide (k % 2 ≠ 0) := by"),
    ('M4', "    ∃ s, 2 * s ≤ 2 * ((W + 1) / 2) ∧ zr h150 L (2 * s) 1 = false := by",
     "    ∃ s, 2 * s ≤ 2 * ((W + 1) / 2) - 2 ∧ zr h150 L (2 * s) 1 = false := by"),
    ('M5', "    ∀ s, 2 * s < 2 * ((W + 1) / 2) → zr h150 L (2 * s) 1 = true := by",
     "    ∀ s, 2 * s ≤ 2 * ((W + 1) / 2) → zr h150 L (2 * s) 1 = true := by"),
    ('M6', "    zr h150 L (t + 2) 1 = zr h150 L t 3 ∧", "    zr h150 L (t + 2) 1 = zr h150 L t 2 ∧"),
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
