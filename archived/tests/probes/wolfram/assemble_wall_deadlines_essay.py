#!/usr/bin/env python3
"""assemble_wall_deadlines_essay.py (Local, 10 November 2026; S-18): essay.md for the wall deadlines of rules 90 and
150: front matter, the prose with the computation at the end of section 5, the formal section with the portal form
embedded verbatim. Adapted from the S-17 assembler.
Run: python3 tests/probes/wolfram/assemble_wall_deadlines_essay.py FOLDER"""
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
heads = ['zr_or_eq_zrow', 'fib2_mod', 'odd90', 'kstar_spec', 'deadline90', 'sharp90', 'two_step150', 'odd150', 'deadline150', 'sharp150']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. Beside a white wall, rules 90 and 150 answer the kit period-two question exactly: every start of width at most W turns depth 1 white by an explicit linear deadline, and explicit classes of starts attain it. Not rule 30.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, period two, Q01, zero-boundary left half, rule 90, rule 150, Fibonacci, deadline, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

'''
compute = '''

```wl
firstWhite[y_, w_, h_] := Module[{r = Join[{0}, Table[BitGet[y, d - 1], {d, 1, w}], ConstantArray[0, 63]], t = 0, res = None},
   While[t <= 60 && res === None, If[EvenQ[t] && r[[2]] == 0, res = t, r = Join[{0}, Table[BitXor[r[[k + 2]], h[r[[k + 1]], r[[k]]]], {k, 1, Length[r] - 2}], {0}]; t++]]; res];
kstar[w_] := SelectFirst[Range[w + 1, w + 6], OddQ[#] && Mod[#, 3] != 0 &];
h90[b_, c_] := c; h150[b_, c_] := BitXor[b, c]; fib[k_] := If[Mod[k, 3] == 0, 0, 1];
res = Table[Module[{f90 = Table[firstWhite[y, w, h90], {y, 0, 2^w - 1}], f150 = Table[firstWhite[y, w, h150], {y, 0, 2^w - 1}], p90, p150},
    p90 = Select[Range[0, 2^w - 1], Function[y, AllTrue[Range[1, w, 2], BitGet[y, # - 1] == fib[#] &]]];
    p150 = Select[Range[0, 2^w - 1], Function[y, AllTrue[Range[1, w, 2], BitGet[y, # - 1] == 1 &]]];
    {Max[f90], Max[f150], Max[f90] == kstar[w] - 1, Max[f150] == 2 Ceiling[w/2],
     Flatten[Position[f90, Max[f90]]] - 1 === p90 && Length[p90] == 2^Floor[w/2] && Flatten[Position[f150, Max[f150]]] - 1 === p150 && Length[p150] == 2^Floor[w/2]}], {w, 1, 12}];
{And @@ res[[All, 3]], And @@ res[[All, 4]], res[[All, 1]], res[[All, 2]], And @@ res[[All, 5]]}
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
rule30Submission["Rule30Submission.sharp150"]["KernelCheck"]
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
