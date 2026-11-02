#!/usr/bin/env python3
"""L1291 (Local, 2026-11-02): period-64 eternal points of the right-edge map at 128-digit precision.
Prediction in reports/rule30-genealogy.md section 25 (second follow-up), written first.
Run: python3 tests/probes/eternal_cycles_128.py   (a minute or two; no files written)
Words are (lo, hi) pairs of uint64: digit k < 64 in lo, digit k >= 64 in hi.
"""
import numpy as np
U = np.uint64
ONE, TWO, S62, S63 = U(1), U(2), U(62), U(63)


def phi(lo, hi, mlo, mhi):
    l1 = lo << ONE; h1 = (hi << ONE) | (lo >> S63)
    l2 = lo << TWO; h2 = (hi << TWO) | (lo >> S62)
    nlo = (lo ^ (l1 | l2 | U(3))) & mlo
    nhi = (hi ^ (h1 | h2)) & mhi
    return nlo, nhi


def masks(k):
    if k <= 64:
        return U((1 << k) - 1) if k < 64 else U(0xFFFFFFFFFFFFFFFF), U(0)
    return U(0xFFFFFFFFFFFFFFFF), U((1 << (k - 64)) - 1) if k < 128 else U(0xFFFFFFFFFFFFFFFF)


p = 64
lo = np.array([0, 1], dtype=U); hi = np.zeros(2, dtype=U)
keep = {}
for k in range(1, 128):
    mlo, mhi = masks(k)
    ylo, yhi = lo.copy(), hi.copy()
    for _ in range(p):
        ylo, yhi = phi(ylo, yhi, mlo, mhi)
    ok = (ylo == lo) & (yhi == hi)
    lo, hi = lo[ok], hi[ok]
    if k in (63, 80, 100, 127):
        keep[k] = (lo.copy(), hi.copy())
    if k < 127:
        if k < 64:
            lo = np.concatenate((lo, lo | U(1 << k))); hi = np.concatenate((hi, hi))
        else:
            lo = np.concatenate((lo, lo)); hi = np.concatenate((hi, hi | U(1 << (k - 64))))
    if lo.size > 6_000_000:
        print('cap reached at level', k); break
print('survivors at level 127:', lo.size)
for depth, (L, H) in keep.items():
    vals = [int(a) | (int(b) << 64) for a, b in zip(L, H)]
    print(f'survival depth {depth:3d} ({len(vals)} nodes): ' + ' '.join(f'K={K}:{len(set(v & ((1 << K) - 1) for v in vals))}' for K in (16, 24, 32, 40)))
# cores: survivors at depth 127 that leave the rain within the first two digits
rain = [0x5555555555555555 | (0x5555555555555555 << 64), 0xAAAAAAAAAAAAAAAA | (0xAAAAAAAAAAAAAAAA << 64)]
L, H = keep[127]
vals = [int(a) | (int(b) << 64) for a, b in zip(L, H)]
def diverge(v):
    best = 0
    for r in rain:
        d = 0
        while d < 127 and ((v >> d) & 1) == ((r >> d) & 1):
            d += 1
        best = max(best, d)
    return best
dv = [diverge(v) for v in vals]
import collections
hist = collections.Counter(dv)
print('divergence depth from the rain (digits agreeing), histogram of the first 30 values:', sorted(hist.items())[:30])
cores = sorted(set(v & ((1 << 100) - 1) for v, d in zip(vals, dv) if d <= 2))
def evp(bits, max_off=40, max_per=48):
    for per in range(1, max_per + 1):
        for off in range(0, max_off + 1):
            if all(bits[i] == bits[i + per] for i in range(off, len(bits) - per)):
                return per, off
    return None
print(f'cores (leaving the rain within 2 digits), distinct to 100 digits: {len(cores)}')
for c in cores[:12]:
    bits = [(c >> i) & 1 for i in range(100)]
    print('  ', ''.join(map(str, bits[:80])), ' eventual period/offset over 100 digits:', evp(bits))
print('ETERNAL_CYCLES_128_DONE')
