#!/usr/bin/env python3
"""S-01's worked example, as a plain replay. Implements the kit's scan, Z and run on lists of bit pairs, builds the chart, and
checks every available chart cell against Rule 30 with a white wall, then compares the row at time two with a zero-boundary
evolution. Prediction, written before the run: 0 mismatches at every frontier, interior from time 0, wall from time 1;
column -1 of the row at time two is black at every even tick while frontiers last. Counterfactual: any mismatch means the
Lean statement and this replay read the definitions differently, and the essay's example must not be built on it.
Usage: frontier_replay.py MAXLEN
"""
import itertools, sys
def scan(w):
    u = v = al = 0; out = []
    for a, b in w:
        v = v ^ (al | b); u = u ^ (v | a); al = a
        out.append((u, v))
    return out, u, v
def Z(w):
    out, u, v = scan(w)
    if u != v: return None
    return out + [(1, 1 - v)], v
def run(w, cap):
    fr = [w]; s = []
    while len(s) < cap:
        z = Z(fr[-1])
        if z is None: break
        fr.append(z[0]); s.append(z[1])
    return fr, s
def at(fr, n, e):
    w = fr[n]
    return w[len(w) - 1 - e] if e < len(w) else (0, 0)
def chart(fr, tau, e):
    if (tau + e) % 2 == 0: return at(fr, (tau + e) // 2, e)[0]
    return at(fr, (tau + e + 1) // 2, e)[1]
def check(fr):
    """cells with every needed frontier available"""
    N = len(fr) - 1
    bad = 0; cells = 0
    for tau in range(0, 2 * N):
        for e in range(0, 2 * N + 2):
            need = (tau + 1 + e + 1 + 1) // 2 + 1
            if need > N: continue
            cells += 1
            if chart(fr, tau + 1, e + 1) != chart(fr, tau, e + 2) ^ (chart(fr, tau, e + 1) | chart(fr, tau, e)): bad += 1
    wall = wbad = 0
    for tau in range(1, 2 * N - 3):
        wall += 1
        if chart(fr, tau + 1, 0) != chart(fr, tau, 1) ^ chart(fr, tau, 0): wbad += 1
    return cells, bad, wall, wbad
def zero_row(fr):
    """the row at time two, as a natural: bit e is depth e + 1"""
    y = 0
    for e in range(0, 2 * len(fr[0]) + 2):
        if chart(fr, 2, e): y |= 1 << e
    return y
def F(y): return (y >> 1) ^ (y | (y << 1))
best = []
nfr = 0
for r in range(1, int(sys.argv[1]) + 1):
    nfr += 2 * 4 ** (r - 1)
    top = (0, None)
    tot = [0, 0, 0, 0]
    for tail in itertools.product(((0, 0), (0, 1), (1, 0), (1, 1)), repeat=r - 1):
        for b0 in (0, 1):
            w = [(1, b0)] + list(tail)
            fr, s = run(w, 400)
            N = len(s)
            if N >= 3:
                c = check(fr)
                for i in range(4): tot[i] += c[i]
            if N > top[0]: top = (N, w)
    print('r', r, 'longest run', top[0], 'cells', tot[0], 'bad', tot[1], 'wall', tot[2], 'bad', tot[3], flush=True)
    best.append((top[0], r, top[1]))
N, r, w = max(best, key=lambda x: (x[0], -x[1]))
print('frontiers', nfr, 'best', N, r, w)
fr, s = run(w, 400)
y = zero_row(fr)
print('tape', ''.join(map(str, s)))
print('row at time 2', y, 'width', y.bit_length())
t = 0; z = y; ev = []
while t <= 2 * N + 20:
    if t % 2 == 0: ev.append(z & 1)
    z = F(z); t += 1
print('column -1 at even ticks', ''.join(map(str, ev)))
print('first white even tick from time two', 2 * ev.index(0) if 0 in ev else None, 'updates', N)
