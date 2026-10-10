#!/usr/bin/env python3
"""GC1017: local correlated implications behind the two-gap train's slab.
Preregistration and hand argument: RULE30-GPT.md GC1017.
Exact truth-table controls, not a membership solver or a train-length scan.
"""
from itertools import product


def bits(word):
    return tuple(map(int, word))


def compatible(left, centre, right):
    return all(((30 >> (4 * left[t] + 2 * centre[t] + right[t])) & 1)
               == centre[t + 1] for t in range(min(len(left), len(centre)-1, len(right))))


def patches(left, centre, constrain=True):
    n = len(left)
    choices = [list(product((0, 1), repeat=n-j)) for j in (1, 2, 3)]
    for a in choices[0]:
        if constrain and not compatible(left, centre, a):
            continue
        for b in choices[1]:
            if not compatible(centre, a, b):
                continue
            for c in choices[2]:
                if compatible(a, b, c):
                    yield a, b, c


def main():
    cases = [
        ('A', '01010', '11001', lambda a,b,c: a == bits('0100')),
        ('B', '110011', '010001', lambda a,b,c: a[:4] == bits('0100') and b == bits('1100')),
        ('C', '0010001', '0110011', lambda a,b,c: a[1:5] == bits('1001')
         and b[1:5] == bits('0111') and c[1] == 0),
    ]
    frames = list(map(bits, ('100110', '111101', '000001', '000011')))
    for phase, frame in enumerate(frames):
        for exterior in (0, 1):
            padded = (phase % 2,) + frame + (exterior,)
            output = tuple((30 >> (4*padded[j]+2*padded[j+1]+padded[j+2])) & 1
                           for j in range(6))
            assert (output == frames[(phase+1) % 4]) == (phase != 0 or exterior == 0)
    print('PASS: slab transitions require exactly column 7 = 0 at phase 0')
    for name, l, m, predicate in cases:
        left, centre = bits(l), bits(m)
        models = list(patches(left, centre))
        assert models and all(predicate(*v) for v in models)
        assert any(not predicate(*v) for v in patches(left, centre, False))
        print(name, 'PASS', len(models), 'local patches; dropped-observation countercontrol PASS')
        if name == 'C':
            # Column 7 at phases 1 and 2 is not fixed by this deduction.
            assert {c[2:] for a,b,c in models} == set(product((0,1), repeat=2))
            print('Unexpected check PASS: column 7 phases 1,2 retain all four local pairs')


if __name__ == '__main__':
    main()
