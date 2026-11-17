# E A⁴ E, the measured transient, and the generated continuation — GC2774

GPT, 9 November 2026. Owner requests CL756/CL757 review and continuation,
considering Cloud's E A⁴ E pull and then the E-hazard decay law. Main
818b68f0 and the new addressed flag were read. Cloud's complete report,
producer, detectors, tables and JSONs were read; its immutable archive is
15,758 bytes, SHA256
`41dfcc828f6d4732639978a1697bfe0fbd693825f2cdc17921ac593c3ac38bfd`,
verified against the raw shared-store response. This is a source/data
review, not an independent rerun of the millions of rows. GC2773's requested
hand carry remains pending: CL756 acknowledges it but explicitly defers it.
Schedules remain paused; no portal submission or hours-long solver is begun.

## Review: retain the observations, correct their scope

Cloud's detector really checks every intervening A template, not just the
separation of two E starts. The reported 5 returns therefore are genuine
finite detector matches, though their particular roots were not retained.
The zero counts for 4 and 6 are finite observations at the declared supports
and horizons, not exclusions for arbitrary rows.

Several quantitative and interpretative corrections are needed:

- E A⁴ E has 96 sampled **intervals**, 97 samples, at odd ticks 1..193.
  The free row at tick 1 needs 193 cells. Our anchored tick-0 formulation
  also requires the black-center predecessor and needs 194 root cells.
  Likewise the full passage uses 359 free tick-1 cells versus 360 anchored
  tick-0 cells. A free-row positive is not automatically an anchored one.
- The exhaustive JSON contains return 115 once at support 19 and once at
  support 20. Thus the observed range extends to 115, and it is a sparse
  set of counts, not every integer from 7 to 114.
- The support-30 long run has 1,532 E launches, including 1,529 in its first
  ten 200-tick bins and three later. This agrees with 1,530 single-E rows
  and one double-E row. The report's 1,526 is an arithmetic error.
- At horizon T, a complete E can only be detected if its start is at most
  T−68. The 8,001-tick run observes starts only through 7,933, not 8,001.
- A suffix that has period 2, 5 or 7 for ten observed periods is a finite
  suffix match. It neither certifies permanent locking nor proves that a
  nonmatching row is aperiodic. Early matches are still candidates; late
  matches have not been proved noise. The 4,001- and 8,001-tick random runs
  use different seeds/cohorts, so they do not track the same rows unlocking.
- The histogram measures event counts. It does not supply a conditional
  hazard or a universal decay law. Its successive ratios are not a constant
  factor of four. Support independence, eventual absence, and a universal
  transient do not follow from these finite counts or the fitted maxima.
- Generic E detection does not check membership in the X component or its
  A-context. A row with an observed E A⁵ E need not be a play in X. Neither
  the X grammar nor its conditional clock can be applied to it without
  that hypothesis.

The kit's `Rule30PeriodTwoWidth13.RD` makes a relevant distinction explicit:
entry into the gate trap **or** eventual periodicity of sampled column 1.
Cloud's suffix detector measures neither trap entry nor this disjunction.
The existing census classified gate-trap entry separately from periodic
locks (L1569); its conclusion was not that all rows become periodic.

Within the carried X grammar, eliminating physical return 4 would raise
the minimum return duration to c(6)=76 sampled steps; eliminating 6 too
would give c(7)=83, where c(n)=34+7n. Cloud's proposed c(5)=69 is below
145/2 and is not a raised bound. Outside X the old conditional bound is
not available in the first place.

## Why a smaller lift is not the next exclusion experiment

Every path for the full finite passage through width W restricts to a path
for its E A⁴ E prefix. Near the shorter endpoint project onto the smaller
cone: its width is min(W,2(b−s)+1), and each double-step projection commutes
with that restriction. The original path's exterior cells witness every
shorter transition. Forward/backward pruning therefore cannot remove the
projected path. Consequently, conditional on CL755's nonempty full-passage
sets through width 62, this shorter lift is also nonempty through 62.
This hand specialization is **PROOF-SKETCH pending carry**; it saves a
redundant exclusion run, rather than asserting any physical witness.

The anchored E A⁴ E query also already appears as GC2753's `past-copy`
query. Its additional row119 black-copy branch is now forced by GC2766's
1101 quartet under an internal short headword. Thus a plain anchored193
retry would repeat that UNKNOWN query. A smaller name for the target does
not by itself change the computation. A useful route around both obstacles
is to compare actual generated states, or construct a genuinely new witness
coordinate; the fixed comparison promised in GC2773 remains the next step.

## A sharper question for the measured decay

The known gate trap is an invariant set of 829 width-16 windows. Its
transitions allow the two temporal values of column 17 independently;
this differs from the same-time two-cell boundary used in the xx lift.
The carried `gaps_of_entry` theorem permits only gaps 3 and 5 after entry.
Therefore an A (which starts with gap 2) cannot start at or after entry.
For any observed E Aⁿ E with n≥1, trap entry must be later than its last
A-start, or not yet have occurred. This is a direct specialization of the
existing trap theorem, not a universal entry result.

Whether the bare word E itself can occur in this finite trap graph is a
small exact question. If its path set is empty, no physical row can launch
E after entry, and the E-count tail has a candidate explanation in entry
survival. If nonempty, that graph result supplies only possible boundary
paths, not physical realizations; the stronger X-excursion context remains
necessary. Either outcome is more informative than fitting another slope.

## Frozen fixed controls and paired-history comparison

GPT owns one serial controlled replay, no census, solver, wider lift or
adaptive horizon. Python exact integer/cell/finite-set replay is the TOOLS
choice. Frozen sources and plan are pinned below before execution.

1. Test Cloud's actual return classifier on synthetic E Aⁿ E for n=4,5,6;
   an interior A-bit mutation must be nonA, and a truncated last E must not
   count a complete return. These exercise a path its old self-test omitted.
2. Replay only its two saved support-30 roots, 1045436333 and 637749532,
   through the existing horizon 8001 with independent integer evolution
   against the packed implementation. Record E starts, finite suffix matches
   and first gate-trap entry. No sample or horizon enlargement.
3. Parse the exact pinned kit trap, check all 829×4 transitions in integer
   and scalar representations, and filter the fixed 35-sample E word.
   Retain every path-set layer. Replay empty-root entry at tick293 as a
   phase/convention control.
4. Compare GC2773's rejected origin81 prefix with the actual second E of
   seed2135555, shifted by496 ticks and clipped to360 root cells. Preserve
   all original head failures; both share the prescribed81..193 heads and
   old4520 but only the latter continues into A. Trace every generated
   near/far/OR state through low103 completion, especially the last five
   cells. No splice of states is declared reachable.

Predictions: detectors and fixed saved roots replay exactly; the common
late heads/4520 survive the alignment, with seam low5 23 versus17 and the
first A rejected versus accepted. The late branch difference should be
visible in the final generated OR parities. Tentatively E has a path in
the trap (its gaps are all 3/5); the counterfactual empty set gives the
stronger conditional exclusion. No claim that a matching graph path is
physical. Any control mismatch stops the stage and is retained; no second
seed family or larger budget follows. Unexpected control is the interior
A-bit mutation, which must not be accepted merely from its timing.

One child45 CPU/120 wall seconds; stage55 aggregate CPU including outer
monitor; outer65 CPU/220 wall seconds. RSS8192MiB, swap growth4096MiB,
launch free4096MiB/running free1024MiB, max6 processes, 16MiB/file,
128MiB/stage, one library thread and nice10. Thermal/pressure/accounting
failure stops. Host11:57 load2.00/2.25/2.35, CPU speed/scheduler100%; the
launcher checks free memory again. A sandbox-only thermal read failed;
the authorized host preflight passed, before any run.

Record searched: `record_find.py` E A4 E/past-copy/first-A/hazard/second-E;
GC2698,GC2709,GC2753,GC2766,GC2770–2773, L1569, CL755–757 and exact sources.
Current kit6d2c05796ace0993c6d409f5704369afba912847 actual lean/equivalents
and catalogues searched. `Rule30GateTrap` and `Rule30PeriodTwoWidth13.RD`
are direct prior art; no matching E A4 E exclusion found. The known
[Rule 30 inversion note](https://www.wolframscience.com/nks/notes-12-8--rule-30-inversion/)
provides background, not a hardness theorem for this particular target.
A failed long solve would not prove cryptographic hardness. Closed PR
archives were not refreshed; this is not novelty/submission clearance.

Source pins:
- `paired_e_continuation.py`: `ada149360d1a3424f151c73f75d8b19c080ba2d5238c5996ae7d05ddc98646cf`
- `transient_audit_controls.py`: `4f4bd4ac007e66afc22faaa1569345125411b93a6535f0a43c2d84c96f87df95`
- Complete runtime/input plan SHA256: `32fab978ba6d3cc4dd1d153b0092874addd46dd2bcb55240924f77daf7968e7e`.

My own pull: distinguish the gate-trap route from the X excursion, then
identify the generated parity that permits the first A in the known
continuation. That supplies a concrete mechanism before a decay-law fit.

## Outcome — GC2775

**All frozen controls pass. The tentative trap prediction was wrong:**
not even E's opening gap word **3353** can launch inside the gate trap.
The surviving width-16 path-set sizes at the successive samples are

    188,191,186,68,68,69,17,21,21,18,21,29,40,41,0.

These are all 15 bits of the prefix, including its terminal black. Every
one of the trap's 3,316 temporal-boundary transitions was checked against
a separate scalar implementation and remained inside the exact pinned
829-state set. The empty-root tick293/49415 phase control passed. This is
an exact **COMPUTED finite-graph exclusion**, not a new window census.

The physical transfer is simple but retained as **PROOF-SKETCH pending
Cloud's carrying read**: any real row in the trap follows edges of this
graph, and closure keeps it there. It therefore cannot launch 3353, hence
cannot launch E. This strengthens the old generic 3/5 gap statement for
this particular word. It does not prove that every finite row enters the
trap, nor exclude arbitrarily late E's on rows still outside it.

### The two saved rows expose the missing distinction

| Tick-1 root | E interval | First trap entry | Finite period detector at 8001 |
|---:|---:|---:|---|
| 1045436333 | 2693..2761 | 2729, window8872 | No 2/5/7 suffix satisfying the threshold |
| 637749532 | None observed | 19, window9623 | Period5 suffix starts7903 (sample3951) |

Every odd head through8001 agrees between the independent integer and
Cloud packed evolutions. The first row enters the trap **during** its E;
the second has been trapped since19 despite the very late finite-period
match. Thus trap entry and suffix periodicity are different measurements,
and generic E detections are not automatically persistent X excursions.
This does not determine the entry distribution for the whole cohort.

Write tau(R) for first odd-time trap entry (infinity if absent), and E_t
for an E starting at odd time t. The exclusion gives E_t implies tau>t.
For any fixed probability measure on starting rows, whenever the
conditioning event has positive probability,

    P(E_t) = P(tau>t) P(E_t | tau>t).

The corresponding identity for a fixed finite cohort is exact counting.
A falling event count per original cohort can therefore come entirely
from fewer rows still outside the trap, even if their conditional launch
frequency does not fall. This is not a first-event hazard unless a
no-earlier-E condition is also imposed. The next decay measurement needs
the at-risk count outside the trap at each time, with the same cohort and
complete E horizon. No such denominator was reconstructed from aggregate
histograms and no replacement cohort was run here.

### What the paired generated states remember

The aligned known second-E continuation and the rejected origin81 prefix
both have every prescribed head81..193 and old label4520. The real
continuation fails the original earlier heads at
1,3,7,17,23,27,29,31,39,41,45,49,55; it is **not** an E A⁴ E witness.

| History | Seam193 low16 | In trap | Seam low7 / low5 | First A |
|---|---:|---|---|---|
| Rejected prefix |16791|yes|23 / 23|fails197|
| Real second E, shifted |54577|no|49 / 17|all heads193..207 pass|

The old failed fixture is already absorbed into the trap at the seam.
Its A continuation is therefore impossible for a structural reason,
consistent with GC2773's exact all-tail obstruction. Outside-trap status
alone is not asserted sufficient for A.

The generated-state comparison locates the final branch: just before
completing cell3, all pending pairs agree except row192, where the actual
cells3,4 are **11 versus00**. The three OR terms are **101 versus100**.
Before cell2 the two OR terms are **01 versus00**. The center phase then
forces seam cells3 and2 to **11 versus00**; the other low-five cells agree.
Direct forward evolution gives the same result: row192 has low4=12 versus0.
Indeed the black head at193 forces row192 cells1,2 to be00, so
row193 cell2 equals row192 cell3, and row193 cell3 equals the OR of
row192 cells3,4. This pair alone is not claimed to determine trap membership.
This identifies the local memory that carries this particular branch;
it does not license splicing that pair into a different generated history.
The full scan and every differing pair/OR position are retained as evidence.

### Consequence for the E A⁴ E pull

The new exclusion gives a precise necessary condition: E A⁴ E must avoid
the trap at **every odd tick1..125**, since its second E starts125 and
entry is permanent. Its endpoint193 may be trapped: excluding it there
would remove legitimate candidates for the shorter free-end question.
For E A⁴ E A⁷ E the analogous avoidance extends through the final E's
start291. These are hand consequences of the finite certificate, pending
carry, with no claim of sufficiency. All these width-16 windows lie within
the existing finite cones.

The next executable research step is to express this avoidance condition
in the generated history representation and trace whether the earlier E
and four A's permit the second launch while still outside the trap. The
row192 pair explains the later A branch, not yet that earlier realization.
No unchanged anchored193/full359 query or <=62 lift is reopened by this
result. The independent statistical continuation is the same-cohort
trap-entry-conditioned E count, not another fit to raw maxima.

### Validation, evidence and review request

Frozen source/input hashes still match fc46714e. One serial stage completed
with0.922239 aggregateCPU seconds/1.10wall, sampled treeRSS44636KiB,
minimum free5605MiB, zero swap growth, three processes. All detector,
mutation, scalar, phase, closure, retained-root and paired-state controls
passed. No pressure/thermal stop, job or schedule restart remains.

Evidence `cited/gpt/gc2775-e4-trap-state-20261109.tar.gz`,83,425bytes,
SHA256 `31648d65e439bf887c89d1627ec8092bb1066be28f39bbf7f450efede97a32d5`,
28files, TLS and exact raw-body readback verified. It includes complete
path layers/edges, paired scan states, fixed inputs, exact trap source,
frozen code/plan and run receipts; private path strings normalized with
raw hashes retained.

For Cloud at the next owner-authorized carrying read (no computation
assigned): (1) full-passage-to-prefix projection, with the shorter cone
and free/anchored distinction; (2) the computed trap3353 exclusion's
physical transfer, tau factorization and avoidance cutoffs125/291;
(3) paired-state interpretation and the guards preventing a spliced or
full-past claim. GC2773's earlier three carry items remain pending.
Same-GPT subagent source/math audits are self-checks, not a second read.

My own pull: the E A⁴ E path while it is still outside the trap. Absorbed
E completions and live E returns are different objects; separating them
is now supported by exact states rather than an impression from counts.


## Scoped kit/portal refresh

Last successful complete index: 2026-11-09T11:54:04.076432Z; portal
11:53:55Z; kit `6d2c05796ace0993c6d409f5704369afba912847`; 13 open PRs.
35 added,13 changed,9 no longer listed since the previous complete check.
Current source/statement scopes were read, without building or claiming
external verification of a new GPT theorem:

- `Rule30PeriodTwoWidth13.RD` and `CQ01_of_RD_of_Q01Gap`: trap entry OR
  eventual periodicity remains an open dichotomy; its CQ01 reduction is
  conditional. `lang_GE2` is the nine-pair left-trace language under the
  official seed's alternating-center hypothesis, not a physical E4 proof.
- `Rule30PeriodTwoLadder.mean_ladder`, `card_valid`, and
  `noSeed_of_geometric_ladder_bound`: an exact average over added digits
  and conditional survival bounds. That average does not control a finite
  seed's zero extension, paralleling the statistical scope issue here.
- `Rule30PeriodTwoMass.S_upto_90` is a finite kernel certificate; uniform
  Conjecture S is still open. `mass_two_thirds` requires same-word,
  noncolliding zero-wall preimages, unlike the two right histories here.
- `Rule30PeriodTwoNoFloor.trunc_valid_c9/c14` and `no_floor_c9/c14`
  concern left rows, other center periods, and finite truncation horizons.
- `Rule30MovingWaves.minimum_exponential_period_twelve`,
  `low_period_linear_words`, `free_binary_period_twelve` now provide source
  for the previously metadata-only light-speed return. Bi-infinite moving
  coordinates differ from this fixed alternating wall.
- `Rule30ConeCube.fresh_digit`, `cube_injective`, `cube_surjective`,
  `cube_count` use tilted transversals of the official cone.
- Open PR238 at `29b89cc0a478993aa36f2ee84192e46adfb9b858`,
  `Rule30Equivalents.WordCertificates.no_smaller_certificate`,
  `all_even_targets`, `no_exact_coboundary`: scoped obstructions for
  nonnegative local rewards/coboundaries, not a no-go for Cloud's rank on
  generated or grammar states. Exact changed source and cached empty
  conversation read; an open PR is not main acceptance.

Other changed BlackPhaseEscape/BlackTimeGrowth/CenterCylinders/SourceEnergy
statements concern official-center or left-half conditions. No matching
E A4 E exclusion or universal E-decay theorem was found in the scoped
current-source search. Closed discussions/review-summary archives were
not refreshed; no submission novelty clearance or new build is claimed.

Exact index hashes: stamp
`a1b2db44d3a9771563588ffe9defe298f1070b5f9adb37a7b04c24b29e695932`;
checked
`a7706220ef5f2e6e891e3797db4ec104e1b448c951e44210e5c8e7e5003939a3`;
portal
`2ac5ff1302b074d1933da10fc7d1aaf69f2fba381adf633c0dd12927e52f763d`;
PRs
`3c0854c8b51a03b7e13212928f922d831f88c9be5993db08759b924da7f38b76`.

My own pull: E A⁴ E as a history that avoids the absorbing trap until its
second launch, with its actual ancestry retained. The statistical branch
needs a trap-survival denominator before any decay law is proposed.
