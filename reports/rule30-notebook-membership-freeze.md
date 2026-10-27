# GC1988: L1034 direct membership source review and one-run freeze

Owner requests Local response review and continuation. Complete199-line proposed driver reviewed, together with the existing CNF constructor/replay, full supervisor and GC1987 specification. L1034 withdraws the unconditional sampling inference. One amended execution is assigned to GPT on Intel; Local must not duplicate it. Schedules stay paused.

## Mathematical target and decisions

P=00010101 at100, R=01010100 at100, each in table and OR/XOR encodings. Only without accepted P100 SAT, ask P99 in both. At most6 external calls,4 if P100 supplies a checked witness. The clamped wall is t mod2, visible ages are half physical time. Fixed left boundary is not a naturally evolving left half. All arbitrary right initial rows in the needed causal cone are included; beyond-cone zero completion is valid.

L1034's original acceptance discarded valid SAT+UNKNOWN pairs. Corrected: either encoding's model, after every-clause and every-physical-cell checks, establishes existence; UNKNOWN on the other encoding does not undo it. SAT versus UNSAT stops for disagreement review. Two UNSAT answers are recorded as solver-reported, not independently proof-checked. No DRAT checker runs in this stage. P100 implies P99 andQ100 by already-carried nestedness and shift; these are derived conclusions, not extra solver outcomes. Failure or timeout never counts as absence.

M1: P100 andR100 possible, closing the finite short-word gate. M2: Local expects at least one timeout with roughly50% subjective confidence; corrected interpretation allows a successful other encoding to settle that word. Counterfactual: dual reported UNSAT at99/100 would be finite evidence of a late death requiring certificate checking before promotion. No numerical trend proves infinite survival or a finite presentation.

## Source review, controls and retained evidence

The two encodings share only the prescribed rule: the table excludes every wrong local assignment, while the second adds exact OR plus XOR clauses. Boundary phases and visible unit-clause offsets were read. Replay checks all cone variables, not only the observed word. The retained P98/R99 rows induce physical assignments for both encodings; auxiliary OR variables follow the exact encoder loop order. Their four clause controls must pass. Flipping the last word bit must violate the corresponding unit clause. Previously completed GC1977 tiny exhaustive and restart controls remain evidence for the unchanged constructor, not claimed as rerun here.

Before freeze, added hard six-call guard, CPU accounting after construction/before launch and after each result, verification of solver RLIMIT_CPU application, pending-query checkpoint and top-level failure receipt. Eight stubbed decision-path tests passed (SAT/UNKNOWN accepted; both conflict orders stop; no solver or research queries). Unexpected check: P99 pruning depends only on a clause-checked and physically replayed P100 SAT witness, never a timeout or an unchecked exit status.

Input cited/l1030-witness-pilot/latest_witnesses.json:15620 bytes, SHA256 ef0ff89cfeee5c4f13def41b9df493d76e5b55f358a1487a27296bffbbccdf90. Existing digest-verified local copy. Frozen hashes:

- `notebook_membership_stage.py`: `6c9329c90e40c846b14ebd7343fa810e2dd7a2a291cbb32a7064018b84ae0297`
- `notebook_death_gate.py`: `6e51527c1198218ed6d1f50e57c09a922ae29713b5bb2258298e7c763f9ff5ee`
- `run_capped.py`: `38ed7189ce5911d06e03e50295995d2a1d5c15451db9367da5cdbf299d2fef6c`
- Kissat4.0.4 executable: `259293810ecf77418cb737d506715e83010855836283c820f6b5be001f6d5838`.

Record searched: GC1987 exact review/specification, GC1979 outcome and unchanged gate source, L1034 entire entry/source. This continues the selected membership question, not a new census or sampler.

## Total bounds and actual enforcement contract

One Python driver plus at most one single-threaded Kissat child. Each solver30s CPU hard limit and30s wall timeout; Python subprocess timeout kills/waits for that solver. Aggregate own+completed-children CPU admission guard210s, repeated after results; this is an admission/accounting guard, not a kernel-enforced210s process-tree ceiling. Each admitted call has its own30s limit. Driver RLIMIT_CPU210s, stage wall300s, group RSS512MiB sampled, disk256MiB sampled/final and per-file64MiB hard. Launch free+inactive4096MiB, stop below1024MiB or swap growth256MiB. Supervisor CPU reported separately. One-second sampling has polling/command latency and is not an instantaneous system-peak limit.

Largest cone has23220 cell variables at H214 and23005 transitions; OR auxiliaries add23005 variables. Control/solver construction is bounded by these loops; no repeated accumulation of full cones between solver calls. CNFs, proof files and stdout fit only while the declared output limits hold; oversized proof or other limit stops do not trigger retries. Keep every CNF, output, DRAT, model/cone witness, decision, failure and supervisor receipt. Input files are fixed small external data, output directory fresh, bytecode disabled, no network during execution. No proof checker, longer timeout, new sampling, further age, or automatic subsequent stage.

Invocation: PYTHONDONTWRITEBYTECODE=1 python3 tests/probes/wolfram/run_capped.py --out "$RUN_DIR" --cpu 210 --wall 300 --rss-mib 512 --file-mib 64 --disk-mib 256 --launch-free-mib 4096 --min-free-mib 1024 --swap-growth-mib 256 -- python3 -B tests/probes/wolfram/notebook_membership_stage.py "$INPUT_FILE"

Publish this source freeze and execution-owner flag before launching. Read actual receipts, independently replay every retained positive, and retain negative/timeout scope after the single stage. Independent Local review remains available for the resulting claim.
