#!/usr/bin/env python3
"""L1464 (Local, 2026-11-03): NIGHT-TASKS A5 in kit form. From the kernel-checked probe module
tests/probes/lean/EpisodeBridge.lean, write lean/Ruliology/CellularAutomata/Rule30EpisodeBridge.lean (module system: public
imports, the official statement module Rule30Prize imported, @[expose] public section) and, with --portal, the portal form
reports/wolfram-agents/submissions/episode-bridge/Rule30Submission.lean (namespace Rule30Submission, plain imports).
Run: python3 tests/probes/wolfram/a5_kit_module.py KITDIR [--portal]
Declarations and proofs are unchanged; only the header, the section and the namespace change, and the #print lines are dropped.
"""
import hashlib
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parents[3]
K = pathlib.Path(sys.argv[1]); portal = '--portal' in sys.argv
src = (root / 'tests/probes/lean/EpisodeBridge.lean').read_text()
imports = ['Rule30FrozenRuler', 'Rule30GateClocks', 'Rule30EtherEpisode', 'Rule30EdgeStaircases']
head = ''.join('import Ruliology.CellularAutomata.%s\n' % m for m in imports)
assert src.startswith(head)
body = src[len(head):]
body = body.split('\n#print axioms', 1)[0].rstrip() + '\n'
body = body.replace('(NIGHT-TASKS A5, L1431)', '')
body = body.replace('# Episodes and eternal tails behind a black right edge ', '# Episodes and eternal tails behind a black right edge')
assert body.count('namespace Ruliology.CellularAutomata.Rule30EpisodeBridge\n') == 1
kit = ('module\n' + ''.join('public import Ruliology.CellularAutomata.%s\n' % m for m in ['Rule30Prize'] + imports) + body)
kit = kit.replace('namespace Ruliology.CellularAutomata.Rule30EpisodeBridge\n',
                  '@[expose] public section\n\nnamespace Ruliology.CellularAutomata.Rule30EpisodeBridge\n', 1)
dst = K / 'lean/Ruliology/CellularAutomata/Rule30EpisodeBridge.lean'
dst.write_text(kit)
print('wrote %s: %d lines, SHA256 %s' % (dst.name, kit.count('\n'), hashlib.sha256(kit.encode()).hexdigest()))
if portal:
    p = ''.join('import Ruliology.CellularAutomata.%s\n' % m for m in ['Rule30Prize'] + imports) + body
    p = p.replace('namespace Ruliology.CellularAutomata.Rule30EpisodeBridge\n', 'namespace Rule30Submission\n\nopen Ruliology.CellularAutomata\n', 1)
    p = p.replace('end Ruliology.CellularAutomata.Rule30EpisodeBridge\n', 'end Rule30Submission\n', 1)
    out = root / 'reports/wolfram-agents/submissions/episode-bridge/Rule30Submission.lean'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(p)
    print('wrote %s: %d lines, SHA256 %s' % (out.name, p.count('\n'), hashlib.sha256(p.encode()).hexdigest()))
