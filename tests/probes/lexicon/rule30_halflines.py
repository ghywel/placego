#!/usr/bin/env python3
"""rule30_halflines.py: the problem as two half-lines driven by the same column 0. The right one has a wheel; does the
left one?

RUN-ON:     cpu (pure Python 3, standard library; seeded random seeds)
COMMAND:    python3 tests/probes/lexicon/rule30_halflines.py
COST:       about five minutes on one core.

The decoupling. Rule 30 at a cell uses only its two neighbours, so with column 0 given for all time, the columns to its
left evolve on their own (Rule 30 with column 0 as their right boundary), and so do the columns to its right (with
column 0 as their left boundary). Column 0 itself must also obey Rule 30: tau(t+1) = x_t(-1) XOR (tau(t) OR
x_t(1)). For tau = 0101..., that says x_t(-1) = 1 at every odd t, and x_t(1) = NOT x_t(-1) at every even t. So a
finite configuration with column 0 = 0101... for ever is a pair of finite seeds, one on each side, whose driven
half-lines produce columns -1 and 1 meeting those two conditions. All night the right half-line was studied (column 1:
the wheel and its kicks, about 0.04 bits per step, PRIZE-PROBLEMS.md section 8.20). This looks at the left one.

An exploratory look (2026-10-05, 300 random 40-cell left seeds, not recorded): column -1 of the left half-line driven
by 0101... has conditional block entropy 1.000 bits per step for blocks up to 8 (0.996 at 12), and half of its
odd-time bits are 1 (0.5005). No wheel. D1 records that; D0, D2 and D3 are new.

PREDICTIONS, written 2026-10-05 before this script's first run:
  D0 (control, exact: the decoupling): for 200 random finite configurations evolved whole for 300 steps, the left
      half-line evolved alone with column 0 clamped to the whole run's column 0 reproduces every left cell, and the
      right half-line alone reproduces every right cell.
  D1 (seen, recorded as a check): next to 0101..., column -1 of the left half-line has h_8 >= 0.98 bits per step.
  D2 (blind; the census): for column 0 = 001..., 0011... and 0001... as well, the left half-line's column -1 has
      h_8 >= 0.95 bits per step. The left side never forms a wheel, because its information flows towards column 0
      at full speed.
  D3 (blind; the asymmetry): for each of the four traces, column 1 of the right half-line (2,000-cell random seeds,
      after 600 steps) has h_24 at most a fifth of the left column's h_8, both per step.
REFUTED-BY: D0 failing (the instrument); D1, D2 or D3 failing.

OUTCOME of the first run, 2026-10-05: D0 passed (0 cells differ in 200 whole runs). The left half-line's column -1, h_8,
and the right half-line's column 1, h_24, in bits per step: 01: 0.9997 and 0.0574; 001: 0.9997 and 0.0382; 0011:
0.9998 and 0.0001; 0001: 0.9997 and 0.0000. D1, D2 and D3 HELD. The left side is pure chaos next to column 0 for
every trace; the right side is a thin channel, and for 0011 and 0001 typical right sides lock column 1 outright (by
Jen's theorem such a right half can never be a counterexample).
"""
import math, random, sys
from collections import Counter

FAILS = 0
TRACES = ["01", "001", "0011", "0001"]


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def H(seqs, k):
    joint, ctx = Counter(), Counter()
    for s in seqs:
        key, m = 0, (1 << k) - 1
        for i, b in enumerate(s):
            if i >= k:
                joint[(key, b)] += 1
                ctx[key] += 1
            key = ((key << 1) | b) & m
    n = sum(ctx.values())
    return -sum(c / n * math.log2(c / ctx[key]) for (key, b), c in joint.items())


def left_line(seed, W, T, tau):
    """Cells -1..-W (bit j-1 = cell -j); column 0 = tau(t). Returns column -1 and all rows."""
    mask = (1 << (W + T + 3)) - 1
    row, col, rows = seed, [], []
    for t in range(T):
        col.append(row & 1)
        rows.append(row)
        left = row >> 1                                  # bit j-1 gets cell -j-1
        right = ((row << 1) | tau(t)) & mask             # bit j-1 gets cell -j+1; bit 0 gets column 0
        row = (left ^ (row | right)) & mask
    return col, rows


def right_line(seed, T, tau):
    """Cells 1..W (bit i = cell i), bit 0 = column 0 = tau(t). Returns column 1 and all rows."""
    mask = (1 << (seed.bit_length() + T + 3)) - 1
    row, col, rows = (seed << 1) | tau(0), [], []
    for t in range(T):
        col.append((row >> 1) & 1)
        rows.append(row)
        row = ((((row << 1) ^ (row | (row >> 1))) & mask) & ~1) | tau(t + 1)
    return col, rows


def main():
    rng = random.Random(9090)
    # D0: whole runs against the two half-lines
    bad = 0
    for _ in range(200):
        WL, WR, T = 20, 20, 300
        off = WL + T + 2                                  # bit off + i holds cell i of the whole line
        whole = rng.getrandbits(WL + 1 + WR) << (off - WL)
        mask = (1 << (off + WR + T + 3)) - 1
        rows = []
        row = whole
        for t in range(T):
            rows.append(row)
            row = ((row << 1) ^ (row | (row >> 1))) & mask
        c0 = [(r >> off) & 1 for r in rows]
        tau = lambda t: c0[t] if t < T else 0
        lseed = sum(((rows[0] >> (off - j)) & 1) << (j - 1) for j in range(1, WL + 1))
        _, lrows = left_line(lseed, WL, T, tau)
        rseed = (rows[0] >> (off + 1)) & ((1 << WR) - 1)
        _, rrows = right_line(rseed, T, tau)
        for t in range(T):
            for j in range(1, WL + t + 1):
                bad += ((lrows[t] >> (j - 1)) & 1) != ((rows[t] >> (off - j)) & 1)
            for i in range(1, WR + t + 1):
                bad += ((rrows[t] >> i) & 1) != ((rows[t] >> (off + i)) & 1)
    report("D0 the decoupling: each half-line alone, given column 0, reproduces the whole run", bad == 0,
           f"{bad} cells differ")
    hl, hr = {}, {}
    for w in TRACES:
        tau = (lambda w: (lambda t: int(w[t % len(w)])))(w)
        ls = [left_line(rng.getrandbits(40), 40, 3000, tau)[0][400:] for _ in range(300)]
        hl[w] = H(ls, 8)
        rs = [right_line(rng.getrandbits(2000) | (1 << 1999), 4200, tau)[0][600:] for _ in range(120)]
        hr[w] = H(rs, 24)
        print(f"   trace {w}: left column -1 h_8 = {hl[w]:.4f}; right column 1 h_24 = {hr[w]:.4f} bits per step",
              flush=True)
    verdict("D1 next to 0101..., the left column -1 has h_8 >= 0.98", hl["01"] >= 0.98, f"{hl['01']:.4f}")
    verdict("D2 the left half-line never forms a wheel (h_8 >= 0.95 for 001, 0011, 0001)",
            all(hl[w] >= 0.95 for w in TRACES[1:]), ", ".join(f"{w}: {hl[w]:.4f}" for w in TRACES[1:]))
    verdict("D3 the asymmetry: right column 1's h_24 at most a fifth of the left column's h_8, for every trace",
            all(hr[w] <= hl[w] / 5 for w in TRACES), ", ".join(f"{w}: {hr[w] / hl[w]:.3f}" for w in TRACES))
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
