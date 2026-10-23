# Submission 9: rule 210, the two-sided statement, no finite configuration keeps the clock (Cloud, 2026-10-23)

MAP.md candidate 5, second half: PROOFS.md entry 32 (Proposition 19; GPT's clearing-front proof GC478, second-read by
Local L285), formalized from GPT's chain GC1700 (`../../GPT-PROOFS32-CHAIN.md`), with the background built sideways
and the finite case by rule 90's freshman's dream in place of the chain's residue-class arithmetic.

- `Rule30Submission.lean`: the module, built and checked in the Rule30PrizeKit at the verifier's commit `cc1e0e0`
  (Lean 4.35.0, Mathlib `56a005855e`). No double quote or backslash in the source. Hand proofs and inductions, no
  kernel computation.
- `check.json`: the kit's `Check.lean` output, verdict `pass`: kernel replay of 236 constants, no new axioms, eight
  headlines each on `propext`, `Classical.choice`, `Quot.sound` only.
- Definitions: `run210 x0` (rule 210 on any configuration; `run210_seed` bridges to the kit's `run g210`),
  `Clock210` (`run210 x0 t 0 = decide (t % 2 = 1)`, white at even times), `Diag210`, `FinLeft210`, `Finite210`;
  `run90`; `lft`, `colR`, `bg` (the sideways background), `Admissible`; `Dev` (the deviation setting), `bb`, `tau`,
  `P`, `Q`, `Ab`.
- Headlines: `no_finite_clock` (the headline: `Finite210 x0 → Clock210 x0 → False`);
  `no_finite_eventually_alternating` (clock from `T` in either phase `φ`); `seed_not_eventually_alternating` (the
  kit's seed through `run210_seed`); `clock_bg` (every admissible left row has a clock realization);
  `parity_left_of_clock`; `no_finite_clock90`; `Dev.even_impossible`; `Dev.odd_impossible`.
- Timing here (4 shared cores): elaboration 10 s, `lake build Rule30Submission` 26 s, `Check.lean` 13 s.
- `essay-template.md` + `assemble.py` → `essay.md`, fast cell order (three display cells with the one `Open` set,
  then `Axioms`, `CallGraph`, `KernelCheck` last). The exploration cells rebuild the sideways background in Wolfram
  Language and run rule 210 on finite seeds with `CellularAutomaton`.
- Expected outputs, computed first by `expected_numbers.py` beside this file: the longest clock survival among the
  8,191 nonempty seeds in `−4 … 8` is 11 steps, by the seed `0000010001010` (positions −4 to 8); the background of
  the empty left row has sites 1 … 64 `1000101000101000101000101000101000101000101000101000101000101000` and, truncated
  at site 160, survives 161 steps; the background of the left row with a black cell at depth 3 has sites −4 … 40
  `010001010101000101000101000101000101000101000` and survives 161 steps truncated at 160; the deviation table for
  flipped sites `1, 2, 3, 4, 6, 8` of the empty-row background: failures at `1, 5, 3, 5, 7, 11`, with `w = 1, 0, 0,
  1` for the even sites and the predictions `e + 2w + 1 = 5, 5, 7, 11` matching. `Axioms` the three standard ones;
  `KernelCheck` `Success`.
- What is new relative to the kit, as the essay states it: the kit's barrier is about the seed's center column; this
  answers the two-sided period-2 question for rule 210 (yes), next to submission 6's one-sided answer (no). The
  "What is not proved" section says plainly that nothing here concerns rule 30's center column and that the
  background is constructed, not identified with the hand proof's closed form.
- Byline, as the owner set it: "Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)"; API `authors`
  "Gareth Herbert; Claude (Anthropic); GPT (OpenAI)". Goes on the owner's renewed standing permission (L767).

To reproduce: copy `Rule30Submission.lean` over the kit's template, then `lake build Rule30Submission` and
`lake env lean --run Check.lean Rule30Submission --claim partial --headline Rule30Submission.no_finite_clock --headline Rule30Submission.no_finite_eventually_alternating --headline Rule30Submission.seed_not_eventually_alternating --headline Rule30Submission.clock_bg --headline Rule30Submission.parity_left_of_clock --headline Rule30Submission.no_finite_clock90 --headline Rule30Submission.Dev.even_impossible --headline Rule30Submission.Dev.odd_impossible`
(one `--headline` flag per name; the checker prints a deprecation warning before its JSON).
