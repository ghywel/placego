#!/usr/bin/env python3
"""gen_free_middle_portal.py: write the portal form of S-13 from its kit form (L1620).

The kit form is a `module` with `public import`s inside `namespace Ruliology.CellularAutomata` /
`Rule30FreeMiddle`. The portal form is the same declarations in `namespace Rule30Submission`, with plain
imports (adding the statement module `Rule30Prize`, which the kit's Check.lean requires) and
`open Ruliology.CellularAutomata`. Nothing else changes; the script asserts that the body is copied byte for byte.

Run: python3 -I tests/probes/swarm/sw02/block11/gen_free_middle_portal.py KIT_FORM PORTAL_FORM
"""
import hashlib
import sys

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
head = ('module\n\npublic import Ruliology.CellularAutomata.Rule30ZeroBoundaryBarriers\n'
        'public import Ruliology.CellularAutomata.Rule30LocalConservation\n\n@[expose] public section\n\n'
        'namespace Ruliology.CellularAutomata\nnamespace Rule30FreeMiddle\n')
tail = '\nend Rule30FreeMiddle\nend Ruliology.CellularAutomata\n'
i = s.index('namespace Ruliology.CellularAutomata\nnamespace Rule30FreeMiddle\n')
doc = s[s.index('module\n') + len('module\n'):i]
doc = doc.replace('public import Ruliology.CellularAutomata.Rule30ZeroBoundaryBarriers\n', '')
doc = doc.replace('public import Ruliology.CellularAutomata.Rule30LocalConservation\n', '')
doc = doc.replace('@[expose] public section\n', '')
assert s.endswith(tail), 'unexpected tail'
body = s[i + len('namespace Ruliology.CellularAutomata\nnamespace Rule30FreeMiddle\n'):-len(tail)]
out = ('import Ruliology.CellularAutomata.Rule30Prize\nimport Ruliology.CellularAutomata.Rule30ZeroBoundaryBarriers\n'
       'import Ruliology.CellularAutomata.Rule30LocalConservation\n' + doc.strip('\n') + '\n\n'
       'namespace Rule30Submission\n\nopen Ruliology.CellularAutomata\n' + body + '\nend Rule30Submission\n')
assert body in out
for bad in ('"', '\\'):
    assert bad not in out, 'portal source must not contain %r' % bad
open(dst, 'w', encoding='utf-8').write(out)
print('body sha256', hashlib.sha256(body.encode()).hexdigest())
print('portal sha256', hashlib.sha256(out.encode()).hexdigest(), len(out.splitlines()), 'lines')
