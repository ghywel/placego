#!/usr/bin/env python3
"""assemble_radius_two_clock_essay.py (Local, 10 November 2026; S-07): essay.md for the radius-two clock: front matter,
the prose with the computation at the end of section 5, the formal section with the portal form embedded verbatim.
Adapted from assemble_ether_cut_edge_essay.py (S-11).
Run: python3 tests/probes/wolfram/assemble_radius_two_clock_essay.py FOLDER"""
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
heads = ['rule_facts', 'z_frontier', 'row_formula', 'd_band', 'z_clock', 'clock', 'column0_alternates']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. Binary radius-two left-permutive rules N(p, q), white-quiescent and nonlinear, in which columns -2 and -1 equal t mod 2 at every time from the finite seed with black cells 0 and 2. The proof is finite: doubled blocks follow rule 150 with frontier sources, and a reflection band makes block -1 flip at every step. Not rule 30.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, left-permutive, radius two, cellular automaton, periodic column, finite seed, rule 150, reflection, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[A New Kind of Science, p. 270](https://www.wolframscience.com/nks/p270--special-initial-conditions/)"]
---

'''
compute = '''

```wl
gfun[p_, q_, w_] := Which[w === {1, 1, 0, 1}, p, w === {1, 0, 1, 1}, q, Equal @@ Rest[w], 0, True, 1];
run[p_, q_, black_, tmax_] := Module[{row = black, cols = {}, wins = {}, sup = True, x, lo, hi, new}, Do[x[i_] := Boole[MemberQ[row, i]]; AppendTo[cols, {x[-2], x[-1], x[0]}]; sup = sup && AllTrue[row, -2 t <= # <= 2 t + 2 &]; {lo, hi} = {Min[row] - 2, Max[row] + 2}; new = {}; Do[With[{w = {x[i - 1], x[i], x[i + 1], x[i + 2]}}, AppendTo[wins, w]; If[BitXor[x[i - 2], gfun[p, q, w]] == 1, AppendTo[new, i]]], {i, lo, hi}]; row = new; wins = Union[wins], {t, 0, tmax - 1}]; {cols, wins, sup}];
res = Flatten[Table[run[p, q, {0, 2}, 200], {p, 0, 1}, {q, 0, 1}], 1];
clocks = AllTrue[res, Function[r, And @@ MapIndexed[#1[[1]] == Mod[#2[[1]] - 1, 2] && #1[[2]] == Mod[#2[[1]] - 1, 2] &, r[[1]]]]];
wins = Union @@ (res[[All, 2]]);
exc = Count[Flatten[res[[All, 2]], 1], {1, 1, 0, 1} | {1, 0, 1, 1}];
col0 = AllTrue[Flatten[Table[run[p, q, {2, 4}, 200], {p, 0, 1}, {q, 0, 1}], 1], Function[r, And @@ MapIndexed[#1[[3]] == Mod[#2[[1]] - 1, 2] &, r[[1]]]]];
{clocks, Length[wins], exc, col0, And @@ res[[All, 3]]}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports only the official statements (`Rule30Prize`).

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata"};
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
rule30Submission["Rule30Submission.column0_alternates"]["KernelCheck"]
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
