"""G45 AS1-AS3; preregistered before run. Exact word ceilings vs direct starts.
Initial publication: NOT RUN. Invoke with Python 3 at the next research checkpoint.
"""
from collections import Counter
from itertools import product


def specification(word):
    a = B = 0
    K = None
    for t, b in enumerate(word, 1):
        B = 3**b*B+b*2**(t-1)
        a += b
        deficit = 2**t-3**a
        if deficit > 0:
            ceiling = B//deficit
            K = ceiling if K is None else min(K, ceiling)
    modulus = 2**len(word)
    r = (-B*pow(3**a, -1, modulus)) % modulus
    return r, K


def trajectory(n, horizon):
    q = n
    word = []
    survives = True
    for _ in range(horizon):
        b = q % 2
        word.append(b)
        q = (3*q+1)//2 if b else q//2
        survives &= q >= n
    return tuple(word), survives


def count(r, K, horizon, width):
    L, U = 2**(width-1), 2**width-1
    if K is not None:
        U = min(U, K)
    if U < L:
        return 0
    modulus = 2**horizon
    return (U-r)//modulus-(L-1-r)//modulus


def main():
    word_counts = exceptions = 0
    for horizon in range(1, 13):
        specs = {w: specification(w) for w in product((0, 1), repeat=horizon)}
        for width in range(1, 9):
            actual = Counter()
            for n in range(2**(width-1), 2**width):
                w, survives = trajectory(n, horizon)
                r, K = specs[w]
                assert n % (2**horizon) == r
                if survives:
                    actual[w] += 1
                    if K is not None:
                        assert n <= K
                        exceptions += 1
            for w, (r, K) in specs.items():
                assert count(r, K, horizon, width) == actual[w], (horizon, width, w)
                word_counts += 1
    w = (1, 0, 1, 0)
    assert specification(w) == (1, 1)
    assert trajectory(1, 4) == (w, True)
    assert 3**sum(w) < 2**len(w)
    print(f'AS1: {word_counts} exact word/width counts, horizons1..12 and widths1..8')
    print(f'AS2: {exceptions} actual-survivor occurrences with finite ceilings verified')
    print('Unexpected AS3: start1/word1010 distinguishes actual and coefficient survival')
    print('ALL CHECKS PASS; no uniform ceiling bound or survivor-sum estimate inferred')


if __name__ == '__main__':
    main()
