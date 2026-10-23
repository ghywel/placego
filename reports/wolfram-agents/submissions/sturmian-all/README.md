# Submission 8: every Sturmian word, every slope and every intercept, excluded beside the clock (Cloud, 2026-10-23)

Theorem E of the record (PROOFS.md entry 14) in full, by GPT's combinatorial route (GC1694) through Corollary F:
the factor-complexity pigeonhole (Bugeaud–Kim Lemma 2.2) and the telescoping of the floor formula, with no
continued fractions. Supersedes submission 7's characteristic case; the two are filed separately.

- `Rule30Submission.lean`: the module, built and checked in the Rule30PrizeKit at the verifier's commit `cc1e0e0`
  (Lean 4.35.0, Mathlib `56a005855e`). No double quote or backslash in the source. Hand proofs over the reals
  (floors, fractional parts, finite sets), no kernel computation.
- `check.json`: the kit's `Check.lean` output, verdict `pass`: kernel replay of 250 constants, no new axioms, eight
  headlines each on `propext`, `Classical.choice`, `Quot.sound` only.
- Definitions: `mechZ α θ i = ⌊θ + (i+1)α⌋ − ⌊θ + iα⌋`, `mech α θ i = decide (mechZ = 1)` (with `mech_eq_fract`:
  `1` iff `1 − α ≤ fract (θ + iα)`, for `0 ≤ α < 1`); `thr α n x` (the `k ≤ n` with `1 ≤ x + fract (kα)`);
  `image f r c` (sliding block codes).
- Headlines: `sturmian_excluded` (the headline: irrational `α`, `0 ≤ α < 1`, any `θ`; a configuration with a
  leftmost black cell `L ≥ 1` left of column 0, the clock from `T0`, visible bits `evol x0 (2 i) 1 = mech α θ i`:
  `False`); `sturmian_excluded_clock0` (`T0 = 0`, `L ≥ 1` derived); `sturmian_excluded_fract` (the record's form of
  the word); `sturmian_block_excluded` (visible bits `image f r (mech α θ)`, any window `r`); `sturmian_pairs`
  (near-squares with slack 1 at unbounded gaps, every intercept); `exists_block_collision` (the pigeonhole);
  `no_small_period` (no long block of a bounded period); `corollary_F`.
- Timing here (4 shared cores): elaboration 17 s, `lake build Rule30Submission` 26 s, `Check.lean` 19 s.
- `essay-template.md` + `assemble.py` → `essay.md`, fast cell order (four display cells with the one `Open` set, then
  `Axioms`, `CallGraph`, `KernelCheck` last).
- Expected outputs, computed first by `expected_numbers.py` beside this file: the golden word with intercept 1/2 begins
  `1010110110101101101011010110110101101011`; distinct blocks `p(n) = 2, 3, …, 13` for `n = 1 … 12`; the collision
  table `{n, i, j, gap, common future, slack}` for the golden slope at intercept 1/2:
  `{5,2,5,3,6,−1}, {10,0,8,8,16,−8}, {20,5,18,13,32,−14}, {50,0,34,34,71,−37}, {100,18,73,55,142,−69},
  {200,0,144,144,304,−160}, {500,73,306,233,608,−302}, {1000,0,610,610,1291,−681}, {2000,306,1293,987,2582,−1289}`
  and for `√2 − 1` at intercept 1/10: `{5,0,5,5,6,−1}, {10,1,8,7,10,−2}, {20,0,12,12,35,−23}, {50,8,37,29,68,−31},
  {100,0,70,70,175,−105}, {200,8,177,169,406,−229}, {500,0,408,408,583,−175}, {1000,585,993,408,1391,−398},
  {2000,993,1978,985,2376,−398}` (slack never above 1; the Mathematica `collide` scans positions in the same order
  as the Python, first repeat wins); the forced left half of the golden word at intercept 1/2 from 3,000 clock
  steps: `Length[row0]` 2999, first 30 black depths `2, 3, 6, 9, 10, 11, 13, 14, 28, 29, 30, 33, 34, 36, 37, 38, 39,
  40, 42, 47, 48, 49, 51, 52, 53, 56, 57, 58, 59, 60`, 1512 black cells, the last at depth 2997, largest spacing 14.
  `Axioms` the three standard ones; `KernelCheck` `Success`.
- What is new relative to the kit, as the essay states it: nothing in the kit excludes any aperiodic right
  neighbour under the clock; this excludes every Sturmian word and every finite block code of one. The "What is not
  proved" section states the slope convention, the inequality-only complexity bound and the rational case plainly.
- Provenance: Theorem E (Local, 2026-10-05, Diophantine); the route through Corollary F is GPT's GC1694
  (2026-10-23), after Cloud's CL582 had concluded, wrongly, that none existed; formalized by Cloud the same day.
- Byline, as the owner set it: "Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)"; API `authors`
  "Gareth Herbert; Claude (Anthropic); GPT (OpenAI)". The owner's overnight standing consent (CL574) was for the
  night; this one goes on the owner's yes.

To reproduce: copy `Rule30Submission.lean` over the kit's template, then `lake build Rule30Submission` and
`lake env lean --run Check.lean Rule30Submission --claim partial --headline Rule30Submission.sturmian_excluded --headline Rule30Submission.sturmian_excluded_clock0 --headline Rule30Submission.sturmian_excluded_fract --headline Rule30Submission.sturmian_block_excluded --headline Rule30Submission.sturmian_pairs --headline Rule30Submission.exists_block_collision --headline Rule30Submission.no_small_period --headline Rule30Submission.corollary_F`
(one `--headline` flag per name; the checker prints a deprecation warning before its JSON).
