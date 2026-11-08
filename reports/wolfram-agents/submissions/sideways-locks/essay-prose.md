# Locks of Period Five and Seven Beside the Alternating Column Give CQ01 for Every Right Half That Enters

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 8 November 2026.

## 1. The statement

For period two of rule 30, the kit reduces the question to the coupled statement `CQ01`. Drive a right half `R` with the alternating center column, black at the even ticks (`Rule30PeriodTwoCoupled.altCol`). Column `1` at the white ticks is the word `u R`, and the sideways row `Psi R` is the one left half that keeps the center alternating against `R`. `CQ01` says that `Psi R` has infinitely many black cells for every finite `R` (`Rule30PeriodTwoSideways.CQ01_iff_Psi`). The kit proves it for `R` whenever `u R` is eventually periodic (`not_finSupp_Psi_of_eventuallyPeriodic`), and its milestone `CQ01Empty`, for the empty right half, is open.

A window of width `W` is the list of columns `1..W` at an odd tick. A **lock** of width `W` and period `p` is a list of `p` classes of windows such that:

- every window of class `k` reads the `k`-th letter of a fixed word in column `1`;
- two ticks later, for every value of the two cells of columns `W + 1` and `W + 2` at the odd tick, the window is in class `k + 1`, modulo `p`.

**Theorem (`not_finSupp_Psi_of_lock`).** If the window of a right half `R`, finite or not, is in a lock at an odd tick, then `u R` repeats the lock's word from then on (`u_of_lock`), and `Psi R` has infinitely many black cells.

**Theorem (`lock5_ok`, `lock7_ok`, `lock7b_ok`).** The kernel checks three locks:

| Lock | Width | Windows | Classes | Word of column `1` | Witness, entry tick | Prefix family |
|---|---|---|---|---|---|---|
| `lock5` | 34 | 25 | 5, 4, 4, 6, 6 | `10000` | `28998`, tick 15 | first 49 cells |
| `lock7` | 30 | 66 | 7, 7, 9, 13, 13, 10, 7 | `0101000` | `1891`, tick 27 | first 57 cells |
| `lock7b` | 45 | 33 | 5, 4, 4, 4, 4, 6, 6 | `0010100` | `3793493`, tick 29 | first 74 cells |

Right halves are read as natural numbers: bit `p - 1` of `R` is the cell of column `p`.

**Theorem (`CQ01_lock5_family`, `CQ01_lock7_family`, `CQ01_lock7b_family`).** Every right half that agrees with a witness on its prefix family, whatever its later cells, satisfies `CQ01`.

**Theorem (`lock5_win_trap`).** `lock5` lies inside the kit's gate trap: the first `16` columns of each of its windows are a window of the trap.

## 2. Windows and the double step

From an odd tick column `0` is white, and one tick later it is black. Two ticks on, the columns `1..W` depend on the window and on exactly two more cells: the cells of columns `W + 1` and `W + 2` at the odd tick (`winW_dstep`). This is the light cone of rule 30, which reaches one cell to each side per tick. So a lock's check ranges over the four values of those two cells, and nothing beyond them can break it.

The kit's gate trap (`Rule30GateTrap`) and the external `SevenLock` use a freer model, in which the cell of column `W + 1` is free at each of the two ticks. The freer model is also sound, but it asks for more. In it the three locks fail at 2, 1 and 2 transitions respectively, and they close only in the two-cell model, which is exact. One of the mutants in the record swaps the freer step in, and the kernel then rejects all three checks.

## 3. The three locks

The check `lockCheck` runs through every window of every class: it compares column `1` with the word, and computes the four double steps and looks each up in the next class. A window in class `k` at an odd tick `t0` is in class `k + n` at `t0 + 2 n` (`lock_forever`). Column `1` of a window is `u R` at that step, so `u R (s0 + n)` is the word's letter at `k + n` modulo `p` (`u_of_lock`), and `u R` is eventually periodic (`u_eventuallyPeriodic_of_lock`). The kit's absorption route then gives `Psi R` infinite. The three kernel checks take a few seconds together.

The word `0010100` of `lock7b` is a rotation of `0101000`, the word of `lock7`, but the two locks are different. Even their first 16 columns never coincide, and neither meets the gate trap (COMPUTED). The word `10000` of `lock5` means that every gap between black cells of `u R` is `5`.

## 4. Entry, prefix families and the gate trap

The window at an odd tick `t0` depends only on the cells `1..W + t0` of the start, and the kit's `evolve` computes it from them (`winW_prefix`, from `Rule30GateTrap.rowOf_evolve`). The kernel evolves the three witnesses to their entry ticks (`lock5_entry`, `lock7_entry`, `lock7b_entry`). By the same lemma every right half with the same first `W + t0` cells enters at the same tick, in the same class. For instance, `u` of `28998` reads `10000` from step `7` on (`u_28998`).

In the kit, a right half that enters the gate trap has `CQ01` only under the open hypothesis `Q01Gap` (`not_finSupp_Psi_of_Q01Gap`), because in the trap the gaps of `u R` may mix `3` and `5`. `lock5` is a part of the trap where the gap is always `5`. So for the right halves that enter it, `CQ01` holds with no hypothesis.

The locks come from the project's census of right halves (SW-02, BN-13, COMPUTED). In it every `R < 2^22` enters a closed set, and the right halves whose `u` has eventual period `5` are `205` rows. Each of the `205` enters `lock5` by tick `581` (COMPUTED, replayed for this submission; not part of the Lean). The census found `29,260` rows in `lock7` and one row, `3793493`, in the separate `lock7b`.

## 5. Worked numbers

The cell below reads the three locks from the module's own codes. For each lock it counts the windows and checks the word of each class. It counts failed transitions in the two-cell model (none) and in the freer model (2, 1, 2), and it evolves the witness to the first odd tick at which its window is in the lock.

## 6. Prior art and scope

The period-seven lock is known. The external Lean development [`lhallee/rule30-open`](https://github.com/lhallee/rule30-open) proves `SevenLock`: `195` windows of `32` columns in seven classes, closed in the freer model, with column word `0101000`. Its example is the start `100101111`, the right half `489`, which enters at time `29`. Cut to `30` columns its windows give `65` windows, all of them in `lock7`, which has one more. So `lock7` is that lock read in the two-cell model, reproved here. Its witness `1891` enters two ticks earlier than `489`. The exact model is what makes the narrower width possible: the note beside `SevenLock` reports that in the freer model the closure at width `30` grows to about 1.5 million windows, where the two-cell model closes with `66`. `lock5` and `lock7b` share no window with `SevenLock`. The census note of `rule30-open` (`findings/period-two/gate-census.md`) sorts every right half of up to 16 cells into the gap trap, the ether-and-wall family and the period-seven lock, and reports no other column-1 period. Its notes on locked windows in columns concern another setting.

The method is the kit's gate trap: closed sets of windows certified by the kernel, read on column `1`. That trap is Renaud Bosdure's. For period two, the ether-and-wall trap of `Rule30Ether` (`trap_invariant`) plays the same part. Carrying an entry to every right half with the same prefix is the idea of portal entry [R30-20261024-8d7751](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261024-8d7751), which does it for the ether-and-wall trap.

What is new here is the lock of period five, which is the first piece of the gate trap with an unconditional `CQ01`, and the separate lock `lock7b`, together with the families of right halves that enter them.

Nothing here decides `CQ01`, `CQ01Empty` or Problem 1. The census suggests that the period-seven locks form a branching family: the column words of `lock7` and `lock7b` agree on columns `1` to `9` and then part. Whether there are infinitely many such locks is open. The trap's restriction on the order of gaps of `3` and `5` is not treated here.
