# Three periodic phases behind Rule 30's black edge, excluded to bounded depth (A6) — delivery record

**Status: ASSEMBLED, notebook RESULT OK, not posted (L1493).** The Lean is Local's probe
`tests/probes/lean/PhaseTrees.lean` (L1489, 7e2590f1…; GPT's source-faithfulness PASS GC2604, and GC2600 for the G16 forerunner).
The tree is Cloud's (CL706), its soundness and alignment contract GPT's (GC2596), the builds and the assembly Local's. Cloud's
packaging review is CL710. Posting waits on GPT's packet read and the owner's word.

## Statement

| Headline | Says |
|---|---|
| `g16_mfinite` | every alignment of G16 (128-cell ring, lag 72, period 16): every episode at depth 14 has at most 22 ticks |
| `p1024_mfinite` | every alignment of P1024 (1,024-cell ring, lag 21, period 1,024): every episode at depth 8 has at most 24 ticks |
| `p480_mfinite` | every alignment of the 480-phase (480-cell ring, period 32, two words): every episode at depth 10 has at most 24 ticks |
| `no_tail_of_mfinite` | a finite longest episode at depth k excludes every black-edge code that follows the phase from any depth d ≤ k on |

| `g16_phase`, `p1024_phase`, `p480_phase` | each is a phase, by `decide` of the frame relation on its literals |

Also `cone` (locality), `sound` and `rep_bound` (the tree). The seven rows above are the submission's headlines.

## Package

- [`title.txt`](title.txt); [`abstract-final.txt`](abstract-final.txt) (248 words, a3a6d68a…, from Cloud's `abstract.txt`);
  [`essay.md`](essay.md) (8b380386…), assembled by
  [`assemble_phase_trees_essay.py`](../../../../tests/probes/wolfram/assemble_phase_trees_essay.py) from Cloud's
  [`essay-prose.md`](essay-prose.md) (77d90307…). Cloud's files are not edited.
- **Portal form:** [`Rule30Submission.lean`](Rule30Submission.lean) (1e7e7c51…), from the pinned probe by
  [`phase_trees_portal.py`](../../../../tests/probes/wolfram/phase_trees_portal.py): namespace, the statement import, the
  `#print` lines dropped, the docstring's first lines in public wording. Declarations and proofs are unchanged.
- **Notebook** ([`phase_trees_notebook.wl`](../../../../tests/probes/wolfram/phase_trees_notebook.wl)): nb2, ab978c74…. nb1
  (4b6e1111…) is superseded: its Abstract cell held the placeholder "See abstract.txt." (GC2615).
- **Kit form:** none yet. Cloud's note: a module `Rule30PhaseTrees`, or none; the owner decides after posting. It would need
  A5's module (#116) or a restatement of its definitions, as the portal form does.

## The assembler's repairs

1. Front matter: final date; the description's bound as "at most" (GC2610).
2. The three phases: provenance corrected from the sources (L1492): G16 from the light-speed analysis at period 16 (L1294),
   P1024 from the forward register (L1308), the 480-phase from the sampled search at period 32 (L1304).
3. Theorems: "every episode has at most 22/24/24 ticks" (GC2610).
4. Controls: the computed maxima are separated from the theorems (GC2610).
5. Related work: "nothing comparable existed" replaced by a dated, scoped search (GC2610).
6. New here: the 1.48 growth as a finite measurement on G16 for depths 8 to 14, with no bound claimed (GC2610).
7. The computation section (CL710): the three-tree table, and a cell replaying G16's representative 41.
8. Abstract: the three bounds as "at most", and the controls sentence (GC2610).
9. Seven headlines: the three phase theorems added (CL710).
10. The front matter's Abstract field carries the cleared abstract in place of the placeholder (GC2615).

## Checks

- **Portal Check** on the verifier kit 93d98bbe: **pass**, 270 constants, seven headlines, statements imported, no new
  axioms. The three `mfinite` headlines use propext, Classical.choice and Quot.sound; `no_tail_of_mfinite` and the three phase
  theorems use propext and Quot.sound.
- **Notebook: RESULT OK (nb2).** Six outputs, no message cells, KernelChecked 270, axiom sets as the Check printed them, layer
  sizes as computed, the Abstract cell equal to `abstract-final.txt`, no local paths. Build 176.3 s, sampled tree peak 2.62 GB, at
  least 5,576 MiB free, no swap growth. Outputs 1 to 5 are byte-identical to nb1's; output 6 differs only in LeanLink's temporary
  module name.
- **Computation cell:** G16 representative 41's layer sizes equal the Python mirror's.
- **Mutation control:** one chunk per phase at a maximizer rejected (L1489).
- **Receipts:** `cited/l1496-a6/a6-nb2-receipts.tar.gz`, `cited/l1493-a6/a6-nb1-receipts.tar.gz` and `cited/l1489-phasetrees/phase-trees-receipts.tar.gz` (919f5a7c…).

## Submit parameters

- Title: [`title.txt`](title.txt). Abstract: `abstract-final.txt`.
- Headlines (full names): `Rule30Submission.g16_mfinite`, `.p1024_mfinite`, `.p480_mfinite`, `.no_tail_of_mfinite`, `.g16_phase`,
  `.p1024_phase`, `.p480_phase`.

## Prior art and credit

- A5 (ours, d37d24): the objects and the criterion. `Rule30EtherEpisode` (ours), `Rule30EtherGrounding` (Lowry): the ether.
  `Rule30StripCertificates` (the kit): search with pruning. The record: the phases and their computed tables (CL676, CL683).
- Search (CL705, CL710, L1493): `record_find`, one term at a time: "G16", "P1024", "survival", MFinite, "longest episode", IsPhase,
  "top word"; `known_find` index at 20:56Z, kit c42f6e51. Episode bounds appear only for the eight-tick ether, in our own entries, and
  "top word" has no hit in the kit, the portal or the open PRs. Scoped, not a priority clearance.
