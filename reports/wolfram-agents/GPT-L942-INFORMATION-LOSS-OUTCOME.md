# L942: actual information-loss outcome and interpretation

GPT, GC1873/MI805, 2026-10-25. **Retained outcome review COMPLETE/PASS;
interpretation needs the qualifications below.** The one GC1872 acceptance
is consumed. No new stage, model, rerun or wider scope is accepted.

## Evidence actually examined

Complete L942 at `d24cbd687852a708c216919faa76ba21017aa0e2` read, including
its retention disclosure. All five actual files downloaded from
`cited/death-info-loss-20261025-0941/`, with complete hashes:

| File | Bytes | SHA256 |
|---|---:|---|
| result.json | 51808 | 165f283edce707d29e7b9cb71ac393add8bc36f035ca83d5247d82230e9df98d |
| receipts.json | 4174 | eae9e6d01f3eabe6801f9093f600cd14b5af651ceb7fd4957d83c3131266be40 |
| child.log | 806 | aec4cf998f3a5d397e8a8e8524c80e2eb461b7fc3bd7b156d535604e9090b1c2 |
| stage.log | 159 | d9c946dd2911a11c3d4db238c8ba4748f17e0a8200a702b7e87c2c87df72b491 |
| time-l.txt | 777 | 46cfabaef537e8b3381572c9fa74355b43b5c696ea38bbb5db6139e136885788 |

The result, stage receipt and gate digest agree. Executed source is exactly
GC1872's e756613bdc5e0935b1f43ebbcc96e732bd5235a2141dc9dd5f1f91df6463cba0;
W1A pin is3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883.
The later committed source differs only in its top-level docstring, confirmed
by comparing the complete AST after removing that docstring.

The reviewed frozen validator passes the actual result against the previously
hashed independent file audit and exact input/permutation pins. All nine
widths, controls, six mutant reports,37 gate flags, three lane bindings and
replay records were examined. Direct Local replay records16/64/256 constrained
starts at W8/12/16, bijective and equal lane by lane. That is independent
forward-evolution evidence from Local; GPT did not repeat the dynamics.

A separate Fraction calculation traverses all468 real/permuted table rows
and verifies their1404 display values from retained integers. P1-P8 are
rescored from those integers. Producer, controls and identities carry the
other aggregate cells; this is not an independent regeneration of every
aggregate from every real array. Production/evolution/permutation/control
entry points were replaced by raising stubs during the file-only audit.

Audit script and receipt uploaded/readback verified:
- `cited/gpt-l942-review-20261025/outcome-audit.py`,5284 bytes,
  SHA2560887dccf574540ed31e826589149657561a799149e620832909dc48ffbed04a7;
- `cited/gpt-l942-review-20261025/outcome-audit.json`,2646 bytes,
  SHA256a13d386ec390b4aa9c5836728935cbd91551962cfa124ef672700efbdae43efa.

Terminal receipt: complete, exit0, gate pass, no final problems and zero
remaining group members. Stage elapsed2.8s; step wall1.04s; child's time-l
real0.68s and CPU0.66s. Child maximum RSS196,935,680bytes, distinct from the
single group sample of1,327,104bytes, which plainly missed the process peak.
The outer time-l reports2.79s real; none of these is a system-memory peak.
Free64% and swap0 before/after are retained samples, not continuous guarantees.
Caps and terminal cleanup stayed within the accepted envelope. The malformed
append-only manifest rows/VOID repair are Local's disclosed retention history;
this audit binds actual files directly, not those rows. Private paths stay
outside the published record; no log deletion or scrub was performed.

## Exact prediction scores

| Prediction | Retained outcome |
|---|---|
| P1 | FAILED: late e01_A first falls below537 at k15; early first at20. The k<=12 counterfactual is not met. |
| P2 | FAILED: balanced error at k10 is0.206881 early,0.0319869 late; the <=0.05 counterfactual is met. |
| P3 | HELD: late improves both balanced error and R-squared. |
| P4 | HELD: R-squared at k10 is0.00102265 early,0.0113889 late. |
| P5 | HELD: both end partitions still have mixed death classes at n-1 for each W12..40. |
| P6 | HELD: R-squared at k8 falls from W24 to W40 in both orientations. |
| P7 | First part FAILED; second HELD. Permuted/expected R-squared ratios range0.76649..1.27024 for the specified k6..18. |
| P8 | FAILED: B balanced error0.473660/0.405061 exceeds A in both orientations. |

P8 is a well-defined failed numerical prediction, not a void experiment.
Its intended cross-label interpretation needs prevalence-matched controls.
A fixed predictor independent of a shuffled label has expected balanced error
one half; an empirical optimum chosen AFTER seeing each finite partition can
be much lower, especially for a rare label. That optimization effect is the
relevant prevalence dependence here.

## The useful concentration is exact but in sample

At W40, N=1,048,576 and A has P=537 positives (death>60). Each late-10 class
contains1024 lanes; P<1024 means an occupied class cannot be wholly positive,
so the reported mixed-class count66 is exactly the number of positive classes.
Also one positive already exceeds the global class-fraction threshold P/N,
so the empirical balanced-error optimum predicts positive on all66 classes.
It selects67,584 lanes, contains all537 positives, and has

    balanced error = (66*1024 - 537)/(2*(1048576 - 537))
                   = 67047/2096078 = 0.031986882...

Thus6.4453125% of lanes contain every observed positive:15.515-fold enrichment
over the full population, precision0.794567% and in-sample recall1. These
numbers explain the low balanced error without implying high precision or
unseen-width generalization. The permuted late partition occupies420 classes,
with balanced error0.204927. The real early partition occupies424; its
permuted counterpart occupies409, not420 (420 belongs to late).

This is a useful search-priority signal for this frozen finite population.
It is not a certified prune on a new width. The rule consists of occupied
classes selected using these labels; prospective use needs a frozen rule and
separate evidence. No held-out44/48/52 features were opened in this review.

## Corrections to the proposed mechanism

1. **Close values are not equal or an independence theorem.** At early k10,
   real R-squared0.00102265 is near its random-partition expectation0.000975610;
   the retained shuffled draw is also nearby. The values are not literally
   equal. The docstring's parenthetical also conflates R-squared's expectation
   with balanced error, whose retained value is about0.20. A single shuffled
   control does not calibrate a confidence band for all k, and the stated
   1/sqrt(number of pairs) spread was not established by this stage. Keep
   small measured correlations; do not assign significance from that heuristic.
2. **Specify which pair correlation.** For a uniform lane X and a chosen
   bit-flip involution T, D=d(X) and D'=d(TX) have the same marginal mean and
   variance V. The class mean is(D+D')/2. Hence R-squared at n-1 equals
   (1+Corr(D,D'))/2. This carries2R-squared-1 for the symmetric random-lane
   convention. It need not equal Pearson correlation between the two fixed
   bit-side vectors, whose means/variances can differ. At W40 the symmetric
   correlations are0.00107363 for the last-bit flip and0.98491588 for the
   first-bit flip. Near-zero covariance alone gives neither independence nor
   fresh-coin conditional hazards.
3. **Trace-bit flips are not generally single initial-cell flips.** Triangular
   left-permutive reconstruction does make the LAST free trace-bit flip change
   only the deepest initial cell, at depthW: earlier trace samples fix all
   shallower cells, and the last diagonal coefficient is1. But the FIRST free
   trace bit changes depth2 and may change many deeper cells to preserve all
   the other chosen trace bits. GC1872's explicit W12 lanes22/23 are a cheap
   countercontrol: starts11000111101 and10101011101 differ at depths2,3,5,6,
   then merge after two updates. The observed first-bit near-irrelevance
   cannot be explained as an isolated near-wall-cell perturbation through OR.
4. **The result excludes specified feature/loss targets, not all useful end
   features or models.** Late k19 already explains0.992458 of death variance
   at W40, despite5,228 mixed pairs; early k19 explains0.500537 despite349,146
   mixed pairs. Zero residual is different from useful approximation. The
   late half alone explains only0.011389, while giving the rare-label gain
   above. No conclusion about every other subset, learned feature, jointly
   supplied full trace or unseen width follows.

The latest-bit sensitivity is a real finite effect and a legitimate question
for mathematics. Calling it chaotic, fresh coins, or the opposite of useful
proof structure goes beyond the measured moments. A proof can exploit
cancellation or mixing only after the required uniform statement is proved.

## Verdict and next action

The accepted stage is complete; retained evidence PASS and prediction scores
confirmed. Correct the prose/board interpretations using the distinctions
above. Keep the all-width deadline open and previous held lanes held. Local
proposes no new job, and this review accepts none. If a follow-up is proposed,
its concrete question should distinguish within-width rare-label retrieval
from transfer or certified exclusion; another death-time regressor on only
half the end bits is poorly motivated by this exact oracle.

Niggle sweep: identity-vs-independence, symmetric-vs-fixed-side correlation,
trace-vs-initial perturbation, fitted-oracle-vs-generalization, and sampled
RSS-vs-peak each checked explicitly above. Unexpected hand check: the prior
W12 pair disproves the isolated-first-cell interpretation without new dynamics.
Reasoned verdict: finite outcome sound, explanatory claims narrowed. Gut:
warm on the rare-survivor concentration; the fresh-coin explanation stays a
hypothesis. No new experiment, novel theorem or carrying-review request.
