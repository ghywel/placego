# W3 width-60 design review — GC1723

2026-10-23. Full L795/67e09e4e and frozen source at 5485f527 read. This follows the owner's width-60 direction reported by Local; submissions remain withheld. GC1722's optional concurrency suggestion is superseded for the next job. No benchmark or kernel computation was run by GPT.

## Exact agreement

GPT accepts ONE sequential dry W3 launch, once Local explicitly accepts the following frozen versions and interpretation in the ledger. No further routine GPT round trip is needed if unchanged.

| Source | SHA256 |
|---|---|
| w3_harness.py | a38615dfebd5ba459c3c4b24fd11685875587c9a38c5b0d222062b6258a6e41e |
| w2_harness.py, imported generator | 1eded5f5a513f1605d668e4da0226b67a4abb15d528c65e9fd13148a857e3906 |
| w1a_harness.py, imported supervisor | 3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883 |
| w1b_harness.py, imported diagnostic matcher | 452c19ffab77c8453855de753a634af7871b1fe937f298103e82ab70b4a3ae86 |

The kit remains cc1e0e0e7c1ae8c971aec5c14aaabb47c7b8c554 with the seven pinned source digests and Lean 4.35.0. Dedicated scratch clone, new output directory, faults disabled, fresh width-60 objects and no concurrent Lean job. Preserve W2's sources/receipts outside that clone; do not erase the completed certificate to obtain a clean pin check. Local records the four source hashes before launch; the receipt itself records W3, generator and supervisor digests, while the matcher is bound by the launch entry.

## Mathematical scope and coverage

W = 60, K = 129, n = 18. Since n <= W/2 and 2^(30 - 18) = 4096, the kit's q01_of_chunks interface needs exactly c = 0 through 4095. Module m contains namespaces 4m through 4m+3; namespace j contains checks 16j through 16j+15. For m = 0 through 63 this partitions the complete interval without gaps or overlaps. The last namespace starts at 4080 and ends at 4095. The wrapper imports 64 modules and appends 256 range proofs; its balanced binary tree has 255 joins. The dependent ChunksOK types, not a numerical row count alone, enforce adjacency and total extent.

A complete successful kernel compilation and wrapper check therefore gives, for every zero-boundary start supported at depths <= 60, a white depth-1 cell at an even t < 129, hence t <= 128. The not_inX corollary uses the same even-time division argument already reviewed at W2. No prior bound at width 60 is required to propose K = 129. Neither exact worst-case death time nor an arbitrary-width theorem follows. D(52) = 96 is not established as an equality by the audited upper-bound certificate; keep the kit's even-time scope separate from records.c's odd-phase observations.

The W2 generator is imported without executing its main. Its literal width-56 globals do not leak into W3's output: W, K, N, module count and namespace count are passed explicitly. W3 binds its own matcher and headline. Runtime source changes from W2 are the new width/bound/counts, imported generator and stage allowance; the prior supervisor lifecycle review remains applicable.

## Controls, resources and interpretation

The existing W52 regeneration control, independent packed/scalar tiny engines and literal orbit witnesses precede the new checks. K = 1 remains a real negative control: an initially black depth-1 start cannot have a white observation at the only eligible time, zero. The missing-last-chunk type control must reject [0,4095) against [0,4096); a deliberately successful first chunk at the proposed K is required before the full modules. All controls and exact diagnostics are preserved. A rejected experimental proof remains provisional, not proof of a surviving physical witness or of the negated time bound.

Accepted caps: **60-minute total supervised stage**, increased from 30; module/wrapper 180 wall / 150 CPU seconds; checker 600 / 540; controls 30 / 30. One worker. Sampled process-group RSS stop 6 GiB, post-module cost-miss stop above 60 seconds or 4.5 GiB. Existing pressure, 256 MiB swap-growth, 5 GiB free-disk, 512 MiB new-artifact and 10 MiB per-log gates remain. Monitor failure, cap, control failure or unaccepted proof stops the stage; retain incomplete receipt, exact command/log and cleanup outcome. No retry, larger K, width extension, concurrency, GPU or submission is authorized. These are monitored operational caps, not hard OS-wide memory reservations.

The source sets H.CAPS['stage_s'] before constructing Supervisor, so the new deadline really is 60 minutes. All 69 supervised invocations (3 controls, 64 modules, wrapper, checker) retain the existing persisted-step/final-outcome policy. The final checker replays wrapper constants; the 4096 imported check theorems are kernel-checked during their fresh compilation, not replayed anew by that wrapper report. Require all module object hashes, generated-source hashes, checker JSON, controls, final counters and complete receipt before adoption.

The roughly 31-minute, 1.3–1.4 GiB predictions are extrapolations from narrow samples, not a K-squared runtime law or a memory law. User time above 0.6 seconds per chunk or process RSS above 2 GiB are retained prediction misses; the executable stop gates are the separately stated 60 seconds / 4.5 GiB and supervisor caps. System CPU time does not establish memory-traffic causation or bandwidth limitation. Per-process and sampled-group peaks are distinct from total-system peak. Accept K = 129 as proposed; there is no evidence requiring a larger margin before this one controlled attempt.

Unexpected check / niggle sweep: check that the fourfold domain growth changes BOTH module count and wrapper namespace count, and that the stage cap changes the actual deadline rather than only prose. Both pass by source inspection. The larger wrapper has 256 ranges but uses a balanced tree, and still has its own finite time cap; no unchecked cost assumption is needed. Reasoned and gut verdict: proceed with the requested dry width-60 test under these exact terms. Wait for actual receipts before promoting coverage.
