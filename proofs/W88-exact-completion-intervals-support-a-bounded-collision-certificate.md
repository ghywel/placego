# Exact completion intervals support a bounded collision certificate

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G88. Exact completion intervals
support a bounded collision certificate (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

A candidate tree can be cut off using exact bounds on every possible continuation.

**What it says.** For each partial step pattern, calculate the smallest and largest final offset allowed by the growth-factor condition and remaining odd count. A pair of starts four apart can meet only if its required offset difference lies inside the two continuation ranges. Every rejected branch has an explicit arithmetic reason; both next parity choices are covered. A complete tree with no witnesses would exclude this finite class.

**Why it matters.** This offers a certificate rather than a larger uncontrolled scan. The run is preregistered with a node and time cap; hitting either cap proves nothing about the unexplored branches. A separate known collision without the growth-factor restriction tests that genuine witnesses are accepted. Independent review and the run remain pending.

**An everyday picture.** Search a route map, stopping at each fork whose remaining distance cannot reach the destination. Only covering every fork certifies that no route reaches it.

## The formal statement and proof

A paired-prefix search can test the remaining a = 21 question without enumerating all admitted words. Fix target a, horizon t_a, and an admitted prefix of length s, odd count j <= a and intercept B. If a-j > t_a-s there is no completion. Otherwise its attained completion extrema are

    B_min(prefix) = 3^(a-j)*B + 2^s*(3^(a-j)-2^(a-j)),
    B_max(prefix) = 3^(a-j)*B + sum_(i=j to a-1) 3^(a-1-i)*2^floor(log_2(3^i)).

The minimum puts remaining odd positions immediately after the prefix; odd steps increase the ratio, and the final ratio stays at least one, so this completion is admitted. The maximum puts each remaining odd step at its latest barrier-permitted position. Prefix admission implies s <= floor(log_2(3^j)), so none of those positions precedes the prefix. G67's deadline bound proves maximality termwise. Empty remaining sums give the same intercept for both extrema.

For a pair of prefixes from starts n and n+4, a meeting with equal target odd count requires final intercept difference 4*3^a. Prune only if this target is outside [min B_low - max B_high, max B_low - min B_high], or an admission/count/capacity condition fails. The common residue r modulo 2^s can be lifted as r or r+2^s; these exhaust the two next parity choices of the lower start. Each lift determines the upper next parity by its affine equation at r+4. Updating both intercepts and r therefore exhausts every possible paired extension. At depth t_a check the exact offset equality, then realize any witness using n = r + 2*2^t_a and n+4; these have a common width. A complete empty tree is a finite no-collision certificate, not an all-a theorem.

**Controls and capped run, preregistered NOT RUN.** CB1: compare complete tree results with independent direct residue scans for admitted a = 3 to 8, displacement 4; require equality. Unexpected positive control: omit admission, use horizon 9, odd count 2 and displacement 28; compare with the full 512-residue scan and require a nonempty witness set, directly checking every returned meeting. Use unrestricted latest-position extrema in this control, rather than the admitted formula. It exercises acceptance as well as rejection. CB2 blind prediction: no admitted collision at a = 21, displacement 4. Cap at 100000 visited nodes and five seconds; retain any cap failure without an exclusion claim. If complete, report visited/pruned/leaf counts and independently evolve every witness; a refuted blind prediction is retained. No a = 22 search or new large compute job. Prior code enumeration through a = 17 remains Local's result; this is a new bounded certificate method in GPT's reasoning lane. Publish before running and request independent review.
