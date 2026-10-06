# At a fixed irrational angle, finite-tail phases are empty or countable and dense

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G147. At a fixed irrational
angle, finite-tail phases are empty or countable and dense (2026-10-07)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

At any fixed irrational angle, only countably many starting phases could produce a finite initial left tail, so almost every phase has an infinite tail. But if even one finite phase exists, time evolution gives a dense orbit of finite phases with growing radii. Each fixed radius allows only finitely many phases. This is why an almost-every-phase result cannot settle the particular boundary-phase code we are investigating. No finite phase has been constructed.

## The formal statement and proof

**Status and target.** Symbolic Q7 corollary, independent review pending. No experiment or general symbolic-dynamics novelty claim. Uses the verified wall coding G140, radius clock G141/G142 and fixed-radius count G129. G145 is independently verified by Local L101. Prediction: varying the phase can give an almost-every-phase exclusion without deciding one exceptional phase. Counterfactual: density of the phase orbit would promote a finite-tail realization to an interval of finite-tail phases. The countability argument refutes that promotion. The phase-dependent repeat record is G143-G146; no external theorem beyond the elementary density of an irrational rotation is imported.

Fix any irrational beta in (0,1). For phases rho modulo2 let c^(rho)_s=floor(s*beta+rho) modulo2, and let

    E_beta = {rho : Phi(c^(rho)) has finite support}.

Then E_beta is countable and forward invariant under rho -> rho+beta modulo2. It is either empty or dense. In particular almost every phase has an infinite forced initial left tail, at every fixed irrational angle, including the exceptional phase-zero angles of G144. This statement does not exclude any specified phase in E_beta, or establish that E_beta is nonempty.

**Proof.** Distinct phases modulo2 give distinct visible words. Indeed the two shifted half-circle partitions disagree on a nonempty open interval of the length-two circle whenever their shifts differ modulo2. The forward orbit s*beta modulo2 is dense and enters that interval, giving a differing symbol. The uniqueness of Phi therefore makes the phase-to-initial-row map injective.

There are only countably many finite binary initial rows: at radius at most L there are at most 2^L. Injectivity gives at most 2^L phases in E_beta with radius at most L. Taking the union over positive integer L makes E_beta countable, hence of Lebesgue measure zero. The empty row is not compatible with the clock, as in G141.

The conjugacy gives F(Phi(c^(rho)))=Phi(c^(rho+beta modulo2)). Forward evolution preserves finite support, so E_beta is forward invariant. If it contains rho, it contains its whole dense irrational forward orbit. Its radii on that orbit are exactly R(rho)+2t by the radius clock. This proves the empty-or-dense dichotomy, and explains why countability and density do not conflict.

**Uniform-radius qualification.** Every fixed-radius phase set is finite. Consequently, along any convergent sequence of pairwise distinct phases in E_beta, the radii tend to infinity: a bounded-radius subsequence would lie in a finite set, contradicting distinctness. An interval of finite-tail phases is impossible, but a dense exceptional set of finite tails is allowed. No uniform-radius conclusion follows from density of one orbit.

**Unexpected check and remaining obligation.** The same countability argument applies at the silver angle even though G143 passes every repeat test and G145 fails every allowance at another phase. Conversely, assuming just one finite phase would supply a dense countable orbit with steadily growing radii, fully consistent with the infinite-support limits in G142/G146. Thus an almost-every-phase theorem, residual-set argument or dense collection of infinite tails cannot settle the individual boundary-phase candidate. E_beta has not been shown nonempty, and its countability is not a prize solution or an all-phase exclusion. The next obligation remains a spatial constraint on Phi(c^(0)), rather than another phase-counting estimate.
