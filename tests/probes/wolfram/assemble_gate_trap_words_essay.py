#!/usr/bin/env python3
"""assemble_gate_trap_words_essay.py (Local, 9 November 2026): essay.md for the gate-trap gap words: front matter, the
prose with the computation at the end of section 6, the formal section with the portal form embedded verbatim.
Adapted from assemble_period_three_language_essay.py (S-14).
Run: python3 tests/probes/wolfram/assemble_gate_trap_words_essay.py FOLDER"""
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
heads = ['not_reads_of_check', 'no_3353_of_entry', 'gap_words_of_entry', 'no_33535555_of_entry', 'no_late_33',
         'minimal_paths', 'Q01GapWords_of_Q01Gap', 'not_finSupp_Psi_of_Q01GapWords', 'CQ01Empty_of_Q01GapWords']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-09
Description: Core Lean. After a right half enters the kit's gate trap, column 1 never reads the gap words 333, 3353, 3533, 3553 or 5533, and from the third black cell on no two consecutive gaps are 3. These are the minimal forbidden words of the relaxed trap graph; completeness is computed separately. Assuming the open Q01GapWords gives CQ01 for trapped right halves and CQ01Empty.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, period two, gate trap, gap words, right half, CQ01, Q01Gap, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[lhallee/rule30-open](https://github.com/lhallee/rule30-open)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261027-230bc7: a closed trap for the right half driven from the empty row](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-230bc7)"]
---

'''
compute = '''

```wl
trapSource = Import[FileNameJoin[{Environment["RULE30PRIZE_KIT"], "lean", "Ruliology", "CellularAutomata", "Rule30Certificates", "GateTrap.lean"}], "Text"];
trap = ToExpression /@ StringCases[First[StringCases[trapSource, "def trapCodes : List Nat := [" ~~ Shortest[c__] ~~ "]" :> c]], DigitCharacter ..];
inTrap = AssociationThread[trap -> True];
step[s_, c_, x_] := With[{e = BitOr[s, BitShiftLeft[x, 16]]}, BitAnd[BitXor[BitOr[BitShiftLeft[e, 1], c], BitOr[e, BitShiftRight[e, 1]]], 65535]];
succ[s_] := Union[step[step[s, 0, #1], 1, #2] & @@@ Tuples[{0, 1}, 2]];
closed = Count[Flatten[Table[step[step[w, 0, a], 1, b], {w, trap}, {a, 0, 1}, {b, 0, 1}]], v_ /; KeyExistsQ[inTrap, v]];
bits[g_] := Join[{1}, Flatten[Append[ConstantArray[0, # - 1], 1] & /@ g]];
sizes[w_] := Module[{S = Select[trap, BitAnd[#, 1] == First[w] &], out}, out = {Length[S]}; Do[S = Select[Union[Flatten[succ /@ S]], BitAnd[#, 1] == y &]; AppendTo[out, Length[S]], {y, Rest[w]}]; out];
gap[S_, g_] := Module[{T = S}, Do[T = Select[Union[Flatten[succ /@ T]], BitAnd[#, 1] == Boole[k == g] &], {k, g}]; T];
allowed = <|{} -> Select[trap, OddQ]|>; forbidden = {};
Do[Do[With[{T = gap[allowed[w], g]}, If[T === {}, AppendTo[forbidden, Append[w, g]], allowed[Append[w, g]] = T]], {w, Select[Keys[allowed], Length[#] == n - 1 &]}, {g, {3, 5}}], {n, 8}];
words = {{3, 3, 3}, {3, 3, 5, 3}, {3, 5, 3, 3}, {3, 5, 5, 3}, {5, 5, 3, 3}};
{Length[trap], closed, sizes[bits[#]] & /@ words, SortBy[Select[forbidden, KeyExistsQ[allowed, Rest[#]] &], {Length, Identity}], Length[DeleteDuplicates[Sort /@ Values[allowed]]]}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30GateTrap`, and through it the trap's data and kernel checks, the driven right half and the zero-boundary left half.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30GateTrap", "Ruliology.CellularAutomata.Rule30StripCertificates", "Ruliology.CellularAutomata.Rule30ZeroBoundary", "Ruliology.CellularAutomata.Rule30PeriodTwoSideways"};
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
rule30Submission["Rule30Submission.CQ01Empty_of_Q01GapWords"]["KernelCheck"]
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
