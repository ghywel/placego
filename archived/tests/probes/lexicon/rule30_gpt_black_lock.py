#!/usr/bin/env python3
"""GC850 independent black-wall lock certificate.
Predictions registered in CLOUD-LOCAL.md before the scratch calculation:
P1: white reset plus ten black updates forces the first bit zero in width five,
    and admits a two-black-step invariant set.
X1: the same forcing at width four (known-wrong countercontrol).
U1 (unexpected): omit the white reset; inspect whether it is essential.
OUTCOME: P1 PASS, X1 REFUTED. U1 strengthens the result: nine black updates
alone force prefix 01; that prefix is invariant under every later black step.
Independent tuple truth-table and integer Boolean kernels must agree on every
edge and every image set. No shared code with OH. Constant-black forcing is a
finite certificate, not a simulation of a selected seed.
"""
from itertools import product
TABLE = dict(zip(product((1, 0), repeat=3), (0, 0, 0, 1, 1, 1, 1, 0)))
MASKS = (0xffffffff, 0xf0cbffff, 0xf0cbff3f, 0xe0cbff3f,
         0xe0cbff33, 0xe00bff33, 0xe00bff03, 0x000bff03,
         0x000bff00, 0x0000ff00, 0x0000bf00)

def literal(x, wall, u):
    return tuple(TABLE[(wall if j == 0 else x[j-1], x[j],
                        u if j == len(x)-1 else x[j+1])]
                 for j in range(len(x)))

def number(x):
    return int(''.join(map(str, x)), 2)

def integer(s, wall, u, k):
    out = 0
    for j in range(k):
        a = wall if j == 0 else (s >> (k-j)) & 1
        b = (s >> (k-1-j)) & 1
        c = u if j == k-1 else (s >> (k-2-j)) & 1
        out = (out << 1) | (a ^ (b | c))
    return out

def image(S, wall):
    return {literal(x, wall, u) for x in S for u in (0, 1)}

def check():
    for k in (4, 5):
        A = set(product((0, 1), repeat=k))
        for x in A:
            for w, u in product((0, 1), repeat=2):
                assert number(literal(x, w, u)) == integer(number(x), w, u, k)
        S = A
        for n in range(11):
            if k == 5:
                assert sum(1 << number(x) for x in S) == MASKS[n]
            # Independent backward image membership, over every possible target.
            parents = {y for y in A if any(integer(number(x), 1, u, k)
                       == number(y) for x in S for u in (0, 1))}
            assert parents == image(S, 1)
            if n < 10:
                S = image(S, 1)
        if k == 4:
            assert any(x[0] == 1 for x in S)  # X1 must fail
    A = set(product((0, 1), repeat=5))
    S = image(A, 0)
    for _ in range(8):
        S = image(S, 1)
    assert any(x[0] == 1 for x in S)  # cannot replace nine by eight here
    S = image(S, 1)
    I = {x for x in A if x[:2] == (0, 1)}
    assert S == I
    assert image(I, 1) <= I
    print('GC850 PASS: exact masks, two independent kernels, reset and width controls')

if __name__ == '__main__':
    check()
