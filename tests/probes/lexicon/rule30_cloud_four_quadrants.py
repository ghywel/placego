#!/usr/bin/env python3
"""rule30_cloud_four_quadrants.py: ordered or coin-like, down the columns and along the diagonals, around a 0101 centre.

RUN-ON:     cpu (Python 3 standard library; columns as big integers over time)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_four_quadrants.py [N=4096] [D=1024]
COST:       expected well under a minute.

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


if __name__ == "__main__":
    main()
