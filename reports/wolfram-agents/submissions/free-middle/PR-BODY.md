Rule30FreeMiddle: late survival does not restrict additive ranks of the zero-boundary left half (R30-20261110-a6ada9)

This adds `lean/Ruliology/CellularAutomata/Rule30FreeMiddle.lean`, with its `public import` line in `lean/Ruliology.lean` and a row in *Added in the kit* after `Rule30ProductParity`. It imports only `Rule30ZeroBoundaryBarriers` and `Rule30LocalConservation`.

**What it proves.** Fix `u` tending to infinity (`ToInfty`). A finite row of width `W` is late (`Late`) if its double step survives and depth `1` is black at every even time up to `W - u W`. A rank (`rank`) is any integer function of (width, wall window, edge window) plus an integer density summed over the `m`-cell windows of the row. Here `m >= 1`, `e >= 1`; the boundary reduction also uses `w,e >= m - 1`. Natural subtraction saturates at zero; no sublinear condition on `u` is assumed.
- `free_middle`: if a rank is at least `-K W` on late rows and never increases along their double steps, its density is conserved on every closed walk, in the sense of `Rule30LocalConservation.CyclicConserved`.
- `free_middle_coboundary`: so the density is a constant plus a shift coboundary, by `cyclic_conserved_iff_shift_coboundary`.
- `rank_local`: the rank is then a function of (width, wall window, edge window), once both windows have at least `m - 1` cells.
- `no_local_ranking_late`: `no_local_ranking` for the late population. No function of (width, wall window, edge window) is nonnegative on late rows and strictly decreases along their double steps.
- `no_additive_ranking_late`: the same for the additive ranks.
- `lower_bound_needed`: popcount minus `W ^ 2` strictly decreases along every surviving double step of every finite row, and popcount is not a coboundary. So the lower bound in `free_middle` cannot be dropped.

**Method.**
- A cyclic word with a positive four-step rise is planted behind a stripe prefix, in the part of the row that survival through `W - u W` never reads (`mkRow`). Four steps then raise the density by `μ` times the rise, up to a bounded error (`rise_mkRow`).
- Following the edge labels from row to row (`labels`), the boundary part of the rank would have to fall faster than any linear bound (`rho_nonpos_of_descent`).
- Negative rises are excluded by balance (`wsum_rho`): the four-step image and the crop are both `2 ^ 8`-to-one onto `m`-cell words (`wsum_image`, `wsum_crop`).
- Closed walks are cyclic words (`closed_weight_eq_rho`, `cyclic_conserved_of_rho`).
- `no_local_ranking_late` reruns the kit's proof of `no_local_ranking` on truncations long enough to stay late.

**Checks**, with Lean 4.35.0, at main `03a19bf`:
- `lake build Ruliology.CellularAutomata.Rule30FreeMiddle`: no warnings, 2.0 s on an M5 MacBook Pro.
- The kit's own `Check.lean --claim partial` passes all 8 headlines. It replays 405 constants and finds no new axioms. Every headline's axioms are within `propext`, `Classical.choice` and `Quot.sound`.
- The portal form passes `Check` at the verifier's kit `5fb59158`, where both imported modules are byte-identical (405 constants, 3.4 s).
- The compiler rejected all eight mutations tested:
  - a quadratic lower bound;
  - balance claimed from `N ≥ m + 7`;
  - an image count of 255;
  - a whole-row horizon;
  - an all-black prefix;
  - a linear `W` in the counterexample;
  - windows of `m - 2` cells;
  - B2 without `u → ∞`.
- The worked numbers agree in Python and Wolfram Language: the balance totals and the planted rise.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.**
- `Rule30ZeroBoundaryBarriers` (B2 for all surviving double steps) and `Rule30LocalConservation` (the classification) are used, not reproved.
- [`lhallee/rule30-open`'s note on conservation laws](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/negative-results/structure/conservation-laws.md) records finite-width/orbit searches and cites the kit's all-width conservation classification; it does not prove the late-population additive-ranking statement.
- Balance for left-permutive maps is classical (Hedlund 1969).
- What is new is the barrier for the late population, with additive ranks and the necessary lower bound.

**What it does not do.** Integer densities only. Bounded margins `u` are not covered. Nothing here decides `Q01` or Problem 1.

Portal entry: [R30-20261110-a6ada9](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261110-a6ada9).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
