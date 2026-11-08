Rule30SidewaysLocks: locks of period five and seven give CQ01 for every right half that enters them (R30-20261108-c1d531)

This adds `lean/Ruliology/CellularAutomata/Rule30SidewaysLocks.lean`, with its `public import` line in `lean/Ruliology.lean` and a row in *Added in the kit*. It imports `Rule30GateTrap` only.

**What it proves.** For the right half `R` driven by the alternating column (`altCol`), with `u R` and `Psi R` as in `Rule30PeriodTwoSideways`:
- `winW_dstep`: from an odd tick, the columns `1..W` two ticks later are `dstep` of the columns `1..W` and the two cells of columns `W + 1`, `W + 2`. Nothing else enters.
- `lockCheck`, `lock_forever`: a lock is `p` classes of windows, checked by computing every double step for the four values of the two outer cells. A window in class `k` at an odd tick is in class `k + n` two `n` ticks later.
- `u_of_lock`, `u_eventuallyPeriodic_of_lock`, `not_finSupp_Psi_of_lock`: column `1` then repeats the lock's word, and `Psi R` is infinite, by `not_finSupp_Psi_of_eventuallyPeriodic`. This holds for every `R`, finite or not.
- `lock5_ok`, `lock7_ok`, `lock7b_ok`, all `decide +kernel`:
  - width `34`, `25` windows in `5` classes, word `10000`;
  - width `30`, `66` windows in `7` classes, word `0101000`;
  - width `45`, `33` windows in `7` classes, word `0010100`.
- `lock5_entry`, `lock7_entry`, `lock7b_entry`: the right halves `28998`, `1891` and `3793493` enter at ticks `15`, `27` and `29`, computed by the kit's `evolve`.
- `winW_prefix`, `CQ01_lock5_family`, `CQ01_lock7_family`, `CQ01_lock7b_family`: the window at tick `t0` depends only on the first `W + t0` cells. So every right half sharing the first `49`, `57` or `74` cells of a witness satisfies `CQ01`, whatever its later cells.
- `lock5_win_trap`: the period-five lock lies inside `Rule30GateTrap.trap`. There `CQ01` is otherwise conditional on `Q01Gap`; inside `lock5` every gap of `u R` is `5`, and `CQ01` holds with no hypothesis.
- `u_28998`: `u` of `28998` reads `10000` from step `7` on.

**Checks**, with Lean 4.35.0, at main `48d8fbbc`:
- `lake build Ruliology.CellularAutomata.Rule30SidewaysLocks`: no warnings, about five seconds for the module on an M5 MacBook Pro, kernel checks included.
- The kit's own `Check.lean --claim partial` passes all 17 headlines. It replays 70 constants and finds no new axioms; the headlines' axioms are within `propext`, `Classical.choice` and `Quot.sound`.
- The compiler rejected all nine mutations tested. Seven fail in `decide` on a false statement: a wrong word, period `4`, a window removed, the word of the other period-seven lock, an entry two ticks early, an entry in the wrong class, and column `W + 1` taken as free at both ticks. That last is the freer model of `Rule30GateTrap`, in which none of the three sets closes.
- The worked numbers agree in Python and Wolfram Language: for each lock its window count, period and word, zero failed transitions in the two-cell model against `2, 1, 2` in the freer model, and the witnesses' entry ticks.
- The portal form, with the same proofs, passes `Check` at the verifier's kit `5fb59158`.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** The method is that of `Rule30GateTrap` (#64): kernel-checked closed sets of windows, read on column `1`. The external development [`lhallee/rule30-open`](https://github.com/lhallee/rule30-open) has a period-seven lock, `SevenLock`: `195` windows of `32` columns, closed with column `33` free at both ticks, word `0101000`. Cut to `30` columns its windows are `65` of the `66` windows of `lock7`, so `lock7` is that lock with the two-cell step, reproved here. `lock5` and `lock7b` share no window with it. The prefix families follow portal entry R30-20261024-8d7751, which does the same for the ether-and-wall trap.

**What it does not do.** Nothing here decides `CQ01`, `CQ01Empty` or the general question of whether every right half enters a trap or lock. The gate trap's restriction on the order of gaps is not treated.

Portal entry: [R30-20261108-c1d531](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261108-c1d531).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
