# reject a uniform three-distance linear potential

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G169 — reject a uniform
three-distance linear potential (RULE30-GPT.md G169; awaiting second reader, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Three waiting distances cannot share one linear timing formula at all the periods tested by the argument.

**What it says.** A formula using the reset distances of the preceding word, the current word and their difference has incompatible coefficient requirements at periods four and eight. Adding a constant cannot repair the conflict.

**Why it matters.** Keeping the two words and the clock is not sufficient if they are compressed into these three numbers with one fixed linear rule. Other formulas remain possible.

**An everyday picture.** Two short receipts put conflicting requirements on the same price list; an extra fixed fee cancels when the receipts are compared.

## The formal statement and proof

**Exact family restriction; independent review requested.** Use G8's reset distance D(w,r)=delta(w,r), including D(0,r)=0. Consider a potential on the full gated compatible domain of the form

    h_q(a,b,r)=C_q+alpha*D(a,r)+beta*D(b,r)+chi*D(a XOR b,r),

where alpha,beta,chi are fixed real coefficients, shared by every dyadic q>=4. C_q is any finite constant depending only on q. This family retains both words and the clock, but only through three scalar reset distances. No member satisfies every doubled slope5/2 edge inequality for every such q. The proof does not require nonnegative coefficients or nonnegative h; it rejects even this larger algebraic family. C_q cancels on every within-q edge.

**Period4 constraints.** First use the gated edge(12,8,0)->(8,8,0) from G166. It costs4 and has reward3. The three source distances are(3,4,3), and the target distances are(4,4,0). Its inequality requires

    -alpha+3*chi >=3.

Next use the zero-driver edge(9,0,0)->(0,14,0). In time-bit notation14 is(0,1,1,1), its cyclic difference is9=(1,0,0,1), and S14=9 XOR14. Both states are gated:9 at time-1 is1, and14(0) XOR14(-1)=1. The edge costs0 and has reward-5. Its source distances are(1,0,1), and target distances are(0,2,2), so

    alpha-2*beta-chi >=-5.

Adding the two inequalities gives2*(chi-beta)>=-2, hence beta-chi<=1. Every triple and distance here is explicit scalar arithmetic; no enumeration or experiment is used.

**Unbounded-period constraint.** For each dyadic q>=4 let b have its sole black bit at q-1. The gated compatible edge(b,b,0)->(b,0,0) costs q and has reward2q-5. Its source distances are(q,q,0), and target distances are(q,0,q). Thus

    q*(beta-chi) >=2q-5.

As dyadic q tends to infinity this requires beta-chi>=2, contradicting the period4 bound. Square. The same contradiction already follows at any dyadic q>=8, where2-5/q>1. Thus this single uniform formula cannot simultaneously certify q4 and q8; no larger computation is needed.

**Identified unexpected guard: the free edge is decisive.** The zero-driver constraint is not vacuous just because its physical waiting cost is0: its doubled reward is-5, and its child can have reset distance2. Omitting it would remove the upper bound on beta-chi and lose this contradiction. All three witnesses are valid gated edges, but root membership is not asserted. The pulse target's zero child is the unique compatible reset continuation, as already proved in G166. These are not projected cycles or sampled independent clocks.

**Scope and counterfactual.** Coefficients depending on q, a special formula at q4, nonlinear combinations, additional features, and a proved rooted-only domain are outside this rejection. In particular this is not a refutation of an asymptotic O(q) bound with finitely many exceptional periods. The constant C_q cannot help because it cancels; but replacing coefficients at small q genuinely changes the family. G8's phase-sensitive pair potential remains valid at the tested periods. The prior record is G8's certificate inequality, G160's gate and G166's pulse edge; no novelty claim is made for the linear-inequality contradiction. Next charge proposals need a richer compatibility feature than this single shared three-distance formula. No computation or prize conclusion is claimed.
