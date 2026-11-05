"""edge_model.py: the two-wheel model of the edge (CL741). The edge m(t) is the lowest erroneous wheel of the actual row
against the strip (e = a XOR C, errors below the edge are zero). Model M(L, R, W): state = the strip's bits at wheels
m-L..m+R and the errors at m+1..m+W; every other bit the wall-frame step needs is a fresh fair coin (two strip bits below
m-L, the strip's and the errors' bits above the window); the new edge is the lowest erroneous wheel at t+1 and the new
state is read there. The transition matrix is exact by enumeration of the coins over an extension of E wheels (a jump past
the extension lands in a fresh uniform state; its mass is reported). The stationary measure predicts the death rate, the
jump law, the error densities above the edge and the law of the state, against the empirical values from the seed on
165,750 wheels (the empirical part re-runs error_process.py's walk and records the state and its transitions every tick).
M_strip: the strip's coins weighted by the strip's own frequency of the whole window, measured on the strip over its
32 rows and all wheels (no edge data); the error coins stay fair. Predictions P-E0 .. P-E5 in CL741, P-F1, P-F2 in its addendum 1.
Usage: python3 edge_model.py ROWSDIR [L,R,W,E[,1] ...]   (a fifth field 1 = the strip-law chain)   (the rows of tree16_data.py at 165,750 wheels; A0.bin at phase 0)"""
import sys, time, collections
import numpy as np

# ---------- the model ----------
def model(L, R, W, E, cfreq=None):
    """M(L,R,W) with extension E. cfreq: the strip's frequency table of windows of L+3+R+E bits (lowest wheel at bit 0);
    None = fair coins for the strip. Errors outside the window are fair coins in both cases."""
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
    T = np.zeros((nS, nS)); death = np.zeros(nS); jumps = np.zeros((nS, R + E + 2)); pbj = np.zeros((nS, R + E + 2)); overflow = 0.0; stayblack = np.zeros(nS)
    maxj = min(E, R + E - W)      # the largest jump whose new state (strip to m'+R, errors to m'+W) is inside the computed window
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
        if cfreq is None: wt = np.full(N, 1.0 / N)
        else:
            code = np.zeros(N, dtype=np.int64)
            for p in range(lo, hi + 1): code |= C[p].astype(np.int64) << (p - lo)
            wt = cfreq[code].astype(float); z = wt.sum()
            wt = wt / z if z > 0 else np.full(N, 1.0 / N)       # a window the strip never shows: unreachable, left uniform
        a = {p: C[p] ^ e[p] for p in C}
        C2 = {p: C[p - 2] ^ (C[p - 1] | C[p]) for p in range(lo + 2, hi + 1)}
        a2 = {p: a[p - 2] ^ (a[p - 1] | a[p]) for p in range(lo + 2, hi + 1)}
        e2 = {p: C2[p] ^ a2[p] for p in C2}
        # new edge: lowest p >= 0 with e2[p] = 1 (e2[p] = 0 for p < 0 automatically)
        m2 = np.full(N, hi + 1, dtype=np.int64)
        for p in range(hi, -1, -1): m2 = np.where(e2[p] == 1, p, m2)
        d = Cs[L - 1]                        # C_{m-1}: death iff 1
        death[s] = d
        if d == 0: stayblack[s] = wt[C2[-1] == 1].sum()      # the parent black at t+1 after a stay (the hazard q)
        for j in range(0, maxj + 1):
            sel = (m2 == j)
            w = wt[sel].sum()
            if w == 0: continue
            jumps[s, j] += w
            if j >= 1: pbj[s, j] += wt[sel & (C2[j - 1] == 1)].sum()
            # new state at m' = j: C at j-L..j+R, e at j+1..j+W (all inside lo+2..hi)
            code = np.zeros(N, dtype=np.int64)
            for i in range(L + 1 + R): code |= C2[j - L + i].astype(np.int64) << i
            for i in range(W): code |= e2[j + 1 + i].astype(np.int64) << (L + 1 + R + i)
            T[s] += np.bincount(code[sel], weights=wt[sel], minlength=nS)
        sel = m2 > maxj
        if sel.any():
            w = wt[sel].sum(); overflow += w / nS; jumps[s, maxj + 1] += w
            T[s] += w / nS                    # a fresh uniform state
    assert np.allclose(T.sum(1), 1), T.sum(1)
    # stationary measure by power iteration
    pi = np.full(nS, 1 / nS)
    for _ in range(20000):
        pi2 = pi @ T
        if np.abs(pi2 - pi).max() < 1e-14: pi = pi2; break
        pi = pi2
    drate = float(pi @ death)
    jl = (pi * death) @ jumps / drate            # jump law at a death (index = jump; the last nonzero index holds every jump past the extension)
    pbl = ((pi * death) @ pbj) / np.maximum((pi * death) @ jumps, 1e-300)   # P(new parent black | jump)
    dens = [float(pi @ np.array([(s >> (L + 1 + R + i)) & 1 for s in range(nS)])) for i in range(W)]
    q = float(pi @ stayblack) / float(pi @ (1 - death))
    return pi, drate, jl, dens, T, overflow, pbl, maxj, q

def fmt_jl(jl, upto=9): return {j: round(float(jl[j]), 4) for j in range(1, min(upto, len(jl) - 1) + 1)}

def strip_windows(cyc, K, width):
    """Frequency of every width-bit window of the strip over its P rows and all wheels (lowest wheel at bit 0)."""
    freq = np.zeros(1 << width, dtype=np.int64)
    for row in cyc:
        b = np.unpackbits(np.frombuffer(row.to_bytes((K + 7) // 8, 'little'), dtype=np.uint8), bitorder='little')[:K].astype(np.int64)
        n = K - width + 1; code = np.zeros(n, dtype=np.int64)
        for i in range(width): code |= b[i:i + n] << i
        freq += np.bincount(code, minlength=1 << width)
    return freq

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
cond = collections.defaultdict(lambda: np.zeros(4, dtype=np.int64))   # per state: visits, e_{m+3}, C_{m+3}, C_{m-3}
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
        if m >= 3: cond[s] += (1, (e >> (m + 3)) & 1, (C >> (m + 3)) & 1, (C >> (m - 3)) & 1)
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
def sname(s): return "C[m-2..m+2]=" + "".join(str((s >> i) & 1) for i in range(5)) + " e[m+1,m+2]=" + "".join(str((s >> (5 + i)) & 1) for i in range(2))
print("where the fair coins fail: the empirical density of e_{m+3}, C_{m+3}, C_{m-3} given the state (the model says 1/2 for each);")
for name, col in (("e_{m+3}", 1), ("C_{m+3}", 2), ("C_{m-3}", 3)):
    tot_v = sum(v[0] for v in cond.values()); mad = sum(abs(v[col] / v[0] - 0.5) * v[0] for v in cond.values()) / tot_v
    ext = sorted(((v[col] / v[0], s, v[0]) for s, v in cond.items() if v[0] >= 1000))
    print(f"  {name}: overall {sum(v[col] for v in cond.values())/tot_v:.4f}, mean |density - 1/2| over the ticks {mad:.4f}; lowest {ext[0][0]:.3f} at {sname(ext[0][1])} ({ext[0][2]}), highest {ext[-1][0]:.3f} at {sname(ext[-1][1])} ({ext[-1][2]})")
by_e = collections.defaultdict(lambda: np.zeros(2, dtype=np.int64))
for s, v in cond.items(): by_e[s >> 5] += (v[0], v[1])
print("  e_{m+3} density given (e_{m+1}, e_{m+2}): " + ", ".join(f"{k & 1}{k >> 1}: {v[1]/v[0]:.4f} ({v[0]})" for k, v in sorted(by_e.items())))
emp = np.array([visits[s] for s in range(nS)], dtype=float); emp /= emp.sum()
# the strip's own statistics: black density over the wheels, and the mean white run in its fixed-wheel series (period 32)
sd = bin(A0).count('1') / K
runs = []; tot_w = 0
for j in range(2, 200002, 97):
    ser = [(cyc[tt] >> j) & 1 for tt in range(P)]
    nb = sum(ser); tot_w += (P - nb) / P
print(f"the strip: black density over the wheels {sd:.4f}; white density in the fixed-wheel series (sample) {tot_w/len(range(2,200002,97)):.4f}")

# the strip's own window law (P-F1): P(C_{j+5} = 1 | C_j..C_{j+4}) over all its positions, against the edge-conditional law
f6 = strip_windows(cyc, K, 6).astype(float)
p6 = {w: f6[w | (1 << 5)] / (f6[w] + f6[w | (1 << 5)]) for w in range(32) if f6[w] + f6[w | (1 << 5)] > 0}
tot6 = f6.sum(); mad6 = sum(abs(p6[w] - 0.5) * (f6[w] + f6[w | 32]) for w in p6) / tot6
ec = collections.defaultdict(lambda: np.zeros(2, dtype=np.int64))
for s_, v in cond.items(): ec[s_ & 31] += (v[0], v[2])
print(f"P-F1: the strip's law P(C_(j+5)=1 | 5-window) over all positions: mean |p - 1/2| = {mad6:.4f}; windows (lowest wheel first) with p < 0.3 or > 0.7: "
      + ", ".join(f"{''.join(str((w >> i) & 1) for i in range(5))}: {p6[w]:.3f}" for w in sorted(p6) if p6[w] < 0.3 or p6[w] > 0.7))
print("  the same at the edge (C_(m+3) given C[m-2..m+2], all error states): "
      + ", ".join(f"{''.join(str((w >> i) & 1) for i in range(5))}: {ec[w][1]/ec[w][0]:.3f}" for w in sorted(ec) if w in p6 and (p6[w] < 0.3 or p6[w] > 0.7)))
print(f"  the strip's windows: {int((f6 > 0).sum())} of 64 six-windows occur; of 15-windows {int((strip_windows(cyc, K, 15) > 0).sum())} of 32768")

# ---------- the models ----------
results = {}
MODELS = [tuple(int(v) for v in a.split(',')) for a in sys.argv[2:]] or [(2, 2, 2, 8), (2, 2, 1, 8), (2, 2, 3, 8), (3, 3, 2, 8), (2, 2, 4, 8), (2, 2, 2, 10), (2, 2, 2, 8, 1), (2, 2, 3, 8, 1), (2, 2, 2, 10, 1)]
for spec in MODELS:
    l, r, w, E = spec[:4]; use_strip = len(spec) > 4 and spec[4] == 1
    t1 = time.time()
    cf = strip_windows(cyc, K, l + 3 + r + E) if use_strip else None
    pi, drate, jl, mdens, T, overflow, pbl, maxj, q = model(l, r, w, E, cf)
    mean = float(sum(j * jl[j] for j in range(len(jl))))
    results[(l, r, w, use_strip)] = (pi, drate, jl, mdens, T)
    print(f"M{'_strip' if use_strip else ''}({l},{r},{w}) E={E}: {1 << (l+1+r+w)} states, {time.time()-t1:.0f} s; overflow mass {overflow:.2e}; "
          f"death rate {drate:.4f}; jump law {fmt_jl(jl)}; mean {mean:.4f}; speed {drate*mean:.4f}; "
          f"error density at offsets 1..{w}: {[round(v, 4) for v in mdens]}; jumps past {maxj} lumped at {maxj+1}; "
          f"P(parent black | jump d): {{{', '.join(f'{d}: {pbl[d]:.3f}' for d in range(1, min(6, maxj) + 1))}}}; "
          f"hazard after a stay q {q:.4f}; S4: S = {sum(float(jl[d]) * (1 - float(pbl[d])) for d in range(1, maxj + 2)):.4f}, 1/(1+S/q) = {1 / (1 + sum(float(jl[d]) * (1 - float(pbl[d])) for d in range(1, maxj + 2)) / q):.4f}")
for key in [(2, 2, 2, False), (2, 2, 2, True)]:
    if key not in results: continue
    pi = results[key][0]
    print(f"P-E4a/P-F2: total variation between M{'_strip' if key[3] else ''}(2,2,2)'s stationary law and the empirical law of the 7-bit state: {0.5 * np.abs(pi - emp).sum():.4f}")
if (2, 2, 2, False) not in results: sys.exit(0)          # the Markov test and the state table are for the two-wheel chain
pi, drate, jl, mdens, T = results[(2, 2, 2, False)]
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
print(f"Markov test on {len(rows)} states with >= 1000 visits: median row TV {np.median([r[0] for r in rows]):.4f}, worst five:")
for tvr, s, n in rows[:5]: print(f"  TV {tvr:.4f} {sname(s)} visits {n}; empirical weight {emp[s]:.4f}, model {pi[s]:.4f}")
print("states by weight (model vs empirical), the ten heaviest:")
for s in np.argsort(-pi)[:10]: print(f"  {sname(s)}: model {pi[s]:.4f}, empirical {emp[s]:.4f}")
