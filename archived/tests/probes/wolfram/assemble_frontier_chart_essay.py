#!/usr/bin/env python3
"""assemble_frontier_chart_essay.py (Local, Block 7): essay.md for S-01: front matter, the prose with the computation at the end
of section 5, the formal section with the portal form embedded verbatim. Run: python3 tests/probes/wolfram/assemble_frontier_chart_essay.py FOLDER"""
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
heads = ['mortality_of_Q01', 'mortality_iff_Q01', 'budget_iff_Q01', 'Z_rec', 'chart_interior', 'chart_wall', 'zrow_chart', 'inX_start', 'finSupp_start']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-06
Description: Core Lean. An immortal frontier gives a finitely supported start of the zero-boundary left half with column -1 black at every even step, so Q01 implies mortality. With the kit's arrows, Q01, mortality and repeat budgets at every length are equivalent. Nothing here proves any of them.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, Q01, mortality, frontier, repeat budget, zero-boundary left half, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)", "S. Wolfram, Random sequence generation by cellular automata, Advances in Applied Mathematics 7 (1986) 123-169"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261102-b8e784: unifying the two frontier modules](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261102-b8e784)"]
---

'''
compute = '''

```wl
scan[w_] := Module[{u = 0, v = 0, al = 0, out}, out = Table[v = BitXor[v, BitOr[al, s[[2]]]]; u = BitXor[u, BitOr[v, s[[1]]]]; al = s[[1]]; {u, v}, {s, w}]; {out, u, v}];
update[w_] := With[{r = scan[w]}, If[r[[2]] == r[[3]], {Append[r[[1]], {1, 1 - r[[3]]}], r[[3]]}, None]];
run[w_] := Module[{fr = {w}, tape = {}, z}, While[Length[tape] < 400 && (z = update[Last[fr]]) =!= None, AppendTo[fr, z[[1]]]; AppendTo[tape, z[[2]]]]; {fr, tape}];
at[fr_, n_, e_] := With[{w = fr[[n + 1]]}, If[e < Length[w], w[[-1 - e]], {0, 0}]];
chart[fr_, t_, e_] := If[EvenQ[t + e], at[fr, (t + e)/2, e][[1]], at[fr, (t + e + 1)/2, e][[2]]];
interior[fr_] := With[{n = Length[fr] - 1}, Flatten[Table[If[Floor[(t + e + 3)/2] + 1 > n, Nothing, chart[fr, t + 1, e + 1] == BitXor[chart[fr, t, e + 2], BitOr[chart[fr, t, e + 1], chart[fr, t, e]]]], {t, 0, 2 n - 1}, {e, 0, 2 n + 1}]]];
wall[fr_] := With[{n = Length[fr] - 1}, Table[chart[fr, t + 1, 0] == BitXor[chart[fr, t, 1], chart[fr, t, 0]], {t, 1, 2 n - 4}]];
symbols = Tuples[{0, 1}, 2];
legal = Flatten[Table[Prepend[tail, {1, b}], {r, 1, 7}, {tail, Tuples[symbols, r - 1]}, {b, 0, 1}], 2];
runs = run /@ legal;
long = Select[runs, Length[#[[2]]] >= 3 &];
inner = Flatten[interior[#[[1]]] & /@ long];
edge = Flatten[wall[#[[1]]] & /@ long];
{fr, tape} = run[{{1, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 1}}];
row = Total[Table[chart[fr, 2, e] 2^e, {e, 0, 2 Length[First[fr]] + 1}]];
F[y_] := BitXor[BitShiftRight[y], BitOr[y, BitShiftLeft[y]]];
firstWhite = 2 LengthWhile[NestList[F[F[#]] &, row, 30], OddQ];
{Length[legal], Length[inner], Count[inner, False], Length[edge], Count[edge, False], Max[Length[#[[2]]] & /@ runs], tape, row, BitLength[row], firstWhite}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30AlternatingTraceBridge` and `Rule30ZeroBoundary`, which hold the frontier, the update and `Q01`.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30SurvivalBridge", "Ruliology.CellularAutomata.Rule30ZeroBoundary"};
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
rule30Submission["Rule30Submission.mortality_iff_Q01"]["KernelCheck"]
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
