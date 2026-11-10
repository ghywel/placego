#!/usr/bin/env python3
"""cone_tip_replay.py (Local, 10 November 2026; S-17): the plain-Python replay of the worked-numbers cell of the
cone-tip essay. Usage: python3 cone_tip_replay.py

Prediction (written before the first run): in the zero-boundary left half of rule 30, with a_t(L) the cell at depth 1
and tick t, the second difference of a_t in the depths t - 1 and t equals (t - 1) mod 2 on every row of width at most
t + 1, for t = 2..14 (`cone_tip`); and for every even t <= 12 the largest normalised Walsh coefficient of a_t over the
rows of width at most t + 1 (its best correlation with an affine function) is at most 1/2, the corollary of
`face_disagree`. Counterfactual: one failing row refutes the cone-tip law. It prints
{law holds for t = 2..14, even-t correlations at most 1/2, the largest Walsh coefficient for t = 2..12 as fractions}.
"""
from fractions import Fraction


def tip(row, t):
    """Depth-1 cell at tick t from a row given as an integer, depth d at bit d - 1."""
    width = t + 2
    r = [0] + [(row >> (d - 1)) & 1 for d in range(1, width + 1)] + [0] * (t + 2)
    for _ in range(t):
        r = [0] + [r[k + 1] ^ (r[k] | r[k - 1]) for k in range(1, len(r) - 1)] + [0]
    return r[1]


def law(t):
    bt, bt1 = 1 << (t - 1), 1 << (t - 2)
    want = (t - 1) % 2
    return all(tip(y, t) ^ tip(y ^ bt, t) ^ tip(y ^ bt1, t) ^ tip(y ^ bt ^ bt1, t) == want
               for y in range(1 << (t + 1)))


def max_walsh(t):
    n = t + 1
    v = [1 - 2 * tip(y, t) for y in range(1 << n)]
    h = 1
    while h < len(v):
        for i in range(0, len(v), 2 * h):
            for j in range(i, i + h):
                a, b = v[j], v[j + h]
                v[j], v[j + h] = a + b, a - b
        h *= 2
    return Fraction(max(abs(x) for x in v), 1 << n)


laws = all(law(t) for t in range(2, 15))
walsh = [max_walsh(t) for t in range(2, 13)]
even_ok = all(w <= Fraction(1, 2) for t, w in zip(range(2, 13), walsh) if t % 2 == 0)
print('{%s, %s, {%s}}' % (laws, even_ok, ', '.join('%d/%d' % (w.numerator, w.denominator) for w in walsh)))
