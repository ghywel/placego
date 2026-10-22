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

## The essay (Cloud, 2026-10-22, later the same evening)

- `essay-template.md` is the essay with a placeholder for the Lean; `assemble.py` inserts `Rule30Submission.lean`
  verbatim and writes `essay.md`. Edit the template, never `essay.md`, and re-run `python3 assemble.py`.
- `essay.md` is what Local builds on the Mac (see ../../HANDOVER-LOCAL.md): with the kit at `$RULE30PRIZE_KIT` and
  LeanLink ≥ 1.2.0, `md2nb["essay.md", "essay.nb", "UseCache" -> False]` in a plain kernel (not the MCP's 60-second
  default). Expected outputs of the exploration cells, computed here in Python first: the first 20 center cells
  `11011100110001011001`; blocks `1 0^q` occur 22, 14, 6, 2, 2, 0, 0 times for q = 8, 9, 10, 11, 12, 15, 20 in the
  first 10,000 cells, longest white run 12; states after 1..4 periods: q=9 {75,69,45,38} not fixed, word `10?1111111`;
  q=10 {69,38,31,31}, q=11 {66,29,24,24}, q=12 {63,24,21,21}, q=15 {62,20,20,20}, q=20 {62,8,7,7}, q=25 {62,7,7,7},
  all fixed after 3, words `1 0 0 1^(q-2)`; the W^26 = W^22 table all True for q = 22..25. The `KernelCheck` cell
  should return `Success`, and `Axioms` the three standard ones.
- Byline, as the owner set it (2026-10-22): "Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)". For the API's
  `authors` field use "Gareth Herbert; Claude (Anthropic); GPT (OpenAI)". Nothing is submitted without the owner's
  explicit yes on the built notebook.

## Submitted, and verified (2026-10-22)

Submitted by Local on the owner's yes at 22:50 BST as **R30-20261022-c27323** (L754), from `essay.md` at commit
51436b05. **Lean Verified at 23:06 BST** after a maintainer's rerun (the automatic check hit the four-minute clock
twice; L755–757). The template was then reordered (every `TypeForm` display before `KernelCheck`, one `Open` set),
after Local measured two display cells at 105 s when they came after the kernel check (L756); `essay.md` now holds
that order, for any later resubmission or as the pattern for later essays. The submitted notebook is the one at
51436b05.
