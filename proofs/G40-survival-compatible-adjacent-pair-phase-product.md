# Survival-compatible adjacent-pair phase product

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT40. Survival-compatible
adjacent-pair phase product"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary
in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Swapping neighbouring odd and even steps shifts a Collatz number's final value by an exact, predictable amount.

**What it says.** Group a step pattern into pairs: two evens, two odds, or a mixed pair. Turning a mixed pair round
(odd-even into even-odd) changes the final value, counted in base 3, by an amount that depends only on where the
pair sits. So the spread of final values over all the swaps is built from independent pieces, and its frequency
fingerprint is a product of simple factors.

**Why it matters.** The Collatz count needs final values to spread out evenly. This gives an exact handle on that
spreading, the Collatz analogue of a random walk built from independent steps.

**An everyday picture.** A row of switches, each adding its own fixed amount to a meter: the spread of possible
readings is the switches' spreads combined.

## The formal statement and proof

**Where:** RULE30-GPT.md G40, 2026-10-06; proof copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9, the count twin. **Status:** complete analytic argument with single-party implementation controls; second-read by Local, 2026-10-06 (see the notes at the head of E2). No aggregate decay claimed.

### G40 theorem and proof: the skeleton phase product

Fix lengthT and endpoint odd count a with3^a>2^T. Partition the coefficient-admissible words into skeletons by recording each adjacent pair as00,11 or mixed, retaining an odd final bit separately. Discard skeletons with no survivors. A skeleton fixes the odd count s at the start t of every pair, and all pair-end coefficient ratios.

For a mixed pair let R=3^s/2^t. Orientation10 has intermediate ratio3R/2 and final ratio3R/4; orientation01 has intermediate ratioR/2 and the same final ratio. Thus, in a surviving skeleton,10 is always allowed;01 is allowed exactly whenR>2. Other prefixes are unchanged by a swap. Therefore the surviving orientations form a full independent binary cube on the free mixed pairs with3^s>2^(t+1); all other mixed pairs are forced10. In particular a skeleton with F free pairs contains exactly2^F words.

Let q(w) be the terminal iterate of the unique representative in[0,2^T), reduced moduloM=3^a. G38's carry-free ternary map applies. Modulo an odd power of3, a local10 composition sends x to(3x+1)/4;01 sends x to(3x+2)/4. Their difference is1/4. The following suffix has lengthT-t-2 and c=a-s-1 odd steps, so its slope is3^c/2^(T-t-2). Hence the final difference is

    Delta_t = 3^(a-s-1)*2^(-(T-t)) modulo3^a.

Negative powers mean multiplicative inverses modulo the odd modulus. The suffix slope depends only on its count, not its other orientations. The differences are therefore additive across all free pairs. If w0 has every mixed pair oriented10, then

    q(w) = q(w0) + sum_t eta_t*Delta_t moduloM,

where eta_t=1 for a free pair oriented01 and0 for10. Uniform sampling in this skeleton makes the eta_t independent fair bits. With e(x)=exp(2*pi*i*x), its normalized Fourier coefficient is exactly

    phi_S(h) = e(h*q(w0)/M) * product_t (1+e(h*Delta_t/M))/2.

Thus its modulus is the product of |cos(pi*h*Delta_t/M)|. This is an identity for the survival-conditioned population inside each skeleton, not an iid assumption on the whole path.

**Aggregate boundary.** If A is the total survivor count and S ranges over surviving skeletons at this endpoint, then

    |phi(h)| <= sum_S (2^F(S)/A)*product_free_t |cos(pi*h*Delta_t/M)|.

This follows by partitioning the uniform population and applying the triangle inequality only between skeletons; cancellation within each cube is retained exactly. For h coprime to3 every free pair gives a strictly smaller than1 factor, since Delta_t has3-adic valuation a-s-1<a. There is no uniform gap from1 as the denominator grows. At a=T the sole all-one word has no free pairs and unit Fourier modulus. This does not preclude decay for an aggregate with other endpoint weights; it does preclude a contraction asserted uniformly at every endpoint. A decay theorem still needs quantitative frequency control and mass bounds for the surviving skeletons.

## Second reader's notes shared with neighbouring proofs

*Copied from the head of PROOFS.md section E2.*

*Second reader's notes (Local, 2026-10-06; chat L007).* Each argument was read line by line, and the load-bearing
identities were checked with independent code, `tests/probes/prizes/collatz_audit_g39_g42.py` (exact arithmetic,
every admissible word to $T = 14$, zero failures). Verdicts: **G39 correct.** The rotation-to-the-minimum step is
the cycle lemma; the lower bound $\binom{T}{a}/T$ is not tight (a class can hold more than one admissible
rotation, since $S_T > 0$ leaves room), which the statement does not claim. One wording: "distinct partial sums
cannot coincide" means partial sums at distinct indices. **G40 correct, and stronger than stated for the affine offset:** the swap
additivity of $f_w(0)$ holds exactly over $\mathbb{Q}$, not only modulo $3^a$ (the terminal value $q$ itself also
carries $3^a r / 2^T$ with a representative $r$ that changes under a swap, so for $q$ the statement stays modulo
$3^a$; GPT's precision in G007, taken), by a direct route that needs no ternary map:
$f_w(0) = \sum_{i:\,w_i = 1} 3^{m_i} / 2^{T - i + 1}$ with $m_i$ the number of ones after position $i$, and swapping a
free pair from 10 to 01 moves one odd step one place later without changing any $m_i$, which adds exactly
$3^{a-s-1} 2^{-(T-t)}$. **G41 correct.** The mode argument, both Chernoff bounds and the transfer through G39 check;
the minimum of $2p(1-p)$ over the interval is at $p = 1 - \varepsilon$ as used. **G42 correct.** The identity
$2^T q = 3^a r + \sum_{\text{odd } j} 2^j 3^{a - S_{j+1}}$ was verified on every admissible word to $T = 10$; the
family's sum is exactly $20480/3103353$ and the modulus is at least $0.9934$.
