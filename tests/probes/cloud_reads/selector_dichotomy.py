"""CL487: a slack-gap dichotomy for the one-hole four-bin selector.

For an I2 instance let h1 = least singleton slack, h2 = least pair slack (each in its own frame).  Conjecture
(from CL486's failure profile at M = 12): (a) if h2 <= h1 + 2, the least pair's boundary (rank staircase, value
staircase or prefix-plus-pair) completes; (b) if h2 >= h1 + 3, the least singleton's G315 recipe (with
missing-pivot repairs) leaves a completing three-bin remainder.
Prediction (written first): both halves 100% at M = 12 and 13.  Counterfactual: a failure of either half is a
case the two-case proof must treat separately.
OUTCOME.  M = 12: (a) 42,756 / 42,756; (b) 80,209 / 80,221 (12 failures, q8 3333 (5,17,17,31) and permutations).
M = 13: (a) 259,704 / 259,776 (72 failures, equal pair targets such as 17/17 at h1 = 14, h2 = 16); (b) 596,592 /
596,616 (24 failures, (5,17,17,44) shape).  Prediction FAILED: the gap rule is not exact.  Every failure of
either half is rescued by the other case (CL486: the pair-first selector is 100%), so the selector, not the gap
rule, is the statement to prove; the failures are equal-split and pinned-plus-equal-split shapes.
"""
import sys, itertools
from collections import Counter
_argv = sys.argv; sys.argv = ['x']
exec(open('tests/probes/cloud_reads/singleton_or_pair.py').read().rsplit("\nif __name__ == '__main__':", 1)[0])
sys.argv = _argv

def run(M):
    cnt = Counter(); ex = []
    for C in itertools.product(range(3, M - 8), repeat=4):
        if sum(C) != M: continue
        CJ = {J: sum(C[i] for i in J) for J in SUB}
        for q in range(1, M):
            S = [x for x in range(M + 1) if x != q]; tot = sum(S); N = len(S)
            sp = spectra(S); mins = lambda c: sum(S[:c]); maxs = lambda c: sum(S[N - c:])
            Rf = [M - x for x in reversed(S)]
            for t3 in itertools.product(*[range(mins(C[i]), maxs(C[i]) + 1) for i in range(3)]):
                t = t3 + (tot - sum(t3),)
                tJ = {J: sum(t[i] for i in J) for J in SUB}
                if not all(tJ[J] in sp[CJ[J]] and tJ[J] - mins(CJ[J]) >= 2 and maxs(CJ[J]) - tJ[J] >= 2 for J in SUB): continue
                sl = sorted([(tJ[p] - mins(CJ[p]), 'lo', p) for p in PAIRS] + [(maxs(CJ[p]) - tJ[p], 'up', p) for p in PAIRS])
                ss = sorted([(t[i] - mins(C[i]), 'lo', i) for i in range(4)] + [(maxs(C[i]) - t[i], 'up', i) for i in range(4)])
                h2, h1 = sl[0][0], ss[0][0]
                if h2 <= h1 + 2:
                    cnt['a_n'] += 1
                    _, side, (X, Y) = sl[0]
                    Z, tt = (S, t) if side == 'lo' else (Rf, tuple(C[i] * M - t[i] for i in range(4)))
                    ok = pair_boundary_ok(Z, C, tt, X, Y, M, N, None); cnt['a_ok'] += ok
                    if not ok and len(ex) < 4: ex.append(('a', q, C, t, h1, h2))
                else:
                    cnt['b_n'] += 1
                    _, side1, A = ss[0]
                    Z1, t1 = (S, t) if side1 == 'lo' else (Rf, tuple(C[i] * M - t[i] for i in range(4)))
                    oth = [i for i in range(4) if i != A]; ok = False
                    for Aset in recipes(Z1, C[A], t1[A], None):
                        rem = tuple(x for x in Z1 if x not in Aset)
                        if (t1[oth[0]], t1[oth[1]]) in three_bin(rem, tuple(C[i] for i in oth)): ok = True; break
                    cnt['b_ok'] += ok
                    if not ok and len(ex) < 8: ex.append(('b', q, C, t, h1, h2))
    return cnt, ex

if __name__ == '__main__':
    for M in map(int, sys.argv[1:]):
        cnt, ex = run(M)
        print(M, '(a) h2 <= h1+2:', cnt['a_ok'], '/', cnt['a_n'], '  (b) h2 >= h1+3:', cnt['b_ok'], '/', cnt['b_n'], '  failures', ex, flush=True)
