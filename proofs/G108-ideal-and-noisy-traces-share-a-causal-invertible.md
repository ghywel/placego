# ideal and noisy traces share a causal invertible coupling

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT108. ideal and noisy traces
share a causal invertible coupling (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Two individually random traces can remain perfectly related when their shared environment is known.

**What it says.** Conditional on the other initial bits and race schedule, noisy samples equal ideal samples XOR a mask determined by earlier ideal samples. The transformation is a causal bijection, with N+1 bits of conditional mutual information.

**Why it matters.** Marginal iid observations do not make two histories independent. First-tick race errors depend on the previous sampled state. This representation does not determine the error process or a decoherence rate. CT1 and review are pending.

**An everyday picture.** Knowing the key can relate two scrambled films even when each looks random on its own.

## The formal statement and proof

### G108. Shared initial bits give a causal invertible coupling of ideal and noisy traces (2026-10-06)

**Status:** conditional finite-horizon coupling proof; CT1 and independent review pending. Follow-up G97/G102/G107. Existing-record search found the fresh-bit marginal trace law but no paired causal-mask representation. This uses elementary triangular bijections and entropy counting, not a new general coding theorem or prize solution.

Fix a horizon N, a predetermined nonrightward path, and a terminating right-reading race field independent of the fair initial row as in G107. Couple the ideal synchronous and noisy histories from that same row. Write I_t and J_t for their sampled bits, t0..N. Their distinct fresh initial pivots are L_t=p_t-t. Let R contain all initial bits outside these N+1 pivots, and fix R and the entire flag field. The remaining pivot bits xi_t=x_0(L_t) are independent fair.

**Triangular pair representation.** G97 and G107 give

    I_t=xi_t XOR a_t(xi_0,...,xi_(t-1);R),
    J_t=xi_t XOR b_t(xi_0,...,xi_(t-1);R,flags).

Neither expression uses later pivots, which lie strictly to the left of its dependency boundary. Both expose the same current pivot with coefficient1. Inverting the first expression recursively recovers xi_<t from I_<t and R. Cancelling xi_t therefore yields

    J_t=I_t XOR e_t(I_0,...,I_(t-1);R,flags),   e_0=0.

This is causal: the time-t mask needs no current or future ideal sample. The map from I_0..I_N to J_0..J_N is itself a triangular bijection, recoverable successively from either trace when R and flags are known. Each trace separately is uniform conditional on this environment, yet their conditional joint law has only2^(N+1) equally likely pairs, rather than2^(2N+2).

In bits, conditional entropy of each trace and of their pair isN+1; conditional mutual information between the traces isN+1. These are statements conditional on R and flags. They do not make the unconditional coupling invertible, give its unconditional mutual information, or let an observer recover a hidden schedule from one trace. G107's independence of the single trace from the flag field is compatible with this conditional relation.

**Predictable-mask qualification.** Conditional on R and flags, e_t is determined by the past ideal samples. The current ideal sample is fresh fair independent of that past, so it is independent of the current mask under that conditioning. The masks need not be independent over time or independent of past samples. Their law remains the missing joint-history object, not something spatial invariance determines.

**First-tick state dependence.** For a stationary target i, let E_1=I_1 XOR J_1. On the common fair initial row, a right race can change its OR term only if x_0(i)=0. If x_0(i)=1, both OR values are1 and E_1=0. With fresh iid Bernoulli flags of rate0<=eps<1, G102's total injection probability gives

    P(E_1=1 | I_0=1)=0,
    P(E_1=1 | I_0=0)=eps/(4-2eps),
    Cov(E_1,I_0)=-eps/(16-8eps).

The latter follows because I_0 is fair, E_1*I_0 is always0, and E[E_1]=eps/(8-4eps). Thus even the first error is not state-blind or independent of the past observed bit for eps>0. This does not contradict iid marginal samples; it concerns the pairing of the two copies.

**Unexpected causal-mask guard.** Fix old sites1,2 to0,1, let only target0 read its updated right neighbour, and update site1 synchronously. Vary the two fresh pivots old0 and old-1 fairly. Then I_1=old-1 XOR I_0 while J_1=old-1 XOR1, so E_1=1-I_0. Each two-sample trace is uniform, but its partner is a deterministic bijective scramble given this environment. A state-independent fair error bit would be the wrong coupling. No selected-seed, finite cyclic survival or matching upper decoherence rate follows.

**CT1 preregistered NOT RUN.** Reuse NT1's literal right-reading history evaluator and an independent synchronous XOR/OR evaluator. For T1..3, all left/stay paths, all global-row switch schedules and all initial words on-2T..T+1, group by nonpivot initial bits. Require both trace projections bijective within each group, paired support size2^(T+1), and each time-t XOR mask constant for a fixed ideal prefix of length t. Predict135296 paired cases and8736 conditional classes. Independently check the four-pivot-input causal-mask guard above. This is a paired-law audit, not a repeat of NT1's marginal statistic; the existing first-tick weighted G102 control supplies the rate formula. Publish before execution.

*Second reader's note on G108 (Local, 2026-10-06; chat L063).* Correct. Both traces expose the same fresh pivot at
each step with coefficient 1 and use only earlier pivots otherwise, so the second is the first scrambled by a causal
mask. Checked (`rule30_audit_g99_g100.py`, S11): for $T \le 3$, every nonincreasing path, whole-row schedule and
non-pivot assignment, both traces are bijective images of the pivots and $I_t \oplus J_t$ is a function of
$I_0 \ldots I_{t-1}$ alone; the guard gives $E_1 = 1 - I_0$ for all four pivot values. The first-tick rates follow from
G102's verified injection rate. This also tightens the reading of my race run: its survival law treats errors as
injected blindly, while the first error already depends on the observed state.
