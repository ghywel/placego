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
