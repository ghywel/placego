Rule30FrontierChart: Q01 implies mortality, so Q01, mortality and a repeat budget at every length are one statement (PORTAL-ID)

This adds `lean/Ruliology/CellularAutomata/Rule30FrontierChart.lean`, with its `public import` line in `lean/Ruliology.lean` and a row in *Added in the kit*. It imports `Rule30AlternatingTraceBridge` and `Rule30ZeroBoundary`. It also changes the sentences in the `Rule30SurvivalBridge` and `Rule30AlternatingTraceBridge` docstrings and catalogue rows that call the converse not known. No proof in those two modules changes.

**What it proves.**
- `mortality_of_Q01`: `Rule30ZeroBoundary.Q01` implies `Rule30SurvivalBridge.Mortality`.
- `mortality_iff_Q01`, `budget_iff_Q01`: with `Q01_of_mortality`, `Q01_iff_staged` and `budget_iff_mortality`, mortality is `Q01`, and a repeat budget at every length is `Q01`.

**Method.** An immortal frontier is read as a space-time chart. The high bit of depth `e` of the `n`-th frontier sits at time `τ` with `τ + e = 2 n`, and the low bit where `τ + e + 1 = 2 n`.
- `Z_rec` extends `Z_depth`'s two recurrences past the frontier's far end, where the scan's zero memory cancels.
- `chart_interior`: those recurrences are the Rule 30 recurrence at every cell of depth at least two.
- `chart_wall`: the terminal symbols `(1, !s)` and `(s, s)` give the rule at depth one with a white wall from time one on.
- `zrow_chart`, `inX_start`, `finSupp_start`: the row at time two is a finitely supported start with column `-1` black at every even step, which `Q01` forbids.

`Legal` is used only to know the first frontier is nonempty. The proof does not show that the frontier was read off this row.

**Checks**, with Lean 4.35.0, at main `9d837cd5`:
- `lake build Ruliology.CellularAutomata.Rule30FrontierChart`: no warnings, under a second for the module on an M5 MacBook Pro.
- The kit's own `Check.lean --claim partial` passes all 9 headlines: 58 constants replayed, no new axioms, axioms within `propext`, `Classical.choice`, `Quot.sound`.
- The compiler rejected all nine mutations tested, in the wall, the interior, the chart's parity, the two recurrences, the start time and the nonempty hypothesis.
- All 10,922 legal frontiers of length at most 7 were run: every checked chart cell obeys the rule, 28,560 interior and 5,208 at the wall, in Python and in Wolfram Language.
- The portal form, the same proofs, passes `Check` at the verifier's kit `5fb59158`.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** The arrows used are from `Rule30SurvivalBridge` and `Rule30AlternatingTraceBridge`, contributed by David Condrey, and R30-20261102-b8e784, by G.P.J.W. Quint and Gemini, unified those modules. Closed PRs 75, 76 and 85 leave the converse open, and PR 75's review asked for the relation to `Q01` to be stated.

**What it does not do.** It proves no budget, capacity bound or mortality, and no prize problem is settled. The equivalence says nothing about which form is easier to prove.

Portal entry: [PORTAL-ID](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/PORTAL-ID).
