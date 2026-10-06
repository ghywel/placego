# Shifted passing codes approach an explicitly excluded infinite tail

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G146. Shifted passing codes
approach an explicitly excluded infinite tail (2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Every time shift of the passing silver code still passes with some finite allowance. Yet these shifted codes can approach the half-phase code, which fails every finite allowance. The required allowances grow without bound. Under the wall’s exact coding, the corresponding initial rows approach a specific row with infinite support. This does not rule out a finite starting row: its radius would grow at every step, as earlier proofs already require. A bound for each word cannot be used as a uniform bound for the whole family.

## The formal statement and proof

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
