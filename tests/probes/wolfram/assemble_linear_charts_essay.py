#!/usr/bin/env python3
"""assemble_linear_charts_essay.py (Local, 11 November 2026; S-24, Cloud's K-10): essay.md for the rigidity of linear
charts of the constrained starts: front matter, the prose with the computation at the end of section 5, the formal
section with the portal form embedded verbatim. Adapted from the S-23 assembler.
Run: python3 tests/probes/wolfram/assemble_linear_charts_essay.py FOLDER"""
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
heads = ['groupLaw_eq_xor', 'fibre_form', 'involution_Q', 'flip_invariant', 'descent_step', 'window_zero', 'q_white', 'kk_Theta', 'fb_Theta', 'Theta_fb', 'kk_two_step', 'fb_shift', 'uld_Theta', 'uld_fb', 'linear_chart_is_free_bit_chart', 'free_bit_chart_affine', 'free_bit_chart_iso', 'free_bit_chart_is_chart']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-11
Description: Core Lean. Every affine chart of the constrained zero-boundary starts on which two steps act affinely is the free-bit chart up to an affine map, through the lemma that shift-equivariant group laws on one-sided bit sequences are xor. Nothing here decides Q01 or period 2.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, zero-boundary left half, free bits, affine chart, one-sided shift, group law, Hedlund, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

'''
compute = '''

```wl
m = 6;
op[q_, w_][x_, y_] := Table[BitXor[x[[n]], y[[n]], q[{Table[x[[Mod[n + i - 1, m] + 1]], {i, w}], Table[y[[Mod[n + i - 1, m] + 1]], {i, w}]}]], {n, m}];
survivesQ[q_, w_] := With[{pts = Tuples[{0, 1}, m]}, AllTrue[Tuples[pts, 2], op[q, w][op[q, w] @@ #, #[[2]]] === #[[1]] &]];
cands[w_, sym_, neu_] := Module[{words = Tuples[{0, 1}, w], zero = ConstantArray[0, w], free = {}},
   Do[If[! (neu && (v === zero || (sym && u === zero))) && ! (sym && MemberQ[free, {v, u}]), AppendTo[free, {u, v}]], {u, words}, {v, words}];
   Table[Module[{tab = Association[Flatten[Table[{u, v} -> 0, {u, words}, {v, words}], 1]]},
     MapThread[(tab[#1] = #2; If[sym, tab[Reverse[#1]] = #2]) &, {free, bits}]; tab], {bits, Tuples[{0, 1}, Length[free]]}]];
count[w_, sym_, neu_] := With[{cs = cands[w, sym, neu]}, {Length[cs], Count[cs, c_ /; survivesQ[c, w]]}];
{count[1, True, True], count[2, True, True], count[1, False, True], count[1, True, False]}
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
rule30Submission["Rule30Submission.free_bit_chart_is_chart"]["KernelCheck"]
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
