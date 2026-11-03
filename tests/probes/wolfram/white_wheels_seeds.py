#!/usr/bin/env python3
"""white_wheels_seeds.py E NSEEDS: the left crystal's eventually-white wheels and period doublings for random finite seeds (round
14, fifth block; Cloud, CL695). Left-finite system (bit k = wheel k of a big integer; the seed's bits occupy wheels 0..23, odd so
wheel 0 is black), run to 1.45 E + 64 as band_coincidence.py does, cycles read from the last 64 rows. For each seed: the all-white
wheels below E, the period before and after each, the weight of the farther neighbour over its least period (odd = doubling, even =
branch), the gaps. Prediction (tracker): gaps within a factor 4 of 2^P for the regime's period P."""
import sys, numpy as np
E, NS = int(sys.argv[1]), int(sys.argv[2]); WB = int(sys.argv[3]) if len(sys.argv) > 3 else 24; K = E + 64; MASK = (1 << K) - 1; T = int(1.45 * E) + 64
def stp(V): return ((V << 2) ^ ((V << 1) | V)) & MASK
rng = np.random.default_rng(31)
def period32(w):
    for p in (1, 2, 4, 8, 16, 32):
        if all(((w >> i) & 1) == ((w >> ((i + p) % 32)) & 1) for i in range(32)): return p
    return None
for s in range(NS):
    seed = int(rng.integers(0, 1 << WB)) | 1
    V = seed
    for t in range(T - 64): V = stp(V)
    rows = []
    for t in range(64): rows.append(V); V = stp(V)
    nbytes = (K + 7) // 8
    R = np.zeros((64, K), dtype=np.uint8)
    for i, r in enumerate(rows):
        R[i] = np.unpackbits(np.frombuffer(r.to_bytes(nbytes, 'little'), dtype=np.uint8), bitorder='little')[:K]
    w0 = np.zeros(K, dtype=np.int64); w1 = np.zeros(K, dtype=np.int64)
    for i in range(32):
        w0 |= R[i].astype(np.int64) << i; w1 |= R[32 + i].astype(np.int64) << i
    bad = int((w0 != w1)[:E].sum()); words = [int(x) for x in w0]
    ew = [e for e in range(2, E) if words[e] == 0 and period32(words[e - 1]) is not None]
    out = []
    prev = None
    for e in ew:
        pb = period32(words[e - 1]); pa = period32(words[e + 1]) if e + 1 < E else None
        wt = bin(words[e - 1] & ((1 << pb) - 1)).count('1') if pb else None
        out.append((e, pb, pa, wt, 'doubling' if wt is not None and wt % 2 else 'branch', (e - prev) if prev is not None else None)); prev = e
    print(f"seed 0x{seed:x} ({WB} bits): wheels not 32-periodic over the last 64 rows below E: {bad}; white wheels (wheel, period before, after, weight of the farther neighbour over its period, kind, gap): {out}", flush=True)
print("WHITE_WHEELS_SEEDS_DONE")
