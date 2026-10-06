# An isolated right-race source error heals once and returns one tick later

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G109. An isolated right-race
source error heals once and returns one tick later (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

An isolated race error can disappear at its source and return without another race.

**What it says.** A right-race injection forces a black ideal right neighbour. The original source's disagreement on the first three ticks is1,0,1. Its second-tick damage has moved elsewhere.

**Why it matters.** Healing at one cell is not coalescence or permanent recovery. This is a local arbitrary-background identity, not a repeated-race survival law. EH1-EH2 and review are pending.

**An everyday picture.** An echo can return after the place where it began has fallen quiet.

## The formal statement and proof

**Status:** local damage-echo proof; EH1-EH2 and independent review pending. Follows G102/G108 and Local L063. Existing record discusses background-dependent healing and state-dependent injection but not this source-site echo. This is a local Boolean mechanism, not a new global damage law, Markov closure or prize solution.

**Single-flip kernel.** Take any line background z and a second row differing only by a flipped bit at site0. Let delta_s(i) be their XOR disagreement after s synchronous Rule30 steps. At s0 the error is only at0. At s1,

    delta_1(-1)=1-z(-1), delta_1(0)=1-z(1), delta_1(1)=1.

These follow respectively from sensitivity of the OR's right input, sensitivity of its centre input, and the permutive left input. Let b=F(z). For the second synchronous step, delta_2(0)=z(1) OR z(2).

To prove this last identity, split on z(1). If z(1)=1, delta_1(0)=0 and b(0)=1-z(-1). Hence delta_2(0)=(1-z(-1)) XOR (1-b(0))=1. If z(1)=0, both centre and right inputs are flipped at s1. Toggling both OR inputs changes its value by1 XOR b(0) XOR b(1). Here b(0)=z(-1) XOR z(0) and b(1)=z(0) XOR z(2). Adding the left disagreement1-z(-1) cancels the z(-1) terms and leaves z(2). Both cases give the OR formula. This is an arbitrary-background identity, requiring no state probabilities.

**Isolated right-race injection.** Start ideal and raced copies from the same arbitrary old row x. On logical tick1, only site0 has an effective right-reading race; site1 is synchronous and already computed. All other sites read the old snapshot. Then the only possible first-row discrepancy is at0, and

    E_1=(1-x(0))*(1-x(1))*x(2).

Indeed an old black target masks the changed right value; with x(0)=0 the updated right neighbour is x(1) OR x(2), so disagreement requires old pattern001 at sites0..2. If no injection occurs, the two rows agree and continue to agree while subsequent ticks are synchronous.

If an injection occurs, the ideal first row z=F(x) has z(1)=1. Apply the single-flip kernel to these first rows. At the original source, disagreement over ticks1,2,3 is exactly

    1, 0, 1.

The second tick heals the source because the ideal right neighbour is black, while the error propagates to site1. The third-tick return follows from delta_2(0)=z(1) OR z(2)=1. There is no new injection in this experiment. Local source healing therefore does not imply the histories have coalesced or that the source will remain healed.

**Fair-input finite law.** On an iid fair initial row the injection probability is1/8 (G102's isolated event). Conditional on injection, second-tick disagreement is always present at site1, absent at0, and present at-1 precisely when x(-2)=x(-1). Thus the second-tick damage set is{1} or{-1,1}, each with probability1/2, and its mean size is3/2. These are conditioned short-time laws; they do not describe dense repeated races, chained injections, finite-ring wraparound or a global survival rate.

**Unexpected echo guard.** The event E_1=1,E_2=0,E_3=1 is forced for every injected isolated right race. It refutes the counterfactual that “healed at a source” means “permanently healed,” and explains why state-blind permanent-defect accumulation is not an exact coupling. It does not refute Local's finite empirical survival fit.

**EH1-EH2 preregistered NOT RUN.** EH1: enumerate all32 backgrounds on-2..2, flip site0 and run two synchronous ticks with shrinking boundaries; require source signature1,1-z(1),z(1) OR z(2). EH2: enumerate all128 old words on-3..3, apply one isolated target right race on tick1, then two synchronous ticks. Predict16 injections, all source signatures101; the other112 give000. Second-tick damage sets{1} and{-1,1} must occur8 times each. Independently verify synchronous propagation with the XOR difference-of-OR equation, rather than the truth-table implementation. These160 exact cases replace no Local long-run job. Publish predictions and instrument before execution.
