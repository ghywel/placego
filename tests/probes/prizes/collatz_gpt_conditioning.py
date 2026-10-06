"""G39 preregistered SC1-SC4 controls; finite implementation checks only.
Run with Python 3. No files or large datasets generated.
"""
from itertools import product
from collections import Counter
from math import comb


def admissible(word):
    a = 0
    for t, b in enumerate(word, 1):
        a += b
        if 3**a <= 2**t:
            return False
    return True


def dp_counts(T):
    counts = {0: 1}
    for t in range(1, T + 1):
        nxt = Counter()
        for a, n in counts.items():
            for b in (0, 1):
                if 3**(a+b) > 2**t:
                    nxt[a+b] += n
        counts = nxt
    return counts


def rotations(w):
    return {w[k:] + w[:k] for k in range(len(w))}


def main():
    words = nodes = classes = 0
    for T in range(1, 13):
        actual = Counter()
        seen = set()
        for w in product((0, 1), repeat=T):
            if admissible(w):
                actual[sum(w)] += 1
            if 3**sum(w) <= 2**T:
                continue
            words += 1
            orbit = rotations(w)
            assert any(admissible(v) for v in orbit), (T, w)
            key = min(orbit)
            if key not in seen:
                seen.add(key)
                classes += 1
        assert actual == dp_counts(T), (T, actual, dp_counts(T))
        for a in range(T+1):
            if 3**a > 2**T:
                nodes += 1
                assert T*actual[a] >= comb(T, a), (T, a)
    # Unexpected control: rotation orbits can have fewer than T members.
    for w in ((1,)*12, (1, 1, 0)*4):
        orbit = rotations(w)
        assert len(orbit) < len(w)
        assert any(admissible(v) for v in orbit)
    # Counterfactual: character on Z/2, E selects the +1 outcome.
    unconditional = (1 + (-1))/2
    conditional = 1
    cost = 2
    assert abs(conditional) > cost*abs(unconditional)
    print(f'SC1: {words} positive-total words, {classes} rotation classes; DP agrees through T12')
    print(f'SC2: {nodes} endpoint count bounds pass')
    print('SC3: all-one and repeated110 short rotation orbits pass')
    print('SC4: complex-cancellation transfer refuted on Z/2')
    print('ALL CHECKS PASS; no survivor-count or Fourier-decay theorem inferred')


if __name__ == '__main__':
    main()
