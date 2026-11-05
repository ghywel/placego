#!/usr/bin/env python3
"""assemble_error_edge_essay.py (Local, L1553): essay.md for the error-edge entry: front matter, the prose with the computation after section 5's text, the formal sections at the end,
the portal form embedded verbatim. Run: python3 tests/probes/wolfram/assemble_error_edge_essay.py FOLDER"""
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
assert lines[0] == '# ' + title and lines[2].startswith('Gareth Herbert;'), lines[:3]
body = '\n'.join(lines[3:]).strip('\n')
heads = ['agree_step', 'agree_after', 'edge_le', 'heal_iff', 'edge_stall', 'edge_heal', 'white_above', 'black_two_above',
         'jump_two', 'jump_three', 'jump_four', 'jump_five', 'jump_six', 'jump_seven']
(d / 'headlines.txt').write_text(' '.join('Rule30Submission.' + h for h in heads) + '\n')
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-05
Description: Core Lean. For any two arrays with the left-diagonal recurrence, agreement below the lowest differing wheel is kept, the arrays agree at that wheel one tick later exactly when the wheel below it is black, and six laws constrain the new parent after a heal.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, left diagonals, damage front, difference pattern, error edge, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)", "S. Wolfram, Random sequence generation by cellular automata, Adv. Appl. Math. 7 (1986)", "S. Wolfram, A New Kind of Science (2002), p. 949"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261103-e660e4: the universal healing bound](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-e660e4)"]
---

'''
compute = '''

```wl
n = 3000; d = 500; w = 2 n + d + 61; c = n + 11;
row[cells_] := ReplacePart[ConstantArray[0, w], Thread[cells -> 1]];
{a, b} = CellularAutomaton[30, row[#], n] & /@ {{c}, {c, c + d}};
wheel[x_, j_, t_] := x[[t + 1, c - t + j]];
e = 0; edge = Table[While[wheel[a, e, t] == wheel[b, e, t], e++]; e, {t, 0, n}];
heals = Select[Range[0, n - 2], edge[[# + 2]] > edge[[# + 1]] &];
jump[t_] := edge[[t + 2]] - edge[[t + 1]];
p1[t_] := wheel[a, edge[[t + 2]] - 1, t + 1];
p2[t_] := wheel[a, edge[[t + 2]] - 1, t + 2];
bad[t_] := Switch[jump[t], 2, p1[t] != 0, 3, p1[t] != 1, 4, p2[t] != 1, 5, p1[t] == 0 && p2[t] != 1, 6 | 7, p1[t] == 0 && p2[t] != 0, _, False];
healOK = AllTrue[Range[0, n - 2], (edge[[# + 2]] > edge[[# + 1]]) == (wheel[a, edge[[# + 1]] - 1, #] == 1) &];
{edge[[n + 1]], Length[heals], KeySort[Counts[jump /@ heals]], healOK, Count[heals, _?bad]}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30AgedLeftDiagonals`, which holds the recurrence.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30AgedLeftDiagonals"};
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
rule30Submission["Rule30Submission.heal_iff"]["KernelCheck"]
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
print('abstract words', len(abstract.split()), 'headlines', len(heads))
