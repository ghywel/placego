#!/usr/bin/env python3
"""Local, 2026-10-28 (L1064): is right-diagonal period doubling a fair coin outside the two proved forbidden words?

For random finite seeds (rightmost black at 0), builds each right diagonal over one exact period from the 8.27
recurrence D_d(t+1) = D_d(t) XOR (D_(d-1)(t) OR D_(d-2)(t)), D_d(0) = seed bit at -d, up to prefix period 2^MAXLOG.
Increment x_j = [Q_j > Q_(j-1)], Q_j = max period so far. After Q >= 4 it classifies each step by the model-M state
(e, 1, 11, 110, 1101) and counts doublings. Model M: 111 and 11011 forbidden (GC763, GC2007), otherwise a fair coin;
stationary doubling density 7/17. Usage: doubling_coin.py SEEDS MAXLOG RNGSEED [QMIN]   (count only steps whose base Q_(j-1) >= QMIN; default 4)
"""
import sys, random
import numpy as np
NS, MAXLOG, R = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
QMIN = int(sys.argv[4]) if len(sys.argv) > 4 else 4
random.seed(R)
def least(a):
    while len(a) > 1 and len(a) % 2 == 0 and np.array_equal(a[:len(a)//2], a[len(a)//2:]): a = a[:len(a)//2]
    return a
def word(seed):
    prev2, prev1 = np.zeros(1, np.uint8), np.ones(1, np.uint8)
    Q = [1]; d = 0
    while True:
        d += 1
        q = max(len(prev1), len(prev2))
        g = np.tile(prev1, q // len(prev1)) | np.tile(prev2, q // len(prev2))
        s0 = seed[d] if d < len(seed) else 0
        D = (np.concatenate(([0], np.bitwise_xor.accumulate(g)[:-1])) ^ s0).astype(np.uint8)
        if g.sum() & 1: D = np.concatenate((D, 1 - D))
        D = least(D)
        Q.append(max(Q[-1], len(D)))
        if Q[-1] > 2**MAXLOG: return Q
        prev2, prev1 = prev1, D
def state(h):
    if h.endswith("1101"): return "1101"
    if h.endswith("11"): return "11"
    if h.endswith("110"): return "110"
    if h.endswith("1"): return "1"
    return "e"
tally = {k: [0, 0] for k in ("e", "1", "11", "110", "1101")}
ones = steps = 0; lengths = []
for _ in range(NS):
    L = random.randint(0, 11); seed = [1] + [random.randint(0, 1) for _ in range(L)]
    Q = word(seed); h = ""
    for j in range(1, len(Q)):
        b = int(Q[j] > Q[j-1])
        if Q[j-1] >= QMIN and len(h) >= 4:
            st = state(h); tally[st][0] += 1; tally[st][1] += b; ones += b; steps += 1
        h += str(b)
    lengths.append(len(Q))
print(f"seeds {NS}, MAXLOG {MAXLOG}, QMIN {QMIN}, steps {steps}, density {ones/steps:.4f} (7/17 = {7/17:.4f})")
for k, (n, o) in tally.items():
    print(f"  state {k:>4}: {n:6d} steps, P(double) = {o/max(n,1):.4f}")
