#!/usr/bin/env python3
"""parent22_review.py: Cloud's check of FOUR-BIN-PARTITIONS section 11 (GPT's parent packet for counts (a,2,2,c), a,c >= 3).
P1  Exhaustive, both directions: realized target tuples = (all fourteen cuts) minus the family F(a,c) closed under
    permutation of equal-size labels, the a/c role exchange, and full reflection. N = a+c+4 <= NMAX.
P2  The two q = 3 lift partitions of section 11.3 and the h = 1, 2 strict-pair switches of 11.4, for a, c < 80.
PREDICTIONS (before any run): P1 has no mismatch to N = 14 (0.85); P2 holds (0.95).
"""
import sys, itertools
L = lambda r: r * (r - 1) // 2

def excluded(a, c):
    N = a + c + 4; out = set()
    sizes = (a, 2, 2, c)
    base = [(L(a) + 1, 2 * a + 2, 2 * a + 4, L(c) + (a + 4) * c - 1)]
    # the a/c role exchange: F(c, a) with its large bins mapped onto our (a, ..., c) positions
    Fc = (L(c) + 1, 2 * c + 2, 2 * c + 4, L(a) + (c + 4) * a - 1)
    base.append((Fc[3], Fc[1], Fc[2], Fc[0]))
    for f in base:
        for g in (f, (f[0], f[2], f[1], f[3])):
            out.add(g)
            out.add(tuple(sz * (N - 1) - s for sz, s in zip(sizes, g)))
    if a == c:   # equal large sizes may also be exchanged as labels
        for g in list(out): out.add((g[3], g[1], g[2], g[0]))
    return out

def P1(Nmax=14):
    tot_mism = 0
    for N in range(10, Nmax + 1):
        for a in range(3, N - 6):
            c = N - 4 - a
            if c < 3: continue
            sizes = (a, 2, 2, c); vals = range(N); real = set()
            for A in itertools.combinations(vals, a):
                As = set(A); R1 = [x for x in vals if x not in As]; sa = sum(A)
                for B in itertools.combinations(R1, 2):
                    R2 = [x for x in R1 if x not in B]
                    for C in itertools.combinations(R2, 2): real.add((sa, sum(B), sum(C)))
            groups = [I for k in (1, 2, 3) for I in itertools.combinations(range(4), k)]
            ex = excluded(a, c); mism = []; npass = 0
            for sa in range(L(a), a * N):
                for sb in range(1, 2 * N):
                    for sc in range(1, 2 * N):
                        s = (sa, sb, sc, L(N) - sa - sb - sc)
                        ok = all(sum(s[i] for i in I) >= L(sum(sizes[i] for i in I)) for I in groups)
                        pred = ok and s not in ex
                        npass += ok
                        if pred != ((sa, sb, sc) in real): mism.append(s)
            tot_mism += len(mism)
            print(f'  N={N} sizes={sizes}: pass cuts {npass}, realized {len(real)}, excluded family members passing cuts {sum(1 for e in ex)}, mismatches {len(mism)} {mism[:3]}', flush=True)
    return tot_mism

def P2(Amax=80):
    bad = []
    for a in range(3, Amax):
        N = a + 7; full = set(range(N))
        As = (set(range(a)) - {a - 2}) | {a + 1}
        for (B, C, D, tg) in [({a - 2, a + 3}, {a, a + 6}, {a + 2, a + 4, a + 5}, (L(a) + 3, 2 * a + 1, 2 * a + 6, 3 * a + 11)),
                              ({a - 2, a + 4}, {a + 2, a + 6}, {a, a + 3, a + 5}, (L(a) + 3, 2 * a + 2, 2 * a + 8, 3 * a + 8))]:
            parts = [As, B, C, D]
            if sum(len(x) for x in parts) != N or set().union(*parts) != full or [sum(x) for x in parts] != list(tg): bad.append(('lift', a))
        for c in range(3, Amax):
            n = a + c; N = n + 4
            # h = 1: low side {0,1,2,4}; reflected complement must be [0, n-2] U {n}
            comp = sorted(N - 1 - v for v in set(range(N)) - {0, 1, 2, 4})
            if comp != list(range(n - 1)) + [n]: bad.append(('h1', a, c))
            # h = 2: low side {0,1,3,4} (split 04/13); reflected complement must be [0, n-2] U {n+1}
            comp = sorted(N - 1 - v for v in set(range(N)) - {0, 1, 3, 4})
            if comp != list(range(n - 1)) + [n + 1]: bad.append(('h2', a, c))
    return bad

if __name__ == '__main__':
    print('P2 failures:', P2()[:5])
    print('P1 total mismatches:', P1(int(sys.argv[1]) if len(sys.argv) > 1 else 14))
