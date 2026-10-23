# Standing GPU jobs: Metal compute for the prize (the owner's question, 2026-10-23)

**Status: standing list, not a priority.** The owner (2026-10-23, supervisory): we chose Rule 30 because it followed on
from the record's GPU interpolation shaders, yet nearly every test we run is CPU (C, Python, now Wolfram Language on
the M5). GPU shaders are not only for images: any data can go to a Metal compute job, and the M5's GPU does massively
parallel work the CPU cannot. Local and GPT are free to choose whether and when to take any of these; the list exists so
the idea is not forgotten and can be circled back to. Cloud wrote the jobs at the owner's request (CL606).

What a GPU can and cannot do for a proof. It cannot close Problem 1 or `Q01`, which are statements about every width.
It can push an empirical frontier far past the CPU, hunt for a decisive object (a counterexample to `Q01` would end the
period-2 case outright), and produce certificates that the Lean kernel then checks. The fit is a plain Metal compute
pipeline with **bit-sliced lanes**: one candidate per bit of a 32- or 64-bit word (the kit's own lanes technique for its
width-52 kernel check, `Rule30ZeroBoundaryLanes`), a hundred thousand threads each holding a word per cell, every rule 30
step a handful of bitwise operations per word. Not the interpolation shaders: a compute kernel over integer buffers.

## Relation to GPT-NEXT-M5-COMPUTE.md (added 22:37 BST, CL608)

GPT's note of 19:35 BST (GC1724, `GPT-NEXT-M5-COMPUTE.md`), written before this list, ranks three M5 compute designs.
They are the same family; this is the map, so that neither document is read without the other:

| GPT's item (GC1724) | Status | Here |
|---|---|---|
| 1. A bounded sequential-versus-two-worker certificate pilot | **DONE** as W4 (L802, GC1729): two workers give 1.8x on width-60 modules | Not a GPU job; its result feeds the kernel-cost side of the board |
| 2. A semantics-preserving early-stop checker (the kit's `run` advances all K levels after `alive` is zero; a short-circuit with a proved equality) | **OPEN**, no owner's word; appears in Local's menus (L812, L821) | **Job 0 below**: a kernel-side design, no GPU; it lowers the cost of every width certificate and of job 1's cross-checks |
| 3. A small exact CPU-versus-Metal survivor-engine pilot (the anti-diagonal reconstruction over lane words, 32-bit lanes mapped to the kit's chunk numbering, no floating point, exhaustive tiny-width agreement with a scalar engine, GPU identity and buffer caps read first) | **OPEN**, not started | **The pilot that job 1 requires** before any census: job 1 is GPT's item 3 taken to scale, under its discipline |

Jobs 2 and 3 below are not in GPT's note. GPT's three design gates stand for every job here: GPU speed cannot
accelerate the Lean kernel; an early-stop equality can still trigger costly reduction of the old definition; apparent
concurrency capacity cannot be inferred by summing process peaks.

## Job 0. The early-stop checker (GPT's item 2; kernel side, no GPU)

- **Object.** The kit's `Rule30ZeroBoundaryLanes.run` keeps stepping after every lane is dead. GPT's source reading:
  `alive` only ever stays or is ANDed, so zero is absorbing; a checker that returns at zero is semantically equal.
- **Work.** The equality lemma against the pinned definition, then a measured comparison on already-certified chunks.
  Prediction: work falls when the last survivor dies well before K. Can fail: late extinction, or the conversion
  path erasing the shortcut (GPT's gate).
- **Why it is here.** Every width certificate (W2 to W5, D-exact, the d-exact submission) pays for the dead levels; and
  job 1's CPU cross-checks run the same engine.

## Job 1. The Q01 death-time census to width 80 to 100 (first of the GPU jobs; the only one that could be decisive)

- **Pilot first, GPT's item 3 as written:** exact agreement between the Metal engine and a scalar engine at tiny
  exhaustive widths and with the CPU bit-sliced engine on frozen inputs spanning first/last chunks and word boundaries
  (31/32, 63/64); 32-bit lane words mapped bit by bit to the kit's lane and chunk numbering; no floating point;
  the M5's GPU identity, feature family and memory baseline read before any cap is proposed; explicit GPU buffers capped
  (GPT's example: 256 MiB) under a separate process-and-system pressure budget. Only a passing pilot earns the census.

- **Object.** The kit's `Q01`: every finite start of the zero-boundary left half (driven by the clock at column 0) has
  column -1 white at some even time. Kernel-checked to width 52 with death within 96 steps (`Rule30ZeroBoundaryWidth52`);
  the bound `2W + 8` is observed, not proved (the kit's words). A width-W start is fixed by about W/2 free bits (the odd
  free bits, the kit's `yFree`), so width 80 is 2^40 candidates of about 170 steps.
- **Kernel.** Each thread owns a block of lanes: the free bits of the lane index enumerate the start; the row is rebuilt
  sideways from the boundary column as the kit's checker does (`recon`, the anti-diagonal scan), or simulated directly
  as a zero-boundary half of width W + T; a lane dies at the first even time with column -1 white; the reduction keeps
  the maximal death time and the surviving lanes per block. Cost: a few 10^14 lane-steps at width 80, hours on the
  M5's GPU, impossible on a CPU.
- **Two outcomes.** If no start survives past the light cone and the death times follow the observed law, the record
  holds the sharpest frontier anyone has and a linear-front structure a theorem could capture. If any start survives,
  it is a candidate counterexample to `Q01`: hand it to the kit's `Rule30ZeroBoundary` definitions in Lean at once.
- **Prediction, to write before running** (corrected 2026-10-23 evening: the first version said D(W) = 2W - 8, which Local's
  D-exact lane has since refuted; D(52) = 96, D(56) = 100, D(60) = 114 exactly, D(64) = 116 a candidate, L810 to L820):
  D(W) stays below 2W for every width tried, with no survivor past the light cone; the GPU census should start above
  width 64, where the M5's kernel frontier now ends (Q01 kernel-checked to 60, W3).
- **Kill test, to write first:** the GPU kernel must reproduce the kit's table D(W) for W ≤ 52 exactly, and must
  report the known death time of the stripe family's exceptional tail (Ying Yin's `v = 1011`, `m` odd: no 31-step bound,
  death at 33190 for m = 33157) when fed that start.

## Job 2. The joint census of visible words (new object)

- **Object.** Submissions 10 and 11 bound the visible words (column 1 at even times under the clock) from the right half
  alone: at most C (R/D)^n words, 0.2445 bits per bit at width 14. GPT's task-1 note (GPT-CL594-WORDS.md) named the
  constraint never used computationally: under the clock the visible bits force the whole left half (column -1 from
  column 1, then leftwards by left-permutivity), and a finite configuration's left half is white beyond some depth L.
- **Kernel.** Enumerate the 2^n visible prefixes (n to about 36) as lanes; for each, rebuild the forced left row to
  depth L + n and test that it is white beyond L, and run the width-m right layer with free inputs (the channel
  automaton's acceptance) for n steps; tabulate the survivors S(n, L, m).
- **Outcome.** If S collapses much faster than (R/D)^n, that is the first evidence for a **two-sided channel theorem**,
  a new target on top of submissions 10 and 11, and the shape of the collapse says where the obstruction lives. If S
  tracks the one-sided bound, the left half adds nothing and the right half is the whole story.
- **Prediction:** the joint count is strictly smaller from n ≈ 2L on, by a factor growing with n.
- **Kill test:** at m = 12 and L large the census must reproduce the accepted-word counts of the width-12 automaton
  (2, 3, 5, 8, 12, 17, 25, 36, 50, 68, 91, 119 for n = 1 to 12), and at n ≤ 12 it must agree with a Python census.

## Job 3. The entropy trend of the channel bound

- **Object.** The certified rates are 0.316, 0.258, 0.245, 0.213 bits per visible bit at widths 10, 12, 14, 16. The
  question is whether they tend to zero. GPT's C program builds the automaton to width 28 on CPU (28 GB at 28; memory
  bound, not a GPU job); the growth rate at each width is a sparse power iteration the GPU does in seconds.
- **Outcome.** A fall like 1/m means the visible bits carry zero entropy in the limit, a theorem worth chasing; a
  plateau means the right half is free and the obstruction must come from the left, which points at job 2.
- **Kill test:** the GPU power iteration must reproduce 1.1956850, 1.1844186 and 1.1591 at widths 12, 14, 16 before
  any new width is trusted.

## Not a GPU job

Widening the kernel certificates (widths 16 and beyond). The verified checker is bound by the kernel's cost and the
notebook's size, not by how fast the automaton is computed (CL600 to CL605, GPT-CL601-WIDTHS.md).

## How to take one

Claim it in the ledger with the "If this holds, it changes X" line (X: Q01 for job 1, the channel row for jobs 2 and
3), write the prediction and the kill test first, keep the Metal source and the raw results outside git with their
digests in the record, and bring the numbers to the record as measurements, never as proofs. A survivor in job 1 goes
to Lean before anything else.
