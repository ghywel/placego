# golden-angle codes cannot be rescued by super-geometric kicks

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT133. golden-angle codes
cannot be rescued by super-geometric kicks (second-read by Local, 2026-10-06)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A golden-angle code needs kicks often enough to interrupt long unbroken stretches.

**What it says.** The earlier repetition proof gives a uniform linear bound on how long a visible companion can agree with a golden-angle Sturmian word beside a finite left seed. Consecutive disagreement times therefore obey a geometric upper bound; super-geometrically separated flips cannot rescue the code.

**Why it matters.** This reaches a class of kicked, aperiodic companions rather than only exact rotation codes. It gives no positive entropy or kick-density bound, and does not exclude every sparse schedule or the measured rational wheel.

**An everyday picture.** A correction cannot postpone the next correction arbitrarily far when the underlying repeated stretches grow at a controlled rate.

## The formal statement and proof

### G133. Golden-angle codes cannot be rescued by super-geometrically separated kicks (2026-10-06)

**Status and target.** Quantitative extraction from Theorem E's existing continued-fraction proof; independent review pending. No experiment. G131/G132 are verified by Local L085/L086. Target: advance the kicked-code part of PERIOD-TWO question 7 with an aperiodic base, rather than another exact-code reformulation. Counterfactual: zero kick density alone permits arbitrarily long unbroken Sturmian stretches beside a finite left seed. The conservative constants below are not optimized. The dyadic-kick guard prevents an entropy or all-kicks exclusion claim.

Let alpha=(sqrt(5)-1)/2 and g_s=1 when theta+s*alpha modulo one belongs to [1-alpha,1), with any theta. Assume the Rule 30 wall is 0101... from time zero and the initial left row is zero beyond radius L.

**Finite repetition lemma.** For every integer C>=0, a golden-angle Sturmian prefix through index

    N=84*(C+4)

cannot obey the finite repeat bound b<=2a+q+C for every repetition g_s=g_(s+q) on a<=s<=b with b+q<=N. In particular a visible companion cannot agree with such a Sturmian word through index 84*(L+4). The L=0 left seed already fails the first black-time equation; for L>=1 Theorem E Step 0 supplies a repeat constant no larger than L.

**Finite-horizon proof.** Use section 8.57's convergent notation q_n, delta_n, K_n and the first two visit times h,h' to K_n. For a fixed q=q_n, if N>=4q+3C+8, the finite repeat bound alone forces

    h <= q+C+2,
    h' <= 2h+q+C+4.

Indeed, if h>q+C+2, the repetition from 0 through q+C+1 violates the bound; all compared samples lie within N. After the first visit, if h'>2h+q+C+4, the repetition from h+1 through 2h+q+C+3 violates the bound. Its last compared index is at most 4q+3C+7, using the first inequality. These are exactly Theorem E's two visit inequalities, obtained without assuming the second visit was already observed. As in that proof, returns to K_n are at least q_(n+1) apart. Thus

    q_(n+1)-q_n-C-4 <= h(n) <= q_n+C+2.       (visit bounds)

Choose n minimally so q_(n-1)>2C+8. For the golden angle all partial quotients are one. The separation argument of Theorem E Step 4, applied at n and n+1, gives

    h(n+1)=h(n)+q_n,
    h(n+2)=h(n+1)+q_(n+1).

Here its prerequisites are just the visit bounds at n,n+1,n+2 and q_(n-1)>2C+8: the two arcs at successive scales are disjoint and closer than delta_(n-1), and the only possible signed return in the bounded visit-time difference is -q_n. No extra hypothesis about the Rule 30 orbit enters this separation step.

The visit bounds and first identity give h(n)>=q_(n-1)-C-4. The second identity and the upper visit bound at n+2 give h(n+1)<=q_n+C+2. Combining these with the first identity yields q_(n-1)<=2C+6, a contradiction.

All three scales are present in the stated horizon. Minimality and the Fibonacci recurrence imply q_(n-1)<=4C+16 and q_(n+2)<=5q_(n-1)<=20C+80. Therefore

    4q_(n+2)+3C+8 <= 83C+328 < 84*(C+4).

This proves the finite repetition lemma.

**Unbroken stretches at later times.** If the visible companion agrees with a golden-angle Sturmian word from visible index a through b, restart at physical time 2a. The left-zero radius is then at most L+2a by the light cone, and the wall has the same phase. The finite lemma, with this larger radius and arbitrary rephased theta, requires

    b-a < 84*(L+2a+4).

This statement does not require the companion to be periodic or the rest of it to be Sturmian.

**Necessary kick-gap bound.** Suppose c equals a fixed golden-angle Sturmian word except at its actual disagreement indices k_0<k_1<.... Finite support requires infinitely many disagreements, since an eventual exact code is already excluded by G131. Before the first kick, the finite lemma gives k_0<=84*(L+4). Between consecutive kicks use a=k_j+1 and b=k_(j+1)-1. The preceding inequality yields the conservative integer bound

    k_(j+1) <= 169*k_j + 84*L + 505.

Thus schedules with unbounded ratios k_(j+1)/k_j are excluded. In particular, flipping the Sturmian bit at every index 2^(2^j) cannot give a finite-left companion, for any phase and any L. This is an infinite class exclusion from a uniform finite-horizon argument, not evidence extrapolated from measured kicks.

**Unexpected checks and limits.** The Fibonacci sizes 13,21,34,55 at C=0 give a hand check of the three-scale horizon: 4*55+8=228<336. More importantly the zero-density schedule k_j=2^j satisfies the derived kick-gap and first-kick bounds for every L>=1. The theorem therefore does not exclude every sparse schedule or establish positive entropy, positive kick density or realizability of dyadic kicks. It supplies only a necessary upper bound on consecutive disagreement times. The actual measured rational wheel, arbitrary irrational angles, phase-reset kicks and genuinely multidimensional codes are outside this golden-base result. These are the identified independent scope checks.

*Second reader's note on G133 (Local, 2026-10-06; chat L087).* Correct. Both visit inequalities are obtained from
repetitions whose compared samples end by index $4q + 3C + 7$; for the golden angle $q_{n+1} - q_n = q_{n-1}$, and the
two Step 4 identities give $q_{n-1} \le 2C + 6$, against the choice $q_{n-1} > 2C + 8$; $q_{n+2} \le 5 q_{n-1} \le 20C + 80$ puts all three scales inside $84(C + 4)$; restarting at physical time $2a$ gives the kick-gap recursion
$k_{j+1} \le 169 k_j + 84L + 505$. Checked (`rule30_audit_g99_g100.py`, S31): for 30 random phases and $C = 0, 2, 5$
every golden prefix of length $84(C + 4)$ contains a violating repetition; descriptively the latest first violation
over those phases came at prefix lengths 27, 45 and 74, about a tenth of the proved horizons, so the constants could
be tightened; the Fibonacci hand check and the two kick schedules (excluded $2^{2^j}$, admitted $2^j$) check.
