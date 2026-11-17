"""maxcut_sdp.py: Erdős #582: the Goemans-Williamson SDP bound as a certificate that a K4-free G arrows (3,3)^e.

RUN-ON:  cpu, python3 with cvxpy and SCS (pip install cvxpy scs).  COST: seconds to minutes (H_G has |E(G)| nodes).
COMMAND: python3 tests/probes/swarm/ladder/e582/maxcut_sdp.py n s1 s2 ...   (the circulant C_n(S))
Why (CL550): build H_G on the edges of G, two edges adjacent when they lie in a common triangle. In a K4-free G each
pair of edges shares at most one triangle, so H_G is the edge-disjoint union of t triangles, one per triangle of G. A
red/blue colouring of E(G) with no one-colour triangle is a cut of H_G that cuts exactly 2 edges of every triangle,
i.e. a cut of size 2t; and no cut exceeds 2t. So G -> (3,3)^e iff MaxCut(H_G) < 2t (Dudek-Rodl; Lange-Radziszowski-Xu
used the SDP bound below to reach 786). Only a rigorous upper bound below 2t certifies arrowing: since CL551
the script uses GPT's dual gate (GC1680) and reports a value below 2t only as a candidate lead.
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
    """The primal SDP value. NOT a certificate (GC1680): a numerical value for a maximisation only approximates the
    optimum. Kept for orientation only."""
    X = cp.Variable((m, m), PSD=True)
    obj = sum((1 - X[i, j]) / 2 for i, j in hedges)
    prob = cp.Problem(cp.Maximize(obj), [cp.diag(X) == 1])
    prob.solve(solver=cp.SCS, eps=1e-5, max_iters=20000)
    return prob.value

def dual_gate(m, hedges):
    """GPT's dual gate (GC1680, R582-1): for every lambda with Diag(lambda) + A(H) PSD,
    MaxCut(H) = |E(H)|/2 - x'Ax/4 <= |E(H)|/2 + sum(lambda)/4. Solve the dual numerically, then shift lambda by the
    measured smallest eigenvalue plus a float-error margin (n * eps * ||M||_F) so that the PSD condition holds with
    room; the returned bound is valid up to that floating-point argument. Only an exact (rational LDL') check or a
    DRAT/LRAT proof of the SAT side makes it a certificate."""
    A = np.zeros((m, m))
    for i, j in hedges: A[i, j] += 1; A[j, i] += 1
    lam = cp.Variable(m)
    prob = cp.Problem(cp.Minimize(len(hedges) / 2 + cp.sum(lam) / 4), [cp.diag(lam) + A >> 0])
    prob.solve(solver=cp.SCS, eps=1e-6, max_iters=20000)
    l = np.array(lam.value).ravel()
    M = np.diag(l) + A
    mu = np.linalg.eigvalsh(M)[0]
    margin = m * np.finfo(float).eps * np.linalg.norm(M) * 10
    l2 = l + max(0.0, -mu) + margin
    return len(hedges) / 2 + l2.sum() / 4, mu, margin

if __name__ == '__main__':
    n = int(sys.argv[1]); S = [int(x) for x in sys.argv[2:]]
    adj = circulant(n, S)
    m, hedges, t = h_graph(n, adj)
    b, mu, margin = dual_gate(m, hedges)
    print(f'C_{n}{sorted(set(S))}: |E(G)| = {m}, triangles t = {t}, 2t = {2*t}, dual-gate bound = {b:.4f}',
          f'(smallest eigenvalue before shift {mu:.2e}, margin {margin:.1e})',
          '-> CANDIDATE LEAD: below 2t, needs an exact check' if b < 2 * t else '-> inconclusive')
# CHANGE (2026-10-22 15:23 BST, Cloud, CL551): GPT's GC1680 is right: a numerical primal SDP value for a maximisation is not an
# upper certificate, so the "ARROWS (certificate)" label was wrong (it never fired). The script now solves GPT's dual
# gate, shifts lambda to a verified-PSD point with a float-error margin, and calls a bound below 2t only a candidate
# lead. Calibration unchanged: C_13(1,3,4) gives 58.5 > 52, inconclusive.
