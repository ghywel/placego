#!/usr/bin/env python3
"""strip_graph.py NAME W: the adversarial strip graph of a phase E in diagonal coordinates. State = (E's phase index at the band's
bottom, the W+1 diagonal values above and including the deepest mismatch k_min). Transition: D_k' = D_(k-2) XOR (D_(k-1) OR D_k) with
E below; the new k_min is the lowest mismatch; the diagonals entering the band from above take both values (branching). Edge weight =
rise of k_min. Maximum mean cycle weight by value iteration on f_(n+1)(v) = max_u f_n(u) + w(u,v), reported as the slope over the last
half of 6V steps; an eternal point needs a cycle of mean exactly 2 (Block 25 (B)). Cloud."""
import sys, numpy as np
name, W = sys.argv[1], int(sys.argv[2])
if name == 'G8': ring, lag = (1,0,0,0), None
else:
    from pysat.solvers import Solver
    N0, r0 = 128, 72; yv = lambda i: (i % N0) + 1; cl = []; nv = N0
    for n in range(N0):
        nv += 1; o = nv; a, b = yv(n-1), yv(n-2); cl += [[-a, o], [-b, o], [a, b, -o]]
        x, z = yv(n-r0), yv(n); cl += [[-x, z, o], [-x, -z, -o], [x, -z, o], [x, z, -o]]
    ds = []
    for i in range(N0 // 2):
        nv += 1; d = nv; a, b = yv(i), yv(i + N0 // 2); ds.append(d); cl += [[-d, a, b], [-d, -a, -b]]
    cl.append(ds)
    with Solver(name='cadical195', bootstrap_with=cl) as s_:
        assert s_.solve(); m = s_.get_model(); ring = tuple(1 if m[i] > 0 else 0 for i in range(N0))
    lag = 72
N = len(ring); y = np.array(ring, dtype=np.uint8)
def cst(s): return s ^ (np.roll(s, 1) | np.roll(s, 2))
orb = [y.copy()]; cur = cst(y)
while not np.array_equal(cur, y): orb.append(cur.copy()); cur = cst(cur)
orb = np.array(orb); q = len(orb)
# E in diagonal coordinates: lab x = k - t; frame depth j = t - x = 2t - k; E_k(t) = orb[t % q][(j + a) % N] for alignment a (time shift absorbed when c = rho^lag)
# phase of the band bottom: (t mod q, (2t - k_min + a) mod N) -> state phase index ph = (t mod q, j0 mod N) with j0 = depth of k_min
# step: t -> t+1; k_min -> k_min + rise; j0' = 2(t+1) - (k_min + rise) = j0 + 2 - rise
phases = [(tq, j0) for tq in range(q) for j0 in range(N)]
if lag is not None: phases = [(0, j0) for j0 in range(N)]    # with c = rho^lag, orb[t][i] = y[i - lag t]: fold time into the depth phase
def Eval(tq, j):
    if lag is not None: return int(y[(j - lag * tq) % N]) if False else int(y[j % N])   # placeholder, replaced below
# exact E for the lag case: E at frame depth j, frame time t = y[(j - lag*t) % N]; we track (t mod N?) -> use j_eff = j - lag*t mod N as the phase
def Ebelow(ph, i, dt):   # value of E at depth j0 + i (i = 1, 2: the diagonals k_min - i BELOW the band bottom are DEEPER) at time t + dt
    # corrected 2026-11-02 (CL687) after GPT's GC2404: the earlier code read depth j0 - i here (a sign error); its outputs (G8: mean rise
    # 4.5 at W = 6, 6.5 at W = 8, "uninformative") are that faulty implementation's and are superseded by this run
    tq, j0 = ph
    if lag is not None: return int(y[(j0 + i - lag * dt) % N])
    return int(orb[(tq + dt) % q][(j0 + i) % N])
def Eat(ph, i, dt):      # E at depth j0 + i (inside the band region) at time t + dt
    tq, j0 = ph
    if lag is not None: return int(y[(j0 + i - lag * dt) % N])
    return int(orb[(tq + dt) % q][(j0 + i) % N])
def rule(a, b, c): return a ^ (b | c)
states = {}; edges = []   # state = (ph, strip) with strip = tuple of W+1 values D_(k_min .. k_min+W); strip[0] != E there
def sid(st):
    if st not in states: states[st] = len(states)
    return states[st]
from itertools import product
# enumerate all states (phase x strips with a mismatch at the bottom)
import collections
queue = collections.deque()
for ph in phases:
    for bits in product((0, 1), repeat=W + 1):
        if bits[0] == Eat(ph, 0, 0): continue
        st = (ph, bits); sid(st); queue.append(st)
V = len(states); print(f"{name}: W={W}, states {V}", flush=True)
src, dst, wt = [], [], []
for st in list(states):
    ph, strip = st; tq, j0 = ph
    # depth of diagonal k_min + i is j0 - i (higher diagonal = shallower); new values
    new = []
    for i in range(W + 1):
        a = strip[i - 2] if i >= 2 else Ebelow(ph, 2 - i, 0)     # D_(k-2)
        b = strip[i - 1] if i >= 1 else Ebelow(ph, 1, 0)         # D_(k-1)
        new.append(rule(a, b, strip[i]))
    # new E values at time t+1 for the band's diagonals: diagonal k_min + i has depth j0 - i at t, and depth j0 - i + 2 at t+1
    Enew = [Eat(ph, 2 - i, 1) if i <= 2 else None for i in range(W + 1)]
    # careful: depth of diagonal k at time t+1 is j0 + 2 - i; Eat takes a depth offset from j0: offset 2 - i (may be negative: deeper)
    Enew = [ (int(y[(j0 + 2 - i - lag) % N]) if lag is not None else int(orb[(tq + 1) % q][(j0 + 2 - i) % N])) for i in range(W + 1)]
    rise = next((i for i in range(W + 1) if new[i] != Enew[i]), None)
    if rise is None: continue     # the whole band healed: the deepest mismatch jumped above the band (no eternal cycle of depth range <= W)
    known = new[rise:]            # known values of the new band from its new bottom
    need = W + 1 - len(known)
    nph = (0, (j0 + 2 - rise - lag) % N) if lag is not None else ((tq + 1) % q, (j0 + 2 - rise) % N)
    for tail in product((0, 1), repeat=need):
        nst = (nph, tuple(known) + tail)
        if nst in states:
            src.append(states[st]); dst.append(states[nst]); wt.append(rise)
src = np.array(src); dst = np.array(dst); wt = np.array(wt, dtype=np.int64)
# --- direct replay control (CL687): build a literal row = E everywhere except the band, step it with the lab rule, and check that the
# graph's successor set contains the real successor (the real new strip, with the real entering diagonals), for random states
if lag is None:
    rng = np.random.default_rng(3); checked = 0; bad = 0
    def Elab(x, t, j0, tq):   # lab cell (x, t) of E when depth j0 at time tq is the band bottom's phase: depth j = t - x ... in diagonal
        return None
    adj = collections.defaultdict(set)
    for a_, b_ in zip(src, dst): adj[int(a_)].add(int(b_))
    keys = list(states)
    for trial in range(2000):
        st = keys[rng.integers(len(keys))]; (tq, j0), strip = st
        # diagonal coordinates: D_k(t+1) = D_(k-2) XOR (D_(k-1) OR D_k); E_k(t) at depth j = 2t - k; here band bottom k_min has depth j0 at
        # phase time tq. Build D over k in [k_min - M, k_min + W + M] with E below and above, the strip in the band, then step literally.
        M = 8; T0 = tq; kmin = 2 * T0 - j0
        ks = list(range(kmin - M, kmin + W + 1 + M)); D = {}
        for k in ks:
            i = k - kmin
            if 0 <= i <= W: D[k] = strip[i]
            else: D[k] = int(orb[T0 % q][(2 * T0 - k) % N])
        Dn = {k: D[k - 2] ^ (D[k - 1] | D[k]) for k in ks if k - 2 in D}
        En = {k: int(orb[(T0 + 1) % q][(2 * (T0 + 1) - k) % N]) for k in Dn}
        mism = [k for k in sorted(Dn) if Dn[k] != En[k] and k >= kmin]
        if not mism: continue   # band healed (graph has no edge); skip
        nk = mism[0]; rise_real = nk - kmin
        if rise_real > W: continue
        nst = (((T0 + 1) % q, (2 * (T0 + 1) - nk) % N), tuple(Dn[nk + i] for i in range(W + 1)))
        checked += 1
        if nst not in states or states[nst] not in adj[states[st]]: bad += 1
    print(f"  replay control: {checked} random real transitions, {bad} not in the graph's successor set")

print(f"  edges {len(src)}; rise distribution {np.bincount(wt).tolist()}", flush=True)
# value iteration with weights rise - 2
f = np.zeros(V, dtype=np.int64); K = 6 * V if V < 20000 else 120000
hist = []
for n in range(K):
    g = np.full(V, -10**12, dtype=np.int64); np.maximum.at(g, dst, f[src] + (wt - 2))
    f = g; 
    if n % (K // 10) == 0 or n == K - 1: hist.append((n, int(f.max())))
print("  max f over steps (n, max f) with weights rise-2:", hist)
slope = (hist[-1][1] - hist[len(hist)//2][1]) / (hist[-1][0] - hist[len(hist)//2][0])
print(f"  slope of max f over the last half: {slope:.4f} => estimated max mean rise {2 + slope:.4f} ({'below 2: no adversarial eternal cycle of depth range <= W' if hist[-1][1] < -V*(W+2) else 'not separated from 2 at this K'})")
print("STRIP_GRAPH_DONE")
