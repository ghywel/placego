Rule30LateTwins: from tick 46 on, every row beside the wall has a twin of the same width with the same image two ticks later (PORTAL-ID)

This adds `lean/Ruliology/CellularAutomata/Rule30LateTwins.lean`, with its `public import` line in `lean/Ruliology.lean` and a row in *Added in the kit*. It imports `Rule30ZeroBoundary` only.

**What it proves.** In `Rule30ZeroBoundary.IntegerForm`:
- `late_twin`: for every nonzero natural `y` and every `t ≥ 46`, the row `x = iter F (t - 2) y` has a twin `x' ≠ x` of the same width, with the same bit `0` and `F (F x') = iter F t y`.
- `late_twin_immortal`, `late_twin_off_orbit`: if `iter G s y` is odd for every `s` and `t` is even, then `iter G s x'` is odd for every `s` too, and `x'` is none of the rows `iter G j y`.
- `F_shiftRight`, `iter_F_shiftRight`: `F Y >>> (m + 1) = R (Y >>> m)` for every `Y` and `m`, with `R u = (u >>> 2) ^^^ ((u >>> 1) ||| u)`.
- `band_settles`, `band_late`: from any start whose top cell is the twentieth, the top twenty cells are on one four-cycle after 26 ticks; so every nonzero row's top twenty cells are on it from tick 45.
- `sync`, `twin_of_factors`: the words `0 1 0` and `0 1111 0` make two runs of `back` agree; two such words, stacked in consecutive rows, give the twin.

**Method.** The settling is two `decide +kernel` stages, over 4,096 and 512 cases, through a binary-split checker that keeps the kernel's recursion shallow. Everything else is short bit arithmetic on top of `back`, `eq_back`, `zrow_back`, `zrow_rowOfNat_one` and `testBit_F_succ_of_top`.

**Checks**, with Lean 4.35.0, at main `48d8fbbc`:
- `lake build Ruliology.CellularAutomata.Rule30LateTwins`: no warnings; under three seconds for the module on an M5 MacBook Pro, kernel stages included.
- The kit's own `Check.lean --claim partial` passes all 9 headlines: 143 constants replayed, no new axioms, axioms within `propext`, `Classical.choice`, `Quot.sound`.
- The compiler rejected all seven mutations tested, among them onset `45` for `46`, and `11` for `12` ticks in the second stage in all four phases.
- The worked numbers agree in Python and Wolfram Language: both stage maxima, and an actual twin at `t = 46` for seven rows.
- The portal form, the same proofs, passes `Check` at the verifier's kit `5fb59158`.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** The reset words come from Feynman's theorem on predecessors (`Rule30Predecessors`, `predCount_eq_one_iff`). Stacking resets across many rows is the inverse-cascade argument of kit PR #60 (`scheduled_cascade_closes`), which assumes them; here every late row is shown to supply two, from an explicit tick. `Rule30PrefixMerger` gives a fixed seven-cell rewrite beside the wall that merges after two ticks. The settling of the top is a small explicit case of `Rule30UniversalLeftSide` and `Rule30FourLeftSides`.

**What it does not do.** A twin has the same future as its row two ticks later, so the twins add rows, not futures. Nothing here bounds a death time or proves `Q01`.

Portal entry: [PORTAL-ID](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/PORTAL-ID).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
