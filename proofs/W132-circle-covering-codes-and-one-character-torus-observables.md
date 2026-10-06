# Circle-covering codes and one-character torus observables are excluded

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G132. Circle-covering codes and
one-character torus observables are excluded (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

A higher-dimensional rotation can still expose only one circle coordinate.

**What it says.** The earlier exclusion applies to torus observables that factor through an integer circle projection and an allowed arc code. Rational projected angles give periodic codes; irrational ones inherit the Sturmian obstruction. Endpoint conventions do not change the conclusion.

**Why it matters.** This covers some partitions with several original endpoint orbits, such as a circle covering. It leaves genuinely multidimensional partitions and general unrelated endpoints open.

**An everyday picture.** Several rotating coordinates can be read through one dial. The exclusion concerns what that dial displays, not how many hidden coordinates are moving.

## The formal statement and proof

**Status and target.** Corollary of G131 and G27.2; independent review pending, including its G131 dependency. No experiment or novelty claim for integer characters. Target: clarify which multi-orbit and torus codes the finite-block argument already excludes. Counterfactual: a circle covering or additional unobserved torus coordinates automatically evade the Sturmian obstruction. A genuine two-coordinate box below is the unexpected scope check.

**Statement.** Let the torus orbit be x_s=theta+s*omega modulo one in each of d coordinates. Fix an integer vector v and the circle projection

    h_v(x)=sum_j v_j*x_j modulo one,
    beta=h_v(omega).

Observe c_s=psi(h_v(x_s)). If beta is rational, every such deterministic observable psi gives a periodic c and is excluded beside the alternating Rule 30 wall with finite initial left support. If beta is irrational, the same exclusion holds whenever psi is a binary finite-union-of-arcs code whose jump endpoints lie on one beta-rotation orbit. Arbitrary fixed choices at the endpoints are allowed. In both cases no assumption is made about periodicity of the actual right-neighbor trace at its hidden phases.

**Proof.** Integer coefficients make h_v well-defined on the torus. Direct addition gives

    h_v(x_s)=h_v(theta)+s*beta modulo one.

For rational beta with denominator q these projected points repeat every q samples, hence c is periodic. The corresponding nearest-left trace is periodic: at even physical times it is 1-c_s, and at odd times it is one. G27.2 excludes this pair for finite initial left support, independently of the right half.

For irrational beta, the projected observable is exactly a circle rotation code of the class in G131, so its finite-block exclusion applies for every starting phase. If endpoint values differ from the half-open convention used there, each endpoint is visited at most once: two visits would make a nonzero multiple of beta integral. There are finitely many endpoints, so the code eventually agrees with the half-open code. G131's eventual-factor clause therefore preserves the exclusion. This also explains why endpoint exceptions do not create a new companion class.

**Circle coverings give a concrete multi-orbit case.** In dimension one take v=2, irrational alpha as omega, and beta=2*alpha modulo one. Let psi be the standard Sturmian interval [1-beta,1). Then f(x)=psi(2*x modulo one) is a two-arc observable for the original alpha rotation. Its endpoint set is

    {0, 1/2, -alpha, 1/2-alpha} modulo one.

The two original alpha-orbit classes represented by 0 and 1/2 are distinct: an equality 1/2=k*alpha modulo one would make alpha rational for nonzero integer k. Thus f does not have all endpoints on one original orbit, yet its sampled code is Sturmian for the projected angle beta and is excluded. More generally any integer circle covering can be used. This narrows part of the unrelated-endpoint lead; it does not exclude arbitrary unrelated endpoints without such a quotient structure.

**Unexpected genuinely multidimensional guard.** On the two-torus, let f(x,y)=1 when both x and y lie in [0,1/2), zero otherwise. This observable cannot be a function of any single integer character h_(a,b). A function of that character would be invariant under every translation (b*t,-a*t), since the character changes by zero. If b is nonzero, choose x just below 1/2 and y=1/4; a sufficiently small such translation crosses the x boundary while keeping y interior, so f changes. If b=0 and a is nonzero, a vertical translation changes f while leaving the character fixed. The zero character would require f constant. All cases contradict factorization. Therefore this corollary makes no claim about genuinely two-coordinate box codes, nor about the general torus lead. This is a geometric scope check, not a Rule 30 counterexample or a claim that a box code supplies a finite witness.

**Resulting boundary.** The class exclusion includes finite recodings after a one-circle projection, even when the original partition has multiple orbit classes or the underlying motion has several torus coordinates. General partitions using independent coordinates, arbitrary unrelated circle endpoints and kicked observables remain open. No uniform finite-left exclusion or prize solution follows.
