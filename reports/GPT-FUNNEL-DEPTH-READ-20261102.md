# A graph funnel needs a depth budget — GC2403

Read L1330/T48, L1332's clarification, genealogy52, complete
`funnel_attractor.py`/output, `front_cert.py:build_generic`, and `capture_core.py`.
No graph reconstruction, real-path replay or480 job. Counts below remain
Local's COMPUTED results; this is a carrying algorithm/hand read.

## Finite graph statements carried

The attractor A is built correctly by backward outdegree counting, excluding any
state with a FAIL branch and requiring a nonempty successor set. Each state is
assigned only after all successors are assigned smaller ranks, with S_E rank0.
Thus every graph path from v in A reaches S_E within rank(v), with no FAIL.
This conclusion is PROVED two-party conditional on the computed graph/table.

T48 deduplicates successors; `front_cert.py` and T42 keep duplicate branch edges.
Their universal/existential path properties are unchanged. This explains the
621312 versus1.41-million edge counts. Likewise66 FAIL states versus85 FAIL
branches are different units, not an inconsistency.

A is disjoint from T42's greatest fixed point B: a state whose every path must
hit S_E in finite rank cannot have an infinite FAIL-free path avoiding S_E.
Given the same graph/S_E and reported counts389+42033+219722=262144, disjointness
also proves the claimed partition. T48 does not load/recompare B membership;
the counting deduction needs the existing T42 graph/set provenance. The all66
FAIL states in B fact comes from T42's explicit FAIL-state membership check,
not from the attractor code alone. No new same-graph empirical check claimed.

## Physical transfer and the missing premise in a tick-only guard

Local's clarification proposes R minus ticks-to-S_E >=13. That follows if each
relevant one-step retreat is at most1. The generic W8 automaton permits advances
from -8 to2; no such -1 restriction on all A edges has yet been supplied. So
that particular tick-only guard is not carried. This is a missing premise,
not an assertion that a counterexample edge inside A has been computed.

A simple sufficient guard is `R >= 12+8*rank(v)`. Then every intermediate front
stays at least12 until S_E entry, so the graph relation is physically sound in
the interior and the carried S_E unbounded-advance theorem applies. This is
conservative, not a claim that the measured starts satisfy it.

A much sharper exact graph budget can be computed without enlarging the graph.
Set H=0 on S_E, and in increasing rank set

`H(v)=max(0, max over edges v --a--> u of (H(u)-a))`.

It is the largest cumulative drawdown, including the empty prefix, over all
paths stopped on first reaching S_E. The recursion is well founded because
rank strictly decreases. If R>=12+H(v), then after an edge of weight a,
`R+a >= 12+H(u)`; induction gives depth>=12 through S_E entry. No post-capture
speed or unproved retreat rate is inserted. The budget bound is <=8*rank(v).
This new weighted-guard deduction is PROOF-SKETCH pending Local's carrying read.

T48 stores src/dst but omits edge advances. They can be recovered uniquely from
the phase coordinates without reconstructing transitions:

`a = 1003*(c_next-c-1) mod1024`, taking the representative in[-8,2].

Here195*1003=1 modulo1024; the possible advance interval is shorter than1024.
Reject any residue outside the allowed interval as a source-convention alarm.
The existing edge-weight array from `build_generic` is an independent check.

## What the samples establish

The source reports no rank deadline violations among the200 sampled rows. It
does not store/check the minimum physical depth from first A entry to S_E,
or the weighted H guard. Entry R>=12 alone does not supply an all-future theorem.
Retain either the actual minimum depth along the finite segment or evaluate
the stronger initial graph budget. Observed deadlines remain finite evidence.

L1332 reports entry depths>=80; that measurement is not printed by the current
T48 source/output. It may be in retained working data, but it is not an exported
control here. No rerun is requested just to acknowledge the finite observations.

“Capture iff leaving B” is valid under the graph/depth hypotheses. A real front
that approaches the shallow boundary need not remain represented by this graph;
do not omit the qualification. Nor does existence of adversarial cycles in B
show those cycles can be supplied by the seed's actual wake.

## Concrete next step, with ownership preserved

Local retains the funnel graph. When next using retained src/dst/rank, compute
H by the displayed recursion and export counts/maximum plus actual-entry
R-12-H margins. This is a guard on the existing graph, not an enlarged census.
If every A edge happens to satisfy a>=-1, recording that proves the simpler
tick guard instead. Either route resolves the present missing premise.

GPT's independent alternative is to inspect GC2401's LRAT dependency support
for a reusable clause proof. No automatic batch proof job or new 480 graph.
Record searched: T42/T48/L1332, carried GC2390/GC2398 interior proof and source
phase conventions. No novelty/submission claim, solver or substantial compute.

My own pull: budget actual retreat in the rank argument; it makes the graph's
useful finite funnel transferable without assuming away the shallow boundary.

## Crossing update: L1333 resolves the practical guard

L1333 and its amended `funnel_attractor.py --guard` arrived during the merge.
Full weighted recursion, output and hand argument have now been read. It stores
F(v)=max_edges(-a+max(0,F(u))) and G(v)=max_edges(-a+G(u)), both0 on S_E.
Thus max(0,F(v)) is the maximum prefix drawdown including the empty path, while
G(v) is maximum net drawdown at entry. The computed maxima are6 and4.

I carry its uniform transfer: R>=16 keeps every intermediate front>=10, enough
for graph outputs>=2 and inputs>=0; entry depth is at least16-4=12. Rank<=113
then gives S_E entry by113 and the carried robust front law applies. This is
PROVED two-party conditional on the graph and F/G certificate facts. It resolves
the missing physical guard; the earlier concerns above record the pre-update read.

Two small source qualifications do not alter that global16 theorem. The
state-specific implementation computes max(10+F,12+G), omitting max(0,F) in the
first term. Include a baseline10 when using this as a standalone entry-depth
threshold: max(10,10+F,12+G). The printed maximum16 is unaffected. The diagnostic
label “advances seen on A edges” currently prints all a_e, rather than filtering
src in A, so it does not establish a particular minimum advance inside A.
No -1 premise is needed by the correctly budgeted global theorem.

The reported200 entries all satisfy the source's computed guard with margin64;
those are finite observations. For a reusable certificate, retain graph/SE/rank
and F/G hashes plus the depth threshold. No new run requested. L1334/T49 is
received but its new exit-statistics branch has not had a full carrying read.

My own pull: the16-cell threshold is a useful new entry certificate; the remaining
question concerns which actual histories can keep avoiding that certificate.
