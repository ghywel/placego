# The Mahler window ladder is equivalent to odd-iterate residue avoidance

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT294. The Mahler window ladder is
equivalent to odd-iterate residue avoidance (Local L711, second-read by GPT, 2026-10-14)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

For the stated ladder of fractional windows, a compatible positive integer start must keep every odd iterate in one specified residue class modulo 2^g. A short gap forces a tail above the window; long gaps bound every tail, and the critical equality code cannot come from a positive integer. GPT checked Local's carrying steps in GC1228.

**Why it matters.** This gives an exact arithmetic formulation for each rung. It does not exclude those integer orbits or cover all Mahler codes.

## The formal statement and proof

**PROVED core equivalence.** Provenance: Local L711 at98fbd35e; GPT carrying read RULE30-GPT.md GC1228. The proof below is copied verbatim from that review. Scope corrections are part of the entry; no emptiness or novelty claim. Filing check: proof_dupes --near G294 passed; nearest G131, G50 and G51 were read. G131 concerns Rule 30 rotation factors; G50/G51 supply the coupling and finite windows used here. The ladder is their explicit gap-threshold corollary, not a restatement of their whole statements.

**Statement (Local's L711, carrying steps independently read by GPT).** Put r=2/3. For an integer g>=3 let alpha_g=1/(3*(1-r^g)) and beta_g=(1+r^(g-1))/3. For every a in [alpha_g,beta_g], a real xi>0 keeps all fractional parts of xi*(3/2)^j in [0,a) exactly when xi=n+u_0(n), where n>=1 is an ordinary integer and every pair of consecutive ones in its F(n)=ceil(3n/2) parity code is separated by at least g places. Equivalently every odd F-iterate is congruent to -1/3 modulo 2^g. This is an equivalence, not an assertion that such integers exist or are absent.

**Residue carrying step.** For a positive odd iterate n_j, set M=(3*n_j+1)/2>0 and v=v_2(M). The next v updates while even multiply by 3 and divide by 2, so the next odd iterate is exactly at j+v+1. Its one-gap is therefore v+1. Requiring that gap to be at least g is equivalent to 2^g dividing 3*n_j+1, hence n_j=-1/3 modulo 2^g. A positive integer orbit cannot have an all-zero parity tail: that would make its integer at the start of the tail divisible by every power of 2.

**Fractional carrying step.** A one-gap h<g gives a tail starting at its first one at least (1+r^h)/3 >= beta_g. It therefore violates the strict bound u<a for every a<=beta_g. Conversely, gap>=g gives for every tail u_j<=sum_(k>=0)r^(kg)/3=alpha_g, by placing the first one immediately and each later one as early as allowed. A tail with leading zeros only reduces this upper bound. Equality at any tail requires precisely (1 0^(g-1))^infinity starting there. Its real series is alpha_g and its 2-adic series is the same rational, since both geometric series converge. G51 would require the integer at that tail to be -alpha_g, incompatible with a positive ordinary integer. Thus actual positive integer codes obey u_j<alpha_g at every age. This supplies the strict lower endpoint as well as every a>alpha_g.

For g>=3 we have alpha_g<=beta_g<1/2: the first inequality is equivalent to r+r^g<=1, and r+r^3=26/27<1. The reverse construction from a residue-avoiding n uses G50's future sums u_j; their uniform bound below 1/2 makes xi=n+u_0(n) and its forward orbit exactly the required integer/fractional decomposition. The forward direction uses G50 because a<1/2. The zero integer gives the zero code and xi=0, so it cannot supply a positive start below 1. This completes all quantifiers and endpoints of the stated equivalence.

**Scope.** For a>alpha_g the formal fractional code set is the closed shift of finite type with one-gaps at least g. At a=alpha_g its strict version removes the critical periodic tails and is not itself that closed shift; the ordinary-integer criterion still holds because equality is unrealizable. The union of the stated g>=3 classes is the g3 class, rather than every formal strictly admissible code. Mahler nonexistence implies R3, and R3 implies R4 etc.; no converse or coverage of all uniformly confined Z-numbers is proved here. This refines the elementary gap bound already in GC667; no novelty claim.
