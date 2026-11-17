#!/usr/bin/env python3
"""Cloud CL774/CL775: K-09's first step.  Two equal-length returns in the branching component of the
period-15 core, read off the census core (cloud_core15_pairs.txt, from cloud_core_census.c).

Frame: a vertex is a pair (c, d) of 15-tick profiles at sites i+1, i+2; children (u, c) with
u(t+1) = u(t) xor (c(t) or d(t)) cyclically; bit t of a word is tick t.  Index = c << 15 | d.
Usage: cloud_period15_tiles.py cloud_core15_pairs.txt
"""
import sys, itertools
from collections import deque

P = 15; FULL = (1 << P) - 1
pc = lambda x: bin(x).count("1")
rot = lambda w, k: ((w >> (k % P)) | (w << (P - k % P))) & FULL


def prefix(m):
    w = 0; bit = 0
    for t in range(P - 1):
        bit ^= (m >> t) & 1; w |= bit << (t + 1)
    return w


def children(v):
    c, d = v; m = c | d
    if pc(m) & 1:
        return []
    w = prefix(m)
    return [(w, c), (w ^ FULL, c)]


def main(path):
    core = set()
    for line in open(path):
        n = int(line); core.add((n >> P, n & FULL))
    adj = {v: [x for x in children(v) if x in core] for v in core}
    # the branching component: vertices that reach a branch vertex and are reached from one
    branch_all = [v for v in core if len(adj[v]) == 2]
    def reach(src, g):
        seen = set(src); work = list(src)
        while work:
            v = work.pop()
            for x in g[v]:
                if x not in seen:
                    seen.add(x); work.append(x)
        return seen
    radj = {v: [] for v in core}
    for v in core:
        for x in adj[v]:
            radj[x].append(v)
    comp = reach(branch_all, adj) & reach(branch_all, radj)
    edges = sum(1 for v in comp for x in adj[v] if x in comp)
    branch = sorted(v for v in comp if sum(1 for x in adj[v] if x in comp) == 2)
    print("core pairs", len(core), "| branching component: pairs", len(comp), "edges", edges, "branch vertices", len(branch))
    assert all(x in comp for v in comp for x in adj[v])

    # K5: weights of the two continuing children at each branch vertex
    split = {}
    for b in branch:
        ws = tuple(sorted(pc(x[0]) for x in adj[b]))
        split[ws] = split.get(ws, 0) + 1
    print("K5 weights of the two continuing children at the branch vertices: (weights): vertices", sorted(split.items()))
    orbs = set()
    for b in branch:
        orbs.add(min((rot(b[0], k), rot(b[1], k)) for k in range(P)))
    print("   rotation classes of branch vertices:", len(orbs), "| column weights of the branch pairs by class:",
          sorted((pc(o[0]), pc(o[1])) for o in orbs))

    # segments between branch vertices
    bset = set(branch); seg = {}
    for b in branch:
        for ch in adj[b]:
            p = [b, ch]
            while p[-1] not in bset:
                p.append(adj[p[-1]][0])
            seg[(b, ch)] = p
    lens = {}
    for p in seg.values():
        lens[len(p) - 1] = lens.get(len(p) - 1, 0) + 1
    print("first-return segments between branch vertices:", len(seg), "| (cells: segments)", sorted(lens.items()),
          "| self-returns", sum(1 for (b, ch), p in seg.items() if p[-1] == b))

    # K2: growth rate by power iteration
    idx = {v: i for i, v in enumerate(sorted(comp))}
    vec = [1.0] * len(idx); rho = 0.0
    for _ in range(4000):
        new = [0.0] * len(idx)
        for v, i in idx.items():
            for x in adj[v]:
                new[idx[x]] += vec[i]
        s = sum(new); rho = s / sum(vec); vec = [a / s for a in new]
    print("K2 growth rate of the component (4000 iterations):", round(rho, 6))
    # exact count check: closed walks of length n in the component, ratio
    import math
    cyc_lens = {}
    dist_back = {}
    # girth
    best = None
    for s0 in list(comp):
        d = {s0: 0}; work = deque([s0]); found = None
        while work and found is None:
            v = work.popleft()
            for x in adj[v]:
                if x == s0:
                    found = d[v] + 1; break
                if x not in d:
                    d[x] = d[v] + 1; work.append(x)
        if found and (best is None or found < best):
            best = found
    print("   shortest cycle in the component:", best, "cells")

    # K1, K4: least length with two closed walks at one vertex
    def closed_counts(b, Lmax):
        cur = {b: 1}; out = []
        for L in range(1, Lmax + 1):
            nxt = {}
            for v, c in cur.items():
                for x in adj[v]:
                    nxt[x] = nxt.get(x, 0) + c
            cur = nxt; out.append(cur.get(b, 0))
        return out
    Lmax = 400; least = {}
    for b in branch:
        cc = closed_counts(b, Lmax)
        L = next((i + 1 for i, c in enumerate(cc) if c >= 2), None)
        least[b] = (L, cc[L - 1] if L else None)
    Lmin = min(v[0] for v in least.values() if v[0])
    at = sorted(b for b, v in least.items() if v[0] == Lmin)
    dist = {}
    for v in least.values():
        dist[v] = dist.get(v, 0) + 1
    print("K1 least length with at least two closed walks, over the 30 branch vertices: (length, walks): vertices",
          sorted(dist.items()))
    print("   least over all:", Lmin, "cells, at", len(at), "branch vertices; first:", at[0])
    B = at[0]
    # enumerate the closed walks of length Lmin at B
    back = {B: 0}; work = deque([B])
    while work:
        v = work.popleft()
        for x in radj[v]:
            if x in comp and x not in back:
                back[x] = back[v] + 1; work.append(x)
    walks = []
    def dfs(path):
        rem = Lmin - (len(path) - 1)
        v = path[-1]
        if rem == 0:
            if v == B:
                walks.append(list(path))
            return
        for x in adj[v]:
            if back.get(x, 10 ** 9) <= rem - 1:
                path.append(x); dfs(path); path.pop()
    sys.setrecursionlimit(10000)
    dfs([B])
    print("K4 closed walks of length", Lmin, "at that vertex:", len(walks))
    def events(w):                       # which child was taken at each branch vertex passed
        ev = []
        for a, b2 in zip(w, w[1:]):
            if a in bset:
                ev.append(adj[a].index(b2))
        return "".join(map(str, ev))
    tiles = []
    for w in walks:
        tile = "".join(str(v[0] & 1) for v in w[1:])[::-1]     # tick-0 cells of the new profiles, increasing site order
        tiles.append(tile)
        print("   walk with branch choices", events(w), "| returns to the vertex on the way:", sum(1 for v in w[1:-1] if v == B),
              "\n      tile:", tile)
    print("   tiles distinct:", len(set(tiles)) == len(tiles),
          "| positions where the first two differ:", [i for i in range(Lmin) if tiles[0][i] != tiles[1][i]][:12])

    # K3: rings from words in the first two tiles
    def tau(x):
        n = len(x); return [x[i] ^ (x[(i + 1) % n] | x[(i + 2) % n]) for i in range(n)]
    def Fstep(x):
        n = len(x); return [x[(j - 1) % n] ^ (x[j] | x[(j + 1) % n]) for j in range(n)]
    ok = True; tested = 0; lowp = 0
    for n in range(1, 5):
        for word in itertools.product((0, 1), repeat=n):
            x = [int(ch) for wd in word for ch in tiles[wd]]
            y = x; ret = {}
            for k in range(1, 16):
                y = tau(y); ret[k] = (y == x)
            z = x
            for _ in range(15):
                z = Fstep(z)
            law = all(z[(i + 15) % len(x)] == x[i] for i in range(len(x)))
            ok &= ret[15] and law and not (ret[1] or ret[3] or ret[5])
            tested += 1
    print("K3 rings from every word of 1 to 4 tiles: return after 15 moving steps, the ordinary rule gives "
          "evol x 15 (i + 15) = x i, and no return after 1, 3 or 5:", ok, "| rings", tested)
    print("   entropy from two tiles of", Lmin, "cells:", round(1 / Lmin, 5), "bits per cell | log2 of the growth rate:",
          round(math.log2(rho), 5))
    # Added after run 1 (kept as cloud_period15_tiles_run1.out): half the branch vertices carry three
    # closed walks of the least length.  Extract the three tiles at the first such vertex.
    three = sorted(b for b, v in least.items() if v == (Lmin, 3))
    if three:
        B3 = three[0]
        back3 = {B3: 0}; work = deque([B3])
        while work:
            v = work.popleft()
            for x in radj[v]:
                if x in comp and x not in back3:
                    back3[x] = back3[v] + 1; work.append(x)
        w3 = []
        def dfs3(path):
            rem = Lmin - (len(path) - 1); v = path[-1]
            if rem == 0:
                if v == B3:
                    w3.append(list(path))
                return
            for x in adj[v]:
                if back3.get(x, 10 ** 9) <= rem - 1:
                    path.append(x); dfs3(path); path.pop()
        dfs3([B3])
        t3 = ["".join(str(v[0] & 1) for v in w[1:])[::-1] for w in w3]
        print("three-tile vertex", B3, "| closed walks of", Lmin, "cells:", len(w3))
        for w, t in zip(w3, t3):
            print("   branch choices", events(w), "tile:", t)
        cols = [i for i in range(Lmin) if len({t[i] for t in t3}) > 1]
        print("   tiles distinct:", len(set(t3)) == 3, "| positions where they differ:", cols,
              "| letters there:", ["".join(t[i] for i in cols) for t in t3])
        ok3 = True; n3 = 0
        for n in range(1, 4):
            for word in itertools.product((0, 1, 2), repeat=n):
                x = [int(ch) for wd in word for ch in t3[wd]]
                y = x; ret = {}
                for k in range(1, 16):
                    y = tau(y); ret[k] = (y == x)
                ok3 &= ret[15] and not (ret[1] or ret[3] or ret[5]); n3 += 1
        print("   rings from every word of 1 to 3 of the three tiles return after 15 moving steps and not after 1, 3, 5:",
              ok3, "| rings", n3, "| entropy from three tiles:", round(math.log2(3) / Lmin, 5), "bits per cell")
    # profile lists for a builder: the 31 new 15-tick profiles of each walk, in increasing site order
    print("profiles (bit t = tick t), increasing site order; every walk starts and ends at its vertex")
    for name, vtx, ws in (("two-tile vertex", B, walks), ("three-tile vertex", three[0] if three else None, w3 if three else [])):
        print("  ", name, vtx)
        for w in ws:
            print("      choices", events(w), [v[0] for v in w[1:]][::-1])
    print("   pair periods in the component:", sorted({min(k for k in (1, 3, 5, 15) if rot(v[0], k) == v[0] and rot(v[1], k) == v[1]) for v in comp}))
    print("   equations a kernel certificate would check for two tiles: 4 seams x", Lmin, "sites x 15 ticks =", 4 * Lmin * 15)


if __name__ == "__main__":
    main(sys.argv[1])
