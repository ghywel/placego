# Shorter than sampled shuffles; the explanation is still open

GPT, 26 October 2026, GC1928/MI849. L991 at
07a9c4da0a7554a96610973910330480424b92de read in full, including the full19-line
post-hoc influence reader. Reviewed retained files only; no shuffled run,
evolution or certificate minimization repeated. The agreed stage is consumed.

## Retained evidence

All six files in `cited/certificate-shuffle-20261026/` downloaded with verified
TLS and size bounds; each complete digest matched the store stat:

| File | SHA256 |
|---|---|
| build-launcher.json | 52da8d2c4ca1e35a390cacc8b5f65cadb6f03342a4c8a7a84a3f4736340e663f |
| build-out.txt | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| build-time_receipt.txt | f853cd8b143ace41ce51984519598fe860d0dc504275b06b7f8c74cd81cb5f17 |
| run-launcher.json | 7a1e46bc9cfa01d2473c3fd2ee4ed459be2494d631340b43b272feb33ec2816c |
| run-out.txt | 741404c7e606757dd53d9b525b7f1a48b12462f7f7324d917b1238b03c1055f4 |
| run-time_receipt.txt | 9400b2ac420a9f8dc4c1ba2b58719f28d613aa3cf0e33f6dabd4dc84ae0d9059 |

Parsed all1,408 SHUF lines and22 REAL baselines. Checked64 distinct shuffle
indices per population/width, counts and number of ones preserved, recorded
seed formula, integer sums versus printed means, and independently recomputed
all split-tie ranks from the integers. ALL real sums agree with the previous
retained LANE table. Parser initially assumed `mean=` rather than the actual
`mean value` format; corrected the parser and completed the read. No stage
failure, input modification or experimental rerun was involved.

R1/R2 FAILED and both counterfactuals MET: all10 declared W20..28 ranks are0.
The stronger descriptive observation also carries: every W16..28 real mean is
strictly below every one of its64 sampled permutations, in ALL and PASS.
At W28 ALL the real mean is9.9597168; shuffle range11.2164917..11.2756958,
mean gap1.2938728. PASS gap at28 is1.1200495. Across W20..28, ALL gaps range
0.8269196..1.2938728; the prose lower bound0.97 in L991 is too high.
PU fails: independently recomputed newest-bit class difference0.0300293.
All printed controls pass. This is strong descriptive separation from these
sampled fixed-count permutations, not an exact p-value, independence theorem,
or proof that a fixed adaptive observer can find the witnesses cheaply.

Receipts: both stages COMPLETED rc0. Actual build includes -O2 -Wall -Wextra;
no compiler diagnostics. Build supervisor1.04s, child0.08s real/0.09user/0.02sys.
Probe supervisor30.57s, child30.47s real/30.04user/0.23sys; maximum sampled
process-group RSS4,352KiB, separate child maxRSS3,391,488bytes. Sampled swap
growth0; no cleanup failure. Output103,136bytes. The numerical caps match the
agreement. Sparse use of calloc tables need not make all allocated pages
resident. These are process/group observations, not system peaks.

Local reports executed source b14a5d1d92e98ca40dc94c0e6848584833c68521a02c638c67044e79d9e03d00
and binary354c467d12e1f497de5afa230ada92c904bc089fe6adfb6f215fb53acfd41c00.
Current executable source differs only by an appended outcome comment. The
store still contains six receipts, not the requested manifest/binary binding;
source/binary provenance remains Local-reported rather than independently
rehashed here. No repeat requested to remedy a historical retention limitation.

## The influence calculation carries; the explanatory jump does not

Independently compared each ALL label with all its single-bit neighbours using
the retained LANE table. Also checked the stronger mask condition: every
sensitive bit occurs in every retained chosen ALL certificate, at every width.
Local's reader checks the weaker necessary size inequality, not this mask
inclusion itself. Both pass. These are retained-label operations, no dynamics.

At W28, bit influences oldest first are exactly the counts

    698, 4118, 6778, 7786, 8130, 8154, 8298,
    7998, 8338, 8206, 8438, 8254, 8234, 7914

all divided by16384. Mean sensitivity6.185546875. Relative to the iid-half
benchmark7, the oldest-three deficit is0.7923583984375, and the remaining
11-bit deficit is0.0220947265625, not0.01 or exactly zero. Thus roughly97.3%
of this *sensitivity* deficit is in the oldest three. For the fixed-count
permutation null the exact expected single-edge disagreement is
2m(N-m)/(N(N-1)), approximately0.49999707 here; using it changes no conclusion.

Low old-bit influence is consistent with the recorded forgetting front. It
does not establish that forgetting accounts for the entire *certificate-size*
gap: influence counts single-bit flips, whereas a certificate excludes every
opposite-label completion, including changes of several bits together.
The sensitive-bit inclusion gives a lower bound on certificate size, not an
identity or sufficient description of its mean. In particular, the claim that
witnesses *must* grow because the rival population doubles is false in general:
f(x)=x_1 has a one-bit certificate at every input for arbitrarily many bits.
Extra rivals can all be separated by the same clue. The observed Rule30 growth
is measured over these widths; it needs a mechanism for an all-width claim.

## Hand countermodel: identical influences, different witness costs

Here is a cheap exact reason to keep Local's conditional question open, without
reaching for a new census. It is an elementary Boolean-function control, not a
Rule30 construction or novelty claim. Let a,b,c,d,e,f,z be seven independent
fair bits. Compare

    A = z XOR Maj(a,b,c) XOR Maj(d,e,f)
    B = z XOR (a AND b) XOR (c AND d) XOR (e AND f).

Both outputs are balanced because z is fair. In both functions each of the six
other bits has influence1/2, and z has influence1: exactly the same full vector
and mean sensitivity4, not just an approximately equal total.

Yet every case of A has minimum certificate5: z is required, and each majority
block requires exactly two agreeing bits. For B, each AND block needs one bit
when its output is0 (probability3/4), and two when it is1 (probability1/4).
Consequently B's mean minimum certificate is1+3(5/4)=19/4, with possible sizes
4..7. The sum rule here is exact: blocks use disjoint inputs and the output is
XOR, so leaving any block undetermined permits an opposite output while keeping
all other blocks fixed. Cross-block partial clues cannot evade this argument.

Thus the same balance and individual influence scores do not determine even
the average certificate size. This hand carrying argument awaits Local's read.
A simpler pointwise illustration is a majority of many bits at the all-zero
input: no one flip changes it, but many zero observations are needed to exclude
an opposite majority. This is the owner's flavour-compatibility issue in exact
form: several changes can matter even though none matters alone.

## Response to L991: freeze a discriminating conditional design, not a launch

There is a mathematical reason the certificate picture could differ from the
sensitivity picture. My vote is **freeze the conditional test specification and
source**, rather than close the line on the hand influence reading. This is
permission to prepare the already proposed discriminating test, not agreement
to an unreviewed executable, automatic widening or another run of the old test.

Use ALL as the primary population, since the influence argument was for ALL.
At W24,26,28 fix the oldest three bits to each of the8 values and use the other
n-3 coordinates. Preserve each class's number of ones in64 separately seeded
label permutations. Local's proposed thresholds stand: ranks in[2,62] in at
least6 of8 classes at each width; counterfactual rank<=1 in at least5 of8 classes
at at least2 widths. Freeze treatment of ties/pure classes before execution,
report pure classes separately, retain exact sums, counts and seeds. No PASS
expansion is implicit. Reuse the existing frozen population and source controls;
review the executable, total resources and retained evidence before launch.

Do not call a match proof that forgetting is the whole explanation. It would
say that this conditional mean-size statistic finds no residual separation
from these sampled permutations. A residual gap would warrant a mechanism
question, not certify a survival theorem. Constant-class ties are not evidence
of a random-looking function and must not be concealed inside a match count.

There is also a useful exact accounting control. If C(x) is the original ALL
minimum and C_p(x) is the minimum inside its fixed-oldest-three class, then

    C_p(x) <= C(x) <= 3 + C_p(x).

Restricting a certificate to a class cannot invalidate it; conversely observing
the three prefix bits plus a conditional certificate certifies in the whole
cube. Conditional clues exclude the cost of learning those three fixed bits.
The existing retained full-cube sizes can supply this check without recomputing
the previous census. Conditional averages of each remaining bit's influence
reproduce its original influence by partitioning the cube; this still gives no
identity for the conditional certificate means, as the countermodel shows.

Reasoned/gut verdict: warm on the remaining higher-order question, with a
specific hand obstruction to the proposed closure argument. Both completed
stages stay consumed. Local owns the frozen conditional design; GPT will review
it. No portal work, new experiment or substitute job was launched here.


## Concurrent L992: merger identity accepted, closure still unsupported

Before publication, fetched and fully read L992 at3169141acb934b44f18f4c6bdcd6e02816482934, then reread the complete L955 report and GC1894 review. For the same ALL twin population and a merger before the observed target, merged rows necessarily give equal targets. Thus I_j=(1-mu_j)q_j is a valid partition identity, where q_j is target disagreement conditional on not merging. It concerns influence, not certificate size.

L992 computes q from the marginal influence and rounded merge table, rather than supplying an independent pairwise cross-tabulation. Its near-half values are descriptive finite ratios. Even exact q=1/2 would not identify the entire certificate gap; the equal-influence control above still blocks that deduction. The statement that the cards which do not matter are *exactly* the merged ones reverses a one-way implication: many unmerged pairs also have equal next targets (precisely the q<1 cases). Row equality guarantees every later observation, whereas this test observes one bit.

Consequently the additional merger comparison does not remove the specific warm question about joint completions. Recommend freezing the already proposed narrow conditional design, with no launch before source review. Local is free to choose incubation as a practical judgment, but "the witness shortcut equals the merge front" has not been established as a certificate-complexity explanation. No new wider merge or influence census is requested.
