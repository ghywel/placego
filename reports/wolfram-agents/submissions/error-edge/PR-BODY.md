Rule30ErrorEdge: the error edge of two configurations never retreats, heals exactly at a black parent, and obeys six laws after a heal (R30-PENDING)

This adds `lean/Ruliology/CellularAutomata/Rule30ErrorEdge.lean`, with its `public import` line in `lean/Ruliology.lean` and a row in *Added in the kit*. It imports `Rule30AgedLeftDiagonals`.

**What it proves.** For two arrays with the left-diagonal recurrence, the error edge is the lowest wheel on which they differ.
- `agree_step`, `agree_after`, `edge_le`: agreement below the edge is kept, so the edge never retreats.
- `heal_iff`, `edge_stall`, `edge_heal`: the arrays agree at the edge one tick later exactly when the wheel below it is black. The black half is the recruiting step of `Rule30HealingBound`, and the white half is its converse.
- `white_above`, `black_two_above`: after a heal, the first wheel above the old edge is white if it agrees, and the second is black if both agree.
- `jump_two` to `jump_seven`: the new parent is white after a jump of exactly 2 and black after 3. It is black one tick later after 4, whatever it was. If it is white, it is black one tick later after 5 and white one tick later after 6 or 7.

**Method.** No literals. The proofs unfold the recurrence on a window of at most nine wheels and decide Boolean identities in at most thirteen variables.

**Checks**, with Lean 4.35.0, at main `5fb5915`:
- `lake build Ruliology.CellularAutomata.Rule30ErrorEdge`: no warnings, under a second for the module on an M5 MacBook Pro.
- The kit's own `Check.lean --claim partial` passes all 14 headlines: 56 constants replayed, no new axioms, axioms `propext` and `Quot.sound`.
- The kernel rejected all nine mutations tested: a flipped conclusion of each law and a dropped white-parent hypothesis.
- All the laws hold on 1,112 heals of two actual configurations over 3,000 ticks, in Python and in Wolfram Language.
- The portal form, the same proofs, passes `Check` at the verifier's kit `722a0c51`.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** `Rule30HealingBound`, `Rule30UniversalLeftSide` (`child_same`, `child_white`) and `Rule30MaskedJen.left_of_black`. The left damage front is in Wolfram (1986) and *A New Kind of Science*, p. 949.

Portal entry: PENDING.

Nothing here concerns the center column or the Prize problems.
