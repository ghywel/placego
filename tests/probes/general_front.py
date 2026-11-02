#!/usr/bin/env python3
"""L1303 (Local, 2026-11-02): is the damage-front lemma true in a general form?
reports/rule30-genealogy.md section 31 (inquisition to GPT). Run: python3 tests/probes/general_front.py

At the first doubled column of an eternal point, the state is (u, v): u has period dividing p/2, v is anti-periodic
(v(t + p/2) = NOT v(t)), and u <= Delta v pointwise (some p/2-periodic column x above has x OR u = Delta v).
General form of the lemma: from every such state, every path dies (no eternal continuation). Edges: (u, v) -> (v, w),
w an integral of u OR v, only if |u OR v| is even. Exhaustive for p <= 16; for p = 32 and 64, valid roots are drawn
directly (v random anti-periodic, u a random p/2-periodic subset of Delta v). For each root that reaches a cycle, the
cycle is named: rain, white, or other (with its size, column least periods, and distinct columns up to rotation).
"""
import random
from collections import Counter


def run(p, sample=None, seed=0):
    rnd = random.Random(seed)
    M = (1 << p) - 1; h = p // 2; HM = (1 << h) - 1
    A = sum(1 << t for t in range(1, p, 2)); AB = M ^ A

    def integ(d):
        w, acc = 0, 0
        for t in range(p):
            if acc:
                w |= 1 << t
            acc ^= (d >> t) & 1
        return w

    def succ(s):
        u, v = s; d = u | v
        if bin(d).count('1') & 1:
            return ()
        w = integ(d)
        return ((v, w), (v, w ^ M))

    def delta(v):
        return v ^ ((v >> 1) | ((v & 1) << (p - 1)))

    roots = []
    if sample is None:
        for uh in range(1 << h):
            for vh in range(1 << h):
                u = uh | (uh << h); v = vh | ((vh ^ HM) << h)
                if not (u & ~delta(v) & M):
                    roots.append((u, v))
    else:
        for _ in range(sample):
            vh = rnd.randrange(1 << h); v = vh | ((vh ^ HM) << h)
            uh = delta(v) & HM & rnd.randrange(1 << h); u = uh | (uh << h)
            roots.append((u, v))
    seen = set(roots); st = list(roots); edges = {}
    while st:
        s = st.pop(); ss = succ(s); edges[s] = ss
        for t in ss:
            if t not in seen:
                seen.add(t); st.append(t)
    outdeg = {s: len(edges[s]) for s in edges}; pred = {}
    for s, ss in edges.items():
        for t in ss:
            pred.setdefault(t, []).append(s)
    dead = [s for s in edges if outdeg[s] == 0]; fin = set(dead)
    while dead:                                   # prune states that cannot reach a cycle
        t = dead.pop()
        for s in pred.get(t, ()):
            outdeg[s] -= 1
            if outdeg[s] == 0 and s not in fin:
                fin.add(s); dead.append(s)
    inf = [r for r in set(roots) if r not in fin]
    rain = {(A, AB), (AB, A)}

    def lp(x):
        q = 1
        while q < p and any(((x >> t) & 1) != ((x >> ((t + q) % p)) & 1) for t in range(p)):
            q *= 2
        return q

    def canon(c):
        return min(((c >> k) | (c << (p - k))) & M for k in range(p))

    def endcycle(r):
        path = {}; s = r; i = 0
        while s not in path:
            path[s] = i; i += 1; s = next(t for t in edges[s] if t not in fin)
        cyc = [x for x, j in path.items() if j >= path[s]]
        if set(cyc) <= rain:
            return 'rain'
        if all(x == (0, 0) for x in cyc):
            return 'white'
        cols = [x[1] for x in cyc]
        return 'other: %d states, column least periods %s, %d distinct columns up to rotation' % (
            len(cyc), sorted(set(lp(c) for c in cols)), len(set(canon(c) for c in cols)))
    kinds = Counter(endcycle(r) for r in inf)
    print('p %d %s: roots %d (distinct %d), reachable states %d, roots with an eternal continuation %d %s' % (
        p, 'exhaustive' if sample is None else 'sampled, seed %d' % seed, len(roots), len(set(roots)), len(edges),
        len(inf), dict(kinds)), flush=True)


for p in (4, 8, 16):
    run(p)
run(16, 3000, 2); run(32, 3000, 2); run(32, 3000, 3); run(64, 200, 2)
