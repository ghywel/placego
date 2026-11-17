#!/usr/bin/env python3
"""assemble_synthesis_essay.py (Local, L1478; adapted from assemble_episode_bridge_essay.py): essay.md for the synthesis entry.
essay.md = Cloud's essay-prose.md with the packaging repairs below, a computation cell at the end of section 7, the formal
section with the checked left-coincidence portal form embedded verbatim, Cloud's entries-by-object.md as section 8, then the
Sources. Cloud's files are not edited; every repair is an exact replacement that must match once.
Run: python3 tests/probes/wolfram/assemble_synthesis_essay.py SYNTHESIS_FOLDER PORTAL_FORM
"""
import hashlib, sys
from pathlib import Path
d = Path(sys.argv[1]); src_path = Path(sys.argv[2])
prose = (d / 'essay-prose.md').read_bytes(); appx = (d / 'entries-by-object.md').read_bytes()
abstract = (d / 'abstract.txt').read_bytes(); src = src_path.read_bytes()
pins = {'essay-prose.md': ('0ec2c035dc58a83aee324b77806438d67a9f96ba2aaf778f486f5322b342f0ee', prose),
        'entries-by-object.md': ('0933fc20a628066d45a765ab17245adac71de3f6de4224f4c341a7e78c3be8ec', appx),
        'abstract.txt': ('dbfc2f54a0a20015f6230894d52d6b633215b7d4eee2d548d25929b5b862a29a', abstract),
        'Rule30Submission.lean': ('62b661a95baa2dce6be9121d75d4449d302ca92179687154937375831fdeeeb1', src)}
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
# 1. Front matter: final date, the abstract field, sources and links in the portal's link format.
p = once(p, 'Date: DRAFT 2026-11-03 16:11 GMT, revised 2026-11-03 18:52 GMT (GC2585 applied)\n', 'Date: 2026-11-03\n',
         'front matter: date')
p = once(p, 'Abstract: see abstract.txt (draft, CL703)\n', 'Abstract: See abstract.txt.\n', 'front matter: abstract field')
p = once(p, 'Sources: [the kit; the portal; the research record; Rowland 2006; Jen 1986]\n',
         'Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", '
         '"[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)", '
         '"[Rowland, Local nested structure in rule 30](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf)", '
         '"[Jen, Global properties of cellular automata](https://doi.org/10.1007/BF01010579)"]\n'
         'Links: ["[Rule 30 Prizes](https://rule30prize.org/)", '
         '"[The kit\'s Rule30LeftReset](https://github.com/WolframInstitute/Rule30PrizeKit/blob/c42f6e5133f61a47e99289fd4b6e0536fd8a0453/lean/Ruliology/CellularAutomata/Rule30LeftReset.lean)"]\n',
         'front matter: sources and links')
# 2. The internal draft-status paragraph (GC2593: strip internal draft text).
i = p.index('*Status: DRAFT by Cloud'); j = p.index('goes out.*\n\n', i) + len('goes out.*\n\n')
assert p.count('*Status: DRAFT') == 1
p = p[:i] + p[j:]
print('applied: removed the draft-status paragraph (%d characters)' % (j - i))
# 3. Section 2: the citation map is now the appendix.
p = once(p, 'the citation map beside this draft has one line\nper entry.',
         'the appendix (section 8) places every entry of\nthe portal, one line each.', 'section 2: the appendix pointer')
# 4. Section 2F: GPT's narrowing of the 4b2a58 sentence (GC2593), verbatim in content.
p = once(p, 'and no observable smaller than a sixteen-cell window certifies the word 1001 with a bounded potential\n'
            '(AIOvernight, 4b2a58).',
         'an eight-cycle obstruction rules out nonzero nonnegative rewards on proper subsets of the four-cell 1001\n'
         'window in a rational 16-cell potential inequality, and a separate return of the seed\'s 16-cell state excludes an exact\n'
         'coboundary for that indicator (AIOvernight, 4b2a58).', 'section 2F: the 4b2a58 sentence (GC2593)')
# 5. Section 7: the anchor as built and read (L1474, L1476; GC2583, GC2587), Lemma E in the module.
p = once(p, 'Built by Local (L1474) as `Rule30LeftCoincidence` on the kit\'s `Rule30LeftReset`: 142 lines of core Lean with standard axioms;\n'
            'the kit\'s Check and the portal Check pass; GPT\'s source read is pending.',
         'Built in our record (L1474, L1476) as `Rule30LeftCoincidence` on the kit\'s `Rule30LeftReset`: 180 lines of core Lean with\n'
         'standard axioms and ten headline theorems; the kit\'s Check and the portal Check pass (37 constants), and GPT read the\n'
         'actual source (GC2583, GC2587). The portal form and its checks follow this section.', 'section 7: build and read status')
p = once(p, '(`D_closed_form`, `D_farther_of_child`, `D_coincidence_iff`, through the kit\'s `D_step`',
         '(`D_closed_form`, `D_farther_of_child`, `D_coincidence_iff`, `D_white_of_coincidence`,\n'
         '  `D_evwhite_iff_eventually_eq`, through the kit\'s `D_step`', 'section 7: the D headlines')
p = once(p, 'parents with a black force a white child (one step of the recurrence, x(t + 1) = ¬b(t) ∧ x(t), to be added to the module);\n'
            '  so the criterion decides which farther diagonal makes the next one white: one farther diagonal for each nearer one.\n',
         'parents force a white child from the next black of the nearer diagonal on (`D_white_of_coincidence`); so the criterion\n'
         '  decides which farther diagonal makes the next one white: one farther diagonal for each nearer one.\n'
         '- **Lemma E** (`white_of_coincidence`, `evwhite_iff_eventually_eq`): if a = b from s on and b(s1) is black for some\n'
         '  s1 ≥ s, then x is white from s1 + 1 on (once a = b the recurrence is x(t + 1) = ¬b(t) ∧ x(t)). So, when the nearer word\n'
         '  has blacks arbitrarily late (as a periodic word with a black does), the child is eventually white if and only if its\n'
         '  parents eventually coincide; the forward direction is the kit\'s `white_forces_eq`.\n',
         'section 7: Lemma E in the module')
p = once(p, 'PROVED two-party by hand (GC2550, GC2565) and in core Lean (L1474; GPT\'s read pending).',
         'PROVED two-party by hand (GC2550, GC2565) and in core Lean (L1474, L1476; GPT\'s source reads GC2583, GC2587).',
         'section 7: statuses')
p = once(p, 'while the unique forward child and the coincidence criterion need the black.',
         'while the unique forward child and the coincidence criterion need the black; Lemma E\'s white child needs a black of the\n'
         'nearer word at or after the onset of coincidence, and its equivalence needs blacks arbitrarily late.',
         'section 7: the Lemma E guards')

compute = '''

**A computation.** The first white diagonals of the single-cell pattern, read on the last 1,024 of 4,096 ticks, and the two
facts the module connects there: a white diagonal D w has coinciding parents D(w − 2) = D(w − 1) (the kit's `D_white_of_eq`),
and that coincidence, after a black of D(w − 2), is equivalent to D(w − 3) being the difference of D(w − 2)
(`D_coincidence_iff`). This is a finite window, an illustration: it does not show that these diagonals stay white.

```wl
T = 4096; L = 1024; ca = CellularAutomaton[30, {{1}, 0}, T];
diag[j_] := diag[j] = Table[ca[[t + 1, T + 1 + j - t]], {t, 0, T}];
win[v_] := Take[v, {T - L + 1, T}];
diff[v_] := BitXor[Most[v], Rest[v]];
white = Select[Range[0, 47], Max[win[diag[#]]] == 0 &]
```

```wl
Grid[Prepend[Table[{w, win[diag[w - 2]] == win[diag[w - 1]],
     If[w >= 3, win[diag[w - 3]] == win[diff[diag[w - 2]]], "(no D(w - 3))"], Max[win[diag[w - 2]]] == 1}, {w, white}],
  {"white D w", "D(w - 2) = D(w - 1)", "D(w - 3) = difference of D(w - 2)", "D(w - 2) has a black"}], Frame -> All]
```
'''

formal = '''

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30LeftReset`, whose
recurrence, reset step and accumulation it builds on, with `Rule30Diagonals.D_step` for the left diagonals, at the verifier's
kit commit 93d98bbe.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"''' + s + '''", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

F1 to F3, as Lean prints them, for any triple and on the left diagonals:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30LeftReset", "Ruliology.CellularAutomata.Rule30Diagonals"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = {"closed_form", "farther_of_child", "solutions_agree", "coincidence_iff", "D_closed_form", "D_coincidence_iff",
   "white_of_coincidence", "evwhite_iff_eventually_eq", "D_white_of_coincidence", "D_evwhite_iff_eventually_eq"};
show[Take[heads, 6], "TypeForm"]
```

Lemma E, both ways:

```wl
show[Take[heads, -4], "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it
resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.coincidence_iff"]["KernelCheck"]
```
'''

a = appx.decode()
a = once(a, '# Appendix: every portal entry placed by object (generated 2026-11-03 18:53 GMT; Cloud)\n',
         '## 8. Appendix: every portal entry placed by object\n', 'appendix: heading')
a = once(a, 'author is the first name as the portal shows it;',
         'author is the first listed author as the portal shows it, "ours" as in section 2;', 'appendix: author column (GC2593)')
a = once(a, 'The placement is Cloud\'s reading\nof each title and abstract,',
         'The placement is a reading\nof each title and abstract by Cloud, the record\'s Claude (Anthropic) worker,', 'appendix: Cloud glossed')
heads_a = [ln for ln in a.split('\n') if ln.startswith('## ') and not ln.startswith('## 8.')]
assert len(heads_a) == 7, heads_a
a = '\n'.join(('#' + ln) if (ln.startswith('## ') and not ln.startswith('## 8.')) else ln for ln in a.split('\n'))
print('applied: appendix object headings demoted to ### (%d)' % len(heads_a))

k = p.index('\n## Sources\n')
body, sources = p[:k].rstrip('\n'), p[k:].strip('\n')
out = body + compute + formal + '\n' + a.rstrip('\n') + '\n\n' + sources + '\n'
for bad in ('DRAFT', 'Not for posting', 'to be added to the module', 'pending.', "read pending", '142 lines'):
    assert bad not in out, bad
(d / 'essay.md').write_text(out)
print('essay.md written: %d bytes, sha256 %s' % (len(out.encode()), hashlib.sha256(out.encode()).hexdigest()))
