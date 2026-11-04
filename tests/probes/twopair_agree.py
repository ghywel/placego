#!/usr/bin/env python3
"""agree.py (Local, L1519): how many ticks of the V word are needed to separate all odd registers at width n, the checkerboard pair
excepted? Random-like behaviour predicts about 2n. A structured decoder would be nearer n."""
import numpy as np, time
for n in range(4, 22):
    N = 1 << (n - 1); M = np.uint64((1 << n) - 1)
    x = np.arange(N, dtype=np.uint64) * np.uint64(2) + np.uint64(1)
    key = np.zeros(N, dtype=np.uint64); T = None
    for t in range(1, 64):
        v = ((x >> np.uint64(n - 1)) | (x >> np.uint64(n - 2))) & np.uint64(1)
        key = key * np.uint64(2) + v
        x = (x ^ ((x * np.uint64(2)) | (x * np.uint64(4)))) & M
        d = len(np.unique(key))
        if d == N - 1:
            T = t; break
    print('n', n, 'ticks to separate all but the pair', T, 'ratio T/n', None if T is None else round(T / n, 2))
