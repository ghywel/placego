# Arc-code components — compiled counting bound and uncompiled real draft

**Current status, GC2066:** ArcBreakBounds passed the first capped Intel4.33.1 compile; Local reports a clean
4.35 check. ArcDeterminantDraft is uncompiled and needs compatible Mathlib plus a frozen validation stage.
Neither is a full real-rotation/Rule30 submission. Dated specifications/results below preserve their scopes.

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
