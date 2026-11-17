#!/usr/bin/env python3
"""assemble_hybrid_wall_essay.py (Local, 10 November 2026; S-08 hybrid half): essay.md for the immortal rows of the
90/150 hybrid with a white wall: front matter, the prose with the computation at the end of section 5, the formal
section with the portal form embedded verbatim. Adapted from the S-06 assembler.
Run: python3 tests/probes/wolfram/assemble_hybrid_wall_essay.py FOLDER"""
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
heads = ['D_P_P', 'psi_even_time', 'even_time_constant', 'psi_mono', 'iter_H_real', 'col_real', 'colE_even', 'col_inj',
         'colE_inj', 'real_surj', 'real_inj', 'immortal_real_iff', 'real_afam', 'immortal_iff_famRow',
         'immortal_iff_bitFam_anyWall', 'immortal_iff_param', 'immortal_width_six', 'not_immortal_width_one',
         'col_not_eventually_periodic', 'immortal_odd_word_not_eventually_periodic']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. For the linear 90/150 hybrid with a white wall, the rows whose depth-1 cell is black at every even time are classified exactly, counted by a bijection, and have aperiodic columns; the proof is a decimation semiconjugacy D P² = P D. Not rule 30.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, period two, Q01, zero-boundary left half, linear cellular automaton, rule 90, rule 150, hybrid, decimation, survivors, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

'''
compute = '''

```wl
hstep[y_] := Total[Table[BitShiftLeft[BitXor[BitGet[y, i + 1], If[i >= 1, BitGet[y, i - 1], 0], If[EvenQ[i], BitGet[y, i], 0]], i], {i, 0, BitLength[y] + 1}]];
immortalQ[y_] := Module[{z = y, ok = True}, Do[If[EvenQ[t] && BitGet[z, 0] == 0, ok = False; Break[]]; z = hstep[z], {t, 0, 400}]; ok];
imm = Table[Select[Range[0, 2^w - 1], immortalQ], {w, 1, 12}];
bitfamQ[y_, w_] := With[{x = Function[d, If[d >= 1, BitGet[y, d - 1], 0]]}, x[1] == 1 && AllTrue[Range[0, Quotient[w, 4] + 1], x[4 # + 3] == x[4 # + 5] && x[4 # + 2] == BitXor[x[4 # + 1], x[4 # + 3]] &]];
fam = AllTrue[Range[12], Function[w, imm[[w]] === Select[Range[0, 2^w - 1], bitfamQ[#, w] &]]];
dec[q_, r_] := Total[Table[BitShiftLeft[BitGet[q, 2 i + r], i], {i, 0, BitLength[q]}]];
pP[{a_, b_}] := {BitXor[a, b], BitShiftLeft[a, 1]};
dD[{a_, b_}] := {dec[a, 1], BitXor[dec[a, 0], dec[b, 1]]};
semi = AllTrue[Tuples[Range[0, 63], 2], dD[pP[pP[#]]] == pP[dD[#]] &];
{Length /@ imm, imm[[6]], fam, semi}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports only the official statements (`Rule30Prize`); the hybrid and its algebra are defined in the module.

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
rule30Submission["Rule30Submission.immortal_iff_bitFam_anyWall"]["KernelCheck"]
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
