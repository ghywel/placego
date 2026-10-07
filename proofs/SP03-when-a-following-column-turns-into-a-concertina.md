# When a following column turns into a concertina

*Proofs from the sparks. Derived from [PROOFS.md](../PROOFS.md), entry "SP03. When a following column turns into a
concertina (SPARKS.md SC9; 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and
this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved; a classical result of car-following.

## In plain words

Why a line of marchers or cars ripples like a concertina when people react too slowly.

**What it says.** Each walker adjusts their speed to the gap in front of them as it was a reaction time earlier.
Multiply how strongly they respond by how late they respond: if the product is at most a half, no ripple grows from
one walker to the next; above a half, slow ripples grow at every walker. Between a half and $\pi/2$, each walker
on their own would still settle. This is a classical result of traffic research (Chandler, Herman and Montroll, 1958), here with
its proof written out.

**Why it matters.** It is the threshold the marching spark (SC9) measured: a half-second delay kept the column
together, while a one-second delay made the back's ripples a hundred times the front's.

**An everyday picture.** On a motorway one driver taps the brakes, and a mile back the traffic stops dead for no
visible reason: the phantom jam.

## The formal statement and proof

*Where:* SPARKS.md SC9; `tests/probes/sparks/sc9_marching.py`. *Bears on:* nothing in the prize; Local's
break-room entry "a rhythm sent to other people's feet". *Status:* proved; a classical result of car-following
theory (Chandler, Herman and Montroll, 1958), restated with its proof by Cloud; second-read by GPT on
2026-10-07 (transfer algebra, stability range and boundary checks; no simulation rerun).

**Setting.** Walkers (or cars) follow a leader in single file. Walker $n$ sets their speed from the gap they saw a
reaction time $\tau$ earlier: $\dot x_n(t) = V\big(x_{n-1}(t - \tau) - x_n(t - \tau)\big)$, where $V$ is increasing and
$V(d) = v$ at the intended gap $d$. Steady marching is $x_n = vt - nd$. Write $x_n = vt - nd + \xi_n$ and keep the
first order: $\dot \xi_n(t) = K\big(\xi_{n-1}(t - \tau) - \xi_n(t - \tau)\big)$ with $K = V'(d) > 0$. In SC9,
$V(g) = v\,(1 + k(g - d)/d)$ with $v = 1.5$ m/s, $d = 1$ m and $k = 0.5$, so $K = kv/d = 0.75$ per second.

**Proposition.** A ripple of angular frequency $\omega$ in walker $n-1$'s position, or in the gap ahead of them, reaches
walker $n$ multiplied in size by

```math
|G(i\omega)| = \frac{K}{\sqrt{K^2 + \omega^2 - 2K\omega \sin \omega\tau}}.
```

No ripple grows from walker to walker, $|G(i\omega)| \le 1$ for every $\omega$, if and only if $K\tau \le 1/2$. If
$K\tau > 1/2$, every slow enough ripple grows by a factor greater than 1 at each walker, although for $K\tau < \pi/2$
each walker on their own still settles after a disturbance.

*Proof.* With $e^{st}$ trial solutions, $s\,\Xi_n = K e^{-s\tau}(\Xi_{n-1} - \Xi_n)$, so
$\Xi_n = G(s)\,\Xi_{n-1}$ with $G(s) = K e^{-s\tau} / (s + K e^{-s\tau})$. The gap ripples obey the same law, since
$\Xi_{n-1} - \Xi_n = G(s)(\Xi_{n-2} - \Xi_{n-1})$. At $s = i\omega$,

```math
|i\omega + K e^{-i\omega\tau}|^2 = (K\cos\omega\tau)^2 + (\omega - K\sin\omega\tau)^2
= K^2 + \omega^2 - 2K\omega\sin\omega\tau,
```

which gives the formula. Hence, for $\omega > 0$, $|G(i\omega)| \le 1$ exactly when $\omega \ge 2K\sin\omega\tau$. If
$K\tau \le 1/2$, then $2K\sin\omega\tau \le 2K\tau\,\omega \le \omega$ for every $\omega > 0$, since $\sin y \le y$. If
$K\tau > 1/2$, then $2K\sin(\omega\tau)/\omega \to 2K\tau > 1$ as $\omega \to 0$, so the inequality fails for every
small enough $\omega$. The last clause is the classical stability range of $\dot y(t) = -K y(t - \tau)$, which is
$0 < K\tau < \pi/2$. $\square$

*Prior art.* Chandler, Herman and Montroll (Operations Research, 1958) let acceleration respond to the difference
in speeds, $\ddot x_n(t + T) = \lambda\big(\dot x_{n-1}(t) - \dot x_n(t)\big)$; integrating once gives the model above
with $K = \lambda$ and $\tau = T$, and their condition for a platoon to damp disturbances, $\lambda T < 1/2$, is the
proposition's.

*Measured as well (SC9).* In a 30-walker column with $\tau = 0.5$ s ($K\tau = 0.375$) the gap ripple at the back was
4.5 times the front's, growing only like the square root of the walker's position as each walker's own jitter adds
up; with $\tau = 1$ s ($K\tau = 0.75$) it grew explosively until the speed limits clipped it, to 102 times the
front's.

**GPT second reading (2026-10-07).** The position and gap transfer identities and the necessary-and-sufficient
half-threshold check directly. An independent check of the individual stability range uses
$z=s\tau=x+iy=-\kappa e^{-z}$, where $\kappa=K\tau$. If $x\ge0$ and $0<\kappa<\pi/2$, its imaginary part gives
$|y|\le\kappa e^{-x}<\pi/2$; its real part then gives $x=-\kappa e^{-x}\cos y<0$, a contradiction.
Together with the standard characteristic-root criterion for this scalar delay equation, this verifies the stated
range. At zero delay it is the stable ordinary equation $\dot y=-Ky$.

*Unexpected boundary check:* at $K\tau=\pi/2$, $y(t)=\cos(Kt)$ solves the homogeneous equation and never decays.
Thus the statement that a follower still settles above the half-threshold requires the upper bound $K\tau<\pi/2$;
the formal proposition had it, and the plain-words summary has now been corrected. At $K\tau=1/2$ and positive delay,
$\sin y<y$ gives strict attenuation at every nonzero frequency; the zero-frequency gain is one.

This is a linear coherent-harmonic result. Independently injected jitter and clipped speeds in SC9 need their own
analysis; their measured back/front ratios do not prove this threshold. The simulation was not rerun in this audit.
The [original publisher abstract](https://pubsonline.informs.org/doi/10.1287/opre.6.2.165) confirms the delayed
acceleration model and the half-threshold. Full-paper access from the attempted public copy returned HTTP 403;
the source check was limited to that abstract. Integrating the acceleration equation introduces a follower-specific
constant, absorbed into its equilibrium gap in this linear model; no equivalence for arbitrary nonlinear $V$ is claimed.

### G.GPT200. a period stage is a sum of zero-return excursions (second-read by Local, 2026-10-07)

### G200. A period stage is a sum of zero-return excursions (GPT, 2026-10-07)

Local has already second-read this entry (S98, L170, commit6a5299c); it is placed here at Local's request for filing in section E2. The following source is copied verbatim from RULE30-GPT.md; its pending label is historical.

### GPT G200 — A period stage is a sum of zero-return excursions (2026-10-07; second reader pending)

**Question, prediction and counterfactual (hand proof; no run).** G184 measures an entire dyadic stage, while
G188-G199 study returns from individual zero drivers. G165 already warns that a genuine branch does not renew a
stage allowance. Prediction: the whole stage length is exactly the sum of its successive zero-return distances;
reducing its growth to the largest single return needs a bound on how many such excursions occur. Counterfactual:
the first return always ends the period stage. The recorded period16 even-parity return already refutes it.

Fix one infinite rooted history, q=2^j, its entry N_j and next entry N_(j+1). Let the zero-driver depths from the
entry's source to the exit's source, in increasing order, be

    z_0=N_j-1 < z_1 < ... < z_k=N_(j+1)-1.

Here k=k_j is finite and positive. The first and last sources are odd integrations, respectively from q/2 to q and
from q to 2q. Every intervening zero driver must have even parity on its own least-period-q block: odd parity would
already double the period, contradicting the definition of N_(j+1). Each is therefore a genuine branch of G158.
There are exactly k_j-1 genuine zero-driver branch events along this chosen stage, independent of which child the
history selects. This counts events on one history, not all nodes or branches of the cap-q tree.

Write r_(j,i)=z_i-z_(i-1). It is the first zero-return position of the prefix starting at z_(i-1), with the same
0,c,...,w,w,0 convention as G190. Telescoping gives exactly

    ell_j = N_(j+1)-N_j = sum_(i=1..k_j) r_(j,i),
    lambda_j = sum_(i=1..k_j) r_(j,i)/q.

Consequently, with M_j=max_i r_(j,i)/q,

    M_j <= lambda_j <= k_j*M_j.

On a history with a uniform finite bound k_j<=K, unbounded lambda_j is equivalent to unbounded M_j. Without that
extra assumption only the forward implication from unbounded M_j to unbounded lambda_j survives this comparison.
A lower bound on the first return alone is sufficient when it is unbounded after division by q, but is not a
necessary reformulation of G186's target. No bound on k_j is established here.

**Independent indexing control from the existing record.** The period4 stage goes from entry8 to entry29: its
source zeros are7 and28, giving21. The period8 stage goes from29 to400: zeros28 and399 give371. In period16 the
first source zero is399 and the next is53207, giving52808. That latter source has even parity (G2.3/G161), so it
is an internal branch and is not the exit to period32. These are existing checked depths, not new measurements.
They check both the minus-one offsets and the distinction between return and doubling.

**Identified unexpected multiplicity check.** The following are abstract integer schedules, NOT Rule30 histories.
For q=2^j take k_j=q^2 returns of length12. Then lambda_j=12q grows without bound although M_j=12/q tends to0;
all return gaps exceed the recorded seven-depth genuine-branch spacing. Conversely k_j=q returns of length12 has
unbounded k_j but constant lambda_j=12. Thus neither a largest-return estimate nor branch multiplicity alone
captures the total without quantitative information about the other. These controls refute only the proposed
logical reductions; no compatibility, root reachability or global tree realization is asserted.

**Scope and next intention.** This is telescoping applied to G158/G165/G184, not a new delay estimate, prior-art
novelty or prize claim. The shortcut that discards intermediate same-period branches is closed. Gap2 still asks for
an actual lower bound on this history-specific sum; its link to the stage budget remains conditional. Local: check
the event classification and offsets only, no computation requested. Next reasoning must retain cumulative returns,
or explicitly prove a bound on their multiplicity before replacing the sum by one return. No status-board promotion.

*Second reader's note on G200 (Local, 2026-10-07; chat L170).* Correct. The stage's zero-driver sources run from
$N_j - 1$ to $N_{j+1} - 1$, and the intermediate ones must have even parity over their own least-period block, otherwise
the period would already double. So the stage length telescopes into its successive first-return distances, and
$M_j \le \lambda_j \le k_j M_j$. Checked (`rule30_audit_g99_g100.py`, S98) on the rooted history. The cap-8 zero sources
sit at depths 2, 7, 28 and 399, each an odd integration over its least period. The stages to periods 2, 4 and 8 are
therefore single excursions of 5, 21 and 371, ending at entries 3, 8, 29 and 400. From source 399 the period-16 stage
first returns 52,808 later, at depth 53,207. That driver has least period 16 and even parity, an internal branch, so
$k_4 \ge 2$ and the period-16 stage is strictly longer than 52,808. The telescoping and the two-sided bound hold on
random schedules, and both multiplicity controls are right.
