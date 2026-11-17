#!/usr/bin/env python3
"""two_fronts_ray_split.py [T]: T-a and T-d of CL708/CL714 (Cloud, 4 November 2026).

One simulation of the single-cell pattern to time T (default 65,536) in wheel coordinates k = x + t, rows kept packed to T/2.

T-a, the two crystal fronts. Left: each wheel's settling time tau_k = 1 + the last t with D_k(t + P_k) != D_k(t), where P_k
is its eventual period (least power of two <= 32 with no violation in the final window of W rows); B(t) = max{k : tau_k <= t}
(settled wheels 0..B inclusive). Trusted for t <= T/2 (G25: every wheel counted has at least T/2 rows after tau_k; periods in
the window are asserted against the universal left side's regimes). Right: e_j = least period exponent of the right diagonal
R_j (bit j of the edge code's autonomous (j+1)-bit prefix), J(t) = max{j : j + 2^e_j <= t}, the deepest diagonal that has
completed a period within the pattern's age. Uncovered width 2t - B - J - 1 (GC2602/GC2610's convention, k <= B).

T-d, the ray split. By the kit's R_step, R_j(s+1) = R_j(s) XOR (R_{j-1}(s) OR R_{j-2}(s)); telescoping from the ray's entry
into the cone, cell(t, x) = R_{j0}(t) with j0 = t - x equals Sigma(j0) XOR C_x(t), where Sigma(j0) = R_{j0}(s* + 1) is the ray's
own value one step after it leaves the settled band (s* = last s with wheel 2s - j0 <= B(s)) and C_x(t) is the parity of the OR of
the two rays beneath it over the core segment s* + 1 .. t - 1. Checked directly on random samples (asserted). Then: Sigma's
statistics and least-period search (P-D1), corr(Sigma(t - x), C_x(t)) per column (P-D2), no column period <= 4096 (P-D3)."""
import sys, time, math, numpy as np
T = int(sys.argv[1]) if len(sys.argv) > 1 else 65536
TH = T // 2; W = min(8192, T // 8); XMAX = 64; T0 = TH // 8
t_start = time.time()
width = 2 * T + 3
arr = np.zeros(width, dtype=np.uint8); arr[0] = 1
PS = [1, 2, 4, 8, 16, 32]
hist = np.zeros((33, width), dtype=np.uint8); hist[0] = arr          # hist[t % 33] = row t
lastviol = {P: np.zeros(width, dtype=np.int32) for P in PS}
rows = np.zeros((TH + 2, (width + 7) // 8), dtype=np.uint8)          # packed rows t <= TH + 1
rows[0] = np.packbits(arr)
for t in range(1, T + 1):
    new = np.zeros(width, dtype=np.uint8)
    new[0] = arr[0]
    new[1] = arr[0] | arr[1]
    new[2:] = arr[:-2] ^ (arr[1:-1] | arr[2:])
    arr = new
    hist[t % 33] = arr
    for P in PS:
        if t >= P:
            v = arr != hist[(t - P) % 33]
            lastviol[P][v] = t
    if t <= TH + 1:
        rows[t] = np.packbits(arr)
t_sim = time.time() - t_start
print(f"simulated T={T} in {t_sim:.1f} s; rows kept to {TH + 1}", flush=True)
# --- T-a left: settling times and B(t) ---
K = int(0.95 * TH)                                      # wheels considered (trusted ones are those with tau_k <= TH)
Pk = np.zeros(K + 1, dtype=np.int32); tau = np.zeros(K + 1, dtype=np.int64)
for k in range(K + 1):
    for P in PS:
        if lastviol[P][k] <= T - W:
            Pk[k] = P; tau[k] = lastviol[P][k] + 1; break
    else:
        Pk[k] = 0; tau[k] = T + 1                      # not settled within the window
# control: the universal left side's period regimes (record §8.31; white wheels 2, 7, 28, 399; periods double after 2, 7, 28, 399)
def expected_P(k):
    if k <= 2: return 1 if k != 1 else 1
    if k <= 7: return 2
    if k <= 28: return 4
    if k <= 399: return 8
    return 16
bad = [k for k in range(3, K + 1) if Pk[k] and expected_P(k) % Pk[k] != 0]
whites = [k for k in (2, 7, 28, 399) if k <= K and Pk[k] != 1]
from collections import Counter
print(f"eventual periods: wheels 3..{K}: {len(bad)} with a least period not dividing the regime's (2..7: 2, 8..28: 4, 29..399: 8, then 16); "
      f"white wheels 2, 7, 28, 399 not of period 1: {whites}; counts of least periods for wheels 400..{K}: {sorted(Counter(int(v) for v in Pk[400:K+1]).items())}")
assert len(bad) == 0 and not whites, "period regime control failed"
B = np.zeros(TH + 1, dtype=np.int64)                    # B(t) = max{k : tau_k <= t}
settled_at = np.full(TH + 1, -1, dtype=np.int64)
for k in range(K + 1):
    if tau[k] <= TH:
        settled_at[tau[k]] = max(settled_at[tau[k]], k)
m = -1
for t in range(TH + 1):
    m = max(m, settled_at[t]); B[t] = m
assert B[TH] < K, "B reached the considered range; enlarge K"
# --- T-a right: e_j and J(t) ---
def least_exp(j):
    mask = (1 << (j + 1)) - 1
    n = 1; seq = bytearray()
    while True:
        seq.append((n >> j) & 1)
        n = (n ^ ((n << 1) | (n << 2))) & mask
        if n == 1: break
    E = len(seq).bit_length() - 1; assert len(seq) == 1 << E
    for m in range(0, E + 1):
        P = 1 << m
        if P >= len(seq) or seq[P:] == seq[:-P]:
            return m, E
e = {}; Eprefix = {}
for j in range(0, 45):
    e[j], Eprefix[j] = least_exp(j)
dbl = [j for j in range(1, 45) if Eprefix[j] > Eprefix[j - 1]]
print(f"prefix period doubles at depths {dbl}")
assert dbl[:16] == [1, 3, 4, 6, 7, 9, 15, 16, 24, 25, 27, 29, 34, 36, 37, 39], "doubling depths control (84a42c) failed"
print(f"bit least-period exponents e_j equal the prefix exponent at {sum(e[j] == Eprefix[j] for j in e)} of 45 depths")
def J(t):
    return max([j for j in e if j + (1 << e[j]) <= t], default=-1)
print("\n=== T-a: the two crystal fronts (trusted t <= T/2) ===")
print("      t     B(t)   B/t    J(t)  2.4log2t  uncovered 2t-B-J-1  fraction")
for p in range(8, int(math.log2(TH)) + 1):
    t = 1 << p; b = int(B[t]); jj = J(t); unc = 2 * t - b - jj - 1
    print(f"{t:7d} {b:8d} {b/t:6.3f} {jj:6d} {2.4*p:9.1f} {unc:12d} {unc/(2*t+1):9.3f}")
ts = np.arange(T0, TH + 1); slope = np.polyfit(ts, B[T0:TH + 1], 1)[0]
print(f"B(t) slope over [{T0}, {TH}]: {slope:.4f}; B(t)/t at t = {TH}: {B[TH]/TH:.4f}")
pmax = int(math.log2(TH)); Jt = np.array([J(1 << p) for p in range(8, pmax + 1)]); lg = np.arange(8, pmax + 1)
cj = np.polyfit(lg, Jt, 1)
print(f"J(t) against log2 t over t = 2^8..2^{pmax}: slope {cj[0]:.3f}, intercept {cj[1]:.2f}")
# --- T-d: the ray split ---
print("\n=== T-d: the ray split ===")
def cell(t, k):                                          # cell at time t, wheel k, from the packed rows
    return (rows[t, k >> 3] >> (7 - (k & 7))) & 1
JMAX = TH + XMAX                                         # rays j0 = t - x with t <= TH, |x| <= XMAX
sstar = np.zeros(JMAX + 1, dtype=np.int64); Sigma = np.zeros(JMAX + 1, dtype=np.uint8)
for j0 in range(JMAX + 1):
    s = (j0 + 1) // 2                                    # entry: wheel 2s - j0 in {0, 1}
    while s + 1 <= TH and 2 * (s + 1) - j0 <= B[s + 1]: s += 1
    assert 2 * s - j0 <= B[s] and (s + 1 > TH or 2 * (s + 1) - j0 > B[s + 1])
    assert s + 1 <= TH + 1, f"exit beyond kept rows for ray {j0}"
    sstar[j0] = s
    Sigma[j0] = cell(s + 1, 2 * (s + 1) - j0)            # R_{j0}(s* + 1) = cell(s*+1, s*+1-j0), wheel = 2(s*+1) - j0
print("exit times s*(j0)/j0 at j0 = " + ", ".join(f"{j}: {sstar[j]/j:.3f}" for j in (1000, 10000, TH) if j <= JMAX))
# direct check of the telescoping identity on random samples
rng = np.random.default_rng(20261104); nchk = 0
for _ in range(2000):
    t = int(rng.integers(T0, TH + 1)); x = int(rng.integers(-XMAX, XMAX + 1)); j0 = t - x
    s = sstar[j0]; par = 0
    for u in range(s + 1, t):
        a = cell(u, 2 * u - j0 + 1); b = cell(u, 2 * u - j0 + 2)   # R_{j0-1}(u) at wheel 2u-(j0-1), R_{j0-2}(u) at wheel 2u-(j0-2)
        par ^= (a | b)
    c = cell(t, t + x)
    assert (int(Sigma[j0]) ^ par) == c, (t, x)
    nchk += 1
print(f"telescoping identity cell(t,x) = Sigma(t-x) XOR core-parity: {nchk} random samples, all exact")
# Sigma statistics
S = Sigma[: TH + 1].astype(np.int8)
dens = S[T0:].mean()
sc = S[T0:] * 2 - 1; acs = [abs(np.mean(sc[:-L] * sc[L:])) for L in range(1, 65)]
print(f"Sigma (band-edge transect, j0 in [{T0}, {TH}]): density {dens:.4f}, max |autocorr| lags 1..64 = {max(acs):.4f}")
def least_period(seq, pmax):
    for P in range(1, pmax + 1):
        if np.array_equal(seq[P:], seq[:-P]): return P
    return None
for lo, hi in [(10, 42), (42, 598), (598, min(4096, TH)), (T0, TH)]:
    seg = S[lo:hi]; lp = least_period(seg, min(4096, len(seg) // 4))
    print(f"  Sigma on [{lo}, {hi}): least period <= {min(4096, len(seg)//4)}: {lp}")
# per-column: cell, S, C over t in [T0, TH]
print("per column x in [-64, 64], t in [%d, %d]:" % (T0, TH))
maxcorr = 0.0; corrs = []; periods_found = []
tt = np.arange(T0, TH + 1)
for x in range(-XMAX, XMAX + 1):
    ks = tt + x
    cells = ((rows[tt, ks >> 3] >> (7 - (ks & 7))) & 1).astype(np.int8)
    Sx = Sigma[tt - x].astype(np.int8); Cx = cells ^ Sx
    a = Sx * 2 - 1; b = Cx * 2 - 1
    r = float(np.mean(a * b)); corrs.append(r); maxcorr = max(maxcorr, abs(r))
    lp = least_period(cells, min(4096, len(cells) // 4))   # cap at a quarter of the window (added after the T = 65,536 run, where 4096 < 28,673/4 already held)
    if lp is not None: periods_found.append((x, lp))
print(f"  P-D2: max |corr(Sigma(t-x), C_x(t))| over 129 columns = {maxcorr:.4f}; mean corr {np.mean(corrs):+.4f}; 2/sqrt(n) = {2/math.sqrt(len(tt)):.4f}")
print(f"  P-D3: columns with a period <= 4096 on the window: {periods_found if periods_found else 'none'}")
# the centre column's core-segment length
print(f"  core segment length t - s*(t) at t = {TH}: {TH - sstar[TH]} ({(TH - sstar[TH])/TH:.3f} t)")
print(f"total {time.time() - t_start:.1f} s")
print("TWO_FRONTS_RAY_SPLIT_DONE")
