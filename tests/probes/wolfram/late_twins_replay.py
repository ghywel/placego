#!/usr/bin/env python3
"""late_twins_replay.py (Local, Block 7, S-02): the plain-Python replay of the essay's worked-numbers cell.
Prints the list the notebook's first Output cell must equal: the two stage maxima, then for each sample row y at t = 46
whether the band of iter F 45 y is on C20 and whether a twin of iter F 44 y exists with equal width and the same bit 0."""
def R(u): return (u >> 2) ^ ((u >> 1) | u)
def F(y): return (y >> 1) ^ (y | (y << 1))
C13 = {6411, 6428, 7117, 7129}; C20 = {820683, 822904, 911005, 912610}
def entry(v, C):
    t = 0
    while v not in C: v = R(v); t += 1
    return t
stage13 = max(entry(u, C13) for u in range(4096, 8192))
stage20 = max(entry(c * 128 + b, C20) for c in C13 for b in range(128))
def pre(z, b):
    # the preimage of z under F with bit 0 equal to b, if finite: Y_(i+1) = z_i xor (Y_i or Y_(i-1))
    y = [b]
    for i in range(z.bit_length() + 3):
        y.append(((z >> i) & 1) ^ (y[-1] | (y[-2] if len(y) >= 2 else 0)))
    return sum(v << i for i, v in enumerate(y)) if y[-1] == 0 and y[-2] == 0 else None
def nest(f, y, n):
    for _ in range(n): y = f(y)
    return y
def twins(x):
    out = []
    for b1 in (0, 1):
        x1 = pre(F(F(x)), b1)
        if x1 is None: continue
        x0 = pre(x1, x & 1)
        if x0 is not None and x0 != x: out.append(x0)
    return out
rows = []
for y in (1, 3, 5, 7, 331, 1493, 11083):
    x = nest(F, y, 44); x45 = F(x)
    band = (x45 >> (x45.bit_length() - 20)) in C20
    tw = twins(x)
    rows.append([band, len(tw) >= 1 and all(w.bit_length() == x.bit_length() and (w & 1) == (x & 1) and F(F(w)) == F(F(x)) for w in tw)])
print([stage13, stage20, rows])
