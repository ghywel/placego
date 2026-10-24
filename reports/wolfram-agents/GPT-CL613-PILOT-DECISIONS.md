# CL613 pilot decisions — GC1776

2026-10-24. Read CL613 and §J at 6e1af39d, fetched through 1c626fdb.
One consolidated follow-up at the owner's request. Both heartbeats PAUSED.
No implementation or run approved; design review only. The earlier corrections
are useful, but “executable scope” still needs executable source/version binding.

## Direct answers

- **P1: NO as written.** Correct the finite-row evaluator contract, especially
  the live-edge/ghost-cell indexing, and fit the batch to the stated memory cap.
- **P2: NO as written.** It depends on a validated P1, and needs one aggregate
  budget covering seeds, training, evaluation and all CPU survivor extensions.
- **P3: NO as written.** Cap the complete experiment, including control generation,
  validation and final inference, rather than training alone; make its positive
  control demonstrably predictable by the baseline being tested.

These are specific remaining defects, not a request to reopen all prior design.
Apply the fixes below in the implementation; freeze source, scope and caps before
launch. No need for another prose-only approval cycle. Silence is not agreement;
explicit owner direction can settle execution without pretending GPT reviewed code.

## P1 — corrections that affect correctness and feasibility

1. **The boundary is off by one.** At time t, K=W+t is an inclusive support bound,
   not a white ghost cell. If the start has its last black at W, `row[K]` is black.
   Setting it to zero and updating only k=1..K-1 drops the edge. A simple correct
   contract uses two buffers with indices 0..W+T+1: row[0]=0; at time t old indices
   above W+t are zero; update new[k] for 1<=k<=W+t+1 with the specified recurrence,
   holding the wall zero and maintaining the outside halo. Stop at t=T before
   stepping again. Explicitly mask unused lanes, including in `~row[1]` and the
   all-dead test. An independent singleton/edge-position control should catch
   this before any performance run.

2. **Name the free coordinates consistently.** The kit's Theta f uses f as odd
   column-trace bits. These parameterize the constrained starts, but are not
   literally the initial cells at depths 2,4,... . Already L(2)=NOT f(0), since
   a(0)=1 and a(1)=L(2) XOR 1. Use “index bit i is odd trace bit a(2i+1)” throughout,
   or supply the triangular conversion if indexing initial even-depth cells.
   Preserve a tiny literal mapping fixture independent of the reconstruction.
   Outside the class the correct bound is d<W; for odd W it can equal W-1, so
   “dies before W-1” is too strong. The maximum-restriction argument survives.

3. **The batch and arithmetic contradict the caps.** At W=60,T=240, two row
   buffers of 302 uint32 words for 2^20 lane-groups require 2,533,359,616 bytes
   (about 2.36 GiB), before reconstruction, death times and reduction. That exceeds
   256 MiB. Choose group count from the sum of ALL live allocations; stream or
   reuse the reconstruction triangle, whose storage must also be counted.
   Likewise 7e4 word-steps/group times 2^25 groups is about 2.35e12 word-steps,
   not 2.5e9. Early extinction can reduce measured work, but cannot repair that
   multiplication. Keep 52/56/60 to explicit frozen fixtures in this pilot, not
   an accidental full census to establish multiplicities. Testing known fixture
   multiplicities does not establish that there are no other maximizers.

4. **Two controls need their domains written literally.** Sparse16 constrains
   the INITIAL row's depths 1..111, not the evolved row's weight. An infinite
   stripe cannot be passed literally through the finite-support input API: use
   a stripe halo sufficient for the observation cone (initial depths through
   T+1 suffice for depth 1 through time T), or a separate synthetic test of the
   censoring logic. Keep that distinct from a claim of infinite support in a
   finite-width census. At small W there may be fewer than 64 lanes; sample at
   most the available set and retain deterministic edge cases.

## P2 — bound the comparison, not just each training loop

P1 pass must precede it. State whether 2^24 unique starts and 20 minutes are
TOTAL across the five seeds for each method/width, or are per seed. The current
reading permits 5 methods x 3 widths x 20 minutes = 5 hours, or 25 hours if per
seed, before unbounded CPU follow-up. Specify a single stage wall/CPU/output/disk
budget and all subordinate limits, with the first exceeded limit stopping work.
For a genuinely small first comparison, narrow methods/widths rather than
silently multiplying the pilot. Equal **caps** are sensible; exact equality of
achieved calls, time and peak memory simultaneously is not a meaningful demand.
Report fixed-call and fixed-time comparisons separately when one cap binds early.

Do not automatically extend EVERY censored lane on the CPU: potentially millions
could reach T. Deduplicate, preserve all censored counts, and choose a bounded
predeclared witness subset for extension to 16W within the same budget. Unextended
lanes remain censored. Freeze beam completion/scoring, mutation restart, network
size and cross-entropy parameters; otherwise these are five method names, not
reproducible executable versions. A candidate's exact independent check remains
valuable even if search does not rediscover every known maximizer.

## P3 — the protocol is much improved; the purported pilot remains large

The test interval contains 399 million bits. A two-hour TRAINING cap says nothing
about validation sweeps, sequential compression, inference on all those contexts,
conversion, or the independent 10^5-step Rule 30 control (quadratic cell work if
implemented literally). Bound total examples, configurations, preprocessing,
control generation, validation and inference wall/CPU time, output/disk, and total
stage time. Start with a fixed smaller slice; only a separately agreed stage
uses the full resource. The 4 GiB memory cap is not an execution-time cap.

Replace “the bits of a Rule 30 row (predictable)” with a specific causal positive
control and a guaranteed baseline: e.g. alternating or short-period bits, with
an explicitly correct predictor. Knowing the previous ENTIRE row determines
its successor; it does not make spatial next-bit prediction inside a single row
trivial for the proposed context model. An LFSR is optional after its recurrence,
order and sufficient context are fixed; learnability by a small CNN is not
implied merely by determinism. A CSPRNG sample is a useful engineering negative
control, not proof that the pipeline's statistical test has its claimed level.

The z>=6 whole-block and z>=3 in every tenth rule can stand as a conservative,
predeclared detection criterion under the stated iid fair-bit null. It tests
advantage over a coin, not superiority to another fitted predictor. For “beats
baselines”, also report paired per-block accuracy/log-loss differences against
frozen baselines, with the comparison rule fixed beforehand. A negative outcome
means the criterion was not met, not equivalence or a bound on every predictor.
Keep a fixed final candidate per rung; later architectures must not be chosen
from earlier final-test outcomes. Report every tested rung, including failures.

## Two separate handoff notes, not extra launch reviews

**Local L860–861:** the reported sandbox memory failure is an important outcome,
but does not measure a 2–4 GiB sandbox limit. Local sampled peaks, different widths,
unknown process aggregation and an inferred submission-13 footprint cannot
identify that limit. “N=20 peak below 2.5 GiB therefore fits with room” is unproved.
Fewer declarations versus total work is not an exhaustive causal dichotomy:
larger individual reductions, retained environments and transient checker state
can change both peak and lifetime. Also W8's 1800-second per-step stop conflicts
with its prediction of up to 2600 seconds per step: a timeout would be censored,
not evidence for hypothesis B. No automatic N=22 follow-up. I have read this
handoff, not audited W8's executable source or accepted its launch; explicit
owner authorization is separate from GPT acceptance.

**Document precedence:** CL613 says every correction was applied, but old job 1
still calls a cutoff survivor a Q01 candidate, job 2 retains its “right half is
the whole story” conclusion, job 3 retains entropy-limit language, and H.4 still
presents a white-run histogram as an extra statistic. Mark these passages
historical/superseded or remove them. Section J and GC1775–1776 should govern;
otherwise stale text can re-enter future job specifications.

This is the requested final compact technical handoff, not an invitation to
spend the remaining GPT budget on incremental drafting. Implementation and
explicit execution decisions remain with Local and the owner under the standing
rules; no job or heartbeat was started here.
