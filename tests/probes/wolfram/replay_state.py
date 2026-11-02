#!/usr/bin/env python3
"""replay_state.py: G28's direct replay. For (9,57) alignment (0,0): simulate the lab configuration, read the real (phase, strip) state at
several times, and check that the certificate's transition applied to the real state reproduces the real next state and anchor motion."""
import numpy as np, importlib.util, sys
sys.argv = ['x', 's9_57', '19', '14', '16', '1']
spec = importlib.util.spec_from_file_location('cs', 'closed_set.py'); src = open('closed_set.py').read().split("T = 400")[0]
ns = {}; exec(src, ns)
E, step, transitions, orb, q, N = ns['E'], ns['step'], ns['transitions'], ns['orb'], ns['q'], ns['N']
r, s, W, T = 0, 0, 16, 600
WL = 2*T + 100; WR = T + 60; c = WL
bg = np.array([E(x, 0, r, s) for x in range(-WL, WR)], dtype=np.uint8); pert = bg.copy(); pert[c] = 1; pert[c+1:] = 0
a, b = bg.copy(), pert.copy(); xA = None; ok = 0; bad = 0
for t in range(T):
    d = np.flatnonzero(a ^ b); xmin = int(d.min()) - c
    if xA is None or xmin - 1 < xA: xA = xmin - 1      # the anchor retreats only
    strip = tuple(int(v) for v in b[c + xA + 1: c + xA + 1 + W]); st = (t % q, (t - xA) % N, strip)
    a2, b2 = step(a), step(b)
    outs = transitions(st, r, s, W)
    d2 = np.flatnonzero(a2 ^ b2); xmin2 = int(d2.min()) - c; xA2 = min(xA, xmin2 - 1)
    strip2 = tuple(int(v) for v in b2[c + xA2 + 1: c + xA2 + 1 + W]); real = ((t + 1) % q, (t + 1 - xA2) % N, strip2)
    if t >= 300:
        if outs is not None and any(nst == real and mv == xA2 - xA for nst, mv in outs): ok += 1
        else: bad += 1; print("mismatch at t", t, "real", real, "predicted", outs)
    a, b, xA = a2, b2, xA2
print(f"(9,57) alignment (0,0), W={W}: real transitions reproduced by the certificate's transition at t in [300, 600): ok {ok}, bad {bad}")
