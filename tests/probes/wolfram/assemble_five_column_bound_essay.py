#!/usr/bin/env python3
"""S09 essay assembly (GPT GC2812, 10 November 2026), adapted from the reviewed
S08 assembler. Local owns Wolfram execution. Embeds the reviewed portal source
verbatim and keeps the worked certificate cell separate from its Lean proof.
Run: python3 assemble_five_column_bound_essay.py PACKAGE_FOLDER
"""
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
heads = ['potential_bounds','local_potential','telescope','five_column_bound','white_column_bound',
         'evol_five_column_bound','cell_five_column_bound','sharp_rate','sharp_constant']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. Every five adjacent Rule 30 columns contain at most 3T + 2 black cells during any interval of T ticks. A bounded potential gives the exact endpoint telescope and both constants are sharp.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, adjacent columns, black count, potential, telescope, sharp bound, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

'''
compute = r'''

```wl
rule30[a_,b_,c_] := BitXor[a,BitOr[b,c]];
pot[u_] := Max[0,2-Total[Rest[u]]];
damaged[u_] := If[u === ConstantArray[0,5],0,pot[u]];
words = Tuples[{0,1},7];
edges = ({Take[#, {2,6}],rule30 @@@ Partition[#,3,1]} &) /@ words;
slacks = (pot[Last[#]]-pot[First[#]]-Total[First[#]]+3 &) /@ edges;
mirror = (pot[Reverse[Last[#]]]-pot[Reverse[First[#]]]-Total[First[#]]+3 &) /@ edges;
bad = (damaged[Last[#]]-damaged[First[#]]-Total[First[#]]+3 &) /@ edges;
linear = (pot[BitXor @@@ Partition[#,3,1]]-pot[Take[#, {2,6}]]-Total[Take[#, {2,6}]]+3 &) /@ words;
neg[v_] := Count[v,x_ /; x<0];
{And @@ (#>=0 & /@ slacks),Length[slacks],Count[slacks,0],neg[mirror],neg[bad],neg[linear]}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30Realization`.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30Jen", "Ruliology.CellularAutomata.Rule30Realization"};
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
rule30Submission["Rule30Submission.five_column_bound"]["KernelCheck"]
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
