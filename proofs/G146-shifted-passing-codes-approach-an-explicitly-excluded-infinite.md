# shifted passing codes approach an explicitly excluded infinite tail

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT146. shifted passing codes
approach an explicitly excluded infinite tail (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Codes that pass the test can come as close as you like to one that fails.

**What it says.** Every time-shifted copy of the passing silver code still passes, but needs an ever larger
allowance, and the shifts approach the failing half-turn code. Their starting rows approach one particular infinite
row.

**Why it matters.** A bound that holds for each pattern separately cannot be used as one bound for the whole family,
and approaching an infinite row does not rule out a finite seed whose edge grows.

**An everyday picture.** Each step towards a cliff is safe on its own, yet the steps lead to the edge.

## The formal statement and proof

### G146. Shifted passing codes approach an explicitly excluded infinite tail (2026-10-07)

**Status and target.** Symbolic Q7 closure audit, independent review pending. Depends on verified G140/G143 and the pending G145 half-phase exclusion. No experiment. Prediction: every time shift of the passing silver code still has some finite repeat allowance, but these allowances cannot be uniform when the phases approach one half. Counterfactual: closure of the passing family might transfer its repeat bound, or finite support, to every limiting rotation phase. G142 already closes the general finite-support compact-limit shortcut; this block names a specific excluded limit and identifies exactly which allowance loses uniformity. Existing rotation and wall-coding records are used, with no new prior-art theorem or computational job.

For a binary one-sided word x define B_C by the requirement that every equality interval x_s=x_(s+q), a<=s<=b, satisfies b<=2a+q+C, for all a>=0 and q>=1. Take C>=0, and put B=union over all nonnegative integer C of B_C. Let sigma be the left shift.

**Shift and finite-prefix control.** If x belongs to B_C, sigma^t x belongs to B_(C+t). A repeat of the shifted word translates to [a+t,b+t] in x, whose bound gives b<=2a+q+C+t. Conversely, if sigma^t x belongs to B_C, then x belongs to B_(C+t). For a repeat of x with a>=t, translate back and use the shifted bound. If a<t<=b, its suffix [t,b] translates to a repeat starting at zero, giving b<=t+q+C<=2a+q+C+t. If b<t, the bound is automatic. Thus x is in B if and only if sigma^t x is in B. Words that agree after a finite prefix also agree on membership in B. Global complementation preserves every B_C exactly.

**Closed at fixed allowance, not at some allowance.** Each B_C is closed in the product topology: any violation is certified by a finite repeat witness, involving finitely many coordinates through b+q, and persists in the corresponding cylinder. An intersection of these closed finite-witness constraints is closed. This does not make their increasing union B closed.

Let beta=2-sqrt(2) and c^(rho)_s=floor(s*beta+rho) modulo2, with rho considered modulo2. G143 places c^(0) in B_0, hence every sigma^t c^(0)=c^(t*beta modulo2) is in B. Irrational rotation has a dense forward orbit, so choose t_j with t_j*beta modulo2 tending to 1/2. No coordinate s*beta+1/2 is an integer, so every fixed finite prefix eventually agrees exactly with c^(1/2). Therefore

    sigma^(t_j)c^(0) -> c^(1/2),

while G145 gives c^(1/2) not in B. This proves B is not closed. More precisely, for any fixed C, choose a G145 witness with debt greater than C. Every sufficiently large j shares all coordinates of that witness and fails B_C. Thus the smallest nonnegative repeat allowances for these passing shifted words tend to infinity, not just along some unspecified subsequence. The simple upper allowance t_j remains valid.

The passing phases t*beta modulo2 and the excluded phases 1/2+t*beta modulo2 are both dense. The latter exclusion follows from the reverse-shift implication above. These are two countable dense phase orbits, not a classification or measure statement about the other phases. They are disjoint by irrationality.

**An explicit infinite forced-tail limit.** In G140's notation Phi maps a visible word to its unique compatible initial left row and satisfies F Phi=Phi sigma for the two-step wall evolution F. Its exact finite-prefix modulus makes Phi continuous. Put u_0=Phi(c^(0)) and u_half=Phi(c^(1/2)). Then

    F^(t_j)(u_0) = Phi(sigma^(t_j)c^(0)) -> u_half.

G145 and the wall's necessary finite-radius repeat bound force u_half to have infinite support. This identifies an infinite-support accumulation point of the actual forced-tail orbit of u_0, without assuming whether u_0 itself has finite support. If u_0 were finite, the exact radius clock in G141/G142 would grow by two per F, and such an infinite-support limit is entirely consistent. No contradiction to a finite u_0 follows. Nor does the existence of infinite support at the limiting phase provide a fixed depth beyond which every approximating phase is nonzero.

**Unexpected prefix guard and remaining obligation.** Altering finitely many symbols of a passing word cannot create the unbounded-debt failure, by the shift control just proved. Hence the half-phase failure is not explained by changing the first boundary symbol or a finite startup transient; the two codes differ at infinitely many times. The phase comparison still yields no lower bound on the actual support of u_0. Q7's remaining obligation is a constraint on that individual forced tail, beyond repetition or nonuniform compact limits. No finite witness or prize claim follows.

*Second reader's note on G146 (Local, 2026-10-07; chat L102).* Correct. The shift control holds in both directions,
including the straddling case $a < t \le b$, where the suffix $[t, b]$ gives $b \le t + q + C$. Each $B_C$ is closed
because a violation is a finite witness. $\sigma^t c^{(0)} = c^{(t\beta \bmod 2)}$ holds since adding 2 to the phase
leaves every parity unchanged. Convergence to $c^{(1/2)}$ is coordinatewise, because no $s\beta + 1/2$ is an integer, so
each G145 witness is eventually inherited and the least allowance escapes along the whole approach, not along a
subsequence. The two dense phase orbits are disjoint by irrationality, and continuity of $\Phi$ with
$F \Phi = \Phi \sigma$ carries the limit to the forced rows. As the block says, this gives no contradiction for a finite
$u_0$ (G142). Checked (`rule30_audit_g99_g100.py`, S42, only GC159's 4,096 symbols of $c^{(0)}$): the shift identity,
the shift allowance (maximal debt at most $t$) on the seven shifts below 2,048 that set a new closest phase to 1/2, and
the G145 witnesses for $n = 3, 5, 7$ inside every shifted prefix whose agreement with $c^{(1/2)}$ covers them.
Descriptive: at $t = 11, 18, 35, 373$ the maximal debt is exactly $t - 3$, so the shift allowance is nearly attained.
The reason: a G143 interval lying wholly beyond $t$ gains exactly $t$ in debt under the shift, and the maximum comes
from a sharp one, for example $[13, 40]$ at period 17 when $t = 11$. My first draft of S42 also expected the agreement
and the debt to rise monotonically along those shifts. G146 claims neither; the approach alternates sides of 1/2 and the
prefix truncates the debt, so that draft failed and was narrowed.
