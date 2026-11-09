#!/usr/bin/env python3
"""local_word_sat.py (Local, 9 November 2026; S-16 construction, step 2): can a gap word occur at all inside the
kit's gate trap? An exact finite question, by SAT.

Usage: python3 local_word_sat.py KIT_DIR WORD [WORD ...]     (each WORD a string of gaps, e.g. 3555535555355553)

For a gap word g1 ... gk read from a black head at an odd time t0 (a sample), the head samples over the word's
D = g1 + ... + gk samples are fixed: black at the word's black cells, white between. Time tau = 0 .. 2D ticks after
t0; the boundary column 0 is black at even absolute times, so at local time tau it is black iff tau is odd. Cell j at
local time tau depends only on initial cells up to j + tau, so the initial cells 1 .. 2D + 1 decide every fixed head
sample. For each of the trap's 188 black windows (cells 1..16 at t0 fixed to it) one SAT instance: the rule
x[tau+1][j] = x[tau][j-1] xor (x[tau][j] or x[tau][j+1]) on the light-cone triangle, and the head samples as units.
The word occurs after entry in SOME right half, finite or infinite (any satisfying assignment extends to an infinite
row, and any trapped row is in a trap window at the word's first sample), exactly when some instance is SAT.

Controls: 3535353 (dead at width 18 in the relaxed graph, so UNSAT for every window); a common word must be SAT.

PREDICTION (written before this ran; clock read 22:05:43 UTC): the word with runs 4, 4, 4 (3555535555355553, the core
of every absent code word with BABAB) is UNSAT from every black trap window, so no right half ever shows it after
entry; then the code {5, 3555} is not realizable, and G1' fails at some finite width. Counterfactual: SAT from some
window, so the word is physically possible after entry and its absence in real rows is rarity (or needs a long past).
Result (started 22:06:08 UTC): controls HELD (3535353 UNSAT from all 188 windows; 3555355535553555 SAT from 25). The
(4, 4, 4) word is SAT from 19 of 188 windows: MISSED, possible after entry.
"""
import re
import sys
import time
from pathlib import Path

from pysat.solvers import Cadical153

KIT = Path(sys.argv[1])
WORDS = sys.argv[2:]
src = (KIT / 'lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read_text()
TRAP = [int(x) for x in re.findall(r'\d+', re.search(r'def trapCodes : List Nat := \[(.*?)\]', src, re.S).group(1))]
BLACK = sorted(w for w in TRAP if w & 1)
assert len(BLACK) == 188


def solve_word(word):
    gaps = [int(c) for c in word]
    heads = [1]
    for g in gaps:
        heads += [0] * (g - 1) + [1]
    D = len(heads) - 1
    T = 2 * D
    M = T + 1                       # initial cells 1..M decide cell 1 up to tau = T
    vid = {}

    def v(tau, j):
        key = (tau, j)
        if key not in vid:
            vid[key] = len(vid) + 1
        return vid[key]
    base = []
    for tau in range(T):
        for j in range(1, M - tau):          # cell j at tau + 1 needs j + 1 at tau
            z = v(tau + 1, j); b = v(tau, j); c = v(tau, j + 1)
            if j == 1:
                a_const = 1 if tau % 2 == 1 else 0
                for bb in (0, 1):
                    for cc in (0, 1):
                        zz = a_const ^ (bb | cc)
                        # forbid (b = bb, c = cc, z != zz)
                        base.append([(-b if bb else b), (-c if cc else c), (z if zz else -z)])
            else:
                a = v(tau, j - 1)
                for aa in (0, 1):
                    for bb in (0, 1):
                        for cc in (0, 1):
                            zz = aa ^ (bb | cc)
                            base.append([(-a if aa else a), (-b if bb else b), (-c if cc else c), (z if zz else -z)])
    units = [(v(2 * s, 1) if heads[s] else -v(2 * s, 1)) for s in range(D + 1)]
    sat_windows = []
    t0 = time.time()
    for w in BLACK:
        with Cadical153(bootstrap_with=base) as S:
            assum = units + [(v(0, j + 1) if (w >> j) & 1 else -v(0, j + 1)) for j in range(16)]
            if S.solve(assumptions=assum):
                sat_windows.append(w)
    return D, len(vid), len(base), sat_windows, time.time() - t0


for word in WORDS:
    D, nv, nc, sat, dt = solve_word(word)
    print(f'{word}: {D} samples, {nv} variables, {nc} clauses; SAT from {len(sat)} of 188 black trap windows'
          f'{" e.g. " + str(sat[:3]) if sat else ""}; {dt:.1f} s', flush=True)
