# L797: W4 revision 1 design review

GPT, 2026-10-23 19:57 BST. Source review only; no benchmark, fault injection or kernel replay here.

**Verdict: the small matched pilot remains the preferred next compute design, but revision 1 is not launch-agreed.**
L797 at cbdcf2a7 and the complete 518-line harness were read. The reviewed W4 SHA256 is
`3e4758cc947ae3bcce248897c817b101e33fc576bb289d36d5e3587eaff43791`.
Its unchanged imports and explicit `INPUT_SET = None` preserve the existing hold. W3 continues unchanged;
its final receipt, source binding and checker outcome are still pending. Local's reported 2.08 GiB module peak
misses the prediction, not the agreed executable stop. No width-60 conclusion follows from progress alone.

The fixed two-module S1/P1/P2/S2 comparison, separate build trees, regenerated source hashes, fresh output checks,
eight retained compilations and a failed-gate outcome are useful. Keep that scope, the 600-second stage cap and
existing per-child, memory, pressure, swap, output and concurrency caps. No wider census is needed.

## Three corrections before freezing revision 2

1. **Use one process snapshot for the pair.** Lines 232–247 call `H.group_sample` once for each live child;
   each call executes its own `ps -axo ...` (W1A lines 186 onward). Thus the claimed single-snapshot aggregate
   is currently a sum of observations at different times. Parse both owned PGIDs from ONE checked snapshot,
   with its sample time, then compute the per-group and combined counters from that same data. Call it a sampled
   aggregate, not the exact system peak. The staggered-hold control distinguishes summed historical peaks from
   observed loads, but does not establish a common snapshot: its long separated holds pass either implementation.
   A deterministic parser/control with interleaved group rows and disjoint membership should exercise the shared
   snapshot and verify that only one process-list read occurs per sample. Keep the live staggered check too.

2. **Compare the same timing boundaries.** Sequential `b.wall_s` at lines 473–482 includes deletion, both
   `run_step` finalizers, receipt saves and output hashing. Parallel `pair.wall_s` at line 309 ends at the last
   observed exit and excludes its finalizers and output checks. Lines 505–506 divide those unlike quantities;
   merely reporting sequential overhead does not remove the bias. Freeze a common start/end definition for both
   modes. A simple honest primary metric is end-to-end batch wall from before target cleanup to after both output
   checks and terminal acceptance in each mode. Also retain child `time -l` real/user/sys and process-span
   diagnostics separately. Do not call the resulting ratio a kernel-only speedup. An overhead control should
   confirm the chosen boundaries include or exclude the same deliberately delayed operation in both arms.
   Keep the 1.3 threshold, but apply it to the explicitly matched primary metric.

3. **Make the new pair lifecycle survive partial startup and finalizer errors.** The aggregate counters,
   `stop_child` and sample count are initialized at line 221, after both spawns. If the second `Popen` raises,
   `finally` reaches uninitialized variables at lines 307–309 and cannot persist a terminal pair result. An error
   after `procs.append` but before the matching PGID/state append can also leave the ownership arrays misaligned.
   Initialize terminal state before opening/spawning; record each owned process immediately and keep its cleanup
   information together. Cleanup and finalization of one child must not prevent cleanup and terminal recording of
   the other. Preserve the original exception, finalize unstarted children as UNKNOWN, verify owned groups empty
   after cleanup, and persist the pair outcome even when a per-child matcher/finalizer fails. This is one pair
   lifecycle correction, not a set of extra acceptance booleans. Proposed adversarial controls are second-spawn
   failure after one live child, and first-child finalizer failure with the other still owned; both require a
   durable UNKNOWN outcome and verified cleanup, with no unowned process touched.

The missing-output control also needs an independent positive partner. Currently B already fails, so its pair
FAIL masks the fact that A's output check changes A only after the pair verdict was computed. Main execution does
separately stop on any child failure, so this is not a demonstrated false acceptance there. Still, recompute the
terminal pair verdict after output validation, and test missing A output with B passing. All stored verdicts should
agree. Keep separate build-error coverage if useful within the same small control stage. Check real paths/build
roots are distinct, not just two different textual paths. State explicitly that completed proof failures are
collected until the other bounded child exits, while resource/monitor stops cancel still-live owned children;
revision 1 currently behaves that way, which differs from an unconditional fail-fast reading.

## Priority and interpretation

I favor an ordinary-priority launch for BOTH modes, omitting the explicit `nice -n 5`, and recording the actual
inherited nice value. This addresses the capacity question while keeping priority fixed across S and P. If the
launcher already has nice 5 and cannot lower it without privilege, use a normal-priority launcher or retain 5
and label that policy; do not introduce privilege changes or a third comparison arm. This is part of the new
frozen specification, not a change to running W3.

Apple's [Apple-silicon tuning documentation](https://developer.apple.com/documentation/apple-silicon/tuning-your-code-s-performance-for-apple-silicon/)
and [performance/efficiency-core explanation](https://developer.apple.com/news/?id=vk3m204o) describe QoS and
system scheduling, including migration between core types. They do not establish that nice 5 pins work to an
efficiency core, or that nice 0 pins it to a performance core. Record core use only if observed.

Remove the claim that user-time inflation distinguishes bandwidth contention from efficiency-core scheduling.
Different core mix, clocks, thermals, cache effects and memory stalls can all change CPU time. The pilot measures
throughput, correctness and sampled memory headroom; these timers alone do not identify a bottleneck. Nor do two
selected modules establish a two-hour/four-hour width-64 runtime. Those remain projections.

## Owner's standing GPU list, CL606

CL606 at b15c2d99 (published in 70908a6a) and GPU-METAL-JOBS.md were read fully. The standing list is useful for
future choice, not a frozen job or a reason to overlap W3. Preserve Cloud's original text and attach these scopes
before using it to design compute:

- A finite-horizon survivor does not refute Q01. It needs an actual admissible physical realization and an
  infinite-continuation proof, such as a cycle in a proved closed finite-state model. A failed sufficient Q01
  route also does not, by itself, settle the full period-2 question in the opposite direction.
- The kit's roughly W/2 free bits parameterize its constrained reconstruction/check, not arbitrary physical
  width-W rows (which have W bits). Direct row simulation cannot silently replace that domain. Freeze the exact
  representation and prove the coverage/realization map before counting; retain phase and tail conditions.
- Width bounds are not exact maximum death times. The kit's W52 upper certificate does not alone prove D(52) = 96;
  independently validate the proposed sharpness and stripe control in the same phase/model. Neither a light-cone
  horizon nor a finite trend proves infinite survival or a uniform linear bound.
- GPU hours/CPU impossibility and a seconds-scale power iteration are unmeasured estimates. Include the full
  bit-plane/depth work and memory footprint. A 28 GB graph does not fit a 16 GB unified-memory machine merely
  because the GPU consumes it; streamed/implicit representations would be a different design.
- Numerical power iteration is a candidate generator, not a rigorous spectral upper certificate. Width-16
  arithmetic bounds and a full physical/Lean bridge have different status; the latter remains uncarried in this
  programme. A finite entropy trend does not prove a zero limit. Joint counts must compare the same accepted-word
  domain and finite-left constraint before interpreting an extra decay factor.

My ranking therefore stays: repair and freeze the small two-worker pilot first; a later small exact CPU/Metal
representation pilot could be worthwhile, without committing to width 80–100 or a memory-exceeding graph.

## Delivery and next step

Send the existing scratch dry-test receipt and its exact source binding if retained; the prose outcomes are read,
not independently replayed or adopted. Return one consolidated revision with the three corrections, matching
control plan, caps, input hashes bound to W3's actual outcome, and ordinary-priority policy. No additional fault
stage or benchmark is authorized merely by this design review; agree its exact executable version first. The
previous W1A supervisor review need not be repeated. No GPT duplicate run, Cloud job, automatic retry or submission.

Niggle sweep: simultaneous-memory claim checked against the actual ps calls; gate checked against both timer
boundaries; unexpected check follows failure of the second spawn before line 221. All three expose concrete gaps.
Reasoned and gut verdict: the small pilot can answer the owner's hardware question after these focused changes;
it remains useful, but revision 1 cannot yet support its claimed measurements or complete failure receipts.
