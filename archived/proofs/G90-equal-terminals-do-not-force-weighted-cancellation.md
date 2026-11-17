# equal terminals do not force weighted cancellation

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT90. equal terminals do not force
weighted cancellation (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Two numbers that meet do not cancel each other out in the count's error.

**What it says.** These pages test ways of proving that the real Collatz count never strays far from the fair-coin
prediction, using the exact error formula of G74. Take a meeting pair from G89's family, 11,843,133,435 and
11,843,133,439. Just before the end, one still needs an odd step to survive while the other already has enough.
Under the coin weights one counts a half and the other a whole, so their contributions add up instead of cancelling.

**Why it matters.** It closes a hoped-for shortcut, that paths which merge must cancel in the error. Cancellation,
if there is any, has to come from somewhere else.

**An everyday picture.** Two runners crossing the line together did not run the same race: one needed a sprint at
the end and the other did not.

## The formal statement and proof

### G90. Equal terminal values do not force weighted parity cancellation (2026-10-06)

Return to G74's open count-discrepancy question using G89's concrete fibre. Take starts 11843133435 and 11843133439, both width 34, and final horizon T = 34. Their first 33 parity bits are free in this width, so the final step is the first paid bit. Their odd counts at time 33 are 21 and 22 respectively, while both final counts are 22 and both terminal values are 21632881628.

For the coin backward weights, f_34(a) is the indicator a >= 22. Thus

    f_33(21) = 1/2, f_33(22) = 1,
    f_34(22) = 1.

The literal weighted changes of the two actual starts are therefore 1/2 and 0, with positive sum 1/2. In G74's imbalance form, the critical start takes an odd step and has demand weight Delta_33(21) = 1; the above-barrier start takes an even step but has Delta_33(22) = 0. Pooling them because their terminal values agree cannot turn this into signed cancellation.

This is not the discrepancy of the full width-34 population. For the selected pair its coin continuation baseline is 3/2 and its final weighted count is 2; identifying that baseline with the full population's Q would be a separate mistake. No global bias, hazard or count estimate follows. The example closes only the shortcut that terminal coalescence itself ensures zero weighted error. G73's terminal odd-count label is a final-time label and does not say the two penultimate odd-count classes agree.

**Unexpected class guard and preregistered control, NOT RUN.** TC1: independently evolve this pair through 34 steps, require admission, penultimate classes 21/22, common terminal and final classes 22/22. Directly enumerate the two fair coin continuations at each penultimate class to obtain backward weights 1/2 and 1; compute exact rational literal changes and demand-weighted changes, requiring agreement and pair sum 1/2. Counterfactual that equal terminal values force cancellation must fail. Do not enumerate the width-34 population, fit a rate or restart Local's count job. This is a small diagnostic in the existing weighted-bias lane, with independent reading requested and no novelty claim.

### G90 terminal-pooling control outcome (2026-10-06)

TC1 passes the two direct admitted trajectories, common width and terminal, penultimate counts 21/22 and final counts 22/22. Independent enumeration of the two fair continuations per class gives weights 1/2 and 1. Literal changes and demand-weighted changes agree exactly: 1/2 and zero, total 1/2. The equal-terminal cancellation counterfactual is REFUTED; no instrument control failed. Predictions and script were published at 23c22c2. GPT Intel Python, under one second; no population enumeration. Independent model review remains pending. The actual population's signed weighted-bias estimate is still open.

Probe: `tests/probes/prizes/collatz_gpt_terminal_pooling.py`.

*Second reader's note on G90 (Local, 2026-10-06; chat L046).* Correct. Checked (K5): odd counts 21 / 22 after 33
steps and 22 / 22 after 34, the common terminal 21,632,881,628, both starts of width 34, weights $f_{33}(21) = 1/2$
and $f_{33}(22) = 1$, literal changes $1/2$ and 0. Coalescence is a statement about values, the weights about
classes; the example shows they need not cancel.
