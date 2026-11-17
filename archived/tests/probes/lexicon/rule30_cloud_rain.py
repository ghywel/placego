#!/usr/bin/env python3
"""rule30_cloud_rain.py: the owner's "rain" of width-1 triangles is the fixed point (01)^inf, eaten from the left.

RUN-ON:     cpu (Python 3 standard library; big-integer rows)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_rain.py [T=2048]
COST:       expected under a minute.

Why (the owner, 2026-10-09, playing Triangle Lightning with "Highlight all: this size" at width 1). For every width
above 1 the highlighted triangles in the core look like random speckle. At width 1 the speckle is "interspersed
with tear drops or rain drops", collections of width-1 triangles in vertical stacks, smeared from top left to bottom
right "like rain falling in that direction". The other widths show no such smears.

Reasoning before the run (Cloud, by hand). A width-1 triangle is an isolated white cell: row t reads 1 0 1 at
columns i - 1, i, i + 1. Rule 30 gives x'(i) = 1 xor (0 or 1) = 0 and x'(i + 1) = 0 xor (1 or ...) = 1 whatever lies
further right, and x'(i - 1) = not x(i - 2). So the isolated white cell survives one more row exactly when
x(i - 2) = 0, and the right side can never end it. Inside an alternating stretch (0101...) every cell is fixed:
x'(j) = x(j - 1) xor 1 = x(j). That is Rule 30's second fixed point, (01)^inf, and every white cell in it is a
width-1 triangle, repeated in place row after row: a vertical stack. At the stretch's left end a (where
x(a - 1) = x(a)), x'(a) = x(a - 1) xor 1 flips cell a, so the end moves right by exactly one cell a row. Hence:
  K1 (exact law). If row t has an isolated white cell at i, and a is the left end of the maximal alternating stretch
     of row t that contains columns i - 1 .. i + 1, then column i stays isolated-white for exactly i - a rows, from
     t to t + i - a - 1, and not at row t + i - a.
  So every stack ends on a line of slope exactly one (the left end moving right a cell a row), and its top is where
  the stretch reached that column. A stretch can only extend on its right (when the cell after its end is a 1 that
  should be 0, it flips; when it is a 0 that should be 1, the end cell flips instead), so a patch drifts right while
  it is eaten from the left. That is the smear from top left to bottom right. Larger triangles cannot stack: a white
  run of width w >= 2 shrinks by one cell at each end every row, so no width-w triangle can sit right under another.

PREDICTIONS, written 2026-10-09 19:27 BST, before any run of this script (T = 2048, single black cell).
  RN-C (control, 0.97): K1 holds at every isolated white cell of rows 0 .. T - 1 whose stack ends before row T.
  RN-P1 (0.85): stacks of length >= 2 are made of width-1 triangles only. No triangle of width >= 2 has another
        triangle of the same width directly below its top row in the next row.
  RN-P2 (0.75): it belongs to the rule, not to the seed. The distribution of stack lengths in the single cell's core
        (columns right of -0.24 t) matches that of a random row evolved for T steps on a 4,096-cell ring: the
        mean length differs by less than 5%, and so does the share of stacks of length >= 4.
  RN-U, the unexpected check (0.5): alternating stretches' right ends advance while the stretch lives, at a mean
        speed above 0.5 cells a row (a patch drifts right faster than half the speed at which it is eaten).
  Counterfactual. A failure of K1 would mean the hand argument is wrong. A seed-specific distribution would make the
  rain a feature of the single cell rather than of Rule 30.

OUTCOME of the first run, 2026-10-09 (T = 2048; under a minute).
  RN-C PASS: K1 held at all 323,172 isolated white cells checked in the core, at all 523,942 in the whole pyramid,
    and at all 1,045,565 on the random ring. There were no violations.
  RN-P1 HELD: no white run of width >= 2 has a same-width run directly below it, on either the pyramid or the ring.
  RN-P2 HELD: the mean stack length is 1.9927 in the core against 1.9956 on the ring (-0.15%), and the share of
    length >= 4 is 0.1249 against 0.1242 (+0.59%). The core's counts halve with each step in length (81,343, 40,436,
    20,114, 10,284, 5,042, ...), so P(L = k) = 2^-k, as fair coins give: each further cell to the left continues the
    alternation with chance 1/2.
  RN-U REFUTED (the unexpected check): the right ends of stretches of six or more cells advance only 0.231 cells a
    row on average (ring: 0.218), against the left end's exact 1. So a patch is eaten about four times faster than it
    grows. The visible streaks are the rarer patches that grew. Their bottoms lie exactly on 45-degree lines, and that
    line is what gives the rain its slant.
  Reading: the rain is Rule 30's second fixed point (01)^inf, appearing in the core by chance with the coin's
  frequency and eaten from the left at exactly one cell a row. It is the rule's, not the seed's. It is a spatial
  alternation frozen in time, not the prize's period-2 column, which alternates in time.
  SCOPE (added 2026-10-09 after GPT's GC847).
  - GPT proved the Bernoulli null exactly. A stack top has exactly two five-bit predecessors, so its birth density is
    1/16 under iid fair initialization, and P(L = k | top) = 2^-k. The core's halving counts are empirical agreement
    with that null, not a proved distribution for the single seed or for a finite ring.
  - The end-of-record filter censors long late stacks.
  - The stack-top event differs from C5's triangle-birth event, whose width-1 density is 3/32.
"""
import random
import sys

T = int(sys.argv[1]) if len(sys.argv) > 1 else 2048


def rows_single(T):
    off = T + 4
    W = 2 * off + 1
    mask = (1 << W) - 1
    x = 1 << off
    out = []
    for _ in range(T):
        out.append(x)
        x = ((x << 1) ^ (x | (x >> 1))) & mask        # bit k holds cell k - off; x'(i) = x(i-1) xor (x(i) or x(i+1))
    return out, off, W


def rows_ring(T, n, seed=1):
    rnd = random.Random(seed)
    x = rnd.getrandbits(n)
    mask = (1 << n) - 1
    out = []
    for _ in range(T):
        out.append(x)
        l = ((x << 1) | (x >> (n - 1))) & mask
        r = ((x >> 1) | (x << (n - 1))) & mask
        x = l ^ (x | r)
    return out, n


def bits(x, W):
    return [(x >> k) & 1 for k in range(W)]


def analyse(rows, W, ring, colmin=None):
    """Return (law violations, law checks, stack lengths). An isolated white cell is 1 0 1 around it."""
    mask = (1 << W) - 1

    def nb(x):
        if ring:
            return ((x << 1) | (x >> (W - 1))) & mask, ((x >> 1) | (x << (W - 1))) & mask
        return (x << 1) & mask, x >> 1                 # bit k of these holds cells k - 1 and k + 1

    iso = []
    for x in rows:
        l, r = nb(x)
        iso.append(~x & l & r & mask)
    nT = len(rows)

    def cell(t, k):
        if ring:
            k %= W
        elif not 0 <= k < W:
            return 0
        return (rows[t] >> k) & 1

    viol = checks = 0
    lengths = []
    for t in range(nT):
        m = iso[t]
        while m:
            low = m & -m
            k = low.bit_length() - 1
            m ^= low
            if colmin is not None and not colmin(t, k):
                continue
            a = k - 1                                  # extend the alternating stretch leftwards from k - 1
            while cell(t, a - 1) != cell(t, a) and k - a < 4 * nT:
                a -= 1
            life = k - a
            if t + life < nT:
                checks += 1
                kk = k % W
                ok = all((iso[t + s] >> kk) & 1 for s in range(life)) and not (iso[t + life] >> kk) & 1
                viol += not ok
                if t == 0 or not (iso[t - 1] >> kk) & 1:   # the top of a stack
                    lengths.append(life)
    return viol, checks, lengths


def runs_same_width(rows, W, ring):
    """Count white runs of width w >= 2 with a same-width white run at the same columns in the next row."""
    B = [bits(x, W) for x in rows]
    bad = 0
    for t in range(len(B) - 1):
        row, nxt = B[t], B[t + 1]
        k = 0
        while k < W:
            if row[k] == 0:
                j = k
                while j < W and row[j] == 0:
                    j += 1
                w = j - k
                if w >= 2 and k > 0 and j < W and row[k - 1] == 1 and row[j] == 1:
                    if all(nxt[m] == 0 for m in range(k, j)) and nxt[k - 1] == 1 and nxt[j] == 1:
                        bad += 1
                k = j
            else:
                k += 1
    return bad


def right_speed(rows, W, ring):
    """Mean advance per row of the right end of alternating stretches of length >= 6, tracked while they live."""
    B = [bits(x, W) for x in rows]
    adv = steps = 0
    for t in range(len(B) - 1):
        row, nxt = B[t], B[t + 1]
        k = 1
        while k < W - 1:
            j = k
            while j + 1 < W and row[j + 1] != row[j]:
                j += 1
            if j - k + 1 >= 6:                         # stretch [k, j]; find its right end in the next row
                m = j - 2
                while m + 1 < W and nxt[m + 1] != nxt[m]:
                    m += 1
                adv += m - j
                steps += 1
            k = j + 1
    return adv / max(steps, 1), steps


def summary(lengths):
    n = len(lengths)
    return n, sum(lengths) / n, sum(1 for L in lengths if L >= 4) / n


def main():
    rs, off, W = rows_single(T)
    core = lambda t, k: (k - off) > -0.24 * t and (k - off) < t - 2
    v, c, L1 = analyse(rs, W, False, core)
    print('RN-C: K1 checked at %d isolated white cells of the core, violations %d' % (c, v))
    v_all, c_all, _ = analyse(rs, W, False, None)
    print('      whole pyramid: %d checks, %d violations' % (c_all, v_all))
    print('RN-P1: width >= 2 runs with a same-width run directly below (single cell): %d'
          % runs_same_width(rs, W, False))
    n = 4096
    rr, W2 = rows_ring(T, n)
    v2, c2, L2 = analyse(rr[:T], W2, True, None)
    print('       ring: K1 checks %d, violations %d; same-width stacking %d' % (c2, v2, runs_same_width(rr, W2, True)))
    s1, s2 = summary(L1), summary(L2)
    print('RN-P2: single-cell core stacks %d, mean %.4f, share >= 4 %.4f' % s1)
    print('       random ring stacks %d, mean %.4f, share >= 4 %.4f' % s2)
    print('       relative differences: mean %.2f%%, share %.2f%%'
          % (100 * (s1[1] / s2[1] - 1), 100 * (s1[2] / s2[2] - 1)))
    from collections import Counter
    c1 = Counter(L1)
    print('       stack length counts (core):', [(L, c1[L]) for L in sorted(c1)[:14]])
    sp, st = right_speed(rs, W, False)
    sp2, st2 = right_speed(rr, W2, True)
    print('RN-U: right-end advance per row, stretches >= 6: single cell %.3f (%d), ring %.3f (%d)'
          % (sp, st, sp2, st2))


if __name__ == '__main__':
    main()
