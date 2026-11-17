#!/usr/bin/env python3
"""assemble_first_check_degree_essay.py (Local, 10 November 2026; S-06): essay.md for the degree of the first check:
front matter, the prose with the computation at the end of section 5, the formal section with the portal form embedded
verbatim. Adapted from assemble_planted_survivor_essay.py (S-08).
Run: python3 tests/probes/wolfram/assemble_first_check_degree_essay.py FOLDER"""
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
heads = ['diag', 'top_succ', 'top_coefficient', 'omit_coefficient', 'anf_expansion', 'check_degree', 'ones_parity',
         'first_check_parity', 'walsh_mod_four', 'walsh_one', 'other_phase_odd']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. For every n the first check of the zero-boundary left half has top ANF coefficient n mod 2 and degree n or n - 1, so its weight and the number of first-check survivors are congruent to n mod 2; in the other clock phase the weight is always odd. Nothing about the single seed.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, period two, zero-boundary left half, first check, algebraic normal form, degree, parity, Moebius transform, Walsh sum, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

'''
compute = '''

```wl
recCell[col_, k_] := Module[{prev = ConstantArray[0, Length[col] + 1], cur = col, nxt}, Do[nxt = Table[BitXor[cur[[t + 2]], BitOr[cur[[t + 1]], prev[[t + 1]]]], {t, 0, Length[cur] - 2}]; prev = cur; cur = nxt, {k - 1}]; First[cur]];
bit[w_, s_] := If[s < Length[w], w[[s + 1]], 0];
check[n_, w_] := recCell[Table[If[EvenQ[t], 1, bit[w, Quotient[t, 2]]], {t, 0, 2 n}], 2 n + 1];
other[n_, w_] := recCell[Table[If[EvenQ[t], bit[w, Quotient[t, 2]], 1], {t, 0, 2 n - 1}], 2 n];
cube[n_] := Tuples[{0, 1}, n];
ones = Association[Table[n -> Total[check[n, #] & /@ cube[n]], {n, 1, 12}]];
kit = AllTrue[Range[12], Mod[ones[#], 2] == Mod[#, 2] &];
omit = AllTrue[Range[2, 12], Function[n, Mod[Total[If[#[[2]] == 0, check[n, #], 0] & /@ cube[n]], 2] == Mod[n + 1, 2]]];
degree[n_] := Module[{tt = ConstantArray[0, 2^n]}, Do[tt[[FromDigits[Reverse[w], 2] + 1]] = check[n, w], {w, cube[n]}]; Do[If[BitGet[x, i] == 1, tt[[x + 1]] = BitXor[tt[[x + 1]], tt[[x - 2^i + 1]]]], {i, 0, n - 1}, {x, 0, 2^n - 1}]; Max[DigitCount[#, 2, 1] & /@ (Flatten[Position[tt, 1]] - 1)]];
step[row_] := With[{r = Join[{0}, row, {0, 0}]}, Table[BitXor[r[[i + 2]], BitOr[r[[i + 1]], r[[i]]]], {i, 1, Length[row] + 1}]];
surv[n_] := Count[cube[2 n], row_ /; Module[{cur = row, ok = True}, Do[If[EvenQ[t] && cur[[1]] == 0, ok = False; Break[]]; cur = step[cur], {t, 0, 2 n}]; ok]];
odd = AllTrue[Range[12], Function[n, OddQ[Total[other[n, #] & /@ cube[n]]]]];
{kit, omit, degree /@ Range[10], surv /@ Range[6], Table[Mod[2^n - 2 ones[n], 4], {n, 1, 12}], odd}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30ZeroBoundary`. The verifier's kit predates the kit module `Rule30FirstChecks`, so the source carries a byte copy of that module's body in the namespace `Rule30Submission.Rule30FirstChecks`.

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
opens = {"Rule30Submission", "Rule30Submission.Rule30FirstChecks", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30ZeroBoundary"};
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
rule30Submission["Rule30Submission.check_degree"]["KernelCheck"]
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
