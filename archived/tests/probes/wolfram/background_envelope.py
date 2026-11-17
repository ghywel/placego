#!/usr/bin/env python3
"""bg_envelope.py: three diagnostics on the (12, 68) front and the provable masking-envelope bound for all backgrounds (Cloud, Block 15).
Orientation: depth j reads j-1 and j-2 (shallower); the front R(t) is the deepest mismatch with the background E; cells deeper than R are E.
(A) backward dependency cone of the front; (B) forward window closure test; (C) band death at large widths; (D) envelope bound L_env(k)."""
import sys, numpy as np
from collections import Counter
STATE0 = {'c7_28': '1000000', 's7_63': '1010000', 's9_57': '100100000', 's12_68': '100100000000', 'e4_8': '1000'}
def background(name):
    s0 = tuple(int(c) for c in STATE0[name]); p = len(s0)
    def ring_step(st): return tuple(st[j] ^ (st[(j-1) % p] | st[(j-2) % p]) for j in range(p))
    orbit = [s0]; cur = ring_step(s0)
    while cur != s0: orbit.append(cur); cur = ring_step(cur)
    return p, len(orbit), orbit
def evolve(name, r, s, T, J):
    """rows X[t, j] for t <= T, j <= J (exact for j < J+1-2t), E[t, j], fronts R[t] on the trusted range."""
    p, q, orbit = background(name)
    X = np.zeros((T+1, J+1), dtype=np.uint8); E = np.zeros((T+1, J+1), dtype=np.uint8)
    for t in range(T+1):
        st = orbit[(t+s) % q]; E[t] = [st[(j+r) % p] for j in range(J+1)]
    X[0] = E[0]; X[0, 0] = 1
    for t in range(T):
        Y = X[t].copy(); Y[1] = X[t, 1] ^ X[t, 0]; Y[2:] = X[t, 2:] ^ (X[t, 1:-1] | X[t, :-2]); X[t+1] = Y
    R = np.full(T+1, -1, dtype=np.int64)
    for t in range(T+1):
        lim = J+1-2*t
        if lim <= 0: R = R[:t]; break
        Dm = np.flatnonzero(X[t, :lim] ^ E[t, :lim]); R[t] = Dm.max() if Dm.size else -1
    return X, E, R
name, r, s = 's12_68', 0, 51
T, J = 700, 2400
X, E, R = evolve(name, r, s, T, J)
D = X ^ E
assert len(R) == T+1 and all(R[t] + 40 < J+1-2*t for t in range(T+1)), "trusted range"
print(f"(A) backward dependency cone, {name} alignment ({r},{s}), fronts to T={T}: R(T)={R[T]}")
def needed_for_front(t):
    """cells at time t whose values decide R(t+1) given R(t) and E: the front's own reads through masking.
    D_{R+2}(t+1) needs nothing (it is NOT E_{R+1}); D_{R+1}(t+1) needs X_{R-1} only if E_{R+1}=1 and E_R=1 (else determined by E);
    if neither advance happens the new front is the deepest mismatch at t+1 among depths <= R, which needs the whole prefix in general,
    so we take the cells that decide D_j(t+1) for j in [R-2, R] (reads of j-1, j-2 with masking) and let the cone grow from there."""
    Rt = R[t]; need = set()
    if E[t, Rt+1] == 1:
        if E[t, Rt] == 1: need.add(Rt-1)
        # D_{R}(t+1) and D_{R-1}(t+1) are needed to locate the front when it does not advance
        if (E[t, Rt] == 1 and X[t, Rt-1] == 0) or E[t, Rt] == 0:  # no certain +1: the front may stay or retreat
            for j in range(Rt-1, Rt+1):
                need.add(j); need.add(j-1)
                if X[t, j-1] == 0: need.add(j-2)
    return need
def inputs(j, t):
    """cells at time t that determine X_j(t+1) through masking."""
    out = {j, j-1}
    if X[t, j-1] == 0: out.add(j-2)
    return out
S = set(needed_for_front(T-1))
dmax = []
for t in range(T-1, 144, -1):
    S = {j for j in S if j <= R[t]}  # cells deeper than the front are E, known
    S |= needed_for_front(t)
    if t % 34 == 0 or t == T-1:
        dmax.append((t, R[t] - min(S) if S else 0, len(S)))
    S = set().union(*(inputs(j, t-1) for j in S)) if S else set()
    S = {j for j in S if j >= 0}
print("  (t, depth of the cone below the front, cells):", dmax)
print("  cone depth at t=145:", R[145] - min(S) if S else 0, "| front R(145) =", R[145])
print(f"(B) forward window closure on t in [145, {T-1}]")
for W in (2, 4, 6, 8, 10, 12, 16, 20):
    seen = {}; conflicts = 0
    for t in range(145, T):
        Rt = R[t]; key = (tuple(D[t, Rt-W+1:Rt+1]), t % 68, Rt % 12); inc = R[t+1] - Rt
        if key in seen and seen[key] != inc: conflicts += 1
        seen.setdefault(key, inc)
    print(f"  W={W:2d}: distinct states {len(seen)}, conflicting transitions {conflicts}")
print("(C) band death from t0=145 at widths 40, 100, 200 (bottom rises 1 if black else 2; the top follows the front)")
for w in (40, 100, 200):
    t0 = 145; b = R[t0] - w; widths = []
    for t in range(t0, T):
        if b > R[t]: widths.append((t, 0)); break
        b = b + 1 if X[t, b] == 1 else b + 2
        if (t - t0) % 34 == 33: widths.append((t+1, R[t+1] - b))
    print(f"  width {w}: (time, width) every 34 ticks:", widths[:12], "..." if len(widths) > 12 else "")
print("(D) the masking envelope: U(t+1) = U(t) + 2 if E_{U+1}(t) = 0 else U(t) + 1; PROVED upper bound on every front; L_env(k) = max_(r,s) min{t: U(t) >= k}")
def envelope_bound(name, KMAX):
    p, q, orbit = background(name)
    Lenv = np.zeros(KMAX+1, dtype=np.int64); speeds = Counter(); best_al = {}
    for r in range(p):
        for s in range(q):
            def Ev(j, t): return orbit[(t+s) % q][(j+r) % p]
            # initial front of the inserted-edge witness: depth 0 if E_0(0) = 0, else no mismatch yet (the edge equals E); start U = 0 in both cases
            U = 0; t = 0; arr = np.full(KMAX+1, -1, dtype=np.int64); arr[0] = 0
            while U < KMAX:
                U = U + 2 if Ev(U+1, t) == 0 else U + 1; t += 1
                for k in range(KMAX+1):
                    if arr[k] < 0 and U >= k: arr[k] = t
            # exact speed from the periodic state (U mod p, t mod q)
            U = 0; t = 0; seen = {}
            while (U % p, t % q) not in seen:
                seen[(U % p, t % q)] = (U, t); U = U + 2 if Ev(U+1, t) == 0 else U + 1; t += 1
            U0, t0 = seen[(U % p, t % q)]; speeds[(U - U0, t - t0)] += 1
            for k in range(1, KMAX+1):
                if arr[k] > Lenv[k]: Lenv[k] = arr[k]; best_al[k] = (r, s)
    return Lenv, speeds, best_al
tables = {'e4_8': None, 'c7_28': [7,7,8,9,10,10,12,12,16,16,17,17,18,18,20,21,24,24,25,26], 's7_63': [11,12,12,15,15,16,17,18,18,20,22,24,24,25],
          's9_57': [12,13,13,15,15,16,16,17,17,19,24,27,28,34,35,35,41,42,42,43], 's12_68': [23,24,24,26,26,28,28,32,32,35,36,36,38,38,40,40,43,45]}
W12 = [int(x) for x in open('background_witness_law_s12_68.out').read().split('W(1..300) = ')[1].split('\n')[0].split()]
for nm in ('e4_8', 'c7_28', 's7_63', 's9_57', 's12_68'):
    KMAX = 300 if nm == 's12_68' else 40
    Lenv, speeds, best_al = envelope_bound(nm, KMAX)
    sp = sorted(((sh/per, sh, per) for (sh, per) in speeds), reverse=True)
    print(f"  {nm}: envelope (shift, period) classes {dict(speeds)}; slowest envelope speed {sp[-1][1]}/{sp[-1][2]} = {sp[-1][0]:.4f}")
    print(f"    L_env(1..{min(KMAX,40)}) = {' '.join(str(int(x)) for x in Lenv[1:min(KMAX,40)+1])}")
    if tables[nm]:
        M = tables[nm]; ok = all(Lenv[k] <= M[k-1] for k in range(1, len(M)+1))
        print(f"    exact M       = {' '.join(map(str, M))}  | L_env <= M at every k: {ok}; equality at k = {[k for k in range(1, len(M)+1) if Lenv[k] == M[k-1]]}")
    if nm == 'e4_8':
        print(f"    ceil(2k/3)    = {' '.join(str(-(-2*k//3)) for k in range(1, 41))}")
    if nm == 's12_68':
        print(f"    W(1..40)      = {' '.join(map(str, W12[:40]))}")
        print(f"    L_env <= W at every k <= 300: {all(Lenv[k] <= W12[k-1] for k in range(1, 301))}; L_env(300) = {Lenv[300]}, W(300) = {W12[299]}, ratio {Lenv[300]/W12[299]:.3f}")
        print(f"    attaining alignments for L_env at k = 20, 100, 300: {best_al[20]}, {best_al[100]}, {best_al[300]}")
print("BG_ENVELOPE_DONE")
