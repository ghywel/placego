#!/usr/bin/env python3
"""L1315 T40 (Local, 2026-11-02): do perturbations in a phase's black-edge wake ever reach the front?
reports/rule30-genealogy.md section 43.4 (predictions written first). Run: python3 tests/probes/wake_decouple.py PHASE

Clean start (the phase directly below a black edge; P1024 at theta = 0, others at alignment (0, 0)). At tick T0 = 600,
flip 1 to 4 random bits within a few cells of depth R(T0) - d (d = 50, 100, 200; 30 trials each), run both rows to
tick T0 + 2000, and track the deepest depth where they differ, Q(t), against the unperturbed front R(t). Reported per d:
trials where Q reached R - 2 or deeper at some tick, the smallest final gap R - Q, and the mean speed of Q.
"""
import os
import random
import sys
import runpy
here = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(here, 'upward_rigid.py'), run_name='lib')
name = sys.argv[1]; p, cols, _ = g['phases']()[name]; NC = len(cols)
T0, T1 = 600, 2600; depth = 2 * T1 + 16; mask = (1 << depth) - 1
if name == 'P1024':
    E = lambda n, t: (cols[0] >> ((t + 195 * n) % p)) & 1
else:
    E = lambda n, t: (cols[n % NC] >> (t % p)) & 1
rows = {}
def erow(t):
    k = t % p
    if k not in rows:
        rows[k] = sum(E(n, t) << n for n in range(depth))
    return rows[k]
step = lambda x: (x ^ ((x << 1) | (x << 2) | 3)) & mask
x = erow(0); traj = []
for t in range(T1 + 1):
    traj.append(x); x = step(x)
front = [((traj[t] ^ erow(t)) & mask).bit_length() - 1 for t in range(T1 + 1)]
rng = random.Random(40)
for d in (50, 100, 200):
    reached = 0; gaps = []; speeds = []
    for trial in range(30):
        y = traj[T0]; c = front[T0] - d
        for _ in range(rng.randint(1, 4)):
            y ^= 1 << (c + rng.randint(-3, 3))
        hit = False; q0 = None
        for t in range(T0, T1 + 1):
            diff = (y ^ traj[t]) & mask
            Q = diff.bit_length() - 1
            if q0 is None:
                q0 = Q
            if Q >= front[t] - 2:
                hit = True
            y = step(y)
        reached += hit; gaps.append(front[T1] - Q); speeds.append((Q - q0) / (T1 - T0))
    print('%s d=%3d: perturbations reaching the front %d of 30; smallest final gap %d; Q speed min %.3f max %.3f; front speed %.3f' % (
        name, d, reached, min(gaps), min(speeds), max(speeds), (front[T1] - front[T0]) / (T1 - T0)), flush=True)
