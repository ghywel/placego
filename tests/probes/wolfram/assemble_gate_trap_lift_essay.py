#!/usr/bin/env python3
"""assemble_gate_trap_lift_essay.py (Local, 9 November 2026; S-16): essay.md for the gate trap at eighteen columns:
front matter, the prose with the computation at the end of section 5, the formal section with the portal form embedded
verbatim. Adapted from assemble_gate_trap_words_essay.py (S-15).
Run: python3 tests/probes/wolfram/assemble_gate_trap_lift_essay.py FOLDER"""
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
heads = ['not_reads18_of_check', 'no_3535353_of_entry', 'trap_reads_3535353', 'lift_minimal_paths',
         'Q01GapCore_of_Q01GapWords', 'not_finSupp_Psi_of_Q01GapCore', 'CQ01Empty_of_Q01GapCore']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-09
Description: Core Lean. The kit's gate trap, lifted by two columns, never shows the gap word 3535353 after entry, for every right half that enters; the sixteen-column graph does read it. So Q01GapWords weakens to Q01GapCore, which still gives CQ01 for trapped right halves and CQ01Empty. Open.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, period two, gate trap, gap words, lift, right half, CQ01, Q01Gap, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[lhallee/rule30-open](https://github.com/lhallee/rule30-open)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261109-897fd1: the gate trap forbids five gap words](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261109-897fd1)", "[R30-20261030-60990f: an all-time forbidden return-gap pattern](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261030-60990f)"]
---

'''
compute = '''

```wl
trapSource = Import[FileNameJoin[{Environment["RULE30PRIZE_KIT"], "lean", "Ruliology", "CellularAutomata", "Rule30Certificates", "GateTrap.lean"}], "Text"];
trap = ToExpression /@ StringCases[First[StringCases[trapSource, "def trapCodes : List Nat := [" ~~ Shortest[c__] ~~ "]" :> c]], DigitCharacter ..];
lift = Flatten[Table[BitOr[t, BitShiftLeft[h, 16]], {t, trap}, {h, 0, 3}]];
inLift = AssociationThread[lift -> True];
step[s_, c_, x_, w_] := With[{e = BitOr[s, BitShiftLeft[x, w]]}, BitAnd[BitXor[BitOr[BitShiftLeft[e, 1], c], BitOr[e, BitShiftRight[e, 1]]], 2^w - 1]];
succ[s_, w_] := Union[step[step[s, 0, #1, w], 1, #2, w] & @@@ Tuples[{0, 1}, 2]];
closed = Count[Flatten[Table[step[step[x, 0, a, 18], 1, b, 18], {x, lift}, {a, 0, 1}, {b, 0, 1}]], v_ /; KeyExistsQ[inLift, v]];
bits[g_] := Join[{1}, Flatten[Append[ConstantArray[0, # - 1], 1] & /@ g]];
sizes[start_, w_, word_] := Module[{S = Select[start, BitAnd[#, 1] == First[word] &], out}, out = {Length[S]}; Do[S = Select[Union[Flatten[succ[#, w] & /@ S]], BitAnd[#, 1] == y &]; AppendTo[out, Length[S]], {y, Rest[word]}]; out];
gap[S_, g_, w_] := Module[{T = S}, Do[T = Select[Union[Flatten[succ[#, w] & /@ T]], BitAnd[#, 1] == Boole[k == g] &], {k, g}]; T];
minimal[start_, w_, nmax_] := Module[{allowed = <|{} -> Select[start, OddQ]|>, forbidden = {}}, Do[Do[With[{T = gap[allowed[u], g, w]}, If[T === {}, AppendTo[forbidden, Append[u, g]], allowed[Append[u, g]] = T]], {u, Select[Keys[allowed], Length[#] == n - 1 &]}, {g, {3, 5}}], {n, nmax}]; SortBy[Select[forbidden, KeyExistsQ[allowed, Rest[#]] &], {Length, Identity}]];
word = bits[{3, 5, 3, 5, 3, 5, 3}];
{Length[lift], closed, sizes[trap, 16, word], sizes[lift, 18, word], minimal[trap, 16, 8], minimal[lift, 18, 8]}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30GateTrap`. Because the verifier's kit predates `Rule30GateTrapWords`, the module first repeats that module's reviewed source verbatim, then adds the eighteen-column lift.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30GateTrap", "Ruliology.CellularAutomata.Rule30StripCertificates", "Ruliology.CellularAutomata.Rule30ZeroBoundary", "Ruliology.CellularAutomata.Rule30PeriodTwoSideways", "Ruliology.CellularAutomata.Rule30Ether"};
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
rule30Submission["Rule30Submission.CQ01Empty_of_Q01GapCore"]["KernelCheck"]
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
