# A fixed dyadic return closure and a one-tick phase constraint

**GC2838 update:** Cloud CL772's two original hand carries are adopted, with
the nonzero-half-difference guard on the entropy count. No new research run;
[scoped receipt](#cloud-cl772-carrying-receipt-adopted-gc2838).

Owner-authorized manual research block, GC2833. Both schedules remain PAUSED.
Cloud CL768's two carrying reads are adopted, with its full-path component
guard and exact tile-window convention. No other worker's task or build is taken.

## Why this test

The full period16 core and its old glider exits are not a new target:
genealogy29.11/T23 already follows G16's period32 off-cycle choices to closure
(18238 states, only rain exits), and T19 does G8. The period32 wave of480
states is also known, L1304/GC2362. Its old generator follows one surviving
continuation to a cycle; it does not identify that cycle's complete SCC.

The new fixed question is whether **that stored cycle**, at the same temporal
period32, has off-cycle paths returning to it and therefore belongs to a
branching SCC. A negative answer is only about its attached forward closure,
not every period32 component, every dyadic period or actual black-edge capture.
No period64 extension, generic sample or full2^64 census is proposed.

**Record searched:** CL768/report and full probe/output; GC2830; LN12 report
§5–§10; genealogy29.4/29.7/29.11/31.4/32; `phase480.py`, stored cycle,
`general_front.py`, its upward-history control, `glider16_defect.py`,
`glider_defect.py` and their existing outputs; G157/G158. The current actual kit
`lean/`, `equivalents/` and catalogues retain MovingWaves' period12 construction,
minimum12 and low-period bounds, with the prior exact PR232/source read.
Complete fresh known-find refresh2026-11-10T17:58:19.690200Z:
kit03a19bf6240b63c6d15894c5f7552f3a6091d937, portal17:58:15Z,38open PRs,
zero changed/added/removed. Two narrow literature queries returned the portal
and our record, not an additional primary-source match; no novelty priority
claim is made from that search.

## A one-tick identity before computing

Use the leftward pair convention (c,d)->(u,c), with
Delta u=c OR d, Delta u(t)=u(t+1) xor u(t). For even temporal P put L=P/2
and Hc=c xor shift_L(c). Hc is L-periodic. Replacing each profile z by its
independently chosen half-shift is z_e=z xor e*Hz, e in{0,1}.

Let A=Hc AND NOT d, B=Hd AND NOT c, C=Hc AND Hd, all as full P-bit words.
Then Hu has Delta Hu=A xor B xor C. The triple of choices(e_u,e_c,e_d)
is legal exactly when

    (e_u xor e_c)*A xor (e_u xor e_d)*B
        xor (e_u xor (e_c AND e_d))*C = 0.

More directly, applying H to the proposed equation cancels the child's choice:
H Delta(u_e)=H Delta u, whereas H(c_e OR d_e) differs from H(c OR d) by
(e_c xor e_d)*C. Therefore

    Hc AND Hd != 0  ==>  e_c=e_d.

This is a local **overlapping-half-defect guard** for the literal one-tick OR
law. It is a PROOF-SKETCH pending an independent carrying read. It restricts
only configurations assembled from half-shifts of a fixed background; it is
not a criterion for arbitrary profiles or a general no-branching theorem.
The tau^3 positive-entropy/dyadic-order countercontrol remains mandatory:
its six-neighbour local law has additional terms, so this two-neighbour OR
identity cannot silently be applied to that different rule.

## Frozen questions, controls and stops

Predictions, before running:

1. The stored480cycle's SCC at P32 is precisely its480-cycle, with no returning
   off-cycle branch (0.8). Its other cyclic destinations are the rain only (0.7).
   Counterfactual: a larger SCC or another branching destination. Retain actual
   closed walks and treat a dyadic branching certificate as a meaningful result,
   without calling it a prize proof.
2. Every adjacent profile pair of the480wave has nonzero half-defect overlap
   (0.7), so its independently half-shifted configurations have only a global
   binary phase. Counterfactual: a zero overlap or a persistent mixed-phase
   path; inspect its exact mask rather than increasing a graph horizon.
3. Positive control: from U=(1323,2868) at P12 recover the known30-state,
   32-edge branching component. Independently audit complete reachability,
   every temporal integral including wrap, and the entire SCC partition in C++.
   Mutating one stored temporal bit must be rejected.
4. Unexpected/chaos test: allow an independent half-period temporal shift of
   **each** spatial profile, preserving all its individual rotation/weight data.
   The small marked phase-constraint graph, not single-profile statistics,
   decides whether those choices glue. Compare the period12 stay loop too,
   removing duplicate spin encodings on profiles fixed by the half-shift.
5. Scope control: reconstruct one six-to-two wall in the tiny P6 graph and
   check it literally. This tests CL768's suggested phrase "period never falls",
   which is not part of its carried formulas. The general safe statement is
   that the child's least pair period divides twice the parent's; its odd part
   may be lost. Odd factors cannot be created by one integration step.

No additional source cycle is searched. Fixed source
`tests/probes/phase480_p32.txt` SHA256
`6f77ed2178c4fca0169fc0690b952b680276a787c06d44e8bba36e0eabb92bc3`.
Normalize each stored(u,v) to(c,d)=(v,u), so one leftward step is(u,c).
[Extractor and gauge test](../tests/probes/swarm/sw02/carry/gpt_dyadic_return.py),
[independent checker](../tests/probes/swarm/sw02/carry/gpt_dyadic_certificate.cpp),
[hashed serial plan](../tests/probes/swarm/sw02/carry/gpt_dyadic_plan.json).

One Intel stage: a hard200000-node cap,110 aggregate CPU-second stop within
120 ceiling,300wall seconds,768MiB tree RSS,max6processes,16MiB/file and128MiB
stage disk. One compute worker/nice10; no solver, Lean, GPU or Wolfram.
run_capped tree tracking,4096MiB launch/1024MiB running free-memory floors,
4096MiB swap-growth, thermal and monitor-failure stops active. Inputs/plan
published before launch. A cap or pressure failure preserves evidence and
redirects to hand work; no retry or automatic cap enlargement.

## Outcome

**First stage COMPLETE, freeze dc3fad7f (published in merge bece27e7).**
The full reachable same-P32 graph has5472states/5472edges. Its only cyclic
component is the original480-cycle, with480internal edges and no forks.
There are4992transient states; all480off-cycle choices stop, with a maximum
transient stretch of35pairs including the last pair with no P32 child. No
off-cycle path returns and no path reaches the rain. This is a spatial
profile-continuation bound at fixed temporal32, not35physical ticks or a
mortality statement. The expected rain escape
did not occur. This does not refute Sink's "every wall ends in rain": there is
no outgoing wall at this period, so that assertion can hold vacuously.

The independent C++ checker reconstructs every cyclic integral one temporal
bit at a time, verifies closed reachability and independently recomputes the
entire SCC partition. P12's92-state reachable closure gives the known30/32
component with its two branch vertices. The one-bit corrupt P32 fixture is
rejected as NOT_CLOSED. No cap/pressure/thermal stop occurred.

The half-shift graph of the480wave has1920marked states and960edges; exactly
two recurrent480-cycles, with no persistent mixed parent phases. Every pair
has nonzero half-defect overlap (support sizes2,4,6,8,10,12,14). This proves
global half-phase locking on this fixed background, on the stated finite data.
But the14-cell P12 stay loop also has only its two global half-phases despite
four zero-overlap positions. Therefore the stay-loop gauge alone does not
separate the known positive-entropy P12 component from the dyadic cycle.

The period-loss control is explicit (pairs in the leftward convention):

    (23,40) -> (42,23) -> (21,42),  pair periods 6 -> 6 -> 2.

The first pair lies on a10-cycle of P6, and the last on the rain2-cycle; all
equations hold including the temporal wrap. Hence the proposed blanket
"period never falls" statement fails even with infinite ancestry. Only the
odd-part divisibility/child-period-divides-twice-parent statement is used here.

**Prior-art clarification:** T32/genealogy37 already reports rightward
rigidity of the480wave, through depth67, from uncertified SAT answers. If
adopted, that rigidity also rules out a returning excursion. This block does
not claim first discovery of the wave's simplicity. It supplies an independent,
small **leftward** complete graph certificate and the explicit35-pair bound;
it does not certify T32's rightward UNSATs or infer rightward rigidity from a
leftward computation. The existing black-edge exclusion remains separately known.

First-stage resource receipt:2.140212aggregate CPU seconds including monitors,
2.73wall seconds, sampled102020KiB treeRSS/max4processes, launch5711MiB and
sampled minimum5666MiB free+inactive, zero swap growth,383691artifact bytes.
All five planned jobs pass, including the expected exit2corruption rejection.

## Follow-on question and freeze: the actual34-cell return words

The local identity has a sharper form. It is **an equality graph**, not a
general nonlinear constraint. For a valid triple(u,c,d), retain the notation
A,B,C and put D=Delta Hu=A xor B xor C.

- If C!=0, the parents must have e_c=e_d. Then the equation is just
  (e_u xor e_c)*D=0, so also e_u=e_c if D!=0.
- If C=0, A and B have disjoint supports. The equation is equivalent to
  e_u=e_c whenever A!=0, and e_u=e_d whenever B!=0.

These conditions are necessary and sufficient. No constraint involves the
spin of a profile with Hz=0, which is a duplicate encoding and is removed.
Thus for any fixed P-periodic background, **all** independently half-shifted
valid fields are exactly spin assignments constant on the components of an
explicit undirected graph on the live spatial sites, with edges of length1or2.
This is a PROOF-SKETCH pending a carrying read; the proof is the displayed
algebra, not an extrapolation from the480wave.

For a spatially N-periodic background the finite quotient graph has integer
translation labels. In each quotient component, assign lift heights along a
spanning tree. The gcd g of the discrepancies on closed walks determines its
lift: g=0 gives one orbit of **finite** components, and g>0 gives g infinite
components. Each finite component can be flipped alone, giving an exact
finite-support phase surgery. An infinite component carries one global bit.
There are at most two infinite components, since any such component is
translation-periodic and crosses every spatial cut with an edge of length<=2.

Let K count only finite-component orbits that contain a column with nonzero
half-difference H (Cloud CL772 guard, adopted GC2838). Flipping a zero-H
column changes no field and contributes no entropy. The resulting field family
has spatial entropy K/N bits per cell: finite components supply independent
bits with that density; their bounded diameters leave only O(1) boundary
choices, while the infinite components add finitely many global bits. The
profile field determines its initial row by determinism, and a spin is recovered
locally from any nonzero Hz coordinate using at most P-1future ticks. A
nontrivial finite-component flip must change some tick0cell, again by
determinism. These are hand implications awaiting a second worker's read.

**Prediction before the follow-on run:** among the three known closed34-cell
return words011,101,110, some pair differs only by such local half-shifts
(0.6). That would locate an actual finite equality component and explain a
binary return choice. Counterfactual: no pair is in one half-shift profile
class; then this gauge mechanism does not explain the branching, and the route
is parked until a concrete profile-substitution argument reopens it. Three
tiles cannot all be one boundary-fixed equality family: its number of choices
is a power of two. No more code words or larger return lengths are searched.

Fixed controls: all legal profile triples at P2,4,6 and every one of their
eight spin choices; the14-cell stay and20-cell cross-cross loops; the same480
background. An independent synchronous leaf deletion of the already checked
P32 graph must give35rounds/4992removed vertices. Any finite phase patch found
is checked at every affected local equation and must be visible at tick0.

[Equality-graph and local-truth-table checker](../tests/probes/swarm/sw02/carry/gpt_phase_wires.py)
and [hashed follow-on plan](../tests/probes/swarm/sw02/carry/gpt_phase_wire_plan.json).
One small further stage, justified by the algebraic representation change:
20aggregate CPU-second stop,60wall,768MiB treeRSS,max4processes, same
16MiB/file/128MiB disk/free-memory/swap/thermal/monitor stops. One worker/nice10.
The first stage has used2.140212CPU, so even this full stop remains below the
original120CPU whole-block budget. No failed job is retried and no period or
node cap is raised. Sources and freeze published before execution.

## Follow-on outcome: phase bits do not explain the P12 branching

**Second stage COMPLETE, freeze ed78fb28.** The equality classification agrees
with literal Rule30 on all4452legal triples at P2,4,6 and all35616spin choices.
Independent synchronous leaf deletion removes all4992off-cycle P32 states in
exactly35rounds, confirming the first stage's height without trusting its DP.

|Fixed background|Spatial period|Finite-component orbits|Infinite components|
|---|---:|---:|---:|
|P12 stay0|14|0|1|
|P12 cross-cross11|20|0|1|
|P12 return011|34|0|1|
|P12 return101|34|0|1|
|P12 return110|34|0|1|
|P32 stored480wave|480|0|1|

**The prediction was REFUTED.** No pair of the three34-cell tiles is columnwise
half-shift equivalent. In the leftward indexing anchored at U,011vs101changes
positions1..14,011vs110changes1..24,101vs110changes11..24; **every** changed
profile is outside the corresponding original profile's half-shift orbit.
All six tested equality graphs have just one infinite wire and no independent
finite phase bit. The finite-patch positive branch of the checker was not
exercised by these backgrounds; it is not claimed as a computed positive example.

Second-stage receipt:0.444913aggregate CPU seconds,0.54wall, no stop. It ended
before the first runtime tree sample, so sampled RSS0 is not a peak claim;
the exact child wait4 maximum17330176bytes and headroom receipt are retained.
**Combined two-stage aggregate CPU:2.585125seconds.** No job remains. No new
period, source wave, code length or graph-cap retry occurred.

### A uniform P12 rigidity argument, beyond the sampled words

The failed prediction suggests a precise hand obstruction. **PROOF-SKETCH,
pending Cloud's carrying read:** let x be any bi-infinite profile path wholly
inside one of the six certified P12 components. If each column of y is either
the corresponding column of x or its six-tick shift, and y is itself a valid
P12 profile field, then y=x or y=shift_6(x), globally. This is about temporal
half-shifts, not every possible profile change.

Here is the carrying argument using the already checked finite component.

1. At U and V, H of the first parent profile is4095 and of the second is1560,
   so their half-defects overlap in four temporal positions. The overlap guard
   forces their two spins equal: the pair in y is the same pair in x, or its
   common six-tick shift.
2. At either branch, the two continuing child profiles have black weights5
   and7. Literally, U's children have profiles2602 and1493; V's2728 and1367.
   Weight5 selects the14-cell stay; weight7 the10-cell cross. A time shift
   preserves black weight, so it cannot interchange those choices. Away from
   the branches there is only one continuing child in the component.
3. The common phase therefore propagates leftward from that branch pair.
   The y path cannot evade the argument by leaving the component: the complete
   reachable P12 certificate has only this30-state cyclic component; all its
   other62states are transient and cannot support a left-infinite continuation.
4. Every x path meets a branch arbitrarily far to the right (CL768's carried
   return coding; the intervening stretches have length10or14). Starting there
   propagates the phase through any prescribed spatial window. Two different
   phases cannot occur on overlapping left tails, since no pair in the
   component is fixed by the six-tick shift. Hence one phase works everywhere.

Thus the phase-equality graph is connected for **every** path in this positive-
entropy P12 family, including aperiodic paths: otherwise an independent bit on
a second live component would construct a third half-shifted solution. In
particular, localized half-phase surgery cannot account for the known free
binary or ternary code. Their branching changes temporal words themselves.

This also clarifies the original parity instinct: both continuing fork
profiles have odd black weight, so that parity does not select the return.
Their weights5and7, or their residues1and3mod4, distinguish the actual
temporal-word alternatives. This is a generating observable at these certified
forks, not a new global invariant or a dyadic exclusion theorem.

### Exact scope of the general equality-graph claim

For completeness, the entropy count above is a hand consequence rather than
a fit. A finite lifted component has at most Nvertices (otherwise a repeated
residue gives a nonzero translation cycle), hence diameter<=2(N-1). Every
field-changing component has a tick0-sensitive site: flipping it changes a valid profile
field; identical initial rows would contradict determinism. Independent flips
of field-changing components wholly in a long window give K/Nbits per cell, and the bounded
diameter leaves only O(1) boundary choices. An infinite lifted component is
invariant under a nonzero translation because it contains repeated residues;
it crosses every cut. At most two disjoint such components can cross a cut
using edges of length<=2. They contribute only finitely many global bits.
This proves the claimed count under the stated equality-graph construction.
The local classification, lift/entropy consequence and uniform P12 rigidity
are new hand deductions here and remain PROOF-SKETCH until carried.

### Disposition and exact next step

The fixed480return question is settled at P32 by a complete independent
certificate. The attempted half-phase explanation is **parked** as a
separator: it locks even on the full positive-entropy P12 family, not just on
the dyadic wave. Reopen only with a concrete profile-substitution mechanism
that is not a columnwise half-shift; do not enlarge phase/degree fits or periods.

The warm next representation is the **temporal-word quotient**, retaining
which complementary integral was chosen. First derive its exact graph from
the existing30-state certificate, quotienting the free six-tick involution
(15vertices/16edges), and retain the5/7 fork labels and the two complete14/10
return histories. Compare those full histories with the certified dying
alternatives of the480wave before formulating a uniform dyadic claim. This is
a proof obligation and exact next executable step, not another launched job.

No all-dyadic nonbranching theorem, full P32 census, black-edge capture claim,
Lean module or release is supplied. Both schedules stay PAUSED. Cloud is asked
for two narrow carries: (1) the necessary-and-sufficient equality graph and its
periodic lift/entropy consequences; (2) the all-background P12 half-phase
rigidity proof, especially its leftward continuation/full-path guards.

Immutable evidence: `cited/gc2835-dyadic-phase-wires-20261110.tar.gz`, 157386 bytes, SHA256
`38aec2d5f265075c0e721549418d88a0d24f3c7ee30e22a541993293696d8fd6`, 64 files; verified TLS/raw-body upload and
byte-exact readback. Includes both frozen stages, original fixed input, graph
and mutation certificates, equality-wire outputs, all receipts, exact index
manifest hashes and the pre-receipt review. Native executable is omitted with
its digest retained; source/compile receipt are included. Private paths in any
warning logs are normalized with original/normalized digests recorded.

My own pull: the5/7 temporal-word change at a true fork, keeping its complete
return history; local half-phase changes are now ruled out as the explanation.


## Cloud CL772 carrying receipt, adopted GC2838

The complete returned hand arguments in the doubling-link report §5 and its
link-lemma context have been read. Both original GC2835 hand arguments are
now PROVED hand/two-party on the independently checked finite inputs. The
entropy count K includes only finite-component orbits containing nonzero H;
zero-H spins change no field. That guard is adopted above. The full-path
period12 family guard remains. Cloud's separate core/doubling census and
period15 observations are received as Cloud COMPUTED, not newly reviewed or
replayed by GPT. No temporal-word research or census is resumed during the
owner-assigned39-card pass. Both schedules stay PAUSED.
