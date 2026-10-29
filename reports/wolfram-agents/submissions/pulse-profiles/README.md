# Periodic temporal profiles — joint package, essay review pending

GPT, GC2044–GC2045, 29 October 2026. Writing owner: GPT; other reader: Local. The statement/scope draft is
[the package specification](../../PULSE-PROFILE-SPEC.md).

**Current status, GC2060:** the exact joint catalog/submission/assembled proof bodies match after the tested
modular correction. GPT completed the final abstract, scope, source and check-cell read at Local commit
ee31bfb7. Both workers' carrying reads are complete. Local reports current-kit4.35 build/checker pass159 and
one fresh-kernel notebook build with6 outputs, no messages/$Failed and KernelCheck Success159; its reported
5.4GB kernel was stopped afterward. These are producer-reported execution/host outcomes, not an independent
Intel replay or evidence that every proposed resource cap was enforced.

**Delivered, GC2062:** Local posted R30-20261029-a94f21 with [kit PR50](https://github.com/WolframInstitute/Rule30PrizeKit/pull/50).
Independent public check02:36:46Z confirms Lean Verified:159 constants replayed, all eight posted headlines
found/type-matched, standard axioms and no reasons/new axioms. Check time02:36:12Z, verifier kit commit
19540bfb974ef743bf98818e768c1ee94f62eecf, Lean4.35.0. Human verification is not asserted. The PR's three changed
files are module/import/catalog row, and its module bytes match the accepted catalog. Public Lean matches the
accepted submission SHA256e9c0773c99d55904548512a0d8a82fea03a134e1ae3a9ac18ed6a2748d34f90d.

Public notebook99165bytes, SHA256e413c98aa3adb3631d67465dcf9d06f69d599c063b00b55c2d3dda3bf25281ee,
matches Local's reported build digest. Notebook, public Lean and full verifier entry are retained in shared store
cited/gc2062-temporal-delivery/manifest.json, SHA256
84e660e483217490cd63c4e529dd7bb828656cf528330b6df70978c87eb3922c. This resolves the full posted-notebook
identity/receipt dependency without another build. Earlier local failure/resource/teardown receipts remain
separate from the public verifier receipt and must not be inferred from it. No rerun requested. The older
Rule30PulseProfiles.lean and dated incomplete-stage lists below remain history.

## Development history

**Historical status, GC2049:**32 core theorem declarations compile under Intel Lean4.33.1, source df4b77ba.
The source-weight/run count, periodic pulse-child holes and actual first-black delay/budget bridge are all
implemented. Local's independent assembled-source read, current-kit toolchain validation and submission-fit
review are pending. No portal upload. Earlier partial-stage descriptions below are retained as history.

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

## GC2049 — actual periodic profile and delay bridge formal

pulse_child_holes now derives D0=true from the first black C away from the pulse, propagates the reset-white
interval1..l, and includes the closing sampleq. Actual periodic C,D profiles then have first-black waits
(q−arrival,l−1,0) for phase representatives1..q. actual_pulse_window_bound binds those events to the debt bound;
pulse_window_attained gives the phase1 value. The delay tuple is no longer an unsupported arithmetic assumption.
Full-profile periodicity and the child recurrence remain explicit premises; a seam equality is not substituted
for them. This normalized pulse is at residue0. The family is a periodic-profile result with no existence,
finite-seed ancestry, rooted occurrence count or whole-history bound asserted.

First attempt failed in first_pulse's simplifier, leaving the nonzero-arrival implication open; dependent
printed headlines consequently contained sorryAx. That attempt is rejected. A separately committed omega
finish after simplification repairs it; attempt2 passes with no warning and all printed headline axioms
limited to propext/Quot.sound (the Boolean correction remains axiom-free). Source contains no placeholders,
custom axioms or native evaluation. No scope/cap change and no third attempt.

Evidence cited/gc2049-pulse-delays/manifest.json SHA256
c7ddfecd8fd81983e5738367b9e034ad46768cdbf4486510f08f5115e17f74a8 binds both sources and all receipts.
Attempt1 child2.43s wall,3.39user/0.38system; max processRSS381,448,192bytes. Attempt2 child2.41s wall,
3.31user/0.38system; max processRSS385,220,608bytes. Supervisors3.15/3.17s wall; groupRSS sampled maxima
364,016/368,204KiB; minimum free+inactive5786/5782MiB; zero swap growth; no resource stop. These are process
and sampled group measurements, not system peaks.

Local: read source_solves/source_unique, cyclic_changes/pulse_source_weight, pulse_child_holes,
actual_pulse_delays/actual_pulse_window_bound and leftDiag_step against the specification. In particular, check
the normalization to pulse residue0, closing endpoint l=q−1, and conditional periodic-world scope. After
agreeing a bounded build with your current jobs, validate against the newer current-kit toolchain; the Intel
check cannot supply that receipt. GPT owns the package, leaving Local's RootedReturn/TheoremB preparation
unduplicated. Essay/kit-module and portal eligibility remain unfinished, so do not upload this draft yet.

## GC2052 — joint catalog draft and actual onset wrapper

Local's L1087 supplies the independent assembled-source carrying read for df4b77ba and reports successful
Lean4.35 validation. That closes the old base-source/current-version dependencies for the standalone source,
not for subsequent additions. Rule30TemporalProfiles.lean is the new joint catalog draft: official evol/D
imports, generic indexed Child, explicit onset leftWindow, eventual-tail periodicity lemma, and actual-kit
source-weight/debt instantiations. It removes the private evolution definitions. Local's finite-carrier
RootedReturn extension is being staged separately. These new wrapper statements have not yet been compiled;
check them before merging the final module and essay.

No Intel toolchain installation was launched: the live Local4.35 receipt arrived during the release lookup,
allowing work to move directly to the mathematical wrapper. Both workers confirmed Local as final posting
owner, GPT as final statement/essay reader; GPT edits the common/pulse source, Local the separate return staging
file. A generic Child predicate does not imply the function carrier is finite. The Nat-indexed pulse proofs
and genuinely finite cyclic return state must retain their separate premises and be bridged explicitly.

## GC2053 — rooted-return carrying read and joint integration

Read all164 lines of Local's RootedReturnExtension.lean atb5e55da2. The reset existence/uniqueness and repeated-
code descent carry. Actual finiteness is on two q-bit codes, and periodic_ext lifts code equality to functions.
Descent uses source recovery and reaches w0=w_(j−i) with j−i>=1; it does not require an infinite function type
to be finite. run_periodic's wrap at the reset uses periodic A,B and the actual black B(t0), so it closes afterq.
The childOf offset is nonnegative because q>=1, and periodicity shifts that run back to all natural times.

Integrated the extension into the actual-kit Rule30TemporalProfiles draft, reusing the shared Child/Periodic
and parent-uniqueness proof; Local's staging source stays unchanged. The kit pigeonhole supplies j<=2^(q+q),
so the joint headline retains the immediate coarse bound1<=k<=2^(q+q). This is existing finite-state counting,
not a useful normalized stage-growth bound. The historical qualitative theorem remains as a corollary.
The final combined wrapper/extension is not yet compiled: Local must validate it on the current kit and read
the small bound-retention/source-name changes before essay/PR/posting. The original staging compile remains
Local's reported outcome, not an independent Intel compiler run.

L1089 closes the old wrapper dependency: Local independently read and compiled c17bdd76 on Lean4.35, including
leftWindow_source_weight, leftWindow_pulse_bound, leftWindow_child and leftDiag_seed. Its separately validated
RootedReturnSection is a name/namespace adaptation of the reviewed extension. The current combined source adds
our reuse of generic parent uniqueness and the retained coarse bound; that final delta still needs validation.

## GC2058 — retain 4.35 failure and tested correction; notebook memory is stage-wide

L1092 reports the GC2055 linter-only first_pulse edit failed on current Lean4.35: simp decomposed the nonzero
sum condition and left an implication, with hne unused. That revision is not a validated release. The canonical
source now uses Local's tested correction: prove the actual modular expression nonzero, then simp [pulse,hne].
No hypothesis or theorem statement changed. Local reports a clean build/checker pass for that correction in
its scratch copy; the retained exact source and regenerated notebook still need the final execution receipt
and read. Do not repeat speculative cosmetic simplifier changes or treat the old assembly as passing.

Local also reported accumulated LeanLink environments in its session's MCP kernel:75GB footprint and39GB host
swap, then2.1GB swap and9.4GB free after stopping that kernel. These are reported Local-host values, not Intel
measurements or independently verified system peaks. A helper process cap alone missed the persistent kernel.
The next notebook stage must begin with a fresh session-owned kernel and end by stopping that same kernel after
retaining outputs. Include its PID/allocation in the stage-wide budget, check concurrent allocations, baseline
swap/pressure and actual headroom, retain post-stage teardown/headroom receipts, and stop on the agreed pressure
limits. Do not restart another session's kernel or rerun automatically. Local must state the concrete caps and
what monitors the MCP process before that next build; the earlier isolated Lean compile budget does not by
itself cap a separate Wolfram kernel. The owner already authorizes bounded validation, so no routine owner
permission round is requested.
