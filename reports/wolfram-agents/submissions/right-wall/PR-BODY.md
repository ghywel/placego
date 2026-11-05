Rule30RightWall: the wall of a rain-tailed edge code. Two letters, three locks and a closed cloud

This adds `lean/Ruliology/CellularAutomata/Rule30RightWall.lean`, `Rule30RightWallLocks.lean` and `Rule30RightWallCloud.lean`, with their `public import` lines in `lean/Ruliology.lean` and a row in *Added in the kit*. It builds on `Rule30FrozenRuler`: the row is the kit's edge code and one tick is the kit's `T`.

**What it proves.** A *rain tail* is an alternating tail of an edge code, and the *wall* is the last equal pair below it.
- `predecessor_unique`: every code has exactly one predecessor under `T`.
- `top_up`, `top_stay`, `top_minus_one`, `top_minus_two`, `top_minus_three`: the exact local rule for the wall under `T`.
- `front_back`, `front_not_periodic`: eighteen windows of eleven cells are closed under the backward tick, and a code showing one is not periodic.
- `deep_words`: three backward advances of three cells leave one of two words, `A = ..####...##` or `B = .#.###...##`. `no_BB`, `no_AAA`, `witness_ABA`: the first facts about their language. `letter_after_B`, `letter_after_A`: the next letter.
- `Reset.reset`, `Reset.above`, `Reset.again`, `Reset.letters`: a ten-cell word that contains a reset word `0 1^(3m+1) 0` of `Rule30ResetFreeCore` and, with rain above it, reappears three cells higher.
- `WindowClosed.Closed`, `held_forever`, `held_not_periodic`: a set of windows closed for every pair of lower cells holds a code for ever, whatever lies below, and such a code is not periodic.
- `LockAB`, `LockAAB`, `LockThird`: closed sets of 4 windows of 45 cells, 6 of 136 and 40 of 175, which force the letters `AB`, `AAB` and `BAABAA` repeated. Each has a witness on an anchored row. `LockThird.no_floor`: below the wall's own, no depth carries a reset word in all forty windows.
- `Cloud.closed`, `avoids_lock`, `no_long_alternation`, `not_periodic`: a closed set of 798 windows of 45 cells that never reaches `LockAB`, on which the letters cannot change on 17 ticks running.
- `Entry.entry`: one explicit anchored row whose images pass from that set into `LockThird`.

**Method.** The finite checks run on numbers. `run` is the backward sweep on one number with one index, and `run_back`, `next_fast` and `closed_fast` prove it equals the sweep on words. `fw` is one forward tick on a number, and `iter_fw` proves it is `T` on all bits.

**Checks**, with Lean 4.35.0, at main `72253ae`:
- `lake build Ruliology.CellularAutomata.Rule30RightWallCloud`: no warnings. On an M5 MacBook Pro the three modules take about 2 s, 2 s and 10 s, and at most 2.7 GB, within the catalog's limit for certificate data.
- The kit's own `Check.lean --claim partial` passes all 36 headlines, 18, 12 and 6 by module: 433, 66 and 126 constants replayed, no new axioms, axioms among `propext`, `Classical.choice` and `Quot.sound`.
- The kernel rejected all ten mutations tested: a window of each lock, a rank, the rank bound, a window of the cloud, a bit of the entry row, a letter, the sweep and the rain.
- A separate plain Python replay from the literals confirms the 3,392 image checks, the letters, the ranks, the reset depths and the entry row.
- The portal form, the same proofs in one module, passes `Check` at the verifier's kit `722a0c51` with 625 constants.
- Not run: the full catalog build (`bash build_all.sh`).
- Every declaration is in the new namespace `Ruliology.CellularAutomata.Rule30RightWall`.

**Prior art.** `Rule30ResetFreeCore` and PR #60 for reset words, `Rule30GateTrap` for closed windows, `Rule30EdgeStaircases` for the rain pair. "Lock" here is not the `Lock` of the period-4 table, and "wall" is not the zero wall.

Portal entry: PENDING.

Nothing here concerns the center column or the Prize problems.
