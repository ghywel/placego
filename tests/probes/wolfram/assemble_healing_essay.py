#!/usr/bin/env python3
"""assemble_healing_essay.py (Local, L1355, NIGHT-TASKS A2): essay.md = essay-prose.md + the formal section, with the
checked portal form embedded verbatim as a multi-line string after (*Iconize["Lean source"]*), as the ether-episode
assembler did. Both inputs are pinned by digest. Run: python3 tests/probes/wolfram/assemble_healing_essay.py FOLDER
"""
import hashlib, sys
from pathlib import Path
d = Path(sys.argv[1])
prose = (d / 'essay-prose.md').read_bytes(); src = (d / 'Rule30Submission.lean').read_bytes()
pins = {'essay-prose.md': ('0b0c723cc9ed1bc05190cbd530448c7f8f015fd0966ca85d856f34ca1e7e18a2', prose), 'Rule30Submission.lean': ('f444ae698fa0de3fff978a5c41ea09aaebc91c80ce3da4ec668a6780c8d325b8', src)}
for name, (want, data) in pins.items():
    got = hashlib.sha256(data).hexdigest()
    if got != want:
        raise SystemExit('REFUSED: %s digest %s, pinned %s' % (name, got, want))
s = src.decode()
assert '"' not in s and '\\' not in s, 'the source must embed as a plain string literal'
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and `Rule30Jen` (for `rule`) at the
verifier's kit commit 93d98bbe. The proof is one induction on time with two cases, plus `omega`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"''' + s + '''", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The three headlines, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30Jen"};
heads = {"healing_bound", "front_ge", "K_succ_bounds"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The frontier and the whole-line rule, as defined in the module:

```wl
show[{"K", "IsR30Z"}, "TermForm"]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it
resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.healing_bound"]["KernelCheck"]
```
'''
out = prose.decode().rstrip('\n') + formal
(d / 'essay.md').write_text(out)
print('essay.md written: %d bytes, sha256 %s' % (len(out.encode()), hashlib.sha256(out.encode()).hexdigest()))
