#!/usr/bin/env python3
"""G49 preregistered controls. NOT RUN at initial publication.

Exact bounded controls, not a proof of Antihydra nonhalting.
No output data files. Run only after predictions have been published.
"""
from fractions import Fraction
from itertools import product


def h(n):
    return (3 * n) // 2


def direct(n, t):
    bits = []
    for _ in range(t):
        bits.append(n % 2)
        n = h(n)
    return tuple(bits), n


def ah1():
    cases = 0
    for t in range(11):
        modulus = 2 ** t
        residues = set()
        for bits in product((0, 1), repeat=t):
            correction = 0
            for j, b in enumerate(bits):
                correction = 3 * correction + b * 2 ** j
            r = (correction * pow(3 ** t, -1, modulus)) % modulus if t else 0
            assert r not in residues
            residues.add(r)
            observed, q = direct(r, t)
            assert observed == bits
            assert 2 ** t * q == 3 ** t * r - correction
            assert 0 <= q < 3 ** t
            for lift in (1, 2):
                lifted_bits, terminal = direct(r + modulus * lift, t)
                assert lifted_bits == bits
                assert terminal == q + 3 ** t * lift
            cases += 1
        assert len(residues) == modulus
    return cases


def ah2():
    shifted, original = 8, 4
    counter, odd_count = 0, 0
    for j in range(33):
        assert shifted == original + 4
        assert counter == 2 * j - 3 * odd_count
        if j < 32:
            assert shifted % 2 == original % 2
            b = shifted % 2
            odd_count += b
            counter += -1 if b else 2
            shifted = h(shifted)
            original = (3 * original) // 2 + 2
    # This checks the reduced recurrences, not six-state TM equivalence.
    return 33


def brute_survival(t):
    count = 0
    for bits in product((0, 1), repeat=t):
        counter = 0
        for b in bits:
            counter += -1 if b else 2
            if counter < 0:
                break
        else:
            count += 1
    return count


def ah3():
    # Keep counts of surviving prefixes; discarded mass has hit -1.
    states = {0: 1}
    for t in range(129):
        survivors = sum(states.values())
        if t <= 10:
            assert survivors == brute_survival(t)
        p = Fraction(survivors, 2 ** t)
        x = 1 - p
        # For x>=0, x^2+x<=1 is equivalent to x<=r.
        assert x >= 0 and x * x + x <= 1
        next_states = {}
        for counter, count in states.items():
            for increment in (2, -1):
                new = counter + increment
                if new >= 0:
                    next_states[new] = next_states.get(new, 0) + count
        states = next_states
    return 129


def ah4():
    n, counter = 3, 0
    counter += -1 if n % 2 else 2
    nxt = h(n)
    assert nxt > n and counter == -1
    return (n, nxt, counter)


if __name__ == '__main__':
    print('AH1 PASS: exact words/lifts:', ah1())
    print('AH2 PASS: shifted-map/counter checkpoints:', ah2())
    print('AH3 PASS: rational survival bounds:', ah3())
    print('AH4 PASS: growing seed still hits counter -1:', ah4())
    print('Finite controls only; selected seed 8 nonhalting remains open.')
