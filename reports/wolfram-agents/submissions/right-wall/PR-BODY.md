Rule30RightWall: the wall of a rain-tailed edge code. Two letters, three locks and a closed cloud

This PR adds `lean/Ruliology/CellularAutomata/Rule30RightWall.lean`, `Rule30RightWallLocks.lean` and `Rule30RightWallCloud.lean`, their umbrella imports and a catalog entry. The catalog also records the shared namespace of the two companion modules. It builds on `Rule30FrozenRuler`: the row is the kit's edge code and one tick is the kit's `T`.

**What it proves.** A *rain tail* is an alternating tail of an edge code, and the *wall*, when present, is the last equal pair below it. Transport and nonperiodicity statements require window start `L ≥ 2`; the local wall law and three-move criterion retain their depth guards.
- `predecessor_unique`: every code has exactly one predecessor under `T`.
- `top_up`, `top_stay`, `top_minus_one`, `top_minus_two`, `top_minus_three`: the exact local rule for the wall under `T`.
- `front_back`, `front_not_periodic`: eighteen windows of eleven cells are closed under the backward tick, and a code showing one is not periodic.
- `deep_words`: three backward advances of three cells leave one of two words, `A = ..####...##` or `B = .#.###...##`. `no_BB`, `no_AAA`, `witness_ABA`: the first facts about their language. `letter_after_B`, `letter_after_A`: the next letter.
- `Reset.reset`, `Reset.above`, `Reset.again`, `Reset.letters`: a ten-cell shape containing a known reset run `0 1^(3m+1) 0` (`Rule30InverseCascade.run_resets`, PR 60) that, with rain above it, reappears three cells higher.
- `WindowClosed.Closed`, `held_forever`, `held_not_periodic`: a set of windows closed for every pair of lower cells holds a code for ever, whatever lies below, and, when the windows have width at least two and end in an equal pair, such a code is not periodic.
- `LockAB`, `LockAAB`, `LockThird`: closed sets of 4 windows of 45 cells, 6 of 136 and 40 of 175, which force the letters `AB`, `AAB` and `BAABAA` repeated. Each has a witness on an anchored row. `LockThird.no_floor`: no offset `d < 164` carries the particular shape `F(b,u,v)` in all forty windows; no exclusion of all synchronizing words is claimed.
- `Cloud.closed`, `avoids_lock`, `no_long_alternation`, `not_periodic`: a closed set of 798 windows of 45 cells that never reaches `LockAB`, on which seventeen successive letter changes are impossible.
- `Entry.entry`: one explicit anchored backward orbit entering `LockThird` while remaining in the coarse cloud.

**Infinite-family scope and checker.** The finite data certify every completion below a displayed window, at every permitted starting index and every backward time, including nonperiodicity of the entire held row. They are not a catalogue of isolated trajectories. The closed-window idea is prior art in `Rule30GateTrap`; its forward, fixed-boundary checker does not directly implement this inverse sweep, moving window and alternating continuation. Here `held_forever` supplies that general soundness theorem, and the numeric bridge verifies the finite implementation. Lock-family and cloud-family data are each consolidated in one companion module.

**Method.** The finite checks run on numbers. `run` is the backward sweep on one number with one index, and `run_back`, `next_fast` and `closed_fast` prove it equals the sweep on words. `fw` is one forward tick on a number, and `iter_fw` proves it is `T` on all bits.

**Checks**, with Lean 4.35.0, at main `72253ae`:
- `lake build Ruliology.CellularAutomata.Rule30RightWallCloud`: no warnings. On an M5 MacBook Pro the three modules take about 2 s, 2 s and 10 s, and at most 2.7 GB, within the catalog's limit for certificate data.
- The kit's own `Check.lean --claim partial` passes all 36 headlines, 18, 12 and 6 by module: 433, 66 and 126 constants replayed, no new axioms, axioms among `propext`, `Classical.choice` and `Quot.sound`.
- The kernel rejected all ten mutations tested: a window of each lock, a rank, the rank bound, a window of the cloud, a bit of the entry row, a letter, the sweep and the rain.
- A separate plain Python replay from the literals confirms the 3,392 image checks, the letters, the ranks, the reset depths and the entry row.
- The portal form, the same proofs in one module, passes `Check` at the verifier's kit `722a0c51` with 625 constants.
- Not run: the full catalog build (`bash build_all.sh`).
- The three files share namespace `Ruliology.CellularAutomata.Rule30RightWall`, as recorded in the proposed catalog namespace note.
- Source review and a second plain-Python replay passed. The only change to Lean source since these compiler/checker receipts is a correction to the base module’s header comment.

**Prior art.** `Rule30ResetFreeRuns` and `Rule30InverseCascade.run_resets` in PR #60 for reset words, `Rule30GateTrap` for closed windows, `Rule30EdgeStaircases` for the rain pair. "Lock" here is not the `Lock` of the period-4 table, and "wall" is not the zero wall.

Portal entry: PENDING.

Nothing here concerns the center column or the Prize problems.
