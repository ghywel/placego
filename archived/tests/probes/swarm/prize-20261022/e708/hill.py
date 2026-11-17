#!/usr/bin/env python3
"""Heuristic search for the worst interval position for a given A (lower bounds on max_I g(A, I)).
Position = start s, represented by residues s mod p^{e_p} (CRT). Exact min cover for each position.
usage: hill.py tlim  (runs the experiment list at the bottom)
"""
import random, sys, time, math
sys.path.insert(0, '.')
from g708 import factor, demands, min_cover

T0 = time.time()
TL = float(sys.argv[1]) if len(sys.argv) > 1 else 300


def capped_v(x, p, ep):
    if x == 0:
        return ep
    v = 0
    while x % p == 0 and v < ep:
        x //= p
        v += 1
    return v


def evaluate(A, res, return_elems=False):
    M = max(A); e = demands(A); primes = sorted(e)
    dem = tuple(e[p] for p in primes)
    elems = []
    for j in range(M):
        vec = tuple(capped_v((res[p] + j) % (p ** e[p]), p, e[p]) for p in primes)
        if any(vec):
            elems.append(vec)
    v = min_cover(dem, elems)
    return (v, elems) if return_elems else v


def star(A, u, rng=None):
    """interval [x-u, x-u+M-1] with x divisible by every prime of prod(A) exactly once (random unit parts)."""
    M = max(A); e = demands(A); res = {}
    for p in e:
        mod = p ** e[p]
        while True:
            c = rng.randrange(1, mod) if rng else 1
            if c % p:
                break
        x = (p * c) % mod if e[p] > 1 else 0
        res[p] = (x - u) % mod
    return res


def climb(A, start, iters, rng):
    e = demands(A)
    cur = dict(start); cv = evaluate(A, cur)
    best, bres = cv, dict(cur)
    for _ in range(iters):
        if time.time() - T0 > TL:
            break
        p = rng.choice(sorted(e))
        mod = p ** e[p]
        new = dict(cur)
        if rng.random() < 0.5:
            new[p] = rng.randrange(mod)
        else:
            new[p] = (cur[p] + rng.choice([-1, 1]) * rng.randrange(1, 4)) % mod
        nv = evaluate(A, new)
        if nv >= cv:
            cur, cv = new, nv
            if cv > best:
                best, bres = cv, dict(cur)
    return best, bres


def run(name, A, iters=300, restarts=4, seed=1):
    rng = random.Random(seed)
    n = len(A); M = max(A)
    om = sum(len(factor(a)) for a in A)
    vals = []
    s = star(A, (M - 1) // 2, None)
    sv = evaluate(A, s)
    best, bres = sv, s
    for r in range(restarts):
        st = star(A, rng.randrange(M), rng) if r % 2 == 0 else {p: rng.randrange(p ** k) for p, k in demands(A).items()}
        b, br = climb(A, st, iters, rng)
        vals.append(b)
        if b > best:
            best, bres = b, br
        if time.time() - T0 > TL:
            break
    print('%s n=%d M=%d sum_omega=%d  star(centre)=%d  climb_best=%d (restarts %s)  2n=%d  t=%.0fs' %
          (name, n, M, om, sv, best, vals, 2 * n, time.time() - T0), flush=True)
    return best


if __name__ == '__main__':
    exps = []
    # Erdos-Suranyi pair family: primes p_1<...<p_l with 2 p_1^2 > p_l^2
    for P in ([7, 11, 13], [17, 19, 23], [11, 13, 17, 19][:0] or [23, 29, 31], [17, 19, 23]):
        pass
    fam = {
        'ES l=3 (7,11,13)': [7, 11, 13],
        'ES l=4 (29,31,37,41)': [29, 31, 37, 41],
        'ES l=5 (53,59,61,67,71)': [53, 59, 61, 67, 71],
    }
    for name, P in fam.items():
        A = sorted(P[i] * P[j] for i in range(len(P)) for j in range(i + 1, len(P)))
        exps.append((name, A))
    for name, A in exps:
        run(name, A, iters=150, restarts=4)
