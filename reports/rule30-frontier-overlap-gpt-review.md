# GC2002 — review of L1061–L1062: the structural connection carries

28 October 2026. Complete entries, report, probe, PROOFS.md item 36 and the relevant 8.27/8.73 sources read. No numerical rerun. Owner explicitly values understanding and discovery independently of prize progress; that is the criterion for continuing this question. The surviving mathematical connection is worthwhile on that basis.

## 1. The frontier and the edge triangle are the same boundary

L1062 section 1 carries. For P=2^v and B the first index with p_B not dividing P, all earlier diagonals return to their initial zero at time P. The forcing at B is P-periodic, and its P-step parity is one, so D_B(P)=1. Hence the white run immediately inside the edge has length B-1:

    B(P)=L(P)+1=w(v)+1.

Proposition 23 already proves this and the all-phase flip used in GC1998. My earlier reconstruction review should have credited that exact argument; it now does. The past interpretation joins two existing descriptions rather than supplying a new independent frontier theorem. This is an explanatory gain, even without a prize consequence or a novelty claim.

Indexing matters: an n-bit prefix c(0),...,c(n-1) is covered when B(P)>=n, equivalently w(v)>=n-1. To place all those copies strictly before time zero also require P>=n. If the desired prefix includes c(n), use w(v)>=n and P>n instead. Equality is guaranteed below B and fails at B; later bits may agree again. 'Equals exactly for n<B' should mean the maximal initial agreement interval, not an assertion that all later bits disagree.

The exact ruler identity supplies no asymptotic logarithmic law. The report's 'logarithmic frontier', 'OR shrinks ... to a logarithmic one', and resulting exponential readout-cost wording must remain measured descriptions. The Rule 60 comparison B(P)=P is exact; a universal asymptotic contrast with Rule 30 has not been proved here. Likewise the literal inverse depth is not a lower bound for every possible algorithm.

## 2. Parity reduction carries, with the driver period specified

All sums here are modulo two. At the frontier,

    pi(D_(B-1) D_(B-2))=1+pi(D_(B-1))+pi(D_(B-2)).

The three weight cases carry for P>=4 if q_k means the least period of the FORCING g_k, and 'doubled' means p_k=2q_k. A feeder with p_k<P repeats an even number of times. A feeder with p_k=P=2q_k complements after P/2 ticks and therefore has exactly P/2 black cells, an even number. In the remaining case p_k=P=q_k its weight parity is unresolved by those facts. For P=2 the half-period weight is odd; the stated P>=4 guard is essential.

Thus overlap is one whenever both feeder weight parities vanish. An inherited full period allows an exception but does not force one: its weight could still be even, or two odd feeder weights could cancel.

A small exact consequence sharpens the measured H2 without assuming monotonicity. At B, q_B divides P and p_B is either q_B or 2q_B. Since p_B does not divide P, necessarily

    q_B=P,  p_B=2P,  max(p_(B-1),p_(B-2))=P.

The last equality follows because q_B divides the least common multiple of the feeder periods, both of which divide P. This is already implicit in Proposition 23. It proves that at least one feeder has the full period. The stronger orientation p_(B-1)=P and the P/2 alternative for the other feeder remain unproved here.

## 3. The proposed impossibility conclusion does not follow

The explicit reduction contains off-centre terms. That establishes that this calculation has not supplied a closed relation among the centre bits. It does not establish that no such relation or cheaper evaluation exists, or that a full period must be read. In many of its own weight cases the overlap already reduces to the known constant one. The remaining inherited-weight cases need an additional argument, not a declaration that all reductions are impossible.

L1061's proposed test did not specify a class of allowable formulas or a lower-bound argument excluding them. A bounded unsuccessful attempt cannot settle that negative prediction. Replace 'prediction holds / conjecture settled' by 'this reduction leaves inherited-period weights unresolved; no centre recurrence was obtained'. The suspicion of conserved difficulty remains a conjecture.

Section 3's narrow observation carries: periodicity equations for each diagonal separately identify copies of its own centre sample. Relations between different diagonal indices require additional input, such as the coupled update or seed geometry. Calling the coupled update the only possible source would be too restrictive without naming the assumptions. The two explicitly displayed centre products are correctly located when the chosen time window contains B-2 and B-1; an arbitrary shifted P-window need not contain those actual centre events.

The illustrative inference p_n<=n => c(n)=0 uses an additional known fact: p_n>ceil(n/2). Together they put t'=n-p_n>=0 and 2t'<n, so x=t'-n lies strictly left of the forward wedge. The inequality p_n<=n alone does not put a point outside the wedge. Include the lower bound when using this argument.

## 4. What the probe checks

The bit update has the correct Rule 30 orientation. It checks H1–H3 on finite forward data. Its `period` routine tests agreement within a finite time window; by itself that is not an all-time period certificate. A proof-aware induction through the forcing periods could certify such periods, but is not implemented in this routine.

Its `doubled(k)` compares p_k with 2*p_(k-1), whereas section 2 requires comparison with 2*q_k. Those are distinct definitions unless an additional relation is established. This does not invalidate the hand proof with q_k correctly defined, but the numerical check is not a direct test of every stated premise. H4 is in the docstring without a corresponding assertion. The 17/60/125 product counts in the report are not emitted by this source, and no raw execution receipt is supplied with this commit. These remain Local's reported measurements; no independent numerical adoption here. No rerun is needed for the hand conclusions above.

## Verdict and continuation

The frontier/triangle identification and scoped weight reduction are independently carried. The asymptotic and impossibility conclusions are not. The owner has explicitly removed prize advancement as a gate: this work can continue for its mathematical content.

A concrete structural object now worth understanding is the sequence of inherited-period weight parities: when does it vanish, when is it odd, and how do the feeder phases determine it? That question is meaningful without a centre-period theorem. Before any new computation, search the existing weight/period record and derive the cheapest cases by hand. This is a direction for joint consideration, not a dispatched experiment or another census.
