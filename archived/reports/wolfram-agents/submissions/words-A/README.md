# Submission 2a: 48 excluded column words of length 11–16, beyond the kit's table (Cloud, 2026-10-22/23)

- `Rule30Submission.lean`: PROOFS.md entry 41 (Local's `tests/probes/lean/JenRoute.lean`, 2026-10-10) restricted to the
  words the kit's `Rule30StripCertificateTable` lacks, restated on the kit's `evol` and `cell`, with the bridge to
  `EventuallyWord`. 41 words at strip width 8 and 7 at width 10 (lengths 11: 1, 12: 1, 13: 2, 14: 9, 15: 15, 16: 20).
  The certificate: after each word's minimal warm-up `n0` (1–5 periods), one more period keeps cell c+1 constant at
  every tick (`walk`) and maps the reachable set into itself (`sub`, one `&&&`); `img_mono`/`reach_sub` carry it to
  every later period. Built and checked in the kit at `cc1e0e0`.
- **Headlines:** `Rule30Submission.not_eventuallyWord_words` (for every listed word, the seed's center column is not
  eventually that word) and `Rule30Submission.words_general` (every column of every configuration with a leftmost
  black cell). `check.json`: verdict pass, replay of 257 constants, no new axioms, both headlines on propext,
  Classical.choice, Quot.sound.
- **Timing here** (4 shared cores): build 140 s, check 125 s; the M5 runs about 1.5× faster, so the notebook in the
  fast cell order should take about 150 s there. Submit this one before words-B and watch the automatic check.
- `essay.md`, assembled by `../assemble_words.py` (the word list and the Lean come from the module). Expected
  outputs, computed in Python first: `Length[words]` 48; by length {11→1, 12→1, 13→2, 14→9, 15→15, 16→20}, by width
  {8→41, 10→7}; the example table: `00000000000001` (K 8, n0 2): states after 1..4 periods {62, 22, 20, 20}, forced
  column `00111111111111`, maps into itself True; `00000001111` (K 10, n0 4): {219, 135, 83, 65}, forced
  `11111111010`, True. `Axioms` the three standard ones; `KernelCheck` Success (last cell). The `LeanEvaluate` cell
  compares the module's `words` with the essay's list and should print True.
- Byline "Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)"; API `authors` "Gareth Herbert; Claude
  (Anthropic); GPT (OpenAI)"; `problem` 1, `claim` partial, `headlines` the two above, `repository`
  https://github.com/ghywel/placego. Submitted by Local on the owner's standing consent of 2026-10-22 23:12 BST (L758).

## Overlap found later (Local, L1080, 2026-10-29)

A comparison with the kit as it stood at submission time (kit main 681863d, 2026-10-22) found that 9 of this
submission's 48 words were already excluded:
- **Fully known**, in our scope (every column of every configuration with a leftmost black cell):
  `0 1^14` and `0 1^15`, by `Rule30FiniteBlackRuns.not_eventually_zero_ones` (k ≥ 9).
- **Known for the single seed and for every finite configuration**: `0^12 11`, `0^13 11` and `0^14 11`, by
  `Rule30WhiteRunEight` and `Rule30FiniteWhiteRuns.no_white_run_11_finite` (r ≥ 8). Our `words_general`, for
  every left-bounded configuration, is broader.
- **Known for the single seed**: `0^9 101`, by `Rule30StripCertificates.not_eventually_000000000101`.
- **Our own earlier submission**: `1 0^13`, `1 0^14` and `1 0^15`, by R30-20261022-c27323 (q ≥ 10).

The essay cites the `0^r 1 1` and `1 0^q` families and still counts these words among its "48 further words". The
correct count of words new outright is 39 of 48. The Lean is unaffected. See PRIOR-ART.md (L1080).
