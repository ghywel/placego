#!/usr/bin/env python3
"""L1279 (Local, 2026-11-01): genealogy schemas beside the colour, tests T1-T3 of
reports/rule30-genealogy.md (predictions are written there, before the first run).

Run: python3 tests/probes/genealogy_schemas.py   (about a minute on the M5; no files written)

Orientation x_i(t+1) = x_(i-1)(t) XOR (x_i(t) OR x_(i+1)(t)), single seed at 0, rows to T = 1500.
T0  identities: S2 (flip counter mod 2 is the colour), S6 (right-half cells are centre cells XOR their line's flips).
T1  the black family tree (S5): designated parent L for 100, C for 010/011, R for 001.
T2  lifts: Z/4 and dual-number identities (all 64 cases); sensitivity path growth (S4); tangent against
    actual damage; second digits of the Z/4 lift (S3) and of the flip counter (S2) on the single seed.
T3  exact cost of a k-generation family patch, by the composed 4^k-state reader (k <= 5).
"""
import numpy as np

T = 1500
W = 2 * T + 5
C = T + 2                                   # array index of position 0
X = np.zeros((T + 1, W), dtype=np.uint8)
X[0, C] = 1
for t in range(T):
    X[t + 1, 1:-1] = X[t, :-2] ^ (X[t, 1:-1] | X[t, 2:])


def rule(a, b, c):
    return a ^ (b | c)


# ---------------- T0: identities ----------------
N = X[0].astype(np.int64)                   # S2 flip counter, N(.,0) = X(.,0)
G = np.zeros((T + 1, W), dtype=np.uint8)    # G[t, i] = flip that made (i, t): x_i(t-1) OR x_(i+1)(t-1)
for t in range(T):
    g = np.zeros(W, dtype=np.uint8)
    g[1:-1] = X[t, 1:-1] | X[t, 2:]
    G[t + 1] = g
    N2 = np.zeros(W, dtype=np.int64)
    N2[1:-1] = N[:-2] + g[1:-1]
    N = N2
    if t + 1 in (10, 500, T):
        assert np.array_equal(N % 2, X[t + 1])
N_final = N
for t in (300, 900, T):                     # S6: x_i(t) = x_0(t-i) XOR sum_{m<i} G(i-m, t-m)
    for i in range(1, t + 1, 7):
        par = 0
        for m in range(i):
            par ^= G[t - m, C + i - m]
        assert X[t, C + i] == X[t - i, C] ^ par
print('T0  S2 flip counter mod 2 = colour (t = 10, 500, 1500); S6 wheel-stamp identity on sampled right-half cells: PASS')

# ---------------- T1: the black family tree ----------------
D = np.zeros((T + 1, W), dtype=np.int8)     # designated step: parent index = idx + D
for t in range(1, T + 1):
    a, b, c = X[t - 1, :-2], X[t - 1, 1:-1], X[t - 1, 2:]
    blk = X[t, 1:-1] == 1
    d = np.where(a == 1, -1, np.where(b == 1, 0, 1))
    D[t, 1:-1] = np.where(blk, d, 0)
# step shares in the bulk (three cells in from each edge), left and right halves
shares = {}
for half, lo_off, hi_off in (('all', None, None), ('left', None, 0), ('right', 1, None)):
    cnt = np.zeros(3)
    for t in range(10, T + 1):
        lo, hi = C - t + 3, C + t - 2
        if lo_off is not None:
            lo = max(lo, C + lo_off)
        if hi_off is not None:
            hi = min(hi, C + hi_off)
        idx = np.arange(lo, hi)
        m = X[t, idx] == 1
        dd = D[t, idx][m]
        cnt += [np.sum(dd == -1), np.sum(dd == 0), np.sum(dd == 1)]
    shares[half] = cnt / cnt.sum()
print('T1  designated-step shares L, C, R in the bulk: ' +
      '; '.join(f'{h} {s[0]:.3f} {s[1]:.3f} {s[2]:.3f}' for h, s in shares.items()))
# founders at t = 1 and at t = 10
F = np.full(W, -1, dtype=np.int64)
F[C - 1], F[C], F[C + 1] = 0, 1, 2
F10 = None
fshare = {}
for t in range(2, T + 1):
    blk = X[t] == 1
    par = np.arange(W) + D[t]
    F = np.where(blk, F[np.clip(par, 0, W - 1)], -1)
    if t == 10:
        F10 = np.where(blk, np.arange(W), -1)
    elif t > 10:
        F10 = np.where(blk, F10[np.clip(par, 0, W - 1)], -1)
    if t in (250, 500, 1000, T):
        nb = blk.sum()
        fshare[t] = [np.sum(F == k) / nb for k in range(3)]
        if t == T:
            alive10 = len(set(F10[blk].tolist()))
print('T1  founder shares of black cells (left, middle, right founder at t = 1): ' +
      '; '.join(f't={t}: ' + ' '.join(f'{v:.3f}' for v in s) for t, s in fshare.items()))
print(f'    black cells at t = 10: {int(X[10].sum())}; of them with descendants at t = {T}: {alive10}')


def ancestors(t0, idxs, smax):
    """distinct designated ancestors s steps back, s = 0..smax."""
    cur = np.unique(idxs)
    out = [len(cur)]
    for s in range(1, smax + 1):
        t = t0 - s + 1
        cur = np.unique(cur + D[t, cur])
        out.append(len(cur))
    return out


win = np.arange(C - 100, C + 101)
win = win[X[T, win] == 1]
prof = ancestors(T, win, T - 1)
mrca = next((s for s, n in enumerate(prof) if n == 1), None)
print(f'T1  central window |i|<=100 of row {T}: {len(win)} black cells; distinct ancestors at s = ' +
      ' '.join(f'{s}:{prof[s]}' for s in (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, T - 1)) +
      f'; first single ancestor at s = {mrca}')
rowall = np.flatnonzero(X[T] == 1)
profall = ancestors(T, rowall, T - 1)
print(f'    whole row {T}: {len(rowall)} black cells; distinct ancestors at s = ' +
      ' '.join(f'{s}:{profall[s]}' for s in (1, 4, 16, 64, 256, 1024, T - 1)))
# centre-column lineages: displacement at lag s
lags = (10, 30, 100, 300, 500)
disp = {s: [] for s in lags}
for t in range(1000, T + 1):
    if X[t, C] != 1:
        continue
    pos, tt = C, t
    for s in range(1, max(lags) + 1):
        pos = pos + int(D[tt, pos])
        tt -= 1
        if s in disp:
            disp[s].append(pos - C)
print('T1  centre lineages (centre black cells t = 1000..1500), displacement mean/std at lag s: ' +
      '; '.join(f's={s}: {np.mean(v):+.2f}/{np.std(v):.2f} (std/sqrt s {np.std(v)/np.sqrt(s):.2f})' for s, v in disp.items()))

# post hoc (no prediction written): the two surviving dynasties and the boundary between them
F = np.full(W, -1, dtype=np.int64)
F[C - 1], F[C], F[C + 1] = 0, 1, 2
bpos, interfaces, centre_fam = [], [], []
for t in range(2, T + 1):
    blk = X[t] == 1
    F = np.where(blk, F[np.clip(np.arange(W) + D[t], 0, W - 1)], -1)
    labs = F[blk]
    pos = np.flatnonzero(blk) - C
    changes = int(np.sum(labs[1:] != labs[:-1]))
    interfaces.append(changes)
    if changes == 1 and set(labs.tolist()) == {0, 2}:
        k = int(np.flatnonzero(labs[1:] != labs[:-1])[0])
        bpos.append((t, (pos[k] + pos[k + 1]) / 2))
    if X[t, C] == 1:
        centre_fam.append((t, int(F[C])))
iv = np.array(interfaces)
print(f'    post hoc: label changes along each row t = 2..{T}: max {iv.max()}, rows with exactly one {np.mean(iv == 1):.4f}; '
      f'middle family last alive at t = {max((t for t, n in enumerate([0, 0] + interfaces) if False), default="-")}')
bt = np.array([b for _, b in bpos]); tt_ = np.array([t for t, _ in bpos])
for t in (100, 250, 500, 750, 1000, 1250, 1500):
    sel = np.flatnonzero(tt_ == t)
    if sel.size:
        print(f'    dynasty boundary at t = {t}: position {bt[sel[0]]:+.1f}')
inc = np.diff(bt)
print(f'    boundary increments: mean {inc.mean():+.4f}, std {inc.std():.3f}; values {sorted(set(np.round(inc, 1).tolist()))[:12]}')
cf = np.array([f for _, f in centre_fam])
print(f'    centre black cells t = 2..{T}: share from the left founder {np.mean(cf == 0):.3f}, right {np.mean(cf == 2):.3f}, middle {np.mean(cf == 1):.3f}')

# T1b: the tie-break at 011 (C as above, R, or a seeded fair coin), and the black-parent DAG with no tie-break
def dynasty_run(mode, seed=0):
    rng_ = np.random.default_rng(seed)
    Fd = np.full(W, -1, dtype=np.int64)
    Fd[C - 1], Fd[C], Fd[C + 1] = 0, 1, 2
    bnd, cen, mid_last = [], [], 1
    for t in range(2, T + 1):
        a, b, c = X[t - 1, :-2], X[t - 1, 1:-1], X[t - 1, 2:]
        if mode == 'C':
            pick_r = np.zeros_like(b, dtype=bool)
        elif mode == 'R':
            pick_r = np.ones_like(b, dtype=bool)
        else:
            pick_r = rng_.integers(0, 2, size=b.size).astype(bool)
        d = np.where(a == 1, -1, np.where((b == 1) & ~((c == 1) & pick_r), 0, 1))
        dd = np.zeros(W, dtype=np.int64)
        dd[1:-1] = d
        blk = X[t] == 1
        Fd = np.where(blk, Fd[np.clip(np.arange(W) + dd, 0, W - 1)], -1)
        labs = Fd[blk]
        if (labs == 1).any():
            mid_last = t
        pos = np.flatnonzero(blk) - C
        ch = np.flatnonzero(labs[1:] != labs[:-1])
        if len(ch) == 1:
            bnd.append((pos[ch[0]] + pos[ch[0] + 1]) / 2)
        if X[t, C] == 1:
            cen.append(int(Fd[C]))
    bnd = np.array(bnd)
    cen = np.array(cen)
    switches = int(np.sum(cen[1:] != cen[:-1]))
    labs = Fd[X[T] == 1]
    final = [float(np.mean(labs == f)) for f in range(3)]
    changes = int(np.sum(labs[1:] != labs[:-1]))
    return mid_last, bnd, cen, switches, final, changes


for mode, seed in (('C', 0), ('R', 0), ('coin', 1), ('coin', 2), ('coin', 3)):
    mid_last, bnd, cen, sw, final, changes = dynasty_run(mode, seed)
    btxt = (f'single-boundary rows {len(bnd)}, last boundary {bnd[-1]:+.1f}, mean step {np.mean(np.diff(bnd)):+.4f}'
            if len(bnd) > 1 else f'single-boundary rows {len(bnd)}')
    print(f'T1b tie-break {mode}{"" if mode != "coin" else " seed " + str(seed)}: middle family last alive t = {mid_last}; '
          f'row {T} family shares L/M/R ' + '/'.join(f'{v:.3f}' for v in final) + f', label changes {changes}; {btxt}; '
          f'centre black cells L/M/R ' + '/'.join(f'{np.mean(cen == f):.3f}' for f in range(3)) + f', switches {sw}')
# the DAG: reachable from each founder through black parents
reach = np.zeros((3, W), dtype=bool)
reach[0, C - 1] = reach[1, C] = reach[2, C + 1] = True
for t in range(2, T + 1):
    blk = X[t] == 1
    new = np.zeros_like(reach)
    for f in range(3):
        r = reach[f]
        new[f, 1:-1] = blk[1:-1] & (r[:-2] | r[1:-1] | r[2:])
    reach = new
blk = X[T] == 1
cls = reach[0].astype(int) * 4 + reach[1].astype(int) * 2 + reach[2].astype(int)
names = {7: 'all three', 5: 'left+right', 6: 'left+middle', 3: 'middle+right', 4: 'left only', 2: 'middle only', 1: 'right only'}
print('T1b black-parent DAG, row 1500: ' + ', '.join(f'{names.get(k, k)} {np.mean(cls[blk] == k):.3f}' for k in sorted(set(cls[blk].tolist()), reverse=True)))

# ---------------- T2: lifts ----------------
ok = 0
for xa in (0, 1):
    for xb in (0, 1):
        for xc in (0, 1):
            r = rule(xa, xb, xc)
            kappa = 1 if xa + xb + xc == 2 else 0
            for ha in (0, 1):
                for hb in (0, 1):
                    for hc in (0, 1):
                        a, b, c = xa + 2 * ha, xb + 2 * hb, xc + 2 * hc
                        z = (a + b + c + b * c) % 4
                        lin = ha ^ ((1 ^ xc) & hb) ^ ((1 ^ xb) & hc)
                        assert z % 2 == r and ((z - r) % 4) // 2 == lin ^ kappa
                        # dual numbers GF(2)[e]/(e^2): (x + e h) through a + b + c + bc
                        eps = (ha + hb + hc + xb * hc + xc * hb) % 2
                        assert eps == lin
                        ok += 1
print(f'T2  Z/4 second digit = Boolean-derivative tangent + carry [two parents black]; dual numbers = tangent: {ok}/64 PASS')
# S4 path growth and tangent versus damage, from single cells at t0 = 500
t0, S = 500, 500
lams, agree_bulk, agree_edge = [], [], []
for j in (-60, -20, 0, 20, 60):
    P = np.zeros(W)
    P[C + j] = 1.0
    logsum = 0.0
    h = np.zeros(W, dtype=np.uint8)
    h[C + j] = 1
    Y = X[t0].copy()
    Y[C + j] ^= 1
    for s in range(S):
        x = X[t0 + s]
        P2 = np.zeros(W)
        P2[1:-1] = P[:-2] + (x[2:] == 0) * P[1:-1] + (x[1:-1] == 0) * P[2:]
        tot = P2.sum()
        logsum += np.log(tot)
        P = P2 / tot
        h2 = np.zeros(W, dtype=np.uint8)
        h2[1:-1] = h[:-2] ^ ((x[2:] == 0) & h[1:-1]) ^ ((x[1:-1] == 0) & h[2:])
        h = h2
        Y2 = np.zeros(W, dtype=np.uint8)
        Y2[1:-1] = Y[:-2] ^ (Y[1:-1] | Y[2:])
        Y = Y2
        if s + 1 == 300:
            dmg = Y ^ X[t0 + s + 1]
            nz = np.flatnonzero(dmg | h)
            lo, hi = nz.min(), nz.max()
            region = slice(lo, hi + 1)
            agree_bulk.append(np.mean(dmg[region] == h[region]))
            agree_edge.append(dmg[C + j + 300] == 1 and h[C + j + 300] == 1)
    lams.append(logsum / S)
print(f'T2  sensitivity-path growth per step from five cells: ' + ' '.join(f'{v:.4f}' for v in lams) +
      f' (ln 2 = {np.log(2):.4f})')
print(f'    tangent mod 2 versus actual damage after 300 steps: agreement over the damage region ' +
      ' '.join(f'{v:.3f}' for v in agree_bulk) + f'; right-edge diagonal cell damaged in both: {agree_edge}')
# S3: Z/4 lift of the single seed
Z = np.zeros(W, dtype=np.int64)
Z[C] = 1
pairs_z = np.zeros((2, 2))
dens = []
for t in range(T):
    Z2 = np.zeros(W, dtype=np.int64)
    Z2[1:-1] = (Z[:-2] + Z[1:-1] + Z[2:] + Z[1:-1] * Z[2:]) % 4
    Z = Z2
    x = Z % 2
    assert np.array_equal(x, X[t + 1])
    H = Z >> 1
    pairs_z[x[C], H[C]] += 1
    if t + 1 >= 1000:
        lo, hi = C - (t + 1) // 2, C + (t + 1) // 2
        dens.append(H[lo:hi].mean())
pairs_z /= pairs_z.sum()
# S2: flip counter second digit on the centre column
Nc = np.zeros(W, dtype=np.int64)
Nc[C] = 1
pairs_n = np.zeros((2, 2))
for t in range(T):
    g = np.zeros(W, dtype=np.int64)
    g[1:-1] = X[t, 1:-1] | X[t, 2:]
    N2 = np.zeros(W, dtype=np.int64)
    N2[1:-1] = Nc[:-2] + g[1:-1]
    Nc = N2
    pairs_n[Nc[C] & 1, (Nc[C] >> 1) & 1] += 1
pairs_n /= pairs_n.sum()
print(f'T2  Z/4 lift of the single seed: colour reproduces Rule 30 for {T} rows; second-digit density in the middle half '
      f'(rows 1000..{T}) {np.mean(dens):.4f}')
print('    centre column (colour, second digit) frequencies, Z/4 lift: ' +
      ' '.join(f'({a},{b}) {pairs_z[a, b]:.3f}' for a in (0, 1) for b in (0, 1)))
print('    centre column (colour, second digit) frequencies, flip counter: ' +
      ' '.join(f'({a},{b}) {pairs_n[a, b]:.3f}' for a in (0, 1) for b in (0, 1)))

# ---------------- T3: the cost of a k-generation patch ----------------
KMAX = 5
NS = 4 ** KMAX
nxt = np.zeros((2, NS), dtype=np.int64)
outs = np.zeros((2, NS, KMAX), dtype=np.uint8)
for y in (0, 1):
    for s in range(NS):
        z = y
        new = 0
        for m in range(KMAX):
            a = (s >> (2 * m + 1)) & 1      # row t-m-1 at the cell just right of the output
            b = (s >> (2 * m)) & 1          # and the one beyond it
            zm = z ^ (a | b)
            outs[y, s, m] = zm
            new |= (zm << (2 * m + 1)) | (a << (2 * m))
            z = zm
        nxt[y, s] = new


def patch_cost(row, i, kmax, wmax=200):
    """least w (per k) such that row[i..i+w] fixes every ancestor of cell i to generation k."""
    res = {}
    for w in range(2, wmax):
        S = np.arange(NS)
        fixed = np.ones((w + 1, kmax), dtype=bool)     # by reading offset j - i
        for j in range(i + w, i - 1, -1):
            o = outs[row[j], S]
            fixed[j - i] = (o == o[0]).all(axis=0)[:kmax]
            S = np.unique(nxt[row[j], S])
        for k in range(1, kmax + 1):
            if k not in res and w >= 2 * k and all(fixed[jj, m - 1] for m in range(1, k + 1) for jj in range(0, 2 * m + 1)):
                res[k] = w
        if len(res) == kmax:
            return res
    return res


rng = np.random.default_rng(1279)
costs = {k: [] for k in range(1, KMAX + 1)}
for _ in range(150):
    t = int(rng.integers(1200, T + 1))
    i = int(rng.integers(C - t // 2, C + t // 2))
    r = patch_cost(X[t], i, KMAX)
    for k, v in r.items():
        costs[k].append(v)
print('T3  exact patch cost d_k over 150 interior cells (rows 1200..1500): ' +
      '; '.join(f'k={k}: mean {np.mean(v):.1f}, median {np.median(v):.0f}, max {max(v)}, n {len(v)}' for k, v in costs.items()))
ks = np.arange(1, KMAX + 1)
means = np.array([np.mean(costs[k]) for k in ks])
slope = np.polyfit(ks, means, 1)[0]
print(f'    least-squares slope of mean d_k against k: {slope:.2f}')
# T1c: reach of each founder through black parents (no tie-break), to t = 20000, rolling rows
TL = 20000
WL = 2 * TL + 5
CL = TL + 2
row = np.zeros(WL, dtype=bool)
row[CL] = True
reachL = np.zeros(WL, dtype=bool)
reachM = np.zeros(WL, dtype=bool)
reachR = np.zeros(WL, dtype=bool)
Btab, LRtab, Mtab = {}, {}, {}
Fc = np.full(W, -1, dtype=np.int64)          # the C tie-break family on the stored orbit, for the equality check
Fc[C - 1], Fc[C], Fc[C + 1] = 0, 1, 2
mismatch = 0
for t in range(1, TL + 1):
    nrow = np.zeros_like(row)
    nrow[1:-1] = row[:-2] ^ (row[1:-1] | row[2:])
    row = nrow
    if t == 1:
        reachL[CL - 1] = reachM[CL] = reachR[CL + 1] = True
    else:
        for r in (reachL, reachM, reachR):
            sp = np.zeros_like(r)
            sp[1:-1] = r[:-2] | r[1:-1] | r[2:]
            r[:] = sp & row
    if 2 <= t <= T:
        Fc = np.where(X[t] == 1, Fc[np.clip(np.arange(W) + D[t], 0, W - 1)], -1)
        bL = np.flatnonzero(reachL).max() - CL
        bC = np.flatnonzero(Fc == 0).max() - C
        mismatch += bL != bC
    if t % 1000 == 0 or t in (100, 250, 500, 1500):
        Btab[t] = np.flatnonzero(reachL).max() - CL
        LRtab[t] = np.flatnonzero(reachR).min() - CL + t
        Mtab[t] = (np.flatnonzero(reachM).min() - CL, np.flatnonzero(reachM).max() - CL) if reachM.any() else None
print(f'T1c rows 2..{T}: rightmost cell reached from the left founder differs from the C-tie-break boundary on {mismatch} rows')
print('    B(t) = rightmost black cell reached from (-1,1): ' + '; '.join(f't={t}: {b} ({b / t:.4f})' for t, b in Btab.items()))
print('    left end of the right founder\'s reach, measured from the left edge -t: ' + ' '.join(f'{t}:{v}' for t, v in LRtab.items()))
print('    reach of the middle founder (0,1) [min, max]: ' + ' '.join(f'{t}:{v}' for t, v in Mtab.items() if t in (100, 1500, 5000, 10000, 20000)))
print('GENEALOGY_SCHEMAS_DONE')
