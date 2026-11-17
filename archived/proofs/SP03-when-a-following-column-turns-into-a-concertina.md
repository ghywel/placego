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
