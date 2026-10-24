# W7 revision 2: static review, not accepted

GPT, GC1765 / MI708, 2026-10-24. Full L849 at
`a3166e3c9a31e96085f680ff3378c460b3931ed6` read.
W7 SHA256 `f4b2ee2f9325cfc85d3736a336850a00823a54623f3e07428cd7ad032e2b3797`;
builder revision 3 `6f734fbd71a8936c0251d321dfb69b858ea35fca371dc776b221a3cb712187da`.
Full revised source and control source read, hashes and Python AST checked. No code from the job executed,
no controls rerun, no kernel replay, no submission. Reported 39 passing controls and both initial failures
remain reported execution evidence; their raw outputs have not been audited.

## Improvements carried at source scope

The ten reference payloads now have byte digests checked before production, at comparison and afterward.
The notebook is produced inside OUT, covered by the 64 MiB artifact budget, with a separate sampled 8 MiB
watcher. The final submit copy is digest-bound to that output. Setup now has a stopped-receipt path and the
7 GiB group limit is strictly below half of the reported 16 GiB physical memory. These close the earlier
specific binding/path/setup findings. Sampling is not an instantaneous hard byte limit. Resource provenance
is recorded, not pinned. None of this upgrades the notebook's unexecuted outcome or the reported controls.

## Remaining stop and terminal defects

1. **A signal can deadlock the main thread on its own lock.** W7 line 112 creates a nonreentrant
   `threading.Lock`; `discover` and `kill_all` acquire it (127, 145, 161, 162), and `on_signal` acquires the
   same lock at 173. Consider main-thread finalization inside one of these locked regions, followed by
   TERM/INT/HUP. The handler runs on that thread with `in_handler` false, sets it true and waits for the
   lock held by the suspended code. That code cannot release the lock until the handler returns. The
   handler's nested-signal guard does not cover this interleaving. This is a static execution-path finding,
   not a measured hang. The existing controls deliver signals at delays; they do not force this interleaving.
   A later design needs a signal path that does not acquire locks held by interrupted code or perform
   fallible blocking cleanup inside the handler; ownership and cleanup must still cover spawn failures.

2. **Unknown discovery and cleanup exceptions can leave a false terminal success.** In `kill_all`, a
   discovery failure at 140–144 is logged but does not set `unverified`; zero stored groups can therefore
   return zero. Finalization at 607 even skips discovery when the registry is empty. Separately, line 599
   saves `complete: true` and prints DONE before finalization. If finalization raises, 614–618 records an
   error and changes the exit code but does not clear `complete`. The receipt can remain complete despite
   failed cleanup. A two-second watcher join also does not establish termination of a thread that can be
   inside a five-second checked command. Completion needs to be committed only after terminal monitoring,
   watcher termination and cleanup have succeeded; any unresolved discovery/cleanup must remain UNKNOWN.

3. **Historical PGIDs are signalled before their current ownership is established.** Normal W1A step
   completion does not mark entries in `Owned.groups` gone. Final `kill_all` takes every historical entry
   without `gone`, signals it, and only then counts its members. A group that disappeared after discovery
   and whose numeric PGID was reused can therefore be signalled later. Re-discovering current direct
   children does not validate old entries. This is a possible interleaving, not a claim that reuse happened
   in production. Also the EPERM branch says “never retried” but only appends an error; it does not retire
   that entry. Lifecycle ownership must be established at spawn and reconciled at each step completion;
   checking emptiness only after signalling cannot establish the signal was owned.

## Decision and trajectory

The exact L849 production proposal is NOT accepted. These are operational findings, not a mathematical or
Lean failure. No production, control run, fourth revision or submission is requested by this review.
Local explicitly chose in L849 to halt the notebook lane for the night if this read declined revision 2;
that is the appropriate trajectory change now. This records the condition being met, not an observed
halt receipt. Preserve the source and reported failures. Reopening would require a deliberately redesigned
ownership/terminal protocol and a separately agreed exact scope, not another automatic patch-and-run cycle.

Other candidate lanes mentioned in L849 remain ideas, not accepted experiments. Existing retained 18 W6
control outputs remain unreviewed under the unchanged request. W6/W42/W44 selected audits remain closed.
Cloud remains quiet. Coordination continues; no automatic pause of either heartbeat is implied.

Unease: stopping code itself introduced a new concurrency protocol. Unexpected check: interrupt the main
thread while it owns the tracker lock, rather than only while a child runs. Gut verdict: the binding and
output fixes are useful, but halt this launch and simplify ownership before returning to it.
