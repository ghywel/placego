# Submission 1: the white end, `1 0^q` for every q ≥ 10 (Cloud, 2026-10-22)

- `Rule30Submission.lean`: the module, built and checked in the Rule30PrizeKit at the verifier's commit `cc1e0e0`
  (Lean 4.35.0, Mathlib `56a005855e`). PROOFS.md entry 40 (Local's `tests/probes/lean/WhiteEnd.lean`) restated on the
  kit's `evol` and `cell`, with the bridge to the kit's `EventuallyWord`.
- `check.json`: the kit's `Check.lean` output, verdict `pass`: kernel replay of 207 constants, no new axioms, four
  headlines each on `propext`, `Classical.choice`, `Quot.sound` only.
- Headlines: `Rule30Submission.not_eventuallyWord_white_end` (the center column of the seed is never eventually
  `1 0^q`, q ≥ 10, in the kit's own vocabulary), `white_end` (every column of every configuration with a leftmost
  black cell), `white_end_finite` (finite nonzero configurations), `white_end_seed` (every column of the seed).
- Timing here (4 shared cores): `lake build Rule30Submission` 86 s, `Check.lean` 70 s.
- The essay is `essay.md` beside this file, once written; Local builds it on the Mac (see ../../HANDOVER-LOCAL.md).

To reproduce: copy `Rule30Submission.lean` over the kit's template, then
`lake build Rule30Submission` and
`lake env lean --run Check.lean Rule30Submission --claim partial --headline Rule30Submission.not_eventuallyWord_white_end --headline Rule30Submission.white_end --headline Rule30Submission.white_end_finite --headline Rule30Submission.white_end_seed`
(one `--headline` flag per name).
