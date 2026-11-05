"""prefix_race.py: the prefix question as a race (CL750). A completion shares the seed's first P bits (bit 0 black, bits
1..P-1 white, as the single cell has them) and carries random bits above P. Its shared prefix with the seed is an error
edge against the seed (never retreats, heals at a black of the seed's wheel below). The branch law says it takes the
seed's branch at a fork j if the shared prefix covers wheel j at the seed's last black there (71,115 at 53,207; 77,909 at
58,286); otherwise its own last black decides. The seed and the completion are evolved together on 165,750 wheels; the
shared prefix is read at the two ticks and every 5,000 ticks; the completion is evolved to a multiple of 32 past the
settling bound and its strip identified among ROWSDIR/*.bin at every phase.
Usage: python3 prefix_race.py ROWSDIR P N RNGSEED"""
import sys, os, random, time
ROWS = sys.argv[1]; Pfx = int(sys.argv[2]); N = int(sys.argv[3]); RS = int(sys.argv[4])
K = 165750; MASK = (1 << K) - 1; P = 32; T0 = 350016; FORKS = {53207: 71115, 58286: 77909}; TICKS = {tk: j for j, tk in FORKS.items()}
def step(v): return ((v << 2) ^ ((v << 1) | v)) & MASK
def lowbit(x): return (x & -x).bit_length() - 1 if x else K
strips = {}
for f in sorted(os.listdir(ROWS)):
    if f.endswith('.bin'):
        r = int.from_bytes(open(f"{ROWS}/{f}", 'rb').read(), 'little') & MASK; c = [r]
        for _ in range(P - 1): c.append(step(c[-1]))
        strips[f[:-4]] = c
rng = random.Random(RS)
for n in range(N):
    t0 = time.time()
    y = ((rng.getrandbits(K) >> Pfx) << Pfx) | 1; x = 1; t = 0; at = {}; prof = []
    while t < T0:
        if t in TICKS or t % 5000 == 0:
            m = lowbit(x ^ y)
            if t in TICKS: at[t] = m
            if t % 5000 == 0: prof.append(m)
        x = step(x); y = step(y); t += 1
    found = None
    for name, cyc in strips.items():
        for ph in range(P):
            if y == cyc[ph]: found = (name, ph)
    covers = all(at[tk] > j for j, tk in FORKS.items())
    print(f"P={Pfx} completion {n}: shared prefix at 71115: {at[71115]} ({'covers' if at[71115] > 53207 else 'below'} 53207), at 77909: {at[77909]} "
          f"({'covers' if at[77909] > 58286 else 'below'} 58286); strip {found[0] if found else None} phase {found[1] if found else None}; "
          f"{'criterion: seed branch' if covers else 'criterion: free'}; {'ok' if (not covers) or (found and found[0] == 'A0') else 'VIOLATION'}; "
          f"prefix every 5000 ticks to 80000: {prof[:17]}; {time.time()-t0:.0f} s")
