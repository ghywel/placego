#!/usr/bin/env python3
"""assemble_period_three_language_essay.py (Local, S-14): essay.md for the period-three column-1 languages: front matter,
the prose with the computation at the end of section 6, the formal section with the portal form embedded verbatim.
Run: python3 tests/probes/wolfram/assemble_period_three_language_essay.py FOLDER"""
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
heads = ['no_pattern3', 'col1_011', 'free_bits_011', 'col1_001', 'free_bits_001', 'C3r011_of_C3w', 'not_eventually_011_of_C3r',
         'C3g001_of_C3s', 'not_eventually_001_of_C3g', 'no_eventual_period_three_of_C3g']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-08
Description: Core Lean. Beside an eventual 011 center, column 1 of rule 30's right half never reads 00 or 011110; beside 001 its free runs have length 2 to 4 and 2 to 5. So the kit's open left statements C3w w011 and C3s001 weaken to C3r011 and C3g001, which still exclude the tails and, together, period three. Both are open.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, period three, center column, right half, strip certificate, masked Jen, left half, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[lhallee/rule30-open](https://github.com/lhallee/rule30-open)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261104-53931f: forbidden-prefix propagation for the period-two language](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261104-53931f)"]
---

'''
compute = '''

```wl
lang[w_, b_, r_, words_] := Module[{n = 2^b, nxt, g, comps, big, in, steps, occ},
  nxt[v_, x_] := With[{ph = Quotient[v, n], e = BitOr[Mod[v, n], BitShiftLeft[x, b]]},
    Mod[ph + 1, 3] n + BitAnd[BitXor[BitOr[BitShiftLeft[e], w[[ph + 1]]], BitOr[e, BitShiftRight[e]]], n - 1]];
  g = Graph[Range[0, 3 n - 1], Flatten[Table[DirectedEdge[v, nxt[v, x]], {v, 0, 3 n - 1}, {x, 0, 1}]]];
  comps = Select[ConnectedComponents[g], Length[#] > 1 &];
  big = First[MaximalBy[comps, Length]];
  in = AssociationThread[big -> True];
  steps[v_] := Flatten[Table[With[{v1 = nxt[v, a]}, If[KeyExistsQ[in, v1], Table[With[{v2 = nxt[v1, c]},
      If[KeyExistsQ[in, v2], {nxt[v2, 0], nxt[v2, 1]}, {}]], {c, 0, 1}], {}]], {a, 0, 1}]];
  occ[word_] := Module[{s = Select[big, Quotient[#, n] == r && BitAnd[#, 1] == First[word] &]},
    Do[s = Select[Union[Flatten[steps /@ s]], KeyExistsQ[in, #] && BitAnd[#, 1] == y &], {y, Rest[word]}]; s =!= {}];
  {Sort[Length /@ comps], Length[big], occ /@ words}];
bits[s_] := ToExpression /@ Characters[s];
{lang[{0, 1, 1}, 7, 0, bits /@ {"00", "011110", "111010", "0101010", "0101110", "01011010", "11101110", "111011010", "11", "0110111"}],
 lang[{0, 0, 1}, 10, 1, bits /@ {"010", "101", "11111", "000000", "100111", "111001", "00000111", "01110001", "10011001", "11100000", "11", "0011", "110011"}]}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`), the kit's `Rule30PeriodTwoLanguage` and `Rule30EtherThreeSkeleton`, and through them the bad-class certificates, masked Jen, the period-three skeletons and the left-half reductions.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30EtherThree", "Ruliology.CellularAutomata.Rule30Jen", "Ruliology.CellularAutomata.Rule30StripCertificates", "Ruliology.CellularAutomata.Rule30PeriodFourSkeleton", "Ruliology.CellularAutomata.Rule30DrivenLeft"};
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
rule30Submission["Rule30Submission.no_eventual_period_three_of_C3g"]["KernelCheck"]
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
