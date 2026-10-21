"""CL500: four bins of sizes >= 3 on a TWO-hole pool [0, M] minus {q1 < q2}: which spectrum-feasible instances are
infeasible, and at what least group margin?  (The next rung of eight streets' crossing-off after P0's one hole.)

Exact: every partition enumerated per pool (sum vectors cached); spectrum feasibility of all 14 groups by DP.
Prediction (written first): exceptions exist, all at least margin <= 2, and they are cores (equal-split six-value
pools beside pinned bins), more families than one hole's single F(s, M).  Counterfactual: an exception at margin
>= 3 would mean two holes need more than scalar margins.

OUTCOME: M = 13, 3333: 1,335,898 spectrum-feasible, infeasible by least margin 0: 432, 1: 1,092, 2: 408, 3: 84,
4: 6 (19.6 s).  M = 14, 3334: 2,369,944; 0: 216, 1: 792, 2: 312, 3: 60.  Prediction FAILED (margins reach 4):
every exception at margin >= 3 has a repeated (size, target), i.e. it is the equal-shares wall of the eightstreets
page, section 9 (twohole_fourbin_deep.py).
"""
import itertools, sys
from collections import Counter
SUB = [J for s in (1, 2, 3) for J in itertools.combinations(range(4), s)]

def spectra(pool):
    sp = [set() for _ in range(len(pool) + 1)]; sp[0].add(0)
    for x in pool:
        for k in range(len(pool) - 1, -1, -1):
            if sp[k]: sp[k + 1] |= {s + x for s in sp[k]}
    return sp

def feasible_set(pool, C):
    a, b, c, d = C; out = set()
    for A in itertools.combinations(pool, a):
        sA = sum(A); r1 = [x for x in pool if x not in A]
        for B in itertools.combinations(r1, b):
            sB = sum(B); r2 = [x for x in r1 if x not in B]
            for Cc in itertools.combinations(r2, c):
                out.add((sA, sB, sum(Cc)))
    return out

def run(M, C):
    cnt = Counter(); exc = []
    for q1 in range(1, M):
        for q2 in range(q1 + 1, M):
            pool = [x for x in range(M + 1) if x not in (q1, q2)]; tot = sum(pool); n = len(pool)
            if n != sum(C): continue
            sp = spectra(pool); F = feasible_set(pool, C)
            mins = lambda c: sum(pool[:c]); maxs = lambda c: sum(pool[n - c:])
            CJ = {J: sum(C[i] for i in J) for J in SUB}
            for t3 in itertools.product(*[range(mins(C[i]), maxs(C[i]) + 1) for i in range(3)]):
                t = t3 + (tot - sum(t3),)
                tJ = {J: sum(t[i] for i in J) for J in SUB}
                if not all(tJ[J] in sp[CJ[J]] for J in SUB): continue
                cnt['spec'] += 1
                if t3 in F: continue
                m = min(min(tJ[J] - mins(CJ[J]), maxs(CJ[J]) - tJ[J]) for J in SUB)
                cnt[('inf', m)] += 1
                exc.append(((q1, q2), t, m))
    return cnt, exc

if __name__ == '__main__':
    M = int(sys.argv[1])
    for C in sorted({tuple(sorted(c)) for c in itertools.product(range(3, M), repeat=4) if sum(c) == M - 1}):
        cnt, exc = run(M, C)
        seen = set(); canon = []
        for (h, t, m) in exc:
            key = (h, tuple(sorted(zip(C, t))))
            if key in seen: continue
            seen.add(key); canon.append((h, sorted(zip(C, t)), m))
        print(M, C, 'spectrum-feasible', cnt['spec'], 'infeasible by least margin', sorted((k[1], v) for k, v in cnt.items() if isinstance(k, tuple)), flush=True)
        for row in canon[:40]: print('   ', row)
