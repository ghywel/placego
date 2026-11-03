#!/usr/bin/env python3
"""L1389 (Local, 2026-11-03): exact checks of GC2481's strict Lyndon interval and gap-word constructor.
Run: python3 tests/probes/mahler/lyndon_constructor_check.py SAMPLES

For gap tuples g = (3,4), (3,5,4), (4,11,6,5), (4,6), (5,7,6) (first gap uniquely shortest, d >= 3):
L1 s = 1 - w satisfies the strict proper-suffix comparison; ell = pi(s), rho = pi(s^inf); for (3,4): S = 945/2059,
   T = 1009/2187, ell = 55/128, rho = 55/127.
L2 the left witnesses z_N = pi((q 1^N)^inf), N = L..L+3: z_N is the minimum of its rotations, z_N = (ell - p_N)/(1 - p_N),
   z_N < ell, increasing in N.
L3 boundary guards: max tail of w^inf (geometric) is S_w at the root; max tail of w^+ 0^inf is T_w at the root; both < 1/2.
L4 G51's window for the finite word w (C_t recurrence): [C_L/3^L, min_t (C_t + 2^(t-1))/3^t) equals [A_w, T_w), S_w inside.
L5 the constructor language on random finite words at a = midpoint of (S_w, T_w] and a = T_w: "every tail < a" iff every
   shift <= w^inf (lexicographic), iff no forbidden block (w_0..w_(j-1) 1 for each zero j of w).
"""
import random
import sys
from fractions import Fraction as F

r = F(2, 3); third = F(1, 3)


def word_of(g):
    L = sum(g); w = [0] * L; p = 0
    for x in g[:-1]:
        w[p] = 1; p += x
    w[p] = 1
    return w


def pi2(bits):
    return sum(F(b, 2 ** (k + 1)) for k, b in enumerate(bits))


def tails_finite(b):
    return [third * sum(r ** (k - j) for k in range(j, len(b)) if b[k]) for j in range(len(b))]


rng = random.Random(2481)
NS = int(sys.argv[1]) if len(sys.argv) > 1 else 400
allok = True
for g in ((3, 4), (3, 5, 4), (4, 11, 6, 5), (4, 6), (5, 7, 6)):
    w = word_of(list(g)); L = len(w); m = len(g)
    s = [1 - x for x in w]
    lyn = all(s[i:] > s[:L - i] for i in range(1, L))
    ell = pi2(s); rho = ell / (1 - F(1, 2 ** L))
    A = third * sum(r ** k for k in range(L) if w[k])
    S = A / (1 - r ** L); T = A + r ** (L - 1) / 3
    q = s[:-1] + [0]
    l2 = True; prev = None
    for N in range(L, L + 4):
        per = q + [1] * N
        rots = [pi2((per[i:] + per[:i]) * 3) for i in range(len(per))]          # 3 periods suffice for ordering
        zN = pi2(per) / (1 - F(1, 2 ** len(per)))
        pN = F(1, 2 ** (L + N))
        l2 &= rots.index(min(rots)) == 0 and zN == (ell - pN) / (1 - pN) and zN < ell and (prev is None or zN > prev)
        prev = zN
    # max tail of w^inf: tails of the periodic word at each one, closed form
    per_tails = [third * sum(r ** ((k - j) % L) for k in range(L) if w[k]) / (1 - r ** L) for j in range(L) if w[j]]
    wplus = w[:-1] + [1]
    ft = tails_finite(wplus)
    l3 = max(per_tails) == per_tails[0] == S and max(ft) == ft[0] == T and S < F(1, 2) and T < F(1, 2)
    C = [F(0)]
    for t in range(L):
        C.append(3 * C[-1] + w[t] * 2 ** t)
    lo = C[L] / F(3) ** L
    hi = min([F(1, 2)] + [(C[t] + 2 ** (t - 1)) / F(3) ** t for t in range(1, L + 1)])
    l4 = lo == A and hi == T and lo < S < hi
    forb = [w[:j] + [1] for j in range(L) if w[j] == 0]
    winf = w * 80
    bad = 0
    for a in ((S + T) / 2, T):
        for _ in range(NS):
            n = rng.randint(1, 3 * L)
            b = [1 if rng.random() < 0.35 else 0 for _ in range(n)]
            if rng.random() < 0.5:                                              # bias towards the critical word
                b = (w * 3)[:rng.randint(1, 3 * L)] + b
            tails_ok = all(u < a for u in tails_finite(b))
            lex_ok = all((b[j:] + [0] * (len(winf)))[:len(winf)] <= winf for j in range(len(b)))
            blk_ok = not any(b[j:j + len(f)] == f for f in forb for j in range(len(b)))
            bad += not (tails_ok == lex_ok == blk_ok)
    ok = lyn and l2 and l3 and l4 and bad == 0
    allok &= ok
    extra = ''
    if g == (3, 4):
        extra = '; (3,4): S %s T %s ell %s rho %s' % (S, T, ell, rho)
    print('g=%s L=%d: Lyndon %s; left witnesses %s; boundary maxima %s; G51 window [A,T) with S inside %s; '
          'random words (2 x %d) mismatches %d%s' % (g, L, lyn, l2, l3, l4, NS, bad, extra))
print('all pass: %s' % allok)
print('LYNDON_DONE')
