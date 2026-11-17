#!/usr/bin/env python3
"""L1422 (Local, 2026-11-03): exact check for the carrying read of GC2522's seed-family extension.
Run: python3 tests/probes/b2_family_check.py N
For N random seeds in each class a = 419 or 3491 (mod 4096) with random higher bits (bits 12..40), the whole-prefix least
periods L0..L15 of the OR edge map, against the claimed 1,2,2,2,4,8,8,16,32,32,64,64,64,128,256 and d15 = 0; and for the
unequal-bit classes 419 + 1024 and 419 + 2048 (mod 4096), L13 = 64 as the report says. Also the retained 0x889da3 words R9..R12
over 64 ticks and their black counts.
"""
import random
import sys

N = int(sys.argv[1]) if len(sys.argv) > 1 else 200
T = 2048


def streams(seed, nbits):
    x = [(seed >> i) & 1 for i in range(nbits)]
    R = [[0] * T for _ in range(nbits)]
    for t in range(T):
        for i in range(nbits):
            R[i][t] = x[i]
        x = [x[i] ^ ((x[i - 1] if i >= 1 else 0) | (x[i - 2] if i >= 2 else 0)) for i in range(nbits)]
    return R


def prefix_periods(R):
    out = []
    for i in range(len(R)):
        p = 1
        while not all(R[k][t] == R[k][t + p] for k in range(i + 1) for t in range(T - p)):
            p *= 2
        out.append(p)
    return out


want = [1, 2, 2, 2, 4, 8, 8, 16, 32, 32, 64, 64, 64, 128, 256]
rng = random.Random(2522)
ok = {419: 0, 3491: 0}; d15 = {419: 0, 3491: 0}
for base in (419, 3491):
    for _ in range(N):
        a = base + 4096 * rng.getrandbits(29)
        L = prefix_periods(streams(a, 16))
        ok[base] += L[:15] == want
        d15[base] += L[15] == L[14]
print('classes 419 and 3491 (mod 4096), %d random seeds each: L0..L14 as claimed in %d and %d; d15 = 0 in %d and %d' % (
    N, ok[419], ok[3491], d15[419], d15[3491]))
une = {}
for base in (419 + 1024, 419 + 2048):
    c = 0
    for _ in range(N):
        a = base + 4096 * rng.getrandbits(29)
        L = prefix_periods(streams(a, 14))
        c += L[13] == 64 and L[:13] == want[:13]
    une[base] = c
print('unequal bits 10/11 (classes %d, %d): L0..L12 as claimed and L13 = 64 in %d and %d of %d' % (
    419 + 1024, 419 + 2048, une[419 + 1024], une[419 + 2048], N))
R = streams(0x889da3, 13)
for i in (9, 10, 11, 12):
    w = R[i][:64]
    print('0x889da3 R%d over 64 ticks: %016x, black %d' % (i, sum(b << t for t, b in enumerate(w)), sum(w)))
print('B2_FAMILY_DONE')
