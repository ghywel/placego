# GPT's carrying read and continuation of the October 31 inquisition

Owner-authorized bounded block, beginning 15:11 UTC. Both recurring schedules remain paused; Local is stopped.
The handover is [L1257](HANDOVER-GPT-20261031.md), with its [complete tracker](inquisition-20261031.md).

**Latest, GC2333 / L1259–L1260: the all-depth formula is PROVED, two-party hand.**
For every k>=1, M(k)=floor(2k/3)+4-[k≡0 or2 mod6]. At edge phase7 the witness is the unique optimal prefix,
not the unique whole row or unique maximizing phase. GPT carried the front proof, replayed its small certificate
once with a rejected-mutation control, and also carried the six-depth descent's hand reductions. The required
mismatch condition is bounded above / finite positive tail, not finite support on all integers. No Lean verification,
submission or novelty clearance is claimed. The older open-gap entries below are historical.

**Latest, GC2331 / CL669:** Cloud's exact witness-front argument is now independently carried, with an explicit
four-tick/six-depth band return checked by hand. Thus M(k)=floor(2k/3)+4 is **PROVED, two-party hand** for
k congruent to 1,3,4,5 modulo 6. The full witness-length formula is proved for every k, but its optimality for
residues 0 and 2 remains open. The proposed exact-pair descent requires t<=L-2; it supplies no terminal-tick value.

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

## GC2331 — Cloud's exact front carried with a four-tick band certificate

The owner passed back CL669. GPT fetched `4943af9b` and read the complete round-four argument, the certificate
source `tests/probes/wolfram/ether_witness_front.py` (SHA256
`8ace97f7fb6dc43939c71d1c5add0baa31610c2031268a16927f0cf94a5320aa`) and its recorded output (SHA256
`831dc9a3ddffa20d23d4cce883016643c07fcfdf972c1f1f6f5ebf06f7da1b36`). The carrying check below is by hand; it
replaces the sampled arithmetic identities by residue calculations and reduces the eight-tick return to four.
It does not rerun Cloud's computations or validate the unrelated restored proofs in that commit.

**Status: PROVED, two-party hand (Cloud argument/certificate, GPT carrying read).** Write R(t)=2 floor((3t-8)/4)
for t>=4. The actual witness has maximal mismatched depth R(t). At t=0,3 its maximal mismatch is 0, and at t=1,2
there are no mismatches. Its pair episode length is

    L_w(k)=ceil((4 ceil(k/2)+8)/3),

and therefore M(k)=floor(2k/3)+4 for k congruent to 1,3,4,5 modulo 6. Only the universal upper estimate for the
other two residues remains open. This concerns offsets behind a moving black edge, not a fixed-centre density.

### Initial condition checked separately

Encode depths 0..15 as the low-to-high bits of a 16-bit integer x. Prefix autonomy makes their update exact:

    x_next = (x XOR ((x << 1) OR (x << 2))) AND 0xffff.

The low bit stays 1, and the depth-one bit uses only depth zero, as required. Direct hexadecimal substitution
in that identity gives the following table; the last column is x XOR the reference's 16-bit prefix.

| t | x | reference E | mismatch mask |
|---|---|---|---|
| 0 | eeef | eeee | 0001 |
| 1 | 1111 | 1111 | 0000 |
| 2 | 7777 | 7777 | 0000 |
| 3 | 8889 | 8888 | 0001 |
| 4 | bbbf | bbbb | 0004 |
| 5 | 4441 | 4444 | 0005 |
| 6 | ddc7 | dddd | 001a |
| 7 | 2259 | 2222 | 007b |
| 8 | efaf | eeee | 0141 |
| 9 | 1051 | 1111 | 0140 |
| 10 | 71b7 | 7777 | 06c0 |
| 11 | 9649 | 8888 | 1ec1 |
| 12 | ebff | bbbb | 5044 |

For 3<=t<=12, the already carried bound U(t)=ceil(3(t-3)/2)<=14 excludes any mismatch beyond this prefix.
The earlier healing proof covers t=0,1,2. Thus the table proves the actual maximal mismatch through t=12,
not merely a lower bound on a truncated row. At t=12 the band at depths 7..15 is `111010111`.

### The guarded band and its return

For t=4q+r with 0<=r<4, the two front formulas give:

| r | R(t) | U(t) | U(t)-R(t) |
|---|---|---|---|
| 0 | 6q-4 | 6q-4 | 0 |
| 1 | 6q-4 | 6q-3 | 1 |
| 2 | 6q-2 | 6q-1 | 1 |
| 3 | 6q | 6q | 0 |

Consequently every cell strictly above R(t)+1 equals E. A band [b,R(t)+1] can be advanced without knowing cells
below b: if X_b=1, its next bottom is b+1, where that 1 masks the missing input at b-1. If X_b=0, choose bottom
b+2, whose two inputs are both already in the band. Higher required input cells come from the known ether above.
This is a band driven by a specified upper boundary, not an assertion that it is isolated from all exterior data.
All updated depths in the cycle below are >=8, so no special edge equation is hidden in this argument.

Evaluating these short Boolean rows by hand gives the entire return (strings are ordered by increasing depth):

| t | band | contents | mismatches inside band |
|---|---|---|---|
| 12 | 7..15 | 111010111 | 12,14 |
| 13 | 8..15 | 00101000 | 12,14 |
| 14 | 10..17 | 11011000 | 12,13,15,16 |
| 15 | 11..19 | 010011010 | 12,13,15,16,17,18 |
| 16 | 13..21 | 111010111 | 18,20 |

The required reference glide is immediate from the source words: 43=0x2b and 178=0xb2 exchange nibbles, as do
202=0xca and 172=0xac. Hence ether(i+2,t+4)=ether(i,t), and E_(j+6)(t+4)=E_j(t).
Both R and U increase by 6 after four ticks. Thus the band contents, its bottom-update rule and its ether inputs
at t=16 are exactly those at t=12 shifted by six depths. Induction repeats this four-tick cycle indefinitely;
Cloud's eight-tick/twelve-depth return follows by two cycles.

At each phase, the band contains a mismatch at R and agrees with E at R+1. The bound U<=R+1 excludes mismatches
above its top. Unknown cells below its bottom lie strictly below R. Therefore R is the actual maximum, without
assuming that the band contains the entire mismatch set. This last distinction matters: at t=12 the full mask
5044 also contains mismatches at depths 2 and 6 below the band.

### First arrival and the exact residue classes

For k>=1, no pair mismatch occurs at t=0,1,2,3. Thereafter R is nondecreasing and jumps by either 0 or 2, always
landing on an even depth. Its first arrival at a depth >=k is therefore exactly at k or k+1, and that front cell
really is mismatched. Before this arrival both observed cells match. Solving the integer inequality gives

    2 floor((3t-8)/4) >= k
    iff 3t >= 4 ceil(k/2)+8.

The first such t is at least 4, so there is no omitted early case. This t is the number of matching ticks from
zero. The six residues make the formula, rather than a finite symbolic sample, explicit:

| k | L_w(k) | carried upper bound for M(k) |
|---|---|---|
| 6n (n>=1) | 4n+3 | 4n+4 |
| 6n+1 | 4n+4 | 4n+4 |
| 6n+2 | 4n+4 | 4n+5 |
| 6n+3 | 4n+6 | 4n+6 |
| 6n+4 | 4n+6 | 4n+6 |
| 6n+5 | 4n+7 | 4n+7 |

Truncating the witness beyond k+1 preserves both observed cells for all time, so the same exact witness episode
occurs in the finite-row class. Equality with M follows in four residues; witness optimality in the two remaining
residues does not follow from this construction.

### Scope of Cloud's diagnosis and the terminal-tick guard

Cloud's max-plus comparison through depth 24 and its exact good-predicate comparison through depth 20 are
COMPUTED claims, not all-depth impossibility theorems for every argument based on that table. I have not replayed
or independently retained the raw packets for those diagnostic computations. They usefully suggest two different
obstructions, but do not yet prove that distinction for every member of either residue class.

There is one endpoint qualification to the proposed exact-pair descent. If the pair matches on ticks 0..L-1,
its successive differences are supplied only on 0..L-2. Thus both conclusions

    E_k(t)=0 implies X_(k-1)(t)=E_(k-1)(t),
    X_(k-1)(t) OR X_(k-2)(t) = E_(k-1)(t) OR E_(k-2)(t)  (k>=2)

are justified on t<=L-2, not automatically on the final tick L-1. The first follows from the depth-(k+1)
update; the second from the depth-k update. For example, an episode of length one fixes only the pair itself,
leaving X_(k-1)(0) arbitrary even if E_k(0)=0. The missing next pair value is precisely the information needed
for that final inference. Any attempt to save the remaining tick must retain this endpoint restriction.

**Next executable step:** formulate the two-residue upper target with the exact-pair constraints restricted to
0..L-2, then trace which constraints can meet an impossible edge phase without asking for the unavailable final
successor. An alternative is a joint-branch inconsistency for the good predicate in residue 0. No larger census
is queued. The second-timer and periodic-interface alternatives remain in the queue.

No new computation ran. A sandboxed preflight could read memory but could not obtain swap/thermal status;
no capped job was launched or retried, and the review continued with the explicit hand tables above. No compiler,
formal verification, submission, priority clearance or schedule restart is claimed.

## GC2333 — L1259/L1260 reviewed: the all-depth maximum and the phase-seven optimum

**Verdict: PROVED, two-party hand, via Proof 1 and its finite transition tables.** For every k>=1, in the moving
black-edge frame and over every initial row, onset and ether phase,

    M(k)=floor(2k/3)+4-[k≡0 or 2 (mod 6)].

At edge phase c=7 the GC2328 witness is the unique optimal prefix through depth k+1. This does not mean a unique
whole row: cells beyond the observed prefix can be arbitrary. Nor does it mean that phase 7 is the only maximizing
phase. The theorem covers both finite rows and arbitrary tails; no fixed-wall, centre-column or density inference
is made.

The requested hand steps of Proof 2 also check, conditional on its stated finite window certificates. I read
both enumerators and its SAT encoding, but did not rerun those larger checks. I read Proof 3's source and its
coverage/replay guards as an additional audit, not a new independent replay of its 254 LRAT artifacts. The
all-depth verdict above does not depend on accepting an uninspected solver trace or on the sixteen same-worker
"not refuted" verdicts.

### Scope repair: right-bounded mismatch, not finite support on all integers

Put X_j=0 for j<0 and X_0=1. The generic recurrence preserves these values, and at depth one gives the required
X_1'=X_1 XOR 1. The reference is E_j(t)=e(t+2j+c), e=(1,1,0,1,0,1,0,0), at every integer depth.
Thus D=X XOR E has infinitely many negative-depth mismatches. Literal finite support of D on all of Z is neither
true nor needed. The needed hypothesis is that D_j(0)=0 for all sufficiently large **positive** j. Equivalently,
the nonnegative mismatch set is finite. Its full mismatch set is nonempty and bounded above, so R=max{j:D_j=1}
exists. Each parity subsequence of e contains a 1, ensuring a negative mismatch at every time; there is never an
empty full mismatch set. F(0,0)=0 keeps the mismatch bounded above under iteration.

In particular the witness's full two-sided fronts at times 1,2 are -4,-2, whereas its **nonnegative** mismatch set
is empty at those times in GC2331. These are consistent descriptions of different domains. References in the
round-five prose to a "finite-support row" or "finite initial mismatch" must be read as finite positive mismatch
after the tail replacement below, not as a restriction on the original row or on all integer depths.

### Front rule, no-retreat step and potential

Subtracting the two Boolean recurrences gives D_j'=D_j XOR F_phi(D_(j-1),D_(j-2)), with phi=t+2j+c. Directly
substituting the two reference inputs yields OR for phi=0,6; (NOT a) AND b for phi=1,4; a AND (NOT b) for phi=2,3;
and AND for phi=5,7. This verifies the four claimed forms without assuming a statistical law.

At a front R let a=D_(R-1), b=D_(R-2), and psi=t+2R+2+c. The potential uses

    g=(-3/2,0,3/2,-1,1/2,-2,-1/2,1),
    Phi=R+g(psi)-3t/2.

Since the cells above R are clean, the next mismatches at R+2 and R+1 are respectively F_(psi+2)(0,1) and
F_psi(1,a). This gives the complete front table:

| psi | front change |
|---|---|
| 0 | +1 |
| 1 | 0, except retreat if a=b=1 |
| 2 | +2 |
| 3 | +1 if a=0; otherwise 0 |
| 4 | +2 |
| 5 | +1 if a=1; otherwise 0 |
| 6,7 | +2 |

In the cases where neither higher cell mismatches, substituting the update at R verifies the stay/retreat cases.
No cell above R+2 can change. The ten non-retreat transitions have psi'=psi+1+2 delta and satisfy
2 delta+2g(psi')-2g(psi)=3, hence preserve Phi.

Only a forced +2 transition from psi=4 can enter psi'=1 without retreat; it leaves the cell just below the new
front clean, since F_4(1,a)=0. A retreat starts at psi=1 and lands at psi'=2+2 delta, which is even for every
negative integer delta. Consequently whenever psi(t)=1 with t>=1, its predecessor was psi=4 and its subfront
bit is zero. It cannot retreat then. This proves no retreat in any transition t->t+1 for t>=1, and constant Phi
from time 1 onward. The first transition is allowed to retreat, which is why time-zero floors would be wrong.

### Healing and the time-one floors

If all positive cells heal at time 1, their initial mismatch bits are forced recursively:

    D_j(0)=F_(2j+c)(D_(j-1)(0),D_(j-2)(0)),
    D_0(0)=1-e(c), D_(-1)(0)=e(c-2).

This is a unique sequence, not a probabilistic choice. Once two consecutive bits are zero, all remaining bits
are zero. Otherwise a repeated state (last two bits,j mod4) gives an infinite nonzero tail. Direct substitution
makes the load-bearing exclusions explicit:

| c | forced positive mismatch sequence D_1,D_2,... for complete healing at time 1 |
|---|---|
| 0,1,3,5,7 | all zeros |
| 2 | 011 followed by (0111) repeated |
| 4 | (1101) repeated |
| 6 | 1 followed by (0111) repeated |

Thus c=2,4,6 cannot heal completely after a finite positive-mismatch start. At c=7 the sole healing start is
exactly the witness. Every other start at that phase has R(1)>=1.

For H_c(t,R)=R+g(t+2R+2+c)-3t/2, increasing R by one changes H by either 0 or 4 (the latter only at psi=0,5).
The fixed nonpositive cells at time 1 give r_c below. Apply monotonicity, and replace r_c by 1 for the excluded
healing sequences; c=7 is separated into witness and non-witness rows:

| c | r_c from nonpositive cells | lower bound on Phi(1) | minimum permitted R at t=1,2,3,4 |
|---|---|---|---|
| 0 | -2 | -5/2 | -2,-1,1,2 |
| 1 | 0 | -1 | -1,1,2,4 |
| 2 | -1 | 1/2 | 1,2,4,5 |
| 3 | 0 | -2 | -2,0,1,3 |
| 4 | -1 | -1/2 | 0,1,3,4 |
| 5 | 0 | -3 | -3,-1,0,2 |
| 6 | 0 | -3/2 | -1,0,2,3 |
| 7, non-witness | -4 | 0 | 0,2,3,5 |
| 7, witness | -4 | -4 | actual front -4,-2,0,2 |

The minima are conservative potential bounds, not assertions of reachability. For example c=4 really has R(1)>=1,
although the potential alone permits R=0. Substitution verifies that each listed minimum meets the floor and its
predecessor does not. The identity H_c(t+4,R+6)=H_c(t,R) extends these four columns to every t>=1.
They all dominate the witness front R_w; the c=7 non-witness row dominates it by at least 3. The witness cycles
through phases 2,7,4,1 with forced front increments 2,2,2,0; the no-retreat result handles its psi=1 tick.
This also recovers the previously carried witness law, rather than assuming it for the upper comparison.

### Clean-tail reduction and uniqueness

Reset an arbitrary episode onset to time zero, absorbing the time shift into c. Replace only initial cells above
k+1 by E. Prefix autonomy preserves the observed pair at all later times. The replacement creates finite positive
mismatch, irrespective of the original tail. If the pair matches on 0..L-1, then all cells above k+1 remain E
throughout that interval: induct on time, using the exact pair as the two lower inputs of the unchanged tail.
Together with pair agreement, this gives R(t)<k for every episode tick. This tail induction is necessary;
front comparison alone would not rule out a remote mismatch above a still-matching pair in an unmodified row.

At T=L_w(k), the universal comparison gives R(T)>=R_w(T)>=k. An episode with T+1 matching ticks is therefore
impossible. The carried finite-prefix witness attains T, proving M(k)=L_w(k) for every k>=1.
For uniqueness at c=7, suppose the prefix differs from the witness. Its modified row is non-witness, so
R(T-1)>=R_w(T-1)+3. First arrival jumps by two onto k or k+1, hence R_w(T-1)>=k-2 and R(T-1)>=k+1.
It cannot match for all T ticks. Since T>=4, the comparison is used only at positive time. This proves precisely
unique prefix optimality at that phase; arbitrary deeper tails are still allowed.

### Proof 2: the requested light-cone and descent reductions

The generic rule's dependence interval at (j,t) is [j-2t,j], by induction on t. For a window W(s,b), let T=s+b.
The observed top pair through T and target pair at depth -6 at tick s therefore depend on the union contained in
[lo,1], lo=min(-2T,-6-2s). Enumerating its 2-lo digits covers every generic configuration, not a periodic or
black-edge subset. In the source the packed and unpacked enumerators do enumerate that same full cube; the SAT
recurrence clauses encode the same XOR-of-OR truth table. The extra four left digits in its SAT encoding cause
no restriction on the cone. The explicit require() checks survive optimized Python.

The seven windows are (s,b)=(0,10),(1,6),(2,6),(3,5),(4,5),(5,4),(6,4), each in eight phases. For L>=11 and a
requested target tick s<=5, its required top endpoint s+b is at most10<=L-1. For 6<=s<=L-5, apply W(6,4) to
Y_r(u)=X_(j+r)(s-6+u), with reference phase c'=c+2j+s-6. Its top window [s-6,s+4] lies inside [0,L-1], and its
target is exactly tick s at depths j-6,j-5. All eight phases are covered. Thus the resulting window is
0..L-5 inclusive, of length L-4: the final supplied top tick is used without inventing a successor at tick L.
This directly respects GC2331's endpoint objection.

For k>=9, a hypothetical episode of L_w(k)+1 ticks has length at least11 and descends to length
L_w(k)+1-4=L_w(k-6)+1 at depth k-6. The equality follows immediately from ceil((k-6)/2)=ceil(k/2)-3.
The finite bases k=1..8 therefore cover every positive k. Alternatively the open-residue induction uses bases
2,6,8 and starts at12. These are sound hand reductions. The 56 finite assertions and base computations remain
Local's reported certificate run (source read, no GPT solver/enumerator replay); the full theorem is already
carried independently by Proof 1 above.

### Computation, provenance and review limits

The single frozen Intel replay under `1ba7cb33` completed once, without retry, at19:22:56UTC. Local's unchanged
front certificate SHA256 `544d14c71a64c5ee1f2c77ea9aed813e65fbabc6374409f7200bc6ebb0f58ee5` passed every check;
changing the first doubled potential value by2 was rejected by the literal transition invariant. The wrapper's
source/hash and caps are in GC2332. Worker own+reaped-child CPU was0.394232s, supervisor CPU0.102s separately;
command wall0.43s, supervised wall0.54s, maximum RSS16,805,888bytes. Launch free+inactive4890MiB,swap0, both thermal
guards100%. It finished before the first periodic sample: sampled zero maxima are not zero usage or continuous
pressure coverage. Normal completion and a fresh no-worker process check were retained.

Immutable raw packet `cited/gpt-gc2333-front-review-e267b56acafc.json`,29,049bytes, SHA256
`e267b56acafc1c6b9bd20b1e805844a55c029e1d08d4ef81a537625fa4d449a7`, contains exact sources, outputs, resource and
cleanup receipts, and the fresh index output. Upload receipt and full raw readback matched. No Local M5 run was
relabelled as an Intel run. I have not retrieved/replayed the 254 raw LRAT proofs, the SAT-to150 run or the sixteen
sub-agent review artifacts. Their code and reported outcomes are supporting evidence, not a replacement for the
carrying argument above. Proof 3's abstract-system phases and clipping reduction are consistent with its stated
scope; no broader general rigidity claim is attributed to that single-phase route.

The complete external refresh at19:21:22UTC found no indexed changes: kit842b756f,23open PRs. This does not clear
priority, a submission package, or the outstanding Phillips figure comparison. The finite-state-front method is
credited to the existing ether-erosion work, and the reference to Lowry's PR69. No new solver stage, Lean build,
public submission or schedule restart was performed.

**Next executable step:** on an owner-directed delivery or continuation block, first turn the now-carried
front proof into one precise theorem statement with right-bounded mismatch, the clean-tail lemma and scoped
phase-seven uniqueness; then finish source/prior-art comparison before deciding on a package. Independent warm
alternative: the second 2058 timer. Curiosity: whether the six-depth exact-window rigidity extends to other
periodic reference solutions. The all-depth ether-episode formula itself is no longer an open research target.

## GC2335 — L1261 carried; odd-period backgrounds have a separate obstruction

31 October 2026, GPT. Review of Local's round six at 39757c75. No solver run, compilation, or
submission in this block. Local retains its ongoing Lean fidelity/adversarial work. Its new Lean file and
final validation receipt were not present in the fetched commits or the addressed review flag.

### Carrying read of the eight-background descent

The **hand reduction is accepted, two-party**. Its finite premises are Local's reported T-D4 computation
with checked LRAT proofs; I read the complete generator/checker and ring-reference source, but did not
receive/replay the 1,266 raw refutations or independently reproduce the numerical base table. Thus this is
acceptance of the requested carrying mathematics and source audit, not an independent certificate replay
or Lean verification.

1. Extend a black-edge code by X_j=0 for j<0 and X_0=1. The generic recurrence
   X_j(t+1)=X_j(t) XOR (X_(j-1)(t) OR X_(j-2)(t)) then holds at every integer j,
   including j=0,1 and the negative half-line. No finite left-support assumption is needed.
2. The dependencies of (j,t) are inside [j-2t,j] at tick zero. In `instance`,
   lo=min(-2T,-1-2a), T=a+b, covers the top pair through T and the target (-1,a).
   Every genuine solution restricts to a satisfying assignment of the recurrence clauses. This implication
   alone suffices for an UNSAT exclusion; no unwarranted extension of a finite model is used.
3. The six clauses encode y=x XOR (c OR d): for c=d=0 the first two give y=x;
   for either driver equal to one its corresponding two clauses give y=not x. The top units specify
   precisely the selected reference, and the final unit negates the desired target value.
4. Suppose an episode at (k+1,k+2) lasts L ticks, starting at arbitrary time n. For
   a<=s<=L-1-b, translate the window by depth k+1 and time n+s-a. Its top observations
   lie wholly inside the episode. All spatial and temporal alignments are included in the certificate,
   so it forces X_k(n+s) to match the same reference. X_(k+1) already matches. Hence the
   pair (k,k+1) has an episode of length L-a-b. If L<=a+b, the claimed upper bound is
   automatic; do not apply a nonempty-window argument to a negative length.
5. Consequently M_R(k+1)<=M_R(k)+a+b. The base at depth one enumerates all four
   possible (X_1,X_2), both of which toggle every tick because X_0=1, and all reference
   alignments. Every onset is included by restarting at its current prefix. The explicit
   `run < H` guard makes each reported first mismatch an exact finite maximum, rather than a
   horizon mistaken for an upper bound. Induction gives M_R(k)<=M_R(1)+(a+b)(k-1).

The checker accepts only positive-hint RUP steps, requires an actual propagation contradiction and an
empty derived clause, and rejects malformed/unsupported steps. The controls negate the target, require
SAT, and reject the original proof against that altered input; alternating remains a positive attachment
control. These are appropriate controls. The source deletes solver proofs after checking, so a durable
replay packet would need to retain them separately before a delivery claim based on independently
replayed certificates.

**Reference identity guard.** The implementation indexes orbits by (p,q), with a dictionary that would
silently replace a second orbit sharing that pair. Scope the eight claims to the actual selected orbits,
identified by their tick-zero words in T-D4, not to all backgrounds with the same period pair. A future
certificate export should use explicit orbit identifiers and an equality/uniqueness guard.

Exact sources read:
- `inquisition_background_rigidity_certificate.py`: SHA256
  b187a39451866141bc6280767855e55513d67aa74a30fc986a317d0b26bd68df.
- `inquisition_ring_references.py`: SHA256
  57a7e5a76148015f076059fab99c26434a21a8fd6bb82d38390ae9cdbe0a8527.
- Kit main 842b756fc7d043995e14019fee2a82ab4ec83cf7, `Rule30Ether.lean`: SHA256
  dc3d84cd13e0f091c400d60a0594e45dba59d9bc86aa224a328b2af66f06d756.

### The classic ether identification is explicit

Let P(x,t) be the kit's `Rule30Ether.etherTable`, interpreted modulo 7 and 4. The selected
ring word 1000000 is exactly

    R_j(t) = P(2+t-j,t).

At t=0 the table has its sole black cell at spatial residue 2, giving R_j(0)=1 iff j=0 mod7.
The physical Rule30 equation gives the displayed moving-frame recurrence: at the next tick its three
inputs are R_j, R_(j-1), R_(j-2). Determinism identifies the entire orbit. The +2 offset is
needed for this particular representative; the unshifted formula describes the same orbit class.

Its least moving-frame period is 28, not merely a divisor of 28. The numbers of black cells in physical
phases 0,1,2,3 are 1,3,3,6, so a moving-frame return must advance the physical phase by a multiple of four.
At phase zero the singleton then returns only if its spatial shift is divisible by seven. Conversely 28
is a period. This carries Local's identification by hand without an orientation search. The certified
linear bound is therefore genuinely about the classic ether, conditional only on T-D4's finite premises.

### A separate obstruction for every background with non-dyadic least period

**PROOF-SKETCH, GPT; independent carrying read requested.** This reuses the mechanism in GC733/GC734,
not a new general clock theorem. It removes the infinite-attachment question for the three shadowed
backgrounds, subject to that read and their reported exact ring periods; their linear episode bounds
remain open.

Let R be a solution of the generic recurrence, spatially periodic with positive period p, whose full
configuration has least temporal period q. Suppose q is not a power of two. For any black-edge code,
any onset/alignment, and any k>=1,

    M_R(k) <= 2^(k+1) + q - 1.

More generally replace 2^(k+1) by any common power-of-two period P of the observed black-edge pair.
This is an exponential fallback bound, not a replacement for Local's stronger linear bounds.

**Proof.** The known finite-diagonal theorem gives period 2^j to X_j, so the pair (X_k,X_(k+1))
has period P=2^(k+1), from tick zero and after every onset. Assume agreement with a reference pair
for P+q consecutive ticks. For each t=0,...,q-1 both t and t+P are inside the window. The
black-edge pair's P-periodicity forces the reference pair's values at these two times to agree.
Since the reference is q-periodic, this equality holds at every time: the reference pair is P-periodic.

Now if two successive reference cells are P-periodic, their OR is P-periodic. The next cell is its
XOR accumulator. Summing two complete P-blocks cancels the driver parity, so that next cell is
2P-periodic. Repeating this argument propagates power-of-two periods forward through one full spatial
circuit. All p reference cells therefore have a common power-of-two period (2^p P is a safe bound).
The least full-state period q divides every full-state period, contradicting its odd factor. This
settles the cheap objection that an individual observed pair could lose the global odd factor.

Equivalent invariant: let d_j be the least period of cell j and let o_j be the odd part of
lcm(d_j,d_(j+1)). The accumulator gives o_(j+1) dividing o_j. Spatial periodicity closes this
divisibility chain, so every o_j is identical; since the lcm of all cell periods is q, every o_j
is exactly the odd part of q. This is GC734's adjacent-pair invariant with the direction reversed
by the coordinate convention. A single cell need not carry the full odd part.

Applied to Local's selected cycles, q=63,57,68 have odd parts 63,57,17. Thus the three finite
shadow witnesses do not suggest eternal attachment to a black edge: they live in a generic model
without its dyadic clock boundary. Conditional on the reported least periods, the respective fallback
bounds are 2^(k+1)+62, 2^(k+1)+56, and 2^(k+1)+67. The same argument also excludes the classic
q=28 ether and the other non-dyadic cycles, but it cannot give the slope 58 or any linear bound.
White and PR69's q=8 ether are dyadic and require their separate arguments; alternating q=2
correctly survives this obstruction.

**Controls by hand.** Spatial periodicity is indispensable: without it propagation only constrains
one half-line. The least-period hypothesis is indispensable: declaring 3 to be a period of a
constant background does not make its least period non-dyadic. Arbitrary onsets cause no problem
because both clocks are periodic from their current states. No generic-shadow-to-black-edge
realization is assumed. No statement about fixed physical columns, walls or density follows.

### White episodes have a short exact proof

**PROOF-SKETCH, GPT hand explanation of Local's computed formula, no novelty claim:**
M_white(k)=ceil(k/2). If an interval of cells is white at consecutive ticks, the recurrence forces
its two preceding cells to be white at the earlier tick. An L-tick white pair at k,k+1 therefore
forces the entire interval [k-2(L-1),k+1] white at the onset. If L>ceil(k/2), this interval includes
the permanently black cell zero, a contradiction. Conversely the code with only X_0 initially black
has no influence at any depth greater than 2t at tick t; it supplies exactly ceil(k/2) initial white
observations of the pair. The upper bound establishes exactness. This needs no SAT certificate.

### Prior art, scope and next steps

Record searched: GC733/GC734 (odd-part invariant), GC738 (periodic-window obstruction), L1261,
and the actual kit/equivalents/catalogue index at 842b756f. Exact kit inputs read are
`Rule30FiniteDiagonals.Rd_periodic` and `Rule30Equivalents.WordsAutomata.eq_of_agree_of_periodic`.
The latter already proves the P+q agreement principle; the proof above spells out the special
comparison directly. `Rule30RingOrbits.encode_walk/decode_ring` supplies the known ring/profile
representation. General odometer background is credited by the kit to
[Coven–Pivato–Yassawi](https://arxiv.org/abs/math/0511030); periodic-word comparison is classical
([Rankin's account of Fine–Wilf](https://arxiv.org/abs/0906.1780)). These primary abstracts were
checked; no unexamined full-paper theorem or first-priority claim is used. The last complete external
index refresh remains 19:21:22Z, not a newly claimed refresh in this block.

L1261's sentence asserting that an attached periodic tail must flip everywhere every tick is not
established by its finite census or descent certificates. Keep it conjectural unless a separate
proof is supplied. Our obstruction narrows the remaining general question to dyadic-period
backgrounds; it does not classify them. The three shadowed cases still pose a useful quantitative
question: linear episode growth versus a larger growth law, not (after the proposed read) eternal
attachment. Local's finite 96-tick witnesses remain valid and useful.

Next executable step: independently carry the pair-to-ring dyadic argument and the P+q finite-window
bound, then update the three shadow cases' qualitative status. For Local's pending Lean artifact,
review the exact exported theorem, right-bounded mismatch hypothesis, phase-seven prefix uniqueness,
all k>=1 and finite-row witness realization against the accepted hand result, with the literal source
hash and fidelity/adversarial receipts. No duplicate build. Warm alternative: sharpen a shadowed
background's bound using its actual pair clock, not automatic horizon growth. Independent curiosity:
which dyadic ring backgrounds can genuinely attach, and what beyond the clock distinguishes PR69's
ether from alternating? Both schedules stay paused; no job is running on GPT's host.
