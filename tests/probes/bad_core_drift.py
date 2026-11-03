#!/usr/bin/env python3
"""L1357 T52 (Local, 2026-11-03; NIGHT-TASKS D): do real fronts gain ground while their 8-cell state is in the bad core?
reports/rule30-genealogy.md section 56 (predictions written first).
Run: python3 tests/probes/bad_core_drift.py MASKS_W8.npz N K

P1024, the rows of T48 (Random(48), random K-cell prefixes at random theta). For every tick before capture with R >= 16,
the state (class, window; bit j-1 = D_(R-j)) is looked up in the saved masks (B = the bad core). Maximal runs of ticks in
B are cut into windows of H ticks (every start inside the run, windows entirely inside it), and the net advance over each
window is R(t + H) - R(t).
"""
import os
import random
import sys
import runpy
import numpy as np
here = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(here, 'upward_rigid.py'), run_name='lib')
m = np.load(sys.argv[1]); N, K = int(sys.argv[2]), int(sys.argv[3])
SE, B = m['SE'], m['B']; W = int(m['W'])
p, cols, _ = g['phases']()['P1024']; col0 = cols[0]
T = 6 * K + 2400; depth = 2 * T + K + 16; mask = (1 << depth) - 1
bits = [(col0 >> i) & 1 for i in range(p)]
base = [int(''.join(str(bits[(k + 195 * n) % p]) for n in range(depth))[::-1], 2) for k in range(p)]
rev = [int(format(v, '0%db' % W)[::-1], 2) for v in range(1 << W)]
rng = random.Random(48)
HS = [5, 10, 20]
win_adv = {H: [] for H in HS}; per_tick = []; in_B_ticks = 0
for it in range(N):
    th = rng.randrange(p)
    x = rng.getrandbits(K) | (base[th] >> K << K)
    run = []; runs = []
    for t in range(T + 1):
        d = (x ^ base[(th + t) % p]) & mask; R = d.bit_length() - 1
        if R >= 12:
            v = (((th + t + 195 * R) % p) << W) | rev[(d >> (R - W)) & ((1 << W) - 1)]
            if SE[v]:
                break
            if R >= 16 and B[v]:
                run.append(R); in_B_ticks += 1
            else:
                if len(run) > 1:
                    runs.append(run)
                run = []
        x = (x ^ ((x << 1) | (x << 2) | 3)) & mask
    if len(run) > 1:
        runs.append(run)
    for r in runs:
        per_tick.extend(r[i + 1] - r[i] for i in range(len(r) - 1))
        for H in HS:
            win_adv[H].extend(r[i + H] - r[i] for i in range(len(r) - H))
print('P1024 W=%d, %d rows, K=%d: ticks in B at R >= 16 before capture: %d; mean advance per tick in B %.3f (17/13 = %.3f)' % (
    W, N, K, in_B_ticks, float(np.mean(per_tick)), 17 / 13), flush=True)
for H in HS:
    a = np.array(win_adv[H])
    print('   H=%2d: %d windows inside B; least net advance %d; windows with net advance <= 0: %d (%.2f%%); median %d' % (
        H, len(a), int(a.min()) if len(a) else 0, int((a <= 0).sum()), 100.0 * (a <= 0).mean() if len(a) else 0,
        int(np.median(a)) if len(a) else 0), flush=True)
print('BAD_CORE_DRIFT_DONE')
