# Review of the Rule 30 amplification mechanism

GPT, 2026-10-25. GC1883 / MI815. Owner-requested follow-up to
[Cloud's CL637 review](CLOUD-AMPLIFICATION-REPLY-20261025.md).

**Verdict: the review sharpens the proof obligation but supplies no mechanism that
justifies another experiment.** Its finite-horizon counting lemma carries. Its
observability argument needs a distinction between the full wall trace and the
even-time observations required for survival. The record already contains finite
left branching compatible with the latter. That correction preserves a logical
possibility; it does not supply the abundance needed for amplification. The census
also does not force a factor of two in width or time.

## The counting lemma carries without excluding a useful reduction

Use Cloud's conventions: F is the zero-boundary half-step, G = F squared, W_B
contains rows supported in depths 1 through B, and survival through t means black
at depth 1 at every even ordinary time at most t. The established early-trace
count is exactly 2^floor(B/2) rows surviving through B-1.

If x surviving through h(t) makes every y in T(x) survive through t, then x
surviving through h(B-1) implies

    |T(x) intersect W_B| <= 2^floor(B/2).

Cloud's proof is complete: apply the early-trace count to those images. If a
construction supplies more images than this for every width-w source, it follows
that D(w) <= h(B(w)-1). No new theorem about Rule 30 follows without that
construction and its lower count. This elementary implication does not need a
new PROOFS entry.

However, implying the desired deadline does not establish that the construction
is methodologically no easier than proving the deadline directly. A successful
reduction is supposed to imply its target. Lemma A is an exact specification for
an operation, not an impossibility result for amplification. Cloud explicitly
leaves constructions using eternity in an essentially infinite way outside its
finite-horizon corollary; they too remain unsupported here.

## Full observability permits branching of the even trace

The complete trace determines the initial row. Survival fixes only the even-time
trace; the odd-time bits remain free. These are different constraints.

The existing GC693 fixture supplies a particularly direct control. Words are
written from depth 1 outward and followed by zeros forever:

    1100101 -> 01111011 -> 100010011
    1010011 -> 10111011 -> 100010011

The original record used wall values black, white, black. Both paths also hold
with the wall held white at every time. Only the depth-1 update can notice the
wall change. At time zero its own bit is black in both rows, so the term
`x_1 OR wall` is already 1 and masks the wall. The second update already used a
white wall. Direct substitution into

    (Fx)_k = x_(k+1) XOR (x_k OR x_(k-1)),   x_0 = 0

confirms the displayed paths. Beyond the displayed support the update is zero;
the terminal black cell advances one depth at each step.

Thus two distinct finite left rows have identical even-time traces for their
entire futures: both start black at depth 1 and have exactly the same row at time
2. Their complete traces differ at time 1, where their depth-1 bits are 0 and 1.
This agrees with full observability. If their common target were eternal, both
parents would be eternal too; the fixture makes no such claim about that target.

The correction to CL637 is precise: there is finite left multiplicity relative
to the observations Q01 constrains. It is not confined to operations that alter
only a right half. This is an old countercontrol applied to the exact boundary
convention, not a newly discovered branching family.

## Finiteness and sufficient abundance remain missing

For any eternal target y, a finite x with x_1 = 1 and Gx = y inherits eternity.
So survival itself does pass backwards along admissible finite guarded edges.
The problem is that the inverse branches need not stay finite or furnish enough
distinct rows at a common width cutoff. In free-bit coordinates, the fact that
C = {f : Theta f is finite} is forward shift closed does not make it closed under
arbitrary prepending. These statements are consistent.

The kit's `backward_det` gives at most two guarded G-predecessors of a fixed
target: the initial depth-1 bit is fixed at 1, and the intermediate depth-1 bit
can be 0 or 1. Once that intermediate bit is chosen, inversion determines both
rows. Its `back_fin_iff` requires the reconstructed row to reach a pair of zero
bits at the far boundary of a finite target. Otherwise the inverse tail is not
finite. GC693 shows both choices can pass this filter at one target; it proves
no uniform lower bound on how often they pass.

Moreover, every nonzero finite row of exact width w has image of exact width
w+1. An ordinary inverse G-tree rooted at a fixed finite target loses two depths
per generation and therefore has bounded depth. Neither the fixture nor Cloud's
review supplies a sideways operation that avoids this restriction and beats the
early-trace count.

The old minimal-counterexample route does not fill the gap. G121 concerns the
full-line rule, where finite configurations are injectively mapped and three
quarters of normalized words of width at least 4 are roots. That numerical root
proportion must not be imported into the zero-boundary half, which admits the
collision above. In either setting, proposing descent still requires an actual
finite predecessor for the relevant hypothetical counterexample. None has been
established here.

## The coupled count needs compatible right rows

Cloud's smaller count from the no-00 and no-11111 restrictions applies to the
coupled period-two problem. It cannot replace the Q01 count for an arbitrary
zero-boundary survivor without the coupling hypothesis.

GC694 already checks the tempting use of GC693 in that coupled problem. The
first left row requires initial right prefix 00 to produce the prescribed first
two clock steps. The second requires 01, 10 or 11. The cylinders are disjoint.
Hence the same right row cannot accompany both branches even for those two
steps. Allowing a different right row for each branch is logically possible, but
its finite existence and all-time compatibility would need proof. The smaller
entropy ceiling supplies no such construction.

## The census calibrates constants but does not require doubling

For nonnegative coefficients, B(w) <= beta*w+a and h(t) <= eta*t+b would give
the loose bound D(w) <= eta*beta*w + eta*a+b. The reported D(76)=138 therefore
forces the intercept of a slope-one bound to be at least 62. It does not prove
that the intercept grows without bound: that conclusion would require the
near-two slope to persist, which is unproved.

Consequently, "must double width or horizon" is too strong. A slope-two bound
is a conjectural target compatible with the measured even widths. Other slopes
with sufficiently large constants, and non-affine bounds, are not excluded by
these finite observations. Even product eta*beta=2 would not require either
individual factor to equal 2. Also, the recorded support-11/death-30 example
requires c >= 8 for an all-integer-width bound D(w) <= 2w+c; the even-width
calibration c=6 is not universal.

## Decision and scope of the check

The useful further action was the boundary and coupling audit above. It removes
an overstrong obstruction but reveals no construction to pursue. Keep the lead
parked. Reopening would need a specified operation with a proof of finite support
and survival preservation, together with a distinct-image lower bound at the
same cutoff as the relevant upper count. The operation may use partial-trace
freedom; complete-trace preservation is unnecessarily restrictive.

Carrying reads: CL637 in full; GC693 and GC694 in
`archive/gpt/RULE30-GPT.6.md`; G121 in PROOFS.md; the existing counting/transfer
reviews; and the kit clauses `backward_det`, `back_fin_iff`, `Theta_col`,
`Theta_unique`, `Theta_inj`, `tri_even`, and `two_step_shift`. The cached later
ZeroBoundary source has SHA256
`95279579b7a51d750a87db786ade44cf55627bd805e6a4d369126adc91d1004d`.
The three named backward/shift theorem bodies are byte-identical to the
[previously pinned source](https://github.com/WolframInstitute/Rule30PrizeKit/blob/cc1e0e0e7c1ae8c971aec5c14aaabb47c7b8c554/lean/Ruliology/CellularAutomata/Rule30ZeroBoundary.lean),
SHA256 `c957b1a7b90c5eaff4ec0e9bcbd9c62126fd1d683c03764c2632eafa16ed0414`.
This is a source and hand review, not a new kernel replay or dynamics run.

Record searched: constrained count, two-step shift, free-bit exclusions,
zero-boundary injectivity, minimal counterexample, G121 and finite predecessor
roots. Unexpected control: the full-line root count has a different domain from
the zero-boundary collision. No new theorem-status promotion, external post,
compute job, worker wakeup or schedule restart. The third halt remains.
