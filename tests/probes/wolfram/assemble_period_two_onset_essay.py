#!/usr/bin/env python3
"""assemble_period_two_onset_essay.py (Local, 10 November 2026; S-21, Cloud's K-02): essay.md for the period-two
column-1 words from two ticks on: front matter, the prose with the computation at the end of section 5, the formal
section with the portal form embedded verbatim. Adapted from the S-18 assembler.
Run: python3 tests/probes/wolfram/assemble_period_two_onset_essay.py FOLDER"""
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
heads = ['win_dstep', 'img5_length', 'img6_length', 'img5_closed', 'img6_closed', 'no_word5', 'no_word6', 'no_short6',
         'onset5', 'onset6', 'col1_constraints5', 'col1_constraints6', 'free_bit5', 'free_bit6', 'free_bit_constraints5',
         'free_bit_constraints6']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. The kit period-two column-1 words at strip widths 5 and 6 hold from two ticks after the center starts to alternate, for every history that obeys rule 30 at columns 1 to b. Nothing here excludes period 2.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, period two, center column, column 1, forbidden words, free bits, explicit onset, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

'''
compute = '''

```wl
tick[l_, r_, x_] := CellularAutomaton[30, Join[{l}, x, {r}], 1][[2, 2 ;; -2]];
succ[x_] := Union[Flatten[Table[tick[1, r2, tick[0, r1, x]], {r1, 0, 1}, {r2, 0, 1}], 1]];
layer[c_, s_] := Select[s, First[#] == c &];
reads[s_, w_] := Fold[layer[#2, Union @@ (succ /@ #1)] &, layer[First[w], s], Rest[w]];
minimal[s_] := Module[{out = {}, go},
   go[w_, l_] := If[Length[w] < 13, Do[With[{l2 = layer[c, Union @@ (succ /@ l)]},
       If[l2 === {}, If[reads[s, Rest[Append[w, c]]] =!= {}, AppendTo[out, Append[w, c]]], go[Append[w, c], l2]]], {c, 0, 1}]];
   Do[If[layer[c, s] === {}, AppendTo[out, {c}], go[{c}, layer[c, s]]], {c, 0, 1}];
   SortBy[StringJoin[ToString /@ #] & /@ out, {StringLength, Identity}]];
digits[w_] := ToExpression /@ Characters[w];
kit5 = {"11", "00000", "100101", "10010001"};
kit6 = Join[kit5, {"101001", "1010100001", "1010001001", "10010000101", "1001000010001"}];
all[b_] := Tuples[{0, 1}, b]; img[b_] := Union @@ (succ /@ all[b]);
{i5, i6} = {img[5], img[6]};
{Length[i5], Length[i6], SubsetQ[i5, Union @@ (succ /@ i5)], SubsetQ[i6, Union @@ (succ /@ i6)],
 AllTrue[kit5, reads[i5, digits[#]] === {} &] && AllTrue[kit6, reads[i6, digits[#]] === {} &],
 reads[i6, digits["101010000"]] === {}, minimal[i5], minimal[i6],
 Select[kit5, reads[all[5], digits[#]] === {} &], Select[kit6, reads[all[6], digits[#]] === {} &]}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30Jen`.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30Jen"};
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
rule30Submission["Rule30Submission.free_bit_constraints6"]["KernelCheck"]
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
