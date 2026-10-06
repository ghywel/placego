# One lag does not close the isolated-pulse paired trace at tick5

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G113. One lag does not close
the isolated-pulse paired trace at tick5 (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Keeping one previous paired observation still misses pulse-model memory.

**What it says.** In the isolated-pulse fair-input ensemble, one positive last-two-state bin has next-error rate5/234, but its refinement by an earlier observation has rate0. The zero child has no original injection; the positive parent is certified by exact cone enumeration.

**Why it matters.** This refutes order-two Markov at tick5 for this specific ensemble. All8192 words were checked with two update formulations; both separate seven-sample marginals remain uniform. Independent review is pending; no all-orders or repeated-race theorem follows.

**An everyday picture.** Remembering yesterday as well as today can still miss an older cause.

## The formal statement and proof

**Status:** exact finite-cone enumeration counterexample; independent review pending. Predictions and instrument published through2589f4f before execution. This is the pulse ensemble of G110, not the fresh Bernoulli-race model of G112 and not an all-orders impossibility claim.

Let K_t=(I_t,E_t) for the source of two common-input Rule30 copies. Start with an infinite iid fair row; only the noisy source0 reads its updated right neighbour on tick1, and all other reads and future ticks are synchronous. Keep the pulse schedule fixed and known. The seven source samples at ticks0..6 depend only on the13 initial bits at sites-6..6; the pulse's extra same-tick right read needs initial sites0..2 and stays inside that domain. Thus8192 equally weighted words give exact probabilities for this infinite ensemble. Literal Rule30 table updates were independently checked against XOR/OR updates throughout the shrinking cone.

Take A={K4=(0,0),K5=(0,0)} and its refinement B=A intersect {K3=(0,0)}. LM2 counts n_A=1872,n_(E6=1,A)=40,n_B=896,n_(E6=1,B)=0. Therefore

    P(E6=1 | A)=40/1872=5/234,
    P(E6=1 | B)=0.

Both bins have positive probability. Their next-error probabilities differ despite identical last two observed paired states; this violates second-order Markov at tick5, even with a time-dependent kernel and the known pulse phase.

The zero child also has an analytic explanation: G109 gives E3=E1, so B's E3=0 means no initial injection. With no future races the two configurations then agree forever. The positive parent-success count is the enumerated existence certificate, checked with both update formulations; it is not an extrapolation or a fitted probability. All count claims can be reproduced by tests/probes/rule30_gpt_lagged_memory.py. Independent reading remains required.

**LM1-LM3 outcomes (2026-10-06 21:05 BST).** LM1 PASS:8192 cone words,001 injection predicate and E1,E2,E3=indicator,0,indicator. LM2's blind split prediction HELD:8 unequal child-parent refinements among16 parents and36 positive children. A second child K3=(0,1),K4=K5=(0,0) has20 successes in40 histories, versus the parent's40 in1872; the rate difference is56/117. LM3, the unexpected marginal check, PASS:both separate seven-sample histograms have128 words64 times each. The permanent-healing counterfactual is refuted by the source echo. Uniform marginals coexist with failure of order-two paired closure. No result about third-order closure, every finite order, repeated fresh flags or long-time survival follows.
