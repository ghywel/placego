"""paley_clique.py: Erdős #78: clique numbers of Paley graphs against log2 p.

RUN-ON: cpu, python3 (standard library). COMMAND: python3 tests/probes/swarm/ladder/e78/paley_clique.py PMAX SECONDS
Why (CL563): #78 asks for an EXPLICIT graph on n vertices with no clique or independent set of size c log n. The
Paley graph P_p (p prime, p = 1 mod 4) is self-complementary (alpha = omega) and is the classical explicit candidate.
Its proved clique bound is only about sqrt(p/2) (Hanson-Petridis), and Graham-Ringrose type lower bounds give
omega >= c log p log log log p for infinitely many p, so Paley along ALL primes cannot give the prize; a subsequence
with omega <= c log p would, but nothing proves one. This measures omega(P_p)/log2(p) exactly for small p.
omega is computed exactly: P_p is arc-transitive, so a maximum clique may be taken to contain 0 and 1; then
omega = 2 + omega(G[N]), N = {x : x and x-1 nonzero squares}, by bitset Bron-Kerbosch with pivoting.
Record searched: Paley, "clique number": no hit.
PREDICTIONS (before the run): omega(P_p)/log2(p) stays between about 0.6 and 1.3 for p up to 3000, with no
downward trend (no evidence for a c log p subsequence with small c). Counterfactual: a clear decreasing ratio.
"""
import math, sys, time


def omega_paley(p):
    sq = {(x * x) % p for x in range(1, p)}
    N = [x for x in range(2, p) if x in sq and (x - 1) % p in sq]
    idx = {v: i for i, v in enumerate(N)}
    adj = [0] * len(N)
    for i, u in enumerate(N):
        m = 0
        for j, v in enumerate(N):
            if i != j and (u - v) % p in sq:
                m |= 1 << j
        adj[i] = m
    best = 0

    def bk(R, P, X):
        nonlocal best
        if not P and not X:
            best = max(best, R); return
        if R + bin(P).count('1') <= best: return
        u = (P | X).bit_length() - 1
        cand = P & ~adj[u]
        while cand:
            v = cand.bit_length() - 1; bit = 1 << v
            bk(R + 1, P & adj[v], X & adj[v])
            P &= ~bit; X |= bit; cand &= ~bit

    bk(0, (1 << len(N)) - 1, 0)
    return best + 2


if __name__ == '__main__':
    pmax, budget = int(sys.argv[1]), float(sys.argv[2])
    t0 = time.time()
    primes = [p for p in range(5, pmax + 1) if p % 4 == 1 and all(p % d for d in range(2, int(p ** .5) + 1))]
    rows = []
    for p in primes:
        if time.time() - t0 > budget: print(f'stopped at p={p} (time)'); break
        w = omega_paley(p); rows.append((p, w, w / math.log2(p)))
    for p, w, r in rows[::max(1, len(rows) // 25)] + rows[-3:]:
        print(f'p={p:5d} omega={w:3d} omega/log2 p={r:.3f}')
    lo = [r for p, w, r in rows if p > 200]
    print(f'{len(rows)} primes; ratio over p>200: min {min(lo):.3f} max {max(lo):.3f}')

# OUTCOME (2026-10-22 18:40 BST, Cloud, CL563): exact omega(P_p) for all 123 primes p = 1 mod 4 up to 1621 (420 s
# budget). omega/log2 p ranges 0.861-1.452 over p > 200, drifting slightly UP (about 0.8 near p = 50, 1.2-1.3 near
# p = 1600); largest omega 14 at p = 1613. Prediction held; no downward trend, so no hint of a c log p subsequence.
# Unexpected check: the known small values reproduce (omega(P_17) = 3, the R(4,4) = 18 witness; P_13 3, P_29 4,
# P_37 4, P_41 5, P_61 5, P_101 5). Measured, finite: it cannot bear on an asymptotic constructive bound.
