#!/usr/bin/env python3
"""diag_certificate.py NAME T: for every alignment of a ring background with a black edge inserted (lab x < 0 ether, x = 0 black,
x > 0 white), the lab front x_min(t) and its eventual law k_min(t+P) = k_min(t) + S (k = x + t), then a three-valued diagonal-band
certificate: the band [k_min, k_min + w] evolves by D_k' = D_(k-2) XOR (D_(k-1) OR D_k) reading the ether below and 'unknown' above;
PASS when after P ticks the shifted band is fully determined, equal to the original, and k_min rose by S, with the ether invariant
under (x -> x + S - P, t -> t + P). Then the law holds for ever (induction). Cloud, Block 23."""
import sys, numpy as np
from collections import Counter
name, T = sys.argv[1], int(sys.argv[2])
WORDS = {'c7_28': '1000000', 'G8': '1000', 's9_57': '100100000', 's7_63': '1010000', 's12_68': '100100000000'}
y = np.array([int(c) for c in WORDS[name]], dtype=np.uint8); N = len(y)
def cst(s): return s ^ (np.roll(s, 1) | np.roll(s, 2))
orb = [y.copy()]; cur = cst(y)
while not np.array_equal(cur, y): orb.append(cur.copy()); cur = cst(cur)
orb = np.array(orb); q = len(orb)
def E(x, t, r, s): return int(orb[(t + s) % q][((t - x) + r) % N])   # lab cell (x, t): frame depth t - x, frame time t
def step(rw):
    n = np.zeros_like(rw); n[1:-1] = rw[:-2] ^ (rw[1:-1] | rw[2:]); return n
WL = 2*T + 100; WR = T + 60; W = WL + WR
U = 2  # unknown
def xor3(a, b): return U if (a == U or b == U) else a ^ b
def or3(a, b):
    if a == 1 or b == 1: return 1
    if a == 0 and b == 0: return 0
    return U
def certify(r, s, t0, kmin0, band0, P, S, w):
    """band0: dict k -> value on [kmin0, kmin0 + w] at time t0 (known). Returns (pass, reason)."""
    # ether invariance under (x -> x + S - P, t -> t + P)
    for x in range(-2*N, 2*N):
        for t in range(2*q):
            if E(x + S - P, t + P, r, s) != E(x, t, r, s): return False, "ether not invariant"
    band = dict(band0); top = kmin0 + w
    for t in range(t0, t0 + P):
        new = {}
        for k in range(kmin0, top + 1):
            a = band.get(k - 2, None); b = band.get(k - 1, None); c = band[k]
            if a is None: a = E(k - 2 - t, t, r, s)
            if b is None: b = E(k - 1 - t, t, r, s)
            new[k] = xor3(a, or3(b, c))
        band = new
    # the shifted band must be determined, equal to the original, and the lowest damage at kmin0 + S
    for k in range(kmin0, kmin0 + S):
        if band[k] == U or band[k] != E(k - (t0 + P), t0 + P, r, s): return False, f"diagonal {k} below the shifted band is {'unknown' if band[k]==U else 'damaged'} at t0+P"
    for k in range(kmin0 + S, top + 1):
        if band[k] == U: return False, f"diagonal {k} unknown after P ticks"
        if band[k] != band0[k - S]: return False, f"diagonal {k} differs from the original band"
    if band[kmin0 + S] == E(kmin0 + S - (t0 + P), t0 + P, r, s): return False, "front did not land on the shifted bottom"
    return True, "ok"
results = Counter(); laws = Counter(); details = []
for r in range(N):
    for s in range(q):
        bg = np.array([E(x, 0, r, s) for x in range(-WL, WR)], dtype=np.uint8); c = WL
        pert = bg.copy(); pert[c] = 1; pert[c+1:] = 0
        a, b = bg.copy(), pert.copy(); km = []; rowsP = {}
        for t in range(T + 1):
            d = np.flatnonzero(a ^ b); km.append(int(d.min()) - c + t)
            rowsP[t] = b.copy() if t >= T - 400 else None
            if t < T: a, b = step(a), step(b)
        km = np.array(km); inc = np.diff(km)
        law = None
        n = len(inc); span = 240
        for P in range(1, 65):
            seg = inc[n - span:]
            if all(np.array_equal(seg[i:i+P], seg[i+P:i+2*P]) for i in range(0, span - 2*P, P)):
                t0 = n - span
                while t0 > 0 and inc[t0-1] == inc[t0-1+P]: t0 -= 1
                law = (P, int(inc[t0:t0+P].sum()), t0); break
        if law is None: results['no law'] += 1; details.append((r, s, None)); continue
        P, S, onset = law; laws[(P, S)] += 1
        t0 = max(onset, T - 300); kmin0 = int(km[t0])
        verdict = None; why = ''
        for w in ():   # certification withdrawn: a one-period band check is not an induction (see PREDICTIONS Block 23)
            band0 = {k: int(rowsP[t0][c + (k - t0)]) for k in range(kmin0, kmin0 + w + 1)}
            ok, why = certify(r, s, t0, kmin0, band0, P, S, w)
            if ok: verdict = w; break
        results['law found'] += 1; details.append((r, s, (P, S), verdict, why if not verdict else ''))
print(f"{name}: N={N}, q={q}, alignments {N*q}, T={T}; eventual laws (P, S) with counts: {dict(laws)}")
print(f"  certificate results: {dict(results)}")
print("  lab speeds implied by the laws (P-S)/P:", sorted(set(round((P - S)/P, 4) for (P, S) in laws)))
fails = [d for d in details if d[2] is not None and d[3] is None]
print("  failures (first 8):", fails[:8])
print("  passes by width:", Counter(d[3] for d in details if d[2] is not None and d[3]))
print("DIAG_CERT_DONE")
