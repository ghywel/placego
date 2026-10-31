# GPT's carrying read and continuation of the October 31 inquisition

Owner-authorized bounded block, beginning 15:11 UTC. Both recurring schedules remain paused; Local is stopped.
The handover is [L1257](HANDOVER-GPT-20261031.md), with its [complete tracker](inquisition-20261031.md).

**Current status, GC2330 / L1258:** Local has carried both GC2327–GC2328 arguments: their bounds and the limit
M(k)/k -> 2/3 are now **PROVED, two-party hand**. GPT has in turn carried Local's early-healing refinement,
giving floor(2(k-1)/3)+4 <= M(k) <= floor(2k/3)+4 and exact equality with the upper value for k ≡ 1 (mod 3).
Earlier sketch labels below preserve the chronology. The all-residue formula remains a conjecture beyond Local's
computed k <= 20. No formal compilation, novelty clearance or submission follows from these hand reviews.


## Carrying reads (GC2326)

All three requested short hand steps have been independently read. This accepts the mathematics below, not a
rerun of Local's computations or a blanket acceptance of the handover's conjectures.

1. **Death-kind pairing: PROVED, two-party hand, with a scope clarification.** The ensemble is the full cube of
   starts supported within depths 1 through W, optionally with the initial clock bit fixed. It is not the subset
   whose last cell is required to be black. At even death time 2 <= t <= W-1, write
   x_1(t-1) = a_t XOR H(a_1,...,a_(t-1)) and
   x_1(t) = a_(t+1) XOR J(a_1,...,a_t). Toggle a_t and then toggle a_(t+1) precisely when needed to restore
   x_1(t)=0. Earlier required clock values are untouched. The repair bit depends only on the shallower coordinates;
   on applying the transformation twice the same repair occurs. This is a fixed-point-free involution exchanging
   the two death kinds. If t+1=W, fixing a_W=1 would break the ensemble, which explains the width clarification.
   The actual current kit's `zrow_aff`, `pivot`, and `zrow_light_cone` supply exactly these dependencies.
2. **Two adjacent left diagonals: PROVED, two-party hand.** For n>=1 the input interval is [-2n+2,1]. The leading
   inputs of the outputs at (-t,t) and (1-t,t) are -2t and 1-2t. They fill that interval without repetition, and each
   enters by XOR. Recover the inputs in descending spatial order. The n=0 case is the empty bijection. This is an
   application of the familiar left-permutive triangular reconstruction, not an asserted new general mechanism.
3. **No 00100 or 11011 on a right diagonal: PROVED, two-party hand; already known in this record.** Local's two
   branches on c_0 are sound. In the c_0=1 branch, b_2 must be both 1 and 0. In the c_0=0 branch, d_0=c_1=1 and
   b_2=0 force c_2 to be both 1 and 0. Both words have the same flip word 0110; global complementation of Rule 30
   is not assumed. [G258](../proofs/G258-four-forbidden-words-in-every-forward-right-moving.md) already carries these
   and 000111/111000, independently read on October 9.

The same record also already contains the [constant-run white wedge](../proofs/G264-a-constant-temporal-run-forces-a-spatial-zero.md),
the [nine-tick exclusion](../proofs/G267-g-traces-never-contain-000001101.md), and a
[ten-tick exclusion](../proofs/G268-g-traces-never-contain-0001101011.md). All four sources were read here. Thus the
new census should be compared with these statements before extending its horizons. Soficity and exact entropy
remain open; finitely many newly found forbidden words cannot by themselves disprove finite type.

## Two cheap objections that change the queue

**The sea-only uniform death bound is REFUTED by existing mathematics.** Given any sea and any H, put the fixed
checkerboard, with depth 1 black, in depths 1 through H+1 and put the chosen sea beyond it. The depth-1 light cone
agrees with the checkerboard through time H. This is a finite patch, and H is arbitrary. More strongly, the current
kit's `Rule30ZeroBoundary.complete_near_wall` permits any prescribed finite depth-1 trace while retaining any far
tail. Its complete proof and the following `edge_region_barrier` were read. A repaired question must allow a bound
depending on patch width, or ask only eventual death. Zero-density or distant forcing does not supply a uniform
time bound.

**The proposed period-three sea does not force forever.** For the unbounded spatially 3-periodic row, a word with
two black cells maps to a singleton, a singleton maps to 111, and 111 maps to 000. Rotations commute with the rule.
Hence every such sea is white within three updates. This eight-word hand check is an elementary known-rule
calculation, not a new classification of periodic seas. If the wall start matches it beyond depth W, locality makes
the state at time 3 white beyond W+3, and at time 4 white beyond W+4. Restarting at the even time 4 preserves the
clock's parity. Conditional on Q01, the resulting finite row therefore dies too. This gives a conditional reduction
to finite white-tail starts, not an unconditional period-three death theorem or a converse reduction.

**Stronger: even the eventual-death version fails for a known period-seven sea.** The actual current kit already
proves `Rule30PeriodTwoCoupled.etherLeft_zbl`, `ether_col1_black`, `ether_free_bits`, and `etherLeft_eq_Theta`.
Their complete relevant proofs and the `B4_imp_B3` masking step were read. At time phase 1, reading away from the
white wall, the initial sea is

    1100001 1100001 1100001 ... .

Its depth-1 trace is `1011` repeated, hence every even tick is black forever. No nontrivial finite patch is needed.
In the spatial-period-seven ether, B3 masks its right neighbour B4: whenever B4 is black, B3 is already black, so
replacing B4 by the permanently white wall leaves the entire left half unchanged. The free bits alternate 0,1.
This is the kit's existing constrained start Theta(alternating), not a new GPT discovery of an eternal row.

Local's period-at-most-six census is consistent with this example, but extrapolating "only the checkerboard" is
false. A meaningful next question is which periodic backgrounds admit a clock-supporting interface, not whether
all non-checkerboard backgrounds die. Kit source SHA256:
`caa2f8ba78d0a48dc8c7db6f8adf65375b1d1442b85021eb5a676c1e185f3d22`.

**The first 2058 timer is already demonstrated.** The delivered
[nested essay](wolfram-agents/submissions/gate-clocks-nested/essay-prose.md) explicitly exhibits the first 20 layers:
11,10,11 followed by seven 01 pairs, with K=2 and M=8. GC2322 carried its executed notebook. Do not rerun the
handover's proposed first-stage test. Symbolic completion of the second timer remains a genuine open target.

## What the left-diagonal change of coordinates does to the wall

Write x_j(t) for the physical left half, with x_0(t)=0 imposed, and
L_k(t)=x_(k-t)(t), for k<=t. Then

    L_k(t+1) = L_(k-2)(t) XOR (L_(k-1)(t) OR L_k(t))   (k <= t),
    L_(t+1)(t+1) = 0.

The two coordinate lines can be taken at k=-1 and k=0 (a shifted version of Local's unrestricted-row bijection).
For the wall problem they are free except for the prescribed initial slot L_0(0)=0: at horizon n>=1 the underlying
interval is [-2n+1,0], and fixing its rightmost bit leaves 2n-1 independent bits. Their backward cones touch the
wall only at that initial slot, so later wall forcing does not change them. But the required clock is
L_(2n-1)(2n)=1, and the wall lies at k=t. They move across the coordinate frame. For example the first nontrivial
clock test is L_1(2)=L_(-1)(1) XOR L_0(1)=1. Later tests require a growing triangular region. A finite initial patch
is also a condition on the decoded row, not a finite list of forbidden coordinate pairs.

This is an exact restatement and an obstruction to the proposed immediate shortcut. It does not prove that no
better coordinate argument exists. Reopen this route with a specific identity controlling that growing region or
the decoded white tail; a fresh-bits argument alone reproduces the already known pre-boundary halving law.

## External refresh and the new pull

The complete index refresh succeeded at 15:11:52 UTC: kit
`842b756fc7d043995e14019fee2a82ab4ec83cf7`, portal update 15:11:47 UTC, 23 open PRs, 34 added / 7 changed / 2 removed
indexed items. This is index completion, not a carrying read of every new submission.

- [PR68](https://github.com/WolframInstitute/Rule30PrizeKit/pull/68), head
  `3b0baae4466097d0a26890edd050aef12cfff9ed`: its author has incorporated Local's `period_of_eventually_time_le` and
  `time_unbounded_le_thirteen`. Both actual new source bodies and the author's reply were read. The reported
  130-constant replay is the author's validation, not a new GPT build. No reply was posted.
- [PR69](https://github.com/WolframInstitute/Rule30PrizeKit/pull/69), head
  `fcffbaa9f28802559706095d50e847b77bd7105f`: Troy Lowry's `Rule30EtherGrounding` excludes eventual one-in-four ether
  pairs at any depth behind a black right edge, without a global period assumption. The full source, README credit,
  and PR description were read; fresh conversation, inline-review, and review-summary lists were empty. Its source
  SHA256 is `538c906ae638b8249ce7445e6d58df13aea8b04a77b7e8a7451657c4ee3fcd2a`. The different spatial-period-seven
  driven ether and its white-tail erosion estimates are not the same statement or frame.

The portal snapshot has 73 entries. Package B remains Human Verified; A, the horizon package, and the nested
package remain Lean Verified with no Human Verified tag. The status-page search cache is not substituted for this
fresh JSON snapshot. No completed submission was recreated.

**Pull:** the PR69 proof transports a local pair invariant to the edge, so it should also bound how long the pattern
can imitate an unattached ether. **Cheap objection:** its published eventual statement hides the ticks discarded
at each descent. **Discriminating test:** derive the exact phase-dependent dependencies, including the one backward
time dependency, then bound the resulting finite proof tree. This is an application of Lowry's invariant. No
first-in-literature or submission claim is made. Searches covered `grounding`, `ether pair`, the current kit and
equivalents/catalogues, portal source, actual PR69 head/discussion/reviews, and primary-source web queries. No
negative keyword search is used as novelty evidence.

For the subsequent front construction, Brummitt and Rowland's
[Boundary Growth in One-Dimensional Cellular Automata](https://ericrowland.github.io/papers/Boundary_growth_in_one-dimensional_cellular_automata.pdf)
was checked at its introduction and Section 2: its constant-background growth inventory is not this extremal
periodic-ether episode statement, and it explicitly distinguishes periodic backgrounds. It points to Phillips's
periodic-background work. Its [2004 notebook](https://www.wolframscience.com/conference/2004/presentations/material/rphillips-growth.nb)
was subsequently obtained using verified TLS: 4,215,694 bytes, SHA256
`3b43f9af2d03dd0d457a39b426c25e938ffe236a88d06a844ec0e679512247da`.
The readable experiment description covers 30 seeds against 30 periodic backgrounds through width four for each
of 88 rules, so it is relevant prior numerical work and could include this background. The Rule 30 section's
principal evidence is embedded bitmap graphics, which were not decoded or inspected here. No notebook code was
executed. Access and a text-scope comparison are complete; an exact comparison with its Rule 30 figures remains a
named dependency before any priority claim. Absence of a theorem in the extracted prose is not novelty evidence.

## A finite ether-window bound (GC2327, PROOF-SKETCH)

This section is a new solo carrying argument and remains **PROOF-SKETCH** until Local or another authorized
independent worker reads it. Same-worker arithmetic or finite checks do not upgrade that status.

Use PR69's edge map, with digit 0 constant black and, at depths j>=2,

    X_j(t+1) = X_j(t) XOR (X_(j-1)(t) OR X_(j-2)(t));
    X_1(t+1) = X_1(t) XOR X_0(t).

For a pair (u,v)=(X_(k+1),X_k), define the eight-phase predicate exactly as in that source:

| r mod 8 | `good(r,u,v)` |
|---|---|
| 0 | u=0, v=1 |
| 1 | u=1 |
| 2 | u=0, v=0 |
| 3 | u=1 |
| 4 | u=0, v=0 |
| 5 | u=1-v |
| 6 | u=1, v=0 |
| 7 | u=1 |

**Claim.** For any k, phase p, and starting time s>=0, this pair cannot satisfy good(t+p) throughout
`s <= t < s + floor(2k/3) + 5`. Consequently an actual ether pair cannot agree for that many consecutive ticks.
This upper bound alone does not establish sharpness; the later construction supplies its leading coefficient. The statement concerns fixed offsets behind a moving black edge, not Q01's fixed
physical wall or the seed's fixed centre column.

### Local dependency table, derived by hand

For adjacent columns u=X_(j+2), v=X_(j+1), w=X_j we have
Delta u = v OR w and w=1 implies Delta v=1, also when j=0. To infer good(h,v(t),w(t)), it suffices that the pair
(u,v) satisfies good(h+2+d) at the times t+d in the following set D(h):

| target phase h | D(h) | Reason, with f=v(t), g=v(t+1), y=w(t) |
|---|---|---|
| 0 | {0,1} | Source phases 2,3 give u(t)=f=0, u(t+1)=1; Delta u=f OR y forces y=1. |
| 1 | {0,1} | Source phases 3,4 give u(t)=1, u(t+1)=g=0; f OR y=1 and y implies f XOR g=1 force f=1. |
| 2 | {0,1} | Source phases 4,5 give f=u(t)=0, u(t+1)=1-g; thus y=1-g; y implies g=1, so y=0. |
| 3 | {-1,0} | Source phases 4,5 at t-1,t give v(t-1)=u(t-1)=0, u(t)=1-f. Thus w(t-1)=1-f; if it were 1, Delta v would force f=1, a contradiction. Hence f=1. |
| 4 | {0,1} | Source phases 6,7 give f=0 and u(t)=u(t+1)=1, hence y=0. |
| 5 | {0,1} | Source phases 7,0 give u(t)=1, u(t+1)=0, g=1. Thus f OR y=1; y implies f=0, so f=1-y. |
| 6 | {0,1,2} | Source phases 0,1,2 give f=1, u(t)=0, u(t+1)=1, u(t+2)=v(t+2)=0. If g=0, Delta u(t+1)=1 forces w(t+1)=1 against Delta v(t+1)=0. So g=1 and y=0. |
| 7 | {0,1} | Source phases 1,2 give u(t)=1, u(t+1)=g=0; the same implication as h=1 forces f=1. |

These are the eight cases underlying PR69's descent, with only the actually used input ticks retained. In the
published formulation the phase advances by 6 when moving one depth toward the edge. Accordingly, tracing a
dependency outwards changes its phase by 2+d, as in this table.

### Weighted proof tree

To infer an edge predicate of phase h from depth k, repeatedly apply the preceding table outward k times.
A path adds offsets d and changes h to h'=h+2+d modulo 8. Put

    P(0),...,P(7) = 0,5,2,-1,4,1,6,3.

Every one of the 17 edges satisfies `3d-2 <= P(h)-P(h')`. Equality holds except for (h,d)=(1,0) and (6,0),
where the slack is 8. Telescoping gives

    total offset <= floor((2k + P(initial h) + 1)/3),

since the smallest potential is -1. There is no unrecorded past-time requirement: start at an even phase h and
offset 0. At every intermediate node the phase parity equals the offset parity. The only negative step, -1,
occurs at phase 3, hence at an odd nonnegative offset, which is at least 1. Thus every intermediate offset stays
nonnegative. All uses of the recurrence are at defined times.

At depth zero, `good` is impossible at phases 2,4,6 because its second bit is the constant black edge. Write
m=floor(2k/3) and let r=(s+p+6k) mod 8 be the prospective edge phase at s. Choose a contradictory phase as follows:

| r | chosen edge phase h | delay t-s | upper bound on outward offset |
|---|---|---|---|
| 0,1,2 | 2 | 2-r | m+1 |
| 3,4 | 4 | 4-r | m+2 |
| 5,6 | 6 | 6-r | m+3 |
| 7 | 2 | 3 | m+1 |

For a leaf at total offset a after k outward steps, its phase is h+2k+a modulo 8.
The chosen edge phase is h=t+p+6k, so this is t+p+a modulo 8, exactly the assumed source phase.
Also `ether_pair` in PR69 gives good(t+q+2i) for ether spatial phase i and temporal phase q; every actual
matching ether pair therefore supplies one of the source phases covered here.

The delay plus the maximum offset is at most m+4 in every row. All leaves of the proof tree therefore lie in the
assumed source interval [s,s+m+4]. They force an impossible predicate at the edge. This proves the claimed
exclusion, conditional only on the local dependency table just derived.

### Controls and limits

- The actual two-sided ether satisfies the pair predicate forever; a constant black edge is essential.
- At k=0 the abstract predicate can hold for three ticks (phases 7,0,1, with pair (1,1),(0,1),(1,1)). This refutes
  any claim of immediate incompatibility. The bound five at k=0 is deliberately not sharp.
- The crude four-tick descent would instead give 3k+4. The improvement uses the phase table and its bounded
  potential, not an assumed uniform propagation speed.
- No period of the orbit, finite support, random initial measure, or absence of exceptional events is assumed.
- This does not give a permanent defect, prevent later re-entry, prove alternating-tail exclusion, or solve Q01.
  It says every sufficiently long time window contains a failure of this particular pair predicate.

**A robust consequence, still within the sketch.** Put B=floor(2k/3)+5. In every N consecutive ticks, at least
floor(N/B) ticks fail the specified good-pair predicate: divide into disjoint B-tick intervals. An actual ether
match implies that predicate, so there are at least as many mismatches with any fixed spatial/time ether phase.
Thus at this fixed depth there cannot even be an ether match outside a set of times of density zero. The bound
decays with depth and says nothing about the right-edge doubling density or an unbounded moving depth.

**Why 2/3 appears.** The dependency graph contains the critical cycle
`0 --(+1)--> 3 --(0)--> 5 --(+1)--> 0`: three outward steps require a two-tick advance. It is reachable from each
contradictory even phase. The potential proves that no dependency path has a larger asymptotic advance per step.
Therefore 2/3 is the exact maximum cycle mean of this particular dependency graph. It is not a measured orbit
speed. Reducing the leading coefficient by this method needs stronger local implications or a reason to discard
some branches of the proof tree. It does not follow that real edge orbits attain the bound.

## Frozen finite self-check (not yet run at freeze)

One pilot will check the eight dependency implications by exhaustive local assignments, all 17 potential
inequalities, the boundary positive control, and every initial black-edge prefix through depth 9 against the
claimed finite bound for k=0..8. A literal physical Rule 30 implementation is an independent implementation
control for the edge map. The false stronger claim of immediate incompatibility must be rejected. This is a
finite self-check of a hand claim, not its independent carrying read or a proof for arbitrary depth.

The source/hash, exact command and stage caps are recorded in the ledger freeze before execution. No longer
horizon or automatic retry is authorized by this pilot. Results and next executable step will be appended here.

### Actual pilot outcome (GC2328)

The one run under freeze e674c2fa completed at 15:23:21 UTC and **PASSED**. All 2048 local assignments were checked
against the eight implications (each implication had a nonempty satisfying premise set), all 17 potential edges
passed, and 1,022 initial prefixes / 8,176 prefix-phase cases at k=0..8 obeyed the bound. The separate physical
truth-table oracle agreed at all 86,912 compared cells. The positive infinite ether, rejection of immediate
incompatibility, and negative-time guard controls passed. No horizon enlargement or retry occurred.

The exact maximal initial good-run lengths in these finite complete prefix cubes were
`3,4,5,6,6,7,7,8,9`. These are checks, not an inferred all-depth formula. Several witnesses begin with
`1` followed by the repeating pattern `1110`, which is a concrete future front-propagation question; no additional
run or attainment claim was made. Such prefixes can be extended arbitrarily because nearer edge digits evolve
autonomously. The claim for arbitrary depth rests on the hand argument above, still awaiting independent reading.

Intel resources: worker aggregate CPU 0.135153s (own CPU plus reaped thermal children), supervisor CPU 0.094s
separately; child wall 0.14s and supervised wall 0.54s. The system time receipt reports maximum RSS 13,041,664 bytes.
Launch free+inactive was 7041MiB, swap 0, both thermal checks passed. The job finished before the first periodic
tree/pressure sample; sampled zeros are not a claim of zero RSS, zero processes, or continuous pressure coverage.
Raw receipts and their digest-bound shared-store packet are retained outside git.
The immutable raw packet is `cited/gpt-gc2328-ether-window-39063cccfa07.json`, 22,808 bytes, SHA256
`39063cccfa07ca722363e18fc462e540f4ef3440af2b63ca216524743f1becf8`. The raw-body upload receipt and a complete
readback matched the bytes. It contains the frozen probe, exact PR69 source, outputs, resource receipt and a fresh
no-worker postcheck. No private configuration or credentials were included.

## An actual family makes the leading coefficient sharp (GC2328, PROOF-SKETCH)

This is a second solo hand step, after the frozen check. No extra simulation was used to infer an infinite family.
It uses the same actual `ether_step` positive control, not a hypothetical permitted word.

Let `E_j(t)=ether(j+3,t+1)`, with ether indices taken modulo 4 and 8 as in PR69. Initially its depth digits are

    E(0) = 0,1,1,1,0,1,1,1,0,... .

Take a black-edge code X with X_0(0)=1 and X_j(0)=E_j(0) for all j>=1. The reference E is a genuine two-sided
solution of the edge-frame recurrence; it does not itself satisfy the constant-black boundary.

**Masking-front lemma.** If X_j(t)=E_j(t) for every j>R, with R>=0, then they agree for every j>R+2 at time t+1.
If additionally E_(R+1)(t)=1, they also agree at j=R+2: the OR gate there is already 1 because of the common nearer
input at R+1, whatever the differing input at R does. Hence a valid boundary of the possible disagreement region
advances by 1 when that reference bit is 1, and by 2 otherwise. Only columns >=2 are used, so the special depth-1
equation and the forced depth-0 edge cause no gap in this argument.

Starting at R_0=0, take R_t=floor(3t/2). The necessary reference bits are given by this complete phase check:

| n mod 4 | E_(3n+1)(2n) | E_(3n+2)(2n+1) |
|---|---|---|
| 0 | ether(0,1)=1 | ether(1,2)=0 |
| 1 | ether(3,3)=1 | ether(0,4)=0 |
| 2 | ether(2,5)=1 | ether(3,6)=0 |
| 3 | ether(1,7)=1 | ether(2,0)=0 |

The table reads directly from the source words 43,202,178,172. Thus the masking-front lemma gives one layer of
possible advance at even t and two at odd t, proving by induction

    X_j(t)=E_j(t) whenever j > floor(3t/2).

At depths k,k+1, this gives an actual matching ether pair at every integer time `0 <= t < 2k/3`, namely
ceil(2k/3) consecutive ticks for k>=1. The auxiliary code had an infinite periodic tail, but the witness need not:
truncate its initial digits after k+1 and put zeros deeper. Edge-prefix autonomy preserves every digit through
k+1 for all future times. The resulting ordinary finite Rule 30 row therefore has exactly the same matching
episode. No assumption about behaviour after the first possible disagreement is needed.

Let M(k) be the largest length of a consecutive ether-pair episode at depths k,k+1, allowing any initial
black-edge row, either finite or infinite, any onset, and any fixed ether spatial/time phase. The new upper sketch
and this explicit finite-row construction give, for k>=1,

    ceil(2k/3) <= M(k) <= floor(2k/3)+4,
    hence M(k)/k tends to 2/3.

The upper bound is uniform over the larger infinite-row class; the lower bound already holds in the finite-row
class, so both classes have that same limiting coefficient. This is an extremal **episode-length** limit, not an
orbit-density limit, a claim that every row has that speed, or exact equality of the additive constants. Both
carrying steps remain PROOF-SKETCH pending independent review. The finite pilot preceded this construction and
must not be described as having tested or proved this all-depth lower bound.


## Durable queue and review boundary

- **Current target:** independently carry the finite ether-episode theorem. Exact next step: read the eight local
  implications, offset parity guard and phase identity above, then the eight-bit masking-front induction and
  finite-prefix truncation. These are the two new carrying steps; the small pilot is only a self-check. If accepted,
  first compare the exact quantitative statement with PR69 and Phillips's Rule 30 figures, then prepare a formal
  statement. No submission or separate formalization owner has been assigned.
- **Warm alternative:** the second 2058 timer's symbolic attainment. Start from the already executed first timer in
  the nested essay; identify its next forced pair and the exact boundary condition. Do not rerun stage one.
- **Curiosity:** characterize clock-supporting interfaces in spatially periodic backgrounds. Start with the known
  seven-cell sea and B3/B4 masking implication, and ask which local masking identities survive phase changes.
  This could separate a structural interface criterion from an arbitrary period census. No larger census queued.
- **Cold approaches:** the free-left-diagonal shortcut reopens only with a specific growing-triangle or decoded-tail
  identity; the sea-only uniform bound and all-noncheckerboard eventual-death conjecture are refuted as stated;
  the right-diagonal forbidden-word route reopens with a word outside G258/G267/G268 or a structural language law.
- **Unchanged open problems:** Q01, right-edge density, exact language entropy/soficity and the additive optimum
  for M(k). Nothing here resolves these. Older GC2314/GC2321 sketches retain their separate pending reads.

The owner's approximately 30-minute block ends with these passive pointers. Both schedules remain paused, Local
has not been woken, and no research job, compilation or posting is running. Resume only on the owner's direction.


### Publication and passive coordination receipt

Mathematical milestone `9103352e` was pushed after a fresh merge, privacy/conflict review, ledger check and document
link check. The frozen probe is unchanged. The two L1257 flags received scoped acknowledgements after the complete
carrying reads; passive READ-LEDGER and REVIEW-REQUEST pointers identify the exact new source for a future
owner-authorized read. Local's chat was not woken and no job was assigned.

The current compact shared-store queue is `flags/gpt/current-queue.GC2329.json`, SHA256
`377016bf1cf500c9a53ac6707eb51f3434cc3a19233c66a378b9855de9446dfb`, 3,194 bytes. Its raw-body upload and full readback
matched, as did the five state/acknowledgement/review pointers. The old large `coordination-state.json` remains
unchanged: automatic approval review declined an additional historical archival upload because that old payload's
sensitivity had not been established. No archival copy was uploaded, no historical evidence was deleted, and the
small new queue contains only this block's reviewed, nonprivate summary. The current NOW/report/queue supersede
that historical state's stale active-task fields.


## GC2330 — carrying Local's early-healing refinement

The owner passed back Local's response. Fetched and merged `d0bec896`, read L1258, the complete round-three
argument, the new probe source and both addressed flags. Local's independent read explicitly covers all eight
upper implications, all 17 potential edges, the parity and phase guards, the original lower construction and its
finite truncation. That is the required second read of GC2327–GC2328, not merely receipt or numerical agreement.

**L1258's new step is PROVED, two-party hand (Local proof, GPT read).** For the same witness and reference
E_j(t)=ether(j+3,t+1), the only initial mismatch is at j=0. I checked the special depth-one equation separately:
E_1(0)=1, X_1(1)=0=E_1(1), and the reference's missing neighbour E_(-1)(0)=ether(2,1)=1 supplies its OR. At j=2,
the common bit E_1(0)=1 masks the edge difference. All larger depths have identical update inputs. Since
E_0(1)=ether(3,2)=1, the whole nonnegative half agrees at t=1. In the next two updates the common edge bit is 1,
so the special depth-one equation again agrees with the two-input reference OR. E_0(2)=ether(3,3)=1 gives complete
agreement at t=2, while E_0(3)=ether(3,4)=0 leaves only depth zero mismatched at t=3. This checks the boundary
exception that a generic identical-input argument alone would miss.

Restart the carried masking-front lemma with R_3=0. Allow two layers at t=3+2n. At t=4+2n the front is 3n+2,
and its next reference bit is E_(3n+3)(4+2n). For n modulo four these are ether(2,5), ether(1,7), ether(0,1),
ether(3,3), all 1 in the source words 43,202,178,172. That tick therefore needs only one layer. Induction gives
agreement at j>R_t with R_t=ceil(3(t-3)/2), for t>=3. Odd-tick reference bits need not be zero: the two-layer
advance is an allowed upper bound on possible disagreement, not an assertion that the front actually moves.

For k>=1, pair agreement holds at t=0,1,2 and at every integer t satisfying
ceil(3(t-3)/2)<=k-1. The last guaranteed tick is 3+floor(2(k-1)/3), so the inclusive count is
floor(2(k-1)/3)+4. Prefix truncation still preserves both observed columns for all time. Together with GC2327:

    floor(2(k-1)/3)+4 <= M(k) <= floor(2k/3)+4;
    M(3n+1)=2n+4 for every n>=0.

The two endpoints coincide exactly in that residue class. In the other two classes they differ by one.
Local's computations suggest which endpoint wins, but the hand proof does not choose it.

### Computation review scope and next step

I read `tests/probes/ether_episode_exact.py` without running it. Its all-prefix/all-phase search matches the
quantifiers: any onset gives an initial prefix, and every initial prefix extends to a finite row. Its alive mask
counts consecutive matching ticks and never restarts after a mismatch. Its horizon exceeds the carried upper
bound, and the script rejects reaching that horizon. These are sound reasons for the reported finite enumeration
to be exact. Local reports M5 CPU 1.60s, maximum RSS 436MB and output digest prefix 3dd3599b; I have not independently
retrieved its raw run packet or replayed those measurements. The full formula remains **COMPUTED through k=20,
CONJECTURE beyond**, distinct from the hand-proved residue family. The physical oracle evolves for 40 ticks but
compares only while its shrinking depth loop is nonempty (t<=30); the P-E4 and P-E5 comparisons print their results
rather than assert them. Neither detail invalidates the reported outputs, but an independent certificate read must
inspect those actual lines rather than treating the final completion marker alone as all-controls acceptance.

**Next executable mathematical step:** for the fixed witness, track the two boundary bits of the mismatch set
at t=3+2n and t=4+2n, to try to carry the proposed extra matching tick when k ≡ 3 or 5 (mod 6). A separate upper
argument must remove one tick for k ≡ 0 or 2 (mod 6); witness analysis cannot establish that universal exclusion.
Do not enlarge the census as a substitute. The previous second-timer alternative and periodic-interface curiosity
remain available. Both recurring schedules stay paused; no live Local job or formalization is dispatched.
