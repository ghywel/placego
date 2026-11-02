#!/usr/bin/env python3
"""ether_zero.py: the classic ether (7-ring '1000000', period 28 under the frame rule c). (1) c^8 against rotations and the lab period;
(2) exact fronts for all 196 alignments of the inserted edge (frame, trusted range) and their eventual laws; (3) the self-contained band
certificate at (8, 8) per alignment; (4) the lab picture of the interface for one alignment. Cloud, Block 23."""
import numpy as np, sys, subprocess
y = np.array([1,0,0,0,0,0,0], dtype=np.uint8); N = 7
def cst(s): return s ^ (np.roll(s, 1) | np.roll(s, 2))
orb = [y.copy()]; cur = cst(y)
while not np.array_equal(cur, y): orb.append(cur.copy()); cur = cst(cur)
orb = np.array(orb); q = len(orb)
rot = [r for r in range(N) if np.array_equal(orb[8 % q], np.roll(y, r))]
print(f"(1) ring period under c: {q}; c^8(y) = rho^r(y) for r in {rot}; c^4 rotation? {[r for r in range(N) if np.array_equal(orb[4], np.roll(y, r))]}")
# lab period: F = rho^-1 c ; F^p = id iff c^p = rho^p
lab = [p for p in range(1, 57) if np.array_equal(orb[p % q], np.roll(y, p % N))]
print(f"    lab periods p <= 56 with c^p = rho^p: {lab}")
# (2) fronts for all alignments
def fronts(r, s, T, J):
    X = np.zeros(J+1, dtype=np.uint8); X[0] = 1
    idx = (np.arange(J+1) + r) % N
    X[1:] = orb[s % q][idx[1:]]
    R = np.zeros(T+1, dtype=np.int64)
    for t in range(T+1):
        lim = J+1-2*t; E = orb[(t+s) % q][idx[:lim]]
        D = np.flatnonzero(X[:lim] ^ E); R[t] = D.max() if D.size else -1
        assert R[t] + 40 < lim
        Y = X.copy(); Y[1] = X[1] ^ X[0]; Y[2:] = X[2:] ^ (X[1:-1] | X[:-2]); X = Y
    return R
T, J = 1500, 5400
laws = {}; onsets = {}; patterns = {}
for r in range(N):
    for s in range(q):
        R = fronts(r, s, T, J); inc = np.diff(R)
        ok8 = np.array_equal(inc[8:], inc[:-8]) and inc[-8:].sum() == 8
        t0 = None
        if ok8:
            t0 = len(inc) - 8
            while t0 > 0 and inc[t0-1] == inc[t0-1+8]: t0 -= 1
        laws[(r, s)] = ok8; onsets[(r, s)] = t0; patterns[(r, s)] = tuple(int(v) for v in inc[-8:])
from collections import Counter
print(f"(2) alignments with the eventual law R(t+8) = R(t)+8 on [t0, {T}]: {sum(laws.values())} of {N*q}; max onset {max(v for v in onsets.values() if v is not None)}")
print("    increment patterns (one period, cyclic) and counts:", Counter(patterns.values()).most_common(8))
bad = [a for a, v in laws.items() if not v]
if bad: print("    alignments WITHOUT the law:", bad[:20])
# (3) the band certificate per alignment
res = Counter(); fails = []
for (r, s) in sorted(laws):
    t0 = max(onsets[(r, s)] or 0, 16) + 8
    passed = None
    for w in (8, 12, 16, 24):
        out = subprocess.run([sys.executable, 'background_certificate.py', 'c7_28', str(r), str(s), str(t0), str(w), '8', '8'], capture_output=True, text=True)
        if 'CERTIFICATE PASS' in out.stdout: passed = w; break
        if 'ValueError' in out.stderr or 'Error' in out.stderr: continue
    res[passed] += 1
    if passed is None: fails.append((r, s, t0))
print(f"(3) band certificate at (8, 8): passes by width {dict(res)}; failures {fails[:10]}")
# (4) lab picture for alignment (0, 0): rows t = 200..215, lab x from x_min-8 to x_min+12 (lab x = t - depth), with the ether's cells marked
r, s = 0, 0; R = fronts(r, s, 240, 1200)
print(f"(4) alignment (0,0): fronts R[200..216] = {R[200:217].tolist()}; lab x_min = t - R: {[int(t - R[t]) for t in range(200, 217)]}")
# rebuild the perturbed rows and print a window in the lab frame
X = np.zeros(1201, dtype=np.uint8); X[0] = 1; idx = (np.arange(1201) + r) % N; X[1:] = orb[s % q][idx[1:]]
rows = []
for t in range(241):
    rows.append(X.copy()); Y = X.copy(); Y[1] = X[1] ^ X[0]; Y[2:] = X[2:] ^ (X[1:-1] | X[:-2]); X = Y
xmin = int(min(t - R[t] for t in range(200, 217)))
print("    lab window: time down, x from", xmin - 6, "to", xmin + 14, "('.' = agrees with the ether, '#' = mismatch; cell colour second block)")
for t in range(200, 217):
    E = orb[(t + s) % q][idx]
    line = ''; col = ''
    for x in range(xmin - 6, xmin + 15):
        j = t - x
        if j < 0 or j > 1200: line += ' '; col += ' '; continue
        line += '#' if rows[t][j] != E[j] else '.'; col += '1' if rows[t][j] else '0'
    print(f"    t={t}: {line}   {col}")
print("ETHER_ZERO_DONE")
