#!/usr/bin/env python3
"""assemble_ternary_waves_essay.py (Local, 10 November 2026; S-22, Cloud's K-04 with K-09a): essay.md for the ternary
travelling-wave codes: front matter, the prose with the computation at the end of section 5, the formal section with
the portal form embedded verbatim. Adapted from the S-19 assembler.
Run: python3 tests/probes/wolfram/assemble_ternary_waves_essay.py FOLDER"""
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
heads = ['tile_certificate12', 'decode12', 'free_ternary_period_twelve', 'ternary_marked_rings_twelve', 'ternary_words_twelve', 'ternary_wave_twelve', 'tile_certificate15', 'decode15', 'free_ternary_period_fifteen', 'ternary_marked_rings_fifteen', 'ternary_words_fifteen', 'ternary_wave_fifteen']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. Three freely joining 34-cell tiles at moving period 12 and three 31-cell tiles at moving period 15 give free ternary codes of rule 30 travelling waves, by one generic kernel-checked development. Nothing is claimed about other periods.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, travelling waves, moving frame, spatial entropy, tiles, ternary code, kernel certificate, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)"]
---

'''
compute = '''

```wl
p12 = {{2868, 3242, 2734, 2769, 1321, 1721, 2469, 1381, 1367, 2772, 3372, 2738, 2986, 1131, 2644, 3674, 2406, 2389, 1493, 1323, 2868, 3242, 2734, 2769, 1321, 1721, 2469, 1381, 1367, 3028, 3116, 2610, 2602, 1323}, {2868, 3242, 2734, 2769, 1321, 1721, 2469, 1381, 1367, 2772, 3372, 2738, 2986, 1131, 2644, 3674, 2406, 2389, 1493, 1327, 2864, 3240, 2728, 2772, 3372, 2738, 2986, 1131, 2644, 3674, 2406, 2389, 1493, 1323}, {2868, 3242, 2734, 2769, 1321, 1721, 2469, 1381, 1367, 3028, 3116, 2610, 2602, 1323, 2868, 3242, 2734, 2769, 1321, 1721, 2469, 1381, 1367, 2772, 3372, 2738, 2986, 1131, 2644, 3674, 2406, 2389, 1493, 1323}};
p15 = {{5461, 23930, 21125, 13126, 10949, 10917, 21927, 10836, 13684, 11082, 11470, 12969, 10921, 27605, 5165, 6707, 22058, 21802, 11581, 21154, 11171, 23122, 26226, 5451, 21834, 24238, 8553, 20889, 12629, 10581, 27050}, {5461, 23930, 21125, 13126, 10949, 10917, 21926, 10837, 30069, 2890, 3277, 2731, 19114, 20310, 10409, 26837, 5293, 7347, 21194, 21162, 11183, 23120, 26216, 21848, 21844, 31412, 17738, 18094, 9577, 26009, 5717}, {5461, 23930, 21125, 13126, 10949, 10917, 21927, 10836, 13684, 11082, 11470, 12969, 10921, 27605, 5165, 6707, 22058, 21802, 11573, 21162, 11183, 23120, 26216, 21848, 21844, 31412, 17738, 18094, 9577, 26009, 5717}};
bit[prof_, a_, r_, t_, per_] := BitGet[prof[[a + 1, r + 1]], Mod[t, per]];
seamsOK[prof_, len_, per_] := Count[Flatten[Table[
     With[{row = Function[{r, t}, If[r < len, bit[prof, a, r, t, per], bit[prof, b, r - len, t, per]]]},
      bit[prof, a, r, t + 1, per] == BitXor[row[r, t], BitOr[row[r + 1, t], row[r + 2, t]]]],
     {a, 0, 2}, {b, 0, 2}, {r, 0, len - 1}, {t, 0, per - 1}]], True];
ringsOK[prof_, len_, per_] := Count[Flatten[Table[
     Module[{x = Flatten[Table[bit[prof, w[[q]], r, 0, per], {q, Length[w]}, {r, 0, len - 1}]], ev},
      ev = CellularAutomaton[30, x, per];
      AllTrue[Range[per - 1], RotateRight[x, #] =!= ev[[# + 1]] &] && RotateRight[x, per] === ev[[per + 1]]],
     {k, 1, 3}, {w, Tuples[{0, 1, 2}, k]}], 1], True];
decoders[prof_, o1_, o2_, per_] := Table[{bit[prof, a, o1, 0, per], bit[prof, a, o2, 0, per]}, {a, 0, 2}];
{seamsOK[p12, 34, 12], seamsOK[p15, 31, 15], ringsOK[p12, 34, 12], ringsOK[p15, 31, 15], decoders[p12, 20, 23, 12], decoders[p15, 6, 23, 15]}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30RingOrbits`.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30RingOrbits"};
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
rule30Submission["Rule30Submission.ternary_wave_fifteen"]["KernelCheck"]
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
