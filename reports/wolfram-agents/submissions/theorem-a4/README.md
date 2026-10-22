# Submission 4: Theorem A⁗, a repeat's white run cannot lie in the settled band (Cloud, 2026-10-23)

MAP.md candidate 4, second part. PROOFS.md entries 10, 12 and 13 (Local's `tests/probes/lean/TheoremA4.lean`)
restated on the kit's `evol`, with the bridge to the kit's `cell` and `Rule30Diagonals.D` for the center column.

- `Rule30Submission.lean`: the module, built and checked in the Rule30PrizeKit at the verifier's commit `cc1e0e0`
  (Lean 4.35.0, Mathlib `56a005855e`). No double quote or backslash in the source.
- `check.json`: the kit's `Check.lean` output, verdict `pass`: kernel replay of 106 constants, no new axioms, six
  headlines each on `propext`, `Classical.choice`, `Quot.sound` only.
- Headlines:
  - `center_A4_sharp` (the headline): equal blocks of length `n` on columns 0 and 1 at times `a < a′`, the kit's
    left diagonals `0 … M` agreeing at times `a′ - P` and `a′` (`P ≥ 1`, `P ≤ a′`, `M < a′ - a`): then
    `n ≤ a′ - M + 2P - 1`; `center_A4` the record's bound `2P`;
  - `theorem_A4_sharp`, `theorem_A4`: the general form for every configuration with a leftmost black cell `L` cells
    left of column `i`, `n ≤ L + a′ - M + 2P - 1`;
  - `theorem_A3`: Theorem A‴'s corollary (a black diagonal `b < a′ - a` at time `a′` gives `n ≤ L + a′ - b`);
  - `lemma_B3_sharp`: the settled band's white-run bound `2P - 1`.
- Timing here (4 shared cores): `lake build Rule30Submission` 17 s, `Check.lean` 8 s. Hand proofs only.
- `essay-template.md` is the essay with a placeholder for the Lean; `assemble.py` inserts `Rule30Submission.lean`
  verbatim and writes `essay.md`. Edit the template, never `essay.md`, and re-run `python3 assemble.py`. Fast cell
  order: the four `TypeForm` displays with the one `Open` set, then `Axioms`, `CallGraph`, `KernelCheck` last.
- Expected outputs of the exploration cells, computed first by `expected_numbers.py` beside this file (400 steps):
  the eight longest common blocks `{n, a, a′}` of columns 0 and 1: `{12, 190, 250}, {11, 191, 251}, {11, 169, 349},
  {11, 46, 242}, {10, 333, 367}, {10, 308, 381}, {10, 192, 252}, {10, 170, 350}`; the settled width `settled[P, t]`
  for `t = 100, 200, 400` and `P = 1, 2, 4, 8, 16`: `2, 7, 28, 64, 58` / `2, 7, 28, 153, 143` / `2, 7, 28, 303, 289`;
  the bound table for the six longest blocks and `P = 1, 2, 4`: `M = 2, 7, 28`, bounds `a′ - 1, a′ - 4, a′ - 21`,
  every row `True` (18 rows). `Axioms` the three standard ones; `KernelCheck` `Success`.
- What is new relative to the kit, as the essay states it: the kit has Jen's clocked bound (`window_jen_col`) and the
  period-`2^j` bound per left diagonal (`D_periodic`) but nothing joining them; Theorem A‴, Lemma B3 and Theorem A⁗
  are absent from its catalogue (MAP.md rows for PROOFS 10, 12, 13). The essay's "What is not proved" says plainly
  that the periodicity hypothesis is not known for the center column's own repeats and that the bound is structural.
- Byline, as the owner set it: "Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)"; API `authors`
  "Gareth Herbert; Claude (Anthropic); GPT (OpenAI)". Submitted by Local on the owner's standing overnight consent
  (CL574, L758).

To reproduce: copy `Rule30Submission.lean` over the kit's template, then `lake build Rule30Submission` and
`lake env lean --run Check.lean Rule30Submission --claim partial --headline Rule30Submission.center_A4_sharp --headline Rule30Submission.center_A4 --headline Rule30Submission.theorem_A4_sharp --headline Rule30Submission.theorem_A4 --headline Rule30Submission.theorem_A3 --headline Rule30Submission.lemma_B3_sharp`
(one `--headline` flag per name). The checker prints a deprecation warning before its JSON; `check.json` is the JSON.
