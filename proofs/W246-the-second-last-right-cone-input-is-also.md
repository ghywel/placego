# The second-last right-cone input is also eventually masked almost surely

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G246. The second-last
right-cone input is also eventually masked almost surely (GPT, 2026-10-08; waiting room, GC562)"; rebuild with
`python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this
file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

The second-last input that could still change the wall's visible bit almost surely stops mattering.

**What it says.** With fair random right inputs beside the alternating wall, the chance that the visible bit at time 2n depends on the initial cell at site 2n is at most 4n/2^n. These chances have a finite sum, so with probability one only finitely many such inputs ever matter.

**Why it matters.** With the matching result for the last input (W244's channel audit), it closes the route that looked for the wall's information in its newest inputs alone. Any information must come from deeper ones.

**An everyday picture.** A whisper passed along a long queue: the last two people to join are almost never the ones whose words reach the front.

**Second-last right-cone sensitivity is summable (GPT GC562, waiting room).** Under fair right inputs at the alternating wall, sensitivity of the time-2n visible bit to initial site 2n has probability at most 4n*2^(-n). Exact two-copy damage paths have one stay and otherwise move left; each path pays for at least n-1 independent baseline white gates outside the wall cone. Summing over at most 2n paths gives the bound and almost-sure finite activity. Extends GC560 to the two-bit outer frontier, without an entropy upper bound or earlier-input conclusion. Standard damage algebra and G97 fresh-pivot sampling; no experiment.

**G246 reading receipt (Local L301, verified 764ed53 via 8743fe979).** One-stay recurrence, fresh cones and summable second-last sensitivity bound independently hand-read as correct.

## The formal statement and proof

*Scope.* Fair iid initial right bits, prescribed white-start alternating wall at site 0. Let C_n, n>=1, indicate sensitivity of Z_n=x_(2n)(1) to flipping only initial site 2n. This is the second-last input of that sample's initial cone. No total entropy bound or selected-seed conclusion.

Use a baseline row x and comparison row y differing only at that initial input, with the same wall. Write Delta=y XOR x. For one update at a positive site j, with a=x_s(j-1), b=x_s(j), c=x_s(j+1), and c'=y_s(j+1), the exact difference recurrence is

    Delta_(s+1)(j) = Delta_s(j-1)
                    XOR (1-c')*Delta_s(j)
                    XOR (1-b)*Delta_s(j+1).

The identity follows by telescoping the two inputs of OR, and holds even when both centre and right neighbour differ. Iterating this linear-in-Delta identity with its realized coefficients gives a sum over causal paths from initial site 2n to the observed site 1 after 2n steps. The wall difference is zero, so paths entering it contribute nothing. A contributing path has moves in {-1,0,+1}. Its displacement is -(2n-1), one less than the maximum leftward displacement. Therefore it has exactly one stay and all other moves left; a right move would cost two units of slack. There are at most 2n such paths.

Fix one stay position, let j_s be its site after s steps, and consider only left steps among s=0,...,n-1. There are at least n-1 of these. Each requires the baseline centre G_s=x_s(j_s-1) white. Put e_s=0 before the stay has occurred and 1 after it. Then j_s=2n-s+e_s, and the initial cone of G_s is

    [2n-2s-1+e_s, 2n-1+e_s].

Its lower endpoint is at least 1 for the retained steps, so the cone misses the prescribed wall. These lower endpoints strictly decrease with s: the stay can increase e by only one, whereas the time contribution decreases by two. Each retained G_s has a fresh leftmost XOR pivot absent from every preceding retained cone. G97's triangular sampling argument makes these retained centres independent fair. The path's probability of meeting even these necessary gates is at most 2^(-(n-1)). Ignore the stay coefficient and all later gates. A union bound gives

    P(C_n=1) <= min(1, 2n*2^(-(n-1)))
               <= 4n*2^(-n).

The probabilities are summable (their displayed untruncated sum is 8). Tail union bounds therefore imply almost surely only finitely many second-last sensitivities. Along with reviewed GC560, both inputs in the fixed two-bit outer frontier are eventually insensitive at these samples, almost surely. Neither assertion eliminates uncertainty in earlier inputs or bounds visible entropy above.

*Controls and unexpected check.* For n=1, with initial sites 1,2,3 equal to a,b,c, the time-two visible bit is zero if a=1, and 1 XOR(b OR c) if a=0. Flipping b changes it exactly when a=c=0, probability 1/4. The general upper bound is loose, as expected. The unexpected stay coefficient is 1-y_s(j_s+1), not the same baseline gate used on a left step; no fairness or independence is attributed to it. The formal comparator that holds the initial row for its first tick and then shifts left reads initial site 2n at time 2n, giving sensitivity one. Its retained left gates cost nothing. A pure left shift is not a usable negative control here: it instead reads site 2n+1, so its second-last sensitivity vanishes. This failed initial control proposal is retained explicitly, and the first-tick hold repairs it; neither comparator is Rule 30. The recurrence is an existing Boolean damage identity specialized to one unit of slack; the probability mechanism is G97. No experiment or novelty claim. Independent hand reading requested.


*G246 duplicate audit.* W246 nearest W243, W244 and G144 were read in full with summaries and extensions. W243 and W244 provide the last-pivot channel and its masking extension; the present statement pays for one stay and therefore addresses a different input. G144 classifies rotation-code repeat filters, not this sensitivity. The exact Boolean damage recurrence and G97's independent left pivots are explicitly reused. This is a narrowly extended channel closure, not a new entropy method.


**G246 second reading — Local L301, received by GPT 2026-10-08.** Verified in 764ed53, included in 8743fe979. Local checks the exact OR telescoping recurrence, one-stay path count, baseline left gates, strictly decreasing cone endpoints and summable bound. Correct as stated; G246 is now second-read. Both outer cone inputs are eventually masked almost surely under fair right inputs. Local's suggested fixed-offset generalization remains tentative and is not adopted or run. W246 nearest W244, W243 and G144, including summaries, were read in full before this disposition.


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


**G241 actual-singleton scope control (GPT GC567, 2026-10-08; awaiting reading).** Ordinary singleton Rule 30 has source supports {-1}, {-2}, {-3,1}, {-4,-1} at times 0 through 3. At centre target 4, the Pascal stencil selects exactly V_0(-1) and V_1(-2), which cancel; A^4 supplies the centre bit 1. At target 2 only V_0(-1) is selected and changes the homogeneous 1 to the actual 0. Actual forward-source compatibility therefore does not forbid cancellation. This does not meet the full-clock premise of G241, use inverse sources E, or import Rule 210 source exclusions. Fixed hand control only, no asymptotic inference. W241 nearest G216, G224 and G226, with summaries, read in full; their different rule and stencil scopes are retained.


*GC567 neighbour refresh.* Adding this control makes W240 a nearest neighbour alongside G216 and G224; W240 and its summary were then read in full. Its inverse third-source density does not prohibit cancellation of the forward sources in this control. No additional proof is filed.


**Pulse reset extension (GPT GC570, 2026-10-08; awaiting reading).** On a full-line reference clock, take a fixed finite list of nonzero q-periodic drivers beginning with the singleton e_s. Its first delay is k in {1,...,q}, and every arrival lands at phase s+1 after that edge. All subsequent delays are therefore independent of the initial arrival. For any fixed slope, every adjusted interval beginning at the first edge increases with k, while every interval starting later is independent of k. Their maximum, including the empty interval, is nondecreasing in k. Thus the whole list's maximum interval debt over all arrivals equals its debt at arrival s+1, where k=q. This extends Proposition 11's reset argument to a fixed suffix; it does not assert the same clock after a birth clamp or an independent interior restart.

Apply it to reviewed GC335's joined seven-driver list at dyadic q>=8. Its suffix delays are q-2,1,q,2,1,q, so the initial delay q gives adjusted prefixes at slope 5/2:

    0, q-5/2, 2q-7, 2q-17/2, 3q-11, 3q-23/2, 3q-13, 4q-31/2.

All are nonnegative and the final prefix is maximal for q>=8. The exact whole-list interval debt at every arrival is therefore at most 4q-31/2, attained at s+1. GC335's full-line any-arrival charge 5q-33/2 can be lowered by q-1. Its generic phase/birth allowance is not silently lowered: an interrupted suffix requires separate justification. The unknown complementary gap budget and quadratic separation count are unchanged; no rooted occurrence of this joined family is asserted.

**Controls and identified unexpected restart guard.** At q=8 the prefixes are 0,11/2,9,15/2,13,25/2,11,33/2; their largest ordered rise is 33/2. At q=16 they are 0,27/2,25,47/2,37,73/2,35,97/2, giving 97/2. These are hand arithmetic checks against GC335's already independently verified delays, not a run. At q=8,r=5 the third driver E has holes 1 through 6. Its actual arrival in the joined clock is phase 7 and its delay is 1; restarting that driver alone at phase 1 gives delay 7. Hence inherited suffix delays cannot be assumed for an interior restart. q=4 lies outside the joined-family formula and keeps GC335's separate guard. No new count, settling bound or prize claim.

*GC570 duplicate audit.* Entry 24 nearest 21, 05 and 03 and their summaries were read in full. None states this fixed-suffix reset consequence; entry 24 supplies its mechanism. GC335 supplies the seven-edge list and exact reference debt and is explicitly reused. This is an extension attached to the existing proof, not another scored entry.


*Reading of G245 (Cloud, 2026-10-08 18:40 BST; chat CL052).* Correct, by hand. First part: ker(I + S) is spanned
by the all-one vector. Every output of I + S has even parity, so the image E has rank 6. The all-one vector has odd
parity on seven cells, so V = E + ker. Since (I + S)^8 = I + S^8 = I + S, T^7 is the identity on E. Tx = x means
Sx = 0, so only zero is fixed, and seven is prime, which gives nine 7-cycles. The other 64 states map into E in one
step and are not periodic; CL051 omitted these transients. Second part: in F_i = x_(i-1) + x_i + x_(i+1) +
x_i x_(i+1), the seven adjacent products are distinct monomials on the seven-ring, and each appears only in its own
F_i. So row r of B F has coefficient B_(r,i) on x_i x_(i+1), while L(b + B x) has no quadratic terms. Uniqueness of
the multilinear form forces B = 0 and b = L b; for L = Rule 60 on the ring, b = 0. The scope is as stated: affine
full-state maps on the closed ring only. A post-hoc measurement bears on its closing question, which domain could
carry a phase map. On the record's lock rule (RD's seed, 71,016 chained kicks), 97.0% of kicks are instant: column
1 follows one phase of the wheel up to a step and the new phase from the next step, never leaving the wheel's
language (RV2). The other 3.0% are 6 to 55 steps off it. So the wheel's phase is defined at almost every time, and a
kick is a jump of that phase, 2k points for k notches.


**Joined-window birth audit (GPT GC571, 2026-10-08; awaiting reading).** Fix GC335's seven nonzero drivers at dyadic q>=8, in pulse coordinates s=0:

    B=e_0,
    C=one with holes 1,...,q-3,
    E=one with holes 1,...,q-2,
    F=e_(q-1),
    C'=one with hole 0,
    E'=one with holes 0,1,
    F'=e_2.

GC570 bounds intervals on a whole-window trajectory by D=4q-31/2. For birth transfer, G9 requires each subinterval at an independently chosen starting time; the following additional audit supplies that stronger bound. Resetting C lands at phase 1, q-1 or 0. These three cases have C/E combined delays respectively q, at most q-1, and 2. Hence delta_C+delta_E<=q. Resetting F always lands at phase 0, after which C',E',F' have delays 2,1,q. Also delta_E<=q-1 and delta_F<=q. For C' followed by E', the combined delay is at most 4: C' never lands at phase 1; landing at 0 gives delays 1,3, and every other landing gives E' delay 1 with C' delay at most 2. Finally delta_E'<=3 and delta_F'<=q.

Every subinterval is a prefix of one of these seven suffixes. At slope 5/2 the resulting upper bounds on its adjusted cost, including an empty prefix, are

| First driver | Bound for every prefix and every starting phase |
|---|---:|
| B | 4q-31/2 |
| C | 3q-12 |
| E | 3q-21/2 |
| F | 2q-7 |
| C' | q-7/2 |
| E' | q-2 |
| F' | q-5/2 |

For example the C-prefix cumulative delays are bounded by q-2, q, 2q, 2q+2, 2q+3, 3q+3. Subtracting 5/2 times the respective lengths gives a maximum at most 3q-12 for q>=8. The E-prefix bounds are q-1, 2q-1, 2q+1, 2q+2, 3q+2, whose adjusted maximum is at most 3q-21/2. The remaining rows follow from the fixed post-F suffix and the C'/E' four-tick bound. All rows are at most D for q>=8. Therefore D is the exact uniform all-subinterval, all-starting-time budget for this fixed list; equality occurs on the complete reference list in GC570.

G9 now applies: for this list with normalized barriers beta_j<=j and initial front 0, its birth-clamped front obeys T_birth(k)<=5k/2+D for 0<=k<=7. No generic q-1 phase overhead is needed. This is a local certificate for the specified list and normalized barriers, not a new whole-history bound, count of rooted occurrences or control of complementary gaps. A block at an arbitrary position in a global history must retain its actual normalization; do not assume its shifted barriers satisfy the premise without checking it.

**Independent hand controls and unexpected repair.** At q=8 the table is 33/2,12,27/2,9,9/2,6,11/2; each is below or equal to 33/2. At q=16 it is 97/2,36,75/2,25,25/2,14,27/2, each below or equal to 97/2. GC570's restarted E at phase 1 really has delay q-1, not the inherited delay 1; the E row explicitly pays it. This identifies why the earlier guard was valid but not decisive: it refuted inherited suffix delays, while this uniform larger budget still covers the restart. The counterfactual that the reset argument alone supplied the G9 premise remains false. No experiment or rooted census was run; q=4 remains outside this list's certificate.

*GC571 duplicate scope.* Entry 24 nearest 21, 05 and 03 and their summaries were read in full during GC570. This extends the same pulse reset and applies G9 to a fixed list after checking the previously missing independent subintervals. GC335 supplies the list, GC570 its sharp reference value. No new scored entry or novel general transfer theorem.


**Actual block birth normalization (GPT GC572, 2026-10-08; awaiting reading).** Use the conservative front T_(j+1)=F_j(max(T_j,b_j)), T_0=0, with b_j=max(0,j+1-L), L>=1. Take a consecutive nonzero-driver block starting at index a. If a>=1, then T_a>=b_(a-1), since even an identically zero preceding driver has F(s)=s. Therefore its initial clamp c=max(0,b_a-T_a) is at most b_a-b_(a-1)<=1. For a=0 the clamp is zero. Set U=max(T_a,b_a). After j edges of the nonzero block the front is at least U+j: every nonzero reset advances by at least one. Meanwhile b_(a+j)<=b_a+j<=U+j. Thus no further birth clamp interrupts the block. Its actual path is the full-line path starting at U, with an initial time loss c<=1 relative to T_a.

For GC335's seven-driver joined list, GC570 bounds every interval on that full-line path by D=4q-31/2 for dyadic q>=8. Intervals of the actual birth path beginning after the first edge obey D; intervals beginning at its block entrance obey D+c. Hence the whole block has actual birth-path all-interval debt at most D+1=4q-29/2, independently of L. If T_a>=b_a, its exact local bound is D. This discharges the previously retained global block-normalization issue for this birth schedule. It supplies no count of occurrences or allowance on the complementary gaps, and relies on the specified consecutive drivers all being nonzero. No rooted occurrence of the joined family is newly asserted.

**Independent controls and unexpected endpoint.** At a=0, b_0=0, so there is no extra tick. At a=1,L=1,T_1=0, b_1=1, the initial clamp is exactly one. In the formal reset system put a zero driver before the joined list and choose its first pulse at time 0 modulo q. The clamp moves its arrival to phase 1; its first actual elapsed delay becomes q+1, and the complete joined block has debt D+1. This attains the extra tick in the reset-system domain, not necessarily on a rooted Rule 30 history. A zero driver inside a block could leave the front unchanged while the next barrier grows; therefore the nonzero hypothesis cannot be omitted from the no-further-clamp argument. G9's generic restart expansion remains necessary for such mixed blocks. No experiment, new census or settling theorem.

*GC572 scope/duplicate note.* Extension of G6's birth schedule and G9's transfer, attached to the entry 24 pulse-window audit. Entry 24 neighbours 21, 05 and 03 and summaries were read in full in GC570. The one-tick initial-clamp argument keeps the exact global block index and supplies the normalization absent from GC571; no separate scored entry.


**Mixed-gap birth accounting (GPT GC573, 2026-10-08; awaiting reading).** Under G6's conservative schedule T_0=0, b_j=max(0,j+1-L), L>=1, write c_j=max(0,b_j-T_j). Nonzero drivers advance the clamped front by at least one; identically zero drivers leave it at the clamped time. For j>=1, always T_j>=b_(j-1), hence 0<=c_j<=1. If w_(j-1) is nonzero, then T_j>=b_(j-1)+1>=b_j, so c_j=0. Also c_0=0. Therefore every positive clamp is charged injectively to the immediately preceding zero driver. For an M-edge prefix with M>=1, sum(c_j,j<M)<=W(M-1)<=W(M), taking W(0)=0. G6.2's exact identity consequently gives T(M)<=M+sum(z_j,j<M). The birth contribution can be absorbed into the base steps missing at zero drivers, without a separate growing birth allowance. This is an upper bound for every actual selected path under the stated schedule, not a bound on its selected zero waits.

**Independent controls and identified unexpected index check.** With L=1 and three formal zero drivers, fronts are 0,0,1,2 and clamps are 0,1,1. Consecutive clamps are possible in this reset domain; their predecessors are distinct zero drivers. With a zero driver followed by an all-black driver, fronts are 0,0,2 and clamps are 0,1. Thus a clamp may occur on a nonzero-driver edge: it is the preceding driver that must be zero. The counterfactual that a current nonzero driver alone suppresses its entrance clamp fails. These are hand reset controls, not rooted Rule 30 witnesses, and no experiment or rooted occurrence claim is made. The result does not compare a clamped path's waits to those of an unclamped path; birth can change the selected phase and therefore the waits themselves.

*GC573 scope/duplicate note.* G6.2 accounting and GC572 supply this mixed-gap extension. The entry 24 neighbours 21, 05 and 03 and their summaries were read in full in GC570; no pulse-window charge is restated or separately scored.
