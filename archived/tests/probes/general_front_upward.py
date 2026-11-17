#!/usr/bin/env python3
"""L1303 (Local, 2026-11-02): control for general_front.py. Do the sampled p = 32 fronts have a valid history above?
reports/inquisition-local-to-gpt-20261102.md section 2.2. Run: python3 tests/probes/general_front_upward.py

Same 3,000 roots as general_front.py with seed 3, classified by where they go (dies, rain, other phase). For each, every
upward history with half-periodic columns is explored (predecessors of (x, u) are (y, x) with y OR x = Delta u), with
cycle detection: an upward cycle would mean the front sits below a period-p/2 phase (white, rain, G8, G16).
"""
# For general fronts (u, v) at p = 32: can the half-periodic history above extend upward forever, and into which phase?
import random, sys
sys.setrecursionlimit(100000)
p = 32; h = 16; M = (1 << p) - 1; HM = (1 << h) - 1
A = sum(1 << t for t in range(1, p, 2)); AB = M ^ A
def integ(d, n):
    w, acc = 0, 0
    for t in range(n):
        if acc: w |= 1 << t
        acc ^= (d >> t) & 1
    return w
def delta(v, n):
    m = (1 << n) - 1
    return (v ^ ((v >> 1) | ((v & 1) << (n - 1)))) & m
def succ(s):
    u, v = s; d = u | v
    if bin(d).count('1') & 1: return ()
    w = integ(d, p); return ((v, w), (v, w ^ M))
# downward: which roots reach the 480-state phase
rnd = random.Random(3); roots = []
for _ in range(3000):
    vh = rnd.randrange(1 << h); v = vh | ((vh ^ HM) << h)
    uh = delta(v, p) & HM & rnd.randrange(1 << h); u = uh | (uh << h); roots.append((u, v))
seen = set(roots); st = list(roots); edges = {}
while st:
    s = st.pop(); ss = succ(s); edges[s] = ss
    for t in ss:
        if t not in seen: seen.add(t); st.append(t)
outdeg = {s: len(edges[s]) for s in edges}; pred = {}
for s, ss in edges.items():
    for t in ss: pred.setdefault(t, []).append(s)
dead = [s for s in edges if outdeg[s] == 0]; fin = set(dead)
while dead:
    t = dead.pop()
    for s in pred.get(t, ()):
        outdeg[s] -= 1
        if outdeg[s] == 0 and s not in fin: fin.add(s); dead.append(s)
rain = {(A, AB), (AB, A)}
def ends(r):
    path = {}; s = r; i = 0
    while s not in path:
        path[s] = i; i += 1; s = next(t for t in edges[s] if t not in fin)
    cyc = [x for x, j in path.items() if j >= path[s]]
    return 'rain' if set(cyc) <= rain else 'other'
cls = {r: ('dies' if r in fin else ends(r)) for r in set(roots)}
# upward on half-period rings (length 16): predecessors of (x, u) are (y, x) with y OR x = Delta u, |y OR x| even
A16 = sum(1 << t for t in range(1, h, 2)); AB16 = HM ^ A16
def preds(x, u):
    du = delta(u, h)
    if x & ~du: return []
    free = [t for t in range(h) if (x >> t) & 1 and (du >> t) & 1]
    base = du & ~x
    out = []
    for m in range(1 << len(free)):
        y = base
        for i, t in enumerate(free):
            if (m >> i) & 1: y |= 1 << t
        out.append((y, x))
    return out
def preds_from(dv, uh):
    # x with x OR uh = dv
    if uh & ~dv: return []
    free = [t for t in range(h) if (uh >> t) & 1]
    base = dv & ~uh; out = []
    for m in range(1 << len(free)):
        x = base
        for i, t in enumerate(free):
            if (m >> i) & 1: x |= 1 << t
        out.append((x, uh))
    return out
def climb(states, cap=300000):
    # states: (x, u) half-period pairs; explore upward; report whether an upward cycle exists and which phases it touches,
    # and whether the black edge's states (0,1)/(1,a) are reached
    seen = set(states); st = list(states); up = {}
    while st and len(seen) < cap:
        s = st.pop(); ps = preds(*s); up[s] = ps
        for t in ps:
            if t not in seen: seen.add(t); st.append(t)
    capped = bool(st)
    # cycle detection on the upward graph (iterative colouring)
    colour = {}; cyc_states = set()
    for s0 in up:
        if s0 in colour: continue
        stack = [(s0, iter(up.get(s0, ())))]; colour[s0] = 1; onstack = [s0]
        while stack:
            s, it = stack[-1]
            nxt = next(it, None)
            if nxt is None:
                colour[s] = 2; stack.pop(); onstack.pop(); continue
            if nxt not in up: continue
            c = colour.get(nxt)
            if c is None:
                colour[nxt] = 1; stack.append((nxt, iter(up.get(nxt, ())))); onstack.append(nxt)
            elif c == 1:
                i = onstack.index(nxt); cyc_states.update(onstack[i:])
    names = set()
    for (x, u) in cyc_states:
        if (x, u) in {(A16, AB16), (AB16, A16)}: names.add('rain')
        elif x == 0 and u == 0: names.add('white')
        else: names.add('other')
    return len(seen), capped, sorted(names)
from collections import defaultdict
agg = defaultdict(lambda: [0, 0, 0, set(), 0])     # roots, max upward states, roots with no first step, cycle names, capped
for r, c in cls.items():
    u, v = r; st0 = preds_from(delta(v, p) & HM, u & HM)
    n, capped, names = climb(st0)
    g = agg[c]; g[0] += 1; g[1] = max(g[1], n); g[2] += (len(st0) == 0); g[3].update(names); g[4] += capped
for c in ('dies', 'rain', 'other'):
    g = agg[c]
    print('%-5s roots %4d: largest upward history %d states, no first step %d, upward cycles %s, capped %d' % (c, g[0], g[1], g[2], sorted(g[3]) or 'none', g[4]))
