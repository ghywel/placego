# PROOFS.md: the solid proofs of this record, in one place

*Split of 2026-10-28 (Local, at the owner's request).* This file had reached 1.9 MB, too large to load or read
comfortably, so section E2 (GPT's second-read proofs, G.GPT39 to G343) moved unchanged into four volumes in
[proofs/](proofs/). Section E2 below is now its index, one line and one link per proof. Every other section is
unchanged and still here.

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

## Contents

*Added 2026-10-22 in the spring clean. "Proofs" counts the entries that `proofs/build.py` gives a page of their own, on
that day; [proofs/README.md](proofs/README.md) lists every one with a line in plain words. On the same day G323, G324
and G325 moved from the waiting room to the end of E2, and section M and Cloud's waiting-room entries were given
pages. C.9 and C.10 are four-bin partition lemmas, filed in C when GPT's reads carried them.*

| Section | Proofs |
|---|---|
| [Generality index](#generality-index-locals-audit-2026-10-06-clouds-cl002-split) |  |
| [A. The wall form](#a-the-wall-form) | 4 |
| [B. Windows, zero runs and the left band](#b-windows-zero-runs-and-the-left-band) | 11 |
| [B′. Siblings, Jen, the squeeze and one certified computation](#b-siblings-jen-the-squeeze-and-one-certified-computation) | 28 |
| [C. Short proofs restated from the running text](#c-short-proofs-recorded-without-a-theorem-heading-restated-here-with-their-proofs) | 11 |
| [E. Theorems proved by GPT (statements; proofs in RULE30-GPT.md)](#e-theorems-proved-by-gpt-statements-verbatim-the-proofs-are-in-rule30-gptmd-at-the-section-named) | 7 |
| [F. Collatz](#f-collatz) | 2 |
| [E2. GPT's proofs, second-read](#e2-gpts-proofs-second-read-g39-to-g204-moved-from-the-waiting-room-2026-10-06-by-local-later-entries-promoted-as-their-readings-arrived-each-naming-its-second-reader) | 289 |
| [M. Mahler and ternary digit obstructions](#m-mahler-and-ternary-digit-obstructions-cloud-and-gpt-each-second-read-by-the-other-2026-10-14) | 4 |
| [S. Proofs from the sparks](#s-proofs-from-the-sparks-sparksmd-opened-2026-10-07-at-the-owners-request) | 4 |
| [G. The waiting room: proof sketches not yet checked by a second reader](#g-the-waiting-room-stated-with-a-proof-sketch-not-yet-checked-by-a-second-reader) | 7 |

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

*Machine-checked (Local, 2026-10-09 22:40 BST).* tests/probes/lean/TheoremA.lean (Lean 4, Mathlib).
- `theorem_A` is the statement above for Rule 30 on configurations ℤ → Bool: a leftmost black cell L >= 0 cells left of
  column c, columns c and c + 1 P-periodic on [a, b], P >= 1, give b <= 2a + L + 2P - 1.
- `no_two_periodic` is the corollary: no two adjacent columns are P-periodic for ever.
- Facts 1 .. 3 are separate lemmas (`left`, `left_iter`, `edge`).
- The axioms are propext and Quot.sound only.
- The case of a leftmost black cell to the right of the column (time re-basing, as in entry 40) stays a hand step.

*Correction (comb note, 2026-10-14, Local, SW-01): "question 2" in the Bears-on field above should read questions 5
and 7 of PERIOD-TWO.md §7, as §8.54 itself says; question 2 is Flatto, Lagarias and Pollington's move.*

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

*Machine-checked (Local, 2026-10-10 04:40 BST).* tests/probes/lean/TheoremB.lean (Lean 4, Mathlib), `theorem_B`.
- Columns 0 and 1 are P-periodic for all t >= 0, P >= 2, and column 0 is black at some time. A zero run of row 0 at
  depths d .. d + R - 1 with d >= 1 then has R <= 2P - 2.
- The steps are separate lemmas: fact 1 on an unbounded window (`left_all`, `left_all_iter`), the white triangle
  (`triangle`), the latch (`latch`) and the rightward push (`push_right`).
- The axioms are propext and Quot.sound only.
- *Added 2026-10-10 04:44 BST:* `theorem_B_odd` machine-checks GPT's odd-run refinement (R5, GC307, read by Local in L190).
  - A run of length 2m + 1 >= 3 bounded by black cells needs P >= m + 3.
  - `shrink` is the run shrinking by one cell at each end per step. Its apex has parents 101 and stays white one
    step more, so it is white for m + 2 steps, which covers a period.
  - `push_to_zero` is the shared finish.

*Odd-run refinement (GPT, 2026-10-07; R5 continuation, GC307; independent review pending).* A maximal odd white run wholly in the forced left half, bounded by black cells and of length n=2m+1>=3, in fact requires P>=m+3, hence n<=2P-5. After m shrink steps its white singleton apex has101 parents and survives one extra tick, giving m+2 consecutive white samples. If these cover a period, its column is forever white; the initially white neighbour to its right is periodic and latched, hence forever white too, contradicting the nonzero wall. The restriction n>=3 is essential: stationary alternating spatial stripes have singleton gaps even at period1. The original general bound for even runs is unchanged. Full proof and endpoint controls are in RULE30-GPT's R5 continuation.

*Author's check of the odd-run refinement (Local, 2026-10-07; chat L190).* Correct, and sharp where it can be tested.
A maximal white run with black ends shrinks to exactly its interior, again with black ends: the left end sees parents
100 and the right end 001, and both turn black. So after $m$ steps the apex is a singleton between black cells, and
parents 101 keep it white one more step. The latch is the one in the proof above. With the centre column $-k$ zero, the
column to its right obeys $x_{t+1}(-k+1) = x_t(-k+1) \vee x_t(-k+2)$ and never turns from black to white. It is
periodic, so constant, and white at time 0 because $n \ge 3$. Checked (`rule30_audit_g99_g100.py`, S106): over every
pair of $P$-periodic columns for $P = 2$ to 7, 40 columns deep, every bounded run in row 0 obeys $n \le 2P - 2$, every
odd $n \ge 3$ obeys $n \le 2P - 5$, and its centre stays white for $m + 2$ steps. The longest odd runs seen are 3, 5,
5 and 9 at $P = 4, 5, 6, 7$, so $2P - 5$ is attained at $P = 4, 5$ and 7. The longest even runs, 4 and 6 at $P = 3, 4$,
attain $2P - 2$.

*Sharpness on actual walls (Local, 2026-10-07; `rule30_aw.py`, AW; chat L191).* Restricting to pairs of columns 0 and 1
that have a periodic right continuation, which certainly come from actual configurations, both bounds are still
attained: $2P - 5$ at $P = 5$ (an odd run of 5), and $2P - 2$ at $P = 3$ and $P = 4$. Whether the formal odd witnesses at
$P = 4$ and $P = 7$ admit a non-periodic right side is not settled.
*Settled (Local, 2026-10-07; `rule30_aw2.py`, AW2; chat L194).* By GPT's strip certificates (GC313) every pair that beats those
maxima has a width with no cycle, so it has no right continuation at all. Within the 40-column census the longest
bounded runs on actual walls are exactly odd 1, 1, 5, 5, 5 and even 4, 6, 2, 4, 6 at $P = 3, \dots, 7$. Among $P = 4$ to 7 the
odd bound $2P - 5$ is attained on an actual wall only at $P = 5$.
*At every depth (GPT's GC316 re-anchoring, checked by Local as S111; chat L196).* Re-anchor any deeper offending run at its
black right boundary. Theorem B puts it within 13 columns of the new wall, inside AW2's refuted excess set, so the
maxima above hold at every depth for $P = 3$ to 7, not only within 40 columns.
*P = 8 and 9 (Local, 2026-10-07; `rule30_aw3.py` and `rule30_aw3b.c`, AW3 and AW3b; chat L203).* The same method gives the exact
actual-wall maxima odd 7, even 6 at both $P = 8$ and $P = 9$. At $P = 8$ one excess pair, columns $(83, 157)$ with a run
of 9, kept a cycle at every strip width to 15 and died only at width 16. For $P = 3$ to 9 the table reads odd 1, 1, 5,
5, 5, 7, 7 and even 4, 6, 2, 4, 6, 6, 6, so among $P = 4$ to 9 the bound $2P - 5$ is attained only at $P = 5$.

*Correction (comb note, 2026-10-14, Local, SW-01): "question 2" in the Bears-on field above should read question 5 of
PERIOD-TWO.md §7, a weaker theorem about every single seed (done by Theorems A and B, §8.54, in its status row);
question 2 is Flatto, Lagarias and Pollington's move.*

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

*Machine-checked (Local, 2026-10-10 04:42 BST).* tests/probes/lean/TheoremAprime.lean (Lean 4, Mathlib), `theorem_A'`.
- Take a leftmost black cell L >= 0 cells left of column i, and equal values on columns i and i + 1 at times
  a + s and a' + s for every s < n, with a < a'. Then n <= L + a'.
- `agree` is the right-to-left determination: the cell m left of column i agrees at times a + s and a' + s when
  s + m < n, by strong induction on m.
- `edge` is the moving left edge.
- The axioms are propext and Quot.sound only.

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

*Machine-checked (Local, 2026-10-10 04:45 BST).* tests/probes/lean/LemmaB1.lean (Lean 4, Mathlib). It holds for any
configuration with a leftmost black cell e. Diagonal j at time t is the cell e - t + j.
- `no_adjacent_white` is part (1), for j >= 0.
- `white_then_black` is part (2), for j >= 0.
- `black_needs_white` is part (3).
- The tools are the diagonal recurrence (`D_succ`), the edge's D_0 = 1 (`D0`), and descent through adjacent white
  pairs (`down`).
- The axioms are propext and Quot.sound, plus Classical.choice in part (2).

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

*Machine-checked (Local, 2026-10-10 05:28 BST, L545).* tests/probes/lean/LemmaB2.lean, `lemma_B2`: no P >= 1 is an eventual
period of every diagonal. It covers the first sentence, that the periods are unbounded; the white/black corollary is
not formalised in that file; JenPow2.lean (L548) adds it: `infinitely_many_white` (for every N some diagonal k >= N
is eventually white) and `infinitely_many_black`, by `reset` (a black D_(k-1) makes D_k inherit its inputs' period)
and B1's white_then_black.
- The proof avoids the vectors over Z/P. Take one time after which diagonals 0 .. 4^P + 1 all have period P.
  Pigeonhole the windows (D_k, D_(k+1)) on [T, T + P); `ext_window` extends equal windows by periodicity.
- `D_back` reads the recurrence backwards, down to a negative diagonal against D_0.
- The axioms are propext, Classical.choice and Quot.sound. With JenPow2.lean the periods are powers of 2 without bound.
- Quantitative form (L550): `lemma_B2_quant`, some diagonal k <= 4^P + 1 lacks eventual period P. This is Nersissian's
  m + 2 <= 4^(Q_m) shape (PRIOR-ART.md, L471), for every configuration with a leftmost black cell.
- Second-read from source: Cloud (CL173, the window bookkeeping and Q's induction) and GPT (GC963, including the
  quantitative form).

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

*Machine-checked (Local, 2026-10-10 04:47 BST).* tests/probes/lean/TheoremAprime.lean, beside Theorem A′.
- `theorem_A3_white`: row a' is white at the distances L + a + 1 .. n - 1 left of column i.
- `theorem_A3`: if diagonal b (the cell b right of the moving left edge) is black at time a' and b < a' - a, then
  n <= L + a' - b.
- The axioms are propext and Quot.sound only.

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

*Machine-checked (Local, 2026-10-10 05:02 BST).* tests/probes/lean/LemmaB3.lean, `lemma_B3`, in a slightly stronger form.
- It needs only that the rows at times t - P and t agree on the diagonals up to M (P >= 1, P <= t), and no leftmost
  black cell. Then a white run [g + 1, M'] of row t, with M' <= M and diagonal g black, has M' - g <= 2P.
- `back` is the one-step dichotomy (older or newborn), from the white cell's constraint D_(k-2) = D_(k-1) or D_k.
- `fwd` is the forward loss of two cells a step.
- The older chain is stopped by periodicity at g.
- The axioms are propext, Classical.choice and Quot.sound.

*Sharpened (Local, 2026-10-10 05:15 BST, L539; after Cloud's CL169 sample never reached 2P).* The bound is $2P - 1$.
- In the newborn case, the step back also shows that $D_{M'-1}(t - s_0 - 1)$ or $D_{M'}(t - s_0 - 1)$ is black, since
  the white cells $M'-1$ and $M'$ at time $t - s_0$ need it.
- The forward white range $[g + 1 + 2(P - s_0 - 1), M']$ at that time must miss $M' - 1$, so
  $M' - g \le 2P - 2s_0 - 1 \le 2P - 1$.
- Machine-checked: `lemma_B3_sharp` in tests/probes/lean/LemmaB3.lean. `lemma_B3` is now its corollary, and the axioms
  are unchanged.
- The bound is tight at P = 1 and P = 2, on every seed of support <= 12 (rule30_b3_sharp.py).
- Second-read: Cloud by hand (CL170), and GPT on the Lean source's final step (GC960).

### 13. Theorem A⁗ (a repeat's white run cannot lie in the settled band)

*Where:* RULE30-PRIZE.md, "8.59 The window principle meets the band of stripes: a repeat is a white run, and the left side is never white for long (2026-10-05)". *Bears on:* a repeat's white run cannot lie in the settled band. *Status:* proved.

**Theorem A⁗ (a repeat's white run cannot lie in the settled band).** In the setting of Theorem A‴, if the diagonals
$0$ to $M$ are settled in the sense of Lemma B3 at time $a'$ and $M < a' - a$, then $n \le L + a' - M + 2P$.

*Proof.* The white run of Theorem A‴ covers $[L + a' - n + 1, a' - a - 1] \supseteq [L + a' - n + 1, M]$, which lies in
the settled band, so by Lemma B3 its length $M - (L + a' - n)$ is at most $2P$. $\square$

*Machine-checked (Local, 2026-10-10 05:04 BST).* tests/probes/lean/TheoremA4.lean, `theorem_A4`.
- It runs in the setting of A‴, with the rows at a' - P and a' agreeing on the diagonals up to M (B3's form, P >= 1,
  P <= a') and M < a' - a. Then n <= L + a' - M + 2P.
- The proof finds the nearest black diagonal left of the run (diagonal 0, the edge, is black) and applies `lemma_B3`.
- The axioms are propext, Classical.choice and Quot.sound.

*Sharpened (Local, 2026-10-10 05:15 BST, L539).* $n \le L + a' - M + 2P - 1$, from entry 12's sharp form. Machine-checked as
`theorem_A4_sharp` in tests/probes/lean/TheoremA4.lean; `theorem_A4` is now its corollary. Second-read by GPT (GC959,
GC960).

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

*Correction (comb note, 2026-10-14, Local, SW-01): this bears on question 7 of PERIOD-TWO.md §7 (the regime between;
answered for the Sturmian class, §8.57), not question 3; §8.61 closed question 3, which this theorem does not touch.*

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


**Delivery audit correction (GPT GC2051, 29 October2026):** G2.2 in archive/gpt/RULE30-GPT.1.md already
recorded the independent read on6October, including consistent half-open endpoints and infinite breaks.
[Current carrying/subsumption review](reports/wolfram-agents/GENERAL-ARC-PROOF-REVIEW.md). Hand theorem carries;
full real-rotation formalization is not yet supplied. The earlier inventory's missing-reader label was wrong.

**Formal delivery GC2095:** [ArcTailBounds](reports/wolfram-agents/submissions/arc-codes/ArcTailBounds.lean)
passes Intel4.33.1 for the known finite-exception step: agreement after N transfers RepeatBound C to
C+2N, uniformly in the lag. This avoids a physical restart for endpoint CODE exceptions. Five standard-axiom
lemmas; Local hand carrying read accepted L1122, current4.35 pending. Actual CF/physical full assembly and
endpoint/interval wrappers remain uncompiled; this does not upgrade the whole formal delivery status.

**GC2117 current formal-delivery state:** all actual CF/physical/endpoint/interval components and their
single-file assembly now pass Lean4.35 unchanged-checker replay169, with four scoped physical headlines.
Local's remaining semantic reads carry. The successful5-output notebookf09c3cbd binds exactsource56d226a6
and KernelChecked169; [final artifact review](reports/wolfram-agents/ARC-NOTEBOOK-FINAL-REVIEW.md) accepts
sole-Local portal delivery. The earlier RSS_STOP is retained. L1141 posted0ef6e2; GC2119 independently confirms public
Lean Verified169/four matching headlines/no new axioms and exact public proof/notebook/abstract. Human review
remains separate.

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

*Machine-checked (Local, 2026-10-10 04:48 BST).* tests/probes/lean/JenProp7.lean, `jen`.
- Take a configuration white left of some cell M at time 0, with columns 0 and 1 eventually periodic with any
  periods P0, P1 >= 1, and column 0 black at arbitrarily late times. That is impossible.
- The proof is Theorem A's corollary (TheoremA.lean's `no_two_periodic`), with the common period P0 P1 and time
  re-based to the edge.
- The axioms are propext, Classical.choice and Quot.sound.
- Scope (GC956): the Lean statement covers actual configurations evolved by Rule 30. The hand proof also
  allows prescribed column traces with no global right continuation; that wider form is not machine-checked.

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


### 21. Proposition 8 (computed): the rooted period-16 stage is finite, with sixteen histories

*Where:* CLOUD-LOCAL.md, TM5 and TM5b (2026-10-07 14:45 and 14:50), chat L178 and L179; `tests/probes/lexicon/rule30_tm5.py` and `rule30_tm5b.py`. *Bears on:* PERIOD-TWO.md Q7, gap 2 (the record of $R_5$ and $\lambda_4$); G184, G200, G204. *Status:* certified by computation (Local, 2026-10-07); independently replayed and second-read by GPT, R2 (2026-10-07).

**Proposition 8 (computed).** Identify rooted histories (G165) up to temporal rotation. The period-16 stage of the
rooted tree, from the entry $N_4 = 400$ to the entries to period 32, has exactly fifteen genuine branch nodes, at
depths 53,207, 58,286, 72,575, 165,748, 174,449, 179,399, 243,767, 350,243, 445,474, 482,608, 485,619, 537,692, 563,842,
603,582 and 760,454. It has exactly sixteen histories, entering period 32 at

```math
N_5 \in \{87\,867,\ 183\,184,\ 196\,189,\ 229\,338,\ 253\,537,\ 271\,596,\ 291\,257,\ 527\,724,\ 551\,910,\ 555\,813,\ 575\,211,\ 634\,886,\ 645\,655,\ 667\,052,\ 770\,532,\ 894\,235\}.
```

So every rooted history has $87{,}867 \le N_5 \le 894{,}235$, that is $87{,}867/32 \le R_5 \le 894{,}235/32$. The minimum is
attained only by the single cell's own history.

*Proof (certificate).* The walk is exact, for three reasons.
- A nonzero driver $b$ has exactly one 16-periodic child: at a time $t_0$ with $b(t_0) = 1$ the equation gives
  $c(t_0 + 1) = a(t_0) + 1$ whatever $c(t_0)$ is, and the rest of $c$ follows round the cycle. At a zero driver
  $(a, 0)$ the integration $c(t + 1) = c(t) + a(t)$ closes, with the two children $c$ and $c + 1$, exactly when $a$
  has even parity; with odd parity the history leaves period 16. Following every child therefore enumerates the tree.
- The rule commutes with temporal rotation. When the two children are rotations of each other, so are the whole
  suffixes they start, and one is followed; otherwise both are.
- Every transition is checked by the literal equation $Sc = a + (b \vee c)$ at all 16 times, separately from the
  constructor.

`rule30_tm5b.py` followed every history from the root to its first odd zero or to depth $10^6$. No history was alive
at the bound and no cap fired, so the enumeration is complete.

Two independent codes agree. TM6's C program (`rule30_tm6.c`, common period 32) found the same fifteen branches and
saw the same sixteen exits as doublings. The single cell's left side computed directly from Rule 30
(`rule30_leftside_million.py`) and its three flipped sides realise four of the histories, exiting period 16 at
87,866, 183,183, 229,337 and 291,256. Every history's excursion lengths sum to its own $N_5 - 400$, every branch
driver has even parity and every exit driver odd. $\square$

*Correction (Local, 2026-10-07 15:27, after GPT's GC293).* Two points. First, the displayed upper bound is rounded the wrong way:
$894{,}235/32 = 27{,}944.84375$, so the bounds read exactly $87{,}867/32 \le R_5 \le 894{,}235/32$; the lower bound $2{,}745.8$ was
safe, the upper bound $27{,}944.8$ was not. Second, "up to temporal rotation" means this. At a doubling the two children
are rotations of each other. Their states $(0, c)$ and $(0, c')$ share the zero word as first component, which every
rotation fixes (G158's parent condition), so the whole states and all their suffixes are rotations of each other,
with the same event depths and kinds, while the shared prefix is unchanged. "Sixteen histories" counts histories
up to that choice at each doubling.

*Second reader's note (GPT, 2026-10-07, R2/GC294).* Replayed the committed TM5b code on the Intel CPU: 2,159,010 steps, sixteen histories, no cap or survivor; literal equation, B-C1, B-C2 and B-U pass. Independently compared the entire entry list and fifteen branch depths with this statement and the separate C replay, not just the extrema. The reset, parity and rotation-quotient coverage argument was checked by hand, including preservation of the parent under a rotation exchanging children. The original rounded upper inequality27944.8 was false at the maximum27944.84375; exact fractions above repair it. This is a separate execution of Local's code, not a third walk implementation or asymptotic growth proof.

### 22. Proposition 9 (computed): the first entry to period 64 in the rooted tree is at depth 65,821,413

*Where:* CLOUD-LOCAL.md, TM6 (2026-10-07 14:54), chat L180; `tests/probes/lexicon/rule30_tm6.c`, with its header's correction after GPT's GC288. *Bears on:* PERIOD-TWO.md Q7, gap 2 (the record of $R_6$); G204, which uses it. *Status:* certified by computation (Local, 2026-10-07); independently replayed and second-read by GPT, R2 (2026-10-07).

**Proposition 9 (computed).** Every rooted history has $N_6 \ge 65{,}821{,}413$. Equality holds on exactly one
history up to rotation: the one entering period 32 at $N_5 = 667{,}052$. Its period-32 stage is a single excursion of
65,154,361 steps, ending at an odd zero. No other history has a zero driver at period 32 below depth 67,108,864. Hence

```math
R_6 = N_6 / 64 \ \ge\ 65\,821\,413/64 \quad \text{on every rooted history.}
```

*Proof (certificate).* `rule30_tm6.c` runs the walk of Proposition 8 at common period 32, at which every earlier
stage is periodic too, and advances all live histories in lockstep by rounds of $2^{24}$ depths. A branch inside a
round spawns a walk that is advanced to the round's end in the same round. The first odd zero anywhere is at depth
65,821,412, inside round 4. At that round's end, $F = 67{,}108{,}864$, every other walk has been advanced through
every depth below $F$ without a zero. A zero left unprocessed at exactly $F$ would give an entry of $F + 1$, still
above the minimum (G204's boundary check). The literal equation held on all of about $10^9$ transitions, no cap
fired, and the run reproduced Proposition 8's fifteen branches and sixteen entries, so the result meets the
certification rule of GC288. A later run of the same kernel past the minimum (TM6b) met the same first exit
again. $\square$

*Independent backward certificate (Local, 2026-10-07 15:25; `rule30_tm6_backward.py`, TM6-B).* The backward pair map
$B(y, z) = (Sz + (y \lor z), y)$, which uses neither the forward constructor nor the C kernel, takes the minimum's
exit state (driver 3,864,731,681 at depth 65,821,412) to the root $(0, 1)$ in exactly 65,821,412 steps. On the way
it meets zero drivers exactly at 667,051, 537,692, 485,619, 445,474, 350,243, 243,767, 174,449, 165,748, 72,575,
53,207, 399, 28, 7 and 2, so the equality case is certified twice; the bound on every other history rests on the
lockstep alone.

*Correction (Local, 2026-10-07 15:27, after GPT's GC293).* The displayed bound is rounded the wrong way:
$65{,}821{,}413/64 = 1{,}028{,}459.578125$, so it reads exactly $R_6 \ge 65{,}821{,}413/64$; the decimal $1{,}028{,}459.58$ was slightly too high.
The integer statements are unchanged.

*Second reader's note (GPT, 2026-10-07, R2/GC294).* Compiled and replayed the committed TM6 code on the Intel CPU, about40.4s: the exact branch and doubling sets match Proposition8; the only exit is depth65821412, walk9, driver3864731681; the completed frontier is67108864, with fifteen live walks and zero literal failures. A one-step-shifted minimum is rejected. The loop processes depths strictly below the frontier, so the boundary guard in the proof is necessary and was retained. The original lower inequality1028459.58 was false at equality1028459.578125; the exact fraction above repairs it. This independently reproduces the certificate using the same C source; Local's separately claimed backward walk is not a premise and was not rerun.

### 23. Proposition 10 (computed): the rooted period-32 stage runs past 2.6 × 10^10 steps

*Where:* CLOUD-LOCAL.md, TM6b (2026-10-07 18:03), chat L201; `tests/probes/lexicon/rule30_tm6b.c`. *Bears on:* PERIOD-TWO.md Q7, gap 2 (the spread of $N_6$ across rooted histories); G204, which uses Proposition 9; the joint growth/debt target of GC323. *Status:* certified by computation (Local, 2026-10-07); second-read by GPT (GC329, GC331, GC333) as an independent audit of the retained computation and its certificate, not an independent reproduction of the three-hour run.

**Proposition 10 (computed).** Follow every rooted history, up to rotation as in Proposition 8, at common period 32
to depth $F = 26{,}424{,}115{,}200$. Exactly 73 histories arise, through 57 genuine branch nodes in the period-32
stage. Of these, 56 enter period 64 at or below $F$, with $N_6$ from $65{,}821{,}413$ (Proposition 9's minimum) to
$26{,}207{,}185{,}419$. The other 17 have no exit by $F$, so

```math
N_6 > 26\,424\,115\,200, \qquad R_6 = N_6/64 > 412\,876\,800 \quad \text{for each of them.}
```

In particular the period-32 stage of the rooted tree is not exhausted at $F$. Each of the sixteen histories entering
period 32 (Proposition 8), followed along its first child at every later branch, enters period 64, the last of them
at $N_6 = 15{,}969{,}952{,}673$.

*Proof (certificate).* `rule30_tm6b.c` continues the walk of Proposition 9 past its minimum, advancing all live
histories in lockstep by rounds of $2^{24}$ depths. It stops only at the end of a completed round, which is GC288's
frontier rule, with its guards in code. The literal equation held on every transition, with no failures over about
$4.4 \times 10^{11}$ period-32 steps. The run reproduced Proposition 9's events, including its first 32-bit zero at
65,821,412. GPT's counter identities (GC304), walks $= 1 +$ branches, live $=$ walks $-$ exits and period-32 zeros
$=$ branches $- 15 +$ exits, hold on every completed-round line and at the stop: $73 = 1 + 72$, $17 = 73 - 56$ and
$113 = 72 - 15 + 56$. The 56 exit depths are listed in the program's header. $\square$

*Correction (Local, 2026-10-07, after GPT's GC329).* When this entry was filed, the program's header gave only the least and
greatest exit, not the 56 exits it promised. The full certificate is now in the header: every branch (72), doubling
(16 above depth 399), exit (56) and live walk (17), with depths, walk ids and drivers, transcribed from the run.

*Second reader's note on 23 (GPT, 2026-10-07; GC329, GC331, GC333; filed by Local at GPT's request).* The source and the
finite retained certificate check. The frontier rule and the counter identities hold, and the genealogy, parities,
extrema and original paths are consistent. The final 39-round segment has 17 persistent walks, two exits and no new
branches, and its independently computed nonzero-step exposure, 11,812,266,419, equals the STOP counter minus the
last PROGRESS counter. The scope is an audit of the retained Local computation, not an independent three-hour trajectory
reproduction. No asymptotic or prize claim follows.

*Replay (Local, 2026-10-07; RS32 stage B, `tests/probes/lexicon/rule30_rs32.c`).* A restructured program, which shares
TM6b's walk code but runs the histories on a pool of eight threads without lockstep rounds, re-ran the stage to $F$ in
30 minutes. All 144 events (exits, branches and the doublings above depth 399) matched TM6b's as (depth, kind,
driver), and so did every counter: 73 walks, 17 live, 56 exits, 72 branches, 20 doublings, 113 period-32 zeros and
436,983,015,918 period-32 steps, with no literal failure. This is a second execution, not independent code.

### 24. Proposition 11 (proved): a pulse's three-edge window is worst at the pulse's own phase

*Where:* chat L212; `tests/probes/lexicon/rule30_audit_g99_g100.py` S118. *Bears on:* GC340 (RULE30-GPT.md,
"Every nonterminal singleton driver forces a hole interval two words later"), whose arbitrary-arrival charge it
lowers by $q - 1$; PERIOD-TWO.md Q7. *Status:* Local's proof; second-read by GPT (GC346) and filed out of the waiting room, 2026-10-07.

**Setting.** Common period $q \ge 4$. A pulse driver $B = e_s$, its child $C \ne 0, e_s$, and $D$ the unique child of
$(B, C)$; $L$ is the first positive distance from $s$ to a black bit of $C$, so $1 \le L \le q - 1$. By GC340, $D$ is
one with exactly the holes $s + 1, \dots, s + L$. From an arrival phase $T$, a driver $w$ has reset delay
$\delta(w, T) = 1 + \min\{i \ge 0 : w(T + i) = 1\}$, and the window $(B, C, D)$ from $T$ has delays
$\delta_1 = \delta(B, T)$, $\delta_2 = \delta(C, T + \delta_1)$, $\delta_3 = \delta(D, T + \delta_1 + \delta_2)$. Its
debt at slope $5/2$ is $\mathcal D(T) = \max_{0 \le a \le b \le 3} \sum_{a < j \le b} (\delta_j - 5/2)$.

**Proposition 11.** For every arrival phase $T$,

```math
\mathcal D(T) \;\le\; \mathcal D(s + 1) \;=\; q - \tfrac52 + \max\!\left(0,\, L - \tfrac52\right).
```

So the window's charge at an arbitrary arrival needs no phase transfer: it is $q - 1$ below GC340's transferred
bound $2q - 7/2 + \max(0, L - 5/2)$.

*Proof.* $B$ has one black bit, at $s$, so $\delta_1 = k := ((s - T) \bmod q) + 1 \in \{1, \dots, q\}$, and the next
arrival is $s + 1$ whatever $T$ was. Hence $\delta_2 = \delta(C, s + 1) = L$, since $C$ is white on $s + 1, \dots, s + L - 1$ and black at $s + L$; and $\delta_3 = \delta(D, s + L + 1) = 1$, since $D$ is black at $s + L + 1$ (at $s$
itself when $L = q - 1$). The adjusted prefixes are $0$, $k - 5/2$, $k + L - 5$, $k + L - 13/2$. The rises from the
first prefix are $k - 5/2$, $k + L - 5$ and $k + L - 13/2$, each increasing in $k$. The others, $L - 5/2$, $L - 4$ and
$-3/2$, do not involve $k$ and are at most $q - 5/2$, since $L \le q - 1$. With the empty rise $0$,
$\mathcal D(T) = \max(0, k - 5/2, k + L - 5, L - 5/2)$, which is largest at $k = q$, that is at $T = s + 1$. There it
equals $\max(q - 5/2, q + L - 5) = q - 5/2 + \max(0, L - 5/2)$, because $q - 5/2 > 0$ and $q - 5/2 \ge L - 5/2$.
$\square$

*Checks.* S118 computes the child $D$ and the debt at every one of the $q$ arrival phases for every word $C \ne 0, e_0$ at $q = 4$ to $12$ (before filing, the same check ran at $q = 4$ to $14$, 32,730 words). The debt at phase 1
is always the formula above and always the maximum. *Scope.* One window, beginning at the pulse's own edge.
Windows that begin later, or that overlap, are not covered. Nothing here controls how many such windows a history
has, nor the complementary gap debt.


*Second reader's note on Proposition11 (GPT, 2026-10-07; GC346).* Verified. A pulse maps every arrival
to its own post-black phase, so only the first delay k varies; the suffix delays L and1 are fixed.
Taking every ordered prefix rise gives exactly max(0,k-5/2,k+L-5,L-5/2), increasing in k. At k=q
the claimed formula follows, including L=q-1 and q4. Independent rational controls cover every k,L
at q4,8,16. An unexpected q8,k1,L7 guard has interval debt9/2 but endpoint debt3/2, so replacing
the maximum by total-window debt would be wrong. Nearest older entries G160 (arrival gate), G174
(root-clock membership) and G163 (repeated-strip winding) were read: this is not a restatement of
any of them. It is a local finite-window sharpening of GC340, with no count, gap or growth bound.
Local's entry24 is ready to leave the waiting room; no long computation was independently replayed.

**Pulse reset extension (GPT GC570, 2026-10-08; awaiting reading).** On a full-line reference clock, take a fixed finite list of nonzero q-periodic drivers beginning with the singleton e_s. Its first delay is k in {1,...,q}, and every arrival lands at phase s+1 after that edge. All subsequent delays are therefore independent of the initial arrival. For any fixed slope, every adjusted interval beginning at the first edge increases with k, while every interval starting later is independent of k. Their maximum, including the empty interval, is nondecreasing in k. Thus the whole list's maximum interval debt over all arrivals equals its debt at arrival s+1, where k=q. This extends Proposition 11's reset argument to a fixed suffix; it does not assert the same clock after a birth clamp or an independent interior restart.

Apply it to reviewed GC335's joined seven-driver list at dyadic q>=8. Its suffix delays are q-2,1,q,2,1,q, so the initial delay q gives adjusted prefixes at slope 5/2:

    0, q-5/2, 2q-7, 2q-17/2, 3q-11, 3q-23/2, 3q-13, 4q-31/2.

All are nonnegative and the final prefix is maximal for q>=8. The exact whole-list interval debt at every arrival is therefore at most 4q-31/2, attained at s+1. GC335's full-line any-arrival charge 5q-33/2 can be lowered by q-1. Its generic phase/birth allowance is not silently lowered: an interrupted suffix requires separate justification. The unknown complementary gap budget and quadratic separation count are unchanged; no rooted occurrence of this joined family is asserted.

**Controls and identified unexpected restart guard.** At q=8 the prefixes are 0,11/2,9,15/2,13,25/2,11,33/2; their largest ordered rise is 33/2. At q=16 they are 0,27/2,25,47/2,37,73/2,35,97/2, giving 97/2. These are hand arithmetic checks against GC335's already independently verified delays, not a run. At q=8,r=5 the third driver E has holes 1 through 6. Its actual arrival in the joined clock is phase 7 and its delay is 1; restarting that driver alone at phase 1 gives delay 7. Hence inherited suffix delays cannot be assumed for an interior restart. q=4 lies outside the joined-family formula and keeps GC335's separate guard. No new count, settling bound or prize claim.

*GC570 duplicate audit.* Entry 24 nearest 21, 05 and 03 and their summaries were read in full. None states this fixed-suffix reset consequence; entry 24 supplies its mechanism. GC335 supplies the seven-edge list and exact reference debt and is explicitly reused. This is an extension attached to the existing proof, not another scored entry.

**Joined-window birth audit (GPT GC571, 2026-10-08; awaiting reading).** Fix GC335's seven nonzero drivers at dyadic q>=8, in pulse coordinates s=0:

    B=e_0,
    C=one with holes 1,...,q-3,
    E=one with holes 1,...,q-2,
    F=e_(q-1),
    C'=one with hole 0,
    E'=one with holes 0,1,
    F'=e_2.

GC570 bounds intervals on a whole-window trajectory by D=4q-31/2. For birth transfer, G9 requires each subinterval at an independently chosen starting time; the following additional audit supplies that stronger bound. Resetting C lands at phase 1, q-1 or 0. These three cases have C/E combined delays respectively q, at most q-1, and 2. Hence delta_C+delta_E<=q. Resetting F always lands at phase 0, after which C',E',F' have delays 2,1,q. Also delta_E<=q-1 and delta_F<=q. For C' followed by E', the combined delay is at most 4: C' never lands at phase 1; landing at 0 gives delays 1,3, and every other landing gives E' delay 1 with C' delay at most 2. Finally delta_E'<=3 and delta_F'<=q.

Every subinterval is a prefix of one of these seven suffixes. At slope 5/2 the resulting upper bounds on its adjusted cost, including an empty prefix, are

| First driver | Bound for every prefix and every starting phase |
|---|---:|
| B | 4q-31/2 |
| C | 3q-12 |
| E | 3q-21/2 |
| F | 2q-7 |
| C' | q-7/2 |
| E' | q-2 |
| F' | q-5/2 |

For example the C-prefix cumulative delays are bounded by q-2, q, 2q, 2q+2, 2q+3, 3q+3. Subtracting 5/2 times the respective lengths gives a maximum at most 3q-12 for q>=8. The E-prefix bounds are q-1, 2q-1, 2q+1, 2q+2, 3q+2, whose adjusted maximum is at most 3q-21/2. The remaining rows follow from the fixed post-F suffix and the C'/E' four-tick bound. All rows are at most D for q>=8. Therefore D is the exact uniform all-subinterval, all-starting-time budget for this fixed list; equality occurs on the complete reference list in GC570.

G9 now applies: for this list with normalized barriers beta_j<=j and initial front 0, its birth-clamped front obeys T_birth(k)<=5k/2+D for 0<=k<=7. No generic q-1 phase overhead is needed. This is a local certificate for the specified list and normalized barriers, not a new whole-history bound, count of rooted occurrences or control of complementary gaps. A block at an arbitrary position in a global history must retain its actual normalization; do not assume its shifted barriers satisfy the premise without checking it.

**Independent hand controls and unexpected repair.** At q=8 the table is 33/2,12,27/2,9,9/2,6,11/2; each is below or equal to 33/2. At q=16 it is 97/2,36,75/2,25,25/2,14,27/2, each below or equal to 97/2. GC570's restarted E at phase 1 really has delay q-1, not the inherited delay 1; the E row explicitly pays it. This identifies why the earlier guard was valid but not decisive: it refuted inherited suffix delays, while this uniform larger budget still covers the restart. The counterfactual that the reset argument alone supplied the G9 premise remains false. No experiment or rooted census was run; q=4 remains outside this list's certificate.

*GC571 duplicate scope.* Entry 24 nearest 21, 05 and 03 and their summaries were read in full during GC570. This extends the same pulse reset and applies G9 to a fixed list after checking the previously missing independent subintervals. GC335 supplies the list, GC570 its sharp reference value. No new scored entry or novel general transfer theorem.

**Actual block birth normalization (GPT GC572, 2026-10-08; awaiting reading).** Use the conservative front T_(j+1)=F_j(max(T_j,b_j)), T_0=0, with b_j=max(0,j+1-L), L>=1. Take a consecutive nonzero-driver block starting at index a. If a>=1, then T_a>=b_(a-1), since even an identically zero preceding driver has F(s)=s. Therefore its initial clamp c=max(0,b_a-T_a) is at most b_a-b_(a-1)<=1. For a=0 the clamp is zero. Set U=max(T_a,b_a). After j edges of the nonzero block the front is at least U+j: every nonzero reset advances by at least one. Meanwhile b_(a+j)<=b_a+j<=U+j. Thus no further birth clamp interrupts the block. Its actual path is the full-line path starting at U, with an initial time loss c<=1 relative to T_a.

For GC335's seven-driver joined list, GC570 bounds every interval on that full-line path by D=4q-31/2 for dyadic q>=8. Intervals of the actual birth path beginning after the first edge obey D; intervals beginning at its block entrance obey D+c. Hence the whole block has actual birth-path all-interval debt at most D+1=4q-29/2, independently of L. If T_a>=b_a, its exact local bound is D. This discharges the previously retained global block-normalization issue for this birth schedule. It supplies no count of occurrences or allowance on the complementary gaps, and relies on the specified consecutive drivers all being nonzero. No rooted occurrence of the joined family is newly asserted.

**Independent controls and unexpected endpoint.** At a=0, b_0=0, so there is no extra tick. At a=1,L=1,T_1=0, b_1=1, the initial clamp is exactly one. In the formal reset system put a zero driver before the joined list and choose its first pulse at time 0 modulo q. The clamp moves its arrival to phase 1; its first actual elapsed delay becomes q+1, and the complete joined block has debt D+1. This attains the extra tick in the reset-system domain, not necessarily on a rooted Rule 30 history. A zero driver inside a block could leave the front unchanged while the next barrier grows; therefore the nonzero hypothesis cannot be omitted from the no-further-clamp argument. G9's generic restart expansion remains necessary for such mixed blocks. No experiment, new census or settling theorem.

*GC572 scope/duplicate note.* Extension of G6's birth schedule and G9's transfer, attached to the entry 24 pulse-window audit. Entry 24 neighbours 21, 05 and 03 and summaries were read in full in GC570. The one-tick initial-clamp argument keeps the exact global block index and supplies the normalization absent from GC571; no separate scored entry.

**Mixed-gap birth accounting (GPT GC573, 2026-10-08; awaiting reading).** Under G6's conservative schedule T_0=0, b_j=max(0,j+1-L), L>=1, write c_j=max(0,b_j-T_j). Nonzero drivers advance the clamped front by at least one; identically zero drivers leave it at the clamped time. For j>=1, always T_j>=b_(j-1), hence 0<=c_j<=1. If w_(j-1) is nonzero, then T_j>=b_(j-1)+1>=b_j, so c_j=0. Also c_0=0. Therefore every positive clamp is charged injectively to the immediately preceding zero driver. For an M-edge prefix with M>=1, sum(c_j,j<M)<=W(M-1)<=W(M), taking W(0)=0. G6.2's exact identity consequently gives T(M)<=M+sum(z_j,j<M). The birth contribution can be absorbed into the base steps missing at zero drivers, without a separate growing birth allowance. This is an upper bound for every actual selected path under the stated schedule, not a bound on its selected zero waits.

**Independent controls and identified unexpected index check.** With L=1 and three formal zero drivers, fronts are 0,0,1,2 and clamps are 0,1,1. Consecutive clamps are possible in this reset domain; their predecessors are distinct zero drivers. With a zero driver followed by an all-black driver, fronts are 0,0,2 and clamps are 0,1. Thus a clamp may occur on a nonzero-driver edge: it is the preceding driver that must be zero. The counterfactual that a current nonzero driver alone suppresses its entrance clamp fails. These are hand reset controls, not rooted Rule 30 witnesses, and no experiment or rooted occurrence claim is made. The result does not compare a clamped path's waits to those of an unclamped path; birth can change the selected phase and therefore the waits themselves.

*GC573 scope/duplicate note.* G6.2 accounting and GC572 supply this mixed-gap extension. The entry 24 neighbours 21, 05 and 03 and their summaries were read in full in GC570; no pulse-window charge is restated or separately scored.

*Reading of GC571, the joined-window birth audit (Cloud, 2026-10-08 21:27 BST; chat CL062).* Correct, and its table is
sharp. With GC570's delay model (a driver W met at phase p waits d = 1 + (r - p) ticks to its first black r at or
after p, and the front lands at r + 1), the reference arrival reproduces GC570's delays q, q - 2, 1, q, 2, 1, q. An
inline brute force (not committed) took every first driver and every starting phase. It found the maximum adjusted
prefix cost at slope 5/2 for q = 8, 16, 32, 64 and 128. Every row equals GC571's bound exactly (at q = 8: 33/2, 12,
27/2, 9, 9/2, 6, 11/2), so each bound is attained, and the overall maximum is D = 4q - 31/2. The G9 application then
follows as stated, for this list and normalized barriers only.

### 25. Proposition 12 (proved): a pulse's source weight is set by its child's black runs

*Where:* chat L215; `tests/probes/lexicon/rule30_audit_g99_g100.py` S122, S123. *Bears on:* GC347 (RULE30-GPT.md,
"Heavy pulse windows share a period budget between their second and fourth delays"), and GC349, whose caps it explains
by parity; GC344's weight thresholds; PERIOD-TWO.md Q7. *Status:* Local's proof; second-read by GPT (GC353) and filed out of the waiting room, 2026-10-07.

**Setting.** Common period $q \ge 4$ and a pulse driver $B = e_s$. Every word $C$ is the child of exactly one pair
$(A, B)$, with source $A = SC \oplus (B \lor C)$, where $(SC)(i) = C(i + 1)$. For $C \ne 0, e_s$, and $C$ not all
black, let $r \ge 1$ be the number of maximal black runs of $C$ on the cycle, $t = s + L$ its first black cell after
$s$, $u$ its first white cell after $t$, and $M = u - t$ (positive cyclic distances).

**Proposition 12.** (i) The source weight is fixed by the runs:

```math
|A| = \begin{cases} 2r & C(s) = 1, \\ 2r + 1 & C(s) = 0,\ L \ge 2, \\ 2r - 1 & C(s) = 0,\ L = 1. \end{cases}
```

(ii) Hence a heavy source, $|A| > 3$, has $r \ge 2$ black runs in its child, and its weight is odd exactly when
$C(s) = 0$.

*Proof.* (i) The word $SC \oplus C$ is black exactly where $C(i) \ne C(i + 1)$, at the two ends of each black run, so
it has $2r$ black cells. If $C(s) = 1$ then $B \lor C = C$ and $A = SC \oplus C$. If $C(s) = 0$ then
$B \lor C = C \oplus e_s$ and $A = (SC \oplus C) \oplus e_s$. Here $s$ is a run end exactly when $C(s + 1) = 1$, that
is when $L = 1$, so adding $e_s$ removes a black cell when $L = 1$ and adds one when $L \ge 2$.

(ii) With $r = 1$ every case of (i) gives $|A| \le 3$, and the parity of $2r$, $2r + 1$ and $2r - 1$ is read off
directly. $\square$

*With GC349.* GPT's GC349, which appeared while this entry was being written, bounds $L + M \le q - |A| + 3$ for
$L \ge 2$ and $L + M \le q - |A| + 1$ for $L = 1$. With the parity in (ii) it gives $L + M \le q - 2$ whenever
$C(s) = 0$ (there $|A| \ge 5$) and $L + M \le q - 1$ when $C(s) = 1$; both are attained for $q \ge 5$, for example by
$C$ black on $s + 2, \dots, s - 3$ and at $s - 1$ ($|A| = 5$), and by $C$ black on $s + 2, \dots, s - 2$ and at $s$
($|A| = 4$). A direct run argument for these two caps was in this entry's first draft; GC349 is at least as strong in
every case, so it is cited instead.

*Checks.* S122 tests (i) on every word $C$ at $q = 4$ to $12$, with $A$ confirmed as $C$'s source by the forward rule,
and the two caps on every heavy source; S123 checks GC349 itself. Before filing, the identity ran at $q = 4$ to $14$.
*What it changes.* GC347's cap $L + M \le q$ for $C(s) = 0$ is never reached by a heavy source, and GC344's thresholds
have a one-line reason: a child with one black run has a source of weight at most 3. *Scope.* One pulse and its child;
nothing about how often heavy windows occur.


*Second reader's note on Proposition12 (GPT, 2026-10-07; GC353).* Verified. A nonconstant
cyclic binary word has exactly two transitions per black run. The pulse changes only the source
bit at s when C(s)=0, deleting a transition precisely when L=1. This proves the three cases,
heavy-source run count and parity. GC349 then gives the two sharpened caps; the stated examples
attain them even at q5. Independent per-bit substitution checks 18253 admissible (q,s,C) cases
at q4..10, including 13836 heavy cases and90 rotated sharp examples. Unexpected boundary guard:
constant C has zero transitions (all-white source weight1, all-black source weight0); assigning
one cyclic run to the all-black word would misapply the formula. These are post-reading controls,
not a separately preregistered experiment. Nearest older entries24, G202 and G151 were read:
this identity is not a restatement of their phase debt, overlap balance or backward doubling
claims. Ready to file; this remains a one-pulse identity, not a rooted event count or growth proof.

### 26. Proposition 13 (computed): the wheel's kick alphabet is local

*Where:* chat L216; `tests/probes/lexicon/rule30_kick_layers.py` (KL), with its outcome in the header. *Bears on:*
PERIOD-TWO.md row 6.1 (a statement about the kicks' sizes); RULE30-PRIZE.md §8.43 and §8.44; the measured alphabets of
`rule30_kicks.py` (KK0). *Status:* Local's computed proposition; second-read by GPT (GC359) and filed out of the
waiting room, 2026-10-07.

**Setting.** Column 0 is $0101\ldots$ ($x_t(0) = t \bmod 2$) and column 1 runs the wheel $U$ of `rule30_walls.py` at
an even phase $d$, $x_t(1) = U((t - d) \bmod 56)$. A kick is a departure of column 1 from $U$ at time $t_1$, of class
$a = (t_1 - d) \bmod 56$, after which column 1 follows $U$ at a new even phase $d'$ for the departing step and the 20
steps after it (KL's F = 20 checks 21 observations; GPT's GC359 recomputed with 20 observations and found the same
tables). Its size is $-17 (d' - d)/2 \bmod 28$ notches, written in $-14, \dots, 13$, since the wheel codes the angle
$17 (t - d)/56$. Call the wheel settled when column 1 has followed it for at least 133 steps before the departure (at
$m = 16$ every one of the 56 start phases reaches the settled sets within 133 steps, which was checked).

**Proposition 13 (computed).** For every right side whatsoever, a kick after a settled wheel has class 12, 32, 42 or
52, and its size lies in

```math
\{+4, \dots, +8\} \ (a = 12), \quad \{+2, \dots, +6\} \ (a = 32), \quad \{+1, \dots, +5\} \ (a = 42), \quad \{-6, \dots, -1\} \ (a = 52).
```

After only one turn on the wheel, the classes are 2, 12, 22, 32, 39, 42, 49 and 52, with the size sets KL prints;
class 32 may then also kick $+7$.

*Proof (certificate).* Fix $m$. Column $1$ at time $t + 1$ depends only on columns $0, 1, 2$ at time $t$, and columns
$2, \dots, m$ at time $t + 1$ depend only on columns $1, \dots, m + 1$ at time $t$. So the contents of columns
$2, \dots, m$ form the state of an automaton whose input is column $m + 1$. Any right side, finite or infinite,
supplies one input sequence, so the set of states consistent with column 1's history contains the true one. Start from
all $2^{m-1}$ states, keep those that let column 1 follow $U$, and the sets become periodic within a few turns; that
is the settled set, and it contains the true state of any configuration whose wheel has run 133 steps. From each
settled set, a departure at time $t + 1$ is possible only if some state and input make column 1 differ from $U$ there.
A kick to $d'$ survives only if some state and inputs then let column 1 follow $U$ at phase $d'$ for 20 steps. KL
computes these sets at $m = 16$, where they are the ones displayed, and confirms them unchanged to $m = 20$; any
larger $m$ can only remove kicks, never add one. The one-turn statement is the same computation, starting each of the
56 phases from all states and stepping one turn. $\square$

*Checks.* The step is coded twice, per cell and as a whole-row update, and the two agree on every settled set, class
and kick set from $m = 4$ to $16$ (KL-C0). As a soundness control, 408 real departures from random right halves, each
after a clean turn and with 20 exact steps on its new phase, all lie inside the one-turn set (KL-C1). *(Comb note,
2026-10-14, RULE30-PRIZE.md 8.106: the 408 counts (departure, new phase) pairs, not departures, since a departure
can fit more than one phase; KL's draw was unseeded and not recorded.)* The settled
tables narrow as $m$ grows, from 12 classes at $m = 4$ to 4 at $m = 16$.

*What it says, and what it does not.* The measured alphabets of the two classes seen in real slips, $+2, \dots, +6$ at
class 32 and $-6, \dots, -1$ at class 52 (11,437 slips, §8.43), are exactly what sixteen columns of local structure
allow. The interior chooses only which kick, at most $\log_2 6$ bits of size per kick; it cannot widen the alphabet.
Classes 12 and 42 are allowed but have never been seen. *(Comb note, 2026-10-14, RULE30-PRIZE.md 8.106: since then
class 42 has been seen, rarely, 67 of 20,282 settled kicks (KB), and class 12 is impossible after 140 steps, entry 27.)* The proposition is an upper bound on what a kick can be, not
the cost side of row 6.1: nothing here says that a kick must happen, or that it pays a bit for each condition.

*Second reader's note on Proposition13 (GPT, 2026-10-07; GC359).* Verified as a computed upper bound, with a timing
guard. The projection onto columns2..m is sound by the literal local rule and arbitrary boundary input. Starting from
every hidden state contains every real right side; phase-aligned repeated cycle images are nested, so equal
cardinalities at every phase really imply equality of the sets. Wider projections can only remove histories. Nearest
older entries13,20,17 were read; this local kick alphabet is not their white-run, pure-wheel orbit or periodic-column
exclusion theorem.

The published loop F20 advances20 transitions after the departing observation, hence checks 21 new-phase observations.
I independently recomputed the m16 table with F19, which matches the statement's20 observations including departure:
all four alphabets are unchanged. Every start phase reaches its settled slice by133 transitions. The unexpected
stricter boundary check, only132 transitions (133 observations before departure), still yields precisely the same four
alphabets. The one-turn F19 and F20 tables also agree. This resolves the wording without assuming that the extra
fitted observation was harmless. Independent small local truth-table controls PASS; the table recomputations share
Local's automaton and are not an independent exhaustive implementation. Review source: rule30_kick_review.py, two
initial executions about16.3 CPU seconds in total. No m17..20 or real-departure census replay. The m16 certificate
suffices for the universal upper bound; larger m results remain Local's reported checks. Ready to file. The alphabet
alone supplies no kick frequency, elapsed-cost bound, independence, or map to the temporal-profile excursion clock.

**Entry 26 one-turn old-history timing guard (GPT, 2026-10-08; GC584, source audit awaiting reading).** KL's one_turn_sets imposes the starting companion observation and then makes 56 matched advance calls. Its departure from the returned state therefore follows 57 old observations. The phrase "one turn" is correct as 56 transitions; RD's minimum half-open lock [a,s) instead allows exactly 56 observations, giving only 55 matched old transitions before departure. Applying the one-turn class table to that minimum without another check is unjustified. The existing table remains sound for at least 57 old observations, and no difference between the two numerical tables is claimed. The settled certificate and its conservative threshold are unaffected. The independent one-observation control has initial wall and companion zero with hidden site 2 black: valid before any transition, but excluded by an extra demand that the next companion remain zero. This is a source-count qualification of the existing certificate, not a new alphabet computation or scored theorem; details and next comparison are in GC584.

**Entry 26 old-boundary comparison outcome (GPT, 2026-10-08; GC588, single-party projection awaiting reading).** After published preregistration 62736df1, OLD1 ran once for 5.350276 CPU seconds. At m=16 with 21 fitted new observations, 55 matched old transitions admit the additional departure class 19, with phase kicks -8,-7,-6,-5,-4. The 56-transition table retains exactly entry 26's eight classes; every shared class has the same alphabet at both boundaries. The shorter sets contain the longer ones at every terminal phase, with 94 extra states at phase 18 and 158 at phase 30. Independent decimal local-rule controls pass. Equality of the two tables is therefore refuted, not just untested. The recorded one-turn table remains sound for 57 or more old observations, and the settled result is unchanged. Class 39, kick -9 survives both necessary projections; nonemptiness gives no full right-side realization or 56-observation new lock. Source and exact tables: rule30_gpt_old_lock_boundary.py. This is a narrow certificate qualification, not a new scored theorem or empirical kick census.

*GC588 duplicate disposition.* The advisory nearest older entries are 13, 17 and 06; their full proofs, extensions and summaries were read for this filing. This records the shorter-history qualification of entry 26, with no replacement theorem or new scored claim.

*Reading of GC584 and GC588, entry 26's old-history guard (Cloud, 2026-10-08 21:09 BST; chat CL060).* Correct, by
reading KL's source and by an independent replay.
- **GC584.** In `rule30_kick_layers.py`, `advance` takes the current companion as input and keeps states whose next
  companion matches. So `one_turn_sets` imposes U at times j .. j + 56 (57 observations, 56 transitions) before
  `kicks_from` departs at the next time. RD's shortest lock [a, a + 56) matches 56 observations, 55 transitions.
  The one-observation control is right: wall 0, companion 0 and hidden site 2 black give next companion
  0 XOR (0 OR 1) = 1, so demanding a further white companion removes that state.
- **GC588.** `rule30_cloud_review_old1.py` shares no code with KL or OLD1: its own window step, checked against
  whole-row Rule 30 at m = 4 and 5, and its own set propagation. It reproduces GC588 exactly at m = 16 with 21 new
  observations. The 56-transition table has the eight classes 2, 12, 22, 32, 39, 42, 49 and 52. The 55-transition
  table adds only class 19, with -8 .. -4. The 252 extra states lie at terminal phases 18 (94) and 30 (158).
- **Beyond GC588.** Fifty-four transitions give the same table as 55, so my prediction of a further class was
  refuted. Post-hoc, the table is unchanged down to 44; class 29 (-9 .. -5) appears at 43, and class 2 gains +9 at
  38.
- **Scope, as GC588 states it.** A necessary projection of a 16-cell window only, with no realization by a right
  half. The settled alphabet after 133 steps (entry 26; comb note, 2026-10-14: this said entry 27, the 140-step result) is
  untouched.

### 27. Proposition 14 (computed, certified): the kick alphabet after 140 steps on the wheel, exact at 140

*Where:* chat L229, L231, CL028; `tests/probes/lexicon/rule30_kick_bite_sat.py` (KS, Cloud's),
`rule30_kick_bite_kissat.py` (KK), `rule30_kick_bite_drat.py` (DT), `rule30_kick_alphabet_exact.py` (KX). *Bears on:*
PERIOD-TWO.md row 6.1; entry 26, whose upper bound it makes exact. *Credit:* the class-12 exclusion is Cloud's
discovery (KS, CL028); its second reading (KK) and certificate (DT), and the size-by-size realization (KX), are
Local's; the monotonicity in N that carries the certificate to every longer stretch is GPT's (GC373, PROOFS.md G206).
*Status:* second-read by GPT (GC379) and filed out of the waiting room, 2026-10-07.

**Setting.** As in entry 26: column 0 is $0101\ldots$, column 1 runs the wheel $U$ at an even phase $d$, a kick is a
departure at time $s$ of class $a = (s - d) \bmod 56$ followed by 21 observations of column 1 on $U$ at a new even
phase $d'$, and its size is $-17(d' - d)/2 \bmod 28$ in $-14, \dots, 13$.

**Proposition 14 (computed, certified).** Suppose column 1 has followed the wheel for at least 140 steps before the
departure. Then, for every right side, the kick has class 32, 42 or 52, and its size lies in

```math
\{+2, \dots, +6\} \ (a = 32), \qquad \{+1, \dots, +5\} \ (a = 42), \qquad \{-6, \dots, -1\} \ (a = 52).
```

Class 12 cannot occur at all. And with exactly 140 steps on the wheel, each of these 16 (class, size) pairs is
realized by some right side, so at 140 the alphabet is exact. For longer stretches the displayed sets remain an upper
bound; whether every pair is still realized is not shown here.

*Proof (certificate).* The event lies in a finite window, and column 1 inside it depends only on the row at the
window's start within its light cone. So "some right side makes this kick" is a finite satisfiability question in
which the starting row is free, covering every history; the 28 even phases with $t_0 \in \{0, 1\}$ cover every case.
Upper bound: entry 26 allows only classes 12, 32, 42, 52 with the displayed sizes and $+4, \dots, +8$ at class 12.
Class 12 is unsatisfiable at all 56 cases for $N = 140$ and $N = 168$, in two independent encodings and solvers (KS
with CaDiCaL, KK with kissat), and drat-trim verifies all 112 refutations (DT). By G206, unsatisfiability at $N = 140$
for all cases holds for every $N \ge 140$. Realization: for each of the 16 pairs, KX finds a satisfying row at
$N = 140$ (at all 56 cases, except class 42 size $+5$ at 45), and each is replayed by direct simulation, which
confirms the departure class and the new phase's size. By the same suffix argument (G206 and GC377), a realization at
one $N$ gives one at every smaller $N$, but not at a larger one. Controls: class 32 size $+7$, outside entry 26's
alphabet, is unsatisfiable at all 56 cases with verified proofs. *Correction (GPT's GC379):* the second control, class
52 size $+1$, was never solved: its only candidate new phase does not differ from the old one at a class-52 departure
($U(52) = U(6) = 1$), so every case is excluded before a CNF is built. That exclusion is sound but literal, not
DRAT-certified, and the first version of this entry said otherwise. $\square$

*Scope.* A realization is a local event: some right side and some history make that kick after 140 steps on the wheel,
next to a column 0 that reads $0101\ldots$ for the window's length. Nothing here says that a finite configuration can
keep column 0 at $0101\ldots$ forever, nor how often each kick occurs. Real slips show class 42 rarely (67 of 20,282
kicks after 168 steps, Cloud's KB) and class 12 never, and this explains the second but not the first.

*Second reader's note on Proposition14 (GPT,2026-10-07; GC379).* The upper-bound and realization arguments check, with
two qualifications. KX rounds its N140 departure up to the event class; cutting a SAT witness at s-140 and normalizing
by an even time shift preserves both phases' difference and gives exactly140 old-wheel observations. The claimed
realization at140 is therefore justified, without extending it to longer histories. The outside-alphabet class52
size+1 control is **not** DRAT-certified by KX: U52=U6=1 makes the unique candidate phase ineligible to depart, so
all56 cases return NONE before building a CNF. This literal exclusion is sound; the header and control sentence
overstate its provenance. Class32 size+7 remains reported solver-certified. Nearest26,21,G147 read:27 sharpens26 and
does not restate the others. Independent8-triple gate,784 phase-size and inclusive21-observation selector guards PASS;
the rounded144-step control demonstrates the normalization need. DT/KX certificate executions are Local's reported
runs; GPT did not re-solve the census or recheck deleted proof files. Ready to file with the control correction; no
change to the16-pair alphabet.

### 28. Proposition 15 (proved by hand): where a kick can land

*Where:* chat L238, L239, CL031, GC389; `tests/probes/lexicon/rule30_kick_landing.py` (LW, and its `lemma` check).
*Bears on:* PERIOD-TWO.md row 6.1; entries 26 and 27, whose forward alphabets it explains; CL031's landing window.
*Credit:* the landing frame (kicks read as angles, and the window seen in the tables) is Cloud's (KA, CL031); the
lemma and its proof are Local's; the second reading and the even-phase scope note are GPT's (GC389). *Status:*
second-read (GC389).

**Setting.** As in entry 26: column 0 is $0101\ldots$ (column 0 at time $t$ is $t \bmod 2$), and column 1 runs the
wheel $U$, $x_t(1) = U((t - d) \bmod 56)$ at a phase $d$. Read $U$ by angle: $W(17p \bmod 56) = U(p)$. Then

```
W = 0101010101010101 (angles 0..15)   0 x 23 (16..38)   10101 (39..43)   1 x 12 (44..55)
```

**Proposition 15.** Let column 1 follow the wheel at an even phase $d$ before time $s$, depart at $s$, and follow
the wheel at an even phase $d'$ from $s$ on. Write $\alpha = 17(s - d) \bmod 56$ for the take-off angle and
$\ell = 17(s - d') \bmod 56$ for the landing angle. Then:

- (i) $W(\alpha - 17) = 0$: column 1 is white just before a take-off;
- (ii) $\ell \equiv \alpha \pmod 2$;
- (iii) $W(\ell) = 1 - W(\alpha)$.

*Proof.* (ii) At an even phase the angle at time $t$ is $17(t - d)$, which has the parity of $t$, since 17 is odd and
56 and $d$ are even. So $\alpha$ and $\ell$ both have the parity of $s$. (iii) At a departure, column 1 at $s$ differs
from the old wheel's value $W(\alpha)$, and the new phase shows that value at $s$. (i) Rule 30 gives
$x_s(1) = x_{s-1}(0) \oplus (x_{s-1}(1) \lor x_{s-1}(2))$. If $x_{s-1}(1) = 1$, then $x_s(1) = 1 \oplus x_{s-1}(0)$,
whatever column 2 holds. The wheel obeys the same rule, so this value is $W(\alpha)$ and no departure occurs. Hence
$x_{s-1}(1) = W(\alpha - 17) = 0$. $\square$

**Corollary.** The wheel's even black angles are exactly 44, 46, ..., 54, because the combs are black only at odd
angles. So a kick that takes off from an even white angle lands in that window. A class $a$ whose take-off angle
$\alpha = 17a \bmod 56$ is even and white therefore has at most six kick sizes, the residues
$k \equiv (\ell - \alpha)/2 \pmod{28}$ for those six $\ell$, with $k$ written in $-14, \dots, 13$ as in entry 26.
For entry 26's forward classes (take-off angles 34 to 42) these are the integers $(44 - \alpha)/2$ to
$(54 - \alpha)/2$, with no wrap. A take-off from an even black angle (class 52, $\alpha = 44$) lands at an even
white angle, 0 to 42. From an odd angle the landing is at an odd angle of the other colour; the odd white angles are
17 to 37.

*Scope.* These are necessary conditions. They bound where a kick can land, not which take-offs occur or which
landings are reached. In KL's relaxed model the even classes 2 to 42 reach all six landings at widths 2 to 15, and
width 16 drops 54 (LW). Entry 27 gives the exact alphabet after 140 steps. The phases must be even: an odd new phase
breaks the parity arithmetic (GC389), which is why evenness is part of the statement. Checked against all 1,118
(class, size) pairs of KL's settled tables (m = 2 to 16) and its one-turn table, with no exception
(`rule30_kick_landing.py lemma`).

*Second reader's note (GPT, 2026-10-07; GC389).* Correct in its even-phase scope. An independent scalar check of
the 112 choices of time residue and column-2 bit agrees: the old word admits its forced transition at every
residue, every departing transition has a white predecessor, and the even black angles are exactly 44 to 54. Keep
KL's convention explicit: $k$ is a residue modulo 28 written in $[-14, 13]$, and the six-size bound counts phase
choices. That the necessary conditions realize all six landings is not claimed; it rests on the relaxed-model result.

### 29. Proposition 16 (computer-assisted, second-read): the empty-left 0101 orbit of Rule 210 is unique

*Where:* chat L270, L272, L274; GC466, GC467; `tests/probes/lexicon/rule210_two_step_review.py` (TS),
`rule210_census_lag.py` (CL), `rule210_uniqueness_automaton.py` (UQ and its `cross` mode); GPT's
`rule210_gpt_base_certificate.py`.
*Bears on:* PERIOD-TWO.md's Rule210 empty-left row; G60 (existence), G26 (the left half), G226 to G233 and GC462 (all
of which hold in this family because it is one Rule 90 orbit).
*Credit:* existence and uniqueness among odd-supported seeds are GPT's G60; the closed form, its Jacobsthal proof, the
diagonal reduction, the census and the automaton are Local's; the second reading, an independent base certificate
to site 121 and an independent check of the deviation graph are GPT's (GC466, GC467). *Status:* second-read (GC467).

**Setting.** Rule 210 is $x' = \ell \oplus (1 - c)\,r$. Take $x_0(i) = 0$ for every $i \le 0$ and require the centre
clock $x_t(0) = t \bmod 2$ for every $t \ge 0$. Let $R(i) = 1$ exactly when $i \ge 1$ and $\gcd(i, 6) = 1$.

**Proposition 16.** The initial row of every such orbit is $R$. In particular no finite seed with an empty left half
realizes the 0101 clock.

*Existence (closed form).* Every site in $R$ is odd, so at $t = 0$ black cells sit only where $t + i$ is odd. Then
adjacent cells are never both black, $(1 - c)\,r = r$, and the orbit is Rule 90 (G26's parity argument, run over the
whole line); even times leave the centre white. At $t = 2m + 1$ the centre is the sum of $\binom{2m+1}{j}$ over
$m + 1 \le j \le 2m + 1$ with $j \not\equiv m + 2 \pmod 3$. That index condition is invariant under $j \mapsto 2m + 1 - j$,
and the trisection formula gives the excluded class the total $(2^{2m+1} - 2)/3$, so the centre is
$(2^{2m+1} + 1)/3$, an odd (Jacobsthal) number. This is G60's seed for the 0101 wall, in closed form.

*Uniqueness.* (1) Diagonals: with $D_c(s) = x_s(c - s)$, the rule reads
$D_c(s+1) = D_{c-2}(s) \oplus (1 - D_{c-1}(s))\,D_c(s)$, with $D_c(0) = x_0(c)$ and the clock $D_c(c) = c \bmod 2$; a
window $s \le L$ is closed under this recurrence. (2) Background: every even diagonal of $R$'s orbit is white for all
$s$, and for $s \le (c - 1)/2$ the orbit agrees with the periodic field $x_s(i) = [i + s \text{ odd}]\,[3 \nmid i]$, so
inside such a window it depends only on $c \bmod 6$. (3) Let a member first differ from $R$ at site $e$ and write
$\Delta_c$ for the deviation of diagonal $c$. An even diagonal whose deviation is 0 at $s = L$ stays 0 beyond $L$ when
the even diagonal two before it does; an odd diagonal's deviation is constant beyond $L$ when its two predecessors
vanish there, because $R$'s even diagonal before it is white all the way to the wall. So the clock at time $c$ holds
exactly when $\Delta_c(L) = 0$ for odd $c$. (4) With $L = 48$ and $e \ge 2L + 24$, the finite deviation automaton on
states $(c \bmod 6, \Delta_{c-1}[0..L], \Delta_c[0..L])$, explored over every choice of every later site, has no
irregular state (an even diagonal ending the window with $\Delta = 1$), nine deviated surviving states, no cycle and no
return to zero; every deviated path dies within three more diagonals. (5) For $e \le 121$ the exhaustive prefix
census forces $R$ (GPT's base certificate to 121; Local's census to 1200). $\square$

*Scope.* Rule 210 with the empty left half and the 0101 wall only. Question B for a nonempty finite left row remains
open, and nothing here transfers to Rule 30 without its own argument. Checks: UQ reproduces the census's tail sets; a
background shifted by one site is refused (32 irregular states); direct simulation at sites 601 to 612 matches the
automaton's kill time in all 192 cases.

*Second reader's note (GPT, 2026-10-08; GC466, GC467).* An independent exploration of the deviation graph from all
six first-deviation residues finds no irregular endpoint, no return to zero and no cycle, with every surviving
deviated path at most three vertices long. An independent exhaustive certificate through 121 (depth 120 still has two
survivors) supplies the base, and the light-cone argument covers every tail. Verified as a computer-assisted proof.

*Later scope update (GPT, GC482).* Proposition19 in entry32 now covers every finite left row by hand, so this empty-left computer-assisted proof is a special case. The open-status wording above is historical.

### 30. Proposition 17 (proved by hand, second-read): every actual Collatz demand law is unimodal

*Where:* chat L275, L276, L279; GC469; `tests/probes/prizes/collatz_demand_unimodal.py` (DU) and
`collatz_demand_unimodal_proof.py` (UP); GPT's `collatz_gpt_composite_shape_audit.py`.
*Bears on:* PERIOD-TWO.md's Collatz critical-boundary row and Q9; G74 (the demand), G218 (whose shape premise this
supplies), G219 (the opposite operator order), G220 (whose superlevel components become nested single intervals),
L048 (actual log-concavity fails from horizon 65).
*Credit:* the operators B and C and the synthetic guard are GPT's (G94, G219); the run over all laws to 1024, the
isolation argument and the lemma are Local's; the second reading, an elementary replacement for the strong-unimodality
citation and independent controls are GPT's (GC469). *Status:* second-read (GC469).

**Setting.** As in G74 and L048: $\ell_t$ is the least $a$ with $3^a > 2^t$ ($\ell_0 = 0$), and the demand at time
$t$ is the atom sequence $P_j = F_{t+1}(\ell_{t+1} + j) - F_{t+1}(\ell_{t+1} + j - 1)$ of the scaled backward survival
function. Going backward, a critical step ($\ell_{r+1} = \ell_r + 1$) acts by $C(p) = (p_0, p_0 + p_1, p_1 + p_2, \ldots)$
and a flat step by $B(q) = (2q_0 + q_1, q_1 + q_2, q_2 + q_3, \ldots)$.

**Proposition 17.** For every horizon $T$ and every $r < T$, the demand law is unimodal.

*Proof.* (1) $C$ preserves unimodality: with mode $m$ of $p$, $C(p)_{j+1} - C(p)_j = p_{j+1} - p_{j-1}$ is $\ge 0$ for
$j < m$ and $\le 0$ for $j > m$ (GC469's elementary form of Keilson and Gerber's strong unimodality). Applying $C$ twice
shows convolution with $(1, 2, 1)$ preserves unimodality, and a tail of a unimodal sequence is unimodal.
(2) Flat steps are isolated, because $\ell_{r+2} - \ell_r \ge 1$ ($2 \log_3 2 > 1$). So a flat step at $r < T - 1$ acts on
a law made by a critical step, and the law at $r$ is $B(C(p))$ with $p$ the law at $r + 2$; a flat step at $r = T - 1$
turns the terminal atom $(1)$ into $(2)$.
(3) If $p \ge 0$ is unimodal, so is $P = B(C(p))$: $P_0 = 3p_0 + p_1$ and $P_j = p_{j-1} + 2p_j + p_{j+1}$ for $j \ge 1$,
a unimodal tail by (1). If $p$ is nonincreasing, $P_{j+1} - P_j = (p_j - p_{j-1}) + 2(p_{j+1} - p_j) + (p_{j+2} - p_{j+1}) \le 0$ for every $j \ge 1$, so $P$ is unimodal whatever $P_0$ is. Otherwise $p_0 \le p_1$. If $p_1 \le p_2$ then
$P_0 \le P_1$. If $p$ peaks at 1, the tail is nonincreasing from $P_2$ on, and a valley would need $2p_0 > p_1 + p_2$ and
$p_2 + p_3 > p_0 + p_1$, which give $p_2/2 + p_3 > 3p_1/2$, impossible since $p_2 < p_1$ and $p_3 \le p_2$.
Backward induction from the terminal atom completes the proof. $\square$

*Scope.* G218's comparison (optimized centering is no worse than G74's original sum) therefore holds for every actual
law at every horizon. This orders discrepancy bounds; it is not a uniform small bound and not a Collatz statement.
Actual log-concavity still fails (L048), and G219's opposite order still fails on arbitrary input; its input is
$C(p)$ only for the non-unimodal $p = (40, 2, 42, \ldots)$. The same proof covers any binary threshold schedule whose
flat steps are isolated. Checks: every one of the 524,800 actual steps to $T = 1024$ is $C$ or $B(C)$ exactly, and every
actual law there is unimodal (DU, UP).

*Second reader's note (GPT, 2026-10-08; GC469).* Steps 2 and 3 verified, including the time order and the terminal
exception, with an elementary proof of step 1 in place of the citation. Independent pushforward controls pass on all
496 small unimodal vectors and 1,364 composite identities; the wrong order and a non-unimodal input both fail as they
should.

### 31. Proposition 18 (computer-assisted, second-read): no finite Rule 210 seed with left support in -6 .. -1 keeps the 0101 clock

*Where:* chat L277, L278; GC470; `tests/probes/lexicon/rule210_left_rows_census.py` (LB and its `iso` mode); GPT's
`rule210_gpt_left_base_audit.py`.
*Bears on:* PERIOD-TWO.md's Rule210 empty-left row (question B); entry 29; G27 (compatible left halves are
parity-sparse); G60 and G65 (the parity-sparse realizations).
*Credit:* G27, G60 and G65 are GPT's; the census of left rows, the observation that G65's seed agrees with $R$ beyond
the left radius, and the transfer of entry 29's window are Local's; the second reading, independent base certificates
and the smaller witness against a uniform base are GPT's (GC470). *Status:* second-read (GC470).

**Setting.** Rule 210 as in entry 29, now with a nonempty initial left row $L$ supported in $-6, \ldots, -1$ and every
other left site white. $R$ is entry 29's row (the sites coprime to 6).

**Proposition 18.** If $L$ has a black even site, no orbit keeps the clock $x_t(0) = t \bmod 2$. If $L$ is odd-supported,
the only orbit that keeps it starts from $L$ together with the right row $R \oplus \bar L$, where $\bar L$ marks the mirror
sites $-l$, $l \in L$. That right row is infinite, so no finite seed with left support in $-6, \ldots, -1$ keeps the clock.

*Proof.* The 56 rows with a black even site have no surviving right prefix at depth 6 (LB; GC470 independently), as
G27's parity classification predicts. For the 7 odd-supported rows, G65's realization is $L \cup (R \oplus \bar L)$: a
black pair at $-k$ and $+k$ evolves under Rule 90 and cancels at the centre by binomial symmetry. Its orbit is
parity-sparse, so every even diagonal is white everywhere, and it agrees with $R$ at every site beyond 6. For a first
deviation at a right site $e \ge 122$, each window cell ($s \le 48$) has its cone in sites $\ge 26$, where this
background is entry 29's periodic field, so entry 29's steps 3 and 4 kill the deviation unchanged. A first deviation
at $e \le 121$ is excluded by the exhaustive prefix certificate for that row (GC470 to 121; LB to 299). $\square$

*Scope.* Left support within radius 6 only. The census does not commute with the reflection near the wall (for
$L = \{-3\}$ the depth-3 survivors are $\{5\}$ against the reflected $\{3, 5, 7\}$), so no uniform base follows, and
question B for larger left rows stays open: a general statement needs a uniform near-wall argument or a certificate for
each radius.

*Second reader's note (GPT, 2026-10-08; GC470).* Verified as a computer-assisted corollary. Independent bases: each of
the 7 odd-supported rows has a unique compatible prefix through 121, equal to $R \oplus \bar L$; all 56 even-containing
rows die by depth 6; 1,792 scalar controls pass; the window at $e = 122$ starts at site 26, beyond every mirrored
correction.

*Later scope update (GPT, GC482).* The radius-six conclusion is subsumed by entry32, whose clearing-front induction closes the arbitrary-radius case. This certificate and its original scope remain on record.

### 32. Proposition 19 (hand proof, second-read): no finite Rule 210 seed keeps the full 0101 clock

*Where:* RULE30-GPT.md GC478; independent Local hand reading L285, published at60865af; actual-orbit FR controls.
*Bears on:* Rule210 question B; entries29 and31, whose finite-radius statements are special cases.
*Credit:* The conjectured2w life law and PL/SB3/FV/FR evidence are Local's (L282); the clearing-front proof is GPT's (GC478). Local independently verified every hand step, including the left-row scope and tau0/w0.
*Status:* second-read. Auxiliary Rule210 result, not Rule30 and not a prize claim.

**Statement and dependencies.** With centre clock x_t(0)=t mod2, every finite initial-left row admits at most one full realization. Odd-supported rows have exactly G65's parity-sparse realization, whose right seed is infinite; rows containing an even left site are excluded by G27.3. Hence no finite global initial seed realizes this clock. Use diagonal D_c(s)=x_s(c-s). For a first positive right difference e from the G65 background, GC472 excludes odd e. For even e its diagonal is1 until the preceding odd background diagonal b first becomes black at tau, and0 thereafter, with tau<=e-1. GC476 gives the background gate transport and finite first-black gate. The quantified proof below is copied from GC478; it uses those independently reviewed lemmas, not a finite graph or census.

**Pair variables.** Write candidate diagonal pairs as P_j(s)=D_(e+2j)(x,s), Q_j(s)=D_(e+2j+1)(x,s). For j>=1 their updates, with U=P_(j-1), B=Q_(j-1), are

    P_j(s+1)=U(s) XOR ((1-B(s))*P_j(s)),
    Q_j(s+1)=B(s) XOR ((1-P_j(s))*Q_j(s)).

Define the marker M_j=(1-P_j)*Q_j, which means the pair is01. Direct binary algebra gives the key identity

    M_j(s+1)=(1-U(s))*(B(s) XOR M_j(s))
              =M_(j-1)(s) XOR ((1-P_(j-1)(s))*M_j(s)).

If U=1, the next marker is zero. If the input pair is01 and the current marker is zero, the output pair is01: Pnext=0, Mnext=1. This is a clearing pulse followed by a front, not a statement about the candidate's literal first black cell.

**Clearing-front propagation lemma.** Suppose an input pair has a time t with Pprev(t)=1, has Mprev(s)=0 for t<=s<T, and is01 at time T>t. Then the output pair has some clearing witness t' in{t,t+1}, has P(t')=1 and M(s)=0 for t'<=s<T+1, and is01 at T+1.

Proof: choose t'=t if P(t)=1, and t'=t+1 otherwise. In the latter case the first update has P(t+1)=1 because U(t)=1 and P(t)=0. In either case M(t')=0. Since U(t)=1, M(t+1)=0 independently of all prior values. From t+1 through T-1 the input marker vanishes, so Mnext=(1-U)*M preserves zero. Thus M(T)=0. At T the input pair is01, so the next output pair is01. The same argument proves every asserted intermediate zero; no unmentioned initial-tail restriction is used.

**Base front and induction.** Let e be a first even initial deviation from G65, and tau the preceding odd diagonal's first black time. GC472 gives P_0(s)=1 through tau and0 afterwards. At s=tau its own next odd update resets Q_0(tau+1)=b(tau)=1. Thus pair0 has a clearing witness t_0=tau, marker zero through tau, and is01 at T_0=tau+1. Iterating the propagation lemma yields, for every j, a witness t_j<=tau+j with P_j(t_j)=1, marker zero from t_j through T_j-1, and pair01 at

    T_j=tau+j+1.

This candidate front statement alone holds for arbitrary later suffixes; it does not yet identify their background errors.

**Identification with the parity background.** Let w be the first initially black odd background gate: A_j(0)=0 for j<w and A_w(0)=1, where A_j=D_(e+2j+1)(y). GC476 proves that A_j stays at its initial value through tau+j and flips at T_j. Hence A_j(T_j)=1 for j<w and A_w(T_w)=0. Every background even diagonal is white.

For j=0, after T_0 the candidate first even diagonal is zero, and candidate/background odd diagonals accumulate the same b. Their error is therefore constant, equal to A_0(0). Induct on j<=w. When j>0, the preceding pair is a passing gate and already equals the background from T_(j-1) onwards. At T_j the candidate pair is01. If j<w this agrees with the background pair01; thereafter both obey the same recurrence and remain equal, with P_j=0. If j=w the background pair is00, so the odd error is1. The preceding even input is zero forever; the current P_w stays zero and both odd tracks accumulate the same preceding odd input. The error remains1 forever. Thus, for every j<=w and every s>=T_j,

    P_j(s)=0,  Q_j(s) XOR A_j(s)=A_j(0).

This is stronger than the tested tau+1+2j settling bound. Its proof covers tau0, w0 and arbitrary later b histories.

**Clock consequence and finite-left exclusion.** Since tau<=e-1, T_j<=e+j<=e+2j+1, and for j>=1 also T_j<=e+2j. All earlier clocks agree by first-difference locality. The first even pulse passes its own clock; every later even clock up to e+2w is white, and every odd clock before e+2w+1 passes. At e+2w+1 the frozen error is1, so that clock fails, regardless of every subsequent initial bit. This proves the exact2w life law.

For any finite odd-supported initial-left row, G65's parity background has R_0 beyond its left radius, so GC476 proves w is finite for every even e. An alternative full0101 member has a first right difference. An odd first difference is impossible by GC472; an even first difference now fails at a later odd clock. Hence the G65 background is the unique full0101 realization of that left row. G27.3 proves that any full0101 left system has initial ones only at odd depths, so all finite initial-left rows are covered. G65's right seed is infinite beyond the left radius; therefore no finite global initial seed has a full0101 centre clock. No assumption of near-wall periodicity, fixed radius or tail truncation enters this conclusion.

**Predictions and controls.** Before running, predict the sharper front/settling times on GC477's abstract cases. The initial sharpened query found no failure. After deriving the clearing-marker identity and witnesses, check all16 input/output pair choices by literal decimal Rule210 and each constructed witness on all10880 abstract cases:40064 front witnesses pass, as do the sharper settling values. Unexpected: the first failing background gate also has the candidate01 front; it fails by its error, not by absence of a front. Omitting the clearing premise fails: input01 with target01 outputs00, not01. Reproduction: `tests/probes/lexicon/rule210_gpt_clearing_front.py`. These are proof controls, not a substitute for the quantified propagation lemma. GC477's earlier indexing failure remains retained.

*Independent reading (Local L285).* Pair updates, marker identity, clearing-witness interval, base and identification all checked by hand. G27.3 uses only the left wall equation, so arbitrary right continuations do not escape its odd-support premise. The separate FR instrument checks235892 actual-orbit tail cases, with sharp settling; these finite controls are evidence about the instrument, not replacements for the induction.


### 33. Proposition 20 (proved by hand, second-read): a checkerboard fringe on the right edge is invisible, so infinitely many finite seeds share the single cell's pattern



*Status:* second-read by GPT (GC641, 2026-10-09); promoted from the waiting room by Local (L351). Waiting-room heading: "33. Proposition 20 (proved by hand; waiting room, second reader wanted): a checkerboard fringe on the right edge is invisible, so infinitely many finite seeds share the single cell's pattern". Not a prize claim.
*Provenance:* Cloud, 2026-10-09 (00:43 BST), from the owner's question "if the centre column was an encrypted message,
not just random but encoding information, how might we decrypt it" (CHAT-LEDGER.md CL069). Found by
`tests/probes/lexicon/rule30_cloud_equivalent_seeds.c`, an exploratory scan with no prediction written first; the proof
was written afterwards.

**Proposition 20.** For $r \ge 1$ let $S_r$ be the seed with black cells $0$ and $r$ and cells $1, \dots, r-1$
alternating white, black, white, … ($S_1 = 11$, $S_2 = 101$, $S_3 = 1011$, $S_4 = 10101$; $S_r = 1(01)^{r/2}$ for even
$r$, $1(01)^{(r-1)/2}1$ for odd $r$). At every time $t \ge 0$ and every cell $x \le t - 1$, Rule 30 from $S_r$ has
the same colour as Rule 30 from the single black cell. In particular the two have the same centre column.

**Proof.** Write $D_k(t) = x_t(t - k)$, the diagonal $k$ cells in from the line $x = t$. Rule 30 at cell $t + 1 - k$
reads $D_k(t+1) = D_k(t) \oplus (D_{k-1}(t) \lor D_{k-2}(t))$, with $D_k(0) = x_0(-k)$. For the single cell,
$D_k \equiv 0$ for $k < 0$ and $D_0 \equiv 1$, so $D_1(t) = t \bmod 2$. For $S_r$, $D_k \equiv 0$ for $k < -r$ and
$D_{-r} \equiv 1$. Every $D_k$ with $-r < k \le 0$ flips at each step. $D_{-r+1}$ sees $1 \lor 0$ and $D_{-r+2}$ sees
$D_{-r+1} \lor 1$. For $k \ge -r + 3$, $D_{k-1}$ and $D_{k-2}$ both flip and start at the adjacent cells
$x_0(1-k) \ne x_0(2-k)$ of the alternating stretch $1, \dots, r-1$. So they stay in opposite phase and their OR is $1$.
Hence $D_0(t) = (t + 1) \bmod 2$. For $k = 1$, $D_0 \lor D_{-1} \equiv 1$ in $S_r$: if $r = 1$, $D_{-1} \equiv 1$; if
$r \ge 2$, $D_{-1}$ flips from $x_0(1) = 0$, opposite to $D_0$. The single cell's OR is $1 \lor 0$, and both
$D_1(0) = 0$, so $D_1$ agrees. For $k = 2$, $D_1 \lor D_0 = (t \bmod 2) \lor ((t+1) \bmod 2) \equiv 1$ in $S_r$, and
$D_1 \lor 1$ in the single cell. $D_2(0) = 0$ in both, so $D_2$ agrees. For $k \ge 3$ both inputs agree and
$D_k(0) = 0$ in both, so $D_k$ agrees by induction. Every cell $x \le t - 1$ lies on a diagonal $k = t - x \ge 1$. ∎

**What the computation adds (exploratory).** The scan decrypts the single cell's centre column under every right half
$x_0(1..W)$. The column is an autokey cipher of the left half keyed by the right half, so the left half is the unique
plaintext. At $T = 400$ the right halves whose plaintext has no black deeper than $200$ are, for $W = 12$ and
$W = 16$, exactly the $S_r$ with $r \le W$ and the single cell itself (13 and 17 of 4,096 and 65,536). Joint cycle
detection on the closed right-edge diagonals confirmed $S_1$ to $S_7$ for ever, in a scratch check. Open: whether a
wider right half, or a finite left half deeper than $200$, also gives the single cell's column.

**Reading.** The centre column does not determine its finite seed, and the OR is the mechanism. The fringe flips
every cell it touches, and its two innermost diagonals are in opposite phase, so the OR that would carry it inward is
already $1$. Compare §8.19: a second seed $d$ cells to the right leaks inward at about $0.28$ cells per step and
reaches the centre after $2.3$ to $2.9\,d$ steps. This fringe leaks at speed zero. It is the smallest case of
Meier and Staffelbach's observation that many right halves are equivalent (PRIOR-ART.md). The prize problems ask
about the single cell's centre column, which every $S_r$ shares. Prior art: none found in a bounded search; likely
folklore of the right-edge diagonals (Jen).

*Independent reading (GPT GC641, 2026-10-09).* Verified by hand: the diagonal update reads left, centre and right inputs D_k, D_(k-1), D_(k-2) in the correct orientation; the fringe's diagonals through D_0 toggle with adjacent ones in opposite phase, the first two after the outermost covered by its fixed black input (r = 1 and 2 included); D_1 and D_2 agree, and the induction gives agreement for every k >= 1 and t; the centre at t = 0 is black in both. *Scoped extension (GC641; read by Local L351).* The same proof covers any common initial left half, finite or infinite, with x_0(0) = 1 and x_0(-1) = 0: the diagonals k <= 0 read only cells x >= 0, D_1 starts at the common 0 and toggles in both histories, and D_2 and deeper start equal and stay equal. The nearest-left guard is essential: with a common black cell at -1, the base {-1, 0} and the fringed {-1, 0, 1} have first rows {-2, -1, 1} and {-2, -1, 2} and centres 0 and 1 at time 2. Local replayed the extension on 600 random common left halves with x_0(-1) = 0 and r up to 9, for 80 steps (7.29 million cells at x <= t - 1, no disagreement), and found the centre columns differing in all 600 cases once x_0(-1) = 1.

### 34. Proposition 21 (proved by hand, second-read): a seed sharing the single cell's centre column begins its left half exactly where its right half alone fails

*Status:* second-read by Local (L370, 2026-10-09); promoted from the waiting room by Local (L370). Waiting-room heading: "34. Proposition 21 (proved by hand; waiting room, second reader wanted): a seed sharing the single cell's centre column begins its left half exactly where its right half alone fails". Not a prize claim.
*Provenance:* Cloud, 2026-10-09 (05:48 BST), pushing on Proposition 20's open converse at the owner's request.
Stated as Lemma U1 in `tests/probes/lexicon/rule30_cloud_fringe_uniqueness.py`, whose predictions were pushed in
8327e7c before its full run, and checked there on every right half of up to 16 cells.

**Proposition 21.** For a right half $R = x_0(1..w)$ let $\tau(R)$ be the first time the centre column of
$(\text{white}, 1, R)$ differs from the single cell's, with $\tau(R) = \infty$ if it never does. Let $X = (L, 1, R)$
be a finite seed whose centre column is the single cell's. Then either $L$ is white and $\tau(R) = \infty$, or the
shallowest black of $L$ is at depth exactly $\tau(R) < \infty$. In particular, (a) the single cell is the only
finite seed with a white right half and this column, and (b) a seed with this column whose right half is a fringe
$S_r$ (Proposition 20) has a white left half.

**Proof.** Put $Y = (\text{white}, 1, R)$. If $L$ is white then $X = Y$, and $\tau(R) = \infty$. Otherwise let $b$
be the depth of the shallowest black of $L$. The rows $X$ and $Y$ differ only at cells $\le -b$, and the rightmost
difference is at $-b$. Rule 30 is left-permutive: if two rows agree at every cell $> i$ and differ at $i$, the next
rows agree at every cell $> i + 1$ and differ at $i + 1$, because $x'(i+1) = x(i) \oplus (x(i+1) \lor x(i+2))$ and
the inputs of the OR agree. So at time $t$ the rightmost difference is exactly at $-b + t$, and the centre columns
of $X$ and $Y$ agree for $t < b$ and differ at $t = b$. As $X$ has the single cell's column, $Y$'s column agrees with
it before $b$ and differs at $b$, so $\tau(R) = b$. For (a), $(\text{white}, 1, \text{white})$ is the single cell, so
$\tau = \infty$ and $L$ is white. For (b), $\tau(S_r) = \infty$ by Proposition 20. ∎

**What the scans add (computer-assisted).** Proposition 21 splits the converse into two finite questions. Both
were answered with predictions pushed first (`rule30_cloud_fringe_uniqueness.py`, `fringe_uniqueness.c`):
- *Empty left half.* For every exact width $w \le 28$, the only right half with $\tau(R) \ge 3000$ is $S_w$ (EQ1
  held). The longest any other right half keeps the column is 476 steps.
- *Any left half.* For right halves of up to 20 cells, no left half of depth $\le 1000$ gives a finite seed with this
  column outside the family (EQ3 held). For up to 28 cells and depth $\le 200$ the same follows from EQ1 and
  Proposition 21. The registered decryption test of this case (EQ2) was refuted as worded: its window of 240 steps
  was shorter than the longest $\tau(R)$. A post-hoc rerun, with no prediction, used a window of 540 steps, longer
  than every $\tau(R)$ found. It left exactly the 29 keys of the family to depth 500 at widths up to 28.
- *Conjecture (open).* The single cell and the $S_r$ are the only finite seeds with the single cell's centre column.
  Wider right halves and deeper left halves are not covered.

*Independent reading (Local L370, 2026-10-09).* Verified by hand: if two rows agree at every cell $> i$ and differ at $i$, the next rows agree at every cell $> i + 1$ (each such update reads only cells $> i$) and differ at $i + 1$ (its OR inputs agree and $x(i)$ differs). So the rightmost difference of $X$ and $Y$ sits at $-b + t$, reaches the centre exactly at $t = b$, and $\tau(R) = b$ because $X$ carries the single cell's column; (a) and (b) follow as stated. The argument uses neither the finiteness of $L$ nor that of $R$, only that $L$ has a shallowest black. Literal check of the lemma: for every third right half of up to 9 cells and every nonwhite left half of depth up to 11, the first centre-column difference between $(L, 1, R)$ and $(\text{white}, 1, R)$ within 48 steps is at exactly the shallowest black's depth (350,037 pairs, no exception). Scope: the proposition fixes where a nonwhite left half must begin, not whether one exists, so the completeness conjecture stays open. Near-entry check, made late (L371; `proof_dupes.py --near 34`): the three nearest older entries are 33, 29 and 06. Entry 34 uses 33 for its corollary (b) and restates none of them (29 is Rule 210's empty-left uniqueness, 06 is Theorem B on zero runs).


### 35. Proposition 22 (proved by hand, second-read): a row that turns faster than light is periodic, and every window turns leftwards

*Status:* second-read by Local (L375, 2026-10-09); promoted from the waiting room by Local (L375). Waiting-room heading: "35. Proposition 22 (proved by hand; waiting room, second reader wanted): a row that turns faster than light is periodic, and every window turns leftwards". Elementary; Boyle and Lee (arXiv:math/0607178, Remark 2.1) describe
the same kind of count for permutive directions, so it is not claimed new. Not a prize claim.
*Provenance:* Cloud, 2026-10-09 (08:12 BST), from the owner's questions after CL071 (which surfaces carry a ring's
history; "a unit vector in a space-time picture is a velocity"). Part (b) was noticed in a disclosed smoke test of
`tests/probes/lexicon/rule30_cloud_turning_rings.py` before it was proved, and checked in the full run, whose
predictions were pushed in dedbe55.

Write $F$ for Rule 30, $F(x)(i) = x(i-1) \oplus (x(i) \lor x(i+1))$, and $\sigma$ for the shift,
$(\sigma^s x)(i) = x(i - s)$, so $s > 0$ moves a pattern right. Call $x \in \{0,1\}^{\mathbb{Z}}$ a *turning row*
with vector $(s, p)$ if $F^p x = \sigma^s x$: its space-time is constant along $(s, p)$.

**Proposition 22.** Let $p \ge 1$ and $|s| > p$.
(a) Every turning row with vector $(s, p)$ is spatially periodic, and there are finitely many. They are exactly the
periodic points of a map $T$ on the $2^{|s| + p}$ words of $|s| + p$ cells, and the least period of the row is the
length of its window's cycle.
(b) If $s < -p$, $T$ is a bijection, so there are exactly $2^{|s| + p}$ turning rows with vector $(s, p)$: every
word of $|s| + p$ cells extends to exactly one row that moves left $|s|$ cells every $p$ steps.

**Proof.** (a) $F^p(x)(i)$ depends only on $x(i-p), \dots, x(i+p)$; write it $G(x(i-p), \dots, x(i+p))$. Suppose
$s > p$. The relation says $x(i - s) = G(x(i-p), \dots, x(i+p))$, and the cell $i - s$ lies outside that window.
Putting $m = i - s$, $x(m) = G(x(m+s-p), \dots, x(m+s+p))$. So the window $W_m = x(m+1), \dots, x(m+s+p)$ fixes
$x(m)$, hence $W_{m-1} = T(W_m)$ for a map $T$ on words of $s + p$ cells. For every $j \ge 0$, $W_m = T^j(W_{m+j})$
lies in the image of $T^j$. On a finite set these images decrease to the set of periodic points of $T$, on which $T$
is a bijection. So every $W_m$ is $T$-periodic, $(W_m)$ is periodic in $m$, and so is $x$, with least period the
length of $W_0$'s cycle (each window fixes the row). Conversely, a $T$-cycle read off cell by cell gives a row
satisfying the relation at every site. If $s < -p$ the same argument runs rightwards, with $x(n)$ fixed by the
$|s| + p$ cells to its left.
(b) Rule 30 is left-permutive, and so is $F^p$: $F^p(x)(i) = x(i-p) \oplus H(x(i-p+1), \dots, x(i+p))$. Put
$j = -s > p$. Moving right, $T$ drops the window's leftmost cell $x(n-j-p)$ and appends
$x(n) = x(n-j-p) \oplus H(x(n-j-p+1), \dots, x(n-j+p))$. Every argument of $H$ is still in the new window, because
$n - j + p \le n - 1$. So the dropped cell is recovered from the new window, $T$ is injective, and on a finite set it
is a bijection. Every word is periodic, and (a) gives the count. ∎

*Remarks.* Part (a) uses only that the rule has radius one. For $s > p$, $T$ drops the rightmost cell, which Rule 30
reads through the OR, and $T$ is not injective: the census finds such rows about as rare as a random map's cycles
(from 4 times more at $p = 1$ to as many at $p = 3$). GC686's all-S ring (CL071: $F x = \sigma^{14} x$ on its own ring
of 84 cells, which is also $\sigma^{-70}$) is a turning row of both kinds.
*Computer check* (`rule30_cloud_turning_rings.py`, `turning_rings.c`). For $p \le 3$ and $|s| + p \le 28$, every
row found satisfies its relation directly. On every ring of period up to 20 the census agrees with brute force over
all rings. For every $s < -p$ all $2^{|s|+p}$ words are periodic.
*Corollary, by composition with GPT's results (conditional on GC687's exhaustive certificate).* A turning row with
$s \ne 0$ whose columns 0 and 1 are the all-S pair (the wall $0101\ldots$ and $110100$ repeated, in marker form) is
a rotation of GC686's ring. Reason: columns 0 and 1 have period 6, so every column to the left does (GC704's
propagation); column $i + s$ is column $i$ delayed by $p$ steps, so every column has period 6. GC688 then fixes the
entrance, GC687 the right half and L372's decoding the left half. The census agrees: in its whole range the only
turning row with an alternating column at all is GC686's ring.

*Independent reading (Local L375, 2026-10-09).* Verified by hand. (a) With $m = i - s$ and $s > p$, the window $x(m+s-p), \dots, x(m+s+p)$ lies inside $W_m = x(m+1), \dots, x(m+s+p)$ because $s - p \ge 1$, so $W_{m-1} = T(W_m)$; $W_m$ lies in every image $T^j$, hence among $T$'s periodic points, where $T$ is a bijection, so the windows cycle both ways and the row is periodic with least period the cycle length. (b) $F^p$ stays left-permutive under composition, and with $j = -s > p$ the arguments of $H$ end at $n - j + p \le n - 1$, inside the new window, so the dropped cell is recovered and $T$ is injective. The corollary's step "column $i + s$ is column $i$ delayed by $p$" reads $x_{t+p}(i) = x_t(i - s)$ correctly, and it carries period 6 from the left columns to every column. Near-entry check first (`proof_dupes.py --near 35`): entries 25, 05 and 07, a pulse-weight proposition and Theorems A and A′; none is restated. The census and GC687 were not replayed here.


*Correction to the corollary's wording (Cloud, 2026-10-09, at GPT's request in GC725).* The corollary assumes
$|s| > p$ as well as $s \ne 0$: its reason uses part (a)'s spatial period. GPT's GC727 (hand proof, read by Cloud in
CL073) extends part (a) to every $s \ne p$: for $s < p$, $x(m) = x(m + p - s) \oplus H(x(m+1), \dots, x(m+2p))$
fixes each cell from cells strictly to its right. With it, the corollary holds for every direction except
$s = p$.

### 36. Proposition 23 (proved by hand, second-read): the triangles on the single cell's right edge are a ruler sequence

*Status:* second-read by GPT (GC730, 2026-10-09); promoted from the waiting room by Local (L377). Waiting-room heading: "36. Proposition 23 (proved by hand; waiting room, second reader wanted): the triangles on the single cell's right edge are a ruler sequence". Not a prize claim. Not found in the record or in a short search; the
periods it uses are Rowland's and OEIS A094605, and the widest edge triangles were seen in §8.68.
*Provenance:* Cloud, 2026-10-09 (08:43 BST), from the owner's observation that the rightmost triangles touch the
pyramid's right edge at linearly spaced points and differ only in size. Checked by the exploratory probe
`tests/probes/lexicon/rule30_cloud_edge_triangles.py` (no prediction pushed first).

In the single cell's history let $D_j(t) = x_t(t - j)$ be the $j$-th right diagonal, so $D_0$ is the edge. By §8.27,
every $D_j$ is purely periodic, with a period $p_j$ that is a power of 2 ($p_0 = 1$): $D_j$ is the running XOR of
$g_j = D_{j-1} \lor D_{j-2}$ from $D_j(0) = 0$, and if $q_j$ is the period of $g_j$ then $p_j = q_j$ when one period
of $g_j$ holds an even number of 1s and $p_j = 2q_j$ when it holds an odd number. The periods are OEIS A094605:
$1, 2, 2, 4, 8, 8, 16, 32, 32, 64, \dots$

**Proposition 23.** For $t \ge 1$ let $L(t)$ be the number of white cells at time $t$ that run leftwards from
cell $t - 1$, just inside the black edge cell $t$. Then
```math
L(t) = \min\{\, j \ge 1 : p_j \nmid t \,\} - 1 .
```
So $L(t) = 0$ for odd $t$, and for $t = 2^v m$ with $m$ odd, $L(t) = w(v) = \min\{j \ge 1 : p_j > 2^v\} - 1$,
which depends only on $v$. At every even $t$ this run is the top row of a white triangle, one cell inside the edge.
So one triangle touches the right edge every two steps, and its width is a ruler sequence:
$w = 2, 3, 5, 6, 8, 14, 15, 23, 24, 26, 28, \dots$ for $v = 1, 2, 3, \dots$

**Proof.** Let $j$ be the least index $\ge 1$ with $p_j \nmid t$; it exists because the periods are unbounded
(§8.27). For $1 \le i < j$, $p_i \mid t$, so $D_i(t) = D_i(0) = 0$: cells $t - 1, \dots, t - j + 1$ are white. Now
$q_j$ divides the least common multiple of the periods of $D_{j-1}$ and $D_{j-2}$ (the white side $D_{-1}$ has
period 1), and both divide $t$, so $q_j \mid t$. As $p_j \nmid t$, $p_j \ne q_j$, so $p_j = 2q_j$, one period of
$g_j$ holds an odd number of 1s, and $D_j(s + q_j) = D_j(s) \oplus 1$ for every $s$. Since $q_j \mid t$ and
$2q_j \nmid t$, $t \equiv q_j \pmod{2q_j}$, so $D_j(t) = D_j(q_j) = D_j(0) \oplus 1 = 1$: cell $t - j$ is black.
Hence $L(t) = j - 1$. Each $p_i$ is a power of 2, so $p_i \mid t$ exactly when $p_i \le 2^v$, which gives the form
in $v$. For odd $t$, $p_1 = 2 \nmid t$, so $L(t) = 0$. For even $t$, $p_1 = p_2 = 2$ divide $t$, so $L(t) \ge 2$. The
run is a triangle's top row: the row above, $t - 1$, is black at cell $t - 2$ ($D_1(t-1) = 1$), so the run is not
the shrunken continuation of a white run above it. ∎

*Remarks.* The widest triangles of the whole cone sit on the edge at the times $m \cdot 2^k$ (§8.68); this is why,
and their width is $w(v_2(t))$ exactly. The layers $[L(t) \ge k]$ are periodic with doubling periods, the nesting of
a hierarchical tiling (§8.72). *Computer check:* for every even $t < 2^{24}$ the width depends only on $v_2(t)$ and
equals the formula wherever the periods are known ($v \le 21$); a direct simulation agrees at every $t < 4096$.

*Independent reading (GPT GC730, 2026-10-09).* Near-entry gate first (05, 33, 06, read in full; no restatement). Verified by hand: the first index whose period does not divide $t$ has a driver period dividing $t$, so its period must double, and the half-period flip makes the first black diagonal while every earlier diagonal is white; power-of-two divisibility gives the ruler dependence; the preceding odd row's black cell $t - 2$ stops the even run being a shrunken triangle from above. The exploratory census, the numerical period list and novelty were not verified. Local re-ran the gate at promotion (05, 33, 06).

### 37. Period 1 (Condrey's theorem, proved again by hand, second-read): no finite seed has an eventually constant column

*Status:* Cloud's proof (RULE30-PRIZE.md §8.76, CL083, 2026-10-09), second-read by Local (chat L417, 2026-10-09). Not
new and not a prize claim: it restates Condrey's theorem (arXiv:2609.09431; PRIOR-ART.md), which the record had cited
but not audited in full (PRIOR-ART.md 2026-10-04, GPT's G11, §5's check A). Filed at the owner's request, through the
near-entry gate.

**Theorem (Condrey).** No nonzero finite configuration of Rule 30 has an eventually constant column.

**Proof.** Rule 30 read for its left input is $x_t(i-1) = x_{t+1}(i) \oplus (x_t(i) \lor x_t(i+1))$, so columns 0 and
1 over $t \ge s$ fix every column to their left over $t \ge s$.
*Edges.* If $E$ is the rightmost black cell of row $t$, cell $E + 1$ of row $t + 1$ is $1 \oplus 0 = 1$ and every
cell beyond it is 0, so the rightmost black cell moves one cell right each step. At the leftmost black cell $L$,
cell $L - 1$ becomes $0 \oplus (0 \lor 1) = 1$ and nothing further left is black. So a finite nonzero row stays
finite and nonzero, and a time shift keeps the hypothesis. By shift invariance take column 0 equal to $c$ for every
$t \ge 0$.
*Black wall, $c = 1$.* $x_t(-1) = 1 \oplus (1 \lor x_t(1)) = 0$ whatever column 1 is. For $j \ge 2$ the left-input
form gives $0 \oplus (0 \lor 1) = 1$ at even $j$ and $1 \oplus (1 \lor 0) = 0$ at odd $j$, by induction on $j$, at
every $t \ge 0$. Row 0 then has infinitely many black cells, a contradiction.
*White wall, $c = 0$.* If every black cell of row 0 lay at a site $\le 0$, its rightmost one $E_0 \le -1$ would
reach column 0 at time $-E_0$. So some black cell lies at a site $\ge 1$. Let $a_t$ be the leftmost one. While
$a_t \ge 2$, sites $1, \dots, a_t - 2$ stay white ($0 \oplus 0$, column 0 being white) and site $a_t - 1$ turns black
($0 \oplus (0 \lor 1)$), so $a_{t+1} = a_t - 1$. Column 1 is black at $t_1 = a_0 - 1$, and
$x_{t+1}(1) = 0 \oplus (x_t(1) \lor x_t(2)) \ge x_t(1)$ keeps it black. From $t_1$ on, columns 0 and 1 read white,
black, so $x_t(-1) = 0 \oplus (0 \lor 1) = 1$, $x_t(-2) = 1 \oplus (1 \lor 0) = 0$, and the same induction makes
every odd depth black. Row $t_1$ is then infinite, a contradiction. ∎

*Remark (§8.76).* The white wall's case is the only place the real right half enters (the latch at column 1). With
an arbitrary column 1, as in LR, a white column 1 beside a white wall forces a white left half, so period 1 fails in
that setting. That is why LR starts at period 2.

*Independent reading (Local L417, 2026-10-09).* Near-entry gate first (`proof_dupes.py --near 37`): 05, 06 and 10,
read in full. 05 (Jen's theorem with a clock) needs two periodic columns; 37's last step is its period-1 case once
the latch has made column 1 constant, and the one-column hypothesis and the latch are what 37 adds. 06 bounds zero
runs under two periodic columns, and 10 is the window principle. None is restated. Verified by hand, on the three points CL083 asked to be
attacked.
- The time shift keeps both edges. Each edge's black cell spreads one site outwards per step, so a finite nonzero row
  stays finite and nonzero.
- Step 3: column 0 is white at time 0, so $E_0 \le -1$ and the contradiction time $-E_0 \ge 1$ lies in the range.
- Step 4's induction includes the boundary cases. At $a_t = 2$ the run $1, \dots, a_t - 2$ is empty. When
  $a_t - 2 = 0$, site $a_t - 1$'s left input is column 0, white by hypothesis.
- Both checkerboard inductions start at the right depths (column 0 counted as depth 0).
- The remark is correct: a white column 1 beside a white wall gives $0 \oplus 0 = 0$ at every depth.

*Formalized (Local, 2026-10-09).* For the single seed, the theorem is machine-checked in Lean 4 against Google
DeepMind's `FormalConjectures/Other/Rule30.lean` definitions. `tests/probes/lean/Rule30Period1.lean` proves
`centerColumn_not_eventually_constant` and the period-1 instance of `Rule30.lean`'s Problem 1 statement
(`¬ ∃ N, ∀ t ≥ N, centerColumn (t + 1) = centerColumn t`). It uses only the standard axioms; `#print axioms` shows no
`sorryAx`. The route avoids the leftmost-black-cell walk:
- an eventually constant column 0 that is never white together with column 1 forces a checkerboard left half,
  which finite support forbids;
- with a white wall, either column 1 turns black once and the latch keeps it there (back to the first case), or
  every column to the right stays white, which the right edge forbids.
- Cloud's scratch machine checks were not replayed.

*Additional independent reading (GPT, GC789, 2026-10-09).* Entry37 passes by hand. The near-entry gate gives05,
06 and10, all read in full; the earlier virtual audit also read18 and17, and the checkerboard/latch components
C1/C2 were explicitly checked. This is the complete one-column constant theorem, credited to Condrey, combining
known components; no new result or duplicate filing. The all-white seed stays white and verifies why the nonzero
hypothesis is essential. At first right black site1, the latch time is0; at site2 the pre-latch white interval is
empty and the update uses the white wall as its left parent. Infinite time in the inverse induction supplies
every needed next-time sample. Cloud's measured scratch controls were not replayed. The original source's
period-2 necessity comment was qualified; the theorem and this filed proof are unchanged.

### 38. The black-end walls (computed and proved, second-read): no finite seed has a column eventually reading 0 1^q for q = 7 or any q >= 9

*Status:* second-read both ways. GPT's GC806 lemma was second-read by hand by Local (chat L430). The logic of
Local's two certificates was read by GPT (GC807 for SG, GC809 for WT); GPT did not rerun the enumerations. Filed by
Local at GPT's request (GC809), 2026-10-09.
*Provenance:* the claim and the strip-graph method are from an external agent-run repository,
cochon123/rule30-prize, pinned at 3915b39 (`research/strip_graph.py`, `research/isolated_zero_uniform.md`). There
it was unverified and its uniform proof had a gap. This entry is its replication and repair, not an independent
discovery.
- GPT read the source without running it (GC805): the relaxation is sound, and its Lemma F does not follow.
- GPT repaired the uniform step (GC806).
- Local reimplemented the finite cases from GC805's specification alone (`rule30_isolated_zero_strip.py`, SG, L429)
  and computed the wrap table (`rule30_isolated_zero_wrap.py`, WT, L431). Both had predictions pushed first, and
  both are exhaustive and take seconds.
Not a prize claim: period 2 (q = 1) is not touched.

**Theorem.** Let q = 7 or q >= 9. No nonzero finite configuration of Rule 30 has a column that is eventually
periodic with the period word $0\,1^q$ (one white tick, then q black ticks).

**Proof.** Suppose one does. Shift it to column 0. Number the phases 0 .. q with phase 0 the white tick, and start
the clock at a time from which column 0 follows the word.

*The strip.* From that time on, the cells on positions -6 .. 6 form an infinite path in a finite graph.
- The vertices are (row on -6 .. 6, phase), with centre 0 at phase 0 and 1 otherwise.
- An edge applies $x'(i) = x(i-1) \oplus (x(i) \lor x(i+1))$ exactly on -5 .. 5, leaves the two outer cells free,
  and advances the phase.
- An infinite path in a finite graph ends in one cyclic strongly connected component. Inside a component of period
  P, every edge advances the BFS class by one modulo P.
- So if column -1 (or +1) has one value on each class, that column is eventually periodic along every path.

*Finite cases, q = 7 and 9 <= q <= 16 (SG).* Each of these graphs has exactly one cyclic component. Its period is
q + 1, and column -1 has one value on each class. The component has 218 vertices at q = 7 and 14q + 74 for q >= 9.

*Every q >= 17 (GC806 and WT).*
1. Ten consecutive 1-ticks at column 0 force columns +1, +2 to 01 within nine updates, whatever enters at +6, and
   01 then persists while the centre stays 1. Write b .. f for columns +1 .. +5 and z for +6.
   - From b = 1, one update gives the pair 01 or 00.
   - From 00 with d = 1, two updates give b, c, d = 000.
   - From 000 with e = 0, two updates give 01.
   - From b, c, d, e = 0001, the prefixes run 1011, 0010, 1 1 1 e_3, 0 0 0 e_4. Here e_3 = NOT f_2 and
     f_3 = f_2 OR z_2, so e_4 = 1 xor (e_3 OR f_3) = 0, and two more updates give 01.
   - The bound is 9, attained (all 32 x 512 boundary paths checked).
2. Seven consecutive 1-ticks force columns -6 .. 0 to 1010101 by the left inversion; depth j needs j + 1 ticks.
   With q >= 17, every row at phases 11 .. q - 6 therefore has the prefix (columns -6 .. +2) 101010101.
   - At those phases the pair 01 held the tick before, so $d' = \lnot(d \lor e)$. Then d' = e' = 1 forces f = 1 and
     f' = 1, and the suffix (columns +3 .. +6) is neither 1100 nor 1101.
   - So these rows lie in C, a set of 14 rows.
3. At phase q, column -1 = 0 xor (1 OR x(1)) = 1 and columns +1, +2 = 01, so the prefix is one of the 32 words
   h + 1101.
   - Following every strip path from each of these 32 x 16 rows through phase 0 and phases 1 .. 11, only prefix
     110001101 can reach C at phase 11 (WT, exhaustive).
   - Its column -2 is 0, so at the next phase 0, column -1 = 0 xor (1 OR 1) = 1.
   - At phases 1 .. q - 1, column -1 = 1 xor 1 = 0, and at phase q it is 1.
   - So column -1 is eventually periodic with period q + 1.

*The contradiction.* Columns -1 and 0 are then periodic with periods dividing their lcm, on an unbounded window.
Jen's theorem with a clock (entry 5) forbids this for a nonzero finite configuration. ∎

*Remarks.*
- The method certifies nothing at q = 1 .. 6 or 8: each graph has a component forcing neither neighbour. At q = 1
  that component is the 84-ring's strip.
- Radius-7 and radius-8 strips certify none of those cases either (`rule30_isolated_zero_wide.py`, L433).
- Exact ring models, whose column reads 0 1^q, exist for q = 1, 2, 3, 4 and 6, on rings of 7, 12, 7, 15 and 15 cells.
- Post hoc, the single-component shape persists to q = 40.
- The theorem is a statement about finite seeds. Rings are not excluded.

*Near-entry gate (Local, at filing).* `proof_dupes.py --near 38` gives 37, 17 and 06, read in full. 37 is period 1
(the constant walls), and 17 is Jen's theorem in the record's form; entry 38 uses entry 5's clocked version of
it only as its last step. 06 bounds zero runs. None is restated. The hard checks pass (272 entries).

*Filed-text audit (GPT GC812, 2026-10-09).* Read entry38 in full after7364e4b7, and ran
`proof_dupes.py --near 38`:37,17,06 read in full, hard checks pass at272 entries. The
filed theorem is the repaired restricted-wall result, not a restatement of any of those
three. It preserves the radius6 relaxation, eventual-onset/phase alignment, SG's finite
range, GC806's nine-update bound and phase11 cruise membership, WT's twelve-update wrap
and the final two-column contradiction. At q17 the cruise window includes phase11 exactly;
this guards the uniform threshold. The numerical certificates remain Local's independently
implemented SG/WT runs, not a GPT rerun. Original external claim/method and repaired proof
are correctly credited; q1..6/q8 and ring models remain outside the conclusion. No change
to the theorem or proof is needed.

*See also (2026-10-09 22:35 BST).* Entry 40's one-sided route reproves this entry for q >= 14, uniformly, and closes the
white end for q >= 10.

*Machine-checked in full (Local, 2026-10-10 06:00 BST, L553).* Every q the entry covers is now machine-checked.
- q >= 14: `black_end` in tests/probes/lean/JenRoute.lean, by the one-sided route.
- q = 7 and 9 .. 13: `black_end_two_sided` in BlackEnd38L.lean, by this entry's two-sided strip with GC951's literal
  stages.
  - The chain from all centre-0 rows, the fixed point's phases and six peel stages are literals.
  - Each inclusion between consecutive stages is its own kernel check, and so is each final colConst.
  - The peeled sets reproduce SG's component sizes (218, and 14q + 74).
- The file is generated by tests/probes/lean/gen_black_end38.py from tests/probes/lean/BlackEnd38base.lean. It is
  1.3 MB of literals, so it is not kept in git; sha256 8a07be2115811fc3.
- The axioms are propext, Classical.choice and Quot.sound. The build takes 456 s and peaks at 1.46 GB.

### 39. Every rooted walk returns (proved by hand, second-read, machine-checked): at every period q, the rooted profile walk reaches a zero child

*Status:* proved by hand by Local (chat L487). Second-read by GPT in GC867, which accepted the statement and the proof
structure against the census walk, with "rooted" meaning zero-started; it does not supply G7's physical-root ancestry.
Machine-checked in Lean 4 against Mathlib (tests/probes/lean/RootedReturn.lean, L489; no sorryAx). The compilation is
Local's reported verification; GPT reviewed the source but did not compile it. Filed by Local, 2026-10-09.
*Provenance:* the walk is S84's (G190 .. G198), as censused by RC88, RC16, RW and RWC. GC863 noted that the two-live-
state bound follows from reset uniqueness (G158, G204, R2), and GC864 bounds each first excursion. This entry adds the
termination argument and its formal check.

**Statement.** Fix q >= 1. For q-periodic binary words, call c a child of the pair (x, y) when
c(t + 1) = x(t) XOR (y(t) OR c(t)) for every t modulo q. For every nonzero word c, the walk (0, c) -> (c, c_2) ->
(c_2, c_3) -> ..., taking at each step the unique child of a nonzero driver, reaches a state whose child is 0, that is,
a return. Every rooted walk of S84 starts at such a state (0, c), after its first integration from (a, 0).

**Proof.**
1. A driver y that is black at some tick t0 has exactly one child. At t0 the recursion resets, c(t0 + 1) = NOT x(t0),
   whatever c(t0) is. So running the recursion forward from t0 + 1 determines c uniquely, and the run closes at t0,
   because the reset value is the same. (Lean: `child_unique`, `child_exists`.)
2. The step (x, y) -> (y, c) is injective, because x(t) = c(t + 1) XOR (y(t) OR c(t)). (Lean: `step_injective`.)
3. Suppose the walk never returns. Its states have nonzero drivers and lie in a finite set, so two of them coincide.
   Let s_i = s_j, with i < j and i least.
   - If i >= 2, injectivity gives s_(i-1) = s_(j-1), against the choice of i.
   - So s_1 = (0, c) = s_j. Its first coordinate is the driver of s_(j-1), which is then 0, against the nonzero
     drivers.
   So the walk returns. (Lean: `terminates`, `rooted_walk_returns`.) ∎

*Scope.* No bound on the return depth follows. The measured depths are 88 and 371 at q = 8, 16 depths up to 214,006
at q = 16, and up to 9.1 x 10^9 so far at q = 32. GC865 and GC870 show the counting (2^q - 1 chains, mean length about
2^q on the full primitive domain), which is not a growth law for the rooted sample. This is not a prize claim.

*Near-entry gate (Local, at filing).* `--near 39` gives entries 10, 17 and 37, all at formal similarity 0.19 or
less: different subjects. Nothing is restated. Hard checks pass.

### 40. The Condrey white end (computed and proved, second-read): no finite seed has a column eventually reading 1 0^q for any q >= 10

*Status:* second-read by Cloud (CL110), which checked steps 2 and 3 by hand and replayed step 1 with a third
implementation (`rule30_cloud_white_end_replay.py`, WR). Local's exploratory finding (L498) was replicated before
filing by a separately written implementation (`rule30_white_end_jen.py`, WJ, predictions first). Filed by Local,
2026-10-09.
*Provenance:* the route is the one-hole relaxation of G15-G20, OH and OHC (rule30_one_hole_widths.py), read for column
+1's whole time series rather than its hole bits (L497). The finish is Theorem A (entry 5). The white end was the
PARKED half of the Condrey ends row, with no case closed (§8.62).

**Theorem.** Let q >= 10. No nonzero finite configuration of Rule 30 has a column that is eventually periodic with the
period word 1 0^q (one black tick, then q white ticks).

**Proof.**
1. *The relaxation.* Take the 8 cells right of column 0, x1 .. x8, with an arbitrary outside bit beyond x8 at every
   step. Every actual history restricts to such a path. Let M_q be the period's step relation, one black step and then
   q white steps, with every outside bit. Let S_k be the k-fold image of all 256 states. The S_k decrease, so they
   reach a stable set S in finitely many periods, and an actual state lies in S from some period on.
2. *Column +1 is determined (computed).* For q = 10 .. 40, x1 takes a single value at every tick of the period from
   S: column +1 reads 1 0 0 1^(q-2).
3. *Every q >= 10.* The white relation satisfies W^(n+4) = W^n exactly for n >= 22. So M_q = M_(q-4) for q - 4 >= 22,
   S_q = S_(q-4), and the tick sets R_j = W^j B S agree with q - 4's for j <= q - 4. For j in (q - 4, q] they repeat
   with period 4, since j - 4 >= 22. Induction from q = 37 .. 40 covers every q >= 41.
4. *The contradiction.* Columns 0 and +1 are then both (q + 1)-periodic for ever. Theorem A (entry 5) forbids two
   adjacent columns that are P-periodic on an unbounded window in a configuration with a leftmost black cell. If that
   cell lies right of column 0 at time 0, re-base time: the left edge passes column 0 in finitely many steps. ∎

*Checks.*
- Three implementations agree: the bitmask one (OH's `jen` mode), WJ (row tuples) and Cloud's WR (set-valued
  relations).
- At width 6 no q is determined; at width 12 no q from 2 to 9 is.
- Plain forward simulation of 200 random true right halves for each of q = 10, 12 and 20 ends, every time, in the
  predicted column +1 word (exploratory).

*Remark (the same route at the black end).* At width 8, the walls 0 1^(p-1) have column +1 determined for every
p >= 15 (B^(n+4) = B^n from n = 20). This reproves entry 38's exclusion for q = p - 1 >= 14, uniformly and without
GC806's lemma, but not entry 38's q = 7 or 9 .. 13 (L497).
Machine-checked (Local, 2026-10-10 00:34 BST): `black_end` in tests/probes/lean/JenRoute.lean, for every q = m >= 14.

*Scope.* q = 1 .. 9 at the white end stay open; q = 1 (the word 10) is the period-2 wall itself. Not a prize claim.

*Near-entry gate (Local, at filing).* `--near 40` gives entries 38 (the black end, by the two-sided strip; a different
family, cross-referenced), 37 (period 1) and 03, all read. None is restated. Hard checks pass.


*Additional independent audit (GPT GC880, 2026-10-09 22:37 BST).* Entry40 accepted by hand and by a new integer-set/literal-rule-number certificate, rule30_gpt_white_end_audit.py. All256 width8 states and both outside bits give W22=W26, W21!=W25, singleton phase words1001^(q-2) for q10..29, and stable counts31/21/7 at q10/12/20. Stabilization takes2 or3 strict decreases; q9 retains an undetermined phase. For every q>=30, choose congruent b26..29: the macro/stable set is identical and every white phase j>=22 reduces to r22..25, all contained in b. Actual-path restriction, eventual-onset re-basing and entry5's unbounded-window contradiction independently checked. No replay of q30..40, width6/12 or WC words. Near40 gate passes and38/37/03 read; no new proof entry or prize claim.

*Machine-checked (Local, 2026-10-09 23:34 BST).* tests/probes/lean/WhiteEnd.lean (Lean 4, Mathlib), the whole entry:
- `white_end`: a configuration with a leftmost black cell has no column reading 1 0^q from some time on, for any
  q >= 10. `white_end_finite` is the same for a finite nonzero seed.
- Steps 1 and 2 are kernel `decide`s on 8-cell states encoded as numbers below 256. The finite facts are:
  - for q = 10 .. 25, three periods reach a fixed point of the period map, and cell +1 is constant at every tick;
  - for q >= 26, W^26 = W^22 on the sets that occur, which gives q's behaviour as 22 + (q - 22) % 4.
- `win_step` proves that the encoded eight cells follow Rule 30 exactly.
- Step 4 uses Theorem A as in TheoremA.lean, including the time re-basing.
- `control_q9` shows that the check fails at q = 9.
- The axioms are propext, Classical.choice and Quot.sound. There is no sorryAx and no native_decide.

*Independent full source review (GPT GC893, 2026-10-09 23:41 BST).* WhiteEnd.lean's statement, state encoding, restricted-set W26/W22 induction, actual-path containment, phase split and formal time rebasing match entry40. TheoremA executable source is unchanged; white_end_finite even allows an infinite right tail, assuming only a left bound and one black cell. q9 is a failed determination check, not a finite-seed counterexample. Source/hand acceptance only: compilation and kernel finite-check execution remain Local L508's evidence, not GPT replay.

*Memory-lean revision source review (GPT GC898, 2026-10-10 00:05 BST).* Nat.rec preserves the old descending accumulator equation for all initial accumulators; split kernel declarations cover exactly q10..25 and representatives22..25. The final theorem assembly is unchanged. Source/hand PASS; no GPT compilation or performance measurement, which remain Local L509 evidence.

### 41. More column words excluded by entry 40's route (computed twice, second-read): 24 words of period 10 .. 14 and 115 of period 15 .. 18

*Status:* the per-word computation was done by Local (`rule30_word_jen_census.py`, WC, predictions first, L499) and
replayed independently by Cloud (`rule30_cloud_word_census_replay.py`, WR2, CL111; Lyndon words by Duval, successor
tables and set-valued stable sets, no shared code). Every count and word agrees. The transfer is entry 40's
(second-read by Cloud CL110 and GPT GC880), and its finish, Theorem A, is machine-checked (entry 5's note). Filed by
Local, 2026-10-09.

*Dated note (Cloud, 2026-10-23): the Rule30PrizeKit's `Rule30StripCertificateTable` (30 words of length 8–13 at strip
widths ≤ 9) overlaps this entry in eleven words of length 10–13 and has run-type words (00111111111, 01011111111,
000111111111, …) that this entry's one-sided relaxation at widths 8 and 10 does not determine. The 128 words of this
entry not in the kit's table were submitted to the Rule 30 Prize for AI agents on the kit's definitions as
R30-20261022-5c4fbf (48 words, lengths 11–16) and R30-20261022-70d23b (80 words, 17–18), both Lean Verified
(reports/wolfram-agents/MAP.md §5).*

**Theorem.** No nonzero finite configuration of Rule 30 has a column that is eventually periodic with any of the
following period words.
- These words, of period 10 .. 14, via the width-10 relaxation (the 14 without a star are already excluded at width 8;
  the 10 starred need width 10):
  - p = 10: 0000000011*, 0011111111
  - p = 11: 00000000001, 00000000011, 00000001111*
  - p = 12: 000000000001, 000000000011, 000000000101*
  - p = 13: 0000000000001, 0000000000011, 0000000000101*, 0000000001011, 0000000001101*, 0000000001111*, 0000000010011*
  - p = 14: 00000000000001, 00000000000011, 00000000000101*, 00000000001011, 00000000001111*, 00000000010011,
    00000000010111, 00000000011011, 00000000110011*
- Every primitive word of period 15 .. 18 that is determined at width 8: 15, 20, 31 and 49 words, 115 in all. They
  are reproduced by `rule30_word_jen_census.py 8 15 18` and by WR2.
- Words are least rotations; any rotation is the same column word.

**Proof.** Entry 40's argument, word by word.
1. In the k-cell one-sided relaxation (k = 8 or 10), the stable set of the period's step relation determines x1 at
   every tick. So column +1 is eventually periodic with the word's period on every actual right half.
2. Column 0 is periodic.
3. Theorem A (entry 5; `no_two_periodic` in TheoremA.lean) forbids two adjacent columns periodic for ever when there
   is a leftmost black cell, re-basing time if the edge starts right of column 0. ∎

*Scope.* No word of period 7 .. 9 is determined at width 8 or 10. Every determined word has a run of length >= 6. The
determined share is 0.6 percent (width 8) and 1.0 percent (width 10) of periods 7 .. 14, and 0.4 percent of 15 .. 18.
The prize's 01 and every word of period <= 9 are untouched. Not a prize claim.

*Near-entry gate (Local, at filing).* `--near 41` gives entry 40, its parent: the route and the white-end family,
which this extends to other words and does not restate; 17 and 38, read. Hard checks pass.

*Machine-checked (Local, 2026-10-10 00:34 BST).* tests/probes/lean/JenRoute.lean (Lean 4, Mathlib).
- `entry41`: no configuration with a leftmost black cell has a column reading any of the 139 words periodically. The
  words are 129 at width 8 and 10 at width 10, the same lists as WC and WR2. `counts` checks the list lengths.
- Each word's finite fact is a kernel `decide` on the K cells as numbers below 2^K. Within n0 <= 6 periods the
  set of states is a fixed point of the period map, and cell +1 is constant at every tick.
- The rest is WhiteEnd.lean's assembly, made generic in K and in the word: the encoding's step lemma (StpOK 8 and
  StpOK 10 by decide), Theorem A, and the time re-basing.
- The axioms are propext, Classical.choice and Quot.sound; there is no sorryAx and no native_decide.

### 42. The left diagonals' periods are powers of 2 (Jen's Theorem 4, proved again, second-read, machine-checked): every diagonal k ≥ 2 settles with a period dividing 2^(k−2)

*Where:* CHAT-LEDGER L540 .. L543 (2026-10-10); the record map's line on left diagonals (§8.27, §8.30). *Bears on:* the
left band's periods (B2, §8.31), and the run bounds of entries 12 and 13. *Status:* proved by Local, machine-checked;
second-read by Cloud by hand (CL171, the step; CL172, the Lean statements) and by GPT on the full Lean source (GC962). The record credits the statement to Jen (1986, Theorem 4) and Rowland (§5); Jen's paper is
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

### 43. Proposition 24 (proved by hand, second-read by GPT): under the Collatz shortcut map an orbit that alternates for ever is the trivial cycle, so the conjecture says every parity column ends in 1010...

*Where:* RULE30-PRIZE.md, "8.92 The fair-coin question, and the pair and price table (2026-10-13 11:32 BST)";
`tests/probes/lexicon/rule30_pair_price.py` (P8, P9, P10). *Bears on:* the pair and price table (8.92), where it puts
Collatz in the cell with neither price nor pair; the Collatz twin (COLLATZ-PRIZE.md). *Status:* Local's proof (2026-10-13, AGENTS.md item 16). Second-read by GPT (GC1162, 2026-10-13): (a) and (b)
confirmed, with an independent integrality check (m - 1 = (3/4)^r (m_0 - 1), so 4^r divides m_0 - 1 for every r and
m_0 = 1); (c) as first written failed at w = 1 in the even phase, and is corrected below to w >= 2. Elementary and very
likely known (the trivial cycle 1, 2 of the shortcut map); prior art not searched.

**Proposition 24.** Let T(n) = n/2 for even n and T(n) = (3n+1)/2 for odd n, on the positive integers, and read the
parity of T^k(n), k = 0, 1, 2, ..., as a column.
(a) If the column of n alternates from some tick on, the orbit of n reaches 1.
(b) So the Collatz conjecture holds if and only if every positive orbit's parity column is eventually 1010....
(c) For every w >= 2 and k >= w, exactly one n in [1, 2^w) has a column that alternates from tick 0 for k ticks in each
phase: n = 1 for 1010... and n = 2 for 0101.... At w = 1 the range holds only n = 1, so the phase 0101... has none
(GPT's correction, GC1162).

*Proof.* (a) Take a tick of the alternating stretch at which the value m is odd. Then T(m) = (3m+1)/2 is even and
T^2(m) = (3m+1)/4 is odd, and (3m+1)/4 < m whenever m > 1. So the odd values along the stretch decrease strictly while
they exceed 1; they cannot decrease for ever, so one of them is 1. (b) An orbit that reaches 1 continues 1, 2, 1, 2, ...,
whose column is 1010...; the converse is (a). (c) By Terras's bijection a parity word of length k fixes n modulo 2^k,
and when k >= w a residue class modulo 2^k holds at most one n in [1, 2^w). The columns of 1 and 2 alternate for ever,
in the two phases, so for w >= 2 each phase has exactly that one n; at w = 1 the number 2 lies outside [1, 2). $\square$

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

*Machine-checked (Local, 2026-10-10 04:56 BST).* tests/probes/lean/ShortC.lean, `checkerboard`, with column 0 black at times t .. t + k and 1 <= j <= k; no sorryAx.

### C.2 The latch (RULE30-PRIZE.md §8.62; 2026-10-06)

*Where:* §8.62, the white Condrey end. *Bears on:* Conjecture B next to white stretches; the slow walls (§8.63). *Status:* proved.

**Lemma.** If column 0 is white at time $t$, then $x_{t+1}(1) = x_t(1) \vee x_t(2)$. Hence across a white stretch of
the wall column 1 is non-decreasing: once black it stays black until the stretch ends.

*Proof.* Rule 30 at column 1 reads $x_{t+1}(1) = x_t(0) \oplus (x_t(1) \vee x_t(2))$, and $x_t(0) = 0$. $\square$

*Machine-checked (Local, 2026-10-10 04:56 BST).* tests/probes/lean/ShortC.lean, `latch`; no sorryAx.

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

*Machine-checked (Local, 2026-10-10 04:56 BST).* tests/probes/lean/ShortC.lean, `shrink`, for a white run [a, b] with b >= a + 1 bounded by black cells; no sorryAx.

### C.4 The leftward speed of information is an identity (RULE30-PRIZE.md §8.66; 2026-10-06)

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

*Independent second reading (GPT, 2026-10-07, R1 in RULE30-GPT.md; GC292).* Verified by right-to-left reconstruction: every length-n output has exactly four free-boundary predecessors; exactly one predecessor of a maximal white run is a continuation. Independent truth-table enumeration confirms the counts for widths1–10 and all output blocks through width7, with Rule0 rejected. The one-cell periodic-ring check rejects importing infinite-row measure invariance into cyclic boundaries. The deterministic single-cell census has not been replicated by this reading.

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


*Admissibility audit (GPT, 2026-10-07, R4/GC299; independent review pending).* The table above is formal in arbitrary visible words. An actual right half beside0101 obeys Lemma3's no11 condition, so its depth4 product is zero. R4 derives affine even/odd formulas through depth6 and the depth7 odd value1 XOR c_(s+3) XOR (c_(s+1) AND c_(s+3)). A single preregistered256-seed check matches literal inverse columns; four witnesses with c_s=c_(s+2)=0 realize all product-input pairs and mixed XOR1. Thus depth7 is nonaffine in these four visible inputs on the driven-right prefix domain. This does not provide an eventually white initial left tail or a global linearization; C7's formal table is preserved.

*Author's check of the admissibility audit (Local, 2026-10-07; chat L187).* R4 is right, with one slip in a printed
list. Beside the wall a visible 1 at time $2s$ persists at $2s + 1$, where the wall is 0. Then, with the wall 1, it
forces the next visible bit to 0, so actual right halves have no 11, and the formal product $c_s c_{s+1}$ in column
$-4$ vanishes on them. R4's reductions at depths 5 to 7 use only $AB = BD = DE = 0$. Checked
(`rule30_audit_g99_g100.py`, S104):
- R4's seven even/odd pairs hold on all 55 no-11 visible words of length 8, with random hidden odd bits, which are
  invisible.
- The formal table above holds on all 256 words, and its product is not identically zero there.
- GPT's four seeds, driven beside the wall, are admissible with $A = D = 0$ and $(B, E) = 00, 01, 10, 11$.
- Their depth-7 odd outputs are 1, 0, 1, 1, as $1 + E + BE$ gives and as GPT's probe prints when run. The "1, 1, 0, 1"
  in R4 and in the probe's outcome note is a transcription slip. The mixed XOR is still 1, so the non-affine
  conclusion stands.


### C.8 Rule 30's velocity is Rule 210 (RULE30-PRIZE.md §8.70; 2026-10-06)

*Where:* §8.70 (the owner's question about velocity and acceleration). *Bears on:* why Rule 210 is Rule 30's closest
sibling; the prize as a difference equation over GF(2). *Status:* proved.

**Proposition.** $x_{t+1}(i) \oplus x_t(i) = x_t(i-1) \oplus (\lnot x_t(i) \wedge x_t(i+1))$ for Rule 30, i.e. Rule 30 $= c \oplus$ Rule 210.

*Proof.* $l \oplus (c \vee r) = l \oplus c \oplus r \oplus cr$, and $l \oplus r \oplus cr = l \oplus (\lnot c \wedge r)$. $\square$

### C.9 Group coarsening with any-realization margin inheritance (Cloud CL508/515; second-read by GPT, MI619)

*Status:* PROVED for lemma(a)–(c), under the stated hypotheses,
by Cloud's hand argument and GPT's targeted carrying read,2026-10-22.
This verifies coarsened cut admission and the exact shifted child margin.
It does not prove the top-tight lemma or solve base exceptions. CL515's
correction is part of the adopted scope; the original pair-branch claim
is not adopted. The original candidate below is retained as provenance.

**Carrying check, GPT.** A group containing the merged bin is exactly an
original proper group; for a proper outside child group K, G union K is
still proper, so subtracting least slacks gives the g*r term. Actual hole
count is g+h-b-(M-c); shifting targets subtracts b*r and gives exactly
mu'=h'+(mu-h)+(M-c). No geometry of a canonical R is used. At h=0
reflection swaps complementary slacks because the pool is a full interval;
that argument is not imported at h>0. Fewer-bin feasibility/exception
control remain premises of the global induction. This is MI368's known
margin computation combined with the requested coarsening application,
not a new GPT theorem or a new computational run.

### Cloud CL508 — Coarsening reduction: H(h) reduces to its co-singleton case (Cloud, 2026-10-22; waiting room)

*Status:* hand proof, single-party (the overnight arrangement, CL481); a second reader is needed before adoption. Step
(b) is MI368's computation with a group in place of a singleton. The new step is the use of (a), coarsening (GPT's device in MI576, there applied to G315), which removes the
pair/triple branch that CL439 expected to need G316's staircase. Machine support (tier 1, single-party):
- `descent_every.py`: every realization of a least-slack singleton or pair keeps the child in its family, with 0 bad
  out of 20,396 and 2,972 realizations;
- `kholek.c`: coarsened instances (one big bin) have no H(h) failures for k = 3, sizes (3,3,6..9), (3,4,7), h ≤ 6, and
  for k = 4, sizes 333X, h ≤ 6 (CL503).

**Setting.** S = [0, M] ∖ H with |H| = h, n = |S| = M + 1 − h, and k bins of sizes c_i ≥ 3 summing to n, with targets
u_i summing to ΣS. The instance is in H(μ), μ ≥ h, if u_J ≥ L(r_J) + μ·r_J for every proper nonempty group J, where
r_J = Σ_{i∈J} c_i and L(r) = r(r − 1)/2. Its slack is σ_J = u_J − L(r_J) − μ·r_J ≥ 0.

**Lemma.** Let G be a proper group of least slack with s bins, 1 ≤ s ≤ k − 2, and g = r_G.
- (a) The coarsened instance I_G (the bins of G, plus one bin B of size n − g ≥ 6 and target ΣS − u_G) is in H(μ) on S.
- (b) For ANY partition of S realizing I_G, let R be the union of G's sets and b ≤ c the least and greatest elements of
  S ∖ R. Shifted by −b, the k − s bins outside G form an instance on S ∖ R ⊆ [b, c] with h′ = (c − b + 1) − (n − g)
  holes, and it is in H(μ′) with μ′ = h′ + (μ − h) + (M − c) ≥ h′.
- (c) Consequently, if I_G and that child are both feasible, so is the instance.

**Proof.**
- (a) A proper nonempty group of I_G either omits B, and is then a nonempty union of G's bins, or contains B and
  omits some bin of G. In both cases it is a union of original bins that is neither empty nor everything, hence an
  original proper group. Its cut condition is the original one, with the same size and target.
- (b) Let K be a proper nonempty group of the bins outside G, with r = r_K. Then G ∪ K is a proper group of the
  instance (it omits a bin outside K), so σ_{G∪K} ≥ σ_G. Since L(g + r) − L(g) = L(r) + g·r,
  u_K = u_{G∪K} − u_G ≥ L(r) + (g + μ)·r.
  Counting S ∖ R in [b, c] gives h′ = (c − b + 1) − (n − g) = g + h − b − (M − c), using n = M + 1 − h. So the shifted
  target is u_K − b·r ≥ L(r) + (g + μ − b)·r = L(r) + μ′·r with μ′ = h′ + (μ − h) + (M − c) ≥ h′. ∎
- (c) Is immediate.

**Consequence.** By induction on k, H(μ) instances whose least slack is attained by some group of at most k − 2 bins
reduce to two instances with fewer bins, each in its own H family:
- the coarsened one, on the same pool, has a big bin;
- the child has h′ holes.

The irreducible instances are those whose least slack is attained ONLY by co-singletons, i.e. groups of k − 1 bins (a
top-tight bin).

At h = 0 the family H(0) on [0, M] is reflection-symmetric: x ↦ M − x maps the slack of J to the slack of its
complement, because L(n) − L(n − r) = rM − L(r) when n = M + 1. So a least-slack co-singleton becomes a least-slack
singleton after reflection, and every H(0) instance reduces.

**Hence SS3 for every k (h = 0) follows from:**
- (i) H₂, the subset-sum spectrum lemma (G318 for at most three deletions);
- (ii) H_j(h) with h ≥ 1 for j < k, in particular its co-singleton case;
- (iii) control of the base exceptions (H₃, H₄ equal-sum cores; CL503–504).

The co-singleton case at h ≥ 1 is CL443's wall. In the five-bin samples of CL505, 55% of H₅(1) instances are of this
kind.

**Correction (Cloud, CL515, 2026-10-22 04:04 BST).** The lemma (a)–(c) stands, but the consequence overstated what it
removes. For s ≥ 2 the coarsened instance I_G has least slack σ_G, because G is one of its groups and is globally
least. In I_G, G is the complement of the single bin B, so **I_G is itself top-tight, with the big bin B top-tight**.
So:
- only singleton-least instances (s = 1) reduce to H₂ plus a child;
- pair- or triple-least instances reduce to a child plus a top-tight instance with one big bin.

The conclusion "SS3 for every k follows from H₂ plus the top-tight lemma (all smaller k, h ≥ 1)" is unchanged, by
induction on k. But CL439's pair/triple branch does not disappear; it becomes the top-tight lemma for instances with a
bin of size ≥ 6. At h = 0 reflection still reduces everything.

### C.10 Triple H2 window at n at least 2h+4 (Cloud CL517; second-read by GPT, MI619)

*Status:* PROVED in the stated triple-only range by Cloud's hand proof,
with GPT's targeted carrying read,2026-10-22. The original candidate
text follows for provenance. No claim for general subset size or the
full measured sharp threshold is adopted.

**Carrying check, GPT.** Endpoint trimming preserves the window inclusion
and weakens the cardinality gate. Each anchor's pair matching has at
least h+2 edges, against h holes plus one forbidden anchor. The translates
integer-join because their cardinality exceeds every possible consecutive
pool gap. For the upper excess, counting each hole's incidences below the
first n-3 values gives E<=d. At offset j, pairs in[0,M-1] have exact
count h+1-ceil(j/2) and smallest possible endpoint
n-h-3+j>d. Hence only h-d holes can hit them, strictly fewer than the
pair count for j<=d. Both endpoint formulas and strict inequalities
were re-derived; no numerical census was rerun or used as a proof premise.
The nearest already-carried G318/G340/G341 scalar engines were read:
this is a different total-dependent H2 window/range, not their restatement.

### Cloud CL517 — Triple sums of an interval with holes fill the H₂ window when n ≥ 2h + 4 (Cloud, 2026-10-22 04:15 BST; waiting room)

*Status:* complete hand proof, single-party (the overnight arrangement, CL481); a second reader is needed before
adoption. It is the r = 3 case of H₂ (CL514), the two-bin base of the H(h) reduction tree (CL508, CL515). Machine
support: `spectrum_h.py` and its edge runs (no window gap for n ≥ 7 and h ≤ 2n − 8 on every pool tested). The
threshold is confirmed by an independent self-check (CL518).

**Statement.** Let S = [0, M] ∖ H with |H| = h, n = |S| = M + 1 − h ≥ 7, and n ≥ 2h + 4. Then every integer u with
3 + 3h ≤ u ≤ ΣS − L(n − 3) − h(n − 3) is the sum of three distinct elements of S. (L(r) = r(r − 1)/2.)

**Proof.**

*Step 0 (reductions).*
- If s₁ = min S > 0, the pool S − s₁ ⊆ [0, M − s₁] has h − s₁ holes. The map u ↦ u − 3s₁ sends the window for (S, h)
  onto the window for (S − s₁, h − s₁):
  - the lower ends agree, since 3 + 3h − 3s₁ = 3 + 3(h − s₁);
  - the upper ends agree, since ΣS − n·s₁ − L(n − 3) − (h − s₁)(n − 3) = ΣS − L(n − 3) − h(n − 3) − 3s₁.
- If max S < M, deleting the top holes lowers h, which lowers the window's lower end and raises its upper end. The
  window only grows.
- Both changes preserve n ≥ 2h + 4. So assume 0, M ∈ S, with all holes interior.
- Write s_i = i − 1 + d_i, where d_i is the number of holes below s_i, and let d = d₂ (the holes between 0 and s₂).

*Step 1 (pairs).* For every z ∈ S and every v with 2h + 3 ≤ v ≤ 2M − 2h − 3, v = x + y with x < y in S ∖ {z}.
- The pairs {x, v − x} with 0 ≤ x < v − x ≤ M are pairwise disjoint.
- There are min(⌊(v + 1)/2⌋, ⌊(2M − v + 1)/2⌋) ≥ h + 2 of them.
- The h holes and z meet at most h + 1 of them.

*Step 2 (the middle).* Σ₃(S) ⊇ [2h + 3, 3M − 2h − 3].
- Σ₃(S) ⊇ ∪_{z ∈ S} (z + I), where I = [2h + 3, 2M − 2h − 3], by Step 1.
- I has 2M − 4h − 5 integers. That is at least h + 1 because 2M = 2n + 2h − 2 ≥ 5h + 6, which follows from n ≥ 2h + 4.
- Consecutive elements of S differ by at most h + 1, so consecutive translates overlap.
- The union therefore runs from 0 + 2h + 3 to M + 2M − 2h − 3.

*Step 3 (the bottom).* 3 + 3h ≥ 2h + 3.

*Step 4 (the top).*
- Since ΣS = L(n) + Σ d_i, L(n) − L(n − 3) = 3n − 6 and d_n = h:
  W_hi − (3M − 2h − 3) = Σ_{i ≤ n−3} (d_i − h) + d_{n−2} + d_{n−1}.
- Here Σ_{i ≤ n−3} (h − d_i) = Σ over holes q of #{i ≤ n − 3 : s_i < q}. Every hole contributes at least 1 (0 ∈ S), and
  at least 2 unless it lies between 0 and s₂.
- So the excess E = W_hi − (3M − 2h − 3) ≤ 2h − (2h − d) = d.
- For u = 3M − 2h − 3 + j with 1 ≤ j ≤ d, write u = M + v with v = 2M − 2h − 3 + j. The pairs {x, v − x} in [0, M − 1]
  number h + 1 − ⌈j/2⌉, and every one has x ≥ n − h − 3 + j.
- The d holes below s₂ lie in [1, d]. Since d ≤ h and n ≥ 2h + 4, d < n − h − 3 + j, so those holes miss every pair.
  At most h − d other holes meet the pairs, and h + 1 − ⌈j/2⌉ > h − d because ⌈j/2⌉ ≤ d.
- So some pair survives, and u = M + x + y with x < y < M. ∎

**Scope.**
- Only r = 3, and only n ≥ 2h + 4. The census indicates the truth is h ≤ 2n − 8, which is sharp by
  S = {0} ∪ [h + 1, M], where u = 2M is missing at h = 2n − 7.
- r ≥ 4 does not follow by window induction (CL519).

### C.11 Exact depth-three and depth-four subset-sum gaps after three deletions (Cloud CL495; second-read by GPT, MI623)

*Status:* PROVED in the stated scalar scope under independent carrying
review. Cloud's original proof is retained below as provenance; its
waiting-room label is historical. GPT read all carrying steps at 2026-10-22 13:32 BST.
The depth>=5 exclusion uses already-PROVED G340; no finite census is
a proof premise. No multi-bin compatibility or novelty claim follows.

**Carrying receipt.** The sorted j-for-j exchange costs at least j².
At offset3 only one exchange can occur; the three possible crossing
pairs are disjoint, so blocking them with<=3 internal holes forces
exactly the four listed tau-relative patterns. Counting holes below
tau translates each to the stated k-relative pattern without a
shift ambiguity. At offset4 the four one-exchange pairs are disjoint;
three holes cannot block them all unless an outer pair lies outside
the ambient interval. k>=3 and n-k>=3 force those boundary cases
to be exactly tau2 or N=tau+3. The three remaining blocking holes
in each case also prevent the only possible two-exchange realization.
Converses and both boundary directions were checked. Finally
beta-alpha>=k(n-k)>=12, so offsets3/4 really have actual depth3/4.

**Hand controls and scope.** At N9,k3,D={4,5,6}, alpha3 and7 is
missing. The complementary reflected N9,k4,D={3,4,5} has alpha9
and13 missing. Unexpected four-hole control: R={0,3,4,5,6,9,10},
k3,alpha7 has no single exchange of gain4, but exchanging3,4 for5,6
realizes11. Thus the double-exchange alternative cannot be omitted
from the underlying argument, even though this control lies outside
the three-hole theorem. No program or basis was run. The nearest
G332/G326/W322 were read in full; none gives this exact arbitrary-k
scalar list. proof_dupes controls pass; source support read, not replayed.

### Cloud CL495 — Lemma G3: the exact deep gaps after three deletions (Cloud, 2026-10-22; waiting room)

*Status:* complete hand proof, single-party (the overnight arrangement, CL481); a second reader is needed before
adoption. It sharpens GPT's G340 (missing depth ≤ 4) to an exact list. Machine support: `deep_gaps_d3.py`,
`deep_gaps_d3_check.py` (exhaustive for N ≤ 22 and k ≤ 6, 35,328 (pool, k) cases, nothing outside the list).

**Statement.** Let R = [0, N] minus a set D of at most three internal values, n = |R| ≥ 7, 3 ≤ k ≤ n − 3. Let α be
the least k-subset sum of R. Then:
- α + 1 and α + 2 may be missing (the near-edge omissions);
- α + 3 is missing exactly when D = k + {0,1,2}, k + {−1,1,3}, k + {−2,2,3} or k + {−1,0,4};
- α + 4 is missing exactly when k = 3 and D = {4, 5, 6}, or k = n − 3 and D = {k − 1, k, k + 1};
- by G340, nothing at depth ≥ 5 is missing.

The high end follows by reflection x ↦ N − x. Complementation (k ↔ n − k) relates the two ends.

**Proof.** Write r₀ < r₁ < … for the elements of R, B = {r₀, …, r_(k−1)} with top τ = r_(k−1), and α = ΣB.
1. *Swap form.* A k-subset X of R is (B ∖ A) ∪ A′ with A ⊆ B, A′ ⊆ R ∖ B and |A| = |A′| = j. List
   A = {a₁ < … < a_j} and A′ = {b₁ < … < b_j}; then ΣX − α = Σ_i (b_i − a_i).
2. *Cost of a swap.* The a_i are distinct values ≤ τ and the b_i distinct values > τ, so a_i ≤ τ − (j − i) and
   b_i ≥ τ + i. Hence b_i − a_i ≥ j for every i, and the excess is at least j². Excess ≤ 3 therefore needs j = 1;
   excess 4 needs j = 1, or j = 2 with A = {τ − 1, τ} and A′ = {τ + 1, τ + 2}, all four present.
3. *α + 3.* It is present iff some a ∈ B and b ∈ R ∖ B have b − a = 3. Since b > τ ≥ a, that means one of the pairs
   (τ − 2, τ + 1), (τ − 1, τ + 2), (τ, τ + 3) has both members in R; a value ≤ τ in R is automatically in B. The
   value τ is in R, and n − k ≥ 3 values of R exceed τ, so all six values lie in [0, N]: τ − 2 ≥ 0 because k ≥ 3.
   So α + 3 is missing iff τ + 3 ∈ D, one of τ − 1, τ + 2 is in D, and one of τ − 2, τ + 1 is in D. That uses all
   three deletions, giving D ∈ {τ + {−2,−1,3}, τ + {−1,1,3}, τ + {−2,2,3}, τ + {1,2,3}}. Since
   τ = k − 1 + |D ∩ [0, τ)|, these are k + {−1,0,4}, k + {−1,1,3}, k + {−2,2,3} and k + {0,1,2}.
4. *α + 4.* By step 2 it is present iff one of the pairs (τ − 3, τ + 1), (τ − 2, τ + 2), (τ − 1, τ + 3), (τ, τ + 4)
   has both members in R, or τ − 1, τ + 1, τ + 2 are all in R. The four pairs are disjoint, so three deletions
   block them all only if one pair does not exist. Either τ − 3 < 0: then τ = 2, k = 3, B = {0,1,2}, no deletion
   lies below τ, and blocking (0,4), (1,5), (2,6) forces D = {4, 5, 6}, which also blocks the double swap. Or
   τ + 4 > N: since n − k ≥ 3 values exceed τ, this means N = τ + 3 with τ + 1, τ + 2, τ + 3 present and k = n − 3;
   blocking (τ − 3, τ + 1), (τ − 2, τ + 2), (τ − 1, τ + 3) forces D = {τ − 3, τ − 2, τ − 1}, so τ = k + 2 and
   D = {k − 1, k, k + 1}, and τ − 1 ∉ R blocks the double swap. Conversely both configurations miss α + 4. (The
   second is the first one's image under complementation k ↔ n − k combined with reflection.)
5. *Depth.* In each case the missing value is at distance 3 or 4 from α, and n ≥ 7 with k ≤ n − 3 puts β at least
   that far away, so the gap's depth is as stated. ∎

*Remark.* The same pair-blocking count explains G341's 2D − 3: missing α + e needs every one of about e disjoint
pairs (τ − i, τ + e − i) blocked, and the double swaps add more.

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


## E2. GPT's proofs, second-read (G39 to G204 moved from the waiting room 2026-10-06, by Local; later entries promoted as their readings arrived, each naming its second reader)

### GC2007 — Five-step right-prefix period bound (second-read by Local, L1063, 2026-10-28)

For every normalized nonempty finite seed, the prefix-growth word11011 is forbidden after base period4. Together with GC763, this gives log2 Q_j<=floor((3j+5)/5). [Complete proof, exceptional base2 and retained self-check](reports/rule30-five-step-period-bound.md). This is a short explicit restriction, not the best known single-seed ceiling: external1b82d8 already has a half-rate bound. Later Newton/source-parametrization addenda in the report are not covered by this second read.


### GC2118 / GC2123 — Explicit whole-prefix bridge and actual 11011 exclusion (Local L1142; compiler L1144)

For arbitrary actual Rule30 diagonals D_i(t)=evol(x,t,t-i), k>=2 and p>0 divisible by4, suppose the
prefix through k-1 has periodp; through k has LEAST period2p; through k+1 has LEAST period4p; through
k+2 has period4p; and through k+3 has LEAST period8p. Then the prefix through k+4 has period8p and
cannot have least period16p. No individual-period monotonicity or finiteness of x is assumed. Its bridge
uses whole-prefix minimality to force a complementary new diagonal; standard cycle lifting is credited,
not claimed new. The genuine p2 single-seed11011 exception is retained.

**PROVED hand, two-party L1142/GC2123.** L1144's retained actual Lean4.35 output has empty original compilation
and exact six standard-axiom declarations, independently read GC2125. [Source and full argument](reports/wolfram-agents/PREFIX-PERIOD-BRIDGE.md).
GC2128 fully reads the retained parent/text/source packet and resolves original/sanitized mutant hashes;
compiler and enforcement evidence accepted within their attributed scope, no independent rerun, binary-object
revalidation, submission-form checker, native notebook or public bridge delivery claimed. This formalizes the explicit guarded content of the older GC2007 hand result, not a new best bound.
**GC2127 disposition:** earlier public PR51 prefix-clock formalization/application read; known mechanisms
reproved in this conditional interface, no new portal/PR extension. [Exact scope and credit](reports/wolfram-agents/PREFIX-PRIOR-ART-REVIEW.md).
The older28October hand proof remains credited; the earlier29October public Lean is Troy Lowry's.


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

*Moved to volumes on 2026-10-28 (Local, at the owner's request).* This section held 506 proofs and 1.64 MB, 85% of
this file. They now live unchanged in four volumes in [proofs/](proofs/). The index below lists every proof, in its
original order, with a link straight to it. The search tool `record_find.py` also searches `proofs/`.

**Volume 1: [proofs/PROOFS-E2.1.md](proofs/PROOFS-E2.1.md), G.GPT39 to G126 (203 proofs)**

- [G.GPT39. Fixed-endpoint survival conditioning](proofs/PROOFS-E2.1.md#ggpt39-fixed-endpoint-survival-conditioning)
- [G39 theorem and proof: fixed-endpoint event transfer](proofs/PROOFS-E2.1.md#g39-theorem-and-proof-fixed-endpoint-event-transfer)
- [G.GPT40. Survival-compatible adjacent-pair phase product](proofs/PROOFS-E2.1.md#ggpt40-survival-compatible-adjacent-pair-phase-product)
- [G40 theorem and proof: the skeleton phase product](proofs/PROOFS-E2.1.md#g40-theorem-and-proof-the-skeleton-phase-product)
- [G.GPT41. Interior-endpoint free-pair mass](proofs/PROOFS-E2.1.md#ggpt41-interior-endpoint-free-pair-mass)
- [G41 theorem and proof: linearly many free pairs at interior endpoints](proofs/PROOFS-E2.1.md#g41-theorem-and-proof-linearly-many-free-pairs-at-interior-endpoints)
- [G.GPT42. A primitive-character resonance with linearly many free pairs](proofs/PROOFS-E2.1.md#ggpt42-a-primitive-character-resonance-with-linearly-many-free-pairs)
- [G42 theorem and proof: primitive characters can remain resonant](proofs/PROOFS-E2.1.md#g42-theorem-and-proof-primitive-characters-can-remain-resonant)
- [G.GPT43. Exact binary-reader Fourier weights](proofs/PROOFS-E2.1.md#ggpt43-exact-binary-reader-fourier-weights)
- [G43 theorem and proof: exact ternary spectrum of a binary reader](proofs/PROOFS-E2.1.md#g43-theorem-and-proof-exact-ternary-spectrum-of-a-binary-reader)
- [G.GPT44. Exact finite-ensemble parity-tail information budget](proofs/PROOFS-E2.1.md#ggpt44-exact-finite-ensemble-parity-tail-information-budget)
- [G44 theorem and proof: resolution of a finite residue ensemble](proofs/PROOFS-E2.1.md#g44-theorem-and-proof-resolution-of-a-finite-residue-ensemble)
- [G.GPT45. Word-specific actual-start survival ceilings](proofs/PROOFS-E2.1.md#ggpt45-word-specific-actual-start-survival-ceilings)
- [G45 theorem and proof: actual-start survival is a residue class cut by a ceiling](proofs/PROOFS-E2.1.md#g45-theorem-and-proof-actual-start-survival-is-a-residue-class-cut-by-a-ceiling)
- [G.GPT46. Unbounded formal ceilings and residue-count rounding](proofs/PROOFS-E2.1.md#ggpt46-unbounded-formal-ceilings-and-residue-count-rounding)
- [G46 theorem and proof: the formal ceilings are unbounded](proofs/PROOFS-E2.1.md#g46-theorem-and-proof-the-formal-ceilings-are-unbounded)
- [G.GPT47. First-deficit single-run survival implies a periodic return](proofs/PROOFS-E2.1.md#ggpt47-first-deficit-single-run-survival-implies-a-periodic-return)
- [G47 theorem and proof: this first-deficit family realizes only by a return](proofs/PROOFS-E2.1.md#g47-theorem-and-proof-this-first-deficit-family-realizes-only-by-a-return)
- [G.GPT48. First-deficit gap and its positive-lift domain](proofs/PROOFS-E2.1.md#ggpt48-first-deficit-gap-and-its-positive-lift-domain)
- [G48 audit identity: the first-deficit gap](proofs/PROOFS-E2.1.md#g48-audit-identity-the-first-deficit-gap)
- [G.GPT48C. Computed first-deficit certificate through horizon16](proofs/PROOFS-E2.1.md#ggpt48c-computed-first-deficit-certificate-through-horizon16)
- [G48 computed finite-horizon certificate](proofs/PROOFS-E2.1.md#g48-computed-finite-horizon-certificate)
- [G.GPT49. Scope of the floor(3n/2) test bed](proofs/PROOFS-E2.1.md#ggpt49-scope-of-the-floor3n2-test-bed)
- [G49 theorem and proof: floor(3n/2) preserves coding but changes survival](proofs/PROOFS-E2.1.md#g49-theorem-and-proof-floor3n2-preserves-coding-but-changes-survival)
- [G.GPT50. Mahler itinerary coupling and alphabet scope](proofs/PROOFS-E2.1.md#ggpt50-mahler-itinerary-coupling-and-alphabet-scope)
- [G50 theorem and proof: Mahler needs both itineraries, and a different alphabet](proofs/PROOFS-E2.1.md#g50-theorem-and-proof-mahler-needs-both-itineraries-and-a-different-alphabet)
- [G.GPT51. Exact finite Mahler coupling window](proofs/PROOFS-E2.1.md#ggpt51-exact-finite-mahler-coupling-window)
- [G51 lemma and proof: exact finite Mahler coupling window](proofs/PROOFS-E2.1.md#g51-lemma-and-proof-exact-finite-mahler-coupling-window)
- [G.GPT52. Phase-aligned period-block extension of Corollary F](proofs/PROOFS-E2.1.md#ggpt52-phase-aligned-period-block-extension-of-corollary-f)
- [G52 theorem and proof: Corollary F for phase-aligned period blocks](proofs/PROOFS-E2.1.md#g52-theorem-and-proof-corollary-f-for-phase-aligned-period-blocks)
- [G52 addendum: the empty initial left row is covered](proofs/PROOFS-E2.1.md#g52-addendum-the-empty-initial-left-row-is-covered)
- [G.GPT53. Period-block form of the entropy squeeze](proofs/PROOFS-E2.1.md#ggpt53-period-block-form-of-the-entropy-squeeze)
- [G53 lemma and proof: period-block entropy conversion](proofs/PROOFS-E2.1.md#g53-lemma-and-proof-period-block-entropy-conversion)
- [G.GPT54. Gap-matrix coarse squeeze for every periodic wall](proofs/PROOFS-E2.1.md#ggpt54-gap-matrix-coarse-squeeze-for-every-periodic-wall)
- [G54 corollary and proof: coarse squeeze for every periodic wall](proofs/PROOFS-E2.1.md#g54-corollary-and-proof-coarse-squeeze-for-every-periodic-wall)
- [G.GPT55. Prime-ring quotient cycle lifting](proofs/PROOFS-E2.1.md#ggpt55-prime-ring-quotient-cycle-lifting)
- [G55 lemma and proof: prime-ring cycle lifting](proofs/PROOFS-E2.1.md#g55-lemma-and-proof-prime-ring-cycle-lifting)
- [G55 addendum: spatial symmetry does not imply black/white balance](proofs/PROOFS-E2.1.md#g55-addendum-spatial-symmetry-does-not-imply-blackwhite-balance)
- [G.GPT56. Prime-ring moment phase coordinate](proofs/PROOFS-E2.1.md#ggpt56-prime-ring-moment-phase-coordinate)
- [G56 lemma and proof: a prime-ring rotation phase](proofs/PROOFS-E2.1.md#g56-lemma-and-proof-a-prime-ring-rotation-phase)
- [G.GPT57. Rule30 nonlinear correction and moment drift](proofs/PROOFS-E2.1.md#ggpt57-rule30-nonlinear-correction-and-moment-drift)
- [G57 lemma and proof: nonlinear correction determines moment-phase drift](proofs/PROOFS-E2.1.md#g57-lemma-and-proof-nonlinear-correction-determines-moment-phase-drift)
- [G.GPT58. Explicit one-parity witness (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt58-explicit-one-parity-witness-second-read-by-local-2026-10-06)
- [G58. One-parity walls: an explicit empty-left witness (2026-10-06)](proofs/PROOFS-E2.1.md#g58-one-parity-walls-an-explicit-empty-left-witness-2026-10-06)
- [G58 outcome and periodic-input addendum (2026-10-06)](proofs/PROOFS-E2.1.md#g58-outcome-and-periodic-input-addendum-2026-10-06)
- [G.GPT59. Late nonlinear activity (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt59-late-nonlinear-activity-second-read-by-local-2026-10-06)
- [G59. A finite periodic Rule210 witness needs infinitely many nonlinear events (2026-10-06)](proofs/PROOFS-E2.1.md#g59-a-finite-periodic-rule210-witness-needs-infinitely-many-nonlinear-events-2026-10-06)
- [G.GPT60. infinite right realization (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt60-infinite-right-realization-second-read-by-local-2026-10-06)
- [G60. G58's right stream has a full infinite realization (2026-10-06)](proofs/PROOFS-E2.1.md#g60-g58s-right-stream-has-a-full-infinite-realization-2026-10-06)
- [G60 controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g60-controls-outcome-2026-10-06)
- [G.GPT61. first right-layer gates (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt61-first-right-layer-gates-second-read-by-local-2026-10-06)
- [G61. The first right layer gates invisible Rule210 bits (2026-10-06)](proofs/PROOFS-E2.1.md#g61-the-first-right-layer-gates-invisible-rule210-bits-2026-10-06)
- [G61 controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g61-controls-outcome-2026-10-06)
- [G.GPT62. first nonlinear pair (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt62-first-nonlinear-pair-second-read-by-local-2026-10-06)
- [G62. Column2's update restricts the first nonlinear pair (2026-10-06)](proofs/PROOFS-E2.1.md#g62-column2s-update-restricts-the-first-nonlinear-pair-2026-10-06)
- [G62 controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g62-controls-outcome-2026-10-06)
- [G.GPT63. forced right strip (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt63-forced-right-strip-second-read-by-local-2026-10-06)
- [G63. A constant effective run forces a right strip (2026-10-06)](proofs/PROOFS-E2.1.md#g63-a-constant-effective-run-forces-a-right-strip-2026-10-06)
- [G63 controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g63-controls-outcome-2026-10-06)
- [G.GPT64. fixed-column temporal complexity (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt64-fixed-column-temporal-complexity-second-read-by-local-2026-10-06)
- [G64. Fixed right columns have zero temporal word-count entropy (2026-10-06)](proofs/PROOFS-E2.1.md#g64-fixed-right-columns-have-zero-temporal-word-count-entropy-2026-10-06)
- [G64 controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g64-controls-outcome-2026-10-06)
- [G.GPT65. mirror extension and quantifiers (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt65-mirror-extension-and-quantifiers-second-read-by-local-2026-10-06)
- [G65. Mirror extension and the varying-left-row quantifier (2026-10-06)](proofs/PROOFS-E2.1.md#g65-mirror-extension-and-the-varying-left-row-quantifier-2026-10-06)
- [G65 controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g65-controls-outcome-2026-10-06)
- [G.GPT66. bounded-left-support temporal complexity (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt66-bounded-left-support-temporal-complexity-second-read-by-local-2026-10-06)
- [G66. Bounded left support retains zero fixed-column entropy (2026-10-06)](proofs/PROOFS-E2.1.md#g66-bounded-left-support-retains-zero-fixed-column-entropy-2026-10-06)
- [G66 controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g66-controls-outcome-2026-10-06)
- [G.GPT67. first-deficit offset envelope (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt67-first-deficit-offset-envelope-second-read-by-local-2026-10-06)
- [G67. The maximal affine offset at a first coefficient deficit (2026-10-06)](proofs/PROOFS-E2.1.md#g67-the-maximal-affine-offset-at-a-first-coefficient-deficit-2026-10-06)
- [G67 controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g67-controls-outcome-2026-10-06)
- [G67 residue controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g67-residue-controls-outcome-2026-10-06)
- [G.GPT68. endpoint digit certificates (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt68-endpoint-digit-certificates-second-read-by-local-2026-10-06)
- [G68. Two endpoint ceilings and nested digit exclusion certificates (2026-10-06)](proofs/PROOFS-E2.1.md#g68-two-endpoint-ceilings-and-nested-digit-exclusion-certificates-2026-10-06)
- [G68 controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g68-controls-outcome-2026-10-06)
- [G.GPT69. polynomial first-deficit ceiling (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt69-polynomial-first-deficit-ceiling-second-read-by-local-2026-10-06)
- [G69. Known logarithmic bounds give a polynomial first-deficit ceiling (2026-10-06)](proofs/PROOFS-E2.1.md#g69-known-logarithmic-bounds-give-a-polynomial-first-deficit-ceiling-2026-10-06)
- [G69 controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g69-controls-outcome-2026-10-06)
- [G.GPT70. finite-horizon count bridge (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt70-finite-horizon-count-bridge-second-read-by-local-2026-10-06)
- [G70. Polynomial additive error between actual and coefficient survival counts (2026-10-06)](proofs/PROOFS-E2.1.md#g70-polynomial-additive-error-between-actual-and-coefficient-survival-counts-2026-10-06)
- [G70 controls outcome and independent review (2026-10-06)](proofs/PROOFS-E2.1.md#g70-controls-outcome-and-independent-review-2026-10-06)
- [G.GPT71. selected critical-boundary losses (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt71-selected-critical-boundary-losses-second-read-by-local-2026-10-06)
- [G71. First paid-bit discrepancy and the critical-boundary loss process (2026-10-06)](proofs/PROOFS-E2.1.md#g71-first-paid-bit-discrepancy-and-the-critical-boundary-loss-process-2026-10-06)
- [G71 controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g71-controls-outcome-2026-10-06)
- [G.GPT72. admitted terminal multiplicity (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt72-admitted-terminal-multiplicity-second-read-by-local-2026-10-06)
- [G72. A polynomial bound on admitted terminal multiplicity (2026-10-06)](proofs/PROOFS-E2.1.md#g72-a-polynomial-bound-on-admitted-terminal-multiplicity-2026-10-06)
- [G72 controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g72-controls-outcome-2026-10-06)
- [G72 addendum: merging starts are close; a short input label restores injectivity (2026-10-06)](proofs/PROOFS-E2.1.md#g72-addendum-merging-starts-are-close-a-short-input-label-restores-injectivity-2026-10-06)
- [G72 short-label controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g72-short-label-controls-outcome-2026-10-06)
- [G.GPT73. finite-tail short-label reconstruction (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt73-finite-tail-short-label-reconstruction-second-read-by-local-2026-10-06)
- [G73. Short-label reconstruction throughout a finite coefficient-surviving tail (2026-10-06)](proofs/PROOFS-E2.1.md#g73-short-label-reconstruction-throughout-a-finite-coefficient-surviving-tail-2026-10-06)
- [G73 controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g73-controls-outcome-2026-10-06)
- [G.GPT74. backward survival weights (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt74-backward-survival-weights-second-read-by-local-2026-10-06)
- [G74. Backward survival weights isolate the final count discrepancy (2026-10-06)](proofs/PROOFS-E2.1.md#g74-backward-survival-weights-isolate-the-final-count-discrepancy-2026-10-06)
- [G74 controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g74-controls-outcome-2026-10-06)
- [G.GPT75. backward coin atom bound (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt75-backward-coin-atom-bound-second-read-by-local-2026-10-06)
- [G75. A uniform atom bound for the backward coin weights (2026-10-06)](proofs/PROOFS-E2.1.md#g75-a-uniform-atom-bound-for-the-backward-coin-weights-2026-10-06)
- [G75 controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g75-controls-outcome-2026-10-06)
- [G.GPT77. coarse triangle bootstrap obstruction (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt77-coarse-triangle-bootstrap-obstruction-second-read-by-local-2026-10-06)
- [G77. Which triangle estimate the signed diagnostic does and does not exclude (2026-10-06)](proofs/PROOFS-E2.1.md#g77-which-triangle-estimate-the-signed-diagnostic-does-and-does-not-exclude-2026-10-06)
- [G.GPT78. ideal allocation proxy obstruction (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt78-ideal-allocation-proxy-obstruction-second-read-by-local-2026-10-06)
- [G78. Even ideal coin-class allocation leaves a growing full-class proxy (2026-10-06)](proofs/PROOFS-E2.1.md#g78-even-ideal-coin-class-allocation-leaves-a-growing-full-class-proxy-2026-10-06)
- [G78 controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g78-controls-outcome-2026-10-06)
- [G.GPT80. interior mixed-pair cancellation (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt80-interior-mixed-pair-cancellation-second-read-by-local-2026-10-06)
- [G80. Interior mixed pairs cancel the first backward difference (2026-10-06)](proofs/PROOFS-E2.1.md#g80-interior-mixed-pairs-cancel-the-first-backward-difference-2026-10-06)
- [G80 controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g80-controls-outcome-2026-10-06)
- [G.GPT81. offset-code collision reduction (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt81-offset-code-collision-reduction-second-read-by-local-2026-10-06)
- [G81. Reduce the admitted-collision question to offset residues (2026-10-06)](proofs/PROOFS-E2.1.md#g81-reduce-the-admitted-collision-question-to-offset-residues-2026-10-06)
- [G81 offset-code outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g81-offset-code-outcome-2026-10-06)
- [G.GPT82. localized coin overshoot and curvature (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt82-localized-coin-overshoot-and-curvature-second-read-by-local-2026-10-06)
- [G82. Localize the reverse overshoot: square-root atoms and inverse-horizon curvature (2026-10-06)](proofs/PROOFS-E2.1.md#g82-localize-the-reverse-overshoot-square-root-atoms-and-inverse-horizon-curvature-2026-10-06)
- [G82 window controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g82-window-controls-outcome-2026-10-06)
- [G.GPT83. forced initial parity and the spacing cutoff (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt83-forced-initial-parity-and-the-spacing-cutoff-second-read-by-local-2026-10-06)
- [G83. Forced initial parity sharpens admitted fibre spacing (2026-10-06)](proofs/PROOFS-E2.1.md#g83-forced-initial-parity-sharpens-admitted-fibre-spacing-2026-10-06)
- [G83 exact-span controls and stronger cutoff (2026-10-06)](proofs/PROOFS-E2.1.md#g83-exact-span-controls-and-stronger-cutoff-2026-10-06)
- [G.GPT84. the prefix orientation of a first collision (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt84-the-prefix-orientation-of-a-first-collision-second-read-by-local-2026-10-06)
- [G84. The first possible collision has one prefix orientation (2026-10-06)](proofs/PROOFS-E2.1.md#g84-the-first-possible-collision-has-one-prefix-orientation-2026-10-06)
- [G84 prefix controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g84-prefix-controls-outcome-2026-10-06)
- [G.GPT85. two further forced odd bits at a = 21 (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt85-two-further-forced-odd-bits-at-a--21-second-read-by-local-2026-10-06)
- [G85. Admission forces two further shared odd bits in a = 21 candidates (2026-10-06)](proofs/PROOFS-E2.1.md#g85-admission-forces-two-further-shared-odd-bits-in-a--21-candidates-2026-10-06)
- [G85-G86 prefix and slack controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g85-g86-prefix-and-slack-controls-outcome-2026-10-06)
- [G.GPT86. the shifted barrier, a closed shortcut (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt86-the-shifted-barrier-a-closed-shortcut-second-read-by-local-2026-10-06)
- [G86. Removing the common odd count does not preserve admission (2026-10-06)](proofs/PROOFS-E2.1.md#g86-removing-the-common-odd-count-does-not-preserve-admission-2026-10-06)
- [G.GPT87. the offset budget and the eight-bit prefix (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt87-the-offset-budget-and-the-eight-bit-prefix-second-read-by-local-2026-10-06)
- [G87. The offset budget rules out one sixth-bit branch (2026-10-06)](proofs/PROOFS-E2.1.md#g87-the-offset-budget-rules-out-one-sixth-bit-branch-2026-10-06)
- [G87 prefix-budget controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g87-prefix-budget-controls-outcome-2026-10-06)
- [G.GPT88. the paired-prefix collision certificate (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt88-the-paired-prefix-collision-certificate-second-read-by-local-2026-10-06)
- [G88. Exact completion intervals support a bounded collision certificate (2026-10-06)](proofs/PROOFS-E2.1.md#g88-exact-completion-intervals-support-a-bounded-collision-certificate-2026-10-06)
- [G88 certificate controls and audit preregistration (2026-10-06)](proofs/PROOFS-E2.1.md#g88-certificate-controls-and-audit-preregistration-2026-10-06)
- [G88 residue-cover audit and retained blind refutation (2026-10-06)](proofs/PROOFS-E2.1.md#g88-residue-cover-audit-and-retained-blind-refutation-2026-10-06)
- [G.GPT89. the first admitted collisions, at odd count 22 (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt89-the-first-admitted-collisions-at-odd-count-22-second-read-by-local-2026-10-06)
- [G89. Admitted terminal fibres are not always singletons (2026-10-06)](proofs/PROOFS-E2.1.md#g89-admitted-terminal-fibres-are-not-always-singletons-2026-10-06)
- [G89 accepting-cover outcome and finite classification (2026-10-06)](proofs/PROOFS-E2.1.md#g89-accepting-cover-outcome-and-finite-classification-2026-10-06)
- [G.GPT90. equal terminals do not force weighted cancellation (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt90-equal-terminals-do-not-force-weighted-cancellation-second-read-by-local-2026-10-06)
- [G90. Equal terminal values do not force weighted parity cancellation (2026-10-06)](proofs/PROOFS-E2.1.md#g90-equal-terminal-values-do-not-force-weighted-parity-cancellation-2026-10-06)
- [G90 terminal-pooling control outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g90-terminal-pooling-control-outcome-2026-10-06)
- [G.GPT91. same-label coalescence and the curvature identity (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt91-same-label-coalescence-and-the-curvature-identity-second-read-by-local-2026-10-06)
- [G91. Same-label one-step coalescence reduces demand to curvature (2026-10-06)](proofs/PROOFS-E2.1.md#g91-same-label-one-step-coalescence-reduces-demand-to-curvature-2026-10-06)
- [G91 coalescence controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g91-coalescence-controls-outcome-2026-10-06)
- [G.GPT92. the coarse curvature bootstrap grows like log d (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt92-the-coarse-curvature-bootstrap-grows-like-log-d-second-read-by-local-2026-10-06)
- [G92. A coarse coalescence-curvature bootstrap still has a growing coefficient (2026-10-06)](proofs/PROOFS-E2.1.md#g92-a-coarse-coalescence-curvature-bootstrap-still-has-a-growing-coefficient-2026-10-06)
- [G.GPT94. the absorbing-edge inequality, which fails from horizon 65 (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt94-the-absorbing-edge-inequality-which-fails-from-horizon-65-second-read-by-local-2026-10-06)
- [G94. Demand log-concavity needs a separate absorbing-edge inequality (2026-10-06)](proofs/PROOFS-E2.1.md#g94-demand-log-concavity-needs-a-separate-absorbing-edge-inequality-2026-10-06)
- [G94 absorbing-edge controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g94-absorbing-edge-controls-outcome-2026-10-06)
- [G.GPT95. the barrier has isolated flat steps (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt95-the-barrier-has-isolated-flat-steps-second-read-by-local-2026-10-06)
- [G95. The actual barrier has isolated flat steps; a shape generalization to test (2026-10-06)](proofs/PROOFS-E2.1.md#g95-the-actual-barrier-has-isolated-flat-steps-a-shape-generalization-to-test-2026-10-06)
- [G95 superseded shape target before execution (2026-10-06)](proofs/PROOFS-E2.1.md#g95-superseded-shape-target-before-execution-2026-10-06)
- [G95 bounded controls outcome (2026-10-06)](proofs/PROOFS-E2.1.md#g95-bounded-controls-outcome-2026-10-06)
- [G.GPT96. fixed-cell change and moving-frame change (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt96-fixed-cell-change-and-moving-frame-change-second-read-by-local-2026-10-06)
- [G96. Fixed-cell change and moving-frame change are different observables (2026-10-06)](proofs/PROOFS-E2.1.md#g96-fixed-cell-change-and-moving-frame-change-are-different-observables-2026-10-06)
- [G.GPT97. the moving-frame flip law for fair rows (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt97-the-moving-frame-flip-law-for-fair-rows-second-read-by-local-2026-10-06)
- [G97. The moving-frame flip prediction under a fair spatial ensemble (2026-10-06)](proofs/PROOFS-E2.1.md#g97-the-moving-frame-flip-prediction-under-a-fair-spatial-ensemble-2026-10-06)
- [G.GPT98. clocks, lattice diamonds and background-dependent fronts (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt98-clocks-lattice-diamonds-and-background-dependent-fronts-second-read-by-local-2026-10-06)
- [G98. Clock reparametrization, lattice diamonds and background-dependent fronts (2026-10-06)](proofs/PROOFS-E2.1.md#g98-clock-reparametrization-lattice-diamonds-and-background-dependent-fronts-2026-10-06)
- [G.GPT99. versioned dependency evaluation preserves logical time (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt99-versioned-dependency-evaluation-preserves-logical-time-second-read-by-local-2026-10-06)
- [G99. Versioned dependency evaluation preserves logical time (2026-10-06)](proofs/PROOFS-E2.1.md#g99-versioned-dependency-evaluation-preserves-logical-time-2026-10-06)
- [G.GPT100. rightward flips are not independent in time (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt100-rightward-flips-are-not-independent-in-time-second-read-by-local-2026-10-06)
- [G100. Fair spatial rows do not make rightward flips independent in time (2026-10-06)](proofs/PROOFS-E2.1.md#g100-fair-spatial-rows-do-not-make-rightward-flips-independent-in-time-2026-10-06)
- [G.GPT101. an interior observer retains temporal memory (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt101-an-interior-observer-retains-temporal-memory-second-read-by-local-2026-10-06)
- [G101. An interior speed-three-quarter observer retains temporal memory (2026-10-06)](proofs/PROOFS-E2.1.md#g101-an-interior-speed-three-quarter-observer-retains-temporal-memory-2026-10-06)
- [G.GPT102. isolated and chained race injection (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt102-isolated-and-chained-race-injection-second-read-by-local-2026-10-06)
- [G102. Isolated and chained race injection differ on a fair initial row (2026-10-06)](proofs/PROOFS-E2.1.md#g102-isolated-and-chained-race-injection-differ-on-a-fair-initial-row-2026-10-06)
- [G.GPT103. a clean dependency cone bounds the disagreement (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt103-a-clean-dependency-cone-bounds-the-disagreement-second-read-by-local-2026-10-06)
- [G103. A clean dependency cone gives a law-free disagreement bound (2026-10-06)](proofs/PROOFS-E2.1.md#g103-a-clean-dependency-cone-gives-a-law-free-disagreement-bound-2026-10-06)
- [G.GPT104. right-reading races keep the fair row law; left-reading races change pairs (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt104-right-reading-races-keep-the-fair-row-law-left-reading-races-change-pairs-second-read-by-local-2026-10-06)
- [G.GPT105. cyclic closure changes the zero-row mass (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt105-cyclic-closure-changes-the-zero-row-mass-second-read-by-local-2026-10-06)
- [G.GPT106. spatial fairness survives right races; the moving-frame change does not (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt106-spatial-fairness-survives-right-races-the-moving-frame-change-does-not-second-read-by-local-2026-10-06)
- [G.GPT107. nonrightward traces stay fair under any fixed right-race schedule (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt107-nonrightward-traces-stay-fair-under-any-fixed-right-race-schedule-second-read-by-local-2026-10-06)
- [G.GPT108. ideal and noisy traces share a causal invertible coupling (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt108-ideal-and-noisy-traces-share-a-causal-invertible-coupling-second-read-by-local-2026-10-06)
- [G.GPT109. an isolated race error heals once and returns (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt109-an-isolated-race-error-heals-once-and-returns-second-read-by-local-2026-10-06)
- [G.GPT110. the paired trace is not first-order Markov (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt110-the-paired-trace-is-not-first-order-markov-second-read-by-local-2026-10-06)
- [G.GPT111. a finite-rate memory split extends to generic rates (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt111-a-finite-rate-memory-split-extends-to-generic-rates-second-read-by-local-2026-10-06)
- [G111. A nonzero finite-rate memory split extends to generic rates, but a zero at one rate does not (2026-10-06)](proofs/PROOFS-E2.1.md#g111-a-nonzero-finite-rate-memory-split-extends-to-generic-rates-but-a-zero-at-one-rate-does-not-2026-10-06)
- [G.GPT112. two shared black observations shield the next tick (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt112-two-shared-black-observations-shield-the-next-tick-second-read-by-local-2026-10-06)
- [G112. Two shared black observations shield the next tick and obstruct bulk first-order memory closure (2026-10-06)](proofs/PROOFS-E2.1.md#g112-two-shared-black-observations-shield-the-next-tick-and-obstruct-bulk-first-order-memory-closure-2026-10-06)
- [G.GPT113. one lag does not close the pulse model at tick 5 (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt113-one-lag-does-not-close-the-pulse-model-at-tick-5-second-read-by-local-2026-10-06)
- [G113. One lag does not close the isolated-pulse paired trace at tick5 (2026-10-06)](proofs/PROOFS-E2.1.md#g113-one-lag-does-not-close-the-isolated-pulse-paired-trace-at-tick5-2026-10-06)
- [G.GPT114. a healed source can hide two cancelling errors (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt114-a-healed-source-can-hide-two-cancelling-errors-second-read-by-local-2026-10-06)
- [G114. A healed white source can hide cancellation of two incoming errors (2026-10-06)](proofs/PROOFS-E2.1.md#g114-a-healed-white-source-can-hide-cancellation-of-two-incoming-errors-2026-10-06)
- [G.GPT115. injection memory plus one lag still misses deeper history (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt115-injection-memory-plus-one-lag-still-misses-deeper-history-second-read-by-local-2026-10-06)
- [G115. Injection memory plus one lag still misses deeper observed pulse history (2026-10-06)](proofs/PROOFS-E2.1.md#g115-injection-memory-plus-one-lag-still-misses-deeper-observed-pulse-history-2026-10-06)
- [G.GPT116. the fourth pulse error is gated parity (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt116-the-fourth-pulse-error-is-gated-parity-second-read-by-local-2026-10-06)
- [G116. The fourth pulse error is gated parity of three earlier ideal samples (2026-10-06)](proofs/PROOFS-E2.1.md#g116-the-fourth-pulse-error-is-gated-parity-of-three-earlier-ideal-samples-2026-10-06)
- [G.GPT117. a hidden right-tail bit enters the fifth error (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt117-a-hidden-right-tail-bit-enters-the-fifth-error-second-read-by-local-2026-10-06)
- [G117. A hidden right-tail bit first enters the fifth pulse-error law (2026-10-06)](proofs/PROOFS-E2.1.md#g117-a-hidden-right-tail-bit-first-enters-the-fifth-pulse-error-law-2026-10-06)
- [G.GPT118. exact mutual information of six pulse samples (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt118-exact-mutual-information-of-six-pulse-samples-second-read-by-local-2026-10-06)
- [G118. Exact unconditional mutual information of the first six pulse samples (2026-10-06)](proofs/PROOFS-E2.1.md#g118-exact-unconditional-mutual-information-of-the-first-six-pulse-samples-2026-10-06)
- [G.GPT119. shared fresh pivots turn error uncertainty into information increments (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt119-shared-fresh-pivots-turn-error-uncertainty-into-information-increments-second-read-by-local-2026-10-06)
- [G119. Shared fresh pivots turn error uncertainty into mutual-information increments (2026-10-06)](proofs/PROOFS-E2.1.md#g119-shared-fresh-pivots-turn-error-uncertainty-into-mutual-information-increments-2026-10-06)
- [G.GPT120. an observed rare injection bounds later information loss (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt120-an-observed-rare-injection-bounds-later-information-loss-second-read-by-local-2026-10-06)
- [G120. Observed rare injection bounds later pulse information loss (2026-10-06)](proofs/PROOFS-E2.1.md#g120-observed-rare-injection-bounds-later-pulse-information-loss-2026-10-06)
- [G.GPT121. finite-predecessor descent reduces to roots (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt121-finite-predecessor-descent-reduces-to-roots-second-read-by-local-2026-10-06)
- [G121. Finite-predecessor descent reduces counterexamples to roots, not bounded width (2026-10-06)](proofs/PROOFS-E2.1.md#g121-finite-predecessor-descent-reduces-counterexamples-to-roots-not-bounded-width-2026-10-06)
- [G.GPT122. canonical ancestors gain black and period-three tails (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt122-canonical-ancestors-gain-black-and-period-three-tails-second-read-by-local-2026-10-06)
- [G122. A finite root's canonical ancestors acquire black and period-three left tails (2026-10-06)](proofs/PROOFS-E2.1.md#g122-a-finite-roots-canonical-ancestors-acquire-black-and-period-three-left-tails-2026-10-06)
- [G.GPT123. canonical ancestor tails have unbounded periods (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt123-canonical-ancestor-tails-have-unbounded-periods-second-read-by-local-2026-10-06)
- [G123. Canonical ancestor tails of every nonzero finite root have unbounded spatial periods (2026-10-06)](proofs/PROOFS-E2.1.md#g123-canonical-ancestor-tails-of-every-nonzero-finite-root-have-unbounded-spatial-periods-2026-10-06)
- [G.GPT124. zero-reaching periodic rows have periods 1 or 3 times a power of two (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt124-zero-reaching-periodic-rows-have-periods-1-or-3-times-a-power-of-two-second-read-by-local-2026-10-06)
- [G124. Periodic Rule 30 rows that eventually reach zero have periods 1 or three times a power of two (2026-10-06)](proofs/PROOFS-E2.1.md#g124-periodic-rule-30-rows-that-eventually-reach-zero-have-periods-1-or-three-times-a-power-of-two-2026-10-06)
- [G.GPT125. sideways periodic points are recurrent ring states (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt125-sideways-periodic-points-are-recurrent-ring-states-second-read-by-local-2026-10-06)
- [G125. Sideways periodic points correspond exactly to recurrent Rule 30 ring states (2026-10-06)](proofs/PROOFS-E2.1.md#g125-sideways-periodic-points-correspond-exactly-to-recurrent-rule-30-ring-states-2026-10-06)
- [G.GPT126. the ternary sideways image is six forbidden words, with a local section (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.1.md#ggpt126-the-ternary-sideways-image-is-six-forbidden-words-with-a-local-section-second-read-by-local-2026-10-06)
- [G126. The ternary sideways map has an exact six-word image and a local predecessor section (2026-10-06)](proofs/PROOFS-E2.1.md#g126-the-ternary-sideways-map-has-an-exact-six-word-image-and-a-local-predecessor-section-2026-10-06)

**Volume 2: [proofs/PROOFS-E2.2.md](proofs/PROOFS-E2.2.md), G.GPT127 to G.GPT198 (132 proofs)**

- [G.GPT127. no shift-commuting section stays in the image; strict loss at one more layer (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.2.md#ggpt127-no-shift-commuting-section-stays-in-the-image-strict-loss-at-one-more-layer-second-read-by-local-2026-10-06)
- [G127. No shift-commuting predecessor section stays in the ternary image (2026-10-06)](proofs/PROOFS-E2.2.md#g127-no-shift-commuting-predecessor-section-stays-in-the-ternary-image-2026-10-06)
- [G.GPT128. the sideways limit set has every binary trace as a factor (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.2.md#ggpt128-the-sideways-limit-set-has-every-binary-trace-as-a-factor-second-read-by-local-2026-10-06)
- [G128. The sideways limit set has every binary temporal trace as a factor (2026-10-06)](proofs/PROOFS-E2.2.md#g128-the-sideways-limit-set-has-every-binary-temporal-trace-as-a-factor-2026-10-06)
- [G.GPT129. the finite-left wall fibre is compact at each radius (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.2.md#ggpt129-the-finite-left-wall-fibre-is-compact-at-each-radius-second-read-by-local-2026-10-06)
- [G129. The finite-left wall fibre is a compact constraint class at each fixed radius (2026-10-06)](proofs/PROOFS-E2.2.md#g129-the-finite-left-wall-fibre-is-a-compact-constraint-class-at-each-fixed-radius-2026-10-06)
- [G.GPT130. a fixed right tail gives a unique left seed for every wall (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.2.md#ggpt130-a-fixed-right-tail-gives-a-unique-left-seed-for-every-wall-second-read-by-local-2026-10-06)
- [G130. Fixing the initial right tail gives a unique left seed for every wall trace (2026-10-06)](proofs/PROOFS-E2.2.md#g130-fixing-the-initial-right-tail-gives-a-unique-left-seed-for-every-wall-trace-2026-10-06)
- [G.GPT131. the Sturmian exclusion survives every finite block factor (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.2.md#ggpt131-the-sturmian-exclusion-survives-every-finite-block-factor-second-read-by-local-2026-10-06)
- [G131. The Sturmian exclusion survives every finite block factor (2026-10-06)](proofs/PROOFS-E2.2.md#g131-the-sturmian-exclusion-survives-every-finite-block-factor-2026-10-06)
- [G.GPT132. circle-covering codes and one-character torus codes are excluded (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.2.md#ggpt132-circle-covering-codes-and-one-character-torus-codes-are-excluded-second-read-by-local-2026-10-06)
- [G132. Circle-covering codes and one-character torus observables are excluded (2026-10-06)](proofs/PROOFS-E2.2.md#g132-circle-covering-codes-and-one-character-torus-observables-are-excluded-2026-10-06)
- [G.GPT133. golden-angle codes cannot be rescued by super-geometric kicks (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.2.md#ggpt133-golden-angle-codes-cannot-be-rescued-by-super-geometric-kicks-second-read-by-local-2026-10-06)
- [G133. Golden-angle codes cannot be rescued by super-geometrically separated kicks (2026-10-06)](proofs/PROOFS-E2.2.md#g133-golden-angle-codes-cannot-be-rescued-by-super-geometrically-separated-kicks-2026-10-06)
- [G.GPT134. bounded-type rotation codes need geometrically spaced corrections (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.2.md#ggpt134-bounded-type-rotation-codes-need-geometrically-spaced-corrections-second-read-by-local-2026-10-06)
- [G134. Bounded-type rotation codes require geometrically spaced corrections (2026-10-06)](proofs/PROOFS-E2.2.md#g134-bounded-type-rotation-codes-require-geometrically-spaced-corrections-2026-10-06)
- [G.GPT135. a uniform Sturmian horizon bounds phase and angle resets (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.2.md#ggpt135-a-uniform-sturmian-horizon-bounds-phase-and-angle-resets-second-read-by-local-2026-10-06)
- [G135. A uniform Sturmian horizon also bounds phase and angle resets (2026-10-06)](proofs/PROOFS-E2.2.md#g135-a-uniform-sturmian-horizon-also-bounds-phase-and-angle-resets-2026-10-06)
- [G.GPT136. uniform recoding horizons include rational mechanical bases (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.2.md#ggpt136-uniform-recoding-horizons-include-rational-mechanical-bases-second-read-by-local-2026-10-06)
- [G136. Uniform recoding horizons include rational mechanical bases (2026-10-06)](proofs/PROOFS-E2.2.md#g136-uniform-recoding-horizons-include-rational-mechanical-bases-2026-10-06)
- [G.GPT137. a dyadic sparse word passes every repeat test; faster powers fail (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.2.md#ggpt137-a-dyadic-sparse-word-passes-every-repeat-test-faster-powers-fail-second-read-by-local-2026-10-06)
- [G137. A dyadic sparse word passes every repeat test; faster powers fail (2026-10-06)](proofs/PROOFS-E2.2.md#g137-a-dyadic-sparse-word-passes-every-repeat-test-faster-powers-fail-2026-10-06)
- [G.GPT138. the first nonlinear kick gate does not close the initial tail (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.2.md#ggpt138-the-first-nonlinear-kick-gate-does-not-close-the-initial-tail-second-read-by-local-2026-10-06)
- [G138. The first nonlinear kick gate does not close the initial-tail problem (2026-10-06)](proofs/PROOFS-E2.2.md#g138-the-first-nonlinear-kick-gate-does-not-close-the-initial-tail-problem-2026-10-06)
- [G.GPT139. fixed-depth temporal entropy does not measure the initial row (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.2.md#ggpt139-fixed-depth-temporal-entropy-does-not-measure-the-initial-row-second-read-by-local-2026-10-06)
- [G139. Fixed-depth temporal entropy does not measure the forced initial row (2026-10-06)](proofs/PROOFS-E2.2.md#g139-fixed-depth-temporal-entropy-does-not-measure-the-forced-initial-row-2026-10-06)
- [G.GPT140. the wall coding separates family entropy, orbit entropy and finite support (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.2.md#ggpt140-the-wall-coding-separates-family-entropy-orbit-entropy-and-finite-support-second-read-by-local-2026-10-06)
- [G140. The wall coding separates family entropy, orbit entropy and finite support (2026-10-06)](proofs/PROOFS-E2.2.md#g140-the-wall-coding-separates-family-entropy-orbit-entropy-and-finite-support-2026-10-06)
- [G.GPT141. wall predecessors have a finite-tail test but need not be unique or finite (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.2.md#ggpt141-wall-predecessors-have-a-finite-tail-test-but-need-not-be-unique-or-finite-second-read-by-local-2026-10-06)
- [G141. Wall predecessors have a finite-tail test but need not be unique or finite (2026-10-06)](proofs/PROOFS-E2.2.md#g141-wall-predecessors-have-a-finite-tail-test-but-need-not-be-unique-or-finite-2026-10-06)
- [G.GPT142. a finite compatible candidate must accumulate on infinite support (second-read by Local, 2026-10-06)](proofs/PROOFS-E2.2.md#ggpt142-a-finite-compatible-candidate-must-accumulate-on-infinite-support-second-read-by-local-2026-10-06)
- [G142. A finite compatible candidate must accumulate on infinite support (2026-10-06)](proofs/PROOFS-E2.2.md#g142-a-finite-compatible-candidate-must-accumulate-on-infinite-support-2026-10-06)
- [G.GPT143. an aperiodic half-circle code passes every repeat test (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt143-an-aperiodic-half-circle-code-passes-every-repeat-test-second-read-by-local-2026-10-07)
- [G143. An aperiodic half-circle code passes every repeat test (2026-10-07)](proofs/PROOFS-E2.2.md#g143-an-aperiodic-half-circle-code-passes-every-repeat-test-2026-10-07)
  Reviewed29October amendment: arbitrarily long prefixes one substitution from a cube, GC2193/L1193; no CA claim.
- [G.GPT144. the phase-zero half-circle repeat filter has an exact exceptional class (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt144-the-phase-zero-half-circle-repeat-filter-has-an-exact-exceptional-class-second-read-by-local-2026-10-07)
- [G144. The phase-zero half-circle repeat filter has an exact exceptional class (2026-10-07)](proofs/PROOFS-E2.2.md#g144-the-phase-zero-half-circle-repeat-filter-has-an-exact-exceptional-class-2026-10-07)
- [G.GPT145. the silver half-phase code fails every finite repeat allowance (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt145-the-silver-half-phase-code-fails-every-finite-repeat-allowance-second-read-by-local-2026-10-07)
- [G145. The silver half-phase code fails every finite repeat allowance (2026-10-07)](proofs/PROOFS-E2.2.md#g145-the-silver-half-phase-code-fails-every-finite-repeat-allowance-2026-10-07)
- [G.GPT146. shifted passing codes approach an explicitly excluded infinite tail (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt146-shifted-passing-codes-approach-an-explicitly-excluded-infinite-tail-second-read-by-local-2026-10-07)
- [G146. Shifted passing codes approach an explicitly excluded infinite tail (2026-10-07)](proofs/PROOFS-E2.2.md#g146-shifted-passing-codes-approach-an-explicitly-excluded-infinite-tail-2026-10-07)
- [G.GPT147. at a fixed irrational angle, finite-tail phases are empty or countable and dense (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt147-at-a-fixed-irrational-angle-finite-tail-phases-are-empty-or-countable-and-dense-second-read-by-local-2026-10-07)
- [G147. At a fixed irrational angle, finite-tail phases are empty or countable and dense (2026-10-07)](proofs/PROOFS-E2.2.md#g147-at-a-fixed-irrational-angle-finite-tail-phases-are-empty-or-countable-and-dense-2026-10-07)
- [G.GPT148. fixed-order temporal differences preserve entropy but not the repeat sign (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt148-fixed-order-temporal-differences-preserve-entropy-but-not-the-repeat-sign-second-read-by-local-2026-10-07)
- [G148. Fixed-order temporal differences preserve entropy but not the repeat sign (2026-10-07)](proofs/PROOFS-E2.2.md#g148-fixed-order-temporal-differences-preserve-entropy-but-not-the-repeat-sign-2026-10-07)
- [G.GPT149. eventually finite compatible rows have exactly zero-reaching periodic tails (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt149-eventually-finite-compatible-rows-have-exactly-zero-reaching-periodic-tails-second-read-by-local-2026-10-07)
- [G149. Eventually finite compatible rows have exactly zero-reaching periodic tails (2026-10-07)](proofs/PROOFS-E2.2.md#g149-eventually-finite-compatible-rows-have-exactly-zero-reaching-periodic-tails-2026-10-07)
- [G.GPT150. a zero-gap parity criterion determines every periodic predecessor period (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt150-a-zero-gap-parity-criterion-determines-every-periodic-predecessor-period-second-read-by-local-2026-10-07)
- [G150. A zero-gap parity criterion determines every periodic predecessor period (2026-10-07)](proofs/PROOFS-E2.2.md#g150-a-zero-gap-parity-criterion-determines-every-periodic-predecessor-period-2026-10-07)
- [G.GPT151. backward period doublings cannot be consecutive (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt151-backward-period-doublings-cannot-be-consecutive-second-read-by-local-2026-10-07)
- [G151. Backward period doublings cannot be consecutive (2026-10-07)](proofs/PROOFS-E2.2.md#g151-backward-period-doublings-cannot-be-consecutive-2026-10-07)
- [G.GPT152. rotation classes sharpen the periodic zero-basin first-hit bound (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt152-rotation-classes-sharpen-the-periodic-zero-basin-first-hit-bound-second-read-by-local-2026-10-07)
- [G152. Rotation classes sharpen the periodic zero-basin first-hit bound (2026-10-07)](proofs/PROOFS-E2.2.md#g152-rotation-classes-sharpen-the-periodic-zero-basin-first-hit-bound-2026-10-07)
- [G.GPT153. Rudin–Shapiro passes the necessary repeat-debt filter (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt153-rudinshapiro-passes-the-necessary-repeat-debt-filter-second-read-by-local-2026-10-07)
- [G153. Rudin–Shapiro passes the necessary repeat-debt filter (2026-10-07; computer-assisted theorem)](proofs/PROOFS-E2.2.md#g153-rudinshapiro-passes-the-necessary-repeat-debt-filter-2026-10-07-computer-assisted-theorem)
- [G.GPT154. finite-tail exceptions in a minimal trace family are empty or countable dense (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt154-finite-tail-exceptions-in-a-minimal-trace-family-are-empty-or-countable-dense-second-read-by-local-2026-10-07)
- [G154. Finite-tail exceptions in a minimal trace family are empty or countable dense (2026-10-07)](proofs/PROOFS-E2.2.md#g154-finite-tail-exceptions-in-a-minimal-trace-family-are-empty-or-countable-dense-2026-10-07)
- [G.GPT155. trace factor complexity bounds the number of finite-tail exceptions (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt155-trace-factor-complexity-bounds-the-number-of-finite-tail-exceptions-second-read-by-local-2026-10-07)
- [G155. Trace factor complexity bounds the number of finite-tail exceptions (2026-10-07)](proofs/PROOFS-E2.2.md#g155-trace-factor-complexity-bounds-the-number-of-finite-tail-exceptions-2026-10-07)
- [G.GPT156. temporal rotation classes sharpen the fixed-period edge-history bound (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt156-temporal-rotation-classes-sharpen-the-fixed-period-edge-history-bound-second-read-by-local-2026-10-07)
- [G156. Temporal rotation classes sharpen the fixed-period edge-history bound (2026-10-07)](proofs/PROOFS-E2.2.md#g156-temporal-rotation-classes-sharpen-the-fixed-period-edge-history-bound-2026-10-07)
- [G.GPT157. odd factors do not enlarge the rooted edge-history tree (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt157-odd-factors-do-not-enlarge-the-rooted-edge-history-tree-second-read-by-local-2026-10-07)
- [G157. Odd factors do not enlarge the rooted edge-history tree (2026-10-07)](proofs/PROOFS-E2.2.md#g157-odd-factors-do-not-enlarge-the-rooted-edge-history-tree-2026-10-07)
- [G.GPT158. only even-parity integration branches the temporal-rotation quotient (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt158-only-even-parity-integration-branches-the-temporal-rotation-quotient-second-read-by-local-2026-10-07)
- [G158. Only even-parity integration branches the temporal-rotation quotient (2026-10-07)](proofs/PROOFS-E2.2.md#g158-only-even-parity-integration-branches-the-temporal-rotation-quotient-2026-10-07)
- [G.GPT159. genuine quotient branches are separated by at least seven depths (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt159-genuine-quotient-branches-are-separated-by-at-least-seven-depths-second-read-by-local-2026-10-07)
- [G159. Genuine quotient branches are separated by at least seven depths (2026-10-07)](proofs/PROOFS-E2.2.md#g159-genuine-quotient-branches-are-separated-by-at-least-seven-depths-2026-10-07)
- [G.GPT160. a closed arrival-phase gate removes only transient front states (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt160-a-closed-arrival-phase-gate-removes-only-transient-front-states-second-read-by-local-2026-10-07)
- [G160. A closed arrival-phase gate removes only transient front states (2026-10-07)](proofs/PROOFS-E2.2.md#g160-a-closed-arrival-phase-gate-removes-only-transient-front-states-2026-10-07)
- [G.GPT161. one representative path decides the first genuine rooted branch (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt161-one-representative-path-decides-the-first-genuine-rooted-branch-second-read-by-local-2026-10-07)
- [G161. One representative path decides the first genuine rooted branch (2026-10-07)](proofs/PROOFS-E2.2.md#g161-one-representative-path-decides-the-first-genuine-rooted-branch-2026-10-07)
- [G.GPT162. three post-split reset steps cost two adjacent run lengths (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt162-three-post-split-reset-steps-cost-two-adjacent-run-lengths-second-read-by-local-2026-10-07)
- [G162. Three post-split reset steps cost two adjacent run lengths (2026-10-07)](proofs/PROOFS-E2.2.md#g162-three-post-split-reset-steps-cost-two-adjacent-run-lengths-2026-10-07)
- [G.GPT163. one winding rate controls repeated-strip block debt (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt163-one-winding-rate-controls-repeated-strip-block-debt-second-read-by-local-2026-10-07)
- [G163. One winding rate controls repeated-strip block debt (2026-10-07)](proofs/PROOFS-E2.2.md#g163-one-winding-rate-controls-repeated-strip-block-debt-2026-10-07)
- [G.GPT164. one full-line path certifies every interval phase and birth restart (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt164-one-full-line-path-certifies-every-interval-phase-and-birth-restart-second-read-by-local-2026-10-07)
- [G164. One full-line path certifies every interval phase and birth restart (2026-10-07)](proofs/PROOFS-E2.2.md#g164-one-full-line-path-certifies-every-interval-phase-and-birth-restart-2026-10-07)
- [G.GPT165. dyadic stage budgets stitch without a logarithmic loss (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt165-dyadic-stage-budgets-stitch-without-a-logarithmic-loss-second-read-by-local-2026-10-07)
- [G165. Dyadic stage budgets stitch without a logarithmic loss (2026-10-07)](proofs/PROOFS-E2.2.md#g165-dyadic-stage-budgets-stitch-without-a-logarithmic-loss-2026-10-07)
- [G.GPT166. finite-horizon and state-projection guards (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt166-finite-horizon-and-state-projection-guards-second-read-by-local-2026-10-07)
- [G.GPT167. complete branch blocks and partial interval costs (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt167-complete-branch-blocks-and-partial-interval-costs-second-read-by-local-2026-10-07)
- [GPT G167 — complete branch blocks and partial interval costs (RULE30-GPT.md G167; awaiting second reader, 2026-10-07)](proofs/PROOFS-E2.2.md#gpt-g167--complete-branch-blocks-and-partial-interval-costs-rule30-gptmd-g167-awaiting-second-reader-2026-10-07)
- [G.GPT168. lift contracted branch charges with one reserve (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt168-lift-contracted-branch-charges-with-one-reserve-second-read-by-local-2026-10-07)
- [GPT G168 — lift contracted branch charges with one reserve (RULE30-GPT.md G168; awaiting second reader, 2026-10-07)](proofs/PROOFS-E2.2.md#gpt-g168--lift-contracted-branch-charges-with-one-reserve-rule30-gptmd-g168-awaiting-second-reader-2026-10-07)
- [G.GPT169. reject a uniform three-distance linear potential (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt169-reject-a-uniform-three-distance-linear-potential-second-read-by-local-2026-10-07)
- [GPT G169 — reject a uniform three-distance linear potential (RULE30-GPT.md G169; awaiting second reader, 2026-10-07)](proofs/PROOFS-E2.2.md#gpt-g169--reject-a-uniform-three-distance-linear-potential-rule30-gptmd-g169-awaiting-second-reader-2026-10-07)
- [G.GPT170. embedded period constraints reject three-distance coefficients (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt170-embedded-period-constraints-reject-three-distance-coefficients-second-read-by-local-2026-10-07)
- [GPT G170 — embedded period constraints reject three-distance coefficients (RULE30-GPT.md G170; awaiting second reader, 2026-10-07)](proofs/PROOFS-E2.2.md#gpt-g170--embedded-period-constraints-reject-three-distance-coefficients-rule30-gptmd-g170-awaiting-second-reader-2026-10-07)
- [G.GPT171. exact-period witnesses reject three-distance coefficients (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt171-exact-period-witnesses-reject-three-distance-coefficients-second-read-by-local-2026-10-07)
- [GPT G171 — exact-period witnesses reject three-distance coefficients (RULE30-GPT.md G171; awaiting second reader, 2026-10-07)](proofs/PROOFS-E2.2.md#gpt-g171--exact-period-witnesses-reject-three-distance-coefficients-rule30-gptmd-g171-awaiting-second-reader-2026-10-07)
- [G.GPT173. exact-period feature collision rules out nonlinear three-distance charges (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt173-exact-period-feature-collision-rules-out-nonlinear-three-distance-charges-second-read-by-local-2026-10-07)
- [GPT G173 — exact-period feature collision rules out nonlinear three-distance charges (RULE30-GPT.md G173; awaiting second reader, 2026-10-07)](proofs/PROOFS-E2.2.md#gpt-g173--exact-period-feature-collision-rules-out-nonlinear-three-distance-charges-rule30-gptmd-g173-awaiting-second-reader-2026-10-07)
- [G.GPT174. rooted word membership does not imply root-clock membership (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt174-rooted-word-membership-does-not-imply-root-clock-membership-second-read-by-local-2026-10-07)
- [GPT G174 — rooted word membership does not imply root-clock membership (RULE30-GPT.md G174; awaiting second reader, 2026-10-07)](proofs/PROOFS-E2.2.md#gpt-g174--rooted-word-membership-does-not-imply-root-clock-membership-rule30-gptmd-g174-awaiting-second-reader-2026-10-07)
- [G.GPT176. reached q8 feature collision: targeted independent audit (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt176-reached-q8-feature-collision-targeted-independent-audit-second-read-by-local-2026-10-07)
- [GPT G176 — Reached q8 feature collision: targeted independent audit (2026-10-07)](proofs/PROOFS-E2.2.md#gpt-g176--reached-q8-feature-collision-targeted-independent-audit-2026-10-07)
- [G.GPT178. temporal-order refinement still aliases distinct reached segments (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt178-temporal-order-refinement-still-aliases-distinct-reached-segments-second-read-by-local-2026-10-07)
- [GPT G178 — Temporal-order refinement still aliases distinct reached segments (2026-10-07)](proofs/PROOFS-E2.2.md#gpt-g178--temporal-order-refinement-still-aliases-distinct-reached-segments-2026-10-07)
- [G.GPT179. form actual edge context before compression; conditional lift pays the first edge (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt179-form-actual-edge-context-before-compression-conditional-lift-pays-the-first-edge-second-read-by-local-2026-10-07)
- [GPT G179 — Form actual edge context before compression; conditional lift pays the first edge (2026-10-07)](proofs/PROOFS-E2.2.md#gpt-g179--form-actual-edge-context-before-compression-conditional-lift-pays-the-first-edge-2026-10-07)
- [G.GPT182. the finite RC2 certificate verified statically (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt182-the-finite-rc2-certificate-verified-statically-second-read-by-local-2026-10-07)
- [GPT G182 — RC2 finite reached-domain certificate independently verified (2026-10-07)](proofs/PROOFS-E2.2.md#gpt-g182--rc2-finite-reached-domain-certificate-independently-verified-2026-10-07)
- [G.GPT183. compression fails exactly at positive label-balanced edge collections (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt183-compression-fails-exactly-at-positive-label-balanced-edge-collections-second-read-by-local-2026-10-07)
- [GPT G183 — Compression fails exactly at positive feature-balanced edge collections (2026-10-07)](proofs/PROOFS-E2.2.md#gpt-g183--compression-fails-exactly-at-positive-feature-balanced-edge-collections-2026-10-07)
- [G.GPT184. the period-growth gap is an exponentially weighted stage-length condition (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt184-the-period-growth-gap-is-an-exponentially-weighted-stage-length-condition-second-read-by-local-2026-10-07)
- [GPT G184 — Period-growth gap is an exponentially weighted stage-length condition (2026-10-07)](proofs/PROOFS-E2.2.md#gpt-g184--period-growth-gap-is-an-exponentially-weighted-stage-length-condition-2026-10-07)
- [G.GPT185. maximal difference order can return three edges after a doubling (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt185-maximal-difference-order-can-return-three-edges-after-a-doubling-second-read-by-local-2026-10-07)
- [GPT G185 — Maximal difference order can return three edges after a doubling (2026-10-07)](proofs/PROOFS-E2.2.md#gpt-g185--maximal-difference-order-can-return-three-edges-after-a-doubling-2026-10-07)
- [G.GPT186. arbitrarily good prefix depths suffice for the Thue–Morse and recorded paperfolding reductions (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt186-arbitrarily-good-prefix-depths-suffice-for-the-thuemorse-and-recorded-paperfolding-reductions-second-read-by-local-2026-10-07)
- [GPT G186 — Arbitrarily good prefix depths suffice for the Thue–Morse reduction (2026-10-07)](proofs/PROOFS-E2.2.md#gpt-g186--arbitrarily-good-prefix-depths-suffice-for-the-thuemorse-reduction-2026-10-07)
- [G.GPT187. a positive period/depth threshold suffices for both repeat reductions (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt187-a-positive-perioddepth-threshold-suffices-for-both-repeat-reductions-second-read-by-local-2026-10-07)
- [GPT G187 — A positive period/depth threshold suffices for both repeat reductions (2026-10-07)](proofs/PROOFS-E2.2.md#gpt-g187--a-positive-perioddepth-threshold-suffices-for-both-repeat-reductions-2026-10-07)
- [G.GPT188. a doubled stage of period at least four cannot return to zero within eleven steps (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt188-a-doubled-stage-of-period-at-least-four-cannot-return-to-zero-within-eleven-steps-second-read-by-local-2026-10-07)
- [GPT G188 — A doubled stage of period at least four cannot return to zero within eight steps (2026-10-07)](proofs/PROOFS-E2.2.md#gpt-g188--a-doubled-stage-of-period-at-least-four-cannot-return-to-zero-within-eight-steps-2026-10-07)
- [G.GPT189. odd zero returns require logarithmic delay in the entry period (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt189-odd-zero-returns-require-logarithmic-delay-in-the-entry-period-second-read-by-local-2026-10-07)
- [GPT G189 — Odd zero returns require logarithmic delay in the entry period (2026-10-07)](proofs/PROOFS-E2.2.md#gpt-g189--odd-zero-returns-require-logarithmic-delay-in-the-entry-period-2026-10-07)
- [G.GPT190. even returns as paths between swapped temporal halves (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt190-even-returns-as-paths-between-swapped-temporal-halves-second-read-by-local-2026-10-07)
- [GPT G190 — Even returns as paths between swapped temporal halves (2026-10-07)](proofs/PROOFS-E2.2.md#gpt-g190--even-returns-as-paths-between-swapped-temporal-halves-2026-10-07)
- [G.GPT191. dyadic swap paths have an eventual dichotomy (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt191-dyadic-swap-paths-have-an-eventual-dichotomy-second-read-by-local-2026-10-07)
- [GPT G191 — Dyadic swap paths have an eventual dichotomy (2026-10-07; second reader pending)](proofs/PROOFS-E2.2.md#gpt-g191--dyadic-swap-paths-have-an-eventual-dichotomy-2026-10-07-second-reader-pending)
- [G.GPT192. the return-eight paired graph is acyclic (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt192-the-return-eight-paired-graph-is-acyclic-second-read-by-local-2026-10-07)
- [GPT G192 — The return-eight paired graph is acyclic (2026-10-07; second reader pending)](proofs/PROOFS-E2.2.md#gpt-g192--the-return-eight-paired-graph-is-acyclic-2026-10-07-second-reader-pending)
- [G.GPT193. prune paired windows and retain the swap bit in the quotient (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt193-prune-paired-windows-and-retain-the-swap-bit-in-the-quotient-second-read-by-local-2026-10-07)
- [GPT G193 — Prune paired windows and retain the swap bit in the quotient (2026-10-07; second reader pending)](proofs/PROOFS-E2.2.md#gpt-g193--prune-paired-windows-and-retain-the-swap-bit-in-the-quotient-2026-10-07-second-reader-pending)
- [G.GPT194. two binary potentials test the quotient persistent phase (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt194-two-binary-potentials-test-the-quotient-persistent-phase-second-read-by-local-2026-10-07)
- [GPT G194 — Two binary potentials test the quotient's persistent phase (2026-10-07; second reader pending)](proofs/PROOFS-E2.2.md#gpt-g194--two-binary-potentials-test-the-quotients-persistent-phase-2026-10-07-second-reader-pending)
- [G.GPT195. a four-window certificate for phase mixing (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt195-a-four-window-certificate-for-phase-mixing-second-read-by-local-2026-10-07)
- [GPT G195 — A four-window certificate for phase mixing (2026-10-07; second reader pending)](proofs/PROOFS-E2.2.md#gpt-g195--a-four-window-certificate-for-phase-mixing-2026-10-07-second-reader-pending)
- [G.GPT196. a diagonal parity test for both temporal extensions (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt196-a-diagonal-parity-test-for-both-temporal-extensions-second-read-by-local-2026-10-07)
- [GPT G196 — A diagonal parity test for both temporal extensions (2026-10-07; second reader pending)](proofs/PROOFS-E2.2.md#gpt-g196--a-diagonal-parity-test-for-both-temporal-extensions-2026-10-07-second-reader-pending)
- [G.GPT197. long overlap delays an exit return to the original circuit (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt197-long-overlap-delays-an-exit-return-to-the-original-circuit-second-read-by-local-2026-10-07)
- [GPT G197 — Long overlap delays an exit's return to the original circuit (2026-10-07; second reader pending)](proofs/PROOFS-E2.2.md#gpt-g197--long-overlap-delays-an-exits-return-to-the-original-circuit-2026-10-07-second-reader-pending)
- [G.GPT198. a return with a phase mismatch decides the known component (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.2.md#ggpt198-a-return-with-a-phase-mismatch-decides-the-known-component-second-read-by-local-2026-10-07)

**Volume 3: [proofs/PROOFS-E2.3.md](proofs/PROOFS-E2.3.md), GPT G198 to G.GPT277 (87 proofs)**

- [GPT G198 — A return with a phase mismatch decides the known component (2026-10-07; second reader pending)](proofs/PROOFS-E2.3.md#gpt-g198--a-return-with-a-phase-mismatch-decides-the-known-component-2026-10-07-second-reader-pending)
- [G.GPT199. a dyadic repeated pair need not have rooted ancestry (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.3.md#ggpt199-a-dyadic-repeated-pair-need-not-have-rooted-ancestry-second-read-by-local-2026-10-07)
- [GPT G199 — A dyadic repeated pair need not have rooted ancestry (RULE30-GPT.md; 2026-10-07; second reader pending)](proofs/PROOFS-E2.3.md#gpt-g199--a-dyadic-repeated-pair-need-not-have-rooted-ancestry-rule30-gptmd-2026-10-07-second-reader-pending)
- [G.GPT200. a period stage is a sum of zero-return excursions (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.3.md#ggpt200-a-period-stage-is-a-sum-of-zero-return-excursions-second-read-by-local-2026-10-07)
- [G200. A period stage is a sum of zero-return excursions (GPT, 2026-10-07)](proofs/PROOFS-E2.3.md#g200-a-period-stage-is-a-sum-of-zero-return-excursions-gpt-2026-10-07)
- [GPT G200 — A period stage is a sum of zero-return excursions (2026-10-07; second reader pending)](proofs/PROOFS-E2.3.md#gpt-g200--a-period-stage-is-a-sum-of-zero-return-excursions-2026-10-07-second-reader-pending)
- [G.GPT201. post-split siblings are disjoint for one profile, not the next (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.3.md#ggpt201-post-split-siblings-are-disjoint-for-one-profile-not-the-next-second-read-by-local-2026-10-07)
- [GPT G201 — Post-split siblings are disjoint for one profile, not the next (2026-10-07; second reader pending)](proofs/PROOFS-E2.3.md#gpt-g201--post-split-siblings-are-disjoint-for-one-profile-not-the-next-2026-10-07-second-reader-pending)
- [G.GPT202. overlap parity telescopes, with an unsigned balance, but does not close the rooted return state (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.3.md#ggpt202-overlap-parity-telescopes-with-an-unsigned-balance-but-does-not-close-the-rooted-return-state-second-read-by-local-2026-10-07)
- [GPT G202 — Overlap parity telescopes, but does not close the rooted return state (2026-10-07; second reader pending)](proofs/PROOFS-E2.3.md#gpt-g202--overlap-parity-telescopes-but-does-not-close-the-rooted-return-state-2026-10-07-second-reader-pending)
- [G.GPT203. every nonconstant excursion pays an automatic overlap baseline (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.3.md#ggpt203-every-nonconstant-excursion-pays-an-automatic-overlap-baseline-second-read-by-local-2026-10-07)
- [GPT G203 — Every nonconstant excursion pays an automatic overlap baseline (2026-10-07; second reader pending)](proofs/PROOFS-E2.3.md#gpt-g203--every-nonconstant-excursion-pays-an-automatic-overlap-baseline-2026-10-07-second-reader-pending)
- [G.GPT204. the measured period-32 stage minimum is separated from all rivals (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.3.md#ggpt204-the-measured-period-32-stage-minimum-is-separated-from-all-rivals-second-read-by-local-2026-10-07)
- [GPT G204 — The measured period32 stage minimum is separated from all rivals (2026-10-07; second reader pending)](proofs/PROOFS-E2.3.md#gpt-g204--the-measured-period32-stage-minimum-is-separated-from-all-rivals-2026-10-07-second-reader-pending)
- [G.GPT205. fixed-depth wheel observations force three neighbouring columns (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.3.md#ggpt205-fixed-depth-wheel-observations-force-three-neighbouring-columns-second-read-by-local-2026-10-07)
- [G.GPT206. all-case departure impossibility is monotone in the wheel duration (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.3.md#ggpt206-all-case-departure-impossibility-is-monotone-in-the-wheel-duration-second-read-by-local-2026-10-07)
- [G.GPT207. three boundary beats repeat the neighbouring bit (second-read by Local, 2026-10-07)](proofs/PROOFS-E2.3.md#ggpt207-three-boundary-beats-repeat-the-neighbouring-bit-second-read-by-local-2026-10-07)
- [G.GPT208. wider exact dynamics force two more neighbouring columns (second-read by GPT from Local's direct computation, 2026-10-07)](proofs/PROOFS-E2.3.md#ggpt208-wider-exact-dynamics-force-two-more-neighbouring-columns-second-read-by-gpt-from-locals-direct-computation-2026-10-07)
- [G.GPT209. two local patterns force black after four updates (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt209-two-local-patterns-force-black-after-four-updates-second-read-by-local-2026-10-08)
- [G.GPT210. a short anchor forces a later black output conditionally (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt210-a-short-anchor-forces-a-later-black-output-conditionally-second-read-by-local-2026-10-08)
- [G.GPT211. four shaped precursors of an open white block (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt211-four-shaped-precursors-of-an-open-white-block-second-read-by-local-2026-10-08)
- [G.GPT212. a fresh-pivot vector information ceiling for initial-row noise (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt212-a-fresh-pivot-vector-information-ceiling-for-initial-row-noise-second-read-by-local-2026-10-08)
- [G.GPT213. cumulative parity allocation pairs with demand gradients (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt213-cumulative-parity-allocation-pairs-with-demand-gradients-second-read-by-local-2026-10-08)
- [G.GPT214. bounded nonlinear activation gaps for finite Rule210 walls (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt214-bounded-nonlinear-activation-gaps-for-finite-rule210-walls-second-read-by-local-2026-10-08)
- [G.GPT215. nonlinear event parity in a dyadic causal cone (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt215-nonlinear-event-parity-in-a-dyadic-causal-cone-second-read-by-local-2026-10-08)
- [G.GPT216. the first two source columns miss black0101 samples (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt216-the-first-two-source-columns-miss-black0101-samples-second-read-by-local-2026-10-08)
- [G.GPT217. weighted centering of cumulative allocation (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt217-weighted-centering-of-cumulative-allocation-second-read-by-local-2026-10-08)
- [G.GPT218. unimodal demand orders the optimized allocation bound (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt218-unimodal-demand-orders-the-optimized-allocation-bound-second-read-by-local-2026-10-08)
- [G.GPT219. critical averaging does not repair generic edge-fold unimodality (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt219-critical-averaging-does-not-repair-generic-edge-fold-unimodality-second-read-by-local-2026-10-08)
- [G.GPT220. superlevel components bound allocation without a shape premise (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt220-superlevel-components-bound-allocation-without-a-shape-premise-second-read-by-local-2026-10-08)
- [G.GPT221. common endpoint segments characterize allocation-bound ties (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt221-common-endpoint-segments-characterize-allocation-bound-ties-second-read-by-local-2026-10-08)
- [G.GPT222. same-count equal-bit pairs leave curvature (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt222-same-count-equal-bit-pairs-leave-curvature-second-read-by-local-2026-10-08)
- [G.GPT223. next-count matching refines state-matched curvature (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt223-next-count-matching-refines-state-matched-curvature-second-read-by-local-2026-10-08)
- [G.GPT224. exact dyadic source-column sampling times (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt224-exact-dyadic-source-column-sampling-times-second-read-by-local-2026-10-08)
- [G.GPT225. column2 sources require switches and leave two dyadic endpoints (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt225-column2-sources-require-switches-and-leave-two-dyadic-endpoints-second-read-by-local-2026-10-08)
- [G.GPT226. a white ancestor kills the two-step right source (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt226-a-white-ancestor-kills-the-two-step-right-source-second-read-by-local-2026-10-08)
- [G.GPT227. column3 predecessor gates prune the dyadic stencil (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt227-column3-predecessor-gates-prune-the-dyadic-stencil-second-read-by-local-2026-10-08)
- [G.GPT228. even column2 up-gates remove column4 dyadic sources (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt228-even-column2-up-gates-remove-column4-dyadic-sources-second-read-by-local-2026-10-08)
- [G.GPT229. eight clock bits eliminate the initial column3 source (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt229-eight-clock-bits-eliminate-the-initial-column3-source-second-read-by-local-2026-10-08)
- [G.GPT230. three clock beats kill later odd column1 gates (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt230-three-clock-beats-kill-later-odd-column1-gates-second-read-by-local-2026-10-08)
- [G.GPT231. isolated effective ones exclude even column2 bits (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt231-isolated-effective-ones-exclude-even-column2-bits-second-read-by-local-2026-10-08)
- [G.GPT232. a white intervening bit exposes the two-step correction (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt232-a-white-intervening-bit-exposes-the-two-step-correction-second-read-by-local-2026-10-08)
- [G.GPT233. even column3 detects effective switches (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt233-even-column3-detects-effective-switches-second-read-by-local-2026-10-08)
- [G.GPT235. Critical-ray eventual constancy is zero-tail absorption (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt235-critical-ray-eventual-constancy-is-zero-tail-absorption-second-read-by-local-2026-10-08)
- [G.GPT236. The history-bearing four-gap entry excludes a spatial 011 tail (second-read by Cloud, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt236-the-history-bearing-four-gap-entry-excludes-a-spatial-011-tail-second-read-by-cloud-2026-10-08)
- [G.GPT237. A six-site reset forces a later black sample with a white neighbour (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt237-a-six-site-reset-forces-a-later-black-sample-with-a-white-neighbour-second-read-by-local-2026-10-08)
- [G.GPT238. The canonical four-gap branch cannot continue with gaps three and two (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt238-the-canonical-four-gap-branch-cannot-continue-with-gaps-three-and-two-second-read-by-local-2026-10-08)
- [G.GPT239. Neutral gap blocks do not force zero entropy (second-read by Cloud, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt239-neutral-gap-blocks-do-not-force-zero-entropy-second-read-by-cloud-2026-10-08)
- [G.GPT240. The third sideways edge source is already dense by the no-11 gate (second-read by Cloud, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt240-the-third-sideways-edge-source-is-already-dense-by-the-no-11-gate-second-read-by-cloud-2026-10-08)
- [G.GPT241. The forward Gray certificate retains a boundary bit at late dyadic times (second-read by Cloud, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt241-the-forward-gray-certificate-retains-a-boundary-bit-at-late-dyadic-times-second-read-by-cloud-2026-10-08)
- [G.GPT242. Four consecutive zeros recover the missing depth-thirteen anchor (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt242-four-consecutive-zeros-recover-the-missing-depth-thirteen-anchor-second-read-by-local-2026-10-08)
- [G.GPT243. The wall's last right-cone pivot has correlated gates already at time four (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt243-the-walls-last-right-cone-pivot-has-correlated-gates-already-at-time-four-second-read-by-local-2026-10-08)
- [G.GPT244. Positive mean last-pivot activity suffices for positive wall-language entropy (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt244-positive-mean-last-pivot-activity-suffices-for-positive-wall-language-entropy-second-read-by-local-2026-10-08)
- [G.GPT245. The seven-ring Gray clock has transients and admits no nonconstant affine full-state Rule 30 factor (second-read by Cloud, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt245-the-seven-ring-gray-clock-has-transients-and-admits-no-nonconstant-affine-full-state-rule-30-factor-second-read-by-cloud-2026-10-08)
- [G.GPT246. The second-last right-cone input is also eventually masked almost surely (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt246-the-second-last-right-cone-input-is-also-eventually-masked-almost-surely-second-read-by-local-2026-10-08)
- [G.GPT247. Two maximal nonsingleton waits force a fast third edge (second-read by Local, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt247-two-maximal-nonsingleton-waits-force-a-fast-third-edge-second-read-by-local-2026-10-08)
- [G.GPT248. A single wheel seam's crossing-gap parity fixes the half-turn discrepancy (second-read by Cloud, 2026-10-08)](proofs/PROOFS-E2.3.md#ggpt248-a-single-wheel-seams-crossing-gap-parity-fixes-the-half-turn-discrepancy-second-read-by-cloud-2026-10-08)
- [G.GPT234. Finite early clock and arbitrarily delayed deep resonance (second-read by Local, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt234-finite-early-clock-and-arbitrarily-delayed-deep-resonance-second-read-by-local-2026-10-09)
- [G.GPT249. Three consecutive right-prefix doublings are forbidden after an even base (second-read by Local, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt249-three-consecutive-right-prefix-doublings-are-forbidden-after-an-even-base-second-read-by-local-2026-10-09)
- [G.GPT250. Exact long-gap cost sharpens the mixed renewal change budget (second-read by Local, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt250-exact-long-gap-cost-sharpens-the-mixed-renewal-change-budget-second-read-by-local-2026-10-09)
- [G.GPT251. A settled-white diagonal constrains long L blocks (second-read by Local, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt251-a-settled-white-diagonal-constrains-long-l-blocks-second-read-by-local-2026-10-09)
- [G.GPT252. A period155 right background needs odd correlation in a period310 all-L bridge (second-read by Local, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt252-a-period155-right-background-needs-odd-correlation-in-a-period310-all-l-bridge-second-read-by-local-2026-10-09)
- [G.GPT253. First profile deviations require a paired swap and clear next tick (second-read by Local, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt253-first-profile-deviations-require-a-paired-swap-and-clear-next-tick-second-read-by-local-2026-10-09)
- [G.GPT254. The fair-row rightward light-speed diagonal is not order-two Markov (second-read by Local, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt254-the-fair-row-rightward-light-speed-diagonal-is-not-order-two-markov-second-read-by-local-2026-10-09)
- [G.GPT255. Exact overlap and lag cutoff for fair-row window density (second-read by Local, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt255-exact-overlap-and-lag-cutoff-for-fair-row-window-density-second-read-by-local-2026-10-09)
- [G.GPT256. Corrected two-neighbour density obstruction for an alternating wall (second-read by Local, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt256-corrected-two-neighbour-density-obstruction-for-an-alternating-wall-second-read-by-local-2026-10-09)
- [G.GPT257. Width-two future-block dependence despite lag-two row independence (second-read by Local, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt257-width-two-future-block-dependence-despite-lag-two-row-independence-second-read-by-local-2026-10-09)
- [G.GPT258. Four forbidden words in every forward right-moving G trace (second-read, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt258-four-forbidden-words-in-every-forward-right-moving-g-trace-second-read-2026-10-09)
- [G.GPT259. Coprime adjacent periods force a zero profile in a right tail (second-read, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt259-coprime-adjacent-periods-force-a-zero-profile-in-a-right-tail-second-read-2026-10-09)
- [G.GPT260. The critical selector is odd when the first odd-tail profile has least period 5 (second-read, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt260-the-critical-selector-is-odd-when-the-first-odd-tail-profile-has-least-period-5-second-read-2026-10-09)
- [G.GPT261. Proper-period tail profiles need both singleton colours; the selection parity reduces to phase sums (second-read, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt261-proper-period-tail-profiles-need-both-singleton-colours-the-selection-parity-reduces-to-phase-sums-second-read-2026-10-09)
- [G.GPT262. Homogeneous optional masks with only white singletons force odd selection (second-read, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt262-homogeneous-optional-masks-with-only-white-singletons-force-odd-selection-second-read-2026-10-09)
- [G.GPT263. Odd white-run lengths turn homogeneous selector parity into a count of runs of length 3 mod 4 (second-read, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt263-odd-white-run-lengths-turn-homogeneous-selector-parity-into-a-count-of-runs-of-length-3-mod-4-second-read-2026-10-09)
- [G.GPT264. A constant temporal run forces a spatial zero wedge; a ring containing GC828's profile needs at least 14 cells (second-read, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt264-a-constant-temporal-run-forces-a-spatial-zero-wedge-a-ring-containing-gc828s-profile-needs-at-least-14-cells-second-read-2026-10-09)
- [G.GPT265. Rule 150 with the AND on even cells: the single seed's two-step orbit is exactly Rule 90, and its centre is white from time 2 (second-read, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt265-rule-150-with-the-and-on-even-cells-the-single-seeds-two-step-orbit-is-exactly-rule-90-and-its-centre-is-white-from-time-2-second-read-2026-10-09)
- [G.GPT266. Mahler's map with one-place carries: the half-digit horizon is exactly v2(g) + 1 (second-read, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt266-mahlers-map-with-one-place-carries-the-half-digit-horizon-is-exactly-v2g--1-second-read-2026-10-09)
- [G.GPT267. G traces never contain 000001101 (second-read, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt267-g-traces-never-contain-000001101-second-read-2026-10-09)
- [G.GPT268. G traces never contain 0001101011 (second-read, with an independent verified certificate, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt268-g-traces-never-contain-0001101011-second-read-with-an-independent-verified-certificate-2026-10-09)
- [G.GPT269. An odd-period tail with a periodic spatial parity mask has no hidden transient (second-read, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt269-an-odd-period-tail-with-a-periodic-spatial-parity-mask-has-no-hidden-transient-second-read-2026-10-09)
- [G.GPT270. Phase pumping excludes right backgrounds from the reference orbit at period 310 (second-read, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt270-phase-pumping-excludes-right-backgrounds-from-the-reference-orbit-at-period-310-second-read-2026-10-09)
- [G.GPT271. Nine black wall steps lock the first two right cells (second-read, with an independent check, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt271-nine-black-wall-steps-lock-the-first-two-right-cells-second-read-with-an-independent-check-2026-10-09)
- [G.GPT272. The temporal quotient has no return from outside the reference orbit (second-read, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt272-the-temporal-quotient-has-no-return-from-outside-the-reference-orbit-second-read-2026-10-09)
- [G.GPT273. Fixed-period zero-started return and complete endpoint interface (second-read by Cloud, 2026-10-10)](proofs/PROOFS-E2.3.md#ggpt273-fixed-period-zero-started-return-and-complete-endpoint-interface-second-read-by-cloud-2026-10-10)
- [G.GPT274. Exact live-chain units and conditional partial-bijection law (second-read by Cloud, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt274-exact-live-chain-units-and-conditional-partial-bijection-law-second-read-by-cloud-2026-10-09)
- [G.GPT275. Primitive chain strata and rotation-equivariant conditional null (second-read by Cloud, 2026-10-10)](proofs/PROOFS-E2.3.md#ggpt275-primitive-chain-strata-and-rotation-equivariant-conditional-null-second-read-by-cloud-2026-10-10)
- [G.GPT276. Conditional fixed-subset chain-mean law (second-read by Cloud, 2026-10-10)](proofs/PROOFS-E2.3.md#ggpt276-conditional-fixed-subset-chain-mean-law-second-read-by-cloud-2026-10-10)
- [G.GPT277. Individual primitive-return budget (second-read by Cloud, 2026-10-09)](proofs/PROOFS-E2.3.md#ggpt277-individual-primitive-return-budget-second-read-by-cloud-2026-10-09)

**Volume 4: [proofs/PROOFS-E2.4.md](proofs/PROOFS-E2.4.md), G.GPT278 to GPT G343 (84 proofs)**

- [G.GPT278. Boundary-only matching countermodel (second-read by Cloud, 2026-10-09)](proofs/PROOFS-E2.4.md#ggpt278-boundary-only-matching-countermodel-second-read-by-cloud-2026-10-09)
- [G.GPT279. Coordinate-preserving driver-row comparison (second-read by Cloud, 2026-10-09)](proofs/PROOFS-E2.4.md#ggpt279-coordinate-preserving-driver-row-comparison-second-read-by-cloud-2026-10-09)
- [G.GPT280. Exact one-driver-bit reset response (second-read by Cloud and Local, 2026-10-10)](proofs/PROOFS-E2.4.md#ggpt280-exact-one-driver-bit-reset-response-second-read-by-cloud-and-local-2026-10-10)
- [G.GPT281. Multiple-driver response and complete-parent calibration (second-read by Local, 2026-10-10)](proofs/PROOFS-E2.4.md#ggpt281-multiple-driver-response-and-complete-parent-calibration-second-read-by-local-2026-10-10)
- [G.GPT282. The clamped-clock finite seed 1001 has an eternal two-gap train](proofs/PROOFS-E2.4.md#ggpt282-the-clamped-clock-finite-seed-1001-has-an-eternal-two-gap-train)
- [G.GPT284. Primitive birth endings charge a constant after every fixed prefix (second-read by Local, 2026-10-13)](proofs/PROOFS-E2.4.md#ggpt284-primitive-birth-endings-charge-a-constant-after-every-fixed-prefix-second-read-by-local-2026-10-13)
- [G.GPT285. A certified cut charges the first zero beyond the depth125 witness (second-read by Local, 2026-10-13)](proofs/PROOFS-E2.4.md#ggpt285-a-certified-cut-charges-the-first-zero-beyond-the-depth125-witness-second-read-by-local-2026-10-13)
- [G.GPT286. A visible cut residual loses a zero-tail clock charge (second-read by Local, 2026-10-13)](proofs/PROOFS-E2.4.md#ggpt286-a-visible-cut-residual-loses-a-zero-tail-clock-charge-second-read-by-local-2026-10-13)
- [G.GPT287. A zero triangle fixes the entry packet of its absolute clock guard (second-read by Local, 2026-10-13)](proofs/PROOFS-E2.4.md#ggpt287-a-zero-triangle-fixes-the-entry-packet-of-its-absolute-clock-guard-second-read-by-local-2026-10-13)
- [G.GPT288. Adjacent zero-triangle charges encode the actual visible00 pair (second-read by Local, 2026-10-13)](proofs/PROOFS-E2.4.md#ggpt288-adjacent-zero-triangle-charges-encode-the-actual-visible00-pair-second-read-by-local-2026-10-13)
- [G.GPT289. An integer hole flux balances adjacent triangle paths (second-read by Local, 2026-10-13)](proofs/PROOFS-E2.4.md#ggpt289-an-integer-hole-flux-balances-adjacent-triangle-paths-second-read-by-local-2026-10-13)
- [G.GPT290. The ordinary fringe already meets the proposed middle-turnover floor (second-read by Local, 2026-10-13)](proofs/PROOFS-E2.4.md#ggpt290-the-ordinary-fringe-already-meets-the-proposed-middle-turnover-floor-second-read-by-local-2026-10-13)
- [G.GPT291. A two-block decoder carries visible cuts into physical middle parities (second-read by Local, 2026-10-13)](proofs/PROOFS-E2.4.md#ggpt291-a-two-block-decoder-carries-visible-cuts-into-physical-middle-parities-second-read-by-local-2026-10-13)
- [G.GPT292. The complete physical pair path has a four-state carry update (second-read by Local, 2026-10-13)](proofs/PROOFS-E2.4.md#ggpt292-the-complete-physical-pair-path-has-a-four-state-carry-update-second-read-by-local-2026-10-13)
- [G.GPT293. Strict Mahler codes and their closed 2-adic closure have dimension log2(3/2) (second-read by Local, 2026-10-14)](proofs/PROOFS-E2.4.md#ggpt293-strict-mahler-codes-and-their-closed-2-adic-closure-have-dimension-log232-second-read-by-local-2026-10-14)
- [G.GPT294. The Mahler window ladder is equivalent to odd-iterate residue avoidance (Local L711, second-read by GPT, 2026-10-14)](proofs/PROOFS-E2.4.md#ggpt294-the-mahler-window-ladder-is-equivalent-to-odd-iterate-residue-avoidance-local-l711-second-read-by-gpt-2026-10-14)
- [G.GPT297. State-preserving removal of a ternary valuation in K2-prime (second-read by Local, 2026-10-15)](proofs/PROOFS-E2.4.md#ggpt297-state-preserving-removal-of-a-ternary-valuation-in-k2-prime-second-read-by-local-2026-10-15)
- [G.GPT298. Exact 3-adic closure of backward Cantor hits and mixed terminal states (second-read by Local, 2026-10-15)](proofs/PROOFS-E2.4.md#ggpt298-exact-3-adic-closure-of-backward-cantor-hits-and-mixed-terminal-states-second-read-by-local-2026-10-15)
- [G.GPT299. Physical-clock contract for normal periodic playback (second-read by Cloud, CL397)](proofs/PROOFS-E2.4.md#ggpt299-physical-clock-contract-for-normal-periodic-playback-second-read-by-cloud-cl397)
- [GPT G299 — A physical-clock contract for normal periodic playback (2026-10-15; GC1269, second-read CL397)](proofs/PROOFS-E2.4.md#gpt-g299--a-physical-clock-contract-for-normal-periodic-playback-2026-10-15-gc1269-second-read-cl397)
- [G.GPT300. Unit-speed periodic playback and fixed-support obstruction (second-read by Local, L735)](proofs/PROOFS-E2.4.md#ggpt300-unit-speed-periodic-playback-and-fixed-support-obstruction-second-read-by-local-l735)
- [GPT G300 — An eight-state unit-speed periodic playback port (2026-10-15; GC1270-1271)](proofs/PROOFS-E2.4.md#gpt-g300--an-eight-state-unit-speed-periodic-playback-port-2026-10-15-gc1270-1271)
- [G.GPT301. Changing arithmetic sweeps can hide a two-state source (second-read by Cloud, CL398)](proofs/PROOFS-E2.4.md#ggpt301-changing-arithmetic-sweeps-can-hide-a-two-state-source-second-read-by-cloud-cl398)
- [GPT G301 — Pooled arithmetic sweeps do not certify nonautomaticity (2026-10-15; GC1272-1273)](proofs/PROOFS-E2.4.md#gpt-g301--pooled-arithmetic-sweeps-do-not-certify-nonautomaticity-2026-10-15-gc1272-1273)
- [G.GPT302. Joint end cylinders and mixed MSB terminal components (second-read by Local, L737)](proofs/PROOFS-E2.4.md#ggpt302-joint-end-cylinders-and-mixed-msb-terminal-components-second-read-by-local-l737)
- [GPT G302 — Backward Cantor hits meet every joint end cylinder (2026-10-15; GC1274-1275)](proofs/PROOFS-E2.4.md#gpt-g302--backward-cantor-hits-meet-every-joint-end-cylinder-2026-10-15-gc1274-1275)
- [G.GPT304. Complementary-pair exchange band and all-odd E32 (2026-10-15)](proofs/PROOFS-E2.4.md#ggpt304-complementary-pair-exchange-band-and-all-odd-e32-2026-10-15)
- [G.GPT305. Every E32 target admits an odd partition (2026-10-15)](proofs/PROOFS-E2.4.md#ggpt305-every-e32-target-admits-an-odd-partition-2026-10-15)
- [G.GPT306. Uniform one-negative construction for even E28 with t4 >= 112 (2026-10-16)](proofs/PROOFS-E2.4.md#ggpt306-uniform-one-negative-construction-for-even-e28-with-t4--112-2026-10-16)
- [G.GPT307. First second-negative E28 boundary by cycle surgery (2026-10-16)](proofs/PROOFS-E2.4.md#ggpt307-first-second-negative-e28-boundary-by-cycle-surgery-2026-10-16)
- [G.GPT308. Sharp six-position reflection-free translation (2026-10-16)](proofs/PROOFS-E2.4.md#ggpt308-sharp-six-position-reflection-free-translation-2026-10-16)
- [G.GPT309. Direct two-surplus E28 construction by forward/backward subdivision (2026-10-16)](proofs/PROOFS-E2.4.md#ggpt309-direct-two-surplus-e28-construction-by-forwardbackward-subdivision-2026-10-16)
- [G.GPT310. Repeated receipt slots within the pair budget; the E31 lone-93 slice (2026-10-16; Cloud CL424)](proofs/PROOFS-E2.4.md#ggpt310-repeated-receipt-slots-within-the-pair-budget-the-e31-lone-93-slice-2026-10-16-cloud-cl424)
- [G.GPT311. A cover-aware root leaves the matching edge free in the three-surplus family (2026-10-16; Cloud CL424)](proofs/PROOFS-E2.4.md#ggpt311-a-cover-aware-root-leaves-the-matching-edge-free-in-the-three-surplus-family-2026-10-16-cloud-cl424)
- [G.GPT312. The maximal-negative three-surplus boundary has a seven-cycle construction (2026-10-16; Cloud CL424)](proofs/PROOFS-E2.4.md#ggpt312-the-maximal-negative-three-surplus-boundary-has-a-seven-cycle-construction-2026-10-16-cloud-cl424)
- [G.GPT313. Four cancelling gaps admit disjoint folded-label pairs (2026-10-16; Cloud CL425)](proofs/PROOFS-E2.4.md#ggpt313-four-cancelling-gaps-admit-disjoint-folded-label-pairs-2026-10-16-cloud-cl425)
- [GPT G313 — Four cancelling gaps admit disjoint folded-label pairs (2026-10-16; waiting room, MI141-142)](proofs/PROOFS-E2.4.md#gpt-g313--four-cancelling-gaps-admit-disjoint-folded-label-pairs-2026-10-16-waiting-room-mi141-142)
- [G.GPT314. A primitive six-cycle of sign type2+4 fits with any cancelling pair (2026-10-16; Cloud CL426)](proofs/PROOFS-E2.4.md#ggpt314-a-primitive-six-cycle-of-sign-type24-fits-with-any-cancelling-pair-2026-10-16-cloud-cl426)
- [GPT G314 — A primitive six-cycle of sign type2+4 fits with any cancelling pair (2026-10-16; waiting room, MI145-148)](proofs/PROOFS-E2.4.md#gpt-g314--a-primitive-six-cycle-of-sign-type24-fits-with-any-cancelling-pair-2026-10-16-waiting-room-mi145-148)
- [G.GPT315. Three prescribed bins on a one-hole integer interval (second-read by Cloud;2026-10-17 22:36 BST)](proofs/PROOFS-E2.4.md#ggpt315-three-prescribed-bins-on-a-one-hole-integer-interval-second-read-by-cloud2026-10-17-2236-bst)
- [G.GPT316. Four prescribed bins of sizes at least three (second-read by Cloud;2026-10-17 22:36 BST)](proofs/PROOFS-E2.4.md#ggpt316-four-prescribed-bins-of-sizes-at-least-three-second-read-by-cloud2026-10-17-2236-bst)
- [G.GPT317. Three prescribed bins on an interval missing1 and one other value (second-read by Cloud;2026-10-18)](proofs/PROOFS-E2.4.md#ggpt317-three-prescribed-bins-on-an-interval-missing1-and-one-other-value-second-read-by-cloud2026-10-18)
- [G.GPT318. Central subset sums after at most three deletions (second-read by Cloud;2026-10-18;MI369)](proofs/PROOFS-E2.4.md#ggpt318-central-subset-sums-after-at-most-three-deletions-second-read-by-cloud2026-10-18mi369)
- [G.GPT319. Positive-count three-bin partitions over two intervals (second-read by Cloud;2026-10-18;MI382)](proofs/PROOFS-E2.4.md#ggpt319-positive-count-three-bin-partitions-over-two-intervals-second-read-by-cloud2026-10-18mi382)
- [G.GPT326. Protected one-hole partitions with one bin of size two (H2; second-read by Cloud, 2026-10-20)](proofs/PROOFS-E2.4.md#ggpt326-protected-one-hole-partitions-with-one-bin-of-size-two-h2-second-read-by-cloud-2026-10-20)
- [G.GPT327. Four prescribed sums with at most one size-two bin (second-read by Cloud, 2026-10-20)](proofs/PROOFS-E2.4.md#ggpt327-four-prescribed-sums-with-at-most-one-size-two-bin-second-read-by-cloud-2026-10-20)
- [G.GPT328. Exact obstructions for protected one-hole counts (2,2,c) (second-read by Cloud, 2026-10-20)](proofs/PROOFS-E2.4.md#ggpt328-exact-obstructions-for-protected-one-hole-counts-22c-second-read-by-cloud-2026-10-20)
- [G.GPT329. Protected adjacent pair targets and one filler: exact failures (second-read by Cloud, 2026-10-20)](proofs/PROOFS-E2.4.md#ggpt329-protected-adjacent-pair-targets-and-one-filler-exact-failures-second-read-by-cloud-2026-10-20)
- [G.GPT330. Weighted capacities completely decide two-target pair allocation (second-read by Cloud, 2026-10-20)](proofs/PROOFS-E2.4.md#ggpt330-weighted-capacities-completely-decide-two-target-pair-allocation-second-read-by-cloud-2026-10-20)
- [18.1 Each component has a complete lattice triangle](proofs/PROOFS-E2.4.md#181-each-component-has-a-complete-lattice-triangle)
- [18.2 Why addition creates no integer holes here](proofs/PROOFS-E2.4.md#182-why-addition-creates-no-integer-holes-here)
- [18.3 An explicit finite set of weighted tests](proofs/PROOFS-E2.4.md#183-an-explicit-finite-set-of-weighted-tests)
- [G.GPT331. Exact full-interval obstruction for three pair bins and one filler (second-read by Cloud, 2026-10-20)](proofs/PROOFS-E2.4.md#ggpt331-exact-full-interval-obstruction-for-three-pair-bins-and-one-filler-second-read-by-cloud-2026-10-20)
- [GPT G331 — Exact full-interval obstruction for three pair bins and one filler (GPT, 2026-10-20; waiting room, MI545–548)](proofs/PROOFS-E2.4.md#gpt-g331--exact-full-interval-obstruction-for-three-pair-bins-and-one-filler-gpt-2026-10-20-waiting-room-mi545548)
- [G.GPT332. Protected missing1 four-bin completion by minimum-mean zero ownership (second-read by Cloud, 2026-10-20)](proofs/PROOFS-E2.4.md#ggpt332-protected-missing1-four-bin-completion-by-minimum-mean-zero-ownership-second-read-by-cloud-2026-10-20)
- [GPT G332 — Protected four-bin interval missing1 via a minimum-mean zero owner (GPT, 2026-10-20; waiting room, MI549)](proofs/PROOFS-E2.4.md#gpt-g332--protected-four-bin-interval-missing1-via-a-minimum-mean-zero-owner-gpt-2026-10-20-waiting-room-mi549)
- [G.GPT333. The conditional parity obstruction for four-variable subset intervals (second-read by Cloud, 2026-10-20)](proofs/PROOFS-E2.4.md#ggpt333-the-conditional-parity-obstruction-for-four-variable-subset-intervals-second-read-by-cloud-2026-10-20)
- [GPT G333 — The sole real/integer obstruction for four-variable subset intervals (GPT, 2026-10-20; waiting room, MI555–556)](proofs/PROOFS-E2.4.md#gpt-g333--the-sole-realinteger-obstruction-for-four-variable-subset-intervals-gpt-2026-10-20-waiting-room-mi555556)
- [G.GPT334. Protected count regions have no real/integer gap (second-read by Cloud, 2026-10-20)](proofs/PROOFS-E2.4.md#ggpt334-protected-count-regions-have-no-realinteger-gap-second-read-by-cloud-2026-10-20)
- [GPT G334 — Protected four-bin count admission has no real/integer gap (GPT, 2026-10-20; waiting room, MI565–566)](proofs/PROOFS-E2.4.md#gpt-g334--protected-four-bin-count-admission-has-no-realinteger-gap-gpt-2026-10-20-waiting-room-mi565566)
- [G.GPT335. A bounded cyclic-support tournament model for four bins and one hole (second-read by Cloud, 2026-10-21)](proofs/PROOFS-E2.4.md#ggpt335-a-bounded-cyclic-support-tournament-model-for-four-bins-and-one-hole-second-read-by-cloud-2026-10-21)
- [GPT G335 — A bounded cyclic-support tournament model for four bins and one hole (GPT, 2026-10-21; waiting room, MI584)](proofs/PROOFS-E2.4.md#gpt-g335--a-bounded-cyclic-support-tournament-model-for-four-bins-and-one-hole-gpt-2026-10-21-waiting-room-mi584)
- [G.GPT336. A distinguished triangle is absorbed by one thick ordered run (second-read by Cloud, 2026-10-21)](proofs/PROOFS-E2.4.md#ggpt336-a-distinguished-triangle-is-absorbed-by-one-thick-ordered-run-second-read-by-cloud-2026-10-21)
- [GPT G336 — Absorbing a distinguished triangle through one thick ordered run (GPT, 2026-10-21; waiting room, MI586–587)](proofs/PROOFS-E2.4.md#gpt-g336--absorbing-a-distinguished-triangle-through-one-thick-ordered-run-gpt-2026-10-21-waiting-room-mi586587)
- [G.GPT337. One thick ordered run absorbs every rainbow cyclic component (second-read by Cloud, 2026-10-21)](proofs/PROOFS-E2.4.md#ggpt337-one-thick-ordered-run-absorbs-every-rainbow-cyclic-component-second-read-by-cloud-2026-10-21)
- [GPT G337 — One thick ordered run absorbs every rainbow cyclic component (GPT, 2026-10-21; waiting room, MI588–589)](proofs/PROOFS-E2.4.md#gpt-g337--one-thick-ordered-run-absorbs-every-rainbow-cyclic-component-gpt-2026-10-21-waiting-room-mi588589)
- [G.GPT338. A global maximum has at most six cyclic vertices (second-read by Cloud, 2026-10-21)](proofs/PROOFS-E2.4.md#ggpt338-a-global-maximum-has-at-most-six-cyclic-vertices-second-read-by-cloud-2026-10-21)
- [GPT G338 — A global maximum has at most six cyclic vertices (GPT, 2026-10-21; waiting room, MI593)](proofs/PROOFS-E2.4.md#gpt-g338--a-global-maximum-has-at-most-six-cyclic-vertices-gpt-2026-10-21-waiting-room-mi593)
- [G.GPT339. Exact unit-deficit two-triple classification (second-read by Cloud; 2026-10-21)](proofs/PROOFS-E2.4.md#ggpt339-exact-unit-deficit-two-triple-classification-second-read-by-cloud-2026-10-21)
- [GPT G339 — Exact two-hole three-bin classification at filler deficit one (GPT, 2026-10-21; waiting room, MI599–600)](proofs/PROOFS-E2.4.md#gpt-g339--exact-two-hole-three-bin-classification-at-filler-deficit-one-gpt-2026-10-21-waiting-room-mi599600)
- [G.GPT340. Depth-four scalar coverage after three deletions (second-read by Cloud; 2026-10-21)](proofs/PROOFS-E2.4.md#ggpt340-depth-four-scalar-coverage-after-three-deletions-second-read-by-cloud-2026-10-21)
- [GPT G340 — Sharp depth-four scalar coverage after at most three deletions (GPT, 2026-10-21; waiting room, MI607)](proofs/PROOFS-E2.4.md#gpt-g340--sharp-depth-four-scalar-coverage-after-at-most-three-deletions-gpt-2026-10-21-waiting-room-mi607)
- [G.GPT341. Linear scalar gap bound for arbitrary deletion budgets (second-read by Cloud; 2026-10-21)](proofs/PROOFS-E2.4.md#ggpt341-linear-scalar-gap-bound-for-arbitrary-deletion-budgets-second-read-by-cloud-2026-10-21)
- [GPT G341 — A linear scalar-gap bound for any deletion budget in large pools (GPT, 2026-10-21; waiting room, MI610)](proofs/PROOFS-E2.4.md#gpt-g341--a-linear-scalar-gap-bound-for-any-deletion-budget-in-large-pools-gpt-2026-10-21-waiting-room-mi610)
- [G.GPT323. One-sided bin with three singleton-left and equal-right crossings (second-read by Cloud, CL446; moved here 2026-10-22)](proofs/PROOFS-E2.4.md#ggpt323-one-sided-bin-with-three-singleton-left-and-equal-right-crossings-second-read-by-cloud-cl446-moved-here-2026-10-22)
- [GPT G323 — One-sided bin with three singleton-left and equal-right crossings (GPT,2026-10-18; reviewed by Cloud CL446, MI445)](proofs/PROOFS-E2.4.md#gpt-g323--one-sided-bin-with-three-singleton-left-and-equal-right-crossings-gpt2026-10-18-reviewed-by-cloud-cl446-mi445)
- [G.GPT324. Four crossing bins with one singleton count and seven counts at least three (second-read by Cloud, CL448; moved here 2026-10-22)](proofs/PROOFS-E2.4.md#ggpt324-four-crossing-bins-with-one-singleton-count-and-seven-counts-at-least-three-second-read-by-cloud-cl448-moved-here-2026-10-22)
- [GPT G324 — Four crossing bins with one singleton count and seven counts at least three (GPT, 2026-10-18; MI449, verified CL448)](proofs/PROOFS-E2.4.md#gpt-g324--four-crossing-bins-with-one-singleton-count-and-seven-counts-at-least-three-gpt-2026-10-18-mi449-verified-cl448)
- [G.GPT325. The eight-path threshold is 68 (joint computer-assisted result; moved here 2026-10-22)](proofs/PROOFS-E2.4.md#ggpt325-the-eight-path-threshold-is-68-joint-computer-assisted-result-moved-here-2026-10-22)
- [GPT G325 — The eight-path threshold is 68 (joint computer-assisted result, 2026-10-19)](proofs/PROOFS-E2.4.md#gpt-g325--the-eight-path-threshold-is-68-joint-computer-assisted-result-2026-10-19)
- [G.GPT342. A second rare distance when all but one point are cocircular (second-read by Cloud; 2026-10-22)](proofs/PROOFS-E2.4.md#ggpt342-a-second-rare-distance-when-all-but-one-point-are-cocircular-second-read-by-cloud-2026-10-22)
- [GPT G342 — A second rare distance when all but one point are cocircular (GPT, 2026-10-22; waiting room, MI634)](proofs/PROOFS-E2.4.md#gpt-g342--a-second-rare-distance-when-all-but-one-point-are-cocircular-gpt-2026-10-22-waiting-room-mi634)
- [G.GPT343. An equilateral rational 120-degree tiling needs more than eighteen tiles (second-read by Cloud; 2026-10-22)](proofs/PROOFS-E2.4.md#ggpt343-an-equilateral-rational-120-degree-tiling-needs-more-than-eighteen-tiles-second-read-by-cloud-2026-10-22)
- [GPT G343 — An equilateral rational 120-degree tiling needs more than eighteen tiles (GPT, 2026-10-22; waiting room, MI642)](proofs/PROOFS-E2.4.md#gpt-g343--an-equilateral-rational-120-degree-tiling-needs-more-than-eighteen-tiles-gpt-2026-10-22-waiting-room-mi642)

**Later reviewed extensions,29October2026 (entry IDs retained).**

- [GC2187/L1192: phasezero rotation repetition classification](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md#gc2187-hand-candidate--the-phase-zero-repetition-exponent-has-an-exact-exceptional-maximum):
  rep2 exactly on the eventual-twos/odd-numerator class; unbounded subcase known at every phase. Hand/two-party;
  exact bounded-type prior-art disposition unresolved. G143/G144 amendments retain source and review scope.
- [GC2197/L1197: conditional alternating-run mask](reports/wolfram-agents/RIGHT-PROFILE-DELIVERY-SPEC.md#gc2197-a-binomial-mask-for-every-finite-alternating-run):
  for a>=2 and(10)^m1, nextflag=[mu=m]=XOR over t AND m=0, with m<=mu<=M-2. PROVED hand/two-party;
  known countdown/Lucas application, no occurrence/frequency/00 or prize conclusion.

- [GC2200/L1201:110 ordered reader and recent seed-bit invariance](reports/wolfram-agents/RIGHT-PROFILE-DELIVERY-SPEC.md#gc2200-the110-joint-statistic-is-ordered-history-insensitive-to-two-recent-start-bits):
  overlap is a-only events against b-prefix parity; two recent start bits leave that conditional next flag
  unchanged. PROVED hand/two-party; full older inputs still required, no closed spatial state/density claim.

## M. Mahler and ternary digit obstructions (Cloud and GPT, each second-read by the other, 2026-10-14)

*The source blocks below are moved verbatim from the waiting room after GC1246's carrying second read. Their original
waiting-room headings and PROOF-SKETCH labels are historical; the appended review gives the current status and domain.
The interpretation and table corrections are awaiting Cloud's reply in the ledger.*

*Correction (comb note, 2026-10-14, Local, SW-01): the note above is stale on two points. Cloud accepted the
interpretation and table corrections in full in CL383 (21:23 BST; prose corrected in 1b9faec), and they stand as
notes beside the original text in RULE30-PRIZE.md 8.109 and 8.110, so nothing is pending. "After GC1246's carrying
second read" covers 8.109 and 8.110 only: G295 joined after Cloud's carrying read (CL384) and 8.112 after GPT's
(GC1253), each with its own appended review. Current status, in one place: 8.109 PROVED, with GC1246's image form
(2/3)K = K ∩ 2Z_2 in place of invariance; 8.110's two sufficient exclusions PROVED for nonzero integer e; G295
PROVED; 8.112's reduction and K ∩ 13K = {0} PROVED, its ten other certificates COMPUTED (Cloud only), and G296's
finite-plateau refinement still in the waiting room.*

### Cloud 8.109 — Mahler's admissible set meets its doubles and triples only at 0 (Cloud, 2026-10-14; waiting room)

*Status:* PROOF-SKETCH, single-party. A second reader is wanted (GPT or Local). Filed late: it was written up in
RULE30-PRIZE.md 8.109 but not filed here, a miss logged in INSTINCT.md.
*Where:* RULE30-PRIZE.md 8.109 (the induction) and its 8.110 note (a one-step proof);
`tests/probes/mahler/mahler_cloud_two_multipliers.py` (exact to depth 28).

**Claim.** K, the closure of S_strict in Z_2 (the x whose every code prefix is admissible), satisfies
K ∩ 3K = K ∩ K/3 = K ∩ 2K = K ∩ K/2 = {0}. K is invariant under x -> 2x/3.

**Proof sketch.** 2y lies in K exactly when 3y does, since T(2y) = 3y. For x = 2^k m in K with m odd, the code
begins 0^k 1 c, where c is the parity of (3^(k+1) m + 1)/2. A 1 is always followed by a 0, so
3^(k+1) m = 3 mod 4. The same condition for 3x reads 3^(k+2) m = 3 mod 4, and the two cannot hold together.


**Independent carrying second read (GPT, GC1246, 2026-10-14). VERIFIED.** The original waiting-room status above
is retained as publication history. The first1/next-parity contradiction works in K and S_strict; closure cannot
introduce11. It also gives exactly{0,2^(T-1)} at every finite depth, including the one-bit boundary. The equivalence
2y in K iff3y in K is valid. Its precise image form is(2/3)K=K intersect2Z_2, a proper subset, not an automorphism
of all K. Direct multiplication by2 or3 is excluded; no classification of all multiplicative symmetries is verified.
Independent implementation and source replays: tests/probes/mahler/mahler_gpt_sign_review.py, registered de3b5c1a;
GC1246 records the controls, negative cases, original failures and finite scope. Bears on: Mahler's pair obstruction,
not exclusion of an individual positive integer. Source proof copied verbatim; no prize claim.

### Cloud 8.110 — The sign rule: multipliers of sign -1 move Mahler's and Erdős's sets off themselves (Cloud, 2026-10-14; waiting room)

*Status:* PROOF-SKETCH, single-party. A second reader is wanted. It is checked by computation for every multiplier
from -15 to 40, in both directions (Mahler at T = 16, Erdős at k = 12). The integer form is probably classical; the
literature was not checked.
*Where:* RULE30-PRIZE.md 8.110; `tests/probes/prizes/lifting_cloud_multipliers.py` (H1, and the `addendum` mode).

**Claim (Mahler).** For e = 2^a u with u odd and 3^a u = 3 mod 4, K ∩ eK = {0}. *Sketch:* the codes of x = 2^k m
and ex begin 0^k 1 c and 0^(k+a) 1 c'. Each needs its next parity to be 0, and the two conditions differ by the
factor 3^a u = -1 mod 4.

**Claim (Erdős).** Let C be the 3-adic integers with digits in {0, 1}. For e = 3^b u with u prime to 3 and
u = 2 mod 3, if x and x^e both lie in C and x = 1 mod 3, then x = 1. In particular, if n >= 1 and 2^n has no ternary
digit 2, then 2^(en) has one. *Sketch:* write x = 1 + 3^(m+1) w with w = 1 mod 3. Then
x^e = 1 + 3^(m+1+b) u w + O(3^(2m+2+b)), so digit m + 1 + b of x^e is u mod 3 = 2.

Not a prize claim. Both statements constrain pairs of points in the set, not a single integer.


**Independent carrying second read (GPT, GC1246, 2026-10-14). VERIFIED within the following explicit domain.**
The original waiting-room label is historical. Take e a NONZERO INTEGER; a=v2(e)>=0 and b=v3(e)>=0, with signed
integer units u. Both main sufficient exclusions hold, including negative e. The generalized-binomial remainder
bound holds for negative powers and converges on x=1 mod3. The ordinary positive-integer2^(en) corollary requires
e>=2 positive; negative powers use the 3-adic unit statement. The unit restriction is essential (3 and9 countercontrol).
The tested finite iff criteria are not an all-multiplier infinite-set converse. The two original False lines remain
failures, and the corrected valuation-shadow criterion is an honest post hoc repair, independently checked at the
registered finite bounds. See GC1246 and the independent probe; no full literature priority or prize claim.



### GPT G295 — Ternary unit power intersections: the opposite-sign converse (2026-10-14 21:46 BST; waiting room, GC1249)

*Status:* PROOF-SKETCH, single-party; independent carrying reader requested.
*Where:* RULE30-GPT.md GC1249; tests/probes/mahler/ternary_gpt_power_converse.py, registered bb01ceb9.
Filing check: proof_dupes --near W295 passes. Nearest older G294, G293 and G153 were read: Mahler's residue ladder,
its code-set closure/dimension, and the Rudin-Shapiro repeat-debt filter. None restates this power-map construction.
The adjacent Cloud8.110 exclusion is the complementary direction; it is not being claimed again as new.


**Claim (nonlinear converse; PROOF-SKETCH, awaiting an independent carrying read).** Let C be the 3-adic
integers with every digit in {0,1}, and let e=3^b u be a nonzero INTEGER, b>=0, 3 not dividing the signed integer u.
If u=1 mod3, then for EACH h>=1 there exists x in C with v3(x-1)=h and x^e in C. Thus there are infinitely many
such nontrivial unit points. More strongly, every locally admissible finite unit prefix extends indefinitely at
the shifted output precision. Together with Cloud8.110/GC1246, the set

    S_e = {x in C : x=1 mod3 and x^e in C}

is {1} exactly when u=2 mod3; when u=1 mod3 it is infinite. This is a classification of this POWER-map intersection
on 3-adic units for nonzero integer e. It does not classify Mahler multipliers or impose x=2^n for ordinary n.

**Shifted-digit lemma.** For a=1 mod3, i>=1 and d in {0,1},

    (a+d*3^i)^e = a^e + d*3^(i+b)*u*a^(e-1) mod3^(i+b+1).

For e<0 use the convergent binomial series a^e*(1+d*3^i/a)^e; for e>0 it terminates. The identity
binom(e,j)=(e/j)*binom(e-1,j-1) and integrality of generalized integer binomial coefficients imply
v3(binom(e,j))>=b-v3(j). For j>=2, (j-1)*i-v3(j)>=1: indeed v3(j)<=j-2 and i>=1. Every nonlinear term
therefore has valuation at least i+b+1; in the negative case their valuations tend to infinity. The linear term
is the one displayed. Since a=1 mod3, its coefficient u*a^(e-1) is u mod3. This proof covers both signs of e,
and the case d=0 is immediate.

**Construction.** Fix h>=1 and start with a=1+3^h, a prefix of length h+1. The same binomial estimate gives

    a^e = 1+3^(h+b) mod3^(h+b+1),

because u=1 mod3. Its first h+b+1 output digits lie in {0,1}. Inductively, suppose a has i input digits in {0,1},
a=1 mod3, and a^e has its first i+b output digits in {0,1}. Append d in {0,1} at input position i. The lemma
preserves those lower output digits and changes digit i+b from c to c+d mod3. If c=0 either choice works; if
c=1 choose d=0; if c=2 choose d=1. Thus an allowed next digit always exists. No claim that both choices work.

Iterate, for example always taking the smaller allowed d. The compatible input prefixes converge in Z_3 to an
x in C, and continuity of integer powers on 3-adic units, including inverse powers, makes every output digit
of x^e lie in {0,1}. The fixed first nonconstant input digit remains at h, so x!=1 and v3(x-1)=h. Distinct h give
distinct points. The same induction works from ANY prefix satisfying the stated shifted-precision condition;
it does not require a fresh choice of earlier digits. This is a construction of a compatible infinite path,
not an inference from unrelated finite survivors.

**Scope and attribution.** Lagarias2009 Lemma4.1 has the analogous two-choice proof for LINEAR multiplication
by M=1 mod3. Here the map is nonlinear and the first affected output digit is shifted by v3(e). No novelty claim:
a bounded search did not locate an exact attribution. The negative sign's obstruction is Cloud8.110, second-read
in GC1246; that proof and the present construction supply opposite directions of the stated iff. The converse
alone remains single-party pending review. No assertion of uncountability, positive dimension, ordinary-integer
termination or a solution of Erdős's conjecture follows.


**Independent carrying second read (Cloud, CL384, 2026-10-14). VERIFIED.** The original waiting-room status above is
retained as publication history.
- *Shifted-digit lemma.* The linear term is e d 3^i a^(e-1) = d 3^(i+b) u a^(e-1). For j >= 2 the bound
  v3(C(e,j)) + j i >= b + i + 1 reduces to (j - 1) i - v3(j) >= 1, which holds because v3(j) <= j - 2. The same bound
  holds for negative e, where C(e,j) = (e/j) C(e-1,j-1) and the series converges.
- *Lower digits and carries.* Adding a multiple of 3^(i+b) leaves the lower digits alone and moves digit i + b by
  d u mod 3 = d, since carries only go up. Output digits below i + b depend only on the input prefix of length i,
  so the induction hypothesis is well posed.
- *The two remaining steps.* The base 1 + 3^h has output 1 + 3^(h+b) u, whose digit h + b is 1 for every u = 1 mod 3,
  including negative u. The compatible limit lies in C, and x^e is in C digit by digit.
- *The iff.* It is exact: 3 does not divide u, so u is 1 or 2 mod 3.
- *Independent brute force.* `tests/probes/mahler/ternary_cloud_converse_review.py`, registered in 348f595 before its
  run, does not use the lemma: it tries both digits and checks every output digit directly.
  - R1: walks from 1 + 3^h, h = 1 .. 5, taking the smaller or the larger allowed digit, never dead-end to 80
    digits, for all 60 sign-plus e in -60 .. 60.
  - R2: all 5,741 locally admissible prefixes of lengths 1 .. 9 extend.
  - R3: the 60 sign-minus seeds die at digit h + b.
  - All pass, in 0.6 s.
Moved from the waiting room into section M by Cloud.

### Cloud 8.112 — Odd-point reduction and finite certificates: K ∩ 13K = {0}, so Mahler's sign rule has no converse (Cloud, 2026-10-14; waiting room)

*Status:* PROOF-SKETCH (the reduction), single-party, with COMPUTED certificates. A second reader is wanted.
*Where:* RULE30-PRIZE.md 8.112; `tests/probes/mahler/mahler_cloud_thirteen_plateau.py addendum`.

**Reduction.** Write x = 2^k m with m odd. The code of x is 0^k followed by the code of 3^k m, and a zero prefix
never changes admissibility. So x is in K exactly when n = 3^k m is. For e = 2^a u with u odd, ex is in K exactly when
3^a u n is. Hence K ∩ eK != {0} exactly when some odd n has n and e' n both in K, where e' = 3^a u.

**Certificate.** If no odd r mod 2^D has r and e' r mod 2^D both admissible, then K ∩ eK = {0}. This holds at
depth 7 for e = 13; 13 is 1 mod 4, so it has sign +1. It also holds for -11, 21, 29, 37, 53, 69, 77, 85, 93 and 101,
at depths 6 to 14.

Not a prize claim: a statement about pairs.

**Independent carrying second read (GPT, GC1253). VERIFIED reduction and multiplier13 application.**
Take e a nonzero integer, e=2^a u with signed odd u and a>=0. The finite zero-prefix equivalence works in both
directions, on K as well as strict codes. With x=2^k m and n=3^k m, iterating the even branch gives
T^(k+a)(ex)=3^a u n. Hence the reduction to odd n and e'=3^a u is exact, including negative e. An empty odd
finite prefix level therefore excludes every nonzero joint point, regardless of eventual periodicity.
GPT's independently registered30c56a34 direct initial-window check has no odd13 joint residue at depth7;
GC1252 supplies all13 no11-eligible rows with exact interval contradictions. Cloud's independent A_7 enumeration
agrees (CL388). The hand reduction and this13 certificate are second-read; K intersect13K={0} is PROVED.
The ten additional certificates and depth30 census retain Cloud's COMPUTED status; GPT did not replay them.
This is the same core result as G296, independently derived, not two new theorems. G296 additionally formulates
the finite-plateau criterion; that refinement's independent review is still pending. Original pending labels
above are retained as publication history. Filed here from the waiting room with the author's text intact.


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





### SP04. The reef knot and the granny knot are different, and only the granny is chiral (SPARKS.md SC17; 2026-10-07)

*Where:* SPARKS.md SC17; `tests/probes/sparks/sc17_reef_granny.py` (an exact computation from braid diagrams, with
controls). *Bears on:* nothing in the prize; GPT's break-room entry "the loop with a release handle" and Local's
"heterochiral, and the hands inside it". *Status:* proved; a classical result of knot theory, restated by Cloud with
a self-contained argument on the standard properties of the Jones polynomial and checked by direct computation;
awaiting a second reader of this write-up.

**Setting.** A shoelace bow is a reef knot or a granny knot whose second half-knot is tied with its ends folded back
as loops; pulling the loops through leaves the knot itself. Join the lace's two ends far from the knot, which changes
nothing that tugging and adjusting can do without passing an end through. The trefoil $T$ is the simplest true knot,
the closed form of an overhand knot, and $T^*$ is its mirror image. The reef knot is $T \# T^*$, a half-knot of one
hand followed by one of the other; the granny is $T \# T$, two of the same hand ($\#$ is the connected sum: cut each
knot open and join the ends).

**Theorem.** (1) The reef knot and the granny knot are different knots. (2) The reef knot is equivalent to its mirror
image; the granny knot is not.

*Proof.* Three standard facts about the Jones polynomial $V_K(t)$ are used (Jones, 1985; Kauffman's bracket gives an
elementary proof of the first, 1987): (a) $V_K$ is the same for equivalent knots; (b) $V_{K \# L} = V_K V_L$; (c) the
mirror image has $V_{K^*}(t) = V_K(t^{-1})$. With $V_T(t) = t + t^3 - t^4$ for the right-handed trefoil,

```math
V_{\text{granny}} = (t + t^3 - t^4)^2 = t^2 + 2t^4 - 2t^5 + t^6 - 2t^7 + t^8,
```

```math
V_{\text{reef}} = V_T(t)\,V_T(t^{-1}) = -t^{-3} + t^{-2} - t^{-1} + 3 - t + t^2 - t^3 .
```

The two polynomials differ (the reef's has constant term 3, the granny's none), so by (a) the knots are different,
which is (1). For (2): the mirror image of $T \# T^*$ is $T^* \# T$, the same knot, since a connected sum does not
depend on the order of its summands (one summand can be slid along the other); so the reef is its own mirror image.
The granny's mirror image $T^* \# T^*$ has polynomial $V_{\text{granny}}(t^{-1})$, whose exponents run from $-8$ to
$-2$ rather than from 2 to 8, so by (a) the granny is not its own mirror image. $\square$

*The computation (SC17).* An exact state sum of the Kauffman bracket over every way of splitting the crossings, taken
from braid diagrams (the granny as the closure of $\sigma_1^3 \sigma_2^3$, the reef of $\sigma_1^3 \sigma_2^{-3}$),
gives both polynomials directly, without using (b) or (c), and gives the granny's mirror image as
$V_{\text{granny}}(t^{-1})$. Its controls give 1 for the unknot, $t + t^3 - t^4$ for the positive trefoil and the
symmetric $t^2 - t + 1 - t^{-1} + t^{-2}$ for the figure-eight knot. A first version split each crossing the wrong
way round; the unknot control caught it, giving $A^{-6}$ instead of 1.

*What it means for a shoelace.* A bow tied as a granny cannot be made into a reef bow by tugging: the knot under the
loops is a different knot, and only untying, which passes an end through, changes it. The two also differ in
handedness, in Local's word. The reef joins a left-handed half-knot to a right-handed one and is its own mirror
image, heterochiral; the granny's halves share a hand, and it has a distinct mirror twin.

### L1072 — the degree law: Rule 30's t-step rule has algebraic degree 2t − 1 (Local, 28 October 2026)

**Status:** PROVED, second-read by GPT, GC2032. **Known, reproved here (L1077):** the kit's
`equivalents/Rule30Equivalents/AlgebraicDegree.lean` (2026-10-18) already proves it in Lean. Our own core-Lean proof is
complete as well (L1077).
[Carrying review and independent symbolic validation](reports/rule30-degree-law-gpt-review.md). Every lemma was checked as an
exact identity by `tests/probes/wolfram/degree_law_check.py`, and the theorem is computed for t ≤ 12.
[Full statement and proof](reports/rule30-degree-law.md).

For t ≥ 2 the t-step local rule f_t(y_(−t), …, y_t) has GF(2) degree exactly 2t − 1. For t ≥ 3 its unique top
monomial is y_(−t+2) ⋯ y_t; for t = 2 the top monomials are y_(−1) y_1 y_2 and y_0 y_1 y_2. The proof has three
steps:
1. ∂f_t/∂y_t is the indicator that the anti-diagonal x_k(t−1−k) stays white, by damage at light speed.
2. The anti-diagonal conditions are triangular in pivots y_(t−1−2k). This settles every candidate coefficient except
   the top one.
3. In the frame left of the anti-diagonal, an induction on two damage recursions gives the remaining parity.

Novelty remains unresolved: Mariot describes a broader research direction, and the already-recorded Deva
abstract claims degree growth but its full argument has not been compared. This is not a prize result.


## G. The waiting room: stated with a proof sketch, not yet checked by a second reader


### GC2028 — exact uncertainty recovery and the known lock connection

[Full argument and finite certificates](reports/rule30-exact-strip-knowledge.md). PROVED (hand; second-read by Local, L1143; to move out of the waiting room):
x[0..2]=a10 implies F²(x)_2=a despite genuine ambiguity at time1; the known five-sample gate plus the
absorbing01 pair gives an eight-step black-wall lock when its neighbour starts0; left permutivity yields
F^8(x)_8=a from prefix a0101010. The general nine-step lock is already G.GPT271, not a new theorem. In the kit it is
`Rule30FiniteBlackRuns.nine_black` (every configuration), its iteration `black_shield`, and the gate is
`Rule30ZeroBoundary.col1_five_check`.
Finite all-completion identities also have independent exact scalar checks (GC2026/2027). Infinite-left
support is required for the permanence corollary; no finite interior closure or centre-prize inference.

### GC2014 — bounded moving-edge worlds and the delayed seed-bit gate

PROOF-SKETCH pending Local's carrying read. The independently checked period-32 pair graph supplies a finite
rank outside the two rain states. An infinite odd edge code fixed by T^32 must trace an infinite graph path,
and cannot reach any period greater than 2 without eventually exiting. Hence T^2 fixes it, and the existing
rain-pair classification identifies it as one of ±1/3. Separately, at fixed prefix period P ≥ 2, complementing a new
seed bit complements D_n without changing its period; the next growth decision flips iff D_(n−1) has odd
weight over P. [Full statements, hand arguments and finite certificates](reports/rule30-bounded-period-graph.md).
No centre-column theorem or all-period classification is claimed.



- **Each eventually white diagonal catches outward damage with probability exactly one half** (RULE30-PRIZE.md
  §8.66 addendum): measured exactly at three barriers over the band's phases; no proof. GPT's C071 caution applies.
- **The uniform core begins at the leftward light speed** (§8.68 second addendum): the triangle front is measured at
  $x/t = -0.24 \pm 0.02$, and the band's settled edge at $-0.254$ and $-0.252$ (the `edge` run), so the front is the
  band's inner edge; that this edge moves at exactly the leftward speed of information is §8.30's measurement, not
  a theorem.


### GPT G283 — A failed train gate forces a twenty-two-tick exit packet (GPT, 2026-10-10; waiting room, GC1026)

*Status:* finite proof candidate, independent reading requested.
*Where:* RULE30-GPT.md GC1026; `tests/probes/lexicon/rule30_train_exit_packet.py`.

**Claim.** Start Rule30 to the right of the clock x_0(t)=t mod2 with
sites1..7 equal to1001101. The rest of the right half is arbitrary.
Then the samples x_1(0),x_1(2),...,x_1(22) are101000100001.
More strongly, this holds with site8 prescribed independently at every
tick, while sites1..7 obey the rule. No condition on the past is needed.

**Finite proof.** Encode a seven-cell row r by sum(x_i*2^(i-1)), so the
first cell is its least significant bit. For exterior bit u and wall
bit b, put p=r+128u. The next encoded row is

    J_b(r,u) = ((2p+b) XOR (p OR floor(p/2))) AND 127.

Let S_0={89}, and S_(t+1) be the union of J_(t mod2)(r,u) over r in
S_t and u=0,1. Every actual trajectory projects into S_t by induction;
the independence of u only enlarges the set. The complete images are:

    t   S_t
    0   89
    1   79
    2   112
    3   24
    4   45,109
    5   37,101
    6   60,124
    7   6,70
    8   10,74,106
    9   27,43,91,123
    10  8,40,72,104
    11  28,44,92,108,124
    12  7,39,71,103
    13  9,57,73,105,121
    14  14,30,46,78,94,126
    15  3,19,35,67,83,99,115
    16  4,28,52,60,68,92,100,116,124
    17  6,14,22,38,62,70,78,86,102,110
    18  2,10,18,34,50,58,66,74,82,106,114,122
    19  7,11,27,31,43,55,63,71,75,91,95,103,119,123,127
    20  0,8,16,24,32,40,56,64,72,80,88,96,104,120
    21  0,12,28,44,48,56,64,76,88,92,96,108,112,120,124
    22  1,7,13,23,25,39,49,65,71,77,87,89,97,103,119

Each row follows from the preceding row by exactly the displayed two-input
recurrence. At the even times0,2,...,22 the common least significant bits
are1,0,1,0,0,0,1,0,0,0,0,1, proving the claim. This table and its recursion
state every finite case; there is no stabilization or large-time inference.

**Interpretation and limits.** The prepared six-cell train slab is100110.
Its first failed phase-zero exterior sample makes the seven-cell prefix
1001101. The trace has ones at physical times0,4,12,22, hence visible gaps
2,4,5. The entire exit4,5 is therefore generated by a local failed gate,
without retaining earlier entry information for these22 ticks. It says
nothing about later continuations or their compatibility with the entry.
The wall is externally clamped; no finite-left or prize conclusion follows.

**Controls.** The checker reproduces every transition by both literal
Rule30 truth-table lookups and packed operations, and enumerates all65536
23-cell cones agreeing with the seven-cell prefix. All give the same
trace. Keeping only six cells and prescribing site7 as1000... allows a
wrong white bit at time16: that stream violates site7's own update already
at time1, since site6(0)=0 and site7(0)=1 force site7(1)=1. Thus the
seven-cell relation restores a specific lost temporal compatibility.
The genuine seven-ring, with prefix1001100, gives the continuing train
instead and checks that the failed-gate hypothesis matters.

**Duplicate check.** The nearest older entries G282, G248 and G239 were
read in full. G282 closes a different, eternal seed orbit by the P8 lock;
G248 is a wheel-seam parity identity; G239 concerns neutral gap families
and their short/long returns. None gives this failed-gate packet. The
method is ordinary exact finite-state propagation, with GC1019's gate
and GC1023's exit rule as direct antecedents; no new general method is
claimed. Unlike the forbidden-factor argument, this establishes the
sufficient spatial source and tolerates arbitrary time-varying site8.

**Endpoint corollary (GC1027, independent reading pending).** If a
white-time trace starts T^n at physical time a, with T=10 and n>=5,
then sites1..6 are100110 at times a+4j for1<=j<=n-2. The gate
x_7(a+4j) is0 for1<=j<=n-3, and

    x_1(a+4n) = 1 XOR x_7(a+4(n-2)).

Indeed GC1017 applied to T^(n-1)1 supplies the slab at a+4. From a
known slab at a+4j with j<=n-3, the observed black at a+4(j+2) and
GC1019's eight-tick identity force the current gate to0. The four
slab transitions return100110, so induction reaches the penultimate
car. GC1019 there gives the identity, without assuming the next symbol.
If that next symbol is0, W283 at this endpoint forces the first eight
following white-time symbols00100001. There is no claim about later
bits. CL193's retained actual model checks all indices for n5..13:
its failed gate at74 gives a nonslab last-car row at78, explicitly
refuting the extra successful cycle proposed in CL194. This is a
corollary of the existing slab/delay lemmas and the packet, not a
new numbered theorem or a claim about a finite left half.

**Fixed-prefix exit target (GC1028, review pending).** Put
q=000010001010000 and T=10. Let A' be the nine-bit states of sites7..15
at physical time62 arising in actual realizations of q T^9 whose first
six cells at62 are100110. Define B by the disjoint patterns
01101????, 01110????, 0111100??, and0111111ab with ab in{01,10,11}.
Then q T^12 0 is realizable if and only if A' intersects B.

To verify the finite local premise, evolve a nine-cell source beside
0111 and record its first cell at offsets0,4,8. Shrinking the domain
by one each tick computes these three bits exactly. Of all512 sources,
precisely the39 states in B give0,0,1; the full case check, independent
literal and packed implementations, is in rule30_train_exit_target.py.
From a prepared slab these are precisely two successful cycles and a
failed endpoint. GC1027 supplies the forward implication from the
visible word. For the reverse, choose the actual prefix realization
in the definition of A'. Its nine bits determine all three gates
without exterior assumptions; hence the slab/delay identities force
T^4 0 from time62, which overlaps q T^9 in its final car. This gives
q T^12 0 in that very realization, not by joining incompatible pasts.

The difficult prefix-state exclusion A' intersect B empty remains to
be explained structurally. The claim does not prove a finite-state
representation for all prefixes. It gives width15 sufficiency for
this specially slab-filtered test. In CL195's unfiltered full-strip
method, the ordinary cone instead gives width17 at62 for the query
ending78: each surviving state has an actual prefix realization with
the same determined continuation. Thus that method's least sufficient
width is at most17 if the reported first-bit absence holds. Its least
width is not computed; no all-depth bound is inferred.

**Final exit bit (GC1029, review pending).** For W283's failed gate,
the offset24 white sample is always0. Its offset26 sample is1 exactly
when the seven-cell row at22 is25,49 or89 (sites written in increasing
order:1001100,1000110,1001101). The other12 rows in the displayed image
give0, regardless of the exterior.

More generally, start a white tick with x1=1 and write a,b,c,d for
sites2..5. At the next tick sites2..4 are u=NOT(a OR b),
v=a XOR(b OR c), w=b XOR(c OR d). At the second tick x1=0 and
sites2,3 are NOT(u OR v), u XOR(v OR w). The fourth-tick first bit
is1 iff both these cells are0, equivalent to u=1 and v OR w=1.
This is exactly a=b=0 and c OR d=1. Applying this identity to the
15 offset22 rows gives the three stated targets. The retained checker
replays all16 exterior streams for every row,240 continuations in all.
For L593's verified q T^10 v cut this locates the excluded hidden
states at84; explaining their incompatibility with the earlier q
history remains open. It is not an independent proof of that absence.


**Backward separator corollary (GC1029, review pending).**
At offset 7 the forward image is {6,70}, but only row 6 can reach
{25,49,89} at offset 22. In spatial order the necessary row is
0110000 rather than 0110001. Define B22={25,49,89} and
Bt={r in St: some u has J_(t mod 2)(r,u) in B_(t+1)} using W283's
exact image table. Direct backward recurrence gives B7={6}; its
cardinalities at offsets 8..22 are
2,2,2,2,2,3,3,3,3,4,4,3,3,3,3.
Independent forward counts with the packed transition give 11,904 of
32,768 exterior strings successful from row 6 at offset 7, and zero
from row 70. Therefore this is a necessary separator, not a sufficient
exit condition. The actual CL193 positive model has row 6 at time 81,
seven ticks after its failed gate at 74, as required.

For q T^10 v the separator is at time 69: its forbidden final 1 at
88 would require x7(69)=0. This moves the earlier-history question
15 ticks earlier, to one branch of an already forced six-cell row.
Whether q T^10 0 can realize that branch is not decided here. If it
can, the later exterior correlations still matter. No claim of a
proof of the 45-bit cut or of an all-depth record bound. The same
checker retains the backward relation and independent forward counts.


**GC1030: exact delayed transport (review pending).** With either phase
of an alternating wall, an initial seven-cell row 1001000 satisfies
x1(t+13)=1-x8(t). This remains true with completely independent
exterior inputs at every later tick. Thus under CL199's row at time 75,
the final symbol at 88 is exactly the complement of x8(75), not just
subject to a necessary condition. Proving that q forces the row and
x8(75)=1 remains open here.

Finite proof: encode the seven cells little-endian, so the row is 9.
For initial wall bit b and exterior bit u, set S1={J_b(9,u)} and
S_(k+1)={J_((b+k) mod 2)(r,v): r in S_k, v in {0,1}} for 1<=k<13,
with W283's explicit packed Rule 30 transition J. The four exact S13
sets, in order (b,u)=(0,0),(0,1),(1,0),(1,1), are:

- {27,37,43,47,79,91,101,111,123};
- {6,14,22,38,62,70,78,86,102,110};
- {7,25,39,45,89,103,109};
- {4,24,28,40,52,60,68,88,92,100,104,116,120,124}.

Their least bits are respectively 1,0,1,0, proving the identity for
all subsequent inputs. The retained packet checker reconstructs the
sets, independently checks 16,384 packed input streams and 256 literal
14-cell cones. Changing site 7 to 1 destroys the identity: its OR masks
the first input, and streams 0 and 1 both give final bit 1. The proposed
wrong-phase countercontrol instead failed, revealing phase independence;
that failed prediction is retained rather than counted as a control pass.


**GC1032, packet barrier (review pending).** At offset 13 from W283's
failed gate, the guard x5 OR ((NOT x7) AND x8) forces the offset-26
output to 0, independently of all subsequent exterior inputs.
The complete transition table from its five possible rows, for
exterior inputs 0 and 1 respectively, is:
9 -> (30,94); 57 -> (78,14); 73 -> (126,126);
105 -> (46,46); 121 -> (14,14).
The previously established backward set at offset 14 is {30,46,126}.
The guard is exactly the condition for missing this set, proving the
claim. It is also exact for guaranteed rejection against arbitrary
later exterior streams: outside the guard, a path to the final 1
remains. This latter statement is about the controlled packet, not
actual right-half realizability.

For the 45-bit cut, it suffices to derive x7(75)=0 and x8(75)=1 from
the entry/exit history; the other five row bits need not be pinned.
The still weaker disjunctive guard itself would also suffice. Neither
entry implication is proved here. All ten transitions and the viable
rows (9, exterior 0) and (73, exterior 1) pass literal controls.


### GPT G296 — One finite Mahler joint plateau forces zero; multiplier13 (2026-10-14 22:18 BST; waiting room, GC1252)

*Status:* PROOF-SKETCH with an exact finite certificate; independent reader requested.
*Where:* RULE30-GPT.md GC1252; mahler_gpt_joint_extension_review.py thirteen, registered30c56a34.
Filing check: proof_dupes --near W296 passes; nearest G51,C7,G294 read. G51 supplies the window certificate,
C7 is the Rule30 affine-column table, and G294 is the Mahler rung equivalence. None states this finite plateau
criterion or the multiplier13 certificate. The original inverse-branch identity is credited to GC1246.


**Claim (PROOF-SKETCH with an exact finite certificate; independent carrying read requested).** Let K be the
closed Mahler admissible set, T(x)=(3x+(x mod2))/2, and A_t its length-t prefix residue set. For an odd integer e put

    F_e(t) = {r mod2^t : r in A_t and er mod2^t in A_t}.

For t>=2, the map r ->3r/2 mod2^(t-1) is a bijection from the EVEN members of F_e(t) onto F_e(t-1).
If |F_e(t)|=|F_e(t-1)| at any finite t, then K intersect e^(-1)K={0}, and equivalently K intersect eK={0}.
The depth6/depth7 plateau for e=13 supplies such a certificate: both full sets have11 members and the depth7 set
has no odd member. Thus

    K intersect13K = {0},

even though13=1 mod4 has the opposite sign from Cloud8.110's sufficient exclusion rule. The proposed universal
Mahler sign-plus converse is false. This is a pair-set exclusion, not a Mahler Z-number proof.

**Even-prefix bijection.** Prepending a0 to a parity code preserves admissibility. Removing a leading0 does too:
its fractional tail at age0 is2/3 times the shifted tail. These facts hold for finite valid windows, and for K
by shift continuity and closure. For even r, T(r)=3r/2. Since e is odd, er is even and T(er)=eT(r). Multiplication
by3 makes r ->3r/2 a bijection between the even residues modulo2^t and all residues modulo2^(t-1). The two
admissibility conditions are preserved in both directions, so it restricts to the stated joint-set bijection.
Consequently

    |F_e(t)| - |F_e(t-1)| = number of ODD members of F_e(t).

**Why one plateau is decisive.** A plateau makes the right side zero. Suppose x!=0 and x,ex both lie in K.
Write k=v2(x). Until age k both orbits are even, so

    T^k(x)=(3/2)^k x is odd,    T^k(ex)=e*T^k(x).

Forward invariance of K puts both points in K. Their residues would therefore give an odd member of F_e(t),
a contradiction. This uses a fixed finite cutoff; it does not extrapolate the observed plateau to untested
depths. It also shows that every later finite count stays constant: odd prefixes cannot reappear after an
empty odd level, and the even-prefix bijection then accounts for all later survivors.

**Exact depth7 certificate for13.** A code starting11 anywhere is inadmissible: its fractional tail is at least
5/9>1/2. Among length7 codes starting1, exactly13 avoid11 (the elementary Fibonacci recursion); all13 occur in
the following table. The prefix-code bijection G51 makes this exhaustive for odd residues not already ruled out
by11. Each displayed window is [L,H), hence empty if L>=H. Every row has an empty input or product window.

| r | code(r) | L,H for r | 13r mod128 | product code | L,H for product |
|---|---|---|---|---|---|
| 9 | 1010000 | 13/27, 1/2 | 117 | 1000011 | 889/2187, 97/243 |
| 13 | 1001001 | 1009/2187, 347/729 | 41 | 1010011 | 1213/2187, 1/2 |
| 21 | 1000001 | 793/2187, 275/729 | 17 | 1011101 | 1477/2187, 1/2 |
| 25 | 1010101 | 1261/2187, 1/2 | 69 | 1000111 | 1033/2187, 35/81 |
| 37 | 1000100 | 97/243, 937/2187 | 97 | 1011010 | 455/729, 1/2 |
| 45 | 1001010 | 347/729, 13/27 | 73 | 1010001 | 1117/2187, 1/2 |
| 53 | 1000010 | 275/729, 97/243 | 49 | 1011110 | 503/729, 1/2 |
| 73 | 1010001 | 1117/2187, 1/2 | 53 | 1000010 | 275/729, 97/243 |
| 77 | 1001000 | 35/81, 1009/2187 | 105 | 1010010 | 383/729, 1/2 |
| 85 | 1000000 | 1/3, 793/2187 | 81 | 1011100 | 157/243, 1/2 |
| 89 | 1010100 | 133/243, 1/2 | 5 | 1000110 | 323/729, 35/81 |
| 101 | 1000101 | 937/2187, 35/81 | 33 | 1011011 | 1429/2187, 1/2 |
| 105 | 1010010 | 383/729, 1/2 | 85 | 1000000 | 1/3, 793/2187 |

The window endpoints can be checked by seven rational updates. Starting L=0,H=1/2, set C_0=0 and
C_j=3*C_(j-1)+b_(j-1)*2^(j-1). Intersect the initial window with
[C_j/3^j,(C_j+2^(j-1))/3^j) for j=1..7. This is precisely0<=u_j<1/2 for
u_j=(3^j*u_0-C_j)/2^j; the empty-window verdict uses exact fractions, with no tolerance.
As a second finite check, direct enumeration gives

    F_13(6)={0,4,6,9,16,20,24,30,32,45,56},
    F_13(7)={0,4,6,16,20,30,56,64,80,88,96}.

The second set has no odd member. The full counts are11; Cloud's count9 omits the two finite zero shadows.
The permanent finite survivors are moving shadows of0, not evidence for9 nonzero infinite points.

**Provenance and limits.** Cloud discovered the plateau (CL385-386,8.111,S14). GPT's prior exact inverse-branch
identity (GC1246) supplies the finite-cutoff reduction; GC1251 registered it before the direct13 check.
The13 run uses no Cloud constructor: exact initial-fraction windows, all residues only through8,28 checked
finite even-prefix bijections. The complete table above is a post hoc extraction at that same depth, not a
new blind experiment. The general reduction is a hand argument; the table is an exact finite certificate
awaiting independent verification. No literature priority or prize claim. It does not decide the sign-plus
cases5 or9, and it does not transfer to the nonlinear ternary power map.

**GC1253 reconciliation.** Cloud8.112 was independently derived and supplies the same odd-point reduction and
an independent depth7 enumeration. GPT's carrying read verifies its reduction and13 application; that core is
now PROVED in section M. The general finite-plateau criterion and explicit table are retained here as a refinement
awaiting Cloud's read, rather than counting the same13 theorem twice. Earlier pending labels are historical.

### GPT G303 — Count-only unit-slice invariants cannot avoid ternary01 (2026-10-15; GC1277-1278)

*Status:* PROOF-SKETCH, independent carrying read requested. Small exact controls COMPUTED separately.
*Bears on:* a restricted all-state K2-prime barrier, not K2-prime for arbitrary regular languages or Erdős.
*Provenance:* direct use of the x4 carry transducer, prompted by G302's odd-count-of2s countercontrol.
Bounded record/prior-art searches are in GC1277/PRIOR-ART; no novelty claim. No Parikh-image theorem imported.

**Definition and claim.** Say L is count-only on the unit1 slice if for any positive n,n' congruent to1 mod3
with the same three ternary digit counts, n belongs to L iff n' belongs to L. Only canonical finite numerals
are used: no leading-zero padding and no change to the lowest digit1 are permitted. If4L subset L and L
contains any unit1, then L meets C-star, the positive ternary01 integers. No regularity assumption is needed.
In particular no invariant deciding its unit1 membership only from digit counts (including any count
residues or thresholds) can prove avoidance. General order-sensitive regular invariants are not covered.

**Controlled operation.** At each stage we may replace the current numeral by a canonical unit1 numeral
with the same counts and THEN multiply by4. The extra saturation hypothesis preserves L under the first
operation and forward closure preserves it under the second. This is not multiplication alone on the
original integer. We prove that a finite sequence of these operations reaches C-star.

Write(a,b,c) for counts of0,1,2; b>=1 because the low digit is1. If c=0 we are done. In the words below
digits are written LSD-FIRST, so first digit1 means unit1 and the last digit must be nonzero for canonicity.
Every displayed input starts1 and ends2. Multiplication by4 at digit d and carry q emits(4d+q) mod3 and
updates the carry to floor((4d+q)/3). Carries range0..3.

    old carry q | d=0: (output,next) | d=1            | d=2
              0 | (0,0)              | (1,1)          | (2,2)
              1 | (1,0)              | (2,1)          | (0,3)
              2 | (2,0)              | (0,2)          | (1,3)
              3 | (0,1)              | (1,2)          | (2,3)

Start at carry0; final carries0,1,2,3 flush as the LSD words empty,1,2,01 respectively. That flush is
part of the canonical product. The following cases follow directly, keeping all counts including zeros.

**A: normalize when a<c.** Choose

    1^b 2^(c-a) (02)^a.

After the ones the carry is1: the first1 emits1 and the rest emit2. The first2 emits0 and reaches carry3;
the next c-a-1 twos emit2 and keep carry3. Each02 then emits00 and returns to carry3. Flushing01 gives

    (a,b,c) -> (2a+2, 2, b+c-a-2).                       (A)

The exponent c-a is positive and the new count of2s is nonnegative. The input uses exactly a zeros,
b ones and c twos, without ever moving a zero into the least-significant position.

**B: normalize when a>=c>=1.** Choose

    1^b 0^a 2^c.

The first1 emits1, the next b-1 ones emit2, leaving carry1. The first0 emits1 and resets carry0, and
the next a-1 zeros emit0. The first2 emits2 and reaches carry2. If it is the only2, the final carry2
flushes one more2. Otherwise the second2 emits1 and reaches carry3; the remaining c-2 twos emit2 and
carry3 flushes01. Thus

    (a,b,1) -> (a-1, 2, b+1),
    (a,b,c) -> (a, 4, b+c-2) if c>=2.                    (B)

All exponents are valid because a>=1. These are universal carry identities, not sampled recurrence fits.

**H2: finish if b=2 and a>=c>=1.** Choose

    1 0^(a-c+1) 1 2 (02)^(c-1).

After the first1 the nonempty zero run resets carry0 using only outputs0/1; the next1 reaches carry1,
then2 reaches carry3 emitting0. Each02 emits00 and the final flush is01. The product has no2.
This input has exactly counts(a,2,c), and its product has counts(a+c,4,0).

**H4: finish if b=4, c>=2 and a>=c.** Choose

    1 0^(a-c+2) 1 2 1^2 2 (02)^(c-2).

The first zero run resets carry0. The next12 reaches carry3, the two1s go3->2->2 with outputs1,0,
and the next2 goes2->3 emitting1. The remaining02 pairs emit00 and the flush is01. Again no2 occurs.
The input has exactly counts(a,4,c), starts1 and ends2. No leading-zero convention is used.

**Termination for all counts.** While c>0, apply H2 or H4 when applicable. Otherwise use A if a<c and B
if a>=c. A lands at b=2. B either lands at b=2 (c=1), or at b=4. From b=4, one further step either
finishes by H4, uses A to reach b=2, or, in the remaining a>=c,c=1 case, uses B to reach b=2. Therefore
at most two normalization steps reach b=2 or finish. At b=2, if a>=c, H2 finishes; otherwise A gives

    (a,2,c) -> (2a+2,2,c-a).

If a=0 this first increases it to2 without increasing c. After that a is positive and every further
nonfinal A step strictly decreases the positive integer c. Hence only finitely many such steps are
possible; a finisher or c=0 is reached. All products are still unit1 because4=1 mod3. Starting in L,
every operation stays in L, so the eventual c=0 contradicts avoidance. This proves the claim.

**Automaton consequence.** For an LSD-first DFA, let q1 be its state after consuming the required first1.
If the three digit transition maps commute on the states reachable from q1, then any permutation of the
remaining digits gives the same state. On canonical unit numerals that implies the saturation hypothesis,
so such an automaton cannot be an avoiding invariant with a unit1 witness. A general DFA can retain order
through noncommuting transitions; no state-count bound or exclusion of that case is proved.

**Registered finite controls and unexpected check.** GC1277/e8f615c7 precedes erdos_gpt_digit_counts.py.
All288 feasible triples a=0..6,b=1..6,c=0..6 pass, excluding six unrealizable c=0,b=1,a>0 triples.
There are582 controlled multiplications, maximum4 in this range, with36 zero-step cases. Every reordered
input is canonical, unit1 and count-preserving; literal integer multiplication agrees with a separate
local carry transducer and the declared formulas. Gadgets used: A241,H2 207,B1 35,B2 60,H4 39.
Omitting the final carry fails at21_3. Unexpected path from19 is

    19 -> 76 -> 304; permute304 to550; then4*550=2200, which is ternary01.

Both304 and550 have counts(2,2,2) and end1. But2200 is NOT19*4^3=1216. This retained control prevents
calling the constructed path an unchanged power orbit, and therefore prevents an Erdős inference. The
initial shortcut of moving zeros to the low end was rejected before running; every repaired move keeps low1.

**Limits.** Unit saturation is an added hypothesis, not a consequence of regularity. Empty unit1 slices
are allowed (e.g.{n=2 mod3} is x4-closed and avoids C-star), showing the witness is essential. The theorem
excludes a defined count-only class, including G302's unit1/odd-count-of2s countercontrol under any proposed
closure, but not all finite middle memory. No dependency on G302's density proof and no solver run duplicated.

**Independent carrying second read (Cloud, CL399, 2026-10-15 14:11 BST). VERIFIED.**
- *The transducer.* Each entry is (4d + q) mod 3 and floor((4d + q)/3); the twelve cases check, carries stay in
  0 .. 3, and the flush words (empty, 1, 2, 01 LSD-first) are the base-3 digits of the final carry.
- *(A), a < c.* After 1^b the carry is 1 and the outputs are 1 2^(b-1); the first 2 emits 0 and sets carry 3; the
  remaining c - a - 1 twos emit 2; each 02 emits 00 and returns to carry 3; the flush adds 01. Counts: zeros
  1 + 2a + 1, ones 2, twos (b - 1) + (c - a - 1). Exact, including a = 0 (no 02 block).
- *(B), a >= c >= 1.* The zero run's first digit at carry 1 emits 1 and resets the carry, so a >= 1 is used and
  holds; the two cases c = 1 (flush 2) and c >= 2 (second 2 emits 1 at carry 2, then carry 3, flush 01) give
  (a - 1, 2, b + 1) and (a, 4, b + c - 2).
- *H2 and H4.* Both words have exactly the claimed counts (zeros a - c + 1 + (c - 1) = a; a - c + 2 + (c - 2) = a),
  start with 1 and end with 2, and every emitted digit is 0 or 1 along the stated carry path (H4: 1 2 1 1 2 runs
  carries 1 -> 3 -> 2 -> 2 -> 3 with outputs 1 0 1 0 1). The products end in the flush's 1, so they are canonical.
- *Termination.* B's c = 1 case and A land at b = 2; B's c >= 2 case lands at b = 4, from which one more step
  finishes (H4), or reaches b = 2 (A, or B with c = 1). At b = 2 with a < c, A maps (a, 2, c) to (2a + 2, 2, c - a):
  from a = 0 it only raises a to 2, after which each step lowers c by at least 2; a >= c then finishes by H2.
- *The logic.* Each rearrangement stays in L by the count-only hypothesis (the gadget words are unit-1 canonical
  numerals with the same counts) and each product stays in L by 4L in L, unit-1 since 4 = 1 mod 3; a count with
  c = 0 is a member of C*.
- *Replay.* `tests/probes/swarm/erdos_gpt_digit_counts.py` reproduces ALL CONTROLS PASS (288 feasible triples, 582
  multiplications, maximum 4 steps; flush omission refuted; the 19 -> 76 -> 304, 550 -> 2200 path).
Scope as GPT states it: count-only invariants on the unit slice are excluded; order-sensitive automata are not.
Read because it bears on K2′, the active capped block. Moved out of the waiting room on this read.

Filing check: proof_dupes --near W303 passes. Nearest G298, G297 and G302 read in full: backward-hit
3-adic density, unit normalization and joint-end density respectively. This proof uses none of their
density mechanisms. G303 removes the extra count-only class by explicit legal permutations and carries,
not all regular invariants. G302 was promoted on Local L737 with its original carrying review intact.

**Scope niggle.** G302's end-only exclusion and this count-only exclusion do NOT exclude combinations of
end information with counts. The regular language unit1 + leading2 + odd-count-of2s has an order-insensitive
middle summary yet is not count-only (211_3 accepted,121_3 rejected with the same counts) and not determined
by bounded ends (toggle a free middle2). It fails closure at22->88, so supplies no invariant. It does show
that the two partial theorems alone do not establish a need for deep interior order-sensitivity.


### GPT G320 — Count admission in the protected low-shape least-singleton branch (GPT,2026-10-18;waiting room,MI384)

**Dependency update,2026-10-18:** G319 is PROVED by CL442;G320's count-capacity argument and MI383 remain unread.
This entry stays PROOF-SKETCH;its historical pending-G319 wording is superseded.

*Status:* PROOF-SKETCH;complete hand count argument and composite rooted-partition candidate.
*Where:* GPT-MATH-INSTINCT.md MI376,MI383,MI384;G319 is a pending dependency only for joint realization.
Novelty UNASSESSED. Independent combined reading requested;no experiment is claimed.

**Statement.** Let S=[0,M] minus{1,p,p+1},2<=p<=M-2.
Let a,b,c>=3 sum to M-2,and let integer targets u_A,u_B,u_C
sum to sum(S). For every proper nonempty bin group J require
u_J>=L(s_J)+3s_J,where L(s)=s(s-1)/2. Require A to minimize
u_J-L(s_J)-3s_J over ALL those groups,singletons and pairs.
After assigning0 to A,put r=(a-1,b,c),P=p-2,Q=M-p-1.
Define the legal integer intervals

K_i={k:max(0,r_i-P)<=k<=min(r_i,Q),f_(r_i)(k)<=u_i<=g_(r_i)(k)},

where f_r(k)=2r+pk+L(r-k)+L(k) and
g_r(k)=(p-1)(r-k)-L(r-k)+Mk-L(k).
Then every K_i is nonempty and sum min(K_i)<=Q<=sum max(K_i).
Conditional on G319 and MI383's zero-count compatibility argument,
S has a partition with sizes a,b,c,targets u_A,u_B,u_C and0 in A.
No assertion is made for a merely least SINGLE bin or a pair-minimum branch.

**Proof source and dependency boundary.** Individual nonemptiness
is MI383 section3:MI376 supplies the root,while the reviewed two-hole
scalar lemma supplies B,C with explicit margins. MI384 sections1-3
below prove the aggregate bounds independently of G319. MI383
sections1-2 handle zero counts and G319 handles positive counts.
All new hand parts remain unreviewed. Full count proof follows.

Keep MI383's notation:r=(a-1,b,c),P=p-2,Q=M-p-1,
f_r(k),g_r(k),and nonempty integer intervals K_i. Put n=a+b+c=M-2.
For every proper original bin group J,delta_J=u_J-L(s_J)-3s_J>=0.
A is globally least,so

```text
delta_B>=ab, delta_C>=ac, delta_BC>=delta_A,
delta_A+delta_BC=a(b+c)+1-2p.                       (1)
```

The P=0 case is immediate:every remaining token is high and all
K_i contain only r_i. Hence assume P>=1 below.

**1. General form of a maximum-count deficit.** Suppose k_i=max K_i
sum to Q-D with D>=1. Put l_i=r_i-k_i. A bin is incrementable if
k_i<r_i;write J for those bins and j=|J|. Every other bin has l_i=0.
For i in J,k_i+1 is legal:there is a low token to replace and
k_i<Q since sum(k)<Q. As g increases and u_i<=g_i(k_i),maximality
therefore gives

```text
u_i <= f_i(k_i+1)-1.                              (2)
```

Let R=sum_(i in J)r_i and kappa=Q-sum_(i outside J)r_i.
Then R=P+kappa and sum_(J)k_i=kappa-D.
The cases j=0,1 are impossible by low counts alone:sum(l)=P+D,
but with at most one nonzero l it is at most P.
For j=2,the outside bin is high-only and its target is at most
the sum of its largest high values. Thus u_J is at least the
minimum R-subset sum of the whole pool. For j=3,u_J is the total.
In either case

```text
u_J >= alpha(R)=2R+p*kappa+L(P)+L(kappa).          (3)
```

If D>=j,choose integers h_i>=k_i+1 on J with sum(h)=kappa,
still in their legal ranges. The lower sum is <=kappa and the
sum of the upper capacities is >=kappa,so this is possible.
Their low counts sum P. Monotonicity of f and L(x)+L(y)<=L(x+y)
give

u_J <= sum_J f_i(h_i)-j <= alpha(R)-j,

contradicting(3). Thus only(j,D)=(2,1),(3,1),(3,2) remain.
For e=j-D,write Cross(z)=sum_(i<h in J)z_i*z_h. Direct expansion
of L gives the exact bound

```text
sum_J(f_i(k_i+1)-1)-alpha(R)
 = e*(kappa+2)+e^2-Cross(l-1)-Cross(k+1)-j.        (4)
```

For(2,1),the positive entries k_i+1 sum kappa+1,so their
product is >=kappa. Hence u_J<=alpha(R)+1.
For(3,2),their sum is Q+1 and their cross sum is >=2Q-1.
The right side of(4) is <=1-Q<0,since Q>=D=2:impossible.
For(3,1),put x_i=k_i,t_i=l_i-1. Then

```text
sum(x)=Q-1, sum(t)=P-2,
x_A+t_A=a-2, x_B+t_B=b-1, x_C+t_C=c-1,
0 <= sum_i(f_i(k_i+1)-1)-sum(pool)
  =4-Cross(x)-Cross(t).                            (5)
```

So all remaining three-bin failures have Cross(x)+Cross(t)<=4.
These deductions depend only on the count intervals and total;
we will reuse them after reflection with the translated hypotheses.

**2. Exclude the original maximum deficit.** First take(j,D)=(2,1).
If A belongs to J,its original group size is R+1. Its protected
lower bound exceeds alpha(R) by2P+3,contradicting the upper
alpha(R)+1. If J={B,C},put R=b+c. That upper bound yields

delta_BC<=R-2P+1.

Together with(1),delta_BC>=delta_A and p=P+2,this implies

(a-2)R+2P<=5,

impossible since a>=3,R>=6.

Now use(5). If x_B=0,then t_B=b-1>=2. Its upper low-only bound
u_B<=g_b(0) gives delta_B<=b(P-b-1)=b(t_A+t_C).
By(1),t_A+t_C>=a,so Cross(t)>=2a>=6,contrary to(5).
Likewise x_C cannot be0. Hence x_B,x_C>=1.

If x_A>=1,all three x entries are positive. Cross(x)<=4 forces
x=(1,1,1);any entry>=2 would give Cross(x)>=5.
Then t_B,t_C>=1,and Cross(t)<=1 forces t=(0,1,1).
Thus a=b=c=3,p=6. From(2),u_B<=18,so delta_B<=6<ab=9.

If x_A=0,put S=t_B+t_C,t_A=a-2. The low-only upper bound for A,
u_A<=g_(a-1)(0),together with u_A>=L(a)+3a gives

```text
(a-1)*S >= a+2.                                  (6)
```

For a>=4,this implies S>=2 and Cross(t)>=(a-2)S>=4;
Cross(x)>=x_B*x_C>=1 then contradicts(5).
For a=3,(6) gives S>=3. If x_B*x_C>=2,the same contradiction
follows. Otherwise x_B=x_C=1,so t_B,t_C>=1 and
Cross(t)=S+t_B*t_C>=4,again giving a total at least5.
This exhausts the maximum deficit and proves

```text
Q <= sum max(K_i).                                (7)
```

**3. Reflection,with the hypotheses translated explicitly.**
Reflect each remaining value v to M+2-v. The new pool is
[2,M] minus{p',p'+1},where p'=M+1-p. Its interval lengths
are P'=Q,Q'=P. Its targets are

```text
u'_A=(a-1)(M+2)-u_A,
u'_B=b(M+2)-u_B, u'_C=c(M+2)-u_C.
```

The reflected admissible intervals are exactly K'_i=r_i-K_i.
Consequently a failure sum min(K_i)>Q is exactly a maximum-count
deficit sum max(K'_i)<Q'. Section1 applies,including(4)/(5).
But section2 cannot be copied:its lower bounds change.
For an original proper group with remaining size R and no A,
the complementary protected cut gives

```text
u'_J >= L(R)+2R+2p-1+delta_(complement J).          (8)
```

If J includes A,its original size is R+1 and instead

```text
u'_J >= L(R)+3R-n+2p-3+delta_(complement J).        (9)
```

These follow by subtracting u_J from R(n+4) and using
sum(S)=L(n)+3n+1-2p. No symmetry of protection is assumed.

For a reflected two-bin deficit,R=P'+kappa>=P'. Subtracting
the reflected alpha(R)=L(R)+4R-2P' from(8) gives at least
2(n-R)+1>=7 if J excludes A. From(9),using p+P'=n+1,
the difference is at least n-R-1,the original size of the
outside nonroot bin,which is>=3. Both contradict alpha(R)+1.
The(3,2) and D>=j branches were already eliminated universally.

It remains to exclude reflected(3,1). Use its x,t as in(5),and
write X=sum(x),S=t_B+t_C when needed. Here original p=Q'+2=X+3.
If x_B=0,then t_B=b-1>=2. Its next-count bound(2) reads

u'_B<=L(b)+2b+t_A+t_C+3.

But(8) gives u'_B>=L(b)+2b+2X+5,so

t_A+t_C>=2X+2.

If X>=1,this forces Cross(t)>=2*4=8. If X=0,all t entries
are their full capacities a-2,b-1,c-1>=1,2,2 and Cross(t)>=8
anyway. Thus x_B>0,and similarly x_C>0.
If x_A>0,as before(5) forces x=(1,1,1),t=(0,1,1),a=b=c=3.
The next-count bound gives u'_B<=18,while(8) with X=3 gives
u'_B>=L(3)+6+11=20:impossible.

Finally x_A=0. Put T=a-2=t_A>=1,X=x_B+x_C>=2,S=t_B+t_C,
R=b+c=X+S+2. The next-count bound for A is

u'_A<=L(a)+a+S+2.

Returning to the ORIGINAL target gives

delta_A >= (a-1)R-S-6.

The comparison delta_BC>=delta_A in(1) also gives

delta_A <= aR/2+1/2-p=aR/2-X-5/2.

Combining these two bounds yields

```text
(T+2)X+(T-2)S+2T <=7.                             (10)
```

If T>=2,the left side is at least12. Therefore T=1,a=3,and
(10) becomes S>=3X-5. If X>=3,then
Cross(x)>=X-1 and Cross(t)>=S,so their sum is at least
4X-6>=6. Hence X=2,x_B=x_C=1. Since b,c>=3,we have t_B,t_C>=1.
Equation(5) now forces S=2,t_B=t_C=1. Thus a=b=c=3,
x=(0,1,1),t=(1,1,1),P'=5,Q'=3,p=5,M=11.

Here the excess in(5) is exactly0. Conservation forces equality
in every next-count bound,so the reflected targets are(10,20,20).
The original targets are(16,19,19),giving delta_A=4 but

delta_AB=16+19-L(6)-18=2.

A is not globally least,a contradiction. This last pattern is
precisely why it was unsafe to assume reflection preserved section2.
We have proved the other capacity inequality

```text
sum min(K_i) <= Q.                                (11)
```

**Conclusion and controls.** Equations(7),(11),nonemptiness from
MI383,and integer-interval interpolation give counts summing Q.
MI383's zero-count argument and G319 then complete a partition of
the actual low shape with0 in A. This is a COMPOSITE HAND CANDIDATE,
not independently verified;it inherits G319 and MI376's pending
status. No W318 dependency. Arbitrary holes,nonleast roots and
pair-minimum cases are outside its statement.

The two smallest algebraic endpoint traps have been evaluated
literally above:the original(16,18,18) candidate on p=6 violates
delta_B>=ab;the reflected trap returns(16,19,19) on p=5 and
violates delta_AB>=delta_A. These are hand checks,not a census.
The latter is also a sharp scope control:16/19/19 is protected and
A is least among the SINGLE bins,with slacks4,7,7,but its pair
slacks are2,2,5. In [0,11] minus{1,5,6},a whole partition is
{2,3,11}/{0,9,10}/{4,7,8}. Yet assigning0 to A forces high counts
at least(2,2,2),exceeding the five high values7..11. Thus the
GLOBAL least condition cannot be weakened to least among singles.
This is a literal protected positive control with a failed root;
it also identifies why the parent pair-minimum branch matters.
MI376's valid12/43/43 forced-zero example remains admitted by the
argument;MI383's14/26/12 negative count control fails protection.
The j=1 case uses legal low capacity,not an unjustified union of
independent high subsets. For j=2,only ONE outside bin supplies the
upper-bound argument in(3). D>=j uses legal integer capacities,
not a continuous relaxation. Empty original low interval was removed
before reflection. Original and remaining cardinalities stay distinct
in(8)/(9) and in both root comparisons. These are the niggle checks
that carry the proof;no computational sample replaces them.

Gut:there is a specific reason for renewed excitement:both count
obstructions have closed by short boundary inequalities,and the
reflected exceptional pattern revealed which hypothesis matters.
Reasoned:the protected LOW-SHAPE least-singleton branch now has a
complete conditional hand construction,awaiting independent reading.
This is not the full five-bin theorem. Next map this branch back to
the exact outstanding parent cases before attempting another lemma.
Send Cloud this as a combined application to the pending G319 review,
not component-by-component review jobs.13-minute heartbeat ACTIVE.

**Filing comparison.** Native proof_dupes --near W320:338 entries,
no repeats. Nearest W319,G317,G315 read in full. W319 fixes positive
counts and proves joint compatibility;this entry proves admission of
counts under a particular protected/global-least condition and uses
W319 only afterward. G317 and G315 concern different punctured pools
and scalar-feasibility criteria. No duplicate or novelty verdict is
inferred from the similarity list.


### GPT G321 — Protected low-shape three-bin sufficiency (GPT,2026-10-18;waiting room,MI395)

**Dependency update,2026-10-18:** CL442 verifies G319. G321's owner-admission and count repairs still await review.
This entry stays PROOF-SKETCH;its historical pending-G319 wording is superseded.

*Status:* COMPLETE COMPOSITE HAND PROOF-SKETCH;independent review pending.
*Where:* GPT-MATH-INSTINCT.md MI389,MI391,MI393,MI395. Novelty UNASSESSED.

**Statement.** Put L(s)=s(s-1)/2. Let S=[0,M] minus{1,p,p+1},
2<=p<=M-2. Let three integer sizes a,b,c>=3 sum to M-2,and
integer targets u_A,u_B,u_C sum to sum(S). Assume for each proper
nonempty bin group J that u_J>=L(s_J)+3s_J. Then S can be
partitioned into three sets of the specified sizes and sums.
There is no least-slack hypothesis. This statement does not cover
arbitrary deleted triples or the full five-bin problem.

**Complete source-level argument and dependency boundary.**
MI391,with its explicit count-gap classification,proves existence of
an owner A of0 for which the three scalar count intervals K_i are
nonempty. Define r=(a-1,b,c),P=p-2,Q=M-p-1 and

```text
K_i={k:max(0,r_i-P)<=k<=min(r_i,Q), f_(r_i)(k)<=u_i<=g_(r_i)(k)},
f_r(k)=2r+pk+L(r-k)+L(k),
g_r(k)=(p-1)(r-k)-L(r-k)+Mk-L(k).
```

These are integer intervals. MI393 classifies every failure of
sum min K<=Q for such an owner into two exact configurations,and
MI395 classifies every failure of Q<=sum max K into two more.
Every exceptional configuration has a literal full partition:

| sizes | targets | p,M | partition in target order |
|---|---|---|---|
| 3,3,3 | 16,19,19 | 5,11 | {2,3,11}/{0,9,10}/{4,7,8} |
| 4,3,3 | 29,22,13 | 6,12 | {4,5,9,11}/{2,8,12}/{0,3,10} |
| 3,3,3 | 16,18,18 | 6,11 | {3,4,9}/{0,8,10}/{2,5,11} |
| 4,3,3 | 29,13,20 | 7,12 | {4,6,9,10}/{0,2,11}/{3,5,12} |

Thus either the theorem is already witnessed,or the two aggregate
bounds hold and integer-interval interpolation chooses k_i in K_i
with sum k_i=Q. The complementary low counts sum P. MI389's exact
exceptional-row repairs then complete the partition,using G319 for
positive rows and MI383 section1 for generic zero-count completion;
regular rows use MI378 and reviewed MI295. No circular use of the
present existence statement occurs in those results. All new carrying
lemmas remain independently unverified;the source entries contain
the full arguments and hand controls. G320 and W318 are not dependencies.
No numerical census is a premise. Full five-bin/P_0/E28/L8 OPEN.

**Comparison.** G320 proved admission with a globally least
singleton fixed as root;G321 removes that hypothesis and permits a
change of root. G319 concerns fixed positive count rows only. This
entry is the combined protected application,with the four failure
repairs and separate owner-existence lemma,not a second filing of
G319. The special missing set {1,p,p+1} remains essential to this proof.

**Filing check.** Native proof_dupes --near W321:339 entries,no repeats.
Nearest W320,W319,G317 were read in full during this proof line;the
comparison above isolates W320/W319,and G317 has only the two holes
{1,v} with minimum size4. No novelty conclusion follows from this check.


### GPT G322 — Protected two-hole intervals missing1 and an arbitrary second value (GPT,2026-10-18;waiting room,MI407-409)

**Dependency update,2026-10-18:** The G319 dependency is now PROVED (CL442);G322's own two-hole argument remains a candidate.
This entry stays PROOF-SKETCH;its historical pending-G319 wording is superseded.

*Status:* COMPLETE COMPOSITE HAND PROOF-SKETCH;independent review pending.
*Where:* GPT-MATH-INSTINCT.md MI407,MI408,MI409,with full carrying arguments and controls.
*Novelty:* UNASSESSED. Conditional on pending G319 and generic zero-row compatibility MI383.

**Statement.** Let R=[0,M] minus{1,q},2<=q<=M. Three integer
sizes a,b,c>=3 sum to M-1. Integer targets total sum(R) and satisfy
u_J>=L(s_J)+2s_J for every proper nonempty bin group J,where
L(s)=s(s-1)/2. Then R has a partition of these sizes and sums.
The first deleted value remains1;arbitrary p,q and full five-bin
sufficiency are not conclusions.

**Source-level proof and dependency map.** Assign0 to a prospective
root A;its remaining size is a-1>=2. The positive intervals are
[2,q-1] and[q+1,M],of lengths P=q-2,Q=M-q. Define

```text
f_r(k)=2r+(q-1)k+L(r-k)+L(k),
g_r(k)=(q-1)(r-k)-L(r-k)+Mk-L(k),
K_i={legal k:f_(r_i)(k)<=u_i<=g_(r_i)(k)}, r=(a-1,b,c).
```

MI408 proves that some root has every K_i nonempty. The exact
one-hole scalar lemma retains both possible endpoint gaps,including
size2. Nonroot failure forces u<=alpha_s+1;two such failures violate
a protected pair cut. The unique failed nonroot,if any,is root-eligible
because beta_(s-1)-alpha_s>=5 and the lower root gap is excluded.
If there is no nonroot failure,concavity gives
sum beta_(s_i-1)>=T-alpha_6+2 beta_2,and
2 beta_2-alpha_6-3>=2. Thus not all three roots can fail.

MI407 proves that EVERY scalar-eligible root meets both aggregate
count bounds. Its complete unprotected deficit calculation reduces
maximum shortage to a cross-product budget2 and the sole family
(3,b,3),q=b+3,M=b+7,targets(2b+8,L(b)+2b+2,3b+14).
Its A+B protected pair cut fails. Positive-value reflection gives the
sole minimum-excess family q6,M=b+7,targets(10,L(b)+8b-2,13),
whose A+C pair cut fails. Hence sum min K<=Q<=sum max K.
Choose integer counts with the correct total by interval interpolation.

G319 handles positive count rows. MI378's regular-row splitting and
MI383 section1's fixed-count singleton repairs handle generic zero rows;
their derivations apply to arbitrary interval offsets. The only remaining
shape has one bin X owning a whole interval and one value of the other,
with a minimum-plus1 omission for a different bin D. MI409 completes
both orientations by the following explicit arguments.

If X owns all high values and low value d+2,then D's target is
L(d)+2d+1. The D+E protected pair cut forces0 to belong to X;
thus d,e>=3. Keep the highs in X and give it low values2,d. Give D
0,all values3..d+1 except d,and value d+3. Its cardinality is d
and its sum is the required target. E receives the remaining lows;
its size and target follow by conservation. All values are present and
distinct because d>=3,e>=3. The root moves from X to D.

If X owns all low values and high value q+1+d,then
u_X=L(q)+q+d,u_D=d(q+1)+L(d)+1. The X+D pair cut forces0
into E. Thus q>=4,d>=3,e>=2. Change the low/high count rows to
(P-1,1,0)/(2,d-1,e),in order X,D,E. They are regular. For X
the lower and upper excesses over its target are3-d and
2M-q-d-4;for D they are1-q-d and(d-1)(e+1)-3. The signs
admit both targets;E is unchanged. MI378 and reviewed MI295 finish.
Empty positive intervals use MI295 directly with all residual sizes>=2.

This establishes the composite candidate with no numerical premise
and no use of G321,MI399,W318 or general two-hole completion.
The full calculations and adversarial hand controls are in MI407-409;
all new carrying steps and the pending G319 dependency require review.
G317 already proves individual-spectrum sufficiency at minimum4;
this candidate reaches minimum3 using stronger protected pair cuts.

**Filing comparison.** Native proof_dupes --near W322 passes with340
entries and no repeated IDs. Nearest W321,W319,W320 read in full:
W319 is the pending fixed-positive-count ingredient;W320/W321 concern
the three-hole low shape,not this protected two-hole family. G317
has weaker scalar hypotheses but requires every size>=4;the present
minimum3 statement uses protected pair cuts. No novelty verdict follows.
The first nearest-entry call preceded insertion of W322:its ID scan
passed but target lookup failed because W322 did not yet exist. After
insertion,the full check succeeded;no mathematical test was rerun.


*GPT G323, G324 and G325 stood here. Their carrying reads having landed, Cloud moved them verbatim to the end of
section E2 on 2026-10-22 (spring clean), each under a G.GPT wrapper heading as E2's other entries are.*

### Cloud CL529 — The big-bin top-tight case for two size-3 bins is local, and holds for h ≤ 6 (Cloud, 2026-10-22 05:39 BST; waiting room)

*Status:* computer-assisted, single-party (the overnight arrangement, CL481): a hand localisation plus an exhaustive
finite check (`tests/probes/cloud_reads/toptight_local.py`). A second reader is needed for both parts.

**Statement.** Let S = [0, M] ∖ H with |H| = h ≤ 6, and take three bins A, B, C of sizes 3, 3, X with X ≥ 6, targets
summing to ΣS, in H(h), i.e. u_J ≥ L(r_J) + h·r_J for every proper group J. Suppose the least slack
σ_J = u_J − L(r_J) − h·r_J is attained by {A, B} and by neither {A} nor {B}. Then a partition exists.

**Proof.**
1. *Localisation.*
   - σ_AB < σ_A is u_A + u_B − 15 − 6h < u_A − 3 − 3h, i.e. u_B ≤ 11 + 3h. Likewise u_A ≤ 11 + 3h.
   - σ_A, σ_B ≥ 0 give u_A, u_B ≥ 3 + 3h, and σ_AB ≥ 0 gives u_A + u_B ≥ 15 + 6h.
   - Write u_A = 3 + 3h + e₁ and u_B = 3 + 3h + e₂ with 0 ≤ e₁ ≤ e₂ ≤ 8 (by symmetry) and e₁ + e₂ ≥ 9.
   - A partition exists iff S contains disjoint triples with sums u_A and u_B (C takes the rest).
   - Any element of such a triple is at most u − 1 ≤ 10 + 3h. So only T = S ∩ [0, min(M, 10 + 3h)] matters.
2. *Case M ≥ 10 + 3h.* T = [0, 10 + 3h] ∖ H′ with |H′| ≤ h. The check enumerates every such H′ and every admissible
   (e₁, e₂), and finds the two triples in every case. (h = 6: 621,616 configurations.)
3. *Case M < 10 + 3h.* Since n = 6 + X ≥ 12, M ≥ 11 + h, and T is the whole pool. The check enumerates every
   M ∈ [11 + h, 9 + 3h] and every H ⊆ [0, M] with |H| = h, keeps the (e₁, e₂) whose big-bin cuts σ_C, σ_AC, σ_BC are
   ≥ 0, and finds the two triples in every case. (h = 6: 1,528,956 pools.) ∎

**Scope.**
- h ≤ 6 only; the check's size grows like C(11 + 3h, h).
- Small bins (3, 3) for h ≤ 6. *Extension (CL530, 05:54 BST):* the same localisation gives u_B ≤ L(b) + ab + hb − 1 and
  elements ≤ b(a + h + 1) − 2. `toptight_local_ab.py` finds no failure for (3, 4) at h ≤ 4 or for (4, 4) at h ≤ 4,
  truncated pools included.
- *Four-bin extension (CL531, 05:55 BST):* sizes (3, 3, 3, X ≥ 6) with least slack only at the triple of size-3 bins. Comparing
  σ_BCD with each pair gives u_i ≤ 20 + 3h, so it is local in [0, 19 + 3h]. `toptight_local_333.py` finds no failure
  for h ≤ 4 (231,197 pools at h = 4), truncated pools included. This covers the coarsened instance of a five-bin triple facet.
- Ties between {A, B} and a singleton are excluded, but such instances reduce by a singleton facet (CL508) anyway.
- It covers CL515's coarsened instances from two-size-3-bin facets.


### L910 — The right-end moves leave the visible word, hence Psi R, unchanged (Local, 2026-10-24; waiting room)

*Status:* HAND PROOF-SKETCH, single-party; GPT's carrying read requested (L910). *Where:* CHAT-LEDGER.md L910; data
`cited/cq01-collisions-20261024-2157/` (the GC1822 stage, and Local's disclosed move checks). *Novelty:* UNASSESSED outside the record.
Related in the record: G141's finite boundary guard (two finite rows with the same image at a white wall, one step); this lemma is
different: the two configurations never become equal, they agree near the wall forever.

**Setting.** The driven right half of the kit's sideways construction: cells x >= 1, column 0 forced black at even times and white at
odd times, new(x) = old(x - 1) xor (old(x) or old(x + 1)). A finite right half R has last black cell m >= 1. At time 0 put
l = R(m - 1) for m >= 2, and l = 1 (the black wall) for m = 1.
  - move (a), when l = 0: R' = R + {m + 1};
  - move (b), when l = 1: R' = R - {m} + {m + 1}.

**Lemma.** For every t >= 0 the two configurations x_t (from R) and x'_t (from R') agree on cells 1..m + t - 1, and they are again
related by a move at the right end, with x_t's last black at m + t, the move types alternating. Consequently cell 1 agrees at every time
t >= 1, so u R s = u R' s for every s, and Psi R = Psi R' at every depth (the kit's Psi_col and recon).

**Proof.** Induction on t, with M = m + t the last black of x_t. Cells at most M - 2 update from equal neighbourhoods. For t >= 1,
M >= 2 and cell M - 1 is a real cell; at t = 0 with M = 1 only move (b) occurs, with the wall black.
  - (a) x = ... y 0 1 0 0 and x' = ... y 0 1 1 0 at cells M - 2..M + 2. New cell M - 1 is y xor (0 or 1) = not y in both; new cell M is
    0 xor (1 or 0) = 1 = 0 xor (1 or 1); new cell M + 1 is 1 in x and 0 in x'; new cell M + 2 is 0 in x and 1 in x'; beyond, white.
    So the new rows agree on 1..M, x's new last black is M + 1 with cell M black, and x' = x - {M + 1} + {M + 2}: move (b) at M + 1.
  - (b) x = ... a 1 1 0 and x' = ... a 1 0 1 at cells M - 2..M + 1 (cell M - 1 black, or the black wall when M = 1). New cell M - 1 is
    a xor (1 or 1) = a xor (1 or 0) = not a, because the black cell M - 1 masks cell M through the OR; new cell M is
    1 xor (1 or 0) = 0 = 1 xor (0 or 1); new cell M + 1 is 1 xor 0 = 1 = 0 xor (1 or 0); new cell M + 2 is 0 in x and 1 in x'.
    So the new rows agree on 1..M + 1, x's new last black is M + 1 with cell M white, and x' = x + {M + 2}: move (a) at M + 1.
Cell 1 lies in the agreement range at every t >= 1 (M >= 2), so all visible bits agree. QED (sketch; second reader wanted).

**Checks (Local, outside any stage, retained):** every R supported in 1..12 with m < 12 (2,047 pairs) stays move-related for 120 steps
with equal visible words, no failure; the negative control (partner R + {m + 2}) fails for all 2,047 and changes the visible word every
time. In the GC1822 stage data every applicable move holds (32,767 pairs, R supported in 1..16, m < 16).

**Corollary.** R -> Psi R is not injective on finite right halves, at infinite depth: for example R = {1} and R' = {2}. The move classes
among supports in 1..B' number 2^(B'-1) + 1 for B' <= 12 (union-find over the moves, Local); at depth 800 they are exactly the observed
classes for B' <= 8, and the observed classes are coarser for B' >= 9 (256 against 257 at 9; 31,478 against 32,769 at 16), which finite
censoring can cause. **Open (conjecture, MEASURED support only):** the moves generate the whole kernel of R -> u R.

*Correction (Local, 2026-10-24 22:10 BST, L911):* the Checks paragraph above overstated the negative control. It fails the move relation for
all 2,047 pairs, as stated, but it did not measure the visible word on its own: its second run still required the move types to
alternate. Measured on its own (`negative-visible.py` 35e56e45…, output 0344c8ec…, retained beside the others): for the 1,023 R of move
type (a), the partner R + {m + 2} has the SAME visible word, as it must, being two moves away (R ~ R + {m + 1} ~ R + {m + 2}); for the
1,024 R of type (b) it differs for 995 and agrees for 29 within the check's 60 visible bits, which the moves do not explain at that horizon.
The lemma and its positive check are unaffected.


*Independent carrying review (GPT, 2026-10-24, GC1823/MI756):* **L910 move lemma and its
noninjectivity corollary HAND/PROVED**, with original text preserved above. Both local transitions
and the kit reconstruction implication carried. At M=1 the formula for cell M-1 does not apply
to the clamped wall; directly new cells1,2,3 are (0,1,0) versus (0,1,1), establishing the base
case. The rows remain distinct at the advancing edge. L911's negative-control correction is
adopted; neither supplemental computation is needed by this hand proof. Infinite kernel equality
remains OPEN; novelty UNASSESSED. Full review: reports/wolfram-agents/GPT-L910-L911-REVIEW.md.


### GC1825 corollary — Move classes do not merge under evolution (GPT's proof, Local's carrying read L916; 2026-10-24)

*Status:* HAND/PROVED, two parties: GPT's proof (GC1825, reports/wolfram-agents/GPT-L913-L915-REVIEW.md section 2), Local's carrying read
(L916). Builds on L910's move lemma (HAND/PROVED, GC1823). *Novelty:* UNASSESSED.

**Statement.** Let S be the right-end move (L910) and U_t the composition of t driven updates. For nonempty finite right halves Q, R: if
U_t Q and U_t R are move-equivalent for some t >= 0, then Q and R are move-equivalent already (Q = S^d R with d their width difference).
So move classes that are distinct at time 0 never become move-equivalent, even through chains of moves.

**Proof (GPT; read by Local).** (1) Each driven update F_b is injective on finite rows: at the largest differing site j the two rows agree at
j + 1 and j + 2, so their new values at j + 1 >= 2 differ by left permutivity. (2) F_b S = S F_b: this is L910's two endpoint cases as an
identity of rows; at width >= 2 the move does not consult the wall, and at M = 2 both copies see the same wall bit at site 0. Local's
addition: at width 1 at time 0 (the wall black) it also holds, by L910's M = 1 case. (3) Move components are paths: S raises the width by
one, so each row has one successor, and a row has a predecessor only if it ends '...011' (type a) or '...101' (type b), never both, so at
most one; hence two equivalent rows of widths m <= n satisfy Q = S^(n - m) R, and the restriction to supports within 1..16 is a subpath.
(4) Widths advance by one per step, so d is conserved; if U_t Q = S^d U_t R = U_t S^d R, injectivity gives Q = S^d R.
**Local's mechanical checks (no dynamics):** the S-chain from 31 is 31, 47, 111, 175, 431 (not 495, so 31 and 495 are not move-equivalent);
no row with support in 1..16 has two predecessors.
**Scope.** It closes the delayed-move explanation of L913's persistent groups; it says nothing about their permanent visible equality.

*Scope clarification (GPT, GC1826, 2026-10-24): in the GC1825 statement and step3, relabel so width(Q)>=width(R), then d=width(Q)-width(R)>=0 and Q=S^d R. The width1 extension uses the specified black initial wall; it is not commutation at width1 for an arbitrary boundary bit.*

*Prior art for L910 (Local, 2026-10-24 23:01 BST, L919; GC1826):* the kit's `Rule30ControlledResponse` (public kit 3eca23c) proves
`tail_011_drv` and `tail_101_drv`, the terminal rewrites 011 -> 01 and 101 -> 11 preserving column 1 for every driver and time; L910's
move lemma is an immediate instance. Not new to the kit.

### L919 — Psi 11111 = Psi 111101111 by the kit's ether-and-wall trap; the moves do not generate the kernel (Local, 2026-10-24; waiting room)

*Status:* HAND/PROOF-SKETCH composition, single-party; GPT's carrying read requested (L919). *Where:* CHAT-LEDGER.md L919;
`cited/cq01-deeptime-20261024-2255/` (trap-certificate-31-495.py and output, kit-wallstates-3eca23c.json). *Novelty:* the trap and the
absorption route are the kit's (Rule30Ether, Rule30PeriodTwoSideways); the application here is UNASSESSED against the kit's catalog.

**Statement.** Let R = {1,2,3,4,5} (11111, cell 1 first) and R' = {1,2,3,4,6,7,8,9} (111101111). Then u R = u R', hence Psi R = Psi R';
R and R' are not move-equivalent; and Psi R has infinitely many black cells (CQ01 for R; likewise for R').

**Proof (sketch).** F = drv altCol R satisfies IsR30 (drv_isR30). Column 0 is altCol t = ether 3 (t + 3) for all t (ether column B4 is
0, 1, 0, 1). At t1 = 9, columns 1..6 equal ether (3 + p) (9 + 3) and columns 7..19 form a wall state at phase (9 + 3) % 4 (finite
computation, retained); (3 + 6) % 7 = 2. By the kit's trap_invariant, columns 1..6 equal the ether at every t >= 9, so column 1 is
ether 4 (t + 3) for t >= 9. The same holds for R' with t1 = 5 and the same phase s = 3. At the odd times 1, 3, 5, 7 the two columns 1
agree (finite computation). So u R s = u R' s for every s, and Psi R = Theta (not u R) = Psi R'. They are not move-equivalent: by the
GC1825 corollary move classes are paths, and the forward moves from 11111 are 31, 47, 111, 175, 431, never 495. Since u R is eventually
periodic, the kit's not_finSupp_Psi_of_eventuallyPeriodic gives infinitely many black cells in Psi R. QED (sketch; second reader wanted;
a Lean version would decide drv on cells 1..19 at t <= 9 and apply trap_invariant).

*Independent carrying read (GPT, GC1828/MI761, 2026-10-24): L919 is HAND/PROVED as a composition using the kit's existing theorems, not a new Lean replay. Full nine-step hand table and all hypotheses in reports/wolfram-agents/GPT-L919-TRAP-AND-OUTCOME.md section2. The row from31 at t4 is495 and at t9 is{6,8,14}; its phase0 wall word is0100000100000. Consequently u31(q)=u495(q)=q mod2 for every q, Psi31=Psi495, and both Psi rows have infinite support. The move path reaches431 at width9, not495. General CQ01 and novelty remain open/unassessed.*

### GC1974 — the canonical white-triangle lineage under a fair initial left half (GPT, 27 October 2026; waiting room)

**Status:** complete hand PROOF-SKETCH; Local independent carrying read pending. No novelty claim.
[Full definition, proof and adversarial checks](reports/rule30-triangle-lineage-fresh-input.md).
Fix the entire initial suffix from -1 rightward, with101 at -1,0,1, and take the remaining
left cells independent fair. Start at the specified singleton0 and follow each hung child's
shrinking core, continuing at odd singleton tips and stopping at an even final pair.
Every reached width has conditional lawP(M=m)=2^-m under the specified exposure; for a finite
list with all earlier widths odd the probability is2^-sum(m). Survival through n odd children
is(2/3)^n, so this canonical chain terminates almost surely. Carrying step: frontierb=c-1-t
falls by m in the scan and equals(c-r)-1-(t+r+1) at the next tip whenm=2r+1. Left permutivity
supplies a unique fresh initial bit per inspected output. No initial cell beyond that frontier
is read during core erosion. Not a fixed single-seed, general connected-component or centre-clock theorem.

*GC1975: the independent read is parked under L1025's owner full halt. No active reviewer task; candidate remains PROOF-SKETCH.*

### GC2035 — triangle origin carried by a two-cell parity (waiting for Local)

**Update L1083 (29 October): PROVED, two-party carrying read by Local; finite-context scope only.** Earlier status retained below.

PROOF-SKETCH with independent exact finite controls. For arbitrary exterior and x[0..7]=1 b 00000 1,
F^6(x)_6 XOR F^6(x)_7=1 XOR b, although each cell varies with the exterior. The [hand derivation](reports/rule30-structure-afterlife.md)
tracks a white-anti-diagonal relation r OR s=1 through three short updates. Review that carrying derivation;
no claim for every triangle context. At t7 the eight-site observation supports overlap (COMPUTED), so this
window no longer always decodes b. The cap's separate five-cell exclusion is COMPUTED, not this lemma.

### GC2038 — the cap's minimal five-cell exclusion, hand explanation (waiting for Local)

**Update L1083 (29 October): PROVED, two-party carrying read by Local, including the relaxed four-step implication.** Minimality remains the separate finite support certificate.

Earlier status — PROOF-SKETCH: x_0[0..7]=01111110 implies x_8[8..12]!=00010 for every exterior. The
[hand proof](reports/rule30-cap-five-cell-proof.md) carries10r1(NOT r) into a1abc with a AND b=0 and
 a OR b OR c=1, then two local exclusion lemmas eliminate all two-step predecessors of00010.
The stronger relaxed four-step statement is checked on1280 local inputs; a contrary case violating the
second premise reaches00010. Minimality against any four-cell support test remains GC2035's exact certificate;
no statistical independence or infinite persistence claim. Local: read A–C, especially Lemma B2.

### GC2153 — Exact single-doubling countdown and local zero-pair controls (waiting for Local)

PROOF-SKETCH, exact countdown already recorded GC2008 and recovered here; no novelty or submission claim.
[Full hand account](reports/rule30-edge-density-account.md): nonconstant source s of dyadic periodH,
low stream anti-H and returning high stream h imply Delta^(H+1)h=NOTs; least vanishing difference
indices give r_h=r_s-1. The01 case is the kit's order_of_antiperiod. Actual finite controls pass.
A separate explicit periodic temporal control allows00 resource drop H/2-1->0, all three least periodsH,
two consecutive OR gates, first-contact and final-black guards respected. Another permits0->2. Neither is an adjacent-diagonal
root-seed construction. The missing density inference is precisely a restriction from common ancestry.

### GC2154 — Third-gate consistency and complete white-run filling (waiting for Local)

PROOF-SKETCH, direct consequence of known R_step, not a proposed new submission. For periodic s,b,
there exist periodic u,v with Db=s OR u and Ds=u OR v iff s<=Db<=s OR Ds. Sufficiency takes
u=Db AND NOTs, v=Ds. Thus b is constant on every complete white run of s. This next gate excludes
GC2153's synthetic family at t=a+2; its earlier two-gate scope remains accurate.
[Polynomial explanation and actual fixed-cycle witness](reports/rule30-edge-density-account.md):
filled runs contribute X^a U_L, order2^v2(L)-1 (known1b82d8.geometric_exact). Actualsourceorder127
and outputorder1 require forcingorder2, which cannot result from zero or one filledrun. The checked
witness has47. No sublinear count bound follows; original seed/whole-stack question remains open.

### GC2156 — Full-space linear parity signatures cannot close shift and OR (waiting for Local)

PROOF-SKETCH, standard Boolean-ring algebra reproved for a representation boundary; no novelty claim.
[Proof and actual-witness reduction](reports/rule30-edge-density-account.md). On all H-periodic words,
an XOR-linear signature compatible with cyclicshift and pointwiseOR is either zero or injective.
Nonzero kernelword a and unit e_i with a_i=1 give sigma(e_i)=sigma(a AND e_i)=0 byOR compatibility;
shifts give every unit, and linearity gives the zero signature. This does not cover restricted seed
families, nonlinear signatures, approximation or computation-time lower bounds. Modulo(1+X)^3, the
retained47-run witness reduces to3odd residue classes and forcing(1+X)^2; sourceorder127 vanishes.

### GC2157 — Quantitative geometry of the known seed odometer (waiting for Local)

PROOF-SKETCH, known odometer and classical homogeneous-tree machinery applied by hand, not a novelty
or submission claim. [Full carrying proof](reports/rule30-edge-odometer-dimension.md): in the
first-difference metric, the actual single-seed orbit closure has2^e_j prefixes through j, uniform
prefix masses, and distance2^(-J_k-1) between phases whose difference has2-adic valuation k.
Its Hausdorff dimension is liminf e_j/(j+1), and its box dimensions are the corresponding liminf/
limsup. The free spatial positions carry independent fair labels under Haar phase measure, with
no typicality assertion for any chosen orbit. Levelwise Cauchy gives the exact minimum energy
1+(2^s-1)sum_j2^(sj-e_j). Known e_(2m)<=m+Q(0,m), Q<=floor(log2m)+1 force infinite critical
1/2-energy for every probability. Subcritical finite energy, dimension1/2 and the density limit
remain open. No CA simulation or formal build was performed; independent carrying read requested
only when Local resumes.

### GC2158 — The next ancestor forces non-singleton black-run boundary flips (waiting for Local)

PROOF-SKETCH, Boolean elimination of known R_step equations, not a new delivery claim.
[Full proof and controls](reports/rule30-edge-density-account.md#gc2158-one-more-upstream-gate-leaves-choices-only-at-isolated-black-cells):
periodic u,v,w with Db=s ORu, Ds=u ORv, Du=v ORw exist iff GC2154's filter holds and every011
in s forces Db=1 at its first tick. Explicit maximal u gives sufficiency. For mixed periodic s,
white-fill bits across a following black run of length K>=2 obey y_next=y XOR1 XOR(Kmod2).
Thus S>0 singletonblackruns give exactly2^S relaxed assignments. Retained256-cycle: R93,S69,
24constraints, all three lowcoefficients still free. Patches preserve three gates but replace
the true upstream profiles, so no actual-root counterexample or asymptotic density statement.

### GC2159 — Signed opposite-arc separation adapter for G134/G135 (waiting for Local)

PROOF-SKETCH variant of the already carried hand argument, classical basis machinery, no novelty
claim. [Exact argument and three uncompiled sources](reports/wolfram-agents/ACTUAL-CONTINUANT-SOURCE-REVIEW.md#gc2159-exact-opposite-scale-separation-now-has-carrying-source):
adjacent-basis errors epsilon,eta have opposite signs. In the spatial strip[-Q-D,D], D<q<=Q,
a return error opposite to eta and smaller than|epsilon| forces coordinates(0,-1). Actual opposite
carry arcs supply the signed error via a floor-difference lift plus/minus1. Coefficient-one actual
continuant recurrences and finite visit bounds give the strip, hence k=h+q_current. Thirteen staged
heads are UNCOMPILED; previous21 passing heads unchanged. The complete251 horizon is not yet assembled.

GC2161 independent carrying read: Local L1168 accepts the complete signed strip, half-open lift and
actual-continuant indexing. **PROVED by hand, two-party; to move out of the waiting room.** The
requested cast normalization is applied; all13new source heads remain UNCOMPILED. No full251 or
current-toolchain certificate follows. Local takes final assembly; GPT source/review work continues.

### Waiting room — GC2205 ruler-closure count (29 October2026)

PROOF-SKETCH, independent read pending: [successive exceptional1(10)^m11 blocks](reports/wolfram-agents/RIGHT-PROFILE-DELIVERY-SPEC.md#gc2205-exceptional-ruler-closures-have-a-deterministic-sparse-count)
have starting exponents e_next>=e+2^e, so completed-block counts have zero density. Known reset/countdown mechanism;
no fair-transition, downstream-influence or new half-rate theorem. The underlying closing-length law is carried
against Cloud's independently written CL645; the new counting argument remains solo. Finite control GC2204 passed.

### Waiting room — GC2206 primitive-front class cardinalities (29 October2026)

PROOF-SKETCH, solo GPT. For k>=5,K>k, the submitted short-inverse classes partition W<2^k in counts2^(k-4),3*2^(k-4),12*2^(k-4). This is an elementary injection/image-count corollary, not a new inverse-tail theorem; exact eight-bit odd classes4/12/48 independently checked in one finite control. No survivor frequency or orbit density. [Proof, guards and source comparison](reports/rule30-primitive-source-review.md#elementary-cardinality-guard--proof-sketch-not-independently-read). Independent reader held without waking Local/Cloud.

### Waiting room — GC2208 clocked driven-boundary interface (29 October2026)

PROOF-SKETCH, solo GPT. Restarting230bc7's driven trace at oddT=2a+1 makes its u R(a+k) the white-even channel observable. The full-root/EdgeOK certificate induction applies directly to a clamped right half, without assuming a whole-line clock extension. Shift-closure language inherits the published path bound. [Exact proof, source and boundaries](reports/rule30-clocked-gap-interface.md#exact-objects-and-the-boundary-guard). No new Lean replay; existing forbidden gaps recovered as prior art. GC2209's finite graph/oracle check passed and does not independently carry this universal interface proof.

### Waiting room — GC2210 guarded00 two-start-bit phase law (29 October2026)

PROOF-SKETCH, solo GPT; [full carrying proof](reports/rule30-zero-pair-phase.md). On an actual finite-seed prefix Q_j=Q_(j+1)=Q_(j+2)=H even, beta/gamma start flips give c'=c+gamma+beta*prefix-XOR(NOTa). The second0 survives iff beta*parity(a)=0; on that branch the next flag is F+beta*A+gamma*B, with A=parity(c XOR(b AND h)), B=parity(b). The alternative01 branch reads the next flag B over2H. One-bit term is already GC2014/L1070; eight fixed controls pass GC2211. Whole older profiles remain required; no root-density, novelty or general00 phase-invariance claim.

### Waiting room — GC2212 finite-precision regularity of the right-edge map (30 October 2026)

PROOF-SKETCH, solo GPT; [full quotient and endpoint proof](reports/rule30-edge-regularity.md). For Phi(x)=x XOR(2x OR4x), the differentiability loci modulo 2,4,8,16 are all 2-adic integers, Z, nonnegative integers and the empty set, respectively. The modulo-four quotient depends exactly on the two bits below the perturbation scale. Ordinary 2-adic differentiability fails everywhere. This closes a direct application of Shi–Anashin–Lin's uniformly differentiable transitive theorem; no density theorem, new experiment, independent read or novelty claim.

GC2213 extends this sketch: exact finite-scale iterate quotients multiply and telescope to the known delayed parity coefficient at prefix returns. Every fixed positive iterate still lacks a common modulo-four threshold even on actual finite-time root states, by the known top-edge growth. [Carrying continuation](reports/rule30-edge-regularity.md#gc2213-the-return-quotient-is-the-known-delayed-phase-coefficient). No new numerical validation or density bound.

### Waiting room — GC2214 thinning consistent periodic drivers (30 October 2026)

PROOF-SKETCH, solo GPT. [Exact reduction](reports/rule30-periodic-mask-review.md#solo-consequence-two-driver-classes-suffice-for-the-strong-assertion): for nonzero e=c AND shift(c), k=previous(e) OR e removes isolated black cells and preserves every remaining effective-consistency pin. For e=0 retain one pulse per period. The strong left-only exclusion reduces exactly to these two classes. No period excluded and no right-half realization preserved; PR57's separately reviewed transport theorem is prior art.

GC2215 adds a [solo ZBL countercontrol](reports/rule30-periodic-mask-review.md#an-aperiodic-actual-zbl-trace-with-every-p-th-bit-black): zeros exactly at P*3^n+1 give an aperiodic trace with every P-th bit black. Known reconstruction realizes it; known Jen clock forces the start infinite. PROOF-SKETCH, no finite counterexample or new priority claim.


### Waiting room — GC2216 reset-free finite predecessor multiplicity (30 October 2026)

PROOF-SKETCH, solo GPT. [Full pair-image proof and boundary guards](reports/rule30-reset-free-review.md#exact-multiplicity-consequence--solo-proof-sketch): a finite zero-wall row has exactly one finite predecessor iff it avoids0 1^(3m+1) 0; a reset gives zero or two. With externally carried PR53, every three successive positive-time rows of a nonzero finite orbit include a two-parent row. Old G13/G141 mechanisms credited. This does not keep either branch alive to a prescribed horizon; the complete13-tree has an immediate dead branch. No independent carrying read or new machine check of this consequence yet.

GC2218: the eight named boundary controls passed once (COMPUTED, not a universal certificate). The same solo argument now gives an exact all-width count: for a_n unique finite-parent targets of width at most n, A(z)=(1+z^2)/(1-z-2z^3); a_n=a_(n-1)+2a_(n-3), initial1,1,2. Finite support growth gives a_n+2d_n=2^(n-1), hence uniform finite-word zero/one/two-parent proportions tend to3/4,0,1/4 with unique fraction at most(7/8)^n. [Full grammar, endpoint guard and prior-art comparison](reports/rule30-reset-free-review.md#gc2218-the-fixed-control-passed-exact-finite-word-counts-by-hand). PROOF-SKETCH; no orbit-density or survival consequence.


### Waiting room — GC2219 exact two-substitution silver-word endpoint (30 October2026)

PROOF-SKETCH, solo GPT. For the carried silver word c(s)=floor(s(2-sqrt2))mod2 and odd convergent i>=3, q=q_i,r=q_(i-1),q'=2q+r,Q=q+r, the longest Q-periodic prefix obtainable with at most two substitutions has length2q'+Q; edits at q and2q' attain it. The next letter raises the minimum cost to three because two residue classes require1+2 edits. [Full signed-arc exclusion, majority proof and hand control](reports/wolfram-agents/UNIFORM-RECODING-DELIVERY-SCOPE.md#gc2219-two-substitutions-have-an-exact-endpoint-set-by-a-residue-chain). Classical Hamming-consensus method credited; no optimum over lags, fixed-edit hierarchy, Rule30-preserving modification, new numerical check or priority claim.


### Waiting room — GC2220 uniform edge-window half-rate and local covering (30 October2026)

PROOF-SKETCH, solo GPT. Restarting the existing kit Path at a gives parameter nu+E(a), because no initial resource is prescribed. Its known potential bound yields e_(2a+2d)-e_(2a)<=d+Q(e_(2a),d)<=d+Q(0,d). Even-endpoint rounding gives every N-window at most N/2+O(log N) doublings, uniformly in depth. Exact homogeneous prefix fibers then give dim_Assouad(K)<=1/2. [Full source comparison, restart proof and metric guards](reports/rule30-edge-odometer-dimension.md#gc2220-the-known-accounting-bound-restarts-in-every-spatial-window). No lower bound, density equality, uniform critical covering constant, novelty clearance, compilation or independent read.


### Waiting room — GC2221 ruler-law control has unbounded critical excess (30 October2026)

PROOF-SKETCH, solo GPT. Starting at s1=3,e1=1 after10, concatenate1(10)^(2^e-1), with e_next=e+2^e and s_next=s+2^(e+1)-1. Every occurrence of the exact carried closing law and the no111 rule holds. At n=s_r-1,2E_n-n=r-1, yet E_n/n tends to1/2. The same construction attaches after any actual finite prefix ending00. [Full occurrence, boundary and density proof](reports/rule30-edge-odometer-dimension.md#gc2221-the-ruler-law-permits-unbounded-critical-excess). Symbolic sufficiency control only, not a Rule30 orbit, full Path model or refutation of the actual critical covering estimate.


### External carrying review — GC2222 PR48 edge-clock source (30 October2026)

Complete external source accepted in stated scope: period h, then antiperiod h, cannot be followed by period h; a constant edge column forces every older column white. An explicit periodic free carrier supports an8-to2 template drop with arbitrary older depth; genuine finite odd codes imitate it through2n+1 ticks at depths4n+3,4n+4. [Proof, boundary guards and evidence review](reports/rule30-edge-clock-drop-review.md). The latter is finite imitation, not an actual all-time period drop. Retained author99-constant/13-headline replay passes; no GPT compiler or new portal/Human Verified claim.

### Waiting room — GC2223 guarded carrier invasion and exact imitation lifetime (30 October2026)

PROOF-SKETCH, solo GPT. [Four-phase guard induction and all exit cases](reports/rule30-carrier-invasion.md): the half-line1110 carrier front advances six depths every four ticks after its exceptional entrance. The closed101/1011/100/100 guard masks arbitrary older cells. For PR48 seeds c_n, first terminal-pair failure is f0=6; f_(3k+1)=8k+6,f_(3k+2)=8k+9,f_(3k+3)=8k+13. A leading-defect-only control lacks the guard. No density/centre-period consequence or novelty clearance; one separately frozen local/table self-check pending, independent carrying read pending.

GC2224: the frozen control passed once, including all four local incoming assignments and the omitted-guard witness. Actual receipts retained; no new independent carrying read or status upgrade for the universal argument.

GC2225 strengthens and clarifies the front law: at phase A the leading defect alone forces6depths/4ticks, with arbitrary older continuation. [Exact trailing map](reports/rule30-carrier-invasion.md#gc2225-exact-guard-map-and-the-remaining-capture-question) gives p'=p AND(q OR r), q'=1 if p1, otherwise q OR NOT(r OR u). Both101 and111 are closed signatures;001 capture for finite older prefixes remains open, and a hand example requires12ticks. PROOF-SKETCH, no new machine check. The omitted101 guard affects the signature, not the phase-dependent speed; GC2223's finite-family exit proof is unchanged.


### Waiting room — GC2231 full-line four-return reproof (30 October2026)

PROOF-SKETCH, solo GPT; known conclusion, explanatory reproof. For Phi(x)_j=x_j XOR(x_(j-1) OR x_(j-2)) on bi-infinite rows, Phi^4(x)=x iff Phi^2(x)=x. G258 forbids odd-weight four-profiles; a primitive0011 profile forces two older0101 profiles and then a newer forcing0111 with odd parity, impossible at clock four. [Complete proof, known two-return classification and scope controls](reports/rule30-full-line-small-clocks.md). A finite older-side chain can end in0011 but its next profile has clock eight. No centre-column conclusion, higher-clock classification, new numerical check or independent carrying read.


### External carrying review — GC2232 finite eight-return criterion (30 October2026)

PR33 current395-line source09aa298b accepted in its all-width finite-white-boundary scope. Its36-pair certificate and length induction give eight-return iff two-return after deleting three newest cells; the first two/eight-step discrepancies are exactly three cells apart when present. The newest-first state bridge preserves full equality through same-length injectivity. [Source, hand certificate reduction and retained evidence](reports/rule30-finite-return-eight-review.md). Current128/four-headline replay is reported by author with maintainer headline confirmation; older26/three-headline raw replay separately inspected, no GPT compiler. Safety completeness remains open.

### Waiting room — GC2233 two-run even profiles force the next doubling (30 October2026)

PROOF-SKETCH, solo GPT. In an actual forward Phi spacetime, a q-periodic temporal profile with exactly one white and one black cyclic run, even q>=4, forces its two older profiles to equal Delta C and its next newer profile to have least period2q. Known G258 forces lengths2and q-2; known GC798 projection plus one more actual equation forces the ancestors, then the next forcing has odd weight and least periodq. For q>4 the consecutive periods are q,q,q,2q; for q4 they are2,2,4,8. [Complete proof and scope guards](reports/rule30-full-line-small-clocks.md#gc2233-an-even-two-run-profile-forces-the-next-period-to-double). No white-root occurrence, frequency, general00 closure, new compute or independent carrying acceptance.


### External carrying review — GC2234 oriented height (30 October2026)

[Exact signed-event identity and oriented safety converse](reports/rule30-oriented-height-review.md) accepted in scope for arbitrary Boolean drivers. Both complete sources and retained43/8 plus13/3 author replay/headline records read; no GPT compile. The integrality argument and initial-colour mark are essential. No finite-white safety completeness, root frequency or period bound follows. GC2235's separate core-only ancestor draft is UNCOMPILED at freeze and does not upgrade the GC2233 hand period theorem.


### External finite witness and failed development check — GC2236–GC2237 (30 October2026)

GC2235's final core theorem failed elaboration:7helper/control heads have empty reported axioms, final head has sorryAx, and the module is NOT accepted. [Exact failure and caps](reports/rule30-full-line-small-clocks.md#gc2236-the-core-check-stopped-on-an-elaboration-error); no rerun. Separately, [GC2237 finite reset witness](reports/rule30-reset-excursion-review.md) is independently carried with defining semantics and6/1 author replay/headline evidence. Its unsafe initial00 trace limits the conclusion to one-excursion parent decoding, not safety completeness.


### Waiting room — GC2238 run-count next-period law (30 October2026)

PROOF-SKETCH, solo GPT. [Exact inverse and period proof](reports/rule30-run-period-law.md): for an actual q-periodic profile with every cyclic run length at least2, both older profiles equal Delta C. The next forcing C OR SC is inverted by adjacent AND and has least periodq; the next newer profile has least periodq or2q according to parity of black cells plus black runs. Known kit input-parity rule credited. No root occurrence/density/general00 theorem or successful core-module compilation.

### External carrying review — GC2239 transition-cover obstruction (30 October2026)

[Complete normalized derivative-chain theorem and evidence](reports/rule30-transition-cover-review.md) carried in scope. Every nonzero dyadic word has a TC chain; actual shared OR recurrence is absent. Raw37constant/3headline author replay accepted in scope, no GPT compiler. The added0001 hand control and pair-projection explanation are solo sketches, not independently reviewed new claims.


### Development validation — GC2241 core ancestor and inverse (30 October2026)

[One changed-source check](reports/rule30-run-period-law.md#gc2241-the-repaired-core-and-inverse-pass-the-development-check):13core heads compile on4.33.1 with empty axioms, expected false-negative and16/8 finite controls pass. GC2236 failure remains retained. This validates local Boolean/forward-profile steps only; no formal least-period/count proof, independent carrying read or official4.35 replay.

### External carrying review and waiting room — GC2242–GC2243 (30 October2026)

[Antiperiod-height source and free-partner construction](reports/rule30-antiperiod-height-review.md). Existing necessity is carried with26constant/6headline author evidence: periodic b, antiperiodic c and safe child imply zero drift/height diameter<=2. New converse is solo PROOF-SKETCH: the height criterion exactly characterizes existence of some freely chosen antiperiodic partner and a safe child returning after2P. Binary-track endpoint exchange is explicit. Neither actual shared ancestry nor a converse for a prescribed c follows; no new trajectory computation.


### Fixed validation and waiting room — GC2245–GC2246 (30 October2026)

[One fixed constructor pilot and exact partner-count sketch](reports/rule30-antiperiod-height-review.md#gc2245-the-fixed-pilot-passes-once). All84P2/4/6drivers agree with8736independent partner/initial-colour cases; endpoint-exchange mutant rejected, receipts retained, no repeat. The universal free-partner theorem remains solo. GC2246 counts safe phase-anchored pairs as2^(P-k+2-D) for2k>0white ticks and height spanD1or2 with zero drift; all-black case2^(P+1), failed criterion0. The bijective excursion proof is PROOF-SKETCH; all84existing counts match without new dynamics. Actual shared ancestry remains absent.


### Waiting room — exact free-partner driver language (GC2247, 30 October2026)

[Carrying proof](reports/rule30-free-partner-language.md), solo PROOF-SKETCH. For P=2m the zero-drift/diameter2 height language has trace(M2^m)-trace(M1^m) phase-anchored words. The three containing strips and two nontrivial overlaps establish the formula; the even/odd intermediate-height guard fixes the top loop count. Dominant cubic root gives an exponentially small fraction of all binary words. This uses known bounded-Motzkin transfer matrices and, for the free-partner interpretation, GC2243's solo converse. No actual-root frequency conclusion or new enumeration.


### External carrying review — the exact D3 equivalence (GC2248, 30 October2026)

[Source, induction and guard audit](reports/rule30-d3-completeness-review.md). RootD3Reduction013b6889 and CedarD3Converse1db70283 are carried in conditional scope: normalized safe words have a safe prefix1–3cells earlier iff all safe finite-white words return8. Neither assertion is proved. The short-extension dependency repeats only an already-returning prefix; full extension safety remains all-time.529retained author replay declarations/20headlines checked across two checkpoints, no GPT replay. Generated trajectory certificate evidence and individual hand-reading limits are explicit. Known1000010 demonstrates why EightWindow alone is insufficient.


### External carrying review — arbitrary-future gate-past closing (GC2250,30 October2026)

[Exact source/evidence](reports/rule30-gate-past-closing-review.md): finite4–7bit covers prove spatial closing for every infinite legal future. Absorbing full-past column pairs and finite tree soundness were read. The all-length conditional finite-row exclusion uses exact support preservation and periodic splicing, not a linear closing bound. AllPastClosing/FiniteCoverFamily remain open. Author3057replayed/37headlines and exact13source closure retained; no GPT replay, generated-reduction and guard limits explicit.


### Waiting room — exact finite-cover completeness (GC2251,30 October2026)

[Complete hand converse](reports/rule30-gate-past-closing-review.md#gc2251-the-finite-cover-format-is-complete-for-qualitative-closing), solo PROOF-SKETCH. For each fixed n, qualitative closing yields an equal pair of full finite-past columns by actual outer locality, hence a finite-prefix leaf. Finite-past legality and canonical packed triangles give the exact PR52 format; König's lemma produces finite root trees. Thus Closing(n), Cover(n) and a uniform cutoff are equivalent. This does not prove their truth for every n, an explicit rate, or a new finite-row exclusion. Independent read and formalization remain pending.

### GC2253 — The finite carrier exit has two different newer-clock outcomes

PROOF-SKETCH, solo hand specialization of the known parity rule. [Exact equations and source-scope correction](reports/rule30-carrier-reach-pilot.md#exact-hand-diagnosis-and-the-other-exit-choice): PR48's endpoint234,170has forcingEAof odd weight, so either next initial bit gives least period16. Choosing85instead of170one step earlier joins the alternating tail and matches PR58's existing witness. No full-line16-return, new novelty claim or completed q16 computation. The failed positive control is retained.


### Waiting room — Boolean gates and an AND branch label (GC2258,30 October2026)

[Complete carrying steps and evidence](reports/quadratic-edge-clock-transfer.md). PROOF-SKETCH: own-bit-XOR triangular updates with arbitrary time-independent two-input Boolean gates satisfy the kit's record-charge window bound, hence upper clock rate and Assouad dimension at most1/2. The generic vanishing argument transfers inequalities without dividing by the quadratic coefficient. All-affine gates have a standard logarithmic bound. Separately, on AND's x0=x1=1 branch, C=x5 XOR x2*x3*x4 distinguishes two six-bit8cycles; seeds3 and35 have equal prefix clocks through j8 but different E9. Solo hand results, not compiled; the frozen80case control covered the earlier quadratic family only. Known Skirrow domino formula and kit mechanism credited. Section2 independently carries Cloud's four elementary break rules in corrected scope.

### Waiting room — choked gates and backward periodic branches (GC2261–GC2270,30 October2026)

[Exact arguments and scoped answer table](reports/cloud-question-workflow-20261030.md). Solo PROOF-SKETCH: for odd seeds, g=b AND NOT s has E(n)<=ceil(log2(floor(n/2)+1)); g=NOT b AND s has E(n)<=ceil(log2(floor((n-1)/2)+1)). Forced constant coordinates give an invariant affine subsystem. A mixed least-period-p spatial driver has parent period exactly p or2p, determined by the permutation of the at-most-two-state recurrent image; constant-one has the separate3cycle. The complete background graph restricts every finite root through40inverse steps to two period sequences; the graph-to-root reduction awaits carrying review. The two final necklaces differ, no all-depth coalescence claim.

Further solo identities in that account: corrected physical finite-parent count2^(w-4) forw>=4, physical/wall bridge T(r)=(r mod2)+2Psi(r), exact reversal response and a specified fresh-bit conditional law. Cloud's antiperiodic-support and physical finite-parent/depth arguments are carried in corrected scope; their source assertions and corrected corollaries are distinguished. Five passed stages, a retained failed control and an unclosed P128substep are separately documented. No new Lean or Human Verified status.

### Waiting room — outside-edge clock imitations and backward period family (GC2272,30 October2026)

[Full short arguments](reports/cloud-revised-questions-review-20261030.md#gc2272-two-immediate-answers-in-the-revised-list), solo PROOF-SKETCH. Known realization with a white right half and trace0101... has rightmost initial black at-1; truncation to[-N,-1] preserves that trace through timeN. This refutes CL663 A6's proposed width-independent constant outside the right edge, without asserting an eternal clock from a finite row. Separately, E2's mixed-driver p/2p law and the initial black/period3 tails imply least backward tail periods3*2^e at every finite depth>=2, for any finite root's white-right history. No branch-count, growth or coalescence theorem. Current RingOrbits' temporal1/2 classification is a different statement.

### Waiting room — a conditional ether return and exact fixed-left optimum (GC2274–GC2276,30 October2026)

[Complete carrying steps](reports/rule30-relay-witness-audit.md). PROOF-SKETCH: the specified seven-cell path0010000->0111000->1100100->101111u->0010000 is equivalent to left exterior inputs0001 and right inputs00uv with u OR v=1. The u=1 orbit is known Rule30Ether; arbitrary boundary histories are not physical realizations. Separately, for the entire initial half-line i<=7 black only at0,7 and centre8white, first failure of0101... is at most17 for every right completion. The forced right samples010101001 contain the already certified finite forbidden word101001; finite row {0,7,14,17} attains17. New independent carrying read needed for the frame/finite-prefix transfer; existing certificate is credited, not recompiled. Two finite controlled computations and receipts retained in the linked account; the predicted improvement to18 failed.


### Waiting room — dyadic phase clocks preserve the proposed half-rate mechanism (GC2278, 30 October 2026)

[Complete carrying argument and failed unscaled control](reports/quadratic-edge-clock-transfer.md#12-gc2278-curiosity-pull--a-fixed-dyadic-phase-clock-can-be-absorbed), solo PROOF-SKETCH. For own-bit-XOR updates with two earlier inputs and coefficients sharing a fixed temporal period L=2^ell, include the phase in every prefix clock and use floor(order/L). Block differences yield the same reset/countdown Path with parameter E_a-ell, hence the proposed window bound. An actual phase-2 three-bit example refutes the unscaled reset law. L=1 recovers the static argument. No odd-period/nonperiodic conclusion, density equality, independent read, compilation or novelty clearance. This is separate from the current static submission candidate.


### Waiting room — arbitrary finite forcing clocks (GC2281,30 October2026)

[Full two-difference proof](reports/quadratic-edge-clock-transfer.md#13-gc2281-use-a-phase-step-difference-for-any-fixed-forcing-period), solo PROOF-SKETCH. For a common finite temporal period L and own-bit-XOR gates with two earlier inputs, the phase-augmented prefix periods are L*2^K_j. The phase-step difference D_L=S^L+I commutes with ordinary Delta; cancellation gives the forward vanishing implication needed for reset/countdown and Path(K_a). Thus the proposed window bound for K has the same thresholds as the static theorem, including odd L. The L-step composite need not have two-input memory and is not used. No nonperiodic/longer-memory claim, independent read, compilation or new dynamics; kept separate from static Package A.


### Waiting room — exact ancestral-age count and temporal memory recovery (GC2284–GC2285,30 October2026)

[Ancestral-age argument](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2284-a-counting-consequence-for-finite-ancestral-age), solo PROOF-SKETCH derived from the already carried G121/L077: uniform normalized width-w words have Pr(A>=k)=C(w-2k)/C(w), with the width-one correction and exact finite means tending to1/3. No orbit measure, independence assumption or novelty claim. [Memory recovery](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2285-the-hidden-memory-bit-is-ambiguous-only-at-c-to-b), solo PROOF-SKETCH from the actual two lower recurrences: C,C forces hidden h=0, C,A forces h=1, and only C,B retains a local choice. This gives a finite-prefix counting upper bound, not global ancestry or return-word injectivity. Neither has an independent carrying read or new compilation. GC2282 corrects attribution of the finite-past core to G121/G122 and L077; it does not promote these two new consequences.


### Waiting room — finite ancestry with at most three black cells (GC2289,30 October2026)

[Complete argument](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2289-at-three-black-cells-finite-ancestry-has-depth-at-most-two), solo PROOF-SKETCH. One/two-black rows are roots. A three-black width-w row has a parent only if it is11 0^(w-3)1; that parent is the solid width-(w-2)block, which has a root predecessor exactly when3divides w-2. Therefore all three-black ages are<=2and the fixed-width/fixed-three-black mean is(1+[w=2mod3])/(w-2). Known G121/G122/L077 and GC544/GC593/CL058 mechanisms credited. No monotone black-count assumption, numerical fit, orbit law, independent read or compilation. The separate GC2286/GC2288 Lean sources transcribe the older finite core and remain UNCOMPILED after the pilot stopped in an unchanged dependency.


### Waiting room — four-black finite ancestry has sharp age bound four (GC2291,30 October2026)

[Complete proof and branch table](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2291-four-black-cells-have-ancestral-age-at-most-four), solo PROOF-SKETCH. Every nonroot four-black row at0,1,k,R has k>=3 and parent1^(k-2)0 1^(R-k). The inverse table reduces the exceptional branch to11(001)^q and then(110)^(q-1)111, whose parent exists exactly for odd q and is a root. The sharp bound is4, attained by110010001. No independent read, machine computation, general fixed-mass bound or novelty claim. Known G121/G122/L077 and current Preimages machinery credited; GC2290 also records the externally known OEIS root/age definitions.


### Waiting room — finite mass and one-step parent counts (GC2296,30 October2026)

[Complete hand argument](reports/rule30-finite-mass-parent-count.md), solo PROOF-SKETCH. A nonzero finite parent's image has population r+2+2h, where r counts black runs and h counts internal white gaps of length at least2. Positive run/gap compositions and known finite injectivity give an exact rational width/mass enumerator and fixed-K parent fraction asymptotic to(K-2)/w. It recovers the known all-width counts and low-mass shapes. No maximal/mean age or actual-orbit conclusion;1001->111111 refutes run monotonicity. Independent carrying read pending; excluded from Package B.


### GC2298 / GC2305 — exact two-past gap counts, carried L1238

[Full boundary machine and phase-path argument](reports/rule30-two-step-finite-past.md), PROVED two-party hand in
L1238's scope: the16state inverse accepts precisely finite two-step ancestors; zero gaps have period3after2;
fixed-mass counts are eventual period3quasipolynomials. The leading coefficient is the explicit binomial-residue
filter of GC2305. The ratio to one-past counts still requires soloGC2296. No single-root or age conclusion.

### Waiting room — compact two-past series and exact mass moments (GC2307–GC2309)

[Complete new carrying steps](reports/rule30-two-step-finite-past.md#gc2307-a-seven-state-quotient-and-compact-exact-bivariate-series),
PROOF-SKETCH: seven quotient states and exact zero-padding removal give H=z^5u^3PS/(P^2-z^2uPR-z^3S^2),
P=1-z, R=P+zu^2, S=P+zuR. GC2308's one frozen exact-arithmetic control passes; this is a self-check, not a carrying
read. Separate pole/derivative algebra gives, for uniform normalized width-W rows with two finite past steps and
W>=16, mean W/2+1 and variance W/4-7/8. The new algebra/moments remain unreviewed and are outside deliveredB.


GC2310 status amendment: L1240 independently carries GC2307's quotient, elimination and padding, now PROVED
two-party hand. GC2309's later moments are still a solo sketch. L1239's generic no-three law is also carried by GPT;
its proposed next-doubling and inner-countdown steps now have explicit guarded GPT proofs awaiting Local.


### Waiting room — nested gate-clock record thresholds (GC2311)

[Complete last-ascent and last01 proof](reports/rule30-gate-clock-sharpness.md#gc2311-a-last-ascent-argument-closes-losses-and-recoveries),
PROOF-SKETCH. For static two-input GateClock with e(0)=0, e(2m)<=m+2 for m<2058. The first higher-record interval
is trimmed after the last lower-level visit, permitting arbitrary earlier00losses and recoveries; initial first-bit
countdown and final last-bit countdown give the bound. Recursive T_q written in the source. No attainment, lower
clock rate, single-root density, compiler result or larger beam. L1241post11order M-2 carries independently here.


GC2312 status amendment: the nested gate-clock record thresholds are PROVED two-party hand by Local L1243's
complete carrying read, agreeing with its independent L1242 draft. Local owns the separate Lean preparation;
no compilation or submission of this sharpening yet. The actual L1241 single-family witness/receipts are read,
with its period replay accepted only through 38 bits and its manifest sanitation-length distinction recorded.


### Waiting room — direct finite-image boundary covariance explanation (GC2313)

[Complete elementary argument](reports/rule30-two-step-finite-past.md#gc2313-the-variance-correction-comes-from-four-boundary-covariances),
PROOF-SKETCH. A triangular bijection makes L-2 output bits jointly fair independent in the two-step image of a
uniform normalized ancestor of width L=W-4. Four left-boundary bits have variance3/8; their only nonzero bulk
covariances are1/8,1/64,-1/64, summing to1/8. Thus the mean W/2+1 and variance W/4-7/8 hold for W>=14.
Independent derivation of solo GC2309, not an independent worker read, new computation, fixed-mass or root-orbit law.

L1251 status amendment: Local read every carrying step, so GC2313 is now **PROVED two-party hand** for W>=14.
An exact control by plain Rule 30 steps (`gc2313_moment_check.py`, W=12..20) matches it from 14 to 20. It also shows
the guard is sharp: at W=12 and 13, Cov(S,Z_8)=0 and the variance exceeds W/4-7/8 by 1/32. GC2309's pole argument
stays solo.


### Waiting room — finite-image binomial coupling and constant cumulant corrections (GC2314)

[Complete proof and guards](reports/rule30-two-step-finite-past.md#gc2314-every-fixed-ancestry-depth-has-a-binomial-bulk-and-finite-boundary-corrections),
PROOF-SKETCH. Uniform normalized width-W rows with at least t finite past steps, W-2t>=2: K=2+S+B with
B~Binomial(W-2t-2,1/2),0<=S<=2t, possibly dependent. Fixed-order cumulants have a width-independent correction
at W>=2t(r+1)+2 by connected input cones. Classical binomial CLT transports when t=o(sqrt(W)); no root-orbit law.
The generic triangular fair-bit and CLT ingredients are known kit results, credited. One frozen moment-only control
GC2315 has not run at this entry and cannot independently carry the hand argument.

GC2316 update: the six-case moment control passed once; all finite controls and actual evidence retained.
The general hand statement remains PROOF-SKETCH. GC2317 separately accepts L1244's full nested gate-clock
development source and exact threshold meaning; this is not an official-checker or new submission receipt.


### Waiting room — bipermutive finite-image control and the missing Rule30 estimate (GC2321)

[Bipermutive boundary control](reports/rule30-two-step-finite-past.md#gc2321-a-bipermutive-control-isolates-the-missing-boundary-estimate), PROOF-SKETCH. For a quiescent bipermutive diameter-D Boolean rule and uniform normalized input of width L,
output width W=L+D has mean W/2+1 for L>=D+2 and variance(W-2)/4 for L>=2D+2. The latter uniform guard is sharp.
Two separate binomial marginals, which need not be independent, give a classical Gaussian transport for D=o(W).
Rule30 lacks the second permutivity property. Its sufficient open target is Var(S_t)=O(t), equivalently an O(t)
bound on the sum of squared conditional martingale increments; centering at W/2 separately needs small bias.
Known triangular independence and Doob mechanisms credited. No computation, independent carrying read or root claim.

### Waiting room — three hand steps from the 31 October inquisition (Local, L1256–L1257)

[Full statements, proofs and their exact controls](reports/inquisition-20261031.md). PROOF-SKETCH (Local solo; GPT's
carrying read requested in [the handover](reports/HANDOVER-GPT-20261031.md)):
1. **Death kinds are a fair coin before the news.** In the kit's normal form, for an even death time t with
   2 ≤ t ≤ W − 1, the starts of width W dying at t split exactly half starved, (x_2, x_1) = (0, 0) at t − 1, and half
   cancelled, (1, 1). Pairing: flip depth t, then flip depth t + 1 iff x_1(t) became black. Both depths reach depth 1
   only at the cone's XOR edge. COMPUTED exact at every such t, W ≤ 20.
2. **Two adjacent left diagonals are coordinates.** For every n, the map from a base row segment of 2n cells to the
   two left diagonals {(−t, t), (−t+1, t) : t < n} is a bijection. Each strip cell's leftmost input enters by XOR, and
   these inputs are distinct, so the map is triangular. COMPUTED N(n) = 4^n, n ≤ 9.
3. **No right diagonal carries 00100 or 11011.** The flips along s(t) = x(t, t) are x(t+1, t) OR x(t+2, t). The
   flip word 0110 is impossible by a two-case analysis on x(3, 0). COMPUTED: the minimal forbidden words to length 10;
   absent in about 6,000 random diagonals of 2,000 steps.

No centre-column or prize inference.


GC2326 status amendment (31 October 2026): GPT has independently carried all three Local steps above. They are
**PROVED, two-party hand**, with the death-pairing ensemble clarified to all starts *supported within* W, not
necessarily having a black final cell. The diagonal-word claim is already G258 (October 9), known and reproved
here; Local's numerical runs were not replayed. [Scoped carrying read](reports/GPT-INQUISITION-20261031.md#carrying-reads-gc2326).

### Waiting room — finite ether episodes beside a moving black edge (GC2327–GC2328)

[Complete upper proof and lower family](reports/GPT-INQUISITION-20261031.md#a-finite-ether-window-bound-gc2327-proof-sketch),
**PROOF-SKETCH**. Applied to Lowry's exact PR69 invariant, eight phase-dependent local implications and a 17-edge
potential give no good-pair interval of length floor(2k/3)+5 at depth k. A parity guard handles the only past-time
premise. A concrete actual ether, with its edge replaced by black, has a masking-front bound floor(3t/2), and
prefix autonomy gives finite-row matching episodes of length ceil(2k/3). Therefore the maximal episode length
M(k) lies between ceil(2k/3) and floor(2k/3)+4, so M(k)/k tends to 2/3 in both finite and arbitrary black-edge row
classes. One frozen finite self-check passed; it preceded the lower construction. No independent carrying read,
compilation, exact additive sharpness, global orbit speed, fixed-centre or doubling-density claim. Review the phase
3 past dependency, the phase 6 three-tick case, and the masking-front/truncation step before any delivery.


L1258 status amendment (31 October 2026, Local): Local has independently read both GC2327 and GC2328 against PR69's
actual source (head fcffbaa9): all eight local implications, the 17 potential edges, the parity guard, the phase
identity, the edge-phase table, the masking-front lemma with its four reference bits, and the truncation. Both are
**PROVED, two-party hand**: ceil(2k/3) <= M(k) <= floor(2k/3)+4, so M(k)/k -> 2/3. Local's exact computation
(`tests/probes/ether_episode_exact.py`, k <= 20, output 3dd3599b) finds every M(k) inside the bounds and the GC2328
witness attaining M(k). [Carrying read and T-M](reports/inquisition-20261031.md#outcomes-of-round-3).

### Waiting room — the exact ether-episode constant for k ≡ 1 (mod 3) (Local, L1258)

[Hand step](reports/inquisition-20261031.md#a-sharper-lower-bound-by-hand-local-proof-sketch), **PROOF-SKETCH**,
for GPT's read. The GC2328 witness heals at once: X(1) = E(1) and X(2) = E(2) at every depth, edge included,
because E's own OR masks the black edge. At t = 3 the two agree beyond depth 0. Restarting the masking front there
(advance two at odd t, one at even t; reference bits E_(3n+3)(4+2n) = ether(2,5), ether(1,7), ether(0,1),
ether(3,3), all 1) gives R_t = ceil(3(t-3)/2). Hence M(k) >= floor(2(k-1)/3) + 4. With GC2327 this makes
M(k) = floor(2k/3) + 4 exactly for k ≡ 1 (mod 3). COMPUTED (k <= 20), CONJECTURE beyond:
M(k) = floor(2k/3) + 4 - [k ≡ 0 or 2 (mod 6)]. Moving black edge only; no fixed-wall, centre or density claim.


GC2330 status amendment (31 October 2026): GPT has carried L1258's early healing at t=1,2,3, checking the special
depth-one boundary update separately, all four masking reference bits, the integer endpoint count and truncation.
The waiting-room step is **PROVED, two-party hand**: floor(2(k-1)/3)+4 <= M(k) <= floor(2k/3)+4, and
M(3n+1)=2n+4 for every n>=0. The all-residue formula remains a conjecture beyond the reported k<=20 computation.
[Detailed carrying read](reports/GPT-INQUISITION-20261031.md#gc2330--carrying-locals-early-healing-refinement).


### Waiting room — the exact mismatch front of the GC2328 witness, and M(k) for every k ≢ 0, 2 (mod 6) (Cloud, CL669)

[Certificate and argument](reports/inquisition-20261031.md#round-4-2026-10-31-cloud-cl669-the-exact-mismatch-front-of-the-witness-the-final-tick-for-k--3-5-mod-6-and-why-the-even-residues-are-different),
**PROOF-SKETCH** (Cloud, solo; a finite certificate plus the two-party front lemma), for GPT's or Local's read.
For the GC2328 witness the maximal mismatched depth is R*(t) = 2 floor((3t − 8)/4) for every t ≥ 4 (direct to
t = 12; then a band of depths [b(t), R*(t)+1], content 111010111 at t = 12, evolves on its own by the masking rule
with E above it by the two-party lemma ceil(3(t−3)/2) ≤ R*(t)+1, and returns shifted by 12 after 8 ticks under the
ether's (2, 4) glide). The front never rests on an odd depth, so the witness's episode at (k, k+1) has length
ceil((4 ceil(k/2)+8)/3) = floor(2k/3)+4 − [k ≡ 0 or 2 (mod 6)], and with GC2327:
M(k) = floor(2k/3) + 4 for all k ≡ 1, 3, 4, 5 (mod 6). For k ≡ 0, 2 (mod 6) only the upper bound is open; the exact
max-plus form of GC2327's tree is already floor(2k/3)+4, the good predicate is exact at k ≡ 0 and loose by one at
k ≡ 2 (mod 6) (computed to k = 20). Moving black edge only; no fixed-wall, centre or density claim.


GC2331 status amendment (31 October 2026, GPT): CL669's carrying argument is independently read and **PROVED,
two-party hand**. GPT checked the bootstrap by explicit hexadecimal rows, U-R by all four residues and the guarded
band's four-tick/six-depth return by hand. First-arrival arithmetic proves the full witness length for every k.
Consequently M(k)=floor(2k/3)+4 for k≡1,3,4,5 mod6. The universal upper improvement for residues0,2 is still open;
Cloud's finite diagnostics do not close it. Exact-pair descent has the necessary endpoint guard t<=L-2.
[Full carrying read](reports/GPT-INQUISITION-20261031.md#gc2331--clouds-exact-front-carried-with-a-four-tick-band-certificate).


### Waiting room — the exact ether-episode length M(k) for every k (Local, L1259)

[Theorem, three proofs and their verification](reports/inquisition-20261031.md#outcomes-of-round-5-mk-for-every-k),
**PROOF-SKETCH** (Local; machine certificates with controls), for GPT's carrying read. For every k ≥ 1,
M(k) = floor(2k/3) + 4 − [k ≡ 0, 2 (mod 6)]. At edge phase 7 the GC2328 witness is the unique optimal prefix.
- **Proof 1, the front potential.** In the two-sided frame the mismatch front's moves follow an 8-phase table, and
  Φ = R + g(ψ) − 3t/2 is invariant. There is no retreat after tick 0. The floors at t = 1 (the c = 2, 4 exclusion
  and the c = 7 dichotomy) give R(t) ≥ R_w(t) for every row and phase. Certificate:
  `ether_front_potential_certificate.py`.
- **Proof 2, the six-depth descent.** An exact window of length L ≥ 11 at depth j forces the exact ether at depth
  j − 6 on 0..L − 5, for every phase. That reduces to 56 light-cone windows, enumerated exhaustively; the bases are
  M(1..8). Certificate: `ether_six_depth_descent_certificate.py`.
- **Proof 3, rigidity with LRAT.** GC2327's tree for r ≠ 7, plus 254 LRAT-checked local systems for r = 7.
  Certificate: `ether_rigidity_certificate.py`.
- **Steps to read.** For Proof 1: the two-sided reduction, Lemma B, the t = 1 floors and the modified-row reduction.
  For Proof 2: the light cone, translation, window containment and the induction. Either proof alone suffices.
- **Self-checks so far.** Twelve same-worker verifiers, none refuting.
- **Scope.** Moving black edge only; no fixed-wall, centre or density claim.


GC2333 status amendment (31 October 2026, GPT): L1259's all-depth formula and phase-seven prefix uniqueness are
**PROVED, two-party hand**, via the front-potential proof with the corrected hypothesis of right-bounded mismatch
(finite positive mismatch, not finite support on Z). GPT carried all requested hand steps, including the healing
exclusion and clean-tail induction, and replayed the small finite certificate with a rejected-potential control.
Proof2's requested hand reductions also check; its finite enumerations were source-read, not rerun. No independent
LRAT replay or Lean verification is claimed. [Full carrying read and evidence](reports/GPT-INQUISITION-20261031.md#gc2333--l1259l1260-reviewed-the-all-depth-maximum-and-the-phase-seven-optimum).


### Waiting room — same-edge rigidity for eight periodic backgrounds, including the classic 7 × 4 ether (Local, L1261)

[Statement, certificate and scope](reports/inquisition-20261031.md#outcomes-of-round-6-which-periodic-backgrounds-a-black-edge-can-follow), **PROOF-SKETCH** (hand reduction by Local; machine certificate with
checked LRAT proofs), for GPT's read.
- **Claim.** No black-edge code follows white, PR69's one-in-four ether, (5, 5), the classic 7 × 4 ether (7, 28),
  (8, 20), (9, 72), (10, 6) or (12, 12) at two adjacent depths forever. Episodes are at most M_R(1) + (a + b)(k − 1).
- **The steps that carry it:**
  - black-edge codes as generic two-sided configurations, and the light cone;
  - the onset-free descent: time translation, so each tick a..L − 1 − b of the shallower pair is covered by a window
    inside the episode;
  - the base M_R(1) finite.
- **Certificate.** `inquisition_background_rigidity_certificate.py`, 1,266 windows, kissat and cadical, LRAT-checked,
  with replay controls.
- **Open.** (7, 63), (9, 57) and (12, 68) have shadows and remain open beyond k = 12.


L1262 status amendment (31 October 2026, Local): M(k) = floor(2k/3)+4-[k ≡ 0, 2 mod 6] for every k >= 1, and the
phase-7 prefix uniqueness, are now **kernel-checked in Lean 4.35** (`lean/Rule30EtherEpisode.lean`, SHA256
33aff7322077fb0b…, core Lean, imports only the kit's `Rule30FrozenRuler`; standard axioms only; two independent
same-worker verifiers, one with a standalone kit-independent re-check). [Details](reports/inquisition-20261031.md#the-lean-formalization-of-mk-l1262).
No submission.
