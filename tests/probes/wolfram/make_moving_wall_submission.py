#!/usr/bin/env python3
"""L1429 (Local, 2026-11-03): the portal form of NIGHT-TASKS A4 from the kit module built by a4_kit_module.py.
Run: python3 tests/probes/wolfram/make_moving_wall_submission.py KITDIR
Writes reports/wolfram-agents/submissions/moving-wall/Rule30Submission.lean: the same declarations and proofs (namespaces
Ring57 and Ring63) in namespace Rule30Submission, with plain imports of the kit's statement module and Rule30Jen.
"""
import hashlib
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parents[3]
K = pathlib.Path(sys.argv[1])
src = (K / 'lean/Ruliology/CellularAutomata/Rule30MovingWall.lean').read_text()
assert src.startswith('module\npublic import Ruliology.CellularAutomata.Rule30Prize\npublic import Ruliology.CellularAutomata.Rule30Jen\n')
s = src.replace('module\npublic import Ruliology.CellularAutomata.Rule30Prize\npublic import Ruliology.CellularAutomata.Rule30Jen\n',
                'import Ruliology.CellularAutomata.Rule30Prize\nimport Ruliology.CellularAutomata.Rule30Jen\n', 1)
s = s.replace('@[expose] public section\n\n', '', 1)
s = s.replace('namespace Ruliology.CellularAutomata.Rule30MovingWall\n\nopen Rule30Jen\n',
              'namespace Rule30Submission\n\nopen Ruliology.CellularAutomata Rule30Jen\n', 1)
s = s.replace('end Ruliology.CellularAutomata.Rule30MovingWall\n', 'end Rule30Submission\n', 1)
assert 'Rule30MovingWall' not in s.split('-/', 1)[1]
dst = root / 'reports/wolfram-agents/submissions/moving-wall/Rule30Submission.lean'
dst.write_text(s)
print('wrote %s: %d lines, SHA256 %s' % (dst.name, s.count('\n'), hashlib.sha256(s.encode()).hexdigest()))
