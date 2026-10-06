# PROOFS.md: the solid proofs of this record, in one place

*Started 2026-10-06 11:15 BST at the owner's instruction: "Solid, concrete proofs that don't outright solve the
prize are extremely valuable and should be stored in their own PROOFS.md document." Each entry is a statement with
a proof a reader can check from the page, or a certificate committed in this repository, copied verbatim from
where it was first recorded (named under* Where*), with what it bears on and its status. Nothing here solves the
prize; everything here is exact. Entries are appended, never rewritten; a correction is a new line under the entry
that names what was wrong. Claims that still want a second reader are kept apart at the end, so that the word
"proved" keeps its meaning.*

*Reading order for a newcomer: A (the wall form) then B (windows and zero runs), which together are what is known
about Conjecture LR and Conjecture B (PERIOD-TWO.md §5, §7); B′ is the siblings, Jen and the squeeze; C is the exact
statements about the single cell proved in the last two days; E is GPT's; F is Collatz; G is the waiting room.*

## A. The wall form

### 1. Lemma 1 (where column 1 is invisible)

*Where:* RULE30-PRIZE.md, "7. Rung 2, first progress: left-side rigidity (2026-10-04)". *Bears on:* the wall form: column 1 is visible only at white times; every statement about injection rates rests on it. *Status:* proved.

**Lemma 1 (where column 1 is invisible).** With column 0's trace $\tau$ fixed, the forced left half depends on column
1 only at the times $t$ with $\tau(t) = 0$.

*Proof.* The only place column 1 enters is
$x_t(-1) = \tau(t+1) + \big(\tau(t) \vee x_t(1)\big) \bmod 2$. Where $\tau(t) = 1$, the "or" is 1 whatever $x_t(1)$
is. Every further left column is built from columns $-1$ and $0$ and those to their left. $\square$

### 2. Lemma 2 (rotations are equivalent)

*Where:* RULE30-PRIZE.md, "7. Rung 2, first progress: left-side rigidity (2026-10-04)". *Bears on:* the wall form: one rotation of a periodic word per class suffices. *Status:* proved.

**Lemma 2 (rotations are equivalent).** A finite configuration whose column is exactly periodic from $t = 0$, with
word $w$, is still finite one step later, and its column is then periodic with $w$ rotated by one place. So a finite
configuration exists for one rotation of a cyclic word exactly when it exists for all of them, and ruling out one
rotation per class is enough. $\square$

### 3. Lemma 3 (two local rules from the right side)

*Where:* RULE30-PRIZE.md, "8. The right side as a complement (2026-10-04)". *Bears on:* the right side as a constraint on column 1 (two local rules). *Status:* proved; checked on random sequences.

**Lemma 3 (two local rules from the right side).** At column 1, Rule 30 reads
$\sigma(t+1) = \tau(t) + \big(\sigma(t) \vee x_t(2)\big) \bmod 2$, where $\tau$ is column 0 and $\sigma$ is column 1.
So, whatever column 2 does:

```math
\tau(t) = 0:\quad \sigma(t) = 1 \;\Rightarrow\; \sigma(t+1) = 1, \qquad\qquad
\tau(t) = 1:\quad \sigma(t+1) = 1 \;\Rightarrow\; \sigma(t) = 0 .
```

For the alternating trace, this means the part of column 1 that the left side sees, $e(s)$, never has two ones in a
row. $\square$ *Checked:* `rule30_twosided.py` T1 and T2 (every right half tried; random sequences violate the rules,

### 4. Lemma 4 (the newest bit of column 1 enters once, as an XOR)

*Where:* RULE30-PRIZE.md, "8.2 Why runs of 13 were missing: templates, and where Fibonacci really is (2026-10-04)". *Bears on:* the counting form: the newest visible bit enters once, as an XOR. *Status:* proved; checked (P2).

**Lemma 4 (the newest bit of column 1 enters once, as an XOR).** Write $L(k)$ for the cell at depth $k$ of the
forced left half (column $-k$ at time 0). It depends on $\sigma(0), \dots, \sigma(k-1)$ only, and on the newest of
them like this:

```math
L(k) = \begin{cases}
\sigma(k-1) \oplus g_k\big(\sigma(0), \dots, \sigma(k-2)\big) & \text{if } \tau(k-1) = 0 \quad \text{(a linear cell)},\\[2pt]
h_k\big(\sigma(0), \dots, \sigma(k-2)\big) & \text{if } \tau(k-1) = 1 \quad \text{(a forced cell)}.
\end{cases}
```

*Proof.* Rule 30 run to the left is $x(i-1, t) = x(i, t+1) \oplus \big(x(i, t) \vee x(i+1, t)\big)$. By induction,
column $-m$ at time $t$ depends on $\sigma(t), \dots, \sigma(t+m-1)$, and the newest of these enters only through
the term $x(-m+1, t+1)$, as an XOR. Unwinding $L(k) = x(-k, 0)$ this way down to column $-1$ at time $k-1$ leaves
$x(-1, k-1) = \tau(k) \oplus \big(\tau(k-1) \vee \sigma(k-1)\big)$. That is $\tau(k) \oplus \sigma(k-1)$ when
$\tau(k-1) = 0$, and it does not involve $\sigma(k-1)$ when $\tau(k-1) = 1$. $\square$ *Checked:* P2 in


## B. Windows, zero runs and the left band

### 5. Theorem A (a window cannot outlast the edge)

*Where:* RULE30-PRIZE.md, "8.54 Jen's theorem with a clock: a window of periodicity cannot outlast the left edge (2026-10-05)". *Bears on:* question 2 of PERIOD-TWO.md §7: a window of periodicity cannot outlast the left edge (Jen with a clock). *Status:* proved.

**Theorem A (a window cannot outlast the edge).** Take a nonzero configuration whose leftmost black cell at time 0
is $L \ge 0$ cells to the left of column $i$. If columns $i$ and $i + 1$ are $P$-periodic on $[a, b]$, then

```math
b \le 2a + L + 2P - 1 .
```

At time $a$ the left edge is $L + a$ cells away. So the window's length $b - a$ is less than that distance plus $2P$.

*Proof.* Three facts, each one line of Rule 30.
1. **Periodicity moves left and loses one step.** $x_t(k-1) = x_{t+1}(k) \oplus (x_t(k) \vee x_t(k+1))$. So if columns
   $k$ and $k+1$ are $P$-periodic on $[a, b]$, column $k - 1$ is $P$-periodic on $[a, b - 1]$. After $j$ steps to the
   left, column $i - j$ is $P$-periodic on $[a, b - j]$.
2. **The edge moves left one cell a step.** The leftmost black cell has two white cells to its left, and $001 \to 1$.
   So column $i - j$ is white before time $j - L$ and black at time $j - L$ (for $j \ge L$).
3. **The two meet.** Take $j = a + P + L$. Column $i - j$ turns black for the first time at $e = a + P$. If
   $b \ge 2a + L + 2P$, then $e \le b - j$. So both $e - P = a$ and $e$ lie in the window where column $i - j$ is
   $P$-periodic. It is white at one and black at the other, a contradiction. $\square$

### 6. Theorem B (a zero run cannot outlast two periods)

*Where:* RULE30-PRIZE.md, "8.54 Jen's theorem with a clock: a window of periodicity cannot outlast the left edge (2026-10-05)". *Bears on:* question 2: a zero run in row 0 of the forced left half is at most two periods long. *Status:* proved; sharp at q = 2.

**Theorem B (a zero run cannot outlast two periods).** Let columns 0 and 1 be $P$-periodic from time 0, with
$P \ge 2$ and column 0 not zero. Then every run of zeros in row 0 of the forced left half has length at most
$2P - 2$. (For $P = 1$ the same proof gives 1, which is attained by the stripes $0101\dots$ in space.)

*Proof.* Every column of the left half is $P$-periodic (fact 1, with an unbounded window). Let row 0 be zero at
depths $d$ to $d + R - 1$. A cell is white when the three cells above it are. So column $-k$ is white at times 0 to
$\min(k - d,\ d + R - 1 - k)$, which is a triangle of zeros under the run. If $R \ge 2P - 1$, the column at
$k = d + P - 1$ is white for $P$ steps in a row, and so for ever. With column $-k$ zero, the rule for the column to
its right reads $x_{t+1}(-k+1) = x_t(-k+1) \vee x_t(-k+2)$. That column never turns from black to white. It is
periodic, so it is constant. Its depth $d + P - 2$ lies in the run because $P \ge 2$, so it is white at time 0, and
zero for ever. Two adjacent zero columns force zeros to
the right, as in §8.13, as far as column 0, which is not zero. $\square$

### 7. Theorem A′ (a block recurs only if it is no longer than the edge is far)

*Where:* RULE30-PRIZE.md, "8.58 The window principle: Theorem A′, and what the Collatz twin shows is missing (2026-10-05)". *Bears on:* the window principle: a block recurs only if it is no longer than the edge is far. *Status:* proved.

**Theorem A′ (a block recurs only if it is no longer than the edge is far).** Take a nonzero configuration whose
leftmost black cell at time 0 is $L \ge 0$ cells to the left of column $i$. If the pair of columns $(i, i+1)$
shows the same block of $n$ consecutive values starting at times $a$ and $a' > a$, then

```math
n \le L + a' .
```

*Proof.* Rule 30 read from right to left gives each cell from the cell to its right one step later and two cells
of its own time. So the two columns at times $t$ to $t + k$ fix the $k$ cells to their left at time $t$. Equal
blocks of length $n$ therefore make the rows at times $a$ and $a'$ agree at the $n - 1$ cells left of column
$i$. The later row has its leftmost black cell $L + a'$ cells out, and the earlier row is white there. If
$L + a' \le n - 1$ the rows disagree inside the range where they must agree. $\square$

### 8. Lemma B1 (white, then black)

*Where:* RULE30-PRIZE.md, "8.59 The window principle meets the band of stripes: a repeat is a white run, and the left side is never white for long (2026-10-05)". *Bears on:* the left band: an eventually white diagonal is preceded by an eventually black one. *Status:* proved.

**Lemma B1 (white, then black).** If diagonal $j$ is eventually white, diagonal $j + 2$ is eventually black. No two
adjacent diagonals are both eventually white. A diagonal other than 0 and 1 is eventually black only if the one two
before it is eventually white.

*Proof.* Once $D_j \equiv 0$, $D_{j+2}(t+1) = D_{j+1}(t) \lor D_{j+2}(t)$, which never falls, so $D_{j+2}$ is eventually
constant, and it is 1 unless $D_{j+1} \equiv D_{j+2} \equiv 0$ as well. If $D_j \equiv D_{j+1} \equiv 0$ then
$D_{j+1}(t+1) = D_{j-1}(t) \oplus (D_j \lor D_{j+1}) = D_{j-1}(t)$ forces $D_{j-1} \equiv 0$, and so on down to
$D_0 \equiv 0$, which is false ($D_0 \equiv 1$). That proves the first two claims. For the third: if $D_k \equiv 1$
then $D_k(t+1) = D_{k-2}(t) \oplus 1$ forces $D_{k-2} \equiv 0$. $\square$

### 9. Lemma B2 (the clock never stops)

*Where:* RULE30-PRIZE.md, "8.59 The window principle meets the band of stripes: a repeat is a white run, and the left side is never white for long (2026-10-05)". *Bears on:* the left band: the diagonal periods double without end (Rowland's mechanism, proved). *Status:* proved.

**Lemma B2 (the clock never stops).** The eventual periods of the diagonals are unbounded. So there are infinitely
many eventually white diagonals, and infinitely many eventually black ones.

*Proof.* Suppose every diagonal had eventual period dividing $P$. Write $V_k \in \{0,1\}^{\mathbb{Z}/P}$ for the
periodic regime of diagonal $k$, indexed by time modulo $P$, so that $V_k(s+1) = V_{k-2}(s) \oplus (V_{k-1}(s) \lor V_k(s))$
for every $k \ge 0$, with $V_{-1} = V_{-2} = 0$. The pairs $(V_{k-1}, V_k)$ take finitely many values, so
$(V_{k_1 - 1}, V_{k_1}) = (V_{k_2 - 1}, V_{k_2})$ for some $k_1 < k_2$. The recurrence can be read backwards,
$V_{k-2}(s) = V_k(s+1) \oplus (V_{k-1}(s) \lor V_k(s))$, so $V_{k_1 - j} = V_{k_2 - j}$ for every $j \ge 0$, and the
backward reading continues into the negative indices, where everything is 0. With $q = k_2 - k_1$ this gives
$V_0 = V_{-q} = 0$, against $V_0 \equiv 1$. So the periods are unbounded. A diagonal's period exceeds the periods
of the two before it only when the one before it is eventually white: otherwise a time with $D_{k-1}(t) = 1$ resets
$D_k(t+1) = \lnot D_{k-2}(t)$, after which $D_k$ follows its inputs' period. Infinitely many doublings need infinitely
many eventually white diagonals, and Lemma B1 turns each into an eventually black one. $\square$

### 10. Theorem A‴ (the window principle, with the band)

*Where:* RULE30-PRIZE.md, "8.59 The window principle meets the band of stripes: a repeat is a white run, and the left side is never white for long (2026-10-05)". *Bears on:* the window principle with the band. *Status:* proved.

**Theorem A‴ (the window principle, with the band).** Let the leftmost black cell at time 0 be $L$ cells left of
column $i$, and let the pair of columns $(i, i+1)$ show the same block of $n$ values from the times $a$ and $a' > a$.
Then row $a'$ is white on its diagonals $L + a' - n + 1$ to $a' - a - 1$. Hence, if diagonal $b$ is black at time $a'$
and $b < a' - a$, then $n \le L + a' - b$.

*Proof.* By §8.58 the rows at $a$ and $a'$ agree on the $n - 1$ cells left of column $i$. Row $a$ is white beyond
distance $L + a$, so row $a'$ is white at the distances $L + a + 1$ to $n - 1$. Its leftmost black cell is at distance
$L + a'$, so those distances are its diagonals $L + a' - n + 1$ to $a' - a - 1$. A black diagonal $b$ in that range
contradicts this; so either $b \ge a' - a$ or $b \le L + a' - n$. $\square$

### 11. Corollary F (near-squares at the start are fatal)

*Where:* RULE30-PRIZE.md, "8.59 The window principle meets the band of stripes: a repeat is a white run, and the left side is never white for long (2026-10-05)". *Bears on:* near-squares at the start are fatal. *Status:* proved.

**Corollary F (near-squares at the start are fatal).** Let $c$ be the visible bits of column 1, and write
$\ell(i, i')$ for the length of the common future of $c$ at the indices $i < i'$. If there is a constant $K$ and pairs
$i_j < i'_j$ with $i'_j - i_j \to \infty$ and $\ell(i_j, i'_j) \ge i'_j - K$, then the forced left half is never finite.
In words: a column 1 that starts with a square, or misses one by a bounded amount, at larger and larger periods,
is excluded, with any left half.

*Proof.* Suppose the left half were finite, its leftmost black cell at depth $L$. By Lemma B2 there is an eventually
black diagonal $b \ge L + 2K$, black from some time $t_b$. The pair of columns $(-1, 0)$ repeats its block of length
$2\ell$ from the times $2i_j$ and $2i'_j$ (column 0 is periodic and column $-1$ at the odd times is constant). Take
$j$ with $2(i'_j - i_j) > b$ and $2i'_j \ge t_b$. Theorem A‴ with the distance $L - 1$ to column $-1$ gives
$2\ell \le L - 1 + 2i'_j - b \le 2i'_j - 2K - 1$, against $\ell \ge i'_j - K$. $\square$

### 12. Lemma B3 (the settled band has no long white run)

*Where:* RULE30-PRIZE.md, "8.59 The window principle meets the band of stripes: a repeat is a white run, and the left side is never white for long (2026-10-05)". *Bears on:* the settled band has no long white run. *Status:* proved.

**Lemma B3 (the settled band has no long white run).** Suppose that at time $t$ the diagonals $0$ to $M$ have been
in their periodic regime, with a common period $P$, for at least $P$ steps. Then no white run of the row inside
diagonals $0$ to $M$ is longer than $2P$.

*Proof.* Let the row be white on $[g+1, M']$ with $M' \le M$ and $D_g(t) = 1$ (diagonals 0 and 1 are black, so such a
$g \ge 1$ exists). One step back, the constraint $D_{k-2} = D_{k-1} \lor D_k$ for $k \in [g+1, M']$ leaves two cases:
either the row at $t - 1$ is white on $[g-1, M']$ with $D_{g-2}(t-1) = 1$ (the run is older and two cells wider),
or it is black on $[g-1, M'-2]$ (the run is born here, under a black run). Repeating, the run is older for $s_0$
steps and born at time $t - s_0 - 1$. At time $t - P$ the row is the same as at $t$, white exactly from $g+1$, so
$s_0 < P$. Forward from time $t - P$, a white run only loses two cells a step at its edge side:
$D_k(\tau+1) = 0$ whenever $k-2$, $k-1$, $k$ are all white. So at time $t - s_0 - 1$ the row is white on
$[g + 1 + 2(P - s_0 - 1), M']$ and black on $[g - 2s_0 - 1, M' - 2]$. The two ranges are disjoint only if
$M' - g \le 2P - 2s_0 \le 2P$. $\square$

### 13. Theorem A⁗ (a repeat's white run cannot lie in the settled band)

*Where:* RULE30-PRIZE.md, "8.59 The window principle meets the band of stripes: a repeat is a white run, and the left side is never white for long (2026-10-05)". *Bears on:* a repeat's white run cannot lie in the settled band. *Status:* proved.

**Theorem A⁗ (a repeat's white run cannot lie in the settled band).** In the setting of Theorem A‴, if the diagonals
$0$ to $M$ are settled in the sense of Lemma B3 at time $a'$ and $M < a' - a$, then $n \le L + a' - M + 2P$.

*Proof.* The white run of Theorem A‴ covers $[L + a' - n + 1, a' - a - 1] \supseteq [L + a' - n + 1, M]$, which lies in
the settled band, so by Lemma B3 its length $M - (L + a' - n)$ is at most $2P$. $\square$

### 14. Theorem E

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

### 15. Theorem E″ (any arcs, for a typical rotation number; added the same night)

*Where:* RULE30-PRIZE.md, "8.57 No pure rotation works: every Sturmian column 1 is excluded (2026-10-05)". *Bears on:* the same for any arcs and a typical rotation number. *Status:* proved.

**Theorem E″ (any arcs, for a typical rotation number; added the same night).** Let $c_s = f(\theta + s\alpha)$,
where $f$ is 1 on a finite union of arcs with $r$ end points in all, and 0 elsewhere. If $\alpha$ has infinitely
many partial quotients larger than $2^{r+1}$, the forced left half is not eventually zero, for every $\theta$.
Almost every $\alpha$ has unbounded partial quotients, so for almost every rotation number **no coding by arcs at
all** can go with a finite left half. These sequences have complexity up to $r\,n$.

*Proof.* $c$ breaks period $q_n$ at time $s$ exactly when $x_s$ lies in one of $r$ arcs of length $|\delta_n|$, one at
each end point. Let $d_1 < d_2 < \dots$ be the break times. Step 0 on the stretch before $d_1$ and on each stretch
between consecutive breaks gives $d_1 \le q_n + C + 1$ and $d_{k+1} \le 2 d_k + q_n + C + 3$, so
$d_k < 2^k (q_n + C + 2)$. Two of the first $r + 1$ breaks belong to the same end point, and returns to an arc of
length $|\delta_n|$ are at least $q_{n+1}$ apart. So $q_{n+1} \le d_{r+1} < 2^{r+1}(q_n + C + 2)$, which fails
when $a_{n+1} > 2^{r+1}$ and $q_n$ is large. $\square$


## B′. Siblings, Jen, the squeeze and one certified computation

### 16. Proposition 5 (Rule 90 has no finite configuration with a period-two column)

*Where:* RULE30-PRIZE.md, "8.3 What was already known, Rule 30's siblings, and the owner's harmonics (2026-10-04)". *Bears on:* the siblings: Rule 90 has no finite configuration with a period-two column. *Status:* proved.

**Proposition 5 (Rule 90 has no finite configuration with a period-two column).** Under Rule 90, $x' = l \oplus r$,
let a finite row have its support in $[-w, w]$. Then column 0 is 0 at time $2^n$ and at time $2^n + 1$ whenever
$2^n > w + 1$.

*Proof.* Rule 90 is linear, and a single 1 at position $j$ reaches $(0, t)$ with the value
$\binom{t}{(t-j)/2} \bmod 2$. By Lucas' theorem, $\binom{2^n}{k}$ is odd only for $k \in \{0, 2^n\}$, and
$\binom{2^n+1}{k}$ only for $k \in \{0, 1, 2^n, 2^n+1\}$. These need $|j| \in \{2^n - 1, 2^n, 2^n + 1\}$, outside the
support. $\square$

### 17. Proposition 7 (Jen)

*Where:* RULE30-PRIZE.md, "8.13 Jen's theorem settles every periodic column 1: a correction (2026-10-05)". *Bears on:* Jen's theorem in the form the record uses (every periodic column 1 is settled). *Status:* proved (Jen 1986, restated with proof).

**Proposition 7 (Jen).** Let column 0 be eventually periodic and not eventually zero, and let column 1 be any
eventually periodic sequence, made by a right half or not. Then the forced left half is never eventually zero.

*Proof.* Shift time so that both columns are exactly periodic from $t = 0$, with a common period $P$. (The row at the
new $t = 0$ still has an eventually zero left half, because the zeros far to the left stay zero for any finite time.)
Rule 30 read from right to left is

```math
x_t(k-1) = x_{t+1}(k) \oplus \big(x_t(k) \vee x_t(k+1)\big) .
```

1. **Periodicity moves left.** If columns $k$ and $k+1$ are $P$-periodic, the formula makes column $k - 1$
   $P$-periodic. Starting from columns 0 and 1, every column of the left half is $P$-periodic.
2. **Zeros stay zero for a while.** Suppose $x_0(k) = 0$ for every $k < -N$. A cell is 0 when all three cells above
   it are, so $x_t(k) = 0$ whenever $k < -N - t$. A column far enough left, $k < -N - P$, is therefore zero for
   $t = 0, \dots, P - 1$, and by step 1 it is zero for ever. So two adjacent columns are both zero for ever.
3. **Zeros move right.** If columns $k - 1$ and $k$ are both zero for ever, the formula reads
   $0 = 0 \oplus (0 \vee x_t(k+1))$, so column $k + 1$ is zero for ever too. Repeating, column 0 is zero, which it is
   not. $\square$

### 18. Theorem (the parity invariant)

*Where:* RULE30-PRIZE.md, "8.65 Rule 210, the one sibling: conjecture LR is false there (2026-10-06)". *Bears on:* Rule 210 next to 0101: the forced left half is Rule 90's (so LR fails there by linearity plus GPT's witness). *Status:* proved.

**Theorem (the parity invariant).** With column 0 equal to 0101... ($x(0, t) = t \bmod 2$) and any column 1, every
black cell $(-m, t)$ of Rule 210's forced left half has $t + m$ odd, and the forced left half is exactly Rule 90's:
$x(-m, t) = x(-m+1, t+1) \oplus x(-m+2, t)$.

*Proof.* Column 0 is black at odd $t$, parity $t + 0$ odd. Column $-1$: $x(-1, t) = \tau(t+1) \oplus (\lnot \tau(t) \land \sigma(t))$
is $1 \oplus \sigma(t)$ at even $t$ (parity $t + 1$ odd) and $0$ at odd $t$. Induction on $m$: the inverse rule is
$x(-m, t) = x(-m+1, t+1) \oplus (\lnot x(-m+1, t) \land x(-m+2, t))$, and the cells $(-m+1, t)$ and $(-m+2, t)$ have
parities $t + m - 1$ and $t + m$, so by the invariant they are never both black: when $x(-m+2, t) = 1$ its neighbour is
white and the AND-NOT equals $x(-m+2, t)$; when it is 0 the term is 0. So the term is $x(-m+2, t)$ in every case,
the rule is Rule 90's inverse, and $x(-m, t) = 1$ needs one of $(-m+1, t+1)$, $(-m+2, t)$ black, both of parity $t + m$,
so $t + m$ is odd. $\square$

### 19. Lemma (the squeeze)

*Where:* RULE30-PRIZE.md, "8.33 The entropy squeeze: a period-2 counterexample must be almost frozen (2026-10-05)". *Bears on:* the entropy squeeze: a period-2 counterexample must carry a certified minimum of information per step. *Status:* proved (the lemma); the constant 0.0618 bits/step is a certified computation (§8.20, §8.33).

**Lemma (the squeeze).** Let $x$ be any configuration of Rule 30 whose column 0 is $0101\ldots$ from time 0. Then
every column to the left of column 0 has

```math
h(\text{column } {-k}) \;\le\; \tfrac12 \log_2 \lambda_{26} \;\le\; 0.0646 \text{ bits per step}, \qquad k = 1, 2, \ldots
```

and at most $4 \times 320{,}528 \times 2^{0.1292 \lceil j/2 \rceil}$ different patterns of width $j$ ever appear just left
of column 0, the same bound for every such configuration. (In fact column −1's entropy is exactly half that of
column 1's visible bits, whose bound is the certified $\log_2 \lambda_{26}' = 0.1292$.)

*2026-10-06, Local.* The certificate now reaches $m = 28$ (`rule30_squeeze.py 27,28 mmap`, SQ6; the pool mapped on the
NVMe as in §8.20's note): $\log_2 \lambda_{27}' = 0.1243$ and $\log_2 \lambda_{28}' = 0.1236$, each checked in exact
rational arithmetic, a bound $10^{-3}$ below $\lambda$ rejected at each. So the lemma holds with **0.0618 bits per step**
in place of 0.0646, and the pattern bound with $2^{0.1236 \lceil j/2 \rceil}$ and the constant 135,663 in place of
320,528. Every sentence below that uses 0.0646 stands with 0.0618.

*Proof.*
1. **Column 1 is a narrow channel.** By §8.20, every stretch of $n$ visible bits of column 1 (the even times)
   lies in the language $L_{26}$ of a 26-cell layer. Restarting the configuration at any even time gives another
   configuration with the same column 0, so this holds for every stretch, not only the first. Hence
   $p_v(n) \le |L_{26}(n)| \le 320{,}528 \times 2^{0.1292\,n}$.
2. **Column −1 is column 1 turned over.** The rule at column 0 reads
   $x_t(-1) = x_{t+1}(0) \oplus (x_t(0) \lor x_t(1))$. So $x_t(-1) = 1$ at odd $t$, and
   $x_t(-1) = \lnot x_t(1)$ at even $t$. A stretch of column −1 is fixed by its starting parity and half as many
   visible bits, so $h(\text{column} -1) \le \tfrac12 h(v)$.
3. **Entropy cannot grow leftwards.** Rule 30 is left-permutive:
   $x_t(j-2) = x_{t+1}(j-1) \oplus (x_t(j-1) \lor x_t(j))$. Each pair of neighbouring columns is computed from the
   pair to its right over two consecutive times, and a computed sequence has no more entropy than what it is computed
   from. Column 0 is periodic and adds nothing.
4. **Patterns.** A width-$j$ pattern just left of column 0 is computed from columns −1 and 0 over $j$ consecutive
   times. $\square$

### 20. Proposition 6 (computed): the pure wheel cannot make a finite left half

*Where:* RULE30-PRIZE.md, "8.6 Order in, noise out: the left side churns the wheel (2026-10-04)". *Bears on:* the pure wheel cannot make a finite left half. *Status:* certified by computation (the script named in the section).

**Proposition 6 (computed): the pure wheel cannot make a finite left half.** Let column 0 be 0101… and column 1 the
universal wheel $U$, at any of its 28 even phases. Then the forced left half is never eventually zero. The orbit of the
column pair enters a cycle after

```math
\mu = 32\,896\,298 \text{ steps}, \qquad \lambda = 15\,009\,104\,432 = 2^4 \cdot 7 \cdot 17 \cdot 1433 \cdot 5501 ,
```

and the cycle is not the zero fixed point. So the left half is eventually periodic in depth, with period dividing
$\lambda$, and it has infinitely many ones.

*Proof.* The certificate $(\mu, \lambda)$ was found by Brent's algorithm in about $4.7 \times 10^{10}$ steps per phase
(O1 and O2 held). It was then re-checked independently by plain stepping:
- the state after $\mu$ steps is not zero, and $\lambda$ further steps return to it;
- $\lambda / p$ steps do not return, for each prime $p$ of $\lambda$, so $\lambda$ is the exact period;
- the state after $\mu - 1$ steps is not on the cycle, so $\mu$ is minimal.

The verifier rejects false certificates (its counterfactuals). Every phase gives the same certificate, for a reason:
$F$ commutes with the rotation of time, which is a permutation of bits, and a rotation by 2 fixes the trace and moves
the wheel's phase by 2. So the 28 orbits are rotations of one, and one certificate settles them all. All 28 were run
anyway and agree. $\square$


## C. Short proofs recorded without a theorem heading (restated here with their proofs)

These were proved inside sections as running text. They are restated so that each is a checkable unit.

### C.1 The checkerboard lemma (RULE30-PRIZE.md §8.62, §8.63; 2026-10-06)

*Where:* §8.62 and §8.63 item 2. *Bears on:* the wall form next to black stretches; GPT's G18 builds on it. *Status:* proved.

**Lemma.** Let column 0 carry the periodic word $\tau$ and let $\tau(t), \tau(t+1), \ldots, \tau(t+k)$ all be black. Then
in the forced left half $x(-j, t) = (j + 1) \bmod 2$ for $1 \le j \le k$, whatever column 1 is.

*Proof.* The inverse rule is $x(-j, t) = x(-j+1, t+1) \oplus \big(x(-j+1, t) \vee x(-j+2, t)\big)$. For $j = 1$:
$x(-1, t) = \tau(t+1) \oplus (\tau(t) \vee x(1, t)) = 1 \oplus 1 = 0$ since $\tau(t) = \tau(t+1) = 1$. Suppose the claim
holds for $j - 1$ at every time $t'$ with $\tau(t'), \ldots, \tau(t' + k - j + 1)$ black (so in particular at $t$ and
$t + 1$ when $j \le k$). Then $x(-j+1, t+1) = j \bmod 2$ and $x(-j+1, t) = j \bmod 2$, and $x(-j+2, t) = (j - 1) \bmod 2$
(for $j = 2$ this is $\tau(t) = 1$). One of $x(-j+1, t)$ and $x(-j+2, t)$ is black, so the OR is 1 and
$x(-j, t) = (j \bmod 2) \oplus 1 = (j + 1) \bmod 2$. $\square$

### C.2 The latch (RULE30-PRIZE.md §8.62; 2026-10-06)

*Where:* §8.62, the white Condrey end. *Bears on:* Conjecture B next to white stretches; the slow walls (§8.63). *Status:* proved.

**Lemma.** If column 0 is white at time $t$, then $x_{t+1}(1) = x_t(1) \vee x_t(2)$. Hence across a white stretch of
the wall column 1 is non-decreasing: once black it stays black until the stretch ends.

*Proof.* Rule 30 at column 1 reads $x_{t+1}(1) = x_t(0) \oplus (x_t(1) \vee x_t(2))$, and $x_t(0) = 0$. $\square$

### C.3 The shrink theorem for white triangles (RULE30-PRIZE.md §8.18; 2026-10-05)

*Where:* §8.18; checked on 1,005,083 runs by `rule30_triangles.py` (0 exceptions; Rule 110 breaks it). *Bears on:* the
triangle census (§8.68); the zero runs of the ladder are the bases of such triangles. *Status:* proved.

**Theorem.** In Rule 30 a maximal run of $n \ge 2$ white cells $[a, b]$, bounded by black cells, becomes exactly the run
$[a + 1, b - 1]$ one step later. So every white triangle is an exact isosceles triangle, fixed by its birth row,
column and width.

*Proof.* $x'(a) = x(a-1) \oplus (x(a) \vee x(a+1)) = 1 \oplus (0 \vee 0) = 1$ since $x(a-1) = 1$ and $n \ge 2$;
$x'(b) = x(b-1) \oplus (x(b) \vee x(b+1)) = 0 \oplus (0 \vee 1) = 1$; every cell strictly inside has three white
parents and $000 \to 0$; and $x'(a+1), \ldots, x'(b-1)$ are bounded by the two black cells just produced. $\square$

### C.4 The leftward speed of information is an identity (RULE30-PRIZE.md §8.66; 2026-10-06)

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

### C.5 The triangle law of the uniform measure (RULE30-PRIZE.md §8.68; 2026-10-06)

*Where:* §8.68; matched on a random row to $0.006\%$ and on the single cell's core right of $x/t = -0.24$ to about
$0.05\%$. *Bears on:* Problem 2's kind of statement; where the single cell's randomness lives. *Status:* proved for
the measure; the single cell's agreement is measured.

**Proposition.** Under the uniform Bernoulli measure on $\{0,1\}^{\mathbb Z}$, which Rule 30 preserves, the density
per cell of tops of white triangles of width $L \ge 1$ (a maximal white run of length $L$ whose cells above, one
wider on each side, are not all white) is $3 \cdot 2^{-(L+4)}$.

*Proof.* Rule 30 is left-permutive ($x' = l \oplus (c \vee r)$ is a bijection in $l$), hence surjective, and a
cellular automaton preserves the uniform measure if and only if it is surjective; so the row at time $t$ is
i.i.d. fair whenever the row at time $t - 1$ is. A maximal white run exactly on $[i, j]$ ($L = j - i + 1$) has
probability $2^{-(L+2)}$ (white inside, black at $i - 1$ and $j + 1$). It is a continuation exactly when the row
above is white on $[i-1, j+1]$ and black at $i - 2$ and $j + 2$: white on $[i-1, j+1]$ makes $[i, j]$ white below
($000 \to 0$), black at $i-2$ makes cell $i - 1$ black below ($100 \to 1$), black at $j+2$ makes cell $j + 1$ black
below ($001 \to 1$), and conversely a run exactly $[i, j]$ below a white stretch $[i-1, j+1]$ forces those two black
cells. That event has probability $2^{-(L+4)}$ in the i.i.d. row above. So the density of tops is
$2^{-(L+2)} - 2^{-(L+4)} = 3 \cdot 2^{-(L+4)}$. $\square$

### C.6 Gliders on prime rings (RULE30-PRIZE.md §8.67; 2026-10-06)

*Where:* §8.67; the census `ring_census.c` to $n = 24$. *Bears on:* constellation row 10 ("which parts are proved").
*Status:* proved (the pigeonhole); the distinctness of lengths at $n = 13, 17, 19, 23$ is the census's exact finding.

**Proposition.** Let $p$ be prime and consider Rule 30 on the ring of $p$ cells. Rotation by one cell commutes with
the rule, so it permutes the cycles and preserves their lengths, and the orbit of a cycle under the rotation group
$\mathbb Z_p$ has size 1 or $p$. Hence a cycle whose length occurs fewer than $p$ times among all cycles is fixed by
rotation: rotation by one cell acts on it as some power of the time map (the pattern travels). In particular, when
all cycle lengths are distinct, every cycle is such a glider.

*Proof.* Commutation: both the rule and the rotation are defined by the same local function applied at every cell.
A group of prime order acting on a set has orbits of size 1 or $p$. A cycle fixed by rotation $\rho$ satisfies
$\rho(s) \in \{f^j(s)\}$ for a state $s$ on it, i.e. $\rho = f^j$ on the cycle. $\square$

### C.7 The first three columns are affine in column 1 (RULE30-PRIZE.md §8.58; used in COLLATZ-PRIZE.md §5)

*Where:* §8.58. *Bears on:* the counting form; the Collatz twin. *Status:* proved (a table computed from the inverse
rule next to the alternating wall; the product first appears in column $-4$).

**Fact.** Next to the wall $0101\ldots$, write $c_s$ for column 1 at time $2s$ (the visible bits). At times $2s$ and
$2s+1$ the forced columns are:

| Column | $-1$ | $-2$ | $-3$ | $-4$ |
|---|---|---|---|---|
| time $2s$ | $\bar c_s$ | $c_s$ | $\bar c_{s+1}$ | $c_s\,c_{s+1}$ |
| time $2s + 1$ | 1 | $c_{s+1}$ | $\bar c_{s+1}$ | $c_{s+2}$ |

Column $-2$ is column 1 with every visible bit held for two steps, column $-3$ is its complement one step on, and
the first product appears in column $-4$.

*Proof.* Lemma 1's explicit form gives column $-1$ ($1$ at odd times, $\bar c_s$ at time $2s$); each further
column is the inverse rule $x(-j, t) = x(-j+1, t+1) \oplus (x(-j+1, t) \vee x(-j+2, t))$ applied to the two columns
to its right, which the table carries out for $j = 2, 3, 4$. $\square$


## E. Theorems proved by GPT (statements verbatim; the proofs are in RULE30-GPT.md at the section named)

GPT's lane is its own file. The statements are copied so that this list is complete; GPT is asked to append its
proofs here in its own words, or to say which it would rather keep as pointers.

### E.1. G13.2. Complete reset language, with a failed first characterization retained

*Where:* RULE30-GPT.md, "G13.2. Complete reset language, with a failed first characterization retained". *Status:* proved by GPT (proof there).

**Theorem.** A finite driver word resets exactly when it contains a factor

### E.2. G13.5. Several backward steps, with the protected window's exact cost

*Where:* RULE30-GPT.md, "G13.5. Several backward steps, with the protected window's exact cost". *Status:* proved by GPT (proof there).

**Theorem.** Suppose a wall has a hole at q and then p−1 black cells, with no premise on its
values outside that window. Compare two right columns differing only at q. For any integer
r with $0\le r\le q$ and $p\ge3r+5$, their rows at q−r agree at **every** depth≥4r+4. In
addition their common cells in the interval

### E.3. G17.1. Exact all-period theorem and certificate

*Where:* RULE30-GPT.md, "G17.1. Exact all-period theorem and certificate". *Status:* proved by GPT (proof there).

**Theorem.** For every p>=2, width-three and width-two relaxations of wall0 1^(p-1)
have exactly the same finite and infinite one-sided hole languages. Thus even p
avoids11; p3 avoids100; odd p>=5 is unrestricted. G16's counts and entropy rates
remain exact for this relaxation. The third cell neither lowers these rates nor
removes any visible word, even though it constrains the hidden dynamics.

### E.4. G18.2. Exact finite-prefix map from a latch position

*Where:* RULE30-GPT.md, "G18.2. Exact finite-prefix map from a latch position". *Status:* proved by GPT (proof there); its finite controls replicated by Local from the committed `rule30_gpt_slow_switch.py`, 2026-10-06 at edce038.

**Theorem.** For wall0^a1^b, a,b>=1, the first p-1 left cells on row0 are
determined by the a visible sigma bits at the white times. If these bits are
monotone (the necessary width-one rule), exactly a+1 distinct prefixes occur.
This is a finite-prefix assertion, not an autonomous state for the infinite row.

### E.5. G18.3. Uniform protected-band theorem, even without a white prefix

*Where:* RULE30-GPT.md, "G18.3. Uniform protected-band theorem, even without a white prefix". *Status:* proved by GPT (proof there); its finite controls replicated by Local from the committed `rule30_gpt_slow_switch.py`, 2026-10-06 at edce038.

**Theorem.** Suppose a black wall run occupies times a..a+b-1, preceded by any a
wall bits and followed by anything. If a>=1 and b>=3a+1, row0 is checkerboard
on depths4a..a+b-1: even depths are1 and odd depths0. The right column before,
during and after the run is arbitrary. In particular this holds for slow walls,
without needing the monotone latch hypothesis.

### E.6. G20.1. Exact theorem, including the failed first prediction

*Where:* RULE30-GPT.md, "G20.1. Exact theorem, including the failed first prediction". *Status:* proved by GPT (proof there).

**Theorem.** For every odd p>=5, the width-four relaxation of wall0 1^(p-1)
allows every finite and infinite one-sided sequence of visible hole bits. It has
exactly2^n words of length n and rate1/p bit per time step. Combining G15-G17,
a layer that first restricts these walls, if one exists, has width at least five.
This is not an existence proof for an entire infinite right half or a finite seed.

### E.7. G27.2. The periodic-pair obstruction works on the forced half-line

*Where:* RULE30-GPT.md, "G27.2. The periodic-pair obstruction works on the forced half-line". *Status:* proved by GPT (proof there).

**Lemma (Jen/Kopra mechanism, half-line form).** For Rule30 on a nonconstant periodic wall, or Rule210 on0101, no consistent left-half evolution with an initially eventually-zero left row can have an eventually periodic adjacent left column pi. Right-half realizability is not a premise.


Further exact results of GPT's recorded as theorems inside RULE30-GPT.md §G11 to §G35 (shielding, reset and the
protected window on one-hole walls; the exact injection rate $\log_2(a+1)/(a+b)$ on slow walls (G15); the reset
theorem for $b \ge 3a + 1$ (G18); the latch obstruction (G19); the sideways map's ternary image (G22); the
periodic Garden-of-Eden density (G24); the dyadic stream and the parity classification (G26, G27); the Collatz
exclusions G28 to G35) are GPT's to copy here; this file lists the ones whose statements carry a theorem heading.


## F. Collatz

### F.1. The remainder lemma

*Where:* COLLATZ-PRIZE.md, "4. The state after the free bits is a remainder modulo a power of 3 (2026-10-05)". *Bears on:* the counting form for Collatz (COLLATZ-PRIZE.md §1). *Status:* proved.

**Lemma.** Let $0 \le r < 2^k$, and let $a$ be the number of odd steps among the first $k$ steps of $r$. Then

### F.2. Dubickas's theorem (external; the record's W2)

*Where:* COLLATZ-PRIZE.md §5; PRIOR-ART.md. *Status:* a published theorem (A. Dubickas, 2009, Theorem 5), read in
full and credited; the record's "complexity at least $1.70951129\,n$" statement for divergent integer orbits is
its restatement, and GPT's G29 audits its extension to signed rationals with the hypotheses named.


## E2. GPT's Collatz proofs G39 to G47, second-read by Local (moved from the waiting room, 2026-10-06)

*Second reader's notes (Local, 2026-10-06; chat L007).* Each argument was read line by line, and the load-bearing
identities were checked with independent code, `tests/probes/prizes/collatz_audit_g39_g42.py` (exact arithmetic,
every admissible word to $T = 14$, zero failures). Verdicts: **G39 correct.** The rotation-to-the-minimum step is
the cycle lemma; the lower bound $\binom{T}{a}/T$ is not tight (a class can hold more than one admissible
rotation, since $S_T > 0$ leaves room), which the statement does not claim. One wording: "distinct partial sums
cannot coincide" means partial sums at distinct indices. **G40 correct, and stronger than stated for the affine offset:** the swap
additivity of $f_w(0)$ holds exactly over $\mathbb{Q}$, not only modulo $3^a$ (the terminal value $q$ itself also
carries $3^a r / 2^T$ with a representative $r$ that changes under a swap, so for $q$ the statement stays modulo
$3^a$; GPT's precision in G007, taken), by a direct route that needs no ternary map:
$f_w(0) = \sum_{i:\,w_i = 1} 3^{m_i} / 2^{T - i + 1}$ with $m_i$ the number of ones after position $i$, and swapping a
free pair from 10 to 01 moves one odd step one place later without changing any $m_i$, which adds exactly
$3^{a-s-1} 2^{-(T-t)}$. **G41 correct.** The mode argument, both Chernoff bounds and the transfer through G39 check;
the minimum of $2p(1-p)$ over the interval is at $p = 1 - \varepsilon$ as used. **G42 correct.** The identity
$2^T q = 3^a r + \sum_{\text{odd } j} 2^j 3^{a - S_{j+1}}$ was verified on every admissible word to $T = 10$; the
family's sum is exactly $20480/3103353$ and the modulus is at least $0.9934$.

### G.GPT39. Fixed-endpoint survival conditioning

**Where:** RULE30-GPT.md G39, 2026-10-06; proof copied verbatim below. **Bears on:** PERIOD-TWO.md §7 question9, the count twin. **Status:** complete analytic argument with single-party finite implementation controls; second-read by Local, 2026-10-06 (see the notes at the head of E2). No Fourier decay or prize solution claimed.

### G39 theorem and proof: fixed-endpoint event transfer

Fix integers T>=1 and0<=a<=T with3^a>2^T. Let U be the uniform law on binary words of lengthT with a ones. Let E require3^a_t>2^t at every nonempty prefix. If A(T,a) counts E, then

    binomial(T,a)/T <= A(T,a) <= binomial(T,a).

**Proof.** For a word w, put S_j=a_j*log(3)-j*log(2), for0<=j<=T. Distinct partial sums cannot coincide: equality would give3^d=2^e with a nonzero integer time difference e, contrary to unique prime factorisation. Choose the unique minimum S_k among S_0,...,S_(T-1). Rotate w to start just after indexk. Before wrapping, every new nonempty partial sum is S_j-S_k>0, including j=T since S_T>0 and S_k<=0. After wrapping it is S_T+S_j-S_k>0. Hence each rotation class contains an admissible word. Every class has at mostT members, even when the word is nonprimitive. Thus the number of classes is at least binomial(T,a)/T and A is at least that number. The upper bound is immediate.

Consequently, for any event B and nonnegative function f on this finite population,

    U(B | E) <= T*U(B),
    expectation_U(f | E) <= T*expectation_U(f).

This follows by dropping the E indicator from the numerator and using U(E)>=1/T. It is a fixed-endpoint comparison, not a bound on the probability of that endpoint under a different law. It applies equally to any iid Bernoulli law after conditioning on its endpoint count, because that conditional law is uniform. It concerns coefficient admissibility, not actual stopping-time survival.

**Cancellation boundary.** On the uniform group Z/2, the nontrivial character has values+1,-1 and expectation0. Conditioning on the +1 point costs just2, but leaves character expectation1. Therefore the event bound cannot imply an analogous bound multiplying the absolute unconditioned complex expectation. This counterexample rejects a general transfer principle, not a possible special estimate for Collatz. Exponentially rare events at fixed endpoints retain their exponential rate after the polynomial factorT; exponentially small Fourier expectations need additional control of their correlation with E.

**Exact next operator.** Fix terminal(T,a). Let h(t,s) count admissible completions after an already-admissible prefix with t bits and s ones. Terminal values are h(T,s)=1 if s=a, otherwise0; impossible states have0. Backwards, h(t,s) is the sum of h(t+1,s+b) over b=0,1 for which3^(s+b)>2^(t+1). Whenever h(t,s)>0, the uniform endpoint-surviving next-bit probability is h(t+1,s+b)/h(t,s) for an admitted child, and0 otherwise. This is proved by partitioning completions by their next bit. These weights depend on(t,s), not on the terminal residue q, although q and the path are correlated. Substituting these weights into G38's deterministic residue update gives the conditioned operator exactly; the weights need not be iid. No decay estimate follows merely from writing this operator.


### G.GPT40. Survival-compatible adjacent-pair phase product

**Where:** RULE30-GPT.md G40, 2026-10-06; proof copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9, the count twin. **Status:** complete analytic argument with single-party implementation controls; second-read by Local, 2026-10-06 (see the notes at the head of E2). No aggregate decay claimed.

### G40 theorem and proof: the skeleton phase product

Fix lengthT and endpoint odd count a with3^a>2^T. Partition the coefficient-admissible words into skeletons by recording each adjacent pair as00,11 or mixed, retaining an odd final bit separately. Discard skeletons with no survivors. A skeleton fixes the odd count s at the start t of every pair, and all pair-end coefficient ratios.

For a mixed pair let R=3^s/2^t. Orientation10 has intermediate ratio3R/2 and final ratio3R/4; orientation01 has intermediate ratioR/2 and the same final ratio. Thus, in a surviving skeleton,10 is always allowed;01 is allowed exactly whenR>2. Other prefixes are unchanged by a swap. Therefore the surviving orientations form a full independent binary cube on the free mixed pairs with3^s>2^(t+1); all other mixed pairs are forced10. In particular a skeleton with F free pairs contains exactly2^F words.

Let q(w) be the terminal iterate of the unique representative in[0,2^T), reduced moduloM=3^a. G38's carry-free ternary map applies. Modulo an odd power of3, a local10 composition sends x to(3x+1)/4;01 sends x to(3x+2)/4. Their difference is1/4. The following suffix has lengthT-t-2 and c=a-s-1 odd steps, so its slope is3^c/2^(T-t-2). Hence the final difference is

    Delta_t = 3^(a-s-1)*2^(-(T-t)) modulo3^a.

Negative powers mean multiplicative inverses modulo the odd modulus. The suffix slope depends only on its count, not its other orientations. The differences are therefore additive across all free pairs. If w0 has every mixed pair oriented10, then

    q(w) = q(w0) + sum_t eta_t*Delta_t moduloM,

where eta_t=1 for a free pair oriented01 and0 for10. Uniform sampling in this skeleton makes the eta_t independent fair bits. With e(x)=exp(2*pi*i*x), its normalized Fourier coefficient is exactly

    phi_S(h) = e(h*q(w0)/M) * product_t (1+e(h*Delta_t/M))/2.

Thus its modulus is the product of |cos(pi*h*Delta_t/M)|. This is an identity for the survival-conditioned population inside each skeleton, not an iid assumption on the whole path.

**Aggregate boundary.** If A is the total survivor count and S ranges over surviving skeletons at this endpoint, then

    |phi(h)| <= sum_S (2^F(S)/A)*product_free_t |cos(pi*h*Delta_t/M)|.

This follows by partitioning the uniform population and applying the triangle inequality only between skeletons; cancellation within each cube is retained exactly. For h coprime to3 every free pair gives a strictly smaller than1 factor, since Delta_t has3-adic valuation a-s-1<a. There is no uniform gap from1 as the denominator grows. At a=T the sole all-one word has no free pairs and unit Fourier modulus. This does not preclude decay for an aggregate with other endpoint weights; it does preclude a contraction asserted uniformly at every endpoint. A decay theorem still needs quantitative frequency control and mass bounds for the surviving skeletons.


### G.GPT41. Interior-endpoint free-pair mass

**Where:** RULE30-GPT.md G41, 2026-10-06; proof copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9, the count twin. **Status:** complete analytic argument; single-party finite controls; second-read by Local, 2026-10-06 (see the notes at the head of E2). No Fourier-decay estimate claimed.

### G41 theorem and proof: linearly many free pairs at interior endpoints

Put beta=log(2)/log(3). Fix epsilon>0 such that[beta+epsilon,1-epsilon] is nonempty. For any fixed endpoint p=a/T in this interval, sample uniformly from the coefficient-admissible words. For every B>0 there is K depending only on epsilon and B such that, outside probability O(T^(-B)), this word has linearly many free mixed pairs starting after L=ceil(K*log(T)). The statement is asymptotic for sufficiently largeT; constants do not depend on a. It asserts abundance of G40's free choices, not separation of their phases.

**Proof.** Let V be iid Bernoulli(p) on lengthT words, U its law conditional on endpoint count a, and U_E the law after also imposing prefix survival E. The binomial endpoint a is a mode of V's count distribution: the ratio of masses at k+1 and k is (T-k)*p/((k+1)*(1-p)), decreases with k, exceeds1 at k=a-1, and is below1 at k=a. Since there are T+1 possible counts, V(S_T=a)>=1/(T+1). Therefore for every event D, G39 gives

    U_E(D) <= T*U(D) <= T*(T+1)*V(D).

Choose lambda>0 sufficiently small that

    rho = exp(lambda*beta)*(1-(beta+epsilon)+(beta+epsilon)*exp(-lambda)) < 1.

Such a choice exists because the expression equals1 at lambda0 and has derivative-epsilon there. For p>=beta+epsilon the analogous moment is no larger. A low incoming ratio at time t means3^S_t<=2^(t+1), hence S_t<=beta*(t+1). The exponential Markov inequality yields

    V(S_t<=beta*(t+1)) <= exp(lambda*beta)*rho^t.

Indeed apply Markov to exp(-lambda*S_t) and use independence to evaluate its expectation as(1-p+p*exp(-lambda))^t. Union over t>=L bounds any such late visit by C*rho^L, where C=exp(lambda*beta)/(1-rho). This includes all late pair starts.

There are n=floor(T/2)-ceil(L/2) disjoint pairs starting at even t>=L. Under V their mixed indicators are independent with probability u=2p(1-p). Throughout the specified interval u>=u0=2epsilon*(1-epsilon)>0. Put kappa=u0/2 and choose theta>0 sufficiently small that

    sigma = exp(theta*kappa)*(1-u0+u0*exp(-theta)) < 1.

Again the derivative at0 is kappa-u0<0. Exponential Markov on their mixed count M gives V(M<=kappa*n)<=sigma^n. If no late low-ratio visit occurs, G40 makes every late mixed pair free, so its free count F equals M. Consequently

    U_E(F<=kappa*n) <= T*(T+1)*(C*rho^L+sigma^n).

Choose K>(B+2)/(-log(rho)). With L=ceil(K*log(T)), n=T/2-O(log(T)), the displayed bound is O(T^(-B)); the second term is exponentially small. This proves the uniform statement. No independence is assumed under U_E: all independence is used under V and transferred through the two explicitly bounded conditioning costs.

**Frequency boundary.** A concrete length12 skeleton begins1111, has three mixed pairs, and ends11. Every orientation of the three mixed pairs survives, so it has8 words and a=9. Their free-pair starting odd counts are s=4,5,6. G40's differences have3-adic valuations4,3,2 respectively. At the nonzero harmonic h=3^7 modulo3^9, all three h*Delta vanish. The entire cube has a constant character and unit Fourier modulus. This is a divisible-by3 frequency control; it does not contradict G40's strict contraction for unit harmonics. The all-one endpoint separately shows why the hypothesis p<=1-epsilon is necessary. Free-pair mass alone does not supply the frequency-sensitive separation needed in G40's aggregate bound.


### G.GPT42. A primitive-character resonance with linearly many free pairs

**Where:** RULE30-GPT.md G42, 2026-10-06; copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9, the count twin. **Status:** complete analytic counterexample family and single-party controls; second-read by Local, 2026-10-06 (see the notes at the head of E2). No aggregate cancellation conclusion.

### G42 theorem and proof: primitive characters can remain resonant

For any parity word of lengthT with a odd steps, write its representative as r in[0,2^T) and terminal value as q. The affine iteration identity is

    2^T*q = 3^a*r + sum_odd_j 2^j*3^(a-S_(j+1)).

Dividing by3^a shows that the character at h=2^T modulo3^a is exactly e(F_T), with F_T=sum_odd_j 2^j/3^S_(j+1), the real inverse partial sum in G32. Here e(x)=exp(2*pi*i*x). At an admitted endpoint h<3^a and is coprime to3, so this is a nonzero primitive character. Multiplying G40's swap difference by h gives phase

    h*Delta_t/3^a = 2^t/3^(s+1) modulo1.

This follows by cancelling the modular inverse of2^(T-t); it is an exact identity, not a real approximation to that inverse.

**Explicit family.** Begin with1111, then repeat the pair-of-pairs(11,M) n times, where M independently chooses10 or01. The skeleton has T=4+4n, a=4+3n and n mixed pairs. Every orientation survives: the initial four ones increase the coefficient ratio; a block has total ratio27/16>1, its first11 multiplies the incoming ratio by9/4, and either mixed orientation remains above1 at its intermediate and final prefixes. In particular every mixed pair is free in G40's sense. There are exactly2^n words.

The kth mixed pair, starting with k=0, has t=6+4k and s=6+3k. Its resonant phase is

    x_k = (64/2187)*(16/27)^k.

G40 gives the normalized Fourier modulus as product_(k<n) cos(pi*x_k); all factors are positive. The elementary inequality cos(u)>=1-u^2/2 and pi^2<10 imply cos(pi*x_k)>=1-5*x_k^2. For nonnegative d_k<=1, induction gives product(1-d_k)>=1-sum(d_k). The full infinite geometric sum satisfies the exact rational inequality

    5*sum_(k>=0) x_k^2 = 20480/3103353 < 1/100.

Therefore the modulus is greater than0.99 for every n. This proves that even a linear count of free mixed pairs, at endpoint densities tending to3/4, does not force within-skeleton Fourier decay uniformly over primitive characters. Each factor is strictly below1, consistent with G40, but their losses are summable.

**Scope.** The family contributes2^n words at its endpoint; no positive lower bound on its fraction of the whole survivor population is asserted. Other skeletons may cancel its contribution or dominate its mass. Thus this counterexample neither refutes aggregate Fourier decay nor proves that G40's weighted absolute-product bound fails. It identifies the missing frequency-sensitive condition. The special harmonic also connects the ternary character directly to G32's real inverse sum; convergence or positivity in the real metric still must not be equated with the 2-adic inverse value.

### G.GPT43. Exact binary-reader Fourier weights

**Where:** RULE30-GPT.md G43, 2026-10-06; copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9 and COLLATZ-PRIZE.md §4. **Status:** analytic derivation and single-party controls; second-read by Local, 2026-10-06 (see the note below the heading of E2). No tail-count bound.

### G43 theorem and proof: exact ternary spectrum of a binary reader

Let M=3^a with a>=1, and interpret q moduloM by its least representative0<=q<M. Set f(q)=(-1)^q and e(x)=exp(2*pi*i*x). For0<=h<M define hat f(h)=M^(-1)*sum_q f(q)*e(-h*q/M). A geometric sum with ratio-e(-h/M) gives

    hat f(h) = 2/[M*(1+e(-h/M))],
    |hat f(h)| = 1/[M*|cos(pi*h/M)|].

The numerator is2 because M is odd and e(-h)=1. The denominator is nonzero for integer h on an odd group. In particular hat f(0)=1/M, not0. Fourier inversion gives, for any distribution of q with phi(h)=expectation e(h*q/M),

    expectation f(q) = sum_h hat f(h)*phi(h).

G38's upper-half state is y=M+q. Since M is odd, its next parity is odd exactly when q is even. Thus

    probability(y odd) = (1+sum_h hat f(h)*phi(h))/2.

This sum is real, although individual summands may be complex. Uniform ternary residues give probability(y odd)=(M+1)/(2M), including the finite1/(2M) bias.

**Which frequencies matter.** The weights peak near h=M/2, where |hat f((M-1)/2)|=1/[M*sin(pi/(2M))], tending to2/pi. If0<=h<=M/3, then |hat f(h)|<=2/M. In G42's family, M/h=(81/16)*(27/16)^n>3 at the resonant primitive harmonic h=2^T. Its contribution to the parity-reader sum therefore has magnitude at most2/M even though |phi(h)|>0.99. This is a within-family bound; it does not transfer that family's measure to the full population. It also does not refute the general relevance of primitive-frequency resonances to other test functions.

For completeness, writing d=|h-M/2| gives |hat f(h)|=1/[M*sin(pi*d/M)]<=1/(2d), using sin(x)>=2x/pi on[0,pi/2]. Sum over the half-integer distances to obtain sum_h|hat f(h)|<=3+log(M), with log natural. Indeed the paired distances give sum_(j=0)^((M-3)/2)1/(j+1/2) plus1/M, bounded by2+log(M)+1/M by integral comparison. Hence a bound |phi(h)|<=delta for all nonzero h implies

    |probability(y odd)-(M+1)/(2M)| <= delta*(3+log(M))/2.

This proves the logarithmic Fourier-weight assertion for one binary bit; it supplies no delta estimate itself. Frequency-specific estimates may instead be inserted into the exact weighted sum.

**Longer binary cylinders.** For B=2^d,0<=c<B, let g_c(q)=1 when q is congruent to c moduloB. Put L_c=max(0,1+floor((M-1-c)/B)). Its Fourier coefficient is the exact finite sum

    hat g_c(h) = e(-h*c/M)/M * sum_(j=0)^(L_c-1) e(-h*B*j/M).

The empty sum is0; at h=0 the value is L_c/M. A nonzero-frequency sum is the usual geometric quotient. A prescribed future parity word corresponds by the parity bijection to one residue of y moduloB, and therefore to c for q after subtracting M. If B>=M, each nonempty cylinder contains just one representative q, and every coefficient has magnitude1/M. Thus the complete tail problem requires finer information than the one-bit reader. Furthermore actual stopping-time survival compares the iterates with their start, not merely with the coefficient barrier; these populations cannot silently be equated.

*Second reader's note on G43 (Local, 2026-10-06; chat L008).* Correct throughout. The geometric sum and its
numerator 2 (odd $M$), the nonvanishing denominator ($e(-h/M) = -1$ is impossible for odd $M$), $\hat f(0) = 1/M$,
the bound $2/M$ for $0 \le h \le M/3$, the peak $2/\pi$, the weight bound via $\sin x \ge 2x/\pi$ and the integral
comparison ($\le 2 + \log M + 1/M$), and the cylinder sums were each checked by hand; the coefficient formula
was checked numerically against the direct sum for every odd $M < 400$ (error $4 \times 10^{-14}$), the weight bound
for those $M$ and for $M = 3^6$ to $3^9$, and the bound $2/M$ at $h = 2^T$ for G42's family for $n = 0$ to $39$
(`collatz_audit_g39_g42.py`, G43 part).

### G.GPT44. Exact finite-ensemble parity-tail information budget

**Where:** RULE30-GPT.md G44, 2026-10-06; copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9 and COLLATZ-PRIZE.md §4. **Status:** complete finite-counting argument and single-party exact controls; second-read by Local, 2026-10-06 (note below). No stopping-time count bound.

### G44 theorem and proof: resolution of a finite residue ensemble

Fix odd M=3^a, a>=1. Let q be uniform on the least representatives0,...,M-1 and y=M+q. For d>=1 put B=2^d. The parity bijection identifies the first d parities of y with y moduloB, through a permutation of the B labels. Therefore its total variation distance from uniform d-bit words equals the variation distance of y moduloB from uniform residues moduloB.

Write M=kB+r with0<=r<B. In any M consecutive integers exactly r residue classes occur k+1 times and the others k times. Hence the variation distance is exactly

    TV = r*(B-r)/(B*M).

Indeed the r excess masses have difference(k+1)/M-1/B=(B-r)/(B*M), and the remaining deficit masses have difference1/B-k/M=r/(B*M); their summed absolute differences divided by2 give the displayed value. It follows that TV<=B/(4M). When B>=M the same formula becomesTV=1-M/B. Thus the approximation improves for coarse binary resolution, but becomes sparse when the requested word population greatly exceeds the initial residue population.

**Information statement.** When B>=M, distinct q give distinct y moduloB, and hence distinct d-parity words. The map is then injective on the entire initial ensemble. For any distribution of q, the Shannon entropy of these words equals H(q); for all d it is at most H(q)<=log2(M), because the words are a deterministic function of q. Uniform q gives entropy exactlylog2(M) once B>=M. This is a finite initial ensemble; it does not make the integer Collatz dynamics an autonomous finite-state system.

More generally, if the q law has support sizeN<=M, its word law has support at mostN and TV from uniform B words is at least1-N/B. Choose that support as the test event: its actual probability is1 and its uniform probability is at mostN/B. For a law uniform on N distinct q and B>=M, the distance is exactly1-N/B and entropylog2(N). Actual endpoint ensembles may have nonuniform terminal-q weights, so they must use their own support and law; uniformity on all M residues is an explicitly idealized comparison.

**Retained counterexample to an overstrong route.** Fix q0 and consider the actual d-parity prefix of y0=M+q0 at each d. For uniform q, once B>=M this cylinder has probability1/M. Its fair-coin probability is2^(-d). Their ratio is2^d/M and is unbounded with d. Thus no constant C can bound every cylinder's probability by C times its coin probability for arbitrarily long tails. No assumption about eventual behaviour of y0 is needed: every integer orbit has finite prefixes. The example refutes only a simultaneous all-cylinder comparison. It neither refutes the specially constrained stopping-time count in COLLATZ-PRIZE.md §1 nor predicts a divergent orbit. That target concerns a selected union of words whose paths stay above their start; some such events may become empty.

*Second reader's note on G44 (Local, 2026-10-06; chat L009).* Correct. Terras's bijection carries the parity-word
law to $y \bmod B$; the count of residue classes among $M$ consecutive integers gives the excess and deficit masses
$(B-r)/(BM)$ and $r/(BM)$ and so $\mathrm{TV} = r(B-r)/(BM) \le B/(4M)$; for $B > M$ ($B \ne M$, one odd and one a
power of two) $k = 0$, $r = M$, $\mathrm{TV} = 1 - M/B$, and the map from $q$ to words is injective; the support and
cylinder statements follow. Checked exactly against parity words computed directly from $y = M + q$ for $a = 1$ to
6 and $d = 1$ to 13 (78 cases, zero failures; `collatz_audit_g39_g42.py`, G44 part).

### G.GPT45. Word-specific actual-start survival ceilings

**Where:** RULE30-GPT.md G45, 2026-10-06; copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9, the actual stopping-time count. **Status:** analytic derivation, second-read by Local, 2026-10-06 (note below); GPT's own preregistered controls had not run at publication.

### G45 theorem and proof: actual-start survival is a residue class cut by a ceiling

Fix a binary parity word w of lengthT>=1. Let a_t count its ones in the first t positions and define B_0=0. Reading the bit b at positiont, update

    B_(t+1)=3^b*B_t+b*2^t.

The usual affine iteration gives n_t=(3^a_t*n+B_t)/2^t for a start n realizing this word. Its realizing starts form the residue class

    n = r_w modulo2^T,
    r_w = -B_T*(3^a_T)^(-1) modulo2^T.

This is the known parity bijection. To see the congruence characterization directly, necessity follows from integrality of n_T. Conversely the congruence propagates to each prefix by reducing modulo2^t: B_T is3^(a_T-a_t)*B_t modulo2^t, so the prefix affine expressions are integers. At each step integrality of the next expression forces the prescribed parity; induction gives the word. The inverse exists because3^a_T is odd.

Actual survival throughT means n_t>=n for every1<=t<=T. If3^a_t>2^t, this condition holds automatically for positive n, since B_t>=0. Equality is impossible for t>=1 by unique prime factorisation. At a deficient prefix3^a_t<2^t, it is equivalent to

    n <= floor(B_t/(2^t-3^a_t)).

Define K_w to be the minimum of these integer ceilings over deficient prefixes, or infinity if there are none. Then the positive starts realizing w and surviving throughT are exactly

    n congruent to r_w modulo2^T, with1<=n<=K_w.

For w-bit starts put L=2^(w-1), U=min(2^w-1,K_w). The exact count for this word is0 if U<L, otherwise

    floor((U-r_w)/2^T)-floor((L-1-r_w)/2^T).

Summing over all lengthT words gives the actual-start survivor count, with no population identified with coefficient survivors by assumption. Words whose coefficient barrier survives have K_w=infinity. Every other word has a finite ceiling, so its actual-survival exceptions are restricted to small starts relative to that particular word. No bound on these ceilings uniform over word length has been proved here.

**Unexpected analytic scope check.** The word1010 has B_4=7,a_4=2 and deficient final coefficient9/16. Its ceiling is K=1 and its residue is1 modulo16. The positive start1 follows the cycle1,2,1,2,1 and stays at or above its start, although its coefficient barrier already fails at step2, where3/4<1. Thus the two notions are not universally equal. This does not challenge their recorded agreement for starts of20 to32 bits.

**What remains.** The formula isolates two contributions: coefficient-admissible residues, and bounded-start exceptions from words with a coefficient deficit. It is an exact finite enumeration identity, not a better bound on either contribution. Both depend on the specific words and realizing residue classes. The generic all-cylinder mixing failure in G44 does not settle their sum. The affine mechanism is established parity machinery; no novelty claim.

*Second reader's note on G45 (Local, 2026-10-06; chat L012).* Correct. The update $B_{t+1} = 3^b B_t + b\,2^t$ is the
affine iteration; the converse of the residue-class statement follows from $B_T \equiv 3^{a_T - a_t} B_t \pmod{2^t}$
(every later term carries a factor $2^s$ with $s \ge t$) and the oddness of 3; survival at a deficient prefix is
exactly $n \le \lfloor B_t / (2^t - 3^{a_t}) \rfloor$; the counting formula is the standard count of a residue class
in an interval; the example 1010 ($B_4 = 7$, $K = 1$, $r = 1$; the orbit $1, 2, 1, 2, 1$) checks. Independently, the
sum of the formula over all words equals a brute-force count of actual survivors (iterates $\ge n$ through $T$
steps) for every $w = 1$ to 12 and $T = 1$ to 14: 168 cases, zero failures (`collatz_audit_g39_g42.py`, G45 part).

### G.GPT46. Unbounded formal ceilings and residue-count rounding

**Where:** RULE30-GPT.md G46, 2026-10-06; copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9. **Status:** analytic argument, second-read by Local, 2026-10-06 (note below); GPT's KC controls preregistered and not run at publication. G45's controls passed and its argument was independently audited by Local L012.

### G46 theorem and proof: the formal ceilings are unbounded

For k>=1 take the word consisting of k ones followed by j-k zeros, where j is the unique integer with2^(j-1)<3^k<2^j. This is j=ceil(k*log2(3)). Every proper prefix has coefficient above1, and the final prefix is deficient. After the first k odd steps the affine intercept is3^k-2^k, unchanged by the following even steps. Thus G45's ceiling for this word is exactly

    K_k = floor((3^k-2^k)/(2^j-3^k)).

These ceilings are unbounded. Put alpha=log2(3), irrational by unique prime factorisation, and delta_k=ceil(k*alpha)-k*alpha. There are arbitrarily large k with delta_k arbitrarily close to0 from above. Here is an elementary one-sided approximation argument. Pigeonholing the fractional parts of0,alpha,...,N*alpha gives a positive q whose multiple is within1/N of an integer. If its fractional part is near1, q already works. Otherwise write its fractional part as eta with0<eta<1/N and take m=floor(1/eta). Irrationality implies m*eta<1 and1-m*eta<eta, so k=m*q has fractional part within eta of1. Taking N arbitrarily large produces delta_k tending to0. Such k must tend to infinity, because each fixed k has a nonzero gap.

The ratio inside the floor is

    (1-(2/3)^k)/(2^delta_k-1).

Along those k its numerator tends to1 and its denominator tends to0 positively, so K_k tends to infinity. In particular the maximum finite word ceiling over word lengths is not O(1). This argument establishes unboundedness, not a polynomial upper bound in j. It uses the elementary affine/parity formula and irrational approximation; no novelty claim.

**Residue-placement boundary.** A ceiling K bounds possible starts in[1,K], but a single realizing residue class modulo2^T has count at mostfloor(K/2^T)+1, not necessarily K/2^T. For word1010, T=4,K=1 and residue1, that count is1 whereas K/2^T=1/16. Thus multiplying a small ceiling by a density1/2^T can give a false upper bound without controlling which residues occupy the short interval. Unbounded K does not imply unbounded actual-survival exceptions: realizing residues may exceed their ceilings. Conversely, a polynomial upper bound on K alone would not remove the additive rounding term. This is a correction to a possible counting shortcut, not a disagreement with G45's exact formula or the observed large-width coefficient agreement.

*Second reader's note on G46 (Local, 2026-10-06; chat L014).* Correct. Only the final prefix of $1^k 0^{j-k}$ is
deficient ($2^{k+i} \le 2^{j-1} < 3^k$ for $k + i < j$); the intercept after $k$ odd steps is
$\sum_{t<k} 3^{k-1-t} 2^t = 3^k - 2^k$; the ratio is $(1 - (2/3)^k)/(2^{\delta_k} - 1)$; and the one-sided approximation is sound ($m = \lfloor 1/\eta \rfloor$
gives $m\eta < 1$ by irrationality and $1 - m\eta < \eta$, so the fractional part of $mq\alpha$ is
within $\eta$ of 1). Checked exactly: the closed form equals G45's general ceiling for every $k \le 399$, and the
record ceilings $(k, K)$ are $(5, 16)$, $(17, 25)$, $(29, 39)$, $(41, 86)$, $(94, 106)$, $(147, 136)$, $(200, 191)$,
$(253, 321)$, $(306, 977)$, at the $k$ where $k\log_2 3$ falls just below an integer (`collatz_audit_g39_g42.py`, G46 part).

### G.GPT47. First-deficit single-run survival implies a periodic return

**Where:** RULE30-GPT.md G47, 2026-10-06; copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9. **Status:** complete analytic argument, second-read by Local, 2026-10-06 (note below); GPT's RC controls published, not run at publication. G46's KC controls passed; G46 argument independently audited by Local L014.

### G47 theorem and proof: this first-deficit family realizes only by a return

Use G46's word1^k followed by j-k zeros, k>=1,j=ceil(k*log2(3)). Put D=2^j-3^k>0 and B=2^(j-k). Any positive start realizing its first k ones has n=2^k*m-1 for a positive integer m, by the exact odd-run identity in G31. After those k odd steps its value is3^k*m-1. Realizing the following j-k zeros requires

    3^k*m-1 = 0 moduloB,
    D*m = -1 moduloB.

The final value is n_j=(3^k*m-1)/B. Since the first segment increases and the even segment decreases, actual survival through this word is equivalent to n_j>=n. Direct subtraction gives

    n_j-n = (B-1-D*m)/B.

The positive integer D*m is congruent to B-1 moduloB, so D*m>=B-1. Survival requires the reverse inequality. Both hold exactly when D*m=B-1, making n_j=n. Therefore there is an actual surviving positive start for this word if and only if

    D divides B-1.

If so it is unique: m=(B-1)/D and n=2^k*m-1. Conversely this value has the prescribed initial odd run and subsequent even run:3^k*m-1=B*n, with n positive odd, so its next j-k parities are zero and its final value is n. All intermediate values are at least n. It lies below2^j and is the single positive representative that can pass the ceiling. Thus this is a genuine periodic return, not a divergent orbit.

At k=1,j=2,D=1,B=2 the criterion gives start1 and the known1,2 cycle. No assertion that this is the only qualifying k for all lengths is proved here. Excluding other positive cycles would require additional reasoning or a precisely audited external result. The criterion is a specialization of G33's known periodic affine formula, sharpened by the monotone shape and first-deficit condition. It does not apply to arbitrary interleaved parity words or bound their actual-survival exceptions. In particular G46's unbounded formal ceilings alone cannot produce nonperiodic exceptions in this specific family.

*Second reader's note on G47 (Local, 2026-10-06; chat L017).* Correct. A start with $k$ initial odd steps is
$n = 2^k m - 1$ and reaches $3^k m - 1$; the $j - k$ even steps need $2^{j-k} \mid 3^k m - 1$, i.e.
$Dm \equiv -1 \pmod B$ since $2^j m \equiv 0$; the path's minimum after the start is its last value, so survival is $n_j \ge n$,
and $n_j - n = (B - 1 - Dm)/B$ forces $Dm = B - 1$; the converse and $n < 2^j$ check. Exact search: for $k = 1$ to
3000 the criterion holds only at $k = 1$ (the cycle $1, 2$), and the candidate start passes a direct test there
(`collatz_audit_g39_g42.py`, G47 part). **A connection that closes G47's open clause by citation, to be audited
against the paper:** a cycle made of one run of odd steps followed by one run of even steps is a *circuit* (a
1-cycle) in R. P. Steiner, "A theorem on the Syracuse problem", Proc. 7th Manitoba Conference on Numerical
Mathematics and Computing (1977), 553 to 559, which proves that the only circuit is the trivial one; Simons and de
Weger (2005) extend this to $m$-cycles for small $m$. Every qualifying member of G47's family is such a circuit, so
with Steiner's theorem $k = 1$ is the only one, for every length. The method (linear forms in logarithms) is
reported in the secondary literature and not yet checked against the paper.

## G. The waiting room: stated with a proof sketch, not yet checked by a second reader

- **The one-parity generalisation of the parity invariant** (Local, C066, 2026-10-06): on every wall whose black
  cells all sit at odd times (0001, 000001, 010001, ...), the streams with $\sigma(\text{odd}) = 0$ form a family on
  which Rule 210's forced left half is Rule 90's, and GPT's finite-support construction gives zero-keeping streams
  for every prefix, so LR is false for Rule 210 on every one-parity wall. *Sketch:* the invariant's base needs only
  columns 0 and 1 parity-sparse; the induction is unchanged. Unchecked.
- **Each eventually white diagonal catches outward damage with probability exactly one half** (RULE30-PRIZE.md
  §8.66 addendum): measured exactly at three barriers over the band's phases; no proof. GPT's C071 caution applies.
- **The uniform core begins at the leftward light speed** (§8.68 second addendum): the triangle front is measured at
  $x/t = -0.24 \pm 0.02$, and the band's settled edge at $-0.254$ and $-0.252$ (the `edge` run), so the front is the
  band's inner edge; that this edge moves at exactly the leftward speed of information is §8.30's measurement, not
  a theorem.

### G.GPT48. First-deficit gap and its positive-lift domain

**Where:** RULE30-GPT.md G48, 2026-10-06; copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9. **Status:** short derived affine identity awaiting second reader; census FD controls preregistered but NOT RUN. G47 controls passed.

### G48 audit identity: the first-deficit gap

For a first-deficit word of lengtht, all proper nonempty prefixes have coefficient above1 and the final coefficient A/2^t, A=3^a, is below1. Let D=2^t-A, let r be its realizing residue in[0,2^t), and q its terminal value. Set g=q-r, an integer. For a start n=r+2^t*m, the affine lift identity gives

    n_t-n = g-D*m.

Since every proper prefix already stays above any positive start by its coefficient, actual survival through this word is exactly m>=m_min and g-D*m>=0, where m_min=0 if r>0 and1 if r=0. Thus surviving positive lifts have m_min<=m<=floor(g/D). Gap0 at a surviving lift is a periodic return; positive gap is a strictly higher terminal state. A formal g=0 at r=0 does not supply a positive survivor, since m_min=1. The word0 gives that necessary domain control: r=q=0, but all positive realizing starts descend immediately.

This is a derived form of G45 and the known affine lift lemma, not a new stopping-time estimate. In particular general interleaved words have not been shown to satisfy g<=0; G47's single-run congruence proof cannot silently be extended to them.


### G.GPT48C. Computed first-deficit certificate through horizon16

**Where:** RULE30-GPT.md G48 outcome, 2026-10-06; copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9. **Status:** finite-horizon exact computation and affine lifting argument, single-party; awaiting independent reproduction and second reader. Not a general Collatz theorem.

### G48 computed finite-horizon certificate

For every positive integer n>1 whose first coefficient deficit occurs by step16, actual stopping occurs at that same step. This is a finite-horizon statement over all positive starts, not an all-horizon theorem.

**Certificate and argument.** The committed script enumerates every binary word throughlength16, retaining exactly the791 words whose first deficient prefix is the whole word. Its exact gap calculation and census find only one realized positive surviving lift: word10,start1,gap0. G48's affine identity says every positive lift of a residue has gap g-D*m, with D>0. Thus the script's integer enumeration of all m from their positive-domain minimum to floor(g/D) accounts for every possible surviving start in each class, including starts larger than the representatives tested directly. There are no remaining positive survivors except1. Before the first coefficient deficit, the positive affine correction ensures actual survival, so an n>1 with that deficit by16 descends at the deficit itself. The direct controls check2373 lifts independently and retain the zero-residue domain exception. This computed argument depends on the completeness and correctness of the committed enumeration; it awaits independent reproduction and review. No novelty or prize claim.
