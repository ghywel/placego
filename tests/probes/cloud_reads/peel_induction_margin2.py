"""Peel-closure test for I2 = {all 14 groups spectrum-feasible, all margins >= 2}, peeling only from bins >= 4."""
import itertools, sys
from collections import Counter
L = lambda n: n*(n-1)//2; T = lambda n: n*(n+1)//2
SUB = [J for s in (1,2,3) for J in itertools.combinations(range(4), s)]
def spectra(pool):
    sp = [set() for _ in range(len(pool)+1)]; sp[0].add(0)
    for x in pool:
        for k in range(len(pool)-1, -1, -1):
            if sp[k]: sp[k+1] |= {s + x for s in sp[k]}
    return sp
cache = {}
def data(M, q):
    if (M, q) not in cache:
        pool = sorted(x for x in range(M+1) if x != q)
        cache[(M, q)] = (pool, spectra(pool))
    return cache[(M, q)]
def in_I2(M, q, C, t):
    if not (1 <= q <= M-1): return False
    pool, sp = data(M, q)
    mins = lambda c: sum(pool[:c]); maxs = lambda c: sum(pool[len(pool)-c:])
    for J in SUB:
        cJ = sum(C[i] for i in J); tJ = sum(t[i] for i in J)
        if tJ not in sp[cJ]: return False
        if tJ - mins(cJ) < 2 or maxs(cJ) - tJ < 2: return False
    return True
def run(M):
    n = fails = 0; how = Counter(); ex = []
    for C in itertools.product(range(3, M-8), repeat=4):
        if sum(C) != M or max(C) < 4: continue
        big = [i for i in range(4) if C[i] >= 4]
        for q in range(1, M):
            pool, sp = data(M, q); S = sum(pool)
            mins = lambda c: sum(pool[:c]); maxs = lambda c: sum(pool[len(pool)-c:])
            for t3 in itertools.product(*[range(mins(C[i]), maxs(C[i])+1) for i in range(3)]):
                t = t3 + (S - sum(t3),)
                if not in_I2(M, q, C, t): continue
                n += 1; ok = None
                for X in big:
                    C2 = tuple(C[i] - (i == X) for i in range(4))
                    t_top = tuple(t[i] - (M if i == X else 0) for i in range(4))
                    if (q == M-1 and all(t_top[i] >= 0 for i in range(4))) or in_I2(M-1, q, C2, t_top): ok = 'top'; break
                    t_bot = tuple(t[i] - (C[i] - 1 if i == X else C[i]) for i in range(4))
                    if in_I2(M-1, q-1, C2, t_bot): ok = 'bottom'; break
                if ok: how[ok] += 1
                else:
                    fails += 1
                    if len(ex) < 5: ex.append((q, C, t))
    return n, fails, dict(how), ex
for M in map(int, sys.argv[1:]):
    print(M, run(M), flush=True)
