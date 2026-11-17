#!/usr/bin/env python3
"""L1352 (Local, 2026-11-03; NIGHT-TASKS A2's rate gate): an independent replay of the healing frontier's rates.
Run: python3 tests/probes/healing_rate_replay.py

For each background (the ring words of Cloud's healing_bound.py: G8 1000, classic ether 1000000, 1010000, 100100000,
100100000000), the lab row at time 0 is built from the frame orbit, evolved by Local's own lab rule 30
(new = left xor (centre or right)) and checked to be a lab orbit, periodic with spatial period N and a lab period P found
here. The frontier of HealingBound.lean (L1349) is then walked in lab coordinates: the last known cell x_K(t) stays if the
background cell (x_K, t) is black and moves one left if it is white, starting at x_K(0) = -1, with key (x mod N, t mod P).
The leftward rate over the cycle bounds any perturbation's leftward damage speed (front_ge). All phases (frame shift r,
time shift s) are replayed. The classic ether is also replayed from the kit's own ether table (7 x 4), as a control.

Predictions (written before the first run): the rates equal Cloud's corrected healing_bound.out exactly: G8 1/2, classic
7/12, 1010000 2/9, 100100000 1/2, 100100000000 7/17, with one value per background (independent of phase); and the
kit-table replay of the classic ether gives 7/12 at all 28 alignments.
"""
from fractions import Fraction

WORDS = {'G8': '1000', 'classic ether': '1000000', '1010000 (7, 63)': '1010000', '100100000 (9, 57)': '100100000',
         '100100000000 (12, 68)': '100100000000'}


def frame_orbit(word):
    y = [int(c) for c in word]; N = len(y); orb = [y]
    while True:
        z = orb[-1]; z = [z[i] ^ (z[i - 1] | z[i - 2]) for i in range(N)]
        if z == y:
            return orb
        orb.append(z)


def lab_step(row):
    N = len(row)
    return [row[(i - 1) % N] ^ (row[i] | row[(i + 1) % N]) for i in range(N)]


def frontier_rate(E, N, P):
    """Leftward rate of the frontier on a lab background E(x, t), periodic (N in x, P in t), from x_K(0) = -1."""
    x, t = -1, 0; seen = {}
    while (x % N, t % P) not in seen:
        seen[(x % N, t % P)] = (x, t)
        if E(x, t) == 0:
            x -= 1
        t += 1
    x0, t0 = seen[(x % N, t % P)]
    return Fraction(-(x - x0), t - t0)


for name, word in WORDS.items():
    orb = frame_orbit(word); q = len(orb); N = len(word)
    rates = set(); lab_periods = set(); ok = True
    for r in range(N):
        for s in range(q):
            row0 = [orb[s % q][((0 - x) + r) % N] for x in range(N)]       # lab row at t = 0, one spatial period
            rows = [row0]
            while True:
                nxt = lab_step(rows[-1])
                if nxt == row0:
                    break
                rows.append(nxt)
                if len(rows) > 4 * q * N:
                    ok = False; break
            P = len(rows); lab_periods.add(P)
            # the frame formula must agree with Local's lab evolution at every cell of one period
            ok &= all(rows[t][x] == orb[(t + s) % q][((t - x) + r) % N] for t in range(P) for x in range(N))
            rates.add(frontier_rate(lambda x, t: rows[t % P][x % N], N, P))
    print('%-22s spatial %2d, lab period %s; lab orbit agrees with the frame formula: %s; frontier rates over all %d phases: %s' % (
        name, N, sorted(lab_periods), ok, N * q, sorted(str(v) for v in rates)))

# control: the classic ether from the kit's own table (Rule30Ether.etherTable), all 28 alignments
T = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
kit = set(frontier_rate(lambda x, t, c0=c0, c1=c1: T[(x + c0) % 7][(t + c1) % 4], 7, 4) for c0 in range(7) for c1 in range(4))
print('kit etherTable, 28 alignments: frontier rates %s' % sorted(str(v) for v in kit))
print('HEALING_RATE_REPLAY_DONE')
