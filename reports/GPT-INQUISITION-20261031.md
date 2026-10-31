# GPT's carrying read and continuation of the October 31 inquisition

Owner-authorized bounded block, beginning 15:11 UTC. Both recurring schedules remain paused; Local is stopped.
The handover is [L1257](HANDOVER-GPT-20261031.md), with its [complete tracker](inquisition-20261031.md).

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

**The first 2058 timer is already demonstrated.** The delivered
[nested essay](wolfram-agents/submissions/gate-clocks-nested/essay-prose.md) explicitly exhibits the first 20 layers:
11,10,11 followed by seven 01 pairs, with K=2 and M=8. GC2322 carried its executed notebook. Do not rerun the
handover's proposed first-stage test. Symbolic completion of the second timer remains a genuine open target.

## What the left-diagonal change of coordinates does to the wall

Write x_j(t) for the physical left half, with x_0(t)=0 imposed, and
L_k(t)=x_(k-t)(t), for k<=t. Then

    L_k(t+1) = L_(k-2)(t) XOR (L_(k-1)(t) OR L_k(t))   (k <= t),
    L_(t+1)(t+1) = 0.

The two free coordinate lines can be taken at k=-1 and k=0 (a shifted version of Local's bijection). Their backward
cones use only the initial left half, so later wall forcing does not change them. But the required clock is
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

**Pull:** the PR69 proof transports a local pair invariant to the edge, so it should also bound how long the pattern
can imitate an unattached ether. **Cheap objection:** its published eventual statement hides the ticks discarded
at each descent. **Discriminating test:** derive the exact phase-dependent dependencies, including the one backward
time dependency, then bound the resulting finite proof tree. This is an application of Lowry's invariant. No
first-in-literature or submission claim is made. Searches covered `grounding`, `ether pair`, the current kit and
equivalents/catalogues, portal source, actual PR69 head/discussion/reviews, and primary-source web queries. No
negative keyword search is used as novelty evidence.

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
There is no claim of sharpness. The statement concerns fixed offsets behind a moving black edge, not Q01's fixed
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

## Frozen finite self-check (not yet run at freeze)

One pilot will check the eight dependency implications by exhaustive local assignments, all 17 potential
inequalities, the boundary positive control, and every initial black-edge prefix through depth 9 against the
claimed finite bound for k=0..8. A literal physical Rule 30 implementation is an independent implementation
control for the edge map. The false stronger claim of immediate incompatibility must be rejected. This is a
finite self-check of a hand claim, not its independent carrying read or a proof for arbitrary depth.

The source/hash, exact command and stage caps are recorded in the ledger freeze before execution. No longer
horizon or automatic retry is authorized by this pilot. Results and next executable step will be appended here.
