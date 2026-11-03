#!/usr/bin/env python3
"""band_edge_coin.py LOG2T LOG2P: the band edge as a damage front between the pattern and its own P-shifted copy (inquisition round
14, H1; Cloud, CL692). On the left-frame system (bit k of the big integer V = left wheel k): B(t) = lowest wheel where rows[t] and
rows[t+P] differ. Checks (predictions in the tracker, round 14): H1a the mask law B(t+1) = B(t) iff D_(B(t)-1)(t) = 0, exactly;
H1b the decider W(t) = D_(B(t)-1)(t) is a function of (B(t)-1, t mod 16); H1c generic tells on W against a biased iid control;
H1d heal sizes against the pattern at the edge. Output: band_edge_coin.out."""
import sys, numpy as np, collections
L2T, L2P = int(sys.argv[1]), int(sys.argv[2]); T = 1 << L2T; P = 1 << L2P; K = T + P + 8; MASK = (1 << K) - 1
def stp(V): return ((V << 2) ^ ((V << 1) | V)) & MASK
rows = []; V = 1
for t in range(T + 2 * P + 300): rows.append(V); V = stp(V)
B = np.zeros(T + 2, dtype=np.int64)
for t in range(T + 2):
    x = rows[t] ^ rows[t + P]; B[t] = (x & -x).bit_length() - 1 if x else K
bit = lambda t, k: (rows[int(t)] >> int(k)) & 1 if int(k) >= 0 else 0
# H1a: the mask law
viol = 0
for t in range(T + 1):
    stay = (B[t + 1] == B[t]); dec = bit(t, B[t] - 1)
    if stay != (dec == 0): viol += 1
print(f"H1a mask law B(t+1)=B(t) iff D_(B-1)(t)=0 over t<= {T}: violations {viol}")
# H1b (redesigned after a vacuous first form: the edge visits each wheel about once, so (B-1, t mod 16) keys never repeat and a
# function test cannot fail): the decider is the crystal table iff the decider wheel is already periodic with period dividing 16 at
# the time it decides: D_(B(t)-1)(t) == D_(B(t)-1)(t - 16 m) for m = 1..4
for per in (16, 32, 64, 128):
    ok = 0; nn = 0
    for t in range(T // 4, T + 1):
        k = int(B[t]) - 1; w = bit(t, k); nn += 1
        if all(bit(t - per * m, k) == w for m in range(1, 5)): ok += 1
    print(f"H1b decider wheel periodic with period | {per} at decision time, t in [T/4, T]: {ok} of {nn} agree with t-{per}m (m=1..4)")
# where the band edge sits relative to the settled zone: the wheel's own least period at time t from its last 2048 values
import math
agree = {16: 0, 32: 0, 64: 0}; nn = 0
for t in range(T // 2, T + 1, 7):
    k = int(B[t]) - 1; nn += 1
    for per in agree:
        if all(bit(t - j, k) == bit(t - j - per, k) for j in range(0, 256)): agree[per] += 1
print(f"H1b' over the 256 ticks before decision, wheel B-1 is periodic with period dividing 16/32/64 in {agree[16]}/{agree[32]}/{agree[64]} of {nn} sampled times")
# H1b'' (forward): the band edge is non-decreasing, so every wheel below B(t) is 1024-periodic from time t on. The least period of
# the decider wheel from its decision time: smallest per | 1024 with D_(B-1)(t + j) == D_(B-1)(t + j + per) for all j < 256
import collections as _c
least = _c.Counter(); nn = 0; before = _c.Counter()
for t in range(T // 2, T + 1, 5):
    k = int(B[t]) - 1; nn += 1; found = None
    for per in (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024):
        if all(bit(t + j, k) == bit(t + j + per, k) for j in range(0, 256)): found = per; break
    least[found] += 1
    # and was it already periodic with that period over the 64 ticks before t?
    if found is not None and all(bit(t - j, k) == bit(t - j + found, k) for j in range(1, 65)): before[found] += 1
print(f"H1b'' least forward period of the decider wheel from its decision time ({nn} sampled times): " + ", ".join(f"{k}: {v}" for k, v in sorted(least.items(), key=lambda kv: (kv[0] is None, kv[0] or 0))))
print(f"      of those, already periodic with that period over the 64 ticks before the decision: " + ", ".join(f"{k}: {v}" for k, v in sorted(before.items())))
# H1c: generic tells on W(t) and on a biased iid control
Wseq = np.array([bit(t, B[t] - 1) for t in range(T // 4, T + 1)], dtype=np.uint8)
rng = np.random.default_rng(5); ctrl = (rng.random(len(Wseq)) < Wseq.mean()).astype(np.uint8)
# the right control: the fair-row front's own decider sequence (the cell ahead, black = heal), same length
def fair_decider(n, seed=4):
    r2 = np.random.default_rng(seed); Tf = n + n // 4 + 10; WL = 2*Tf + 100; WR = Tf + 60
    a = r2.integers(0, 2, WL + WR).astype(np.uint8); b = a.copy(); b[WL] ^= 1; out = []
    def stepf(r):
        q = np.zeros_like(r); q[1:-1] = r[:-2] ^ (r[1:-1] | r[2:]); return q
    for t in range(Tf):
        d = np.flatnonzero(a ^ b); x = int(d.min())
        if t >= Tf - n: out.append(int(a[x-1]))
        a, b = stepf(a), stepf(b)
    return np.array(out, dtype=np.uint8)
fair = fair_decider(len(Wseq))
def block_entropy_deficit(c, nmax=10):
    res = []
    for m in range(1, nmax + 1):
        words = np.lib.stride_tricks.sliding_window_view(c, m); keys = words @ (1 << np.arange(m)[::-1])
        cnt = np.bincount(keys, minlength=2**m).astype(float); p = cnt[cnt > 0] / cnt.sum()
        H = -(p * np.log2(p)).sum(); res.append(int(round(1000 * (m - H))))
    return res
def berlekamp_massey(bits):
    s = [int(b) for b in bits]; nn = len(s); C = [1] + [0]*nn; Bp = [1] + [0]*nn; L = 0; m = -1
    for i in range(nn):
        d = s[i]
        for j in range(1, L + 1): d ^= C[j] & s[i - j]
        if d:
            Tc = C[:]
            for j in range(0, nn - i + m + 1):
                if Bp[j]: C[j + i - m] ^= 1
            if L <= i // 2: L = i + 1 - L; m = i; Bp = Tc
    return L
def kernel_distinct(c, depth=6, length=64):
    q = 1 << depth; return len({tuple(c[r:r + q*length:q][:length]) for r in range(q)})
def max_autocorr(c, Kl=64):
    x = c.astype(float) - c.mean(); v = np.mean(x*x); return max(abs(np.mean(x[:-k] * x[k:]) / v) for k in range(1, Kl + 1))
for name, c in (("band-edge decider W(t)", Wseq), ("fair-row front decider", fair), ("biased iid control", ctrl)):
    print(f"H1c {name:20s} density={c.mean():.4f} deficit={block_entropy_deficit(c)} LC2048={berlekamp_massey(c[:2048])} kernel={kernel_distinct(c)} autocorr={max_autocorr(c):.4f}")
# H1d: heal sizes against the shift-difference pattern at the edge: (a[B], a[B+1], b[B], b[B+1]) with a = rows[t+P], b = rows[t]
pat = collections.defaultdict(list)
for t in range(T // 4, T + 1):
    if bit(t, B[t] - 1) == 1:
        a0, a1 = bit(t + P, B[t]), bit(t + P, B[t] + 1); b0, b1 = bit(t, B[t]), bit(t, B[t] + 1)
        pat[f"{a0}{a1}{b0}{b1}"].append(int(B[t + 1] - B[t]))
print("H1d heal size by the pattern (a[B],a[B+1],b[B],b[B+1]) at the edge (a = row t+P, b = row t): mean, n, distinct sizes")
for k in sorted(pat): v = np.array(pat[k]); print(f"   {k}: mean {v.mean():.3f} n={len(v)} sizes {sorted(set(v.tolist()))[:6]}")
print("BAND_EDGE_COIN_DONE")
