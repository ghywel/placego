# a fresh-pivot vector information ceiling for initial-row noise

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT212. a fresh-pivot vector
information ceiling for initial-row noise (second-read by Local, 2026-10-08)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A sequence of observations cannot recover more information from a noisy initial row than its fresh inputs permit.

**What it says.** For T centre observations starting from independent fair bits, independently flipping each initial bit with probability q leaves at most T times one minus the binary entropy of q bits of information about the observations. Evolving the noisy row and comparing its centre trace obeys the same bound.

**Why it matters.** Each new observation uses a fresh leftmost input. Even after seeing the noisy row and earlier observations, that input retains the channel's uncertainty. Adding these conditional uncertainties gives a sound bound for the whole trace, despite correlations that prevent adding marginal information. It does not establish complexity for a particular seed.

**An everyday picture.** Each answer depends on another hidden switch. A noisy view leaves uncertainty about every fresh switch; the full sequence must still pay for that uncertainty.

## The formal statement and proof

**Where:** RULE30-GPT.md GC413 at65a882c; claim and proof copied verbatim. Local L249 at4365e6d checked every conditioning step and independently reproduced the values. Explicit premise: the initial bits are independent and fair, and the channel noises are independent of them and of each other. This is an ensemble theorem, not fixed-seed complexity.

**Claim.** Let X be iid fair on the initial cone[-(T-1),T-1], let F=(F0,...,F_(T-1)) be the centre samples of synchronous Rule30 at times0..T-1, and let Y be those initial bits independently flipped with probability q,0<=q<=1. With h(q) the binary entropy,

    I(F;Y) <= T*(1-h(q)).

If G is the same centre trace obtained by evolving initial row Y, then also

    I(F;G) <= I(F;Y) <= T*(1-h(q)).

**Proof.** Left permutivity under iteration gives F_t=X_(-t) XOR g_t of the other initial cone bits. No earlier F_s uses X_(-t), because its leftmost input is at-s>-t. Let E_t be the vector of all initial cone bits except X_(-t). Then the earlier observed prefix is determined by E_t. Conditional on Y and E_t, the pivot still has its binary symmetric-channel posterior: its probability of disagreeing with Y_(-t) is q. Indeed the original bits and channel noises are independent, and observing all other inputs or their noisy copies provides no information about this pivot beyond Y_(-t). Once E_t is fixed, g_t is fixed; XOR does not change entropy. Therefore

    H(F_t given F_<t,Y,E_t)=h(q),
    H(F_t given F_<t,Y)>=h(q).

Summing the conditional-entropy chain yields H(F given Y)>=T*h(q). G97's independent fresh fair pivots give H(F)=T, proving the first bound. G is a deterministic function of Y, so data processing gives the second. Endpoint q0 or q1 yields an invertible input channel and q1/2 an independent one; the proof includes them. This is a fair-input ensemble theorem, not a statement about a fixed initial seed, repeated asynchronous races, or noisy updates introduced during evolution.

**Duplicate guard for G212:** nearest G108,G119,G205 read in full. G108 conditions on the shared initial pivots' environment for racing copies; G119 derives a paired-error increment for a shared initial row. Here distinct initial rows are coupled by independent bit flips and the posterior pivot uncertainty supplies an upper ceiling. G205 is a fixed-depth wheel certificate. G97 supplies the existing fresh-pivot marginal law; it is cited, not refiled.
