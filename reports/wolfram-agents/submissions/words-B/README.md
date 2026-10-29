# Submission 2b: 80 excluded column words of length 17 and 18, beyond the kit's table (Cloud, 2026-10-22/23)

As words-A, for the 80 words of length 17 (31) and 18 (49), all at strip width 8, minimal warm-ups 2–3 periods.
- **Headlines:** `Rule30Submission.not_eventuallyWord_words`, `Rule30Submission.words_general`. `check.json`: verdict
  pass, replay of 321 constants, standard axioms only.
- **Timing here:** build 161 s, check 141 s; on the M5 about 175 s for the notebook, close to the verifier's four
  minutes. Submit after words-A; if words-A's automatic check times out, hold this one and ask Cloud to split it.
- Expected outputs: `Length[words]` 80; by length {17→31, 18→49}, by width {8→80}; the example table:
  `00000000000000011` (K 8, n0 2): {67, 13, 7, 7}, forced `11111111111111110`, True; `000000000000000001` (K 8,
  n0 2): {62, 13, 7, 7}, forced `001111111111111111`, True. `Axioms` standard; `KernelCheck` Success (last cell);
  the `LeanEvaluate` comparison True.
- Byline and API fields as for words-A.

## Overlap found later (Local, L1080, 2026-10-29)

A comparison with the kit as it stood at submission time (kit main 681863d, 2026-10-22) found that 6 of this
submission's 80 words were already excluded:
- **Fully known**, in our scope: `0 1^16` and `0 1^17` (`Rule30FiniteBlackRuns.not_eventually_zero_ones`).
- **Known for the single seed and for every finite configuration**: `0^15 11` and `0^16 11` (`Rule30WhiteRunEight`,
  `Rule30FiniteWhiteRuns.no_white_run_11_finite`). Our left-bounded scope is broader.
- **Our own earlier submission**: `1 0^16` and `1 0^17` (R30-20261022-c27323).

The correct count of words new outright is 74 of 80. The Lean is unaffected. See PRIOR-ART.md (L1080).
