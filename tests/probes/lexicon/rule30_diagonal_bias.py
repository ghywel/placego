#!/usr/bin/env python3
"""rule30_diagonal_bias.py: DB, the exact light-speed diagonal correlation rho_k of CL078 beyond Cloud's k = 12, for row
20's open sign question (is (-1)^k rho_k > 0 for every k?). Local's run (chat L416), predictions pushed before it.

RUN-ON:     cpu (Python 3, a C compiler; the kernel rule30_diagonal_bias.c, threaded); minutes to about an hour
COMMAND:    python3 tests/probes/lexicon/rule30_diagonal_bias.py [THREADS=8] [CAP_MINUTES=90]

rho_k = E (-1)^(x_0(0) xor x_k(k)) on fair rows = 1 - 2 N_k / 4^k, where N_k counts the words w of x_0(1) .. x_0(2k)
with g_k(w) = 1 (left permutivity; Cloud's `rule30_cloud_alternation.py`, RULE30-PRIZE.md §8.70 third addendum). The
kernel enumerates all 4^k words, bit-sliced and split across threads; its binary is built in the scratch directory, not
in the repository. The ladder runs k = 1, 2, ... and stops before a k whose time, extrapolated from the last one (cost
x 4 x (k + 1)^2 / k^2), would pass the cap.

PREDICTIONS (Local's, published before the run):
  DB-C1 (control): k = 1 .. 12 reproduce Cloud's exact values (-1/2, 1/4, -1/4, 5/32, -5/64, 77/1024, -141/2048,
        39/512, -3273/65536, 2785/131072, -21759/1048576, 27905/2097152), and k = 1 .. 6 agree with a literal Python
        evolution of every word.
  DB-P1 (blind, confidence 0.7): the sign alternates at every new lag reached: (-1)^k rho_k > 0 for k = 13 .. KMAX.
  DB-P2 (blind, confidence 0.6): |rho_k| < |rho_12| = 0.01331 for every k from 16 to KMAX.
  DB-D1 (descriptive): the exact values, |rho_(k+1) / rho_k|, and the 2-adic size of each numerator.
  Counterfactual: a positive (-1)^k rho_k at some k would refute the all-lag alternation outright (one exact lag
  suffices), and GC777's even/odd white-driver parity reduction would have to show the sign change there.
  After the run (descriptive, not a prediction): the integers 4^k |rho_k| are looked up in OEIS.
OUTCOME, 2026-10-09 15:05 BST (M5, 8 threads, run at commit 0e144133; the ladder stopped before k = 22, about 154 min):
  DB-C1 PASS (k = 1 .. 12 equal Cloud's values; k = 1 .. 6 equal the literal evolution). DB-P2 HELD (|rho_k| < 0.01331
  for k = 16 .. 21).
  DB-P1 REFUTED. rho_13 .. rho_21 = -29327/2^23, +232275/2^26, -954569/2^28, +6558911/2^30, +416163/2^31,
    -8682903/2^32, -71816115/2^36, -523202389/2^38, +2833481325/2^40 (-0.003496, +0.003461, -0.003556, +0.006108,
    +0.000194, -0.002022, -0.001045, -0.001903, +0.002577). (-1)^k rho_k > 0 holds for every k <= 16 and at k = 19,
    and fails at k = 17, 18, 20 and 21: after k = 16 the sign pattern is +, -, -, -, + rather than alternating.
  D1: |rho_(k+1)/rho_k| for k = 12 .. 20: 0.263, 0.990, 1.027, 1.718, 0.032, 10.43, 0.517, 1.821, 1.354. The magnitude
    stops falling at about k = 13 and sits between 0.0002 and 0.0061 to k = 21. The integers 4^k |rho_k| are 2, 4,
    16, 40, 80, 308, 1128, 4992, 13092, 22280, 87036, 223240, 234616, 929100, 3818276, 26235644, 3329304, 138926448,
    287264460, 2092809556, 11333925300; reduced denominators 2^1 .. 2^40, never 4^k after k = 2.
  Instrument check, after the run: an independent kernel (rule30_diagonal_bias_direct.c: every row x_0(0 .. 2k) as one
    word, stepped by the plain formula, counting x_k(k) != x_0(0) over all 2^(2k+1) rows, no left-permutivity
    reduction) gives the same exact counts for k = 1 .. 18, so the refuting lags 17 and 18 rest on two methods.
  OEIS (after the run): neither 2, 4, 16, 40, 80, 308, 1128, 4992 nor the counts N_k = 3, 6, 40, 108, 552, 1894, 8756,
    30272 is in the database (2026-10-09).
  Reading: the all-lag alternation CL078 asked about is false; it first fails at k = 17. Not shown: any decay law; whether |rho_k| tends to 0; any pattern in the later signs.
"""
import os
import subprocess
import sys
import time
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
CLOUD = [F(-1, 2), F(1, 4), F(-1, 4), F(5, 32), F(-5, 64), F(77, 1024), F(-141, 2048), F(39, 512), F(-3273, 65536),
         F(2785, 131072), F(-21759, 1048576), F(27905, 2097152)]


def literal(k):
    """N_k by evolving every word of x_0(0 .. 2k) literally and counting x_k(k) != x_0(0), over w only (x_0(0) = 0)."""
    n = 0
    for w in range(1 << (2 * k)):
        row = [0] + [(w >> i) & 1 for i in range(2 * k)]
        for _ in range(k):
            row = [row[i - 1] ^ (row[i] | row[i + 1]) for i in range(1, len(row) - 1)]
        n += row[0]
    return n


def build():
    exe = os.path.expanduser('~/np-scratch-int/rule30-db/rule30_diagonal_bias')
    os.makedirs(os.path.dirname(exe), exist_ok=True)
    subprocess.run(['cc', '-O3', '-march=native', '-o', exe, os.path.join(HERE, 'rule30_diagonal_bias.c'), '-lpthread'],
                   check=True)
    return exe


def main():
    threads = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    cap = 60 * float(sys.argv[2]) if len(sys.argv) > 2 else 90 * 60
    exe = build()
    rho = {}
    lit_ok = all(literal(k) == (1 - CLOUD[k - 1]) * 4 ** k / 2 for k in range(1, 7))
    for k in (1, 2):
        rho[k] = 1 - F(2 * literal(k), 4 ** k)
    k, last = 3, None
    while True:
        if last is not None and last * 4 * (k / (k - 1)) ** 2 > cap:
            print('stop: k = %d would take about %.0f min' % (k, last * 4 * (k / (k - 1)) ** 2 / 60), flush=True)
            break
        t0 = time.time()
        out = subprocess.run([exe, str(k), str(threads)], capture_output=True, text=True, check=True).stdout.split()
        last = time.time() - t0
        assert int(out[0]) == k
        rho[k] = 1 - F(2 * int(out[1]), 4 ** k)
        r = rho[k]
        num = abs(r.numerator)
        v2 = (num & -num).bit_length() - 1 if num else None
        print('k = %2d: rho = %s = %+.6f; 4^k |rho| = %d; ratio %s; %.1f s' % (
            k, r, float(r), abs(r) * 4 ** k, '%.4f' % abs(float(r / rho[k - 1])) if k - 1 in rho else '-', last),
            flush=True)
        k += 1
    kmax = max(rho)
    c1 = lit_ok and all(rho[k] == CLOUD[k - 1] for k in range(1, 13) if k in rho)
    print('DB-C1', 'PASS' if c1 and kmax >= 12 else 'FAIL')
    print('DB-P1', 'HELD' if all((-1) ** k * rho[k] > 0 for k in range(13, kmax + 1)) else 'REFUTED',
          '(k = 13 .. %d)' % kmax)
    big = [k for k in range(16, kmax + 1) if abs(rho[k]) >= abs(CLOUD[11])]
    print('DB-P2', ('HELD' if not big else 'REFUTED at k = %s' % big) if kmax >= 16 else 'NOT REACHED')
    print('integers 4^k |rho_k|:', ', '.join(str(abs(rho[k]) * 4 ** k) for k in sorted(rho)))
    print('COMPLETE')


if __name__ == '__main__':
    main()
