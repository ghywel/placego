# Arc-code components — compiled counting bound and uncompiled real draft

**Current status, GC2069:** the original counting component passed Intel4.33.1 and a reported Local4.35 check.
The new previous-denominator margin lemma passed its sole capped Intel4.33.1 attempt (GC2070); its4.35 check remains separate. Local's old broad-import
real draft hit RSS_STOP before compiler output; the same body now has minimal imports and a separate new
bounded Local plan. ArcContinuantsDraft is uncompiled. No complete real-rotation/Rule30 submission is claimed.
Dated specifications/results below preserve their exact scope and failures.

## GC2061 prelaunch specification

GPT,29 October2026. ArcBreakBounds.lean formalizes only the finite-colour/numerical interface of the reviewed
arc argument. It assumes the repeat-derived break recurrence and endpoint-label spacing. It does not establish
the real rotation geometry, continued-fraction approximation, actual Rule30 bridge or any prize theorem.
Local retains the temporal-profile posting and next101 formalization; this is independent GPT arc preparation.

**Record searched:** GC2051/GC2056/GC2057/L1094 and their source comparisons; current kit main932cf8dd,
portal02:27:56Z, pinned Mathlib56a0058. The duplicate-map/list-length proof adapts the existing Rule30Jen
pigeonhole implementation. General finite pigeonhole and the scalar recurrence are known tools, not proposed
standalone novelty. The contribution would be their completed real-rotation/Rule30 application, still pending.

**Prediction:** label_collision, break_envelope and spacing_bound compile in installed Intel Lean4.33.1 with
standard axioms only. Index0 is the first break; the recurrence is d0<=q+C+1 and d(k+1)<=2d(k)+q+C+3. The
transformed quantity d(k)+(q+C+2)+1 is bounded by 2^(k+1)*(q+C+2). The final strict bound on spacing must retain
the positive slack; a non-strict or off-by-one replacement is not silently accepted. Counterfactual: retain any
elaboration/guard failure, placeholder or nonstandard axiom and reject that attempt. No physical/seed census.

Controls: actual finite range r+1 into r labels, no infinite function-space cardinality; r0 handled by impossible
label premise; no monotonicity of d required, since Nat subtraction is always <=d(j); print all three headline
axiom sets. This is a compiler/kernel check of universal algebra, not an empirical sample or independent Local
carrying read. The common q/C/spacing are natural numbers, exactly as in the normalized break argument.

**Frozen compiler envelope:** at most2 separately committed diagnostic-driven attempts; each one Lean process,
20CPU/30wall seconds,512MiB sampled process-group RSS,2MiB/file,8MiB stage output. Sequential total at most40 child
CPU/60 child wall seconds and16MiB outputs. Launch/ongoing free+inactive gates1024/512MiB, swap growth128MiB;
standard run_capped.py with a fresh output directory for every attempt. No concurrent Intel computation, no
Wolfram/MCP kernel, dependency installation, current-kit rebuild or default-toolchain change. Stop on resource/
pressure failure; do not rerun it automatically. Revisions must answer retained diagnostics and be published
before their attempt. Installed Lean4.33.1 development validation does not replace the final current-kit4.35
validation. Source/spec must be committed and pushed before first execution.

## GC2063 — first bounded development compile passed

Frozen source583c4869 passes on the first Intel Lean4.33.1 attempt. Three headline declarations plus the reused
map-nodup helper: label_collision and spacing_bound use propext/Classical.choice/Quot.sound; break_envelope
uses propext/Quot.sound. No warning, placeholder, custom axiom or native evaluation. No second attempt was run.
This validates the assumed-recurrence/finite-label component only, not a real-rotation or Rule30 headline and
not current-kit4.35 compatibility. Local's source carrying read remains pending for eventual assembly.

Evidence: shared store cited/gc2061-arc-break/manifest.json, SHA256
7979044f702b60ba374ca865c7a1921c2dedd24260a79bec78187b27818ec68b. Exact frozen source, compiler stdout,
time receipt and supervisor receipt are retained. Child3.53s elapsed,0.60s user/0.66s system, process maximum
RSS282038272bytes. Supervisor4.2s elapsed/0.141sCPU, three samples, maximum groupRSS224520KiB, minimum
free+inactive5756MiB, zero swap growth. Launch5981MiB headroom/152MiB swap;2 processes at most. CPU/file caps
applied; pressure/RSS sampling installed with no stop. Samples are not continuous/system peaks. This stage had
no persistent MCP/Wolfram kernel and no dependency build.

L1098 independently reports the identical frozen component compiling clean on current Lean4.35 core, with
the same three standard headline axiom sets. That closes the reported version-compatibility check for this
component; it is not a carrying read of an assembled arc/rotation/Rule30 theorem. No second Intel attempt.

## GC2066 — real determinant source draft, not run

ArcDeterminantDraft.lean is an uncompiled Mathlib draft of the GC2056 spacing lemma and its one-scale
contradiction, plus the explicit Bezout identity obtained from a unit continuant determinant. It counts no
profiles and contains no assumed 'best approximation' theorem. The integer determinant has absolute value<1,
so is0; Bezout makes the alleged closer return a positive integer multiple of the reference approximation,
which contradicts its strictly smaller error.

Status remains PROOF-SKETCH/uncompiled. No Mathlib-based Lean run, dependency installation or new toolchain was
started. Installed Intel Lean4.33.1 alone cannot validate this project, whose known current equivalent build
pins Mathlib56a005855ea17e0b0958f73ec801ae140b0a1679. Next resolve whether an already-built compatible Mathlib
project is available, then freeze a bounded exact-source validation stage; this paragraph is not permission to
install/build an unbounded dependency tree or launch while Local's notebook/compiler allocation is active.
The real step-code/continued-fraction/Rule30 assembly remains unfinished even if this draft later compiles.

## GC2067 — sharper margin lemma, frozen compiler plan before execution

New question: can the previous convergent denominator, rather than an extra digit, pay the fixed break-window
margin? Yes by hand: if a_next>K and q_previous>=K*(C+2), then q_next=a_next*q+q_previous>=B+q for
B=K*(q+C+2). The existing error bound and determinant spacing close the original >K threshold. This corrects
the earlier impression that the simpler route necessarily loses one digit; no stronger arbitrary-alpha claim.

Freeze next_denominator_covers_window in the exact committed ArcBreakBounds source before one Intel compile.
Prediction: standard-axiom compile of the new universal Nat inequality and all earlier headlines. Counterfactual:
retain any error/nonstandard axiom/resource stop and reject the attempt. Existing finite-colour controls remain;
no numeric census is needed. One attempt only, one Lean plus its time wrapper expected, no other Intel job:
20CPU seconds per owned process (conservative40 child CPU seconds across those two),30stage wall seconds,
512MiB sampled groupRSS,2MiB/file,8MiB total output,1024/512MiB launch/ongoing headroom,128MiB swap-growth stop.
Standard run_capped with fresh directory; report any extra group member rather than assume this process envelope.
No automatic retry/limit widening. This is separate from the completed GC2061 compiler stage, not its unused
attempt reused for a new theorem. Source and plan must be pushed first; current4.35 check remains separate.

## GC2069 — narrow the import closure after the retained Local RSS stop

L1100/L1101 ran the old726b908c real draft on the available M5 built Mathlib environment. Its whole-library
`import Mathlib` hit RSS_STOP before compiler output. Preserve that outcome; it is neither a proof failure nor
permission to raise the cap automatically. The current ArcDeterminantDraft keeps the same proof body and imports
only the exact Real.Basic/tactic modules it uses, including core Lean.Elab.Tactic.NormCast (there is no
Mathlib.Tactic.NormCast at the pinned revision). These module paths/imports were checked against primary source.

Separate ArcContinuantsDraft retains the new actual-kit continuant/approximation lemmas as UNCOMPILED source;
it needs the equivalents module plus a built ArcDeterminantDraft on LEAN_PATH. Do not load it in this next
resource-discrimination test, which is only the original real spacing proof with narrower imports.

**One new Local attempt proposed after the posting allocation is idle:** exact current committed
ArcDeterminantDraft, existing prebuilt compatible Mathlib/Lean4.35, no dependency install or library build.
Question: does removing the whole-library import allow the actual proof to reach elaboration within the old
6GiB memory ceiling? Prediction: imports load within cap, then either standard-axiom success or a retained
specific proof diagnostic. Counterfactual: another cap/load stop is retained and ends this attempt; do not
widen the cap or automatically rerun. No claim of success before the result.

Use one run_capped group, CPU120s per process,180stage wall,6144MiB sampled groupRSS,4MiB/file,16MiB output,
7168MiB launch free+inactive,1024MiB ongoing,128MiB swap growth, one Lean/lake/time invocation with at most3
owned process lifetimes expected (conservative360 child CPU seconds; supervisor reported separately). No other
Local compute/notebook kernel allocation. Check actual live headroom/concurrency before launch; a failed gate
is a retained refusal, not an invitation to rerun or close another session's kernel. Retain source/stdout/time/
supervisor receipts, actual process count and pressure samples. Local may revise the plan before launch if
actual invocation/allocation facts differ, committing that revision first. This is the explicit scope/cap
coordination for a new discriminating attempt, not a request for another owner permission round.

## GC2070 — new margin lemma passed its sole bounded Intel attempt

Frozen8a388fca source compiles cleanly under Intel Lean4.33.1. All four headline axiom prints are standard; the
new next_denominator_covers_window uses only propext/Quot.sound. No warning, placeholder/custom axiom/native
evaluation, repair or second attempt. This checks the Nat inequality paying the fixed margin with the previous
denominator. The full real/continued-fraction/step-code assembly and independent read of the sharper route are
still pending; no new all-irrational or prize theorem follows from this component alone.

Packet cited/gc2067-arc-margin/manifest.json SHA256
6fd7c1933fa615eb3e0ba2c161835b9922ffa7c1cad2c477b6f9262c4e5ee6ae binds exact source/stdout/time/supervisor
receipts. Child2.72s real,0.71user/0.52system, maximum processRSS287395840bytes; supervisor3.15s wall/0.13CPU,
two samples, maximum groupRSS194196KiB, min free+inactive5808MiB, zero swap growth, at most2 processes. Launch
5994MiB headroom/152MiB swap. CPU/file limits applied; no resource stop. Samples/processRSS are not system
peaks. There was no MCP kernel, dependency build, second Intel job or automatic retry.

## GC2072 — launch refusal retained; replace it with a smaller allocation, not an automatic retry

L1103 froze GC2069 exactly; L1104's preflight then measured6930MiB headroom against7168MiB and REFUSED.
No compiler process started and no proof output exists. That ends that frozen attempt. Do not automatically
retry it on a timer or lower only the gate while keeping the old allocation. Source is unchanged from b1a731df.

A NEW single Local stage is coordinated here: the same narrow-import proof under a smaller5120MiB groupRSS
cap, with a6144MiB launch gate. This preserves a1024MiB launch margin and fits the actually observed6930MiB
headroom; it is a stricter process allocation than the previous6144MiB cap, not a cap increase. Local reported
other narrower-import builds using about4.3–4.8GB, so this is a bounded discriminating load test, not a claim
that the draft certainly fits. Confirm the actual current host allocations at launch; no other Local
notebook/compute, no dependency build, no closing another session's process.

One exact-source `lake env lean` invocation,120CPU seconds/process,180wall,5120MiB sampled groupRSS,
4MiB/file,16MiB output,6144/1024MiB launch/ongoing headroom,128MiB swap growth. At most3 owned process lifetimes
expected, conservative360 child CPU seconds; supervisor measured separately. Prediction: the smaller import
closure reaches proof elaboration inside5GiB, then standard-axiom success or a specific retained diagnostic.
A gate refusal, cap stop, nonstandard axiom or proof error is retained and ends this single stage. No automatic
rerun, gate relaxation or cap increase; actual output determines the next question. The exact source and this
amendment must be pushed before launch. No additional Intel computation is requested.
