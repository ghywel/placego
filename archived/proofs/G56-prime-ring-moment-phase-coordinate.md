# Prime-ring moment phase coordinate

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT56. Prime-ring moment phase
coordinate"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A "centre of mass" for patterns on a prime ring tells exactly how far a cycle drifts.

**What it says.** Give each black square its position, and average the positions in clock arithmetic on a dial of p
hours. This "phase" moves by exactly one when the ring is turned by one, so it measures drift. A cycle's total drift
is the sum of the phase changes along it.

**Why it matters.** It makes G55's drift computable step by step. Whether the drift can be zero for Rule 30 is still
open.

**An everyday picture.** A clock dial of p hours on which each black square adds its own hour: the total moves on by
exactly one hour when the ring is turned by one square, so watching that total shows how far the pattern has
drifted.

## The formal statement and proof

**Where:** RULE30-GPT.md G56; copied proof. **Status:** second-read by Local, 2026-10-06 (note below); PH controls not run at publication, now PH1-PH3 pass (G56 outcome).

### G56 lemma and proof: a prime-ring rotation phase

Number sites0,...,p-1 so R moves the bit at i to i+1 modulo the prime p. For a nonconstant binary state x, define its weight w(x)=sum_i x_i and moment m(x)=sum_i i*x_i modulo p. Since1<=w(x)<=p-1, w(x) is invertible modulo p. Set

    theta(x)=m(x)*w(x)^(-1) modulo p.

Rotation preserves w and gives m(Rx)=m(x)+w(x) modulo p, including the wrap from p-1 to0. Therefore theta(Rx)=theta(x)+1. Each rotation class has a unique representative N(x)=R^(-theta(x))x with theta0. This is another exact quotient coordinate, not a new quotient or a claim of measured computational speedup.

Whenever x and F(x) are nonconstant and F commutes with R, the phase increment delta(x)=theta(F(x))-theta(x) is rotation-invariant. For a q-cycle of rotation classes, use theta0 representatives x_j and let e_j=theta(F(x_j)). Its quotient update is x_(j+1)=R^(-e_j)F(x_j). Repeated commutation gives

    F^q(x_0)=R^(e_0+...+e_(q-1))x_0.

Thus G55's displacement is b=sum_j e_j modulo p. Equivalently delta summed along the actual q-step lifted path telescopes to b. The coordinate does not show b is nonzero: the verified zero-displacement cycles at7 and11 remain valid. A Rule30-specific restriction on these phase sums is still needed.

Unexpected domain check: on a four-cell ring x=0011 has weight2 and four distinct rotations, yet2 has no inverse modulo4. A free spatial orbit alone does not justify this moment coordinate on composite rings. The constant states also have weight0 modulo p and are excluded explicitly. Lexicographic rotation representatives still work in those cases; this particular formula does not.

This is a direct elementary coordinate for the cyclic action, derived here and without a novelty claim. It distinguishes spatial phase from the temporal clock quotient already used in G9; neither supplies the missing nonzero-displacement theorem.

*Second reader's note on G56 (Local, 2026-10-06; chat L029).* Correct. With $1 \le w(x) \le p - 1$ invertible modulo
the prime $p$, rotation adds $w(x)$ to the moment, so $\theta(Rx) = \theta(x) + 1$ and the $\theta = 0$ representative is
unique; the phase increment is rotation-invariant; and along a quotient cycle of $\theta = 0$ representatives,
$F^q(x_0) = R^{\sum e_j} x_0$ by repeated commutation, so $b = \sum e_j$. Checked (`rule30_audit_g55.py`, G56 part):
$\theta(Rx) = \theta(x) + 1$ on every nonconstant state for $p = 5, 7, 11, 13$, and the phase sums equal the directly
measured displacements on every quotient cycle: $(q, b) = (4, 0), (9, 5)$ at 7 and $(14, 8), (17, 0)$ at 11, exactly
GPT's G024 values, and $(7, 12), (19, 5), (20, 2), (64, 4)$ at 13, every displacement nonzero there.
