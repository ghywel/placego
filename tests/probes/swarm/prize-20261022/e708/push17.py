#!/usr/bin/env python3
"""Addendum: can the threshold 16 be pushed to 17?  For |H| = 17 the crude Hall bound (union >= max t_a) can fail
only for S = H with every t_a < 17, i.e. H = C_M := {a heavy, all prime powers < 17, a <= M < 17 w_a} when
|C_M| = 17 (stab.py: max |C_M| = 17).  For each such set, compute the exact minimum over ALL interval positions of
|union of multiples of w_a in a window of length M|, at the worst (smallest) M = max(S).  If >= 17 always, Hall holds
for |H| = 17 and Theorem 2 gives g(A,I) <= 2n whenever |H| <= 17."""
import sys, time, math
import numpy as np
T0 = time.time(); TL = 400
i = 17
def primes_upto(n):
    return [p for p in range(2, n + 1) if all(p % q for q in range(2, int(p ** .5) + 1))]
ps = primes_upto(i - 1)
opts = []
for p in ps:
    pw, q = [], p
    while q < i:
        pw.append(q); q *= p
    opts.append(pw)
cands = []
def dfs(k, a, Q, om):
    if k == len(ps):
        if om >= 3:
            w = a // Q
            if a <= i * w - 1:
                cands.append((a, w))
        return
    dfs(k + 1, a, Q, om)
    for q in opts[k]:
        dfs(k + 1, a * q, max(Q, q), om + 1)
dfs(0, 1, 1, 0)
# endpoints where C_M can change
pts = sorted({a for a, w in cands} | {i * w for a, w in cands})
sets = {}
for M in pts:
    C = tuple(sorted((a, w) for a, w in cands if a <= M <= i * w - 1))
    if len(C) >= i:
        sets.setdefault(C, M)
print('distinct candidate sets with |C_M| >= 17:', len(sets), ' sizes:', sorted({len(C) for C in sets}), flush=True)
worst_overall = None
for C, M0 in sets.items():
    if len(C) > i:
        print('  |C|>17 case (needs subset check):', len(C), flush=True); continue
    M = max(a for a, w in C)  # smallest admissible window
    assert all(M <= i * w - 1 for a, w in C)
    W = sorted({w for a, w in C})
    L = 1
    for w in W:
        L = L * w // math.gcd(L, w)
    if L > 3 * 10 ** 7:
        print('  period too large', L, flush=True); continue
    ind = np.zeros(L + M, dtype=np.int8)
    for w in W:
        ind[::w] = 1
    cs = np.concatenate(([0], np.cumsum(ind, dtype=np.int64)))
    win = cs[M:L + M] - cs[0:L]
    mn = int(win.min()); arg = int(win.argmin())
    print('  set a=%s  M=%d  distinct w=%d  period=%d  min union over positions=%d (start %d)  need >= 17 -> %s' %
          ([a for a, w in C], M, len(W), L, mn, arg, 'OK' if mn >= i else 'FAIL'), flush=True)
    worst_overall = mn if worst_overall is None else min(worst_overall, mn)
    if time.time() - T0 > TL:
        print('TIMEOUT'); break
print('worst min union =', worst_overall, ' t=%.0fs' % (time.time() - T0), flush=True)
