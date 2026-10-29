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
