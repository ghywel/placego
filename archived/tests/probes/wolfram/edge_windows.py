"""edge_windows.py: the seed's edge statistics in matched windows (CL743, after GC2682). The error process of
error_process.py on the seed against its strip at the seed's phase, on 894,236 wheels to the exact settling, with every
quantity of the heal identity read per window of wheels: ticks T, heals D, stays W, A (heals followed by a white parent),
B (stays followed by a black parent), q = B/W, S = A/D, p = D/T, the jump law and P(parent black | jump d); the finite
identity D/T = (q - (H_T - H_0)/T)/(q + S) (GC2682, PROVED two-party) checked in each window; and the same for the
whole run. A window is the stretch of ticks during which the edge lies in [a, a + WIDTH).
CL744: also the hazard past wheel LATE by stall length n (n = 1 also by the preceding jump) and by phase t mod 32, against
the strip's own per-phase law of the XOR below a white bit.
Usage: python3 edge_windows.py ROWSDIR [WIDTH] [K] [LATE] [STRIP] [DAMAGE]   (the rows of tree16_data.py at 894,236 wheels, phase 0;
STRIP the row's file name without .bin, default A0; DAMAGE 0 = the seed, else the strip with random damage from wheel W0 (arg 7,
default 64) with that seed; T0 (arg 8, a multiple of 32, at or past the settling bound): first evolve the damaged row T0 ticks and
identify the strip it settles on among ROWS/*.bin, then run the edge against that strip; CL745; TAU (arg 9): save the settling
ticks per wheel to this .npy, CL746)"""
import sys, time, collections
ROWS = sys.argv[1]; WIDTH = int(sys.argv[2]) if len(sys.argv) > 2 else 100000
STRIP = sys.argv[5] if len(sys.argv) > 5 else "A0"             # CL745: the strip's file name without .bin
DAMAGE = int(sys.argv[6]) if len(sys.argv) > 6 else 0            # 0: the seed (x = 1); else the strip with random damage above wheel 2 (this seed)
A0 = int.from_bytes(open(f"{ROWS}/{STRIP}.bin", 'rb').read(), 'little')
K = int(sys.argv[3]) if len(sys.argv) > 3 else 894236
MASK = (1 << K) - 1; P = 32
def step(v): return ((v << 2) ^ ((v << 1) | v)) & MASK
def lowbit(x): return (x & -x).bit_length() - 1 if x else K
cyc = [A0 & MASK]
for _ in range(P): cyc.append(step(cyc[-1]))
assert cyc[P] == cyc[0], "the strip does not return at 32 on these wheels"; cyc = cyc[:P]
class Win:
    def __init__(s): s.T = 0; s.D = 0; s.A = 0; s.B = 0; s.H0 = None; s.HT = None; s.jumps = collections.Counter(); s.pbj = collections.Counter(); s.t0 = None; s.t1 = None
wins = collections.defaultdict(Win); allw = Win()
TAU = sys.argv[9] if len(sys.argv) > 9 else None             # CL746: save the settling ticks per wheel (the first tick with the edge above the wheel) to this .npy
import numpy as np
tau = np.full(K, -1, dtype=np.int64) if TAU else None
# CL744: the hazard by stall length n and phase t mod 32, past wheel LATE; n = 1 also by the preceding jump d
LATE = int(sys.argv[4]) if len(sys.argv) > 4 else 200000
st = collections.Counter(); bk = collections.Counter()        # (n, phi) -> stall ticks, blacks at t+1
st1 = collections.Counter(); bk1 = collections.Counter()      # n = 1 by the preceding jump d
n_stall = 0; last_jump = None
import random, os
W0 = int(sys.argv[7]) if len(sys.argv) > 7 else 64          # the damage starts at wheel W0 (above the never-black wheels 2, 7, 28)
T0 = int(sys.argv[8]) if len(sys.argv) > 8 else 0           # if given: evolve the damaged row T0 ticks (a multiple of 32), identify its strip among ROWS/*.bin, use that
if DAMAGE:
    rng = random.Random(DAMAGE); x0 = (cyc[0] ^ ((rng.getrandbits(K) >> W0) << W0 | (1 << W0))) & MASK
    if T0:
        assert T0 % P == 0; y = x0
        for _ in range(T0): y = step(y)
        found = None            # the low wheels fix the phase only modulo the small periods: search every strip at every phase
        for f in sorted(os.listdir(ROWS)):
            if not f.endswith('.bin'): continue
            r = int.from_bytes(open(f"{ROWS}/{f}", 'rb').read(), 'little') & MASK; c = [r]
            for _ in range(P - 1): c.append(step(c[-1]))
            for ph in range(P):
                if c[ph] == y: found = (f[:-4], ph, c)
        assert found, "the damaged row is on none of the strips at tick T0, at any phase"
        STRIP, PHASE, c = found
        cyc = c[PHASE:] + c[:PHASE]          # the strip at the configuration's phase: compare x(t) with cyc[t mod 32]
        assert step(cyc[P - 1]) == cyc[0]
    x = x0
else: x = 1
print(f"strip {STRIP} on {K} wheels; actual row: {'the seed' if not DAMAGE else f'strip {sys.argv[5] if len(sys.argv) > 5 else 'A0'} with random damage from wheel {W0}, seed {DAMAGE}' + (f', settling on {STRIP} at phase {PHASE} by tick {T0}' if T0 else '')}")
t0 = time.time(); t = 0; m_prev = None; h_prev = None; dec = 0
while True:
    C = cyc[t % P]; e = x ^ C; m = lowbit(e)
    if m >= K: break
    if m_prev is not None and m < m_prev: dec += 1
    if TAU is not None and (m_prev is None or m > m_prev): tau[(m_prev if m_prev is not None else 0):m] = t
    h = (C >> (m - 1)) & 1 if m >= 1 else 0           # H_t: the parent black = the edge heals at t -> t+1
    x2 = step(x); C2 = cyc[(t + 1) % P]; e2 = x2 ^ C2; m2 = lowbit(e2)
    h2 = (C2 >> (m2 - 1)) & 1 if 1 <= m2 < K else 0  # H_{t+1}
    if h: n_stall = 0; last_jump = m2 - m
    else:
        n_stall += 1
        if m >= LATE:
            key = (min(n_stall, 12), t % P); st[key] += 1; bk[key] += h2
            if n_stall == 1 and last_jump is not None: st1[min(last_jump, 9)] += 1; bk1[min(last_jump, 9)] += h2     # CL746: jumps 7 and 8 separately, 9 pools the rest
    for w in (wins[m // WIDTH], allw):
        if w.H0 is None: w.H0 = h; w.t0 = t
        w.T += 1; w.HT = h2; w.t1 = t + 1
        if h:
            w.D += 1; d = m2 - m; w.jumps[d] += 1
            if h2: w.pbj[d] += 1
            else: w.A += 1
        elif h2: w.B += 1
    x = x2; t += 1; m_prev = m
print(f"settled through {K-1} at tick {t}; edge decreases {dec}; {time.time()-t0:.0f} s")
if TAU is not None: tau[m_prev:K] = t; np.save(TAU, tau); print(f"settling ticks saved ({K} wheels)")
print("window(wheels)      ticks    p=D/T   q=B/W   S=A/D   identity   E[jump]  P(1)   P(2)   P(3)   pb1    pb4    pb5    H0 HT")
def report(name, w):
    Wst = w.T - w.D; q = w.B / Wst; S = w.A / w.D; p = w.D / w.T
    ident = (q - (w.HT - w.H0) / w.T) / (q + S)
    tot = sum(w.jumps.values()); mean = sum(j * v for j, v in w.jumps.items()) / tot
    jl = {j: w.jumps[j] / tot for j in (1, 2, 3)}
    pb = {j: (w.pbj[j] / w.jumps[j] if w.jumps[j] else float('nan')) for j in (1, 4, 5)}
    print(f"{name:16s} {w.T:9d}  {p:.4f}  {q:.4f}  {S:.4f}  {ident:.6f}  {mean:.4f}  {jl[1]:.3f}  {jl[2]:.3f}  {jl[3]:.3f}  {pb[1]:.3f}  {pb[4]:.3f}  {pb[5]:.3f}  {w.H0}  {w.HT}   exact: {abs(ident - p) < 1e-12}")
for k in sorted(wins): report(f"{k*WIDTH}-{min((k+1)*WIDTH, K)-1}", wins[k])
report("all", allw)
import math
print(f"the hazard past wheel {LATE}: stall ticks {sum(st.values())}, blacks {sum(bk.values())}, q = {sum(bk.values())/sum(st.values()):.4f}")
print("  h(1) by the preceding jump d: " + ", ".join(f"{d}: {bk1[d]/st1[d]:.4f} ({st1[d]})" for d in sorted(st1)))
hn = {}
for n in range(1, 13):
    S_ = sum(v for (nn, _), v in st.items() if nn == n); B_ = sum(v for (nn, _), v in bk.items() if nn == n)
    if S_: hn[n] = (B_ / S_, S_)
print("  h(n) by stall length (ticks): " + ", ".join(f"{n}: {h:.4f} ({c})" for n, (h, c) in hn.items()))
qphi = []
for phi in range(P):
    S_ = sum(v for (nn, pp), v in st.items() if pp == phi and nn >= 2); B_ = sum(v for (nn, pp), v in bk.items() if pp == phi and nn >= 2)
    qphi.append((B_ / S_, S_))
mean_q = sum(b * c for b, c in qphi) / sum(c for _, c in qphi); sd = (sum((b - mean_q) ** 2 for b, _ in qphi) / (P - 1)) ** 0.5
binom = (sum(math.sqrt(mean_q * (1 - mean_q) / c) ** 2 for _, c in qphi) / P) ** 0.5
print(f"  q by phase (n >= 2): mean {mean_q:.4f}, sd over the 32 phases {sd:.4f}, binomial sd per phase {binom:.4f}, ratio {sd/binom:.2f}; "
      f"phases above {mean_q+0.01:.3f} or below {mean_q-0.01:.3f}: {[phi for phi, (b, _) in enumerate(qphi) if abs(b - mean_q) > 0.01]}")
print("  q(phi): " + " ".join(f"{b:.3f}" for b, _ in qphi))
# the strip's own law per phase, unconditional on the edge: P(C_(j-3) xor C_(j-2) = 1 | C_(j-1) = 0) over wheels >= LATE
import numpy as np
def bits(row): return np.unpackbits(np.frombuffer(row.to_bytes((K + 7) // 8, 'little'), dtype=np.uint8), bitorder='little')[:K].astype(np.int64)
u = []
for phi in range(P):
    b = bits(cyc[phi])[LATE:]; w = (b[2:] == 0); xr = b[:-2] ^ b[1:-1]; u.append(float(xr[w].mean()))
print("  the strip's own u(phi) = P(xor below a white bit) per phase, wheels >= LATE: " + " ".join(f"{v:.3f}" for v in u))
print(f"  selection by phase, q(phi) - u(phi): sd over phases {np.std([b - v for (b, _), v in zip(qphi, u)], ddof=1):.4f}; mean {np.mean([b - v for (b, _), v in zip(qphi, u)]):.4f}")
