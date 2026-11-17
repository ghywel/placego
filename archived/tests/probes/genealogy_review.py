#!/usr/bin/env python3
"""GC2352: fixed small independent controls; predictions in genealogy report section7.
512 finite nine-bit rows, every black cut; 64 mod4 inputs; 16 crossing windows.
No files, solver, random samples, horizon enlargement or imported Local implementation.
"""
from itertools import product


def f(a, b, c):
    return (30 >> (4*a + 2*b + c)) & 1


def step(row):
    return {j for j in range(min(row)-1, max(row)+2)
            if f(int(j-1 in row), int(j in row), int(j+1 in row))}


def advance(row, b):
    nxt = step(row)
    nb = b+1 if b+1 not in row and b+2 not in row else max(j for j in nxt if j <= b)
    return nxt, nb


def p(a, b, c):
    return a+b+c+b*c


def exact(a, b, c):
    u = b+c-b*c
    return a+u-2*a*u


for a, b, c, d in product(range(2), repeat=4):
    # Crossing edges need black parents at the two interior coordinates.
    assert not (b and c and f(a,b,c) and f(b,c,d))

for a, b, c in product(range(4), repeat=3):
    x, y, z = a%2, b%2, c%2
    ha, hb, hc = a//2, b//2, c//2
    tangent = ha ^ ((1 ^ z) & hb) ^ ((1 ^ y) & hc)
    carry = int(x+y+z == 2)
    assert p(a,b,c)%2 == exact(a,b,c)%2 == f(x,y,z)
    assert (p(a,b,c)%4)//2 == tangent ^ carry
    assert (exact(a,b,c)%4)//2 == tangent
for abc in product(range(2), repeat=3):
    assert exact(*abc) == f(*abc)

# The arbitrary-row front tracks a marked black prefix, not one isolated founder.
solid = set(range(5))
children = step(solid)
assert not (children & {1, 2, 3})  # middle founder 2 has no black child
assert advance(solid, 2)[1] == 0  # the prefix front nevertheless survives

cuts = retreats = refunds = 0
largest = 0
for word in product(range(2), repeat=9):
    row = {i for i,v in enumerate(word) if v}
    for b in sorted(row):
        cuts += 1
        reached = {i for i in row if i <= b}
        nxt, nb = advance(row,b)
        image = {j for j in nxt if {j-1,j,j+1} & reached}
        assert image == {j for j in nxt if j <= nb}
        d = b-nb
        if d > 0:
            retreats += 1
            largest = max(largest,d)
            assert not (set(range(nb+1,b+2)) & nxt)
            for _ in range((d+1)//2):
                nxt, nb2 = advance(nxt,nb)
                assert nb2 == nb+1
                nb = nb2
                refunds += 1
print(f'PASS: {cuts} black cuts in 512 rows; {retreats} retreats, largest {largest}; {refunds} forced advances')
print('PASS: 16 crossing windows; 64 inputs for both lifts; 8 exact binary outputs')
