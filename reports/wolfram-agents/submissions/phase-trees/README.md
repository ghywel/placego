# Three periodic phases behind Rule 30's black edge, excluded to bounded depth (A6) — delivery record

**Status: DRAFT by Cloud (packaging review, CL710), 3 November 2026. Not assembled, not posted.** The Lean is Local's probe
`tests/probes/lean/PhaseTrees.lean` (L1489, 509 lines, 7e2590f1…; GPT's source-faithfulness PASS GC2604 and, for the G16
single-phase forerunner, GC2600). The tree is Cloud's (CL706), its soundness and alignment contract GPT's (GC2596), the builds
Local's (L1484, L1489). Posting waits on the portal form, the notebook, GPT's packet read and the owner's word.

## Statement

| Headline | Says |
|---|---|
| `g16_mfinite` | every alignment of G16 (128-cell ring, lag 72, period 16): longest episode at depth 14 is 22 ticks |
| `p1024_mfinite` | every alignment of P1024 (1,024-cell ring, lag 21, period 1,024): longest episode at depth 8 is 24 ticks |
| `p480_mfinite` | every alignment of the 480-phase (480-cell ring, period 32, two words): longest episode at depth 10 is 24 ticks |
| `no_tail_of_mfinite` | a finite longest episode at depth k excludes every black-edge code that follows the phase from any depth d ≤ k on |

Also `g16_phase`, `p1024_phase`, `p480_phase` (each is a phase), `cone` (locality), `sound` and `rep_bound` (the tree).

## Package (Cloud's draft; Local assembles)

- `title.txt`, `abstract.txt` (under 250 words), `essay-prose.md` (this folder); the computation section is Local's table.
- Portal form: from the probe, with the four headlines above (Local decides whether the three phase theorems are headlines too).
- Notebook: as for A5 and the synthesis entry; the computation cell replays `phase_tree_size.py`'s table.
- Kit form: a module `Rule30PhaseTrees` on `Rule30FrozenRuler`, or none; the owner decides after posting.

## Checks (Local fills)

- Kit Check / portal Check: [pending]. Axioms: propext, Classical.choice, Quot.sound on the three headlines; propext and
  Quot.sound on the phase theorems and `no_tail_of_mfinite` (L1489).
- Mutation control: one chunk per phase at a maximizer rejected (L1489). Receipts: `cited/l1489-phasetrees/...` (919f5a7c…).

## Prior art and credit

- A5 (ours, d37d24): the objects and the criterion. `Rule30EtherEpisode` (ours), `Rule30EtherGrounding` (Lowry): the ether.
  `Rule30StripCertificates` (the kit): search with pruning. The record: the phases and their computed tables (CL676, CL683).
- Search (CL705, CL710): `record_find` "G16", "P1024", "survival"; `known_find` index at 18:49Z: no portal or kit entry on these
  phases or on episode certificates beyond the ether. Scoped, not a priority clearance.
