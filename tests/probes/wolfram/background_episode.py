#!/usr/bin/env python3
"""bg_episode.py BACKGROUND KMAX: exact M(k), maximizer witness test and inserted-edge front speeds for one ring background (Cloud, Block 13)."""
import sys, numpy as np
name = sys.argv[1]; KMAX = int(sys.argv[2])
STATE0 = {'c7_28': '1000000', 's7_63': '1010000', 's9_57': '100100000', 's12_68': '100100000000', 'e4_8': '1000'}[name]
p = len(STATE0); s0 = tuple(int(c) for c in STATE0)
def ring_step(s): return tuple(s[j] ^ (s[(j-1) % p] | s[(j-2) % p]) for j in range(p))
orbit = [s0]; cur = ring_step(s0)
while cur != s0: orbit.append(cur); cur = ring_step(cur)
q = len(orbit)
print(f"background {name}: p={p} q={q} state0={STATE0}", flush=True)
def traces(k, H):
    n = 1 << (k+1); r = np.arange(n, dtype=np.int64)
    X = np.zeros((k+2, n), dtype=np.uint8); X[0] = 1
    for j in range(1, k+2): X[j] = (r >> (j-1)) & 1
    a = np.empty((H, n), dtype=np.uint8); b = np.empty_like(a)
    for t in range(H):
        a[t], b[t] = X[k], X[k+1]
        Y = X.copy(); Y[1] = X[1] ^ X[0]; Y[2:] = X[2:] ^ (X[1:-1] | X[:-2]); X = Y
    return a, b
def inserted_prefix(k, r, s):
    st = orbit[s % q]; v = 0
    for j in range(1, k+2): v |= st[(j + r) % p] << (j-1)
    return v
results = {}
for k in range(1, KMAX+1):
    H = 3*k + 3*q + 24
    a, b = traces(k, H)
    best = 0; argmax = []
    for r in range(p):
        for s in range(q):
            alive = np.ones(a.shape[1], dtype=bool); run = np.zeros(a.shape[1], dtype=np.int64)
            for t in range(H):
                st = orbit[(t+s) % q]
                alive &= (a[t] == st[(k+r) % p]) & (b[t] == st[(k+1+r) % p])
                if not alive.any(): break
                run += alive
            rm = int(run.max())
            if rm > best: best, argmax = rm, [(r, s, int(x)) for x in np.flatnonzero(run == rm)[:50]]
            elif rm == best: argmax += [(r, s, int(x)) for x in np.flatnonzero(run == rm)[:50]]
    nwit = sum(1 for (r, s, x) in argmax if x == inserted_prefix(k, r, s))
    results[k] = (best, len(argmax), nwit)
    print(f"k={k:2d} M={best:3d} (horizon {H}) maximizers listed {len(argmax)}, of which inserted-edge witnesses {nwit}", flush=True)
print("M(1..%d) = %s" % (KMAX, ' '.join(str(results[k][0]) for k in range(1, KMAX+1))), flush=True)
# fronts of inserted-edge witnesses (all alignments), depth J, time T
T, J = 70, 300
speeds = {}
for r in range(p):
    for s in range(q):
        X = np.zeros(J+1, dtype=np.uint8); X[0] = 1
        for j in range(1, J+1): X[j] = orbit[s % q][(j+r) % p]
        R = []
        for t in range(T+1):
            st = orbit[(t+s) % q]
            E = np.array([st[(j+r) % p] for j in range(J+1)], dtype=np.uint8)
            D = np.flatnonzero((X ^ E)[:J+1-2*t]) if J+1-2*t > 0 else np.array([])
            R.append(int(D.max()) if D.size else -1)
            Y = X.copy(); Y[1] = X[1] ^ X[0]; Y[2:] = X[2:] ^ (X[1:-1] | X[:-2]); X = Y
        tt = np.arange(24, 61); rr = np.array(R[24:61], dtype=float)
        slope = np.polyfit(tt, rr, 1)[0] if np.all(rr >= 0) else float('nan')
        speeds[(r, s)] = (round(float(slope), 3), R)
sl = sorted(set(v[0] for v in speeds.values()))
print("inserted-edge witness front speeds (slope of R*(t) over t=30..60), distinct values:", sl, flush=True)
# the witness with the longest episode at depth KMAX and its front sequence
# episode length of witness (r,s) at depth k = first t with R*(t) >= k
def wit_len(R, k):
    return next((t for t, x in enumerate(R) if x >= k), None)
for k in (KMAX,):
    L = {(r, s): wit_len(speeds[(r, s)][1], k) for (r, s) in speeds}
    bestL = max(v for v in L.values() if v is not None)
    bests = [a for a, v in L.items() if v == bestL]
    print(f"witness episode lengths at k={k}: max {bestL} (exact M({k}) = {results[k][0]}) attained by alignments {bests[:8]}", flush=True)
    r, s = bests[0]
    print(f"front R*(t) t=0..60 for alignment {(r, s)}: {speeds[(r, s)][1][:61]}", flush=True)
    print("increments t=8..60:", [speeds[(r, s)][1][t] - speeds[(r, s)][1][t-1] for t in range(9, 61)], flush=True)
print("BG_EPISODE_DONE", flush=True)
