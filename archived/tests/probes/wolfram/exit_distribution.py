#!/usr/bin/env python3
"""Local, 2026-10-28 (L1066): exact distribution of the first diagonal with period > P, measured from the first
period-4 diagonal j, when the two equal alternating feeders at j have a fair phase and every new start bit is fair.
Exact path counting on the complete cap-P pair graph (integers; weight of a depth-n path is 2^-(n+1)).
Usage: exit_distribution.py P
"""
import sys
from fractions import Fraction
P = int(sys.argv[1]); M = (1 << P) - 1
def pe(g):
    y = (g << 1) & M; k = 1
    while k < P: y ^= (y << k) & M; k <<= 1
    return y
alt = int("01" * (P // 2), 2)
layer = {(alt, alt): 1, (alt ^ M, alt ^ M): 1}   # the two genuine feeder pairs at j (fair phase)
dist = {}; n = 0
while layer:
    nxt = {}
    for (a, b), w in layer.items():
        g = a | b
        if bin(g).count("1") & 1:
            dist[n] = dist.get(n, 0) + w * 2     # both start bits of the next diagonal exit: count both
            continue
        base = pe(g)
        for s in (0, M):
            v = (b, base ^ s); nxt[v] = nxt.get(v, 0) + w
    layer = nxt; n += 1
# path weight: a path that has made n bit choices after j has weight 1/(2 * 2^n); exits counted with the next bit
tot = sum(Fraction(w, 2 * 2 ** (k + 1)) for k, w in dist.items())
print(f"P={P}: total probability {tot}")
mean = sum(Fraction(w, 2 * 2 ** (k + 1)) * k for k, w in dist.items())
print("mean offset from j of the first period >", P, ":", mean, "=", float(mean))
for k in sorted(dist):
    pr = Fraction(dist[k], 2 * 2 ** (k + 1))
    if pr: print(f"  offset {k}: {pr}  ({float(pr):.3g})")
