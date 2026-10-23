# Submission 7: every characteristic Sturmian word is excluded beside the clock (Cloud, 2026-10-23; block codes added 00:55 BST)

Theorem E's characteristic case (PROOFS.md entry 14, one intercept per slope) by word combinatorics on top of
Corollary F (PROOFS 11, submission 5): the standard words, their near-commutation, the near-square at the start.

- `Rule30Submission.lean`: the module, built and checked in the Rule30PrizeKit at the verifier's commit `cc1e0e0`
  (Lean 4.35.0, Mathlib `56a005855e`). No double quote or backslash in the source. Hand proofs and list inductions,
  no kernel computation.
- `check.json`: the kit's `Check.lean` output, verdict `pass`: kernel replay of 266 constants, no new axioms, seven
  headlines each on `propext`, `Classical.choice`, `Quot.sound` only.
- Definitions: `wpow w a` (`w` repeated); `std d n` (`[1]`, `[0]`, then `(std (n+1))^(d n) ++ std n`); `cw d i`
  (the characteristic word, position `i` read in `std d (i + 2)`); `Agree u v m`.
- Headlines: `characteristic_excluded` (the headline: `d` with every `d n ≥ 1`, a configuration with a leftmost
  black cell at `−L`, the clock on column 0 from time 0, visible bits `evol x0 (2 i) 1 = cw d i`: `False`);
  `characteristic_block_excluded` (visible bits `image f r (cw d) i`, any sliding block code of window `r`);
  `characteristic_excluded_compl` (visible bits `!cw d i`); `fibonacci_excluded` (`d n = 1`);
  `cw_near_square` (`s + 2 < |std d (n+1)|` gives `cw d s = cw d (|std d (n+1)| + s)`); `std_near_comm`
  (`Agree (std (n+1) ++ std n) (std n ++ std (n+1)) (|std (n+1)| + |std n| − 2)`); `corollary_F`.
- Timing here (4 shared cores): `lake build Rule30Submission` 20–40 s, `Check.lean` 11–15 s.
- `essay-template.md` + `assemble.py` → `essay.md`, fast cell order (four display cells with the one `Open` set, then
  `Axioms`, `CallGraph`, `KernelCheck` last).
- Expected outputs, computed first by `expected_numbers.py` beside this file: Fibonacci standard words
  `1, 0, 01, 010, 01001, 01001010, 0100101001001`, lengths `1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233`, the
  Fibonacci word's first 55 bits `0100101001001010010100100101001001010010100100101001010`; near-commutation
  `{True, True}`; the near-square tables `{n, |std n|, common future of (0, |std n|), slack}`: Fibonacci
  `{1,1,0,1}, {2,2,1,1}, {3,3,3,0}, {4,5,6,−1}, {5,8,11,−3}, {6,13,19,−6}, {7,21,32,−11}, {8,34,53,−19}` and
  `2,1,3,1,…`: `{1,1,1,0}, {2,3,2,1}, {3,4,13,−9}, {4,15,17,−2}, {5,19,51,−32}, {6,53,70,−17}, {7,72,267,−195},
  {8,269,339,−70}` (slack never above 2); the forced left half of the Fibonacci word from 3,000 clock steps:
  `Length[row0]` 2999, first 30 black depths `1, 7, 10, 11, 13, 14, 16, 17, 19, 21, 23, 25, 26, 27, 28, 30, 31, 33,
  34, 38, 41, 42, 43, 46, 47, 49, 50, 52, 54, 56`, 1515 black cells, the last at depth 2998, longest white gap 14.
  `Axioms` the three standard ones; `KernelCheck` `Success`.
- What is new relative to the kit, as the essay states it: nothing in the kit excludes any aperiodic right
  neighbour under the clock (`Rule30DrivenLeft.no_periodic_column` is for eventually periodic drivers; CATALOG only
  remarks that Sturmian sequences are not eventually periodic). The "What is not proved" section states the time-0
  clock, the characteristic-only intercept and the unformalized rotation identification plainly.
- Byline, as the owner set it: "Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)"; API `authors`
  "Gareth Herbert; Claude (Anthropic); GPT (OpenAI)". Submitted by Local on the owner's standing overnight consent
  (CL574, L758).

To reproduce: copy `Rule30Submission.lean` over the kit's template, then `lake build Rule30Submission` and
`lake env lean --run Check.lean Rule30Submission --claim partial --headline Rule30Submission.characteristic_excluded --headline Rule30Submission.characteristic_block_excluded --headline Rule30Submission.characteristic_excluded_compl --headline Rule30Submission.fibonacci_excluded --headline Rule30Submission.cw_near_square --headline Rule30Submission.std_near_comm --headline Rule30Submission.corollary_F`
(one `--headline` flag per name; the checker prints a deprecation warning before its JSON).

## Errata (GPT's second read GC1697, 2026-10-23; the submitted essay R30-20261023-e872a3 is frozen, these are dated corrections)

- "Each is a prefix of the next" holds from `std 1` on: `[1] = std 0` is not a prefix of `[0] = std 1`. The formal `std_prefix` has the right indices (`std (n+1) <+: std (n+2)`); the Abstract's and the body's sentence should say so.
- The slope convention `[0; d 0 + 1, d 1, d 2, …]` is confirmed against Peltomäki (arXiv:1411.5474v2, §3); positive directives cover the slopes below 1/2 and the letter exchange the rest.

## Resubmission for the public abstract (Cloud, 2026-10-23 07:30 BST, at the owner's word)

The abstract of **R30-20261023-e872a3** reached the public submissions page garbled: the API sends one byte per character unless each
text parameter is wrapped in `utf8 = FromCharacterCode[ToCharacterCode[#, "UTF-8"]]&` (skill.md 1.14.0). The essay,
the Lean and the verdict are unaffected. `abstract-v2.md` is the corrected abstract, written to the skill's new guidance
(Markdown with TeX math, ASCII outside the math, four parts in order). Local resubmits the same notebook with
`supersedes=R30-20261023-e872a3`, the same title, authors, agent and headlines, this abstract, every text through `utf8`; the new id
and verdict go here as a dated note. The frozen module and essay are unchanged.
*Dated note (Cloud, 2026-10-23 08:09 BST, L772/L773).* Resubmitted by Local at 07:41 BST as **R30-20261023-0c4a33** (supersedes R30-20261023-e872a3),
**Lean Verified automatically at 07:43 BST**, first attempt. The public page now shows the corrected abstract typeset
(checked on `submissions.json` at 07:08Z: TeX present, no stray bytes); R30-20261023-e872a3 stands as superseded.

