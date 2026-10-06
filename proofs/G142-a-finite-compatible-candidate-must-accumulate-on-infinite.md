# a finite compatible candidate must accumulate on infinite support

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT142. a finite compatible
candidate must accumulate on infinite support (second-read by Local, 2026-10-06)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A finite seed that kept the middle blinking would still have rows approaching an infinite pattern.

**What it says.** Its edge moves outward every tick, so its rows cannot stay inside any bounded family, and some
sequence of them must approach an infinite pattern.

**Why it matters.** Finding an infinite limit therefore does not refute a finite seed, a mistake the record now
guards against.

**An everyday picture.** Growing ripples can look more and more like one endless straight wave, though each ripple
is finite.

## The formal statement and proof

### G142. A finite compatible candidate must accumulate on infinite support (2026-10-06)

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

*Second reader's note on G142 (Local, 2026-10-06; chat L095).* Correct, checked by hand; no run was needed. The
surjective core holds: $F(K) \subseteq K$ by nesting, each $C_n$ is nonempty because $y \in F(F^n(A))$, and it is
compact because $F^{-1}(\{y\})$ is closed, so the nested intersection supplies a preimage inside $K$. The quantifier
is right: the conclusion is about each member of $S_{\mathrm{fin}}$ and is vacuous if that set is empty. The core is
correct but more than the lemma needs. Every point of $F^n(A)$ is $F^n(a)$ with $a$ nonempty, so its radius is
$R(a) + 2n \ge 2n + 1$; the sets $F^n(A)$ are nested, compact and nonempty, so their intersection has a point, and that
point would have radius at least $2n + 1$ for every $n$, which no finite row has. So the lemma is a nested compact
intersection plus the radius clock. The exclusion of the empty row enters only through exact growth, since the empty
row gains radius one, not two, over a white-black pair. The guard is well chosen: the rows $e_n$ show precisely that
compactness without forward invariance bounds nothing. The consequence that $S_{\mathrm{fin}}$ is empty or not
closed generalises G140's dyadic case to every candidate.
