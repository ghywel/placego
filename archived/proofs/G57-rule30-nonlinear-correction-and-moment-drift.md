# Rule30 nonlinear correction and moment drift

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT57. Rule30 nonlinear correction and
moment drift"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

How a Rule 30 pattern drifts round a prime ring is set exactly by where its "and" operations happen.

**What it says.** Rule 30 is a simple sum of neighbours plus a correction wherever two neighbouring squares are both
black. GPT showed that the drift of G56's phase is an exact formula in that correction: where the correction sits,
weighted by position.

**Why it matters.** It ties the drift to Rule 30's non-linear part, the part that makes it hard. It does not yet say
the drift is never zero.

**An everyday picture.** A shopping trolley with one sticky wheel: left alone it would roll straight, and every
swerve it makes comes from where and when that wheel catches.

## The formal statement and proof

**Where:** RULE30-GPT.md G57; copied proof. **Status:** second-read by Local, 2026-10-06 (note below); DC controls not run at publication, now DC1-DC3 pass (G57 outcome).

### G57 lemma and proof: nonlinear correction determines moment-phase drift

Work modulo a prime p. For a nonconstant state x whose Rule30 successor y is also nonconstant, put w=sum_i x_i and m=sum_i i*x_i, with indices modulo p. Define the local arrays

    T_i=x_i*x_(i+1),
    H_i=x_(i-1)*(x_i OR x_(i+1)),
    E_i=T_i+2*H_i,
    C=sum_i E_i as an integer; D=sum_i i*E_i modulo p.

Then the exact integer weight identity and modular moment identity are

    w(y)=3*w-C,
    m(y)=3*m-D modulo p,

where the first identity uses the ordinary integer sum C. Consequently G56's moment-phase increment is

    delta(x)=(C*m-D*w)/(w*w(y)) modulo p.

Proof. Set A_i=x_(i-1),B_i=x_i OR x_(i+1)=x_i+x_(i+1)-T_i. Rule30 gives y_i=A_i XOR B_i=A_i+B_i-2H_i. Summing proves the weight identity. The moments of the shifted arrays x_(i-1) and x_(i+1) are m+w and m-w modulo p. Therefore the moment of A+B is3m minus the moment of T; subtracting2H gives3m-D. Both weights are invertible under the stated nonconstant assumptions. Subtracting m/w from(3m-D)/(3w-C) gives the formula. No division by C or assumption C!=0 is made.

The numerator C*m-D*w is rotation-invariant: rotation sends m to m+w and D to D+C while preserving C,w. This is consistent with G56's rotation-invariant increment. The identity turns phase drift into a local nonlinear-correction moment; it does not control its sign or show a quotient cycle has nonzero total.

A phase coordinate has freedom. If phi is any rotation-invariant function on nonconstant states, theta'=theta+phi is still rotation-covariant. Its edge increment is delta'=delta+phi(Fx)-phi(x). Around a quotient cycle the added terms telescope to0, because the endpoint is a rotation of the initial state. Thus displacement is coordinate-independent while individual edge increments can change. Unexpected scope check: changing phi at one vertex of a quotient cycle of length at least2 changes its incoming and outgoing increments by opposite amounts, preserving the total. A nonzero increment at each step alone is also insufficient: p increments of1 sum to0 modulo p.

This is elementary Boolean/integer algebra and a coordinate-change identity, derived from the recorded Rule30 rule and G56, without a novelty claim. The known zero-displacement cycles at7 and11 remain necessary controls. The missing statement is still a Rule30-specific restriction on the cycle sum, not an identity for one edge.

*Second reader's note on G57 (Local, 2026-10-06; chat L030).* Correct. Rule 30 is $y_i = A_i + B_i - 2A_iB_i$ with
$A_i = x_{i-1}$, $B_i = x_i + x_{i+1} - T_i$ and $A_iB_i = H_i$; summing gives $w(y) = 3w - C$, and the shifted moments
$m + w$ and $m - w$ give $m(y) = 3m - D$; subtracting $m/w$ gives $\delta = (Cm - Dw)/(w\,w(y))$, both weights being
invertible for nonconstant states; rotation sends $(m, D)$ to $(m + w, D + C)$, so the numerator is invariant. Checked
exhaustively (`rule30_audit_g55.py`, G57 part): all four identities on all 10,392 states of the prime rings 5, 7,
11, 13 whose successor is nonconstant, zero failures. G027's gauge remark is also right: adding any class function
to $\theta$ shifts consecutive increments by opposite amounts and leaves every cycle sum unchanged.
