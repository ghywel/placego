#!/usr/bin/env python3
"""rho_coincidence_error.py (Local, L1518): do CL733's standard errors hold up? CL733 closes "is the coincidence share the boundary
density?" on a difference of 0.0082 against a combined s.e. of 0.0023, using sqrt(p(1-p)/n). That formula assumes independent
samples. The record says the step process has memory (CL720: P-F2 refuted).

Prediction, before the run: batch-means standard errors exceed the binomial ones, and rho(1) drifts between windows beyond its
binomial s.e. (it was 0.458 on CL719's window and 0.462 here). Counterfactual: if batch-means errors match the binomial ones and
the difference stays above three of them at every block size, CL733's conclusion stands as stated.

The series are the ones forced_front4.py computes, for the seed on A0: per tick, a mismatch at B(t) + 1; per wheel, a local
coincidence tau_k < G_k."""
import re, sys
import numpy as np
from collections import deque
K = 87867; P = 16; MASK = (1 << K) - 1; T_END = 118000; W0 = 8192
def step(v): return ((v << 2) ^ ((v << 1) | v)) & MASK
def lowbit(x): return (x & -x).bit_length() - 1 if x else K
src = open('reports/wolfram-agents/submissions/four-left-sides/Rule30Submission.lean').read()
A0 = int(re.search(r'^def A0 : Nat := (0x[0-9a-f]+)', src, re.M).group(1), 16)
rows = [A0]
for _ in range(P): rows.append(step(rows[-1]))
assert rows[P] == A0
word = np.zeros(K, dtype=np.int64)
for r in range(P):
    bits = np.unpackbits(np.frombuffer(rows[r].to_bytes((K + 7) // 8, 'little'), dtype=np.uint8), bitorder='little')[:K]
    word |= bits.astype(np.int64) << r
V = 1; ring = deque(maxlen=P + 1); B = []; series = []
for t in range(T_END + P + 1):
    ring.append(V)
    if t >= P:
        x = ring[0] ^ V; b = lowbit(x); B.append(b)
        if W0 <= t - P and b < K - 2:
            series.append((x >> (b + 1)) & 1)
    V = step(V)
Barr = np.array(B); tau = np.full(K, -1, dtype=np.int64); cur = 0
for t, b in enumerate(Barr):
    while cur <= min(b - 1, K - 1): tau[cur] = t; cur += 1
    if cur > K - 1: break
coin = []
for k in range(2, K):
    m = int(max(tau[k - 2], tau[k - 1])); w = int(word[k - 1])
    if w == 0: g = m
    else:
        u = m
        while not (w >> (u % P)) & 1: u += 1
        g = u + 1
    coin.append(1 if tau[k] < g else 0)
rho = np.array(series, dtype=float); co = np.array(coin, dtype=float)
def batch(x, b):
    n = len(x) // b
    m = x[:n * b].reshape(n, b).mean(axis=1)
    return m.std(ddof=1) / n ** 0.5, n
def acf(x, l):
    y = x - x.mean()
    return float((y[:-l] * y[l:]).mean() / y.var())
print(f'rho(1): mean {rho.mean():.4f}, n {len(rho)}, binomial s.e. {(rho.mean() * (1 - rho.mean()) / len(rho)) ** 0.5:.5f}')
print('  autocorrelation lags 1, 2, 3, 4, 8, 16, 32:', [round(acf(rho, l), 4) for l in (1, 2, 3, 4, 8, 16, 32)])
print(f'coincidence: mean {co.mean():.4f}, n {len(co)}, binomial s.e. {(co.mean() * (1 - co.mean()) / len(co)) ** 0.5:.5f}')
print('  autocorrelation lags 1, 2, 3, 4, 8, 16, 32:', [round(acf(co, l), 4) for l in (1, 2, 3, 4, 8, 16, 32)])
d = rho.mean() - co.mean()
print(f'difference {d:.4f}')
for b in (16, 64, 256, 1024, 4096, 8192):
    a, na = batch(rho, b); c, nc = batch(co, b)
    comb = (a * a + c * c) ** 0.5
    print(f'  block {b:5d}: rho s.e. {a:.5f} ({na} blocks), coincidence s.e. {c:.5f} ({nc} blocks), difference / combined s.e. {d / comb:.2f}')
print('rho(1) by quarter of its window:', [round(float(q.mean()), 4) for q in np.array_split(rho, 4)])
print('coincidence by quarter of its wheels:', [round(float(q.mean()), 4) for q in np.array_split(co, 4)])
