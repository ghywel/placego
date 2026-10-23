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

## Job 1. The Q01 death-time census to width 80 to 100 (first; the only one that could be decisive)

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
- **Prediction, to write before running:** D(W) = 2W - 8 continues (D(52) = 96) and no survivor at any width tried.
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
