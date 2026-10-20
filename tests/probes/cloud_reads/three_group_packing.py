"""CL475 bounded test: a three-group packing statement behind core rows 7-9.

Domain: M = 12, all sizes 3 (bins a, c, d; the remainder b is free), every hole q, targets with the
baseline cut t_J >= T(C_J) for J inside {a, c, d} and nonempty K for each single and union group.
Question: are there always three disjoint subsets of [0, M] minus {q} realising (3, t_a), (3, t_c),
(3, t_d)?  If yes, rows 7-9 (each written on three labels) would follow from such a packing theorem.
Prediction: packing fails somewhere (dropping b's cuts is too generous).  Counterfactual: no failure.

OUTCOME: 125,177 instances, 3 with no packing, all permutations of q6, targets 18/18/32 with remainder
target 4 < T_3 = 6.  Every failure violates the remainder's own singleton cut.
"""
import itertools
L = lambda n: n * (n - 1) // 2
T = lambda n: n * (n + 1) // 2
M = 12; c = 3
fails = n = 0; ex = []
for q in range(1, M):
    pool = [x for x in range(M + 1) if x != q]; S = sum(pool); H = M - q
    def K(cc, t):
        v = [r for r in range(max(0, cc - q), min(cc, H) + 1)
             if L(cc - r) + (q + 1) * r + L(r) <= t <= (cc - r) * (q - 1) - L(cc - r) + M * r - L(r)]
        return bool(v)
    trip = set()
    for A in itertools.combinations(pool, 3):
        r1 = [x for x in pool if x not in A]
        for C in itertools.combinations(r1, 3):
            r2 = [x for x in r1 if x not in C]
            sa, sc = sum(A), sum(C)
            for D in itertools.combinations(r2, 3):
                trip.add((sa, sc, sum(D)))
    for ta in range(T(3), S):
        for tc in range(T(3), S):
            for td in range(T(3), S - ta - tc + 1):
                if min(ta + tc, ta + td, tc + td) < T(6) or ta + tc + td < T(9): continue
                if ta + tc + td > S - L(3): continue          # leaves room for a 3-token remainder
                if not all(K(cc, t) for cc, t in ((3, ta), (3, tc), (3, td), (6, ta + tc), (6, ta + td),
                                                  (6, tc + td), (9, ta + tc + td))): continue
                n += 1
                if (ta, tc, td) not in trip:
                    fails += 1
                    if len(ex) < 5: ex.append((q, ta, tc, td, S - ta - tc - td))
print('instances', n, 'no packing', fails, ex)
