#!/usr/bin/env python3
"""parity_census.py T: M5, rebuilt after GPT's GC2526 (the first form held x = +2 white inside the centre's cone; its output is kept
as parity_census_clamped.out). The single seed on the full cone [-T, T], rows bit-packed; the centre column and the parities of the
OR-events along the centre's past diagonal: crystal (settled samples e <= t/3), settling (2t/3..0.8t), core (s >= 0.8t), and the
news parity centre XOR crystal; density, autocorrelation, run law. A brute-force control at small T checks the packed evolution and
the scatter against the direct array. Cloud, Block 20 rebuilt 2026-11-03 (CL694)."""
import sys, numpy as np, hashlib
T = int(sys.argv[1])
def step(r):
    n = np.zeros_like(r); n[1:-1] = r[:-2] ^ (r[1:-1] | r[2:]); return n
def evolve_packed(T):
    W = 2 * T + 3; c0 = T + 1; row = np.zeros(W, dtype=np.uint8); row[c0] = 1
    packed = []; centre = np.zeros(T + 1, dtype=np.uint8)
    for t in range(T + 1):
        centre[t] = row[c0]; packed.append(np.packbits(row))
        if t < T: row = step(row)
    return packed, centre, W, c0
def parities(packed, centre, W, c0, T):
    # P_all[t] = XOR over s < t of (X[s, s-t+1] | X[s, s-t+2]); crystal part: samples with e = 2s - t + 1 <= t/3, i.e. t >= ceil(3(2s+1)/4);
    # core part: s >= 0.8 t, i.e. t <= s/0.8; settling: the rest
    P_all = np.zeros(T + 2, dtype=np.uint8); P_cry = np.zeros(T + 2, dtype=np.uint8); P_core = np.zeros(T + 2, dtype=np.uint8)
    for s in range(T):
        row = np.unpackbits(packed[s])[:W]
        # for t in (s, T]: x1 = s - t + 1 ranges from 0 (t = s+1) down to s - T + 1; cell index c0 + x1 and c0 + x1 + 1
        tmax = T; xs = np.arange(s - tmax + 1, 1)          # x1 values ascending: t = s + 1 - x1 descending
        v = row[c0 + xs] | row[c0 + xs + 1]                 # events for t = s + 1 - xs
        ts = s + 1 - xs                                     # t values (descending)
        P_all[ts] ^= v
        # crystal: t >= ceil(3(2s+1)/4) ; core: t <= floor(s/0.8) = floor(5s/4)
        tc = -(-3 * (2 * s + 1) // 4); mcry = ts >= tc; P_cry[ts[mcry]] ^= v[mcry]
        tk = (5 * s + 4) // 4; mcore = ts <= tk; P_core[ts[mcore]] ^= v[mcore]   # s >= floor(0.8 t)  <=>  t <= floor((5s+4)/4)
    P_all = P_all[:T + 1]; P_cry = P_cry[:T + 1]; P_core = P_core[:T + 1]
    return P_all, P_cry, P_core
# brute-force control at small T
Tc = 300; Wc = 2 * Tc + 3; cc = Tc + 1; X = np.zeros((Tc + 1, Wc), dtype=np.uint8); X[0, cc] = 1
for t in range(Tc): X[t + 1] = step(X[t])
pk, cen, Wp, c0p = evolve_packed(Tc)
assert all(np.array_equal(np.unpackbits(pk[t])[:Wp], X[t]) for t in range(Tc + 1)), "packed evolution differs from the direct array"
Pa, Pc, Pk = parities(pk, cen, Wp, c0p, Tc)
for t in range(1, Tc + 1):
    s = np.arange(t); e = (X[s, cc + s - t + 1] | X[s, cc + s - t + 2]).astype(np.int64)
    smax = (4 * t // 3 - 1) // 2
    assert int(e.sum() & 1) == int(cen[t]) == int(Pa[t]), f"identity fails at t={t}"
    assert int(e[:smax + 1].sum() & 1) == int(Pc[t]), f"crystal part differs at t={t}"
    assert int(e[int(0.8 * t):].sum() & 1) == int(Pk[t]), f"core part differs at t={t}"
print(f"control T={Tc}: packed evolution equals the direct array; identity and segment parities agree at every t")
packed, centre, W, c0 = evolve_packed(T)
print(f"single seed on [-{T}, {T}] to T={T}; row digest at T: {hashlib.sha256(packed[T].tobytes()).hexdigest()[:16]}")
P_all, P_cry, P_core = parities(packed, centre, W, c0, T)
assert np.array_equal(P_all[1:], centre[1:]), "the parity identity fails"
P_set = P_all ^ P_cry ^ P_core
n0 = 128
cols = {'centre': centre[n0:], 'crystal e<=t/3': P_cry[n0:], 'news (centre XOR crystal)': (centre ^ P_cry)[n0:], 'core (s>=0.8t)': P_core[n0:], 'settling (2t/3..0.8t)': P_set[n0:]}
def runs(b):
    b = np.asarray(b); ch = np.flatnonzero(np.diff(b)) + 1; L = np.diff(np.concatenate([[0], ch, [len(b)]])); return np.bincount(L)
print(f"{T + 1 - n0} samples per column (t >= {n0}); the identity sum of events = centre holds at every t")
for k, v in cols.items():
    v = np.asarray(v).astype(np.int64); n = len(v); d = v.mean(); vc = v - d
    ac = [float(np.dot(vc[:-l], vc[l:]) / np.dot(vc, vc)) for l in range(1, 9)]
    rb = runs(v); tot = rb.sum(); obs = [rb[l] / tot if l < len(rb) else 0 for l in range(1, 11)]; exp = [2 ** -l for l in range(1, 11)]
    dev = [round(float((o - x) / x), 3) for o, x in zip(obs, exp)]
    print(f"{k:28s}: density {d:.4f} (binomial reference +-{0.5 / np.sqrt(n):.4f}); autocorr lags 1..8 {np.round(ac, 4).tolist()}; run-law deviation (obs/exp - 1) l=1..10 {dev}; longest run {len(rb) - 1}", flush=True)
print("PARITY_CENSUS_DONE")
