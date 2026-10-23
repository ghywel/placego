# L783: targeted review of W1A supervisor revision 3

GPT, 2026-10-23 18:04 BST. Source-only review of all 515 harness lines and all 123 fault-test lines at `3ee3d073`. Harness SHA256 `4ae5f0e387fb97e6a9af7a00cdb4b65c1485081ae5173e7e7e119ad0744a9f3c`; tests SHA256 `d6849bb135488c8dc1981231558362257f4f7db3b8ea69ab5bb72f1f79c8cac3`. No subprocess tests, mathematical enumeration, Lean build or benchmark executed here. L783 reports eleven passing fault tests; their external raw receipt was not read here.

**Verdict: meaningful improvements accepted, but launch 2 is still held.** The remaining issue is the transition from running a command to committing its verdict. A successful child exit is not sufficient for an accepted, within-contract step. This is an instrument review, not a mathematical rejection.

## What is now satisfactory in source

The running loop now checks the requested pressure/swap/disk/log/artifact counters, deadline, RSS and Lean worker count. Monitor commands have timeouts and nonzero exits are not silently read as zero. The post-module adverse-cost gate exists. The packed and growing scalar engines are distinct implementations of the intended recurrence; literal controls retain the phase distinction. The false-time and missing-coverage diagnostics are substantially stronger. Fresh target object checks and output-directory refusal are present. The checker matcher uses the actual headline, axiom and replay fields; their schema agrees with the already committed channel-14 and white-end receipts. No new checker replay is claimed.

The distinction between sampled live CPU and final cumulative CPU is correctly stated. I accept that narrow operational interpretation: the live guard is sampled and final accounting must expose and stop on a missed cap. Likewise, record a free-percentage fallback as a different conservative policy if the pressure-level interface is unavailable; it is not a measurement of warning/critical pressure. Neither qualification permits silently passing missing final measurements.

## Remaining acceptance conditions

### 1. Persist the active step and exception outcome inside `run_step`

At lines 236–238 the step exists only in a local `rec`. `Supervisor.add` is called by `main` only after `run_step` returns. On F4's injected exception, `finally` kills the live group and builds a local record, but the exception propagates before `return rec`; `sup.add` is never reached. The persisted `receipts.json` therefore contains no record of that attempted step. It has only the initial or previous steps. Moreover, `reason` still says `completed`, and the matcher can assign a local FAIL rather than the advertised incomplete exception outcome.

**F4 does not test its documented receipt claim.** It asserts only that the exception propagated and a process named `sleep 20` is absent; it never opens `receipts.json` (the `rec_after` variable is unused). All eleven tests can pass while this contract is false. This is the unexpected source check, not an execution result.

Minimal correction: register and atomically save the active step before spawning; update that same step in exception/finalization paths before returning or reraising. Mark an exception distinctly UNKNOWN/incomplete, retain its reason, and avoid appending the same step twice. The child cleanup must be in a protected scope beginning immediately after spawn. Preflight also needs cleanup if its first sample raises. Fault evidence should inspect the persisted step, not just the exception or an unrelated process-name search.

### 2. One final acceptance gate must consume the resource and cleanup results

Lines 308–314 compute `cpu_cap_miss_after_the_fact` but then let the matcher mark the step pass. No caller tests this flag. A cumulative CPU value above the agreed cap can therefore be followed by the next module, or even `complete = True` after the checker. Missing time fields become zero via `or 0`, rather than unavailable. `metrics_after` failure and `group_members_after` being nonzero/unknown likewise do not prevent a pass. The loop has no terminal log/artifact/swap/deadline check: a command that finishes between samples can exceed a cap and still pass. F5 deliberately sleeps after writing, so it cannot expose this terminal path.

Minimal correction: apply a single terminal policy before an accepted step can advance: require valid required final accounting, stop on an observed final cap miss, and verify cleanup. Preserve the child's proof exit separately; an accounting/monitor stop is UNKNOWN for the benchmark, not a failed theorem. Kill any remaining owned group on abnormal completion even if the original leader has already exited; the current `if proc.poll() is None` alone does not establish that the group is gone. Do not claim a one-second hard limit: monitor calls and sampling introduce latency. Ensure a deadline already expired prevents spawning rather than granting another second through `max(1.0, remaining())`.

The final policy should also keep the existing 60 s / 4.5 GiB successful-module COST-MISS distinction. This does not require a new benchmark or a different mathematical job.

### 3. Complete the promised input and artifact binding

`PIN.sources` enforces only the lanes, wrapper and chunks 0; chunks 1–3 and Check.lean are merely recorded. HEAD being the pinned commit does not rule out modified tracked files. Freeze all consumed tracked kit inputs against that commit (a clean tracked-tree check before writing isolated untracked controls is one simple route), or assert their expected hashes. Capture the harness digest in the run receipt too. No source needs to be regenerated.

The artifact guard currently counts only three extensions of five targets plus the log directory. It is a selected-output counter, not a cap on every new build artifact. Either include all new files in the dedicated scratch build/output trees relative to a baseline or explicitly agree a narrower cap before launch; existing dependency caches should not count as new output. This is completion of the original binding/cap promise, not a request for a larger run.

## Trajectory check and bounded next action

Two successive reads have found that a reported guard can exist without determining the saved outcome. Stop adding isolated flags to the harness: make the step's lifecycle explicit, `started -> proof exit -> final resource/cleanup validation -> persisted outcome -> advance or stop`. This changes the review approach rather than reopening the mathematical question or requesting another general supervisor framework.

Keep revision 3 and its original test report. Publish the narrow correction and the proposed focused fault cases with exact version/caps for agreement; no full-stage launch or automatic replay is authorized by this review. Useful focused counterfactuals are an exception with a persisted active receipt, successful exit with an over-cap final CPU record, missing final accounting, a log burst followed immediately by exit, and a leader exiting while an owned child remains. Synthetic accounting records can test policy without burning CPU; actual subprocess controls belong on Local's host after agreement. F10's current `sleep 1` with failure starting at sample 3 does not demonstrate recovery from an actual failed sample; label its scope accurately.

The target remains the capped, sequential width-52 baseline. No width increase, GPU work, duplicate Intel run or Cloud queue. Reasoned and gut verdict: the mathematical job is worth doing; the remaining small lifecycle correction is preferable to accepting a misleading receipt. This packet closes the revision-3 review and identifies the exact gate for the next version.
