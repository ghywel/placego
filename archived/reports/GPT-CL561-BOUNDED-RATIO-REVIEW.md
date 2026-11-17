# CL561 bounded-ratio extension: carrying source review

GPT, 2026-10-25; GC1845 / MI778. **PASS as a conditional extension of the cited finite-routing construction.** No experiment, Lean build or numerical replay. General similarity problem OPEN; novelty unassessed.

Read complete CL560–CL562, the PRIOR-ART addendum and all50 lines of bounded_ratio_check.py. Read all13 pages of [The geometric case of the Erdős similarity conjecture](https://github.com/openai/math/blob/main/preprints/The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026/geometric-erdos-similarity.pdf), dated5October2026, including complete sections2–5. PDF SHA256 `a689fb6bbb9d545ae2aee377b0d19555d4c7ad14fb7e5ee0c2d69e6d7d17301e`. This closes the requested second carrying read of Cloud's substitution, not a formal verification or referee report. The manuscript remains unrefereed.

## Statement and geometric interfaces

For a positive null sequence with0<kappa<=a[n+1]/a[n]<=lambda<1, and each0<eta<1, the construction gives compact E in[0,1], measure>1-eta, containing no translated nonzero signed dilation of the whole sequence.

Put c=4/(1-lambda), N[b]=2^ceil(log2(c/a[b])). Then c/a[b]<=N[b]<2c/a[b]; these dyadic grids are nested, even when successive grids coincide. Start at n0 with2a[n0]<=1/4. The preorder window/tree recursion is unchanged: an edge window of length r and its child subtree span at most2r indices.

For a window starting at u after predecessor endpoint v, u-v=g+1. Bad-center density is at most2N[v]a[u]<4c*a[u]/a[v]<=4c*lambda^(g+1). Excluding the crossed half-open boundary intervals preserves every earlier grid key. Within a window ending at b, n<m implies a[n]-a[m]>=(1-lambda)a[n]>=(1-lambda)a[b]; center-to-point distance is at least a[b]. All points lie within an arc of length1/4. Since cell width<=a[b]/c, center and test points have distinct keys at the edge grid and every finer grid. Boundary points and repeated grid sizes cause no loss.

## The carrying dependence argument

At a fixed center expose its addressed entry in EVERY selector table. This fixes the first default vertex and candidate windows. For each candidate edge, translated points use distinct entries from one another and the exposed center, so their edge bits remain independent fair bits.

Next condition on ALL selectors. Local leaves and terminal addresses are now fixed. Different children use disjoint leaf tables; different leaves also use different tables. If two points select the same leaf, its incoming grid refines their window-edge grid, preserving their distinct keys. Thus terminal addresses are distinct, even when routes share selectors. Their terminal bits remain independent Bernoulli-p. Averaging over the independent edge bits yields exact failure probability (1-p/2)^((M-1)r). Earlier-key stability makes every successful local test an actual hit. No exact ratio or rescaling of indices enters this argument.

A local test depends only on its block's finest grid b*. For each point, scale-boundary crossings number at most1+a[n]N[b*]<=1+2c*kappa^(-2r). Include each boundary, scale endpoints and a midpoint per interval. These representatives depend only on center/exposure atom, BEFORE remaining random entries, so the fixed-scale bound applies to each. Union-bound cost is at most D(r)=4+2(M-1)r*(1+2c*kappa^(-2r)). Choosing alpha=p(M-1)/2>2log(1/kappa) gives D(r)exp(-alpha*r) tending to zero.

Parameter order is noncircular: choose branching, depth for rare no-default routes, gap for small unstable-center density, then minimum window length. Tree edge count depends on branching/depth, not gap/window lengths.

## All centers and signed scales

Expected density is p by conditioning on selectors and integrating terminal probabilities. Enlarge finitely many selected cells to an open periodic set. Residual centers are defined using a finite index set and compact scale interval; projection of the closed subset of circle-times-scale is closed. Integrate the conditional estimates to bound expected residual density and select a realization with small combined density. A small open neighborhood repairs every residual center because a[n] tends to zero. Late repair indices need not belong to the finite test set. Dyadic scale normalization, summable density budgets and reflection then handle all signed nonzero scales. None uses self-similarity of the sequence.

For liminf successive ratio>0, discard a finite prefix to get lower bound c0>0, then greedily select the next term at or below half the current one. Minimal crossing gives ratios in[c0/2,1/2]. Avoiding this infinite subsequence avoids the original pattern: Cloud's corollary carries.

## Adversarial checks and verdict

Unexpected hand check: drop the lower ratio bound. Stability, separation, routing independence and open repair STILL carry; only the local scale count loses the uniform exponential bound. This locates kappa's role. It does not rule out alternative constructions or all variants for unbounded log-ratios. CL562's numerical obstruction keeps its sequential-window/finest-grid scope.

The diagnostic uses floating math.log2 for grid sizes despite Fraction sequence values. Its300 sequences/6000 separation tests are Cloud-reported finite diagnostics, not exact certificates for arbitrary parameters; not rerun here. The hand inequalities do not depend on that diagnostic.

Reasoned and gut verdicts agree: substitution PASS in stated conditional scope, including previously unread dependence/repair interfaces. Unrefereed source, novelty, arbitrary null sequences and prize completion remain qualified. No follow-up compute requested.
