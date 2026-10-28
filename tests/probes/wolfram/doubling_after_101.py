#!/usr/bin/env python3
"""Local, 2026-10-28 (L1064): check the hand lemma for the word 101 in the right-diagonal doubling sequence.

x_j = [Q_j > Q_(j-1)], Q_j = largest period among D_0..D_j. Claim: if Q_(j-1) = q and x_j x_(j+1) x_(j+2) = 101,
then x_(j+3) = (q/2 + E_q(D_(j-1))) mod 2, where E_q(d) = XOR of d(s) over even s in [0, q). Also checks the
mod-4 forcing form of E_q (q >= 4), tallies the corollary cases, and checks the cascade: after 10101 with q >= 8,
x_(j+3) = XOR of D_(j-3)(s) over s = 0, 1 (mod 4) in [0, q/2). Diagonals are built over exact periods from the
8.27 recurrence, as in doubling_coin.py. Usage: doubling_after_101.py SEEDS MAXLOG RNGSEED
"""
import sys, random
import numpy as np
NS, MAXLOG, R = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
random.seed(R)
def least(a):
    while len(a) > 1 and len(a) % 2 == 0 and np.array_equal(a[:len(a)//2], a[len(a)//2:]): a = a[:len(a)//2]
    return a
def diagonals(seed):
    prev2, prev1 = np.zeros(1, np.uint8), np.ones(1, np.uint8)
    Ds, Gs = [prev1], [None]; d = 0
    while True:
        d += 1
        q = max(len(prev1), len(prev2))
        g = np.tile(prev1, q // len(prev1)) | np.tile(prev2, q // len(prev2))
        s0 = seed[d] if d < len(seed) else 0
        D = (np.concatenate(([0], np.bitwise_xor.accumulate(g)[:-1])) ^ s0).astype(np.uint8)
        if g.sum() & 1: D = np.concatenate((D, 1 - D))
        D = least(D); Ds.append(D); Gs.append(g)
        if max(len(a) for a in Ds) > 2**MAXLOG: return Ds, Gs
        prev2, prev1 = prev1, D
def at(a, n): return np.tile(a, max(1, n // len(a)))[:n] if len(a) <= n else None
seen = set(); occ = ok = okmod4 = 0; cases = {}; cocc = cok = 0
for _ in range(NS):
    L = random.randint(0, 13); seed = tuple([1] + [random.randint(0, 1) for _ in range(L)])
    if seed in seen: continue
    seen.add(seed)
    Ds, Gs = diagonals(list(seed))
    Q = np.maximum.accumulate([len(a) for a in Ds]); x = [None] + [int(Q[j] > Q[j-1]) for j in range(1, len(Q))]
    for j in range(2, len(Q) - 3):
        if (x[j], x[j+1], x[j+2]) != (1, 0, 1): continue
        q = int(Q[j-1]); d = at(Ds[j-1], q)
        E = int(d[0::2].sum() & 1)
        pred = (q // 2 + E) & 1
        occ += 1; ok += pred == x[j+3]
        if q >= 4:
            g = Gs[j-1]; gq = at(g, q) if g is not None and len(g) <= q else None
            if gq is not None:
                s = np.arange(q); okmod4 += int(gq[(s % 4) < 2].sum() & 1) == E
            else: okmod4 += 1
        pd = len(Ds[j-1])
        kind = "q=2" if q == 2 else ("p(j-1)<=q/2" if pd <= q // 2 else ("doubled into q" if x[j-1] else "inherited q"))
        c = cases.setdefault(kind, [0, 0]); c[0] += 1; c[1] += x[j+3]
        if j >= 3 and q >= 8 and (x[j-2], x[j-1]) == (1, 0):
            f3 = at(Ds[j-3], q // 2); s3 = np.arange(q // 2)
            cocc += 1; cok += int(f3[(s3 % 4) < 2].sum() & 1) == x[j+3]
print(f"distinct seeds {len(seen)}, occurrences of 101: {occ}, lemma holds: {ok}, mod-4 form holds: {okmod4}")
for k, (n, o) in cases.items(): print(f"  {k:>15}: {n} occurrences, next doubles {o}")
print(f"cascade after 10101 (q >= 8): {cocc} occurrences, formula holds {cok}")
