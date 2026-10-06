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


## E2. GPT's proofs G39 to G116, second-read by Local (moved from the waiting room, 2026-10-06)

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

**Status:** exact finite-cone candidate-state counterexample; independently reviewed by Local L072. IS0-IS2 predictions and instrument published through114a83c before execution. This tests Local L070's injection-history repair in the isolated-pulse ensemble, not repeated random races.

Use the same8192 fair initial cone words as G113. Define F=E1, the actual injection indicator, and candidate X5=(F,K4,K5). Every positive injection happens at the fixed pulse time1, so adding its time or age at tick5 adds no further information. Refine each candidate bin by the full observed history H=(K0,...,K5). The instrument uses two independently checked update formulations and exact integer cross products.

The parent A={F=1,K4=(0,0),K5=(0,0)} has80 compatible words and40 next errors, so P(E6=1|A)=1/2. Its full-history child

    H=((0,0),(0,1),(0,0),(0,1),(0,0),(0,0))

has20 compatible words and no next error, so P(E6=1|H)=0. Both bins have positive probability in the infinite fair ensemble because only13 initial bits are needed. Thus the next-error law retains observed-past information not supplied by injection occurrence/time and one lag. The specified state is not sufficient at tick5, even allowing the known pulse phase.

A concrete word in the zero child is0101100010000 on-6..6. G113's independently checked positive cylinder0011110010000 lies in the same candidate parent and produces next error1. The zero conditional rate for the entire full-history child is certified by exhaustive enumeration, not inferred from the single zero word. Independent review remains required; no repeated-race or all-finite-orders conclusion follows.

**IS0-IS2 outcomes (2026-10-06 21:19 BST).** IS0 PASS:all8192 words, F=E3=001 indicator, bin totals and unaugmented0/896 versus40/1872 witness. IS1's blind split prediction HELD:24 unequal full-prefix refinements among18 candidate parents and112 full histories. A second witness has parent(F,K4,K5)=(1,(0,0),(0,1)), next-error24/48, while its zero-success full-history child has0/12. IS2's unexpected shallow-equality prediction HELD:zero unequal refinements when only K3 is added to X5. This is a controlled false reassurance: the K3-only diagnostic holds at this horizon while the complete observed past splits. No held finite diagnostic is promoted to closure. The unaugmented one-lag closure counterfactual remains refuted.

### G.GPT116. the fourth pulse error is gated parity (second-read by Local, 2026-10-06)

### G116. The fourth pulse error is gated parity of three earlier ideal samples (2026-10-06)

**Status:** local algebraic proof; PE0-PE2 pass, independently reviewed by Local L072. Follows G109's echo, G114's Boolean damage equation and G115's shallow/full-history distinction. This is the fixed isolated-pulse model, not a law for repeated races or a physical jerk measurement.

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

## G. The waiting room: stated with a proof sketch, not yet checked by a second reader

- **Each eventually white diagonal catches outward damage with probability exactly one half** (RULE30-PRIZE.md
  §8.66 addendum): measured exactly at three barriers over the band's phases; no proof. GPT's C071 caution applies.
- **The uniform core begins at the leftward light speed** (§8.68 second addendum): the triangle front is measured at
  $x/t = -0.24 \pm 0.02$, and the band's settled edge at $-0.254$ and $-0.252$ (the `edge` run), so the front is the
  band's inner edge; that this edge moves at exactly the leftward speed of information is §8.30's measurement, not
  a theorem.


### G117. A hidden right-tail bit first enters the fifth pulse-error law (2026-10-06)

**Status:** local algebraic kernel and fair-ensemble law proposed; FT0-FT2 pass, independent review pending. Continues G116 in the fixed isolated-pulse model. There are no further races after tick1; conditional uncertainty here comes from initial bits outside the observed source history, not fresh noise.

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
