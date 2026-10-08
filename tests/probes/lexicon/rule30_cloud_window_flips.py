#!/usr/bin/env python3
"""rule30_cloud_window_flips.py: RW, bit flips in fixed windows of the single-cell pyramid (the owner's descent)

RUN-ON:     cpu (Python 3 standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_window_flips.py [T=8192] [R=48] [WMAX=8]
COST:       well under a minute.

The owner's question (2026-10-08), after the Gray-code parallel (CL046): Rule 30 from one black cell draws a pyramid,
row r spanning columns -r .. r. Take a row, choose w adjacent pixels of it, and descend through that fixed window,
inspecting the bit flips from row to row; do this for every window of every width that fits the row. A Gray code
flips exactly one bit per step. Is a limited descent informative?

Cost. One run of the pyramid serves every window, since each window is read from the same rows; the rows are Python
integers used as bitsets. A window starting at a later row is a suffix of the same window started at the first row it
fits, so each absolute window [a, a + w - 1] is descended once, from row max(|a|, |a + w - 1|) to T.

What a flip measures (the Gray split of CL046, forward). Rule 30 = Rule 60 XOR (r AND NOT c), so cell i's flip is
    x_(t+1)(i) XOR x_t(i) = x_t(i-1) XOR (x_t(i+1) AND NOT x_t(i)),
its left neighbour XOR an edge event. A window's flip word is the window one column to the left, corrected by edge
events. Under Rule 60 it would be exactly that shifted window. The exact null: under the fair spatial law, solving
from the right as in G97, every w-bit flip word has exactly four preimages among the w + 2 cells it reads. So a
coin-like window has flip count k ~ Binomial(w, 1/2), and its Gray steps (k = 1) occur at the rate w / 2^w.
Controls (should PASS):
  RW-C1: in every window at every step, the flip word equals the shifted window XOR the edge word.
  RW-C2: for w = 3 .. WMAX, all 2^(w+2) neighbourhoods give every flip word exactly four times.
PREDICTIONS (Cloud's, pushed before the first run; T = 8192, |columns| <= 48, w = 3 .. 8):
  RW-P1: fixed windows look coin-like after their start row. The median, over all fixed windows, of the total
         variation distance between the flip-count histogram and Binomial(w, 1/2) is below 0.015. Confidence 0.7.
  RW-P2: no excess of Gray steps. Over all fixed windows of each width, P(k = 1) is within 0.01 of w / 2^w.
         Confidence 0.7.
UNEXPECTED CHECK (Cloud's): the pyramid's order lives at its edges, where Rowland's right diagonals have periods
  2^alpha. So windows that move with the right edge (columns t - d - w + 1 .. t - d, d = 0 .. 15) are not coin-like:
  their total variation distance from the binomial exceeds 0.1, and their edge-event density differs from 1/4 by more
  than 0.05, for most d < 8. Confidence 0.6; the direction is not predicted.
Counterfactual: if fixed windows near the centre are far from binomial, the core is not locally coin-like at these
  sizes, which would be news for Problem 2 (RULE30-PRIZE.md sections 8.34, 8.35).
"""
import sys
from math import comb

T = int(sys.argv[1]) if len(sys.argv) > 1 else 8192
R = int(sys.argv[2]) if len(sys.argv) > 2 else 48
WMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 8
OFF = T + 2                                   # bit OFF + i holds column i


def rows():
    row = 1 << OFF
    for _ in range(T + 1):
        yield row
        row = (row << 1) ^ (row | (row >> 1))


def tv(hist, w):
    n = sum(hist)
    return 0.5 * sum(abs(hist[k] / n - comb(w, k) / 2 ** w) for k in range(w + 1))


def null_ok(w):
    count = {}
    for m in range(1 << (w + 2)):
        x = [(m >> j) & 1 for j in range(w + 2)]                   # x[0] is the left neighbour of the window
        f = tuple(x[j - 1] ^ (x[j + 1] & (1 - x[j])) for j in range(1, w + 1))
        count[f] = count.get(f, 0) + 1
    return len(count) == 2 ** w and set(count.values()) == {4}


def main():
    print("RW-C2", "PASS" if all(null_ok(w) for w in range(3, WMAX + 1)) else "FAIL")
    fixed = {(a, w): [0] * (w + 1) for w in range(3, WMAX + 1) for a in range(-R, R - w + 2)}
    edge = {(d, w): [0] * (w + 1) for w in range(3, WMAX + 1) for d in range(16)}
    edge_ev = {d: [0, 0] for d in range(16)}
    c1 = True
    prev = None
    for t, row in enumerate(rows()):
        if prev is not None:
            s = t - 1
            flips = prev ^ row
            ev = (prev >> 1) & ~prev                                  # bit i: x(i+1) AND NOT x(i), at time s
            c1 &= flips == ((prev << 1) ^ ev) & ((1 << (OFF + s + 2)) - 1)
            for (a, w), h in fixed.items():
                if s >= max(abs(a), abs(a + w - 1)):
                    h[bin((flips >> (OFF + a)) & ((1 << w) - 1)).count("1")] += 1
            for (d, w), h in edge.items():
                lo = s - d - w + 1
                if lo >= -s:
                    h[bin((flips >> (OFF + lo)) & ((1 << w) - 1)).count("1")] += 1
            for d in edge_ev:
                i = s - d - 1                                         # edge event read at column i (needs i + 1)
                if i >= -s:
                    edge_ev[d][0] += (ev >> (OFF + i)) & 1
                    edge_ev[d][1] += 1
        prev = row
    print("RW-C1", "PASS" if c1 else "FAIL")
    tvs = sorted(tv(h, w) for (a, w), h in fixed.items())
    med = tvs[len(tvs) // 2]
    print(f"fixed windows: {len(tvs)}; total variation from Binomial(w, 1/2): median {med:.4f}, "
          f"max {tvs[-1]:.4f}")
    print("RW-P1", "HELD" if med < 0.015 else "REFUTED")
    p2 = True
    for w in range(3, WMAX + 1):
        hs = [h for (a, ww), h in fixed.items() if ww == w]
        n1 = sum(h[1] for h in hs)
        n = sum(sum(h) for h in hs)
        p2 &= abs(n1 / n - w / 2 ** w) <= 0.01
        worst = max(((tv(h, w), a) for (a, ww), h in fixed.items() if ww == w))
        print(f"  w = {w}: P(k = 1) = {n1 / n:.4f} against {w / 2 ** w:.4f}; worst window a = {worst[1]} "
              f"(tv {worst[0]:.4f})")
    print("RW-P2", "HELD" if p2 else "REFUTED")
    far = 0
    for d in range(16):
        tvd = [tv(edge[(d, w)], w) for w in range(3, WMAX + 1)]
        dens = edge_ev[d][0] / max(1, edge_ev[d][1])
        far += d < 8 and min(tvd) > 0.1 and abs(dens - 0.25) > 0.05
        print(f"  right edge, d = {d:2d}: tv by width {' '.join(f'{x:.3f}' for x in tvd)}; "
              f"edge-event density {dens:.3f}")
    print("unexpected check", "HELD" if far >= 5 else "REFUTED", f"({far} of d < 8 far from coin-like)")


if __name__ == "__main__":
    main()
