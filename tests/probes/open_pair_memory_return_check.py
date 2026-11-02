#!/usr/bin/env python3
"""GC2395: two explicit histories, three literal steps; prediction in its report."""
R = 12
mask = (1 << 28)-1


def step(x):
    return (x ^ ((x << 1) | (x << 2) | 3)) & mask


for u in (0, 1):
    e = 1 << (R+5)
    x = e ^ (1 << R) ^ (1 << (R-3)) ^ (u << (R-1))
    observed = []
    for t in range(4):
        delta = e ^ x
        front = delta.bit_length()-1
        pair = ((delta >> (front-1)) & 1, (delta >> (front-2)) & 1)
        observed.append((front, pair))
        if t == 2:
            assert (front, pair) == (R+4, (1, 0))
            assert (delta >> (front-3)) & 1 == u
            assert (e >> (front+1)) & 1 == 1
        if t < 3:
            e, x = step(e), step(x)
    assert observed[1][0] == R+2
    assert observed[3] == (R+5, (0, 1-u))
    print('old bit', u, 'front/pair history', observed)
print('PASS: same reset pair; old pair bit returns on the next blocked step')
