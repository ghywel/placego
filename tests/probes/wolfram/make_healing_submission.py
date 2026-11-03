#!/usr/bin/env python3
"""make_healing_submission.py (Local, L1350, NIGHT-TASKS A2): the portal form of tests/probes/lean/HealingBound.lean.
Run: python3 tests/probes/wolfram/make_healing_submission.py CATALOG OUT

Mechanical: plain imports of Rule30Prize (the official statements) and Rule30Jen; namespace Rule30Submission with
`open Ruliology.CellularAutomata`; no `module`, `public import` or `@[expose] public section`; the module docstring
in public wording. Every other line of the catalog file is kept byte for byte, and the script refuses otherwise.
"""
import sys
src = open(sys.argv[1]).read().split('\n')
head_end = next(i for i, l in enumerate(src) if l.startswith('namespace Ruliology.CellularAutomata.HealingBound'))
body = src[head_end + 1:]
assert body[0] == 'open Rule30Jen', body[0]
end = body.index('end Ruliology.CellularAutomata.HealingBound')
code = body[1:end]
for l in code:
    for bad in ('L13', 'CL6', 'GC2', 'NIGHT', 'placego'):
        assert bad not in l, ('internal reference left', l)
doc = '''/-!
# Rule 30: the universal healing bound

For any rule-30 evolution `E` of the whole line (a background orbit, periodic or not) and any rule-30 evolution `G` that
agrees with `E` at time 0 on the columns `x ≤ -1`, define the **recruitment frontier** `K t` on diagonals `x + t`:
`K 0 = -1`, and `K (t + 1) = K t + 1` if the background cell `E t (K t - t)` is black, else `K t`.

* `healing_bound`: `G` agrees with `E` at every cell on a diagonal `x + t ≤ K t`. A black centre masks its right
  neighbour, so a diagonal whose newest known cell is black is recruited at the next tick.
* `front_ge`: the leftmost disagreement at time `t` lies at `x ≥ K t - t + 1`. Where the frontier's climb rate has a
  long-run mean (for a periodic background, the cycle mean of a finite walk on its torus), damage moves left at most at
  one minus that mean.
* `K_succ_bounds`: the frontier never falls and climbs at most one diagonal per tick.

Scope: any background orbit and any perturbation confined to `x ≥ 0` at time 0. Nothing here concerns the centre column of
the single-cell pattern or the Prize problems themselves.
-/'''
out = ['import Ruliology.CellularAutomata.Rule30Prize', 'import Ruliology.CellularAutomata.Rule30Jen', '', doc, '',
       'namespace Rule30Submission', 'open Ruliology.CellularAutomata', 'open Rule30Jen'] \
      + code + ['end Rule30Submission', '']
open(sys.argv[2], 'w').write('\n'.join(out))
print('portal form written: %d lines (%d code lines kept byte for byte)' % (len(out), len(code)))
