#!/usr/bin/env python3
"""assemble_cone_tip_essay.py (Local, 10 November 2026; S-17): essay.md for the cone tip of the zero-boundary left
half: front matter, the prose with the computation at the end of section 4, the formal section with the portal form
embedded verbatim. Adapted from the S-08 hybrid assembler.
Run: python3 tests/probes/wolfram/assemble_cone_tip_essay.py FOLDER"""
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
heads = ['level_aff', 'diag', 'chain_flip', 'cone_tip', 'face_disagree', 'affine_second', 'tip_not_affine']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. In the zero-boundary left half of rule 30 the second difference of the depth-1 cell at tick t in depths t - 1 and t is t - 1 mod 2 on every row; for even t the cell is not affine and disagrees with every affine function on each face of four rows.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, zero-boundary left half, left permutivity, Boolean derivative, algebraic degree, affine, Walsh, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

'''
compute = '''

```wl
tips[t_] := Module[{n = t + 1, nn, w, c, y},
   nn = 2^n; w = 2 t + 4;
   c = Join[{0}, Table[If[d <= n, FromDigits[Reverse[Table[BitGet[y, d - 1], {y, 0, nn - 1}]], 2], 0], {d, 1, w}], {0}];
   Do[c = Join[{0}, Table[BitXor[c[[k + 2]], BitOr[c[[k + 1]], c[[k]]]], {k, 1, w}], {0}], {t}];
   Reverse[IntegerDigits[c[[2]], 2, nn]]];
law[t_] := With[{a = tips[t], bt = 2^(t - 1), bt1 = 2^(t - 2)}, AllTrue[Range[0, 2^(t + 1) - 1], BitXor[a[[# + 1]], a[[BitXor[#, bt] + 1]], a[[BitXor[#, bt1] + 1]], a[[BitXor[#, bt, bt1] + 1]]] == Mod[t - 1, 2] &]];
maxWalsh[t_] := Module[{v = 1 - 2 tips[t], h = 1, len, a, b},
   len = Length[v];
   While[h < len, Do[Do[a = v[[j]]; b = v[[j + h]]; v[[j]] = a + b; v[[j + h]] = a - b, {j, i, i + h - 1}], {i, 1, len, 2 h}]; h *= 2];
   Max[Abs[v]]/len];
walsh = maxWalsh /@ Range[2, 12];
{AllTrue[Range[2, 14], law], AllTrue[Transpose[{Range[2, 12], walsh}], OddQ[#[[1]]] || #[[2]] <= 1/2 &], walsh}
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
rule30Submission["Rule30Submission.tip_not_affine"]["KernelCheck"]
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
