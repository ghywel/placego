#!/usr/bin/env python3
"""L1454 (Local, 2026-11-03): follow the SAT models of a4_wall_robustness.py. Replace pattern PATTERN's cells at relative
W+1 .. W+len(EXT) at T0 by the breaking content EXT (the rest of the row actual), evolve TF more ticks, and report the
front's late behaviour: least exact lag over the last half, its speed, and the slope. Run:
python3 tests/probes/wolfram/a4_breaking_followup.py DATA63.json PATTERN T0 W TF EXT [EXT ...]
"""
import json
import sys
from fractions import Fraction

import numpy as np

data = json.load(open(sys.argv[1])); PAT = int(sys.argv[2], 0); T0, W, TF = map(int, sys.argv[3:6]); EXTS = sys.argv[6:]
orb = [tuple(o) for o in data['orb']]; q = len(orb); N = data['N']; r0, s0 = data['r'], data['s']
E = lambda x, t: orb[(t + s0) % q][((t - x) + r0) % N]
TM = T0 + TF + 5; lo = -2 * TM - 10; hi = TM + 600; c = -lo
row = np.array([E(x, 0) for x in range(lo, hi)], dtype=np.uint8); bg = row.copy()
for i in range(12):
    row[c + i] ^= (PAT >> i) & 1
for t in range(1, T0 + 1):
    n = np.zeros_like(row); n[1:-1] = row[:-2] ^ (row[1:-1] | row[2:]); row = n
    m = np.zeros_like(bg); m[1:-1] = bg[:-2] ^ (bg[1:-1] | bg[2:]); bg = m
A0 = int(np.flatnonzero(row ^ bg).min()) - 1
for label, ext in [('actual', None)] + [('model %d' % i, e) for i, e in enumerate(EXTS)]:
    r2 = row.copy(); b2 = bg.copy()
    if ext:
        for i, ch in enumerate(ext):
            r2[A0 + W + 1 + i] = int(ch)
    Fs = []
    for k in range(TF + 1):
        if k:
            n = np.zeros_like(r2); n[1:-1] = r2[:-2] ^ (r2[1:-1] | r2[2:]); r2 = n
            m = np.zeros_like(b2); m[1:-1] = b2[:-2] ^ (b2[1:-1] | b2[2:]); b2 = m
        Fs.append(int(np.flatnonzero(r2 ^ b2).min()))
    f = np.array(Fs[TF // 2:]); found = None
    for L in range(1, 600):
        d = f[L:] - f[:-L]
        if (d == d[0]).all():
            found = (L, int(d[0])); break
    sl = (Fs[-1] - Fs[TF // 2]) / (TF - TF // 2)
    print('%s: late slope over [%d, %d] = %.4f; exact lag law: %s' % (
        label, T0 + TF // 2, T0 + TF, sl, ('lag %d, displacement %d, speed %s' % (found[0], found[1], Fraction(-found[1], found[0]))) if found else 'none <= 600'))
print('A4_BREAKING_FOLLOWUP_DONE')
