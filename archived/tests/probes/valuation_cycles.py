#!/usr/bin/env python3
"""L1306 T28 (Local, 2026-11-02): a valuation separator for the top layer, tested on cycles.
reports/rule30-genealogy.md section 33 (predictions written first). Run: python3 tests/probes/valuation_cycles.py

Columns are time-rings of length p = 2L; v(c) is the (1+z)-adic valuation in GF(2)[z]/((1+z)^p). Nested front:
v(c) = L/2 - 1. Candidate S: top-layer states whose columns have v <= L/2 - 2.
- P28a: an explicit valid state in S with a child outside S (O2 fails locally).
- P28b: at p = 32, every nontrivial strongly connected component of the explored pair graph whose columns have least
  period 32 contains a column of valuation exactly 7 (the cycle lemma). Roots: 20,000 random valid fronts and 20,000
  random states with |u OR v| even; at most 1.5e6 states explored; Tarjan on the explored subgraph.
- P28c: valuations of top-layer columns below the front in T_64 (all) and T_128 (all 1,118,828 nodes) stay <= L/2-2.
"""
import random
import sys
from collections import Counter
sys.setrecursionlimit(10000)


def make(p):
    M = (1 << p) - 1

    def integ(d):                      # w(t) = XOR of d(s) for s < t, w(0) = 0
        y, s = d, 1
        while s < p:
            y ^= (y << s) & M
            s <<= 1
        return (y << 1) & M

    def val(c):
        k = 0
        while c:
            if bin(c).count('1') & 1:
                return k
            c = integ(c); k += 1
        return p

    def lp(x):
        q = 1
        while q < p and (((x >> q) | (x << (p - q))) & M) != x:
            q *= 2
        return q
    return M, integ, val, lp


# ---- P28a
p = 32; L = 16; M, integ, val, lp = make(p)
rng = random.Random(28)
u = rng.getrandbits(p) | 1
while bin(u).count('1') % 2 == 0:
    u = rng.getrandbits(p)
v = M ^ u
w = integ(u | v)
print('== P28a: state (u, v) = (%08x, %08x): v(u) = %d, v(v) = %d, |u OR v| = %d; child column w = %08x has v = %d' % (
    u, v, val(u), val(v), bin(u | v).count('1'), w, val(w)))
found = None
for _ in range(200000):
    a, b = rng.getrandbits(p), rng.getrandbits(p)
    if bin(a | b).count('1') & 1 or val(a) > L // 2 - 2 or val(b) > L // 2 - 2:
        continue
    c = integ(a | b)
    if val(c) == L // 2 - 1:
        found = (a, b, c); break
if found:
    a, b, c = found
    print('   a state in S whose child is a nested front: (%08x, %08x), valuations %d, %d -> child %08x, valuation %d' % (
        a, b, val(a), val(b), c, val(c)))

# ---- P28b
A = sum(1 << t for t in range(1, p, 2)); AB = M ^ A; h = p // 2; HM = (1 << h) - 1


def delta(x):
    return x ^ ((x >> 1) | ((x & 1) << (p - 1)))


roots = []
for _ in range(20000):
    vh = rng.getrandbits(h); vv = vh | ((vh ^ HM) << h)
    uh = delta(vv) & HM & rng.getrandbits(h); roots.append((uh | (uh << h), vv))
while len(roots) < 40000:
    a, b = rng.getrandbits(p), rng.getrandbits(p)
    if not bin(a | b).count('1') & 1:
        roots.append((a, b))
CAP = 1500000
edges = {}; st = []
for r in roots:
    if len(edges) >= CAP:
        break
    if r in edges:
        continue
    st.append(r)
    while st and len(edges) < CAP:
        s = st.pop()
        if s in edges:
            continue
        a, b = s; d = a | b
        if bin(d).count('1') & 1:
            edges[s] = ()
        else:
            wv = integ(d); edges[s] = ((b, wv), (b, wv ^ M))
            for t in edges[s]:
                if t not in edges:
                    st.append(t)
explored = set(edges)
print('== P28b: roots used up to the cap; explored states %d' % len(explored))
# iterative Tarjan on the explored subgraph
index = {}; low = {}; onst = set(); stack = []; comps = []; idx = 0
for s0 in explored:
    if s0 in index:
        continue
    work = [(s0, 0)]
    while work:
        s, i = work.pop()
        if i == 0:
            index[s] = low[s] = idx; idx += 1; stack.append(s); onst.add(s)
        succ = [t for t in edges[s] if t in explored]
        if i < len(succ):
            work.append((s, i + 1)); t = succ[i]
            if t not in index:
                work.append((t, 0))
            elif t in onst:
                low[s] = min(low[s], index[t])
            continue
        for t in succ:
            if t in onst:
                low[s] = min(low[s], low[t])
        if low[s] == index[s]:
            comp = []
            while True:
                x = stack.pop(); onst.discard(x); comp.append(x)
                if x == s:
                    break
            if len(comp) > 1 or s in [t for t in edges[s]]:
                comps.append(comp)
        if work:
            parent = work[-1][0]
            low[parent] = min(low[parent], low[s])
rain = {(A, AB), (AB, A)}
summary = Counter(); lemma_fail = []
for comp in comps:
    cs = set(comp)
    if cs <= rain:
        summary['rain'] += 1; continue
    if cs == {(0, 0)}:
        summary['white'] += 1; continue
    cols = [s[1] for s in comp]
    pers = sorted(set(lp(c) for c in cols)); vals = Counter(val(c) for c in cols)
    key = 'size %d, column least periods %s, valuations %s' % (len(comp), pers, dict(sorted(vals.items())))
    summary[key] += 1
    if max(pers) == p and vals[L // 2 - 1] == 0:
        lemma_fail.append(comp)
print('nontrivial strongly connected components: %d' % len(comps))
for k, n in sorted(summary.items(), key=lambda kv: str(kv[0])):
    print('   %4d x %s' % (n, k))
print('least-period-32 components with no column of valuation 7 (cycle-lemma counterexamples): %d' % len(lemma_fail))
for comp in lemma_fail[:3]:
    print('   witness component of %d states, first states: %s' % (len(comp), ', '.join('(%08x,%08x)' % s for s in comp[:4])))

# ---- P28c
for p in (64, 128):
    L = p // 2; M, integ, val, lp = make(p); A = sum(1 << t for t in range(1, p, 2))

    def per(x, n):
        out = 0
        for t in range(p):
            out |= ((x >> (t % n)) & 1) << t
        return out
    stck = [(A, A, 1)]; vc = Counter(); n = 0
    while stck:
        a, b, H = stck.pop(); Lc = 2 * H
        d = (a | b) & ((1 << Lc) - 1); sp = bin(d).count('1') & 1
        if Lc == p:
            n += 1; vc[val(b)] += 1
        H2 = 2 * H if sp else H
        if 2 * H2 > p:
            continue
        L2 = 2 * H2; Mm = (1 << L2) - 1
        y, s = (a | b) & Mm, 1
        while s < L2:
            y ^= (y << s) & Mm; s <<= 1
        w0 = (y << 1) & Mm
        for wv in ([per(w0, L2)] if sp else [per(w0, L2), per(w0 ^ Mm, L2)]):
            stck.append((b, wv, H2))
    below = {k: c for k, c in vc.items() if k != L - 1}
    print('== P28c: T_%d top layer, %d nodes: valuations %s; largest below the front %d (band starts at %d)' % (
        p, n, dict(sorted(vc.items())), max(below), L // 2 - 1))

# ---- P28d (found after the run; hand proof in section 33.3): the valuation passes through the front.
# At a layer root (x, y) of T_p, x = c_(j0-1) is L-periodic and y = c_(j0) is the front. Both children w of the root
# satisfy v_p(w) = v_L(x restricted to one half-period) - 1, whenever the root splits.
for p in (16, 32, 64, 128):
    L = p // 2; M, integ, val, lp = make(p); A = sum(1 << t for t in range(1, p, 2))
    Ml, integl, vall, lpl = make(L)

    def per(x, n):
        out = 0
        for t in range(p):
            out |= ((x >> (t % n)) & 1) << t
        return out
    stck = [(A, A, 1, False)]; ok = bad = dead = 0
    while stck:
        a, b, H, isroot = stck.pop(); Lc = 2 * H
        d = (a | b) & ((1 << Lc) - 1); sp = bin(d).count('1') & 1
        if isroot:
            if sp:
                dead += 1
            else:
                w0 = integ(a | b)
                exp = vall(a & Ml) - 1
                for wv in (w0, w0 ^ M):
                    ok += (val(wv) == exp); bad += (val(wv) != exp)
        H2 = 2 * H if sp else H
        if 2 * H2 > p:
            continue
        L2 = 2 * H2; Mm = (1 << L2) - 1
        y, s2 = (a | b) & Mm, 1
        while s2 < L2:
            y ^= (y << s2) & Mm; s2 <<= 1
        w0 = (y << 1) & Mm
        kids = [per(w0, L2)] if sp else [per(w0, L2), per(w0 ^ Mm, L2)]
        for wv in kids:
            stck.append((b, wv, H2, Lc < p and L2 == p))
    print('== P28d: T_%d layer roots: root dies at once %d; children with v = v_L(x) - 1: %d, exceptions %d' % (p, dead, ok, bad))

