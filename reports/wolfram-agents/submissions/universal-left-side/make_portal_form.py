#!/usr/bin/env python3
"""make_portal_form.py KIT_MODULE OUT: the portal form of Rule30UniversalLeftSide.lean (L1506): plain imports and the
namespace Rule30Submission. The module imports only what the verifier's kit (c42f6e51) has, so nothing else changes."""
import sys
kit = open(sys.argv[1]).read()
END = 'end Ruliology.CellularAutomata.Rule30UniversalLeftSide\n'
for old, new in [
    ('module\n\npublic import Ruliology.CellularAutomata.Rule30Prize\npublic import Ruliology.CellularAutomata.Rule30AgedLeftDiagonals\n',
     'import Ruliology.CellularAutomata.Rule30Prize\nimport Ruliology.CellularAutomata.Rule30AgedLeftDiagonals\n'),
    ('@[expose] public section\n\nnamespace Ruliology.CellularAutomata.Rule30UniversalLeftSide\n',
     'namespace Rule30Submission\n\nopen Ruliology.CellularAutomata\n'),
    (END, 'end Rule30Submission\n'),
]:
    assert old in kit, old[:40]
    kit = kit.replace(old, new)
open(sys.argv[2], 'w').write(kit)
