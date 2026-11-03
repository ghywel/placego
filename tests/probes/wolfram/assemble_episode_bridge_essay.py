#!/usr/bin/env python3
"""assemble_episode_bridge_essay.py (Local, L1464, NIGHT-TASKS A5; adapted from assemble_moving_wall_essay.py): essay.md = essay-prose.md + the formal section, with the
checked portal form embedded verbatim as a multi-line string after (*Iconize["Lean source"]*), as the healing-bound
assembler did. Both inputs are pinned by digest. Run: python3 tests/probes/wolfram/assemble_episode_bridge_essay.py FOLDER
"""
import hashlib, sys
from pathlib import Path
d = Path(sys.argv[1])
prose = (d / 'essay-prose.md').read_bytes(); src = (d / 'Rule30Submission.lean').read_bytes()
pins = {'essay-prose.md': ('1e988089babb25c45deae7c3713e6d2eab45a2e45208b03172d70b6d925e4000', prose),
        'Rule30Submission.lean': ('69391dbf907c0b8c007943d1a1202cedc834495ac9c5168037d14ce2751a5066', src)}
for name, (want, data) in pins.items():
    got = hashlib.sha256(data).hexdigest()
    if got != want:
        raise SystemExit('REFUSED: %s digest %s, pinned %s' % (name, got, want))
s = src.decode()
assert '"' not in s and '\\' not in s, 'the source must embed as a plain string literal'
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit modules it builds on
(`Rule30FrozenRuler`, `Rule30GateClocks`, `Rule30EtherEpisode`, `Rule30EdgeStaircases`) at the verifier's kit commit
93d98bbe: the edge map as a gate clock, the uniform prefix period, phases and episodes, the horizon and the finite
criterion, the pasted eternal point, the bridge, and the two controls.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30FrozenRuler"};
heads = {"episode_bridge", "mfinite_iff", "episode_extend", "eternal_of_long", "eternal_of_eventual", "rain_not_mfinite"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The horizon, as defined in the module:

```wl
show[{"horizon"}, "TermForm"]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it
resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.episode_bridge"]["KernelCheck"]
```
'''
out = prose.decode().rstrip('\n') + formal
(d / 'essay.md').write_text(out)
print('essay.md written: %d bytes, sha256 %s' % (len(out.encode()), hashlib.sha256(out.encode()).hexdigest()))
