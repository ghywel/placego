# CQ01 per-R source review — GC1818 / MI751

**Review complete with corrections; revision 3 is not accepted for launch.**
Full L905 at `cf1897fb6c5b510f253a309d8241f37b8ed1a1b8`, its instinct
addendum, all 553 source lines, and the reused source/retained bindings were read.
The mathematical statistic is useful. Repair the numeric gate and scope wording
in one revision; keep the proposed scope and caps. No census, physical control,
GPU or Lean job was run by GPT.

## Source and mathematical findings

- Runner: `bce390987b00754cd8a95b7ed518df1cba0a176f453ac7912710e0abdec1807c`.
- Census: `b46a07a31a4ffa3e867fad707ba510a1f84806b345134dd506691bc442216d59`.
  Every function AST equals the previously accepted 793f12b0 version; the
  intervening change is documentation. The existing dynamics review carries.
- W1A: `3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883`.
- All 18 hard-coded E/count/least-lane bindings match the actual retained L904
  result, digest645fc352. No values were inferred from the ledger alone.

The little-endian transpose puts lane r in column r, depth k in row k. The
window count subtracts depth1, and the longest-window recurrence resets before
depth2 and retains the trailing open run. Thus both statistics concern exactly
799 bits at stage scope. Closed runs include the virtual boundary at depth0;
pooled gaps instead require a previous actual black. The max-gap binding starts
at black depths at most400, including the virtual boundary. E(400,16)=417,
with the full-lane census binding, ensures all such starts have a closing black
within the recorded horizon; no censored tail is silently used for that binding.

The run-avoidance recurrence correctly retains suffix states0..ell-1 and removes
paths reaching ell whites. F(ell)=P(M<ell), G uses that same strict inequality,
and the mean identity is sum over ell>=1 of1-F(ell). The adaptive truncation is
a numerical approximation to the exact finite law: in exact arithmetic its
remaining mean tail is at most799 times the stopping tail probability. The
implementation uses ordinary floats, not certified probability intervals. This
is adequate for the declared descriptive margins, not a rigorous hypothesis
test. After the last evaluated threshold G=1 and the exact F is increasing, so
an omitted upper tail cannot create a larger CDF discrepancy. The declared
single fitted p and absence of per-R p-values address GC1817's main objection.

Two interpretation corrections:

1. **Finite-prefix collisions do not prove failure of infinite injectivity.**
   Fewer than65536 prefixes at depth800 means the map R -> Psi(R)[1..800]
   loses information at that horizon. Two sequences can agree for800 bits and
   differ at801. Conversely,65536 distinct prefixes by depth64 establishes
   injectivity on these65536 right halves, even for their infinite sequences;
   it does not establish it for all finite right supports. Correct L905 and the
   docstring's last counterfactual before interpreting the run.
2. **The pooled geometric curve is an approximation for completed gaps in a
   finite window.** For depth1 fixed black and depths2..K iid Bernoulli(p),
   the exact expected number of closed gaps of length j per lane is
   p*q^j*[1+(K-j-2)*p] for0<=j<=K-2, and zero otherwise, q=1-p.
   The first term is the gap starting at depth1; each of the K-j-2 other
   possible starts contributes p^2*q^j. Their total is(K-1)*p.
   The declared N*p*q^j instead uses the observed number N of completed gaps
   and the infinite-gap shape. With N replaced by its mean and K=800, the
   finite-window/curve ratio is1+(q/p-j)/799. This is a small but systematic
   boundary effect, not evidence against iid bits. Either label the existing
   curve as this descriptive approximation and quantify the effect on the
   compared lengths, or implement the exact finite expectation in the repaired
   source with its own literal controls. Do not call this a calibrated test.
   The hand check K=2 is decisive: one possible completed gap of length0 has
   expectation p, whereas the mean-N geometric curve gives p^2.

Passing the stated summary margins would show agreement of those summaries
with that reference; it would not identify an iid process or establish
independence across right halves. Intermediate results between the prediction
and counterfactual margins are inconclusive by those criteria, not a forced
choice between exhaustive alternatives. No finite run settles CQ01 or uniform
bounded/unbounded white gaps.

## Concrete gate defect and repair

All39 committed gate fixtures pass when run on the two handmade lanes only.
No engine or physical controls were invoked. From that same valid packet,
each of the following six single-field mutations is **falsely accepted**:
`density.mean_count`, `density.sd_count`, `density.binomial_sd_count`,
`window.mean`, `window.D`, `window.reference_mean` replaced by NaN.
The cause is that float types are admitted and `abs(NaN - expected) > tol`
is false. The actual JSON-file matcher also returned pass for NaN sd_count,
D and reference_mean: Python's default JSON decoder accepts the token.

Require finite numbers before every arithmetic comparison, with appropriate
bounds/nonnegativity. Reject NaN and infinities on input, including numeric
exponent overflow, and prevent nonfinite output serialization. Keep fail-closed
exception handling. Add fixtures for every numeric family, preserving a valid
positive packet and the legitimate near-one CDF rounding case.

The schema also accepts a dictionary for each of `elapsed_s`, `started` and
`finished`, and negative values for all three timing fields. Give these their
stated types/domains; elapsed/timing numbers must be finite and nonnegative.
The supervisor remains the operational cap authority; child timing labels
are measurements, not independent total CPU or system peaks.

**Unexpected check:** the fixture loop checks only the diagnostic category
(`types:`, `keys:`, `domains:`, `bindings:`, `arithmetic:`, `completion:`).
It does not establish L905's stronger claim that each fixture fails at its
own specific obligation: another earlier obligation in the same category
would pass that check. Compare the full expected diagnostic or a stable
obligation identifier, or weaken the coverage claim to category coverage.
Add a literal stage-scope gap-binding fixture without running the stage.

A changed but in-range `longest.max_start` also passes: the gate checks range
and endpoint plausibility, not the actual lane bits. This is a scope limit of
an aggregate report, not a reason to retain the whole52MB array or replay it.
If an extremal lane later becomes a mathematical lead, retain its bounded
bit string or another carrying witness before treating it as independently
checked. Existing18 census bindings remain useful controls, not proofs of
all new histograms.

## Resource and execution review

The proposed single stage is `stage OUT 16 800`, fresh absolute OUT,600s stage,
step wall and child CPU,4GiB sampled group RSS,50MiB artifacts and10MiB log.
The wrapper pins both dependencies, runs its controls/mutants in the same child,
uses one child under W1A, and inherits pressure/free-memory stops,256MiB swap
growth stop,5GiB free-disk minimum, monitoring/finalization and group cleanup.
Retain failure receipts as well as success; no rerun or wider scope follows.

The main byte array is52,494,336bytes. At the largest prefix, packbits adds
6,553,600bytes; unique/sorting can hold several packed copies and index arrays.
The simultaneously live per-lane int64/Boolean statistics, temporary masks,
reconstruction vectors, JSON summaries, NumPy and interpreter must also be
counted. An allowance below1GiB is plausible from these allocations, while
4GiB is the enforced stop, not a measurement or a promise of system headroom.
On16GiB unified memory the inherited available-memory/pressure checks are
still required. This CPU stage has no Metal allocation or GPU timing claim.
The under60s cost prediction remains untested, within the600s stop.

Three disclosed tiny development attempts remain prior exposure, including
revision2's CDF rounding failure. They were not GPT-accepted launches or
independently reviewed outcome packets. No rerun to recover them is requested.

## Verdict and next action

Revise the numeric/metadata gate, add the boundary fixtures, and correct the
finite-prefix and finite-gap-reference wording. Publish the new exact source
hash at the same16/800 scope and caps for a delta review. Revision3 remains
unaccepted; no stage launched/completed is inferred from this review.

Niggle sweep: nonfinite comparison, finite-prefix inference and closed-gap
selection all had concrete cheap checks; each resolves toward the corrections
above. Reasoned verdict: the core statistic/source mapping carries, the gate
must be repaired. Gut: the useful next step is one consolidated correction,
not another wider census or a new theorem claim. Existing W8 retry/W78 holds
and the pending maintainer response are unchanged.
