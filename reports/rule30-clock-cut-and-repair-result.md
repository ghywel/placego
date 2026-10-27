# A real one-beat repair, followed by an unavoidable failure

GC1940 / MI859 / DQ-023, 27 October 2026. COMPUTED with two implementation
controls and a hand explanation; Local L1003 independently carries the frozen source and diagnostic; completed outcomes remain pending Local review.
[Preregistered plan](rule30-clock-cut-and-repair-plan.md).

## What the test answered

**Question:** can changing the actual right starting row compensate for cutting
the clock's infinite left support, without spoiling an earlier beat?

**Response:** yes in one declared case. Keeping left depths through21, flipping
right positions10 and12 delays the first failure from time22 to time23. Both
bits were initially0 and become1. Either flip on its own leaves failure at22.
All centre values through time22 agree with the required1010 sequence.

**Challenge:** this is a one-beat compensation, not a surviving wheel. At time22
the repaired centre is1 and its left neighbour is0. Rule30 then forces the next
centre to1 regardless of the right side; the required next value is0. The
left diagnostic proves this deadline for **every** right starting row with this
fixed left initial condition, provided the earlier clock beats are preserved.

**Better question:** in the cut23 case the left side permits repair until at
most time33, but the declared right edits cannot repair the failure at28.
Which required right-neighbour history is incompatible with these edits? Can
Local derive a short constraint distinguishing a genuinely impossible right
completion from this small edit family's inability to supply it? Work on that
compatibility by hand before proposing another numerical domain.

## Full declared outcome

Time0 is the initial row. d is the first missed beat with unchanged right;
H is the first unavoidable deadline from the clamped-left diagnostic. This
diagnostic supplies a bound, not the actual natural evolution used in cases.

| Left cut | d | H | Natural candidate rows tested | Repairs beyond d | Best first failure |
|---|---:|---:|---:|---:|---:|
| 14 | 15 | 15 | 0; analytically excluded | 0 | baseline15 |
| 15 | 16 | 17 | 191 | 0 | 16 |
| 16 | 21 | 21 | 0; analytically excluded | 0 | baseline21 |
| 21 | 22 | 23 | 191 | 1 | 23 |
| 22 | 23 | 23 | 0; analytically excluded | 0 | baseline23 |
| 23 | 28 | 33 | 191 | 0 | 28 |

573 declared intervention cases, plus the reference/baseline/diagnostic controls.
Prediction P held. No case was censored at256. Three cuts needed no intervention
search because H=d already excludes every right completion. The counts are exact
for the specified cases, not population frequencies or probabilities of survival.

All failure-time histograms, including unchanged rows:

- cut15: 2:37, 6:34, 10:40, 14:11, 16:69.
- cut21: 2:37, 6:34, 10:40, 14:11, 18:1, 22:67, 23:1.
- cut23: 2:37, 6:34, 10:40, 14:11, 18:1, 22:1, 28:67.

Unexpected transfer check from the same table: the successful pair10/12 does
nothing useful at cut15 (failure16) and makes cut23 worse (failure22 instead of28).
The three excluded cuts admit no improvement by the hand deadline, so no extra
runs were used to test the pair there. This is phase-dependent compatibility,
not a universally beneficial edit or a transferable repair mechanism.

## The repaired beat, in three cells

The retained windows show these (left, centre, right) triples:

| Time | Unchanged right | Flips10/12 |
|---|---|---|
| 20 | 110 | 110 |
| 21 | 101 | 100 |
| 22 | 001 | 011 |

At time21 the centre is0 and the left cell is1. Unchanged right1 produces
1 XOR (0 OR 1) = 0, missing the required1. Edited right0 produces
1 XOR (0 OR 0) = 1, repairing that beat. At time22, repaired011 produces
0 XOR (1 OR 1) = 1 and misses the required0. Thus the failure explanation is
an exact local calculation, not an inference from the lifetime histogram.

The two single-edit cases both have101 at time21. Their combined effect at this
cell is therefore non-additive. This is a concrete instance of the owner's
compatibility intuition; it does not establish a general theory from that analogy.
Also, the repaired white-phase support is10, not01: do not call this a newly
created left0/right1 handover or claim it sustains the infinite sequence of such
handovers required by GC1937.

## Controls, provenance and actual resource evidence

Frozen source: commit010fe86b1871dd8cdea63ed323679cc9354030ba,
`tests/probes/wolfram/clock_cut_repair_intel.py`, SHA256
`78fc320f7ee0a1ad6cb93b41421b1e1455f1a837b2f1b6432ee49e7fbe3c9f74`.
The CPU inheritance correction was committed at34e789bf before any numerical
case ran. First launch refused in preexec_fn; zero numerical output. Both
attempts are retained. This was an implementation error in launching, not a
failed mathematical prediction, and no numerical stage was automatically rerun.

Literal truth-table/scalar and packed-XOR engines agree on every retained
radius4 local history and all first-failure labels. All eight local inputs,
external ether coordinate conversion, six predicted baseline failures, H>=d,
every candidate failure<=H, reference clock through256, and the duplicate
cuts16..20 instrument control pass. Zero boundaries are288 cells away, beyond
the256-step observation cone plus radius4; no periodic wrapping. Full local
histories include every earlier handover, not just the best case.

One computational process/thread. Actual child0.53s wall,0.50s user+0.02s system;
supervisor receipt1.05s wall and0.134s own CPU. Child max RSS14,020,608bytes
(about13.4MiB), as reported by time-l; not system peak memory. Completed final
artifact directory149,463bytes including the completed launcher receipt.
Launch free+inactive4769MiB (proxy), OS pressure normal. The run ended before
the supervisor's first one-second sample: its sampled RSS/disk maxima of0 mean
**no sample**, not zero consumption. No continuous system pressure/RSS peak is
claimed. Post-run disk check passed. Kernel CPU/file limits applied as described
in the execution amendment; aggregate CPU is not an atomic process-tree cap.
Legacy merge startup remains capped/incomplete, not a pass.

Evidence retained and byte-for-byte read back under
`cited/gc1940-clock-repair/manifest.json`. Result SHA256
`a43067ee892cef57fdb4a1aa509518ec22ea91034acbc49a1f7dffdbd195ffbd`;
all573 rows SHA256
`f4064bbd95982c0b572f07569b2f8e6d8c9bc5d77c7dd239e500b7fed056aeb7`.
No data added to git. No external submission: this finite intervention is not
a new universal proof or a counterexample to the single-seed prize problem.

Reasoned verdict: a successful finite compensation with a sharp stopping
explanation; retain the cut23 compatibility question for hand review. Gut:
encouraged by a real causal repair, checked by its very limited duration and
failed transfer. The programme remains active under the owner's restart;
there is no authorization to expand or rerun this completed stage automatically.


## L1003 received during publication

Local's independent source read at010fe86b and separate reference/deadline replay
agree with this stage; adopted for source correctness, not for unreviewed outcomes.
Its proposed white-phase filter passes on retained data: the repaired site1 first
differs from baseline at t21=d−1, with no earlier white-tick difference. A wording
qualification: the general black-tick masking argument forbids earlier differences
at **white ticks**, not all earlier times. It does not by itself exclude a masked
black-tick difference that disappears before a white tick. The actual successful
pair happens to pass the stronger statement too. H is a universal upper bound,
not automatically an attained first-failure time for arbitrary right rows.


## GC1941 supersedes the proposed cut23 follow-up

The apparent window closes for every right completion by the known no11 gate
rule. Required right1 at25 and27 is impossible; cut15 closes analogously.
See [the hand application](rule30-clock-repair-right-obstruction.md). Original
measurements and their preregistered scope remain unchanged. This cheap right
screen should have preceded the search, alongside the left-only deadline.
