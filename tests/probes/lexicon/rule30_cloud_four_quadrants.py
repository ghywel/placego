#!/usr/bin/env python3
"""rule30_cloud_four_quadrants.py: ordered or coin-like, down the columns and along the diagonals, around a 0101 centre.

RUN-ON:     cpu (Python 3 standard library; columns as big integers over time)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_four_quadrants.py [N=4096] [D=1024]
COST:       about 5 s (the main run took 1 s).

Why (the owner, 2026-10-09): "If the deterministic side has coin flip verticals and orderly diagonals, rather than
the wave front crossing the centre column to put it in the correct band for it's state as a test, does there exist on
the centre column the inverse - an orderly vertical (which it already is) and coin-flip diagonals (unknown)".

The four combinations, from the record before this run:
  coin-like columns, ordered left diagonals: the band (§8.74; columns measured coin-like in the shunted-column run);
  coin-like columns, coin-like diagonals:    the core (§8.34, §8.70; measured);
  ordered column, ordered diagonals:         ring orbits, such as the necklace, whose clock reads 010101 (§8.71);
  ordered column, coin-like diagonals:       the period-2 hypothetical, measured here.
A fact from the record that shapes the question: in any finite configuration every diagonal, in either direction,
is eventually periodic. Each family is a closed system anchored at its own edge (left, D_e depends on D_(e-1),
D_(e-2) and itself, §8.74; right, the same from the right edge, §8.27), and both edges move at light speed. So only
columns can be the open question, and no two adjacent columns can both be eventually periodic (Jen).
The construction (§5, §7): column 0 is tau = 0101... (black at odd rows), column 1 is sigma, and every column to the
left is forced, x_t(-k) = x_(t+1)(-k+1) xor (x_t(-k+1) or x_t(-k+2)). Two kinds of sigma: fair random bits (Conjecture
LR's setting, every column 1), and column 1 of a random finite right half of width 16 driven by tau (statement B's
setting). A left diagonal through the centre is the cells (t0 + k, -k), k = 0 .. 511; a right diagonal is
(t0 + k, k) in the driven right half.

PREDICTIONS, written 2026-10-09 13:32 BST, before any run of this script (N = 4096 rows, D = 1024 forced columns,
four sigmas of each kind, left and right diagonals from 64 starting rows t0 each).
  FQ1 (0.75). In the forced left half, left diagonals through the centre are coin-like: pooled flip rate and density
      within 0.02 of 1/2, at least 250 of the 256 eight-bit words in each diagonal, none with a period of at most a
      quarter of its length. For both kinds of sigma.
  FQ2 (0.7). In the driven right half, right diagonals flip at 3/4 within 0.02 (the light-speed OR law, §8.70, which
      the 0101 column does not change), with density within 0.02 of 1/2, and none periodic as in FQ1 except
      possibly those with t0 < 40. Amended before the run, on rereading §8.27: a right diagonal of a finite right
      half lies at a fixed depth (16 + t0) from its right edge and is eventually periodic, with period about
      2^(0.35 depth), so shallow ones can repeat within 512 cells.
  FQ3 (0.8). Columns -3 to -1024 are coin-like (pooled flip rate and density within 0.02 of 1/2). Column -1 is black
      at every odd row (R0, a check), with density 3/4 within 0.02 for random sigma.
  FQ4, the unexpected check (0.6). The longest white run along any measured left diagonal is at most 30 cells: the
      forced half never goes quiet along a diagonal for long (the record's realizable white runs along columns are
      7 to 16 for depths to 93; PERIOD-TWO.md Q6).
  Counterfactual. If FQ1 fails with ordered left diagonals, the hypothetical would carry the band's kind of order
      next to an ordered column, the ring orbits' quadrant, which is known only on infinite periodic rows. If FQ1
      holds, the inverse the owner describes is locally self-consistent, which is why no local check excludes it.

OUTCOME of the first run, 2026-10-09 (1 s).
  FQ1 PART. Held: left diagonals through the centre flip at 0.5041 (random sigma) and 0.5018 (driven), with density
    0.4998 and 0.4993, and none is periodic. Refuted as worded: the fewest distinct 8-bit words in a diagonal are
    199 and 201, not at least 250. The threshold was miscalibrated: post hoc, 256 fair-coin sequences of 512 cells
    have 220 words on average and 200 at fewest, so the diagonals are at a coin's level.
  FQ2 HELD. Right diagonals in the driven right half flip at 0.7500, density 0.4991, none periodic.
  FQ3 HELD. Columns -3 to -1024 (every 31st): flip 0.4921 and density 0.4994 (random sigma), 0.4847 and 0.5175
    (driven). Column -1 is black at every odd row in all eight runs, density 0.7493 for random sigma.
  FQ4 HELD. The longest white run along a measured left diagonal is 14 (random) and 17 (driven).
  Post hoc, not predicted (posthoc() below, run after the outcome was seen), and the finding of the run. With a
    finite right half, the 0101 centre comes with a strip of vertical order. Column 1 is the record's wheel (§8.5):
    13 to 18 distinct 8-bit words over 4,096 rows, density 0.41. The forced columns -1 to -10 average 14 to 21 words of
    256. They fade to coin-like by about column -150 and show all 256 beyond -250 (four right halves of width 16).
    Through that strip the left diagonals stay coin-like (FQ1). That is the owner's inverse, an ordered vertical
    with coin-like diagonals, and it is a strip, not a single column. With random sigma (LR's setting) the strip is
    only about ten columns wide, where R0's forcing acts. In the single seed, every column from -40 to 40 shows all
    256 words over rows 2048 to 6143. Scope: four right halves of width 16 and 4,096 rows. A counterexample's right
    half is whatever its row holds when the period starts, and the record's wheel is kicked by its right side
    (§8.11), so how ordered the strip would be there is not measured. In one driven run column -1 is 0.893 black
    and column -2 0.214, and 2(0.893) + 0.214 = 2.000, as §8.34's lemma requires.
  Scope, added after GPT's GC782. stats() tests only the second half of a sequence, for periods up to a quarter of
    that half (64 on diagonals): read "periodic 0" as no tested suffix period <= 64, not the registered quarter of
    the full length. FQ3 samples every 31st column (3, 34, ..., 995). posthoc() draws a different four right halves
    from main()'s, because its random stream is consumed differently. The 0.7500 is measured on these draws; the OR
    law's 3/4 needs fair drivers. Few distinct words is finite variety, not order.
"""
import random
import sys

N = int(sys.argv[1]) if len(sys.argv) > 1 else 4096
D = int(sys.argv[2]) if len(sys.argv) > 2 else 1024
K = 512
L = N + D + K + 4


def tau_int(n):
    return sum(1 << t for t in range(1, n, 2))      # 0101..., black at odd rows


def driven_sigma(rnd, n, w=16):
    """A finite right half of width w driven on its left by tau. Row bit i is site i (bit 0 is site 0 = tau)."""
    row, rows = (rnd.getrandbits(w) | 1) << 1, []
    for t in range(n):
        row = (row & ~1) | (t % 2)                   # impose tau(t) on site 0
        rows.append(row)
        row = (row << 1) ^ (row | (row >> 1))        # site i: site i-1 xor (site i or site i+1)
    sigma = sum(((rows[t] >> 1) & 1) << t for t in range(n))
    return sigma, rows


def forced_columns(tau, sigma, n, depth):
    cols = {0: tau, 1: sigma}
    mask = (1 << n) - 1
    for k in range(1, depth + 1):
        a, b = cols[-k + 1], cols[-k + 2]
        cols[-k] = ((a >> 1) ^ (a | b)) & (mask >> k)
    return cols


def bits(v, n):
    return [(v >> t) & 1 for t in range(n)]


def stats(seq):
    n = len(seq)
    flips = sum(seq[i] != seq[i - 1] for i in range(1, n))
    w8 = len({tuple(seq[i:i + 8]) for i in range(n - 7)})
    half = seq[n // 2:]
    per = next((q for q in range(1, len(half) // 4 + 1)
                if all(half[i] == half[i + q] for i in range(len(half) - q))), None)
    run = best = 0
    for x in seq:
        run = run + 1 if x == 0 else 0
        best = max(best, run)
    return flips, n - 1, sum(seq), n, w8, per, best


def main():
    rnd = random.Random(30)
    tau = tau_int(L)
    starts = [rnd.randrange(0, N - K - 4) for _ in range(64)]
    report = {}
    for kind in ("random", "driven"):
        acc = {"ld": [], "rd": [], "col": [], "m1": []}
        for _ in range(4):
            if kind == "random":
                sigma, rows = rnd.getrandbits(L), None
            else:
                sigma, rows = driven_sigma(rnd, L)
            cols = forced_columns(tau, sigma, L, D)
            assert all((cols[-1] >> t) & 1 for t in range(1, N, 2)), "R0 fails: column -1 not black at odd rows"
            colbits = {k: cols[-k] for k in range(1, D + 1)}
            for t0 in starts:
                diag = [(colbits[k] >> (t0 + k)) & 1 if k else (tau >> t0) & 1 for k in range(K)]
                acc["ld"].append(stats(diag))
                if rows is not None:
                    rdiag = [(rows[t0 + k] >> k) & 1 for k in range(K)]
                    acc["rd"].append(stats(rdiag))
            for k in range(3, D + 1, 31):
                acc["col"].append(stats(bits(colbits[k], N)))
            acc["m1"].append(stats(bits(colbits[1], N)))
        report[kind] = acc
    for kind, acc in report.items():
        print(f"sigma = {kind}")
        for name, label in (("ld", "left diagonals through the centre"), ("rd", "right diagonals (driven right half)"),
                            ("col", "columns -3 .. -1024 (every 31st)"), ("m1", "column -1")):
            rows = acc[name]
            if not rows:
                continue
            fr = sum(r[0] for r in rows) / sum(r[1] for r in rows)
            de = sum(r[2] for r in rows) / sum(r[3] for r in rows)
            w8 = min(r[4] for r in rows)
            per = [r[5] for r in rows if r[5] is not None]
            wr = max(r[6] for r in rows)
            print(f"  {label}: {len(rows)} sequences, flip rate {fr:.4f}, density {de:.4f}, fewest 8-bit words {w8},"
                  f" periodic {len(per)}, longest white run {wr}")


def posthoc():
    """Post hoc: a coin's word count for 512 cells, the driven strip's width, and the single seed's columns."""
    rnd = random.Random(7)
    w = [stats([rnd.getrandbits(1) for _ in range(K)])[4] for _ in range(256)]
    print(f"post hoc: fair coins, {K} cells: 8-bit words mean {sum(w) / len(w):.1f}, fewest {min(w)}")
    rnd = random.Random(30)
    tau = tau_int(L)
    rnd.getrandbits(L)
    for trial in range(4):
        sigma, _ = driven_sigma(rnd, L)
        cols = forced_columns(tau, sigma, L, D)
        w = [stats(bits(cols[-k], N))[4] for k in range(1, D + 1)]
        last = max(k for k in range(1, D + 1) if w[k - 1] < 200)
        bands = [(lo, round(sum(w[lo - 1:hi]) / (hi - lo + 1)))
                 for lo, hi in ((1, 10), (11, 30), (31, 60), (61, 100), (101, 150), (151, 250), (251, D))]
        print(f"  driven {trial}: column 1 has {stats(bits(sigma, N))[4]} words; last column under 200: -{last};"
              f" mean words by depth: {bands}")
    V, cols = 1, {c: [] for c in range(-40, 41)}
    for t in range(6144):
        if t >= 2048:
            for c in cols:
                cols[c].append((V >> (t + c)) & 1)
        V = (V << 2) ^ ((V << 1) | V)
    print("  single seed, rows 2048..6143, columns -40..40: fewest 8-bit words",
          min(stats(v)[4] for v in cols.values()))


if __name__ == "__main__":
    main()
    posthoc()
