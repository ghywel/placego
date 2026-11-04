#!/usr/bin/env python3
"""forced_front4.py: the kit's frontBound recursion on all four strips of L1513 (A0, A1, B0, B1, read from the four-left-sides
file) at all sixteen phases through wheel 87,866; the seed's actual settling through 87,866; the local coincidence share
(CL695's form) on the longer range; and the boundary density rho(1) of CL719 on the matching range (Cloud, CL733).
Register K = 87,867 bits (prefix autonomy makes the truncation exact). Strip words: Sp v j t = bit j of rowAt v (t mod 16).
F_s(0) = 0, F_s(1) = 1, F_s(j+2) = max(F_s j, F_s (j+1)) if word_(j+1) is white, else 1 + the least u >= that max with
word_(j+1) black at phase (u - s) mod 16. The seed is on A0 at phase 0 (L1513: the orbit from 1 reaches A0 after 117,328 ticks).
tau_k = first tick with rows t, t+16 agreeing on wheels 0..k; G_k = 1 + first black of word_(k-1) at or after
max(tau_(k-2), tau_(k-1)) (that max at a white word); rho(h) = fraction of ticks with a lag-16 mismatch at wheel B(t) + h."""
import re, sys, time
import numpy as np
from collections import deque
K = 87867; P = 16; MASK = (1 << K) - 1; T_END = 118000; W0 = 8192
def step(v): return ((v << 2) ^ ((v << 1) | v)) & MASK
def lowbit(x): return (x & -x).bit_length() - 1 if x else K
t0 = time.time()
src = open('reports/wolfram-agents/submissions/four-left-sides/Rule30Submission.lean').read()
def literal(name):
    m = re.search(r'^def %s : Nat := (.*?)\n\n' % name, src, re.S | re.M); body = m.group(1)
    return [int(h, 16) for h in re.findall(r'0x[0-9a-fA-F]+', body)]
A0 = literal('A0')[0]; A1 = A0 ^ literal('A1')[0]; B0 = A0 ^ literal('B0')[0]; B1 = B0 ^ literal('B1')[0]
strips = {'A0': A0, 'A1': A1, 'B0': B0, 'B1': B1}
def words_of(v):
    rows = [v]
    for _ in range(P): rows.append(step(rows[-1]))
    assert rows[P] == v, "no 16-tick return"
    # word_j as a 16-bit int: bit r = bit j of rows[r]
    W = np.zeros(K, dtype=np.int64)
    for r in range(P):
        bits = np.frombuffer(rows[r].to_bytes((K + 7) // 8, 'little'), dtype=np.uint8)
        bits = np.unpackbits(bits, bitorder='little')[:K].astype(np.int64)
        W |= bits << r
    return W
def front(W, s, jmax):
    F = np.zeros(jmax + 1, dtype=np.int64); F[1] = 1
    for j in range(2, jmax + 1):
        m = max(F[j - 2], F[j - 1]); w = int(W[j - 1])
        if w == 0: F[j] = m; continue
        u = m
        while not (w >> ((u - s) % P)) & 1: u += 1
        F[j] = u + 1
    return F
print("rows read:", {n: v.bit_length() for n, v in strips.items()}, f"({time.time()-t0:.1f} s)")
Ws = {n: words_of(v) for n, v in strips.items()}
print("strip words built; white wheels below 87,867 per strip:", {n: [int(j) for j in np.where(W[:K] == 0)[0] if j >= 2] for n, W in Ws.items()})
U4 = 0; F_A0 = None
for n, W in Ws.items():
    Fs = [front(W, s, K - 1) for s in range(P)]
    U = np.max(np.stack(Fs), axis=0); Fmin = np.min(np.stack(Fs), axis=0)
    inc = (Fs[0][K - 1] - Fs[0][K - 1 - 30000]) / 30000
    print(f"  {n}: F_0(53207) = {Fs[0][53207]}, F_0(87866) = {Fs[0][K-1]}, U(87866) = {U[K-1]}, phase spread at 87,866 = {U[K-1] - Fmin[K-1]}, increment over the last 30,000 wheels {inc:.4f} ticks/wheel (speed {1/inc:.4f})", flush=True)
    U4 = max(U4, int(U[K - 1]))
    if n == 'A0': F_A0 = Fs[0]
print(f"uniform bound over the four strips and sixteen phases: U4(87866) = {U4}; kit-style linear bound with five white wheels below 87,866 (1 + 32 j) = {1 + 32 * (K - 1)}")
# the seed's actual settling on the truncated register, its band edge, rho(h) and the local coincidences on A0 at phase 0
V = 1; ring = deque(maxlen=P + 1); B = []; mism = {1: 0, 2: 0}; nticks = 0
for t in range(T_END + P + 1):
    ring.append(V)
    if t >= P:
        x = ring[0] ^ V; b = lowbit(x); B.append(b)
        tt = t - P
        if W0 <= tt and b < K - 2:
            nticks += 1
            for h in (1, 2): mism[h] += (x >> (b + h)) & 1
    V = step(V)
Barr = np.array(B, dtype=np.int64)
tau = np.full(K, -1, dtype=np.int64); cur = 0
for t, b in enumerate(Barr):
    while cur <= min(b - 1, K - 1): tau[cur] = t; cur += 1
    if cur > K - 1: break
assert tau[K - 1] >= 0, "seed not settled through 87,866 by T_END"
W = Ws['A0']
viol = int(np.sum(tau > F_A0))
def local_stats(lo, hi):
    co = vi = 0; sl = []
    for k in range(lo, hi + 1):
        m = max(tau[k - 2], tau[k - 1]); w = int(W[k - 1])
        if w == 0: g = m
        else:
            u = m
            while not (w >> (u % P)) & 1: u += 1
            g = u + 1
        if tau[k] < g: co += 1
        elif tau[k] > g: vi += 1
        sl.append(int(g - tau[k]))
    n = hi - lo + 1; p = co / n
    return co, vi, n, p, (p * (1 - p) / n) ** 0.5, float(np.mean(sl))
for lo, hi, label in ((2, 53207, "wheels 2..53,207"), (53208, K - 1, "wheels 53,208..87,866"), (2, K - 1, "wheels 2..87,866")):
    co, vi, n, p, se, msl = local_stats(lo, hi)
    print(f"seed on A0, local cascade lock, {label}: violations {vi}, coincidences {co}/{n} = {p:.4f} (s.e. {se:.4f}), mean slack {msl:.4f}")
print(f"seed actual: tau(53207) = {tau[53207]}, tau(87866) = {tau[K-1]}; violations of tau <= F_A0 at any wheel: {viol}; increment over wheels 57,866..87,866: {(tau[K-1]-tau[K-1-30000])/30000:.4f} ticks/wheel")
r1 = mism[1] / nticks; r2 = mism[2] / nticks
print(f"rho(1) on ticks [{W0}, tau(87864)] with the edge below 87,865: {r1:.4f} (s.e. {(r1*(1-r1)/nticks)**0.5:.4f}, {nticks} ticks); rho(2) = {r2:.4f}")
print(f"total {time.time()-t0:.1f} s")
print("FORCED_FRONT4_DONE")
