# Submission draft: white runs beside two periodic columns (Theorem B)

Local, 2026-10-29 (L1084). Theorem B of PROOFS.md entry 6, with GPT's odd-run refinement, ported to the kit's
core Lean on `Rule30Realization.evol`.

- `Rule30PairedColumnRuns.lean`: the kit catalog module, committed on a local kit branch `paired-column-runs`
  (not pushed). The kit's `Check.lean` passes (`--claim partial`, both headlines, 81 constants replayed,
  standard axioms: propext and Quot.sound).
- `Rule30Submission.lean`: the same proof as the essay's module, which compiles against the verifier's kit with
  the same axioms.
- `essay.md`: the draft essay. Its census cell was run separately (rings of 3 to 14 cells in the Wolfram
  Language, and 3 to 18 in Python), with no violations and the bound attained at P = 3 and P = 4.

**Status:** awaiting GPT's read of the statement, the carrying proof steps and the honest-scope section. After
that come the kit pull request, the notebook build and the upload, under the owner's permission of 2026-10-29.
