# Submission 5: Corollary F, near-squares beside a period-2 center column are fatal (Cloud, 2026-10-23)

MAP.md candidate 4, last part. PROOFS.md entry 11 (a hand proof, no Lean before this) formalized on the kit's
`evol`, from the record's Lean for Lemma B2 (`tests/probes/lean/JenPow2.lean`) and Theorem A‴
(`tests/probes/lean/TheoremA4.lean`).

- `Rule30Submission.lean`: the module, built and checked in the Rule30PrizeKit at the verifier's commit `cc1e0e0`
  (Lean 4.35.0, Mathlib `56a005855e`). No double quote or backslash in the source.
- `check.json`: the kit's `Check.lean` output, verdict `pass`: kernel replay of 189 constants, no new axioms, six
  headlines each on `propext`, `Classical.choice`, `Quot.sound` only.
- Headlines: `corollary_F` (the headline: a configuration with a leftmost black cell `L ≥ 1` left of column 0, whose
  column 0 reads `decide (t % 2 = 1)` from `T0`, has no `K` and pairs `i < i′` with `i′ − i` unbounded, `T0 ≤ 2i`,
  and `evol x0 (2(i+s)) 1 = evol x0 (2(i′+s)) 1` for all `s + K < i′`); `col_m1` (column −1 under the clock);
  `blocks_of_visible`; `theorem_A3`; `infinitely_many_black`; `lemma_B2`.
- Timing here (4 shared cores): `lake build Rule30Submission` 36 s, `Check.lean` 13 s. Hand proofs only.
- `essay-template.md` + `assemble.py` → `essay.md`, as in the other folders; fast cell order (three displays, one
  `Open` set, then `Axioms`, `CallGraph`, `KernelCheck` last).
- Expected outputs, computed first by `expected_numbers.py` beside this file: period-doubling's first 32 bits
  `01000101010001000100010101000101`; the near-square table `{k, l(0, 2^k), 2^k − 1}` for `k = 1 … 11` with
  `l = 2^k − 1` in every row (1, 3, 7, …, 2047); the forced left half from 3,000 clock steps: `Length[row0]` 2999,
  the first 40 black depths `1, 7, 9, 15, 16, 18, 21, 24, 25, 27, 29, 31, 32, 33, 37, 39, 40, 44, 46, 48, 49, 51, 53,
  57, 59, 61, 62, 65, 66, 67, 70, 71, 72, 73, 76, 77, 79, 81, 82, 83`, 1497 black cells, the last at depth 2995, the
  longest white gap 13. The seed's first 20 center cells `11011100110001011001`. `Axioms` the three standard ones;
  `KernelCheck` `Success`.
- What is new relative to the kit, as the essay states it: the kit asks the period-2 question for the seed (`Q01`)
  and has Jen's clocked bound; it has nothing joining that bound to the diagonal periods, and nothing excluding
  classes of right neighbours under the clock. The "What is not proved" section states the `L ≥ 1` and `T0 ≤ 2i`
  hypotheses and the shift remark plainly.
- Byline, as the owner set it: "Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)"; API `authors`
  "Gareth Herbert; Claude (Anthropic); GPT (OpenAI)". Submitted by Local on the owner's standing overnight consent
  (CL574, L758).

To reproduce: copy `Rule30Submission.lean` over the kit's template, then `lake build Rule30Submission` and
`lake env lean --run Check.lean Rule30Submission --claim partial --headline Rule30Submission.corollary_F --headline Rule30Submission.col_m1 --headline Rule30Submission.blocks_of_visible --headline Rule30Submission.theorem_A3 --headline Rule30Submission.infinitely_many_black --headline Rule30Submission.lemma_B2`
(one `--headline` flag per name; the checker prints a deprecation warning before its JSON).
