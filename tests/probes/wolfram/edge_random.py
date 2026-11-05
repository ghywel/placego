"""edge_random.py: the error edge over a random background, and Rule 30's left damage front (CL741 addendum 2).
(i) The error process over a random background. Not in the wall frame: there the implicit zeros below wheel 0 give every
row a left side (the universal strip), so the background near the edge is never random and an error at wheel 0 never
heals (the first design, killed). In the standard frame instead: a random row a of N cells and b = a with random damage on
the cells from the centre up; the leftmost damaged cell x_L, the wall-frame edge m = x_L + t; every tick the parent's bit
(the cell below x_L),
the parent's bit, the jump at a death, the error density at offsets 1..4, and the strip's bit three above the edge in the
state (window C[m-2..m+2] = 01101, lowest wheel first, both errors set), whose density was 0.989 on the actual strip.
(ii) The standard frame: two random rows of N cells differing in one cell, the leftmost differing cell after T steps,
lambda_L = its mean leftward motion per step (NKS p. 949: about 0.2428). Predictions P-G1 .. P-G3 in CL741 addendum 2.
Usage: python3 edge_random.py [K] [NSEEDS] [N] [T] [NRUNS_ii] [ring] [SEED0]   defaults 400000 3 524288 200000 NSEEDS+1 (K unused now)
(CL741: N = 2^20, T = 300,000, three backgrounds for (i); part (ii) separately with four runs at N = 2^19, T = 200,000.
CL742: 'ring', N = 2^21, T = 900,000, nine backgrounds in three processes with SEED0 = 10, 20, 30; also the hazard after a
stay, P(parent black | jump) and S4's formula for P(heal), per run.)"""
import sys, time, collections, random
K = int(sys.argv[1]) if len(sys.argv) > 1 else 400000
NS = int(sys.argv[2]) if len(sys.argv) > 2 else 3
N = int(sys.argv[3]) if len(sys.argv) > 3 else 1 << 19
T = int(sys.argv[4]) if len(sys.argv) > 4 else 200000
NL = int(sys.argv[5]) if len(sys.argv) > 5 else NS + 1     # runs of part (ii)
RING = len(sys.argv) > 6 and sys.argv[6] == 'ring'           # part (i) on a ring of N cells (no boundary cone; the damage must not wrap)
S0 = int(sys.argv[7]) if len(sys.argv) > 7 else 0            # seed offset for part (i)
import functools; print = functools.partial(print, flush=True)
def lowbit(x, K): return (x & -x).bit_length() - 1 if x else K
print("(i) the error edge over a random background: standard frame, the damage half-infinite to the right of the centre; wheel = cell + tick")
speeds = []
for seed in range(S0 + 1, S0 + NS + 1):
    rng = random.Random(seed); MASK = (1 << N) - 1; x0 = N // 2
    if RING:
        def step(v): return ((((v << 1) | (v >> (N - 1))) & MASK) ^ (v | ((v >> 1) | ((v & 1) << (N - 1)))))
    else:
        def step(v): return ((v << 1) ^ (v | (v >> 1))) & MASK
    a = rng.getrandbits(N); b = a ^ ((rng.getrandbits(N) | 1) << x0)      # the damage: random above the centre, the centre damaged
    t0 = time.time(); pblack = 0; nwin = 0; jumps = collections.Counter(); dens = [0] * 5; m_prev = None; pb_prev = 0
    special = [0, 0]; dec = 0; xL0 = x0; after_stay = [0, 0]; after_jump = collections.defaultdict(lambda: [0, 0])
    for t in range(T):
        d = a ^ b; xL = lowbit(d, N)
        if RING:
            if xL < 8 or d.bit_length() > N - 8: raise RuntimeError("the damage wrapped round the ring")
        elif xL < t + 8: raise RuntimeError("the damage reached the boundary's cone")   # cell 0's influence reaches cell t at tick t
        m = xL + t                                             # the wall-frame edge
        if m_prev is not None and m < m_prev: dec += 1
        nwin += 1; pb = (a >> (xL - 1)) & 1; pblack += pb              # the parent: the cell below the edge (undamaged, so a = b there)
        w = (d >> (xL + 1)) & 15
        for k in range(1, 5): dens[k] += (w >> (k - 1)) & 1
        if (w & 3) == 3 and ((a >> (xL - 2)) & 31) == 0b10110: special[(a >> (xL + 3)) & 1] += 1
        if m_prev is not None:
            if pb_prev: jumps[m - m_prev] += 1; after_jump[m - m_prev][pb] += 1
            else: after_stay[pb] += 1
        pb_prev = pb; m_prev = m
        a = step(a); b = step(b)
    xL = lowbit(a ^ b, N); lam = (x0 - xL) / T
    tot = sum(jumps.values()); mean = sum(j * v for j, v in jumps.items()) / tot; dr = pblack / nwin
    jl = {j: round(v / tot, 4) for j, v in sorted(jumps.items()) if j <= 7}
    speeds.append(1 - lam)
    q = after_stay[1] / sum(after_stay); pbd = {j: after_jump[j][1] / sum(after_jump[j]) for j in sorted(after_jump) if sum(after_jump[j]) > 0}
    S = sum(v / tot * (1 - pbd[j]) for j, v in jumps.items()); formula = 1 / (1 + S / q)
    print(f"  seed {seed}: N={N}, T={T}: lambda_L {lam:.4f}, wall-frame speed {1-lam:.4f}; edge decreases {dec}; "
          f"P(heal) {dr:.4f}; jump law {jl}; mean {mean:.4f}; product {dr*mean:.4f}; error density at offsets 1..4 "
          f"{[round(dens[k]/nwin, 4) for k in range(1, 5)]}; P-G3 state: C_(m+3)=1 on {special[1]} of {sum(special)} visits "
          f"({special[1]/max(1,sum(special)):.3f}); hazard after a stay q {q:.4f}; P(parent black | jump d) {{{', '.join(f'{j}: {pbd[j]:.3f}' for j in pbd if j <= 6)}}}; "
          f"S4's formula 1/(1 + S/q) with S {S:.4f}: {formula:.4f}; {time.time()-t0:.0f} s")
import statistics
if speeds: print(f"  speed over {NS} backgrounds: mean {statistics.mean(speeds):.4f}" + (f", sd {statistics.stdev(speeds):.4f}" if NS > 1 else ""))
print("(ii) the left damage front, standard frame: two random rows differing in one cell")
lams = []
for seed in range(1, NL + 1):
    rng = random.Random(100 + seed); MASK = (1 << N) - 1
    def step(v): return ((v << 1) ^ (v | (v >> 1))) & MASK
    a = rng.getrandbits(N); b = a ^ (1 << (N // 2)); x0 = N // 2; t0 = time.time()
    for _ in range(T): a = step(a); b = step(b)
    xL = lowbit(a ^ b, N); lam = (x0 - xL) / T; lams.append(lam)
    print(f"  seed {seed}: N={N}, T={T}: left edge moved {x0 - xL} cells: lambda_L = {lam:.4f}; {time.time()-t0:.0f} s")
if lams: print(f"  lambda_L over {len(lams)} runs: mean {statistics.mean(lams):.4f}" + (f", sd {statistics.stdev(lams):.4f}" if len(lams) > 1 else "") + f"; 1 - lambda_L = {1-statistics.mean(lams):.4f}")
