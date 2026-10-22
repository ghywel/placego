#!/usr/bin/env python3
"""Find a position for A={77,91,143} (primes 7,11,13; violates 2p1^2>p3^2) with min|B| = 4 and verify it by
independent brute force over all subsets of size <= 3 of the interval's relevant elements."""
import itertools, random, sys, time
sys.argv = [sys.argv[0], '120']
sys.path.insert(0, '.')
import hill
from hill import climb, star, evaluate
A = [77, 91, 143]
rng = random.Random(3)
found = None
for r in range(20):
    b, res = climb(A, star(A, rng.randrange(143), rng), 150, rng)
    if b >= 4:
        found = res; break
print('climb found value', b, 'residues', found, flush=True)
# CRT: build the actual start s from residues mod 49, 121, 169
def crt(res):
    s, m = 0, 1
    for p, r in res.items():
        mod = p ** 2
        while s % mod != r:
            s += m
        m *= mod
    return s
s = crt(found) + 10 ** 7 * (49 * 121 * 169)  # shift by a multiple of the period: same pattern, large integers
I = list(range(s, s + 143))
P = 7 ** 2 * 11 ** 2 * 13 ** 2
rel = [b for b in I if b % 7 == 0 or b % 11 == 0 or b % 13 == 0]
ok3 = [B for k in (1, 2, 3) for B in itertools.combinations(rel, k) if eval('*'.join(map(str, B))) % P == 0]
ok4 = next((B for B in itertools.combinations(rel, 4) if (B[0]*B[1]*B[2]*B[3]) % P == 0), None)
print('start s =', s, ' relevant elements:', len(rel))
print('subsets of size <=3 with prod(A) | prod(B):', len(ok3), ' -> min|B| >= 4' if not ok3 else ' -> FAIL')
print('a size-4 B:', ok4, [ (b % 7 == 0, b % 11 == 0, b % 13 == 0, b % 49 == 0, b % 121 == 0, b % 169 == 0) for b in ok4])
x = [b for b in I if b % 1001 == 0]
print('elements divisible by 7*11*13 in I:', [(b, b - s) for b in x])
