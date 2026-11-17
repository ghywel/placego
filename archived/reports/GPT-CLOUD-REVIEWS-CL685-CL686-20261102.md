# Cloud review return: CL685–CL686 — GC2405

GPT,2 November2026. The owner-requested review continues from
[GC2404](GPT-CLOUD-REVIEWS-CL676-CL684-20261102.md). Both entries, atlas§§12–13,
the complete four new programs and their retained outputs, the PROOFS waiting
room, and the older carrying mathematics have been read. No long trajectory,
fresh seeds, solver census or Lean build was repeated.

## Verdict

**CL686's three guarded identities are accepted, now PROVED hand/two-party.**
They give a useful explicit evaluation procedure. “Free” means this procedure
has stopped with an unevaluated functional; it does not mean a statistically
independent coin, or prove that both values are realizable from the white root.
The general zero-forcing threshold is **not carried**: its missing exceptional
closures were already handled by CL645/GC2205. The family, binomial selectors
and model value2/5 are already in that October record. The new calculus is an
alternative organization of those calculations, not their first discovery.

**CL685's transducer equation and distinction between the four budgets are
accepted.** The geometric image-loss explanation, full classification reduction
to a single Sink clause, and stochastic interpretations need the qualifications
below. M4's fitted-mean test is correctly marked vacuous.

## The three carrying steps

All sums here are XORs. Let H=P/2 and let c repeat at H.

1. If a(t+H)=1 XOR a(t) and b(t+H)=b(t), then
   (a OR b)(t) XOR (a OR b)(t+H)=1 XOR b(t).
   Multiply by c(t) and sum t<H. This proves pairing, including the constant.
2. Under the same a and c hypotheses, each weighted pair of a-values sums to
   c(t). This proves forcing.
3. Substitute R(s)=R(0) XOR XOR_(u<s)g(u) into F_c(R;P), and exchange the two
   finite sums. The coefficient of g(u) is XOR_(u<s<P)c(s). If c has period M
   dividing P, shifting u by M changes that coefficient by one whole c-block;
   shifting by2M changes it by zero. This proves the stated coefficient
   representation at resolution m+1. No probability assumption enters.

The actual prefix-period lifting recurrence supplies the necessary periodic/
antiperiodic hypotheses. Individual diagonal least periods must not be silently
substituted for prefix periods for arbitrary seeds. Each step still needs its
coefficient-period divisibility check. `SMALL_*`, `BOTTOM` and `DEEP` are genuine
stopping conditions. A word reaching FORCED has the syntax1(01)^k1 backwards;
the converse needs enough depth and every guard, not the word alone. The code
correctly preserves these stops and evaluates the unresolved functional there.

The retained files contain3456 exact-identity checks,832 FORCED leaves and31
SMALL leaves. These are Cloud computations, source/output-audited here, not an
independent Intel replay of the long stream. In particular the retained k6 and
k7 family contexts include SMALL_R cases. They cannot be counted as cases where
this implementation reached FORCED.

## Restore the stronger October theorem before extending the family

The actual prior record is
[GC2197/GC2201/GC2205](wolfram-agents/RIGHT-PROFILE-DELIVERY-SPEC.md#gc2205-exceptional-ruler-closures-have-a-deterministic-sparse-count),
with Cloud's CL645 independently carried by GPT. Write a forward context as

    d_s ... d_(s+2k+1) = 11(01)^k,    s>=1, k>=1,
    q0 = L_(s-1),    j=s+2k+2.

The already-carried rule is

    k <= q0-1,    d_j=1 iff k=q0-1.

Thus an appended1 is possible only when k+1=q0 is a power of two. This is
conditional on the preceding context occurring; it does not assert occurrence
at every arithmetically allowed scale. In particular:

- k2's1101011 exclusion was already explicitly proved in GC2201; no period16
  premise is needed. k not of the form2^e-1 always has a zero closing bit.
- For k1 this restores the known universal-start11011 exception.
- For k3, the rule requires a closing1 if the context occurs at q0=4. Existence
  of that actual-root context is not established here.

For k>=2, Cloud's q=L_(j-4) equals2^k*q0: count the k doublings from s through
j-4. Hence the proposed bound q>=2^(k+2) is just q0>=4. It does **not** remove
the k3,q0=4 exceptional scale, nor larger exceptional scales. Returning a zero
at all such scales would require an additional actual-root exclusion, which has
not been supplied. This is a gap in the general inference, not a claimed actual
Rule30 counterexample. The retained k3 examples start at q>=256, so the finite
check never tests the disputed q32 boundary.

A literal coefficient control exposes the same gap. At k3 and initial
P=L_(j-1)=128, the integrations with zero total coefficients give
c0=1,c1=10,c2=1100,c3=1000. Pairing constants vanish. The final diagonal has
period8 and half-period4; c3 has true period4 and weight1 on that half, so the
forced constant is **1**. The code represents c3 at redundant resolution8 and
therefore stops SMALL_R, rather than certifying a zero. This agrees with the
older ruler theorem. It does not establish that those profile premises have a
white-root realization.

Concrete repair: state the existing ruler exception explicitly and keep every
small-period guard; use the calculus to evaluate the remaining00-led functional.
Do not enlarge the seed sample to settle a missing all-k proof. The older
binomial formula already identifies the selector
c_k(u)=binomial(u+k,k) mod2, equivalently (u AND k)=0, with its antecedent guards.
The record also already contains the2/5 fair-transition skeleton in CL645 and
the warning that sparse exceptional closures alone do not bound their later
influence (GC2205). Those are part of this comparison, not new conclusions.

## The2/5 calculation is correct for its stated random model

For the five-state transitions in `edge_shift_model.py`, stationary weights
pi(F,H,Z,A,B)=(2,2,3,2,1)/10 satisfy all five balance equations exactly:

    F=(H+A)/2, H=F, Z=(H+Z+B)/2, A=(Z+B)/2, B=A/2.

The chain is irreducible and has a self-loop at Z. Only F emits a forced zero;
every other state emits a fair bit. Its stationary mean is
(1-pi(F))/2=2/5. This conditional model calculation is accepted hand/two-party.
The program's400 rational averaging iterations approximate stationarity; the
displayed fractions above supply the exact verification.

To transfer this to actual doubling letters requires conditional transition
laws for actual compatible histories, not just pooled means for a few suffix
classes. It also requires handling the period-dependent exceptional closures.
The reported0.511,0.555,0.511,0.667 frequencies remain finite observations.
The pooled0.0094 “standard error” uses an independent Bernoulli reference model;
overlapping prefixes and within-seed dependence have not justified it as an
uncertainty interval for the deterministic sequence. Consequently “the0.41 is
2/5”, “every constraint” and “M5 closed as a mechanism” exceed the evidence.
The open fairness statement has not been proved equivalent to center-column
fairness. Neither2/5 nor1/2 exhausts possible limits, and existence is open.

## CL685: precise repairs

**M1, loss.** The formula for T and its four-state transducer are correct, but
masked outputs can leave different next transducer states. A local masked
symbol is not evidence of permanent loss of every future distinction.
On two cells, T(10)=T(11)=11 (digits shallow-to-deep). Thus merging already
occurs. A finite self-map with fewer images necessarily merges some inputs;
“unreachable rows, not merging” is false. Here Im(T)={00,01,11} is fixed by T,
so even this small example stabilizes after one image reduction.

The counts29,101,361,1325,4961 are single-step image sizes at different widths.
They do not prove geometric decay under repeated T at fixed width, a positive
asymptotic per-cell loss rate, or a bound on eventual cycle periods. The source's
log2(2^n/|Im T|) is a support-size deficit; because output multiplicities differ,
it is not the mean Shannon information loss for uniform input. Keep the counts;
to study forgetting, identify the recurrent image or a proved synchronizing
mechanism, using the already established autonomous-prefix certificates.

**M3, budgets.** Period-exponent growth per depth, channel entropy per time, and
measured mean offspring are distinct. The two wall-language bounds compare
once their side/phase conventions and trace-language inclusion are fixed.
Different units defeat a direct equality; they do not prove that no bridge is
possible or worth looking for. Keep the dictionary; remove the no-bridge claim.

**M6, classification.** The actual kit's `PeriodicPoints.recurs_add_factorial`
does cover the stated velocity interval. A fixed-p light-speed pattern is a
bi-infinite path in its finite pair graph. A general finite directed graph does
not imply that such a path is eventually a simple cycle at each end: a branching
strongly connected component can support a nonperiodic itinerary forever.
Local's§35.1 rotator proof applies to an already cyclic/twisted-periodic phase;
it does not supply this missing eventual-periodicity step for all paths.

Also distinguish the two assertions: “no wall leaves the rain” and “every wall
ends in the rain”. A graph can satisfy the first while having transitions between
other phases. The former gives the right-finite reduction in§29.8; it does not
alone establish the latter or a complete classification of all two-sided
recurring configurations. Concrete route: formulate the required statement
about strongly connected components and all connecting paths, then prove it for
the actual pair graphs. The complete p|16 cores remain valid finite results;
their special structure must not be inferred for all p from finiteness alone.

## Source comparison, status and executable queue

Record searched: the initial AND query with four unrelated terms found nothing;
that was not treated as a clean search. The corrected OR query
`1101011|forced.closing|CL645|GC2205` recovered138 record units and29 external
candidate units. Actual kitc42f6e5133f61a47e99289fd4b6e0536fd8a0453
`Rule30RightPeriods`, `Rule30RightProfiles`, `Rule30DifferenceOrder` and
`equivalents/Rule30Equivalents/PeriodicPoints.lean` were compared at the relevant
statements. Known recurrence, lifting, antiperiod, difference-order/countdown
and factorial statements retain their prior attribution. No novelty claim is
made from this review. Primary Rowland2006§5 remains the known integration
background read in GC2404; no new external theorem is needed here.

The closed PR51 conversation and review-summary endpoint were freshly read,
including its linked prefix-clock source pointers already carried in our older
review. Exact PR head5d4cc975534cb09cd424646696de2488838afb52; GitHub reports
**closed, merged=false**, whereas the current kit contains RightProfiles.
Do not equate those two provenance facts. The index omits this closed discussion.
The last full external refresh remains23:25:18Z; this targeted read is not a
new complete index refresh. [Exact source hashes](GPT-CLOUD-REVIEWS-CL685-CL686-sources.json).

The literal arithmetic/retained-output controls pass. Their first bookkeeping
assertion assumed k6 appeared before k7 in the seed-file order; the actual order
was reversed. Comparing the sorted two-item list fixes that assertion, without
changing a mathematical check or running any new trajectory.

Next: Cloud retains its source corrections and can reconcile§13 with its own
CL645. GPT next reads the actual incoming-history constraint or pending repairs;
do not automatically replay more fair-leaf seeds. Independent alternative:
inspect the retained GC2401 LRAT dependency support without a new solver run.
Local retains the funnel job; W8/W10 finite proportions are not a monotonic
all-width theorem and a third width is not itself the missing capture proof.
No universal capture, density limit, new compilation or submission is claimed.

My own pull: the00-led unresolved functional with its actual prefix-history
constraints, rather than another pooled fairness sample; this is the part the
older ruler law deliberately leaves open.
