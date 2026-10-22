#!/usr/bin/env python3
"""Tests of the two constructions (Lemma 1 and Theorem 2) on random A and random intervals.
Each construction is built explicitly and checked: prod(A) | prod(B) prime by prime, and the size bound.
Also compares with the exact optimum (g708.min_cover) on small cases."""
import random, sys, time
sys.path.insert(0, '.')
from g708 import factor, min_cover
T0 = time.time(); TL = 200
rng = random.Random(708)

def vp(x, p):
    v = 0
    while x % p == 0:
        x //= p; v += 1
    return v

def check(A, B):
    e = {}
    for a in A:
        for p, k in factor(a).items():
            e[p] = e.get(p, 0) + k
    return all(sum(vp(b, p) for b in B) >= k for p, k in e.items())

def lemma1(A, I):
    B = set()
    primes = sorted({p for a in A for p in factor(a)})
    for p in primes:
        Ap = sorted((a for a in A if a % p == 0), key=lambda a: -vp(a, p))
        cand = sorted(I, key=lambda b: -vp(b, p))
        for a, b in zip(Ap, cand):
            assert vp(b, p) >= vp(a, p), ('Hall level count failed', A, p)
            B.add(b)
    return B

def theorem2(A, I):
    """squarefree A; heavy a (omega>=3): block w=a/P(a) placed at distinct elements; residual roles per prime."""
    M = max(A)
    heavy = [a for a in A if len(factor(a)) >= 3]
    light = [a for a in A if len(factor(a)) < 3]
    host = {}  # a -> element for its w-block
    used = set()
    for a in sorted(heavy, key=lambda a: M // (a // max(factor(a)))):
        w = a // max(factor(a))
        c = [b for b in I if b % w == 0 and b not in used]
        if not c:
            return None  # SDR failed (condition violated)
        host[a] = c[0]; used.add(c[0])
    B = set(host.values())
    primes = sorted({p for a in A for p in factor(a)})
    for p in primes:
        blocked = {host[a] for a in heavy if (a // max(factor(a))) % p == 0}
        roles = [a for a in light if a % p == 0] + [a for a in heavy if max(factor(a)) == p]
        cand = [b for b in I if b % p == 0 and b not in blocked]
        assert len(cand) >= len(roles), ('residual count failed', A, p)
        B.update(cand[:len(roles)])
    return B

def cond2(A):
    M = max(A)
    heavy = [a for a in A if len(factor(a)) >= 3]
    t = sorted(M // (a // max(factor(a))) for a in heavy)
    return all(t[i] >= i + 1 for i in range(len(t)))

def squarefree(a):
    return all(k == 1 for k in factor(a).values())

stats = dict(l1=0, l1_exact=0, l1_gap_max=0, t2=0, t2_cond=0, worst_ratio=0)
while time.time() - T0 < TL:
    n = rng.randint(2, 7)
    X = rng.choice([60, 200, 1000, 5000])
    pool = list(range(2, X + 1))
    if rng.random() < 0.5:
        pool = [a for a in pool if squarefree(a) and len(factor(a)) >= 2]
    A = sorted(rng.sample(pool, n))
    M = A[-1]
    s = rng.randrange(10 ** 6, 10 ** 9)
    I = list(range(s, s + M))
    B = lemma1(A, I)
    assert check(A, B) and len(B) <= sum(len(factor(a)) for a in A), ('LEMMA1 FAIL', A, s)
    stats['l1'] += 1
    if all(squarefree(a) for a in A) and cond2(A):
        stats['t2_cond'] += 1
        B2 = theorem2(A, I)
        assert B2 is not None and check(A, B2) and len(B2) <= 2 * n, ('THM2 FAIL', A, s, B2)
        stats['t2'] += 1
    if M <= 1000 and stats['l1_exact'] < 400:
        primes = sorted({p for a in A for p in factor(a)})
        e = {p: sum(vp(a, p) for a in A) for p in primes}
        elems = [tuple(min(vp(b, p), e[p]) for p in primes) for b in I]
        opt = min_cover(tuple(e[p] for p in primes), elems)
        stats['l1_exact'] += 1
        stats['worst_ratio'] = max(stats['worst_ratio'], opt / n)
        stats['l1_gap_max'] = max(stats['l1_gap_max'], len(B) - opt)
print('random tests passed:', stats, 't=%.0fs' % (time.time() - T0), flush=True)
