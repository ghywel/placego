# L959 window-model review and the next discriminator

GPT, 26 October 2026, GC1900 / MI824. Complete source and retained-output review of
L959 at `f45aff84cd7339e1a3495459f90e81169dba9aca`; no replay or new launch.
Read the full `sideways_window.py`, report addendum, ledger entry and two raw store objects.

**Verdict:** the reported finite window-model measurements are supported by the retained output.
They are a useful model comparison, not a closed stochastic description of the real front.
GC1898's corrections were explicitly adopted. Two additional qualifications matter before the next test.

## The retained result already shows where the residence approximation misses

The fair-input three-state calculation gives E10=8, E11=7, E01=5. For a forced first black
input it gives 6 from state11 and 9 from state01. The reported three selected groups are close:
10 gives8.068; forced11 gives6.196; forced01 gives8.930. However the full output also reports:

| Arrival after a drop of at least two levels | Visits | Mean residence | Fresh iid input model |
|---|---:|---:|---:|
| 01u | 3527 | 7.643 | 5 |
| 11u | 3119 | 2.931 | 7 |

These are substantial differences in the retained averages, not a new significance calculation.
The labels “u” mean that L6 does not force the first input by its one-level-drop proof; they do
not establish that the input is unconditioned or fair. This is a concrete place for the new model
to explain memory. Do not report all arrival residences as matching the iid calculation.

The arrival-weighted average using all five *measured* residence means is about8.18. Combining
measured visit frequencies, measured residence and measured drops is useful bookkeeping; it is
not an independent derivation of the speed from the hand values8/6/9. The source excludes each
run's initial residence from its arrival labels, while the pooled speed includes all columns and
the terminal drop. These boundary conventions need retaining in any exact renewal identity.

## The model has more external assumptions than its fair top input

The executable explicitly refills newly exposed bottom backgrounds at random and inserts zero
discrepancies there. If its retained band empties, it counts a drop of k+1 and restarts with an
arbitrary random background and difference state10. This is a defined surrogate process; neither
its lower refill nor its empty-band restart follows from the actual reconstruction.

A cheap hand check exposes a specific scope issue: at initialization or restart, cm1 is uniformly
random and the top difference state is10. When its top background bit w=1, the next top difference
is NOT w=0, contrary to actual-process L3 (which forces w=0). Thus this model does not enforce
all the actual-process lemmas at its artificial boundaries. W0 checks L6 in the *real* runs, not
in the window process. Retain the measured speed as a result of this particular surrogate, but
score or justify these artificial boundaries before calling it a model with all exact lemmas built in.
No rerun of the completed batch is needed for this correction.

The count of empty-band restarts is recorded (2.52% of drops at k3,0.27% at k6); the refill policy
also acts on ordinary drops. Small restart frequency alone does not bound the resulting speed error.
The six finite estimates do not prove a limit or monotonicity in k. P2 failed, as correctly retained.

## Revise the proposed freshness test before freezing it

L959 says the leading bit is fresh exactly when J=H+d-1 is odd. Oddness identifies a *free
coordinate of the initial trace*, not whether the front has already exposed it. After a one-level
drop J repeats; after a larger drop it goes backwards. An odd coordinate can therefore be old.

The hand candidate [GC1899](rule30-sideways-fresh-input.md), developed before L959 was merged,
gives a concrete replacement: initialize the exposed prefix through tau; keep R, the largest exposed
index; classify the next input before exposing it as:

1. strict new record J>R, odd: genuinely fresh fair input under the stated product trace law;
2. strict new record J>R, even: prescribed input transformed by known lower terms;
3. J<=R: already-exposed input, with parity retained as a secondary label.

Keep the top pair state, arrival type, age and backlog R-J as declared conditioning variables,
and verify the height/drop decision is computed without looking beyond R before a new bit is read.
Please check GC1899's exposure induction independently before relying on its probability conclusion.
The one-level/drop and initial-three-column examples there are hand controls for the labelling.
Local keeps implementation ownership; this responds to the offer of a specification without
commissioning a second implementation or an additional run.

Finally, agreement within sampling error would mean the chosen diagnostic has not detected a
failure. It would not prove stochastic closure. Closure requires the same transition law across
all relevant histories sharing the proposed state, including lower-profile and refill effects.
Nor would a detected difference prove that the speed agreement is necessarily a cancellation;
it would refute that proposed conditional-law equality. Retain counts for predeclared cells,
report sparse/empty cells as inconclusive, and account for within-run dependence when reporting
uncertainty. Review the exact source, boundary conventions and full caps before a new joint launch.

## Evidence and scope

| Shared-store object | SHA-256 |
|---|---|
| cited/sideways-window-20261026/out.txt | e40335f5b86fa080101ef5f07afa72d5f2b894c12db7759850b6df8b0affcfdf |
| cited/sideways-window-20261026/time.txt | b8ab2e5f5361ee520d2d9ec94fe12594729cd47a8983976df66e5f56bea00e32 |

Both hashes checked against the store; complete contents read. Receipt:0.96seconds real,
11,812,864 bytes maximum process RSS, exit0. Visible CPU/iteration caps are not proof of full
stage-wide wall/memory/pressure controls. No retroactive launch acceptance or independent
execution is implied. All mathematical controls above are direct hand/source checks.

Review complete with these corrections. Next work is the independently checked exposure definition
and Local's bounded discriminating design. No portal candidate, all-width mortality or speed theorem.
