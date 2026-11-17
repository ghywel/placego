#!/usr/bin/env python3
"""Local, 2026-10-28 (L1072): brute-force checks of each lemma in the hand proof of the degree law
(reports/rule30-degree-law.md). Rule 30: new(i) = x(i-1) XOR (x(i) OR x(i+1)); y_j = initial cell j.

  L1  d c(t)/d y_t = product over k=0..t-1 of NOT x_k(t-1-k)   (all initial rows on [-t, t], t <= 7)
  L2  #words on [-t+1, t-2] keeping the anti-diagonal x_k(t-1-k) white for k = 1..t-1 equals 2^(t-1)   (t <= 10)
  L3  z-frame: Delta_{z0(2m-1)} Phi_m = m + (m-1) P + sum_{i=1}^{m-2} W_i^(m-1)  as functions   (m <= 7)
  L4  z-frame: Delta_{z0(2m-1)} W_k^(m) = k + k P + sum_{i=1}^{k-1} W_i^(m-1)  as functions        (m <= 7)
  L5  tau(Phi_m) = tau(W_k^(m)) = 1                                                                (m <= 8)
Every check is an exact identity over all inputs; any mismatch prints FAIL and exits 1.
"""
import itertools, sys
import numpy as np
ok = True
def report(name, good):
    global ok; ok &= good; print(f"{name}: {'pass' if good else 'FAIL'}")
# L1
good = True
for t in range(1, 8):
    n = 2 * t + 1; N = 1 << n; idx = np.arange(N, dtype=np.uint32)
    cells = {j: ((idx >> (j + t)) & 1).astype(np.uint8) for j in range(-t, t + 1)}
    hist = [cells]; cur = cells
    for k in range(t):
        cur = {j: cur[j - 1] ^ (cur[j] | cur[j + 1]) for j in range(-t + k + 1, t - k)}
        hist.append(cur)
    c = hist[t][0]
    flipped = idx ^ np.uint32(1 << (2 * t))                     # flip y_t
    deriv = c ^ c[flipped]
    prod = np.ones(N, np.uint8)
    for k in range(t): prod &= 1 - hist[k][t - 1 - k]
    good &= bool(np.array_equal(deriv, prod))
report("L1 anti-diagonal product formula, t<=7", good)
# L2
good = True
for t in range(2, 11):
    a, b = -t + 1, t - 2; L = b - a + 1; N = 1 << L; idx = np.arange(N, dtype=np.uint32)
    row = {x: (((idx >> (x - a)) & 1).astype(np.uint8) if a <= x <= b else np.zeros(N, np.uint8)) for x in range(a - t - 2, t + 3)}
    white = np.ones(N, bool); cur = row
    for k in range(1, t):
        cur = {x: cur[x - 1] ^ (cur[x] | cur[x + 1]) for x in range(min(cur) + 1, max(cur))}
        white &= cur[t - 1 - k] == 0
    good &= int(white.sum()) == 2 ** (t - 1)
report("L2 triangular count 2^(t-1), t<=10", good)
# z-frame systems
def evolve(z, steps):
    hist = [z]
    for _ in range(steps):
        z = [0] + [z[j + 2] ^ (z[j + 1] | z[j]) for j in range(1, len(z) - 2)] + [0, 0]
        hist.append(z)
    return hist
def system(m, frees, J):
    z = [0] * J
    for i, v in enumerate(frees): z[2 * i + 1] = v
    for k in range(m - 1):
        for v in (0, 1):
            z[2 * k + 2] = v
            h = evolve(z, k)
            if h[k][1] == h[k][2]: break
        else: raise SystemExit("pivot unsolvable")
    return z, evolve(z, m)
good3 = good4 = True
for m in range(2, 8):
    J = 4 * m + 6
    for frees in itertools.product((0, 1), repeat=m - 1):
        z0, h0 = system(m, frees + (0,), J); z1, h1 = system(m, frees + (1,), J)
        _, hs = system(m - 1, frees, J)                           # S_(m-1), same free cells
        P = z0[2 * m - 2]
        Wsmall = lambda i: hs[i][2 * (m - 1) - 2 * i]
        dphi = (h0[m - 1][1] ^ h0[m - 1][2]) ^ (h1[m - 1][1] ^ h1[m - 1][2])
        rhs = (m + (m - 1) * P + sum(Wsmall(i) for i in range(1, m - 1))) & 1
        good3 &= dphi == rhs
        for k in range(1, m):
            dW = h0[k][2 * m - 2 * k] ^ h1[k][2 * m - 2 * k]
            rhs = (k + k * P + sum(Wsmall(i) for i in range(1, k))) & 1
            good4 &= dW == rhs
report("L3 Phi recursion identity, m<=7", good3); report("L4 W recursion identity, m<=7", good4)
good = True
for m in range(1, 9):
    J = 4 * m + 6; tp = 0; tw = [0] * m
    for frees in itertools.product((0, 1), repeat=m):
        _, h = system(m, frees, J); tp ^= h[m - 1][1] ^ h[m - 1][2]
        for k in range(1, m): tw[k] ^= h[k][2 * m - 2 * k]
    good &= tp == 1 and all(tw[k] == 1 for k in range(1, m))
report("L5 tau(Phi_m)=tau(W_k)=1, m<=8", good)
print("ALL LEMMAS PASS" if ok else "FAILURE"); sys.exit(0 if ok else 1)
