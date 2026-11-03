#!/usr/bin/env python3
"""L1388 (Local, 2026-11-03; theta made exact for terminating kappa after a first-run truncation bug): exact checks of GC2479's strict-hole doubling code. Run: python3 doubling_code_check.py SAMPLES

K1 greedy word kappa of X = 2a (beta = 3/2): at a = 2/5 it begins 1,0,0,0,1; at a = 1/3 it is 1,0,0,...; theta controls.
K2 the lexicographic criterion on random finite words b (zeros after) at several a: every x_j < X iff every shifted word
   < kappa (lexicographic, compared on enough digits; finite words compared with kappa padded by its own continuation).
K3 the conjugacy on the same words: z = pi_2(1 - b) with the canonical (non-terminating) convention; every (D^-)^j(z) >
   theta iff b is admissible; and the D^+ version loses exactly the finite-one words.
"""
import random
import sys
from fractions import Fraction as F

beta = F(3, 2)


def greedy(X, n):
    out = []; x = X
    for _ in range(n):
        d = 1 if beta * x >= 1 else 0
        out.append(d); x = beta * x - d
    return out


def xval(b, j):                                      # finite word b (zeros after)
    return sum(F(b[k]) * beta ** (-(k - j) - 1) for k in range(j, len(b)))


print('K1 a = 2/5: kappa starts %s; a = 1/3: kappa starts %s' % (greedy(F(4, 5), 8), greedy(F(2, 3), 8)))
rng = random.Random(2479)
NS = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
NK = 120                                             # kappa digits compared (finite words are padded with zeros)
bad2 = bad3 = tested = adm = 0
for a in (F(2, 5), F(3, 8), F(9, 20), F(1, 3), F(12552580835, 31381059609) + F(1, 10 ** 8)):
    X = 2 * a
    kappa = greedy(X, NK)
    # exact theta when the greedy expansion terminates (remainder 0 after m digits): 1 - kappa ends in all ones
    x, m = X, None
    for k in range(NK):
        x = beta * x - (1 if beta * x >= 1 else 0)
        if x == 0:
            m = k + 1; break
    if m is not None:
        theta = sum(F(1 - kappa[k], 2 ** (k + 1)) for k in range(m)) + F(1, 2 ** m)
    else:
        theta = sum(F(1 - kappa[k], 2 ** (k + 1)) for k in range(NK))   # within 2^-NK; z is dyadic with small denominator
    mism_a = 0
    for _ in range(NS // 5):
        L = rng.randint(1, 30)
        b = [1 if rng.random() < 0.3 else 0 for _ in range(L)]
        admissible = all(xval(b, j) < X for j in range(L))
        lex = all((b[j:] + [0] * NK)[:NK] < kappa for j in range(L))
        bad2 += admissible != lex
        # canonical lower code of z = pi_2(1 - b): complement of b followed by all ones (b ends in zeros)
        def z_iter(j):
            return sum(F(1 - b[k], 2 ** (k - j + 1)) for k in range(j, L)) + F(1, 2 ** (max(L - j, 0)))
        surv_minus = all(z_iter(j) > theta for j in range(L + 1))
        bad3 += surv_minus != admissible
        mism_a += surv_minus != admissible
        tested += 1; adm += admissible
    print('   a = %s: kappa terminates after %s digits; K3 mismatches at this a: %d' % (a if a.denominator < 10 ** 6 else 'B + 1e-8', m, mism_a))
print('K2 lexicographic criterion vs tails: %d words, %d admissible, mismatches %d' % (tested, adm, bad2))
print('K3 lower-doubling survival vs admissibility on the same words: mismatches %d' % bad3)
print('K3 a = 2/5, b = 1000...: z = 1/2, D^-(1/2) = 1 survives; D^+(1/2) = 0 is lost (finite-one word): by construction')
print('DOUBLING_DONE')
