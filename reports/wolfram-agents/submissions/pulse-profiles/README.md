# Pulse profiles — partial formal implementation, not submitted

GPT, GC2044–GC2045, 29 October 2026. Writing owner: GPT; other reader: Local. The statement/scope draft is
[the package specification](../../PULSE-PROFILE-SPEC.md).

`Rule30PulseProfiles.lean` has12 proved theorems in core Lean with no imports, placeholders, custom axioms or
native evaluation. It passed its first capped Intel development compile under Lean4.33.1, source frozen at
f0129f48. The three printed axiom checks report no axioms for source_bit_correction, and only propext/Quot.sound
for pulse_window_bound and leftDiag_step. No current-portal-toolchain validation or independent source read is
claimed for this new module yet.

**Formalized:** Boolean source recovery/uniqueness, the pointwise signed weight correction, reduction of all six
nonempty interval costs plus the empty interval, monotonicity in first delay, exact pulse-arrival maximum,
and the literal left-diagonal recurrence for arbitrary Rule30 initial rows.

**Still missing:** cyclic summation into the source weight/run-count statement; the actual cyclic pulse-child
hole identity and conversion from reset phases into delays(k,L,1). The bound theorem is currently conditional
arithmetic in k,L. It does not assert that arbitrary inputs have these delays. The actual Rule30 recurrence
bridge does not confer finite-seed ancestry on arbitrary periodic profiles.

No essay/notebook, kit module/PR, submission ID or verifier receipt exists yet. Base hand claims retain the
older PROOFS24/25 carrying reads; the new assembled formal source still needs Local's independent read and
current-toolchain validation. Novelty remains unresolved; general synchronization is known background.

Evidence: shared store cited/gc2044-pulse-core/manifest.json, SHA256
b488280f1e1ea9b5f1d58326567ec983bdd7dfffbfc25be89ec9932af093456c. This binds source, output, time and launcher
receipts. No rerun was needed. Child4.85s elapsed,1.86s user/0.77s system, max processRSS341,848,064bytes;
supervisor5.24s wall and0.125s CPU. Four samples, maximum groupRSS307,788KiB, minimum free+inactive5751MiB,
zero swap growth. Launch5907MiB headroom,152MiB swap. Per-process CPU/file limits applied; process-group and
pressure monitoring sampled, not a continuous/system-wide memory peak. Output1010bytes before final launcher
receipt; no resource stop. The compiler stage's unused repair attempts were not run.

## GC2047 — cyclic weight/run identity now formal

The source frozen at08581b6d compiles with23 theorem declarations under the same Intel Lean4.33.1. The finite
sum of changes telescopes to twice the rising-edge count plus bit(f0)−bit(fn). Seam equality f(q)=f(0) closes
the count. The pulse source differs in one bit, giving pulse_source_weight and its three cases; the
heavy_source_two_runs corollary is proved. Both new printed headlines use only propext and Quot.sound.
Cyclic run count here means rising-edge count, zero for either constant word, with no hidden nonconstant
hypothesis. Seam equality is enough for the finite identity and is not asserted to imply periodicity.

Attempt1 failed at a corollary's final omega call because a simp-only step left the Boolean conditional
unreduced. Retained error; one explicit simp repair, separately committed; attempt2 passes. No scope/cap
change or third attempt. New evidence: cited/gc2047-pulse-weight/manifest.json, SHA256
5146eda5acb1460b6a451ce4196c85d79c8f79283483b103cc4a1bdbb40ab68d, binding both sources and both attempts'
output/time/launcher receipts. Attempt1 child2.00s wall,2.49user/0.35system; max processRSS355,631,104bytes.
Attempt2 child2.07s wall,2.53user/0.34system; max processRSS370,085,888bytes. Supervisors2.10/2.16s wall;
sampled groupRSS maxima304,656/305,984KiB, minimum free+inactive5825/5803MiB, zero swap growth in both.
No resource stop. Remaining main formal gap: periodic pulse-child holes and actual reset-delay identification;
current-kit validation, independent assembled-source read and submission preparation also remain pending.
