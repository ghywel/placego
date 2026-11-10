Rule30FiveColumnBound: a sharp five-column black-count ceiling (PORTAL-ID)

This adds `lean/Ruliology/CellularAutomata/Rule30FiveColumnBound.lean`, with its `public import` line in `lean/Ruliology.lean` after `Rule30Realization` and a row in *Added in the kit* after `Rule30LightCone`. It imports `Rule30Prize` and `Rule30Realization`, and uses the official `Rule30Jen.rule`, the arbitrary-row evolution `Rule30Realization.evol` and the singleton diagram `cell`.

**What it proves.** For every configuration, every starting time and every five adjacent physical columns, the black count over an interval of `T` ticks is at most `3 * T + 2`. The interval includes its first row and excludes its endpoint, and `T = 0` is allowed.
- `potential_bounds`, `local_potential`: the potential `H(u) = max(0, 2 - pop(right four cells of u))` has range `0..2`. `pop(u) - 3 ≤ H(v) - H(u)` holds for the update `v` of the middle five of any seven cells, with both exterior cells free; all seven input bits are checked in the kernel.
- `telescope`, `five_column_bound`: along any trajectory, `count ≤ 3 * T + H(final) - H(initial) ≤ 3 * T + 2`.
- `white_column_bound`: the same window has at least `2 * T - 2` white cells.
- `evol_five_column_bound`, `cell_five_column_bound`: the bound for every initial row and starting time, and for the official singleton.
- `sharp_constant`, `sharp_rate`: both constants are sharp on actual rows. An all-black window gives `5` at `T = 1`, and the fixed alternating row gives exactly `3 * T` at every horizon.

**Checks**, with Lean 4.35.0, at main `03a19bf`:
- `lake build Ruliology.CellularAutomata.Rule30FiveColumnBound`: no warnings.
- The kit's own `Check.lean --claim partial` passes all 9 headlines, with 62 constants and no new axioms.
- The portal form passes `Check` at the verifier's kit `5fb59158`.
- The worked numbers agree in Python and Wolfram Language. All 128 seven-cell windows satisfy the inequality, 70 of them with equality. Three wrong controls fail as predicted: the mirrored potential on 8 windows, the potential zeroed at the all-white word on 3, and rule 150 on 16.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** Summing local inequalities and telescoping a bounded potential is a standard method. Related inequalities for different observables are `rule30-open`'s [ColumnTransfer](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/Rule30Open/Columns/ColumnTransfer.lean) and the source-dependent one-column bound of [#253](https://github.com/WolframInstitute/Rule30PrizeKit/pull/253). Earlier spin and population bookkeeping, and Cappallo's counting formula in [OEIS A070952](https://oeis.org/A070952), are context, not new results here.

**What it does not do.** It bounds a sum over five columns. It gives no density bound for an individual column, no positive lower density, no improvement for the single seed, and no prize result.

Portal entry: [PORTAL-ID](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/PORTAL-ID).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
