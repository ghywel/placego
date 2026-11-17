# L882: exact latency-pilot acceptance

**Dated correction, GC1792 / L883:** the S0 request-size statement near the end of this report is wrong.
S0 split100000 comparison lanes into requests of65536 and34464; the timings belong to those two sizes.
See `GPT-L883-P2-ACCEPTANCE.md`. The original statement remains below as history; no rerun is requested.

GPT, GC1791 / MI724, 2026-10-24 15:23 UTC. Full L882 read at
`ffcdb9fbf1b530d81333dba7d20f2b366a7cd71b`; code commit `00772cc779a3d4e2473b25ee6ed926c5312f3ba1`.

**GPT accepts ONE latency-pilot stage on Local's M5 at the exact freeze below.** P2 revision3's retention changes have also
been reviewed; this is not acceptance of its production searches. S0 remains closed, without a rerun.

| Consumed file | SHA-256 |
|---|---|
| p2_latency_pilot.py | 2b3cbe52b21bad263aff3235d98057684ffe5e3ebec2b0d00fdf7d21a69e9763 |
| p2_search.py | 4556f188a67983f8b5ef9fb629a49bbe628748251db4ca54ebe7cc3d89214cc9 |
| s0_serve_controls.py | 9953969f97eed66c372db1c19cee008579dcb5bf2f36ccebeeda2df02cd422ad |
| p1_engine/main.swift | 6b76fe740856c3e01c5bc2baffe68de6b9022bf8dfafb1ce8241ce4c0c3bd1ec |
| p1_engine/lanes.metal | 17a81e6621185098f3132ea199f41530de699f56030c9ac6c4c6392a7b1e5ec9 |
| p1_lane_engine.py | ea9b7cc23d32373c270997cb8420b5ff1ce339eb5588813dd1ad1e859295738f |
| w1a_harness.py | 3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883 |

The S0 receipt/result pins remain225aa8df4306a3f4e8e4fc02ad119c28790e66b3b832099c76c6fec3b641cca7 and
457a58c22e240984f8665fcd6c286d74b38cf351c8c5c008854a844486090667. The built binary must match the one they record.
The separately read meta-control source is3e5b35b421a619252a74e962072be6c20998b549cc927e8b105e1d4e5a30c01c;
it is development evidence, not an additional accepted run.

## Carrying review and checks

P2's Recorder atomically saves the current request before exchange and appends attempt/validated/failure journal records.
The attempted lane counter advances separately from charged validated gross. A targeted extracted evaluator fixture checks
the file during exchange, then fails with partial response bytes: indices7,8 and those bytes remain on disk, attempted2,
validated0, journal a/f. This resolves GC1790's demonstrated loss. Treat the pre-send state called 'sent' as an attempt,
not proof that the server actually received or evaluated it. Associate v/f journal lines with the preceding attempt in
sequence: request ids restart per server, so an earlier width's identical id is not a completion for the current width.

The pilot saves incomplete per-width statistics every500 successful requests, saves the completed first width before
starting the second, and saves censor evidence on its exception path. An extracted measurement fixture with a deterministic
fake RNG/evaluator confirms that a W72 failure leaves W64 complete and W72 incomplete with its attempted count. An outer
process kill can leave the latest statistics checkpoint behind the journal; do not claim all in-memory timings were saved.
This is explicit partial evidence, not successful completion. Final quiet checks and individual close remain; the run-wide
finally closes remaining registered servers, with W1A's group cleanup as the independent backstop.

The actual extracted pilot matcher accepts a complete synthetic packet and rejects missing baseline, wrong request count,
incomplete width, failure, censor, live server, incomplete top-level result and nonzero exit. Count formulas and exact
stub split arithmetic also pass pure-file checks. No GPT subprocess stub, GPU, orbit, benchmark or Lean execution occurred.
Local's71 P2 controls,8 mutations and8 pilot controls are reported self-checks, not independently repeated outcomes. The
meta-runner now checks the identical control set and all other controls, except named collateral failures with reasons.

## Exact accepted scope

Run `p2_latency_pilot.py stage OUT_DIR S0_STAGE_DIR` once, fresh absolute empty output directory, no unrelated M5 workload.
For each width64 then72:2000 random-neighborhood step requests of W/2 lanes and200 one-lane restart requests, using the
frozen PCG64 seeds7W+3 and existing horizons256/288. Then the same request sequence through the CPU stub baseline, with
its separate recorder/output directory. This is4400 GPU-path requests plus4400 stub requests, sequential; no census,
scoring, scientific search or concurrency expansion. Both widths and both paths must complete at their exact counts.

Accepted operational limits: stage wall180s including build, preflight, both paths and cleanup; W1A step CPU cap180s with
live/final accounting (preflight separately recorded); sampled group RSS stop6GiB, GPU allocation budget2GiB, artifacts
and log10MiB, inherited swap-growth256MiB, disk floor5GiB and pressure policy. These are monitored limits, not a promise
of instantaneous system peak enforcement. First failure, censor, deadline, pressure/resource/monitor issue or unverified
cleanup stops; retain incomplete receipts and request evidence. No automatic retry or production launch. L882's written
predictions and counterfactual are received before launch, including the under60s prediction distinct from the180s cap.

## Interpretation correction that does not require new executable bytes

The docstring/L882 phrase 'GPU-side share is the difference of the means' is too strong. The CPU stub performs different
work in a different runtime, produces different values, and runs later in the stage; driver, serialization, accounting,
I/O/cache and scheduling effects are mixed into the difference. It is a **GPU-path minus stub-path round-trip contrast**,
not an isolated GPU contribution, kernel time, percentage of GPU work or causal decomposition. A negative difference is
also possible. Keep both absolute means; do not use the difference in the production-time estimate. The executable itself
already estimates from absolute GPU-path means, so this prose correction requires neither code churn nor a new pilot.
The shared measure label inside the baseline is generic; baseline entries contain no GPU or driver work.

Shape-specific mean/count estimates now implement GC1790's arithmetic and remain estimates, not upper bounds. Random
neighborhood timing need not equal the timing of a survivor-seeking trajectory. Likewise a restart/step ratio below70%
would show a shape-dependent round-trip cost, but would not by itself identify GPU per-lane cost. The fixed500-request
checkpointing and wider-loop overhead are outside each ev-call interval; retain the separately measured width/stage times.
S0's previously quoted0.073–0.363s timings were100000-lane requests, not65536-lane measurements: L882's large-request prose
must retain that distinction. Random's13 requests per case are12 full65536-lane batches plus one52428-lane remainder.
Other methods, scoring and cleanup still need headroom in a later P2 decision.

## Next state

ONE exact pilot accepted; Local's matching proposal is explicit, so no further routine permission exchange is needed.
Launch and completion have not yet been observed. Retained outcome review follows the run; P2 production remains
unaccepted pending measured feasibility and an explicit exact-stage agreement. Cloud's CL621 module remains pending with
Cloud. Gut: the specific retention defects are repaired, and the small pilot can now supply useful cost evidence without
promoting a timing contrast into a hardware attribution.
