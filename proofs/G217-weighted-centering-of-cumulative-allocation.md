# weighted centering of cumulative allocation

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT217. weighted centering of
cumulative allocation (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Demand-weighted centering improves the earlier global range bound on cumulative parity allocation.

**What it says.** Center the cumulative imbalance at a weighted median, with weights given by absolute demand gradients. This minimizes the resulting absolute-sum bound and never exceeds the global midpoint estimate.

**Why it matters.** It retains which cumulative values the changing demand actually uses. Seven small cases show improvement over an older absolute bound in four cases, but no general comparison or asymptotic count estimate follows.

**An everyday picture.** Choose a reference value using the points that carry weight, rather than distant extremes that nobody uses.

## The formal statement and proof

**Where:** RULE30-GPT.md GC426 at4c16d30; inequality and median argument copied verbatim below. Local L255 in e831c68 checks centering, breakpoint minimization, midpoint comparison and zero-gradient guard. This is a refinement of G213 by ordinary weighted absolute-value minimization; the seven-case improvements are measurements, not part of the universal theorem.

Keep G213's actual cumulative imbalance B_a and demand gradients g_a=d_a-d_(a+1), including both endpoints. Since sum g_a=0, its exact signed term obeys, for any real c,

    abs(H_(t+1)-H_t) <= (1/2)*sum_a abs(B_a-c)*abs(g_a).

Minimize the right side over c. A weighted median of B_a with weights abs(g_a) attains this convex piecewise-linear minimum; equivalently enumerate its breakpoints B_a. Evaluating at the global range midpoint proves the optimized value is no larger than osc(B)*TV(d)/4. This is ordinary weighted absolute-value minimization applied to G213, not a new median theorem. Telescoping supplies a sufficient discrepancy bound, without an asymptotic estimate or shape assumption. It can still discard signed cancellation.

**Scope:** no universal comparison with G74's original absolute bound or asymptotic count estimate is proved. GC426 retains the exact zero-gradient extremum guard and bounded measured results separately.

**Duplicate guard for G217:** actual nearest G213,G92,G78 read in full. G213 supplies the exact Abel identity and global midpoint estimate; G217 minimizes that same centering bound with actual gradient weights. G92 and G78 close coarse curvature/full-class proxies, not this optimized bound. No uniform bootstrap or general median theorem claimed.
