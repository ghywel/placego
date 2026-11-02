#!/usr/bin/env python3
"""L1315 T39 (Local, 2026-11-02): is P1024's clean-start wake a global attractor for black-edge rows?
reports/rule30-genealogy.md section 43 (predictions written first). Run: python3 tests/probes/wake_attractor.py [N] [K ...]

P1024 below a black edge, C_K(t) = C_0(t + 195 K), at a random class theta. A row has random digits at depths 0 .. K-1
above P1024's clean tail; it evolves by Phi(x) = x ^ ((x << 1) | (x << 2) | 3) for 6K + 2000 ticks. After the front
first passes depth 3K, the run records the first exact recurrence of (256 mismatch bits above the front, front class
theta), giving (period, advance). The clean-start wake has (208, 272), speed 17/13. Reported per K: runs that recur
with (208, 272) or a multiple of it, runs that recur otherwise, runs with no recurrence, and the late speed.
"""
import os
import random
import sys
import runpy
from collections import Counter
here = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(here, 'upward_rigid.py'), run_name='lib')
p, cols, _ = g['phases']()['P1024']; col0 = cols[0]
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200
Ks = [int(x) for x in sys.argv[2:]] or [40, 80]
WIN = 256; rng = random.Random(39)
for K in Ks:
    T = 6 * K + 2000; depth = 2 * T + K + 16; mask = (1 << depth) - 1
    kinds = Counter(); late_speeds = []
    for it in range(N):
        th = rng.randrange(p)
        rows = {}
        def erow(t):
            k = t % p
            if k not in rows:
                rows[k] = sum(((col0 >> ((th + t + 195 * n) % p)) & 1) << n for n in range(depth))
            return rows[k]
        x = rng.getrandbits(K) | (erow(0) >> K << K)
        seen = {}; found = None; passed_t = None; passed_R = None
        for t in range(T + 1):
            d = (x ^ erow(t)) & mask
            R = d.bit_length() - 1
            if passed_t is None and R >= 3 * K:
                passed_t, passed_R = t, R
            if passed_t is not None and found is None and R >= WIN:
                key = ((d >> (R - WIN)) & ((1 << WIN) - 1), (th + t + 195 * R) % p)
                if key in seen:
                    t1, R1 = seen[key]; found = (t - t1, R - R1)
                else:
                    seen[key] = (t, R)
            x = (x ^ ((x << 1) | (x << 2) | 3)) & mask
        if passed_t is not None and T > passed_t:
            late_speeds.append((R - passed_R) / (T - passed_t))
        if found is None:
            kinds['no recurrence'] += 1
        elif found[0] % 208 == 0 and found[1] * 208 == found[0] * 272:
            kinds['clean-start wake (208, 272) or a multiple'] += 1
        else:
            kinds['other recurrence %s' % (found,)] += 1
    print('K=%d, %d runs, %d ticks: %s; late speed min %.4f max %.4f (17/13 = %.4f)' % (
        K, N, T, dict(kinds), min(late_speeds), max(late_speeds), 17 / 13), flush=True)
