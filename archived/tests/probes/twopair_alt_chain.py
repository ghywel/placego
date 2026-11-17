#!/usr/bin/env python3
"""alt_chain.py (Local, L1519, P-R3): relaxed chains of time-periodic words going DOWN from an alternating top, with no black edge.
A node is (u, w): adjacent diagonals, u the higher. The next lower word z must satisfy Delta u = w OR z at every tick:
  Delta u = 0 forces w = z = 0;  Delta u = 1 with w = 0 forces z = 1;  Delta u = 1 with w = 1 leaves z free.
Top nodes: u alternating, w black on every even tick and not alternating. Reports depth reached and whether a cycle exists."""
import sys
sys.setrecursionlimit(1000000)
def succ(u, w, P):
    M = (1 << P) - 1
    rot = ((u >> 1) | ((u & 1) << (P - 1))) & M        # u(t+1) at bit t
    d = u ^ rot                                        # Delta u
    if w & ~d & M: return []                           # Delta u = 0 with w = 1: dead
    forced = d & ~w & M                                # z = 1 here
    free = w
    bits = [i for i in range(P) if (free >> i) & 1]
    out = []
    for m in range(1 << len(bits)):
        z = forced
        for k, b in enumerate(bits):
            if (m >> k) & 1: z |= 1 << b
        out.append(z)
    return out
for P in (2, 4, 8, 16):
    M = (1 << P) - 1
    alt = sum(1 << i for i in range(1, P, 2))          # black on odd ticks
    evens = sum(1 << i for i in range(0, P, 2))
    tops = []
    for m in range(1 << (P // 2)):
        w = evens
        for k in range(P // 2):
            if (m >> k) & 1: w |= 1 << (2 * k + 1)
        if w != evens: tops.append((alt, w))
    frontier = set(tops); seen = set(tops); depth = 0; sizes = []
    edges = {}
    while frontier and depth < 400:
        nxt = set()
        for (u, w) in frontier:
            ss = succ(u, w, P)
            edges[(u, w)] = [(w, z) for z in ss]
            for z in ss:
                nd = (w, z)
                if nd not in seen:
                    seen.add(nd); nxt.add(nd)
        sizes.append(len(frontier))
        frontier = nxt; depth += 1
        if len(seen) > 3000000: print('  cap reached'); break
    # a cycle among reached nodes?
    color = {}; hascycle = False
    for s in list(seen):
        if s in color: continue
        stack = [(s, iter(edges.get(s, [])))]; color[s] = 1
        while stack:
            nd, it = stack[-1]
            for ch in it:
                c = color.get(ch, 0)
                if c == 1: hascycle = True
                if c == 0:
                    color[ch] = 1; stack.append((ch, iter(edges.get(ch, [])))); break
            else:
                color[nd] = 2; stack.pop()
    print(f'P={P}: tops {len(tops)}, nodes {len(seen)}, BFS depth {depth}, level sizes {sizes[:14]}, cycle {hascycle}')
