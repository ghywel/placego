# L879–L881: P2 revision 2 and latency pilot review

GPT, GC1790 / MI723, 2026-10-24 15:08 UTC. Full entries read at
`fcb0cd36298558333b29026df4da75115407bc98` (L879), `ce6d2b44dad1cecfde872f5b263afe37fe0fb504` (L880), and
`9fa9f04af05fcecbd211433bcdc4c93e7d5e9743` (L881). Complete P2, meta-control and pilot sources read.

**Choose (b), a supervised latency pilot first. Neither current pilot nor P2 production is launch-accepted yet.**
The main P2 correctness repairs carry at source scope; failure retention needs the narrow changes below. Do not rerun S0.

| File | SHA-256 reviewed |
|---|---|
| p2_search.py | 385c0d8bbb326bc13436b98b04afe5101887deddcd99cf51dbfa44744a0f20b3 |
| p2_controls_meta.py | cb122085065a498a2047e6bc3a2bcac11f7bf38236aaa3fec1dc1028a82a6e19 |
| p2_latency_pilot.py | c43e3881d212817da4b9199ae192cccc52ceca12ac32dafc73939fc38e82b116 |

## What now carries

The five RNG/method functions are byte-identical to the previously reviewed version. Scoring now saves contradictions and
fails; it distinguishes a legitimate nonmaximal near candidate from a false claimed maximizer. Pinned census bytes are
checked before and after the searches, contents validated only in the supervisor before launch and in scoring afterward.
First reach uses ordered position, with batch-end counts/time separately labelled. A censor stops before ranking and
retains indices/deaths in P2. S0/helper/source/binary/result bindings and strict shared transport are present. Zero-wait
polling checks buffered bytes and EOF; next-response identity and the final full quiet check remain. The final gate enforces
the exact cases/scored set, budgets, zero correctness failures and bindings; cleanup stays inside the inherited W1A group.
The bounded high-candidate store checks whether pruning touched D-4, rather than silently claiming full retention.

Extracted pure-file controls independently confirmed ordered position2 versus batch end3, censor retention without
ranking, and terminal rejection of seven scope/failure/binding mutations. No module job, subprocess stub, GPU, scalar
orbit search or Lean replay was launched. Local's 68 controls, seven meta-mutations and three pilot controls are reported
self-check outcomes; their source was read, their raw outputs not fetched or independently rerun. The meta-runner requires
the named guarding controls to fail, but only reports counts for other controls; its PASS alone does not establish that
all other controls passed. This qualification does not negate the reported development results.

## Required retention correction

P2's `Budgeted.__call__` calls the evaluator before increasing gross/requests or entering its progress-writing finally.
An extracted fake evaluator that records receiving indices[7,8] and then raises a transport Stop produces gross0,
requests0 and no progress line. The failed request's indices are absent from the interrupted case. The existing dead-server
control explicitly expects that omission. Successful prior requests are retained, and this failure cannot pass the gate;
the problem is evidence loss, not false mathematical success.

Retain a bounded attempted-request record before exchange, with width, horizon, request id, indices and attempted lane
count. Afterward record validated completion or the transport/contract failure (including bounded observed response bytes
where available). Keep attempted and validated counts distinct: do not pretend an unreturned result was evaluated or rank
it. Pending request evidence should survive an outer supervisor stop, so write it before sending, not only in the Python
exception handler. One atomically replaced current-request file plus a compact attempt/completion journal can suffice;
there is no need to save every successful request's full indices. Add a fake transport-failure check that asserts retention.

The latency pilot has a stronger version of this gap: `measure` accumulates timings in local variables and returns only
when both widths finish; `R['latency'] = measure(...)` commits nothing on exception. A W72 failure loses W64's completed
statistics too. Its local Budgeted censor witness is not attached to the receipt. Persist incremental per-width/request
progress and failure/censor evidence, including the successful first width if the second fails or hits the cap. Keep partial
results explicitly incomplete. Adapt the existing censor control to assert actual retained evidence, not merely an exception.

## Pilot interpretation and caps

The exact proposal is now180s wall/CPU, not the earlier under-one-minute sketch; 4400 requests at15ms already take66s
before startup, so that correction is sensible. The proposed6GiB sampled group stop,2GiB GPU budget,10MiB artifacts/log,
pressure/swap/disk guards, one server per width and no retry remain bounded. No increased scope is needed for this review.
The measured interval around `ev(idx)` includes Python transport/accounting as well as GPU work. Call it request round-trip
wall time, not GPU kernel time; report build/startup/end-to-end separately.

Do not use median step latency times all stub requests as the sole launch-cost estimate. Medians do not add into total
cost, restart latency is measured separately, and real fitness changes hill trajectories and their restart counts. Retain
median/p90/max as descriptive statistics, but add shape-specific mean scenarios and counts. With B=838860 and n=W/2,
step count s<=floor(B/n); restart count r<=floor((B+n)/(n+1)), since r<=s+1 and ns+r<=B. Thus the independently conservative
count bounds are:

| Width | Steps at most | Restarts at most |
|---|---:|---:|
|64|26214|25420|
|72|23301|22672|

A conservative-count scenario is five times the sum over widths of these bounds times the respective measured mean
latencies. The two separate maxima need not be attained together. This is still a timing estimate, not a latency upper
bound: random neighborhoods can differ from long-lived hill neighborhoods and future latency can vary. Show the original
stub-count scenario separately if useful; account for random/beam/CEM, scoring, build and cleanup before a full-stage
decision. Do not automatically launch P2 from a successful pilot or silently enlarge its5400s cap.

## Status and next action

Local can consolidate attempted-request retention, pilot partial evidence and the estimator clarification, then supply
exact revised source/pins and pre-run predictions. The narrow pilot is the next proposed execution; P2 production remains
separate. No automatic repeat of S0, completed GPU censuses or development controls is requested here.

L881's timestamp erratum is adopted: use the cited commit times rather than estimated headers; it does not change the
retained measurements. Its18-of19 Lean Verified summary is Local-reported status, not a new GPT output audit. Submission14's
automatic Lean/sandbox outcome remains distinct from the previously reported Human Verified label. Cloud's CL621 carrying
Lean module remains pending with Cloud; no duplicate formalization.

Gut verdict: the correctness repairs are substantial and specific. The useful next step is a small measured pilot with
honest partial receipts, not spending the full comparison budget on an unmeasured round-trip cost.
