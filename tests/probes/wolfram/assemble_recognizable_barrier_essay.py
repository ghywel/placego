#!/usr/bin/env python3
"""assemble_recognizable_barrier_essay.py (Local, 10 November 2026; S-19, Cloud's K-06 with K-01): essay.md for the
recognizable-statistic barriers: front matter, the prose with the computation at the end of section 5, the formal
section with the portal form embedded verbatim. Adapted from the S-21 assembler.
Run: python3 tests/probes/wolfram/assemble_recognizable_barrier_essay.py FOLDER"""
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
heads = ['no_recognizable_ranking', 'no_recognizable_ranking_nat', 'no_wall_recognizable_ranking', 'no_windowed_recognizable_ranking', 'no_local_ranking_of_recognizable', 'edge_decomp', 'sharp_rows_check', 'sharp_rows_width', 'sharp_rows_survive', 'sharp_rows_fourteen', 'no_width_bounded_ranking', 'no_edge_automaton_ranking', 'no_joint_recognizable_ranking', 'no_joint_recognizable_ranking_nat', 'no_joint_windowed_recognizable_ranking', 'no_joint_local_ranking_of_recognizable', 'c7cut_span']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. No rank of the width and a finite-monoid image of the row falls at every surviving double step, in the zero-boundary and the coupled frames; two rows of width 11 defeat every width-bounded rank. Statements about proof shapes; nothing here decides Q01 or period 2.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, period two, Q01, zero-boundary left half, barrier, ranking function, finite monoid, recognizable, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

'''
compute = '''

```wl
f[y_] := BitXor[BitShiftRight[y, 1], BitOr[y, BitShiftLeft[y, 1]]];
firstEven[y_] := LengthWhile[NestList[f[f[#]] &, y, 400], OddQ];
maxima = Table[Max[firstEven /@ Select[Range[2^(len - 1), 2^len - 1], OddQ]], {len, 1, 12}];
arg11 = Select[Range[2^10 + 1, 2^11 - 1, 2], firstEven[#] == maxima[[11]] &];
tick[row_] := Prepend[Table[BitXor[row[[k + 2]], BitOr[row[[k + 1]], row[[k]]]], {k, 1, Length[row] - 2}], 0];
iterRow[n_, j_] := Nest[Append[tick[#], 0] &, Join[{0}, Table[Mod[k, 2], {k, 1, n}], ConstantArray[0, 2 j + 2]], 2 j];
decomp = And @@ Flatten[Table[Module[{row = iterRow[n, j], w = n + 2 j, k = (n + 1 - 2 j)/2, edge},
      edge = row[[w + 1 ;; 2 ;; -1]];
      {row[[w + 1]] == 1, Total[row[[w + 2 ;;]]] == 0, Take[edge, -2 k] == Flatten[ConstantArray[{0, 1}, k]],
       Take[edge, 4 j - 1] == Take[Reverse[iterRow[4 j + 1, j][[2 ;; 6 j + 2]]], 4 j - 1]}],
     {n, 5, 41, 2}, {j, 1, Floor[n/4]}]];
{firstEven[1493], firstEven[1507], maxima, arg11, decomp}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30ZeroBoundaryBarriers`.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30ZeroBoundary", "Ruliology.CellularAutomata.Rule30ZeroBoundaryBarriers"};
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
rule30Submission["Rule30Submission.c7cut_span"]["KernelCheck"]
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
