#!/usr/bin/env python3
"""make_ether_zero_submission.py (Local, L1346, NIGHT-TASKS A1): the portal form of tests/probes/lean/EtherEdgeZero.lean.
Run: python3 tests/probes/wolfram/make_ether_zero_submission.py CATALOG OUT

Mechanical: plain imports of Rule30Prize (the official statements) and Rule30Ether; namespace Rule30Submission with
`open Ruliology.CellularAutomata`; no `module`, `public import` or `@[expose] public section`; the module docstring
in public wording. Every other line of the catalog file is kept byte for byte, and the script refuses otherwise.
"""
import sys
src = open(sys.argv[1]).read().split('\n')
head_end = next(i for i, l in enumerate(src) if l.startswith('namespace Ruliology.CellularAutomata.EtherEdgeZero'))
body = src[head_end + 1:]
assert body[0] == 'open Rule30Jen Rule30StripCertificates Rule30Ether', body[0]
end = body.index('end Ruliology.CellularAutomata.EtherEdgeZero')
code = body[1:end]
for l in code:
    for bad in ('L13', 'CL6', 'GC2', 'NIGHT', 'placego', 'Lowry', 'PR65'):
        assert bad not in l, ('internal reference left', l)
doc = '''/-!
# Rule 30: the classic ether absorbs a black edge, so the edge's front speed is exactly zero

Insert one black cell, with white to its right, into the ether of `Rule30Ether` (spatial period 7, temporal period 4)
at any of its 28 alignments `(c0, c1)`, and evolve by rule 30 on the whole line (`G`). Then from a finite time on, the
ether is undisturbed at and left of a fixed column `xB`, and the disturbance never heals within the 13 cells to its
right (`edge_pinned`). The leftmost cell where `G` differs from the ether therefore stays in a fixed window for ever:
its speed is exactly zero, at every alignment.

* `trap_two_sided`: the ether-wall trap of `Rule30Ether` (`trap_invariant`) on the whole line. The prescribed column is
  replaced by the induction hypothesis on the columns left of the B3 column.
* `G_left`: the light cone (columns `x < -t` are still the ether).
* `iter3_G`: a finite list simulation (`lin3` of `Rule30StripCertificates`) agrees with `G` on its range.
* `entry_c0_c1`: for each alignment, the kernel checks that by a stated time `t1 ≤ 222` the columns `-t1 .. xB` are the
  ether, `xB` is a B3 column, and the next 13 cells form one of the 109 wall states (`checkEntry`, by `decide`).
* `wall_ne_ref_all`: no wall state equals the ether's own 13 cells after a B3 (by `decide`), so the disturbance never
  heals.
* `edge_pinned_tail`: the same for every rule-30 evolution whose initial row agrees with the inserted edge's on
  `x ≤ 198`, whatever its right tail (radius-one locality, `agree_cone`, and the trap's closure under every right input).

Prior art: the ether, its 109 wall states and `trap_invariant` are the kit's `Rule30Ether`, used there to exclude ether
walls beside a periodic center column; kit pull request 65 later added `Lock` and `Rule30EtherWallWitness`. This module
proves the trap on the whole line and shows that an inserted edge enters it at every alignment. Scope: the lab frame of the ether; nothing here concerns the center column of the single-cell pattern.
-/'''
out = ['import Ruliology.CellularAutomata.Rule30Prize', 'import Ruliology.CellularAutomata.Rule30Ether', '', doc, '',
       'namespace Rule30Submission', 'open Ruliology.CellularAutomata', 'open Rule30Jen Rule30StripCertificates Rule30Ether'] \
      + code + ['end Rule30Submission', '']
open(sys.argv[2], 'w').write('\n'.join(out))
print('portal form written: %d lines (%d code lines kept byte for byte)' % (len(out), len(code)))
