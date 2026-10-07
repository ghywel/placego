# rotation classes sharpen the periodic zero-basin first-hit bound

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT152. rotation classes
sharpen the periodic zero-basin first-hit bound (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A pattern on its way to dying out never returns even to a shifted copy of itself, which limits how long the dying
takes.

**What it says.** Counting repeating rows up to rotation, with the periods G124 allows, gives a sharper limit on how
long a row takes to reach all white: at most 3 steps for period three and at most 12 for period six.

**Why it matters.** It sharpens the picture of the dying patterns and gives backward tails a faster growth floor
(G123). It does not settle the blinking wall.

**An everyday picture.** A walker who may never revisit any spot on a round track, even one shifted along, cannot
walk for long.

## The formal statement and proof

### G152. Rotation classes sharpen the periodic zero-basin first-hit bound (2026-10-07)

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

*Second reader's note on G152 (Local, 2026-10-07; chat L109).* Correct. The rotation quotient is deterministic because
the update commutes with rotations; a revisited class would lie on a cycle of the quotient, and the zero class is a
fixed absorbing class, so a revisit forces the class to be zero before the first hit. Every row on the trajectory
reaches zero and has period dividing $p$, so G124 leaves only the constants and the primitive periods $3 \cdot 2^b$,
$b \le a$. The Moebius count is the standard primitive-necklace formula, with $L(3) = 2$, $L(6) = 9$ and $L(12) = 335$.
The asymptotic substitution is right: the smaller terms total at most $a \, 2^{p/2}$, which is negligible against
$2^p/p$, and $\log_2 p \ge \log_2 \log_2 (T+1)$ follows from the labeled count. Checked (`rule30_audit_g99_g100.py`,
S47): the three necklace counts by brute force; on rings of size 3, 6, 12 and 24 every zero-reaching row's trajectory
visits distinct rotation classes, all of allowed periods, with $T + 1 \le C_a$; and the period-three trajectory
attaining $C_0 - 1 = 3$. The largest first-hit times are 3, 10, 17 and 147, far inside the bounds 4, 13, 348 and
699,218. Writing S47 exposed a fault in my S44 and S46 ring censuses, which stopped each row after $3n + 3$ steps; all
three checks now use the exact basin from a backward search (corrections in the G149 and G151 notes).
