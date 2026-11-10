#!/usr/bin/env python3
"""assemble_unrestricted_closing_essay.py (Local, 10 November 2026; S-23, Cloud's K-08): essay.md for the failure of
unrestricted tail closing on the constrained class: front matter, the prose with the computation at the end of
section 5, the formal section with the portal form embedded verbatim. Adapted from the S-22 assembler.
Run: python3 tests/probes/wolfram/assemble_unrestricted_closing_essay.py FOLDER"""
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
heads = ['two_A', 'two_B', 'two_C', 'two_cycle', 'inX_A', 'inX_B', 'inX_C', 'free_A', 'free_B', 'free_C', 'theta_A', 'theta_B', 'theta_C', 'differ_AB', 'differ_one_tick', 'not_unrestricted_closing']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. Three periodic rows of the zero-boundary left half of rule 30, all black at depth 1 at every even tick, with two of them mapped to the same row by two ticks while differing on every tail: unrestricted tail closing fails on the class. Nothing here decides Q01 or period 2.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, period two, Q01, zero-boundary left half, closing, counterexample, periodic rows, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

'''
compute = '''

```wl
n = 700;
pa = {1, 0, 1, 1, 1, 1, 1}; pb = {0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0}; pc = {1, 1, 0, 0, 0, 0, 1};
rowA = Table[pa[[Mod[d - 1, 7] + 1]], {d, 1, n}];
rowB = Join[{1, 1}, Table[pb[[Mod[d - 3, 14] + 1]], {d, 3, n}]];
rowC = Table[pc[[Mod[d - 1, 7] + 1]], {d, 1, n}];
tick[s_] := Module[{w = Join[{0}, s, {0}]}, Table[BitXor[w[[k + 2]], BitOr[w[[k + 1]], w[[k]]]], {k, 1, Length[s]}]];
g[s_] := tick[tick[s]];
m = n - 100;
same[x_, y_] := Take[x, m] === Take[y, m];
orbit[s_] := NestList[g, s, 39];
headsBlack = AllTrue[Join[orbit[rowA], orbit[rowB], orbit[rowC]], First[#] == 1 &];
free[s_] := StringJoin[ToString /@ (First[tick[#]] & /@ Take[orbit[s], 8])];
res = Union[Select[Range[3, m], rowA[[#]] =!= rowB[[#]] &]];
residues = Union[Mod[res, 14]];
consistent = AllTrue[Range[3, m], (rowA[[#]] =!= rowB[[#]]) === MemberQ[residues, Mod[#, 14]] &] && rowA[[2]] =!= rowB[[2]] && rowA[[1]] === rowB[[1]];
split = AllTrue[Range[0, Floor[(m - 10)/14] - 1], tick[rowA][[14 # + 4]] == 0 && tick[rowB][[14 # + 4]] == 1 &];
{same[g[rowA], rowC], same[g[rowB], rowC], same[g[rowC], rowA], headsBlack, {free[rowA], free[rowB], free[rowC]}, residues, consistent && split}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30ZeroBoundary`.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30ZeroBoundary"};
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
rule30Submission["Rule30Submission.not_unrestricted_closing"]["KernelCheck"]
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
