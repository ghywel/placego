Rule30FirstChecks: an exact pair law for the first check past the free range, and two of every three such checks are balanced (R30-20261106-bdd993)

This adds `lean/Ruliology/CellularAutomata/Rule30FirstChecks.lean`, with its `public import` line in `lean/Ruliology.lean` and a row in *Added in the kit*. It imports `Rule30ZeroBoundary` only.

**What it proves.** Write `check n l = Theta (word l) (2 n + 1)` for a word `l` of length `n`, `ones n` for the number of words on which it is black, and `gap n` for the smaller of `ones n` and `2 ^ n - ones n`.
- `first_check_count`: the rows of width at most `2 n` black at column `-1` at every even tick through `2 n` number exactly `2 ^ n - ones n`.
- `pair_count`: the check differs from the check of the shifted word on exactly `2 ^ m + ones m` of the words of length `m + 2`.
- `adjacent`: `2 ^ m + ones m ≤ gap (m + 2) + 2 * gap (m + 1)`.
- `distance_two`: `2 ^ (m + 2) ≤ 4 * gap (m + 4) + 24 * gap (m + 2)`.
- `two_of_three`, `first_check_balanced`: at most one of any three consecutive checks from `2` on has `40 * gap n < 2 ^ n`, and each of the others passes between 1/40 and 39/40 of the rows.

**Method.** `two_tick` is two ticks of a row with a white wall as one Boolean identity. With `two_step_shift` it compares a check with the check of the shift (`check_xor`). `tri_odd`, `tri_even` and `Theta_dep` then fix what the newest two free bits do (`four_sum`), and summing gives `pair_count`. `overlap` is the elementary bounds on two subsets of the cube. `adjacent` and `distance_two` are `omega` after that. `first_check_count` follows the free word and the row together, using `snoc_pivot` and `ok_snoc`.

**Checks**, with Lean 4.35.0, at main `9d837cd5`:
- `lake build Ruliology.CellularAutomata.Rule30FirstChecks`: no warnings, about a second for the module on an M5 MacBook Pro.
- The kit's own `Check.lean --claim partial` passes all 10 headlines: 98 constants replayed, no new axioms, axioms within `propext`, `Classical.choice`, `Quot.sound`.
- The compiler rejected all eleven mutations tested, including `23` for `24` in `distance_two` and `39` for `40` in `Bad`.
- Direct counts agree in Python and Wolfram Language: `ones n` and the pair law for `n ≤ 12`; the row count over all rows for `n ≤ 6`, and in Python for `n ≤ 11`.
- The portal form, the same proofs, passes `Check` at the verifier's kit `5fb59158`.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** `Theta`, `two_step_shift`, `tri_odd`, `tri_even`, `Theta_dep`, `snoc_pivot`, `ok_snoc` and `count_constrained` are `Rule30ZeroBoundary`. The two-tick identity is two applications of the rule. We found no bound on these checks in the kit, on the portal, in the open pull requests, or in `lhallee/rule30-open` at `f877f5af`.

**What it does not do.** It bounds the first check past the free range only, and two of every three `n`, not every `n`. From the second check on the fresh bits are pinned, so the bounds do not multiply along a row. It does not prove `Q01`, and no prize problem is settled.

Portal entry: [R30-20261106-bdd993](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-bdd993), **Lean Verified**.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
