#!/usr/bin/env python3
"""hybrid_wall_replay.py (Local, 10 November 2026; S-08 hybrid half): the plain-Python replay of the worked-numbers
cell of the hybrid-wall essay. Usage: python3 hybrid_wall_replay.py

Prediction (written before the first run): for the alternating 90/150 white-wall hybrid, with horizon 400, the rows of
width at most W that are black at depth 1 at every even time number 0, 1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32 for
W = 1..12; those of width at most 6 are 3, 11, 53, 61 (depth d at bit d - 1); the simulated immortal set equals the
cell-by-cell family BitFam (x1 = 1, x(4j+3) = x(4j+5), x(4j+2) = x(4j+1) + x(4j+3)) for every W <= 12; and the
decimation D(a, b) = (a_o, a_e + b_o) satisfies D(P(P x)) = P(D x), with P(a, b) = (a + b, T a), on all 4096 pairs of
polynomials of degree below 6. Counterfactual: a mismatch means the module's statement or the model is misread.
It prints {counts, width-six list, family equal, semiconjugacy holds}."""


def H(y):
    """One step on a row encoded as an integer, depth d at bit d - 1."""
    out = 0
    for i in range(y.bit_length() + 2):
        b = ((y >> (i + 1)) & 1) ^ (((y >> (i - 1)) & 1) if i >= 1 else 0) ^ (((y >> i) & 1) if i % 2 == 0 else 0)
        out |= b << i
    return out


def immortal(y, hor=400):
    for t in range(hor + 1):
        if t % 2 == 0 and not (y & 1):
            return False
        y = H(y)
    return True


def bitfam(y, W):
    x = lambda d: (y >> (d - 1)) & 1 if d >= 1 else 0
    return x(1) == 1 and all(x(4 * j + 3) == x(4 * j + 5) and x(4 * j + 2) == x(4 * j + 1) ^ x(4 * j + 3)
                             for j in range(W // 4 + 2))


imm = {W: [y for y in range(1 << W) if immortal(y)] for W in range(1, 13)}
counts = [len(imm[W]) for W in range(1, 13)]
fam = all(set(imm[W]) == {y for y in range(1 << W) if bitfam(y, W)} for W in range(1, 13))


def T(q):
    return q << 1


def dec(q, r):
    out, i = 0, 0
    while q >> (2 * i + r):
        out |= ((q >> (2 * i + r)) & 1) << i
        i += 1
    return out


def P(x):
    a, b = x
    return (a ^ b, T(a))


def D(x):
    a, b = x
    return (dec(a, 1), dec(a, 0) ^ dec(b, 1))


semi = all(D(P(P((a, b)))) == P(D((a, b))) for a in range(64) for b in range(64))
print('{{%s}, {%s}, %s, %s}' % (', '.join(map(str, counts)), ', '.join(map(str, imm[6])), fam, semi))
