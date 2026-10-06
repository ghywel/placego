# The leftward speed of information is an identity

*Short proofs restated from the running text. Derived from [PROOFS.md](../PROOFS.md), entry "C.4 The leftward speed
of information is an identity (RULE30-PRIZE.md §8.66; 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved (the identity);.

## In plain words

How fast news travels leftwards in Rule 30 is an exact bookkeeping identity: full speed, minus the times it gets
squashed.

**What it says.** Compare two copies of Rule 30 that differ somewhere and watch the leftmost difference. Read along
the diagonals, the difference never moves backwards, and it is held back only when the square just below it on the
diagonal is black. So its average speed equals full speed minus (how often it is held back) times (how far it is set
back each time). The measured numbers, 0.41 and 1.84, give a speed of about a quarter. A diagonal that turns white
for good becomes a barrier: damage that crosses it never heals.

**Why it matters.** It turns a measured speed into an exact identity, and explains why the band of white diagonals
left of the middle acts as a one-way wall for information.

**An everyday picture.** A rumour running down a queue: it moves one person per tick, except when it meets a
sceptic, who knocks it back a few places.

## The formal statement and proof

*Where:* §8.66. *Bears on:* constellation row 3; the band's white diagonals as barriers. *Status:* proved (the identity);
the numbers $0.41$ and $1.84$ are measured.

**Proposition.** Write $D_k(t) = x(k - t, t)$ (diagonal coordinates). Then
$D_k(t+1) = D_{k-2}(t) \oplus (D_{k-1}(t) \vee D_k(t))$ on the whole plane. Consequently, for two configurations differing somewhere, the lowest damaged
diagonal $k_{\min}(t)$ never decreases, it increases at step $t$ only if the undamaged diagonal below it is black
($D_{k_{\min}-1}(t) = 1$), and the leftward speed of the leftmost differing cell, averaged over $[t_1, t_2]$, is
$v = 1 - (\text{number of rises}) \cdot (\text{mean rise}) / (t_2 - t_1) = 1 - P(\text{heal}) \, E[\text{jump} \mid \text{heal}]$.

*Proof.* $x(i, t+1) = x(i-1, t) \oplus (x(i, t) \vee x(i+1, t))$ with $i = k - t - 1$ gives the three parents on
diagonals $k - 2, k - 1, k$. So $D_k(t+1)$ depends on diagonals $\le k$ only: a difference confined to diagonals
$\ge k_{\min}$ stays confined there. If $D_{k_{\min}-1}(t) = 1$ (the same in both copies, being below the damage),
then $D_{k_{\min}}(t+1) = D_{k_{\min}-2}(t) \oplus 1$ is the same in both copies, so $k_{\min}$ rises; if it is 0,
$D_{k_{\min}}(t+1) = D_{k_{\min}-2}(t) \oplus D_{k_{\min}}(t)$ differs, so $k_{\min}$ stays. The leftmost differing
cell is at $x = k_{\min}(t) - t$, whose mean velocity is $(\Delta k_{\min})/\Delta t - 1$; the stated identity is
that average written as (frequency of rises) times (mean rise). $\square$

*Corollary (the band locks).* If diagonal $w$ is eventually white, then from that time
$D_{w+1}(t+1) = D_{w-1}(t) \oplus D_{w+1}(t)$, so a difference on diagonal $w + 1$ is permanent: damage that reaches $w + 1$ never heals.
(Measured: caught with probability exactly one half over the band's phases at $w = 7, 28, 399$.)
