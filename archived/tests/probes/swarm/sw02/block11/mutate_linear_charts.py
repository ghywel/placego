#!/usr/bin/env python3
"""mutate_linear_charts.py: must-fail mutants of the S-24 module Rule30LinearCharts (Cloud's K-10, Theorem D).

Prediction (written before the first run): each mutant is rejected. Counterfactual: an accepted mutant means the
statement or hypothesis it touches does not carry the claim. Record searched: the swarm XP-2 report (Theorem D),
Local's feasibility map (L1661) and GPT's carry of the group-law lemma (GC2894); kit Rule30ZeroBoundary.
False statements: M1 the group-law lemma without the neutral element (x xor y xor 1 is a law); M2 without
commutativity (x_n + y_n + y_(n+1) is a law); M3 the free bits shifted by two; M4 the white correction term true;
M5 the chart linear instead of affine. Hypothesis the proof uses: M6 the inverse chart without finite dependence.

Run from the kit's lean/ directory: python3 -I PATH/mutate_linear_charts.py MODULE OUTDIR
"""
import os
import subprocess
import sys

src, out = sys.argv[1], sys.argv[2]
base = open(src, encoding='utf-8').read()
M = [
    ('M1', "    (hid : ∀ x, op x (fun _ => false) = x) (hcomm : ∀ x y, op x y = op y x)\n    (hinv : ∀ x y, op (op x y) y = x)\n    (hsh",
     "    (hid : True) (hcomm : ∀ x y, op x y = op y x)\n    (hinv : ∀ x y, op (op x y) y = x)\n    (hsh"),
    ('M2', "    (hid : ∀ x, op x (fun _ => false) = x) (hcomm : ∀ x y, op x y = op y x)\n    (hinv : ∀ x y, op (op x y) y = x)\n    (hsh",
     "    (hid : ∀ x, op x (fun _ => false) = x) (hcomm : True)\n    (hinv : ∀ x y, op (op x y) y = x)\n    (hsh"),
    ('M3', "theorem fb_shift (L : Nat → Bool) : fb (zrow L 2) = fun s => fb L (s + 1) := by",
     "theorem fb_shift (L : Nat → Bool) : fb (zrow L 2) = fun s => fb L (s + 2) := by"),
    ('M4', "    qOf op u (fun _ => false) = false := by", "    qOf op u (fun _ => false) = true := by"),
    ('M5', "    ∀ f g, Φ (Theta (xr f g)) = xr (xr (Φ (Theta f)) (Φ (Theta g))) (Φ (Theta (fun _ => false))) :=",
     "    ∀ f g, Φ (Theta (xr f g)) = xr (Φ (Theta f)) (Φ (Theta g)) :="),
    ('M6', "    (hcont : ULD KK Φ) (hcont' : ULD A Φ') :\n    ∀ f g, Φ (Theta (xr f g))",
     "    (hcont : ULD KK Φ) (hcont' : True) :\n    ∀ f g, Φ (Theta (xr f g))"),
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
