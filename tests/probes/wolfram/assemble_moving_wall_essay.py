#!/usr/bin/env python3
"""assemble_moving_wall_essay.py (Local, L1429, NIGHT-TASKS A4): essay.md = essay-prose.md + the formal section, with the
checked portal form embedded verbatim as a multi-line string after (*Iconize["Lean source"]*), as the healing-bound
assembler did. Both inputs are pinned by digest. Run: python3 tests/probes/wolfram/assemble_moving_wall_essay.py FOLDER
"""
import hashlib, sys
from pathlib import Path
d = Path(sys.argv[1])
prose = (d / 'essay-prose.md').read_bytes(); src = (d / 'Rule30Submission.lean').read_bytes()
pins = {'essay-prose.md': ('7d765b2ab977d610dc96741d3b58dd1a8a22fab57c4b8f460bb73f8da2cb7877', prose),
        'Rule30Submission.lean': ('095e3800341d85e14990390c5b1871f9dcafb42dd62a154dd2f76b36b4a50e14', src)}
for name, (want, data) in pins.items():
    got = hashlib.sha256(data).hexdigest()
    if got != want:
        raise SystemExit('REFUSED: %s digest %s, pinned %s' % (name, got, want))
s = src.decode()
assert '"' not in s and '\\' not in s, 'the source must embed as a plain string literal'
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and `Rule30Jen` (for `rule`) at the verifier's
kit commit 93d98bbe. Each background has its own namespace with the same structure: the ring table, one sound tick, the
closure and potential as data checked by the kernel, the generic induction, the start at t = 300, and the laws.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"''' + s + '''", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headline theorems, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30Jen"};
heads = {"Ring57.edge_law", "Ring63.edge_law", "Ring57.edge_law_tail", "Ring63.edge_law_tail", "Ring57.step_sound", "Ring63.step_sound"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The invariant carried by the window, as defined in the module:

```wl
show[{"Ring57.Inv"}, "TermForm"]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it
resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.Ring57.edge_law"]["KernelCheck"]
```
'''
out = prose.decode().rstrip('\n') + formal
(d / 'essay.md').write_text(out)
print('essay.md written: %d bytes, sha256 %s' % (len(out.encode()), hashlib.sha256(out.encode()).hexdigest()))
