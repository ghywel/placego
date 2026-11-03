#!/usr/bin/env python3
"""cascade_sync.py TABLE K NROWS: does the settling cascade synchronise across rows? (round 14, sixth block; Cloud, CL696.) For the
single seed and NROWS random left-finite rows (random odd seeds of random width 1..64 bits), run the strip of K+64 wheels to
T = 1.45 K + 64, read the cycles from the table (universal up to the row's clock shift j, found by matching wheel 3's alternating
phase and checked on wheels 100..115), compute every wheel's settling time by the backward scan, and compare the settling phases
(tau_k - j) mod 16 with the single seed's. Reports each row's synchronisation wheel (first k from which all later phases agree),
any later disagreement, and along the single seed the frequency of the two sub-cases (parent's last defect a black or a missing
black). Predictions in the tracker."""
import sys, numpy as np, collections
table, K, NR = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
C = [tuple(int(ch) for ch in l.strip()) for l in open(table) if l and not l.startswith('#')]
assert len(C) >= K + 64
KB = K + 64; T = int(1.45 * K) + 64; MASK = (1 << KB) - 1
def stp(V): return ((V << 2) ^ ((V << 1) | V)) & MASK
def run(seed):
    rows = []; V = seed
    for t in range(T + 1): rows.append(V); V = stp(V)
    # clock shift j: wheel 3 alternates (period 2) from t >= 2; find j with C_3 shifted matching; refine with wheels 100..115 (period 16)
    def bit(t, k): return (rows[t] >> k) & 1
    cands = [j for j in range(16) if all(bit(t, k) == C[k][(t - j) % 16] for k in range(400, 432) for t in range(T - 64, T))]
    if len(cands) != 1: return None, cands
    j = cands[0]
    cyc_rows = [sum(C[k][(r - j) % 16] << k for k in range(KB)) for r in range(16)]
    tau = np.full(KB, -1, dtype=np.int64); unseen = (1 << KB) - 1
    for t in range(T, -1, -1):
        mism = (rows[t] ^ cyc_rows[t % 16]) & unseen
        while mism:
            low = mism & -mism; k = low.bit_length() - 1; tau[k] = t + 1; unseen &= ~low; mism &= ~low
        if not unseen: break
    tau[tau < 0] = 0
    return (j, tau, rows), cands
res0, _ = run(1); j0, tau0, rows0 = res0
ph0 = (tau0 - j0) % 16
rng = np.random.default_rng(606); syncs = []; desync = []; PH = []; VIOL = []; WIDTHS = []
for n in range(NR):
    wb = int(rng.integers(1, 65)); seed = ((int(rng.integers(0, 1 << 32)) << 32) | int(rng.integers(0, 1 << 32))) & ((1 << wb) - 1) | 1; WIDTHS.append(wb)
    res, cands = run(seed)
    if res is None: print(f"row 0x{seed:x} ({wb} bits): clock shift ambiguous {cands}; skipped"); continue
    j, tau, _ = res; ph = (tau - j) % 16; PH.append(ph[:K])
    # consistency: tau_k <= 1 + first black of C_(k-1) at/after max(tau_(k-1), tau_(k-2)) for all k in [400, K); count violations
    viol = 0
    for k in range(400, K):
        t0 = max(int(tau[k - 1]), int(tau[k - 2])); u = C[k - 1]
        if not any(u): continue
        t = t0
        while u[(t - j) % 16] == 0: t += 1
        if tau[k] > t + 1: viol += 1
    VIOL.append(viol)
    agree = (ph[:K] == ph0[:K])
    # synchronisation wheel: first k such that agree[k:] all True
    ks = np.flatnonzero(~agree); ksync = int(ks.max()) + 1 if len(ks) else 0
    syncs.append(ksync)
    # later disagreement after first agreement run of >= 50 wheels
    first_run = None
    for k in range(K):
        if agree[k:k + 50].all(): first_run = k; break
    later = [int(k) for k in ks if first_run is not None and k > first_run + 50]
    if later: desync.append((seed, wb, first_run, later[:5]))
    print(f"row 0x{seed:x} ({wb:2d} bits): shift {j:2d}; synchronisation wheel {ksync:5d}; disagreements after the first 50-wheel agreement: {len(later)}", flush=True)
PHa = np.array(PH); dis = (PHa != ph0[:K][None, :])
per_wheel = dis.sum(axis=0); free = np.flatnonzero(per_wheel > 0)
print(f"per-wheel: wheels (of {K}) where at least one row's settling phase differs from the seed's: {len(free)}; where at least half differ: {int((per_wheel >= len(PH)/2).sum())}")
runs = []; k = 0
while k < K:
    if per_wheel[k] > 0:
        k2 = k
        while k2 < K and per_wheel[k2] > 0: k2 += 1
        runs.append(k2 - k); k = k2
    else: k += 1
print(f"  disagreement runs (consecutive free wheels): {len(runs)} runs, lengths {collections.Counter(runs).most_common(8)}")
ncls = np.array([len(set(PHa[:, k].tolist() + [int(ph0[k])])) for k in range(K)])
print(f"  distinct settling-phase classes among the rows per wheel: max {int(ncls.max())}, mean {ncls.mean():.2f}; wheels with one class: {int((ncls == 1).sum())} of {K}; last wheel with more than one class below K: {int(np.flatnonzero(ncls > 1).max())}")
print(f"  first 40 free wheels: {free[:40].tolist()}")
print(f"  distinct phase values at the free wheels (rows + seed): " + ", ".join(f"{int(k)}:{sorted(set(PHa[:, k].tolist() + [int(ph0[k])]))}" for k in free[:12]))
# the sub-case at free wheels along the single seed: parent's last defect a black or a missing black, and does the parent's defect window hold a black
def subcase(k):
    t = int(tau0[k - 1]) - 1
    if t < 0: return 'n/a'
    return 'black' if C[k - 1][(t - j0) % 16] == 0 else 'missing'
fr = collections.Counter(subcase(int(k)) for k in free if k >= 100); al = collections.Counter(subcase(k) for k in range(100, K))
print(f"  sub-case of the parent's last defect at free wheels >= 100: {dict(fr)}; at all wheels: {dict(al)}")
# does the partition of rows by settling phase ever split? (two rows equal at k, different at k+1); merges; the profile of distinct phases
splits = merges = 0; split_wheels = []
for k in range(400, K - 1):
    a = PHa[:, k]; b = PHa[:, k + 1]
    for v in set(a.tolist()):
        idx = np.flatnonzero(a == v)
        if len(set(b[idx].tolist())) > 1: splits += 1; split_wheels.append(k + 1)
    merges += len(set(a.tolist())) - len(set(b.tolist())) if len(set(a.tolist())) > len(set(b.tolist())) else 0
print(f"partition events over wheels 400..{K-1} (60 rows): splits {splits} (at wheels {split_wheels[:12]}...), net merges {merges}; distinct phases every 200 wheels from 400: {[int(len(set(PHa[:, k].tolist()))) for k in range(400, K, 200)]}")
# the two classes: at the first free wheels >= 400, the phase values with counts, and the offset between the classes
fw = [int(k) for k in free if k >= 400][:12]
print("free wheels >= 400, phase values with row counts (seed's phase first): " + "; ".join(f"{k}: seed {int(ph0[k])}, rows {dict(collections.Counter(PHa[:, k].tolist()))}" for k in fw))
# around the synchronising wheel: cycle weights and the first-black structure of wheels 3490..3500
print("cycle weights (blacks per 16) of wheels 3488..3500: " + " ".join(f"{k}:{sum(C[k])}" for k in range(3488, 3501)))
if len(sys.argv) > 4: np.save(sys.argv[4], PHa)   # optional dump of the phase table
print(f"cascade-formula violations (tau later than the formula) per row: max {max(VIOL)}, total {sum(VIOL)}")
print("width and disagreement count per row: " + " ".join(f"{w}:{int((PHa[i] != ph0[:K]).sum())}" for i, w in enumerate(WIDTHS)))
print(f"synchronisation wheels over {len(syncs)} rows: max {max(syncs)}, median {int(np.median(syncs))}, all <= 100: {all(s <= 100 for s in syncs)}; rows that desynchronise later: {len(desync)} {desync[:3]}")
# sub-cases along the single seed: is the parent's last defect tick a black (C_(k-1)(tau_(k-1)-1) = 0) or a missing black?
blk = miss = 0
for k in range(100, K):
    t = int(tau0[k - 1]) - 1
    if t < 0: continue
    if C[k - 1][(t - j0) % 16] == 0: blk += 1
    else: miss += 1
print(f"single seed, wheels 100..{K-1}: parent's last defect a black (universal reset) {blk}, a missing black {miss}")
print("CASCADE_SYNC_DONE")
