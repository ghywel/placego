#!/usr/bin/env python3
"""parity_census.py T: M5. The single seed to time T; the centre column, the crystal parity (settled samples e <= t/3 along the past
diagonal), the news parity, the core parity and the settling-zone parity; density, autocorrelation, run-length law. Cloud, Block 20."""
import sys, numpy as np
T = int(sys.argv[1])
# store x in [-T-2, 2]: index i <-> x = i - (T+2)
W = T + 5; c0 = T + 2
X = np.zeros((T+1, W), dtype=np.uint8); X[0, c0] = 1
for t in range(T):
    r = X[t]; n = np.zeros_like(r); n[1:-1] = r[:-2] ^ (r[1:-1] | r[2:]); X[t+1] = n
centre = X[:, c0].astype(np.int64)
def events(t):
    s = np.arange(t); return (X[s, c0 + s - t + 1] | X[s, c0 + s - t + 2]).astype(np.int64)
n0 = 128
cols = {'centre': [], 'crystal e<=t/3': [], 'news (centre XOR crystal)': [], 'core (s>=0.8t)': [], 'settling (2t/3..0.8t)': []}
for t in range(n0, T+1):
    e = events(t)
    # sampled diagonal e_d = 2s - t + 1 <= t/3  <=>  s <= (4t/3 - 1)/2
    smax = (4*t//3 - 1)//2
    pc = int(e[:smax+1].sum() & 1); x0 = int(centre[t]); assert (e.sum() & 1) == x0
    cols['centre'].append(x0); cols['crystal e<=t/3'].append(pc); cols['news (centre XOR crystal)'].append(x0 ^ pc)
    cols['core (s>=0.8t)'].append(int(e[int(0.8*t):].sum() & 1)); cols['settling (2t/3..0.8t)'].append(int(e[smax+1:int(0.8*t)].sum() & 1))
def runs(b):
    b = np.asarray(b); ch = np.flatnonzero(np.diff(b)) + 1; L = np.diff(np.concatenate([[0], ch, [len(b)]])); return np.bincount(L)
print(f"single seed to T={T}; {T+1-n0} samples per column")
for k, v in cols.items():
    v = np.asarray(v); n = len(v); d = v.mean(); vc = v - d
    ac = [float(np.dot(vc[:-l], vc[l:]) / np.dot(vc, vc)) for l in range(1, 9)]
    rb = runs(v); tot = rb.sum(); obs = [rb[l]/tot if l < len(rb) else 0 for l in range(1, 11)]; exp = [2**-l for l in range(1, 11)]
    dev = [round((o - x)/x, 3) for o, x in zip(obs, exp)]
    print(f"{k:28s}: density {d:.4f} (+-{0.5/np.sqrt(n):.4f}); autocorr lags 1..8 {np.round(ac, 4).tolist()}; run-law deviation (obs/exp - 1) l=1..10 {dev}; longest run {len(rb)-1}", flush=True)
print("PARITY_CENSUS_DONE")
