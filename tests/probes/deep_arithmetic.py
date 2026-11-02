#!/usr/bin/env python3
"""L1290 (Local, 2026-11-02): the arithmetic behind the ancestry front. Predictions P10a-P10f in
reports/rule30-genealogy.md section 24.2, written first. Run: python3 tests/probes/deep_arithmetic.py  (under a minute)

Phi(x) = x XOR ((x << 1) OR (x << 2) OR 3) on 2-adic integers, bit 0 = the cell just behind the front (GC2356).
"""
import numpy as np


def Phi(x):
    return x ^ ((x << 1) | (x << 2) | 3)


def v2(n):
    return (n & -n).bit_length() - 1


# P10a: the Syracuse form on the seed, exact integers
T = 5000
W = 2 * T + 9
C = T + 4
row = np.zeros(W, dtype=bool); row[C] = True
row = np.concatenate(([False], row[:-2] ^ (row[1:-1] | row[2:]), [False]))
B, t = -1, 1
episodes = fails = len_fails = 0
dD, dB = [], []
while t < T - 10:
    u, Bu = t, B
    cells = row[C - u:C + Bu][::-1]                      # B-1, B-2, ..., -u  -> bit 0 first
    w = int(''.join('1' if c else '0' for c in cells[::-1]), 2) if cells.size else 0
    if w.bit_length() != Bu + u:
        len_fails += 1
    q = int(np.flatnonzero(row[C + Bu + 1:])[0]); r = q // 2
    for _ in range(r + 1):
        row = np.concatenate(([False], row[:-2] ^ (row[1:-1] | row[2:]), [False]))
    v = u + r + 1
    Bn = int(np.flatnonzero(row[:C + Bu + r + 2]).max()) - C
    y = w
    for _ in range(r):
        y = Phi(y)
    L = 1 + v2(y + 1)
    pred = Phi(y) >> L
    cells2 = row[C - v:C + Bn][::-1]
    actual = int(''.join('1' if c else '0' for c in cells2[::-1]), 2) if cells2.size else 0
    if pred != actual or Bn != Bu + r - (L - 1):
        fails += 1
    dD.append(2 * (r + 1) - L); dB.append(r - (L - 1))
    episodes += 1
    t, B = v, Bn
print(f'P10a: {episodes} episodes to t = {t}: Syracuse form reproduces the whole next deep word (exact integers) with {fails} failures; '
      f'bit length = B(u) + u at every start: {len_fails} failures')

# P10b
bad = sum(1 for x in range(1, 1 << 16) if Phi(x).bit_length() != x.bit_length() + 2)
print(f'P10b: x in [1, 2^16): Phi adds exactly 2 to the bit length except in {bad} cases')


# cycle types
def cycles(perm):
    n = len(perm); seen = np.zeros(n, dtype=bool); lens = []
    for s in range(n):
        if not seen[s]:
            L = 0; x = s
            while not seen[x]:
                seen[x] = True; x = perm[x]; L += 1
            lens.append(L)
    return sorted(lens, reverse=True)


phi3 = [Phi(x) & 7 for x in range(8)]
t3 = cycles(phi3)
affine = {}
for a in (1, 3, 5, 7):
    for b in range(8):
        affine[(a, b)] = cycles([(a * x + b) & 7 for x in range(8)])
match = [ab for ab, ty in affine.items() if ty == t3]
print(f'P10c: Phi on Z/8 has cycle type {t3}; affine maps x -> ax+b with that type: {match}; '
      f'affine types seen: {sorted(set(tuple(v) for v in affine.values()))}')

# P10d: orbit of 0
first = None
x, y = 0, 0
for n in range(1, 4096):
    x = Phi(x); y = 3 * y + 3
    for k in range(1, 20):
        if (x - y) % (1 << k):
            if first is None or k < first[0]:
                first = (k, n)
            break
agree8 = all(((Phi_n - A_n) % 8 == 0) for Phi_n, A_n in [(0, 0)])
xs, ys = [0], [0]
for n in range(64):
    xs.append(Phi(xs[-1])); ys.append(3 * ys[-1] + 3)
print(f'P10d: orbit of 0 under Phi vs 3x+3: first disagreement at modulus 2^{first[0]}, step n = {first[1]}; '
      f'agree mod 8 for n <= 64: {all((a - b) % 8 == 0 for a, b in zip(xs, ys))}; first values Phi: {xs[:6]}, 3x+3: {ys[:6]}')

# P10e: cycle structure by level
print('P10e: Phi on Z/2^k: k, number of cycles, longest, G249 bound 2^ceil((2k-1)/3), all lengths powers of 2, lengths histogram (length: count)')
for k in range(1, 21):
    n = 1 << k
    xs = np.arange(n, dtype=np.int64)
    perm = (xs ^ ((xs << 1) | (xs << 2) | 3)) & (n - 1)
    ls = cycles(perm)
    bound = 1 << -(-(2 * k - 1) // 3)
    from collections import Counter
    h = Counter(ls)
    pow2 = all(l & (l - 1) == 0 for l in ls)
    orbit0 = 1; z = int(perm[0])
    while z != 0:
        z = int(perm[z]); orbit0 += 1
    print(f'  k={k:2d}: cycles {len(ls):6d}, longest {ls[0]:6d}, bound {bound:6d}, orbit of 0 {orbit0:6d}, powers of 2 {pow2}; '
          + ' '.join(f'{l}:{c}' for l, c in sorted(h.items())))

# P10f
dD = np.array(dD); dB = np.array(dB)
print(f'P10f: per episode on the seed: mean change of D (bit length) {dD.mean():.4f}, of B {dB.mean():.4f}; '
      f'Collatz Syracuse step for random n: log2(3) - 2 = {np.log2(3) - 2:.4f} bits')
print('DEEP_ARITHMETIC_DONE')
