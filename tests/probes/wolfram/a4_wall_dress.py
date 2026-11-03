#!/usr/bin/env python3
"""L1441 (Local, 2026-11-03): P-j. How wide is the co-moving periodic "dress" behind a wall on 1010000? For a finite
perturbation, evolve exactly and record rows; at times t compare row(t)[F(t) + j] with row(t + L)[F(t + L) + j] for j >= 0
and report the first j where they differ (the dress width), for each lag L given. Run:
python3 tests/probes/wolfram/a4_wall_dress.py DATA63.json TMAX PATTERN L [L ...]
"""
import json
import sys

import numpy as np

data = json.load(open(sys.argv[1])); TMAX = int(sys.argv[2]); PAT = int(sys.argv[3], 0); LAGS = [int(x) for x in sys.argv[4:]]
orb = [tuple(o) for o in data['orb']]; q = len(orb); N = data['N']; r0, s0 = data['r'], data['s']
E = lambda x, t: orb[(t + s0) % q][((t - x) + r0) % N]
lo = -2 * TMAX - 10; hi = TMAX + 22; c = -lo
row = np.array([E(x, 0) for x in range(lo, hi)], dtype=np.uint8); bg = row.copy()
for i in range(12):
    row[c + i] ^= (PAT >> i) & 1
keep = {}; Fs = {}
SAMPLE = set(range(500, TMAX + 1, 250))
need = set()
for s in SAMPLE:
    for L in LAGS:
        if s + L <= TMAX:
            need |= {s, s + L}
for t in range(0, TMAX + 1):
    if t > 0:
        n = np.zeros_like(row); n[1:-1] = row[:-2] ^ (row[1:-1] | row[2:]); row = n
        m = np.zeros_like(bg); m[1:-1] = bg[:-2] ^ (bg[1:-1] | bg[2:]); bg = m
    if t in need:
        d = np.flatnonzero(row ^ bg); Fs[t] = int(d.min()); keep[t] = (row.copy(), len(row) - t - 2)
print('pattern %d (0x%x), lags %s:' % (PAT, PAT, LAGS))
for s in sorted(SAMPLE):
    parts = []
    for L in LAGS:
        if s + L > TMAX:
            continue
        a, va = keep[s]; b, vb = keep[s + L]; Fa, Fb = Fs[s], Fs[s + L]
        J = min(va - Fa, vb - Fb)
        diff = np.flatnonzero(a[Fa: Fa + J] != b[Fb: Fb + J])
        w = int(diff[0]) if len(diff) else J
        parts.append('L=%d: shift %d, dress %d%s' % (L, Fb - Fa, w, '' if len(diff) else ' (whole exact range)'))
    if parts:
        print('  t=%d F=%d: %s' % (s, Fs[s] - c, '; '.join(parts)), flush=True)
print('A4_WALL_DRESS_DONE')
