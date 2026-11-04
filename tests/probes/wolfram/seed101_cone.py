#!/usr/bin/env python3
"""seed101_cone.py [LOG2T]: is the orbit of the row 101 (cells 0 and 2) the single seed's orbit on every cell left of the seed's
right edge? (Cloud, CL721, after walk_merge.py found J(t) - 2t of mean 1.0 for 0x5.) Wall frame, bit j at tick t = cell j - t;
the seed's right-edge cell x = t is bit 2t. Reports, for t <= T: the first tick from which J(t) >= 2t holds at every later tick
(J = the lowest differing bit), the distinct values of J(t) - 2t from there with their counts, and the check that bits 0 .. 2t - 1
agree at every tick from that point."""
import sys
L2T = int(sys.argv[1]) if len(sys.argv) > 1 else 15
T = 1 << L2T; K = 2 * T + 104; MASK = (1 << K) - 1
def step(V): return ((V << 2) ^ ((V << 1) | V)) & MASK
def lowbit(x): return (x & -x).bit_length() - 1 if x else K
Vs, Vr = 1, 5; vals = {}; first_ok = None; bad_after = 0
for t in range(0, T + 1):
    J = lowbit(Vs ^ Vr); d = J - 2 * t
    if d >= 0:
        if first_ok is None: first_ok = t
        vals[d] = vals.get(d, 0) + 1
    else:
        first_ok = None; vals = {}
    if first_ok is not None and t > first_ok and ((Vs ^ Vr) & ((1 << (2 * t)) - 1)): bad_after += 1
    Vs = step(Vs); Vr = step(Vr)
print(f"T=2^{L2T}: J(t) >= 2t at every tick from t = {first_ok} on; values of J - 2t there: {sorted(vals.items())}; agreement failures on bits 0..2t-1 after that tick: {bad_after}")
print("SEED101_CONE_DONE")
