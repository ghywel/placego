#!/usr/bin/env python3
"""front_feet.py T NS: the fair-row damage front's intrinsic coin against its wake (inquisition round 14, Q5; Cloud, CL691).
Single flip on a fair row. At every step the cell ahead of the leftmost mismatch, (x-1, t), has left foot x-1-t. The foot is FRESH
if it is strictly left of every earlier cell ahead's foot (tracked from t = 0). Hand claim (left-feet lemma): at a fresh foot the cell
ahead is a fair coin independent of the whole history, so the advance decision there is exactly 1/2; at reused feet the wake decides.
Predictions (tracker round 14): P-a1 P(white | fresh) = 1/2 +- 2 se; P-a2 P(white | reused) off 1/2 by > 0.1; P-a3 the 0.491 after
an advance is a fresh/reused mixture. Output: front_feet.out."""
import sys, numpy as np
T, NS = int(sys.argv[1]), int(sys.argv[2]); rng = np.random.default_rng(11)
def step(r):
    n = np.zeros_like(r); n[1:-1] = r[:-2] ^ (r[1:-1] | r[2:]); return n
WL = 2*T + 100; WR = T + 60; W = WL + WR
rows = []   # (trial, t, jump_just_made, ahead_white, fresh, dist_to_min, prev_jump)
for s in range(NS):
    a = rng.integers(0, 2, W).astype(np.uint8); b = a.copy(); b[WL] ^= 1
    k_prev = None; minfoot = None; prevjump = -1
    for t in range(T + 1):
        d = np.flatnonzero(a ^ b); x = int(d.min()); k = x + t
        jump = (k - k_prev) if k_prev is not None else -1
        foot = x - 1 - t
        fresh = (minfoot is None) or (foot < minfoot)
        dist = 0 if fresh else foot - minfoot
        if t >= T // 4 and k_prev is not None:
            rows.append((s, t, jump, int(a[x-1] == 0), int(fresh), dist, prevjump))
        if minfoot is None or foot < minfoot: minfoot = foot
        k_prev = k; prevjump = jump
        if t < T: a, b = step(a), step(b)
R = np.array(rows)
jump, white, fresh, dist, prevj = R[:, 2], R[:, 3], R[:, 4], R[:, 5], R[:, 6]
n = len(R); print(f"fair row, single flip, {NS} rows, T={T}, {n} steps after T/4")
def rep(mask, label):
    m = int(mask.sum());
    if m: print(f"  {label:58s} n={m:6d}  P(white ahead)={white[mask].mean():.4f}  se={np.sqrt(0.25/m):.4f}")
rep(np.ones(n, bool), "all steps")
rep(fresh == 1, "fresh foot")
rep(fresh == 0, "reused foot")
rep(jump == 0, "step just made an advance (jump 0)")
rep((jump == 0) & (fresh == 1), "advance, fresh foot")
rep((jump == 0) & (fresh == 0), "advance, reused foot")
print(f"  reused fraction after advances: {((jump == 0) & (fresh == 0)).sum() / max(1, (jump == 0).sum()):.4f}")
for j in range(1, 6):
    rep(jump == j, f"step just made a heal of {j}")
    rep((jump == j) & (fresh == 1), f"heal of {j}, fresh foot")
    rep((jump == j) & (fresh == 0), f"heal of {j}, reused foot")
print("PU: white-ahead frequency by distance of the foot from the running minimum (reused cells):")
for dd in range(0, 8):
    mk = (fresh == 0) & (dist == dd)
    if mk.sum() > 30: print(f"  dist {dd}: n={int(mk.sum())} P(white)={white[mk].mean():.4f}")
mk = (fresh == 0) & (dist >= 8)
if mk.sum() > 30: print(f"  dist >= 8: n={int(mk.sum())} P(white)={white[mk].mean():.4f}")
print("FRONT_FEET_DONE")
