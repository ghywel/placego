#!/usr/bin/env python3
"""Local, 2026-10-28 (L1068): approximate periodic points of the edge map T(x) = x XOR (2x OR 4x) (GC808).

For each k, counts odd residues x mod 2^k with T^P(x) = x (mod 2^k), vectorised over all residues. T is 1-Lipschitz,
so this is the number of residues lying on cycles of T mod 2^k whose length divides P. Usage: approx_periodic_points.py KMAX [P1,P2,...]   (default 2,8,64)
"""
import sys
import numpy as np
KMAX = int(sys.argv[1]); PS = [int(v) for v in (sys.argv[2] if len(sys.argv) > 2 else '2,8,64').split(',')]
for k in range(4, KMAX + 1):
    mask = np.uint32((1 << k) - 1)
    x = np.arange(1, 1 << k, 2, dtype=np.uint32); y = x.copy(); out = []
    for t in range(1, max(PS) + 1):
        y = (y ^ ((y << np.uint32(1)) | (y << np.uint32(2)))) & mask
        if t in PS: out.append(int(np.count_nonzero(y == x)))
    print(f"k={k:2d}: " + "   ".join(f"T^{p}: {c:6d}" for p, c in zip(PS, out)) + f"   (of {1 << (k - 1)})", flush=True)
