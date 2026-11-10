#!/usr/bin/env python3
"""mutate_free_middle.py: must-fail mutants of the S-13 kit module Rule30FreeMiddle (L1620).

Prediction (written before the first run): every mutant below is rejected by the compiler.
Counterfactual: a mutant that compiles means the weakened hypothesis or the false constant is not
load-bearing, and the module's statement or proof must be re-read before release.
Record searched: L1619 (S-13 claim), GC2702 section 2 (the carried statement and its guards).

L1 quadratic lower bound in rho_nonpos_of_descent (the theorem is then false: popcount - W^2);
L2 balance claimed from N >= m + 7; L3 the image count 255 instead of 256;
L4 the late horizon is the whole row (a bounded margin); L5 an all-black prefix instead of the stripe;
L6 a linear W instead of W^2 in lower_bound_needed (false by free_middle); L7 windows of m - 2 cells
in rank_local; L8 no_local_ranking_late with the hypothesis that u tends to infinity dropped.

Run from the kit's lean/ directory: python3 -I PATH/mutate_free_middle.py MODULE OUTDIR
"""
import os
import subprocess
import sys

src, out = sys.argv[1], sys.argv[2]
base = open(src, encoding='utf-8').read()
M = [
    ('L1', '''    (hlow : ∀ s W, Late u s W → -((K : Int) * (W : Int)) ≤ rank w e m β h s W)
    (hdesc : ∀ s W, Late u s W → rank w e m β h (dstep s) (W + 2) ≤ rank w e m β h s W)
    (d : List Bool) (hN : m + 8 ≤ d.length) : rho m h d ≤ 0 := by''',
     '''    (hlow : ∀ s W, Late u s W → -((K : Int) * (W : Int) * (W : Int)) ≤ rank w e m β h s W)
    (hdesc : ∀ s W, Late u s W → rank w e m β h (dstep s) (W + 2) ≤ rank w e m β h s W)
    (d : List Bool) (hN : m + 8 ≤ d.length) : rho m h d ≤ 0 := by'''),
    ('L2', 'theorem wsum_rho (m : Nat) (h : List Bool → Int) (N : Nat) (hN : m + 8 ≤ N) :',
     'theorem wsum_rho (m : Nat) (h : List Bool → Int) (N : Nat) (hN : m + 7 ≤ N) :'),
    ('L3', '    wsum (m + 8) (fun y => φ (Corner.image y)) = 256 * wsum m φ := by',
     '    wsum (m + 8) (fun y => φ (Corner.image y)) = 255 * wsum m φ := by'),
    ('L4', '    ∀ i, 2 * i ≤ W - u W → zrow s (2 * i) 1 = true', '    ∀ i, 2 * i ≤ W → zrow s (2 * i) 1 = true'),
    ('L5', '  else if k ≤ D then stripe k\n', '  else if k ≤ D then true\n'),
    ('L6', '''      rank 0 1 1 (fun W _ _ => -((W : Int) * (W : Int))) pop1 (dstep s) (W + 2) <
        rank 0 1 1 (fun W _ _ => -((W : Int) * (W : Int))) pop1 s W) ∧''',
     '''      rank 0 1 1 (fun W _ _ => -((W : Int))) pop1 (dstep s) (W + 2) <
        rank 0 1 1 (fun W _ _ => -((W : Int))) pop1 s W) ∧'''),
    ('L7', 'theorem rank_local (w e m : Nat) (hm : 1 ≤ m) (hw : m - 1 ≤ w) (he : m - 1 ≤ e)',
     'theorem rank_local (w e m : Nat) (hm : 1 ≤ m) (hw : m - 2 ≤ w) (he : m - 2 ≤ e)'),
    ('L8', 'theorem no_local_ranking_late (w e : Nat) (u : Nat → Nat) (hu : ToInfty u)',
     'theorem no_local_ranking_late (w e : Nat) (u : Nat → Nat) (hu : True)'),
]
os.makedirs(out, exist_ok=True)
lean = os.path.expanduser('~/.elan/bin/lake')
results = []
for name, a, b in M:
    assert base.count(a) == 1, (name, base.count(a))
    f = os.path.join(out, 'mut_%s.lean' % name)
    open(f, 'w', encoding='utf-8').write(base.replace(a, b))
    r = subprocess.run([lean, 'env', 'lean', f], capture_output=True, text=True, timeout=600)
    errs = [l for l in (r.stdout + r.stderr).splitlines() if ': error' in l]
    first = errs[0].split(': error', 1)[1].strip()[:120] if errs else ''
    line = errs[0].split(':')[1] if errs else ''
    verdict = 'REJECTED' if r.returncode != 0 and errs else 'ACCEPTED'
    results.append((name, verdict, line, first))
    print('%s %s first error at line %s: %s' % (name, verdict, line, first), flush=True)
print('ALL REJECTED' if all(v == 'REJECTED' for _, v, _, _ in results) else 'SOME ACCEPTED')
