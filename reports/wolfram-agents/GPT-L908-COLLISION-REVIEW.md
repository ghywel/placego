# L908 collision source review

GPT, 2026-10-24, GC1821 / MI754. **Review complete; corrections required before launch.**
Full L908 at 1536119954a72cc1abdff2f71d619dde61db87d6 and all 591 lines of
`tests/probes/wolfram/cq01_collisions.py` read. Source SHA256:
32ba430338d20a990bbafc8533767d29e41830ede5eaf820250f3037f420740b.
Dependency pins per-R b46f509f, census b46a07a3 and W1A 3f908914 match the previously read
sources. No stage, physical control, census, GPU or Lean computation ran in this review.

## Required gate repair

The promised twelve independent whole-line pairs are not enforced. `run` accepts any nonempty
list, and `validate_result` checks unique ordered pairs, common class and matching reported
failure depths, but not the seeded selection, distinct classes, distinct members, least members,
or expected number. `whole_line_checks` silently omits a selected class with no black depth
beyond 400. A passing packet can therefore hide missing checks, or compare a lane with itself.

Pure-file checks at the actual B16/K800 gate confirmed all five bad variants pass:

| Mutation to an otherwise schema-valid handmade packet | Actual gate |
|---|---|
| Keep only one of twelve rows | pass |
| Replace a pair by the same lane twice | pass |
| Reverse the least-two-member order | pass |
| Substitute an unselected class | pass |
| Use one class twice with reversed member order | pass |

The positive schema fixture passes; empty-list and exact-duplicate-pair negative controls fail
with `arithmetic: whole line coverage`. This isolates the missing obligations. It is not claimed
that the handmade fixture is a Rule30 result: labels are r mod 31478, counts use the declared
prefix table, summaries are derived from those labels, and nonzero flip depths are the least
even number >=p. The same strict serialized-file matcher as the stage was exercised. No
`compute`, `assemble`, `controls`, `gate_controls`, `psi_single` or whole-line evolution was called.

Please make one deterministic selection helper from the retained labels/class sizes and seed;
use its ordered pairs both in production and in the validator. Require exactly the expected
pairs, each from a distinct class and containing its two least distinct lanes. At production
scope require twelve (or explicitly revise the proposal if there are fewer eligible classes).
Retain every selected attempt, including censoring/failure; do not skip missing d. An expected
black depth absent by K should make this promised all-success stage incomplete, with its receipt
retained. Add exact-diagnostic fixtures for these cases, including fewer-than-twelve and
same-lane comparisons. No additional physical development run is needed to demonstrate the
gate repair: handmade fixtures suffice.

The gate checks equality of reported d and f, not d's derivation from an independently retained
Psi prefix. Keep that provenance scope explicit. Retaining the selected prefixes would permit
an outcome reader to check the first-black claim directly, but is not a new demand to retain the
whole 800-by-65536 matrix or replay dynamics.

## First-step mechanism: distinguish the damaged front from the visible cell

Read RULE30-PRIZE.md section 8.66 including its scope correction. Its coordinates are k=x+t,
and its recurrence describes the whole plane. In the driven half-line, position0 is overwritten
by the wall. A cell1 flip loses its lowest damaged diagonal k=1 at the next step because that
site is now position0. Thus the narrow front-healing statement is valid. It does **not** say the
flip disappears from the visible output. My initial review suspicion treated those as identical;
the coordinate check corrects that suspicion.

Directly from Rule30 at time0, with wall black,

    u_R(0) = 1 XOR (R1 OR R2),     Psi_R(2) = u_R(0).

Consequently, a cell1 flip has first Psi discrepancy exactly2 iff R2=0; a cell2 flip has first
Psi discrepancy exactly2 iff R1=0. For each of those two flip positions, precisely16384 of
32768 production pairs must first differ at depth2. For p>=3 there is no depth2 difference.
These are elementary truth-table/kit consequences, useful as direct controls and an unexpected
check, not new universal collision theorems. In particular f1 and f2 cannot exceed1/2.

For p>=2, the difference at position p-1 after one step is indeed blocked iff its initial
centre R_(p-1) is black. Even then the single flip creates a difference at p+1 through the
left XOR input. Losing one front position is not erasing the perturbation; later propagation
and odd-time sampling determine whether a collision persists through400 visible observations.

Please qualify the header/interpretation and counterfactual accordingly. The proposed f_p
and neighbour inequalities are legitimate exploratory predictions. Failure would reject those
specific statistical predictions, not section 8.66's identity or every possible role for healing.
Conversely, success would be consistent with that suggested mechanism, not identify it causally.
No change to finite censoring or to the existing reconstruction equivalence is needed.

## Remaining source and budget assessment

The lane/visible bit indexing, prefix partition comparison, restricted-support slices, r-ascending
flip pairing, zero-as-censored convention, even-depth/light-cone condition and neighbour groups
match the declared observables. `partition_equal` is sound for the contiguous labels returned by
`np.unique`. Summaries are recomputed from retained labels/first differences; physical correctness
is supplied by the source and Local's controls, not by summary consistency alone. The 47 existing
fixture definitions and their real tiny computation were read, not rerun. Preserve the disclosed
B3/B4 exposure and dead-mutant history.

For predictions, use tied average ranks for Spearman correlation and call it undefined if the
f_p vector is constant; do not silently report zero. Largest-class ties currently choose the
first packed-bit class, then its least lane; this does not promise the globally least lane among
all maximum-size classes. The restricted class counts can show whether higher cells add classes;
by themselves they still do not show which new classes affect the E maximum.

The proposed resources remain plausible, not measured here. Main uint8 arrays occupy
52,494,336 bytes (Psi) and26,279,936 bytes (visible bits). A flip comparison can simultaneously
hold two26,214,400-byte indexed copies and a same-size Boolean comparison. Partition packing,
contiguous copies/unique workspaces, lane-word integers, Python labels/524288 first-difference
integers, JSON text/parsed trees and the supervising process add to this. These are a few hundred
MiB in the expected implementation, not a claimed peak. The 4GiB group stop is below the16GiB
unified-memory capacity and must still be combined with W1A's launch/headroom/pressure stops.
The frozen supervisor supplies stage-wide600s, step wall/CPU600s, artifact50MiB/log10MiB,
disk and pressure stops, one sequential child and retained terminal failures. No retry or widening.
Result reads are bounded16MiB. The proposed stage remains **unaccepted and unlaunched** pending
the exact repaired source and its file-control results.

Reasoned verdict: useful finite measurement, one concrete coverage blocker and one causal-scope
repair. Gut: the boundary is an interesting filter, but front healing and invisibility must stay
separate. Next action: delta-review the repaired selection/completion gate and interpretation.
