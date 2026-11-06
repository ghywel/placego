#!/usr/bin/env python3
"""Block 5: the second check, and low-degree invariants on survivors.

Part A, the conditioned checks. For even W, r_j = S_W(t0 + 2 j + 2) / S_W(t0 + 2 j) in rows and rho_j the same in classes,
for the first three composite checks. Prediction (0.8): rho_2 stays within 3 binomial sigma of 1/2 at W >= 24, and no
exact law appears. Counterfactual: a closed form or a persistent bias, which would be a fresh handle on the second check.

Part B, degree 3. Survivors at tick t, coordinates the first m bits of the row at t past the black wall cell. Is there a nonzero
polynomial over F_2 of degree at most 3 vanishing on all survivors? Rank of the evaluation matrix on at least 3 times as
many survivors as monomials. Prediction (0.85): full rank at every (W, t) tested, so no degree-3 invariant.
Counterfactual: a rank deficit, a hidden invariant a proof could use.
Power control: remove the survivors with z4 z5 z6 + z7 = 1, and the rank must fall by at least one.
"""
import itertools, math, random, sys
import numpy as np
sys.path.insert(0, sys.argv[1])
from class_tables_lib import step, lanes, one
def survivors_at(W, ts):
    rule = 30
    R = lanes(rule, W)
    t0 = W - 2
    lo = R; hi = np.zeros_like(lo); t = 0; out = {}
    while t <= max(ts):
        if t % 2 == 0 and t >= t0:
            al = (lo & one) == 1
            lo, hi = lo[al], hi[al]
            if t in ts: out[t] = (lo.copy(), hi.copy())
        lo, hi = step(rule, lo, hi); t += 1
    return out
def distinct_idx(lo, hi):
    o = np.lexsort((hi, lo)); l, h = lo[o], hi[o]
    b = np.concatenate([[True], (l[1:] != l[:-1]) | (h[1:] != h[:-1])])
    return o[b]
print('Part A: W, S at t0, then ratios in rows and classes for checks 1..3, z of the class ratio')
for W in range(24, 45, 4):
    t0 = W - 2
    sv = survivors_at(W, set(range(t0, t0 + 10, 2)))
    S = [sv[t][0].size for t in sorted(sv)]
    Q = [distinct_idx(*sv[t]).size for t in sorted(sv)]
    line = []
    for j in range(3):
        r = S[j + 1] / S[j]; q = Q[j + 1] / Q[j]; z = (q - .5) * 2 * math.sqrt(Q[j])
        line.append('r %.4f rho %.4f z %+.2f' % (r, q, z))
    print(W, S[0], ' | '.join(line), flush=True)
def rank_deg3(rows, m, deg=3):
    mons = [c for d in range(0, deg + 1) for c in itertools.combinations(range(m), d)]
    basis = {}
    for r in rows:
        bits = [(r >> i) & 1 for i in range(m)]
        v = 0
        for idx, c in enumerate(mons):
            x = 1
            for i in c:
                x &= bits[i]
                if not x: break
            if x: v |= 1 << idx
        while v:
            h = v.bit_length() - 1
            if h in basis: v ^= basis[h]
            else: basis[h] = v; break
    return len(basis), len(mons)
print('Part B: W t m survivors-used rank monomials; planted control')
random.seed(1)
m = 22
for W, ks in ((32, (0, 1, 3)), (40, (0, 2, 5))):
    t0 = W - 2
    ts = [t0 + 2 * k for k in ks]
    sv = survivors_at(W, set(ts))
    for t in ts:
        lo, hi = sv[t]
        ix = distinct_idx(lo, hi)
        rows = [int(x) >> 1 for x in lo[ix]]
        rows = list(dict.fromkeys(rows))
        random.shuffle(rows)
        M = sum(math.comb(m, d) for d in range(4))
        use = rows[:3 * M]
        rk, mon = rank_deg3(use, m)
        pl = [r for r in use if (((r >> 3) & (r >> 4) & (r >> 5) & 1) ^ ((r >> 6) & 1)) == 0]
        rk2, _ = rank_deg3(pl, m)
        print(W, t, m, len(use), rk, mon, 'planted', len(pl), rk2, flush=True)
