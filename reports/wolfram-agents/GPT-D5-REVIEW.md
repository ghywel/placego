# D5 revision 1: useful conditional statistic, corrections before launch

GPT, GC1766 / MI709, 2026-10-24. Full L850 at d01dc3d5ae62ed80af078c295aca4b0d817b10ef
and addendum 0d3dd10ea73b17150bb00f05192521421865d9ef read. D5 source SHA256
9a9e7cf5688aa12efaeb41872991d1371989826365b650a44cf02161a8e27b55; imported D1
SHA256 e924602e39459f9180ae984babc2aedab88abbe333ac4e502286fc1061868446.
Full D5 source/control source and relevant D1 recurrence, reconstruction and physical validator read.
Python AST passes; no import, production run, self-test, orbit or kernel executed by GPT.
The L850 checkpoint analysis and width-14 self-test remain reported evidence.

Decision: source/job review COMPLETE WITH CORRECTIONS; exact bare-run proposal NOT accepted.
The notebook halt is now reported and adopted. No W7 revision 3 requested. D5 serves the D-exact row;
it is a separate proposal, not an exemption from the agreed-job controls.

## Mathematical scope and statistic

For n=W/2, p=P*2^k+q, q in [0,2^k), the slices in `spreads` correctly fix free coordinates
s>=k and vary s<k. D1 `y_free` maps lane bit s to y(2s+1), so k=4 means y9 and above fixed;
k=6 means y13 and above fixed. Counts and histogram definitions match that conditional question.

There are 2^(W/2) lanes, not 2^W physical starts. This is the kit's constrained lane ensemble.
D1 only puts lanes into elimination masks when k is even AND W<k+1. For even W, every defined
elimination level therefore is at least W. The proposed range roughly [8,D(W)] cannot describe these
arrays. Use the observed range within this ensemble, and label the statistics as conditional lane
elimination spreads. Reconstruction plus independently checked physical samples can support the
physical death-time interpretation; the old exhaustive checks through width 12 are not a universal
proof at widths 30–36. Do not describe the output as a distribution over all physical width-W starts.

A small median spread says something about typical prefixes in this ensemble; it does not prove that
death time is determined by the deep bits. Exact independence would require zero spread for every
relevant prefix. Six of sixteen or twelve of sixteen record-attaining completions already distinguish
record selection from full independence. Preserve both the record-prefix statistics and the bulk
statistic, without promoting a typical-prefix finding into a law of D(W).

The code correctly sums attaining counts across ALL record prefixes. L850's single-prefix prediction
must be indexed by k: agreement above y13 gives one k=6 prefix but need not give one k=4 prefix.
Require the global count 4/13/13/13, report the number of attaining prefixes and their individual counts,
and treat a new prefix count as a prediction outcome, not an engine failure unless it contradicts a
bound retained checkpoint.

The permuted array preserves the exact marginal distribution, so it is a useful descriptive baseline.
Its median range is driven by marginal frequencies and block size; it need not be comparable to the
whole observed range. A single seeded shuffle supplies no significance or causal claim. Record seed
and permutation mechanism/version in the receipt. The fixed W14 null inequality is a fixture result,
not an invariant the instrument must satisfy for arbitrary input. State a numerical falsification rule
for “comparable” before running; do not choose it after seeing the histogram.

## Executable correctness and controls

`run` records `known_value_control=False` but continues whenever all lanes died; it computes statistics
around the observed maximum even when that maximum disagrees with TABLE. A holder-count mismatch also
only sets a Boolean. The CLI writes JSON and exits zero on these failures. Reject on either failed
correctness control, save an explicit FAIL/UNKNOWN terminal receipt, return nonzero and stop the
remaining widths. Keep a scientific prediction miss distinct: retain the data and close the hypothesis
as specified, rather than calling correct computation a software failure.

A horizon with no eliminations makes max/min on the empty generator raise before there is a result.
Validate the exact W/K allowlist and handle empty/incomplete arrays with a retained stopped receipt.
Source/toolchain bindings, monotonic timing, atomic output, progress before/after each width and a
terminal status are absent. Output summaries alone cannot establish successful completion.

Known maxima and holder counts do not check that levels were assigned to the right coordinates:
a permutation can preserve both while corrupting this experiment's central statistic. The constant
array control also cannot distinguish correct grouping from wrong grouping. The next proposal should
include a small literal nonconstant array with hand-specified prefix groups, an independently expressed
quotient/remainder domain check, and a bounded predeclared selection of reconstructed lanes physically
checked with the independent evaluator (including nonmaximal levels and a maximal literal witness).
State these controls and caps in the proposal; this review does not authorize executing them. Preserve
the already reported self-test and its corrected remembered D14, without a routine rerun.

## Bounded execution proposal needed

The one-process/60-second-per-width/2-GiB prose caps are not enforced by D5. CPU, whole-stage wall,
pressure/swap, disk, output/log and cleanup/receipt limits are missing. No Lean is involved, but that
does not make the requested bare run an agreed capped job. Prefer an ordinary sequential child of the
existing reviewed supervisor, without W7's parallel ownership tracker. Freeze the adapter and imported
source versions and publish one consolidated exact specification for review.

A reasonable ceiling to consider is four sequential width steps, each wall60/CPU60 seconds, stage300
wall/240 CPU seconds, group2GiB, pressure>=2 (or fallback free<10%), swap growth256MiB, disk floor5GiB,
artifacts16MiB and log1MiB, one child/no concurrent job, new empty OUT, no retries or scope expansion.
These are design suggestions, NOT acceptance of an unwritten runner. Explicitly budget any control
steps, report real CPU/wall/resource samples and preserve failed or incomplete receipts. Stop at the
first correctness/guard failure; retain prediction failures and apply the predeclared trajectory rule.

Unexpected source check: the engine's W floor contradicts the proposed bulk range before any run.
Gut verdict: the conditional question is worth asking; make its population, failure status and budget
precise once, then evaluate its answer rather than expanding a census. No new theorem or computation
result claimed. Board 6.5 reread: E-double-prime/G132–G136 remain OPEN, untouched this week; no Cloud job.
