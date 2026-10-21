"""CL500: does the pair-first selector (least pair's boundary: rank staircase / value staircase / prefix-plus-pair;
else least singleton's G315 recipe with repairs + three-bin completion) complete FEASIBLE two-hole four-bin instances?
Domain: [0, M] minus {q1, q2}, sizes 3333 (M = 13), all 14 group targets in their spectra, least margin >= 2, and
actually feasible (checked against the enumerated feasible set).
Prediction (written first): >= 99% complete; misses are equal-target instances.  Counterfactual: a large miss rate
means the selector is a one-hole phenomenon.

OUTCOME (M = 13, 3333, 93 s): 954,454 feasible instances; pair boundary 896,298; recipe 55,086; miss 3,070 (982
with repeated targets), concentrated at ADJACENT holes.  With displacement-2 repairs (twohole_selector_d2.py):
miss 694 (99.93% complete), 334 with repeated targets.  Prediction: >= 99% held; "misses are equal-target" failed.
"""
import itertools, sys
from collections import Counter
_a = sys.argv; sys.argv = ['x']
exec(open('tests/probes/cloud_reads/singleton_or_pair.py').read().rsplit("\nif __name__ == '__main__':", 1)[0])
exec(open('tests/probes/cloud_reads/twohole_fourbin.py').read().rsplit("\nif __name__ == '__main__':", 1)[0].split("SUB = [J")[0])
sys.argv = _a
from itertools import combinations

def feas_set(pool, C):
    a, b, c, d = C; out = set()
    for A in combinations(pool, a):
        sA = sum(A); r1 = [x for x in pool if x not in A]
        for B in combinations(r1, b):
            sB = sum(B); r2 = [x for x in r1 if x not in B]
            for Cc in combinations(r2, c): out.add((sA, sB, sum(Cc)))
    return out

def run(M, C):
    cnt = Counter(); ex = []
    CJ = {J: sum(C[i] for i in J) for J in SUB}
    for q1 in range(1, M):
        for q2 in range(q1 + 1, M):
            S = [x for x in range(M + 1) if x not in (q1, q2)]; tot = sum(S); N = len(S)
            if N != sum(C): continue
            sp = spectra(S); F = feas_set(S, C); mins = lambda c: sum(S[:c]); maxs = lambda c: sum(S[N - c:])
            Rf = [M - x for x in reversed(S)]
            for t3 in itertools.product(*[range(mins(C[i]), maxs(C[i]) + 1) for i in range(3)]):
                t = t3 + (tot - sum(t3),)
                tJ = {J: sum(t[i] for i in J) for J in SUB}
                if not all(tJ[J] in sp[CJ[J]] and tJ[J] - mins(CJ[J]) >= 2 and maxs(CJ[J]) - tJ[J] >= 2 for J in SUB): continue
                if t3 not in F: continue
                cnt['n'] += 1
                sl = sorted([(tJ[p] - mins(CJ[p]), 'lo', p) for p in PAIRS] + [(maxs(CJ[p]) - tJ[p], 'up', p) for p in PAIRS])
                ss = sorted([(t[i] - mins(C[i]), 'lo', i) for i in range(4)] + [(maxs(C[i]) - t[i], 'up', i) for i in range(4)])
                _, side, (X, Y) = sl[0]
                Z, tt = (S, t) if side == 'lo' else (Rf, tuple(C[i] * M - t[i] for i in range(4)))
                if pair_boundary_ok(Z, C, tt, X, Y, M, N, None): cnt['pair'] += 1; continue
                _, side1, A = ss[0]
                Z1, t1 = (S, t) if side1 == 'lo' else (Rf, tuple(C[i] * M - t[i] for i in range(4)))
                oth = [i for i in range(4) if i != A]; ok = False
                for Aset in recipes(Z1, C[A], t1[A], None):
                    rem = tuple(x for x in Z1 if x not in Aset)
                    if (t1[oth[0]], t1[oth[1]]) in three_bin(rem, tuple(C[i] for i in oth)): ok = True; break
                cnt['single'] += ok
                if not ok:
                    cnt['miss'] += 1
                    rep = any(t[i] == t[j] and C[i] == C[j] for i in range(4) for j in range(i + 1, 4))
                    cnt['miss_repeat'] += rep
                    if len(ex) < 6: ex.append(((q1, q2), t, rep))
    return cnt, ex

if __name__ == '__main__':
    M = int(sys.argv[1]); C = tuple(map(int, sys.argv[2].split(',')))
    cnt, ex = run(M, C)
    print(M, C, dict(cnt), ex, flush=True)
