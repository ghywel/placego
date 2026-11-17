#!/usr/bin/env python3
"""L1311 T34 part 1 (Local, 2026-11-02): the mismatch front of a black-edge row against the phase G16.
reports/rule30-genealogy.md section 39 (predictions written first). Run: python3 tests/probes/front_g16.py [N] [K] [T]

E = G16 two-sided in the edge frame: E_n(t) = column (n + a) mod 128 of G16's 128-cell ring at time (t + q) mod 16, for an
alignment (a, q). A row X has random bits at depths 0..K and E's bits below (a clean tail); it evolves by the edge map
Phi(x) = x ^ ((x << 1) | (x << 2) | 3) (black edge above depth 0). The mismatch D(t) = Phi^t(X) xor E(t) has its deepest 1
at R(t), the front. Reported: mean speed R(T)/T, retreats (R(t+1) < R(t)) after time 1, the longest stall (ticks
without a new maximum of R), and the slowest run.
"""
import os
import random
import sys
import runpy
here = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(here, 'upward_rigid.py'), run_name='lib')
p, cols, _ = g['phases']()['G16']; NC = len(cols)            # p = 16, 128 columns
N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
K = int(sys.argv[2]) if len(sys.argv) > 2 else 40
T = int(sys.argv[3]) if len(sys.argv) > 3 else 300
DEPTH = K + 2 * T + 8; MASK = (1 << DEPTH) - 1
rng = random.Random(34)


def erow(a, q, t):
    tt = (t + q) % p
    return sum(((cols[(n + a) % NC] >> tt) & 1) << n for n in range(DEPTH))


speeds = []; retreat_runs = 0; retreats_total = 0; stall_max = 0; slow = None
for it in range(N):
    a, q = rng.randrange(NC), rng.randrange(p)
    E = [erow(a, q, t) for t in range(p)]
    x = (rng.getrandbits(K + 1)) | (E[0] >> (K + 1) << (K + 1))
    R = []; best = -1; stall = 0; rets = 0
    for t in range(T + 1):
        d = (x ^ E[t % p]) & MASK
        r = d.bit_length() - 1
        R.append(r)
        if t >= 2 and r < R[-2]:
            rets += 1
        if r > best:
            best = r; stall = 0
        else:
            stall += 1
            stall_max = max(stall_max, stall)
        x = (x ^ ((x << 1) | (x << 2) | 3)) & MASK
    v = R[-1] / T; speeds.append(v)
    retreats_total += rets; retreat_runs += rets > 0
    if slow is None or v < slow[0]:
        slow = (v, a, q, R[:40])
speeds.sort()
print('G16 fronts: %d runs, prefix depth K = %d, %d ticks' % (N, K, T))
print('speed R(T)/T: min %.3f, median %.3f, max %.3f' % (speeds[0], speeds[len(speeds) // 2], speeds[-1]))
print('runs with a retreat after time 1: %d of %d (retreats in all %d); longest stall %d ticks' % (retreat_runs, N, retreats_total, stall_max))
print('slowest run (alignment a=%d, q=%d), R(t) for t < 40: %s' % (slow[1], slow[2], slow[3]))
