#!/usr/bin/env python3
"""L1040: exhaustive self-checks for the reset-track lemma and its gap-pair corollary.

Local, 2026-10-27. A reset row is a row (cells 1, 2, ... at an even time, wall x(t,0) = t mod 2) that begins 000, so
the next visible bit is 1. Finite truth-table checks of the clamped two-step map only: no solver, sampling or census.
Each block checks one statement of reports/rule30-reset-tracks.md; the hand proofs are in that report.
"""
import itertools


def step(x, wall):
    return [(wall if i == 0 else x[i - 1]) ^ (x[i] | x[i + 1]) for i in range(len(x) - 1)]


def two(x):
    return step(step(x, 0), 1)


def s(t):
    return ''.join(map(str, t))


def after_reset(tail, gaps=1):
    """Rows two updates apart after the reset row 000+tail, through `gaps` further resets; (gap list, row prefixes)."""
    x, out, z, seen = [0, 0, 0] + list(tail), [], 0, []
    while len(out) < gaps:
        assert len(x) >= 5, 'tail too short for the requested gaps'
        x = two(x)
        seen.append(s(x[:3]))
        if x[:3] == [0, 0, 0]:
            out.append(z)
            z = 0
        else:
            z += 1
    return out, seen, x


GAP = {1: {'0001', '0010', '0011'}, 2: {'1101', '1110', '1111'},
       3: {'0000', '0100', '0101', '0110', '0111'}, 4: {'1000', '1001', '1010', '1011', '1100'}}
TRACK = {1: ['100'], 2: ['111', '010'], 3: ['10', '001', '010'], 4: ['111', '011', '001', '010']}

# Track lemma: the next gap is N(t1..t4), and the rows before the next reset begin with the listed tracks
# (gap 3's first row is 100 or 101, i.e. begins 10). The row just before every reset begins 100 or 010.
for t in itertools.product((0, 1), repeat=14):
    (g,), seen, _ = after_reset(t)
    assert s(t[:4]) in GAP[g]
    assert all(row.startswith(p) for row, p in zip(seen, TRACK[g])) and seen[-1] == '000'
# Gap-pair corollary: right after a reset, a gap of 1 is never followed by 2, and a gap of 2 only by 2 or 4.
# The second gap is N of the next reset row's first four tail bits (track lemma), and those four bits depend only on
# the first 4 + 2(g+1) <= 14 tail bits of the first reset row (checked here with two further free bits).
pairs, depend = set(), {}
for t in itertools.product((0, 1), repeat=16):
    (g,), _, r2 = after_reset(t)
    g2 = next(k for k, v in GAP.items() if s(r2[3:7]) in v)
    pairs.add((g, g2))
    depend.setdefault((g, t[:4 + 2 * (g + 1)]), set()).add(g2)
assert all(len(v) == 1 for v in depend.values())
assert pairs == set(itertools.product((1, 2, 3, 4), repeat=2)) - {(1, 2), (2, 1), (2, 3)}
print('track lemma and gap-pair corollary pass')
