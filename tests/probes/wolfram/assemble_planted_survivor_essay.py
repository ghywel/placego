#!/usr/bin/env python3
"""assemble_planted_survivor_essay.py (Local, 10 November 2026; S-08 plant): essay.md for the planted survivor: front
matter, the prose with the computation at the end of section 5, the formal section with the portal form embedded verbatim.
Adapted from assemble_radius_two_clock_essay.py (S-07).
Run: python3 tests/probes/wolfram/assemble_planted_survivor_essay.py FOLDER"""
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
heads = ['psi_psiInv', 'psiInv_psi', 'psi_stripe', 'psiInv_fin', 'Tn_eq', 'T_finite', 'T_zero', 'T_fixed',
         'fixed_survives', 'survival_table']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. A tree automorphism conjugates rule 30's zero-boundary step into a map with an immortal finite row. Its exact survival counts differ by a zero-or-one term with width and time guards, and can match arbitrarily large finite portions of the original table.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, period two, Q01, zero-boundary left half, survival count, conjugacy, tree automorphism, barrier, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

'''
compute = '''

```wl
f30[y_] := BitXor[BitShiftRight[y, 1], BitOr[y, BitShiftLeft[y, 1]]];
psi[l_, x_, nb_] := Module[{out = 0, agree = True, b}, Do[b = BitGet[x, i]; out = BitOr[out, BitShiftLeft[BitXor[b, Boole[agree && EvenQ[i] && i >= 2 l]], i]]; agree = agree && b == Boole[EvenQ[i]], {i, 0, nb - 1}]; out];
psiInv[l_, y_, nb_] := Module[{x = 0, agree = True, b}, Do[b = BitXor[BitGet[y, i], Boole[agree && EvenQ[i] && i >= 2 l]]; x = BitOr[x, BitShiftLeft[b, i]]; agree = agree && b == Boole[EvenQ[i]], {i, 0, nb + 2}]; If[agree, None, x]];
survZ[z_, t_] := If[z === None, True, Module[{w = z, ok = True}, Do[If[EvenQ[s] && BitGet[w, 0] == 0, ok = False; Break[]]; w = f30[w], {s, 0, t}]; ok]];
survTdirect[l_, y0_, t_] := Module[{y = y0, u = (4^l - 1)/3, ok = True, z}, Do[If[EvenQ[s] && BitGet[y, 0] == 0, ok = False; Break[]]; If[y =!= u, z = psiInv[l, y, BitLength[y] + 2]; y = psi[l, f30[z], BitLength[z] + 4]], {s, 0, t}]; ok];
cases = Flatten[Table[With[{cT = Count[Table[survZ[psiInv[l, y, w], t], {y, 0, 2^w - 1}], True], cF = Count[Table[survZ[y, t], {y, 0, 2^w - 1}], True]}, cT == cF + Boole[2 l - 1 <= w && 2 Ceiling[w/2] <= t]], {l, 1, 3}, {w, 0, 10}, {t, 0, 14}]];
diffs = Table[Count[Table[survZ[psiInv[2, y, w], 8], {y, 0, 2^w - 1}], True] - Count[Table[survZ[y, 8], {y, 0, 2^w - 1}], True], {w, 0, 10}];
direct = And @@ Flatten[Table[survTdirect[l, y, 12] === survZ[psiInv[l, y, 8], 12], {l, 1, 3}, {y, 0, 2^8 - 1}]];
stripe40 = Total[2^Range[0, 38, 2]];
fixed = And @@ Table[Mod[psi[l, f30[stripe40], 40], 2^30] == (4^l - 1)/3, {l, 1, 3}];
{And @@ cases, Length[cases], diffs, direct, fixed}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30ZeroBoundaryBarriers`.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30ZeroBoundary", "Ruliology.CellularAutomata.Rule30ZeroBoundaryBarriers"};
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
rule30Submission["Rule30Submission.survival_table"]["KernelCheck"]
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
