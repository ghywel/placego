#!/usr/bin/env python3
"""G50 controls, NOT RUN at publication. Exact arithmetic, no data files.

Tests scope identities, not Mahler's conjecture.
"""
from fractions import Fraction as Q
from itertools import product


def g(x, y):
    return 3 * (x % 2) + y // 2


def f(x, y, z):
    return g(g(x, y), g(y, z))


def ma1():
    count = 0
    for x, y, z in product(range(6), repeat=3):
        expanded = 3 * ((3 * (x % 2) + y // 2) % 2) + (3 * (y % 2) + z // 2) // 2
        assert f(x, y, z) == expanded
        assert 0 <= f(x, y, z) < 6
        count += 1
    for y, z in product(range(6), repeat=2):
        assert len({f(x, y, z) for x in range(6)}) == 2
        for parity in (0, 1):
            assert len({f(x, y, z) for x in range(parity, 6, 2)}) == 1
    return count


def ma2():
    cases, applicable, boundary = 0, 0, 0
    for n, u in product(range(32), (Q(0), Q(1, 6), Q(1, 3), Q(1, 2))):
        x = (n + u) * Q(3, 2)
        observed_n = x.numerator // x.denominator
        observed_u = x - observed_n
        cases += 1
        if u == Q(1, 2):
            boundary += 1
            # Canonical first fractional base-six digit excludes 1/2.
            assert (6 * u).numerator // (6 * u).denominator == 3
            continue
        if observed_u < Q(1, 2):
            b = n % 2
            assert observed_n == (3 * n + b) // 2
            assert observed_u == (3 * u - b) / 2
            applicable += 1
    assert boundary == 32 and applicable > 0
    return cases, applicable, boundary


def ma3():
    tails = (Q(9, 19), Q(6, 19), Q(4, 19))
    for j, b in enumerate((1, 0, 0)):
        assert 0 <= tails[j] < Q(1, 2)
        assert (3 * tails[j] - b) / 2 == tails[(j + 1) % 3]
    for k in range(1, 13):
        modulus = 8 ** k
        r = (-9 * pow(19, -1, modulus)) % modulus
        n = r
        for _ in range(k):
            for b in (1, 0, 0):
                assert n % 2 == b
                n = (3 * n + b) // 2
        assert (19 * r + 9) % modulus == 0
        correction = 9 * (27 ** k - 8 ** k) // 19
        assert modulus * n == 27 ** k * r + correction
    assert Q(-9, 19) < 0 and Q(-9, 19).denominator != 1
    return 12


if __name__ == '__main__':
    print('MA1 PASS: local triples:', ma1())
    print('MA2 PASS: samples/applicable/excluded boundary:', ma2())
    print('MA3 PASS: fractional cycle and finite residue controls:', ma3())
    print('Infinite integer exclusion is an analytic divisibility argument; Mahler remains open.')
