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
