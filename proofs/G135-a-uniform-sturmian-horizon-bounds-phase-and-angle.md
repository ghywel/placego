# a uniform Sturmian horizon bounds phase and angle resets

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT135. a uniform Sturmian
horizon bounds phase and angle resets (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The correction-spacing limit holds for every irrational Sturmian angle, even when resets change the angle.

**What it says.** The repetition obstruction itself controls the growth of the scales used in the proof. This gives one uniform bound on an uninterrupted Sturmian-coded stretch, without assuming bounded partial quotients. Phase and angle can both change between pieces, but reset times cannot spread faster than geometrically.

**Why it matters.** This removes the angle restriction from the sparse-correction exclusion and reaches phase-reset codes. Geometric resets, general arc observables and a positive entropy theorem remain open.

**An everyday picture.** Changing the dial at each reset cannot make the next uninterrupted stretch arbitrarily long relative to the current time.

## The formal statement and proof

### G135. A uniform Sturmian horizon also bounds phase and angle resets (2026-10-06)

**Status and target.** Symbolic proof, independent review pending; no experiment. G133 is independently verified by Local L087; G134 is awaiting review. This strengthens their angle scope rather than optimizing the golden constant. Counterfactual: a huge continued-fraction coefficient could postpone the next usable scale beyond every horizon proportional to the left radius. The finite repetition bound itself prevents that escape. All inputs are the existing Theorem E continued-fraction facts and the explicit G134 finite-offset argument; no general novelty claim.

**Uniform finite-prefix theorem.** For every irrational alpha in (0,1), every phase theta and every integer C>=0, its standard half-open Sturmian prefix through

    N=251*(C+4)

contains a repetition g_s=g_(s+q) on a<=s<=b with b+q<=N and b>2a+q+C. There is no bound on partial quotients in this statement.

Suppose otherwise. Put T=2C+8. Choose n minimally with q_(n-1)>T and put r=n-2. Then q_r<=T. At every usable scale j the finite comparison deadlines of G133 give

    q_(j+1)-q_j-C-4 <= h(j) <= q_j+C+2,
    q_(j+1) <= 2q_j+2C+6 < 2q_j+T,

provided N>=4q_j+3C+8. The second line is the crucial replacement for an externally assumed bound on partial quotients.

The starting scale r is usable, including its small-index cases. If r=0, q_1>T implies alpha<1/8; delta_0=alpha and the two mismatch arcs for period q_0=1 are disjoint, so Theorem E's break description and return gap at least q_1 hold. If r>=1, |delta_r| is at most min(alpha,1-alpha), making the same break description valid. Indeed, when a_1=1, |delta_1|=1-alpha; when a_1>=2, the recurrence alpha=a_2*|delta_1|+|delta_2| gives |delta_1|<alpha. Later errors decrease. Equality of an error with the shorter interval length merely makes the mismatch arcs touch at a half-open endpoint; it does not create an overlap.

Starting with q_r<=T, apply the growth inequality successively at r,r+1,r+2,r+3. Every application is justified within the fixed horizon, because the resulting bounds are

    q_(n-1) < 3T,
    q_n < 7T,
    q_(n+1) < 15T,
    q_(n+2) < 31T,

and

    4*(31T)+3C+8 = 251C+1000 < 251*(C+4).

Thus the visit bounds hold at n,n+1,n+2 as well. This is an induction on already bounded denominators, not a circular assumption that the later scales fit.

At those three scales, any coefficient a_(j+1)>=2 would give q_(j-1)<=2C+6, contradicting q_(n-1)>T. Hence a_(n+1),a_(n+2),a_(n+3) must all be one. The explicit separation in G134 applies at n and n+1: for m=h(j)-h(j+1), best approximation gives m=-q_j-u with 0<=u<=2C+6; a positive u<q_(j-1) would give

    ||(q_j+u)*alpha|| >= |delta_(j-2)|-|delta_j|
                         >= |delta_(j-1)|,

contrary to the distance across the opposite mismatch arcs. Therefore

    h(n+1)=h(n)+q_n,
    h(n+2)=h(n+1)+q_(n+1).

Combining the lower visit bound at n with the upper bound at n+2 yields q_(n-1)<=2C+6, the final contradiction. The uniform finite-prefix theorem follows.

**Companion and reset consequences.** Beside a Rule 30 wall 0101... with initial left-zero radius L>=1, any interval [a,b] matching a standard irrational Sturmian code obeys

    b-a < 251*(L+2a+4).

The phase and angle may be chosen separately for each interval: restart at physical time 2a, use the light-cone radius L+2a and apply the uniform theorem with repeat constant C=L+2a. No relation between the different intervals' angles is required.

Consequently, if a companion is made of consecutive Sturmian-coded pieces with reset times 0=t_0<t_1<..., even allowing both phase and angle to change at each reset, it necessarily satisfies

    t_(j+1) <= 503*t_j + 251*L + 1004.

A final infinite piece is impossible. Super-geometrically separated resets cannot support a finite left seed. For actual disagreements k_j against one fixed irrational Sturmian base, the corresponding statement is

    k_0 <= 251*(L+4),
    k_(j+1) <= 503*k_j + 251*L + 1507.

This excludes super-geometric flips for every irrational base angle, including unbounded-type angles. The improved golden constant of G133 is still stronger within its narrower class.

**Unexpected independent checks and limits.** A tiny alpha whose first denominator is enormous is the identified unexpected check: the initial q_0=1 scale already forces q_1<=2C+8, so the proof never waits for that enormous denominator. The complementary near-one case uses q_1=1 and its short error, rather than incorrectly using the long q_0 mismatch arc. These endpoint-angle controls justify the uniform claim. Dyadic times still pass the necessary bounds, so no positive density, positive entropy or realizability conclusion follows. The pieces must use the standard Sturmian interval (or its complement, which has identical repetitions); arbitrary arc observables and the measured rational wheel are not asserted to have this form. This is a class exclusion for companions, not a prize solution.

*Second reader's note on G134 and G135 (Local, 2026-10-06; chat L088).* Both correct. G134: minimality gives
$q_{n-1} \le (A+1)T$ and $q_{n+2} \le (A+1)^4 T$, hence $K_A = 8(A+1)^4 + 3$ (131 at $A = 1$); the finite-offset step
is sound, since $0 < r \le D < q_{j-1}$ would give $\|r\alpha\| \ge |\delta_{j-2}| \ge |\delta_{j-1}| + |\delta_j|$
and so $\|(q_j + r)\alpha\| \ge |\delta_{j-1}|$, and that step also supplies the explicit form of Theorem E Step 4
that G133 used. G135: the visit bounds themselves give $q_{j+1} \le 2q_j + 2C + 6$, and starting from $q_r \le T$
each step uses a horizon already justified ($3T, 7T, 15T, 31T$), so $4 \cdot 31T + 3C + 8 = 251C + 1000$ fits inside
$251(C + 4)$ with no bound on partial quotients; the tiny-angle and near-one starts are handled correctly. Checked
(`rule30_audit_g99_g100.py`, S32): for the golden angle, $\sqrt 2 - 1$, $e - 2$, $\pi - 3$, a tiny angle
$1/(50 + \varphi)$ and one minus it, at 10 random phases each and $C = 0, 2$, every prefix of length $251(C + 4)$
contains a violating repetition; the latest first violation over all of them came at prefix length 45, so the
uniform constant is very conservative.
