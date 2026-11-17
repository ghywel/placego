#!/usr/bin/env python3
"""fake_coin_tells.py N: a tell library for apparent fair coins (inquisition round 14, Q2; Cloud, CL691). Controls: an iid coin,
Thue-Morse, Rudin-Shapiro, a 31-bit LFSR (x^31 + x^3 + 1). The W-family: the centre column of a Rule 30 row with iid fair cells on
[-W, W] and white outside (W = 0 is the single seed), N steps. Tells: block-entropy deficit n - H_n in millibits for n = 1..10;
linear complexity of the first 2048 bits (Berlekamp-Massey); distinct 2-kernel sequences at depth 6 (64 of 64 terms); max |autocorr|
over lags 1..64; max density deviation over t mod 8. Predictions in the tracker (round 14): controls caught by their named tells;
the W-family passes all at the iid level. Output: fake_coin_tells.out."""
import sys, numpy as np, collections
N = int(sys.argv[1]) if len(sys.argv) > 1 else 8192
rng = np.random.default_rng(2026)
def rule30_centre(W, N):
    L = N + W + 4; row = np.zeros(2*L + 1, dtype=np.uint8); c = L
    if W == 0: row[c] = 1
    else: row[c-W:c+W+1] = rng.integers(0, 2, 2*W+1)
    out = np.empty(N, dtype=np.uint8)
    for t in range(N):
        out[t] = row[c]; n = np.zeros_like(row); n[1:-1] = row[:-2] ^ (row[1:-1] | row[2:]); row = n
    return out
def thue_morse(N): return np.array([bin(t).count('1') & 1 for t in range(N)], dtype=np.uint8)
def rudin_shapiro(N): return np.array([bin(t & (t >> 1)).count('1') & 1 for t in range(N)], dtype=np.uint8)
def lfsr(N):
    s = 0x6D3A9F17 & ((1 << 31) - 1) or 1; out = np.empty(N, dtype=np.uint8)
    for i in range(N):
        out[i] = s & 1; fb = ((s >> 0) ^ (s >> 3)) & 1; s = (s >> 1) | (fb << 30)   # x^31 + x^3 + 1
    return out
def block_entropy_deficit(c, nmax=10):
    res = []
    for n in range(1, nmax + 1):
        words = np.lib.stride_tricks.sliding_window_view(c, n); keys = words @ (1 << np.arange(n)[::-1])
        cnt = np.bincount(keys, minlength=2**n).astype(float); p = cnt[cnt > 0] / cnt.sum()
        H = -(p * np.log2(p)).sum(); res.append(int(round(1000 * (n - H))))
    return res
def berlekamp_massey(bits):
    s = [int(b) for b in bits]; n = len(s); C = [1] + [0]*n; B = [1] + [0]*n; L = 0; m = -1
    for i in range(n):
        d = s[i]
        for j in range(1, L + 1): d ^= C[j] & s[i - j]
        if d:
            Tc = C[:]
            for j in range(0, n - i + m + 1):
                if B[j]: C[j + i - m] ^= 1
            if L <= i // 2: L = i + 1 - L; m = i; B = Tc
    return L
def kernel_distinct(c, depth=6, length=64):
    q = 1 << depth; seqs = set()
    for r in range(q): seqs.add(tuple(c[r:r + q*length:q][:length]))
    return len(seqs)
def max_autocorr(c, K=64):
    x = c.astype(float) - 0.5; return max(abs(4 * np.mean(x[:-k] * x[k:])) for k in range(1, K + 1))
def residue_dev(c, m=8):
    return max(abs(c[r::m].mean() - 0.5) for r in range(m))
seqs = [("iid coin", rng.integers(0, 2, N).astype(np.uint8)), ("Thue-Morse", thue_morse(N)), ("Rudin-Shapiro", rudin_shapiro(N)),
        ("LFSR-31", lfsr(N))] + [(f"rule30 W={W}" + (" (single seed)" if W == 0 else ""), rule30_centre(W, N)) for W in (0, 2, 8, 32, 128)]
print(f"N={N}; tells: entropy deficit (millibits) n=1..10 | linear complexity of 2048 | 2-kernel distinct (64 max) | max|autocorr| lags 1..64 | max residue dev mod 8")
for name, c in seqs:
    ed = block_entropy_deficit(c); lc = berlekamp_massey(c[:2048]); kd = kernel_distinct(c); ac = max_autocorr(c); rd = residue_dev(c)
    print(f"{name:28s} density={c.mean():.4f} | deficit={ed} | LC={lc} | kernel={kd} | autocorr={ac:.4f} | residue={rd:.4f}", flush=True)
print("FAKE_COIN_TELLS_DONE")
