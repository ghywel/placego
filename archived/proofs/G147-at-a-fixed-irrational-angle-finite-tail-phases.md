# at a fixed irrational angle, finite-tail phases are empty or countable and dense

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT147. at a fixed irrational angle,
finite-tail phases are empty or countable and dense (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

At any one irrational angle, at most countably many starting points could come from a finite seed.

**What it says.** So almost every starting point is ruled out. But if even one works, time evolution produces a
dense crowd of them with growing seeds, and each seed size allows only finitely many.

**Why it matters.** This is why an "almost every starting point" result cannot settle the particular code under
study.

**An everyday picture.** A rule that holds for almost every dart thrown says nothing about the one dart you care
about.

## The formal statement and proof

### G147. At a fixed irrational angle, finite-tail phases are empty or countable and dense (2026-10-07)

**Status and target.** Symbolic Q7 corollary, independent review pending. No experiment or general symbolic-dynamics novelty claim. Uses the verified wall coding G140, radius clock G141/G142 and fixed-radius count G129. G145 is independently verified by Local L101. Prediction: varying the phase can give an almost-every-phase exclusion without deciding one exceptional phase. Counterfactual: density of the phase orbit would promote a finite-tail realization to an interval of finite-tail phases. The countability argument refutes that promotion. The phase-dependent repeat record is G143-G146; no external theorem beyond the elementary density of an irrational rotation is imported.

Fix any irrational beta in (0,1). For phases rho modulo2 let c^(rho)_s=floor(s*beta+rho) modulo2, and let

    E_beta = {rho : Phi(c^(rho)) has finite support}.

Then E_beta is countable and forward invariant under rho -> rho+beta modulo2. It is either empty or dense. In particular almost every phase has an infinite forced initial left tail, at every fixed irrational angle, including the exceptional phase-zero angles of G144. This statement does not exclude any specified phase in E_beta, or establish that E_beta is nonempty.

**Proof.** Distinct phases modulo2 give distinct visible words. Indeed the two shifted half-circle partitions disagree on a nonempty open interval of the length-two circle whenever their shifts differ modulo2. The forward orbit s*beta modulo2 is dense and enters that interval, giving a differing symbol. The uniqueness of Phi therefore makes the phase-to-initial-row map injective.

There are only countably many finite binary initial rows: at radius at most L there are at most 2^L. Injectivity gives at most 2^L phases in E_beta with radius at most L. Taking the union over positive integer L makes E_beta countable, hence of Lebesgue measure zero. The empty row is not compatible with the clock, as in G141.

The conjugacy gives F(Phi(c^(rho)))=Phi(c^(rho+beta modulo2)). Forward evolution preserves finite support, so E_beta is forward invariant. If it contains rho, it contains its whole dense irrational forward orbit. Its radii on that orbit are exactly R(rho)+2t by the radius clock. This proves the empty-or-dense dichotomy, and explains why countability and density do not conflict.

**Uniform-radius qualification.** Every fixed-radius phase set is finite. Consequently, along any convergent sequence of pairwise distinct phases in E_beta, the radii tend to infinity: a bounded-radius subsequence would lie in a finite set, contradicting distinctness. An interval of finite-tail phases is impossible, but a dense exceptional set of finite tails is allowed. No uniform-radius conclusion follows from density of one orbit.

**Unexpected check and remaining obligation.** The same countability argument applies at the silver angle even though G143 passes every repeat test and G145 fails every allowance at another phase. Conversely, assuming just one finite phase would supply a dense countable orbit with steadily growing radii, fully consistent with the infinite-support limits in G142/G146. Thus an almost-every-phase theorem, residual-set argument or dense collection of infinite tails cannot settle the individual boundary-phase candidate. E_beta has not been shown nonempty, and its countability is not a prize solution or an all-phase exclusion. The next obligation remains a spatial constraint on Phi(c^(0)), rather than another phase-counting estimate.

*Second reader's note on G147 (Local, 2026-10-07; chat L103).* Correct, checked by hand with G146 as asked; no run was
needed. Two phases that differ modulo 2 code by two half-circles of the length-2 circle whose symmetric difference is a
nonempty open set (the whole circle when the phases differ by 1, giving the complement), and the dense forward orbit
enters it, so phase to word is injective, and $\Phi$ makes phase to row injective. Countability follows from the
countable finite rows. $\sigma c^{(\rho)} = c^{(\rho + \beta)}$ with $F \Phi = \Phi \sigma$ gives forward invariance,
the dense forward orbit gives the dichotomy, and the radius clock gives $R(\rho) + 2t$ along it. One sharpening from
GC156: by the free odd depths, at most $2^{\lceil L/2 \rceil}$ phases in $E_\beta$ have radius at most $L$, not $2^L$.
The record certificate behind G129 also makes every member of $E_\beta$, at every angle, have radius above about 84.
This bounds nothing uniformly, as the block's divergence statement already says. GC164's warning is well placed: a
measure or census statement would be overwhelmingly negative and still blind to the countable set a candidate must lie
in.
