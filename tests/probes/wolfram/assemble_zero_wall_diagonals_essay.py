#!/usr/bin/env python3
"""assemble_zero_wall_diagonals_essay.py (Local, 10 November 2026; S-12): essay.md for the zero-wall diagonals,
bounded lag and factor complexity: front matter, the prose with the computation at the end of section 5, the formal
section with the portal form embedded verbatim. Adapted from the S-08 hybrid assembler.
Run: python3 tests/probes/wolfram/assemble_zero_wall_diagonals_essay.py FOLDER"""
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
heads = ['E_entry', 'E_tailLeft', 'tail_periodic', 'tail_profile_bound', 'tail_white_unbounded', 'tail_no_two_white', 'tail_black_after_white', 'tail_black_unbounded', 'E_black_unbounded', 'row_eq_Theta', 'rows_agree', 'freeWord_bounded_lag', 'freeWord_bounded_lag_of_finSupp', 'le_factorCount', 'factorCount_le', 'factorCount_succ', 'rightSpecialCount_pos', 'two_run', 'complexity_of_bounded_lag', 'freeWord_complexity']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. Zero-wall left diagonals of rule 30 obey their recurrence from entry time, giving eventually black diagonals of every large index; hence a surviving finite row would have a free word with bounded-lag repeats and unbounded factor-complexity excess. Conditional on Q01 failing.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, period two, Q01, zero-boundary left half, left diagonals, factor complexity, right-special factors, Sturmian words, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

'''
compute = '''

```wl
T = 600; m = 1; width = m + T + 4;
rows = NestList[Function[r, Join[{0}, Table[BitXor[r[[k + 2]], BitOr[r[[k + 1]], r[[k]]]], {k, 1, width}], {0}]], Join[{0}, Table[If[k == m, 1, 0], {k, 1, width}], {0}], T + 1];
EE[j_, t_] := If[m + t - j >= 0, rows[[t + 1, m + t - j + 1]], 0];
inside = AllTrue[Flatten[Table[If[j + 2 <= m + t, EE[j + 2, t + 1] == BitXor[EE[j, t], BitOr[EE[j + 1, t], EE[j + 2, t]]], True], {t, 0, T - 1}, {j, 0, 12}]], TrueQ];
outside = AnyTrue[Flatten[Table[If[j + 2 == m + t + 1, EE[j + 2, t + 1] != BitXor[EE[j, t], BitOr[EE[j + 1, t], EE[j + 2, t]]], False], {t, 0, T - 1}, {j, 0, 12}]], TrueQ];
latePeriod[j_] := With[{s = Table[EE[j, t], {t, 400, 599}]}, SelectFirst[Range[200], Function[p, AllTrue[Range[Length[s] - p], s[[#]] == s[[# + p]] &]]]];
periods = latePeriod /@ Range[0, 10];
divides = AllTrue[Range[0, 10], Divisible[2^#, periods[[# + 1]]] &];
fibw = Take[Nest[{#[[2]], Join[#[[2]], #[[1]]]} &, {{0}, {0, 1}}, 25][[2]], 20000];
fibcounts = Table[With[{f = Union[Partition[Most[fibw], n, 1]], g = Union[Partition[Most[fibw], n + 1, 1]]}, {Length[f], Count[f, u_ /; MemberQ[g, Append[u, 0]] && MemberQ[g, Append[u, 1]]]}], {n, 1, 12}];
{inside, outside, divides, periods, fibcounts === Table[{n + 1, 1}, {n, 1, 12}]}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30LeftUnbounded` and `Rule30ZeroBoundary`.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30ZeroBoundary", "Ruliology.CellularAutomata.Rule30LeftReset"};
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
rule30Submission["Rule30Submission.freeWord_complexity"]["KernelCheck"]
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
