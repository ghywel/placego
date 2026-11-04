#!/usr/bin/env python3
"""settling_bounds.py [NROWS=5]: the kit's frontBound recursion (Rule30FrontLaw) evaluated on the universal strip at every
phase, against the actual settling of the seed and of random left-finite rows (Cloud, CL730).
Strip: the words C_j (j <= 53,207) generated as in universal_table.py (phase anchored so that C_j(t) is the seed's wheel j at
tick t once settled). frontBound at phase s: F_s(0) = 0, F_s(1) = 1, F_s(j+2) = 1 + the least u >= max(F_s j, F_s (j+1)) with
C_(j+1)(u - s) black, or that max if the word is white. U(j) = max_s F_s(j), the phase-free bound. Actual settling of a row:
tau_k = the first tick t with rows t and t + 16 agreeing on wheels 0 .. k (from the lag-16 band edge), in the row's own clock;
the row's phase s is read off its settled wheels. Reported: F_0 and U at 53,207 and their increments (ticks per wheel) over
the last 40,000 wheels; the kit-style bound 1 + 16 j; the seed's tau at 53,207 and increment; the share of wheels where the
seed settles strictly before F_0 (coincidences); the maximum of F_0(k) - tau_k; for each random row, its phase, violations of
tau_k <= F_s(k) (must be 0), its increment and coincidence share."""
import sys, time
import numpy as np
from collections import deque
from math import gcd
NROWS = int(sys.argv[1]) if len(sys.argv) > 1 else 5
J = 53208; P = 16; T0 = 4096; TMAX = 76000; K = 2 * TMAX + 104; MASK = (1 << K) - 1
def step(V): return ((V << 2) ^ ((V << 1) | V)) & MASK
def lowbit(x): return (x & -x).bit_length() - 1 if x else K
t0 = time.time()
# --- the strip (as universal_table.py) and the seed's band edge in one evolution
V = 1; rowsT0 = []; B = []; ring = deque(maxlen=P + 1)
for t in range(TMAX + P + 1):
    ring.append(V)
    if T0 <= t < T0 + P: rowsT0.append(V)
    if t >= P: B.append(lowbit(ring[0] ^ V))     # B[t-16] = band edge at tick t-16
    V = step(V)
def seed_word(j): return sum(((rowsT0[i] >> j) & 1) << i for i in range(P))
def bit(w, i): return (w >> (i % P)) & 1
C = [0xFFFF, 0xFFFF]
for j in range(2, J):
    a, b = C[j - 2], C[j - 1]
    if b:
        tb = next(i for i in range(P) if bit(b, i)); x = [0] * P; x[(tb + 1) % P] = bit(a, tb) ^ 1
        for k in range(1, P):
            i = (tb + k) % P; x[(i + 1) % P] = bit(a, i) ^ (bit(b, i) | x[i])
    else:
        x = [0] * P; x[0] = bit(seed_word(j), 0)
        for i in range(P - 1): x[i + 1] = bit(a, i) ^ x[i]
    C.append(sum(x[i] << i for i in range(P)))
# phase convention: bit i of C_j is the value at tick T0 + i, so C_j(t) = bit (t - T0) mod 16
def Cval(j, t): return bit(C[j], (t - T0) % P)
def frontBound(s):
    F = [0, 1]
    for j in range(2, J):
        m = max(F[j - 2], F[j - 1]); w = C[j - 1]
        if w == 0: F.append(m); continue
        u = m
        while not Cval(j - 1, u - s): u += 1
        F.append(u + 1)
    return np.array(F, dtype=np.int64)
F0 = frontBound(0)
U = F0.copy()
for s in range(1, P): U = np.maximum(U, frontBound(s))
Barr = np.array(B, dtype=np.int64)
def tau_from_B(Barr, kmax):
    tau = np.full(kmax + 1, -1, dtype=np.int64); cur = 0
    for t, b in enumerate(Barr):
        while cur <= min(b - 1, kmax): tau[cur] = t; cur += 1
        if cur > kmax: break
    return tau
tau_seed = tau_from_B(Barr, J - 1)
assert tau_seed[J - 1] >= 0, "seed not settled through 53,207 within TMAX"
def incr(x, lo, hi): return (x[hi] - x[lo]) / (hi - lo)
lo, hi = J - 1 - 40000, J - 1
print(f"strip to wheel {J-1}; seed evolved to {TMAX} ({time.time()-t0:.1f} s)")
print(f"frontBound on the strip, seed phase: F_0(53207) = {F0[J-1]}; increment over the last 40,000 wheels {incr(F0, lo, hi):.4f} ticks/wheel (front speed {1/incr(F0, lo, hi):.4f})")
print(f"phase-free bound U(53207) = max over 16 phases = {U[J-1]}; max over wheels of U - F_0 = {int((U - F0).max())}; kit-style bound 1 + 16 j = {1 + 16 * (J - 1)}")
print(f"seed actual: tau(53207) = {tau_seed[J-1]}; increment over the last 40,000 wheels {incr(tau_seed, lo, hi):.4f} ticks/wheel (front speed {1/incr(tau_seed, lo, hi):.4f})")
viol = int(np.sum(tau_seed > F0)); early = int(np.sum(tau_seed[2:] < F0[2:])); eq = int(np.sum(tau_seed[2:] == F0[2:]))
print(f"seed: wheels with tau > F_0 (violations of the bound): {viol}; wheels settling strictly before F_0 (coincidences): {early} of {J-2} ({early/(J-2):.4f}); equal: {eq}; max F_0 - tau = {int((F0 - tau_seed).max())} at wheel {int(np.argmax(F0 - tau_seed))}")
# random rows (CL696's construction): their own band edge, phase and tau
rng = np.random.default_rng(606)
print("random rows: width, phase s, violations of tau_k <= F_s(k), tau(53207), increment, coincidence share, max F_s - tau")
for r in range(NROWS):
    wb = int(rng.integers(1, 65)); seed = ((int(rng.integers(0, 1 << 32)) << 32) | int(rng.integers(0, 1 << 32))) & ((1 << wb) - 1) | 1
    V = seed; ring = deque(maxlen=P + 1); Br = []; late = None
    for t in range(TMAX + P + 1):
        ring.append(V)
        if t >= P: Br.append(lowbit(ring[0] ^ V))
        if t == 70000: late = V
        V = step(V)
    tau_r = tau_from_B(np.array(Br, dtype=np.int64), J - 1)
    if tau_r[J - 1] < 0: print(f"  width {wb}: not settled through 53,207 by {TMAX}"); continue
    # phase: the s with late row's settled wheels 1000..40000 equal to C_j(70000 - s)... row time u = t + s <-> strip time t: a_j(u) = C_j(u - s)
    best = None
    for s in range(P):
        agree = sum(((late >> j) & 1) == Cval(j, 70000 - s) for j in range(1000, 40000, 97))
        if best is None or agree > best[0]: best = (agree, s)
    s = best[1]; Fs = frontBound(s) if s else F0
    v = int(np.sum(tau_r > Fs)); e = int(np.sum(tau_r[2:] < Fs[2:]))
    print(f"  width {wb:2d}: s = {s:2d} (agreement {best[0]}/{len(range(1000,40000,97))}), violations {v}, tau(53207) = {tau_r[J-1]}, increment {incr(tau_r, lo, hi):.4f}, coincidences {e/(J-2):.4f}, max F_s - tau = {int((Fs - tau_r).max())}")
print(f"total {time.time()-t0:.1f} s")
print("SETTLING_BOUNDS_DONE")
