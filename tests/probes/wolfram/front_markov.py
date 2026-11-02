#!/usr/bin/env python3
"""front_markov.py T NS: the fair-row damage front (single flip) and its local statistics: the mask lemma control, jump independence,
and the white-ahead bias conditioned on the previous step. Cloud, Block 21(b)."""
import sys, numpy as np
T, NS = int(sys.argv[1]), int(sys.argv[2]); rng = np.random.default_rng(7)
def step(r):
    n = np.zeros_like(r); n[1:-1] = r[:-2] ^ (r[1:-1] | r[2:]); return n
WL = 2*T + 100; WR = T + 60; W = WL + WR
rec = []   # (jump, a[x-3..x-1], a[x..x+2], b[x..x+2])
for s in range(NS):
    a = rng.integers(0, 2, W).astype(np.uint8); b = a.copy(); b[WL] ^= 1
    xm_prev = None; k_prev = None
    for t in range(T + 1):
        d = np.flatnonzero(a ^ b); x = int(d.min()); k = x + t
        if t >= T//4 and k_prev is not None:
            rec.append((k - k_prev, int(a[x-3]), int(a[x-2]), int(a[x-1]), int(a[x]), int(a[x+1]), int(a[x+2]), int(b[x]), int(b[x+1]), int(b[x+2])))
        if t >= 1:
            assert k >= k_prev
        # the mask lemma control uses the PREVIOUS state's a[x-1]: record it as the jump just made (k - k_prev) against a_prev[x_prev-1]
        k_prev = k
        if t < T: a, b = step(a), step(b)
rec = np.array(rec)
jump = rec[:, 0]; a3, a2, a1 = rec[:, 1], rec[:, 2], rec[:, 3]
print(f"fair row, single flip, {NS} rows, T={T}, {len(rec)} steps recorded after T/4")
print("jump distribution 0..7:", np.round(np.bincount(jump, minlength=8)[:8]/len(jump), 4).tolist(), "mean", round(float(jump.mean()), 4), "=> v =", round(1 - float(jump.mean()), 4))
# P-K2: the NEXT jump is 0 iff a[x-1] = 0 at the current step: compare jump[i+1] with a1[i]
nxt = jump[1:]; ahead_white = (a1[:-1] == 0)
print(f"P-K2 mask lemma: next jump 0 when a[x-1]=0: {np.mean(nxt[ahead_white] == 0):.4f}; next jump 0 when a[x-1]=1: {np.mean(nxt[~ahead_white] == 0):.4f}")
heal = jump > 0
print(f"P(heal)={heal.mean():.4f}; P(heal | prev heal)={heal[1:][heal[:-1]].mean():.4f}; P(heal | prev advance)={heal[1:][~heal[:-1]].mean():.4f}")
print(f"P(a[x-1]=0)={np.mean(a1==0):.4f}; P(a[x-2]=0)={np.mean(a2==0):.4f}; P(a[x-3]=0)={np.mean(a3==0):.4f}")
prev_adv = ~heal[:-1]
print(f"P(a[x-1]=0 | previous step an advance)={np.mean(a1[1:][prev_adv]==0):.4f}; P(a[x-1]=0 | previous step a heal)={np.mean(a1[1:][~prev_adv]==0):.4f}")
for j in range(1, 5):
    sel = jump[:-1] == j
    if sel.sum() > 50: print(f"  P(a[x-1]=0 | previous jump = {j}) = {np.mean(a1[1:][sel]==0):.4f} (n={int(sel.sum())})")
# jump size given heal: distribution by the damaged pair pattern (a[x],a[x+1],b[x],b[x+1]) at the previous step
E = rec[:, 4:7]; Bv = rec[:, 7:10]
pat = (rec[:-1, 4] << 3) | (rec[:-1, 5] << 2) | (rec[:-1, 7] << 1) | rec[:-1, 8]
print("E[next jump | a[x-1]=1, pattern (a[x],a[x+1],b[x],b[x+1])]:", {f"{p:04b}": round(float(nxt[(pat == p) & ~ahead_white].mean()), 3) for p in range(16) if ((pat == p) & ~ahead_white).sum() > 100})
print("FRONT_MARKOV_DONE")
