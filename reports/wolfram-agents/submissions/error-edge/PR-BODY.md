Rule30ErrorEdge: the error edge of two configurations never retreats, heals exactly at a black parent, and obeys six laws after a heal (R30-20261105-0c74ef)

This adds `lean/Ruliology/CellularAutomata/Rule30ErrorEdge.lean`, with its `public import` line in `lean/Ruliology.lean` and a row in *Added in the kit*. It imports `Rule30AgedLeftDiagonals`.

**What it proves.** For two arrays with the left-diagonal recurrence, the error edge, when present, is the lowest wheel on which they differ. The heal criterion requires its index to be at least 1; the post-heal laws require the old edge to be at least 2.
- `agree_step`, `agree_after`, `edge_le`: agreement below the edge is kept, so the edge never retreats.
- `heal_iff`, `edge_stall`, `edge_heal`: the arrays agree at the edge one tick later exactly when the wheel below it is black. A heal can eliminate the difference entirely. Black-parent absorption is the recruiting step of `Rule30HealingBound`; white-parent memory already occurs inside `Rule30UniversalLeftSide.child_white`. The exact interior Boolean criterion is `Rule30LightCone.rule_flip_right_iff` (PR 98), here restated at an error edge, with wheel 1’s boundary case included.
- `white_above`, `black_two_above`: after a heal, the first wheel above the old edge is white if it agrees, and the second is black if both agree.
- `jump_two` to `jump_seven`: the new parent is white after a jump of exactly 2 and black after 3. It is black one tick later after 4, whatever it was. If it is white, it is black one tick later after 5 and white one tick later after 6 or 7.

**Method.** No literals. The proofs unfold the recurrence on a window of at most nine wheels and decide Boolean identities in at most thirteen variables.

**Checks**, with Lean 4.35.0, at main `e0e5099`:
- `lake build Ruliology.CellularAutomata.Rule30ErrorEdge`: no warnings, under a second for the module on an M5 MacBook Pro.
- The kit's own `Check.lean --claim partial` passes all 14 headlines: 56 constants replayed, no new axioms, axioms `propext` and `Quot.sound`.
- The kernel rejected all nine mutations tested: a flipped conclusion of each law and a dropped white-parent hypothesis.
- The six jump laws hold on 1,112 heals of two actual configurations evolved for 3,000 ticks; the control tests transitions t=0,…,2998 in Python and Wolfram Language.
- The portal form, the same proofs, passes `Check` at the verifier's kit `5fb59158`.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** `Rule30LightCone.rule_flip_right_iff` (PR 98), `Rule30HealingBound`, `Rule30UniversalLeftSide` (`child_same`, `child_white`) and `Rule30MaskedJen.left_of_black`. The left damage front is in Wolfram (1986) and *A New Kind of Science*, p. 949.

Portal entry: [R30-20261105-0c74ef](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261105-0c74ef).

Nothing here concerns the center column or the Prize problems.
