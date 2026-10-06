"""G70 HC1–HC2; preregistered at 43874f5 (research commit 068b3f8).

Direct small-start controls and an exact large-width cutoff calculation.
"""
from collections import Counter


def runs(values):
    result = []
    start = previous = values[0]
    for value in values[1:]:
        if value != previous+1:
            result.append((start, previous))
            start = value
        previous = value
    result.append((start, previous))
    return result


def main():
    actual = [set() for _ in range(33)]
    coefficient = [set() for _ in range(33)]
    discrepancy = Counter()
    equal_guaranteed = Counter()
    for n in range(1, 4097):
        q = n
        a = 0
        stays = barrier = True
        for t in range(1, 33):
            b = q % 2
            a += b
            q = (3*q+1)//2 if b else q//2
            stays &= q >= n
            barrier &= 3**a >= 2**t
            if stays:
                actual[t].add(n)
            if barrier:
                coefficient[t].add(n)
            assert not barrier or stays
            if stays != barrier:
                assert 3**10*n**10 < t**143
                discrepancy[n] += 1
            if 3**10*n**10 >= t**143:
                assert stays == barrier
                equal_guaranteed[t] += 1
    intervals = 0
    for t in range(1, 33):
        assert coefficient[t] <= actual[t]
        assert len(actual[t])-len(coefficient[t]) <= t**15//3
        for w in range(1, 13):
            lo, hi = 2**(w-1), 2**w
            aa = sum(lo <= n < hi for n in actual[t])
            cc = sum(lo <= n < hi for n in coefficient[t])
            possible = max(0, min(hi-1, t**15//3)-lo+1)
            assert 0 <= aa-cc <= possible
            if 3**10*lo**10 >= t**143:
                assert aa == cc
            intervals += 1
    print(f'HC1: {4096*32} start/horizon pairs and {intervals} width/horizon '
          'counts pass inclusion and cutoff controls')
    print('Discrepancies (start:number of horizons):', sorted(discrepancy.items()))
    print('Guaranteed-equality samples by horizon:', sorted(equal_guaranteed.items()))

    true = []
    false = []
    for w in range(2, 257):
        T = (3*w+1)//2
        holds = 3**10*2**(10*(w-1)) >= T**143
        (true if holds else false).append(w)
    assert 32 in false and 256 in true
    print('HC2: T=ceil(3w/2), exact criterion false intervals:', runs(false))
    print('HC2: exact criterion true intervals:', runs(true))
    assert 1 in actual[2] and 1 not in coefficient[2]
    print('CF: universal actual/coefficient equality refuted by n1,T2')


if __name__ == '__main__':
    main()
