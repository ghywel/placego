Rule30SeparatorQ01: the constant-tail separator is Q01 for free bits without two adjacent whites, and BWH is a death-time bound (R30-20261108-752db6)

This adds `lean/Ruliology/CellularAutomata/Rule30SeparatorQ01.lean`, with its `public import` line in `lean/Ruliology.lean` and a row in *Added in the kit*. It imports `Rule30SEPToPeriodTwo`, `Rule30GateTrap` and `Rule30ZeroBoundarySmall`.

On #76 the maintainers asked how `BWH`, `RW` and `SEP` relate to `Rule30PeriodTwo.Q01`, and asked for the implications that hold to be proved. The docstrings now say that none is known. This module proves the relations for `SEP` and `BWH`.

**What it proves.**
- `cone_chart`, `peel_chart`: for a zero-boundary start `L` whose depth `1` is black at the even ticks up to `2 S`, the inverse cone of the endpoint stream `zEnd L j = zpair L (2 j + 1) 1` is the run of `L`. Precisely, `cone (zEnd L) n j = zpair L (2 j + n) (n + 2)` and `peelPow d (inverse (zEnd L)) t = zpair L t (2 d + t + 2)` for `j + n ≤ S` and `t + d ≤ S`. This is `actual_cone_chart` in zero-boundary coordinates, with no right half.
- `hardCore_endOf_iff`, `zEnd_Theta`: the endpoint of `Theta f` is hard-core exactly when `f` has no two adjacent white bits.
- `sep_iff_QN`, `orbitSeparator_iff_QN`: `ConstantTailSeparator` holds iff `Theta f` is never finitely supported when `f` has no two adjacent white bits.
- `Q01_iff_sep_and`: `Q01` holds iff `SEP` holds and no finitely supported `Theta f` has free bits meeting two adjacent whites infinitely often. In particular `Q01_sep`.
- `sep_Q01Gap`, `sep_CQ01Empty`: `SEP` implies `Q01Gap`, hence `CQ01Empty`.
- `sep_iff_LR1`, `layerWord_realizes`, `layerWord_no11`: the words of a single column beside the alternating column, at the white ticks, with any start cell and any input from column `2`, are exactly the words with no two adjacent black bits. `SEP` is equivalent to no such layer having a finitely supported forced left row. `sep_CQ01` follows; it is `constant_separator_excludes_alternating` in the sideways coordinates.
- `bwh_iff_deathBounds`: `BWH` holds iff every start of exact even width `W ≥ 16` dies by tick `2 W` and every start of exact odd width `W ≥ 17` with its top two cells black dies by tick `2 W - 2`. The dictionary in both directions is `wedge_of_row_two`, `wedge_of_row_three` and `row_of_wedge`.
- `bwh_death`, `bwh_Q01`: under `BWH`, every start supported at depths `≤ W` with `W ≥ 16` has a white depth-`1` cell at some even tick `≤ 2 W + 4`, and `Q01` follows.
- Controls, by `decide +kernel` on natural numbers: `odd_guard_needed` (the start `272125`, of exact width `19` with a white cell at depth `18`, survives to tick `36`) and `even_threshold_needed` (the start `11083`, of exact width `14`, survives to tick `30`). Also `black_tick_control`.

**Checks**, with Lean 4.35.0, at main `48d8fbbc`, and after rebasing onto main `12ddd22` (`Check` rerun there, same result):
- `lake build Ruliology.CellularAutomata.Rule30SeparatorQ01`: no warnings, under half a second for the module on an M5 MacBook Pro.
- The kit's own `Check.lean --claim partial` passes all 17 headlines. It replays 164 constants and finds no new axioms; every headline's axioms are within `propext`, `Classical.choice`, `Quot.sound`.
- The compiler rejected all ten mutations tested. Three state something false and fail in `decide`: a tail symbol `1`, and each control witness one tick longer. The two dropped-guard mutations state what the controls refute.
- The worked numbers agree in Python and Wolfram Language: both controls' death ticks, the peel chart at all 136 pairs `t + d ≤ 15` on the start `11083`, and the layer-word counts `2, 3, 5, 8, 13, 21`.
- The portal form, with the same proofs, passes `Check` at the verifier's kit `5fb59158`.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** The chart, `Q01 ⇒ ConstantTailSeparator` and `BWH ⇒ Q01` are in the external development [`lhallee/rule30-open`](https://github.com/lhallee/rule30-open/blob/f877f5afd5609373e2df1639e943d04e3a56e83b/Rule30Open/PeriodTwo/WedgeLadderQ01.lean) (`zcone_chart`, `zpeel_chart`, `binaryCTS_iff_Q01`, `q01_constantTailSeparator`, `bwh_Q01`). They are reproved here in the kit's coordinates. Its [`WedgeLadder.md`](https://github.com/lhallee/rule30-open/blob/f877f5afd5609373e2df1639e943d04e3a56e83b/Rule30Open/PeriodTwo/WedgeLadder.md), section “BWH is the kit's Q01 at a linear horizon (computed)”, also states the exact-width death-time interpretation with both horizons and the top-two-black guard, and checks it through `n = 12`; it says that finite form is not in Lean. `bwh_iff_deathBounds` formalizes that known interpretation in both directions, and `bwh_death` gives the at-most-width consequence. The hard-core class, `Q01Gap` implication and layers are additional to that development. The hypotheses and their period-two consequences are from #76, #84, #86 and #101; `Q01Gap` is from #64.

**What it does not do.** None of `SEP`, `BWH` or `Q01` is proved. Whether `SEP` implies `Q01` is left exactly as open as whether a finite constrained start can have free bits meeting two adjacent whites infinitely often. The docstrings of `Rule30WedgeBridge`, `Rule30SeparatorEquivalences` and `Rule30SEPToPeriodTwo`, and the README's period-2 row, still say that no relation with `Q01` is known. They are left to you to update, if you wish.

Portal entry: [R30-20261108-752db6](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261108-752db6).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
