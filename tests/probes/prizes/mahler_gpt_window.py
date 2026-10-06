#!/usr/bin/env python3
"""G51 exact controls. NOT RUN at publication. No data files or conjecture claim."""
from fractions import Fraction as Q
from itertools import product


def prefix_window(bits):
    correction = 0
    lower, upper = Q(0), Q(1, 2)
    for j, b in enumerate(bits):
        correction = 3 * correction + b * 2 ** j
        t = j + 1
        lower = max(lower, Q(correction, 3 ** t))
        upper = min(upper, Q(correction + 2 ** (t - 1), 3 ** t))
    return lower, upper, correction


def backward_window(bits):
    lower, upper = Q(0), Q(1, 2)
    for b in reversed(bits):
        if lower >= upper:
            return None
        lower = max(Q(0), (b + 2 * lower) / 3)
        upper = min(Q(1, 2), (b + 2 * upper) / 3)
    return (lower, upper) if lower < upper else None


def controls():
    comparisons, trajectories = 0, 0
    for t in range(11):
        modulus = 2 ** t
        for bits in product((0, 1), repeat=t):
            lower, upper, correction = prefix_window(bits)
            interval = (lower, upper) if lower < upper else None
            assert interval == backward_window(bits)
            r = (-correction * pow(3 ** t, -1, modulus)) % modulus if t else 0
            # Check the integer itinerary even when the fractional window is empty.
            n = r
            for b in bits:
                assert n % 2 == b
                n = (3 * n + b) // 2
            assert modulus * n == 3 ** t * r + correction
            comparisons += 1
            if interval is None:
                continue
            u = (lower + upper) / 2
            for lift in (0, 1):
                start = r + modulus * lift
                x, integer = start + u, start
                for j in range(t + 1):
                    observed_integer = x.numerator // x.denominator
                    assert observed_integer == integer
                    assert 0 <= x - observed_integer < Q(1, 2)
                    if j < t:
                        b = integer % 2
                        assert b == bits[j]
                        integer = (3 * integer + b) // 2
                        x *= Q(3, 2)
                trajectories += 1
    word = (1, 0, 1, 0, 1)
    assert all(a + b < 2 for a, b in zip(word, word[1:]))
    lower, upper, _ = prefix_window(word)
    assert lower == Q(133, 243) and lower >= upper
    print('MW1/MW2 PASS: word comparisons, midpoint trajectories:', comparisons, trajectories)
    print('MW3 PASS: 10101 avoids 11 but its fractional window is empty.')
    print('Finite controls only; infinite integer compatibility remains unresolved.')


if __name__ == '__main__':
    controls()
