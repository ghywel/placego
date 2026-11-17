#!/usr/bin/env python3
"""Local, 2026-10-28 (L1071): GF(2) algebraic normal form of the centre cell after t steps, as a function of its
2t+1 initial cells, by exhaustive truth table and Moebius transform. Reports degree, number of monomials and the
top-degree monomials (as the initial cells they omit). Independent check of a research agent's report (degree 2t-1 for 2 <= t <= 9).
Usage: centre_anf_degree.py TMAX
"""
import sys
import numpy as np
TMAX = int(sys.argv[1])
for t in range(1, TMAX + 1):
    n = 2 * t + 1; N = 1 << n
    idx = np.arange(N, dtype=np.uint32)
    cells = [((idx >> k) & 1).astype(np.uint8) for k in range(n)]   # cell k = initial position k - t
    row = cells
    for _ in range(t):
        row = [row[i - 1] ^ (row[i] | row[i + 1]) for i in range(1, len(row) - 1)]
    f = row[0].copy()                                               # truth table of c(t)
    for k in range(n):                                              # Moebius transform -> ANF coefficients
        s = 1 << k
        f = f.reshape(-1, 2 * s); f[:, s:] ^= f[:, :s]; f = f.reshape(-1)
    mons = np.nonzero(f)[0]
    deg = np.array([bin(int(m)).count("1") for m in mons])
    top = int(deg.max())
    tops = [[k - t for k in range(n) if not (int(m) >> k) & 1] for m in mons[deg == top]]
    print(f"t={t}: degree {top} (2t-1 = {2*t-1}), monomials {len(mons)}, top-degree monomials {int((deg == top).sum())}, "
          f"cells missing from them {tops}", flush=True)
