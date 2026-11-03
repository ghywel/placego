#!/usr/bin/env python3
"""L1394 (Local, 2026-11-03): exact checks of GC2490 (one-sided endpoints, finite maxima, last-bit, separated blocks).
Run: python3 tests/probes/mahler/one_sided_check.py

O1 one-sided cut: terminating thresholds a = 13/27 (u = 101) and a = 1009/2187 (u = 1001001): G^(L-1)(X) = 2/3, and for
   y = X - delta (delta small, beta^L delta < 1 - X) G^L(y) = 1 - beta^L (X - y) > X, exactly.
O2 finite maxima of a nonterminating threshold: a = S_w = 27/65 (w = 1000, kappa = (1000)^inf) and a = S for w = 1001000:
   m_n = max tail of the n-digit truncation, n = 1..30: m_n < a, nondecreasing, A_n <= m_n, and each m_n satisfies the
   threshold criterion (all G-iterates of 2 m_n stay <= 2 m_n), so m_n is in E.
O3 right approach: for u = 101 (a = 13/27) and u = 1001001, append a 1 at N = L..L+12: the max tail v_N lies in
   [a + r^N/3, a + r^(N-L+1)/3], and satisfies the criterion while below 1/2.
O4 last bit: from u = 1001001 (T_w of w = 1001000), w = u with final 1 lowered satisfies the strict suffix predicate
   w_i.. < w_0.. for 1 <= i < L; wrap gap >= 4.
O5 separated blocks for a = 27/65: p_1 0^K_1 p_2 0^K_2 ... p_8 with r^(K_n + 1) < a - m_n: every tail of the finite word
   is < a, and each block root is >= A_n (the root of p_n alone), with A_n nondecreasing towards a. (A first version
   printed 'roots increase', which GC2490 does not claim; corrected before recording.)
"""
import math
from fractions import Fraction as F

beta = F(3, 2); r = F(2, 3); third = F(1, 3)


def G(x):
    y = beta * x
    return y - math.floor(y)


def tails(bits):
    n = len(bits)
    return [third * sum(r ** (k - j) for k in range(j, n) if bits[k]) for j in range(n)]


def in_E(a, steps=400):
    """Exact: True if the G-orbit of X = 2a reaches 0 or an exact rational cycle without exceeding X; False on an
    escape; None (UNKNOWN) at the cap. (Fixed after GC2492: the first version returned True at the cap.)"""
    X = 2 * a; x = X; seen = {X}
    for _ in range(steps):
        x = G(x)
        if x > X:
            return False
        if x == 0 or x in seen:
            return True
        seen.add(x)
    return None


def val(bits):
    return third * sum(r ** k for k, b in enumerate(bits) if b)


for u in ([1, 0, 1], [1, 0, 0, 1, 0, 0, 1]):
    a = val(u); X = 2 * a; L = len(u)
    x = X
    for _ in range(L - 1):
        x = G(x)
    d = (1 - X) / beta ** L / 7
    y = X - d; z = y
    for _ in range(L):
        z = G(z)
    print('O1 u = %s: a = %s; G^(L-1)(X) = %s; G^L(X - delta) = %s, formula %s, > X: %s' % (
        ''.join(map(str, u)), a, x, z, z == 1 - beta ** L * d, z > X))
for w in ([1, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0]):
    L = len(w); a = val(w) / (1 - r ** L)
    ok = in_E(a) is True; prev = None; good = True
    for n in range(1, 31):
        p = (w * 10)[:n]
        t = tails(p); m = max(t); A = t[0]
        good &= m < a and A <= m and (prev is None or m >= prev) and in_E(m) is True
        prev = m
    print('O2 w = %s: a = S_w = %s in E: %s; m_1..m_30 below a, nondecreasing, A_n <= m_n, each in E: %s; a - m_30 = %.3e' % (
        ''.join(map(str, w)), a, ok, good, float(a - prev)))
for u in ([1, 0, 1], [1, 0, 0, 1, 0, 0, 1]):
    a = val(u); L = len(u); good = True
    for N in range(L, L + 13):
        b = u + [0] * (N - L) + [1]
        v = max(tails(b))
        good &= a + r ** N / 3 <= v <= a + r ** (N - L + 1) / 3 and (v >= F(1, 2) or in_E(v) is True)
    print('O3 u = %s: v_N bounds and membership for N = L..L+12: %s' % (''.join(map(str, u)), good))
u = [1, 0, 0, 1, 0, 0, 1]; w = u[:-1] + [0]; L = len(w)
print('O4 u = 1001001 -> w = %s: strict suffix predicate %s; wrap gap %d' % (
    ''.join(map(str, w)), all(w[i:] < w[:L - i] for i in range(1, L)), L - max(i for i in range(L) if w[i])))
w = [1, 0, 0, 0]; a = F(27, 65); word = []; roots = []; good = True; As = []
for n in range(1, 13):
    p = (w * 10)[:n]
    m = max(tails(p)); As.append(tails(p)[0])
    K = n
    while r ** (K + 1) >= a - m:
        K += 1
    roots.append(len(word)); word += p + [0] * K
t = tails(word)
good = all(x < a for x in t)
ge = all(t[i] >= As[k] for k, i in enumerate(roots)) and all(As[k] <= As[k + 1] for k in range(len(As) - 1))
print('O5 separated blocks (12 blocks, %d digits): every tail < a: %s; block root >= A_n and A_n nondecreasing: %s; '
      'A_12 = %.6f, a = %.6f' % (len(word), good, ge, float(As[-1]), float(a)))
print('ONE_SIDED_DONE')
