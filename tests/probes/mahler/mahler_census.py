#!/usr/bin/env python3
"""mahler_census.py: the Mahler record census, the first block of the Mahler room (MAHLER.md section 1; L708).

For every start n in [1, 2^w), the survival horizon H(n) is the number of steps after which no xi in [n, n+1) keeps
every fractional part {xi (3/2)^j} in [0, 1/2), i.e. CL092's H. A Z-number below 2^w exists iff some n in [1, 2^w)
has H(n) = infinity. The walk is exact (mahler_census.c, 128-bit integers; stragglers alive at step 124 are replayed
here with Python integers and exact fractions).

RUN-ON:     cpu, the C walker in parallel over the low PREFIXBITS bits of n; minutes to hours depending on w.
COMMAND:    python3 tests/probes/mahler/mahler_census.py W [WORKERS=8] [PREFIXBITS=6]
            python3 tests/probes/mahler/mahler_census.py control

Record searched (record_find, 2026-10-14 07:55 BST): 'Z-number.*verif|verif.*Z-number|no Z-number below' -> 2 hits in
2 files (no census); 'Mahler.*census|record horizon|H\\*\\(w\\)' -> 10 hits in 5 files (CL092's horizons to 2^20,
GC931's fixed-code residue); 'mahler_horizon|ceil\\(3' -> 31 hits in 13 files (CL092, G50/G51, GC663/664). The
literature survey (PRIOR-ART.md, today) found no published large-scale check.

PREDICTIONS (written 2026-10-14 07:55 BST, before any run of this driver; the walker's control at w = 12, C0, was run
  first and is recorded here as done).
  C0 must hold (done before this file, recorded): the walker's horizon histogram equals CL092's exact-fraction H on
     every n in [1, 2^12), with H(1 .. 5) = 4, 3, 2, 12, 6 and maximum 29 (at n = 149).
  M1 must hold (instrument at scale): at w = 20 the walker's whole horizon histogram equals the exact-fraction one
     computed independently in Python (CL092's H), with maximum 47 (CL092).
  M2 must hold (the free bits pay exactly): for T < w, #{n < 2^w : H(n) > T} = 2^(w - T) A(T), with A(T) the same
     at every w (it counts the admissible parity words of length T); reported A(T) and A(T+1)/A(T) -> 3/2.
  M3 blind (0.7): the record horizons H*(w) = max_{n < 2^w} H(n) satisfy 2.2 w <= H*(w) <= 2.7 w at every w >= 24
     computed (coin law: w + 0.585 w / 0.415 = 2.41 w). Counterfactual: some H*(w) > 3 w, an anomalously long
     survivor, which would be the most interesting outcome.
  M4 (the verification): every n in [1, 2^w) has a finite horizon, so no Z-number lies below 2^w. A failure would be
     a Z-number candidate, replayed exactly before any claim.
  M5 (reported): the tail ratio N(h+1)/N(h) for h > w (CL092: about 3/4).
  Unexpected check: the walker's n = 0 path (the all-zero code, xi = 0) is excluded and never counted; we confirm the
     histogram total is exactly 2^w - 1.

OUTCOME (control, 2026-10-14 07:56 BST, M5, 23 s): M1 HELD on the second run. The first run FAILED (the histograms
  differed, maximum 47 matched). The cause was the walker's prefix replay: a window dying inside the fixed chunk bits
  recorded its whole family of 2^(w - T - 1) starts in every chunk sharing those bits, overcounting early deaths. Now
  each chunk records only its own 2^(w - PREFIXBITS) starts. Rerun: the walker's w = 20 histogram equals the exact
  fractions, maximum 47 at n = 690773.

OUTCOME (census, 2026-10-14 08:18 BST, M5, 9 workers; machine output quoted): M2 HELD, M3 REFUTED (narrowly), M4 HELD
  to w = 63, M5 as reported; the unexpected check held (each total is exactly 2^w - 1).
  w : H*(w) at n (H*/w), stragglers replayed exactly
  24:  59 at 13272845 (2.458)            28:  61 at 119104516 (2.179)
  32:  76 at 3097089134 (2.375)          36:  93 at 27255143437 (2.583)
  40:  99 at 704731028141 (2.475)        44: 106 at 8255931584461 (2.409)
  48: 120 at 119619616250377 (2.500)     52: 130 at 4473844327117093 (2.500), 1 straggler
  56: 137 at 9850069454682037 (2.446), 44 stragglers
  60: 143 at 439797727552450048 (2.383), 634 stragglers, 237 s
  63: 157 at 1541211973603965806 (2.492), 4499 stragglers, 798 s
  M4: every start in [1, 2^63) has a finite horizon, so no Z-number lies below 2^63 = 9.22e18. No candidate
     appeared, and every straggler alive at step 124 died in the exact replay.
  M2: (#{n >= 1 : H(n) > T} + 1) / 2^(w - T) = A(T) is integral and identical at every w:
     2, 3, 5, 8, 12, 18, 27, 40, 60, 90, 134, 201, 302, 452, 678, 1018, 1527, 2291, 3438, 5157, ...
     A(T + 1) / A(T) tends to 3/2. It is not the ceil(3x/2) iterates (they differ from T = 8, 40 against 41).
  M3: H*(w)/w lies in 2.18 .. 2.58. w = 28 (2.179) breaks the registered lower bound of 2.2, so M3 is refuted.
     The counterfactual (some H* > 3w) did not occur.
  M5: tail ratio N(h+1)/N(h) for h > w, mean 0.744 .. 0.752 at every w (CL092's 3/4).
  Reading (MEASURED): the record horizons follow the coin law, about 2.4 w, with no anomalous survivor, and the
  record holders show no binary structure (mostly odd, no shared low bits). This is evidence, not proof (Turing's
  p. 253: any finite range is checkable; "forever" is not reached this way).
"""
import os, subprocess, sys, time
from collections import Counter
from fractions import Fraction as F
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
BIN = os.path.join(os.path.expanduser('~/np-scratch-int'), 'mahler', 'mahler_census_bin')


def H_exact(g, cap=100000):
    a, b, gn, n = F(g), F(g) + F(1, 2), g, 1
    while n < cap:
        G = (3 * gn + 1) // 2
        a, b = max(F(3, 2) * a, F(G)), min(F(3, 2) * b, G + F(1, 2))
        if a >= b:
            return n
        gn, n = G, n + 1
    return None


def build():
    os.makedirs(os.path.dirname(BIN), exist_ok=True)
    subprocess.run(['cc', '-O3', '-o', BIN, os.path.join(HERE, 'mahler_census.c')], check=True)


def chunk(args):
    w, pb, prefix = args
    out = subprocess.run([BIN, str(w), str(pb), str(prefix)], capture_output=True, text=True, check=True).stdout
    hist, strag, mx = Counter(), [], (0, 0)
    for line in out.splitlines():
        f = line.split()
        if f[0] == 'H':
            hist[int(f[1])] += int(f[2])
        elif f[0] == 'S':
            strag.append(int(f[1]))
        elif f[0] == 'MAX':
            mx = (int(f[1]), int(f[2]))
    return hist, strag, mx


def census(w, workers, pb):
    pb = min(pb, w - 1)
    hist, strag, best = Counter(), [], (0, 0)
    with Pool(workers) as pool:
        for h, s, mx in pool.imap_unordered(chunk, [(w, pb, p) for p in range(1 << pb)]):
            hist.update(h); strag.extend(s)
            if mx[0] > best[0]:
                best = mx
    for n in strag:                                   # exact replay of the starts alive at step 124
        h = H_exact(n)
        if h is None:
            print('Z-NUMBER CANDIDATE (alive at 100000 steps):', n, flush=True)
            continue
        hist[h] += 1
        if h > best[0]:
            best = (h, n)
    return hist, best, len(strag)


def control():
    build()
    hist, best, ns = census(20, 8, 6)
    exact = Counter(H_exact(g) for g in range(1, 1 << 20))
    print('M1 w=20 walker histogram equals exact fractions:', hist == exact, '| max', best, flush=True)


def main():
    if sys.argv[1] == 'control':
        control()
        return
    w = int(sys.argv[1])
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    pb = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    build()
    t0 = time.time()
    hist, best, ns = census(w, workers, pb)
    total = sum(hist.values())
    print('w=%d: starts %d (2^w - 1 = %d), max horizon %d at n = %d, stragglers replayed %d, %.0f s' % (
        w, total, (1 << w) - 1, best[0], best[1], ns, time.time() - t0), flush=True)
    surv = {}
    acc = 0
    for h in sorted(hist, reverse=True):
        acc += hist[h]
        surv[h - 1] = acc                             # #{n : H(n) > h-1}
    A = {T: surv.get(T, 0) / 2 ** (w - T) for T in range(1, w)}
    print('A(T) for T = 1 .. min(w-1, 30):', [int(A[T]) if A[T] == int(A[T]) else A[T] for T in range(1, min(w, 31))])
    tail = [hist[h + 1] / hist[h] for h in range(w + 1, best[0]) if hist[h] >= 200 and hist[h + 1] > 0]
    print('tail ratio N(h+1)/N(h), h > w with N(h) >= 200: mean %.4f over %d values' % (
        sum(tail) / len(tail) if tail else float('nan'), len(tail)))
    print('H*(w)/w = %.3f' % (best[0] / w))
    print('HIST', ' '.join('%d:%d' % (h, hist[h]) for h in sorted(hist)))


if __name__ == '__main__':
    main()
