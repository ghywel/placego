#!/usr/bin/env python3
"""L1426 (Local, 2026-11-03): combine A4's two kernel-checked modules (tests/probes/lean/MovingWall.lean, MovingWall63.lean) into
the kit-form module lean/Ruliology/CellularAutomata/Rule30MovingWall.lean, with namespaces Ring57 and Ring63.
Run: python3 tests/probes/wolfram/a4_kit_module.py KITDIR
Declarations and proofs are unchanged; only the module header, docstring and namespaces are added.
"""
import hashlib
import pathlib
import sys

W = pathlib.Path(__file__).resolve().parents[3]
K = pathlib.Path(sys.argv[1])


def body(path, sub):
    s = (W / path).read_text()
    s = s.split('namespace Ruliology.CellularAutomata.', 1)[1].split('\n', 1)[1]
    s = s.rsplit('end Ruliology.CellularAutomata.', 1)[0]
    s = s.replace('open Rule30Jen\n', '', 1)
    return 'namespace ' + sub + '\n' + s.rstrip() + '\n\nend ' + sub + '\n'


doc = '''module
public import Ruliology.CellularAutomata.Rule30Prize
public import Ruliology.CellularAutomata.Rule30Jen

/-!
# Moving walls: exact front speeds of an inserted edge on two ring backgrounds

Take a spatially periodic background orbit of rule 30 (a ring word `w`, evolved on the whole line) and insert one black
cell, with white to its right. On the ring backgrounds `100100000` and `1010000`, at the alignments `(0, 0)` and `(0, 4)`,
the leftmost difference from the background moves left at an exact rational speed, for all time and whatever the damage
behind it does. (The ring orbits have periods 57 and 63 in the diagonal coordinate `t - x`; at a fixed column the
backgrounds repeat every 171 and 63 ticks.)

* `Ring57.edge_law`: for every `t ≥ 300` there is an anchor `A` with the background intact at and left of `A`, a
  difference within the 24 cells right of `A`, and `-14 ≤ 19 (A + 72) + 5 (t - 300) ≤ 22`: speed exactly `5/19`.
* `Ring63.edge_law`: the same with 16 cells and `-20 ≤ 9 (A + 55) + 2 (t - 300) ≤ 4`: speed exactly `2/9`.
* `Ring57.edge_law_tail`, `Ring63.edge_law_tail`: the same laws for every rule-30 evolution whose initial row agrees with
  the inserted edge's at `x ≤ 252` (respectively `x ≤ 261`), whatever its cells beyond (`agree_cone`, `law_from`).

The proof is a closed set of anchored window states with a moving anchor (the anchor moves left one column exactly when its
own cell becomes a difference), checked by the kernel on bit masks (`closure_ok`), with an exact potential on its edges:
the weight `P * motion + (P - S)` changes the potential by itself on every edge, so `P (A - A0) + (P - S) (t - t0)` is a
function of the current state. `step_sound` shows that one tick of the window is sound on every rule-30 evolution of the
whole line, whatever the cell beyond the window; `anchored` carries the invariant through any checked closure, and
`entry_inv` puts the inserted edge into the closure at `t = 300` by a bit-mask simulation. Because the closure contains
every successor under both values of the cell beyond the window, the law holds for every front whose state enters the
closure, whatever lies behind it. It does not say that every front on these backgrounds enters it.

The method, a finite front state with a potential certified on local patterns, is that of `Rule30EtherThreeErosion`
(there an inequality for the period-three ether); here the potential is an exact identity and the anchor moves.
`Rule30Ether`'s `trap_invariant` is the stationary case. Growth from finite perturbations of periodic backgrounds was
studied by Phillips (Wolfram Science Conference 2004). Nothing here concerns the centre column.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30MovingWall

open Rule30Jen

'''
out = doc + body('tests/probes/lean/MovingWall.lean', 'Ring57') + '\n' + body('tests/probes/lean/MovingWall63.lean', 'Ring63') + \
    '\nend Ruliology.CellularAutomata.Rule30MovingWall\n'
dst = K / 'lean/Ruliology/CellularAutomata/Rule30MovingWall.lean'
dst.write_text(out)
print('wrote %s: %d lines, SHA256 %s' % (dst.name, out.count('\n'), hashlib.sha256(out.encode()).hexdigest()))
