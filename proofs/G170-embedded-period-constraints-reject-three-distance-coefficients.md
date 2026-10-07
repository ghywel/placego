# embedded period constraints reject three-distance coefficients

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT170. embedded period
constraints reject three-distance coefficients (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Even a formula allowed to change with the period fails, because a long period still contains short-period patterns.

**What it says.** G169's two period-4 steps can be repeated inside any larger period q, where they keep their short
waiting distances. Together with a period-q step they again contradict any choice of multiples for that q, unless
the allowance is at least 3q/(q + 1), which at period 8 exceeds the 5/2 allowed. Formulas that use each state's own
shortest period, or richer information, remain open.

**Why it matters.** It closes the obvious repair of G169 and says the next candidate must tell the period levels
apart.

**An everyday picture.** A fare chart for the long-distance line must still price the local stopping trains that
share its track.

## The formal statement and proof

### GPT G170 — embedded period constraints reject three-distance coefficients (RULE30-GPT.md G170; awaiting second reader, 2026-10-07)

**Stronger family restriction; review requested.** Fix a dyadic common period q>=8. Its compatible graph includes words whose least period divides q, as G7/G157 specify; it is not restricted to least period exactly q. Consider

    h_q(a,b,r)=C_q+alpha_q*D(a,r)+beta_q*D(b,r)+chi_q*D(a XOR b,r).

Here all four coefficients may depend on the common graph period q, but are shared by all its vertices. If this potential satisfies every gated edge inequality at slope gamma, then necessarily

    gamma >=3q/(q+1).

Thus no such formula certifies gamma5/2 at any dyadic common period q>=8. Even allowing coefficients to vary with the common period cannot rescue this family. For any fixed gamma<3 it fails at all sufficiently large dyadic q. This is a necessary bound, not a construction at equality, and nonnegativity of the coefficients is not assumed.

**Proof by three explicit edges.** Repeat G169's period4 words(12,8),(8,8),(9,0),(0,14) q/4 times in time. Shift, OR and XOR commute with this repetition, so their two edges remain compatible. Their phase0 delays and feature differences remain exactly the same: the gate reads time q-1, which has residue3 modulo4. Consequently their edge inequalities at slope gamma are

    -alpha_q+3*chi_q >=8-2*gamma,
    alpha_q-2*beta_q-chi_q >=-2*gamma.

Adding yields beta_q-chi_q<=2*gamma-4. The separate least-period-q single-pulse edge(b,b,0)->(b,0,0) remains gated and requires

    q*(beta_q-chi_q) >=2q-2*gamma.

Together these force2-2*gamma/q<=2*gamma-4, hence gamma>=3q/(q+1). Equivalently multiply each embedded inequality by q/2 and the pulse inequality by1. Every coefficient cancels, leaving0>=6q-2*gamma*(q+1). This explicit nonnegative combination is the contradiction certificate whenever the displayed necessary slope fails. C_q cancels separately on each edge. No numerical optimization is involved. Square.

**Known-value control and identified unexpected check.** At q8 the required slope is at least8/3, strictly larger than5/2. At gamma5/2 the cancelling combination gives0>=q-5, hence0>=3 at q8. The pulse itself has reward11 while the two embedded constraints give beta_q-chi_q<=1. At q4 the same combination gives no contradiction at5/2; no feasibility conclusion is made there. The unexpected ingredient is the embedded period4 states: their distances remain small after repetition, rather than scaling with q. Treating every q-bit word as having least period q would incorrectly erase these valid constraints.

**Scope and revised next intention.** G169's period-dependent-coefficient escape is now closed for coefficients chosen only by the common graph period. Coefficients chosen by the state's least pair period are different: the embedded states would use period4 coefficients and the pulse states period-q coefficients, so cancellation no longer follows. Nor does this reject nonlinear features, additional state information, a different domain proved closed, or rooted-only certificates. A full gated pair/phase potential is known feasible at gamma5/2 for q8; only this linear feature compression fails. Dependencies are G7's common-period convention, G169's literal edges and G160's gate. The repetition argument and linear dual certificate are elementary, with no novelty claim or new computation. Next useful family must distinguish embedded period strata or retain richer joint information; the all-period debt theorem remains open.

*Second reader's note on G170 (Local, 2026-10-07; chat L132).* Correct. Repeating G169's period-4 words $q/4$ times
commutes with the shift, OR and XOR, so both edges stay compatible. Their phase-0 delays and distance triples are
unchanged, and the gate reads time $q - 1$, which is 3 modulo 4. In doubled units at slope $\gamma$ the two embedded
inequalities give $\beta_q - \chi_q \le 2\gamma - 4$, and the least-period-$q$ pulse needs
$\beta_q - \chi_q \ge 2 - 2\gamma/q$. The weights $q/2, q/2, 1$ cancel every coefficient and leave
$0 \ge 6q - 2\gamma(q + 1)$, so $\gamma \ge 3q/(q + 1)$. That is $8/3 > 5/2$ at $q = 8$ and only $12/5$ at $q = 4$.
Checked (`rule30_audit_g99_g100.py`, S65) at $q = 8$ and 16: the repeated edges' children, gates, delays and triples,
and the dual combination's value for slopes on both sides of the bound. The scope point stands: coefficients chosen by
each state's least period are not covered.
