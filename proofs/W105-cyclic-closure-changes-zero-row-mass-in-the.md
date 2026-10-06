# Cyclic closure changes zero-row mass in the actual race model

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G105. Cyclic closure changes
zero-row mass in the actual race model (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Closing the row into a ring changes an exact probability even when large-ring statistics look fair.

**What it says.** Every right flag pattern gives exactly two preimages of the zero row. Left patterns give one or two according to whether any effective race is present. The resulting zero-row probabilities differ from the uniform ring law.

**Why it matters.** Infinite fair spatial invariance cannot be imported as exact finite cyclic invariance. The all-zero initial row also blocks any state-uniform upper decoherence bound. ZR1 passes43648 cases and40 exact weighted probabilities; independent review is pending.

**An everyday picture.** Joining the ends of a chain removes the free end used to reconstruct it.

## The formal statement and proof

**Status:** finite-ring preimage proof; ZR1 passes, independent review pending. Follow-up G104 and Local L054. This is a scope audit of the finite cyclic snapshot/sequential model in races.c, not a new damage-speed or prize theorem. Existing-record checks found fair infinite-row invariance and healing in structured backgrounds; these do not establish finite cyclic uniform invariance.

Take W>=3 cells with indices modulo W, old row x uniformly distributed over all 2^W words, and a fixed state-independent flag word. Sequential right-reading updates process W-1 down to0; an effective race at i<W-1 uses already-computed y_(i+1), otherwise old x_(i+1). Left-reading updates process0 up toW-1; an effective race at i>0 uses y_(i-1), otherwise old x_(i-1). The first processed cell always uses the old cyclic neighbour, so its flag is ineffective.

**Right zero-row preimages.** If the entire new row is zero, every update requires

    x_(i-1)=x_i OR [0 if the right race is effective else x_(i+1)].

If any x_i=1, this equation forces x_(i-1)=1, then repeats around the ring to force all old cells1. Conversely both the all-zero and all-one old rows produce the all-zero new row for every right flag pattern: induction in the scan order, using centre1 to keep the OR1 in the all-one case. These are the only two preimages. Thus conditional on any flags,

    P(new row is all zero)=2^(1-W).

The uniform ring law assigns that row probability2^(-W), so it is not invariant under any fixed right flag pattern or any state-independent mixture of them. G104's infinite-line fair product theorem is intact; closing the inverse around a cycle removes its independent tail. This mass discrepancy is exponentially small as W grows and does not refute Local's large-ring approximate statistics.

**Left zero-row preimages.** Any old1 at an effectively raced site would give new1 because its new left input is0. Therefore an old1 must sit at a nonraced site, where a zero output forces its old left neighbour1. Repeating this implication around the ring either encounters an effective race (a contradiction) or forces the whole old row1 with no effective flags. The all-zero old row always maps to zero. The all-one row does so exactly when no effective left flags are present. Consequently the zero row has one preimage when any effective left flag is present, and two otherwise. With independent Bernoulli(eps) flags,

    P(new row is all zero)=[1+(1-eps)^(W-1)]*2^(-W).

For0<=eps<1 this too differs from the uniform ring law. At eps1 the zero-row mass alone does not decide invariance; no claim is made from this one cylinder.

**No universal decoherence upper bound.** From the common all-zero initial row, ideal and raced histories remain identically zero for all logical times, every flag sequence and either scan direction. Thus no positive mean threshold can have a finite state-uniform onset bound, even with independent positive-rate flags. A matching upper side to G103 needs initial-state or activity assumptions. Fair marginal rows by themselves also cannot specify a coupling: equal copies have disagreement0, while independent fair copies have disagreement1/2, and synchronous Rule30 preserves both constructions' marginals. Those example couplings are not the common-initial-state race process; they only refute inference from marginals alone.

**Unexpected boundary/healing guard.** On a ring, distinct all-zero and all-one rows merge to the same all-zero row in one synchronous tick. Left permutivity therefore supplies no blanket finite-ring noncoalescence theorem. Infinite-line rightmost-damage propagation requires a rightmost discrepancy; these two infinite constant rows would have none. Local's background-dependent healing is preserved, not contradicted.

**ZR1 preregistered NOT RUN.** For W3..7, enumerate every old row and every flag word in both scan directions using the literal Rule30 truth table. Count zero-output preimages for every flag word: right always2; left1 or2 according to whether any effective flag is present. Independently apply exact Bernoulli weights at eps0,1/4,1/2,1 and compare the two formulas. Predict43648 row/flag/direction cases and40 weighted probability checks. Retain zero-row closure and the synchronous two-preimage healing guard. Counterfactual that G104 gives exact finite-ring uniform invariance must fail. This is a short exact enumeration, no long-run or Local scaling job. Publish before execution.


**ZR1 outcome (2026-10-06 20:13 BST).** Ran after proof, predictions and instrument publication throughf0f3a1b. PASS:43648 row/flag/direction cases and40 exact rational weighted probabilities. Right zero-row preimages are exactly zero and one for every flag pattern; left has only zero whenever any effective flag is present. Absorbing-zero and synchronous cyclic-coalescence guards pass. This confirms the finite preimage formulas; it supplies no long-run invariant measure, matching decoherence rate or selected-seed result. Independent review remains pending.
