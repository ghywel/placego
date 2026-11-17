# Independent check of MI305's pool lemma: P = {0..l-1} u T, T any h-subset of {l..l+2h-1}, m = l + h; for r, q = m - r >= h+1,
# the r-subset sums of P are exactly the integers in [L(r), U_m(r) + delta], delta = sum(P) - L(m).
import itertools
def L(r): return r*(r-1)//2
def U(N, r): return r*(2*N - r - 1)//2
pools = checks = 0; bad = []
for h in (1, 2, 3):
    for m in range(2*h + 2, 15):
        l = m - h
        for T in itertools.combinations(range(l, l + 2*h), h):
            P = list(range(l)) + list(T); delta = sum(P) - L(m); pools += 1
            for r in range(h + 1, m - h):
                sums = {sum(c) for c in itertools.combinations(P, r)}; checks += 1
                if sums != set(range(L(r), U(m, r) + delta + 1)): bad.append((h, m, T, r))
print("pools", pools, "(h, m, T, r) checks", checks, "spectrum failures", len(bad), bad[:3])
# the invalid-cardinality control from MI305: h2, m5, P={0,1,2,5,6}, r=2 (q=3 < h+1) misses 4
P = [0,1,2,5,6]; s = {a+b for a, b in itertools.combinations(P, 2)}; print("control r=2 on {0,1,2,5,6}: missing", sorted(set(range(1, 12)) - s))
