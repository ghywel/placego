#!/usr/bin/env python3
"""band_coincidence.py E_MAX: the single seed's left band to depth E_MAX on the autonomous big-integer system, run to 1.45 E_MAX so every
diagonal is settled; the periodic word of each diagonal; eventually-white diagonals and their doubling/branch parity; the Hamming
distance between consecutive words against the binomial law. Cloud, Block 22."""
import sys, math, numpy as np
E = int(sys.argv[1]); K = E + 64; MASK = (1 << K) - 1; T = int(1.45 * E) + 64
def stp(V): return ((V << 2) ^ ((V << 1) | V)) & MASK
V = 1
for t in range(T - 64): V = stp(V)
rows = []
for t in range(64): rows.append(V); V = stp(V)
# bit extraction vectorised: each row to a numpy bit array (bit e of row = diagonal e), then 32-bit words per diagonal
nbytes = (K + 7) // 8
R = np.zeros((64, K), dtype=np.uint8)
for i, r in enumerate(rows):
    bits = np.unpackbits(np.frombuffer(r.to_bytes(nbytes, 'little'), dtype=np.uint8), bitorder='little')
    R[i] = bits[:K]
np.save('band_rows64.npy', np.packbits(R, axis=1))     # checkpoint of the 64 settled rows
w0 = np.zeros(K, dtype=np.int64); w1 = np.zeros(K, dtype=np.int64)
for i in range(32):
    w0 |= R[i].astype(np.int64) << i; w1 |= R[32 + i].astype(np.int64) << i
bad = int((w0 != w1)[:E].sum()); words = [int(x) for x in w0]
print(f"band to E={E}: diagonals not 32-periodic over the last 64 rows: {bad} (expected 0 up to E; the last 64 may be unsettled)")
def period(w):
    for p in (1, 2, 4, 8, 16, 32):
        if all(((w >> i) & 1) == ((w >> ((i + p) % 32)) & 1) for i in range(32)): return p
ew = [e for e in range(2, E) if words[e] == 0]
print("eventually-white diagonals to E:", ew)
for e in ew:
    wt = bin(words[e-1]).count('1') // (32 // period(words[e-1]))   # black cells per period of L_(e-1)
    print(f"  e={e}: period before {period(words[e-1])}, after {period(words[e+1]) if e+1 < len(words) else None}; weight of L_(e-1) per period {wt} -> {'doubling' if wt % 2 else 'branch'}")
# Hamming distance between consecutive words, by regime
def ham(a, b): return bin(a ^ b).count('1')
for (lo, hi, P) in ((399, 87866, 16), (87866, min(E, len(words) - 1), 32)):
    ds = []
    for e in range(lo + 2, hi):
        a, b = words[e-2], words[e-1]
        if P == 16: a &= 0xFFFF; b &= 0xFFFF
        ds.append(ham(a, b))
    ds = np.array(ds); n = len(ds)
    binom = [math.comb(P, k) / 2**P for k in range(P + 1)]
    obs = np.bincount(ds, minlength=P + 1) / n
    print(f"regime period {P}, e in [{lo}, {hi}): {n} pairs; mean d {ds.mean():.3f} (binomial {P/2}); min d {ds.min()}; count d=0: {int((ds == 0).sum())}")
    cum_obs = np.cumsum(obs); cum_b = np.cumsum(binom)
    print("  P(d<=k) observed / binomial for k=0..4:", [(round(float(cum_obs[k]), 6), round(cum_b[k], 6), round(float(cum_obs[k] / cum_b[k]), 2) if cum_b[k] > 0 else None) for k in range(5)])
    print("  d histogram (first 10 bins):", np.round(obs[:10], 4).tolist(), "binomial:", [round(x, 4) for x in binom[:10]])
print("BAND_COINCIDENCE_DONE")
