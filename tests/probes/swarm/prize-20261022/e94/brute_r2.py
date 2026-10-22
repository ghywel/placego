#!/usr/bin/env python3
"""Control: brute force over ALL subsets of the radius-2 hex patch (19 points): for each n, the minimum number of
distances with multiplicity in [1, n] (rmin) and the max second-smallest multiplicity (m2max). Compare with SAT."""
import itertools, time
from collections import defaultdict
t0 = time.time()
R = 2
pts = [(a, b) for a in range(-R, R+1) for b in range(-R, R+1) if abs(a+b) <= R]
M = len(pts)
D = [[(pts[i][0]-pts[j][0])**2 + (pts[i][0]-pts[j][0])*(pts[i][1]-pts[j][1]) + (pts[i][1]-pts[j][1])**2 for j in range(M)] for i in range(M)]
rmin = {}; m2max = {}
for mask in range(1, 1 << M):
    S = [i for i in range(M) if mask >> i & 1]
    n = len(S)
    if n < 5: continue
    c = defaultdict(int)
    for a in range(n):
        Da = D[S[a]]
        for b in range(a+1, n): c[Da[S[b]]] += 1
    v = sorted(c.values())
    r = sum(1 for x in v if x <= n)
    if r < rmin.get(n, 99): rmin[n] = r
    m2 = v[1] if len(v) > 1 else 0
    if m2 > m2max.get(n, -1): m2max[n] = m2
    if time.time() - t0 > 540: print('time limit'); break
print('rmin', dict(sorted(rmin.items())))
print('m2max', dict(sorted(m2max.items())))
print('secs', round(time.time() - t0, 1))
