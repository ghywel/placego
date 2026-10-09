#!/usr/bin/env python3
"""Bounded instrument audit of GC665--GC667, not a Z-number search.

PREDICTIONS (before first run): exact predecessor white gates agree for
n=0..11 and fractions 0,1/5,1/4,1/3,2/5. Actual signed rounded-map bits
agree with repeat divisibility for n=-8..32, q=1..4, k=1..3, and the
first disagreement occurs at v2(M) when M is nonzero.
COUNTERFACTUAL: the inverse gate can use u<=1/4; x=33/4 must reject it.
UNEXPECTED: retain signed/zero cycle exceptions and nonprimitive words.
No older instrument is imported. Finite checks do not prove asymptotics.
OUTCOME at preregistration: NOT RUN.
ADDENDUM first run: PASS, 60 predecessor gates, 3690 repeat membership
checks, 1222 first-disagreement checks, 8 cycle exceptions, 960 positive
height budgets. Quarter-boundary, nonprimitive and sparse-code controls pass.
"""
from fractions import Fraction
from itertools import product


def frac(x):
    return x - x.numerator // x.denominator


def direct_bits(n, length):
    bits = []
    for _ in range(length):
        bits.append(n % 2)
        n = (3 * n + 1) // 2
    return bits


def valuation(m):
    assert m != 0
    m = abs(m)
    v = 0
    while m % 2 == 0:
        v += 1
        m //= 2
    return v


def main():
    predecessor = 0
    for n in range(12):
        for u in map(Fraction, [0, Fraction(1, 5), Fraction(1, 4),
                                Fraction(1, 3), Fraction(2, 5)]):
            white = frac(2 * (n + u) / 3) < Fraction(1, 2)
            gate = n % 3 == 0 or (n % 3 == 2 and u < Fraction(1, 4))
            assert white == gate, (n, u)
            predecessor += 1
    assert frac(Fraction(33, 4) * Fraction(2, 3)) == Fraction(1, 2)

    membership = prefixes = cycles = budgets = 0
    for q in range(1, 5):
        for word in product((0, 1), repeat=q):
            c = 0
            for j, bit in enumerate(word):
                c = 3 * c + bit * 2**j
            delta = 3**q - 2**q
            assert 0 <= c <= delta
            for n in range(-8, 33):
                m = delta * n + c
                for k in range(1, 4):
                    actual = direct_bits(n, k * q) == list(word) * k
                    assert actual == (m % 2**(k * q) == 0), (n, word, k)
                    membership += 1
                if m == 0:
                    assert n <= 0
                    cycles += 1
                    continue
                v = valuation(m)
                bits = direct_bits(n, v + 1)
                assert all(bits[j] == word[j % q] for j in range(v))
                assert bits[v] != word[v % q]
                prefixes += 1
                if n >= 1:
                    assert m > 0
                    assert 2**v <= m < 3**q * (n + 1)
                    budgets += 1

    assert direct_bits(16, 7) == [0, 0, 0, 0, 1, 0, 1]
    assert 3**65 * 2**16 < 2**(65 + 55)
    assert Fraction(1, 3) / (1 - Fraction(2, 3)**3) == Fraction(9, 19)
    print('PASS predecessor=%d membership=%d first_disagreement=%d '
          'cycles=%d positive_budgets=%d' %
          (predecessor, membership, prefixes, cycles, budgets))


if __name__ == '__main__':
    main()
