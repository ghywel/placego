#!/usr/bin/env python3
"""assemble_ether_zero87_essay.py (Local, L1390; from assemble_ether_zero_essay.py, L1354): essay.md = essay-prose.md + the formal section, with the
checked portal form embedded verbatim as a multi-line string after (*Iconize["Lean source"]*), as the ether-episode
assembler did. Both inputs are pinned by digest. Run: python3 tests/probes/wolfram/assemble_ether_zero_essay.py FOLDER
"""
import hashlib, sys
from pathlib import Path
d = Path(sys.argv[1])
prose = (d / 'essay-prose.md').read_bytes(); src = (d / 'Rule30Submission.lean').read_bytes()
pins = {'essay-prose.md': ('07602b5583ca6cfb2e36efa0d0aa076a7666f779e38b5ec71ce0ad27f9a6e2a2', prose), 'Rule30Submission.lean': ('d583be068ba7e92ea8ad5a542f7af1db37306e1e1ea13ec704948e0ade2c9da4', src)}
for name, (want, data) in pins.items():
    got = hashlib.sha256(data).hexdigest()
    if got != want:
        raise SystemExit('REFUSED: %s digest %s, pinned %s' % (name, got, want))
s = src.decode()
assert '"' not in s and '\\' not in s, 'the source must embed as a plain string literal'
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30Ether` at the
verifier's kit commit 93d98bbe. The 28 entries and the rooted observer's 28 runs are proved by `decide +kernel`, and
the never-heals table by `decide`; the kernel evaluates them. The rest is induction, rewriting and `omega`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"''' + s + '''", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The six headlines, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30Ether"};
heads = {"edge_pinned", "edge_pinned_tail", "edge_pinned_tail87", "trap_two_sided", "wall_ne_ref_all", "check_sound"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The inserted edge's row, its evolution, and the entry check run by the kernel for each alignment:

```wl
show[{"initRow", "G", "checkEntry"}, "TermForm"]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it
resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.edge_pinned"]["KernelCheck"]
```
'''
out = prose.decode().rstrip('\n') + formal
(d / 'essay.md').write_text(out)
print('essay.md written: %d bytes, sha256 %s' % (len(out.encode()), hashlib.sha256(out.encode()).hexdigest()))
