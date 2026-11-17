# Submission 3: the left diagonals, Lemmas B1–B3 (Cloud, 2026-10-23)

MAP.md candidate 4: the band of stripes beside the pattern's left edge. PROOFS.md entries 8, 9 and 12 (Local's
`tests/probes/lean/JenPow2.lean`) restated on the kit's `evol`, with the bridge to the kit's `Rule30Diagonals.D`.

- `Rule30Submission.lean`: the module, built and checked in the Rule30PrizeKit at the verifier's commit `cc1e0e0`
  (Lean 4.35.0, Mathlib `56a005855e`). No double quote or backslash in the source (it sits inside a Wolfram string).
- `check.json`: the kit's `Check.lean` output, verdict `pass`: kernel replay of 162 constants, no new axioms, eight
  headlines each on `propext`, `Classical.choice`, `Quot.sound` only.
- Headlines, all in the kit's vocabulary for the single-seed pattern (`Rule30Diagonals.D j t = cell t (j - t)`):
  - `seed_no_adjacent_white` (Lemma B1): diagonals `j` and `j + 1` are not both eventually white;
  - `seed_white_then_black` (Lemma B1): an eventually white diagonal `j` makes `j + 2` eventually black;
  - `seed_periods_unbounded` (Lemma B2): no `P ≥ 1` is an eventual period of every left diagonal, the lower bound
    matching the kit's `D_periodic` upper bound `2^j`;
  - `seed_periods_unbounded_quant`: among `j ≤ 4^P + 1` one diagonal does not have eventual period `P`;
  - `seed_infinitely_many_white`, `seed_infinitely_many_black`: the corollary;
  - `lemma_B2`, `lemma_B3_sharp`: the general forms for every configuration `x0` with a leftmost black cell `e`
    (the module's `D x0 e k t = evol x0 t (e - t + k)`); B3 says a white run of the row at time `t` inside diagonals
    `0 … M` that have had period `P` for `P` steps, bounded on the left by a black diagonal `g`, has length
    `M' - g ≤ 2P - 1`.
- Timing here (4 shared cores): `lake build Rule30Submission` 18 s, `Check.lean` 10 s. No kernel computation; the
  module is hand proofs only, so the notebook's cost is LeanLink's display cells.
- `essay-template.md` is the essay with a placeholder for the Lean; `assemble.py` inserts `Rule30Submission.lean`
  verbatim and writes `essay.md`. Edit the template, never `essay.md`, and re-run `python3 assemble.py`. The cell
  order is the fast one (every `TypeForm` display with the one `Open` set before `Axioms`, `CallGraph` and
  `KernelCheck`; `KernelCheck` last).
- Expected outputs of the exploration cell, computed here in Python first from 12,000 rows: for `j = 0 … 12` the least
  eventual period `1, 1, 1, 2, 1, 2, 2, 1, 4, 1, 4, 4, 4` and the colour `black, black, white, mixed, black, mixed,
  mixed, white, mixed, black, mixed, mixed, mixed`. `Axioms` the three standard ones; `KernelCheck` `Success`.
- What is new relative to the kit, as the essay states it: the kit has the upper bound `D_periodic` and cites Rowland
  2006 for the doubling without a formal statement; it has lower bounds only for right diagonals
  (`Rule30RightPeriods`). B1, B2's lower bound and quantitative form, and B3 are absent from its catalogue. The
  unboundedness is credited to Rowland in the abstract, the provenance and the references.
- Byline, as the owner set it: "Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)"; API `authors`
  "Gareth Herbert; Claude (Anthropic); GPT (OpenAI)". Submitted by Local on the owner's standing overnight consent
  (CL574, L758).

To reproduce: copy `Rule30Submission.lean` over the kit's template, then `lake build Rule30Submission` and
`lake env lean --run Check.lean Rule30Submission --claim partial --headline Rule30Submission.seed_no_adjacent_white --headline Rule30Submission.seed_white_then_black --headline Rule30Submission.seed_periods_unbounded --headline Rule30Submission.seed_periods_unbounded_quant --headline Rule30Submission.seed_infinitely_many_white --headline Rule30Submission.seed_infinitely_many_black --headline Rule30Submission.lemma_B2 --headline Rule30Submission.lemma_B3_sharp`
(one `--headline` flag per name).
