# CQ01 retained-outcome review — GC1815 / MI748

**COMPLETE / PASS at finite numerical-evidence scope.** The one GC1814-accepted
Local stage is completed and its permission consumed. Read complete L902 at
`3de6560b47385a2636546f087d0fe029ec400774`, all 1,701 result records by file
validation/arithmetic, every retained control report, the complete log and
terminal receipt. No census, physical controls, GPU or Lean computation was
repeated by GPT.

## Exact evidence and provenance

Shared-store packet: `cited/cq01-census-20261024-2031/`.

| File | Bytes | SHA256 |
|---|---:|---|
| cq01_result.json | 452786 | 781833d6a26826590ab038743e22078535c4ff867ef015d3b38f49a70c7bc475 |
| receipts.json | 4054 | ada44134ca3d203ca4faa6519ff0a238c10b18549e6cd2fda56ffe9fbccca84d |
| cq01_census.log | 795 | 4c625926a4893f46f08d7cc2eeea624266c302cc028aec89871e5ebaaf09ede7 |

All downloaded bytes match store stat digests. Result and receipt bind the
accepted runner `7c88ec565cc72588ad81e6cc996a98ad5a3d42a5b2ec21016c27e6fdae56bef7`
and W1A `3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883`.
The receipt's matcher digest equals the downloaded result; its full log tail
equals the downloaded log. L902 changes only the runner's OUTCOME docstring;
validation used the accepted historical bytes, not the new documentation hash.
Previous deleted development outputs remain unavailable and separately disclosed.

## Numerical read

The accepted historical validator passes the actual result. Separate file-only
checks cover unique exact grid coverage, integer domains, all witness lengths
and bits, right-witness/lane identity, attaining counts, monotonicity in each
coordinate, zero censoring and all 21 retained L=80 resimulation outcomes.
These checks read evidence; they do not independently regenerate the census or
physically replay its witnesses. Five base reports are true, all four mutants
have actual false outcomes and consistent caught flags, and all 21 gate reports
are true. The multiplicity mutant fails the word-set check as intended.

Unexpected boundary check: every L=0 row has E=1, all 2^B lanes maximizing and
minimum lane zero; every B=0 row has exactly one maximizing lane. All pass,
including both degenerate support boundaries.

| L | E(L,0) | E(L,4) | E(L,8) | E(L,12) | E(L,16) | E(L,20) |
|---|---:|---:|---:|---:|---:|---:|
| 10 | 14 | 16 | 16 | 16 | 16 | 16 |
| 20 | 22 | 25 | 36 | 36 | 36 | 36 |
| 40 | 41 | 47 | 47 | 47 | 48 | 48 |
| 60 | 61 | 66 | 69 | 69 | 69 | 69 |
| 80 | 81 | 82 | 89 | 90 | 90 | 93 |

E(80,20)=93 has six maximizers, smallest right-lane index 281871. It means
alternation through time 92, failure at 93, and n*(80,20)=46 in GC1811's pair
units. The maximum E-L is 17; maximum E(L,20)-E(L,0) is 14 at L=19,20,21.
No row violates E<=1.5L+10. Exactly 1656/1701 cells satisfy E<=1.2L+10;
78/81 values of L satisfy it for **every** B in the grid. This also checks the
original wording “most L,” rather than substituting only a cell-weighted count.
The [85,130] prediction contains 93. These prediction successes retain L899's
prior-development-exposure qualification; they were not fully blind forecasts.

## Execution and limits

Preflight passed. One census child exited zero; the peak group membership two
includes its time wrapper, with no Lean process. Stage elapsed 198.0 s; step wall
196.33 s; time-l real 196.02 s and user+system CPU 195.70 s. Sampled group RSS peak
462,553,088 bytes; time-l process maximum RSS 461,668,352 bytes. Neither is a
system-wide peak. New artifacts at final accounting 455,954 bytes; log 795 bytes.
All are below the exact accepted caps. Baseline and final pressure level are 1,
free percentages 64 and 66, swap growth zero; free disk remains above 5 GiB.
The receipt records 190 monitor samples, no final problems and zero group
members after cleanup. Raw per-sample trajectories are not retained; these are
the supervisor's aggregates/endpoints, not a continuous system-pressure proof.
The terminal evidence closes the cleanup question for this stage only; it does
not repair W8's separate incomplete cleanup receipt.

Lane-pass times sum to 195.41 s; B=20 alone takes 148.11 s. B=16 through20 cost
0.59,2.15,8.55,35.54,148.11 s. These measured costs support the earlier warning
against linear extrapolation in B. They do not identify which internal operation
caused the scaling; no new profiling or benchmark is requested.

## Mathematical interpretation and next boundary

L902's question is well formed with one distinction: for each fixed finite R,
CQ01 requires arbitrarily deep black cells of Psi R, equivalently every finite
L eventually encounters one. A uniform bound on white-gap length for that R is
stronger. A binary sequence with black cells only at powers of two illustrates
the logical gap (not asserted to be any actual Psi R). For fixed B, finitely
many R let individual gap bounds combine if they have first been proved; the
present finite-depth table proves no such bounds. The largest measured white
run beginning just beyond an admitted L is E-L-1=16. Keep E-L=17 distinct from
that length. No comparison with D(W) establishes an asymptotic law or speedup.

L902's suggested L<=400, B<=16, K=800 is **not accepted or launched by this
review**. It requires the promised exact source/specification, controls and
stage-wide caps; current source explicitly refuses that scope. Record any
follow-up prediction after this table's exposure. No automatic retry, cap raise
or widening. W78 and W8 retry remain held.

Instinct/niggle sweep: the small gaps are interesting, but the shift from finite
finiteness to uniformly bounded gaps is the carrying uncertainty. The sparse
black-position control separates those statements; endpoint and “most L”
checks resolve the cheap data niggles. Gut verdict: a useful clean finite
measurement, with its stronger extrapolation still a question.
