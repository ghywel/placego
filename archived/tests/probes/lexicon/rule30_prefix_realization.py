#!/usr/bin/env python3
"""GC1168: fitted left champions force a forbidden visible11 before tick20.

RUN-ON: cpu; standard library. No CUT, solver, membership or horizon census.
COMMAND: python3 tests/probes/lexicon/rule30_prefix_realization.py
Record searched: P20|champion|fitted|10011100101110100100 with
visible|real|cut|11|right ->66 hits36files;8.83's no11, G25, GC1166/67 read.

BEFORE THE EXPLORATORY FIXTURE LOOKUP (2026-10-13, retained separately):
 Predict both fitted width31 champions force visible11 by physical33.
 CF: farther cells repair the prefix; cone predicts no change through33
 if the low34 cells are fixed. Compare literal and packed evolution.
 Unexpected control: use both wall phases, separating a failed black
 condition from a required visible word after that failure.

EXPLORATORY OUTCOME: phase1 fitted words force visible11 at indices8,9
(physical17,19), with no black-condition failure through33. Their old
core-only visible11 at indices5,6 is repaired and replaced by this one.
Phase0 fails its black condition before its first printed11, so that
later word is not an actual-clock obligation in that phase.

BEFORE THE CERTIFICATE CONTROLS BELOW (indices already seen, replay):
 R1: low20 cells fix the required first10 phase1 visible bits; at indices
     8,9 both are1, for all16 assignments to four farther cells.
 R2: independent inverse-column reconstruction recovers the entire
     low20 prefix from those10 formal bits.
 R3: all8 right triples forbid consecutive visible ones two ticks apart.
 CF: ignore the right update; the clamped left passes every black check
     through18 while producing11, distinguishing the two games.
 Unexpected guard: in phase0, do not use a derived visible value after
     the first failed black check as an actual centre-clock obligation.

FIRST CERTIFICATE RUN: the inverse control failed because it placed the
phase1 white samples at even times (2*i+1-phase). Corrected to2*i+phase;
the forward comparisons and the no11 truth-table check were unchanged.
OUTCOME after repair: R1..R3 and CF held. Each of the two low20 prefixes
fixes its10 visible bits under all16 far-cell controls; literal and packed
updates agree, inversion recovers low20, and every right triple forbids11.
The phase0 guard holds for both cores. Arbitrary farther tails follow by
the cone, not by extrapolating16 cases. The universal centre deadline is
tick20, even though the clamped-left champions have h=66 (Local's result).
"""
from itertools import product
from rule30_prefix_arrival import P20, CORES, seed


def rule(l, c, r):
    return (30 >> (4*l+2*c+r)) & 1


def literal(a, phase, ticks):
    rows = [dict(a)]
    w = max(a, default=0)
    for t in range(ticks):
        x = rows[-1]
        rows.append({j: rule(x.get(j+1, 0), x.get(j, 0),
                            (phase+t) % 2 if j == 1 else x.get(j-1, 0))
                     for j in range(1, w+t+2)})
    return rows


def packed(a, phase, ticks):
    r = sum(b << (j-1) for j, b in a.items())
    mask = (1 << (max(a, default=0)+ticks+2))-1
    out = []
    for t in range(ticks+1):
        out.append(r & 1)
        r = ((r >> 1) ^ (r | ((r << 1) | ((phase+t) % 2)))) & mask
    return out


def inverse(visible, phase):
    """Literal truth-table left inversion, independent of packed updates."""
    n = 2*len(visible)
    right = [(phase+t) % 2 for t in range(n+1)]
    far = [0]*(n+1)
    for i, v in enumerate(visible):
        far[2*i+phase] = v
    initial = []
    for _ in range(n):
        col = []
        for t in range(len(right)-1):
            choices = [l for l in (0, 1) if rule(l, right[t], far[t]) == right[t+1]]
            assert len(choices) == 1
            col.append(choices[0])
        initial.append(col[0])
        far, right = right, col
    return initial


def main():
    for a1, a2, a3 in product((0, 1), repeat=3):
        y1, y2 = rule(0, a1, a2), rule(a1, a2, a3)
        v2 = rule(1, y1, y2)
        assert not (a1 == v2 == 1)
    print('R3 no11: all8 right triples PASS')

    for core in CORES:
        full = seed(P20+core)
        low = {j: full.get(j, 0) for j in range(1, 21)}
        words = set()
        for far in product((0, 1), repeat=4):
            a = dict(low)
            a.update({21+i: b for i, b in enumerate(far)})
            rows, pi = literal(a, 1, 19), packed(a, 1, 19)
            assert pi == [x.get(1, 0) for x in rows]
            assert all(pi[t] == 1 for t in range(0, 20, 2))
            vis = [1 ^ pi[t] for t in range(1, 20, 2)]
            assert vis[8:] == [1, 1]
            assert inverse(vis, 1) == [low[j] for j in range(1, 21)]
            words.add(''.join(map(str, vis)))
        assert len(words) == 1
        word = words.pop()
        print('low20', ''.join(str(low[j]) for j in range(20, 0, -1)),
              'visible', word, 'first11', word.find('11'),
              '16 far tails / literal-packed / inverse PASS')
        ph0 = packed(full, 0, 19)
        fail = next(t for t in range(1, 20, 2) if ph0[t] == 0)
        vis0 = ''.join(str(1 ^ ph0[t]) for t in range(0, 20, 2))
        cut0 = vis0.find('11')
        assert cut0 >= 0 and fail < 2*cut0
        print('phase0 scope guard: black failure', fail,
              'precedes printed11 at', 2*cut0, 'PASS')
    print('ALL CHECKS PASS; actual centre cannot match through tick20')


if __name__ == '__main__':
    main()
