# Task 5: EdgeObservable, response to CL616

GPT, 2026-10-24. Bounded mathematical/source reading, **no experiment run or accepted**. The conjecture remains OPEN. The elementary lemma below is a standard consequence of left-permutivity, not a claimed new prize theorem or kernel-checked submission.

## Sources and scope

Read the exact source of `Rule30TraceEdge`, `Rule30TraceMerge`, `Rule30TraceAmbiguity`, `Rule30FeedbackErasure` and `Rule30FiniteDiagonals` at kit commit **2f63afda261888e04ec57237290e723190914a1d**. Primary source directory: [the pinned kit](https://github.com/WolframInstitute/Rule30PrizeKit/tree/2f63afda261888e04ec57237290e723190914a1d/lean/Ruliology/CellularAutomata). This is a source read, not a Lean replay. Also read the record's B1–B3 and A‴/A⁗ in RULE30-PRIZE.md §8.59, MAP §§6–7 and CL615–616. Separate `record_find.py` searches for `EdgeObservable` and `trace injectivity` found the recent notebook/NOW/MAP pointers, not an earlier solution. The initial combined-term search returned no hits; it was not evidence of individual absence.

Write F(x)(p) = x(p-1) xor (x(p) or x(p+1)). The question asks whether two finite, nonzero initial rows with equal **entire** center traces must have equal left edges. The kit proves the implication to non-eventual-periodicity for every finite nonzero start, hence official Problem 1. It does not prove the premise.

## 1. Plausibility: a real obstruction, not a counterexample

My instinct is **cautiously receptive to edge observability, skeptical of a small universal observation deadline**. The edge itself cannot disappear: an edge a moves exactly to a-t. Consequently, two different-edge rows cannot coalesce as whole configurations at any finite time. The kit's merging examples therefore do not directly produce a counterexample.

But one center bit is insufficient to invert a row: when the center is 0, its next value gives the xor of the left and right neighbors, so changes on the two sides can compensate. When the center is 1, the right input is masked and the next value determines the left neighbor. A different-edge counterexample would need an indefinitely compatible sequence of such compensation, arising from two finite rows. The same-edge ambiguity and feedback-erasure examples demonstrate real information loss, but do not establish this stronger mechanism.

I have neither a different-edge counterexample nor a proof that compensation must end. In particular, arbitrary long **same-edge** ambiguity cannot be used as evidence that a different-edge separation bound fails. Conversely, finite agreement does not establish an infinite collision.

**Scope check resolved:** the displayed easy theorem covers both edges nonnegative. A mixed-sign pair does not need a separate conjecture: restart both evolutions at an integer S greater than both edges and at least 0. The two new edges a-S and b-S are negative, finite support is preserved, and equal complete traces give equal future traces. Thus resolving the both-negative case really would resolve all cases. This does not equate an arbitrary pair with two times of one orbit.

## 2. A genuine limited case, and why the diagonal argument does not yet extend it

**Standard rightmost-disagreement lemma.** Suppose x and y agree at every p>q and differ at q. After t steps they agree at every p>q+t and differ at q+t.

Proof by induction. At p>q+t+1, all three parent cells lie strictly to the right of q+t and agree. At p=q+t+1 the center and right parents agree, while the left parents differ. Left-permutivity makes the two outputs differ. This proves both assertions and the induction.

**Corollary (common right half).** If x and y are finite with different left edges and agree initially for every p>=0, let q be their rightmost initial disagreement. Then q<0; their first center disagreement is exactly at time **-q**. If the edges are a<b, then q>=a, so this is no later than -a. No eventual periodicity or computational bound is assumed. Finiteness can be weakened to existence of that rightmost disagreement.

This is a noncircular special case with an explicit separation time. Its missing hypothesis in the general problem is exactly the unknown right half. It is useful as a control and possibly a small kit convenience lemma, but ordinary permutivity is not new mathematical progress toward the prize; I do not recommend packaging this alone as a substantive submission.

**B2/B3/A⁗ do not currently prove the requested gap-one or bounded-negative-edge cases.** Two separate gaps must be respected:

- A‴ and A⁗ start from repeated blocks in **two adjacent columns**, which permit backward reconstruction and force a white interval. Equality of one arbitrary center trace does not supply that second column. A clocked-center argument that makes it reconstructible has additional hypotheses, absent here. B3 bounds a white run once such a run is established; it does not manufacture one from one-column equality.
- Each fixed edge-relative diagonal j is eventually periodic. At the center, however, a row whose edge began at a is read on **j=t-a**. The statement “for each j there is a settling time T(j)” does not bound T(t-a) by t, and it supplies no common phase agreement between the two configurations. Even an assumed settled band must cover the particular moving indices, with explicit phases and enough structure to turn one trace into the needed spatial comparison.

So “edge diagonals have settled by first possible disagreement” is not yet a sufficient, precisely stated hypothesis. An actual synchronization/reconstruction lemma is missing. I found no nontrivial negative-edge-only theorem from these ingredients in this reading. This is a limitation of the attempted inference, not a proof that such a theorem is impossible.

## 3. Proposed finite kill test — design only, not a job agreement

**Target.** Test a precisely bounded version of Cloud's sharper deadline guess, and look for unexpectedly persistent different-edge agreement. Never describe the result as testing all finite configurations of a given width without fixing their position relative to the center.

**Finite domain E1.** All rows supported in [-6,6], with leftmost black position a in {-6,...,-1}. For each a set x(a)=1, every p<a to 0, and enumerate all bits a+1,...,6; outside the window is 0. There are exactly **8064** rows. Only compare rows of different edges. Width here means support span at most 13, not number of black cells. No translations outside the declared window and no larger follow-up census.

**Observations.** Compute center bits at t=0,...,255 once per row, retaining prefix partitions at H=32,64,128,256. Group by literal trace prefixes rather than executing every pair evolution. For each pair of edges report the largest common-prefix length and a canonical attaining pair (lexicographic initial bit strings), with censoring at 256. Separately test the explicit candidate **first disagreement delta <= -a+8**, for a<b<0. A pair agreeing through time -a+8 refutes that finite-domain candidate. Do not choose c after seeing the maximum.

**Predictions and failure interpretation.** My low-confidence working prediction is no different-edge collision at H=256 in this small positioned box. I do not endorse c=8; it is a predeclared falsification target for the stronger intuition. Agreement to H=256 would surprise me and refute that finite prediction, but remains only a finite witness, not a counterexample to EdgeObservable. No collision would supply a finite-domain separation maximum, not a uniform bound in width or edge depth. A genuinely infinite collision would need an additional exact invariant/certificate covering all times.

**Independent controls.** Use a full expanding zero-background row update, not a truncated fixed window. Independently replay the 16 longest-agreeing different-edge pairs (or all if fewer) with a literal eight-case Rule 30 table; retain whole starts, the first differing bit or censoring, and hashes. Compare every configuration supported in [-2,2] for its first 32 center bits between the two implementations. Check equal-right-half pairs against the exact -q lemma above. Include the kit's same-edge `{1}` versus `{1,2}` feedback-erasure pair as a separate positive agreement control; it must not be misclassified as a different-edge candidate. As an unexpected orientation check, the starts `{-1,0}` and `{0,1}` have center values respectively 0 and 1 after one step. This catches a left/right swap that the symmetric single-seed center trace can hide. Verify enumeration count, uniqueness, edges and the zero extension independently of the evolution engine.

**Proposed caps, requiring an executable specification and both parties' agreement before launch.** Local CPU only, one process, no GPU and no concurrent benchmark; aggregate CPU 180 s, wall 240 s including controls/validation, RSS 512 MiB, output 16 MiB, disk growth 32 MiB. The literal 8064 by 256-bit traces occupy 258048 bytes; even with Python overhead this is a small-memory design, so 512 MiB is a conservative explicit allowance, not the old illustrative GPU ceiling. Confirm actual headroom at launch. Stop on the first mismatch, count/orientation failure, cap, pressure warning or swap-growth stop (256 MiB over baseline); retain a bounded failure packet and unfinished checkpoint, no retry or scope extension. Record source/toolchain digests, machine/baseline, times, memory-sampling semantics and every prediction, including failed ones; progress every 15 seconds or each horizon, whichever comes first. Supervisor design/version and pressure measurement must be frozen with the implementation. No code is supplied, no run claimed, and these caps are a proposal only.

## 4. Circularity and what would change my view

For the official single seed, forbidding equal complete future center traces for every pair F^T(seed), F^(T+P)(seed), P>0, is equivalent to its non-eventual-periodicity. For **every finite nonzero x**, the analogous orbit-pair statement is equivalent to universal finite-start non-eventual-periodicity, a stronger assertion than official Problem 1 alone. The edge inequality follows automatically from P>0.

It is not circular to prove that restricted statement from independent lemmas; it is unhelpful to assume it and present the conditional implication as progress. General EdgeObservable imposes a different, stronger quantifier over arbitrary pairs; it is sufficient, with no converse proved here. The common-right-half lemma avoids that logical circle but does not generally apply to time-separated orbit rows.

The useful next mathematical input would be a checkable condition under which a single trace determines enough right-head information to invoke left reconstruction, or a finite different-edge pair whose long agreement suggests an exact infinite compensation mechanism. Without one, I would not iterate more settled-band reformulations or open a larger census. GPU P2 remains the priority; E1 is parked until deliberately chosen and agreed.
