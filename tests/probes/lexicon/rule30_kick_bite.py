#!/usr/bin/env python3
"""rule30_kick_bite.py: KB, why the wheel never kicks at classes 12 and 42 (PERIOD-TWO.md row 6.1; the owner's
"bite" steer of 2026-10-07; Cloud's block, claimed in CLOUD-LOCAL.md with these predictions pushed before the run).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_kick_bite.py [TRIALS=400] [T=3000]
COST:       minutes.

Setting. Local's KL (rule30_kick_layers.py, PROOFS.md entry 26) proves, for every right side, that after 133 steps
on the wheel U a departure of column 1 can occur only at classes 12, 32, 42 and 52, with kicks +4..+8, +2..+6, +1..+5
and -6..-1. Real slips (11,437 in section 8.43, 408 in KL-C1) were only ever seen at 32 and 52. KL's automaton lets
the input at column m + 1 be anything at every step, so it over-approximates in one specific way: it never uses
that a real right half is finite. This script asks whether that is where the bite is. It runs the wall form (column
0 = t mod 2, any right half) on four families of right halves and tallies every departure after a long settled
stretch on the wheel:
  F1  finite random right halves, widths 16, 32, 64 and 128;
  F2  infinite random right halves (a random row wider than the light cone, T + 2 cells, so no right edge is ever
      seen by column 1 within T steps);
  F3  infinite spatially periodic right halves, a random word of period 1 to 12 repeated past the light cone;
  F4  infinite random right halves of density 1/8 and 7/8 (sparse and dense backgrounds).
A departure is counted as in KL-C1: column 1 follows U at an even phase d for at least S steps, leaves it at time s,
and then follows U at an even phase d' for 21 observations; its class is (s - d) mod 56 and its kick is KL's
kick_of(d' - d). S = 168 (three turns), past KL's 133-step settling.

Controls:
  KB-C0 (the detector can see the bite): a synthetic column 1 that runs U at phase 0 for 300 steps and then jumps
        to a phase chosen to make a class-12 kick of +6 is reported as exactly that, and likewise class 42, +3.
  KB-C1 (KL's theorem as a guard): every settled departure in every family lies inside KL's settled table. A
        departure outside it would mean a bug here, or an error in entry 26.
  KB-C2 (replication): F1 at width 16 shows classes 32 and 52 only, as KL-C1 and section 8.43 did.

PREDICTIONS (Cloud's, written and pushed before the first run):
  KB-P1: F1 at every width shows no class 12 or 42 departure. Confidence 0.9.
  KB-P2: F2 shows no class 12 or 42 departure either. Confidence 0.7. Near column 1, a finite right half looks like
         an infinite random one until the right edge's influence arrives, so if F1 never shows them, F2 probably
         does not.
  KB-P3: some F3 background (a periodic right half) does show a class 12 or 42 departure. Confidence 0.4.
  KB-P4: F4 shows class 12 or 42 at one of the two densities. Confidence 0.3.
Counterfactual: if F2, F3 or F4 show classes 12 or 42 while F1 never does, the absence comes from the right half's
finiteness or genericity, and that is the bite: a non-local constraint of the kind Q2 asks for. If no family shows
them, the absence is a deeper law (or very rare), and the next step is an exact search for a finite right half that
makes one.
"""
import os
import random
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(__file__))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_walls as wl                                    # noqa: E402
sys.argv = _argv

U = [int(c) for c in wl.U]
P, F, S = 56, 20, 168
TRIALS = int(sys.argv[1]) if len(sys.argv) > 1 else 400
T = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
KL = {12: range(4, 9), 32: range(2, 7), 42: range(1, 6), 52: range(-6, 0)}


def kick_of(dn):                                             # as in rule30_kick_layers.py
    k = (-17 * (dn // 2)) % 28
    return k if k < 14 else k - 28


def column1(R, width):
    """Column 1 for T steps of the wall form, right half R (bit i = column i + 1), the row cut at width cells."""
    mask = (1 << (width + T + 4)) - 1
    row, c1 = R << 1, []
    for t in range(T):
        c1.append((row >> 1) & 1)
        row = ((((row << 1) ^ (row | (row >> 1))) & ~1) | ((t + 1) % 2)) & mask
    return c1


def departures(c1, need=S):
    out = []
    t, n = 0, len(c1)
    while t + P + F < n:
        d = next((d for d in range(0, P, 2) if all(c1[t + j] == U[(t + j - d) % P] for j in range(P))), None)
        if d is None:
            t += 1
            continue
        s = t + P
        while s < n and c1[s] == U[(s - d) % P]:
            s += 1
        if s + F >= n:
            break
        if s - t >= need:
            a = (s - d) % P
            for dn in range(0, P, 2):
                if all(c1[s + j] == U[(s + j - dn) % P] for j in range(F + 1)):
                    out.append((a, kick_of((dn - d) % P)))
        t = s
    return out


def synthetic(cls, kick):
    """U at phase 0 for 300 steps, then the even phase that gives (class, kick) at the departure."""
    s = next(s for s in range(300, 300 + P) if s % P == cls)
    dn = next(dn for dn in range(0, P, 2) if kick_of(dn) == kick and U[(s - dn) % P] != U[s % P])
    return [U[t % P] for t in range(s)] + [U[(t - dn) % P] for t in range(s, s + 200)]


def main():
    c0 = all(departures(synthetic(c, k)) == [(c, k)] for c, k in ((12, 6), (42, 3), (32, 4), (52, -3)))
    print('KB-C0', 'PASS' if c0 else 'FAIL', flush=True)
    rng = random.Random(int.from_bytes(os.urandom(4), 'big'))
    fams = {}
    for w in (16, 32, 64, 128):
        fams['F1 finite w%d' % w] = lambda w=w: (rng.getrandbits(w) | 1, w)
    fams['F2 infinite random'] = lambda: (rng.getrandbits(T + 2), T + 2)

    def periodic():
        p = rng.randint(1, 12)
        word = rng.getrandbits(p) or 1
        R = 0
        for i in range(0, T + 2, p):
            R |= word << i
        return R & ((1 << (T + 2)) - 1), T + 2
    fams['F3 periodic'] = periodic

    def dense(q):
        R = 0
        for i in range(T + 2):
            if rng.random() < q:
                R |= 1 << i
        return R, T + 2
    fams['F4 density 1/8'] = lambda: dense(1 / 8)
    fams['F4 density 7/8'] = lambda: dense(7 / 8)
    guard, bite = True, {}
    for name, make in fams.items():
        tally = Counter()
        for _ in range(TRIALS):
            R, w = make()
            for a, k in departures(column1(R, w)):
                tally[(a, k)] += 1
                guard &= a in KL and k in KL[a]
        classes = Counter()
        for (a, k), v in tally.items():
            classes[a] += v
        bite[name] = classes[12] + classes[42]
        print('%-20s departures %6d  by class %s' % (name, sum(tally.values()), dict(sorted(classes.items()))),
              flush=True)
        for a in sorted(classes):
            print('    class %2d kicks %s' % (a, dict(sorted((k, v) for (b, k), v in tally.items() if b == a))))
    print('KB-C1', 'PASS' if guard else 'FAIL (a departure outside KL\'s settled table)')
    print('KB-C2', 'PASS' if bite['F1 finite w16'] == 0 else 'FAIL')
    f1 = sum(v for n, v in bite.items() if n.startswith('F1'))
    f4 = bite['F4 density 1/8'] + bite['F4 density 7/8']
    print('KB-P1', 'HELD' if f1 == 0 else 'REFUTED', '(%d)' % f1)
    print('KB-P2', 'HELD' if bite['F2 infinite random'] == 0 else 'REFUTED', '(%d)' % bite['F2 infinite random'])
    print('KB-P3', 'HELD' if bite['F3 periodic'] > 0 else 'REFUTED', '(%d)' % bite['F3 periodic'])
    print('KB-P4', 'HELD' if f4 > 0 else 'REFUTED', '(%d)' % f4)


if __name__ == '__main__':
    main()
