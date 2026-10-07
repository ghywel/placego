# Theorem E

*Windows, zero runs and the left band. Derived from [PROOFS.md](../PROOFS.md), entry "14. Theorem E"; rebuild with
`python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this
file.*

**Status:** proved.

## In plain words

A perfectly regular wheel, never nudged, cannot produce the pattern.

**What it says.** If column 1 is the trace of a wheel turning by a fixed irrational angle (a "Sturmian" sequence,
like the pattern of a clock hand passing a mark), the left half is never finite. With Jen's theorem for rational
angles, no un-kicked wheel of any speed works.

**Why it matters.** Column 1 next to a blinking wall really does behave like a wheel with occasional kicks. This
proves the kicks are necessary: any counterexample must come from the kicks, never from the turning alone.

**An everyday picture.** No metronome is ever truly left alone: friction in its own pivot drains its swing and
nudges its beat, with nobody touching it (the owner's reading). Theorem E is Rule 30's version. A perfectly regular
wheel cannot come from a finite seed, so column 1 must slip, and the slips come from Rule 30's own cells, not from
anyone outside.

## The formal statement and proof

*Where:* RULE30-PRIZE.md, "8.57 No pure rotation works: every Sturmian column 1 is excluded (2026-10-05)". *Bears on:* question 3 of PERIOD-TWO.md §7 (closed by §8.61): no pure rotation gives a period-two column. *Status:* proved.

**Theorem E.** Let $\alpha$ be irrational and $\theta$ any real number, and let column 1's visible bits be the
Sturmian sequence $c_s = 1$ if the fractional part of $\theta + s\alpha$ lies in $[1 - \alpha, 1)$, and $c_s = 0$
otherwise. Let column 0 be 0101… Then the forced left half is not eventually zero.

With Jen's theorem for rational $\alpha$: **no column 1 that codes a rotation in this way, by any angle and from any
starting point, can go with a finite left half.** In the language of §8.5: a wheel that is never kicked cannot hold
the left half, whatever its rotation number. Conjecture LR holds for every such column 1, and these are
uncountably many sequences of zero entropy, none of them eventually periodic.

*Proof.* Suppose the left half is zero beyond depth $L$. ($L \ge 1$: an empty left half fails the condition at
time 1.) Put $C = \lfloor (L - 3)/2 \rfloor$.

**Step 0: Theorem A in visible bits.** If $c_s = c_{s+q}$ for every $s$ from $s_a$ to $s_e$, then

```math
s_e \le 2 s_a + q + C . \tag{$\ast$}
```

Column $-1$ is $\bar c_s$ at even times and 1 at odd times (§8.39), so columns $-1$ and 0 are $2q$-periodic on the
times $2s_a$ to $2(s_e + q) + 1$. Theorem A, with the left edge $L - 1$ cells from column $-1$, gives $(\ast)$. It
needs no right half: its proof uses Rule 30 only at columns 0 and to the left.

**Notation.** Let $p_n / q_n$ be the convergents of $\alpha$, with partial quotients $a_n$, and
$\delta_n = q_n\alpha - p_n$. The signs of $\delta_n$ alternate, $|\delta_{n-1}| = a_{n+1}|\delta_n| + |\delta_{n+1}|$,
and $\|m\alpha\| \ge |\delta_n|$ for $0 < |m| < q_{n+1}$ ($\|\cdot\|$ is the distance to the nearest integer). Write
$x_s$ for $\theta + s\alpha$ on the circle, and $K_n$ for the half-open arc of length $|\delta_n|$ that ends at 0 if
$\delta_n > 0$ and starts at 0 if $\delta_n < 0$. Take $n$ large.

**Step 1: where $c$ breaks period $q_n$.** $c_{s+q_n}$ is the code of $x_s + \delta_n$, a point $|\delta_n|$ away from
$x_s$. The two codes differ exactly when an end of $[1 - \alpha, 1)$ lies between them, which is when $x_s$ or
$x_{s+1}$ is in $K_n$. Let $h < h'$ be the first two times the orbit visits $K_n$. A return to an arc of length
$|\delta_n|$ needs $\|(h' - h)\alpha\| < |\delta_n|$, so $h' - h \ge q_{n+1}$.

**Step 2: two inequalities at every scale.** $c_s = c_{s+q_n}$ for $0 \le s \le h - 2$, and again for
$h + 1 \le s \le h' - 2$. Apply $(\ast)$ to each stretch:

```math
h \le q_n + C + 2, \qquad h' \le 2h + q_n + C + 4 .
```

With $h' \ge h + q_{n+1}$ the second gives $h \ge q_{n+1} - q_n - C - 4$. So the first visit $h(n)$ to $K_n$ satisfies

```math
q_{n+1} - q_n - C - 4 \;\le\; h(n) \;\le\; q_n + C + 2 . \tag{$\ast\ast$}
```

**Step 3: a partial quotient of 2 or more.** If $a_{n+1} \ge 2$ then $q_{n+1} - q_n \ge q_n + q_{n-1}$, and
$(\ast\ast)$ is empty as soon as $q_{n-1} > 2C + 6$. So if infinitely many partial quotients are at least 2, the
proof is done.

**Step 4: all partial quotients 1 from some point on.** Then $q_{n+1} - q_n = q_{n-1}$ and
$|\delta_{n-1}| = |\delta_n| + |\delta_{n+1}|$. Put $s = h(n)$ and $s' = h(n+1)$. The arcs $K_n$ and $K_{n+1}$ lie on
opposite sides of 0, so $x_s$ and $x_{s'}$ are less than $|\delta_n| + |\delta_{n+1}| = |\delta_{n-1}|$ apart, on known
sides. By $(\ast\ast)$, $m = s - s'$ lies between $-q_n - 2C - 6$ and $2C + 6$, and $m \ne 0$ because the two arcs
are disjoint. An $m \ne 0$ with
$\|m\alpha\| < |\delta_{n-1}|$ has $|m| \ge q_n$, and for large $n$ the only one in that range with the right sign is
$m = -q_n$. So

```math
h(n+1) = h(n) + q_n \qquad\text{for every large } n .
```

The upper bound of $(\ast\ast)$ at $n + 1$ now gives $h(n) \le q_{n-1} + C + 2$, and the lower bound at $n$ gives
$h(n) \ge q_{n-1} - C - 4$. So $h(n)$ is within $C + 4$ of $q_{n-1}$, for every large $n$. Then $h(n+1) = h(n) + q_n$
is within $C + 4$ of $q_{n+1}$. But the same statement at $n + 1$ puts $h(n+1)$ within $C + 4$ of $q_n$. Those
disagree once $q_{n-1} > 2C + 8$. $\square$
