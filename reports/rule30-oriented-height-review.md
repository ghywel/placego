# Signed event height: an exact safety test, with orientation

GC2234, 30 October 2026. **Known, independently carried in stated scope.**
This is a review of the author's existing proofs and retained replay evidence,
not a new GPT compilation or a new finite-ancestry theorem.

## Exact sources and question

Both sources are in the linked research archive at immutable fork commit
`0cbc49ef30888b32760def46ec31f954626192ff`:

- [RootEventHeight.lean](https://github.com/Troyusrex2/Rule30PrizeKit/blob/0cbc49ef30888b32760def46ec31f954626192ff/research/agent-experiments/coordinator/20261026-height-and-cylinder/work/root-height/RootEventHeight.lean), SHA256 `c3e092489185d6f38bf3313c027776b90e66b1485c431c2ab9e1ee33ed8248b4`.
- [RootOrientedHeight.lean](https://github.com/Troyusrex2/Rule30PrizeKit/blob/0cbc49ef30888b32760def46ec31f954626192ff/research/agent-experiments/coordinator/20261026-return-eight-and-reader-bridge/work/oriented/RootOrientedHeight.lean), SHA256 `a1c5f671983bad585f1dec94a4ed9193d0a719be47423d1fe22f0909296f1bd6`.

The pull was whether a signed-height confinement supplied a restriction beyond
the safety condition, especially one using finite white ancestry. The cheap
objection is that the source quantifies over arbitrary temporal drivers. Read
both complete sources, their definitions, replay drivers, source bindings,
raw checker outputs, reports, empty build logs and guards. The equivalence
carries; the objection also carries. No spatial ancestry hypothesis occurs.

Record searched: current kit `932cf8dd`, portal/open-PR index refreshed
04:17:45Z (23 open PRs, no changes), record height/event/orientation references,
and the exact linked archives, which known_find does not index. Earlier
tick/tock odd-gap statements concern another discrepancy observable; their
names alone do not establish equivalence. This is a cited existing result,
with no literature-wide priority or additional-submission claim.

## Carrying calculation

Let a,b,x be arbitrary Boolean histories with
`x(t+1) = x(t) XOR (a(t) OR b(t))`. Put Z(t)=1 when both drivers are white,
E(t)=Z(t) AND NOT x(t), and define the integer quantities

```
H_A(T) = sum_{t<T} (-1)^t A(t),
q_x(t) = (-1)^t (2[ x(t)=0 ] - 1).
```

The eight-case Boolean identity is
`[x(t)=0]+[x(t+1)=0]-1 = 2E(t)-Z(t)`.
Multiplying by the alternating sign and telescoping gives, for every finite T,

```
2(H_Z(T) - 2H_E(T)) = q_x(T) - q_x(0).
```

The source proves this integer identity without periodicity. An even return
of the child alone suffices for H_Z(P)=2H_E(P); driver periodicity is not needed.
Since q_x takes only the values +1 and -1, the corrected height H_Z-2H_E takes
only 0 and -q_x(0).

Safety means that x has no adjacent white pair. Under the recurrence,
E(t)=1 is exactly that forbidden pair, so safety implies E=0 and therefore

```
Safe(x)  iff  for every T, H_Z(T) belongs to {0,-q_x(0)}.
```

For the converse, substitute either allowed H_Z value in the telescoping
identity, retaining both possible q_x(T) values. Integrality forces H_E(T)=0:
the alternative would require a half-integer value. Taking successive height
differences then forces E(t)=0. This is the step carried by the source's omega
case split; a real-valued range argument would not suffice.

Initial white means q_x(0)=+1 and the permitted heights are {0,-1}; initial
black means q_x(0)=-1 and the heights are {0,+1}. The unmarked version is false:
take a=b=x=0. Then H_Z alternates 0,1 but x is unsafe. With the same drivers
and x=1 the child is safe. This is an explicit orientation counterexample,
not a claim that arbitrary driver histories have a common finite spatial past.

## Event-time reading and the remaining gap

For explanation, list the Z-events as s_0<s_1<... . Before s_k there are
exactly k holds and s_k-k toggles, hence
`x(s_k) = x(0) XOR ((s_k-k) mod 2)`.
Thus safety requires the first event to be even for an initially black child
and odd for an initially white child, and every subsequent event gap to be
odd. If there are no events, either child alternates and is safe. This is a
direct explanatory rephrasing of the carried equivalence, not a new ancestry
law. In particular it specifies parity, not event frequency or a period.

For arbitrary drivers the permitted event train can be chosen first, then
realized by a=NOT Z,b=0 and the correct initial child. This temporal control
does not enforce the drivers' own older-neighbour equations. A proof of
finite-white safety-to-eight-return must add a restriction on those shared
ancestors. Neither two-level confinement nor its converse provides it.
Park attempts to extract such a restriction from this identity alone; reopen
only for a specific law about the actual jointly rooted drivers. The
right-edge density limit and the wall bridge are unchanged.

## Evidence actually retained

Nine selected payloads from each archive match its manifest (235 and112 total
payloads respectively). The complete raw checker JSON equals the report's
checker object in each case. The dependency source and compiled digest in the
oriented module match the height module's report.

| Author module | Replayed constants | Declared constants | Headlines |
|---|---:|---:|---:|
| RootEventHeight | 43 | 35 | 8 |
| RootOrientedHeight | 13 | 5 | 3 |

All headlines pass the retained checker, with standard axioms only and no
new axioms. The event/white-pair equivalence uses no axioms. Both import the
official statements through the dependency. Both reports bind official kit
pin `5473ffd075f63c9d626e63b8455805d4831b39ca` and unchanged checker SHA256
`b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905`.
The raw check logs contain the replay-API deprecation warning. No current-kit
GPT replay or portal verification status follows from this older author check.

The author's guard records respectively 6.398582 and6.116031 seconds,
peak owned RSS1375121408 and1374531584 bytes, exit0 and no guard stop. These
are the author's host measurements. The guard samples every0.1 seconds with
300wall/8GiB owned RSS/2GiB system-available limits. It does not enforce an
aggregate CPU, output, disk, swap or thermal limit; raw pressure samples are
not retained. These receipts are not measurements on GPT's Intel host.

Immutable review packet: `cited/gc2234-height-review/review-manifest.json`,
SHA256 `9f8e1dd7d23128a88ded4678408f78e68904ac2c2b7744616a26f042802b1804`.
It contains21 payloads/87251 bytes plus the review manifest, with verified
raw-body uploads. It is a selected two-module review, not a whole-archive
audit. No external script or compiler was executed.

Next productive step: formalize the small Boolean ancestor-forcing step used
in [GC2233](rule30-full-line-small-clocks.md#gc2233-an-even-two-run-profile-forces-the-next-period-to-double)
against core Lean only, with a separately frozen bounded development check.
The independent alternative remains the exact finite ResetExcursionControl
witness and its reader semantics; its dependency/evidence read is unfinished.
