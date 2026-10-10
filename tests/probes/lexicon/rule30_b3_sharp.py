#!/usr/bin/env python3
"""rule30_b3_sharp.py: B3S, Lemma B3 sharpened from 2P to 2P - 1 (PROOFS.md entry 12), checked on every small seed.

RUN-ON:     cpu (Python 3, numpy); about a minute
COMMAND:    python3 tests/probes/lexicon/rule30_b3_sharp.py [S=12] [T=100] [PMAX=30]

Why. Cloud's CL169 tested lemma_B3 on 2.5 million white runs and never saw a run of length 2P; the largest was 2P - 1.
The proof explains it. In the newborn case, `back` already knows that diagonal M' - 1 or M' is black at the birth time
t - s0 - 1 (its `top` step). Forward from t - P the run is white on [g + 1 + 2(P - s0 - 1), M'] at that time. If
M' - g >= 2P, that range holds both M' - 1 and M', which contradicts `top`. So M' - g <= 2P - 2 s0 - 1 <= 2P - 1.
The entry-12 hand proof used only the black range [g - 2 s0 - 1, M' - 2], which gives 2P - 2 s0.

What this scan does. It takes every seed with leftmost black cell 0 and support inside cells 0 .. S - 1 (2^(S-1)
seeds), runs T steps, and reads the row in diagonals D_k(t) = cell e - t + k. For each t and 1 <= P <= min(t, PMAX),
M* is the largest M with D_k(t - P) = D_k(t) for all k <= M. For each white run [g + 1, M'] with D_g(t) black and
M' <= M* (the maximal such M' per g), it records the length M' - g against 2P - 1.

PREDICTIONS (Local's, written before the Lean run and before this scan; the time is in the ledger entry L538):
  B3S-C1 (control): no run exceeds 2P (lemma_B3, machine-checked 10-10), and diagonal 0 is black at every t.
  B3S-P1 (0.85): Lean accepts lemma_B3_sharp (M' - g <= 2P - 1) under lemma_B3's hypotheses, with no sorryAx, and
         theorem_A4_sharp (n <= L + a' - M + 2P - 1) follows with the same proof.
  B3S-P2 (0.97): this scan finds no run of length 2P (the sharp bound, checked independently of Lean).
  B3S-P3 (the unexpected check, 0.5): some P >= 2 attains 2P - 1 here, so the sharp bound is tight beyond P = 1.
         Cloud saw 2P - 1 only at P = 1. Attaining 2P - 1 needs s0 = 0: the run is newborn one step before t.
"""
import sys

import numpy as np

S = int(sys.argv[1]) if len(sys.argv) > 1 else 12
T = int(sys.argv[2]) if len(sys.argv) > 2 else 100
PMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 30


def diagonals(seed):
    """D[t, k] = cell e - t + k at time t, for k = 0 .. S + 2T - 1 (white beyond)."""
    K = S + 2 * T
    W = 3 * T + S + 4
    e = T + 2
    x = np.zeros(W, np.uint8)
    x[e:e + S] = seed
    D = np.zeros((T + 1, K), np.uint8)
    for t in range(T + 1):
        D[t] = x[e - t:e - t + K]
        y = np.zeros(W, np.uint8)
        y[1:-1] = x[:-2] ^ (x[1:-1] | x[2:])
        x = y
    return D


def main():
    K = S + 2 * T
    worst = {}                  # P -> largest run length M' - g seen
    hits = {}                   # P -> count of runs of length 2P - 1
    over2P = over = edge_bad = 0
    nruns = 0
    for bits in range(1 << (S - 1)):
        seed = [1] + [(bits >> i) & 1 for i in range(S - 1)]
        D = diagonals(seed)
        if not D[:, 0].all():
            edge_bad += 1
        for t in range(1, T + 1):
            row = D[t]
            for P in range(1, min(t, PMAX) + 1):
                neq = np.flatnonzero(D[t - P] != row)
                Ms = (neq[0] - 1) if len(neq) else K - 1
                if Ms < 1:
                    continue
                b = np.flatnonzero(row[:Ms + 1])
                lens = np.append(np.diff(b) - 1, Ms - b[-1])
                lens = lens[lens > 0]
                if not len(lens):
                    continue
                nruns += len(lens)
                m = int(lens.max())
                worst[P] = max(worst.get(P, 0), m)
                if m > 2 * P:
                    over2P += 1
                if m > 2 * P - 1:
                    over += 1
                hits[P] = hits.get(P, 0) + int((lens == 2 * P - 1).sum())
    print('S=%d T=%d PMAX=%d: %d seeds, %d white runs' % (S, T, PMAX, 1 << (S - 1), nruns))
    print('edge diagonal not black in %d seeds; runs over 2P: %d; runs of length 2P: %d' % (edge_bad, over2P,
                                                                                           over - over2P))
    for P in sorted(worst):
        print('  P=%2d  longest %2d  (2P-1 = %2d)  runs of length 2P-1: %d' % (P, worst[P], 2 * P - 1, hits[P]))
    print('B3S-C1', 'PASS' if over2P == 0 and edge_bad == 0 else 'FAIL')
    print('B3S-P2', 'HELD' if over == 0 else 'REFUTED')
    print('B3S-P3', 'HELD' if any(hits.get(P, 0) for P in worst if P >= 2) else 'REFUTED')


if __name__ == '__main__':
    main()
