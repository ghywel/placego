#!/usr/bin/env python3
"""L1425 (Local, 2026-11-03): exact check for the carrying read of GC2525 (C4's parity bridge). Run: python3 tests/probes/c4_parity_bridge_check.py N
Single black cell, whole-line Rule 30. For t = 2 .. N + 1: c_t = x(t, 0) equals the XOR over s < t of
O_t(s) = x(s, s - t + 1) OR x(s, s - t + 2) (the kit's center_eq_parity); with b(t) = floor(4t / 5), A_t = XOR over s < b(t)
and B_t = XOR over b(t) <= s < t, c_t = A_t XOR B_t; and sum chi(B) = D_0 + D_1, sum chi(c) = D_0 - D_1, with the measured
D_0, D_1 (COMPUTED values only, no balance inferred).
"""
import sys
import numpy as np

N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
T = N + 2
W = 2 * T + 4; c0 = T + 2
rows = np.zeros((T + 1, W), dtype=np.uint8); rows[0, c0] = 1
for t in range(T):
    r = rows[t]; n = np.zeros_like(r); n[1:-1] = r[:-2] ^ (r[1:-1] | r[2:]); rows[t + 1] = n
x = lambda s, j: int(rows[s, c0 + j])
ok_par = ok_split = 0; D = [0, 0]; sB = sC = 0
for t in range(2, N + 2):
    O = [x(s, s - t + 1) | x(s, s - t + 2) for s in range(t)]
    c = x(t, 0)
    ok_par += c == (sum(O) & 1)
    b = (4 * t) // 5
    A = sum(O[:b]) & 1; B = sum(O[b:]) & 1
    ok_split += c == (A ^ B)
    chiB = 1 - 2 * B; D[A] += chiB; sB += chiB; sC += 1 - 2 * c
print('t = 2 .. %d: centre = XOR of O_t (center_eq_parity) %d of %d; c = A XOR B %d of %d' % (N + 1, ok_par, N, ok_split, N))
print('sum chi(B) = %d = D0 + D1 = %d + %d: %s; sum chi(c) = %d = D0 - D1: %s' % (sB, D[0], D[1], sB == D[0] + D[1], sC, sC == D[0] - D[1]))
print('C4_BRIDGE_DONE')
