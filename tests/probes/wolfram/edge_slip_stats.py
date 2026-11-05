"""edge_slip_stats.py: the clock offset between two walks over the same strip, wheel by wheel (CL746). Delta_j =
tau'_j - tau_j from two saved settling-tick arrays (edge_windows.py, TAU argument): the residues of Delta modulo the
strip's period 32 past wheel LO, the maximal runs of constant Delta, the locked stretches (runs of at least MINLOCK
wheels) with their offsets, and the excursions between them with their change in whole periods.
Usage: python3 edge_slip_stats.py TAU_A.npy TAU_B.npy [LO=200000] [MINLOCK=2000]"""
import sys, numpy as np, collections
a = np.load(sys.argv[1]); b = np.load(sys.argv[2]); LO = int(sys.argv[3]) if len(sys.argv) > 3 else 200000; MINLOCK = int(sys.argv[4]) if len(sys.argv) > 4 else 2000
K = len(a); d = b - a; P = 32
res = collections.Counter((d[LO:] % P).tolist()); top = max(res, key=res.get)
print(f"residues of Delta mod {P} over wheels >= {LO}: the residue {top} on {res[top]} of {K - LO} wheels ({res[top]/(K-LO):.4f}); the others {sum(v for r, v in res.items() if r != top)}")
runs = []; start = 0
for j in range(1, K):
    if d[j] != d[j - 1]: runs.append((start, j - 1, int(d[start]))); start = j
runs.append((start, K - 1, int(d[start])))
locked = [r for r in runs if r[1] - r[0] + 1 >= MINLOCK]
print(f"maximal constant-Delta runs: {len(runs)}; locked stretches (>= {MINLOCK} wheels): {len(locked)}; their residues mod {P}: {sorted(set(v % P for _, _, v in locked))}")
for s, e, v in locked: print(f"  locked wheels {s}-{e} ({e-s+1} wheels; ticks {a[s]}-{a[e]} on the first walk): Delta {v}")
print("excursions between locked stretches:")
for (s1, e1, v1), (s2, e2, v2) in zip(locked, locked[1:]):
    seg = d[e1 + 1:s2]
    print(f"  wheels {e1+1}-{s2-1} ({s2-e1-1} wheels, {a[s2]-a[e1]} ticks): Delta {v1} -> {v2} (change {v2-v1} = {(v2-v1)/P:+.2f} periods); range inside {seg.min()}..{seg.max()}")
