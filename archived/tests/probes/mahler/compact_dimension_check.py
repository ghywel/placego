#!/usr/bin/env python3
"""L1401 (Local, 2026-11-03): exact checks for the carrying read of GC2498 (direct word counts and compact dimension).
Run: python3 tests/probes/mahler/compact_dimension_check.py LMAX NMAX

For every w in W with |w| = L <= LMAX (start 1, end 0, every proper suffix strictly below the equal-length prefix,
S_w < 1/2), delta = w repeated, H_w = {x : every shift of x <= delta}:
D1 gamma: the root in (1, 3/2) of t^L - sum_(w_j = 1) t^(L-j-1) - 1, bracketed exactly by Fraction bisection;
   F_w(3/2) = 2 S_w exactly.
D2 N_n = #{p in {0,1}^n : every suffix of p <= the prefix of delta of the same length} (such p extend by zeros, so these
   are exactly the occurring prefixes), for n <= NMAX; checks N_n <= 1 + sum delta_j N_(n-j) and
   gamma^n <= N_n <= gamma^(n+L) (with the exact gamma bracket).
D3 the derivative comparison (gamma - 1)^2 R <= 3/2 - gamma <= (9/4) R with R = 1 - 2 S_w, and
   (beta - gamma)/(beta log beta) <= 1 - d_w <= (beta - gamma)/(gamma log beta).
D4 the cover's membership claim on known E points: for every pair v, w in the class with S_v <= S_w, the greedy code of
   2 S_v (= v repeated) and of 2 T_v (v with its last 0 raised to 1, then zeros) lies in H_w when T_v <= S_w; and
   whenever T_v is in (S_w, T_w] it is T_w itself (no E point inside an open band).
D5 the gap-2 control: w = 101000000 has polynomial value 217/512 at 3/2.
"""
import math
import sys
from fractions import Fraction as Fr

LMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 12
NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 16
r = Fr(2, 3)
beta = Fr(3, 2)


def words(L):
    for v in range(1 << (L - 2)):
        w = [1] + [(v >> i) & 1 for i in range(L - 2)] + [0]
        if all(w[i:] < w[:L - i] for i in range(1, L)):
            A = sum(r ** j for j in range(L) if w[j]) / 3
            S = A / (1 - r ** L)
            if S < Fr(1, 2):
                yield w, A, S, A + r ** (L - 1) / 3


def poly(w, t):
    L = len(w)
    return t ** L - sum(t ** (L - j - 1) for j in range(L) if w[j]) - 1


def gamma_bracket(w):
    lo, hi = Fr(1), beta
    assert poly(w, lo) < 0 < poly(w, hi)
    for _ in range(70):
        mid = (lo + hi) / 2
        if poly(w, mid) < 0:
            lo = mid
        else:
            hi = mid
    return lo, hi


def counts(delta, nmax):
    N = [1]
    level = [()]
    for n in range(1, nmax + 1):
        nxt = []
        for p in level:
            for b in (0, 1):
                q = p + (b,)
                if all(q[i:] <= tuple(delta[:n - i]) for i in range(n)):
                    nxt.append(q)
        level = nxt
        N.append(len(level))
    return N


cls = [x for L in range(2, LMAX + 1) for x in words(L)]
print('D0 %d words in the class with |w| <= %d' % (len(cls), LMAX))
bad = {'F': 0, 'rec': 0, 'low': 0, 'up': 0, 'der': 0, 'dim': 0}
worst_up = 0.0
for w, A, S, T in cls:
    L = len(w)
    F_beta = sum(w[j] * beta ** (-j - 1) for j in range(L)) / (1 - beta ** (-L))
    bad['F'] += F_beta != 2 * S
    glo, ghi = gamma_bracket(w)
    delta = (w * ((NMAX // L) + 2))[:NMAX + L]
    N = counts(delta, NMAX)
    for n in range(1, NMAX + 1):
        bad['rec'] += N[n] > 1 + sum(delta[j - 1] * N[n - j] for j in range(1, n + 1))
        bad['low'] += glo ** n > N[n]
        bad['up'] += N[n] > ghi ** (n + L)
        worst_up = max(worst_up, float(N[n] / glo ** (n + L)))
    R = 1 - 2 * S
    bad['der'] += not ((glo - 1) ** 2 * R <= beta - glo and beta - ghi <= Fr(9, 4) * R)
    g = float(glo); b = 1.5
    d = math.log(g) / math.log(b)
    bad['dim'] += not ((b - g) / (b * math.log(b)) - 1e-12 <= 1 - d <= (b - g) / (g * math.log(b)) + 1e-12)
print('D1 F_w(3/2) == 2 S_w exactly: %d failures' % bad['F'])
print('D2 recursion inequality failures %d; gamma^n <= N_n failures %d; N_n <= gamma^(n+L) failures %d (n <= %d); '
      'max N_n / gamma^(n+L) = %.4f' % (bad['rec'], bad['low'], bad['up'], NMAX, worst_up))
print('D3 derivative comparison failures %d; exponent-deficit bracket failures %d' % (bad['der'], bad['dim']))


def greedy_code(X, n):
    out = []
    for _ in range(n):
        y = beta * X
        d = 1 if y >= 1 else 0
        out.append(d); X = y - d
    return out


def in_H(code, delta):
    n = len(code)
    return all(tuple(code[i:]) <= tuple(delta[:n - i]) for i in range(n))


memb = viol = inside = 0
LEN = 40
for v, Av, Sv, Tv in cls:
    cs = greedy_code(2 * Sv, LEN); ct = greedy_code(2 * Tv, LEN)
    assert cs == (v * (LEN // len(v) + 1))[:LEN]
    for w, Aw, Sw, Tw in cls:
        delta = (w * (LEN // len(w) + 2))[:LEN]
        if Sv <= Sw:
            memb += 1; viol += not in_H(cs, delta)
        if Tv <= Sw:
            memb += 1; viol += not in_H(ct, delta)
        if Sw < Tv <= Tw and Tv != Tw:
            inside += 1
print('D4 %d membership checks of E points below S_w (codes of 2S_v and 2T_v, first %d digits): %d violations; '
      'T_v strictly inside an open band (S_w, T_w): %d' % (memb, LEN, viol, inside))
w9 = [1, 0, 1, 0, 0, 0, 0, 0, 0]
print('D5 gap-2 word: polynomial at 3/2 = %s; in class: %s' % (poly(w9, beta), any(x[0] == w9 for x in cls)))
print('COMPACT_DIMENSION_DONE')
