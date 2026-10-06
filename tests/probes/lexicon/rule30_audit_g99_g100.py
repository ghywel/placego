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
  S16 (G114, added 2026-10-06 at 9e09890): the expanded difference identity delta = p XOR (1-c) q XOR (1-b) r XOR q r
     against the truth table on all 64 triples; the cylinder 0011110010000 on -6..6 with the pulse gives ideal / noisy
     rows 1010101 / 1111011 (tick 3), 01010 / 00001 (tick 4), 101 / 001 (tick 5), incoming source errors (1, 1) at
     tick 4 and (1, 0) at tick 5; the black-centre guard (p = q = 0, r = 1) gives 0, not Rule 90's 1.
  S17 (G115, G116, added 2026-10-06 at 241fb49): over the 8,192 pulse words, the candidate X_5 = (F, K_4, K_5) with
     F = E_1: parent (1, (0,0), (0,0)) has 80 words with 40 next errors, its full-history child
     ((0,0),(0,1),(0,0),(0,1),(0,0),(0,0)) has 20 with none; 24 full-history children of 112 differ from their parent's
     rate (18 parents); adding only K_3 to X_5 splits nothing. And E_4 = F (I_1 XOR I_2 XOR I_3) on every word; on these
     8,192 words (16 times G116's 512) 1,024 injections, 512 fourth errors, each (I_2, I_3) bin 256 histories with 128
     errors (the first run compared with G116's unscaled 64, 32 and 16/8 and failed for that reason only).
  S18 (G117, added 2026-10-06 at 6c4792e): over the 2,048 pulse words on sites -5..5: the fifth error equals G117's
     formula in (I_1, I_2, I_3, I_4, D), D = x(3) (x(4) OR x(5)), on every injected word and is 0 otherwise; 256
     injections, 152 fifth errors; each injected ideal quadruple occurs 16 times, D = 1 in 6; the per-quadruple error
     counts have histogram {0: 2, 16: 6, 6: 6, 10: 2}; the all-zero quadruple has E_5 = D.
  S19 (G118, added 2026-10-06 at 8ced884): over the 2,048 pulse words, six samples each: both marginal traces 64 x 32;
     the joint histogram {32: 32, 24: 32, 8: 16, 5: 16, 3: 16}, 112 distinct pairs; each ideal trace beginning 0 has 8
     injections among 32, beginning 1 none; H(A, B) and MI(A; B) from the counts equal 6 + h2(1/4)/2 + h2(3/8)/16 and
     6 - h2(1/4)/2 - h2(3/8)/16 to 1e-12.
  S20 (G119, added 2026-10-06 at 439744b): on the 2,048 pulse words, for t = 0..5, the prefix mutual information M_t
     equals (t + 1) - sum_(s <= t) H(E_s | paired past), every quantity computed from exact counts; and the two toys:
     the positive control gives M = 1, 2 - h2(1/4), 3 - h2(1/4), the cross-copy reuse guard gives M = 1, 1, 3 while
     its last error is known from the paired past (so the identity would wrongly give 2 there).
  S21 (G120, added 2026-10-06 at 9f37d68): on the real pulse traces, H(E_t | paired past) <= 1/8 for t = 2..5 (the
     values are 0, 0, 0 and h2(3/8)/16); the positive toy's final error entropy is 1/8 (the bound tight), and the hidden
     event guard's is h2(1/8)/2 > 1/8 while its prefix information still obeys G119's identity.
  S22 (G121, G122, added 2026-10-06 at 65e0261): every finite word of span w grows to span w + 2 (w <= 14); images of
     distinct words are distinct; for w = 4..16 exactly 2^(w-4) of the 2^(w-2) normalized span-w words have a finite
     predecessor (three quarters are roots), and 101 is a root at w = 3; the canonical right-quiescent predecessor of
     the single black cell has an all-black left tail, and its own predecessor a left tail of period 3 with bits 001
     up to phase; applying Rule 30 to each returns the row it came from.
  S23 (G123, G124, added 2026-10-06 at 9da67fb): (a) on every ring of N = 1..16 cells, every state that reaches zero
     has least spatial period 1 or 3 * 2^k, and periods 3, 6 and 12 all occur (N = 12); (b) the single cell's canonical
     ancestors x_1..x_12, computed on a long window, have far-left tails whose least periods p_n are 1, 3, then 3 * 2^k,
     with p_(n-1) dividing p_n, p_n >= ceil(log2(n + 1)), and Rule 30 mapping each tail to the previous one; (c) the
     cyclic trajectory 001010 -> 011011 -> 010010 -> 111111 -> 000000.
  S24 (G125, added 2026-10-06 at 0c1c83f): for m = 1..10, the recurrent states of the m-cell ring map to track pairs
     (sites 0, 1) that H^m returns exactly, distinct states giving distinct pairs; for m = 1..4, a brute-force count of
     H^m-fixed pairs among all temporally periodic track pairs of period L (L the lcm of the ring's cycle lengths),
     made without the ring correspondence, equals the number of recurrent states; H(1, 1) = (0, 1).
  S25 (G126, added 2026-10-06 at 1a5a291): the ternary map T (decode a code to its pair in H's image, apply H, encode),
     built from G22's definitions: (a) no ternary predecessor window of length k + 2 maps onto any of the six forbidden
     words (length k), a local check with no periodicity; (b) for every period p = 1..8, the periodic targets with a
     p-periodic predecessor are exactly the periodic words avoiding the six words cyclically; (c) the local section R
     gives T(R(z)) = z for every such word; (d) 0220 has predecessor 2210 and 112 has none. (The first run failed
     only at p = 2 because the cyclic-avoidance test unrolled the word too few times to see 0202 inside 2020; fixed.)
  S26 (G127, G128, added 2026-10-06 at 81fb4fd): T on the period-two points 00, 11, 22, 12, 21 gives 00, 22, 11, 22, 22;
     0102 lies in Y and maps to 1212; the full-shift precursor blocks of the target prefix 022000 are exactly the six
     listed, all beginning 22100, and those of 022001 also all begin 22100; (022000) repeated lies in Y. For G128:
     every binary word of length N <= 11 is the trace of site 0 over times 0..N-1 for some finite initial row (solved
     leftwards); the spatial checkerboard is fixed by Rule 30; the pair (alternating, all ones) is not in H's image.
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
ok16 = True
for a_, b_, c_, p_, q_, r_ in product((0, 1), repeat=6):
    lit = R30(a_, b_, c_) ^ R30(a_ ^ p_, b_ ^ q_, c_ ^ r_)
    ok16 &= lit == p_ ^ ((1 - c_) & q_) ^ ((1 - b_) & r_) ^ (q_ & r_)
word = '0011110010000'
x = {i - 6: int(word[i]) for i in range(13)}
zr, yr = dict(x), dict(x)
rows = {}
for t in range(1, 6):
    lo, hi = -6 + t, 6 - t
    nz = {i: R30(zr[i - 1], zr[i], zr[i + 1]) for i in range(lo, hi + 1)}
    ny = {i: R30(yr[i - 1], yr[i], yr[i + 1]) for i in range(lo, hi + 1)}
    if t == 1:
        ny[0] = R30(yr[-1], yr[0], ny[1])
    zr, yr = nz, ny
    rows[t] = (zr, yr)
sl = lambda r_, lo, hi: ''.join(str(r_[i]) for i in range(lo, hi + 1))
ok16 &= (sl(rows[3][0], -3, 3), sl(rows[3][1], -3, 3)) == ('1010101', '1111011')
ok16 &= (sl(rows[4][0], -2, 2), sl(rows[4][1], -2, 2)) == ('01010', '00001')
ok16 &= (sl(rows[5][0], -1, 1), sl(rows[5][1], -1, 1)) == ('101', '001')
e4 = (rows[4][0][-1] ^ rows[4][1][-1], rows[4][0][1] ^ rows[4][1][1])
e5 = (rows[5][0][-1] ^ rows[5][1][-1], rows[5][0][1] ^ rows[5][1][1])
ok16 &= e4 == (1, 1) and e5 == (1, 0)
ok16 &= (0 ^ ((1 - 0) & 0) ^ ((1 - 1) & 1) ^ (0 & 1)) == 0 and (0 ^ 1) == 1
check('S16 G114: expanded identity on 64 triples; the cylinder rows; incoming errors (1,1), (1,0); black guard', ok16)
par, full, k3 = {}, {}, {}
ok17 = True
inj = e4s = 0
bins23 = {}
for w in range(2 ** 13):
    x = {i: (w >> (i + 6)) & 1 for i in range(-6, 7)}
    zr, yr = dict(x), dict(x)
    I7, J7 = [x[0]], [x[0]]
    for t in range(1, 7):
        lo, hi = -6 + t, 6 - t
        nz = {i: R30(zr[i - 1], zr[i], zr[i + 1]) for i in range(lo, hi + 1)}
        ny = {i: R30(yr[i - 1], yr[i], yr[i + 1]) for i in range(lo, hi + 1)}
        if t == 1:
            ny[0] = R30(yr[-1], yr[0], ny[1])
        zr, yr = nz, ny
        I7.append(zr[0])
        J7.append(yr[0])
    E7 = [a ^ b for a, b in zip(I7, J7)]
    K = tuple((I7[t], E7[t]) for t in range(7))
    Fi = E7[1]
    ok17 &= E7[4] == Fi * (I7[1] ^ I7[2] ^ I7[3])
    if Fi:
        inj += 1
        e4s += E7[4]
        b = bins23.setdefault((I7[2], I7[3]), [0, 0])
        b[0] += 1
        b[1] += E7[4]
    X = (Fi, K[4], K[5])
    for d, key in ((par, X), (full, (X, K[:6])), (k3, (X, K[3]))):
        v = d.setdefault(key, [0, 0])
        v[0] += 1
        v[1] += E7[6]
ok17 &= par[(1, (0, 0), (0, 0))] == [80, 40]
Hz = ((0, 0), (0, 1), (0, 0), (0, 1), (0, 0), (0, 0))
ok17 &= full[((1, (0, 0), (0, 0)), Hz)] == [20, 0]
uneq = sum(1 for (X, H), (n, e) in full.items() if e * par[X][0] != par[X][1] * n)
uneq3 = sum(1 for (X, k), (n, e) in k3.items() if e * par[X][0] != par[X][1] * n)
ok17 &= uneq == 24 and len(full) == 112 and len(par) == 18 and uneq3 == 0
ok17 &= inj == 64 * 16 and e4s == 32 * 16 and all(v == [256, 128] for v in bins23.values()) and len(bins23) == 4   # 8,192 words = 16 x G116's 512
check('S17 G115, G116: candidate witness 80/40 vs 20/0; 24 of 112 full-history splits, none from K_3; E_4 parity law',
      ok17, 'full splits %d of %d (parents %d), K_3 splits %d; injections %d, fourth errors %d' % (
          uneq, len(full), len(par), uneq3, inj, e4s))
ok18 = True
inj18 = e5s = 0
quad = {}
for w in range(2 ** 11):
    x = {i: (w >> (i + 5)) & 1 for i in range(-5, 6)}
    zr, yr = dict(x), dict(x)
    I6, J6 = [x[0]], [x[0]]
    for t in range(1, 6):
        lo, hi = -5 + t, 5 - t
        nz = {i: R30(zr[i - 1], zr[i], zr[i + 1]) for i in range(lo, hi + 1)}
        ny = {i: R30(yr[i - 1], yr[i], yr[i + 1]) for i in range(lo, hi + 1)}
        if t == 1:
            ny[0] = R30(yr[-1], yr[0], ny[1])
        zr, yr = nz, ny
        I6.append(zr[0])
        J6.append(yr[0])
    E6 = [u ^ v for u, v in zip(I6, J6)]
    Fi = E6[1]
    if not Fi:
        ok18 &= E6[5] == 0
        continue
    inj18 += 1
    e5s += E6[5]
    a_, b_, c_, d_ = I6[1], I6[2], I6[3], I6[4]
    Dh = x[3] & (x[4] | x[5])
    H_ = a_ ^ b_ ^ c_
    L_ = 1 ^ ((1 - b_) & (d_ ^ (c_ | (1 ^ a_ ^ b_))))
    R_ = b_ ^ Dh
    C_ = c_ ^ ((1 ^ a_ ^ b_) | (1 ^ a_ ^ Dh))
    form = L_ ^ ((1 - C_) & H_) ^ ((1 - d_) & R_) ^ (H_ & R_)
    ok18 &= E6[5] == form
    q = quad.setdefault((a_, b_, c_, d_), [0, 0, 0])
    q[0] += 1
    q[1] += Dh
    q[2] += E6[5]
    if (a_, b_, c_, d_) == (0, 0, 0, 0):
        ok18 &= E6[5] == Dh
hist = {}
for v in quad.values():
    hist[v[2]] = hist.get(v[2], 0) + 1
ok18 &= inj18 == 256 and e5s == 152 and len(quad) == 16 and all(v[0] == 16 and v[1] == 6 for v in quad.values())
ok18 &= hist == {0: 2, 16: 6, 6: 6, 10: 2}
check('S18 G117: fifth-error formula on every injected word; 256 injections, 152 errors; D-split; histogram', ok18,
      'injections %d, errors %d, histogram %s' % (inj18, e5s, dict(sorted(hist.items()))))
import math
joint, mA, mB, injA = {}, {}, {}, {}
for w in range(2 ** 11):
    x = {i: (w >> (i + 5)) & 1 for i in range(-5, 6)}
    zr, yr = dict(x), dict(x)
    A_, B_ = [x[0]], [x[0]]
    for t in range(1, 6):
        lo, hi = -5 + t, 5 - t
        nz = {i: R30(zr[i - 1], zr[i], zr[i + 1]) for i in range(lo, hi + 1)}
        ny = {i: R30(yr[i - 1], yr[i], yr[i + 1]) for i in range(lo, hi + 1)}
        if t == 1:
            ny[0] = R30(yr[-1], yr[0], ny[1])
        zr, yr = nz, ny
        A_.append(zr[0])
        B_.append(yr[0])
    A_, B_ = tuple(A_), tuple(B_)
    joint[(A_, B_)] = joint.get((A_, B_), 0) + 1
    mA[A_] = mA.get(A_, 0) + 1
    mB[B_] = mB.get(B_, 0) + 1
    ia = injA.setdefault(A_, [0, 0])
    ia[0] += 1
    ia[1] += A_[1] ^ B_[1]
jh = {}
for v in joint.values():
    jh[v] = jh.get(v, 0) + 1
Hn = lambda counts: -sum(c / 2048 * math.log2(c / 2048) for c in counts)
HAB = Hn(joint.values())
HA, HB = Hn(mA.values()), Hn(mB.values())
h2 = lambda q: -q * math.log2(q) - (1 - q) * math.log2(1 - q)
ok19 = len(mA) == 64 and set(mA.values()) == {32} and len(mB) == 64 and set(mB.values()) == {32}
ok19 &= jh == {32: 32, 24: 32, 8: 16, 5: 16, 3: 16} and len(joint) == 112
ok19 &= all(v[1] == (8 if a[0] == 0 else 0) for a, v in injA.items())
ok19 &= abs(HAB - (6 + h2(0.25) / 2 + h2(0.375) / 16)) < 1e-12 and abs((HA + HB - HAB) - (6 - h2(0.25) / 2 - h2(0.375) / 16)) < 1e-12
check('S19 G118: marginals, joint histogram, injections by I_0, H(A,B) and MI', ok19,
      'MI = %.6f bits' % (HA + HB - HAB))
def H_counts(counter, total):
    return -sum(c / total * math.log2(c / total) for c in counter.values() if c)


def prefix_MI(samples, t):
    """samples: list of (I tuple, J tuple), equally weighted. MI between prefixes of length t + 1."""
    n = len(samples)
    from collections import Counter
    cA = Counter(I[:t + 1] for I, J in samples)
    cB = Counter(J[:t + 1] for I, J in samples)
    cAB = Counter((I[:t + 1], J[:t + 1]) for I, J in samples)
    return H_counts(cA, n) + H_counts(cB, n) - H_counts(cAB, n)


def cond_err_entropy(samples, t):
    """H(E_t | K_0..K_(t-1)) from counts."""
    from collections import Counter
    n = len(samples)
    past = Counter((tuple(zip(I[:t], J[:t]))) for I, J in samples)
    joint = Counter((tuple(zip(I[:t], J[:t])), I[t] ^ J[t]) for I, J in samples)
    return H_counts(joint, n) - H_counts(past, n)


pulse = []
for w in range(2 ** 11):
    x = {i: (w >> (i + 5)) & 1 for i in range(-5, 6)}
    zr, yr = dict(x), dict(x)
    A_, B_ = [x[0]], [x[0]]
    for t in range(1, 6):
        lo, hi = -5 + t, 5 - t
        nz = {i: R30(zr[i - 1], zr[i], zr[i + 1]) for i in range(lo, hi + 1)}
        ny = {i: R30(yr[i - 1], yr[i], yr[i + 1]) for i in range(lo, hi + 1)}
        if t == 1:
            ny[0] = R30(yr[-1], yr[0], ny[1])
        zr, yr = nz, ny
        A_.append(zr[0])
        B_.append(yr[0])
    pulse.append((tuple(A_), tuple(B_)))
ok20 = True
acc = 0.0
for t in range(6):
    acc += cond_err_entropy(pulse, t)
    ok20 &= abs(prefix_MI(pulse, t) - ((t + 1) - acc)) < 1e-12
toy = []
for b in range(32):
    X0, X1, X2, U, V = [(b >> k) & 1 for k in range(5)]
    Rr = U & V
    toy.append(((X0, X1, X2), (X0, X1 ^ Rr, X2 ^ (Rr & X0))))
ok20 &= abs(prefix_MI(toy, 0) - 1) < 1e-12 and abs(prefix_MI(toy, 1) - (2 - h2(0.25))) < 1e-12
ok20 &= abs(prefix_MI(toy, 2) - (3 - h2(0.25))) < 1e-12
reuse = [((X, Y, Z), (X, Z, Y)) for X in (0, 1) for Y in (0, 1) for Z in (0, 1)]
Ms = [prefix_MI(reuse, t) for t in range(3)]
ok20 &= all(abs(a - b) < 1e-12 for a, b in zip(Ms, (1, 1, 3))) and abs(cond_err_entropy(reuse, 2)) < 1e-12
check('S20 G119: the increment identity on the pulse traces (t <= 5); positive toy; the cross-copy reuse guard', ok20,
      'pulse M_5 = %.6f' % prefix_MI(pulse, 5))
ok21 = True
vals = [cond_err_entropy(pulse, t) for t in range(2, 6)]
ok21 &= all(v <= 0.125 + 1e-12 for v in vals) and abs(vals[3] - h2(0.375) / 16) < 1e-12 and all(abs(v) < 1e-12 for v in vals[:3])
posit = []
for b in range(64):
    X0, X1, X2, U, V, Q = [(b >> k) & 1 for k in range(6)]
    Fv = (1 - X0) & (1 - U) & V
    posit.append(((X0, X1, X2), (X0, X1 ^ Fv, X2 ^ (Fv & Q))))
ok21 &= abs(cond_err_entropy(posit, 2) - 0.125) < 1e-12 and abs((prefix_MI(posit, 2) - prefix_MI(posit, 1)) - 0.875) < 1e-12
hidden = []
for b in range(32):
    X0, X1, U, V, Q = [(b >> k) & 1 for k in range(5)]
    Fv = (1 - X0) & (1 - U) & V
    hidden.append(((X0, X1), (X0, X1 ^ (Fv & Q))))
he = cond_err_entropy(hidden, 1)
ok21 &= abs(he - h2(0.125) / 2) < 1e-12 and he > 0.125
ok21 &= abs((prefix_MI(hidden, 1) - prefix_MI(hidden, 0)) - (1 - he)) < 1e-12
check('S21 G120: pulse error entropies <= 1/8 after t = 1; tight toy 1/8; hidden-event guard h2(1/8)/2', ok21,
      'pulse t = 2..5: %s; hidden %.6f' % (['%.4f' % v for v in vals], he))
def fwd_finite(bits):
    """bits: tuple with bits[0] = bits[-1] = 1 (normalized); image on positions -1..len, normalized."""
    w = len(bits)
    x = lambda i: bits[i] if 0 <= i < w else 0
    out = tuple(R30(x(i - 1), x(i), x(i + 1)) for i in range(-1, w + 1))
    return out


ok22 = True
for w in range(1, 15):
    seen = set()
    for m in range(2 ** max(0, w - 2)):
        mid = tuple((m >> k) & 1 for k in range(w - 2)) if w >= 2 else ()
        word = (1,) + mid + ((1,) if w >= 2 else ())
        img = fwd_finite(word)
        ok22 &= img[0] == 1 and img[-1] == 1 and len(img) == w + 2
        ok22 &= img not in seen
        seen.add(img)
for w in range(4, 17):
    imgs = set()
    for m in range(2 ** (w - 4)):
        mid = tuple((m >> k) & 1 for k in range(w - 4))
        imgs.add(fwd_finite((1,) + mid + (1,)))
    ok22 &= len(imgs) == 2 ** (w - 4)
ok22 &= fwd_finite((1,)) == (1, 1, 1)


def canon_pred(y, lo, hi, depth):
    """Right-quiescent predecessor of y (dict on lo..hi, zero outside), computed down to site lo - depth."""
    x = {hi + 1: 0, hi + 2: 0}
    for i in range(hi + 1, lo - depth, -1):
        x[i - 1] = y.get(i, 0) ^ (x[i] | x[i + 1])
    return x


y0 = {0: 1}
p1 = canon_pred(y0, 0, 0, 40)
tail1 = [p1[i] for i in range(-30, -10)]
ok22 &= all(b == 1 for b in tail1)
ok22 &= all(R30(p1.get(i - 1, 0), p1.get(i, 0), p1.get(i + 1, 0)) == y0.get(i, 0) for i in range(-25, 3))
p2 = {hi: 0 for hi in ()}
x = {3: 0, 4: 0}
for i in range(3, -60, -1):
    yi = p1.get(i, 1 if i < -39 else 0)
    x[i - 1] = yi ^ (x[i] | x[i + 1])
tail2 = [x[i] for i in range(-50, -20)]
per3 = all(tail2[k] == tail2[k + 3] for k in range(len(tail2) - 3)) and sorted(tail2[:3]) == [0, 0, 1]
ok22 &= per3
ok22 &= all(R30(x[i - 1], x[i], x[i + 1]) == p1.get(i, 0) for i in range(-30, 2))
check('S22 G121, G122: span growth and injectivity; root fraction 3/4; canonical tails black then period 3 (001)',
      ok22, 'second tail sample %s' % ''.join(map(str, tail2[:9])))
def least_period(seq):
    n = len(seq)
    for q in range(1, n + 1):
        if n % q == 0 and all(seq[i] == seq[(i + q) % n] for i in range(n)):
            return q
    return n


ok23 = True
allowed = lambda q: q == 1 or (q % 3 == 0 and (q // 3) & ((q // 3) - 1) == 0)
seen_periods = set()
for N in range(1, 17):
    mask = (1 << N) - 1
    nxt = []
    for st in range(1 << N):
        if N == 1:
            nxt.append(R30(st, st, st))
            continue
        l = ((st << 1) | (st >> (N - 1))) & mask
        r = ((st >> 1) | (st << (N - 1))) & mask
        nxt.append((l ^ (st | r)) & mask)
    preds = {}
    for st, t in enumerate(nxt):
        preds.setdefault(t, []).append(st)
    basin, stack = {0}, [0]
    while stack:
        u = stack.pop()
        for v in preds.get(u, []):
            if v not in basin:
                basin.add(v)
                stack.append(v)
    for st in basin:
        q = least_period([(st >> i) & 1 for i in range(N)])
        ok23 &= allowed(q)
        if N == 12:
            seen_periods.add(q)
ok23 &= {3, 6, 12} <= seen_periods
# canonical ancestors of the single cell on a long window
Wn = 6000
lo_w, hi_w = -Wn, 2
cur = {i: 0 for i in range(lo_w, hi_w + 1)}
cur[0] = 1
tails = []
for n in range(1, 13):
    x = {hi_w + 1: 0, hi_w + 2: 0}
    for i in range(hi_w + 1, lo_w, -1):
        x[i - 1] = cur.get(i, 0) ^ (x[i] | x[i + 1])
    seg = [x[i] for i in range(lo_w + 50, lo_w + 50 + 1536)]
    q = None
    for cand in range(1, 769):
        if all(seg[i] == seg[i + cand] for i in range(len(seg) - cand)):
            q = cand
            break
    tails.append(q)
    ok23 &= all(R30(x[i - 1], x[i], x[i + 1]) == cur.get(i, 0) for i in range(lo_w + 2, hi_w))
    cur = {i: x[i] for i in range(lo_w, hi_w + 1)}
import math as _m
ok23 &= tails[0] == 1 and tails[1] == 3 and all(q is not None and allowed(q) for q in tails)
ok23 &= all(tails[k] % tails[k - 1] == 0 for k in range(1, len(tails)))
ok23 &= all(tails[n - 1] >= _m.ceil(_m.log2(n + 1)) for n in range(1, 13))
traj = ['001010', '011011', '010010', '111111', '000000']
for a_, b_ in zip(traj, traj[1:]):
    v = [int(c) for c in a_]
    ok23 &= ''.join(str(R30(v[i - 1], v[i], v[(i + 1) % 6])) for i in range(6)) == b_
ok23 &= [least_period([int(c) for c in t]) for t in traj] == [6, 3, 3, 1, 1]
check('S23 G123, G124: zero-basin periods on rings to 16; canonical tail periods; the period-6 trajectory', ok23,
      'tail periods %s; periods at N = 12 %s' % (tails, sorted(seen_periods)))
def Hmap(a, b):
    """Sideways map on periodic tracks (tuples of equal length L, time index mod L)."""
    L_ = len(a)
    return tuple(a[(t + 1) % L_] ^ (a[t] | b[t]) for t in range(L_)), a


ok24 = True
from math import gcd
for m in range(1, 11):
    mask = (1 << m) - 1
    def ring_step(st):
        if m == 1:
            return R30(st, st, st)
        l = ((st << 1) | (st >> (m - 1))) & mask
        r = ((st >> 1) | (st << (m - 1))) & mask
        return (l ^ (st | r)) & mask
    nxt = [ring_step(st) for st in range(1 << m)]
    # recurrent states: on cycles
    rec = set()
    for st in range(1 << m):
        x = st
        for _ in range(1 << m):
            x = nxt[x]
        rec.add(x)
    # close: collect full cycles
    recurrent = set()
    for st in rec:
        y = nxt[st]
        while y != st:
            recurrent.add(y)
            y = nxt[y]
        recurrent.add(st)
    cyc_len = {}
    for st in recurrent:
        y, k = nxt[st], 1
        while y != st:
            y, k = nxt[y], k + 1
        cyc_len[st] = k
    Lc = 1
    for k in set(cyc_len.values()):
        Lc = Lc * k // gcd(Lc, k)
    pairs = set()
    for st in recurrent:
        rows = [st]
        for _ in range(Lc - 1):
            rows.append(nxt[rows[-1]])
        bit = lambda r_, i: (r_ >> (i % m)) & 1
        a = tuple(bit(r_, 0) for r_ in rows)
        b = tuple(bit(r_, 1) for r_ in rows)
        u, v = a, b
        for _ in range(m):
            u, v = Hmap(u, v)
        ok24 &= (u, v) == (a, b)
        pairs.add((a, b))
    ok24 &= len(pairs) == len(recurrent)
    if m <= 4 and 2 * Lc <= 20:
        cnt = 0
        for wa in range(1 << Lc):
            for wb in range(1 << Lc):
                a = tuple((wa >> t) & 1 for t in range(Lc))
                b = tuple((wb >> t) & 1 for t in range(Lc))
                u, v = a, b
                for _ in range(m):
                    u, v = Hmap(u, v)
                cnt += (u, v) == (a, b)
        ok24 &= cnt == len(recurrent)
ok24 &= Hmap((1,), (1,)) == ((0,), (1,))
check('S24 G125: recurrent ring states give exact H^m fixed pairs (m <= 10); brute-force fixed-point counts (m <= 4)', ok24)
def decode_cyc(code):
    """Ternary code (cyclic tuple) -> pair (X, Y) of H's image: Y = [code = 2], X = code where Y = 0, else 1 - Y(t+1)."""
    L_ = len(code)
    Y = tuple(1 if c == 2 else 0 for c in code)
    X = tuple(code[t] if Y[t] == 0 else 1 - Y[(t + 1) % L_] for t in range(L_))
    return X, Y


def encode(X, Y):
    return tuple(2 if Y[t] else X[t] for t in range(len(X)))


def T_cyc(code):
    X, Y = decode_cyc(code)
    L_ = len(code)
    X2 = tuple(X[(t + 1) % L_] ^ (X[t] | Y[t]) for t in range(L_))
    return encode(X2, X)


FORB = [(1, 0, 0), (1, 0, 1), (1, 1, 2), (0, 2, 1, 0), (0, 2, 1, 1), (0, 2, 0, 2)]
ok25 = True
for w in FORB:
    k = len(w)
    for pre in product((0, 1, 2), repeat=k + 2):
        Y = [1 if c == 2 else 0 for c in pre]
        X = [pre[t] if Y[t] == 0 else (1 - Y[t + 1] if t + 1 < len(pre) else None) for t in range(len(pre))]
        # target code at t: the new second track X(t) marks 2, the new first track is X(t+1) XOR (X(t) OR Y(t))
        tgt = tuple(2 if X[t] == 1 else (X[t + 1] ^ (X[t] | Y[t])) for t in range(k))
        ok25 &= tgt != w
def avoids_cyc(word):
    L_ = len(word)
    ext = word * 8            # long enough that every 4-letter window starting in the middle copy is complete
    return not any(tuple(ext[i:i + len(f)]) == f for f in FORB for i in range(L_, 2 * L_))


def section(z):
    L_ = len(z)
    C = tuple(1 if c == 2 else 0 for c in z)
    D = tuple(z[t] if C[t] == 0 else 1 - C[(t + 1) % L_] for t in range(L_))
    A = tuple((D[t] ^ C[(t + 1) % L_]) if C[t] == 0 else int(z[(t - 1) % L_] == 0) for t in range(L_))
    return tuple(2 if A[t] else C[t] for t in range(L_))


for p_ in range(1, 9):
    images = set(T_cyc(c) for c in product((0, 1, 2), repeat=p_))
    Yset = set(w for w in product((0, 1, 2), repeat=p_) if avoids_cyc(w))
    ok25 &= images == Yset
    ok25 &= all(T_cyc(section(z)) == z for z in Yset)
ok25 &= T_cyc((2, 2, 1, 0)) == (0, 2, 2, 0) and (1, 1, 2) not in set(T_cyc(c) for c in product((0, 1, 2), repeat=3))
check('S25 G126: forbidden windows have no predecessor; periodic images = Y for p <= 8; the local section inverts T', ok25)
def T_window(pre):
    """Precursor code block of length k + 2 -> target block of length k."""
    Yp = [1 if c == 2 else 0 for c in pre]
    Xp = [pre[t] if Yp[t] == 0 else (1 - Yp[t + 1] if t + 1 < len(pre) else None) for t in range(len(pre))]
    return tuple(2 if Xp[t] == 1 else (Xp[t + 1] ^ (Xp[t] | Yp[t])) for t in range(len(pre) - 2))


ok26 = True
per2 = {w: T_cyc(w) for w in [(0, 0), (1, 1), (2, 2), (1, 2), (2, 1)]}
ok26 &= per2 == {(0, 0): (0, 0), (1, 1): (2, 2), (2, 2): (1, 1), (1, 2): (2, 2), (2, 1): (2, 2)}
ok26 &= avoids_cyc((0, 1, 0, 2)) and T_cyc((0, 1, 0, 2)) == (1, 2, 1, 2) and avoids_cyc((1, 2))
pre6 = sorted(''.join(map(str, pre)) for pre in product((0, 1, 2), repeat=8) if T_window(pre) == (0, 2, 2, 0, 0, 0))
ok26 &= pre6 == ['22100000', '22100001', '22100002', '22100022', '22100220', '22100221']
pre6b = [pre for pre in product((0, 1, 2), repeat=8) if T_window(pre) == (0, 2, 2, 0, 0, 1)]
ok26 &= len(pre6b) > 0 and all(pre[:5] == (2, 2, 1, 0, 0) for pre in pre6b)
ok26 &= avoids_cyc((0, 2, 2, 0, 0, 0))
# G128: finite-window realization of every binary trace (left-permutive solving)
for Nw in range(1, 12):
    for wv in range(2 ** Nw):
        target = [(wv >> t) & 1 for t in range(Nw)]
        # unknown initial bits at sites 0, -1, ..., -(Nw-1); all other initial bits zero
        init = {}
        for k in range(Nw):
            # choose x_0(-k) so that the site-0 sample at time k matches
            for guess in (0, 1):
                init[-k] = guess
                row = {i: init.get(i, 0) for i in range(-Nw - 1, Nw + 2)}
                for t in range(k):
                    row = {i: R30(row[i - 1], row[i], row[i + 1]) for i in range(-Nw - 1 + t + 1, Nw + 1 - t)}
                if row[0] == target[k]:
                    break
            else:
                ok26 = False
        row = {i: init.get(i, 0) for i in range(-Nw - 1, Nw + 2)}
        tr = [row[0]]
        for t in range(Nw - 1):
            row = {i: R30(row[i - 1], row[i], row[i + 1]) for i in range(-Nw - 1 + t + 1, Nw + 1 - t)}
            tr.append(row[0])
        ok26 &= tr == target
chk = [0, 1] * 4
ok26 &= [R30(chk[i - 1], chk[i], chk[(i + 1) % 8]) for i in range(8)] == chk
# (a, b) = ((01)^inf, 1^inf) has no H-preimage: H's second output is the first input, which must then be all ones,
# and the first output is then S(ones) XOR (ones OR b') = 0 everywhere. Brute force over period-2 (and period-4) inputs:
for Lq in (2, 4):
    tgt_a = tuple(t % 2 for t in range(Lq))
    tgt_b = tuple(1 for _ in range(Lq))
    for wa in range(2 ** Lq):
        for wb in range(2 ** Lq):
            ap = tuple((wa >> t) & 1 for t in range(Lq))
            bp = tuple((wb >> t) & 1 for t in range(Lq))
            ok26 &= Hmap(ap, bp) != (tgt_a, tgt_b)
ok26 &= Hmap(tuple([1] * 4), tuple([0, 1, 0, 1]))[0] == (0, 0, 0, 0)
check('S26 G127, G128: period-two table; 0102 lift; the six precursors of 022000 (all 22100...); finite-window traces', ok26)
print('ALL CHECKS PASS' if not fails else 'FAILED: ' + ', '.join(fails))
