#!/usr/bin/env python3
"""assemble_universal_left_essay.py (Local, L1507): essay.md for the universal-left-side entry.

essay.md = front matter (title.txt, abstract.txt) + Cloud's essay-prose.md, unedited, without its title and byline lines, with a
computation cell after section 3 and the formal sections after section 8. The portal form is embedded verbatim.
Run: python3 tests/probes/wolfram/assemble_universal_left_essay.py FOLDER
"""
import hashlib
import sys
from pathlib import Path

d = Path(sys.argv[1])
prose = (d / 'essay-prose.md').read_text()
title = (d / 'title.txt').read_text().strip()
abstract = (d / 'abstract.txt').read_text().strip()
src = (d / 'Rule30Submission.lean').read_text()
assert '"' not in src and '\\' not in src, 'the source must embed as a plain string literal'
assert 'See abstract' not in abstract

lines = prose.split('\n')
assert lines[0].startswith('# ') and lines[2].startswith('Gareth Herbert;'), lines[:3]
body = '\n'.join(lines[3:]).strip('\n')

front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-04
Description: A two-sided answer in core Lean to Rowland's 2006 question on the left side of rule 30: every configuration with a leftmost black cell carries one strip on every left diagonal through wheel 53,207, up to one time shift, and two finite rows realize the two continuations at wheel 53,208, with no shift relating them.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, left diagonals, left side, Rowland, reset recurrence, universal strip, fork, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)", "[Rowland, Local nested structure in rule 30](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261103-3cf160: Rule 30, the picture so far](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-3cf160)", "[R30-20261104-30d8ae: Quint and Gemini's extension of the left-coincidence module](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261104-30d8ae)", "[R30-20261027-317c64: Bosdure's universal left-edge crystal](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-317c64)"]
---

'''

compute = '''

**A computation.** This replays the data in Wolfram Language, outside Lean, starting from the single black cell: 72,000 ticks of
the wall-frame map on 53,209 bits give `B`, sixteen more return to it, and the wheels below 53,208 with no black in the cycle are
the five named above. The table gives, for each white wheel, its farther wheel, the period `L` of the words below it, and the
farther weight over `L`. This cell is the replay behind the phrase "the seed's row at tick 72,000". The Lean below does not
depend on it: there `B` is a number, and every statement about it is checked by the kernel.

```wl
K = 53209; mask = 2^K - 1;
step[v_] := BitAnd[BitXor[BitShiftLeft[v, 2], BitOr[BitShiftLeft[v, 1], v]], mask];
B = Nest[step, 1, 72000];
rows = NestList[step, B, 15];
all = BitOr @@ rows;
white = Select[Range[0, K - 2], BitGet[all, #] == 0 &];
{Nest[step, B, 16] == B, IntegerLength[B], white}
```

```wl
weightRow[{w_, L_}] := {w, w - 1, L, Total[Table[BitGet[rows[[r]], w - 1], {r, L}]]};
Grid[Prepend[weightRow /@ {{2, 1}, {7, 2}, {28, 4}, {399, 8}, {53207, 16}},
  {"white wheel", "farther wheel", "L", "farther weight"}], Frame -> All]
```
'''

formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30AgedLeftDiagonals`, which
brings `Rule30FiniteDiagonals`, `Rule30Diagonals` and `Rule30Realization`. Nothing else is needed. The hexadecimal literal encodes a register of 53,209 wheels. The finite checks use Lean kernel reduction on its cycle and the cycle of the flipped register.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"''' + src + '''", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The generic theorem and the universal side, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30AgedLeftDiagonals", "Ruliology.CellularAutomata.Rule30FiniteDiagonals", "Ruliology.CellularAutomata.Rule30Diagonals"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = {"universal_of_strip", "universal_left_side", "one_left_side", "seed_left_side", "fork_dichotomy", "first_fork",
   "left_side_not_unique", "odd_farther_weights", "even_farther_weight"};
show[Take[heads, 4], "TypeForm"]
```

The fork, and Rowland's parity condition:

```wl
show[Take[heads, -5], "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it
resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.first_fork"]["KernelCheck"]
```
'''

i = body.index('\n## 4. ')
j = body.index('\n## 8. ')
k = body.find('\n## ', j + 1)
assert k == -1, 'section 8 must be the last section'
out = front + body[:i].rstrip('\n') + compute + body[i:].rstrip('\n') + formal
for bad in ('DRAFT', 'Not for posting', 'See abstract'):
    assert bad not in out, bad
(d / 'essay.md').write_text(out)
for name in ('essay-prose.md', 'title.txt', 'abstract.txt', 'Rule30Submission.lean', 'essay.md'):
    print(name, hashlib.sha256((d / name).read_bytes()).hexdigest())
print('abstract words', len(abstract.split()))
