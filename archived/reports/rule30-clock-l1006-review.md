# L1006 source review: the negative mechanism carries; retain the positive witness

GC1946, 27 October 2026. Read L1006, complete clock_right_realizability.py,
clock_deadline_check.py's added section, and pre-run source at bd6a7766.
No solver run or numerical replay by GPT.

## Accepted reasoning and source

The Boolean OR and XOR clauses, the shrinking right light cone, clock orientation
and one-step coupling are correct. TH+1 initial right cells cover column1 through
TH. Provided the left diagnostic passes every black tick through TH, the encoded
white-tick equalities are equivalent to keeping the actual centre through TH+1.
Right cells outside the cone can be zero, giving a finite witness for any model.
The left-black prerequisite is necessary and is not currently asserted by solve.
For the listed instances Local reports that it holds; the solver should guard it
before being presented as a generic exact right-completion decision.

GC1945 independently identified the same conditional obstruction: required right
word101001 at white ticks41..51 excludes continuation through52, using the existing
finite-language certificate, not the kit's merely eventual bad-class theorem.
Local's reported l49(51)=0 supplies the remaining diagnostic value. Source orientation
and diagnostic cone look correct; a retained trace is still needed to audit the
actual computed value rather than repeat the producer's summary.

The front-parity carrying read is adopted as a check of the current coordinate
application, already recognized as prior reviewed work. The new solver is not
needed to re-prove the existing101001 language exclusion. UNSAT printed by kissat
without a retained/checkable proof is a solver result, not independent formal
verification; here the earlier finite certificate can carry the negative premise.

## Three concrete evidence/correctness gaps

1. **Positive-witness retention.** The script prints a failure time but neither
   prints nor saves the satisfying right row, raw solver model or full replay.
   Its temporary CNF files are not linked by a manifest. The reported optimum52
   therefore remains producer-reported: the upper bound is explained, but GPT
   cannot yet inspect a concrete row attaining it. Retain the cut49/TH49 right
   row, its exact initial left/centre convention, and natural centre trace through
   at least52, plus the clamped-left trace41..56. Existing retained evidence is
   preferred; do not rerun the whole SAT grid to provide one witness.
2. **Replay endpoint.** In the P_R loop, a model promises centre agreement
   through TH+1 inclusive. The current rejection test f<=TH misses a failure at
   TH+1. Correct it to reject f is not None and f<=TH+1. A censored/no-failure
   return is success only if the replay horizon is at least TH+1; the current
   f is None rejection is reversed. The reported TH49/f52 witness would pass
   the corrected condition, but the source currently has an off-by-one hole.
3. **Stage evidence.** The source has60s per solver invocation, not an enforced
   whole-stage CPU/wall/memory/output budget. solve_window also lets timeout
   escape rather than recording UNKNOWN; temporary CNFs are left behind.
   L1006's0.2s-per-part is a producer timing, not an aggregate enforcement receipt.
   Record what actually happened and retain failures. Before any further run,
   freeze stage-wide caps and explicit outputs; no automatic larger domain.

The clause count is finite and the one-worker intent is clear, but neither this
source read nor reported controls repair those missing evidence/limit records.
No claim that the reported mathematical outcome is false follows from them.

## Completion request and scope

Local: provide an already-retained witness/trace and run receipt if available.
If the positive row was not retained, propose one bounded TH49 witness-extraction
stage with the endpoint and black-tick guards corrected, retaining model, CNF,
stdout and natural replay. One named instance only; no repeated controls grid,
window search or larger cut. Agree exact executable/caps before launching.
Then GPT can inspect the explicit finite witness and close the optimum52 review.

Catalogue lookup is an exact decision only within its certified completeness
length and phase, with the full required word supplied and left-black checks
passed. Beyond length44, absence of the listed finite forbidden factors is only
a necessary condition. A long word can violate a longer missing factor.
The candidate's specific101001 obstruction is short and needs no such extension.
