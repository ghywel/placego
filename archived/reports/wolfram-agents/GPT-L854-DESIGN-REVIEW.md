# L854: notebook supervisor design review

GPT GC1770 / MI713, 2026-10-24. Full L854/80c0fb224bf59d5e24b1087371ff5d367eb6826f and
L853 addendum35192400bfb45ae34d599f676c9b55170ffe8870 read. Relevant existing W1A run_step,
finalize, group_sample and kill_group source reread against GC1765. Design review COMPLETE WITH CORRECTIONS.
This is neither an executable review nor exact job agreement. No code, control batch or run requested tonight.
Honor Local's research rest; there is no promise the next implementation is the final review round.

The single main loop, no tracker thread/lock, and signal handler that only records an interrupt address the
specific W7 self-deadlock mechanism. Keep this direction. Make the following lifecycle requirements explicit
before freezing a later implementation and its separately agreed controls/production scope.

1. Interrupt lifetime must cover the whole active stage, including setup, between steps, finalization and terminal
publication. Restoring default TERM/HUP between steps does not implement STOP plus a persisted receipt; default
termination can bypass that path. INT's default behavior also differs. Use one stage-owned, non-raising flag handler
through final persistence, or an explicitly gap-free equivalent. Save and restore the previous dispositions at the
outer boundary, not assumed defaults. Preserve the first interrupt; repeated signals cannot clear it or turn failure
into success. Check the flag before spawn, immediately after spawn, after child exit, after finalization and before
committing success. It is not sufficient to check only inside `while proc.poll() is None`: a signal plus a fast exit
can skip that loop. Do not reset a stage interrupt at the next run_step.

2. Move ownership and exception protection around the complete spawn transition. Existing W1A calls Popen and then
getpgid before entering its try/finally; merely adding a flag check leaves that exception window. Initialize process
state before the protected region; once a child may exist, failures in PGID acquisition, sampling, matcher, accounting
or persistence must still reach the one bounded cleanup path. A failed spawn before a child exists must also leave a
non-success receipt. Preflight ownership and its cleanup belong in the same stage-level contract.

3. A numeric PGID retained while a Python step is open is not by itself a proof of current ownership. A fast leader
can exit and be reaped before finalization while the logical step remains open; comparing only numeric PGID afterward
does not establish identity. Specify what maintains the owned group's lifetime through the last possible signal, when
it is retired, and what happens when identity cannot be established. Do not signal historical or uncertain groups;
UNKNOWN is preferable to guessing. An explicit live launcher/anchor design is one possible direction, but its lifetime,
reaping order and cleanup would themselves need review. A group scan also cannot establish that descendants never
created a new session/group: bound the claim to the execution contract or provide a concrete containment mechanism.
This is a design obligation for the proposed new supervisor, not a reopening of completed W1A jobs.

4. Define watched-path states without an exists-then-stat ambiguity. Distinguish permitted not-yet-created from
unreadable/invalid and terminal-required missing; define symlink/replacement and nonregular-file policy for exact OUT
paths. Check the final size after process cleanup, not only once per second: a child may write an oversized output and
exit between samples. Keep the full-cell gate's own size/binding checks. Sampling plus terminal checks is still not an
instantaneous OS byte limit, and the report must say so. A terminal missing or unreadable output cannot pass merely
because no live sample observed it.

5. Keep COMPLETE as the last atomic state transition after all accepted steps, cleanup, accounting, output binding,
full-cell gate and final interrupt check succeed. Prepare the success record only for this commit; if persistence fails,
exit nonzero and leave the previous durable incomplete record. Attempt a failure receipt without claiming that it was
saved if storage itself fails. Never print DONE before successful publication. Restore handlers only after reaching a
terminal state. Cleanup errors must not mask the original stop; no remaining phase may launch another child after one.
Copy/submission are distinct: no submission before full output/KernelCheck acceptance and the separately recorded owner
permission. A RESULT OK marker alone is not that acceptance.

Controls to specify later (not authorized to run by this note): deterministic seams before/after spawn registration,
instant child exit coincident with interrupt, interrupt between steps and during finalization, repeated signals,
monitor failure after leader exit, watched file oversized on immediate exit, stat error/missing terminal file, terminal
save failure, and no signaling after ownership retirement. The current delayed-signal stand-in alone does not force
these paths. Keep controls bounded and preserve failing receipts. Default compatibility must mean more than the old
suite passing: changed handlers/finalization can change default behavior even with watch_paths=None. Freeze a new
supervisor version for the notebook rather than silently replacing the digest used by existing accepted callers.
The name W1B already denotes an earlier benchmark lane; use an unambiguous new supervisor identifier.

No production caps are newly accepted here: the next exact proposal must restate source digests, executable, stage and
per-step caps, CPU accounting scope, memory/pressure/swap/disk/output limits, concurrency, stop conditions and control
scope. Do not infer them from the prior declined W7 versions. This design read can wait for morning implementation;
no automatic fourth patch-and-run cycle, notebook restart or D5b experiment follows.

L853 correction follow-through is closed at selected scope: measured floor mass replaces exact halving; conditional
median occupancy is not near-universal; user3.31+system0.03 seconds are child time, not stage CPU. Artifact growth
8256/17199/26207/35277 bytes and final folder37483 bytes supersede the truncated figures. Raw receipts remain unverified.
W6 control outputs unavailable, request closed without rerun. Other selected audits remain closed. Cloud quiet.

Unexpected check: the child exits before the loop can observe an interrupt or oversized output. Gut: the architecture
is simpler; make the lifecycle contract precise before code, then assess one frozen implementation without haste.
