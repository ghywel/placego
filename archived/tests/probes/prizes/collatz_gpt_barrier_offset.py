"""G67 OB1–OB2 and conditioning guard, preregistered at 7cc1b4b.

Exact integer controls; no larger first-deficit census or survivor claim.
"""
from itertools import product
from collatz_gpt_actual_ceiling import specification
from collatz_gpt_first_deficit_gap import first_deficit


def intercept(word):
    B = 0
    for p, b in enumerate(word):
        B = 3**b * B + b * 2**p
    return B


def extremal(a):
    positions = [(3**i).bit_length()-1 for i in range(a)]
    t = (3**a).bit_length()
    occupied = set(positions)
    word = tuple(int(p in occupied) for p in range(t))
    B = sum(3**(a-1-i) * 2**p for i, p in enumerate(positions))
    return word, B


def main():
    classes = {}
    population = 0
    for t in range(1, 17):
        for word in product((0, 1), repeat=t):
            if not first_deficit(word):
                continue
            population += 1
            a = sum(word)
            if not a:
                assert word == (0,) and intercept(word) == 0
                continue
            expected, bound = extremal(a)
            B = intercept(word)
            assert len(expected) == t and B <= bound
            classes.setdefault(a, []).append((B, word))
    for a, rows in sorted(classes.items()):
        expected, bound = extremal(a)
        maximum = max(B for B, _ in rows)
        winners = [word for B, word in rows if B == maximum]
        assert maximum == bound and winners == [expected]
    print(f'OB1: {population} first-deficit words; '
          f'{len(classes)} nonzero classes; unique intercept maxima pass')

    for a in range(1, 257):
        word, B = extremal(a)
        t = len(word)
        assert sum(word) == a and word[-1] == 0
        assert first_deficit(word) and intercept(word) == B
        assert 6*B > a*3**a and 3*B <= a*3**a
        assert (3*B == a*3**a) == (a == 1)
        _, K = specification(word)
        assert K == B // (2**t-3**a)
    print('OB2: 256 exact constructions; barrier, recurrence, envelope '
          'and independent prefix-ceiling controls pass')
    assert intercept((0, 0, 1, 1)) == 20
    assert not first_deficit((0, 0, 1, 1))
    assert extremal(2) == ((1, 1, 0, 0), 5)
    print('CF: unrestricted 0011 maximum fails the first-deficit barrier')


if __name__ == '__main__':
    main()
