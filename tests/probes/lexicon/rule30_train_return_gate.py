#!/usr/bin/env python3
"""GC1018: exact reduced train gate and a failed two-cycle closure.
Preregistered in RULE30-GPT.md after GC1017. No SAT or record scan.
Controls: literal shrinking cone, packed padded evolution, explicit full-slab
witness. The latter must leave the train by time 20, by GC1017, because its
column 7 violates the gate at time 8. Two exterior paddings are independent
controls; neither is a universal-extension claim.
"""
from itertools import product


def cone(row):
    row = tuple(row)
    for wall in (0, 1, 1, 1):
        src = (wall,) + row
        row = tuple((30 >> (4*src[j]+2*src[j+1]+src[j+2])) & 1
                    for j in range(len(row)-1))
    return row


def packed(row, wall):
    return ((row << 1) | wall) ^ (row | (row >> 1))


def encode(row):
    return sum(bit << i for i, bit in enumerate(row))


def main():
    for a,b,c,d in product((0,1), repeat=4):
        source = (0,a,b,c,d)
        expected = (1-a)*(1-b)*(c | d)
        assert cone(source) == (expected,)
        for padding in (0, (1 << 12)-1):
            row = encode(source) | (padding << 5)
            for wall in (0,1,1,1):
                row = packed(row, wall)
            assert row & 1 == expected
    bad = []
    for tail in product((0,1), repeat=8):
        source = (0,) + tail
        first = cone(source)
        if first[0] == 0 and cone(first)[0] == 1:
            bad.append(source)
    witness = tuple(map(int, '011010000'))
    assert len(bad) == 39 and witness in bad
    assert cone(witness) == tuple(map(int, '00010'))
    assert cone(cone(witness)) == (1,)
    assert cone((0,0,0,0,0)) == (0,) and cone((0,0,0,0,1)) == (1,)
    exits = []
    for padding in (0, (1 << 30)-1):
        row = encode(tuple(map(int, '100110')) + witness) | (padding << 15)
        failure = None
        for t in range(21):
            if t == 8:
                assert (row >> 6) & 1 == 1
            if t % 2 == 0 and (row & 1) != (1-(t//2)%2) and failure is None:
                failure = t
            row = packed(row, t % 2)
        assert failure is not None and failure <= 20
        exits.append(failure)
    print('PASS: all 16 exact gates and both paddings; 39 two-cycle nonclosure witnesses')
    print('PASS: 011010000 -> 00010 -> 1; full-slab train exits at times', exits)


if __name__ == '__main__':
    main()
