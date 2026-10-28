#!/usr/bin/env python3
"""Local, 2026-10-28 (L1066): every Rule 30 ring configuration of size m whose moving-frame map
Phi(x)[i] = x[i] XOR (x[i+1] OR x[i+2]) returns it after P steps (P a power of two), for m <= MMAX, vectorised.
Prints the primitive orbits (least spatial period, up to rotation) with their least Phi-periods.
Usage: ring_power2_census.py MMAX P [MMIN]
"""
import sys
import numpy as np
MMAX, P = int(sys.argv[1]), int(sys.argv[2]); MMIN = int(sys.argv[3]) if len(sys.argv) > 3 else 1
prim = {}
for m in range(MMIN, MMAX + 1):
    full = np.uint32((1 << m) - 1)
    x = np.arange(1 << m, dtype=np.uint32); y = x.copy()
    def rot(z, r):
        r %= m
        return z if r == 0 else ((z >> np.uint32(r)) | (z << np.uint32(m - r))) & full
    for _ in range(P):
        y = y ^ (rot(y, 1) | rot(y, 2))
    hits = x[y == x]
    for z in hits.tolist():
        s = format(z, f"0{m}b")
        # least spatial period of the cyclic word
        sp = next(q for q in range(1, m + 1) if m % q == 0 and s == s[q:] + s[:q])
        w = s[:sp]; can = min(w[r:] + w[:r] for r in range(sp))
        if can not in prim:
            # least Phi-period on the primitive ring
            mm = sp; f = (1 << mm) - 1; v = int(can, 2)
            def ph(u):
                def rr(z, r):
                    r %= mm
                    return z if r == 0 else ((z >> r) | (z << (mm - r))) & f
                return u ^ (rr(u, 1) | rr(u, 2))
            u = ph(v); t = 1
            while u != v and t <= P: u = ph(u); t += 1
            prim[can] = t
    print(f"m={m}: {len(hits)} configurations return within {P} steps", flush=True)
print("primitive orbits (word up to rotation: least Phi-period):", prim)
