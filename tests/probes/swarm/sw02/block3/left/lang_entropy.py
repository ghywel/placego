#!/usr/bin/env python3
"""Entropy and periodic words of the exact gap languages, width by width.

Prediction, written before the run. X: entropy per step is positive and constant over W = 38 to 41, since its language
does not change. Y: entropy per step falls with W from 40 to 60 and stays positive (0.6). Counterfactual: Y's entropy
reaches zero, so Y holds only finitely many periodic words and transitions, and every play in it ends periodic: harmless.

Weighted by step: a gap g takes g steps, so the growth rate r per step solves spectral radius of M(r) = 1, where
M(r)[s][t] = sum over gaps g from s to t of r^-g. Entropy per step is log2 r.
Usage: lang_entropy.py FILE...
"""
import collections, sys
import numpy as np
import scipy.sparse as sp
from scipy.sparse.csgraph import connected_components

def load(path):
    T = {}
    for line in open(path):
        p = line.split(); s = int(p[0]); T[s] = {}
        for x in p[2:]:
            g, t = x.split(':'); T[s][int(g)] = int(t)
    return T
def minimise(T):
    letters = sorted({g for r in T.values() for g in r})
    part = {s: 0 for s in T}; part[-1] = 1
    while True:
        sig = {s: (part[s],) + tuple(part[T[s].get(g, -1)] if s != -1 else part[-1] for g in letters) for s in part}
        ids = {}
        new = {s: ids.setdefault(v, len(ids)) for s, v in sig.items()}
        if len(ids) == len(set(part.values())): break
        part = new
    M = collections.defaultdict(dict)
    for s in T:
        for g, t in T[s].items(): M[part[s]][g] = part[t]
    return M
def radius(edges, n, r):
    rows = [e[0] for e in edges]; cols = [e[1] for e in edges]; vals = [r ** (-e[2]) for e in edges]
    A = sp.csr_matrix((vals, (rows, cols)), shape=(n, n))
    x = np.ones(n) / n; lam = 0
    for i in range(4000):
        y = A @ (A @ x)
        s = y.sum()
        if s == 0: return 0.0
        y /= s; nl = s ** 0.5
        if abs(nl - lam) < 1e-13: lam = nl; break
        lam = nl; x = y
    return lam
for path in sys.argv[1:]:
    M = minimise(load(path))
    ids = {s: i for i, s in enumerate(M)}
    n = len(ids)
    E = [(ids[s], ids[t], g) for s, r in M.items() for g, t in r.items() if t in ids]
    A = sp.csr_matrix(([1] * len(E), ([e[0] for e in E], [e[1] for e in E])), shape=(n, n))
    nc, lab = connected_components(A, directed=True, connection='strong')
    sizes = collections.Counter(lab.tolist())
    big = [c for c, k in sizes.items() if k > 1]
    res = []
    for c in big:
        v = np.nonzero(lab == c)[0]; mp = {int(x): i for i, x in enumerate(v)}
        e = [(mp[a], mp[b], g) for a, b, g in E if a in mp and b in mp]
        lo, hi = 1.0, 2.0
        for _ in range(50):
            m = (lo + hi) / 2
            if radius(e, len(v), m) > 1: lo = m
            else: hi = m
        res.append((len(v), round(float(np.log2(lo)), 6)))
    # periodic words: closed walks in steps, up to 400 steps, by walking the DFA from every state
    st = {i: collections.Counter() for i in range(1)}
    cyc = collections.Counter()
    adj = collections.defaultdict(list)
    for a, b, g in E: adj[a].append((b, g))
    L = 260
    if n <= 8000:
        import itertools
        rec = set()
        for c in big: rec |= set(np.nonzero(lab == c)[0].tolist())
        # number of closed walks of each step length: dynamic programming per state is costly; use vectors for a sample of lengths
        P = np.zeros(L + 1)
        I = np.eye(n, dtype=np.float32) if n <= 1500 else None
        if I is not None:
            W = [None] * (L + 1); W[0] = I
            G = collections.defaultdict(lambda: np.zeros((n, n), dtype=np.float32))
            for a, b, g in E: G[g][a, b] += 1
            for l in range(1, L + 1):
                acc = np.zeros((n, n), dtype=np.float32)
                for g, Mg in G.items():
                    if l - g >= 0: acc += W[l - g] @ Mg
                W[l] = acc
                P[l] = np.trace(acc)
            nz = [l for l in range(1, L + 1) if P[l] > 0]
        else:
            nz = None
    print(path.split('/')[-1], 'minimal states', n, 'recurrent parts (states, bits per step)', sorted(res, reverse=True)[:3], 'closed-walk lengths', (nz[:16] if n <= 1500 else 'skipped'))
