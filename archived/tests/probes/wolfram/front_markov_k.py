#!/usr/bin/env python3
"""front_markov_k.py T NS: does the fair-row damage front's speed close as a k-step Markov chain on step types? Fit P(heal | last k types)
and E[jump | heal, last k types] from data, build each chain, compute its stationary speed 1 - sum pi(h) P(heal|h) E[jump|heal,h], and
compare with the direct speed. Cloud, Block 26 (M4's residue)."""
import sys, numpy as np
from collections import defaultdict
T, NS = int(sys.argv[1]), int(sys.argv[2]); rng = np.random.default_rng(11)
def step(r):
    n = np.zeros_like(r); n[1:-1] = r[:-2] ^ (r[1:-1] | r[2:]); return n
WL = 2*T + 100; WR = T + 60; W = WL + WR
jumps = []
for s in range(NS):
    a = rng.integers(0, 2, W).astype(np.uint8); b = a.copy(); b[WL] ^= 1; kp = None; js = []
    for t in range(T + 1):
        d = np.flatnonzero(a ^ b); k = int(d.min()) + t
        if kp is not None and t > T//4: js.append(k - kp)
        kp = k
        if t < T: a, b = step(a), step(b)
    jumps.append(np.array(js))
allj = np.concatenate(jumps); direct = 1 - allj.mean()
print(f"fair row, {NS} rows, T={T}, {len(allj)} steps; direct speed {direct:.4f}")
for k in range(0, 6):
    cnt = defaultdict(lambda: [0, 0, 0.0])   # history -> [n, n_heal, sum jump at heals]
    for js in jumps:
        typ = (js > 0).astype(int)
        for i in range(k, len(js)):
            h = tuple(typ[i-k:i]); c = cnt[h]; c[0] += 1
            if js[i] > 0: c[1] += 1; c[2] += js[i]
    # chain on histories of length k (shift register of types): transition h -> h[1:] + (type,)
    hist = list(cnt.keys()); idx = {h: i for i, h in enumerate(hist)}; n = len(hist)
    P = np.zeros((n, n)); gain = np.zeros(n)
    for h in hist:
        c = cnt[h]; ph = c[1] / c[0]; ej = (c[2] / c[1]) if c[1] else 0.0
        gain[idx[h]] = ph * ej
        for typ, pr in ((1, ph), (0, 1 - ph)):
            nh = (h + (typ,))[1:] if k > 0 else ()
            if nh in idx: P[idx[h], idx[nh]] += pr
    # stationary distribution
    w, v = np.linalg.eig(P.T); pi = np.real(v[:, np.argmin(np.abs(w - 1))]); pi = pi / pi.sum()
    speed = 1 - float(pi @ gain)
    print(f"  k={k}: {n} histories; implied speed {speed:.4f} (difference from direct {speed - direct:+.4f})")
print("FRONT_MARKOV_K_DONE")
