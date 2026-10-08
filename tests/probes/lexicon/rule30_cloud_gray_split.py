#!/usr/bin/env python3
"""rule30_cloud_gray_split.py: RG, Rule 30 as the Gray-code rule plus an edge term, run sideways (row Q6, LR)

RUN-ON:     cpu (Python 3 standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_gray_split.py [TRIALS=200] [DEPTH=40] [SEED=6060]
COST:       a few seconds.

The owner's question (2026-10-08): can the centre column settle into a Gray code? The answer led to a parallel.
Rule 60, x' = l XOR c, applied once to a number's binary digits (most significant on the left), gives its Gray code.
Rule 30 is x' = l XOR (c OR r), and c OR r = c XOR (r AND NOT c), so
    Rule 30 = Rule 60 XOR (r AND NOT c),
the Gray-code rule plus an edge term that fires where a white cell has a black right neighbour. The record has Rule 60
as the one sibling with period-2 witnesses (RULE30-PRIZE.md section 8.3), the identity (c OR r) XOR c = r AND NOT c
inside G97, and forward Duhamel sums with a Pascal kernel over other linear parts (G28, G214, G215). This probe checks
the sideways form, which reads the forced left half in the Gray split.
Sideways, section 5's recursion x_t(-k) = x_(t+1)(-k+1) XOR (x_t(-k+1) OR x_t(-k+2)) becomes
    column(-k) = D column(-k+1) XOR E_k,   (D v)(t) = v(t+1) XOR v(t),   E_k(t) = x_t(-k+2) AND NOT x_t(-k+1).
D is the flip record: each column to the left records where its right neighbour flips, as one Gray step in time
does, corrected by the edge events E_k. Unrolled, with D^m having the Pascal coefficients C(m, i) mod 2 in time
(computed here by Lucas's theorem, independently of the recursion):
    column(-k) = D^k column(0) XOR (XOR over j = 1 .. k of D^(k-j) E_j).
For the clock 0101 (the wall form), D of it is 1111 and D^2 of it is 0. So from depth 2 on, the forced left half is
exactly a Pascal-in-time superposition of edge events. With no edge events after the first, it would be zero.
Controls (each should PASS):
  RG-C1: Rule 30 = Rule 60 XOR (r AND NOT c) on all 8 neighbourhoods; one Rule 60 step is the Gray code of every
         8-bit number.
  RG-C2: on random right halves next to the 0101 wall, the unrolled formula equals section 5's recursion at every
         depth 2 .. DEPTH and every time where both are defined.
UNEXPECTED CHECK (Cloud's, predicted before the run): the density of edge events E_k in the forced left half, over
  depths 2 .. DEPTH, lies between 0.20 and 0.30, near the 1/4 of a fair coin (white cell, black right neighbour).
  Confidence 0.6. Counterfactual: a density well away from 1/4 would mean the left half's local statistics are not
  coin-like, and the edge events carry structure of their own.
"""
import random
import sys

TRIALS = int(sys.argv[1]) if len(sys.argv) > 1 else 200
DEPTH = int(sys.argv[2]) if len(sys.argv) > 2 else 40
SEED = int(sys.argv[3]) if len(sys.argv) > 3 else 6060


def rule(n, l, c, r):
    return (n >> (4 * l + 2 * c + r)) & 1


def column1(R, T):
    """Column 1 for t = 0 .. T-1 of the right half with initial row R (bit i is site i + 1), wall 0101."""
    row, out = R << 1, []
    for t in range(T):
        out.append((row >> 1) & 1)
        row = (((row << 1) ^ (row | (row >> 1))) & ~1) | ((t + 1) % 2)
    return out


def subsets(m):
    """The i with C(m, i) odd (Lucas: the binary digits of i are a subset of those of m)."""
    i, out = m, []
    while True:
        out.append(i)
        if i == 0:
            return out
        i = (i - 1) & m


def main():
    ok1 = all(rule(30, l, c, r) == rule(60, l, c, r) ^ (r & (1 - c))
              for l in (0, 1) for c in (0, 1) for r in (0, 1))
    for k in range(256):
        row = [0] + [(k >> (7 - i)) & 1 for i in range(8)] + [0]
        g = [rule(60, row[i - 1], row[i], row[i + 1]) for i in range(1, 9)]
        ok1 &= int("".join(map(str, g)), 2) == k ^ (k >> 1)
    print("RG-C1", "PASS" if ok1 else "FAIL")
    rng = random.Random(SEED)
    T = 2 * DEPTH + 40
    ok2, events, cells = True, 0, 0
    for i in range(TRIALS):
        w = (8, 16, 24, 32)[i % 4]
        c1 = column1(rng.getrandbits(w) | 1, T)
        # columns as bitsets: bit t is the cell at time t; n[k] is how many times are defined
        cols = {1: sum(b << t for t, b in enumerate(c1)), 0: sum((t % 2) << t for t in range(T))}
        n = {1: T, 0: T}
        E = {}
        for k in range(1, DEPTH + 1):
            a, b = cols[-k + 1], cols[-k + 2]
            n[-k] = min(n[-k + 1] - 1, n[-k + 2])
            mask = (1 << n[-k]) - 1
            cols[-k] = ((a >> 1) ^ (a | b)) & mask                          # section 5
            E[k] = (b & ~a) & ((1 << min(n[-k + 1], n[-k + 2])) - 1)
        for k in range(2, DEPTH + 1):
            acc = 0
            for j in range(1, k + 1):
                for s in subsets(k - j):                                     # D^(k-j) by Lucas
                    acc ^= E[j] >> s
            mask = (1 << n[-k]) - 1
            ok2 &= acc & mask == cols[-k]
            events += bin(E[k] & mask).count("1")
            cells += n[-k]
    print("RG-C2", "PASS" if ok2 else "FAIL", f"({TRIALS} right halves, depths 2 .. {DEPTH})")
    dens = events / cells
    print(f"edge-event density over depths 2 .. {DEPTH}: {dens:.4f} ({events} of {cells} cells)")
    print("unexpected check", "HELD" if 0.20 <= dens <= 0.30 else "REFUTED")


if __name__ == "__main__":
    main()
