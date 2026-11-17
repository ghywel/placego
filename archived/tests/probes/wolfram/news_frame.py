#!/usr/bin/env python3
"""news_frame.py [T]: T-c, the news frame (Cloud, CL718; the atlas grid's row v = -0.246).

The left-frame system as a big integer V_t (bit k = wheel k, V' = (V<<2) XOR ((V<<1) OR V)), the single seed to time T (65,536).
The lag-16 band edge B(t) = lowest wheel where rows t and t+16 differ (CL692's object; GC2621: the contiguous least-period
settling frontier is B(t) - 1 on the certified prefix). In the frame moving with B the dynamics is: shift by Delta_t = B(t+1) - B(t)
and apply the rule (GC2602's equation), with Delta_t given by the mask law (B stays iff the decider wheel B-1 is white at t,
CL692 H1a, exact) and the jump by the mismatch pattern above the edge (CL692 H1d). Incoming cells enter from the deep side.

Measured here (trusted t in [T/8, T/2], every wheel counted certified 16-periodic by the autonomous prefix agreeing at T-W and
T-W+16, GC2621's cross-check): C1 B(t)-1 against the contiguous frontier from the lag-16 settling times (control); the mask law
(control); the step law (distribution of Delta, mean, P(heal), E[jump|heal]) against section 8.74 and 8.66; C2 the determination
horizon of Delta: collisions of the window state (decider, rows t and t+16 on wheels B..B+w) with different Delta, for w = 0..24;
C3-C5 the mismatch-density profile rho(h) = P(row_t XOR row_{t+16} at wheel B+h) for h = 0..64, its bulk value and its stationarity
across halves; C6 the row's own black density across the frontier, h in [-16, 64]."""
import sys, time, math, numpy as np
from collections import Counter, defaultdict
T = int(sys.argv[1]) if len(sys.argv) > 1 else 65536
W = min(8192, T // 8); TH = T // 2; T0 = T // 8; P = 16; HMAX = 64
t0 = time.time()
K = 2 * T + 40; MASK = (1 << K) - 1
rows = [1]; V = 1
for t in range(T + P + 1):
    V = ((V << 2) ^ ((V << 1) | V)) & MASK; rows.append(V)
print(f"simulated T={T} ({time.time()-t0:.1f} s)", flush=True)
def bits_of(v, n):                                     # bool array of the lowest n bits of v, index = wheel
    b = (v & ((1 << n) - 1)).to_bytes((n + 7) // 8, 'little')
    return np.unpackbits(np.frombuffer(b, dtype=np.uint8), bitorder='little')[:n].astype(bool)
# certified prefix: wheels agreeing at T-W and T-W+16 (autonomous prefix, so the equality propagates forever)
agree = ~bits_of(rows[T - W] ^ rows[T - W + P], K)
Kc = int(np.argmin(agree)) if not agree.all() else K        # first disagreeing wheel; wheels < Kc certified
print(f"certified 16-periodic prefix at T-W: wheels 0..{Kc-1}")
# lag-16 settling times from the last lag-16 mismatch, t <= T-W, on the certified prefix
lastviol = np.full(Kc, -1, dtype=np.int64)
for t in range(0, T - W + 1):
    d = bits_of(rows[t] ^ rows[t + P], Kc)
    lastviol[d] = t
tau16 = lastviol + 1
pm = np.maximum.accumulate(tau16)
def Bcontig(t): return int(np.searchsorted(pm, t, side='right')) - 1   # deepest k with every wheel <= k settled by t
# the band edge
B = np.zeros(TH + 2, dtype=np.int64)
for t in range(TH + 2):
    x = rows[t] ^ rows[t + P]; B[t] = (x & -x).bit_length() - 1
assert B[TH + 1] + HMAX + 2 < Kc, "window reaches beyond the certified prefix"
# C1: B - 1 against the contiguous frontier
mism = sum(1 for t in range(T0, TH + 1) if B[t] - 1 != Bcontig(t))
print(f"C1: B16(t)-1 == contiguous least-period frontier at {TH - T0 + 1 - mism} of {TH - T0 + 1} ticks in [{T0}, {TH}] (mismatches {mism})")
bit = lambda t, k: (rows[t] >> k) & 1 if k >= 0 else 0
# mask law control
viol = sum(1 for t in range(T0, TH + 1) if (B[t + 1] == B[t]) != (bit(t, int(B[t]) - 1) == 0))
print(f"mask law (B stays iff decider B-1 white): violations {viol} over [{T0}, {TH}]")
# step law
D = B[T0 + 1:TH + 2] - B[T0:TH + 1]
cnt = Counter(int(d) for d in D)
heal = D > 0
print(f"step law: mean Delta {D.mean():.4f} (8.74: 0.755; CL715 least-period frontier: 0.744); P(heal) {heal.mean():.4f}; "
      f"E[jump|heal] {D[heal].mean():.3f}; max jump {D.max()}; distribution {sorted(cnt.items())}")
print(f"  product P(heal)*E[jump] = {heal.mean()*D[heal].mean():.4f}; 8.66's fair-row front: 0.410 x 1.839 = 0.754")
# C2: determination horizon of Delta from the window (decider; rows t and t+16 on wheels B..B+w)
print("C2: collisions of the window state with different Delta (t in [T0, TH]):")
for w in [0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24]:
    seen = {}; coll = 0; keys = 0
    for t in range(T0, TH + 1):
        b = int(B[t]); m = (1 << (w + 1)) - 1
        key = (bit(t, b - 1), (rows[t] >> b) & m, (rows[t + P] >> b) & m)
        d = int(B[t + 1] - b)
        if key in seen:
            if seen[key] != d: coll += 1
        else:
            seen[key] = d; keys += 1
    print(f"  w={w:2d}: distinct states {keys:6d}, collisions {coll:5d}")
# C3-C5: the mismatch-density profile above the edge; C6: the row's density across the frontier
prof = np.zeros(HMAX + 1); prof1 = np.zeros(HMAX + 1); prof2 = np.zeros(HMAX + 1)
dens = np.zeros(HMAX + 17); n1 = n2 = 0; tm = (T0 + TH) // 2
for t in range(T0, TH + 1):
    b = int(B[t]); x = rows[t] ^ rows[t + P]
    seg = np.array([(x >> (b + h)) & 1 for h in range(HMAX + 1)], dtype=float)
    prof += seg
    if t < tm: prof1 += seg; n1 += 1
    else: prof2 += seg; n2 += 1
    dens += np.array([bit(t, b + h) for h in range(-16, HMAX + 1)], dtype=float)
n = TH - T0 + 1; prof /= n; prof1 /= n1; prof2 /= n2; dens /= n
print("C3: mismatch density rho(h) above the edge, h = 0..24:", " ".join(f"{v:.3f}" for v in prof[:25]))
bulk = prof[32:].mean()
print(f"C5: bulk rho (h = 32..64) = {bulk:.4f}; first h with |rho(h) - bulk| <= 0.02: {next((h for h in range(HMAX + 1) if abs(prof[h] - bulk) <= 0.02), None)}")
print(f"C4: max |rho_half1 - rho_half2| over h <= 32: {np.max(np.abs(prof1[:33] - prof2[:33])):.4f} (halves of {n1} and {n2} ticks)")
print("C6: the row's black density across the frontier, h = -16..-1 | 0..15 | 16..64:",
      f"{dens[:16].mean():.4f} | {dens[16:32].mean():.4f} | {dens[32:].mean():.4f}")
print("    by h, -16..24:", " ".join(f"{v:.2f}" for v in dens[:41]))
print(f"total {time.time()-t0:.1f} s")
print("NEWS_FRAME_DONE")
