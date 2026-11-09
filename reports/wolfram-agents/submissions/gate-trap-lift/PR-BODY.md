Rule30GateTrapLift: at eighteen columns the gate trap forbids 3535353, and Q01GapCore (PORTAL-ID)

This adds `lean/Ruliology/CellularAutomata/Rule30GateTrapLift.lean`, with its `public import` line in `lean/Ruliology.lean` and a row in *Added in the kit* after `Rule30GateTrapWords`. It imports only `Rule30GateTrapWords`.

**What it proves.** `Rule30GateTrapWords` excludes the gap words `333`, `3353`, `3533`, `3553` and `5533` after entry into the gate trap; these are all that the trap's sixteen-column graph forbids, and that graph reads `3535353`.
- `win18_eq`, `win18_step2`: an 18-column window at an odd time is the trap's window followed by the columns `17` and `18`. Two steps later it is the kit's `step2` of it, with the two values of column `19` as exterior inputs. So the lift of the trap by two columns is closed, and every trapped right half stays in it.
- `no_3535353_of_entry`: if the window of `R` is in `trap` at an odd time `t0`, then `u R` never reads `3, 5, 3, 5, 3, 5, 3` from a step `s` with `t0 ≤ 2 s + 1`.
- `trap_reads_3535353`: an explicit path of the sixteen-column trap graph reads it, so the lift is needed.
- `lift_minimal_paths`: it is minimal for the lift. `353535` and `535353` are read along explicit lift paths.
- `Q01GapCore` (open) is `Q01GapWords` with `3535353` excluded as well.
  - `Q01GapCore_of_Q01GapWords`: `Q01GapWords` implies it.
  - `not_finSupp_Psi_of_Q01GapCore`: it still gives `¬ FinSupp (Psi R)` for every right half whose window enters the trap.
  - `CQ01Empty_of_Q01GapCore`: hence `CQ01Empty`.

**Method.** The method is `Rule30GateTrapWords`'s. The path sets of `3535353` in the lift, from all 752 black lift windows, are given as data: 27 nonempty layers, 4,644 windows in all. The kernel checks that the double step takes each layer into the next for every value of column `19`, and that the last layer is empty (`wordCheck18`, `not_reads18_of_check`). Each layer is split into chunks of at most 192 windows, one `decide +kernel` each, so that the kernel's caches stay small.

**Checks**, with Lean 4.35.0, at main `03a19bf`:
- `lake build Ruliology.CellularAutomata.Rule30GateTrapLift`: no warnings, 38 s and 1.2 GB on an M5 MacBook Pro.
- The kit's own `Check.lean --claim partial` passes all 7 headlines. It replays 202 constants and finds no new axioms; every headline's axioms are within `propext`, `Classical.choice`, `Quot.sound`.
- The portal form passes `Check` at the verifier's kit `5fb59158`: 422 constants. Because that kit predates `Rule30GateTrapWords`, the portal form carries that module's reviewed source verbatim.
- The compiler rejected all seven mutations tested: a window dropped from a layer chunk and from a middle layer, a white start, the final empty layer removed, a layer shifted by one bit, and corrupted start windows for the 16-column and lift paths.
- The worked numbers agree in Python and Wolfram Language: the lift's closure (3,316 windows, 13,264 of 13,264 edges), the layers of `3535353` in the trap and in the lift, and the minimal forbidden gap words of up to eight gaps at both widths.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** [R30-20261030-60990f](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261030-60990f) (J. Lee) proves that `33`, `3553` and `3535353` never occur at any index for the trajectories of an invariant pool of 18-cell windows, among them the one-cell right seed. Here the premise is entry into the kit's whole trap, whose transients can read `33` once. What is new is `3535353` for every right half that enters the kit's trap, its minimality for the lift, and `Q01GapCore`.

**What it does not do.** None of `Q01Gap`, `Q01GapWords`, `Q01GapCore`, `CQ01`, `CQ01Empty` or the absence of period 2 is proved.

Portal entry: [PORTAL-ID](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/PORTAL-ID).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
