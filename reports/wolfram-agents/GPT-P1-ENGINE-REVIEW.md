# P1 engine review — GC1778

2026-10-24. Owner requested one source review with the remaining budget. Read
L863–L864 and all three engine/harness sources through 6f9efe73. Both GPT
heartbeats remain PAUSED. No GPU job, census or kernel replay run by GPT.

**Verdict:** PASS on the core algorithm and bounded P1 control design, for the
reviewed W<=64, T<=256, 32/64-lane settings. The proposed W64 P1b census is a
reasonable next measurement, with the finalization requirements below. This is
not acceptance of widths 66–72 or of a census harness not yet present in the
checkout. The actual P1 pilot already ran under the owner's afternoon direction;
this review does not retroactively claim GPT launch agreement.

## Reviewed source and evidence

- lanes.metal SHA256 17a81e6621185098f3132ea199f41530de699f56030c9ac6c4c6392a7b1e5ec9.
- main.swift SHA256 8649a5983df144fae99305a7eb689037d76ea9b932540d193a69ca51a913004e.
- p1_lane_engine.py SHA256 e4549116d53679b618e0f448b830a45a1df95b539f4c530f5dd4fa154a7f3945
  (current text includes the reported outcomes; differs from the executed harness
  digest quoted in L864).

Ran the existing CPU-only `--controls`: all eight checks PASS, including the
small reconstruction bijection, literal hand fixtures, three known witness
deaths, planted Sparse16 violations, censored handling, dump decoding and all
4096 width-24 lanes against d1. This took under one second. The reported 71 GPU
checks, receipts, timings and cleanup have been read in L864, not independently
replayed or fetched as raw receipts here. Source/control PASS and reported GPU
outcome are separate evidence scopes.

## What carries

The trace constructor uses the corrected odd-time coordinates. Its two-column
in-place reconstruction reads the old needed entry before overwriting it. The
forward kernel carries old[k-1] and old[k] in registers, reads old[k+1] before its
write, includes the newly advancing edge, preserves a white wall and an initialized
halo, tests death only at even ordinary times and stops without stepping past T.
The valid mask participates in death, censoring and all-dead checks. The reviewed
index shifts are in range for W<=64. Per-group finite maxima and censored markers
are coherent with the host's histogram and maximizer extraction.

The reduction has a useful independent CPU path. Threadgroup-local counters are
cleared before the barrier; all dispatched threads reach the final barrier;
finite deaths and censored lanes each contribute exactly once. For P1b, a batch
has at most 2^19*32=2^24 lanes, so its UInt32 histogram bins cannot overflow; the
host aggregates into UInt64. Do not infer that this covers arbitrary batch sizes.
The host's equality check between histogram total and valid-mask population is
worth retaining, along with independent coverage checks in the census runner.

The cell-by-cell edge trace and dropped-edge mutant are particularly useful:
the mutant could preserve the maximum while corrupting individual lanes. The
pilot tests more than a reassuring maximum. The one-buffer implementation and
two-column workspace also resolve the earlier two-buffer memory objection;
2 GiB is a legitimate revised explicit budget, subject to actual headroom.

## P1b: requirements for one trustworthy W64 census

The checkout contains the P1 pilot harness, not an executable P1b runner. The
following are concrete requirements for that runner, not a request for another
round of prose drafting:

1. Freeze the three source hashes, binary hash and job JSON. Use W64, T256,
   32-bit lanes, G<=2^19, GPU budget 2 GiB, the stated W1A resource stops, 900 s
   total wall/CPU and 120 s per engine call; include ALL reference generation,
   scalar checks and finalization within those stage caps. Only W64 is in scope.
2. Cover [0,2^32) exactly once with 256 batches of 2^24 lanes (or the same exact
   union in 8 calls of 32 batches). Record disjoint contiguous call/batch ranges,
   source/version binding and total 2^32. Check returned W,T,range,mode,word width,
   mutant-empty, histogram sums, lane counts and result status; reject missing or
   duplicate ranges. A plausible maximum does not establish coverage.
3. Gate the batch-0 full d1 comparison BEFORE the remainder is trusted, and check
   scalar samples for each call before continuing. Retain failures and offending
   lanes. The announced 64 samples are presently “up to 64 distinct” after the
   driver's deduplication; either fill back to 64 unique valid indices or record
   the actual count honestly. Every engine or comparison error stops the stage.
4. Require `censored==0` before reporting exact numerical D(64). `max` is the
   maximum of known finite deaths even when censored lanes exist; it alone is
   not D(W). Censoring at 256 is an unresolved outcome, not a finite maximum.
5. Aggregate `max_count` across all calls, and test `maximizers_truncated`.
   The driver retains only the first 4096 maximizer indices. If truncated, retain
   the count and report the witness list as partial, or stop/extract the rest
   under the same cap. Never silently say “all maximizers checked”. Verify every
   retained maximizing start by the scalar engine and validate_witness, and the
   relevant complete d1 chunks as proposed. Stop on any disagreement, including
   missing expected known witness; retain it as a diagnostic, not a new table row.
6. Keep the 32 MiB full dump and d1 reference work bounded, delete disposable dumps
   after digest/comparison, and enforce the 100 MiB artifact limit across the
   entire stage. Save final status only after all checks and cleanup. No automatic
   retry or move to W66 follows from a P1b pass.

A W64 agreement would be an independent forward-evolution numerical census;
it remains distinct from the kernel-certified upper bound. Both engines share
an indexing/reconstruction interface, so the independent scalar/hand fixtures
remain essential. A disagreement might be indexing, reduction, coverage or data
binding, not necessarily the Rule 30 step itself.

## Small source limitations to fix or fence explicitly

- **Actual latent memory-safety bug outside P1b:** `reduce="cpu"` bypasses the
  T<=4092 histogram guard, but the SAME simulate kernel still updates `th[t/2]`.
  Long CPU-reduction jobs can collide with the censored bin and eventually write
  beyond HB=2048. Apply the bound to BOTH modes, or compile a genuine histogram-
  free CPU-reduction kernel. P1b's T=256 is safe; this does not require rerunning
  its already completed P1 controls. Add a cheap refusal check for large T.
- Validate positive G_max, supported W/Wsup, nonnegative trace_steps<=T and the
  index-width domain. The current driver is designed for trusted fixed JSON,
  not arbitrary parameters. For this stage fence to W64/T256 with trace disabled;
  later widths and modes need their own checks. Check all buffer sizes as well
  as the row buffer when expanding scope.
- Death dumps use host-native byte order while the reader specifies little
  endian. That is consistent on the measured Apple host; record the format as
  little endian if the files become portable evidence.

## Interpretation of the outcome

The reported 79 M lanes/s and 3.5x comparison are useful measurements of these
implementations on one W60 range. `wall_total_s` begins AFTER Metal compilation,
host range construction and buffer allocation; the CPU comparison includes pool
startup and requests record=True per-lane levels, while the dump-free GPU timing
returns mostly aggregate data. Keep those boundaries explicit. This is not a
universal 3.5x advantage over an optimized all-core histogram census. Record total
stage wall alongside engine timing. Early-death distributions at later widths can
change throughput; the extrapolation is a prediction, not a cap adjustment.

The core engine and controls are materially stronger than the original draft.
I support the bounded W64 independent-check direction. Exact launch agreement
still refers to the actual frozen census runner/specification, or to explicit
owner direction; this source review grants no broader sequence of censuses.
No routine reply loop requested under the owner's budget constraint.
