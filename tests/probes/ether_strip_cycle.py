#!/usr/bin/env python3
"""L1364 T55b (Local, 2026-11-03): extract a minimum-mean invading cycle of ether_strip.py's S = 13 model (44 ticks, one
re-anchoring, mean drift -7/44) and test it exactly: a depth-first search over the right half's bits (cell a + 14
onwards), keeping only bit strings whose column at the moving input position a + 14 - 7j at time 44j + t follows the
cycle's inputs, for PERIODS repetitions. NOT realizable means no right half produces even that many periods of the cycle.
reports/rule30-genealogy.md section 59. Run: python3 tests/probes/ether_strip_cycle.py > cycle.txt;
python3 tests/probes/ether_strip_cycle.py --realize cycle.txt PERIODS
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] == '--realize':
    sys.argv = [sys.argv[0]] + sys.argv[2:]
    import sys, time
    lines = [l for l in open(sys.argv[1]) if l.startswith('ph')]
    PER = int(sys.argv[2])
    TAB = [[0,0,1,1],[0,1,1,0],[1,1,0,1],[0,1,0,1],[0,0,1,1],[0,0,0,1],[0,0,0,1]]
    ph0 = int(lines[0].split()[1]); strip0 = lines[0].split('strip ')[1].split()[0]
    inputs = [int(l.split('input ')[1].split()[0]) for l in lines]
    P = len(inputs)
    LO = -(P + 8) * PER - 60
    def row0(bits):
        r = 0
        for x in range(LO, 1):
            r |= TAB[(2 + x) % 7][ph0] << (x - LO)
        for i, ch in enumerate(strip0):
            r |= int(ch) << (1 + i - LO)
        for i, b in enumerate(bits):
            r |= b << (14 + i - LO)
        return r
    cons = {}   # k -> list of (T, x, required)
    for j in range(PER):
        for t in range(P):
            T = P * j + t; x = 14 - 7 * j
            k = x + T - 13
            cons.setdefault(max(k, 1), []).append((T, x, inputs[t]))
    KMAX = max(cons)
    TMAX = P * PER
    nodes = [0]; best = [0]
    def check(bits):
        k = len(bits)
        need = cons.get(k, [])
        if not need: return True
        r = row0(bits)
        tneed = max(T for T, x, u in need)
        rows = {}
        a = r
        for T in range(0, tneed + 1):
            if T > 0:
                a = (a << 1) ^ (a | (a >> 1))
            rows[T] = a
        return all(((rows[T] >> (x - LO)) & 1) == u for T, x, u in need)
    sys.setrecursionlimit(10000)
    t0 = time.time()
    def dfs(bits):
        nodes[0] += 1
        best[0] = max(best[0], len(bits))
        if len(bits) >= KMAX: return bits
        if time.time() - t0 > 80: return None
        for b in (0, 1):
            nb = bits + [b]
            if check(nb):
                res = dfs(nb)
                if res is not None: return res
        return None
    res = dfs([])
    print('periods %d: %s; DFS nodes %d; deepest bit %d of %d; %.1f s' % (PER, 'REALIZED' if res else ('timeout' if time.time()-t0 > 80 else 'NOT realizable'), nodes[0], best[0], KMAX, time.time() - t0))
    if res: print('right half from a+14:', ''.join(map(str, res)))
else:
    import runpy, sys, io, contextlib
    import numpy as np
    from fractions import Fraction
    sys.argv = ['x', '0']
    import os
    src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ether_strip.py')).read()
    src = src[:src.index('for S in Ss:')]
    g = {}
    exec(compile(src, 'ether_strip', 'exec'), g)
    step, scc = g['step'], g['scc']
    S = 13
    N = 4 << S
    adj = [[] for _ in range(N)]
    lab = {}
    for ph in range(4):
        for s in range(1 << S):
            for u in (0, 1):
                ph2, s2, d = step(ph, s, u, S)
                adj[ph * (1 << S) + s].append((ph2 * (1 << S) + s2, d, u))
    comp, nc = g['scc'](N, [[(w, d) for w, d, u in a] for a in adj])
    cyc = [v for v in range(N) for w, d, u in adj[v] if d < 0 and comp[v] == comp[w]]
    c = comp[cyc[0]]
    mem = [v for v in range(N) if comp[v] == c]
    # search for a cycle of mean -7/44 via reweighting: weight 44*d + 7 >= 0 on every cycle; find a zero-weight cycle
    loc = {v: i for i, v in enumerate(mem)}
    E = [(loc[v], loc[w], 44 * d + 7, u, d) for v in mem for w, d, u in adj[v] if comp[w] == c]
    n = len(mem)
    INF = 10 ** 12
    # Bellman-Ford potentials (no negative cycles), then zero-reduced-cost subgraph has the zero cycles
    pot = [0] * n
    for it in range(n):
        ch = False
        for a, b, w, u, d in E:
            if pot[a] + w < pot[b]:
                pot[b] = pot[a] + w; ch = True
        if not ch: break
    assert not ch, 'negative cycle in reweighted graph?'
    Z = {}
    for a, b, w, u, d in E:
        if pot[a] + w == pot[b]:
            Z.setdefault(a, []).append((b, u, d))
    # find a cycle in Z that contains a re-anchoring (d<0) edge
    for a0, b0, w0, u0, d0 in E:
        if d0 < 0 and pot[a0] + w0 == pot[b0]:
            # BFS from b0 back to a0 in Z
            prev = {b0: None}; q = [b0]
            while q:
                x = q.pop(0)
                if x == a0: break
                for y, u, d in Z.get(x, []):
                    if y not in prev:
                        prev[y] = (x, u, d); q.append(y)
            if a0 in prev:
                path = []; x = a0
                while prev[x] is not None:
                    px, u, d = prev[x]; path.append((px, u, d)); x = px
                path = path[::-1] + [(a0, u0, d0)]
                break
    L = len(path); R = sum(1 for p in path if p[2] < 0)
    print('cycle: %d ticks, %d re-anchorings, mean drift %s' % (L, R, Fraction(-7 * R, L)))
    TAB = g['TAB']
    for (v, u, d) in path:
        gv = mem[v]; ph, s = gv >> S, gv & ((1 << S) - 1)
        eth = ''.join(str(TAB[(2 + i) % 7][ph]) for i in range(-13, 1))
        strip = ''.join(str((s >> i) & 1) for i in range(S))
        print('ph %d  ether..a %s | strip %s | input %d%s' % (ph, eth, strip, u, '  re-anchor -7' if d < 0 else ''))
