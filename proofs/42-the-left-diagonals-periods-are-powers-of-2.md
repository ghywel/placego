# The left diagonals' periods are powers of 2 (Jen's Theorem 4, proved again, second-read, machine-checked): every diagonal k ≥ 2 settles with a period dividing 2^(k−2)

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "42. The left diagonals' periods are
powers of 2 (Jen's Theorem 4, proved again, second-read, machine-checked): every diagonal k ≥ 2 settles with a
period dividing 2^(k−2)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved by Local, machine-checked;.

## In plain words

The stripes running down the left edge of a Rule 30 picture each settle into a beat, and every beat is a power of 2.

**What it says.** Number the diagonal stripes from the left edge of the pattern. Each one eventually repeats, and stripe
number k repeats with a period that divides 2 to the power k − 2: 1, 2, 4, 8 and so on, never 3 or 5. Each stripe is
driven by the two stripes beside it, and a stripe driven by two regular beats can at most double their period.

**Why it matters.** The record took this from Jen's 1986 paper, which is still unread; now it rests on the record's own
proof. It also explains the gap sizes seen in the settled band: an odd beat leaves only gaps of one cell.

**An everyday picture.** A row of drummers, each copying the two to their left with one simple rule. However the first
drummers play, each new drummer settles into a beat at most twice as long as the beats feeding them.

**Checked by machine.** A proof assistant (Lean) has checked the argument and its consequences for the gaps.

## The formal statement and proof

*Where:* CHAT-LEDGER L540 .. L543 (2026-10-10); the record map's line on left diagonals (§8.27, §8.30). *Bears on:* the
left band's periods (B2, §8.31), and the run bounds of entries 12 and 13. *Status:* proved by Local, machine-checked;
second-read by Cloud by hand (CL171, the step; CL172, the Lean statements); GPT's full source review is queued (GC961). The record credits the statement to Jen (1986, Theorem 4) and Rowland (§5); Jen's paper is
still unread, so this is the record's own proof, not his.

**Theorem (power-of-2 periods).** Let a configuration have a leftmost black cell $e$ at time 0, and write
$D_k(t)$ for the cell $e - t + k$ at time $t$. For every $j \ge 0$ there is a time $T$ after which every diagonal
$k \le j + 2$ has period $2^j$: $D_k(t + 2^j) = D_k(t)$ for all $t \ge T$.

*Proof.* The diagonals obey $D_k(t+1) = D_{k-2}(t) \oplus (D_{k-1}(t) \lor D_k(t))$, with $D_k \equiv 0$ for $k < 0$.
So $D_0 \equiv 1$, $D_1(t) = 0 \oplus (1 \lor \cdot) = 1$ for $t \ge 1$, and $D_2(t) = 1 \oplus 1 = 0$ for $t \ge 2$:
every $k \le 2$ has period 1 from $t = 2$.

For the step, let $a = D_{k-2}$ and $b = D_{k-1}$ both have period $p$ from time $T$, and put $x = D_k$, so
$x(t+1) = a(t) \oplus (b(t) \lor x(t))$. If $x(s) = x(s + mp)$ for some $s \ge T$, then $x(s + i) = x(s + mp + i)$ for
all $i \ge 0$: the two runs see the same inputs. Two of the three bits $x(T)$, $x(T + p)$, $x(T + 2p)$ are equal.
- If $x(T) = x(T + p)$, the runs from $T$ and $T + p$ agree, so $x(T + 3p) = x(T + 2p) = x(T + p)$.
- If $x(T) = x(T + 2p)$, the runs from $T$ and $T + 2p$ agree, so $x(T + 3p) = x(T + p)$.
- If $x(T + p) = x(T + 2p)$, the runs from $T + p$ and $T + 2p$ agree, so $x(T + 3p) = x(T + 2p) = x(T + p)$.
In each case $x(T + p) = x(T + 3p)$, and the runs from $T + p$ and $T + 3p$ agree: $x$ has period $2p$ from $T + p$.
Diagonals with period $p$ also have period $2p$, so by induction on $j$ every $k \le j + 2$ has period $2^j$. $\square$

**Corollary (run bounds).** With entry 12's sharp form ($M' - g \le 2P - 1$ under agreement at lag $P$):
- from some time on, every white run in the diagonals $\le j + 2$, bounded on the left by a black diagonal, is at most
  $2^{j+1} - 1$ long;
- if those diagonals have period $P$ from some time, the bound is $2\gcd(P, 2^j) - 1$, because two periods of an
  eventually periodic sequence combine to their gcd (Euclid on periods). For odd $P$ the bound is 1.

*Machine-checked (Local, 2026-10-10).* tests/probes/lean/JenPow2.lean: `forced_periodic` (the step), `jen_pow2` (the
theorem), `run_bound` and `run_bound_gcd` (the corollaries), with `per_gcd`. The axioms are propext, Classical.choice
and Quot.sound (`forced_periodic` and `per_gcd` need only propext and Quot.sound); no sorryAx.

*Computed (rule30_jen_pow2.py, JP).* Every seed of support ≤ 12 settles within 65,536 steps, with least periods
1, 1, 1, 2, 1, 2, 2, 1, 4, 1, 4, 4, 4, 4, 4 for $k = 0 .. 14$, the same for every seed. So the bound $2^{k-2}$ is
attained only at $k = 3$. That was already measured: UB (L383, rule30_edge_period_universal.py) found the same
left-edge staircase on 21 rows, $P_e = 4$ for $8 \le e < 29$ (Cloud, CL171). The seed-independence is §8.31's one
generic left side; the theorem does not explain it.
The places where §8.31's left sides can split are exactly where the one-period map of the step is the identity: $b$
eventually white and an even number of black cells in a period of $a$.
