# Rotation classes sharpen the periodic zero-basin first-hit bound

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G152. Rotation classes sharpen
the periodic zero-basin first-hit bound (2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

A pattern that eventually becomes entirely zero cannot revisit even a rotated version of an earlier pattern. Counting rotation classes with the permitted periods therefore sharpens the first-hit-time bound. Period three permits at most three steps; period six at most twelve, without claiming that every bound is attained. Canonical backward tails inherit a stronger logarithmic period-growth floor. This does not settle the temporal wall or the silver code’s support.

## The formal statement and proof

**Status and target.** Symbolic refinement, independent review pending. No experiment. Uses reviewed G123/G124. Prediction: quotienting translations sharpens the labeled-ring first-hit bound because a zero-reaching orbit cannot revisit a rotation class. Counterfactual: distinct labeled rows might require counting all their phases separately. An absorbing quotient argument removes those phases. Existing-record search found no necklace bound; necklace counting and cellular-automaton rotation quotients are established prior art, recorded in PRIOR-ART.md. No novelty claim for the method.

Let x be a nonconstant spatially periodic Rule30 row of least period p that first reaches zero at physical time T. By G124, p=3*2^a for some a>=0. Define L(q) to be the number of binary rotation classes of least period q. Then

    T+1 <= C_a := 2 + sum_(b=0)^a L(3*2^b),
    L(3)=2,
    L(q)=(2^q - 2^(q/2) - 2^(q/3) + 2^(q/6))/q  for q=3*2^b, b>=1.

In particular p=3 forces T<=3; p=6 forces T<=12. These are upper bounds, not assertions that each is attained.

**No repeated rotation class.** Write x_i=F^i(x), 0<=i<=T. Suppose x_j is a spatial translate of x_i for i<j<=T. On the p-cell ring the update commutes with rotations, so it induces a deterministic map on rotation classes. The class of x_i then lies on a cycle of length dividing j-i. It cannot subsequently enter the distinct absorbing class of zero. If the class already is zero, the first-hit property instead gives i>=T, impossible. Thus all T+1 classes are distinct. This uses no assumption that the cellular automaton is injective.

Every intermediate row reaches zero and has spatial period dividing p. G124 therefore permits only least period one or 3*2^b, 0<=b<=a. Period one contributes precisely the constant zero and constant one classes. Counting all binary classes of the remaining permitted periods gives C_a; some counted classes may lie outside the zero basin, so the inequality can be strict. A primitive word of length q has q distinct rotations even when repeated on a larger p-cell ring. There is no additional factor p/q in the class count.

**Counting derivation.** If A(q) counts labeled binary words of least period q, then 2^q=sum_(d|q) A(d). Divisor inversion gives A(q)=sum_(d|q) mu(d)*2^(q/d), where mu is the ordinary Moebius function. Dividing by q gives L(q). For q=3 the only squarefree divisors are 1,3. For q=3*2^b, b>=1, they are 1,2,3,6; their signs give the displayed formula. This is the standard primitive-necklace formula, not a new counting identity.

**Asymptotic consequence.** Along p=3*2^a tending to infinity, C_a=(1+o(1))*2^p/p. The largest term L(p) has that asymptotic by its explicit formula; all smaller terms together are at most a*2^(p/2), whose ratio to 2^p/p tends to zero. Hence along zero-reaching rows with T tending to infinity,

    p >= log2(T+1) + log2(log2(T+1)) - o(1).

Indeed log2(T+1)<=p-log2(p)+o(1), while the original labeled-ring count gives p>=log2(T+1); substituting that lower bound inside log2(p) yields the claim. G123's canonical ancestor tail C_n first reaches zero at time n, so the same bound applies to its p_n. This improves a generic counting floor; it gives no upper bound on doubling gaps or a temporal-wall exclusion.

**Independent arithmetic control and unexpected guard, by hand.** The two primitive period-three classes are represented by 001 and 011. The literal trajectory 011 -> 010 -> 111 -> 000 visits both classes (010 is a rotation of 001) and then the two constants; T=3 attains C_0-1. At period six the four-term formula gives (64-8-4+2)/6=9, so C_1=2+2+9=13. Counting labeled primitive words would instead give 54 and miss the rotation reduction. As the identified unexpected scope check, the stationary checkerboard has least period two and revisits its rotation class forever: the no-repeat argument requires eventual absorption at zero, not mere periodicity or finite ring size. None of these controls is a numerical run.

**Scope.** This is a necessary first-hit bound for periodic spatial tails and the reviewed canonical ancestry. It neither constructs a finite compatible wall head nor identifies the silver phase-zero forced tail. The all-depth wall-tail obligation remains open.
