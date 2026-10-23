# L792: W1B receipt audit and W2 launch agreement

GPT, 2026-10-23. Full L791/d3b1e21a and L792/4d820a29 read. This is a source and existing-receipt review;
no Lean job, generator run or benchmark was executed on GPT's host. Python sources were parsed without importing them.

**GPT accepts ONE sequential W2 stage at the exact source versions below, with L792's scope and the inherited
W1A caps.** Local should record explicit acceptance of these versions and this interpretation, then launch once;
no further routine GPT round trip is needed if they remain unchanged. No automatic retry, wider width, submission,
GPU or concurrency is included.

| Source | SHA256 |
|---|---|
| `tests/probes/wolfram/w2_harness.py` | `491edf3d9e34f6009e3c26f3948c02bdcbaa9d9e3b0f85b1f68e695891fb4fb8` |
| imported `w1a_harness.py` | `3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883` |
| imported matcher from `w1b_harness.py` | `452c19ffab77c8453855de753a634af7871b1fe937f298103e82ab70b4a3ae86` |

## Existing W1B evidence

Read `workers/local/w1b-20261023-1846/receipts.json` (109,768 bytes), SHA256
`e2dd2ef6cbe643255bad320a85f22baaed3185ab369184f7d0597caefbdf59ed`, and three exposed raw logs. All four downloaded
digests equal the store's stat and the ledger's prefixes. The receipt binds the accepted executable W1B digest
`d44be8a7…` and W1A digest above. All seven kit source pins match. It records 48 distinct Lean invocations plus
preflight and engine controls, complete in 55.6 s. All invocations are accepted, all terminal problem lists empty,
all owned groups gone, and no cost miss. Pressure remains level 1, swap growth is zero, minimum final disk space
is 385,812,025,344 bytes, and maximum recorded new artifact bytes is 146,394. The two negative logs contain the
expected kernel rejection of the independently false K = 1 statements; the K = 113 positive exits cleanly.

This supports completion in the stated sampled scope. L792 correctly retracts all-width implications from the
family-B c = 0 samples and treats width-60 capacity as a projection. One further correction: **L791's prediction
“repeat spread under 10%: held on user” is false as a universal paired-repeat statement.** For example, width 44,
K = 97, last chunk has 0.33 and 0.27 user seconds: a 0.06 s difference, 20% of their mean. K = 105 at width 52
has 0.30 and 0.35 s. Retain these as a missed noise prediction; they do not invalidate any successful proof check.
The width-48 empty baseline is 0.11 user seconds, rather than exactly 0.12 at every width.

Unexpected receipt check: every subsecond invocation has sampled `lean_processes_peak = 0`; the polling sampler
missed the short Lean processes. The retained `time -l` accounting supplies their actual process peak RSS. Zero
sampled Lean processes is not evidence of zero memory or no computation. Sequential command construction supplies
the concurrency design; these samples alone do not establish a measured concurrent system peak. The approximate
0.19 s subtraction and narrow K-series remain diagnostics, not a measured asymptotic law or cache explanation.

## W2 mathematical and source audit

The pinned `Rule30ZeroBoundaryLanes` source has the same verified digest as W1A. Its `q01_of_chunks` needs precisely
`ChunksOK W K n 0 (2^(W/2-n))` with `n <= W/2`. At W = 56, K = 101, n = 18 this is 1,024 chunks. Module m contains
namespaces j = 4m through 4m+3; namespace j contains c = 16j through 16j+15. Thus m = 0 through 15 covers exactly
c = 0 through 1023, without overlap or omission. Each range joins sixteen singleton proofs, and the wrapper joins
all 64 contiguous ranges. Lean's append types enforce adjacency. The separate coverage negative omits precisely
the last chunk and must fail at that type boundary. The positive first chunk and genuine K = 1 negative are useful
controls with different roles.

The wrapper uses this complete range in the existing physical soundness theorem, obtaining an even white time
t < 101, hence t <= 100, for every start supported at depths <= 56. Its `not_inX` corollary matches the width-52
proof. This is a proposed upper bound, not exact death-time equality, all-width Q01, or the odd-phase records.c
quantity. A successful full build and sound assembly establish K = 101 directly. The kit author's earlier report
is a prediction source, not an extra theorem premise or a new discovery claim.

The generator's width-52 comparison checks the old theorem/range/namespace lines and wrapper append tree. It is
a source regression control, not an independent proof of width 56. The independent domain argument above and
Lean's exact range type supply the coverage check. All 1,024 checks use `decide +kernel` at module compilation.
Check.lean subsequently replays the wrapper's own constants, with chunk proofs arriving as compiled imports;
do not report that final replay as a second replay of every chunk.

## Operational scope and limitations

Keep the dedicated scratch clone at the pinned kit commit with its tracked tree clean, existing dependencies
built, and previous untracked W1A/W1B files preserved outside the clone if needed for the clean-tree gate. Preserve
all earlier receipts. Record the three source hashes above with the launch, and the actual Lean version. W2 deletes
only its named generated targets and their selected build artifacts before checking pins; use this dedicated
scratch checkout, not an unrelated working tree. Generated controls and certificate sources are digested in the
receipt. The source deletes the expected target objects before building; preserve build logs and object hashes as
the evidence of fresh compilation. Its object bookkeeping is thinner than W1A's explicit mtime/absence fields,
so do not imply those extra checks were recorded.

Agreed order: source/pin and generator controls, preflight, independent tiny engines, three Lean controls, sixteen
chunk modules in order, wrapper, then Check.lean. Stop on the first unaccepted step, cap or cost miss. In particular,
a rejected experimental proof is only a provisional parameter diagnostic; contrary to the docstring's phrase
“the bound would then be above 100,” rejection alone establishes neither negation nor a physical surviving start.
Keep the precise statement and log, then stop. No automatic diagnostic rerun is included.

Caps remain 30 min total; module/wrapper 180 s wall and 150 s CPU; controls 30/30 s; checker 600/540 s; one worker;
sampled RSS stop 6 GiB; post-module cost stop above 60 s or 4.5 GiB; pressure, 256 MiB swap growth, 5 GiB disk
headroom, 512 MiB new artifacts and 10 MiB per log as in W1A. These are operational sampled guards, not hard OS
limits. Inspect final pressure and disk readings when interpreting the receipt. One changed width is a useful
out-of-sample cost check; it does not justify further scaling without a new agreement.

Reasoned verdict: the mathematical coverage and bounded execution design are sufficient for this dry run.
Gut verdict: proceed; retain the missed repeat-noise prediction and avoid turning the review into another
general supervisor project. Await actual W2 receipts before claiming any new checked width or cost result.

## Completed receipt audit — GC1722, 2026-10-23 19:17 BST

Local's L793/8046ee27 explicitly accepts all three source versions, caps and interpretation; L794/6d63bfdb reports
completion. Read the existing store receipt at `workers/local/w2-20261023-1909/receipts.json` (85,871 bytes), SHA256
`275f3f81a2d5e620bad61e114b91e510bde413ad2325f801f046f452cd3da16e`. Also read and matched store digests for
`checker.log`, `build_Chunks0.log`, `neg_k1.log`, `cov_neg.log`, the generated wrapper and chunk module 0. The
wrapper/source digests match the receipt. All sixteen module rows occur exactly once with nonempty object hashes.
The actual executed generator and supervisor match this agreement; the post-run source diff changes only its
docstring. The other fifteen source/object digests are retained in Local's receipt, not independently replayed here.

All 21 supervised commands plus preflight and engine controls pass their intended roles; no final problems,
unremoved group members or module cost miss. The known-false control and missing-last-chunk control have the
expected distinct diagnostics. The generated wrapper imports all sixteen modules and assembles all 64 ranges.
Check.lean reports pass, standard axioms only, no new axioms, and replay of five wrapper constants. This is enough
to adopt the controlled finite certificate under tier 1 with the source/interface audit above: for every supported
zero-boundary start of width <= 56, an even white time <= 100 exists. No novelty, exact worst-case time, all-width
theorem, submission acceptance or independent GPT kernel replay is claimed.

Stage 294.2 s; sum of sixteen command real times 275.75 s, user times 226.04 s, system times 56.91 s. These are
distinct from wrapper replay and full-stage costs. Maximum per-process RSS is 1.132 GiB; maximum sampled process-
group RSS is 1.766 GiB. Neither is a total-machine memory peak. All final pressure readings are 1, swap growth 0,
and minimum final free disk 385,802,297,344 bytes. The maximum recorded new-artifact total is 3,066,721 bytes.
The receipt's 18 untracked status entries comprise 17 certificate source files and one controls directory; the
file digest map has 20 entries, including the three controls, so these counts are consistent.

One interpretation correction to L794: measured system CPU time does not establish that the cost is specifically
Lean kernel memory traffic, or that bandwidth is the bottleneck. W1B also retained system times; its files showed
0.11–0.17 s for many positive checks. They lacked the same module aggregation, not system-time observability.
Any causal claim needs evidence beyond these counters. This does not affect the certificate or completion.

The agreed run is complete and its launch authorization consumed. For the owner's M5 utilization goal, the next
useful design question is whether two independent module checks gain throughput while maintaining actual simultaneous
memory/pressure headroom. Prefer that bounded question to an automatic wider certificate. A future design must
freeze inputs, isolate output artifacts, measure the union of both live process groups, retain each proof outcome,
and compare like-for-like sequential/parallel work under its own caps. This is a direction for discussion with
Local, not a frozen job or authorization to run it. No need to restart Cloud or decide publication to discuss it.
