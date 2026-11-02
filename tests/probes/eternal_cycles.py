#!/usr/bin/env python3
"""L1291 (Local, 2026-11-02): eternal cycles of the right-edge map Phi(x) = x XOR ((x<<1)|(x<<2)|3) on Z_2.
Predictions P11a-P11d in reports/rule30-genealogy.md section 25.2, written first.
Run: python3 tests/probes/eternal_cycles.py   (about a minute; no files written)
"""
import numpy as np

KMAX = 60
CAP = 3_000_000


def phi_np(x, mask):
    return (x ^ ((x << np.uint64(1)) | (x << np.uint64(2)) | np.uint64(3))) & mask


def solutions(p):
    """level-by-level solutions of Phi^p(x) = x mod 2^k, k = 1..KMAX; returns the list of arrays per level or None if capped."""
    S = np.array([0, 1], dtype=np.uint64)
    levels = {}
    for k in range(1, KMAX + 1):
        mask = np.uint64((1 << k) - 1) if k < 64 else np.uint64(0xFFFFFFFFFFFFFFFF)
        y = S.copy()
        for _ in range(p):
            y = phi_np(y, mask)
        S = S[y == S]
        levels[k] = S
        if k == KMAX:
            break
        if 2 * S.size > CAP:
            return levels, k
        S = np.concatenate((S, S | np.uint64(1 << k)))
    return levels, KMAX


def phi_int(x, k):
    return (x ^ ((x << 1) | (x << 2) | 3)) & ((1 << k) - 1)


def period_of(x, k, pmax=1 << 12):
    y = phi_int(x, k); n = 1
    while y != x and n <= pmax:
        y = phi_int(y, k); n += 1
    return n


def eventual_period(bits, max_off=20, max_per=24):
    for per in range(1, max_per + 1):
        for off in range(0, max_off + 1):
            if all(bits[i] == bits[i + per] for i in range(off, len(bits) - per)):
                return per, off
    return None


print('p, deepest level reached, solutions there, projections to K = 8, 16, 24, 32, 40 of the deepest solutions')
results = {}
for m in range(0, 8):
    p = 1 << m
    levels, kdeep = solutions(p)
    S = levels[kdeep]
    proj = {K: len(set((int(s) & ((1 << K) - 1)) for s in S)) if K <= kdeep else None for K in (8, 16, 24, 32, 40)}
    results[p] = (kdeep, S)
    print(f'  p={p:4d}: level {kdeep:2d}, {S.size:8d} solutions; projections ' + ' '.join(f'K={K}:{v}' for K, v in proj.items()))
# eternal points with exact period p, their digit structure (for small finite sets)
print('eternal points by exact period (from the deepest level; exact period measured at that level):')
for p, (kdeep, S) in results.items():
    if S.size == 0 or S.size > 4096:
        continue
    exact = [int(s) for s in S if period_of(int(s), kdeep) == p]
    # keep only one representative per orbit
    orbits = []
    seen = set()
    for x in sorted(exact):
        if x in seen:
            continue
        orb = [x]; y = phi_int(x, kdeep)
        while y != x:
            orb.append(y); y = phi_int(y, kdeep)
        seen.update(orb)
        orbits.append(orb)
    print(f'  p={p}: {len(exact)} points of exact period {p}, {len(orbits)} orbits at level {kdeep}')
    for orb in orbits[:8]:
        x = min(orb)
        bits = [(x >> i) & 1 for i in range(kdeep)]
        ep = eventual_period(bits)
        print(f'    orbit rep digits 0..39: {"".join(map(str, bits[:40]))}  eventual digit period/offset: {ep}')
print('ETERNAL_CYCLES_DONE')
