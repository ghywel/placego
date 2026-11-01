#!/usr/bin/env python3
"""bg_fronts.py BACKGROUND EXACT_M_LIST: inserted-edge fronts per alignment with periodicity detection (T=120, J=400), and the
patched-witness family (inserted edge with depths 1..8 free): arrival times vs the exact M(k)."""
import sys, numpy as np
name = sys.argv[1]; exact = [int(x) for x in sys.argv[2].split(',')]
STATE0 = {'c7_28': '1000000', 's7_63': '1010000', 's9_57': '100100000', 's12_68': '100100000000', 'e4_8': '1000'}[name]
p = len(STATE0); s0 = tuple(int(c) for c in STATE0)
def ring_step(s): return tuple(s[j] ^ (s[(j-1) % p] | s[(j-2) % p]) for j in range(p))
orbit = [s0]; cur = ring_step(s0)
while cur != s0: orbit.append(cur); cur = ring_step(cur)
q = len(orbit)
T, J, PB = 120, 400, 8
def run_family(r, s):
    """columns = 2^PB patches of depths 1..PB; rows = depths 0..J; returns fronts R[t, patch]."""
    n = 1 << PB; idx = np.arange(n, dtype=np.int64)
    X = np.zeros((J+1, n), dtype=np.uint8); X[0] = 1
    st = orbit[s % q]
    for j in range(1, J+1): X[j] = st[(j+r) % p]
    for j in range(1, PB+1): X[j] = (idx >> (j-1)) & 1
    ins = sum(st[(j+r) % p] << (j-1) for j in range(1, PB+1))   # the pure inserted-edge patch index
    R = np.full((T+1, n), -1, dtype=np.int64)
    for t in range(T+1):
        E = np.array([orbit[(t+s) % q][(j+r) % p] for j in range(J+1)], dtype=np.uint8)
        Dm = (X ^ E[:, None])
        lim = J+1-2*t
        if lim <= 0: break
        Dm = Dm[:lim]
        any_ = Dm.any(axis=0)
        last = lim - 1 - np.argmax(Dm[::-1], axis=0)
        R[t] = np.where(any_, last, -1)
        Y = X.copy(); Y[1] = X[1] ^ X[0]; Y[2:] = X[2:] ^ (X[1:-1] | X[:-2]); X = Y
    return R, ins
def period_of(seq):
    for per in range(1, 60):
        if all(seq[i] == seq[i+per] for i in range(len(seq)-per)): return per
    return None
speeds = {}; best_arr = {}
for r in range(p):
    for s in range(q):
        R, ins = run_family(r, s)
        inc = np.diff(R[:, ins])[60:118]
        per = period_of(list(inc))
        mean = inc.mean()
        speeds[(r, s)] = (round(float(mean), 3), per, list(np.diff(R[:, ins])[60:60+(per or 24)]))
        # arrival times for every patch: first t with R >= k
        for k in range(1, len(exact)+1):
            arr = np.array([next((t for t in range(T+1) if R[t, c] >= k), 10**6) for c in range(R.shape[1])])
            best_arr[k] = max(best_arr.get(k, 0), int(arr.max()))
print(f"{name}: p={p} q={q}; inserted-edge front mean speed over t=60..118 by alignment: distinct {sorted(set(v[0] for v in speeds.values()))}")
from collections import Counter
print("  increment-pattern periods found:", Counter(v[1] for v in speeds.values()))
ex = [(k, v) for k, v in speeds.items()][:3]
for k, v in ex: print(f"  alignment {k}: speed {v[0]}, period {v[1]}, one period of increments {v[2]}")
print("  patched-witness family (depths 1..8 free) arrival time vs exact M(k):")
print("   k      :", ' '.join(f"{k:3d}" for k in range(1, len(exact)+1)))
print("   family :", ' '.join(f"{best_arr[k]:3d}" for k in range(1, len(exact)+1)))
print("   exact  :", ' '.join(f"{m:3d}" for m in exact))
print("   equal  :", all(best_arr[k] == exact[k-1] for k in range(1, len(exact)+1)))
print("BG_FRONTS_DONE")
