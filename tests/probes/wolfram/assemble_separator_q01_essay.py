#!/usr/bin/env python3
"""assemble_separator_q01_essay.py (Local, Block 7): essay.md for S-04: front matter, the prose with the computation at the end
of section 5, the formal section with the portal form embedded verbatim. Run: python3 tests/probes/wolfram/assemble_separator_q01_essay.py FOLDER"""
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
heads = ['cone_chart', 'peel_chart', 'hardCore_endOf_iff', 'sep_iff_QN', 'orbitSeparator_iff_QN', 'Q01_sep', 'Q01_iff_sep_and', 'sep_Q01Gap', 'sep_CQ01Empty', 'sep_iff_LR1', 'layerWord_realizes', 'sep_CQ01', 'bwh_iff_deathBounds', 'bwh_death', 'bwh_Q01', 'odd_guard_needed', 'even_threshold_needed']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-08
Description: Core Lean. The constant-tail separator SEP is Q01 restricted to free bits with no two adjacent whites, and Q01 is SEP plus the free bits that meet two adjacent whites infinitely often; SEP implies Q01Gap and is a width-one-layer statement; BWH is equivalent to exact-width death bounds and gives D(W) ≤ 2W + 4. Nothing here proves SEP, BWH or Q01.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, Q01, zero-boundary left half, constant-tail separator, binary wedge hypothesis, death time, Q01Gap, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[lhallee/rule30-open, WedgeLadderQ01](https://github.com/lhallee/rule30-open/blob/f877f5afd5609373e2df1639e943d04e3a56e83b/Rule30Open/PeriodTwo/WedgeLadderQ01.lean)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261027-230bc7: the gate trap and Q01Gap](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-230bc7)", "[R30-20261102-f48894: BWH implies the separator](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261102-f48894)", "[R30-20261106-45f6e9: Q01, mortality and repeat budgets](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-45f6e9)"]
---

'''
compute = '''

```wl
F[y_] := BitXor[BitShiftRight[y], BitOr[y, BitShiftLeft[y]]];
death[y0_] := Module[{y = y0, t = 0}, While[OddQ[y], y = F[F[y]]; t += 2]; t];
phi[a_, b_] := Which[a == 0, {0, 1, 3, 2}[[b + 1]], a == 2, {3, 2, 0, 1}[[b + 1]], True, {3, 2, 1, 0}[[b + 1]]];
rows = NestList[F, 11083, 80];
zrow[t_, k_] := If[k == 0, 0, BitGet[rows[[t + 1]], k - 1]];
zpair[t_, k_] := 2 zrow[t, k] + zrow[t, k + 1];
end[j_] := zpair[2 j + 1, 1];
cone[0, j_] := 3 - end[j];
cone[1, j_] := phi[end[j], 3 - end[j + 1]];
cone[t_, j_] := cone[t, j] = phi[cone[t - 2, j + 1], cone[t - 1, j + 1]];
peel[0, t_] := cone[t, 0];
peel[d_, t_] := peel[d, t] = phi[peel[d - 1, t], peel[d - 1, t + 1]];
pairs = Flatten[Table[{d, t}, {d, 0, 15}, {t, 0, 15 - d}], 1];
layerWord[x0_, r_, k_] := Module[{c = x0, w = {}},
  Do[c = BitXor[Boole[EvenQ[t]], BitOr[c, BitGet[r, t]]]; If[EvenQ[t], AppendTo[w, c]], {t, 0, 2 k - 1}]; w];
layerCount[k_] := Length[Union[Flatten[Table[layerWord[x0, r, k], {x0, 0, 1}, {r, 0, 2^(2 k) - 1}], 1]]];
{death[272125], death[11083], Length[pairs], AllTrue[pairs, peel[#[[1]], #[[2]]] == zpair[#[[2]], 2 #[[1]] + #[[2]] + 2] &], layerCount /@ Range[6]}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30SEPToPeriodTwo` (the streams, the separators and `encodePair`), `Rule30GateTrap` (`Q01Gap`) and `Rule30ZeroBoundarySmall` (the bound at width `16`).

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30WedgeBridge", "Ruliology.CellularAutomata.Rule30SeparatorBridge", "Ruliology.CellularAutomata.Rule30ZeroBoundary"};
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
rule30Submission["Rule30Submission.bwh_Q01"]["KernelCheck"]
```
'''
i = body.index('\n## 7. ')
out = front + body[:i].rstrip('\n') + compute + body[i:].rstrip('\n') + formal
for bad in ('DRAFT', 'Not for posting', 'See abstract'):
    assert bad not in out, bad
(d / 'essay.md').write_text(out)
h = hashlib.sha256((d / 'essay.md').read_bytes()).hexdigest()
(d / 'essay.sha256').write_text(h + '\n')
for name in ('essay-prose.md', 'title.txt', 'abstract.txt', 'Rule30Submission.lean', 'essay.md'):
    print(name, hashlib.sha256((d / name).read_bytes()).hexdigest())
print('abstract words', len(abstract.split()), 'headlines', len(heads))
