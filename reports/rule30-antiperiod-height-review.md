# Antiperiodic drivers: the height obstruction and its free-partner converse

GC2242–GC2243, 30 October2026. The external necessary theorem is independently
carried in scope. The constructive converse and controls are **PROOF-SKETCH,
solo GPT**, pending an independent carrying read. No trajectory search or
external compiler ran in this block.

## GC2242: the exact existing necessary condition

Complete source:
[RootAntiPeriodHeight.lean](https://github.com/Troyusrex2/Rule30PrizeKit/blob/0cbc49ef30888b32760def46ec31f954626192ff/research/agent-experiments/coordinator/20261026-height-and-cylinder/work/root-height/RootAntiPeriodHeight.lean),
SHA256 `513de31a591d3fa7afbeb69e4ac8a3967718a1ba8ced6df39a4ba2039083ed57`.
Its dependency RootEventHeight has the exact c3e09248 source already carried
in GC2234; the retained source/report binding matches again.

Let P>0 be even, b(t+P)=b(t), c(t+P)=NOT c(t), and
d(t+1)=d(t) XOR(b(t) OR c(t)). Safe means that d never has two consecutive
white cells. Write A=NOT b, Z=NOT b AND NOT c, and
H_X(T)=sum over t<T of (-1)^t X(t), with Boolean bits interpreted as integers.
The source proves:

```
H_A(T) = H_Z(T) + H_Z(T+P) - H_Z(P).
Safe(d) implies H_A(P)=0 and |H_A(T)-H_A(S)|<=2 for all S,T.
```

P is a returning period, not necessarily a least period or a power of two.
The hypotheses do not impose the actual recurrence between b and c, nor
finite white ancestry. This is a necessary condition for a specified pair
of drivers and a specified child; no sufficiency is asserted in that source.

The carrying steps are short and exact. Antiperiodicity partitions the
white ticks of b between Z(t) and Z(t+P). Since P is even the two signed
weights have the same sign, giving the first identity, including its prefix
offset. Safe d puts H_Z in the single oriented pair {0,-q(d,0)}, by GC2234.
Every difference of two such heights is in [-1,1], so the sum of the two
shifted differences is in [-2,2]. Finally H_A(3P)=3H_A(P); the bounded
integer difference forces H_A(P)=0. The proof never needs a safety converse
or a count/frequency premise.

Raw evidence:26 replayed constants,12 declared constants, six exact headline
types, all standard propext/Classical.choice/Quot.sound, no new axioms,
required statement import, partial pass. Raw checker JSON equals the report.
Author compiled digest
`745e714a6054c7f9b2703eaf295a205480224cb14a526514ab28b2997b746321`;
official pin5473ffd0 and checkerb882f252 match the other retained height
records. Author compile3.6510182s/total6.0986038s; guard6.1969036s,
1375985664bytes owned RSS,43203649536bytes minimum available, exit0/no stop.
The300s/8GiB RSS/2GiB available guard and0.1s sampling were read. No aggregate
CPU, disk/output, swap or thermal enforcement or raw sample series is
inferred. No GPT replay or live portal status is asserted.

Twelve selected author payloads match the112-entry archive. The adjacent
CedarD3Converse statement was read to disambiguate its name: it equates two
open finite-word completeness statements, not the height converse below.
Its imported certificate chain is not newly accepted here.

Shared-store packet `cited/gc2242-antiperiod-height/review-manifest.json`,
SHA256 `eb83f9ea79ef7e5b388cf15417829a76dab57041e287addf69aac2c1ff5cba01`:
14payloads53261bytes plus manifest,15 verified raw uploads. Selected evidence
review only, not a full112-entry archive audit.

## Two hand controls: sharpness and the quantifier on the partner

Take P=6 and repeat b=010010. Its white indicator A=101101 has prefix heights

```
0,1,1,2,1,1,0.
```

Thus the necessary height diameter is exactly2. Take c=001001110110,
repeated with period12; the second half complements the first. Its joint
white-event word is Z=100100001001. From initial d(0)=1 the child is
d=110110101101, repeating with period12 and with no00. These strings directly
attain the bound. They are arbitrary temporal drivers: b contains cyclic
00100, forbidden by G258 for an actual profile. No rooted realization is
provided.

Keep b fixed but choose c=000000111111. This also is6-antiperiodic and b
still passes the same height test. If d(0)=0, then d(1)=0. If d(0)=1, then
d(2)=d(3)=0. No initial colour is safe for this specified partner. Hence
the height test cannot be sufficient for every given c. The meaningful
remaining question is existence of a suitable freely chosen c.

## GC2243: existence of a free antiperiodic partner is exactly the height test

**Claim, solo PROOF-SKETCH.** Fix any positive even returning period P and
any P-periodic Boolean b. There exists a P-antiperiodic Boolean c and a safe
child d obeying the single displayed recurrence if and only if

```
H_A(P)=0 and max(H_A)-min(H_A)<=2, where A=NOT b.
```

Zero drift and even P make H_A itself P-periodic, by the carried
height_period_add identity. Thus the extrema may be taken over one P-block
including its endpoint. In the forward direction the carried theorem applies. In the reverse direction
the construction also makes d2P-periodic, not necessarily of least period2P.
There is no recurrence requirement between b and c, or older ancestry.

The pull is to regard the bounded integer height as the sum of two binary
paths. The cheap objection is endpoint orientation: after P ticks the two
paths must exchange their endpoint values so they can be concatenated.
That issue is settled explicitly, rather than assumed from a height bound.

### Lift a three-level walk to two binary paths

Let h(t)=H_A(t) for0<=t<=P; h(0)=h(P)=0. Its steps are
h(t+1)-h(t)=(-1)^t A(t). Choose a sign e in {1,-1} and a in {0,1} so that
S(t)=e*h(t)+a always belongs to {0,1,2}:

- If h is nonnegative, choose e=1,a=0.
- If h is nonpositive, choose e=-1,a=0 (either choice handles h identically0).
- Otherwise its minimum and maximum are -1 and1; choose e=1,a=1.

Lift S to two binary paths z,w with z+w=S. At a nonzero step of S change
exactly one of the two bits in that same direction; at a zero step change
neither. Such a move is always possible at levels0,1,2. Start with
(z(0),w(0))=(0,a). We can arrange the final pair to be (a,0):

- For a=0, total S(P)=0 already forces both bits to be0.
- For a=1, h is nonconstant. Ignore zero steps and take the first excursion
  from total1 back to total1. It is1,0,1 or1,2,1. In the first case remove
  the initially occupied bit, then fill the other; in the second fill the
  initially empty bit, then remove the other. Either exchanges the labels.
  On every later excursion use the same bit for the outward and return
  moves, preserving the exchanged labels. Thus the endpoint is (1,0).

An excursion cannot move through level0 or2 to any other level before
returning to1, so this construction covers every finite walk. No fairness,
probability or asymptotic argument is involved.

### Concatenate, then choose the partner

Define K over0..2P by following z for the first P ticks and w for the next
P ticks. The endpoint conditions z(P)=w(0)=a and w(P)=z(0)=0 make K a
well-defined2P-periodic binary path starting at0.

For0<=t<P, let Z(t) mark whether z changes at that tick. Since only one
track changes when A(t)=1, the change of w is marked by A(t)-Z(t). Define
Z(t+P)=A(t)-Z(t), and repeat with period2P. Evenness of P gives

```
K(t+1)-K(t) = e*(-1)^t Z(t),
H_Z(T) = e*K(T), for every nonnegative T.
```

In particular Z<=A and its signed height is always in {0,e}. On the first
half choose c(t)=1-Z(t) wherever b(t)=0, and choose c(t)=0 wherever b(t)=1.
Set c(t+P)=1-c(t), then repeat. At a white tick of b, the second half's joint
white event is1-Z(t)=A(t)-Z(t); at a black tick neither half has a joint
white event. Thus the constructed Z is exactly NOT b AND NOT c.

Start d black for e=1 and white for e=-1. Then -q(d,0)=e. The already
carried oriented-height equivalence GC2234 applies to the recursively
defined child and shows it is safe, since H_Z always lies in {0,e}.

Finally, the number of joint white events in a2P-block equals the number
of white ticks of b in a P-block. Zero signed drift means equal even- and
odd-position white counts, so this number is even. The OR forcing over2P
therefore also has even weight. XOR accumulation gives d(t+2P)=d(t).
This proves existence and the stated returning period, without a least-period
claim.

## Searches, disposition and next discriminating check

Record searched: GC2234's complete oriented equivalence; the exact
RootAntiPeriodHeight source/report above; GC2239's missing shared-profile
compatibility control; current record and known-index queries for the named
height theorem; actual kit lean/equivalents searches for the signed-height
and antiperiod-height expressions. The last complete portal/kit refresh is
04:53:47Z at932cf8dd,23 open PRs. The linked archive explicitly states only
necessity. CedarD3Converse concerns a different finite-word quantifier.
A bounded primary-source web search for the exact antiperiod/signed-height
terms returned no source; that negative search supplies no novelty evidence.
The construction is elementary binary-path lifting; no priority or submission
claim is made.

The distinction this settles is mathematical: for a freely chosen partner,
the projected height information is enough; for a prescribed partner or a
shared Rule30 ancestry, it is not. Do not promote this to finite-white safety
completeness, a root-density bound or an obstruction to an actual00 pair.

Next executable step: write the two-track constructor with its endpoint
exchange explicit, and compare its outputs against independent exhaustive
partner/initial-colour existence at fixed P=2,4,6 only. Predict exact
equivalence with the finite height test. Include nonnegative, nonpositive,
and mixed-sign height paths, the identically-zero path and both P6 controls.
Freeze source, counters and conservative pilot limits before any run; no
larger period or automatic repetition. Independent alternative remains a
scoped source read of RootD3Reduction/CedarD3Converse's actual completeness
interface, not an assumption that either open statement is proved.


## GC2244: one fixed constructor-versus-existence pilot

The [pilot source](../tests/probes/rule30_free_partner_pilot.py) is frozen at
SHA256 `b6db991d88b2d4fbf44b84c6eda2fb8197f5aa36843a73abb94e1278dbc2109e`;
run_capped stays
`c8c58b49e032fc4c20b61675adc4194646713e692a51815996791ac8943ffc56`.
Source has been read and syntax parsed, but not executed at this freeze.

**Prediction:** the height criterion, explicit binary-track construction and
independent existence oracle agree for every driver at P=2,4,6. Every
constructed partner is P-antiperiodic and its chosen child is safe and returns
after2P. This tests the construction and its indexing, not the infinite
statement or rooted occurrence. **Counterfactual:** any mismatch, unsafe
constructed child, missing endpoint exchange, absent coverage/control,
resource/monitor failure or input mismatch stops the stage. No automatic
repair, repeat or larger period.

Exactly84 drivers,2^P partners per driver and both initial colours give
8736 partner/initial cases. No early termination of the outer enumeration.
The oracle uses the literal eight-entry Rule30 table and detects cycles in
(phase modulo2P,child colour), at most4P updates per case; no height or track
logic enters its existence decision. These are only fixed small-period
controls, not a seed census or an attempt to infer density.

Independent controls: the retained P6 sharpness trace and the prescribed bad
partner are checked exactly. **Unexpected/mutation check:** deliberately
omit the endpoint exchange for b=100100; the track endpoints must fail and
neither child initial colour may be safe for that mutant's partner. Correct
constructions must include zero, nonnegative, nonpositive and mixed-sign
height cases. The drift/diameter theorem's necessity is already the carried
external result; finite agreement is not its replacement.

Record searched: GC2242/GC2243's exact external513de31a necessity source,
GC2234 oriented converse, adjacent CedarD3Converse's different quantifier,
and the actual kit932cf8dd/23PR/portal snapshot completed04:53:47Z. The prior
bounded primary-source search is recorded above. This is validation of the
written sketch, not a new novelty decision or a search-silence claim.

ONE run after this freeze is pushed. Single Python process, one thread,
nice10, no subprocesses, no GPU or concurrent heavy job. Kernel-enforced
60CPU seconds for the sole computation process, below the120aggregate pilot
ceiling; actual process/supervisor CPU separately retained. Per-process
limits are not described as aggregate tree metering. Outer300wall,
768MiB owned-tree RSS,max2processes (time plus Python),16MiB/file,
128MiB/stage,4096MiB launch and3072MiB running free+inactive,64MiB swap
growth. Tree/monitor failure stops and cleanup checks remain active.

Intel preflight05:30:17Z:6236MiB free+inactive,193.25MiB swap, load2.08;
no existing compute process. pmset reports no recorded thermal/performance
warning and scheduler/speed limits100. This is warning-status evidence, not
continuous temperature monitoring. Retain a completion warning/process
snapshot, source, full84-row outcome, controls, time/pressure/cleanup and
limit receipts. A warning redirects later work to light reasoning. No
post-freeze cap increase or extra period is authorized by this stage.


## GC2245: the fixed pilot passes once

Freeze5c5fd4fd/sourceb6db991d ran once at05:31:37Z, COMPLETED rc0. All84
height/construction/existence decisions agree across8736 partner/initial
cases and61642 literal updates. Accepted-driver counts at P2,4,6 are2,6,20.
All28 accepted drivers receive safe constructed children returning after2P.
Their height categories are18 nonnegative,5 nonpositive,2 mixed and3 zero.
The two retained P6 controls pass. Without the endpoint exchange, the mixed
control ends its tracks at0,1 instead of1,0; the two child starts fail at
indices4and7. No larger period, repeated dynamics or seed search ran.

This finite check tests the construction including its mixed-sign boundary.
It does not prove the universal claim. In particular, these small periods
cannot expose every possible height-range obstruction; the necessity proof
remains the separately carried external theorem, not a fitted count pattern.

Actual Intel receipts: computation0.022510s wall, process0.070153CPU seconds;
outer0.54s wall and0.138 supervisorCPU. The separate time receipt gives
0.07real,0.06user/0.01system and14635008bytes maximum RSS. Kernel60CPU and
16MiB file limits were read back exactly. Launch6242MiB free+inactive;
the job completed before the first0.5s monitor sample. Therefore sampled
RSS/proc zeros and an empty pressure series do not mean zero memory usage
or a measured running minimum. Completion6252MiB/swap193.25MiB, no compute
process and no recorded thermal/performance warning. No continuous thermal
claim; original receipts and the empty sample series are preserved.

Shared-store `cited/gc2245-free-partner-pilot/manifest.json`, SHA256
`6254e7bb89e8a905f80389150fbd18dbeebf86472c3fd9e513fb418b0bc675ef`:
11payloads81339bytes plus manifest,12 verified raw uploads. Full84-row
results SHA256 `0b35dd6067c68be374bc42fbf6d18664bf917bce74c7444d122ae59d26a544af`.
The stage is consumed; no repeat or extension is queued.

## GC2246: count all free partners by excursion choices

**PROOF-SKETCH, solo GPT.** Fix the phase of b and P; count pairs consisting
of a P-bit first half of c and the initial colour of its child. The second
half of c is forced by antiperiodicity. These are distinct phase-anchored
words, with no quotient by rotations or by least periods.

Let h=H_not_b, D=max(h)-min(h) over0..P, and n be the number of white ticks
of b in a P-block. If h(P) is nonzero or D>2, the carried necessary theorem
gives zero safe pairs. Otherwise n=2k is even. The exact count is

```
n=0:             2^(P+1),
n>0 and D=1:     2^(P-k+1),
n>0 and D=2:     2^(P-k).
```

No other D occurs when n>0 under the criterion. This is a refinement of the
free-partner construction, not a new restriction on actual older profiles.

### Why the lift counts all choices

For a safe pair choose e=-q(d,0) and a=e*H_Z(P), so a is0or1. The two tracks
are uniquely recovered as z(t)=e*H_Z(t) and w(t)=e*H_Z(t+P). The paired-height
identity gives z+w=e*h+a. They start at(0,a) and end at(a,0), because zero
drift gives H_Z(2P)=0. Each white tick of b changes exactly one track, and
all other ticks change neither. Conversely every such lift gives precisely
the white-tick values of c and the specified safe initial colour, by GC2243.
Thus the correspondence is bijective on white ticks. At each of the P-2k
black ticks, the first-half value of c is free and invisible to the child;
its complement in the second half is then fixed. This multiplies the count
by2^(P-2k).

Discard zero steps of the total walk S=e*h+a. Its2k steps alternate between
level1 and the boundary levels0or2. If a=0, every departure from a boundary
into level1 has two possible track labels, independently; the k choices
always finish at(0,0). There are2^k lifts.

If a=1, the walk has k excursions from level1 back to level1. Each excursion
may preserve or exchange the two labels. Ending at(1,0) from(0,1) requires
an odd number of exchanges. For k>0, exactly2^(k-1) label-choice sequences
have that parity. This includes all tracks, rather than only the one chosen
by the constructor's first-excursion rule.

For D=1, h has range[0,1] or[-1,0]. Exactly one orientation/offset pair has
a=0 and two have a=1. The total lift count is
2^k+2*2^(k-1)=2^(k+1). For D=2 with0 at an endpoint of h's range, exactly
one pair has a=0, giving2^k. For D=2 with range[-1,1], both orientations
have a=1, again giving2*2^(k-1)=2^k. Multiplying by the free black-tick factor
proves the two nonzero-n formulas. If n=0, b is constantly black: both child
starts alternate safely for every one of the2^P partners, giving2^(P+1).

For n>0 each admissible partner has only one safe child start. If both
complementary child histories were safe, neither could contain00or11, so
both would alternate. That forces Z identically0, contradicting
Z(t)+Z(t+P)=NOT b(t). Thus in this case the displayed pair count is also
the number of admissible partner words.

### Retained-data prediction before checking counts

Record searched: the exact GC2242 necessary source and GC2234 oriented
converse, GC2243's construction, and current record/kit/portal searches for
partner counting and binary tracks. The elementary excursion/parity method
is credited as such; no priority claim or additional literature clearance
is asserted. The complete paired-height statement is the primary source
used, with its arbitrary-driver scope preserved.

Prediction, written before reading the retained per-driver success counts:
all84 oracle_safe_initial_cases fields equal the displayed formula. Specific
controls: P6 b010010 and b100100 each give16; b000000 gives16; b111111
gives128. Counterfactual: any disagreement rejects this counting sketch
pending an exact diagnosis; do not rerun the trajectory pilot or widen P.
The comparison uses only the already-retained84 JSON rows and their digest,
with integer arithmetic; no new dynamics, compiler or substantial run.


The retained-data comparison PASSED all84 counts, including the four named
P6 predictions16,16,16,128. It executed only integer arithmetic on the
existing JSON, after checking its exact SHA256; no trajectories were rerun.
Audit `cited/gc2246-free-partner-count/manifest.json`, SHA256
`66e7d4ec437dce476bf30fdc574fd4657828a5d23521348d2b3a31a8376639a4`,
two payloads15352bytes plus manifest, three verified raw uploads. The
universal bijection/count argument still needs an independent carrying read.

Next pull: count the admissible phase-anchored driver words themselves, not
just their partners. Pairing one even and one odd tick suggests finite walk
matrices M1=[[2,1],[1,1]] and M2=[[2,1,0],[1,2,1],[0,1,1]]. Test by hand
whether the exact count at P=2m is trace(M2^m)-trace(M1^m), carefully handling
which height intervals contain the initial0 and overlap. This would describe
how restrictive the free-partner language is among all periodic drivers;
it would say nothing about the actual root's sampling of those drivers.
Search the record/current sources and standard bounded-walk prior art first.
Use the retained2,6,20 counts as scope controls only; no new enumeration,
larger pilot or inferred root density is queued.
