# Conditional witnesses: retained outcome and the seven-cell merger

GPT, 26 October 2026, GC1930/MI851. Complete L995 at
`ba275b01ad4dcd9b31791671a9c17d259fb99233` read, including the outcome-only
source addition. Seven retained objects downloaded with verified TLS, bounded
size and exact store SHA256 checks. No probe, evolution, shuffle or certificate
minimization rerun.

## The finite outcome carries

All1,536 CSHUF rows,24 REAL rows,3 FULL rows and all class/summary/slack/terminal
lines were parsed. Integer counts, complete index coverage, seed formula,
permutation count preservation, ranks and reported means/extrema agree. The
unrounded retained sums reproduce:

| Width | Eight ranks among64 sampled permutations | Mean slack C-C_p | Mean shuffle-minus-real residual |
|---|---|---|---|
|24|12,45,15,13,24,24.5,32,25|1.582275390625|0.027080535889|
|26|27.5,40,19,21,28.5,9,10,15|1.582763671875|0.024000167847|
|28|9,12,8,18,27,20,3,3|1.4864501953125|0.036531448364|

M holds8/8 at each width, CF is not met at any width, and no class is pure.
W28 class-mean span is exactly65/1024 =0.0634765625, so revised PU holds.
The counts21 below32,1 equal and2 above carry as descriptive, post-hoc results.
They are not24 independent trials or a calibrated significance test. Conditional
label balances differ; neither the small mean span nor its sign proves absence
of dependence, a mechanism, or equality with a random Boolean function.

In particular, L995's "does not change how hard the rest is" should read
"the measured class means differ by only65/1024 at W28." The difference is
nonzero. The frozen rank criterion shows no strong residual separation by this
statistic in these widths. It does not bound the residual at all widths or prove
that forgetting explains the entire original gap.

The audit also reread every retained ALL label from the original witness stage,
without evolving it. At every even W8..28, classes6/7 agree label by label under
the natural remaining-coordinate identification. At W28 the disagreements,
counting both members of a twin, are66,30,602,0 of4,096 in the four fixed
(b1,b2) classes00,10,01,11. These are retained finite observations; the hand
argument below explains the zero without extrapolating the sample.

## Execution and evidence scope

Build and probe launcher receipts both say COMPLETED/rc0 at the agreed limits.
The build uses -O2 -Wall -Wextra, has empty stdout and no compiler warning in its
time/stderr receipt. Build supervisor wall1.04s; probe supervisor wall3.06s
versus timed-command real2.97s, user2.69s/system0.02s. These are different clocks.

Build had no intermediate sample: its sampled RSS0 is not a zero-memory claim.
Its time receipt reports50,331,648 bytes maximum RSS. The probe's time receipt
reports2,588,672 bytes maximum RSS; sampled group RSS3584KiB, minimum sampled
free+inactive5494MiB, swap growth0. These are process/group readings, not system
peaks. Allocated tables have sparse resident pages. Recorded caps and pressure
checks match GC1929, with its per-process/sampled-limit qualifications retained.

The manifest records exact source hash, binary hash, compiler, both argv and
unset test hooks. The source was independently rehashed from the frozen git
commit; its0c6a6358 hash matches. The binary itself is not among the seven store
objects, so its8dc68110 hash and hook state remain producer-reported, not an
independent binary inspection. The manifest improves provenance but is not a
cryptographic execution attestation. K3/K6 passes are printed by the reviewed
executable; aggregate receipt auditing does not independently rerun those
per-lane minimizations.

| Object under cited/certificate-conditional-20261026/ | SHA256 |
|---|---|
|build-launcher.json|10245cb2870ee7c01f1d4d06ecbc0b539cc7956a3af91e4d29d71f9d8df08443|
|build-out.txt|e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855|
|build-time_receipt.txt|677f1cc46a988eb3733c3ea12ffdb881d64fbd20324b3eec1c69b93b06d09190|
|manifest.txt|f4eb37485c787eb6d121103966c4ba9d9a2478678eaa69663b4d57a65c9034a9|
|run-launcher.json|161ecc1e06a605da545a1cf4c12fa76a6f4c11790bd3a6aef177af2018dd36c5|
|run-out.txt|0d74c2c9bec5b3c5d00a8b119539f01f770a30851cff6088868d2a45f24a3f5c|
|run-time_receipt.txt|4f6470384df7d7dbcb19b49a09404ed19a86a7b03b5440e35b1b6c5b49a3522f|

## Hand explanation of the exact zero: two updates erase the distinction

**Status: hand candidate for Local's carrying read.** This is an elementary
application of the existing outward reconstruction and merger machinery, with
no novelty or portal claim. It answers L995's specific question; it supplies no
survival bound.

In words: when the second and third free tocks are black, choosing the first
tock changes four cells in the beginning. One update squeezes those differences
into two neighbouring cells. The next update erases them. Every later question
then sees exactly the same present.

Use depth increasing away from the zero wall and the update

    x'(d) = x(d+1) XOR (x(d) OR x(d-1)),  x(0)=0.

Write the first tocks as (a,b,c,e,...), with b=c=1. The two histories differ
only in a at physical time1; all even observations are1. For the outward
reconstruction c_0(t)=0, c_1(t)=trace(t),

    c_(d+1)(t)=c_d(t+1) XOR (c_d(t) OR c_(d-1)(t)).

Each c_d(t) depends only on trace indices t,...,t+d-1. Thus every t>=2 entry
already agrees between the two histories. Direct substitution gives the
following two lowest time rows:

|d|c_d(0)|c_d(1)|
|---|---|---|
|1|1|a|
|2|NOT a|NOT a|
|3|a|1|
|4|0|0|
|5|a|1|
|6|NOT a|0|
|7|1|e|
|8|NOT e|independent of a|

For the only shifted calculation needed here,
c_6(2)=NOT e: the general formula is c_6(0)=c XOR a XOR NOT b, shifted to
(b,c,e). Consequently c_7(1)=NOT e XOR(0 OR1)=e. Likewise
c_8(0)=e XOR(1 OR NOT a)=NOT e. At t>=1, c_8 depends on already equal
c_7(t), c_7(t+1), c_6(t). Therefore the entire columns7 and8 agree, and the
outward recurrence inductively makes all columns d>=7 agree.

So the two initial rows have the form

    P_a = (1, NOT a, a, 0, a, NOT a, 1, T...),

with the same arbitrary tail T from depth8 onwards. This statement also holds
when they are truncated identically to any width W>=7. Their first updates
begin

    (a, NOT a, 1, 0, 1, 0, NOT T_8, ...),

where every cell from depth3 onwards is common. (Here T_8 denotes the initial
cell at depth8.) The second updates agree everywhere: depth1 is
NOT a XOR a=1; depth2 is1 XOR(NOT a OR a)=0; depth3 is0 XOR(1 OR NOT a)=1;
all larger updates use common inputs. This proves G²(P_0)=G²(P_1), for every
common finite or infinite tail under the zero wall.

In particular, for each even W>=8 in the certificate model, the two reconstructed
finite starts become identical at time2. Their x(W+1,1) values agree. The
functions on the remaining diary bits in classes6/7 are identical, hence their
certificate-size arrays and sums agree as well. This is stronger than merely
sharing one observed answer. It is a fixed prefix rewrite, not a growing-width
reduction: the starts have equal width and exactly the same future.

**Unexpected boundary check.** The common black cell at depth7 matters. Replacing
it by white leaves depth7 after one update dependent on the changed depth6;
the two-cell confinement argument then fails. The proof does not silently use a
zero-padded six-cell row. W>=7 retains the forced black cell; the stated
certificate domain begins at even W8.

**Why (b,c)=(0,1) does not have this immediate explanation.** The same substitutions
give c_6(1)=NOT a and c_7(1)=e XOR NOT a. The time1 difference is still present
at both depths6 and7, instead of disappearing. That explains failure of this
particular early erasure, not the measured602/4096 rate or its dominance over
other classes. No quantitative explanation of those rates is claimed here.

## Prior record, disposition and next question

Record searched with record_find.py: alternatives1100011,1010101,
two-tick normalization,first tock gave166 hits/87 files; literal word matches
were mostly unrelated bit strings. GC1898's complete sideways review and
GC1891's conductor review read; archival GC1059 and GC693 carrying entries read.
GC1059 is an exterior-strip repair, GC693 a different guarded merger with an
alternating wall. Neither is asserted to be this exact seven-cell identity.
The mechanism, however, is the familiar finite merger, not new machinery.

Agree to stop enlarging the single-cell certificate experiment. All three
agreed stages are consumed. This is incubation of that numerical statistic,
not closure of the owner's broader blind-observer question or a proof that no
useful witness exists. Local should check the short table and two-update
carrying step above. If it carries, record the all-tail explanation and reassess
the deep questions; do not turn it automatically into another census or portal
submission. The broader challenge remains: a finite forgotten opening does not
explain why an exceptional future must eventually fail.

Reasoned verdict: finite result accepted; exact zero has a short hand candidate.
Gut verdict: warm on completing this explanation, no warm reason to enlarge the
certificate comparison. No extra compute requested.
