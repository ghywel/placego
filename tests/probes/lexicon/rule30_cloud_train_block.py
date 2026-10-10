#!/usr/bin/env python3
"""rule30_cloud_train_block.py: TG, the 2-gap train. Is the visible word 1010.. (column 1 of period 4 in time beside
the 0101 wall) actual at every length, and does a finite right half sustain it? (row Q6, serving CUT's cuts.)

RUN-ON:     cpu (Python 3; mode member needs kissat and rule30_relaxed_records_k.py's scratch, NP_SCRATCH_RLK)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_train_block.py member [NMAX=200]
            python3 tests/probes/lexicon/rule30_cloud_train_block.py seeds [SITES=12] [CAP=400]
            python3 tests/probes/lexicon/rule30_cloud_train_block.py block [STEPS=20000] [WMAX=24]
COST:       member: seconds a call to n = 200. seeds: about 10 s. block: about a minute at WMAX = 24, more at 60.

Why. CUT's cuts at Cloud's depths, length 53 at d = 140 (L590) and length 81 at d = 152 (L591), are built around long
2-gap trains (gaps 2,2,2,.. between visible ones), as L557 read the K = 18 words. If the pure train had a maximal
length m, (10)^(m+1) would be a minimal forbidden word, a provable family and the home of relax40's slack at those
depths. If the train is actual at every length, the cuts forbid how a train is entered and left, not its length.
Visible index k is wall time 2k + phase; 1 at k and k + 2 means x(1) = 1, 0, 1 at those white times.

Record searched: `record_find.py "2-gap"` -> L557's reading only (via KIMI-ONBOARDING §2); `"ring" "period 4"`,
`alternat`, `"finite right half"`, `shield` -> nothing on this train (G112's white shield is the left half).

PREDICTIONS. TG-P1 (registered in CL185, pushed 13:33 BST before the run; 0.65): (10)^n is in L and in L1 for every
n to 40. Counterfactual: a maximal train length. TG-P2 (informed, not blind: formed after the first SAT witness's cone
showed the four-cell right half 1001 followed by zeros; written here after its run; 0.5): the FINITE right half 1001
beside the phase-0 clock keeps column 1 on the train for 3000 readings. Counterfactual: a finite failure time, so
long trains need an infinite tailored right half. TG-P3 (informed, 0.5): the observed windows (t mod 4, sites 1..W)
close under one step with a free site W + 1 for some W <= 40, a finite certificate that the block lasts for ever.
Counterfactual: no closure, the state count outrunning the sample.

OUTCOME (2026-10-10 13:45 BST). TG-P1 HELD, to n = 200 in both phases (Local, L592, to n = 100 independently).
TG-P2 HELD: 3000 of 3000 readings; the same seed in phase 1 fails at the first reading; of the 4095 seeds on sites
1..12 (phase 0), 28 reach the 400-reading cap and every one of them begins 1001; the longest failing seed reaches 32.
Block: sites 1..6 follow a period-4 cycle for 20,000 steps from t = 2 while site 7 is still broken at the end of the
run (chaos sits against the block), so column 1 reads 1100 repeating. TG-P3 REFUTED: no closure to W = 60 (an ad hoc
run; the distinct windows grow to the sample size), and at W = 6 the single unclosed transition is x(7) = 1 at t = 0
mod 4, never observed. The chain of what the train needs of the right half runs one site further back each step:
x(2) = 0 at t = 2, 3 mod 4; x(7) = 0 at t = 0; x(7) or x(8) at t = 3; .. The eternity of the train, and of the block,
is OPEN: measured to 20,000 steps, not proved. Unexpected check: the block holds although site 7 is chaotic throughout.
"""
import os, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def step(row, wall):
    """One Rule 30 step of the right half (site i is bit i - 1) with the wall value at site 0."""
    return ((row << 1) | wall) ^ (row | (row >> 1))


def train_length(seed, phase, cap):
    """Readings of column 1 at the wall's white times that follow 1010.. before the first break, at most cap."""
    row, k = seed, 0
    for t in range(2 * cap):
        wall = (t + phase) % 2
        if wall == 0:
            if (row & 1) != (1 - k % 2):
                return k
            k += 1
        row = step(row, wall)
    return k


def member(nmax):
    import rule30_relaxed_records_k as rk
    for ph in (0, 1):
        assert not rk.in_language_phase('11', ph) and rk.in_language_phase('0101', ph), 'controls'
    for n in (5, 10, 20, 40, 100, nmax):
        w = '10' * n
        verdicts = ['L%d %s' % (ph, 'IN' if rk.in_language_phase(w, ph) else 'ABSENT') for ph in (0, 1)]
        print('(10)^%-3d len %3d: %s' % (n, len(w), '  '.join(verdicts)), flush=True)


def seeds(sites, cap):
    print('seed 1001, phase 0: train length %d of %d; phase 1: %d'
          % (train_length(0b1001, 0, cap), cap, train_length(0b1001, 1, cap)))
    full, best = [], 0
    for s in range(1, 1 << sites):
        n = train_length(s, 0, cap)
        if n >= cap:
            full.append(format(s, 'b')[::-1])
        else:
            best = max(best, n)
    print('%d of %d seeds on sites 1..%d reach the cap; longest failing seed %d; all capped seeds begin 1001: %s'
          % (len(full), (1 << sites) - 1, sites, best, all(f.startswith('1001') for f in full)))


def block(steps, wmax):
    rows, row = [], 0b1001
    for t in range(steps + 1):
        rows.append(row)
        row = step(row, t % 2)
    bit = lambda r, i: (r >> (i - 1)) & 1
    last = {i: max([t for t in range(steps - 3) if bit(rows[t], i) != bit(rows[t + 4], i)] or [-1])
            for i in range(1, 13)}
    print('last period-4 violation by site:', ' '.join('%d:%d' % kv for kv in last.items()))
    print('cycle of sites 1..6 by t mod 4 (from t = 4):', [format(rows[4 + p] & 63, '06b')[::-1] for p in range(4)])
    mask = lambda W: (1 << W) - 1
    for W in range(6, wmax + 1):
        seen = {p: set() for p in range(4)}
        for t in range(2, steps + 1):
            seen[t % 4].add(rows[t] & mask(W))
        bad = sum(1 for p in range(4) for w in seen[p] for b in (0, 1)
                  if step(w | (b << W), p % 2) & mask(W) not in seen[(p + 1) % 4])
        print('W=%2d windows per phase %s unclosed %d%s'
              % (W, [len(seen[p]) for p in range(4)], bad, '  CLOSED' if bad == 0 else ''))
        if bad == 0:
            break


if __name__ == '__main__':
    cmd, a = sys.argv[1], [int(x) for x in sys.argv[2:]]
    t0 = time.time()
    {'member': lambda: member(*(a or [200])), 'seeds': lambda: seeds(*(a or [12, 400])),
     'block': lambda: block(*(a or [20000, 24]))}[cmd]()
    print('(%.0f s)' % (time.time() - t0))
