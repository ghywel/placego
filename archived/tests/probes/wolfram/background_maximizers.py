#!/usr/bin/env python3
import sys, numpy as np
name = sys.argv[1]; ks = [int(x) for x in sys.argv[2].split(',')]
STATE0 = {'c7_28': '1000000', 's7_63': '1010000', 's9_57': '100100000', 's12_68': '100100000000', 'e4_8': '1000'}[name]
p = len(STATE0); s0 = tuple(int(c) for c in STATE0)
def ring_step(s): return tuple(s[j] ^ (s[(j-1) % p] | s[(j-2) % p]) for j in range(p))
orbit = [s0]; cur = ring_step(s0)
while cur != s0: orbit.append(cur); cur = ring_step(cur)
q = len(orbit)
def traces(k, H):
    n = 1 << (k+1); r = np.arange(n, dtype=np.int64)
    X = np.zeros((k+2, n), dtype=np.uint8); X[0] = 1
    for j in range(1, k+2): X[j] = (r >> (j-1)) & 1
    a = np.empty((H, n), dtype=np.uint8); b = np.empty_like(a)
    for t in range(H):
        a[t], b[t] = X[k], X[k+1]
        Y = X.copy(); Y[1] = X[1] ^ X[0]; Y[2:] = X[2:] ^ (X[1:-1] | X[:-2]); X = Y
    return a, b
def inserted(k, r, s):
    st = orbit[s % q]; return ''.join(str(st[(j + r) % p]) for j in range(1, k+2))
for k in ks:
    H = 3*k + 3*q + 24; a, b = traces(k, H); best = 0; arg = []
    for r in range(p):
        for s in range(q):
            alive = np.ones(a.shape[1], dtype=bool); run = np.zeros(a.shape[1], dtype=np.int64)
            for t in range(H):
                st = orbit[(t+s) % q]
                alive &= (a[t] == st[(k+r) % p]) & (b[t] == st[(k+1+r) % p])
                if not alive.any(): break
                run += alive
            rm = int(run.max())
            if rm > best: best, arg = rm, [(r, s, int(x)) for x in np.flatnonzero(run == rm)]
            elif rm == best: arg += [(r, s, int(x)) for x in np.flatnonzero(run == rm)]
    print(f"\n{name} k={k}: M={best}, {len(arg)} maximizers (r,s,prefix); depths 1..{k+1} left to right")
    for (r, s, x) in arg[:4]:
        pre = ''.join(str((x >> (j-1)) & 1) for j in range(1, k+2)); ins = inserted(k, r, s)
        diff = ''.join('^' if u != v else '.' for u, v in zip(pre, ins))
        # best other alignment matching the top part: largest d such that prefix depths d..k+1 equal some inserted(k, r', s') there
        bestd = None
        for r2 in range(p):
            for s2 in range(q):
                ins2 = inserted(k, r2, s2)
                d = next((j for j in range(k+1) if pre[j:] == ins2[j:]), None)
                if d is not None and (bestd is None or d < bestd[0]): bestd = (d, r2, s2)
        print(f"  align ({r:2d},{s:2d}) prefix {pre}\n               inserted {ins}\n               differs  {diff}   | top part equals inserted-edge of alignment {bestd[1:]} from depth {bestd[0]+1}")
