# Larger-L CQ01 outcome — GC1817 / MI750

**COMPLETE / PASS, finite numerical evidence.** Read full L904 at
`12a53d31b5308a44a7ed3aea284a2a276c40db76`, its instinct note and post-run
docstring, all6817 result records by file validation/arithmetic, all retained
controls, the complete log and terminal receipt. The one GC1816 stage has
completed; its permission is consumed. No physical control/census/witness
simulation, GPU or Lean job was run by GPT.

## Evidence bindings and outcome

Packet `cited/cq01-census-20261024-2041/`, stat digests verified on downloaded
bytes through verified TLS with an8MiB bound per file:

| File | Bytes | SHA256 |
|---|---:|---|
| cq01_result.json | 5044216 | 645fc352943858b69edd024ad21a2d1a09f84dabed22060a26d783af0c73c70b |
| receipts.json | 4041 | 261d255f9e691d7a8c4aadc436c0e05ce67804a66461d993e25175f35de3145d |
| cq01_census.log | 795 | 56420233942c4c2e9f3c60dc3dd56a32ac7f68fab7db35019686bd6582cb04cb |

Runner793f12b06a4b18375f7892f979777df3fe1523d4ac129ce74cdc1d2d1a17f33b
and W1A3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883
match the exact acceptance, result and receipt. The command/scope is400/16/800.
The historical accepted validator passes the actual result. Independent file
checks confirm unique full grid, integer domains, lane/count bounds, witness
bits/lengths/right-lane binding, monotonicity, zero censoring and the17 recorded
L400 witness results. The receipt's result digest matches the downloaded bytes;
its full log tail equals the log. L904's code change is only an OUTCOME docstring.

All five base checks pass, four actual mutant reports catch their faults, and
21 gate controls pass. Every full record in the1377-row intersection with the
first run agrees, including **both witness arrays**, not just E/count/minimum
lane. L0/all-lane and B0/single-lane boundary counts also agree. This is a strong
retained-data consistency check across horizons, not an independent engine
proof of every census value.

| L | E(L,0) | E(L,4) | E(L,8) | E(L,12) | E(L,16) |
|---|---:|---:|---:|---:|---:|
| 80 | 81 | 82 | 89 | 90 | 90 |
| 100 | 102 | 104 | 110 | 111 | 112 |
| 200 | 201 | 205 | 210 | 210 | 212 |
| 300 | 301 | 304 | 307 | 315 | 315 |
| 400 | 401 | 405 | 408 | 414 | 417 |

E(400,16)=417, four maximizers, minimum lane9787, so n*=208. Maximum E-L=22
occurs at L377,B11..16 (E399): white-run length21, then black. Maximum right
gain20. All L903 predictions hold on their stated finite domain: no E-L>25,
417 in[401,430], and E(L,0)=L+1 at228/401 L. The >40 diagnostic is not met.
The nine band maxima17,16,16,19,20,21,21,22,17 reproduce. Growth from17 to22
rules out extending that particular observed17 bound, not every constant bound.

## Terminal accounting

Stage elapsed8.0s; step wall6.19s; time-l real6.00s, CPU5.95s. Sampled group
RSS117276672bytes, time-l process maximum117194752bytes, six monitor samples.
Two peak group members comprise the time wrapper and census child; zero Lean
processes. Preflight passes, exit0, zero group members after cleanup, no final
problems. Artifacts5047384bytes and log795bytes fit50MiB/10MiB; all wall/CPU/RSS
caps met. Pressure level1, free percentage66 before/after, zero swap growth,
disk above5GiB. These are retained aggregates/endpoints, not system-wide peaks
or complete pressure trajectories. The short run has full output/control and
source bindings; per-B timing alone would not prove that no work was skipped.
B16 pass0.92s is below the2.36s estimate; no timing law is inferred.

L904's40 additional interior resimulations and flipped-bit checks are reported
outside the stage. Their script, seed and individual receipts are not in this
three-file packet. They remain Local-reported, not independently read or
retroactively included in the exact agreement. No recovery/repetition requested.

## Carrying read of the coin interpretation

B0 determines Psi(empty) at depths1..401 by E(d-1,0)=d. Recomputed228 black
positions and gap histogram(127,59,24,10,4,4) for lengths0..5 agree. This counts
the initial gap before the first black using a virtual black at depth0; the
last observed depth401 is black, so no trailing partial gap is omitted. The
weighted gaps sum to173 whites. With p=228/401,q=173/401, expected geometric
counts228*p*q^k reproduce L904's displayed numbers; the omitted >=6 category
has expectation about1.47 and observed0. This descriptive fitted comparison
is not a calibrated goodness-of-fit test or a proof of Bernoulli behavior.

The displayed model medians8,11,15,18,21 reproduce for **D=white-gap+1**, under
the surrogate F_D(m)=(1-q^m)^(401*2^B); measured6,12,17,22,22 use that same
D convention. They are not medians for white-run length itself. More crucially,
the401 positions within one R are not independent even under an iid-bit model:
if d_R(L)>L+1 then d_R(L+1)=d_R(L), so the residual waiting time decreases by1.
The retained B0 column satisfies this exact countdown identity throughout.
Thus the iid-waiting-times maximum is only a crude surrogate. Its median miss
and B12-to16 stall do not by themselves establish heterogeneous densities or
a particular cross-R dependence. The all-R ensemble is deterministic, and
embedding the same R at successive B also cannot supply independent samples.

**Design correction for the planned per-R review:** individual inter-black
gaps have a geometric law under iid bits; the longest run in K bits does not.
For an explicit iid-bit reference at fixed p, compute its finite-length law by
an exact run-avoidance recurrence, without a simulation job: initialize x0=1,
xj=0; for an ell-run threshold update x0'=p*sum(xj) and xj'=q*x(j-1) for
1<=j<ell. After K updates, sum(xj)=P(longest white run<ell). This follows by
conditioning on the next bit and retaining only suffix lengths below ell.
If conditioning on the known first black depth1, use K-1 updates. State whether
initial/trailing runs count; keep one-sided censoring explicit. Fitting p from
each tested word changes calibration and does not automatically justify an
ordinary fixed-p tail probability. Any scan across many R also needs a declared
aggregation/multiplicity policy before interpreting outliers statistically.

Under an actual infinite iid process with0<p<1, infinitely many black bits and
unbounded white runs both hold almost surely (disjoint blocks give failure
probabilities tending to zero). That conditional probability statement does
not transfer to deterministic Psi R from a finite histogram. “Each R's longest
run follows the geometric law” should therefore be replaced in the proposed
kill test by a specified finite-run statistic/reference. This advice concerns
the already proposed analysis, not authorization for new source or computation.

Instinct/niggle: the longest-run versus gap-law distinction is the cheap
adversarial check that matters before interpreting a new batch. It resolves
toward correcting the reference model, while retaining the numerical table.
Gut: clean finite extension, promising descriptive structure, no universal
CQ01 or bounded/unbounded-gap theorem. Per-R source/spec/controls/caps remain
pending; no further stage accepted. W8 retry/W78 held; sandbox work awaits the
maintainers' reply.
