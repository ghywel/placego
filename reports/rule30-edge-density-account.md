# DQ-024: the missing lower bound, and a test already in print

GPT, 29 October 2026, GC2151. The owner assigns this pull while Local is offline. The finite-horizon
formalization is checkpointed at GC2150; no M5 job is requested or presumed running.

## The proposed40 forecast has an existing answer

Rowland, [Local Nested Structure in Rule30](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf),
Complex Systems16 (2006), section1, author-PDF page4, lists a(k) through40. Its definition counts the black
cap immediately before a dyadic return. The kit's last_black_run/last_white identify this cap as J_k+1.
Thus J_k=a(k)-1. Every one of the38 overlapping values k=0..37 in Cloud's retained edge_gaps.out matches.
The last entries give J_38=89, J_39=90, J_40=92. Consequently J_40-J_34=13: the forecast12±2 holds against
published data. This is a checked citation and index conversion, not a new dynamics run or formal certificate.
The hour-long40 run would duplicate this evidence. Cloud's output header says35 but its actual rows reach37.

The finite marginal rate is6/13 over34..40, rather than exactly one half. Over24..40 it is16/33.
Neither interval resolves the limiting rate. Rowland also discusses seed dependence in section3; that topic
is not new just because a twelve-seed experiment has been repeated. Original Cloud text is preserved.

## Exact accounting question

Use the kit's actual least exponent e_j and J_k=max{j:e_j<=k}. Its monotonicity, unit increments and
unboundedness imply e_(J_k)=k and e_(J_k+1)=k+1. Standard monotone inversion then gives the equivalence
e_j/j ->1/2 iff J_k/k ->2. For example, if J_(k-1)<j<=J_k, then e_j=k; squeeze j/k between the
adjacent J values. Conversely, k=e_(J_k), and unboundedness ensures J_k tends to infinity.

Put E_i=e_(2i), w_i=E_(i+1)-E_i in{0,1,2}, and let N_r(n) count i<n with w_i=r. Exact summation gives

    E_n = N_1(n)+2N_2(n),
    n-E_n = N_0(n)-N_2(n).

Therefore the desired half density is exactly N_0(n)-N_2(n)=o(n). The known record-charge theorem gives
only N_2(n)-N_0(n)<=Q(0,n), an upper bound on the OPPOSITE signed balance. Its axioms allow w_i=1
forever with resource0, and w_i alternating0,1 with resource0. These have diagonal rates1/2 and1/4.
Both have unbounded exponents. They are abstract accounting paths, not claimed Rule30 orbits.

More strongly, any actual finite Path prefix can be followed by one zero-weight step, with resource reset
to0 afterwards, and then either of those tails. All three Path laws survive: the zero step has no resource
condition, and later weight-one inequalities read0<=1. Thus the accounting theorem plus any finite prefix
cannot force the limiting rate. This is an explicit insufficiency argument, not evidence against the conjecture.
The earlier GC1960 review already identified unconstrained zero steps; the balance and extension make the
exact missing lower-density statement explicit. Hand deductions here remain PROOF-SKETCH pending Local.

Equivalently, with D_k=J_k-2k and g_k=J_(k+1)-J_k,

    D_(k+1)-D_k = g_k-2.

Unit gaps reduce the balance by1, gaps of2 leave it fixed, and longer gaps add their excess. The conjecture
requires that accumulated excess to be sublinear. Positive linear drift of D_k would argue against it;
Cloud's suggested negative linear drift has the sign reversed and would conflict with the already proved
upper bound on e_j/j. No finite drift alone refutes an asymptotic assertion. The wall's free-bit count
and this exponent rate remain different objects, even if their limiting numerical values agree.

## A sharper local pull before any longer simulation

Read actual kit932cf8dd Rule30RightPeriods.pairPath/pairResource and Rule30DifferenceOrder.difs_past,
order_of_antiperiod, order_countdown; actual portal1b82d8's Resource and WallResource construction.
The resource r_i is the capped multiplicity of X+1 in the time polynomial of R_(2i) over H=2^E_i.

For a single doubling inside the pair, distinguish the two locations:

- 01: low diagonal stays, high doubles. Antiperiodicity gives r_(i+1)=H-1 exactly (known kit lemma).
- 10: low doubles, high stays. For nonconstant source s=R_(2i), the forcing identity is
  Delta^(H+1) h = NOT s. If d(s) is its least vanishing difference index, complementing a nonconstant
  dyadic-periodic stream does not change d(s). Thus d(h)=H+1+d(s), and r_(i+1)=r_i-1.
  In particular r_i>=1. The constant initial source needs separate treatment. This is a hand corollary
  of the existing difference identity, not a new difference-order mechanism or a novelty claim.
- 11: the known exact reset has r_i=0 and r_(i+1)=2^(E_(i+1)-1)-1.
- 00: no resource law in the accounting abstraction. This is the specific unresolved transition.

The exact10 decrement is PROOF-SKETCH, not checked Lean. Its proof uses Delta^(d(s)-1)s nonzero to get
the matching lower bound on d(h), and Delta^d(s)s=0 for the upper bound. Because s is nonconstant,
d(s)>=2, so the constant discarded by complement cannot affect this last nonzero difference.

Record searched: per_upper_half|not_half_lower|record_charge|DQ-024|white gap; Rowland with40|121|nested;
zero-resource/rootMultiplicity with half/density/countdown; exact-countdown/difs_past. Known hits are
GC1960/1961/2009, the original1b82d8 source, current-kit RecordCharge/DifferenceOrder/RightPeriods and
Troy Lowry's openPR55 generalization. Fresh kit932cf8dd/portal11:04:42Z/openPR21 check had0changes.
Primary literature inspected: Rowland sections1-3; OEIS A094605/A110240; Brunnbauer's period-doubling
discussion. No lower-density theorem was imported; negative search is not a novelty certificate.

## One bounded Intel diagnostic, frozen before execution

Question: do actual zero-doubling pairs erase more than one resource unit already among the first20pairs,
and does the exact10 decrement survive independent finite controls? This inspects the omitted transition,
rather than repeating the published40 value. It cannot decide the limit.

Prediction P: at least one00pair has r_i-r_(i+1)>1. Counterfactual: none does in this fixed domain.
Prediction Q: every noninitial10pair has r_(i+1)+1=r_i. Any failure stops this approach for diagnosis.
Unexpected check: report whether any00pair INCREASES the resource; do not silently discard it.

Source: tests/probes/wolfram/edge_resource_account.py, fixed single seed, j<=40, t<=65536,21source
streams, no seed census, no extrapolated density. Exponents are selected from the published gap table,
then checked by actual truncated returns and nonreturns at half the proposed period. Root multiplicities
use a Boolean binomial transform, independently checked by polynomial long division on all8-bit words;
small periodic streams also use repeated cyclic differences. Scalar physical Rule30 checks orientation.
Old reset/countdown inequalities are controls, not the new prediction. Source and wrapper hashes go in
the ledger before launch. No automatic rerun, larger horizon or additional formal build.

Caps: one Intel worker, CPU30s per process, stage wall60s, sampled ownedRSS512MiB, file2MiB, disk8MiB,
max3 owned processes, launch free+inactive4096MiB, ongoing2048MiB, swap growth128MiB, run_capped.py
with track-tree. Preflight found about7817MiB free+inactive, existing swap1183MiB, no research job.
The parent gate rechecks actual launch state; pressure/monitor/resource failure stops the stage.

## GC2152: actual diagnostic outcome and its limits

The single stage frozen at6a7a64cd COMPLETED0, 11:19:29–30Z. P and Q held; the unexpected check found
a00 increase. Counts among20pairs:00six,11two,01four,10eight (the initial10 is exceptional); E_20=16,
so N0-N2=4 as required by the balance. Selected actual transitions are:

| Diagonal pair | Doubling bits | Resource before -> after |
|---|---|---|
|10 to12|00|5 ->0|
|14 to16|11|0 ->127|
|16 to18|00|127 ->1|
|20 to22|00|0 ->2|
|30 to32|00|252 ->4|
|32 to34|01|4 ->4095|
|36 to38|10|8191 ->8190|

All256 small polynomial controls,33 physical rows,41 return/nonreturn checks and the known resource
laws passed. The seven noninitial10pairs satisfy the predicted exact decrement. This is COMPUTED on
the stated finite domain, not an independent carrying read, a Lean proof or a density estimate at infinity.

Full immutable source/output/parent/time packet: cited/gc2152-edge-resource/manifest.json,
SHA2567545430becd9872e642b9ee44d2ef5afb3da3bf8af8ede6673b93655011470d3.
Parent wall0.55s; child time0.22real/0.16user/0.01sys, child maxRSS12066816bytes. Launch headroom7777MiB,
existing swap1183MiB, final artifacts5400bytes. The child finished before the first monitor sample:
owned RSS/process/ongoing-pressure maxima are UNAVAILABLE, not zero. CPU/file limits and the launch
gate applied; no continuous or sampled stage-peak memory claim. No rerun or larger census follows.

## GC2153: why local gate laws alone permit arbitrary collapse

PROOF-SKETCH, a temporal-stream control, not a single-seed counterexample. Let H=2m=2^v, v>=4,
and choose an EVEN2<=a<=m-3. Over the first half-cycle let s be black only at a; let its second half
be the complement. In the first half let b be black at a+1,a+2 only; in the second half let b alternate
0,1,0,1,... . Let h(0)=0 and

    h(t+1) XOR h(t) = b(t) OR s(t).

All streams extend H-periodically: the OR has m+2 black cells, an even number. Its polynomial is

    P_s = (1+X^m) X^a + X^m U_m,
    P_g = P_s + X^(a+1)(1+X),     U_m=1+X+...+X^(m-1).

In the second half, b is white at the single white hole m+a of s (a is even); its other black cells
lie on black cells of s. Thus only the first two pulses contribute additionally to the OR. Over F2,
P_s has multiplicity m-1 at X=1, while the added term has multiplicity1. Hence P_g has multiplicity1.
Cyclic integration gives (1+X)P_h = X P_g modulo(1+X)^H, so P_h has multiplicity0. The resource
therefore falls from m-1 to0 in ONE00pair, however large m is. P_b is the two-pulse term of
multiplicity1 plus an alternating second-half term of multiplicity m-2>1, hence has multiplicity1.
All three streams have least periodH: a shorter dyadic period would force multiplicity at least H/2.
There is no hidden period reduction to explain the collapse.

This family also respects the elementary first-contact and final-black guards: s first turns black at a,
b and h at a+1, and all three are black at H-1. So those three guards alone do not close the argument.
A cheap objection is that b must itself integrate an OR containing s. This stronger control answers it:
wherever s(t)=1, b flips at t, both at the first pulse a and throughout its alternating second half.
Thus s(t)<=Delta b(t). Set u=Delta b; then ALSO Delta b=u OR s. This is a pair of consecutive gates,
not an arbitrary choice of the low stream. It still does not impose the entire upstream stack: no
claim is made that s itself integrates u OR a further stream. That is a genuine further restriction.
For H=16,a=2 the words are s=0010000011011111, b=0001100001010101, h=0001011110110101.
These are temporal controls, NOT asserted to be actual adjacent diagonals from the root.

Increase is locally possible too: take H>=8 dyadic, s black only at0 and b black at1,2,3. Their OR
polynomial is U_4=(1+X)^3; h(0)=0 gives P_h=X+X^3=X(1+X)^2. Thus the resource grows0->2 with
all three streams still of least periodH. This second control does not impose the first-contact guards.
It explains why a universal monotone-fuel gloss fails in both directions.

The warm question is now specific: what does the ENTIRE SHARED UPSTREAM STACK from the one-black
seed forbid in these00 transitions, beyond these two OR gates, equal periods, first contact and final black caps? For density
one half we need a sublinear net count of00 over11, not a bound on the size of an individual resource loss.
The finite observations do not yet offer such a bound. Local's resumption read should target the exact10
decrement and the temporal controls; neither is a proposed standalone new portal submission.


**Record cross-check during the hand continuation:** the Newton-basis exact countdown was already
written in GC2008, reports/rule30-five-step-period-bound.md, after the original half-rate review. It is
known, recovered here, not a new discovery. The current Q check supplies finite actual-resource controls;
P and the unexpected00 increase were the distinct questions of this diagnostic. This recovery changes
no frozen source, prediction or receipt. The new local controls are explanatory, not a locality no-go
theorem: extending them through all upstream gates to the actual seed remains unproved.


Validation note: ledger and link checks pass. Repository math-render checks on the edited research documents
containing TeX pass (0errors/0stray dollars) using the existing bundled Node/installed browser; the initial
missing-Node PATH invocation was an environment failure, resolved without installation or source changes.
The16-tick hand-control table was checked separately after its derivation; it is not part of the earlier
frozen20-pair dynamics receipt.


Scientific figure of the published41values (inspected after rendering):
cited/gc2153-edge-density-figure/manifest.json, SHA256
8fcf8b9f5381b1148b38237dd836bb1fbef78d65d2eb9b79b6eb2130630d45a7.
Both J_k and J_k-2k are drawn; the straight2k reference is not a fit or an extrapolated theorem.

## GC2154: the next upstream gate forces whole-run filling

Continuation after the block checkpoint. This is a hand specialization of the known R_step equation,
not a new Rule30 law. Write Df(t)=f(t+1) XOR f(t), B=Db. Two predecessor streams u,v satisfying

    Db=s OR u,       Ds=u OR v

exist, with the same period as s,b if these are periodic, EXACTLY when

    s <= B <= s OR Ds                         (pointwise Boolean order).

Necessity follows by u<=Ds. Conversely take u=B AND NOTs and v=Ds. This realizes precisely those
two equations; it does not impose equations on u,v themselves or the root's prescribed boundary.
Consequently b flips whenever s is black, stays constant inside each white run of s, and has a choice
only at a0->1 transition of s. Thus g=s OR b is obtained by filling ENTIRE white runs of s, never an
arbitrary selection of cells inside a run.

This is a cheap objection to GC2153's synthetic family. At t=a+2 it has s=0, Ds=0 but Db=1, because
the isolated b pulse ends in the interior of a longer white run. So the family cannot satisfy this NEXT
gate, before any genuinely global root constraint is invoked. The earlier two-gate claim remains
correct in exactly its stated scope; it was not an all-local-laws impossibility argument. No universal
conclusion about ancestry versus locality is warranted. The next useful restriction is already local.

For actual periodic diagonals, let filled white runs have starts a_r and lengths L_r. Their time
polynomials obey the exact identity

    P_g = P_s + sum_r X^(a_r) U_(L_r),
    (1+X) P_h = X P_g mod (1+X)^H.

The known geometric-factor lemma gives order_(X+1)(U_L)=2^v2(L)-1 for positive L. This is exactly
portal1b82d8.geometric_exact, already used in the original resource proof; no new valuation theorem.
For the COMPUTED actual16->18 case, r_s=127 and r_h=1 imply order(P_g)=2. No SINGLE filled white run
can explain it: its order is0,1,3,7,..., never2. If its order differs from127, the sum's order is the
smaller; if equal, cancellation raises it above127. Zero filled runs also fail. Therefore at least
two filled runs must participate in this actual collapse. The low-order parity contributions cancel
before the first surviving one. This conclusion is a PROOF-SKETCH using the independently controlled
finite values, not an all-time bound or a density theorem.

Record searched: existing run-rule report, GC1960 resource/valuation review, current-kit R_step and
inp_least_period, portal1b82d8.geometric_exact; record searches white-run/source with flip/transition
return the old relaxation/run mechanisms, not a novelty certificate. The whole-run algebra is recorded
as a known-mechanism specialization, not a submission candidate.

### Fixed witness extraction, frozen before execution

Discriminating question: which filled runs and parity cancellations produce the already observed127->1
collapse? Do not widen the20-pair stage. Extract ONLY diagonals14..18 over the single256-cycle, with
the root fixed to1, to retain their exact time words and run decomposition. No period search or census.

Prediction: at least2 filled runs; their combined first three root coefficients are0,0,1. Counterfactual:
zero/one run or a different coefficient triple rejects this derivation/index conversion. Unexpected
check: retain the smallest individual run-factor order and cancellations there, rather than assuming
the participating runs have length2. Independently compare scalar physical evolution through256 with
the integer frame; check all three gate equations, cycle closure, whole-run constancy, exact polynomial
identity and orders by polynomial long division (independent of the previous binomial-transform method).

Source edge_run_witness.py and its wrapper are pinned in GC2154 before launch. One Intel worker,
CPU15s per process, wall30s, sampled ownedRSS128MiB, file1MiB/disk4MiB/max3procs,
launch4096MiB/ongoing2048MiB/swapgrowth128MiB, track-tree run_capped. No automatic rerun or expansion.
This is a new256-tick witness question, not a replay of the65536-tick diagnostic for a cleaner receipt.

The separate ledger render reports0TeXerrors but flags20 literal code/shell dollar signs already present
before this block (Wolfram symbol and environment-variable names); all20 are unchanged. Its blanket
stray-dollar gate therefore FAILS for the existing ledger. This exception is retained, not relabelled a
pass or fixed by changing the other worker's historical text. The five research-document math checks,
ledger-structure and link checks pass.


## GC2155: actual whole-run cancellation witness

The fb740b94 stage COMPLETED0 at11:47:28–29Z. All257 scalar physical rows, three gate equations,
cycle closure, whole-white-run constancy and exact polynomial identities pass. Independent long
division gives orders127,2,1 for source, forcing and output. There are47 filled white runs:33 of
length1,11 of length2,3 of length3. Thus the prediction of at least2 holds; no enlargement is needed.

The actual first three coefficients after substituting X=1+Y show the cancellation explicitly:

| Filled-run family | Number | Y^0,Y^1,Y^2 coefficient XOR |
|---|---|---|
| Odd lengths1or3 |36|0,1,0|
| Even length2 |11|0,1,1|
| Both families combined |47|0,0,1|

The36 odd-run factors each have order0; the11 length2 factors have order1. Their constant terms
cancel within the odd family. Their first-order terms cancel BETWEEN the two families, while the
second-order term survives. Since the source has order127, it does not affect these three terms.
This gives forcingorder2, and integration gives outputorder1. Resource loss is an interaction of
whole gaps, not one independent destructive cell. This is a COMPUTED exact witness with a hand
explanation, not a frequency law, independence assertion or an all-time density bound.

Parent wall0.54s; child0.07real/0.06user/0.01sys, childmaxRSS11616256bytes. Launch6982MiB free+inactive,
swap1119MiB, final9540bytes. Again the stage finishes before any monitor sample: owned-memory,
process-count and ongoing-pressure peaks are unavailable, not zero. CPU/file limits and launch gate
apply. No failures or retries in the dynamics. Exact time words of diagonals14..18 are retained.

Packet and corrected metadata: cited/gc2155-edge-run-witness/manifest-v2.json (digest in GC2155).
The initial immutable manifest mistakenly labelled the run count46; the actual output always had47.
The new manifest corrects only that status text and preserves the first manifest's hash; source, outputs
and enforcement receipts are unchanged. No rerun was made to repair a metadata typo.

The next discriminating hand question is whether actual upstream equations restrict the cancellation
of these run-factor coefficients across many scales. The number of filled runs or the size of one
resource drop does not itself bound N0-N2. The global lower-density inference remains open.

## GC2156: a three-term witness hidden inside the47 fills

Post hoc HAND/PROOF-SKETCH reduction of the retained GC2155 output; no new dynamics or enlarged run.
Set p=1+X. To recover the first three coefficients at X=1 it suffices to work modulo p^3. In this
quotient X^4=1 and U_4=p^3=0. Hence X^a U_L depends only on a mod4 and L mod4. Four consecutive
time cells contribute nothing to these three coefficients, regardless of where that block starts.
This follows directly from characteristic2 algebra; equivalently it is the first small case of the
classical binomial/Lucas transform. [Mathlib's Lucas documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Choose/Lucas.html)
was checked; no new arithmetic theorem or imported asymptotic estimate is claimed.

The full table of run contributions (constant,linear,quadratic coefficients in p) is:

| Start mod4 | Length0mod4 | Length1mod4 | Length2mod4 | Length3mod4 |
|---|---|---|---|---|
|0|000|100|010|111|
|1|000|110|011|100|
|2|000|101|010|110|
|3|000|111|011|101|

Group the actual47 fills by these16 classes and cancel classes that occur an even number of times.
Only THREE classes remain odd:

| Start mod4 | Length mod4 | Representative polynomial | Signature |
|---|---|---|---|
|0|1|1|100|
|2|3|X^2+X^3+X^4|110|
|3|2|X^3+X^4|011|

Their representatives sum EXACTLY to1+X^2=p^2. The source polynomial is divisible by p^127, so it
vanishes in this quotient. Thus P_g=p^2 modulo p^3. Cyclic integration gives pP_h=XP_g modulo p^256,
so P_h=p modulo p^2. This recovers the order1 output with an explicit three-term parity witness.
It is a compression of this observed cancellation, not a count of independent causes or a minimal
description of the full time streams.

Record searched: Lucas/mod4 with run/polynomial/Newton; the nearest named old proof, G.GPT263 in
PROOFS-E2.3, was read. It is a previously second-read homogeneous-selector identity for odd cyclic
lengths and odd white-run lengths, with its own critical premises. It is related parity bookkeeping,
not this unrestricted filled-run polynomial dictionary. Both use standard residue arithmetic; this
new explanatory specialization is not proposed as a separate submission or a novelty claim.

### Cheap objection: is this now an autonomous eight-state model?

No. A class modulo p^3 has eight possible values, and XOR and time translation act on these classes.
The Rule30 OR does not. On period4 take time words u=0000, u'=1111 and b=1000, with time0 written
first. Their polynomials are0, U_4=p^3 and1. The first two words have the SAME class0, but

    class(u OR b)=1,     class(u' OR b)=0.

Thus the same input classes can produce different OR classes. This explicit algebraic control rejects
using the three-bit signature alone to predict the next diagonal. It is not a general finite-model
impossibility theorem. The missing data are the shared intersections of time supports, exactly the
nonlinear information lost by projecting to these parity sums. Future work must retain that information
or use an actual-seed restriction; another plot of the same density is not a substitute.

The objection persists if we also retain least period, initial colour, first black time and final black
colour. At period8 take u=01000001, u'=01111101, b=00100001 (time0 first). Both u profiles have
least period8, begin white, first turn black at1, and end black; b also has least period8, begins white,
first turns black at2, and ends black. The u-polynomial difference is X^2 U_4, hence zero modulo p^3.
But the OR-polynomial difference is X^3+X^4+X^5, which is X^2 modulo p^3 and nonzero. These are
abstract temporal inputs, not asserted seed diagonals. This strengthens only the particular signature
countercontrol, not a no-go theorem for every richer representation.

### Why adding a few more parity bits cannot close OR on the full space

Standard Boolean-ring algebra, reproved here as HAND/PROOF-SKETCH; not a novel Rule30 barrier or a
submission candidate. Let V be ALL H-periodic Boolean words, viewed as an H-dimensional F2 vector
space. Suppose an XOR-linear signature sigma:V->W has both properties:

1. Equal signatures remain equal after cyclic time shift.
2. The signature of pointwise OR depends only on the two input signatures.

Then sigma is either identically zero or injective. In particular a nonzero such signature with r
binary coordinates requires r>=H, even if those coordinates are a clever selection of parity sums.

Proof: if a nonzero word a is in the kernel, choose a coordinate i with a_i=1 and let e_i be its unit
word. Since AND = OR XOR left XOR right, OR-compatibility and linearity imply

    sigma(a AND e_i) = sigma(0 AND e_i)=0.

But a AND e_i=e_i, so e_i is in the kernel. Shift-compatibility puts every other unit word in the
kernel, because a cyclic shift acts transitively on the H coordinates. Linearity then puts every word
in the kernel, proving sigma=0. Otherwise the kernel is trivial, hence sigma is injective.

This closes the attempted EXACT parity-only quotient that preserves shift and OR separately on
arbitrary periodic inputs. It does not close nonlinear signatures, conditional identities, approximate models, or representations
on a restricted actual-seed family. Such a family is not the whole vector space and is not generally
closed under XOR, so the proof's unit-word argument need not apply. It is not a theorem that a seed
cell requires a particular amount of time to compute. The useful reopening condition for this route
is a specific actual-seed relation that determines the missing intersection signature; merely adding
another fixed batch of generic parity moments does not supply that relation.
