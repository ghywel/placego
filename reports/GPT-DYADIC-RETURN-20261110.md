# A fixed dyadic return closure and a one-tick phase constraint

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
off-cycle path returns and no path reaches the rain. The expected rain escape
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

Let K be the number of finite-component orbits. The resulting marked family
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
