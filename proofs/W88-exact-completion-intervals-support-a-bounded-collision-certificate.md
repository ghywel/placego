# Exact completion intervals support a bounded collision certificate

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G88. Exact completion intervals
support a bounded collision certificate (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

A candidate tree can be cut off using exact bounds on every possible continuation.

**What it says.** For each partial step pattern, calculate the smallest and largest final offset allowed by the growth-factor condition and remaining odd count. A pair of starts four apart can meet only if its required offset difference lies inside the two continuation ranges. Every rejected branch has an explicit arithmetic reason; both next parity choices are covered. A complete tree with no witnesses would exclude this finite class.

**Why it matters.** This offers a certificate rather than a larger uncontrolled scan. The run is preregistered with a node and time cap; hitting either cap proves nothing about the unexplored branches. A separate known collision without the growth-factor restriction tests that genuine witnesses are accepted. The capped run completed in 59 nodes with no candidate, and the positive collision control passed. The count-21 coverage audit passed. The next count, 22, produced genuine counterexamples to universal injectivity; independent review remains pending.

**An everyday picture.** Search a route map, stopping at each fork whose remaining distance cannot reach the destination. Only covering every fork certifies that no route reaches it.

## The formal statement and proof

A paired-prefix search can test the remaining a = 21 question without enumerating all admitted words. Fix target a, horizon t_a, and an admitted prefix of length s, odd count j <= a and intercept B. If a-j > t_a-s there is no completion. Otherwise its attained completion extrema are

    B_min(prefix) = 3^(a-j)*B + 2^s*(3^(a-j)-2^(a-j)),
    B_max(prefix) = 3^(a-j)*B + sum_(i=j to a-1) 3^(a-1-i)*2^floor(log_2(3^i)).

The minimum puts remaining odd positions immediately after the prefix; odd steps increase the ratio, and the final ratio stays at least one, so this completion is admitted. The maximum puts each remaining odd step at its latest barrier-permitted position. Prefix admission implies s <= floor(log_2(3^j)), so none of those positions precedes the prefix. G67's deadline bound proves maximality termwise. Empty remaining sums give the same intercept for both extrema.

For a pair of prefixes from starts n and n+4, a meeting with equal target odd count requires final intercept difference 4*3^a. Prune only if this target is outside [min B_low - max B_high, max B_low - min B_high], or an admission/count/capacity condition fails. The common residue r modulo 2^s can be lifted as r or r+2^s; these exhaust the two next parity choices of the lower start. Each lift determines the upper next parity by its affine equation at r+4. Updating both intercepts and r therefore exhausts every possible paired extension. At depth t_a check the exact offset equality, then realize any witness using n = r + 2*2^t_a and n+4; these have a common width. A complete empty tree is a finite no-collision certificate, not an all-a theorem.

**Controls and capped run, preregistered NOT RUN.** CB1: compare complete tree results with independent direct residue scans for admitted a = 3 to 8, displacement 4; require equality. Unexpected positive control: omit admission, use horizon 9, odd count 2 and displacement 28; compare with the full 512-residue scan and require a nonempty witness set, directly checking every returned meeting. Use unrestricted latest-position extrema in this control, rather than the admitted formula. It exercises acceptance as well as rejection. CB2 blind prediction: no admitted collision at a = 21, displacement 4. Cap at 100000 visited nodes and five seconds; retain any cap failure without an exclusion claim. If complete, report visited/pruned/leaf counts and independently evolve every witness; a refuted blind prediction is retained. No a = 22 search or new large compute job. Prior code enumeration through a = 17 remains Local's result; this is a new bounded certificate method in GPT's reasoning lane. Publish before running and request independent review.


### G88 certificate controls and audit preregistration (2026-10-06)

CB1 passes six admitted tree/direct comparisons and 722 attained prefix-extrema controls. Its unexpected unrestricted positive case completes with 53 visited nodes, 24 pruned nodes and three accepting leaves: residues 85, 424 and 426 modulo 512. The independent direct scan verifies these meetings, so the witness-acceptance branch is exercised.

CB2 completes the a = 21, displacement-four tree in 59 visited nodes, with 30 pruned nodes and no accepting leaves. The blind no-collision prediction HELD. Neither the 100000-node nor five-second cap was reached; the combined probes took under one second on GPT's Intel host. Predictions and scripts were published at da98314. No control failed and no a = 22 search occurred. This complete finite search, together with G84's displacement reduction, supports exclusion of the a = 21 class. A separate residue-cover audit and independent proof review remain pending before marking the extension finalized. The a <= 20 result and its pending independent review are unchanged; no all-a or prize claim.

Probes: `tests/probes/prizes/collatz_gpt_sixth_branch.py` and `tests/probes/prizes/collatz_gpt_collision_tree.py`.

**Next independent audit, preregistered NOT RUN.** RC1: export the 30 rejected prefix residue classes, then verify each using independent direct prefix trajectories, completion-offset extrema and an explicit reason (admission, capacity, count or target outside the offset interval). Require pairwise disjoint classes and exact total covered mass 2^33, counting a length-s class as 2^(33-s) residues. Predict full coverage and no valid class rejected; retain any failure and reopen the a = 21 claim. Store the certificate data outside Git; publish the reproducible checker and its counts. This audits the implementation's coverage rather than rerunning a larger population. RC2 unexpected negative controls: delete one cut, duplicate a cut, and claim the whole root is rejectable; require the auditor to reject all three certificates for insufficient coverage, overlap and invalid arithmetic respectively. BN1, preregistered NOT RUN: after RC1-RC2 pass, test a = 22 to 24 with a cumulative 100000-node/five-second tree budget. Before each class verify its exact normalized span is less than 8; G83 then reduces every possible same-count collision to displacement 4. Blind prediction: no collision in these classes. Audit each complete empty tree with the independent residue-cover checker; stop on a witness, cap or failed span prerequisite and retain it. This is the only further range registered; no larger search or all-a inference.


### G88 residue-cover audit and retained blind refutation (2026-10-06)

RC1 passes: 30 pairwise disjoint rejected residue classes cover all 8589934592 residues modulo 2^33. Independent direct-prefix and position-sum checks justify 17 admission rejections and 13 offset-interval rejections. RC2 rejects a missing class, a duplicated class and an invalid root rejection for the predicted reasons. Thus the count-21 finite exclusion passes the separate coverage audit; independent model review remains pending.

BN1's blind no-collision prediction is REFUTED at a = 22. That tree completes in 647 visited nodes with 319 rejected nodes and five accepting leaves. It stops there as preregistered; a = 23 and 24 were not run. The span prerequisite R_22 < 8 passes. All five accepted residues yield positive same-width starts four apart, 22 odd steps each, coefficient admission at every prefix and equal terminals after 34 steps. Least-residue starts were additionally checked with two direct update formulas and independent odd-position intercept sums. The combined audit/search took under one second; no cap was reached. Predictions at 6c69d5e. No instrument control failed; the blind mathematical prediction failed and is retained.

Certificates and witness data are saved outside Git; the reproducible audit script is `tests/probes/prizes/collatz_gpt_cover_audit.py`. The a = 22 accepting/rejected partition has not yet had a separate coverage audit, so five found pairs is not yet asserted to be the exhaustive family count. The counterexamples themselves already refute all-a admitted injectivity.

**Next audit, preregistered NOT RUN.** RC3: independently check the a = 22 partition consisting of 319 rejected classes and five singleton accepting residues. Validate every rejection and every witness from direct trajectories and position sums, require disjointness and total mass 2^34, and reject a corrupted accepting residue. Also require the independent root span to be less than 8 and every accepted pair to first meet at step 34. Predict full coverage and five valid accepted classes; retain any failure. Do not resume the stopped a = 23–24 search. Independent Local review remains queued for return; this is not a prize candidate.
