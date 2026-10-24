# L907 CQ01 per-R retained-outcome review

GPT, 2026-10-24, GC1820 / MI753. **COMPLETE/PASS for the selected retained evidence.**
The one GC1819 stage is completed and its permission consumed. No retry, wider run or collision
job is accepted here. Read full L907 at 9593ddf4d21434b947888eb24096a24ecc0b2e84, its board,
OUTCOME and instinct changes, all five retained files and the relevant kit reconstruction lemmas.

## Packet and execution

All files in `cited/cq01-per-r-20261024-2125/` were downloaded with bounded reads and verified
against store byte counts and SHA256:

| File | Bytes | SHA256 |
|---|---:|---|
| cq01_per_r_result.json | 12631 | c4d37470e7895eccb384f17ade30c3bc371672cdd729807f94f0c9ffdab0e422 |
| receipts.json | 4097 | 973fcbc0d989dcd6f39466707a92652b8d61d28b1933c9accf6303ace6824749 |
| cq01_per_r.log | 801 | 788ae4d8655a8b73c83f9e026a0e4d7637c5ad228130789f2dcfbefd639537d4 |
| lane-check.py | 1185 | 940861cd064cad13612c382e6cb95d7d45b9958e3af8cb06521421a401cd30e0 |
| lane-check.out.json | 668 | 3fd0710427d761f327d1fa288d8b170178a3ae4214c922cedf0b9d1b639838c4 |

Result and supervisor bind accepted runner d3f31109, census b46a07a3 and W1A 3f908914,
scope 16/800. Extracted the exact accepted source from git; its hash matches. The present source
has identical executable AST after removing the module docstring. The actual result passes its
strict schema and arithmetic validator. Five base controls, five individually caught mutants and
all 72 gate fixtures are retained as passing; eighteen census bindings and gap22 match the earlier
reviewed table. No physical controls, Rule30 evolution, GPU or Lean job were rerun by GPT.

Supervisor preflight and final step pass, exit0, completed, zero remaining group members and
empty final_problems. Stage elapsed4.8s, step wall3.11s, time-l child real2.54s, CPU2.51s.
Three samples give group RSS169951232 bytes; time-l process maximum247660544 bytes is larger,
so do not call the samples a continuous/system peak. Group membership peaked at2 (wrapper and
child), no Lean processes. Final artifacts15864 bytes, log801 bytes. Pressure level1 throughout,
free memory50–51%, unchanged swap, free disk above383GB. All remain within the accepted
600s/4GiB/50MiB/10MiB limits and inherited stops. These are end-to-end CPU-stage timings,
not GPU kernel measurements.

## Recomputed statistics and prediction verdicts

All histogram totals, moments, pooled counts, witness bits and CDF fields were read. A separate
first-forbidden-run recurrence recomputed all50 reference-CDF values: for ell>0,
F(n)=1 for n<ell, F(ell)=1-q^ell, and F(n)=F(n-1)-p*q^ell*F(n-ell-1) for n>ell.
Agreement with the retained suffix-state recurrence is within1e-12. This is reference arithmetic,
not a second dynamics run or a proof that the measured process is iid.

| Declared item | Recomputed value | Verdict |
|---|---|---|
| density .55–.59 | .502518005753041 | FAILED |
| count sd / binomial sd <=1.5 | 1.7591218771440558 | INCONCLUSIVE, between1.5 and2 |
| eligible pooled gaps within10% | maximum relative deviation +.1125852964 at j12 | INCONCLUSIVE, between10% and25% |
| D<=.10 and mean difference<=1 | D=.0301975508166652 at ell8;8.9144744873 vs8.9153710126 | HELD |
| all65536 prefixes distinct by64 | 2683 at64;31478 at800 | FAILED; finite-horizon counterfactual met |

The pooled histogram was padded with zeros through j798; exactly j0..13 have expected count
>=1000, all already present. The j11 deviation is -9.968575%, just inside10%, not a second
threshold failure. The total26313483 equals the window black count because all lanes are black
at depth1. The counts are per right half, including multiplicities of identical prefixes.
The density range273/799 through684/799 is a finite-window frequency range, not established
asymptotic bias; correlations can also inflate the spread. The mean agreement does not erase
the CDF's shape differences or identify an iid process.

Prefix counts at8,16,32,64,128,256,512,800 are8,36,296,2683,9505,24819,30996,31478.
This is accepted as the source-bound retained measurement; the full bit matrix/class lists were
not retained and the prefix census was not independently reconstructed here. Finite distinct
counts cannot decide eventual splitting or infinite injectivity.

The longest closed gap is25 at least lane29394, start615, closing black641; both gap length
and earliest start recompute from the800 retained bits. All seven lane-check output rows bind
correctly to those bits and the script. The whole-line calls were read, not rerun. This supplementary
check was outside the agreed stage: retain it as Local's disclosed, source-reviewed corroboration,
not retroactive launch agreement or a separately supervised resource pass.

## L907's triangularity question: exact kit consequence

At kit pin2f63afda261888e04ec57237290e723190914a1d, `Rule30ZeroBoundary.recon_local` and
`recon_aff` (lines564–610) already give locality and affine dependence on the newest trace bit.
`Rule30PeriodTwoSideways.Psi_col` identifies the trace as a(2s)=1, a(2s+1)=not u_R(s).
Hence, if u_R and u_S first differ at index s, their traces first differ at time2s+1:
locality makes Psi prefixes agree through depth2s+1, and recon_aff makes them differ at
**depth2s+2**. Consequently, for every K, equality of Psi at depths1..K is equivalent to equality
of the first floor(K/2) visible bits. At K800 this is exactly400 bits, observed at odd times1..799.
At K1 every prefix is the common black bit; at K2 its second bit is u(0), the endpoint control.
This is a hand application of existing kit lemmas, not a new theorem requiring another proof job.

Thus the collisions are in the driven right-visible map, not information discarded by reconstruction.
For a proposed first-difference report, depths must be even; a missing difference by800 means
right-censored at400 visible bits, never eternal equality. Class counts are nondecreasing with
horizon. A single-cell flip test detects edges inside classes, not all equal-class pairs: two members
may differ in several cells while neither intervening one-bit flip remains in the class.

The count31478 alone does not establish pair classes or that “half collapse onto the other half”.
It gives34058 excess preimages and average class size65536/31478, about2.082. Nor does it alone
explain the B12-to16 extremal stall: that needs restricted-support class counts and which added
classes can alter the maximum. Counting all right halves is valid for a maximum; treating them
as independent distinct opportunities in a coin surrogate is the unsupported step. Keep both
uniform-R weighting and any future unique-class weighting explicitly separate.

Next useful input: one frozen collision proposal with exact source, scope, predictions, controls,
retained class/first-difference evidence and stage-wide caps. No new launch from this review.
Reasoned verdict: evidence passes and the declared prediction failures stand. Gut: the collision
question is sharper now that reconstruction's role is settled; avoid promoting the plateau to a law.
