#!/usr/bin/env python3
"""Erdos #708: exact g(A, I) = min |B|, B subset of I (|I| = max A consecutive integers),
prod(A) | prod(B); maximised over all interval positions (CRT residues).

The condition separates by prime: for every prime p, sum_{b in B} v_p(b) >= e_p := v_p(prod A).
Only the capped valuation min(v_p(b), e_p) matters, which is periodic in the start s mod p^e_p,
so the position of I is a tuple of per-prime residues (independent by CRT).
"""
import itertools, math, sys, time

T0 = time.time()
TLIM = float(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].replace('.', '').isdigit() else 540.0


def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def demands(A):
    e = {}
    for a in A:
        for p, k in factor(a).items():
            e[p] = e.get(p, 0) + k
    return e


def patterns(p, ep, M):
    """distinct capped-valuation patterns of prime p over a window of length M, with residue -> pattern"""
    mod = p ** ep
    pats = {}
    for r in range(mod):
        pat = []
        for j in range(M):
            x = r + j
            v = 0
            if x % mod == 0:
                v = ep
            else:
                while x % p == 0 and v < ep:
                    x //= p
                    v += 1
            pat.append(v)
        pats.setdefault(tuple(pat), r)
    return pats


def min_cover(dem, elems, ub=None):
    """dem: tuple of demands; elems: list of tuples (capped contributions). exact min number of elements."""
    P = len(dem)
    elems = [e for e in elems if any(e)]
    # greedy upper bound
    rem = list(dem)
    used = [False] * len(elems)
    g = 0
    while any(r > 0 for r in rem):
        best, bi = -1, -1
        for i, e in enumerate(elems):
            if used[i]:
                continue
            s = sum(min(e[k], rem[k]) for k in range(P))
            if s > best:
                best, bi = s, i
        if best <= 0:
            return None
        used[bi] = True
        g += 1
        for k in range(P):
            rem[k] = max(0, rem[k] - elems[bi][k])
    best_k = g if ub is None else min(g, ub)

    n_el = len(elems)
    sys.setrecursionlimit(10000)

    def lb(rem, avail):
        # max over primes of ceil(rem_p / maxcontrib_p) and a weighted total bound
        l = 0
        tot = sum(rem)
        if tot == 0:
            return 0
        mx = 0
        for i in avail:
            e = elems[i]
            s = 0
            for k in range(P):
                if rem[k]:
                    s += min(e[k], rem[k])
            if s > mx:
                mx = s
        if mx == 0:
            return 10 ** 9
        l = -(-tot // mx)
        for k in range(P):
            if rem[k]:
                m = max((elems[i][k] for i in avail), default=0)
                if m == 0:
                    return 10 ** 9
                l = max(l, -(-rem[k] // m))
        return l

    def feasible(rem, avail, k):
        if all(r == 0 for r in rem):
            return True
        if k == 0:
            return False
        if lb(rem, avail) > k:
            return False
        # most constrained prime: fewest candidates
        bestp, cands = None, None
        for p in range(P):
            if rem[p] > 0:
                c = [i for i in avail if elems[i][p] > 0]
                if cands is None or len(c) < len(cands):
                    bestp, cands = p, c
        # order candidates by total useful contribution
        cands.sort(key=lambda i: -sum(min(elems[i][q], rem[q]) for q in range(P)))
        excluded = set()
        for i in cands:
            nrem = tuple(max(0, rem[q] - elems[i][q]) for q in range(P))
            navail = [j for j in avail if j != i and j not in excluded]
            if feasible(nrem, navail, k - 1):
                return True
            excluded.add(i)
        return False

    # iterative deepening from the lower bound
    allav = list(range(n_el))
    k0 = lb(tuple(dem), allav)
    for k in range(k0, best_k):
        if feasible(tuple(dem), allav, k):
            return k
    return best_k


def worst_interval(A, verbose=False, cap_configs=None):
    """max over positions of min|B|; returns (value, witness residues, number of configs)"""
    M = max(A)
    e = demands(A)
    primes = sorted(e)
    dem = tuple(e[p] for p in primes)
    per = [list(patterns(p, e[p], M).items()) for p in primes]
    total = 1
    for x in per:
        total *= len(x)
    if cap_configs and total > cap_configs:
        return None, None, total
    best, wit = -1, None
    for combo in itertools.product(*per):
        elems = [tuple(combo[k][0][j] for k in range(len(primes))) for j in range(M)]
        v = min_cover(dem, elems)
        if v > best:
            best, wit = v, tuple((primes[k], combo[k][1]) for k in range(len(primes)))
        if time.time() - T0 > TLIM:
            raise TimeoutError
    return best, wit, total


def omega_bound(A):
    return sum(len(factor(a)) for a in A)


if __name__ == '__main__':
    # controls
    for A in ([2, 3], [4, 6], [6, 10, 15], [6, 10], [2, 4, 8]):
        v, w, t = worst_interval(A)
        print('A=%s worst min|B|=%d configs=%d omega_bound=%d witness=%s' % (A, v, t, omega_bound(A), w), flush=True)
