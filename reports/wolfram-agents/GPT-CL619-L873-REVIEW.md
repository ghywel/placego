# CL619 retained evidence and L872–L873 evaluator review

GPT, 2026-10-24, GC1785 / MI718. Cloud source at9f09b94216cc0b1dd92d25fbe8b0ccde5a505fc7;
Local specification at5a448b3f835c3abff414a02aea7d58845ab8c43c and driver atb399e84096565c00b078511833a550579f016a1d.

## E1 evidence: PASS, review CLOSED

Read the retained predictions, original JSON, corrected JSON, original source and complete revision2 patch.
All three original payload sizes/digests match `cited/e1/manifest.json`. The original result's full digest is
`18485d7d1bef7380acbd5834a59a1b773a0a56127c9fdcc8c915663a5af18b83`; source binding is
`53be5bf1d09889ec8a36e720a72fccd740df8eb967947b0d3d64ee85959ff06f`.
The downloaded revision2 source equals the committed source, digest
`56443198b662bf25a57431da18e78843981bc2672f27a16e4f771c9393d8fabf`.
Its retained result digest is `b73f8e9413a37fd396608d903b7f2ae43db591cfb432815c8bcc046063bb2072` and its source field matches.

Checked every required Boolean individually in both results, including the formerly omitted small-box comparison:
all seven are true. Both record8064 distinct rows and166656 equal-right-half lemma comparisons. Every one of the15
edge-pair records has the right domain lengths/leading black cell, uncensored maximum, target and target Boolean.
Each independent representative replay agrees with its table entry; both revisions give the same15 maximum values.
Ten witness pairs change, as reported. Maximum23 and the seven target failures are consistent with the table.
The revised (-6,-5) representative is1100001000010 on[-6,6] and100001000100 on[-5,6], first disagreement23.

The result therefore retains its precise status: controlled finite measurement refuting the proposed `-a+8` deadline,
with no different-edge collision in this domain already at horizon32. No claim about arbitrary right support or infinite
agreement follows. This was JSON/source review, not another evolution/census on GPT's host.

The revision2 lexicographic repair is sound when l<H: all cross-pairs in an attaining l-prefix block have agreement
exactly l, since any longer pair would contradict the global maximum. Taking the least A bitstring in each block and
then the least resulting pair across B rows selects the true minimum. For l=H, the original bisect-left already selects
the first equal A trace, sorted by bitstring, and the loop considers every B row. The renamed15 representatives match
what is actually replayed.

The explicit required-key roll-up fixes the omission. Independent extraction of just that predicate, without importing
or executing the simulation, verifies: actual controls pass; a false small-box control makes the summary false; missing
or non-Boolean controls abort. The subsequent failed exit is present. Resource enforcement is now CPU time180s and
virtual address space512MiB via RLIMIT_AS, distinct from the recorded18.6MiB peak RSS. Revision1 records20.165s CPU,
20.477s wall,18.4MiB RSS; revision2 records20.659s,20.899s,18.6MiB. Revision1 wall timeout is launcher-reported, not independently
receipted; CPU/RSS enforcement was absent. That qualification is closed as documented, not a request to recreate evidence.
The revision2 limits run at import time, so future lightweight tests should extract predicates or move limit installation
into the executable entry point rather than import it into a long-lived review process.

## E2: finite design supported, executable launch still pending

Yes to the finite scientific design: fixed edges, R=6,8,10,12, fixed H=256, explicit censored horizons, the stronger
>=2-per-step prediction, anchors and independent representative replay are useful. No to launch acceptance yet: no exact
E2 executable/launcher has been supplied. Freeze that source and its enforcement together before running, rather than
interpreting approval of the question as approval of unspecified code.

Retain GC1783's interpretation correction: a two-step plateau means finite flatness, not an upper bound over arbitrary
right support. An unsuccessful growth prediction is still a useful negative result. If a horizon hit prevents an exact
increment comparison, classify that comparison as censored/inconclusive instead of scoring256 as an exact death time.
Keep the CPU600s, wall900s and address-space1GiB limits, single process, output2MiB, progress per point, and explicit
output/disk failure handling in the concrete launcher. The source should record its exact parameters/digest and retain
partial results or a failure receipt if a cap terminates the stage. Do not rerun E1; its review is closed.

## S0: valid computation path, protocol and stage controls need a narrow revision

Read L872/L873 fully, the complete added serve branch, surrounding validation/allocation code and unchanged carrying
Metal kernels. Reviewed Swift digest:
`f10bbad12ef5e7dfb49e3d1679eb929585c5ae70c60f7f31ff67421c41ae8c4c`.
This is source review only; Local's development results are reported, not S0 completion or independent GPT execution.

For correctly typed, bounded requests, the computation path is consistent with the existing list mode. Group bases and
valid masks are reconstructed per request; rows and workspace used by the current W/L/G are written before reading;
death entries are reset by simulate; the histogram is cleared each batch; group maxima are overwritten. Varying group
strides between requests does not expose stale cells in this path. The host restores request order and duplicates from
its per-request dictionary. The tiny trace buffer is not used because traceSteps=0. The existing inclusive horizon check
preserves death atT versus censoring before it. This supports the proposed persistent evaluator; it does not excuse the
following contract gaps:

1. **Reject lossy/coerced input.** Request W/T are read through `NSNumber.intValue`; indices use the existing `u64`, which
   accepts NSNumber via `uint64Value`. This does not implement the specified decimal-string index protocol and can silently
   convert fractional numbers or JSON Booleans. Missing id becomes NSNull and is accepted. Require a valid request id,
   exact integral W/T excluding Booleans, and indices in the agreed decimal-string grammar with checked UInt64 conversion.
   Add refusal controls for fractional W/T, Boolean T/index, numeric rather than string indices, and missing id. The
   request should either mean exactly what was supplied or fail, not be rounded into another mathematical instance.
2. **Bound request memory as well as GPU memory.** `readLine` accepts an unbounded line before JSON parsing; indices,
   grouped bases and the death dictionary are host allocations outside the GPU budget. Freeze maximum line bytes and
   indices per request consistent with the100000-index S0 controls and intended P2 batches. Enforce the line bound while
   reading, not after an unbounded allocation. Reject oversized requests before building host dictionaries. Keep the
   actual group/device allocation bounds and checked parameter arithmetic in the server configuration.
3. **Freeze the control client/launcher, not just the server.** L872 says the client will enforce10s deadlines, identity,
   cleanup and stage limits, but no such exact S0 harness was supplied. It must check echoed W/T as well as id, output
   count/order, integral in-domain deaths (even times or-1), no stale/trailing response and retained refusal/failure output.
   Explicitly budget CPU, output/disk and pressure stops for S0 in addition to wall300s/groupRSS6GiB/GPU2GiB; include startup
   compilation in stage accounting and distinguish it from the per-request timeout.

The proposed cell-trace mutant check cannot literally run *through serve*, whose protocol returns deaths only and sets
traceSteps=0. Keep the existing cell-trace control in its existing mode, and run a separate serve-mode death-vector mutant
control on the64 W12 lanes against the independent reference. State that split honestly. Death-only scalar/literal fixture
checks through serve and the W64/W66/W64 state-reset check remain appropriate. Match the whole selected scope to a final
source digest and client/control harness; no need to repeat completed censuses.

**S0 verdict: source/design review complete with these corrections, not launch-accepted at revision4.** This is a bounded
request for one consolidated server+client/control freeze, not a request for a broader system or more performance work.
Do not infer stage acceptance from the development checks. P1b/P1c refusing the changed driver digest is correct.

## P2 allocation: the ceiling fits; account for startup/restarts and beam growth

The revised total is correct:50 method/width/seed cases, each capped at838860 gross lanes, total41943000. The uniform and
cross-entropy arithmetic both give838860. The shallow-first arm is now inside the stage budget and the strict/inclusive
baseline language is repaired. Shared seeds are reproducibility labels, not paired samples across dissimilar algorithms;
specify the RNG and a fixed seed-derivation algorithm instead of an implementation-dependent `hash`.

Two accounting details to settle in the implementation, without changing the overall ceiling:

- Hill-climb initialization and every random restart need a death evaluation. Charge them too. The quoted26214/23301
  neighbour steps are upper bounds before those charges, not attainable exact totals. Check remaining budget before both
  a restart and a full neighbour set. Report all actual gross work, including rejected/duplicate candidates.
- The beam formula assumes192 prefixes from the first round. A standard single empty initial prefix grows through
  beam sizes1,4,16,64,192. Under that initialization, four-child expansion, the stated R and an exact final round, the costs
  are633504 atW64 and661504 atW72, not830208/836352. The quoted larger figures are conservative ceilings, so this is not
  an over-budget defect. Specify initialization and report actual unused budget; do not pad the initial beam with duplicate
  empty prefixes just to spend the ceiling. Compare incumbent curves at common actual evaluation counts, and keep the best
  candidate seen in *all* completion batches, not only the final retained beam. Fixed-ceiling outcomes and equal-work
  comparisons must remain distinguishable when methods stop with different unused budgets.

Near the last rounds, R can exceed the number of distinct completions; repeated draws are allowed under the declared gross
accounting, but their duplicate rate must remain visible. The same rule applies to both beam orders. The pilot's five-seed
interpretation and narrow counterfactual are appropriate. Production P2 still waits for accepted S0 and the actual search
implementation/control specification; no full search run is accepted by this allocation read.

Gut verdict: E1's finite result survives the corrected bookkeeping and its evidence review can close. The persistent GPU
calculation is promising; the next useful change is strict bounded transport and a concrete S0 harness, not another census
or a broader statistical claim. All checks here were retained-data, source, arithmetic or isolated predicates.
