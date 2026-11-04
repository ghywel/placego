Rule30FourFronts: an explicit settling tick on the four left strips through wheel 87,866

This adds `lean/Ruliology/CellularAutomata/Rule30FourFrontsBase.lean` and `Rule30FourFronts.lean`, with their `public import` lines in `lean/Ruliology.lean` and a row in *Added in the kit*. It extends `Rule30FourLeftSides` (R30-20261104-458f3b) and imports it.

**What it proves.**
- `forced_front_four`: every array with the left-diagonal recurrence and a black start carries one of the four strips on every wheel `j ≤ 87,866` from strip tick `F_v(j)`, at a shift of at most 15. `F_v` is the settling recursion of `Rule30FrontLaw`, read on the strip's sixteen-row cycle.
- `forced_front_four_uniform`, `forced_front_four_left_side`, `forced_front_four_seed`: the same from strip tick 177,560, for every configuration with a leftmost black cell, and for the single black cell.
- `forced_front_low`, `forced_front_low_left_side`: through wheel 53,207 from strip tick 107,310, on `A0`.
- `classification_bounded`: the classification of `Rule30FourLeftSides` with its shift bounded by 15.
- `FA0_87866`, `FA1_87866`, `FB0_87866`, `FB1_87866`: the fronts at wheel 87,866 are 176,968, 177,229, 177,170 and 177,560.

The moves are `extend` and `branch` of `Rule30FourLeftSides` with the time carried. The values come from `walk`: from wheel `j` at tick `t`, move to wheel `j + 1` if the strip's cell is black and stay if it is white. `frun_of_walk` reads the recursion's state off four facts about the walk, and the kernel checks those facts directly. There is no data module: the rows are computed from the four literals already in `Rule30FourLeftSides`.

**Checks**, with Lean 4.35.0:
- `lake build Ruliology.CellularAutomata.Rule30FourFronts` at main `96b4f2a`: no warnings. `Rule30FourFronts` builds in 7 s at 2.1 GB on an M5 MacBook Pro, within the catalog's limit for certificate data.
- The kit's own `Check.lean --claim partial` passes the eleven headlines above: 256 constants replayed, no new axioms, axioms `propext`, `Classical.choice` and `Quot.sound`.
- The kernel rejected all four single-number mutations tested in `a_low`, `a_1` and `b1_1`.
- The four fronts agree with a separate evaluation of the recursion wheel by wheel on literal rows, in Lean on two hosts, and with a Python replay.
- The portal form, the same proofs with the imported parts repeated, passes `Check` at the verifier's kit `722a0c51` with 681 constants.
- Not run: the full catalog build (`bash build_all.sh`).
- Every declaration is in the new namespaces `Ruliology.CellularAutomata.Rule30FourFrontsBase` and `Ruliology.CellularAutomata.Rule30FourFronts`.

Portal entry: [R30-20261104-9aa447](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261104-9aa447).

Nothing here concerns the center column or the Prize problems, and 87,866 is where these rows stop, not a claim about what happens beyond it.
