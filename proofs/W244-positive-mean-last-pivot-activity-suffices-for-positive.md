# Positive mean last-pivot activity suffices for positive wall-language entropy

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G244. Positive mean last-pivot
activity suffices for positive wall-language entropy (GPT, 2026-10-08; waiting room, GC559)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

A positive average of active last inputs would prove positive boundary-language entropy.

**What it says.** The visible-prefix entropy is at least the expected count of active last initial cone bits. If their average activation probability stays positive, the actual wall language has positive entropy.

**Why it matters.** This is a concrete sufficient target that does not require independent activations or a stationary visible measure. Its large-time lower bound remains unproved; inactivity of these particular inputs does not imply zero entropy.

**An everyday picture.** Each exposed fresh switch that still reaches the observation contributes a bit of conditional uncertainty.

**W243/W244 review disposition (2026-10-08).** Local L298 verifies the isolation extension and L299 verifies the entropy inequality. Both are now second-read.

**W244 channel audit (GC560; reading pending).** The first half of every last-input path lies outside the wall cone and has independent fair gates, so activation probability is at most 2^(-n). Its mean density is zero and only finitely many such activations occur almost surely. This closes that particular positive-mean route, without bounding total visible entropy above.

**GC560 review disposition (Local L300, verified c51e30f via 4d7b4639).** Exponential masking and summable last-pivot activation are second-read. G244's chosen positive-mean route is closed under the fair-right ensemble; its entropy inequality remains correct, with no entropy upper inference.

**GC563 extension of W244 (awaiting reading).** Conditioning only on visible history gives next-black probability equal to the posterior of a hidden white pair when the current bit is zero. With beta_n the optimal history-only prediction error, 1+2 sum beta_n <= visible-prefix entropy <=1+(N-1)h2(mean beta). Positive average beta suffices for positive support entropy; no such lower bound is shown. A random-phase alternating comparator has persistent productive events but zero prediction error and entropy rate. Standard inequalities, no runtime or actual comparator realization claim.

**GC563 reading (Local L302, verified 2ca1aa0).** Visible posterior recursion and both prediction-error entropy bounds are second-read; average beta positivity remains open.

**GC564 G244 finite posterior control (awaiting reading).** At two-symbol histories 00 and 10, the next-black probabilities are exactly 5/12 and 3/16; 01 forces zero. Three-symbol masses are 7,5,4,13,3 over 32, matching GC502's collision 67/256, and beta_1=1/4. The initial white-pair to black-pair surgery cannot be transported after history 00 because evolved hidden pair 11 is impossible in that fibre. No long-time posterior estimate or new run.

**GC565 G244 gap-start target (awaiting reading).** At an observable first-zero gap start, restrict to actual hidden sites 2 and 4 black. GC503 makes the next two symbols 01 or 00 according to hidden site 3. Weighted posterior entropy gamma on this event lower-bounds two-symbol conditional entropy; overlapping blocks give H_N >= (1/2) sum gamma. Average gamma positivity remains unproved. Removing the hidden gate fails when sites 4 and 5 are both white. Initial four-symbol proposal sharpened to two; standard entropy algebra, no experiment or universal wheel-profile assumption.

**GC566 upstream local control (awaiting consolidated reading).** Actual even-row prefix 1110e evolves in two ticks to 0,1,1-e,1, independently of the exterior, and its next three visible outputs are 0,0,e. Refines reviewed GC504. The initial cylinders are real; later fifth-cell edits have no established lift preserving the complete observed-history fibre. No posterior or frequency bound. Stop local entropy-target rewrites; move to a distinct structural-balance audit.

## The formal statement and proof

*Scope and provenance.* Fair iid initial right bits under the imposed white-start alternating wall. Standard entropy chain rule and conditioning inequality, applied to G243's finite cone. GC499-GC500 identify the actual boundary-language entropy as lim_N log2(M_N)/N, where M_N counts its length-N words. No stationarity of the induced visible measure, independent activation events or positive activation-density claim.

Let Z_n=x_(2n)(1) and A_n be its Boolean sensitivity to initial site 2n+1, with A_0=1. Write F_n for the initial bits at sites 1 through 2n. Locality makes Z_n depend only on F_n and the fresh fair bit B_n=x_0(2n+1), and makes every earlier Z_j determined by F_n. Every binary function of one bit is affine, so

    Z_n = h_n(F_n) XOR A_n(F_n)*B_n.

The sensitivity A_n is independent of B_n, being a function of F_n; it is not assumed independent of earlier sensitivities. Conditional on F_n, an active output is fair and an inactive output deterministic. Hence H(Z_n | F_n)=P(A_n=1). Because the preceding visible prefix is determined by F_n, conditioning gives

    H(Z_n | Z_0,...,Z_(n-1)) >= H(Z_n | F_n).

Sum the entropy chain rule, including the fair initial Z_0:

    log2(M_N) >= H(Z_0,...,Z_(N-1))
                  >= sum_(n=0..N-1) P(A_n=1).

Every sample lies in the actual length-N language, so the support-size inequality applies. GC500's limit then gives h_infinity>=delta if the liminf of the displayed expected activation sum divided by N is at least delta. This is a sufficient condition, not an estimate of that liminf. G243 supplies only P(A_1)=1/4 and P(A_2)=1/8; the three-symbol lower bound is therefore 11/8 bits.

*Independent controls and failed converse.* GC501's two-symbol law gives entropy 1+(1/2)*h2(1/4), at least 5/4, agreeing with the new lower bound 1+P(A_1). The unexpected formal comparator Z_0=B_0 and Z_n=x_0(2n) for n>=1 has A_n=0 for every n>=1 but independent fair outputs and entropy rate one. It respects the same input-window upper bounds but is not a Rule 30 construction. Thus absent last-pivot activity supplies no entropy upper bound; earlier inputs may carry all the information. GC558's isolation, if verified, gives only an upper frequency bound on this particular sufficient channel, not on total language entropy. No experiment was run. Independent hand reading requested.

*G244 duplicate audit.* W244 nearest W243,W239,G212 read in full, including their extensions and summaries. W243 supplies the exact local sensitivity mechanism; W239 is an abstract and finite-width block construction; G212 supplies an upper information ceiling for noisy full-row observations. This is a lower conditional-entropy application to the wall language, not any of those conclusions. The chain rule and conditioning inequality are standard; no information-theoretic novelty is claimed.


**G244 channel audit — exponential masking of its last pivots (GPT, 2026-10-08; GC560, awaiting reading).** For n>=1, activation A_n needs all path centres G_s=x_s(2n-s) white for s=0,...,2n-1. Consider only s=0,...,n-1. The entire initial cone of G_s lies in [2n-2s,2n], with lower endpoint at least 2. Thus the imposed wall never enters these cones, and G97's left-permutive triangular formula applies using only fair initial right bits. G_s has fresh XOR pivot x_0(2n-2s); every earlier G_r has strictly greater lower endpoint and uses none of that pivot. Therefore these first n gates are independent fair. Their all-white probability is 2^(-n), giving

    P(A_n=1)<=2^(-n),
    sum_(n>=0) P(A_n=1)<=2.

For any m>=1, the union bound gives P(any A_n=1 with n>=m)<=2^(1-m). Letting m grow proves almost surely only finitely many activations under this fair-right ensemble, without independence between A_n events. In particular G244's expected activation sum divided by N tends to zero: its positive-mean sufficient channel cannot establish positive entropy in this ensemble. The original inequality remains correct and supplies no entropy upper bound. The reviewed small probabilities sharpen the total expected count to at most 13/8, but this also bounds only that lower certificate, not actual visible entropy.

*Controls and provenance.* The n=1 first-gate bound is 1/2 while the actual event has probability 1/4; n=2 gives 1/4 while the actual event has probability 1/8. Thus the argument does not pretend to capture all later correlated gates. The unexpected frontier is s=n: its initial cone reaches site 0, which is fixed by the wall, so extending the fresh-pivot induction across it is unjustified. This is G97's existing iid non-rightward sampling argument stopped before the boundary, applied to G243's path. No new experiment or iid activity assumption. Independent hand reading requested.

**G243 extension and G244 original statement reviews — Local L298 and L299, received by GPT 2026-10-08.** Verified in eee11aaf. L298 checks the odd-wall latch, all neighbour controls and time-zero exception, so GC558 is second-read. L299 checks the conditional affine law, conditioning direction, chain rule, language support, small entropy control and failed converse, so G244's original inequality is second-read. These readings do not yet verify the later GC560 exponential-masking audit. The suggestion that the mean might still be positive is superseded if that new audit passes.
