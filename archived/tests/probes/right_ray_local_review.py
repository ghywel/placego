#!/usr/bin/env python3
"""right_ray_local_review.py (Local, L1518): an independent brute-force test of GC2657-GC2667's right-ray claims, written from the
report's prose without reading GPT's probes. Observer tick u reads wheel u // 2 of the row u ticks after launch.

Predictions, written before the first run:
  T1  the two white-interval equivalences hold exhaustively on small rows.
  T2  the launch table at wheel 9 holds exactly.
  T3  the delayed black reaches every chosen repeat i < m at age 6m.
  T4  block_iff_return and next_record hold at every launch.
  T5  extra white occurs at some launch exactly when the larger clock doubles.
  T6  GC2667: for every J >= 4 the h-sample window certifies a low-J return, and the stated colour at the next sample occurs
      at some launch exactly when the clock doubles at J. This is the hand extension: the test that could fail.
  T7  the complete movies separate every odd low state at d = 8 and d = 10, and the top-cell counts are 126 and 510.
Counterfactual: any mismatch is a finding against the report. Nothing here proves an all-depth statement."""
import sys, time
import numpy as np

def phi(x): return x ^ ((2 * x) | (4 * x))
def bit(x, j): return (x >> j) & 1 if j >= 0 else 0
t0 = time.time()

# T1
bad = 0; tested = 0
for n in range(0, 8):
    for m in range(1, 4):
        W = n + m + 3
        lo = max(0, n - 3 * m + 1); hi = n + m - 1
        mask = 0
        for j in range(lo, hi + 1): mask |= 1 << j
        lo2 = max(0, n - 3 * m); hi2 = n + m
        mask2 = 0
        for j in range(lo2, hi2 + 1): mask2 |= 1 << j
        for x in range(1 << W):
            r = x; white = True
            for tau in range(2 * m):
                if bit(r, n + tau // 2): white = False; break
                r = phi(r)
            tested += 1
            if white != ((x & mask) == 0): bad += 1
            # 2m + 1 readings starting with a repeat of wheel n: tau = 0 reads n, then pairs from n + 1
            r = x; white2 = True
            for tau in range(2 * m + 1):
                if bit(r, n + (tau + 1) // 2): white2 = False; break
                r = phi(r)
            tested += 1
            if white2 != ((x & mask2) == 0): bad += 1
print('T1 white intervals: cases', tested, 'mismatches', bad)

# the singleton on a register
def orbit(width, n):
    M = (1 << width) - 1
    x = 1; out = [1]
    for _ in range(n):
        x = phi(x) & M; out.append(x)
    return out
def period(width):
    M = (1 << width) - 1
    x = phi(1) & M; p = 1
    while x != 1:
        x = phi(x) & M; p += 1
    return p
print('periods of the low J bits, J = 1..22:', [period(J) for J in range(1, 23)])

# T2
big = orbit(40, 300)
for s, want in ((50, ['01']), (48, ['00', '01']), (47, ['00', '00', '01']), (46, ['00', '00', '00'])):
    got = []
    for i in range(len(want)):
        w = 9 + i
        got.append(str(bit(big[s + 2 * w], w)) + str(bit(big[s + 2 * w + 1], w)))
    print('T2 launch', s, got, 'as stated' if got == want else 'DIFFERS from ' + str(want))

# T3
ok3 = 0; n3 = 0
for m in range(1, 7):
    W = 4 * m + 3; P = period(W); rows = orbit(W, 2 * P)
    for i in range(m):
        e = (3 * m - 3 * i - 1) // 2
        s = (e - 6 * m) % P
        pairs = [(bit(rows[s + 6 * m + 2 * k], 3 * m + k), bit(rows[s + 6 * m + 2 * k + 1], 3 * m + k)) for k in range(i + 1)]
        n3 += 1
        ok3 += all(p == (0, 0) for p in pairs[:i]) and pairs[i] == (0, 1)
print('T3 delayed black at repeat i of m: ', ok3, 'of', n3)

# T4, T5
for m in range(1, 6):
    W = 4 * m + 1; P = period(W); PL = period(4 * m)
    rows = orbit(W, 2 * P + 8 * m + 4)
    Ml = (1 << (4 * m)) - 1
    badr = badn = 0; extra = 0
    for s in range(P):
        c = rows[s + 6 * m]
        wh = all(bit(rows[s + 6 * m + u], 3 * m + u // 2) == 0 for u in range(2 * m))
        ret = (c & Ml) == 1
        badr += wh != ret
        if wh:
            nxt = bit(rows[s + 8 * m], 4 * m)
            badn += (nxt == 0) != (bit(c, 4 * m) == 1)
            extra += nxt == 0
    print(f'T4/T5 m={m}: block_iff_return mismatches {badr}, next_record mismatches {badn}; P(4m)={PL} P(4m+1)={P}; extra white at some launch {extra > 0}, doubled {P == 2 * PL}')

# T6
fails = 0
for J in range(4, 21):
    h = J // 2
    W = J + 1; P = period(W); PL = period(J)
    M = (1 << W) - 1
    rows = np.empty(P + 2 * J + 2, dtype=np.int64)
    x = 1
    for k in range(len(rows)):
        rows[k] = x; x = phi(x) & M
    s = np.arange(P)
    white = np.ones(P, dtype=bool)
    for u in range(2 * J - h, 2 * J):
        white &= ((rows[s + u] >> (u // 2)) & 1) == 0
    start = rows[s + 2 * J - h]
    ret = (start & ((1 << J) - 1)) == 1
    a = int((white != ret).sum())
    nxt = (rows[s + 2 * J] >> J) & 1
    topbit = (start >> J) & 1
    want = (nxt == 0) if J % 2 == 0 else (nxt == 1)
    b = int((want[white] != (topbit[white] == 1)).sum())
    colour = bool((want & white).any())
    doubled = P == 2 * PL
    fails += a + b + (colour != doubled)
    print(f'T6 J={J}: window vs return mismatches {a}; colour vs top bit mismatches {b}; colour at some launch {colour}; doubled {doubled}; returns {int(white.sum())} of {P}')
print('T6 total failures', fails)

# T7, and beyond the report's two depths
for d in (8, 10, 12, 14, 16):
    n = 1 << (d - 1)
    M = (1 << d) - 1
    x = (np.arange(n, dtype=np.uint64) * 2 + 1)
    hU = np.zeros(n, dtype=np.uint64); hF = np.zeros(n, dtype=np.uint64); hF2 = np.zeros(n, dtype=np.uint64)
    A = np.uint64(0x9E3779B97F4A7C15); B = np.uint64(0xC2B2AE3D27D4EB4F)
    for t in range(1 << (d - 1)):
        U = (x >> np.uint64(d - 1)) & np.uint64(1)
        V = U | ((x >> np.uint64(d - 2)) & np.uint64(1))
        hU = hU * A + U + np.uint64(1)
        code = U * np.uint64(2) + V + np.uint64(1)
        hF = hF * A + code
        hF2 = hF2 * B + code
        x = (x ^ ((x * np.uint64(2)) | (x * np.uint64(4)))) & np.uint64(M)
    full = len(set(zip(hF.tolist(), hF2.tolist())))
    print(f'T7 d={d}: odd states {n}, distinct top-cell movies {len(set(hU.tolist()))}, distinct full movies {full}')
print('seconds', round(time.time() - t0, 1))
