#!/usr/bin/env python3
"""assemble_late_twins_essay.py (Local, Block 7): essay.md for S-02: front matter, the prose with the computation at the end
of section 5, the formal section with the portal form embedded verbatim. Run: python3 tests/probes/wolfram/assemble_late_twins_essay.py FOLDER"""
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
heads = ['F_shiftRight', 'iter_F_shiftRight', 'band_settles', 'band_late', 'sync', 'twin_of_factors', 'late_twin', 'late_twin_immortal', 'late_twin_off_orbit']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-08
Description: Core Lean. For every nonzero natural y and every t ≥ 46, the row F^(t-2)(y) beside the wall has a twin of the same width with the same image two ticks later; at even t it inherits immortality and lies off the orbit. Twins share their future. Nothing here proves Q01.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, Q01, zero-boundary left half, backward transducer, reset words, left side, twin, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)", "S. Wolfram, Random sequence generation by cellular automata, Advances in Applied Mathematics 7 (1986) 123-169"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261106-45f6e9: Q01, mortality and repeat budgets](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-45f6e9)", "[R30-20261106-bdd993: the first checks](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-bdd993)"]
---

'''
compute = '''

```wl
R[u_] := BitXor[BitShiftRight[u, 2], BitOr[BitShiftRight[u, 1], u]];
F[y_] := BitXor[BitShiftRight[y], BitOr[y, BitShiftLeft[y]]];
c13 = {6411, 6428, 7117, 7129}; c20 = {820683, 822904, 911005, 912610};
entry[v0_, c_] := Module[{v = v0, t = 0}, While[! MemberQ[c, v], v = R[v]; t++]; t];
pre[z_, b_] := Module[{y = {b}}, Do[AppendTo[y, BitXor[BitGet[z, i], BitOr[y[[-1]], If[Length[y] >= 2, y[[-2]], 0]]]], {i, 0, BitLength[z] + 2}];
  If[y[[-1]] == 0 && y[[-2]] == 0, FromDigits[Reverse[y], 2], Missing[]]];
twins[x_] := Select[Table[With[{x1 = pre[F[F[x]], b1]}, If[MissingQ[x1], x1, pre[x1, BitGet[x, 0]]]], {b1, 0, 1}], IntegerQ[#] && # != x &];
check[y_] := With[{x = Nest[F, y, 44]}, With[{x45 = F[x], tw = twins[x]},
  {MemberQ[c20, BitShiftRight[x45, BitLength[x45] - 20]],
   Length[tw] >= 1 && AllTrue[tw, BitLength[#] == BitLength[x] && BitGet[#, 0] == BitGet[x, 0] && F[F[#]] == F[F[x]] &]}]];
{Max[entry[#, c13] & /@ Range[4096, 8191]], Max[Flatten[Table[entry[c 128 + b, c20], {c, c13}, {b, 0, 127}]]], check /@ {1, 3, 5, 7, 331, 1493, 11083}}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30ZeroBoundary`, which holds the integer form of the wall dynamics and the backward transducer.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30ZeroBoundary", "Ruliology.CellularAutomata.Rule30ZeroBoundary.IntegerForm"};
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
rule30Submission["Rule30Submission.late_twin"]["KernelCheck"]
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
