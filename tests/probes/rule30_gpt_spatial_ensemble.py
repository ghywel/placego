"""G97 SC1-SC2 SC1-SC2 preregistered at a233f59; PASS 2026-10-06.
SC1: widths1..8, each output word has exactly four local preimages.
SC2: five-bit neighbourhoods give 16,16,24 left/stay/right flips;
literal truth-table updates agree with separate Boolean identities.
Unexpected scope guard: zero row flips0, all-one first right flip1.
No orbit profile or temporal independence assertion.
"""
from collections import Counter
from itertools import product


def update(l, c, r):
    return (30 >> (4*l + 2*c + r)) & 1


def main():
    words = 0
    for width in range(1, 9):
        counts = Counter()
        for row in product((0, 1), repeat=width+2):
            out = tuple(update(*row[j:j+3]) for j in range(width))
            counts[out] += 1
            words += 1
        assert len(counts) == 2**width
        assert set(counts.values()) == {4}
    counts = [0, 0, 0]
    for a, b, c, d, e in product((0, 1), repeat=5):
        literal = (update(a,b,c)^c, update(b,c,d)^c, update(c,d,e)^c)
        algebra = (a^(b & (1-c)), b^(c|d)^c, d|e)
        assert literal == algebra
        for j, value in enumerate(literal):
            counts[j] += value
    assert counts == [16, 16, 24]
    assert update(0,0,0)^0 == 0
    assert update(1,1,1)^1 == 1
    print('SC1 PASS:', words, 'input words, widths1..8, four preimages/output')
    print('SC2 PASS: 32 neighbourhoods; left/stay/right flips', counts)
    print('Scope guard PASS: constant rows refute universal three-quarter frequency')


if __name__ == '__main__':
    main()
