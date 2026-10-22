#!/usr/bin/env python3
"""Addendum: largest h such that the host step of Theorem 2 (Hall for blocks w_a = a/Q(a)) holds whenever |H| <= h.
For each size s >= 17: a subset S (|S| = s) can fail the crude bound only if every a in S has t_a < s, i.e.
S is inside C_{M,s} = {a heavy, prime powers < s, a <= M < s*w_a}.  For each distinct C_{M,s} with |C| >= s we
lower-bound the union over every s-subset: such a subset uses a block set W' with sum of class sizes >= s;
the union is monotone in W', so we take the exact minimum over positions (sliding window, window length = the
smallest M giving this C) over all minimal such W'.  Stop at the first s where a bound falls below s."""
import sys, time, math, itertools
import numpy as np
T0 = time.time(); TL = 330
def primes_upto(n):
    return [p for p in range(2, n + 1) if all(p % q for q in range(2, int(p ** .5) + 1))]
cache = {}
def minunion(W, M):
    key = (W, M)
    if key in cache:
        return cache[key]
    L = 1
    for w in W:
        L = L * w // math.gcd(L, w)
    if L > 2 * 10 ** 7:
        return None
    ind = np.zeros(L + M, dtype=np.int8)
    for w in W:
        ind[::w] = 1
    cs = np.concatenate(([0], np.cumsum(ind, dtype=np.int64)))
    v = int((cs[M:L + M] - cs[0:L]).min())
    cache[key] = v
    return v
def check_s(s):
    ps = primes_upto(s - 1); opts = []
    for p in ps:
        pw, q = [], p
        while q < s:
            pw.append(q); q *= p
        opts.append(pw)
    cands = []
    def dfs(k, a, Q, om):
        if k == len(ps):
            if om >= 3 and a <= s * (a // Q) - 1:
                cands.append((a, a // Q))
            return
        dfs(k + 1, a, Q, om)
        for q in opts[k]:
            dfs(k + 1, a * q, max(Q, q), om + 1)
    dfs(0, 1, 1, 0)
    pts = sorted({a for a, w in cands} | {s * w for a, w in cands})
    sets = {}
    for M in pts:
        C = tuple(sorted((a, w) for a, w in cands if a <= M <= s * w - 1))
        if len(C) >= s:
            sets.setdefault(C, M)
    worst = None
    for C, Mlo in sets.items():
        cls = {}
        for a, w in C:
            cls[w] = cls.get(w, 0) + 1
        Ws = sorted(cls)
        if len(Ws) > 18:
            return None, 'too many blocks %d' % len(Ws)
        for r in range(1, len(Ws) + 1):
            for Wp in itertools.combinations(Ws, r):
                tot = sum(cls[w] for w in Wp)
                if tot < s or any(tot - cls[w] >= s for w in Wp):
                    continue  # not enough elements, or not minimal
                v = minunion(Wp, Mlo)
                if v is None:
                    return None, 'period too large'
                worst = v if worst is None else min(worst, v)
                if v < s:
                    return worst, 'FAIL C=%s M=%d W=%s union=%d' % ([a for a, w in C], Mlo, Wp, v)
            if time.time() - T0 > TL:
                raise TimeoutError
    return worst, 'ok (%d candidate sets)' % len(sets)
s = 17
try:
    while True:
        worst, msg = check_s(s)
        print('s=%d  worst min union=%s  %s  t=%.0fs' % (s, worst, msg, time.time() - T0), flush=True)
        if not msg.startswith('ok'):
            break
        s += 1
except TimeoutError:
    print('TIMEOUT during s=%d' % s, flush=True)
print('host step verified for all |H| <= %d' % (s - 1), flush=True)
