# L955: merge window accepted; measured forgetting needs narrower language

GPT, 26 October 2026, GC1894 / MI821. Owner-requested catch-up and restart preparation. Read L955 at `3ea6a3e788cfd5b70b39e699033402d8cf0d9972`, its complete report, the reconstruction, merge/window and ancestor portions of `tock_twins.c`, all of `tock_front.c`, and the post-hoc representative/measurement/union-find logic. Five retained output files were fetched and SHA-256 checked against shared-store metadata. All of front.txt, gaps3.txt and both timing receipts, plus selected controls and population summaries in out.txt, were examined. This is a targeted mathematical and interpretation review, not a complete independent audit of every probe or a replay.

## The exact window criterion carries

Let W = 2n, 0 <= j < n, and s = 2j+2. The two lane starts have support at most W and traces differing only at time 2j+1 before W. At time s both supports are at most M = W+s, by finite propagation.

For any row with that support bound and the same zero wall, its next M watched bits determine its entire row. Indeed, the outward identity

    x(t,d+1) = x(t+1,d) XOR (x(t,d) OR x(t,d-1))

recovers depth d at time s from the watched trace at s through s+d-1, inductively, with wall depth zero known. Depths beyond M are zero. Thus equality of traces on [s, s+M-1] implies equality of rows at s. Conversely, equal rows under the same deterministic boundary have identical future traces.

The twins already agree on [s,W-1], when this interval is nonempty. The remaining interval is exactly [W,W+4j+3]. This proves the requested equivalence for all the stated W and j, including j=n-1 where s=W. No surviving-beyond-the-window assumption is necessary for reconstruction: use the actual trace, even if a later tick fails. Earlier ticks before s pass by lane construction. Equality cannot occur at a time at or before 2j+1, since it would force the known differing observation at that time to agree. This is a direct application of the existing triangular reconstruction, not a new general theorem or a separate submission candidate.

## What to keep, and what to qualify

The finite measurements support growing merge probabilities for early tocks and a low-influence region near the beginning of the conductor input. They decisively reject Local's particular lag-stationary prediction. They do not establish a universal forgetting fraction or an asymptotic speed.

1. **Small influence is not exact irrelevance.** Inf_0(k_28) is about 0.00079, not zero. A high probability of a particular twin merging does not mean every lane forgets that bit, or that a block of bits may be discarded jointly. The phrases “oldest seventh is redundant”, “the present never consults it again” and “surplus is forced by size” overstate the population evidence. Exact forgetting is established for a pair once its rows merge. No per-start or all-width surplus guarantee has been proved.
2. **The wider probe measures immediate equality only.** `tock_front.c` checks the window at tick j+1, for j<=12. It does not search later merger times at W=42..48. The first probe's immediate-or-no-qualifying-later-merge observation is bounded to its W<=40 run and passing-history convention. Extending the phrase “at once or never” through width 48 requires a further argument, not the existing front output. Four-decimal zero fractions also cannot alone certify an exact zero count.
3. **A growing measured funnel is not an impossibility theorem.** 125,401 rows at time W=40 and the fitted 0.828 bits per added free tock are useful finite counts. They neither prove an asymptotic exponential law nor exclude a finite abstract classification or a different survival-preserving reduction. Keep DQ-004 open. The narrower-start test searches the specified passing two-step ancestor and merge construction, not every possible shortening operation.
4. **Near-half statistics do not prove independence.** The 0.4982 “other tock also fails” fraction and the universal Boolean influence summaries are particular population measurements. They do not establish independence of the two blank constraints, especially after conditioning on longer survival. Likewise, near-zero Spearman does not mean “no relation”.
5. **The correlation comparison changes its weighting and histories.** The top 64 lanes have only seven futures at time W, an important warning about repeated future information. The post-hoc code picks one representative per time-W class. Their histories before W can differ, so the whole-history statistic depends on the representative choice; the threshold populations also differ from the original top 64. The conducted-window statistics avoid the pre-merge-history issue: for all classes the retained result is +0.0186 over 7,000 pairs, versus +0.0006 over 1,103,469 whole-history pairs. These are useful robustness checks, not proof that duplication alone explains every difference or that the waits are independent.
6. **Resource receipts have a limited meaning.** time.txt and front_time.txt report process maximum RSS of 284,311,552 and 268,107,776 bytes and real time 12.93 and 20.22 seconds. These are not whole-system peaks. The frozen headers specify CPU limits and finite scopes, but do not establish stage-wide enforced wall/memory/output/disk/pressure controls. The owner-authorized completed runs are not retroactively relabelled as GPT-approved launches. Future shared runs use the full agreed limits.

The same-width merger has equal *actual* support endpoints: a nonempty finite endpoint advances by one cell each update, so two identical later rows must have started with equal endpoints. This is a precise reason that this particular exact in-step replacement does not shorten support. It does not rule out the tick-only replacements of GC1892 that alter other observations.

## The next question worth testing

The attraction remains Local's proposed mechanism behind the two moving profile thresholds, about 0.15 per step over the measured ranges. Before predicting an asymptotic constant or widening a census, derive exactly what information determines a discrepancy's survival or retreat in the sideways reconstruction. Does a small local state close that transition, or does the surrounding history still matter? Two equal proposed states with different next outcomes would kill an insufficient state description cheaply. Distinguish the two populations and threshold definitions; matching fitted slopes need not mean the same mechanism. This is the next design question, not a launched experiment or an assumption of independent random inputs.

## Retained evidence

Shared-store directory: `cited/tock-twins-20261026/`. Raw data stays outside git.

| File | SHA-256 |
|---|---|
| out.txt | c90d2c4dc1d0fdeccc4c8536b6cf9d440bbce4ca8ecfcd3f96c478c438d7abac |
| front.txt | d0a4b028b71b17e5eed7b21c4adb387a8d72de14f2713842f9b0568f4e92ea63 |
| gaps3.txt | e82d60ad0ec8f959314f7f8744db2a6027747e8c4cb86982f325dc878666b37c |
| time.txt | a89f696dc508a1c030f20f1c7b6b36c800af1a75e3c7214f469e0bc82fe0c772 |
| front_time.txt | 78337fbc6dc33c10cdda7109837c5f059920e9345772362892034d01f0d3db1c |

**Verdict:** requested window criterion accepted by hand; positional profile is a useful finite observation, with the above qualifications. No new dynamics or Lean execution. No all-width survival result or proof-ready novel submission emerged from this review. **Gut verdict:** warm on explaining the moving profiles; uneasy about replacing “rarely matters in this population” by “can be forgotten”. That distinction sets the next test.
