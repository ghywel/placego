Rule30UniversalLeftSide: one left side through wheel 53,207 for every configuration with a leftmost black cell, and the first fork realized

This adds `lean/Ruliology/CellularAutomata/Rule30UniversalLeftSide.lean`, with its `public import` in `lean/Ruliology.lean` and a row in *Added in the kit*.

**What it proves.** Rowland (*Local nested structure in rule 30*, 2006, §5) asked whether the eventual left-diagonal periods are independent of the initial row. He identified an even-weight integral whose two possible child words are complements. His child column 53,209 is zero-based wheel 53,208 here. These results concern the words under a common time shift; the two complementary words have the same least period.
- `universal_of_strip`: for every array with the left-diagonal recurrence (`Rule30AgedLeftDiagonals.Recurrence`) and a black wheel 0, and every reference strip with black base words, the stated recurrence, and either arbitrarily late black bits on each nearer parent or a common period of the lower words that is an antiperiod of the child, one time shift aligns every wheel through `J` with the strip. This is Rowland's induction.
- `universal_left_side`: every configuration with a leftmost black cell, whatever lies to its right, carries the strip `C` on every wheel through 53,207 after one shift. `one_left_side`: any two such configurations share their left side through 53,207 up to a shift. `seed_left_side`: so does the single black cell.
- `fork_dichotomy`: with that shift, wheel 53,208 of every such configuration is eventually `C`'s word or its complement.
- `first_fork`: the finite rows `B` and `B'` (`B` with bit 53,208 flipped) agree on every wheel through 53,207 and are complementary on wheel 53,208 at every tick, and no common shift aligns their entire prefixes through 53,208. `left_side_not_unique` proves that at least one of these finite rows differs from the singleton through 53,208 under every shift, without identifying which row.
- `odd_farther_weights`, `even_farther_weight`: Rowland's parity condition at the five white wheels.

The sixteen-tick return of the literal `B` in the 53,209-wheel register is kernel-checked (`B_return`). A separate replay identifies it with the singleton’s wall-frame row at tick 72,000 truncated to the low 53,209 bits. The proof uses the literal and its verified return independently of that computation.

**Checks**, with Lean 4.35.0:
- The kit's own `Check.lean --claim partial` passes all nine headlines on this module at main `a91c7273`, and on its portal form at the verifier's kit `722a0c51`. Each run replays 193 constants with no new axioms; the headline axioms are within `propext`, `Classical.choice` and `Quot.sound`. The portal form passes at `722a0c51` on three hosts (macOS arm64, macOS Intel, Linux); this module passes at `a91c7273` on the two macOS hosts and at `722a0c51` on Linux.
- `lake build Ruliology` with this module and its import line completes at `722a0c51`: 206 jobs, exit 0, no warning from this module. On a 15 GiB Linux host the existing 52-wide certificate chunk modules had to be built one at a time first, each peaking near 12.8 GB; they are unrelated to this module.
- That full build was not repeated at `a91c7273`, which changes only `Rule30CoupledGerms`, `Rule30PeriodFourSkeleton`, `Rule30ZeroBoundary` and the README. At that commit this module and its import closure build and pass `Check`.
- Not run: the full catalog build (`bash build_all.sh`).
- Every declaration is in the new namespace `Ruliology.CellularAutomata.Rule30UniversalLeftSide`.

Portal entry: [@@ENTRY@@](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/@@ENTRY@@).

Nothing here concerns the center column or the Prize problems. Credits: Rowland's argument; the kit's `Rule30LeftReset`, `Rule30FiniteDiagonals` and `Rule30AgedLeftDiagonals`; Bosdure's universal left-edge crystal (R30-20261027-317c64) for wheels through 7.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
