#!/usr/bin/env python3
"""assemble_four_fronts_essay.py (Local, L1524): essay.md for the forced-front entry: front matter, the prose with a computation after section 5's text,
the formal sections at the end, the portal form embedded verbatim. Run: python3 tests/probes/wolfram/assemble_four_fronts_essay.py FOLDER"""
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
Description: An explicit tick in core Lean. Every configuration with a leftmost black cell carries one of four explicit strips on every left diagonal through wheel 87,866 from tick 177,560 + s of its own clock, with s at most 15, and the time of each wheel is given by a settling recursion evaluated by the kernel.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, left diagonals, left side, settling time, forced front, Rowland, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)", "[Rowland, Local nested structure in rule 30](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261104-458f3b: exactly four left sides through wheel 87,866](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261104-458f3b)", "[R30-20261104-309041: one left side through wheel 53,207](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261104-309041)", "[R30-20261103-1c93e6: exact bounded whiteCount witnesses](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-1c93e6)"]
---

'''
compute = '''

```wl
K = 87867; mask = 2^K - 1;
step[v_] := BitAnd[BitXor[BitShiftLeft[v, 2], BitOr[BitShiftLeft[v, 1], v]], mask];
A = Nest[step, 1, 128000];
bits = Reverse[IntegerDigits[#, 2, K]] & /@ NestList[step, A, 15];
black = Total[bits];
t = 1;
F = Join[{0, 1}, Table[If[black[[j + 1]] > 0, While[bits[[Mod[t, 16] + 1, j + 1]] == 0, t++]; t++]; t, {j, 1, 87865}]];
{Nest[step, A, 16] == A, F[[53208]], F[[87867]], Hash[IntegerString[A, 16], "SHA256", "HexString"]}
```

```wl
reach[v_] := Module[{x = v, n = 0}, While[x != A && n < 128000, x = step[x]; n++]; n];
Grid[{{"F(87,866) on A0", F[[87867]]}, {"first tick at which the single black cell equals A0", reach[1]}}, Frame -> All]
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30AgedLeftDiagonals`, which brings `Rule30FiniteDiagonals`, `Rule30Diagonals` and `Rule30Realization`. Its first part repeats the module of R30-20261104-458f3b, because the verifier's kit does not hold that module. The rest is the recursion, the moves with the time carried, the walk and the numbers. The kernel checks the four front values and the settling bounds in section 1 independently of the computation above. The build times in section 4 were measured on the M5.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30AgedLeftDiagonals", "Ruliology.CellularAutomata.Rule30FiniteDiagonals", "Ruliology.CellularAutomata.Rule30Diagonals"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = {"forced_front_four", "forced_front_four_uniform", "forced_front_four_left_side", "forced_front_four_seed", "classification_bounded",
   "forced_front_low", "forced_front_low_left_side", "FA0_87866", "FA1_87866", "FB0_87866", "FB1_87866"};
show[Take[heads, 5], "TypeForm"]
```

The statement below the first fork, and the four fronts:

```wl
show[Take[heads, -6], "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.forced_front_four_left_side"]["KernelCheck"]
```
'''
i = body.index('\n## 6. ')
out = front + body[:i].rstrip('\n') + compute + body[i:].rstrip('\n') + formal
for bad in ('DRAFT', 'Not for posting', 'See abstract'):
    assert bad not in out, bad
(d / 'essay.md').write_text(out)
h = hashlib.sha256((d / 'essay.md').read_bytes()).hexdigest()
(d / 'essay.sha256').write_text(h + '\n')
for name in ('essay-prose.md', 'title.txt', 'abstract.txt', 'Rule30Submission.lean', 'essay.md'):
    print(name, hashlib.sha256((d / name).read_bytes()).hexdigest())
print('abstract words', len(abstract.split()))
