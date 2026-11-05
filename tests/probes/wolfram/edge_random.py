"""edge_random.py: the error edge over a random background, and Rule 30's left damage front (CL741 addendum 2).
(i) The wall-frame error process of error_process.py with the strip replaced by a uniformly random row C (evolved by the
same step; the actual row a = C XOR e with e random above wheel 0): every tick the edge m (the lowest erroneous wheel),
the parent's bit, the jump at a death, the error density at offsets 1..4, and the strip's bit three above the edge in the
state (window C[m-2..m+2] = 01101, lowest wheel first, both errors set), whose density was 0.989 on the actual strip.
(ii) The standard frame: two random rows of N cells differing in one cell, the leftmost differing cell after T steps,
lambda_L = its mean leftward motion per step (NKS p. 949: about 0.2428). Predictions P-G1 .. P-G3 in CL741 addendum 2.
Usage: python3 edge_random.py [K] [NSEEDS] [N] [T] [NRUNS_ii]   defaults 400000 3 524288 200000 NSEEDS+1
(run here as K = 300,000 with three backgrounds, and part (ii) separately with four runs)"""
import sys, time, collections, random
K = int(sys.argv[1]) if len(sys.argv) > 1 else 400000
NS = int(sys.argv[2]) if len(sys.argv) > 2 else 3
N = int(sys.argv[3]) if len(sys.argv) > 3 else 1 << 19
T = int(sys.argv[4]) if len(sys.argv) > 4 else 200000
NL = int(sys.argv[5]) if len(sys.argv) > 5 else NS + 1     # runs of part (ii)
import functools; print = functools.partial(print, flush=True)
def lowbit(x, K): return (x & -x).bit_length() - 1 if x else K
print("(i) the error edge over a random background, wall frame")
speeds = []
for seed in range(1, NS + 1):
    rng = random.Random(seed); MASK = (1 << K) - 1
    def step(v): return ((v << 2) ^ ((v << 1) | v)) & MASK
    C = rng.getrandbits(K); e = rng.getrandbits(K) | 1; a = C ^ e
    t0 = time.time(); t = 0; pblack = 0; nwin = 0; jumps = collections.Counter(); dens = [0] * 5; m_prev = None
    special = [0, 0]; dec = 0
    while True:
        e = a ^ C; m = lowbit(e, K)
        if m >= K: break
        if m_prev is not None and m < m_prev: dec += 1
        if m >= 2:
            nwin += 1; pb = (C >> (m - 1)) & 1; pblack += pb
            w = (e >> (m + 1)) & 15
            for d in range(1, 5): dens[d] += (w >> (d - 1)) & 1
            if (w & 3) == 3 and ((C >> (m - 2)) & 31) == 0b10110:     # window 01101 lowest wheel first = bits 0..4 = 0,1,1,0,1
                special[(C >> (m + 3)) & 1] += 1
            if m_prev is not None and pb_prev: jumps[m - m_prev] += 1
            pb_prev = pb
        else: pb_prev = 0
        m_prev = m; a = step(a); C = step(C); t += 1
    tot = sum(jumps.values()); mean = sum(j * v for j, v in jumps.items()) / tot; dr = pblack / nwin
    jl = {j: round(v / tot, 4) for j, v in sorted(jumps.items()) if j <= 7}
    speeds.append((K - 1) / t)
    print(f"  seed {seed}: K={K} settled at tick {t}: speed {(K-1)/t:.4f} (leftward {1-(K-1)/t:.4f} cells/step); edge decreases {dec}; "
          f"death rate {dr:.4f}; jump law {jl}; mean {mean:.4f}; product {dr*mean:.4f}; error density at offsets 1..4 "
          f"{[round(dens[d]/nwin, 4) for d in range(1, 5)]}; P-G3 state: C_(m+3)=1 on {special[1]} of {sum(special)} visits "
          f"({special[1]/max(1,sum(special)):.3f}); {time.time()-t0:.0f} s")
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
