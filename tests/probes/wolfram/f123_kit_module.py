#!/usr/bin/env python3
"""L1474 (Local, 2026-11-03): the F1-F3 anchor (CL697, CL701) in kit form. From the kernel-checked probe
tests/probes/lean/LeftCoincidence.lean, write lean/Ruliology/CellularAutomata/Rule30LeftCoincidence.lean (module system,
public imports including the statement module Rule30Prize, @[expose] public section) and, with --portal,
reports/wolfram-agents/submissions/left-coincidence/Rule30Submission.lean (namespace Rule30Submission, plain imports).
Run: python3 tests/probes/wolfram/f123_kit_module.py KITDIR [--portal]
Declarations and proofs are unchanged; only the header, the section and the namespace change, and the #print lines are dropped.
"""
import hashlib
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parents[3]
K = pathlib.Path(sys.argv[1]); portal = '--portal' in sys.argv
src = (root / 'tests/probes/lean/LeftCoincidence.lean').read_text()
head = 'import Ruliology.CellularAutomata.Rule30LeftReset\n'
assert src.startswith(head)
body = src[len(head):].split('\n#print axioms', 1)[0].rstrip() + '\n'
ns = 'namespace Ruliology.CellularAutomata.Rule30LeftCoincidence\n'
assert body.count(ns) == 1
kit = ('module\npublic import Ruliology.CellularAutomata.Rule30Prize\npublic import Ruliology.CellularAutomata.Rule30LeftReset\n'
       + body.replace(ns, '@[expose] public section\n\n' + ns, 1))
dst = K / 'lean/Ruliology/CellularAutomata/Rule30LeftCoincidence.lean'
dst.write_text(kit)
print('wrote %s: %d lines, SHA256 %s' % (dst.name, kit.count('\n'), hashlib.sha256(kit.encode()).hexdigest()))
if portal:
    p = 'import Ruliology.CellularAutomata.Rule30Prize\nimport Ruliology.CellularAutomata.Rule30LeftReset\n' + body
    p = p.replace(ns, 'namespace Rule30Submission\n\nopen Ruliology.CellularAutomata\n', 1)
    p = p.replace('end Ruliology.CellularAutomata.Rule30LeftCoincidence\n', 'end Rule30Submission\n', 1)
    out = root / 'reports/wolfram-agents/submissions/left-coincidence/Rule30Submission.lean'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(p)
    print('wrote %s: %d lines, SHA256 %s' % (out.name, p.count('\n'), hashlib.sha256(p.encode()).hexdigest()))
