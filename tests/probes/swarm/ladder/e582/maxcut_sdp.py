"""maxcut_sdp.py: Erdős #582: the Goemans-Williamson SDP bound as a certificate that a K4-free G arrows (3,3)^e.

RUN-ON:  cpu, python3 with cvxpy and SCS (pip install cvxpy scs).  COST: seconds to minutes (H_G has |E(G)| nodes).
COMMAND: python3 tests/probes/swarm/ladder/e582/maxcut_sdp.py n s1 s2 ...   (the circulant C_n(S))
Why (CL550): build H_G on the edges of G, two edges adjacent when they lie in a common triangle. In a K4-free G each
pair of edges shares at most one triangle, so H_G is the edge-disjoint union of t triangles, one per triangle of G. A
red/blue colouring of E(G) with no one-colour triangle is a cut of H_G that cuts exactly 2 edges of every triangle,
i.e. a cut of size 2t; and no cut exceeds 2t. So G -> (3,3)^e iff MaxCut(H_G) < 2t (Dudek-Rodl; Lange-Radziszowski-Xu
used the SDP bound below to reach 786). Any SDP upper bound below 2t certifies arrowing.
PREDICTIONS (before any run): on small graphs that do not arrow, the bound is >= 2t (inconclusive, as it must be).
Counterfactual: a bound below 2t on a graph a SAT solver colours would mean a bug.
"""
import itertools, sys
import numpy as np, cvxpy as cp

def circulant(n, S):
    S = {s % n for s in S} - {0}; S |= {(-s) % n for s in S}
    return [set((v + s) % n for s in S) for v in range(n)]

def h_graph(n, adj):
    eid = {}
    for u in range(n):
        for v in adj[u]:
            if u < v: eid[(u, v)] = len(eid)
    hedges, t = [], 0
    for u in range(n):
        for v in adj[u]:
            if v <= u: continue
            for w in adj[u] & adj[v]:
                if w <= v: continue
                a, b, c = eid[(u, v)], eid[(u, w)], eid[(v, w)]
                hedges += [(a, b), (a, c), (b, c)]; t += 1
    return len(eid), hedges, t

def sdp_bound(m, hedges):
    X = cp.Variable((m, m), PSD=True)
    obj = sum((1 - X[i, j]) / 2 for i, j in hedges)
    prob = cp.Problem(cp.Maximize(obj), [cp.diag(X) == 1])
    prob.solve(solver=cp.SCS, eps=1e-5, max_iters=20000)
    return prob.value

if __name__ == '__main__':
    n = int(sys.argv[1]); S = [int(x) for x in sys.argv[2:]]
    adj = circulant(n, S)
    m, hedges, t = h_graph(n, adj)
    b = sdp_bound(m, hedges)
    print(f'C_{n}{sorted(set(S))}: |E(G)| = {m}, triangles t = {t}, 2t = {2*t}, SDP bound = {b:.3f}',
          '-> ARROWS (certificate)' if b < 2 * t - 1e-3 else '-> inconclusive')
# OUTCOME (2026-10-22 15:03 BST, Cloud, CL550): calibration only. C_13(1,3,4): 39 edges, 26 triangles, SDP bound 58.5 > 2t = 52,
# inconclusive as predicted. Not yet run on a candidate.
