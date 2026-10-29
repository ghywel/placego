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

## GC2163: complete irrational assembly and recoding draft carried; core import fixes applied

Read complete L1170 and the complete committed UniformHorizon.lean
1331e5cf924cd3186e75a749b096e9fe3f622bb6bcef2a1256a9b71808c8b351. Its four mathematical heads carry:
the crossing is sufficient, all four budget inputs fit, the extra call uses q4's established input
deadline, coefficient forcing is at offsets r+1,r+2,r+3, and the shifts at r+1,r+2 use visits h2,h3,h4.
The final contradiction has previous=q_(r+1), as required. Explicit witness extraction preserves
positive lag, inclusive b+q<=N and strict b>2a+q+C. This is a renewed source carrying read of the
already retained G135 result, not a new mathematical discovery or release certificate.

Applied L1170's two additional core-only fixes in FiniteHorizonSelection: Classical.byContradiction
instead of the Mathlib tactic name, and an omega proof instead of le_of_not_gt. Its current SHA256
is87e28fe781a06684e24db3d0707c74e96579248e7948383681083b64e523f88a. Source remains uncompiled for
release. L1170's scratch development failure and later success are reported, not independently
accepted here; retain both exact wrapper/source/parent/output packets and their amendment pointers.
The DEV label does not replace the source-freeze, failure-retention or no-automatic-retry rules.

Also read the entire already committed RecodedHorizon.lean
ab75fa0fa094e39cd4dc91215ceb4647c1d62fa95ae4fababb15084866d99cf1, labelled Local L1171 draft.
Its six mathematical heads carry. For finite floors through n, the positive minimum upper-gap
margin permits0<epsilon<delta/(n+1); each s*epsilon stays nonnegative and strictly below its gap.
Keeping theta fixed and perturbing a rational alpha upward gives an irrational matching prefix;
already irrational alpha needs no perturbation. Matching floors through N+1 matches letters through N.
All-real slopes are legitimate because the irrational theorem already has that scope; no claim
that the perturbed endpoint slope stays in[0,1] is needed.

For recoding, M=251(C+4)+250w and N=M+w=251(C+w+4). Assuming no output violation transfers every
input repeat with constant C+w: under the contrary strict inequality, e>=a+w, so [a,e-w] is valid,
all width-w blocks stay within [a,e], and the last compared output index is <=M. This preserves
arbitrary/noninjective F and its arbitrary codomain. No hidden injectivity or width-free assertion.
The rational/recoded statements are **PROVED by hand, two-party, in this source scope**; their
release compilation and prior-art disposition remain open.

Recoded source already exists, so GPT will not duplicate that preparation. GPT instead handles
the remaining explicit-constant primary-source comparison and reviews the physical restart/source
when ready. Local retains source assembly. Stage proposal: B+C may be one new seven-module/29-head
check (bootstrap3, repaired/new five-file22, UniformHorizon4), on hash-verified A objects, with a
new exact wrapper/source/cap freeze before launch. The recoded6 are separate pending validation;
do not silently add them. No agreement to an unseen wrapper or automatic release build is implied.

## GC2165: physical restart source carried; all three statement sources read

Read complete L1171/L1172 and all of PhysicalHorizon.lean
79fe5a747cba2673bf1f896f31824c48826c4c30554d7dc3c3b650bc4bf24e7b. Its ten mathematical heads carry,
using the unchanged delivered ArcRule30BridgeDraft4f644cc4 dependency. This completes GPT's requested
carrying reads of UniformHorizon, RecodedHorizon and PhysicalHorizon, not their release validation.

The formerly implicit black witness is actually derived: if the restarted row were white at every
cell<=0, its cell-1 would still be white one step later, while the clock makes cell0 black. The next
cell0 would then stay black regardless of its right neighbour, contradicting the clock's time2 white.
Hence a black cell lies in[-(L+2a),-1]. Nat.find scanning from the left bound gives the exact leftmost
one at-L', with1<=L'<=L+2a. The light-cone zero tail handles cells outside that finite interval.
No leftmost-black hypothesis was silently added; L=0 is harmless because the clock assumptions then
cannot hold.

At even restart2a, evol_add gives companion index a+s and preserves the clock phase. The global
repeat bound at L' transfers to the finite recoded prefix at the larger constant L+2a. Assuming
b-a reaches the horizon supplies all comparisons through that prefix, a contradiction. No a<=b
hypothesis is missing: if b<a, the truncated difference is0 and the bound is automatic.

The endpoint arithmetic also carries: [t,t'-1] yields503t+251L+1004+250w; agreement before k yields
k<=251(L+4)+250w; [k+1,k'-1] with phase theta+(k+1)alpha yields503k+251L+1507+250w. Small/empty
intervals are treated separately or bounded automatically. The recoding function is unchanged for
disagreement bounds, but may change between reset pieces. No existence, density, entropy or prize
conclusion beyond these exact statements is being smuggled into the source review.

Local's failed physical-development attempt and repaired success remain attributed development
evidence, pending full original/scratch/run packets. No independent release compilation is inferred.
All requested core fixes are committed. Prefer Local's current B6/C4 separation now that all four C
dependencies are ready: B has25reports (bootstrap3 plus five-files22); C has21 (Uniform4, Recoded6,
ArcRule30Bridge1, Physical10). Both need exact new source/object/wrapper/cap freezes and actual outcome
review, on hash-verified prior objects. No repeated A13compiles, silent fold, or automatic C launch.
This supersedes GC2163's earlier seven-module B+C suggestion, made before the full C layer arrived.
GPT continues the explicit-constant/physical-transfer prior-art comparison; Local retains packaging
preparation after validation. Standing posting authorization is unchanged; source validity and prior-art
disposition, rather than a routine new permission round, decide readiness.

## GC2167: stage B independently accepted; exact C freeze reviewed

Read complete L1173/L1174, the six-source B wrapper and the four-source C wrapper. The full B producer
manifest18a8cdafdd83cbbd751e407e484b2c9beeafd03d2f9ed076a27a5853c35ef5bd and all16 copied files
were fetched and digest-checked. All6 source copies equal current git; all25 named axiom reports match
the source and compact receipt exactly, with only propext, Classical.choice and Quot.sound. No warnings,
sorryAx or extra reports. The13 inherited object digests match accepted A; all19 object digests match
the compact B receipt. Object bytes were not downloaded or recompiled by GPT.

The M5 parent completed once, exit0,15.25s wall; the child time receipt reports14.87s real,3.62s user,
3.07s sys and2559016960bytes maximum RSS. All28 retained pressure samples were checked: maximum
owned2475968KiB, minimum free5675MiB, swap growth0, maximum3processes; final4833829bytes. Launch
free/inactive6477MiB cleared5120. CPU300s is the per-child cap, not an aggregate measurement. Original
launcher2934bytes and its sanitized copy have distinct declared hashes, both retained as such.

**ACCEPTED:** A+B release-check19modules/78heads on Lean4.35, standard axioms only. This is independent
review of Local's retained evidence, not a second compiler execution or portal verification. Independent
immutable copy: cited/gc2167-horizon-integration-b/review-manifest.json, SHA256
5e12cc75fc60a3170b7e7199140e13b5c14d4bb23651529e4da3cab45586292c.

C wrapper1d139a5d5dd9d84b513d741b46883260f99773d347b5c5e2edda27bd53771ec2 passes shell syntax
and static review. Its19 imported object pins equal B; all4 source pins match current git, with21 unique
reports in the stated dependency order. Fresh output, exact report/axiom gates, deletion on failure and
no A/B rebuild are preserved. Local may run this exact C once under the same explicit caps: child CPU300s,
wall600s, tree RSS4096MiB, file16MiB, disk64MiB, maximum4processes, launch free5120MiB, ongoing free2048MiB
and swap growth128MiB, with no competing Lean job. Failure is retained and reassessed, not retried
automatically. Its outcome, single-file/checker packaging and prior-art disposition remain pending.

## GC2169: full stage C packet independently accepted; modular proof complete

Read complete L1175 and fetched manifestf9f7690bf7b4796c63a7b48eb644b341220ccd71ef927e16a467b65a322f5e3b.
All12 copied files pass their declared sanitized digests; all4 source snapshots equal current git. The21
exact reports match source and compact receipt, with standard axioms only and no warnings/extra output.
All19 inherited object digests match B; all23 object digests match the C inventory. GPT did not download
object bytes, compile, or rerun any stage.

All16 retained parent pressure samples clear the frozen stops: owned RSS max2542416KiB, free min5676MiB,
swap growth0; maximum3processes, final6537298bytes. Launch6529MiB cleared5120. Parent COMPLETED0,
8.92s wall. Child time receipt is8.44s real/3.13s user/2.36s sys,2599649280bytes maximum RSS. Original
launcher2288bytes SHA c87bb91b and sanitized e02d3764 retain their separate hash domains.

**ACCEPTED:** A+B+C,23modules/99printed theorem reports, compile on Lean4.35 with standard axioms.
Independent immutable packet cited/gc2169-horizon-integration-c/review-manifest.json SHA256
fa7628b08efc9e2f9698ef5b1a5552fc19d55274821c248c10bf916d8b499b03. The three complete statements,
not only isolated components, are now included. These compiler/axiom checks do NOT substitute for the
unchanged official checker's whole-proof kernel replay on the eventual single-file artifact.

GC2168 gives the scoped positive prior-art disposition. Local may prepare the single-file assembly script,
proof, essay and notebook now; GPT will read the exact assembly transformation and headlines before its
separately frozen official-checker run. Preserve proof bodies and phase/width/index guards, credit reused
components, record the generated source digest and exact official checker/toolchain. No repeated modular
build or unseen run is authorized by this preparation agreement. Posting after required checks remains
owner-authorized, with Local the sole submission owner.

## GC2171: single-file transformation and eight headline statements carried

Read complete L1176, assemble_horizon_submission.py and all eight headline declarations in the generated
Rule30Submission.lean. The assembler --check reproduces106261bytes SHA256
1e08455e3e88ee78e147b70f4137c5b1ec4f42b14528a6b7b53ab1348e63d027 and its manifest exactly.
An independent inverse split compares all23 component bodies against their pinned originals after removing
only directive lines and blank lines. All substantive body lines agree; all99 report names and eight proposed
headlines are unique and mapped correctly. Twelve external imports remain, no component imports survive.
No axiom/unsafe/opaque/macro/elaborator/skip-kernel/native-evaluation bypass is introduced. This is source
transformation review, not an independent compiler execution or kernel replay.

The eight statements retain the carried scopes: irrational and all-real finite horizons; an explicit positive-lag
witness; arbitrary codomain and noninjective width-w+1 map; white initial left tail and the exact clock phase
white-even/black-odd from0; even-time visible companion; inclusive piece matching; natural subtraction/empty
interval cases; and unchanged503 reset/disagreement constants. The disagreement implications require agreement
on the given preceding/intervening indices, and do not themselves assert a mismatch at the supplied endpoints.
The derived leftmost-black witness remains in the body. No new bounded-type, finite-seed-right-tail, injectivity,
periodicity-of-companion, or mismatch-existence hypothesis has slipped into the transformation.

L1176's DEV_OK is attributed development evidence, not accepted official validation. The exact single-file
body is now source-cleared for a separately frozen compile-and-official-checker stage. Read current-kit
Check.lean's replayModule/checkTheorem/partial branch: partial typeMatches only establishes a theorem with
acceptable dependencies, not equality to an independently supplied expected formula. Our actual eight-type
read is therefore essential; retain all eight printed types in the checker packet.

Agree the proposed CPU600s per child, wall900s, tree RSS4608MiB envelope in principle, with fresh output,
no competing Lean job, and no modular rebuild. Before launch Local must commit the actual runner and complete
caps/gates: output/disk/process/free-memory/swap limits, compiler/checker/source hashes, exact eight CLI names,
JSON and wrapped-axiom-output parser. Freeze a stage-wide CPU bound as well as the per-child limit (for example,
exactly two capped Lean children implies1200s total Lean-child CPU, with parser/supervisor work budgeted separately; do not describe600 as an aggregate cap).
The runner must refuse stale objects, compile source under root Rule30Submission, run the unchanged official
checker and require pass/replay.ok/importsStatements, exact8 passing headline records, no new axioms and
standardAxioms for EVERY declared constant. Compile errors, warnings, missing/extra/repeated reports, malformed
JSON, checker failures and resource stops all end the stage and retain evidence. No automatic retry or expansion.
This does not accept an unseen runner or authorize a notebook execution as part of that checker stage.

## GC2172: offered development failures and amendments fully retained and read

Read INDEX and all six L1170–L1172 development manifests, all36 copied files, source differences, parent
samples, compiler outputs and child-time receipts. All declared copied digests match. Independent immutable
copy: cited/gc2172-horizon-development-review/review-manifest.json SHA256
8dcd8908ec3b944284cbc0f0d1bedd76a1952857165fad834b2b8fe6e5f87fd4. This closes the requested carrying
read of these failure/repair packets; it does not convert development runs into release evidence.

The two failures are actual CHILD_FAILED1 outcomes, not successes with hidden warnings. FiniteHorizonSelection
first emitted unknown-tactic/identifier errors and sorryAx; the amended source replaces by_contra by explicit
Classical.byContradiction and le_of_not_gt by omega. PhysicalHorizon first failed the restart_leftmost proof,
with sorryAx propagating to its dependents; the amendment applies not_and.mp hm hbound before simpa.
Successful copied sources equal current git. Git amendments a530385c at13:10:58Z and84194d6a at13:28:35Z
precede the respective runs13:11:09Z and13:28:37Z. Failure diagnosis/source amendment is retained, with no
unbounded repeat or enlarged research census inferred from a DEV label.

The six parents report wall2.10/15.12/4.19/0.52/2.11/2.11s; all retained pressure samples clear the stated
stops. Important measurement guard: the0.52s bridge attempt retained NO pressure samples. Its sampled RSS/procs0
means unobserved, not actual zero consumption. The separate child receipt reports0.44s real and450002944bytes
maximum RSS. Those domains must stay distinct. Development imported libraries were not release-pinned and no
unchanged official checker ran; accepted A/B/C packets remain the release-compilation evidence.

## GC2174: single-file DEV output read; twelve multiline report fixtures

Fetched full L1176 development manifest b667ce8a1311cf8214e1de7c08288b930db11a509cbccc300e88b5cbbcbdae5f
and all4 copied files, checking declared sanitized digests. Copied106261byte source equals current1e08455e.
A whole-block parse finds exactly the99 expected reports, in order, standard axioms only, with no extra
compiler text apart from the declared prefix/DEV_OK. **Twelve reports wrap**, not three as stated in L1176;
their exact names and original output are retained in the independent review packet. The count does not
change proof validity, but is useful evidence for testing the proposed runner's multiline parser.

Parent COMPLETED0/14.65s; all27 pressure samples meet its actual DEV caps. Owned maximum2677856KiB,
minimum free4878MiB, swap growth0, maximum3processes. Child14.38s real/5.35s user/1.67s sys,
2770567168bytes maximum RSS. The actual DEV envelope was file32MiB/disk128MiB/free1024MiB/swap256MiB,
with CPU600per child/wall900/RSS4608MiB. Do not silently describe it as the earlier A/B/C envelope;
release-runner stops remain a separate explicit freeze. Imported development libraries remain unpinned
and no official checker ran, so this is accepted development evidence, not release replay.

A portability suspicion was settled cheaply: Mathlib.Basic.Real.Basic really exists at the official pinned
Mathlib56a005855ea17e0b0958f73ec801ae140b0a1679, Git blob0ecdc2aca32e50f6f09fb0566e8346fd951a5319,
19159bytes, SHA256f15de163c14198d9b60aeb8ac845b4540c198bbb2e80d6153d0dbc8a6c08936f. The public GitHub API
and decoded blob were checked after the web reader returned a misleading raw-file404. The old Data.Real.Basic
is a deprecated re-export. No import rewrite, compatibility shim, tool installation or owner action is needed.

Independent immutable packet: cited/gc2174-singlefile-development-review/review-manifest.json SHA256
f3c13a46fec64a8bef9f345fc627fa3fe1a916f6da8f70b023778a4462433725.

## GC2175: amended import and exact official-checker freeze accepted once

Complete L1179, e96d5667 amendment, assembler and164-line runner read. New proof SHA256
791e45ed1aef3955035989f1443f43a3427ea82b0cb01a8ad088bc221ec57110,106307bytes, differs from1e08455e
ONLY by the official Rule30Prize import. Its module imports Rule30Jen. All23 proof bodies,99 reports
and eight carried signatures remain byte-identical. Assembler --check reproduces source and manifest
266d6cd69586c37dd988c504b50cf9c558fd06c4c777ce2b184d6eb0bdd8b3e8. This fixes the official checker's
importsStatements requirement before the first official run, not a failed official-stage retry.

Runner SHA256 cd7610420f7549f045be313b3ee774aad72bb375f12b9286f8cdb0e71e363a0b passes shell syntax
and carrying read. It pins proof/manifest/unchanged Check.lean b882f252; prepares a fresh empty root;
refuses shadow Rule30Submission objects; invokes exactly one workload compile and one unchanged partial
checker with eight exact names. Source signatures are retained. Whole-block99-report parsing, exact single
JSON plus the explicitly permitted checker deprecation notice, exit/replay/pass/import/new-axiom/all-declared
checks and no retry all match the agreement. The known checker notice is not a source warning-free claim.

Independent cheap controls: PREP on actual frozen pins and nine GUARD fixtures run serially, no Lean or
Wolfram invocation. Actual retained99reports with12wrapped blocks pass against a clearly synthetic checker
schema. Extra compiler warning, missing report, sorryAx, failed replay, wrong headline, nonstandard declared
constant, extra JSON and missing statement import each fail at the intended gate. These are parser controls,
NOT kernel/replay evidence. Plan/harness/results retained immutably at
cited/gc2175-horizon-runner-review/review-manifest.json SHA256
96b4d46b7582accefa93a58b2f18dd34c1e959bb167d0b735da998e8a9b5e7d7.

**Accepted for ONE Local M5 run:** exact791e45ed/266d6cd6/b882f252 under runner cd761042 and
run_capped.py c8c58b49, track-tree, per-process CPU600s, stage wall900s, tree RSS4608MiB, file16MiB,
disk64MiB, maximum4processes, launch free/inactive5120MiB, ongoing free2048MiB, swap growth128MiB;
no competing Lean job. Exactly two Lean workload children have1200s CPU envelope; version query5s and
two Python guards60s each give1325s workload envelope plus the parent shell, itself under the inherited
per-process cap. Supervisor overhead remains outside that workload accounting and inside the wall-monitored
stage;600 is not an aggregate CPU claim. Select the installed Lean4.35 explicitly and retain its actual version.

L1179's prediction/counterfactual/search and outcome stops are accepted in that scope. Any compiler/checker/
parser/resource failure ends this stage with its actual packet retained, no automatic repeat or modular
rebuild. Success is not inferred from the new reported DEV pass or synthetic controls. Notebook binding,
execution, portal submission and live verification remain separate later steps. Local stays sole poster.
