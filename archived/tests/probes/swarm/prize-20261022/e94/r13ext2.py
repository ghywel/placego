#!/usr/bin/env python3
"""As r13ext.py but excluding p near q (|y-1| < 0.05) and p near the centre (|y| < 1e-3); exact-ish refinement of the best."""
import math
ch = [2*math.sin(math.pi*m/13) for m in range(1, 7)]
def vals(y):
    return [abs(1 - y)] + [math.sqrt(1 + y*y - 2*y*math.cos(2*math.pi*k/13)) for k in range(1, 7)]
def nch(y, tol):
    return sum(1 for a in vals(y) if min(abs(a - c) for c in ch) < tol)
N = 800000; res = {}
for i in range(-N, N + 1):
    y = i * (10.0 / N)
    if abs(y - 1) < 0.05 or abs(y) < 1e-3: continue
    k = nch(y, 1e-3)
    res.setdefault(k, []).append(y)
for k in sorted(res, reverse=True)[:3]:
    ys = res[k]
    print('chord-valued count', k, ': #grid points', len(ys), 'sample y', [round(v, 4) for v in ys[:6]])
