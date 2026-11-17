#!/usr/bin/env python3
"""rule30_trace_width2.py: TWX, the width-2 trace counts N(n) of Rule 30 to n = 17, by the C kernel
rule30_trace_width2.c, extending TW (rule30_trace_widths.py, n <= 14). Cloud's CL086 (RULE30-PRIZE.md §8.77): this
trace's entropy is Rule 30's topological entropy, so log 2 <= h_top <= log2(N(n)) / n for every n. Local's run (chat
L435), with these predictions pushed before it.

RUN-ON:     cpu (Python 3, a C compiler; 2 GB of memory at n = 17); minutes
COMMAND:    python3 tests/probes/lexicon/rule30_trace_width2.py [THREADS=6] [NMAX=17]

PREDICTIONS (Local's, published before the run):
  TWX-C1 (control): n = 4 .. 14 equal TW's counts (80, 200, 496, 1208, 2916, 6964, 16476, 38616, 89844, 207544, 476596).
  TWX-P1 (blind, confidence 0.8): the successive ratio N(n)/N(n - 1) keeps falling at n = 15, 16 and 17.
  TWX-P2 (blind, confidence 0.75): the ratio at n = 17 is still above 2.2.
  TWX-D1 (descriptive): N(15 .. 17) and the upper bounds log2(N(n)) / n.
  Not decidable here: whether h_top exceeds log 2. These counts give only upper bounds.
OUTCOME, 2026-10-09 16:36 BST (M5, six threads, about 95 s, run at commit aab55342): TWX-C1 PASS, TWX-P1 HELD,
  TWX-P2 HELD.
  N(15) = 1089000, N(16) = 2477236, N(17) = 5615036; ratios 2.2850, 2.2748, 2.2667 (falls of 0.0136, 0.0114, 0.0102,
  0.0081 from n = 14 on, themselves shrinking). Upper bounds log2(N(n)) / n: 1.3370, 1.3275, 1.3189 bits, so
  log 2 <= h_top(Rule 30) <= 1.3189 bits (CL086's identification of h_top with this trace's entropy).
  Two naive extrapolations of the ratio (A + B/n through n = 16, 17; a geometric tail on the falls) put its limit near
  2.14 .. 2.22, about 1.10 .. 1.15 bits. That is an estimate from finite data, not a bound and not a claim that
  h_top > log 2.
"""
import math
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
TW = {4: 80, 5: 200, 6: 496, 7: 1208, 8: 2916, 9: 6964, 10: 16476, 11: 38616, 12: 89844, 13: 207544, 14: 476596}


def main():
    threads = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 17
    exe = os.path.expanduser('~/np-scratch-int/rule30-tw/rule30_trace_width2')
    os.makedirs(os.path.dirname(exe), exist_ok=True)
    subprocess.run(['cc', '-O3', '-o', exe, os.path.join(HERE, 'rule30_trace_width2.c'), '-lpthread'], check=True)
    N = {}
    for n in range(4, nmax + 1):
        t0 = time.time()
        k, c = map(int, subprocess.run([exe, str(n), str(threads)], capture_output=True, text=True,
                                       check=True).stdout.split())
        assert k == n
        N[n] = c
        print('n = %2d: N = %d; ratio %s; upper bound %.4f bits; %.1f s' % (
            n, c, '%.4f' % (c / N[n - 1]) if n - 1 in N else '-', math.log2(c) / n, time.time() - t0), flush=True)
    print('TWX-C1', 'PASS' if all(N[n] == v for n, v in TW.items() if n in N) else 'FAIL')
    r = {n: N[n] / N[n - 1] for n in N if n - 1 in N}
    print('TWX-P1', 'HELD' if all(r[n] < r[n - 1] for n in range(15, nmax + 1)) else 'REFUTED')
    print('TWX-P2', 'HELD' if r[nmax] > 2.2 else 'REFUTED', '(ratio %.4f at n = %d)' % (r[nmax], nmax))
    print('COMPLETE')


if __name__ == '__main__':
    main()
