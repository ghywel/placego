#!/usr/bin/env python3
"""assemble_horizon_submission.py (Local, L1176): byte-preserving single-file assembly of the finite-horizon package,
the transformation of GPT's assemble_arc_submission.py (GC2105) applied to the 23 modules release-checked in stages A, B
and C (L1169, L1174, L1175). Each component's top imports and header docstrings are removed, its `#print axioms`
commands are removed, and its complete body from `namespace` onward is kept byte for byte, inside `namespace
Rule30Submission`; external imports are deduplicated; the same 99 heads are printed with the `Rule30Submission.`
prefix. `--check` verifies the committed result without writing. The new single-file context is unvalidated until its
own frozen compile and the official checker.

L1179: one import is added, `Ruliology.CellularAutomata.Rule30Prize`. The kit's Check.lean fails any module whose
environment lacks that statement module, and no component reaches it (the arc package got it from its
ArcRule30ExclusionDraft component). It imports only Rule30Jen, already in the closure. No proof body changes."""
from pathlib import Path
import hashlib, json, re, sys

root = Path(__file__).resolve().parents[3]
subs = root / 'reports/wolfram-agents/submissions'
folder = subs / 'finite-horizon'
# Dependency order of stages A, B and C, with the digests their wrappers pinned.
components = [
    ('arc-codes', 'ArcBreakBounds', 'cbb2f4ba2a384a9b9cb077f4b5c9242339237864bc47af70f0afddaf5b78f1a6'),
    ('arc-codes', 'ArcBreakSequence', '7d6f45508ce456e11cefa1e305580f8d1195f26e5cd1375e9cd9e96dd53ffdfe'),
    ('arc-codes', 'ArcDeterminantDraft', 'aa2402bddf84deac9c38f3383fb55b57e6f088a1453b02dd465b128d99fa083a'),
    ('arc-codes', 'ArcContinuantsDraft', '7c32512f60fb003c598d86d31474109e700edac3991528b1e3522cba4ea79fab'),
    ('arc-codes', 'ArcCoverDraft', '58268dd3a9e52652fe904d390c51b2354b6eae90bde99fd06e12c4e60958d5f4'),
    ('arc-codes', 'ArcStepCodeDraft', 'b207135e62cb7e8dde7f4e79ecb1f20f6825001efdae997536ce60dc0f6dafe5'),
    ('arc-codes', 'ArcRotationDraft', '4acd4c0eda5777a2365424601b627a1f2ef86fe9b8c51a185fa658364d78aef9'),
    ('finite-horizon', 'SharpAdjacentReturn', '17679e3755d6d8b9fedf8f0f14d6e6dbade1f3367b6e0a10d257a00e998bdfb1'),
    ('finite-horizon', 'MechanicalCarry', 'b0b83cd83df4fbf1aeb04bf680708a47ed8d8ea9e6c44f0b77d9c366e6481253'),
    ('finite-horizon', 'FiniteHorizonBounds', 'ceafe8f929b8a5d62ab2e8a0ea3b7ac7eb9cd3c589018e7f24191d12a8ffd7c9'),
    ('finite-horizon', 'CarryReturnSpacing', '3445f7f25ce765ffdbf29040e45f964b98978bab17d3b1c47595ff2f17445c40'),
    ('finite-horizon', 'ActualContinuants', '4367bc2b3b1fa68c7cbf516f0a000a1033f92eb3389d7bdf195e271d5bb87836'),
    ('finite-horizon', 'ActualCarrySpacing', 'a514f7a025c7ea1f284882958db353832b4a0576fd6c7ad61ada327c50f2f878'),
    ('finite-horizon', 'DenominatorBootstrap', 'c9c8cbe4b3eb9b46cb7f87e32c26668c6a4245bd82a1a7d5a2ef6e2c4d4ae729'),
    ('finite-horizon', 'FiniteHorizonSelection', '87e28fe781a06684e24db3d0707c74e96579248e7948383681083b64e523f88a'),
    ('finite-horizon', 'ContinuantSequence', '430d45dbd2cfe47ec9740a047f544f0d1887f897ca46c1dd85ec5076f9d3afbb'),
    ('finite-horizon', 'OppositeArcStrip', '3151c0511b5aac522279e1d6f6be8b825715b1837d890da86aa9d0df769b6d93'),
    ('finite-horizon', 'OppositeCarryArcs', '7f47629a93f59263274399abd1785d9e9dbe9f842b0fc2789fc16d48c4eb8e7f'),
    ('finite-horizon', 'ActualOppositeCarry', '0c02e7ae932cffe44e5d160a329243b026b29cc8771e7d4934395aa6cf58ec25'),
    ('finite-horizon', 'UniformHorizon', '1331e5cf924cd3186e75a749b096e9fe3f622bb6bcef2a1256a9b71808c8b351'),
    ('finite-horizon', 'RecodedHorizon', 'ab75fa0fa094e39cd4dc91215ceb4647c1d62fa95ae4fababb15084866d99cf1'),
    ('arc-codes', 'ArcRule30BridgeDraft', '4f644cc44e1365dd7b9292a64dbd14a5984ed2758506a3cab072dcb15f63d6b1'),
    ('finite-horizon', 'PhysicalHorizon', '79fe5a747cba2673bf1f896f31824c48826c4c30554d7dc3c3b650bc4bf24e7b'),
]
local = {name for _, name, _ in components}
imports, parts, heads = [], [], []
for where, name, digest in components:
    data = (subs / where / (name + '.lean')).read_bytes()
    assert hashlib.sha256(data).hexdigest() == digest, name
    s = data.decode()
    n = s.index('\nnamespace ') + 1
    prefix = s[:n]
    for imp in re.findall(r'^import (\S+)\s*$', prefix, re.M):
        if imp not in local and imp not in imports:
            imports.append(imp)
    rest = re.sub(r'^import \S+\s*$', '', prefix, flags=re.M)
    rest = re.sub(r'/-!.*?-/', '', rest, flags=re.S)
    assert not rest.strip(), (name, rest)
    body = s[n:].strip()
    heads += ['Rule30Submission.' + x for x in re.findall(r'^#print axioms (\S+)\s*$', body, re.M)]
    body = re.sub(r'^#print axioms \S+\s*\n', '', body, flags=re.M)
    parts.append('/- Component: ' + name + '; proof body retained from the release-checked integration. -/\n' + body)
assert len(heads) == 99 and len(set(heads)) == 99, len(heads)
# The official statement module, which Check.lean requires in the environment (L1179).
statements = 'Ruliology.CellularAutomata.Rule30Prize'
assert statements not in imports
imports.append(statements)
header = '''/-!
# An explicit finite horizon for mechanical words, and matching pieces beside a Rule 30 clock

Classical Sturmian repetition theory already gives the qualitative obstruction: every Sturmian word repeats a long
factor early, uniformly over slope and phase. This file formalizes a uniform EXPLICIT finite witness, keeps its loss
under arbitrary finite block maps, and transfers it to matching pieces beside a Rule 30 period-two clock.

* `UniformHorizon.uniform_horizon`: for every irrational slope `α`, every phase `θ` and every `C`, the mechanical word
  `⌊θ+(s+1)α⌋ − ⌊θ+sα⌋` has a repetition of positive lag `q` on `[a, b]` with `b+q ≤ 251*(C+4)` and `b > 2a+q+C`.
* `RecodedHorizon.uniform_horizon_all` and `recoded_horizon`: the same for every real slope, and for every recoding of
  width `w+1` (any block map, any codomain) through `251*(C+4)+250*w`.
* `PhysicalHorizon.piece_bound`, `reset_step`, `first_disagreement`, `disagreement_step`: for a configuration white left
  of `-L` whose column `0` is a clock from time `0`, any stretch `[a, b]` of the visible column `evol x (2s) 1` agreeing
  with a recoded mechanical word has `b − a < 251*(L+2a+4)+250*w`; consecutive reset times satisfy
  `t' ≤ 503t+251L+1004+250w`, and disagreements with one fixed recoded word satisfy `k_0 ≤ 251(L+4)+250w` and
  `k' ≤ 503k+251L+1507+250w`.

The constants are explicit, not claimed sharp. The continued-fraction and repetition background is credited: the
best-approximation step is classical, Bugeaud–Kim (Trans. AMS 371, 2019) and Bugeaud–Laurent (AIF 73, 2023) contain
finite and qualitative repetition estimates, and the width transfer is an elementary block argument. The additional
content is the checked quantitative bound and its physical endpoint accounting. These are conditional statements about
a genuine clock; they do not construct one, and give no density, entropy, realizability or prize conclusion. The arc
components are those of the delivered arc package; the physical repeat bound is its `ArcRule30Bridge.repeat_bound`.
-/
'''
s = ('\n'.join('import ' + x for x in imports) + '\n\n' + header + '\nnamespace Rule30Submission\n\n' +
     '\n\n'.join(parts) + '\n\n' + '\n'.join('#print axioms ' + x for x in heads) + '\n\nend Rule30Submission\n')
assert not any(re.search(r'^import ' + re.escape(x) + r'\s*$', s, re.M) for x in local)
assert not re.search(r'\b(?:sorry|admit|native_decide|bv_decide|skipKernelTC)\b', s)
source_path = folder / 'Rule30Submission.lean'
check = '--check' in sys.argv
if check:
    assert source_path.read_text() == s, 'assembled source differs'
else:
    source_path.write_text(s)
headlines = ['Rule30Submission.' + x for x in [
    'UniformHorizon.uniform_horizon', 'UniformHorizon.uniform_horizon_witness', 'RecodedHorizon.uniform_horizon_all',
    'RecodedHorizon.recoded_horizon', 'PhysicalHorizon.piece_bound', 'PhysicalHorizon.reset_step',
    'PhysicalHorizon.first_disagreement', 'PhysicalHorizon.disagreement_step']]
assert all(h in heads for h in headlines)
manifest = {'source_sha256': hashlib.sha256(s.encode()).hexdigest(), 'source_bytes': len(s.encode()),
            'components': {name: digest for _, name, digest in components}, 'public_imports': imports,
            'printed_heads': heads, 'proposed_headlines': headlines,
            'transformation': 'Remove top component imports, header docstrings and axiom-print commands; keep each '
            'complete body from `namespace` onward exactly; deduplicate external imports and add the official '
            'statement module Ruliology.CellularAutomata.Rule30Prize, which Check.lean requires; wrap in '
            'Rule30Submission; print the same 99 names with the prefix. The new single-file context is unvalidated '
            'until its own frozen compile and the official checker.'}
manifest_text = json.dumps(manifest, indent=2) + '\n'
if check:
    assert (folder / 'assembly.json').read_text() == manifest_text, 'assembly manifest differs'
else:
    (folder / 'assembly.json').write_text(manifest_text)
print(manifest['source_sha256'], manifest['source_bytes'])
print('\n'.join(imports))

# The essay binding (L1180), as in the arc assembler: the reviewed prose (GC2173's correction, with L1187's
# IncludeInternal repair) with the source embedded once as a Wolfram Language string, and its draft sentence removed.
# The abstract file must equal the front matter's. This writes only essay.md; the source and manifest are unchanged.
prose_data = (folder / 'essay-prose.md').read_bytes()
assert hashlib.sha256(prose_data).hexdigest() == \
    '060de9b8c435cce923735f9c2ce81b0451592fd0e2dda6366f3ee7b9518d91ef', 'essay prose differs from the reviewed one'
prose = prose_data.decode()
assert prose.count('%%LEAN%%') == 1
abstract = re.search(r'^Abstract: (.*)$', prose, re.M).group(1)
assert (folder / 'abstract.txt').read_text() == abstract + '\n', 'abstract.txt differs from the front matter'
draft = ' This essay is currently a preparation draft, not a report that these cells ran.'
assert prose.count(draft) == 1
essay = prose.replace(draft, '').replace('%%LEAN%%', json.dumps(s, ensure_ascii=False)[1:-1])
if check:
    assert (folder / 'essay.md').read_text() == essay, 'essay source binding differs'
else:
    (folder / 'essay.md').write_text(essay)
print('essay', hashlib.sha256(essay.encode()).hexdigest(), len(essay.encode()))
