#!/usr/bin/env python3
"""assemble_not_absorption_essay.py (Local, 10 November 2026; S-05): essay.md for AbsorptionT t001: front matter, the
prose with the computation at the end of section 4, the formal section with the portal form embedded verbatim.
Adapted from assemble_free_middle_essay.py (S-13).
Run: python3 tests/probes/wolfram/assemble_not_absorption_essay.py FOLDER"""
import hashlib
import sys
from pathlib import Path

d = Path(sys.argv[1])
prose = (d / 'essay-prose.md').read_text()
title = (d / 'title.txt').read_text().strip()
abstract = (d / 'abstract.txt').read_text().strip()
assert abstract == ' '.join(abstract.split()), 'abstract.txt must be one canonical line for the notebook byte check'
src = (d / 'Rule30Submission.lean').read_text()
assert '"' not in src and '\\' not in src, 'the source must embed as a plain string literal'
lines = prose.split('\n')
assert lines[0] == '# ' + title and lines[2].startswith('Gareth Herbert;'), lines[:3]
body = '\n'.join(lines[3:]).strip('\n')
heads = ['trap001fifteen_check', 'fifteen_apart_t001', 'stays', 'not_absorptionT_t001', 'rule30open_half']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean, the kit's own definitions. The kit's open statement AbsorptionT t001 for the period-3 word 001 is false: a checked period-15 trap for 001 is apart from t001, and a right half started in it never enters t001. The theorem and the trap are Logan Hallee's, in lhallee/rule30-open; this restates it in the kit's form so that the kit's status can be corrected.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, period three, 001, trap, AbsorptionT, right half, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[lhallee/rule30-open](https://github.com/lhallee/rule30-open)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[rule30-open: Traps001](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/Rule30Open/Columns/Traps001.md)"]
---

'''
compute = '''

```wl
trapSource = Import[FileNameJoin[{Environment["RULE30PRIZE_KIT"], "lean", "Ruliology", "CellularAutomata", "Rule30EtherThreeTrap.lean"}], "Text"];
num[name_] := ToExpression[First[StringCases[trapSource, "def " <> name <> " : Nat := " ~~ digits : DigitCharacter .. :> digits]]];
r001 = num["t001_R"]; l001 = num["t001_L"];
states = GroupBy[Table[{Mod[BitShiftRight[l001, 5 i], 2^5], Mod[BitShiftRight[r001, 47 i], 2^47]}, {i, 0, 814}], (Mod[First[#], 3] &) -> Last, AssociationThread[# -> True] &];
run[x0_] := Module[{x = x0, first = -1, seen = <||>}, Do[If[first < 0 && KeyExistsQ[Lookup[states, Mod[t, 3], <||>], Mod[x, 2^47]], first = t]; seen[Mod[x, 2^52]] = True; x = BitXor[BitOr[BitShiftLeft[x, 1], {0, 0, 1}[[Mod[t, 3] + 1]]], BitOr[x, BitShiftRight[x, 1]]], {t, 0, 3000}]; {first, Length[seen]}];
{a, r, c} = run /@ {266113541000008, 196676618523018, 0};
{a[[1]], r[[1]], c[[1]], a[[2]], r[[2]]}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30EtherThreeTrap`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"''' + src + '''", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The theorems, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30EtherThree", "Ruliology.CellularAutomata.Rule30Ether", "Ruliology.CellularAutomata.Rule30StripCertificates"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = ''' + wl + ''';
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.rule30open_half"]["KernelCheck"]
```
'''
i = body.index('\n## 5. ')
out = front + body[:i].rstrip('\n') + compute + body[i:].rstrip('\n') + formal
for bad in ('DRAFT', 'Not for posting', 'See abstract'):
    assert bad not in out, bad
(d / 'essay.md').write_text(out)
h = hashlib.sha256((d / 'essay.md').read_bytes()).hexdigest()
(d / 'essay.sha256').write_text(h + '\n')
for name in ('essay-prose.md', 'title.txt', 'abstract.txt', 'Rule30Submission.lean', 'essay.md'):
    print(name, hashlib.sha256((d / name).read_bytes()).hexdigest())
print('abstract words', len(abstract.split()), 'headlines', len(heads))
