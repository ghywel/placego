# A zero-transient, history-sensitive budget — GC2458

GPT,3 November2026. **PROVED hand, two-party L1378**, conditional on the
carried strip transfer and independently checked finite potential. A specialization
of the already-certified finite potential,not a new potential method or an
answer to the three-fall SAT query, which was unattempted when this proof
was drafted. No computation launched for
this hand step after the monitor preflight stopped.

Normalize a B3 anchor a0 at phase3,with the actual row equal to the classic
ether onx≤a0. Suppose its13cell core is any word in
`M={671,1951,4767,6047,6815}`. These have h=−385,the global minimum in the
independently checked S13 potential. The current/future right tail is arbitrary.
The carried strip transfer follows an anchor a(t) with each shift exactly−7,
while maintaining agreement with ether onx≤a(t). Let:

- R(t) be the number of shifts in updates0..t−1,so a(t)=a0−7R(t).
- C(t) be the number of those updates whose phase/core state is in
  `D={(0,2258),(1,5982),(1,8030)}`.

For each state in D,both input choices have reduced cost56 (carried L1375).
All other reduced costs are nonnegative by the complete certificate. No claim
that D lists all positive-cost states is needed.

**Claim, for every such actual right tail and every t:**

`44 R(t) + 8 C(t) ≤ t`.

In particular R(t)≤floor(t/44),without the generic55tick transient. More
precisely the entire row agrees with the reference through

`x ≤ a0 − 7 floor((t−8C(t))/44)`.

When a leftmost difference exists,it is at least one cell farther right.
The formula is valid even if differences disappear altogether; the anchor
and clean half-line are still defined. No return to the original core,no
infinite sequence of shifts and no capture assumption is used.

## Proof

Write v_s for the actual projected state and d_s for its drift. The finite
certificate gives
σ_s=h(v_s)+44d_s+7−h(v_(s+1))≥0.
Summing throughs=t−1 gives

`7t−308R(t)=h(v_t)−h(v_0)+sum σ_s`.

Here h(v_0)=−385 and h(v_t)≥−385. Also sumσ≥56C(t). Thus
7t−308R(t)≥56C(t);divide by7. The agreement claim follows from the maintained
clean half-line and the integer bound onR. The actual input column may have
complex correlations; all choices already satisfy the pointwise certificate,
so no fresh-input independence or fair-coin assumption enters this proof.

For the original three-fast-fall query,t=132 andR=3 leave no room for
positive cost. The global-minimum bound actually forces h_end=h_start and
every σ=0,not merelyC=0. Thus it is exactly an actual-row admissibility test
of a132tick all-zero-cost path with threefalls. The already replayed88tick
two-fall path is a positive control. This consequence has not been inserted
as extra clauses: the original physical circuit stays unchanged.

The time t is measured from the stated critical reset. For the retained
trajectory one can start at originalt15,anchor−12,core1951; translate the
argument accordingly. The eight52returns each add one Dvisit and the two
44returns add none,with every other edge cost0 in those passages. Consequently
their observed reset times satisfy equality relative to15:
52n for the first8,then460 and504 for the ninth/tenth. This is finite exact
accounting,not a claim that this pattern continues forever.

## How sharp is the bound?

The physical normalized B431 template has firstfalls44and88. Hence the
re-anchor-count bound is attained at those two times. We do not infer it is
attainable for every number of falls; whether a third is possible is exactly
the outstanding original SAT question.

The clean-half-line bound is also attained at pre-fall times43and87 for
that template. Immediately before a B3 failure,the phase is2,g_0=0 and
failure on the next tick requires g_1=1; the reference at g_1 is0. Thus the
leftmost difference is a+1. At43,a=a0;at87,a=a0−7. This shows the universal
constant “one cell beyond the anchor bound” cannot be improved for all times
in this initial-prefix family. It is not an optimality statement for every
t,for eventual pinning or for all initial reset words.

## What this adds and what remains open

GC2453's cost56delay was stated for a return toρ after one shift. This law
removes the endpoint condition: every visit to D charges at least eight
ticks against all subsequent progress measured from a minimum reset. The
pointwise known costs become a history-dependent all-time shield for five
explicit initial-prefix families. It does not prove that a trigger must be
visited,how often it is visited,or that the front is uniformly bounded.
Starting from a nonminimum state restores the initial potential credit;
one must not apply this zero-transient bound to arbitrary ether disturbances.

A concrete route beyond an unsuccessful path search is to prove a rooted
lower bound onC(t),or a forced passage to a wall,for a specified family.
Neither has been proved here. Solving the exact three-fall question would
settle one smallest sharpness case; it still requires a repaired preflight,
a new freeze and no automatic budget increase.

Record searched: GC2445/L1371 finite envelope,GC2452/53/L1375 reduced-cost
return law,GC2454/L1377 global-minimum reset lemma and original finite S13
certificate. Standard additive-potential telescoping is known,reproved in
this specialization. Current kitc42f6e51/external04:35:16Z (Local04:40) unchanged;
no novelty or submission decision. The sharper statement is conditional on
the same carried transfer/certificate,not a new Lean theorem.

**Carrying read adopted (GC2460):** L1378 read the endpoint removal, exact
charging and specimen sharpness. Its independent finite-model check covers
all input paths from M through 200 ticks; that finite check supports rather
than replaces the all-time telescoping proof. No trigger-frequency or capture
claim was added. The separately corrected solver stage subsequently checked
a physical three-fast-fall witness; see [GC2460](GPT-THREE-FAST-FALLS-RESULT-20261103.md).

Next: investigate a rooted trigger-visitation condition rather than assume
slowdown follows two fastest falls. Independent alternative retained original
gap43 proof support.
My own pull: a forced lower bound on visits to a concrete charged state would
turn this accounting into dynamical progress; the missing step is admission
of histories,not another free-input density fit.
