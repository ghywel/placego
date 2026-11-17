# unimodal demand orders the optimized allocation bound

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT218. unimodal demand orders the
optimized allocation bound (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Unimodal demand makes weighted centering no worse than the earlier absolute allocation bound.

**What it says.** If nonnegative demand rises to a mode and then falls, use the cumulative imbalance at that mode as a centre. Telescoping on the two sides bounds the optimized objective by the original weighted absolute sum.

**Why it matters.** It provides a shape condition under which the new bound is guaranteed to improve or tie. Actual demand unimodality is unproved; a separated-spike demand defeats general domination. The terminal single-spike layer ties exactly.

**An everyday picture.** With one hill in the weights, choosing a reference at its summit accounts for both slopes. Multiple hills need another argument.

## The formal statement and proof

**Where:** RULE30-GPT.md GC428 at2293b9c; conditional statement and proof copied verbatim below. Local L256 in f0c44b9 checks gradient signs, finite-sum interchange, mode indexing and all three analytic guards. Actual demand unimodality is not asserted. The comparison is a conditional refinement of G213-G217, not a count-ratio estimate.

Keep G213's finitely supported signed I_j, its cumulative B_j, and a nonnegative finitely supported demand d_j. Suppose d is unimodal: for some mode k it is nondecreasing up to k and nonincreasing thereafter. Plateaux are allowed, and the zero demand is trivial. Then G217's optimized bound is no greater than G74's original absolute sum:

    (1/2)*min_c sum_a abs(B_a-c)*abs(d_a-d_(a+1))
        <= (1/2)*sum_j abs(I_j)*d_j.

This is conditional on demand shape, not an actual Collatz shape theorem. Existing-record search found G93's bounded shape observations and L048's later log-concavity failures, but no general unimodality proof or this weighted-centering comparison. The derivation below is elementary finite-sum rearrangement applied to G213-G217, with no novelty claim.

**Proof.** Evaluate the left objective at c=B_k. For a<k, abs(B_a-B_k)<=sum_(j=a+1)^k abs(I_j); the gradient weight is d_(a+1)-d_a. Interchanging the finite sums yields

    sum_(a<k) abs(B_a-B_k)*(d_(a+1)-d_a)
        <= sum_(j<=k) abs(I_j)*d_j,

since sum_(a<j)(d_(a+1)-d_a)=d_j after zero extension on the left. For a>=k, abs(B_a-B_k)<=sum_(j=k+1)^a abs(I_j), and the gradient weight is d_a-d_(a+1). Reordering gives

    sum_(a>=k) abs(B_a-B_k)*(d_a-d_(a+1))
        <= sum_(j>k) abs(I_j)*d_j,

using the zero right tail. Add, divide by2 and then minimize. The point a=k contributes0, so the endpoint convention does not double-count its imbalance. This proves the comparison without a log-concavity assumption or any sign restriction on I.

**Scope:** GC428's single-spike tie, plateau cancellation and separated-spike failure are retained in its source. Arbitrary nonnegative demand does not imply this comparison; the actual backward law needs its own shape proof.

**Duplicate guard for G218:** actual nearest G217,G213,G94 read in full. G217 defines optimized centering and G213 the Abel identity. G218 supplies a conditional comparison with the original absolute bound by unimodal gradient signs; G94 concerns the absorbing log-concavity edge and does not establish actual unimodality.
