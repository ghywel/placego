Rule30GateTrapWords: the gap words the gate trap forbids, and Q01GapWords (R30-20261109-897fd1)

This adds `lean/Ruliology/CellularAutomata/Rule30GateTrapWords.lean`, with its `public import` line in `lean/Ruliology.lean` and a row in *Added in the kit*. It imports only `Rule30GateTrap`.

**What it proves.** A gap word `g₁ g₂ … gₖ` is read from a black cell of `u R` when the next black cells follow at the gaps `g₁, g₂, …`, with white cells between (`gapWord`, `Reads`). For every right half `R` whose window enters the trap at an odd time `t0`, and every step `s` with `t0 ≤ 2 s + 1`:
- `gap_words_of_entry`: `u R` reads none of `333`, `3353`, `3533`, `3553` and `5533` from `s`. `no_3353_of_entry` is `3353` alone.
- `no_33535555_of_entry`: nor `33535555`, which begins with `3353`.
- `no_late_33`: after any two gaps, the next two are not both `3`. With `gaps_of_entry`, after the third black cell at or after entry, `u R` is a concatenation of `001` and `00001` with no two blocks `001` adjacent and none separated by exactly two blocks `00001`.
- `minimal_paths`: each word is minimal for the trap graph, whose column `17` is free. Removing its first or last gap gives one of `33`, `335`, `353`, `533`, `355` and `553`, and each is read along an explicit path of the graph. This is graph minimality; no realization by a right half is claimed.
- `Q01GapWords` (open) restricts `Q01Gap` to starts whose complemented free bits eventually also avoid the five words.
  - `Q01GapWords_of_Q01Gap`: the kit's `Q01Gap` implies it.
  - `not_finSupp_Psi_of_Q01GapWords`, `CQ01Empty_of_Q01GapWords`: it still gives `¬ FinSupp (Psi R)` for every right half whose window enters the trap, and `CQ01Empty`, as `Q01Gap` does.

**Method.** The kit's own: for each word, the windows of `trap` that can have read its first samples form layers, given as data, and the kernel checks that the double step takes each layer into the next for every value of column `17`, and that the last layer is empty (`wordCheck`, `not_reads_of_check`, by induction along the word through `win_next` and `win_mem_trap`). The five words share their first samples, so there are 40 layers in all. Each of the one start check and the 44 step checks is its own `decide +kernel`, which keeps the kernel's caches small. Membership uses a bitmap built from the codes (`maskN`) and `decode (encList w) = w`.

**Checks**, with Lean 4.35.0, at main `8d252e19`:
- `lake build Ruliology.CellularAutomata.Rule30GateTrapWords`: no warnings; the module builds in about 26 s, with a peak of about 1 GB for the module itself, on an M5 MacBook Pro.
- The kit's own `Check.lean --claim partial` passes all 9 headlines. It replays 240 constants and finds no new axioms; every headline's axioms are within `propext`, `Classical.choice`, `Quot.sound`.
- Eight mutations that must fail were all rejected. They drop a window from a middle layer and from the shared first layer, shift every code of a layer, start from the white windows, remove the final empty layer, claim the allowed word `3355` with the layers of `3353`, and give a witness path a start window with the wrong column `1` or one outside the trap. A ninth mutation, one early column-`17` value flipped in a witness path, was accepted. That is expected: column `17` reaches column `1` only after about eight double steps, so the path still reads its word.
- The worked numbers agree in Python and Wolfram Language: the closure of the trap (3,316 of 3,316 edges), the layer sizes of the five words, and the minimal forbidden gap words up to eight gaps.
- The portal form, with the same proofs, passes `Check` at the verifier's kit `5fb59158`.
- Not run: the full catalog build (`bash build_all.sh`).

**By computation, not in Lean.** The five words are the whole gap language of the trap graph: a word over the gaps `3` and `5` is read along some path exactly when it contains none of them (a product of two automata, 19 reachable pairs). `3535353` is read by the 16-column graph and dies when the trap is lifted to 18 columns.

**Prior art.**
- [R30-20261030-60990f](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261030-60990f) (J. Lee) proves in Lean that `33`, `3553` and `3535353` never occur in the gap sequence, at every index, for the trajectories of an invariant pool of 18-cell windows (`relaxed_no_forbidden_factor`), among them the one-cell right seed. The premise here is entry into the kit's whole 829-window trap, whose transients can read `33` once.
- [`lhallee/rule30-open`'s gate census](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/findings/period-two/gate-census.md) computes a gap trap of windows with a counter, which the kit's trap reaches at its next black sample, and notes the positive entropy of `Q01Gap`'s word class.
- `Rule30PeriodTwoWidth13` constrains every right half to a nine-pair gap language that allows every word over `3` and `5`.

What is new here is the list in Lean for every right half that enters the kit's trap, the start words `333`, `3353`, `3533` and `5533`, minimality for the trap graph, and `Q01GapWords` with its reductions.

**What it does not do.** None of `Q01Gap`, `Q01GapWords`, `CQ01`, `CQ01Empty` or the absence of period 2 is proved, nor that every finite right half enters the trap.

Portal entry: [R30-20261109-897fd1](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261109-897fd1).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
