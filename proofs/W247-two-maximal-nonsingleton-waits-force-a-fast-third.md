# Two maximal nonsingleton waits force a fast third edge

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G247. Two maximal nonsingleton
waits force a fast third edge (GPT, 2026-10-08; waiting room, GC575)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Two longest possible waits for rows with more than one black cell force the following wait to be short.

**What it says.** In a repeating row of q cells containing at least two black cells, the longest reset delay is q-1. If two compatible successive rows both attain it along the same uninterrupted clock, the next row is black at its arrival, so its delay is one.

**Why it matters.** Compatibility restricts consecutive extreme waits. But the three delays still add to 2q-1, so this fact alone gives no average-speed bound independent of the period.

**An everyday picture.** Three traffic lights on a route: the timing of two long stops can require the third light to be green when you reach it. That green light does not refund all the time already spent waiting.

**G247 reading receipt (Local L305, verified 36f7bc519c20).** Both supports, forced third bit and endpoint arithmetic independently checked; second-read in its original full-line scope.

G247 extension GC594, awaiting reading: consecutive delays a,b with a+b>q and b<q force the next compatible driver black at inherited arrival. The first driver may be singleton. Three ordinary nonsingleton waits total at most 2q-1. Strict crossing, the second delay guard and uninterrupted births matter; the bound is period-dependent and gives no rooted frequency or global Q7 conclusion.

G247 extension GC595, awaiting reading: ordinary blocks have no internal conservative birth clamps; GC594 applies after their entrance phase changes. Whole-prefix cost sums their triple envelopes plus singleton waits and one global zero-driver clamp charge. At common period four, slope-5/2 debt is <=1+(5/2) times singleton count. No bound on that count or generalization to larger periods is proved.

**G247 / GC596 extension (awaiting reading):** conservative common-q prefixes satisfy T-gamma M<=2(q-1-gamma)+(3q-2-3gamma)P for (2q-1)/3<=gamma<=q-1. Zero separators cancel at the same threshold as triples. This envelope yields sub-three only for dyadic q=2,4; it is no dynamical lower bound.

## The formal statement and proof

*Where:* RULE30-GPT.md, GC575. *Bears on:* Q7 selected waiting budget. *Status:* hand proof awaiting independent reading.

**Statement and proof.** Let q>=4 and let B,C,D be q-periodic temporal words satisfying D(t+1)=B(t) XOR (C(t) OR D(t)). Assume B and C each have at least two black residues. On a full-line reset path beginning at time T, suppose B and then C each have delay q-1, with no intervening birth clamp. A nonzero reset waits until the first black and then advances one tick. The first delay therefore leaves B zero at residues T through T+q-3 and black at T+q-2. Since B has at least two black residues, its only remaining residue T+q-1 must also be black. Thus B's support is exactly {T-2,T-1} modulo q. The next arrival is T+q-1, and the same argument gives C's support exactly {T-3,T-2}. The third arrival is T+2q-2, congruent to T-2. At time T-3 the recurrence gives D(T-2)=B(T-3) XOR (C(T-3) OR D(T-3))=0 XOR 1=1. Therefore every compatible next driver has reset delay 1 at this inherited arrival. The three elapsed delays sum 2q-1. No power-of-two period, gate, rooted ancestry or weight assumption on D is needed; existence of a periodic D is not asserted for arbitrary B,C.

**Controls and identified unexpected scope check.** GC362's q=8 pair B=192,C=96 has arrival residues 0,7,6 and forces D(6)=1 regardless of D(5). This locates why GC574's D=48 fails. At q=4, B=12,C=6 similarly force D(2)=1 from t=1; the wraparound argument survives. The OR latch is an independent local check: C(T-3)=1 erases the free D input. At slope 5/2 the complete three-edge debt is 2q-17/2, still positive for q>=5 and unbounded with q. Hence the forced fast third edge does not pay the two extreme waits by a period-independent constant. These are hand checks, no new run. Birth interruption can change the third arrival and is outside this full-line statement.

*G247 duplicate audit.* Nearest entries 25, G162 and W246, including their full proofs, summaries and attached extensions, were read. Entry 25 counts runs next to a pulse; G162 counts post-split run lengths; W246 bounds a right-cone sensitivity. None states this ordinary two-maximal-wait implication. G6 reset arithmetic, GC362's pair and the existing OR latch are explicitly reused; no new mechanism or prior-art priority claim.


**G247 second reading (Local L305, verified 36f7bc519c20; received by GPT 2026-10-08).** Local independently checks both forced two-black supports, the inherited third arrival, the OR latch forcing D(T-2)=1, the total 2q-1, and the q=8 and q=4 controls. Correct with the uninterrupted full-line scope retained. G247 is second-read; selected near-extreme waits and a global debt bound remain open.

**G247 long-pair extension (GPT, 2026-10-08; GC594, awaiting reading).** Let q>=2 and B,C,D be q-periodic words satisfying D(t+1)=B(t) XOR (C(t) OR D(t)). B and C are nonzero. On an uninterrupted full-line reset path arriving at B at time T, let their consecutive delays be a,b. If a+b>q and b<q, then D is black at the inherited third arrival S=T+a+b, so its delay is one. No weight assumption on B or D is needed. C having at least two black residues suffices for b<q; this condition can also hold for a singleton at a favourable arrival.

**Proof.** Translate T to zero. B is zero at residues 0 through a-2 and its first black is at a-1. C's first black at its arrival a occurs at a+b-1, so C(S-1)=1. Put h=a+b-1-q. Since a+b>q, h>=0; since b<q, h<=a-2. Also a<=q,b<q imply S-1<2q, so this is the correct residue, not an extra wrap. Consequently B(S-1)=B(h)=0. The recurrence at S-1 gives D(S)=0 XOR 1=1, independent of D(S-1). This extends G247 from two maximal waits to every pair crossing the common-period threshold.

**Near-extreme and ordinary-gap consequences.** Writing a=q-1-alpha and b=q-1-beta, the sufficient condition is alpha+beta<=q-3. For any compatible three ordinary drivers, each nonzero and with at least two black residues, their elapsed delays sum to at most 2q-1: if a+b>q the third delay is one; otherwise it is at most q-1. A fixed uninterrupted list of M ordinary drivers therefore has total delay at most floor(M/3)*(2q-1)+(M modulo 3)*(q-1), by disjoint triples. No compatible infinite repetition attaining this arithmetic envelope is asserted. The bound still scales with q and does not supply the period-independent slope or rooted frequency needed for Q7. Birth clamps and zero/singleton drivers require their existing separate accounting.

**Hand controls, counterfactual and identified unexpected checks.** Temporal masks use time zero as the low bit. At q=4, B=10,C=9,D=2 satisfy the recurrence with delays a=b=2 and inherited third delay two: a+b=q, so the strict threshold cannot be weakened to equality. Removing b<q fails at B=12,C=4,D=7: delays are 3,4,2, even though a+b>q. Both controls follow by checking the four cyclic recurrence equations. Unexpectedly the first driver may be singleton: B=8,C=6,D=12 have delays 4,2,1 and satisfy the same four equations. This confirms that G247's first weight assumption is unnecessary for the extension. These are compatible periodic triples, not rooted or birth-interrupted paths; no computation ran. At q=4 and q=8 the ordinary three-edge envelope is respectively 7 and 15, matching G247's existing maximal-pair arithmetic.

*GC594 duplicate disposition.* G247 nearest 25,G162,W246 full proofs, extensions and summaries were read for GC575 and retained here; the advisory is unchanged. This is a stronger local consequence of the same OR latch, not a new waiting model or global compensation claim.

**G247 conservative-birth transfer and period-four pulse budget (GPT, 2026-10-08; GC595, awaiting reading).** Use G6's schedule T_0=0, b_j=max(0,j+1-L), L>=1. Fix a common period q for a finite compatible driver prefix. An ordinary driver is nonzero with at least two black residues modulo q; let maximal ordinary blocks have lengths m_i. Write P for the number of singleton drivers and W for zero drivers. GC572 makes each ordinary block uninterrupted after an entrance clamp of at most one tick: it is the full-line path starting at the clamped entrance. GC594 applies to that new starting phase, not the unclamped one. Put

    F_q(m)=floor(m/3)*(2q-1)+(m modulo 3)*(q-1).

The reset delays within ordinary block i total at most F_q(m_i). Every singleton reset delay is at most q; every zero driver has reset delay zero. GC573 bounds all entrance clamps together by W(M-1), the zero count among the first M-1 drivers. Therefore for the M-edge prefix

    T(M) <= sum_i F_q(m_i) + q*P + W(M-1).

No clamp is added separately per block in this global expression. It would count the same birth cost twice. This uses the specified schedule and common period, not a generic barrier with arbitrary jumps.

**Period four.** Let K=sum_i floor(m_i/3) and R=sum_i (m_i modulo 3), so the ordinary count is O=3K+R and T(M)<=7K+3R+4P+W for q=4. The number B of nonempty ordinary blocks is at most P+W+1, and R<=2B. With M=3K+R+P+W, subtracting (5/2)M gives

    T(M)-(5/2)M <= -(1/2)K+(1/2)R+(3/2)P-(3/2)W
                       <= 1+(5/2)P-(1/2)K-(1/2)W
                       <= 1+(5/2)P.

Thus a common-period-four prefix without singleton drivers has whole-prefix slope-5/2 debt at most one, even with zero separators and their births. More generally singleton count alone pays the remaining upper allowance in this fixed-period estimate. This is not a bound on the singleton count or the periods of an actual rooted history. It does not transfer the constant to q>=8.

**Hand controls, counterfactual and identified unexpected saving.** For a single uninterrupted ordinary q=4 block, GC594 gives adjusted cost at most -floor(m/3)/2+(m modulo 3)/2<=1. Its birth path has block debt at most two. The ordinary pair B=12,C=6 at arrival zero has delays 3,3 and debt one; D=7 supplies a compatible next word, so the full-line endpoint allowance cannot be deleted. With L=1 a zero driver followed by an all-black driver has fronts 0,0,2: the nonzero entrance clamp is real, refuting the counterfactual that ordinary drivers never pay a clamp. Nevertheless its two-edge global debt is negative. Unexpectedly counting the preceding zero's missing reset delay absorbs all block entrances in the global period-four bound, improving the crude sum of two per-block allowances. These are hand reset controls, not rooted occurrences; no computation ran.

*GC595 duplicate disposition.* G247 nearest 25,G162,W246 full readings and summaries are retained. GC572 and GC573 already prove the birth normalization and clamp charge; this extension combines them with GC594's new compatibility bound, without reopening unsigned-charge or named-window refinements. All statements await reading in this combined scope.

**Reading receipt for GC594 (Local L311, 2026-10-08; received through commit 188ec664).** Local independently verified the long-pair proof, all three cyclic period-four controls, and the ordinary triple envelope by hand. The GC594 extension is second-read in that scope. GC595 remains awaiting reading.

**G247 affine mixed-prefix envelope (GPT, 2026-10-08; GC596, awaiting reading).** Keep GC595's conservative schedule and common-period prefix, q>=2. Let P,W count singleton and zero drivers. Choose a slope gamma in [(2q-1)/3,q-1]. Write K=sum floor(m_i/3), R=sum (m_i modulo 3) over maximal ordinary blocks. GC595 gives T<= (2q-1)K+(q-1)R+q P+W and M=3K+R+P+W. Set delta=2q-1-3gamma<=0 and a=q-1-gamma>=0. Since R<=2(P+W+1), direct subtraction gives

    T-gamma*M <= delta*K+a*R+(q-gamma)*P+(1-gamma)*W
                  <= 2a+(3q-2-3gamma)*P+delta*(K+W)
                  <= 2(q-1-gamma)+(3q-2-3gamma)*P.

The zero-separator coefficient after paying the two possible leftover ordinary edges is exactly delta, the same coefficient as a full ordinary triple. Thus zeros cancel at precisely the triple-envelope slope threshold in this argument. No extra per-block clamp allowance is needed. At gamma=(2q-1)/3 this becomes

    T-((2q-1)/3)*M <= 2(q-2)/3+(q-1)*P.

**Hand controls, failed counterfactual and identified threshold check.** At q=4,gamma=5/2 the formula reproduces GC595's 1+(5/2)P. At q=2 the interval has just gamma=1 and gives T-M<=P, including the degenerate all-black ordinary word. At q=8 the lowest slope this argument certifies is five, with allowance 4+7P; it is not a sub-three estimate. Unexpectedly the threshold reaches three already at q=5, so among dyadic periods q>=2 this method yields a sub-three slope only at q=2,4. That is a limitation of the envelope proof, not a lower bound on actual rooted slopes. GC362's q8 pair already has P=0 and debt nine at slope 5/2, refuting literal transplantation of GC595's period-four constant one. Its debt remains O(q), so it does not refute a period-scaled pulse-free budget. GC370's actual reported period-32 segment likewise has no pulses and positive debt 78.5; its finite literal audit is retained, not rerun or promoted to an asymptotic obstruction.

**Disposition and duplicate check.** G247's nearest 25,G162,W246 full readings remain retained; GC572-GC575 and GC594-GC595 supply all dynamical inputs. This is the affine accounting consequence, not a new scored theorem or experiment. Close the attempted all-period sub-three extension from the triple envelope alone. The open input is stronger multi-edge compensation or a selected-history frequency bound; no actual slope lower bound is proved.

**Scoped reading receipt for GC595 (Local L312, commit 0b4b59cf, 2026-10-08).** Local independently verified the prefix assembly conditional on GC572 and GC573, and all period-four budget arithmetic. Local explicitly has not read those two birth premises. The conditional arithmetic is second-read; the complete birth chain is not yet independently verified. GC596 remains awaiting reading.

**Reading receipts (2026-10-08; L313 and CL056, received in 11195c70).** Local L313 independently checked GC572 and GC573 by hand, including their two birth controls. With the earlier conditional L312 receipt, GC595 is now second-read throughout. Cloud CL056 independently verified G248 and GC582 by hand and reports their RG248 replay controls passing. The separated-lock extension has a hand reading only: all sampled pairs were chained, so that unexpected empirical check was vacuous. GPT received the replay report without rerunning it; the reported nearest-gap correction preserves parity.

**Reading receipt for GC596 (Local L317, commit 6bbd6635).** Local independently checked the affine subtraction, remainder bound, equal zero/triple coefficient, all stated endpoint controls and the sub-three threshold. The extension is second-read with its method-limit scope; no actual slope lower bound is inferred.
