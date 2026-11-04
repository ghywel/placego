Rule30FourLeftSides: exactly four left sides through wheel 87,866

This adds `lean/Ruliology/CellularAutomata/Rule30FourLeftSides.lean`, with its `public import` in `lean/Ruliology.lean` and a row in *Added in the kit*. It extends `Rule30UniversalLeftSide` (R30-20261104-309041) and imports it.

**What it proves.**
- `left_side_classification`: every configuration with a leftmost black cell, whatever lies to its right, eventually agrees with one of four explicit strips on all left diagonals through wheel 87,866, with one common time shift.
- `exactly_four_left_sides`, `four_distinct`, `on_exactly_one`: the four strips are realized by finite rows, no two are related by a time shift, and each configuration is on exactly one.
- `odd_reaches_one_of_four`, `least_period_16`: iterating `v ↦ 4 v ⊕ (2 v ∨ v)` modulo `2 ^ 87867` from any odd `v` reaches `A0`, `A1`, `B0` or `B1`, each of least period 16.
- `seed_classified`: the single black cell is on one of the four; the proof does not say which. A separate replay identifies it with `A0`.
- `fork_weights`: the farther words at the three forks have weights 6, 10, 10 over 16.

The proof applies two moves along the tree of forks at wheels 53,208, 58,287 and 72,576: `extend` (a nearer word with blacks arbitrarily late continues an alignment with the same shift) and `branch` (a white wheel leaves the strip's word or its complement). The checked black windows between forks make the list exhaustive. The rows are one literal and three high-part differences, and every data condition is a kernel evaluation over sixteen rows. Rowland located these forks; the record's computations (sections 8.31 and 8.60, and GC2635) found the four rows and the tree.

**Checks**, with Lean 4.35.0:
- @@FULLBUILD@@
- `lake build Ruliology.CellularAutomata.Rule30FourLeftSides` at main `2b623385`: no warnings. The kit's own `Check.lean --claim partial` passes eight headlines there: 220 constants replayed, no new axioms, axioms within `propext`, `Classical.choice` and `Quot.sound`.
- The portal form, the same proofs with the imported part repeated, passes `Check` at the verifier's kit `722a0c51` on two hosts, with 272 constants. Everything after the imported part is byte-identical in both forms.
- Not run: the full catalog build (`bash build_all.sh`).
- Every declaration is in the new namespace `Ruliology.CellularAutomata.Rule30FourLeftSides`.

Portal entry: [@@ENTRY@@](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/@@ENTRY@@).

Nothing here concerns the center column or the Prize problems, and 87,866 is where these rows stop, not a claim about what happens beyond it.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
