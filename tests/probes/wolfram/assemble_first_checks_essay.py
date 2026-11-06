#!/usr/bin/env python3
"""assemble_first_checks_essay.py (Local, Block 7): essay.md for S-03: front matter, the prose with the computation at the end
of section 5, the formal section with the portal form embedded verbatim. Run: python3 tests/probes/wolfram/assemble_first_checks_essay.py FOLDER"""
import hashlib
import sys
from pathlib import Path

d = Path(sys.argv[1])
prose = (d / 'essay-prose.md').read_text()
title = (d / 'title.txt').read_text().strip()
abstract = ' '.join((d / 'abstract.txt').read_text().split())
src = (d / 'Rule30Submission.lean').read_text()
assert '"' not in src and '\\' not in src, 'the source must embed as a plain string literal'
lines = prose.split('\n')
assert lines[0] == '# ' + title and lines[2].startswith('Gareth Herbert;'), lines[:3]
body = '\n'.join(lines[3:]).strip('\n')
heads = ['two_tick', 'check_xor', 'four_sum', 'pair_count', 'overlap', 'adjacent', 'distance_two', 'two_of_three', 'first_check_count', 'first_check_balanced']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-06
Description: Core Lean. An exact pair law between the first check past the free range and the check of the shifted word, an exact count of the rows that pass, and the consequence that at most one of any three consecutive checks is near constant. First check only. Nothing here proves Q01.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, Q01, free bits, zero-boundary left half, first check, pair law, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)", "S. Wolfram, Random sequence generation by cellular automata, Advances in Applied Mathematics 7 (1986) 123-169"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261106-45f6e9: Q01, mortality and repeat budgets](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-45f6e9)"]
---

'''
compute = '''

```wl
theta[f_, k_] := Module[{c = Table[If[EvenQ[t], 1, If[(t + 1)/2 <= Length[f], f[[(t + 1)/2]], 0]], {t, 0, k - 1}], p, q},
  p = ConstantArray[0, k];
  Do[q = Table[BitXor[c[[i + 1]], BitOr[c[[i]], p[[i]]]], {i, Length[c] - 1}]; p = c; c = q, {k - 1}];
  First[c]];
check[l_] := theta[l, 2 Length[l] + 1];
ones = Table[Total[check /@ Tuples[{0, 1}, n]], {n, 0, 12}];
flips = Table[Count[Tuples[{0, 1}, n], l_ /; check[l] != check[Rest[l]]], {n, 2, 12}];
F[y_] := BitXor[BitShiftRight[y], BitOr[y, BitShiftLeft[y]]];
rows = Table[Count[Range[0, 4^n - 1], y_ /; AllTrue[NestList[F[F[#]] &, y, n], OddQ]], {n, 1, 6}];
gaps = Table[Min[ones[[n + 1]], 2^n - ones[[n + 1]]], {n, 0, 12}];
{ones, flips, flips == Table[2^(n - 2) + ones[[n - 1]], {n, 2, 12}], rows == Table[2^n - ones[[n + 1]], {n, 1, 6}], Select[Range[0, 12], 40 gaps[[# + 1]] < 2^# &]}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30ZeroBoundary`, which holds `Theta` and the counting of constrained starts.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30ZeroBoundary"};
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
rule30Submission["Rule30Submission.pair_count"]["KernelCheck"]
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
