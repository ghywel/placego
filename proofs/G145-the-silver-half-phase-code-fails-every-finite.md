# the silver half-phase code fails every finite repeat allowance

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT145. the silver half-phase
code fails every finite repeat allowance (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Moving the starting point half a turn changes the verdict: the silver half-turn code fails.

**What it says.** For the silver angle, whose continued-fraction digits (the whole numbers you get by repeatedly
taking off a number's whole part and turning what is left upside down) are all 2, the boundary-start code passes the
repeat test (G144). Starting half a turn later produces repeats whose excess grows without bound, the first one
already seen by Local at period seven, so that code is excluded.

**Why it matters.** The starting point matters, not just the angle.

**An everyday picture.** The same tune started on the off-beat clashes with the band.

## The formal statement and proof

### G145. The silver half-phase code fails every finite repeat allowance (2026-10-07)

**Status and target.** Symbolic Q7 proof, independent review pending. No experiment. G143 is independently verified by Local L099; G144 remains under review. This block follows the finite half-phase control HR3 already preregistered in GC159 and reported by Local L097. The prediction is that its debt-3 witness is the first member of an unbounded family. The counterfactual is a uniform finite debt bound at this phase. The proof uses G143's explicit convergents and mismatch interval, not a new computational scan or a theorem imported from the Rote literature in PRIOR-ART.md.

Put beta=2-sqrt(2), r=sqrt(2)-1 and c_s=floor(s*beta+1/2) modulo2. Let p_n/q_n be beta's convergents, with n=1 giving 1/1 and n=2 giving 1/2. For every odd n>=3, put Q_n=q_n+q_(n-1). Then the period-Q_n prefix equality interval is exactly

    [0, h_n-1],    h_n=2q_n+q_(n-1)/2,

and its debt is

    (h_n-1)-Q_n = q_n-q_(n-1)/2-1 -> infinity.

Consequently no finite C makes b<=2a+q+C hold for every repeat of this half-phase code. In particular it cannot be the wall's companion from any finite left radius. This concerns the chosen half-phase silver code, not every phase or angle.

**Proof of the first hit.** For these odd n, q_n is odd, q_(n-1) is even, and both numerators are odd. Set d=|delta_n|, where delta_n=q_n*beta-p_n. The exact signed errors are delta_n=-d and delta_(n-1)=(2+r)d. Period Q_n has an even numerator and positive error E=(1+r)d. Since E<1/2 for n>=3, its mismatch interval in the shifted coordinate is [1-E,1). Thus a positive time k is a mismatch exactly when

    {k*beta} is in [1/2-E,1/2).

Equivalently, there is an odd integer p with 2k*beta-p negative and magnitude at most 2E. Equality at the endpoint is impossible: it would imply an integer multiple of beta is an integer, since E=Q_n*beta-(p_n+p_(n-1)). Expand the integer pair (p,2k) in the unimodular basis (p_n,q_n),(p_(n-1),q_(n-1)), with integer coefficients m,l. Denominator parity forces m even; odd numerator parity then forces l odd. Its error is

    [-m+(2+r)l]*d.

A negative error of magnitude less than 2E requires m,l>0. Indeed m<=0,l>0 has the wrong sign; both negative give a negative denominator. If m>0,l<0, parity gives m>=2 and |l|>=1, and the magnitude is at least (4+r)d>2E. A zero coefficient is ruled out by parity, has the wrong error sign, or has a nonpositive denominator. Therefore m is a positive even integer and l a positive odd integer.

For l=1, the first possible m is 4: m=2 has positive error; m=4 has negative error of magnitude (2-r)d<2E. It gives denominator 4q_n+q_(n-1), hence time h_n. If l>=3, negative error requires m>(2+r)l, so m>=8; its denominator exceeds the one just found. This proves h_n is the first positive mismatch. Time zero is not a mismatch, since its shifted coordinate is 1/2. The prefix equality and its exact endpoint follow.

The denominator recurrence gives unbounded q_n and q_(n-1)<q_n, so the displayed debt is greater than q_n/2-1 and diverges. This proves the exclusion for every finite allowance.

**Unexpected check and scope.** At n=3 the convergents are 3/5 and 1/2: Q_n=7, h_n=11, and debt=3, exactly HR3's retained finite witness. The same angle at phase zero passes every period with C=0 by G143. Thus changing the phase can change boundedness of the repeat debt, not just its finite constant. This is not a finite Rule30 witness at either phase. The boundary-phase exceptional angles in G144 and their actual forced initial tails remain unresolved; no prize claim follows.

*Second reader's note on G145 (Local, 2026-10-07; chat L101).* Correct. At phase one half the mismatch rule for period
$Q_n$ moves the arc to $\{k\beta\} \in [1/2 - E, 1/2)$, which is exactly an odd $p$ with $2k\beta - p \in [-2E, 0)$. For
odd $n$ the denominators $q_n$ are odd and $q_{n-1}$ even, so in the basis expansion of $(p, 2k)$ the coefficient $m$ is
even and $l$ odd, and the error is $(-m + (2+r) l) d$. Mixed signs give at least $(4 + r) d > 2E$, zero coefficients
fail by parity, sign or denominator, and for $l = 1$ only $m = 4$ lands in the window $(2 + r, 4 + 3r)$; every $l \ge 3$
needs $m \ge 8$ and a larger denominator. So the first hit is $h_n = 2q_n + q_{n-1}/2$, time zero is not a mismatch, and
the prefix debt is $q_n - q_{n-1}/2 - 1$. The phase contrast with G143 is the striking part: the same angle passes every
period at phase zero with $C = 0$ and fails every finite allowance at phase one half. Checked
(`rule30_audit_g99_g100.py`, S41, within GC159's 4,096 symbols, the integer floors cross-checked against 60-digit
decimals): for $n = 3, 5, 7, 9$ the first mismatch of period $Q_n$ is $h_n$, every mismatch time lies in G145's arc and
every arc time is a mismatch, and the prefix debts are 3, 22, 133 and 780, the first being HR3's witness.
