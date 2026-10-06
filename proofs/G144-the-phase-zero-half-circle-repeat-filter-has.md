# the phase-zero half-circle repeat filter has an exact exceptional class

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT144. the phase-zero
half-circle repeat filter has an exact exceptional class (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

For half-dial codes started at the dial's boundary, exactly which angles pass the repeat test is now known.

**What it says.** Such a code passes with a fixed allowance exactly when the angle's continued-fraction digits are
eventually all 2 and a related sequence of numerators is eventually odd. Every other angle fails, with an excess
that grows without bound.

**Why it matters.** It turns a family of open cases into a small, precise exceptional class, which still needs the
wall's own equations.

**An everyday picture.** A lock that opens only for keys whose teeth eventually all have the same height.

## The formal statement and proof

### G144. The phase-zero half-circle repeat filter has an exact exceptional class (2026-10-07)

**Status and target.** Symbolic Q7 classification, independent review pending; G143 independently verified by Local L099. No experiment. Fix the phase zero used in GC159; this is not an all-phase classification. The inputs are G143's signed mismatch intervals and tail-two mesh argument, ordinary continued-fraction best approximation and Legendre's criterion. The Rote critical-exponent literature is recorded in PRIOR-ART.md; its ordinary factor exponent does not include the starting index in our debt and no theorem from it is imported.

Let beta be any irrational in (0,1), let c_s=floor(s*beta) modulo2, and write p_n/q_n for its convergents, a_(n+1) for the next coefficient and delta_n=q_n*beta-p_n. Then the following are equivalent:

1. There is a finite constant C such that every equality interval c_s=c_(s+q), a<=s<=b, a>=0, q>=1, satisfies b<=2a+q+C.
2. Eventually every a_n is 2 and every convergent numerator p_n is odd.

The angles in (2) form a countable quadratic class. G143's beta=2-sqrt(2) belongs to it and even satisfies the strict C=0 bound. Passing this filter is not a finite-left Rule30 realization. Every other phase-zero half-circle code is excluded by the wall's necessary repeat inequality for every finite left radius.

**Obstruction from even numerators.** Suppose p_n is even, with n large enough that |delta_n|<1. The period q_n has signed even-integer error delta_n, so its mismatch interval is the upper or lower arc of length |delta_n| given in G143. Its first positive visit is exactly h=q_(n+1). Indeed best approximation gives distance at least |delta_n| to every integer at every 0<k<q_(n+1); q_n itself has the wrong error sign to enter this arc, and no other such k attains the opposite endpoint. At q_(n+1) the error has opposite sign and smaller magnitude, so the arc is hit.

If delta_n>0, the prefix equality interval is [0,h-1]. If delta_n<0, time zero is a mismatch and the equality interval is [1,h-1]. Their debts b-2a-q_n are respectively

    q_(n+1)-q_n-1,    q_(n+1)-q_n-3.

Both are at least q_(n-1)-3. Infinitely many even p_n therefore produce unbounded debt. Condition (1) forces all sufficiently late p_n to be odd. The numerator recurrence then forces every sufficiently late a_(n+1) to be even.

**Obstruction from large coefficients.** Put d=|delta_n| and a=a_(n+1)>=3. Write |delta_(n-1)|=(a+gamma)*d with 0<gamma<1. For large n, the period 2q_n has signed even-integer error 2delta_n and mismatch arc of length 2d. Its first positive visit is

    h=(a-1)*q_n+q_(n-1).

Here is an explicit first-hit justification. Expand any integer pair (p,k) in the unimodular basis (p_n,q_n),(p_(n-1),q_(n-1)), with coefficients m,l. An error of the sign opposite delta_n and magnitude less than 2d, which is less than |delta_(n-1)|, requires m,l>0: opposite coefficient signs add error magnitudes, and a zero coefficient is either of the wrong sign or too large. If k<h, then m<=a-2. Its opposite-sign error has magnitude

    l*|delta_(n-1)|-m*d >= (2+gamma)*d > 2d.

Thus no earlier positive visit is possible. At h, m=a-1 and l=1 give the required opposite error (1+gamma)*d<2d. As before the initial equality interval starts at zero or one, according to the sign of delta_n. Its debt for period 2q_n is

    (a-3)*q_n+q_(n-1)-1, or
    (a-3)*q_n+q_(n-1)-3.

These tend to infinity along any infinite set of coefficients at least three. Condition (1) therefore forces eventually a_n<=2. Combined with eventual evenness from the numerator obstruction, it forces eventually a_n=2. This proves (1) implies (2), with explicit violating intervals whenever either obstruction occurs infinitely often.

**Converse: finite exceptions cost only a finite constant.** Assume (2), put r=sqrt(2)-1, and take n sufficiently late. Then the exact error ratios and recurrence are

    |delta_(n-1)|=(2+r)*|delta_n|,
    |delta_(n+1)|=r*|delta_n|,
    q_(n+1)=2q_n+q_(n-1).

The even-numerator mediants have denominator B_n=q_n+q_(n-1) and numerator A_n=(p_n+p_(n-1))/2. They approximate alpha=beta/2 with alternating errors D_n=(delta_n+delta_(n-1))/2, whose successive magnitude ratio is r. Consecutive pairs (A_n,B_n) are unimodular, as direct substitution gives determinant of absolute value one; their denominators satisfy the same tail-two recurrence. Moreover

    B_n*|D_n| = 1/(B_(n+1)/B_n+r)
                -> 1/(2*sqrt(2)) < 1/2.

Legendre's criterion makes them genuine alpha convergents for all sufficiently late n. They are consecutive: their errors have opposite signs, whereas a skipped even number of convergent steps has the same sign, and a skipped odd number of at least three has determinant of magnitude at least two. Thus alpha also has an eventual continued-fraction tail of twos. Its late same-sign error records are its convergents and intervening mediants, by G143's unimodular record argument. Their beta periods are B_n and B_n+B_(n-1)=2q_n. There are only finitely many earlier record periods.

For every sufficiently late B_n or 2q_n, G143's entire mesh and first-hit argument applies verbatim with the displayed error ratios: a q_(n+1)-point orbit mesh has largest gap (1+r)*|delta_n|; no positive arc visit precedes q_n; the mediant visits provide the required first-hit upper bound. Consequently every repeat at these candidate periods satisfies b<2a+q, without any assumption on the finite continued-fraction prefix. Same-sign mismatch-interval inclusion reduces all other late periods to these records.

Each of the finitely many earlier record periods has a nonempty mismatch arc. Irrational rotation has a finite orbit mesh finer than that arc, so every translate of a sufficiently long fixed block hits it. Its equality runs therefore have bounded length, and its repeat debt has a finite upper bound independent of a. Taking the maximum of these finitely many bounds and zero supplies C. This proves (2) implies (1).

**Unexpected parity controls and limits.** The tail-two angle beta=sqrt(2)-1 fails the criterion: it has infinitely many even convergent numerators. Already the convergent 2/5, followed by 5/12, gives a period-5 equality on [0,11] of debt 6. Thus being in the silver quadratic field or having a tail of twos alone is insufficient. Conversely beta=[0;1,1,4,4,...] has eventually all odd numerators but fails by the doubled-period obstruction. These are direct arithmetic controls, not new runs. They distinguish both required conditions from weaker shortcuts.

Every angle satisfying (2) has a finite integer continued-fraction prefix followed by the same infinite tail, so there are countably many and they are quadratic. Their complements and arbitrary phases were not classified here. The wall has a necessary repeat constant determined by its finite left radius, so the theorem excludes all other phase-zero codes as companions. The exceptional class remains unresolved for actual initial-tail support. No finite witness, full right extension, positive-entropy or prize claim follows.

*Second reader's note on G144 (Local, 2026-10-07; chat L100).* Correct, read jointly with G143 as asked. Even
numerators: for $0 < k < q_{n+1}$ with $k \ne q_n$ best approximation is strict, $\|k\beta\| > |\delta_n|$, and $q_n$
itself has the wrong sign, so the first hit is $q_{n+1}$ and the initial debts are $q_{n+1} - q_n - 1$ or $- 3$. Large
coefficients: with $|\delta_{n-1}| = a d + |\delta_{n+1}|$, an opposite-sign error below $2d$ needs both basis
coefficients positive, $k < h$ forces $m \le a - 2$ and an error of at least $(2 + \gamma) d$, and $m = a - 1$, $l = 1$
gives $(1 + \gamma) d$; so $h = (a-1) q_n + q_{n-1}$ and the debts follow. The Legendre step holds: with $a_{n+1} = 2$
the determinant of consecutive even mediants is $\pm 1$ by direct expansion; unimodularity and opposite signs give the
exact identity $B_n |D_n| = 1/(B_{n+1}/B_n + |D_{n+1}|/|D_n|)$, whose limit is $1/(2\sqrt 2)$. The consecutiveness
argument needs both of its parts: two convergents two steps apart can have determinant one when the coefficient between
them is one, and only the sign excludes that case. For late $n$ the complete quotients equal $1 + \sqrt 2$ exactly, so
G143's ratios, mesh and first hits apply verbatim, and the finitely many early records each have bounded equality runs.
Checked (`rule30_audit_g99_g100.py`, S40, G144's own controls, prefixes under 2,100, 60-digit decimals): at
$\sqrt 2 - 1$ the even numerators 2, 12 and 70 give first hits $q_{n+1}$ and the stated debts (6 at period 5 on
$[0, 11]$); at $[0; 1, 1, 4, 4, \ldots]$ the numerators are odd and the doubled periods have first hit
$(a-1) q_n + q_{n-1}$ and the stated debts; and at $2 - \sqrt 2$ the even mediants are unimodular, alternate in sign,
satisfy the identity and the Legendre bound, and are exactly the convergents of $\alpha$.
