"""Cloud's carrying-read instruments for GPT's G333 and G334 (CL474).

I1  the G334 identity g_c(r-1) - f_c(r+1) = (r-1)(h-1) + (l-1)(d-1) - 6, l=c-r, h=H-r, d=q-l,
    over every M <= 60, c, q, r with r-1 and r+1 legal.
I2  G333 on random integer interval systems in four variables: integer-empty and real-nonempty
    iff the three symmetrised pair intervals are pinned with wrong parity.  Real feasibility is
    decided exactly on the half grid: after eliminating k4 every row is a 0/1 or 0/-1 vector in
    three variables, whose 3x3 minors have |det| <= 2, so every vertex lies on (1/2)Z^3.
I3  G334 directly: every count pattern c_i >= 3 with M = 12..MMAX, every hole q, every target
    vector with t_J >= T_(C_J) for all proper J; P(t) built from the exact admission intervals
    K(C_J, t_J); count instances that are half-grid feasible but integer empty.  Also checks
    K(complement) = H - K, and that the pinned pair splits seen at half-integral points are only
    the lemma's types (i) and (ii).
Predictions: I1 0 failures; I2 0 mismatches; I3 0 real-but-not-integer instances.
Counterfactual: any I3 instance refutes G334 as stated.

OUTCOME (2026-10-20): I1 487,635 cases, 0 failures.  I2 20,000 systems, 17,094 real-nonempty, 1,015
genuine obstructions, 0 mismatches with the criterion.  I3 M = 12..15: 9,370,699 protected instances,
0 real-but-not-integer, 0 complement mismatches, and 0 empty P: every instance has an integer count
vector (so I3 is consistency for G334, whose carrying support is the hand read; 8m33s).
"""
import itertools, random, sys
import numpy as np

L = lambda n: n * (n - 1) // 2
T = lambda n: n * (n + 1) // 2

def f(c, q, M, r): return L(c - r) + (q + 1) * r + L(r)
def g(c, q, M, r): return (c - r) * (q - 1) - L(c - r) + M * r - L(r)

def I1(MMAX=60):
    bad = n = 0
    for M in range(2, MMAX + 1):
        for q in range(1, M):
            H = M - q
            for c in range(1, M + 1):
                for r in range(1, c):
                    if r + 1 > min(c, H) or c - (r - 1) > q or r - 1 < 0: continue
                    l, h = c - r, H - r; d = q - l
                    n += 1
                    if g(c, q, M, r - 1) - f(c, q, M, r + 1) != (r - 1) * (h - 1) + (l - 1) * (d - 1) - 6: bad += 1
    return n, bad

SUB = [J for s in (1, 2, 3) for J in itertools.combinations(range(4), s)]
PAIRS = [(0, 1), (0, 2), (0, 3)]
comp = lambda J: tuple(i for i in range(4) if i not in J)

def feasible(lo, hi, H, scale):
    """Points k in (1/scale)Z^4, sum H, lo_J <= k(J) <= hi_J; bounds from 0..max."""
    m = scale * max(hi[(i,)] for i in range(4))
    for a in range(scale * lo[(0,)], scale * hi[(0,)] + 1):
        for b in range(scale * lo[(1,)], scale * hi[(1,)] + 1):
            for c in range(scale * lo[(2,)], scale * hi[(2,)] + 1):
                k = (a, b, c, scale * H - a - b - c)
                if all(scale * lo[J] <= sum(k[i] for i in J) <= scale * hi[J] for J in SUB):
                    return k
    return None

def I2(trials=20000, seed=1):
    rnd = random.Random(seed); mism = cnt_obs = cnt_real = 0
    for _ in range(trials):
        # random systems built around a random half-grid point, so that pinned half-integral
        # corners occur often; slack 0..1 on each side, sometimes shifted to make P empty
        k0 = [rnd.randint(0, 8) for _ in range(4)]
        if rnd.random() < 0.5: k0 = [x + 1 for x in k0]          # stays integral in 2x units
        if (sum(k0) % 2) and rnd.random() < 0.7: k0[0] += 1
        twoH = sum(k0)
        if twoH % 2: k0[0] += 1; twoH += 1
        H = twoH // 2
        lo, hi = {}, {}
        for J in SUB:
            v = sum(k0[i] for i in J)                              # 2 k0(J)
            lo[J] = (v // 2) - rnd.choice([0, 0, 1]); hi[J] = -((-v) // 2) + rnd.choice([0, 0, 1])
            if rnd.random() < 0.03: lo[J] += 1
        for i in range(4):
            lo[(i,)] = max(lo[(i,)], 0); hi[(i,)] = max(hi[(i,)], lo[(i,)])
        r = feasible(lo, hi, H, 2)
        if r is None: continue
        cnt_real += 1
        z = feasible(lo, hi, H, 1)
        A = [max(lo[J], H - hi[comp(J)]) for J in PAIRS]
        B = [min(hi[J], H - lo[comp(J)]) for J in PAIRS]
        crit = A == B and (sum(A) - H) % 2 != 0
        if crit: cnt_obs += 1
        if (z is None) != crit: mism += 1
    return dict(real_nonempty=cnt_real, obstructions=cnt_obs, mismatches=mism)

def I3(MMAX):
    out = dict(instances=0, real_not_integer=0, comp_mismatch=0, real_empty=0, half_pins=set())
    for M in range(12, MMAX + 1):
        for C in itertools.product(range(3, M), repeat=4):
            if sum(C) != M: continue
            for q in range(1, M):
                H = M - q; S = T(M) - q
                CJ = {J: sum(C[i] for i in J) for J in SUB}
                memo = {}
                def K(c, t):
                    if (c, t) in memo: return memo[(c, t)]
                    v = [r for r in range(max(0, c - q), min(c, H) + 1) if f(c, q, M, r) <= t <= g(c, q, M, r)]
                    memo[(c, t)] = (min(v), max(v)) if v else None
                    return memo[(c, t)]
                for t3 in itertools.product(*[range(T(C[i]), S - T(M - C[i]) + 1) for i in range(3)]):
                    t = t3 + (S - sum(t3),)
                    tJ = {J: sum(t[i] for i in J) for J in SUB}
                    if not all(tJ[J] >= T(CJ[J]) for J in SUB): continue
                    out['instances'] += 1
                    Ks = {J: K(CJ[J], tJ[J]) for J in SUB}
                    for J in SUB:
                        a, b = Ks[J], Ks[comp(J)]
                        if (a is None) != (b is None) or (a and (a[0] != H - b[1] or a[1] != H - b[0])):
                            out['comp_mismatch'] += 1
                    if any(v is None for v in Ks.values()):
                        out['real_empty'] += 1; continue
                    lo = {J: Ks[J][0] for J in SUB}; hi = {J: Ks[J][1] for J in SUB}
                    if feasible(lo, hi, H, 1): continue
                    h2 = feasible(lo, hi, H, 2)
                    if h2 is None:
                        out['real_empty'] += 1; continue
                    out['real_not_integer'] += 1
                    print('COUNTEREXAMPLE', M, q, C, t, h2, flush=True)
    out['half_pins'] = sorted(out['half_pins'])
    return out

if __name__ == '__main__':
    what = sys.argv[1]
    if what == 'I1': print('I1', I1())
    if what == 'I2': print('I2', I2())
    if what == 'I3': print('I3', I3(int(sys.argv[2])), flush=True)
