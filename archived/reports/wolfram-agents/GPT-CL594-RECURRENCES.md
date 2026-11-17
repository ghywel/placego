# Approximate recurrences transfer to visible bits but do not close the clock problem

2026-10-23, GPT, CL594 task 2. **The feedback theorem transfers verbatim to any binary visible sequence. What does not transfer is an inference from a periodic boundary to autonomous finite memory for that sequence.** This is a scoped source/hand guard, not a new period-2 exclusion or experiment. If a coupled finite-memory theorem held, it would make the visible bits periodic and contradict the existing Corollary F; the missing finite-memory theorem is the substantive obligation.

Read [ApproximateRecurrence.lean](https://github.com/WolframInstitute/Rule30PrizeKit/blob/9679f830d345efc7b4e6a5c30dc5468836e30e21/equivalents/Rule30Equivalents/ApproximateRecurrence.lean) in full and the carrying `eventuallyPeriodic_iff_feedback` proof in [WordsAutomata.lean](https://github.com/WolframInstitute/Rule30PrizeKit/blob/9679f830d345efc7b4e6a5c30dc5468836e30e21/equivalents/Rule30Equivalents/WordsAutomata.lean), at the pinned commit. Also read the Q01 definition, reconstruction/Theta interface and free-bit aperiodicity statements in [Rule30ZeroBoundary.lean](https://github.com/WolframInstitute/Rule30PrizeKit/blob/9679f830d345efc7b4e6a5c30dc5468836e30e21/lean/Ruliology/CellularAutomata/Rule30ZeroBoundary.lean). These newer modules are source inputs, not imports available automatically at the verifier's older commit.

For **every** b: Nat -> Bool over any normed field, the first module proves

```math
b\text{ eventually periodic}\iff
\exists Q\text{ monic},\ N,\ \forall n\ge N:\ \|Q(\sigma)b(n)\|<\tfrac12.
```

No center-column hypothesis occurs. For fixed Q of degree q, the two possible next bits give residuals separated by norm 1; the strict half-radius condition makes at most one possible. Hence the last q bits determine the next bit. The finite window state repeats and gives eventual periodicity. Conversely a period P supplies Q = X^P-1. Monicity, a fixed Q and the strict inequality are essential to this argument; no computability of its coefficients is asserted.

Substitute b(n) = x_(2n)(1) directly. Under Corollary F's exact left-edge and clock hypotheses, b cannot be eventually periodic: choose one sufficiently late start i and arbitrarily large gaps that are multiples of its tail period. The agreement is infinite, so the required CF pairs exist. Thus those same hypotheses already imply **no** monic approximate recurrence for b. This is an equivalent restatement of an existing exclusion, with no bound on degree and no new LR coverage. The center's exact Q = X^2-1 recurrence does not manufacture one for b.

For Q01, `InX L` fixes the **even** depth-1 samples to 1, while the odd samples f remain free. Applying the theorem to the fixed even samples is trivial. Applying it to f converts `free_not_eventuallyPeriodic` into the corresponding absence of a monic approximate recurrence, conditional on `FinSupp L` and `InX L`. It does not prove those two hypotheses incompatible. `Theta f` realizes **every** f without the finite-support condition. Taking f to be 1 exactly at powers of 2 gives an explicit aperiodic free sequence: infinitely many ones and unbounded zero gaps. This actual one-sided realization refutes a recurrence forced merely by the white boundary plus `InX`. No finite-support claim is made; this is not a claimed counterexample to Q01.

A physical open-layer control shows why adding the clock phase to a finite state is insufficient. At width 1, Rule 30's two-step update under the white-even clock is

```math
s_{n+1}=\lnot(s_n\lor u_n\lor v_n).
```

Every sequence b without `11` can follow this update: take s_n=b(n), u_n=0 and v_n=1-b(n+1). Choose b with ones exactly at 2,4,8,16,... to obtain an aperiodic output of a one-cell layer with a periodic boundary. The far boundary is an external input, so this is not an autonomous full Rule 30 realization. It defeats the proposed finite-state reduction of an **open** layer, not the prize conjecture. If all inputs were periodic, or the entire coupled state were genuinely finite and autonomous, adjoining the phase would work; proving either condition is the missing step.

**Disposition:** yes to the generic visible-sequence equivalence; no to a boundary-driven finite-memory inference. The known Q01/free-bit formulation and the open-layer control retain total scope. No source-proof replay, new small-order conjecture, coefficient search, kernel benchmark or carrying queue is warranted by this reformulation alone.
