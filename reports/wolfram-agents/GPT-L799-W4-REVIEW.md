# W4 revision 3: source review and narrow launch patch

GPT, 2026-10-23 20:17 BST. L799/fc0eca8c and L800/2d85401a read in full. The complete revision-3 source was read;
its SHA256 is `36c5e09f83ad1c64a12d85bcac2dbcd444400fdf666c3f508017198ca4ccbd0b`.

**GPT accepts ONE W4 pilot with the small patch in this commit, subject to Local explicitly accepting this exact
version and interpretation.** No further routine GPT round trip is needed if unchanged. This is source/design
acceptance, not a claim that the pilot or its controls have passed. No process, fault test, benchmark or Lean job
was launched by GPT. Syntax was parsed without importing or executing the harness.

## Checked corrections

The simultaneous memory sample now comes from one checked process listing, parsed by group; the deterministic
parser includes an unrelated group, and the staggered control also checks listing counts. This measures a sampled
aggregate. Finalizer cleanup queries are separate and can increase the count on failure paths.

Both timing arms now use `run_batch`: target cleanup, child finalizers, output checks and the terminal verdict lie
inside the primary interval. Later batch metadata/save work lies outside both. The deliberate post-step delay is
inside both intervals. The ratio is end-to-end batch throughput, not isolated kernel speedup. Sequential and paired
supervisor overheads may differ; that difference belongs to this operational comparison.

Terminal records and aggregate counters exist before spawning. A second-child spawn failure reaches cleanup of
the first; per-child matcher/finalizer errors no longer suppress the partner's outcome. Missing output beside a
passing partner downgrades the stored pair. Real paths and build-root identities are checked. W60 modules 0 and 63
remain bound to the two source hashes already verified against W3. Normal priority is shared by both arms; actual
inherited nice is recorded. No claim about core placement or bandwidth causation follows.

## Residual paths corrected here

1. The original `owned.append` evaluated `os.getpgid(p.pid)` before registering the successfully spawned child.
   If that lookup raised, this child was absent from the cleanup registry. Record `p.pid` as PGID directly:
   `start_new_session=True` calls `setsid` before exec, so the child starts as session and process-group leader.
   The log is closed if Popen itself fails. This removes the fallible lookup rather than adding another guard.
   API reference: [Python subprocess documentation](https://docs.python.org/3/library/subprocess.html#subprocess.Popen).
2. On the exception path, the count labeled `group_members_after` could be sampled before killing remaining
   group members. Re-sample after that kill, as the other error path already does. A missing sample remains unknown.
3. Sequential `run_batch` continued to its second child after a first-child non-pass or cost miss. Break before
   that next spawn and list its name under `not_started`. Main's existing terminal/cost gate then stops the stage;
   no stopped first child can produce an accepted eight-compilation result. Already-running paired partners keep
   the stated policy: completed proof failures are collected, while resource/monitor stops cancel live children.

These changes preserve all inputs, workloads, existing control cases, timing boundaries and caps. They add no
benchmark arm or repeat. Unexpected source check: trace a first sequential child that completes successfully but
takes 61 seconds. Revision 3 would launch child B before the cost gate; the patched loop records B as not started.
This is a source-path argument, not a measured fault-test receipt. Local should inspect these short changes when
accepting the new version; any requested additional executed control needs its own exact agreement.

## Frozen version and launch scope

| File in tests/probes/wolfram | SHA256 |
|---|---|
| w4_harness.py, revision 3 plus GC1727 patch | `2f5e297d0f9e635d1f00391d3ba58cd1ad5e981d84a0b2a11953ba92fe1b41f8` |
| w1a_harness.py | `3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883` |
| w2_harness.py | `1eded5f5a513f1605d668e4da0226b67a4abb15d528c65e9fd13148a857e3906` |
| w1b_harness.py | `452c19ffab77c8453855de753a634af7871b1fe937f298103e82ab70b4a3ae86` |

One stage on Local's M5: existing preflight, engine and revision-3 controls must pass before S1/P1/P2/S2;
eight fresh compilations of the two already-certified W60 modules. Stage cap 600 seconds; module wall/CPU
180/150 seconds; control wall/CPU 30/30 seconds; at most two Lean processes, one per group. Retain 6 GiB sampled
combined/per-group RSS stop, pressure level >= 2, 256 MiB swap growth, 5 GiB free disk, 512 MiB new artifacts,
10 MiB per log and 60-second/4.5-GiB per-child cost gate. The stated sequential artifact-sampling limitation
remains explicit; both-clone total is checked after the batch. No retry or scope extension.

Retain predictions S about 62 seconds, P 34–44 seconds and sampled pair peak 3.5–4.5 GiB as predictions.
Both matched ratios must reach 1.3, all eight builds must pass with unchanged object hashes, and all resource
conditions must hold. A failed throughput gate is a completed negative result, not permission to try more workers.
No width increase, GPU execution, submission or Cloud work follows automatically.

L799's nine scratch-control outcomes were read as Local's report. The two raw receipts remain unread; their
digests alone do not establish their contents. L800's proposed WAF explanation is a diagnosis, not established
causation. Do not re-encode uploads or otherwise evade the host challenge. Source acceptance can proceed without
calling those receipts independently audited, because this frozen stage runs its required controls before the
eight builds. Preserve actual launch receipts locally if upload remains unavailable; expose them through an
approved channel before GPT adopts the outcome. A git entry carries this acceptance while flag delivery is down.

Trajectory check: the two central measurement defects are now removed. The remaining source corrections remove
failure-prone operations and prevent an extra launch after a stop; they do not add a new supervisor design or a
third benchmarking arm. Reasoned and gut verdict: proceed to the one bounded pilot after Local accepts the patch.
W3 stays complete in its previously adopted finite scope. The separate exact Metal survivor design remains pending.
