#!/usr/bin/env python3
"""L1315 T39 (Local, 2026-11-02): is P1024's clean-start wake a global attractor for black-edge rows?
reports/rule30-genealogy.md section 43 (predictions written first). Run: python3 tests/probes/wake_attractor.py [N] [K ...]

P1024 below a black edge, C_K(t) = C_0(t + 195 K), at a random class theta. A row has random digits at depths 0 .. K-1
above P1024's clean tail; it evolves by Phi(x) = x ^ ((x << 1) | (x << 2) | 3) for 6K + 2000 ticks. After the front
first passes depth 3K, the run records the first exact recurrence of (256 mismatch bits above the front, front class
theta), giving (period, advance). The clean-start wake has (208, 272), speed 17/13. L1316 (T41, P41e): --win=W uses
the W mismatch bits above the front instead of 256, with the same prefixes; at W = 32 the clean-start near-front
period is 52 (advance 68), a quarter of 208, so (52, 68) and its multiples are counted too; and capture is tested
strictly: the first tick at which (window, front class) equals one of the clean front's own pairs (ticks >= 600) at the
same theta. Reported per K: runs that recur
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
args = [a for a in sys.argv[1:] if not a.startswith('--win=')]      # L1316 T41 P41e: --win=W cuts the window (default 256)
WIN = next((int(a[6:]) for a in sys.argv[1:] if a.startswith('--win=')), 256)
N = int(args[0]) if args else 200
Ks = [int(x) for x in args[1:]] or [40, 80]
rng = random.Random(39)
for K in Ks:
    T = 6 * K + 2000; depth = 2 * T + K + 16; mask = (1 << depth) - 1
    kinds = Counter(); late_speeds = []; capts = []
    for it in range(N):
        th = rng.randrange(p)
        rows = {}
        def erow(t):
            k = t % p
            if k not in rows:
                rows[k] = sum(((col0 >> ((th + t + 195 * n) % p)) & 1) << n for n in range(depth))
            return rows[k]
        x = rng.getrandbits(K) | (erow(0) >> K << K)
        if WIN != 256:                    # the clean front's (window, class) pairs from tick 600 on, at the same theta
            clean = set(); xc = erow(0)
            for t in range(T + 1):
                dc = xc ^ erow(t); Rc = dc.bit_length() - 1
                if t >= 600:
                    clean.add(((dc >> (Rc - WIN)) & ((1 << WIN) - 1), (th + t + 195 * Rc) % p))
                xc = (xc ^ ((xc << 1) | (xc << 2) | 3)) & mask
        seen = {}; found = None; passed_t = None; passed_R = None; capt = None
        for t in range(T + 1):
            d = (x ^ erow(t)) & mask
            R = d.bit_length() - 1
            if passed_t is None and R >= 3 * K:
                passed_t, passed_R = t, R
            if passed_t is not None and found is None and R >= WIN:
                key = ((d >> (R - WIN)) & ((1 << WIN) - 1), (th + t + 195 * R) % p)
                if WIN != 256 and capt is None and key in clean:
                    capt = t
                if key in seen:
                    t1, R1 = seen[key]; found = (t - t1, R - R1)
                else:
                    seen[key] = (t, R)
            x = (x ^ ((x << 1) | (x << 2) | 3)) & mask
        if passed_t is not None and T > passed_t:
            late_speeds.append((R - passed_R) / (T - passed_t))
        if WIN != 256:
            kinds['window equals a clean-front window'] += capt is not None
            if capt is not None:
                capts.append(capt - passed_t)
        if found is None:
            kinds['no recurrence'] += 1
        elif found[0] % 208 == 0 and found[1] * 208 == found[0] * 272:
            kinds['clean-start wake (208, 272) or a multiple'] += 1
        elif WIN != 256 and found[0] % 52 == 0 and found[1] * 52 == found[0] * 68:
            kinds['clean-start near-front period (52, 68) or a multiple'] += 1
        else:
            kinds['other recurrence %s' % (found,)] += 1
    print(('window %d, ' % WIN if WIN != 256 else '') + 'K=%d, %d runs, %d ticks: %s; late speed min %.4f max %.4f (17/13 = %.4f)' % (
        K, N, T, dict(kinds), min(late_speeds), max(late_speeds), 17 / 13), flush=True)
    if capts:
        print('   ticks from passing depth 3K to the first clean-front window: median %d, max %d' % (
            sorted(capts)[len(capts) // 2], max(capts)), flush=True)
