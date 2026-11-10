#!/usr/bin/env python3
"""mutate_cone_tip.py: must-fail mutants of the S-17 module Rule30ConeTip (L1641).

Prediction (written before the first run): each mutant is rejected. Counterfactual: an accepted mutant means the
proof step it touches does not carry the claim. Record searched: Cloud CL773 and the triage report section 11.1 (the carried LN-02.1 cone-tip law).
M1 the cone-tip value at odd t; M2 the newest depth one deeper; M3 the derivative without the flip hypothesis;
M4 the chain without its negation; M5 the chain flip parity reversed.

Run from the kit's lean/ directory: python3 -I PATH/mutate_cone_tip.py MODULE OUTDIR
"""
import os
import subprocess
import sys

src, out = sys.argv[1], sys.argv[2]
base = open(src, encoding='utf-8').read()
M = [
    ('M1', "      decide (t % 2 = 0) := by", "      decide (t % 2 = 1) := by"),
    ('M2', "      xor (zrow L s k) (zrow L' s k) = xor (L (k + s)) (L' (k + s)) := by",
     "      xor (zrow L s k) (zrow L' s k) = xor (L (k + s + 1)) (L' (k + s + 1)) := by"),
    ('M3', "    (hflip : xor (L d) (L' d) = true) :\n    ∀ s k, 1 ≤ k → k + s = d + 1",
     "    (hflip : True) :\n    ∀ s k, 1 ≤ k → k + s = d + 1"),
    ('M4', "  | k, s + 1 => xor (chain L (k + 1) s) (!zrow L s (k - 1))",
     "  | k, s + 1 => xor (chain L (k + 1) s) (zrow L s (k - 1))"),
    ('M5', "= decide (s % 2 = 1) := by", "= decide (s % 2 = 0) := by"),
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
