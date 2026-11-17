#!/usr/bin/env python3
"""assemble_right_wall_essay.py (Local, L1548): essay.md for the wall entry: front matter, the prose with the computation after section 7's text, the formal sections at the end,
the portal form embedded verbatim. Run: python3 tests/probes/wolfram/assemble_right_wall_essay.py FOLDER"""
import hashlib
import re
import sys
from pathlib import Path

d = Path(sys.argv[1])
prose = (d / 'essay-prose.md').read_text()
title = (d / 'title.txt').read_text().strip()
abstract = (d / 'abstract.txt').read_text().strip()
src = (d / 'Rule30Submission.lean').read_text()
assert '"' not in src and '\\' not in src, 'the source must embed as a plain string literal'
lines = prose.split('\n')
assert lines[0] == '# ' + title and lines[2].startswith('Gareth Herbert;'), lines[:3]
body = '\n'.join(lines[3:]).strip('\n')
E = re.search(r'def E : Nat := 0x([0-9a-f]+)', src).group(1)
heads1 = ['predecessor_unique', 'step_rain_tail', 'back_rain_tail', 'front_back', 'front_not_periodic', 'deep_words', 'no_BB', 'no_AAA', 'witness_ABA',
          'Reset.reset', 'Reset.above', 'Reset.again', 'Reset.letters', 'WindowClosed.held_forever', 'WindowClosed.held_not_periodic', 'WindowClosed.letters_closed',
          'WindowClosed.letter_after_B', 'WindowClosed.letter_after_A']
heads2 = ['LockAB.letters', 'LockAB.not_periodic', 'LockAB.witness', 'LockAB.floor', 'LockAAB.letters', 'LockAAB.not_periodic', 'LockAAB.witness', 'LockAAB.floor',
          'LockThird.letters', 'LockThird.not_periodic', 'LockThird.witness', 'LockThird.no_floor', 'Cloud.closed', 'Cloud.cloud_not_lock', 'Cloud.avoids_lock', 'Cloud.not_periodic',
          'Cloud.no_long_alternation', 'Entry.entry']
(d / 'headlines.txt').write_text(' '.join('Rule30Submission.' + h for h in heads1 + heads2) + '\n')
wl = lambda l: '{' + ', '.join('"' + h + '"' for h in l) + '}'
front = f'''---
Template: ComputationalEssay
Name: {title}
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-05
Description: Core Lean. On rows of rule 30 with an alternating left tail, closed sets of windows at the wall force the letter sequences AB and AAB for ever, whatever lies below, and a closed set of 798 windows excludes the first of those locks.
Abstract: {abstract}
Keywords: [rule 30, Rule 30 Prize, right edge, edge map, backward tick, closed windows, reset word, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)", "E. M. Coven, M. Pivato and R. Yassawi, Prevalence of odometers in cellular automata, Proc. AMS 135 (2007)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261027-196370: staircases near the right edge, and the rain rows](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-196370)"]
---

'''
compute = '''

```wl
back[{p1_, p2_}, l_] := Module[{a = p1, b = p2, z}, Table[z = BitXor[c, BitOr[a, b]]; b = a; a = z; z, {c, l}]];
next[w_, p_] := back[p, Join[Most[w], {1, 0, 1, 0, 1, 0, 1}]][[4 ;; 3 + Length[w]]];
bits[s_] := Characters[s] /. {"." -> 0, "#" -> 1};
lockAB = bits /@ {"..##.#...#.#..#..#........##....##..####...##", ".#.#.#...#.#..#..#........##....##..####...##", "..####.#.##.##.########......#.##..#.###...##", ".#.###.#.##.##.########......#.##..#.###...##"};
closed = AllTrue[Tuples[{lockAB, Tuples[{0, 1}, 2]}], MemberQ[lockAB, next @@ #] &];
row0 = 16^^''' + E + ''';
fw[v_] := BitAnd[BitXor[v, BitOr[BitShiftLeft[v, 1], BitShiftLeft[v, 2]]], 2^850 - 1];
rows = NestList[fw, row0, 110];
cells[v_, lo_, n_] := Reverse[IntegerDigits[BitAnd[BitShiftRight[v, lo], 2^n - 1], 2, n]];
letter[w_] := Which[w === bits["..####...##"], "A", w === bits[".#.###...##"], "B", True, "?"];
{closed, StringJoin[Table[letter[cells[rows[[k + 1]], 229 + 3 (110 - k), 11]], {k, 0, 110}]]}
```

```wl
ArrayPlot[Table[Reverse[cells[rows[[k + 1]], 450 - 3 k, 120]], {k, 110, 0, -1}], ImageSize -> 480]
```
'''
formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30FrozenRuler`, which holds the edge map. The row of section 1 is `Row`, one tick is `step`, the kit's `T`, and `iter x t` is the kit's `iter t x`.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"''' + src + '''", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The theorems of sections 2 to 4, as Lean prints them:

```wl
opens = {"Rule30Submission", "Rule30Submission.WindowClosed", "Rule30Submission.Reset", "Rule30Submission.Cloud", "Rule30Submission.Entry", "Ruliology.CellularAutomata.Rule30FrozenRuler"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads1 = ''' + wl(heads1) + ''';
heads2 = ''' + wl(heads2) + ''';
show[heads1, "TypeForm"]
```

The locks, the cloud and the row that enters:

```wl
show[heads2, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, Join[heads1, heads2]]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.Entry.entry"]["KernelCheck"]
```
'''
i = body.index('\n## 8. ')
out = front + body[:i].rstrip('\n') + compute + body[i:].rstrip('\n') + formal
for bad in ('DRAFT', 'Not for posting', 'See abstract'):
    assert bad not in out, bad
(d / 'essay.md').write_text(out)
h = hashlib.sha256((d / 'essay.md').read_bytes()).hexdigest()
(d / 'essay.sha256').write_text(h + '\n')
for name in ('essay-prose.md', 'title.txt', 'abstract.txt', 'Rule30Submission.lean', 'essay.md'):
    print(name, hashlib.sha256((d / name).read_bytes()).hexdigest())
print('abstract words', len(abstract.split()), 'headlines', len(heads1 + heads2))
