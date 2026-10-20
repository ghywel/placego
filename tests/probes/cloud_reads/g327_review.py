#!/usr/bin/env python3
"""g327_review.py: Cloud's carrying-review checks of GPT's G327 (four prescribed sums on [0, N-1], at most one size-2 bin).
S1  Step 1: the pair spectra of P_m(h) and Q_m(h) contain [1+h, 2m-3] for c = m-2 >= 3 and 0 <= h < 2c; m up to MMAX1.
S2  The statement, both directions: for every size pattern (2,b,c,d), b,c,d >= 3, N <= NMAX, the set of target tuples
    realized by some partition equals the set passing all fourteen lower cuts S_I >= L(C_I).
S3  Step 3's normalization: for the recipe A = [0,l-1] U [N-k,N-1] U {p}, h = s_A - L(a) = kM + q with M = N-a, q = p-l,
    and the sum of the normalized remaining targets is L(M+1) - q. Checked for N < 60.
PREDICTIONS (before any run): S1 holds (0.9); S2 has no mismatch to N = 14 (0.85); S3 holds (0.95).
"""
import sys, itertools
from collections import defaultdict
L = lambda r: r * (r - 1) // 2
T = lambda r: r * (r + 1) // 2

def staircase(m, h):
    if h == 0: return list(range(m)), list(range(m))
    s = 1
    while T(s + 1) <= h: s += 1
    t = h - T(s); assert 0 <= t <= s
    p = m - s
    P = list(range(p)) + [p + 2 * j + 1 + (1 if j >= s - t else 0) for j in range(s)]
    if t == 0: Q = P
    else:
        S = s + 1; q = m - S
        Q = list(range(q)) + [q + 2 * j + 1 - (1 if j >= t else 0) for j in range(S)]
    return P, Q

def S1(Mmax=300):
    bad = []
    for m in range(5, Mmax + 1):
        c = m - 2
        for h in range(0, 2 * c):
            for name, pool in zip('PQ', staircase(m, h)):
                if len(pool) != m or len(set(pool)) != m or min(pool) < 0: bad.append((name, m, h, 'bad pool')); continue
                if sum(pool) != L(m) + h: bad.append((name, m, h, 'sum')); continue
                sums = {x + y for x, y in itertools.combinations(pool, 2)}
                miss = [z for z in range(1 + h, 2 * m - 2) if z not in sums]
                if miss: bad.append((name, m, h, miss[:3]))
    return bad

def S2(Nmax=14):
    out = []
    for N in range(11, Nmax + 1):
        for b in range(3, N):
            for c in range(b, N):
                d = N - 2 - b - c
                if d < c: continue
                sizes = (2, b, c, d)
                real = set()
                vals = range(N)
                for A in itertools.combinations(vals, 2):
                    R1 = [x for x in vals if x not in A]
                    for B in itertools.combinations(R1, b):
                        Bs = set(B); R2 = [x for x in R1 if x not in Bs]
                        sb = sum(B)
                        for C in itertools.combinations(R2, c):
                            real.add((sum(A), sb, sum(C)))
                tot = L(N); cuts_ok = 0; mism = []
                groups = [I for k in (1, 2, 3) for I in itertools.combinations(range(4), k)]
                for s1 in range(1, 2 * N):
                    for s2 in range(L(b), b * N):
                        for s3 in range(L(c), c * N):
                            s = (s1, s2, s3, tot - s1 - s2 - s3)
                            ok = all(sum(s[i] for i in I) >= L(sum(sizes[i] for i in I)) for I in groups)
                            if ok: cuts_ok += 1
                            if ok != ((s1, s2, s3) in real): mism.append(s)
                out.append((N, sizes, len(real), cuts_ok, mism[:3], len(mism)))
                print(f'  N={N} sizes={sizes}: realized {len(real)}, pass all 14 cuts {cuts_ok}, mismatches {len(mism)}', flush=True)
    return out

def S3(Nmax=60):
    bad = 0
    for N in range(4, Nmax):
        for a in range(2, N - 1):
            M = N - a
            for k in range(a):
                l = a - 1 - k
                for p in range(l, N - k):
                    A = list(range(l)) + list(range(N - k, N)) + [p]
                    h = sum(A) - L(a); q = p - l
                    rem_norm = sum(x - l for x in range(N) if x not in A)
                    if h != k * M + q or rem_norm != L(M + 1) - q: bad += 1
    return bad

if __name__ == '__main__':
    print('S3 normalization mismatches:', S3())
    b1 = S1(); print('S1 pair-lemma failures:', len(b1), b1[:5])
    S2(int(sys.argv[1]) if len(sys.argv) > 1 else 14)
