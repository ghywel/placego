#!/usr/bin/env python3
"""bg_exact.py NAME KMIN KMAX: exact M(k) by chunked exhaustion (2^18 prefixes per chunk), with maximizer prefixes and the minimal
shield (depths where a maximizer differs from its own alignment's inserted edge). Cloud, Block 14."""
import sys, numpy as np
name = sys.argv[1]; KMIN, KMAX = int(sys.argv[2]), int(sys.argv[3])
STATE0 = {'c7_28': '1000000', 's7_63': '1010000', 's9_57': '100100000', 's12_68': '100100000000', 'e4_8': '1000'}[name]
p = len(STATE0); s0 = tuple(int(c) for c in STATE0)
def ring_step(s): return tuple(s[j] ^ (s[(j-1) % p] | s[(j-2) % p]) for j in range(p))
orbit = [s0]; cur = ring_step(s0)
while cur != s0: orbit.append(cur); cur = ring_step(cur)
q = len(orbit)
CH = 1 << 18
def traces_chunk(k, H, base, n):
    r = np.arange(base, base + n, dtype=np.int64)
    X = np.zeros((k+2, n), dtype=np.uint8); X[0] = 1
    for j in range(1, k+2): X[j] = (r >> (j-1)) & 1
    a = np.empty((H, n), dtype=np.uint8); b = np.empty_like(a)
    for t in range(H):
        a[t], b[t] = X[k], X[k+1]
        Y = X.copy(); Y[1] = X[1] ^ X[0]; Y[2:] = X[2:] ^ (X[1:-1] | X[:-2]); X = Y
    return a, b
def inserted(k, r, s):
    st = orbit[s % q]; return ''.join(str(st[(j + r) % p]) for j in range(1, k+2))
for k in range(KMIN, KMAX+1):
    H = 3*k + 3*q + 24; N = 1 << (k+1); best = 0; arg = []
    for base in range(0, N, CH):
        n = min(CH, N - base); a, b = traces_chunk(k, H, base, n)
        for r in range(p):
            for s in range(q):
                alive = np.ones(n, dtype=bool); run = np.zeros(n, dtype=np.int64)
                for t in range(H):
                    st = orbit[(t+s) % q]
                    alive &= (a[t] == st[(k+r) % p]) & (b[t] == st[(k+1+r) % p])
                    if not alive.any(): break
                    run += alive
                rm = int(run.max())
                if rm > best: best, arg = rm, [(r, s, base + int(x)) for x in np.flatnonzero(run == rm)[:20]]
                elif rm == best: arg += [(r, s, base + int(x)) for x in np.flatnonzero(run == rm)[:20]]
    desc = []
    for (r, s, x) in arg[:3]:
        pre = ''.join(str((x >> (j-1)) & 1) for j in range(1, k+2)); ins = inserted(k, r, s)
        diff = [j+1 for j in range(k+1) if pre[j] != ins[j]]
        desc.append(f"({r},{s}) shield depths {diff}")
    print(f"k={k:2d} M={best:3d} horizon {H} maximizers {len(arg)}: " + '; '.join(desc), flush=True)
print("BG_EXACT_DONE", flush=True)
