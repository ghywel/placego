#!/usr/bin/env python3
"""g331_g332_review.py: Cloud's carrying-review checks of GPT's G331 and G332. Independent of GPT's engines.
G331: full interval [0,M], counts (2,2,2,c), c = M-5. For every M in [8, MMAX] and every sorted pair-target triple:
      all fourteen cuts (lower and upper rank bounds) versus existence of three disjoint pairs; failures must be exactly
      (2,6,8) and (2M-8,2M-6,2M-2).
G332: [0,M] minus {1}, four counts >= 3: protected cuts t_J >= T(C_J) must imply a partition. Every size pattern with
      M <= MMAX2, by enumerating all partitions.
PREDICTIONS (before any run): G331 failure set exact at every M (0.9); G332 has no protected input without a
partition (0.9).
"""
import sys, itertools
L = lambda r: r * (r - 1) // 2
T = lambda r: r * (r + 1) // 2

def g331(Mmax):
    bad = []; nadm = 0; nfail = 0
    for M in range(8, Mmax + 1):
        c = M - 5; N = M + 1; tot = T(M)
        fib = {u: [(x, u - x) for x in range(0, M + 1) if x < u - x <= M] for u in range(1, 2 * M)}
        U = lambda r: r * (2 * M + 1 - r) // 2
        for a in range(1, 2 * M):
            for b in range(a, 2 * M):
                for d in range(b, 2 * M):
                    w = tot - a - b - d; s = (a, b, d, w); sz = (2, 2, 2, c)
                    ok = all(L(sum(sz[i] for i in I)) <= sum(s[i] for i in I) <= U(sum(sz[i] for i in I))
                             for k in (1, 2, 3) for I in itertools.combinations(range(4), k))
                    if not ok: continue
                    nadm += 1
                    exists = any(not (set(e1) & set(e2)) and not (set(e1) & set(e3)) and not (set(e2) & set(e3))
                                 for e1 in fib[a] for e2 in fib[b] for e3 in fib[d])
                    exc = (a, b, d) in ((2, 6, 8), (2 * M - 8, 2 * M - 6, 2 * M - 2))
                    if not exists: nfail += 1
                    if exists == exc: bad.append((M, a, b, d, exists))
    return nadm, nfail, bad

def g332(Mmax):
    out = []
    for M in range(12, Mmax + 1):
        P = [0] + list(range(2, M + 1)); tot = T(M) - 1
        for sizes in sorted({tuple(sorted(x)) for x in itertools.product(range(3, M), repeat=4) if sum(x) == M}):
            real = set()
            c1, c2, c3, c4 = sizes
            for A in itertools.combinations(P, c1):
                R1 = [x for x in P if x not in A]; sa = sum(A)
                for B in itertools.combinations(R1, c2):
                    Bs = set(B); R2 = [x for x in R1 if x not in Bs]; sb = sum(B)
                    for C in itertools.combinations(R2, c3): real.add((sa, sb, sum(C)))
            groups = [I for k in (1, 2, 3) for I in itertools.combinations(range(4), k)]
            prot = miss = 0; ex = []
            for sa in range(T(c1), tot):
                for sb in range(T(c2), tot - sa):
                    for sc in range(T(c3), tot - sa - sb):
                        s = (sa, sb, sc, tot - sa - sb - sc)
                        if all(sum(s[i] for i in I) >= T(sum(sizes[i] for i in I)) for I in groups):
                            prot += 1
                            if (sa, sb, sc) not in real: miss += 1; ex.append(s)
            out.append((M, sizes, prot, miss, ex[:3]))
            print(f'  G332 M={M} sizes={sizes}: protected inputs {prot}, without a partition {miss} {ex[:3]}', flush=True)
    return out

if __name__ == '__main__':
    nadm, nfail, bad = g331(int(sys.argv[1]) if len(sys.argv) > 1 else 40)
    print(f'G331: admitted {nadm}, failures {nfail}, mismatches with the stated families {len(bad)} {bad[:5]}', flush=True)
    g332(int(sys.argv[2]) if len(sys.argv) > 2 else 14)
