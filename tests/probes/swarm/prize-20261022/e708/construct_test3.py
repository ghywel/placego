#!/usr/bin/env python3
"""Theorem 2 construction at ADVERSARIAL (star) positions: I centred on a common multiple of all of A
(or of a random subfamily), the configuration behind the Erdos-Suranyi lower bound."""
import random, sys, time, math
sys.path.insert(0, '.')
from g708 import factor
from construct_test2 import build, check
T0 = time.time(); TL = 90
rng = random.Random(70801)
st = dict(tests=0, ok=0)
while time.time() - T0 < TL:
    n = rng.randint(3, 12)
    X = rng.choice([500, 3000, 20000])
    pool = [a for a in range(30, X + 1) if len(factor(a)) >= 3] if rng.random() < 0.7 else list(range(2, X + 1))
    A = sorted(rng.sample(pool, n)); M = A[-1]
    sub = A if rng.random() < 0.5 else rng.sample(A, max(2, n // 2))
    L = 1
    for a in sub:
        L = L * a // math.gcd(L, a)
    x = L * rng.randrange(1, 10 ** 6)
    u = rng.choice([M // 2, rng.randrange(M)])
    I = list(range(x - u, x - u + M))
    status, B = build(A, I)
    st['tests'] += 1
    if status == 'ok':
        st['ok'] += 1
        assert check(A, B) and len(B) <= 2 * n, ('FAIL', A, x, u)
print('construct_test3 (star positions) passed:', st, 't=%.0fs' % (time.time() - T0), flush=True)
