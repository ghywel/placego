#!/usr/bin/env python3
"""Local's carrying read of Cloud's CL681 corollary (2026-11-02): an independent replay of the finite part.
Run: python3 tests/probes/ether_trap_replay.py KIT_RULE30ETHER_LEAN [T] [AFTER]

Cloud's ether_trap_check.py compares the evolved row with a lab ether built from the frame ring and matched to the kit's ether
on ticks 0..7 only, and finds the leftmost mismatch inside columns -40..59 only. This replay uses neither: the reference is the
kit's own ether(x + c0, t + c1) (a rule-30 orbit by the kit's ether_rule), every column inside the left light cone of the row's
boundary is compared, and the configurations are enumerated by kit alignment (c0, c1) (the inserted-edge row at t = 0 is
ether(x + c0, c1) for x < 0, black at 0, white beyond, so the 196 frame alignments fall into at most 28 cases).
The 109 wall states are parsed from the Lean list by a different route (ast.literal_eval of the list text).

Predictions (written before the first run, Local, 2026-11-02):
  R1 wallOK replays true: every state has length 13 and phase < 4, the head condition holds, closure under both right inputs.
  R2 all 28 kit alignments occur among Cloud's 196 and every one enters the trap (ether up to a B3 at x_B, then a wall state at
     the phase) by t = 222; the entry times lie in Cloud's range 4 .. 222.
  R3 with the full-row comparison, at entry no column <= x_B mismatches the kit's ether, and the leftmost mismatch never lies
     left of -40 before entry (so Cloud's window was wide enough).
  R4 after entry, AFTER more exact ticks: no column <= x_B ever mismatches, and the 13 cells right of x_B stay in the wall set
     at the right phase (the two-sided induction, observed).
  R5 positive control of the two-sided statement: ether up to a B3, a random wall state, then random cells to the right;
     AFTER exact ticks; no column <= x_B ever mismatches.
Counterfactual: if Cloud's frame-built ether drifts from the kit's after tick 7, or a mismatch hides left of -40, R2/R3 fail with
a different entry time or a mismatch left of x_B; if my reading of the two-sided step were wrong (orientation, or the B3's
right neighbour mattering when B3 is black), R4/R5 would show a mismatch at or left of x_B.
Record searched: python3 tests/probes/record_find.py "ether-wall trap" trap_invariant wallStates -> CL681, PROOFS.md waiting room,
PRIOR-ART Lowry row, kit Rule30Ether.lean (trap_invariant, wall_facts, wallOK_true) at kit main c42f6e5.
"""
import ast
import random
import sys

import numpy as np

src = open(sys.argv[1]).read()
T = int(sys.argv[2]) if len(sys.argv) > 2 else 400
AFTER = int(sys.argv[3]) if len(sys.argv) > 3 else 2000


def lean_list(name, stop):
    body = src[src.index('def ' + name):]
    body = body[body.index(':=') + 2:body.index(stop)]
    return ast.literal_eval(body.replace('true', '1').replace('false', '0').strip())


etherTable = lean_list('etherTable', '/-- Ether column')
wall = {(phi, tuple(s)) for phi, s in lean_list('wallStates', '/-- Closure under')}
print('parsed: etherTable %s; %d wall states' % (etherTable, len(wall)))


def ether(j, phi):
    return etherTable[j % 7][phi % 4]


def rule(a, b, c):
    return a ^ (b | c)


def lin3(cells):
    return tuple(rule(cells[i - 1], cells[i], cells[i + 1]) for i in range(1, len(cells) - 1))


ok = all(len(s) == 13 and phi < 4 for phi, s in wall)
ok &= all(ether(2, phi) == 1 or s[0] == ether(3, phi) for phi, s in wall)
ok &= all(((phi + 1) % 4, lin3((ether(2, phi),) + s + (x,))) in wall for phi, s in wall for x in (0, 1))
assert all(ether(j, p + 1) == rule(ether(j - 1, p), ether(j, p), ether(j + 1, p)) for j in range(7) for p in range(4))
print('R1 wallOK replayed: %s' % ok)


def step(row):
    """One rule-30 tick of a finite row with white beyond its right end; the left end cell is wrong (handled by the age)."""
    n = np.empty_like(row)
    n[0] = 0
    n[1:-1] = row[:-2] ^ (row[1:-1] | row[2:])
    n[-1] = row[-2] ^ row[-1]
    return n


ETH = np.array(etherTable, dtype=np.uint8)


def ref(lo, n, c0, tt):
    return ETH[(np.arange(lo, lo + n) + c0) % 7, tt % 4]


def leftmost(row, lo, c0, tt, age):
    """Leftmost mismatch against ether(x + c0, tt) over the columns the left end cannot yet have reached (age ticks)."""
    d = np.flatnonzero(row[age + 1:] != ref(lo, len(row), c0, tt)[age + 1:])
    return int(d[0]) + age + 1 + lo if len(d) else None


def trap_ok(row, lo, xB, phase):
    i = xB - lo
    return (phase % 4, tuple(int(v) for v in row[i + 1:i + 14])) in wall


# R2, R3: the inserted edge at every kit alignment
WL = 2 * (T + AFTER) + 50; WR = T + AFTER + 50; lo = -WL
entries = {}
for c0 in range(7):
    for c1 in range(4):
        row = np.array([ether(x + c0, c1) if x < 0 else (1 if x == 0 else 0) for x in range(lo, WR)], dtype=np.uint8)
        found = None; worst_left = 0
        for t in range(T + 1):
            xmin = leftmost(row, lo, c0, t + c1, t)
            if xmin is not None:
                worst_left = min(worst_left, xmin)
                for xB in range(xmin - 1, xmin - 8, -1):
                    if (xB + c0) % 7 == 2 and trap_ok(row, lo, xB, t + c1):
                        found = (t, xB, xmin); break
            if found:
                break
            row = step(row)
        entries[(c0, c1)] = (found, worst_left, row)
ent = [v[0] for v in entries.values() if v[0]]
print('R2 kit alignments %d; entered by T=%d: %d; entry times min %d, max %d' % (
    len(entries), T, len(ent), min(e[0] for e in ent), max(e[0] for e in ent)))
print('   (c0, c1): (entry tick, x_B, x_min) %s' % sorted((k, v[0]) for k, v in entries.items()))
print('R3 leftmost mismatch over all ticks up to entry, all alignments: %d (Cloud\'s window starts at -40)' % min(
    v[1] for v in entries.values()))

# R4: after entry
bad4 = 0; trapfail = 0; minx = []
for (c0, c1), (found, _, row) in entries.items():
    if not found:
        continue
    t1, xB, _ = found
    m = None
    for k in range(AFTER + 1):
        xmin = leftmost(row, lo, c0, t1 + k + c1, t1 + k)
        if xmin is not None and xmin <= xB:
            bad4 += 1
        if not trap_ok(row, lo, xB, t1 + k + c1):
            trapfail += 1
        m = xmin if m is None or (xmin is not None and xmin < m) else m
        row = step(row)
    minx.append(m - xB)
print('R4 after entry, %d ticks each: ticks with a mismatch at or left of x_B %d; ticks outside the wall set %d; '
      'least (x_min - x_B) %d' % (AFTER, bad4, trapfail, min(minx)))

# R5: positive control with random right halves beside a wall state
rng = random.Random(681); bad5 = 0; NR = 60
walls = sorted(wall)
for it in range(NR):
    phi, s = walls[rng.randrange(len(walls))]
    c1 = phi; c0 = rng.randrange(7); xB = (2 - c0) % 7 - 7   # a B3 column left of 0
    lo5 = xB - (2 * AFTER + 50)
    row = np.array([ether(x + c0, c1) if x <= xB else (s[x - xB - 1] if x <= xB + 13 else rng.getrandbits(1))
                    for x in range(lo5, xB + AFTER + 60)], dtype=np.uint8)
    for k in range(AFTER + 1):
        xmin = leftmost(row, lo5, c0, k + c1, k)
        if (xmin is not None and xmin <= xB) or not trap_ok(row, lo5, xB, k + c1):
            bad5 += 1
        row = step(row)
print('R5 %d random right halves beside a wall state, %d ticks each: bad ticks %d' % (NR, AFTER, bad5))
print('REPLAY_DONE')
