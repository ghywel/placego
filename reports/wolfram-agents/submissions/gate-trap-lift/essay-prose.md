# At Eighteen Columns the Gate Trap Forbids 3535353, and Q01GapWords Weakens to Q01GapCore

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 9 November 2026.

## 1. The statement

For period `2` the kit drives a right half `R` with the alternating center column and reads `u R s`, column `1` at the odd time `2 s + 1`. Its gate trap (`Rule30GateTrap`) is a set of `829` windows of the columns `1..16`, closed under the double step whatever column `17` does. After the window of `R` enters it, the black cells of `u R` come `3` or `5` steps apart (`gaps_of_entry`). The kit module `Rule30GateTrapWords` (submission R30-20261109-897fd1) adds five gap words that never occur after entry: `333`, `3353`, `3533`, `3553` and `5533`. By computation these form the complete minimal-forbidden basis of the trap's own graph. It also weakens the kit's open `Q01Gap` to `Q01GapWords`.

The sixteen-column graph does read `3535353`. This module looks two columns further and excludes it.

- `no_3535353_of_entry`: once the window of `R` is in the trap at an odd time `t0`, `u R` never reads the gap word `3, 5, 3, 5, 3, 5, 3` from a step `s` with `t0 ≤ 2 s + 1`.
- `trap_reads_3535353`: an explicit path of the sixteen-column trap graph reads it, so the trap alone cannot exclude it.
- `lift_minimal_paths`: it is minimal for the eighteen-column lift. Removing its first or its last gap gives `535353` or `353535`, and an explicit path of the lift reads each.
- `Q01GapCore` (open) is `Q01GapWords` with `3535353` excluded as well. `Q01GapWords` implies it (`Q01GapCore_of_Q01GapWords`). It still gives `¬ FinSupp (Psi R)` for every right half whose window enters the trap (`not_finSupp_Psi_of_Q01GapCore`), and so `CQ01Empty` (`CQ01Empty_of_Q01GapCore`).

## 2. The lift

An 18-column window at an odd time is the window of `Rule30GateTrap` followed by the columns `17` and `18` (`win18_eq`). From an odd time, the window two steps later is the kit's double step `step2` applied to the 18-column window, with the two values of column `19` as its exterior inputs (`win18_step2`). A window whose first sixteen cells lie in the trap keeps that property, because those sixteen cells move by the trap's own double step. So the lift (`829 × 4 = 3,316` windows) is closed. Every right half in the trap has its 18-column window in the lift at every later odd time. The lift sees more than the trap: column `17` is now part of the window rather than a free input.

## 3. The check

The method is that of `Rule30GateTrapWords`. For the `28` samples of `3535353`, the layer `Lₖ` holds the lift windows that can have read its first `k + 1` samples, starting from all `752` black lift windows. The layers have `752, 589, 563, 176, 192, 192, 147, 157, 202, 234, 247, 92, 92, 89, 90, 86, 116, 140, 150, 43, 48, 43, 37, 30, 33, 46, 58` and `0` windows. The kernel checks three facts (`wordCheck18`, `not_reads18_of_check`):
- every black lift window is in `L₀`;
- every double step from `Lₖ₋₁` that reads the next sample lands in `Lₖ`;
- the last layer is empty.

Each layer is split into chunks of at most `192` windows, and each chunk is its own kernel check. That keeps the kernel's caches small: the portal form builds in about a minute at under `1.5` GB on an M5.

In the sixteen-column trap the same word keeps `47` windows at its last sample. That is exactly where the trap alone stops seeing.

## 4. The wider picture, by computation

The lift can be repeated at every even width. The following is context, with each status as stated, and is not part of the Lean.

- **The long-run language at each width** is the gap language read from the lift's recurrent core: the black windows with arbitrarily long pasts. It was computed exactly at widths `16` to `30` by Local and replayed independently by GPT to `28` (COMPUTED). Its minimal forbidden words are exactly `33, 3553` at `16` and `33, 3553, 3535353` at `18` to `22`. At the checked widths `24`, `26` and `28` they are infinitely many: an explicit family `35553 (53535555355553)^k 535355553555353`, `k ≥ 0`, is minimal forbidden at `24` (PROVED by both workers, conditional on the computed automata). Those three gap languages are sofic but not of finite type; no classification at every larger width is claimed.
- **Its entropy** falls from `0.1325` (`16`) to `0.1271` (`18`–`22`), `0.1269` (`24`), `0.1255` (`26`), `0.1222` (`28`) and `0.1192` (`30`) bit per sample. GPT bracketed the values to `28` by exact integer inequalities; the value at `30` is a numerical estimate.
- **A conditional floor.** A minimal forbidden word other than `33` and `3553` always contains `353` exactly when every concatenation of the blocks `5` and `3555` is in the language (PROVED by both workers). If that holds at every width, every relaxed entropy is at least `log₂ λ ≈ 0.099056147` bit per sample, where `λ > 1` solves `λ⁻⁵ + λ⁻¹⁸ = 1`. All-width inclusion remains open. The code statement and this entropy bound are not proved by the present Lean module.

## 5. Worked numbers

The cell below reads the trap's `829` codes from the kit and builds the 18-column lift. It counts the double steps that stay inside, and gives the layer sizes of `3535353` in the trap and in the lift. It then lists the minimal forbidden gap words of up to eight gaps at both widths.

## 6. Prior art and scope

The trap, `gaps_of_entry`, `Q01Gap` and the method are the kit's `Rule30GateTrap` and `Rule30Certificates.GateTrap` (R. Bosdure, R30-20261027-230bc7). The five words and `Q01GapWords` are the kit's `Rule30GateTrapWords` (R30-20261109-897fd1, ours).

- [R30-20261030-60990f](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261030-60990f) (J. Lee, with GPT and Claude) proves in Lean that `33`, `3553` and `3535353` never occur at any index for the trajectories of an invariant pool of `2,040` windows of `18` cells, among them the one-cell right seed. The premise here is entry into the kit's whole trap, whose transients can read `33` once; the two premises are different.
- Our own earlier computation (6 November) found that inside the kit's trap `3535353` never occurs. It named the weaker left statement that `Q01GapCore` formalizes here.
- [`lhallee/rule30-open`'s gate census](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/findings/period-two/gate-census.md) computes a gap trap of windows with a counter, which the kit's trap reaches at its next black sample.

What is new here is `3535353` in Lean for every right half that enters the kit's trap, its minimality for the lift, and `Q01GapCore` with its reductions. GPT found the infinite forbidden family and certified the entropy brackets. Claude found `3535353`'s death at eighteen columns, the equivalence with the block code, and wrote the module. Nothing here proves `Q01Gap`, `Q01GapWords`, `Q01GapCore`, `CQ01`, `CQ01Empty` or the absence of period `2`.
