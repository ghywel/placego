# Actual continuant data and finite-carry instantiation (GC2144)

**Execution update:** the10:28 gate deferral was followed by the single L1159 stage once headroom recovered.
It failed in MechanicalCarry, while both core components pass4.35; GC2145 retains the full failure and
freezes a targeted instance/deprecation source repair. These two adapters remain UNCOMPILED and are not
added to that repair stage.

GPT prepares two UNCOMPILED adapters, not a new abstract replacement for the continued fraction:

- submissions/finite-horizon/ActualContinuants.lean,
  SHA2564367bc2b3b1fa68c7cbf516f0a000a1033f92eb3389d7bdf195e271d5bb87836;
- submissions/finite-horizon/ActualCarrySpacing.lean,
  SHA256a514f7a025c7ea1f284882958db353832b4a0576fd6c7ad61ada327c50f2f878.

The first imports the existing ArcRotationDraft/ArcContinuantsDraft helpers from the delivered arc work.
Their exact compiled objects/source identities must be available before any future validation; no library
rebuild, dependency download or broad import build is requested. The second additionally imports the new
actual carry/spacing and finite-prefix staging components. This does not widen L1158's existing stage.

Record searched: actual current-kit932cf8dd Lagrange cont_det, contQ_nonneg, one_le_contQ, contQ_ge,
error_mul and one_lt_cq; existing ArcRotation.denominator_cast/real/pos and
ArcDeterminant.continuant_error_lt_next; G135/L1151/L1153, GC2135/GC2142/GC2143. These are known classical
continuant properties and local formal adapters, not additional submission items. Current formalization
of the explicit finite horizon, not novelty of continued fractions, is the purpose.

## Carrying request, after GPT's cheap index checks

The actual numerator is contP(digit alpha)(n+2), and the denominator is the already used natural-valued
ArcRotation.denominator. The multiplier

    D_n=cq(alpha,n+1)*Q_n+contQ(digit alpha,n+1)

is strictly positive: Q_n>=1, the previous denominator is nonnegative and cq(alpha,n+1)>1. Existing error_mul
then gives epsilon_n D_n=(-1)^n. Multiply the n/n+1 identities: their positive multiplier product times
epsilon_n epsilon_(n+1) is-1. Hence consecutive actual errors have opposite signs, not merely assumed signs.
The unit determinant has the orientation p_n Q_(n+1)-p_(n+1)Q_n, the NEGATIVE of cont_det at n+2; its square
is1. The already checked strict next-denominator error bound gives |epsilon_n|<1 because Q_(n+1)>=1.

Cheap controls by hand: at n=0 and alpha in(0,1), p0=0,Q0=1,p1=1,Q1=a1, determinant-1 and error signs+,-;
at n=1 the determinant flips+1. The denominator index is n+2 throughout, including n=0. These check the
sign/orientation mismatch that an unshifted generic-convergent citation would hide.

The second adapter instantiates CarryReturnSpacing.return_spacing with THESE actual data, then feeds its
actual gap and MechanicalCarry.difference_identity to the already checked finite-prefix growth theorem.
Its result has actual adjacent denominator bounds and an actual nonzero carry witness. It does not yet
force coefficients, select adjacent-scale witnesses, prove opposite-arc separation or assemble251(C+4).

Local: please carry the multiplier/sign/determinant index step and actual instantiation, without launching
an additional compile while the existing stage is held. Check exact old module-object availability only
when planning the subsequent validation. No new computation/resource agreement follows from this source.

## GC2148: finite threshold/coefficient selection uses actual kit inputs

Two further UNCOMPILED sources, with no added validation run:

- FiniteHorizonSelection.lean SHA256c416f5cefb2e72774d1d7916eb7f62577d9f652a89b2b99ee55cde2a1ef770bf:
  coefficient_one, crossing_before, crossing_scale, successive_ge. A>=2 and next=A*q+previous together
  with next<=2q+2C+6 force previous<=2C+6; hence above that threshold the coefficient is1. Threshold selection
  uses induction on a supplied finite witness, not Nat.find, and needs no monotonicity for the crossing itself.
- ContinuantSequence.lean: denominator_zero, denominator_recurrence, denominator_unbounded,
  denominator_successive, threshold_crossing, using the ACTUAL ArcRotation denominator. Source digest is
  recorded in GC2148. Lagrange.contQ_ge gives the explicit unboundedness witness B+1; the positive recurrence
  gives successive nondecrease, including the possible initial equality q0=q1=1.

The core adapter is instantiated in the second file: q0=1 and qr<=T<q(r+1) are not merely assumed for an
arbitrary substitute model. The offset recurrence q(n+2)=a(n+2)q(n+1)+q(n) avoids Nat-subtraction index cases.
Core lemma signatures were checked from the installed Lean source; current4.35 elaboration still awaits a
future separately frozen integration. No result is upgraded from source preparation alone.

Local: please include this coefficient/selection carrying read with the actual index/sign adapter read,
not an extra compiler run. First finish/review the seven-head repair's actual outcome. Then locate exact
previous arc module objects and agree one dependent-source integration plan. Do not rebuild Mathlib or
widen an active stage silently. Opposite-arc separation and the complete251 theorem remain unfinished.

## GC2150: block closure and exact resumption point

L1164 carries the three GC2143/GC2144 sources at their recorded hashes: the actual continuant index,
error signs, determinant orientation and carry-spacing instantiation. Accepted. It does not cover the
GC2148 selection/sequence sources above; that nine-head source read remains pending. L1163's seven-head
MechanicalCarry PASS is independently accepted in GC2149, with the original failure retained. There are
21 passing component heads on Lean4.35; none of these statements constitutes the assembled251 theorem.

For a future dependent-module check, the minimal old arc closure is, in dependency order:
ArcBreakBounds, ArcBreakSequence, ArcDeterminantDraft, ArcContinuantsDraft, ArcCoverDraft,
ArcStepCodeDraft, ArcRotationDraft. Their imports and the public Lagrange dependency were inspected.
The current eight-module closure is SharpAdjacentReturn, MechanicalCarry, FiniteHorizonBounds,
CarryReturnSpacing, ActualContinuants, ActualCarrySpacing, FiniteHorizonSelection, ContinuantSequence
(ordered consistently with these imports). These expose37 diagnostic heads; DenominatorBootstrap is
not imported and need not be repeated. The seven older modules expose25 diagnostic heads, separately.
The actual files, not a count of heads, determine acceptance.

First locate exact existing old arc/Lagrange objects from L1127/L1128 and compare source identities.
If unavailable, agree the necessary old-source compilation explicitly. Prior checks without an output
object do not provide importable objects for the new modules. Use a fresh isolated output library,
validate each dependency before using its object, stop at the first failure, and forbid stale or
sorry-containing fallbacks. No Mathlib rebuild, lake invocation, cache download or toolchain change.
Actual host headroom, stage-wide caps and the exact wrapper must be frozen before launching this NEW
integration. This note is a module plan, not a frozen stage or permission to widen a previous check.

Owner-directed switch: Local is offline for approximately1.5 hours (L1165); GPT now investigates Cloud's
DQ-024 edge-density pull. The finite-horizon task remains open with these source and validation gaps.

## GC2159: exact opposite-scale separation now has carrying source

After checkpointing DQ024, GPT resumes this unfinished delivery dependency while Local stays offline.
GC2158 parks the one-gate-at-a-time density ladder without a repeatable component/root-profile law.
Queue/audit, original G134/G135/L088, current adapters and the adjacent-basis dependency were reread.
Record/currentkit932cf8dd/portal/PR searches recover that separation and classical determinant machinery.
This is known machinery reapplied, not a new approximation theorem, novelty clearance or submission.

Three new **UNCOMPILED** sources in submissions/finite-horizon, thirteen diagnostic heads in total:

| Source | Heads | SHA256 |
|---|---:|---|
| OppositeArcStrip.lean |5|3151c0511b5aac522279e1d6f6be8b825715b1837d890da86aa9d0df769b6d93|
| OppositeCarryArcs.lean |4|c8260a465c741c4b36192cd038eefbbe5b7375a1556d49ff3558d3bac942ffb6|
| ActualOppositeCarry.lean |4|0c02e7ae932cffe44e5d160a329243b026b29cc8771e7d4934395aa6cf58ec25|

### Carrying simplification: retain the displacement's sign

For adjacent integer basis vectors (p,q),(P,Q), determinant of square1 and0<q<=Q, let the errors
epsilon,eta have opposite signs. Suppose (a,m) has

    -Q-D <= m <= D,   D<q,
    E=m*alpha-a opposite in sign to eta,   |E|<|epsilon|.

Then (m,a)=(-Q,-P). Write (a,m)=u(p,q)+v(P,Q). Orient epsilon<0<eta, so
epsilon<E=u*epsilon+v*eta<0. If u>0, v>=0 puts m>=q>D, whereas v<0 puts E<epsilon.
If u<0, v<0 puts m<=-q-Q<-Q-D, whereas v>=0 puts E>0. Hence u=0. The error sign forces
v<0; D<Q and the spatial lower bound exclude v<=-2. Thus v=-1. Negate all errors for the other
orientation. The source reuses the already compiled SharpAdjacentReturn.basis_coordinates.
No circle norm or previous-previous approximation/offset argument is needed.

Width-endpoint hand control: alpha7/10, p/q=1/1, P/Q=1/2, D=q=1, (m,a)=(-3,-2) satisfies
all other interface conditions but m!=-Q. This is exact rational arithmetic in source, **not yet
a checked Lean output**. It tests this general interface, not genuine successive convergents.

### Actual half-open carries supply the signed error

At consecutive scales j,j+1 put x=fract(theta+h*alpha), y=fract(theta+k*alpha). If epsilon_j>0,
actual nonzero carries give x in[1-epsilon_j,1) and y in[0,-epsilon_(j+1)). For m=h-k choose

    a=floor(theta+h*alpha)-floor(theta+k*alpha)+1.

Then E=x-y-1<0 and |E|<|epsilon_j|+|epsilon_(j+1)|. If epsilon_j<0, choose the same floor
difference MINUS1; E=x-y+1>0 with the same strict magnitude bound. Half-open endpoints preserve
the strictness. These are actual MechanicalCarry.carry predicates, not opaque arc membership.
No ordering of h,k, absence of earlier visits or confusion of visits with mismatches is required.

Coefficient a_(j+1)=1 gives epsilon_(j+1)=epsilon_j+epsilon_(j-1), hence
|epsilon_j|+|epsilon_(j+1)|=|epsilon_(j-1)|. The strip uses the basis at j-1,j. The finite bounds

    q_(j+1)<=h+q_j+C+4,       h<=q_j+C+2,
    q_(j+2)<=k+q_(j+1)+C+4,   k<=q_(j+1)+C+2

and q_(j+1)=q_j+q_(j-1), q_(j+2)=q_(j+1)+q_j imply
-q_j-(2C+6)<=h-k<=2C+6. Therefore q_(j-1)>2C+6 forces k=h+q_j exactly.
ActualOppositeCarry.visit_shift instantiates the actual kit denominators, numerator, determinant,
signs and error bounds at n=j-1. It derives numerator/error recurrences with the +2 indexing and
takes digit(n+2)=digit(n+3)=1 explicitly. These are the two local coefficient conclusions needed,
not an assumption that the continued fraction has an eventual all-one tail.

### Status and next assembly step

The renewed argument is **PROOF-SKETCH** until Local reads this variant; original G134/G135's
carried hand status remains credited. The three new files are not elaborated, compiled, axiom-checked
or independently reviewed. Twenty-one older component heads retain their prior passing status;
thirteen uncompiled outputs do not increase that count. Source/API and rational guards have GPT's
hand/self-check only. No compiler, Mathlib rebuild, dependency download or new experiment was run.

Next: compose actual threshold crossing, the four-step growth budget, the growth call at its final
usable scale, coefficient forcing at three scales, these two selected-visit shifts, then the final
contradiction. The index guard is explicit: if q0=q_r and q4=q_(r+4), four calls bound q1..q4;
the budget proves q4's INPUT deadline fits, permitting a FIFTH call to obtain the carry/next-growth
bound there. This forces coefficient a_(r+5)=1. It does not require q5's input deadline or a sixth
call. The selected visits are at q2,q3,q4, and the three coefficients are a3,a4,a5 in this offset.
Rational-prefix,
recoding and physical-restart layers remain subsequent obligations. No complete251/250 theorem or
portal readiness follows from this dependency.

For a future separately frozen integration, OppositeArcStrip follows SharpAdjacentReturn;
OppositeCarryArcs also needs MechanicalCarry; ActualOppositeCarry follows ActualCarrySpacing,
ContinuantSequence and both new files. Including them changes GC2150's eight-module/37-head plan to
eleven modules/50 heads. This is a plan update, not permission to widen a frozen stage. Exact old
objects, source identities, host headroom, wrapper and stage-wide caps still need agreement first.

Local, on resumption: carry the signed basis strip, plus/minus1 floor lift and n=j-1 coefficient
indexing. GC2148's nine-head selection read remains separately pending. No build is requested while
offline; source preparation is not a passing receipt.

## GC2160: Local resumed; selection carrying read and stage A agreement

L1166's complete nine-head mathematical carrying read is accepted. Applied its exact two atom
normalizations, without rerunning the reported core probe or compiling the files:

- FiniteHorizonSelection.lean now5c12a376dcb214fd7d1a12510cac6145ba8ad01fdef4fd2c03922b5666ddd384:
  explicit `show q (n+1) <= q (n+2)` before the final omega in successive_ge (Lean source uses the
  corresponding mathematical inequality symbol).
- ContinuantSequence.lean now430d45dbd2cfe47ec9740a047f544f0d1887f897ca46c1dd85ec5076f9d3afbb:
  the positive-digit hypothesis explicitly has argument n+2. Both files remain UNCOMPILED.

Accept L1166's split: GPT owns separation source; Local prepares integration and final assembly.
The three GC2159 separation files now exist and await Local's full carrying read. Local's stage B
must account for all three modules/13heads after these two repaired files, under its own freeze.

GC2160 agrees L1167's ONE stage A, wrapper4aeb80bd252e72e760a1d8c45447c962fa27c84ba20612d91dcfbb5f6775ca34:
seven old arc modules and six current modules,13total/53heads. All source pins and head lists were
independently checked; no repaired selection/sequence or new separation module is included. Fresh
owned output library, exact standard-axiom output, stop first failure/delete failed object; no lake,
Mathlib rebuild or dependency download. CPU300s per child/wall600s/RSS4096MiB/file16/disk64/max4,
launch5120/ongoing2048/swapgrowth128MiB, track-tree, one compiler, fresh actual M5 concurrency gate.
This is a plan agreement, not an execution or passing receipt. Full actual evidence remains required;
no automatic retry. GPT will not duplicate Local's final assembly or run a competing Mathlib check.

## GC2161: separation carried by Local; cast normalization applied

Full L1168 and its fourteen-line probe source read. Local carries all three GC2159 mathematical
sources at their original hashes: signed strip, strict half-open floor lift and actual n=j-1
instantiation. Accepted as a second carrying read. The hand argument is now **PROVED, two-party**;
all thirteen new Lean heads remain **UNCOMPILED**. The reported probe outcome is not independently
rerun or treated as a compilation of our complete files.

Applied the exact requested `push_cast at heq` after the type-changing line in error_witness.
OppositeCarryArcs.lean is now7f47629a93f59263274399abd1785d9e9dbe9f842b0fc2789fc16d48c4eb8e7f.
The other two GC2159 source hashes are unchanged. GC2160's selection/sequence fixes already landed.
No logical hypothesis/conclusion changed, and none of these edits touches stage A's frozen sources.

Keep stage A as the agreed single13-module run; do not fold or silently widen it. After reading its
actual outcome, stage B may validate the five additional files/22heads against accepted A objects,
with its own exact source/object pins, wrapper and caps. Combined coverage would be75heads, not a
claim that they have passed. No automatic stage B or repeated old-module compilation follows.
Local owns the final finite-horizon assembly and may draft it now; GPT reviews its carrying steps
and actual integration evidence. The four-budget-plus-fifth-call guard remains explicit.

## GC2162: full stage A evidence independently accepted

Read complete L1169, the compact receipt and every copied artifact from producer manifest
630bdf96d373a6ffe368d334ef87add304f5eb6c9ff7d3afa96e911daa6f4021. All13source files are byte-identical
to the frozen repository sources. All53reports match their exact expected names and standard axioms,
with no warnings; the combined output/version and per-module outputs agree with the compact receipt.
**ACCEPTED:** all13modules compile together on Lean4.35. No compiler rerun was made.

Actual parent COMPLETED0 at13:05:17–40Z,22.94wall; child22.77real/8.39user/6.48sys, timed maximumRSS
2568765440bytes. All43kept pressure samples read and checked: ownedRSS maximum2449936KiB, minimum
free4747MiB, swapgrowth0, sampled disk maximum3329330bytes. Parent maximum3processes; launch5850MiB,
existing swap1107.12MiB; final3365028bytes. These are the actual stated stage-A caps, not a lower
proposed envelope. Cleanup=null is normal completion.

All30downloaded text/source files have verified sanitized digests. Qualification: launcher original
length4103bytes versus sanitized4000bytes; its declared SANITIZED hash matches exactly. Both domains
are retained. The13object digests match the compact receipt, but object bytes were not downloaded or
rebuilt by GPT. This does not weaken the checked source/output result; reuse must verify those bytes
locally against the producer digests.

Immutable complete review copy: cited/gc2162-horizon-integration-a/review-manifest.json,
SHA25602f5db61d41e87cad332bad9c80308801881d1cffe973b179586422c58266fc5.
Stage A covers25old arc heads and28current heads; with the earlier3-head bootstrap,31current
finite-horizon component heads now have4.35checks. This is not the full uniform horizon theorem.
Stage B's five files/22heads remain UNCOMPILED.

Do not repeat A's13compiles simply to obtain a fresh B library. Copy the13accepted objects to a
fresh B library after checking each byte digest against the retained A inventory; refuse missing or
mismatched objects. Then separately freeze B's five new/repaired files, exact wrapper/caps and
dependency identities. If objects are unavailable, report that obstruction before proposing a
broader rebuild. No automatic B launch or rerun follows from this acceptance.

Local retains the irrational final assembly. GPT next takes the independent G136 finite-prefix
rational/endpoint perturbation and recoding margin source, after its carrying/known-source reads,
while reviewing Local's B/assembly evidence. No duplicate assembly or competing Mathlib stage.
