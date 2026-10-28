#!/usr/bin/env python3
"""Local, 2026-10-28 (L1066): Rule 30 ring orbits whose moving-frame period is a power of two, and whether their
diagonal pair states can be reached from a black right edge.

On a ring of size m, Phi(x)[i] = x[i] XOR (x[i+1] OR x[i+2]) is Rule 30 seen from a frame moving right one cell per
step (GC808). Every Phi-periodic configuration whose period divides P gives right diagonals D_d(t) = Phi^t(x)[-d]
(indices mod m) of period dividing P, so its pair states (D_(d-1), D_d) form a cycle of the cap-P pair graph IF
they are reachable from the edge state (0, 1). Lists, for m <= MMAX, every Phi-periodic configuration with period a
power of two <= P (up to rotation), and tests each one's pair states against the complete cap-P graph built by
pair_graph_bits.py's construction. Usage: ring_power2_orbits.py MMAX P
"""
import sys, collections
MMAX, P = int(sys.argv[1]), int(sys.argv[2]); MP = (1 << P) - 1
def prefix_excl(g):
    y = (g << 1) & MP; k = 1
    while k < P: y ^= (y << k) & MP; k <<= 1
    return y
reach = {(0, MP)}; q = collections.deque(reach)
while q:
    a, b = q.popleft(); g = a | b
    if bin(g).count("1") & 1: continue
    base = prefix_excl(g)
    for s in (0, MP):
        v = (b, base ^ s)
        if v not in reach: reach.add(v); q.append(v)
print(f"cap-{P} graph: {len(reach)} reachable pair states")
for m in range(1, MMAX + 1):
    full = (1 << m) - 1
    def phi(x):  # bit i = x[i] XOR (x[i+1] OR x[i+2]), cyclic
        r1 = ((x >> 1) | (x << (m - 1))) & full; r2 = ((x >> 2) | (x << (m - 2))) & full if m >= 2 else x
        if m == 1: r1 = r2 = x
        return x ^ (r1 | r2)
    seen = set(); found = []
    for x0 in range(1 << m):
        if x0 in seen: continue
        # walk to find whether x0 is periodic with period a power of two <= P
        y = x0; per = None
        for t in range(1, P + 1):
            y = phi(y)
            if y == x0: per = t; break
        if per is None or per & (per - 1): continue
        orb = [x0]; y = x0
        for t in range(per - 1): y = phi(y); orb.append(y)
        rots = set()
        for z in orb:
            for r in range(m): rots.add(((z >> r) | (z << (m - r))) & full)
        seen |= rots
        # diagonals D_d(t) = Phi^t(x0)[-d mod m], packed over P ticks
        traj = [x0]; y = x0
        for t in range(P - 1): y = phi(y); traj.append(y)
        diag = lambda d: sum(((traj[t] >> ((-d) % m)) & 1) << t for t in range(P))
        pairs = [(diag(d - 1), diag(d)) for d in range(1, m + 1)]
        inreach = any(p in reach for p in pairs)
        found.append((per, format(x0, f"0{m}b")[::-1], inreach))
    if found:
        print(f"m={m}: " + "; ".join(f"x={x} period {p}{' REACHABLE' if r else ''}" for p, x, r in found))
