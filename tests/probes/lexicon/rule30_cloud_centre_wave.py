#!/usr/bin/env python3
"""rule30_cloud_centre_wave.py: CW, can a wave from the imposed centre reach the right edge and come back as the
ruler?

RUN-ON:     cpu (Python 3 standard library; big-integer rows)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_centre_wave.py [T=4096] [W=64]
COST:       seconds.

Why (the owner, 2026-10-09, after CL096). "The centre column is the order we impose. What I am imagining [is] a wave
that emits from the center, travels right, reaches the wall and bounces back. This is the ruler ... the ruler is not
the source of the wave, it is the reflection of the wave from the centre as it bounces off the wall."

Reasoning before the run (Cloud, by hand; exact).
  W1. The centre's wave moves right at exactly one cell a row. Compare two worlds that differ only in the clamped
      column 0. At the rightmost differing cell c, x'(c + 1) = x(c) xor (x(c + 1) or x(c + 2)) with the last two
      inputs equal, so the difference always moves to c + 1. That is left permutivity.
  W2. The wall moves right at exactly one cell a row too: a finite right half's rightmost black cell advances one
      cell every row. So a wave from the centre never closes the gap. It stays exactly as far behind the wall as it
      started, for ever.
  W3. The strip by the wall is causally closed. Measure distance d from the right edge. A cell at distance d depends
      only on the cells at distances d, d - 1 and d - 2 one row earlier: the right-edge frame is a T-function
      (RULE30-PRIZE.md section 8.77, R -> R xor (2R or 4R)). So the ruler is fixed by the initial cells nearest the
      edge alone, and nothing the centre does can reach it. The ruler is the edge's own order, as the left band is
      the left edge's.

PREDICTIONS, written 2026-10-09 20:12 BST, before any run of this script (T = 4096, W = 64, 16 random right halves).
  CW-C1 (exact, W1): with column 0 clamped to 0101... in one world and to all-white in the other, the rightmost
        cell where the two differ is at column t - 1 at every row t >= 1. The clamps first differ at row 1.
  CW-C2 (exact, W2 and W3): the two worlds' cells at distances 0 .. W - 1 from the right edge agree at every row,
        and the gap between the edge and the wave's front is exactly W + 1 at every row.
  CW-U, the unexpected check (0.5): behind the front, the centre's wave changes about half the cells. Between 40%
        and 60% of the cells at distances W + 2 .. 2W from the edge differ between the two worlds, over rows t >= W.
  Counterfactual. Any difference within distance W of the edge would mean the centre's wave reaches the wall,
  and that the T-function argument is wrong.

OUTCOME of the first run, 2026-10-09 (T = 4096, W = 64, 16 right halves; seconds).
  CW-C1 PASS: the difference front sits at column t - 1 in every row of every run (0 exceptions).
  CW-C2 PASS: no cell within distance 63 of the edge ever differs, and the gap between edge and front is exactly 65
    (W + 1) at every row of every run.
  CW-U HELD: behind the front, 50.0% of the cells at distances 66 .. 128 differ between the two worlds.
  Reading: the centre's wave is real. It travels right at exactly one cell a row and changes half of everything
  behind it. But the wall runs ahead at the same speed, so the wave never arrives and nothing comes back. The ruler
  is the right edge's own order, made by the edge from the seed's nearest cells. The three orders are each anchored
  to their own source: the left band to the left edge, the ruler to the right edge, and the wheel's block to the
  imposed centre.
  SCOPE (added 2026-10-09 after GPT's GC856). The barrier holds for any two binary centre clamps on the same finite
  right half: if they first differ at row tau, the damage front is at t - tau and the gap is W + tau. It says nothing
  against news travelling from the edge to the centre, which KR measures. That leftward speed of 0.246 is for random
  backgrounds.
"""
import random
import sys

T = int(sys.argv[1]) if len(sys.argv) > 1 else 4096
W = int(sys.argv[2]) if len(sys.argv) > 2 else 64


def run(cells, clamp, T):
    row, rows = cells, []
    for t in range(T):
        row = (row & ~1) | clamp(t)
        rows.append(row)
        row = (row << 1) ^ (row | (row >> 1))
    return rows


def main():
    bad_front = bad_strip = 0
    gaps, diff_cells, all_cells = set(), 0, 0
    for seed in range(16):
        rnd = random.Random(400 + seed)
        cells = (rnd.getrandbits(W) | (1 << (W - 1))) << 1      # sites 1 .. W, site W black
        a = run(cells, lambda t: t % 2, T)
        b = run(cells, lambda t: 0, T)
        for t in range(1, T):
            d = a[t] ^ b[t]
            front = d.bit_length() - 1 if d else -1
            if front != t - 1:
                bad_front += 1
            edge = max(a[t].bit_length(), b[t].bit_length()) - 1
            strip = ((1 << W) - 1) << (edge - W + 1)
            if (a[t] ^ b[t]) & strip:
                bad_strip += 1
            gaps.add(edge - front)
            if t >= W:
                band = ((1 << (W - 1)) - 1) << (edge - 2 * W)           # distances W + 2 .. 2W
                diff_cells += ((a[t] ^ b[t]) & band).bit_count()
                all_cells += W - 1
    print('CW-C1: rows where the difference front is not at column t - 1: %d' % bad_front)
    print('CW-C2: rows with any difference within distance %d of the edge: %d; gaps seen: %s'
          % (W - 1, bad_strip, sorted(gaps)[:6]))
    print('CW-U: cells at distances %d .. %d from the edge that differ between the worlds: %.1f%%'
          % (W + 2, 2 * W, 100 * diff_cells / all_cells))


if __name__ == '__main__':
    main()
