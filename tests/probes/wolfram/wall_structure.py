#!/usr/bin/env python3
"""wall_structure.py T: classic ether, alignment (0,0): the settled wake behind the wall. Lab column periods along x at time T (over the
last 512 rows), the settled width at several times, and whether settled columns match the ether in another alignment. Cloud, Block 23."""
import sys, numpy as np
T = int(sys.argv[1]); y = np.array([1,0,0,0,0,0,0], dtype=np.uint8); N = 7
def cst(s): return s ^ (np.roll(s, 1) | np.roll(s, 2))
orb = [y.copy()]; cur = cst(y)
while not np.array_equal(cur, y): orb.append(cur.copy()); cur = cst(cur)
orb = np.array(orb); q = len(orb)
def E(x, t, r=0, s=0): return int(orb[(t + s) % q][((t - x) + r) % N])
def step(rw):
    n = np.zeros_like(rw); n[1:-1] = rw[:-2] ^ (rw[1:-1] | rw[2:]); return n
WL = 2*T + 100; WR = T + 60; W = WL + WR; c = WL
bg = np.array([E(x, 0) for x in range(-WL, WR)], dtype=np.uint8); pert = bg.copy(); pert[c] = 1; pert[c+1:] = 0
keep = {}; marks = sorted(set([T//4, T//2, 3*T//4, T]))
hist = []
b = pert.copy()
for t in range(T + 1):
    if t > T - 512: hist.append(b.copy())
    if t in marks: keep[t] = None
    if t < T: b = step(b)
H = np.array(hist)   # last 512 rows
def col_period(col):
    for p in range(1, 129):
        if np.array_equal(col[p:], col[:-p]): return p
    return None
print(f"classic ether (0,0), T={T}: lab column periods over the last 512 rows, x from -4 to 120:")
per = {x: col_period(H[:, c + x]) for x in range(-4, 400)}
print("  ", [(x, per[x]) for x in range(-4, 60)])
runs = []; last = None
for x in range(-4, 400):
    if per[x] != last: runs.append([per[x], x, x]); last = per[x]
    else: runs[-1][2] = x
print("  period runs (period, x_from, x_to):", [tuple(r) for r in runs][:30])
settled = max([x for x in range(-4, 400) if per[x] is not None and all(per[x2] is not None for x2 in range(-4, x+1))], default=None)
print(f"  settled width (every column periodic with period <= 128 from the wall to x): {settled}")
# ether phase identification of settled columns: compare column x over the last 64 rows with E at every alignment (r,s)
def phase_of(x):
    col = H[-64:, c + x]
    for r in range(N):
        for s in range(q):
            if all(int(col[i]) == E(x, T - 63 + i, r, s) for i in range(64)): return (r, s)
    return None
print("  ether phase of columns x = -4..40 (None = not the ether in any alignment):", [(x, phase_of(x)) for x in range(-4, 41)])
print("WALL_STRUCTURE_DONE")
