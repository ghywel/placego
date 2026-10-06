# Uniform recoding horizons include rational mechanical bases

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G136. Uniform recoding horizons
include rational mechanical bases (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md
and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Finite recodings retain the uniform spacing bound, with an explicit allowance for their window width.

**What it says.** A code that reads a fixed finite block of a mechanical word cannot evade the repetition obstruction. Rational angles are included by finite-prefix approximation. Resetting the code, phase and angle between pieces still requires corrections no farther apart than a geometric bound, provided the reading widths stay bounded.

**Why it matters.** This reaches recoded and orbit-endpoint reset companions. The window bound is essential: increasingly wide recodings can imitate any selected finite binary prefix. General companions and positive entropy remain open.

**An everyday picture.** Reading several neighboring symbols adds a fixed allowance. Increasing that reading window indefinitely changes the problem.

## The formal statement and proof

**Status and purpose.** Symbolic corollary of G131 and G135; independent review pending. No experiment. Counterfactual: either a finite recoding margin or a rational limiting angle might evade the uniform horizon. The exact margin and a finite-prefix approximation settle both. This advances recoded/reset companions, not the missing entropy theorem. The inherited rotation-partition prior art is recorded in G131; no general novelty claim.

Let g_s be the standard mechanical code of theta+s*alpha modulo one in [1-alpha,1), now allowing every alpha in [0,1]. The endpoint angles give the constant zero and constant one codes. Let F be any binary function of a block of width w+1, w>=0, and put c_s=F(g_s,...,g_(s+w)). Define

    H(C,w)=251*(C+4)+250*w.

**Finite-prefix theorem.** For every integer C>=0, the prefix of c through index M=H(C,w) contains a repetition c_s=c_(s+q) on a<=s<=b with b+q<=M and b>2a+q+C. Neither injectivity nor nonconstancy of F is needed.

First extend G135 to rational and endpoint angles. Every finite prefix g_0,...,g_N of the specified mechanical code is also a prefix of an irrational mechanical code with slightly perturbed angle and phase. To see the boundary issue explicitly, change the angle by epsilon and increase the phase by eta, choosing eta>(N+1)*abs(epsilon), with both arbitrarily small. At a sample exactly on the upper endpoint 0 modulo one, its displacement is eta+s*epsilon>0, giving the correct right-hand value zero for an interior angle. At a sample on the lower endpoint 1-alpha, its displacement relative to that moving endpoint is eta+(s+1)*epsilon>0, giving the correct right-hand value one. All other finitely many samples have a positive margin and keep their value for sufficiently small changes. Choose the perturbed angle irrational. For alpha=0, choose a small positive angle and a phase perturbation larger than the total drift; every sample stays outside its tiny one-interval. For alpha=1, choose an angle just below one and the same dominating positive perturbation; every sample stays inside the one-interval. Thus the finite-prefix contradiction of G135 holds for every mechanical angle.

Now suppose c satisfies the finite repeat bound through M. The underlying mechanical prefix is available through N=M+w=251*(C+w+4). If g repeats on [a,e] with e+q<=N and e>=a+w, then c repeats on [a,e-w], and its compared samples end by N-w=M. Hence e<=2a+q+C+w. If e<a+w, the same inequality is automatic. Every repetition of g through N would therefore satisfy the forbidden bound with constant C+w, contradicting the extended G135 theorem. This proves the claim and explains why the margin is 250*w rather than an unspecified additive loss.

**Matching pieces and corrections.** Beside the alternating Rule 30 wall with initial left-zero radius L>=1, a companion cannot match such a recoded mechanical word on [a,b] unless

    b-a < H(L+2a,w).

For pieces with reset times t_j and widths bounded by one fixed w, the functions, angles and phases may change from piece to piece, but necessarily

    t_(j+1) <= 503*t_j + 251*L + 1004 + 250*w.

For actual disagreement indices against one fixed recoded mechanical base, the bounds are

    k_0 <= 251*(L+4)+250*w,
    k_(j+1) <= 503*k_j + 251*L + 1507 + 250*w.

Finitely many disagreements or a final infinite piece are impossible by the same finite-prefix theorem at a later restart. Consequently super-geometrically spaced resets or corrections are excluded for bounded-width recodings at every mechanical angle. These are necessary bounds, not a construction of a realizable companion.

**Orbit-endpoint interpretation.** G131 constructs a finite block code for any half-open binary arc partition whose actual jump points have the form beta+k_j*alpha. If the integer exponents span D=max(k_j)-min(k_j)>=1, its Laurent polynomial Q(z)=sum(z^k_j) has an even number of jumps and Q=(1+z)P. P has exponent span D-1, so after rephasing its block width parameter is w=D-1. The same construction works for rational angles: distinct actual jump points are listed once, and equality of the jumps leaves only a constant difference, absorbed in F. Constant partitions use w=0. Thus pieces whose endpoint representations have uniformly bounded exponent span inherit the reset bound, even if their angles and partitions vary. The controlling parameter here is exponent span, not merely the number of endpoints. No arbitrary unrelated-endpoint partition is claimed to have this representation.

**Unexpected width guard, proved without a run.** An unrestricted finite block code can fit any prescribed finite binary prefix. Fix an irrational Sturmian g and finitely many starting indices 0,...,m. Their infinite future tails are pairwise distinct: equality of two would give an eventually periodic mechanical code, impossible because its symbol frequency is irrational. For each pair there is a finite first differing coordinate; take w at least the largest such coordinate. All the blocks g_s,...,g_(s+w) at these indices are distinct. Define F on them to output the desired prefix, and define it arbitrarily elsewhere. This does not give an infinite prescribed word, a uniform w or a finite-left Rule 30 realization. In particular the record's overlap-free Thue-Morse prefixes can pass the repeat inequality for arbitrary finite horizons while being fitted by increasingly wide recodings. A horizon independent of all recoding widths is therefore false. This is the identified independent scope check. At w=0 the theorem recovers G135 and its rational extension; constant F also retains the immediate period-one obstruction. Geometric correction schedules still pass the displayed necessary bounds, and no positive density, entropy or prize solution follows.
