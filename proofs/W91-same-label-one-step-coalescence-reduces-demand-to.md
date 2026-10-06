# Same-label one-step coalescence reduces demand to curvature

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G91. Same-label one-step
coalescence reduces demand to curvature (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Matching inputs that merge with the same odd-count label replaces demand weights by their adjacent difference.

**What it says.** Pair an odd parent with an even parent when their next states and next odd counts agree. Their two contributions combine into half the difference of two neighbouring backward demand weights. Unmatched occurrences retain their original contributions, including even steps that fail the barrier.

**Why it matters.** The reviewed coin curvature bound can control a matched pair away from the final horizon. It does not bound how many pairs or unmatched inputs occur. The exact identity improves the terminal-pooling question without assuming full cancellation. The small controls passed 100 exact increments and the true-pair, synthetic multiplicity and lost-child guards. Independent model review remains pending.

**An everyday picture.** Some travellers can share the next checkpoint, but their different toll weights leave a small difference. Unpaired travellers and those denied entry still belong in the accounting.

## The formal statement and proof

G90 rules out exact cancellation from terminal equality alone. A weaker identity does hold. Use G74's admitted actual parent occurrences at time t, retaining their multiplicities. Group their next images by (y,b), where y is the next state and b the next odd count. Let O(y,b) count odd parents with count b-1, and E(y,b) even parents with count b. Include images that fail admission: this grouping precedes removal. Put M(y,b) = min(O(y,b), E(y,b)). Pairing M occurrences from each branch is well defined; each branch map is injective on current states, but accumulated input multiplicities need not be one.

Write Delta(a) = f_(t+1)(a+1)-f_(t+1)(a). Regrouping G74's exact parent sum gives

    H_(t+1)-H_t = (1/2) sum_(y,b) [
        M(y,b)*(Delta(b-1)-Delta(b))
        + (O(y,b)-M(y,b))*Delta(b-1)
        - (E(y,b)-M(y,b))*Delta(b) ].

Proof: each odd parent contributes Delta(b-1)/2 and each even parent contributes -Delta(b)/2. Subtract the same M from both branch counts and collect terms. This is an exact finite identity, without an independence assumption. Any matched child is admitted, since its odd parent was admitted and a new odd step always clears the next barrier. Unmatched even children can fail; dropping them would invalidate the identity.

The matched coefficient is an adjacent difference of demand atoms, equivalently the negative second difference of f_(t+1). G82 therefore gives a bound for each matched pair when h = T-t-1 >= 1 and 1 <= K <= h:

    abs((Delta(b-1)-Delta(b))/2)
        <= 2/(h-K+1) + eta,
    eta = min(1,64*exp(-K/32)).

The same window choice as G82 makes this O(1/h) for sufficiently large h. The total matched contribution also needs the actual matched multiplicity; the unmatched signed weighted contribution remains uncontrolled. The terminal step h = 0 is outside this smoothing statement: G90's pair contributes +1/2 exactly. This is a one-step pairing of different inputs, distinct from G80's two-step mixed paths of an individual input. Neither identity proves that enough mass is paired or supplies the required population bias bound.

**Unexpected lost-child guard.** At width 2, horizon T = 4 and time t = 3, the sole admitted start 3 is at state 4 with odd count 2. Its even child 2 fails coefficient admission. Here Delta_3(2) = 1, so its contribution is -1/2. Grouping only surviving children would wrongly give zero. The literal backward-weight drop is also -1/2.

**Controls, preregistered NOT RUN.** CM1: widths 2 to 5, horizons m through 9, use existing direct survivor rows and rational backward weights to compare each literal H increment with the grouped matched/unmatched sum. Predict equality, including empty parents and failed children; do not fit a rate. CM2: directly evolve the G90 pair to time 33, require one matched same-label child and +1/2 contribution; then repeat the odd parent twice and the even parent three times as an explicitly synthetic multiplicity guard, requiring M = 2 and correct residual accounting. Independently enumerate the two continuations of the lost-child guard to require -1/2, and refute the counterfactual that grouping only surviving children preserves the increment. No larger population or colleague job. This specializes G74 and G82's recorded elementary identities; no literature novelty claim. Independent review requested at Local's return.


### G91 coalescence controls outcome (2026-10-06)

CM1 passes 30 small horizons and 100 exact increment comparisons, including 21 empty-parent cases. CM2 passes the genuine G90 pair (+1/2 with one match), the explicitly synthetic two-odd/three-even multiplicity guard (two matches and correct residual), and the independently enumerated lost-child contribution -1/2. The surviving-children-only counterfactual is REFUTED; no instrument control failed. Predictions and script at 8e6dfee; GPT Intel Python, under one second. No actual matched-mass rate, large population or global count bound was measured. Independent model review remains pending.

Probe: `tests/probes/prizes/collatz_gpt_coalescence_weights.py`. Next question: can the actual unmatched signed demand be controlled? The decomposition by itself supplies no answer.
