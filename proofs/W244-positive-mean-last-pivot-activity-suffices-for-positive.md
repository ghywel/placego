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

**G244 history-conditioned replacement target (GPT, 2026-10-08; GC563, awaiting reading).** Keep the actual fair-right wall process and let H_n denote the visible history Z_0,...,Z_n. At even time 2n, write the first three right cells as z,b,c. Two literal Rule 30 updates give the next visible cell zero when z=1 and 1 XOR(b OR c) when z=0. Equivalently,

    Z_(n+1)=(1-Z_n)*(1-x_(2n)(2))*(1-x_(2n)(3)).

On a history ending in zero, let q_n(H_n) be the conditional probability that those two hidden cells are both white. On a history ending in one, the next output is forced zero. Thus its conditional black probability is p_n(H_n)=(1-Z_n)*q_n(H_n), taking q_n=0 on the forced branch. Define beta_n=E[min(p_n,1-p_n)], the minimum expected error of any predictor of the next bit given only that visible history. There is no runtime restriction on this predictor. Standard binary entropy h2 and its symmetry give H(Z_(n+1)|H_n)=E[h2(min(p_n,1-p_n))]. Concavity between 0 and 1/2 gives h2(r)>=2r, and Jensen gives the upper bound h2(E[r]). Consequently for N>=2, with beta_bar=(sum_(n=0..N-2) beta_n)/(N-1),

    1+2*sum_(n=0..N-2) beta_n <= H(Z_0,...,Z_(N-1))
        <= 1+(N-1)*h2(beta_bar).

In particular positive liminf beta_bar suffices for positive actual boundary-language entropy, through the support bound log2(M_N)>=H. If beta_bar tends to zero, this ensemble's Shannon entropy per symbol tends to zero; that does not imply zero support-language entropy (GC501's mixture control). Earlier input uncertainty is retained because conditioning is only on observations, unlike G244's original entire-input-prefix conditioning. No positive beta lower bound is proved.

*Controls and failed shortcut.* GC501's exact first transition has p_0=0 on Z_0=1 and p_0=1/4 on Z_0=0, each history having probability 1/2. Hence beta_0=1/8 and conditional entropy (1/2)*h2(1/4), between 1/4 and h2(1/8). The unexpected comparator is a fair random phase of the periodic word 10: it avoids 11 and 00000, has productive next-one events of frequency 1/2, and yet every later bit is predictable from the first, with beta_n=0 and total entropy one. Formal hidden pair-void events can equal those productive events, satisfying the displayed visible recursion; no Rule 30 right realization is asserted. Thus positive void frequency or the finite gap restrictions alone do not ensure entropy. This is standard binary prediction/entropy algebra applied to the already recorded two-step wall identity, not a new predictor, Problem 3 runtime result or experiment. The next actual obligation is average posterior uncertainty, not another unconditioned pair-frequency measurement.

*GC563 duplicate audit.* Filed as an extension of W244; its nearest W243, G212 and W239, with their full proofs and summaries, have been read. The original W244 estimates entropy by a chosen last pivot; this extension instead uses all observed-history prediction error. G212 concerns fresh full-row sampling and W239 abstract block entropy. No new entropy theorem is claimed beyond standard inequalities. GC501's nonstationarity and failed pointwise contraction remain intact.

**GC563 second reading — Local L302, received by GPT 2026-10-08.** Verified in 2ca1aa0, included in 0981b01abe60. Local independently checks the visible gate, both concavity bounds, chain rule, initial beta control and formal alternating comparator. Correct as stated. Average history-conditioned prediction error remains open. The reading neither supplies its positivity nor makes a runtime claim. W244 neighbours W243, G212 and W239 were read in full, including summaries and extensions.

**G244 posterior control and failed pair surgery (GPT, 2026-10-08; GC564, awaiting reading).** Retain the fair initial right row. Write its first five bits as a,b,c,d,e. After one tick the first four right bits are u_1=a OR b, u_2=a XOR(b OR c), u_3=b XOR(c OR d), u_4=c XOR(d OR e). After two ticks Z_1 is zero when a=1 and 1 XOR(b OR c) when a=0; hidden sites 2 and 3 are v_2=u_1 XOR(u_2 OR u_3), v_3=u_2 XOR(u_3 OR u_4).

Condition first on visible history 00. Then a=0 and b OR c=1. If b=1, v_2=0. Its companion v_3=0 occurs for (c,d,e) in {000,001,010,011,100}, five of eight assignments: for c=d=0, u_3=1; for c=0,d=1, u_4=1; for c=1, u_3=0 and u_4=1 XOR(d OR e), which is one only at d=e=0. If b=0, the history forces c=1, and v_2=1,v_3=0 regardless of d,e. Therefore the hidden pair 11 is impossible after this history, while 00 has unconditional probability 5/32. Since P(history 00)=3/8, its posterior white-pair probability is 5/12. The actual cylinder 01000 is an explicit surviving 00 example.

Condition next on visible history 10. This is precisely a=1, probability 1/2. For v_2=v_3=0, u_2 OR u_3 must equal one and u_2=u_3 OR u_4. If u_2=0 the latter forces u_3=u_4=0, contradicting the former. Hence u_2=1, which forces b=c=0. Now u_3=d,u_4=d OR e, so d OR e=1. There are three such four-bit assignments, giving posterior probability 3/16. History 01 ends in one and forces the next visible bit zero.

The three-symbol probabilities, in order 000,001,010,100,101, are consequently 7/32,5/32,4/32,13/32,3/32. Their squared sum is 67/256, independently agreeing with GC502's existing literal-update collision measurement. GC563's next-step optimal prediction error is beta_1=(3/8)*(5/12)+(1/2)*(3/16)=1/4. Its exact conditional entropy increment is (3/8)*h2(5/12)+(1/2)*h2(3/16). This is a finite posterior control, not an asymptotic estimate.

*Failed transfer, controls and next.* At the initial row, on a=0, swapping the pair b,c=00 with 11 is a measure-preserving pairing of opposite next outputs, preserving the first visible bit. Its paired mass is 1/4, giving the exact optimal-error contribution 1/8. Repeating that swap on the evolved hidden pair after history 00 is invalid: the proposed target pair 11 has no actual predecessor in that history fibre. Thus a current-row surgery cannot be assumed to lift to an initial-row pairing that preserves observed history. The conditioned fair-product counterfactual fails structurally, before any probability fitting. Unexpected check is the full collision reconstruction above, reusing the existing measurement rather than running a larger census. This local gate and entropy control reuse GC501, GC502 and the literal two-step wall update. No novel method or positive long-time beta is claimed. Next a history-preserving initial-input pairing with certified multiplicity, or a different reasoning lead; do not enumerate more posteriors.

**G244 gap-start block target (GPT, 2026-10-08; GC565, awaiting reading).** Keep the actual fair-right process and visible history H_n=(Z_0,...,Z_n). For n>=1 let S_n be the observable first-zero event Z_(n-1)=1,Z_n=0. At physical time 2n write right sites 1..5 as 0,b,q,r,z on this event. Let E_n be the hidden event b=r=1, without assuming it holds at every gap start. Reviewed GC503 gives zero-gap length R=2 when q=0 and R=4 when q=1 on E_n, independently of z and farther cells. In fact the next two visible symbols are already 01 or 00, respectively. They determine q on E_n; waiting for the terminating one in the longer gap is unnecessary.

Let theta_n=P(q=1|H_n,E_n), set arbitrarily when the conditioning event has zero probability. Define gamma_n=E[1_(S_n)*P(E_n|H_n)*h2(theta_n)]. Conditioning cannot raise entropy, and S_n is determined by H_n. On E_n, the two future visible symbols determine q. Consequently

    H(Z_(n+1),Z_(n+2)|H_n) >= gamma_n.

No posterior fairness is assumed. For N>=4, summing over n=1,...,N-3 gives

    H(Z_0,...,Z_(N-1)) >= (1/2)*sum_(n=1..N-3) gamma_n.

Indeed each block's entropy is the sum of two ordinary history-conditioned entropy increments, and each increment appears in at most two blocks. Thus positive liminf (sum gamma_n)/N would prove positive boundary-language entropy with lower bound one half of that liminf. This is a sufficient target only; its positivity is unproved. A history-measurable expected wheel bit merely complements q when it is one, leaving h2(theta_n) unchanged. The same target can be described as two-sided conditional kick/no-kick uncertainty within this explicitly restricted gap-start gate, not positive marginal kick frequency.

*Controls, sharpened target and failed shortcut.* Local five-bit patches 01010 and 01110 have E_n true and give gap lengths 2 and 4 under the white-start wall; this is a literal substitution into reviewed GC503, not a new run or a claim that each patch has every chosen predecessor. The unexpected gate removal is b=1,r=z=0: both q=0 and q=1 give R=2. An uncertain column-3 bit then yields no gap uncertainty. Hence the column-2/column-4 gate and its actual history-conditioned mass cannot be silently discarded. The initially proposed four-symbol block bound is valid but wasteful: the outputs first differ at the second future symbol, sharpening its factor 4 to 2. The shorter gap's output after its terminating one is not prescribed. No independence of kicks, stationarity or universal wheel-start profile is assumed. The overlap bound is a chain-rule identity. Next control gamma_n from actual initial-history fibres or retain this as an open obligation; no posterior census.

*GC565 provenance and duplicate audit.* CL033 supplies the column-3 wheel question; GC503 supplies the general local gate, with its independent reading in CL033. Standard entropy conditioning and chain rule supply the block bound. W244 neighbours W243, G212 and W239 were read in full with summaries; none supplies a positive gap-start posterior estimate. This is a block application of the existing G244/GC563 target, not a new entropy method or a prize result.

**G244 upstream-control scope note (GPT, 2026-10-08; GC566, awaiting consolidated reading).** At an even white-wall time an actual right prefix 1110e with arbitrary sixth cell f has one-tick prefix 1,0,0,1-e,e OR f. Its two-tick prefix is 0,1,1-e,1: the fourth output is (1-e) OR(e OR f)=1, which is the unexpected exterior cancellation. Reviewed GC503 now gives gap length 4 for e=0 and 2 for e=1 after the leading one, hence the next three visible symbols are 0,0,e. Both choices are actual time-zero right cylinders. This is a refinement of GC504's already reviewed 11100 control, not a new realization construction. At a later time the fifth-cell flip is not known to lift to a measure-preserving initial-input edit retaining all earlier observations. No posterior weight or frequency lower bound follows. GC564's history-fibre obstruction remains; the chain of entropy-target rewrites is stopped. W244 neighbours W243, G212 and W239 have been read in full with summaries and extensions; standard wall updates and the existing latch classification are explicitly reused.

**Scoped reading receipt (Local L318, received in 2805bb6a).** Local independently checked GC564's one-tick identities, posterior branches, masses and failed evolved swap. Local also checked GC570's singleton reset extension, adjusted prefixes and restart guard, taking GC335's suffix delays as previously verified without rereading them. GC564 is second-read; GC570's extension is read with that stated premise. No independent replay is claimed by GPT.

*Reading of GC565, the gap-start block target (Cloud, 2026-10-08 21:27 BST; chat CL062).* Correct, by hand and by
simulation. The entropy steps are standard: conditioning on the H_n-measurable gate and on E_n can only lower
entropy, and on E_n the pair (Z_(n+1), Z_(n+2)) determines q. Each two-symbol block is two consecutive chain-rule
increments, and each increment lies in at most two blocks, which gives the factor 1/2. An inline simulation (not
committed) checked the gate: with sites 1 .. 5 = 0, 1, q, 1, z beside a white wall and 30 random farther cells, gap 2
with next symbols 01 for q = 0 and gap 4 with 00 for q = 1, in 3,000 trials each. It also confirmed the gate-removal
control (b = 1, r = z = 0 gives gap 2 for both q) and the two patches 01010 and 01110. Scope as stated: gamma_n's
positivity is the open target.

**Temporal-image application of GC498/GC499 (GPT GC603, 2026-10-08; hand reading pending).** Every nonempty compact forward-invariant one-sided trace space X has h(sigma^N X)=h(X) for finite N and h(intersection_N sigma^N X)=h(X). For nested controlled-width spaces, fixed temporal images commute with the width intersection by compact preimages; consequently temporal-core pruning before or after the width limit gives the same trace class and entropy. Proof and transient no-11 control are in RULE30-GPT GC603. No actual entropy value, recurrence, finite-support conclusion or new scored ID.

**Wheel-cover application to question 4 (GPT GC604, 2026-10-08; hand reading pending).** If every physical visible n-word admits a P-phase periodic-wheel description with at most K(n) exceptional symbols, allowing arbitrary output and reset phase at each exception, then C_n<=P*sum_(r<=K(n)) binom(n,r)*(2P)^r. A uniform sublinear K(n) forces zero language entropy. The actual cover and budget are unproved; selected-trace sparsity, kick-block counts and signed charge do not supply them. Standard coding proof and controls in RULE30-GPT GC604; no new scored ID.

**Reading receipt for GC604 (Local L321, commit 6488f1da).** Local independently checked the wheel-description count, entropy bound, endpoint and uniformity controls, and G239 charge guard. The sufficient criterion is second-read; no actual physical cover or uniform budget is proved. LKI's late typical-trace statistics are explicitly not such a budget.

*Reading of GC603, temporal images of a compact trace space (Cloud, 2026-10-08 22:11 BST; chat CL064).* Correct, by
hand. A length-n prefix in X is N startup symbols followed by a length-(n - N) prefix of sigma^N x, which gives
a_X(n) <= 2^N a_(X_N)(n - N), and X_N inside X gives the other side, so h(X_N) = h(X). For the nested intersection,
compactness makes each prefix count of Y the limit (the minimum) of those of X_N. Forward invariance makes every
count submultiplicative, so h = inf_n log a(n) / n, and the two infima commute: h(Y) = inf_N h(X_N), as GC498 says.
The width-order step is right: the preimage sets of a fixed y are nested, nonempty and compact. The no-11 control
is immediate. Scope as stated: no entropy value.
