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
