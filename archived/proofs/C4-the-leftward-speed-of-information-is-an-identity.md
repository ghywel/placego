# The leftward speed of information is an identity

*Short proofs restated from the running text. Derived from [PROOFS.md](../PROOFS.md), entry "C.4 The leftward speed
of information is an identity (RULE30-PRIZE.md §8.66; 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved (the identity);.

## In plain words

How fast news travels leftwards in Rule 30 is an exact bookkeeping identity: full speed, minus the times it gets
squashed.

**What it says.** Compare two copies of Rule 30 that initially differ at finitely many cells and watch the leftmost difference. Read along
the diagonals, the difference never moves backwards, and it is held back only when the square just below it on the
diagonal is black. So its average speed equals full speed minus (how often it is held back) times (how far it is set
back each time). The measured numbers, 0.41 and 1.84, give a speed of about a quarter. If the copies agree below and on a diagonal that turns white
for good, a difference immediately above it cannot heal.

**Why it matters.** It turns a measured speed into an exact identity, and explains why the band of white diagonals
left of the middle acts as a one-way wall for information.

**An everyday picture.** A shopper walking down a busy aisle at full pace, knocked back a step or two each time a
trolley cuts across them: their average pace is full pace minus the knocks. A white diagonal is a one-way turnstile:
once through, nobody pushes them back.

## The formal statement and proof

*Where:* §8.66. *Bears on:* constellation row 3; the band's white diagonals as barriers. *Status:* proved (the identity);
the numbers $0.41$ and $1.84$ are measured.

**Proposition.** Write $D_k(t) = x(k - t, t)$ (diagonal coordinates). Then
$D_k(t+1) = D_{k-2}(t) \oplus (D_{k-1}(t) \vee D_k(t))$ on the whole plane. Consequently, for two configurations with a finite, nonempty initial set of differing cells, the lowest damaged
diagonal $k_{\min}(t)$ never decreases, it increases at step $t$ only if the undamaged diagonal below it is black
($D_{k_{\min}-1}(t) = 1$), and the leftward speed of the leftmost differing cell, averaged over $[t_1, t_2]$, is
$v = 1 - (\text{number of rises}) \cdot (\text{mean rise}) / (t_2 - t_1) = 1 - P(\text{heal}) \, E[\text{jump} \mid \text{heal}]$.

*Proof.* $x(i, t+1) = x(i-1, t) \oplus (x(i, t) \vee x(i+1, t))$ with $i = k - t - 1$ gives the three parents on
diagonals $k - 2, k - 1, k$. So $D_k(t+1)$ depends on diagonals $\le k$ only: a difference confined to diagonals
$\ge k_{\min}$ stays confined there. If $D_{k_{\min}-1}(t) = 1$ (the same in both copies, being below the damage),
then $D_{k_{\min}}(t+1) = D_{k_{\min}-2}(t) \oplus 1$ is the same in both copies, so $k_{\min}$ rises; if it is 0,
$D_{k_{\min}}(t+1) = D_{k_{\min}-2}(t) \oplus D_{k_{\min}}(t)$ differs, so $k_{\min}$ stays. The leftmost differing
cell is at $x = k_{\min}(t) - t$, whose mean velocity is $(\Delta k_{\min})/\Delta t - 1$; the stated identity is
that average written as (frequency of rises) times (mean rise); if there are no rises, the product is defined to be zero. The differing set remains finite by the finite propagation cone and remains nonempty: at the cell one place right of the rightmost difference, the left parent differs while the other two parents agree, so its next value differs. Thus the front exists at every finite time. $\square$

*Corollary (the band locks).* Suppose both copies agree on every diagonal at or below $w$, and their common diagonal $w$ is eventually white. Then from that time
$D_{w+1}(t+1) = D_{w-1}(t) \oplus D_{w+1}(t)$, so a difference on diagonal $w + 1$ is permanent: damage that reaches $w + 1$ never heals.
(Measured: caught with probability exactly one half over the band's phases at $w = 7, 28, 399$.)

*Second reader's correction (GPT, 2026-10-07, R3/GC295).* The original wording allowed any two differing configurations; a leftmost difference need not exist, and even an initially existing front can disappear. Explicit one-step coalescing rows and a barrier countercontrol are recorded in R3. The finite-perturbation hypothesis above is sufficient; more generally the speed identity holds on any interval where a nonempty damage set with a minimum survives. Agreement below the barrier is essential for the corollary, because incoming differences can change its XOR forcing. The reported single-flip measurements are within the repaired scope and were not rerun.

*Author's check of the correction (Local, 2026-10-07; chat L186).* The repair is right and the original wording was
too broad. GPT's two rows (black through site 0 then white; black except site 0) differ on an infinite set with a
minimum, and both become one black cell at site 1 after a step, so a front need not survive. For a finite perturbation
it does: one place right of the rightmost difference, only the left parent differs, so the difference moves right and
never dies. On the corollary, in the proposition's own setting (damage reaching $w + 1$, so $k_{\min} = w + 1$) the
agreement below $w$ is automatic, since $k_{\min}$ is the lowest damaged diagonal. The added hypothesis makes it
explicit, and the countercontrol shows it cannot be dropped once differences exist below. Checked
(`rule30_audit_g99_g100.py`, S103):
- The diagonal recursion holds on random rows.
- GPT's coalescing pair coalesces as stated.
- On 300 finite perturbations the damage never vanishes, $k_{\min}$ never falls and rises only over a black
  diagonal, and the rises telescope.
- The barrier recursion locks with agreement below and heals at once without it.
