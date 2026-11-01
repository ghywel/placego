#!/usr/bin/env python3
"""L1285 T7 (Local, 2026-11-01): three ancestries from the seed's left edge, Rule 30, rows to t = 3000.
Predictions in reports/rule30-genealogy.md section 19.3, written first. Run: python3 tests/probes/genealogy_gate_seed.py

Left-edge coordinates a_j(t) = x_(-t+j)(t); child j has parents (j-2, j-1, j) at the previous time, left to right.
  V0  all black parents (GC2357);
  V1  sensitive parents of any colour: left always; centre iff the right parent is white; right iff the centre is white;
  V2  black parents that are sensitive.
Marks start at the edge cell at time 1. Reported: orphan share (black children of 011) in the bulk; the marked fronts
D0, D1, D2; per-diagonal capture (last time with an unmarked cell on diagonal j, j <= 60) for V1 and V2.
"""
import numpy as np

T = 3000
W = 3 * T + 12
C = T + 4
rows = np.zeros((T + 1, W), dtype=np.uint8)
rows[0, C] = 1
for t in range(T):
    rows[t + 1, 1:-1] = rows[t, :-2] ^ (rows[t, 1:-1] | rows[t, 2:])
JW = 2 * T + 2


def diag(t):
    return rows[t, C - t: C - t + JW]


m0 = np.zeros(JW, dtype=np.uint8); m0[0] = 1
m1 = np.zeros(JW, dtype=np.uint8); m1[0] = 1
m2 = np.zeros(JW, dtype=np.uint8); m2[0] = 1
JM = 61
last_un = {k: np.full(JM, -1) for k in (0, 1, 2)}
D = {k: [] for k in (0, 1, 2)}
orph_black = orph_all = 0
for t in range(1, T):
    a = diag(t)
    a1 = diag(t + 1)
    L = np.concatenate(([0, 0], a[:-2]))          # left parent of index j is index j-2
    Cn = np.concatenate(([0], a[:-1]))            # centre parent: index j-1
    R = a                                         # right parent: index j
    sL = np.ones_like(a)                          # sensitivities
    sC = (R == 0).astype(np.uint8)
    sR = (Cn == 0).astype(np.uint8)
    pL = np.concatenate(([0, 0], m0[:-2])); pC = np.concatenate(([0], m0[:-1])); pR = m0
    n0 = a1 & (pL | pC | pR)
    pL = np.concatenate(([0, 0], m1[:-2])); pC = np.concatenate(([0], m1[:-1])); pR = m1
    n1 = (pL & sL) | (pC & sC) | (pR & sR)       # any colour
    pL = np.concatenate(([0, 0], m2[:-2])); pC = np.concatenate(([0], m2[:-1])); pR = m2
    n2 = a1 & ((pL & sL) | (pC & sC) | (pR & sR))
    m0, m1, m2 = n0, n1, n2
    for k, m in ((0, m0), (1, m1), (2, m2)):
        D[k].append(int(np.flatnonzero(m).max()))
        if k == 1:
            un = np.flatnonzero(m[:JM] == 0)      # V1 capture: every cell, any colour
        else:
            un = np.flatnonzero((a1[:JM] == 1) & (m[:JM] == 0))
        last_un[k][un] = t + 1
    if t >= 1000:
        lo, hi = t // 2, 3 * t // 2              # bulk in left-edge coordinates
        blk = a1[lo:hi] == 1
        o = blk & (L[lo:hi] == 0) & (Cn[lo:hi] == 1) & (R[lo:hi] == 1)
        orph_black += int(blk.sum()); orph_all += int(o.sum())
print(f'orphans (black children of 011) among bulk black cells, rows 1001..{T}: {orph_all / orph_black:.4f}')
for k, name in ((0, 'V0 all black parents'), (1, 'V1 sensitive, any colour'), (2, 'V2 black and sensitive')):
    d = np.array(D[k])
    print(f'{name}: marked front D(t) at t = 100, 1000, 2000, 3000: {[int(d[i - 2]) for i in (100, 1000, 2000, 3000)]}; '
          f'D(t) = 2t at every step: {bool(np.all(d == 2 * np.arange(2, T + 1)))}; D(t) = 0 from t = '
          f'{next((i + 2 for i in range(len(d)) if np.all(d[i:] == 0)), None)}')
lu = last_un[2]
print(f'V2 per-diagonal: last time with an unmarked black cell, j = 0..12: {lu[:13].tolist()}; diagonals 1..60 with unmarked black after t = 2000: '
      f'{int(np.sum(lu[1:] > 2000))} of 60')
lu = last_un[1]
ev = [int(j) for j in range(JM) if lu[j] <= 2000]
print(f'V1 per-diagonal (every cell): captured by t = 2000: {ev}; not captured: {[int(j) for j in range(JM) if lu[j] > 2000]}')
print(f'    last unmarked time at j = 1, 3, 5, 7, 9, 11: {[int(lu[j]) for j in (1, 3, 5, 7, 9, 11)]}; even j <= 60 all captured by time j/2 + 1: '
      f'{bool(all(lu[j] <= j // 2 + 1 for j in range(0, JM, 2)))}')
print('GENEALOGY_GATE_SEED_DONE')
