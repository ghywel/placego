# L875 S0 exact-stage review

GPT, 2026-10-24, GC1786 / MI719. Reviewed full L875 at
a47fa17ad8cc4c3f4891fb00795f9f6c501ee0a2, the complete 290-line client,
revision5 Swift patch and surrounding allocation code, and the carrying W1A group-monitor/cleanup paths.

Pinned bytes independently hashed:
- Swift: `4a6cda6031625dabce3c0ed051d4ef3fc88c2c03cfffbb4c94267bdbc64c97dd`.
- S0: `bfcb4f46fe1c15ace495d0b46089fac9e010524f09f9430ce0dae42a1a5e6e23`.
- Metal: `17a81e6621185098f3132ea199f41530de699f56030c9ac6c4c6392a7b1e5ec9`.
- W1A: `3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883`.
- Consumed P1 Python helper: `ea9b7cc23d32373c270997cb8420b5ff1ce339eb5588813dd1ad1e859295738f` (recorded by S0, not enforced as a pin).

**Verdict: full source/stage review COMPLETE WITH CORRECTIONS; this S0 freeze is not accepted for launch.**
The Swift request limits and decimal-string parsing address the earlier defects within this frozen configuration.
The POSIX-read change resolves the described full-chunk wait. The bounded reader checks oversized lines before JSON
parsing, with at most one read-chunk overshoot. Death/trace mutant routing now matches the interfaces. The finite
control scope is appropriate; no census expansion is requested. Local's 27/27 development run remains reported evidence,
not an agreed stage or an independent GPT replay.

## Carrying integration defects

1. **The persistent GPU server escapes the supervisor's group.** W1A creates the stage step in one session, samples only
   its PGID, and kills only that PGID on a stop. `Server.__init__` then uses `start_new_session=True` again. The actual GPU
   server is consequently outside the advertised live group RSS/CPU guard and cleanup. A W1A kill can leave it alive;
   graceful client cleanup is not available after SIGKILL. There is also no run-wide `finally` closing all live servers:
   a comparison failure, JSON decoding exception, or list-mode error can strand one. Fix the ownership model at this
   integration boundary. The simplest option for this single-process server is to inherit the W1A step group and use
   per-child terminate/kill/wait for normal client cleanup (do not retain `killpg(server.pid)` after removing its session).
   Keep W1A's outer group cleanup as the last stop. If separate groups are retained, the outer monitor must explicitly
   account for and clean them; a client-only registry is insufficient. Retain a cleanup-failure outcome if death cannot
   be verified, and protect the entire live-server lifetime with cleanup on exceptions.

2. **The request deadline starts after an unbounded write.** `send_raw` performs one raw unbuffered pipe write, ignores
   the returned byte count, then flushes. Raw writes can be short; a blocked reader can also stall the call before
   `_line(10)` begins. Use a write-all loop with a shared request deadline and readiness/nonblocking handling, including
   the oversized-line refusal control. Bound the response buffer as well and drain or file-capture stderr so a full
   stderr pipe cannot deadlock the server. Persist bounded diagnostics. These are transport controls, not GPU trials.

3. **Response-contract checks admit malformed echoes and trailing data.** Python numeric equality accepts `True == 1`
   and `64.0 == 64`; `check_response` does not require exact integer types for the echoes or an actual object/list shape.
   `no_trailing` returns true when partial extra bytes arrive without a newline and can also treat an early EOF as
   quiet success. Validate shapes and exact types before comparison, reject any extra buffered byte, and distinguish
   live silence from unexpected EOF. Refusal controls currently require only an `error` key plus nonzero exit, despite
   the docstring's exact-key promise. Check the error schema and the appropriate echoed or null id as well.

Cheap adversarial checks executed by extracting only the client methods with AST (no import side effects, child process,
GPU or evolution): Boolean/float echoes produced an empty problem list; a fake sink returning a seven-byte short write
left the request truncated; the trailing-check predicate accepted a retained partial buffer. These independently expose
contract gaps. The group-ownership failure follows directly from the two `start_new_session` calls and PGID filter;
no deliberately orphaned process was created to demonstrate it.

## Complete the same freeze, without adding scientific scope

Pin the consumed P1 helper too: its engine build, reference functions and GPU budget are part of the reviewed job.
Make the final matcher require the exact named control set and Boolean passes, not merely `all` over whatever keys are
present (which is vacuously true for an empty map). Save failure details before cleanup, including generic transport and
JSON exceptions; preserve already recorded checks. Test client faults with fakes or a small protocol stub: short write,
blocked input, malformed response, partial trailing bytes, and a forced failure while a server is live. Such controls
should demonstrate the repairs inside the next exact proposal, not silently launch another GPU run.

The declared wall/CPU300s, RSS6GiB, GPU2GiB, artifacts50MiB, inherited swap256MiB/disk5GiB/pressure policy are explicit.
Their applicability to the GPU process is the current blocker, not their numerical size. No arbitrary256MiB GPU ceiling
is introduced. No request to redo completed P1/E1 work. P2 allocation corrections are acknowledged as adopted in L875;
actual P2 implementation remains pending. Submission15 is now **Local-reported Lean Verified**, distinct from Human
Verified; its source/output sign-off remains closed.

Gut verdict: the mathematical controls are sufficient in shape; fix the transport and process ownership before trusting
this stage as a resource-bounded evaluator test. This is an integration review, not evidence against the GPU calculation.
