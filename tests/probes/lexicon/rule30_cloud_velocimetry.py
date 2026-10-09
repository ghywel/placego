#!/usr/bin/env python3
"""rule30_cloud_velocimetry.py: do triangles move? Particle-image velocimetry on Rule 30, and does the wheel print them?

RUN-ON:     cpu (Python 3 standard library; big-integer rows)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_velocimetry.py [T=4096] [part=all|piv|wheel|posthoc]
COST:       expected a few minutes.

Why (the owner, 2026-10-09, after Cloud's answer on the wheel and the random side). "Does the wheel 'print' triangles
into the pattern directly? Or does a [triangle] in one location get translated/rotated to a new location? Are the
triangles a random speckle pattern, or with careful analysis can we say they actually evolve and move over time." The
owner likened it to the interpolation shaders and particle-image velocimetry (PIV): rows are frames, and PIV finds a
displacement by the peak of the cross-correlation between frames.

Reasoning before the run (Cloud, by hand).
  V1 (a theorem for fair rows). Rule 30 is left-permutive: given the cells to its right, a block of m cells of row
     t + d is a bijective function of the m cells of row t starting d places to its left. Rows of a fair random line
     stay fair (Rule 30 is surjective, so it keeps the uniform measure). So an event in row t + d is independent of
     every event in row t whose cells avoid that leftmost window. Every correlation between frames therefore lies on
     the rightward line s = +d, widened only by the events' own widths. For single cells it is exactly the line: the
     correlation of x_t(i) and x_(t+d)(i+s) is zero unless s = d, where it is the alternation law's rho_d (-1/2, 1/4,
     -1/4, 5/32, -5/64, 77/1024, -141/2048, 39/512; RULE30-PRIZE.md section 8.70). In PIV terms the pattern has one
     velocity, one cell a row to the right, carried with a sign flip and fading. Nothing correlates leftwards, though
     influence does spread left (at 0.246 a row): the leftmost XOR scrambles it, so correlation cannot see it.
  V2. A triangle top (a white run that is not the shrunk continuation of a run above, as in Triangle Lightning) is
     such an event, so births correlate only near the rightward line. A triangle is not carried bodily: its edges
     close in at one cell a row on each side, and the next generation is born where the rightward-moving information
     lands. Speckle with a drift, not moving objects.
  V3 (the wheel, in the period-2 world: column 0 clamped to 0101, a random right half driven by it). Columns 0 and 1
     force everything to their left (Proposition 7): column -k at time t depends on columns 0 and 1 at times t to
     t + k + 1. So wherever column 1 runs a clean 56-step stretch of the wheel U, every cell and every triangle to the
     left within depth 54 is a function of the wheel's position: printed exactly. To the right, column 2 is fixed only
     where column 1 is white (x_t(2) = x_(t+1)(1) xor x_t(0)), and further right the dependence should fade fast.

PREDICTIONS, written 2026-10-09 19:58 BST, before any run of this script (T = 4096).
  VE-C (control, 0.9): on a fair random line, the cell correlation at (d, s), d = 1 .. 8, |s| <= 12, is within 5
        standard errors of rho_d where s = d and of 0 elsewhere.
  VE-P1 (0.85): the same holds in the single cell's core (columns -0.2 t .. 0.9 t, rows T/4 .. T).
  VE-P2 (0.8): for triangle tops of width <= 3 on the random line, the normalised cross-correlation C(d, s) differs
        from 1 by more than 5 standard errors only for s in [d - 7, d + 7], d = 1 .. 8, |s| <= 16. That is the band
        V1 allows, since a top of width <= 3 is a function of 8 cells of the row above it. Inside the band it does so
        for every d <= 4.
  VE-P3 (0.75): the single cell's core gives the same band picture for triangle tops.
  VE-U, the unexpected check (0.5): the triangle ridge inherits the alternating sign: C(d, d) - 1 alternates in sign
        for d = 1 .. 6 on the random line.
  VW-C (control, exact by V3): on rows where column 1 matches a rotation of U for 56 steps, the wheel's position
        (with the clock's parity) determines column 1 and every column -1 .. -12 completely (conditional entropy 0).
  VW-P1 (0.6): the mutual information between the wheel's position and column 2 lies in [0.3, 0.7] bits.
  VW-P2 (0.6): it at least halves from column 2 to column 4, and it is below 0.05 bits for columns 5 .. 12.
  Counterfactual. A correlation off the rightward band (VE-C or VE-P2 failing) would refute V1's reading and point to
  genuine moving structure. Information about the wheel persisting far right would mean the wheel prints into the
  random side.

OUTCOME of the first run, 2026-10-09 (T = 4096; a few minutes on one core beside RR3).
  VE-C PASS: on the random line the largest off-diagonal cell correlation is 3.43 standard errors, and the diagonal
    reproduces the alternation law within 1.3 se at every d (-0.5001, 0.2501, -0.2501, 0.1564, -0.0783, 0.0753,
    -0.0691, 0.0764).
  VE-P1 HELD: the single cell's core gives the same, with the largest off-diagonal at 3.59 se and the diagonal within
    1.5 se.
  VE-P2 HELD: for triangle tops, the largest |C - 1| outside the band [d - 7, d + 7] is 3.42 se. Inside the band the
    deviations are huge at every d (61 to 1,050 se).
  VE-P3 HELD: the single cell's core gives the same, with 2.60 se outside the band.
  VE-U HELD (the unexpected check): along the rightward line, C(d, d) runs 0, 2.10, 0.25, 1.92, 0.73, 1.25, 0.87,
    1.37 for d = 1 .. 8, alternating about 1. A top never has another top one row down and one cell right, and is
    twice as likely to have one two rows down and two cells right. That is the alternation law's rhythm, in triangles.
  VW-C PASS: on clean rows (58.0% of rows start a clean 56-step stretch of U) the wheel's position and the clock's
    parity fix column 1 and every column -1 .. -12 completely, cells and triangle tops alike.
  VW-P1 REFUTED, VW-P2 REFUTED: the wheel's position also fixes columns 2, 3 and 4 completely (0.970, 0.997 and 0.857
    bits, all of their entropy). It fixes 93% of column 5's entropy, then 94, 76, 70, 55, 46, 38 and 29% out to
    column 12. Triangle tops in columns 2 .. 10 follow it in the same way.
  POST HOC (written after the run; part=posthoc). The run conditions on column 1 following U for the next 56 rows,
    which constrains the right side's present. So the same measure was taken with the wheel's past 56 rows instead.
    It still fixes 94% of column 2's entropy, then 89, 81, 71, 64, 51, 48, 38, 30, 24 and 17% for columns 3 .. 12.
    Column 2 repeats 56 rows later at 95% of consecutive clean starts.
  Reading. In the period-2 world the wheel is not one column. It is the edge of a block of columns that turns
  together: columns 1 to 4 locked rigidly, the lock fading over about ten columns into the random side. Triangles in
  the block are printed at the same places every 56 rows, like teeth on a turning gear, until a kick from further
  out slips it. Outside the block, and everywhere in the single cell's real core, triangles are speckle with one
  drift: their births echo along the rightward light line, with the alternation law's sign rhythm, and nothing else
  correlates.
"""
import random
import re
import sys
from collections import Counter
from math import log2, sqrt

T = int(sys.argv[1]) if len(sys.argv) > 1 else 4096
PART = sys.argv[2] if len(sys.argv) > 2 else 'all'
D, S, SB = 8, 12, 16
RHO = [-1 / 2, 1 / 4, -1 / 4, 5 / 32, -5 / 64, 77 / 1024, -141 / 2048, 39 / 512]
U = '00010011010001001101000100110100010011010001001101001101'


def evolve(x, n, W):
    mask = (1 << W) - 1
    rows = []
    for _ in range(n):
        rows.append(x)
        x = ((x << 1) ^ (x | (x >> 1))) & mask        # bit k is cell k: x'(i) = x(i-1) xor (x(i) or x(i+1))
    return rows


def shifted(r, s):
    return r >> s if s >= 0 else r << -s              # bit i of the result holds cell i + s


def cell_corr(rows, masks, t0, t1):
    out = {}
    for d in range(1, D + 1):
        for s in range(-S, S + 1):
            agree = n = 0
            for t in range(t0, t1):
                m = masks[t]
                agree += (~(rows[t] ^ shifted(rows[t + d], s)) & m).bit_count()
                n += m.bit_count()
            out[(d, s)] = ((2 * agree - n) / n, 1 / sqrt(n))
    return out


def tops(rows, W):
    """Bitsets of the left ends of triangle tops of width <= 3 (white runs bounded by black, not a continuation)."""
    out, prev = [], set()
    for x in rows:
        s = format(x, '0%db' % W)[::-1]
        cur, e = set(), 0
        for m in re.finditer(r'(?<=1)0+(?=1)', s):
            a, b = m.start(), m.end() - 1
            cur.add((a, b))
            if (a - 1, b + 1) not in prev and b - a + 1 <= 3:
                e |= 1 << a
        out.append(e)
        prev = cur
    return out


def top_corr(E, masks, t0, t1):
    out = {}
    for d in range(1, D + 1):
        for s in range(-SB, SB + 1):
            joint = expect = 0.0
            for t in range(t0, t1):
                m, m2 = masks[t], masks[t + d]
                base = (E[t] & m).bit_count()
                dens = (E[t + d] & m2).bit_count() / m2.bit_count()
                joint += (E[t] & m & shifted(E[t + d], s)).bit_count()
                expect += base * dens
            out[(d, s)] = (joint / expect, 1 / sqrt(expect))
    return out


def piv():
    rnd = random.Random(30)
    Wr = 8192 + 2 * (T + D) + 64
    lo, hi = T + D + 32, Wr - T - D - 32
    band = ((1 << (hi - lo)) - 1) << lo
    line = evolve(rnd.getrandbits(Wr), T + D + 1, Wr)
    lmask = [band] * (T + D + 1)
    off = T + D + 4
    W1 = 2 * off + 1
    single = evolve(1 << off, T + D + 1, W1)
    smask = []
    for t in range(T + D + 1):
        a, b = -int(0.2 * t), int(0.9 * t) - 1
        smask.append(((1 << (b - a + 1)) - 1) << (off + a) if b > a + 16 and a > -t else 0)
    worlds = [('random line', line, lmask, Wr, 0, T), ('single cell core', single, smask, W1, T // 4, T)]
    for name, rows, masks, W, t0, t1 in worlds:
        cc = cell_corr(rows, masks, t0, t1)
        worst_off = max(abs(v) / se for (d, s), (v, se) in cc.items() if s != d)
        diag = [(d, cc[(d, d)][0], (cc[(d, d)][0] - RHO[d - 1]) / cc[(d, d)][1]) for d in range(1, D + 1)]
        print('%s cells: largest off-diagonal |corr|/se %.2f' % (name, worst_off))
        print('  diagonal s = d: ' + '; '.join('d%d %.4f (%+.1f se)' % x for x in diag))
        E = tops(rows, W)
        tc = top_corr(E, masks, t0, t1)
        outside = [(abs(v - 1) / se, d, s) for (d, s), (v, se) in tc.items() if not d - 7 <= s <= d + 7]
        print('%s triangle tops: largest |C-1|/se outside the band %.2f at (d, s) = (%d, %d)'
              % ((name,) + max(outside)))
        for d in range(1, D + 1):
            inside = [(abs(tc[(d, s)][0] - 1) / tc[(d, s)][1], s) for s in range(d - 7, d + 8) if -SB <= s <= SB]
            best = max(inside)
            print('  d = %d: C(d, d) = %.4f; strongest in band |C-1|/se %.1f at s = %d (C = %.4f)'
                  % (d, tc[(d, d)][0], best[0], best[1], tc[(d, best[1])][0]))


def wheel():
    rot = {}
    for p in range(56):
        rot[sum(int(U[(p + j) % 56]) << j for j in range(56))] = p
    seeds, n = 16, 4 * T
    cnt = {k: Counter() for k in range(-12, 13) if k != 0}
    tcnt = {k: Counter() for k in range(-10, 11)}
    clean = total = 0
    for seed in range(seeds):
        rnd = random.Random(1000 + seed)
        Wr = 2 * n + 64
        row = rnd.getrandbits(Wr) << 1
        rows = []
        for t in range(n + 64):
            row = (row & ~1) | (t % 2)                # impose the clock 0101... on column 0 (bit 0)
            rows.append(row)
            row = (row << 1) ^ (row | (row >> 1))
        N = n + 64
        col = {k: [(rows[t] >> k) & 1 for t in range(N)] for k in range(0, 13)}
        tau = sum(col[0][t] << t for t in range(N))
        sig = sum(col[1][t] << t for t in range(N))
        mask = (1 << N) - 1
        left = {0: tau, 1: sig}
        for k in range(1, 13):
            a, b = left[-k + 1], left[-k + 2]
            left[-k] = ((a >> 1) ^ (a | b)) & (mask >> k)
        for k in range(1, 13):
            col[-k] = [(left[-k] >> t) & 1 for t in range(N)]
        win = 0
        for j in range(56):
            win |= col[1][j] << j
        prevruns = set()
        for t in range(n):
            if t:
                win = (win >> 1) | (col[1][t + 55] << 55)
            seg = ''.join(str(col[k][t]) for k in range(-12, 13))
            runs = set()
            topset = set()
            for m in re.finditer(r'(?<=1)0+(?=1)', seg):
                a, b = m.start() - 12, m.end() - 1 - 12
                runs.add((a, b))
                if (a - 1, b + 1) not in prevruns and b - a + 1 <= 3:
                    topset.add(a)
            prevruns = runs
            if t < 1024:
                continue
            total += 1
            p = rot.get(win)
            if p is None:
                continue
            clean += 1
            state = 2 * p + t % 2                     # the wheel's position, with the clock's parity
            for k in cnt:
                cnt[k][(state, col[k][t])] += 1
            for k in tcnt:
                tcnt[k][(state, int(k in topset))] += 1
    print('wheel: %d of %d rows (%.1f%%) start a clean 56-step stretch of U' % (clean, total, 100 * clean / total))

    def mi(c):
        nn = sum(c.values())
        px, pp = Counter(), Counter()
        for (p, x), v in c.items():
            px[x] += v
            pp[p] += v
        hx = -sum(v / nn * log2(v / nn) for v in px.values())
        hxp = -sum(v / nn * log2(v / pp[p]) for (p, x), v in c.items())
        return hx, hx - hxp
    for k in sorted(cnt):
        hx, m = mi(cnt[k])
        print('  column %3d: H = %.3f bits, information from the wheel %.3f bits (%.0f%%)'
              % (k, hx, m, 100 * m / hx))
    for k in sorted(tcnt):
        hx, m = mi(tcnt[k])
        print('  triangle tops at column %3d: H = %.3f, from the wheel %.3f (%.0f%%)'
              % (k, hx, m, 100 * m / hx if hx else 0))


def posthoc():
    """The wheel's past 56 rows instead of its next 56: how much of column k at time t do they fix?"""
    rot = {sum(int(U[(p + j) % 56]) << j for j in range(56)): p for p in range(56)}
    n = 4 * T
    res = {k: Counter() for k in range(2, 13)}
    rep = Counter()
    for seed in range(16):
        rnd = random.Random(1000 + seed)
        row = rnd.getrandbits(2 * n + 64) << 1
        rows = []
        for t in range(n + 64):
            row = (row & ~1) | (t % 2)
            rows.append(row)
            row = (row << 1) ^ (row | (row >> 1))
        col = {k: [(rows[t] >> k) & 1 for t in range(n + 64)] for k in range(0, 13)}
        P = [rot.get(sum(col[1][t + j] << j for j in range(56))) for t in range(n)]
        for t in range(1024, n):
            pp = P[t - 55]
            if pp is not None:
                for k in range(2, 13):
                    res[k][(2 * ((pp + 55) % 56) + t % 2, col[k][t])] += 1
            if P[t] is not None and t + 1 < n and P[t + 1] is not None:
                rep[col[2][t] == col[2][t + 56]] += 1

    def mi(c):
        nn = sum(c.values())
        px, pq = Counter(), Counter()
        for (p, x), v in c.items():
            px[x] += v
            pq[p] += v
        hx = -sum(v / nn * log2(v / nn) for v in px.values())
        return hx, hx + sum(v / nn * log2(v / pq[p]) for (p, x), v in c.items())
    for k in range(2, 13):
        hx, m = mi(res[k])
        print('past window: column %2d: H = %.3f, fixed by the wheel %.3f (%.0f%%)' % (k, hx, m, 100 * m / hx))
    print('column 2 equal 56 rows later at consecutive clean starts:', dict(rep))


if __name__ == '__main__':
    if PART in ('all', 'piv'):
        piv()
    if PART in ('all', 'wheel'):
        wheel()
    if PART == 'posthoc':
        posthoc()
