#!/usr/bin/env python3
"""rule30_window.py: the window principle on the Rule 30 side. A block of two adjacent columns can recur at a later
time only if it is no longer than the left edge is far. (Local, 2026-10-05; RULE30-PRIZE.md section 8.58; the
Collatz twin is tests/probes/prizes/collatz_window.py and COLLATZ-PRIZE.md section 5.)

RUN-ON:     cpu, one core (Python 3 with numpy)
COMMAND:    python3 tests/probes/lexicon/rule30_window.py [WMAX=9]
COST:       about two minutes.

THE STATEMENT (Theorem A', proved in section 8.58; it contains Theorem A of section 8.54). Take a nonzero
configuration whose leftmost black cell at time 0 is L >= 0 cells to the left of column i. If the pair of columns
(i, i+1) shows the same block of n consecutive values starting at times a and a' > a, then n <= L + a'.
The proof in one line: two equal blocks of length n force the rows at times a and a' to agree at the n - 1 cells
left of column i (Rule 30 read from right to left), and the later row has its leftmost black cell L + a' cells
out, where the earlier row is white.

PREDICTIONS, written 2026-10-05 before this script's first run.
  WN1 (Theorem A', must hold): for every seed of width 1 to WMAX, every column pair from the seed's left end to 8
      cells past its right end, and every pair of times a < a' <= 120 whose common block ends before the horizon
      (160 steps): the common block's length n is at most L + a'.
  WN2 (blind; how tight): the bound is attained (n = L + a') for at least one seed of width 3 or more with
      a' >= 2, and the largest n / (L + a') over pairs with a' >= 40 is below 0.5 (late blocks are far from it).
  CF  (counterfactual, must fail): the bound n <= L + a, with the earlier time, is violated.
REFUTED-BY: WN1 or CF failing (the proof or the instrument); WN2 the other way.

OUTCOME of the first run, 2026-10-05 (WMAX 9, 17 seconds): WN1 PASSED (7,436,643 recurring blocks, 0 violations).
  CF PASSED (20,179 violations with the earlier time). WN2 REFUTED in its first half: the bound n = L + a' is never
  attained with a' >= 2 by a seed of width 3 or more (it is attained at a' = 1 by the seed 101, section 8.54); its
  second half held (largest late ratio 0.255). Post hoc, with 400 steps: the longest block that recurs at a late
  time a' is 15, 18, 18 and 19 cells for a' in [40, 80), [80, 160), [160, 240) and [240, 360). That is the growth
  of a coin's longest match (a logarithm of the number of pairs), not a share of the bound, so the ratio falls from
  0.26 at a' = 40 to 0.07 by a' = 300. The 0.255 sits near Rule 30's leftward speed only by accident.
"""
import sys
import numpy as np

WMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 9
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def step(x):
    left = np.zeros_like(x); left[1:] = x[:-1]
    right = np.zeros_like(x); right[:-1] = x[1:]
    return left ^ (x | right)


def main(T=160, amax=120):
    viol = cf_viol = blocks = 0
    attained = []
    late_ratio = 0.0
    for w in range(1, WMAX + 1):
        inner = max(w - 2, 0)
        for s in range(1 << inner):
            bits = [1] + [(s >> i) & 1 for i in range(inner)] + ([1] if w > 1 else [])
            width = w + 2 * T + 8
            x = np.zeros(width, dtype=np.uint8)
            off = T + 4
            x[off:off + w] = bits
            hist = np.zeros((T + 1, width), dtype=np.uint8)
            hist[0] = x
            for t in range(T):
                x = step(x); hist[t + 1] = x
            for L in range(0, w + 8):
                i = off + L
                pair = hist[:, i].astype(np.int16) * 2 + hist[:, i + 1]
                for d in range(1, amax + 1):
                    eq = pair[:T + 1 - d] == pair[d:]
                    m = len(eq)
                    a = np.arange(m)
                    nextfalse = np.minimum.accumulate(np.where(eq, m, a)[::-1])[::-1]
                    run = nextfalse - a                         # run[t]: the common block's length from time t
                    complete = (nextfalse < m) & (a + d <= amax) & (run > 0)
                    if not complete.any():
                        continue
                    n = run[complete]
                    a2 = a[complete] + d
                    blocks += int(complete.sum())
                    viol += int((n > L + a2).sum())
                    cf_viol += int((n > L + a[complete]).sum())
                    hit = (n == L + a2) & (a2 >= 2)
                    if hit.any() and w >= 3:
                        k = int(np.argmax(hit))
                        attained.append((w, s, L, int(a[complete][k]), int(a2[k]), int(n[k])))
                    late = a2 >= 40
                    if late.any():
                        late_ratio = max(late_ratio, float((n[late] / (L + a2[late])).max()))
    report("WN1 Theorem A': a recurring block is no longer than L + a'", viol == 0,
           f"{blocks} recurring blocks, {viol} violations")
    report("CF  with the earlier time a the bound is violated", cf_viol > 0, f"{cf_viol} violations")
    verdict("WN2 attained for some seed of width >= 3 with a' >= 2, and below half the bound from a' = 40 on",
            len(attained) > 0 and late_ratio < 0.5,
            f"{len(attained)} attaining cases" + (f", e.g. width {attained[0][0]} seed {attained[0][1]} L "
            f"{attained[0][2]} times {attained[0][3]}, {attained[0][4]} block {attained[0][5]}" if attained else "")
            + f"; largest late ratio {late_ratio:.3f}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


if __name__ == "__main__":
    main()
