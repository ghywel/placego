#!/usr/bin/env python3
"""rule30_prng.py: what is Rule 30's "poor behaviour on a chi-squared test when applied to all the columns"?

RUN-ON:     cpu (pure Python 3, standard library; seeded)
COMMAND:    python3 tests/probes/lexicon/rule30_prng.py
COST:       about two minutes on one core.

The owner's question (2026-10-05), on Wikipedia's sentence that "Sipper and Tomassini have shown that as a random
number generator Rule 30 exhibits poor behavior on a chi squared test when applied to all the rule columns" (Int. J.
Mod. Phys. C 7 (1996) 181-190; not read, paywalled). Their setup, as Spencer's survey (arXiv:1306.3546, read) describes
it: a ring of 50 cells, 300 random initial rows, 4,096 steps, every cell used as a stream (a parallel generator),
four statistical tests. Wolfram's own generator uses one stream only, the centre column.

The hypothesis, from Rule 30's formula alone. Read right to left, x_{t+1}(i) = x_t(i-1) XOR (x_t(i) OR x_t(i+1)), so
    x_{t+1}(i) XOR x_t(i-1) = x_t(i) OR x_t(i+1),
which is 1 three times in four. Each column is its left neighbour's column, delayed one step, XORed with a mask that
is 1 three-quarters of the time. Any test that looks at two neighbouring streams together sees that at once, and a
test of one stream at a time cannot. In the linear rules 90 and 150 the same XOR is an unbiased bit, so this test
passes for them (other tests do not). Lemma 3 of this work and the left-permutive inverse are this identity.

PREDICTIONS, written 2026-10-05 before this script's first run:
  C  (control, exact): the identity holds at every cell of every run, and the patterns (x_t(i-1), x_t(i), x_{t+1}(i))
     = (0, 1, 0) and (1, 1, 1) never occur (if x_t(i) = 1 then x_{t+1}(i) = NOT x_t(i-1)).
  P1 (blind; one stream at a time): over the 15,000 streams (50 cells x 300 starts), the share failing a frequency
     chi-square at p < 0.01 lies in [0.5%, 2%], as for fair coins.
  P2 (blind; one stream, blocks of 4 steps, 16 bins): the share failing at p < 0.01 lies in [0.5%, 2%].
  P3 (blind; one row at a time): bytes of 8 adjacent cells at one time, 256 bins, one test per start: the share failing
     at p < 0.01 lies in [0%, 3%]. (A uniformly random row stays uniformly distributed under Rule 30.)
  P4 (blind; two streams together, the parallel failure): the share of steps with x_{t+1}(i) = x_t(i-1) lies in
     [0.24, 0.26] (fair, independent streams would give 0.5), and every one of the 15,000 neighbour-pair chi-squares
     has p < 1e-10.
  P5 (counterfactual): the same statistic for rings run by Rule 90 and by Rule 150 lies in [0.49, 0.51].
  P6 (blind; Wolfram's way): the centre column from a single 1, 40,000 steps, on a row wide enough never to wrap.
     Its bytes pass a 256-bin chi-square (p > 0.01), and the share of steps with x_{t+1}(0) = x_t(-1) still lies in
     [0.24, 0.26]: the flaw is there, but a user who reads only column 0 never sees column -1.
REFUTED-BY: C failing (the harness); P1 to P6 failing.
"""
import math, random

N, STARTS, T = 50, 300, 4096
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def chi2_sf(x, k):
    """P(chi-square with k degrees of freedom >= x): the regularised upper incomplete gamma Q(k/2, x/2)."""
    a, z = k / 2.0, x / 2.0
    if z <= 0:
        return 1.0
    if z < a + 1:                                     # series for P, then Q = 1 - P
        term = s = 1.0 / a
        n = a
        while abs(term) > 1e-15 * abs(s):
            n += 1
            term *= z / n
            s += term
        return max(0.0, 1.0 - s * math.exp(-z + a * math.log(z) - math.lgamma(a)))
    b, c, d = z + 1 - a, 1e300, 1 / (z + 1 - a)       # continued fraction for Q (Lentz)
    h = d
    for i in range(1, 10000):
        an = -i * (i - a)
        b += 2
        d = an * d + b
        d = 1 / d if d != 0 else 1e300
        c = b + an / c if c != 0 else 1e-300
        delta = d * c
        h *= delta
        if abs(delta - 1) < 1e-15:
            break
    return math.exp(-z + a * math.log(z) - math.lgamma(a)) * h


def chi2(counts):
    n, k = sum(counts), len(counts)
    e = n / k
    return chi2_sf(sum((c - e) ** 2 / e for c in counts), k - 1)


def ring_step(row, rule, n):
    mask = (1 << n) - 1
    left = ((row << 1) | (row >> (n - 1))) & mask      # bit i holds x(i-1)
    right = ((row >> 1) | ((row & 1) << (n - 1))) & mask   # bit i holds x(i+1)
    if rule == 30:
        return left ^ (row | right)
    if rule == 90:
        return left ^ right
    return left ^ row ^ right                           # 150


def main():
    rng = random.Random(1996)
    ident_bad = forbidden = 0
    p1 = p2 = p3 = p4 = 0
    p4_min_ok = True
    same = total = 0
    lin = {90: [0, 0], 150: [0, 0]}
    for _ in range(STARTS):
        row0 = rng.getrandbits(N)
        rows = [row0]
        for _ in range(T - 1):
            rows.append(ring_step(rows[-1], 30, N))
        mask = (1 << N) - 1
        for a, b in zip(rows, rows[1:]):
            left = ((a << 1) | (a >> (N - 1))) & mask
            right = ((a >> 1) | ((a & 1) << (N - 1))) & mask
            ident_bad += (b ^ left) != (a | right)
            forbidden += bin(a & ~(b ^ left) & mask).count("1")   # x(i) = 1 and x'(i) = x(i-1)
        cols = [[(r >> i) & 1 for r in rows] for i in range(N)]
        for i in range(N):
            c = cols[i]
            ones = sum(c)
            p1 += chi2([ones, T - ones]) < 0.01
            blocks = [0] * 16
            for j in range(0, T - 3, 4):
                blocks[c[j] << 3 | c[j + 1] << 2 | c[j + 2] << 1 | c[j + 3]] += 1
            p2 += chi2(blocks) < 0.01
            prev = cols[(i - 1) % N]
            s = sum(1 for t in range(T - 1) if c[t + 1] == prev[t])
            same += s
            total += T - 1
            pv = chi2([s, T - 1 - s])
            p4_min_ok &= pv < 1e-10
        byte = [0] * 256
        for r in rows:
            for k in range(N // 8):
                byte[(r >> (8 * k)) & 255] += 1
        p3 += chi2(byte) < 0.01
        for rule in (90, 150):
            a = row0
            for _ in range(T - 1):
                b = ring_step(a, rule, N)
                left = ((a << 1) | (a >> (N - 1))) & mask
                lin[rule][0] += N - bin((b ^ left) & mask).count("1")
                lin[rule][1] += N
                a = b
    report("C the identity x'(i) XOR x(i-1) = x(i) OR x(i+1) holds everywhere, and (a, 1, a) never occurs",
           ident_bad == 0 and forbidden == 0, f"{ident_bad} rows break the identity; {forbidden} forbidden patterns")
    ns = N * STARTS
    verdict("P1 one stream at a time passes a frequency chi-square (failures 0.5% to 2%)",
            0.005 <= p1 / ns <= 0.02, f"{p1} of {ns} fail at p < 0.01 ({p1 / ns:.2%})")
    verdict("P2 one stream, 4-step blocks, passes (failures 0.5% to 2%)", 0.005 <= p2 / ns <= 0.02,
            f"{p2} of {ns} fail ({p2 / ns:.2%})")
    verdict("P3 one row at a time, 8-cell bytes, passes (failures at most 3%)", p3 / STARTS <= 0.03,
            f"{p3} of {STARTS} starts fail ({p3 / STARTS:.2%})")
    share = same / total
    verdict("P4 neighbouring streams: x'(i) = x(i-1) in 24% to 26% of steps, every pair test p < 1e-10",
            0.24 <= share <= 0.26 and p4_min_ok, f"share {share:.4f}; every pair below 1e-10: {p4_min_ok}")
    l90, l150 = lin[90][0] / lin[90][1], lin[150][0] / lin[150][1]
    verdict("P5 the linear rules 90 and 150 pass the same test (share 0.49 to 0.51)",
            0.49 <= l90 <= 0.51 and 0.49 <= l150 <= 0.51, f"Rule 90 {l90:.4f}, Rule 150 {l150:.4f}")

    steps = 40000
    width = 2 * steps + 3
    c0 = steps + 1                                      # bit c0 is column 0; bit i - 1 is the left neighbour of bit i
    row = 1 << c0
    mask = (1 << width) - 1
    centre, left_col = [], []
    for _ in range(steps + 1):
        centre.append((row >> c0) & 1)
        left_col.append((row >> (c0 - 1)) & 1)           # column -1
        row = ((row << 1) ^ (row | (row >> 1))) & mask    # x'(i) = x(i-1) XOR (x(i) OR x(i+1)), as on the ring
    byte = [0] * 256
    for j in range(0, steps - 7, 8):
        v = 0
        for b in centre[j:j + 8]:
            v = v << 1 | b
        byte[v] += 1
    pc = chi2(byte)
    sh = sum(1 for t in range(steps) if centre[t + 1] == left_col[t]) / steps
    verdict("P6 Wolfram's centre column passes a byte chi-square, and the neighbour flaw is still there",
            pc > 0.01 and 0.24 <= sh <= 0.26, f"byte chi-square p = {pc:.3f}; x_(t+1)(0) = x_t(-1) in {sh:.4f}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")


if __name__ == "__main__":
    main()
