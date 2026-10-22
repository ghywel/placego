# Submission 6: rule 210 beside the clock, the one-sided period-2 statement is false (Cloud, 2026-10-23)

MAP.md candidate 5, first half: PROOFS.md entry 18 (the parity invariant) and §8.65's witness (the empty left half),
formalized for the first time, in the kit's zero-boundary (ZBL) encoding. Barrier material, not a rule 30 claim.

- `Rule30Submission.lean`: the module, built and checked in the Rule30PrizeKit at the verifier's commit `cc1e0e0`
  (Lean 4.35.0, Mathlib `56a005855e`). No double quote or backslash in the source. Everything is by `rfl`,
  induction and `omega`; no kernel computation.
- `check.json`: the kit's `Check.lean` output, verdict `pass`: kernel replay of 29 constants, no new axioms, six
  headlines each on `propext`, `Classical.choice`, `Quot.sound` only (several use fewer).
- Definitions: `zrow210 L t k` (rule 210's left half with the period-2 clock at the wall, black at the even steps
  as in the kit's `InX`; depth `k` is position `−k`; the start `L` at depths `k ≥ 1`); `InX210 L` (column −1 white at
  every even step, which is what the clock forces); `Q01_210` (the kit's `Q01` with those replacements, using the
  kit's `Rule30ZeroBoundary.FinSupp`).
- Headlines: `not_Q01_210` (the headline: `¬ Q01_210`, by the empty start); `parity_invariant` (for every start
  with `InX210`, every black cell has `t + k` even); `linear` (the step is rule 90's, `xor (z t (k+2)) (z t k)`);
  `white_start_inX`, `white_start_parity` (the empty start keeps the clock; from a white start every black cell has
  `t + k` even); `no_adjacent`.
- Timing here (4 shared cores): `lake build Rule30Submission` 7–9 s, `Check.lean` 11 s. (A first `lake build` of
  this module hung for twelve minutes in a stale lake process and was killed; `lake env lean` on the file takes 8 s
  and the rebuild 7 s. If the Mac's build hangs, run `lake env lean Rule30Submission.lean` first.)
- `essay-template.md` + `assemble.py` → `essay.md`, fast cell order (three display cells with the one `Open` set,
  then `Axioms`, `CallGraph`, `KernelCheck` last). The first exploration cell shows the kit's own `Q01` beside ours
  via `rule30Submission["Ruliology.CellularAutomata.Rule30ZeroBoundary.Q01"]`.
- Expected outputs, computed first by `expected_numbers.py` beside this file: the parity check over 300 steps inside
  the light cone finds 0 black cells with `t + k` odd among 13,679 black cells; column −1 is white at every even
  `t < 40`; the forced column-1 bits at the odd steps `1, 3, 5, …` begin `0110000111111110000000000000000111…`
  with runs of lengths `1, 2, 4, 8, 16, 32, 64, 23` (the last cut by the 150 odd steps computed); the 12-row picture
  has the wall black at even rows; the count of width-`W` starts keeping the clock through time `W − 1` is
  `1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64` for `W = 1 … 12`, equal to `2^⌊W/2⌋` in every row. `Axioms` the three
  standard ones; `KernelCheck` `Success`.
- What is new relative to the kit, as the essay states it: the kit's barrier is about the seed's center column of
  rules 90/150/210; this answers the kit's period-2 question `Q01` itself for rule 210 (no), and proves the left half
  linear beside the clock. The two-sided statement for rule 210 (PROOFS 32) is cited as the record's hand proof and
  not formalized. The doubling-runs formula and the `2^⌊W/2⌋` count are computations, said so.
- Byline, as the owner set it: "Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)"; API `authors`
  "Gareth Herbert; Claude (Anthropic); GPT (OpenAI)". Submitted by Local on the owner's standing overnight consent
  (CL574, L758).

To reproduce: copy `Rule30Submission.lean` over the kit's template, then `lake build Rule30Submission` and
`lake env lean --run Check.lean Rule30Submission --claim partial --headline Rule30Submission.not_Q01_210 --headline Rule30Submission.parity_invariant --headline Rule30Submission.linear --headline Rule30Submission.white_start_inX --headline Rule30Submission.white_start_parity --headline Rule30Submission.no_adjacent`
(one `--headline` flag per name; the checker prints a deprecation warning before its JSON).
