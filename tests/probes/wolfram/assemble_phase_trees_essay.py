#!/usr/bin/env python3
"""assemble_phase_trees_essay.py (Local, L1493, L1496; adapted from assemble_synthesis_essay.py): essay.md and abstract-final.txt for A6.
essay.md = Cloud's essay-prose.md with the repairs below (GC2610's scope corrections, CL710's provenance corrected from the
sources, the computation section), then the formal section with the checked portal form embedded verbatim. Cloud's files are
not edited; every repair is an exact replacement that must match once.
Run: python3 tests/probes/wolfram/assemble_phase_trees_essay.py FOLDER
"""
import hashlib, sys
from pathlib import Path
d = Path(sys.argv[1])
prose = (d / 'essay-prose.md').read_bytes(); abstract = (d / 'abstract.txt').read_bytes(); src = (d / 'Rule30Submission.lean').read_bytes()
pins = {'essay-prose.md': ('77d90307fd4017bb21018f2404469e987ea883e4af6a8fb665559be15c93d6c7', prose),
        'abstract.txt': ('455508236c23da94cd22df2d9fb8fb146cd3fe8ec2dbf9e3decdbecfba589e26', abstract),
        'Rule30Submission.lean': ('1e7e7c51a58e684140a4c48c1d962d8bcd259021ed78793b6c91671794b3c977', src)}
for name, (want, data) in pins.items():
    got = hashlib.sha256(data).hexdigest()
    if got != want:
        raise SystemExit('REFUSED: %s digest %s, pinned %s' % (name, got, want))
s = src.decode()
assert '"' not in s and '\\' not in s, 'the source must embed as a plain string literal'


def once(text, old, new, why):
    n = text.count(old)
    if n != 1:
        raise SystemExit('REFUSED: %s matches %d times (%s)' % (old[:60], n, why))
    print('applied: %s' % why)
    return text.replace(old, new)


p = prose.decode()
p = once(p, "Date: DRAFT 2026-11-03 (Cloud's packaging draft; Local assembles)\n", 'Date: 2026-11-03\n', 'front matter: date')
p = once(p, 'the longest episode at a chosen depth is 22, 24 and 24 ticks at every alignment,',
         'every episode at a chosen depth has at most 22, 24 and 24 ticks, at every alignment,', 'description: upper bound (GC2610)')
p = once(p, "The rings\nare the record's: G16 from a SAT census of single-column phases at $N = 128$, P1024 from the eternal-cycle line, the 480-phase\nfrom the classification at period 32.\n",
         "The rings\nare the record's. G16 is a cyclic component of the exhaustive light-speed analysis at period 16, one cycle of 128 states\n(L1294). P1024 was found as a cycle of the forward register $y_n = y_{n-21} \\oplus (y_{n-1} \\lor y_{n-2})$, and is the phase that\nrefuted our cycle lemma (L1308). The 480-phase is the first non-rain cycle reached by a sampled search at period 32 (L1304).\n",
         'the three phases: provenance from the sources (CL710)')
p = once(p, '`MFinite (g16 i) 14` with longest episode 22.', '`MFinite (g16 i) 14`: every episode has at most 22 ticks.', 'theorems: G16 (GC2610)')
p = once(p, '`MFinite (p1024 i) 8` with longest episode 24.', '`MFinite (p1024 i) 8`: every episode has at most 24 ticks.', 'theorems: P1024 (GC2610)')
p = once(p, '`MFinite (p480 r s) 10` with longest episode 24.', '`MFinite (p480 r s) 10`: every episode has at most 24 ticks.', 'theorems: the 480-phase (GC2610)')
p = once(p, "- Each phase's longest episode at the certified depth equals the record's computed table (G16: 22 at depth 14; P1024: 24 at\n  depth 8; the 480-phase: 24 at depth 10), and the tables agree at every smaller depth with the record's exhaustive runs.\n",
         "- The certified bound equals the computed maximum over all representatives, which is a computation and not a Lean statement\n  (G16: 22 at depth 14; P1024: 24 at depth 8; the 480-phase: 24 at depth 10). The trees' deepest layers also equal the record's\n  exhaustive tables at every smaller depth.\n",
         'controls: computed maxima separated from the theorems (GC2610)')
p = once(p, "**`Rule30EtherGrounding`** (Troy Lowry) its eventual exclusion. Nothing comparable existed for any other phase.\n",
         "**`Rule30EtherGrounding`** (Troy Lowry) its eventual exclusion. A search of the kit, the portal and the open kit pull requests\n  (index of 3 November, 20:56Z) found episode bounds for no other phase.\n",
         'related work: search scoped (GC2610)')
p = once(p, "and the\n  top-word tree as a reusable certificate whose size grows with the depth, about 1.48-fold per depth step on these three\n  phases, and with the number of alignments, not with the phase's period.\n",
         "and the\n  top-word tree as a reusable certificate. At these depths it avoids scanning the temporal horizon. Its size per representative\n  grew about 1.48-fold per depth step on G16 for depths 8 to 14, and was nearly equal across the three phases at depth 8: a finite\n  measurement, not a bound.\n",
         'new here: the growth as a measurement (GC2610)')
comp = '''The size of each tree, summed over its representatives. The candidate tests count every extension tried, including those of the
final empty layer. These counts are computed, by `phase_tree_size.py` in our record; the empty layers are the kernel's.

| phase | depth | representatives | retained nodes | candidate tests | first empty layer |
|---|---:|---:|---:|---:|---:|
| G16 | 14 | 128 | 45,866 | 83,342 | 23 |
| P1024 | 8 | 1,024 | 37,144 | 70,786 | 25 |
| the 480-phase | 10 | 960 | 76,560 | 140,032 | 25 |

One representative replayed here: the layer sizes of G16's representative 41 at depth 14, the one class that keeps a word
through layer 22. This reproduces the certificate's computation, and is shown as an illustration.

```wl
ring = 16^^468b2e4a3c095cc178d9b5d3f6c43ea7;
y[n_] := BitGet[ring, Mod[n, 128]];
phase[i_][j_, t_] := y[j + i + 56 t];
wd[k_, t_] := Min[2 t, k + 1];
edgeStep[c_] := BitXor[c, BitOr[BitShiftLeft[c, 1], BitShiftLeft[c, 2]]];
pass[i_, k_, t_, w_] := With[{c = Nest[edgeStep, BitOr[BitShiftLeft[w, k + 2 - wd[k, t + 1]], 1], t]},
   BitGet[c, k] == phase[i][k, t] && BitGet[c, k + 1] == phase[i][k + 1, t]];
layers[i_, k_, n_] := FoldList[Function[{s, t}, With[{d = wd[k, t + 1] - wd[k, t]},
     Select[Flatten[Table[BitOr[BitShiftLeft[w, d], e], {w, s}, {e, 0, 2^d - 1}]], pass[i, k, t, #] &]]], {0}, Range[0, n - 1]];
Length /@ layers[41, 14, 23]
```
'''
p = once(p, "[Local: the table of the three trees from `phase_tree_size.py`: phase, depth, representatives, retained nodes, candidate tests,\ndeepest layer; and the replay of one representative's layers.]\n",
         comp, 'the computation section (CL710)')

a = abstract.decode()
a = once(a, 'The longest episode at depths 14 and 15 of the period-16 phase G16, a 128-cell ring with lag 72, is 22 ticks; at depths 8 and 9 of the period-1024 phase P1024 it is 24; at depths 10 and 11 of the period-32 phase on a 480-cell ring it is 24; each at every alignment.',
         'Every episode at depths 14 and 15 of the period-16 phase G16, a 128-cell ring with lag 72, has at most 22 ticks; at depths 8 and 9 of the period-1024 phase P1024, at most 24; at depths 10 and 11 of the period-32 phase on a 480-cell ring, at most 24; each at every alignment.',
         'abstract: upper bounds (GC2610)')
a = once(a, "Controls: each longest episode reproduces the record's computed table, and shortening the tree by one tick fails at a known maximizer.",
         "Controls: each bound equals the record's computed maximum, and shortening the tree by one tick fails at a known maximizer.",
         'abstract: controls (GC2610)')
words = len(a.split()); assert words <= 250, words
(d / 'abstract-final.txt').write_text(a)
p = once(p, 'Abstract: See abstract.txt.\n', 'Abstract: ' + a.strip() + '\n', 'front matter: the cleared abstract in place of the placeholder (GC2615)')
print('abstract-final.txt: %d words, sha256 %s' % (words, hashlib.sha256(a.encode()).hexdigest()))

formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30FrozenRuler` at the verifier's
kit commit 93d98bbe, and restates the three definitions of our R30-20261103-d37d24 verbatim. In order: the edge map on bit words
and the backward cone; the tree and its soundness, generic in the depth and the phase; then for each phase its literals, the
frame relation and `IsPhase`, the alignment shift and the kernel checks in chunks.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"''' + s + '''", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headline theorems, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30FrozenRuler"};
heads = {"g16_mfinite", "p1024_mfinite", "p480_mfinite", "no_tail_of_mfinite", "g16_phase", "p1024_phase", "p480_phase"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it
resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.g16_mfinite"]["KernelCheck"]
```
'''
out = p.rstrip('\n') + formal
for bad in ('DRAFT', '[Local:', 'longest episode 2', 'Nothing comparable'):
    assert bad not in out, bad
(d / 'essay.md').write_text(out)
print('essay.md written: %d bytes, sha256 %s' % (len(out.encode()), hashlib.sha256(out.encode()).hexdigest()))
