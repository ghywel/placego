# bounded-type rotation codes need geometrically spaced corrections

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT134. bounded-type rotation
codes need geometrically spaced corrections (second-read by Local, 2026-10-06)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The same holds for every rotation angle whose continued-fraction digits (the whole numbers you get by repeatedly
taking off a number's whole part and turning what is left upside down) stay bounded.

**What it says.** G133's spacing limit extends from the golden ratio to every irrational angle of "bounded type",
whose continued-fraction digits never grow large.

**Why it matters.** A larger family of kicked patterns is excluded.

**An everyday picture.** The same rule for every top that wobbles at a steadily irrational rate.

## The formal statement and proof

### G134. Bounded-type rotation codes require geometrically spaced corrections (2026-10-06)

**Status and target.** Symbolic extension of G133, independent review pending. No experiment or new numerical prediction. Theorem E and G2.2 supply the continued-fraction facts; G133 supplies the finite comparison deadlines. Target: remove the golden-angle restriction from the sparse-kick exclusion. Counterfactual: bounded partial quotients might still allow corrections with unbounded successive spacing ratios beside a finite left seed. The proof below excludes that possibility. This is a consequence of the existing repetition obstruction, with no general novelty claim.

Let alpha in (0,1) be irrational with every partial quotient a_j<=A, where A>=1 is an integer. For any phase theta let g be its standard half-open Sturmian code. Define

    K_A=8*(A+1)^4+3.

**Finite-prefix theorem.** For every integer C>=0, the prefix of g through index N=K_A*(C+4) cannot satisfy b<=2a+q+C for every repetition g_s=g_(s+q) on a<=s<=b with b+q<=N.

Use Theorem E's convergents q_n, errors delta_n, mismatch arcs K_n and first visit h(n). G133's finite comparison argument, valid for every irrational angle once these mismatch arcs have the stated form, gives

    q_(j+1)-q_j-C-4 <= h(j) <= q_j+C+2

whenever N>=4q_j+3C+8. Choose n minimally with q_(n-1)>T=2C+8. The initial denominator q_0=1 is below T. Minimality and q_j=a_j*q_(j-1)+q_(j-2) give q_(n-1)<=(A+1)*T. Thus

    q_(n+2) <= (A+1)^3*q_(n-1) <= (A+1)^4*T,
    4q_(n+2)+3C+8 <= K_A*(C+4).

The visit bounds therefore hold at all three indices n,n+1,n+2. If any of a_(n+1),a_(n+2),a_(n+3) is at least two, the corresponding visit bounds imply q_(j-1)<=2C+6, impossible. All three coefficients must consequently be one.

**Quantitative separation, including the finite-offset check.** Put D=2C+6. At j=n and j=n+1, the opposite mismatch arcs are disjoint, their combined length is |delta_(j-1)|, and the visit bounds place

    m=h(j)-h(j+1) in [-q_j-D,D].

Also m is nonzero and ||m*alpha||<|delta_(j-1)|. Best approximation forces |m|>=q_j. Since D<q_(j-1)<=q_j, this means m=-q_j-r with 0<=r<=D. If r>0, then r<q_(j-1), so the preceding best-approximation bound and the error recurrence give

    ||r*alpha|| >= |delta_(j-2)|
                 = a_j*|delta_(j-1)|+|delta_j|
                 >= |delta_(j-1)|+|delta_j|.

The triangle inequality on the circle now gives ||(q_j+r)*alpha||>=|delta_(j-1)|, a contradiction. Hence r=0 exactly, and

    h(n+1)=h(n)+q_n,
    h(n+2)=h(n+1)+q_(n+1).

This finite-offset argument uses no unspecified sufficiently-large threshold or phase-dependent distance. It also supplies the explicit justification for G133's quantitative use of Theorem E Step 4. At the selected indices the standard mismatch description applies: n>=2; if n=2 then q_1>T forces alpha<1/8, and later convergent errors are smaller than both coding-interval lengths. The same assertion at n>=3 follows from the first convergent errors and their monotone decrease.

Finally the lower visit bound at n is h(n)>=q_(n-1)-C-4. The second identity and upper bound at n+2 give h(n+1)<=q_n+C+2. Substituting the first identity forces q_(n-1)<=2C+6, again a contradiction. This proves the finite-prefix theorem.

**Finite-left companion consequence.** Let the Rule 30 wall be 0101... and its initial left row be zero beyond radius L>=1. Theorem E Step 0 permits repeat constant C=L. Restarting at physical time 2a enlarges the left-zero radius to at most L+2a. Any matching stretch with this fixed-angle Sturmian code, rephased as necessary, obeys

    b-a < K_A*(L+2a+4).

For the actual disagreement indices k_0<k_1<... against a fixed base code, G131 already excludes finitely many disagreements. The finite-prefix theorem and the intervals between disagreements give

    k_0 <= K_A*(L+4),
    k_(j+1) <= (2K_A+1)*k_j + K_A*L + 6K_A + 1.

Thus unbounded ratios k_(j+1)/k_j are impossible for every bounded-type irrational angle, every phase and every finite left radius. In particular super-geometric flip schedules are excluded throughout this class. The sharper golden constant in G133 remains useful; this uniform class constant is deliberately conservative.

**Independent and unexpected scope checks.** The finite-offset check above is independent of G2.2's asymptotic eta argument and is the identified unexpected check. At A=1 this theorem gives K_A=131 rather than G133's 84, a consistency check without an optimality claim. The schedule k_j=2^j still satisfies the resulting necessary bounds for L>=1, so this argument establishes neither positive kick density nor positive entropy nor realizability. For unbounded partial quotients, the controlled denominator growth used to choose a linear horizon fails; this proof supplies no uniform linear bound there. Arbitrary phase-reset kicks, the measured rational wheel and genuinely multidimensional observables remain outside the claim.
