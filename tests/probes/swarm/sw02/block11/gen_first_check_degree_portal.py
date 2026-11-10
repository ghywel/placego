#!/usr/bin/env python3
"""gen_first_check_degree_portal.py: write the portal form of S-06 from its kit form (L1629).

The kit form `Rule30FirstCheckDegree` imports `Rule30FirstChecks`, which is on kit main but not in the portal
verifier's kit (`5fb59158`). So the portal form imports `Rule30Prize` and `Rule30ZeroBoundary` only, and carries the
body of the kit's `Rule30FirstChecks` byte for byte in the nested namespace `Rule30Submission.Rule30FirstChecks`,
followed by the body of `Rule30FirstCheckDegree` byte for byte in `Rule30Submission`. The script asserts both copies,
and that the result has no double quote and no backslash.

Run: python3 -I tests/probes/swarm/sw02/block11/gen_first_check_degree_portal.py KIT_FORM KIT_FIRSTCHECKS PORTAL_FORM
"""
import hashlib
import sys

src, dep, dst = sys.argv[1], sys.argv[2], sys.argv[3]


def body(path, name, imports):
    s = open(path, encoding='utf-8').read()
    head = 'namespace Ruliology.CellularAutomata\nnamespace %s\n' % name
    tail = '\nend %s\nend Ruliology.CellularAutomata\n' % name
    assert s.startswith('module\n'), path
    assert s.endswith(tail), ('unexpected tail', path)
    i = s.index(head)
    doc = s[len('module\n'):i]
    for imp in imports:
        assert ('public import %s\n' % imp) in doc, (path, imp)
        doc = doc.replace('public import %s\n' % imp, '')
    doc = doc.replace('@[expose] public section\n', '')
    return doc.strip('\n'), s[i + len(head):-len(tail)]


doc, main = body(src, 'Rule30FirstCheckDegree', ['Ruliology.CellularAutomata.Rule30FirstChecks'])
_, first = body(dep, 'Rule30FirstChecks', ['Ruliology.CellularAutomata.Rule30ZeroBoundary'])
out = ('import Ruliology.CellularAutomata.Rule30Prize\nimport Ruliology.CellularAutomata.Rule30ZeroBoundary\n'
       + doc + '\n\n' + 'namespace Rule30Submission\n\nopen Ruliology.CellularAutomata\n\n'
       + '/-! ### A copy of the kit module `Rule30FirstChecks`, which the verifier kit does not have -/\n\n'
       + 'namespace Rule30FirstChecks\n' + first + '\nend Rule30FirstChecks\n'
       + main + '\nend Rule30Submission\n')
assert main in out and first in out
assert '"' not in out and '\\' not in out, 'portal form must have no double quote and no backslash'
open(dst, 'w', encoding='utf-8').write(out)
for label, text in (('first-checks body', first), ('module body', main), ('portal', out)):
    print(label, 'sha256', hashlib.sha256(text.encode('utf-8')).hexdigest())
print('portal lines', out.count('\n'))
