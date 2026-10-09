# More column words excluded by entry 40's route (computed twice, second-read): 24 words of period 10 .. 14 and 115 of period 15 .. 18

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "41. More column words excluded by
entry 40's route (computed twice, second-read): 24 words of period 10 .. 14 and 115 of period 15 .. 18"; rebuild
with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never
this file.*

**Status:** the per-word computation was done by Local (`rule30_word_jen_census.

## In plain words

The same short argument that closed the white end also rules out 139 more drumbeat patterns that a column of a finitely seeded Rule 30 picture might have settled into.

**What it says.** For each of these patterns, a narrow strip of eight or ten cells beside the column is forced into one fixed rhythm, so the neighbouring column repeats too, which a pattern with a left edge cannot sustain. The patterns are long: periods 10 to 18, each with a long run of white or of black ticks.

**Why it matters.** It widens the list of rhythms known to be impossible, and the computation was done twice by independently written programs.

**An everyday picture.** A rule that silences a whole family of drum patterns at once, checked by two separate referees.

**Checked by machine.** A proof assistant (Lean) has checked every one of the 139 patterns, along with the argument.

## The formal statement and proof

*Status:* the per-word computation was done by Local (`rule30_word_jen_census.py`, WC, predictions first, L499) and
replayed independently by Cloud (`rule30_cloud_word_census_replay.py`, WR2, CL111; Lyndon words by Duval, successor
tables and set-valued stable sets, no shared code). Every count and word agrees. The transfer is entry 40's
(second-read by Cloud CL110 and GPT GC880), and its finish, Theorem A, is machine-checked (entry 5's note). Filed by
Local, 2026-10-09.

**Theorem.** No nonzero finite configuration of Rule 30 has a column that is eventually periodic with any of the
following period words.
- These words, of period 10 .. 14, via the width-10 relaxation (the 14 without a star are already excluded at width 8;
  the 10 starred need width 10):
  - p = 10: 0000000011*, 0011111111
  - p = 11: 00000000001, 00000000011, 00000001111*
  - p = 12: 000000000001, 000000000011, 000000000101*
  - p = 13: 0000000000001, 0000000000011, 0000000000101*, 0000000001011, 0000000001101*, 0000000001111*, 0000000010011*
  - p = 14: 00000000000001, 00000000000011, 00000000000101*, 00000000001011, 00000000001111*, 00000000010011,
    00000000010111, 00000000011011, 00000000110011*
- Every primitive word of period 15 .. 18 that is determined at width 8: 15, 20, 31 and 49 words, 115 in all. They
  are reproduced by `rule30_word_jen_census.py 8 15 18` and by WR2.
- Words are least rotations; any rotation is the same column word.

**Proof.** Entry 40's argument, word by word.
1. In the k-cell one-sided relaxation (k = 8 or 10), the stable set of the period's step relation determines x1 at
   every tick. So column +1 is eventually periodic with the word's period on every actual right half.
2. Column 0 is periodic.
3. Theorem A (entry 5; `no_two_periodic` in TheoremA.lean) forbids two adjacent columns periodic for ever when there
   is a leftmost black cell, re-basing time if the edge starts right of column 0. ∎

*Scope.* No word of period 7 .. 9 is determined at width 8 or 10. Every determined word has a run of length >= 6. The
determined share is 0.6 percent (width 8) and 1.0 percent (width 10) of periods 7 .. 14, and 0.4 percent of 15 .. 18.
The prize's 01 and every word of period <= 9 are untouched. Not a prize claim.

*Near-entry gate (Local, at filing).* `--near 41` gives entry 40, its parent: the route and the white-end family,
which this extends to other words and does not restate; 17 and 38, read. Hard checks pass.

*Machine-checked (Local, 2026-10-10 00:34 BST).* tests/probes/lean/JenRoute.lean (Lean 4, Mathlib).
- `entry41`: no configuration with a leftmost black cell has a column reading any of the 139 words periodically. The
  words are 129 at width 8 and 10 at width 10, the same lists as WC and WR2. `counts` checks the list lengths.
- Each word's finite fact is a kernel `decide` on the K cells as numbers below 2^K. Within n0 <= 6 periods the
  set of states is a fixed point of the period map, and cell +1 is constant at every tick.
- The rest is WhiteEnd.lean's assembly, made generic in K and in the word: the encoding's step lemma (StpOK 8 and
  StpOK 10 by decide), Theorem A, and the time re-basing.
- The axioms are propext, Classical.choice and Quot.sound; there is no sorryAx and no native_decide.
