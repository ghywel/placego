"""edge_model.py: the two-wheel model of the edge (CL741). The edge m(t) is the lowest erroneous wheel of the actual row
against the strip (e = a XOR C, errors below the edge are zero). Model M(L, R, W): state = the strip's bits at wheels
m-L..m+R and the errors at m+1..m+W; every other bit the wall-frame step needs is a fresh fair coin (two strip bits below
m-L, the strip's and the errors' bits above the window); the new edge is the lowest erroneous wheel at t+1 and the new
state is read there. The transition matrix is exact by enumeration of the coins over an extension of E wheels (a jump past
the extension lands in a fresh uniform state; its mass is reported). The stationary measure predicts the death rate, the
jump law, the error densities above the edge and the law of the state, against the empirical values from the seed on
165,750 wheels (the empirical part re-runs error_process.py's walk and records the state and its transitions every tick).
Predictions P-E0 .. P-E5 in CL741.
Usage: python3 edge_model.py ROWSDIR   (the rows of tree16_data.py at 165,750 wheels; A0.bin at phase 0)"""
import sys, time, collections
import numpy as np

# ---------- the model ----------
def model(L, R, W, E, verbose=True):
    """Returns (pi, death, jump_law, dens, T, overflow, codes) for M(L,R,W) with extension E."""
    assert W <= R + E - 1
    nS = 1 << (L + 1 + R + W)
    # positions p relative to the edge: strip known on -L..R (state), coins on -L-2, -L-1 and R+1..R+E;
    # errors: 0 below the edge, 1 at 0, state on 1..W, coins on W+1..R+E
    cpos = list(range(-L - 2, -L)) + list(range(R + 1, R + E + 1))
    epos = list(range(W + 1, R + E + 1))
    ncoin = len(cpos) + len(epos)
    N = 1 << ncoin
    idx = np.arange(N, dtype=np.int64)
    coins = [((idx >> i) & 1).astype(np.int8) for i in range(ncoin)]
    lo, hi = -L - 2, R + E
    T = np.zeros((nS, nS)); death = np.zeros(nS); jumps = np.zeros((nS, R + E + 2)); overflow = 0.0
    maxj = E - max(R, W)          # the largest jump whose new state is fully inside the computed window
    for s in range(nS):
        Cs = [(s >> i) & 1 for i in range(L + 1 + R)]          # C at -L..R
        es = [(s >> (L + 1 + R + i)) & 1 for i in range(W)]    # e at 1..W
        C = {}; e = {}
        k = 0
        for p in range(lo, hi + 1):
            if -L <= p <= R: C[p] = np.full(N, Cs[p + L], dtype=np.int8)
            else: C[p] = coins[k]; k += 1
        for p in range(lo, hi + 1):
            if p < 0: e[p] = np.zeros(N, dtype=np.int8)
            elif p == 0: e[p] = np.ones(N, dtype=np.int8)
            elif p <= W: e[p] = np.full(N, es[p - 1], dtype=np.int8)
            else: e[p] = coins[k]; k += 1
        assert k == ncoin
        a = {p: C[p] ^ e[p] for p in C}
        C2 = {p: C[p - 2] ^ (C[p - 1] | C[p]) for p in range(lo + 2, hi + 1)}
        a2 = {p: a[p - 2] ^ (a[p - 1] | a[p]) for p in range(lo + 2, hi + 1)}
        e2 = {p: C2[p] ^ a2[p] for p in C2}
        # new edge: lowest p >= 0 with e2[p] = 1 (e2[p] = 0 for p < 0 automatically)
        m2 = np.full(N, hi + 1, dtype=np.int64)
        for p in range(hi, -1, -1): m2 = np.where(e2[p] == 1, p, m2)
        d = Cs[L - 1]                        # C_{m-1}: death iff 1
        death[s] = d
        for j in range(0, maxj + 1):
            sel = (m2 == j)
            w = sel.mean()
            if w == 0: continue
            jumps[s, j] += w
            # new state at m' = j: C at j-L..j+R, e at j+1..j+W (all inside lo+2..hi)
            code = np.zeros(N, dtype=np.int64)
            for i in range(L + 1 + R): code |= C2[j - L + i].astype(np.int64) << i
            for i in range(W): code |= e2[j + 1 + i].astype(np.int64) << (L + 1 + R + i)
            T[s] += np.bincount(code[sel], minlength=nS) / N
        sel = m2 > maxj
        if sel.any():
            w = sel.mean(); overflow += w / nS; jumps[s, maxj + 1] += w
            T[s] += w / nS                    # a fresh uniform state
    assert np.allclose(T.sum(1), 1)
    # stationary measure by power iteration
    pi = np.full(nS, 1 / nS)
    for _ in range(20000):
        pi2 = pi @ T
        if np.abs(pi2 - pi).max() < 1e-14: pi = pi2; break
        pi = pi2
    drate = float(pi @ death)
    jl = (pi * death) @ jumps / drate            # jump law at a death (index = jump)
    dens = [float(pi @ np.array([(s >> (L + 1 + R + i)) & 1 for s in range(nS)])) for i in range(W)]
    return pi, drate, jl, dens, T, overflow

def fmt_jl(jl, upto=9): return {j: round(float(jl[j]), 4) for j in range(1, min(upto, len(jl) - 1) + 1)}

# ---------- the data ----------
K = 165750; MASK = (1 << K) - 1; P = 32
ROWS = sys.argv[1]
def step(v): return ((v << 2) ^ ((v << 1) | v)) & MASK
def lowbit(x): return (x & -x).bit_length() - 1 if x else K
A0 = int.from_bytes(open(f"{ROWS}/A0.bin", 'rb').read(), 'little')
cyc = [A0]
for _ in range(P): cyc.append(step(cyc[-1]))
assert cyc[P] == A0; cyc = cyc[:P]
L = R = W = 2
t0 = time.time()
x = 1; t = 0
visits = collections.Counter(); trans = collections.Counter()
after_stay = [0, 0]; after_jump = collections.defaultdict(lambda: [0, 0]); jumps = collections.Counter()
dens = np.zeros(9, dtype=np.int64); nwin = 0; pblack = 0
def state_of(C, e, m):
    s = 0
    for i in range(L + 1 + R): s |= ((C >> (m - L + i)) & 1) << i
    for i in range(W): s |= ((e >> (m + 1 + i)) & 1) << (L + 1 + R + i)
    return s
prev = None   # (state, m, pb)
while True:
    C = cyc[t % P]; e = x ^ C; m = lowbit(e)
    if m >= K: break
    if m >= L:
        s = state_of(C, e, m); visits[s] += 1; nwin += 1
        pb = (C >> (m - 1)) & 1; pblack += pb
        for d in range(1, 9): dens[d] += (e >> (m + d)) & 1
        if prev is not None:
            ps, pm, ppb = prev
            trans[(ps, s)] += 1
            if ppb == 0: after_stay[pb] += 1
            else: after_jump[m - pm][pb] += 1; jumps[m - pm] += 1
        prev = (s, m, pb)
    else: prev = None
    x = step(x); t += 1
print(f"data: {nwin} ticks with the edge at a wheel >= 2 (settling at {t}); {time.time()-t0:.0f} s")
d_rate = pblack / nwin; tot = sum(jumps.values()); d_jl = {j: round(v / tot, 4) for j, v in sorted(jumps.items()) if j <= 9}
d_mean = sum(j * v for j, v in jumps.items()) / tot
print(f"empirical death rate {d_rate:.4f}; jump law {d_jl}; mean {d_mean:.4f}; product {d_rate*d_mean:.4f}")
print(f"empirical error density at offsets 1..8: {[round(float(dens[d])/nwin, 4) for d in range(1, 9)]}")
print(f"P-E0: parent black at t+1 after a jump of 2: {after_jump[2][1]} of {sum(after_jump[2])} (PROVED: must be 0)")
print(f"P-E4b: P(parent black at t+1 | the edge stayed) = {after_stay[1]/sum(after_stay):.4f} on {sum(after_stay)} stays")
print("parent black at t+1 after a jump of d: " + ", ".join(f"{d}: {after_jump[d][1]/sum(after_jump[d]):.3f} ({sum(after_jump[d])})" for d in sorted(after_jump) if d <= 6))
nS = 1 << (L + 1 + R + W)
emp = np.array([visits[s] for s in range(nS)], dtype=float); emp /= emp.sum()
# the strip's own statistics: black density over the wheels, and the mean white run in its fixed-wheel series (period 32)
sd = bin(A0).count('1') / K
runs = []; tot_w = 0
for j in range(2, 200002, 97):
    ser = [(cyc[tt] >> j) & 1 for tt in range(P)]
    nb = sum(ser); tot_w += (P - nb) / P
print(f"the strip: black density over the wheels {sd:.4f}; white density in the fixed-wheel series (sample) {tot_w/len(range(2,200002,97)):.4f}")

# ---------- the models ----------
results = {}
for (l, r, w, E) in [(2, 2, 2, 8), (2, 2, 1, 8), (2, 2, 3, 8), (3, 3, 2, 7), (2, 2, 4, 8)]:
    t1 = time.time()
    pi, drate, jl, mdens, T, overflow = model(l, r, w, E)
    mean = float(sum(j * jl[j] for j in range(len(jl))))
    results[(l, r, w)] = (pi, drate, jl, mdens, T)
    print(f"M({l},{r},{w}) E={E}: {1 << (l+1+r+w)} states, {time.time()-t1:.0f} s; overflow mass {overflow:.2e}; "
          f"death rate {drate:.4f}; jump law {fmt_jl(jl)}; mean {mean:.4f}; speed {drate*mean:.4f}; "
          f"error density at offsets 1..{w}: {[round(v, 4) for v in mdens]}")
pi, drate, jl, mdens, T = results[(2, 2, 2)]
tv = 0.5 * np.abs(pi - emp).sum()
print(f"P-E4a: total variation between M(2,2,2)'s stationary law and the empirical law of the 7-bit state: {tv:.4f}")
# the Markov test: per-state transition rows, model vs empirical, for well-visited states
rows = []
for s in range(nS):
    n = visits[s]
    if n < 1000: continue
    er = np.zeros(nS)
    for s2 in range(nS): er[s2] = trans[(s, s2)]
    er /= er.sum()
    rows.append((0.5 * np.abs(er - T[s]).sum(), s, n))
rows.sort(reverse=True)
def sname(s): return "C[m-2..m+2]=" + "".join(str((s >> i) & 1) for i in range(5)) + " e[m+1,m+2]=" + "".join(str((s >> (5 + i)) & 1) for i in range(2))
print(f"Markov test on {len(rows)} states with >= 1000 visits: median row TV {np.median([r[0] for r in rows]):.4f}, worst five:")
for tvr, s, n in rows[:5]: print(f"  TV {tvr:.4f} {sname(s)} visits {n}; empirical weight {emp[s]:.4f}, model {pi[s]:.4f}")
print("states by weight (model vs empirical), the ten heaviest:")
for s in np.argsort(-pi)[:10]: print(f"  {sname(s)}: model {pi[s]:.4f}, empirical {emp[s]:.4f}")
