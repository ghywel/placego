#!/usr/bin/env python3
"""mutate_recognizable_barrier.py: must-fail mutants of the S-19 module Rule30RecognizableBarrier (Cloud's K-06 with K-01).

Prediction (written before the first run): each mutant is rejected. Counterfactual: an accepted mutant means the
statement or hypothesis it touches does not carry the claim. Record searched: GPT's B2+ carry and Cloud's BR-2.1 (K-06),
LN-06 (K-01); the kit's Rule30ZeroBoundaryBarriers (RankCert, CertE, JointCert, no_edge_dfa_ranking); portal
R30-20261108-a0fd36 (the 1493/1507 sharpness).
False statements: M1 the rows stay odd for sixteen iterates; M2 the rows have width 12; M3 fifteen surviving double
steps; M4 one more alternating pair in the edge decomposition; M5 an ether word one cell longer.
Hypotheses the proof uses: M6 the rank relation without well-foundedness; M7 the width bound loosened by two.

Run from the kit's lean/ directory: python3 -I PATH/mutate_recognizable_barrier.py MODULE OUTDIR
"""
import os
import subprocess
import sys

src, out = sys.argv[1], sys.argv[2]
base = open(src, encoding='utf-8').read()
M = [
    ('M1', "    (∀ s, s < 15 → (Rule30ZeroBoundary.IntegerForm.iter G s 1493).testBit 0 = true) ∧",
     "    (∀ s, s < 16 → (Rule30ZeroBoundary.IntegerForm.iter G s 1493).testBit 0 = true) ∧"),
    ('M2', "    rowOfNat Y 11 = true ∧ ∀ k, 11 < k → rowOfNat Y k = false := by",
     "    rowOfNat Y 12 = true ∧ ∀ k, 12 < k → rowOfNat Y k = false := by"),
    ('M3', "    (∀ j, j ≤ 13 → Survives (iter (rowOfNat Y) j)) ∧ ¬ Survives (iter (rowOfNat Y) 14) := by",
     "    (∀ j, j ≤ 14 → Survives (iter (rowOfNat Y) j)) ∧ ¬ Survives (iter (rowOfNat Y) 15) := by"),
    ('M4', "    edgeWord (iter (trunc n) j) (n + 2 * j) = Zw j ++ altWord ((n + 1 - 2 * j) / 2) := by",
     "    edgeWord (iter (trunc n) j) (n + 2 * j) = Zw j ++ altWord ((n + 1 - 2 * j) / 2 + 1) := by"),
    ('M5', "        (etherWord (14 * N + 8 - 2 * (28 * c)) ++",
     "        (etherWord (14 * N + 9 - 2 * (28 * c)) ++"),
    ('M6', "    {r : α → α → Prop} (hwf : WellFounded r) (R : Nat → M → α) : ¬ RecCert S img r R :=",
     "    {r : α → α → Prop} (hwf : True) (R : Nat → M → α) : ¬ RecCert S img r R :="),
    ('M7', "(∀ k, W < k → s k = false) → -1 ≤ ρ s W ∧ ρ s W ≤ W) :",
     "(∀ k, W < k → s k = false) → -1 ≤ ρ s W ∧ ρ s W ≤ W + 2) :"),
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
