#!/usr/bin/env python3
"""assemble_free_middle_essay.py (Local, 10 November 2026; S-13): essay.md for the free-middle theorem: front matter,
the prose with the computation at the end of section 5, the formal section with the portal form embedded verbatim.
Adapted from assemble_gate_trap_lift_essay.py (S-16).
Run: python3 tests/probes/wolfram/assemble_free_middle_essay.py FOLDER"""
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
heads = ['no_local_ranking_late', 'wsum_rho', 'cyclic_conserved_of_rho', 'free_middle', 'free_middle_coboundary',
         'rank_local', 'no_additive_ranking_late', 'lower_bound_needed']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. In rule 30's zero-boundary left half, a rank made of any function of width and boundary windows plus an integer additive density, bounded below linearly and nonincreasing on rows that survive to within a growing margin of their width, has a conserved density; so no such rank terminates the late survivors. The lower bound is necessary.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, period two, zero-boundary left half, Q01, ranking function, barrier, conservation law, additive density, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[lhallee/rule30-open](https://github.com/lhallee/rule30-open)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[rule30-open: Rule 30 has no additive conservation law](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/negative-results/structure/conservation-laws.md)"]
---

'''
compute = '''

```wl
cstep[x_] := MapThread[BitXor[#1, BitOr[#2, #3]] &, {RotateRight[x], x, RotateLeft[x]}];
rise[x_, h_, m_] := With[{y = Nest[cstep, x, 4]}, Total[h /@ Partition[y, m, 1, 1]] - Total[h /@ Partition[x, m, 1, 1]]];
stats[n_, h_, m_] := With[{r = rise[#, h, m] & /@ Tuples[{0, 1}, n]}, {Total[r], Max[r], Count[r, _?Positive], Count[r, _?Negative]}];
pop[w_] := First[w];
c11[w_] := Boole[w === {1, 1}];
words = Tuples[{0, 1}, 9];
maxRise = Max[rise[Reverse[#], pop, 1] & /@ words];
best = Last[Select[words, rise[Reverse[#], pop, 1] == maxRise &]];
row[D_, mu_, d_] := With[{n = Length[d], q = (mu + 2) Length[d]}, Join[{0}, Table[Which[k <= D, Mod[k, 2], k <= D + q, d[[Mod[k, n] + 1]], True, 1], {k, D + q + 1}]]];
zstep[s_] := With[{t = Join[s, {0, 0}]}, Join[{0}, Table[BitXor[t[[k + 2]], BitOr[t[[k + 1]], t[[k]]]], {k, 1, Length[t] - 2}]]];
changes = Table[With[{s = row[12, mu, best]}, Total[Rest[Nest[zstep, s, 4]]] - Total[Rest[s]]], {mu, 0, 6}];
{stats[9, pop, 1], stats[10, c11, 2], best, maxRise, changes}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30ZeroBoundaryBarriers` and `Rule30LocalConservation`.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30ZeroBoundaryBarriers", "Ruliology.CellularAutomata.Rule30ZeroBoundary", "Ruliology.CellularAutomata.Rule30LocalConservation"};
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
rule30Submission["Rule30Submission.lower_bound_needed"]["KernelCheck"]
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
