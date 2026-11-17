#!/usr/bin/env python3
"""GC1021: a bounded failed escape-transport diagnostic, not an all-time claim.

Record search and prediction precede the run in RULE30-GPT.md. Insert the
known GC1018 escape suffix after zero to three extra seven-ring copies.
The original placement exits at t=16. The shifted placements have no exit
through t=100, under either tested continuation. This supplies no fixed
transport law and does not prove that the shifted defects heal forever.
Independent literal shrinking cones and packed evolution; unperturbed
periodic background is the negative control. No SAT or new record scan.
"""
RING = '0100110'
ESCAPE = '011010000'
HORIZON = 100


def first_exit(source):
    row = tuple(source)
    packed = sum(v << i for i, v in enumerate(source))
    first = None
    for t in range(HORIZON+1):
        assert row[0] == (packed & 1)
        if row[0] != int(t % 4 < 2) and first is None:
            first = t
        if t < HORIZON:
            p = (t % 2,) + row
            row = tuple((30 >> (4*p[i]+2*p[i+1]+p[i+2])) & 1
                        for i in range(len(row)-1))
            packed = ((packed << 1) | (t % 2)) ^ (packed | (packed >> 1))
    assert len(row) == 1
    return first


def main():
    assert first_exit(tuple(int(RING[i % 7]) for i in range(1, 102))) is None
    for copies in range(4):
        start = 7+7*copies
        for continuation in ('white', 'periodic'):
            source = tuple(
                int(RING[i % 7]) if i < start else
                int(ESCAPE[i-start]) if i < start+len(ESCAPE) else
                int(RING[i % 7]) if continuation == 'periodic' else 0
                for i in range(1, 102))
            result = first_exit(source)
            assert result == (16 if copies == 0 else None)
            print(copies, continuation, result)
    print('PASS controls; shifted exit NOT SEEN through 100, not eternal healing')


if __name__ == '__main__':
    main()
