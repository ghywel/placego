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

*For a general reader: [proofs/README.md](proofs/README.md) gives every entry its own page, opening with a summary
in plain words, built from this file by `python3 proofs/build.py`. A new entry needs its summary in
[proofs/summaries.md](proofs/summaries.md); the build names any that are missing and writes nothing until they
exist (Cloud, 2026-10-06, at the owner's request).*

## Generality index (Local's audit, 2026-10-06; Cloud's CL002 split)

What each Rule 30 entry's proof actually uses about the wall. "Any trace" means any column 0 at all, periodic or
not; "any periodic word" means any word of any period; "0101" means the period-two wall only. "Extends to" says what
the same proof gives with no new idea, and whether that was checked (✓ written out here or in the entry; ~ plausible,
not written out). Rule 210, Rule 90 and the Collatz entries are marked by their own scope.

| Entry | As stated | What the proof uses | Extends to |
|---|---|---|---|
| A1 Lemma 1 (invisibility) | any trace | the inverse rule at column $-1$ only | any trace ✓ |
| A2 Lemma 2 (rotations) | any exactly periodic word | one time step shifts the word | any periodic word ✓ |
| A3 Lemma 3 (two right-side rules) | any trace | Rule 30 at column 1 | the two rules: any trace ✓; "no two visible ones in a row" is 0101's |
| A4 Lemma 4 (newest bit as XOR) | any trace | unwinding the inverse rule | any trace ✓ |
| B5 Theorem A (window and edge) | any configuration, any column pair, any period $P$ | the edge's speed and periodicity moving left | general ✓ |
| B6 Theorem B (zero runs) | columns 0 and 1 periodic, $P \ge 2$, column 0 not zero | $P \ge 2$ places depth $d + P - 2$ inside the run | every period $p \ge 2$, any periodic pair ✓ |
| B7 Theorem A′ | any configuration | as Theorem A | general ✓ |
| B8 Lemma B1, B9 Lemma B2 | the diagonals of any left-bounded row | the diagonal recurrence | general (the band is wall-independent) ✓ |
| B10 Theorem A‴, B12 Lemma B3, B13 Theorem A⁗ | any configuration with a settled band | the window and the band | general ✓ |
| B11 Corollary F (near-squares) | 0101 | the pair $(-1, 0)$ repeats at shifts $2(i' - i)$ because column $-1$ is constant at odd times | any nonconstant periodic wall, for phase-aligned period blocks: GPT's G52, second-read ✓ |
| B14 Theorem E, B15 Theorem E″ | 0101, visible bits a rotation coding | the wall's visible times are the even times | 0101 only as audited |
| B′16 Proposition 5 | Rule 90, period two | $x_{2^n + s}(0) = x_s(-2^n) \oplus x_s(2^n)$ | Rule 90 with any periodic nonzero column 0: the identity gives long white stretches ✓ (standard for linear rules) |
| B′17 Proposition 7 (Jen) | column 0 eventually periodic and not eventually zero; column 1 eventually periodic | Jen's mechanism | general for Rule 30 ✓ |
| B′18 the parity invariant | Rule 210, 0101 | the parity of the wall's black times | one-parity walls: in the waiting room |
| B′19 the squeeze | 0101 | step 1, the certified channel for 0101; step 2, column $-1$ is 1 at odd times | every periodic wall, coarsely: GPT's G53 (period-block conversion) and G54 (gap-matrix bound $\log_2 \rho(M)/p$), second-read ✓; a sharp bound for a wall still needs its own deeper-layer certificate |
| B′20 Proposition 6 (the wheel) | 0101 | a computation | 0101 only |
| C.1 checkerboard, C.2 latch | any trace (a black stretch; a white time) | one rule step | any trace ✓ |
| C.3 shrink, C.4 speed identity | any configuration | one rule step; the diagonal recurrence | general ✓ (the speed's numbers are the background's) |
| C.5 triangle law | the uniform measure | surjectivity | general for the measure ✓ |
| C.6 prime-ring gliders | Rule 30 on prime rings | rotation commutes with the rule | any rule on prime rings ✓ |
| C.7 affine columns | 0101 | the table | 0101 only |
| E.1 G13.2, E.2 G13.5 | the one-hole family (a hole then $p - 1$ black cells) | as stated | the one-hole family |
| E.3 G17.1 | $0\,1^{p-1}$, every $p \ge 2$ | as stated | every $p$ |
| E.4 G18.2 | $0^a 1^b$ | as stated | slow walls |
| E.5 G18.3 | any wall with a black run of length $b$ | as stated | any wall with a long black run ✓ |
| E.6 G20.1 | $0\,1^{p-1}$, odd $p \ge 5$ | as stated | odd one-hole walls |
| E.7 G27.2 (Jen/Kopra, half-line) | Rule 30 on any nonconstant periodic wall; Rule 210 on 0101 | as stated | general for Rule 30 ✓ |

**What the audit says.** The wall-form lemmas, the window principle (Theorems A, A′, A‴, A⁗), the zero-run bound
(Theorem B), the band (B1 to B3), Jen and the short proofs of section C already hold for every wall, most for every
trace. What is period-two-specific is a short list: the channel certificate and the squeeze built on it, the wheel
(Proposition 6), the rotation-coding exclusions (Theorems E, E″), the affine columns, and Corollary F as written. So
a proof that wanted to leave period 2 would carry almost all of the machinery with it, and would need, for each new
wall, its own channel certificate. Both "~" extensions are now written out and second-read: Corollary F for phase-aligned period blocks (G52) and a
coarse squeeze for every periodic wall (G53, G54). What remains period-two-specific is the sharp channel constant.

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

*Correction (Cloud, 2026-10-06): the copy above was cut off mid-sentence. The source, RULE30-PRIZE.md §8.2, ends the note: "so they are not vacuous)."*

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

*Correction (Cloud, 2026-10-06): the copy above was cut off mid-sentence. The source, RULE30-PRIZE.md §8.2, ends the note: "P2 in `rule30_linear_cell.py` (7 words, 50 random
columns 1, every depth to 192: no violation; the counterfactual 'the flip changes only $L(k)$' is caught)."*


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

*Note (Cloud, 2026-10-07, the duplicate sweep): the first half of this lemma is the first of Lemma 3's two rules
(entry 3, from §8.2 on 2026-10-04), proved the same way; it was filed here from §8.62 without a cross-reference. What
C.2 adds is the equality $x_{t+1}(1) = x_t(1) \vee x_t(2)$ and its iteration across a white stretch.*

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
*Status:* proved (the pigeonhole); the distinctness of lengths at $n = 13, 17, 19, 23$ and 29 is the census's exact finding (§8.67 and its addendum). GPT's G55 (second-read, §E2) refines it to an exact criterion: lengths are distinct exactly when every nonconstant quotient cycle has nonzero rotation displacement and the quotient periods are distinct.

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


### C.8 Rule 30's velocity is Rule 210 (RULE30-PRIZE.md §8.70; 2026-10-06)

*Where:* §8.70 (the owner's question about velocity and acceleration). *Bears on:* why Rule 210 is Rule 30's closest
sibling; the prize as a difference equation over GF(2). *Status:* proved.

**Proposition.** $x_{t+1}(i) \oplus x_t(i) = x_t(i-1) \oplus (\lnot x_t(i) \wedge x_t(i+1))$ for Rule 30, i.e. Rule 30 $= c \oplus$ Rule 210.

*Proof.* $l \oplus (c \vee r) = l \oplus c \oplus r \oplus cr$, and $l \oplus r \oplus cr = l \oplus (\lnot c \wedge r)$. $\square$

## E. Theorems proved by GPT (statements verbatim; the proofs are in RULE30-GPT.md at the section named)

GPT's lane is its own file. The statements are copied so that this list is complete; GPT is asked to append its
proofs here in its own words, or to say which it would rather keep as pointers.

### E.1. G13.2. Complete reset language, with a failed first characterization retained

*Where:* RULE30-GPT.md, "G13.2. Complete reset language, with a failed first characterization retained". *Status:* proved by GPT (proof there).

**Theorem.** A finite driver word resets exactly when it contains a factor

*Correction (Cloud, 2026-10-06): the copy above was cut off mid-sentence. The statement in RULE30-GPT.md G13.2 continues with the factor:*

```math
 0\,1^{3k+1}\,0\,z,\qquad k\ge0,\quad z\in\{0,1\}.
```

### E.2. G13.5. Several backward steps, with the protected window's exact cost

*Where:* RULE30-GPT.md, "G13.5. Several backward steps, with the protected window's exact cost". *Status:* proved by GPT (proof there).

**Theorem.** Suppose a wall has a hole at q and then p−1 black cells, with no premise on its
values outside that window. Compare two right columns differing only at q. For any integer
r with $0\le r\le q$ and $p\ge3r+5$, their rows at q−r agree at **every** depth≥4r+4. In
addition their common cells in the interval

*Correction (Cloud, 2026-10-06): the copy above was cut off mid-sentence. The statement in RULE30-GPT.md G13.5 continues:*

```math
 [4r+4,\ p-1+r]
```

*are the checkerboard: black at even depths and white at odd depths. The interval's length is p−4−3r; each
backward step consumes three cells of this protected window. All other right-column inputs, and the wall before
and after the specified window, are arbitrary and common to the two constructions.*

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

*Correction (Cloud, 2026-10-06): the copy above was cut off mid-sentence. The statement in COLLATZ-PRIZE.md §4 continues:*

```math
0 \le T^k(r) < 3^a \qquad\text{and}\qquad T^k(2^k m + r) = 3^a m + T^k(r) \ \text{ for every integer } m .
```

### F.2. Dubickas's theorem (external; the record's W2)

*Where:* COLLATZ-PRIZE.md §5; PRIOR-ART.md. *Status:* a published theorem (A. Dubickas, 2009, Theorem 5), read in
full and credited; the record's "complexity at least $1.70951129\,n$" statement for divergent integer orbits is
its restatement, and GPT's G29 audits its extension to signed rationals with the hypotheses named.


## E2. GPT's proofs G39 to G202, second-read by Local (moved from the waiting room, 2026-10-06)

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

### G.GPT48. First-deficit gap and its positive-lift domain

**Where:** RULE30-GPT.md G48, 2026-10-06; copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9. **Status:** short derived affine identity, second-read by Local, 2026-10-06 (note below the certificate). G47 controls passed.

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

*Second reader's note on G48 and its certificate (Local, 2026-10-06; chat L018).* The identity is correct: with
$n = r + 2^t m$, $n_t = q + A m$, so $n_t - n = g - Dm$; every proper prefix has coefficient above 1 and so already lifts
any positive start, which makes survival exactly $g - Dm \ge 0$ with the stated $m_{\min}$. The certificate was
reproduced independently with my own code (`collatz_audit_g39_g42.py`, G48 part): exactly 791 first-deficit words
of length at most 16, and over all of them the only surviving positive lift is the word 10 with start 1 and gap 0;
and, separately, a brute-force scan of every start $1 < n < 2^{22}$ finds none whose coefficient deficit comes by
step 16 without its actual stopping at that step. So the finite-horizon statement is replicated, by two methods.
It is the coefficient stopping time conjecture checked to horizon 16, which GPT identifies as known (G014); the
literature verifies it much further, so the value here is the exact gap form, not the horizon.

### G.GPT49. Scope of the floor(3n/2) test bed

**Where:** RULE30-GPT.md G49, 2026-10-06; copied verbatim. **Bears on:** PRIZE-PROBLEMS.md §8, Antihydra tool transfer. **Status:** analytic map/counter/coin calculation, second-read by Local, 2026-10-06 (note below); AH1-AH4 finite controls pass (G49 outcome). Machine reduction is reported from the project source, not independently machine-verified.

### G49 theorem and proof: floor(3n/2) preserves coding but changes survival

Let H(n)=floor(3n/2) on nonnegative integers. Write b=n modulo2. Then H(n)=(3n-b)/2. Every n>=2 strictly increases, since H(n)-n=floor(n/2)>=1;0 and1 are fixed. Therefore the count of positive w-bit starts staying above their start is2^(w-1) for every horizon, rather than exponentially decaying. This does not settle a parity-counter halting problem.

For a word b_0,...,b_(t-1), define C_0=0 and C_(j+1)=3*C_j+b_j*2^j. Then

    2^t*H^t(n) = 3^t*n-C_t.

The word is realized by exactly one residue r modulo2^t, namely r=C_t*(3^t)^(-1) modulo2^t. Prefix congruences and integrality force the prescribed parities just as in G45. Lifting a start by2^t*m adds3^t*m to its terminal value. For0<=r<2^t, nonnegativity and C_t>=0 give0<=H^t(r)<3^t. Thus the parity bijection, affine lift and finite-residue binary reader transfer, with modulus3^t independent of the odd count. G43/G44's reader identities can be used with that law; none supplies a pointwise orbit theorem.

**Actual test-bed event.** In the reported Antihydra reduction, the initial value is H_0=8 and a counter starts at0, gains2 when H_j is even and loses1 when it is odd. Writing a_t for the odd count, its value aftert steps is2t-3a_t. Avoiding halt throughT requires2t-3a_t>=0 at every prefix, since the only negative crossing is to-1. This upper-odd-density barrier differs from Collatz's coefficient lower-density barrier. Strict growth of H says nothing by itself about it: seed3 grows but makes the zero counter hit-1 immediately. The reduction is cited from the project source; the original six-state Turing-machine transition simulation has not been independently verified here.

**The fair-coin analogue does not have exponential survival decay.** Let iid bits drive counter increments+2 for0 and-1 for1. Put r=(sqrt(5)-1)/2, so r^2+r=1. For counter c>=0, h(c)=r^(c+1) obeys(h(c+2)+h(c-1))/2=h(c), and h(-1)=1. Stopping at the first hit of-1 or at finiteT gives expectation h(C_stopped)=r at initial counter0: this follows by successive conditional expectation, with no unbounded stopping theorem. On paths that hit, h=1; on other paths h>=0. Hence P(hit byT)<=r and P(surviveT)>=1-r>0 for everyT. No assumption about H^t(8)'s actual parity distribution is made. Uniform starts modulo2^T realize all T-bit words once, so the same lower bound holds for that finite initial ensemble. It does not determine the selected start8. Thus transferring the Collatz coin's decaying survival target to this barrier is mathematically invalid.

*Second reader's note on G49 (Local, 2026-10-06; chat L021).* Correct. $H(n) = (3n - b)/2$ and
$H(n) - n = \lfloor n/2 \rfloor$; the identity $2^t H^t(n) = 3^t n - C_t$ follows by induction
($2^{t+1} H^{t+1} = 3 \cdot 2^t H^t - 2^t b_t$); the residue, the lift by $3^t m$ and $0 \le H^t(r) < 3^t$ check;
the counter is $2t - 3a_t$; and $h(c) = r^{c+1}$ is harmonic for the walk that adds 2 or subtracts 1, because
$r^3 - 2r + 1 = (r - 1)(r^2 + r - 1) = 0$, so the stopped expectation gives $P(\text{survive } T) \ge 1 - r$. Checked
exactly: the identity and residue law for every $n < 3000$ and $t \le 20$, and the fair-coin survival probability
by exact dynamic programming, $0.5$, $0.4023$, $0.3822$ at $T = 1$, 10, 60, every value above $1 - r = 0.3820$
(`collatz_audit_g39_g42.py`, G49 part). The Antihydra reduction itself is, as G49 says, taken from the project
source and not machine-verified here.

### G.GPT50. Mahler itinerary coupling and alphabet scope

**Where:** RULE30-GPT.md G50; proof copied verbatim. **Status:** second-read by Local, 2026-10-06 (note below G51); corrected MA controls pass, initial phase-order failure retained in G50 outcome. Established decoupling specialized; no novelty or Z-number nonexistence claim.

### G50 theorem and proof: Mahler needs both itineraries, and a different alphabet

Write xi*(3/2)^j=n_j+u_j, with integer n_j>=0 and0<=u_j<1/2 at every j. If b_j=n_j modulo2, direct separation of integer and fractional parts gives

    n_(j+1)=(3*n_j+b_j)/2=ceil(3*n_j/2),
    u_(j+1)=(3*u_j-b_j)/2.

For even n_j, the half-interval condition forces u_j<1/3; for odd n_j it forces u_j>=1/3, wrapping the fractional part once. Iterating the second recurrence backwards and using the bounded tail yields

    u_j=sum_(k>=0) b_(j+k)*2^k/3^(k+1).

Conversely, start from a nonnegative integer n_0 and its ceil-map parity itinerary. Define u_j by this convergent series. If every u_j<1/2, the series gives3*u_j= b_j+2*u_(j+1). Combining this with the integer recurrence shows n_j+u_j=xi*(3/2)^j, xi=n_0+u_0. Provided xi>0, this is a Z-number. Thus the fractional-tail restriction and ordinary-integer itinerary realization are both required. No lower coefficient-deficit ceiling arises, since the integer coefficient is(3/2)^t at every prefix. This is the established decoupling mechanism, specialized here; no novelty claim.

Two consecutive ones are forbidden: their contribution to u_j is at least1/3+2/9=5/9>1/2. This finite forbidden word does not establish emptiness. Unexpected scope control: the purely periodic formal word(100)^infinity has tail values9/19,4/19,6/19, all below1/2, and satisfies the fractional recurrence exactly. It nevertheless cannot be the itinerary of any nonnegative integer start. A period100 has the integer branch map n -> (27*n+9)/8. After k periods integrality implies

    19*n_0+9 = 0 modulo8^k.

Indeed8^k*n_(3k)=27^k*n_0+9*(27^k-8^k)/19, and27 is invertible modulo8^k. Divisibility for every k forces19*n_0+9=0, impossible for a nonnegative integer. The compatible 2-adic value-9/19 is not an ordinary integer start. Formal fractional admissibility alone is therefore insufficient, even when every tail obeys the strict half-interval bound.

For the actual base-six CA, Kari–Kopra define g(x,y)=3*(x modulo2)+floor(y/2) and f(x,y,z)=g(g(x,y),g(y,z)). Fix y,z and vary x in{0,...,5}. The output depends only on x modulo2, so this six-letter local rule is not left-permutive in the usual full-alphabet sense. Both parity choices give distinct outputs: the inner value changes by3, its parity flips, and the outer value changes by3. There are exactly two outputs, not six. Membership in a broader expansive class must not be substituted for the binary left-invertibility used in our wall proofs. Canonical base-six expansions encode the strict fractional half-interval by a first fractional digit in{0,1,2}; the selected real configurations also require an eventually-zero integer-side tail. Arbitrary bi-infinite traces discard that realization requirement.

### G.GPT51. Exact finite Mahler coupling window

**Where:** RULE30-GPT.md G51; copied proof. **Status:** second-read by Local, 2026-10-06 (note below); GPT's MW1-MW3 finite controls pass (G51 outcome).

### G51 lemma and proof: exact finite Mahler coupling window

Fix a T-bit word b_0,...,b_(T-1). Put C_0=0 and C_(t+1)=3*C_t+b_t*2^t. Prescribed ceil branches and fractional branches give

    2^t*n_t=3^t*n_0+C_t,
    2^t*u_t=3^t*u_0-C_t.

The integer word is realized by the unique nonnegative residue r_T=-C_T*(3^T)^(-1) modulo2^T. This follows from prefix congruences and integrality, as in G49 with the sign reversed. The allowable initial fractions through timeT form the half-open interval

    I_T=[L_T,U_T),
    L_T=max_(0<=t<=T) C_t/3^t = C_T/3^T,
    U_T=min_(0<=t<=T) (C_t+2^(t-1))/3^t,

with the t0 upper endpoint interpreted as1/2. If L_T>=U_T it is empty. The lower equality follows because C_t/3^t is a partial sum of nonnegative terms b_j*2^j/3^(j+1). These inequalities are precisely0<=u_t<1/2 for all prefixes. Consequently every n_0=r_T+2^T*m>=0 paired with u_0 in I_T satisfies the finite Z-number condition throughT, except xi=n_0+u_0=0 is excluded. The recurrence in G50 proves both necessity and sufficiency; no independent parity or randomness assumption is needed.

Across increasing T for a single infinite word, realizing residues satisfy r_(T+1)=r_T or r_T+2^T. They therefore form a nondecreasing integer sequence. An ordinary nonnegative integer realizes the infinite itinerary if and only if these least residues are bounded: bounded monotone integers stabilize, and the stabilized value realizes every prefix; conversely a realizing integer has r_T equal to itself once2^T exceeds it. This makes the missing integer compatibility an explicit boundedness condition, separate from nonemptiness of the fractional intersection. No boundedness theorem for Mahler-admissible words is supplied.

Unexpected finite exclusion:10101 contains no11, but its terminal lower endpoint is133/243>1/2. Its fractional window is empty. Thus the simple no11 subshift from G50 is a strict overestimate of the fractional language; checking only adjacent forbidden bits is insufficient. These are elementary specialized forms of the already recorded decoupling/residue tools, not a new Mahler nonexistence proof.

*Second reader's note on G50 and G51 (Local, 2026-10-06; chat L022).* Both correct. G50: separating integer and
fractional parts of $\tfrac32(n_j + u_j)$ gives $n_{j+1} = \lceil 3n_j/2 \rceil$ and $u_{j+1} = (3u_j - b_j)/2$, with
$u_j < 1/3$ forced at even $n_j$ and $u_j \ge 1/3$ at odd; the tail series and its converse hold; two adjacent ones
force $u \ge 5/9$; the $(100)$ tails are $9/19$, $4/19$, $6/19$ in that order (G018's corrected order); and the
integer obstruction $19 n_0 + 9 \equiv 0 \pmod{8^k}$ follows because 19 and 27 are invertible modulo $8^k$. The
base-six rule's two outputs check for every $(y, z)$; that this is Kari and Kopra's rule is taken from the source,
not checked here. G51: both affine identities by induction; the window is exactly $0 \le u_t < 1/2$ for every
prefix, with $L_T = C_T/3^T$ because the partial sums increase; the residues are nondecreasing and stabilise
exactly when an ordinary integer realises the word; $10101$ gives $133/243 > 1/2$. Exact checks
(`collatz_audit_g39_g42.py`, G50/G51 part): for every word of length at most 12 with a nonempty window (588
words), $\xi = r_T + L_T$ was multiplied by $(3/2)^t$ in exact rationals, and its integer parts follow the word's
parities and its fractional parts stay in $[0, 1/2)$ through $T$; no $n_0 < 200$ passes the $8^6$ congruence.

### G.GPT52. Phase-aligned period-block extension of Corollary F

**Where:** RULE30-GPT.md G52; copied proof. **Status:** second-read by Local, 2026-10-06 (note below); GPT's MF controls not run at publication. The original index's plausible extension is not promoted before review.

### G52 theorem and proof: Corollary F for phase-aligned period blocks

Let a nonconstant Rule30 wall tau have period p>=2 from time0. For each period m, let v_m be the vector of column1 bits at the white phases within times pm,...,pm+p-1, in phase order. Suppose there is a fixed integer K>=0 and pairs i_j<i'_j with i'_j-i_j tending to infinity for which the vectors v at these indices have a common future of at least ell_j periods, with ell_j>=i'_j-K. Then the forced left half cannot have an initially finite nonempty black support.

Proof. Assume finite support and let its leftmost black cell be at depth L. The universal band lemma B2 supplies an eventually-black diagonal b>=L+pK, black from time t_b. Matching white-phase vectors for ell_j complete periods makes the column pair(-1,0) identical for p*ell_j times from a=pi_j and a'=pi'_j. This follows directly from Lemma1: at a white phase the left neighbour depends on the matching visible bit, and at a black phase it is independent of that bit; tau(t) and tau(t+1) agree because both shifts are multiples of p. Choose j so p(i'_j-i_j)>b and pi'_j>=t_b. Theorem A triple-prime with distance L-1 from the leftmost black cell to column-1 gives

    p*ell_j <= L-1+pi'_j-b <= pi'_j-pK-1,

contradicting ell_j>=i'_j-K. This reuses the checked half-line versions of Lemma1, B2 and the window principle; no full right-half realization is required. For0101 there is one white phase per period and this is Corollary F's existing statement. It is a derived extension, without a novelty claim. Empty initial left rows are not included in this stated version; their forced first birth and time shift need a separate scope check.

Phase alignment matters. For wall001 and visible bits all0, Lemma1 gives column-1 values0,1,1 at phases0,1,2. Shifting by one visible-bit index exchanges the two white phases (physical times0 and1), whose left-neighbour values differ. Identical visible-bit futures alone therefore do not justify repeating the pair at those physical shifts. The block statement above supplies the missing alignment. It does not prove that an arbitrary near-square in the ungrouped visible sequence can be aligned, nor supply a new channel/squeeze certificate.

### G52 addendum: the empty initial left row is covered

The phase-aligned period-block theorem also excludes an empty initial left row. A nonconstant cyclic binary wall has a phase j in[0,p-1] with tau(j)=1 and tau(j+1)=0. Lemma1 forces x_j(-1)=1 there, independently of column1. Starting from an empty left row, every finite-time left row has finite support by the local update rule. Once a leftmost black cell exists, it advances left at each subsequent step: the new cell just left of it has input100 and Rule30 outputs1. Consequently the left row at time p is finite and nonempty.

Shift the whole forced evolution forward by p. Its wall has the same phase and its period-block word is v'_m=v_(m+1). The near-square hypothesis persists with slack K+1. For any sufficiently long original pair(i,i',ell), if i>=1 use shifted indices(i-1,i'-1) and the same length ell. If i=0, discard the first common block and use shifted indices(0,i') with length ell-1. In both cases the gap still tends to infinity and the new common length is at least its later shifted index minus(K+1). G52's proved nonempty-row case now contradicts finiteness of the shifted row. This completes the initially-empty case without assuming a realized full right half. The original limitation above records the first scoped version; this addendum removes it by an explicit time-shift argument.

The statement still requires phase-aligned period-block repeats. It does not exclude all unaligned visible-bit near-squares or solve any Rule30 prize question. This is a derived extension of the checked band/window lemmas, awaiting independent review.

**G52 control status:** MF1-MF2 pass50 walls/288 samples/8016 transitions; analytic extension and empty-row addendum independently read by Local (L023/L024).

*The addendum above was written by GPT after Local's first reading below; Local second-read it the same day
(chat L024): correct. A nonconstant wall has a phase with black then white, where Lemma 1 makes column $-1$ black
whatever column 1 is; the leftmost black cell then persists and moves left ($100 \to 1$), so the left row at time
$p$ is finite and nonempty; shifting by one period keeps the near-square hypothesis with slack $K + 1$, using indices
$(i - 1, i' - 1)$ when $i \ge 1$ and $(0, i')$ with length $\ell - 1$ when $i = 0$; the nonempty case then applies.*

*Second reader's note on G52 (Local, 2026-10-06; chat L023).* Correct. Matching white-phase vectors over $\ell_j$
complete periods at shifts that are multiples of $p$ make the pair $(-1, 0)$ identical over $p\ell_j$ times, by
Lemma 1 and the periodicity of $\tau$ (including $\tau(t+1)$ at a block's last time); Theorem A‴ at distance
$L - 1$ with $b < p(i'_j - i_j)$ black at time $p\,i'_j$ gives $p\ell_j \le p\,i'_j - pK - 1$, against
$\ell_j \ge i'_j - K$; such $j$ exist because $i'_j - i_j \to \infty$. The 001 example checks (column $-1$ reads
0, 1, 1 at the three phases with column 1 white). Checked: the window-matching step on 1,764 random nonconstant
walls of periods 2 to 9 with arbitrary bits at black phases, zero failures (`rule30_audit_g52.py`). GPT's own MF1 and MF2 controls (`tests/probes/rule30_gpt_period_blocks.py`) replicated unchanged by Local on
2026-10-06 at 05f1619: 50 walls, 288 samples, 8,016 transitions, and the 001 misalignment.

### G.GPT53. Period-block form of the entropy squeeze

**Where:** RULE30-GPT.md G53; copied proof. **Status:** second-read by Local, 2026-10-06 (note below G54). No new numerical certificate claimed.

### G53 lemma and proof: period-block entropy conversion

Fix a period-p wall tau, with z white phases per period. Let v_m be the z-bit vector of column1 at those phases during period m, and let pi be column-1. For a one-sided sequence s, let P_s(n) count its distinct contiguous n-symbol words, and h(s)=limsup log2(P_s(n))/n. The vectors v are symbols in an alphabet of size2^z. Then

    h(pi)=h(v)/p,
    h(column -k)<=h(v)/p for every fixed k>=1.

At each white phase, pi(t)=tau(t+1) XOR sigma(t), so its p-symbol period block determines v_m uniquely. At each black phase, pi(t)=tau(t+1) XOR1 is fixed. Therefore period blocks of pi and symbols v are in bijection. Every n-vector word supplies a distinct aligned pn-bit pi word, giving P_v(n)<=P_pi(pn). Every m-bit pi word is determined by its start phase and at most ceil(m/p)+1 consecutive v symbols. Extend shorter determining words to this common length using the infinite future; hence P_pi(m)<=p*P_v(ceil(m/p)+1). Taking the two limsup bounds proves the equality.

Repeated scalar inversion computes column-k over m times from pi and tau over at most m+k-1 times. There are p possible start phases of tau. Thus a deliberately loose uniform bound is

    P_(column -k)(m)<=p*P_v(ceil((m+k-1)/p)+1).

This proves the entropy inequality, since fixed finite lookahead and the phase factor disappear after division by m. In particular h(v)<=z gives the elementary bound z/p bits per physical step. If an independently certified per-period vector language obeys P_v(n)<=C*lambda^n, the bound improves to log2(lambda)/p. That hypothesis needs a certificate for the chosen wall; the0101 certificate does not establish it for another wall. With p2,z1 this recovers the established squeeze conversion, apart from deliberately looser finite constants.

Unexpected scope check: for wall001 and all white-phase bits0, pi is the periodic word011 independently of every right bit at a black phase. Across N periods there are2^N choices of those invisible bits and only one pi prefix. Counting all column1 bits rather than its visible period vectors can therefore lose the exact entropy equality. This is an algebraic family of formal boundary inputs; no assertion that all these inputs admit full right-half realization is made.

This is the period-block form of RULE30-PRIZE.md section8.33 proof steps2-4, not a new channel certificate or a positive lower entropy bound for a finite seed. It leaves the fixed-seed cost and left/right compatibility gaps open.

### G.GPT54. Gap-matrix coarse squeeze for every periodic wall

**Where:** RULE30-GPT.md G54; copied proof. **Status:** second-read by Local, 2026-10-06 (note below). Reuses G14/G15; no new channel data.

### G54 corollary and proof: coarse squeeze for every periodic wall

Let tau have period p and at least one white phase. List its white phases cyclically, let g_1,...,g_z be the positive gaps between consecutive white times (including the wrap gap), and put

    M=B_(g_1)*...*B_(g_z),
    B_1=A=[[1,1],[0,1]],
    B_2=F=[[1,1],[1,0]],
    B_g=J=[[1,1],[1,1]] for g>=3.

Then every fixed column to the left of the wall has entropy at most log2(rho(M))/p, where rho is the spectral radius.

G15 proves these are the exact allowed visible pairs in the width-one relaxation with an independently chosen next-right input. Its language contains every actual right-column visible itinerary. A word of n complete periods has nz visible symbols; its pair constraints use n cyclic matrix products apart from fixed endpoint factors. Equivalently counts are obtained from M^(n-1) with fixed nonnegative two-state boundary factors. Their growth is at most a constant times(n+1)*rho(M)^n, allowing a Jordan block; rho(M)>=1 because the all-zero visible path is allowed. Thus the period-vector entropy is at most log2(rho(M)). G53 propagates the bound to every fixed left column and divides by p physical steps per period. No equality is asserted for an actual orbit. If the wall has no white phase, its left-neighbour trace is periodic and all fixed left columns have entropy0 by inversion.

The same bound is independent of which white phase starts the product: cyclic products have the same trace and determinant, hence the same characteristic polynomial in this two-state case. For an explicit exact value, with t=trace(M),d=det(M), rho(M)=(t+sqrt(t*t-4*d))/2. These nonnegative products have real eigenvalues since the discriminant equals(a-d_entry)^2+4bc>=0. This algebraic value is an upper bound from the relaxation, not a new large-layer certificate.

For wall0^(p-1)1, the product A^(p-2)F=[[p-1,1],[1,0]] recovers G14's bound log2(((p-1)+sqrt((p-1)^2+4))/2)/p. For the one-hole wall01^(p-1) with p>=3, it is J and gives1/p. Neither closes the single-orbit information-cost gap.

Unexpected units check: G14's p8 visible rate0.354491897 is already per physical step, so it bounds fixed left-column entropy directly; dividing it by8 again would be wrong. G15's period8 examples00111111 and01101111 instead have per-period roots3 and4, so the respective physical bounds are log2(3)/8 and2/8. White fraction alone does not determine this certificate. These examples and calculations are reused from G14/G15, without a new experimental or novelty claim.

*Second reader's note on G53 and G54 (Local, 2026-10-06; chat L026).* Both correct. G53: at a white phase
$\pi(t) = \tau(t+1) \oplus \sigma(t)$ and at a black phase $\pi(t)$ is fixed, so aligned period blocks of $\pi$
correspond one to one with the vectors $v$; $P_v(n) \le P_\pi(pn)$ and $P_\pi(m) \le p\,P_v(\lceil m/p \rceil + 1)$ give
$h(\pi) = h(v)/p$ (the lower bound along $m = pn$ suffices for the limsup), and column $-k$ over $m$ times needs
$\pi$ over $m + k - 1$ times and one phase, so it inherits the bound. G54: G15's gap matrices bound a superset of
every actual visible itinerary; cyclic products share trace and determinant; the discriminant $(a - d)^2 + 4bc$ is
nonnegative; and the examples check exactly: for $0^7 1$ the product $A^6 F$ has spectral radius $(7 + \sqrt{53})/2$
and gives $0.354491897$ bits per step, **exactly G14's recorded rate**, which confirms the units; $00111111$ and
$01101111$ give $\log_2 3/8$ and $2/8$; the one-hole walls $1/p$; and $0101$ gives $\log_2 \varphi / 2 = 0.3471$, the
coarse bound that the certified $0.0618$ improves on (`rule30_audit_g53_g54.py`, all checks pass). With these two
entries the Generality index's last "~" is resolved for a coarse bound: every periodic wall has a squeeze; a sharp
one needs a deeper-layer certificate per wall.

### G.GPT55. Prime-ring quotient cycle lifting

**Where:** RULE30-GPT.md G55; copied proof. **Status:** second-read by Local, 2026-10-06 (note below); GPT's RQ1-RQ3 finite controls pass.

### G55 lemma and proof: prime-ring cycle lifting

Let R be rotation of a binary ring of prime size p, and let F commute with R. Nonconstant states have free rotation orbits of size p: a stabilizing nonidentity rotation generates the prime cyclic group and would make every cell equal. Quotient these states by rotation. Consider a q-cycle of the induced quotient map that stays nonconstant. Choose a representative x. After q time steps,

    F^q(x)=R^b(x), with a unique b modulo p.

This rotation displacement is independent of the representative, since F commutes with R. Along this quotient cycle, the corresponding pq states form an invariant set. On return to the chosen quotient vertex, the rotation label advances by b. If b=0, there are p temporal cycles of length q, one for each label. If b!=0, addition by b visits all p labels and there is one temporal cycle of length pq. No shorter period is possible: a temporal return must first return to the quotient vertex, hence be a multiple of q, and its rotation label must return too. In the nonzero case rotation preserves the single temporal cycle; in the zero case it permutes the p separate cycles.

For Rule30 the constant states satisfy F(0)=0,F(1)=0. Therefore its only constant temporal cycle is the white fixed point. For this rule on a prime ring, all temporal cycle lengths are pairwise distinct if and only if every nonconstant quotient cycle has nonzero displacement and the quotient cycle lengths are pairwise distinct. This is an exact reduction, not a proof that either condition holds for unexamined primes.

Existing controls from Local's census: p7 has seven4-cycles and a63-cycle; the lift description predicts a zero-displacement quotient4-cycle and a nonzero-displacement quotient9-cycle. At p11 the eleven17-cycles and154-cycle similarly predict quotient periods17 and14, with zero and nonzero displacement respectively. These are reconstruction targets from known data, not blind new predictions. In particular a claim for all prime sizes is already false.

Unexpected structural check: take F=R itself on a three-cell binary ring. Its two nonconstant temporal cycles, represented by001 and011, both travel and both have length3. Thus every cycle travelling does not imply pairwise distinct lengths. This is a different CA used to test what rotation symmetry alone proves; it is not a Rule30 counterexample at13 or later.

This specializes elementary cyclic-group cycle lifting and the already recorded rotation-orbit pigeonhole in RULE30-PRIZE.md section8.67. It identifies the remaining Rule30 mechanism as excluding zero displacement and repeated quotient periods in the observed prime-size regime, without a novelty or asymptotic claim.

### G55 addendum: spatial symmetry does not imply black/white balance

For a rotation-invariant temporal cycle C of length L on a p-ring, every spatial site has the same number of black occurrences during one temporal cycle. Rotation is a bijection of C and sends the bit at one site to the bit at its neighbour, proving equality of these finite counts. If L is odd, that common integer count cannot equal L/2. Thus the verified Rule30 p13 cycles of lengths91 and247 are travelling yet each column has biased black frequency, at least1/(2L) away from one half.

This proves a limit of the symmetry argument, not a fixed-single-seed Rule30 frequency result. It does not supply the actual black counts of those cycles, which were not measured in this block. Equal frequencies at all sites and equal frequencies of the two colours are distinct requirements.

**G55 finite control status:** RQ1-RQ3 pass10408 states at prime sizes<=13; proof and addendum await independent reading.

*The addendum was written by GPT after Local's first reading below; Local second-read it the same day (chat L028):
correct (rotation maps the cycle onto itself and site $i$ to site $i + 1$, so the black counts per site agree, and an
odd length cannot split in half). The counts it did not measure, measured (`rule30_audit_g55.py`): on the four
travelling cycles at $p = 13$ every site has the same black count, 425 of 832 (0.5108), 133 of 260 (0.5115), 123 of
247 (0.4980) and 46 of 91 (0.5055); the even-length cycles are biased as well, which parity alone does not force.*

*Second reader's note on G55 (Local, 2026-10-06; chat L027).* Correct. A rotation fixing a state on a prime ring
generates all rotations, so nonconstant states have free orbits; $F^q(x) = R^b(x)$ fixes $b$ independently of the
representative because $F$ commutes with $R$; $b = 0$ gives $p$ cycles of length $q$ and $b \ne 0$ one cycle of length
$pq$, with no shorter return in either case; Rule 30 sends the all-black ring to white, so the white fixed point is
the only constant cycle. Checked directly (`rule30_audit_g55.py`): on the prime rings 5, 7, 11, 13, 17 and 19 every
temporal cycle obeys the lifting law; the zero-displacement families are exactly the seven 4-cycles at 7 and the
eleven 17-cycles at 11; and G55's criterion (nonzero displacement and distinct quotient periods) agrees with
"all cycle lengths distinct" at every one of them. The quotient periods at 13 are 64, 20, 19, 7; at 17, 638, 96, 51,
18, 8, 1; at 19, 195, 13, 7, 2. This upgrades PROOFS.md C.6 from a pigeonhole to an exact reduction.

### G.GPT56. Prime-ring moment phase coordinate

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

### G.GPT57. Rule30 nonlinear correction and moment drift

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

### G.GPT58. Explicit one-parity witness (second-read by Local, 2026-10-06)

### G58. One-parity walls: an explicit empty-left witness (2026-10-06)

Independent audit of Local C066 in PROOFS.md's waiting room, extending the existing G26 construction rather than claiming a new mechanism. Let tau(t)=0 at every even time, with arbitrary odd-time bits a_m=tau(2m+1). Periodicity is not required. At left depth k>=1 set u_k(0)=0, u_0(t)=tau(t), and evolve the Dirichlet half-line by

    u_k(t+1)=u_(k-1)(t) XOR u_(k+1)(t).

Induction gives u_k(t)=0 whenever t+k is even, including the boundary k=0. Consequently adjacent cells cannot both be1. Rule210 is f(l,c,r)=l XOR r XOR(c*r); its nonlinear term vanishes throughout this left half. The half-line therefore satisfies Rule210 exactly, not merely Rule90 approximately. Each time has finite support because influence travels at most one cell per step.

Put pi(t)=u_1(t) and sigma(t)=tau(t+1) XOR pi(t). Then pi(odd)=sigma(odd)=0. At even t, tau(t)=0 and the wall's Rule210 update is pi(t) XOR sigma(t)=tau(t+1). At odd t, tau(t+1)=pi(t)=sigma(t)=0, so the same wall equation holds. Thus the entire left half and wall are compatible for all t>=0, with an empty initial left row. This refutes LR for every wall in this phase of the one-parity family. It does not construct a right half realizing sigma; B/full-clock realization and Rule30 remain open. C066's existence conclusion is verified by this argument; its family wording must not be read as saying every sigma with odd bits zero gives an empty initial row.

G26's Dyck-walk calculation gives the explicit boundary filter:

    pi(2n)=XOR over m=0..n-1 of a_m*(C_(n-m-1) mod2)
           =XOR over r>=0 with 2^r<=n of a_(n-2^r),
    sigma(2n)=a_n XOR pi(2n).

The empty sum at n=0 is0. The second equality uses the already proved Catalan parity identity C_j odd iff j=2^r-1. Arbitrary holes at odd times are therefore allowed; the alternating wall is only a special case. No universal claim that these witnesses are aperiodic is made for arbitrary a.

**Unexpected scope check, proved without a run.** A nonzero periodic one-parity wall cannot have odd period: adding an odd period sends every odd time to an even time with the same bit, forcing that bit to0. This explains why an odd-period nonzero wall cannot be inserted into the construction by merely choosing a time phase. The opposite parity phase has the analogous invariant t+k even and can be constructed directly. Also the previously recorded Rule30 countercontrol remains: f(0,1,0)=1 for Rule30 but0 for Rule210/Rule90, so parity sparsity does not transfer the linear reduction.

**Next bounded controls, preregistered, NOT RUN.** OP1: for all26 nonzero odd-time masks of periods2,4,6,8, through256 steps, independently compare scalar truth-table Rule210 half-line evolution and XOR half-line evolution, starting with an empty row; parity and wall equations must hold. OP2: compare depth1 against exact integer Catalan coefficients and the dyadic filter above, including all odd-time white holes. CF: applying the same left evolution as a Rule30 witness must fail (retain (0,1,0) as a concrete rule-level discriminator). These checks validate implementation, not the all-length theorem; there is no blind empirical prediction or large census. Both earlier startup controls remain passed; no environment or job change. Next implement these controls and ask Local to audit the explicit filter and scope.


### G58 outcome and periodic-input addendum (2026-10-06)

OP1 passes26 nonzero one-parity wall masks of periods2,4,6,8,6656 whole-row transitions through256 steps with independent scalar truth-table and bit-vector XOR implementations. OP2 passes3354 depth1/Catalan/dyadic comparisons (including time0). The Rule30 counterfactual is refuted by197914 cell disagreements, including the concrete tuple(0,1,0). Probe: `tests/probes/lexicon/rule30_gpt_one_parity.py`, Python on GPT's Intel host. These are finite implementation checks; the all-length claim rests on G58's induction. No failed control was discarded.

**Additional proof: every nonzero periodic input in this family has an aperiodic empty-left witness.** Work with formal power series over the two-element field. Let A(z)=sum_(n>=0) a_n*z^n, P(z)=sum pi(2n)*z^n, and V(z)=sum sigma(2n)*z^n. The explicit filter proves

    S(z)=sum_(r>=0) z^(2^r),
    P(z)=A(z)*S(z),
    V(z)=A(z)*(1+S(z)).

For periodic a of period q, A(z)=(a_0+...+a_(q-1)*z^(q-1))/(1+z^q) is rational and nonzero. S is not rational: its coefficient sequence has infinitely many1s and unbounded gaps, so cannot be eventually periodic. Over a finite field every rational power series has eventually periodic coefficients, because a fixed finite linear recurrence advances a finite set of windows deterministically; conversely an eventually periodic sequence has a polynomial prefix plus a rational periodic tail. If V were eventually periodic, V would be rational, and S=V/A+1 would be rational, a contradiction. Hence sigma's even subsequence, and therefore its full stream, is not eventually periodic. Division by A is in the rational-function field; A need not have a nonzero constant coefficient. This extends G26's particular alternating-wall aperiodicity result to all nonzero periodic walls in this parity phase. The zero wall is excluded essentially (A=0 gives V=0). No finite computation is cited as proving aperiodicity.

This algebraic argument is derived from the existing Catalan filter and the finite-state recurrence proof above; no novelty claim. It concerns this empty-row witness, not all finite-left witnesses and not right realization. Independent Local reading requested. The bounded construction/control block is complete; the useful next question is whether the required right stream can be realized, checked against G28's existing obstructions before any new route.

*Second reader's note on G58 and its addendum (Local, 2026-10-06; chat L033).* Correct. The invariant $u_k(t) = 0$ for
$t + k$ even holds from the empty row and the white even times of the wall, and propagates because both neighbours
then have $t + k$ even; so Rule 210's term $c \cdot r$ vanishes and the half-line is Rule 90's exactly. The wall
equation holds at even times by the definition of $\sigma$ and at odd times because every term is 0. The filter uses
the classical fact that $C_j$ is odd exactly when $j = 2^r - 1$. The addendum is sound: over $\mathbb{F}_2$,
$V = A(1 + S)$, rational series are exactly the eventually periodic ones, and $S = \sum z^{2^r}$ has unbounded gaps,
so a nonzero periodic $A$ forces $\sigma$ to be aperiodic. Checked independently (`rule30_audit_g58.py`): from an
empty row under Rule 210's own truth table, for 200 inputs (periodic with periods 1 to 7 and random, with holes),
the parity invariant, the wall equation, $\sigma(\text{odd}) = 0$ and the dyadic filter hold at every time to 160;
the Rule 30 counterfactual fails. **This settles Local's C066** (formerly in the waiting room): its existence claim
is proved, for every one-parity wall in this phase and with odd-time holes allowed; its family wording is
corrected as G58 says (not every $\sigma$ with $\sigma(\text{odd}) = 0$ gives an empty initial row).

### G.GPT59. Late nonlinear activity (second-read by Local, 2026-10-06)

### G59. A finite periodic Rule210 witness needs infinitely many nonlinear events (2026-10-06)

A bounded proof audit extending G28's necessary condition, using the already recorded general Rule90 obstruction (PROOFS B′16), not a new mechanism or a computational search. Suppose a finite global Rule210 initial row realizes a nonzero periodic temporal wall of period p. Then adjacent black pairs must occur at arbitrarily late times. Equivalently its nonlinear source V_t(i)=x_t(i)*x_t(i+1) cannot vanish identically for all sufficiently large t.

Proof. If V_t=0 for every t>=t0, the configuration at t0 is finite by finite propagation, and all later updates are Rule90. Write A=S+S^(-1). If that row has support in[-R,R], then A^(2^k)=S^(2^k)+S^(-2^k). For every j=0,...,p-1 and 2^k>R+p, the centre of A^(2^k+j)x is0: it samples A^j x at sites plus/minus2^k, outside its support[-R-j,R+j]. Thus the wall contains p consecutive zeros at arbitrarily late times. A nonzero p-periodic wall cannot contain even one such block. Contradiction. The argument also covers an eventually periodic nonzero wall by choosing k beyond its transient.

This strengthens G28's requirement of at least one nonlinear activation to infinitely many activations for any nonzero periodic wall, including G58's one-parity family. It does not prove activations reach the wall, exclude a finite witness, or realize the required right stream. Infinite nonlinear activity is necessary, not asserted sufficient. Because a global single-parity row stays Rule90 forever, no finite global single-parity seed can realize any nonzero eventually periodic wall; the period-two clock was only G28's special case.

**Unexpected scope guard, checked algebraically.** Finiteness cannot be dropped from the Rule90 step. A spatially period-three row100 repeated evolves under Rule90 to011 repeated, which is fixed: the three neighbor XORs are0,1,1. At the sites with value1 this gives a nonzero constant temporal wall from time1. This is a Rule90 domain counterexample, not a Rule210 witness (the adjacent pairs activate its nonlinear gate). It prevents importing the finite-row obstruction into unrestricted infinite backgrounds.

No experiment ran and no numerical extrapolation is used. Existing G28 controls and the recorded Rule90 identity are reused. Independent Local reading requested; next right-realization reasoning must allow mixed parity and unbounded nonlinear activity, rather than a finite correction followed by a linear tail.


*Second reader's note on G59 (Local, 2026-10-06; chat L034).* Correct. With no adjacent black pair from $t_0$ on,
Rule 210's term $c \cdot r$ is $V_t(i) = 0$ and the global evolution is Rule 90 from a finite row; over GF(2),
$A^{2^k} = S^{2^k} + S^{-2^k}$, so the centre of $A^{2^k + j}x$ samples $A^j x$ outside its support once
$2^k > R + p$, and the wall has $p$ consecutive zeros at arbitrarily late times, impossible for a nonzero
(eventually) periodic wall. The single-parity corollary and the period-3 scope guard ($100\ldots \to 011\ldots$, then
fixed) check. Checked (`rule30_audit_g59.py`): the zero blocks on 300 random finite rows and the fixed point.

### G.GPT60. infinite right realization (second-read by Local, 2026-10-06)

### G60. G58's right stream has a full infinite realization (2026-10-06)

Question: can the empty-left witness of G58 be realized on the right at all, separately from the finite-global-seed B question? Yes, within the globally parity-sparse Rule90 subsystem already identified in G28. This is a triangular construction from the recorded additive rule, not a new external mechanism. It realizes every one-parity temporal wall, even nonperiodic ones, on a full Rule210 configuration with an empty left half. For nonzero eventually periodic walls this particular right half necessarily has infinite support.

Let tau(2n)=0 and a_n=tau(2n+1). At time0 set x(i)=0 for i<=0 and for positive even i. Write v_j=x(2j+1), j>=0. Globally all occupied sites have odd parity, so by G28 the full Rule210 orbit agrees with Rule90 for all time. At even times its centre is0. At odd time2n+1, expanding the commuting shift operators gives

    x_(2n+1)(0)=XOR over j=0..n of
                 (binom(2n+1,n-j) mod2)*v_j.

All negative initial sites are0; the coefficient of the newest positive site2n+1 is1. Thus define recursively

    v_n=a_n XOR (XOR over j=0..n-1 of
                 (binom(2n+1,n-j) mod2)*v_j).

This gives existence and uniqueness within the class of empty-left, globally odd-supported initial rows, for every infinite binary input a. Every finite-time equation involves only finitely many initial sites, so the recursion defines an actual full configuration and its orbit; no limiting-time interchange or finite-support assumption is needed. Its centre trace is exactly tau. Its left half must agree with G58's empty-left Dirichlet evolution, whose initial row and boundary are identical. Its right neighbor has odd-time bits0 by global parity. At even times the wall equation forces sigma(2n)=a_n XOR pi(2n). Hence it realizes precisely G58's selected sigma, not merely a wall with another unspecified adjacent stream.

For nonzero eventually periodic tau, v cannot have finite support. Otherwise the full seed would be finite and single-parity, contradicting the general finite Rule90 white-block obstruction in G59. This is an existence result for an infinite right half and an obstruction for this linear finite-support class. It does not exclude a different, mixed-parity finite right seed realizing the same wall or settle B. References to “right compatibility/B” in earlier status summaries must distinguish these two domains.

**Unexpected scope check, analytic.** Infinite support is not compulsory for arbitrary nonperiodic one-parity walls. Taking v_0=1 and every other v_j=0 gives the finite seed at site1; its odd-time wall is a_n=binom(2n+1,n) mod2. This is a valid input/output pair of the recursion, but cannot be nonzero eventually periodic by the same obstruction. The periodicity hypothesis is therefore essential to the infinite-support conclusion.

**Preregistered next controls, NOT RUN.** FR1: reconstruct v for all26 nonzero odd-time masks of periods2,4,6,8 and256 odd-time samples from the exact binomial recursion; independently evolve scalar Rule210 on the full finite light cone through512 steps and recover tau through time511. FR2: compare its right-neighbor trace with G58's dyadic filter, retaining its empty-left parity invariant. CF: truncating a nonzero periodic input's reconstructed seed to a fixed finite odd-site prefix keeps its wall forever; must fail, with a failure time found analytically by G59's white block and checked beyond that block. These are implementation controls, not a finite-right search or a proof of eventual periodicity from data. Next implement this bounded audit; Local review of the construction is requested.


### G60 controls outcome (2026-10-06)

FR1 passes26 nonzero masks of periods2,4,6,8 with13312 centre comparisons through time511. FR2 passes13286 left/right neighbor comparisons through time510 against the independent dyadic filter. Full scalar Rule210 evolution preserves global parity throughout. The finite-truncation counterfactual is refuted in all26 cases: keeping only the first16 odd-site bits (radius<=31) first loses the prescribed wall at times33..43. Every truncated seed also has the analytically predicted white block at64..71, containing a prescribed black wall time. The unexpected site1 inverse guard recovers exactly[1,0,...,0] through256 bits from its binomial wall input.

Probe: `tests/probes/lexicon/rule30_gpt_full_parity.py`, Python on GPT's Intel host. These controls check finite light cones of the infinite construction; its all-length existence and periodic-input infinite-support conclusions remain analytic. No finite mixed-parity search ran, no finite-witness exclusion was obtained, and no data or generated files were tracked. G60 awaits Local's independent reading while offline. This bounded control block is complete. Next inspect the first right-layer compatibility equations for mixed-parity seeds before defining any further computation.


### G.GPT61. first right-layer gates (second-read by Local, 2026-10-06)

### G61. The first right layer gates invisible Rule210 bits (2026-10-06)

Continue the right-realization audit without a width-survival scan. Existing record: G26 gives the empty-left0101 wall's effective stream, G27 classifies its left half, G28/G59 give finite-global obstructions, and G60 supplies an infinite full realization. Here a direct truth-table calculation restricts which wall-invisible odd-time bits could differ from G60. No novelty or full-right sufficiency claim.

For any full Rule210 orbit with wall tau(2n)=0, tau(2n+1)=1, write s_n=x(1,2n), d_n=x(1,2n+1), b_n=x(2,2n), c_n=x(2,2n+1). Updating column1 at the two parities gives exactly

    d_n=(1-s_n)*b_n,
    s_(n+1)=1 XOR ((1-d_n)*c_n).

Therefore d_n=1 requires s_n=0 and s_(n+1)=1. Conversely these conditions are sufficient for the two column1 updates to admit b_n,c_n: when d=0 choose c=1 XOR s_next, and choose b=0 if s=0 or arbitrarily if s=1; when d=1 the required transition is0 to1, choose b=1 and c arbitrarily. This is an exact width-one temporal compatibility characterization. It does not require or provide column2's own evolution.

For G26's empty initial left row, s_0=1 and s_n=floor(log2(n)) mod2 for n>=1. Its transitions0 to1 occur exactly at n=2^(2r+1)-1, r>=0. Thus any full right realization of this particular left system must satisfy

    x(1,t)=0 at odd t except possibly t=2^(2r+2)-1,

namely3,15,63,255,... . “Possibly” is essential: G60 takes all these bits0. The number of allowed odd-time positions through T is at most floor(log_4(T+1)), hence only logarithmic, with unbounded gaps. This is a necessary condition for other right realizations of the same empty-left system; an arbitrary finite initial left row has a different s and is not covered by the dyadic timing specialization.

**Unexpected guard, analytic.** Sparse odd-time gates in column1 do not bound all nonlinear activity on the right. At even time, s=1 allows b arbitrarily, so b=1 gives a nonlinear pair x(1)*x(2)=1 while the equation still forces d=0. Thus one cannot infer globally sparse nonlinear events from the sparse gate schedule, or combine it with G59 to claim a finite-seed exclusion. The wall's nonlinear pair tau*x(1) can activate only at the listed odd times, but pairs farther right are unrestricted by this calculation.

**Next controls, preregistered NOT RUN.** RG1: enumerate all8 triples(s,d,s_next) and all4 pairs(b,c) with Rule210's scalar truth table; existence must agree exactly with d=0 OR(s=0 AND s_next=1). RG2: through4096 effective indices compare the0-to1 transition locations of G26's exact dyadic formula with n=2^(2r+1)-1, including special index0. CF: every odd-time invisible bit is free after imposing the first right layer; must fail, with d=1 on(s,s_next)=(1,0) as a concrete obstruction. Check the even-time nonlinear guard separately. These validate the formula, not full right realization; no job has run. Next use these controls before considering a deeper-layer or tail argument. Independent Local reading requested when back online.


### G61 controls outcome (2026-10-06)

RG1 passes all8 triples and32 hidden-pair comparisons, accepting exactly5 triples. RG2 passes4096 transition indices: the allowed effective up-transitions are1,7,31,127,511,2047. The arbitrary-invisible-bit counterfactual is refuted by(1,1,0), and the even-time deeper nonlinear guard passes. Probe: `tests/probes/lexicon/rule30_gpt_right_gates.py`, Python on GPT's Intel host. These finite controls confirm the algebra; no full-right sufficiency or finite-witness exclusion follows. Block complete; G62 imposes column2's own update next.


### G.GPT62. first nonlinear pair (second-read by Local, 2026-10-06)

### G62. Column2's update restricts the first nonlinear pair (2026-10-06)

Continue G61 by imposing column2's even-to-odd update, rather than assuming its freely chosen temporal pair evolves. Retain s_n,d_n,b_n,c_n from G61 and let q_n=x(3,2n). Rule210 gives

    c_n=s_n XOR ((1-b_n)*q_n).

If d_n=1, G61 forces s_n=0,b_n=1. The new equation then forces c_n=0. Thus x(1,2n+1)*x(2,2n+1)=d_n*c_n=0 at every odd time in any full0101 wall orbit. If s_n*b_n=1 at even time, then s_n=b_n=1, so d_n=0 and c_n=1. G61's odd-to-even equation forces s_(n+1)=0. Therefore

    x(1,2n)*x(2,2n)=1 implies (s_n,s_(n+1))=(1,0).

The temporal support of this particular nonlinear gate is confined to effective1-to0 transitions, and its odd-time support is empty. This is necessary for full orbits; it is not a sufficiency statement for a whole right half. In contrast, G61's wall gate tau*x(1) can occur only at odd-time0-to1 transitions. The two neighboring nonlinear sources therefore have distinct allowed timing.

For G26's empty-left stream,1-to0 transitions are n=4^r-1, r>=0, including the special n=0. Hence the pair in columns1-2 can activate only at even times2*(4^r-1)=0,6,30,126,... . The wall's allowed gate times remain4^(r+1)-1=3,15,63,... . These are possible times, not a claim that every such gate fires. G60's fully parity-sparse realization fires neither.

**Unexpected guard.** G61's local tuple(s,d,s_next,b,c)=(1,0,0,1,1) remains compatible with column2's added even update, for either q. Thus deeper compatibility sharpens the support but does not eliminate nonlinear activity at the allowed down-transition gates. No timing restriction on pairs at sites2 or farther right is obtained here, so neither logarithmic gate count nor G59 implies a finite-seed exclusion. This direct Boolean derivation uses the existing rule and G61, with no novelty claim and no new computational experiment.

**Next bounded control, preregistered NOT RUN.** NG1: enumerate all32 initial positive patches(s,b,q,h,z)=x(1..5,2n), evaluate scalar Rule210 updates of columns1-3 at two steps under the imposed wall values0 then1, and check both implications. This is a local Dirichlet-layer check, not a claim that the imposed wall evolves from the patch alone. Compare resulting s,d,b,c with G61; retain the allowed tuple above as a realizable local guard. NG2: compare down-transition positions through4096 effective indices with n=4^r-1 including0. CF: the columns1-2 pair can be black at an odd time under the clock; must fail. A local two-step patch is not an infinite full clock or a finite witness. Independent Local reading requested; next complete these controls before extending farther right.


### G62 controls outcome (2026-10-06)

NG1 passes all32 positive five-cell Dirichlet patches through the two specified updates. All8 patches with an even columns1-2 black pair force the next effective bit0; all32 have no odd pair. The allowed even-pair guard survives in8 patches. NG2 passes4096 indices, with down-transition positions0,3,15,63,255,1023,4095. The odd-pair counterfactual is refuted. Probe: `tests/probes/lexicon/rule30_gpt_pair_support.py`, Python on GPT's Intel host, under1 s.

These are local compatibility controls under the imposed wall, not a full-clock construction or a finite-seed search. No control failed. G62 remains awaiting an independent reader. The pair-specific block is complete; next seek a statement controlling a whole right strip during a constant effective run, rather than extrapolating the first pair's support to all depths.

*Second reader's note on G60, G61 and G62 (Local, 2026-10-06; chat L035).* All three correct. G60: in Rule 90 the
centre at time $2n+1$ is $\bigoplus_j \binom{2n+1}{n-j} v_j$ with coefficient 1 on the newest site, so the recursion is
triangular and defines the full odd-supported seed; the left half is G58's because it depends only on the left cells
and column 0; finite support would contradict G59 for a nonzero periodic wall; the site-1 scope check gives
$a_n = \binom{2n+1}{n} \bmod 2$. G61: the two column-1 updates are $d_n = (1 - s_n)b_n$ and
$s_{n+1} = 1 \oplus (1 - d_n)c_n$, and G26's up-transitions fall at $n = 2^{2r+1} - 1$, odd times $3, 15, 63, \ldots$.
G62: column 2's update $c_n = s_n \oplus (1 - b_n)q_n$ makes every odd columns-1-2 pair impossible and forces
$s_{n+1} = 0$ after an even pair; G26's down-transitions fall at $n = 4^r - 1$ (with $n = 0$). Checked independently
(`rule30_audit_g60_g66.py`): full Rule 210 evolved from the recursion's seed reproduces the wall for 12 periodic
inputs over 120 steps; the G61 and G62 truth tables exhaustively; the transition positions to 5,000.

### G.GPT63. forced right strip (second-read by Local, 2026-10-06)

### G63. A constant effective run forces a right strip (2026-10-06)

Question from G037: can G61-G62's individual gate restrictions be replaced by a strip statement? The following local extension lemma does so. This is derived from Rule210's recorded truth table and the parity subsystem in G28; a targeted record search for period-six/constant Rule210 strip statements found no matching entry. It is not a literature novelty claim, a full-realization construction, or a finite-seed exclusion.

**Local extension lemma.** In a Rule210 orbit let neighboring columns L,C have constant two-phase temporal values on an integer time interval I=[A,B], inclusive. Write their (even,odd) pairs as L=(l_e,l_o), C=(c_e,c_o), each in{00,10,01}, with disjoint occupied phases: l_e*c_e=l_o*c_o=0. Then the next column R is forced on[A+2,B-2] to the pair

    R=(c_o XOR l_e, c_e XOR l_o).

No temporal periodicity assumption is imposed on R or any farther column. If C=00, its own update gives R(t)=L(t), using C(t+1)=0, and the formula follows. If C=10, its odd-time white update forces R(odd)=1 XOR l_o, while its even black update requires l_e=0. Put b=1 XOR l_o. If b=1, R is black at the preceding odd time; its own update then forces its next even value to C(odd)=0, independently of the farther column. If b=0 and an even R were1, its own update would force the next odd R to C(even)=1, contradicting the known odd0. Thus R(even)=0 in either case. The case C=01 is the parity-swapped argument, giving R(odd)=0 and R(even)=1 XOR l_e. Trimming two steps at each end ensures every preceding/following sample and C update used lies in I. These cases prove the lemma and show the output remains in{00,10,01}, with opposite occupied phase to C whenever nonzero.

**Strip corollary for0101.** Suppose s_n=x(1,2n)=a is constant for m<=n<=N. G61 forces d_n=x(1,2n+1)=0 for m<=n<N, since a constant transition is not0-to1. Thus columns0 and1 have pairs v_0=01, v_1=(a,0) on[2m,2N]. Iterating the lemma gives, for every k>=1 with a nonempty specified window,

    column k has pair v_k on
    [2m+2*(k-1), 2N-2*(k-1)],
    v_(k+1)=swap(v_k) XOR v_(k-1).

The vectors repeat spatially with period6. For a=0, v_0..v_5 are01,00,01,10,00,10; for a=1 they are01,10,00,10,01,00. In both cases direct recurrence gives v_6=v_0 and v_7=v_1, proving repetition. Neighboring forced columns have disjoint black phases, so every adjacent pair wholly inside their common forced time window has nonlinear product0. This is a growing, parity-linear right strip on the interior of a constant effective run, not just one gate's support. In G26 the effective dyadic runs grow without bound, so any full realization of that particular empty-left system has arbitrarily wide such strips.

**Unexpected boundary guard.** Dropping the temporal margin is unjustified. In the local layer system L=00,C=10 on[0,7], choose R=11 at times0,1 and thereafter R=01 (even0,odd1). C's updates and R's updates admit a farther-column stream, yet R(0)=1 disagrees with the predicted pair01. The preceding odd sample outside the interval is missing. This is a counterexample within the stated local layer equations, not an assertion that the farther stream itself has a full evolution. It shows why the lemma's proof must retain its time-window premises. The two-step margin is conservative; no optimality claim.

The corollary does not force the entire right half at one time or make every nonlinear event vanish eventually. Growing strips inside growing intervals can coexist with activity at their edges or farther right. G59 therefore still supplies no finite-seed contradiction. Full mixed-parity finite witnesses remain open.

**Next controls, preregistered NOT RUN.** ST1: enumerate all7 disjoint-phase pairs(L,C), all256 eight-bit R words on[0,7]; retain exactly those satisfying C's seven updates and admitting seven farther-column bits for R's own updates. Every accepted R must match the lemma on[2,5]. ST2: check both six-phase spatial cycles and their disjoint-phase property through60 columns. CF: the same forcing holds at every endpoint with no margin; must fail on the specified L=00,C=10,R boundary guard. These are local controls, not finite/full orbit searches. Independent Local reading requested; next run them before using the strip quantitatively.


### G63 controls outcome (2026-10-06)

ST1 passes all7 disjoint-phase pairs and1792 candidate eight-bit right words; exactly15 words admit both layers' specified updates, and all15 agree with the predicted trace at times2..5. ST2 passes both period-six patterns through120 column-phase values and118 neighboring phase pairs. The no-margin counterfactual is refuted by the accepted local boundary word with R(0)=1 instead of0. Probe: `tests/probes/lexicon/rule30_gpt_strip.py`, Python on GPT's Intel host, under1 s. No control failed.

These checks are local temporal layers, not full realizations of their farther streams; the full-orbit corollary uses the analytic lemma. G63 remains awaiting Local's independent reading. The bounded strip control block is complete. Next examine temporal block complexity for a fixed right column: the growing dyadic-run strips may leave only logarithmically many unconstrained windows. Any entropy claim needs a uniform bound over arbitrary starting times, not just a count of prefixes from time0; no such bound is claimed here yet.


### G.GPT64. fixed-column temporal complexity (second-read by Local, 2026-10-06)

### G64. Fixed right columns have zero temporal word-count entropy (2026-10-06)

Use G63's strip lemma for all full Rule210 realizations of the0101 wall with the empty initial left row of G26. This class is nonempty by G60; the right half may be infinite or mixed-parity. For each fixed column k>=1 let P_k(N) count all distinct length-N temporal words, across all such realizations and all starting times u>=0. Then

    P_k(N)=O_k(N^(4k+2)),
    limsup as N->infinity of log2(P_k(N))/N=0.

This extends G26's factor-count observation for one particular adjacent stream to every fixed right column in this precisely specified family. It is not a Rule30 theorem, an assertion of zero entropy for the whole CA, or an exclusion of finite mixed-parity witnesses. The constant and exponent depend on k.

**Forced positions.** The effective stream changes across odd times in B={2^j-1:j>=1}; include a virtual boundary-1 for the start of time. G63 forces column k to its known two-phase template except within distance2k of these boundaries. Indeed each constant effective run spans even endpoints[2m,2N]; the lemma trims2(k-1) at each end, and the intervening odd transition time is in B. Every omitted sample is inside the asserted radius; choosing2k is conservative. Outside those neighborhoods the template depends only on the effective run's value, the time parity and k modulo6.

**Uniform word bound.** Fix N,k, set r=2k, L=N+2r and choose M to be the least power of2 with M>=L+1. Thus M<2(L+1). For early starts0<=u<M+r, the enlarged window[u-r,u+N-1+r] ends before2M-1. It contains at most Q=log2(M)+1 boundaries, counting the virtual-1. The unconstrained samples in the word are at most(2r+1)Q. At a fixed start the forced template is already known, so early starts contribute at most

    (M+r)*2^((2r+1)*Q).

For late starts u>=M+r, the enlarged window begins at least M. Consecutive boundaries there are separated by at least2M>L, so it contains at most one. Allow its relative position any of L integer positions, or allow no boundary; choose either effective value independently on each side and either time parity, at most8 template choices. Allow all2r+1 boundary-neighborhood bits arbitrary. Late words contribute at most

    8*(L+1)*2^(2r+1).

These bounds count a superset, including choices that need not have a full realization. Their sum bounds P_k(N). Since 2^((2r+1)Q)=2^(2r+1)*M^(2r+1), it is O_k(N^(2r+2))=O_k(N^(4k+2)). Taking log and dividing by N proves the entropy statement uniformly over starting times. Column0 separately has at most2 words of every length. No finite measurements are used in the all-length proof.

**Unexpected guard: prefix density is insufficient.** Concatenate lists containing every binary word of length m, separated by zero blocks of length2^(2^m). Their black prefix density tends to0, since the previous zero block eventually dwarfs the next list of size O(m*2^m). Yet every binary word occurs, so temporal factor complexity is2^N and entropy1. This illustrates why the arbitrary-start late-window argument is necessary; a sparse prefix count alone would not prove G64. It is a constructed binary-sequence counterexample, not a Rule210 realization.

This is elementary counting from G26/G63 and the explicitly defined word-count entropy, with no literature novelty claim. Earlier G53/G54 bounds concern another family and do not supply the dyadic transition hypothesis here. G63 and this consequence await Local's independent reading. No uniform-in-k or initial-condition-wide conclusion is made.

**Next controls, preregistered NOT RUN.** WC1: k=1..6,N in{1,2,4,8,16,32,64,128}, every start0..4095; directly enumerate enlarged-window boundaries and marked sample positions, checking the early Q bound and late one-boundary bound. WC2: on G60's explicit0101 full realization, compare columns1..6 through time500 with G63's templates at every sample outside the stated boundary neighborhoods, using an independent scalar full evolution. CF: prefix sparsity implies zero factor entropy; refuted analytically by the concatenated-word construction above, without an empirical entropy estimate. These controls validate margins and counting instrumentation, not the entropy limit itself.


### G64 controls outcome (2026-10-06)

WC1 passes196608 windows for k=1..6, lengths1,2,4,8,16,32,64,128 and every start0..4095:3952 early windows obey Q and marked-sample bounds;192656 late windows obey the one-boundary and radius bounds. WC2 passes2524 forced samples of columns1..6 through time500 on G60's explicit scalar full Rule210 realization;482 samples are excluded by the conservative neighborhoods. Probe: `tests/probes/lexicon/rule30_gpt_window_complexity.py`, Python on GPT's Intel host, under1 s. No control failed.

These finite checks validate the counting split and forcing margins; the entropy limit remains the analytic G64 proof, not an empirical estimate. The concatenated-word counterfactual is retained as an analytic counterexample. Independent reading remains queued. This bounded block is complete; next audit the effect of varying initial left support, since G27's arbitrary finite visible prefixes warn against treating one fixed empty-left family as the union of all finite-left families.


### G.GPT65. mirror extension and quantifiers (second-read by Local, 2026-10-06)

### G65. Mirror extension and the varying-left-row quantifier (2026-10-06)

Scope audit following G041, using G27's finite-prefix continuation and G60's triangular full realization. Fix tau=0101. Let h_j be G60's initial right bit at site2j+1 for the empty-left system. Prescribe any finite initial left row supported on odd depths, with e_j at site-(2j+1), and define the initial right row by

    v_j=h_j XOR e_j,

with every positive even site and the centre0. This gives a full Rule210 realization of the same clock and the prescribed left row. Its right support is infinite, since h has infinite support and e is finite. It is not a finite global witness.

Proof. The entire initial configuration has odd spatial support, so its Rule210 orbit agrees with Rule90. Relative to G60, the added configuration has the same bit e_j at the reflected sites plus/minus(2j+1). In the Rule90 expansion at the centre, those two sites have equal binomial coefficients at every time (the two coefficients are symmetric), so their contributions cancel over GF(2). Thus the wall stays0101 for all time. Equivalently the odd-time triangular equation depends on v_j XOR e_j; setting this to h_j preserves every equation. No linearity claim is made outside the global parity-sparse subsystem. The full left evolution is the unique Dirichlet evolution with that row and wall, hence matches G27's compatible left construction. This proves full infinite-right extension for every finite odd-supported left row, not only for the empty row.

**Exact language count after varying the row.** Restrict to these globally parity-sparse full realizations while allowing every finite odd-supported initial left row. In column1 every odd-time bit is0. By G27's continuation corollary, every length-n even-time word occurs: choose its finite left row (support at most2n-1) and apply the mirror extension above. Thus length-N temporal factors, across all realizations and all start times, are exactly the binary words with zeros on one of their two alternating position classes. Either class is realized by choosing a sufficiently long even-time prefix and a start of parity0 or1. Their intersection contains only the all-zero word. Therefore

    P(N)=2^ceil(N/2)+2^floor(N/2)-1,
    lim as N->infinity of log2(P(N))/N=1/2.

This is entropy of the union's temporal language. It does not assert that any one orbit has entropy1/2, or that every fixed nonempty initial left row has zero entropy. G64 proved zero for one fixed empty-left family, including its potentially nonlinear right realizations. Removing the fixed-row hypothesis already gives entropy at least1/2 in the broader family, because the parity-sparse subfamily above realizes these factors. No exact entropy is asserted for the broader mixed-parity family.

**Unexpected domain guard.** Reflected additions do not automatically cancel in Rule210 outside the parity subsystem. From the finite initial seed{1}, the centre at time2 is0. Adding the reflected even sites{-2,2} gives seed{-2,1,2}, whose centre at time1 is1, left neighbor1 and right neighbor0; Rule210 then gives centre1 at time2. Thus the centre changes, despite the mirrored addition. This is an analytic truth-table counterexample to importing Rule90 superposition into mixed-parity Rule210. It is not a clock witness or an experiment.

This synthesizes already recorded G27/G60 with the elementary binomial symmetry; no novelty claim or new prior-art theorem. The finite-right B problem remains open, and no Rule30 consequence is asserted. New details await Local's independent reading.

**Next controls, preregistered NOT RUN.** MX1:32 odd-depth left masks through depth9, reflected onto G60's reconstructed right seed, scalar Rule210 through256 steps; clock, prescribed initial left row and global parity must hold. MX2: all256 odd-depth left masks through depth15, same full extension, first8 column1 even bits must cover all256 words. Compare the two-phase temporal factor count for lengths1..8 against the exact formula above using those finite prefixes. CF: adding any reflected finite seed preserves a Rule210 centre trace; refute with{1} versus{-2,1,2} at time2. These are bounded controls for full infinite-right light cones and the language map, not finite-global witness searches.


### G65 controls outcome (2026-10-06)

MX1 passes32 left masks/8224 clock and parity time checks through256 steps. MX2 realizes all256 distinct eight-bit even-time column1 prefixes; temporal factor counts for lengths1..8 are2,3,5,7,11,15,23,31, matching the exact formula. The mixed-parity reflected-addition counterfactual is refuted at time2 (centre0 versus1). Probe: `tests/probes/lexicon/rule30_gpt_mirror.py`, Python on GPT's Intel host, under1 s. These finite checks do not estimate entropy or construct finite global witnesses. No control failed. The extension/count block is complete; G66 addresses bounded support uniformly.


### G.GPT66. bounded-left-support temporal complexity (second-read by Local, 2026-10-06)

### G66. Bounded left support retains zero fixed-column entropy (2026-10-06)

Complete G65's quantifier audit. For every fixed R>=0 and k>=1, all full Rule2100101 realizations whose initial left support lies in[-R,-1] have zero temporal word-count entropy in column k, uniformly across those left rows, right realizations and temporal starting positions. An infinite right half is allowed. The bound depends on R,k. G65's positive union-language entropy is therefore a genuinely unbounded-left-support effect; it does not require any individual orbit to have positive entropy.

**A finite Rule90 trace is localized near powers of two.** Let E be any finite initial row supported in[-R,R], and A=S+S^(-1) over GF(2). If 2^q<=t<2^(q+1), the Frobenius identity gives

    A^t=product over b with the b-th bit of t=1 of
        (S^(2^b)+S^(-2^b)).

Every monomial exponent has absolute value at least2^q-(t-2^q)=2^(q+1)-t: the largest signed power cannot be canceled by more than the sum of all smaller ones. Thus (A^t E)(i)=0 whenever2^(q+1)-t>R+abs(i). No assertion that all remaining times are nonzero is made. This is a direct shift-polynomial bound, not a new prior-art theorem.

**Apply it to the left perturbation.** G27's inverse classification makes every clock-compatible left row odd-supported and its evolution Rule90 with boundary0101. Compare a row e supported in[-R,-1] with the empty-left evolution. Their difference has zero boundary and evolves linearly. Extend e symmetrically to the positive side, forming a finite E supported in[-R,R]. Its global Rule90 centre is0 for all time by reflection symmetry; hence its left restriction is exactly this zero-boundary difference. The left-neighbor discrepancy at time t is (A^t E)(-1), which can be nonzero only within R+1 time steps before the next power of2. The even-time effective stream s differs from G26's dyadic baseline by that discrepancy; its odd-time left-neighbor values remain0. At t=0 any discrepancy is handled by the initial boundary margin.

Let B={-1} union{2^j-1:j>=1}. Outside radius R+2 neighborhoods of B, the two neighboring effective even bits agree with the same constant baseline run. G61 then forces the intervening odd-time column1 bit0. Thus columns0 and1 agree with the baseline two-phase templates between these widened neighborhoods. Applying G63 iteratively shows column k agrees with the baseline spatial-period-six template outside radius

    r=R+2k+4

of B. This is a conservative enlargement: R+2 covers perturbations and neighboring even samples; each added column trims2 more time steps at each end. Activity inside these neighborhoods or farther right is not excluded.

**Uniform counting.** Reuse G64's arbitrary-start early/late window argument with this fixed radius r. With L=N+2r, M the least power of2 at least L+1, Q=log2(M)+1, the combined family has

    P_(R,k)(N) <= (M+r)*2^((2r+1)*Q)
                  +8*(L+1)*2^(2r+1)
               =O_(R,k)(N^(2r+2)).

At a fixed start, every forced template is common to all left rows with this radius; arbitrary neighborhood bits already cover their differences. The bound is uniform over starting times and right realizations. Its logarithm divided by N tends to0. This proves the stated entropy result, including each particular finite compatible left row. It does not give a uniform bound as R or k grows with N.

**Unexpected quantifier guard.** G65's arbitrary-prefix construction uses left support growing with the requested prefix length (at most2n-1 for n even-time bits). It supplies full parity-sparse realizations and union-language entropy1/2 when R is unrestricted. Thus taking a supremum over R before taking the temporal word-length limit changes the answer. The bounded-support theorem and the unbounded union do not contradict each other; neither yields a finite-global-seed exclusion. No Rule30 transfer is asserted.

No experiment ran for this new lemma. It synthesizes G27/G63-G65 and the recorded Frobenius identity, with no novelty claim. Independent Local reading requested.

**Next controls, preregistered NOT RUN.** BP1: all32 reflected odd-left masks through depth9, scalar Rule90 through512 steps; compare the trace at-1 with the left discrepancy of the corresponding full Rule210 mirror extension, and require it to vanish whenever the next-power gap exceeds10. BP2: for the same full realizations, columns1..6 through time500 must match the baseline period-six templates whenever farther than r=9+2k+4 from B. CF: the same strip/entropy bound is uniform over unrestricted left radius; rejected analytically by G65's exact union-language count, not by an empirical entropy estimate. These validate localization and conservative margins, not the entropy limit itself.


### G66 controls outcome (2026-10-06)

BP1 passes16416 left-neighbor discrepancy comparisons through512 steps for32 reflected odd-left masks, including14304 checks that the trace vanishes when the next-power gap exceeds10. BP2 passes62432 forced samples through time500 on columns1..6;33760 samples are excluded by the conservative radius9+2k+4. Independent scalar truth tables evolve the finite Rule90 perturbation and full Rule210 mirror extension. Probe: `tests/probes/lexicon/rule30_gpt_bounded_perturbation.py`, Python on GPT's Intel host, seconds.

No control failed. Finite right initial data extend beyond every compared light cone, so the run checks the stated infinite construction locally, not a finite-global clock. The radius-uniform counterfactual remains the analytic G65 language result. G66's entropy limit is analytic and awaits independent reading. This bounded Rule210 strip/complexity block is complete; next reopen the Collatz survivor-count reasoning at G45-G48 rather than add equivalent entropy bounds without a bridge to finite right realization. No Collatz experiment starts in this checkpoint.

*Second reader's note on G63, G64, G65 and G66 (Local, 2026-10-06; chat L036).* All four correct. G63: from
$C(t+1) = L(t) \oplus R(t)(1 \oplus C(t))$, $R$ is forced wherever $C$ is white, and the two black-phase cases close through
$R$'s own update ($R(t) = 1$ forces $R(t+1) = C(t)$; otherwise a black $R$ would contradict the forced odd 0), so
$R = \mathrm{swap}(C) \oplus L$ with the stated margins; both period-6 cycles recomputed. G64: early windows end before
$2M - 1$ and meet at most $\log_2 M + 1$ boundaries, late windows meet at most one because the gaps are at least
$2M > L$, giving $O_k(N^{4k+2})$; the prefix-density counterexample is the right guard. G65: the centre coefficients
$\binom{t}{(t \pm (2j+1))/2}$ are equal, so mirrored odd pairs cancel under Rule 90; the union count
$2^{\lceil N/2 \rceil} + 2^{\lfloor N/2 \rfloor} - 1$ and the $\{1\}$ versus $\{-2, 1, 2\}$ guard check. G66: every monomial
of $A^t$ has $|\text{exponent}| \ge 2^{q+1} - t$, so a finite perturbation reaches site $i$ only within $R + |i|$ steps of
the next power of 2, and G64's counting applies with radius $R + 2k + 4$. Checked independently
(`rule30_audit_g60_g66.py`): G63's lemma exhaustively over local layers (15 accepted words, all forced), G64's forced
template against a full G60 realization (2,554 samples, columns 1 to 5), G65's mirror extension under full Rule 210
(20 rows), and G66's localization (240,116 predicted zeros).

### G.GPT67. first-deficit offset envelope (second-read by Local, 2026-10-06)

### G67. The maximal affine offset at a first coefficient deficit (2026-10-06)

Return to the open Collatz survivor count, without extending G48's horizon census. The [Rozier–Terracol primary source, Definition1.2](https://arxiv.org/html/2502.00948v2) explicitly calls equality of actual and coefficient stopping times a conjecture for n>=2. G48's source wording must be read in that sense, not as an all-horizon theorem. Its Lemma2.1/Theorem2.2 give the unconditioned parity-word offset order and extrema; the calculation below conditions on the first-deficit barrier. No novelty claim.

Fix a first coefficient-deficit word with a>=1 ones and length t. Necessarily t is the least integer with2^t>3^a, because its last bit is0 and the preceding coefficient is above1. Write p_i for the position of its(i+1)-st1, indexed from0. Then

    p_0=0,
    p_i<=floor(i*log2(3)) for1<=i<a,
    B=sum over i=0..a-1 of 3^(a-1-i)*2^p_i.

The position bound follows from the proper prefix just before that1: it contains i ones and p_i steps, so3^i>2^p_i. Irrationality of log2(3) converts this to the stated floor. The displayed B is the affine intercept from G45's recurrence, expanded by odd-step positions.

All maximal positions can be attained simultaneously. Set p_i=floor(i*log2(3)) and place zeros at the remaining positions through t-1. These positions increase strictly, start at0, and end before the final zero. Before each new1,3^i>2^p_i; every earlier prefix in the intervening zero run has at least that coefficient. After the final1 the coefficient stays above1 through t-1 and first fails at t. Thus this is an admissible first-deficit word. Since every summand of B strictly increases with its position and the bounds are componentwise, it is the unique maximum-intercept word in this class. Define

    B_max(a)=sum over i=0..a-1 of
             3^(a-1-i)*2^floor(i*log2(3)).

This can be evaluated with exact integers: floor(i*log2(3))=bit_length(3^i)-1, including i=0. No floating-point logarithm is needed.

Dividing by3^a gives(1/3)*sum_i 2^(-fractional_part(i*log2(3))). Hence

    a*3^a/6 < B_max(a) <= a*3^a/3,

with equality in the upper bound only at a=1. In particular every first-deficit word's formal G45 ceiling is bounded by

    K_w <= floor(B_max(a)/(2^t-3^a)),

and this maximum ceiling is attained by the maximum-intercept word, though rounding need not make its maximizer unique. This improves the unconditioned offset envelope to linear-in-a times3^a on the first-deficit barrier. It does not uniformly bound K over a, remove the near-resonance denominator, or control the realizing residue. G46's unbounded formal ceilings and G48's actual-start gap remain relevant. No summed survivor estimate follows just by multiplying this ceiling by residue density; G46's rounding counterexample still applies.

**Unexpected conditioning guard.** For a=2,t=4, the barrier maximizer is1100 with B=5. The unrestricted word0011 has B=20 but already fails the coefficient barrier at its first step. Thus the source's unrestricted extremal order cannot be substituted directly for the barrier maximum. The zero-ones first-deficit word0 is a separate case: B=0 and no positive actual survivor, as G48 records.

No experiment has run for this envelope. Existing G45-G48 machinery and the source's unconditioned order are credited. The CST conjecture, residue placement and Collatz prize remain unresolved. Independent Local reading requested.

**Next controls, preregistered NOT RUN.** OB1: reuse the complete first-deficit-word population throughlength16, compare every B with this bound and the maximum within each nonzero a class with B_max(a), including uniqueness of its maximizing word. OB2: a=1..256, exact integer construction of the maximizing word; check first-deficit condition, intercept recurrence, strict lower/non-strict upper envelope and G45 ceiling formula. CF: the unrestricted maximum-offset word is a first-deficit word; refute with0011. This is an extremality audit on the existing small census, not a larger stopping-time job or a claim of actual survivor realization.


### G67 controls outcome (2026-10-06)

OB1 passes all791 first-deficit words throughlength16, including the separate zero-ones word. All10 nonzero odd-count classes have the exact unique maximum-intercept word predicted by G67. OB2 passes256 exact constructions: first-deficit condition, affine recurrence, strict lower/non-strict upper offset envelope, and G45's independent prefix-ceiling calculation. The unexpected0011 conditioning guard is retained: B20 exceeds the a2 barrier maximum5 but fails the barrier immediately. Probe: `tests/probes/prizes/collatz_gpt_barrier_offset.py`; Python on GPT's Intel host, under1 s. No control failed. This audits extremality, not actual residue placement or an all-horizon stopping theorem. Independent proof review remains pending.

### G67 residue controls outcome (2026-10-06)

RB1 passes its prediction on the same791 first-deficit words throughlength16. Maximum-intercept words also maximize the least-residue terminal gap in classes a=1,2,3; they fail to maximize it in every class a=4..10. Retained pairs (a, extremal gap, maximum gap): (4,-21,-2), (5,-5,-1), (6,-145,-82), (7,-474,-107), (8,-609,-37), (9,-2859,-50), (10,-5572,-34). These are finite class maxima, not bounds for larger a.

The unexpected ordering counterfactual is refuted by a fully explicit pair, isolated as a post-control diagnostic. Both words below have a4,t7,D=47 and are first-deficit:

| Word | Offset B | Least residue r | Terminal q | Gap q-r |
| --- | --- | --- | --- | --- |
| 1101100 | 85 | 59 | 38 | -21 |
| 1110100 | 73 | 7 | 5 | -2 |

Their integer trajectories are respectively59,89,134,67,101,152,76,38 and7,11,17,26,13,20,10,5. They have the same formal ceiling K=1, but neither residue lies below it. G48's exact identity2^t*g=B-D*r explains the reversal: the offset increases by12 while D*r increases by2444, so the gap falls by19. Componentwise odd-position monotonicity of B therefore cannot be transferred to actual gaps. The counterexample is exact arithmetic, not a statistical inference.

RB2 passes its finite prediction on all256 G67 extremizers: no zero residues occur, and the complete list of positive surviving lifts is(a,t,n,g)=(1,2,1,0). The least positive realizing start for each word is evolved independently, including the positive-domain guard r=0, and every putative surviving lift is checked. The identity linking intercept, residue and gap is also verified. No larger census, extrapolation to all a, or new stopping theorem is claimed. Probe: `tests/probes/prizes/collatz_gpt_barrier_residue.py`; Python on GPT's Intel host, under1 s. No control failed; all mismatches predicted by RB1 are retained.

This completes the finite extremality audit. Next reasoning target: a residue-sensitive inequality or certificate for first-deficit words; any such claim must retain this ordering counterexample and G46's rounding obstruction. Simply extending the extremizer table would not supply the missing uniform argument. No new experiment is registered or launched in this checkpoint.


### G.GPT68. endpoint digit certificates (second-read by Local, 2026-10-06)

### G68. Two endpoint ceilings and nested digit exclusion certificates (2026-10-06)

Continue G67's residue-sensitive audit. This is an elementary consequence of G45/G48 and Local's least-terminal-residue lemma in COLLATZ-PRIZE.md §4, not a new distribution theorem or a novelty claim. G67's ordering counterexample and G46's rounding obstruction remain controls.

Let w be a first coefficient-deficit word of length t with a>=1 ones, M=2^t, A=3^a, D=M-A>0 and affine intercept B. Put K=floor(B/D). Its least realizing start is r in[0,M-1] and its least terminal value is y=T^t(r) in[0,A-1], with

    M*y=A*r+B.

Both r,y are positive: a word with at least one odd step cannot be the itinerary of0, and T preserves positive integers. Every positive realizing lift is n=r+M*m, with terminal q=y+A*m and m>=0. Every proper prefix has coefficient greater than1 and nonnegative intercept, so actual survival through t is equivalent to q>=n at the final step alone. The affine relation gives two forms of the gap:

    q-n=(B-D*n)/M=(B-D*q)/A.

Consequently q>=n iff n<=K iff q<=K. Thus start and terminal have exactly the same ceiling, despite different moduli. The two exact lift counts agree:

    max(0,1+floor((K-r)/M))
      =max(0,1+floor((K-y)/A)).

This is an identity of the same lift parameter m, not an independence assertion. The a0 word0 is separate, with no positive survivor.

**Partial digit certificates.** A prefix u of length s has intercept C_u and odd count a_u. Every realizing positive n satisfies

    n = -C_u*3^(-a_u) mod2^s.

A suffix v of length ell with b ones and intercept C_v satisfies2^ell*q=3^b*x+C_v for the intermediate integer x, so every positive terminal q satisfies

    q=C_v*2^(-ell) mod3^b.

Inverses exist in the indicated moduli; with s=0 or b=0, modulus1 is interpreted as the sole residue0. For a residue rho modulo H define its least positive representative L_H(rho)=rho if rho>0, and H otherwise. If either the prefix representative or suffix representative exceeds K, the full word has no positive actual survivor. This gives independently checkable exclusion certificates without assuming uniform residues or multiplying densities. It uses the exact full-word ceiling; no efficient method to sum such certificates over all words is proved here.

These lower bounds are nested as information increases. Each longer prefix has the same residue modulo the shorter power of2. Each longer suffix has the same terminal residue modulo the shorter power of3; this also follows directly by reducing its affine identity. The positive representatives therefore cannot decrease. At full prefix or full suffix length the tests are individually complete, giving r>K or y>K. Before full length, passing either or both is only absence of an exclusion certificate.

**Unexpected sufficiency guard.** The first-deficit word1101100 has K1,r59,y38 by G67. Its one-bit prefix1 permits positive start1, and its two-bit suffix00 has b0 and permits positive terminal1. Both partial lower bounds equal K, yet the full word has no positive survivor. Thus passing two partial endpoint tests is not a survival theorem. This analytic counterexample is deliberately retained alongside the stronger tests; no computational experiment was needed to derive it.

The unresolved task is an arithmetic bound on how many barrier words escape short endpoint certificates, with rounding retained. The lemma changes the available certificates, not the known all-horizon stopping status. Independent Local reading requested.

**Next controls, preregistered NOT RUN.** EC1: exactly the existing791 first-deficit words throughlength16, check the terminal formula and equality of both lift counts; independently evolve all claimed surviving positive lifts. EC2: for every prefix/suffix length of every nonzero-a word in that population, check the two congruences, nested positive lower bounds, sound exclusion and completeness at full length. Record minimal binary-prefix and ternary-suffix certificate lengths for the256 G67 extremizers; predict all a2..256 have both full certificates, while a1 has none. No short-depth asymptotic prediction or new horizon. Counterfactual: passing two partial endpoint tests suffices for survival; must fail on1101100 with prefix1 and suffix00. This is a bounded instrument audit and keeps Local's computational lane free.


### G68 controls outcome (2026-10-06)

EC1 passes791 first-deficit words throughlength16: both endpoint lift counts agree on all791, with one positive surviving lift independently evolved (the known n1 return). EC2 passes25358 prefix/suffix endpoint congruence checks, including monotone positive representatives, sound exclusions and full-length completeness. The a0 word is separately checked to have no positive survivor. The unexpected partial-sufficiency counterfactual fails on1101100 exactly as predicted.

All255 G67 extremizers with a2..256 admit both certificates; a1 admits neither. Minimal prefix-length frequencies (length:count) are0:1,2:2,4:15,5:32,6:57,7:68,8:35,9:24,10:11,12:6,13:2,15:2. Minimal suffix-length frequencies are0:1,3:2,5:2,6:7,7:21,8:35,9:87,10:62,11:11,13:23,15:2,18:2. Zero-depth exclusion is the a2 word, whose ceiling is0; it does not imply a zero-length word or a nontrivial residue constraint.

Post-control diagnostics identify the two maximum-depth cases as a200 and253: prefix15, suffix18 containing11 ones. The largest sampled ceiling is19584 at a253. These are descriptive finite maxima, not preregistered depth bounds, asymptotic rates or evidence of independence. All256 individual records are retained outside git; the probe reproduces them with an optional output-file argument. Probe: `tests/probes/prizes/collatz_gpt_endpoint_certificates.py`; Python on GPT's Intel host, about6 s. No control failed.

The bounded instrument audit is complete; independent proof review remains pending. Next reasoning/source audit: whether established lower bounds for linear forms in logarithms give a uniform polynomial envelope for G67's near-resonance denominator, and what that envelope actually says about counts. No such bound is claimed yet, and it would not by itself prove an actual survival estimate. No larger census or additional run is started here.


### G.GPT69. polynomial first-deficit ceiling (second-read by Local, 2026-10-06)

### G69. Known logarithmic bounds give a polynomial first-deficit ceiling (2026-10-06)

G67's ceiling is unbounded, but it has a uniform polynomial envelope in the deficit time. This is a consequence of established logarithmic lower bounds, not a new transcendence result or a prize solution.

**Source and hypotheses.** [Rozier–Terracol arXiv:2502.00948v3, Proposition6.3](https://arxiv.org/html/2502.00948v3#S6) states Rhin's effective bound: for integer coefficients and H=max(abs(u1),abs(u2))>=2, abs(u0+u1*log2+u2*log3)>=H^(-13.3). Here log denotes the natural logarithm of the indicated number, not a base-two logarithm. Read the proposition and its application in Section6; the original1987 Rhin proof was not read. Their subsequent finiteness argument additionally uses conjectural orbit bounds. We use only the stated unconditional logarithmic inequality, not those conjectural hypotheses. The numerical exponent is source-attributed and awaits independent reading.

For a first-deficit word with a>=1 ones and t=ceil(a*log2(3)), let A=3^a, D=2^t-A, and

    lambda=t*ln(2)-a*ln(3)>0.

Since t>=2 and t>a, the cited bound applies with u0=0,u1=t,u2=-a,H=t. Thus

    D/A=exp(lambda)-1>lambda>=t^(-13.3).

G67 gives B<=a*A/3 for every word in this barrier class, so

    K=floor(B/D)<a*t^13.3/3<t^14.3/3.

The zero-ones first-deficit word has no positive survivor. Therefore every positive actual start surviving at its first coefficient deficit at time t satisfies n<t^14.3/3. Its positive terminal value obeys the same bound by G68. The displayed inequality is strict because exp(lambda)-1>lambda.

**A limited count consequence.** Let E_t be the set of positive integers whose coefficient first falls below1 at time t but whose actual trajectory has not fallen below its own start through that time. Every member lies in the same interval[1,t^14.3/3), irrespective of which parity word realizes it. Hence

    abs(E_t)<=floor(t^14.3/3)<=floor(t^15/3),
    abs(E_t intersection[1,2^t])/2^t<=t^14.3/(3*2^t)->0.

The harmless floor bound is still valid when the strict cutoff is an integer. At each fixed t this also bounds starts beyond the least-residue period, since the ceiling bounds all positive lifts. No independence or residue-density multiplication is used. This is a polynomial bound on actual exceptions at a specified first deficit, not the number of all non-stopped starts at horizon t. Summing polynomial bounds over unbounded t gives no finite total. It does not prove that E_t is empty for n>=2, rule out coefficient stopping time infinity, or establish the open tail-survivor estimate of COLLATZ-PRIZE.md §1.

**Independent weaker source route.** [Languasco–Luca–Moree–Togbé, Theorem2.1](https://link.springer.com/article/10.1007/s12188-025-00293-9) states the rational positive-number form of Matveev's theorem. With numbers2,3 and exponents t,-a, it gives D/A>(e*t)^(-C), where C=1.4*30^5*2^(9/2)*ln(2)*ln(3). Combining with G67 yields K<(a/3)*(e*t)^C, again polynomial with a very large exponent. Its theorem hypotheses and application to prime-power gaps were read. This independently supplies the qualitative polynomial conclusion without relying on the sharper source-attributed13.3 exponent. Neither underlying logarithmic proof has been reproduced here.

**Unexpected scope guard.** At horizon1 all positive odd starts have T(n)=(3n+1)/2>=n and coefficient3/2>1. This is an unbounded set of actual survivors. It cannot satisfy G69's polynomial endpoint cutoff because no coefficient deficit has occurred. Thus interpreting the exceptional-first-deficit count as a bound on all horizon survivors would be false. G46's unbounded formal ceilings are also consistent with polynomial growth; polynomial does not mean uniformly bounded.

**Next controls, preregistered NOT RUN.** LF1: a1..256, t=bit_length(3^a), exact integer check D^10*t^133>A^10 (the weaker consequence D/A>t^(-13.3)), and K^10*3^10<a^10*t^133 for G67's maximum ceiling. These are finite application controls, not a verification of Rhin's theorem. LF2: reuse exactly791 first-deficit words throughlength16 and their independently evolved positive surviving lifts; require all such starts and terminals to satisfy3*n<t^15 and3*q<t^15, and their counts at each time to respect the coarse cutoff. No larger census. Counterfactual: the same cutoff bounds all horizon survivors without a deficit; refute analytically at horizon1 with unbounded odd starts. Independent proof/source reading requested.


### G69 controls outcome (2026-10-06)

LF1 passes256 exact integer denominator and maximum-ceiling inequalities; no floating logarithms or fractional powers were used. LF2 passes the existing791 first-deficit words throughlength16, independently evolving their sole positive survivor at t2,n1 and checking the coarse start/terminal/count cutoffs. The no-deficit horizon counterfactual is refuted analytically by all positive odd starts; the probe retains n3 as an exact witness. Probe: `tests/probes/prizes/collatz_gpt_logarithmic_ceiling.py`; Python on GPT's Intel host, under1 s. No control failed. These validate finite applications, not the deep logarithmic theorem. The bounded application audit is complete; independent source/proof reading remains pending. G70 records the finite-horizon count consequence separately.

*Second reader's note on G67, G68 and G69 (Local, 2026-10-06; chat L037).* All three correct (G69 conditional on the
cited Rhin bound, which neither of us has re-proved). G67: the prefix before the $(i+1)$-st odd step has $i$ ones in
$p_i$ steps, so $3^i > 2^{p_i}$ and $p_i \le \lfloor i \log_2 3 \rfloor$; the latest positions are simultaneously
admissible (strictly increasing since $\log_2 3 > 1$, every intermediate prefix above 1, first failure at
$t = \lceil a \log_2 3 \rceil$) and maximize $B$ componentwise; $B_{\max}/3^a = \tfrac13 \sum_i 2^{-\{i \log_2 3\}}$ gives the
envelope. G68: $q - n = (B - Dn)/M = (B - Dq)/A$, so start and terminal share the ceiling; the prefix and suffix
congruences and the nesting hold, and the 1101100 guard reproduces $(K, r, y) = (1, 59, 38)$. G69:
$D/A = e^\lambda - 1 > \lambda \ge t^{-13.3}$ with $H = t$ (as $t > a$), so $K < a t^{13.3}/3$; the scope guard at
horizon 1 is right.
Checked independently (`collatz_audit_g67_g69.py`): G67 on all 81,119 first-deficit words to length 24 (each class's
maximum unique and equal to $B_{\max}(a)$, $a \le 15$) and the envelope to $a = 399$; G68's identities, lift counts and
prefix-certificate soundness on every first-deficit word to length 20; G69's two exact consequences for
$a = 1$ to 2000, where the least observed $\log(D/A)/\log t$ is $-1.585$, far inside the cited $-13.3$.

### G.GPT70. finite-horizon count bridge (second-read by Local, 2026-10-06)

### G70. Polynomial additive error between actual and coefficient survival counts (2026-10-06)

G69 has a direct finite-horizon consequence for the open counting lane. Let A(T) be the set of positive starts whose actual iterates stay at or above their start through every step1..T. Let C(T) be the set whose coefficient3^(a_j)/2^j is at least1 at every such prefix. Nonnegative affine offsets give C(T) subset A(T).

If n belongs to A(T) but not C(T), its coefficient has a first deficit at some j<=T. Since its actual orbit still survives that step, G69 applies and gives

    n<j^14.3/3<=T^14.3/3.

Thus, with R(T)=T^14.3/3,

    A(T) symmetric_difference C(T) subset[1,R(T)),
    A(T) intersection[R(T),infinity)
       =C(T) intersection[R(T),infinity).

This uses only the source-attributed unconditional logarithmic bound and G67's barrier envelope. No bound on an orbit's stopping time is assumed. Starts of infinite coefficient stopping time are in C(T) for every finite T and are not excluded by this argument.

For any finite integer interval I, the additive count discrepancy satisfies

    0<=abs(A(T) intersection I)-abs(C(T) intersection I)
      <=abs(I intersection[1,R(T)))<=floor(R(T)).

There is no factor T from summing over possible first-deficit times: their exceptional starts all lie below the same monotonically increasing cutoff. The bound holds for every finite interval, including intervals shorter than a parity modulus; G46's rounding warning is respected. It is a polynomial additive error, not a relative error when the desired count is small.

In particular, for the width-w interval I_w=[2^(w-1),2^w), exact equality of both counts is guaranteed when

    3^10*2^(10*(w-1))>=T^143.

This is the exact integer form of2^(w-1)>=R(T). The coarser criterion3*2^(w-1)>=T^15 also suffices. For any fixed positive constant c and horizons T<=c*w, either criterion eventually holds as w increases. Consequently, in that asymptotic linear-horizon regime, an actual-versus-coefficient discrepancy is not the missing obstacle. The open part remains counting coefficient-surviving itineraries realized by ordinary starts beyond their free binary digits; their distribution is not proved here. No usable universal threshold or small-width equality follows without evaluating the criterion.

**Unexpected small-start guard.** The start1 survives forever on1,2,1,2,..., whereas its coefficient first falls below1 at step2. Hence1 belongs to A(2) but not C(2). Exact equality cannot be asserted at every start merely because the high-start counts agree. Moreover polynomial additive error alone cannot certify that a target count is below1. G69's odd-start/no-deficit guard and G67's offset-order reversal remain intact.

This is a direct corollary of G69 and the already recorded affine survival formulation, with no novelty claim or prize conclusion. Independent Local reading requested.

**Next controls, preregistered NOT RUN.** HC1: direct actual trajectories for n1..4096 through32 steps, independently accumulate coefficient counts, and at every horizon check set inclusion, the exact tenth-power cutoff for every discrepancy, and the interval count difference bound. Predict no inclusion/cutoff failure; retain the n1 discrepancy rather than discarding it. HC2: for T=ceil(3*w/2), w2..256, evaluate the exact integer criterion and record its truth intervals; predict failure at w32 and success at w256, with no first-threshold prediction. Counterfactual: A(T)=C(T) at all positive starts; refute at n1,T2. These are bounded controls, not a large stopping census or a proof of the beyond-free-bits distribution.

*Second reader's note on G70 (Local, 2026-10-06; chat L038).* Correct, conditional on G69's cited bound. Nonnegative
offsets give $C(T) \subseteq A(T)$; a start in $A(T) \setminus C(T)$ survives its first deficit at some $j \le T$, so G69
gives $n < j^{14.3}/3 \le T^{14.3}/3$, and the discrepancy is additive with no factor $T$; the tenth-power form is exact.
Checked by direct trajectories (`collatz_audit_g67_g69.py`, G70 part): for every $n < 65{,}536$ and $T \le 40$, $C(T)$ lies
inside $A(T)$ and the only discrepancy start is $n = 1$; with $T = \lceil 3w/2 \rceil$ the exact width criterion first
holds at $w = 104$.

### G70 controls outcome and independent review (2026-10-06)

HC1 passes131072 start/horizon pairs (n1..4096,T1..32) and384 width/horizon interval-count checks. The sole discrepancy start is1, at all31 horizons2..32; it is retained. The exact tenth-power cutoff holds for every discrepancy, and coefficient survival implies actual survival in every sample. Limitation: only the4096 horizon1 samples lie in the guaranteed-equality region. Thus this small-start run checks the formulas and counterexample, not direct large-width equality at later horizons.

HC2's exact integer calculation for T=ceil(3*w/2), w2..256, finds the criterion false on2..103 and true on104..256. Its predicted failure at32 and success at256 both hold; the first threshold104 was a descriptive outcome, not a prediction. The all-start equality counterfactual fails at n1,T2 as planned. Probe: `tests/probes/prizes/collatz_gpt_count_bridge.py`; Python on GPT's Intel host, under1 s. No control failed.

Local L038 independently reviewed G70, preserving the cited-logarithmic-bound qualification, checked starts below65536 through40 steps and independently obtained threshold104. Local's larger scope is credited separately; GPT did not repeat it. G60-G70's offline review queue is now complete in PROOFS.md §E2 (L035-L038); G69/G70 use the published Rhin theorem as stated, with its original proof unaudited by either party. The bounded Collatz ceiling/certificate block is complete.

Next reasoning target: isolate the coefficient-survivor count loss at the first step beyond w-1 free bits, using the critical odd-count class and terminal parity in G38/G43. This must concern the specific barrier event, preserve G42's resonance and G44's failure of an all-cylinder comparison, and avoid recasting the generic cancellation problem as solved. No new experiment is registered or launched in this checkpoint.

### G.GPT71. selected critical-boundary losses (second-read by Local, 2026-10-06)

### G71. First paid-bit discrepancy and the critical-boundary loss process (2026-10-06)

Resume the coefficient count of COLLATZ-PRIZE.md §1. G70 separates it from actual survival on sufficiently high intervals; this section concerns coefficient survival only. It specializes the already recorded parity bijection, G38's terminal recursion and G43's binary reader. No novelty claim, mixing estimate or tail-count theorem.

Let ell_t be the least nonnegative integer a with3^a>=2^t (ell_0=0). At t>0 equality of these powers is impossible, so this is also the coefficient-admissible endpoint threshold. Its increments are0 or1. Call step t to t+1 critical when ell_(t+1)=ell_t+1. Let V(t) count length-t words whose every prefix has coefficient at least1. At a critical step, let N(t) count those words with exactly ell_t ones; otherwise put N(t)=0. A child of such a critical-boundary word fails iff its new bit is0. All other admitted parents have two admitted children. Therefore

    V(t+1)=2*V(t)-N(t).

**The first step after the free bits.** Fix width w>=2 and m=w-1. Every admitted length-m word has one representative r in[0,2^m), and exactly one width-w start n=2^m+r. If it has a ones and terminal q=T^m(r), its actual state at the free-bit boundary is y=3^a+q. Since3^a is odd, its next parity is1 minus the parity of q.

Let C_w(t) count coefficient-surviving starts in[2^m,2^(m+1)) through horizon t. At a critical step m to m+1, write O(m) for the number of critical-boundary parents with q odd, and

    F(m)=sum over critical-boundary parents of (-1)^q
        =N(m)-2*O(m).

At a noncritical step put O(m)=F(m)=0. Only the parents counted by O(m) fail the next barrier, because q odd means y even. Thus

    C_w(w)=V(m)-O(m),
    2*C_w(w)-V(w)=F(m).

The coin benchmark2^(w-1)*P(w) equals V(w)/2, so the signed first-paid-bit discrepancy is exactly F(m)/2. At noncritical steps it is zero regardless of the terminal distribution. At critical steps it is the parity imbalance of one selected endpoint class, not the imbalance of the whole admitted ensemble. G43 expresses this reader as a weighted ternary spectrum; no cancellation for this selected class is established here.

**An exact selected-event loss process for later steps.** For any t, among the width-w coefficient survivors let E_w(t) count those with a_t=ell_t and even current state, provided the step is critical; otherwise set E_w(t)=0. Then

    C_w(t+1)=C_w(t)-E_w(t).

No claim of conditional fairness is made. When C_w(t)>0 define h_w(t)=E_w(t)/C_w(t), and put h_coin(t)=N(t)/(2*V(t)). With Q_w(t)=2^(w-1)*V(t)/2^t and R_w(t)=C_w(t)/Q_w(t),

    R_w(t+1)=R_w(t)*(1-h_w(t))/(1-h_coin(t)).

This formula includes a zero next count; logarithms may be taken only while both consecutive counts are positive. At t=m, R_w(m)=1 by the free-bit bijection. Hence bounded excess requires control of the accumulated selected-event hazard discrepancy after m. Noncritical steps contribute no loss on either side. This is an exact reduction of the desired count, not a proof of its boundedness or an independence model. It neither requires nor establishes G44's invalid all-cylinder comparison, and G42's resonances remain retained obstacles to generic Fourier arguments.

**Unexpected parity-sign guard.** At w2,m1 there is one admitted parent word1, r1,q2. Its width-two start is n3 with actual iterates3,5,8, so the next bit is1 and it survives the critical step. Thus C_2(2)=1,V(2)=1,F(1)=1, giving discrepancy+1/2. Counting q-even parents as losses instead would give C_2(2)=0 and the wrong sign. This exact two-step example checks the odd lift3^a; no experiment was needed to derive it. C_w is not asserted to equal the actual-survival count for every small width; G70's stated criterion governs that comparison.

**Next controls, preregistered NOT RUN.** BT1: m1..12, enumerate admitted parity words and their least representatives, compare the selected-class N/O/F formula with independently evolved width-(m+1) coefficient counts at horizon m+1. Predict exact equality, and zero discrepancy on every noncritical step; retain signed discrepancies on critical steps. BT2: widths2..10 through24 steps, direct trajectories and independent integer dynamic programming for V(t), checking the boundary-loss recurrence and exact rational ratio identity from the free-bit boundary onward. Retain zero counts and restrict probability/log identities to their stated domain. Counterfactual: q-even parents are the failing ones after the upper-half lift; must fail at width2. These are bounded controls, not a larger stopping scan or a uniform Fourier-transfer assertion. Independent Local reading requested.

### G71 controls outcome (2026-10-06)

BT1 passes507 admitted parents across m1..12. Retained rows(m,N,O,F,C) are(1,1,0,1,1),(2,0,0,0,1),(3,1,0,1,2),(4,2,1,0,2),(5,0,0,0,4),(6,3,0,3,8),(7,7,3,1,10),(8,0,0,0,19),(9,12,7,-2,31),(10,0,0,0,64),(11,30,14,2,114),(12,85,44,-3,182). First-paid-bit discrepancy F/2 has both signs; no one-sided bias law is inferred. Noncritical rows have F0 exactly.

BT2 passes171 boundary-loss recurrences,117 exact rational ratio identities and54 zero-parent steps at widths2..10 through24 steps. Zero counts are retained; no conditional probabilities or logarithms were taken on empty ensembles. The unexpected q-even-loss counterfactual fails at width2, whose direct count is1 rather than0. Probe: `tests/probes/prizes/collatz_gpt_boundary_loss.py`; Python on GPT's Intel host, under1 s. No control failed. These check identities, not a bound on accumulated hazard discrepancy. Next G72 examines admitted terminal multiplicity rather than assume a sign for the observed bias. Local's width40 run remains a separate claimed lane.

*Second reader's note on G71 (Local, 2026-10-06; chat L039).* Correct. An admitted parent with $a > \ell_t$, or any parent
at a noncritical step, has two admitted children, and a parent with $a = \ell_t$ at a critical step loses exactly its
0-child, so $V(t+1) = 2V(t) - N(t)$. At the free-bit boundary the width-$w$ start's state is $y = 3^a + q$, so its next
parity is $1 - (q \bmod 2)$; hence $C_w(w) = V(m) - O(m)$ and $2C_w(w) - V(w) = F(m)$. Later, $C_w(t+1) = C_w(t) - E_w(t)$,
and $V(t+1)/(2V(t)) = 1 - h_{\mathrm{coin}}(t)$ gives the ratio identity with $R_w(m) = 1$. The width-2 guard reproduces
($3 \to 5 \to 8$, discrepancy $+1/2$). Checked by direct trajectories (`collatz_audit_g67_g69.py`, G71 part): the
recurrence for $V$ to $T = 30$, and for every width 2 to 15 the free-bit equality, the first-paid-bit identity and the
loss process at every step to horizon 30.

### G.GPT72. admitted terminal multiplicity (second-read by Local, 2026-10-06)

### G72. A polynomial bound on admitted terminal multiplicity (2026-10-06)

Continue the selected coefficient-survivor ensemble, respecting Local's separate width40 counting claim. Fix m>=1. For each coefficient-admissible length-m word w, let r be its least representative, a its odd count, B its intercept, and q=T^m(r). The corresponding width-(m+1) start is n=2^m+r, with terminal y=3^a+q. The parity bijection, least-terminal-residue lemma and G67's barrier position bound are already recorded; the following is an elementary synthesis with no novelty or mixing claim.

**Offset interval.** Every admissible word obeys p_i<=floor(i*log2(3)), by the proper prefix before its(i+1)-st odd step. Thus B<=B_max(a) from G67, even when m is not its first-deficit length. This is an upper bound only; its extremizer need not fit length m. The increasing positions also satisfy p_i>=i, giving

    B>=sum_i 3^(a-1-i)*2^i=3^a-2^a.

At a fixed terminal q and odd count a,2^m*q=3^a*r+B. Distinct representatives r have distinct offsets B separated by multiples of3^a. The number of such offsets in the indicated interval, and therefore the fibre size, is at most

    L(a)=1+floor((B_max(a)-(3^a-2^a))/3^a)
        <=1+floor(a/3).

The conservative last bound follows from G67's B_max<=a*3^a/3 and positivity of the lower endpoint. No monotonicity or tightness of L(a) is asserted.

**The upper-half terminal labels its odd count.** The least-residue lemma gives0<=q<3^a, hence

    3^a<=y<2*3^a.

These intervals are disjoint for distinct a. Therefore y determines a, and the same L(a) bound holds for its full fibre across all admitted odd-count classes. In particular the terminal map from admitted width-(m+1) starts has multiplicity at most L_m=max_(1<=a<=m)L(a)<=1+floor(m/3).

For a uniform distribution on N admitted starts, each terminal atom has probability at most L_m/N. Since y is deterministic, its Shannon entropy in bits satisfies

    H(y)>=log2(N)-log2(L_m).

This bounds loss of initial information by a logarithmic quantity. It does not assert terminal residues are uniform, independent or fair in either base. G44's sparse-cylinder obstruction remains intact.

**Why this is relevant to the selected event.** Starts in the same terminal fibre have the same a and the same future integer orbit. Their future coefficient-barrier status is therefore identical: at d more steps it depends on3^(a+future_odd_count)/2^(m+d), not the original representative. Future coefficient counts can consequently be written as sums of fibre sizes over a selected terminal set, with each weight at most L_m. This does not give the selected set's size relative to its coin probability. In particular the bound is not a uniform all-cylinder density comparison, and it gives no bounded hazard debt by itself. Actual survival compares iterates with the original start and is a separate predicate; no fibre equivalence is claimed for that predicate.

**Unexpected barrier guard.** At m6, the width-seven starts85,84,80 have parity words100000,001000,000010 and all end at y4 after six steps. Their odd count is a1 and the fibre size is3, whereas L(1)=1. These words are not coefficient-admissible: the first has a deficit at step2 and the other two at step1. Thus dropping the barrier invalidates the multiplicity bound. More generally all m words with one odd step have terminal q in{1,2}, giving unbounded unrestricted multiplicity as m grows. The disjoint odd-count terminal intervals alone do not control multiplicity.

**Next controls, preregistered NOT RUN.** FM1: reuse admitted words at m1..12 (the BT1 population), independently evolve the upper-half starts, verify their terminal odd-count labels, offset interval and exact L(a) fibre bound, recording all non-singleton fibres if any. FM2: for those fibres, compare coefficient-survival statuses through eight additional steps by independent evolution of each start; verify agreement within a fibre and the weighted selected-terminal count. Predict no bound/label/status failure; no collision frequency prediction. Counterfactual: the same L(a) holds without the barrier; must fail on the three m6,a1 starts above. These are bounded controls, not Local's width40 job or an asymptotic entropy measurement. Independent Local reading requested.


### G72 controls outcome (2026-10-06)

FM1 passes507 admitted starts across m1..12, independently comparing parity-word specifications with upper-half trajectories, odd-count terminal labels, offset intervals and exact L(a) bounds. They give507 distinct terminal values: no non-singleton admitted fibre occurs in this sample. Thus it does not empirically exercise the multiplicity bound on an actual admitted collision. FM2 passes4563 future coefficient-status checks and108 weighted selected-terminal counts through eight additional steps. The unexpected unrestricted m6,a1 guard has all three starts85,84,80 end at4 and refutes dropping admission, as predicted.

Probe: `tests/probes/prizes/collatz_gpt_terminal_fibres.py`; Python on GPT's Intel host, under1 s. No control failed. Entropy remains an analytic consequence, not an estimated limit or a measurement. Cloud's documentation sweep is read and preserved; Local's width40 counting claim remains separate. The following addendum strengthens the algebraic statement rather than enlarge the sample to find a collision.

### G72 addendum: merging starts are close; a short input label restores injectivity (2026-10-06)

The same proof yields more than a cardinality bound. If two admitted width-(m+1) starts n,n' have the same terminal y, they have the same odd count a. Their affine identities imply

    3^a*(n-n')=B'-B,
    abs(n-n')<a/3<=m/3.

The strict inequality uses B_max<=a*3^a/3 and the positive lower intercept3^a-2^a. All admitted starts are odd, since a first even step would immediately violate the coefficient barrier. Their offsets in a fixed terminal fibre are therefore spaced by multiples of2*3^a. The sharper bound is

    L_odd(a)=1+floor((B_max(a)-(3^a-2^a))/(2*3^a))
            <=ceil(a/6).

The final inequality follows from a fibre's span being strictly less than a/3 and spacing at least2. It is a conservative bound, not an assertion of attainable collisions. The terminal entropy bound improves by replacing L_m with max L_odd(a)<=ceil(m/6).

Let s be the least nonnegative integer with3*2^s>=m. Then the map

    n -> (terminal y, n modulo2^s)

is injective on the admitted width-(m+1) ensemble. Equal labels would make the nonzero difference at least2^s>=m/3, contradicting the strict span bound. Since s=O(log m) and s<=m, the low-input label can equivalently be given by the first s parity bits, by the known parity bijection. At s0 the modulus is1. This is exact reconstruction with a short side label, not a fairness or future-distribution statement.

**Unexpected admission guard for the stronger claim.** At m9, unrestricted odd starts625 and597 both have a2 and terminal11. Their parity words are101000000 and100000001; their trajectories are625,938,469,704,352,176,88,44,22,11 and597,896,448,224,112,56,28,14,7,11. Their low residues modulo4 agree (both1), as do their first two parities10, so the joint label is not injective. Here s2 since3*4>=9. Both have already had coefficient deficits, at steps4 and2 respectively. Their difference28 also violates the admitted span bound9/3. This exact counterexample strengthens the original barrier guard without asserting any admitted collision.

**Next control, preregistered NOT RUN.** FM3: on the same admitted m1..12 population, check L_odd(a), the strict fibre-span bound, and injectivity of both short labels (y,low input residue) and(y,first s parities), including modulus1. Predict no failure; the existing FM1 result says these samples have no admitted non-singleton fibres, so this sample does not empirically exercise the collision-span case. Independently evolve the two unrestricted m9 guard trajectories and require their matching labels and failure of admission. No larger census or Local compute job. This addendum is a direct algebraic refinement, not a new asymptotic count theorem; independent reading requested.


### G72 short-label controls outcome (2026-10-06)

FM3 passes507 admitted starts/507 terminal fibres at m1..12, checking sharp odd-input multiplicity bounds, strict spans, low-residue labels and parity-prefix labels. Four admitted starts exercise modulus1. There are still no admitted non-singleton fibres in this sample, so its collision-span cases are not empirically exercised. The unrestricted625/597 guard trajectories are independently checked: both end at11 after9 steps with a2, share both short labels, and fail admission and the span bound. Probe mode: `tests/probes/prizes/collatz_gpt_terminal_fibres.py --short-labels`; predictions atfc268ed, Python on GPT's Intel host, under1 s. No control failed; no larger population was run. G73 extends the analytic result to specified finite tail horizons.


### G.GPT73. finite-tail short-label reconstruction (second-read by Local, 2026-10-06)

### G73. Short-label reconstruction throughout a finite coefficient-surviving tail (2026-10-06)

G72's reconstruction extends beyond its free-bit boundary. Fix width w=m+1 with m>=1, and horizon1<=t<=3*2^m. Consider only starts n in[2^m,2^(m+1)) whose coefficients have survived every prefix through t. If their odd count is a, intercept B and terminal y, then

    2^t*y=3^a*n+B,
    0<B/3^a<=a/3<=t/3<=2^m.

The offset bound is G67's proper-prefix position argument, valid for every admitted word; no first-deficit or logarithmic theorem is used. Therefore

    3^a*2^m<=2^t*y<3^(a+1)*2^m.

The upper bound is strict since n<2^(m+1). These disjoint bands determine a from y at the known width and horizon. No rounded logarithm is needed: compare the displayed integers.

If two admitted starts have the same y, they have the same a. G72's offset interval and first-bit parity now give

    abs(n-n')<a/3<=t/3,
    fibre size<=L_odd(a)<=ceil(a/6)<=ceil(t/6).

Let s(t) be the least nonnegative integer with3*2^s>=t. The label(y,n modulo2^s), equivalently(y,the first s parities), is injective on the ensemble. Indeed a nonzero difference sharing the input label would be at least2^s>=t/3. Here s<=m by the horizon hypothesis, and s<=t; the indicated prefix is available. For a uniform nonempty surviving ensemble of size N_t, H(y)>=log2(N_t)-log2(ceil(t/6)). All these statements concern surviving initial inputs at a specified time, not entropy generated by an orbit.

The exact inverse carry is also small:

    n=floor(2^t*y/3^a)-floor(B/3^a),
    0<=floor(B/3^a)<=floor(a/3).

This follows by taking the floor of n+B/3^a. It supplies a bounded correction after the terminal's odd-count label has been identified; it does not assert that the correction is uniformly distributed or independent of y.

This covers any fixed linear horizon t<=c*w eventually in width. It is a structural statement about the ensemble underlying G71's selected losses. It does not bound its surviving cardinality, its accumulated hazard discrepancy or future parity bias. G44's finite-information obstruction is consistent with it. Local's width40 count job is not needed or duplicated. The proof is an elementary extension of recorded affine/barrier lemmas, with no novelty claim.

**Unexpected admission guard.** At width4,horizon13, unrestricted starts9 and13 both end at1 but have respectively6 and5 odd steps. Their trajectories are9,14,7,11,17,26,13,20,10,5,8,4,2,1 and13,20,10,5,8,4,2,1,2,1,2,1,2,1. The horizon condition13<=3*8 holds, but both had their first coefficient deficit at step2. Thus a terminal need not identify the odd count once admission is removed. This is separate from G72's same-odd-count hash collision guard.

**Next controls, preregistered NOT RUN.** AT1: reuse widths2..10 through24 steps, direct coefficient-survivor trajectories; at every horizon satisfying t<=3*2^(w-1), verify exact bands, odd-count uniqueness, fibre span/multiplicity, short-label injectivity and the inverse carry. Predict no failure; retain zero ensembles and all non-singleton fibres if any. AT2: independently evolve the width4,horizon13 guard, record the two odd counts and first-deficit times; the unrestricted odd-count-identification counterfactual must fail. No larger census, empirical entropy claim or mixing prediction. Independent Local reading requested.


### G73 controls outcome (2026-10-06)

AT1 passes2313 admitted start/horizon samples and2313 terminal fibres at widths2..10 through24 steps, restricted to t<=3*2^(w-1). Exact bands, inverse carries, multiplicities, strict spans and both short labels pass. All27 empty ensembles are retained. No admitted non-singleton fibre occurs, so these controls do not empirically exercise merging or estimate entropy. AT2 independently verifies the width4,horizon13 trajectories: starts9 and13 end at1 with odd counts6 and5, respectively, and both first fail the coefficient barrier at step2. The unexpected unrestricted odd-count-identification counterfactual fails as predicted.

Probe: `tests/probes/prizes/collatz_gpt_tail_labels.py`; predictions at773b424, Python on GPT's Intel host, under1 s. No control failed. The reconstruction block is complete, with independent reading pending. Next reasoning returns to G71's critical-event hazard: small fibres and disjoint odd-count bands do not by themselves control the even/odd allocation inside a selected critical class. No larger census or Local count job is duplicated.

*Second reader's note on G72 (with its addendum) and G73 (Local, 2026-10-06; chat L040).* All correct. Every admitted
word has $i \le p_i \le \lfloor i \log_2 3 \rfloor$, so $3^a - 2^a \le B \le B_{\max}(a)$; equal terminals at fixed $a$ force offsets
congruent modulo $3^a$ (modulo $2 \cdot 3^a$ once one notes that admitted starts are odd), which gives $L(a)$ and
$L_{\mathrm{odd}}(a)$ and the strict span $|n - n'| < a/3$; the least-terminal-residue bound $0 \le q < 3^a$ makes
$y = 3^a + q$ label $a$, and G73's band $3^a 2^m \le 2^t y < 3^{a+1} 2^m$ does the same up to horizon $3 \cdot 2^m$. The
85/84/80 and 625/597 guards check. Checked independently (`collatz_audit_g67_g69.py`, G72/G73 part): the band labels
on 22,854 admitted samples (widths 2 to 18, several horizons each). As in GPT's own controls, no admitted collision
occurred anywhere in that population, so the fibre bounds remain proved but unexercised; whether admitted fibres
are always singletons is an open question (a collision needs odd starts at distance below $a/3$, so $a \ge 7$).

### G.GPT74. backward survival weights (second-read by Local, 2026-10-06)

### G74. Backward survival weights isolate the final count discrepancy (2026-10-06)

G71's hazard ratio is exact but changes both the critical-class occupancy and its parity allocation. A standard backward-equation telescoping argument instead writes the final additive discrepancy directly in terms of parity imbalances at each odd count. This is an application of finite first-step analysis, not a novelty or mixing claim; prior-art scope is recorded in PRIOR-ART.md.

Fix w=m+1, m>=1 and final horizon T>=m. Let K_w(t,a) count width-w starts coefficient-admitted through t with a odd steps. Let I_w(t,a) be the number of these starts with odd current state minus the number with even current state. Counts include multiplicity of starts, even if terminal states merge. Put I=0 for absent classes.

Define f_t(a) as the probability that independent fair future parity bits survive every coefficient barrier from the already-admitted state (t,a) through T. Set f_t(a)=0 when a<ell_t, f_T(a)=1 when a>=ell_T. For admitted a and t<T, first-step analysis gives

    f_t(a)=(f_(t+1)(a)+f_(t+1)(a+1))/2,
    Delta_t(a)=f_(t+1)(a+1)-f_(t+1)(a).

The definition extends f_t to every integer a; a killed state stays killed. Coupling the same future bits from a and a+1 proves monotonicity in a. Hence0<=Delta_t(a)<=1. Also Delta_t(a)=0 for a>=ell_T, since either child then survives even an all-zero future. Only admitted classes with ell_t<=a<ell_T can contribute.

Let H_t=sum_a K_w(t,a)*f_t(a). An odd actual current state sends its input to a+1; an even state sends it to a. Inadmissible children have f=0, matching their removal. Subtracting the fair average for each parent gives exactly

    H_(t+1)-H_t=(1/2)*sum_a I_w(t,a)*Delta_t(a).

At the free-bit boundary K_w(m,a) equals the number of admitted length-m words with a ones, by the parity bijection. Therefore H_m=Q_w(T)=2^m*V(T)/2^T, while H_T=C_w(T). Telescoping proves

    C_w(T)-Q_w(T)
      =(1/2)*sum_(t=m)^(T-1) sum_a I_w(t,a)*Delta_t(a).

This includes T=m (empty sum) and empty later ensembles. It requires no conditional probabilities of the actual ensemble and no positive-count assumption. In particular

    abs(C_w(T)-Q_w(T))
      <=(1/2)*sum_(t=m)^(T-1) sum_a abs(I_w(t,a))*Delta_t(a).

The weights have a concrete interpretation. Take fair bits for steps t+2 through T, with cumulative ones Z_k and Z_0=0. Put

    J=max_(j=t+1)^T (ell_j-Z_(j-t-1)).

A child with a ones survives precisely when a>=J. Thus Delta_t(a)=Pr(J=a+1). Over all integer a these weights sum to1. On the actual admitted classes their sum is at most1; consequently the previous bound is at most half the sum over t of max_a abs(I_w(t,a)). This coarse bound is not known to be small. The sharper weighted signed sum is the selected object; no cancellation, bounded excess or exponential count rate is proved.

**Unexpected immediate-loss guard.** Width3 has a single admitted start at m2: n7, with trace7,11,17,26,13 through T4 and odd counts1,2,3,3. Step2 to3 is noncritical (ell_2=ell_3=2), yet I_w(2,2)=1 and Delta_2(2)=1/2, since f_3(2)=1/2 and f_3(3)=1. Its contribution is1/4. At step3 the only class is a3, where Delta_3(3)=0. Here V(4)=3, Q_w(4)=3/4 and C_w(4)=1: the entire additive discrepancy comes from a noncritical step. Dropping noncritical terms from this formula gives0, incorrectly. This does not contradict G71: noncritical steps have no immediate count loss, but their parity allocation changes a later critical-class occupancy.

**Next controls, preregistered NOT RUN.** BW1: widths2..10, every final T from m through24; compute rational backward f and independent direct survivor states, verify each H increment, the final telescoping identity, monotone/nonnegative weights and the weighted absolute bound. Retain zero ensembles and separate noncritical contributions. Predict exact equality and no bound failure, without predicting the signs or a decay rate. BW2: for final T<=10, independently enumerate future coin strings to check the J distribution against backward Delta on every integer a in its support. Counterfactual: only critical steps contribute to the additive sum; must fail on width3,T4 as above. No large stopping scan, entropy measurement or Local job. Independent Local reading requested; next controls are an instrument check, not a proof of the count conjecture.


### G74 controls outcome (2026-10-06)

BW1 passes180 width/final-horizon cases and1740 exact rational H increments at widths2..10, T=m..24. All516 empty-parent increments are retained; terminal telescoping, nonnegative weights and the weighted absolute bound pass. BW2 independently enumerates future coin strings for T1..10 and matches440 backward weights to the maximum-demand distribution. The unexpected critical-only counterfactual is refuted: width3,T4 has total discrepancy1/4 and noncritical contribution1/4.

Probe: `tests/probes/prizes/collatz_gpt_backward_weights.py`; preregistration at4a78c0b, GPT's Intel host, Python, under1 s. No control failed. These validate the finite identity and its guard, not a uniform bound or cancellation rate. Independent Local proof reading remains pending. Next reasoning should target the signed weighted sum, rather than discard noncritical steps or substitute a bound on terminal information loss.

### G.GPT75. backward coin atom bound (second-read by Local, 2026-10-06)

### G75. A uniform atom bound for the backward coin weights (2026-10-06)

G74's weights can be bounded without any assumption on the actual Collatz ensemble. Write h=T-t-1>=0 for the number of future coin bits after the selected child. For every integer L>=1,

    max_a Delta_t(a)
      <=min(1, L/sqrt(h+1)+32*exp(-(L-1)/2)).

Choosing L=ceil(4*ln(h+1))+1 proves a uniform O(log(h+1)/sqrt(h+1)) bound as h tends to infinity. This controls the coin completion weights only. It neither bounds actual class imbalances nor proves bounded count excess.

**Proof.** Use G74's future-bit count Z_h and maximum demand J. Reverse the h fair bits and write S_k=Z_h-Z_(h-k), with S_0=0. Algebra gives

    J=ell_T-Z_h+R,
    R=max_(0<=k<=h) (S_k-(ell_T-ell_(T-k))).

Here R is a nonnegative integer, since k0 contributes0. Let beta=log(2)/log(3). The ceiling identity ell_j=ceil(beta*j) implies ell_T-ell_(T-k)>beta*k-1. The exact inequality3^5<2^8 gives beta>5/8. For integer r>=1, R>=r therefore requires some k>=1 with

    S_k-k/2>r-1+k/8.

For completeness the needed fair-binomial tail estimate is elementary: E exp(theta*(S_k-k/2))=cosh(theta/2)^k<=exp(k*theta^2/8). The inequality follows from tanh(u)<=u for u>=0 by integration. Markov's inequality, optimized at theta=4*x/k, gives Pr(S_k-k/2>=x)<=exp(-2*x^2/k) for x>=0. Apply this with x=r-1+k/8 and take a union bound; independence of different suffix sums is not required. Since

    2*(r-1+k/8)^2/k >= (r-1)/2+k/32,

we obtain

    Pr(R>=r)<=exp(-(r-1)/2)*sum_(k>=1) exp(-k/32)
             <32*exp(-(r-1)/2).

The central atom of Binomial(h,1/2) is at most1/sqrt(h+1). One direct proof: for h=2j its maximum is p_(2j)=binom(2j,j)/4^j; p_0=1 and p_(2j+2)/p_(2j)=(2j+1)/(2j+2). Induction uses (2j+1)*(2j+3)<(2j+2)^2 to give p_(2j)<=1/sqrt(2j+1). The odd maximum p_(2j+1)=p_(2j)*(2j+1)/(2j+2) is at most1/sqrt(2j+2).

For any integer v, split the event J=v into R0..L-1 and R>=L. Each small-R event is contained in Z_h=ell_T+r-v, regardless of dependence between R and Z_h. Thus

    Pr(J=v)<=sum_(r=0)^(L-1) Pr(Z_h=ell_T+r-v)+Pr(R>=L),

which gives the displayed bound and, for the stated L, tail term at most32/(h+1)^2. Since Delta_t(a)=Pr(J=a+1), the claim follows. The h0 case is included, though its bound is simply1. This is a standard concentration-plus-truncation argument, not a new probability theorem; prior art is recorded separately.

**Unexpected dependence guard.** Take T3,t1,h1. Then ell_2=ell_3=2, so J=max(2,2-Z_1)=2, while R=Z_1. Its demand distribution has an atom of1, even though Z_1 has maximum atom1/2. Dropping R, or importing the binomial atom bound directly for J, is wrong. The proof above keeps the dependence and its truncation cost. It also shows why no short-horizon square-root estimate with constant1 is asserted.

**Next controls, preregistered NOT RUN.** WA1: reuse G74's complete future-string population T1..10. For each word verify the reverse decomposition, then compare exact R tail probabilities to the conservative geometric bound for every attained positive r, and each J atom to the displayed bound for L1..8. Predict no failure; retain bounds above1 as vacuous rather than evidence of sharpness. WA2: verify the central-binomial induction inequality by exact squared-integer comparisons for h0..256, and independently enumerate the T3,t1 guard. Counterfactual: max atom of J never exceeds max atom of Binomial(h,1/2); must fail at h1 above. No actual-orbit distribution measurement, asymptotic constant estimate or large Local job. Independent proof reading requested.


### G75 controls outcome (2026-10-06)

WA1 passes2036 exact reverse decompositions across all future coin strings for T1..10,57 overshoot-tail comparisons and1304 atom comparisons for L1..8. All1304 atom bounds are vacuous (the uncapped expression exceeds1) at this deliberately small scope: this run does not empirically exercise a nontrivial atom bound or measure decay. Tail and atom exponential comparisons use floating arithmetic with1e-14 tolerance, while probabilities and reverse identities are exact. WA2 passes257 exact squared-integer central-binomial bounds for h0..256. The unexpected T3,t1 guard is confirmed: J has an atom of1 and R equals the fair bit, refuting the direct binomial-atom shortcut.

Probe: `tests/probes/prizes/collatz_gpt_weight_atoms.py`; predictions at51a1a0e, GPT's Intel host, Python, under1 s. No control failed. The asymptotic atom bound remains the analytic result, pending independent reading; the small controls do not demonstrate its asymptotic usefulness. No actual-orbit or Local computational job was run. The remaining count problem is to control actual signed class imbalances against these weights.

*Second reader's note on G74 and G75 (Local, 2026-10-06; chat L041).* Both correct. G74: an odd parent's child has
$f_{t+1}(a+1) = f_t(a) + \Delta/2$ and an even parent's $f_{t+1}(a) = f_t(a) - \Delta/2$, so
$H_{t+1} - H_t = \tfrac12 \sum_a I \Delta$; $H_m = 2^m V(T)/2^T$ because every admitted length-$T$ word has an admitted
length-$m$ prefix; and a child survives exactly when $a \ge J$, so $\Delta_t(a) = \Pr(J = a + 1)$; the width-3 guard
checks. G75: with $j = T - k$ the demand is $J = \ell_T - Z_h + R$; $3^5 < 2^8$ gives $\beta > 5/8$; the Hoeffding tail and
$\sum_k e^{-k/32} < 32$ hold; the central-atom induction rests on $(2j+1)(2j+3) < (2j+2)^2$; the $T = 3$ guard checks.
Checked independently (`collatz_audit_g67_g69.py`): G74's telescoping identity in exact rationals in 180 cases
(widths 2 to 13, $T = m$ to $m + 14$, direct trajectories); G75's bound against the exact distribution of $J$ by dynamic
programming, which makes the bound non-vacuous for the first time (0.977 at $h = 200$, 0.822 at $h = 300$, against exact
maximum atoms 0.058 and 0.047). The exact atoms decay like $1/\sqrt{h}$ with no visible logarithm (ratio 1.55 from
$h = 128$ to 300 against $\sqrt{300/128} = 1.53$), so the bound's $\log$ factor looks like a cost of the proof.

### G.GPT77. coarse triangle bootstrap obstruction (second-read by Local, 2026-10-06)


### G77. Which triangle estimate the signed diagnostic does and does not exclude (2026-10-06)

The count target is an upper bound on C_w(T)/Q_w(T), not a small cancellation factor A/abs(D). From G76, C=Q+D<=Q+A. Therefore a uniform estimate A<=B*Q would suffice to give C/Q<=1+B, or excess at most log2(1+B) bits whenever C>0. Cancellation is one possible mechanism, not a necessary assumption for that upper-bound strategy.

**Unexpected normalization guard.** G76's largest positive-count cancellation factor2155/88 (width10,T20) has A/Q=2155/3416<1, D/Q=-11/427 and C/Q=416/427. A triangle estimate already gives C/Q<=1+2155/3416<2 in that case. Thus a large A/abs(D) does not refute a useful bound on A/Q. This is an exact consequence of the retained rational row, not a new run. The full small sample's maximum A/Q=1033093/95527 also supplies no uniform constant at larger width.

A particular coarse use of G75, however, cannot close a horizon-independent estimate. For h>=0 put

    b(h)=min(1, inf over integer L>=1 of
                  (L/sqrt(h+1)+32*exp(-(L-1)/2))).

Each term inside the infimum is at least1/sqrt(h+1), so b(h)>=1/sqrt(h+1). Since sum_a abs(I_w(t,a))<=C_w(t), G74-G75 give

    A_w(T)<= (1/2)*sum_(t=m)^(T-1) b(T-t-1)*C_w(t).

Suppose one substitutes the desired bootstrap C_w(t)<=K*Q_w(t) at all preceding horizons. Q_w(t) is nonincreasing, because the coin survivor probability is nonincreasing. Consequently the resulting sufficient upper bound has the form

    A_w(T)/Q_w(T) <= K*B_(m,T),
    B_(m,T)=(1/2)*sum_(t=m)^(T-1)
                       b(T-t-1)*Q_w(t)/Q_w(T),
    B_(m,T)>=sqrt(T-m+1)-1.

The last inequality follows from the preceding lower bound on b and sum_(j=1)^d j^(-1/2)>=2*(sqrt(d+1)-1), with d=T-m. Thus the coefficient in this particular sufficient estimate grows with the paid-tail length. It cannot certify a uniform B or close a fixed-K induction simply by substituting the same coarse count bound. This is a statement about the estimate's right-hand side, not a lower bound on the true A or D and not a refutation of the count conjecture. It remains valid along linear horizons where the paid tail grows with width.

**Route status.** Close only the route that takes the maximum coin weight, replaces every class imbalance by its full class size, and feeds a uniform count bootstrap into that bound. A sharper triangle estimate retaining the actual odd-count allocation, or cancellation in the signed sum, remains open. The next reasoning question is whether the barrier-demand weights suppress classes carrying most of the actual mass, rather than taking their maximum. No new experiment is proposed in this audit; G74-G76 identities and the exact normalization guard are the controls. Independent Local reading requested. This is elementary accounting of recorded bounds, with no novelty claim.

### G.GPT78. ideal allocation proxy obstruction (second-read by Local, 2026-10-06)

### G78. Even ideal coin-class allocation leaves a growing full-class proxy (2026-10-06)

G77 leaves allocation-aware triangle estimates open. One qualification is needed: merely matching the coin odd-count allocation does not make the bound from replacing abs(I) by K uniformly small. Define v(t,a) as the number of admitted length-t words with a ones and

    q_w(t,a)=2^m*v(t,a)/2^t,
    U_coin(m,T)=(1/2)*sum_(t=m)^(T-1) sum_a q_w(t,a)*Delta_t(a).

These are ideal coin class masses and their full-class proxy, not actual Collatz measurements. Let d=T-m. Choose a length-T admitted word uniformly, and let Z_tail be its number of ones after the first m bits. Then exactly

    U_coin(m,T)/Q_w(T)=E[2*Z_tail-d | admitted through T].

**Proof.** Keep the admitted first-m-bit ensemble with one unit of mass per word and replace only the d future bits by independent bits of odd probability p. Its final mass is the finite polynomial

    F(p)=sum over admitted length-T words of p^z*(1-p)^(d-z),

where z=Z_tail. Thus F(1/2)=V(T)/2^d=Q_w(T), and differentiation gives

    F'(1/2)/(2*F(1/2))=E[2*Z_tail-d | admitted through T].

Independently, differentiate one tail coordinate at a time. An admitted prefix at time t has mass q_w(t,a) when all tail coordinates are fair. Making its next bit odd rather than even changes its future completion probability by Delta_t(a). A prefix already killed contributes0. The coordinate sum is therefore F'(1/2)=sum_(t=m)^(T-1) sum_a q_w(t,a)*Delta_t(a)=2*U_coin. This is the finite increasing-event differentiation formula often called Margulis-Russo; the complete specialization is proved here and no external theorem is required.

Since each surviving full word has at least ell_T ones and its prefix at most m, Z_tail>=ell_T-m. Consequently

    U_coin(m,T)/Q_w(T)>=2*ell_T-T-m.

In particular beta=log(2)/log(3)>5/8 gives, at T=8*m with m>=1,

    U_coin(m,8*m)/Q_w(8*m)>m.

The ideal full-class proxy thus grows along a fixed linear horizon. A classwise comparison K_w(t,a)<=K*q_w(t,a), followed by abs(I_w(t,a))<=K_w(t,a), yields A_w(T)<=K*U_coin(m,T). Its sufficient right-hand side cannot establish a uniform A/Q bound by itself. This is not a lower bound on actual A: in an exactly fair coin ensemble the signed class imbalance vanishes, even though the proxy is positive. Sharper estimates for actual abs(I), or a signed cancellation argument, remain open. No assertion is made that actual classwise domination holds.

**Unexpected proxy-versus-error guard.** At m2,T5 the four admitted full words have tail words011,101,110,111. Their tail signed counts2*z-3 are1,1,1,3, with mean3/2. Here Q=1/2 and U_coin=3/4. Ideal fairness has zero count discrepancy despite that positive proxy. Replacing a zero imbalance by the full class size is therefore a substantive loss, not just a change of normalization.

**Next controls, preregistered NOT RUN.** PC1: m1..8,T=m..24, compute U_coin by exact rational backward weights and compare it with an independent forward integer recurrence for admitted word counts and summed tail odd counts. Predict identity and the endpoint lower bound; retain T=m. PC2: coin dynamic programming only, m1..32,T=8*m; verify the strict lower bound U_coin/Q>m by the moment formula and independently enumerate the m2,T5 guard. Counterfactual: an ideal fair ensemble's full-class proxy equals its signed discrepancy0; must fail on the positive3/4 guard. No actual-start scan, Local job, or empirical claim about actual class domination. Independent Local reading requested.


### G78 controls outcome (2026-10-06)

PC1 passes164 exact rational backward-proxy/forward-tail-moment comparisons at m1..8,T=m..24, including8 empty-tail cases. Endpoint lower bounds pass. PC2 passes32 exact strict inequalities U_coin(m,8*m)/Q_w(8*m)>m for m1..32, using integer counts and moments only. Independently enumerating the m2,T5 words gives tails011,101,110,111, normalized proxy3/2 and proxy3/4, refuting equality with the ideal fair ensemble's zero signed discrepancy.

Probe: `tests/probes/prizes/collatz_gpt_coin_proxy.py`; predictions at14fde39, GPT's Intel host, Python, under1 s. No control failed. The asymptotic obstruction is proved in G78; these are finite instrument checks. No actual-start population, classwise-domination claim or Local computational job was run. Independent proof reading remains pending.

*Second reader's note on G77 and G78 (Local, 2026-10-06; chat L042).* Both correct. G77: $C = Q + D \le Q + A$; each
term of the infimum is at least $1/\sqrt{h+1}$, so $b(h) \ge 1/\sqrt{h+1}$; $\sum_a |I| \le C_w(t)$; with $Q$ nonincreasing
the bootstrap coefficient is at least $\tfrac12 \sum_{j \le d} j^{-1/2} \ge \sqrt{d+1} - 1$, which closes only that coarse
route. G78: $F(\tfrac12) = V(T)/2^d = Q$, and both the derivative of $F$ and Russo's coordinate sum give
$U_{\mathrm{coin}}/Q = E[2Z_{\mathrm{tail}} - d]$; every surviving word has at least $\ell_T$ ones, so the ratio is at least
$2\ell_T - T - m$, which exceeds $m$ at $T = 8m$ because $\beta > 5/8$; the $m = 2$, $T = 5$ guard reproduces. Checked
by coin dynamic programming (`collatz_audit_g67_g69.py`, G77/G78 part): the moment identity, the endpoint bound and
the bootstrap floor on 104 $(m, T)$ cases, and $U/Q > m$ at $T = 8m$ for every $m < 200$.

### G.GPT80. interior mixed-pair cancellation (second-read by Local, 2026-10-06)

### G80. Interior mixed pairs cancel the first backward difference (2026-10-06)

G76's opposite-sign contributions sometimes cancel for a structural reason. Fix final T and two consecutive steps from t to t+2<=T. Consider one actual input still coefficient-admitted at time t, with a odd steps, and assume

    a>=ell_(t+1).

This means both choices of the first bit would pass the intermediate barrier. Since ell increases by at most1 per step, either mixed pair01 or10 also passes the endpoint barrier with a+1 ones. This statement concerns coefficient admission only, not actual survival relative to the original input.

Write F(j)=f_(t+2)(j), with the same killed-state extension as G74. Two backward fair steps give

    f_t(a)=(F(a)+2*F(a+1)+F(a+2))/4.

Indeed both intermediate states a and a+1 are admitted, so their first-step recursions apply. For either actual mixed pair, the sum of that input's two signed G74 contributions is therefore exactly

    F(a+1)-f_t(a)
      =(2*F(a+1)-F(a)-F(a+2))/4.

The first differences have cancelled, leaving a second difference. The result is independent of which mixed order the actual orbit takes. No bijection between actual01 and10 inputs, swapped orbit realization or equality of their terminal integers is asserted. It is cancellation between times along one actual input, using the coin completion potential.

**Exact block accounting.** Partition the paid tail into disjoint two-step blocks starting at m,m+2,..., leaving one final step if needed. For each alive input in a block, use the displayed curvature contribution only when it has a mixed pair and the intermediate condition holds. Every other case uses its literal potential change f_(t+2)(a_after)-f_t(a_before), with endpoint potential0 if the input dies during the block. Sum over inputs alive at the block's start. Intermediate cancellations telescope, giving C_w(T)-Q_w(T) exactly after adding the possible last step. This does not bound the number or mass of mixed blocks, the curvature, or the remaining00/11 and boundary terms. G42's Fourier resonance and G44's information guards remain intact; no generic contraction claim follows.

**Unexpected barrier guard.** At width2,m1,t1,a1,T3, the start3 has current5 and actual pair10, finishing at8 with a2. It passes both actual steps. But ell_2=2>a1, so alternative01 is killed immediately. Here f_1(1)=1/2 and f_3(2)=1, giving literal contribution1/2. The unjustified curvature formula instead gives(2*1-0-1)/4=1/4. A mixed endpoint alone does not license the two-step fair recursion at its inadmissible intermediate state.

**Recorded interior example.** Width3,T5,start7 has at t2 the actual pair10, a2 and ell_3=2. G76 records its two contributions+1/4,-1/4. Here F(2)=0,F(3)=1/2,F(4)=1, so the curvature contribution is0, explaining this exact cancellation without an independence assumption.

**Next controls, preregistered NOT RUN.** MP1: reuse widths2..10,T=m..24 and direct states, verify the curvature identity on every interior mixed block, retaining all boundary mixed blocks separately. MP2: verify disjoint block accounting against the independent final count/coin difference for all180 cases, including inputs killed inside blocks, empty ensembles and odd tail lengths. Predict exact equality; make no mixed-block frequency or curvature-size prediction. Independently evolve both guards and require interior0 and boundary1/2 versus invalid1/4. Counterfactual: the curvature formula applies to every mixed block; must fail on the boundary guard. No larger population or Local job. Independent Local reading requested. This is an elementary two-step application of G74's backward equation, not a new asymptotic cancellation theorem.


### G80 controls outcome (2026-10-06)

MP1 passes2925 interior mixed-block curvature identities in the existing width2..10,T=m..24 scope. All257 surviving boundary mixed blocks are retained separately. MP2's disjoint block accounting matches independent direct final count minus coin benchmark in all180 cases, including753 block inputs killed during their block,88 odd tail lengths and57 empty final ensembles. These repeated block counts are instrument controls, not estimates of an asymptotic mixed-block frequency. The two independently evolved guards pass: interior contribution0, boundary contribution1/2 versus unjustified curvature1/4. The unexpected unrestricted-curvature counterfactual is refuted.

Probe: `tests/probes/prizes/collatz_gpt_mixed_curvature.py`; predictions ata4645cf, GPT's Intel host, Python, under1 s. No control failed. The exact local cancellation and block identity remain pending independent reading; no bound on total curvature, boundary mass or equal-bit blocks is established. No larger actual population or Local job was run.

### G.GPT81. offset-code collision reduction (second-read by Local, 2026-10-06)

### G81. Reduce the admitted-collision question to offset residues (2026-10-06)

Reply to Local L040. Absence of a collision in both finite start samples is not a singleton theorem. There is a finite coding question for each odd count that avoids a larger actual-start scan.

Fix a>=1 and t_a=floor(log_2(3^a)), computed as bit_length(3^a)-1. Let W_a contain every length-t_a coefficient-admitted parity word with exactly a ones. For each word use its affine intercept B. Then a pair of distinct words in W_a with equal B modulo3^a exists if and only if there exists a same-odd-count admitted terminal collision (at some horizon and within a common dyadic width). In particular this is equivalent to a collision somewhere in G73's width/horizon domain, where the terminal labels the odd count.

**Necessity and reduction to one horizon.** If two admitted starts meet after t steps with odd count a, their affine equations give

    3^a*(n'-n)=B-B'.

Their words are distinct, since the same affine map is injective in the start, and offsets agree modulo3^a. Admission implies t<=t_a. Pad both words with zeroes to length t_a. Their intercepts and odd counts stay unchanged and their coefficient prefixes remain admitted. These are abstract parity words; padding need not be the continuation of the original starts. The coding collision persists.

**Sufficiency and explicit realization.** Conversely take distinct words in W_a with intercepts B,B' congruent modulo A=3^a. Put M=2^t_a and delta=(B-B')/A. The offsets cannot be equal: equal A,B at this common length would give the same least parity representative, hence the same word. Thus delta!=0. Both intercepts are odd, since admission forces first bit1, so delta is even. G72's offset bound gives abs(delta)<a/3<M.

Let r=(-B*A^(-1)) modulo M be the least representative of the first word. Choose n=r+2*M if delta>0, and n=r+3*M if delta<0; put n'=n+delta. Both lie in[2*M,4*M), have the same width t_a+2, and are distinct positive odd integers. The residue congruence for B' holds because A*n'+B'=A*n+B. Thus they realize the two prescribed words by the parity bijection, and their terminals are equal. They are coefficient-admitted through t_a, and t_a<=3*2^(t_a+1), so this witness is within G73's domain. No actual-survival or prize solution is implied.

This also recovers L040's lower threshold: delta is a nonzero even integer and abs(delta)<a/3, so a>=7. For a<=6 the offset residue map is injective. For higher a its injectivity is an open coding question here. G73's short-label theorem does not prove it.

**Unexpected admission guard.** The unrestricted words101000000 and100000001 have a2 and intercepts7 and259, equal modulo9. They realize the recorded625/597 collision, since(7-259)/9=-28. Both first fail the coefficient barrier at step2 (their first two bits are10); neither belongs to W_2, whose maximal admitted horizon is3. Thus a modular collision below a7 does not refute the admitted threshold. This guard also distinguishes abstract padding of admitted words from extending a nonadmitted word backwards into the set.

**Next finite search, preregistered NOT RUN.** CI1: enumerate W_a for a1..12 using increasing odd positions with p_i<=floor(i*log_2(3)); independently check full-prefix admission and compare affine-recursion intercepts with the position sum. Require no residue collision for a1..6. CI2 blind prediction: no residue collision for a7..12; retain a refutation, and if one occurs construct and directly evolve the two witness starts above before asserting an admitted collision. Report word counts and all colliding residue groups (or their absence), without extrapolation. Independently check the unrestricted7/259 guard and its first deficits. Counterfactual: admission can be omitted from the a>=7 threshold; must fail on that guard. This is a small finite word-code search, not a repeated Local start population or a large compute job. The lemma uses the recorded Terras parity bijection and affine/barrier identities; no novelty claim. Independent Local reading requested.


### G81 offset-code outcome (2026-10-06)

CI1 checks all68722 fixed-cardinality position sets at a1..12 against independent full-prefix admission; exactly4403 admitted words remain. Counts by a are1,1,2,3,7,12,30,85,173,476,961,2652. Affine-recursion and position-sum intercepts and direct parity representatives agree. There are no colliding intercept residues in any of the12 classes. CI2 HELD: the blind no-collision prediction for a7..12 survives this complete finite search. Consequently, via G81, same-odd-count admitted collisions with a<=12 are excluded across widths and horizons, not just in one finite start interval. This is an exhaustive finite code verification with an analytic reduction; it is not an all-a singleton theorem or an asymptotic rarity estimate. G73's domain additionally ensures any terminal collision has the same odd count.

The unrestricted guard independently gives intercepts7/259, common terminal11 and first deficits2 for both starts625/597, refuting omission of admission. No collision witness could be constructed in this population because no code collision occurred; the constructive branch therefore remains empirically unexercised. Probe: `tests/probes/prizes/collatz_gpt_offset_codes.py`; predictions at9a9a46d (published via050f51c), GPT's Intel host, Python, under1 s. The first included-word pass was followed by the full excluded-set completeness control to check enumeration coverage; both passed. Independent Local reading and reproduction of the new reduction remain requested.

*Second reader's note on G80 and G81 (Local, 2026-10-06; chat L043).* Both correct. G80: with $a \ge \ell_{t+1}$ both
intermediate states are admitted, so $f_t(a) = (F(a) + 2F(a+1) + F(a+2))/4$, and a mixed pair's two contributions sum to the
second difference; the block accounting telescopes; the boundary guard shows why the condition is needed. Checked: the
two-step identity on all 6,376 admitted $(T, t, a)$ states with $T \le 30$, in exact rationals. G81: a collision gives
$3^a(n' - n) = B - B'$ and padding to $t_a$ keeps $B$ and admission; conversely $\delta = (B - B')/3^a$ is nonzero (equal
least representatives would give equal words), even (every admitted word starts with 1, so $B$ is odd) and below
$a/3 < M$ in size, so $n = r + 2M$ or $r + 3M$ and $n' = n + \delta$ realize both words with equal terminals; the 7/259 guard
checks. Checked independently with my own enumeration (`collatz_audit_g67_g69.py`, G81 part): the counts $|W_a|$ for
$a \le 12$ agree with GPT's, and **the search extends to $a = 17$** ($|W_a|$ = 8045, 17637, 51033, 108950, 312455 for
$a = 13$ to 17) **with no offset-residue collision**, so by G81 there is no same-odd-count admitted collision for
$a \le 17$ at any width or horizon.

### G.GPT82. localized coin overshoot and curvature (second-read by Local, 2026-10-06)

### G82. Localize the reverse overshoot: square-root atoms and inverse-horizon curvature (2026-10-06)

Reply to Local L041. The logarithm in G75 can be removed by truncating how far back the overshoot looks, instead of truncating its value. The remaining coin bits then are independent of the retained shift. This is a bound for the fair coin model, not the actual Collatz ensemble.

Take a demand J starting at time r=T-h with h future bits. Use G75's reversed suffix sums S_k and write

    J=ell_T-Z_h+R_h,
    R_h=max_(0<=k<=h)(S_k-(ell_T-ell_(T-k))).

For an integer8<=K<=h, define R_K by the same maximum restricted to k<=K, and J_K=ell_T-Z_h+R_K. Put n=h-K and eta=min(1,64*exp(-K/32)). Then, uniformly in r,T and integer v,

    Pr(J=v)<=min(1,1/sqrt(n+1)+eta),
    abs(Pr(J=v+1)-Pr(J=v))<=4/(n+1)+2*eta.

**Coupling error.** Since R_K>=0, R_h differs from R_K only if some k>K has S_k-(ell_T-ell_(T-k))>0. G75's rational slope bound beta>5/8 implies S_k-k/2>k/8-1. Here k>=9, so the threshold is positive. The proved fair-binomial tail estimate gives

    Pr(S_k-k/2>k/8-1)
      <=exp(-2*(k/8-1)^2/k)
      <=exp(1/2)*exp(-k/32).

Summing over k>K and using exp(1/2)<2 yields Pr(R_h!=R_K)<64*exp(-K/32). Thus J and J_K have a coupling with error at most eta. No independence between the full R_h and Z_h is used.

**Independent prefix.** Separate the first n coin bits from the last K. Their count Z_n is Binomial(n,1/2) and independent of the suffix variables S_K,R_K. Precisely

    J_K=ell_T-Z_n-S_K+R_K.

Its law is therefore a mixture of integer shifts of a reflected binomial distribution. The atom bound from G75 applies to each shift. For completeness a binomial mass p_n also has

    max_v abs(p_n(v+1)-p_n(v))<=4/(n+1).

To see this, split n into floor(n/2) and ceil(n/2), convolve their laws, and use the sup norm of the first mass times the l1 norm of the second mass's first difference. Binomial unimodality gives the latter as twice its maximum atom. G75's atom bounds give at most2/sqrt((floor(n/2)+1)*(ceil(n/2)+1))<=4/(n+1), including n0. Mixing shifts preserves both bounds. Coupling changes a single atom by at most eta and an adjacent-atom difference by at most2*eta, proving the claims.

Choose K=ceil(128*ln(h+1)). For sufficiently large h it lies between8 and h/2, and eta<=64/(h+1)^4. Hence

    max atom of J<=sqrt(2/(h+1))+64/(h+1)^4,
    max adjacent-atom difference<=8/(h+1)+128/(h+1)^4.

Thus G75's coin weights are O(h^(-1/2)), without the logarithm. For G80's mixed block use r=t+2 and h=T-t-2: its curvature is an adjacent-atom difference divided by4, so its magnitude is O(1/h) for long remaining horizons. Short horizons retain their literal bounds and boundary guards. Neither estimate controls how many actual blocks occur, their class mass, equal-bit blocks or the accumulated actual error; G77-G79's missing estimates remain missing.

**Unexpected suffix-shift guard.** At T3,r2,h1,K1 the single suffix bit b gives R_K=S_K=b and n0. Correctly J_K=2-0-b+b=2, with atom1. Omitting the suffix count from the shift would give2+b, a different distribution. Independence of the retained prefix does not permit dropping any correlated terms within the suffix. This also preserves L041's original atom1 dependence guard.

**Next controls, preregistered NOT RUN.** LW1: all future strings for T1..12 and every r with h=T-r, every K1..h: verify the window decomposition and the exact independent-prefix convolution law for J_K. Check total variation between J and J_K is at most their exact disagreement probability; for K>=8 compare disagreement with eta, explicitly retaining vacuous small-scope bounds. LW2: exact integer checks of the binomial first-difference bound for n0..256, plus arithmetic evaluation at h4096 and8192 of the chosen K and both displayed finite bounds; predict K<=h/2 and nonvacuous atom/curvature bounds. These two arithmetic evaluations are not distribution measurements. Independently enumerate the suffix-shift guard; counterfactual omitting S_K must fail. No actual-start scan, asymptotic fit or repeated Local h200/300 job. Independent Local reading requested; this is elementary concentration and convolution using the recorded backward equations, with no novelty claim.

*Second reader's note on G82 (Local, 2026-10-06; chat L044).* Correct. $R_h \ne R_K$ needs some $k > K$ with
$S_k - k/2 > k/8 - 1$, and $e^{1/2} \sum_{k > K} e^{-k/32} < 64 e^{-K/32}$; the last $K$ reversed bits carry $S_K$ and $R_K$ while the
first $n = h - K$ bits give an independent $Z_n$, so $J_K$ is a mixture of shifts of a reflected binomial; the split
convolution gives the first-difference bound $4/(n+1)$; coupling costs $\eta$ per atom and $2\eta$ per adjacent difference; the
suffix-shift guard checks. Checked exactly (`collatz_audit_g67_g69.py`, G82 part): the joint law of $(J, J_K)$ by dynamic
programming in 22 $(h, K)$ cases with $h \le 96$ (total variation $\le \Pr(J \ne J_K) \le \eta$; atom and adjacent-difference
bounds); the binomial first-difference bound for $n \le 256$; and at $h = 4096$ and 8192, $K = 1065$ and 1154 (both $\le h/2$)
with non-vacuous atom bounds 0.0221 and 0.0156 and curvature bounds 0.00195 and 0.00098. This answers L041: the
logarithm in G75 was a cost of the proof, and G82 removes it.

### G82 window controls outcome (2026-10-06)

LW1 passes163872 exact window decompositions and364 independent-prefix convolution/total-variation controls on all future strings for T1..12. All35 comparisons with the geometric window bound are vacuous at this small scope; the exact coupling comparisons remain separately verified. LW2 passes257 exact integer binomial first-difference controls for n0..256, including the unimodality l1 identity. Its arithmetic evaluations give(h,K,atom upper bound,curvature upper bound)=(4096,1065,0.01816,0.001319) and(8192,1154,0.01192,0.0005683). These are double-precision evaluations of the proved bounds, not observations of a demand distribution or empirical decay. The suffix-shift counterfactual is independently refuted: actual J is constant2, while omitting S_K gives2+b.

Probe: `tests/probes/prizes/collatz_gpt_window_smoothing.py`; predictions at42e96b1, GPT's Intel host, Python, about1 s. No control failed. The asymptotic improvement is analytic and independently reviewed by Local L044. No actual-start population or Local h200/300 distribution job was repeated, and no bound on actual block mass or total signed discrepancy is inferred.

### G.GPT83. forced initial parity and the spacing cutoff (second-read by Local, 2026-10-06)

### G83. Forced initial parity sharpens admitted fibre spacing (2026-10-06)

Reply L040/L043. Admission through step 2 forces both initial parity bits to be11: one odd step would leave coefficient3<4. Thus every admitted start at a horizon t>=2 is3 modulo 4. Any same-odd-count terminal collision has displacement delta=(B-B')/3^a divisible by 4, rather than merely even. At t = 1 the affine map with the admitted first bit1 is already injective; this short horizon must be handled separately.

For a>=2 pad the admitted words to t_a as in G81. Their intercepts lie between B_min=3^a-2^a (all a odd positions first) and G67's B_max. The lower bound follows termwise from p_i>=i; the all-ones prefix followed by zeroes is admitted through t_a and attains it. Define the exact normalized span

    R_a=(B_max-(3^a-2^a))/3^a.

In any fixed-a terminal fibre, distinct starts are separated by at least4 and their full span is at most R_a. Consequently

    fibre size <= 1+floor(R_a/4),
    R_a <= a/3-1+(2/3)^a.

This bound applies to the admitted words at any shorter horizon by padding, and to all terminal fibres in G73's domain because there the terminal labels a. It is a stronger multiplicity bound, not a proof of singleton fibres at every a.

**Analytic cutoff.** The right-hand side increases with a: its successive difference is(1-(2/3)^a)/3>0. At a = 14 it is11/3+(2/3)^14<4, since(2/3)^14<(2/3)^3=8/27<1/3. Hence R_a<4 for2<=a<=14, so delta must be zero and the affine map forces the starts to coincide. The a = 1 case has only the admitted length-one word. Therefore same-odd-count admitted collisions require a>=15. This explains more of L040's unexercised fibre bound analytically; L043's independent exhaustive code search already excludes a<=17, a stronger finite cutoff. No duplication of that search is requested.

The exact spans also have a simple recurrence, from appending the last term of B_max:

    R_(a+1)-R_a=2^floor(log_2(3^a))/3^(a+1)-(2/3)^a/3.

For a>=2 its first term exceeds1/6, while the subtracted term is at most4/27<1/6, so R_a strictly increases there; R_1=R_2=0. This identifies where the spacing bound can first stop proving injectivity, without searching words or claiming a collision actually exists.

**Unexpected short-horizon guard.** At t = 1, n = 1 is coefficient-admitted but is1 modulo 4, so the assertion that every admitted start is3 modulo 4 is false without t>=2. It does not refute injectivity at that horizon. The unrestricted625/597 guard remains outside admission and does not challenge the span bound, even though its displacement28 is divisible by 4.

**Next controls, preregistered NOT RUN.** FS1: exact integer intercept-span recurrence and monotonicity for a = 1 to 64, locate the first a with R_a>=4 (no numerical value predicted); require R_a<4 through 14. FS2: reuse the already covered a = 1 to 12 words to verify first11, the common offset residue5*3^(a-2) modulo 4 for a>=2, and the exact span bounds; independently check both short-horizon and unrestricted guards. Counterfactual: the3-modulo 4 requirement applies already at horizon1; must fail on n = 1. No new a = 13 to 17 enumeration or actual-start population. The derivation uses only the recorded affine/barrier identities and offset extrema; independent reading requested, no novelty or prize claim.

### G83 exact-span controls and stronger cutoff (2026-10-06)

FS1 passes 64 exact span bounds and63 recurrence comparisons. The first a with R_a>=4 is21, an unpredicted arithmetic outcome. The exact bracket is

    R_20=13805179460/3486784401<4,
    R_21=43561973452/10460353203>4.

G83's proved monotonicity therefore gives R_a<4 for every a<=20. Combining the exact integer evaluation with the spacing 4 argument analytically excludes same-odd-count admitted collisions through a = 20, across widths and horizons. This is not a new word enumeration; it strengthens Local L043's a<=17 finite code result using the extrema and a proved recurrence. At a = 21 the bound merely stops excluding a collision; no collision, frequency estimate or all-a singleton theorem follows.

FS2 passes 4403 existing a = 1 to 12 admitted words, checking initial11, common offset residue modulo 4 and exact extrema. Both guards pass, and unconditional3-modulo 4 at horizon1 is refuted on n = 1. Probe: `tests/probes/prizes/collatz_gpt_forced_spacing.py`; predictions ate9b1213, GPT Intel Python, under1 s. No control failed; no Local a = 13 to 17 search or actual-start population was repeated. Independent review of the new spacing lemma and strengthened cutoff remains pending.

*Second reader's note on G83 (Local, 2026-10-06; chat L046).* Correct. Admission through step 2 forces the bits 11,
so admitted starts at $t \ge 2$ are $3 \bmod 4$ and same-count displacements are multiples of 4; the span bound and
its recurrence are exact. Checked (`collatz_audit_g83_g89.py`, K2): over every admitted word the least intercept is
$3^a - 2^a$ and the greatest is G67's $B_{\max}$, for $a \le 22$; $R_a$ increases for $a \ge 2$ and obeys the bound
for $a \le 64$; $R_{20} < 4 < R_{21}$ with the stated fractions; $R_{22} = 4.438 < 8$. Independently, enumerating all
of $W_a$ with no pruning finds no realized same-count collision for any $a \le 21$ (K1), confirming the analytic cutoff
at 20 and, by a different method, G88's certificate at 21.

### G.GPT84. the prefix orientation of a first collision (second-read by Local, 2026-10-06)

### G84. The first possible collision has one prefix orientation (2026-10-06)

G83 leaves a = 21 as the first odd count not excluded by its exact spacing bound. Without enumerating those words, their first three bits sharply constrain any collision. This is a necessary condition, not existence.

For a>=3, split W_a into prefixes110 and111. Position extrema give

    min B_110=13*3^a/9-2^(a+1),
    max B_111=B_max-4*3^(a-3).

For the first formula, the earliest positions of a word 110 are0,1,3,4,...,a. The initial two terms sum to5*3^(a-2); the remaining terms are twice the corresponding all-ones-prefix terms. This sums to the displayed minimum. These earliest positions satisfy admission. For the second, G67's latest positions begin0,1,3; imposing111 replaces only position3 by 2, reducing the intercept by 4*3^(a-3). The remaining latest positions are unaffected, and the resulting word is admitted. Both bounds are attained within their classes. Thus the signed opposite-prefix difference obeys

    (B_111-B_110)/3^a <= R_a-16/27+(2/3)^a.

At a = 21, the right-hand side is exactly37365342780/10460353203<4, while4<R_21<8. Equal-terminal words with the same first three bits would realize starts equal modulo 8 (the parity-word bijection), hence have a nonzero displacement of magnitude at least8; the global span excludes this. Opposite-prefix words therefore are required. The signed bound excludes B_111>B_110 by 4*3^21 or more. Every possible collision must consequently have

    B_110-B_111=4*3^21,
    n_111=n_110+4,
    n_110=3 modulo 8, n_111=7 modulo 8.

The two parity representatives modulo 8 follow directly by evolving one odd start of each class for three steps. G81 realizes any code collision by actual positive starts; the necessity above holds for all realizing lifts. No candidate has been found, and no new a = 21 search is registered. The reduction narrows any future witness search rather than replaces the missing injectivity proof.

**Unexpected signed-direction guard.** At a = 3, W_110 consists of1101 with B23, and W_111 of1110 with B19. The reverse signed bound is-4/27, attained by(19-23)/27. It is not an absolute-difference bound: abs(19-23)/27=4/27. Replacing a directional bound by an absolute bound is the counterfactual refuted here. Also a = 2 has no111 class; the extrema formulas require a>=3.

**Next controls, preregistered NOT RUN.** PF1: reuse a = 3 to 12 admitted words to verify both attained prefix extrema and the signed inequality; independently check representatives3/7 modulo 8 and the a = 3 direction guard. PF2: exact integer verification of a = 21's two interval bounds and signed numerator. Require the stated necessity bounds to hold; do not infer or search for a collision. Report any failure, and record this as a continuation of the existing residue-code lane, not a duplicate of Local's a = 17 enumeration. Elementary affine/position reasoning from G67/G81/G83, no imported theorem or novelty claim; independent review requested.

### G84 prefix controls outcome (2026-10-06)

PF1 passes 10 attained-prefix-extrema pairs on 4401 existing admitted words at a = 3 to 12. Representatives3/7 modulo 8 and the signed-direction counterfactual check. PF2 verifies exactly4<R_21<8 and the reverse-direction bound12455114260/3486784401<4 (the reduced form of the stated fraction). No control failed; no a = 21 word or actual-start search occurred. Probe: `tests/probes/prizes/collatz_gpt_prefix_orientation.py`; predictions at4c2e796, GPT Intel Python, under1 s. Necessity only, with independent proof review pending.

*Second reader's note on G84 (Local, 2026-10-06; chat L046).* Correct. The two prefix extrema are attained on every
admitted word for $a = 3$ to 14 (K3), and the $a = 21$ numerator 37,365,342,780 is exact. At $a = 21$ the necessity
is vacuous (no collision exists, K1). The same argument applies at $a = 22$ ($R_{22} - 16/27 + (2/3)^{22} = 3.846 < 4$), and all five pairs found there have the 110 start lower and the 111 start upper, as it requires.

### G.GPT85. two further forced odd bits at a = 21 (second-read by Local, 2026-10-06)

### G85. Admission forces two further shared odd bits in a = 21 candidates (2026-10-06)

Continue G84's necessary a = 21 collision orientation. Let the smaller start n have prefix110 and the other start n+4 prefix111. After three steps their values are

    u=(9*n+5)/8, u'=(27*n+127)/8=3*u+14.

Thus these values have the same parity. Admission of the110 branch at step 4 requires its next bit1: retaining only two odd bits would leave9<16. Both values therefore take an odd step, giving v' =3*v+20 where v=(3*u+1)/2. These values again have the same parity. Admission of the lower branch at step 5 requires another odd bit, since27<32. Both take that odd step. Every a = 21 collision candidate must consequently have first five bits11011 and11111, respectively. By the parity bijection the lower start is27 modulo 32 and the upper31 modulo 32. After five steps their values satisfy w'=3*w+29, so they have opposite parity next; no further common-bit extension is asserted.

This is a conditional constraint on any collision, not its existence or an a = 21 exclusion. The global span bound still allows the positive intercept orientation, and these prefixes still attain its opposing extrema; this refinement does not by itself improve the cutoff20.

**Unexpected admission guard.** Starts3 and7 differ by 4 and begin110/111, but the lower branch fails coefficient admission at step 4. Its first five bits are11000, while the upper has11101. Thus displacement4 and the three-bit orientation alone do not imply the five-bit prefixes. The counterfactual omitting admission must fail on this pair.

**Next controls, preregistered NOT RUN.** FP1: direct exact trajectories for n=8*k+3 with0<=k<256 and n+4; whenever the lower start is coefficient-admitted through 5, require both five-bit prefixes, the three affine relations above, residues27/31 modulo 32 and opposite next parity. Do not require a terminal collision or infer one. FP2: separately check3/7 and the residue representatives27/31, retain failed admission in the guard. These are small algebra controls, not a new collision search or a Local computational job. Review requested; elementary recorded identities, no novelty claim.

### G85-G86 prefix and slack controls outcome (2026-10-06)

FP1-FP2 pass all 256 displacement-four pairs: 64 lower prefixes satisfy admission through five steps and have the required five-bit words, residues and affine relations; the 192 excluded prefixes are retained. SR1 confirms full and shifted admission of the 33-step word, fresh suffix deficit at step 26, and six-step states 107/121 with odd counts 5/5 for starts 27/31. Both counterfactuals are refuted. No control failed and no meeting pair was sought or asserted. Probe: `tests/probes/prizes/collatz_gpt_prefix_slack.py`; predictions at 2a8df48, published via aab6d7d, GPT Intel Python, under one second. Independent proof review remains pending.

### G.GPT86. the shifted barrier, a closed shortcut (second-read by Local, 2026-10-06)

### G86. Removing the common odd count does not preserve admission (2026-10-06)

A tempting continuation of G85 would reduce a = 21 collisions to the already excluded smaller odd counts by restarting after a short common-count prefix. This route fails: the coefficient barrier carries accumulated slack, and a suffix is not generally admitted relative to its own starting time.

In G85's possible sixth-bit branch(1,0), both trajectories have accumulated five odd steps after six steps. Their new states differ by 14: from w'=3*w+29, the odd/even updates give (3*w+1)/2 and (3*w+29)/2. If they eventually meet with a = 21, the remaining27-step suffixes have16 odd steps. But3^16=43046721<2^27, so neither suffix can satisfy the fresh coefficient barrier even at its endpoint. G83's cutoff through 20 cannot be applied to those suffixes. This is conditional reasoning, not an assertion that this collision branch exists.

The correct suffix condition after a prefix of length s and odd count j is

    3^(j+a_k)>=2^(s+k),

rather than3^a_k>=2^k. It depends on the accumulated prefix ratio. A fresh-admission injectivity proof is not thereby an injectivity proof for all such shifted barriers.

**Unexpected explicit slack guard.** The word 110111 followed by 16 ones and11 zeroes has length 33 and21 ones. Its first six coefficient prefixes are admitted; the subsequent ones increase the coefficient ratio, and among the trailing zeroes the endpoint is the smallest ratio, with3^21>2^33. Thus the full word is admitted. Its27-bit suffix1^16 0^11 first fails the fresh barrier at step 26, since2^25<3^16<2^26, while it remains admitted against the shifted barrier. This is an abstract parity word, realizable by the recorded parity bijection; no meeting pair is implied. Starts27/31 realize G85's six-bit branch and have new states 107/121, illustrating the displacement14 without claiming that they meet.

**Next control, preregistered NOT RUN.** SR1: exact prefix tests of this full word and suffix, require full admission, shifted suffix admission and fresh suffix first deficit26; direct27/31 six-step guard must give odd counts5/5 and states 107/121. Counterfactual that restarting preserves fresh admission must fail. No extended collision enumeration. Record this as a closed shortcut, not closure of the shifted-barrier problem or the original singleton question.

*Second reader's note on G85 and G86 (Local, 2026-10-06; chat L046).* Both correct. G85's affine relations
$u' = 3u + 14$, $v' = 3v + 20$, $w' = 3w + 29$ re-derived; the forced prefixes are vacuous at $a = 21$ and hold for
all five $a = 22$ pairs (11011 / 11111, lower start $27 \bmod 32$). G86 closes a real shortcut: the suffix condition
is $3^{j + a_k} \ge 2^{s + k}$, not a fresh barrier. Checked (K6): the 33-bit word is admitted; its 27-bit suffix
first fails the fresh barrier at 26 and is admitted against the shifted one.

### G.GPT87. the offset budget and the eight-bit prefix (second-read by Local, 2026-10-06)

### G87. The offset budget rules out one sixth-bit branch (2026-10-06)

Continue G84-G85 at odd count a = 21. After five steps the states obey w' = 3*w + 29 and therefore have opposite parity. The branch with lower bit 1 and upper bit 0 would give prefixes 110111 and 111110. For a >= 5 their attained extrema are

    max B_110111 = B_max - 32*3^(a-5),
    min B_111110 = 3^a + 32*3^(a-5) - 2^(a+1).

The first replaces G67's fifth odd position 6 by 5; later latest positions are unchanged. The second delays the earliest odd positions after the initial five ones by one place, if any remain. Both extremal words satisfy admission. Their normalized positive gap is consequently

    max (B_110111-B_111110)/3^a = R_a - 64/243 + (2/3)^a.

At a = 21 its numerator over 3^21 is 40809080460, less than 4*3^21 = 41841412812. G84 requires the positive offset gap to equal 4*3^21, so this branch is impossible for a collision. The sixth bits must instead be 0/1.

After that branch the states satisfy x' = 9*x + 44. Admission of the lower branch forces an odd seventh bit, since its four odd steps would otherwise give 81 < 128. Both states have the same parity, so both take an odd step and satisfy y' = 9*y + 62. The lower branch needs another odd bit at step eight, since 243 < 256, again forcing both; then z' = 9*z + 89. Thus every a = 21 candidate must begin 11011011/11111111, with starts 251/255 modulo 256. The ninth bits are opposite. No meeting pair has been found, and no a = 21 word search is registered.

**Unexpected minimum-offset correction guard.** At a = 5 the extremal words 1101110 and 1111100 have offsets 287 and 211. Their gap is 76/243. Omitting the positive (2/3)^a correction from the normalized formula would give only 44/243 and falsely exclude this valid gap. The correction is small at a = 21, but cannot be discarded from a uniform bound.

**Next controls, preregistered NOT RUN.** PB1: reuse existing a = 5 to 12 admitted words to check both attained sixth-prefix extrema and their gap formula. PB2: exact a = 21 integer comparison and direct first-eight-step controls on starts 251/255, including the three affine relations and opposite ninth parity; do not claim they meet. Require the formulas and necessary bound to hold. Counterfactual dropping the correction must fail on the a = 5 guard. No extended collision enumeration or Local job duplication. Independent reading requested; elementary recorded offset extrema.

### G87 prefix-budget controls outcome (2026-10-06)

PB1 passes eight attained sixth-prefix extrema pairs on 4396 existing words. PB2 verifies the exact a = 21 budget and eight-step affine guards; the omitted-correction counterfactual is refuted.

### G.GPT88. the paired-prefix collision certificate (second-read by Local, 2026-10-06)

### G88. Exact completion intervals support a bounded collision certificate (2026-10-06)

A paired-prefix search can test the remaining a = 21 question without enumerating all admitted words. Fix target a, horizon t_a, and an admitted prefix of length s, odd count j <= a and intercept B. If a-j > t_a-s there is no completion. Otherwise its attained completion extrema are

    B_min(prefix) = 3^(a-j)*B + 2^s*(3^(a-j)-2^(a-j)),
    B_max(prefix) = 3^(a-j)*B + sum_(i=j to a-1) 3^(a-1-i)*2^floor(log_2(3^i)).

The minimum puts remaining odd positions immediately after the prefix; odd steps increase the ratio, and the final ratio stays at least one, so this completion is admitted. The maximum puts each remaining odd step at its latest barrier-permitted position. Prefix admission implies s <= floor(log_2(3^j)), so none of those positions precedes the prefix. G67's deadline bound proves maximality termwise. Empty remaining sums give the same intercept for both extrema.

For a pair of prefixes from starts n and n+4, a meeting with equal target odd count requires final intercept difference 4*3^a. Prune only if this target is outside [min B_low - max B_high, max B_low - min B_high], or an admission/count/capacity condition fails. The common residue r modulo 2^s can be lifted as r or r+2^s; these exhaust the two next parity choices of the lower start. Each lift determines the upper next parity by its affine equation at r+4. Updating both intercepts and r therefore exhausts every possible paired extension. At depth t_a check the exact offset equality, then realize any witness using n = r + 2*2^t_a and n+4; these have a common width. A complete empty tree is a finite no-collision certificate, not an all-a theorem.

**Controls and capped run, preregistered NOT RUN.** CB1: compare complete tree results with independent direct residue scans for admitted a = 3 to 8, displacement 4; require equality. Unexpected positive control: omit admission, use horizon 9, odd count 2 and displacement 28; compare with the full 512-residue scan and require a nonempty witness set, directly checking every returned meeting. Use unrestricted latest-position extrema in this control, rather than the admitted formula. It exercises acceptance as well as rejection. CB2 blind prediction: no admitted collision at a = 21, displacement 4. Cap at 100000 visited nodes and five seconds; retain any cap failure without an exclusion claim. If complete, report visited/pruned/leaf counts and independently evolve every witness; a refuted blind prediction is retained. No a = 22 search or new large compute job. Prior code enumeration through a = 17 remains Local's result; this is a new bounded certificate method in GPT's reasoning lane. Publish before running and request independent review.

### G88 certificate controls and audit preregistration (2026-10-06)

CB1 passes six admitted tree/direct comparisons and 722 attained prefix-extrema controls. Its unexpected unrestricted positive case completes with 53 visited nodes, 24 pruned nodes and three accepting leaves: residues 85, 424 and 426 modulo 512. The independent direct scan verifies these meetings, so the witness-acceptance branch is exercised.

CB2 completes the a = 21, displacement-four tree in 59 visited nodes, with 30 pruned nodes and no accepting leaves. The blind no-collision prediction HELD. Neither the 100000-node nor five-second cap was reached; the combined probes took under one second on GPT's Intel host. Predictions and scripts were published at da98314. No control failed and no a = 22 search occurred. This complete finite search, together with G84's displacement reduction, supports exclusion of the a = 21 class. A separate residue-cover audit and independent proof review remain pending before marking the extension finalized. The a <= 20 result and its pending independent review are unchanged; no all-a or prize claim.

Probes: `tests/probes/prizes/collatz_gpt_sixth_branch.py` and `tests/probes/prizes/collatz_gpt_collision_tree.py`.

**Next independent audit, preregistered NOT RUN.** RC1: export the 30 rejected prefix residue classes, then verify each using independent direct prefix trajectories, completion-offset extrema and an explicit reason (admission, capacity, count or target outside the offset interval). Require pairwise disjoint classes and exact total covered mass 2^33, counting a length-s class as 2^(33-s) residues. Predict full coverage and no valid class rejected; retain any failure and reopen the a = 21 claim. Store the certificate data outside Git; publish the reproducible checker and its counts. This audits the implementation's coverage rather than rerunning a larger population. RC2 unexpected negative controls: delete one cut, duplicate a cut, and claim the whole root is rejectable; require the auditor to reject all three certificates for insufficient coverage, overlap and invalid arithmetic respectively. BN1, preregistered NOT RUN: after RC1-RC2 pass, test a = 22 to 24 with a cumulative 100000-node/five-second tree budget. Before each class verify its exact normalized span is less than 8; G83 then reduces every possible same-count collision to displacement 4. Blind prediction: no collision in these classes. Audit each complete empty tree with the independent residue-cover checker; stop on a witness, cap or failed span prerequisite and retain it. This is the only further range registered; no larger search or all-a inference.

### G88 residue-cover audit and retained blind refutation (2026-10-06)

RC1 passes: 30 pairwise disjoint rejected residue classes cover all 8589934592 residues modulo 2^33. Independent direct-prefix and position-sum checks justify 17 admission rejections and 13 offset-interval rejections. RC2 rejects a missing class, a duplicated class and an invalid root rejection for the predicted reasons. Thus the count-21 finite exclusion passes the separate coverage audit; independent model review remains pending.

BN1's blind no-collision prediction is REFUTED at a = 22. That tree completes in 647 visited nodes with 319 rejected nodes and five accepting leaves. It stops there as preregistered; a = 23 and 24 were not run. The span prerequisite R_22 < 8 passes. All five accepted residues yield positive same-width starts four apart, 22 odd steps each, coefficient admission at every prefix and equal terminals after 34 steps. Least-residue starts were additionally checked with two direct update formulas and independent odd-position intercept sums. The combined audit/search took under one second; no cap was reached. Predictions at 6c69d5e. No instrument control failed; the blind mathematical prediction failed and is retained.

Certificates and witness data are saved outside Git; the reproducible audit script is `tests/probes/prizes/collatz_gpt_cover_audit.py`. The a = 22 accepting/rejected partition has not yet had a separate coverage audit, so five found pairs is not yet asserted to be the exhaustive family count. The counterexamples themselves already refute all-a admitted injectivity.

**Next audit, preregistered NOT RUN.** RC3: independently check the a = 22 partition consisting of 319 rejected classes and five singleton accepting residues. Validate every rejection and every witness from direct trajectories and position sums, require disjointness and total mass 2^34, and reject a corrupted accepting residue. Also require the independent root span to be less than 8 and every accepted pair to first meet at step 34. Predict full coverage and five valid accepted classes; retain any failure. Do not resume the stopped a = 23–24 search. Independent Local review remains queued for return; this is not a prize candidate.

*Second reader's note on G87 and G88 (Local, 2026-10-06; chat L046).* Both correct. G87: the two sixth-prefix extrema
are attained for $a = 5$ to 14 (K3) and the $a = 21$ numerator $40{,}809{,}080{,}460 < 4 \cdot 3^{21}$ is exact; the
forced eight-bit prefixes 11011011 / 11111111 (starts 251 / 255 mod 256) also hold for all five $a = 22$ pairs, whose
ninth bits are opposite (0 / 1 in four pairs, 1 / 0 in one). G88: the completion extrema are attained for every
admitted prefix with $a = 2$ to 11 (K7, 7,496 prefixes), and the certificate's outcomes (empty at 21, five leaves at
22) agree exactly with the unpruned enumeration.

### G.GPT89. the first admitted collisions, at odd count 22 (second-read by Local, 2026-10-06)

### G89. Admitted terminal fibres are not always singletons (2026-10-06)

The count-22 run refutes the open all-a injectivity conjecture from L040. One explicit pair is

    n = 5348744187, n' = 5348744191,
    T^34(n) = T^34(n') = 9770112830.

Both starts have width 33. Their parity words, where 1 denotes an odd step of the halved Collatz map, are

    1101101101011011100110110110101101,
    1111111111011100100111011100001100.

Each word has 22 ones and satisfies 3^(prefix odd count) >= 2^(prefix length) at all 34 prefixes. This is checked by exact integer comparisons, separately from the actual trajectories. Their intercepts are B = 166780787837 and B' = 41256549401; their difference is 125524238436 = 4*3^22. The position-sum intercept formula and direct evolutions independently verify

    2^34*9770112830 = 3^22*5348744187 + 166780787837
                      = 3^22*5348744191 + 41256549401.

Thus the meeting is within G73's admitted common-width domain. It does not contradict G72-G73's multiplicity or short-label reconstruction theorems, which allow multiplicity; it refutes the unproved singleton conjecture. Since R_22 < 8, G83 bounds each same-count fibre by two, and this pair attains that bound.

**Infinite lift families.** For every integer k >= 0 add k*2^34 to both starts. The parity bijection preserves both 34-bit words and admission, and the common terminal becomes 9770112830 + k*3^22. For k = 0 their common width is directly checked. For k >= 1 both lie strictly inside the same length-2^34 interval, and every relevant power-of-two width boundary is an endpoint of such an interval; their widths therefore agree. This gives infinitely many admitted meeting pairs at the one horizon 34, not an asymptotic collision density.

Five least-residue pairs were independently validated; exhaustive enumeration of the accepting partition remains under RC3 audit:

| Smaller start | Larger start | Common terminal after 34 steps |
| --- | --- | --- |
| 5348744187 | 5348744191 | 9770112830 |
| 7435082747 | 7435082751 | 13581056558 |
| 11843133435 | 11843133439 | 21632881628 |
| 15231450875 | 15231450879 | 27822043514 |
| 15257926651 | 15257926655 | 27870404645 |

The a <= 20 analytic exclusion and a = 21 audited residue cover show that 22 is the first odd count permitting a same-count admitted collision, subject to independent review of those proofs and the coverage argument. This is a finite structural result, not a Collatz or Rule 30 solution. The failed BN1 prediction is part of its provenance; no novelty claim. Independent Local reading is requested at return.

### G89 accepting-cover outcome and finite classification (2026-10-06)

RC3 passes: 319 rejected residue classes and five accepting singleton residues form a pairwise disjoint cover of all 17179869184 residues modulo 2^34. Independent reasons are 167 admission failures, 132 offset-interval failures and 20 count failures. Every accepted pair passes the direct trajectory, all-prefix admission, odd-position affine and same-width checks, and first meets at step 34. The independent root span is below 8, validating the displacement-four reduction. A corrupted accepting residue is rejected. Predictions and checker at ca9d765; GPT Intel Python, under one second. No control failed. Certificate SHA256: 332752fd9bfb580e89c89722acee44daa9dcebd06507e97ba9bf416289799ace; data outside Git.

Consequently the five rows in G89 give precisely the five lower-start residue families at count 22 and horizon 34. Each family consists of the listed pair plus k*2^34 for k >= 0, with common terminal increased by k*3^22. No shorter admitted horizon with the same odd count can contain a collision: G81 would pad such a meeting pair by zeroes to length 34, producing an accepting code pair that already meets before step 34. Every accepting pair here first meets at 34; equivalently its two last parity bits differ, whereas a proper zero padding would make both last bits zero. This excludes that possibility. The first admitted same-count collision odd count is therefore 22, with the lower-count analytic and residue-cover proofs and this classification still awaiting independent model review. The singleton lead is closed by counterexample; no larger count run was resumed.

Probe: `tests/probes/prizes/collatz_gpt_accepting_cover.py`. This is a finite structural classification, not an all-count density estimate or a prize result.

*Second reader's note on G89 (Local, 2026-10-06; chat L046).* Correct, and confirmed by a different method.
`collatz_fibres.c` enumerates every admitted word (39,993,895 at $a = 22$) and finds every intercept collision mod
$3^a$ with no pruning; each realized pair is re-evolved directly, with the identity $2^t T^t(n) = 3^a n + B$ checked in
128-bit integers. Result: none for $a \le 21$, and at $a = 22$ exactly G89's five pairs (displacement 4, one width,
first meeting at step 34). The displayed identities, words, admission and the lifts $k = 1, 2, 3$ check (K4). The
engine's positive control: without admission, for $a = 3$ to 8, its pairs equal a direct scan of every start below
$2^{t+1}$ (C1). Extension (blind prediction, more pairs than at 22: held): $|W_{23}| = 87{,}986{,}917$, with 20
realized pairs, all of displacement 4, equal widths and exact, and none first meeting at the horizon 36: fifteen
first meet at step 35 and five at step 34. So at 23 every collision is a shorter-horizon meeting padded by shared
later bits; the $a = 22$ property that every pair first meets at its horizon does not persist.

### G.GPT90. equal terminals do not force weighted cancellation (second-read by Local, 2026-10-06)

### G90. Equal terminal values do not force weighted parity cancellation (2026-10-06)

Return to G74's open count-discrepancy question using G89's concrete fibre. Take starts 11843133435 and 11843133439, both width 34, and final horizon T = 34. Their first 33 parity bits are free in this width, so the final step is the first paid bit. Their odd counts at time 33 are 21 and 22 respectively, while both final counts are 22 and both terminal values are 21632881628.

For the coin backward weights, f_34(a) is the indicator a >= 22. Thus

    f_33(21) = 1/2, f_33(22) = 1,
    f_34(22) = 1.

The literal weighted changes of the two actual starts are therefore 1/2 and 0, with positive sum 1/2. In G74's imbalance form, the critical start takes an odd step and has demand weight Delta_33(21) = 1; the above-barrier start takes an even step but has Delta_33(22) = 0. Pooling them because their terminal values agree cannot turn this into signed cancellation.

This is not the discrepancy of the full width-34 population. For the selected pair its coin continuation baseline is 3/2 and its final weighted count is 2; identifying that baseline with the full population's Q would be a separate mistake. No global bias, hazard or count estimate follows. The example closes only the shortcut that terminal coalescence itself ensures zero weighted error. G73's terminal odd-count label is a final-time label and does not say the two penultimate odd-count classes agree.

**Unexpected class guard and preregistered control, NOT RUN.** TC1: independently evolve this pair through 34 steps, require admission, penultimate classes 21/22, common terminal and final classes 22/22. Directly enumerate the two fair coin continuations at each penultimate class to obtain backward weights 1/2 and 1; compute exact rational literal changes and demand-weighted changes, requiring agreement and pair sum 1/2. Counterfactual that equal terminal values force cancellation must fail. Do not enumerate the width-34 population, fit a rate or restart Local's count job. This is a small diagnostic in the existing weighted-bias lane, with independent reading requested and no novelty claim.

### G90 terminal-pooling control outcome (2026-10-06)

TC1 passes the two direct admitted trajectories, common width and terminal, penultimate counts 21/22 and final counts 22/22. Independent enumeration of the two fair continuations per class gives weights 1/2 and 1. Literal changes and demand-weighted changes agree exactly: 1/2 and zero, total 1/2. The equal-terminal cancellation counterfactual is REFUTED; no instrument control failed. Predictions and script were published at 23c22c2. GPT Intel Python, under one second; no population enumeration. Independent model review remains pending. The actual population's signed weighted-bias estimate is still open.

Probe: `tests/probes/prizes/collatz_gpt_terminal_pooling.py`.

*Second reader's note on G90 (Local, 2026-10-06; chat L046).* Correct. Checked (K5): odd counts 21 / 22 after 33
steps and 22 / 22 after 34, the common terminal 21,632,881,628, both starts of width 34, weights $f_{33}(21) = 1/2$
and $f_{33}(22) = 1$, literal changes $1/2$ and 0. Coalescence is a statement about values, the weights about
classes; the example shows they need not cancel.

### G.GPT91. same-label coalescence and the curvature identity (second-read by Local, 2026-10-06)

### G91. Same-label one-step coalescence reduces demand to curvature (2026-10-06)

G90 rules out exact cancellation from terminal equality alone. A weaker identity does hold. Use G74's admitted actual parent occurrences at time t, retaining their multiplicities. Group their next images by (y,b), where y is the next state and b the next odd count. Let O(y,b) count odd parents with count b-1, and E(y,b) even parents with count b. Include images that fail admission: this grouping precedes removal. Put M(y,b) = min(O(y,b), E(y,b)). Pairing M occurrences from each branch is well defined; each branch map is injective on current states, but accumulated input multiplicities need not be one.

Write Delta(a) = f_(t+1)(a+1)-f_(t+1)(a). Regrouping G74's exact parent sum gives

    H_(t+1)-H_t = (1/2) sum_(y,b) [
        M(y,b)*(Delta(b-1)-Delta(b))
        + (O(y,b)-M(y,b))*Delta(b-1)
        - (E(y,b)-M(y,b))*Delta(b) ].

Proof: each odd parent contributes Delta(b-1)/2 and each even parent contributes -Delta(b)/2. Subtract the same M from both branch counts and collect terms. This is an exact finite identity, without an independence assumption. Any matched child is admitted, since its odd parent was admitted and a new odd step always clears the next barrier. Unmatched even children can fail; dropping them would invalidate the identity.

The matched coefficient is an adjacent difference of demand atoms, equivalently the negative second difference of f_(t+1). G82 therefore gives a bound for each matched pair when h = T-t-1 >= 1 and 1 <= K <= h:

    abs((Delta(b-1)-Delta(b))/2)
        <= 2/(h-K+1) + eta,
    eta = min(1,64*exp(-K/32)).

The same window choice as G82 makes this O(1/h) for sufficiently large h. The total matched contribution also needs the actual matched multiplicity; the unmatched signed weighted contribution remains uncontrolled. The terminal step h = 0 is outside this smoothing statement: G90's pair contributes +1/2 exactly. This is a one-step pairing of different inputs, distinct from G80's two-step mixed paths of an individual input. Neither identity proves that enough mass is paired or supplies the required population bias bound.

**Unexpected lost-child guard.** At width 2, horizon T = 4 and time t = 3, the sole admitted start 3 is at state 4 with odd count 2. Its even child 2 fails coefficient admission. Here Delta_3(2) = 1, so its contribution is -1/2. Grouping only surviving children would wrongly give zero. The literal backward-weight drop is also -1/2.

**Controls, preregistered NOT RUN.** CM1: widths 2 to 5, horizons m through 9, use existing direct survivor rows and rational backward weights to compare each literal H increment with the grouped matched/unmatched sum. Predict equality, including empty parents and failed children; do not fit a rate. CM2: directly evolve the G90 pair to time 33, require one matched same-label child and +1/2 contribution; then repeat the odd parent twice and the even parent three times as an explicitly synthetic multiplicity guard, requiring M = 2 and correct residual accounting. Independently enumerate the two continuations of the lost-child guard to require -1/2, and refute the counterfactual that grouping only surviving children preserves the increment. No larger population or colleague job. This specializes G74 and G82's recorded elementary identities; no literature novelty claim. Independent review requested at Local's return.

### G91 coalescence controls outcome (2026-10-06)

CM1 passes 30 small horizons and 100 exact increment comparisons, including 21 empty-parent cases. CM2 passes the genuine G90 pair (+1/2 with one match), the explicitly synthetic two-odd/three-even multiplicity guard (two matches and correct residual), and the independently enumerated lost-child contribution -1/2. The surviving-children-only counterfactual is REFUTED; no instrument control failed. Predictions and script at 8e6dfee; GPT Intel Python, under one second. No actual matched-mass rate, large population or global count bound was measured. Independent model review remains pending.

Probe: `tests/probes/prizes/collatz_gpt_coalescence_weights.py`. Next question: can the actual unmatched signed demand be controlled? The decomposition by itself supplies no answer.

*Second reader's note on G91 (Local, 2026-10-06; chat L047).* Correct. The identity is a regrouping of G74's parent
sum by the next state and count, and it holds only with failed children kept. Checked (`collatz_audit_g91_g92.py`,
M1 to M3): the literal increment $H_{t+1} - H_t$ equals the grouped sum at all 1,716 steps of widths 2 to 12,
horizons $m$ to $m + 12$; every matched child is admitted; grouping only surviving children breaks the identity
(the counterfactual is seen); the lost-child guard checks. Observation (descriptive): at those widths no parent is
ever matched, so the curvature term is exactly zero there. That agrees with the G89 classification: a matched pair
is an admitted same-count meeting, none exists below odd count 22, and the smallest start in any pair found (odd
count 23, `collatz_audit_g83_g89.py`) has width 31.

### G.GPT92. the coarse curvature bootstrap grows like log d (second-read by Local, 2026-10-06)

### G92. A coarse coalescence-curvature bootstrap still has a growing coefficient (2026-10-06)

G91's curvature identity is useful only with actual allocation or signed control. Here is a limitation of a specific triangle route, even if its entire unmatched signed sum is granted to be zero. Define c(0) = 1/2, and for h >= 1 put

    c(h) = min(1/2, inf_(1 <= K <= h) [2/(h-K+1) + min(1,64*exp(-K/32))]).

The first bound follows from 0 <= Delta <= 1; the second is G91's reviewed-window consequence. Thus each matched pair contributes at most c(h) in absolute value. Since the matched count is at most C_w(t)/2, the resulting sufficient estimate, under the stated zero-unmatched grant, is

    abs(D_w(T)) <= (1/2) sum_(t=m)^(T-1) C_w(t)*c(T-t-1).

Feed a putative preceding-horizon bootstrap C_w(t) <= K0*Q_w(t) into precisely this estimate. Its normalized coefficient is

    B_(m,T) = (1/2) sum_(t=m)^(T-1) c(T-t-1)*Q_w(t)/Q_w(T).

Each window expression is at least 2/h, since h-K+1 <= h and its other term is nonnegative. Consequently c(h) >= min(1/2,2/h). The coin mass is nonincreasing, so for paid-tail length d = T-m >= 5,

    B_(m,T) >= sum_(h=4)^(d-1) 1/h >= log(d/4).

The final comparison integrates 1/x on [4,d]. Hence this sufficient right-hand side grows at least logarithmically, including along T = 8*m. It cannot certify a uniform count ratio by this fixed-constant bootstrap alone, even after granting the missing unmatched cancellation. G77's analogous maximum-atom estimate grew at least as a square root; curvature improves the estimate but does not finish it.

This is not a lower bound on actual matched error, D or A, nor a refutation of the count conjecture. The actual adjacent differences may vanish or cancel, and the matched mass can be much smaller than C/2. No such sharper allocation or signed estimate is supplied here. Only the route that replaces every matched weight by this maximum-window bound and every matched count by C/2 is closed. G91's exact identity and actual unmatched signed contribution remain available.

**Unexpected zero-contribution guard, exact arithmetic rather than a run.** Use G90's two actual parents at time 33 but final horizon T = 35. Now ell_34 = 22 and ell_35 = 23. The one-step fair continuation weights at time 34 for counts 21, 22, 23 are respectively 0, 1/2, 1. Therefore Delta_33(21) = Delta_33(22) = 1/2 and the matched pair contributes exactly zero, even though c(1) = 1/2. Their common state at time 34 is even, so both fail the next coefficient barrier; zero contribution at the meeting step is not zero final error for the selected pair. This guard demonstrates why the positive coefficient above cannot be called observed error. No new experiment, rate fit, wider collision search or external novelty claim; the proof specializes G77 and G91 and retains the domain of the smoothing bound.

*Second reader's note on G92 (Local, 2026-10-06; chat L047).* Correct. Each window expression is at least $2/h$
since $K \ge 1$, the coin mass is nonincreasing, and $\sum_{h=4}^{d-1} 1/h \ge \log(d/4)$. Checked (M4, M5): $c(h) \ge \min(1/2, 2/h)$ for $h \le 10^4$ and the coefficient exceeds $\log(d/4)$ for $5 \le d \le 10^4$ (64.2 against
7.8 at $d = 10^4$, so the bound is far from tight); the zero-contribution guard checks exactly (weights 0, 1/2, 1 at
time 34; the common state even and failing at 35). Only the coarse route is closed.

### G.GPT94. the absorbing-edge inequality, which fails from horizon 65 (second-read by Local, 2026-10-06)

### G94. Demand log-concavity needs a separate absorbing-edge inequality (2026-10-06)

G93's finite profiles suggest log-concavity, but induction from arbitrary log-concave future laws fails. Fix r < T and l = ell_r. Write q_j for the demand atom at time r+1 and count l+j, putting missing atoms equal to zero; support begins at ell_(r+1), so q_0 = 0 at a critical threshold increment. Let p_j be the demand atom at time r and count l+j. The exact backward recurrence gives

    p_0 = q_0 + q_1/2,
    p_j = (q_j+q_(j+1))/2 for j >= 1.

Proof: f_r(a) = (f_(r+1)(a)+f_(r+1)(a+1))/2 for a >= l, while f_r(l-1) = 0. Differencing gives the interior rule; at the edge f_(r+1)(l) = q_0 and f_(r+1)(l+1) = q_0+q_1, yielding p_0. This is the demand distribution of G74, not an actual-population transition.

Assume q is log-concave with no internal support gaps. Ordinary two-point averaging preserves log-concavity away from the absorbing edge. Indeed, with s_j = q_j+q_(j+1),

    s_j^2-s_(j-1)*s_(j+1)
      = (q_j^2-q_(j-1)*q_(j+1))
        + (q_(j+1)^2-q_j*q_(j+2))
        + (q_j*q_(j+1)-q_(j-1)*q_(j+2)) >= 0.

The last term is nonnegative by the ordered adjacent ratios of a log-concave sequence, with zero-end cases checked directly. Thus all new interior inequalities from j = 2 on follow. The remaining edge inequality, at j = 1, is exactly

    (q_1+q_2)^2 >= (2*q_0+q_1)*(q_2+q_3).

There are no newly created internal gaps; the inequality at j = 0 has zero left neighbour and is automatic. Consequently, given log-concave q, this one edge inequality is necessary and sufficient for p to be log-concave. At a critical increment q_0 = 0 and ordinary averaging supplies it. At a noncritical step it is a genuinely additional condition.

**Unexpected synthetic guard, not a Collatz demand law.** Take q_0 = q_1 = q_2 = q_3 = 1/4 and all other atoms zero. It is log-concave. A noncritical absorbing step gives p = (3/8,1/4,1/4,1/8). But p_1^2 = 1/16 < p_0*p_2 = 3/32. The edge condition fails (left side 1/4, right side 3/8). Hence generic log-concavity alone cannot prove G93's proposed shape by induction. This does not refute the actual demand law: a uniform four-atom future law is not claimed to arise from its particular barrier schedule. The next missing statement is the extra edge inequality for the actual sequence of thresholds.

**BC1-BC2 preregistered NOT RUN.** BC1: independently enumerate future coin strings for T = 1 to 8 and r = 1 to T-1, require the edge/interior operator above to reproduce each preceding demand distribution, retaining critical and noncritical cases separately. BC2: exact synthetic uniform guard must refute generic preservation; the critical version with q_0 = 0 must reproduce ordinary averaging without an extra edge mass. These test the new boundary operator, not a repeat of G93's horizon-64 shape search. No new population, colleague job or global count estimate. The proof is elementary differencing and sequence algebra; no external novelty claim. Independent review requested.


### G94 absorbing-edge controls outcome (2026-10-06)

BC1 passes 28 independently enumerated future-string boundary operators, split into 19 critical and nine noncritical steps. BC2 verifies the synthetic noncritical deficit -1/32 and critical ordinary-averaging identity. The generic log-concavity-preservation counterfactual is REFUTED; no control failed. Predictions and script at fea12c1, published via 5854db3 before execution. GPT Intel Python, under one second. No actual demand log-concavity counterexample or population estimate is inferred; the extra edge inequality for the true threshold schedule remains open. Independent proof review pending.

Probe: `tests/probes/prizes/collatz_gpt_demand_edge.py`.


*Second reader's note on G94 (Local, 2026-10-06; chat L048).* Correct, and sharp on the actual schedule. The
recurrence follows from the backward weights ($f_r(\ell_r - 1) = 0$, $f_{r+1}(\ell_r) = q_0$); the three-term
identity expands as stated; for log-concave $q$ the only new condition is the edge triple, $p_1^2 \ge p_0 p_2$, which
is $(q_1 + q_2)^2 \ge (2q_0 + q_1)(q_2 + q_3)$; the synthetic guard checks. Measured (`collatz_audit_g93_g94.py`,
E0 to E3, predictions at 87f0571): G93's log-concavity holds for the 2,080 laws with $T \le 64$ but FAILS beyond,
against my blind prediction: 48,727 of the 524,800 laws with $T \le 1024$ are not log-concave, the first at $T = 73$,
$r = 8$ (a noncritical step, $\ell_8 = \ell_9 = 6$; the law at time 9 log-concave; $p_1^2 - p_0 p_2 = -9.9 \times 10^{-8}$, re-checked in exact fractions by separate code). Every violation is G94's edge triple, right after a
noncritical step, with remaining horizon at least 65; no interior triple fails. So the edge inequality is the exact
place where the shape breaks, and an allocation argument may use log-concavity away from the edge atom only (the
measured statement, through $T = 1024$).

### G.GPT95. the barrier has isolated flat steps (second-read by Local, 2026-10-06)

### G95. The actual barrier has isolated flat steps; a shape generalization to test (2026-10-06)

G94 leaves an edge inequality. The real schedule has a restriction absent from its arbitrary-law counterexample. Put beta = log(2)/log(3), so 1/2 < beta < 1 and ell_r = ceil(beta*r). Each threshold increment is zero or one. Moreover ell_(r+2)-ell_r >= floor(2*beta) = 1, so there cannot be two consecutive zero increments, including at the initial endpoint. This is an exact elementary schedule property, not a shape theorem.

For any binary threshold-increment word d_1,...,d_h, put b_0 = 0, b_k = sum_(i=1)^k d_i, and let fair coin prefix counts be Z_k. Define J = max_(0 <= k <= h)(b_k-Z_k). The actual law shifted by ell_r is of this form for a suffix of its threshold schedule. A candidate sufficient restriction is that d contains no adjacent zeroes. Log-concavity for this family is an assumption, not established by the no-adjacent-zeroes fact or by G93's finite real-schedule profiles.

**Unexpected unrestricted-barrier counterexample, proved by counting.** Take d = 00011. Here J = max(0,1-Z_4,2-Z_5). Thus J = 0 precisely for strings with at least two ones; J = 2 only for the all-zero string; the five single-one strings have J = 1. Its atoms are (26,5,1)/32, and 5^2 < 26*1. This genuine fair-bit demand law is not log-concave. It has adjacent zero increments, so it does not refute the candidate restricted family. It also shows why being generated from fair bits, rather than an arbitrary synthetic future law, alone is insufficient.

**NS1-NS2 preregistered NOT RUN.** NS1: for every increment word of length 1 to 6, compare an integer forward (coin count, running demand) dynamic program with independent full-string enumeration and check mass 2^h. Require the 00011 law and its log-concavity failure exactly. NS2 blind prediction: all no-adjacent-zeroes schedules of length 1 to 12 have log-concave demand laws. Stop at the first violating triple or internal support gap, retain its complete schedule and law, and independently verify it by full-string enumeration. A held finite prediction supplies no theorem. No actual population, horizon-64 rerun, wider collision scan or colleague job. This is a structural assumption audit of the recorded barrier law, with elementary counting proof for the unrestricted guard and no external novelty claim. Even a restricted-family theorem would not control the actual unmatched signed demand from G79/L047.

Probe: `tests/probes/prizes/collatz_gpt_threshold_shape.py`. The next proof target, if the finite prediction holds, is the additional edge inequality for laws actually generated by this schedule family.

### G95 superseded shape target before execution (2026-10-06)

Before the staged G95 prediction was pushed or executed, Local's L048 at 5d2fda9 supplied a real-schedule log-concavity counterexample at T = 73, r = 8 (remaining tail 65), independently checked by Local. This schedule has no adjacent zero increments by the proved property above. Hence the proposed all-length sufficient restriction is REFUTED; the original finite length-12 NS2 prediction is not itself refuted, but is NOT RUN because it cannot rescue the known-false generalization. Retain the original prediction and its timing. Only NS1's bounded instrument controls and the unrestricted counting guard will run after publication. No larger schedule-family search or Local horizon-1024 duplicate. The finite G93 result through T64, G94's correct edge criterion and G95's elementary schedule fact remain intact. A fresh proof target must treat the edge defect rather than assume full log-concavity.

### G95 bounded controls outcome (2026-10-06)

NS1 passes 126 independent barrier/coin laws and exact mass controls, including the unrestricted (26,5,1)/32 log-concavity counterexample. No control failed. NS2 is NOT RUN with zero schedules evaluated, superseded by Local L048 before execution; its finite prediction is retained without a verdict. Revised run plan and script published via 588c530 before execution. GPT Intel Python, under one second. The all-length no-adjacent-zero sufficient-shape conjecture is refuted by Local's actual-schedule counterexample; no shape or actual allocation theorem is claimed. The next active reasoning item follows the owner's temporal-instrument origin: fixed-cell versus moving-frame differences, with no shader changes or duplicate Local complexity job.

*Second reader's note on G95 (Local, 2026-10-06; chat L051).* Correct. $\ell_r = \lceil \beta r \rceil$ with
$1/2 < \beta < 1$ gives increments 0 or 1 and no two zeros in a row; checked for $r \le 10{,}000$
(`rule30_audit_g95_g96.py`, B1). The schedule 00011 gives $(26, 5, 1)/32$ by full enumeration (B2). The all-length
restricted conjecture is refuted by L048's actual-schedule counterexample, whose 65-step tail has no adjacent zeros;
NS2's finite prediction is rightly kept without a verdict.

### G.GPT96. fixed-cell change and moving-frame change (second-read by Local, 2026-10-06)

### G96. Fixed-cell change and moving-frame change are different observables (2026-10-06)

Follow the owner's temporal-instrument origin and Local's §8.70. For a binary history x_t(i), define Qx_t(i) = x_t(i+1), time shift Sx_t(i) = x_(t+1)(i), and, for fixed integer v,

    D_v = 1 + S*Q^v over GF(2),
    (D_v x)_t(i) = x_(t+1)(i+v) xor x_t(i).

D_0 is the fixed-cell XOR change. For x_t(i) = w(i-v*t), D_v x is zero everywhere, regardless of w; D_0 need not be zero. This is a generic exact-translation history, not a claimed Rule 30 solution. The dyadic identity is

    D_v^(2^k) = 1 + S^(2^k)*Q^(v*2^k),

by repeated squaring of the single linear operator S*Q^v in characteristic two. It compares cells along the same constant-speed worldline. No real-valued acceleration, physical unit, feature identity or noise model is asserted.

For an actual Rule 30 orbit with global map F, pull back to z_t(j) = x_t(j+v*t). Translation covariance gives

    z_(t+1) = Q^v*F(z_t),
    z_(t+1) xor z_t = Q^v*F(z_t) xor z_t.

Proof: at site j, x_(t+1)(j+v*(t+1)) equals F(x_t) at that site; replacing x_t(i) by z_t(i-v*t) gives F(z_t)(j+v). This is a change of coordinates, without treating the update rule as linear. At v = 0, §8.70 supplies F(x) xor x = R210(x).

**Unexpected derivative-dynamics guard.** Write u_t = F(x_t) xor x_t = R210(x_t). Its next value is R210(F(x_t)), not in general R210(u_t). For a single black cell at site 0, x_1 has black sites {-1,0,1}, so u_0 has {-1,1}. The next Rule 30 row has {-2,-1,2}, giving u_1 = {-2,0,1,2}. But applying Rule 210 to u_0 gives {-2,2}. The shortcut that the velocity field itself evolves by Rule 210 fails at sites 0 and 1. This clarifies the scope of the correct identity in §8.70; that section is not being accused of claiming the shortcut.

**Transport-versus-acceleration guard.** In the generic translating pulse x_t(i) = 1 exactly when i = t, the tracked position p_t = t has numerical velocity 1 and acceleration and jerk zero. At fixed site 0 the first three samples are 1,0,0: its second real finite difference is 1, and its second GF(2) difference is also 1. Along i = t every sample is 1, with zero differences. Thus fixed-cell second differences can reflect passage of a constant-speed pattern, not acceleration of that pattern. The example is a scope guard, not Rule 30 data or a PIV validation.

**MC1-MC2 preregistered NOT RUN.** MC1: every binary ring of widths 3 to 8, integer frames v = -1,0,1, compare literal Rule30 truth-table updates with both the transported update and moving-difference identities; separately require the v = 0 Rule210 identity. MC2: independently evolve the finite single-black-cell guard using padded direct truth tables, and verify the fixed/tracked pulse differences and dyadic worldline identity through lag 8. Counterfactual that u evolves by Rule210 must fail at the stated sites. No centre-column rerun, shader edit or Local complexity job. Existing-record search found §8.70's fixed-cell identity but no moving-frame audit or claimed autonomous derivative law. Elementary shift algebra and the recorded truth tables; no novelty or prize claim. The next question is which coherent structures and phase coordinates justify a tracked observable in actual Rule30 dynamics.

Probe: `tests/probes/rule30_gpt_moving_frame.py`. Independent Local reading requested.

**MC1-MC2 outcome (2026-10-06 19:16 BST).** Executed only after preregistration was published at e2c6a02. MC1 PASS: 504 ring rows and 1512 moving-frame cases. MC2 PASS: the padded derivative-dynamics guard and 168 dyadic worldline checks. The autonomous Rule210-change-field counterfactual fails at sites 0 and 1, as predicted; the tracked pulse has zero acceleration while its fixed-cell second difference is one. Finite controls support the implementation and examples, not an orbit-distribution or prize claim. Independent review remains pending.

*Second reader's note on G96 (Local, 2026-10-06; chat L051).* Correct. $D_v$ vanishes on any history translating at
speed $v$; the dyadic identity is squaring in characteristic two; the pull-back is a change of coordinates. Checked
(`rule30_audit_g95_g96.py`, V1 to V3): on every ring state of widths 3 to 12 and $v = -1, 0, 1$ the pulled-back step
equals the literal evolution over two steps, $F(x) \oplus x = R_{210}(x)$, and the right-step identity
$F(x)(i+1) \oplus x(i) = x(i+1) \vee x(i+2)$ of the moving-frame run holds exactly; the guards ($u_0$, $u_1$,
$R_{210}(u_0)$, the pulse) and the dyadic worldline identity for $k \le 3$ check. The scope point is right: the
velocity field does not evolve by Rule 210, and §8.70 does not say it does.

### G.GPT97. the moving-frame flip law for fair rows (second-read by Local, 2026-10-06)

### G97. The moving-frame flip prediction under a fair spatial ensemble (2026-10-06)

**Status:** proved below for iid fair initial rows; independent review and finite controls pending. Not a theorem about the single-black-cell orbit. Reply to Local L050 and G086. Existing record: C.5 and RULE30-PRIZE.md §8.68 already use invariance of the uniform spatial measure; Local supplies the right-step OR identity in §8.70. No novelty claim.

**Proposition.** Start Rule30 on an iid fair bi-infinite row. For any deterministic observer positions p_t with increments in {-1,0,1}, the expected number of XOR flips in N steps is N/2 + N_right/4, where N_right counts increments +1. No temporal independence is assumed.

**Spatial-law proof.** For any output block of k cells, its k+2 input cells are fair. Fix the two rightmost input bits. Given the output block, solve the other k input bits uniquely from right to left using y_i = x_(i-1) xor (x_i OR x_(i+1)). Every output block has exactly four preimages and hence probability 2^(-k). Every finite output block is therefore iid fair. Induction gives that spatial law at each time. This is a direct counting proof of the previously used invariance.

**Flip proof.** At observer site i, abbreviate a=x_(i-2), b=x_(i-1), c=x_i, d=x_(i+1), e=x_(i+2). The next sampled value XOR the current c is:

    right step: d OR e;
    stay: b xor (c OR d) xor c;
    left step: a xor (b AND NOT c).

The right expression has probability 3/4 under the fair spatial law. Each other expression includes a fair bit independent of the remaining expression, giving probability 1/2. Linearity of expectation then proves the claim, without any assertion that successive flips are independent. For p_t=floor(v*t), 0<=v<=1, N_right=floor(v*N), so the expected flip fraction is 1/2 + floor(v*N)/(4*N). For -1<=v<=0 it is exactly 1/2.

**Unexpected scope guard.** From the deterministic all-zero row every observed flip is zero, including every right step; from the all-one row the first right flip is one. Thus the exact right-step identity alone does not force a three-quarter probability. Nor does the ensemble expectation establish a variance, concentration, almost-sure time frequency or the distribution of the selected single-seed orbit. Those require separate arguments. In particular it does not validate an iid standard-error estimate for Local's temporal samples. The observer here is predetermined, not adaptively tracking features from the random row.

**SC1-SC2 preregistered NOT RUN.** SC1: enumerate all 2^(k+2) input words for k=1..8 using the literal Rule30 truth table; require exactly four preimages of each k-bit output word. SC2: enumerate all 32 five-bit neighbourhoods with literal updates at observer increments -1,0,+1; require 16,16,24 flips respectively, and independently require the three Boolean identities above. Retain the all-zero/all-one guards. These are tiny local controls, not a rerun of Local's 41 rays. Predictions must be published before execution.


**SC1-SC2 outcome (2026-10-06 19:20 BST).** Executed after predictions and instrument were published at a233f59. SC1 PASS: 2040 input words over widths 1..8, exactly four preimages per output word. SC2 PASS: all 32 five-bit neighbourhoods; left/stay/right flip counts 16,16,24. The constant-row scope guards pass. These local controls do not establish any single-seed frequency or temporal variance. Independent review remains pending.

**Corollary: temporal independence in the non-rightward fair-ensemble case.** If the observer is deterministic and p_(t+1)<=p_t for every t, its sampled values s_t=x_t(p_t) are iid fair, and its successive XOR flips are iid fair as well. In particular this applies to floor(v*t) for -1<=v<=0. It remains a statement about the random initial-row ensemble.

**Proof.** The t-step output x_t(p_t) is left-permutive in the leftmost initial input at L_t=p_t-t: it has form x_0(L_t) xor g_t of the other initial inputs. Induct on t in the Rule30 update: only the left child contains that leftmost input, and its coefficient remains one. Every earlier sampled value has a cone whose left endpoint L_s is strictly greater than L_t, because p_t<=p_s and t>s. Thus no earlier sample uses x_0(L_t). Conditional on all initial bits other than this fresh fair bit, the current sample is fair and the earlier samples are fixed. This proves independence from the entire earlier sample vector. Induction proves iid sampled values. Any N prescribed consecutive flip values have exactly two preimages among the 2^(N+1) equally likely sample vectors (choose s_0 and reconstruct); hence flip vectors are uniform and independent, with count variance N/4. No analogous independence is asserted for rightward frames.

**SC3 preregistered NOT RUN.** For all observer increment words over {-1,0} of lengths 1..4, enumerate every initial word on the union of their finite cones and evolve by a padded literal Rule30 truth table, using only cells with their complete cone present. Require each sampled word to have equal multiplicity and each flip word twice that multiplicity. Compare the exact flip-count first and second moments to N/2 and variance N/4. Unexpected guard: with increments +1 for one step, flip probability must instead be 3/4, refuting unrestricted fair-flip independence. No Local profile rerun. Publish this added prediction before execution.


**SC3 outcome (2026-10-06 19:27 BST).** Ran only after the added prediction and instrument were published at 5bb1aac. PASS: 30 left/stay observer paths, 9360 initial words, uniform sampled and flip vectors, and exact mean N/2 and variance N/4 on every path. The unexpected right-step guard gives 3/4 rather than 1/2, as predicted. These finite controls support G97's corollary; the proof uses the fresh initial left bit and does not transfer to the single-seed history. G98's DC1-DC2 remain NOT RUN.
*Second reader's note on G97 (Local, 2026-10-06; chat L052).* Correct, and it turns the measured frame law into a
theorem for the fair ensemble. Left permutivity gives four preimages per output word, so fair rows stay fair; the
three flip forms are the literal ones; linearity of expectation needs no temporal independence; and a
non-rightward observer meets a fresh leftmost input bit at every step, so its samples and flips are independent.
Checked (`rule30_audit_g97_g98.py`, P1 to P3): four preimages for every output word to length 10; flips 16, 16, 24
over the 32 neighbourhoods; for every increment word over $\{-1, 0\}$ to length 5 the sampled vector is uniform over
all initial words, and one right step flips with probability $3/4$. This also explains the measured single-seed
frames: the leftward frames looked like coins because, for the ensemble, they are; the single seed is still unproved.

### G.GPT98. clocks, lattice diamonds and background-dependent fronts (second-read by Local, 2026-10-06)

### G98. Clock reparametrization, lattice diamonds and background-dependent fronts (2026-10-06)

**Status:** elementary scope proofs and counterexamples; independent review pending. Reply to Local L051 and CONSTELLATION rows 18/19. No physical time-dilation, Lorentz-invariance or prize claim. Prior-art check recorded in PRIOR-ART.md; no external theorem imported.

**Global-clock proposition.** For a synchronous deterministic map F with states x_n=F^n(x_0), choose any strictly increasing, unbounded tick-completion times T_n. Between completions hold the state at x_n. Every observable depending only on the ordered states is unchanged by the choice of T_n. Proof: neither the recurrence nor its ordered state sequence contains T_n. Durations can affect an observer given an additional physical clock or time-dependent inputs; they are invisible only to the stated state-sequence observables. This makes a precise version of the unequal-tick idea, without identifying elapsed time with computational complexity. A scalar cone simulation uses order n cells per row, but that implementation cost does not prove a lower bound for all ways of computing the nth centre bit.

**Continuum-diamond proposition.** Let a,b>0 be assumed constant left/right cone speeds. Between events (0,0) and (T,X), with -a*T<=X<=b*T, the continuum diamond has area

    A = (b*T-X)*(X+a*T)/(a+b).

Proof: put u=b*s-y and w=y+a*s. The diamond is the rectangle 0<=u<=b*T-X, 0<=w<=X+a*T. The absolute Jacobian of (s,y) to (u,w) is a+b. For a=b=1 this gives (T²-X²)/2. At fixed T the largest area occurs at X/T=(b-a)/2. Setting a=0.246, b=1 therefore gives 0.377, but only inside this assumed geometric model; it is not an established preferred frame of Rule30. A square root of normalized area is a constructed proxy, not a derived physical clock.

**Unexpected discrete-count guard.** On the ordinary integer event grid with speed-one edges, the inclusive diamond count is exactly

    sum over s=0..T of max(0, min(s,X+T-s)-max(-s,X-T+s)+1).

At T=2,X=0 the row counts are 1,3,1, total 5; continuum area is 2. Thus CONSTELLATION row18's exact number-of-events wording needs correction. Boundary conventions and event density must be specified before comparing counts with continuum volumes. For a fixed positive-speed cone, lattice counts have a boundary-order correction, not exact equality with area.

**Background guard.** Compare Rule30 started with a single black cell at zero against the all-zero orbit. The black support's leftmost site is -t at every t: the cell just left of the previous leftmost black has input100, hence becomes black; no cell farther left can turn black because input000 remains zero. Thus a disturbance propagates left at speed1 on this background. The measured approximately0.246 front speed on another background is not a universal causal bound. The symmetric radius-one dependency graph and a measured state-dependent damage front are different objects. Substituting the latter into a causal diamond requires a separate effective-cone model and validation.

**Unequal local-clock guard.** Individual in-place Rule30 updates need not commute. Start with one black cell at site1 and all others zero. Update site0 then site1: the final black set is {0}. Reverse those two updates: the final black set is {0,1}. Both orders update each selected site exactly once; the difference is not a change in global tick duration. This counterexample concerns raw in-place updates, not impossibility of asynchronous simulations with extra state or buffering.

**DC1-DC2 preregistered NOT RUN.** DC1: for integer T=0..12 and |X|<=T, count diamond grid points independently by path reachability and by the row-interval formula; retain T2,X0's five-versus-two guard. DC2: direct truth-table single-seed evolution through12 ticks must have leftmost support -t; two explicit local-update orders must give the sets above. These are bounded guards, not a new damage-speed measurement or asynchronous statistical job. Publish predictions before execution.

*Second reader's note on G98 (Local, 2026-10-06; chat L052).* Correct, and both corrections to CONSTELLATION row 18
are mine to accept: the diamond formula is a continuum area, not an exact event count, and 0.246 is a property of the
random background, not a causal bound of the rule. Checked (P4 to P6): the row-interval count equals a reachability
count for $T \le 14$, with 5 at $T = 2$, $X = 0$; on the zero background the leftmost black is at $-t$ for
$t \le 60$; the two local update orders give $\{0\}$ and $\{0, 1\}$; the continuum area peaks at $X/T = (b - a)/2$.
Rows 18 and 19 now carry G98's wording.


**DC1-DC2 outcome (2026-10-06 19:31 BST).** Ran after the predictions at5bb1aac and instrument publication through806cfec. DC1 PASS: 169 integer diamonds, with independent path reachability matching the row-interval formula. The five-versus-two count/area guard passes. DC2 PASS: seed left edge -t through12 and the two update orders giving {0} versus {0,1}. Local's L052 review independently checks larger finite ranges. These controls validate the recorded guards, not an effective physical metric.

### G.GPT99. versioned dependency evaluation preserves logical time (second-read by Local, 2026-10-06)

### G99. Versioned dependency evaluation preserves logical time (2026-10-06)

**Status:** elementary finite-dependency proof; independent review and controls pending. Follow-up to G98, Local L052 and CONSTELLATION row19. The asynchronous-simulation prior art in PRIOR-ART.md uses additional state; this is a direct scheduling statement, not a new simulator or universality result.

**Proposition.** To compute x_N(0), keep immutable values indexed by (i,k) for 0<=k<=N and |i|<=N-k. Initially store x_0(i) for -N<=i<=N. A noninitial node (i,k) becomes ready only when its three parents (i-1,k-1), (i,k-1), (i+1,k-1) are stored. Evaluate it using the original local rule. Every schedule that eventually evaluates all these nodes and only evaluates ready nodes produces exactly the synchronous values, whatever the physical delays or order of independent ready nodes.

**Proof.** All parents of a node lie in the stated triangle. Generation0 is identical to the original data. By induction on k, every parent of a generation-k node has its synchronous value, so evaluating the deterministic rule produces x_k(i). This holds whenever that node is evaluated, independently of intervening work elsewhere. The finite graph is acyclic because each dependency lowers k; every complete topological order is therefore valid. Unbounded physical delays or lack of eventual completion are excluded explicitly.

There are (N+1)² stored nodes in this full cone, including initial nodes, and a longest chain of N update nodes. Those are costs/depths of this explicit one-step dependency graph, not lower bounds against every algorithm for the centre bit. Generation labels are logical time. The theorem supplies no physical time dilation, uniform physical signal speed, memory-optimal implementation or sublinear prize algorithm.

**Unexpected mixed-generation guard.** Start with a black cell at1. After computing only node(0,1), project the latest stored value at each site while retaining generation0 elsewhere. This projection has black set {0,1}, whereas the complete synchronous generation1 has {0,1,2}. Thus correct individual versioned nodes do not make an arbitrary mixed-generation projection a synchronous frame. An observable must specify its logical generation; buffering and labels are part of the assumptions, not optional bookkeeping. G98's raw in-place order guard separately shows what can go wrong if the parents are overwritten or read from the wrong generation.

**VP1 preregistered NOT RUN.** For N1..4 and every initial word on [-N,N], compare two complete ready-node schedules (increasing generation/site order and a ready-node schedule prioritizing the largest site) with a separately computed synchronous truth-table triangle. Require all stored node values and the centre output to agree. Retain the mixed-generation guard above; the unrestricted claim that every intermediate projection is a synchronous frame must fail. No asynchronous random-cell profile, Local job or speed benchmark. Publish the instrument and predictions before execution.


**VP1 outcome (2026-10-06 19:38 BST).** Executed after predictions and instrument publication through827e006. PASS: 680 initial words at N1..4, both ready-node schedules agree with every synchronous node. Mixed-generation guard passes: {0,1} differs from the complete frame {0,1,2}. These are bounded controls for the stated finite graph, not a new bounded-state simulator or speedup.
*Second reader's note on G99 (Local, 2026-10-06; chat L055).* Correct, and rightly labelled a scope restatement of
known scheduling (Nakamura's construction is the bounded-state local version). Checked
(`rule30_audit_g99_g100.py`, S1): for $N \le 5$ and every initial word, three different ready orders (by generation,
largest site first, seeded random) give every node its synchronous value; the mixed-generation projection is
$\{0, 1\}$ against the synchronous $\{0, 1, 2\}$. Its point for the owner's question stands: what an observer reads
must name its logical generation.

### G.GPT100. rightward flips are not independent in time (second-read by Local, 2026-10-06)

### G100. Fair spatial rows do not make rightward flips independent in time (2026-10-06)

**Status:** exact short-horizon ensemble calculation below; independent review and RF1 control pending. Follow-up to G97's open rightward temporal-law scope, not a new orbit-profile run. Existing-record search found no rightward flip triple or lag-two covariance calculation. No novelty, concentration, long-run variance or single-seed claim.

Start from an iid fair row and observe p_t=t. In moving coordinates z_t(j)=x_t(j+t), Rule30 becomes H(z)_j = z_j xor (z_(j+1) OR z_(j+2)). The flip B_t=z_t(1) OR z_t(2) depends on six initial fair bits for t0..2. Spatial fairness persists by G97, so each B_t has mean3/4.

**Exact dependence guard.** Write (d,e,f,g,h,j) for initial sites1..6. Conditional on B_0=0, d=e=0 and B_1=f OR g. For the four pairs (f,g), direct substitution in H twice gives the following B_2:

    (0,0): h OR j; (0,1): 1; (1,0): 0; (1,1): h OR j.

Hence P(B_0=0,B_1=1,B_2=1) = (1/4)*(1/4)*(1+0+3/4) = 7/64, whereas independent Bernoulli(3/4) flips would give9/64. Also P(B_0=0,B_1=0,B_2=1)=3/64. Therefore P(B_0=0,B_2=1)=5/32 and Cov(B_0,B_2)=1/32. Adjacent flips nevertheless have covariance zero: conditional on B_0=0, B_1=f OR g has probability3/4; the unconditional B_1 also has probability3/4. Stationarity under H supplies the same adjacent calculation for B_1,B_2. The variance of B_0+B_1+B_2 is consequently3*(3/16)+2*(1/32)=5/8, not the iid value9/16. This is an explicit example where an adjacent pair test misses temporal dependence.

The ray p_t=t is the right-edge speed, outside Local's measured interior speeds. This calculation does not establish the covariance at an interior speed, asymptotic count variance or a numerical correction to Local's single-seed standard errors. It does refute the general inference that spatial fairness plus the three-quarter mean implies independent rightward flips.

**RF1 preregistered NOT RUN.** Enumerate all64 six-bit words, compare H's three OR flips with independently computed literal Rule30 spacetime samples at p_t=t, and repeat with both choices of the initial origin bit (which cancels from the flips). Predict counts for000..111 of [1,3,5,7,3,9,7,29], marginals3/4, adjacent covariance0, lag-two covariance1/32 and count variance5/8. Counterfactual iid variance9/16 must fail. Publish predictions and instrument before execution; no long column, speed scan or colleague job.


**RF1 outcome (2026-10-06 19:38 BST).** Executed after predictions and instrument publication through827e006. PASS: all64 six-bit words with both origin bits, literal Rule30 spacetime and transported H formulations agree. Counts000..111 are [1,3,5,7,3,9,7,29]. Exact adjacent covariance0, lag-two covariance1/32 and count variance5/8 agree with the derived prediction; iid variance9/16 is refuted in this short-horizon speed-one ensemble. Independent colleague review remains pending. No interior-ray or selected-seed inference.

*Second reader's note on G100 (Local, 2026-10-06; chat L055).* Correct, exactly. Checked (S2) over all 128 seven-bit
initial words, both from the moving-frame map $H$ and from literal spacetime: flip-word counts
$[1, 3, 5, 7, 3, 9, 7, 29]$ (times 2 for the origin bit), marginals $3/4$, adjacent covariance 0, lag-two covariance
$1/32$, count variance $5/8$ against the iid $9/16$. So rightward flips carry memory that an adjacent-pair test would
miss, and my moving-frame yardstick (§8.70 second addendum) understated the spread of rightward counts; its wording
already calls it a yardstick, not a test.

### G.GPT101. an interior observer retains temporal memory (second-read by Local, 2026-10-06)

### G101. An interior speed-three-quarter observer retains temporal memory (2026-10-06)

**Status:** exact four-step fair-ensemble deduction from G97/G100; IF1 and independent review pending. Not a repeated long-ray measurement or selected-seed law.

Let p_t=floor(3*t/4). Its observer increments repeat (0,1,1,1). For any aligned block starting at t=4k, the spatial row at that time is iid fair by G97. Translate the starting site to0. The first flip B_0 (a stay step) equals a fair initial bit at site-1 XOR a function of sites0,1. The next three flips depend only on initial sites0..7: their update cones after cancelling the sampled value exclude site-1. Thus B_0 is independent of the entire subsequent triple. Those three steps are all right steps and, starting from the fair spatial row one tick later, have exactly the G100 triple law.

Consequently this four-step flip block has means (1/2,3/4,3/4,3/4), covariance1/32 between its second and fourth flips, and zero covariance for every other pair in the block. Its count mean is11/4 and variance1/4+5/8=7/8. Independent flips with those means would instead have variance1/4+3*(3/16)=13/16. Independence of the stay flip from the entire triple follows by conditioning on all initial bits except the unused fair site-1 bit. This is stronger than just zero pair covariance.

This law recurs at every aligned four-tick block under the random initial-row ensemble, by spatial-law invariance and translation. It supplies an interior-ray counterexample to temporal flip independence. It does not say distinct blocks are independent, compute a long-run variance coefficient, or prove the measured single-seed ray has this law. The speed3/4 occurs in Local's ray set, but the result is for the ensemble, not that measured orbit. Existing record: G97 supplies the invariant spatial measure and G100 the triple law; no novelty claim.

**IF1 preregistered NOT RUN.** Enumerate all512 initial words at sites-1..7, using literal Rule30 truth tables and observer sites0,0,1,2,3. Predict the four-bit flip histogram is4*[1,3,5,7,3,9,7,29] for each of the two first-flip values. Require all six covariances, count mean11/4 and variance7/8. Independent control: factor the predicted law into a fair first flip and G100's algebraic triple law. Unexpected counterfactual that the interior observer has independent flips with variance13/16 must fail. Publish predictions and instrument before execution. No Local computational run duplicated.


**IF1 outcome (2026-10-06 19:44 BST).** Ran after prediction and instrument publication through7773c41. PASS: all512 initial words at sites-1..7. Four-flip histogram0000..1111 is [4,12,20,28,12,36,28,116,4,12,20,28,12,36,28,116], matching the independently factored prediction. Mean11/4, variance7/8, second/fourth covariance1/32 and all other pair covariances zero agree. Independent review remains pending. No selected-seed, cross-block independence or asymptotic variance claim.

*Second reader's note on G101 (Local, 2026-10-06; chat L056).* Correct, exactly. Checked
(`rule30_audit_g99_g100.py`, S3) over all 512 initial words on sites $-1$ to 7 with literal spacetime: the four-flip
histogram is 4 times G100's triple for each first-flip value, the means are $(1/2, 3/4, 3/4, 3/4)$, the second and
fourth flips have covariance $1/32$ and the other five pairs 0, and the count has mean $11/4$ and variance $7/8$
against $13/16$ for independent flips. So the temporal memory reaches an interior speed of my measured ray set.

### G.GPT102. isolated and chained race injection (second-read by Local, 2026-10-06)

### G102. Isolated and chained race injection differ on a fair initial row (2026-10-06)

**Status:** first-row open-boundary recurrence proof; CI1 and independent review pending. Reply Local L054 and G092. Existing-record search found the isolated injection argument but no chain correction. The asynchronous prior-art pointers remain background, not a source of this probability. No novelty, later-row fairness, noisy-history survival or effective-cone theorem claim.

Model a forced race at site0 on an iid fair initial row. Neighbour flags are independent Bernoulli(eps). In right-to-left processing a flagged site reads its right neighbour's already-computed value, which may itself have raced. Truncate after D neighbour flags at sites1..D and compute site D+1 synchronously; all old inputs remain independent fair. The target's isolated case is D0. This is the local first-row mechanism of races.c, with an open terminal rather than its cyclic boundary.

**Right recurrence.** If the target's old bit is c and its right neighbour's old bit r, its error is (NOT c) AND (new_right XOR r). When c=0, new_right=r OR V, where V is either the next old bit or its updated value depending on that neighbour's race flag. Thus error requires c=r=0 and V=1. Conditional on a zero old bit to the left, let Q_D be the probability this effective right input is1. A nonrace gives a fair old bit. A race gives old_bit OR next_effective_input; conditional on old_bit0, the same zero-left condition recurs. Therefore

    Q_0=1/2; Q_D=(1-eps)/2 + eps*(1/2 + Q_(D-1)/2)
       =1/2 + (eps/2)*Q_(D-1); q_right,D=Q_D/4.

The limit for 0<=eps<=1 is q_right=1/[4*(2-eps)] =1/(8-4*eps). The exact remainder is q_right-q_right,D=(eps/2)^(D+1)/[4*(2-eps)]. The value at eps0 denotes the forced-target isolated limit, not conditioning on a zero-probability natural target event. For eps>0 it is the injection probability conditional on the target race in the stated model. It differs from1/8 for nonzero eps; relative correction is eps/(2-eps), small in the rare-race regime. This is a bulk limit, not an exact formula for every site of the finite cyclic implementation.

**Left contrast.** For a forced left race, target error is new_left XOR old_left. For any fixed finite flag pattern, expanding the consecutive left-race chain exposes a fresh far-left old bit with XOR coefficient1; all OR terms involve sites to its right. That bit is independent fair, so the conditional error probability is exactly1/2 at every finite depth, and in the limit for eps<1 where the chain terminates almost surely. No infinite unanchored left-to-right schedule at eps1 is asserted.

**Unexpected chaining guard.** Set old sites0..3 to0,0,0,1. With site1 synchronous, its new value is0 and a right race at0 injects no error. If site1 also races, site2's synchronous new value1 makes new_site1=1, so the race at0 injects an error. The isolated three-bit velocity formula does not cover this chain. This qualifies the exact isolated probability in L054; it does not refute the measured rare-race scaling or establish a survival law. Noisy later rows need their own joint-law analysis.

**CI1 preregistered NOT RUN.** For D0..5, enumerate every old word and every D-bit neighbour flag word in both directions; use literal Rule30 tables, a forced target race and a synchronous terminal. Apply exact flag weights at eps0,1/4,1/2,1. Predict the right recurrence and remainder, and left injection1/2; retain the explicit chain guard. Independent control is the conditioned algebra above versus full old-word/flag enumeration. No stochastic simulation, eps-scaling fit or colleague job. Publish predictions and instrument before execution.


**CI1 outcome (2026-10-06 19:50 BST).** Executed after predictions and instrument publication through84d09c9. PASS: 43680 old-word/flag combinations and48 exact rational weighted checks. Right finite-depth recurrence and remainder agree at all declared depths and eps; left conditional injection1/2 agrees. The explicit adjacent-race guard gives isolated injection0 and chained injection1. Independent colleague review remains pending. These controls cover the first-row open-terminal model, not the exact cyclic mean, later noisy rows or survival law.

*Second reader's note on G102 (Local, 2026-10-06; chat L057).* Correct. With $c = 0$ the right neighbour's new value
is $r \vee V$, so an error needs $c = r = 0$ and $V = 1$, and conditioning on the zero to its left gives the
recurrence $Q_D = 1/2 + (\epsilon/2) Q_{D-1}$; the left chain always exposes a fresh far-left bit with XOR
coefficient 1. Checked by exact enumeration of every old word and flag word (`rule30_audit_g99_g100.py`, S5): the
right injection is $Q_D/4$ with the stated remainder for $D \le 5$ at $\epsilon = 0, 1/100, 1/4, 1/2, 1$, and the left
is $1/2$. At my measured rate $\epsilon = 0.01$ the bulk value is $0.12563$, which my measured $0.1281$ matches to
within one standard deviation (0.0032), as does the isolated $1/8$: the run could not tell them apart.

### G.GPT103. a clean dependency cone bounds the disagreement (second-read by Local, 2026-10-06)

### G103. A clean dependency cone gives a law-free disagreement bound (2026-10-06)

**Status:** coupling/union-bound proof; CP1 and independent review pending. Follow-up to Local L054 and G102. Existing-record search found the effective-cone fit but no clean-dependency-cone bound. This uses elementary deterministic dependencies and Bernoulli/union bounds, not a new concentration theorem.

Couple an ideal radius-one synchronous history and a raced history from the same arbitrary initial row. Assume every unflagged update reads its three parents from the raced history's previous logical row and applies the original rule; flagged updates may read already-computed neighbours as in races.c. For target(i,t), take all ancestor update nodes (j,s), 1<=s<=t, |j-i|<=t-s. There are t² distinct nodes on the line. On a W-cell ring, deduplication gives M=sum over s1..t of min(W,2*(t-s)+1)<=t².

**Clean-cone lemma.** If no ancestor node is flagged, target(i,t) equals the ideal value, regardless of flags outside the cone. Proof: induction from the common initial row through the cone's generations. Each cone update is unflagged and its three parents lie in the preceding cone layer. All those parents therefore agree, and applying the same deterministic rule preserves equality. New-value propagation outside the cone cannot enter via an unflagged node. Snapshot reads at unflagged nodes are an explicit assumption, not a claim about arbitrary in-place updating.

With independent Bernoulli(eps) flags, the clean event has probability(1-eps)^M. Consequently

    P(target differs)<=1-(1-eps)^M<=1-(1-eps)^(t²).

Without independence, if every flag has marginal probability at most eps, the union bound still gives P(target differs)<=min(1,eps*t²). Neither bound assumes fair states, injected-error independence, a measured speed0.246, damage irreversibility or a half-differing interior. Averaging cell indicators gives the same bound for the expected disagreement fraction D_t on a finite ring; spatial independence is unnecessary. Markov's bound also gives P(D_t>=delta)<=min(1,[1-(1-eps)^(t²)]/delta).

For 0<eps,delta<1, mean disagreement at least delta requires

    t>=sqrt(log(1-delta)/log(1-eps))

under independent flags, and t>=sqrt(delta/eps) under the marginal-only bound. Thus the necessary timescale is at least order eps^(-1/2) as eps tends to0, for any fixed mean threshold. This is a lower constraint on the onset of mean decoherence, not a matching upper estimate, exact survival law, realised hitting-time bound or exponent fit. It does not turn Local's measured coefficient0.623 into a theorem. Local's fractions concern finite realised runs.

**Unexpected final-tick guard.** On a five-cell ring started from a black cell at2, allow a right race only at site0 on step1, then no races on step2. Site1 on step2 differs from the ideal history despite its own final update being unflagged. Its ancestor at(step1,site0) was flagged. Checking just the final target is insufficient.

**CP1 preregistered NOT RUN.** For W3..5,T1..2, enumerate all initial rows and flag histories in both sequential race directions with races.c's boundary convention. Require agreement at every site with a clean cone. Use exact weights at eps0,1/4,1/2,1 and require every site disagreement probability to obey both bounds. Independently construct ancestor sets, and retain the final-tick guard. This is77440 short row/flag cases, no stochastic simulation or eps-scaling rerun. Publish predictions and instrument before execution.


**CP1 outcome (2026-10-06 19:56 BST).** Ran after prediction and instrument publication through43095bf. PASS: 77440 initial-row/flag histories and192 exact weighted site bounds. Every clean-cone site agrees, both independent-flag and marginal-only bounds hold, and the final-unflagged/earlier-ancestor guard differs as predicted. These finite controls support the coupling proof; they provide no matching rate, effective cone or realised hitting-time claim. Independent colleague review remains pending.

*Second reader's note on G103 (Local, 2026-10-06; chat L058).* Correct. An unflagged node reads only the previous
logical row, so a cone with no flag stays exact whatever happens outside it, and the cone has $t^2$ update nodes
(fewer on a small ring). Checked (`rule30_audit_g99_g100.py`, S6): on rings of 3 to 5 cells for $T \le 2$, every
initial row and every flag history in both race directions, every clean-cone site agrees with the ideal history and
every site's exact disagreement probability at $\epsilon = 1/4, 1/2, 1$ obeys both bounds; the final-tick guard
gives the raced row $[1, 1, 1, 1, 0]$ at step 1 and a differing site 1 at step 2. Against my race run
(`rule30_races.py`), the measured time to a quarter disagreement exceeds the bound $\sqrt{\ln(3/4)/\ln(1 - \epsilon)}$
by a factor 2.68 to 2.81 at every $\epsilon$ from $10^{-3}$ to $10^{-7}$: the bound has the right $\epsilon^{-1/2}$
form, and the constant $\sqrt{\ln 2 / (0.623 \cdot \tfrac12 \cdot \ln \tfrac43)} = 2.78$ is the measured part (the
half-differing interior, the injection probability $1/2$ and the cone area 0.623).

### G.GPT104. right-reading races keep the fair row law; left-reading races change pairs (second-read by Local, 2026-10-06)

**Status:** bulk spatial-law proof; OM1-OM2 pass, independently reviewed by Local L059. Follow-up G102/G103 and Local L054. Prior-art abstract checks are recorded in PRIOR-ART.md; no imported theorem or novelty claim. This is the sequential snapshot/raced-neighbour model, not a general asynchronous cellular automaton.

On the infinite line, take old row x iid fair and a fixed flag pattern r independent of x. For right-reading updates, assume every rightward consecutive flag run terminates, so the recursion

    y_i=x_(i-1) xor (x_i OR [y_(i+1) if r_i=1 else x_(i+1)])

is well-defined by a finite recursion at every site. This condition holds almost surely for independent Bernoulli(eps) flags with eps<1.

**Right-law proposition.** Conditional on any such fixed flag pattern, y is iid fair. Proof: for output block[a,b], fix all old bits at sites>=b. This fixes y_(b+1), whose recursion uses only those tail bits. Given any prescribed y_a..y_b, solve right-to-left:

    x_(i-1)=y_i xor (x_i OR [y_(i+1) if r_i=1 else x_(i+1)]).

There is exactly one preimage among the b-a+1 old bits at[a-1,b-1]. They were independent fair even conditional on the tail, so every output block has probability2^(-(b-a+1)). This proves the product law for every finite block. Adaptive flags depending on x are excluded. Independent new flag fields at each logical step therefore preserve the fair spatial law at every step, although the temporal history need not match the ideal orbit.

**Earned extension of G102.** In this infinite right-reading model, the current noisy row remains iid fair and is independent of the next fresh flags. Thus G102's bulk conditional injection rate1/(8-4eps) applies at each step relative to F(current noisy row), for eps>0. It is not the disagreement rate relative to the original ideal history, and does not supply a survival law. This is no exact finite-ring invariant-measure claim.

**Left contrast and unexpected density guard.** For left-reading updates, assume each leftward flag chain terminates, and use

    y_i=[y_(i-1) if r_i=1 else x_(i-1)] xor (x_i OR x_(i+1)).

Expanding the chain ending at i exposes a fresh far-left old bit with XOR coefficient1, independent of all old bits at sites>=i. Therefore y_i is fair and independent of those higher old bits, conditional on the fixed flags. If r_(i+1)=0, y_(i+1) depends on x_i,x_(i+1),x_(i+2), so P(y_i differs from y_(i+1))=1/2. If r_(i+1)=1, their XOR is x_(i+1) OR x_(i+2), so that probability is3/4. Independent Bernoulli flags with0<=eps<1 give first-row adjacent disagreement1/2+eps/4 despite both densities remaining1/2. Thus the left map does not preserve the iid fair row law for eps>0.

This separates unchanged density from unchanged pair law. The left formula is for a fair input row and is not asserted at later noisy steps. Local's finite-ring later-time descriptive statistics are not being relabelled refuted; the theorem is about explicit infinite-bulk law and first-step scope. No selected-seed conclusion follows.

**OM1-OM2 preregistered NOT RUN.** OM1: widths1..4, every right flag pattern, every fixed three-bit synchronous terminal tail and every old block; require a bijection to output blocks and recovery by the independent XOR inverse. OM2: anchored left depths0..3, all old rows and flag patterns; require density1/2, pair disagreement1/2 or3/4 according to the right cell's flag. Exact weights at eps0,1/4,1/2,1 must give pair law1/2+eps/4. Counterfactual that unchanged density forces fair pairs must fail. No noisy long-run measurement or Local job. Publish predictions and instruments before execution.



**OM1-OM2 outcome (2026-10-06 20:07 BST).** Executed after predictions and instrument publication through8753ab0. OM1 PASS: 2720 right input cases, every fixed-tail/flag block map bijective and independently inverted. OM2 PASS: 10880 left input cases and48 exact rational weighted moments. Both densities are1/2, but left adjacent disagreement is1/2+eps/4 as predicted. The eps1 checks are finite anchored endpoint controls; the infinite terminating-chain theorem excludes eps1. These controls support the spatial-law proof, not ideal/noisy history survival or exact cyclic invariance. Local independently reviewed it in L059.


*Second reader's note on G104 (Local, 2026-10-06; chat L059).* Correct. With the tail at sites $\ge b$ fixed, the
right-reading recursion inverts uniquely from right to left, so fair rows stay fair under independent flags; the
left-reading chain exposes a fresh far-left bit (density $1/2$), while a raced right cell makes the pair XOR
$x_{i+1} \vee x_{i+2}$. Checked (`rule30_audit_g99_g100.py`, S7): a bijection for every flag pattern and tail at block
widths up to 5; on a fair first row, left races give density $1/2$ and adjacent disagreement $1/2, 9/16, 5/8, 3/4$
at $\epsilon = 0, 1/4, 1/2, 1$, which is $1/2 + \epsilon/4$. This fits my race run (right-race rows stayed at 1/2 in
density and pairs; the left-race pair bias $\epsilon/4 \le 0.00025$ was below its resolution) and sharpens its
summary: one direction of fuzz leaves the row law exactly intact, the other leaves a fingerprint in the pairs.

### G.GPT105. cyclic closure changes the zero-row mass (second-read by Local, 2026-10-06)

**Status:** finite-ring preimage proof; ZR1 passes, independently reviewed by Local L060. Follow-up G104 and Local L054. This is a scope audit of the finite cyclic snapshot/sequential model in races.c, not a new damage-speed or prize theorem. Existing-record checks found fair infinite-row invariance and healing in structured backgrounds; these do not establish finite cyclic uniform invariance.

Take W>=3 cells with indices modulo W, old row x uniformly distributed over all 2^W words, and a fixed state-independent flag word. Sequential right-reading updates process W-1 down to0; an effective race at i<W-1 uses already-computed y_(i+1), otherwise old x_(i+1). Left-reading updates process0 up toW-1; an effective race at i>0 uses y_(i-1), otherwise old x_(i-1). The first processed cell always uses the old cyclic neighbour, so its flag is ineffective.

**Right zero-row preimages.** If the entire new row is zero, every update requires

    x_(i-1)=x_i OR [0 if the right race is effective else x_(i+1)].

If any x_i=1, this equation forces x_(i-1)=1, then repeats around the ring to force all old cells1. Conversely both the all-zero and all-one old rows produce the all-zero new row for every right flag pattern: induction in the scan order, using centre1 to keep the OR1 in the all-one case. These are the only two preimages. Thus conditional on any flags,

    P(new row is all zero)=2^(1-W).

The uniform ring law assigns that row probability2^(-W), so it is not invariant under any fixed right flag pattern or any state-independent mixture of them. G104's infinite-line fair product theorem is intact; closing the inverse around a cycle removes its independent tail. This mass discrepancy is exponentially small as W grows and does not refute Local's large-ring approximate statistics.

**Left zero-row preimages.** Any old1 at an effectively raced site would give new1 because its new left input is0. Therefore an old1 must sit at a nonraced site, where a zero output forces its old left neighbour1. Repeating this implication around the ring either encounters an effective race (a contradiction) or forces the whole old row1 with no effective flags. The all-zero old row always maps to zero. The all-one row does so exactly when no effective left flags are present. Consequently the zero row has one preimage when any effective left flag is present, and two otherwise. With independent Bernoulli(eps) flags,

    P(new row is all zero)=[1+(1-eps)^(W-1)]*2^(-W).

For0<=eps<1 this too differs from the uniform ring law. At eps1 the zero-row mass alone does not decide invariance; no claim is made from this one cylinder.

**No universal decoherence upper bound.** From the common all-zero initial row, ideal and raced histories remain identically zero for all logical times, every flag sequence and either scan direction. Thus no positive mean threshold can have a finite state-uniform onset bound, even with independent positive-rate flags. A matching upper side to G103 needs initial-state or activity assumptions. Fair marginal rows by themselves also cannot specify a coupling: equal copies have disagreement0, while independent fair copies have disagreement1/2, and synchronous Rule30 preserves both constructions' marginals. Those example couplings are not the common-initial-state race process; they only refute inference from marginals alone.

**Unexpected boundary/healing guard.** On a ring, distinct all-zero and all-one rows merge to the same all-zero row in one synchronous tick. Left permutivity therefore supplies no blanket finite-ring noncoalescence theorem. Infinite-line rightmost-damage propagation requires a rightmost discrepancy; these two infinite constant rows would have none. Local's background-dependent healing is preserved, not contradicted.

**ZR1 preregistered NOT RUN.** For W3..7, enumerate every old row and every flag word in both scan directions using the literal Rule30 truth table. Count zero-output preimages for every flag word: right always2; left1 or2 according to whether any effective flag is present. Independently apply exact Bernoulli weights at eps0,1/4,1/2,1 and compare the two formulas. Predict43648 row/flag/direction cases and40 weighted probability checks. Retain zero-row closure and the synchronous two-preimage healing guard. Counterfactual that G104 gives exact finite-ring uniform invariance must fail. This is a short exact enumeration, no long-run or Local scaling job. Publish before execution.



**ZR1 outcome (2026-10-06 20:13 BST).** Ran after proof, predictions and instrument publication throughf0f3a1b. PASS:43648 row/flag/direction cases and40 exact rational weighted probabilities. Right zero-row preimages are exactly zero and one for every flag pattern; left has only zero whenever any effective flag is present. Absorbing-zero and synchronous cyclic-coalescence guards pass. This confirms the finite preimage formulas; it supplies no long-run invariant measure, matching decoherence rate or selected-seed result. Independent review remains pending.


*Second reader's note on G105 (Local, 2026-10-06; chat L060).* Correct. A zero new row forces
$x_{i-1} = x_i \vee R_i$ around the ring, so one old 1 spreads to all; the left scan's raced sites forbid old 1s. Checked
(`rule30_audit_g99_g100.py`, S8) with my own sequential race step on rings of 3 to 7 cells, every flag word and both
directions: exactly 2 zero-row preimages for right races, 1 or 2 for left races according to an effective flag, the
exact masses $2^{1-W}$ and $[1 + (1-\epsilon)^{W-1}]\,2^{-W}$ at four values of $\epsilon$, and the zero row fixed
under every flag word. This qualifies my race run's summary: on a finite ring the exact row law fails (the zero row's mass
is doubled, an exponentially small amount for one event; GPT's G103 note: this is not a bound on total variation or
on any other statistic, so how close the ring stays overall is open), and "the fuzz replaces the history" needs an active state: the empty
row is never replaced.


**GPT scope clarification after L060.** The zero-row probability discrepancy is exponentially small. This one cylinder supplies no upper bound on total variation of the whole row law or on every local statistic, especially at later times. General finite-ring closeness remains open.

### G.GPT106. spatial fairness survives right races; the moving-frame change does not (second-read by Local, 2026-10-06)

**Status:** infinite-bulk one-step flip-law proof; TF1 passes, independently reviewed by Local L061. Follow-up G97/G102/G104. Existing record separates spatial invariance from temporal independence; this derives a changed temporal mean in the specific right-reading race model. No general probabilistic-CA theorem, novelty or selected-seed claim is imported.

Use G104's infinite right-reading recursion with fair iid old row x and fresh independent Bernoulli(eps) flags,0<=eps<1. Let y be the next noisy row. For an observer moving by delta in{-1,0,1}, its flip is x_i XOR y_(i+delta). All flag chains terminate almost surely. The fresh flag field is independent of the current old row at each step.

**Nonrightward mean.** For delta0, y_i has form x_(i-1) XOR A, where A involves only old bits at sites>=i, even through raced-neighbour recursion. The bit x_(i-1) is fresh fair and independent of x_i and A, so the flip is fair. For delta-1, y_(i-1) similarly exposes fresh old x_(i-2). Thus both flip probabilities are1/2, conditional on any terminating fixed flag pattern. This is a marginal statement, not temporal independence of successive flips.

**Rightward mean.** Write

    A_j=x_j OR [y_(j+1) if r_j=1 else x_(j+1)].

The rightward observer's flip is x_i XOR y_(i+1)=A_(i+1). If r_j=0, A_j is the OR of two fair bits, hence has mean3/4. If r_j=1, y_(j+1)=x_j XOR A_(j+1), so

    A_j=x_j OR (x_j XOR A_(j+1))=x_j OR A_(j+1).

Here x_j is independent fair relative to A_(j+1), which depends only on higher old sites and flags. Let U be the translation-invariant mean of A_j. Conditioning on r_j gives

    U=(1-eps)*3/4+eps*(1/2+U/2)=(3-eps)/(4-2eps).

Hence U=3/4+eps/(8-4eps). The additive change is the total right-race injection rate from G102; this equality concerns a one-step temporal observable, not ideal/noisy disagreement accumulated over time. G104 preserves the fair spatial row law and independence from each next fresh flag field, so these flip means hold at every logical step in this ensemble.

**Predetermined moving path.** For N observer increments in{-1,0,1}, with N_right rightward increments, linearity of expectation gives mean flip count

    N/2+N_right/(4-2eps).

This extends G97's synchronous mean. It supplies no independence, covariance, variance, concentration or claim about an adaptively chosen observer. The infinite model excludes eps1; the finite anchored limit as eps tends to1 is a separate endpoint control.

**Finite anchored prediction.** With D potentially raced sites before a synchronous right terminal, define U_0=3/4 and U_D=3/4-eps/4+(eps/2)*U_(D-1). Then

    U-U_D=[eps/(8-4eps)]*(eps/2)^D.

For finite D these are polynomial probabilities also defined at eps1. At eps1, U_D=1-2^(-D-2); this does not define a nonterminating infinite update.

**Unexpected temporal guard.** With eps1/2, the infinite rightward flip mean is5/6, not3/4, although every noisy spatial row remains iid fair. Equal spatial measures need not give equal transition measures. This directly addresses the owner's temporal-field motivation without claiming physical acceleration or a prize result.

**TF1 preregistered NOT RUN.** D0..4, enumerate all old words on sites-2..D+2 and every flag pattern on sites-1..D, with siteD+1 a synchronous terminal. Use the literal Rule30 truth table to compute the next block, then count observer flips for delta-1,0,1. Exact flag weights at eps0,1/4,1/2,1 must give1/2,1/2,U_D. Independent control is the conditioned OR recurrence, including its exact remainder, against full word/flag enumeration. Predict43648 cases and60 weighted flip checks; this count happens to match ZR1 but the objects differ. Counterfactual that unchanged spatial law forces unchanged rightward flip mean must fail. Publish predictions and instrument before execution; no long-ray or colleague race-statistics rerun.



**TF1 outcome (2026-10-06 20:18 BST).** Executed after proof, predictions and instrument publication throughd05bb6b. PASS:43648 old-word/flag cases and60 exact rational weighted flip means. Left/stay means1/2 hold for every finite flag pattern; right U_D and its bulk remainder agree at every declared depth and eps. Finite eps1 checks remain anchored endpoint controls. The infinite eps1/2 rightward mean5/6 follows the proved recurrence, not a long-run empirical fit. No temporal independence, variance or ideal/noisy survival result follows. Independent review remains pending.

*Second reader's note on G106 (Local, 2026-10-06; chat L061).* Correct. The rightward flip is $A_{i+1}$, and a raced
site gives $A_j = x_j \vee A_{j+1}$ with $x_j$ fresh, so $U = (3 - \epsilon)/(4 - 2\epsilon)$; stays and left steps
keep a fresh far-left bit. Checked (`rule30_audit_g99_g100.py`, S9) by exact enumeration of old words and flags for
$D \le 4$ at $\epsilon = 0, 1/4, 1/2, 1$: means $1/2$, $1/2$ and $U_D$ with the stated remainder; the limit at
$\epsilon = 1/2$ is $5/6$. This is the cleanest answer yet to the owner's fuzz question: every snapshot stays fair,
and the fuzz shows only in the temporal field seen by an observer moving right.

### G.GPT107. nonrightward traces stay fair under any fixed right-race schedule (second-read by Local, 2026-10-06)

**Status:** conditional trace-law proof; NT1 passes, independently reviewed by Local L062. Extends G97's synchronous fresh-bit proof to G104's right-reading recursion, following G106 and Local L061. This is a model-specific extension of known left permutivity, not a prize solution or novelty claim. Existing record G97 supplies the synchronous argument; G104 supplies the terminating recursion.

Start on the infinite line from an iid fair row. Allow any fixed right-reading flag field whose rightward runs terminate at every site and logical step. It need not be spatially or temporally independent. For random flags, require the entire flag field to be independent of the initial row, and termination almost surely. Fresh Bernoulli flags with eps<1 satisfy this. Adaptive flags selected from states are excluded.

**Triangular composition lemma.** Conditional on the whole flag field, each time-t value at site i has form

    x_t(i)=x_0(i-t) XOR g_(t,i)(initial bits strictly to the right of i-t).

Its dependency uses only finitely many initial bits at each finite t. Proof by induction: one right-reading update is x_(t-1)(i-1) XOR A, and the OR/recursive term A uses only previous-row sites>=i. Each recursion terminates, so it has finitely many such inputs. Their initial left endpoints are at least i-(t-1)=i-t+1; only the left input exposes initial bit i-t, with XOR coefficient1. Finite composition of finite recursion trees remains finite. Thus the fresh leftmost initial bit never enters the other term, even though the right dependency may be arbitrarily long.

**Conditional trace law.** Fix a predetermined path p_0,p_1,... with p_t nonincreasing. Define L_t=p_t-t, which strictly decreases. Earlier samples depend only on initial sites>=L_s>L_t. Given all other initial bits and the flag field, the current sample contains the untouched fair bit at L_t, whereas all earlier samples are fixed. It is therefore fair independent of the earlier sample vector. Induction gives iid fair sampled bits conditional on the full flag field. Their distribution does not depend on that field, so the trace is also independent of the flag field as a random object (equality of every finite cylinder law).

Each N-vector of consecutive XOR flips has exactly two sample-vector preimages, so flips are iid fair, mean count N/2 and variance N/4. This now earns the nonrightward temporal-independence result deliberately left open by G106. No state-law induction or independence between successive flag rows is needed: conditioning first handles all their correlations.

**Scope and unexpected coupling guard.** Under these assumptions a single predetermined nonrightward trace has exactly the same statistical law as the synchronous fair-ensemble trace. This does not say the noisy and ideal traces coincide, nor that their two copies are independent: at eps0 they are the same random trace. Their joint history remains a separate question. No selected-seed, finite-ring, adaptive-observer or multisite-transition claim follows. Rightward observers are excluded; G106's rightward mean differs from1/2 even at eps0. Thus this theorem cannot justify calling every temporal observable insensitive to races.

**NT1 preregistered NOT RUN.** T1..3; every path with increments-1 or0; every T-bit schedule switching entire update rows between synchronous and right-reading races, except a fixed synchronous right terminal. Enumerate every initial word on sites-2T..T+1 and evaluate by literal Rule30 tables with shrinking finite boundaries. For each path/schedule, group inputs by all bits except the fresh pivots L_0..L_T: every conditional group must map bijectively onto sampled words. Independently check uniform flip words and mean/variance T/2,T/4. Predict135296 word/path/schedule cases and8736 conditional bijection classes. The schedule family includes fully correlated successive flags, not just fresh Bernoulli rows. Retain the eps0 identical-copy guard using the same inputs. This finite control supports the conditional proof; no simulation fit or colleague job. Publish before execution.



**NT1 outcome (2026-10-06 20:23 BST).** Executed after conditional proof, predictions and instrument publication throughe779bd0. PASS:135296 word/path/schedule cases and8736 conditional pivot-bijection classes. Sample and flip vectors are uniform in every declared path/schedule, with flip-count mean T/2 and variance T/4. The zero-flag history agrees with an independent synchronous XOR/OR formulation, confirming the identical-copy guard. These finite anchored controls support the infinite conditional fresh-bit proof; they establish no selected-seed, finite-ring or joint ideal/noisy independence claim. Independent review remains pending.


*Second reader's note on G107 (Local, 2026-10-06; chat L062).* Correct. One right-reading update is
$x_{t-1}(i-1) \oplus A$ with $A$ built from previous-row sites $\ge i$, so the leftmost initial bit of each cone enters
with coefficient 1 whatever the fixed flag field, and a nonincreasing path meets a fresh one at every step. Checked
(`rule30_audit_g99_g100.py`, S10): for $T \le 3$, every nonincreasing path and every schedule switching whole rows
between synchronous and right-reading-everywhere updates (fully correlated rows), the sampled vector is uniform over
all initial words on sites $-2T$ to $T + 1$. My L061 phrase "visible only in the temporal field of a right-moving
observer" is narrowed accordingly: among the observables classified so far.

### G.GPT108. ideal and noisy traces share a causal invertible coupling (second-read by Local, 2026-10-06)

**Status:** conditional finite-horizon coupling proof; CT1 passes, independently reviewed by Local L063. Follow-up G97/G102/G107. Existing-record search found the fresh-bit marginal trace law but no paired causal-mask representation. This uses elementary triangular bijections and entropy counting, not a new general coding theorem or prize solution.

Fix a horizon N, a predetermined nonrightward path, and a terminating right-reading race field independent of the fair initial row as in G107. Couple the ideal synchronous and noisy histories from that same row. Write I_t and J_t for their sampled bits, t0..N. Their distinct fresh initial pivots are L_t=p_t-t. Let R contain all initial bits outside these N+1 pivots, and fix R and the entire flag field. The remaining pivot bits xi_t=x_0(L_t) are independent fair.

**Triangular pair representation.** G97 and G107 give

    I_t=xi_t XOR a_t(xi_0,...,xi_(t-1);R),
    J_t=xi_t XOR b_t(xi_0,...,xi_(t-1);R,flags).

Neither expression uses later pivots, which lie strictly to the left of its dependency boundary. Both expose the same current pivot with coefficient1. Inverting the first expression recursively recovers xi_<t from I_<t and R. Cancelling xi_t therefore yields

    J_t=I_t XOR e_t(I_0,...,I_(t-1);R,flags),   e_0=0.

This is causal: the time-t mask needs no current or future ideal sample. The map from I_0..I_N to J_0..J_N is itself a triangular bijection, recoverable successively from either trace when R and flags are known. Each trace separately is uniform conditional on this environment, yet their conditional joint law has only2^(N+1) equally likely pairs, rather than2^(2N+2).

In bits, conditional entropy of each trace and of their pair isN+1; conditional mutual information between the traces isN+1. These are statements conditional on R and flags. They do not make the unconditional coupling invertible, give its unconditional mutual information, or let an observer recover a hidden schedule from one trace. G107's independence of the single trace from the flag field is compatible with this conditional relation.

**Predictable-mask qualification.** Conditional on R and flags, e_t is determined by the past ideal samples. The current ideal sample is fresh fair independent of that past, so it is independent of the current mask under that conditioning. The masks need not be independent over time or independent of past samples. Their law remains the missing joint-history object, not something spatial invariance determines.

**First-tick state dependence.** For a stationary target i, let E_1=I_1 XOR J_1. On the common fair initial row, a right race can change its OR term only if x_0(i)=0. If x_0(i)=1, both OR values are1 and E_1=0. With fresh iid Bernoulli flags of rate0<=eps<1, G102's total injection probability gives

    P(E_1=1 | I_0=1)=0,
    P(E_1=1 | I_0=0)=eps/(4-2eps),
    Cov(E_1,I_0)=-eps/(16-8eps).

The latter follows because I_0 is fair, E_1*I_0 is always0, and E[E_1]=eps/(8-4eps). Thus even the first error is not state-blind or independent of the past observed bit for eps>0. This does not contradict iid marginal samples; it concerns the pairing of the two copies.

**Unexpected causal-mask guard.** Fix old sites1,2 to0,1, let only target0 read its updated right neighbour, and update site1 synchronously. Vary the two fresh pivots old0 and old-1 fairly. Then I_1=old-1 XOR I_0 while J_1=old-1 XOR1, so E_1=1-I_0. Each two-sample trace is uniform, but its partner is a deterministic bijective scramble given this environment. A state-independent fair error bit would be the wrong coupling. No selected-seed, finite cyclic survival or matching upper decoherence rate follows.

**CT1 preregistered NOT RUN.** Reuse NT1's literal right-reading history evaluator and an independent synchronous XOR/OR evaluator. For T1..3, all left/stay paths, all global-row switch schedules and all initial words on-2T..T+1, group by nonpivot initial bits. Require both trace projections bijective within each group, paired support size2^(T+1), and each time-t XOR mask constant for a fixed ideal prefix of length t. Predict135296 paired cases and8736 conditional classes. Independently check the four-pivot-input causal-mask guard above. This is a paired-law audit, not a repeat of NT1's marginal statistic; the existing first-tick weighted G102 control supplies the rate formula. Publish before execution.



**CT1 outcome (2026-10-06 20:29 BST).** Ran after paired proof, predictions and instrument publication through85f0972. PASS:135296 paired cases and8736 conditional triangular-coupling classes. Both projections are bijective, every time-t mask is determined by the ideal prefix of length t, and the four-input guard gives E_1=1-I_0. These controls support the conditional causal representation and its support/entropy count, not an unconditional independence, information value or survival rate. Independent review remains pending.

*Second reader's note on G108 (Local, 2026-10-06; chat L063).* Correct. Both traces expose the same fresh pivot at
each step with coefficient 1 and use only earlier pivots otherwise, so the second is the first scrambled by a causal
mask. Checked (`rule30_audit_g99_g100.py`, S11): for $T \le 3$, every nonincreasing path, whole-row schedule and
non-pivot assignment, both traces are bijective images of the pivots and $I_t \oplus J_t$ is a function of
$I_0 \ldots I_{t-1}$ alone; the guard gives $E_1 = 1 - I_0$ for all four pivot values. The first-tick rates follow from
G102's verified injection rate. This also tightens the reading of my race run: its survival law treats errors as
injected blindly, while the first error already depends on the observed state.

### G.GPT109. an isolated race error heals once and returns (second-read by Local, 2026-10-06)

**Status:** local damage-echo proof; EH1-EH2 pass, independently reviewed by Local L064. Follows G102/G108 and Local L063. Existing record discusses background-dependent healing and state-dependent injection but not this source-site echo. This is a local Boolean mechanism, not a new global damage law, Markov closure or prize solution.

**Single-flip kernel.** Take any line background z and a second row differing only by a flipped bit at site0. Let delta_s(i) be their XOR disagreement after s synchronous Rule30 steps. At s0 the error is only at0. At s1,

    delta_1(-1)=1-z(-1), delta_1(0)=1-z(1), delta_1(1)=1.

These follow respectively from sensitivity of the OR's right input, sensitivity of its centre input, and the permutive left input. Let b=F(z). For the second synchronous step, delta_2(0)=z(1) OR z(2).

To prove this last identity, split on z(1). If z(1)=1, delta_1(0)=0 and b(0)=1-z(-1). Hence delta_2(0)=(1-z(-1)) XOR (1-b(0))=1. If z(1)=0, both centre and right inputs are flipped at s1. Toggling both OR inputs changes its value by1 XOR b(0) XOR b(1). Here b(0)=z(-1) XOR z(0) and b(1)=z(0) XOR z(2). Adding the left disagreement1-z(-1) cancels the z(-1) terms and leaves z(2). Both cases give the OR formula. This is an arbitrary-background identity, requiring no state probabilities.

**Isolated right-race injection.** Start ideal and raced copies from the same arbitrary old row x. On logical tick1, only site0 has an effective right-reading race; site1 is synchronous and already computed. All other sites read the old snapshot. Then the only possible first-row discrepancy is at0, and

    E_1=(1-x(0))*(1-x(1))*x(2).

Indeed an old black target masks the changed right value; with x(0)=0 the updated right neighbour is x(1) OR x(2), so disagreement requires old pattern001 at sites0..2. If no injection occurs, the two rows agree and continue to agree while subsequent ticks are synchronous.

If an injection occurs, the ideal first row z=F(x) has z(1)=1. Apply the single-flip kernel to these first rows. At the original source, disagreement over ticks1,2,3 is exactly

    1, 0, 1.

The second tick heals the source because the ideal right neighbour is black, while the error propagates to site1. The third-tick return follows from delta_2(0)=z(1) OR z(2)=1. There is no new injection in this experiment. Local source healing therefore does not imply the histories have coalesced or that the source will remain healed.

**Fair-input finite law.** On an iid fair initial row the injection probability is1/8 (G102's isolated event). Conditional on injection, second-tick disagreement is always present at site1, absent at0, and present at-1 precisely when x(-2)=x(-1). Thus the second-tick damage set is{1} or{-1,1}, each with probability1/2, and its mean size is3/2. These are conditioned short-time laws; they do not describe dense repeated races, chained injections, finite-ring wraparound or a global survival rate.

**Unexpected echo guard.** The event E_1=1,E_2=0,E_3=1 is forced for every injected isolated right race. It refutes the counterfactual that “healed at a source” means “permanently healed,” and explains why state-blind permanent-defect accumulation is not an exact coupling. It does not refute Local's finite empirical survival fit.

**EH1-EH2 preregistered NOT RUN.** EH1: enumerate all32 backgrounds on-2..2, flip site0 and run two synchronous ticks with shrinking boundaries; require source signature1,1-z(1),z(1) OR z(2). EH2: enumerate all128 old words on-3..3, apply one isolated target right race on tick1, then two synchronous ticks. Predict16 injections, all source signatures101; the other112 give000. Second-tick damage sets{1} and{-1,1} must occur8 times each. Independently verify synchronous propagation with the XOR difference-of-OR equation, rather than the truth-table implementation. These160 exact cases replace no Local long-run job. Publish predictions and instrument before execution.



**EH1-EH2 outcome (2026-10-06 20:34 BST).** Ran after proof, predictions and instrument publication throughf9aa008. EH1 PASS:32 arbitrary backgrounds and the source kernel1,1-z(1),z(1) OR z(2). EH2 PASS:128 initial words; exactly16 injections, all source signatures101, while112 noninjections give000. Second-tick masks{1} and{-1,1} occur8 times each. The independent XOR difference-of-OR propagation agrees throughout. This verifies the local echo, not repeated-race memory closure or a survival rate. Independent review remains pending.


*Second reader's note on G109 (Local, 2026-10-06; chat L064).* Correct. A flipped cell is the left input of its right
neighbour (always felt), the centre input of itself (felt iff $z(1) = 0$) and the right input of its left neighbour
(felt iff $z(-1) = 0$); an isolated right race injects exactly on the old pattern 001, which forces $z(1) = 1$. Checked
(`rule30_audit_g99_g100.py`, S12) with a propagation of the difference of the OR term, independent of the truth-table
code: the kernel $1, 1 - z(1), z(1) \vee z(2)$ on every background of seven cells; 16 injections among 128 words, each
with source signature $1, 0, 1$, the other 112 giving $0, 0, 0$; second-tick damage sets $\{1\}$ and $\{-1, 1\}$, 8 each.
An exact local reason why "healed" is not "coalesced".

### G.GPT110. the paired trace is not first-order Markov (second-read by Local, 2026-10-06)

**Status:** exact projected-memory counterexample; PM1 passes, independently reviewed by Local L065. Follow-up G108/G109 and Local L063's transition-table offer. Existing record provides causal masks and the source echo; this audits a concrete compressed state. It is not a general non-Markov theorem for repeated iid races or a new theory of hidden-state processes.

Use an infinite iid fair initial row. On tick1 only target0 reads its updated right neighbour; all other updates and all later ticks are synchronous. Let I_t,J_t be the ideal/noisy source samples and E_t=I_t XOR J_t. Consider the candidate observable state K_t=(I_t,E_t), equivalently the pair(I_t,J_t). The external pulse schedule is fixed and known.

G109 proves E_2=0 and E_3=E_1 for every initial row, with E_1 the indicator that old sites0..2 are001. Thus E_1 has probability1/8. By synchronous left permutivity, I_2 has form old(-2) XOR a function of old sites-1..2. That fresh old bit is fair independent of the injection event. Hence for b0 or1,

    P(E_1=1 | K_2=(b,0))=1/8,
    P(E_3=1 | K_2=(b,0))=1/8.

But conditioning further on the observed past error gives

    P(E_3=1 | K_2=(b,0),E_1=1)=1,
    P(E_3=1 | K_2=(b,0),E_1=0)=0.

Both earlier-error strata have positive probability in each current-state bin. E_1 is a function of past state K_1, so the next state's error component retains past information absent from K_2. This violates the first-order Markov property at tick2, even allowing a time-dependent transition kernel and the known pulse phase. Merely adding the current ideal sample to the current error does not close this projection.

**Unexpected marginal guard.** Both I_0..I_3 and J_0..J_3 separately are iid fair by G97/G107; the fixed isolated flag field is terminating and independent of the initial row. Each separate trace is therefore Markov, while their paired observable is not. This is an explicit distinction between marginal randomness and coupling memory, not a failure of the previous trace theorem.

A lagged error distinguishes the two groups in this three-tick example, but this proves no general finite-order closure. Repeated fresh Bernoulli races, finite rings and the selected seed are different models and remain to be checked. The full paired configuration remains a sufficient state for synchronous future evolution; this result is about a compressed single-site projection.

**Diagnostic for Local.** A useful measurement state is K_t=(I_t,E_t). Compare the empirical next-error fraction conditional on K_t with the same bins further split by E_(t-1); report counts for every bin. The pulse control must reproduce the exact split above. For repeated iid races, declare scope, flag rule, boundary, sample/replicate counts and predictions before running; a retained split is evidence against the proposed state, while a held finite table is not a Markov proof. GPT remains in the proof/counterexample lane and will not duplicate Local's measurements. No production-law split magnitude is predicted here.

**PM1 preregistered NOT RUN.** Enumerate all128 old words on-3..3; apply the isolated pulse and evolve to tick3 with literal Rule30 tables. Independently compute E_1 from the001 indicator and I_2's fresh-bit complement pairing. Predict current-bin counts8 for previous-error1 and56 for previous-error0, for each ideal bit b; next error equals previous error. Each marginal four-sample histogram must contain16 words8 times each. Counterfactual first-order Markov equality must fail in both bins despite uniform marginal traces. No long-run or colleague job. Publish before execution.



**PM1 outcome (2026-10-06 20:41 BST).** Executed after proof, predictions and instrument publication throughf922142. PASS:128 initial words. In each current ideal-bit bin, previous-error1/next-error1 count is8 and previous-error0/next-error0 count56; both opposite transitions have count0. Both marginal four-sample histograms contain16 words8 times each. The independent001 indicator and fresh-bit complement pairing agree. First-order Markov equality for the paired state is refuted in both bins of this isolated-pulse ensemble, not asserted refuted for repeated iid races. Independent review remains pending.


*Second reader's note on G110 (Local, 2026-10-06; chat L065).* Correct. $E_3 = E_1$ and $E_2 = 0$ come from G109; the
ideal bit $I_2$ carries a fresh old bit, so the injection has the same rate $1/8$ in both of its bins. Checked
(`rule30_audit_g99_g100.py`, S13) over all 128 words: in each bin $K_2 = (b, 0)$, 8 words with $E_1 = 1$ and 56 with
$E_1 = 0$, $E_3 = E_1$ always, and both four-sample traces uniform. The finite-ring production table GPT specified is
`rule30_race_memory.py` (Local's lane).

### G.GPT111. a finite-rate memory split extends to generic rates (second-read by Local, 2026-10-06)

### G111. A nonzero finite-rate memory split extends to generic rates, but a zero at one rate does not (2026-10-06)

**Status:** finite Bernoulli-polynomial certificate proof; PC1-PC3 pass; independently reviewed by Local L067. Complements Local's requested W5,T3 memory table without enumerating that job. Existing record has exact rational weighting and pulse memory; this derives a parameter-scope certificate. It uses elementary polynomial counting, not a general closure theorem or prize solution.

Let A be a positive-count current-state bin at tick2, B a refined past/current bin contained in A, and S the next-error event E3=1. With a fixed finite initial distribution independent of the flags, use m independent Bernoulli(eps) flags before the current tick and n independent flags for its next step. All probabilities below are finite sums of eps^k*(1-eps)^(M-k) terms with nonnegative fixed weights. Past-only probabilities P(A),P(B) have degree at most m; success probabilities P(S and A),P(S and B) have degree at most m+n.

Define the conditional-split determinant

    D(eps)=P(S and B)*P(A)-P(S and A)*P(B).

When both bins are positive, D differs from0 exactly when P(S|B) differs from P(S|A). Its degree is at most2m+n. Any bin with positive count at an interior rate has positive probability at every eps in(0,1), because each compatible finite flag history has positive weight there. Hence a nonzero D at one interior rate proves D is not the zero polynomial and the split holds at every interior rate except finitely many roots.

**Application conditional on Local finding a split.** W5,T3 has m8 effective flags before tick2 and n4 on tick3, so degree is at most20. At eps0 both copies are identical, making the success event impossible and D(0)=0. If an exact eps1/2 table finds a nonzero witness, that same witness can fail at no more than19 interior rates. In particular it holds for all sufficiently small positive eps, since a nonzero polynomial has only finitely many roots. This gives no numerical rare-rate threshold or magnitude without coefficients, no infinite-ring conclusion and no long-time survival law. This generic implication was prepared before receiving Local's table; the support application below uses its subsequently published certificate.

At eps1/2 every one of the131072 paired histories has equal weight, so the integer witness is

    n_(S,B)*n_A-n_(S,A)*n_B,

and its nonzero status is exactly D(1/2)'s nonzero status. To reconstruct D, retain each event count by total number of active flags k: h_k. The scaled probability polynomial is sum h_k*eps^k*(1-eps)^(12-k); divide by32 for the uniform initial-row probabilities. Polynomial expansion and multiplication use integer coefficients; the determinant's common positive scale does not affect its roots. Past degrees reduce to8 when the future flags are summed out.

**Unexpected held-rate guard.** For two independent flag bits X,Y, take A always, B={X=1}, S={X XOR Y=1}. Then

    D(eps)=eps*(1-eps)*(1-2eps).

Conditional-rate equality holds at eps1/2 while failing at eps1/4, where D=3/32. Thus a held table at one noise rate cannot certify even a single witness polynomial identically zero. Nor does an identically zero determinant for one refinement prove full Markov closure.

**PC1-PC3 preregistered NOT RUN.** A four-count-histogram polynomial tool will be checked on three independent two-flag toy predicates: PC1 S=X, predicted D=eps*(1-eps); PC2 S=Y, predicted D identically0; PC3 S=X XOR Y, predicted D=eps*(1-eps)*(1-2eps). All use A always and B={X=1}. Expand active-count histograms, compare to declared coefficient vectors, and independently enumerate the four flag histories with rational weights at eps0,1/4,1/2,1 (12 determinant checks). The unexpected PC3 half-rate equality must coexist with quarter-rate failure. This validates certificate arithmetic, not Local's production table. Publish before execution.


**Application to Local L066's complete table: a support witness needs no rate exceptions.** During this block Local published the exact enumeration with controls, preregistered at9de993f. GPT audited the script's complete32-row/4096-effective-flag-history coverage and right-reading model, but did not repeat the computational lane. Take A={I2=1,E2=0} and B={I1=1,I2=1,E1=0,E2=0}. Local reports n_A=52736,n_(S,A)=9216,n_B=25600,n_(S,B)=0. Thus D(1/2)=-225/16384, an exact nonzero split. More strongly, the zero count means S and B has no compatible history, whereas B and S and A each have positive counts. All finite histories retain positive weight for every0<eps<1. Therefore P(S|B)=0 while P(S|A)>0 throughout that interval: the finite W5 paired state is not first-order Markov for any interior rate, without exceptional roots. This support argument is a finite-ring result; it supplies no infinite-bulk or higher-order conclusion. The general polynomial method remains useful for nonextremal witnesses. Independent review of this extension remains pending.

**PC1-PC3 outcome (2026-10-06 20:54 BST).** Executed after predictions and instrument publication through d8d67d1. PASS: coefficient vectors [0,1,-1], [0] and [0,1,-3,2], with12 independent exact rational determinant checks. The unexpected XOR toy has equality at eps1/2 and a nonzero determinant3/32 at eps1/4. This checks the polynomial arithmetic only; Local's production enumeration was not repeated. Independent review of G111 remains pending.


*Second reader's note on G111 (Local, 2026-10-06; chat L067).* Correct. Each probability is a finite sum of
$\epsilon^k (1-\epsilon)^{M-k}$ terms with nonnegative weights, so the split determinant is a polynomial of degree at most
20 vanishing at 0, and a nonzero value at $1/2$ leaves at most 19 interior roots. The support argument is right: the
child $(1,1,0,0)$ has no history with $E_3 = 1$ while its parent $(1,0)$ has 9,216, and every finite history keeps
positive weight at every interior rate, so the split holds on all of $(0, 1)$; $D(1/2) = -225/16384$ (checked from
the counts). The toy determinants $\epsilon(1-\epsilon)$, 0 and $\epsilon(1-\epsilon)(1-2\epsilon)$ check by hand
($3/32$ at $\epsilon = 1/4$). The count spectrum GPT asked for, and an exact root count for every child against its
parent, are `rule30_race_memory.py --spectrum` (Local's lane).

### G.GPT112. two shared black observations shield the next tick (second-read by Local, 2026-10-06)

### G112. Two shared black observations shield the next tick and obstruct bulk first-order memory closure (2026-10-06)

**Status:** local proof and infinite-ensemble counterexample; WH1-WH3 pass, independently reviewed by Local L069. This explains Local L066's deterministic bin without repeating its production enumeration. It extends G109-G111 by a local argument, not by taking a ring limit. The general issue of projected Markov processes is established lumpability theory; the claim here is only this Rule30 coupling identity.

Let z_t be synchronous Rule30 and y_t its right-reading raced copy, with common initial row x. At each site the raced update reads the old left and centre and either the old or updated right neighbour. Write I_t=z_t(0), E_t=z_t(0) XOR y_t(0), K_t=(I_t,E_t). Flags may be arbitrary provided right recursions terminate. For the probabilistic conclusion use iid fair initial bits and fresh independent Bernoulli(eps) flags,0<eps<1, on the infinite line; these recursions terminate almost surely at every site and finite tick.

**First-step white agreement lemma.** If z_1(j+1)=y_1(j+1)=0, then z_1(j)=y_1(j). If x(j)=1, its old centre masks both right-read alternatives. If x(j)=0, the ideal right output0 equals x(j) XOR (x(j+1) OR x(j+2)), forcing x(j+1)=0. Both the old and updated raced right alternatives are then0, so the target updates agree. The lemma uses common initial input; it is not asserted for arbitrary later unequal rows.

**Two-black shielding.** Suppose z_1(0)=y_1(0)=z_2(0)=y_2(0)=1. The black old centre at site0 shields its tick2 right read. Output1 therefore forces z_1(-1)=y_1(-1)=0. Applying the white agreement lemma at j=-2 gives z_1(-2)=y_1(-2). When site-1 updates on tick2, its centre is0 but its old and updated right alternatives are both1. Its output is consequently the shared old left value XOR1, so z_2(-1)=y_2(-1). Site0's black old centre again shields tick3, yielding z_3(0)=y_3(0). Thus the refined bin

    B={I1=1,I2=1,E1=0,E2=0}

has next error E3=0 for every compatible shared-input history. This is a deterministic three-tick statement, independent of the rate and outside flag patterns.

**Positive finite cylinders, not an infinite clean event.** Define the nine update nodes C: tick1 sites-2..2, tick2 sites-1..1 and tick3 site0. Their ordinary ancestors are initial sites-3..3.

For initial word0110000 on-3..3 and all nine flags in C zero, both source traces have I1=I2=1, so B occurs. This cylinder has probability(1-eps)^9/128>0.

For initial word0000010 on-3..3, set only site0's tick1 flag in C to1 and all other eight to0. Its updated right neighbour at tick1 is an unflagged node of C, so no extra outside recursion enters. The ideal source trace at ticks0..3 is0011 and the raced trace0110: I2=1,E2=0,E3=1. The cylinder has probability eps*(1-eps)^8/128>0. Outside initial bits and flags are unrestricted in both constructions.

Take A={I2=1,E2=0} and S={E3=1}. The cylinders prove P(B)>0 and P(S and A)>0. The shielding identity proves P(S|B)=0, whereas P(S|A)>0. Since B further specifies past K1 within A, this violates the first-order Markov property of the single-site paired observable at tick2, even allowing time-dependent kernels. This proves neither failure of every finite memory order nor a long-time survival law. Each separate trace can remain iid fair as in G107; coupling memory is a different question. This is not a single-seed or prize claim.

**WH1-WH3 preregistered NOT RUN.** WH1: all initial rows and effective right-flag patterns on rings W3..5 (672 effective cases, equivalently1344 full flag assignments), test the first-step white agreement implication at every site. It must hold; this small one-step control is not Local's three-tick production table. WH2: implement the two explicit finite cylinders with shrinking boundaries and literal Rule30 table, independently compare the declared four-bit traces and synchronous XOR/OR updates; predict B and A intersect S respectively. WH3, unexpected orientation guard: on a W5 left-reading scan, initial00001 and only site1 flagged yield ideal/raced shared white output at site2 but different output at site1. The counterfactual that white agreement works for either scan direction must fail. Publish these predictions and instrument before execution; no production sweep or random trial.

**WH1-WH3 outcome (2026-10-06 20:59 BST).** Executed after proof, predictions and instrument publication through38eda50. WH1 PASS:672 effective one-step right-ring cases (equivalently1344 full flag assignments), with the white-agreement implication checked at every site. WH2 PASS:both explicit finite cylinders and independent literal-table/XOR-OR controls; pulse traces0011/0110 and the clean two-black bin agree with predictions. WH3 PASS:the left-reading00001 guard has shared white output at site2 and different output at site1, refuting orientation independence. These finite controls support the written local identity and cylinder construction; they do not themselves prove an infinite limit. The infinite conclusion rests on that argument and remains pending independent review.

*Second reader's note on G112 (Local, 2026-10-06; chat L069).* Correct, and both points GPT asked me to challenge
hold. White agreement: if $x(j) = 1$ the old centre masks both right reads; if $x(j) = 0$ the ideal white output
forces $x(j+1) = 0$, so both right alternatives are 0. The nine-node cylinders are closed: every unflagged node reads
the old snapshot, and the one flagged node (site 0, tick 1) reads an unflagged node of the cone. Checked
(`rule30_audit_g99_g100.py`, S14): white agreement at every site of every ring of 3 to 6 cells under every right flag
word; both cylinders on the line (the first gives $B$ with $E_3 = 0$, the second ideal 0011 and raced 0110 with
$I_2 = 1$, $E_2 = 0$, $E_3 = 1$); the left-scan guard breaks agreement as stated. The second cylinder lies in the child
$(0, 1, 1, 0)$, the one with the interior root in my spectrum: at that rate it matches its parent's rate, but here it
supplies $S \cap A$ at every rate, which is all the argument needs.

### G.GPT113. one lag does not close the pulse model at tick 5 (second-read by Local, 2026-10-06)

### G113. One lag does not close the isolated-pulse paired trace at tick5 (2026-10-06)

**Status:** exact finite-cone enumeration counterexample; independently reviewed by Local L070. Predictions and instrument published through2589f4f before execution. This is the pulse ensemble of G110, not the fresh Bernoulli-race model of G112 and not an all-orders impossibility claim.

Let K_t=(I_t,E_t) for the source of two common-input Rule30 copies. Start with an infinite iid fair row; only the noisy source0 reads its updated right neighbour on tick1, and all other reads and future ticks are synchronous. Keep the pulse schedule fixed and known. The seven source samples at ticks0..6 depend only on the13 initial bits at sites-6..6; the pulse's extra same-tick right read needs initial sites0..2 and stays inside that domain. Thus8192 equally weighted words give exact probabilities for this infinite ensemble. Literal Rule30 table updates were independently checked against XOR/OR updates throughout the shrinking cone.

Take A={K4=(0,0),K5=(0,0)} and its refinement B=A intersect {K3=(0,0)}. LM2 counts n_A=1872,n_(E6=1,A)=40,n_B=896,n_(E6=1,B)=0. Therefore

    P(E6=1 | A)=40/1872=5/234,
    P(E6=1 | B)=0.

Both bins have positive probability. Their next-error probabilities differ despite identical last two observed paired states; this violates second-order Markov at tick5, even with a time-dependent kernel and the known pulse phase.

The zero child also has an analytic explanation: G109 gives E3=E1, so B's E3=0 means no initial injection. With no future races the two configurations then agree forever. The positive parent-success count is the enumerated existence certificate, checked with both update formulations; it is not an extrapolation or a fitted probability. All count claims can be reproduced by tests/probes/rule30_gpt_lagged_memory.py. Independent reading remains required.

**LM1-LM3 outcomes (2026-10-06 21:05 BST).** LM1 PASS:8192 cone words,001 injection predicate and E1,E2,E3=indicator,0,indicator. LM2's blind split prediction HELD:8 unequal child-parent refinements among16 parents and36 positive children. A second child K3=(0,1),K4=K5=(0,0) has20 successes in40 histories, versus the parent's40 in1872; the rate difference is56/117. LM3, the unexpected marginal check, PASS:both separate seven-sample histograms have128 words64 times each. The permanent-healing counterfactual is refuted by the source echo. Uniform marginals coexist with failure of order-two paired closure. No result about third-order closure, every finite order, repeated fresh flags or long-time survival follows.

**LM4 outcome and explicit positive cylinder (2026-10-06 21:09 BST).** Predictions and instrument published through832c0d3 before execution. PASS:the lexicographically first success word on sites-6..6 is0011110010000, with ideal source trace0110000 and noisy trace0011001 at ticks0..6. It has K3=(0,1),K4=K5=(0,0),E6=1. The zero-child witness is0000000000000 with both traces0000000. These specify only13 initial bits, not the whole infinite row; each cylinder has probability1/8192. All eight independently implemented padded-boundary histories preserve the predicted traces. Arbitrary exterior independence follows from the explicit finite ancestor cone, not from extrapolating those eight tests.

Consequently the proof's positive parent-success event can be checked by forwarding this single finite word, without trusting a total-count census. The zero child follows analytically from E3=E1 and no future injections, while this cylinder gives P(E6=1 and A)>0 and hence P(E6=1|A)>0. The exact5/234 rate remains the independently controlled enumeration result; the order-two counterexample itself now needs only the identity and a finite positive cylinder. This strengthens inspectability without changing the pulse-model scope or claiming every finite memory order.



*Second reader's note on G113 (Local, 2026-10-06; chat L070).* Correct. The zero child is explained exactly: in $B$,
$E_3 = 0$ forces $E_1 = 0$ by G109, so no injection occurred and the copies agree forever. Checked
(`rule30_audit_g99_g100.py`, S15) with my own shrinking-cone evolution over all 8,192 words on sites $-6$ to 6:
$A$ has 1,872 words with 40 giving $E_6 = 1$, $B$ has 896 with none, the child $K_3 = (0, 1)$ has 40 with 20, and both
seven-sample traces are uniform (128 words, 64 each). Keeping the last two paired states does not close the pulse
model's paired trace.

### G.GPT114. a healed source can hide two cancelling errors (second-read by Local, 2026-10-06)

### G114. A healed white source can hide cancellation of two incoming errors (2026-10-06)

**Status:** local algebraic identity and hand-derived pulse mechanism; DP0-DP2 preregistered NOT RUN, independent review pending. This unpacks G113's explicit witness. G109 already gives the difference-of-OR propagation law; this is its Boolean expansion and a causal explanation, not new general damage-spreading theory.

For a synchronous tick, let a,b,c be ideal left, centre and right bits and p,q,r their respective XOR errors. Expanding OR over binary arithmetic gives

    delta_next = p XOR ((1-c)*q) XOR ((1-b)*r) XOR (q*r).

This follows by subtracting (in XOR) the two Rule30 outputs and using OR(b,c)=b XOR c XOR(b*c). If the source is currently healed, q=0, the update reduces to

    delta_next = p XOR ((1-b)*r).

At a shared black centre only the left error matters. At a shared white centre the two incoming errors cancel when equal, including when both are1. Thus zero observed source error is not evidence that either incoming channel is clean. The nonlinear q*r term also prevents treating the full damage process as autonomous Rule90. This identity applies to synchronous propagation after the isolated pulse; it is not the rule for a newly raced update.

**Hand derivation for G113's finite cylinder.** Initial sites-6..6 are0011110010000; only source0 races right on tick1. In the shrinking source cone, predicted ideal/noisy rows are:

| Tick | Sites | Ideal | Noisy |
|---|---|---|---|
| 3 | -3..3 | 1010101 | 1111011 |
| 4 | -2..2 | 01010 | 00001 |
| 5 | -1..1 | 101 | 001 |

At tick4 the white source has no error, but both immediate neighbours have errors1. These cancel, producing another healed source at tick5. At tick5 the source is still white and only its left neighbour has error1, so the source error returns on tick6. The observed two-tick recovery was parity cancellation, not elimination of the surrounding discrepancy. Rows in this table are restricted to the shrinking cone, not claims about the entire damage set.

**DP0-DP2 preregistered NOT RUN.** DP0:all64 ideal-neighbourhood/error triples must satisfy the expanded identity, independently compared with the literal Rule30 truth table. DP1:forward the specified cylinder through tick6 and require the three hand-derived rows above; check the expanded difference identity at every synchronous update, and require incoming source errors(1,1) at tick4 and(1,0) at tick5. DP2, unexpected guard:shared black centre with p=q=0,r=1 has next error0, whereas autonomous Rule90 would give1; the autonomous-damage counterfactual must fail. Publish before execution. No new production table or repeated-race job.

**DP0-DP2 outcome (2026-10-06 21:16 BST).** Ran after proof, predictions and instrument publication through9e09890. DP0 PASS:all64 local ideal/error triples satisfy the expanded Boolean difference identity. DP1 PASS:all three hand-derived cone rows agree; at tick4 the white source receives errors(1,1), cancelling to0, and at tick5 it receives(1,0), returning error1. The identity also matches literal-table differences at every synchronous node. DP2 PASS:the shared-black guard blocks right error, refuting autonomous Rule90 damage evolution. The result explains this pulse witness; it supplies no stochastic closure or survival rate. Independent review pending.

*Second reader's note on G114 (Local, 2026-10-06; chat L071).* Correct. With $\mathrm{OR}(x, y) = x \oplus y \oplus xy$
the difference of the two Rule 30 outputs is $p \oplus (1-c)q \oplus (1-b)r \oplus qr$, and at a healed source two
equal incoming errors cancel when the centre is white. Checked (`rule30_audit_g99_g100.py`, S16): the identity on all
64 triples against the truth table; the cylinder's rows at ticks 3, 4 and 5 exactly as in the table, with incoming
source errors $(1, 1)$ at tick 4 and $(1, 0)$ at tick 5; and the black-centre guard (0, where autonomous Rule 90
would give 1). "Healed" at the source was parity cancellation, not the disappearance of damage.

### G.GPT115. injection memory plus one lag still misses deeper history (second-read by Local, 2026-10-06)

### G115. Injection memory plus one lag still misses deeper observed pulse history (2026-10-06)

**Status:** exact finite-cone candidate-state counterexample; independent review pending. IS0-IS2 predictions and instrument published through114a83c before execution. This tests Local L070's injection-history repair in the isolated-pulse ensemble, not repeated random races.

Use the same8192 fair initial cone words as G113. Define F=E1, the actual injection indicator, and candidate X5=(F,K4,K5). Every positive injection happens at the fixed pulse time1, so adding its time or age at tick5 adds no further information. Refine each candidate bin by the full observed history H=(K0,...,K5). The instrument uses two independently checked update formulations and exact integer cross products.

The parent A={F=1,K4=(0,0),K5=(0,0)} has80 compatible words and40 next errors, so P(E6=1|A)=1/2. Its full-history child

    H=((0,0),(0,1),(0,0),(0,1),(0,0),(0,0))

has20 compatible words and no next error, so P(E6=1|H)=0. Both bins have positive probability in the infinite fair ensemble because only13 initial bits are needed. Thus the next-error law retains observed-past information not supplied by injection occurrence/time and one lag. The specified state is not sufficient at tick5, even allowing the known pulse phase.

A concrete word in the zero child is0101100010000 on-6..6. G113's independently checked positive cylinder0011110010000 lies in the same candidate parent and produces next error1. The zero conditional rate for the entire full-history child is certified by exhaustive enumeration, not inferred from the single zero word. Independent review remains required; no repeated-race or all-finite-orders conclusion follows.

**IS0-IS2 outcomes (2026-10-06 21:19 BST).** IS0 PASS:all8192 words, F=E3=001 indicator, bin totals and unaugmented0/896 versus40/1872 witness. IS1's blind split prediction HELD:24 unequal full-prefix refinements among18 candidate parents and112 full histories. A second witness has parent(F,K4,K5)=(1,(0,0),(0,1)), next-error24/48, while its zero-success full-history child has0/12. IS2's unexpected shallow-equality prediction HELD:zero unequal refinements when only K3 is added to X5. This is a controlled false reassurance: the K3-only diagnostic holds at this horizon while the complete observed past splits. No held finite diagnostic is promoted to closure. The unaugmented one-lag closure counterfactual remains refuted.

### G.GPT116. the fourth pulse error is gated parity (second-read by Local, 2026-10-06)

### G116. The fourth pulse error is gated parity of three earlier ideal samples (2026-10-06)

**Status:** local algebraic proof; PE0-PE2 pass, independent review pending. Follows G109's echo, G114's Boolean damage equation and G115's shallow/full-history distinction. This is the fixed isolated-pulse model, not a law for repeated races or a physical jerk measurement.

Write F=E1 for actual injection and I_t for ideal source0. With common initial input and only a source right race on tick1, followed by synchronous ticks,

    E4=F*(I1 XOR I2 XOR I3).

If F=0 there is no changed cell and all later errors vanish. If F=1, initial sites0..2 are001. Ideal first-tick sites1 and2 are therefore both1. At tick2 the ideal right sites1,2 have values1 XOR I1 and0 respectively; the ideal source is I2=1 XOR z1(-1). G109's second-tick errors are delta2(-1)=I2,delta2(0)=0,delta2(1)=1, with no error outside sites-1..1.

Using G114's synchronous damage equation on tick3:delta3(-1)=(1-I2)*I2=0; delta3(0)=I2 XOR(1-I2)=1; delta3(1)=1 because ideal tick2 site2 is0. Independently the ideal tick3 site1 is I2 XOR(1 XOR I1). Thus at the fourth source update, old errors(left,centre,right) are(0,1,1), and ideal(centre,right) are(I3,I2 XOR1 XOR I1). Flipping both OR inputs changes their OR by1 XOR centre XOR right. Substitution gives E4=I1 XOR I2 XOR I3, proving the gated identity.

**Conditional fair law.** Under F=1, the initial negative bits remain independent fair. The ideal samples I1,I2,I3 successively contain fresh initial bits-1,-2,-3 as XOR pivots. Conditioning on injection therefore leaves those three samples iid fair. Consequently P(E4=1|F=1,I2,I3)=1/2, but further specifying I1 makes E4 deterministic. Unconditionally P(E4=1)=1/16. This gives an exact example of older observed information disappearing under a shallow average; it does not by itself prove the later G115 candidate failure, which has its own complete-history certificate.

**PE0-PE2 preregistered NOT RUN.** Enumerate512 initial words on-4..4 through four ticks, with independent literal-table/XOR-OR updates. PE0 must reproduce F=001 and E1,E2,E3=F,0,F. PE1 must verify E4=F*(I1 XOR I2 XOR I3),64 injected words and448 noninjections, and32 fourth errors. PE2, the unexpected shallow-average guard, requires eight ideal triples(I1,I2,I3), each appearing8 times among injections. For each fixed I2,I3 there must be8 fourth errors among16 histories, whereas each I1 refinement is deterministic. The counterfactual that F and the last two ideal samples determine E4 must fail in every such bin. These are512 local cone controls, not a rerun of the8192-word production-history audit. Publish before execution.

**PE0-PE2 outcome (2026-10-06 21:25 BST).** Executed after proof, predictions and instrument publication through241fb49. PASS:all512 initial cone words;64 injections and448 noninjections;source echo and the gated parity E4=F*(I1 XOR I2 XOR I3). Exactly32 fourth errors. Among injections every one of the eight ideal triples appears8 times. Each fixed I2,I3 bin has8 errors among16 histories, while adding I1 gives deterministic parity. The unexpected shallow-average guard refutes last-two-ideal-sample sufficiency in all four such bins. Independent review pending;no repeated-race or physical-derivative law follows.

*Second reader's note on G115 and G116 (Local, 2026-10-06; chat L072).* Both correct; G115 refutes my L070
suggestion, as it should be recorded. Checked (`rule30_audit_g99_g100.py`, S17) over all 8,192 pulse words with my
own evolution: the candidate parent $(1, (0,0), (0,0))$ has 80 words with 40 next errors and its full-history child
20 with none; 24 of the 112 full-history children differ from their parent's rate (18 parents), and adding only
$K_3$ splits nothing, the controlled false reassurance. G116's parity law $E_4 = F(I_1 \oplus I_2 \oplus I_3)$ holds
on every word; on these 8,192 words (16 times G116's 512) there are 1,024 injections, 512 fourth errors, and each
$(I_2, I_3)$ bin among injections has 256 histories with 128 errors, so the last two samples give a coin and $I_1$
decides it. (My first comparison used G116's unscaled counts and failed for that reason only.)

### G.GPT117. a hidden right-tail bit enters the fifth error (second-read by Local, 2026-10-06)

### G117. A hidden right-tail bit first enters the fifth pulse-error law (2026-10-06)

**Status:** local algebraic kernel and fair-ensemble law proposed; FT0-FT2 preregistered NOT RUN, independent review pending. Continues G116 in the fixed isolated-pulse model. There are no further races after tick1; conditional uncertainty here comes from initial bits outside the observed source history, not fresh noise.

Condition on injection F=1, so old sites0..2 are001. Put D=x(3)*(x(4) OR x(5)), for the common initial row x. Write a=I1,b=I2,c=I3,d=I4 and define

    H=a XOR b XOR c,
    L=1 XOR ((1-b)*(d XOR (c OR (1 XOR a XOR b)))),
    R=b XOR D,
    C=c XOR ((1 XOR a XOR b) OR (1 XOR a XOR D)).

Then the fifth source error is

    E5=L XOR ((1-C)*H) XOR ((1-d)*R) XOR (H*R).

**Derivation.** G116 gives source delta4=H and ideal tick3 site1=1 XOR a XOR b. Direct ideal updates give z2(3)=D and z3(2)=1 XOR a XOR D: when x3=0 the relevant OR is1, and when x3=1 its complement is x4 OR x5. Hence ideal tick4 site1 is C. Tick3 right errors at sites1,2 are both1, so G114 gives delta4(1)=z3(1) XOR z3(2)=R. On the left delta3(-1)=0,delta3(0)=1 and delta3(-2)=(1-z2(-2))*b. If b=1, z3(-1)=1 XOR z2(-2), so delta4(-1)=1; if b=0 it is1 XOR z3(-1). Since z3(-1)=d XOR(c OR (1 XOR a XOR b)), these cases give L. Substituting the tick4 errors(L,H,R) and ideal centre/right(d,C) in G114's damage law proves the formula. For F=0 the copies remain identical, so E5=0.

**Exact fair conditional kernel.** After fixing F=1, D has probability3/8 of being1. Given the entire nonnegative initial tail, a,b,c,d each contain a successive independent fair negative pivot; their joint distribution is uniform on16 words independent of that tail. Thus D is independent of the ideal prefix. The paired observed history through tick4 contains no further tail information: I0=0, E1,E2,E3=1,0,1 and E4=H are fixed by that prefix.

Let g(a,b,c,d,D) denote the displayed formula. Then the exact next-error probability given the full paired observed past is (5/8)*g(a,b,c,d,0)+(3/8)*g(a,b,c,d,1). Algebra gives8 contexts that depend on D,6 deterministic-error contexts and2 deterministic-zero contexts. Of the8 mixed contexts,6 have rate3/8 and2 have rate5/8. Therefore

    P(E5=1)=19/256,
    H(E5 | K0,...,K4)=h2(3/8)/16,

where h2 is binary entropy in bits. For a=b, D affects the error exactly when d=c; for a differs from b, exactly when d=0, giving the eight mixed contexts. The unconditional entropy weights each injected prefix by1/128 and all noninjected histories by0. This is an exact short-horizon conditional uncertainty, not an entropy rate or a Markov-order theorem.

**FT0-FT2 preregistered NOT RUN.** Enumerate2048 initial words on-5..5 through tick5. Independently compare literal-table and XOR/OR updates; FT0 must recover F,0,F and G116's fourth parity. FT1 must verify the fifth-error formula,256 injections,1792 noninjections and152 fifth errors. Each injected ideal quadruple must occur16 times with D=1 in6 and D=0 in10. The16 conditional error counts must have histogram{0:2,16:6,6:6,10:2}. FT2, unexpected no-fresh-noise guard:prefix a=b=c=d=0 has E5=D, hence6 errors in16 otherwise identical observed histories. Print one initial word for each D value and verify identical paired histories through4 with different E5. The counterfactual that the full observed past determines the next error after racing stops must fail. Publish before execution; no repeated-race production job.

**FT0-FT2 outcome (2026-10-06 21:30 BST).** Executed after proof, predictions and instrument publication through6c4792e. PASS:2048 initial cone words,256 injections and152 fifth errors. All16 injected ideal prefixes occur16 times each, with D=1 in6 histories and D=0 in10. The conditional error-count histogram is exactly{0:2,16:6,6:6,10:2}, verifying the displayed kernel and entropy weighting. Independent literal-table/XOR-OR updates agree. The unexpected guard gives initial words00110001000 (D0,E5=0) and00110001101 (D1,E5=1) on-5..5, both with identical paired history((0,0),(0,1),(0,0),(0,1),(0,0)) through tick4. No fresh flags are present after the pulse. Independent review pending;these controls do not turn the conditional entropy into an entropy rate.


*Second reader's note on G117 (Local, 2026-10-06; chat L073).* Correct. Checked (`rule30_audit_g99_g100.py`, S18)
over all 2,048 pulse words on sites $-5$ to 5 with my own evolution: the fifth error equals the stated formula in
$(I_1, I_2, I_3, I_4, D)$ on every injected word and is 0 otherwise; 256 injections and 152 fifth errors
($19/256$); every injected ideal quadruple occurs 16 times with $D = 1$ in 6; the per-quadruple error counts have
histogram $\{0{:}\,2, 6{:}\,6, 10{:}\,2, 16{:}\,6\}$, so eight contexts are mixed (six at $3/8$, two at $5/8$) and the
conditional entropy is $8 \cdot \tfrac{1}{128} \cdot h_2(3/8) = h_2(3/8)/16$; the all-zero quadruple has $E_5 = D$.
After racing stops, the observed past no longer determines the next error: a hidden bit to the right decides it.

### G.GPT118. exact mutual information of six pulse samples (second-read by Local, 2026-10-06)

### G118. Exact unconditional mutual information of the first six pulse samples (2026-10-06)

**Status:** short-horizon entropy proof; JI0-JI2 preregistered NOT RUN, independent review pending. Complements G108's conditional coupling law using G116-G117. It is a pulse ensemble calculation, not an entropy rate, prize result or repeated-race law.

Let A=(I0,...,I5),B=(J0,...,J5) be ideal and noisy source traces in the fair initial-row isolated-pulse model. Both are iid fair by G97/G107, so H(A)=H(B)=6 bits. XOR-error history E is in bijection with B once A is given. Write h2(p) for binary entropy, with0*log2(0)=0. Then

    H(A,B)=6+h2(1/4)/2+h2(3/8)/16,
    MI(A;B)=6-h2(1/4)/2-h2(3/8)/16.

**Proof.** F=E1 is the001 injection indicator. Given I0=1, F=0; given I0=0, F is Bernoulli1/4. Fixing the nonnegative initial tail leaves the ideal samples I1..I5 successively triangular in five fresh negative initial bits, hence jointly uniform. Thus conditioning on those ideal samples adds no information about F or the hidden D of G117 beyond I0. In particular H(F|A)=h2(1/4)/2, not h2(1/8).

If F=0 the whole error history is zero. If F=1, its first five entries are0,1,0,1,I1 XOR I2 XOR I3. Only E5 remains to be specified. G117's independent D has rate3/8 even when the fifth ideal sample is observed: the fifth fresh negative pivot preserves the uniform conditional likelihood of the ideal prefix for every fixed right tail. Eight of the16 ideal quadruples have a D-dependent E5, each with entropy h2(3/8). Since P(F=1)=1/8, H(E5|F,A)=h2(3/8)/16. The first error identifies F, so entropy chain rule gives H(E|A)=H(F|A)+H(E5|F,A). Add H(A)=6 and subtract from H(A)+H(B)=12 to prove the formulas.

This gives unconditional MI strictly below6 bits, whereas G108 gives6 bits conditional on the nonpivot environment for the same horizon. In that conditional model the environment fixes the hidden inputs and the two traces are causally bijective. This is a statement about these two information quantities in this model, not a general monotonicity rule for conditional mutual information.

**Exact joint-count predictions.** On the2048 equally weighted11-bit initial words, each of64 ideal traces has32 preimages. For the32 traces with I0=1 all32 give one paired trace. For I0=0,24 are noninjections. For16 of those ideal traces the eight injected words give one deterministic-error trace; for the other16 they split5 and3 according to D. Thus the joint-support count histogram is{32:32,24:32,8:16,5:16,3:16}, with112 distinct pairs.

**JI0-JI2 preregistered NOT RUN.** JI0 checks all2048 words with independent literal-table/XOR-OR updates; both marginal histograms must contain64 traces32 times each and the joint histogram must match the prediction above. JI1 compares entropy from the integer count spectrum with the displayed binary-entropy expression and MI identity, tolerance1e-12 only for floating logarithms. JI2, unexpected conditioning guard:each ideal trace beginning0 must have8 injections among32, each beginning1 none; replacing H(F|A) by unconditional h2(1/8) must overestimate joint entropy. Publish before execution. No production job or asymptotic inference.

**JI0-JI2 outcome (2026-10-06 21:36 BST).** Executed after proof, predictions and instrument publication through8ced884. PASS:2048 words;both marginal histograms have64 traces32 times each. The112 joint pairs have exactly the predicted count histogram{32:32,24:32,8:16,5:16,3:16}. Entropy from those counts agrees with the closed expression within1e-12:joint6.465291187412 bits,mutual information5.534708812588 bits. The unexpected conditioning guard passes:every ideal trace starting0 has8 injections in32 histories;those starting1 have none. Substituting unconditional h2(1/8) overestimates joint entropy,refuting injection-independence. Independent review pending;no entropy-rate or repeated-race conclusion.


*Second reader's note on G118 (Local, 2026-10-06; chat L074).* Correct, including the two points GPT asked me to
challenge. The conditioning is right: injection needs $x(0) = 0$, $x(1) = 0$, $x(2) = 1$, so it is impossible when
$I_0 = 1$ and has probability $1/4$ when $I_0 = 0$; and $I_1$ to $I_5$ each carry a fresh pivot from the left, so for
every fixed right tail they are uniform and say nothing more about $F$ or the hidden $D$. Checked
(`rule30_audit_g99_g100.py`, S19) over all 2,048 words: both marginals 64 traces of 32; joint histogram
$\{32{:}\,32, 24{:}\,32, 8{:}\,16, 5{:}\,16, 3{:}\,16\}$ with 112 pairs; 8 injections in every ideal trace beginning 0
and none in those beginning 1; and the entropies from the counts match both formulas to $10^{-12}$, giving
$\mathrm{MI}(A; B) = 5.5347$ bits.

### G.GPT119. shared fresh pivots turn error uncertainty into information increments (second-read by Local, 2026-10-06)

### G119. Shared fresh pivots turn error uncertainty into mutual-information increments (2026-10-06)

**Status:** general right-reading fair-ensemble identity; GF0-GF2 preregistered NOT RUN, independent review pending. Uses G107-G108's fresh-pivot property and ordinary entropy chain rule, not a new general information theorem.

Start ideal and right-reading noisy Rule30 copies from the same infinite iid fair row. The entire terminating right-reading flag field is independent of the initial row; temporal flag dependence is allowed. Observe both on a predetermined nonrightward path p_t. Put K_t=(I_t,J_t),E_t=I_t XOR J_t and M_t=MI(I0..It;J0..Jt), with empty-prefix M_-1=0. Then

    M_t-M_(t-1)=1-H(E_t | K0,...,K_(t-1)),
    M_T=(T+1)-sum_(t=0..T) H(E_t | paired past).

Each increment is between0 and1 bit;M_0=1 since the initial copies agree. No limit or entropy rate is asserted.

**Proof of the required conditional freshness.** The initial pivot index L_t=p_t-t strictly decreases. By G107-G108, both samples have form X_(L_t) XOR u_t and X_(L_t) XOR v_t, where u_t,v_t depend only on initial bits strictly to the right of L_t and the independent flag field. All prior paired samples also depend only on those higher initial bits and flags. The shared pivot remains a fresh fair bit even after conditioning on the whole paired past and E_t=u_t XOR v_t. Hence each current marginal sample is fair independent of that conditioned information, and

    H(I_t,J_t | paired past)=H(I_t,E_t | paired past)=1+H(E_t | paired past).

Each separate trace is iid fair, so extending each marginal prefix adds1 bit of entropy. Extending the joint prefix adds the displayed1+conditional-error term. Subtracting joint entropy from the sum of marginal entropies proves the increment identity;telescoping proves the total. This argument establishes unconditional information growth, unlike G108's result conditioned on the entire environment.

The relevant property is a common unused pivot relative to the paired history, not merely two iid marginal traces. Adaptive paths, reused finite-ring pivots, state-dependent flags and nonterminating right chains are outside the proof. Biased initial rows do not supply the fair-bit baseline. This gives no closure of the error history and no asymptotic information rate.

**GF0-GF2 preregistered NOT RUN.** Use two independent small finite controls, not another Rule30 production run. GF0-GF1 positive control:three fair pivots X0,X1,X2 and two fair hidden bits U,V, R=U*V;I=(X0,X1,X2),J=(X0,X1 XOR R,X2 XOR(R*X0)). All32 histories have equal weight. Predict both marginal prefixes uniform,MI prefixes1,2-h2(1/4),3-h2(1/4),and next-error conditional entropies0,h2(1/4),0. Independently compare integer joint/marginal entropy spectra with conditional-error groups, tolerance1e-12 only for logs.

GF2, unexpected cross-copy-reuse guard:all8 fair triples X,Y,Z with I=(X,Y,Z),J=(X,Z,Y). Both marginals are iid and initial samples agree, butMI prefixes are1,1,3;the last increment is2 while the last error is known from the paired past. The formula would predict1 there and must fail. This counterexample refutes extending the identity from marginal iid laws alone. Publish before execution. It is a scope control, not a Rule30 counterexample.

**GF0-GF2 outcome (2026-10-06 21:40 BST).** Executed after proof,predictions and instrument publication through439744b. PASS:the32 positive histories have uniform marginal prefixes,MI1,2-h2(1/4),3-h2(1/4),and conditional-error entropies0,h2(1/4),0;the increment identity agrees within1e-12. The unexpected8-history reuse guard has MI1,1,3 and zero final error uncertainty,yet final MI increment2. It refutes extending the identity from marginal iid laws alone. The general Rule30 result rests on the written common-fresh-pivot proof,not on extrapolating toy cases. Independent review verified by Local L075;no limit or rate inferred from the controls.

*Second reader's note on G119 (Local, 2026-10-06; chat L075).* Correct, including the measurability step GPT asked me
to challenge: every earlier paired sample and the current $u_t, v_t$ depend only on initial bits strictly right of
$L_t$ (earlier pivots lie further right), so the shared pivot is fresh even given the whole paired past and $E_t$,
and the joint increment is $1 + H(E_t \mid \text{paired past})$. Checked (`rule30_audit_g99_g100.py`, S20) on the real
pulse traces from all 2,048 words: $M_t = (t + 1) - \sum_{s \le t} H(E_s \mid \text{paired past})$ for every
$t \le 5$, every quantity from exact counts, ending at $M_5 = 5.534709$, G118's value; the positive toy gives
$1$, $2 - h_2(1/4)$, $3 - h_2(1/4)$; the cross-copy reuse guard gives $1, 1, 3$ with its last error known, so the
identity would wrongly give 2 there, as stated.

### G.GPT120. an observed rare injection bounds later information loss (second-read by Local, 2026-10-06)

### G120. Observed rare injection bounds later pulse information loss (2026-10-06)

**Status:** pulse-model entropy bound; RB0-RB2 preregistered NOT RUN, independent review pending. Corollary of G119, conditional on its scope. The asymptotic statement is a liminf bound, not existence or evaluation of an information-rate limit. It does not concern repeated races or the selected Rule30 seed.

In the common-input fair isolated-pulse model, F=E1 is observable from K1 and P(F=1)=1/8. If F=0 the pulse changes no cell, and subsequent synchronous evolution preserves equality of the entire configurations. For t>=2 the paired past contains F. Thus

    H(E_t | paired past)=P(F=1)*H(E_t | paired past,F=1)<=1/8.

Here the second conditional entropy is averaged over histories within the injected branch. Dependence between F and the initial source bit causes no problem:the weights in conditional entropy average to the unconditional branch probabilities. The bound uses both F's measurability from the past and the zero-error noninjected branch.

G119 therefore gives

    M_t-M_(t-1)>=7/8 for t>=2,
    M_T>=2-h2(1/4)/2+(7/8)*(T-1) for T>=1.

Using G118's exact six-sample result gives the sharper finite bound

    M_T>=6-h2(1/4)/2-h2(3/8)/16+(7/8)*(T-5) for T>=5.

Consequently liminf_(T->infinity) M_T/(T+1)>=7/8. Mutual information per sample is also at most1 by the marginal entropy bound. This does not prove the normalized sequence converges, determine its limit, or control the injected branch's damage lifetime. In particular,the seven-eighths lower bound partly comes from histories in which the pulse never injects;it is not a claim that active damage preserves seven-eighths of its information.

**Why observability is essential.** If F is not determined by the conditioned past, separating the branches also costs uncertainty about F. An event with small probability alone does not justify H(error|past)<=P(F=1). The scope guard below keeps the fresh-pivot information identity but hides F,so it must violate the rare-event budget rather than the identity itself.

**RB0-RB2 preregistered NOT RUN.** Positive control:64 equal-weight fair histories of X0,X1,X2,U,V,Q, with F=(1-X0)*(1-U)*V. Set I=(X0,X1,X2),J=(X0,X1 XOR F,X2 XOR(F*Q)). RB0 checks uniform marginals,P(F1)=1/8,and F observable after the first error. RB1 must give final conditional-error entropy1/8 and final MI increment7/8,showing the budget can be tight. Independently compare grouped error entropy with joint/marginal count spectra.

RB2, unexpected hidden-event guard:32 fair histories of X0,X1,U,V,Q with the same F,but I=(X0,X1),J=(X0,X1 XOR(F*Q)). The initial paired past does not reveal F. Predict next-error entropy h2(1/8)/2>1/8 and MI increment1-h2(1/8)/2<7/8,while both marginals remain iid and the fresh-pivot identity holds. The counterfactual that injection probability alone supplies the budget must fail. Tolerance1e-12 only for logarithms;publish before execution. No production scaling run.

**RB0-RB2 outcome (2026-10-06 21:48 BST).** Executed after9f37d68 published the proof,predictions and instrument. PASS:64 equality-case histories give observed F,probability1/8,error entropy1/8 and MI increment7/8. The32 hidden-F histories give error entropy0.271782221600 and increment0.728217778400,violating the rare-probability-only budget while satisfying the fresh-pivot identity. Independent grouped-error and joint-count calculations agree within1e-12. These toy controls check the scope;the all-time pulse bound follows from the written conditional-entropy proof. Reviewed by Local L076.

*Second reader's note on G120 (Local, 2026-10-06; chat L076).* Correct, and the weighting GPT asked me to challenge
holds: conditional entropy averages over pasts with their unconditional weights, the noninjected pasts carry zero
error entropy once $F$ is observed, so the total is at most $P(F = 1) = 1/8$ whatever the dependence of $F$ on $I_0$.
The interpretation is also right: much of the $7/8$ comes from histories that were never damaged. Checked
(`rule30_audit_g99_g100.py`, S21): on the real pulse traces the error entropies for $t = 2$ to 5 are 0, 0, 0 and
$h_2(3/8)/16 = 0.0597$, all below $1/8$; the positive toy is tight at $1/8$; the hidden-event guard gives
$h_2(1/8)/2 = 0.2718 > 1/8$ while G119's identity still holds there.

### G.GPT121. finite-predecessor descent reduces to roots (second-read by Local, 2026-10-06)

### G121. Finite-predecessor descent reduces counterexamples to roots, not bounded width (2026-10-06)

**Status:** paper proof and failed bridge, independent review pending. Responds to Cloud CL005's minimal-counterexample suggestion. No experiment or production run. This does not prove period-two exclusion or a prize result.

Let F be synchronous Rule30 on the infinite zero background. For a nonzero finite configuration x let [L,R] be its smallest support interval and w=R-L+1 its span, including internal zeroes. Its image has support endpoints exactly L-1,R+1:the outside adjacent triples are001 and100,both producing1,and all further outside triples are000. Therefore span(F(x))=w+2. This is an endpoint theorem,not a monotonicity theorem for the number of black cells.

F is injective on finite configurations. If two finite rows differ,let k be their rightmost differing site. Their values at k+1,k+2 agree,so their next values at k+1 differ:the left argument enters by XOR. Hence a finite row has at most one finite predecessor. If y has span w and a nonzero finite predecessor,that predecessor has span w-2. Iterating finite predecessors therefore terminates in a unique finite root r with no finite predecessor,and y=F^a(r) for a unique nonnegative age a. Its span is span(r)+2a. This is descent of ancestry,not descent along forward time.

Suppose a finite row is a counterexample to eventual-period-two exclusion at a fixed spatial column. Its finite predecessor,if present,is also a counterexample at that same column:the traces differ only by one initial time step. Thus every counterexample descends to a root counterexample,and a globally minimum-span counterexample must be a root. No phase assumption is needed because eventual alternation tolerates a time shift. Conversely,a root counterexample's forward images remain counterexamples. This gives an exact reduction to roots,without asserting any root is a counterexample.

**Where the bridge fails,for all widths.** Normalize support endpoints to0 and w-1,so for w>=2 there are2^(w-2) finite words. For w>=4 the images of normalized span-(w-2) words give exactly2^(w-4) distinct normalized span-w words,by endpoint growth and finite injectivity. Exactly one quarter have finite predecessors;the other three quarters,3*2^(w-4),are roots. For w=3 the sole image is111 from1;101 is a root. The span-one and span-two words are roots. In particular roots exist at every width. The predecessor reduction supplies no upper bound on a minimal counterexample's width and no induction step that covers the roots. The selected single-black-cell seed is already a root.

**Unexpected scope check,by hand.** The counterfactual "left permutivity gives a finite predecessor for every finite row" fails already on a single black cell:every nonzero finite image has span at least3,and the zero row maps to zero. Yet every finite output block has a compatible longer input block by right-to-left inversion (G104);compactness gives global predecessors. Such predecessors of this root must have infinite support. So full-shift surjectivity cannot supply the missing finite descent. This distinction is standard cellular-automaton background:see Jarkko Kari's [Cellular Automata tutorial](https://users.utu.fi/jkari/wp-content/uploads/sites/1251/2023/12/CAintro.pdf),slides89-100,on finite injectivity versus finite surjectivity and infinite predecessors. No novelty claim for finite injectivity;the present application identifies the precise failure of this proposed bridge.

**Next proof obligation.** A minimal-counterexample argument needs a different transformation that preserves eventual alternation while shrinking a root,or a theorem excluding every root. Removing an endpoint by hand has no established trace-preservation property:its causal cone eventually reaches any fixed observation column,so finite propagation alone guarantees no forever equality. The root count is not evidence of period-two survival. Ordinary inverse-time descent alone is closed as a complete proof route;other shrinking transformations remain open.

### G.GPT122. canonical ancestors gain black and period-three tails (second-read by Local, 2026-10-06)

### G122. A finite root's canonical ancestors acquire black and period-three left tails (2026-10-06)

**Status:** symbolic inverse-map proof; independent review pending. Extends G121's failed descent by identifying the class it leaves. No new experiment. Does not exclude eventual temporal alternation at a fixed column.

Call a row right-quiescent when it is zero at all sufficiently large spatial indices;it may be infinite to the left. Rule30 is bijective on this class. To invert a right-quiescent output y,choose B beyond its rightmost possible nonzero cell,set x_B=x_(B+1)=0,and recursively solve

    x_(i-1)=y_i XOR (x_i OR x_(i+1))

for every i<=B. Set all x_i=0 for i>B. This produces a right-quiescent row satisfying F(x)=y at every site. Uniqueness follows from G121's rightmost-difference argument,which still applies to two rows bounded on the right even when both have infinite left tails. Taking a larger B only adds zero recursion steps,so the inverse is independent of the cutoff. No claim of bijectivity on the whole two-sided full shift is made.

For a finite nonzero output y,its canonical predecessor has an eventually constant left tail. Indeed below y's leftmost nonzero site,the recursion has y_i=0. On adjacent inverse bits (u,v)=(x_i,x_(i+1)),the descending spatial map is

    M0(u,v)=(u OR v,u).

Its complete graph is00->00,01->10,10->11,11->11. Every state reaches00 or11 within two steps. Thus the inverse is either finite (left tail0) or has left tail1. A G121 root has no finite predecessor,so its unique right-quiescent predecessor must be eventually black on the left. This is a necessity and sufficiency test for root status;an infinite black tail is not extra input freedom once the right-quiescent inverse is fixed.

Take one more canonical predecessor of such a root. In its far left recursion the output is now constantly1,so

    M1(u,v)=(1 XOR (u OR v),u).

The complete graph is00->10->01->00 and11->01. Every state joins the three-cycle within one step. Consequently the second canonical predecessor has a far-left spatial tail of least period3,with repeating bits001 up to phase. The tail is spatial,not a period-three source trace. As a direct independent local check,the cyclic triples of001 are100,001,010,and Rule30 maps each to1;the constant1 row maps to0. This verifies the far-left forward sequence001->1->0 without using the inverse-state graph. These two hand checks are exact truth-table evaluations,not an extrapolated probe.

**Unexpected scope check.** The counterfactual "constant output tails force constant predecessor tails" is refuted by M1's three-cycle. Even a uniquely selected predecessor may increase the tail's spatial period. More generally,if a right-quiescent output has an eventually periodic left tail of period p,the inverse tail is eventually periodic with a period at most4p:combine the4 pair states with the p output phases to obtain a deterministic finite graph. Its eventual cycle has length k*p for some1<=k<=4;the inverse bit period divides that length. No uniform bound over repeated inversions follows.

**Bridge interpretation.** G121's backward shrinking stays within finite seeds only until its root. Continuing the unique inverse is possible,but it leaves that class through an infinite black tail and then a spatial period-three tail. Thus lack of a finite predecessor is not lack of a global predecessor. An eventual temporal wall would persist under these time shifts;the resulting periodic tails do not by themselves contradict it. A useful next theorem would need a compatibility obstruction between that wall and the canonical ancestor tails,not an assumption that ancestor tails stay finite or constant. This is a reformulation and an identified missing implication,not a prize proof. Background distinction and prior art as in G121 (Kari's tutorial);no novelty claim for the inverse transducer itself.

*Second reader's note on G121 and G122 (Local, 2026-10-06; chat L077).* Both correct. The endpoint triples 001 and
100 give span $w + 2$; the rightmost difference survives one step, so finite rows have at most one finite
predecessor; counterexamples descend to roots; and the inverse maps $M_0$ and $M_1$ have the stated graphs. Checked
(`rule30_audit_g99_g100.py`, S22): span growth and distinct images for every word to span 14; exactly $2^{w-4}$ of
the $2^{w-2}$ normalized words have a finite predecessor for $w = 4$ to 16, with 101 a root at $w = 3$; the single
cell's canonical predecessor has an all-black left tail and its own predecessor a tail $\ldots100100100$, each mapping
back exactly. My view on the reformulation (chat L077): an ancestor's future is the root's future shifted, and the
tails exist exactly when the word is a root, so a wall-against-tails obstruction is the same as excluding roots,
which G121 already reduced to; I do not see a new lever in it.

### G.GPT123. canonical ancestor tails have unbounded periods (second-read by Local, 2026-10-06)

### G123. Canonical ancestor tails of every nonzero finite root have unbounded spatial periods (2026-10-06)

**Status:** all-depth paper theorem conditional on G121-G122's proved inverse construction;independent review pending. No measurement or new experiment. This concerns spatial periods in backward ancestors,not the source's temporal period or a prize solution.

Let r be a nonzero finite root,and let x_n be its unique right-quiescent nth canonical predecessor,with x_0=r. G122 inductively supplies an eventually periodic far-left tail for each x_n. Let C_n be the unique two-sided periodic extension of that tail,with least spatial period p_n. C_0 is the zero row,C_1 the one row,and p_0=p_1=1,p_2=3.

The extensions obey F(C_n)=C_(n-1). To see this,far enough left the local update on x_n reads only its periodic tail,so F(C_n) agrees there with the tail of F(x_n)=x_(n-1). Both extended rows are periodic;agreement on a left half-line forces agreement at every site. Thus F^n(C_n)=0 and F^(n-1)(C_n)=1. Zero is absorbing,so C_n first reaches zero after exactly n steps. This is exact for all n,not a horizon fit.

All n+1 rows C_n,F(C_n),...,F^n(C_n) are distinct. A repeat before hitting zero would put the deterministic orbit on a cycle,which cannot later hit absorbing zero for the first time. Every row in this trajectory has spatial period dividing p_n,because a translation-commuting cellular automaton preserves any input period. They therefore occupy n+1 distinct labeled configurations on a p_n-cell ring,which has 2^p_n configurations. Consequently

    n+1 <= 2^p_n,
    p_n >= ceil(log2(n+1)).

In particular the ancestor-tail spatial periods are unbounded for every nonzero finite root. Moreover p_(n-1) divides p_n:the output's least period divides any period of its input. Combined with G122,p_(n-1)<=p_n<=4*p_(n-1). The divisibility chain must have infinitely many strict increases. No linear growth law,exact multiplier sequence,or bounded gaps between increases is established.

**Independent perspective and unexpected check.** The same bound is the finite-state absorbing-orbit bound:a p-bit deterministic system cannot have a first-hit transient of length>=2^p. This checks the indexing without the inverse graphs. The nonzero-root hypothesis is essential:the zero row has all canonical ancestors zero,all periods 1,and first-hit time 0. Treating every finite row as a root,or every inverse depth as a first-hit time,would incorrectly apply the bound to this counterexample. For a non-root finite row,first descend to its root as in G121;the finite ancestry contributes a time offset,so the statement above is anchored at the root.

**What this bridges and what it does not.** This crosses from the finite inverse transducer to an all-depth necessity:uniformly bounded ancestor-tail periods are impossible. The natural candidate ranking is the first-hit depth on each periodic ring;it decreases under forward evolution,but its state space changes with p_n. It is not a ranking for the forced0101 walk and provides no contradiction to a temporal wall. The missing theorem remains a link from an eventual0101 wall to bounded ancestor-tail periods,or another incompatible restriction. Since unbounded tail periods occur for every nonzero finite root,the property alone cannot distinguish a hypothetical period-two counterexample from other seeds. The counting here is a finite-state pigeonhole proof,not a survivor-decay assumption. The finite-state pigeonhole bound is elementary. G105 supplies related absorbing-zero ring examples, not this ancestor-depth claim. No novelty claim for the general orbit bound.

### G.GPT124. zero-reaching periodic rows have periods 1 or 3 times a power of two (second-read by Local, 2026-10-06)

### G124. Periodic Rule 30 rows that eventually reach zero have periods 1 or three times a power of two (2026-10-06)

**Status:** symbolic inverse-transducer theorem; independent review pending. No new experiment. This classifies least spatial periods of individual periodic rows that reach the all-zero row; it does not claim that Rule 30 is a nilpotent cellular automaton. It supplies no temporal-wall exclusion.

Let y be a spatially periodic output with least period p, and let x be any spatially periodic predecessor. Translation invariance implies p divides x's least period q. Inverting from right to left uses G122's pair maps

    M0(u,v)=(u OR v,u),
    M1(u,v)=(1 XOR (u OR v),u).

If y is nonconstant, p>=2 and one output symbol in a period is zero. Choose the period cut so the first descending symbol is that zero. The first map sends all four pair states into T={00,10,11}. The following map sends T to at most two states, regardless of the next symbol:

    M0(T)={00,11},
    M1(T)={10,01}.

Every later map preserves the upper bound on image size. Thus the p-symbol return map has image size at most two and every cycle has length at most two. The pair states of a periodic predecessor lie on a return-map cycle: there is no transient when the row repeats in both spatial directions. If the cycle length is k, the reconstructed bits have period dividing k*p. Combining k<=2 with p dividing q gives

    q=p or q=2*p.

This statement permits several predecessors and does not assume a unique periodic predecessor. The cut is just a phase choice, not a restriction on the row.

For constant output zero, M0 has only fixed cycles 00 and11, so its periodic predecessors are exactly the constant zero and constant one rows. For constant output one, M1 has the unique three-cycle 00->10->01->00, with11 entering it; its periodic predecessors are exactly the three phases of 001. Their least spatial period is 3. These constants are the exceptions to the nonconstant-output period rule.

**Classification.** Take a periodic row reaching zero, and use its finite first-hit trajectory backward from zero. If it is already zero or is the one row, its least period is 1. Otherwise the step before one has period 3. Every earlier row is nonconstant (a constant could reach zero in at most one step), so successive backward least periods are preserved or doubled. The original least period is therefore 3*2^k for some integer k>=0.

**Existence at every allowed period.** G123's canonical tails of any nonzero finite root give periodic rows C_n that first hit zero at time n. Starting with p_2=3, the present return-map bound forces each subsequent period to stay fixed or double. G123 proves these periods unbounded. Hence every value3*2^k is attained somewhere in that ancestry, without skipping a power. Together with the zero and one rows, this proves the possible least periods are exactly1 and3*2^k. The depth at which each doubling occurs is not bounded here beyond G123's finite-state estimate.

**Independent local check and unexpected guard, by hand.** The cyclic words give the exact forward trajectory

    001010 -> 011011 -> 010010 -> 111111 -> 000000.

Each arrow is checked by applying the literal triples of Rule 30 at the six labeled sites. The first word has least period 6, the next two period 3, and the last two period 1. This shows the doubled-period case is real, and that nilpotent-to-zero periodic rows need not have prime-power spatial periods. Separately,001->111 refutes applying q<=2*p to the constant-one output. These are independent finite algebra checks, not a run or a horizon extrapolation.

**Scope and prior art.** Existing-record checks found G105's zero preimages and G122's inverse maps, but no recorded classification of all possible least periods of zero-reaching periodic rows. Targeted prior-art searches for Rule 30 periodic preimages and zero-reaching/nilpotent periodic configurations did not locate a suitable primary source for this exact claim; novelty remains unresolved. The proof above is self-contained. Every nonzero root has these ancestor-period doublings, so they are not a distinguishing feature of a hypothetical eventual 0101 trace. This theorem is a structural result about the periodic zero basin, not evidence that the open temporal-wall bridge is complete.

*Second reader's note on G123 and G124 (Local, 2026-10-06; chat L078).* Both correct, including the steps GPT asked
me to challenge. Periodic rows agreeing on a half-line agree everywhere, so $F(C_n) = C_{n-1}$ and the first hit of
zero is exactly at $n$; the return map's first zero sends the four pair states into $\{00, 10, 11\}$, and both $M_0$ and
$M_1$ then reduce that set to two states, so cycles have length at most 2 and the period keeps or doubles; doubling
one step at a time cannot skip a power. Checked (`rule30_audit_g99_g100.py`, S23): every zero-reaching state on
rings of 1 to 16 cells has least period 1 or $3 \cdot 2^k$, with 3, 6 and 12 all present at 12 cells; the single
cell's canonical tails have periods $1, 3, 3, 6, 6, 6, 6, 6, 6, 12, 12, 12$ for $n = 1$ to 12, with the divisibility
chain, the pigeonhole bound and $F(C_n) = C_{n-1}$; the period-6 trajectory checks cell by cell. (Descriptive: the
doublings come at depths 2, 4 and 10, far earlier than the pigeonhole bound forces.)

### G.GPT125. sideways periodic points are recurrent ring states (second-read by Local, 2026-10-06)

### G125. Sideways periodic points correspond exactly to recurrent Rule 30 ring states (2026-10-06)

**Status:** symbolic correspondence using G22; independent review pending. Distinct lane: CONSTELLATION row 5, sideways dynamics. No computation or new ring census. The ordinary finite-state orbit argument is standard; no novelty claim.

On two bi-infinite binary time tracks define S a(t)=a(t+1) and the sideways map

    H(a,b)=(S a XOR(a OR b),a).

This is G22's map F, renamed H here to distinguish it from ordinary forward-time Rule 30, R. Fix m>=1. Then Fix(H^m) is in bijection with the recurrent states of R on a labeled m-cell ring. A recurrent state means a row lying on a temporal cycle, not a transient that will eventually enter one. Every track pair in Fix(H^m) is temporally periodic, with a common period no larger than 2^m-1. The same correspondence applies to periodic points of G22's induced ternary map.

**From a sideways periodic point to a ring.** Successive H iterates give neighboring columns extending leftward: H(a,b)=(c,a) is exactly the inverse-column equation c(t)=a(t+1) XOR(a(t) OR b(t)). If H^m(a,b)=(a,b), these columns close into a spatial period-m spacetime diagram. At each integer time t its labeled ring row u_t satisfies R(u_t)=u_(t+1), for all positive and negative t. Thus it is a bi-infinite orbit of a finite deterministic map.

Every row of such a bi-infinite finite-state orbit is recurrent. There is a uniform maximum transient length among the finitely many ring states. If u_0 were transient, u_(-N) would have to remain transient for at least N steps before reaching u_0, which is impossible for larger N. Recurrent ring states lie on cycles, and on that recurrent set R is a permutation. Therefore the temporal history is periodic in both directions and uniquely determined by u_0. There are at most 2^m-1 recurrent states:the all-one ring row maps to zero and is not itself recurrent. This gives the stated common temporal-period bound, not necessarily the least period of either individual track.

**From a recurrent ring state to a sideways periodic point.** A recurrent row has a unique bi-infinite temporal orbit on its cycle. Periodically extend each ring row to the whole spatial line and take the time tracks at sites 0 and 1 as (a,b). All inverse-column equations hold, so applying H m times shifts left by one spatial circumference and recovers (a,b). The two constructions are inverse:two adjacent tracks and their inverse-column iterates recover the labeled ring row, while a recurrent ring row determines its entire past and future. Labels and the distinguished time 0 are retained;this is a bijection with states, not merely with cycles modulo time or spatial rotation. Periods dividing m are allowed.

**Ternary scope.** Every H-periodic point lies in H's one-step image, since it is the image of H^(m-1) of itself. G22's conjugacy on that image therefore transfers this exact periodic-point description to the ternary induced dynamics. It does not transfer arbitrary transient two-track states into the ternary domain, nor assert a dynamical-entropy formula or classify all iterated images.

**Independent hand check and unexpected transient guard.** On a two-cell Rule 30 ring the four rows obey00->00,11->00,01->01,10->10. Hence there are exactly three recurrent states. The corresponding sideways pairs are the constant tracks(0,0),(0,1),(1,0);H fixes the first and exchanges the last two, so Fix(H^2) has exactly three points. On a one-cell ring only zero is recurrent and H has only the zero fixed point. The counterfactual "any periodic ring row supplies a bi-infinite sideways orbit" fails on the spatially and temporally constant proposed pair(1,1):it is transient, H(1,1)=(0,1), and its purported forward-time all-one row maps to zero. Having a spatially periodic initial row supplies a forward orbit, not automatically a bi-infinite orbit through that row. These are literal truth-table checks, not a simulation extrapolation.

**Result for the open lane.** Classification of sideways periodic points reduces to the recurrent-state sets of finite rings. No nonperiodic time track can lie on a finite sideways cycle. A fixed wall or finite-seed condition is absent here, so this does not exclude a 0101 wall, bound its information cost, or solve a prize. Existing-record checks found G22/G24's image and forbidden-word theorems and the ring census, but not this explicit labeled correspondence. The next useful obligation is an invariant for nonperiodic sideways orbits or iterated images; another census would not establish it.

*Second reader's note on G125 (Local, 2026-10-06; chat L079).* Correct, including the two steps GPT asked me to
challenge: a bi-infinite orbit of a finite deterministic map can contain no transient state, and two adjacent tracks
rebuild every column through the inverse-column equation, so the correspondence is injective. Checked
(`rule30_audit_g99_g100.py`, S24): for $m = 1$ to 10 every recurrent ring state gives a track pair that $H^m$
returns exactly, with distinct states giving distinct pairs; and, independently of the correspondence, a brute-force
count of $H^m$-fixed pairs among all temporally periodic track pairs (period $L$, the lcm of the ring's cycle
lengths) equals the recurrent count for $m = 1$ to 4: 1, 3, 1 and 11, the last over all $2^{16}$ period-8 pairs. The
guard $H(1,1) = (0,1)$ checks.

### G.GPT126. the ternary sideways image is six forbidden words, with a local section (second-read by Local, 2026-10-06)

### G126. The ternary sideways map has an exact six-word image and a local predecessor section (2026-10-06)

**Status:** symbolic all-sequence image theorem using G22/G24; reviewed by Local L080. No experiment or production run. Coordinates are the bi-infinite time axis of the formal sideways map; no fixed wall or finite-seed condition is imposed.

Let H(a,b)=(S a XOR(a OR b),a) and let T be G22's induced ternary map on H's one-step image. Then T's image is exactly the set Y of bi-infinite ternary sequences avoiding

    100, 101, 112, 0210, 0211, 0202.

Thus the image is a shift of finite type, not merely a language with the two necessary exclusions of G24. There is a shift-commuting local map R from Y to the full ternary shift with T(R(z))=z. It uses only z(t-1),z(t),z(t+1). In particular every p-periodic target in Y has a p-periodic predecessor (its least period may divide p). This is not a claim that R(z) lies in Y or that T is onto its own image.

**Reduction to binary predecessor constraints.** Decode a target z as (D,C), where C(t)=[z(t)=2], and D(t)=z(t) when C(t)=0, otherwise D(t)=1-C(t+1). A ternary predecessor is represented by a compatible pair(C,A). Its image must satisfy

    D(t)=C(t+1) XOR(C(t) OR A(t)).

When C(t)=0 this forces A(t)=e(t)=D(t) XOR C(t+1). When C(t)=1 the target equation is automatic and A(t) is free. G22's image compatibility for(C,A) requires, at every site with A(t)=1,

    C(t)=1-A(t+1).

Hence a forced 1 at a zero site of C requires the next A bit to be 1; a chosen 1 at a one site of C requires the next A bit to be 0.

**Necessity of the six exclusions.** Two consecutive zero sites of C cannot have e(t)=1,e(t+1)=0. In target symbols this is exactly100 or101 when C(t+2)=0, and112 when C(t+2)=1. Also a zero-one-zero block of C with e(t)=1 forces A(t+1)=1 and then A(t+2)=0. Its first target symbol is0, its middle symbol2, and its final forced e(t+2) must be0. The three ways to violate this last condition are0210,0211,0202. Each exclusion therefore holds for arbitrary predecessors, periodic or not.

**Sufficiency and local section.** For any target avoiding these words, define

    A(t)=D(t) XOR C(t+1)                    if C(t)=0,
    A(t)=[z(t-1)=0]                       if C(t)=1.

All target equations hold. Check compatibility only where A(t)=1. If C(t)=0 and C(t+1)=0, the forbidden triples ensure the next forced bit is1. If C(t)=0 and C(t+1)=1, the equation e(t)=1 means z(t)=0, so the prescribed next bit is1. If C(t)=1, its chosen bit is1 only after target symbol0. When C(t+1)=1 the next chosen bit is0 because its preceding symbol is2. When C(t+1)=0, avoidance of the forbidden quadruples makes its forced bit0. These exhaust the cases and prove compatibility. Encode(C,A) as R(z)(t)=2 when A(t)=1, otherwise C(t). G22's recoding then gives T(R(z))=z. This construction is valid on the whole bi-infinite sequence; no boundary completion or compactness assumption is hidden in it.

**Independent hand certificate and unexpected gap check.** For the repeating target0220, the formulas give C=0110,D=0010,A=1100 and predecessor code2210. A further binary predecessor B=0011 satisfies, by direct XOR/OR evaluation,

    H(1100,0011)=(0110,1100),
    H(0110,1100)=(0010,0110).

The last pair codes0220, independently certifying a target in the second image. Conversely the repeating target112 avoids100 and101, but forces A(t)=1,A(t+1)=0 at two successive zero sites of C. It has no predecessor under T. This refutes the counterfactual that G24's two old exclusions already describe the image exactly. These are finite algebra checks supporting the case proof, not a computational extrapolation.

**The image still has positive shift entropy.** Arbitrary aligned concatenations of blocks00 and22 belong to Y:there are no ones, and every constant run has length at least two, so0202 cannot occur. Distinct binary choices of n blocks give 2^n distinct words of length2n. The word-count entropy of Y is therefore at least1/2 bit per time-axis site. No exact entropy or limit-set entropy is evaluated. A local predecessor section does not imply its repeated application remains inside Y; deeper images remain unclassified.

**Record and scope.** This advances CONSTELLATION row 5's exact image description using the existing sideways recurrence and G22's compatibility theorem. G24's periodic missing-target conclusion remains correct and is strengthened by a complete image test. No claim of external novelty; the construction is a project-local symbolic derivation. An eventual0101 wall or finite forced left row would need additional constraints. The positive entropy lower bound prevents mistaking this finite image refinement for a collapse to a finite collection of traces or a prize proof.

*Second reader's note on G126 (Local, 2026-10-06; chat L080).* Correct, including the sufficiency case GPT asked me to
challenge: a chosen 1 at a $C = 1$ site follows a target 0, and the next bit is 0 either because its own preceding
symbol is 2 (when $C(t+1) = 1$) or because the forbidden quadruples force it (when $C(t+1) = 0$). Checked
(`rule30_audit_g99_g100.py`, S25) with $T$ rebuilt from G22's definitions: no predecessor window of length $k + 2$
maps onto any of the six forbidden words (a local test, no periodicity); for every period $p \le 8$ the periodic
targets with a $p$-periodic predecessor are exactly the periodic words avoiding the six; the local section satisfies
$T(R(z)) = z$ on all of them; $2210 \mapsto 0220$, and 112 has no predecessor. (My first run failed at $p = 2$ through
my own short unrolling, which missed 0202 inside 2020; G126 was right.)

### G.GPT127. no shift-commuting section stays in the image; strict loss at one more layer (second-read by Local, 2026-10-06)

### G127. No shift-commuting predecessor section stays in the ternary image (2026-10-06)

**Status:** symbolic section obstruction and strict deeper-image loss; NS0/NS2 pass and NS1 prediction held. Uses G126's image theorem; independent review pending. The preregistered distinction between a section failure and strict loss is resolved by the separate certificate below. Further image layers remain open.

For the ternary sideways map T, let Y be the sequences avoiding100,101,112,0210,0211,0202. The period-two points of Y are exactly the repeating words00,11,12,21,22. Literal evaluation of G22's rule gives

    00 -> 00,
    11 -> 22,
    22 -> 11,
    12 -> 22,
    21 -> 22.

Thus the target(12)^infinity belongs to Y but has no period-two predecessor in Y. Any shift-commuting section Q:Y->Y of T would preserve being fixed by the two-step shift. Its value at this target would be such a predecessor, a contradiction. There is no shift-commuting section into Y, regardless of continuity; in particular there is no local one. G126's section into the full ternary shift is unaffected.

**Unexpected guard: a deeper predecessor nevertheless exists.** The repeating word0102 lies in Y and T(0102)=1212. It is a period-four predecessor of the period-two target. G126's canonical section instead returns(01)^infinity, outside Y. Hence failure of the canonical choice, and even failure of every period-preserving section, cannot establish absence of all image-constrained predecessors. These statements separate a constructive local inverse from mere onto-ness.

**NS0-NS2 preregistration.** A bounded search will address a different implication:does some target in Y have a finite prefix with no possible predecessor from Y? NS0 compares all27 radius-two ternary cases with an independent binary-pair decoding. NS2 checks the five period-two targets, the period-four lift0102, and the canonical-section failure;this is the identified unexpected check.

NS1 considers prefix lengths n=1..7, in increasing order. Enumerate all3^(n+2) full-shift precursor blocks, compute their length-n outputs, and retain as possible Y precursors every block avoiding the six forbidden words internally. This is a superset of globally admissible precursor blocks, so a missing output certifies impossibility for nonperiodic predecessors too. Restrict target witnesses to words w whose cyclic repetition lies in Y, to certify target extendability. Stop at the first length and lexicographically first missing target prefix. Blind prediction:a witness occurs by length7. If none occurs, record that prediction as refuted;do not infer stabilization.

For a witness, retain the complete set of its full-shift precursor blocks in memory and the spectrum of forbidden factors excluding them. Independently count every full-shift precursor via a de Bruijn-pair dynamic program using the binary-decoded rule, and require exact agreement with the enumerated count. No sampling or floating arithmetic. A full blocked-prefix certificate would prove T(Y) is a proper subset of Y;the absence of a short certificate would be finite evidence only. Counterfactual:the period-two failure alone proves strict deeper-image loss;NS2 must refute it. Publish the predictions and instrument before execution. This small structural certificate search duplicates no ring census or Local computational job.

**NS0-NS2 outcome (2026-10-06 22:20 BST).** Executed after81fb4fd published the proof,predictions and instrument. NS0 PASS on all27 triple cases;NS2 PASS on the period-two section obstruction and period-four lift. NS1 HELD at n=6,so the blind witness-by7 prediction held. The search checked9,828 full-shift precursor blocks across n=1..6. The first missing periodic target prefix is022000. All six full-shift precursor blocks are

    22100000, 22100001, 22100002,
    22100022, 22100220, 22100221.

Each contains100. The independently decoded de Bruijn path count is also6. No floating arithmetic or sampling. Minimality is asserted only within the preregistered search of cyclically admissible target words through length6,not all possible global target classes.

**All-sequence obstruction,independently derived from binary constraints.** In any target starting02200d with d in{0,1}, C begins011000 and D begins00100 (the sixth D need not be used). The predecessor constraints force A(0)=1 because D(0)=0,C(1)=1. Compatibility at site0 forces A(1)=1,and compatibility at site1 then forces A(2)=0. The target equations at sites3 and4 force A(3)=A(4)=0. Encoding(C,A) forces precursor prefix22100,which contains100. This eliminates every global ternary predecessor lying in Y,periodic or not,without relying on enumerated boundary choices. Thus T(Y) forbids022000 and022001 in addition to Y's old exclusions.

The cyclic target(022000)^infinity belongs to Y: it consists of zero runs of length4 and two runs of length2,with no ones and no0202. Hence it has a full-shift predecessor by G126,but no predecessor from Y. Therefore T(Y) is a proper subset of Y,or equivalently T^2(full ternary shift) is strictly smaller than T(full ternary shift). G126's explicit predecessor section cannot establish stabilization,and now stabilization at this layer is refuted by a complete finite obstruction. This proves strict loss at one further layer,not strict loss at every depth or zero entropy of the limit set. Further iterated images and any wall-specific consequence remain open. Independent review pending.

### G.GPT128. the sideways limit set has every binary trace as a factor (second-read by Local, 2026-10-06)

### G128. The sideways limit set has every binary temporal trace as a factor (2026-10-06)

**Status:** all-depth compactness proof using G4.4/G22; independently verified by Local L081. No experiment or probability extrapolation. The entropy here is word-count entropy under time-axis shift, not dynamical entropy under sideways iteration and not the entropy of a fixed-wall fibre.

Let X be all pairs of bi-infinite binary time tracks, H(a,b)=(S a XOR(a OR b),a), and

    Lambda_H = intersection_(n>=0) H^n(X).

Let Lambda_T be the corresponding limit set of G22's ternary map. Then Lambda_H is exactly the set of adjacent-column pairs occurring in full Rule 30 spacetime diagrams on integer space and integer time. Projection onto either track is onto the full binary shift. Under G22's ternary recoding, the one-block map pi(z)(t)=[z(t)=2] maps Lambda_T onto the full binary shift. Consequently every ternary iterated image and the limit set itself have word-count entropy at least1 bit per time-axis site. Lambda_T contains nonperiodic time-axis sequences. No fixed finite initial seed is asserted to realize them.

**Spacetime equivalence.** A full spacetime diagram supplies predecessors of an adjacent pair at every sideways depth: shifting to two columns farther right and applying H recovers the chosen pair. Hence that pair lies in every H^n(X).

Conversely, membership in H^n(X) supplies a right extension of n columns satisfying the inverse-column equations at every time. All left columns are determined by forward H iterates. For each n there is therefore a spacetime strip extending arbitrarily far left and n columns right. Fill its remaining sites arbitrarily. The full diagram space {0,1}^{Z x Z} is compact. A convergent subsequence, or the equivalent finite-intersection argument, preserves the given two columns and every local rule equation:each finite spatial region is covered once n is large enough. The resulting diagram obeys Rule 30 at every integer space-time site. No coherent choice of predecessors at successive finite depths was assumed.

**Every binary trace is realizable in this unrestricted class.** Fix any desired bi-infinite binary column b(t). For each N, prescribe b on times-N through N. Start a row at time-N. Iterated left-permutivity gives the sample after k ticks as its initial bit at site-k XOR a function of higher initial bits. Fix the initial positive-index bits and solve successively for sites0,-1,...,-2N, as in G4.4. This realizes the desired finite window;all other initial bits may be zero. Evolve forward on the whole spatial line, and fill times earlier than-N arbitrarily.

Compactness now gives a full spacetime diagram whose source column is b(t) at every integer time:each prescribed value and each local rule equation is eventually enforced in these diagrams. The finite-window seeds may differ with N and grow in width. Their compact limit need not have finite spatial support at any chosen time. Spatial translation makes the same argument apply to either track of an adjacent pair. Thus both projections of Lambda_H are onto the full binary shift.

**Ternary factor and entropy bound.** H's one-step image I is invariant under H, and G22 conjugates H restricted to I with T. The nested images starting from I have the same intersection as those starting from X, because H^n(I)=H^(n+1)(X). Therefore the conjugacy maps Lambda_H onto Lambda_T. In the recoding, the second binary track is exactly[z(t)=2], so its surjectivity is a one-block factor statement. Every length-N binary word is the pi-image of a length-N ternary word in Lambda_T;distinct binary words require distinct ternary words. There are at least2^N such words, proving the entropy lower bound. Every finite iterate contains Lambda_T and inherits it. If b is nonperiodic, any preimage under pi is nonperiodic, proving nonperiodic sequences exist in the limit set. This says nothing about recurrence or periodicity under T itself.

**Unexpected fixed-wall guard, checked algebraically.** The binary trace b=1^infinity is realized in Lambda_H by the pair(a,b)=(0^infinity,1^infinity), from the fixed spatial checkerboard:Rule 30 preserves cyclic01. But the pair(a,b)=((01)^infinity,1^infinity) is not even in H(X). G22 compatibility would force a(t)=1-b(t+1)=0 at every t, which the proposed a violates. Therefore the unrestricted factor is not onto after fixing an alternating wall. It cannot refute the thin fixed-wall channel bounds or supply a finite-seed counterexample. This is the identified unexpected check.

**Implication for the active route.** G127's strict image loss is genuine, yet unrestricted image pruning cannot collapse this limit set to finitely many traces or below1 bit of shift entropy. A prize-relevant invariant must use the wall, finite support, or another restriction absent from the full spacetime class. The all-depth factor is a structural obstruction to a proposed global-collapse route,not a theorem that a particular seed is random. The construction is the standard triangular trace argument plus compactness;no novelty claim for those ingredients.

*Second reader's note on G127 and G128 (Local, 2026-10-06; chat L081).* Both correct, including the steps GPT asked
me to challenge. G127: the forced bits at sites 0 to 4 follow from G126's target and compatibility equations, and
$(022000)^\infty$ is admissible in $Y$ (no ones, runs of length at least two, no 0202). G128: the finite-window step is
the usual left-permutive solving, the compactness steps are standard, and the transfer through G22's conjugacy uses
$H^n(I) = H^{n+1}(X)$. Checked (`rule30_audit_g99_g100.py`, S26): $T$ on the period-two points
$00, 11, 22, 12, 21$ gives $00, 22, 11, 22, 22$; 0102 lies in $Y$ and maps to 1212; the precursor blocks of 022000 are
exactly the six listed, all beginning 22100, and every precursor of 022001 also begins 22100; $(022000)^\infty$ lies in
$Y$; every binary word of length up to 11 is the site-0 trace of a finite initial row; the checkerboard is fixed;
and a brute force over period-2 and period-4 inputs finds no $H$-preimage of (alternating, all ones). (A first
version of that last check was vacuous and was replaced before recording.)

### G.GPT129. the finite-left wall fibre is compact at each radius (second-read by Local, 2026-10-06)

### G129. The finite-left wall fibre is a compact constraint class at each fixed radius (2026-10-06)

**Status and target.** Symbolic bridge from G128 to the finite-left boundary problem; independently verified by Local L083. No experiment or novelty claim for compactness. Existing record: G27.2 excludes periodic companions, G53 identifies the wall-visible bits, and G128 characterizes unrestricted spacetime pairs. The target is an exact finite-left constraint that does not assume companion periodicity. The counterfactual is that a compact limit of witnesses with growing support must retain finite support. One unexpected check below separates counting full itineraries from counting their time factors.

Use one-sided time t>=0. Let X+ be all pairs of binary future tracks and H(a,b)=(S a XOR (a OR b),a), with S advancing time. Let Lambda+ be the intersection of H^n(X+) over n>=0. The same strip-compactness proof as G128 identifies Lambda+ exactly with adjacent-column pairs in full-space, forward-time Rule 30 diagrams: right extensions of every finite width have a coherent compact limit, and all left columns are uniquely given by H iterates. This does not require any periodicity or a past before time zero.

Fix any prescribed wall tau and integer L>=0. Define

    B(L,tau) = { (a,b) in Lambda+ : a=tau,
                 first_track(H^d(a,b))(0)=0 for every d>L }.

**Exact boundary interpretation.** B(L,tau) consists precisely of the wall/right-neighbor pairs of full forward diagrams whose initial left row is zero at all sites i<-L. There is no bound on the initial right row. In one direction, H^d recovers column -d, so the displayed conditions are its initial zero tail. In the other direction, Lambda+ supplies a full forward diagram with this pair; every possible extension has the same forced left columns and therefore the specified initial zero tail. This is a left-support condition, not a finite global seed condition.

For fixed L, B(L,tau) is compact: Lambda+ is an intersection of nested compact images; fixing a track is closed; and each displayed initial-cell equation is a closed cylinder condition depending on only finitely many input cells. Their countable intersection is closed. All finite-left pairs form the union of these classes over L. That union cannot be treated as one fixed-radius compact class merely because each member is compact.

**Finite-box alternative.** B(L,tau) is empty if and only if some finite rectangle already forbids a forward diagram with that wall and that left radius. Specifically, take sites -N through N and times 0 through N, fix the wall samples, fix initial cells -N through -L-1 to zero when N>L, and enforce every Rule 30 equation whose three input sites and output lie in the rectangle. Leave the right initial row unrestricted. If every N has an assignment, extend each assignment arbitrarily outside its rectangle and use compactness. Every fixed wall sample, local equation and initial left-zero condition is eventually enforced, so the limit is a full forward diagram in the class. The converse follows by restriction. Thus a failure at fixed L has a finite Boolean certificate in principle; no uniform certificate size or effective search bound is supplied. Certificates for a few radii do not prove emptiness for every radius.

**Visible itineraries have a finite cardinality bound at fixed L.** Observe b only at white wall times. There are at most 2^L such complete visible itineraries in B(L,tau). Choose the L initial left bits. With tau imposed as a boundary, forward evolution of sites i<0 is deterministic. Write its nearest-left trace as ell(t). At a white time, the wall equation forces b(t)=tau(t+1) XOR ell(t). At a black time, it instead requires ell(t)=1-tau(t+1), independently of b(t); failure rejects that left seed. Thus each left seed permits at most one whole visible itinerary, even when hidden black-phase bits or full right extensions are not unique. This is a boundary-determinism count, not an entropy or finite-state closure theorem.

**Counterfactual and unexpected check.** Initial rows with ones at -L,...,-1 and zeros elsewhere converge, as L increases, to an infinite left black tail. Their ordinary forward Rule 30 diagrams consequently have a compact limit with infinite initial left support. This general support guard does not claim those rows share one prescribed alternating wall; it shows why varying-radius compactness alone does not retain the required boundary condition. Separately, a single sequence formed by concatenating every finite binary word has one prefix of each length but all 2^n time factors of length n. Therefore the 2^L whole-itinerary bound gives no zero factor-entropy conclusion. This is the identified unexpected check, reused from G64's distinction; it is not a Rule 30 realization claim.

**Remaining bridge.** To exclude a finite seed realizing an alternating wall, it would suffice to prove B(L,tau) empty for every L; that stronger finite-left assertion is not proved here. If a class is nonempty, full finite-right support remains an additional obligation. The next invariant must address an aperiodic companion inside these explicit classes, rather than unrestricted Lambda+ or a periodic closure. No new channel census is requested.

*Second reader's note on G129 (Local, 2026-10-06; chat L083).* Correct. With the wall fixed, the left half evolves
deterministically from its initial left row, the white-time wall equation forces each visible bit and the black-time
one constrains only the left trace, so a seed determines at most one visible itinerary. Two connections. First, the
record's exact zero-run records next to $0101\ldots$ (RULE30-PRIZE.md §8.36, §8.37; PERIOD-TWO.md Q6: no left half is
zero from any depth up to 85, for every column 1) are finite certificates of exactly G129's kind: they show
$B(L, 0101\ldots)$ empty for every $L$ up to about 84, and Conjecture LR (or the doubling conjecture) for every column
1 would make it empty for every $L$. Second, an independent direct check (`rule30_audit_g99_g100.py`, S27): every
left seed of radius $L \le 10$ evolved against the alternating wall, in either phase, violates the black-time equation
within 18 ticks, so those classes are empty with very small boxes (death times 1, 7, 7, 7, 7, 9, 9, 9, 17, 17, 17 for
the phase starting white).

### G.GPT130. a fixed right tail gives a unique left seed for every wall (second-read by Local, 2026-10-06)

### G130. Fixing the initial right tail gives a unique left seed for every wall trace (2026-10-06)

**Status and purpose.** Exact coordinate reduction of G4.4's triangular inversion; independently verified by Local L084. This is not a new left-permutivity theorem or a solution of the wall problem. G129 leaves finite right support as an additional constraint. Here the target is to identify exactly what that constraint can and cannot exclude. No experiment. Counterfactual: finite initial right support alone restricts possible temporal walls, or exact finite-prefix realizations guarantee a finite left seed. The delayed single-cell example below independently rejects the latter implication at a fixed right tail.

Fix the initial values r_i at all sites i>=0. For any desired one-sided wall tau with tau(0)=r_0, there is exactly one initial left word u=(x_-1,x_-2,...) whose full forward Rule 30 evolution has x_0(t)=tau(t) for every t>=0. The map from u to the future trace (tau(1),tau(2),...) is a homeomorphism of binary sequence spaces. No periodicity premise is used.

**Proof.** G4.4 gives, for each n>=1,

    x_0(n) = x_-n(0) XOR P_n(x_(-n+1)(0),...,x_n(0)).

The unique path carrying the leftmost input to the observed output contributes by XOR; all other terms use higher initial indices. Fix r and solve x_-1, then x_-2, and so on, using the prescribed tau(n). Each step has exactly one solution and does not alter earlier samples. These compatible finite assignments define one infinite initial row, and its ordinary forward evolution realizes every sample. Uniqueness follows from the same successive solving. Both directions are continuous: a trace prefix of length N uses only the first N left bits and r_0,...,r_N; conversely those N left bits are determined by that trace prefix and the same finite right data. This is an initial-row/trace coordinate map, not a conjugacy between Rule 30 evolution and a shift on a fixed-tail space, since the initial right tail need not remain fixed after an update.

**Finite-right support is compatible with every wall in isolation.** Set r_0=tau(0) and r_i=0 for all i>0. The construction realizes every tau, including an alternating wall, with this finite initial right tail. Its forced left word may be infinite. Thus no obstruction based only on requiring finite initial right support can exclude a temporal word when arbitrary infinite left support is allowed. This does not assert that a chosen companion from G129 has a finite-right extension.

**Exact finite-global criterion.** For a prescribed tau, let r range over all eventually-zero initial right tails with r_0=tau(0), and write u_r for the uniquely solved left word. A finite global seed realizes tau if and only if at least one u_r is eventually zero. Necessity applies uniqueness to that seed's right tail; sufficiency joins the two finite tails and invokes the construction. Hence the joint boundary problem is a zero-tail question for this canonical family, rather than existence of an unrestricted right extension. This supplies no uniform zero-tail test, search bound, or exclusion theorem. The finite-left condition of G129 still has to hold for the same row.

**Unexpected fixed-tail finite-prefix guard, exact.** Take the initial row x_i=1 for i<0 and x_i=0 for i>=0. Rule 30 sends it in one tick to the single black cell at site 0: triples 111 and 110 give zero on the left, triple 100 gives one at the wall, and triples 000 give zero on the right. Let tau be this row's wall trace: its first sample is zero and its later samples are the single-cell wall trace shifted by one tick. With the fixed initial right tail all zero, this tau has the unique left seed 111..., so no finite left seed with that same right tail realizes it forever.

For every N>=1, truncating that left seed to ones at -N,...,-1 yields a finite seed with the same right tail and exactly the same wall through time N. Its first wrong wall sample is at time N+1: the higher initial indices agree, while the fresh XOR pivot x_(-N-1)(0) differs. Thus arbitrary finite horizons are realized with growing left support even though no fixed finite left seed works for that fixed right tail. No claim is made about alternative right tails for this tau, or about periodicity of the single-cell trace. The check uses both the explicit one-tick truth table and the independent triangular uniqueness mechanism.

**Next obligation.** For an alternating or eventually alternating prescribed wall, prove a property of u_r uniform over finite r that prevents an eventual zero tail, or identify a counterexample. Periodic companion assumptions, unrestricted trace existence and growing finite-prefix realizations do not supply that property. This is a reformulation of the missing proof, not a claim that the canonical words have been classified.

*Second reader's note on G130 (Local, 2026-10-06; chat L084).* Correct. With the right half fixed, each wall sample
brings exactly one fresh left bit by XOR, so the left word is solved uniquely and continuously; a finite seed exists
exactly when some finite right tail gives an eventually-zero left word. Checked (`rule30_audit_g99_g100.py`, S28): 200
random finite right tails with random wall prefixes to length 12 each have exactly one solution at every step, and
its evolution realizes the prefix; $\ldots111|000\ldots$ becomes the single black cell in one tick; truncating its
left seed at radius $N$ keeps the wall through time $N$ and breaks it at $N + 1$, for $N = 1$ to 14. For the
alternating wall, the record's LR records add one fact to this criterion: for every finite right tail, the left word
cannot be zero from any depth up to 85 onward, so an eventually-zero $u_r$, if one exists, starts its zero tail
beyond depth 85.

### G.GPT131. the Sturmian exclusion survives every finite block factor (second-read by Local, 2026-10-06)

### G131. The Sturmian exclusion survives every finite block factor (2026-10-06)

**Status and purpose.** Symbolic extension of RULE30-PRIZE.md section 8.57's Theorem E; independently verified by Local L085. No experiment. The target is the open rotation-code lead in PERIOD-TWO.md question 7, without assuming a periodic companion. The counterfactual is that a finite recoding can remove the early repetitions responsible for Theorem E. The proof retains the exact fixed margin. Prior art: finite block coding and orbit-endpoint rotation partitions are standard; the abstract of Kupsa and Starosta, [On the partitions with Sturmian-like refinements (2015)](https://www.aimsciences.org/article/doi/10.3934/dcds.2015.35.3483), discusses this class and stronger refinement results. Only the abstract was read; no refinement or injectivity theorem is imported. The result below is a corollary of the project's existing repeat obstruction, not a novelty claim about Sturmian coding.

**Theorem.** Let g be any irrational Sturmian sequence, with any phase. Let F be any binary function of a fixed block of width w+1, and set c_s=F(g_s,...,g_(s+w)) for s>=0. If c is column 1's visible sequence beside the alternating Rule 30 wall 0101..., the forced initial left row cannot be eventually zero. No injectivity, nonconstancy or aperiodicity premise is imposed on F.

**Proof.** Section 8.57 Step 0 says finite left support would supply a fixed constant C>=0 such that every repetition c_s=c_(s+q) on a<=s<=b, q>=1, obeys

    b <= 2a+q+C.                         (repeat bound)

Enlarging a possibly negative original C only weakens this necessary bound. Suppose g_s=g_(s+q) on a<=s<=e. If e>=a+w, then c repeats on a<=s<=e-w, so e<=2a+q+C+w. If e<a+w, the same inequality holds automatically. Thus finite left support for c would make every repetition of g obey the repeat bound with constant C+w. The continued-fraction argument in section 8.57 Steps 1 to 4 proves that no irrational Sturmian sequence, at any phase, can obey that bound with any fixed constant. Its proof uses only the repeat bound after Step 0, so it applies here unchanged. This contradiction proves the theorem. The margin is w, not a scale-dependent loss.

A finite block function using shifts m,...,M of a bi-infinite mechanical word is also covered: rephase the Sturmian input by m and take w=M-m. Likewise an eventual finite-block coding is excluded once the clock and coding have both begun: restart at an even physical time beyond that prefix. Finite initial left support remains finite at that time by the light cone.

**Corollary: every finite union of arcs with endpoints on one rotation orbit.** Let 0<alpha<1 be irrational, let f be a binary, right-continuous step function on the circle, and suppose its actual jump endpoints all have the form beta+k_j*alpha modulo one, with finitely many integer k_j. Then c_s=f(theta+s*alpha) is excluded beside 0101... for every theta and every alpha, including bounded-partial-quotient angles. This covers multiple arcs, not just the original interval of length alpha.

Here is a direct finite-block construction, with exact endpoint conventions. Put y=x-beta and g(y)=1 on [1-alpha,1), zero elsewhere. A binary circular step function has an even number of jump endpoints. Over GF(2), form the Laurent polynomial

    Q(z)=sum_j z^(k_j)=(1+z)*P(z).

The divisibility follows from Q(1)=0 after multiplication by a power of z to clear negative exponents. For each nonzero coefficient P_k define

    h(y)= XOR_k g(y-(k+1)*alpha).

The k-th term jumps at k*alpha and (k+1)*alpha, so the jump set of h is precisely Q: interior endpoints cancel modulo two. Thus f(beta+y) and h(y) have the same jumps and differ by one constant bit. Right-continuity makes the equality hold at the endpoints as well. Along the orbit this is a finite XOR block code of one rephased Sturmian word, plus that constant. The theorem therefore applies. A constant f is the empty-code case and is covered too.

**Unexpected degeneracy check.** With irrational 0<alpha<1/2, the standard Sturmian word has no adjacent ones: rotating its one interval [1-alpha,1) by alpha lands in [0,alpha), where the next bit is zero. Hence the finite block factor F(u,v)=u AND v is constantly zero, not Sturmian. The proof still excludes it, directly through the repeat bound. Therefore the argument must use inherited repetitions rather than assert that a finite factor stays Sturmian or invertible. This is the identified independent check.

**Scope and lead status.** The one-orbit-endpoint subclass of question 7 is now covered for all phases and all irrational angles, conditional only on the already proved Theorem E repeat argument. Endpoints on unrelated rotation orbits with bounded partial quotients remain open; a finite recoding of several differently phased Sturmian words does not guarantee a common long repeat. Torus rotations, kicked codes and general aperiodic companions remain outside this result. It is a class exclusion for the finite-left problem, not the prize's exclusion of every companion.

*Second reader's note on G131 (Local, 2026-10-06; chat L085).* Correct. A repetition of $g$ on $[a, e]$ gives one of
the block code on $[a, e - w]$, so Step 0's bound passes to $g$ with constant $C + w$; and Theorem E's Steps 1 to 4
(RULE30-PRIZE.md §8.57) apply that bound only to stretches where the Sturmian word itself repeats with period $q_n$,
so they run unchanged on $g$. The corollary's construction is right: an even number of endpoints gives $Q(1) = 0$, and
each $g(y - (k+1)\alpha)$ codes $[k\alpha, (k+1)\alpha)$, so the XOR has exactly $Q$'s jumps. Checked
(`rule30_audit_g99_g100.py`, S29): for 40 random one-orbit arc unions at two irrational angles, $f(\beta + y) \oplus h(y)$ is constant along 20,000 orbit points; for $\alpha < 1/2$ the Sturmian word has no adjacent ones; block codes
inherit repetitions as stated. This closes the one-orbit part of PERIOD-TWO question 7 for every angle; arcs with
unrelated endpoints and small partial quotients remain open, as G131 says.

### G.GPT132. circle-covering codes and one-character torus codes are excluded (second-read by Local, 2026-10-06)

### G132. Circle-covering codes and one-character torus observables are excluded (2026-10-06)

**Status and target.** Corollary of G131 and G27.2; independently verified with G131 by Local L086. No experiment or novelty claim for integer characters. Target: clarify which multi-orbit and torus codes the finite-block argument already excludes. Counterfactual: a circle covering or additional unobserved torus coordinates automatically evade the Sturmian obstruction. A genuine two-coordinate box below is the unexpected scope check.

**Statement.** Let the torus orbit be x_s=theta+s*omega modulo one in each of d coordinates. Fix an integer vector v and the circle projection

    h_v(x)=sum_j v_j*x_j modulo one,
    beta=h_v(omega).

Observe c_s=psi(h_v(x_s)). If beta is rational, every such deterministic observable psi gives a periodic c and is excluded beside the alternating Rule 30 wall with finite initial left support. If beta is irrational, the same exclusion holds whenever psi is a binary finite-union-of-arcs code whose jump endpoints lie on one beta-rotation orbit. Arbitrary fixed choices at the endpoints are allowed. In both cases no assumption is made about periodicity of the actual right-neighbor trace at its hidden phases.

**Proof.** Integer coefficients make h_v well-defined on the torus. Direct addition gives

    h_v(x_s)=h_v(theta)+s*beta modulo one.

For rational beta with denominator q these projected points repeat every q samples, hence c is periodic. The corresponding nearest-left trace is periodic: at even physical times it is 1-c_s, and at odd times it is one. G27.2 excludes this pair for finite initial left support, independently of the right half.

For irrational beta, the projected observable is exactly a circle rotation code of the class in G131, so its finite-block exclusion applies for every starting phase. If endpoint values differ from the half-open convention used there, each endpoint is visited at most once: two visits would make a nonzero multiple of beta integral. There are finitely many endpoints, so the code eventually agrees with the half-open code. G131's eventual-factor clause therefore preserves the exclusion. This also explains why endpoint exceptions do not create a new companion class.

**Circle coverings give a concrete multi-orbit case.** In dimension one take v=2, irrational alpha as omega, and beta=2*alpha modulo one. Let psi be the standard Sturmian interval [1-beta,1). Then f(x)=psi(2*x modulo one) is a two-arc observable for the original alpha rotation. Its endpoint set is

    {0, 1/2, -alpha, 1/2-alpha} modulo one.

The two original alpha-orbit classes represented by 0 and 1/2 are distinct: an equality 1/2=k*alpha modulo one would make alpha rational for nonzero integer k. Thus f does not have all endpoints on one original orbit, yet its sampled code is Sturmian for the projected angle beta and is excluded. More generally any integer circle covering can be used. This narrows part of the unrelated-endpoint lead; it does not exclude arbitrary unrelated endpoints without such a quotient structure.

**Unexpected genuinely multidimensional guard.** On the two-torus, let f(x,y)=1 when both x and y lie in [0,1/2), zero otherwise. This observable cannot be a function of any single integer character h_(a,b). A function of that character would be invariant under every translation (b*t,-a*t), since the character changes by zero. If b is nonzero, choose x just below 1/2 and y=1/4; a sufficiently small such translation crosses the x boundary while keeping y interior, so f changes. If b=0 and a is nonzero, a vertical translation changes f while leaving the character fixed. The zero character would require f constant. All cases contradict factorization. Therefore this corollary makes no claim about genuinely two-coordinate box codes, nor about the general torus lead. This is a geometric scope check, not a Rule 30 counterexample or a claim that a box code supplies a finite witness.

**Resulting boundary.** The class exclusion includes finite recodings after a one-circle projection, even when the original partition has multiple orbit classes or the underlying motion has several torus coordinates. General partitions using independent coordinates, arbitrary unrelated circle endpoints and kicked observables remain open. No uniform finite-left exclusion or prize solution follows.

*Second reader's note on G132 (Local, 2026-10-06; chat L086).* Correct, with its G131 dependency reviewed above. The
character projection is linear along the orbit; rational $\beta$ gives a periodic code (G27.2), irrational $\beta$ a
rotation code whose endpoints are each visited at most once, so G131's eventual clause applies. Checked
(`rule30_audit_g99_g100.py`, S30): the covering example's jumps sit exactly at $\{0, 1/2, -\alpha, 1/2 - \alpha\}$ for
two irrational angles (with $2\alpha$ on either side of 1), on two distinct $\alpha$-orbits, and its orbit code
equals the $2\alpha$-Sturmian code for 20,000 steps; the box $[0, 1/2)^2$ is not a function of any nonzero character
with coefficients up to 4. PERIOD-TWO question 7's row now records the one-orbit and one-character exclusions.

### G.GPT133. golden-angle codes cannot be rescued by super-geometric kicks (second-read by Local, 2026-10-06)

### G133. Golden-angle codes cannot be rescued by super-geometrically separated kicks (2026-10-06)

**Status and target.** Quantitative extraction from Theorem E's existing continued-fraction proof; independent review pending. No experiment. G131/G132 are verified by Local L085/L086. Target: advance the kicked-code part of PERIOD-TWO question 7 with an aperiodic base, rather than another exact-code reformulation. Counterfactual: zero kick density alone permits arbitrarily long unbroken Sturmian stretches beside a finite left seed. The conservative constants below are not optimized. The dyadic-kick guard prevents an entropy or all-kicks exclusion claim.

Let alpha=(sqrt(5)-1)/2 and g_s=1 when theta+s*alpha modulo one belongs to [1-alpha,1), with any theta. Assume the Rule 30 wall is 0101... from time zero and the initial left row is zero beyond radius L.

**Finite repetition lemma.** For every integer C>=0, a golden-angle Sturmian prefix through index

    N=84*(C+4)

cannot obey the finite repeat bound b<=2a+q+C for every repetition g_s=g_(s+q) on a<=s<=b with b+q<=N. In particular a visible companion cannot agree with such a Sturmian word through index 84*(L+4). The L=0 left seed already fails the first black-time equation; for L>=1 Theorem E Step 0 supplies a repeat constant no larger than L.

**Finite-horizon proof.** Use section 8.57's convergent notation q_n, delta_n, K_n and the first two visit times h,h' to K_n. For a fixed q=q_n, if N>=4q+3C+8, the finite repeat bound alone forces

    h <= q+C+2,
    h' <= 2h+q+C+4.

Indeed, if h>q+C+2, the repetition from 0 through q+C+1 violates the bound; all compared samples lie within N. After the first visit, if h'>2h+q+C+4, the repetition from h+1 through 2h+q+C+3 violates the bound. Its last compared index is at most 4q+3C+7, using the first inequality. These are exactly Theorem E's two visit inequalities, obtained without assuming the second visit was already observed. As in that proof, returns to K_n are at least q_(n+1) apart. Thus

    q_(n+1)-q_n-C-4 <= h(n) <= q_n+C+2.       (visit bounds)

Choose n minimally so q_(n-1)>2C+8. For the golden angle all partial quotients are one. The separation argument of Theorem E Step 4, applied at n and n+1, gives

    h(n+1)=h(n)+q_n,
    h(n+2)=h(n+1)+q_(n+1).

Here its prerequisites are just the visit bounds at n,n+1,n+2 and q_(n-1)>2C+8: the two arcs at successive scales are disjoint and closer than delta_(n-1), and the only possible signed return in the bounded visit-time difference is -q_n. No extra hypothesis about the Rule 30 orbit enters this separation step.

The visit bounds and first identity give h(n)>=q_(n-1)-C-4. The second identity and the upper visit bound at n+2 give h(n+1)<=q_n+C+2. Combining these with the first identity yields q_(n-1)<=2C+6, a contradiction.

All three scales are present in the stated horizon. Minimality and the Fibonacci recurrence imply q_(n-1)<=4C+16 and q_(n+2)<=5q_(n-1)<=20C+80. Therefore

    4q_(n+2)+3C+8 <= 83C+328 < 84*(C+4).

This proves the finite repetition lemma.

**Unbroken stretches at later times.** If the visible companion agrees with a golden-angle Sturmian word from visible index a through b, restart at physical time 2a. The left-zero radius is then at most L+2a by the light cone, and the wall has the same phase. The finite lemma, with this larger radius and arbitrary rephased theta, requires

    b-a < 84*(L+2a+4).

This statement does not require the companion to be periodic or the rest of it to be Sturmian.

**Necessary kick-gap bound.** Suppose c equals a fixed golden-angle Sturmian word except at its actual disagreement indices k_0<k_1<.... Finite support requires infinitely many disagreements, since an eventual exact code is already excluded by G131. Before the first kick, the finite lemma gives k_0<=84*(L+4). Between consecutive kicks use a=k_j+1 and b=k_(j+1)-1. The preceding inequality yields the conservative integer bound

    k_(j+1) <= 169*k_j + 84*L + 505.

Thus schedules with unbounded ratios k_(j+1)/k_j are excluded. In particular, flipping the Sturmian bit at every index 2^(2^j) cannot give a finite-left companion, for any phase and any L. This is an infinite class exclusion from a uniform finite-horizon argument, not evidence extrapolated from measured kicks.

**Unexpected checks and limits.** The Fibonacci sizes 13,21,34,55 at C=0 give a hand check of the three-scale horizon: 4*55+8=228<336. More importantly the zero-density schedule k_j=2^j satisfies the derived kick-gap and first-kick bounds for every L>=1. The theorem therefore does not exclude every sparse schedule or establish positive entropy, positive kick density or realizability of dyadic kicks. It supplies only a necessary upper bound on consecutive disagreement times. The actual measured rational wheel, arbitrary irrational angles, phase-reset kicks and genuinely multidimensional codes are outside this golden-base result. These are the identified independent scope checks.

*Second reader's note on G133 (Local, 2026-10-06; chat L087).* Correct. Both visit inequalities are obtained from
repetitions whose compared samples end by index $4q + 3C + 7$; for the golden angle $q_{n+1} - q_n = q_{n-1}$, and the
two Step 4 identities give $q_{n-1} \le 2C + 6$, against the choice $q_{n-1} > 2C + 8$; $q_{n+2} \le 5 q_{n-1} \le 20C + 80$ puts all three scales inside $84(C + 4)$; restarting at physical time $2a$ gives the kick-gap recursion
$k_{j+1} \le 169 k_j + 84L + 505$. Checked (`rule30_audit_g99_g100.py`, S31): for 30 random phases and $C = 0, 2, 5$
every golden prefix of length $84(C + 4)$ contains a violating repetition; descriptively the latest first violation
over those phases came at prefix lengths 27, 45 and 74, about a tenth of the proved horizons, so the constants could
be tightened; the Fibonacci hand check and the two kick schedules (excluded $2^{2^j}$, admitted $2^j$) check.

### G.GPT134. bounded-type rotation codes need geometrically spaced corrections (second-read by Local, 2026-10-06)

### G134. Bounded-type rotation codes require geometrically spaced corrections (2026-10-06)

**Status and target.** Symbolic extension of G133, independent review pending. No experiment or new numerical prediction. Theorem E and G2.2 supply the continued-fraction facts; G133 supplies the finite comparison deadlines. Target: remove the golden-angle restriction from the sparse-kick exclusion. Counterfactual: bounded partial quotients might still allow corrections with unbounded successive spacing ratios beside a finite left seed. The proof below excludes that possibility. This is a consequence of the existing repetition obstruction, with no general novelty claim.

Let alpha in (0,1) be irrational with every partial quotient a_j<=A, where A>=1 is an integer. For any phase theta let g be its standard half-open Sturmian code. Define

    K_A=8*(A+1)^4+3.

**Finite-prefix theorem.** For every integer C>=0, the prefix of g through index N=K_A*(C+4) cannot satisfy b<=2a+q+C for every repetition g_s=g_(s+q) on a<=s<=b with b+q<=N.

Use Theorem E's convergents q_n, errors delta_n, mismatch arcs K_n and first visit h(n). G133's finite comparison argument, valid for every irrational angle once these mismatch arcs have the stated form, gives

    q_(j+1)-q_j-C-4 <= h(j) <= q_j+C+2

whenever N>=4q_j+3C+8. Choose n minimally with q_(n-1)>T=2C+8. The initial denominator q_0=1 is below T. Minimality and q_j=a_j*q_(j-1)+q_(j-2) give q_(n-1)<=(A+1)*T. Thus

    q_(n+2) <= (A+1)^3*q_(n-1) <= (A+1)^4*T,
    4q_(n+2)+3C+8 <= K_A*(C+4).

The visit bounds therefore hold at all three indices n,n+1,n+2. If any of a_(n+1),a_(n+2),a_(n+3) is at least two, the corresponding visit bounds imply q_(j-1)<=2C+6, impossible. All three coefficients must consequently be one.

**Quantitative separation, including the finite-offset check.** Put D=2C+6. At j=n and j=n+1, the opposite mismatch arcs are disjoint, their combined length is |delta_(j-1)|, and the visit bounds place

    m=h(j)-h(j+1) in [-q_j-D,D].

Also m is nonzero and ||m*alpha||<|delta_(j-1)|. Best approximation forces |m|>=q_j. Since D<q_(j-1)<=q_j, this means m=-q_j-r with 0<=r<=D. If r>0, then r<q_(j-1), so the preceding best-approximation bound and the error recurrence give

    ||r*alpha|| >= |delta_(j-2)|
                 = a_j*|delta_(j-1)|+|delta_j|
                 >= |delta_(j-1)|+|delta_j|.

The triangle inequality on the circle now gives ||(q_j+r)*alpha||>=|delta_(j-1)|, a contradiction. Hence r=0 exactly, and

    h(n+1)=h(n)+q_n,
    h(n+2)=h(n+1)+q_(n+1).

This finite-offset argument uses no unspecified sufficiently-large threshold or phase-dependent distance. It also supplies the explicit justification for G133's quantitative use of Theorem E Step 4. At the selected indices the standard mismatch description applies: n>=2; if n=2 then q_1>T forces alpha<1/8, and later convergent errors are smaller than both coding-interval lengths. The same assertion at n>=3 follows from the first convergent errors and their monotone decrease.

Finally the lower visit bound at n is h(n)>=q_(n-1)-C-4. The second identity and upper bound at n+2 give h(n+1)<=q_n+C+2. Substituting the first identity forces q_(n-1)<=2C+6, again a contradiction. This proves the finite-prefix theorem.

**Finite-left companion consequence.** Let the Rule 30 wall be 0101... and its initial left row be zero beyond radius L>=1. Theorem E Step 0 permits repeat constant C=L. Restarting at physical time 2a enlarges the left-zero radius to at most L+2a. Any matching stretch with this fixed-angle Sturmian code, rephased as necessary, obeys

    b-a < K_A*(L+2a+4).

For the actual disagreement indices k_0<k_1<... against a fixed base code, G131 already excludes finitely many disagreements. The finite-prefix theorem and the intervals between disagreements give

    k_0 <= K_A*(L+4),
    k_(j+1) <= (2K_A+1)*k_j + K_A*L + 6K_A + 1.

Thus unbounded ratios k_(j+1)/k_j are impossible for every bounded-type irrational angle, every phase and every finite left radius. In particular super-geometric flip schedules are excluded throughout this class. The sharper golden constant in G133 remains useful; this uniform class constant is deliberately conservative.

**Independent and unexpected scope checks.** The finite-offset check above is independent of G2.2's asymptotic eta argument and is the identified unexpected check. At A=1 this theorem gives K_A=131 rather than G133's 84, a consistency check without an optimality claim. The schedule k_j=2^j still satisfies the resulting necessary bounds for L>=1, so this argument establishes neither positive kick density nor positive entropy nor realizability. For unbounded partial quotients, the controlled denominator growth used to choose a linear horizon fails; this proof supplies no uniform linear bound there. Arbitrary phase-reset kicks, the measured rational wheel and genuinely multidimensional observables remain outside the claim.

### G.GPT135. a uniform Sturmian horizon bounds phase and angle resets (second-read by Local, 2026-10-06)

### G135. A uniform Sturmian horizon also bounds phase and angle resets (2026-10-06)

**Status and target.** Symbolic proof, independent review pending; no experiment. G133 is independently verified by Local L087; G134 is awaiting review. This strengthens their angle scope rather than optimizing the golden constant. Counterfactual: a huge continued-fraction coefficient could postpone the next usable scale beyond every horizon proportional to the left radius. The finite repetition bound itself prevents that escape. All inputs are the existing Theorem E continued-fraction facts and the explicit G134 finite-offset argument; no general novelty claim.

**Uniform finite-prefix theorem.** For every irrational alpha in (0,1), every phase theta and every integer C>=0, its standard half-open Sturmian prefix through

    N=251*(C+4)

contains a repetition g_s=g_(s+q) on a<=s<=b with b+q<=N and b>2a+q+C. There is no bound on partial quotients in this statement.

Suppose otherwise. Put T=2C+8. Choose n minimally with q_(n-1)>T and put r=n-2. Then q_r<=T. At every usable scale j the finite comparison deadlines of G133 give

    q_(j+1)-q_j-C-4 <= h(j) <= q_j+C+2,
    q_(j+1) <= 2q_j+2C+6 < 2q_j+T,

provided N>=4q_j+3C+8. The second line is the crucial replacement for an externally assumed bound on partial quotients.

The starting scale r is usable, including its small-index cases. If r=0, q_1>T implies alpha<1/8; delta_0=alpha and the two mismatch arcs for period q_0=1 are disjoint, so Theorem E's break description and return gap at least q_1 hold. If r>=1, |delta_r| is at most min(alpha,1-alpha), making the same break description valid. Indeed, when a_1=1, |delta_1|=1-alpha; when a_1>=2, the recurrence alpha=a_2*|delta_1|+|delta_2| gives |delta_1|<alpha. Later errors decrease. Equality of an error with the shorter interval length merely makes the mismatch arcs touch at a half-open endpoint; it does not create an overlap.

Starting with q_r<=T, apply the growth inequality successively at r,r+1,r+2,r+3. Every application is justified within the fixed horizon, because the resulting bounds are

    q_(n-1) < 3T,
    q_n < 7T,
    q_(n+1) < 15T,
    q_(n+2) < 31T,

and

    4*(31T)+3C+8 = 251C+1000 < 251*(C+4).

Thus the visit bounds hold at n,n+1,n+2 as well. This is an induction on already bounded denominators, not a circular assumption that the later scales fit.

At those three scales, any coefficient a_(j+1)>=2 would give q_(j-1)<=2C+6, contradicting q_(n-1)>T. Hence a_(n+1),a_(n+2),a_(n+3) must all be one. The explicit separation in G134 applies at n and n+1: for m=h(j)-h(j+1), best approximation gives m=-q_j-u with 0<=u<=2C+6; a positive u<q_(j-1) would give

    ||(q_j+u)*alpha|| >= |delta_(j-2)|-|delta_j|
                         >= |delta_(j-1)|,

contrary to the distance across the opposite mismatch arcs. Therefore

    h(n+1)=h(n)+q_n,
    h(n+2)=h(n+1)+q_(n+1).

Combining the lower visit bound at n with the upper bound at n+2 yields q_(n-1)<=2C+6, the final contradiction. The uniform finite-prefix theorem follows.

**Companion and reset consequences.** Beside a Rule 30 wall 0101... with initial left-zero radius L>=1, any interval [a,b] matching a standard irrational Sturmian code obeys

    b-a < 251*(L+2a+4).

The phase and angle may be chosen separately for each interval: restart at physical time 2a, use the light-cone radius L+2a and apply the uniform theorem with repeat constant C=L+2a. No relation between the different intervals' angles is required.

Consequently, if a companion is made of consecutive Sturmian-coded pieces with reset times 0=t_0<t_1<..., even allowing both phase and angle to change at each reset, it necessarily satisfies

    t_(j+1) <= 503*t_j + 251*L + 1004.

A final infinite piece is impossible. Super-geometrically separated resets cannot support a finite left seed. For actual disagreements k_j against one fixed irrational Sturmian base, the corresponding statement is

    k_0 <= 251*(L+4),
    k_(j+1) <= 503*k_j + 251*L + 1507.

This excludes super-geometric flips for every irrational base angle, including unbounded-type angles. The improved golden constant of G133 is still stronger within its narrower class.

**Unexpected independent checks and limits.** A tiny alpha whose first denominator is enormous is the identified unexpected check: the initial q_0=1 scale already forces q_1<=2C+8, so the proof never waits for that enormous denominator. The complementary near-one case uses q_1=1 and its short error, rather than incorrectly using the long q_0 mismatch arc. These endpoint-angle controls justify the uniform claim. Dyadic times still pass the necessary bounds, so no positive density, positive entropy or realizability conclusion follows. The pieces must use the standard Sturmian interval (or its complement, which has identical repetitions); arbitrary arc observables and the measured rational wheel are not asserted to have this form. This is a class exclusion for companions, not a prize solution.

*Second reader's note on G134 and G135 (Local, 2026-10-06; chat L088).* Both correct. G134: minimality gives
$q_{n-1} \le (A+1)T$ and $q_{n+2} \le (A+1)^4 T$, hence $K_A = 8(A+1)^4 + 3$ (131 at $A = 1$); the finite-offset step
is sound, since $0 < r \le D < q_{j-1}$ would give $\|r\alpha\| \ge |\delta_{j-2}| \ge |\delta_{j-1}| + |\delta_j|$
and so $\|(q_j + r)\alpha\| \ge |\delta_{j-1}|$, and that step also supplies the explicit form of Theorem E Step 4
that G133 used. G135: the visit bounds themselves give $q_{j+1} \le 2q_j + 2C + 6$, and starting from $q_r \le T$
each step uses a horizon already justified ($3T, 7T, 15T, 31T$), so $4 \cdot 31T + 3C + 8 = 251C + 1000$ fits inside
$251(C + 4)$ with no bound on partial quotients; the tiny-angle and near-one starts are handled correctly. Checked
(`rule30_audit_g99_g100.py`, S32): for the golden angle, $\sqrt 2 - 1$, $e - 2$, $\pi - 3$, a tiny angle
$1/(50 + \varphi)$ and one minus it, at 10 random phases each and $C = 0, 2$, every prefix of length $251(C + 4)$
contains a violating repetition; the latest first violation over all of them came at prefix length 45, so the
uniform constant is very conservative.

### G.GPT136. uniform recoding horizons include rational mechanical bases (second-read by Local, 2026-10-06)

### G136. Uniform recoding horizons include rational mechanical bases (2026-10-06)

**Status and purpose.** Symbolic corollary of G131 and G135; independent review pending. Dependencies G134/G135 are independently verified by Local L088. No experiment. Counterfactual: either a finite recoding margin or a rational limiting angle might evade the uniform horizon. The exact margin and a finite-prefix approximation settle both. This advances recoded/reset companions, not the missing entropy theorem. The inherited rotation-partition prior art is recorded in G131; no general novelty claim.

Let g_s be the standard mechanical code of theta+s*alpha modulo one in [1-alpha,1), now allowing every alpha in [0,1]. The endpoint angles give the constant zero and constant one codes. Let F be any binary function of a block of width w+1, w>=0, and put c_s=F(g_s,...,g_(s+w)). Define

    H(C,w)=251*(C+4)+250*w.

**Finite-prefix theorem.** For every integer C>=0, the prefix of c through index M=H(C,w) contains a repetition c_s=c_(s+q) on a<=s<=b with b+q<=M and b>2a+q+C. Neither injectivity nor nonconstancy of F is needed.

First extend G135 to rational and endpoint angles. Every finite prefix g_0,...,g_N of the specified mechanical code is also a prefix of an irrational mechanical code with slightly perturbed angle and phase. To see the boundary issue explicitly, change the angle by epsilon and increase the phase by eta, choosing eta>(N+1)*abs(epsilon), with both arbitrarily small. At a sample exactly on the upper endpoint 0 modulo one, its displacement is eta+s*epsilon>0, giving the correct right-hand value zero for an interior angle. At a sample on the lower endpoint 1-alpha, its displacement relative to that moving endpoint is eta+(s+1)*epsilon>0, giving the correct right-hand value one. All other finitely many samples have a positive margin and keep their value for sufficiently small changes. Choose the perturbed angle irrational. For alpha=0, choose a small positive angle and a phase perturbation larger than the total drift; every sample stays outside its tiny one-interval. For alpha=1, choose an angle just below one and the same dominating positive perturbation; every sample stays inside the one-interval. Thus the finite-prefix contradiction of G135 holds for every mechanical angle.

Now suppose c satisfies the finite repeat bound through M. The underlying mechanical prefix is available through N=M+w=251*(C+w+4). If g repeats on [a,e] with e+q<=N and e>=a+w, then c repeats on [a,e-w], and its compared samples end by N-w=M. Hence e<=2a+q+C+w. If e<a+w, the same inequality is automatic. Every repetition of g through N would therefore satisfy the forbidden bound with constant C+w, contradicting the extended G135 theorem. This proves the claim and explains why the margin is 250*w rather than an unspecified additive loss.

**Matching pieces and corrections.** Beside the alternating Rule 30 wall with initial left-zero radius L>=1, a companion cannot match such a recoded mechanical word on [a,b] unless

    b-a < H(L+2a,w).

For pieces with reset times t_j and widths bounded by one fixed w, the functions, angles and phases may change from piece to piece, but necessarily

    t_(j+1) <= 503*t_j + 251*L + 1004 + 250*w.

For actual disagreement indices against one fixed recoded mechanical base, the bounds are

    k_0 <= 251*(L+4)+250*w,
    k_(j+1) <= 503*k_j + 251*L + 1507 + 250*w.

Finitely many disagreements or a final infinite piece are impossible by the same finite-prefix theorem at a later restart. Consequently super-geometrically spaced resets or corrections are excluded for bounded-width recodings at every mechanical angle. These are necessary bounds, not a construction of a realizable companion.

**Orbit-endpoint interpretation.** G131 constructs a finite block code for any half-open binary arc partition whose actual jump points have the form beta+k_j*alpha. If the integer exponents span D=max(k_j)-min(k_j)>=1, its Laurent polynomial Q(z)=sum(z^k_j) has an even number of jumps and Q=(1+z)P. P has exponent span D-1, so after rephasing its block width parameter is w=D-1. The same construction works for rational angles: distinct actual jump points are listed once, and equality of the jumps leaves only a constant difference, absorbed in F. Constant partitions use w=0. Thus pieces whose endpoint representations have uniformly bounded exponent span inherit the reset bound, even if their angles and partitions vary. The controlling parameter here is exponent span, not merely the number of endpoints. No arbitrary unrelated-endpoint partition is claimed to have this representation.

**Unexpected width guard, proved without a run.** An unrestricted finite block code can fit any prescribed finite binary prefix. Fix an irrational Sturmian g and finitely many starting indices 0,...,m. Their infinite future tails are pairwise distinct: equality of two would give an eventually periodic mechanical code, impossible because its symbol frequency is irrational. For each pair there is a finite first differing coordinate; take w at least the largest such coordinate. All the blocks g_s,...,g_(s+w) at these indices are distinct. Define F on them to output the desired prefix, and define it arbitrarily elsewhere. This does not give an infinite prescribed word, a uniform w or a finite-left Rule 30 realization. In particular the record's overlap-free Thue-Morse prefixes can pass the repeat inequality for arbitrary finite horizons while being fitted by increasingly wide recodings. A horizon independent of all recoding widths is therefore false. This is the identified independent scope check. At w=0 the theorem recovers G135 and its rational extension; constant F also retains the immediate period-one obstruction. Geometric correction schedules still pass the displayed necessary bounds, and no positive density, entropy or prize solution follows.

*Second reader's note on G136 (Local, 2026-10-06; chat L089).* Correct. The perturbation is sound: with
$\eta > (N + 1)|\epsilon|$ a sample on either endpoint moves to the correct side of the moved interval, and every other
sample keeps a positive margin; the prefix through $N = M + w = 251(C + w + 4)$ carries repetitions of $g$ to
repetitions of $c$ with constant $C + w$, which is where $H(C, w) = 251(C + 4) + 250w$ comes from; the reset and
disagreement recursions follow. Checked (`rule30_audit_g99_g100.py`, S33): exact rational mechanical codes
($\alpha = 0, 1, 1/2, 2/5, 3/7$) and random block codes of width up to 4 over irrational and rational mechanical words
all violate within $H(C, w)$; for the width guard, fitting the first 121 Thue–Morse bits by a recoding of a golden
Sturmian word needs width 204 here, and that Thue–Morse prefix (overlap-free) passes the repeat bound with $C = 0$,
so no width-independent horizon exists, as G136 says.

### G.GPT137. a dyadic sparse word passes every repeat test; faster powers fail (second-read by Local, 2026-10-06)

### G137. A dyadic sparse word passes every repeat test; faster powers fail (2026-10-06)

**Status and target.** Symbolic obstruction audit, independent review pending; no experiment. G134/G135 are verified by Local L088 and G136 awaits review. Counterfactual: using every period and every starting position in Theorem E Step 0, rather than only the derived kick recursion, might rule out all geometrically sparse corrections or force positive word-count entropy. The explicit dyadic word refutes that inference. This strengthens the scope guard rather than claiming a Rule 30 realization. The existing Thue-Morse guard in section 8.57 already shows that the repeat inequality alone is not an entropy theorem; the new point is its exact compatibility with sparse geometric defects. G26/G64 concern a different Rule210 dyadic-run construction and do not supply a Rule30 realization here.

Let d_s=1 precisely when s=2^j for some integer j>=0, and d_s=0 otherwise, including d_0=0.

**Every repetition obeys the strongest nonnegative-margin test.** If d_s=d_(s+q) for every a<=s<=b, where a>=0 and q>=1, then

    b <= 2a+q-1.

For a>=1, choose the smallest power of two p>=a, so p<=2a. If p+q is not a power of two, there is a mismatch at s=p. If p+q=P is a power of two, then P>=2p and p+2q=2P-p lies strictly between P and 2P. Thus there is a mismatch at s=P=p+q. In both cases a mismatch lies in [a,2a+q], proving the bound.

For a=0, if q is a power of two, s=0 is already a mismatch. Otherwise q>=3. If q+1 is not a power of two, s=1 is a mismatch; if q+1 is a power of two, s=2 is a mismatch since q+2 lies strictly between q+1 and its double. In either case the first mismatch is at most q, giving b<=q-1 as required. The reasoning covers every q, not only a selected sequence of convergent periods.

Consequently d satisfies the necessary finite-left repeat bound b<=2a+q+C for every C>=0, all periods and all starting positions. Passing this necessary condition does not establish a compatible forced left row, a full right evolution or a finite global seed.

**Sparse, aperiodic and zero word-count entropy.** The ones have zero density because their count up to N is at most 1+floor(log_2 N). They are infinite but have unbounded gaps, so d is not eventually periodic. For a factor length m>=1, starts a<m contribute at most m different words. For a>=m, two powers of two cannot both lie in [a,a+m-1]: their separation is at least a>=m. Such factors have at most one one, giving at most m+1 possibilities. Therefore the number P(m) of distinct length-m factors obeys

    P(m) <= 2m+1,
    limsup log_2(P(m))/m = 0.

This is word-count entropy of this one word, not the dynamical entropy of Rule 30. Complementing d preserves all repetition tests and its factor complexity.

**Unexpected rate control.** For an integer B>=3 let d^(B) have ones at B^j and zero elsewhere. For sufficiently large p=B^j, between p and Bp the period-one equality stretch has a=p+1 and b=Bp-2. The repeat bound would require

    (B-2)*p <= C+5.

It fails for arbitrarily large p, for every fixed C. Thus these faster geometric isolated-one schedules are excluded for a finite-left alternating-wall companion by Theorem E Step 0 alone. Powers of two are the exact surviving integer-base case for this necessary test. This is the identified independent check: geometric spacing is not a single undifferentiated regime. No experiment or claim about irrational-base flips is used in this control.

**Closed bridge and next obligation.** Do not try to deduce positive entropy, positive defect density or exclusion of every geometric schedule solely from the repeat inequality, even when all q and a are imposed. The explicit sparse word passes the full family. Adding it to a Sturmian base need not preserve that property, so this does not prove that a dyadically flipped Sturmian word passes the tests or is realizable. A useful next proof must use a further Rule30 wall constraint, a relation across the corrections, or the coupled-tail condition of G130. The finite-left sufficiency question for d itself is not answered here.

*Second reader's note on G137 (Local, 2026-10-06; chat L090).* Correct. For $a \ge 1$ the first power of two
$p \ge a$ satisfies $p \le 2a$; either $p + q$ is not a power of two, or $P = p + q$ is and $2P - p$ lies strictly
between $P$ and $2P$, so a mismatch falls in $[a, 2a + q]$; the $a = 0$ cases check; at most $2m + 1$ factors of length
$m$; for base $B \ge 3$ the zero stretch between $p$ and $Bp$ forces $(B - 2)p \le C + 5$. Checked
(`rule30_audit_g99_g100.py`, S34): no repetition of the dyadic word to index 3,000 reaches $b \ge 2a + q$; factor
counts are at most $2m + 1$ for $m \le 40$; the base-3 and base-4 words violate the bound with $C = 5$. The open
question G137 names, whether $d$ itself has a finite left half, is measured directly in
`rule30_dyadic_companion.py` (predictions pushed with this note).

### G.GPT138. the first nonlinear kick gate does not close the initial tail (second-read by Local, 2026-10-06)

### G138. The first nonlinear kick gate does not close the initial-tail problem (2026-10-06)

**Status and purpose.** Symbolic wall audit, independent review pending; no experiment. This follows G137's failed entropy bridge by using the actual Rule30 inverse, rather than another repetition inequality. Prediction: the first few forced columns expose an explicit nonlinear product of neighboring visible bits. Counterfactual: sparsity of that product alone makes the entire forced initial row finite or infinite. Neither implication is obtained. This is an exact low-depth reduction and a retained failed bridge, not a new general inversion theorem or prize result.

Write v_j(t)=x_(-j)(t), with v_0(2s)=0 and v_0(2s+1)=1. Let c_s be column 1's visible bit at physical time 2s. The wall forces v_1(2s)=1-c_s and v_1(2s+1)=1. The inverse Rule30 identity is

    v_(j+1)(t)=v_j(t+1) XOR (v_j(t) OR v_(j-1)(t)).

Put A=c_s, B=c_(s+1), D=c_(s+2). Repeated Boolean substitution yields the exact even/odd pairs

    (v_1(2s),v_1(2s+1)) = (1-A,1),
    (v_2(2s),v_2(2s+1)) = (A,B),
    (v_3(2s),v_3(2s+1)) = (1-B,1-B),
    (v_4(2s),v_4(2s+1)) = (A*B,D),
    (v_5(2s),v_5(2s+1)) = (D XOR (A OR (1-B)),1-B).

For example the depth-four even entry is (1-B) XOR ((1-B) OR A)=A*B. Its odd entry is (1-D) XOR ((1-B) OR B)=D. The depth-five odd entry is B*D XOR (D OR (1-B))=1-B: for B=0 both sides are one, and for B=1 both sides are zero. These independent Boolean simplifications check the product and the cancellation without a dynamical run. They apply to the forced left construction; a full right evolution is an additional constraint.

**Dyadic specialization.** For c=d of G137, c_s*c_(s+1)=1 only at s=1, because 1 and 2 are the only consecutive positive powers of two. Depth four's even trace therefore has exactly one one, at physical time 2; its odd trace still contains infinitely many shifted dyadic pulses. The initial row's first five cells are

    (v_1(0),...,v_5(0))=(1,0,0,0,1).

This supplies neither a tail classification nor a finite-left realization. Vanishing on one temporal parity at one depth is not eventual vanishing across all initial depths.

**Unexpected constant-code control.** If c is constantly zero, the same formulas give an all-one depth-one column and then stationary alternating columns 0,1,0,1 through the depths displayed. The inverse recurrence continues that checkerboard to arbitrary depth: whenever two neighboring columns are stationary and opposite, the next outward column is the inner column's complement. Thus the forced initial left row has infinitely many ones even though the depth-four product is identically zero. This is the identified independent check against treating a sparse product as a finite tail. The constant-one case gives a time-alternating depth-one column, stationary one at depth two, then stationary alternating columns 0,1,0,... outward, likewise an infinite initial tail.

**Failed bridge retained.** A long zero segment of c creates a local checkerboard strip, but the strip's temporal margins grow with the number of inverse columns. Dyadic segments move outward in time as their lengths increase. The low-depth identities do not put that strip onto arbitrarily large depths of the single initial row. Nor does the single nonzero product guarantee that all deeper nonlinear products stay sparse. To settle the dyadic candidate, one needs a uniform all-depth invariant for this inverse recurrence, or a certified initial one at unbounded depths. To settle the general prize, the invariant must cover every admissible companion. No additional census or claimed closed finite-state recursion follows from these formulas.

### G.GPT139. fixed-depth temporal entropy does not measure the initial row (second-read by Local, 2026-10-06)

### G139. Fixed-depth temporal entropy does not measure the forced initial row (2026-10-06)

**Status and target.** Symbolic inverse-locality proof, independent review pending; no experiment. G138's low-depth audit is extended to every fixed depth. Prediction: a temporally sparse visible input creates temporally localized defects at each fixed depth, without controlling the entire spatial initial tail. Counterfactual: irregularity measured along the forced initial row would therefore imply positive temporal word-count entropy in a fixed column. The proof separates those axes. G64's earlier zero-entropy result concerned fixed right columns in a different Rule210 family; it is not imported as a Rule30 theorem.

Use G138's v_j(t) and inverse recurrence. For the constant-zero visible code, the background is b_j=1 at odd j and 0 at even j, for every j>=1. For any visible c define e_j(t)=v_j(t) XOR b_j. Then e_1(2s)=c_s and e_1(2s+1)=0. At depth two,

    e_2(t)=e_1(t+1) XOR e_1(t).

For j>=2, direct subtraction of the stationary background gives

    e_(j+1)(t)=e_j(t+1) XOR e_j(t)*(1-e_(j-1)(t))    when j is odd,
    e_(j+1)(t)=e_j(t+1) XOR (1-e_j(t))*e_(j-1)(t)    when j is even.

Indeed adjacent background bits are opposite. Their perturbed OR differs from one by e_j*(1-e_(j-1)) in the odd case and (1-e_j)*e_(j-1) in the even case. The temporal advance e_j(t+1) remains present; this is not an autonomous elementary rule for the defect field.

**All-depth locality.** By induction, e_j(t) is determined by the samples of e_1 on [t,t+j-1]. If all those samples vanish, e_j(t)=0. The base cases j=1,2 are explicit; at the next depth the two e_j terms use [t,t+j] and the shallower term uses a subinterval, and zero maps to zero in both displayed formulas. For the dyadic c=d of G137, the possible defect times at depth j therefore lie in

    union over k>=0 of [2^(k+1)-j+1, 2^(k+1)], intersected with t>=0.

This is an upper support bound, not equality. Outside these backward neighborhoods the forced column is exactly its checkerboard background value. It does not require linearizing away a nonlinear interaction.

**Temporal word bound.** Let P_c(n) count distinct length-n factors of c. A length-m time factor of v_j starting at u is determined by u modulo two and at most m+j consecutive visible symbols: the inverse locality spans physical times [u,u+m+j-2], and e_1 inserts a zero between visible symbols. Padding the visible window if needed gives

    P_(v_j)(m) <= 2*P_c(m+j).

The same reasoning jointly bounds a temporal vector of the first J columns by 2*P_c(m+J). Thus zero word-count entropy of c implies zero temporal word-count entropy at every fixed depth, and in every fixed finite left window. For d or its complement, G137 gives the explicit bound P_(v_j)(m)<=4(m+j)+2. This is not a uniform statement when the observed depth grows with m.

**Unexpected spatial-tail guard.** To evaluate v_j(0), the determining window length grows with j. Once j>=3, the first dyadic pulse at physical time 2 lies inside that window for every further j. The support lemma therefore does not force e_j(0) to vanish at large j. Nor may the fixed-j entropy limit be taken with j growing. G136's arbitrary-prefix fitting guard is another exact illustration of why unbounded recoding windows evade fixed-width control. These are the identified independent quantifier checks. Finite initial-row measurements described as coin-like are compatible with the proved zero temporal entropy; they concern different axes and do not supply an entropy theorem in either direction.

**Remaining obligation.** This characterizes fixed-depth temporal behavior, but neither proves nor disproves eventual zero support of the forced initial row. An all-depth spatial statement is still required: an explicit infinite family of v_j(0)=1, or another invariant preventing a zero tail. Full right-half realizability and a finite global Rule30 seed remain additional questions. No computational job duplicates Local's dyadic initial-row probe.

*Second reader's note on G138 and G139 (Local, 2026-10-06; chat L092).* Both correct. G138's five even/odd pairs
follow from the wall's two conditions and the inverse recurrence; G139's background is stationary and alternating in
depth, the defect field obeys the two displayed recurrences, and a defect at depth $j$ needs a visible pulse in
$[t, t + j - 1]$. Checked (`rule30_audit_g99_g100.py`, S35) by direct column computation: the five pairs on 100
random visible words; the dyadic initial cells $1, 0, 0, 0, 1$; both defect recurrences and the locality for depths
to 12; the dyadic defects at depths to 30 inside the stated backward neighbourhoods; temporal factor counts at most
$4(m + j) + 2$ for $j \le 10$, $m \le 30$. G139's quantifier point also qualifies my L091: the dyadic word's spatial
row looks coin-like while every fixed-depth column has zero word entropy, and a zero tail beyond the measured depth
is not excluded by that measurement.

### G.GPT140. the wall coding separates family entropy, orbit entropy and finite support (second-read by Local, 2026-10-06)

### G140. The wall coding separates family entropy, orbit entropy and finite support (2026-10-06)

**Status and target.** Symbolic quantifier audit of section 8.39's existing wall itinerary/seed bijection, independent review pending. No experiment or new novelty claim about that bijection. G139 controls fixed-depth temporal words; this block makes its dynamical meaning explicit and checks whether a checkerboard limit supplies a finite-tail contradiction. Counterfactual: zero temporal entropy or an infinite-support limit state would settle the finiteness of the initial seed. Neither does.

Let S be the set of left initial rows whose evolution with imposed wall 0101... has a black nearest-left cell at every odd time. Let Phi(c) be the forced initial left row for any one-sided binary visible word c, and let F be two steps of this wall-driven half-line evolution.

**The known coding intertwines the dynamics.** Phi is a homeomorphism from the full one-sided binary sequence space onto S. Existence follows by the inverse columns: v_1(2s)=1-c_s, v_1(2s+1)=1, and the inverse recurrence constructs all farther columns. Every constructed left cell satisfies the forward Rule30 equation; uniqueness of forward evolution with the imposed wall recovers this diagram from row zero. Conversely any row in S determines c_s=1-v_1(2s), and the same inverse reconstructs that row. Finite output coordinates depend on finite c prefixes, and finite c prefixes depend on finite initial cones, proving continuity both ways. This is the section 8.39/WA1 coding, not a new existence theorem.

The periodic boundary returns to its original phase after two steps. Shifting the whole constructed diagram by two physical times therefore gives

    F(Phi(c))=Phi(shift(c)).

Unlike G130's fixed-right-tail coordinate map, this boundary condition is invariant under the chosen time step, so the displayed relation really is a dynamical conjugacy. S is compact and F-invariant. Its full-family topological entropy is one bit per two-step iterate, because its conjugate is the full binary shift. This does not give a positive entropy theorem for each individual row or any finite-support subclass.

**Dyadic orbit closure.** Let X_d be the closure of the one-sided shifts of the powers-of-two word d. Phi(X_d) is exactly the F-orbit closure of its forced left row. The length-m language of X_d is the language of d; G137 bounds its size by 2m+1. Hence X_d, and by conjugacy Phi(X_d), have zero topological entropy. Equivalently, in the product topology every fixed finite spatial observation has zero temporal entropy as in G139. The full compatible family has entropy one while this particular orbit closure has entropy zero: the quantifiers differ.

**Unexpected support-limit check.** Take t_n=3*2^(n-1), n>=1, halfway between successive dyadic ones. Its distance to the next one tends to infinity, so shift^(t_n)(d) converges to the all-zero visible word. Continuity gives

    F^(t_n)(Phi(d)) -> Phi(0,0,...).

G138 identifies the limit row as the stationary left checkerboard, with one at every odd depth. Thus the dyadic orbit closure contains an infinite-support row regardless of whether its starting row has finite support. If that starting row had radius L, its radius at this iterate would be at most L+2t_n; this bound grows without limit. Finite-support rows with no common radius bound can converge to an infinite-support row. The limit therefore supplies no contradiction. This is the identified independent check, now within one fixed wall and one orbit closure rather than a collection of unrelated initial rows.

**Finite-left target retained.** Write S_fin for S intersected with the eventually-zero initial rows. It is forward invariant, since the left light cone expands by at most two cells per F iterate. It is not known to be nonempty, closed or compact. Neither entropy of S, zero entropy of a particular orbit closure, nor the checkerboard limit decides membership in S_fin. For d itself the needed statement remains an all-depth spatial certificate that Phi(d) has infinitely many ones. For the prize the required exclusion must cover every admissible visible word. This closes only the proposed temporal-entropy/limit-state shortcut; no finite-left witness, full right extension or prize solution is asserted.

*Second reader's note on G140 (Local, 2026-10-06; chat L093).* Correct, and both points GPT asked me to challenge
hold. The conjugacy: the wall has period two, so the diagram from time 2 on is again a compatible diagram in phase
$0101\ldots$ with visible word $\sigma c$, and uniqueness of the coding gives $F(\Phi(c)) = \Phi(\sigma c)$. A second
proof of the coding, by left permutivity: $x_t(-1) = x_0(-1-t) \oplus g_t$, where $g_t$ depends only on depths $1$ to
$t$ and the wall. So the black-time condition at $t = 2s+1$ forces depth $2s+2$ from the depths above it, and the
letter $c_s$ at $t = 2s$ sets depth $2s+1$ freely: in $S$ the odd depths are free and the even depths forced (depth 2
is the complement of depth 1), the first $k$ letters of $c$ fix exactly depths $1$ to $2k$, and depths $1$ to $2k-1$
already fix those $k$ letters. The support quantifier: right; $L + 2t_n$ is a bound for each iterate with no uniform
radius, so the limit gives no contradiction. Two sharpenings. (1) The radius grows by exactly two per $F$ iterate, not
at most two: a leftmost one at $-L$ puts a one at $-L-1$ on the next step, since Rule 30 is permutive in its left
input. So a finite-support $F$-preimage of a radius-$L$ element of $S_{\mathrm{fin}}$ has radius exactly $L-2$, and
any backward chain inside $S_{\mathrm{fin}}$ is finite; with G129's record certificate (no element of radius up to
about 84 for this wall) such a chain has at most about $(L - 84)/2$ steps. This is consistent with G141's finite
descent that can stop, and proves nothing about existence (G141's descent paragraph, written before this note,
already states the exact growth). (2) The measured convergence is sharp:
$\Phi(\sigma^{t_n} d)$ agrees with the checkerboard on exactly depths $1$ to $2^n$ for $n = 2, \ldots, 7$ (the window
of 200 caps $n = 8$), as the modulus predicts, because $\sigma^{t_n} d$ begins with exactly $2^{n-1}$ zeros. Checked
(`rule30_audit_g99_g100.py`, S36 and S37): the two-step intertwining on 50 random words to depth 74 by an independent
half-line evolution; the forward read-back $x_{2s}(-1) = 1 - c_s$ and $x_{2s+1}(-1) = 1$ on 30 words; the free and
forced depth counts for every prefix of length up to 10; exact radius growth on 200 random finite rows.

### G.GPT141. wall predecessors have a finite-tail test but need not be unique or finite (second-read by Local, 2026-10-06)

### G141. Wall predecessors have a finite-tail test but need not be unique or finite (2026-10-06)

**Status and target.** Symbolic spatial-support audit, independent review pending; no experiment. Counterfactual: G121's finite-row injectivity and unique-root descent carry over unchanged to an imposed alternating wall. The boundary guard below refutes the injectivity import, and the inverse transducer gives the exact replacement. G122 already records the zero/black and period-three inverse-tail graphs; this block applies them with the wall's phase and black-time condition specified. It does not revive the closed root route as a prize proof.

Let u be a finite left row at white wall phase zero. Assume, for the conditional clock statement, that u belongs to G140's compatible set S. Rows are listed by increasing depth from the wall. A backward step solves

    q_(j+1)=y_j XOR (q_j OR q_(j-1)),

where y is the output row and q_0 is the input wall bit.

**First backward step, black phase.** The input wall bit is q_0=1 and the black-time condition forces q_1=1. Thus there is exactly one black-phase predecessor z. If u is zero beyond radius L, its outward recursion eventually follows

    M0(a,b)=(a OR b,a).

The graph is 00->00, 01->10, 10->11, 11->11. Consequently z has either an eventual zero tail or an eventual black tail, determined after finitely many inverse steps through u's nonzero region. If u is clock-compatible, z extends its future clock by one black-time sample, so it is compatible in the black starting phase too.

**Second backward step, white phase.** The input boundary is zero, and the nearest-left input bit a is free, giving exactly two white-phase predecessors w^(0),w^(1). They are distinct because their depth-one bits differ. Each evolves to z, then u. If u belongs to S, both predecessors belong to S: their first black-time condition is z_1=1 and all later conditions are inherited from u. Their newly prepended visible bit is 1-a.

If z has an eventual black tail, the far-left recursion of either w follows

    M1(a,b)=(1 XOR (a OR b),a).

Its recurrent graph is 00->10->01->00, with 11 entering at 01. Both predecessors therefore have an eventual period-three tail containing ones, and neither is finite. If z has an eventual zero tail, process its finite nonzero region for each a, then inspect the inverse pair. A 00 pair gives a zero tail; every other pair enters 11 under M0. This is a finite test for which of the two predecessors are finite, conditional on the given finite u. It does not decide whether u satisfies the infinitely many future clock conditions.

**Unexpected finite boundary guard.** With the white boundary fixed at zero, the distinct finite input rows

    (0,1,1,0,0,...) and (1,0,1,0,0,...)

both produce the same left output row (1,0,1,1,0,0,...). Direct XOR-OR substitution at depths 1 through 4 verifies every nonzero output; farther triples are zero. Its depth-one bit is one, so both inputs satisfy the first black-time condition. Their next left output under the black boundary is (1,0,0,1,1,0,0,...). Thus even two-step finite wall evolution is not injective on finite rows passing that first condition. No claim is made that either row passes every later condition or lies in S_fin. Ordinary whole-line finite injectivity remains true: the discarded boundary output and the full right evolution are precisely what this guard omits. This is the identified independent check.

**Descent and its remaining gap.** Any nonempty finite left row has its leftmost one advance exactly one site left per forward step, since the exterior triple is 001. A compatible white-phase row is nonempty, because an empty row fails its first black-time condition. Hence a finite two-step predecessor, when one exists, has radius L-2. Backward descent through finite compatible predecessors must terminate, but it may branch and it can stop when the inverse tails are infinite. Neither a unique finite root nor a finite ancestor for every compatible finite row has been proved. The actual missing bridge would have to exclude these clock-compatible roots or supply a further spatial invariant; the existence of two unrestricted predecessors does not supply such a bridge. No new census, full right extension, finite-left witness or prize conclusion is asserted.

*Second reader's note on G141 (Local, 2026-10-06; chat L094).* Correct; the phase convention, the tail tests and the
finite-prefix scope all hold. With rows by depth and $q_0$ the wall bit, the black-phase predecessor is unique
($q_0 = q_1 = 1$), its tail follows $M_0$ from the last pair, and the two white-phase predecessors ($q_0 = 0$,
$q_1 = a$) follow $M_1$ after a black tail (recurrent cycle $00 \to 10 \to 01 \to 00$, so a period-three tail with
ones) or the $M_0$ test after a zero tail. The guard is right: $011$ and $101$ both give $1011$ and then $10011$, so
$10011$ has two finite white-phase predecessors and the descent really can branch. One connection: by G140's
conjugacy the white-phase predecessors of $\Phi(c)$ are exactly $\Phi(0c)$ and $\Phi(1c)$, the new letter
being $1 - a$, so G141's backward tree is the tree of one-letter extensions of the visible word, and the finite-tail test is
a computable pruning of it. Credit: the exact radius growth that L093 offered as a sharpening of G140 is already in
G141's descent paragraph, written before that note. Checked (`rule30_audit_g99_g100.py`, S38) on 400 random finite
rows of radius 1 to 15: the black-phase predecessor evolves forward to the row, has radius $L - 1$ when finite, and
has the tail $M_0$ predicts; both white-phase predecessors evolve to it, are finite exactly when the test says so,
then with radius $L - 2$, and have a period-three tail after a black tail; the guard; and $\Phi(ac)$ as the
predecessors on 30 random words.

### G.GPT142. a finite compatible candidate must accumulate on infinite support (second-read by Local, 2026-10-06)

### G142. A finite compatible candidate must accumulate on infinite support (2026-10-06)

**Status and target.** Symbolic consequence of the reviewed G140 compact wall coding and G141 exact radius growth; independent review pending. No experiment or novelty claim about compactness. The targeted record search found G129's varying-radius guard and G140's dyadic checkerboard limit, but no statement excluding every compact forward-invariant finite-support subfamily. Counterfactual: an infinite-support accumulation point would contradict a finite compatible starting row. The conclusion below reverses that inference conditionally; it does not prove a finite candidate exists.

Use G140's compact compatible space S and continuous two-step map F. Its finite-support subset S_fin is forward invariant. Every member has positive integer radius R, since the empty row fails the first black-time condition, and G141 proves R(Fu)=R(u)+2.

**Lemma.** There is no nonempty compact A contained in S_fin with F(A) contained in A.

**Proof.** Suppose such an A exists. The sets F^n(A) are nested, nonempty and compact, so their intersection K is nonempty and compact. Moreover F(K)=K. The forward inclusion follows from nesting. For the reverse inclusion, fix y in K. For each n the set

    C_n = F^n(A) intersect F^(-1)({y})

is nonempty, since y belongs to F^(n+1)(A). These sets are nested and compact. Any x in their intersection lies in K and satisfies F(x)=y.

Every point of K has positive integer radius. Choose y in K with the smallest radius occurring in K; this uses the well-ordering of the integers, not continuity or boundedness of the radius function. Surjectivity on K supplies x in K with F(x)=y. Exact growth gives R(x)=R(y)-2, contradicting minimality. Thus A cannot exist.

**Consequences, conditional on existence.** For any u in S_fin, its forward orbit closure in S is nonempty, compact and forward invariant. The lemma forces that closure to contain a row z of infinite support. Since every orbit point F^n(u) is finite, z is an accumulation point along indices tending to infinity. Therefore every hypothetical finite compatible candidate necessarily has an infinite-support orbit accumulation point, not merely the dyadic candidate of G140. Also S_fin is either empty or not closed in S: if nonempty and closed it would itself be a forbidden compact forward-invariant A. In particular it cannot be assumed compact to manufacture finite ancestors. This sharpens G140's closure qualification without deciding whether S_fin is empty.

**Unexpected compactness check.** Compactness alone does not bound finite radii. In the ordinary binary half-line product space, the set consisting of the empty row and the rows e_n with exactly one one at depth n is compact, every row is finite, and its radii are unbounded: e_n converges to the empty row. This is not a compatible wall family; the empty row is excluded from S. It rejects a false shortcut to the lemma. The proof instead uses forward invariance, a compact surjective core and strict radius growth. No assertion that an individual finite row has a finite predecessor is used, and G141's branching or infinite-tail predecessors remain allowed.

**Remaining prize obligation.** An infinite-support limit cannot exclude finite initial support; conditional on such a candidate it is unavoidable. The open Q7 question is still emptiness of S_fin, or a wall-specific constraint on each individual initial tail. This closes the general compact-orbit-limit shortcut, not the finite-tail problem. No measurement, full right extension, finite witness or prize solution is claimed.

*Second reader's note on G142 (Local, 2026-10-06; chat L095).* Correct, checked by hand; no run was needed. The
surjective core holds: $F(K) \subseteq K$ by nesting, each $C_n$ is nonempty because $y \in F(F^n(A))$, and it is
compact because $F^{-1}(\{y\})$ is closed, so the nested intersection supplies a preimage inside $K$. The quantifier
is right: the conclusion is about each member of $S_{\mathrm{fin}}$ and is vacuous if that set is empty. The core is
correct but more than the lemma needs. Every point of $F^n(A)$ is $F^n(a)$ with $a$ nonempty, so its radius is
$R(a) + 2n \ge 2n + 1$; the sets $F^n(A)$ are nested, compact and nonempty, so their intersection has a point, and that
point would have radius at least $2n + 1$ for every $n$, which no finite row has. So the lemma is a nested compact
intersection plus the radius clock. The exclusion of the empty row enters only through exact growth, since the empty
row gains radius one, not two, over a white-black pair. The guard is well chosen: the rows $e_n$ show precisely that
compactness without forward invariance bounds nothing. The consequence that $S_{\mathrm{fin}}$ is empty or not
closed generalises G140's dyadic case to every candidate.

### G.GPT143. an aperiodic half-circle code passes every repeat test (second-read by Local, 2026-10-07)

### G143. An aperiodic half-circle code passes every repeat test (2026-10-07)

**Status and target.** Symbolic Q7 repeat-filter counterexample, independent review pending. No experiment run by GPT. HR0-HR3 were published for Local at d8bb640 before the requested finite test; Local L097 reports HR0, HR2 and HR3 PASS and HR1 HELD on that requested scope; the proof below is all-period and does not infer its conclusion from that test. Existing record: G137's sparse dyadic counterexample, GC158's failed XOR-derivative transfer, and Local L096's all-odd convergent guard. PRIOR-ART.md records the known Rote/Sturmian relation. This is an application to the wall's necessary repeat inequality, not a novelty claim about Rote sequences or a Rule30 realization.

Put beta=2-sqrt(2), alpha=beta/2 and r=sqrt(2)-1. Define

    c_s = floor(s*beta) modulo 2,    s>=0.

**Claim.** For every q>=1 and every interval of equality c_s=c_(s+q) on a<=s<=b, with a>=0,

    b < 2a+q.

Thus this aperiodic half-circle rotation code passes the wall's entire necessary repeat family even with constant C=0. It is not thereby a compatible finite-left companion. Its XOR derivative is the Sturmian mechanical word of slope beta, every constant run of c has length at most two, and its word-count entropy is zero. In particular this filter alone cannot exclude every nonsparse, low-complexity unrelated-endpoint rotation code.

**Mismatch intervals and reduction to records.** Choose the even integer P nearest q*beta and set epsilon=q*beta-P, so -1<epsilon<1 and epsilon is nonzero. With x_s={s*beta}, direct floor subtraction says a mismatch occurs exactly when

    epsilon>0: x_s in [1-epsilon,1),
    epsilon<0: x_s in [0,-epsilon).

For errors of the same sign, a smaller absolute error gives a smaller mismatch interval. Therefore it suffices to prove the claim at the successive same-sign error records: for any q choose a record q0<=q whose error has the same sign and no greater magnitude. A q-repeat interval avoids the larger mismatch interval, hence is a q0-repeat interval, giving b<2a+q0<=2a+q.

Here these records are among q=1, q=2, and the denominators listed below. To justify completeness, alpha=[0;3,2,2,...]. After its first denominator 3, consecutive convergents P/Q and P'/Q' form an integer basis, with opposite signed errors D,D' satisfying |D'|=(2+r)|D|, where Q'<Q. The next denominator is 2Q+Q'. Any pair (p,q) has the form m(P,Q)+k(P',Q'). If its error improves the current record of its sign, m and k must both be positive: opposite signs of coefficients add the error magnitudes, while a zero coefficient gives a multiple no better than a current record. With q<2Q+Q', m must then be one. For k>=2 the magnitude of D+kD' exceeds |D'|, so the only possible improving intermediate is m=k=1, the mediant. At the next convergent the induction repeats. Before denominator 3, the relevant nearest-integer periods are just 1 and 2. Scaling these errors by two gives exactly the even-integer records needed for beta; records with even larger error need not be retained.

Let p_n/q_n be beta's convergents, starting p_1/q_1=1/1 and p_2/q_2=1/2. For n>=2 all p_n are odd,

    q_(n+1)=2q_n+q_(n-1),
    delta_n=q_n*beta-p_n=(-1)^n*r^n.

The alpha convergents after denominator 1 are the even-numerator beta mediants

    Q_n=q_n+q_(n-1),    P_n=p_n+p_(n-1),    n>=2.

Their errors have sign opposite delta_n and magnitude E=(1+r)*|delta_n|. The intervening alpha mediants have beta denominators 2q_n and even numerator 2p_n. This follows by the displayed denominator recurrence (the first such denominator is 4). Hence the required candidate periods are 1, 2, Q_n and 2q_n for n>=2; proving more candidates than strictly set records is harmless.

**A return bound with its mesh proof.** Fix n>=2, put d=|delta_n| and Qnext=q_(n+1). Every block of Qnext successive orbit samples {s*beta} meets every half-open interval of length E=(1+r)*d. Indeed the Qnext orbit points have successive gaps d and d+|delta_(n+1)|=E. To see this directly, in the orientation given by the sign of delta_n, advance the index by q_n modulo Qnext. Without index wrap the circular distance is d; with wrap it is d+|delta_(n+1)|. Coprimality makes one cycle through all indices, and its total distance is

    Qnext*d + q_n*|delta_(n+1)| = 1

by the consecutive-convergent determinant identity. Thus this is the circular neighbor order and its largest gap is E. A half-open arc of length E contains a point even at a gap endpoint. Translating this mesh proves the block statement. It also holds for intervals of length 2d>E. Consecutive mismatch visits for either length therefore have time gap at most Qnext.

We also use the ordinary continued-fraction best-approximation fact already used in G134: for 0<k<q_n, the distance of k*beta to any integer is at least |delta_(n-1)|=(2+r)*d. Both E and 2d are smaller. So neither mismatch interval has a positive visit before q_n.

**Mediant periods Q_n.** The mismatch interval has length E and sign opposite delta_n. If it is the upper interval, its first visit is exactly q_n; if it is the lower interval, it contains time zero and its first positive visit is exactly q_n. In either case the samples at q_n land in it because their signed error has magnitude d<E. A repeat interval before that visit has b<=q_n-1<Q_n, and so satisfies the claim. For any later maximal repeat interval, write its preceding mismatch time as h>=q_n and the next mismatch time as h+g, with g<=Qnext. Then a=h+1, b=h+g-1 and

    b-2a-Q_n = g-h-Q_n-3
              <= Qnext-q_n-(q_n+q_(n-1))-3 = -3.

Subintervals only lower this debt. In the lower-interval case the first run starts at 1, making its bound still stronger.

**Doubled convergent periods 2q_n.** The mismatch interval now has length 2d and the same sign as delta_n. Its first positive visit lies between q_n and Q_n: there is no visit before q_n, and the mediant Q_n has the opposite signed error of magnitude E<2d, so it lands in the interval. In the lower-interval case time zero is also a mismatch. Any repeat before the first positive visit ends by Q_n-1<2q_n. Every later maximal repeat has preceding mismatch h>=q_n and gap g<=Qnext, giving

    b-2a-2q_n <= Qnext-q_n-2q_n-3
               = q_(n-1)-q_n-3 < 0.

This proves the claim for these periods too. For q=1 a match requires x_s<1-beta; its next sample is outside that interval because beta>1/2, so a match run has length at most one. For q=2 the nearest even displacement has epsilon=2beta-2<0, so a match requires x_s>=2-2beta. Its next sample wraps into [1-beta,beta), outside the match interval, and again every match run has length at most one. Both small periods satisfy the claim. The record reduction now proves it for every q.

**Complexity and the unexpected phase check.** The derivative g_s=c_s XOR c_(s+1) equals floor((s+1)*beta)-floor(s*beta), a Sturmian word. Thus c is aperiodic. Since beta>1/2, g contains no consecutive zeros, so c has no constant run longer than two. A length-m c block is determined by its first bit and the length-(m-1) g block. Hence P_c(m)<=2m and c has zero word-count entropy; no randomness statement follows.

The phase is essential. For c'_s=floor(s*beta+1/2) modulo2, the exact first 19 bits are 0110010011001001101. Period 7 repeats on [0,10] and fails at 11, giving debt 10-7=3. These finite values follow from adjacent-integer square-root bounds, the HR3 control preregistered in GC159; this is a direct algebraic check, not a new run or an all-phase conclusion. The period-q derivative lift counterfactual remains refuted by 0101... and its constant-one derivative.

**Scope.** The known half-circle code and the sparse dyadic word of G137 both pass the full necessary repeat family, by different mechanisms. Here numerator parity and mediant returns explain the gap. No initial-tail support theorem, full right extension, finite-left witness, positive-entropy theorem or prize conclusion is established. Q7 now needs a further wall or coupled-tail constraint to exclude this particular phase-zero code; stronger repetition arguments must specify a condition beyond the inequality just passed.

*Second reader's note on G143 (Local, 2026-10-07; chat L099).* Correct; I checked each step by hand, and the lemmas
exactly (S39). The mismatch rule follows from $\lfloor x_s + \varepsilon \rfloor$ with an even shift. The record
reduction is right because a larger mismatch interval of the same sign contains the smaller one. Since
$\alpha = [0; 3, 2, 2, \ldots]$, the same-sign records are the convergents and the single intermediate fraction between
each pair. With $\delta_n = (-1)^n r^n$, the mediant error is $(1+r)d$ with the opposite sign and the doubled error is
$2d$ with the same sign. The mesh is the two-gap case of the three-distance theorem at $q_{n+1}$ points: gap $d$ taken
$q_{n+1} - q_n$ times and gap $E$ taken $q_n$ times, by $q_{n+1} d + q_n |\delta_{n+1}| = 1$. The first-hit times and
both debt bounds follow, and so do the two small periods. The bounds are sharp. At every mediant scale the interval from
$q_n + 1$ to $q_n + q_{n+1} - 1$ (for example $[13, 40]$ at period 17) attains debt $-3$, exactly as L097 measured. At
period 4 the initial interval $[0, 2]$ attains the doubled-period bound $q_{n-1} - q_n - 1 = -2$, and period 1 attains
the overall maximum $-1$. The survival is L096's parity guard made quantitative: every even-sign shift is a mediant or a
doubled convergent, whose error is $\sqrt 2$ or 2 times the convergent's. At a mediant the longest return gap $q_{n+1}$
equals the shift $Q_n$ plus the first-hit time $q_n$, so the debt cannot pass $-3$. Checked (`rule30_audit_g99_g100.py`,
S39, within GC159's 4,096 symbols and with 60-digit decimals): the mismatch rule for every period up to 200; the record
list to 2,048; the gap counts for $n = 2$ to 9; the first hits; the debt bounds at every record period, with $-3$
attained at 7 to 577. The first S39 run failed through my own sign error in the mismatch test ($1 + \varepsilon$ for
$1 - \varepsilon$); after the fix every part passes.

### G.GPT144. the phase-zero half-circle repeat filter has an exact exceptional class (second-read by Local, 2026-10-07)

### G144. The phase-zero half-circle repeat filter has an exact exceptional class (2026-10-07)

**Status and target.** Symbolic Q7 classification, independent review pending; G143 independently verified by Local L099. No experiment. Fix the phase zero used in GC159; this is not an all-phase classification. The inputs are G143's signed mismatch intervals and tail-two mesh argument, ordinary continued-fraction best approximation and Legendre's criterion. The Rote critical-exponent literature is recorded in PRIOR-ART.md; its ordinary factor exponent does not include the starting index in our debt and no theorem from it is imported.

Let beta be any irrational in (0,1), let c_s=floor(s*beta) modulo2, and write p_n/q_n for its convergents, a_(n+1) for the next coefficient and delta_n=q_n*beta-p_n. Then the following are equivalent:

1. There is a finite constant C such that every equality interval c_s=c_(s+q), a<=s<=b, a>=0, q>=1, satisfies b<=2a+q+C.
2. Eventually every a_n is 2 and every convergent numerator p_n is odd.

The angles in (2) form a countable quadratic class. G143's beta=2-sqrt(2) belongs to it and even satisfies the strict C=0 bound. Passing this filter is not a finite-left Rule30 realization. Every other phase-zero half-circle code is excluded by the wall's necessary repeat inequality for every finite left radius.

**Obstruction from even numerators.** Suppose p_n is even, with n large enough that |delta_n|<1. The period q_n has signed even-integer error delta_n, so its mismatch interval is the upper or lower arc of length |delta_n| given in G143. Its first positive visit is exactly h=q_(n+1). Indeed best approximation gives distance at least |delta_n| to every integer at every 0<k<q_(n+1); q_n itself has the wrong error sign to enter this arc, and no other such k attains the opposite endpoint. At q_(n+1) the error has opposite sign and smaller magnitude, so the arc is hit.

If delta_n>0, the prefix equality interval is [0,h-1]. If delta_n<0, time zero is a mismatch and the equality interval is [1,h-1]. Their debts b-2a-q_n are respectively

    q_(n+1)-q_n-1,    q_(n+1)-q_n-3.

Both are at least q_(n-1)-3. Infinitely many even p_n therefore produce unbounded debt. Condition (1) forces all sufficiently late p_n to be odd. The numerator recurrence then forces every sufficiently late a_(n+1) to be even.

**Obstruction from large coefficients.** Put d=|delta_n| and a=a_(n+1)>=3. Write |delta_(n-1)|=(a+gamma)*d with 0<gamma<1. For large n, the period 2q_n has signed even-integer error 2delta_n and mismatch arc of length 2d. Its first positive visit is

    h=(a-1)*q_n+q_(n-1).

Here is an explicit first-hit justification. Expand any integer pair (p,k) in the unimodular basis (p_n,q_n),(p_(n-1),q_(n-1)), with coefficients m,l. An error of the sign opposite delta_n and magnitude less than 2d, which is less than |delta_(n-1)|, requires m,l>0: opposite coefficient signs add error magnitudes, and a zero coefficient is either of the wrong sign or too large. If k<h, then m<=a-2. Its opposite-sign error has magnitude

    l*|delta_(n-1)|-m*d >= (2+gamma)*d > 2d.

Thus no earlier positive visit is possible. At h, m=a-1 and l=1 give the required opposite error (1+gamma)*d<2d. As before the initial equality interval starts at zero or one, according to the sign of delta_n. Its debt for period 2q_n is

    (a-3)*q_n+q_(n-1)-1, or
    (a-3)*q_n+q_(n-1)-3.

These tend to infinity along any infinite set of coefficients at least three. Condition (1) therefore forces eventually a_n<=2. Combined with eventual evenness from the numerator obstruction, it forces eventually a_n=2. This proves (1) implies (2), with explicit violating intervals whenever either obstruction occurs infinitely often.

**Converse: finite exceptions cost only a finite constant.** Assume (2), put r=sqrt(2)-1, and take n sufficiently late. Then the exact error ratios and recurrence are

    |delta_(n-1)|=(2+r)*|delta_n|,
    |delta_(n+1)|=r*|delta_n|,
    q_(n+1)=2q_n+q_(n-1).

The even-numerator mediants have denominator B_n=q_n+q_(n-1) and numerator A_n=(p_n+p_(n-1))/2. They approximate alpha=beta/2 with alternating errors D_n=(delta_n+delta_(n-1))/2, whose successive magnitude ratio is r. Consecutive pairs (A_n,B_n) are unimodular, as direct substitution gives determinant of absolute value one; their denominators satisfy the same tail-two recurrence. Moreover

    B_n*|D_n| = 1/(B_(n+1)/B_n+r)
                -> 1/(2*sqrt(2)) < 1/2.

Legendre's criterion makes them genuine alpha convergents for all sufficiently late n. They are consecutive: their errors have opposite signs, whereas a skipped even number of convergent steps has the same sign, and a skipped odd number of at least three has determinant of magnitude at least two. Thus alpha also has an eventual continued-fraction tail of twos. Its late same-sign error records are its convergents and intervening mediants, by G143's unimodular record argument. Their beta periods are B_n and B_n+B_(n-1)=2q_n. There are only finitely many earlier record periods.

For every sufficiently late B_n or 2q_n, G143's entire mesh and first-hit argument applies verbatim with the displayed error ratios: a q_(n+1)-point orbit mesh has largest gap (1+r)*|delta_n|; no positive arc visit precedes q_n; the mediant visits provide the required first-hit upper bound. Consequently every repeat at these candidate periods satisfies b<2a+q, without any assumption on the finite continued-fraction prefix. Same-sign mismatch-interval inclusion reduces all other late periods to these records.

Each of the finitely many earlier record periods has a nonempty mismatch arc. Irrational rotation has a finite orbit mesh finer than that arc, so every translate of a sufficiently long fixed block hits it. Its equality runs therefore have bounded length, and its repeat debt has a finite upper bound independent of a. Taking the maximum of these finitely many bounds and zero supplies C. This proves (2) implies (1).

**Unexpected parity controls and limits.** The tail-two angle beta=sqrt(2)-1 fails the criterion: it has infinitely many even convergent numerators. Already the convergent 2/5, followed by 5/12, gives a period-5 equality on [0,11] of debt 6. Thus being in the silver quadratic field or having a tail of twos alone is insufficient. Conversely beta=[0;1,1,4,4,...] has eventually all odd numerators but fails by the doubled-period obstruction. These are direct arithmetic controls, not new runs. They distinguish both required conditions from weaker shortcuts.

Every angle satisfying (2) has a finite integer continued-fraction prefix followed by the same infinite tail, so there are countably many and they are quadratic. Their complements and arbitrary phases were not classified here. The wall has a necessary repeat constant determined by its finite left radius, so the theorem excludes all other phase-zero codes as companions. The exceptional class remains unresolved for actual initial-tail support. No finite witness, full right extension, positive-entropy or prize claim follows.

*Second reader's note on G144 (Local, 2026-10-07; chat L100).* Correct, read jointly with G143 as asked. Even
numerators: for $0 < k < q_{n+1}$ with $k \ne q_n$ best approximation is strict, $\|k\beta\| > |\delta_n|$, and $q_n$
itself has the wrong sign, so the first hit is $q_{n+1}$ and the initial debts are $q_{n+1} - q_n - 1$ or $- 3$. Large
coefficients: with $|\delta_{n-1}| = a d + |\delta_{n+1}|$, an opposite-sign error below $2d$ needs both basis
coefficients positive, $k < h$ forces $m \le a - 2$ and an error of at least $(2 + \gamma) d$, and $m = a - 1$, $l = 1$
gives $(1 + \gamma) d$; so $h = (a-1) q_n + q_{n-1}$ and the debts follow. The Legendre step holds: with $a_{n+1} = 2$
the determinant of consecutive even mediants is $\pm 1$ by direct expansion; unimodularity and opposite signs give the
exact identity $B_n |D_n| = 1/(B_{n+1}/B_n + |D_{n+1}|/|D_n|)$, whose limit is $1/(2\sqrt 2)$. The consecutiveness
argument needs both of its parts: two convergents two steps apart can have determinant one when the coefficient between
them is one, and only the sign excludes that case. For late $n$ the complete quotients equal $1 + \sqrt 2$ exactly, so
G143's ratios, mesh and first hits apply verbatim, and the finitely many early records each have bounded equality runs.
Checked (`rule30_audit_g99_g100.py`, S40, G144's own controls, prefixes under 2,100, 60-digit decimals): at
$\sqrt 2 - 1$ the even numerators 2, 12 and 70 give first hits $q_{n+1}$ and the stated debts (6 at period 5 on
$[0, 11]$); at $[0; 1, 1, 4, 4, \ldots]$ the numerators are odd and the doubled periods have first hit
$(a-1) q_n + q_{n-1}$ and the stated debts; and at $2 - \sqrt 2$ the even mediants are unimodular, alternate in sign,
satisfy the identity and the Legendre bound, and are exactly the convergents of $\alpha$.

### G.GPT145. the silver half-phase code fails every finite repeat allowance (second-read by Local, 2026-10-07)

### G145. The silver half-phase code fails every finite repeat allowance (2026-10-07)

**Status and target.** Symbolic Q7 proof, independent review pending. No experiment. G143 is independently verified by Local L099; G144 remains under review. This block follows the finite half-phase control HR3 already preregistered in GC159 and reported by Local L097. The prediction is that its debt-3 witness is the first member of an unbounded family. The counterfactual is a uniform finite debt bound at this phase. The proof uses G143's explicit convergents and mismatch interval, not a new computational scan or a theorem imported from the Rote literature in PRIOR-ART.md.

Put beta=2-sqrt(2), r=sqrt(2)-1 and c_s=floor(s*beta+1/2) modulo2. Let p_n/q_n be beta's convergents, with n=1 giving 1/1 and n=2 giving 1/2. For every odd n>=3, put Q_n=q_n+q_(n-1). Then the period-Q_n prefix equality interval is exactly

    [0, h_n-1],    h_n=2q_n+q_(n-1)/2,

and its debt is

    (h_n-1)-Q_n = q_n-q_(n-1)/2-1 -> infinity.

Consequently no finite C makes b<=2a+q+C hold for every repeat of this half-phase code. In particular it cannot be the wall's companion from any finite left radius. This concerns the chosen half-phase silver code, not every phase or angle.

**Proof of the first hit.** For these odd n, q_n is odd, q_(n-1) is even, and both numerators are odd. Set d=|delta_n|, where delta_n=q_n*beta-p_n. The exact signed errors are delta_n=-d and delta_(n-1)=(2+r)d. Period Q_n has an even numerator and positive error E=(1+r)d. Since E<1/2 for n>=3, its mismatch interval in the shifted coordinate is [1-E,1). Thus a positive time k is a mismatch exactly when

    {k*beta} is in [1/2-E,1/2).

Equivalently, there is an odd integer p with 2k*beta-p negative and magnitude at most 2E. Equality at the endpoint is impossible: it would imply an integer multiple of beta is an integer, since E=Q_n*beta-(p_n+p_(n-1)). Expand the integer pair (p,2k) in the unimodular basis (p_n,q_n),(p_(n-1),q_(n-1)), with integer coefficients m,l. Denominator parity forces m even; odd numerator parity then forces l odd. Its error is

    [-m+(2+r)l]*d.

A negative error of magnitude less than 2E requires m,l>0. Indeed m<=0,l>0 has the wrong sign; both negative give a negative denominator. If m>0,l<0, parity gives m>=2 and |l|>=1, and the magnitude is at least (4+r)d>2E. A zero coefficient is ruled out by parity, has the wrong error sign, or has a nonpositive denominator. Therefore m is a positive even integer and l a positive odd integer.

For l=1, the first possible m is 4: m=2 has positive error; m=4 has negative error of magnitude (2-r)d<2E. It gives denominator 4q_n+q_(n-1), hence time h_n. If l>=3, negative error requires m>(2+r)l, so m>=8; its denominator exceeds the one just found. This proves h_n is the first positive mismatch. Time zero is not a mismatch, since its shifted coordinate is 1/2. The prefix equality and its exact endpoint follow.

The denominator recurrence gives unbounded q_n and q_(n-1)<q_n, so the displayed debt is greater than q_n/2-1 and diverges. This proves the exclusion for every finite allowance.

**Unexpected check and scope.** At n=3 the convergents are 3/5 and 1/2: Q_n=7, h_n=11, and debt=3, exactly HR3's retained finite witness. The same angle at phase zero passes every period with C=0 by G143. Thus changing the phase can change boundedness of the repeat debt, not just its finite constant. This is not a finite Rule30 witness at either phase. The boundary-phase exceptional angles in G144 and their actual forced initial tails remain unresolved; no prize claim follows.

*Second reader's note on G145 (Local, 2026-10-07; chat L101).* Correct. At phase one half the mismatch rule for period
$Q_n$ moves the arc to $\{k\beta\} \in [1/2 - E, 1/2)$, which is exactly an odd $p$ with $2k\beta - p \in [-2E, 0)$. For
odd $n$ the denominators $q_n$ are odd and $q_{n-1}$ even, so in the basis expansion of $(p, 2k)$ the coefficient $m$ is
even and $l$ odd, and the error is $(-m + (2+r) l) d$. Mixed signs give at least $(4 + r) d > 2E$, zero coefficients
fail by parity, sign or denominator, and for $l = 1$ only $m = 4$ lands in the window $(2 + r, 4 + 3r)$; every $l \ge 3$
needs $m \ge 8$ and a larger denominator. So the first hit is $h_n = 2q_n + q_{n-1}/2$, time zero is not a mismatch, and
the prefix debt is $q_n - q_{n-1}/2 - 1$. The phase contrast with G143 is the striking part: the same angle passes every
period at phase zero with $C = 0$ and fails every finite allowance at phase one half. Checked
(`rule30_audit_g99_g100.py`, S41, within GC159's 4,096 symbols, the integer floors cross-checked against 60-digit
decimals): for $n = 3, 5, 7, 9$ the first mismatch of period $Q_n$ is $h_n$, every mismatch time lies in G145's arc and
every arc time is a mismatch, and the prefix debts are 3, 22, 133 and 780, the first being HR3's witness.

### G.GPT146. shifted passing codes approach an explicitly excluded infinite tail (second-read by Local, 2026-10-07)

### G146. Shifted passing codes approach an explicitly excluded infinite tail (2026-10-07)

**Status and target.** Symbolic Q7 closure audit, independent review pending. Depends on verified G140/G143 and the pending G145 half-phase exclusion. No experiment. Prediction: every time shift of the passing silver code still has some finite repeat allowance, but these allowances cannot be uniform when the phases approach one half. Counterfactual: closure of the passing family might transfer its repeat bound, or finite support, to every limiting rotation phase. G142 already closes the general finite-support compact-limit shortcut; this block names a specific excluded limit and identifies exactly which allowance loses uniformity. Existing rotation and wall-coding records are used, with no new prior-art theorem or computational job.

For a binary one-sided word x define B_C by the requirement that every equality interval x_s=x_(s+q), a<=s<=b, satisfies b<=2a+q+C, for all a>=0 and q>=1. Take C>=0, and put B=union over all nonnegative integer C of B_C. Let sigma be the left shift.

**Shift and finite-prefix control.** If x belongs to B_C, sigma^t x belongs to B_(C+t). A repeat of the shifted word translates to [a+t,b+t] in x, whose bound gives b<=2a+q+C+t. Conversely, if sigma^t x belongs to B_C, then x belongs to B_(C+t). For a repeat of x with a>=t, translate back and use the shifted bound. If a<t<=b, its suffix [t,b] translates to a repeat starting at zero, giving b<=t+q+C<=2a+q+C+t. If b<t, the bound is automatic. Thus x is in B if and only if sigma^t x is in B. Words that agree after a finite prefix also agree on membership in B. Global complementation preserves every B_C exactly.

**Closed at fixed allowance, not at some allowance.** Each B_C is closed in the product topology: any violation is certified by a finite repeat witness, involving finitely many coordinates through b+q, and persists in the corresponding cylinder. An intersection of these closed finite-witness constraints is closed. This does not make their increasing union B closed.

Let beta=2-sqrt(2) and c^(rho)_s=floor(s*beta+rho) modulo2, with rho considered modulo2. G143 places c^(0) in B_0, hence every sigma^t c^(0)=c^(t*beta modulo2) is in B. Irrational rotation has a dense forward orbit, so choose t_j with t_j*beta modulo2 tending to 1/2. No coordinate s*beta+1/2 is an integer, so every fixed finite prefix eventually agrees exactly with c^(1/2). Therefore

    sigma^(t_j)c^(0) -> c^(1/2),

while G145 gives c^(1/2) not in B. This proves B is not closed. More precisely, for any fixed C, choose a G145 witness with debt greater than C. Every sufficiently large j shares all coordinates of that witness and fails B_C. Thus the smallest nonnegative repeat allowances for these passing shifted words tend to infinity, not just along some unspecified subsequence. The simple upper allowance t_j remains valid.

The passing phases t*beta modulo2 and the excluded phases 1/2+t*beta modulo2 are both dense. The latter exclusion follows from the reverse-shift implication above. These are two countable dense phase orbits, not a classification or measure statement about the other phases. They are disjoint by irrationality.

**An explicit infinite forced-tail limit.** In G140's notation Phi maps a visible word to its unique compatible initial left row and satisfies F Phi=Phi sigma for the two-step wall evolution F. Its exact finite-prefix modulus makes Phi continuous. Put u_0=Phi(c^(0)) and u_half=Phi(c^(1/2)). Then

    F^(t_j)(u_0) = Phi(sigma^(t_j)c^(0)) -> u_half.

G145 and the wall's necessary finite-radius repeat bound force u_half to have infinite support. This identifies an infinite-support accumulation point of the actual forced-tail orbit of u_0, without assuming whether u_0 itself has finite support. If u_0 were finite, the exact radius clock in G141/G142 would grow by two per F, and such an infinite-support limit is entirely consistent. No contradiction to a finite u_0 follows. Nor does the existence of infinite support at the limiting phase provide a fixed depth beyond which every approximating phase is nonzero.

**Unexpected prefix guard and remaining obligation.** Altering finitely many symbols of a passing word cannot create the unbounded-debt failure, by the shift control just proved. Hence the half-phase failure is not explained by changing the first boundary symbol or a finite startup transient; the two codes differ at infinitely many times. The phase comparison still yields no lower bound on the actual support of u_0. Q7's remaining obligation is a constraint on that individual forced tail, beyond repetition or nonuniform compact limits. No finite witness or prize claim follows.

*Second reader's note on G146 (Local, 2026-10-07; chat L102).* Correct. The shift control holds in both directions,
including the straddling case $a < t \le b$, where the suffix $[t, b]$ gives $b \le t + q + C$. Each $B_C$ is closed
because a violation is a finite witness. $\sigma^t c^{(0)} = c^{(t\beta \bmod 2)}$ holds since adding 2 to the phase
leaves every parity unchanged. Convergence to $c^{(1/2)}$ is coordinatewise, because no $s\beta + 1/2$ is an integer, so
each G145 witness is eventually inherited and the least allowance escapes along the whole approach, not along a
subsequence. The two dense phase orbits are disjoint by irrationality, and continuity of $\Phi$ with
$F \Phi = \Phi \sigma$ carries the limit to the forced rows. As the block says, this gives no contradiction for a finite
$u_0$ (G142). Checked (`rule30_audit_g99_g100.py`, S42, only GC159's 4,096 symbols of $c^{(0)}$): the shift identity,
the shift allowance (maximal debt at most $t$) on the seven shifts below 2,048 that set a new closest phase to 1/2, and
the G145 witnesses for $n = 3, 5, 7$ inside every shifted prefix whose agreement with $c^{(1/2)}$ covers them.
Descriptive: at $t = 11, 18, 35, 373$ the maximal debt is exactly $t - 3$, so the shift allowance is nearly attained.
The reason: a G143 interval lying wholly beyond $t$ gains exactly $t$ in debt under the shift, and the maximum comes
from a sharp one, for example $[13, 40]$ at period 17 when $t = 11$. My first draft of S42 also expected the agreement
and the debt to rise monotonically along those shifts. G146 claims neither; the approach alternates sides of 1/2 and the
prefix truncates the debt, so that draft failed and was narrowed.

### G.GPT147. at a fixed irrational angle, finite-tail phases are empty or countable and dense (second-read by Local, 2026-10-07)

### G147. At a fixed irrational angle, finite-tail phases are empty or countable and dense (2026-10-07)

**Status and target.** Symbolic Q7 corollary, independent review pending. No experiment or general symbolic-dynamics novelty claim. Uses the verified wall coding G140, radius clock G141/G142 and fixed-radius count G129. G145 is independently verified by Local L101. Prediction: varying the phase can give an almost-every-phase exclusion without deciding one exceptional phase. Counterfactual: density of the phase orbit would promote a finite-tail realization to an interval of finite-tail phases. The countability argument refutes that promotion. The phase-dependent repeat record is G143-G146; no external theorem beyond the elementary density of an irrational rotation is imported.

Fix any irrational beta in (0,1). For phases rho modulo2 let c^(rho)_s=floor(s*beta+rho) modulo2, and let

    E_beta = {rho : Phi(c^(rho)) has finite support}.

Then E_beta is countable and forward invariant under rho -> rho+beta modulo2. It is either empty or dense. In particular almost every phase has an infinite forced initial left tail, at every fixed irrational angle, including the exceptional phase-zero angles of G144. This statement does not exclude any specified phase in E_beta, or establish that E_beta is nonempty.

**Proof.** Distinct phases modulo2 give distinct visible words. Indeed the two shifted half-circle partitions disagree on a nonempty open interval of the length-two circle whenever their shifts differ modulo2. The forward orbit s*beta modulo2 is dense and enters that interval, giving a differing symbol. The uniqueness of Phi therefore makes the phase-to-initial-row map injective.

There are only countably many finite binary initial rows: at radius at most L there are at most 2^L. Injectivity gives at most 2^L phases in E_beta with radius at most L. Taking the union over positive integer L makes E_beta countable, hence of Lebesgue measure zero. The empty row is not compatible with the clock, as in G141.

The conjugacy gives F(Phi(c^(rho)))=Phi(c^(rho+beta modulo2)). Forward evolution preserves finite support, so E_beta is forward invariant. If it contains rho, it contains its whole dense irrational forward orbit. Its radii on that orbit are exactly R(rho)+2t by the radius clock. This proves the empty-or-dense dichotomy, and explains why countability and density do not conflict.

**Uniform-radius qualification.** Every fixed-radius phase set is finite. Consequently, along any convergent sequence of pairwise distinct phases in E_beta, the radii tend to infinity: a bounded-radius subsequence would lie in a finite set, contradicting distinctness. An interval of finite-tail phases is impossible, but a dense exceptional set of finite tails is allowed. No uniform-radius conclusion follows from density of one orbit.

**Unexpected check and remaining obligation.** The same countability argument applies at the silver angle even though G143 passes every repeat test and G145 fails every allowance at another phase. Conversely, assuming just one finite phase would supply a dense countable orbit with steadily growing radii, fully consistent with the infinite-support limits in G142/G146. Thus an almost-every-phase theorem, residual-set argument or dense collection of infinite tails cannot settle the individual boundary-phase candidate. E_beta has not been shown nonempty, and its countability is not a prize solution or an all-phase exclusion. The next obligation remains a spatial constraint on Phi(c^(0)), rather than another phase-counting estimate.

*Second reader's note on G147 (Local, 2026-10-07; chat L103).* Correct, checked by hand with G146 as asked; no run was
needed. Two phases that differ modulo 2 code by two half-circles of the length-2 circle whose symmetric difference is a
nonempty open set (the whole circle when the phases differ by 1, giving the complement), and the dense forward orbit
enters it, so phase to word is injective, and $\Phi$ makes phase to row injective. Countability follows from the
countable finite rows. $\sigma c^{(\rho)} = c^{(\rho + \beta)}$ with $F \Phi = \Phi \sigma$ gives forward invariance,
the dense forward orbit gives the dichotomy, and the radius clock gives $R(\rho) + 2t$ along it. One sharpening from
GC156: by the free odd depths, at most $2^{\lceil L/2 \rceil}$ phases in $E_\beta$ have radius at most $L$, not $2^L$.
The record certificate behind G129 also makes every member of $E_\beta$, at every angle, have radius above about 84.
This bounds nothing uniformly, as the block's divergence statement already says. GC164's warning is well placed: a
measure or census statement would be overwhelmingly negative and still blind to the countable set a candidate must lie
in.

### G.GPT148. fixed-order temporal differences preserve entropy but not the repeat sign (second-read by Local, 2026-10-07)

### G148. Fixed-order temporal differences preserve entropy but not the repeat sign (2026-10-07)

**Status and target.** Symbolic diagnostic audit, independent review pending. No experiment, shader change or new general finite-difference novelty claim. The owner linked the project to temporal motion fields; WHAT-WE-BUILT.md's overview and motion-field description were read, alongside the existing G96 transport guard, G138/G139 stationary-tail controls and G143's Sturmian derivative. Prediction: every fixed-order XOR temporal difference has the same word-count entropy as the original binary trace. Counterfactual: going to acceleration, jerk or another fixed order automatically reveals positive entropy missed by the visible trace. The elementary block argument refutes that implication, without refuting uses of these fields for specific structural diagnostics.

Let S shift a one-sided binary word forward, and let D=1+S over GF(2). For any fixed k>=1, D^k is the order-k XOR temporal difference. If P_x(n) counts the distinct length-n factors of x, then

    P_(D^k x)(n) <= P_x(n+k) <= 2^k P_(D^k x)(n).

The first inequality holds because the difference block is a fixed function of its n+k input symbols. For the second, each output block and the first k input bits determine all the remaining input bits: the coefficient of x_(s+k) in (D^k x)_s is one, so solve sequentially for x_k,x_(k+1),...,x_(n+k-1). There are at most 2^k possible first k bits. Thus the word-count entropies agree (using limsup log2(P(n))/n, and invariance under the fixed length shift k). This is valid for one word and its factors, not only for the full shift.

In particular every fixed-order difference of G143's silver code still has zero word-count entropy. The combined jet (x,Dx,...,D^k x) has exactly P_x(n+k) distinct length-n vector factors: its first component gives the n observed input bits; at the last observed time, levels 1 through k form a triangular system recovering the next k input bits in order, because each level has coefficient one on its newest input. Keeping all levels cannot add an entropy rate either. No assertion is made for k growing with the observation length, or for unbounded spatial windows.

**Period and sign controls.** G96 already proves the dyadic identity D^(2^m)=1+S^(2^m); it is reused, not rediscovered as a new result. Thus at these orders a zero difference interval is exactly an equality interval with lag 2^m. A nonzero difference distinguishes a complement-repeat from a repeat, which is the sign lost in the Sturmian integration in GC158. If D^k x is eventually zero, choose 2^m>=k and multiply by D^(2^m-k): x is eventually periodic with period dividing 2^m. More generally eventual periodicity of D^k x implies eventual periodicity of x, by integrating each order: when Dy is p-periodic, y_(s+p) XOR y_s is the constant parity of one derivative period, hence y is 2p-periodic. Iterating gives a sufficient period 2^k p. This period bound is not claimed optimal.

These XOR observables are different from ordinary signed finite differences on integer-valued samples. If an ordinary order-k difference of a bounded integer sequence is eventually zero, successive summation makes its tail a polynomial of degree at most k-1; boundedness forces that polynomial to be constant. For the alternating binary trace 0101..., D^2 x is zero, but its ordinary second difference is the alternating sequence -2,2,-2,2,... . XOR acceleration zero therefore does not mean a constant binary state, or zero ordinary acceleration.

**Unexpected support guard and next obligation.** G138's constant-zero visible code has the stationary checkerboard forced left row, with infinitely many ones. Every fixed-depth temporal column is constant, so all positive-order temporal differences vanish there, under either arithmetic. The derivatives discard the stationary spatial background. This directly refutes inferring finite spatial support from quiet temporal jets, even when every fixed order at every fixed depth is checked. G96 separately explains why fixed-cell differences are not physical acceleration of tracked structures. A productive next use must name a coupled spatial constraint or a specific phase/sign relation; it cannot rely on a generic entropy increase, derivative quietness or the mere word 'acceleration'. No finite initial-tail exclusion or prize claim follows.

*Second reader's note on G148 (Local, 2026-10-07; chat L104).* Correct, with both points GPT asked me to audit
confirmed. The block inversion: the coefficient of $x_{s+k}$ in $(D^k x)_s$ is $\binom{k}{k} = 1$, so the first $k$
input bits and an output block of length $n$ fix the input block of length $n + k$, giving
$P_x(n+k) \le 2^k P_{D^k x}(n)$. The joint jet: the first component gives the $n$ observed bits, and at the last
observed time level $j$ has coefficient one on $x_{t+j}$ with all its other inputs already known, so the jet block and
the input block of length $n + k$ determine each other and the count is exactly $P_x(n+k)$. The integration period $2p$,
the dyadic identity owned by G96, the ordinary-difference contrast and the stationary checkerboard all hold. The
checkerboard is fixed by every single wall step, since every cell has a black cell among its centre and right inputs
(the wall included) and so becomes the complement of its left neighbour, which is its own value. Checked
(`rule30_audit_g99_g100.py`, S43): both inequalities and the exact jet count for $k \le 5$ and $n \le 12$ on GC159's
silver prefix and 20 random words; the dyadic identity for $m \le 4$; the period $2p$ for every derivative pattern with
$p \le 6$; the $0101\ldots$ contrast; and the checkerboard fixed for 40 single steps.

### G.GPT149. eventually finite compatible rows have exactly zero-reaching periodic tails (second-read by Local, 2026-10-07)

### G149. Eventually finite compatible rows have exactly zero-reaching periodic tails (2026-10-07)

**Status and target.** Symbolic Q7 tail reduction, independent review pending. No experiment. Uses the reviewed inverse-pair maps and periodic-tail classification G124, the wall coding G140 and predecessor/radius facts G141/G142. Existing-record search found these ingredients but not the all-depth equivalence below. No novelty claim for finite-state inversion or backward shift density. Prediction: finite future support is a stricter spatial-tail property than mere eventual periodicity, but is invariant under finite visible-prefix changes. Counterfactual: a periodic initial tail or a quiet temporal field automatically supplies a finite future row. The stationary checkerboard refutes that shortcut.

Write S for the compatible initial left rows with imposed wall 0101..., F for two physical steps, and S_fin for its finite-support rows. Define

    S_event = union_(k>=0) F^(-k)(S_fin), inside S.

Then u belongs to S_event if and only if its initial far-left tail is eventually spatially periodic, with that periodic pattern reaching the all-zero pattern after a finite number of ordinary Rule30 steps. This is an exact characterization of becoming finite later, not of being finite at time zero.

**Necessity, using both neighboring cells.** Suppose F^k(u) is finite, so the row at physical time 2k is eventually zero. A single backward step solves the known inverse recurrence

    q_(j+1)=y_j XOR (q_j OR q_(j-1)).

If the output y has an eventually periodic tail of period p, the outward recursion is a deterministic finite-state system: its state is the adjacent input pair together with position modulo p. There are 4p states. Along the actual predecessor row the state eventually repeats, so the predecessor also has an eventually periodic spatial tail. No injectivity, finite predecessor or particular choice of near-wall bits is assumed. Repeating this argument for all 2k backward steps proves that u has an eventually periodic tail.

For any fixed number of forward steps, sufficiently far-left cells have cones disjoint from the finite head and the wall. Their evolution is therefore exactly the ordinary Rule30 evolution of this periodic tail pattern. Since the output after 2k steps is eventually zero, the whole periodic pattern reaches zero by then. G124 now restricts its least spatial period to 1 or 3*2^a, a>=0. For k>=1 a nonconstant such pattern has a<=2k-2, since the two final steps are period3 -> all ones -> all zeros, and each earlier backward period can at most double. Thus its least period is at most 3*4^(k-1). These bounds describe tails only; they do not decide the wall compatibility of a finite head.

**Sufficiency.** Conversely, suppose u is in S and its eventual periodic tail pattern reaches zero after T steps. Beyond the finite head enlarged by the T-step light cone, the evolved row is zero. It has finite support. Advance to the next even physical time if T is odd; finite support is preserved. Thus F^ceil(T/2)(u) is finite and u belongs to S_event. The imposed wall and its compatibility must be retained; a tail pattern alone is not a construction of such a u.

**Visible-prefix interpretation and density qualification.** Let C_fin=Phi^(-1)(S_fin). G140's conjugacy gives

    Phi^(-1)(S_event)=union_(k>=0) sigma^(-k)(C_fin).

Each length-k binary prefix can be prepended freely to any c in C_fin, producing a compatible row that becomes Phi(c) after k two-step iterates. All these ancestors have zero-reaching periodic spatial tails by the equivalence just proved. Initial finiteness itself is not asserted for them; G141 explains that ancestors may instead have black or period-three tails.

S_event is countable: S_fin is countable, and each finite row has exactly 2^k compatible preimages under F^k by the full one-sided shift coding. It is empty exactly when S_fin is empty. If nonempty, it is dense in S: to match any finite visible prefix w, prepend w to one chosen c in C_fin. Continuity of Phi transfers this cylinder density. This countable dense conditional family is not a finite-support compact family or an existence proof.

**Unexpected periodic-tail control and consequence.** A spatial 001 tail evolves to all ones and then zero. A spatial 01 checkerboard is stationary, so periodicity alone does not suffice. G138/G140's compatible checkerboard example has quiet temporal columns and lies outside S_event. Conversely a zero-reaching tail class, if wall-compatible, gives a finite future row even though its initial support can be infinite. These are far-tail identities, not new experiments or candidate constructions.

An unbounded-debt visible word cannot lie in S_event: if any shift had a finite compatible row, its repeat allowance would be finite; G146's reverse-shift control would give one for the original word. Hence G145's half-phase code has neither a finite initial tail nor any zero-reaching eventual periodic tail. The phase-zero silver code remains unresolved. For it, proving an aperiodic tail or a periodic tail outside the zero basin would exclude even future finiteness; proving membership in the zero-reaching tail class would instead supply a finite compatible future row. Full right extension and a finite global seed remain separate obligations. No prize conclusion follows.

*Second reader's note on G149 (Local, 2026-10-07; chat L105).* Correct. Necessity: the inverse recursion run outward on
an output with eventual period $p$ is a finite-state system on (pair, position modulo $p$), so every predecessor,
whatever its near-wall bits, has an eventually periodic tail, and $2k$ steps carry this back to $u$. Far cells see
neither the head nor the wall for a fixed number of steps, so the tail pattern itself must reach zero by time $2k$. The
period bound rests on G124's reviewed rule that a nonconstant output's periodic predecessors at most double the least
period, with the only other step $001 \to 111$; so a nonconstant tail has period $3 \cdot 2^a$ with $a \le T - 2$ and
$T \le 2k$. Sufficiency, the prefix interpretation, countability through exactly $2^k$ preimages, and conditional
density all hold, and the unbounded-debt exclusion is right by G146's reverse-shift control. Checked
(`rule30_audit_g99_g100.py`, S44): on every cyclic ring up to size 24, each row reaching zero has least period 1 or
$3 \cdot 2^a$ with $a \le T - 2$; from 200 random finite rows, one to four backward wall pairs give eventually periodic
tails of an allowed period that reach zero within $2k$ ordinary steps, and each evolves forward to its finite row; and
the 001 and 01 controls. The first run of the second part failed through my own orientation slip: the depth-indexed
tails, which run leftward, were fed to a ring that reads left to right. Reversed, every case passes.
*Correction (Local, 2026-10-07, chat L109).* The ring part of S44 was not exhaustive as first run: it followed each
row forward for only $3n + 3$ steps, and on the 24-ring 2,592 rows first reach zero later, up to step 147. S44 now
takes the exact basin from a backward search from zero, cross-checked on the 24-ring against 1,500 forward steps,
and the period statement holds on every zero-reaching row of every ring up to size 24.

### G.GPT150. a zero-gap parity criterion determines every periodic predecessor period (second-read by Local, 2026-10-07)

### G150. A zero-gap parity criterion determines every periodic predecessor period (2026-10-07)

**Status and target.** Symbolic periodic-tail refinement, independent review pending. No experiment. Uses reviewed G13's exact reset language and G124's inverse-pair period bound; relevant prior-art scope is in PRIOR-ART.md. Prediction: for a nonconstant periodic output, the stay-or-double choice is determined by a parity of its cyclic zero gaps. Counterfactual: G124's bound alone leaves that choice unspecified. The two-state return calculation below supplies the exact choice and counts the aligned whole-line predecessors. This concerns ordinary spatial rows, not temporal diagonals or a forced-wall finite head.

Fix a nonconstant whole-line output y of least spatial period p. Around one primitive period, list the lengths L of runs of ones between consecutive zeros, including L=0 for adjacent zeros. Then:

- If any L is 1 modulo3, y has exactly one whole-line predecessor, of least period p.
- Otherwise, let N count the gaps with L=2 modulo3. If N is even, y has exactly two whole-line predecessors, both of least period p. If N is odd, it has exactly two whole-line predecessors, both of least period 2p; translation by p exchanges them.

Every whole-line predecessor is periodic. Counts are for a fixed labeled output y, without quotienting the predecessors by spatial phase. Constant outputs are separate: zero has its two constant predecessors, and one has the three period-three phases from G124.

**Return-map proof.** Use G13's adjacent input state (a,b) and descending driver transitions

    T_y(a,b)=(b, y XOR (a OR b)).

Reading one spatial output period gives a deterministic map H on four states. A whole-line predecessor supplies a bi-infinite orbit of H at successive period cuts. Every such orbit lies on a cycle: in a finite functional graph, a noncycle point has only a bounded backward transient; a deterministic cycle cannot be exited. Conversely every cycle point determines a unique predecessor by following the within-period transitions in both directions. This also proves that no nonperiodic whole-line predecessor was omitted.

If a cyclic gap has L=1 modulo3, repetitions of the driver contain the G13 reset factor 0 1^(3h+1) 0 z. Some power of H therefore has singleton image. H has exactly one cycle point and that point is fixed, giving one p-periodic predecessor. Least period is p because an output's least period divides every predecessor period. The reset factor may straddle periods; it is not necessary that H itself already have rank one.

Suppose no gap is 1 modulo3. After sufficiently many zeros, the surviving pair-state set just after a zero is either

    C={00,11},    A={00,01}.

This follows from G13's image table: the second zero reduces the full image to at most two states, and in the absence of the forbidden gap the after-zero sets are C or A. Label 00 as zero and the other state as one. Direct use of the four-state transition table gives, for a run of L ones followed by a zero:

| L modulo3 | Starting C or A | Ending set | Label map |
|---|---|---|---|
| 0 | either | C | identity |
| 2 | either | A | interchange |

This includes L=0. For positive multiples of three, T_1 cycles 00->01->10->00, and the following zero yields C with the same labels; for residue two the following zero yields A with exchanged labels. In particular both labels survive every permitted gap. At a fixed cyclic cut the set type returns to itself, so H on its recurrent two-state set is identity when N is even and interchange when N is odd. The corresponding one- or two-period cycles give exactly the stated two predecessors. Output least period p rules out any smaller period; the interchange case is not p-periodic, so its least period is 2p.

**Independent arithmetic controls, without a run.** Output (001)^infinity has a cyclic one-run of length1 and the unique predecessor (101)^infinity. Output (011)^infinity has one gap of length2, hence two period-six predecessors: (001010)^infinity and its translate by three, as in G124's literal trajectory. Output (000111)^infinity has gaps 0,0,3 and no interchange; its two period-six predecessors are (000010)^infinity and (111001)^infinity. Their six literal triples give the same labeled output 000111. This last example is the unexpected guard: absence of a reset does not itself imply period doubling; the parity is essential. Constants cannot be put into the zero-gap rule unchanged.

**Tail implication and limit.** G149's backward periodic tail can now be classified at each step by reset presence and this parity, rather than only bounded by p or 2p. A reset fixes the tail independently of the finite head; without one, the head selects a surviving label, possibly only the phase of a doubled tail. This does not bound reset gaps across successive backward rows, determine the boundary-phase silver initial tail, or prove a forced wall has a finite head. The one-step criterion must not be iterated as though its gap counts stayed unchanged. No new run, finite witness or prize conclusion follows.

*Second reader's note on G150 (Local, 2026-10-07; chat L106).* Correct. I checked the gap-label table by hand from the
descending transitions: after a zero the surviving pair sets are $\{00, 11\}$ or $\{00, 01\}$. A run of ones of length
$0 \bmod 3$ returns to the first set with labels kept, one of length $2 \bmod 3$ ends in the second set with labels
exchanged, and a run of length $1 \bmod 3$ is G13's reset. The aligned counts follow from the cycle structure of the
period return map. Every whole-line predecessor is periodic because its cut states form a bi-infinite orbit of a finite
deterministic map. The counts were also checked by a method that does not use the reset machinery
(`rule30_audit_g99_g100.py`, S45). For every nonconstant cyclic output of least period at most 14 (32,474 outputs:
28,637 with a reset, 1,872 even, 1,965 odd), the left-to-right transfer matrix counts the predecessors on rings of size
$mp$ for $m = 1$ to 6. They are 1 for every $m$ with a reset, 2 for every $m$ with even parity, and 2 or 0 by the parity
of $m$ with odd parity, so no predecessor of period $3p$, $4p$, $5p$ or $6p$ exists anywhere in that range. The three
literal controls were checked as ring steps. GC167's caution stands: the criterion is exact for one step, and the gaps
change from row to row.

### G.GPT151. backward period doublings cannot be consecutive (second-read by Local, 2026-10-07)

### G151. Backward period doublings cannot be consecutive (2026-10-07)

**Status and target.** Symbolic tail-period refinement, independent review pending; G150 independently verified by Local L106. No experiment. Uses G150's two-label criterion and reviewed G13/G124. Prediction: a doubled predecessor necessarily acquires a reset, forcing the next backward step to preserve its period. Counterfactual: the bound p or 2p permits doubling at every backward nonconstant row. The reset argument excludes that possibility; it gives no upper bound on the delays between doublings or a wall-support conclusion.

Let y be a nonconstant periodic ordinary Rule30 row of least period p, and suppose its predecessor x has least period 2p. Then x contains a cyclic factor 010. Consequently x has exactly one whole-line predecessor z, with least period 2p. In particular no periodic backward chain has consecutive doublings between nonconstant rows.

**Proof.** By G150, y has no resetting zero gap, and an odd number of its cyclic runs of ones have length 2 modulo3. Choose one such run, whose length is at least two. At the cut just after the preceding zero the inverse recurrent pair set is C={00,11} or A={00,01}. Label 00 as zero and the other state as one. One p-period interchanges the labels. Thus in the doubled predecessor x, the selected cut takes both labels one p apart. At the occurrence with label zero, the actual adjacent input pair is 00. The first two driver ones give

    00 --1--> 01 --1--> 10.

The consecutive reconstructed input symbols are therefore 0,1,0. Reversing the spatial reading direction leaves 010 unchanged. Since x is a whole-line periodic row there is also a following symbol, so G13's reset factor 010z occurs. G150's reset case now gives exactly one predecessor of x, of the same least period 2p. This proves the claim without assuming any particular finite head or boundary bit.

**Improved zero-basin time bound.** If a nonconstant periodic pattern first reaches zero at physical time T>=2, the last two backward states are the all-one row and a period-three phase of 001. That period-three pattern has a cyclic 010 reset, so the next earlier pattern, if present, must also have period three. Beyond it, no two consecutive steps can double. Thus if the original least period is 3*2^a,

    a <= floor((T-2)/2),
    period <= 3*2^floor((T-2)/2).

This is stronger than G124/G149's a<=T-2 cap. In G149's setting, a compatible row becoming finite after k two-step iterates has a nonconstant zero-reaching eventual tail with

    a <= k-1,    period <= 3*2^(k-1),    k>=1.

If its periodic tail reaches zero earlier, apply the first-hit statement with that earlier T<=2k. Constant tails retain least period one. The former 3*4^(k-1) bound remains true but is superseded by this stronger bound; no reviewed text is invalidated.

**Independent control and unexpected sharpness guard.** The literal six-site trajectory extends G124 as

    101011 -> 001010 -> 011011 -> 010010 -> 111111 -> 000000.

The first arrow is checked by its six ordinary left-to-right triples, which give 0,0,1,0,1,0. The first two words have least period six; 011011 and 010010 have least period three. Read backward, the 3-to-6 doubling is followed by a 6-to-6 preservation, exactly as proved. Moreover 101011 itself has cyclic factor 010 (at positions 1,2,3), so its predecessor again preserves period six. The control prevents claiming that the upper bound is automatically attained by doubling every other step. No such matching all-depth construction is supplied.

**Scope.** This sharpens the periodic spatial zero basin and the conditional ancestors of finite compatible rows in G149. G123's canonical periods still have unbounded growth, and this theorem does not bound the gaps between their increases. It does not prove that the phase-zero silver tail is periodic, zero-reaching, finite or infinite. A new multi-row invariant or an actual all-depth tail classification is still required. No new computation, full right extension or prize conclusion follows.

*Second reader's note on G151 (Local, 2026-10-07; chat L107).* Correct, read jointly with G150. In the doubled case the
selected residue-two run sees both labels one period apart, and at the label-zero occurrence the pair is $00$; two
driver ones give $00 \to 01 \to 10$, so the reconstructed inputs read $0, 1, 0$, a run of one 1 between zeros, which is
G150's reset case for $x$. The time indexing is right: below the all-one row and the period-three phase of $001$ (which
itself contains $010$, forcing the next row back to period three) there remain $T - 3$ backward steps, so at most
$\lceil (T-3)/2 \rceil = \lfloor (T-2)/2 \rfloor$ non-consecutive doublings, and $a \le k - 1$ in G149's setting.
Checked (`rule30_audit_g99_g100.py`, S46): for all 672 doubling outputs of least period at most 12, both period-$2p$
predecessors (found by the descending recursion and confirmed forward) contain $010$ and have exactly one predecessor on
rings of size $2p$ and $4p$; on every ring up to size 24 (all 3,168 rows first reaching zero at time 2 or later; the
per-size cap was never hit) the period obeys $a \le \lfloor (T-2)/2 \rfloor$; and the six-site trajectory, with
$101011$'s own $010$.
*Correction (Local, 2026-10-07, chat L109).* "All 3,168 rows" was wrong: I checked that a sampling cap was never
hit and missed that the forward run stopped after $3n + 3$ steps. On the 24-ring 2,592 rows first reach zero later,
up to step 147. With the exact basin from a backward search the complete count of rows first reaching zero at time
2 or later, on rings up to 24, is 5,760, and every one obeys $a \le \lfloor (T-2)/2 \rfloor$.

### G.GPT152. rotation classes sharpen the periodic zero-basin first-hit bound (second-read by Local, 2026-10-07)

### G152. Rotation classes sharpen the periodic zero-basin first-hit bound (2026-10-07)

**Status and target.** Symbolic refinement, independent review pending. No experiment. Uses reviewed G123/G124. Prediction: quotienting translations sharpens the labeled-ring first-hit bound because a zero-reaching orbit cannot revisit a rotation class. Counterfactual: distinct labeled rows might require counting all their phases separately. An absorbing quotient argument removes those phases. Existing-record search found no necklace bound; necklace counting and cellular-automaton rotation quotients are established prior art, recorded in PRIOR-ART.md. No novelty claim for the method.

Let x be a nonconstant spatially periodic Rule30 row of least period p that first reaches zero at physical time T. By G124, p=3*2^a for some a>=0. Define L(q) to be the number of binary rotation classes of least period q. Then

    T+1 <= C_a := 2 + sum_(b=0)^a L(3*2^b),
    L(3)=2,
    L(q)=(2^q - 2^(q/2) - 2^(q/3) + 2^(q/6))/q  for q=3*2^b, b>=1.

In particular p=3 forces T<=3; p=6 forces T<=12. These are upper bounds, not assertions that each is attained.

**No repeated rotation class.** Write x_i=F^i(x), 0<=i<=T. Suppose x_j is a spatial translate of x_i for i<j<=T. On the p-cell ring the update commutes with rotations, so it induces a deterministic map on rotation classes. The class of x_i then lies on a cycle of length dividing j-i. It cannot subsequently enter the distinct absorbing class of zero. If the class already is zero, the first-hit property instead gives i>=T, impossible. Thus all T+1 classes are distinct. This uses no assumption that the cellular automaton is injective.

Every intermediate row reaches zero and has spatial period dividing p. G124 therefore permits only least period one or 3*2^b, 0<=b<=a. Period one contributes precisely the constant zero and constant one classes. Counting all binary classes of the remaining permitted periods gives C_a; some counted classes may lie outside the zero basin, so the inequality can be strict. A primitive word of length q has q distinct rotations even when repeated on a larger p-cell ring. There is no additional factor p/q in the class count.

**Counting derivation.** If A(q) counts labeled binary words of least period q, then 2^q=sum_(d|q) A(d). Divisor inversion gives A(q)=sum_(d|q) mu(d)*2^(q/d), where mu is the ordinary Moebius function. Dividing by q gives L(q). For q=3 the only squarefree divisors are 1,3. For q=3*2^b, b>=1, they are 1,2,3,6; their signs give the displayed formula. This is the standard primitive-necklace formula, not a new counting identity.

**Asymptotic consequence.** Along p=3*2^a tending to infinity, C_a=(1+o(1))*2^p/p. The largest term L(p) has that asymptotic by its explicit formula; all smaller terms together are at most a*2^(p/2), whose ratio to 2^p/p tends to zero. Hence along zero-reaching rows with T tending to infinity,

    p >= log2(T+1) + log2(log2(T+1)) - o(1).

Indeed log2(T+1)<=p-log2(p)+o(1), while the original labeled-ring count gives p>=log2(T+1); substituting that lower bound inside log2(p) yields the claim. G123's canonical ancestor tail C_n first reaches zero at time n, so the same bound applies to its p_n. This improves a generic counting floor; it gives no upper bound on doubling gaps or a temporal-wall exclusion.

**Independent arithmetic control and unexpected guard, by hand.** The two primitive period-three classes are represented by 001 and 011. The literal trajectory 011 -> 010 -> 111 -> 000 visits both classes (010 is a rotation of 001) and then the two constants; T=3 attains C_0-1. At period six the four-term formula gives (64-8-4+2)/6=9, so C_1=2+2+9=13. Counting labeled primitive words would instead give 54 and miss the rotation reduction. As the identified unexpected scope check, the stationary checkerboard has least period two and revisits its rotation class forever: the no-repeat argument requires eventual absorption at zero, not mere periodicity or finite ring size. None of these controls is a numerical run.

**Scope.** This is a necessary first-hit bound for periodic spatial tails and the reviewed canonical ancestry. It neither constructs a finite compatible wall head nor identifies the silver phase-zero forced tail. The all-depth wall-tail obligation remains open.

*Second reader's note on G152 (Local, 2026-10-07; chat L109).* Correct. The rotation quotient is deterministic because
the update commutes with rotations; a revisited class would lie on a cycle of the quotient, and the zero class is a
fixed absorbing class, so a revisit forces the class to be zero before the first hit. Every row on the trajectory
reaches zero and has period dividing $p$, so G124 leaves only the constants and the primitive periods $3 \cdot 2^b$,
$b \le a$. The Moebius count is the standard primitive-necklace formula, with $L(3) = 2$, $L(6) = 9$ and $L(12) = 335$.
The asymptotic substitution is right: the smaller terms total at most $a \, 2^{p/2}$, which is negligible against
$2^p/p$, and $\log_2 p \ge \log_2 \log_2 (T+1)$ follows from the labeled count. Checked (`rule30_audit_g99_g100.py`,
S47): the three necklace counts by brute force; on rings of size 3, 6, 12 and 24 every zero-reaching row's trajectory
visits distinct rotation classes, all of allowed periods, with $T + 1 \le C_a$; and the period-three trajectory
attaining $C_0 - 1 = 3$. The largest first-hit times are 3, 10, 17 and 147, far inside the bounds 4, 13, 348 and
699,218. Writing S47 exposed a fault in my S44 and S46 ring censuses, which stopped each row after $3n + 3$ steps; all
three checks now use the exact basin from a backward search (corrections in the G149 and G151 notes).

### G.GPT153. Rudin–Shapiro passes the necessary repeat-debt filter (second-read by Local, 2026-10-07)

### G153. Rudin–Shapiro passes the necessary repeat-debt filter (2026-10-07; computer-assisted theorem)

**Status.** Computer-assisted theorem, independently verified by Local L111 at 8f7841c. The direct RSP-S semantic reconstruction and debt-product argument have been audited and independently replayed; the Walnut compilation dependency is discharged. RSP preregistration was pushed at dd61eb5 before runs. No finite-left realization or prize claim. The raw universal decision is TRUE and an independently implemented graph-product check agrees, conditional on the compiled repeat predicate's semantics. The standard automatic-sequence logical decision theorem is the prior-art method, not a new technique.

Let r(n) be the parity of overlapping occurrences of11 in the binary representation of n, r(0)=0. Proposed statement: for every a,b>=0 and q>=1, if r(s)=r(s+q) for all a<=s<=b with b>=a, then

    b <= 2*a+q.

Thus Safe(0) and Bounded in the RSP plan hold. This is a necessary-filter pass, not a candidate construction. RSP2 was not run because a verified Safe(0) would already settle Bounded positively.

**Certificate chain.** The four-state output automaton remembers the last binary digit h and the parity e. Reading d updates (h,e) to (d,e XOR h*d); induction on digits proves the definition of r, including leading-zero padding. Pinned Walnut7.1.0 source commit67e69c248d07324b25de1d4a498e877ac504999a compiled the exact RSP predicate

    q>=1 AND b>=a AND FOR ALL s:
        (a<=s AND s<=b) IMPLIES r(s)=r(s+q)

into a deterministic78-state automaton over synchronized most-significant binary digits of (a,b,q). Its exported file SHA256 is1a0f3ac7b9222da522c2077b1dbeccb8098bc9df15a1200af6920a2243f309b6. Review artifacts rsp-repeat-dd61eb5.txt and rsp-product-dd61eb5.json are in the shared scratch; bulk outputs stay outside Git. The formula, driver and replay verifier are in tests/probes/prizes/rudin_shapiro_repeat.py.

The independent checker intersects that exported relation with a separately derived debt comparator. After a digit triple, the signed prefix debt d=b-2a-q updates to 2*d+b_bit-2*a_bit-q_bit. Values at most-1 stay negative under all later digits; values at least3 stay positive. Saturation to the five states -1,0,1,2,3 is therefore exact, with final d>0 accepting. Breadth-first traversal of the product has84 reachable states and no accepting state. Closed reachability proves emptiness for all finite digit strings, not a finite integer horizon. This product check alone does not establish the compiled relation's semantics. The separate RSP-S reconstruction, audited and replayed by Local L111, discharges that dependency for this exported relation. Walnut's separately compiled universal formula also returned TRUE.

**Controls and failures.** RSP0 passes: the supplied generator versus the integer bit-count formula at0..4095 and189 selected64-bit carry-boundary inputs;2040 admissible literal repeats through a,b<=15 and q<=15; constant-zero and alternating Bounded=FALSE controls; and G137's powers-of-two Safe(0)=TRUE control. An expanded4096-tuple replay includes q=0 and reversed ranges and checks three additional leading zeros. The debt comparator matches32768 independent integer comparisons through31. These finite controls check instruments, not the universal theorem. The identified unexpected padding check is supplemented by the initial all-zero-digit self-loop and unbounded finite-graph traversal; no fixed bit width is used.

The first RSP0 run failed because Walnut resolves command filenames inside its command directory; the absolute positional filename was invalid. That failed run is retained, lookup corrected, and RSP0 completed before RSP1. Python's toolchain metadata request also failed its certificate-store check; system curl succeeded without disabling TLS. A checksum-verified portable Java archive and isolated tool/dependency caches were used, with no system-runtime installation. Formula processes had120 CPU-second limits,768MiB Java heap bounds,1GiB sampled-RSS termination checks and an additional180-second wall limit. No limit was approached: successful formulas took about0.42 seconds wall each, with sampled peak RSS below50MiB. Resource samples are not exact peak-memory measurements. No Local computational job was duplicated.

**Scope and next obligation.** After independent review, the ordinary repeat-filter exclusion route is closed for this specific automatic word. Its forced initial tail and full right extension remain unresolved. Passing this necessary inequality is neither finite evidence for support nor a theorem that a compatible finite row exists.

*Second reader's note on G153 (Local, 2026-10-07; chat L111).* Correct as a computer-assisted theorem, with the semantic
dependency on Walnut discharged. The definition, the inclusive endpoints and the quantifiers match the RSP plan and
G135's convention, and the first interval $[0, 1]$ at period 1 has debt exactly 0, so $C = 0$ is tight. I audited
RSP-S's three steps. The carry completion holds, since $s \le b$ fits the input width and $s + q$ needs at most one more
digit, so one implicit zero digit closes the carry and the last adjacent pair. The reversal holds: reversing the
exported automaton makes its accepting states the starts and its initial state the target, and a simultaneous subset
search that closes decides language equality for every nonempty input. The adjacent-11 parity is the same in either
reading direction. The saturated debt comparator is exact, since $2(-1) + 1 < 0$ and $2 \cdot 3 - 3 \ge 3$. Checked in
code sharing nothing with GPT's (`rudin_shapiro_review.py`). RV1: the exported relation agrees with brute force on all
$32^3$ triples at two paddings. RV2: my own debt product on it reaches 84 states and no violation. Reproduced on this
machine: RSP-S's equivalence closing at 17,033 states with the mutation caught at $(0, 0, 0)$, and G153's replay with 84
product states. Both GPT scripts need Python 3.10 or later for `int.bit_count`, and this machine's default is 3.9. My
first attempt, an independent most-significant-digit construction, was stopped at 3 GB while still determinising once
GC177 showed GPT had closed that lane; it is kept in the script's docstring. The scope stands as written: this closes
the repeat-filter route for this word at this start, and says nothing about its forced tail.

### G.GPT154. finite-tail exceptions in a minimal trace family are empty or countable dense (second-read by Local, 2026-10-07)

### G154. Finite-tail exceptions in a minimal trace family are empty or countable dense (2026-10-07)

**Status and target.** Symbolic scope audit, independently verified by Local L112; no computation. Uses reviewed G140's wall coding and radius clock, and generalizes G147's phase-counting argument to a minimal trace family. This is an elementary dynamical argument, not a novelty claim about substitution systems. Prediction: generic infinite support cannot exclude the original Rudin–Shapiro trace. Counterfactual: minimal recurrence plus a generic exclusion forces every individual trace to have an infinite tail. The conditional dense-exception argument below shows why that inference fails. G153 and its RSP-S certificate are not assumed in this proof.

Let X be a nonempty compact, forward-shift-invariant family of one-sided visible binary words in which every forward orbit is dense. Assume X is infinite. Under G140's bijection Phi from visible words to compatible white-phase initial rows, set

    E_X = {c in X : Phi(c) has finite left support}.

Then E_X is empty or countable dense in X. Its complement is residual and has full measure for every shift-invariant probability measure on X. For each fixed radius L, at most 2^L words of E_X have radius at most L. None of these statements excludes a specified word of X.

**Proof.** There are at most 2^L binary rows supported in the first L cells. Injectivity of Phi gives the same bound for words, so E_X is countable. The conjugacy F Phi = Phi shift and finite-support preservation show that E_X is forward invariant. If nonempty, it contains a dense forward orbit and hence is dense. On that orbit radii increase by exactly two at each shift.

An infinite minimal compact trace family has no eventually periodic points: such a point would yield a finite periodic orbit in X, whose dense orbit would force X to be finite. It also has no isolated points. If a cylinder isolates c, minimality supplies a positive return of c to that cylinder, forcing shift^n(c)=c. More explicitly, compactness gives a finite cover by inverse images of that cylinder; applying the cover to shift(c) supplies the positive return. The resulting periodic point contradicts infinitude. Thus each singleton is nowhere dense, and countability makes E_X meagre. For an invariant probability measure, an atom at c would give every distinct forward image mass at least that atom's mass, since the preimage of the image contains c. Infinitely many such images contradict total mass one. Hence every such measure is nonatomic and E_X is null. This argument does not require Phi to preserve a preferred measure.

**Rudin–Shapiro supplies such an X.** Write r(n) for adjacent-11 parity. Appending a binary digit gives r(2n)=r(n) and r(2n+1)=r(n) XOR (n modulo 2). The pair (r(n),n modulo 2) is the fixed word starting at a of the substitution

    a -> ab, b -> ad, c -> cd, d -> cb,
    a=(0,0), b=(0,1), c=(1,0), d=(1,1).

Its directed graph reaches a from every letter in at most three steps and reaches every letter from a in at most three; the a self-loop pads each composed path to exactly six. Thus every sixfold substituted letter contains every letter. Any factor of the fixed word occurs inside some substituted prefix of a; consequently every sufficiently large substituted letter contains it. The fixed word is tiled by equal-length such substituted letters, so every sufficiently long factor contains that chosen factor. Projecting to the first coordinate preserves this bounded-gap property. The binary shift closure X_r is therefore minimal: every factor of r occurs in every member with bounded gaps, so every forward orbit meets every cylinder of X_r.

For completeness r is not eventually periodic. For m<2^(k-1), the separated binary blocks give r(2^k+m)=r(m) and r(3*2^k+m)=1 XOR r(m). If r were eventually q-periodic, taking k arbitrarily large in the first identity transfers that periodicity to every initial m, making it purely q-periodic. Now choose k with 2^(k-1)>q. The first identity at m=0 through q-1 says translation by 2^k fixes the entire q-periodic word; translation by 3*2^k must then fix it too. The second identity at m=0 contradicts that, since r(0)=0 and r(3*2^k)=1. Thus X_r is infinite and the stated dichotomy applies.

**Unexpected periodic-family check.** If X is instead a finite periodic orbit, E_X is empty: a finite row corresponding to a p-periodic visible word would return after p applications of F, contradicting radius growth by 2p. The all-zero visible control gives the infinite checkerboard initial tail, not a finite row. This verifies why temporal simplicity is not a spatial-support certificate.

**Scope.** For Rudin–Shapiro, generic members of its binary shift closure have infinite forced initial tails, independently of the pending repeat-filter decision. If even one member has finite support, its dense shift orbit has growing finite radii and remains fully consistent with generic infinite support and infinite-support accumulation points. The original r is a specified member; this argument neither excludes it nor constructs an exception. The missing obligation remains a direct spatial-tail constraint on Phi(r), and full right extension is separate. No prize claim.

*Second reader's note on G154 (Local, 2026-10-07; chat L112).* Correct; every hypothesis is stated and used. The
substitution follows from appending a digit: $r(2n) = r(n)$ and $r(2n+1) = r(n) \oplus (n \bmod 2)$, so a letter
$(r, p)$ becomes $(r, 0)(r \oplus p, 1)$, which is $a \to ab$, $b \to ad$, $c \to cd$, $d \to cb$. Its graph reaches $a$
from every letter and every letter from $a$ within three steps, and the loop at $a$ pads to exactly six, so the sixth
power is positive. Uniform recurrence of the fixed word passes to its first coordinate because a factor of $r$ is the
projection of the factor of the pair word at the same positions. Minimality then gives the two generic statements. An
isolated point would return to its own cylinder and be periodic, so singletons are nowhere dense. An atom would put at
least its mass on every distinct forward image, since each image's preimage contains the point. The block identities
need $m < 2^{k-1}$ so that the digit after the leading 1 or 11 is 0, and both proofs use exactly that. One sharpening,
as in G147: by GC156's free odd depths, at most $2^{\lceil L/2 \rceil}$ words of $E_X$ have radius at most $L$. Checked
(`rule30_audit_g99_g100.py`, S48): both digit recurrences for $n < 2^{14}$; the pair word equals the substitution's
fixed word on $2^{14}$ letters; the sixth power of the letter matrix is positive; and the separated-block identities for
$k \le 12$.

### G.GPT155. trace factor complexity bounds the number of finite-tail exceptions (second-read by Local, 2026-10-07)

### G155. Trace factor complexity bounds the number of finite-tail exceptions (2026-10-07)

**Status and target.** Symbolic deduction, independently verified by Local L113; no computation. Uses reviewed G139 inverse locality, G140 coding/radius growth and G154 (Local L112). The record search found G147/G154's exponential fixed-radius count and G139's fixed-depth temporal factor bound, but not this growing-radius exception count. This is an elementary application of substitution factor counting, not a new general complexity theorem. Prediction: Rudin–Shapiro's exception count is at most linear in radius. Counterfactual: temporal zero entropy alone resolves whether there is even one finite-tail exception; the matching conditional lower bound shows the remaining gap.

For a forward-shift-invariant trace family X, let P_X(k) count its length-k factors and N_X(L) count c in X whose compatible initial row Phi(c) has radius at most L. For integers L>=1, put k=ceil(L/2). Then

    N_X(L) <= P_X(k).

**Proof.** G139's inverse recurrence determines the first L initial cells from the visible prefix c_0 through c_(k-1): the physical-time determining window at depth j is [0,j-1], containing exactly ceil(j/2) even samples. Thus two visible words sharing their first k bits have identical initial rows through depth L. If both rows are zero beyond L, the entire rows agree; injectivity of Phi makes the words identical. Hence the exceptional words inject into their length-k prefixes, a subset of X's factors. This also proves Local L112's sharper universal bound 2^k, without assuming that different arbitrary length-k prefixes necessarily produce different length-L rows.

**Rudin–Shapiro bound.** Use G154's four-letter length-two fixed substitution word. For k>=1 choose m minimal with h=2^m>=k; then h<2k. Any length-k factor fits inside two consecutive level-m substituted letters, with its start at one of h offsets in the first. There are at most sixteen ordered letter pairs. Projection to the binary word cannot increase this count, so

    P_(X_r)(k) <= 16*h < 32*k,
    N_(X_r)(L) < 32*ceil(L/2).

This is a deliberately coarse all-length bound, not a claim about the exact known factor complexity. If a finite-tail exception c of radius R exists, its time shifts have distinct radii R+2t. For L>=R this gives

    N_(X_r)(L) >= floor((L-R)/2)+1.

Consequently N_(X_r) is either identically zero or grows linearly in L, with matching upper and conditional lower orders. No existence has been supplied.

**Unexpected endpoint check.** Replacing ceil(L/2) by floor(L/2) is wrong. At depth three G138 gives v_3(0)=1-c_1: words with the same c_0 but different c_1 have different depth-three cells. At even depth four the determining prefix has two symbols, as v_4(0)=c_0*c_1. Thus the count uses the actual growing window, not a fixed-depth entropy limit or an omitted endpoint. The bound is compatible with a dense countable exceptional set and unbounded radii from G154.

**Scope.** This counts hypothetical finite-tail rows within the Rudin–Shapiro family. It excludes neither the original word nor any specified shift and gives no full right extension. The necessary count is linear, not positive entropy. A spatial invariant forcing N_(X_r) to be zero is still missing; another prefix census cannot establish that invariant. No prize conclusion.

*Second reader's note on G155 (Local, 2026-10-07; chat L113).* Correct. The determining window is the one from my G140
note: depth $j$ at time 0 needs the wall-neighbour column at times 0 to $j - 1$, whose even times carry
$\lceil j/2 \rceil$ visible letters, so two words sharing $\lceil L/2 \rceil$ letters share the row through depth $L$.
Two finite rows that agree through $L$ and vanish beyond it are equal, and injectivity of $\Phi$ finishes. The two-block
coverage holds because the fixed word is tiled by level-$m$ blocks of length $h \ge k$, so a factor of length $k$ lies
in two consecutive blocks and is fixed by the pair and an offset. The lower bound uses the radius clock, and the
depth-three endpoint check is right. Checked (`rule30_audit_g99_g100.py`, S49): on 60 random words, for $L$ up to 40,
changing any letter from position $\lceil L/2 \rceil$ on leaves depths 1 to $L$ unchanged, while changing letter
$\lceil L/2 \rceil - 1$ changes depth $L$ when $L$ is odd. Depth 3 is $1 - c_1$ and depth 4 is $c_0 c_1$, and on
$2^{18}$ letters of $r$ the factor counts obey $P(k) \le 16h < 32k$ for $k \le 64$. Descriptive: those counts equal
$8k - 8$ at every tested $k$ from 8 to 64, the value I recall from the automatic-sequences literature for Rudin–Shapiro
(not re-read here). If that value holds, the exception count is at most $8 \lceil L/2 \rceil - 8$ once
$\lceil L/2 \rceil \ge 8$.

**Source-checked refinement (GPT GC184; Local L114 checks the transfer).** Allouche and Shallit1993, Theorem1, gives P_r(k)=8k-8 for k>=8 for the exact substitution and binary coding used here. Consequently N_(X_r)(L)<=8*ceil(L/2)-8 for L>=15. For k=ceil(L/2)=1..7 use2,4,8,16,24,36,46 instead; the affine formula is not asserted below8. The published base enumeration is accepted, not independently rerun. See PRIOR-ART.md for the primary source and scope. This changes only the upper constant, not existence or the zero-or-linear dichotomy.

### G.GPT156. temporal rotation classes sharpen the fixed-period edge-history bound (second-read by Local, 2026-10-07)

### G156. Temporal rotation classes sharpen the fixed-period edge-history bound (2026-10-07)

**Status and target.** Symbolic edge-diagonal proof, independent review pending; no computation. Returns to Q7's open period-growth/settling lead, distinct from Local's G155 review. G7 already proves the absolute-profile tree bound K<=4^P-1. Prediction: counting temporal rotations gives a stronger bound of order 4^P/P. Counterfactual: rotation-equivalent pairs can occur at different edge depths despite the absorbing zero boundary. The first-hit argument excludes that. The small-period controls below are literal finite graph proofs, not a sampled census.

Let K count a compatible prefix w_0 through w_(K-1) of P-periodic diagonal profiles rooted at (w_(-1),w_0)=(0,1^P). On pairs define

    B(a,b)=(S b XOR (a OR b),a),

with cyclic time shift S. G7's diagonal equation gives B(w_(j-1),w_j)=(w_(j-2),w_(j-1)). The zero pair is fixed, and the root maps to it. Thus the pair at depth j has first zero-hit time j+1: an earlier zero would force the root to be zero after further applications. B commutes with temporal rotation, so rotation-equivalent pairs have the same first-hit time. Pairs at different depths are therefore inequivalent even after rotation. Including the zero class gives

    K+1 <= N_4(P),
    N_4(P) = (1/P) * sum over d dividing P of phi(d)*4^(P/d).

Here N_4(P) counts cyclic words of length P over the four-letter pair alphabet. For a rotation by h, a fixed pair word has gcd(P,h) freely chosen letters, hence 4^gcd(P,h) possibilities. Averaging fixed counts over the cyclic group and grouping equal gcd values gives the displayed standard necklace formula. All periods dividing P are included; using only primitive necklaces would undercount.

For P>=2 the nonidentity contribution is at most (P-1)*4^(P/2)/P. Consequently N_4(P)=(4^P/P)*(1+o(1)). Along prefixes with K tending to infinity this strengthens G7's lower period floor to

    P >= log_4(K)+log_4(log_4(K))-o(1).

It is a lower bound on period, not an upper bound or a waiting-time budget.

**Period-one control.** N_4(1)=4. The root path (0,1),(1,1),(1,0) contains three pairs; each maps backward to its predecessor and then zero. The last pair has no constant-profile child. Thus K=3 attains the bound.

**Unexpected nonabsorbing-class check, period two.** Encode two-bit temporal words with the least significant bit at time zero. S swaps1 and2, fixes0 and3. The pairs (1,2) and (2,1) form a B-cycle and are rotations of one another, so their single rotation class cannot lie on a rooted edge history. N_4(2)=(16+4)/2=10; excluding zero and this additional class gives K<=8. The eight-pair path

    (0,3),(3,3),(3,0),(0,1),(1,3),(3,1),(1,1),(1,0)

attains it. Substitution in B sends each pair to the preceding one and the first to zero. Hence the maximum common-period-two rooted prefix has K=8. This check both tests the quotient convention and prevents mistaking every necklace class for an absorbing class.

**Prior-art map distinction.** Re-read Nersissian's section4 through Theorem13: its backward map B is exactly G7's edge-diagonal map, and its absolute-profile first-hit argument is the same mechanism. The earlier vertical-wall audit remains correct: that inverse shifts the first coordinate rather than the second and is a different map. The paper's profile bound is not a new wall theorem; the rotation quotient here applies directly to the diagonal tree. Standard necklace counting was already recorded for G152. No novelty is claimed for that counting method.

**Scope.** This improves the necessary period lower bound for every compatible edge branch and certifies the two smallest controls. It supplies no sublinear upper period growth, no adaptive waiting bound below slope3, no finite-left exclusion and no prize result. Q7's all-branch settling obligation remains open. No period16 graph, new ring census or Local computational job is requested.

*Second reader's note on G156 (Local, 2026-10-07; chat L114).* Correct. The indexing is right: $K$ words give $K$ pairs
including the root $(0, 1^P)$, the pair at depth $j$ first hits zero at $j + 1$ because an earlier zero would make the
root zero, and $B$ commutes with rotation, so distinct depths lie in distinct rotation classes. The count must be of all
necklaces, since a pair can have a smaller period, and the Burnside formula is the right one. I traced both controls by
hand: the period-one path stops after $(1, 0)$, and every arrow of the period-two path maps to its predecessor, with
$(1, 2)$ and $(2, 1)$ forming a rotation class on a 2-cycle. Checked exhaustively (`rule30_audit_g99_g100.py`, S50) for
every $P \le 7$ over all $4^P$ pairs: rotation commutes with $B$; the rooted tree's depths lie in distinct classes;
$K + 1 \le N_4(P)$; $K = 3$ and 8 at $P = 1$ and 2; and the same results with the time shift taken in either direction.
Descriptive, not part of G156: the longest $K$ is 3, 8, 3, 29, 3, 8, 3 for $P = 1$ to 7, against bounds 4, 10, 24, 70,
208, 700, 2344. So the deepest branch depends only on the power of two in $P$, odd periods add nothing beyond the
constant path, and $P = 6$ repeats $P = 2$. This is consistent with the powers-of-two periods of Jen's theorem on these
diagonals (§8.13).

### G.GPT157. odd factors do not enlarge the rooted edge-history tree (second-read by Local, 2026-10-07)

### G157. Odd factors do not enlarge the rooted edge-history tree (2026-10-07)

**Statement.** Let P>=1 and Q=2^v, where v is the exponent of two dividing P. The common-period-P rooted tree of G7 is isomorphic to the common-period-Q tree: repeat each Q-bit temporal word P/Q times. This preserves depth, the predecessor B, zero hits and temporal rotation classes. In particular its maximum prefix length K is identical, and G156 sharpens to

```math
K+1\le N_4(Q)=\frac1Q\sum_{d\mid Q}\varphi(d)4^{Q/d}.
```

Every odd P has exact maximum K=3; every P with v=1 has exact maximum K=8. These are finite-tree statements, not a bound on physical transient lengths.

**Proof.** A child c of the adjacent pair (a,b) obeys

```math
c(t+1)=a(t)\oplus\bigl(b(t)\vee c(t)\bigr).
```

Suppose a and b have a common dyadic period d. If b has a one, a reset at t0 fixes c(t0+1)=a(t0) XOR1 independently of c(t0). The same reset occurs at t0+d, so c agrees with its d-shift immediately after the reset and thereafter by the recurrence. For any integer t choose an earlier reset; hence the entire periodic word c has period d. If b is zero, summing d steps gives c(t+d)=c(t) XOR sigma, where sigma is the parity of one d-block of a; in particular c has period 2d. Starting from the constant root, induction makes every profile's least period a power of two. Each profile is also P-periodic, so its least period divides P and therefore divides Q.

Restrict every profile to its first Q letters. Since all have period Q, restriction commutes with shift, OR, XOR and B. Conversely repetition embeds any Q-periodic rooted history in the P-periodic tree. The two maps are inverse on every node and edge, and a rotation by t on either side depends only on t modulo Q. Thus the entire rooted trees and their rotation quotients agree. Apply G156 at Q. Its literal Q=1 and Q=2 controls supply the asserted exact maxima. Square.

**Controls and identified unexpected check (symbolic, no run).** Local L114's P=3,5,7 maxima3 and P=6 maximum8 follow exactly, rather than merely fitting a pattern. At P=6 the necklace upper bound drops from700 to10; excluding the known nonabsorbing class gives exact K=8. The rooted hypothesis is essential: the ambient period-three pair (0,100), with the cyclic word written in temporal order, has least pair period3 and cannot be reduced to Q=1. It is excluded by the rooted induction, not by an assertion that all periodic B-states are dyadic. This is the unexpected scope guard.

**Prior art and limits.** This is an explicit finite-tree corollary of the reset/integration mechanism in Nersissian, section4, Theorems10-12 (read directly); that source attributes dyadic diagonal periods to Jen. No novelty is claimed for period doubling or the reset proof. The source's initialized physical tails do not alone establish equality of our arbitrary-phase rooted trees, so the two-sided periodic argument above supplies that transfer. This does not identify maximum K at Q>=4, control actual settling times, establish an upper period-growth law, or solve a prize problem. No computational experiment was launched.

*Second reader's note on G157 (Local, 2026-10-07; chat L115).* Correct. The two-sided reset argument holds on the cyclic
group: when $b$ has a one, the same reset recurs every $d$ steps, so $c$ agrees with its $d$-shift after every reset,
and every time is preceded by one. When $b = 0$, integration over a block gives $c(t+d) = c(t) \oplus \sigma$. From the
constant root, induction keeps every least period a power of two, which divides $P$ and so divides $Q$. Restriction to
$Q$ letters commutes with the shift, OR, XOR and $B$, and repetition inverts it, so the trees and their rotation
quotients coincide. Checked (`rule30_audit_g99_g100.py`, S51) for every $P \le 15$, building each rooted tree from its
children: every profile has a dyadic least period dividing $Q$, restriction maps the $P$-tree's nodes bijectively onto
the $Q$-tree's with depths kept, and the longest $K$ is that of $Q$. By-product, not claimed by G157:
$K = 3, 8, 29, 400$ for $Q = 1, 2, 4, 8$, the last from a tree of 3,065 nodes. A first draft also built $P = 16$; it ran
past ten minutes and was stopped, nothing concluded.
*Correction (Local, 2026-10-07, chat L119).* The heights $3, 8, 29, 400$ given above as a by-product were already
in the record as G2.3's common-period doubling points, and G2.3 also certifies the first genuine branch at diagonal
53,208; the by-product reproduces it and is not new.

### G.GPT158. only even-parity integration branches the temporal-rotation quotient (second-read by Local, 2026-10-07)

### G158. Only even-parity integration branches the temporal-rotation quotient (2026-10-07)

**Statement.** Quotient G7's common-period-P rooted tree by simultaneous temporal rotation of each adjacent pair. It remains a finite rooted tree. At a node represented by (a,b), its number of child classes is classified as follows:

- If b is nonzero, there is exactly one child class.
- If b=0, write q for the least period of a and sigma for the parity of one q-block. The two words cannot both be zero. For sigma=0 there are exactly two child classes, both of least word period q.
- For sigma=1 and 2q dividing P, there is exactly one child class: the two literal children, of least period2q, differ by a rotation through q.
- For sigma=1 and 2q not dividing P, there are no children.

By G157, q is dyadic and divides Q=2^v2(P), so the final case means q=Q. Thus genuine branching in the quotient occurs precisely at even-parity zero-driver nodes; leaves occur precisely when odd-parity integration would exceed the allowed dyadic period. In particular, if E counts the even-parity zero-driver node classes and L counts leaf classes, then L=E+1. Period doubling itself supplies no new branch choice after phase quotienting.

**Proof.** Rotation commutes with B. Every node orbit has a unique predecessor orbit. Distinct depths cannot coincide by G156's first-zero-hit argument; no reconvergence is possible because predecessors are unique. The root is rotation invariant. Hence the quotient is a finite rooted tree. To find its children, rotate any child so that its parent is a chosen representative. Two representative children give the same orbit exactly when a rotation preserving that parent exchanges them.

An active driver b resets the scalar recurrence, as in G157: one complete driver period determines the unique periodic solution c. It has period dividing a common period of a and b, hence divides P. There is one child, before as well as after quotienting.

For b=0 the equation is c(t+1) XOR c(t)=a(t). Choosing c(0) gives exactly two complementary solutions. Summing q steps gives c(t+q)=c(t) XOR sigma. If sigma=0, both solutions are q-periodic. Their least periods are exactly q: any period of c is a period of its difference a, so it must be divisible by q. If sigma=1, their least periods are exactly2q for the same reason, and their q-shifts are their complements. Such solutions close at period P if and only if2q divides P.

Finally the stabilizer of (a,0) consists precisely of shifts divisible by q. For sigma=0 those shifts fix each child and cannot exchange the complementary solutions; for sigma=1 a shift by q exchanges them. This proves the child-class counts. A finite rooted tree with outdegrees0,1,2 has L=E+1 by counting edges in two ways. Square.

**Symbolic controls and identified unexpected check.** At P=1, the three G156 nodes form one chain and the last node (1,0) is the excluded-doubling leaf. At P=2, a nonzero word of least period1 has odd block parity, and a binary word of least period2 is01 or10, also odd. There are therefore no even-parity branch nodes; the quotient is one chain, with its eight nodes given by G156. The apparent first doubling is two phase copies of one continuation.

The unexpected even-parity guard is a=0110, of least period4: with b=0 its solutions are c=0010 and1101. Their child pairs are not rotation equivalent, because any rotation fixing the parent a is a multiple of4. This is a local transition check, not a claim that this parent lies in the rooted tree. By contrast a=01 integrates to0011 and1100, exchanged by rotation through2. Confusing these two parity cases would erase actual possible quotient branching.

**Prior art and scope.** The scalar reset/integration classification is the existing mechanism of Nersissian section4, Theorems10-12, and G7. The additional statement here classifies child orbits using the parent stabilizer; the record's G152 spatial quotient is different and need not be a tree. G157 is a pending proof dependency for the dyadic leaf identification, while the child-orbit calculation above holds without that dependency whenever a is periodic. No novelty is claimed for reset, integration or elementary tree counting. No new computation, larger graph census, uniform bound on E, period-growth upper bound, physical settling bound or prize solution is asserted.

*Second reader's note on G158 (Local, 2026-10-07; chat L115).* Correct. A rotation taking one child $(0, c_1)$ to
another $(0, c_2)$ must fix the parent, since $B$ commutes with rotation and both children map to $(a, 0)$. So the
relevant rotations are the shifts by multiples of $q$. They fix each $q$-periodic solution when $\sigma = 0$, and
exchange the two complementary solutions when $\sigma = 1$. The leaf count $L = E + 1$ is edge counting in a tree with
outdegrees at most 2. Checked (`rule30_audit_g99_g100.py`, S52): on the rooted trees for $P \le 15$, every node's
child-class count follows the rule, leaves exceed branch classes by one, and $P = 1, 2$ are chains. Because those trees
turned out to contain no even-parity branch at all, the rule was also checked ambiently at every pair of $P$-periodic
words for $P \le 8$, including 236 pairs with two child classes. The two local guards check in time order.

### G.GPT159. genuine quotient branches are separated by at least seven depths (second-read by Local, 2026-10-07)

### G159. Genuine quotient branches are separated by at least seven depths (2026-10-07)

**Statement.** On any rooted periodic edge history, two consecutive even-parity zero-driver branch nodes of G158 have depth difference at least7. Consequently the number of temporal-rotation classes at depth n in the common-period-P tree is at most2^ceil(n/7). This is a branch-choice rate bound, not an upper bound on the height of the tree or on physical waiting times.

**Proof.** At an even-parity branch write the profiles starting at its zero driver as0,c,d,e,f,g,h. The previous profile a is nonzero and satisfies Delta c=a, so c is nonconstant. The equation for d is S d=c OR d. A one in the periodic c resets d to1; thereafter1 persists. Periodicity therefore forces d=1. Next S e=1 XOR c, so e is nonconstant. If f=0, its equation S f=1 XOR(e OR f) would force e=1, impossible. Thus profiles c,d,e,f are all nonzero.

If g=0 then its equation forces e=f. Substituting in the equation for f gives S e=1 XOR e, so e and c are alternating and a=Delta c=1. But the constant-one profile has least period1 and odd block parity; it cannot be the even-parity branch under consideration. Hence g is nonzero.

If h=0 then f=g, and the equation for g gives e=f XOR S f. The equation for f is S f=1 XOR(e OR f). At any time with f=0 these two identities imply S f=1 XOR S f, a contradiction. Thus f must be constant1; then its equation would give S f=0, another contradiction. Hence h is nonzero. No zero-driver node occurs in the next six depths, proving the spacing claim.

A path from the root to depth n crosses at mostceil(n/7) binary branch nodes. By G158 all other nodes have at most one child in the rotation quotient. The binary decision words for distinct depth-n nodes are prefix-free (a proper prefix would give the same path until one node already ended at depth n). A prefix-free collection with maximum word length m has at most2^m members, by extending its words to disjoint sets of m-bit strings. Take m=ceil(n/7). The case n=0 has the single root. Square.

**Controls and identified unexpected check (symbolic, no run).** The constant-one predecessor is essential: odd-parity integration gives an alternating c, and the resulting segment0,c,1,c,c,0 has zero drivers only5 depths apart. This is exactly the period-two control and rejects extending the seven-depth claim to all zero drivers. The even-parity local guard a=0110 from G158 is nonconstant and does not trigger that exception. No claim of attainment at distance7 is made. A tree consisting entirely of unary nodes can have arbitrary height while obeying the depth-n count1; this is the unexpected inference guard against converting a branch-rate bound into a settling bound.

**Prior art and dependencies.** The calculation uses G7's recurrence and the pending G158 quotient classification; the six-step exclusion is proved directly here. Existing reset/integration prior art and G156-G158 are the relevant records. No computation or literature novelty claim is made. The number and location of later branch nodes, dyadic-period record spacing and adaptive physical waiting budgets remain open.

*Second reader's note on G159 (Local, 2026-10-07; chat L115).* Correct. After an even-parity zero driver, $c$ is
nonconstant; $d$ is forced to the constant one by the persistent reset; and $e$ is nonconstant. $f = 0$ would make $e$
constant. $g = 0$ forces $e = f$ and then an alternating $c$, so $a = 1$ with odd parity, which is excluded. $h = 0$
gives $e = f \oplus Sf$, which at any zero of $f$ contradicts $f$'s own equation. The width bound is the prefix-free
count. A finding that changes how much any check here can say: on the rooted trees for every $P \le 15$ there is no
even-parity branch node, each rotation quotient is a single chain, and the spacing claim is vacuous there. So S53
(`rule30_audit_g99_g100.py`) also tests the lemma ambiently: below every nonzero even-parity $a$ with zero driver, for
$P \le 8$, all 2,736 continuations keep nonzero drivers for six depths. On the rooted trees it confirms at most
$2^{\lceil n/7 \rceil}$ classes per depth, which is trivially 1.

### G.GPT160. a closed arrival-phase gate removes only transient front states (second-read by Local, 2026-10-07)

### G160. A closed arrival-phase gate removes only transient front states (2026-10-07)

**Statement.** Use G8's common-period-P full-line reset-front graph, excluding the zero word-pair. For a state (a,b,r), define the gate by

- if a is nonzero: a(r-1)=1;
- if a=0: (S b XOR b)(r-1)=1.

Indices are modulo P. The gate is forward invariant. Every nonzero compatible front path is in it after at most two edges. The rooted front starts at the exceptional pair (0,1) and enters the gate after one edge. Every compatible phase-augmented cycle lies entirely inside the gate.

**Proof.** An edge goes to (b,c,r'), with S c=a XOR(b OR c). If b is nonzero, r'=r+delta(b,r) is exactly one time past the first black b cell at or after arrival. Thus b(r'-1)=1 and the child is in the first part of the gate regardless of the parent's phase.

If b=0, delta=0 and r'=r. The child obeys S c XOR c=a. Since (a,b) is not the zero pair, a is nonzero and c is nonconstant. A gated parent has a(r-1)=1, so the child's second gate condition holds. This proves invariance. From any ungated state an active b enters immediately. If b=0, its child has nonconstant driver c, so the following edge enters immediately. No nonzero pair has the zero pair as a child, by the same recurrence. Hence two edges suffice. The root has constant-one driver and cost1, giving the gated child (1,1). On a cycle every state has at least two preceding edges on the same cycle; the two-edge entry assertion puts every state inside the gate. Square.

**Phase counts and certificate transfer.** For a fixed pair of common period P, the gate allows exactly the number of black bits in a when a is nonzero, or the number of transitions in b when a=0. On its relative-phase fiber of size q, use the corresponding counts in q letters. This is an exact local restriction, not a census of reachable states. If a phase-sensitive potential on the gated graph bounds interval debt at slope gamma>=0 by H, the whole nonzero graph has the bound H+2P: discard at most two initial edges, each of cost at most P, and apply the gated certificate to the rest. For the rooted front, the initial cost is1, giving H+1 instead. Intervals wholly inside the discarded part obey the same conservative bound. These are full-line front statements; birth clamps and sublinear period growth remain separate obligations.

**Controls and identified unexpected check (symbolic, no run).** The root (0,1) itself fails the second gate condition because a constant word has no transitions; its first child satisfies the first condition. The derivative condition at a=0 is essential, as the period-two integrated children have zero first coordinate yet valid arrival phases.

The two-step threshold is needed on the unrestricted graph. In temporal order take a=0101, b=0000, r=1 at period4. Integration gives c=0011. The parent fails a(0)=1, and the child (0,c,1) still fails Delta c(0)=1. Its active c then enters on the next edge. This checks a local compatible path, not root reachability. The identified unexpected cycle guard is that every cycle already lies in the gate: G8's compatible slope-2 obstruction survives unchanged. Gate pruning cannot improve cycle means or cure that obstruction; it removes transient arrival phases only.

**Record and scope.** This is a direct finite-graph consequence of G8's reviewed next-black arrival rule and G7's diagonal recurrence. It does not depend on the pending G157-G159 proofs. No computation or literature novelty claim is made. A uniform gated potential size bound remains unproved; the gate by itself gives neither a settling bound nor a prize result.

*Second reader's note on G160 (Local, 2026-10-07; chat L116).* Correct. With an active driver the arrival lands one past
a black driver cell, so the child is gated whatever the parent's phase. With a zero driver the phase is kept, and the
child's word difference equals the parent's first word, so a gated parent gives a gated child. A nonzero pair never has
the zero pair as a child, so two edges always reach an active driver. Every state on a cycle has two cycle edges before
it and is therefore gated. The transfer charge is at most $P$ per discarded edge, and 1 for the root's edge. Checked
exhaustively (`rule30_audit_g99_g100.py`, S54) on the full-line front graph for every $P \le 7$: the gate is invariant,
every state is gated within two edges, and every state of every cyclic strongly connected component is gated (5,894
cyclic states at $P = 7$). The gated phases of each pair number the black cells of $a$, or the transitions of $b$ when
$a = 0$. GPT's period-four control fails the gate at the parent and at both integrated children, and enters at the next
edge. A muddled first draft of the control's boolean expression was rewritten before the recorded run.

### G.GPT161. one representative path decides the first genuine rooted branch (second-read by Local, 2026-10-07)

### G161. One representative path decides the first genuine rooted branch (2026-10-07)

**Statement.** For a dyadic common-period cap Q, the existence of an even-parity zero-driver node anywhere in the rooted tree can be decided by one representative path, without enumerating its phase copies. Start at (a,b)=(0,1) with least common period q=1. Repeat:

1. If b is nonzero, construct the unique q-periodic child c by resetting at any black b cell and following the scalar recurrence. Replace (a,b) by (b,c); keep q.
2. If b=0 and one q-block of a has even parity, stop: this path is a rooted genuine-branch witness.
3. If b=0 and that parity is odd, then if q=Q stop: no rooted genuine branch exists at this cap. Otherwise integrate a with c(0)=0 over2q letters, repeat a and b to that length, replace the pair by (b,c), and double q.

The procedure terminates. It uses O(Q) working bits apart from a retained witness, and O(sum q_j) bit updates along its visited path; in particular O(QK) for K visited nodes. These are symbolic complexity bounds, not runtime measurements or a claim that K is small.

**Proof.** All rooted pair periods are dyadic by verified G157. If a child pair has a period d, its predecessor B has period d too; therefore the least common period of the parent divides that of the child. Active-driver construction gives a child with period dividing q, so its pair period is exactly q. At a zero driver the pair period is the least period of a. Odd integration gives child period exactly2q, as in G158. The period variable therefore remains exact throughout.

By verified G158 an active-driver node has one child class and an odd-parity integration node has one child class after rotation. Choosing c(0)=0 in the odd case selects one of two representatives of that same class. Every property being tested, including zero driver, least period and block parity, is invariant under temporal rotation. Until an even-parity node is met the entire quotient is a single chain, so the representative path cannot bypass an earlier genuine branch. An even-parity node has two q-periodic child classes and is a witness regardless of the remaining cap. Conversely an odd-parity node at q=Q is a leaf; if the representative chain reaches it with no genuine branch, no other quotient branch exists. Termination follows from G7's finite, nonrepeating rooted tree at cap Q. A reset scan, parity scan or integration costs O(q) with only the current words retained, proving the resource bounds. Square.

**Controls and identified unexpected check (no run).** Local L115's complete trees at Q=1,2,4,8 have no genuine branch and respective heights3,8,29,400. Under that independently checked condition, their total labeled-node counts must be3, 3+2*(8-3)=13, 13+4*(29-8)=97 and97+8*(400-29)=3065: each quotient node at pair period q has q distinct rotations. These identities agree with G8 and L115 and check that phase copies, rather than missing branches, account for those counts. This does not extend the observation to Q=16.

The unexpected choice guard is that selecting c(0)=0 is safe only before the first genuine branch. At an even-parity node the two children are not rotation equivalent, so silently selecting one and continuing would cease to certify the whole tree. The procedure stops and reports that node instead. No Q=16 run was launched; Local's stopped full build remains a recorded limitation, not a negative result.

**Scope.** This is a direct algorithmic corollary of the verified rooted-tree and child-orbit proofs, not a new automaton or phase-independent cost certificate. It supplies a bounded-memory exact alternative to a full phase-copy enumeration for this specific first-branch question. Large height, actual waiting costs, and the uniform potential bound remain unresolved. No literature novelty claim or prize result is asserted.

*Second reader's note on G161 (Local, 2026-10-07; chat L117).* Correct. The period variable stays exact: a parent's
least common period divides its child's, an active driver's child has period dividing $q$, and odd integration doubles
it exactly. Before the first even-parity node the quotient is a single chain (G158), so choosing $c(0) = 0$ only picks a
phase copy. Stopping at an even-parity node is what keeps the certificate complete. The labeled-count identity holds
because the chain at cap $Q$ extends the chain at cap $Q/2$ through its leaf, and every later node has pair period $Q$
and so $Q$ rotations. Checked (`rule30_audit_g99_g100.py`, S55) against S51's complete trees, for $Q = 1, 2, 4, 8$ only.
The single path reports no genuine branch and visits exactly $K = 3, 8, 29, 400$ nodes with non-decreasing periods, and
$N(Q) = 3, 13, 97, 3065$ satisfies the identity. The procedure makes $Q = 16$ inexpensive; it was not run, because GC190
asked for no new job.

### G.GPT162. three post-split reset steps cost two adjacent run lengths (second-read by Local, 2026-10-07)

### G162. Three post-split reset steps cost two adjacent run lengths (2026-10-07)

**Statement.** At a genuine even-parity zero-driver node (a,0) of least period q, the complementary integrated children are c and1 XOR c. Let r be the arrival phase and suppose the gate a(r-1)=1 holds. Then r starts a constant run of c. Let ell and m be the lengths of this run and the next one, respectively. For G8's full-line reset front, the unordered pair of elapsed costs over the next three nonzero drivers is

    {ell+2, ell+m+2}.

In particular the worst sibling cost is at most q+2. This bound is attained on the gated compatible domain at every dyadic q>=4, so these three steps do not have a uniform period-independent cost bound. Root reachability of the attaining family is not asserted.

**Proof.** Since Delta c=a is nonzero, c is nonconstant. The next driver d satisfies S d=c OR d; periodicity and a black reset force d=1. The following driver e satisfies S e=1 XOR c, hence e(t)=1 XOR c(t-1). For the complementary child the same reasoning gives drivers1 and1 XOR e. These are exactly the next three drivers on each continuation.

If c(r)=1, the first reset costs1 and reaches r+1; the constant-one driver costs1 more. The first one of e at or after r+2 is at r+ell+1, including the ell=1 endpoint. Its reset therefore finishes at r+ell+2. The complementary child initially has zeros of length ell, so its first reset finishes at r+ell+1, and its constant-one reset at r+ell+2. Its third driver is c(t-1); the next c-one starts after the following zero run of length m. That reset finishes at r+ell+m+2. When c(r)=0 interchange the two children. Subtract the initial r to obtain the formula. Adjacent runs occupy at most one period, so ell+m<=q.

For sharpness take c to have one black cell at q-1 and zeros elsewhere, with r=0. Then ell=q-1 and m=1. Its difference a has black cells only at q-2 and q-1, least period q for q>=4 and even parity. The parent gate holds because a(q-1)=1. Both integrated children close at period q, and the larger three-step cost is q+2. This is an ambient compatible witness, not a rooted one. Square.

**Known rooted control, not a new search.** Local L118 and GPT's backward audit give a=0000110001010011. Choosing c(0)=0 integrates to c=0000010000110001. G160's gate allows phases0,5,6,10,12,15. The respective (ell,m) pairs are(5,1),(1,4),(4,2),(2,3),(3,1),(1,5); therefore the two unordered costs are{7,8},{3,7},{6,8},{4,7},{5,6},{3,8}. The maximum is8. An independent literal reset scan checks all six table entries and the same-order cost18 counterexample, without a continuation search. This certifies only the first three full-line reset steps after the known split; it gives no later cost or actual transient maximum.

**Difference-order guard.** At dyadic q>=8, put a single pulse g at q-1 and take c=Delta g, a=Delta^2 g, r=0. Then c has its two adjacent ones at q-2,q-1, a has two ones at q-3,q-1, the gate holds, and the least periods remain q. Since nu(g)=q, their orders are nu(a)=q-2 and nu(c)=q-1. The cost maximum is again q+2. At q=16 this has exactly the known rooted witness’s orders14 ->15 but cost18 rather than8. It is not asserted rooted. Thus these scalar difference orders do not alone control local reset cost on the gated compatible domain.

**Identified unexpected check and scope.** At ell=1 the third driver is already black at its arrival, so its cost is1, not0: the fast sibling cost is3. The sharp gated single-black-cell family rejects a uniform local three-step slope below3 once q>=8, despite the structural seven-depth branch spacing. A period-dependent potential could still absorb such a finite cost; no uniform potential-size bound is disproved. Existing G2.3, G8, G159 and G160 are the relevant prior records; this is direct run-length accounting, with no novelty claim or new search. Birth clamps, rooted all-branch control and sublinear period growth remain separate obligations.

*Second reader's note on G162 (Local, 2026-10-07; chat L120).* Correct, including the timing GPT asked me to check.
Below the split the three drivers are $c$, the all-ones word forced by the persistent reset, and
$e(t) = 1 \oplus c(t-1)$. The gate makes $r$ a run start of $c$. With $c(r) = 1$ the first two resets end at $r + 2$,
and $e$'s first black cell at or after $r + 2$ is at $r + \ell + 1$; for $\ell = 1$ this is the arrival itself, so the
cost is 1 and the fast total is 3. The sibling waits $\ell$ for its first black cell and then for the whole next run,
giving $\ell + m + 2$. I traced the rooted control's six gated phases by hand from the runs of $c$ (5, 1, 4, 2, 3, 1)
and they give G162's pairs, maximum 8. The two $q + 2$ families check as stated, with orders $q - 2 \to q - 1$ for the
pulse differences. Checked by literal reset arithmetic, independent of the run-length formula
(`rule30_audit_g99_g100.py`, S56). That covers all 4,458 gated even-parity cases for every period $P \le 10$, the rooted
control at period 16, and both families at $q = 4$ to 16 where they apply. GC196's averages also check: over the six
phases the slower sibling averages $22/3$ and both siblings 6.

### G.GPT163. one winding rate controls repeated-strip block debt (second-read by Local, 2026-10-07)

### G163. One winding rate controls repeated-strip block debt (2026-10-07)

**Statement and domain.** Fix a spatially repeated list of m temporal drivers, each periodic with common period P. It may be a compatible Rule30 pair cycle, but the timing statement only uses G8's full-line next-black reset rule. Let F(t) be the integer arrival time after one whole spatial block, starting at integer time t. There is one phase-independent rational rate rho per block such that, for every integer t and n>=0,

    abs(F^n(t)-t-n*rho) <= P-1.

A single orbit of the phase map F modulo P determines rho: if its eventual phase cycle has length d<=P and lift displacement k*P, then rho=k*P/d. All phase cycles have this same rate, even if they do not merge. The per-driver asymptotic slope is rho/m.

At block boundaries, a nonnegative P-periodic integer potential H with

    H(t) >= 2*(F(t)-t)-5*m+H(F(t))

exists if and only if rho<=5*m/2. Whenever it exists, one can choose max H<=2*(P-1), independent of m. This is a whole-block certificate for this fixed repeated strip, not G8's one-edge potential on the entire compatible graph.

**Proof.** A nonzero driver's reset map sends t to one plus its first black time at or after t; a zero driver's map is the identity. Both are nondecreasing and commute with translation by P. Their composition F has both properties. Its phase map is a function on P residues, so every phase orbit eventually cycles. A recurrent lift cycle of length d has displacement k*P; repeating it gives limiting displacement rate k*P/d. If t<=u<=t+P, monotonicity and translation give F^n(t)<=F^n(u)<=F^n(t)+P. Hence any two initial times have the same limiting rate rho, by translating one into that interval and dividing by n. This proves existence, independence and the orbit formula without requiring an invertible phase map.

Fix n>=1 and let D_n(t)=F^n(t)-t. This is P-periodic. For residues t,u with 1<=u-t<=P-1, the previous inequality gives -(u-t)<=D_n(u)-D_n(t)<=P-(u-t). Thus its largest and smallest residue values differ by at most P-1. Write these values M_n and a_n. Iterating F^n in blocks shows j*a_n<=F^(j*n)(t)-t<=j*M_n. Divide by j and let j grow to obtain a_n<=n*rho<=M_n. Every D_n(t) lies in that same interval, giving the claimed P-1 error. The n=0 case is exact.

When rho<=5*m/2, define H(t) as the supremum, over n>=0, of 2*D_n(t)-5*m*n. The n=0 term is0; the error bound makes every term at most2*(P-1). Since these are integers in a bounded interval, the supremum is a finite nonnegative integer, periodic in t. Splitting off the first block gives the potential inequality. Conversely, sum such an inequality over n blocks. A finite periodic H bounds the total reward; dividing by n yields 2*rho-5*m<=0. Equality is allowed: zero-weight recurrent loops do not make the potential infinite. Square.

**Independent existing control.** G8's compatible period4, spatial-length12 witness has F(0)=27 and F(3)=31. Therefore F^n(0)=28*n-1 for n>=1, while F^n(3)=3+28*n; both rates are28 per block, hence slope7/3. The phase-zero first-block slope27/12 is not its asymptotic rate. Its whole-block error from phase0 is1, within P-1=3. No new cycle search was run.

**Identified unexpected check: coalescence is not required.** The all-zero compatible strip gives F(t)=t. Its P phase residues remain separate fixed points, but all have rate0 and H=0. The proof needs weak monotonicity, not invertibility or convergence to one phase. A single pulse at time0 gives a sharp clock-only error control: F(0)=1, F(t)=P+1 for 1<=t<P, and its recurrent rate is P. The error at t=0 is P-1. That single-driver repeated strip is not claimed Rule30-compatible for P>1; it tests the timing lemma's general domain, not a compatible slope obstruction.

**Prior record and limits.** This is the standard monotone degree-one translation-number mechanism, here proved directly on integer times with the discrete P-1 bound. The primary Mathlib translation-number module states phase-independent limits and bounded iterate displacement; no novelty is claimed for rotation theory, and no Lean validation of this application is claimed. G6 already gives phase comparison for a fixed history; G8/G10 already compute exact recurrent phase means. This entry supplies the explicit whole-block potential consequence. It does not prove rho<=5*m/2 for all compatible cycles, charge partial blocks independently of m, bound outward trees or rooted branched paths, include birth clamps, or establish sublinear period growth. Those remain separate obligations before any prize conclusion.

*Second reader's note on G163 (Local, 2026-10-07; chat L121).* Correct; the two points GPT asked about hold. The
displacement sandwich: for residues $1 \le u - t \le P - 1$, monotonicity gives $D_n(u) \ge D_n(t) - (u - t)$, and
translation gives $D_n(u) \le D_n(t) + P - (u - t)$, so the spread of $D_n$ over residues is at most $P - 1$. Splitting
$F^{jn}$ into $j$ blocks of $n$ puts $n\rho$ between the extremes, hence $|F^n(t) - t - n\rho| \le P - 1$. The
potential: with $\rho \le 5m/2$ every term $2D_n(t) - 5mn$ is at most $2(P - 1)$, the supremum is a bounded nonnegative
integer, and shifting the index by one block gives the inequality; summing it gives the converse. The G8 witness
arithmetic ($F^n(0) = 28n - 1$) and the sharp pulse strip both check. Checked (`rule30_audit_g99_g100.py`, S57) on 400
random strips with zero drivers allowed: monotone degree-one maps, one rate per strip over every phase cycle, the
$P - 1$ band for $n \le 60$, and a truncated potential within $2(P - 1)$ that satisfies the block inequality. The pulse
strip's error is exactly $P - 1$ at $P = 2, 5, 8$.

### G.GPT164. one full-line path certifies every interval phase and birth restart (second-read by Local, 2026-10-07)

### G164. One full-line path certifies every interval phase and birth restart (2026-10-07)

**Statement.** Fix a finite list of M temporal drivers with one common period P. Let F_j be G8's full-line reset map, including the identity for a zero driver, and let T_0=0, T_(j+1)=F_j(T_j). For gamma>=1 define the reference path's all-interval debt

    D = max over 0<=a<=b<=M of [T_b-T_a-gamma*(b-a)].

Then for every such interval and every integer starting time u,

    G_(a,b)(u)-u <= gamma*(b-a)+D+P-1,

where G_(a,b)=F_(b-1) composed through F_a. Consequently G9's normalized birth-clamped front, with barriers beta_j<=j, obeys T_birth(k)<=gamma*k+D+P-1 for every k<=M. The statement also holds for every global temporal phase shift of the same driver list. No compatibility or spatial repetition is needed for this transfer; those conditions remain necessary to establish a useful D for the actual Rule30 history.

**Proof.** G_(a,b) is nondecreasing on integer times and commutes with translation by P. Its displacement Q(u)=G_(a,b)(u)-u is P-periodic. For residues u<v with 1<=v-u<=P-1, monotonicity and periodicity give

    -(v-u) <= Q(v)-Q(u) <= P-(v-u).

Hence the spread of Q over every starting residue is at most P-1. At the actual reference arrival T_a its value is T_b-T_a, so any Q(u) is at most T_b-T_a+P-1. The definition of D proves the interval inequality. Apply G9's exact maximum-over-restarts identity to that uniform interval budget and beta_j<=j to obtain the birth bound. A phase shift phi conjugates each reset to F_j(s+phi)-phi, so the shifted interval displacement is the original Q(u+phi); it obeys the same bound. Square.

This uses the displacement-spread argument of G163 for a finite interval composition, not its repeated-block rate. The reference debt must cover all intervals, not just the whole prefix. Comparing two reference prefix bounds separately would introduce 2(P-1); composing the interval directly keeps the overhead to P-1. The common P must cover the whole driver list being certified; it cannot be replaced by a smaller current-driver period without a separate justification.

**Existing finite evidence, not a new run.** G7's recorded phase-zero period16 history through M=53207 has maximum interval debt26.5 at slope5/2. Conditional on that recorded finite calculation, this lemma supplies all-starting-time interval debt at most41.5 on the same history. For every phase and L>=1, its normalized birth-clamped absolute bound is T_birth(k)<=(5/2)*k+41.5 for k<=53207. G9 also gives birth-clamped interval debt at most42.5 for L=1, or41.5+L in general. These are loose universal budget consequences, not new maxima or a sharper final settling time; G2's final-time bounds remain unchanged. The computation is not rerun or newly independently verified here. The history ends at the known genuine split: another continuation requires its own reference-path debt. No all-branch or asymptotic conclusion follows.

**Identified unexpected sharpness/domain control.** A single pulse driver at residue0 has reset displacement1 from reference time0, but displacement P from starting time1. Thus its displacement spread is exactly P-1; the transfer cannot remove that overhead in the generic clock domain. At gamma=1 the one-step reference debt is0 while the starting-time1 debt is P-1. This is not claimed a repeated compatible Rule30 strip. At P=1 the overhead vanishes, including the zero-driver identity. G9's endpoint-only birth counterexample remains consistent: this lemma explicitly adds the period overhead and requires every reference interval. G163's interior-debt counterexample still prevents replacing D by a whole-block rate certificate.

**Scope and remaining obligation.** Direct corollary of reviewed G6/G9/G163 monotone clock maps; no new prior-art or computation claim. The missing research bound is now an all-interval budget on one full-line reference path per admissible branched history, together with the independent period-growth requirement. An arbitrary-period D=O(P) bound is not supplied. Births and phase restarts need no separate search once that reference budget is established. No prize result is claimed.

*Second reader's note on G164 (Local, 2026-10-07; chat L122).* Correct; the two points GPT asked about hold. The
all-interval quantifier is needed and is used correctly. The bound at an interval $[a, b]$ comes from that interval's
own displacement, pinned at the reference arrival $T_a$, so $D$ must cover every reference interval, and composing the
interval map directly keeps the overhead at $P - 1$ rather than $2(P - 1)$. The phase conjugacy holds: a global shift
$\varphi$ turns each reset into $F(s + \varphi) - \varphi$, so the interval displacement is $Q(u + \varphi)$, with the
same spread. The birth bound uses $\beta_j \le j \le \gamma j$, which is where $\gamma \ge 1$ enters. Checked
(`rule30_audit_g99_g100.py`, S58) on 300 random driver lists, $M \le 40$ and $P \le 8$, at $\gamma = 1$ and $5/2$. Every
interval, every start and every phase shift obeys the bound. The birth-clamped front, computed by its own recursion
$f_j = \max(\beta_j, F(f_{j-1}))$ rather than G9's identity, stays below $\gamma k + D + P - 1$ for random barriers. The
single pulse attains the overhead $P - 1$. The period-16 numbers (26.5 and 41.5) rest on G7's recorded computation,
which this review did not rerun.

### G.GPT165. dyadic stage budgets stitch without a logarithmic loss (second-read by Local, 2026-10-07)

### G165. Dyadic stage budgets stitch without a logarithmic loss (2026-10-07)

**Conditional reduction.** Follow one infinite admissible rooted diagonal history. At node k let p_k be the least common temporal period of its adjacent pair, with the root (0,1) at k=0. Use gamma with 1<=gamma<3. Suppose there is one finite constant C>=0 for this history such that, on every maximal constant-period stage q, one full-line reference path has debt at most C*q on every finite subinterval of that stage. Different stages may use different reference arrival phases, but C and gamma must stay uniform along this history.

Then, for a prefix of M edges, every full-line interval and every starting time has debt at most2*(C+1)*p_M. The same bound transfers to normalized birth-clamped absolute timing:

    T_birth(M) <= gamma*M+2*(C+1)*p_M.

It also covers every global temporal phase of this same history. Thus p_M=o(M), together with the assumed stage budget, would supply G2's below-3 sufficient settling bound on this history. To cover every admissible left side, both assumptions must hold separately on every history; history-dependent constants are allowed as in G2. No stage budget or period-growth estimate is proved here.

**Exact stage structure.** The predecessor B commutes with temporal shifts. If a child pair has period q', its predecessor has a period dividing q'. G157's reset/integration rule supplies child common period at most q, or2q at an odd zero-driver integration, when the parent's least period is q. Since rooted periods are dyadic, the child's least period is therefore q or2q, never smaller. A doubling can occur only on a zero-driver edge; that edge has full-line reset cost0. Every edge whose source pair has period q uses a driver with period dividing q, including that final zero edge. Consequently all clock maps within a stage share common period q. Genuine even-parity branches preserve q; they do not start a new period stage.

**Proof of the budget.** Fix any finite interval within the M-edge prefix and split it at period changes. For its part in a q-stage, G164 upgrades the assumed reference all-interval debt C*q to an arbitrary-start debt at most(C+1)*q-1. Each stage is contiguous, so the interval visits each q at most once. The distinct q are powers of2 bounded by p_M. Their sum is at most2*p_M-1. Sum the interval inequalities at their actual arrival times to obtain elapsed <=gamma*(interval length)+2*(C+1)*p_M. This holds for every starting time, so G9's restart identity applies on the finite prefix, giving the stated birth bound. Phase conjugacy preserves the same inequalities. No separate phase sum, per-birth penalty or per-branch allowance occurs. Square.

**Equivalent period-growth checkpoint.** Every infinite rooted history has unbounded p_k: otherwise its path would be infinite in G7's finite rooted tree. Let N_j be the first node of least period2^j, for j>=1. The exact stage structure gives p_k=2^j for N_j<=k<N_(j+1). Hence p_k=o(k) if and only if2^j/N_j tends to0. Necessity evaluates at k=N_j; sufficiency bounds p_k/k by2^j/N_j throughout that stage. This is a reformulation, not an estimate for N_j. A large finite doubling delay does not prove the limiting condition.

**Identified unexpected check: branching is not doubling.** The known split at diagonal53208 has period16 children, as G2.3, G158 and the independent FBR16 replay establish. It is not the first period32 node N_5 and earns no new stage allowance. The known initial stage entries3,8,29,400 do not locate N_5. Nor may one add C*q after every genuine branch at fixed q: the assumed all-interval budget must already cover the selected continuation within that entire stage. The elementary sum1+2+4+8+16=31 checks the strict bound below2*16, but certifies no actual stage debt.

**Scope.** Direct use of G2, G7, G157/G158, G164's interval transfer and G9's birth theorem; elementary geometric summation, with no novelty or new computation claim. G164 was independently verified by Local L122 during this publication; its review and controls are preserved. The hard obligations remain uniform one-reference-path stage debt and superlinear doubling-entry positions on every admissible history. Word-only branch counting, finite doubling records and repeated-strip rates supply neither obligation. No prize conclusion is asserted.

*Second reader's note on G165 (Local, 2026-10-07; chat L123).* Correct as a conditional reduction. The stage structure
holds: since $B$ commutes with shifts, the parent's least period divides the child's, so with G157's reset and
integration rule a child has period $q$ or $2q$ and never less. Doubling happens only on an odd-parity zero-driver edge,
which costs 0, and an even-parity branch keeps $q$. The budget sum holds: within a stage G164 turns the assumed $Cq$
into an arbitrary-start $(C + 1)q - 1$. An interval meets each dyadic stage at most once, and the powers of two up to
$p_M$ sum to less than $2p_M$. The period-growth reformulation is right in both directions. Checked
(`rule30_audit_g99_g100.py`, S59) along the known $Q = 16$ representative path to its first genuine branch (53,208
nodes). The period never decreases and changes only at odd-parity zero drivers, by doubling. Every node's driver has
least period dividing its stage period. The stage entries are $N_1, \ldots, N_4 = 3, 8, 29, 400$ with no period-32 node,
and the branch keeps period 16. Both hypotheses, the uniform stage budget and $2^j/N_j \to 0$, remain unproved, as G165
says.


### G.GPT166. finite-horizon and state-projection guards (second-read by Local, 2026-10-07)

**Exact horizon diagnostic: tight-edge distance, not potential size (2026-10-07; symbolic, review requested).** Consider any finite directed graph with real edge rewards w, no positive-reward cycle, and stopping permitted at every vertex. Let h(v) be its least nonnegative feasible potential, equivalently the maximum reward of any finite walk from v, including the empty walk. G8 already proves finiteness by deleting nonpositive cycles. For an edge v->u set its slack s(v,u)=h(v)-w(v,u)-h(u)>=0. For any at-most-n-edge walk p ending at z, telescoping gives

    h(v)-reward(p)=h(z)+sum of the edge slacks on p.

Therefore h(v)-H_n(v) is exactly the minimum of this terminal potential plus accumulated slack over all such walks. In particular H_n(v)=h(v) if and only if some at-most-n-edge walk consists entirely of tight edges (slack0) and ends at h=0. All summands are nonnegative, so neither implication loses a condition. This also covers h(v)=0 by the empty walk and vertices with no successors.

Such a tight walk always exists: choose a minimum-length walk attaining h(v). An optimum exists among simple paths by cycle deletion. Its endpoint must have h=0, since otherwise a positive optimal continuation increases the reward; then the telescoping identity forces every traversed edge to be tight. Let d(v) be the shortest tight-edge distance to the zero-potential set. The first globally stable Bellman horizon is exactly max_v d(v): equality H_n=h is equivalent to n>=max d; and any equality H_(n+1)=H_n makes H_n a feasible potential, hence the least potential because H_n<=h. The shortest tight path is simple, so d(v)<=|V|-1. This is a finite graph bound, exponential rather than linear in q for the aligned pair domain; it supplies no all-period Rule30 budget.

**Identified unexpected check: allowed numerical weights do not control horizon.** On a directed chain take2L+1 edges with rewards(-1,+1) repeated L times, followed by+1, for L>=1. These weights have the exact numerical reset form2*delta-5 with delta2 or3. Every even-index vertex before the final leaf has h=1, every odd-index vertex has h=2, and the leaf has h=0. Every edge is tight. Thus max h=2 while the initial vertex has d=2L+1: all earlier even prefixes have reward0 and odd prefixes reward-1. No positive cycle exists. This refutes a generic inference from bounded potential size to bounded horizon, even with bounded positive reset delays and odd integer rewards. It is an abstract chain, not a claimed compatible or rooted Rule30 history. The zero leaf and empty-stop conventions are essential controls, and no computation was run.

**Application and next question.** HG4 failure concerns the tight-route length in the full gated graph. It does not by itself refute a potential magnitude O(q). Local's descriptive85, if its fixed-point computation is correct, means max d=85 in that finite q8 domain; this is an interpretation, not an independent global audit. A future horizon proof needs a compatibility theorem on tight paths, while the actual stage goal can instead bound h directly without a short-horizon theorem. This isolates two obligations that should not be conflated. No new universal bound, rooted counterexample or prize result follows. The reweighting/telescoping mechanism is standard shortest-path potential theory; see PRIOR-ART.md, not a novelty claim.


**Direct-potential restriction: the current driver and phase are insufficient (2026-10-07; symbolic, review requested).** At any dyadic q>=4, let b have its sole black bit at time q-1, let a=S b XOR b, and take arrival phase0. Then c=b is a valid child of(a,b), because S b=a XOR(b OR b). Both source(a,b,0) and target(b,b,0) satisfy G160's gate: a(q-1)=1 and b(q-1)=1. The source reset costs q, so the clock returns to phase0 and the edge reward at slope gamma is q-gamma.

Suppose a proposed finite potential has the form f(b,r), depending on the whole current driver b and relative phase r but forgetting the preceding word a. Its edge inequality here becomes

    f(b,0) >= q-gamma+f(b,0).

This is impossible when gamma<q. In particular no such potential can certify slope5/2 on the full gated q-domain for any dyadic q>=4. More generally a fixed finite gamma cannot be certified on all dyadic periods by this restricted family. The argument permits arbitrary dependence on q and arbitrary finite potential magnitude: changing constants, density, run lengths, difference orders or even retaining the whole b cannot rescue the family if a is discarded. This is a restriction on the potential's information, not a refutation of G8's two-word-and-phase potentials or G165's desired bound. Root reachability of these sources is not asserted.

**Identified unexpected check: the projected loop is not an actual repeatable cycle.** The target(b,b) has unique period-q child0: a black b resets c to0 and all intervening white times preserve c. Thus the actual next target is(b,0), not another copy of(b,b). The second reset also costs q, and the next zero-driver reset costs0. Forgetting a creates a positive self-loop in the projected driver graph from a valid edge, while the actual pair graph has no such self-loop here. Repeating that projected loop is invalid. The actual two-edge cost2q is a finite period-scale charge, consistent with an O(q) pair potential. At q4 the source is(12,8), its target(8,8), and then(8,0): both delays4 and rewards3, agreeing with HG4's known H0 rejection and G10's maximum6. At q2 the edge reward at slope5/2 is negative, so this specific obstruction does not apply; the dyadic q>=4 condition matters. No numerical run or new cycle census was used.

**Prior record and next intention.** G7's scalar compatibility/reset rule and G160's gate supply the calculation; G8 already keeps both words. This sharpens the earlier phase-loss guard by showing that preserving phase while discarding the preceding word also fails on the ambient gated domain. It is elementary state-projection reasoning, with no novelty claim. Next candidate charges must retain preceding-word information or explicitly exploit a proved rooted restriction. No claim is made that the rooted domain contains this family, and no additional Local computation is requested.


**G8 phase-free obstruction survives the arrival gate (2026-10-07; symbolic scope audit, review requested).** G8.2 already rejects a phase-free two-word potential on the full compatible domain at every slope gamma<3. It is not a new cycle discovery. The remaining scope question is whether G160's gate removes the individually maximizing phases used in that proof. It does not. For G8's cyclic list of period4 words the following exact table supplies a gated maximum-delay phase on each edge; a is the preceding cyclic word and b the listed driver. Time bits are least-significant first.

| b | a | arrival r | a(r-1) | delta(b,r) |
|---|---|---|---|---|
|9|13|1|1|3|
|8|9|0|1|4|
|14|8|0|1|2|
|12|14|0|1|3|
|4|12|3|1|4|
|7|4|3|1|2|
|6|7|3|1|3|
|2|6|2|1|4|
|11|2|2|1|2|
|3|11|2|1|3|
|1|3|1|1|4|
|13|1|1|1|2|

Each source is gated, each triple is the existing compatible G8 triple, and each target is gated by G160 closure. A finite phase-free g(a,b) that satisfies the edge inequalities for all gated states must satisfy each independently chosen row. Summing cancels the cyclic pair potentials and gives36<=12*gamma. Hence gamma>=3 remains necessary even on the gated domain, at dyadic q4. The existing phase-sensitive q4 certificate at gamma5/2 is consistent with this distinction.

**Identified unexpected check and counterfactual.** The selected phases need not concatenate into one physical front. Their use is valid precisely because g forgets phase and must satisfy all gated instances separately. Claiming a real36-step compatible clock cycle would be false: G8's coherent recurrent circuit has elapsed28. If even one of the displayed maximizing phases were excluded by the gate, the old unrestricted proof could not simply be imported; all twelve gate bits have instead been checked explicitly. No new computation was run. This is an exact scope extension of G8, using G160, not a new general potential theorem.

**Working restriction after the two projection guards.** On the full gated domain, neither discarding a while retaining(b,r), nor discarding r while retaining(a,b), can support the desired below3 certificate. These facts do not prove that every successful statistic must store the full pair and phase; other compressions or a rooted-only restriction remain possible. The next direct-charge argument must preserve the distinction each proposed compression erases, rather than transfer an unrestricted graph result without checking its gate. No rooted debt lower bound or prize conclusion is claimed.



*Second reader's note on G166 (Local L127, 2026-10-07).* The tight-edge distance identity and both projection obstructions are correct. S60 checks equality of tight distance and stabilization at horizons4,21,85 for q4,6,8 and the abstract chain controls. S61 checks all twelve gated phases and the compatible q4 cycle. The audit initially imported HG4's module-level CPU limit and lost later output; Local moved the limit to main() and repeated the audit. The corrected complete audit passes; the earlier incomplete run is not a pass.

### G.GPT167. complete branch blocks and partial interval costs (second-read by Local, 2026-10-07)

### GPT G167 — complete branch blocks and partial interval costs (RULE30-GPT.md G167; awaiting second reader, 2026-10-07)

**Bounded symbolic result, independent review requested.** Include G162's zero-driver branch edge(a,0)->(0,c), then the three nonzero-driver edges whose elapsed cost is either ell+2 or ell+m+2. Here r is gated, ell and m are the first two constant-run lengths of c, and ell+m<=q. The zero-driver edge costs0. At slope5/2 the total doubled reward of this four-edge block is therefore one of

    2*ell-16, 2*(ell+m)-16.

The worst endpoint reward is at most2q-16. Thus every such block at dyadic q<=8 has nonpositive endpoint reward. This is an ambient gated statement, not a rootedness assertion. At larger periods the upper bound can be positive. G162's pulse attaining family makes the larger reward2q-16 sharp. G159's seven-depth separation ensures these four-edge blocks around distinct genuine branches do not overlap, but supplies no bound on the remaining edges.

**Exact partial-prefix audit.** On the fast sibling c(r)=1, the four reset delays are0,1,1,ell. Its prefix doubled rewards, after0 through4 edges, are

    0, -5, -8, -11, 2*ell-16.

On the slow sibling c(r)=0, the delays are0,ell+1,1,m. The rewards are

    0, -5, 2*ell-8, 2*ell-11, 2*(ell+m)-16.

These follow directly from G162's literal reset arithmetic, including the m=1/ell=1 endpoint cases. Consequently the largest reward of a prefix anchored before the free zero edge is the maximum of0,2*ell-8,2*(ell+m)-16 across the two siblings. It is at most max(0,2q-10), since a nonconstant c has ell<=q-1. This says nothing about an interval that begins after the free edge.

**Known rooted control, not a new run.** G162's six allowed phases at the recorded q16 split have(ell,m)=(5,1),(1,4),(4,2),(2,3),(3,1),(1,5). Hence every whole four-edge branch block there has doubled reward at most-4, while the largest branch-anchored prefix reward across phases and siblings is2 (debt1). This is arithmetic on the existing table, not a continuation search or a uniform q16 theorem. No actual birth-clamped settling estimate is imported.

**Identified unexpected check/counterfactual: endpoint payment does not pay arbitrary intervals.** At q8 choose the valid G162 gated pulse family with ell=7,m=1. The slow sibling's whole four-edge reward is0, but its two-edge prefix reward is6 (debt3). If an interval starts immediately after the free edge, its very next reset costs8 and has reward11 (debt5.5). These are actual compatible local blocks from G162, unlike the generic clock schedules of G163's addendum; rooted membership is not claimed. They refute treating nonpositive block endpoints as a certificate for every prefix or subinterval.

**What moves and what remains.** The free zero edge is an exact part of the local branch charge and should not be discarded when charging complete branch blocks. Negative complete blocks can be recognized without charging a fresh period budget per branch. However interior endpoint effects and the intervening nonbranch edges still need control, especially at larger q. Removing blocks does not create a new compatible history, so no bound may be applied to the compressed word sequence without a separate argument. G165's uniform all-interval stage obligation remains unproved. This is a symbolic corollary of G162 and G159, not a new general amortized theorem or prize claim; no computation was run.

*Second reader's note on G167 (Local, 2026-10-07; chat L128).* Correct. With the free zero edge included, the four-edge
block costs $\ell + 2$ or $\ell + m + 2$. Its doubled slope-5/2 reward is therefore $2\ell - 16$ or $2(\ell + m) - 16$,
at most $2q - 16$ and sharp in the pulse family. The per-sibling delays are $0, 1, 1, \ell$ (fast) and
$0, \ell + 1, 1, m$ (slow), which give the stated prefix rewards. So the anchored prefix maximum is at most
$\max(0, 2q - 10)$. The rooted $q = 16$ arithmetic gives block maximum $-4$ and prefix maximum 2, and the $q = 8$
counterexample gives 0, 6 and 11 as stated. Checked by literal reset arithmetic (`rule30_audit_g99_g100.py`, S62) on all
8,916 gated even-parity sibling cases for $P \le 10$, plus the rooted arithmetic and the $q = 8$ case.

### G.GPT168. lift contracted branch charges with one reserve (second-read by Local, 2026-10-07)

### GPT G168 — lift contracted branch charges with one reserve (RULE30-GPT.md G168; awaiting second reader, 2026-10-07)

**Conditional finite-history statement; review requested.** Fix one finite gated periodic history and disjoint four-edge branch blocks from G167, all at common period q. Keep every other edge unchanged and replace each complete branch block by one edge between its actual endpoints, with reward equal to the sum of its four original rewards. These contracted edges represent actual blocks; the compressed sequence is not asserted to be a new Rule30 history. Suppose a nonnegative potential K on the retained vertices satisfies every contracted edge inequality, with original doubled slope5/2 rewards.

Let A bound the positive reward of every prefix starting at a branch block's first vertex, allowing an empty prefix. Let B bound the positive reward of every contiguous subinterval inside any one block. Both are nonnegative and uniform across the blocks. Then K lifts to a nonnegative potential h on every original vertex, satisfying every original edge inequality, with

    max h <= max K+A+B.

Thus the interior cost is one reserve for the whole fixed-period history, not A or B multiplied by the number of branches. This is conditional on a certificate K for all retained ordinary edges and complete blocks; no such uniform certificate is supplied here.

**Proof.** Give every retained vertex h=K+A. Inside a block, define h backwards from that fixed endpoint by h(v)=max(0,w(v,u)+h(u)). This is possible on a finite block and verifies all its interior edge inequalities. Expanded at an internal vertex, h is the maximum of rewards from stopping at an interior vertex and the remaining-block reward plus the endpoint's K+A. The first terms are at most B and the last is at most B+max K+A. At the block's first vertex the backwards-required value is the maximum of prefix stopping rewards, at most A, and whole-block reward plus K(endpoint)+A, at most K(start)+A by the contracted inequality. Hence the assigned h at the first vertex also covers its first original edge. Ordinary edges retain their inequalities because the same A is added at both ends. Nonnegativity and the stated uniform upper bound follow. Adjacent blocks would also work if they share only a retained endpoint; G159's spacing guarantees disjoint blocks on the rooted histories under discussion. No new compatibility after contraction is assumed. Square.

**Exact G167 reserves.** Its fast block rewards are(-5,-3,-3,2ell-5); its slow block rewards are(-5,2ell-3,-3,2m-5). With ell+m<=q and ell,m>=1, G167 supplies A=max(0,2q-10). Every single positive edge is at most2q-5; every two-edge interval is smaller than this, and every three-edge interval is at most2q-11, while the four-edge reward is at most2q-16. Thus B=max(0,2q-5) suffices. The lifted overhead is at most4q-15 for q>=8 (and3 for q4), independent of the number of genuine branches. On the known q16 split's table, the sharper reserves A=2 and B=7 give overhead9 for those local blocks only. This is not a bound on later q16 branch blocks.

**Identified unexpected control and counterfactual.** The q8 slow pulse block has rewards(-5,11,-3,-3), total0. With K=0 at its two contracted endpoints, naive lifting with no reserve fails at the first endpoint because its two-edge prefix earns6. With A=6 the backwards construction gives original vertex values(6,11,0,3,6); every edge inequality holds and the zero stopping option is active at the middle vertex. The general bound max K+A+B=17 safely covers these values. Using a whole-block endpoint inequality alone would miss that middle stop; repeating the block does not require adding6 per repetition. This is exact arithmetic on the existing compatible block, with no new computation or root-membership claim.

**Scope and next obligation.** This is standard finite-path dynamic programming, already present in G8/G166, now applied to G167's actual branch blocks. It resolves how a contracted certificate would transfer to arbitrary subintervals without a per-branch reserve. It does not construct K, bound intervening nonbranch charges, solve the all-period cycle problem, or establish period growth. For multiple dyadic stages, any eventual O(q) certificate must still be stitched as in G165/G166. No prize conclusion or new run is claimed. Next reasoning target is K on the retained ordinary edges and genuine branch transitions, rather than accumulating a fresh allowance for each branch.

*Second reader's note on G168 (Local, 2026-10-07; chat L130).* Correct. With $h = K + A$ at retained vertices and the
backward fill inside each block, the value required at a block's first vertex is the larger of a prefix reward, at most
$A$, and the block reward plus the endpoint's value. The contracted inequality covers the second. Interior values are a
subinterval reward, at most $B$, or the remaining block plus the endpoint, at most $B + \max K + A$. Since the same $A$
is added at both ends of every retained edge, one reserve serves the whole history. The G167 reserves follow from the
edge rewards $(-5, -3, -3, 2\ell - 5)$ and $(-5, 2\ell - 3, -3, 2m - 5)$: $A = \max(0, 2q - 10)$ and
$B = \max(0, 2q - 5)$. At the known $q = 16$ split these are 2 and 7. Checked (`rule30_audit_g99_g100.py`, S63). The
lifting holds on 500 random paths with disjoint blocks, the least contracted potential lifting with
$\max h \le \max K + A + B$. Both reserves hold over every gated block for $P \le 10$, and the $q = 8$ slow pulse block
lifts to $(6, 11, 0, 3, 6)$.

### G.GPT169. reject a uniform three-distance linear potential (second-read by Local, 2026-10-07)

### GPT G169 — reject a uniform three-distance linear potential (RULE30-GPT.md G169; awaiting second reader, 2026-10-07)

**Exact family restriction; independent review requested.** Use G8's reset distance D(w,r)=delta(w,r), including D(0,r)=0. Consider a potential on the full gated compatible domain of the form

    h_q(a,b,r)=C_q+alpha*D(a,r)+beta*D(b,r)+chi*D(a XOR b,r),

where alpha,beta,chi are fixed real coefficients, shared by every dyadic q>=4. C_q is any finite constant depending only on q. This family retains both words and the clock, but only through three scalar reset distances. No member satisfies every doubled slope5/2 edge inequality for every such q. The proof does not require nonnegative coefficients or nonnegative h; it rejects even this larger algebraic family. C_q cancels on every within-q edge.

**Period4 constraints.** First use the gated edge(12,8,0)->(8,8,0) from G166. It costs4 and has reward3. The three source distances are(3,4,3), and the target distances are(4,4,0). Its inequality requires

    -alpha+3*chi >=3.

Next use the zero-driver edge(9,0,0)->(0,14,0). In time-bit notation14 is(0,1,1,1), its cyclic difference is9=(1,0,0,1), and S14=9 XOR14. Both states are gated:9 at time-1 is1, and14(0) XOR14(-1)=1. The edge costs0 and has reward-5. Its source distances are(1,0,1), and target distances are(0,2,2), so

    alpha-2*beta-chi >=-5.

Adding the two inequalities gives2*(chi-beta)>=-2, hence beta-chi<=1. Every triple and distance here is explicit scalar arithmetic; no enumeration or experiment is used.

**Unbounded-period constraint.** For each dyadic q>=4 let b have its sole black bit at q-1. The gated compatible edge(b,b,0)->(b,0,0) costs q and has reward2q-5. Its source distances are(q,q,0), and target distances are(q,0,q). Thus

    q*(beta-chi) >=2q-5.

As dyadic q tends to infinity this requires beta-chi>=2, contradicting the period4 bound. Square. The same contradiction already follows at any dyadic q>=8, where2-5/q>1. Thus this single uniform formula cannot simultaneously certify q4 and q8; no larger computation is needed.

**Identified unexpected guard: the free edge is decisive.** The zero-driver constraint is not vacuous just because its physical waiting cost is0: its doubled reward is-5, and its child can have reset distance2. Omitting it would remove the upper bound on beta-chi and lose this contradiction. All three witnesses are valid gated edges, but root membership is not asserted. The pulse target's zero child is the unique compatible reset continuation, as already proved in G166. These are not projected cycles or sampled independent clocks.

**Scope and counterfactual.** Coefficients depending on q, a special formula at q4, nonlinear combinations, additional features, and a proved rooted-only domain are outside this rejection. In particular this is not a refutation of an asymptotic O(q) bound with finitely many exceptional periods. The constant C_q cannot help because it cancels; but replacing coefficients at small q genuinely changes the family. G8's phase-sensitive pair potential remains valid at the tested periods. The prior record is G8's certificate inequality, G160's gate and G166's pulse edge; no novelty claim is made for the linear-inequality contradiction. Next charge proposals need a richer compatibility feature than this single shared three-distance formula. No computation or prize conclusion is claimed.

*Second reader's note on G169 (Local, 2026-10-07; chat L131).* Correct. All three witness edges are valid gated
compatible edges. $(12, 8, 0) \to (8, 8, 0)$ costs 4 with distances $(3, 4, 3) \to (4, 4, 0)$.
$(9, 0, 0) \to (0, 14, 0)$ is free, since $S\,14 = 9 \oplus 14$, with distances $(1, 0, 1) \to (0, 2, 2)$. The pulse
edge $(b, b, 0) \to (b, 0, 0)$ costs $q$ with distances $(q, q, 0) \to (q, 0, q)$. The first two give
$-\alpha + 3\chi \ge 3$ and $\alpha - 2\beta - \chi \ge -5$, whose sum is $\beta - \chi \le 1$, while the third gives
$\beta - \chi \ge 2 - 5/q$, which already exceeds 1 at $q = 8$. As G169 stresses, the free edge's reward $-5$ is what
supplies the upper bound. Checked (`rule30_audit_g99_g100.py`, S64): the children, gates, costs and distance triples of
all three edges (the pulse at $q = 4, 8, 16$), and the coefficient arithmetic of the two inequalities.

### G.GPT170. embedded period constraints reject three-distance coefficients (second-read by Local, 2026-10-07)

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

### G.GPT171. exact-period witnesses reject three-distance coefficients (second-read by Local, 2026-10-07)

### GPT G171 — exact-period witnesses reject three-distance coefficients (RULE30-GPT.md G171; awaiting second reader, 2026-10-07)

**Stronger restriction; independent review requested.** For every dyadic q>=16, restrict to gated edges whose source and target pairs both have least temporal period exactly q. A potential of the three-distance form in G170, with coefficients selected by this least pair period, still requires gamma>=3q/(q+1). Thus no fixed gamma<3 can be certified at all sufficiently large dyadic periods by this family, even after removing all lower-period states and allowing arbitrary period-dependent coefficients. G170's embedded-state proof alone did not imply this stronger scope.

**Exact-period first edge.** Let b have black bits only at3,7,q-1, let a=S b XOR b, and take arrival r=0. The compatible child is c=b. Since b(0)=0 and b(q-1)=1, a(q-1)=1 and the source is gated. It costs4 and reaches(b,b,4); that target is gated because b(3)=1. The source distance triple is(3,4,3): D(a,0)=3, D(b,0)=4 and a XOR b=S b has first black bit2. From phase4 the target has distances(4,4,0), because its next black bit is7. Hence the first constraint remains

    -alpha_q+3*chi_q >=8-2*gamma.

The word b has odd weight3. A proper-period word at a dyadic common period repeats an even number of times and has even weight. Therefore b, and both endpoint pairs containing b, have least period q. The far black bit at q-1 creates exact-period membership without changing the local distance triples.

**Exact-period zero edge.** Let c have black bits only at1,q-1, and put a=S c XOR c. Use(a,0,0)->(0,c,0). The scalar integration equation holds, the cost is0, and the source/target gates follow from c(0)=0,c(q-1)=1. The feature triples are(1,0,1) and(0,2,2), so

    alpha_q-2*beta_q-chi_q >=-2*gamma.

The two black positions are not opposite at q>=16, so c cannot be a repetition of a proper dyadic divisor: a two-black word with a proper period would have to repeat twice with opposite black positions. Thus c has least period q. Also a has least period q. If a had period dividing q/2, then the difference c(t+q/2) XOR c(t) would be constant, since its temporal difference is0. Constant0 contradicts c's least period; constant1 would force c to have q/2 black bits, contrary to its weight2. This checks exact-period membership of the source as well as the child, which a common-period closure check would not suffice to establish.

**Third edge and contradiction.** The single pulse b at q-1 supplies the gated edge(b,b,0)->(b,0,0), both pairs of least period q, with constraint q*(beta_q-chi_q)>=2q-2*gamma. All three edges now use the same least-period coefficients and constant, which cancels on each edge. Multiply the first two inequalities by q/2 and the third by1. Their left sides cancel and give0>=6q-2*gamma*(q+1), hence gamma>=3q/(q+1). This is an explicit three-edge dual certificate, not a numerical feasibility result. Square.

**Known arithmetic controls and identified unexpected guard.** At q16 the first word is b=32904 and its preceding word is a=49356; the first arrival becomes phase4, not phase0. The second edge uses c=32770 and a=49155. Its preceding word must also have exact period16; checking only c would leave the coefficient cancellation unjustified. The pulse is32768. At gamma5/2 the certificate reads0>=q-5, hence0>=11 at q16. The original G170 embedding changed common period without changing least period; these sparse constructions genuinely change least period while retaining the same three observed distances. No run was used to obtain these controls.

**Counterfactual and remaining scope.** If coefficients were chosen by additional state features, the three inequalities could use different coefficients and cancellation would fail. Nonlinear features, explicit pair interactions, history-dependent or rooted-only certificates remain open. Root reachability of these witnesses is not asserted, and no positive compatible cycle or finite-seed obstruction is claimed. The bound3q/(q+1) is necessary only, not sufficient. This closes the least-period-coefficient escape for the specific three-reset-distance linear family, including finitely many exceptional small periods, but not the all-period O(q) debt conjecture. It uses G169-G170's algebra with explicit compatible exact-period witnesses; no novelty claim is made for linear duality or period counting. Next direct-charge proposals need additional joint state information rather than a period lookup for these same three features.

*Second reader's note on G171 (Local, 2026-10-07; chat L133).* Correct. The first edge is compatible because
$S b = a \oplus b$, and both ends are gated: the arrival moves to phase 4, where $b(3) = 1$. It keeps the triples
$(3, 4, 3) \to (4, 4, 0)$, since $b$'s next black bit after phase 4 is 7. The zero edge keeps $(1, 0, 1) \to (0, 2, 2)$,
and the pulse edge is as in G166. The exact-period arguments hold. An odd-weight word cannot repeat at a dyadic period.
The two black positions 1 and $q - 1$ are opposite only when $q = 4$. A period of $q/2$ in $a$ would make
$c(t + q/2) \oplus c(t)$ constant, which neither value allows. So the same least-period coefficients appear in all three
inequalities, and the dual weights cancel them as in G170. Checked (`rule30_audit_g99_g100.py`, S66) at
$q = 16, 32, 64$: compatibility, gates, costs, triples and least period exactly $q$ for every endpoint word. At $q = 16$
the words are 32904, 49356, 32770, 49155 and 32768, as stated.

### G.GPT173. exact-period feature collision rules out nonlinear three-distance charges (second-read by Local, 2026-10-07)

### GPT G173 — exact-period feature collision rules out nonlinear three-distance charges (RULE30-GPT.md G173; awaiting second reader, 2026-10-07)

**Symbolic theorem; independent review requested.** For every dyadic q>=4 there is a gated compatible edge whose source and target have the same three reset distances(1,3,1), the same least pair period q, and elapsed time3. Consequently no finite potential depending only on these three distances and the least pair period can satisfy every full gated-domain edge inequality at any slope gamma<3. The function can be arbitrary and nonlinear, chosen separately for each period; no potential-size or coefficient restriction is assumed. This is an ambient-domain compression obstruction, not a rooted theorem.

**Construction at q>=8.** Let b have black bits only at2,3,q-1, and c black bits only at1,5,q-1. Define a=S c XOR(b OR c), so the triple is compatible by construction. Begin at phase0. Since b's first black bit is2, its reset costs3. At the source a(0)=c(1) XOR(b(0) OR c(0))=1, while b(0)=0; therefore D(a,0)=1, D(b,0)=3 and D(a XOR b,0)=1. At the target(b,c,3), b(3)=1, c(3)=c(4)=0 and c(5)=1. Its three distances are also(1,3,1). Both gates hold: a(q-1)=c(0) XOR(b(q-1) OR c(q-1))=1 at the source, and b(2)=1 at the target.

Both b and c have exactly three black bits, so have least period q: any repetition of a proper dyadic divisor would have even weight. Each pair contains b, hence both pair periods are q even if a has a smaller period. This last distinction matters at q8, where a is the constant-one word. In the proposed feature potential the edge's two values are identical, while its reward is3-gamma (or twice that in doubled arithmetic). The inequality would require0>=3-gamma. Square.

**Period4 base and known controls.** Local's DQ3 edge is source(a,b)=(15,12), child c=2, arrival0->3. Its aligned target is(9,4). Both pair periods are4, both gates hold, and both feature triples are(1,3,1). The reward at5/2 is1 in doubled arithmetic. At q8 the sparse family gives source(255,140), unaligned child162 and aligned target(145,84); the independent scalar audit above verifies it. The q4 and sparse q8 checks use different actual triples, not an assumed extension of one pair cycle. No further numerical run is needed for the general construction.

**Identified unexpected guard: pair period survives even when one word collapses.** At q8 the source a=255 has period1, not8; source pair(a,b) still has least period8 because b has odd weight3. Requiring every individual word to have period exactly q would incorrectly discard the witness, although G8/G172's graph and G171's coefficient classification use the pair's period. Conversely the source and target actual pairs differ, so the feature self-loop cannot be repeated as a real self-loop. The known original finite certificates remain consistent with this positive projected edge.

**What closes and what remains.** G169-G171's linear restrictions are strengthened: even arbitrary nonlinear functions of the same three distances, augmented by least pair period, fail below3 on every tested or constructed dyadic period q>=4. A rooted-only domain may exclude these witnesses; no root membership is asserted. Additional temporal profile information, other joint features and history-sensitive charges remain possible. The actual all-period O(q) budget, contracted certificate K of G168, and period-growth estimate remain unproved. This theorem is a direct symbolic extension of DQ3's audited feature collision using G7 compatibility and G160's gate; no novelty or prize solution is claimed. Next reasoning should use a feature that distinguishes these explicitly colliding states, rather than another function of the same three distances.

*Second reader's note on G173 (Local, 2026-10-07; chat L135).* Correct. The triple is compatible by construction. At
phase 0, $a(0) = c(1) = 1$ and $b(0) = 0$ give the source triple $(1, 3, 1)$, and $b$'s reset costs 3. At phase 3,
$b(3) = 1$, $c(3) = c(4) = 0$ and $c(5) = 1$ give the target triple $(1, 3, 1)$. Both gates hold. Both pairs have least
period $q$ because $b$ has weight 3, even at $q = 8$, where $a$ is the all-ones word. A function of the features and the
pair period alone would therefore need $0 \ge 3 - \gamma$. Checked (`rule30_audit_g99_g100.py`, S67) at $q = 4$ (DQ3's
$(15, 12)$ with child 2, aligned target $(9, 4)$) and at $q = 8, 16, 32, 64$: compatibility, gates, cost and arrival
phase, both triples, and pair least period $q$ at both ends. At $q = 8$ the words are 255, 140 and 162, with aligned
target $(145, 84)$, as stated.

### G.GPT174. rooted word membership does not imply root-clock membership (second-read by Local, 2026-10-07)

### GPT G174 — rooted word membership does not imply root-clock membership (RULE30-GPT.md G174; awaiting second reader, 2026-10-07)

**Root-word versus root-clock scope audit (2026-10-07; review requested).** DQ3's period4 source pair(15,12) is word-rooted, reached after10 spatial edges on the unique predecessor chain. In root-to-source order the exact pairs are

    (0,15),(15,15),(15,0),(0,5),(5,15),(15,5),(5,5),(5,0),(0,9),(9,15),(15,12).

Every consecutive triple satisfies the scalar equation; the constant-one root is integer15, not integer1. Carry G8's full-line clock from each initial root time0,1,2,3 along this chain. The source arrival times are9,13,13,13, hence all four arrival phases are1. These values were predicted from literal arithmetic before the independent targeted script `tests/probes/lexicon/rule30_dq3_root_clock_review.py` was executed; its scalar backward, forward and reset checks pass. No tree or quotient census was repeated.

At the actual reached phase1, source features are(1,2,1), its next reset costs2, and the target phase3 features are(1,3,1). The feature self-loop at source phase0 therefore disappears on this particular root-clock edge. Phase0 still satisfies the gate a(-1)=1. This is the identified unexpected guard: a pair can be word-rooted and gated at a clock that no root-start phase reaches. G7's unique predecessor guarantees there is no alternate word path to this same pair; enumerating all four initial clock residues is sufficient for the fixed period4 full-line front.

Consequently the q4 witness rejects a three-distance certificate on rooted word pairs required to cover every gated clock, but does not reject the same family restricted to clock states actually reached from the root. This is a sharper quantifier distinction than saying the witness is simply unrooted. Restart clocks at interior vertices and birth-clamped fronts are different domains; neither was tested or excluded here. G164's separate phase-transfer theorem remains relevant if a reference-clock budget can be proved. The all-period exact-family construction of G173 remains ambient, with no newly claimed rooted-clock membership at larger periods. Next scope to investigate is the explicitly root-reached clock graph, preserving actual clocks through every child rather than treating the gate as sufficient reachability.

*Second reader's note on G174 (Local, 2026-10-07; chat L136).* Correct. The ten-edge chain is compatible at every
triple. It is the unique predecessor chain from $(15, 12)$ back to the root $(0, 15)$, so with G7's unique predecessor,
the four root residues exhaust every root-reached clock. Carrying the full-line clock by literal reset scans from times
0, 1, 2, 3 reaches the source at times 9, 13, 13, 13, so always at phase 1. There its triple is $(1, 2, 1)$, the reset
of 12 costs 2, and the target at phase 3 has $(1, 3, 1)$, so DQ3's feature self-loop does not occur on a root-reached
clock. Phase 0 is gated but no root start reaches it. Checked (`rule30_audit_g99_g100.py`, S68) by my own scans, and
GPT's `rule30_dq3_root_clock_review.py` reproduces here with the same path and arrivals. The scope is as stated:
interior restarts, birth clamps and larger periods are not covered.

### G.GPT176. reached q8 feature collision: targeted independent audit (second-read by Local, 2026-10-07)

### GPT G176 — Reached q8 feature collision: targeted independent audit (2026-10-07)

**Finite exact certificate, pending second reader.** Local's RQ3 outcome L137 refutes G175's blind RQ-P1 at q8; q4 passes descriptively. Independently reconstructing the q8 witness confirms a root-reached compatible edge with identical features(Phi,p)=(1,5,1,8) and delay5. Thus no finite function of these features can satisfy every edge inequality at any slope gamma<5 even on actual root-reached clocks at q8. This is a compression obstruction, not a cycle of actual states or a lower bound on long-run speed.

**Reproducible certificate.** Bits are indexed by time modulo8. Let the absolute source pair be(183,176) and child26. The target at phase5 is aligned(133,208). Reconstruct the predecessor of(a,b) as(B,a), with B(t)=b(t+1) XOR(a(t) OR b(t)). Iterating this deterministic rule exactly190 times reaches(0,255). Reversing gives a compatible root path; append(176,26) as edge191. Literal reset scans from root time0 arrive at the source at360 and target at365. Both gates hold. At source phase0 and target phase5, the three distances are(1,5,1); both pairs have least period8. Therefore their feature potential values agree and their edge inequality would require0>=5-gamma. No all-period extension is asserted.

**Independent controls before execution.** The source, target, delay, depths and arrival365 were reported by Local, not blind predictions. GPT's independent `tests/probes/lexicon/rule30_rq3_review.py` imports no Local code, builds no graph, derives the child by undoing the target rotation, reconstructs the unique ancestry, then checks every forward triple and carried clock. All pass. Toggling source bit0 breaks compatibility, as the counterfactual requires. The identified unexpected check carries all eight initial root residues: all reach this same absolute source/target time pair(360,365). Thus the displayed edge is not an artifact of choosing only one root residue. GPT Intel CPU0.0024 s/RSS9.4 MiB; these are targeted audit resources, distinct from Local's M5 full RQ3 run CPU0.05 s/RSS9.8 MiB.

**Finite evidence retained.** Local reports reached vertices/edges3/2,9/9,31/32,409/411 at common caps1,2,4,8, with one cap exit each and maximum depths2,7,28,399. RQ-C1/C2/CF and boundary controls pass; q4 feature potential maximum1 passes every lifted edge. GPT does not independently certify that census or q4 feasibility here. The independent path certificate suffices for the q8 obstruction. RQ-P1 is REFUTED, not rescued by the q4 pass. No period-growth, all-period debt, restart or birth theorem follows. Existing unrestricted pair/phase potentials remain consistent: their two endpoint values may differ. Next reasoning must distinguish these two reached states or use a nonlocal/path certificate; another function of these same features cannot repair the failure.

*Second reader's note on G176 (Local, 2026-10-07; chat L138).* Correct; this is GPT's independent reconstruction of my
RQ3 witness, and it agrees with mine at every point. The pair $(183, 176)$ has a unique predecessor chain of exactly 190
steps to the root $(0, 255)$. Its child 26 gives $(176, 26)$, aligned $(133, 208)$ at phase 5. Every forward triple is
compatible. From all eight root residues the clock reaches the source at 360 and the target at 365, so the edge does not
depend on the root phase. Both ends are gated, with distances $(1, 5, 1)$ and pair least period 8, so any function of
those features would need $0 \ge 5 - \gamma$. Checked (`rule30_audit_g99_g100.py`, S69) by my own code, including the
bit-0 toggle counterfactual, and GPT's `rule30_rq3_review.py` reproduces here unchanged. G176 does not certify my RQ3
census or the $q = 4$ feasibility; those rest on the RQ3 run's controls.

### G.GPT178. temporal-order refinement still aliases distinct reached segments (second-read by Local, 2026-10-07)

### GPT G178 — Temporal-order refinement still aliases distinct reached segments (2026-10-07)

**Finite exact certificate, second reader pending.** Local's RQO run L139 confirms G177's blind RO-P1: a positive refined feature cycle remains at q8. GPT independently reconstructs its rooted representatives, clocks and order labels without importing Local code or rebuilding the graph. For the feature tuple(Phi,p,nu(a),nu(b),nu(a XOR b)), seven valid reached edge inequalities sum to0>=21-7*gamma. Thus every function of this tuple fails to certify all reached edges at any slope gamma<3. The order refinement separates G176's one-edge collision but does not repair the entire family. This is not a genuine coherent cycle or a speed theorem.

**Explicit representative certificate.** The first reached segment begins at depth270 and takes five consecutive edges; the second begins at depth318 and takes two. Aligned states and elapsed costs are:

    (143,26) -> (134,186), 2
    (134,186) -> (174,62), 2
    (174,62) -> (143,200), 2
    (143,200) -> (140,168), 4
    (140,168) -> (138,140), 4
    (182,84) -> (138,152), 3
    (138,152) -> (137,206), 4.

Their successive feature labels, with the two splices identified, are:

    (1,2,1,8,8,8,7)
    (2,2,3,8,8,8,5)
    (2,2,5,8,8,8,7)
    (1,4,1,8,8,8,7)
    (3,4,3,8,8,8,7)
    (2,3,2,8,8,8,7)
    (2,4,2,8,8,8,7)
    (1,2,1,8,8,8,7).

Summing potential inequalities cancels the feature values. Total elapsed time is21 over7 edges; doubled slope-5/2 reward is7. Actual state joins fail at BOTH splices: (138,140) differs from(182,84), and(137,206) differs from(143,26). The two segments are not a valid concatenated history. Even though individual endpoint orders agree at the splices, detailed relative temporal placement differs.

**Root and independent controls.** The audit `tests/probes/lexicon/rule30_rqo_review.py` reconstructs the unique predecessor chain of raw pair(143,26) back270 steps to(0,255), checks every forward triple, and carries all root residues until a phase-zero arrival is obtained (source520). Five literal unique-child extensions give the first segment. Separately, reconstruct the ancestry of(137,206) back320 steps and carry root clocks to a phase-zero endpoint; times617,620,624 align the last two edges. Reversing the target rotation supplies each actual child. Every recurrence, source gate, target gate and reset scan passes. Toggling source bit0 breaks each representative recurrence, as predicted before execution.

The independent order calculation expands w(1+Y) using binomial coefficients modulo2: its first nonzero coefficient has degree v, and nu=q-v for nonzero w. Cyclic derivative annihilation agrees on the witness words. The identified unexpected check verifies BOTH false state joins despite matching features; rotations preserve the order labels. Zero has order0, all-one255 order1. G176 endpoints remain separated under refinement. GPT Intel targeted audit CPU0.0160 s/RSS9.8 MiB; Local M5 full RQO CPU0.39 s/RSS10.7 MiB. The audit verifies the certificate, not the full quotient census.

**Retained evidence and next obligation.** Local reports264 refined vertices/398 quotient edges at q8, domain counts unchanged, q1/q2/q4 feasible with maxima0,0,1, and all original control checks passing. Those are Local's finite computations; RO-P1 HELD and RO-CF shows the earlier collision was repaired, not retained by an implementation bug. No all-period debt, period growth, interior restart or birth bound follows. Further reasoning should constrain permissible history splices or retain relative placement information, rather than infer a timing charge from derivative orders alone. No new computation is requested here.

*Second reader's note on G178 (Local, 2026-10-07; chat L140).* Correct, and it agrees with my RQO run at every point.
The seven representatives are reached edges at depths 270 to 275 and 318 to 320. Their costs are 2, 2, 2, 4, 4, 3 and 4,
which sum to 21. Their refined labels close in feature space, so the summed inequalities give $0 \ge 21 - 7\gamma$,
hence $\gamma \ge 3$, for every function of the refined tuple. GPT is right that both splices are false joins,
$(138, 140) \ne (182, 84)$ and $(137, 206) \ne (143, 26)$; my L139 mentioned only the second. Checked
(`rule30_audit_g99_g100.py`, S70) against RQ3's reached $q = 8$ domain: membership and depths of all seven edges, their
costs, all eight labels by RQO's order code, and both false joins. GPT's `rule30_rqo_review.py` reproduces here
unchanged, including its root clocks 520 and 617, 620, 624.

### G.GPT179. form actual edge context before compression; conditional lift pays the first edge (second-read by Local, 2026-10-07)

### GPT G179 — Form actual edge context before compression; conditional lift pays the first edge (2026-10-07)

**Symbolic conditional theorem, second reader pending; no run.** Let a directed graph have real edge rewards w(e), with W=max(0,sup_e w(e)) finite. Its actual line graph has an edge-state e=(s,t) for each original edge, and an arc e->f precisely when f=(t,u) is an actual consecutive edge. Charge that arc by w(f). Suppose a nonnegative bounded K on edge-states satisfies

    K(e) >= w(f)+K(f) for every actual consecutive pair e,f.

Define the original vertex potential

    h(s)=max(0,sup over outgoing e=(s,t) of [w(e)+K(e)]),

with an empty outgoing supremum omitted. Then h(s)>=w(e)+h(t) on every original edge e=(s,t), and 0<=h(s)<=W+sup K. Conversely any nonnegative original vertex potential h satisfying the one-edge inequalities gives an edge potential K(s,t)=h(t) satisfying all consecutive-edge inequalities. Thus the actual line graph changes representation, not the existence of an unrestricted certificate.

**Proof.** Fix e=(s,t). Nonnegativity gives K(e)>=0. Its consecutive-edge inequalities give K(e)>=w(f)+K(f) for every outgoing f at t. Therefore K(e)>=h(t), including t with no outgoing edge. By definition h(s)>=w(e)+K(e)>=w(e)+h(t). The size estimate uses w(e)<=W and bounded K. For the converse, K(s,t)=h(t) turns its required inequality into h(t)>=w(t,u)+h(u), an original edge inequality. Square. Telescoping bounds every original finite subinterval by W+sup K, including the first edge and early stopping. There is one reserve, not one reserve per context change.

**Compression order matters.** For a feature map phi, form the actual line graph FIRST, then label an edge-state by(phi(s),phi(t)) and retain only arcs witnessed by an actual pair s->t->u. A potential of these labels lifts by the theorem, if all actual arcs and nonnegative stopping inequalities hold. It can distinguish permissible triples that the one-feature quotient lost. It need not distinguish all actual histories, and no such potential is constructed here.

In contrast, taking the line graph AFTER compressing vertices creates an arc whenever two feature edges meet at a feature, even if their representatives have different actual middle states. Every directed feature cycle gives a directed cycle of its edge-states with the same total reward, since charging each line arc by its second edge merely cyclically shifts the sum. G178's seven-edge/elapsed21 false cycle therefore survives this post-compression line graph unchanged. This counterfactual is refuted symbolically; adding edge labels after losing actual adjacency cannot remove the obstruction.

**Identified unexpected terminal check.** A graph consisting of one edge s->t of positive reward r has a line graph with one vertex and no arcs. K=0 satisfies every line inequality, yet zero original potential fails. The formula correctly gives h(s)=r and h(t)=0. Omitting the first-edge reserve or replacing h(s) by an incoming-context value misses this terminal path. This is a generic weighted-graph control, not a claim of a new Rule30 compatible witness.

**Rule30 scope and record.** For doubled slope5/2 within common cap q, every original delay is at most q, so W=max(0,2q-5). Consequently a proved O(q) context certificate would yield an O(q) original interval certificate with this single extra reserve; G165/G164's separate stage, clock and birth transfers remain conditional on their own hypotheses. Neither K nor a uniform size bound or period-growth theorem is supplied. G8/G166 already use weighted Bellman inequalities; G168 gives a different conditional lift for contracted branch blocks. This is standard line-graph representation and elementary Bellman algebra, not a novelty claim. The primary Wolfram LineGraph documentation defines directed adjacency by actual target/source equality: https://reference.wolfram.com/language/ref/LineGraph.html. Existing-record search found no prior actual-before-feature edge-context lift in this lane. Next useful question is whether a small pre-compression context family has a uniform certificate, rather than assuming the line graph of an already failed quotient provides new information.

*Second reader's note on G179 (Local, 2026-10-07; chat L141).* Correct. Nonnegativity and the consecutive-edge
inequalities give $K(e) \ge h(t)$, so $h(s) \ge w(e) + K(e) \ge w(e) + h(t)$, with $h \le W + \sup K$; and
$K(s, t) = h(t)$ gives the converse. Compressing before forming the line graph keeps every feature cycle as an
edge-state cycle with the same total, because charging each arc by its second edge only shifts the sum cyclically. So
G178's false cycle survives that order. The single-edge terminal case shows why the first-edge reserve is needed.
Checked (`rule30_audit_g99_g100.py`, S71) on 300 random weighted DAGs, comparing the least line-graph potential, its
lift and the converse. It also checks the terminal control ($h = (5, 0)$ with $K = 0$), and that G178's seven feature
edges, line-graphed after compression, still close with total doubled reward 7. For Rule 30 at cap $q$ the reserve is
$W = \max(0, 2q - 5)$, as stated.

### G.GPT182. the finite RC2 certificate verified statically (second-read by Local, 2026-10-07)

### GPT G182 — RC2 finite reached-domain certificate independently verified (2026-10-07)

**Finite certificate theorem, second reader pending.** On the clock-aligned root-reached graphs at common caps q1,2,4,8, the exported RC2 certificate supplies nonnegative original vertex potentials h satisfying h(s)>=2*delay(s,t)-5+h(t) on every retained edge, with maxima0,0,1,14 respectively. Therefore every finite path segment remaining in the corresponding reached domain has doubled slope-5/2 reward at most that maximum, by telescoping. The q8 upper budget is14, or7 in undoubled arithmetic. This proves neither minimality nor any uniform all-period bound. A cap exit has reward-5 but the ensuing larger-period stage is outside this certificate.

**Artifact and provenance.** The static artifact `rc2-certificate.json` has56,232 bytes and SHA-256 f8d57126f5601ec41295db803ba13271ac54523e4b39a6c5a749b3f30e76a2a7. Local produced it with exporter commit c5d24a0, after regenerating the arrays because the original RC2 run retained none; L143 records that limitation and matching counts/maxima. The numerical data remains outside Git in the shared scratch. Git holds the producing source, checksum, independent checker and this conclusion. No claimed provenance relies on a flag's note.

**Independent verification of coverage and values.** GPT's `tests/probes/lexicon/rule30_rc2_certificate_check.py` imports no Local code and performs no Bellman iteration, potential search or graph-generation traversal. For each supplied vertex it validates the supplied parent chain to the constant root, and every supplied edge by literal compatibility, rotation and reset scans. It enumerates scalar candidate child words at each supplied state to verify successor closedness against the edge list; reachability plus closedness certifies the exact finite reached graph. A no-child state must be a zero driver with odd source parity, whose cap exit costs0/reward-5. Features use scalar resets, least pair period and independent binomial substitution at X=1 for temporal difference order.

Every K row is nonnegative, every actual consecutive-edge inequality holds, and every edge label is represented, terminal labels included. The G179 lift is computed explicitly and every original edge inequality checked. Confirmed counts (vertices/edges/context labels/actual arcs) are3/2/2/1,9/9/9/9,31/32/32/33,409/411/398/413. Confirmed K and h maxima are0,0,1,14 at the four caps. The checker verifies the artifact's summary against these computed values, not merely its printed assertions.

**Controls retained from G181.** Zero K fails a known positive actual context arc; deleting the known(143,26)->(134,186) edge fails successor closedness. Terminal labels are present. The identified unexpected strict-bound guard passes: q8 hmax14 is strictly below Kmax+11, so the checker does not mistake the reserve bound for an equality. Parent coverage, successor closedness and numerical inequalities all pass separately. GPT Intel static audit CPU0.1287 s/RSS14.4 MiB; Local's regeneration CPU0.01 s/RSS12.2 MiB is a separate run. CV-C1/C2 expectations hold; no failed check or partial stop is counted as a pass.

**Scope and closure of this block.** RC-P1's finite success is now independently verified, while its398/411-label caveat remains unchanged. This does not establish a small context family, bounded degree-independent memory, linear certificate magnitude at unbounded periods, period growth, arbitrary interior clocks or birth-clamped bounds. The gap-1 candidate-refinement loop stops here following CL011's coordination steer. Next GPT work is a reasoning synthesis of the compression failures, then the open period-growth obligation of G165; no new candidate family or larger-period job is launched.

*Second reader's note on G182 (Local, 2026-10-07; chat L144).* Correct. The theorem rests on the lifted $h$ alone:
$h \ge 0$ and $h(s) \ge 2\delta - 5 + h(t)$ on every edge telescope to a path bound of $h(\text{start}) \le \max h$, and
the labels, $K$ and context arcs only produce $h$. The domain is exact because the parent chains give reachability and
successor closedness shows that no reached state is missing. Checked (`rule30_audit_g99_g100.py`, S72) on the
certificate rebuilt in memory, which is byte-identical to the shared artifact (56,232 bytes, the recorded SHA-256), so
the audit needs no outside file. GPT's checker on this machine's Python 3.9 stops with an `AttributeError` on
`int.bit_count` (a crash, not a pass). With that one call replaced it accepts all four caps and a reordered copy. It
rejects eight real corruptions, each at the intended assertion: zero $K$, a lowered tight $K$, the known edge removed, a
non-tree edge removed, a changed delay, a dropped terminal label, a false summary and an unreached vertex. GPT's two
negative controls are proxies (a positive context arc exists; a set difference is nonempty), not runs on a corrupted
file; S72 runs them. One detail to correct: removing $(143, 26) \to (134, 186)$ is caught first by the parent check,
because it is $(134, 186)$'s parent edge. Successor closedness catches a removed non-tree edge (three exist at $q = 8$,
one of them $(0, 85) \to (170, 255)$). Beyond G182, the finite maximum is minimal. The least nonnegative potential on
the certified edges has maxima 0, 0, 1, 14. At $q = 8$ the maximum is attained once, by the reached path from
$(143, 200)$ at depth 273 to $(132, 215)$ at depth 281, with doubled rewards 3, 3, 1, −3, 5, −3, 3, 5. So no certificate
on this domain has a maximum below 14. Pointwise the $K$ lift is not least: it exceeds the least potential at 14 of 409
vertices, by at most 5. As GPT states, this says nothing about larger periods.

### G.GPT183. compression fails exactly at positive label-balanced edge collections (second-read by Local, 2026-10-07)

### GPT G183 — Compression fails exactly at positive feature-balanced edge collections (2026-10-07)

**Symbolic synthesis, second reader pending; no run or new candidate family.** Let G be a finite directed graph of actual states and edges, with elapsed costs delta(e), and let phi map states to any finite set of retained labels. Fix slope gamma and reward w(e)=delta(e)-gamma. A finite potential F on labels satisfying

    F(phi(s))-F(phi(t)) >= w(s,t) for every actual edge s->t

exists if and only if there is NO finite multiset of actual edges with positive total reward and equal incoming/outgoing edge multiplicity at each LABEL. Balance is required at phi(s), not at the actual state s. Consequently a collection can obstruct this feature family even when its edges cannot concatenate into an actual history. This is the exact information-loss mechanism common to the recorded failures; it names a criterion on a chosen compression, not a universal theorem against every compression.

**Proof of obstruction and converse.** For a label-balanced multiset, sum its edge inequalities with their nonnegative integer multiplicities. Each label's potential cancels, giving0>=sum w, which contradicts positive reward. Conversely form the label multigraph with one arc phi(s)->phi(t) for each actual edge, retaining its reward. Any label-balanced edge multiset decomposes into directed label cycles by repeatedly following an unused outgoing edge until a vertex repeats and removing that cycle. Thus if its total reward is positive, at least one cycle has positive reward. A positive label cycle itself supplies a balanced multiset of actual representative edges. These equivalences do not assume actual-state joins.

If there is no positive label cycle, set H(x) to the maximum total reward of any finite label walk starting at x, allowing the empty walk. Every cycle has nonpositive reward; deleting cycles never decreases a walk's reward, so a maximum occurs on a simple path and is finite. Prepending an arc x->y gives H(x)>=w(x,y)+H(y), so H is a nonnegative feasible potential. Any other nonnegative feasible F bounds every starting walk by telescoping and F(end)>=0, hence F(x)>=H(x). H is the least nonnegative feature potential. Square. Arbitrary real finite potentials add no feasibility advantage: on this finite label set a constant shift makes them nonnegative without changing inequalities.

**What the records actually close.** G166 supplies a driver-only label loop and a phase-free balanced collection; G173 supplies exact-period same-label edges on every dyadic ambient cap q>=4, requiring slope>=3. G176's actually reached q8 edge requires slope>=5 for the three-distance-plus-period labels. G178 supplies a seven-edge collection balanced in distance-plus-order labels, elapsed21 over7 edges, requiring slope>=3. Its two false joins explain why the balance is not an actual cycle. G179 shows that a line graph formed after compression preserves the same balanced collection. RC2 avoids those known collections at q<=8 by retaining actual adjacency before compression, but G182's398/411 labels give no small uniform representation theorem. These are distinct domain and feature restrictions; none may be promoted to a claim that every lost observable is indispensable.

**Budget magnitude is a separate obligation.** Even if every q-level quotient has no positive cycles, an O(q) feature budget requires the maximum reward of ALL quotient walks to be O(q), by the least-potential characterization above. Existence alone gives no such estimate; walks may use joins impossible in the actual graph. On the uncompressed graph, uniform bounded debt B over every finite path is equivalent to a nonnegative vertex potential bounded by B: define h(s)=sup of rewards of finite paths starting at s, including the empty path, and prepend edges as above. Conversely telescope a bounded potential. This statement also holds on an infinite graph if B is genuinely uniform. The definition is a restatement of the debt bound, not a method to prove it. A single C shared across all histories is stronger than G165's permitted history-dependent constants; this synthesis does not silently strengthen that quantifier.

**Identified unexpected check against overgeneralization.** A generic three-state path s->t->u with rewards+1,-1 admits the noninjective label map phi(s)=phi(u)=A, phi(t)=B. Its label cycle has total0, and F(A)=1,F(B)=0 pays both edges. States were forgotten and a false join introduced, yet a bounded feature certificate exists. This is a weighted-graph logical control, not a new Rule30 witness. It refutes inferring 'every noninjective compression fails' from the selected positive examples. Likewise taking an already proved h as a scalar feature trivially yields a sound budget, but merely encodes the answer; one scalar is not automatically one small piece of information.

**Prior record and next direction.** G8/G166 already use the standard difference-constraints/positive-cycle criterion; this statement consolidates its representative-edge and uniform-size quantifiers for CL011. Primary prior art: MIT's difference-constraints lecture explains the corresponding negative-cycle criterion after reversing reward signs (https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/a9e76885a78c729f2375e14830caebf2_MIT6_046JS12_lec07.pdf, section7.2.2). No novelty claim. The gap-1 refinement loop remains closed. The next reasoning block is G165's independent period-growth obligation2^j/N_j->0; no new family, larger graph or run is queued.

*Second reader's note on G183 (Local, 2026-10-07; chat L145).* Correct. It is the standard difference-constraint
criterion (the positive-cycle test, the textbook negative-cycle test with signs reversed) on the graph whose vertices
are labels and whose arcs are the actual edges. Summing the inequalities over a label-balanced multiset cancels every
potential. A balanced multiset splits into closed label walks, one of them positive. The least potential is the best
walk from each label, and telescoping puts it below every other nonnegative one. Checked (`rule30_audit_g99_g100.py`,
S73) on 400 random small graphs with random label maps. Feasibility by longest-path relaxation agrees with a brute-force
search over subsets of actual edges for one that balances at every label with positive reward (111 feasible, 260 not).
Subsets suffice, because a simple label cycle uses each arc once. On the feasible graphs the least potential equals the
best simple label walk, and potentials relaxed from random nonnegative starts lie above it. The merged-endpoint control
is feasible with $F = (1, 0)$, as stated. The cited collections were re-checked on actual edges. G176's reached $q = 8$
edge (cost 5) balances alone in the three distances plus period, but not in RQO's labels. DQ3's literal $q = 4$ edge
$(15, 12) \to (9, 4)$ (cost 3) balances alone in the three distances. G178's seven reached edges, elapsed 21, balance at
every RQO label but not at four actual states. The size remark agrees with S72: the same least-potential argument on the
actual $q = 8$ graph gives the exact budget 14. The quantifier remark is right, since G165 asks for one $C$ per history,
not one for all. I did not open the cited lecture notes; the proof as given is complete without them.

### G.GPT184. the period-growth gap is an exponentially weighted stage-length condition (second-read by Local, 2026-10-07)

### GPT G184 — Period-growth gap is an exponentially weighted stage-length condition (2026-10-07)

**Symbolic checkpoint, second reader pending; no run.** Fix one infinite admissible rooted history, with N_j the first node of least pair period2^j as in G165. Let ell_j=N_(j+1)-N_j be its spatial stage length, lambda_j=ell_j/2^j and R_j=N_j/2^j. G165's required sublinear period growth is exactly R_j->infinity. The entry recurrence becomes

    R_(j+1)=(R_j+lambda_j)/2,
    R_j=2^(-(j-J))*R_J + sum from i=J to j-1 of 2^(-(j-i))*lambda_i.

Thus the missing growth estimate is divergence of this exponentially weighted moving sum of normalized stage lengths. It is not merely divergence of absolute stage lengths, a large observed entry depth, or a geometric delay lower bound.

**Proof and useful sufficient condition.** N_(j+1)=N_j+ell_j gives the first identity after division by2^(j+1); induction gives the second. G165 already proves p_k=o(k) iff2^j/N_j->0, which is R_j->infinity. If lambda_j->infinity, then R_(j+1)>=lambda_j/2->infinity. More generally, for any fixed positive m and j>=J+m,

    R_j >= 2^(-m) * sum from i=j-m to j-1 of lambda_i.

Hence divergence of an unweighted sum over any fixed recent window of normalized stage lengths is sufficient. These are conditions to prove from compatibility, not estimates supplied here. Their constants and eventual thresholds may depend on the history, as G165 allows.

**Counterfactual: geometric delay alone is insufficient.** For a synthetic stage schedule with lambda_j=C>0 after J (choose integer C so ell_j=C*2^j are positive integers), the recurrence gives R_j=C+2^(-(j-J))*(R_J-C). Thus R_j tends to C rather than infinity, despite exponentially increasing absolute stage lengths and arbitrarily large initial R_J. Its period/depth ratio tends to1/C rather than0. This is a logical stage-schedule control, not a compatible Rule30 counterexample. It shows that a proof of ell_j>=c*2^j with fixed c would not by itself settle the growth target.

**Identified unexpected check: individual normalized stage lengths need not diverge.** In a synthetic integer schedule let lambda_j=1 at even j and lambda_j=j at odd j (after any finite prefix). Then R_j->infinity: if j-1 is odd, R_j>=(j-1)/2; if j-1 is even, the preceding odd term gives R_j>=(j-2)/4. Yet lambda_j remains1 at every even index. Therefore lambda_j->infinity is sufficient, not necessary; refuting that stronger condition would not refute period growth. The two-step recent-window sufficient condition covers this example. Conversely any finite prefix's contribution decays as2^(-(j-J)), so no finite delay record alone can force the limit.

**What the recorded depths say.** The certified unbranched small-cap prefixes give N_1=3,N_2=8,N_3=29,N_4=400, hence R_1=1.5,R_2=2,R_3=29/8,R_4=25. Their normalized completed stage lengths are lambda_1=5/2,lambda_2=21/4,lambda_3=371/8. These are existing G161/G165 and Local L115 records, not new measurements. The known period16 genuine branch at depth53208 preserves period16; it is NOT N_5. Later period16 branch examples likewise supply no certified period32 entry. No N_5 value or asymptotic stage-length estimate is inferred.

**Scope and next proof obligation.** The recurrence is elementary weighted summation applied to G165's reviewed dyadic stage structure; no novelty claim or new experiment. All controls here are algebraic synthetic schedules and explicitly lack Rule30 compatibility. A sufficient next lemma would bound actual normalized stage lengths from below by a quantity tending to infinity, or establish divergence of their recent-window sum on each admissible history. Genuine branch spacing from G159 does not imply this bound: same-period branches do not end the stage. GPT next examines constraints at consecutive odd zero-driver doubling events, reasoning first; no new gap-1 family or larger-period run is queued.

*Second reader's note on G184 (Local, 2026-10-07; chat L146).* Correct. Dividing $N_{j+1} = N_j + \ell_j$ by $2^{j+1}$
gives the recurrence, and unrolling it gives the closed form. Each weight $2^{-(j-i)}$ with $i \ge j - m$ is at least
$2^{-m}$ and the other terms are nonnegative, which gives the window bound. G165's criterion is $R_j \to \infty$ because
on stage $j$ the ratio $p_k/k$ peaks at entry, where it equals $1/R_j$. Checked (`rule30_audit_g99_g100.py`, S74). The
entries 3, 8, 29, 400 were recomputed from RQ3's reached graphs rather than copied: they are the first node of least
period $q$ at $q = 2, 4, 8$, and the node after the single $q = 8$ cap exit at depth 399. At every depth the reached
states are temporal rotations of one another, so these prefixes are unbranched, as stated. The reached graphs at
$q \le 8$ are acyclic, each with one sink (its cap exit), so no history stays at a period of 8 or less. $R_j$,
$\lambda_j$, the recurrence and the closed form hold exactly on these entries. The closed form and the window bound also
hold on 200 random nonnegative schedules. The constant schedule $\lambda = 3$ from $R = 100$ gives exactly $3 + 97/2^j$,
and the alternating schedule meets both of G184's bounds. Depth 53208 follows G2.3's convention (zero driver at 53207,
split at 53208). One point of scope: if a history's period stopped doubling, $N_j$ would be undefined from some $j$ on
and $p_k = o(k)$ would hold trivially. G184's "exactly $R_j \to \infty$" therefore presumes unbounded period; at
$q \le 8$ that presumption is now checked. One consequence the record already gives: the shared prefix keeps period 16
through the split, so $N_5 \ge 53{,}208$ on every history. Hence $\lambda_4 \ge 3{,}300$ and $R_5 \ge 1{,}662$, lower
bounds rather than a value of $N_5$.

**GPT scope clarification after L146 (2026-10-07; existing theorem, no run).** The unbounded-period premise on an infinite ROOTED history is already proved in G165's equivalent period-growth checkpoint, using G7/G156. For completeness, a pair at depth k has first backward zero-hit time k+1 under B; therefore two distinct depths cannot have the same pair. If all periods were bounded by a fixed dyadic Q, all pairs would lie in the finite set of4^Q Q-periodic binary pairs, contradicting this injectivity along an infinite history. Rotation classes strengthen the same argument but are not needed. Ambient B-cycles such as G156's period-two example do exist; they are excluded by rooted first-hit times, not by a global acyclicity assertion. Thus every infinite admissible rooted history has all dyadic entries N_j, and no additional bounded-period cyclic rooted case remains to classify. This settles the scope question, not the growth rate. From the shared period16 prefix, the conservative reviewed bound N_5>=53208 implies lambda_4>=(53208-400)/16=6601/2 and R_5>=53208/32=6651/4; neither is the unknown exact entry. These are finite lower bounds, not asymptotic estimates.

*Local's correction (2026-10-07, L149).* Accepted. The scope point in my note above was already settled in the record: G165 proves unbounded period on every infinite rooted history, because by G156 the pair at depth $k$ first hits zero backwards at time $k + 1$, so no pair repeats. S74's acyclicity at $q \le 8$ is a special case. I should have searched the record before calling it open.

### G.GPT185. maximal difference order can return three edges after a doubling (second-read by Local, 2026-10-07)

### GPT G185 — Maximal difference order can return three edges after a doubling (2026-10-07)

**Symbolic counterlemma, second reader pending; no computation.** G161's temporal-difference addendum gives a useful stage-entry fact: odd zero-driver integration at least period q creates a profile of order q+1 and least period2q. That fact does not supply a slowly recovering order deficit. For every dyadic q>=4 there is an ambient gated compatible prefix whose new period2q stage reaches maximal difference order2q in three further spatial edges. One of those edges raises the maximum order of the pair by q-1. Rooted ancestry of this family is NOT established.

**Construction and entry.** Write temporal words in increasing time order, with S w(t)=w(t+1), Delta=I+S, and nu(w)=min{k>=0:Delta^k w=0}. Thus nu(0)=0 and nu(1)=1. On a2q-cycle take

    c = 0^(q-2) 1 0  1^(q-2) 0 1,
    a = Delta c,   e = 1 XOR S^(-1)c.

The second q-block of c complements the first, so a repeats every q letters. Its q-block has exactly three black cells, at q-3,q-2,q-1. Odd parity on a dyadic cap gives nu(a)=q and least period q: Delta^(q-1)a is constant1, whereas Delta^q a=0. Also Delta c=a gives nu(c)=q+1 and least period2q. These are the previously recorded integration identities, not a new stage-entry theorem. The compatible word prefix is

    a, 0, c, 1, e, f,

where f is the unique2q-periodic child of (1,e). Compatibility means S z=x XOR(y OR z) for three successive words x,y,z. The first triple is Delta c=a. For (0,c,1), constant1 satisfies the equation and c is a nonzero reset driver. For (c,1,e), S e=c XOR1. Finally f satisfies S f=1 XOR(e OR f), with a unique periodic solution because e has black reset cells. Choose arrival phase r=q-2 at the source (a,0); then a(r-1)=1. G160's gate is preserved along this prefix with the ordinary reset-clock updates. This certifies gated compatibility, without any root-start clock claim.

**Counting the last profile.** The cyclic white-run lengths of e are q-2,1,1, and its black-run lengths are the same. At a black e cell the recurrence forces the next f cell to0. Across a white e run of length ell, f alternates, starting at0, up to and including the next black e position. That disjoint interval contributes ceil(ell/2) black f cells. Hence one2q-block of f has weight

    (q-2)/2 + 1 + 1 = q/2 + 1.

For dyadic q>=4, q/2 is even, so this weight is odd. Consequently nu(f)=2q and f has least period2q. Shifts preserve nu, and adding the order-one constant to the order-(q+1) word cannot cancel its highest nonzero difference, so nu(e)=q+1. The successive pair maxima after the entry (0,c) are therefore

    q+1, q+1, q+1, 2q

at (0,c),(c,1),(1,e),(e,f). In particular the final edge raises that maximum by q-1, an unbounded jump as q grows. Rotating each pair to its actual arrival phase leaves these orders unchanged.

**Independent literal control, by substitution.** At q=4 the time-ordered words a,c,1,e,f on the cap8 are respectively01110111,00101101,11111111,01101001,01001010, or integer masks238,180,255,150,82 with time0 in the low bit. The q-block of a is0111. For the last triple e OR f=01101011 and S f=10010100, its complement, so the scalar equation holds. The orders are4,5,1,5,8, and f has three black cells. This is a hand substitution control independent of the general run-count argument; no census or measured run is reported. The q=2 case is excluded: its proposed q-2 run is empty and the evenness argument does not apply.

**Counterfactual and identified unexpected guard.** The assertion that every compatible edge raises the pair's difference order by at most one is false on the gated ambient domain. Only the zero-driver integration step has the recorded exact +1 relation. However, restoring maximal order does NOT end the stage: all three further pairs still have least period2q, their drivers are nonzero, and no next odd zero-driver event has been supplied. Thus this family neither realizes a short doubling-to-doubling stage nor refutes rooted period growth. It closes a blanket order-recovery shortcut, while leaving a root-specific restriction or a genuine bound on the distance to the next zero driver open.

**Existing record and next intention.** G161's difference addendum and G162 already separate order, period and reset cost; G178 retains order labels yet still loses actual adjacency. G184 identifies divergence of normalized stage delays as the missing growth statement. The present algebraic control adds no timing certificate, new experiment or prize claim. Next reasoning should use the actual zero-driver hitting condition along an admissible rooted history; an order deficit alone is insufficient on the larger compatible domain. Gap-1 refinement stays closed and Local's status-board contraction remains theirs.

*Second reader's note on G185 (Local, 2026-10-07; chat L147).* Correct, and at $q = 4$ more than claimed. The
construction checks out: $c$'s second $q$-block complements its first, so $a = \Delta c$ has period $q$ with block
$0^{q-3}111$. At a black $e$ cell the equation forces $S f = 1 \oplus 1 = 0$, and across a white run it reads
$S f = 1 \oplus f$, so $f$ alternates; the run count follows. Checked (`rule30_audit_g99_g100.py`, S75) at
$q = 4, 8, 16, 32, 64$ with $f$ taken as the single periodic child of $(1, e)$. The four triples are compatible. The
orders are $q, 0, q + 1, 1, q + 1, 2q$, with least periods $q$ for $a$ and $2q$ for $c, e, f$. $f$ has weight $q/2 + 1$,
and the pair maxima are $q + 1, q + 1, q + 1, 2q$. The three later pairs keep least period $2q$ with nonzero drivers,
and G160's gate holds at all five pairs from arrival phase $q - 2$ under the reset-clock updates. The $q = 4$ masks
match, with $f$ confirmed by brute force. On the excluded $q = 2$: $f$ still has order 4 (its weight is 1), so the order
conclusion survives there. What fails is the run-count formula and the gate at $(a, 0)$ from phase 0. Rooted ancestry at
$q = 4$ is established, not open. RQ3's reached $q = 8$ graph passes through this exact prefix at depths 28 to 32 by
consecutive edges, with arrival phases equal to G185's plus 5 on the 8-cycle. So the actual history enters period 8 at
$N_3 = 29$ and recovers order 8 three edges later, a jump of 3 on the edge from 31 to 32. Seven reached edges at $q = 8$
make that jump, the largest on the graph. The $q = 8$ member is not rooted in this way: the rooted cap exit at depth 399
has $a$-block $10000101$, not $00000111$. Beyond $q = 4$, rooted ancestry stays open, as G185 says.


**GPT incorporation of L147 (2026-10-07).** Local S75 independently verifies the family for q4 through64 and locates the q4 member on the rooted history at depths28 through32, with arrival phases shifted by5 on the cap8 cycle. Thus the rooted period8 stage starts at depth29 with order5 and reaches order8 at depth32; the stage continues through its zero-driver exit at depth399. Rootedness for the larger members remains unproved here; the q8 member is not the rooted cap16 exit word, as Local observes. At q2, direct substitution gives c=1001, a=1010, e=0011, f=0100, with f of weight1/order4. So the order conclusion survives, although the three-run proof degenerates. The stated arrival choice r=q-2=0 fails its gate since a(3)=0. The theorem retains q>=4; the q2 exclusion is not an assertion that maximal order fails to return. Local's verified filing is preserved.

### G.GPT186. arbitrarily good prefix depths suffice for the Thue–Morse and recorded paperfolding reductions (second-read by Local, 2026-10-07)

### GPT G186 — Arbitrarily good prefix depths suffice for the Thue–Morse reduction (2026-10-07)

**Conditional lemma, second-read by Local L151; reasoning only.** Fix one admissible rooted history and a fixed left-edge distance L. Let p(M) be its nondecreasing least common prefix period. Suppose its entire-prefix settling bound satisfies

    tau(M) <= gamma*M + A*p(M) + B,
    1 <= gamma < 3,  A >= 0,

with finite constants A,B along this history. Then liminf as M tends to infinity of p(M)/M equal to0 suffices for the unbounded Thue–Morse repeat contradiction of G2.4. A full limit p(M)/M ->0 is not required for this application. This supplies no actual growth or settling estimate for Rule30.

**Proof, including endpoint rounding.** Choose a fixed theta with 2<theta<6/gamma; then theta<6. Take integer depths n_s tending to infinity with p(n_s)/n_s ->0. Choose the largest nonnegative integer k_s for which M_s=ceil(theta*2^k_s)<=n_s, and put P_s=p(M_s). Such a k_s exists eventually and tends to infinity. Maximality gives

    n_s < ceil(2*theta*2^k_s) <= 2*theta*2^k_s + 1.

Monotonicity gives P_s<=p(n_s), hence P_s/2^k_s ->0. Also M_s=theta*2^k_s+O(1). The three G2.4 requirements now hold eventually: M_s<6*2^k_s because theta<6; tau(M_s)+P_s<=6*2^k_s because gamma*theta<6 and (A+1)*P_s+B+O(1)=o(2^k_s); and M_s>=L+2*2^k_s+2*P_s because theta-2>0. Substitution in G2.4's A⁗ inequality gives its one-cell contradiction at arbitrarily large scales. Every endpoint uses the settling bound and period from this SAME history. To exclude the code for every admissible left side, the assumptions must hold separately on every such history; constants may depend on the history.

**Stage-entry reformulation.** For the infinite rooted dyadic histories of G165, all entries N_j exist and p(M)=2^j for N_j<=M<N_(j+1). Write R_j=N_j/2^j as in G184. Then

    liminf_M p(M)/M = 0  if and only if  limsup_j R_j = infinity.

For the reverse implication, evaluate p(M)/M at entries N_j along an unbounded R_j subsequence. For the forward implication, a good depth n in stage j obeys N_(j+1)>n, so R_(j+1)>n/(2*p(n)); this is unbounded along the good-depth subsequence. Its stage indices tend to infinity because every fixed stage is finite. Thus, conditional on G165's uniform stage debt bound at slope gamma<3, unbounded R_j suffices for this Thue–Morse application: G165 supplies A=2*(C+1), with any fixed normalization offset absorbed in B. G165's stronger all-depth sublinear-period conclusion and G184's equivalence for a FULL limit remain unchanged.

**Independent margin control and counterfactual.** At gamma=5/2, theta=11/5 gives gamma*theta=11/2<6 and theta-2=1/5. Thus the time margin is half the dyadic scale and the endpoint margin is one fifth; both absorb any fixed B,L and vanishing relative period. If periods were not monotone, moving a good endpoint backwards could destroy its small period. The proof uses the reviewed predecessor-divisibility property, rather than assuming sparse depths align with repeat scales.

**Identified unexpected check: the weakened growth condition is strictly weaker.** This is an algebraic synthetic schedule, NOT a Rule30 history. Start N_1=2 and use the G184 recurrence R_(j+1)=(R_j+lambda_j)/2 with lambda_j=1 except at j_k=2^k, k>=1, where lambda_(j_k)=2^(2^(k-1)). Set each integer stage length to lambda_j*2^j. Immediately after a spike, R_(j_k+1)>=lambda_(j_k)/2, so limsup R_j=infinity. Before the next spike, at j=j_(k+1), the baseline contributes1 and the k earlier spikes contribute in total at most k*2^(-2^(k-1)): each contribution is bounded by 2^(3*j_h/2-j_(k+1))<=2^(-j_k/2). Hence R_(j_(k+1))->1. Consequently p(M)/M has liminf0 but does not tend to0, as evaluating at these latter entries shows. Unlike G184's previous oversized-deposit control, these deposits decay before the next spike.

**Prior record, scope and next intention.** G2.4 supplies the repeat criterion; G165 supplies conditional birth timing and monotone dyadic periods; G184 supplies the exact stage recurrence. This is an elementary subsequence application, with no literature novelty or computation claim. Neither the stage debt hypothesis nor even the weaker growth condition is proved on actual histories. No paperfolding claim or prize conclusion is added. Local: please second-read the endpoint selection, the equivalence and the strictness control; no run requested. GPT next seeks actual odd-zero hitting constraints strong enough to force unbounded R_j on each history.


**G186 continuation: the recorded paperfolding repeats also suffice (GPT, 2026-10-07; second reader pending, no run).** The initial G186 statement concerned only Thue–Morse. RULE30-PRIZE.md section8.59 also records paperfolding repeats with i=s, i'=3*s and ell=2*s-1 at dyadic scales s. Apply A⁗ to the same adjacent pair (-1,0) at distance L-1, with a=2*s, a'=6*s and n=2*ell=4*s-2. Its endpoint and one-cell contradiction requirements become

    M < 4*s,
    tau(M)+P <= 6*s,
    M >= L+2*s+2*P+2.

Indeed these give 4*s-2 <= L-1+6*s-M+2*P <= 4*s-3, impossible. The lost repeat symbol contributes the additional2 in the lower endpoint requirement; the later start contributes the stricter upper endpoint4*s, not6*s.

Under G186's SAME history-specific settling bound and liminf p(M)/M=0, choose theta with 2<theta<min(4,6/gamma). This interval is nonempty for 1<=gamma<3. The already proved endpoint selection gives M=ceil(theta*s), P/s->0 and arbitrarily large dyadic s. The strict positive margins 4-theta, 6-gamma*theta and theta-2 absorb all fixed offsets and the extra2. Thus the conditional sparse-depth criterion excludes the recorded paperfolding code as well as Thue–Morse. No new repeat theorem is proved here: the application uses exactly the recorded section8.59 repeats and A⁗, with the original timing/settled-band assumptions.

**Independent offset control and identified unexpected check.** Put L=1, s=8, P=1 and M=21, and assume tau(21)+1<=48. The upper endpoint is21<32, the lower threshold is1+16+2+2=21, and the A⁗ right side is1-1+48-21+2=29 whereas n=30, the desired one-cell contradiction. Reusing the Thue–Morse lower threshold would allow M=19, giving right side31 and NO contradiction. This literal arithmetic control retains the two-cell correction instead of treating the two repeat families as identical. No actual settling-time measurement is claimed by this assumed-timing control. The unresolved stage budget and actual unbounded stage-entry ratios remain necessary proof obligations for this route; no prize claim. Local: review the additional start-time and length offsets, no new job.

*Second reader's note on G186 (Local, 2026-10-07; chat L151).* Correct. The three requirements are exactly G2.4's
($M_k < 6 \cdot 2^k$, $\tau(M_k) + P_k \le 6 \cdot 2^k$, $M_k \ge L + 2^{k+1} + 2P_k$), and the third is also the upper
half of the A⁗ sandwich. Choosing $k$ maximal with $\lceil \theta 2^k \rceil \le n$ keeps the good depth below $2M + 1$,
since $n < 2\theta 2^k + 1$ and $M \ge \theta 2^k$. Monotone periods, from predecessor divisibility, then carry the
small period down to the endpoint, so $P/2^k \to 0$. The two margins are $6 - \gamma\theta$ for time and $\theta - 2$
for space, and both are fixed fractions of $2^k$ that absorb $A P + B$, $L$ and the ceiling. The equivalence follows
from $p/M = 1/R_j$ at entries and from $R_{j+1} > n/(2p(n))$ inside stage $j$. Checked (`rule30_audit_g99_g100.py`, S76)
at $\gamma = 5/2$, $\theta = 11/5$ on 300 random good depths. In the 134 cases where $P/2^k$ is small against $A$, $B$
and $L$, all three requirements and the sandwich hold with the settling bound taken at its worst. A slope with
$\gamma\theta = 6$ fails the time requirement, as it should. On the spike schedule the recurrence holds exactly, and
$R_{2^k + 1} \ge 2^{2^{k-1}}/2$ and $R_{2^{k+1}} \le 1 + k 2^{-2^{k-1}}$ for $k = 1$ to 4 ($R_{17} > 128$,
$R_{32} - 1 < 1/100$). So the weakened condition is strictly weaker, as stated. Beyond G186, the weakened condition has
an exact restatement: $\limsup R_j = \infty$ if and only if the normalized stage lengths $\lambda_j$ are unbounded,
since $\lambda_j/2 \le R_{j+1} \le \max(R_j, \lambda_j)$ (also checked in S76). The paperfolding continuation is also
correct. With §8.59's recorded repeat ($i = s$, $i' = 3s$, $\ell = 2s - 1$), A⁗ at $(-1, 0)$ has $a = 2s$, $a' = 6s$ and
$n = 4s - 2$. So $M < a' - a = 4s$, and the contradiction needs $M \ge L + 2s + 2P + 2$, the same offsets as BF4's
general form $L + 2i' - 2\ell$. S77 checks both thresholds exactly for $s = 2^3$ to $2^{20}$: one below the threshold
there is no contradiction, and $M = 4s$ breaks the first requirement. It also reproduces GPT's offset control (29
against 30 at $M = 21$, and 31 at the Thue–Morse threshold) and checks that $\theta = 11/5$ serves both families at
$\gamma = 5/2$. The quantifier stays per history, as in GC233. Rule 30's finite record cannot bear on a limsup.

### G.GPT187. a positive period/depth threshold suffices for both repeat reductions (second-read by Local, 2026-10-07)

### GPT G187 — A positive period/depth threshold suffices for both repeat reductions (2026-10-07)

**Conditional quantitative lemma, second-read by Local L152; no GPT run.** Fix a left-edge distance L and one admissible rooted history with nondecreasing common prefix period p(M). Suppose its entire-prefix settling bound is

    tau(M) <= gamma*M+A*p(M)+B,
    1 <= gamma < 3, A >= 0,

with finite constants A,B on that history. Define

    delta = (3-gamma)/(2*gamma+2*A+8).

Then liminf p(M)/M < delta suffices for G2.4's unbounded Thue–Morse repeat contradiction. For the recorded paperfolding repeats, the sufficient condition is liminf p(M)/M < min(delta,1/6). In G165's application A=2*(C+1)>=2, so delta<=1/7<1/6 and the SAME delta suffices for both codes. This complements G186: for a specified budget it weakens the sufficient growth condition. G186 remains useful when only existence of a finite budget constant is known. Neither lemma proves an actual budget or period estimate.

**Endpoint construction and proof.** Choose a number r strictly between the liminf and the relevant threshold. Along arbitrarily large integer depths n, let q=p(n)<=r*n. Put D=L for Thue–Morse and D=L+2 for paperfolding, and choose the largest dyadic s for which 2*s<=n-2*q-D. Such a scale exists eventually. Then

    s > (n-2*q-D)/4,
    M = 2*s+2*q+D <= n,
    P = p(M) <= q.

Thus s tends to infinity, and limsup along these chosen depths of q/s is at most 4*r/(1-2*r). Direct rearrangement shows

    r < delta  iff  4*r/(1-2*r) < (6-2*gamma)/(2*gamma+A+1).

Consequently

    tau(M)+P <= 2*gamma*s+(2*gamma+A+1)*q+gamma*D+B < 6*s

eventually, by a strict linear margin in s. For Thue–Morse, r<delta<=1/5<1/4 implies q/s<2 eventually, hence M<6*s. For paperfolding, r<1/6 implies q/s<1 eventually, hence M<4*s. All fixed D and B are absorbed by those strict margins.

For Thue–Morse, the G2.4 A⁗ right side is at most L-1+6*s-M+2*q=4*s-1, below its repeat-run length4*s. For paperfolding the same expression is4*s-3, below repeat-run length4*s-2. Both contradictions use exactly the repeats and timing hypotheses already recorded in G2.4 and G186's section8.59 continuation. To exclude either code for every admissible left side, this quantitative condition and the settling budget must hold separately on every such history, with history-dependent constants allowed.

**Exact dyadic stage interpretation.** In G165's rooted stage structure the last depth m_j=N_(j+1)-1 minimizes p(M)/M within stage j. Its value is

    p(m_j)/m_j = 1/(2*R_(j+1)-2^(-j)).

Every stage is finite and its index tends to infinity with depth. Thus taking the liminf of these stage minima gives the exact extended-real identity

    liminf_M p(M)/M = 1/(2*limsup_j R_j),

with 1/infinity=0 and 1/0=infinity. The vanishing subtraction2^(-j) does not affect the denominator's limsup; inversion exchanges positive limsup and liminf, including these limiting cases. Hence the displayed quantitative condition is equivalent to limsup R_j>1/(2*delta). The factor2 comes from using the END of a stage, just before the next doubling, rather than its entry. For G165 at gamma=5/2 and C=1, A=4 and delta=1/42. Entry ratios above21 by a fixed margin at arbitrarily large indices therefore suffice for BOTH repeat applications, conditional on that stage budget. No such actual asymptotic statement is established.

**Independent integer control.** Hypothetically take L=1, B=0, gamma=5/2, A=4, n=1000 and q=16. For paperfolding D=3; the selected s is256 and M=547. The assumed bound gives tau(M)+P<=1447.5<1536=6*s, and M<1024=4*s. The A⁗ right side is at most1021 against repeat-run length1022. The same endpoint also works for Thue–Morse, whose run length is1024. This verifies the arithmetic under the stated assumptions; it is NOT a settling measurement or a certified C=1 budget on a Rule30 history.

**Identified unexpected strictness/control check.** If q/s equals (6-2*gamma)/(2*gamma+A+1), the scale-dependent time margin vanishes. A positive gamma*D+B then prevents the required timing inequality: this argument cannot replace its strict threshold by a non-strict one. Moreover the synthetic schedule N_j=25*2^j has constant R_j=25 and integer stage lengths25*2^j; it satisfies the gamma=5/2,C=1 entry threshold while p(N_j)/N_j=1/25 never tends to0. Its stage-end ratios tend to1/50. At period16, the entry depth400 has ratio1/25 above1/42, but the last stage depth799 has ratio16/799 below1/42. Thus G186's unbounded-ratio condition is sufficient but not necessary for the conditional application. This schedule has no asserted Rule30 compatibility.

**Prior record and next intention.** This is a quantitative endpoint selection using reviewed G165 timing, G184 stage notation and the pending G186 repeat applications; no novelty or computation claim. A finite large entry such as the conservative N_5 lower bound does not establish arbitrarily many useful scales. The actual target can now be a history-specific positive period/depth threshold tied to its stage-debt constant, rather than unbounded R alone. Both linked obligations remain open. Local: please second-read the threshold algebra and scope, together with G186; no run requested. GPT next examines what actual odd-zero hitting constraints could maintain or recurrently recover such a threshold.


**G187 continuation: align the repeat scale with the dyadic period (GPT, 2026-10-07; second reader pending, no run).** The general sparse-depth threshold is sufficient but can lose room by treating periods as arbitrary integers. In G165's actual stage structure, let q=2^j and choose a FIXED power of two K with

    K > (2*gamma+A+1)/(6-2*gamma).

For the paperfolding application also require K>1. With G165's A=2*(C+1)>=2 and gamma>=1, the displayed fraction is at least5/4, so its smallest admissible dyadic K automatically meets this additional requirement. Then

    limsup_j R_j > K+1

suffices for both repeat contradictions, conditional on that same history's settling budget. At infinitely many stages the next entry obeys N_(j+1)>2*(K+1)*q+D, where D=L for Thue–Morse or L+2 for paperfolding, because the limsup inequality has a fixed positive margin and q tends to infinity. Set s=K*q (a valid dyadic repeat scale) and M=2*(K+1)*q+D. Since M<N_(j+1), its common prefix period P is at most q, whether M falls in the q-stage or an earlier stage. The settling bound gives

    tau(M)+P <= [2*gamma*(K+1)+A+1]*q+gamma*D+B < 6*K*q = 6*s

eventually. The strict coefficient gap is (6-2*gamma)*K-(2*gamma+A+1)>0. Also M<4*s eventually when K>1, hence the paperfolding upper endpoint holds; this also implies the Thue–Morse upper endpoint M<6*s. Both lower endpoints and the one-cell contradictions follow from the same M=2*s+2*q+D construction in G187. This proves the claim without assuming liminf period/depth zero, or measuring any new stage length.

**Independent coefficient control and identified unexpected comparison.** For the hypothetical gamma=5/2,C=1 budget, A=4 and the coefficient fraction is10. Choose K=16; the sufficient entry threshold is now17 rather than G187's general21. At q=16,L=1,B=0 the paperfolding endpoint is again M=547,s=256, and the timing margin is6*q-7.5=88.5, agreeing with the earlier literal control. A synthetic constant schedule N_j=18*2^j has R_j=18 and stage-end period/depth ratios tending to1/36. It passes this new threshold but fails the earlier sufficient condition liminf period/depth<1/42. Thus the improvement is strict as a reduction; no Rule30 compatibility or actual C=1 budget is asserted. Choosing K=8 instead would give a negative coefficient gap8-10=-2, so the next smaller dyadic scale is not licensed by this bound. If the fraction itself is a power of two, equality still leaves no positive margin for offsets: choose the next power. No optimality claim is made for other endpoint strategies or stronger timing information.

**Handoff.** This is a refinement of the same pending G187 proof, not a new growth estimate or a reopened gap-1 family. Local: include the dyadic scale choice and the earlier-stage prefix-period guard in the second read; no job requested. The remaining actual obligation is a recurrent entry-ratio margin linked to the history's uniform stage-debt constant. Finite large entries alone still supply no such recurrence.

*Second reader's note on G187 (Local, 2026-10-07; chat L152).* Correct. With $M = 2s + 2q + D$ the third G2.4
requirement holds with $q$ in place of $P$, and $P \le q$ by monotone periods. The time requirement then reduces to
$(2\gamma + A + 1) q < (6 - 2\gamma) s$, up to the fixed $\gamma D + B$. Taking $s$ maximal and dyadic gives $q/s$ at
most $4r/(1 - 2r)$ in the limit. Cross-multiplying, $4r/(1 - 2r) < (6 - 2\gamma)/(2\gamma + A + 1)$ is
$r(4\gamma + 4A + 16) < 6 - 2\gamma$, which is $r < \delta$. The two codes differ only in $D$, and in paperfolding's cap
$M < 4s$, which $r < 1/6$ secures; $\delta \le 1/7$ once $A \ge 2$. Within a stage $p/M$ falls until the last depth,
where it equals $1/(2R_{j+1} - 2^{-j})$, so the liminf is $1/(2 \limsup R_j)$. Checked (`rule30_audit_g99_g100.py`,
S78). The equivalence holds on a rational grid. On 400 random depths the construction reaches both contradictions
whenever $r < \delta$ (800 of 800), and at $r = 3\delta$ its time margin fails (200 of 200). S78 also covers GPT's
integer control, the strictness case, the stage-end identity on random schedules and the $25 \cdot 2^j$ schedule.
Against the record, at $\gamma = 5/2$ and $C = 1$ ($\delta = 1/42$, so entries above 21): RC2's exact finite budget, a
debt of 7 at $q = 8$ (S72), lies within $Cq$ with $C = 1$ through period 8. The recorded entry $R_4 = 25$ and the bound
$R_5 \ge 1{,}662$ both exceed 21, and the stage ends $8/399$ and at most $16/53{,}207$ lie below $1/42$. That is finite
evidence about two scales and proves nothing about arbitrarily large ones, as G187 says. The dyadic refinement is also
correct. With $K$ the least power of two above $(2\gamma + A + 1)/(6 - 2\gamma)$, the endpoint $s = Kq$,
$M = 2s + 2q + D$ lies before the next entry, so $P \le q$, and the coefficient gap $(6 - 2\gamma)K - (2\gamma + A + 1)$
is positive while at $K/2$ it is not. Since the fraction is at least 5/4 once $A \ge 2$, $K \ge 2$ gives paperfolding's
$M < 4s$ (S79, with GPT's control: fraction 10, $K = 16$, threshold 17, margin 88.5). At $C = 1$ the record's $R_4 = 25$
clears this threshold too.

### G.GPT188. a doubled stage of period at least four cannot return to zero within eleven steps (second-read by Local, 2026-10-07)

### GPT G188 — A doubled stage of period at least four cannot return to zero within eight steps (2026-10-07)

**Local zero-return lemma, second reader pending; symbolic, no run.** Consider an odd zero-driver integration that doubles period from q/2 to q>=4. Write its following compatible temporal profiles as

    0, c, 1, e, f, g, h, i, ...,

with S w(t)=w(t+1), Delta=I+S over binary XOR, and T=S^(q/2). Integration gives T c=1+c. Then none of profiles at positions1 through8 after the displayed initial zero can be identically zero. Thus the first subsequent zero is at position at least9. On a rooted history, every stage entered by doubling to q>=4 has length at least9. This is a CONSTANT bound; it gives no positive lower bound on normalized stage length as q grows.

**The first six positions.** The reset equations force the next profile to1 and S e=1+c, equivalently e=1+S^(-1)c. G159's direct six-position calculation applies because the pre-integration source Delta c has least period q/2>=2 and is nonconstant. Its only earlier-zero exception would require that source to be constant1. Therefore c,1,e,f,g,h are nonzero. This uses the already reviewed local proof, not its even-branch hypothesis: nonconstancy excludes the same exception here.

**Position7 cannot be zero.** If i=0, compatibility forces g=h. The equations for g and h then give S g=f+g and e=f*g (pointwise product). Since e is contained in f, the f equation reduces to S f=1+f. Thus f alternates, g integrates that alternating word, and g is a rotation of0011 repeated. The word e=f*g has exactly one black cell per four positions. Therefore c=1+S e has least period4 and three black cells per four positions. But an entry word c of least period q with complementary q/2 halves has exactly q/2 black cells. Here q must be4 and the required weight is2, contradicting3.

**Position8 cannot be zero.** Suppose the profile after i is0; then h=i. The equations for h and i give g=Delta h, and comparison with the h equation gives f=g*h. Since f is contained in g, the g equation gives e=Delta g=Delta^2 h. Put x=h(t), y=h(t+1), z=h(t+2). The f equation reads

    y*(1+z) = 1 + [(x+z) OR x*(1+y)].

Its allowed triples are001,010,011,100,101. No periodic or bi-infinite word satisfying these constraints can contain11: both110 and111 are forbidden. Hence011 is also absent, and h has no adjacent ones and no three consecutive zeros. The shifted word T h has the same two properties.

Now beta=h+T h obeys Delta^2 beta=1, because e+T e=1 follows from c+T c=1. Thus beta(t+2)=1+beta(t): beta is a rotation of0011 repeated. Choose a phase with five successive beta bits11001. At the second position, h and T h differ; absence of adjacent ones forces their common bit at the third position to0. At the fifth position they also differ, forcing their common fourth-position bit to0. Absence of000 now forces BOTH second-position bits to1, a contradiction. This excludes position8.

**Independent literal control and identified unexpected exception.** The seven-step compatible zero return

    a=0110, 0, c=1101, 1=1111, e=0001,
    f=0101, g=0011, h=0011, 0

uses increasing temporal order on cap4. Direct substitution gives Delta c=0110, S e=0010=1+c, S f=1010=1+(e OR f), S g=S h=0110, and the last equal pair produces0. It has an EVEN pre-integration source and no complementary halves in c, so it does not refute the lemma. Rootedness of this control is not asserted. The q=2 exception is essential: the compatible prefix0,01,11,01,01,0 returns to zero in five steps after constant-one integration, as already recorded in G159. The new assertion keeps q>=4. These literal checks independently guard against extending the result to all zero-driver events or to the smallest doubling.

**Prior record and scope.** G157-G159 supply reset, integration and the six-position guard; G185 shows difference order can recover rapidly without ending a stage. The present short-return exclusion uses actual compatibility and complementary temporal halves, rather than an autonomous order or half-difference model. Neither rooted reachability of the control nor attainment at position9 is claimed. The bound9/q tends to0: this result does NOT establish the unbounded normalized lengths of G186/L151, or the budget-linked recurrent thresholds of G187. No literature novelty, computation or prize claim. Local: please second-read the two return equations, especially the five-position beta contradiction; no job requested. Next useful task is whether longer return constraints yield a period-dependent obstruction, rather than extrapolating this constant bound.


**G188 continuation: positions9 and10 are also impossible (GPT, 2026-10-07; second reader pending, hand algebra only).** These two exclusions require only a nonzero initial c, which forces the following profile to1; they do not require complementary halves. Together with the initial G188 argument, a period-doubling entry of least period q>=4 has no subsequent zero in positions1..10, so its first return and its stage length are at least11. This remains a constant bound, not a normalized-stage estimate.

Define, for three consecutive bits x,y,z of a temporal word w,

    E(x,y,z) = x+y+z*(1+x)*(1+y),

where additions are XOR and products are AND. In the order000,001,010,011,100,101,110,111, its values are0,1,1,1,1,1,0,0. This function arises directly by eliminating the four profiles before a repeated pair (w,w): they are E(w), Delta^2 w, w*Delta w, Delta w, followed by w,w. Here E(w)(t)=E(w(t),w(t+1),w(t+2)). Indeed the closest equations first give Delta w, then w*Delta w, then Delta^2 w, and the next gives S(w*Delta w)+(Delta^2 w OR w*Delta w)=E(w).

**Return at position9.** In 0,c,1,e,f,g,h,i,j,0, the repeated pair i=j=w forces h=Delta w, g=w*Delta w, f=Delta^2 w and e=E(w). The remaining equation for f is

    S(Delta^2 w) = 1 + (E(w) OR Delta^2 w).

For x=w(t), y=w(t+1), z=w(t+2), v=w(t+3), this fixes v uniquely. The resulting triple-state transitions are

    000 -> 001 -> 010 -> 101 -> 010,
    011 -> 111 -> 110 -> 101,
    100 -> 000.

These lines include all eight states. The only cycle is010 <->101, so every periodic w satisfying the equation alternates. Then e=1 and c=1+S e=0, contradicting the nonzero entry. Merely finding a cycle of the necessary temporal map is insufficient: the entry condition must still be checked.

**Return at position10.** In 0,c,1,e,f,g,h,i,j,k,0, the repeated pair j=k=w instead forces i=Delta w, h=w*Delta w, g=Delta^2 w and f=E(w). With e=S g+(f OR g), the remaining f equation reduces to

    if E(x,y,z)=1: E(y,z,v)=0;
    if E(x,y,z)=0: E(y,z,v)=1+x+y+z+v.

Its ONLY allowed triple-state edges are

    011 -> 110 or111,  111 -> 110,  110 -> 100,  100 -> 000.

State000 has no outgoing edge; states001,010,101 likewise have none. This graph has no cycle, so no periodic temporal word can satisfy the return equation. In fact it has no infinite path, even without periodicity. This excludes position10.

**Independent substitution controls and identified unexpected fragment check.** At state000 the position9 equation forces v=1 because E=0 and Delta^2 w=0; at state111 it forces v=0 for the same reason, reproducing the two easily confused endpoints of the first table. At state011 the position10 equation admits both v values because E=1 while E(1,1,v)=0; at state000 it admits neither because it would require v=1+v. The finite fragment0111000 obeys four successive position10 constraints (edges011->111->110->100->000), yet cannot continue even one more bit. A short temporal window can therefore mimic the return condition without defining a compatible periodic profile. No finite fragment is counted as a return certificate. These are direct Boolean substitutions independent of the cycle inspection, not a computational job or a new measured census.

**Scope and handoff.** The argument uses the same backward pair equations as G7/G159, with all word products and shifts retained. It supplies two additional local exclusions; no attainment at11, period-dependent return bound, rooted control example or prize claim follows. Local: include these two tables and the nonzero-entry guard in G188's second read, no run requested. The normalized lower bound11/q still tends to0; whether longer constraints force a growing obstruction remains open.


**G188 continuation: return11 has an odd-period cycle, so cannot follow doubling (GPT, 2026-10-07; second reader pending, hand algebra only).** Retain E(x,y,z)=x+y+z*(1+x)*(1+y), and define H(x,y,z)=(x+y) OR (y+z), equal to0 exactly at000 and111. Four profiles before a repeated pair were eliminated in the previous continuation. One further backward step gives

    F(x,y,z,v)=y+v+H(x,y,z).

For a putative return0,c,1,e,f,g,h,i,j,k,l,0, the last equal pair k=l=w therefore forces j=Delta w, i=w*Delta w, h=Delta^2 w, g=E(w), f=F(w), and e=S E(w)+(F(w) OR E(w)). Its remaining f equation simplifies to

    S F(w) = 1 + (F(w) OR Delta E(w)).

For consecutive w bits x,y,z,v,u, it determines the next bit uniquely:

    u = z + H(y,z,v) + 1
        + [F(x,y,z,v) OR (E(x,y,z)+E(y,z,v))].

The resulting four-bit-state successors, in increasing binary order0000 through1111, are

    0001,0011,0100,0111,1000,1011,1100,1111,
    0000,0010,0100,0111,1001,1011,1100,1110.

Every state feeds the SINGLE cycle

    0000 -> 0001 -> 0011 -> 0111 -> 1111 -> 1110
         -> 1100 -> 1001 -> 0010 -> 0100 -> 1000 -> 0000.

Hence a periodic w satisfying the equation has least period11. The reconstructed preceding profiles are all11-periodic. In particular c cannot have the even least period created by odd integration: its period divides11. For a rooted dyadic stage, there is also the direct check that w cannot be both11-periodic with least period11 and q-periodic for a power of two q. No earlier zero occurs through position10 by the preceding exclusions, so reset uniqueness indeed keeps all these profiles within the entry period until this putative return. Thus position11 is excluded. Combined with G188's earlier parts, the first subsequent zero and the stage length after doubling to q>=4 are at least12. This is still a constant bound.

**Independent cycle-word control and identified unexpected ambient return.** Reading the cycle gives the cyclic temporal word w=00001111001. Its four-bit windows reproduce exactly the eleven cycle states above. It has five black cells and, since11 is prime and the word is nonconstant, least period11. At window0000 the formula has E=F=S E=0, so e=0; at window0111 it has E=F=1 and S E=0, so e=1. Therefore c=1+S e is nonconstant and of least period11. Backward reconstruction consequently DOES produce a compatible ambient return at position11 with a nonzero entry; its pre-integration source Delta c has even block parity. This guards against claiming that the return equation has no compatible solutions. What fails is period-doubling ancestry, not compatibility. Neither this odd-period ambient return nor its gate/root reachability is asserted to belong to the rooted tree. The table and these controls are Boolean proof calculations, not a computed census or a requested Local run.

**Next obligation.** This continuation identifies an actual domain countercontrol while extending only a fixed local exclusion. The lower bound12/q still vanishes. No rule for arbitrary return lengths, period-dependent obstruction, recurrence of large normalized stages, or prize conclusion is established. Local: include the successor list, single cycle and odd-period scope check in G188's second read; no new job.

*Second reader's note on G188 (Local, 2026-10-07; chat L153).* Correct, with its continuation. Checked
(`rule30_audit_g99_g100.py`, S80) exhaustively at $q = 4, 8, 16$. After every odd doubling (every odd $q/2$-source, both
integration children, each with $Tc = 1 + c$), no profile at positions 1 to 11 is zero. Positions 9 and 10 need only a
nonzero $c$, as the continuation says. At every cap from 2 to 12, for every nonzero $c$ and every branch, position 2 is
$1$ and positions 9 and 10 are nonzero. GPT's $E$ table, the position-9 transitions (whose only cycle is
$010 \leftrightarrow 101$), the five position-10 edges (no cycle) and position 8's allowed triples were rebuilt by brute
force over bits. Both literal controls substitute correctly. The return-11 continuation is also correct (S81). The
successor rule reproduces GPT's sixteen entries, and every state feeds the one 11-cycle, whose word is $00001111001$.
Backward reconstruction from it gives a compatible return at position 11 at cap 11, nonzero throughout and with an
even-parity source, and the forward walk reproduces it. Among caps 2 to 13, a first zero at position 11 occurs only at
cap 11. The rooted $q = 16$ stage, followed forwards from the $q = 8$ cap exit $(161, 0)$, first returns to zero 52,808
steps later, at depth 53,207, with an even driver. That is G2.3's genuine split, replayed a third way. The constant is
far from sharp. An exploratory enumeration that was not preregistered (`rule30_g188_returns.py`) gives the earliest
first return after any odd doubling as 21 at $q = 4$, 88 at $q = 8$ and 6,343 at $q = 16$. In units of $q$ that is 5.25,
11 and about 396. Sixteen walks at $q = 16$ show no zero within 200,000 steps. These are descriptive numbers for three
periods, not a bound, and they cover the ambient domain, which contains every rooted history.

### G.GPT189. odd zero returns require logarithmic delay in the entry period (second-read by Local, 2026-10-07)

### GPT G189 — Odd zero returns require logarithmic delay in the entry period (2026-10-07)

**Odd-return period bound, second reader pending; symbolic, no run.** Let compatible periodic profiles start with0,c,1, where c is nonzero of least period q. Suppose the first subsequent identically zero profile occurs at an ODD position r=2k+3, counting the initial zero as position0. Then

    q <= 2^k; equivalently r >= 2*log2(q)+3.

This applies to a doubled dyadic stage when its first zero return is odd. It does not assert that first returns are always odd, or that logarithmic delay supplies the normalized growth required by G186/G187.

**Prediction and counterfactual before the hand checks.** The backward profile functions at even indices should be affine with coefficient1 in their newest temporal bit, so a constant-one condition determines that bit. At odd indices this coefficient can vanish. The counterfactual that every return constraint is deterministic should fail at G188's return10 branch. The controls below check these three claims without a census or computational job.

**Backward functions and their temporal support.** At the final zero the preceding two profiles must be equal; call them w,w. Define U0(w)=U1(w)=w and, for n>=0,

    U_(n+2)(w) = S U_n(w) + (U_(n+1)(w) OR U_n(w)).

Here S w(t)=w(t+1), addition is XOR, and OR is pointwise. This is exactly the compatibility equation solved for the preceding profile, not a model that drops its background. By induction, U_(2j) and U_(2j+1) depend only on bits w(t)..w(t+j). Moreover

    U_(2j)(w)(t) = w(t+j) + A_j(w(t),...,w(t+j-1))

for a Boolean function A_j (A0=0). For the induction step, S U_(2j) has the new bit w(t+j+1) with coefficient1; the OR term in U_(2j+2) depends only on bits through t+j and cannot cancel it. The odd function U_(2j+3) has support through t+j+1, because it is S U_(2j+1) plus an OR term on that same support. This proves both support and affine claims.

In a return of length r, the profile at position2 is U_(r-3)(w), and the entry at position1 is U_(r-2)(w). Thus odd r=2k+3 forces U_(2k)(w)=1. For k>=1 this fixes

    w(t+k) = 1 + A_k(w(t),...,w(t+k-1)).

The k consecutive bits are therefore a state of a deterministic shift map with2^k states. Because w is periodic, its state sequence is a directed cycle, of length P<=2^k. Its temporal word repeats with period P. Every reconstructed profile, including c=U_(r-2)(w), also repeats with P, since these functions commute with time shift. Hence the least period q of c divides P and q<=2^k. For k=0, U0(w)=1 gives w=1 and q=1, yielding the same bound directly. No root reachability assumption is needed for this necessary bound.

**Independent literal and formula controls.** The first functions are U2=Delta w, U3=w*Delta w and U4=Delta^2 w, where Delta=I+S. Thus the r=5 equation fixes w(t+1)=1+w(t), and the r=7 equation fixes w(t+2)=1+w(t), matching G188's alternating and0011 cycles. The literal first return0,01,11,01,01,0 has q2,r5 and meets the bound exactly. Direct forward substitution checks its four interior triples: the right-hand sides are11,10,10,00, respectively, equal to the shifted children. Its preceding source is constant1, so this also guards the essential q2 exception in G188. The ambient r7 control there has entry1101 of least period4 and also meets the bound exactly, but is not an odd-source doubling. G188's ambient r11 entry has period11<=16, consistent with the bound and inconsistent with a blanket dyadic claim for ambient histories.

**Identified unexpected check: even returns retain branching.** U3(x,y)=x*(1+y) is independent of y when x=0, so the even-index induction does not extend to all U_n. More directly, G188's actual r10 condition admits BOTH next bits from state011, even though its full graph has no periodic cycle. This prevents replacing the even return condition with a deterministic map on the same states. For a nondeterministic graph, a periodic word can revisit states before its least temporal period: even the full binary shift admits words0^(m-1)1 of arbitrary least period m on a fixed finite state graph. That abstract control is not a compatible Rule30 return. It only shows why counting states alone is insufficient for the even case.

**Existing record, scope and next obligation.** This generalizes the deterministic odd-return maps of G188 using the backward identity already present in G7/G159. Finite deterministic maps and their cycle bounds are standard; no literature novelty is claimed. The result is a parity-restricted necessary logarithmic delay, not a growing normalized delay: log2(q)/q tends to0. Even first returns, ancestry restrictions and recurrence of large normalized stage lengths remain open. Local: please second-read the support induction, r-3 indexing and least-period divisibility; no new job or larger cap requested. The saved return12 calculation remains unpublished rather than supplying another fixed-bound increment.

*Second reader's note on G189 (Local, 2026-10-07; chat L154).* Correct. Solving each compatibility triple for its first
profile gives $U_{n+2} = SU_n + (U_{n+1} \lor U_n)$ from the final pair $(w, w)$, so $U_n$ is the profile at position
$r - 1 - n$. Hence position 2 is $U_{r-3}$ and the entry is $U_{r-2}$, as stated. In the induction, $SU_{2j}$ carries
$w(t + j + 1)$ with coefficient 1 and the OR term stops at $t + j$, so $U_{2j+2}$ is affine in its newest bit. A
periodic word driven by a deterministic $k$-bit map lies on one cycle of length $P \le 2^k$, so $w$, and with it every
shift-commuting profile, has period $P$, and the entry's least period divides $P$. Checked (`rule30_audit_g99_g100.py`,
S82). The backward functions were computed directly on all words of length 9: for $n \le 12$ the support and affine
claims hold, and $U_2 = \Delta w$, $U_3 = w\,\Delta w$, $U_4 = \Delta^2 w$. On actual walks, every nonzero $c$ at caps 2
to 11 whose first zero falls at an odd position $r = 2k + 3$ has least period at most $2^k$. The bound is exact at
$r = 5$ and $r = 7$ and loose from $r = 11$ on. The even case is not merely unproved: at cap 12 an even first return at
$r = 8$ has an entry of least period 12, far above what the odd bound would allow at that length, so an even-return
obstruction must use the doubling structure, as G188's position-8 argument does.

### G.GPT190. even returns as paths between swapped temporal halves (second-read by Local, 2026-10-07)

### GPT G190 — Even returns as paths between swapped temporal halves (2026-10-07)

**Exact ambient reformulation, second reader pending; hand proof, no run.** Fix an even return position r=2m+2>=4 and a dyadic target period q=2^j>=2; put h=q/2. There is a compatible q-periodic prefix0,c,1,...,w,w,0 returning to zero at position r, entered by odd integration from least period h, if and only if the finite paired-window graph below has a path of length h from some vertex v to its swapped vertex sigma(v). The return need not be FIRST, and no root reachability or growth bound follows.

**Prediction and counterfactual.** The affine newest-bit identity of reviewed G189 should fix the XOR of the two appended bits, leaving up to two candidates before filtering. The counterfactual that complementarity alone fixes BOTH bits is false. The exact path construction must also force least period q, not merely a representation on cap q; the nondyadic guard below checks this obligation.

**Graph definition retaining the full background.** Use G189's exact backward functions U0=U1=w and

    U_(n+2)=S U_n+(U_(n+1) OR U_n).

For m-bit windows X, let F_m(X) be U_(2m-1), which uses only those m bits. Write

    U_(2m)(w)(t)=w(t+m)+A_m(w(t),...,w(t+m-1)).

Vertices are pairs v=(X,Y) with F_m(X)=F_m(Y)=1. An edge appends bits b,b', drops the oldest bit of each window, and requires both the new vertex condition and

    b+b'=1+A_m(X)+A_m(Y).

All additions are XOR. There are at most4^m vertices and at most two outgoing candidates before the new vertex test. Swapping X,Y and b,b' preserves every condition, so sigma is a graph symmetry. This stores the actual backward functions, including their OR backgrounds; it is not an autonomous difference-order approximation.

**Necessity.** In the stated prefix the final zero forces its preceding profiles equal to w. Backward reconstruction places U_(2m-1)=1 at position2 and U_(2m)=c at position1. Since w is q-periodic and c(t+h)=1+c(t), its paired windows X(t) and Y(t)=X(t+h) obey the edge equation. After h shifts their order is swapped. Thus they supply the required length-h path. In particular an actual FIRST even return after doubling to q satisfies this condition: reset uniqueness keeps its profiles q-periodic until that return.

**Sufficiency and overlap audit.** Given v0->...->v_h=sigma(v0), follow it by its swapped copy. This is a closed walk of length2h=q. Extend it periodically in both time directions. The shift-and-append edges make the first windows consistent with a temporal word w, even if h<m; closed-window consistency handles overlapping indices. The second window at time t is the first window at time t+h, because the second half of the walk is the swapped first half. Define c=U_(2m)(w). The edge equation gives c(t+h)=1+c(t), and the vertex equation gives U_(2m-1)(w)=1.

All reconstructed profiles have period dividing q. Since q is a power of two, every proper divisor of q divides h. Hence c's complementary halves force its least period to be EXACTLY q. Its source a=Delta c is h-periodic, and its h-block parity is

    XOR_(t=0)^(h-1) a(t)=c(0)+c(h)=1.

A smaller period dividing h would repeat an even number of times in the h-block, contradicting that odd parity. Thus a has least period h. This is genuinely odd period-doubling integration, rather than the balanced same-period control of GC244.

Backward reconstruction supplies every interior compatibility triple and the final triple(w,w,0). At the other end, U_(2m+1)=S1+(c OR1)=0, so the initial zero is also correct. If an earlier zero appears, it is part of this compatible q-periodic prefix; the construction makes no first-return claim. Its first return is at most r. Arrival-clock gates and rooted ancestry are not supplied by this ambient statement.

**Independent boundary control and identified unexpected nondyadic check.** At r4, m1, F1=w forces both windows to1. Then A1(X)=X=1, so the complementary edge needs b+b'=1, whereas new vertices force b=b'=1. The graph has no edge, consistently excluding this return. GC244's literal balanced cap8 return8 satisfies the constant-one reconstruction but fails c(1)+c(5)=1; the paired condition rejects precisely what scalar balance admitted. Its eight forward triples were independently verified by Local S83, L155.

The dyadic assumption in the least-period conclusion is essential: c=010101 on cap6 has c(t+3)=1+c(t), yet least period2 and source Delta c=111111 of least period1. This is a word-level countercontrol, not an asserted even-return graph path. An ordinary closed walk alone does not certify primitive period; dyadic complementarity supplies that extra conclusion here.

**Record, prior method and limitations.** G7/G159 supply backward compatibility; G188 supplies short-return languages and the complementary-half guard; G189 supplies exact support and affine functions. The record already uses standard finite-window path graphs for precursor blocks (G127); no novelty is claimed for that representation or for closing a path with its swapped copy. The new application retains the exact doubling domain for even returns. Neither candidate branching nor a state count establishes recurrent branching, a period-dependent delay, uniform normalized growth or a prize result. Local: please audit the overlap closure, initial-zero indexing and dyadic least-period/source-parity steps; no census or larger run requested. Next reasoning concerns the recurrent part of this paired relation, not fixed-position table extensions.

*Second reader's note on G190 (Local, 2026-10-07; chat L156).* Correct. The vertex test is G189's $U_{2m-1} = 1$ read on
each window. The edge equation is $c(t) + c(t + h) = 1$ written through G189's affine form of $U_{2m}$. A path of length
$h$ from $v$ to $\sigma(v)$, followed by its swap, is a closed walk of length $q$, so it is the same thing as a
$q$-periodic word with both properties. The three steps GPT asked about hold. Overlap closure needs only that
consecutive first windows shift by one bit, which the edges enforce whatever the size of $h$ against $m$. The initial
zero is $U_{2m+1} = S1 + (c \lor 1) = 0$. At dyadic $q$ every proper divisor divides $h$, so complementary halves force
least period $q$, and the source's odd $h$-parity forces its least period $h$. Checked (`rule30_audit_g99_g100.py`,
S84). With the graph built from its definition (1, 1, 25, 25, 225 and 1,089 vertices for $m = 1$ to 6), there is no swap
path and no doubling-entered return for $q = 2$ to 16. The positive direction was checked on the two actual even first
returns after odd doublings: $q = 8$ at $r = 88$, and the rooted $q = 16$ at $r = 52{,}808$. Both equal the backward
reconstruction at every position, with $U_{r-3} = 1$, complementary halves, the initial zero, least period $q$ and an
odd source of least period $q/2$. The $q = 8$ return also traces a length-4 swap path in the graph built from the
definition at $m = 43$, the overlap case $h < m$. In both actual cases $m$ is much larger than $h$ (43 against 4, and
26,403 against 8), so the paths are short and the windows long.

### G.GPT191. dyadic swap paths have an eventual dichotomy (second-read by Local, 2026-10-07)

### GPT G191 — Dyadic swap paths have an eventual dichotomy (2026-10-07; second reader pending)

**G190 continuation: dyadic swap paths are eventually all present or all absent (GPT, 2026-10-07; second reader pending).** This is a finite-graph lemma applied to the independently verified G190 construction. No component of an actual return graph was enumerated or classified, and no new computation ran.

Let a finite directed graph have n vertices and an involutive automorphism sigma. Call q=2^j, j>=1, admitted when a path of length q/2 joins some v to sigma(v). Then exactly one of these alternatives holds:

    every sufficiently large dyadic q is admitted;
    every admitted dyadic q satisfies q<=n.

The first alternative holds exactly when a sigma-invariant strongly connected component with a positive cycle has power-of-two cycle gcd g and sigma preserves its cyclic classes. A strongly connected component is a set of vertices mutually reachable by directed paths. Its cycle gcd is the greatest common divisor of its positive closed-walk lengths; its g cyclic classes advance by one class on every edge.

**Prediction and counterfactual before the hand controls.** The involution should restrict its cyclic-class shift to zero or half a cycle. Thus dyadic admissions should become constant, rather than alternate forever with j. The counterfactual that arbitrary closed walks suffice should fail when the swap exchanges disconnected components. The literal graphs below check these distinctions independently of the general argument.

**Component and phase proof.** An admitted path followed by its swapped copy is a closed walk of length q, lying in a sigma-invariant strongly connected component C. Thus g divides q, so g=2^s, and g<=|C|<=n because g divides a simple-cycle length. Choose a root in C and assign each vertex a class by a root-to-vertex path length modulo g. This is well-defined: append a common return path to compare any two such lengths. Edges increase the class by1. Since sigma preserves edges, its class displacement d is constant along edges and hence throughout C. Since sigma^2 is the identity,2d=0 modulo g. Therefore d=0, or d=g/2 when g is even. Every path v->sigma(v) has length congruent to d modulo g.

Conversely, every sufficiently large length in that residue occurs. Closed walks at v have gcd g: to compare with a cycle elsewhere in C, walk there and back, then repeat with one additional traversal of that cycle. Choose finitely many closed lengths with gcd g. After division by g, their nonnegative combinations contain all sufficiently large integers. For completeness, fix one generator a; the others generate every residue modulo a, and each residue has a nonnegative representative since inverses in a finite residue group can be replaced by positive multiples. Add multiples of a beyond the largest representative. Concatenate the corresponding closed walks before any fixed path v->sigma(v). This supplies all sufficiently large lengths in the required residue.

If d=0, all sufficiently large powers2^(j-1) are divisible by g, giving the first alternative. If d=g/2, the congruence

    2^(j-1)=2^(s-1) modulo2^s

forces j=s, so any admitted q equals g<=n. A component with an odd factor in g cannot contain an admitted closed walk of length2^j. If no component has power-of-two g and d=0, all admitted q are therefore at most n. Components without a positive cycle cannot contribute. This proves the dichotomy and its exact component criterion. An admitted q>n is sufficient to force eventual admission, but it is not necessary.

**Independent graph controls and identified unexpected disconnected check.** A directed cycle on four vertices with sigma shifting by two has g4,d2, and admits q4 only. The complete directed bipartite graph with parts{a,a'} and{b,b'}, all edges in both directions between parts, and sigma exchanging the primed/unprimed vertices within each part has g2,d0. The path a->b->a' and alternating padding admit every even half-length at least2, hence every dyadic q>=4. This also guards against claiming q>n is necessary. A directed cycle on six vertices with sigma shifting by three admits no dyadic q, retaining the odd-factor obstruction. Unexpected check: two disjoint self-loop vertices exchanged by sigma have ordinary closed walks of every positive length but NO swap path. Reachability of the swapped endpoint cannot be replaced with return to the original vertex. These are abstract graph controls, not Rule30 profiles or rooted witnesses.

**Rule30 application and remaining gap.** For fixed even r=2m+2, G190 has n<=4^m=2^(r-2). Conditional on its exact reconstruction, that fixed return position either admits ambient doubling entries at every sufficiently large dyadic period, or all its admitted periods are at most n. The construction may have earlier zeros; it guarantees first return AT MOST r, not exactly r. No actual component satisfying the first case has been exhibited.

Let f(q) denote the minimum first-return length over the ambient odd-doubling domain at period q, using infinity for no finite return. G189 bounds periods for every fixed odd first-return length. Consequently f(q) tends to infinity exactly when every fixed even-return graph lacks the component described above. Indeed, bounded first returns at infinitely many q give one fixed even length by pigeonhole; its graph then admits returns at every sufficiently large q and makes f eventually bounded. The converse follows directly from reconstruction. This concerns absolute delay only. It falls far short of f(q)/q tending to infinity, supplies no normalized-stage estimate, and has no rootedness conclusion.

**Prior-art credit and handoff.** Cyclic classes and eventual path-length residues are standard finite-state period theory; see [MIT 6.262 Lecture7, especially slides14 and18](https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/2fdbd4633466ba1429e7cc24bce37514_MIT6_262S11_lec07.pdf). The graph proof above is self-contained; no novelty is claimed for that background or attributed Rule30 result in the source. Local: include the component/class-shift argument, finite-period bound and abstract controls in G190's review, no run requested. The actual paired graphs' recurrent structure remains unclassified.

**G191 continuation: an explicit cutoff for the eventual alternative (GPT, 2026-10-07; second reader pending).** For an n-vertex graph as above, n>=1, if the persistent component exists, every dyadic q>=8n^2 is admitted. Therefore admission at any one dyadic Q>=8n^2 is equivalent to the persistent alternative. This is a conservative sufficient cutoff, not a sharp threshold or an efficient Rule30 computation.

**Prediction and counterfactual before hand controls.** Short paths to cycles should give closed-walk generators of length at most3n; a finite residue graph should turn their gcd into a quadratic sufficient length. The counterfactual that gcd1 gives every positive length immediately will be checked with the integers3 and5. No computational run is proposed.

**Bounded generators.** Work in a contributing component C of size k<=n, with cycle gcd g a power of two and swap displacement zero. Fix v. A shortest positive closed walk at v is a simple cycle of length at most k; include its length. For every simple cycle, choose a vertex x on it, a path v->x and a path x->v, each of length at most k-1. Include their concatenated length if positive and the length after one traversal of that cycle. Every included positive length is at most3k-2. Their gcd is g: they are closed lengths, while subtracting each pair shows that their gcd divides every simple-cycle length. If the concatenation is zero, its partner is the cycle length itself, so that case also works.

Divide these generators by g. They are positive integers with gcd1, all at most B=floor((3k-2)/g), and they include a generator a<=k/g. In the directed graph of residues modulo a, adding any generator is an edge. Gcd1 implies that every residue is reachable from0: the generated finite additive semigroup is a group and equals all residues. A shortest path to any residue has at most a-1 edges. Thus that residue has a nonnegative representative of size at most (a-1)B. Every integer N>=(a-1)B is representable: subtract the representative with its residue, then pad by copies of a. Consequently every multiple of g of length at least g(a-1)B is a closed-walk length at v.

Take a simple path v->sigma(v) of length p<=k-1 (the empty path is allowed if fixed). Since the class displacement is zero, p is a multiple of g. Any multiple h of g with h>=g(a-1)B+p is therefore a swap-path length. The right side is at most3k^2+k-1<=4n^2. If q>=8n^2 is dyadic, h=q/2>=4n^2 is a power of two at least g, hence divisible by g. This proves the sufficient cutoff. Conversely Q>=8n^2>n cannot be admitted in G191's bounded alternative.

**Independent arithmetic control and unexpected empty-path check.** The generators3 and5 have gcd1 but omit7. With a3 and B5, residues0,2,1 have representatives0,5,10, respectively; padding by3 represents every integer at least10, exactly as the sufficient argument promises. It does not promise the smaller missing7. Unexpected check: one isolated vertex fixed by sigma has an empty swap path but no positive cycle, so it admits no q>=2. The component's positive-cycle hypothesis cannot be dropped just because the endpoint is fixed. For the four-cycle with half-turn swap from the base argument, Q128 exceeds8n^2 and is absent; for its four-vertex bipartite control Q128 is present. Those literal constructions check both sides independently.

**Rule30 scope.** The fixed even-return graph at r>=4 has n<=2^(r-2). Thus the single dyadic Q=2^(2r-1) is beyond the sufficient cutoff even using the crude upper bound on n. Its admission is equivalent to that graph admitting every sufficiently large dyadic period. This is a finite characterization for each fixed r, not a claim that Q was tested, that any actual component persists, or that all r can be handled uniformly. G191 remains awaiting independent review. No new rooted or normalized-delay conclusion follows.

**Rule30-specific continuation: persistence requires internal branching (GPT, 2026-10-07; second reader pending).** In G190's paired-window graph, no edge joins two vertices fixed by sigma. A fixed vertex has X=Y. If its successor is also fixed, the appended bits satisfy b=b', but the edge equation gives b+b'=1+A_m(X)+A_m(X)=1, a contradiction over binary XOR. This uses the actual complementary-half equation; it is not a property of arbitrary graphs with an involution.

Consider a sigma-invariant strongly connected component whose every vertex has exactly one outgoing edge within the component. Strong connectivity makes it a single directed cycle, of length k. Every automorphism of that cycle is a rotation. If sigma preserves its cyclic classes, it is the identity rotation, so every vertex is fixed. The preceding no-edge fact excludes this. Hence every persistent component in G191's criterion has a vertex with two distinct outgoing edges INSIDE the component. G190 has at most two candidate outgoing edges in total, so the necessary branch is genuinely recurrent, not merely an exit to another component.

More precisely, an invariant single cycle can only have a nonidentity involution rotating halfway around it: k is even and the class displacement is k/2. A dyadic q is then admitted there only if q=k, by G191's phase congruence. If k has an odd factor, none is admitted. Thus this entire structural class of components cannot sustain unbounded dyadic admissions. This does not assert that all actual components belong to it.

**Prediction and independent controls.** The complementary-half equation should exclude persistent nonbranching components; dropping that equation should restore them. The abstract four-cycle with half-turn swap has one internal successor everywhere and admits q4 only. The bipartite four-vertex example has two internal successors and persists, showing that branching is consistent with persistence, not sufficient to prove persistence in any Rule30 graph. Unexpected counterfactual: an abstract single self-loop vertex with identity sigma admits every dyadic q despite having no branch. It violates G190's no-edge-between-fixed-vertices condition, so the restriction cannot be claimed for arbitrary involutive graphs. No new actual graph enumeration ran.

**Next obstruction and limits.** A proof that every sigma-invariant recurrent component of each actual fixed-return graph is a single cycle would exclude persistence and establish G191's weaker absolute-delay conclusion. That hypothesis is unproved. Branches leaving a component do not refute it; two successors within one component do. Conversely, finding such an internal branch alone would not settle persistence: its cycle gcd and swap displacement must still be checked. Existing temporal entropy bounds for specified histories (G139-G140) do not classify this ambient graph family. No normalized-stage or rooted-growth result follows.

*Second reader's note on G191 (Local, 2026-10-07; chat L157).* Correct. An admitted path and its swapped copy close into
a walk of length $q$ inside one strongly connected component, which is $\sigma$-invariant because it contains both $v$
and $\sigma(v)$. So the period $g$ divides $q$ and is a power of two no larger than the component. Because $\sigma$ maps
edges to edges, its class displacement is constant along edges, and $\sigma^2 = 1$ gives $2d \equiv 0$, so $d$ is 0 or
$g/2$. With $d = g/2$, the congruence $2^{j-1} \equiv 2^{s-1} \pmod{2^s}$ forces $j = s$, and the admitted $q$ is $g$
itself. With $d = 0$, all sufficiently long paths in the residue exist, by the standard semigroup argument given. The
reduction for $f(q)$ is sound. Bounded first returns at infinitely many $q$ pin one length by pigeonhole. G189 rules out
the odd case, and an even length admitted at some $q$ beyond its graph's size forces the eventual alternative. Checked
(`rule30_audit_g99_g100.py`, S85) on 400 random graphs of up to 8 vertices with an involutive automorphism, 266 with the
component and 134 without. G191's component test predicted the alternative every time: with the component, every dyadic
$q$ from $2^8$ to $2^{12}$ was admitted, and without it no admitted $q$ exceeded $n$. All four controls behave as
stated. The cutoff continuation is also correct. Closed-walk generators of length at most $3k - 2$, a shortest cycle of
length $a g \le k$, and residues mod $a$ reached in at most $a - 1$ steps give every multiple of $g$ from
$g(a-1)B + p \le 3k^2$ on, so any dyadic $q \ge 8n^2$ works once $g$ divides it. S86 confirms, on 300 further random
graphs, that admission at the first two dyadic $Q \ge 8n^2$ agrees with the component test. The 3-and-5 control (every
integer from 10, not 7), the isolated fixed vertex, and the 4-cycle and $K_{2,2}$ at $Q = 128$ all check. The Rule 30
continuation is also correct. A $\sigma$-fixed vertex has $X = Y$, so an edge between two fixed vertices would append
equal bits against the edge equation's $b + b' = 1$. A nonbranching invariant component is a single cycle whose
class-preserving automorphism is the identity, so it would need such an edge. S87 confirms that no such edge exists in
G190's actual graphs for $m \le 6$. On 600 random involutive graphs without such edges, all 106 nonbranching invariant
components fail the persistence test, while a fixed self-loop, which breaks the property, persists. Beyond these
structural checks, nothing new is checked for the Rule 30 graphs beyond S84, which found no admission at $q \le 16$ for
$r \le 14$; their eventual class remains unclassified, as G191 says.

### G.GPT192. the return-eight paired graph is acyclic (second-read by Local, 2026-10-07)

### GPT G192 — The return-eight paired graph is acyclic (2026-10-07; second reader pending)

**Statement and scope.** G190's actual graph at r8, m3 has no directed cycle. This extends G188's five-position contradiction from a word and its shifted copy to ANY two words carried by a closed paired walk. It is an analytic check on one of Local's six PR191-C1 graphs, not an all-return theorem or an independent rerun of that computation.

**Prediction and counterfactual before the hand controls.** G188's argument should not need the shift relation between the two words: their separate constraints and complementary reconstructed entries should suffice. The counterfactual that the single-word return language is itself empty is false; the recorded word10100100 remains a control. No computation ran in this block.

**Single-word constraints.** Put U0=U1=w, with G189's recurrence. Direct substitution gives U4=Delta^2 w, where Delta=1+S, and U5=F3. On a triple(x,y,z), F3=1 exactly for001,010,011,100,101. These five cases are a hand truth-table control. A periodic word with F3=1 cannot contain011, since the next triple would start11, and neither110 nor111 is allowed. It therefore has neither adjacent ones nor three consecutive zeros. Also, when U5=1,

    c=U6=S U4+(U5 OR U4)=1+S Delta^2 w.

**Paired contradiction.** Suppose the graph had a directed closed walk. Its overlap edges give two periodic temporal words u,v with F3(u)=F3(v)=1. The edge equation is precisely c_u+c_v=1. With beta=u+v, the displayed identity gives Delta^2 beta=1, after undoing the shift S. Thus beta(t+2)=1+beta(t), and beta is a rotation of0011 repeated. This forces a block11001 at some phase.

Number those five positions0 through4. At position1 the words differ, so one has a1; since both prohibit adjacent ones and agree at position2, both position2 bits must be0. At position4 they differ, and they agree at position3, so both position3 bits must likewise be0. To avoid000 at positions1,2,3 both words would need a1 at position1, contradicting their difference there. This excludes the closed walk. It never used v=S^h u or a dyadic period, so it excludes every directed cycle, including cycles not preserved by the swap.

**Independent control and identified unexpected single-word check.** The accepted-triple table follows directly from U2=x+y, U3=x(1+y), U4=x+z and U5=y(1+z)+((x+z) OR x(1+y)), with XOR additions. Its five accepted inputs give25 paired vertices. Acyclicity therefore bounds every directed path by24 edges. Unexpected check: the cap8 word10100100 has every triple among the accepted ones, so the single-word constraint DOES have a periodic solution. Its ordinary return8, entry10010011 and even same-period source were independently checked in L155/S83. The obstruction needs a second word with the complementary reconstructed entry; it cannot be inferred by erasing the pairing.

**Prior record and next step.** This is a scope extension of G188's verified local contradiction and G190's verified edge identity; no external novelty is claimed. Local L158's preregistered exhaustive construction reports all six graphs r4,6,8,10,12,14 acyclic, with sizes/edges1/0,1/0,25/24,25/8,225/70,1089/612. GPT has read the construction and component code, not rerun the census. G192 supplies a hand proof for r8 only. Please second-read the extension to arbitrary paired words; no further computation requested. The first recurrent graph and the class-preserving-swap question at larger r remain open, with a cycle already known at r88 from the actual q8 return. No normalized growth or rooted exclusion follows.

*Second reader's note on G192 (Local, 2026-10-07; chat L159).* Correct. The single-word facts are G188's: $U_5 = F_3$
accepts exactly 001, 010, 011, 100 and 101, which forbids adjacent ones and three zeros in a row, and
$c = 1 + S\Delta^2 w$ once $U_5 = 1$. The extension needs only that a closed walk carries two periodic words $u, v$
whose entries are complementary. Then $\beta = u + v$ satisfies $\Delta^2\beta = 1$, so $\beta$ is a rotation of 0011
and contains 11001, and the five-position argument applies unchanged. No shift relation between $u$ and $v$ is used, so
every directed cycle is excluded, swap-invariant or not. Checked (`rule30_audit_g99_g100.py`, S88). The triple table was
rebuilt directly. At every cap from 1 to 16 the 362 single words with $U_5 = 1$ all reconstruct $c$ as stated and use
only accepted triples, yet no two of them have complementary entries. The solutions of $\Delta^2\beta = 1$ are the four
rotations of 0011. This agrees with PR191-C1's computation (25 vertices, 24 edges, acyclic at $r = 8$) by an independent
route, since S88 searches word pairs rather than the graph.

### G.GPT193. prune paired windows and retain the swap bit in the quotient (second-read by Local, 2026-10-07)

### GPT G193 — Prune paired windows and retain the swap bit in the quotient (2026-10-07; second reader pending)

**Statement.** For G190 at r=2m+2, m>=1, define V_m(X)=U_(2m-2) on an m-bit window X. Let H_m contain precisely the original vertices (X,Y) satisfying V_m(X)+V_m(Y)=1. Every edge of the original graph ends in H_m. The induced graph on H_m preserves all positive-length swap paths and all positive-length directed closed walks. It has no swap-fixed vertex, so its unordered-pair quotient has an exact binary edge label recording the change of orientation. A dyadic q return is equivalent to a quotient closed walk of length q/2 whose edge labels XOR to1.

**Prediction and counterfactual before hand controls.** The constant-one vertex condition should turn G190's append equation into a condition on the target alone. A quotient should then need an orientation bit to distinguish returning to the same ordered pair from exchanging it. The counterfactual that an unlabeled quotient closed walk alone certifies a swap path will fail on the half-turn four-cycle. No graph computation or larger-return search ran here.

**Target-only identity.** Write X'=(tail(X),b) and Y'=(tail(Y),b'). At the source F_m(X)=F_m(Y)=1. The recurrence therefore gives, at that temporal position,

    U_(2m)(u)=1+V_m(X'),    U_(2m)(v)=1+V_m(Y').

Indeed U_(2m)=S U_(2m-2)+(U_(2m-1) OR U_(2m-2)), and the OR term is1. Comparing with U_(2m)=b+A_m(X) proves that G190's edge equation is equivalent to V_m(X')+V_m(Y')=1. Thus H_m's edges are simply shift-and-append edges retaining its vertex conditions; no additional edge equation is needed. Every excluded vertex has indegree zero. All positive-length directed closed walks stay in H_m. A path of positive length to sigma(v) ends in H_m, and H_m is swap-invariant, so v also lies there; the path remains there throughout. Hence all positive-length swap paths are preserved, not arbitrary paths starting at discarded vertices.

In particular diagonal vertices have no incoming edges at all, stronger than G191's no-edge-between-two-fixed-vertices fact. Do not erase them from the original graph's vertex count without this qualification: they exist as transient vertices there. If N0 and N1 count F_m-admitted windows with V_m equal to0 and1, H_m has2N0N1 ordered vertices. Its quotient has N0N1 unordered vertices, at most(N0+N1)^2/4; either count may be zero.

**Orientation and exact path lifting.** Give each unordered vertex its unique canonical representative with V_m(X)=0 and V_m(Y)=1. Every ordered vertex is that representative or its swap. For each edge orbit choose its lift beginning at the canonical source and label it epsilon=0 when its target is canonical, epsilon=1 when its target is swapped. Swapping the edge supplies the lift from the other orientation. Keep distinct edge orbits even if their source and target coincide in the quotient.

Induction over edges shows that a path starting in orientation s ends in orientation s plus the XOR of all epsilon labels. Consequently a length-h path ends at the swap of its start exactly when its quotient walk closes and that XOR is1. Set h=q/2 and use G190 for the stated return criterion. The entire window pair is retained; this is not a closed evolution on a scalar difference or an assumption of autonomous background dynamics.

**Independent controls and identified unexpected parallel-edge check.** For an abstract directed four-cycle numbered0,1,2,3, swap i with i+2, and take canonical vertices0,1. The quotient has edges0->1 labeled0 and1->0 labeled1. A quotient circuit of length2 has XOR1 and gives q4. The length4 quotient walk has XOR0 and does NOT give q8, despite being a closed walk. This checks why labels cannot be dropped. For G191's four-vertex bipartite example with swap within each part, choose the unprimed vertices canonical. There are two edge orbits in each direction, with the SAME quotient endpoints but labels0 and1. Odd-label closed walks exist at every even length at least2, hence q>=4 is admitted. Unexpected check: merging those parallel edge orbits discards a real choice and can change admission. These are abstract lift controls, not newly found Rule30 components.

An actual hand boundary check at m1 has F1(1)=1 and V1(1)=1, so N0=0 and H1 is empty. At m3, G192's five allowed triples have V3=U4=x+z: 010 and101 have label0; 001,011,100 have label1. Thus the r8 quotient has six vertices. G192's acyclicity implies quotient acyclicity too: a quotient circuit lifts either to a closed walk or to a swap path whose swapped copy closes it. Hence an original r8 path has at most six edges, allowing one initial edge from a discarded vertex, compared with the earlier coarse24-edge bound. This is a hand consequence, not a measured maximum.

**Prior method and limits.** Binary orientation labels are the standard two-sheet graph-cover method (often called voltage labels); see Gross and Tucker's 1977 [Generating all graph coverings by permutation voltage assignments](https://www.sciencedirect.com/science/article/pii/0012365X77901315), whose abstract identifies that construction. Its full text was unavailable in this check; the lifting proof above is self-contained. No novelty is claimed for graph covers. The Rule30 application is the exact target-only pruning and natural V_m orientation. No quotient at a larger actual return was classified. G191's persistence test remains unresolved for general r, and ordinary cycles are allowed, including the known r88 witness. Local: second-read the target identity, preservation of positive swap paths and edge-orbit labels; no computational job requested.

*Second reader's note on G193 (Local, 2026-10-07; chat L160).* Correct. At a source vertex $U_{2m-1} = 1$, so the OR
term in $U_{2m} = SU_{2m-2} + (U_{2m-1} \lor U_{2m-2})$ is 1 and $U_{2m}$ becomes $1 + V_m$ of the next window.
Comparing with $U_{2m} = b + A_m$ turns G190's edge equation into $V_m(X') + V_m(Y') = 1$, a condition on the target
alone. Every edge therefore ends in $H_m$, and vertices outside $H_m$, the diagonal ones among them, have no incoming
edge. Positive closed walks and positive swap paths consist of edge targets, so they stay in $H_m$, which contains no
fixed vertex. The orientation bookkeeping is the usual two-sheet cover argument, and the half-turn 4-cycle shows that
the label cannot be dropped. Checked (`rule30_audit_g99_g100.py`, S89) on G190's actual graphs for $m = 1$ to 6. Every
edge ends in $H_m$ and every discarded vertex has indegree 0. $|H_m| = 2N_0N_1$, with $(N_0, N_1)$ = (0, 1), (0, 1), (2,
3), (2, 3), (5, 10), (16, 17). For every source vertex and appended pair, the edge equation holds exactly when
$V(X') + V(Y') = 1$, and on every edge the source's orientation plus the label gives the target's. The longest $r = 8$
path has 5 edges, within G193's bound of 6. $V_3 = x + z$ on G192's triples, and the labelled quotients of both controls
admit exactly the stated lengths.

### G.GPT194. two binary potentials test the quotient persistent phase (second-read by Local, 2026-10-07)

### GPT G194 — Two binary potentials test the quotient's persistent phase (2026-10-07; second reader pending)

**Continuation of reviewed G193 and G191.** Let C be a strongly connected component of G193's labeled quotient, with a positive directed cycle, k vertices, cycle gcd g, and edge labels epsilon in {0,1}. Preserve parallel edge orbits. Assign cyclic classes i(v) in {0,...,g-1}, so each edge increases i by1 modulo g. Define its wrap bit w(e)=1 exactly when i(source)=g-1 and i(target)=0 (for g=1, every edge wraps).

Test these two systems over GF(2), with one unknown p(v) per vertex:

    A: epsilon(e)=p(source)+p(target), for every edge;
    B: epsilon(e)+w(e)=p(source)+p(target), for every edge.

If A is soluble, this component supplies no positive swap path. If A is insoluble and B is soluble, its lift has period2g and swap displacement g: a dyadic admission can occur only at q=2g, and only if g is a power of two. That possible q need not actually occur. If both are insoluble, the lift has period g and swap displacement zero: this component supplies every sufficiently large dyadic q exactly when g is a power of two. An odd factor in g excludes every dyadic admission in either connected case. This is an exact finite certificate for the phase criterion, not a classification of an actual larger Rule30 graph.

**Prediction and counterfactual before hand controls.** G193's exchange bit should give a disconnected lift exactly when it is a vertex-potential difference. The other obstruction should be a potential after adding the cyclic-class wrap. The counterfactual that adding1 to EVERY edge detects the locked case should fail when g=2. No computational job or new graph census runs in this block.

**Potential and connectivity lemma.** In any strongly connected directed graph, a binary edge function has zero XOR on every positive closed walk exactly when it has the form p(source)+p(target). One direction telescopes. For the other, assign p(v) by the XOR on a root-to-v path. Any two such paths can be followed by the same v-to-root path; the resulting closed walks have XOR zero, proving independence. Comparing a path extended by one edge gives the equation, including parallel edges.

Thus A soluble means every quotient closed walk has even label XOR, excluding G193's swap paths. If A is insoluble, an odd closed walk exists. There is an odd closed walk based at every vertex: travel to the known odd walk and back; either the connector walk is already odd, or inserting that odd walk makes it odd. A path between any two base vertices then lifts to either desired sheet, using an odd loop to change the initial sheet when needed. Consequently the two-sheet lift of C is strongly connected and invariant under swap.

**Period and wrap lemma.** Let G be the lift's cycle gcd. Every lifted closed walk projects to a base closed walk, so g divides G. Every base closed walk of length L lifts either to a closed walk of length L or, after repetition, one of length2L. Hence G divides2g. Therefore G is g or2g.

If G=2g, let K(v,s) be the lift's cyclic class, with sheet s=0 or1. Reduction modulo g equals i(v), after aligning the roots. The swap's class displacement is either0 or g. It cannot be0: in that case K(v,0)=K(v,1), and every base edge advances this class by1 modulo2g, making every base closed length divisible by2g, contrary to the definition of g. Thus the displacement is g. Write

    K(v,s)=i(v)+g(p(v)+s) modulo2g.

An edge from sheet0 has target sheet epsilon. Substituting in K(target,epsilon)=K(source,0)+1 gives epsilon+w=p(source)+p(target). Hence B is soluble. Conversely, if B is soluble, that displayed expression defines a lift class advancing by1 modulo2g. Every lifted closed length is divisible by2g; since G divides2g, G=2g.

If B is insoluble, G=g. Reduction modulo g now gives the lift's entire cyclic class i(v), independent of its sheet; swap displacement is zero. G191 supplies all sufficiently large lengths in that residue. When G=2g and the displacement is g, an admitted half-length must satisfy h=g modulo2g. For dyadic h this requires g to be a power of two and h=g, giving q=2g. A congruence is only necessary at this small length; it is not a claimed path. An odd factor in g prevents the swapped path plus its swapped copy from having dyadic length. These observations prove the three cases.

**Independent controls and identified unexpected wrap check.** In the half-turn four-cycle, the quotient is a two-cycle, g=2, with labels0,1. A is insoluble; B is soluble because the labels equal the wrap bits. Its only admission is q4. In G191's bipartite example the quotient has two vertices and parallel labels0 and1 in each direction. Neither system is soluble: two edges with the same endpoints demand contradictory potential differences. The lift persists, as independently checked by its alternating paths.

A separate disconnected control gives both edges of a quotient two-cycle label1. A is soluble with potentials0,1; every closed walk has even XOR, although every individual edge exchanges the sheet. There is no swap path. Unexpected check: in the four-cycle control, replacing the wrap bit by a constant1 changes labels0,1 into1,0, whose circuit XOR is still1; that incorrect test would miss the locked case. For g=1 the distinction disappears, but it must not be generalized to other periods.

**Scope and next question.** This derives an explicit potential form of G191's standard cyclic-class test using G193's standard two-sheet lifting (the graph-cover and finite-state prior methods credited there). No novelty is claimed for those methods. Local has independently verified G193 (S89/L160); G194's two-potential criterion remains awaiting review. No actual larger component has been tested, no first-return or rootedness conclusion is added, and normalized growth remains open. Local: second-read the connectivity, wrap equation and the necessary-only q=2g clause; no run requested. The next structural question is whether Rule30's backward recurrence forces either potential on each recurrent quotient component; no such claim is made here.

*Second reader's note on G194 (Local, 2026-10-07; chat L161).* Correct. The potential lemma is the standard one: a
binary edge function is a coboundary exactly when every closed walk has even XOR. If A fails, an odd loop reachable from
every vertex makes the two-sheet lift strongly connected and swap-invariant. The lift's period $G$ is $g$ or $2g$. For
the wrap equation, write $K(v, s) = i(v) + g(p(v) + s)$. An edge from class $g - 1$ to class 0 loses $g$ in the integer
representative, which is the wrap bit, so $K(t, \varepsilon) = K(s, 0) + 1$ reduces to $\varepsilon + w = p(s) + p(t)$
modulo 2. The $q = 2g$ clause is correctly stated as necessary only. Checked (`rule30_audit_g99_g100.py`, S90) on 500
random strongly connected labelled quotients with up to 6 vertices and parallel edges allowed: 105 with A soluble, 100
with only B soluble and 295 with neither. The two potentials predict the explicit two-sheet lift exactly in every case.
With A there is no swap path at all. With only B, admissions occur at $q = 2g$ alone, and never unless $g$ is a power of
two. With neither, persistence holds exactly at power-of-two $g$, checked to $q = 4096$, beyond G191's cutoff. GPT's
three controls and the constant-1 counter-check behave as stated.

### G.GPT195. a four-window certificate for phase mixing (second-read by Local, 2026-10-07)

### GPT G195 — A four-window certificate for phase mixing (2026-10-07; second reader pending)

**Statement, using independently reviewed G194.** In G193's quotient at m>=1, two distinct edge orbits have the same source and target exactly when there is an (m-1)-bit word T such that

    F_m(0T)=F_m(1T)=F_m(T0)=F_m(T1)=1,
    V_m(0T)+V_m(1T)=1.

Their source is the unordered pair {0T,1T}, their target {T0,T1}, and their exchange labels are0 and1. If this edge lies on a positive closed walk, its strongly connected component makes both G194 potential systems insoluble. If the component's cycle gcd is a power of two, every sufficiently large dyadic period is admitted. A known dyadic return in that SAME quotient component already certifies the gcd condition; no full component census is needed for this implication.

**Prediction and counterfactual before hand controls.** Oppositely labeled parallel edges should arise precisely when dropping the leading bit erases the difference between the two source windows. A single such pair should obstruct both potentials. The counterfactual that the local pattern alone forces persistence will be checked on the independently acyclic return-eight graph. No computational job runs here.

**Exact local characterization.** G189 gives V_m(Z)=last(Z)+A_(m-1)(the preceding bits), with V1(Z)=Z covering the m1 boundary. For a fixed source, each proposed target orientation therefore fixes both appended bits uniquely. There is at most one edge of each exchange label.

Two distinct edge orbits with the same quotient endpoints must consequently have opposite labels. Lift both from the canonical source (X,Y). Their ordered targets must be exchanged copies of one another. Since each target's first m-1 bits equal the corresponding source tail, this requires tail(X)=tail(Y)=T. The source windows are distinct in H_m, so they are0T and1T. The target windows are distinct too, so they areT0 andT1. Source and target admission supplies all four F conditions and the source V condition.

Conversely those conditions put {0T,1T} in the quotient. The two target windows have opposite V values by the affine last-bit identity. Both are F-admitted, so appending0,1 in either order gives valid H_m edges with exchanged ordered targets. These are the two distinct edge orbits and their labels differ.

**Recurrence and the dyadic witness.** Both potential equations in G194 assign the SAME right-hand side to parallel edges. Their left-hand sides differ by1, because their labels differ while their cyclic-class wrap bits agree. Thus neither system can be soluble in a component containing them. If the edge lies on a positive closed walk, both endpoints lie in one cyclic strongly connected component. G194's persistent case then applies exactly when its gcd g is a power of two.

If a known dyadic return q occurs in that component, its quotient closed walk has length h=q/2. Therefore g divides h, already making g a power of two. A return elsewhere does not suffice. Persistence would give ambient first returns at most r for every sufficiently large dyadic q, via G190; it supplies neither exact first return r nor rooted ancestry. Finding this certificate would refute divergence of the minimum AMBIENT return delay, while leaving the rooted and normalized growth questions open.

**Independent boundary control and identified unexpected transient check.** At m1, F1(0)=0, so the four-window certificate fails, agreeing with the empty retained graph. At m3 take T=01. G192's admitted triples include001,101,010,011. Their V3 values are respectively1,0,0,1. From canonical source (101,001), appending(0,1) gives canonical target (010,011), label0; appending(1,0) gives its swap, label1. Thus this parallel pair really occurs in Rule30, rather than only in an abstract control.

Unexpected check: G192 proves this actual graph acyclic. The parallel pair is therefore transient and gives no persistent component. The missing return path is a mathematical requirement, not an optional computational check. G194's abstract bipartite control supplies the contrasting recurrent example, with both labels in each direction and dyadic admissions at all q>=4.

**Record and limits.** G193/G194 already retain parallel choices; this adds their exact Rule30 window criterion and the same-component witness shortcut. No novelty is claimed for generic graph potentials. No larger-r window or recurrent component has been tested, including r88. Local: second-read the necessity of equal tails and the transient guard; no job requested. The next bounded structural question is whether a known return component can reach one of these four-window pairs and return from its target. That question remains open, and absence of this sufficient certificate would not rule out persistence by longer oppositely labeled paths.

**G195 continuation: long overlap excludes the certificate on the observed walk (GPT, 2026-10-07; second reader pending).** On any dyadic swap walk of length h=q/2 in G190, if m-1>=h, none of its source vertices can have equal tails. Hence none can be the source of G195's parallel edge pair. This does not exclude other vertices in the same strongly connected component.

**Prediction and counterfactual before controls.** The difference between the two temporal halves should have period h; a whole h-block of zeros should therefore be impossible. The counterfactual that the known short-period witness itself is a suitable place to search for the local certificate fails in this overlap regime. No computation runs.

Close the walk by its swapped copy, as in reviewed G190, to obtain a q-periodic word w. Put beta(t)=w(t)+w(t+h). Then beta(t+h)=beta(t). If the source windows at some t share a tail, beta is zero at t+1 through t+m-1. When m-1>=h, that interval contains a full h-block; h-periodicity forces beta identically zero. But w would then be h-periodic, and so would c=U_(2m)(w), contradicting c(t+h)=1+c(t). This proves the exclusion.

A further simple-cycle guard applies when m>=q. The word w has least period q: it is q-periodic and its derived c has least period q. If two unordered quotient vertices at times0<=s<t<h coincide, their m-bit first windows either coincide or are exchanged. At least one full q-block then shows that shifting w by t-s or t-s-h preserves w. Neither shift is0 modulo q, contrary to least period q. Thus the h vertices on this particular quotient walk are distinct. The component can still contain additional edges and vertices; a simple observed circuit is not a certificate that the entire component is a simple cycle.

**Actual controls and identified unexpected sharp-length guard.** The reviewed q8/r88 witness has h4,m43; the rooted q16/r52808 witness has h8,m26403. Both therefore exclude the four-window certificate on their observed paths and have simple quotient circuits of length4 and8 respectively. These are hand consequences of their verified parameters, not new graph runs. Unexpected check: an h-periodic nonzero difference can contain h-1 consecutive zeros. For h4, take the word-only control w=00001000; beta=w+S4w=10001000, which has three consecutive zeros. This is not asserted to satisfy the return graph. It checks why the zero-block argument requires h zeros and cannot silently use h-1.

The next recurrence question must therefore concern a detour from a known return component to a four-window pair and back, or a longer pair of equal-length paths with opposite labels. Inspecting only the known periodic circuit cannot answer it. No detour search, PR191-B1 restart or larger-r census is requested.

*Second reader's note on G195 (Local, 2026-10-07; chat L162).* Correct. By G189's affine form, $V_m$ of a window is its
last bit plus a function of the earlier bits. A target orientation therefore fixes both appended bits, so each source
has at most one edge per label, and parallel quotient edges must carry opposite labels. Exchanged ordered targets share
their first $m - 1$ bits with the two source tails, so the tails are equal, which forces the windows $0T, 1T$ and
$T0, T1$. The converse follows by appending 0 and 1 in both orders. Equal right-hand sides with unequal labels defeat
both of G194's potentials. Checked (`rule30_audit_g99_g100.py`, S91) on G190's graphs for $m = 1$ to 6, pruned to $H_m$.
Each source has at most one edge per label, every parallel pair carries opposite labels, and the parallel pairs are
exactly the four-window pairs. There is one at $m = 3$ (GPT's $T = 01$, reproduced edge for edge) and one at $m = 6$,
none elsewhere, all in acyclic graphs and so transient, as the guard says. On 300 random strongly connected labelled
graphs with an opposite parallel pair added, neither potential is soluble. The overlap continuation is also correct: on
a closed swap walk, $\beta = w + S^h w$ has period $h$, so equal tails over $m - 1 \ge h$ positions would make $\beta$
vanish and $w$, hence $c$, $h$-periodic, against $c(t + h) = 1 + c(t)$. S92 confirms on both actual even returns
($q = 8$, $m = 43$; rooted $q = 16$, $m = 26{,}403$) that $\beta$ is nonzero, no source on the walk has equal tails, and
the walk's quotient vertices are distinct. GPT's $h - 1$ guard (00001000) has three zeros in a row in $\beta$ but not
four.

### G.GPT196. a diagonal parity test for both temporal extensions (second-read by Local, 2026-10-07)

### GPT G196 — A diagonal parity test for both temporal extensions (2026-10-07; second reader pending)

**Statement and scope.** Use reviewed G189/G193: F_m=U_(2m-1), V_m=U_(2m-2), and H_m is the paired shift graph with F_m(X)=F_m(Y)=1 and V_m(X)+V_m(Y)=1. For an (m-1)-bit word T, define the last-bit Boolean difference

    D_m(T)=F_m(T0)+F_m(T1).

All sums are XOR; multiplication is AND. If suffix_k(T) is the final k bits, then

    D_m(T)=(m mod2)+sum_(k=1..m-1) F_k(suffix_k(T)).

The empty sum gives D1=1. Put B_m(T)=F_m(T0)*(1+D_m(T)). A source (X,Y) of H_m has two outgoing edges exactly when B_m(tail(X))=B_m(tail(Y))=1. Thus any persistent component in G191 must contain a source satisfying these two diagonal parity tests, with both successors internal to the component. This is necessary only: neither the test nor branching supplies recurrence, a dyadic witness, rootedness or normalized growth.

**Prediction and counterfactual for the hand controls.** The affine newest bit in each even U should let us telescope the odd last-bit difference along a backward diagonal. The counterfactual that all two-successor sources have equal tails should fail already at m3. No experiment, graph census or Local job runs here; the independent literal controls below are hand substitutions.

**Difference recurrence.** For m>=2, the U recurrence gives

    F_m(Tb)=F_(m-1)(suffix_(m-2)(T)b)
            +(V_m(Tb) OR F_(m-1)(T)).

The first term's difference as b flips is D_(m-1)(suffix_(m-2)(T)). The second has difference 1+F_(m-1)(T): V_m is affine with coefficient1 in b, and OR with a fixed bit a has difference 1+a. Hence

    D_m(T)=D_(m-1)(suffix_(m-2)(T))+1+F_(m-1)(T).

Start with F1(b)=b, so D1=1. Iterating this identity gives m copies of1 plus precisely the suffix terms in the statement. The formula retains the full backward backgrounds; it is not an autonomous difference evolution.

**Exact branching.** B_m(T)=1 exactly when both F_m(T0) and F_m(T1) equal1. At a source of H_m, G193 reduces edge validity to target F admission and opposite target V labels. V_m(Tb)=b+A_(m-1)(T); choosing the first appended bit determines the second uniquely. There are therefore exactly two candidate appended pairs, related by flipping both bits. Both are admitted exactly when both tails admit both extensions, namely the two B conditions. Their ordered targets differ, including m1. A persistent component has two internal successors somewhere by reviewed G191, so this local test is necessary there. Outgoing edges that leave the component do not count toward that condition.

**Independent literal controls.** At m1, F1=b gives D1=1 and B1=0. At m2, F2(x,b)=x*(1+b), giving D2(x)=x and no tail with B2=1. At m3, use G192's independently verified allowed triples 001,010,011,100,101 and V3(x,y,z)=x+z. Directly comparing the two extensions gives D3(00)=1 and D3(01)=D3(10)=D3(11)=0. The formula agrees: D3(xy)=1+y+x*(1+y). Only tails01 and10 have B3=1; tail11 has zero difference but both extensions are rejected. This last case guards against confusing insensitivity with admission.

**Identified unexpected unequal-tail check.** The actual source (010,001) has F3 values1,1 and V3 values0,1. Its unequal tails10 and01 both admit both extensions. The two ordered targets are (100,010) and (101,011), with V pairs(1,0) and(0,1). Both are admitted and their unordered targets differ. Hence this is genuine branching without G195's equal-tail parallel-edge pattern. Yet G192 proves the entire r8 graph acyclic: neither branch is recurrent. This refutes both the equal-tail shortcut and any inference from this test alone to persistence.

**Existing record and limits.** This is a Boolean-difference expansion of the already proved backward recurrence, not a novelty claim for Boolean differentiation. G195 characterizes parallel quotient edges; this tests general outgoing branching, including distinct quotient targets. The known D0 q8/r88 component stays closed. No other actual larger component has been classified. Local: please second-read the suffix indexing, affine-OR difference and unequal-tail control; no computational job requested. The unresolved obligation is to control these branch sources inside recurrent components, rather than only their local existence.

*Second reader's note on G196 (Local, 2026-10-07; chat L164).* Correct. The recurrence reads
$F_m = U_{2m-1} = SU_{2m-3} + (U_{2m-2} \lor U_{2m-3})$ on the window $Tb$. The shifted term is $F_{m-1}$ on the last
$m - 1$ bits, ending in $b$, and $U_{2m-2} = V_m$ is affine in $b$, so ORing it with the fixed bit $a = F_{m-1}(T)$
changes by $1 + a$ when $b$ flips. Telescoping down to $D_1 = 1$ gives $m$ ones and exactly the suffix terms, with the
indices as stated. At a source, G193's target test makes the two candidate appends differ in both bits, so both are
edges exactly when both tails admit both extensions. Checked (`rule30_audit_g99_g100.py`, S93). The suffix formula and
the one-step recurrence hold for every tail at $m = 1$ to 10, and the three controls hold. In G190's actual graphs for
$m = 1$ to 6, $B_m$ on both tails predicts the two-successor sources exactly. There are 4 such sources at $m = 3$, 2 of
them with unequal tails, including GPT's $(010, 001)$ with its two targets, and 70 at $m = 6$, 68 with unequal tails.
None occur at $m = 1, 2, 4, 5$. All sit in acyclic graphs, so the test is necessary only, as stated.

### G.GPT197. long overlap delays an exit return to the original circuit (second-read by Local, 2026-10-07)

### GPT G197 — Long overlap delays an exit's return to the original circuit (2026-10-07; second reader pending)

**Statement and scope.** Let w have least dyadic period q>=2, let m>=q, and let the paired circuit consist of the m-bit windows of w at phases t and t+h, h=q/2, as in G190/G195. Suppose its first alternative edge flips both appended bits. Let L be a phase-identifying length: the q length-L cyclic blocks of w are distinct. Along ANY subsequent shift-and-append continuation, a return to any vertex of the original ordered or unordered circuit requires at least

    ell >= m-L+1

edges counted from the source before that first flipped edge. A phase-identifying length L<=q-1 always exists for a primitive binary word. Separately, along any continuation from the original paired source, the equal-tail pattern of G195 cannot occur before ell>=m-h. These are necessary latency bounds, not an assertion that a continuation is legal or ever returns.

**Prediction and counterfactual for hand controls.** The untouched prefix should fix the old phase until the first flipped bit has approached the start of the window. The counterfactual that a short continuation can rejoin the rooted q16 circuit will fail through 26395 edges. An unexpected equal-weight check should improve the generic q-bit phase anchor to q-1 bits. No trajectory computation or graph search runs here.

**Return bound.** Set the exit source's first window at phase0. After ell edges, 1<=ell<=m, the first window starts with the untouched block w(ell)..w(m-1), of length m-ell. Immediately after that prefix is the first injected bit w(m)+1, still retained. If ell<=m-L, the first L untouched bits identify phase ell uniquely among all q phases. Equality with any original first window would thus require precisely that phase. But the injected bit disagrees with its expected bit w(m). This is impossible. Matching an unordered pair does not avoid the argument: its first window must equal one of the original windows, and both orientations already occur among the q phases. The same argument applies at any exit phase by rotation. Later appended bits were arbitrary throughout the proof.

**The q-1 anchor.** Distinct rotations of a binary word have equal total weight. If their first q-1 bits agree, their final bits must also agree to preserve that weight. Their full q-blocks therefore agree; least period q makes their phases identical. Hence length q-1 identifies every phase. This is a word fact, not a special property of the return graph.

**Equal-tail bound.** Before ell>=m, the tails of the two current windows still contain the untouched paired differences beta(ell+1)..beta(m-1), a block of length m-ell-1. By G195, beta(t)=w(t)+w(t+h) is nonzero and h-periodic on this dyadic circuit. If m-ell-1>=h, those tails cannot be equal, since a full h-block of zeros would force beta identically zero. Thus equal tails require ell>=m-h. This applies even without a first flipped edge. It does not exclude general unequal-tail branching from G196.

**Actual hand control: the PR196-D1 rooted word.** Local's verified word is w=1000101001100001, q16, m26403. Its cyclic length-eight blocks at phases0..15 are

    10001010 00010100 00101001 01010011
    10100110 01001100 10011000 00110000
    01100001 11000011 10000110 00001100
    00011000 00110001 01100010 11000101.

They are all distinct. Phases7 and13 have the same seven-bit prefix0011000, so the smallest phase-identifying length is exactly8. The return bound is therefore ell>=26403-8+1=26396. The parallel-edge source requires ell>=26403-8=26395. These apply to both D1 exit decisions by rotation; they establish no path of those lengths.

**Independent word-only boundary control and identified unexpected weight guard.** For w=0001, phases0 and1 share the first two bits00, so q-2 bits do not identify phases, whereas q-1 bits do; the weight argument's universal length cannot be lowered. For w=01, m3, the initial pair(010,101), flipped first target(100,011), then targets(001,110) and(010,101) return after exactly3 edges. Here L1, so m-L+1=3 is attained. These arbitrary append paths are NOT asserted to lie in any Rule30 return graph. They check the counting convention, retention of the injected bit and the strict boundary in the bound.

**Record and limits.** This extends G195's original-circuit overlap argument to arbitrary continuations, using standard cyclic-word phase identification and no external novelty claim. It does not classify the rooted strongly connected component. D1's legal exits refute outgoing isolation; the component itself can still be the original sixteen-cycle if no exit returns. A short detour search cannot establish a return here. Local: audit the untouched-prefix indexing, eight-block table and both word-only guards; no continuation job is requested. General recurrence and normalized stage growth remain open.

*Second reader's note on G197 (Local, 2026-10-07; chat L166).* Correct. After $\ell$ edges the first window begins with
the untouched block $w(\ell), \dots, w(m-1)$ and then the flipped bit $w(m) + 1$. If $m - \ell \ge L$, that block fixes
the phase as $\ell$, and the flipped bit contradicts it; both orientations of an unordered pair occur among the $q$
phases, so the pair gives no escape. Equal weight of rotations makes $q - 1$ bits enough. The paired tails keep
$\beta(\ell + 1), \dots, \beta(m - 1)$ untouched, so a full $h$-block of zeros, which G195 forbids, would be needed
before $\ell \ge m - h$. Checked (`rule30_audit_g99_g100.py`, S94). Every primitive word of length up to 12 is
phase-identified by $q - 1$ bits, and 0001 needs exactly 3. By brute force over every continuation, on five small
primitive words with $m = q$ to $q + 3$ and every exit phase, no first window returns before $m - L + 1$ edges. On three
complementary dyadic words, no paired continuation reaches equal tails before $m - h$. GPT's $w = 01$, $m = 3$ path
returns in exactly 3 edges, attaining the bound. The PR196-D1 word's sixteen 8-bit blocks match GPT's table and are
distinct, phases 7 and 13 share 0011000, and so $L = 8$, giving the bounds 26,396 and 26,395.

### G.GPT198. a return with a phase mismatch decides the known component (second-read by Local, 2026-10-07)

### GPT G198 — A return with a phase mismatch decides the known component (2026-10-07; second reader pending)

**Statement, a specialization of reviewed G191.** Let a finite directed graph have the swap automorphism sigma of G190, and a simple directed cycle v_0,...,v_(q-1), with dyadic q>=2 and sigma(v_t)=v_(t+q/2). Let C be its strongly connected component. Then C is persistent in G191's sense if and only if there is a directed excursion from some v_s to some v_u, with no original-cycle vertex in its interior, whose length ell satisfies

    ell+s-u != 0 mod q.

Such an excursion must use an edge outside the original cycle. A return satisfying ell+s-u=0 does not certify persistence. Phases are ORDERED phases modulo q; the unordered quotient phase alone is insufficient.

**Prediction and counterfactual for hand controls.** The original cycle fixes the possible component gcds to divisors of q. A return with a mismatch should force a proper divisor and hence class-preserving swap. The counterfactual that any recurrent branch or any return length not divisible by q suffices will fail on a locked component with a phase-aligned detour. No trajectory search or graph census runs here.

**Component period.** Since v_s and its swap are joined along the original cycle, sigma(C)=C. Let G be C's cycle gcd. The original q-cycle gives G dividing q, hence G is a power of two. Along the original half-cycle, cyclic class advances by q/2, so sigma's cyclic-class displacement is q/2 modulo G. If G=q, that displacement is q/2 and the component is locked. If G is a proper divisor of q, dyadicity implies G divides q/2 and the displacement is zero. By reviewed G191 these are respectively the nonpersistent and persistent cases. Thus C is persistent exactly when G is a proper divisor of q.

**A mismatched return is sufficient.** Close the excursion v_s to v_u by the forward part of the original cycle returning to v_s. Its length L is congruent to ell+s-u modulo q. A nonzero residue means L is not divisible by q. Since G divides both L and q, it is a proper divisor of q; the previous paragraph applies. The closing part may have length zero if u=s. The resulting positive closed walk is enough; it need not be a simple cycle.

**Necessity and first-return reduction.** The gcd of positive closed-walk lengths based at any vertex of a strongly connected finite graph is G. To recall why, every such walk is a concatenation of directed cycles and has length divisible by G. Conversely, paths from the base to a cycle and back give a connector closed walk of length a+b and, after inserting that cycle of length d, one of length a+b+d; their difference recovers d. The gcd of based walks therefore divides every cycle length. A zero-length connector causes no difficulty, since the cycle itself is then a based walk.

If G is proper, some positive closed walk based at v_s has length not divisible by q; otherwise that gcd would be divisible by q. Cut it at every visit to an original-cycle vertex. The segment residues length+startphase-endphase add modulo q to the total walk length, since the phases telescope. At least one segment has nonzero residue. Its interior avoids the original cycle. Ordinary cycle edges have zero residue, so that segment is an excursion departing from the original cycle and returning with a mismatch. This proves the equivalence, without claiming that any such excursion has been found in Rule30.

**Independent locked-detour control.** Start with a directed four-cycle0->1->2->3->0, sigma(t)=t+2. Add vertices a,a' exchanged by sigma and edges0->a->2, 2->a'->0. There is genuine internal branching and a two-edge return to the old circuit, but it is aligned: ell=2, s0, u2. Assign cyclic classes0,1,2,3 to the old vertices and1,3 to a,a'. Every edge advances by1 modulo4, so all closed walks have length divisible by4. The old four-cycle shows G=4 exactly. Swap shift2 keeps the component locked. This is an abstract control, not an actual larger Rule30 component.

**Independent mismatched control.** Instead add chords0->2 and2->0 to the four-cycle, preserving sigma. The first chord rejoins at phase2 after one edge, residue1-2=3 modulo4. Closing through2->3->0 gives a three-cycle, so G divides gcd(4,3)=1 and the component is persistent. Again this is an abstract graph control, not a found Rule30 return.

**Identified unexpected orientation check.** In the unmodified four-cycle, three original edges from phase0 end at ORDERED phase3 and are aligned: 3-3=0. The unordered quotient identifies phases1 and3. Mistaking that endpoint for phase1 gives residue2 and would falsely report persistence. Keep the orientation bit from G193, or retain the full ordered windows, whenever recording a rejoin.

**Actual scope and next obligation.** For D1 the known q16 circuit has only the two unordered exit decisions0 and4, by its completed first-edge census. Any mismatched first-return excursion must start at one of them or their swaps. G197 proves every first rejoin requires at least26396 edges. A hypothetical rejoin from s0 at ell26396 would be aligned at ordered u12, and mismatched at any other u; no such return is asserted. A finite list of aligned returns cannot prove that every return is aligned. This specializes G191's standard gcd/cyclic-class machinery into the exact question a continuation search would have to answer. It establishes neither rooted growth nor persistence of an actual component. Local: second-read the based-walk gcd, first-return reduction and orientation control; no computational job requested.

*Second reader's note on G198 (Local, 2026-10-07; chat L167).* Correct. The swap joins $v_s$ to $\sigma(v_s)$ along the
cycle, so the component is swap-invariant and its period $G$ divides $q$. The class shift is $q/2$ modulo $G$: it is
$G/2$ when $G = q$ (locked) and 0 when $G$ is a proper divisor (persistent, by G191). Closing an excursion along the
cycle gives a walk of length $\ell + s - u$ modulo $q$, so a mismatch forces a proper divisor. Conversely, cutting a
based walk of length not divisible by $q$ at its cycle visits telescopes the residues, so one segment must be a
mismatched excursion, since cycle edges have residue 0. Checked (`rule30_audit_g99_g100.py`, S95) on 600 random graphs
built around a dyadic cycle ($q = 2, 4, 8$) with the half-turn swap and random swap-closed additions: 321 persistent,
279 not. Persistence held exactly when a mismatched excursion existed, found by a search over (vertex, length mod $q$)
avoiding the cycle's interior, and G191's test on the component agreed every time. GPT's locked detour has $G = 4$ and
no mismatched excursion, and the chords give $G = 1$. The ordered-phase trap reads 0 at phase 3 and 2 at phase 1, as
stated, and the D1 arithmetic gives an aligned hypothetical rejoin at phase 12.

### G.GPT199. a dyadic repeated pair need not have rooted ancestry (second-read by Local, 2026-10-07)

### GPT G199 — A dyadic repeated pair need not have rooted ancestry (RULE30-GPT.md; 2026-10-07; second reader pending)

**Question, control and counterfactual.** A possible way to simplify the rooted distance problem was to treat every dyadic repeated pair(w,w) as lying in the backward zero basin. That would erase the ancestry test at a return endpoint. Check it against G189's already verified balanced cap8 return, rather than launch a basin census. The counterfactual is that dyadic period plus equal endpoint profiles suffices for rootedness. It fails; the inference below uses the completed rooted cap8 certificate, not a new run.

Recall B(a,b)=(S b XOR(a OR b),a). For any nonzero pair whose iterates first reach(0,0), its last nonzero predecessor must be(0,1): B(a,b)=0 forces a=0 and S b=b, so b is constant; the nonzero choice is1. Thus finite absorption is equivalent to membership in the rooted tree. This observation does not assert absorption for arbitrary pairs.

Use temporal words w=10100100, c=10010011 and a=10110100 from the verified G189/S83 prefix

    a, 0, c, 1, e, f, g, w, w, 0.

All displayed profiles are cap8 words. Counting the seven backward pair steps in that prefix gives B^6(w,w)=(0,c) and B^7(w,w)=(a,0). Directly Delta c=a. The word a has four black bits and least period8: its halves1011 and0100 differ. Hence(a,0) would be a genuine even-parity zero-driver branch node of least period8 if it were rooted. The complete cap8 rooted certificate, recorded under Local L115 and G161, excludes every such node. It follows that(a,0) and consequently(w,w) never reach zero under B. A finite eventual nonzero cycle follows from the finite cap8 state space, but no cycle length or trajectory was computed here.

**Identified unexpected scope check.** The previous cap2 nonabsorbing example(01,10) had unequal coordinates, so it did not refute this repeated-pair shortcut. This cap8 example has equal coordinates AND primitive dyadic period. It is still not a period-doubling return: its integration source has even parity and full period8, as G189 already records. Therefore it blocks erasing rooted ancestry but does not refute G190's odd-doubling reconstruction or establish a nonrooted witness inside that stronger domain.

**Failure retained and next obligation.** Dyadic repeated endpoints alone cannot recover the missing rooted predecessor history. No new growth estimate or status-board change. Local: check the six/seven-step indexing and the transfer from the existing all-cap8 no-genuine-branch certificate; no basin computation requested. The next rooted distance argument must retain actual ancestry, not silently infer it from the endpoint's period or equality.


**G199 continuation: ancestry is also missing inside the odd-doubling domain (2026-10-07; second reader pending).** The fixed S84/D0 witness has source with four-bit block1000 (odd parity), target period8, word w=00111101, and first return88. Thus it satisfies G190's stronger odd-doubling condition, unlike the balance control above. It still cannot be rooted.

By the complete cap8 certificate and G158, the rooted temporal-rotation quotient has no genuine branch and is a single chain. Its sole period8 entry orbit occurs at depth29; the preceding zero is at28 and its next zero at399, so its first-return distance is371. The complementary integration choices are shifts through4, and all temporal rotations preserve zero-hit positions and therefore this first-return distance. There is no later odd-doubling entry from period4 on a rooted history: periods do not decrease, and the unique cap4 quotient chain ends at that doubling. Consequently every rooted odd-doubling entry to period8 has first return371. The verified first return88 is incompatible with that rooted orbit. Its source(a,0), entry(0,c), and repeated endpoint(w,w) are outside the backward zero basin. If the endpoint were absorbing, its uniquely reconstructed preceding source would be absorbing and hence rooted, giving the contradiction just established.

This uses the completed finite root certificate, the reviewed rotation-quotient classification and D0's exact first-return witness. No unpreregistered minimum or new trajectory run is used. It specifically refutes replacing rooted ancestry by odd source parity plus complementary halves. It does not classify other return-88 components or bound large-period rooted return lengths. Local: include the unique-entry and rotation-invariant first-return argument in the same G199 second reading; no computation requested.

*Second reader's note on G199 (Local, 2026-10-07; chat L169).* Correct. $B(a, b) = 0$ forces $a = 0$ and $Sb = b$, so
the only nonzero pair sent to zero is the root $(0, 1)$, and finite absorption is exactly rootedness. Counting back
along the prefix $a, 0, c, 1, e, f, g, w, w, 0$, six steps from $(w, w)$ reach $(0, c)$ and seven reach $(a, 0)$, with
$a = \Delta c$ of weight 4 and least period 8, an even-parity zero driver that would be a genuine branch. The rooted
cap-8 graph has none: its zero drivers sit at depths 2, 7, 28 and 399 and are the odd doublings. Checked
(`rule30_audit_g99_g100.py`, S96). The two backward steps reach exactly $(0, c)$ and $(a, 0)$. At caps 1 to 8 only
$(0, \text{all ones})$ maps to zero. No rotation of $(a, 0)$ lies in RQ3's rooted cap-8 graph. Iterating $B$ from
$(w, w)$ enters a cycle of length 4,064 after 389 steps without ever reaching zero; G199 left this cycle unmeasured, and
the measurement is descriptive. The cap-2 pair $(01, 10)$ also never reaches zero. One slip of mine, recorded in S96: a
first draft took the zero drivers' parity over all 8 bits. That flagged the rooted doublings from periods 1, 2 and 4,
whose parity is odd over their own least period. Parity over the least-period block is the right notion, and with it the
check passes. The odd-domain continuation is also correct. The rooted cap-8 chain has a single period-8 entry, at depth
29, and rotations preserve zero-hit positions, so every rooted entry to period 8 first returns at 371. The D0 witness
returns at 88 and therefore cannot be rooted, and since $B$ is a function, neither can its endpoint. S97 confirms this
directly. The witness's source has the odd block 1000, it returns at 88, and its endpoint never reaches zero. The rooted
source, block 1011 doubled, returns at 371 with either integration child and in every rotation, and the only rooted
period-8 entries sit at depth 29.



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

### G.GPT201. post-split siblings are disjoint for one profile, not the next (second-read by Local, 2026-10-07)

### GPT G201 — Post-split siblings are disjoint for one profile, not the next (2026-10-07; second reader pending)

**Question and hand prediction; no run.** G200 requires cumulative returns on each selected history. Can the two
children of an even-parity zero supply a joint constraint that persists along their continuations? G162 already
supplies the prefix a,0,c,1,e on one child and a,0,1+c,1,1+e on the other, with e=1+S^-1 c. The immediate next
profiles should have disjoint support, because their reset drivers are complementary. A tempting stronger
counterfactual is that this disjointness continues thereafter. The following exact rooted control refutes it.
This is exploratory hand algebra, not a preregistered computational experiment.

All sums below are XOR, products are AND, and S shifts forward in temporal phase. Write the continuations as

    a,0,c,1,e,f,g,...
    a,0,1+c,1,1+e,f',g',....

Compatibility gives

    S f = 1+(e OR f) = (1+e)(1+f),
    S f' = 1+((1+e) OR f') = e(1+f').

Their product is zero at every phase, hence f*f'=0. Put D=f+f', their support union. If D(t)=0 then both f(t)
and f'(t) are0, and the displayed equations give D(t+1)=(1+e(t))+e(t)=1. Thus D has no cyclic00, and

    weight(f)+weight(f') = weight(D) >= q/2

on their common dyadic period q. At least one sibling therefore has weight at least q/4. This statement does not
select which sibling, give a lower bound for each, or bound a zero-return distance. It uses G162's complementary
profiles and literal compatibility; no new prior-art or novelty claim.

**Independent literal control and identified unexpected failure on the actual root.** Use G162/L118's known
rooted even source and its child, in increasing time order,

    a=0000110001010011, c=0000010000110001, q=16.

The four needed child bits are c(14)=0, c(15)=1, c(0)=0, c(1)=0. Therefore e(15)=1,e(0)=0,e(1)=1,e(2)=1.
The equations above force f(0)=0,f(1)=1,f(2)=0, and f'(1)=0,f'(2)=1. These values also follow directly from
S f=1+(e OR f), without the product/union argument. The next sibling profiles obey

    S g = e+(f OR g),
    S g' = (1+e)+(f' OR g').

Since f(1)=1, the first equation resets g(2)=1+e(1)=0. At phase2 it then gives g(3)=e(2)+(f(2) OR g(2))=1.
Since f'(2)=1, the second equation independently resets g'(3)=(1+e(2))+1=1. Thus g(3)=g'(3)=1: disjointness
fails at the very next profile on two continuations of a certified rooted branch. No ambient-to-root inference,
trajectory run, new branch search or numerical census is used. The earlier saved cap4 ambient control is unnecessary
for this refutation and is not promoted as rooted evidence.

**Failure retained and scope.** The one-profile union bound is exact. Its proposed preservation along all later
profiles is false even on the rooted domain. Consequently it cannot by itself charge every subsequent excursion or
prove G200's cumulative normalized growth. Nor does this control rule out every more detailed coupling or potential.
Local: second-read the reset indexing at phases0 to3 and the transfer from the known rooted c only; no job requested.
Next reasoning must retain the source backgrounds and each history's actual returns, rather than propagate this
one-step support separation as an invariant. The shared growth status remains open.

*Second reader's note on G201 (Local, 2026-10-07; chat L172).* Correct. By De Morgan, $Sf = (1 + e)(1 + f)$ and
$Sf' = e(1 + f')$, so their product contains $e(1 + e) = 0$ and $ff' = 0$. Where both vanish, the equations give
$D(t + 1) = (1 + e(t)) + e(t) = 1$, so the union has no cyclic 00 and weighs at least $q/2$. In the rooted control,
$e(t) = 1 + c(t - 1)$ gives $e = 1, 0, 1, 1$ at phases 15, 0, 1, 2. The resets then give $f = 0, 1, 0$ at phases 0, 1, 2
and $f' = 0, 1$ at phases 1, 2, and the next equations give $g(2) = 0$, $g(3) = 1$ and $g'(3) = 1$, as stated. Checked
(`rule30_audit_g99_g100.py`, S99). After every even-parity zero driver at caps 4 and 8, and 400 sampled at 16 (534 in
all), the actual children give $c, 1 + c$, then 1, then $e, 1 + e$. The next profiles are disjoint, with no cyclic 00 in
their union. GPT's source $a$ is $\Delta c$ for the stated $c$, has weight 6 and least period 16, and is a rotation of
D1's rooted driver. Computed by the actual child map, its continuations share phase 3 at the following profile, so the
disjointness indeed stops after one step.

### G.GPT202. overlap parity telescopes, with an unsigned balance, but does not close the rooted return state (second-read by Local, 2026-10-07)

### GPT G202 — Overlap parity telescopes, but does not close the rooted return state (2026-10-07; second reader pending)

**Question and hand prediction; no new run.** G200 needs the full sum of rooted zero-return excursions.
The saved restart note proposed cyclic overlap parity as a possible charge. Prediction: summing the compatibility
equation gives an exact boundary syndrome, but no unsigned cumulative charge. Counterfactual: the two profile
parities and their overlap parity determine the next profile parity at fixed period. The already-reviewed rooted
period8 prefix refutes that depth-independent closure below. This uses G3's Boolean expansion, G157-G158's
cyclic compatibility, and G185/S75's existing words; no new prior-art or novelty claim.

Fix a common temporal period q and write pi(v) for the parity of its q bits. For q-periodic profiles a,b,c with

    S c = a XOR (b OR c),

shift invariance of parity and b OR c = b XOR c XOR (b AND c) give

    pi(a) = pi(b) XOR pi(b AND c).

The two appearances of pi(c) cancel. In particular this identity does NOT solve for pi(c) from pi(a),pi(b).

On a rooted history write w_n for its profiles and define

    I_n = pi(w_n AND w_(n+1)).

Compatibility of w_(n-1),w_n,w_(n+1) gives I_n=pi(w_(n-1)) XOR pi(w_n). Therefore any interval of valid
common-q triples obeys

    XOR_(n=h..k) I_n = pi(w_(h-1)) XOR pi(w_k).

For one G200 excursion between zero profiles at z_prev and z_next, take h=z_prev+1 and k=z_next-1. The boundary
w_z_prev is zero, and w_(z_next-1) is the returning source a_next. Thus

    XOR_(n=z_prev+1..z_next-1) I_n = pi(a_next).

An internal same-period branch has syndrome0; the odd source ending the period stage has syndrome1. Summing
these disjoint excursion intervals gives total syndrome1 for a complete stage. This asserts an ODD number of
odd-overlap positions before its exit, not a lower bound growing with q, its length, or the number of internal
branches. No independence or nonnegative monotone charge follows.

**Identified unexpected boundary check.** The last included index is z_next-1, whose overlap is with the zero
profile and is itself0. Extending through index z_next would use the integration child beyond the returning
zero. At the odd exit that child has least period2q, so the q-period shift-parity argument would be invalid.
The zero overlap there does not repair that missing periodicity. A same-period even integration does permit
extension, but that is not the stage exit. This checks the cap and indexing without a new trajectory run.

**Literal rooted closure countercontrol.** G185's q4 construction on cap8 has, in increasing temporal order,

    a=01110111, c=00101101, one=11111111, e=01101001, f=01001010.

G185/S75 places the suffix zero,c,one,e,f at rooted depths28 through32, up to a common temporal rotation, which preserves
all the parities used here. They lie in the same period8 stage. The masks with time0 in the low bit are
238,180,255,150,82 respectively. The weights of c,one,e,f are4,8,4,3. Both reached pairs (c,one) at depth30
and (one,e) at depth31 have summary

    (pi(first), pi(second), pi(first AND second)) = (0,0,0).

Their respective next profiles e and f have parities0 and1. Hence no depth-independent next-parity function of
this summary and the common period can be valid even on this single rooted history. The literal equation
S f = one XOR (e OR f) checks the latter output: e OR f=01101011 and S f=10010100. This is hand substitution
in an independently reviewed finite prefix, not a new measurement or an assertion of rootedness for G185's
larger family. Depth-aware summaries, more retained information, and inequalities using the full words are
not refuted by this two-depth control.

**Scope and next intention.** The overlap syndrome is a necessary exact diagnostic and can check a future
cumulative-return argument. Its telescoping value alone supplies no normalized growth. The proposed autonomous
three-parity state at fixed period is closed in the precise depth-independent sense above; no general barrier
to all parity methods is claimed. G200's actual cumulative-return estimate and the stage budget remain open.
Bears on: PERIOD-TWO.md question7, growth gap2. Local: please check the cyclic cancellation, terminal index and
transfer of S75's rooted prefix; no new run or job requested. Next reasoning should retain full source backgrounds
or establish an unsigned history-specific charge rather than treating this binary syndrome as accumulated cost.


**G202 unsigned balance addendum (GPT, 2026-10-07 13:04 BST; hand proof, review pending).**
Question and retained false start: the saved hand note treated the integer expansion as only signed
cancellation and overlooked that the reset intersection is bounded by |c|. The algebra below corrects that
assessment: a nonnegative correction survives. Counterfactual: overlap equals the weight difference alone.
The already-rooted S75 triple (one,e,f) rejects it. No experiment or blind prediction is claimed; this is
the integer Boolean expansion of G202's same equation, with no new prior-art claim.

Write |v| for the number of ones in a common-q block, and define

    E(b,c)=|S c AND NOT(b OR c)|.

All complements here are within the q-bit block. This counts rising bits of c at positions where b=c=0,
since S c = a XOR (b OR c) forces a=1 at every counted position. The identity
|x XOR y|=|x|+|y|-2|x AND y| and shift invariance of |c| give

    |a|-|b| = 2|c|-|b AND c|-2|S c AND (b OR c)|
               = 2E(b,c)-|b AND c|.

Consequently, with E_n=E(w_n,w_(n+1)), ordinary integer summation, rather than XOR, gives

    sum_(n=h..k) |w_n AND w_(n+1)|
        = |w_k|-|w_(h-1)| + 2*sum_(n=h..k) E_n.

For the same G200 excursion boundaries as above, this is exactly

    total overlap = |a_next| + 2*total rising-outside-reset count.

Thus its overlap total is at least the returning source's weight. Over a complete stage the disjoint
excursion intervals give a lower bound by the sum of all returning source weights. Internal genuine
branches contribute positive even weights, at least2, and the final odd source contributes at least1;
therefore the overlap total is at least2*k_j-1. This is a bound on bit incidences, not spatial steps.
Each overlap position can contain up to q ones, so this inequality alone does not establish growing
normalized stage lengths. No bound on k_j or source weights increasing with q is supplied.

**Independent rooted hand control.** In S75's triple (a,b,c)=(one,e,f), the weights are8,4,3 and
|e AND f|=2. The literal words above give S f=10010100 and e OR f=01101011, so E(e,f)=3.
The integer identity reads8-4=2*3-2. Dropping E would instead predict overlap=-4.

**Identified unexpected units check.** Dividing the overlap total by q bounds the number of included
spatial positions from below, but does not divide their actual distance by q again for free. More
explicitly there are ell_j-k_j included positions, since each excursion omits its initial zero profile;
thus q*(ell_j-k_j)>=2*k_j-1. This weak inequality is not a period-growth estimate. At an odd exit
the period2q child remains excluded exactly as in G202's boundary check. Local: please include this
integer identity and the S75 hand control in the requested symbolic review; no run requested.

*Second reader's note on G202 and its unsigned addendum (Local, 2026-10-07; chat L174).* Correct. Shift invariance gives
$\pi(Sc) = \pi(c)$, and $b \vee c = b + c + bc$, so $\pi(c)$ cancels and $\pi(a) = \pi(b) + \pi(bc)$. The excursion
indexing is right: with $h = z_{prev} + 1$ and $k = z_{next} - 1$, the boundary profiles are $w_{z_{prev}} = 0$ and
$w_k = a_{next}$. The terminal exclusion is not a technicality. If an odd exit source had a $q$-periodic child, the
identity at index $z_{next}$ would force $\pi(a_{next}) = \pi(0) + \pi(0) = 0$. At an even branch the extension is
valid. The integer form follows from $|x + y| = |x| + |y| - 2|xy|$ and $|c| = |Sc(b \vee c)| + E(b, c)$, and every
counted rise has $a = 1$. The stage bound $2k_j - 1$ needs every returning source to be nonzero, and that holds on
any rooted history. A zero child of $(x, 0)$ forces $x = 0$, so the state $(0, 0)$ can only follow itself, and the root
$(0, 1)$ is not it. The units inequality $q(\ell_j - k_j) \ge 2k_j - 1$ is right and, as stated, weak. Checked
(`rule30_audit_g99_g100.py`, S100):
- Both identities hold on every $q$-periodic compatible triple for $q \le 8$, exhaustively, and fail on some
  incompatible ones.
- From $q = 3$, each parity class of $(a, b)$ admits both parities of $c$. At $q = 2$ the class $(1, 0)$ forces
  $\pi(c) = 1$.
- On every edge of the rooted graphs at caps 1, 2, 4 and 8 both identities hold, and $(0, 0)$ is never reached.
- Along the root path to each cap exit, the syndromes are $\pi_q$ of the returning sources. They are 1 only at the
  exit, since the doubled earlier exits are even over $q$ bits. The overlap totals equal $|a_{next}| + 2\sum E$.
- The two known first returns show both cases. The $q = 8$ witness ($r = 88$) ends at the odd driver 00111101, an exit
  with no 8-periodic child (syndrome 1). The rooted $q = 16$ return ($r = 52{,}808$) ends at an even driver (syndrome
  0). "Even" there names the return length, as in G190, not the driver's parity.
- GPT's control words, weights and equation are as stated. The pairs sit at depths 28 to 32 on consecutive rooted
  edges. Each stored state carries its own arrival-phase rotation (S75's 7, 7, 0, 1, 2), and the edge delays make
  these one rotation in absolute time. Every summary used is invariant under rotating a pair as a unit, so the
  transfer holds.
- The summaries at depths 30 and 31 are both $(0, 0, 0)$, with next parities 0 and 1.
- In the addendum's control, $|ef| = 2$, $E(e, f) = 3$ and $8 - 4 = 2 \cdot 3 - 2$.


## S. Proofs from the sparks (SPARKS.md; opened 2026-10-07 at the owner's request)

The sparks are small experiments drawn from the break room, on anything except the prize ([SPARKS.md](SPARKS.md)).
When one of them turns on a proof, the proof is written up here so that it can be read and checked on its own, like
every other entry. The owner, 2026-10-07: "Interesting proofs from SPARKS should get their own proof write up in the
repository - possible name as S01 etc". They are numbered SP01, SP02, ... (spark proofs), because S1, S2, ... already
name Local's second-reading checks, which this file cites as "(S72)" and the like. Nothing in this section bears on
the prize. Each entry names its spark, who proved what, and who has second-read it.

### SP01. Orphans and matches in a sock drawer (SPARKS.md SC2; 2026-10-07)

*Where:* SPARKS.md SC2 and GPT's second-reading note there; `tests/probes/sparks/sc2_socks.py` (simulation) and
`tests/probes/sparks/sc2_gpt_audit.py` (exact enumeration). *Bears on:* nothing in the prize; the break-room entry
on socks (Gareth). *Status:* proved by Cloud and second-read by GPT, who counted independently and enumerated
exactly.

**Proposition.** A drawer holds $n \ge 1$ matched pairs of socks.

1. If $k$ of the $2n$ socks are lost, all $k$-subsets equally likely, the expected number of surviving socks whose
   partner was lost (orphans) is $\dfrac{k(2n-k)}{2n-1}$.
2. Two socks drawn at random from the full drawer match with probability $\dfrac{1}{2n-1}$. So if every morning two
   socks are drawn independently from the full, replenished drawer, the first matched pair comes after a geometric
   number of mornings with mean $2n-1$.
3. If all the socks are interchangeable, no sock is without a possible partner while at least two remain.

*Proof.* (1) A given sock survives with probability $(2n-k)/(2n)$. Given that it survives, the lost socks form a
uniform $k$-subset of the other $2n-1$, which contains its partner with probability $k/(2n-1)$. By linearity of
expectation over the $2n$ socks, the mean number of orphans is
$2n \cdot \frac{2n-k}{2n} \cdot \frac{k}{2n-1} = \frac{k(2n-k)}{2n-1}$. (2) Whatever the first sock, the second is
uniform among the other $2n-1$, exactly one of which is its partner. Mornings are independent with success
probability $p = 1/(2n-1)$, so the first match comes on morning $m$ with probability $(1-p)^{m-1}p$, and the mean is
$1/p = 2n-1$. (3) Any two remaining socks make a pair. $\square$

*GPT's independent count (second reading).* Each orphan is the surviving half of exactly one split pair, so the
orphans are counted by the split pairs. A given pair is split with probability
$\binom{2n-2}{k-1} \cdot 2/\binom{2n}{k} = \frac{k(2n-k)}{n(2n-1)}$, and the $n$ pairs give the same mean. GPT noted
that losing $k$ socks and losing $2n-k$ leave the same orphan mean (a pair is split by a set exactly when it is split
by the set's complement), that $k = 0$ and $k = 2n$ leave none, and that $k = 1$ leaves exactly one, with no spread.
GPT's exact enumeration checked every loss count for $n \le 6$ (48 cases, 5,460 subsets) and every two-sock draw in
those drawers (161 draws).

*Scope (GPT's note).* The mean wait in (2) needs independent draws from the full drawer. Without replenishment it
fails: with two matched pairs, a mismatched first draw leaves a mismatched second, so a match before the drawer
empties has probability only $1/3$. In (3), having a possible partner is not being paired: three interchangeable
socks each have a possible partner, yet one is left over in any pairing.

*Measured as well (SC2).* In 200,000 simulated trials for each $n \in \{5, 10, 20\}$ and $k \in \{1, 3, 5, 10\}$, every
orphan mean lay within 2.5 standard errors of (1), and the mean waits were 8.97, 19.02 and 38.61 mornings against 9,
19 and 39.

### SP02. The last diminisher: always proportional, sometimes envy-free (SPARKS.md SC3; 2026-10-07)

*Where:* SPARKS.md SC3 and GPT's second reading there; `tests/probes/sparks/sc3_last_diminisher.py`. *Bears on:*
nothing in the prize; Cloud's break-room entry "I've been the tea towel all morning". *Status:* proved; (1) and (2)
are classical and were reproved by GPT, (3) and (4) are GPT's correction of Cloud's claim, and Cloud has checked
GPT's bound and its example in exact arithmetic.

**Setting.** The pot is the interval $[0, 1]$, and person $i$ of $n$ values a piece by $V_i$, the integral of a
density, with $V_i([0,1]) = 1$. With $r$ people still waiting and $C = [c, 1]$ left, the first of them marks the
point where their value of $[c, x]$ reaches $V_i(C)/r$; each of the others in turn, if they value the marked piece
at more than $V_i(C)/r$, moves the mark back to their own such point; the last to move it takes $[c, x]$ and leaves.
The last person left takes what remains. (The classical rule, due to Banach and Knaster, trims to $1/n$ rather than
to $V_i(C)/r$; the proof of (1) is the same.)

**Proposition.**

1. Everyone receives a piece worth at least $1/n$ by their own measure.
2. With two people, nobody envies the other.
3. The first person served values their piece at exactly $1/n$, and envies someone exactly when the other $n - 1$
   pieces are not all worth $1/n$ to them.
4. Envy is not certain. In SC3's model (20 equal cells, each density constant on every cell, each person's 20 cell
   weights drawn uniformly from the simplex), if every person puts weight more than $1 - 1/n$ on the last cell
   $[19/20, 1]$, nobody envies anybody; and this happens with probability $n^{-19n} > 0$.

*Proof.* (1) Suppose that when $r$ people are waiting, every one of them values what is left at $V_i(C) \ge r/n$;
it holds at the start, with $r = n$. The piece $P$ handed over ends at the smallest mark, so it is worth exactly
$V_h(C)/r \ge 1/n$ to its taker $h$, and at most $V_i(C)/r$ to everyone else. So each person still waiting keeps
$V_i(C \setminus P) \ge V_i(C)\,(r-1)/r \ge (r-1)/n$, and the claim passes down to $r - 1$. The last person keeps at
least $1/n$. (2) Each person's values of the two pieces add up to 1 and their own is at least $1/2$. (3) At the start
$V_h(C) = 1$ and $r = n$, so the first piece is worth $1/n$ to its taker, and the other $n - 1$ pieces share the
remaining $1 - 1/n$ by that person's measure: either all are worth exactly $1/n$ or one is worth more. (4) Every
person values $[0, 19/20]$ at less than $1/n$, so every first mark lies inside the last cell, and so does all that
is left after the first piece. There every density is constant, so every later mark cuts the same length, $|C|/r$,
from the left end: the later $n - 1$ pieces have equal lengths and, for each person, equal values. The first taker
values each at $(1 - 1/n)/(n - 1) = 1/n$, the same as their own. Every other person values the first piece at most
$1/n$ (their mark lay at or beyond it), so values each later piece at least $(1 - 1/n)/(n - 1) = 1/n$; their own
piece is one of these, as good as every other later piece and at least as good as the first. Nobody envies. For
the probability: under the uniform distribution on the 20-cell simplex the last weight exceeds $t$ with probability
$(1 - t)^{19}$, which is $n^{-19}$ at $t = 1 - 1/n$, and the $n$ people are independent. $\square$

*An example (GPT's, checked by Cloud in exact arithmetic).* Three people put $3/4$, $4/5$ and $5/6$ on the last cell
and spread the rest evenly over the other nineteen. Their first marks are $43/45$, $23/24$ and $24/25$, so the first
person takes $[0, 43/45]$, and the rest is halved at $44/45$. The three pieces are worth $(1/3, 1/3, 1/3)$ to the first
person, $(13/45, 16/45, 16/45)$ to the second and $(7/27, 10/27, 10/27)$ to the third: proportional and envy-free.

*What it corrects.* SC3 found envy in every one of 20,000 runs for each $n$ from 3 to 6 and concluded that envy, and
the first taker's envy, have probability one. That conclusion is false by (4). The measurement itself stands: the
envy-free event of (4) has probability $3^{-57}$ at $n = 3$, far too small to turn up in 20,000 runs, and it is only
a lower bound for the true chance of no envy, which was not estimated.

### SP03. When a following column turns into a concertina (SPARKS.md SC9; 2026-10-07)

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



## G. The waiting room: stated with a proof sketch, not yet checked by a second reader

- **Each eventually white diagonal catches outward damage with probability exactly one half** (RULE30-PRIZE.md
  §8.66 addendum): measured exactly at three barriers over the band's phases; no proof. GPT's C071 caution applies.
- **The uniform core begins at the leftward light speed** (§8.68 second addendum): the triangle front is measured at
  $x/t = -0.24 \pm 0.02$, and the band's settled edge at $-0.254$ and $-0.252$ (the `edge` run), so the front is the
  band's inner edge; that this edge moves at exactly the leftward speed of information is §8.30's measurement, not
  a theorem.


