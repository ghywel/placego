#!/usr/bin/env python3
"""assemble_four_left_essay.py (Local, L1514): essay.md for the four-left-sides entry: front matter, the prose with a computation
after section 5's text, the formal sections after section 8, the portal form embedded verbatim.
Run: python3 tests/probes/wolfram/assemble_four_left_essay.py FOLDER
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
lines = prose.split('\n')
assert lines[0].startswith('# ') and lines[2].startswith('Gareth Herbert;'), lines[:3]
body = '\n'.join(lines[3:]).strip('\n')
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-04
Description: A classification in core Lean: every configuration with a leftmost black cell carries one of four explicit strips on every left diagonal through wheel 87,866, all four occur, and no time shift relates two of them. As arithmetic, every odd number reaches one of four numbers under one map modulo 2^87867.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, left diagonals, left side, Rowland, classification, T-function, cycles, fork, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)", "[Rowland, Local nested structure in rule 30](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf)", "[Nersissian, Diagonal Periods and Newton Supports of Rules 30, 86 and 135](https://arxiv.org/abs/2609.25077)", "[OEIS A364239](https://oeis.org/A364239)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261104-309041: one left side through wheel 53,207](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261104-309041)", "[R30-20261027-317c64: Bosdure's universal left-edge crystal](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-317c64)", "[R30-20261104-30d8ae: Quint and Gemini's extension of the left-coincidence module](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261104-30d8ae)"]
---

'''
compute = '''

```wl
K = 87867; mask = 2^K - 1;
step[v_] := BitAnd[BitXor[BitShiftLeft[v, 2], BitOr[BitShiftLeft[v, 1], v]], mask];
A = Nest[step, 1, 128000];
all = BitOr @@ NestList[step, A, 15];
{Nest[step, A, 16] == A, IntegerLength[A, 16], Select[Range[0, K - 1], BitGet[all, #] == 0 &],
 Hash[IntegerString[A, 16], "SHA256", "HexString"]}
```

```wl
reach[v_] := Module[{x = v, n = 0}, While[x != A, x = step[x]; n++]; n];
Grid[Prepend[{#, reach[#]} & /@ {1, 7}, {"odd start", "ticks to reach A0"}], Frame -> All]
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30AgedLeftDiagonals`, which brings `Rule30FiniteDiagonals`, `Rule30Diagonals` and `Rule30Realization`. The four rows are the hexadecimal literals in the source, and every `decide +kernel` is the Lean kernel evaluating sixteen rows of them.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"''' + src + '''", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The classification, as Lean prints it:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30AgedLeftDiagonals", "Ruliology.CellularAutomata.Rule30FiniteDiagonals", "Ruliology.CellularAutomata.Rule30Diagonals"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = {"universal_of_strip", "left_side_classification", "exactly_four_left_sides", "on_exactly_one", "odd_reaches_one_of_four",
   "least_period_16", "seed_classified", "four_distinct", "fork_weights"};
show[Take[heads, 4], "TypeForm"]
```

The arithmetic form, the seed, the distinctness and the fork weights:

```wl
show[Take[heads, -5], "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.exactly_four_left_sides"]["KernelCheck"]
```
'''
i = body.index('\n## 6. ')
j = body.index('\n## 8. ')
assert body.find('\n## ', j + 1) == -1, 'section 8 must be the last section'
out = front + body[:i].rstrip('\n') + compute + body[i:].rstrip('\n') + formal
for bad in ('DRAFT', 'Not for posting', 'See abstract'):
    assert bad not in out, bad
(d / 'essay.md').write_text(out)
for name in ('essay-prose.md', 'title.txt', 'abstract.txt', 'Rule30Submission.lean', 'essay.md'):
    print(name, hashlib.sha256((d / name).read_bytes()).hexdigest())
print('abstract words', len(abstract.split()))
