# fixed-column temporal complexity

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT64. fixed-column temporal complexity
(second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this
summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

In that Rule 210 family, every fixed column on the right is almost completely predictable.

**What it says.** Take Rule 210 with the blinking wall and an initially empty left half, and any right half that
fits. Using G63, the number of different patterns of length N seen in any fixed right column grows only like a power
of N, not exponentially. Such a column carries no lasting new information: its entropy is zero.

**Why it matters.** It shows how little freedom the right side has in this family, a strong constraint of the kind a
proof needs.

**An everyday picture.** A radio station that only ever plays a handful of jingles: however long you listen, you
learn almost nothing new.

## The formal statement and proof

### G64. Fixed right columns have zero temporal word-count entropy (2026-10-06)

Use G63's strip lemma for all full Rule210 realizations of the0101 wall with the empty initial left row of G26. This class is nonempty by G60; the right half may be infinite or mixed-parity. For each fixed column k>=1 let P_k(N) count all distinct length-N temporal words, across all such realizations and all starting times u>=0. Then

    P_k(N)=O_k(N^(4k+2)),
    limsup as N->infinity of log2(P_k(N))/N=0.

This extends G26's factor-count observation for one particular adjacent stream to every fixed right column in this precisely specified family. It is not a Rule30 theorem, an assertion of zero entropy for the whole CA, or an exclusion of finite mixed-parity witnesses. The constant and exponent depend on k.

**Forced positions.** The effective stream changes across odd times in B={2^j-1:j>=1}; include a virtual boundary-1 for the start of time. G63 forces column k to its known two-phase template except within distance2k of these boundaries. Indeed each constant effective run spans even endpoints[2m,2N]; the lemma trims2(k-1) at each end, and the intervening odd transition time is in B. Every omitted sample is inside the asserted radius; choosing2k is conservative. Outside those neighborhoods the template depends only on the effective run's value, the time parity and k modulo6.

**Uniform word bound.** Fix N,k, set r=2k, L=N+2r and choose M to be the least power of2 with M>=L+1. Thus M<2(L+1). For early starts0<=u<M+r, the enlarged window[u-r,u+N-1+r] ends before2M-1. It contains at most Q=log2(M)+1 boundaries, counting the virtual-1. The unconstrained samples in the word are at most(2r+1)Q. At a fixed start the forced template is already known, so early starts contribute at most

    (M+r)*2^((2r+1)*Q).

For late starts u>=M+r, the enlarged window begins at least M. Consecutive boundaries there are separated by at least2M>L, so it contains at most one. Allow its relative position any of L integer positions, or allow no boundary; choose either effective value independently on each side and either time parity, at most8 template choices. Allow all2r+1 boundary-neighborhood bits arbitrary. Late words contribute at most

    8*(L+1)*2^(2r+1).

These bounds count a superset, including choices that need not have a full realization. Their sum bounds P_k(N). Since 2^((2r+1)Q)=2^(2r+1)*M^(2r+1), it is O_k(N^(2r+2))=O_k(N^(4k+2)). Taking log and dividing by N proves the entropy statement uniformly over starting times. Column0 separately has at most2 words of every length. No finite measurements are used in the all-length proof.

**Unexpected guard: prefix density is insufficient.** Concatenate lists containing every binary word of length m, separated by zero blocks of length2^(2^m). Their black prefix density tends to0, since the previous zero block eventually dwarfs the next list of size O(m*2^m). Yet every binary word occurs, so temporal factor complexity is2^N and entropy1. This illustrates why the arbitrary-start late-window argument is necessary; a sparse prefix count alone would not prove G64. It is a constructed binary-sequence counterexample, not a Rule210 realization.

This is elementary counting from G26/G63 and the explicitly defined word-count entropy, with no literature novelty claim. Earlier G53/G54 bounds concern another family and do not supply the dyadic transition hypothesis here. G63 and this consequence await Local's independent reading. No uniform-in-k or initial-condition-wide conclusion is made.

**Next controls, preregistered NOT RUN.** WC1: k=1..6,N in{1,2,4,8,16,32,64,128}, every start0..4095; directly enumerate enlarged-window boundaries and marked sample positions, checking the early Q bound and late one-boundary bound. WC2: on G60's explicit0101 full realization, compare columns1..6 through time500 with G63's templates at every sample outside the stated boundary neighborhoods, using an independent scalar full evolution. CF: prefix sparsity implies zero factor entropy; refuted analytically by the concatenated-word construction above, without an empirical entropy estimate. These controls validate margins and counting instrumentation, not the entropy limit itself.


### G64 controls outcome (2026-10-06)

WC1 passes196608 windows for k=1..6, lengths1,2,4,8,16,32,64,128 and every start0..4095:3952 early windows obey Q and marked-sample bounds;192656 late windows obey the one-boundary and radius bounds. WC2 passes2524 forced samples of columns1..6 through time500 on G60's explicit scalar full Rule210 realization;482 samples are excluded by the conservative neighborhoods. Probe: `tests/probes/lexicon/rule30_gpt_window_complexity.py`, Python on GPT's Intel host, under1 s. No control failed.

These finite checks validate the counting split and forcing margins; the entropy limit remains the analytic G64 proof, not an empirical estimate. The concatenated-word counterfactual is retained as an analytic counterexample. Independent reading remains queued. This bounded block is complete; next audit the effect of varying initial left support, since G27's arbitrary finite visible prefixes warn against treating one fixed empty-left family as the union of all finite-left families.
