# An aperiodic half-circle code passes every repeat test

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G143. An aperiodic half-circle
code passes every repeat test (2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and
this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

There is a particular way to turn an irrational rotation into black and white symbols that passes every repetition test we have required of the wall's neighbour. It is not periodic, its constant runs are at most two symbols long, and its number of distinct words grows only linearly. Differentiating it gives a Sturmian sequence, but some good rotation approximations flip every symbol instead of repeating it. Tracking that sign proves it passes the test at every period. This does not show that Rule 30 can produce it from a finite pattern; it shows that the repetition test alone cannot rule it out.

## The formal statement and proof

**Status and target.** Symbolic Q7 repeat-filter counterexample, independent review pending. No experiment run by GPT. HR0-HR3 were published for Local at d8bb640 before the requested finite test; Local L097 reports HR0, HR2 and HR3 PASS and HR1 HELD on that requested scope; the proof below is all-period and does not infer its conclusion from that test. Existing record: G137's sparse dyadic counterexample, GC158's failed XOR-derivative transfer, and Local L096's all-odd convergent guard. PRIOR-ART.md records the known Rote/Sturmian relation. This is an application to the wall's necessary repeat inequality, not a novelty claim about Rote sequences or a Rule30 realization.

Put beta=2-sqrt(2), alpha=beta/2 and r=sqrt(2)-1. Define

    c_s = floor(s*beta) modulo 2,    s>=0.

**Claim.** For every q>=1 and every interval of equality c_s=c_(s+q) on a<=s<=b, with a>=0,

    b < 2a+q.

Thus this aperiodic half-circle rotation code passes the wall's entire necessary repeat family even with constant C=0. It is not thereby a compatible finite-left companion. Its XOR derivative is the Sturmian mechanical word of slope beta, every constant run of c has length at most two, and its word-count entropy is zero. In particular this filter alone cannot exclude every nonsparse, low-complexity unrelated-endpoint rotation code.

**Mismatch intervals and reduction to records.** Choose the even integer P nearest q*beta and set epsilon=q*beta-P, so -1<epsilon<1 and epsilon is nonzero. With x_s={s*beta}, direct floor subtraction says a mismatch occurs exactly when

    epsilon>0: x_s in [1-epsilon,1),
    epsilon<0: x_s in [0,-epsilon).

For errors of the same sign, a smaller absolute error gives a smaller mismatch interval. Therefore it suffices to prove the claim at the successive same-sign error records: for any q choose a record q0<=q whose error has the same sign and no greater magnitude. A q-repeat interval avoids the larger mismatch interval, hence is a q0-repeat interval, giving b<2a+q0<=2a+q.

Here these records are among q=1, q=2, and the denominators listed below. To justify completeness, alpha=[0;3,2,2,...]. After its first denominator 3, consecutive convergents P/Q and P'/Q' form an integer basis, with opposite signed errors D,D' satisfying |D'|=(2+r)|D|, where Q'<Q. The next denominator is 2Q+Q'. Any pair (p,q) has the form m(P,Q)+k(P',Q'). If its error improves the current record of its sign, m and k must both be positive: opposite signs of coefficients add the error magnitudes, while a zero coefficient gives a multiple no better than a current record. With q<2Q+Q', m must then be one. For k>=2 the magnitude of D+kD' exceeds |D'|, so the only possible improving intermediate is m=k=1, the mediant. At the next convergent the induction repeats. Before denominator 3, the relevant nearest-integer periods are just 1 and 2. Scaling these errors by two gives exactly the even-integer records needed for beta; records with even larger error need not be retained.

Let p_n/q_n be beta's convergents, starting p_1/q_1=1/1 and p_2/q_2=1/2. For n>=2 all p_n are odd,

    q_(n+1)=2q_n+q_(n-1),
    delta_n=q_n*beta-p_n=(-1)^n*r^n.

The alpha convergents after denominator 1 are the even-numerator beta mediants

    Q_n=q_n+q_(n-1),    P_n=p_n+p_(n-1),    n>=2.

Their errors have sign opposite delta_n and magnitude E=(1+r)*|delta_n|. The intervening alpha mediants have beta denominators 2q_n and even numerator 2p_n. This follows by the displayed denominator recurrence (the first such denominator is 4). Hence the required candidate periods are 1, 2, Q_n and 2q_n for n>=2; proving more candidates than strictly set records is harmless.

**A return bound with its mesh proof.** Fix n>=2, put d=|delta_n| and Qnext=q_(n+1). Every block of Qnext successive orbit samples {s*beta} meets every half-open interval of length E=(1+r)*d. Indeed the Qnext orbit points have successive gaps d and d+|delta_(n+1)|=E. To see this directly, in the orientation given by the sign of delta_n, advance the index by q_n modulo Qnext. Without index wrap the circular distance is d; with wrap it is d+|delta_(n+1)|. Coprimality makes one cycle through all indices, and its total distance is

    Qnext*d + q_n*|delta_(n+1)| = 1

by the consecutive-convergent determinant identity. Thus this is the circular neighbor order and its largest gap is E. A half-open arc of length E contains a point even at a gap endpoint. Translating this mesh proves the block statement. It also holds for intervals of length 2d>E. Consecutive mismatch visits for either length therefore have time gap at most Qnext.

We also use the ordinary continued-fraction best-approximation fact already used in G134: for 0<k<q_n, the distance of k*beta to any integer is at least |delta_(n-1)|=(2+r)*d. Both E and 2d are smaller. So neither mismatch interval has a positive visit before q_n.

**Mediant periods Q_n.** The mismatch interval has length E and sign opposite delta_n. If it is the upper interval, its first visit is exactly q_n; if it is the lower interval, it contains time zero and its first positive visit is exactly q_n. In either case the samples at q_n land in it because their signed error has magnitude d<E. A repeat interval before that visit has b<=q_n-1<Q_n, and so satisfies the claim. For any later maximal repeat interval, write its preceding mismatch time as h>=q_n and the next mismatch time as h+g, with g<=Qnext. Then a=h+1, b=h+g-1 and

    b-2a-Q_n = g-h-Q_n-3
              <= Qnext-q_n-(q_n+q_(n-1))-3 = -3.

Subintervals only lower this debt. In the lower-interval case the first run starts at 1, making its bound still stronger.

**Doubled convergent periods 2q_n.** The mismatch interval now has length 2d and the same sign as delta_n. Its first positive visit lies between q_n and Q_n: there is no visit before q_n, and the mediant Q_n has the opposite signed error of magnitude E<2d, so it lands in the interval. In the lower-interval case time zero is also a mismatch. Any repeat before the first positive visit ends by Q_n-1<2q_n. Every later maximal repeat has preceding mismatch h>=q_n and gap g<=Qnext, giving

    b-2a-2q_n <= Qnext-q_n-2q_n-3
               = q_(n-1)-q_n-3 < 0.

This proves the claim for these periods too. For q=1 a match requires x_s<1-beta; its next sample is outside that interval because beta>1/2, so a match run has length at most one. For q=2 the nearest even displacement has epsilon=2beta-2<0, so a match requires x_s>=2-2beta. Its next sample wraps into [1-beta,beta), outside the match interval, and again every match run has length at most one. Both small periods satisfy the claim. The record reduction now proves it for every q.

**Complexity and the unexpected phase check.** The derivative g_s=c_s XOR c_(s+1) equals floor((s+1)*beta)-floor(s*beta), a Sturmian word. Thus c is aperiodic. Since beta>1/2, g contains no consecutive zeros, so c has no constant run longer than two. A length-m c block is determined by its first bit and the length-(m-1) g block. Hence P_c(m)<=2m and c has zero word-count entropy; no randomness statement follows.

The phase is essential. For c'_s=floor(s*beta+1/2) modulo2, the exact first 19 bits are 0110010011001001101. Period 7 repeats on [0,10] and fails at 11, giving debt 10-7=3. These finite values follow from adjacent-integer square-root bounds, the HR3 control preregistered in GC159; this is a direct algebraic check, not a new run or an all-phase conclusion. The period-q derivative lift counterfactual remains refuted by 0101... and its constant-one derivative.

**Scope.** The known half-circle code and the sparse dyadic word of G137 both pass the full necessary repeat family, by different mechanisms. Here numerator parity and mediant returns explain the gap. No initial-tail support theorem, full right extension, finite-left witness, positive-entropy theorem or prize conclusion is established. Q7 now needs a further wall or coupled-tail constraint to exclude this particular phase-zero code; stronger repetition arguments must specify a condition beyond the inequality just passed.
