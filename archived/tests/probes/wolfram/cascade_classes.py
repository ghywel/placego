#!/usr/bin/env python3
"""cascade_classes.py TABLE NROWS: settling-phase classes just before the branch wheel 53,208 (round 14, sixth block; Cloud, CL696).
Cycles to wheel 53,300 by F from the certificate table (no white wheel between 12,000 and 53,207); NROWS random wide rows (40..64
bits) plus the single seed, strips of 53,300 wheels to T = 77,300; the clock shift from wheels 53,000..53,031; settling times of
wheels 52,900..53,210 by a backward scan from T; the number of distinct settling-phase classes among the rows at each wheel.
Prediction (tracker): the class count drops to 1 at some wheel between 52,900 and 53,206 and stays 1 through 53,210."""
import sys, numpy as np
table, NR = sys.argv[1], int(sys.argv[2])
C = [tuple(int(ch) for ch in l.strip()) for l in open(table) if l and not l.startswith('#')]
def F(u, w):
    p = 16
    if not any(u):   # white parent: the seed's branch at 53,207 is the integral from 0 (crystal_orbit.py, seed.0 -> 58,286)
        d = [0] * p
        for r in range(p - 1): d[r + 1] = d[r] ^ w[r]
        return tuple(d)
    r0 = u.index(1); d = [None] * p; d[(r0 + 1) % p] = 1 - w[r0]; r = (r0 + 1) % p
    for _ in range(2 * p):
        nr = (r + 1) % p; d[nr] = w[r] ^ (u[r] | d[r]); r = nr
    return tuple(d)
while len(C) < 53300: C.append(F(C[-1], C[-2]))
assert all(any(C[k]) for k in range(12000, 53207)) and not any(C[53207]), "unexpected white wheel"; assert all(any(C[k]) for k in range(53208, 53300))
K0, K1 = 52900, 53211; KB = 53300; T = int(1.45 * 53300) + 64; T0 = 69000; MASK = (1 << KB) - 1   # T0 below every settling time (tau ~ 1.33 k ~ 70,900; G25)
def stp(V): return ((V << 2) ^ ((V << 1) | V)) & MASK
def run(seed):
    V = seed
    for t in range(T0): V = stp(V)
    rows = []
    for t in range(T0, T + 1): rows.append(V); V = stp(V)
    def bit(i, k): return (rows[i] >> k) & 1
    cands = [j for j in range(16) if all(bit(i, k) == C[k][(T0 + i - j) % 16] for k in range(53000, 53032) for i in range(len(rows) - 64, len(rows)))]
    if len(cands) != 1: return None
    j = cands[0]
    tau = {}
    for k in range(K0, K1):
        last = None
        for i in range(len(rows) - 1, -1, -1):
            if bit(i, k) != C[k][(T0 + i - j) % 16]: last = i; break
        assert last is not None and last < len(rows) - 100, f'settling of wheel {k} not inside the window (G25)'
        tau[k] = T0 + last + 1
    return j, tau
res = run(1); j0, tau0 = res
rng = np.random.default_rng(909); PH = [np.array([(tau0[k] - j0) % 16 for k in range(K0, K1)])]; n_ok = 0
for n in range(NR):
    wb = int(rng.integers(40, 65)); seed = ((int(rng.integers(0, 1 << 32)) << 32) | int(rng.integers(0, 1 << 32))) & ((1 << wb) - 1) | 1
    r = run(seed)
    if r is None: print(f"row 0x{seed:x}: ambiguous clock; skipped"); continue
    j, tau = r; PH.append(np.array([(tau[k] - j) % 16 for k in range(K0, K1)])); n_ok += 1
    print(f"row 0x{seed:x} ({wb} bits): shift {j}; disagreements with the seed over wheels {K0}..{K1-1}: {int((PH[-1] != PH[0]).sum())}", flush=True)
PHa = np.array(PH); ncls = np.array([len(set(PHa[:, i].tolist())) for i in range(K1 - K0)])
ks = np.arange(K0, K1)
print(f"{n_ok + 1} rows: distinct phase classes per wheel over {K0}..{K1-1}: max {int(ncls.max())}; wheels with one class {int((ncls == 1).sum())} of {K1 - K0}")
multi = ks[ncls > 1]
print(f"  last wheel with more than one class: {int(multi.max()) if len(multi) else None}; wheels 53200..53210 classes: {ncls[53200 - K0:].tolist()}")
print(f"  class counts by wheel (every 10th from {K0}): {ncls[::10].tolist()}")
print("CASCADE_CLASSES_DONE")
