#!/usr/bin/env python3
"""GC1019: eight-tick interface-to-train delay, and the Q2 seed reduction.
Preregistered timing block in RULE30-GPT.md. Controls cover all eight cone
sources and all 256 freely controlled exterior streams. No long seed run.
"""
from itertools import product

SLAB = tuple(map(int, '100110'))


def literal(row, wall, exterior):
    p = (wall,) + tuple(row) + (exterior,)
    return tuple((30 >> (4*p[j]+2*p[j+1]+p[j+2])) & 1 for j in range(len(row)))


def packed(r, wall):
    return ((r << 1) | wall) ^ (r | (r >> 1))


def mask_table(gate):
    row = [{v} for v in SLAB]
    result = []
    for t in range(8):
        p = [{t % 2}] + row + [{gate} if t == 0 else {0,1}]
        row = [{a ^ (b | c) for a,b,c in product(*p[j:j+3])} for j in range(6)]
        result.append(''.join(str(next(iter(s))) if len(s)==1 else '?' for s in row))
    return result


def main():
    expected = {
        0: ['111101','000001','000011','100110','11110?','0000??','000???','10????'],
        1: ['111100','00001?','00011?','10110?','1010??','001???','011???','010???'],
    }
    for gate in (0,1):
        assert mask_table(gate) == expected[gate]
    for exterior in product((0,1), repeat=8):
        row = SLAB
        trace = [row[0]]
        for t, bit in enumerate(exterior):
            row = literal(row,t % 2,bit)
            trace.append(row[0])
        assert trace[:8] == [1,1,0,0,1,1,0,0]
        assert trace[8] == 1-exterior[0]
        if exterior[0]:
            assert trace[6] == 0  # Countercontrol: failure is not at time 6.
    for tail in product((0,1), repeat=3):
        source = SLAB + tail
        row = source
        trace = [row[0]]
        for t in range(8):
            row = literal(row,t % 2,0)[:-1]
            trace.append(row[0])
        assert trace == [1,1,0,0,1,1,0,0,1-tail[0]]
        base = sum(v << i for i,v in enumerate(source))
        for padding in (0, (1 << 16)-1):
            r = base | (padding << 9)
            for t in range(8):
                r = packed(r,t % 2)
            assert r & 1 == trace[-1]
    r = 9
    for t in range(4):
        r = packed(r,t % 2)
    assert r == int('10011001'[::-1],2)
    assert r & 63 == sum(v << i for i,v in enumerate(SLAB)) and r >> 6 == 2
    print('PASS: symbolic tables, 256 exterior streams, 8 actual cones, two paddings, seed at time 4')


if __name__ == '__main__':
    main()
