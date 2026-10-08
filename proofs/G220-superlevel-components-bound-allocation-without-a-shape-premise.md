# superlevel components bound allocation without a shape premise

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT220. superlevel components bound
allocation without a shape premise (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Demand superlevel intervals give an allocation bound no worse than both earlier absolute bounds, without assuming demand shape.

**What it says.** Split each demand level into its connected intervals, sum the signed imbalance inside each, then take absolute values. The resulting bound is at most the original weighted absolute sum and at most optimized centering.

**Why it matters.** This removes the need for actual unimodality solely to order the bounds. A uniform count estimate still requires controlling interval imbalance; cancellation between separate intervals and times is discarded.

**An everyday picture.** Group contributions only where the demand level connects them. Empty gaps should not make unrelated contributions into one interval.

## The formal statement and proof

**Where:** RULE30-GPT.md GC432 at925f17e; statement and proof copied verbatim below. Local L258 in 36d0bf2 checks the finite layer identity, interval triangle inequalities, endpoint incidence, zero tails and disconnected guard. This is a finite decomposition refining G213-G217; the seven-case numerical gain is a measurement, not a universal rate estimate.

Let I_a be finitely supported signed class imbalances, B_a=sum_(b<=a) I_b, and d_a>=0 finitely supported. Write its distinct positive heights as0=h_0<h_1<...<h_n. For each j, let C_j be the maximal integer intervals[l,r] on which d_a>=h_j. Define

    E=(1/2)*sum_(j=1)^n (h_j-h_(j-1))*sum_([l,r] in C_j) abs(B_r-B_(l-1)).

Then the exact signed increment S and both comparisons are

    S=(1/2)*sum_a I_a*d_a
      =(1/2)*sum_j (h_j-h_(j-1))*sum_([l,r] in C_j) (B_r-B_(l-1)),
    abs(S)<=E<= (1/2)*sum_a abs(I_a)*d_a,
    E<= (1/2)*min_c sum_a abs(B_a-c)*abs(d_a-d_(a+1)).

**Proof.** The finite identity d_a=sum_j(h_j-h_(j-1))*1_(d_a>=h_j) gives the signed equality after summing I over each interval. Taking absolute values after each interval sum proves abs(S)<=E. Bounding each abs(sum_(a=l)^r I_a) by sum_(a=l)^r abs(I_a), then exchanging the finite sums, proves the comparison with G74's original bound. For any c, abs(B_r-B_(l-1))<=abs(B_r-c)+abs(B_(l-1)-c). At a boundary between a and a+1, the total height weight of component endpoints is exactly abs(d_a-d_(a+1)), including both outer zero tails. Therefore summing the endpoint inequality proves E is no larger than G217's objective for every c, hence its minimum. Zero demand gives E=S=0. No shape assumption or sign restriction on I is used.

Thus summing E over time gives a sufficient discrepancy bound no worse than either previous absolute bound, even when actual demand shape is unresolved. This does not prove a uniform count ratio: actual interval imbalance still needs control. Signed cancellation across separate components or times is discarded.

**Scope:** the actual interval imbalances and signed cancellation across components or time remain uncontrolled. GC432's exact disconnected-level guard and bounded measurements are retained in the source. No uniform count ratio follows.

**Duplicate guard for G220:** actual nearest G218,G217,G213 read in full. G213 supplies the Abel identity, G217 optimizes one common center, and G218 compares that optimized bound with the original under unimodality. G220 instead decomposes arbitrary nonnegative demand into its actual connected superlevel components and bounds their endpoint differences, obtaining both comparisons without a shape premise. This is an elementary finite layer decomposition, not a general transport novelty claim.
