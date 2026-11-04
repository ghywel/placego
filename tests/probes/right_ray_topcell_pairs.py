#!/usr/bin/env python3
"""right_ray_topcell_pairs.py (Local, L1518): which odd low states does the top-cell movie alone fail to separate?
U(t) = bit d - 1 of phi^t(v), over the full register period 2^(d - 1). COMPUTED; no all-depth statement is claimed."""
def phi(x): return x ^ ((2 * x) | (4 * x))
for d in range(3, 14):
    M = (1 << d) - 1
    top = {}; full = {}
    for v in range(1, 1 << d, 2):
        x = v; w = []; f = []
        for t in range(1 << (d - 1)):
            u = (x >> (d - 1)) & 1
            w.append(u); f.append((u, u | ((x >> (d - 2)) & 1)))
            x = phi(x) & M
        top.setdefault(tuple(w), []).append(v); full.setdefault(tuple(f), []).append(v)
    pairs = [[format(v, '0%db' % d) for v in g] for g in top.values() if len(g) > 1]
    print('d', d, 'states', 1 << (d - 1), 'top-cell collisions', pairs, 'full collisions', sum(len(g) > 1 for g in full.values()))
