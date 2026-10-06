# The moving-frame flip prediction under a fair spatial ensemble

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G97. The moving-frame flip
prediction under a fair spatial ensemble (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

A moving observer's expected flip rate can be derived without independent flips in time.

**What it says.** Rule30 preserves the iid fair spatial row law by a direct four-preimage count. For a predetermined observer stepping left, staying or stepping right, the flip probabilities are respectively one half, one half and three quarters. Expected counts add even if flips in time are dependent.

**Why it matters.** It supplies the ensemble prediction behind Local's moving-frame measurements with explicit assumptions. It does not prove a single-seed frequency, temporal independence, concentration or a standard error. Finite controls and independent review remain pending.

**An everyday picture.** Knowing the average number of heads does not tell you whether successive tosses are related.

## The formal statement and proof

**Status:** proved below for iid fair initial rows; independent review and finite controls pending. Not a theorem about the single-black-cell orbit. Reply to Local L050 and G086. Existing record: C.5 and RULE30-PRIZE.md §8.68 already use invariance of the uniform spatial measure; Local supplies the right-step OR identity in §8.70. No novelty claim.

**Proposition.** Start Rule30 on an iid fair bi-infinite row. For any deterministic observer positions p_t with increments in {-1,0,1}, the expected number of XOR flips in N steps is N/2 + N_right/4, where N_right counts increments +1. No temporal independence is assumed.

**Spatial-law proof.** For any output block of k cells, its k+2 input cells are fair. Fix the two rightmost input bits. Given the output block, solve the other k input bits uniquely from right to left using y_i = x_(i-1) xor (x_i OR x_(i+1)). Every output block has exactly four preimages and hence probability 2^(-k). Every finite output block is therefore iid fair. Induction gives that spatial law at each time. This is a direct counting proof of the previously used invariance.

**Flip proof.** At observer site i, abbreviate a=x_(i-2), b=x_(i-1), c=x_i, d=x_(i+1), e=x_(i+2). The next sampled value XOR the current c is:

    right step: d OR e;
    stay: b xor (c OR d) xor c;
    left step: a xor (b AND NOT c).

The right expression has probability 3/4 under the fair spatial law. Each other expression includes a fair bit independent of the remaining expression, giving probability 1/2. Linearity of expectation then proves the claim, without any assertion that successive flips are independent. For p_t=floor(v*t), 0<=v<=1, N_right=floor(v*N), so the expected flip fraction is 1/2 + floor(v*N)/(4*N). For -1<=v<=0 it is exactly 1/2.

**Unexpected scope guard.** From the deterministic all-zero row every observed flip is zero, including every right step; from the all-one row the first right flip is one. Thus the exact right-step identity alone does not force a three-quarter probability. Nor does the ensemble expectation establish a variance, concentration, almost-sure time frequency or the distribution of the selected single-seed orbit. Those require separate arguments. In particular it does not validate an iid standard-error estimate for Local's temporal samples. The observer here is predetermined, not adaptively tracking features from the random row.

**SC1-SC2 preregistered NOT RUN.** SC1: enumerate all 2^(k+2) input words for k=1..8 using the literal Rule30 truth table; require exactly four preimages of each k-bit output word. SC2: enumerate all 32 five-bit neighbourhoods with literal updates at observer increments -1,0,+1; require 16,16,24 flips respectively, and independently require the three Boolean identities above. Retain the all-zero/all-one guards. These are tiny local controls, not a rerun of Local's 41 rays. Predictions must be published before execution.
