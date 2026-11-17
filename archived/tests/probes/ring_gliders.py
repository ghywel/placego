#!/usr/bin/env python3
"""L1294 T17 (Local, 2026-11-02): every cycle of the full pair graph of p-periodic time-rings, p = 2, 4, 8.
Predictions in reports/rule30-genealogy.md section 29.3, written first. Run: python3 tests/probes/ring_gliders.py

State (u, v): two p-bit time-rings. Edges (u, v) -> (v, w), w = running XOR of u | v from w(0) in {0, 1}, iff |u | v|
is even. A cycle of length m is a light-speed ring glider on m cells. Reports the cyclic strongly connected
components, cycle lengths found by walking each, and reachability from the edge state (0, 1).
"""
import sys
sys.setrecursionlimit(1 << 20)


def run(p):
    M = (1 << p) - 1
    A = sum(1 << t for t in range(1, p, 2))
    pc = lambda x: bin(x).count('1')

    def integ(d):
        y, s = d, 1
        while s < p:
            y ^= (y << s) & M
            s <<= 1
        return (y << 1) & M

    N = 1 << (2 * p)
    succ = [[] for _ in range(N)]
    for u in range(1 << p):
        for v in range(1 << p):
            d = u | v
            if pc(d) & 1:
                continue
            w0 = integ(d)
            succ[(u << p) | v] = [(v << p) | w0, (v << p) | (w0 ^ M)]
    # Tarjan, iterative
    index, low, onst, st, comps, idx = [-1] * N, [0] * N, [False] * N, [], [], 0
    for s0 in range(N):
        if index[s0] >= 0:
            continue
        work = [(s0, 0)]
        while work:
            x, i = work.pop()
            if i == 0:
                index[x] = low[x] = idx; idx += 1; st.append(x); onst[x] = True
            recurse = False
            for j in range(i, len(succ[x])):
                y = succ[x][j]
                if index[y] < 0:
                    work.append((x, j + 1)); work.append((y, 0)); recurse = True; break
                elif onst[y]:
                    low[x] = min(low[x], index[y])
            if recurse:
                continue
            if low[x] == index[x]:
                comp = []
                while True:
                    y = st.pop(); onst[y] = False; comp.append(y)
                    if y == x:
                        break
                if len(comp) > 1 or x in succ[x]:
                    comps.append(comp)
            if work:
                par = work[-1][0]
                low[par] = min(low[par], low[x])
    # reachability from the edge state (0, 1)
    edge = (0 << p) | M
    seen, stack = {edge}, [edge]
    while stack:
        x = stack.pop()
        for y in succ[x]:
            if y not in seen:
                seen.add(y); stack.append(y)
    white, rain = {0}, {(A << p) | (M ^ A), ((M ^ A) << p) | A}
    print(f'p = {p}: states {N}; cyclic components {len(comps)}')
    for comp in sorted(comps, key=len):
        cs = set(comp)
        tag = 'white' if cs == white else 'rain' if cs == rain else 'other'
        ex = comp[0]
        cols = [ex >> p, ex & M]
        print(f'   size {len(comp):6d} ({tag}); reachable from the edge: {bool(cs & seen)}; '
              f'example state (u, v) = ({cols[0]:0{p}b}, {cols[1]:0{p}b})' if len(comp) < 64 or tag != 'other' else
              f'   size {len(comp):6d} ({tag}); reachable from the edge: {bool(cs & seen)}')


for p in (2, 4, 8):
    run(p)
print('RING_GLIDERS_DONE')
