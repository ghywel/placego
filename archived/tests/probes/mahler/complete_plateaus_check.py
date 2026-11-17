#!/usr/bin/env python3
"""L1397 (Local, 2026-11-03): exact checks of GC2494 (self-maximal guard, full word constructor, completeness controls).
Run: python3 tests/probes/mahler/complete_plateaus_check.py SAMPLES

P1 self-maximal guard: random finite words b (zeros after) that are lexicographically >= all their shifts and have
   X = 2 U_0 < 1: the root is the numerical maximum of all tails, and every 2 U_j < 1.
P2 identities: T_w - 1/2 = (1 - r^L)(S_w - 1/2) for random w, L = 2..20; S = C/(3^L - 2^L), T = (C + 2^(L-1))/3^L.
P3 the gap-2 example w = 101000000: strict suffix predicate; S = 9477/19171, T = 9733/19683, (T - S)/(T - A) = 217/19171;
   the band language: on random finite words at the band midpoint and at T, "every tail < a" iff every shift <= w^inf.
P4 critical expansion of 1: the first 60 greedy digits of z_0 = 1 have no final all-zero tail (each truncation's tail
   maximum e_n is < 1/2, increasing to 1/2), and the parity obstruction 3^(n+1) odd vs. even digit sum holds.
P5 right isolation on examples: a purely periodic threshold (w = 1000, a = 27/65) has no E point in (a, a + 10^-6] among
   the terminating candidates u0^inf with |u| <= 16; a terminating threshold (u = 1001001) has E points just above it
   (GC2490's v_N).
"""
import random
import sys
from fractions import Fraction as F

beta = F(3, 2); r = F(2, 3); third = F(1, 3)
rng = random.Random(2494)
NS = int(sys.argv[1]) if len(sys.argv) > 1 else 300


def tails(bits):
    n = len(bits)
    return [third * sum(r ** (k - j) for k in range(j, n) if bits[k]) for j in range(n)]


def selfmax(b):
    n = len(b)
    return all(b[j:] + [0] * j <= b for j in range(1, n))


tested = bad = 0
while tested < NS:
    b = [1] + [1 if rng.random() < 0.4 else 0 for _ in range(rng.randint(1, 18))]
    if not selfmax(b):
        continue
    t = tails(b)
    if 2 * t[0] >= 1:
        continue
    tested += 1
    bad += not (max(t) == t[0] and all(2 * x < 1 for x in t))
print('P1 self-maximal words with X < 1: %d tested, violations %d' % (tested, bad))
ok = True
for L in range(2, 21):
    for _ in range(5):
        w = [1] + [rng.getrandbits(1) for _ in range(L - 2)] + [0]
        A = third * sum(r ** j for j in range(L) if w[j]); S = A / (1 - r ** L); T = A + r ** (L - 1) / 3
        C = sum(2 ** j * 3 ** (L - 1 - j) for j in range(L) if w[j])
        ok &= T - F(1, 2) == (1 - r ** L) * (S - F(1, 2)) and S == F(C, 3 ** L - 2 ** L) and T == F(C + 2 ** (L - 1), 3 ** L)
print('P2 identities for L = 2..20: %s' % ok)
w = [1, 0, 1, 0, 0, 0, 0, 0, 0]; L = len(w)
A = third * sum(r ** j for j in range(L) if w[j]); S = A / (1 - r ** L); T = A + r ** (L - 1) / 3
s = [1 - x for x in w]
pred = all(s[i:] > s[:L - i] for i in range(1, L))
winf = w * 40; bad3 = 0
for a in ((S + T) / 2, T):
    for _ in range(NS):
        b = [1 if rng.random() < 0.3 else 0 for _ in range(rng.randint(1, 30))]
        if rng.random() < 0.5:
            b = (w * 3)[:rng.randint(1, 3 * L)] + b
        lhs = all(x < a for x in tails(b))
        rhs = all((b[j:] + [0] * len(winf))[:len(winf)] <= winf for j in range(len(b)))
        bad3 += lhs != rhs
print('P3 w = 101000000: suffix predicate %s; S = %s (%s), T = %s (%s), ratio = %s (%s); band language mismatches %d of %d' % (
    pred, S, S == F(9477, 19171), T, T == F(9733, 19683), (T - S) / (T - A), (T - S) / (T - A) == F(217, 19171), bad3, 2 * NS))
z = F(1); d = []
for _ in range(60):
    dg = 1 if beta * z >= 1 else 0
    d.append(dg); z = beta * z - dg
es = [max(tails(d[:n])) for n in range(1, 61) if any(d[:n])]
print('P4 critical expansion of 1: first digits %s; ones in 60 digits %d; e_n < 1/2 and nondecreasing: %s; 1/2 - e_60 = %.3e; '
      'parity check n = 0..59: %s' % (''.join(map(str, d[:24])), sum(d), all(e < F(1, 2) for e in es) and es == sorted(es),
                                     float(F(1, 2) - es[-1]), all((3 ** (n + 1)) % 2 == 1 for n in range(60))))


def in_E(a, steps=400):
    X = 2 * a; x = X; seen = {X}
    for _ in range(steps):
        y = beta * x; x = y - (y.numerator // y.denominator)
        if x > X:
            return False
        if x == 0 or x in seen:
            return True
        seen.add(x)
    return None


a = F(27, 65)
near = []
for n in range(2, 17):
    for v in range(1 << (n - 1)):
        u = [1] + [(v >> i) & 1 for i in range(n - 2)] + [1]
        val = third * sum(r ** j for j in range(n) if u[j])
        if a < val <= a + F(1, 10 ** 6) and in_E(val) is True:
            near.append(val)
print('P5 purely periodic a = 27/65: terminating E points in (a, a + 1e-6] with |u| <= 16: %d (isolated on the right predicts 0)' % len(near))
u = [1, 0, 0, 1, 0, 0, 1]; a2 = third * sum(r ** j for j in range(7) if u[j])
vs = [max(tails(u + [0] * (N - 7) + [1])) for N in range(7, 25)]
print('P5 terminating a = 1009/2187: E points just above, v_N - a for N = 20..24: %s; all in E: %s' % (
    ['%.2e' % float(v - a2) for v in vs[-5:]], all(in_E(v) is True for v in vs)))
print('COMPLETE_PLATEAUS_DONE')
