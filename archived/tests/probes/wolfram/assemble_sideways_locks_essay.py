#!/usr/bin/env python3
"""assemble_sideways_locks_essay.py (Local, Block 8): essay.md for the lock instances of CQ01: front matter, the prose with the computation at the end
of section 5, the formal section with the portal form embedded verbatim. Run: python3 tests/probes/wolfram/assemble_sideways_locks_essay.py FOLDER"""
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
heads = ['winW_dstep', 'lock_forever', 'u_of_lock', 'u_eventuallyPeriodic_of_lock', 'not_finSupp_Psi_of_lock', 'winW_prefix', 'lock5_ok', 'lock7_ok', 'lock7b_ok', 'lock5_entry', 'lock7_entry', 'lock7b_entry', 'CQ01_lock5_family', 'CQ01_lock7_family', 'CQ01_lock7b_family', 'lock5_win_trap', 'u_28998']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-08
Description: Core Lean. Three closed locks of the right half driven by the alternating column, of widths 34, 30 and 45 and column words 10000, 0101000 and 0010100, are checked by the kernel; every right half that enters one satisfies CQ01, among them the families sharing the first 49, 57 or 74 cells of 28998, 1891 and 3793493. The period-five lock lies inside the gate trap. Nothing here decides CQ01.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, period two, CQ01, sideways row, driven right half, closed lock, gate trap, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[lhallee/rule30-open](https://github.com/lhallee/rule30-open)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261027-230bc7: the gate trap and Q01Gap](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-230bc7)", "[R30-20261024-8d7751: two families absorbed by the ether](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261024-8d7751)"]
---

'''
compute = '''

```wl
st[e_, c_] := BitXor[BitOr[BitShiftLeft[e], c], BitOr[e, BitShiftRight[e]]];
cells[w_, W_] := Table[BitAnd[st[st[BitOr[w, BitShiftLeft[e, W]], 0], 1], 2^W - 1], {e, 0, 3}];
free[w_, W_] := Flatten[Table[BitAnd[st[BitOr[BitAnd[st[BitOr[w, BitShiftLeft[a, W]], 0], 2^W - 1], BitShiftLeft[b, W]], 1], 2^W - 1], {a, 0, 1}, {b, 0, 1}]];
lk5 = {{547958887, 2695442535, 6990409831, 11285377127, 15580344423}, {2594196878, 6889164174, 11184131470, 15479098766}, {714676060, 5009643356, 9304610652, 13599577948}, {706780010, 2854263658, 5001747306, 9296714602, 11444198250, 15739165546}, {689582056, 2837065704, 4984549352, 7132033000, 11427000296, 15721967592}};
lk7 = {{46898496, 181116224, 315333952, 583769408, 717987136, 852204864, 986422592}, {59587889, 193805617, 328023345, 462241073, 596458801, 730676529, 999111985}, {122973256, 223636552, 257190984, 391408712, 492072008, 760507464, 794061896, 1028942920, 1062497352}, {55753223, 223525383, 357743111, 458406407, 525515271, 592624135, 760396295, 793950727, 861059591, 894614023, 995277319, 1028831751, 1062386183}, {54712734, 88267166, 222484894, 356702622, 524474782, 591583646, 625138078, 759355806, 792910238, 860019102, 893573534, 1027791262, 1061345694}, {54260276, 87814708, 222032436, 356250164, 591131188, 624685620, 758903348, 859566644, 893121076, 1027338804}, {75243858, 209461586, 343679314, 612114770, 746332498, 880550226, 1014767954}};
lk7b = {{1372794518866, 5770841029970, 14566934052178, 23363027074386, 32159120096594}, {4817275456832, 13613368479040, 22409461501248, 31205554523456}, {2878366659889, 11674459682097, 20470552704305, 29266645726513}, {2427647947848, 11223740970056, 20019833992264, 28815927014472}, {1462412784135, 10258505806343, 19054598828551, 27850691850759}, {1455023374750, 5853069885854, 10251116396958, 19047209419166, 23445255930270, 32241348952478}, {1390110553652, 5788157064756, 10186203575860, 14584250086964, 23380343109172, 32176436131380}};
entry[r_, W_, set_] := Module[{d = r, t = 0}, While[! (OddQ[t] && MemberQ[set, BitAnd[d, 2^W - 1]]), d = st[d, If[EvenQ[t], 1, 0]]; t++]; t];
report[c_, W_, r_] := Module[{p = Length[c], set = Flatten[c]},
  {Length[set], p, StringJoin[ToString[BitAnd[First[#], 1]] & /@ c],
   Count[Flatten[Table[MemberQ[c[[Mod[k, p] + 1]], #] & /@ cells[w, W], {k, p}, {w, c[[k]]}]], False],
   Count[Flatten[Table[MemberQ[set, #] & /@ free[w, W], {w, set}]], False],
   entry[r, W, set]}];
{report[lk5, 34, 28998], report[lk7, 30, 1891], report[lk7b, 45, 3793493]}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30GateTrap`: the gate trap, its window machinery and `evolve`, and through it the driven right half and the sideways row.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30PeriodTwoSideways", "Ruliology.CellularAutomata.Rule30Ether", "Ruliology.CellularAutomata.Rule30StripCertificates"};
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
rule30Submission["Rule30Submission.CQ01_lock5_family"]["KernelCheck"]
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
