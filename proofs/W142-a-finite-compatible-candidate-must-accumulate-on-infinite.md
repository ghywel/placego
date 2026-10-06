# A finite compatible candidate must accumulate on infinite support

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G142. A finite compatible
candidate must accumulate on infinite support (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

If a finite pattern can keep the alternating wall's condition forever, its successive rows must approach an infinite pattern along some subsequence. This is necessary because its outermost black cell moves outward at every step: a compact family made entirely of finite compatible patterns would force a predecessor with a smaller radius than the family's smallest one. So finding an infinite limit does not refute a finite starting pattern. The question of whether any finite starting pattern works is still open.

## The formal statement and proof

**Status and target.** Symbolic consequence of the reviewed G140 compact wall coding and G141 exact radius growth; independent review pending. No experiment or novelty claim about compactness. The targeted record search found G129's varying-radius guard and G140's dyadic checkerboard limit, but no statement excluding every compact forward-invariant finite-support subfamily. Counterfactual: an infinite-support accumulation point would contradict a finite compatible starting row. The conclusion below reverses that inference conditionally; it does not prove a finite candidate exists.

Use G140's compact compatible space S and continuous two-step map F. Its finite-support subset S_fin is forward invariant. Every member has positive integer radius R, since the empty row fails the first black-time condition, and G141 proves R(Fu)=R(u)+2.

**Lemma.** There is no nonempty compact A contained in S_fin with F(A) contained in A.

**Proof.** Suppose such an A exists. The sets F^n(A) are nested, nonempty and compact, so their intersection K is nonempty and compact. Moreover F(K)=K. The forward inclusion follows from nesting. For the reverse inclusion, fix y in K. For each n the set

    C_n = F^n(A) intersect F^(-1)({y})

is nonempty, since y belongs to F^(n+1)(A). These sets are nested and compact. Any x in their intersection lies in K and satisfies F(x)=y.

Every point of K has positive integer radius. Choose y in K with the smallest radius occurring in K; this uses the well-ordering of the integers, not continuity or boundedness of the radius function. Surjectivity on K supplies x in K with F(x)=y. Exact growth gives R(x)=R(y)-2, contradicting minimality. Thus A cannot exist.

**Consequences, conditional on existence.** For any u in S_fin, its forward orbit closure in S is nonempty, compact and forward invariant. The lemma forces that closure to contain a row z of infinite support. Since every orbit point F^n(u) is finite, z is an accumulation point along indices tending to infinity. Therefore every hypothetical finite compatible candidate necessarily has an infinite-support orbit accumulation point, not merely the dyadic candidate of G140. Also S_fin is either empty or not closed in S: if nonempty and closed it would itself be a forbidden compact forward-invariant A. In particular it cannot be assumed compact to manufacture finite ancestors. This sharpens G140's closure qualification without deciding whether S_fin is empty.

**Unexpected compactness check.** Compactness alone does not bound finite radii. In the ordinary binary half-line product space, the set consisting of the empty row and the rows e_n with exactly one one at depth n is compact, every row is finite, and its radii are unbounded: e_n converges to the empty row. This is not a compatible wall family; the empty row is excluded from S. It rejects a false shortcut to the lemma. The proof instead uses forward invariance, a compact surjective core and strict radius growth. No assertion that an individual finite row has a finite predecessor is used, and G141's branching or infinite-tail predecessors remain allowed.

**Remaining prize obligation.** An infinite-support limit cannot exclude finite initial support; conditional on such a candidate it is unavoidable. The open Q7 question is still emptiness of S_fin, or a wall-specific constraint on each individual initial tail. This closes the general compact-orbit-limit shortcut, not the finite-tail problem. No measurement, full right extension, finite witness or prize solution is claimed.
