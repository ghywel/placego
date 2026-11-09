#!/usr/bin/env python3
"""local_code_control.py (Local, 9 November 2026; S-16 construction, step 3): is the next code block controllable from
the far right? A greedy test of the mechanism a construction would need.

Usage: python3 local_code_control.py KIT_DIR TRIALS BLOCKS SEED

Criterion. By compactness (GC2796 (1) <=> (2)), the free code {A = 5, B = 3555} lies in every width's eventual language
exactly when every FINITE code word is read, from its first black head, by some right half whose window is in the
kit's trap at that head. A greedy construction would follow if this held: once a code prefix of duration D samples is
realized, freezing every initial cell its heads depend on (cells 1 .. 2D + 1), both A and B can still follow, using
only cells further right. Then every infinite code is built block by block, and compactness is not even needed.

Test. One incremental SAT formula (CaDiCaL) for the longest horizon: the rule on the light-cone triangle from an odd
sample time, the alternating boundary, the start window among the trap's 188 black windows as a 16-cell assumption.
Each trial: pick a start window and a first block that is SAT; then for each further step, with cells 1 .. 2D + 1
frozen to the last witness, ask whether A and whether B can follow; choose one of the possible blocks at random;
stop at a dead end (neither possible).

PREDICTION (written before this ran; clock read 22:09:08 UTC): no dead end in any trial, and both blocks possible at
every step: the next gap is controlled by cells beyond the prefix's cone. Counterfactual: steps where only one block
(or neither) is possible with the prefix frozen; then a construction needs lookahead, and control is not local.
First run (FRAC 1.0, seed 3, started 22:09:56 UTC): MISSED completely. Both blocks possible at 0 of 37 steps; one block
only at 35, dead ends at 2. The frozen light-cone prefix already decides the next block.
SECOND PREDICTION, for a frozen fraction FRAC of the light cone (cells 17 .. FRAC * (2D + 1)), written before that
run (clock read 22:10 UTC, see the launch line): both blocks are often possible at FRAC <= 0.2 and almost never at
FRAC >= 0.4, the change sitting near Rule 30's left damage speed (about 0.24 cell per tick, so the deciding cells
lie near 0.24 times the elapsed time). Counterfactual: no free choice even at FRAC = 0.1, or free choice persisting at
FRAC = 0.6, either of which would put the control scale away from the damage speed.
Second run (started 22:10:56 UTC): both blocks possible at 70%, 64%, 55%, 30%, 4.5% of 44 steps for FRAC 0.1, 0.2,
0.3, 0.4, 0.6; no dead end below FRAC 1. Often free at <= 0.2 HELD; almost never at 0.4 MISSED (30%); the change is
gradual, centred near 0.3 to 0.4, not sharp. Forced-A steps (B impossible from that window) persist even at FRAC 0.1.
"""
import random
import re
import sys
import time
from pathlib import Path

from pysat.solvers import Cadical153

KIT, TRIALS, BLOCKS, SEED = Path(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
FRACS = [float(x) for x in sys.argv[5:]] or [1.0]
src = (KIT / 'lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read_text()
TRAP = [int(x) for x in re.findall(r'\d+', re.search(r'def trapCodes : List Nat := \[(.*?)\]', src, re.S).group(1))]
BLACK = sorted(w for w in TRAP if w & 1)
CODE = {'A': [5], 'B': [3, 5, 5, 5]}
Dmax = 18 * BLOCKS
T = 2 * Dmax
M = T + 1
vid = {}


def v(tau, j):
    if (tau, j) not in vid:
        vid[(tau, j)] = len(vid) + 1
    return vid[(tau, j)]


cl = []
for tau in range(T):
    for j in range(1, M - tau):
        z = v(tau + 1, j); b = v(tau, j); c = v(tau, j + 1)
        if j == 1:
            a0 = 1 if tau % 2 == 1 else 0
            for bb in (0, 1):
                for cc in (0, 1):
                    zz = a0 ^ (bb | cc)
                    cl.append([(-b if bb else b), (-c if cc else c), (z if zz else -z)])
        else:
            a = v(tau, j - 1)
            for aa in (0, 1):
                for bb in (0, 1):
                    for cc in (0, 1):
                        zz = aa ^ (bb | cc)
                        cl.append([(-a if aa else a), (-b if bb else b), (-c if cc else c), (z if zz else -z)])
print(f'formula: {len(vid)} variables, {len(cl)} clauses, horizon {T} ticks', flush=True)
S = Cadical153(bootstrap_with=cl)


def heads_of(blocks):
    h = [1]
    for x in blocks:
        for g in CODE[x]:
            h += [0] * (g - 1) + [1]
    return h


def assume(blocks, window, frozen):
    h = heads_of(blocks)
    a = [(v(2 * s, 1) if h[s] else -v(2 * s, 1)) for s in range(len(h))]
    a += [(v(0, j + 1) if (window >> j) & 1 else -v(0, j + 1)) for j in range(16)]
    a += frozen
    return a, len(h) - 1


t0 = time.time()
for FRAC in FRACS:
  rng = random.Random(SEED)
  stats = {'steps': 0, 'both': 0, 'onlyA': 0, 'onlyB': 0, 'dead': 0}
  for trial in range(TRIALS):
      order = BLACK[:]; rng.shuffle(order)
      blocks, window, frozen = None, None, []
      for w in order:
          x = rng.choice('AB')
          a, D = assume([x], w, [])
          if S.solve(assumptions=a):
              blocks, window = [x], w
              model = S.get_model(); break
      if blocks is None:
          print(f'trial {trial}: no start'); continue
      path = []
      while len(blocks) < BLOCKS:
          D = len(heads_of(blocks)) - 1
          mset = set(model)
          frozen = [(v(0, j) if v(0, j) in mset else -v(0, j)) for j in range(17, min(int(FRAC * (2 * D + 1)), M) + 1)]
          ok = {}
          models = {}
          for x in 'AB':
              a, _ = assume(blocks + [x], window, frozen)
              ok[x] = S.solve(assumptions=a)
              if ok[x]:
                  models[x] = S.get_model()
          stats['steps'] += 1
          if ok['A'] and ok['B']:
              stats['both'] += 1; path.append('*')
          elif ok['A']:
              stats['onlyA'] += 1; path.append('a')
          elif ok['B']:
              stats['onlyB'] += 1; path.append('b')
          else:
              stats['dead'] += 1; path.append('X'); break
          choices = [x for x in 'AB' if ok[x]]
          x = rng.choice(choices)
          blocks.append(x); model = models[x]
      print(f'trial {trial}: window {window}, blocks {"".join(blocks)}, steps {"".join(path)} '
            f'(* both possible, a/b only one, X dead end); {time.time() - t0:.0f} s', flush=True)
  print(f'FRAC {FRAC}: totals', stats, flush=True)
