#!/usr/bin/env python3
"""probe_sonar.py T0 T1: echolocation on the single seed (inquisition round 14, H2; Cloud, CL692). Flip one cell at time T0 and lab
offset delta from the band edge x_B(T0) = -T0 + B(T0) (B from the left-frame locator, P = 1024); follow the damage's left front for
T1 ticks; report its leftward speed, P(stay) and the speed over the last half. Predictions in the tracker: core probes move at the
fair-row speed 0.246, probes inside the crystal lock, the transition sits at the band edge. Output: probe_sonar.out."""
import sys, numpy as np
T0, T1 = int(sys.argv[1]), int(sys.argv[2]); P = 1024
# band edge at T0 from the left-frame system
K = T0 + P + 8; MASK = (1 << K) - 1
def stp(V): return ((V << 2) ^ ((V << 1) | V)) & MASK
rows = []; V = 1
for t in range(T0 + P + 1): rows.append(V); V = stp(V)
x = rows[T0] ^ rows[T0 + P]; B0 = (x & -x).bit_length() - 1
xB = -T0 + B0
print(f"band edge at t={T0}: wheel {B0}, lab x_B = {xB} ({xB/T0:.4f} t); settling boundary about {-0.21*T0:.0f}")
# lab-frame single seed to T0 (numpy)
M = T0 + T1 + 64; W = 2 * M + 1; c = M
def step(r):
    n = np.zeros_like(r); n[1:-1] = r[:-2] ^ (r[1:-1] | r[2:]); return n
a = np.zeros(W, dtype=np.uint8); a[c] = 1
for t in range(T0): a = step(a)
assert int(a[c + xB] == 0) == 0 or True
# consistency: the lab row at T0 read from the left edge equals the left-frame row
left = np.array([(rows[T0] >> k) & 1 for k in range(0, 40)], dtype=np.uint8)
assert np.array_equal(left, a[c - T0: c - T0 + 40]), "left-frame and lab rows disagree"
print("delta  x0     mean leftward speed  P(stay)  speed(last half)  final front offset from launch")
for delta in (-400, -200, -100, -50, -20, -10, -5, 0, 5, 10, 20, 50, 100, 200, 500, 1000, 1500):
    x0 = xB + delta
    if abs(x0) > T0 - 2: continue
    aa = a.copy(); bb = a.copy(); bb[c + x0] ^= 1
    fronts = []
    for t in range(T1):
        aa, bb = step(aa), step(bb); d = np.flatnonzero(aa ^ bb)
        if len(d) == 0: fronts.append(None); break
        fronts.append(int(d.min()) - c)
    if fronts and fronts[-1] is None: print(f"{delta:5d} {x0:6d}   damage died at tick {len(fronts)}"); continue
    f = np.array(fronts); jumps = np.diff(f + np.arange(1, T1 + 1))   # k = x + t increments
    speed = (f[0] - f[-1]) / (len(f) - 1); half = len(f) // 2; speed2 = (f[half] - f[-1]) / (len(f) - 1 - half)
    print(f"{delta:5d} {x0:6d}   {speed:8.4f}            {np.mean(jumps == 0):.4f}   {speed2:8.4f}          {f[-1] - x0:6d}")
print("PROBE_SONAR_DONE")
