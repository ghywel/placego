"""CL478: three bins, sizes >= 3, on a TWO-hole pool [0, M] minus {q1 < q2} (holes internal).

Question: is scalar spectrum feasibility of all six proper groups sufficient for a partition, and if not, what
are the exceptions?  This is the base case that a one-hole four-bin proof on the G316 skeleton needs (the
least-slack bin's prefix/suffix/pivot set leaves a two-hole remainder for three bins).
Output: every spectrum-feasible infeasible instance, canonical up to bin order and reflection, with the least
group margin.  Prediction: exceptions exist and are the {0,2,3,5,6,8}+s equal-split core plus pinned bins,
with margin <= 1 only.  Counterfactual: exceptions at margin >= 2 would mean the four-bin margin alone cannot
drive this base.

OUTCOME (M = 10..17, 2m54s for 15..17): spectrum-feasible 14,160 / 25,080 / 83,868 / 203,384 / 412,678 /
771,315 / 1,577,709 / 2,542,622; infeasible 54 / 18 / 24 / 24 / 30 / 30 / 36 / 36.  Least margins 1..3 from
M = 11 on (18 at margin 4 at M = 10 only).  Prediction FAILED on the margin: exceptions reach margin 3.
The families (canonical, holes (q1,q2), (size,target)) are stable from M = 16: two kinds.
(i) equal-split cores: holes (1,4) sizes 3,3 targets 12,12 on {0,2,3,5,6,8}; holes (2,6) 11,11 on
    {0,1,3,4,5,9}; holes (5,6) 10,10 on {0,1,2,3,4,10}; each with the third bin pinned near its maximum.
(ii) forced collisions: a bin with a unique realising set that meets every realising set of another bin,
    e.g. holes (2,3) (3,8),(3,16),(k,max-1); (7,8) (3,4),(3,14),(k,max-2); (3,4) (3,19),(4,11),(k,max-1).M = 18 (background, ~8 min): 4,407,030 / 42 / 17 families; the predicted clump exception at holes (9,10),
sizes (3,5,9), targets (20,11,121) appeared (printed reflected as holes (8,9), (34,79,41)); the distance-6
chain gained (6,12) (3,27),(7,24),(7,102).  Prediction held (bin size corrected from 10 to 9).
"""
import itertools, sys
from collections import Counter

def spectra(pool):
    sp = [set() for _ in range(len(pool) + 1)]; sp[0].add(0)
    for x in pool:
        for k in range(len(pool) - 1, -1, -1):
            if sp[k]: sp[k + 1] |= {s + x for s in sp[k]}
    return sp

def run(M, out):
    tot = Counter(); exc = []
    for q1 in range(1, M):
        for q2 in range(q1 + 1, M):
            pool = [x for x in range(M + 1) if x not in (q1, q2)]; S = sum(pool); n = len(pool)
            sp = spectra(pool)
            mins = lambda c: sum(pool[:c]); maxs = lambda c: sum(pool[n - c:])
            for a in range(3, n - 5):
                for b in range(3, n - a - 2):
                    c = n - a - b
                    if c < 3 or not (a <= b <= c): continue
                    feas = set()
                    for A in itertools.combinations(pool, a):
                        sA = sum(A); r1 = [x for x in pool if x not in A]
                        for B in itertools.combinations(r1, b):
                            feas.add((sA, sum(B)))
                    for sA in range(mins(a), maxs(a) + 1):
                        if sA not in sp[a]: continue
                        for sB in range(mins(b), maxs(b) + 1):
                            sC = S - sA - sB
                            if sB not in sp[b] or sC not in sp[c] or sA + sB not in sp[a + b] or sA + sC not in sp[a + c] or sB + sC not in sp[b + c]: continue
                            tot['spec'] += 1
                            if (sA, sB) in feas: continue
                            tot['inf'] += 1
                            m = min(min(v - mins(k), maxs(k) - v) for k, v in ((a, sA), (b, sB), (c, sC), (a + b, sA + sB), (a + c, sA + sC), (b + c, sB + sC)))
                            tot[('margin', m)] += 1
                            exc.append((M, (q1, q2), (a, b, c), (sA, sB, sC), m))
    print(M, dict(tot), file=out, flush=True)
    # canonical listing: reflect so that q1 + q2 <= M
    seen = set()
    for M_, (q1, q2), sz, t, m in exc:
        key1 = ((q1, q2), tuple(sorted(zip(sz, t))))
        key2 = ((M_ - q2, M_ - q1), tuple(sorted(zip(sz, tuple(s * M_ - v for s, v in zip(sz, t))))))
        key = min(key1, key2)
        if key in seen: continue
        seen.add(key); print('  ', M_, 'holes', key[0], 'sizes/targets', key[1], 'least margin', m, file=out, flush=True)

if __name__ == '__main__':
    for M in map(int, sys.argv[1:]):
        run(M, sys.stdout)
