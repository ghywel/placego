#!/usr/bin/env python3
"""L1364 T55b (Local, 2026-11-03): can any disturbance invade the classic ether more than a bounded distance?
reports/rule30-genealogy.md section 59. Run: python3 tests/probes/ether_strip.py S [S ...] [--anchor K]

Background: the kit's classic ether E(t, x) = ether(x mod 7, t mod 4) (alignment absorbed into the anchor's column).
State at time t: an anchor a, a column of ether type K (default 2, the B3 column of Rule30Ether's walls), with G = E on
x <= a, and the exact strip G(t, a+1 .. a+S). Each tick the cell a + S + 1 is a free input u (the adversary; sound).
Next: cells a .. a+S at t+1 by rule 30. If the anchor cell differs from the ether, re-anchor at a - 7: the new strip
a-6 .. a+S-7 is known exactly (ether, the changed cell, the old strip's first S - 7 cells); drift -7. Else drift 0.
Nodes: (t mod 4, strip) for all 2^S strips. Checks:
  C1 control: the kit's 109 wall states (S = 13, K = 2), parsed from Rule30Ether.lean when the kit is present, are
     closed under both inputs with no re-anchoring (wallOK_true);
  C2 the re-anchoring edges that lie on a cycle (same strongly connected component): none means every path
     re-anchors at most R times, R the largest number of re-anchoring edges on a path of the component DAG, so the
     front stays at x >= a(0) - 7R + 1 for every disturbance and every right input sequence;
  C3 if some lie on cycles: the minimum cycle mean of the drift (Karp, per component) bounds the leftward speed.
"""
import os
import sys
from fractions import Fraction

args = sys.argv[1:]
K = 2
if '--anchor' in args:
    i = args.index('--anchor'); K = int(args[i + 1]); del args[i:i + 2]
Ss = [int(a) for a in args] or [13]
TAB = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]


def eth(i, ph):
    """Ether value at anchor offset i (column K + i) and phase ph."""
    return TAB[(K + i) % 7][ph % 4]


def step(ph, s, u, S):
    """Successor (ph', s', drift) of strip s (bit i-1 = cell a+i, i = 1..S) under input u."""
    c = lambda i: eth(i, ph) if i <= 0 else (((s >> (i - 1)) & 1) if i <= S else u)
    n = [c(i - 1) ^ (c(i) | c(i + 1)) for i in range(0, S + 1)]
    ph2 = (ph + 1) % 4
    if n[0] != eth(0, ph2):
        cells = [eth(i, ph2) for i in range(-6, 0)] + [n[0]] + n[1:S - 6]   # a-6 .. a+S-7
        assert len(cells) == S
        return ph2, sum(b << i for i, b in enumerate(cells)), -7
    return ph2, sum(b << (i - 1) for i, b in enumerate(n) if i >= 1), 0


def scc(nodes_n, adj):
    """Iterative Tarjan: component index per node."""
    index = [-1] * nodes_n; low = [0] * nodes_n; on = [False] * nodes_n; comp = [-1] * nodes_n
    st = []; idx = 0; nc = 0
    for root in range(nodes_n):
        if index[root] != -1:
            continue
        work = [(root, 0)]
        while work:
            v, pi = work.pop()
            if pi == 0:
                index[v] = low[v] = idx; idx += 1; st.append(v); on[v] = True
            recurse = False
            for j in range(pi, len(adj[v])):
                w = adj[v][j][0]
                if index[w] == -1:
                    work.append((v, j + 1)); work.append((w, 0)); recurse = True; break
                elif on[w]:
                    low[v] = min(low[v], index[w])
            if recurse:
                continue
            if low[v] == index[v]:
                while True:
                    w = st.pop(); on[w] = False; comp[w] = nc
                    if w == v:
                        break
                nc += 1
            if work:
                u = work[-1][0]
                low[u] = min(low[u], low[v])
    return comp, nc


def wall_states():
    for base in [os.path.expanduser('~/placego-data/t43/kit93/lean'), os.path.expanduser('~/placego-data/t43/kitlean')]:
        p = os.path.join(base, 'Ruliology/CellularAutomata/Rule30Ether.lean')
        if os.path.exists(p):
            src = open(p).read()
            body = src[src.index('def wallStates'):]
            body = body[body.index(':=') + 2:body.index('/-- Closure under')]
            import ast
            return ast.literal_eval(body.replace('true', '1').replace('false', '0').strip())
    return None


for S in Ss:
    N = 4 * (1 << S)
    node = lambda ph, s: ph * (1 << S) + s
    adj = [[] for _ in range(N)]
    for ph in range(4):
        for s in range(1 << S):
            for u in (0, 1):
                ph2, s2, d = step(ph, s, u, S)
                adj[node(ph, s)].append((node(ph2, s2), d))
    if S == 13 and K == 2:
        ws = wall_states()
        if ws is None:
            print('C1 skipped: kit source not found')
        else:
            W = {node(ph, sum(b << i for i, b in enumerate(cells))) for ph, cells in ws}
            closed = all(v in W and d == 0 for x in W for v, d in adj[x])
            print('C1 control: %d wall states, closed under both inputs without re-anchoring: %s' % (len(W), closed))
            assert closed
    comp, nc = scc(N, adj)
    cyc = [(v, w) for v in range(N) for w, d in adj[v] if d < 0 and comp[v] == comp[w]]
    print('S=%d anchor column %d: %d nodes, %d components; re-anchoring edges %d, of which on a cycle: %d' % (
        S, K, N, nc, sum(1 for v in range(N) for w, d in adj[v] if d < 0), len(cyc)), flush=True)
    if not cyc:
        # longest number of re-anchorings along a path of the component DAG (components are numbered in reverse
        # topological order by Tarjan: edges go from higher to lower or equal index)
        best = [0] * nc
        members = [[] for _ in range(nc)]
        for v in range(N):
            members[comp[v]].append(v)
        for c in range(nc):
            m = 0
            for v in members[c]:
                for w, d in adj[v]:
                    if comp[w] != c:
                        m = max(m, best[comp[w]] + (1 if d < 0 else 0))
                    # d < 0 inside a component cannot happen here
            best[c] = m
        R = max(best)
        print('   C2: NO re-anchoring edge on a cycle; at most %d re-anchorings on any path: the front stays at '
              'x >= a(0) - %d + 1 for every disturbance' % (R, 7 * R), flush=True)
    else:
        comps = {comp[v] for v, w in cyc}
        print('   C3: re-anchoring cycles in %d component(s), sizes %s' % (
            len(comps), sorted(sum(1 for v in range(N) if comp[v] == c) for c in comps)[:10]), flush=True)
        for c in comps:                                     # Karp on the component (numpy, exact at the end)
            import numpy as np
            mem = [v for v in range(N) if comp[v] == c]
            loc = {v: i for i, v in enumerate(mem)}
            E = [(loc[v], loc[w], d) for v in mem for w, d in adj[v] if comp[w] == c]
            n = len(mem); src = np.array([e[0] for e in E]); dst = np.array([e[1] for e in E])
            wt = np.array([e[2] for e in E], dtype=np.int64)
            INF = 10 ** 12
            Dk = np.zeros((n + 1, n), dtype=np.int64)
            for k in range(1, n + 1):
                row = np.full(n, INF, dtype=np.int64)
                np.minimum.at(row, dst, Dk[k - 1][src] + wt)
                Dk[k] = row
            ks = np.arange(n)
            with np.errstate(invalid='ignore'):
                ratios = (Dk[n][None, :] - Dk[:n, :]) / (n - ks)[:, None]
            ratios[Dk[:n, :] >= INF // 2] = -np.inf
            vmax = ratios.max(axis=0)
            vmax[Dk[n] >= INF // 2] = np.inf
            v = int(np.argmin(vmax)); k = int(np.argmax(ratios[:, v]))
            mu = Fraction(int(Dk[n][v] - Dk[k][v]), n - k)
            print('   C3: component of %d nodes: minimum cycle mean %s, leftward speed bound %s (%.4f)' % (
                n, mu, -mu, float(-mu)), flush=True)
print('ETHER_STRIP_DONE')
