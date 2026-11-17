#!/usr/bin/env python3
"""g330_review.py: Cloud's carrying-review check of GPT's G330 (two-target pair quotas on an alternating path forest).
For random pools of distinct integers (and some real-valued pools) and two distinct targets u, v: every attainable
(red, blue) count by brute-force matching enumeration, against (a) the hull of the attainable set (no integer holes)
and (b) the finite weighted test (18.3) built from the component intercepts (A_i, B_i). Also checks the forest claim.
PREDICTIONS (before any run): attainable = (18.3) everywhere (0.9); no integer hull holes (0.9); no cycles (0.99).
"""
import random, itertools
from fractions import Fraction as Fr

def graph(pool, u, v):
    S = set(pool); red = [(x, u - x) for x in pool if x < u - x and u - x in S]
    blue = [(x, v - x) for x in pool if x < v - x and v - x in S]
    return red, blue

def attainable(red, blue):
    edges = [(e, 0) for e in red] + [(e, 1) for e in blue]; out = set()
    def go(i, used, r, b):
        if i == len(edges): out.add((r, b)); return
        go(i + 1, used, r, b)
        (x, y), c = edges[i]
        if x not in used and y not in used: go(i + 1, used | {x, y}, r + (c == 0), b + (c == 1))
    go(0, frozenset(), 0, 0); return out

def components(red, blue):
    adj = {}
    for (x, y) in red + blue: adj.setdefault(x, []).append(y); adj.setdefault(y, []).append(x)
    col = {frozenset(e): 0 for e in red}; col.update({frozenset(e): 1 for e in blue})
    seen = set(); comps = []; cyc = False
    for s in adj:
        if s in seen: continue
        stack = [s]; verts = set()
        while stack:
            x = stack.pop()
            if x in verts: continue
            verts.add(x); stack += adj[x]
        seen |= verts
        es = {frozenset((x, y)) for x in verts for y in adj[x]}
        if len(es) >= len(verts): cyc = True; continue
        ends = [x for x in verts if len(adj[x]) == 1]
        cols = [col[e] for e in es]; ell = len(es); k = ell // 2
        if ell % 2 == 0: A, B = k, k
        else:
            endcols = {col[frozenset((x, adj[x][0]))] for x in ends}
            A, B = (k + 1, k) if endcols == {0} else (k, k + 1)
        comps.append((A, B))
    return comps, cyc

def predicted(comps, r, s):
    normals = [(1, 0), (0, 1)] + [(B, A) for A, B in comps if A * B > 0]
    return all(p * r + q * s <= sum(max(p * A, q * B) for A, B in comps) for p, q in normals)

def in_hull(pts, r, s):
    pts = list(pts)
    # point in convex hull of finite planar set: check against every supporting line from pairs (brute force)
    if (r, s) in pts: return True
    hull = sorted(set(pts))
    def cross(o, a, b): return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    lower, upper = [], []
    for p in hull:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0: lower.pop()
        lower.append(p)
    for p in reversed(hull):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0: upper.pop()
        upper.append(p)
    H = lower[:-1] + upper[:-1]
    if len(H) < 3:
        if len(H) == 1: return (r, s) == H[0]
        a, b = H; return cross(a, b, (r, s)) == 0 and min(a[0], b[0]) <= r <= max(a[0], b[0]) and min(a[1], b[1]) <= s <= max(a[1], b[1])
    return all(cross(H[i], H[(i + 1) % len(H)], (r, s)) >= 0 for i in range(len(H)))

if __name__ == '__main__':
    random.seed(20261020); n = mism = holes = cycles = 0
    for trial in range(6000):
        size = random.randint(2, 15); top = random.randint(size, 40)
        pool = sorted(random.sample(range(top + 1), size))
        if trial % 5 == 0: pool = [Fr(x, 1) + Fr(random.randint(0, 2), 3) for x in pool]; pool = sorted(set(pool))
        u = random.choice([a + b for a in pool for b in pool if a != b] or [1]); v = random.choice([a + b for a in pool for b in pool if a != b] or [2])
        if u == v: continue
        red, blue = graph(pool, u, v)
        comps, cyc = components(red, blue); cycles += cyc
        att = attainable(red, blue); n += 1
        R = max(r for r, _ in att) + 1; Sm = max(s for _, s in att) + 1
        for r in range(R + 1):
            for s in range(Sm + 1):
                if ((r, s) in att) != predicted(comps, r, s): mism += 1
                if (r, s) not in att and in_hull(att, r, s): holes += 1
    print(f'pools {n}: cycles found {cycles}, (18.3) mismatches {mism}, integer hull holes {holes}')
    # can-fail control: an alternating 4-cycle (not an additive two-sum graph) has the hole (1,1)
    att = {(0, 0), (1, 0), (0, 1), (2, 0), (0, 2)}
    print('control C4 hole (1,1) detected by in_hull:', in_hull(att, 1, 1) and (1, 1) not in att)
