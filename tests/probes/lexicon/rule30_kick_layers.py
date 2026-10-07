#!/usr/bin/env python3
"""rule30_kick_layers.py: KL, what local structure alone says about the wheel's kicks (PERIOD-TWO.md row 6.1; Local's
draw-and-work block of 2026-10-07; claimed in CLOUD-LOCAL.md with these predictions pushed before the run below).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_kick_layers.py [MMAX=20]
COST:       minutes to MMAX = 18; about 10 minutes more for 19 and 20.

Setting (RULE30-PRIZE.md sections 8.5 to 8.8, 8.43). Column 0 is 0101... (column 0 at time t is t mod 2) and column
1 runs the wheel U of rule30_walls.py, U[(t - d) mod 56] at phase d. A kick is a departure of column 1 from U at time
t1, of class a = (t1 - d) mod 56, onto a new even phase d'. With the angle 17 (t - d)/56 of the coded rotation, the
kick is -17 (d' - d)/2 mod 28 notches, signed into -14 .. 13.

The instrument is the m-layer automaton of section 8.20 aimed at the kicks. Its state is the set of contents of the
hidden columns 2 .. m consistent with what column 1 has done; the input at column m + 1 is arbitrary at every step.
Every real right side is one such input sequence, so the automaton over-approximates: a departure class or a kick it
rules out is ruled out for every right side. Two preconditions on what came before the departure:
  settled: column 1 followed U long enough that the state sets are periodic (the fixed point, reached in a few turns);
  one turn: column 1 followed U for exactly 56 steps, from any start phase (the union over start phases).
After the departure the new phase must hold for F = 20 steps (the window rule30_kicks.py fits a new phase in).

The step is coded twice, independently: per cell from the rule x' = left XOR (centre OR right), and as one row update
((row << 1) XOR (row OR (row >> 1))) on columns 0 .. m + 1, as rule30_walls.spacetime does.

An exploratory look came before this script, inside the same reasoning block. It was not preregistered and its
numbers are not scored here. Settled, the departure classes shrank with m to {12, 32, 42, 52} by m = 16 and stayed so
to m = 22. At m = 16 with F = 20 the kick sets were exactly the measured alphabets for the two observed classes,
32: +2 .. +6 and 52: -6 .. -1, with 12: +4 .. +8 and 42: +1 .. +5 for the two classes never seen in data.

PREDICTIONS, Local's, published before this script's run (blind unless marked):
  KL-C0 (control): the two codings give identical settled state sets, departure classes and kick sets at every m
        from 4 to 16.
  KL-C1 (control, sound): every real departure after at least one clean turn of the wheel, with 20 exact steps on a
        new phase, from a sample of random right halves, lies in the one-turn automaton's (class, kick) set at m = 16.
        The sample must contain at least 50 such departures, or KL-C1 is void.
  KL-C2 (control, the exploratory look reproduced): settled at m = 16, classes {12, 32, 42, 52}, class 32 kicks
        {+2 .. +6}, class 52 kicks {-6 .. -1}.
  KL-P1 (blind): settled, for every m from 17 to MMAX the classes stay {12, 32, 42, 52} and the class 32 and 52 kick
        sets stay exactly the measured alphabets.
  KL-P2 (blind, uncertain): classes 12 and 42 are still allowed at m = MMAX.
  KL-P3 (blind): with the one-turn precondition at m = 16, the class set is larger than the settled one (it includes
        at least one class outside {12, 32, 42, 52}).
OUTCOME: not yet run.
"""
import os
import random
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))
sys.argv, _argv = sys.argv[:1], sys.argv
import rule30_walls as wl
sys.argv = _argv

U = [int(c) for c in wl.U]
P = len(U)
F = 20
MMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20


def step_cells(h, t, m, inp, c1):
    def col(i):
        if i == 0:
            return t % 2
        if i == 1:
            return c1
        return (h >> (i - 2)) & 1 if i <= m else inp
    nh = 0
    for i in range(2, m + 1):
        nh |= (col(i - 1) ^ (col(i) | col(i + 1))) << (i - 2)
    return nh, col(0) ^ (col(1) | col(2))


def step_row(h, t, m, inp, c1):
    row = (t % 2) | (c1 << 1) | (h << 2) | (inp << (m + 1))
    new = (row << 1) ^ (row | (row >> 1))
    return (new >> 2) & ((1 << (m - 1)) - 1), (new >> 1) & 1


def advance(S, t, m, c1, want, step, keep_equal=True):
    out = set()
    for h in S:
        for inp in (0, 1):
            nh, x1 = step(h, t, m, inp, c1)
            if (x1 == want) == keep_equal:
                out.add(nh)
    return out


def settled(m, step):
    S, prev = set(range(1 << (m - 1))), None
    while True:
        sets = []
        for t in range(P):
            sets.append(S)
            S = advance(S, t, m, U[t], U[(t + 1) % P], step)
        if prev is not None and [len(x) for x in sets] == [len(x) for x in prev]:
            return sets
        prev = sets


def kick_of(dn):
    k = (-17 * (dn // 2)) % 28
    return k if k < 14 else k - 28


def kicks_from(start_sets, m, step):
    """start_sets[t]: the state set at time t (phase 0) before a possible departure at t + 1."""
    out = {}
    for t in range(P):
        a = (t + 1) % P
        dep = advance(start_sets[t], t, m, U[t], U[a], step, keep_equal=False)
        if not dep:
            continue
        ks = []
        for dn in range(0, P, 2):
            if U[(a - dn) % P] != 1 - U[a]:
                continue
            S = dep
            for s in range(a, a + F):
                S = advance(S, s, m, U[(s - dn) % P], U[(s + 1 - dn) % P], step)
                if not S:
                    break
            if S:
                ks.append(kick_of(dn))
        out[a] = sorted(ks)
    return out


def one_turn_sets(m, step):
    """union over start phases: the state set at each time t after exactly P steps on the wheel"""
    sets = [set() for _ in range(P)]
    for j in range(P):
        S = set(range(1 << (m - 1)))
        for t in range(j, j + P):
            S = advance(S, t % P, m, U[t % P], U[(t + 1) % P], step)
        sets[(j + P) % P] |= S
    return sets


def main():
    t0 = time.time()
    c0 = True
    for m in range(4, 17):
        a, b = settled(m, step_cells), settled(m, step_row)
        c0 &= a == b and kicks_from(a, m, step_cells) == kicks_from(b, m, step_row)
    print('KL-C0', 'PASS' if c0 else 'FAIL', '(%.0f s)' % (time.time() - t0), flush=True)
    rows = {}
    for m in range(4, MMAX + 1):
        k = kicks_from(settled(m, step_row), m, step_row)
        rows[m] = k
        print('settled m %2d: %s' % (m, {a: v for a, v in sorted(k.items())}), flush=True)
    meas = {32: [2, 3, 4, 5, 6], 52: [-6, -5, -4, -3, -2, -1]}
    k16 = rows[16]
    c2 = sorted(k16) == [12, 32, 42, 52] and k16[32] == meas[32] and k16[52] == meas[52]
    print('KL-C2', 'PASS' if c2 else 'FAIL')
    one = kicks_from(one_turn_sets(16, step_row), 16, step_row)
    print('one-turn m 16: %s' % {a: v for a, v in sorted(one.items())}, flush=True)
    # KL-C1: real departures after at least one clean turn, then 20 exact steps on a new phase
    rng = random.Random(int.from_bytes(os.urandom(4), 'big'))
    n, bad = 0, []
    for trial in range(3000):
        R, T, row, c1 = rng.getrandbits(16) | 1, 3000, 0, []
        row = R << 1
        for t in range(T):
            c1.append((row >> 1) & 1)
            row = ((((row << 1) ^ (row | (row >> 1))) & ~1) | ((t + 1) % 2)) & ((1 << (T + 24)) - 1)
        t = 0
        while t + P + F < T:
            d = next((d for d in range(0, P, 2) if all(c1[t + j] == U[(t + j - d) % P] for j in range(P))), None)
            if d is None:
                t += 1
                continue
            s = t + P
            while s < T and c1[s] == U[(s - d) % P]:
                s += 1
            if s + F >= T:
                break
            a = (s - d) % P
            for dn in range(0, P, 2):
                if all(c1[s + j] == U[(s + j - dn) % P] for j in range(F + 1)):
                    n += 1
                    if kick_of((dn - d) % P) not in one.get(a, []):
                        bad.append((a, kick_of((dn - d) % P)))
            t = s
        if n >= 400:
            break
    print('real departures after a clean turn with %d steps on a new phase: %d; outside the one-turn set: %d %s'
          % (F, n, len(bad), bad[:5]))
    print('KL-C1', 'VOID' if n < 50 else ('PASS' if not bad else 'FAIL'))
    p1 = all(sorted(rows[m]) == [12, 32, 42, 52] and rows[m][32] == meas[32] and rows[m][52] == meas[52]
             for m in range(17, MMAX + 1))
    print('KL-P1', 'HELD' if p1 else 'REFUTED')
    print('KL-P2', 'HELD' if 12 in rows[MMAX] and 42 in rows[MMAX] else 'REFUTED')
    print('KL-P3', 'HELD' if set(one) - {12, 32, 42, 52} else 'REFUTED')
    print('time %.0f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
