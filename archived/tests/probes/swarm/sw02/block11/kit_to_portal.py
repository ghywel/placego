#!/usr/bin/env python3
"""kit_to_portal.py: write the portal form of a kit-form module (L1623; generalises gen_free_middle_portal.py).

The kit form is a `module` with `public import`s, `@[expose] public section`, and its declarations inside
`namespace Ruliology.CellularAutomata` / `namespace NAME`. The portal form has the same declarations in
`namespace Rule30Submission`, plain imports (with the statement module `Rule30Prize` first, which the kit's Check.lean
requires) and `open Ruliology.CellularAutomata`. The body is copied byte for byte, which the script asserts.

Run: python3 -I tests/probes/swarm/sw02/block11/kit_to_portal.py NAME KIT_FORM PORTAL_FORM
"""
import hashlib
import re
import sys

name, src, dst = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(src, encoding='utf-8').read()
assert s.startswith('module\n'), 'not a kit module'
ns = 'namespace Ruliology.CellularAutomata\nnamespace %s\n' % name
tail = '\nend %s\nend Ruliology.CellularAutomata\n' % name
assert s.count(ns) == 1 and s.endswith(tail), 'unexpected namespaces'
i = s.index(ns)
pre = s[len('module\n'):i]
imports = re.findall(r'^public import (\S+)$', pre, re.M)
doc = re.sub(r'^public import \S+\n', '', pre, flags=re.M).replace('@[expose] public section\n', '')
body = s[i + len(ns):-len(tail)]
lines = ['import Ruliology.CellularAutomata.Rule30Prize'] + ['import ' + m for m in imports if m != 'Ruliology.CellularAutomata.Rule30Prize']
out = '\n'.join(lines) + '\n' + doc.strip('\n') + '\n\nnamespace Rule30Submission\n\nopen Ruliology.CellularAutomata\n' + body + '\nend Rule30Submission\n'
assert body in out
for bad in ('"', '\\'):
    assert bad not in out, 'portal source must not contain %r' % bad
open(dst, 'w', encoding='utf-8').write(out)
print('imports', imports)
print('body sha256', hashlib.sha256(body.encode()).hexdigest())
print('portal sha256', hashlib.sha256(out.encode()).hexdigest(), len(out.splitlines()), 'lines')
