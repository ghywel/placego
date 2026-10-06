# Equal terminal values do not force weighted parity cancellation

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G90. Equal terminal values do
not force weighted parity cancellation (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Meeting at the same terminal value does not make two starts cancel in the weighted count error.

**What it says.** Choose a meeting pair from W89 at width 34. Just before the last step, one start needs an odd step to pass the growth-factor barrier, while the other already has enough odd steps. Their fair-coin continuation weights are one half and one. Both actually survive, so their individual weighted changes sum to a positive half rather than zero.

**Why it matters.** Terminal pooling cannot supply the missing signed cancellation merely because two trajectories meet. This selected-pair example does not estimate the full population error. It returns the collision insight to the open weighted-bias question. The preregistered two-trajectory control passed, including the unequal penultimate-class guard. Independent model review remains pending.

**An everyday picture.** Two travellers reach the same destination, but only one used the last coin toss to clear a toll. Sharing a destination does not balance their different budgets.

## The formal statement and proof

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
