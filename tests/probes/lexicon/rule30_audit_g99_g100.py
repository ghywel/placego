#!/usr/bin/env python3
"""rule30_audit_g99_g100.py: Local's second reading of GPT's G99 (versioned dependency evaluation preserves logical
time) and G100 (fair rows do not make rightward flips independent in time), independent of GPT's VP1 and RF1. Exact
enumeration. (Local, 2026-10-06; PROOFS.md notes; chat.)

COMMAND:    python3 tests/probes/lexicon/rule30_audit_g99_g100.py      (seconds)

CHECKS (GPT's claims at 827e006):
  S1 (G99): for N = 1..5 and every initial word on [-N, N], evaluating the triangle's nodes in three different ready
     orders (by generation, by largest site first, and a seeded random ready order) gives every node its synchronous
     value; the mixed-generation projection after only node (0, 1) from a seed at 1 is {0, 1}, not {0, 1, 2}.
  S2 (G100): at the observer p_t = t, the flip words B_0 B_1 B_2 over all 128 seven-bit initial words have counts
     [1, 3, 5, 7, 3, 9, 7, 29] x 2 both from the moving-frame map H and from literal spacetime; marginals 3/4, adjacent
     covariance 0, lag-two covariance 1/32, count variance 5/8 (iid would be 9/16).
  S3 (G101, added 2026-10-06 at 7773c41): the observer p_t = floor(3t/4) over all 512 initial words on sites -1..7,
     literal spacetime: the four-flip histogram is 4 x [1, 3, 5, 7, 3, 9, 7, 29] for each first-flip value; means
     (1/2, 3/4, 3/4, 3/4); covariance 1/32 between the second and fourth flips and 0 for the other five pairs; count
     mean 11/4 and variance 7/8 (independent flips: 13/16).
  S4 (G092's scope point on L054, exact): from sites 0..3 = 0, 0, 0, 1 (zeros elsewhere), right races at site 1 then
     site 0 make site 0 differ from the synchronous value, while site 0's isolated right-race injection is 0.
  S5 (G102, added 2026-10-06 at 84d09c9): a forced race at site 0 of a fair row, neighbour race flags at sites 1..D
     (right) or -1..-D (left) with weights eps^k (1 - eps)^(D - k), the next site synchronous; by exact enumeration of
     every old word and flag word for D = 0..5 and eps = 0, 1/100, 1/4, 1/2, 1: right injection = Q_D / 4 with
     Q_0 = 1/2, Q_D = 1/2 + (eps/2) Q_(D-1), remainder (eps/2)^(D+1) / (4 (2 - eps)) to 1/(8 - 4 eps); left = 1/2.
  S6 (G103, added 2026-10-06 at 43095bf): on rings of 3 to 5 cells, T = 1, 2 steps, every initial row and every flag
     history, both race directions with races.c's conventions: every site whose dependency cone holds no flag agrees
     with the ideal history; with exact flag weights at eps = 1/4, 1/2, 1, every site's disagreement probability is at
     most 1 - (1 - eps)^M (M the deduplicated cone size) and at most eps t^2; the final-tick guard (ring of 5, black
     cell at 2, one right race at site 0 on step 1) makes site 1 differ on step 2.
  S7 (G104, added 2026-10-06 at 8753ab0): right-reading races: for block widths 1..5, every flag pattern and every
     three-bit tail, the old bits x_0..x_(w-1) map bijectively onto y_1..y_w. Left-reading races on a fair first row:
     density 1/2 and adjacent disagreement 1/2 (right cell unflagged) or 3/4 (flagged), so 1/2 + eps/4 with exact
     weights at eps = 0, 1/4, 1/2, 1 (chains anchored at depth <= 3).
  S8 (G105, added 2026-10-06 at f0f3a1b): on rings of 3 to 7 cells, every flag word in both scan directions (races.c's
     conventions, race_step above): the all-zero new row has exactly 2 old preimages under right races, and under left
     races 1 or 2 according to whether an effective flag is present; the exact masses 2^(1-W) and
     [1 + (1 - eps)^(W-1)] 2^(-W) at eps = 0, 1/4, 1/2, 1; the all-zero row stays zero under every flag word.
  S9 (G106, added 2026-10-06 at d05bb6b): right-reading races, old words on sites -2..D+2, flags on -1..D, site D+1
     synchronous, D = 0..4, exact weights at eps = 0, 1/4, 1/2, 1: the observer's flip x_0 XOR y_delta has mean 1/2
     for delta = -1, 0 and U_D for delta = +1, with U_0 = 3/4, U_D = 3/4 - eps/4 + (eps/2) U_(D-1), and the remainder
     to (3 - eps)/(4 - 2 eps) is [eps/(8 - 4 eps)] (eps/2)^D.
  S10 (G107, added 2026-10-06 at e779bd0): for T = 1..3, every nonincreasing path (increments -1 or 0) and every
     schedule switching whole rows between synchronous and right-reading-everywhere (a synchronous right terminal),
     over all initial words on sites -2T..T+1: the sampled vector (s_0..s_T) is uniform for every path and schedule,
     so the trace is iid fair conditional on the schedule, with fully correlated rows included.
  S11 (G108, added 2026-10-06 at 85f0972): for T = 1..3, every nonincreasing path and whole-row schedule, and every
     assignment of the non-pivot initial bits: the ideal and noisy traces are each bijective images of the T + 1 pivots,
     and the mask I_t XOR J_t is a function of the ideal prefix I_0..I_(t-1) alone (causal); the guard (old 1, 2 = 0, 1,
     only the target racing) gives E_1 = 1 - I_0 for all four pivot values.
  S12 (G109, added 2026-10-06 at f9aa008): (a) every background on sites -3..3 with site 0 flipped: the source error
     over ticks 0, 1, 2 is 1, 1 - z(1), z(1) OR z(2), and delta_1(-1) = 1 - z(-1), delta_1(1) = 1, computed by an
     XOR-difference propagation (the difference of the OR term), not the truth table; (b) every old word on sites
     -3..3 with one isolated right race at site 0 on tick 1: 16 injections, each with source signature 1, 0, 1 over
     ticks 1..3, the other 112 giving 0, 0, 0; second-tick damage sets {1} and {-1, 1}, 8 each.
  S13 (G110, added 2026-10-06 at f922142): the isolated pulse over all 128 words on -3..3: in each bin K_2 = (b, 0),
     8 words with E_1 = 1 and 56 with E_1 = 0; E_3 = E_1 always; both four-sample traces uniform (16 words, 8 each).
  S14 (G112, added 2026-10-06 at 38eda50): (a) white agreement after one right-reading step, at every site of every
     ring of 3 to 6 cells, every initial row and flag word: z_1(j+1) = y_1(j+1) = 0 implies z_1(j) = y_1(j); (b) the two
     nine-node cylinders on the line (initial words 0110000 and 0000010 on -3..3, flags as stated): ideal / raced source
     traces 1100..., B occurs with E_3 = 0, and 0011 / 0110 with I_2 = 1, E_2 = 0, E_3 = 1; (c) the left-scan guard on
     a ring of 5 (initial 00001, only site 1 flagged): site 2 white in both, site 1 different.
  S15 (G113, added 2026-10-06 at 832c0d3): the isolated pulse over all 8,192 words on sites -6..6, seven samples at
     site 0: A = {K_4 = K_5 = (0, 0)} has 1,872 words with 40 giving E_6 = 1; B = A and {K_3 = (0, 0)} has 896 with 0;
     the child K_3 = (0, 1) has 40 with 20; both seven-sample traces uniform (128 words, 64 each).
"""
import random
from fractions import Fraction as F
from itertools import product

fails = []


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
    if not ok:
        fails.append(name)


R30 = lambda l, c, r: l ^ (c | r)
rng = random.Random(99)
ok = True
for N in range(1, 6):
    nodes = [(i, k) for k in range(1, N + 1) for i in range(-(N - k), N - k + 1)]
    for s in range(2 ** (2 * N + 1)):
        x0 = {i: (s >> (i + N)) & 1 for i in range(-N, N + 1)}
        sync = {(i, 0): x0[i] for i in x0}
        for k in range(1, N + 1):
            for i in range(-(N - k), N - k + 1):
                sync[(i, k)] = R30(sync[(i - 1, k - 1)], sync[(i, k - 1)], sync[(i + 1, k - 1)])
        for order in ('generation', 'largest-site', 'random'):
            store = {(i, 0): x0[i] for i in x0}
            todo = set(nodes)
            while todo:
                ready = [n for n in todo if all((n[0] + d, n[1] - 1) in store for d in (-1, 0, 1))]
                if order == 'generation':
                    n = min(ready, key=lambda q: (q[1], q[0]))
                elif order == 'largest-site':
                    n = max(ready, key=lambda q: (q[0], -q[1]))
                else:
                    n = rng.choice(ready)
                i, k = n
                store[n] = R30(store[(i - 1, k - 1)], store[(i, k - 1)], store[(i + 1, k - 1)])
                todo.remove(n)
            ok &= all(store[n] == sync[n] for n in nodes)
seed = {1}
latest = {i: int(i in seed) for i in range(-3, 4)}
latest[0] = R30(0, 0, 1)
proj = {i for i, v in latest.items() if v}
full = {i for i in range(-3, 4) if R30(int(i - 1 in seed), int(i in seed), int(i + 1 in seed))}
check('S1 three ready orders give the synchronous triangle (N <= 5, every word); mixed projection {0,1} vs {0,1,2}',
      ok and proj == {0, 1} and full == {0, 1, 2}, '%s %s' % (sorted(proj), sorted(full)))
cH, cL = [0] * 8, [0] * 8
for s in range(128):
    x = [(s >> i) & 1 for i in range(7)]
    z, B = x[:], []
    for t in range(3):
        B.append(z[1] | z[2])
        z = [z[j] ^ (z[j + 1] | z[j + 2]) for j in range(len(z) - 2)]
    cH[B[0] * 4 + B[1] * 2 + B[2]] += 1
    rows = [{i: x[i] for i in range(7)}]
    for t in range(3):
        p = rows[-1]
        rows.append({i: R30(p[i - 1], p[i], p[i + 1]) for i in p if i - 1 in p and i + 1 in p})
    Bl = [rows[t + 1][t + 1] ^ rows[t][t] for t in range(3)]
    cL[Bl[0] * 4 + Bl[1] * 2 + Bl[2]] += 1
P = lambda w: F(cH[w], 128)
m = [sum(P(w) for w in range(8) if (w >> (2 - k)) & 1) for k in range(3)]
c01 = sum(P(w) for w in range(8) if (w >> 2) & 1 and (w >> 1) & 1) - m[0] * m[1]
c02 = sum(P(w) for w in range(8) if (w >> 2) & 1 and w & 1) - m[0] * m[2]
var = sum(P(w) * bin(w).count('1') ** 2 for w in range(8)) - sum(P(w) * bin(w).count('1') for w in range(8)) ** 2
check('S2 counts, marginals 3/4, cov 0 and 1/32, variance 5/8 (not 9/16); H agrees with literal spacetime',
      [c // 2 for c in cH] == [1, 3, 5, 7, 3, 9, 7, 29] and cH == cL and m == [F(3, 4)] * 3 and c01 == 0
      and c02 == F(1, 32) and var == F(5, 8) and var != F(9, 16), str([c // 2 for c in cH]))
hist = {}
for s_ in range(512):
    x = {i - 1: (s_ >> i) & 1 for i in range(9)}
    rows = [x]
    for t in range(4):
        q = rows[-1]
        rows.append({i: R30(q[i - 1], q[i], q[i + 1]) for i in q if i - 1 in q and i + 1 in q})
    pos = [(3 * t) // 4 for t in range(5)]
    B = tuple(rows[t + 1][pos[t + 1]] ^ rows[t][pos[t]] for t in range(4))
    hist[B] = hist.get(B, 0) + 1
Pw = lambda w: F(hist.get(w, 0), 512)
words = [tuple((v >> (3 - k)) & 1 for k in range(4)) for v in range(16)]
mean = [sum(Pw(w) * w[k] for w in words) for k in range(4)]
cov = {(a, b): sum(Pw(w) * w[a] * w[b] for w in words) - mean[a] * mean[b] for a in range(4) for b in range(a + 1, 4)}
cm = sum(Pw(w) * sum(w) for w in words)
cv = sum(Pw(w) * sum(w) ** 2 for w in words) - cm ** 2
tri = [1, 3, 5, 7, 3, 9, 7, 29]
ok3 = all(hist.get((b0,) + tuple((v >> (2 - k)) & 1 for k in range(3)), 0) == 4 * tri[v] for b0 in (0, 1) for v in range(8))
check('S3 G101: histogram 4 x G100 triple for each first flip; means; covariances; count mean 11/4, variance 7/8',
      ok3 and mean == [F(1, 2)] + [F(3, 4)] * 3 and cov[(1, 3)] == F(1, 32)
      and all(v == 0 for k, v in cov.items() if k != (1, 3)) and cm == F(11, 4) and cv == F(7, 8) and cv != F(13, 16),
      'variance %s' % cv)
row = {0: 0, 1: 0, 2: 0, 3: 1, 4: 0, -1: 0}
sync = {i: R30(row.get(i - 1, 0), row[i], row.get(i + 1, 0)) for i in range(0, 4)}
new = {}
for i in (3, 2):
    new[i] = R30(row.get(i - 1, 0), row[i], row.get(i + 1, 0))
new[1] = R30(row[0], row[1], new[2])          # right race at site 1 reads the new site 2
new[0] = R30(row[-1], row[0], new[1])         # right race at site 0 reads the raced site 1
iso0 = (1 - row[0]) & (sync[1] ^ row[1])      # isolated injection at site 0: NOT x_0 AND (synchronous change of site 1)
check('S4 G092: chained right races make site 0 differ though its isolated injection is 0',
      new[0] != sync[0] and iso0 == 0, 'sync %d raced %d' % (sync[0], new[0]))
def chain(D, eps, side):
    """Exact injection probability at site 0 under a forced race, D neighbour flags, as a Fraction."""
    tot = F(0)
    n = D + 4                                     # old sites -(D+2) .. (D+2) suffice for both sides
    sites = list(range(-(D + 2), D + 3))
    for w in range(2 ** len(sites)):
        old = {sites[k]: (w >> k) & 1 for k in range(len(sites))}
        for fl in range(2 ** D):
            flags = [(fl >> k) & 1 for k in range(D)]
            weight = F(1)
            for f_ in flags:
                weight *= eps if f_ else 1 - eps
            new = {}
            if side == 'R':
                # site D+1 synchronous; sites D..1 race if flagged (read the new right neighbour); site 0 forced race
                new[D + 1] = R30(old[D], old[D + 1], old[D + 2])
                for i in range(D, 0, -1):
                    rr = new[i + 1] if flags[i - 1] else old[i + 1]
                    new[i] = R30(old[i - 1], old[i], rr)
                raced = R30(old[-1], old[0], new[1])
            else:
                new[-(D + 1)] = R30(old[-(D + 2)], old[-(D + 1)], old[-D])
                for i in range(-D, 0):
                    ll = new[i - 1] if flags[-i - 1] else old[i - 1]
                    new[i] = R30(ll, old[i], old[i + 1])
                raced = R30(new[-1], old[0], old[1])
            sync = R30(old[-1], old[0], old[1])
            tot += weight * (raced != sync)
    return tot / 2 ** len(sites)


ok5 = True
for eps in (F(0), F(1, 100), F(1, 4), F(1, 2), F(1)):
    Q = F(1, 2)
    for D in range(0, 6):
        if D > 0:
            Q = F(1, 2) + eps / 2 * Q
        r_, l_ = chain(D, eps, 'R'), chain(D, eps, 'L')
        lim = 1 / (8 - 4 * eps)
        ok5 &= r_ == Q / 4 and lim - r_ == (eps / 2) ** (D + 1) / (4 * (2 - eps)) and l_ == F(1, 2)
check('S5 G102: right chain Q_D/4 with the stated remainder; left 1/2 (D <= 5; eps = 0, 1/100, 1/4, 1/2, 1)', ok5,
      'q at eps = 1/100: %.5f' % float(1 / (8 - 4 * F(1, 100))))
def race_step(row, flags, mode):
    W_ = len(row)
    new = [0] * W_
    order = range(W_) if mode == 'L' else range(W_ - 1, -1, -1)
    for i in order:
        l = row[(i - 1) % W_]
        r = row[(i + 1) % W_]
        if flags[i] and mode == 'L' and i > 0:
            l = new[i - 1]
        if flags[i] and mode == 'R' and i < W_ - 1:
            r = new[i + 1]
        new[i] = R30(l, row[i], r)
    return new


def ideal_step(row):
    W_ = len(row)
    return [R30(row[(i - 1) % W_], row[i], row[(i + 1) % W_]) for i in range(W_)]


ok6 = True
for W_ in range(3, 6):
    for T_ in (1, 2):
        cones = {}
        for i in range(W_):
            cone = set()
            for s_ in range(1, T_ + 1):
                for d in range(-(T_ - s_), T_ - s_ + 1):
                    cone.add(((i + d) % W_, s_))
            cones[i] = cone
        for mode in 'LR':
            prob = {e: [F(0)] * W_ for e in (F(1, 4), F(1, 2), F(1))}
            for r0 in range(2 ** W_):
                row0 = [(r0 >> k) & 1 for k in range(W_)]
                ideal = row0
                for _ in range(T_):
                    ideal = ideal_step(ideal)
                for fh in range(2 ** (W_ * T_)):
                    flags = [[(fh >> (s_ * W_ + k)) & 1 for k in range(W_)] for s_ in range(T_)]
                    row = row0
                    for s_ in range(T_):
                        row = race_step(row, flags[s_], mode)
                    nf = bin(fh).count('1')
                    for i in range(W_):
                        clean = all(not flags[s_ - 1][j] for (j, s_) in cones[i])
                        if clean and row[i] != ideal[i]:
                            ok6 = False
                        if row[i] != ideal[i]:
                            for e in prob:
                                prob[e][i] += e ** nf * (1 - e) ** (W_ * T_ - nf) / 2 ** W_
            for e in prob:
                for i in range(W_):
                    M = len(cones[i])
                    ok6 &= prob[e][i] <= 1 - (1 - e) ** M and prob[e][i] <= min(1, e * T_ ** 2)
row = [0, 0, 1, 0, 0]
r1 = race_step(row, [1, 0, 0, 0, 0], 'R')
r2 = race_step(r1, [0] * 5, 'R')
i2 = ideal_step(ideal_step(row))
check('S6 G103: clean cones agree; disagreement within both bounds (rings 3..5, T <= 2, both directions); final-tick '
      'guard', ok6 and r1 == [1, 1, 1, 1, 0] and r2[1] != i2[1], 'raced step 1 %s' % r1)
ok7 = True
for w in range(1, 6):
    for fl in range(2 ** w):
        r = {i: (fl >> (i - 1)) & 1 for i in range(1, w + 1)}
        for tail in range(8):
            tx = {w: tail & 1, w + 1: (tail >> 1) & 1, w + 2: (tail >> 2) & 1}
            outs = set()
            for ob in range(2 ** w):
                x = dict(tx)
                for i in range(w):
                    x[i] = (ob >> i) & 1
                y = {w + 1: R30(x[w], x[w + 1], x[w + 2])}
                for i in range(w, 0, -1):
                    y[i] = R30(x[i - 1], x[i], y[i + 1] if r[i] else x[i + 1])
                outs.add(tuple(y[i] for i in range(1, w + 1)))
            ok7 &= len(outs) == 2 ** w
lefts = {}
for D in range(0, 4):
    # sites -(D+1) .. 3 old; target pair (1, 2); flags at sites 1-D .. 2 (site 2 is the pair's right cell)
    sites = list(range(-(D + 1), 4))
    flag_sites = list(range(1 - D, 3))
    for e in (F(0), F(1, 4), F(1, 2), F(1)):
        dens = F(0)
        dis = F(0)
        for xw in range(2 ** len(sites)):
            x = {sites[k]: (xw >> k) & 1 for k in range(len(sites))}
            for fw in range(2 ** len(flag_sites)):
                r = {flag_sites[k]: (fw >> k) & 1 for k in range(len(flag_sites))}
                r[1 - D] = 0                         # anchor: the chain's leftmost site reads an old bit
                nf = sum(r[k] for k in flag_sites)
                wt = e ** nf * (1 - e) ** (len(flag_sites) - 1 - nf) if True else 0
                if (fw & 1):                          # anchored site forced unflagged: skip the flagged half
                    continue
                y = {}
                for i in range(1 - D, 3):
                    y[i] = R30(y[i - 1] if r[i] and (i - 1) in y else x[i - 1], x[i], x[i + 1])
                dens += wt * y[1]
                dis += wt * (y[1] ^ y[2])
        tot = 2 ** len(sites)
        lefts[(D, e)] = (dens / tot, dis / tot)
ok7 &= all(v[0] == F(1, 2) and v[1] == F(1, 2) + e / 4 for (D, e), v in lefts.items() if D >= 1)
check('S7 G104: right-reading block bijection (widths <= 5); left first-row density 1/2, pairs 1/2 + eps/4', ok7,
      'depth 3: %s' % {str(e): str(lefts[(3, e)][1]) for e in (F(0), F(1, 4), F(1, 2), F(1))})
ok8 = True
for W_ in range(3, 8):
    for mode in 'LR':
        mass = {e: F(0) for e in (F(0), F(1, 4), F(1, 2), F(1))}
        for fw in range(2 ** W_):
            flags = [(fw >> k) & 1 for k in range(W_)]
            eff = any(flags[1:]) if mode == 'L' else any(flags[:W_ - 1])
            pre = sum(1 for r0 in range(2 ** W_) if not any(race_step([(r0 >> k) & 1 for k in range(W_)], flags, mode)))
            want = 2 if mode == 'R' else (1 if eff else 2)
            ok8 &= pre == want and not any(race_step([0] * W_, flags, mode))
            nf = sum(flags)
            for e in mass:
                mass[e] += e ** nf * (1 - e) ** (W_ - nf) * F(pre, 2 ** W_)
        for e in mass:
            ok8 &= mass[e] == (F(2, 2 ** W_) if mode == 'R' else (1 + (1 - e) ** (W_ - 1)) / 2 ** W_)
check('S8 G105: zero-row preimages 2 (right), 1 or 2 (left); exact masses; the zero row stays zero (rings 3..7)', ok8)
ok9 = True
for D in range(0, 5):
    sites = list(range(-2, D + 3))
    fsites = list(range(-1, D + 1))
    for e in (F(0), F(1, 4), F(1, 2), F(1)):
        mean = {-1: F(0), 0: F(0), 1: F(0)}
        for xw in range(2 ** len(sites)):
            x = {sites[k]: (xw >> k) & 1 for k in range(len(sites))}
            for fw in range(2 ** len(fsites)):
                r = {fsites[k]: (fw >> k) & 1 for k in range(len(fsites))}
                nf = sum(r.values())
                wt = e ** nf * (1 - e) ** (len(fsites) - nf)
                y = {D + 1: R30(x[D], x[D + 1], x[D + 2])}
                for i in range(D, -2, -1):
                    y[i] = R30(x[i - 1], x[i], y[i + 1] if r[i] else x[i + 1])
                for d in (-1, 0, 1):
                    mean[d] += wt * (x[0] ^ y[d])
        tot = 2 ** len(sites)
        U = F(3, 4)
        for _ in range(D):
            U = F(3, 4) - e / 4 + e / 2 * U
        lim = (3 - e) / (4 - 2 * e)
        ok9 &= mean[-1] / tot == F(1, 2) and mean[0] / tot == F(1, 2) and mean[1] / tot == U
        ok9 &= lim - U == e / (8 - 4 * e) * (e / 2) ** D
check('S9 G106: flip means 1/2, 1/2 and U_D with the stated remainder (D <= 4; eps = 0, 1/4, 1/2, 1)', ok9,
      'eps = 1/2 limit %s' % ((3 - F(1, 2)) / (4 - 2 * F(1, 2))))
ok10 = True
for T_ in range(1, 4):
    lo0, hi0 = -2 * T_, T_ + 1
    nb = hi0 - lo0 + 1
    for path in product((-1, 0), repeat=T_):
        pos = [0]
        for d in path:
            pos.append(pos[-1] + d)
        for sched in product((0, 1), repeat=T_):
            cnt = {}
            for w in range(2 ** nb):
                row = {lo0 + k: (w >> k) & 1 for k in range(nb)}
                lo, hi = lo0, hi0
                samp = [row[0]]
                for t in range(T_):
                    new = {}
                    new[hi - 1] = R30(row[hi - 2], row[hi - 1], row[hi])
                    for i in range(hi - 2, lo, -1):
                        rr = new[i + 1] if sched[t] else row[i + 1]
                        new[i] = R30(row[i - 1], row[i], rr)
                    row, lo, hi = new, lo + 1, hi - 1
                    samp.append(row[pos[t + 1]])
                cnt[tuple(samp)] = cnt.get(tuple(samp), 0) + 1
            ok10 &= len(cnt) == 2 ** (T_ + 1) and len(set(cnt.values())) == 1
check('S10 G107: nonincreasing traces uniform under every whole-row race schedule (T <= 3)', ok10)
def trace(row0, lo0, hi0, pos, sched):
    row, lo, hi = dict(row0), lo0, hi0
    out = [row[pos[0]]]
    for t in range(len(sched)):
        new = {hi - 1: R30(row[hi - 2], row[hi - 1], row[hi])}
        for i in range(hi - 2, lo, -1):
            new[i] = R30(row[i - 1], row[i], new[i + 1] if sched[t] else row[i + 1])
        row, lo, hi = new, lo + 1, hi - 1
        out.append(row[pos[t + 1]])
    return out


ok11 = True
for T_ in range(1, 4):
    lo0, hi0 = -2 * T_, T_ + 1
    for path in product((-1, 0), repeat=T_):
        pos = [0]
        for d in path:
            pos.append(pos[-1] + d)
        piv = [pos[t] - t for t in range(T_ + 1)]
        others = [i for i in range(lo0, hi0 + 1) if i not in piv]
        for sched in product((0, 1), repeat=T_):
            for rw in range(2 ** len(others)):
                base = {others[k]: (rw >> k) & 1 for k in range(len(others))}
                Is, Js, mask = set(), set(), {}
                for pw in range(2 ** (T_ + 1)):
                    row = dict(base)
                    for k in range(T_ + 1):
                        row[piv[k]] = (pw >> k) & 1
                    I = trace(row, lo0, hi0, pos, (0,) * T_)
                    J = trace(row, lo0, hi0, pos, sched)
                    Is.add(tuple(I))
                    Js.add(tuple(J))
                    for t in range(T_ + 1):
                        key = (t, tuple(I[:t]))
                        e = I[t] ^ J[t]
                        if mask.setdefault(key, e) != e:
                            ok11 = False
                ok11 &= len(Is) == 2 ** (T_ + 1) and len(Js) == 2 ** (T_ + 1)
g_ok = True
for xm1 in (0, 1):
    for x0 in (0, 1):
        x = {-1: xm1, 0: x0, 1: 0, 2: 1, -2: 0, 3: 0}
        I1 = R30(x[-1], x[0], x[1])
        y1 = R30(x[0], x[1], x[2])
        J1 = R30(x[-1], x[0], y1)
        g_ok &= (I1 ^ J1) == 1 - x0
check('S11 G108: both traces bijective in the pivots, the mask causal in the ideal prefix (T <= 3); E_1 = 1 - I_0',
      ok11 and g_ok)
def diff_step(z, d, lo, hi):
    """Synchronous step of a background z and its difference d, by the difference of the OR term."""
    nz, nd = {}, {}
    for i in range(lo + 1, hi):
        nz[i] = R30(z[i - 1], z[i], z[i + 1])
        orz = z[i] | z[i + 1]
        orw = (z[i] ^ d[i]) | (z[i + 1] ^ d[i + 1])
        nd[i] = d[i - 1] ^ orz ^ orw
    return nz, nd


ok12 = True
for w in range(2 ** 7):
    z = {i: (w >> (i + 3)) & 1 for i in range(-3, 4)}
    d = {i: int(i == 0) for i in range(-3, 4)}
    z1, d1 = diff_step(z, d, -3, 3)
    z2, d2 = diff_step(z1, d1, -2, 2)
    ok12 &= (d[0], d1[0], d2[0]) == (1, 1 - z[1], z[1] | z[2])
    ok12 &= d1[-1] == 1 - z[-1] and d1[1] == 1
inj = 0
sets = {}
for w in range(2 ** 7):
    x = {i: (w >> (i + 3)) & 1 for i in range(-3, 4)}
    ideal1 = {i: R30(x[i - 1], x[i], x[i + 1]) for i in range(-2, 3)}
    raced1 = dict(ideal1)
    raced1[0] = R30(x[-1], x[0], ideal1[1])        # site 1 synchronous, already computed; only site 0 races
    def sync(r, lo, hi):
        return {i: R30(r[i - 1], r[i], r[i + 1]) for i in range(lo, hi + 1)}
    i2, r2 = sync(ideal1, -1, 1), sync(raced1, -1, 1)
    i3, r3 = sync(i2, 0, 0), sync(r2, 0, 0)
    sig = (ideal1[0] ^ raced1[0], i2[0] ^ r2[0], i3[0] ^ r3[0])
    if sig[0]:
        inj += 1
        ok12 &= sig == (1, 0, 1)
        dset = tuple(i for i in (-1, 0, 1) if i2[i] != r2[i])
        sets[dset] = sets.get(dset, 0) + 1
    else:
        ok12 &= sig == (0, 0, 0)
check('S12 G109: single-flip kernel by XOR-difference propagation; 16 injections, all 1, 0, 1; damage sets',
      ok12 and inj == 16 and sets == {(1,): 8, (-1, 1): 8}, 'injections %d, sets %s' % (inj, sets))
bins = {}
hI, hJ = {}, {}
ok13 = True
for w in range(2 ** 7):
    x = {i: (w >> (i + 3)) & 1 for i in range(-3, 4)}
    ideal1 = {i: R30(x[i - 1], x[i], x[i + 1]) for i in range(-2, 3)}
    raced1 = dict(ideal1)
    raced1[0] = R30(x[-1], x[0], ideal1[1])
    def sync(r, lo, hi):
        return {i: R30(r[i - 1], r[i], r[i + 1]) for i in range(lo, hi + 1)}
    i2, r2 = sync(ideal1, -1, 1), sync(raced1, -1, 1)
    i3, r3 = sync(i2, 0, 0), sync(r2, 0, 0)
    I = (x[0], ideal1[0], i2[0], i3[0])
    J = (x[0], raced1[0], r2[0], r3[0])
    E = tuple(a ^ b for a, b in zip(I, J))
    ok13 &= E[2] == 0 and E[3] == E[1]
    key = (I[2], E[2], E[1])
    bins[key] = bins.get(key, 0) + 1
    hI[I] = hI.get(I, 0) + 1
    hJ[J] = hJ.get(J, 0) + 1
ok13 &= all(bins.get((b, 0, 1), 0) == 8 and bins.get((b, 0, 0), 0) == 56 for b in (0, 1))
ok13 &= len(hI) == 16 and set(hI.values()) == {8} and len(hJ) == 16 and set(hJ.values()) == {8}
check('S13 G110: bins 8 and 56 per ideal bit, E_3 = E_1, both traces uniform', ok13, str(sorted(bins.items())))
ok14 = True
for W_ in range(3, 7):
    for r0 in range(2 ** W_):
        x = [(r0 >> k) & 1 for k in range(W_)]
        z = ideal_step(x)
        for fw in range(2 ** W_):
            fl = [(fw >> k) & 1 for k in range(W_)]
            y = race_step(x, fl, 'R')
            for j in range(W_):
                j1 = (j + 1) % W_
                if z[j1] == 0 and y[j1] == 0 and z[j] != y[j]:
                    ok14 = False


def line_cyl(word, flag_t1_site0):
    x = {i - 3: int(word[i]) for i in range(7)}
    z1 = {i: R30(x[i - 1], x[i], x[i + 1]) for i in range(-2, 3)}
    y1 = {}
    for i in range(2, -3, -1):                     # right-to-left scan on the cone's tick-1 nodes
        rr = y1[i + 1] if (i == 0 and flag_t1_site0) else x[i + 1]
        y1[i] = R30(x[i - 1], x[i], rr)
    z2 = {i: R30(z1[i - 1], z1[i], z1[i + 1]) for i in range(-1, 2)}
    y2 = {i: R30(y1[i - 1], y1[i], y1[i + 1]) for i in range(-1, 2)}
    z3 = R30(z2[-1], z2[0], z2[1])
    y3 = R30(y2[-1], y2[0], y2[1])
    return (x[0], z1[0], z2[0], z3), (x[0], y1[0], y2[0], y3)


I_, J_ = line_cyl('0110000', False)
E_ = [a ^ b for a, b in zip(I_, J_)]
ok14 &= I_[1] == 1 and I_[2] == 1 and E_[1] == 0 and E_[2] == 0 and E_[3] == 0
I_, J_ = line_cyl('0000010', True)
E_ = [a ^ b for a, b in zip(I_, J_)]
ok14 &= I_ == (0, 0, 1, 1) and J_ == (0, 1, 1, 0) and I_[2] == 1 and E_[2] == 0 and E_[3] == 1
x5 = [0, 0, 0, 0, 1]
z5 = ideal_step(x5)
y5 = race_step(x5, [0, 1, 0, 0, 0], 'L')
ok14 &= z5[2] == 0 and y5[2] == 0 and z5[1] != y5[1]
check('S14 G112: white agreement (rings 3..6, right scan); both cylinders; the left-scan guard', ok14)
cntA = sA = cntB = sB = cntC = sC = 0
hI7, hJ7 = {}, {}
for w in range(2 ** 13):
    x = {i: (w >> (i + 6)) & 1 for i in range(-6, 7)}
    zr = dict(x)
    yr = dict(x)
    I7, J7 = [x[0]], [x[0]]
    for t in range(1, 7):
        lo, hi = -6 + t, 6 - t
        nz = {i: R30(zr[i - 1], zr[i], zr[i + 1]) for i in range(lo, hi + 1)}
        if t == 1:
            ny = {i: R30(yr[i - 1], yr[i], yr[i + 1]) for i in range(lo, hi + 1)}
            ny[0] = R30(yr[-1], yr[0], ny[1])           # the pulse: site 0 reads its updated right neighbour
        else:
            ny = {i: R30(yr[i - 1], yr[i], yr[i + 1]) for i in range(lo, hi + 1)}
        zr, yr = nz, ny
        I7.append(zr[0])
        J7.append(yr[0])
    E7 = [a ^ b for a, b in zip(I7, J7)]
    K = [(I7[t], E7[t]) for t in range(7)]
    hI7[tuple(I7)] = hI7.get(tuple(I7), 0) + 1
    hJ7[tuple(J7)] = hJ7.get(tuple(J7), 0) + 1
    if K[4] == (0, 0) and K[5] == (0, 0):
        cntA += 1
        sA += E7[6]
        if K[3] == (0, 0):
            cntB += 1
            sB += E7[6]
        if K[3] == (0, 1):
            cntC += 1
            sC += E7[6]
check('S15 G113: A 1872 with 40, B 896 with 0, child (0,1) 40 with 20; traces uniform',
      (cntA, sA, cntB, sB, cntC, sC) == (1872, 40, 896, 0, 40, 20) and len(hI7) == 128 and set(hI7.values()) == {64}
      and len(hJ7) == 128 and set(hJ7.values()) == {64}, str((cntA, sA, cntB, sB, cntC, sC)))
print('ALL CHECKS PASS' if not fails else 'FAILED: ' + ', '.join(fails))
