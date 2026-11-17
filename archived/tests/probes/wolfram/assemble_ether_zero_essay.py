#!/usr/bin/env python3
"""assemble_ether_zero_essay.py (Local, L1354, NIGHT-TASKS A1): essay.md = essay-prose.md + the formal section, with the
checked portal form embedded verbatim as a multi-line string after (*Iconize["Lean source"]*), as the ether-episode
assembler did. Both inputs are pinned by digest. Run: python3 tests/probes/wolfram/assemble_ether_zero_essay.py FOLDER
"""
import hashlib, sys
from pathlib import Path
d = Path(sys.argv[1])
prose = (d / 'essay-prose.md').read_bytes(); src = (d / 'Rule30Submission.lean').read_bytes()
pins = {'essay-prose.md': ('86068b3900b0fcee9a769d179eef0654ab425ac0bcfadbf12cf7ca2bcd18f831', prose), 'Rule30Submission.lean': ('4a2688b0c03fd1274aa0a2381f98b5405f7fb42ab0a1bde1c1472bcf6db07018', src)}
for name, (want, data) in pins.items():
    got = hashlib.sha256(data).hexdigest()
    if got != want:
        raise SystemExit('REFUSED: %s digest %s, pinned %s' % (name, got, want))
s = src.decode()
assert '"' not in s and '\\' not in s, 'the source must embed as a plain string literal'
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30Ether` at the
verifier's kit commit 93d98bbe. The 28 entries and the never-heals table are proved by `decide`, which the kernel
evaluates. The rest is induction, rewriting and `omega`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"''' + s + '''", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The four headlines, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30Ether"};
heads = {"edge_pinned", "edge_pinned_tail", "trap_two_sided", "wall_ne_ref_all"};
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
