"""CL478: does one-hole protection survive peeling the top or the bottom element into some big bin?

Instance (M, q, c, t): pool [0, M] minus q, sizes c_i >= 3 summing to M, targets summing to T(M) - q,
protected: t_J >= T(C_J) for every proper group J.  slack_J = t_J - T(C_J).

  TOP peel into X (give M to X):    residual (M-1, q, c - e_X, t - M e_X) is protected  iff
                                    slack_J >= M - C_J = C_(J^c)  for every proper J containing X.
  BOTTOM peel into X (give 0 to X): residual pool [1, M] minus q, shifted down by 1:
                                    (M-1, q-1, c - e_X, t'), t'_i = t_i - c_i (i != X), t'_X = t_X - c_X + 1;
                                    protected iff slack_J >= C_J for every proper J avoiding X.
Both keep the pool a one-hole interval, so protection is the only invariant.  Peeling only from bins with
c_X >= 4 keeps all sizes >= 3; the base case is then M = 12, c = 3333 (finite, machine-checked).

Question: for every protected instance with M >= 13, is there a bin X with c_X >= 4 admitting a TOP or a
BOTTOM peel?  Predictions (written first): NO, failures exist, because a bin can be too rich for bottom
and too poor for top in some group simultaneously; the failures have a tight group through every big bin.
Counterfactual: 0 failures would make P0 a two-line induction from M = 12.

OUTCOME: M = 13: 495,384 protected instances, 59,352 with no admissible peel (top 285,636, bottom 150,396);
M = 14: 2,082,068 / 96,174.  Prediction held.  First failures: q = 1, sizes 3334, t = (6,15,33,36): A is tight
(size 3, cannot be peeled) and ABD has slack 2 < 3.  With the weaker invariant "all 14 group targets in
their spectra and every margin >= 2" (scratch peel2.py): 88,524 of 856,392 at M = 13 fail the same way.
Single-element peeling from big bins is not the induction.
"""
import itertools, sys
from collections import Counter

T = lambda n: n * (n + 1) // 2
SUB = [J for s in (1, 2, 3) for J in itertools.combinations(range(4), s)]

def run(M, maxfail=6):
    n = fails = 0; shapes = Counter(); ex = []
    for C in itertools.product(range(3, M - 8), repeat=4):
        if sum(C) != M or max(C) < 4: continue
        CJ = {J: sum(C[i] for i in J) for J in SUB}
        big = [i for i in range(4) if C[i] >= 4]
        for q in range(1, M):
            S = T(M) - q
            for t3 in itertools.product(*[range(T(C[i]), S - T(M - C[i]) + 1) for i in range(3)]):
                t = t3 + (S - sum(t3),)
                sl = {J: sum(t[i] for i in J) - T(CJ[J]) for J in SUB}
                if min(sl.values()) < 0: continue
                n += 1
                ok = False
                for X in big:
                    if all(sl[J] >= M - CJ[J] for J in SUB if X in J): ok = 'top'; break
                    if all(sl[J] >= CJ[J] for J in SUB if X not in J): ok = 'bottom'; break
                if ok: shapes[ok] += 1
                else:
                    fails += 1
                    if len(ex) < maxfail: ex.append((q, C, t))
    return n, fails, dict(shapes), ex

if __name__ == '__main__':
    for M in map(int, sys.argv[1:]):
        print(M, run(M), flush=True)
