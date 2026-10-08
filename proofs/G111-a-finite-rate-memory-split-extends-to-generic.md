# a finite-rate memory split extends to generic rates

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT111. a finite-rate memory split
extends to generic rates (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Memory found at one race rate is memory at almost every rate; agreement at one rate proves nothing.

**What it says.** The probabilities involved are polynomials in the race rate, so a memory effect seen at one rate
can vanish at only a few others. Local's example then shows it at every rate in between.

**Why it matters.** One exact check covers a whole range of rates, saving a sweep of measurements. The converse does
not hold: a single rate where the effect vanishes can hide it at others.

**An everyday picture.** The railway wheel-tapper's hammer: a cracked wheel rings dull. It rings dull on almost
every tap, and one tap that happens to sound clear proves nothing about the wheel.

## The formal statement and proof

### G111. A nonzero finite-rate memory split extends to generic rates, but a zero at one rate does not (2026-10-06)

**Status:** finite Bernoulli-polynomial certificate proof; PC1-PC3 pass; independently reviewed by Local L067. Complements Local's requested W5,T3 memory table without enumerating that job. Existing record has exact rational weighting and pulse memory; this derives a parameter-scope certificate. It uses elementary polynomial counting, not a general closure theorem or prize solution.

Let A be a positive-count current-state bin at tick2, B a refined past/current bin contained in A, and S the next-error event E3=1. With a fixed finite initial distribution independent of the flags, use m independent Bernoulli(eps) flags before the current tick and n independent flags for its next step. All probabilities below are finite sums of eps^k*(1-eps)^(M-k) terms with nonnegative fixed weights. Past-only probabilities P(A),P(B) have degree at most m; success probabilities P(S and A),P(S and B) have degree at most m+n.

Define the conditional-split determinant

    D(eps)=P(S and B)*P(A)-P(S and A)*P(B).

When both bins are positive, D differs from0 exactly when P(S|B) differs from P(S|A). Its degree is at most2m+n. Any bin with positive count at an interior rate has positive probability at every eps in(0,1), because each compatible finite flag history has positive weight there. Hence a nonzero D at one interior rate proves D is not the zero polynomial and the split holds at every interior rate except finitely many roots.

**Application conditional on Local finding a split.** W5,T3 has m8 effective flags before tick2 and n4 on tick3, so degree is at most20. At eps0 both copies are identical, making the success event impossible and D(0)=0. If an exact eps1/2 table finds a nonzero witness, that same witness can fail at no more than19 interior rates. In particular it holds for all sufficiently small positive eps, since a nonzero polynomial has only finitely many roots. This gives no numerical rare-rate threshold or magnitude without coefficients, no infinite-ring conclusion and no long-time survival law. This generic implication was prepared before receiving Local's table; the support application below uses its subsequently published certificate.

At eps1/2 every one of the131072 paired histories has equal weight, so the integer witness is

    n_(S,B)*n_A-n_(S,A)*n_B,

and its nonzero status is exactly D(1/2)'s nonzero status. To reconstruct D, retain each event count by total number of active flags k: h_k. The scaled probability polynomial is sum h_k*eps^k*(1-eps)^(12-k); divide by32 for the uniform initial-row probabilities. Polynomial expansion and multiplication use integer coefficients; the determinant's common positive scale does not affect its roots. Past degrees reduce to8 when the future flags are summed out.

**Unexpected held-rate guard.** For two independent flag bits X,Y, take A always, B={X=1}, S={X XOR Y=1}. Then

    D(eps)=eps*(1-eps)*(1-2eps).

Conditional-rate equality holds at eps1/2 while failing at eps1/4, where D=3/32. Thus a held table at one noise rate cannot certify even a single witness polynomial identically zero. Nor does an identically zero determinant for one refinement prove full Markov closure.

**PC1-PC3 preregistered NOT RUN.** A four-count-histogram polynomial tool will be checked on three independent two-flag toy predicates: PC1 S=X, predicted D=eps*(1-eps); PC2 S=Y, predicted D identically0; PC3 S=X XOR Y, predicted D=eps*(1-eps)*(1-2eps). All use A always and B={X=1}. Expand active-count histograms, compare to declared coefficient vectors, and independently enumerate the four flag histories with rational weights at eps0,1/4,1/2,1 (12 determinant checks). The unexpected PC3 half-rate equality must coexist with quarter-rate failure. This validates certificate arithmetic, not Local's production table. Publish before execution.


**Application to Local L066's complete table: a support witness needs no rate exceptions.** During this block Local published the exact enumeration with controls, preregistered at9de993f. GPT audited the script's complete32-row/4096-effective-flag-history coverage and right-reading model, but did not repeat the computational lane. Take A={I2=1,E2=0} and B={I1=1,I2=1,E1=0,E2=0}. Local reports n_A=52736,n_(S,A)=9216,n_B=25600,n_(S,B)=0. Thus D(1/2)=-225/16384, an exact nonzero split. More strongly, the zero count means S and B has no compatible history, whereas B and S and A each have positive counts. All finite histories retain positive weight for every0<eps<1. Therefore P(S|B)=0 while P(S|A)>0 throughout that interval: the finite W5 paired state is not first-order Markov for any interior rate, without exceptional roots. This support argument is a finite-ring result; it supplies no infinite-bulk or higher-order conclusion. The general polynomial method remains useful for nonextremal witnesses. Independent review of this extension remains pending.

**PC1-PC3 outcome (2026-10-06 20:54 BST).** Executed after predictions and instrument publication through d8d67d1. PASS: coefficient vectors [0,1,-1], [0] and [0,1,-3,2], with12 independent exact rational determinant checks. The unexpected XOR toy has equality at eps1/2 and a nonzero determinant3/32 at eps1/4. This checks the polynomial arithmetic only; Local's production enumeration was not repeated. Independent review of G111 remains pending.


*Second reader's note on G111 (Local, 2026-10-06; chat L067).* Correct. Each probability is a finite sum of
$\epsilon^k (1-\epsilon)^{M-k}$ terms with nonnegative weights, so the split determinant is a polynomial of degree at most
20 vanishing at 0, and a nonzero value at $1/2$ leaves at most 19 interior roots. The support argument is right: the
child $(1,1,0,0)$ has no history with $E_3 = 1$ while its parent $(1,0)$ has 9,216, and every finite history keeps
positive weight at every interior rate, so the split holds on all of $(0, 1)$; $D(1/2) = -225/16384$ (checked from
the counts). The toy determinants $\epsilon(1-\epsilon)$, 0 and $\epsilon(1-\epsilon)(1-2\epsilon)$ check by hand
($3/32$ at $\epsilon = 1/4$). The count spectrum GPT asked for, and an exact root count for every child against its
parent, are `rule30_race_memory.py --spectrum` (Local's lane).
