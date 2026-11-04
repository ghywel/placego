Rule30UniversalLeftSide: one left side through wheel 53,207 for every configuration with a leftmost black cell, and the first fork realized

This adds `lean/Ruliology/CellularAutomata/Rule30UniversalLeftSide.lean`, with its `public import` in `lean/Ruliology.lean` and a row in *Added in the kit*.

**What it proves.** Rowland (*Local nested structure in rule 30*, 2006, §5) conjectured that rule 30 has only one left side, and located the first possible failure at his column 53,209, which is wheel 53,208 here.
- `universal_of_strip`: for every array with the left-diagonal recurrence (`Rule30AgedLeftDiagonals.Recurrence`) and a black wheel 0, and every strip whose wheels at each step have blacks arbitrarily late or a period of the lower words that is an antiperiod of the child, one time shift aligns every wheel through `J` with the strip. This is Rowland's induction.
- `universal_left_side`: every configuration with a leftmost black cell, whatever lies to its right, carries the strip `C` on every wheel through 53,207 after one shift. `one_left_side`: any two such configurations share their left side through 53,207 up to a shift. `seed_left_side`: so does the single black cell.
- `fork_dichotomy`: with that shift, wheel 53,208 of every such configuration is eventually `C`'s word or its complement.
- `first_fork`: the finite rows `B` and `B'` (`B` with bit 53,208 flipped) agree on every wheel through 53,207 and are complementary on wheel 53,208 at every tick, and no time shift relates them. `left_side_not_unique`: some finite row differs from the single seed there; the proof does not say which of the two.
- `odd_farther_weights`, `even_farther_weight`: Rowland's parity condition at the five white wheels.

The reference is one 53,209-bit literal `B` that returns after sixteen ticks (`B_return`), so every condition is a kernel evaluation over sixteen rows. No table of cycles and no run of the seed is needed. That `B` is the single seed's row at tick 72,000 is a replayed computation and is not used in any proof.

**Checks**, Lean 4.35.0:
@@CHECKS@@
- Every declaration is in the new namespace `Ruliology.CellularAutomata.Rule30UniversalLeftSide`.

Portal entry: @@ENTRY@@.

Nothing here concerns the center column or the Prize problems. Credits: Rowland's argument; the kit's `Rule30LeftReset`, `Rule30FiniteDiagonals` and `Rule30AgedLeftDiagonals`; Bosdure's universal left-edge crystal (R30-20261027-317c64) for wheels through 7.
