#!/usr/bin/env python3
"""assemble_ether_cut_edge_essay.py (Local, 10 November 2026; S-11): essay.md for the cut ether: front matter, the
prose with the computation at the end of section 5, the formal section with the portal form embedded verbatim.
Adapted from assemble_not_absorption_essay.py (S-05).
Run: python3 tests/probes/wolfram/assemble_ether_cut_edge_essay.py FOLDER"""
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
heads = ['cycle9', 'cycle13', 'off9_closed', 'cut_code_prefix', 'c7cut_depth', 'c7cut_frozen', 'c7cut_off_seed',
         'c7cut_not_seed_row', 'seed_no_flush_ether', 'seed_flush_ether_sharp', 'seed_offset_ether_204']
assert (d / 'headlines.txt').read_text().split() == ['Rule30Submission.' + h for h in heads]
wl = '{' + ', '.join('"' + h + '"' for h in heads) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-10
Description: Core Lean. The kit's cut ether c7cut N has edge-code depth 8 with phase 16 for every N, never agrees on nine edge bits with any phase of the single cell, and so is never a translate of a single-cell row; conversely no single-cell row shows thirteen ether cells flush with its rightmost black cell, and twelve is sharp.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, edge code, frozen ruler, ether, c7cut, single cell, 2-adic edge map, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[lhallee/rule30-open](https://github.com/lhallee/rule30-open)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[rule30-open: SeedPastPeriods](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/Rule30Open/Frames/SeedPastPeriods.lean)"]
---

'''
compute = '''

```wl
tm[c_, nb_] := Mod[BitXor[c, BitOr[BitShiftLeft[c, 1], BitShiftLeft[c, 2]]], 2^nb];
cycle[nb_] := Most[NestWhileList[tm[#, nb] &, 1, # != 1 &, {2, 1}]];
c9 = cycle[9]; c13 = cycle[13];
step[row_Association] := With[{ps = Union[Flatten[{# - 1, #, # + 1} & /@ Keys[row]]], g = Lookup[row, #, 0] &}, Association[(# -> 1) & /@ Select[ps, BitXor[g[# - 1], BitOr[g[#], g[# + 1]]] == 1 &]]];
c7[p_] := Boole[Mod[p + 1, 7] == 0];
cut[n_] := Association[(# -> 1) & /@ Select[Range[-(7 n + 1), 7 n + 6], c7[#] == 1 &]];
code[row_, e_, n_] := Sum[Lookup[row, e - k, 0] 2^k, {k, 0, n - 1}];
prefixes = Table[code[cut[n], 7 n + 6, 9], {n, 0, 5}];
seeds = NestList[step, <|0 -> 1|>, 320];
frozen = And @@ Flatten[Table[With[{rows = NestList[step, cut[n], 32]}, Table[With[{a = code[rows[[t + 1]], 7 n + 6 + t, 9], b = code[seeds[[17 + t]], 16 + t, 9]}, Mod[a, 256] == Mod[b, 256] && BitGet[a, 8] != BitGet[b, 8]], {t, 0, 32}]], {n, 0, 2}]];
ether = NestList[Function[r, Table[BitXor[r[[Mod[p - 1, 7] + 1]], BitOr[r[[p + 1]], r[[Mod[p + 1, 7] + 1]]]], {p, 0, 6}]], Table[c7[p], {p, 0, 6}], 3];
flush = Table[With[{cs = Table[Lookup[seeds[[s + 1]], s - j, 0], {j, 0, 12}]}, Max[Table[LengthWhile[Range[0, 12], cs[[# + 1]] == ether[[a + 1, Mod[p - #, 7] + 1]] &], {a, 0, 3}, {p, 0, 6}]]], {s, 0, 300}];
row204 = And @@ Table[Lookup[seeds[[205]], 204 - 7 - j, 0] == ether[[3, Mod[1 - j, 7] + 1]], {j, 0, 12}];
{Length[c9], MemberQ[c9, 129], Length[c13], prefixes, frozen, Max[flush], First[FirstPosition[flush, Max[flush]]] - 1, row204}
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30FrozenRuler` and `Rule30ZeroBoundaryBarriers`.

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
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30FrozenRuler", "Ruliology.CellularAutomata.Rule30ZeroBoundaryBarriers", "Ruliology.CellularAutomata.Rule30Realization", "Ruliology.CellularAutomata.Rule30Jen"};
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
rule30Submission["Rule30Submission.seed_offset_ether_204"]["KernelCheck"]
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
