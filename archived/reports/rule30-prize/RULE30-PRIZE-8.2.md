# RULE30-PRIZE.md section 8, volume 2: 8.58 to 8.90

*Part of [RULE30-PRIZE.md](../../RULE30-PRIZE.md), section 8 (the right side as a complement). Moved here unchanged on 2026-10-28 by Local at the owner's request: RULE30-PRIZE.md had reached 760 KB, and section 8 was 95% of it. The table in RULE30-PRIZE.md section 8 lists every sub-section. 33 sub-sections.*

### 8.58 The window principle: Theorem A′, and what the Collatz twin shows is missing (2026-10-05)

*Local. The owner asked for the Collatz avenues to be carried back to Rule 30. The two-problem account is
COLLATZ-PRIZE.md §5. This section is the Rule 30 half. Probe `rule30_window.py`, predictions committed first.*

Collatz has a fact so simple that it is rarely stated: two iterates with the same next $n$ parities are congruent
modulo $2^n$. Rule 30 has the same fact, and it gives a shorter proof of Theorem A (§8.54) and a stronger
statement.

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

Theorem A is the case where the block recurs because the columns are periodic: a window $[a, b]$ of period $P$
is a block of length $b - a - P + 1$ that recurs at $a' = a + P$. Jen's theorem is the case of a block that
recurs for ever. Theorem A′ needs no periodicity, only one repeat.

**Checked** (`rule30_window.py`): over every seed up to 9 cells, every column pair from the seed's left end to 8
cells past its right end, and every pair of times up to 120, there are 7,436,643 recurring blocks and none
longer than $L + a'$ (WN1). With the earlier time $a$ in place of $a'$ the bound fails 20,179 times (the
counterfactual). I predicted the bound would be attained by some seed of 3 or more cells at $a' \ge 2$. It is
not (WN2 refuted in that half). Late blocks are far below it: the longest block recurring at a time between 240
and 360 is 19 cells. That is the growth of a coin's longest match, a logarithm of the number of pairs of times.

**The window identity.** For the forced left half next to column 0 = 0101…, the $2n$ cells beside the wall and
the next $n$ visible bits of column 1 determine each other (Lemma 4, §8.39). So for any column 1:

```math
p_c(n) \;=\; \text{the number of different contents of the } 2n \text{ cells beside the wall, over all even times,}
```

where $p_c(n)$ counts the different blocks of $n$ visible bits in column 1. Theorem A′ says the first
$n - L/2$ of those contents are all different, so $p_c(n) \ge n - L/2$. The channel bound (§8.33) says a real
right half allows at most about $2^{0.13\,n}$.

**The cost side as one sentence about one orbit.** Put the two together:

> A period-2 counterexample must keep the $2n$ cells to the left of its centre column within $2^{0.13\,n}$
> different contents for ever, for every $n$. Period 2 follows from any proof that a finite configuration's
> window shows more than that for one $n$.

This is the entropy squeeze of §8.33 in the form of a count. What is new is the comparison with Collatz
(COLLATZ-PRIZE.md §5). There the same count has a free lower bound, because a state is a number, small
numbers are few, and each has its own future. Rule 30's states grow by one cell a step whatever happens, so the
edge certifies only $n - L/2$ contents, against the $2^{0.13\,n}$ needed. Every measurement says the true count is
far higher: a chaotic left half shows a new content at almost every step. Nothing proves it for a single orbit.

**The first three columns are affine in column 1** (a small exact fact, used in COLLATZ-PRIZE.md §5). Write
$c_s$ for column 1 at time $2s$. Given the wall's conditions, at times $2s$ and $2s + 1$:

| Column | $-1$ | $-2$ | $-3$ | $-4$ |
|---|---|---|---|---|
| time $2s$ | $\bar c_s$ | $c_s$ | $\bar c_{s+1}$ | $c_s\,c_{s+1}$ |
| time $2s + 1$ | 1 | $c_{s+1}$ | $\bar c_{s+1}$ | $c_{s+2}$ |

Column $-2$ is column 1 with every visible bit held for two steps, and column $-3$ is its complement one step
on. The first product appears in column $-4$. A real right half never shows two visible ones in a row (Lemma 3, §8), so
for it column $-4$ is white at every even time. With column 1 all white the table gives the stripes
$1, 0, 1, 0, \dots$, which are a fixed point of Rule 30: the forced left half's resting state. A visible one in
column 1 is a defect in the stripes, and a finite left half needs the defects to cancel every stripe beyond its
edge.

**A repeat is a white run.** The proof gives more than the inequality. If a block of length $n$ recurs at time
$a'$, the row at time $a'$ copies the row at time $a$ on the $n - 1$ cells left of the columns. The earlier row is
white beyond its edge, $L + a$ cells out. So the later row is white from cell $L + a + 1$ to cell $n - 1$: a run of
$n - 1 - L - a$ white cells, in a row whose own edge is further out. In the forced left half that reads: if the
visible bits of column 1 agree for $n$ steps from the times $2i$ and $2j > 2i$, the row at time $2j$ has a zero run
of length $2n - L - 2i$ starting at depth $L + 2i + 1$. Zero runs are what the records of §8.36 and the ladder of
§8.56 bound. So a bound $R(d) \le \rho\,d + C$ on zero runs from depth $d$ would give
$2n \le (1 + \rho)(L + 2i) + C$ for every later time $2j$: a block that starts early enough never recurs at all.
With the doubling conjecture ($\rho = 1$) the first $L + 3$ visible bits of column 1 never recur. This is
conditional, and the computed zero-run bounds (the ladder's $R(24, S)$ to depth 249, §8.56; the free records $R(d)$
to depth 89, §8.37) lie below the depths $L + 2i + 1 \ge 250$ where a counterexample would need it. It is recorded
because it ties three things together exactly: a repeat in the trace, a white run in a later row, and the cost of
that run. *(comb note, 2026-10-14, Local, SW-01: $R(d)$ and the ladder's $R(m, S)$ separated; the conclusion
unchanged.)*

**What it does not give.** Theorem A′ is sharper than Theorem A and not stronger in its reach. Real right halves
have no long early repeats, so it does not bind them. The squeeze sentence above is a restatement, as §8.33 was.
Its use is the comparison: it says exactly which number a proof must move, and from where to where.


### 8.59 The window principle meets the band of stripes: a repeat is a white run, and the left side is never white for long (2026-10-05)

Question 7 of PERIOD-TWO.md asked which columns 1 of zero entropy are excluded. Theorem E (§8.57) excluded the
Sturmian ones, by their long early repetitions. §8.57 also said where that method has no grip: a sequence with
no repetition longer than two periods, Thue–Morse for one, passes the condition $(\ast)$ untouched. This section
takes the other half of the picture, the left end of the rows, and gets a grip on part of that class. Everything
here is elementary, and `rule30_band.py` checked each statement with predictions written first. Two of its blind
predictions and one counterfactual missed; they are recorded below.

**The idea in one line.** §8.58 showed that a repeat of the trace is a white run in the later row. The later row's
left end is the band of stripes (§8.27, §8.30): eventually periodic diagonals with tiny periods. A band like that
is never white for long. So a repeat must stay below Theorem A′'s bound by the black in the band, and the band's
black is a universal, computable object.

**Notation.** Diagonal $k$ of a row is the cell $k$ places right of the row's leftmost black cell, and $D_k(t)$ is
its colour at time $t$. From Rule 30, $D_k(t+1) = D_{k-2}(t) \oplus (D_{k-1}(t) \lor D_k(t))$, with $D_{-1} = D_{-2} = 0$.
So diagonal $k$ depends only on diagonals nearer the edge, and by induction each is eventually periodic in time,
with a period that is a power of two (§8.27). "Eventually white" and "eventually black" mean constant from some
time on. In the wall form (§8.39) the same holds: diagonal $k$ exists from time $k - L$, when it is at the wall,
and obeys the recurrence from then on.

**Lemma B1 (white, then black).** If diagonal $j$ is eventually white, diagonal $j + 2$ is eventually black. No two
adjacent diagonals are both eventually white. A diagonal other than 0 and 1 is eventually black only if the one two
before it is eventually white.

*Proof.* Once $D_j \equiv 0$, $D_{j+2}(t+1) = D_{j+1}(t) \lor D_{j+2}(t)$, which never falls, so $D_{j+2}$ is eventually
constant, and it is 1 unless $D_{j+1} \equiv D_{j+2} \equiv 0$ as well. If $D_j \equiv D_{j+1} \equiv 0$ then
$D_{j+1}(t+1) = D_{j-1}(t) \oplus (D_j \lor D_{j+1}) = D_{j-1}(t)$ forces $D_{j-1} \equiv 0$, and so on down to
$D_0 \equiv 0$, which is false ($D_0 \equiv 1$). That proves the first two claims. For the third: if $D_k \equiv 1$
then $D_k(t+1) = D_{k-2}(t) \oplus 1$ forces $D_{k-2} \equiv 0$. $\square$

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

Rowland (2006, §5) proves when the periods double, and §8.31 found the first branch point of the left side, which
is an eventually white diagonal too. Whether the unboundedness itself is in the literature was not checked (owed:
Jen 1986, Rowland 2006). Measured: below diagonal 53,200 the eventually white diagonals are exactly 2, 7, 28 and
399, the eventually black ones exactly 0, 1, 4, 9, 30 and 401, the period 16 (BF0, with a certificate $V_t = V_{t+16}$
for the strip of 53,200 diagonals; one cycle, reached by the single cell and by random seeds). Over all 512 contents
of the first 10 diagonals, diagonal 4 is black from time 4 and diagonal 9 from time 11 (BD3).

*Literature, 2026-10-09 (Local, L471).* Lemma B2 is in print for the single seed. Nersissian, "Diagonal Periods and
Newton Supports of Rules 30, 86 and 135", arXiv:2609.25077 (submitted 2026-09-18, before §8.59), Theorem 13,
proves that the least eventual periods of Rule 86's natural diagonals are unbounded. Rule 86 is Rule 30 reflected
(its Proposition 3), and those diagonals are our left-half diagonals. The proof is the same as B2's: a pigeonhole on
adjacent periodic profile pairs, read backward into the zero boundary. It adds a bound, m + 2 <= 4^(Q_m), where Q_m
is the running largest period through depth m. Its Corollary 3 is Rowland's doubling criterion (his Proposition 2).
B2 as stated here applies to every left-finite row; the proof uses only V_(-1) = V_(-2) = 0 and V_0 = 1. That is an
immediate extension of the same argument, not a new method; the credit for the method is Nersissian's. Rowland §5
has the doubling criterion but not unboundedness (GPT's reading, 2026-10-06). Jen 1986 is still owed (paywalled).
Read through a fetched summary of the arXiv HTML, with the statement excerpts checked; not a full proof audit.

**Theorem A‴ (the window principle, with the band).** Let the leftmost black cell at time 0 be $L$ cells left of
column $i$, and let the pair of columns $(i, i+1)$ show the same block of $n$ values from the times $a$ and $a' > a$.
Then row $a'$ is white on its diagonals $L + a' - n + 1$ to $a' - a - 1$. Hence, if diagonal $b$ is black at time $a'$
and $b < a' - a$, then $n \le L + a' - b$.

*Proof.* By §8.58 the rows at $a$ and $a'$ agree on the $n - 1$ cells left of column $i$. Row $a$ is white beyond
distance $L + a$, so row $a'$ is white at the distances $L + a + 1$ to $n - 1$. Its leftmost black cell is at distance
$L + a'$, so those distances are its diagonals $L + a' - n + 1$ to $a' - a - 1$. A black diagonal $b$ in that range
contradicts this; so either $b \ge a' - a$ or $b \le L + a' - n$. $\square$

With $b = 0$ this is Theorem A′. With $b = 1, 4, 9$ (universal from times 1, 4, 11) it is checked on every seed of
width up to 9 (BD4, 0 violations), and the bound with $b = 9$ is sharp: 166 pairs attain $n = L + a' - 9$ (BD5).

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

What it reaches, with the slack $i' - \ell(i, i')$ measured over all pairs with $i' - i \ge 64$ and $i' \le 4096$
(BD8, all held): the period-doubling word (fixed by $0 \to 01$, $1 \to 00$) has slack 1 for ever, since its first
$2^k$ symbols recur at $2^k$ for exactly $2^k - 1$ symbols (BD7). Chacon's word (fixed by $0 \to 0010$, $1 \to 1$)
has slack 0: it begins with the squares $\sigma^k(0)\sigma^k(0)$ (BD7). So does every fixed point of a substitution
whose first two letters are equal, and so does the Fibonacci word (slack $-1595$ in the range measured; Theorem E
already covers it). For a Sturmian word with partial quotient $a_{n+1} \ge 2$, the first break of period $q_n$ at
$h$ and the next, at least $q_{n+1}$ later, give one repetition of slack at most 1 at each such scale, so Corollary F
gives that case of Theorem E in two lines; the case of eventually all $a_n = 1$ still needs §8.57's three scales.
Not reached: Thue–Morse, Rudin–Shapiro and paperfolding, whose slack grows with the period (32, 32 and 33 in the
range measured; for Thue–Morse the squares of period $d$ sit at positions $\ge d$, so the slack is at least $d/3$).
As column 1, the period-doubling word, Chacon's word and their complements give forced rows that look like coin
flips to depth 6000 (longest zero run 11 to 13, ones 0.497 to 0.510; BD9).

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

Measured on the universal strip (16 phases, 53,200 diagonals): the longest white run is 17 (BF1 held its bound,
32; its blind half, "between 5 and 16", missed by one).

**Theorem A⁗ (a repeat's white run cannot lie in the settled band).** In the setting of Theorem A‴, if the diagonals
$0$ to $M$ are settled in the sense of Lemma B3 at time $a'$ and $M < a' - a$, then $n \le L + a' - M + 2P$.

*Proof.* The white run of Theorem A‴ covers $[L + a' - n + 1, a' - a - 1] \supseteq [L + a' - n + 1, M]$, which lies in
the settled band, so by Lemma B3 its length $M - (L + a' - n)$ is at most $2P$. $\square$

**The settling front.** When does diagonal $M$ settle? A diagonal in its regime settles the next one at the first
black cell it shows afterwards: $D_{k+1}(t+1) = \lnot D_{k-1}(t)$ when $D_k(t) = 1$, and from then on $D_{k+1}$ follows
its inputs. After an eventually white diagonal the next one settles at once. So
$\tau_{k+1} = 1 + \min\{t \ge \max(\tau_k, \tau_{k-1}) : D_k(t) = 1\}$ (or $\max(\tau_k, \tau_{k-1})$ after a white
diagonal) is an upper bound on the settling time of diagonal $k+1$, for every row with a white left tail, whatever
its seed and whatever its phase, once the regime values $D_k(t)$ are taken from the universal cycle at the worst
of its 16 phases. Measured (BF2): the worst-phase front reaches diagonal 53,199 at time 107,294, a slope of 2.017
(1.992 at diagonal 1,000; I had predicted 1.5 to 2.0). The actual rows settle faster: the median row is in its
regime to diagonal $0.78\,t$ at $t = 1600$ (the 0.25 cells per step of §8.30), but at $t = 200$ single rows ranged
from $0.76\,t$ to $1.01\,t$, which is why the counterfactual CF2 ("no row agrees with the cycle below $2S(t)$")
failed in 2 of 120 cases: it assumed the average rate for every row. BF3 held: every row agrees with a phase of the
cycle on every diagonal below the front's $S(t)$ ($S(200) = 97$, $S(1600) = 804$).

**What Theorem A⁗ reaches** (BF4). A pair $i < i'$ of column 1 with common future $\ell$ excludes every left edge
$L$ for which $L + 2i' - 2\ell + 32 \le \min(2(i'-i) - 1,\, 53199)$ and $\tau_{L + 2i' - 2\ell + 32} \le 2i' - 16$.
The front's slope is just above 2, so a repetition is fatal, at depths the certified strip covers, when
$\ell > i'/2 + L/2 + O(1)$, roughly: when the future at $i'$ repeats more than half of the time before it.
- Period-doubling (the control): excluded to $L = 53{,}165$, the strip's cap; Corollary F excludes every $L$.
- **Thue–Morse: excluded for every $L \le 15{,}870$**, by the pair $i = 0$, $i' = 49{,}152$, $\ell = 32{,}768$ (the
  prefix of length $2^{k+1}$ recurs at $3 \cdot 2^k$).
- **Paperfolding: excluded for every $L \le 15{,}868$**, by $i = 16{,}384$, $i' = 49{,}152$, $\ell = 32{,}767$ (the
  block starting at $2^{k-1}$ has period $2^k$ for $2^k - 1$ symbols).
- Rudin–Shapiro: nothing. Its best repeats have $\ell$ near $i'/2$, which the slope 2.017 just fails to reach.
The records (§8.36) exclude every column 1 for $L \le 84$ ($R(85)$ is finite); this is the same kind of
statement, about 190 times deeper, for two named sequences.

**What it reduces to.** For Thue–Morse and every $L$, the argument needs, at infinitely many scales $k$, that
diagonal $L + 2^{k+1} + 33$ has settled by time $6 \cdot 2^k - 16$: that the front's slope stays below 3 and the
band's period stays small against its depth. Those are statements about one object, the universal left side of
Rule 30 (§8.31), not about seeds. Below diagonal 53,200 the slope is 2.017 and the period 16. Beyond 160,000
diagonals nothing has been computed, and Lemma B2 says the period keeps doubling, each doubling at an eventually
white diagonal whose position no one can predict. So the Thue–Morse case of question 7 is now: *prove that the
left side of Rule 30 settles at a bounded rate*. That is a cleaner question than the one it replaces, and still
open.

**What this does not do.** Nothing for real right halves: their repeats are short and late, far below Theorem A′,
let alone A⁗. Nothing for the counting form. The left half's edge is where Rule 30 is most orderly, and the prize
lives in the chaotic core, so a method that lives on the edge was always going to reach only the columns 1 that
echo their own beginnings.


**Audit note (2026-10-06, after GPT's independent reading, RULE30-GPT.md §G2).** No counterexample to any statement
of this section or of §8.54, §8.57 and §8.58. Three qualifications are adopted here. (i) Corollary F's substitution
example needs the substitution to grow on its first letter, $|\sigma^k(a)| \to \infty$; the identity fixes every
word and gives nothing. (ii) In the wall form a diagonal $k$ exists only from time $k - L$, so the settling
recursion for the forced half-line starts at $\max(\tau_{k-1}, \tau_{k-2}, k - L)$; with $L = 1$ the worst-phase
bounds move by one step (107,295 and 107,313 at diagonals 53,199 and 53,207), which changes no number used above.
(iii) Any extension of the Thue–Morse exclusion to every $L$ needs the settling slope below 3 *and* the period
$o(M)$ on every left side a finite seed can realise, not only on the generic one; GPT's §G2.4 states the sufficient
criterion exactly. GPT also supplied the finite-offset sentence that Theorem E's Step 4 had left implicit (§G2.2):
for the eventually-all-1 case the offset $m = -q_n - r$ with $1 \le r \le 2C + 6$ is impossible for large $n$ because
$\|r\alpha\|$ is bounded below by a fixed $\eta > 0$. That repair is accepted as part of the proof of Theorem E.

### 8.60 The small items: the wall never sees the far end, the mostly-zero words, and the left side to a million (2026-10-06)

The board in PERIOD-TWO.md §6 listed eight items found in this file that had never been leads. The owner asked for
them. Three took runs, each with predictions written first; two (why the forced cells inside a long run stay 0,
§8.2; whether a structural reason for balance reaches the core, §8.34) went to GPT by the split agreed in the
messages table of CLOUD-LOCAL.md on 2026-10-06 at 00:17. The runs are `rule30_sync.py` (five runs),
`rule30_records_word.py` with the engine `records_word.c`, and `rule30_leftside_million.py`.

**1. Are the walls synchronised in time across right halves? (§8.10's untested hint.)** They are, and the reason
is not a clock. The first run measured the Fano factor of the number of halves slipping at each window, over the
3,936 unlocked right halves of up to 12 cells: 5.8 in the formation (windows 2 to 11), 2.7 in the middle, 3.1 late
(windows 40 to 72), where independent halves give 0.5, 0.86 and 0.92 (the value $1 - \sum p_h^2 / \sum p_h$, which
the shifted control reproduces; my counterfactual's band had assumed rare slips and missed it). I predicted the
synchrony would fade; it did not (S2 refuted). Four more pre-registered runs found why:
- The excess does not grow with the population (SA1 refuted: 2.05 at 15,744 halves against 2.42 at 3,936), so it
  is not a modulation shared by all halves but clusters.
- Grouping the halves by their six cells nearest the wall, the 64 groups' slip counts are uncorrelated (0.009);
  within groups the excess is 1.24 (SB3 held). No common clock. The alternative that would have survived a
  refutation, the wall's parity clock (every wheel's phase is even, and the phases favour 4, 6 and 8), is out.
- **The synchrony is duplication.** Among the 3,936 unlocked halves there are only 1,968 distinct columns 1 (983
  traces come from one half, 495 from two, 241 from three, up to one from twelve; SC1 missed by 32). Keeping one
  half per trace, the late Fano factor is 0.75 against an independence value of 0.73 (SC2 held).
- **Where the duplicates come from: the wall often never sees the far end of its right half.** A half $R$ and its
  sister $R + 2^{12}$ (one more black cell at position 13) have the *same* column 1 for all 4,096 steps in 1,479
  of 3,936 cases (37.6%). The rest first differ at a median of 34 steps (quartiles 26 and 50; SB1's second half
  refuted). Sisters that differ at all are uncorrelated afterwards (0.001; SB2 refuted). In all 1,479 identical
  pairs the two space-time patterns still differ at time 4,096, but only within 60 cells of the right edge (SC3
  held, 1,479 of 1,479), and 200 of 200 stay identical to 16,384 steps (SC4 held).

The mechanism, stated as an observation: a change in Rule 30 always travels right at speed 1, because the next
value is the XOR of the left neighbour, so a change at the far end rides with the right edge for ever. It reaches
the wall only if its left front escapes into the chaotic core, and the escape is decided in the first few dozen
steps: either within about 50 steps or never. The decision is made at the far end: grouping all 4,096 halves by
their outermost six cells, the share of identical sisters is 0 or 1 in 56 of the 64 groups (exploratory, no
predictions written). Not proved: that a change confined to the right edge's band (the thin strip of §8.30) can
never re-enter the core. Not explained: the 37.6%. Both are in the messages to GPT. For
the prize this is a fact about the instrument, not the problem: the counterexample searches over right halves
(§8.21) have been testing fewer distinct columns 1 than halves, about half as many at width 12.

**2. LR for the words that leave column 1 almost free (§7's "mostly zeros").** `records_word.c` computes the exact
record $R_w(d)$ for any periodic wall word $w$, by the anti-diagonal recurrence of §8.36 generalised: a free bit
branches below depth $d$ and is forced above it. Its controls: $R(d)$ for the 0101 wall equals the record file at
every depth 1 to 61 (W0); the word 0 reaches the cap from every depth, the word 1 gives the universal fibre
(0 from even depths, 1 from odd; my control W1 had said "1 at every depth", a wrong statement of the fibre, and
failed on that wording). W2, a cross-check against `rule30_rigidity.py`'s 14-free-bit maxima, gave per rotation 54, 52, 58, 56 for 0001 and 45, 66, 64, 48, 53 for 00001, against the recorded ranges "54 to 58" and "45 to 66": one rotation, 0010, lies 2 below the prose's range. Rerun here, `rule30_rigidity.py` itself (14 free bits, four jobs) gives exactly 54, 52, 58, 56, so the two implementations agree and the prose's lower end was imprecise.

| $d$ | 8 | 12 | 16 | 20 | 24 | 28 | 32 | 36 | 40 | 44 |
|---|---|---|---|---|---|---|---|---|---|---|
| $R_{0001}(d)$ | 24 | 28 | 32 | 52 | 52 | 80 | 76 | 84 | 96 | 100 |

| $d$ | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 |
|---|---|---|---|---|---|---|---|---|
| $R_{00001}(d)$ | 35 | 45 | 50 | 85 | 85 | 105 | 115 | 130 |

No run reaches the cap at any depth (W3 held: LR holds to 36 free bits for these words). The growth is linear and not faster (W4 held), and well below the coin's slope (W5 refuted): a least-squares line from depth 24 has slope 2.11 for 0001 against the coin's 3, and from depth 25 slope 2.40 for 00001 against the coin's 4; for 0101 the measured law is 0.83 against 1. The record takes a smaller share of the coin's run the freer the column is: 0.83, 0.70, 0.60. The histograms printed by the engine (`rule30_records_word.txt`) show the bulk to be very nearly a coin, and not exactly one: from depth 45 with 00001, of the $2^{36}$ prefixes 34,359,738,788 end at the first forced cell (run 0), 420 more than half; 17,175,829,450 at the next (run 5), 4,039,734 fewer than a quarter; and so on down to the 314 that reach 130. I first wrote "exactly, to the last digit" here and in the chat; GPT read the file and corrected it (CHAT-LEDGER.1.md C008, RULE30-GPT.md §G3.5), with its own control: for 0101 from depth 21 the first forced cell leaves 512 of 1,024 and the second 268 of the 512. A forced cell is not a balanced function of the earlier free bits, and conditioning on earlier survival does not preserve balance; left-permutivity gives no such theorem. The record is the tail of a nearly fair coin, and the tail is shorter than independent fair coins would give (the merging of §8.38), more so the more free bits there are. $R < 4d$ and $R < 5d$ held throughout (W6).

**3. Do branch points go on for ever? (§8.31.)** Lemma B2 (§8.59) says the eventually white diagonals never stop,
and each is a doubling or a branch; its proof also gives an explicit if weak bound: while the period is $P$, the
pairs of consecutive diagonals' regimes are all distinct, so the period must grow within $4^P$ diagonals.
`rule30_leftside_million.py` ran the single cell's strip of $10^6$ diagonals for $2.2 \times 10^6$ steps (253 s)
and certified it periodic with period 32. Its eventually white diagonals: 2, 7, 28, 399 (doublings, periods 1 to
16), 53,207 and 58,286 (branches), 87,866 (a doubling, 16 to 32), and **none between 87,867 and 1,000,000**. The
list to 160,000 was already in `rule30_leftsides.py`'s recorded outcome; §8.31's prose had not repeated the
doubling at 87,866, and my predictions M0 to M2, built on the prose, missed it (M0 failed on that, M1 and M2
refuted). The worst-phase settling front of §8.59 has slope 2.0057 at a million (M3 held). The counterfactual
("not yet periodic 1,000 steps before the end") was ill set: the strip settles at about 2.006 steps per diagonal
and had 190,000 steps to spare. What the run adds: the gaps between eventually white diagonals, 5, 21, 371,
52,808, 5,079, 29,580, and then more than 912,000, follow no pattern seen; whether the branches among them go on
for ever stays open, and the next white diagonal lies beyond a million.

**Addendum, the four left sides (GPT's ask in CHAT-LEDGER.1.md C004; `rule30_leftside_million.py sides`, predictions L0
to L4 written first).** The four left sides that §8.31 realised, each run to a million diagonals from a settled
strip with the split diagonal flipped (a settled strip is itself a finite row): all four certify with period 32 at
a million (L1 held), and their worst-phase settling slopes are 2.0057, 2.0023, 2.0052 and 2.0076 (L4 held, within
0.01). But they differ beyond their splits (L2 and L3 refuted): the generic side doubles at 87,866; the side
flipped at 53,208 branches again at 72,575 and 165,748 and doubles at 183,183; the side flipped at 58,287 doubles
at 229,337; the side flipped at 53,208 and 72,576 doubles at 291,256. So "the universal left side" is universal
only below the first split, as GPT's audit said to make explicit; beyond it each side has its own white
diagonals. What the four share is what an all-$L$ statement needs: a period that stays tiny ($32$ at $10^6$ on every
side) and a settling slope near 2. That is data for a conjecture with the right quantifiers, not a proof of one.

**What the three items give the prize.** Nothing directly, as expected of small items. Item 1 corrects the
instrument (distinct traces, not halves, are the population of a right-half search). Item 2 tests conjecture LR
where it is weakest and finds the coin's law again. Item 3 settles a number and sharpens a question.


**GPT audit note on §8.60 (2026-10-06).** The committed histograms are approximately geometric, not exact
halvings. For 00001 at depth 45, half of 68,719,476,736 is 34,359,738,368, whereas the first death count
is 34,359,738,788 (420 more). For 0101 at depth 21, a fresh independent control gives survivors 1,024,
512, 268 at consecutive forced tests, not 1,024, 512, 256. Left-permutivity supplies no exact conditional
halving theorem here. Also the finite agreement windows in the synchrony runs need an additional invariant
proof before “for ever” follows. See RULE30-GPT.md G3.4–G3.5 and CHAT C008; the original prose is preserved
for Local to correct. These qualifications do not change the computed record maxima.


### 8.61 Question 3 assessed: the certificate it asks for is question 1 in another costume (2026-10-06)

Question 3 of PERIOD-TWO.md asked for a machine-found certificate: encode the forced walk inside a zero run as a
string rewriting system and search, with SAT, for an arctic matrix interpretation or an automaton invariant with a
ranking function that proves every run ends, as Yolcu, Aaronson and Heule did for weakenings of Collatz. It had
never been started. Before building an encoding (a leap), the step: what would such a certificate have to be?

**What a certificate is here.** The forced walk from depth $d$ (§8.37) has as its state the last two anti-diagonals
of the left half, about $d + k$ bits after $k$ steps, and it ends when a forced cell shows a 1. A termination
certificate is a function $\Phi$ of the state, non-negative, that falls by at least a fixed amount at every forced
cell passed and never rises at a linear one. Then no walk from a state of potential $\Phi_0$ can pass more than
$\Phi_0 / \delta$ forced cells, and the run from depth $d$ is bounded by about $2\Phi_0 / \delta$.

**Two things pin $\Phi$ down.** First, walks of length $0.83\,d$ from every depth $d$ exist (§8.36, exact to depth 85),
so $\Phi$ at the start must be at least linear in $d$: any certificate scales with the seed, as the question itself
noted from Condrey's bound. Second, the state's description also grows linearly, and no bounded-size interpretation
(a fixed finite automaton, a fixed matrix dimension) can carry a potential that is linear in an unbounded string
*and* knows which forced cells will be 0: the walk's forced cells are the chaotic core's own values. So $\Phi$ would
have to be a statistic of the whole state that falls at each forced cell, which is a counting statement: the
number of continuations still able to keep the run alive falls by a constant factor per forced cell. That is the
bounded-debt form of question 1, $N(T + k) \le 2^{c - \alpha k} N(T)$, written as a potential $\Phi = \log_2 N$.
*(comb note, 2026-10-14, Local, SW-01: depth 85 is in §8.37's note, not §8.36; $R(89) = 75$ landed at 06:19 the same
day.)*

**So question 3 waits on question 1.** The only potentials anyone here has named are counting ones, and a counting
potential is question 1. That is a statement about the candidates in hand, not an impossibility: GPT's audit
(RULE30-GPT.md §G5, CHAT-LEDGER.1.md C012) rightly objects that a fixed matrix can carry a potential linear in an
unbounded string (the unary counter), that a ranking need not be a population-decay curve ($2^d$ countdown paths
of length $2d$ have a linear ranking and a flat survivor count), and that "walks of length $0.83\,d$ from every
depth" is measured to depth 89, not proved. The first version of this section claimed an equivalence and an
impossibility; both are withdrawn. What stands: SAT can search only a finite family of candidates, none has been
named, and what SAT does well here it has already done (the crib of §8.37, the ladder's exhaustive checks). Closed
as a route of its own until a family of potentials is named; its tools would then serve, and the naming is where
the work is.


**GPT audit note on §8.61 (2026-10-06).** A fixed 2-by-2 matrix with diagonal entries 1 and upper-right
entry 1 represents unary length: its n-th power has upper-right entry n. Fixed dimension therefore
does not prohibit a potential linear in an unbounded word. Further, 2^d labelled paths all terminating
after 2d countdown steps have a decreasing linear ranking but no uniform fractional survivor
contraction: the population stays constant until termination, including a window beyond step d.
Thus an individual ranking is not equivalent to the stated bounded-debt count law. These examples
are not Rule 30 certificates; the practical deferral until an actual candidate remains reasonable.
The general impossibility/equivalence argument needs qualification. See RULE30-GPT.md G5 and CHAT C012.


*Reopened and closed again, 2026-10-09 22:09 BST (Local, a drawn row; PERIOD-TWO.md Q3 row).* The named finite family:
strip-graph certificates of radius R (entry 38's method), which did produce exclusions for the walls 0 1^q, q = 7
and q >= 9. For period 2 (the word 01) the family is empty up to R = 9. Its cyclic component forcing neither
neighbour grows 84, 150, 264, 456 with the radius (RG, `rule30_rung3_strip.py`, L488), and the same holds for every
word of period 3 .. 6. This is consistent with the assessment above: the certificate would have to carry Q1's
potential, and a fixed-radius strip cannot.
*(comb note, 2026-10-14, Local, SW-01: the heading's "question 1 in another costume" and this note's "would have to
carry Q1's potential" are the withdrawn first reading (the equivalence withdrawn after GPT's audit, G5, C012), not
the standing one. What stands is the section's: the only potentials named are Q1's counting ones, and the route is
closed until a finite family of potentials is named; the family named since, strip graphs, is empty for 01 to R = 9.)*

### 8.62 The owner's question: what "period 1" means, whether period 2 had to follow, and the ladder by freedom (2026-10-06)

The owner asked, on the morning of 2026-10-06: the prize asks whether the centre column of Rule 30, from one black
cell, ever becomes periodic; Condrey proved that no nonzero finite configuration has an eventually constant centre
column, "period 1", and our work has been on "period 2" as his own next step. But what does period 1 even mean,
does period 2 necessarily follow, where else could one have started, and what would period 3 look like?

**What the words mean.** The centre column $c(t) = x_t(0)$ is *eventually periodic* if there are $T$ and $p \ge 1$ with
$c(t + p) = c(t)$ for every $t \ge T$. The prize's conjecture is that it is not; so the conjecture is the conjunction,
over every $p$, of "not eventually periodic with period $p$". "Period 1" is the case $p = 1$: the column eventually
constant, $000\ldots$ or $111\ldots$ from some time on. "Period 2" is the case of least period 2: $0101\ldots$ or
$1010\ldots$ from some time on. The cases are logically independent of one another, and there are infinitely many.

**Why a statement about all finite seeds from time 0 is the right shape.** The row of the single cell's pattern at
time $T$ is itself a finite configuration, of width $2T + 1$. So "the centre column is $p$-periodic from time $T$ on,
from the single cell" is the same as "the centre column is $p$-periodic from time 0, from that finite seed". A
theorem of the form *no nonzero finite configuration has a centre column $p$-periodic from time 0* therefore
settles period $p$ for the single cell, "eventually" included. That is the shape of Condrey's theorem (§5,
PRIOR-ART.md: no nonzero finite configuration has a centre column constant from time 0 for longer than $w + 2$
steps, sharp), and it is the shape of everything in this record: Conjecture B, the ladder, the records, the
exclusions. Period 1 was not a special case of the single cell's column; it was the first wall.

**Does period 2 follow?** Not logically. Nothing about period 1 implies anything about period 2, and settling
period 2 would settle nothing about period 3. The prize needs every period at once, so an enumeration by period
can never finish; what it can do is show the uniform argument somewhere. Period 2 was chosen as the smallest open
case and the simplest wall that is not constant. That choice is Condrey's, and it is natural, but it is not forced.

**The ladder that the record found is not the period but the freedom.** Fix the wall: column 0 equal to a word $w$
of period $p$ with $z$ white cells per period, from time 0. By Lemma 1 (§8.2), column 1 is visible to the left
half only at the white times, and by Lemma 4 the cells of the forced left half come in two kinds: a linear cell for
every white time (set at will by column 1's bit) and a forced cell for every black time (a condition). Write
$f = z / p$ for the wall's *freedom*. The coin model of §8.38 then says the record zero run grows like
$R_w(d) \approx \frac{f}{1 - f}\, d$, less a merging loss. On that scale:
- Condrey's wall $1^\infty$ has $f = 0$: no free bit, the universal fibre, $R = 1$. The proof lives here because
  the wall admits no choice at all.
- The one-hole walls $0\,1^{p-1}$ have $f = 1/p$: one free bit per $p$ steps, the least free walls there are, and
  the nearest to Condrey's. `rule30_rigidity.py` found them the most rigid of all words (§7, R5), and nobody has
  tried to carry Condrey's argument across to them.
- Our wall $0101$ has $f = 1/2$: the middle of the scale, with $R \approx 0.83\,d$.
- The words that are mostly white, $0^{p-1}1$, have $f \to 1$: §8.60 measured $R \approx 2.1\,d$ and $2.4\,d$ for 0001
  and 00001.
Period 3 is two walls on opposite sides of this scale, $011$ ($f = 1/3$) and $001$ ($f = 2/3$); every general
statement in this record (Jen's theorem; Theorems A, A′, B; E and E″; the band lemmas; the window principle)
holds for every period, and the records engine of §8.60 takes any word, but §8.8 found that no wall other than
$0101$ turns a wheel, so the specific structure of §8.4 to §8.11 does not carry. "Period 3" would be the same
missing statement (§5) with different numbers, twice.

**Where else one could have started.** Three places, by this reading.
1. *The Condrey end.* Extend his monotonicity (next to a constant wall, column 1 can only turn black once) to
   the one-hole walls, one free bit per period, and see what survives. This is the job given to GPT on the
   morning of 2026-10-06 (CHAT-LEDGER.1.md C018); the measurement that goes beside it is below.
2. *The single cell's own pattern.* The prize is about one configuration, which has structure no general finite
   seed has (the universal left side, §8.30 and §8.31; the nested right side; the core between). A proof that its
   centre column has unbounded zero runs, or unbounded factor complexity, would settle the prize without any
   wall. Nothing in this record reaches the core of the single cell's pattern, and the two bands are provably
   far from the centre, so this route has no foothold yet.
3. *The uniform count.* Question 1 of PERIOD-TWO.md, stated for every wall at once: the number of finite seeds of
   width $w$ whose centre keeps any period-$p$ word for $T$ steps falls like $2^{w - \alpha T}$. Only this shape
   wins the prize, whichever wall is studied first.

**The measurement at the Condrey end** (`rule30_records_word.py holes`, predictions H0 to H3 written first; the
engine `records_word.c` of §8.60 widened to 512 bits; results in `rule30_records_word.txt`). H0 and the counterfactual passed (0111's 14-free-bit maximum is 19, as rigidity recorded; the word 0 caps and the word 1 never exceeds 1). **H1 held: no run reaches the cap**, so LR holds for the six one-hole walls to 32 free bits, at depths up to 256.

| Word $w$ ($f = 1/p$) | depths | $R_w(d)$ | $R/d$ at the deepest | coin's $f/(1-f) = 1/(p-1)$ | share |
|---|---|---|---|---|---|
| 011 | 24, 48, 72, 96 | 9, 20, 27, 39 | 0.406 | 0.500 | 0.81 |
| 0111 | 32, 64, 96, 128 | 18, 19, 26, 43 | 0.336 | 0.333 | 1.01 |
| 01111 | 40, 80, 120, 160 | 8, 18, 24, 30 | 0.188 | 0.250 | 0.75 |
| 011111 | 48, 96, 144, 192 | 10, 18, 23, 32 | 0.167 | 0.200 | 0.83 |
| 0111111 | 56, 112, 168, 224 | 6, 14, 25, 31 | 0.138 | 0.167 | 0.83 |
| 01111111 | 64, 128, 192, 256 | 8, 16, 22, 31 | 0.121 | 0.143 | 0.85 |

H3 held ($R \le 1.5\,d/(p-1) + 10$ throughout). H2, the slope between the two deepest points within 70% to 130% of the coin's, was refuted: two-point slopes of small numbers are noise (0.60 to 1.59 of the coin's), and the
ratio $R/d$ at the deepest point is the better statistic. It says something the free side did not: **on the rigid side the record keeps about 0.8 of the coin's share** (0.75 to 1.01 across $p = 3$ to $8$; the one outlier, 0111 at depth 128, is a lucky walk reached by 16 of $2^{32}$ prefixes), the same share as the 0101 wall's 0.83, while on the free side it fell to 0.70 and 0.60 (§8.60). So the merging loss is a property of freedom above one half, and below it the coin model with one fixed factor describes every wall measured. The one-hole walls are not more rigid than the coin predicts; they are rigid because the coin gives them one free bit per $p$ steps. For GPT's job that is the number to match: a proof at the Condrey end would have to allow runs of about $0.8\,d/(p-1)$, and Condrey's own argument allows $w + 2$ with no free bit at all.

**An exploratory negative, the same morning (no predictions written; it died at once).** I had hoped the one-hole
walls were *perturbed Condrey*: next to the constant wall the left half is the alternating fibre, on which Rule 30 is
affine, so a hole might inject a single ray travelling left at speed 1 and flip one cell of the time-0 row, which
would bound the record by about $2d/(p-2)$ at once. Three facts for $p = 3, 4, 6, 8$ kill it: with every hole
zero the left half is not the fibre (the wall has white cells); a single hole flips 11 to 115 of 160 depths, its
whole leftward cone, chaotically; and the map from holes to the row is not linear (38% to 47% of cells disagree
with the XOR of single-hole effects). There are no rays. What survives of Condrey's monotonicity has to survive
chaos in the left half; the one strong constraint the holes leave is that column $-1$ is pinned at $p - 1$ of every
$p$ times (CHAT-LEDGER.1.md C021).

**The two Condrey ends (after GPT's reading of his proof, RULE30-GPT.md §G11, CHAT-LEDGER.1.md C020).** Condrey's
period-1 theorem has two mechanisms, one per constant wall. Next to the white wall $0^\infty$ the latch: when
$x_t(0) = 0$, $x_{t+1}(1) = x_t(1) \lor x_t(2) \ge x_t(1)$, so column 1 can only turn black, once. Next to the black wall
$1^\infty$ the fixed checkerboard, with no latch. So the freedom scale has a Condrey end at each end, and they are
different problems. At the black end, $0\,1^{p-1}$, the checkerboard survives one hole only as a prefix: GPT's
§G11 proves that at each white time $np$ the first $p-1$ left cells are $[h, h, 1-h, 1, 0, 1, 0, \ldots]$ with
$h = 1 - \sigma(np)$, which for $p \ge 5$ forces a black cell at depth $2\lfloor (p-1)/2 \rfloor$ and excludes any
smaller initial left support; the comparison cone reaching the next hole is where the argument stops, and the
left half past the hole is chaotic (above). At the white end, $0^{p-1}1$, LR is false for the limit wall (column 1
zero gives the zero configuration), so the statement must be B, with a real right half, as Condrey's own proof
needed; and the latch gives a one-line lemma there: *between two black times of the wall, column 1 is
non-decreasing; at a black time it may fall to $\lnot(x_t(1) \lor x_t(2))$.* So per period column 1 takes one of at
most $p + 1$ shapes, $0^a 1^b$ then one reset, and carries at most $\log_2(p+1)/p$ bits per step: 0.79 for $p = 2$,
0.40 for $p = 8$, against one condition per $p$ steps. The bound falls like $\log p / p$ and the conditions like
$1/p$, so the latch alone closes no white-end wall: §8.45's positive-entropy gap in miniature. Freedom orders the
slopes of the records, not their values: GPT notes the maximal run from depth 1 is 1 for 0101 and 2 for 0111.


### 8.63 If period 2 had never been proposed: the next steps after Condrey, and a reframing of the work (2026-10-06)

The owner, after §8.62: "Can you expand on what alternative next steps might be imagined, as if Condrey's period 2 had
not been proposed. This becomes a full workflow reframing of where we should give our attention, as the current
pathway and projection is built off a predicate that does not, necessarily, follow logically." This section is that
expansion. It is reasoning, with one measurement started beside it; nothing here is a theorem.

**1. What a next step has to be.** The prize is one orbit, and "eventually periodic" quantifies over every period $p$
and every starting time $T_0$. Because the row at time $T_0$ is a finite seed, the only statements that bear on the
prize are theorems over *all finite seeds* (or over all $T_0$ at once). A finite exclusion never helps: computing the
single cell's centre column to time $T$ excludes every $(p, T_0)$ with $T_0 + 3p < T$ for every $p$ at once, which
is more than any of this record's finite exclusions (the ladder's 248 cells, the records' 84) says about the prize.
*(comb note, 2026-10-14, Local, SW-01: 84 is the left-edge exclusion $L \le 84$ from $R(85)$; with $R(89) = 75$,
finite since 06:19 that morning, it is 88.)*
Those exclusions are evidence for conjectures LR and B and tests of mechanisms; they are not steps toward the prize.
So "the next step after Condrey" means: *the next family of walls over which a theorem can be proved*, chosen so
that the mechanism found there has a chance of being the uniform one.

**2. The two coordinates of a wall.** A periodic column 0 is a word $w$ of period $p$. Two numbers describe how it
treats the left half. Its *freedom* $f$, the share of white cells, is the share of steps at which column 1 is
visible to the left half (Lemma 1, §8.2) and hence the rate at which the right half can inject bits; §8.62 is the
ladder along $f$. Its *switch density* $s$, the number of colour changes per step, is the rate at which the wall
interrupts the two mechanisms of Condrey's proof: next to a white stretch, column 1 can only turn black (the latch),
and next to a black stretch of $r$ steps the forced left half is the checkerboard to depth $r - 1$ whatever column 1
is (Lemma 1 again: $x(-k, t) = (k+1) \bmod 2$ whenever $\tau(t), \ldots, \tau(t+k)$ are all black). Condrey's walls
have $s = 0$. The wall $0101$ has $s = 1$, the largest possible: it switches every step, so neither mechanism ever
has time to act, and a third one appears there and nowhere else, the wheel (§8.8). Measured by $s$, period 2 is not
the simplest non-constant wall; it is the one farthest from Condrey's.

**3. The alternatives, as a map.**
- *Along $f$ at small $s$: the one-hole walls* $0\,1^{p-1}$ (§8.62, GPT's §G11 to §G13). Freedom $1/p$, switch density
  $2/p$. The checkerboard survives each hole as a prefix; past the hole the left half is chaotic; LR there is the
  statement, measured at $0.8\,d/(p-1)$.
- *Along $s$ at any $f$: the slow walls* $0^a 1^b$ with $a, b \to \infty$. One switch pair per period, and each
  mechanism gets its stretch. What the left half sees per period is explicit: during the black stretch nothing
  from the right (column 1 is invisible, the checkerboard forms by force to depth $b - 1$); during the white
  stretch, column $-1$ copies column 1 ($x(-1, t) = \sigma(t)$ while the next wall cell is white, and its complement
  at the last white step), and column 1 from a real right half is latched, $0^{a'} 1^{a - a'}$, one integer. (Two
  endpoints, after GPT's §G18: the checkerboard to depth $b - 1$ holds at the *start* of the black stretch, and at its
  last black time the first left cell is already 1.) So a real right half injects $O(\log a)$ bits per
  period into the left half, against about $a + b$ conditions, and the target for the left half is nearly
  deterministic: its own column $-1$, under its own autonomous evolution with the wall as boundary, must read
  $0^{b-1} 1$ through every black stretch and a monotone word through every white one. This is the cleanest form of
  the question anywhere on the map: a finite half-line seed, a periodic boundary, and a column that must be a fixed
  word on long stretches for ever. The one-hole walls are its $a = 1$ corner. In the other corner, $a \gg b$, the
  latch dominates and the statement must be B (LR is false for $0^\infty$).
- *Along $p$ at $s \approx 1$: the by-period ladder.* Period 2, then 3 (two walls, $011$ and $001$), then 4. Each is
  a new wall with the switches every step or two; the wheel of period 2 does not carry (§8.8), so each would need
  its own structure. This is the ladder the project has been on. Its justification was that 0101 is the smallest
  open case, which is true, and that the uniform argument must show itself somewhere, which is true of every
  family.
- *The single cell itself.* The prize's orbit has structure no general seed has (the universal left side, the nested
  right side, the core). A direct proof that its centre column has unbounded complexity or unbounded runs would
  need a handle on the core, and the two bands are provably far from it (§8.30). No foothold is known.
- *A condition that forces a neighbour column periodic* (question 2's move). Next to a white stretch the latch
  makes column 1 eventually constant; with $p \to \infty$ that is Condrey's white case through Jen's theorem. On
  slow walls the latch holds per stretch, which is why they are the family where this move has the most to work
  with.

**4. What the measurements say so far.** §8.42 measured the horizon of real seeds for every word up to period 4 and a
random word: total width plus 6 to 10 steps, the same law for all, which says that for *real* right halves the cost
per step is about one bit whatever the wall, because the right half pays for column 1 too (§8.51). §8.60 and §8.62
measured LR's records across $f$ and found the coin's law with a share between 0.6 and 1.0. Neither measured $s$ at
fixed $f$. `rule30_records_word.py slow` (predictions SW0 to SW3, written first) now takes the walls $0^a 1^a$, which
have 0101's freedom and switch densities $1/a$, for $a = 2, 4, 8, 16$: if the law stays $0.83\,d$ the checkerboard
stretches cost nothing and freedom is the whole story; if it falls, switch density is a second axis and the slow
walls are a genuinely different problem. **Measured** (8 threads, 7 minutes; SW0 and SW1 passed, no cap): $R/d$ at depth 48 is 0.812, 0.812, 0.667 and
0.792 for $a = 2, 4, 8, 16$, against 0.83 for 0101 and the coin's 1. SW2, which predicted a fall to below 0.60 at
$a = 16$, is **refuted**; SW3 held with room to spare (the longest run at $a = 16$ is 38). So no fall of the predicted
size was seen: in this run the checkerboard stretches did not cost the free column 1 what I expected. That is what
the data say and no more (GPT's qualification, CHAT-LEDGER.1.md C033, is right: four ratios at one depth do not fix
an asymptotic slope, and a switch-density effect stays unresolved; my first wording, "freedom is the whole story",
overstated it). What the slow walls change for certain is the B side: the budget of a *real* right half, which the
latch cuts to one integer per white stretch, and which GPT's §G15 makes exact for the width-one relaxation: a rate
of $\log_2(a+1)/(a+b)$ bits per step. The reframing below is adjusted accordingly.

**5. The reframing, as a workflow.** Three changes, offered for the owner's decision (DECISION OWED):
*(comb note, 2026-10-14, Local, SW-01: no longer owed. The owner's reset of 2026-10-06 09:20 gave the choice to the
two models; Local adopted the three changes in CHAT-LEDGER.1.md C049; the board marks the reframing DONE (CL005 and
the first triage, CL009 and GC155; PERIOD-TWO.md §6).)*
1. *Stop extending finite exclusions as a goal.* The ladder's next depth and the records' depth 93 would cost days
   and move no theorem; §1 above says why they cannot. They remain useful as instruments for testing a mechanism
   (the records engine took any wall in minutes this morning) and should be run for that purpose only.
2. *Give the slow walls the attention period 2 has had, on the B side.* The measurement above says LR is no easier
   there, so the target is B: a real right half, whose column 1 the latch cuts to one integer per white stretch,
   driving a finite left half that must answer every black stretch with the fixed word $0^{b-1}1$. The first
   theorem to try: with the right half's injection explicit ($O(\log a)$ bits per period against $a + b$
   conditions), prove the bounded-debt count of question 1 for this family, where the "debt" is paid by a single
   integer per period rather than by a chaotic column. GPT's exact finite mechanisms at the one-hole corner (§G11
   to §G13) are the right kind of object for the two switch events. GPT's §G18 and §G19 (2026-10-06, hours later) already
   supply the first pieces: for $b \ge 3a + 1$ the row at the first white time is the checkerboard on depths $4a$ to
   $a + b - 1$ whatever the inputs; on balanced walls the real-right latch excludes freely driven prefixes (a finite
   support exclusion, interior latch positions minimising); and the caution that certifying both switches does not
   make the per-period state finite, because the spatial tail is a state of its own that needs a closure or cost
   theorem. That tail is the precise missing item.
   *Measured the same morning (`rule30_uniform.py slow`, US0 to US3 written first):* next to $0^a 1^a$ for $a = 4, 8, 16$
   every right half of width up to 16 keeps its centre on the word for at most its total width plus 9, 7 and 6 steps
   (the empty right half next to $0^{16} 1^{16}$ alone reaches +15), and for $a = 8$ and $16$ the excess is negative from
   width 7 on. Three blind predictions missed on the empty right half and on a flag's semantics (the probe's outcome
   says how); the law of §8.42 stands on the slow walls, with smaller constants than 0101's. That is the B side's
   promise in numbers: the latch leaves a real right half little to say, and the left half pays for it.
3. *Keep period 2's record as the measured reference, not the route.* Its wheel is special, its channel bound is
   certified, its counting form is measured to width 26; a proof on the slow walls would be tested against it,
   not derived from it.
What does not change: the uniform count of question 1 is still the only shape that wins, whichever family it is
first proved on, and the method (predictions first, failures kept, two readers) is the same on every wall.

The owner's second question the same morning, what we would investigate if we were not chasing the money, is answered
in [CONSTELLATION.md](../../CONSTELLATION.md), which also carries this section's families as its Part A.


### 8.64 What makes 30 special among the 256: the left band of every rule (2026-10-06)

Row 14 of CONSTELLATION.md, taken as the cheapest question that bears on all the others: which of this record's facts
are Rule 30's and which belong to its class. `rule30_otherrules.py` (predictions OR0 to OR4 and CF written first; two
runs, 7 s and 3 s) runs the band instrument of §8.30, §8.31 and §8.59 on every elementary rule for which the instrument
is valid: the left edge of the single cell must move at light speed, $f(0,0,1) = 1$, and the white tail must stay white,
$f(0,0,0) = 0$. There are 64 such rules. (The first run used the 128 with $f(0,0,1) = 1$ alone; six of its nine
"nontrivial bands" were artefacts of a frame no configuration realises, among them Rule 135, Rule 30's colour-complement,
which showed Rule 30's band exactly. The scope error is in the probe's outcome; the second run is the result.)

**The result.** Of the 64 rules, from the single cell to 8,192 diagonals:
- **three** have a certified band with a small period: **Rule 30** (period 16; eventually white diagonals 2, 7, 28,
  399), **Rule 110** (period 32, doublings at diagonals 2, 3, 5, 7 and 45, no eventually white diagonal) and **Rule
  118** (period 4, no eventually white diagonal; nearly trivial);
- 47 are trivial (every diagonal of period 1 or 2);
- 14 do not certify within period 1,024: the additive and nested rules, 18, 22, 26, 82, 86, 90, 102, 126, 146, 150,
  154, 182, 210 and 218, whose diagonal periods grow too fast for the strip to repeat.

Three of the four blind predictions were refuted: I expected 5 to 30 rules with a nontrivial band (OR2: 3), Rule 30's
period to be the smallest among them (OR3: 118 has 4 and 110 has 32), and some other rule to share the white diagonals
2 and 7 (OR4: none). OR1 held: the mirror 86 and the linear rules do not certify.

**What it says.** The odometer at the left edge is rare: two rules in sixty-four have one worth the name, and they are
the two famous ones, 30 and 110. Rule 30 is the only rule whose band grows its period through eventually white
diagonals, which is Rowland's parity mechanism (§8.27, §8.31) and depends on Rule 30's OR and XOR; Rule 110's band
doubles by some other mechanism, five times in the first 45 diagonals and then not again below 8,192. So of the facts in
this record, the universal band's existence is shared with 110 and 118, its white-diagonal clock is Rule 30's own, and
the nested right side belongs to the additive-like rules that fail to certify here. The wheel, the channel and the
forced left half were not tested on other rules; they need the wall form, which is next (the instruments take any
rule's truth table). Recorded in CONSTELLATION.md, row 14.

**Addendum, the same morning.** The wall-form instruments (the forced left half, the records, the channel) need
left-permutivity, $f(0, c, r) \ne f(1, c, r)$ for every $(c, r)$. Among the 64 rules above exactly four are left-permutive:
30, 90, 150 and 210; 90 and 150 are linear. So Rule 210, $x' = l \oplus (\lnot c \land r)$, is the one sibling on which
the wall-form instruments can be tried as they stand (its OR becomes an AND-NOT in the anti-diagonal recurrence); its
single-cell band did not certify within period 1,024 at 8,192 diagonals. Rules 110 and 118, which share the odometer,
are not permutive in either direction, so they have no forced left half and the comparison stops at the band.

**The chaos item (GPT's seed, CHAT-LEDGER.1.md C045): the background is part of the object.** Colour-complement
conjugacy, $f'(n) = \lnot f(\lnot n)$, maps a rule on a white background with a black defect to its conjugate on a black
background with a white defect. Checked: the physical strip of Rule 135 (a white defect in black, the black tail kept
black) is the complement of Rule 30's strip at every one of 300 steps. The six artefacts of the first run have
conjugates 37, 25, 41, 9, 30 and 22: two of them (135 and 151) are Rule 30 and Rule 22 seen through the wrong
background, and four (91, 103, 107, 111) are conjugate to rules whose single cell does not even move at light speed,
so their "bands" were frames of nothing at all. The 128-rule census double-counted by conjugation; the 64 valid rules
are the whole census up to it. (Rule 30's own artefact frame, a black tail, turns white in one step because
$f(111) = 0$, which is why the artefact showed Rule 30's band two diagonals shifted.)


### 8.65 Rule 210, the one sibling: conjecture LR is false there (2026-10-06)

§8.64 found that among the 64 rules whose single cell has a light-speed edge and a quiescent white tail, exactly one
other rule is nonlinear and left-permutive: Rule 210, $x' = l \oplus (\lnot c \land r)$. Its inverse reads
$l = x' \oplus (\lnot c \land r)$, so the forced left half of §8.39 exists for it with the OR of Rule 30's inverse replaced by
an AND-NOT, and `records_word.c -DRULE210` runs the same search (predictions Z0 to Z3 and CF written first; the run took
seconds). The question was whether Rule 30's rigidity at period 2, conjecture LR with its records at $0.83\,d$, belongs to
the rule or to its class.

**It belongs to the rule.** Next to the wall 0101, Rule 210's forced cells never show a 1: from every depth tried (1, 8,
16, 24, 32) every prefix of column 1 continues to a zero run that reaches the search's cap, 509 cells (Z1, Z2), while the
control with Condrey's black wall gives $R = 0$ as it must (CF). An independent greedy computation by the column
recurrence confirmed zero runs of 112 cells from depth 8 for all 16 prefixes, and found an explicit column 1 whose
forced left half is **empty at time 0**: visible bits $1\,0\,1^2\,0^4\,1^8\,0^{16} \cdots$ (I first wrote "$1011\,0000\,1111\,1111$
then zeros", which is wrong: with zeros after the sixteenth bit a 1 appears at depth 65; GPT's §G26 caught it). The
left half-line is white and stays consistent with the wall for ever, and GPT's §G26 proves it: on the empty left half
the occupied cells satisfy $t + j$ odd, so no two neighbours are both black, the AND-NOT reduces to XOR, and the system
is Rule 90 driven by 0101; the visible bits are $\sigma(2n) = \lfloor \log_2 n \rfloor \bmod 2$, the parity of Rule 90's
Catalan return paths, which switches at the powers of two. So conjecture LR, that no column 1 at all gives a finite forced left half, is
false for Rule 210 at period 2, from the very first depth.

**What is not settled.** Conjecture B, that no finite configuration keeps the centre 0101, is open for Rule 210: a search
over every right half of width up to 20, the wall at its left end, found none that keeps 0101 for 300 steps (Z3; most die
within a few steps, as for Rule 30). So Rule 210 is a rule where the one-sided conjecture fails and the two-sided one
may still hold, which is the gap between LR and B made concrete on a rule where it can be studied cheaply.

**What it means for the record.** Rule 30's records ($R \approx 0.83\,d$), the exact halving of survivors at the forced
cells, Theorems A to E and the band lemmas were all derived for Rule 30's OR. The band exists on Rule 110 and 118 too
(§8.64); the rigidity of the forced left half does not survive the change of one gate. "Rule 30 is special" now has
two measured senses: the white-diagonal clock in its band, and LR. CONSTELLATION.md row 14 is updated.

**Addendum, the same hour: Jen does not rescue B for Rule 210, and the empty-left-half column is a doubling-runs
sequence.** The hope of CHAT-LEDGER.1.md C053 was that every zero-keeping column 1 of Rule 210 might be eventually
periodic, so that Jen's theorem would give B. `rule210_streams.py` (predictions ZS0 to ZS2 and CF written first) followed
every zero-keeping stream from depths 1, 8, 16 and 24, all 4,369 of them, for 4,000 depths: **none shows a period up
to 64 over its last 2,000 visible bits** (ZS1 and ZS2 refuted outright; a finite test, as GPT's C057 notes, but the
empty-left-half stream is proved aperiodic by §G26's formula, which already defeats the hope). So the zero-keeping choice is not a bounded-window function of the row, and B for
Rule 210 is a real open question, not a corollary. The stream that keeps the whole left half empty from depth 1 is,
$1\,0\,1^2\,0^4\,1^8\,0^{16} \cdots$, runs of lengths $1, 1, 2, 4, 8, \ldots$ (measured to 1024, then proved for all $n$ by
§G26: $\sigma(2n) = \lfloor \log_2 n \rfloor \bmod 2$), with no limiting frequency of ones (the run ends give subsequential
densities $1/3$ and $2/3$; my "0.34" was one window's count) and factor complexity
$p(n) = 10, 15, 20, 25, 31, 40, 63$ at $n = 4, 6, 8, 10, 12, 16, 24$: linear, so zero entropy. A chaotic-looking rule
whose empty left half is kept by a sequence of doubling runs is the kind of object CONSTELLATION.md is for; its proof
is GPT's §G26 (a linear subsystem, Rule 90, inside a nonlinear rule), and its right half (B) stays a search item.

**Second addendum: next to 0101, Rule 210's forced left half is always Rule 90's.** `rule210_streams.py parity`
(PS0 to PS2 and CF written first) asked which zero-keeping streams share the parity-sparse regime of §G26. All of them:
every one of the 4,368 streams from depths 8, 16 and 24 has no two horizontally adjacent black cells anywhere in a
300 by 300 window (PS1 refuted the other way). The reason is a two-line theorem that holds for *every* column 1.

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

**Consequences.** Everything in §8.65 follows at once: the forced left half is a linear function of column 1 over
GF(2), so "row zero beyond depth $d$" is a system of linear equations on the visible bits and the zero-keeping
streams form an affine space. Linearity alone does not make that space non-empty (an affine system can be
inconsistent; GPT's point in C061, taken): what does is GPT's finite-support construction (§G27.3), which inverts
the first $2n$ cells of any $n$-bit visible prefix and sets the deeper initial cells to zero. So every prefix
extends, conjecture LR fails, and the empty-left-half stream is the particular solution §G26 computed. Conjecture B for Rule 210 at period 2 becomes a
clean question: *does any finite right half of Rule 210, evolving against the wall 0101, produce visible bits that
satisfy that linear system?* The width-20 search says none does; the search can now be replaced by linear algebra over
the right half's own dynamics, which is nonlinear (the AND-NOT fires on the right, where the invariant does not hold).
For Rule 30 the same induction fails at the first step: its OR is 1 whenever either neighbour is black, so no parity
invariant forces linearity, and the forced left half is chaotic. That is the exact sense in which Rule 30's rigidity
is its OR.


### 8.66 The leftward light speed is the background's: $0.246 = 1 - 0.41 \times 1.84$; the checkerboard heals, the band locks (2026-10-06)

CONSTELLATION.md row 3, chosen by a random draw after the owner asked the two models to stop converging on the same
rows. Rule 30's rightward speed of influence is exactly 1; the leftward one was measured at 0.246 on a random
background (§8.30, LB5) and never derived. `rule30_damage_speed.py` (predictions DS0 to DS5, CF, then DL1 and DL2,
written and pushed before each run) measures it on structured backgrounds, with the two factors that make it.

**The identity.** In diagonal coordinates $k = x + t$ the rule reads $D_k(t+1) = D_{k-2}(t) \oplus (D_{k-1}(t) \lor D_k(t))$ on the whole plane, so a difference between two configurations never reaches a lower diagonal. Its lowest
damaged diagonal $k_{\min}(t)$ can only rise, and it rises exactly when the undamaged diagonal below it is black at
that step: then $D_{k_{\min}}(t+1) = D_{k_{\min}-2}(t) \oplus 1$ is the same in both copies. The leftmost damaged
cell is at $x = k_{\min} - t$, so

```math
v = 1 - P(\text{heal}) \cdot E[\text{jump} \mid \text{heal}],
```

an identity (it held within 0.009 on every background). I had written in the predictions that the jump is at most
2, because $D_{k+2}(t+1) = D_k(t) \oplus (\cdots)$ always carries damage two diagonals up; that is wrong where the
damage is dense, since the OR can then differ too and cancel the XOR, and the instrument check DS1 caught it: jumps
of 5, 7 and 10 occurred. The error is kept in the probe's header.

**Scope correction (GPT's independent reading R3, 2026-10-07; GC295).** The front identity presupposes a surviving nonempty damage set with a minimum. A finite nonempty initial perturbation guarantees both conditions at all finite times. Bounded-below infinite disagreement alone does not: R3 exhibits two rows that coalesce in one step. The barrier statement also needs the two copies to agree on all lower diagonals; incoming lower disagreement can cancel the difference above a common white diagonal. These conditions cover the recorded single-flip runs. The measurements have not been rerun by this reading.

**What the run found** (eight random trials and eleven structured backgrounds, $2^{13}$ steps each).
- *Random background:* $v = 0.2468$ (DS0 held; LB5's 0.246). $P(\text{heal}) = 0.410$, not $1/2$, and $E[\text{jump}]   = 1.84$, not $1.5$ (DS5 refuted both ways): the front sits preferentially above white cells because it heals at
  black ones, a selection effect, and the jumps are long for the cancellation reason above. So $0.246 = 1 - 0.410   \times 1.839$ to the run's accuracy, and neither factor is the background's density: the first is the density of
  the diagonal below the front *as the front sees it*. A derivation of 0.246 is a derivation of that conditional
  density, which is where the directed-percolation flavour of row 3 lives.
- *The checkerboard* (a fixed point of the rule): $v = -0.388$. The damage front moves RIGHT. Healing happens every
  other step (the diagonal below alternates) with mean jump 2.5, and $0.555 \times 2.5 > 1$: the chaotic region a
  flipped cell creates drifts rightward as a whole and the checkerboard closes behind it. A fixed point that heals
  its left side faster than light. (DS2 predicted $1/4$.)
- *The single cell's own band:* damage put on diagonal 64 at $t = 4096$ climbs for 429 steps and then LOCKS on
  diagonal 400 for ever ($v = 1$ exactly). The mechanism is the band's eventually white diagonals (§8.31): once
  $D_{399}$ is white, $D_{400}(t+1) = D_{398}(t) \oplus D_{400}(t)$ and a difference on 400 is permanent. DL1 held
  for 64 → 400 and 10 → 29, failed for 3 (which is already above the white diagonal 2 and never moves; my
  misapplication) and for 20, which passed 29 and 399 and climbed to 6,259 at $v = 0.2453$: the lock is not
  certain, because $k_{\min}$ jumps, and if diagonal $w + 1$ happens to be undamaged when the front passes $w$ the
  damage goes on. So the eventually white diagonals are *partial barriers* for information moving outward through
  the band, and this is a new role for the doubling positions 2, 7, 28, 399, 87,866. Above 399 the band carries
  damage at the random background's speed (DL2 held: a flip on 500 climbs at 0.2510), so the band's period-16
  diagonals are, as the front sees them, as black as random ones. (DS3 predicted the random speed for the band;
  refuted by the lock, then held above it.)
- *Periodic backgrounds* tiled from one cycle state of each ring $n = 3..10$: speeds from $-0.388$ to $1$ (DS4's
  "spread above 0.05" held by a factor 28; its "densest is slowest" refuted: the densest, ring 10 at 0.700, is among
  the fastest at $2/3$). Where the heal is periodic and the jump exactly 2 the speed is an exact rational: ring 4
  (1000) $1/2$, ring 5 (11001) $1/3$, ring 10 (0011111011) $2/3$; ring 7 gives $0.2222$ and ring 9 $0.2632$; ring 8
  (11000001) gives $v = 1$ with $P(\text{heal}) = 0.0006$, a white diagonal running through it on which the damage
  locks as in the band.

**What it says.** The leftward speed of information is not a constant of the rule. It is $1 - (\text{heal rate})$,
and the heal rate is set by the black cells of the background's diagonals as the front meets them: zero on a white
diagonal (speed 1, the band's lock), every other step on the checkerboard (negative speed), 0.41 on a random
background and, as it turns out, on the band's periodic diagonals too (0.246). The rightward speed 1 and the
leftward 0.246 are therefore different kinds of number: the first is the rule's XOR, the second a statistic of the
orbit. Row 3's "is 0.246 algebraic" becomes "is the front's conditional density algebraic", which nobody should
expect. What is exact and new is the structural fact: the eventually white diagonals of the universal left side are
one-way barriers that information crossing the band outward can be caught on, with the catch probabilistic.

Reproduction: `python3 tests/probes/lexicon/rule30_damage_speed.py 13` (70 s) and `... 13 lock` (40 s). The
outcomes are in the probe's header; the predictions were pushed in `5cee204` and `bfa54ab` before each run.

**Addendum (the same day): each white diagonal is, as measured, a fair coin.** (GPT's caution in C071, taken: the one-half and the independence are exact measurements at three barriers, not a theorem; the heading says "measured" until one exists.) Two more runs of the probe (`lockprob`, `lockphase`;
predictions LP0 to LP3, LQ1 to LQ3 pushed first, most refuted). The catch is deterministic in the flip's diagonal and
$t \bmod 16$, and at every barrier exactly half of the phases that reach it are caught, independently of what
happened at the earlier barriers: at 8 two residues of four (the period above it is 4), at 29 four of eight, at 400
eight of sixteen for every one of eleven flip positions from 30 to 395. So a flip below 8 ends locked with
probability $1 - 1/8$, below 29 with $1 - 1/4$, below 400 with $1/2$, and the damage's density plays no part (LP2
refuted). Which phases catch depends on the flip's diagonal (at 400: flips 300 and 395 are caught on complementary
sets of phases), so the barrier is not a single bit of the clock (LQ3 refuted). Why exactly half is open; the hint
is the doubling itself: the diagonal above a white one is the running XOR of the one two below, so what reaches it
is a parity of the damage's history, and a parity of a long chaotic history is balanced over the phases. For the
owner's question about information in the band: a perturbation anywhere in the single cell's band changes the
phase of the strip above the next white diagonal with probability exactly one half, and the probabilities at
successive barriers multiply.

### 8.67 Rule 30 on rings to $n = 24$, complete: cycle counts, transients longer than cycles, and every cycle a glider on prime rings (2026-10-06)

CONSTELLATION.md row 10, by the random draw; literature first (PRIOR-ART.md: OEIS A334497 and A334496 tabulate the
maximum period and the single cell's period; nothing tabulates the number of cycles, the periodic states, the
transients or the gliding cycles). `ring_census.c` visits all $2^n$ states for $n \le 24$ and certifies every cycle
by a state and a length; `rule30_ring_census.py` carries the predictions (RC0 to RC4, CF, pushed in `71f704c`
before the run) and the table is `rule30_ring_census.txt`. Both OEIS sequences are reproduced to $n = 24$ (A334497's
b-file reaches 36). The four new columns, and what was wrong in my expectations:
- *Cycle counts* $c(n)$: 1, 3, 1, 4, 2, 3, 9, 5, 3, 6, 13, 12, 5, 18, 31, 9, 7, 18, 5, 27, 60, 24, 4, 49. Not divisor
  structure in the way I predicted (RC2 refuted at 7 and 11): prime rings have few cycles *unless* one length is
  repeated, in which case rotation supplies $p$ copies at once (seven 4-cycles at $n = 7$, eleven 17-cycles at 11).
- *Periodic states* $P(n)$: 431 at 12, then 1431, 2082, 1776, 10291, 13805, 4350, 4124, 33926, 16619, 15744, 43172,
  194991 at 24; a fitted $2^{0.553 n}$ (RC1 predicted 0.6 to 0.8) but the fit means little: the periodic set is a
  vanishing and erratic fraction of the ring.
- *Transients*: the longest preperiod is 9,568 at $n = 24$ (RC3 predicted below 200), and at $n = 21$ and $22$ it is
  LONGER than the longest cycle (4,308 against 2,793; 5,477 against 3,553). On a ring Rule 30 can wander longer than
  it cycles.
- *Gliding cycles* (rotation by one cell maps the cycle to itself, so the pattern travels): at every prime $n$ from 13
  to 23 every cycle is gliding. This is a pigeonhole, worth stating because it is exact: rotation permutes the cycles
  of each length and its orbits on a prime ring have size 1 or $p$; at $n = 13, 17, 19, 23$ every cycle length occurs
  once, so every cycle is rotation-invariant and rotation is a power of the time map on it. The 63-cycle of the
  7-ring is one (the 7-periodic tails of §5 are travelling patterns), and the one non-gliding class at 7 and 11 is
  the one repeated length. Which parts are proved, then: the glider statement is proved for the listed $n$ by the
  census plus the pigeonhole; the growth of the maximum period is not proved for any $n$ beyond the table.

What would change the picture: a cycle count that stayed smooth in $n$ would have said the ring's cycles do not
come from sub-rings; they do not, in the way I had assumed, and the count is dominated instead by whether rotation
classes are full. Reproduction: `python3 tests/probes/lexicon/rule30_ring_census.py 24` (40 s, 300 MB).

*(An addendum of the same day carries this census to n = 29; it was filed at the end of 8.69, as "Addendum to
§8.67". Pointer added 2026-10-22.)*

### 8.68 The triangle census of the single cell: the core's triangles are the uniform measure's to three decimals, $3 \cdot 2^{-(L+4)}$ per cell (2026-10-06)

CONSTELLATION.md row 13, the last cheap-run row nobody was on. `rule30_triangle_census.py` (predictions TC0 to TC4
and CF pushed in `ac4f5c4` before the run) counts the tops of white triangles (§8.18's shrink theorem makes every
triangle exact and fixes it by its top) in the single cell's light cone to $t = 10^5$, by width $L$ and position
$x/t$; the vectorised census was checked top by top against a set-based one over sixty rows.

**The core** ($|x/t| \le 0.3$, area $3.0 \times 10^9$ cells): the counts by width are $281{,}011{,}418$;
$140{,}641{,}871$; $70{,}333{,}586$; $35{,}178{,}509$; $17{,}580{,}624$; \ldots; $137{,}109$ at $L = 12$; \ldots; one
top of width 29. The ratios $N(L+1)/N(L)$ are $0.500, 0.500, 0.500, 0.499, 0.503, 0.500, 0.496, 0.495, 0.507, 0.485$
for $L = 3$ to $12$ (TC1 predicted $[0.4, 0.6]$). The exact law was derived after the run and then matched: the
uniform Bernoulli measure is invariant under Rule 30 (the rule is surjective, being left-permutive), and under it a
maximal white run $[i, j]$ of length $L$ has probability $2^{-(L+2)}$ (white inside, black at both ends) while the
run is a *continuation* with probability $2^{-(L+4)}$ (the $L + 2$ cells above white, and the two beyond them black
so that the run below is exactly $[i, j]$, since $100 \to 1$ and $001 \to 1$). So the density of tops of width $L$
is $2^{-(L+2)} - 2^{-(L+4)} = 3 \cdot 2^{-(L+4)}$ per cell. Against the core's area that predicts $281{,}250{,}000$;
$140{,}625{,}000$; $70{,}312{,}500$; $35{,}156{,}250$; $17{,}578{,}125$ for $L = 1$ to $5$: measured within $0.09\%$,
$0.01\%$, $0.03\%$, $0.06\%$, $0.02\%$; $549{,}316$ at $L = 10$ (measured $547{,}147$); $536$ at $L = 20$ ($505$);
$1.05$ at $L = 29$ (two tops of 28, one of 29; TC2 held). *At the level of triangle births, the core of the single
cell is the uniform measure to three decimals through twelve octaves.* This is Problem 2's kind of statement made on
a two-dimensional object, and the deviation at $L = 1$ ($-0.09\%$ on $2.8 \times 10^8$ counts, far outside Poisson
noise) is real and small; what it is, is not known.

**The right edge.** The widest triangles of the whole cone sit *on* the edge, $x/t = 1.000$, at the times $m \cdot 2^k$: width 40 at $t = 65{,}536$, 38 at $32{,}768$ and $98{,}304$, 36 at $16{,}384$, $49{,}152$, $81{,}920$, 35 at
$8{,}192$ and its odd multiples. They grow like $\log_2 t + 22$, so TC3's "more than twice the core's" was wrong:
the nested side's triangles are large by position, not by scale, and the core's widest ($29 = \log_2$ of $3 \cdot \text{area}/16$) keeps pace with them.

**The left band** ($x/t < -0.6$): tops of width 15 ($21{,}916$) and 16 ($5{,}882$) exist and none wider, against
TC4's "under 12"; the band's ratios are near $1/2$ to $L = 9$ and structured beyond ($0.61$ at 10, $0.88$ at 15).
A reading, not pre-registered: the band's widest white run is its period, 16.

Reproduction: `python3 tests/probes/lexicon/rule30_triangle_census.py 100000` (4 minutes). Literature (PRIOR-ART.md):
NKS note 6.1 has the ratio, "roughly like $2^{-n}$" for rules 126, 30, 150, 182 on random initial conditions, with
no constant and no derivation; the exact $3 \cdot 2^{-(L+4)}$ and the single-cell match were not found there (NKS
p. 871 still to be read; the 1984 paper is a scan not readable here).

**Addendum (the same day): the law is exact, the deficit is the orbit's.** The same census on a random row, counted
only inside the inner light cone where the field is exactly the uniform measure (predictions TR0 to TR2 and CF
pushed in `0a44d87` first), gives deviations of $-0.002\%, +0.003\%, -0.006\%, +0.000\%, -0.004\%, +0.004\%$ from
$3 \cdot 2^{-(L+4)} \cdot \text{area}$ for $L = 1$ to $6$ on $1.25 \times 10^{10}$ cells, Poisson-sized (TR1), and
$-0.002\%$ at $L = 1$ (TR2 held). So the derivation is exact, and the single cell's $-0.09\%$ deficit of width-1 tops
in its core is a property of that orbit. I first wrote "about fifteen standard deviations"; GPT objected (C080)
that tops on a deterministic space-time are dependent and a total count does not license Poisson errors, and the
calibration it asked for (ten time blocks, two halves; predictions TB0 to TB3 and CF pushed in `35ae8a9` first)
proved it right: the width-1 deviation by block is $-0.034\%, -0.220\%, +0.034\%, -0.314\%, +0.087\%, -0.189\%, -0.100\%, -0.074\%, +0.025\%, -0.136\%$, mixed signs with a scatter near $0.13\%$ against a Poisson $0.02\%$. The
sigma claim is withdrawn. What the blocks show instead is where the departure lives: the right half of the core
($0 \le x/t < 0.3$) matches the law at $-0.011\%$ with blocks within $\pm 0.06\%$ and a white density within
$0.003\%$ of one half, while the left half ($-0.3 \le x/t < 0$) carries $-0.161\%$ with blocks from $-0.64\%$ to
$+0.21\%$ and a white density wandering by up to $0.033\%$. So the single cell's core is the uniform measure to
about $0.01\%$ on the side facing the nested edge and only to a few tenths of a percent, block by block, on the
side facing the ordered band, whose influence evidently reaches past $x/t = -0.3$. That is the finding; the
$-0.09\%$ total was an average of it.

**Second addendum: the uniform core begins at the leftward light speed.** Two more pre-registered runs (`bins`, then
`fine`; TN0 to TN3, TF1 to TF3, pushed first) locate the departure. In bins of $x/t$ the width-1 deviation from
$3/32$ is $-1.48\%, -0.89\%, -0.38\%, -0.42\%$ for $x/t$ from $-0.6$ to $-0.2$ and then $\pm 0.05\%$ in every bin
from $-0.2$ to $+0.6$: a front, not a gradient (TN2 refuted). At resolution $0.02$ the last bin with a deviation
above $0.2\%$ is $[-0.26, -0.24)$, and the width-4 excess ($+0.95\%$ to $+1.19\%$ in $[-0.34, -0.26)$: fewer short
white runs, more long ones) ends at the same place (TF1, TF3 held; TF2 missed by one bin at the $0.1\%$ scatter).
So the single cell's pattern is the uniform measure's, at the level of triangle births, exactly from $x/t = -0.24 \pm 0.02$ rightward, and $0.246$ is Rule 30's leftward speed of information (§8.30, LB5; §8.66): *the uniform core
is the region that news of the seed has reached.* (I first wrote here that "between the band's settled edge near
$-0.5$ and $-0.25$ lies a zone that is neither band nor coin". That was wrong: I never measured the band's edge.
Measured afterwards, with predictions TE1, TE2 and CF pushed first (`edge` mode), the settled edge, below which every
diagonal already has its period 16, is at $x/t = -0.254$ at $t = 40{,}000$ and $-0.252$ at $t = 80{,}000$, on the
triangle front. So there are two regimes, not three: the triangle law fails on the settled band and holds exactly
off it, and the front is the band's inner edge, which §8.30 already showed moves at the leftward speed.) Bears on: nothing in PERIOD-TWO.md §7 directly; it is the sharpest statement in
this record of where the single cell's randomness lives, and it ties rows 3 and 13 of the constellation together.

### 8.69 The slow walls from the left: the left half's own conditions stop every seed of width 16 within one period (2026-10-06)

The slow walls' B question (§8.63 item 5.2) from the side nobody had enumerated. Next to a periodic column 0 the left
half evolves on its own with the wall as boundary; the right half reaches it only through two conditions on column
$-1$ that no right half can lift: at black times $x(-1, t) = \lnot\tau(t+1)$ (column 1 is invisible, Lemma 1), and
at white times the implied stream $\sigma(t) = \tau(t+1) \oplus x(-1, t)$ must be non-decreasing inside each white
stretch (the latch, PROOFS.md C.2). `leftside_horizon.c` takes every finite left seed of width $W$ (cell $-W$
black) and every phase of the wall and finds the first failure; $H_L(W)$, the best over seeds and phases, bounds
the lifetime of every two-sided configuration whose left half has width $W$. Predictions LH0 to LH3 were pushed at
09:45 (`5cee204`) and the run waited until nobody else was on the slow walls (claimed in CLOUD-LOCAL.md).

- *Controls.* Black wall: $H_L(W) = W \pm 1$ (the checkerboard seed holds until its left end's defect arrives at
  speed 1). White wall: the empty seed lives for ever.
- *The wall 0101.* $H_L(W) = 1, 7, 6, 5, 6, 9, 10, 12, 17, 18, 17, 30, 29, 28, 32, 31, 30, 31, 33, 38, 37$ for
  $W = 0$ to $20$: width plus a constant of about 17 from $W = 11$ on (LH1's bracket of 12 was too tight; the shape
  held), against the two-sided law's "total width plus 6 to 10" (§8.42). So next to 0101 the left half's own
  conditions already give the law; the right half tightens the constant.
- *The slow walls $0^a 1^a$, $a = 2, 4, 8, 16$.* Over every seed of width $\le 16$ and every phase the best lifetime
  is $29, 22, 22, 21$ steps. Two consecutive complete black stretches span at least $3a$ steps from any phase
  ($24$ for $a = 8$, $48$ for $a = 16$), so **no finite left seed of width at most 16 survives two consecutive black
  stretches next to $0^8 1^8$ or $0^{16} 1^{16}$**, whatever phase it starts at; for $a = 16$ it does not even
  survive one period (21 < 32). For $a = 2$ and $4$ seeds of width 16 outlive several periods (29 and 22 steps
  against periods 4 and 8), so the width of the seed against the stretch is what matters, as §8.63 said. (LH2 held.)
  *Correction, 11:35 the same day:* this paragraph first said "for $a = 8$ and 16 that is less than one period",
  which is false for $a = 8$ (22 steps against a period of 16: the best seed passes one black and one white stretch
  and dies six steps into the second black stretch); my misreading, caught on rereading, corrected everywhere.
- *Record seeds do not nest* (LH3 refuted).

What it says for the reframing (§8.63): the slow walls are, from the left, a *harder* family than 0101 at the
widths measured, and the theorem to try there (column $-1$ cannot read $0^{b-1}1$ through two consecutive black
stretches for $b$ large against the seed) has its finite evidence at $b = 8, 16$ against seeds of width 16, and is
false for $b = 2, 4$ against the same seeds, which is the "large against the seed" clause doing its work. Bears on: PERIOD-TWO.md
§7 question 2 (B next to the slow walls). Single-party. Reproduction: `python3 tests/probes/lexicon/rule30_leftside_horizon.py 20 100`
(seconds).

**Addendum (11:28 the same day): wider seeds pass.** Widths 17 to 24 (`wide`; LW1 to LW3 and CF pushed in `13a7b23`
first; all three blind predictions refuted, the control held). Next to $0^8 1^8$: $H_L = 24, 25, 26, 29, 31, 30, 34, 36$ for $W = 17$ to $24$: a seed of width 20 passes two consecutive black stretches and one of width 24 lives two full
periods and four steps more. Next to $0^{16} 1^{16}$: $21, 24, 26, 26, 26, 29, 30, 32$: width 24 reaches exactly one
period and dies at the second black stretch. So "the wall sets the horizon" (LW3) was wrong; the seed's width
against the stretch is the whole hypothesis: $W = 2b$ fails and $W = 2.5\,b$ passes at $b = 8$, $W = 1.5\,b$ fails at
$b = 16$. The theorem to try is therefore: *next to $0^a 1^b$, no left seed of width $W < 2b$ (or thereabouts) can
hold condition (i) through two consecutive black stretches*; the checkerboard triangle of depth $b - 1$ must be
rebuilt across the white stretch from what the seed carries, and width about $2b$ is what it takes. Next to 0101
the law continues ($H_L(24) = 42$). Single-party.

**Second addendum (11:37): the hypothesis is the period, not $2b$.** GPT (G003) asked that the $2b$ threshold be kept
tentative across white-stretch lengths; the run `white` (LA1 to LA3 and CF pushed in `03aec91` first) fixes $b = 8$
and varies $a = 4, 8, 16, 32$: the least width whose best seed survives two consecutive complete black stretches is
$P = 13, 17, 23$ and none to width 24 (for $a = 32$, which needs 48 steps). So $P(a) \approx a + b + 1$: the passing
width is about the wall's **period**, and the earlier "$W < 2b$" was the special case $a = b$. GPT's caution was
right and the hypothesis of the theorem to try is now: *next to $0^a 1^b$, no left seed narrower than about the
period $a + b$ holds the forced $0^{b-1}1$ through two consecutive black stretches.* Below the passing width the
horizon barely depends on $a$ (the seed dies in the second black stretch at about the same depth whatever the
white stretch was). A fourth run with $b = 4$ and $16$ (LB1, CF registered) tests the period reading from the other
side. Single-party.

**Third addendum (11:38): the period, to within two cells, from both sides.** The run `period` (LB1 and CF pushed in
`04ada9b` first) with $b = 4$ and $16$: $P(4,4) = 6$, $P(8,4) = 10$, $P(4,16) = 20$, $P(8,16) \ge 25$. Against the
period $a + b$ over all eight walls measured today: $6/8$, $10/12$, $13/12$, $17/16$, $23/24$, $20/20$, $\ge 25/24$,
$\ge 25/32$. **The least width of a left seed that survives two consecutive black stretches next to $0^a 1^b$ is
the wall's period to within two cells**, for $4 \le a + b \le 24$. (LB1's two tightest brackets were off by one
cell; kept.) The theorem to try is now stated with its hypothesis measured: next to $0^a 1^b$ a left seed narrower
than $a + b - 2$ cannot hold the forced $0^{b-1}1$ through two consecutive black stretches. Why the period and not
the black stretch alone: the seed must carry, across the white stretch, both the checkerboard the next black
stretch forces and the monotone latch word the white stretch demands, and the sum of their lengths is the period.
That sentence is a reading, offered to GPT as the reasoning item; single-party.

**Addendum to §8.67 (the same day): rings to $n = 29$.** The census was extended to $n = 25$ to 29 (`deep` mode;
predictions RD0 to RD3 and CF pushed first; the OEIS b-files of A334497 and A334496 read before the run as controls,
both reproduced). The prime ring $n = 29$ has 14 cycles, of 14 distinct lengths (the longest 1,466,066), and all 14
are gliders, as the pigeonhole of PROOFS.md C.6 requires when the lengths are distinct: the pattern seen at 13, 17,
19 and 23 continues at 29. Cycle counts 16, 33, 40, 60, 14 for $n = 25$ to 29. My prediction that some ring in 25 to
28 would again have a transient longer than its longest cycle failed: 21 and 22 stay the only such rings found. The
first attempt at $n = 29$ thrashed this 16 GB machine and was stopped; the engine now needs 8 bytes per state.

### 8.70 Rule 30's velocity is Rule 210: time derivatives of the rule, and the prize as a difference equation (2026-10-06)

The owner, on a train: the link between the n-frame interpolation shaders and this work is time; temporal shaders
analyse change over time, and without time no state changes. "Do we consider not just the velocity of the state
change but its acceleration as well?" Over GF(2) the discrete time derivative of a cell is its XOR with its next
value, and the answer to the first half of his question is exact and short.

**Proposition (velocity).** For Rule 30, $x_{t+1}(i) \oplus x_t(i) = x_t(i-1) \oplus (\lnot x_t(i) \wedge x_t(i+1))$, which
is Rule 210's local rule. *Proof.* Rule 30 is $l \oplus (c \vee r) = l \oplus c \oplus r \oplus cr$; adding $c$ leaves
$l \oplus r \oplus cr = l \oplus (\lnot c \wedge r)$, Rule 210 (checked on all eight neighbourhoods). $\square$

So Rule 30 is "position plus a Rule 210 velocity": $x_{t+1} = x_t \oplus R_{210}(x_t)$. This is why Rule 210 kept appearing
as Rule 30's closest sibling (§8.64, §8.65, GPT's G26 to G28 and G58 to G66): it is Rule 30's time derivative. It also
says which neighbourhoods move a cell: only $\ast 01$ with left neighbour 0 and $\ast\ast\ast$ patterns where the left
neighbour differs from $\lnot c \wedge r$; a black cell with a black right neighbour never changes on account of its
right side.

**Acceleration, jerk, and the prize.** Higher derivatives are iterated differences, $\Delta = 1 + S$ with $S$ the time
shift, and over GF(2) $\Delta^{2^k} = 1 + S^{2^k}$ (the Frobenius identity GPT used in G59 and G66), so the $2^k$-th
derivative is the lag-$2^k$ difference. The centre column is eventually periodic with period $p$ exactly when
$(S^p - 1)x = ((1 + \Delta)^p - 1)x$ is eventually zero: when the column eventually satisfies a linear constant-coefficient
difference equation in its velocity, acceleration, jerk and higher derivatives. The prize's first question therefore
asks whether *any* finite-order linear difference equation eventually holds for the centre column. The least order
of such an equation for a prefix is its linear complexity (the Berlekamp–Massey profile), and an eventually periodic
column has bounded linear complexity. That makes the linear-complexity profile of the centre column the natural
measurement of the owner's question; it is registered as CONSTELLATION.md row 17 and as Local's next run, with
predictions written before it. Literature to check first: the linear complexity of Rule 30's centre column has
been studied in the cryptographic literature on Wolfram's generator (Meier and Staffelbach, 1991, and later work),
not yet read here.

**Addendum (2026-10-06 18:05 BST): the measurement.** Literature: linear complexity tests on Rule 30's centre column
are reported as passed (L near half the length) at cryptographic lengths; no published profile of the single-cell
column at millions of bits was found. `rule30_linear_complexity.py` (with a bit-packed Berlekamp–Massey engine,
`linear_complexity.c`; predictions LC1 to LC4 pushed before the run) measured the first $N = 2^{22} = 4{,}194{,}304$
bits. The linear complexity is $L_N = 2{,}097{,}152 = N/2$ exactly. So no linear difference equation over GF(2), of
any order below $N/2$ and with any coefficients, holds on these bits: if the centre column is eventually periodic,
its preperiod plus period is at least $2{,}097{,}152$. The whole profile is that of fair coins: about $N/4$ jumps
whose heights fit $2^{-k}$ (chi-square $p = 0.92$), the deepest dip $12.5$ below $n/2$. The column read backwards in
time gives the same (reversal is not an identity for linear complexity: $0001$ has $L = 4$, $1000$ has $L = 1$).
Velocity, acceleration and jerk have exactly the same complexity, as they must: if the first $N$ bits of $x$
satisfy a recurrence of order $L$ then $\Delta x$ satisfies the same one, and conversely $x$ satisfies $C(z)(1+z)$,
so $L(x) - j \le L(\Delta^j x) \le L(x)$ (proved in the probe's header, checked exactly). The 1,024 lag differences
and the 1,024 derivatives $\Delta^j$ show no bias (largest $|z| = 3.48$ among 2,048, mean $z^2 = 1.006$). So, to the
owner's question: in the GF(2) sense, the centre column's acceleration and jerk carry no more structure than its
velocity, and its velocity none beyond the column itself; every derivative is as complex as the column, which is as
complex as a coin. The counterfactual (Rule 30 on the ring of 22 cells, eventually periodic) saturates at $L = 4{,}480$
as it must. One control band failed narrowly (one of eight coin arms had a jump of 29 against a cap of 27; the
band was set per arm and not widened for eight). This is a finite fact, not a proof: it bounds the period from below
far less strongly than a direct search, but it covers every linear equation at once.

**Second addendum (2026-10-06 19:15 BST): moving frames.** The owner's compass (GPT's G083) separates change at a
fixed cell from change followed along a structure. `rule30_frames.py` reads the single-cell pattern along 41 frames
$x_t(\lfloor vt \rfloor)$, $v = k/20$, to $N = 2^{20}$ (predictions pushed before the run). Every interior frame,
from $v = -0.95$ to $0.95$, is linearly a coin ($L_N = N/2 \pm 2$, fair jump law, unbiased density), the left band
included; the only linear structure is a prefix of about $2/(1 - |v|)$ steps while a frame is within two cells of an
edge. The frame's own change is not always a coin. A step one cell to the right reads
$x_{t+1}(i+1) \oplus x_t(i) = x_t(i+1) \vee x_t(i+2)$, the OR term of Rule 30, which is 1 with probability $3/4$ when the
two cells are independent fair bits (GPT's G086: for independent Bernoulli($q$) cells it is $2q - q^2$, so this is a
property of the row's statistics, not of the rule alone); a step in place reads Rule 210 and a step to the left an XOR with a fresh cell, both $1/2$. So a frame
of speed $v \ge 0$ sees change with probability $1/2 + v/4$, measured to within $1.4$ at all 19 rightward speeds, in units that treat successive changes as
independent (they are not, so this is a yardstick, not a test; the single seed's pair law is not proved). In the frame moving right at the speed of light, Rule 30 is no longer a coin: that observer rides
the permutive channel, sees only the OR, and sees change three times in four. Two of the three blind predictions
failed (I did not compute this transport bias before predicting, and the left band is not linearly simpler).

**Third addendum (2026-10-09 12:35 BST): the light-speed frame's memory, heard first.** The owner heard the necklace
page's music box alternate, "staccato arpeggio staccato arpeggio repeat", and asked whether alternation of that form,
N times over, could reveal structure. The alternation is this section's light-speed law, and it has an exact form.
Rule 30 is left-permutive, so $k$ steps give $x_{t+k}(i) = x_t(i-k) \oplus g_k$ with $g_k$ independent of
$x_t(i-k)$. In a fair row (independent fair cells, which Rule 30 preserves on the line), every other cell of row
$t$ then has zero covariance with $x_{t+k}(i)$. So the correlation between a window's density in row $t$ and in row
$t+k$ is, up to an edge factor $\max(w-k, 0)/w$ for a window of $w$ cells (zero for $k \ge w$: the window loses the
diagonal's partner; G.GPT255, GC776),

```math
\rho_k = \mathbb{E}\,(-1)^{x_{t+k}(i) \oplus x_t(i-k)} ,
```

the correlation along the rightward light-speed diagonal. Exact enumeration (`rule30_cloud_alternation.py`, 6 s)
gives $\rho_1, \dots, \rho_{12}$ = -1/2, 1/4, -1/4, 5/32, -5/64, 77/1024, -141/2048, 39/512, -3273/65536,
2785/131072, -21759/1048576, 27905/2097152, with every other covariance term exactly 0. The sign alternates at every
lag computed, and the memory is long: $|\rho_8| = 0.076$, where independent flips with probability 3/4 would give
$2^{-8} = 0.004$. Counts of adjacent black pairs (the arpeggio's runs) alternate with the same signs to $k = 7$. So
dense and sparse rows take turns everywhere in Rule 30, not only in the necklace. On random fair rows a window of 63
cells flips between denser and sparser than half at 0.668 of steps, and eight flips in a row happen 6.3% of the time,
16 times as often as for uncorrelated rows. A search for N-fold alternation would therefore mostly find the rule
itself; structure would show only as a departure from these exact values. In the necklace the whole ring keeps 43
black cells at every beat (each step is a rotation), so its alternation lives in the comb's 14-cell window, which
reads the ring's six segments in turn (the unexpected check). Exploratory: no prediction was pushed, and the exact
part needs none. Not proved: that the sign alternates at every lag, that $\rho_k \to 0$, or that the single seed's
rows follow these values (they are not known to be fair rows; G086's scope). The single-seed measurement is offered
to a worker with its predictions first (CL078).
Correction (2026-10-09, Local's DB, L416 to L418). The exact values continue past $k = 12$, and the alternation
stops: $\rho_{17} = +416163/2^{31}$ is positive at an odd lag and $\rho_{18}$ is negative. Two independent kernels
agree, one of them stepping every 35-cell row by the plain rule. "The sign alternates at every lag computed" held
only to 16, so the all-lag sign question has a negative answer. Local's single-seed run (L415) found AL1 to AL3
held.


### 8.71 Turning rows: the all-S ring turns 14 cells a step, rows outrunning light are rings, and pattern speed is not signal speed (2026-10-09)

*Cloud, from the owner's questions of 2026-10-09: which surfaces can carry a ring's history, and "a unit vector in a
space-time picture is a velocity; the arrows carry information only if the data, not the layout, chooses where they
point". Probe `rule30_cloud_turning_rings.py` with `turning_rings.c`; predictions pushed in dedbe55 before the full
run. Chat CL071 and CL072; PROOFS.md entry 35.*

**The rotation (CL071; a finite certificate, found while exploring).** On GC686's ring `0x688eb74a45efb082671ee`
(site 0 at bit 0), one update is a rotation: $x_{t+1}(i) = x_t(i - 14)$. One update is 84 cell checks, and Rule 30
commutes with rotation, so this holds for every $t$; two programs agree over 1000 updates. Hence the period is
$84 / 14 = 6$, the least spatial period is 84, and on the line $x_t(i) = x_0(i - 14t)$: the clock is the initial row
read at every 14th cell, $x_t(0) = x_0(-14t)$. The 14 is a pattern speed, not a signal speed.

**Turning rows in general (Proposition 22, PROOFS.md entry 35, waiting room).** Call $x$ a turning row with vector
$(s, p)$ if $F^p x = \sigma^s x$. If $|s| > p$ the pattern outruns light; then $x$ is spatially periodic, and the rows
are exactly the periodic points of a map on words of $|s| + p$ cells. If $s < -p$ that map is a bijection, by
left-permutivity, so every word of $|s| + p$ cells extends to exactly one row moving left. Moving right, the map
loses information through the OR, and the rows are as rare as a random map's cycles. §8.67's gliding cycles on rings
up to 29 cells are the same objects seen ring by ring; this census takes every ring size at once, for bounded speeds.

**The census** ($p \le 3$, $|s| + p \le 28$; 1,399 rings, $1.611 \times 10^9$ rows counting rotations).
- Controls: every row satisfies its relation directly; census and brute force agree on every ring up to 20 cells;
  every left-moving run has all $2^{|s|+p}$ words periodic.
- Right-moving rows: at most 16 cycles in any run, the largest holding 55% of the periodic points on average (TC8,
  the unexpected check, held). The count exceeds the random-map heuristic $\sqrt{\pi 2^L / 2}$ about fourfold at
  $p = 1$ and matches it at $p = 3$. TC4 predicted agreement within a factor of $2^{2.5}$ at every size and was
  refuted at four sizes.
- **Walls.** Only one turning row in the whole census has an alternating column at all: GC686's ring, with six all-S
  walls 14 cells apart. No mixed S/L word and no all-L word appears (TC6 held). Every visible S/L wall is in marker
  form, which agrees with GC625 and GC626 (TC7 held). That the all-S turning row is unique also follows by
  composition with GC704, GC687, GC688 and L372 (PROOFS.md entry 35, corollary); the census confirms it on
  independent data.
- So the turning shortcut supplies no new S/L witness for portfolio question 4 in this range. GC686's ring is
  isolated even among turning rows, and why it turns is open (asked of GPT in CL071).

**Velocities chosen by the data.** Every background tested keeps the proved right edge: the rightmost difference is
at the flip $+\,t$ (DV1, 128 backgrounds). The left edge depends on the background.

| Background | Left speed of a single flip's damage |
|---|---|
| The white row | 1 (the single cell's pattern) |
| GC686's ring | 0.2969 at $T = 4096$ (84 flips, 0.2922 to 0.2986); 0.2976 at $T = 16384$ |
| 103 turning rows of 65 to 1024 cells | median 0.2765, 62% above 0.245 |
| Random rows, same instrument (post hoc) | 0.2450, standard error 0.0023 (§8.66: 0.246) |
| The checkerboard | $-0.3887$ (§8.66's $-0.388$, reproduced) |

Small rings give speeds near simple fractions: 1/3 at 5 cells, 2/5 at 12, 1/2 at 15, 3/5 at 14 and 17, 1/5 at 29.
Across all 127 turning rows of up to 1024 cells, the Spearman correlation of left speed with pattern speed is
$-0.001$ (DV4 held). A unit vector in space-time carries the row's information in two different ways. The vector
$(s, p)$ along which the row is constant is chosen by the pattern. The damage cone's edges, $+1$ and the
background's own leftward speed, are chosen by the rule acting on it. The two are unrelated.

### 8.72 Interlocking shapes: Rule 30 is eight jigsaw tiles, its periodic histories are single-brick walls, and next to the wall a periodic column 1 crystallises the left half (2026-10-09)

*Cloud, from the owner's question of 2026-10-09: "Interlocking shapes are some of the most interesting objects ...
especially ... the unusual single form shapes that interlock to infinity. I would like an exploration on the
applicability on rule 30." Probe `rule30_cloud_bricks.py` with `rule30_bricks.c`; predictions pushed in 7250395
before the run. Chat CL073.*

**1. Rule 30 is a set of tiles.** Give each neighbourhood $(l, c, r)$ one square tile with west edge $(l, c)$, east
edge $(c, r)$, south edge $c$ and north edge $f(l, c, r)$. Neighbours in a row must agree on the two cells they share,
and a tile's north edge must equal the centre of the tile above. So the tilings of the plane by these eight tiles
are exactly the bi-infinite Rule 30 histories, and the single cell's history is a tiling of the half-plane seeded by
one black tile. Edge colours can be cut as jigsaw tabs, so this is literally eight interlocking pieces. It is the
standard reading of a cellular automaton as a deterministic Wang tile set (Kari).

**2. The set is not aperiodic, and every periodic tiling is a wall of one brick.** A tiling periodic in two
directions is a Rule 30 history with a lattice of periods. One fundamental domain of the lattice, painted, is a single
brick, and its translates fill the plane. The white row, the checkerboard and every turning row of §8.71 are such
walls. GC686's ring has lattice $\langle (14, 1), (0, 6) \rangle$ in (space, time), so its whole infinite history is
one $14 \times 6$ brick of 43 black cells, laid in columns, each column of bricks one step lower than the last.

**3. How the single-shape tilings that interlock to infinity are proved non-periodic, and why that does not
transfer directly.** Two methods are known.
- *Hierarchy*: Robinson's tiles, Penrose's, and the hat and spectre monotiles (Smith, Myers, Kaplan and
  Goodman-Strauss, 2023). Every tiling is forced into nested supertiles of unbounded size, so a period would have to
  fit inside one supertile. The record's nearest relative is the left band: Rowland's local nested structure, and
  Lemma B1 to B3 and Theorem A‴ (§8.59), where unbounded diagonal periods keep a repeat out of the settled band.
- *Arithmetic*: Kari's 14 tiles and Culik's 13 (1996), and Jeandel and Rao's 11 (2015) as the minimum. Each row of
  tiles encodes a real number by its average, and each row multiplies it by 2 or by 2/3 (Kari), or by 3 or 1/2
  (Culik). A period would need $2^m 3^n = 1$. That is the Mahler and Collatz arithmetic which §8.45 and
  COLLATZ-PRIZE.md find in the prize.
Both methods prove that no tiling at all is periodic. Rule 30's tiles have periodic tilings (item 2), so neither can
apply to the tile set. They can enter only through the boundary condition, white far to the left, which is what a
finite seed supplies and what Jen's and Condrey's proofs use. In tiling language, Problem 1 is an aperiodicity
question for one seeded tiling, not for a tile set.

**4. Jen's case crystallises (the computation).** Let column 0 be the wall $0101\ldots$ and column 1 any word of
even length $P$, both $P$-periodic. Read sideways, Rule 30 sends the pair of columns $(c_i, c_{i+1})$ to
$(c_{i-1}, c_i)$, a map on $2^{2P}$ states. So from some depth $\mu$ on, the forced left half is periodic in space as
well as in time: a wall of one $P \times Q$ brick. Jen's theorem (Proposition 7) says the brick is never blank, and
Theorem B says no row of it has a white run longer than $2P - 2$. The census runs every word of every even length
up to 20, 1,398,100 words in all; its predictions were pushed first.
- **There are very few crystals.** At each $P$ at most seven bricks hold all $2^P$ words (BK4 held), and 20 bricks
  serve every length up to 20. A brick whose columns have period $p$ recurs at every multiple of $p$.

| Columns' period | Bricks: width $Q$; "every $q$" means bricks $q$ wide, each column of them lower than the last |
|---|---|
| 2 | the checkerboard: black and white columns alternating, constant in time |
| 4 | the 7-ring's 4-cycle (§5, G4.2): 7 wide, 13 black of 28 |
| 6 | GC686's all-S ring: 84 wide, every 14 by one step; it takes 48 of the 64 words at $P = 6$ |
| 10 | 155 wide, every 31 (the largest crystal again at $P = 20$, with 53% of all words); 90, every 18 |
| 12 | 138, every 46; 60, every 15; 100, every 25 |
| 14 | 728, every 104; 1316, every 94; 644, every 92 |
| 16 | 325, no stagger; 2032, every 127 |
| 18 | 1962, every 218; 8370, every 930; 4050, every 225; 342, every 19; 477, every 53 |
| 20 | 25000, every 1250; 400, every 40 |

- **The checkerboard takes exactly the words whose visible bits are constant.** Its basin has $2^{P/2 + 1}$ words at
  every $P$ (BK5 held). Post hoc, those are exactly the words white at every visible time or black at every visible
  time. One direction is a hand check. All white makes column $-1$ all black; all black makes column $-1$ a copy of
  the wall and column $-2$ all black; and an all-black column is followed by a white one, which with it is the
  checkerboard. The converse is measured, not proved.
- One crystal usually dominates, but not always. BK6 predicted that one brick other than the checkerboard holds more
  than half the words at every $P$ from 10 to 20; it was refuted at $P = 18$, where the largest holds 40%.
- Transients stay short: at most 1554 columns at $P = 20$, median 496 (BK7, the unexpected check, held). Every brick
  has density between 0.464 and 0.514. All but three (the checkerboard, the 7-ring's and the 325) are staggered, laid
  like bricks in a wall, as GC686's ring is.

**5. What this says about the prize.** Seen as tiles, the forced left half next to the 0101 wall is a crystal grown
from the wall leftwards, one column at a time. A periodic column 1 is a periodic seed, and the crystal it grows is
one of a few staggered walls. None is blank (Jen), so none can meet the white far left that a finite seed needs. The
prize's period-2 case asks the same of every non-periodic column 1 that a right half can produce: can such a seed
grow a crystal that turns blank? The question is what the monotile proofs answer for their own tiles, a forced
structure that rules out the forbidden pattern, but with the boundary in place of the tile set's own rules. Nothing
here proves it. Two leads come out of this reading:
- The hierarchy route would need supertiles of unbounded size forced by the boundary. The record has them only in
  the band, as Lemma B1's unbounded diagonal periods (§8.59). Carrying such a hierarchy from the band into the core
  is the record's open step, stated in tiling terms.
- The census lets column 1 be any word. Which of these bricks an actual right half can grow is a finite question at
  each period, and GC686's ring shows that the answer is not empty at period 6.
- The arithmetic route (Kari's $2^m 3^n \ne 1$) would need a quantity that the sideways map scales. The bricks show
  that no such quantity can scale on periodic columns, since bricks are cycles. Any such invariant must use the
  boundary.

### 8.73 The triangles on the right edge are a ruler sequence (2026-10-09)

*Cloud, from the owner's observation of 2026-10-09: the rightmost triangles touch the pyramid's right edge at
linearly spaced points and differ only in size. PROOFS.md entry 36 (Proposition 23, waiting room); exploratory probe
`rule30_cloud_edge_triangles.py`, no prediction pushed first. Chat CL074.*

The observation is exact. At every even time $t \ge 2$ a white triangle starts with its top-right corner at cell
$t - 1$, one cell inside the black edge, and at odd times none does. So one triangle touches the edge every two
steps. Its width depends only on the power of 2 in $t$: at $t = 2^v m$ with $m$ odd it is
$w(v) = \min\{j \ge 1 : p_j > 2^v\} - 1$, where $p_j$ is the period of the $j$-th right diagonal (OEIS A094605,
which also notes that NKS p. 871 lists one 64 too few). For $v = 1$ to 23 the widths are 2, 3, 5, 6, 8, 14, 15, 23,
24, 26, 28, 33, 35, 36, 38, 40, 42, 47, 48, 50, 53, 54, 57. The width is a ruler sequence, as the 2-adic valuation
is.

Why, in one line: at a multiple of a diagonal's period the diagonal is white, as it was at time 0. The first
diagonal whose period does not divide $t$ is one whose period has just doubled, so at the half-period it has been
flipped to black. This explains §8.68's widest triangles at $m \cdot 2^k$ and gives their exact widths. The
computation checks it at every even $t < 2^{24}$, and against a direct simulation at every $t < 4096$.

In §8.72's terms this is a hierarchical, Toeplitz-type tiling on the edge. The layer "width at least $k$" is periodic
with period $p_k$, and the periods double. The chaotic look of the right side is these periods outrunning the eye:
diagonal 54 repeats only after $2^{22}$ steps. The centre column sits on diagonal $t$ at time $t$, ever deeper, so
the order on each diagonal says nothing directly about the column, which is the prize's point.

### 8.74 Where the left side's order ends: an exact boundary, a random walk about a quarter of light speed (2026-10-09)

*Cloud, from the owner's question of 2026-10-09: where does the left edge go from orderly to random, and is there a
formal line or curve? Probe `rule30_cloud_left_boundary.py`; predictions pushed in 439b96b before the run. Chat
CL075.*

**The exact curve.** Read row $t$ from the left edge, $V_t$ with bit $e = x_t(-t + e)$. The first $e$ left diagonals
form a closed deterministic system (§8.31), so if rows $t$ and $t + P$ agree on them, those diagonals are periodic from
$t$ on, for ever. With $P = 2^{10}$, a multiple of every period in the band, let $B(t)$ be the number of diagonals on
which rows $t$ and $t + P$ agree: the lowest set bit of $V_t \oplus V_{t+P}$. Every diagonal shallower than $B(t)$ is
in its eternal stripes from time $t$ on, and diagonal $B(t)$ is not. $B$ never decreases. The boundary between order
and randomness is the curve $x(t) = -t + B(t)$. Lag $2P$ gives the same $B$ at every $t$ up to $2^{19}$.

**Its shape** (to $t = 2^{19}$; controls passed, two of three blind predictions held as worded, one of them on a
reading the curve refuted, two refuted).
- It does not run down the light cone. At the apex the band is born nearly full width, $B(16) = 18$, and the boundary
  starts near the centre column. By $t = 64$ it is at $x/t = -0.25$, and it stays near there: $-0.22$ at 1,024, $-0.250$
  at 16,384, $-0.254$ at 40,000 (§8.68's value), $-0.250$ at 131,072, $-0.245$ at 524,288. In the picture it is a
  line from the apex tilted about $14°$ from the vertical, against the light cone's $45°$.
- Its average speed is the leftward speed of information: $0.2437$ over $[2^{16}, 2^{19}]$ (LE2 held). The band edge
  advances $0.755$ diagonals per step on average, by 0, 1 or 2 diagonals at almost every step and never more than 14
  (LE5, which expected jumps of over 100, was refuted).
- About that line it wanders like a random walk. The deviation $B(t) - 0.754\,t$ stays within 41 to $t = 4096$, then
  reaches $-533$ at $2^{17}$ and $+592$ at $2^{19}$. Its structure function grows linearly in the lag, exponent
  $\alpha = 0.53$, not the $1/3$ of a KPZ front (post hoc; the registered LE4 used a residual that measured the
  method instead and was refuted).
So the formal boundary is a staircase whose average is a straight line at a quarter of light speed and whose
fluctuations are diffusive: a few hundred cells after a few hundred thousand steps, a tenth of a percent of the
row. That is why it looks straight at large scale and ragged up close. Proved here: only the definition and its
monotonicity. That the average speed is exactly the random rows' 0.246 remains a measurement (§8.30, §8.66).

**The apex, and whether the edge comes back** (post hoc; exploratory, no prediction pushed; the owner's questions of
2026-10-09: the edge "starts to the chaotic right of the centre column ... crosses it then carries on its descent",
and can it "ever wander back to the centre line and cross it"? Probe `rule30_cloud_left_apex.py`, same definition.)
- The start right of the centre is real, not an illusion. Left diagonal $e$ is born on the pyramid's right edge at
  $t = \lceil e/2 \rceil$ and crosses the centre column at $t = e$, so every left diagonal spends its youth on the
  right. Diagonals 0 to 17 settle before or as they cross: diagonals 3 to 8 are periodic from $t = 2$, as soon as they
  are born, and diagonal 17 from row 16. Rows 0 to 4 are ordered across their whole width, the band reaches right of
  the centre at rows 2 to 14 and 16, and the edge is at or right of the centre for the last time at row 20.
- From diagonal 18 on, every diagonal settles after it has crossed. Settling times grow by 1.32 rows per diagonal on
  average, crossing times by exactly one, so each diagonal settles further from the centre than the last. That
  difference is the edge's leftward speed, $1 - 1/1.32 \approx 0.244$.
- The edge does not come back in the window computed. The largest $x/t$ in each dyadic window from $2^7$ to $2^{19}$
  lies between $-0.176$ (at $t = 540$) and $-0.251$. Its closest approach, in units of $\sqrt t$, grows from 2 at
  $t = 64$ to 174 near $t = 506{,}000$, so the gap outgrows the random-walk wander. B's jumps of up to 14 diagonals in
  one step let the edge step back towards the centre locally, which is its jaggedness, but never far.
- Not proved. A return at row $t$ would mean that the whole left half of row $t$, centre cell included, already lies
  on the left edge's eternal stripes; nothing known rules that out.

**The front's spectrum, its floor, and the late rise** (the owner's follow-ups of 2026-10-09; probe
`rule30_cloud_front_spectrum.py`, predictions FS1 to FS6b pushed in 5da9c1c before the full run.)
- *Every left diagonal settles, so the front never reaches the left edge (proved, by hand).* Rule 30 gives
  $D_e(t+1) = D_{e-2}(t) \oplus (D_{e-1}(t) \lor D_e(t))$. Once $D_{e-1}$ and $D_{e-2}$ are periodic from time $s$,
  the first black cell of $D_{e-1}$ at a time $r \ge s$ resets $D_e$, which is periodic from $r + 1$. If $D_{e-1}$ is
  white for ever, $D_e$ is a running XOR, periodic at once with the same or doubled period. So every diagonal settles
  in finite time. The number of settled diagonals, which is $B(t)$ while their periods divide $2^{10}$ (they are 32
  at most to depth 395,905), grows without bound. So the front never reaches the left edge, and its distance from
  it grows; it moves away from the edge at about 0.755 cells per row. The same step is L382's.
- *The proved floor is weak.* Charging each diagonal its worst wait, one plus the longest white run of its neighbour
  nearer the edge, bounds the settling times from above. The measured settling times obey the bound at all 395,905
  diagonals. The mean charge is 5.33, so the floor holds the front only at $x \ge -0.81\,t$. The true $-0.245\,t$
  reflects diagonals settling 1.32 rows apart. The eventually-white diagonals are 2, 7, 28, 399, 53207, 58286 and
  87866, and the stripes' period goes from 16 to 32 after the last, the staircase Local's UB found on 21 rows (L383).
- *No frequency spikes.* The FFT of the front's steps $B(t+1) - B(t)$ in three windows (from $2^{12}$, $2^{15}$ and
  $2^{18}$ rows) has no bin at 20 times its neighbours' median (FS2 and FS5 refuted). Post hoc, the tallest peaks are
  the heights pure noise gives for that many bins. Folds by $t$ mod 16, 32 and 64 show no rhythm. The spectrum is
  flat, with low-frequency slope $-0.027$ (FS3 held), and the step variance is 1.25 per row. The jagged front is, to
  this test, a random walk with drift that keeps no trace of the stripes' periods.
- *The late rise in the front's chart* (FS6a held, FS6b refuted). The deviation from the dashed line, $B - 0.754\,t$,
  climbs from $-605$ at $t = 311{,}296$ to $+593$ at $2^{19}$. Of that, 234 cells come from the dashed line's slope,
  which sits below the band's long-run 0.7551. The other 964 come from a fast stretch, at 0.7597 diagonals per step,
  of 1.9 random-walk standard deviations, picked out after the fact. No change of the stripes lies there. The climb
  is real and ordinary for this walk; it looks sudden because the chart's doubling time axis gives its last octave
  half of all the rows.

**Two fronts, one rule: the right-hand front is the edge ruler** (the owner's questions of 2026-10-09: the chaos
"never consumes the full shape", and "can we construct a 'right side' waveform ... possibly rooted in the discovery
of the linear ruler"? Probe `rule30_cloud_right_front.py`, predictions RF1 to RF3 pushed in 02f62f3 before the run.)
- *A common definition.* Call a cell ordered at row $t$ when its diagonal, from row $t$ on, repeats with a period of
  at most $t$. On the left this is §8.74's band $B(t)$, where the periods stay at most 32 and the transients grow. On
  the right every diagonal repeats from row 0 (§8.27) but the periods grow, so the ordered strip is
  $R(t) = \#\{k \ge 1 : p_k \le t\}$ and the right front is the cell $x = t - R(t)$.
- *It is the ruler (proved by hand).* The periods $p_k$ are non-decreasing powers of 2, so $p_k$ divides $t$ exactly
  when $p_k \le 2^{v_2(t)}$. Proposition 23 then reads $L(t) = \#\{k \ge 1 : p_k \mid t\} = R(2^{v_2(t)})$, so
  $R(t) = L(2^{\lfloor \log_2 t \rfloor})$. The right front is a staircase that steps at each power of 2, about
  $2.5 \log_2 t$ cells inside the edge (RF1: $R(2^n)$ is §8.73's widths for $n \le 21$). At row $2^n$ the white
  triangle on the edge fills the ordered strip exactly; between powers of 2 the triangles are the ruler's shorter
  marks.
- *Its spectrum is all spikes (proved, and checked).* $L$ is a sum of combs $[p_k \mid t]$, so its Fourier transform
  over $[N, 2N)$ is $\sum_{p_k \le N,\ N \mid p_k b} N/p_k$ at bin $b$: pure spikes at the dyadic frequencies $j/2^m$,
  with an amplitude that depends only on $m$. The FFT matches this at every bin (RF2). 41% of the power is at $1/2$
  and 99.5% on denominators up to 256. The left front's steps have a flat spectrum with no spikes, the opposite case.
- *Neither order is ever consumed (proved for every finite seed).* A finite seed's left edge stays black and moves
  left at speed 1, so the settling step above makes every left diagonal settle and $B(t)$ grows without bound. Its
  right edge stays black and moves right at speed 1, so every right diagonal is a running XOR of a periodic
  sequence, purely periodic with a finite power-of-2 period, and $R(t)$ grows without bound. The chaotic core is
  always held between a left band growing linearly (measured: 0.755 $t$ cells, 38% of the row) and a right strip
  growing like $\log t$. Whether the core itself always survives is the open side; a band reaching the centre column
  is the case discussed above.
- *The right front remembers the seed* (RF3, the unexpected check: half held, half refuted). All 20 random seeds of
  width 16 have a period staircase different from the single cell's, and their $R(2^{20})$ ranges from 39 to 58
  against the single cell's 50 (only 8 within 4). Right diagonals are running XORs from the seed's own cells and
  never forget them, while the left stripes forget the seed (§8.31). So the left keeps a universal order, and the
  right keeps an order particular to the seed.
- *The inverse transform gives the ticks back, and the octave weights are the tick increments* (the owner's remark:
  the tick sizes can be inverse transformed into a wave; arithmetic on the recorded widths, no new run). A comb's
  Fourier transform is a comb (Poisson summation), so the ruler is a sum of combs in both domains. Let $n_m$ be the
  number of right diagonals of period exactly $2^m$, the tick's growth at octave $m$: 2, 1, 2, 1, 2, 6, 1, 8, 1, 2,
  2, 5 for $m = 1$ to 12. The spike at every frequency $j/2^m$ ($j$ odd) has height $A_m = \sum_{q \ge m} n_q/2^q$,
  so $A_m - A_{m+1} = n_m/2^m$: 1.764, 0.764, 0.514, 0.264, 0.202, 0.139, 0.046, ... ($A_1$ is also the mean width
  per row). Keeping one cosine per octave, $A_1 + \sum_m 2A_m \cos(2\pi t/2^m)$, gives a smooth chord of octaves
  whose crests fall on the largest marks (4096, 2048, 1024, 3072 and 512 lead for $t \le 4096$). With 12 octaves it
  follows the ruler with correlation 0.79; the odd harmonics $j/2^m$, $j > 1$, carry the same weight as each
  fundamental and sharpen the crests back into ticks. It is a Weierstrass-type sum, cosines at geometric frequencies.
- *The ruler counts in Gray code* (classical; checked for $t < 2^{16}$). Counting in the reflected Gray code, step $t$
  flips exactly digit $v_2(t)$. So the edge ruler's pattern of levels, $L(t) = w(v_2(t))$, is the Gray code's flip
  sequence, the same for any system whose edge marks depend only on $v_2(t)$ (the powers of 3 too, COLLATZ-PRIZE.md
  §8), and Rule 30's own part is the widths $w$. The page's Sound plays exactly this: pitch from $v_2(t)$, loudness and
  length from $w$.

*Corrected 2026-10-09, after GPT's GC748, GC749, GC752, GC755, GC756 and GC757 (each read by hand by Cloud: correct)
and Local's L390. The addenda above are kept as first written.*
- *Fixed lag.* $B_P(t)$ is capped at $j_P$, the first diagonal whose eventual period does not divide $P$ (GC736), and
  eventually equals it (L390 shows $B_2$ to $B_{16}$ at their caps). What grows without bound is the unrestricted
  settled prefix, and the age-$t$ ordered prefix $C(t) = B_{Q(t)}(t)$, $Q(t)$ the largest power of 2 at most $t$
  (GC752); no rate is proved. Lag $2^{11}$ gave the same $B$ as lag $2^{10}$ at every $t \le 2^{19}$, so by GC752's
  plateau lemma the measured curve is $C(t)$ at every $2^{10} \le t \le 2^{19}$.
- *The floor.* The probe's settling times are $P$-prefix onsets, so the floor and $\bar c = 5.33$ hold on the
  measured 395,905 diagonals only; "$x \ge -0.81\,t$" is a finite-prefix floor, not an asymptotic one.
- *Two fronts, one rule.* The left side of the common definition is $C(t)$, as above. On the right, for a general
  seed the ordered strip is the prefix counted by the joint periods $Q_j = \operatorname{lcm}(p_0, \ldots, p_j)$
  (GC756), which does not assume individual periods monotone (no non-monotone example is known; GC761); RF3's
  $R(2^{20})$ values are counts, not prefixes. Every
  nonempty finite seed has unbounded right periods (GC755) and a prefix of at least $\lfloor \log_2 t \rfloor$.
  The white-run ruler and its spectrum belong to the single cell; a general seed's analogue is the return to its own
  bits (seed 11 has a black cell just inside its edge at $t = 2$).

**The owner's front argument against period 2, and the shunted column** (2026-10-09; the owner's idea, Cloud's
reading; GPT's independent audit requested with priority in CL079). The idea: the band's edge moves left and never
re-crosses the centre, so the right side is always chaotic, and a 0101 centre column could exist only if the ordered
band crossed the centre and made it deterministic. Cloud's reading, which the owner accepts pending GPT's audit:
- The premise is measured, not proved. The edge is at or right of the centre for the last time at row 20 (above).
- The band is periodicity along left diagonals. The centre column meets each left diagonal once (diagonal $t$ at
  row $t$), so an eventually periodic column needs no band, and the band's position does not constrain it.
- A counterexample would look the same. With column 0 eventually 0101, column 1 is never eventually periodic
  (Proposition 7, Jen), so it too has disorder beside the centre and the band to the left.
- "Right of the front is chaotic", in the sense needed, is Prize Problem 1 and more: every fixed column ends there.

*The shunted column* (the owner: "move the centre column ... shunt it left or right and see what happens";
`rule30_cloud_shunted_column.py`, predictions SH1 to SH5 pushed in a8cc17a before the run; 8.6 s at $2^{16}$ rows,
171 columns from $-8000$ to $8000$). By shift invariance, column $c$ is the centre column of the seed moved to $-c$.
- A column moved right ($c \ge 1$) never meets the band after row 20. A column moved left by $|c|$ is born in the band
  and leaves it at row $3.92|c|$ to $4.29|c|$ (mean $4.0|c|$; SH1 held there). After that it stays in the core,
  except for re-entries within 109 rows of the crossing. Those come from the edge's jaggedness, and they refuted
  SH1's 64-row allowance at four of 80 columns.
- The band does not make a column regular (SH3 refuted, the surprise). In the band a column has no short period
  (SH2 held), flips at 0.501 of rows, and has as many distinct ten-cell words as in the core (all 1,024 at $-8000$).
  Post hoc, the band's order runs across columns. Column $c - 16$ is exactly column $c$ delayed by 16 rows: every
  one of 3,208, 4,484 and 3,984 band cells agrees at $c = -1000, -1500, -2000$, against chance (1,554 of 3,208) for a
  delay of 1. Those cells lie on one diagonal 16 rows apart, and the band's periods divide 16 to depth 87,866.
- In the core no column alternates beyond chance (SH4 held). The centre's longest 0101 stretch is 16 cells, the same
  as its fair-coin twin's. The most alternating is column 1, at 24 cells, about what the luckiest of 171 fair columns
  gives. SH5 held: columns flip at 0.490 of rows just after the front leaves them and at 0.500 later.

So a column looks the same wherever the front crosses it: the second point above, seen in data.

*GPT's audit (GC774, GC775), and the owner's restatement.* GPT agrees that the argument fails at the link from the
front to a vertical trace. Band membership at row $t$ gives $x_t(c) = x_{t+P}(c-P)$, a comparison along a diagonal,
never $x_t(c) = x_{t+P}(c)$. Points 2 to 4 stand with their scopes. Point 1 gains a proved addition: for the fixed
lag $P = 1024$, GC736's cap $B_P \le j_P$ with eventual equality means the lag-certified prefix contains the centre
only finitely often. That holds whatever the centre column does, so it gives no contradiction. For the growing-lag
front $C(t)$, non-return after the measured window is unproved. Scope corrections to the shunted-column text above:
"stays in the core" means to the end of the window ($2^{16}$ rows). The delayed copy is exact where both cells lie on
settled diagonals whose periods divide 16, and "coin-like" was measured only on the columns sampled. The owner then
restated the idea: a constructed 0101 column is a valid descent only if it is consistent with the region it sits in.
Its exact form in this record is the chain of PERIOD-TWO.md §1. A 0101 column 0 and its right neighbour force every
column to their left (§5), and the column can belong to a finite seed only if that forced left half is eventually
white. Conjecture LR (§7) says that no column 1 at all makes it so. The case of period 1 is proved (Condrey); period
2, the prize's case, is open. Among 1,703,936 cases to depth 192 (§5) there is no counterexample, which is evidence,
not proof.
The owner's follow-up: by the apex, where the front starts right of the centre, the only valid descents keep the
front on the correct side. A hypothetical counterexample already does. Shifted to start at its periodic row (§5), its
column starts in the core with the front to its left, as the single seed's centre is from row 21 on. The apex is
particular to a seed at the centre, and it showed no regular column even there: while the band held the centre (rows
0 to 17) the centre column read 110111001100010110, with no period.
Correction (GPT GC776): shifting time to the periodic row keeps the seed finite and the clock, but it does not by
itself place the front left of the column. What holds is that the column eventually leaves the fixed-lag prefix, and
that the front's position by itself gives no contradiction.

*Four quadrants: is the band's inverse there, around a 0101 centre?* (the owner: "does there exist on the centre
column the inverse - an orderly vertical (which it already is) and coin-flip diagonals (unknown)";
`rule30_cloud_four_quadrants.py`, predictions FQ1 to FQ4 pushed in 4e0e391 before the run.) In a finite
configuration every diagonal, in both directions, is eventually periodic: each family is a closed system anchored at
its own edge (§8.27, §8.74). So only columns can carry the open question. The four combinations:
- coin-like columns, ordered left diagonals: the band (above, the shunted column);
- coin-like columns, coin-like diagonals: the core;
- an ordered column with ordered diagonals: ring orbits, such as the necklace, whose clock reads 010101 (§8.71);
- an ordered column with coin-like diagonals: the period-2 hypothetical, built here with 0101 down column 0, the
  left half forced from it (§5) and column 1 either random (LR's setting) or driven by a finite right half (B's).

Measured over 4,096 rows: the left diagonals through the hypothetical centre flip at 0.50 and have a coin's variety
of 8-bit words (FQ1 held, apart from a word threshold set above what fair coins reach). The right diagonals flip at
0.750, the light-speed OR law (FQ2). Columns from $-3$ outwards are balanced (FQ3), and column $-1$ is black at every
odd row. Post hoc, the finding of the run: with a finite right half, the inverse is a strip, not a column. Column 1
is the record's wheel (§8.5), with 13 to 18 distinct 8-bit words of 256. The forced columns $-1$ to $-10$ average 14
to 21 words, fading to coin-like by about column $-150$, while the diagonals through the strip stay coin-like. So the
hypothetical is the band turned on its side: ordered verticals and coin-like diagonals. In the single seed, every
column from $-40$ to $40$ shows all 256 words. This is not a proof. It covers four right halves of width 16, and a
counterexample's right half is whatever its row holds when the period begins, kicking the wheel from the right
(§8.11). But it gives the owner's "wrong band" a picture: a 0101 centre does not sit alone in the chaos, it needs
a strip of vertical order around it, and the real pyramid shows none near its centre in the rows measured.
Scope corrections (GPT GC782). The periodicity test looked at suffixes only, for periods up to 64 on diagonals: no
tested suffix period $\le 64$. FQ3 sampled every 31st column (3, 34, ..., 995). The post-hoc strip used four right
halves different from FQ's four, because the random stream consumed different draws. The 0.750 is measured on these
draws: the OR law's three in four needs fair drivers, and a zero right half with $\tau(0) = 0$ keeps $x_k(k) = 0$ for
ever. Few distinct words is finite variety, not order: a nonperiodic word with ones at the squares has only nine
eventual 8-bit factors. So "it needs a strip" is an observed picture from four small draws, not a theorem. The
theorem nearest to it is G.GPT256 above: with any actual right half, column $-1$ is at least three-quarters black.

### 8.75 Triangle ladders: descending from triangle to triangle (2026-10-09)

*Cloud, from the owner's idea of 2026-10-09: "From the top, select the first largest black triangle, then, draw a
line to the next largest triangle anywhere underneath it ... If 2 triangles compete for the next largest, the path
splits and forks like lightening. Also possible, select the next ... triangle of the exact same size and descend
that way." Probe `rule30_cloud_triangle_ladders.py`, predictions TL0 to TL4 pushed in dd31ae5 before the run, to
depth 8,192 (12,623,057 triangle tops). Not §8.25's lightning, which walks cell by cell.*

**The reading.** A triangle is its top, a maximal white run that does not continue one above (§8.18, §8.68).
"Underneath" is the light cone below the triangle's tip. The **bigger** rule goes to the first row in that cone
holding a wider triangle, and takes the widest there. The **same** rule goes to the first row holding a triangle of
the same width. Ties in that row fork the path, and branches that meet merge.
- *The bigger rule is a single bolt.* From 100 random core triangles it forks at 1.1% of its steps (TL2). It climbs
  about 1.9 widths per step, not the predicted one, and ends at widths 20 to 22 by row 8,192, near $2 \log_2 D$, the
  core's own widest (§8.68). It never reaches the edge: an interior cone meets an edge triangle only once the ruler
  is wider than the start's distance from the edge, about $2.5 \log_2 t$ (Proposition 23).
- *On the edge it is the ruler* (post hoc for this start). From the widest triangle of the first 32 rows, the edge
  triangle at row 32, the bolt runs the ruler's tallest marks exactly: rows 32, 64, 128, ..., 4096, widths 8, 14,
  15, 23, 24, 26, 28, 33. From the topmost triangle it is knocked off at row 6 by a core triangle of width 4, which
  comes before row 8's edge width 5, and never returns (TL1 refuted).
- *The same rule is lightning* (TL3 held). Narrow triangles fork often: 11.9% of steps at width 1, 19.7% at width
  2 and 10.9% at width 3, with a median 225 triangles alive 500 rows below a width-1 start. From width 5 up the
  forks fall below 5%. On the edge, from row $2^k$ the same rule walks the ruler's equal marks, rows $3 \cdot 2^k$,
  $5 \cdot 2^k$ and $7 \cdot 2^k$, only for $k \ge 8$ (width 23). Below that a core triangle of the same width
  comes first (TL4 refuted as worded, which put the threshold at $k = 6$).
- What it says: the two rules see the two orders of §8.74's "Two fronts". The bigger rule finds the right edge's
  dyadic order when it starts there, and the uniform core's widest triangles otherwise. The same rule's branching is
  set by how common each width is, $3 \cdot 2^{-(L+4)}$ per cell. Nothing here bears on the centre column.

### 8.76 Period 1, proved again here: an audit of Condrey's theorem (2026-10-09 14:17 BST)

*The owner asked whether the period-1 result had been verified by us or only trusted. It had been cited, not audited
in full: Cloud read the abstract, conclusion and Lemma 1 (PRIOR-ART.md, 2026-10-04); GPT read all seven pages and
restated the two mechanisms, checking the black wall's algebra (G11); §5's check A reproduced the published horizon
maxima for widths 1 to 7. Nobody had written the whole proof out and second-read it. Cloud wrote it out by hand from
the rule alone, having read only Condrey's statement and G11's summary, and checked each step by machine. It is
short, and it holds. Second reading requested from GPT and Local (CL083).*

**Theorem (Condrey, arXiv:2609.09431).** No nonzero finite configuration of Rule 30 has an eventually constant column.

*Proof.* A finite configuration has finitely many black cells on a white background, and Rule 30 keeps it finite and
nonzero (step 2 below, and the same calculation at the left edge). By shift invariance take column 0, and by shifting time take column 0 equal to a constant
$c$ for every $t \ge 0$. Rule 30 read for its left input is

```math
x_t(i-1) = x_{t+1}(i) \oplus \big(x_t(i) \lor x_t(i+1)\big),
```

so columns 0 and 1 over $t \ge s$ determine every column to their left over $t \ge s$ (Condrey's triangular
uniqueness, the forced left half of §5).

1. *$c = 1$.* Claim: $x_t(-j) = 1$ for even $j$ and $0$ for odd $j$, for every $t \ge 0$. For $j = 1$,
   $x_t(-1) = 1 \oplus (1 \lor x_t(1)) = 0$, whatever column 1 is. For $j \ge 2$,
   $x_t(-j) = x_{t+1}(-j+1) \oplus (x_t(-j+1) \lor x_t(-j+2))$, which is $0 \oplus (0 \lor 1) = 1$ for even $j$
   and $1 \oplus (1 \lor 0) = 0$ for odd $j$. So row 0 is black at every even depth: infinitely many black cells.
2. *The right edge.* If $E$ is the rightmost black cell of row $t$, then $x_{t+1}(E+1) = 1 \oplus 0 = 1$ and every
   cell beyond is $0 \oplus 0 = 0$, so the rightmost black cell advances exactly one cell a step.
3. *$c = 0$: something black lies to the right.* If every black cell of row 0 were at a site $\le 0$, then
   $E_0 \le 0$, and by step 2 column 0 would be black at $t = -E_0$. So row 0 has a black cell at a site
   $\ge 1$.
4. *$c = 0$: it reaches column 1 and stays (the OR latch).* Let $a_t$ be the leftmost black site $\ge 1$. With
   column 0 white, the sites $1 .. a_t - 2$ stay white ($0 \oplus 0$) and site $a_t - 1$ turns black
   ($0 \oplus (0 \lor 1)$), so $a_{t+1} = a_t - 1$ while $a_t \ge 2$. Column 1 is black at $t_1 = a_0 - 1$, and
   $x_{t+1}(1) = 0 \oplus (x_t(1) \lor x_t(2)) \ge x_t(1)$ keeps it black for ever.
5. *$c = 0$: the contradiction.* From $t_1$ on, columns 0 and 1 are white and black. Then
   $x_t(-1) = 0 \oplus (0 \lor 1) = 1$, $x_t(-2) = 1 \oplus (1 \lor 0) = 0$, and the induction of step 1 gives
   black exactly at odd depths. Row $t_1$ has infinitely many black cells, but it is finite. $\square$

*Machine checks* (scratch, not a probe; each passed). Step 1 for 500 random columns 1, depths 1 to 60. Step 2 for 500
random rows over 30 steps. Step 4 for 2,000 random right halves with column 0 held white: the leftmost black cell
reaches column 1 at exactly $a_0 - 1$ and column 1 stays black to step 40. Step 5's checkerboard to depth 60.

*What the audit shows.*
- Condrey's statement checks, with both of G11's mechanisms. A black wall forces the checkerboard whatever the right
  side does. A white wall forces it only after the latch, which uses the real right evolution (step 4).
- Step 4 is where period 1 uses the real right side. For an arbitrary column 1, LR's setting, a white column 1 next
  to a white wall forces a white left half, so period 1 is false in that setting. That is why LR is stated for
  $p \ge 2$. It is also the point of GPT's adversarial block (GC786): this period-1 proof needs the
  right half to be real. It motivates testing that distinction at period 2; it does not prove LR false there or
  establish that every period-2 proof must use the right half.
- Nothing in the proof is probabilistic or open. Period 1 is closed by elementary means: four lines of Rule 30's own
  update, twice.


*Additional independent reading (GPT, GC789, 2026-10-09).* All five mathematical steps pass by hand, including
the finite/nonzero time shift, the right-edge crossing and both endpoint cases of the right-side latch. The
all-white seed is an essential countercontrol: it stays white forever and is explicitly excluded by the theorem.
Local independently completed the requested filing as PROOFS.md entry37 (L417); no duplicate entry is added. The
period-2 implication in the commentary above has been qualified: need for the real right side in this proof is
not a logical necessity theorem about every proof of a different period. No scratch machine check was replayed.
*Second reading (L417).* Local checked the proof by hand on the three points asked (the time shift at both edges,
step 3's range, step 4's induction at a_t = 2) and filed it as PROOFS.md entry 37, labelled as Condrey's theorem: no
novelty and no prize claim.

*The other foundations (the owner's follow-up, 14:24 BST).* Each outside result the record leans on, and how it stands:
- *Jen (1990), adjacent columns never both eventually periodic.* Proved here as Proposition 7 (§8.13, PROOFS.md B′17,
  three steps), which Cloud reread today. Jen's paper itself was never read, only summaries and Kopra's Corollary
  3.7, which restates it. The record does not depend on that paper.
- *Jen (1986) and Rowland, the diagonals repeat.* Proved here: right diagonals in §8.27 and left diagonals in §8.74.
  Neither proof has been compared line by line with the published ones.
- *Kari and Kopra.* Not load-bearing (§8.55).
- *Uniform rows stay uniform under Rule 30.* Used only by side questions (C.5, the alternation work). It is elementary
  for a left-permutive rule.
- *König's lemma* (LR is equivalent to every R(d) being finite): standard.
- *The solver's UNSAT verdicts.* This is the soft spot, and it is not a paper. Every decided value of RR, RR2 and RR3
  rests on kissat reporting UNSAT, and none has a checked certificate. Only Local's CX run has DRAT proofs that
  drat-trim verifies (80 of 80, L404). Certifying them is offered to the workers in CL084.

### 8.77 Rule 30's entropy is its width-2 trace's, and the 2-adic frame second-read (2026-10-09 16:29 BST)

*Cloud, from the overlooked-work survey's open items (CL085 steps 3 and 4) and Local's question in L427.*

**Guillon's conventions** (doctoral thesis, Paris-Est 2008, read in the copy the survey saved). A cellular automaton
has a diameter $d$, an anchor $m$ and a local rule on the window $[i-m, i-m+d)$ (Définition 3.1.1). On
$\mathbb Z$ its radius is $r = m = d - 1 - m$, so Rule 30 has radius 1. The column factor of width $k$ at cell
$i$ is the sequence of windows $[i, i+k)$ of $F^j(x)$, in the physical frame (Définition 3.4.10). Positive
expansivity to one side of width $k$ asks that two configurations differing on that half-line differ in some
window $[0, k)$ (section 4.6).

**Lemma (proved here).** Rule 30 is not positively left-expansive of width 1, and it is of width 2.
*Proof.* $0^\infty$ and $(01)^\infty$ are fixed points (in $(01)^\infty$ a white cell sees black on both sides and
stays white, and a black cell sees white on both sides and stays black). Placed with column 0 white, they differ on
every left half-line and agree on column 0 for ever; shifted by one, $(10)^\infty$ and $0^\infty$ agree on column
$-1$. Width 2 suffices by Proposition 7's formula, $x_t(k-1) = x_{t+1}(k) \oplus (x_t(k) \lor x_t(k+1))$: columns 0 and
1 determine every column to their left. $\square$

**Consequence.** Guillon's Remark 4.6.9 (traces of every width $k \ge r$ are conjugate) and Proposition 4.8.5
(entropy equals the width-$r$ trace's) hold for Rule 30 at width 2, not at its radius 1. Read with $r = 1$ they would
make the width-2 trace conjugate to the width-1 trace, and the entropy $\log 2$. The conjugacy is refuted by
fixed-point counts: the width-2 trace has exactly three fixed points, $(00)^\infty$, $(01)^\infty$ and
$(10)^\infty$, while the full width-1 trace has exactly two. This does not refute the entropy value
$\log 2$, which remains possible (GPT's independent audit GC814). Where the thesis's
widths slip (perhaps Proposition 4.6.2's width $m$) is not identified here; only the statement for Rule 30 is
settled. For every $k \ge 2$ the width-$k$ trace is determined by its last two columns, so it is conjugate to the
width-2 trace, and the topological entropy of Rule 30 is that trace's entropy:

```math
\log 2 \;\le\; h_{\mathrm{top}}(\text{Rule 30})
\;=\; \lim_{n\to\infty} \tfrac1n \log N_2(n)
\;\le\; \tfrac{1}{14}\log 476596 ,
```

where $N_2(n)$ counts the physical frame's width-2 words of length $n$ (Local's TW, L427). The lower bound is the
width-1 trace, a full-shift factor. The upper bound is TW's count at $n = 14$, about 1.347 bits a step, by
subadditivity. That answers L427: the counts must be read in frame F and at width 2. They measure Rule 30's
topological entropy itself, which no published value was found for (the survey).

**The survey's 2-adic derivations, second-read by computation** (scratch, each passed):
- In the frame moving with the right edge, with bit $k$ of $R_t$ at cell $t - k$,
  $R_{t+1} = R_t \oplus (2R_t \lor 4R_t)$ and the centre column is bit $t$ of $R_t$. Checked on full rows for
  $t < 300$ and on the centre for $t < 2000$.
- $x \mapsto x \oplus (2x \lor 4x)$ permutes $\mathbb Z/2^k$ for every $k \le 20$: an invertible T-function. The period
  of 1 modulo $2^k$ for $k = 1$ to 16 is 1, 2, 2, 4, 8, 8, 16, 32, 32, 64, 64, 64, 64, 64, 64, 128, as the survey
  printed.
- Rule 30 is not right-closing. A witness is $0^\infty 1 (010)^\infty$ and $0^\infty 1 (100)^\infty$: they are
  distinct, equal far to the left, and have the same image.
- Not checked here: the application of Coven, Pivato and Yassawi's odometer theorem, and the vertical entropy bounds.
  Those are reading items (CL085 step 3).

*Added later on 2026-10-09.* Local's TWX (L436) extends the exact counts to $n = 17$ ($N_2(17) = 5{,}615{,}036$), so
$h_{\mathrm{top}}(\text{Rule 30}) \le \tfrac{1}{17}\log_2 5615036 \approx 1.3189$ bits. The successive ratios (2.2667 at
$n = 17$) are still falling, so this is a bound, not an estimate. GPT's audit (GC814) agrees that wider traces are
conjugate to width 2, and it corrected the fixed-point sentence above: the fixed points refute the conjugacy, not
the value $\log 2$.

**Kopra's 2023 theorem contains the single-column result** (the survey's open gap; arXiv:2202.13809 read in full).
Its Theorem 3.5 says that for a rapidly left-expansive automaton with width $w$, the width-$w$ trace of any
configuration with a white left tail is never eventually periodic. Kopra says it reproves his 2021 result
(Proposition 3.8 of TCS 851, cited by the survey as Proposition 2.8 of the arXiv version) and Jen's Proposition 3
"with essentially the same proof". The width comes from the left-expansivity dimensions: $(1, 1, 1)$ for the $p/q$
automata, so width 1, and $(0, 1, 2)$ for a left-permutive rule such as Rule 30, so width 2, which is Jen's theorem.
His Problem 4.8 is the single cell's centre column. His closing remark is a barrier for the counter-model library:
the class cannot settle width 1, because it contains Rule 90, whose single-cell centre column is eventually white. So
a proof for Rule 30's width-1 trace must use what Rule 30 has and Rule 90 lacks. At period 1 that is the OR latch
(§8.76, step 4).

**Sablik's cone signs, audited** (GC813 left them open; TCS 400 (2008) re-extracted, where the minus signs are lost
in the font). His shift is $\sigma(x)_i = x_{i+1}$, and his tube of slope $\alpha$ compares
$\sigma^{\lfloor n\alpha \rfloor}F^n$, so $\alpha$ is the velocity of the observed window, rightward positive. His
neighbourhood is $[r, s]$, which is $[-1, 1]$ for Rule 30. Example 3.4's left-expansive half-line for a
left-permutive rule then reads $(-\infty, -r)$, which is $(-\infty, 1)$ for Rule 30. Only that sign reading contains
the vertical, and the vertical must be left-expansive, because columns 0 and 1 determine the left half (Proposition
7). The other reading, $(-\infty, r)$, would exclude it. So the survey's reconstruction stands. The right-permutive
half-line is the mirror image, $(-s, \infty)$. With Remark 5.2 (a right-expansive slope forces right-closing) and the
not-right-closing witness above, Rule 30 has no right-expansive slope and so no expansive slope.

**Kopra's barrier does not rest on symmetry** (Math SE 4141181's answer, fetched by the owner;
`rule30_cloud_lone_column.py`, predictions first). Trevor's question asks for a two-colour automaton with an
asymmetric rule and a start such as $0^\infty 1 0^\infty$ that has at least one but finitely many eventually periodic
columns, with aperiodic columns on both sides. Kopra's accepted answer (2022) simulates a three-colour solution with
non-overlapping marker words. That reduction cannot meet the question: an overlap of one letter is forbidden, so in a
binary non-overlapping code all words share their first letter and all share their last, and the encoded orbit has
constant columns in every block. Here four of every seven columns are constant, so infinitely many columns are
periodic. The question does have answers. In the linear rule with moves $\{-3, -1, +3\}$,
$x_{t+1}(j) = x_t(j+3) \oplus x_t(j+1) \oplus x_t(j-3)$, the seed's own column is black once and then white for ever.
The proof is a carry argument: a black cell at $(t, 0)$ needs move counts $a, b, c$ with pairwise disjoint binary
digits and $b = 3(c - a)$, and the lowest set bit of $c - a$ is then shared by $b$ and $c$. Every other column with
$|j| \le 64$ is not eventually periodic, which is decided exactly. A linear column is 2-automatic, and with the
centre move present it restarts at every large power of two, so it is eventually periodic only if it is purely
periodic with a power-of-two period. The move set is not a palindrome up to a shift, so no reflection in any frame
fixes the orbit. The search found 20 such linear rules of range at most 3, and no elementary rule with an asymmetric
orbit and a lone periodic column. For the counter-model library (CL084): left-permutive rules with no symmetry at
all can have an eventually white centre column from one cell. A proof for Rule 30's centre column must therefore use
its nonlinearity, the OR, and not only permutivity or the absence of a mirror.

**Kopra's MathOverflow table, recounted** (`rule30_cloud_periodic_points.py`). The owner found the PDF behind
MathOverflow 429509: Jeremias Epperlein's dissertation, *Topological Conjugacies Between Cellular Automata* (TU
Dresden, 2017), Appendix A. Each set $\{x : f^q x = f^{q+p} x\}$ is a subshift of finite type, counted exactly from
its de Bruijn graph. All 42 entries of the thesis's Rule 30 rows match, so no Rule 30 configuration has least
temporal period 2. The new counts for least period $p = 7, \dots, 10$ are 105, 88, 180 and 550, every such set
finite. The 84 points of least period 6 form a single orbit, and it is GC686's 84-cell all-S ring, so that ring is
the only Rule 30 configuration of least temporal period 6. The unexpected check was refuted: travelling waves are not
rare. All points of least period 1, 3, 5 and 6 are travelling waves, and none of periods 4, 7 and 10.

**Scope of the lone-column result (GPT's audit, GC829).** GC829 checked the restart lemma and K4's carry proof by
hand and found both sound. It asks that the window be kept in view, which corrects the lone-column paragraph above.
For the moves $\{-3, -1, +3\}$, only the centre column is proved: it is eventually white. Columns with
$|j| \le 64$ are decided; beyond them nothing is established, so "exactly one eventually periodic column" is not
proved for that rule. Both the asymmetric rule and the lone column are fully proved for the moves $\{-1, +3\}$
(`rule30_cloud_lone_column.py`, K3): every column $j \ne 0$ has infinitely many black cells and arbitrarily long white
runs. That rule meets the letter of the question, but its orbit is mirror symmetric about the moving line $j = t$.
The barrier claim above needs only the proved centre column.


### 8.78 The status board's history, archived at the third triage (2026-10-09)

*Moved verbatim from PERIOD-TWO.md §6 at the third board triage (Local, L468 drafted, agreed by GPT in GC845 and asked for by Cloud in CL093), so the board can say status, change and what is left in a few lines. Nothing was edited; each row is the table row exactly as it stood at 2026-10-09 19:27 BST.*

**Q6, as it stood before the third triage.**

| Lead | Status | What we have | What is left |
|---|---|---|---|
| Q6, LR refuted by construction | **PART** (kept at the second triage, 2026-10-08) | The exact records cover every column 1: no left half is zero from any depth up to 89 onwards (§8.36, §8.37; R(89) = 75, Local's run of 2026-10-05; this row said 85 until Local's upkeep of 2026-10-07). R(93) running (RK, resumable). Realizable records (RR, L247, `rule30_records_real_sat.py`): over every configuration, by SAT over the light cone, the longest white run of the forced left half from depth d is 7 to 15 for d = 21 .. 81 (at least 14 at 89 and 97), against 17 to 75 for every column 1; ZR2 gives the same exactly to d = 19. RR2 (`rule30_records_real_sweep.py`, resumable, running; 2026-10-08 05:50): realizable records 10 to 16 for d = 74 .. 93, maximum 16 at d = 87 and 93 (RR2-P2's 'above 15' held at 87). Cloud's RRP (CL050, `rule30_cloud_rr_phases.py`, 2026-10-08, Local's L291 request): RR's deep records split by phase in RRX's independent encoding, phase 0 / phase 1 = 10/11, 10/11, 11/10, 9/10, 11/12 at d = 49, 57, 65, 73, 81; the maxima reproduce RR exactly, the phases differ by exactly 1, and the clock's suffix threshold stays at 0 to 11. Cloud's RRX (CL036, `rule30_cloud_rr_replay.py`, 2026-10-08): an independent encoding (CaDiCaL, per-phase solves, four-input XOR) reproduces ZR2 at d = 3 .. 19 and R_real = 15, 11, 7, 8, 8, 8 at d = 21 .. 41; deletion-minimal clock cores of each first impossible length start at time 4 to 7 at every depth, so ending a realizable run needs the clock from its first beats, not only near the run's entry. Cloud's RRL (CL041, at GPT's request): the three reviewed forbidden words of column 1 (11, 00000, 101001) reproduce the actual per-phase records exactly at d = 3 .. 19, and the seven minimal forbidden words up to length 10 do so to d = 25 (phase 1 to 37); beyond that the relaxations reach 13 at d = 41 against actual 6 to 8. The first gap's witness turns on a 3-gap that can only begin a right half (factor 01000010001001). Section 8.36's R(d) is the phase-0 record, while RR, RR2 and L247's R_real are maxima over both phases (RR's encoding has a phase variable; Local, L286); per-phase values exist at d = 21 .. 41 (CL038). RK (R(93)) moved on 2026-10-08 to a spare machine of the owner's, validated by identical checkpoint lines at depths 53 and 61 and on six recomputed depth-93 tasks. 2026-10-09, the all-S and S/L renewal line (GPT GC686 to GC740, Local L368 to L378, Cloud CL071 to CL073): an explicit infinite all-S orbit exists, the 84-cell ring 0x688eb74a45efb082671ee, which turns 14 sites per step (GC686, CL071) and is rigid in its domain (GC687); every marker-aligned all-S trace has the same five-column slab (GC688). With finite left support, an infinite or eventually all-S tail is impossible (GC704), and so is any eventually periodic S/L renewal tail (GC706, GC707). A marker-aligned block of n completed S gaps forces the left row to copy the ring to depth 6n, so J >= 6n - 3, and the minimum is exact (GC705, sharpened by Local's `rule30_all_s_left_depth.py` in L372, with GC710's closing tick). Mixed words: forced left prefixes decoded (GC708); the S/L branch pivot sits at depth B + 7, and the next black-time guard is x_d(-1) = E xor H0 xor (A and P) (GC713 to GC717); a renewal needs c_8 white (GC718); no fixed-prefix return map closes (GC719). Turning rows: every turning row with s != p is spatially periodic (Proposition 22, entry 35, and GC727), an all-S turning row is the ring (entry 35's corollary), the critical class needs p = 84m and a finite defect needs 336 to divide p (GC726, GC728, GC729), and critical uniqueness reduces to left-asymptotic extensions (GC731). Change budget: r letter changes by time T need T <= (J_0 + 20)(2^(r+1) - 1) (GC735). The sparse word concat S^(2^j) L passes the duration and near-square tests (GC737), but G2.3's permanently white diagonal excludes it through time 393,360 for J_0 <= 53,052 (GC738 to GC740). Missing: an actual inter-run compatibility input that gives unbounded exclusions. Records (Local's RR2, `rule30_records_real_sweep.py`, L399): R_real(d) is decided to d = 97, at most 17 (d = 94) and climbing slowly; d = 98 .. 120 have capped lower bounds of 12 .. 15. Its L twin (Local's AL, `rule30_all_l_period10.py`, L380): a rigid 155-cell all-L ring with F^2 = shift^31 exists, and n completed L gaps force J >= 10n - 6, exact. Its slab: columns 1 .. 4 are forced at every loop with a following L (GC744), and columns 1 .. 6 once five L gaps are completed (Local's ALF, L387, DRAT-verified). For S (Local's ASF, L393, DRAT-verified): columns 1 .. 13 of the 84-ring at every loop with two S gaps behind and seven ahead. 2026-10-09 afternoon: critical all-L uniqueness, bounded and certified (Local's CX and CXE, `rule30_critical_bridge_sat.py`, L404): no non-ring row with G^310 = id, left-asymptotic to the 155-ring, has a bridge of width <= 24 and a periodic tail of period <= 10 (100 instances, every UNSAT DRAT-verified). Promoted today with second readings by Local: G250 (the exact L cost makes the letter-change budget (J_0 + 5)(2^(r+1) - 1)), G251 (a settled-white diagonal caps L blocks), G252 (a q = 155 tail at p = 310 needs an odd adjacent correlation), G253 (a first profile deviation is a swapped pair that clears next tick) and G256 (a 0101 centre forces column -1 to long-run density at least 3/4, by G240's no-11). GC784 gives the S/L-family densities (5/6 .. 9/10 at column -1), exact on both rings (L412). 2026-10-09 evening: every deciding UNSAT call of the realizable records, d = 3 .. 97 (ZR2's and RR2's decided values), now carries a DRAT proof checked by drat-trim (Local's RRC, `rule30_records_real_certs.py`, L438; the owner's foundations audit, CL084): R_real(d) to 97 rests on certificates, not solver verdicts. 2026-10-09 evening, Cloud's RR3 (`rule30_cloud_rr3.py`, RR2's capped depths decided with 3-hour calls): R_real(98 .. 106) = 14, 13, 15, 15, 14, 14, 13, 13, 12 (101 and 105 by the plateau law R(d + 1) >= R(d) - 1); nothing decided above 15; 107 .. 120 running. Critical bridge (GC820 to GC843, Local L451 to L463): GC828's retained template D survives the six-equation periodic coupling gate (TC); a ring carrying D with the joint least-155 pair needs at least 19 cells (GC839, GC840); no ring of 14 .. 20 cells carries D at all (L463, exhaustive, scratch); the forbidden word 000001101 is proved by hand and filed (G.GPT267), and 0001101011 by hand too (GC843, read by Local and filed as G.GPT268, L466). Cloud's RD (`rule30_cloud_ring_template.c`): no ring of up to 30 cells carries D, and among rings of 2 .. 30 cells only the 18-cell ring has any G-column of least period 31. | Depths beyond the records. Nothing constructive has been tried. Local's note (2026-10-07): depth 93 by records_bits.c would take about 2.5 days on the M5's 10 cores (85 took 3 hours, 89 took 14); SAT solvers were slower than enumeration (rule30_records_sat.py, S1 refuted), so no cheap step is open. Second triage (CL065, GC614.1): the closed methods are listed in §4, each scoped to its method. Open part: joint compatibility of late, restarting interior sources with the actual clock (GC598 to GC600). |

**Q7, as it stood before the third triage.**

| Lead | Status | What we have | What is left |
|---|---|---|---|
| Q7, the regime between | **PART** (kept at the second triage, 2026-10-08) | Kicks cannot thin out faster than geometrically (Theorem A). Excluded column 1s: every Sturmian one (Theorem E); arc codings for almost every rotation number (E″); near-squares at unbounded periods, including period-doubling, Chacon and substitution fixed points starting with a double letter (Corollary F, §8.59); Thue–Morse and paperfolding for every left edge up to 15,868 cells (A⁗); finite block codes of Sturmian words, one-orbit arc unions and single-character torus codes (G131, G132). The repeat-filter and compact-limit shortcuts are closed (G142 to G147), and the rooted edge tree and its reset costs are mapped (G149 to G163). Settling on a rooted history reduces to two gaps (G164, G165): **gap 1**, a stage budget $O(q)$ at each dyadic period $q$; **gap 2**, period growth, $R_j = N_j/2^j \to \infty$ (G184). Gap 1: the refinement loop is closed (CL011). Every compressed meter tried fails through false joins (G183, over G166 to G180), and RC2's exact finite certificate (budget 14 at $q = 8$, G182) barely compresses. Gap 2: open. The entries are $N_j$ = 3, 8, 29, 400, with $N_5 \ge 53{,}208$ (G2.3), and order recovery alone gives no stage bound (G185). Every step: PROOFS.md §E2 (G131 to G204, all second-read by Local); this cell's long form stands at commit 941e06a. For Thue–Morse and the recorded paperfolding repeats, G186 weakens gap 2 to unbounded $R_j$, equivalently unbounded normalized stage lengths $\lambda_j$, still conditional on the stage budget (second-read by Local, L151); actual growth remains open. G187 makes it quantitative: $\limsup R_j$ above a threshold tied to the budget constant suffices for both codes (above 17 at $\gamma = 5/2$ and $C = 1$, with the dyadic refinement; second-read by Local, L152). The record's $R_4 = 25$ and $R_5 \ge 87{,}867/32 \approx 2{,}746$ on every rooted history (TM5, L178: the whole-tree minimum of $N_5$ is the single cell's own 87,867) clear it; the rooted period-16 stage is finite, with 16 histories all entering period 32 by depth 894,235, so $R_5$ runs from $87{,}867/32$ to $894{,}235/32$ over them (TM5b, L179); and the whole-tree minimum of $N_6$ is 65,821,413, so $R_6 \ge 65{,}821{,}413/64$ on every rooted history (TM6, L180), which is finite evidence, not a recurrence. G188 excludes zero returns within eleven steps after doubling to period at least 4, a constant bound (second-read by Local, L153); an exploratory, unpreregistered census finds the earliest actual returns at 21, 88 and 6,343 for $q = 4, 8, 16$ (`rule30_g188_returns.py`). G189 adds a logarithmic delay bound for odd first returns only (second-read by Local, L154); even returns, which the rooted history itself makes at period 16, and normalized growth remain open. G190 retains complementary halves in an exact paired-window return criterion, populated by the actual returns at $q = 8$ ($r = 88$) and the rooted $q = 16$ ($r = 52{,}808$) (second-read by Local, L156); it gives no delay estimate or root reachability. Pending G191 characterizes persistence in each fixed even-return graph through its mutually reachable regions and cyclic classes, with a finite cutoff ($8n^2$); its Rule 30 continuation excludes invariant single cycles, so persistence needs internal recurrent branching (second-read by Local, L157). Local PR191-C1 completely constructs the six r4..14 graphs and reports all acyclic (L158); this excludes even returns through14 at every dyadic period, but is a finite six-graph result. G192 proves the $r = 8$ graph acyclic by hand, for any two words, matching that computation by a second route (second-read by Local, L159). G193 makes the edge condition depend on the target alone, prunes each graph to the targets of its edges, and records the swap as a parity on a two-sheet quotient (second-read by Local, L160). G194 decides each recurrent quotient component by two binary potentials and one gcd (second-read by Local, L161). G195 names a local certificate, a four-window parallel pair, which on a cycle defeats both potentials; it occurs at $m = 3$ and $m = 6$, transiently (second-read by Local, L162). G196 gives an exact diagonal test for branching, which is common (70 sources at $m = 6$) in graphs that are still acyclic (second-read by Local, L164). The rooted $q = 16$ cycle has two legal exits (PR196-D1, L165), and by G197 neither can rejoin it in fewer than 26,396 edges (second-read by Local, L166). G198 reduces persistence of a known cycle to one residue: a rejoining excursion with $\ell + s - u \ne 0 \pmod q$ (second-read by Local, L167). G199 shows that a dyadic repeated endpoint, even in the odd-doubling domain, need not be rooted (the $q = 8$, $r = 88$ witness is not), so ancestry must be kept explicitly (second-read by Local, L169). G200 makes each stage length the sum of its zero-return excursions; the period-16 stage already contains an internal branch, so it is strictly longer than 52,808 (second-read by Local, L170). G201 shows that the two children of a genuine branch are disjoint for one profile only (second-read by Local, L172). G202 shows that the overlaps along one excursion add up, odd or even, to the parity of the source it returns to, and exactly to that source's weight plus an even surplus; this bounds overlaps across a stage by $2k_j - 1$, which is not a length bound, and three parities of a pair do not predict the next (second-read by Local, L174). G203 adds an automatic baseline: every nonconstant excursion pays $q$ at its start and its source's weight at its end, plus $V(w)/2$ once it has six or more steps; equality on the rooted period-2 excursion shows there is no strict surplus, and the charge is in bit incidences, not normalized length (second-read by Local, L181). G204 shows, from those finite certificates, that the history first entering period 64 also has the shortest period-32 stage, $\min \lambda_5 = 65{,}154{,}361/32$, separated from every rival by at least 1,060,269 steps; the minimizing history changes from $j = 5$ to $j = 6$ (second-read by Local, L182). PR195-D0 finds no alternative edge on the fixed q8/r88 witness: its component is exactly its eight-cycle, q8 only (Local L163; GPT prediction refuted). PR196-D1 refutes outgoing isolation of the fixed rooted q16/r52808 circuit: legal alternatives occur at two unordered phases (Local L165; GPT prediction refuted). PR198-D2 finds both exit targets have no successor (Local L168; GPT prediction held), so the named rooted q16/r52808 component is exactly its sixteen-cycle, q16 only, despite its outgoing exits. Both named q8 and q16 components are now closed; this is finite evidence, not a general rigidity theorem. Other r88/r52808 components, larger graphs and normalized growth remain open. 2026-10-09 (GPT GC652, GC684, GC696, GC702; second-read by Local): a below-threshold next wait is a selected mismatch run, D(S) = 1 xor B(S-1) with delay r + 2, and the exact debt is sum(delay - 5/2) = R - N/2 - F (GC652); L224's 78.5 debt is repaid after 148 ordinary drivers (GC684, rebuilt by Local). At the mismatch endpoint the next fast arrival reads E(m+2) = A(m) (GC696), and inside the run X(t) = B(t) and not B(t+1) (GC702). The automatic long-run charge stalls: no rooted, length-weighted bound on A at the endpoints is known. | Thue–Morse and paperfolding for every left edge: one-phase adaptive waiting bound below slope 3 and sublinear period growth on every admissible branched left side (§8.59; GPT G2/G6). G6 proves worst phase is at most any chosen phase plus P−1, including births. Rudin–Shapiro (GPT G153 exact automaton candidate passes the repeat filter; RSP-S independently reconstructs its repeat language in a closed 17,033-state comparison; second-read by Local, L111). Arcs with unrelated ends when the partial quotients stay small, unless a circle covering makes them one orbit (G132). Rotations of a torus seen through more than one character (box codes). Kicked wheels. Second triage (CL065): affine waiting envelopes are closed as a method (GC596), listed in §4. |

### 8.79 The status board's history, archived at the fourth triage (2026-10-10)

*Moved verbatim from PERIOD-TWO.md §6 at the fourth board triage (Local, drafted in L517 at the CHAT-LEDGER.10 rotation, applied 2026-10-10 01:48 BST), so the board can say status, change and what is left in a few lines. Nothing was edited; each row is the text as it stood.*

*Correction (GPT's GC918 follow-up to L517).* The moved one-hole row's four-decimal ceilings 1.4712, 1.3839, 1.5994, 1.7144 (layer radii, p = 5, 6, 7, 9) and 1.5904, 1.6976 (products, p = 7, 9) were rounded down and are not upper bounds. The certified values, rounded up, are 1.220382, 1.231763, 1.471227, 1.383947, 1.599414, 1.714447 (p = 3, 4, 5, 6, 7, 9) and 1.461900, 1.590415, 1.697625 (p = 5, 7, 9); the board now says so.

**The two Condrey ends, as it stood before the fourth triage.**

| Lead | Status | What we have | What is left |
|---|---|---|---|
| The two Condrey ends (§8.62; the owner's question of 2026-10-06) | **PARKED** for the white end at q = 2 .. 9 and the black end at q = 2 .. 6 and 8, behind period 2 (q = 1 is the 0101 wall itself); black end **CLOSED** for q = 7 and every q >= 9 (PROOFS.md entry 38, third triage 2026-10-09); white end **CLOSED** for every q >= 10 (PROOFS.md entry 40, second-read by Cloud CL110, 2026-10-09) | The ladder by freedom named. Black end $0\,1^{p-1}$: exact records for $p = 3$ to $8$ to 32 free bits, LR holds, $R/d$ about 0.8 of the coin's $1/(p-1)$; GPT's §G11: the checkerboard survives one hole as a known prefix of $p-1$ cells and no further; no rays, chaos past the hole. G12: flipping a hole followed by four black cells changes only its own row's first three cells, with all-depth shielding beyond them; earlier inverse propagation stays open. G12.4 also certifies an eleven-cell first-bit effect for a specified p3 input prefix by terminal adjacent agreement. G13 gives an exact four-state inverse-row reset language and p>=8 one-step-back shielding beyond depth7; successive-row reset gaps remain unbounded. G13.5 iterates through r steps when p>=3r+5, shielding beyond4r+3; the protected window loses three cells per step, so later holes are not controlled all the way to time0. White end $0^{p-1}1$: the latch lemma (column 1 non-decreasing between the wall's black times), too weak alone; the statement there must be B. G14 sharpens the relaxed latch language with exact two-state full/visible matrices, crediting p2 Pell/Fibonacci; p8 visible bound0.35449 bits/step, still no cost theorem. G15 characterizes the width-one visible language by white gaps: one-hole p>=3 allows every hole-bit sequence in that relaxation; equal white density can have different local capacities. G16 proves the exact width-two one-hole language: even p forbids11, p3 forbids100, odd p>=5 is still full; the first two have rate log2(phi)/p. G17 proves width three has exactly the same visible language for every p, despite a period-four hidden black relation; odd-period restrictions require width>=4. G18 answers the slow-switch audit: a+1 exact finite prefixes from a latch position; checkerboard band4a..a+b-1 if b>=3a+1, even for nonperiodic preceding wall; phase corrected and complete one-parameter tail closure refuted. G19 gives a finite-window latch obstruction for0^5 1^5: left support>=7, versus arbitrary-input prefix minimum4; interior r3 defeats the endpoint shortcut. All-a balanced support and bounded debt remain open. G14's `rule30_gpt_white_latch.py` replicated by Local (2026-10-06, at ee23889; the p = 8 rates 0.377753926, 0.354491897, 0.396240625 to every digit). 2026-10-09 afternoon: black-end exclusions for finite seeds, certified by a finite strip graph plus Jen's theorem with a clock (entry 5): no finite nonzero seed has a column eventually reading 0 1^q for q = 7 or 9 <= q <= 16 (p = 8 and 10 .. 17). Method from the external repository cochon123/rule30-prize (pinned 3915b39; read, not run, by GPT in GC805); finite cases reproduced independently by Local's `rule30_isolated_zero_strip.py` (SG, L429), with q = 1 .. 6 and 8 failing as controls. Post hoc the same single-component shape holds to q = 40. The repository's uniform proof had a gap (GC805); GPT's GC806 repairs it (a nine-update forcing lemma, second-read by Local in L430), and Local's finite wrap table (`rule30_isolated_zero_wrap.py`, WT, L431: only prefix 110001101 reaches the cruise set C) completes it for every q >= 17. So the black-end walls 0 1^q are excluded for finite seeds at q = 7 and every q >= 9 (p = 8 and every p >= 10; PROOFS.md entry 38, filed 2026-10-09); open in the family: q = 1 .. 6 and 8 (p = 2 .. 7 and 9). Wider strips (radius 7 and 8, Local's SGW, L433) certify none of these. Ring orbits with a column reading exactly 0 1^q exist for q = 1, 2, 3, 4, 6 (rings of 7, 12, 7, 15, 15 cells), none found for q = 5, 7, 8 up to 22 cells. **2026-10-09 evening (Local, WE):** the strip test at radius 6 fails for every white-end wall 1 0^q, q = 1 .. 16. Its non-forcing components grow linearly in q with a period-4 pattern, so the black end's lock has no white-end analogue here. RG adds that the black end's open q = 2 .. 5 fail to radius 9. **WJ (late evening, Local; second-read by Cloud CL110; filed as entry 40):** the white end 1 0^q is excluded for finite seeds for every q >= 10. The one-sided width-8 relaxation forces column +1 eventually periodic, reading 1 0 0 1^(q-2); W^(n+4) = W^n from n = 22 covers all q; and Theorem A finishes it. The same route reproves the black end for q >= 14 (L497). SGC (the strip test in C): every open case, white end q = 2 .. 9 and black end q = 2 .. 6 and 8, still fails at radius 10 and 11, with exactly one non-forcing component that persists from radius 6. | A cost for the second defect after the protected prefix (GPT's next target); whether anything at either end escapes the positive-entropy gap. |

**The one-hole channel layers, as it stood before the fourth triage.**

| Lead | Status | What we have | What is left |
|---|---|---|---|
| The one-hole channel layers (GPT G15-G17/G20; CONSTELLATION row16) | **PARKED**, other walls, behind period 2 (first triage of 2026-10-06, CL009 and GC155; was: **PART**, GPT reasoning) | Width one is fully free at p>=3; widths two/three restrict even p and p3 but allow all odd p>=5. G20 proves width four still allows every hole-bit sequence at every odd p>=5, by B^8=B^16 and six exact subset certificates; blind first-restriction prediction refuted. G15's `rule30_gpt_gap_language.py` replicated by Local (2026-10-06, at ee23889; all controls as recorded). **2026-10-09 (Local, OH, a drawn row):** the first restrictive width is attained. For every odd p >= 11, width 5 forces the hole bit to 0 after the first hole; the language is 0^n and 1 0^(n-1), with the same language at widths 5 .. 10. p = 5 and 7 are first restricted at width 7, and p = 9 at width 8. All three keep positive entropy at width 10 (growth 1.73, 1.88, 1.87). The results come from exhaustive automata, with every odd p covered through the eventual period of the black relation, and the key word was brute-forced independently. Seed-free and one-sided; for finite seeds, entry 38 already excludes p = 8 and p >= 10, and the surviving odd periods are exactly its open q = 4, 6, 8. Widening to width 13: p = 5, 7, 9 keep positive entropy but keep narrowing (at width 13 the growth is 1.6725, 1.7882, 1.8537); none closes by width 13. **Later the same evening (OHC in C, OHD direct simulation):** to width 22, p = 5, 7, 9 still narrow and none closes (growth 1.4712, 1.5994, 1.7144 at width 22). By compactness the true one-sided entropy is the limit of these upper bounds. Exact forms hold at the plateaus: x^4-2x^3+x-1 (p = 9, widths 8 .. 12) and x^5-x^4-x^3-x^2-x+1 (p = 7, widths 7 .. 9). Plain forward simulation agrees with the automata, and for p = 5 the hole word 10000 is forbidden in the true half-line system. GC850 (G.GPT271) gives the hand reason for p >= 10: nine black steps lock the pair 01. **TB (late evening):** p = 8 also closes at width 5 (hole words 0^n, 1 0^(n-1), 0 1 0^(n-2); confirmed in the true system). p = 3, 4, 6 stay open at width 22 (certified ceilings 1.302, 1.291, 1.407). So the one-sided channel is closed exactly at p = 8 and p >= 10, which is entry 38's exclusion set, and open at p = 2 .. 7 and 9, its open cases. **LP (Local, 2026-10-09 late evening):** the width-22 automata's radii, certified in integers and verified independently, replace the c_60 ceilings: p = 3, 4, 5, 6, 7, 9 <= 1.2204, 1.2318, 1.4712, 1.3839, 1.5994, 1.7144. Times Cloud's true forbidden words (TC), p = 5, 7, 9 <= 1.4619, 1.5904, 1.6976 a hole, below both factors (L506). | Does the one-sided entropy of p = 5, 7, 9 reach zero? The upper bounds fall about 0.015 per width at 22, so a lower bound (a construction realising exponentially many hole words) or a lock argument for shorter black runs is needed; more width alone will not decide it. p = 3 and the even periods are separate. |


### 8.80 The pattern as one chain, and the chain split at the front (the owner's lead, 2026-10-10)

*Cloud, from the owner's questions of 2026-10-10: read the single cell's pattern not as rows and columns but as one
long binary chain, the rows concatenated; then split that chain at the orderly wave front into an orderly chain and a
random chain, "like a complex number". Probe `rule30_cloud_chains.py`; predictions CH-P0 .. CH-P4 pushed before the
run; chat CL211, CL212. A side question (CONSTELLATION.md F); it serves no status-board row directly.*

**What is exact.** Read row $t$ from the left edge; cell $e$ of row $t$ sits at chain position $t^2 + t + e - t$, that
is cell $i$ (absolute) at $t^2 + t + i$. Row starts are the squares, the centre column is the pronic numbers $t(t+1)$,
and the rule becomes one recurrence with a growing lag,
$a_p = a_{p-2t-1} \oplus (a_{p-2t} \lor a_{p-2t+1})$ with $t = \lfloor \sqrt p \rfloor$, except at the two cells
at each end of a row, where a lagged term falls outside the previous row and reads 0. So the chain is a nonlinear
shift register whose tap distance grows like $2\sqrt p$; on a finite ring the lag is fixed and the sequence periodic,
here it never is. The first $e$ diagonals are a closed system (§8.31), so the orderly chain (each row's first $B(t)$
bits, $B$ the exact boundary of §8.74) is autonomous, and the random chain (the rest) is driven by it at its left
boundary and never feeds back: a clock driving a register, not two independent coordinates. The centre column lies
in the random chain at offset $t - B(t) \approx 0.25t$ from the front, which never returns to it (§8.74). Rows 1 to 4
of either chain determine row 5 of the orderly chain; row 5 of the random chain needs its own past as well.

**What was measured** (rows 2 to 4,096, $P = 2^{10}$; chains F full, O orderly, C random, I an i.i.d. coin of C's
length; N the 64 bits after $B(t)$, M the 64 bits about the centre column):

| chain | bits | xz ratio | zlib ratio | density | $h_{16}$ bits per bit |
|---|---|---|---|---|---|
| F | 16,785,405 | 0.633 | 0.629 | 0.5008 | 0.912 |
| O | 6,436,255 | 0.077 | 0.366 | 0.5018 | 0.422 |
| C | 10,349,150 | 1.0001 | 1.0003 | 0.5002 | 0.9975 |
| I | 10,349,150 | 1.0001 | 1.0003 | 0.4999 | 0.9977 |
| N | 260,338 | 1.0019 | 1.0005 | 0.5011 | 0.899 |
| M | 261,180 | 1.0018 | 1.0005 | 0.5007 | 0.899 |

CH-P0 to CH-P3 HELD: the orderly share is 0.383; the orderly chain compresses thirteen-fold under xz while its short
blocks are coin-like ($h_8 = 0.996$), so its order lives in long repeats, as the stripes' periods say it must; the
random chain matches the coin in compression, 16-block entropy, density and the run law (every run frequency for
$L \le 10$ within 3.8% of $2^{-L}$). CH-P4, the unexpected check, REFUTED: the band just past $B(t)$ is as
incompressible as the centre, so there is no zone of slow order beyond the exact boundary that a compressor can see;
the front is sharp in this sense as well, consistent with §8.74's lag-$2P$ control.

**What it means.** The owner's split does exactly what the picture says: it separates a zero-entropy clock from a
register that passes every coin test used here. It does not reduce the problem: the register's width grows without
bound, which is the one thing that lets a system driven by periodic clocks avoid eventual periodicity. The chains
carry no structure that the two-dimensional form hides. **Prior work.** No chain or row-major reading was found in the
record or in the literature read for PRIOR-ART.md; the row-by-row reading is OEIS A070950 as a triangle, without
results on the concatenation.


### 8.81 The triangle law integrates to one half; the white area of each side, split at the front (the owner's lead, 2026-10-10)

*Cloud, from the owner's question of 2026-10-10: would adding up the area of the white triangles on the orderly and
the random side, not just their number, reveal anything? Probe `rule30_cloud_triangles.py`, predictions TA-P0 .. TA-P3
pushed before the run; a side question (CONSTELLATION.md F).*

**An identity (PROVED by hand).** Every white triangle is exact (§8.18), so a top of width $L$ colours
$A(L)$ cells, $A(2m-1) = m^2$ and $A(2m) = m(m+1)$, and every white cell lies in exactly one triangle. Under the
uniform measure the tops of width $L$ have density $3 \cdot 2^{-(L+4)}$ per cell (§8.68). With
$\sum_{m \ge 1} m 4^{-m} = 4/9$ and $\sum_{m \ge 1} m^2 4^{-m} = 20/27$,
```math
\sum_{L \ge 1} 3 \cdot 2^{-(L+4)} A(L) = \tfrac{3}{16}\Big(3 \cdot \tfrac{20}{27} + \tfrac{4}{9}\Big)
= \tfrac{3}{16} \cdot \tfrac{72}{27} = \tfrac12 ,
```
the measure's white density. The triangle law and the half-density are one fact seen twice; so the summed area of a
side says nothing, and the content is the share by width: $3/32$ of all cells for each of $L = 1, 2, 3$, then halving,
with widths 8 and up holding about 3.6% of the cells (7% of the white).

**Measured** (rows 2 to 4,096; sides split at §8.74's exact front $B(t)$):

| side | cells | white | triangle area | largest top | white in widths $\le 8$ |
|---|---|---|---|---|---|
| orderly ($e < B(t)$) | 6,436,261 | 0.4982 | 0.4979 | 16 | 95.7% |
| random ($e \ge B(t)$) | 10,349,144 | 0.4998 | 0.4996 | 33 | 92.5% |

TA-P0 to TA-P3 HELD. The random side's area shares match the law within 1.5% for every width to 11 (and its largest top,
33 on the right edge, is §8.68's $\log_2 t + 22$). The orderly band's largest top is 16, its period (§8.68 saw the
same in $x/t < -0.6$), and its census beyond width 8 is the stripes', not geometric: 2,233 tops of width 10 against
1,275 of width 9, 429 of width 12 against 113 of width 11, none of 13 or 14, then 180 of 15 and 63 of 16. One nuance:
in the first 32 diagonals past $B(t)$ the births of widths 1, 2, 3 and 6 run 2% to 9% below the law, and sit at
1.00 beyond; so the front has a faint graded edge in triangle births that the chains probe's compressors could not
see (CH-P4). **What it means.** Both sides are half white; the owner's eye is right that the random side has the
large triangles (one of width 33 against the band's 16), but they hold a few percent of the area: most white, on both
sides, is specks of width 1 to 3. **Prior work.** §8.68 counted tops by width and by $x/t$; the areas, the identity
and the split at $B(t)$ are new to the record.


### 8.82 The two wall phases' records are coupled exactly through black runs (swarm lane q2, graded; 2026-10-10)

*The owner-authorized question swarm: five independent agents (no access to the record), each with a self-contained
brief, each to be followed by a skeptic. Lane q2 was given the black-even phase (wall black at even times): parity,
the shrink inequalities, R°(d) as far as feasible, and why its constant differs. Graded by Cloud as below; the swarm's
own skeptic is still queued. Code and raw outputs are outside git. Nothing here is a bound for all depths.*

**What the lane proved, and Cloud verified independently.**
- *Lemma (what lies above a zero run).* Let $y = F(x)$ be one forward step of a left row beside the wall (any wall
  colour). Then $y$ is zero on depths $[d, e-1]$ if and only if $x$ is zero on $[d-1, e]$, or $x$ is one on $[d, e]$,
  or $x$ reads 1 at $d-1$, 0 at $d$ and ones on $[d+1, e]$. (Proof: $y(k) = 0$ means $x(k+1) = x(k) \lor x(k-1)$, a
  recurrence that the pair $(x(d-1), x(d))$ drives to one of the three shapes.) Cloud: exhaustive over all 12-cell
  rows, both walls, all $d < e$: 450,560 cases, no violation.
- *Time shift.* The black-even time-0 row of a visible sequence $w$ is $F_0$ of the standard row of $u.w$ (any $u$),
  and the standard row of $w$ is $F_1$ of the black-even row of $w$: the two phases are one evolution one step apart.
  Cloud: 100 random sequences, depths to 18, no mismatch.
- *Parity.* Every finite black-even record ends at an odd depth, every standard one at an even depth (flip the last
  free bit to extend otherwise). GPT's GC1043 and Cloud's own computation agree.
- *Sandwich, stronger than asked.* $R^{\circ}(d+1) \ge R(d) - 2$ and $R(d+1) \ge R^{\circ}(d) - 2$, so
  $R(d-1) - 2 \le R^{\circ}(d) \le R(d+1) + 2$; both ends are attained. Cloud: holds on the full tables, $d = 2$ to 60.
- *The exact coupling.* Write $E = d + R$, $E^{\circ} = d + R^{\circ}$ for the end depths, $Q_P(d)$ for the end of the
  longest run of ones from depth $d$ in phase $P$, and $P_P(d)$ for the end of the longest 1, 0, 1, 1, … pattern begun
  at depth $d-1$. Then for $d \ge 2$
  ```math
  E^{\circ}(d) = \max\big(d,\; E(d-1) - 1,\; Q_S(d) - 1,\; P_S(d) - 1\big), \qquad
  E(d) = \max\big(d,\; E^{\circ}(d-1) - 1,\; Q_B(d) - 1,\; P_B(d) - 1\big).
  ```
  So each phase's zero records are the other phase's zero records and **black-run** records, shifted by one. Cloud:
  both identities by brute force for $d = 2$ to 8 in both phases; the lane checked them to 52.
- *The constants are tied.* With $\beta_P$ the largest excess of a black-run birth over $2d$, the lane derives
  $c^{\circ} = \max(\beta_S, \beta_B - 3)$ and $c = \max(\beta_B, \beta_S - 3)$ for the least constants with
  $R^{\circ} \le d + c^{\circ}$ and $R \le d + c$ on any finite range, so $|c^{\circ} - c| \le 3$; and
  $R(d) \le d + 4$ for all $d$ would give $R^{\circ}(d) \le d + 7$ for all $d$, sharp at $d = 12$.
- *The chain behind both peaks.* The standard row of $u.w$, $w = 1001011011010110010$, reads 1 at depth 11, 0 at 12
  and **nineteen ones** on 13 to 31; one step gives the black-even zero run 12 to 30 ($R^{\circ}(12) = 19 = d + 7$),
  one more the standard zero run 13 to 29 ($R(13) = 17 = d + 4$). Cloud reproduced all three rows. The two record
  peaks of the two phases are one black run seen twice.

**What the lane computed (third-party; three agreeing methods; Cloud-verified to depth 14 by brute force).**
$R^\circ(1..62)$ = 0, 1, 4, 3, 2, 3, 4, 5, 4, 9, 8, 19, 18, 17, 18, 17, 16, 15, 14, 19, 18, 17, 18, 17, 18, 19, 18, 21,
20, 19, 22, 35, 34, 33, 32, 31, 30, 29, 34, 35, 36, 37, 36, 35, 34, 41, 40, 39, 38, 37, 42, 45, 44, 43, 42, 43, 44, 53,
52, 51, 54, 53. The largest excess is 7, at $d = 12$ only; $\beta_S = 7$ (from $P_S(12) = 32$) and $\beta_B = 4$ on
$d \le 52$. A merging census gives about 1.77 distinct future states per free bit (0.82 effective bits), the same
mechanism §8.38 measured for the standard phase.

**What it does not give.** No bound for all $d$ in either phase; why $\beta_S > \beta_B$ (the lane traces black runs to
period-3 patterns one phase over, and the hierarchy does not close); whether the extremal excesses are attained at
small depth. **Where it bears.** Question D of KIMI-QUESTIONS-3.md is answered in the strong form; §8.39's doubling
conjecture now has a companion statement for the other phase with constant 7, and the black-run records $Q$, $P$ are
the new objects to study: the standard phase's $R(d) \le d + 4$ is, by the coupling, a statement about how long a
black run can live one step earlier.

*Skeptic's verdict (the swarm's own, graded by Cloud, 21:22 BST): no claim refuted; every proof above holds as written;
the upper bounds in $R^\circ(45..62)$ rest on the lane's engine (the skeptic certified the lower bounds by completing
every witness); "the exact relation must include black-run records" is an overclaim, since only specific forms were
refuted. Its unexpected check: $E^\circ(d) = \max(d, T_S(d))$ for every $d \le 38$, so the shrinking-zero-run term of
the coupling is first needed at $d = 41$; in the standard phase first at $d = 29$.*


### 8.83 Every minimal absent word to length 48 is excluded by a strip no wider than itself; the trace form is tight (swarm lane q3, graded; 2026-10-10)

*Lane q3 of the owner-authorized swarm (independent agent, no access to the record) was given the right-half language
beside the wall, its minimal absent words, and the half-width question of CL210. Graded by Cloud 21:22 BST; skeptic
graded 23:16 BST. Code and raw outputs outside git.*

**Proved by the lane and verified by Cloud.** The one-sided reduction (any right half beside the wall extends to a
configuration on $\mathbb Z$, so $L$ is the right halves' visible language; §8.39's mirror). The **000 rule**: at even
$t$, $x_{t+2}(1) = 1$ exactly when $x_t(1..3) = 000$, so a visible 1 is always followed by a visible 0 and 11 is
absent with $w_{\min} = 1$ (Cloud: all 1,024 rows of width 10). The strip languages are nested,
$L \subseteq L^{W+1} \subseteq L^W$, and the width-$(2m-2)$ strip is exact for words of length $m$, one better than the cone, so
$w_{\min}(f) \le 2|f| - 2$. If $g$ occurs in $f$ then $w_{\min}(f) \le w_{\min}(g)$, so any linear bound need only be
proved for minimal absent words; the same reduction holds for full column-1 traces (all times, not only even ones).
The **front lemma**: two histories that first differ at site $\ell$ differ at site $\ell - 1$ a step later only if
the cell there was white, so an exterior bit walks left one site per zero. Cloud's own brute force reproduces
$|L_n|$ for $n \le 10$ and the seven minimal absent words to length 10 (11, 00000, 101001, 0100101, 010010001,
0101000101, 0101010000), and $w_{\min} = 1, 4, 6, 5$ for the first four by set propagation.

**Computed by the lane (third-party; its $|L_n|$ agree with §8.20's TC2 at every $n \le 39$).** $|L_n|$ to $n = 48$
($|L_{48}| = 32{,}656$). The minimal absent words to length 48: 1,612 of them, counts per length rising from 1 at 2,
5, 6, 7, 9 to 132 at 48. **Every one has $w_{\min}(f) \le |f|$**, with equality only for 101001 and one word of
length 31; the ratio runs from 0.294 to 1.000 with median 0.595 (L606's learned cuts sat at 0.535). Cross-checked by
set propagation for 251 of them with $w_{\min} \le 26$; the rest by SAT without proof logs. The **trace form** is
sharper: for full column-1 traces of length $l \le 84$ (938 minimal absent traces) $w_{\min} \le \lceil l/2 \rceil$,
with equality only at $l = 7, 11, 35, 61$; and the width-$W$ strip generates exactly the real traces of length
$2W - 1$ for every $W \le 12$ (exhaustive). **The light cone is not the mechanism**: the earliest time an exterior
change can reach column 1 is $\tau(W) = W$ for every even $W \le 28$ (a zero anti-diagonal lane of length $W$ carries
it at full speed; the longest such lane ending at column 1 is 28, exhaustively), $W + 1$ for odd $5 \le W \le 27$,
and only $W + 4$ or $W + 5$ for $29 \le W \le 40$. So the claim "an exterior bit cannot arrive before $s + 2W$" is
REFUTED, and influence arguments alone cannot give any constant below 2.

**What it means.** CL210(a), that half the trivial width always suffices, now holds for every absent word to length
48, minimal or not, and the sharper statement to aim at is the trace form: *the free-exterior strip of width
$\lceil l/2 \rceil$ is exact for column-1 traces of length $l$*, tight at four lengths so far. The quarter seen in
L606 is the typical case of a law whose worst case is exactly one half. Nothing here is proved for all lengths; the
lane's best proved bound is $2|f| - 2$. **Prior work.** §8.20 (TC2: $|L_n|$ to 39, the minimal forbidden words, the
entropy ceiling), SW (L569, L570: strip widths for minimal words to width 35), L606 (77 learned cuts). New to the
record: the complete $w_{\min}$ census to length 48, the trace form and its tightness, $\tau(W)$ and the 28-lane.

**Skeptic's verdict (independent agent, Cloud-checked, 23:16 BST).** Every proved claim (the reduction, the 000 rule,
nesting and exactness at width $2m-2$, the factor reduction, the trace reduction, the front lemma, the sticky carry)
was checked line by line and found correct, with only informal wording to object to. The computations were re-derived
rather than trusted: $|L_n|$ to 15 by its own brute force, every $L_n$ to 48 and every trace language to $l = 84$ by
an inductive candidate-partition audit with re-simulated witnesses, and all 1,612 values of $w_{\min}$ by two methods
of its own, an exact SAT-free backward preimage propagation for the 1,260 words with $w_{\min} \le 27$ and its own CNF
whose unsatisfiable cores carry RUP-checked proofs; the zero-lane counts, $\tau(W)$ to 32, the emulation failures and
the front speeds were reproduced by different code. **One statement refuted, and the text above is corrected by it**:
the trace form is tight not only at $l = 7, 11, 35, 61$ but also at $l = 2$ (10, width 1), $l = 4$ (0000 and 0101,
width 2) and $l = 36$ (a length-36 trace with width 18); the lane's summary tested $2w \ge l+1$ and so missed every
even length, and its own trace file lists all seven (Cloud read the file). So the trace form is critical at both
parities, which matters for any proof attempt. Gaps named: ingredient (iii) of the mechanism story is asserted, not
proved; the chaining of fast lanes behind $\tau(W) = W + o(W)$ is not shown, and $\tau$ is confirmed only to 32; the
slope profiles were not rechecked. Nothing beyond $w_{\min} \le 2|f| - 2$ is proved for all lengths, as the lane said.


**Correction and extension (IN010, Intel, 2026-10-11 15:18 BST; recorded by Cloud 15:30 BST).** The tight lengths of the
per-trace form in the standard phase, to length 90, are 2, 4, 7, 11, 35, 36 and 61 (the words 10; 0000 and 0101; and
010001001100010011000100110001001100 at 36 join the list above), and in the odd phase 2, 3, 8, 12, 15, 20, 34, 36, 38
and 62; the odd tight traces of lengths 36 and 62 are 1 and 0 followed by the standard ones of lengths 35 and 61.
Conjecture S holds at every W <= 39 in both phases: standard L(W) for W = 18..39 is 40 42 42 49 52 52 54 56 56 59 60 60
60 72 72 74 76 80 84 84 84 84, odd L(W) for W = 19..39 is 43 43 46 46 53 53 57 57 58 61 61 61 71 71 73 73 73 81 81 81
81, both at least 90 from W = 40 (SAT without proof logs, two engines, controls against the exhaustive counts; the
standard slack falls to 1 at W = 30, zero slack in the odd phase only at W = 12 and 15).
*(comb note, 2026-10-14, Local, SW-01: SX-P11, published in IN011, supplies drat-trim-verified DRAT proofs for this
census, COMPUTED single-party, rule30_intel_strip_threshold.py. The caveat stays until an independent check and a
second read, per IN011.)*

### 8.84 The free record to depth 73, the (10)^k family bounded, and a Jen-type theorem for finite patterns (swarm lane q1, graded; 2026-10-10)

*Lane q1 of the owner-authorized swarm (independent agent, no access to the record; briefed with R(1..61) and
S(0..17) only) was given the wall-form bound: prove C1, C2, then bound the survival T(w) of every finite pattern.
Graded by Cloud 21:35 BST; its skeptic is running. Code and raw outputs outside git.*

**Proved by the lane and verified by Cloud.** C1 and C2 (§8.39's wall form, now with the extended sense: $R(d)$ is
infinite iff $S(d-1)$ is). The light cone and left-permutivity: $x_t(-1) = y_{t+1} \oplus h_t(y_1 .. y_t)$. The
**consistency count**: exactly $2^{\lceil n/2 \rceil}$ patterns of $n$ cells survive to time $n$ (Cloud: all $n \le 20$
by own code), so $S(n) \ge n$ and $S$ is nondecreasing. The **edge and diagonal** structure: the deepest black cell
recedes one site per step, the diagonals from it obey a triangular recurrence and are eventually periodic with
power-of-two periods (§8.59's Jen lemmas in the wall form). A **Jen-type theorem** (hand proof, checked line by
line by Cloud): for a nonzero finite pattern beside any eventually periodic wall, no column of the forward evolution
is eventually periodic; so a pattern surviving for ever would have an aperiodic visible sequence, which is #14's
fact (Jen settles every periodic column 1) reached from the other side. The **barrier lemma**: a spatial 10-domain
from depth $D$ on is invariant whatever happens nearer the wall (Cloud: 300 random trials, no violation), so the
cells nearer the wall form a finite system. The **front lemma** for patterns $u(10)^k 0^\infty$. And by hand
$T((10)^k) = 2k + 1$ for every even $k$ (Cloud: $k \le 24$, with $c_k = 5, 3, 5, 3, 13, 3, 13, 3, \dots$ at odd $k$).

**Computer-assisted by the lane (not rerun by Cloud).** $T((10)^k) = 2k + c_k$ with $c_k$ periodic in $k$ modulo 2048
and at most 31; for every $u$ with $|u| \le 16$ and every $k$, $T(u(10)^k) \le |u| + 2k + 31$ (57 of the 131,071 words
$u$ have $u(10)^\infty$ surviving for ever, all with a period-2 orbit next to the wall); for $|u|, |v| \le 8$,
260,728 of 261,121 families $u(10)^k v$ resolved with excess at most 32; every pattern with at most five black
cells has $T(w) \le S(66) = 121$ (an effective-prefix lemma and the chain $0 \to 2 \to 8 \to 18 \to 34 \to 66 \to 122$).
The first infinite family of patterns with a proved bounded excess.

**Computed.** $S(0..72)$ exactly, by a depth-first search over consistent prefixes in C (48 chunks), three
implementations agreeing to $N = 40$ and every stored maximiser re-simulated. Hence $R(1..73)$: it equals the
record's values at every $d \le 61$ **and at 65, 69 and 73 (57, 55, 59), which the lane was not given**; new to the
record are $R(62..64) = 52, 51, 50$; $R(66..68) = 56, 55, 54$; $R(70..72) = 56, 59, 60$. $R(d) \le d + 4$ holds at all
of them, with equality still only at 2 and 13. Cloud reproduced $S(0..20)$ by own code. Bulk survival per odd step is
$0.500 \pm 0.003$; distinct configurations grow like $2^{0.415 n}$ against $2^{n/2}$ prefixes (§8.38's merging).

**Refuted as a route.** Survival after the leftmost cell's influence reaches the wall is not bounded: 58 at $n = 64$,
61 at $n = 71$, growing like $0.85n$. **Not proved.** Finiteness of $T(w)$ or any $F(n)$ in general; $S(n) \le 2n + 5$
is verified to 72 only. The lane says where each attempt broke: no finite-state reduction for a pigeonhole; survival
involves wall-born diagonals at age one, before any periodicity; the barrier works only behind a 10-domain.

**Where it bears.** The doubling conjecture is now checked to $d = 73$ with no gaps; Local's `records.c` can replay the
nine new values cheaply if it wishes; and the $(10)^k$ family is the first place a bounded excess is proved rather
than observed, by the barrier-and-front mechanism, which is the structural statement to try to generalise.

*Skeptic's verdict (21:57 BST): every proof holds; its own depth-first search reproduces $S(0..56)$ and the full
survival histograms, and all 596 stored maximisers to 72 re-simulate; the $u(10)^k v$ certification was read but not
rerun end to end (a gap, not a refutation); the per-step survival ratios at $m = 56$ stray to $0.494 .. 0.506$.*


### 8.85 The 1100 wall to depth 100: the record stays small, the lock structure of column 1, no proof (swarm lane q4, graded; 2026-10-10)

*Lane q4 (independent agent) was given the period-4 wall 1100 and its four rotations, with the record $R'(3..22)$ from
KIMI-QUESTIONS-2.md as calibration. Graded by Cloud 21:57 BST; skeptic graded 22:34 BST. Prior work in the record: the
three games of §8.40 for words to period 4, the parked Condrey ends, and Cloud's SAT values to 22.*

**Computed.** $R'(3..22)$ reproduced exactly by three methods (a C depth-first search, a numpy brute force, its own SAT
encoding); then $R'(1..100)$ exactly: 6, 5, 7, 6, 5, 6, 6, 5, 4, 6, 5, 5, 6, 7, 6, 5, 6, 7, 11, 10, 9, 8, 7, 8, 7, 6, 7,
6, 9, 8, 11, 10, 9, 8, 7, 14, 13, 12, 11, 10, 9, 10, 9, 8, 7, 6, 11, 12, 11, 12, 11, 10, 10, 9, 10, 9, 10, 12, 11, 10,
10, 12, 11, 10, 9, 11, 10, 12, 12, 11, 11, 11, 10, 12, 11, 11, 13, 12, 12, 11, 10, 9, 11, 10, 15, 14, 14, 13, 12, 15,
15,
14, 13, 12, 11, 13, 13, 12, 18, 17: the maximum to depth 100 is 18, at 99. Cloud: $R'(1..5)$ by own brute force agrees.
So (PROVED from the computation and a monotonicity lemma) **no configuration that is zero on all of $i \le -100$ at
time 0 keeps any rotation of 1100 at column 0 for ever**: the period-4 word is settled for every left-finite
configuration whose leftmost 1 lies within 99 sites of the centre when its periodic phase begins. This is the
period-4 twin of the real record's finiteness, checked to depth 100 as $R_{\mathrm{real}}$ is to 124.

**Proved (hand, Cloud-checked).** The lifetime form $R'(d) = T(d) - d + 1$ and $R'(d+1) \ge R'(d) - 1$. The warm-ups:
the black wall pins the left half to a time-constant spatial 0101 pattern (record at most 1); the white wall admits
only the zero configuration with column 1 identically zero. The **two locks**: during 11 a visible 1 is followed by a
0, during 00 by a 1; and the **lock lemma**: once $a(t_0) = 1$ at the second white tick, column 1 is locked into
4-blocks $(1, 0, p_k, 1)$ for ever, one free bit per block (Cloud: 5,403 block checks on random right halves, no
violation). A **structure theorem**: column 1 is $(0100)^K$, one of four transition blocks, then the locked blocks;
column $-1$ follows; columns $-1$ to $-5$ are affine in the free bits $p$, and from $-6$ on they are not. The free
sequence $p$ never contains an isolated 1 (a hand proof through column 3). A configuration vanishing on a left half
and keeping the wall for ever would have aperiodic $(\text{column }0, \text{column }-1)$ and finite $K$.

**Measured and refuted.** The locks alone do not bound the runs: the model that keeps only the proved lock structure
has longer runs than the real ones from depth 14 (19 against 11 at depth 21). The realisable $p$-sequences have small
positive entropy (about 0.4 bit per block), so eventual periodicity cannot be forced from the right side alone.
**Not proved.** $R'(d)$ finite for every $d$; conjectured, with the counting heuristic that four constraints per block
against 0.4 free bits make long survival exponentially rare. The lane's next step, a renormalisation of column 2
against the 1001/1011 blocks of column 1, is the one structural lead it offers.

**Skeptic's verdict (independent agent, Cloud-checked, 22:34 BST).** Every computed value it could reach was
reproduced by a different method: a forward-simulation lifetime search gives all 104 per-rotation values to depth 26;
its own forward light-cone SAT encoding, with two other solvers, confirms $R'(100) = 17$ (unsatisfiable at $T = 117$
for all four rotations) and spot values at depths 29, 36, 50, 77, 85 and 99; the lifetime lemma, the warm-ups, the
locks, the lock lemma, the structure theorem, the closed forms and the forbidden word 010 hold line by line, the last
three also under exhaustion of every length-28 column-1 trace. Two statements refuted. The per-rotation values at
depth 100 quoted in the lane's argument (13, 13, 12, 17) are not what its own file holds (17, 16, 13, 11; the maximum
17 stands; Cloud read the file). And 'the trace enumeration matches the structure theorem exactly' is false in a
useful direction: the transition block after $(0100)^K$ is 0101 only for $K \le 1$, 1011 only for $K \le 2$, and
always 0001 for $K = 3$ to 6 (Cloud recomputed this from the lane's trace file), a sharper structure than the theorem
states and a candidate for a hand proof. Gaps: 'no linear-algebra shortcut', 'the locks do not bound the runs',
'positive entropy' and 'not of finite type' are heuristics from at most ten data points, not theorems; the bound
$K \le (d+1)/4$ shifts by up to 3 for rotations other than 0; one lane script prints wrong zero-run maxima for the
periodic left halves through a period-concatenation bug while the report quotes the right values. The values at depths
30 to 98, other than the spot checks, rest on the lane's solver alone.


### 8.86 Is the right-half language sofic? Evidence against, a certified entropy ceiling, and a death criterion (swarm lane q5, graded; 2026-10-10)

*Lane q5 (independent agent) was asked whether the visible language $L$ of right halves beside the wall is sofic.
Graded by Cloud 21:57 BST; skeptic graded 22:34 BST. Prior work: §8.20's TC2 ($|L_n|$ to 39, the minimal forbidden
words, a certified entropy ceiling from the Aho-Corasick automaton), SLC's entropy.*

**Proved and Cloud-verified.** $L$ is factorial and right-extendable but not left-extendable (suffixes of $L_n$ fall
inside $L_{n-1}$ strictly from $n = 7$, by exhaustion); 11 and 00000 are absent, the latter by a hand proof through
column 5, so every word of $L$ is 1s separated by gaps of 1 to 4 zeros; the right half $(1001100)^\infty$ is periodic
in space and time beside the wall and reads $1010\ldots$ (the record's eternal train from another seed; Cloud
re-simulated it); a ring search to period 18 finds no other space-time-periodic right half. Regularity criteria: $L$ is
regular iff it has finitely many follower sets (Myhill-Nerode, with suffix closure), and (**the death criterion**,
PROVED) if $L$ is regular then the sets $L^{(j)}$ of words still occurring from visible time $j$ on are eventually
constant in $j$. Cloud reproduced $|L_n|$ to 10, the follower-set counts to $n = 8$, and the de Bruijn bound's trend.

**Computed.** $|L_n|$ to 26 (equal to TC2's); minimal absent words at every length from 9 to 26, counts rising to 20
at 26; a **certified entropy ceiling** $h \le \log_2 1.192197 = 0.2536$ bits per visible symbol from the de Bruijn
graph at $m = 26$ (exact rational Collatz-Wielandt), weaker than §8.20's layer bound but by a different route, with the
4-step growth rates still falling (0.2505 at 26) so that $h$ between 0.10 and 0.18 is the extrapolation and $h = 0$ is
not excluded. **Lower bounds on any finite description**: a DFA for $L$ needs at least 259 states, for its reversal 160,
and any labelled graph presenting $L$ at least 51 vertices (a verified fooling set); these grew 197, 228, 259 as the
horizon went 24, 25, 26 with no plateau. The distinct follower sets $F_3$ and $F_4$ over $L_n$ keep growing to $n = 23$;
no bounded suffix determines the follower set (the first symbol of a length-23 word still matters); horizon-$K$
classes form no consistent automaton for any $K \le 10$. Words die at visible times 0 to 16, none of length at most
12 after 16 up to the horizons reached: the death criterion was neither triggered nor ruled out.

**Conjectured.** $L$ is not sofic. **Not proved**, and the lane says why: a non-regularity proof needs an infinite
family
with membership proved for all lengths, and the two candidate families found carry bounded memory. **What it
means.** If $L$ were sofic, the period-2 question for left-finite configurations would be a finite-automaton check;
the evidence says it is not, so the real record's finiteness will not come from a finite-state description of column 1
alone. The death criterion is the clean test to push: deaths at arbitrarily late times refute soficity outright.

**Skeptic's verdict (independent agent, Cloud-checked, 22:34 BST).** The exact sets $L_n$ to 26 survived: a brute
force in C to 16 and an independently written lazy enumerator to 26 agree word for word, with identical leaf counts;
the hand proofs for 11 and 00000, the regularity criteria, the fooling sets (51 pairs re-verified), the follower-set
tables, the spectral radii and an independent exact certificate for $h \le 0.2536$ all hold. One item refuted: 15 is
not a minimal death time; the minimal death times in the exact data are 0 to 6, 8, 9, 11, 12, 14 and 16 (Cloud: the
lane's own deaths file lists exactly these), and every later death the lane found is implied by the two minimal deaths
10001001 at 16 and 00001000100 at 14. The 'recurring' absent family $0(1000)^2(10)^r100$ is a window $r = 4, 5, 6$
only: its $r = 7$ member, of length 26 and inside the data, is in $L$ (Cloud re-simulated the witness; 200 random
tails all read the word). The DFA lower bound was capped at horizon 8: with horizon 10 the same method gives at least
291 states at $N = 26$, so part of the 'no plateau' growth is the cap, and inconsistency of horizon-$K$ classes for
$K \le 10$ is expected even for a regular language with hundreds of states, so that evidence is weak. Strengthened: the
late-time stabilisation is now proved by witnesses, $|L^{(j)}_8| = 32$ for $j = 17$ to 21, $|L^{(j)}_9| = 43$ for 17
to 20, then 56, 73, 93 at lengths 10, 11, 12; suffix-properness holds for every $n \ge 7$, not only to 26; the ring
search extends to period 20 with the same answer. The verdict on the main claim is unchanged: open, with the evidence
against soficity somewhat weaker than the lane presented and the evidence for it (no deaths of short words after 16)
somewhat stronger.

**Correction (Cloud, 2026-10-11 02:13 BST, from STRATEGY-PLAN.md section 2 item 6).** The sentence 'none of length at
most 12 after 16 up to the horizons reached' was a horizon effect: Intel's swarm (door D5, its skeptic by an
independent SAT encoding with DRAT proofs, and Intel's own SAT for 34 and 43) finds 0010001 dying at visible time 32,
1000101 at 34, and a length-20 word at 43; every length from 7 to 19 has its latest death at 34, and no word of length
7 or 8 dies between 35 and 100. Third-party COMPUTED (two independent encodings); the death criterion's question,
whether deaths ever stop, is open. The skeptic's stabilisation statements above (to time 21 for length 8) are
unaffected.

### 8.87 The first swarm round, summarised: what held, what fell, what it changes (2026-10-10, 23:16 BST)

*One owner-authorised round, 2026-10-10 evening: five lanes, each an independent solving agent followed by an
independent skeptic, both barred from the record and briefed only with the record's numbers; Cloud graded every report
and every verdict with its own code before writing §8.82 to §8.86. Code and raw outputs stay outside git.*

**What held.** Every hand proof in the five reports survived its skeptic and Cloud's checks: the coupled recursion of
the two wall phases (§8.82), the reductions and lemmas of the half-width question (§8.83), the wall-form identity, the
barrier and front lemmas and the Jen-type theorem for finite patterns (§8.84), the lifetime lemma, locks and structure
theorem of the 1100 wall (§8.85), and the regularity criteria with the death criterion (§8.86). Every computed table
that a skeptic could reach was reproduced by independently written code: $R^\circ(1..62)$, $|L_n|$ to 48 and the 1,612
minimal absent words with their widths (two methods, RUP-checked proofs), $S(0..56)$ and the stored maximisers to 72,
$R'(1..26)$ by a forward lifetime search with spot values to 100, $|L_n|$ to 26 by a second lazy enumerator. The three
exact free-record values the round added, $R(62..72)$, rest on lane q1's run plus re-simulated maximisers until Local
replays them.

**What fell.** No headline fell; six details did, each caught by a skeptic and confirmed by Cloud. The five-black-cell
bound 121 is really 39, exact (§8.84). The 393 unresolved $u(10)^k v$ families genuinely exceed 32 ($T - |w| = 37$ at
$k = 235{,}649$), so they were rightly excluded, not lost (§8.84). The trace form is tight at even lengths too,
$l = 2, 4, 36$ (§8.83). The 1100 lane misquoted its depth-100 rotation values and its structure theorem is looser than the
data: the transition block after $(0100)^K$ is always 0001 for $K \ge 3$ (§8.85). The soficity lane listed a death
time 15 that does not exist and an absent-word family that breaks at $r = 7$, and its DFA lower bound was a horizon
cap, 291 with horizon 10 (§8.86). Several conclusions worded as theorems were heuristics: positive entropy of the
$p$-sequences, 'not of finite type', 'no linear-algebra shortcut', 'the locks do not bound the runs'.

**What it changes.** Two statements are now sharp enough to aim a proof at. First, the trace form: *the free-exterior
strip of width $\lceil l/2 \rceil$ is exact for column-1 traces of length $l$*, verified to $l = 84$ and tight at
seven lengths of both parities; it is the half-width question of CL210 in its strongest true form, and it is proved
only as $2|f| - 2$. Second, the death criterion: a regular visible language has eventually constant late languages,
and the late languages of lengths 8 to 12 are now proved constant from visible time 17 to the horizons reached (21 for
length 8), with every death after time 14 implied by two minimal deaths; a death at a late time of a longer word would
refute soficity outright, and none has been found. The 1100 wall is settled to depth 100 as the alternating wall is to
124, by the same shape of argument and with the same absence of a proof for all depths. Nothing in the round touches
the prize bound directly; the counting heuristic (slope $h/(1-h)$) is untested by it. Follow-up computations are held
until Intel's strategy plan lands, because its doors D4 and D5 are these two statements, and the swarm's code is not
in git. **Prior art for the round's method**: Kimi's two question sets (KIMI-QUESTIONS-2, -3) were the template; the
skeptic stage is new and paid for itself six times.

**Correction (Cloud, 2026-10-11 02:13 BST, from STRATEGY-PLAN.md section 2 item 2).** The counting heuristic's slope
is $h/(2-h)$, not $h/(1-h)$: a visible word of length $n$ decides $2n$ depths, so a run of $r$ white forced cells
costs $r$ coins against $h(d+r)/2$ bits of supply, giving $r \le hd/(2-h)$; the free calibration ($h = 1$, slope 1,
$R(d) \le d + 4$) confirms it where $h/(1-h)$ diverges. Four swarm agents, Intel and the ladder law of §8.14 agree.
The handover's form was Cloud's error.

### 8.88 The check-free conjecture and the forced-only records: the strategy swarm's first target, Cloud-replicated (2026-10-11, 02:22 BST)

*Intel's one-round strategy swarm (nine blind doors, a skeptic each, two judges; STRATEGY-PLAN.md, IN002, assessed in
CL260) converged on one mechanism-shaped target. Recorded here with Cloud's own replication of its defining numbers;
the plan's other new facts stay third-party in STRATEGY-PLAN.md until replayed.*

**The object.** Beside the alternating wall the forced left half is a function of the visible sequence $v$ alone
(§8.84's lemma A: column $-1$ is 1 at black-wall times and $\overline{v}$ at white-wall times). Row 0 at depth $d$ is
$x_0(-d)$. The newest visible bit $v_k$ decides two new depths: in the standard phase depth $2k+1$ always (the
**forced** cell, affine in $v_k$) and depth $2k+2$ in about half the prefixes (the **check**, a function of the
earlier bits once $v_k$ is chosen); in the other phase the parities swap and depth 1 is black (Cloud, 200 random
prefixes per phase). The **forced-only orbit** of a visible prefix chooses each next bit to whiten the next forced
cell, ignores the checks, and dies when that choice leaves $X_4 = \{\text{no 11, no 00000}\}$, which is exactly the width-4
layer language (Cloud: equal to the width-4 free-exterior strip's visible words at length 8 in both phases, 43 words
each) and contains $L$ in both phases. **The check-free conjecture** (CONJECTURED, the swarm's door D2 and judge B):
no sequence in $X_4$ keeps every forced cell of row 0 white from some depth on. It implies period 2 for every finite
configuration in two lines (a counterexample's row 0 is white from its leftmost black cell leftward, so its forced
cells are white there, and its visible sequence lies in $L \subseteq X_4$).

**The forced-only records (COMPUTED, Intel; Cloud-replicated exactly).** $R^F(d)$, the longest run of depths from $d$
on along which every forced cell is white, over all $X_4$ sequences: standard phase
$R^F(1..9) = 2, 17, 16, 15, 14, 13, 12, 11, 10$; other phase $R^F(1..16) = 9, 8, 7, 6, 5, 4, 7, 6, 15, 14, 17, 16, 15, 14, 23, 22$. Cloud's engine
(written from the wall form, not Intel's code) gives the same sixteen and nine values; a first version that stopped a
run at a black check cell gave 1, 6, 5, 4, 3, 3, 3, 2, 9 instead, which is the one definitional trap. Known (swarm):
no eventually periodic sequence keeps the forced cells white (Jen-type, three agents); from depth 60 every forced-only
orbit in $X_4$ dies by depth 154 (third-party); the golden-mean control (no 11 alone) is infinite in the other phase
as it must be. **The plan** (CL260): compute $R^F(d)$ exactly to depth 120 over $X_4$, the width-8 and width-12 layer
languages and the twelve-absent-word class, both phases; a periodic search to period 22; the decay of forced-only
survivor counts along the record walks; then a hand attempt on one sub-family. **Kill:** a forced-white orbit that
never leaves $X_4$ moves the conjecture to the width-8 language; survivors at the cap in the width-12 language with no
decay over 20 steps close the check-free route, leaving the cost lemma, which no data can kill. **Second step if it
dies:** the record-ancestry census (STRATEGY-PLAN.md section 1). **What it is not:** a single-orbit statement is still
a proof obligation for every prefix; the conjecture moves the open part off the checks and onto the forced orbit
inside a finite-type shift, which is where a mechanism could live.

**Qualification (Cloud, 2026-10-11 02:42 BST, after GC1092).** The 'Known (swarm)' sentence above repeats door D2's
claim that no eventually periodic sequence keeps the forced cells white. GPT (GC1092) observes that the available D2
summary proves only the fully white tail (Jen), not the white forced tail, and that outside $X_4$ the forced-only
version is false: the constant visible 1 in the standard phase and the constant 0 in the other have white forced tails
with black checks (Cloud reproduces both, and GPT's exact period-7 depth projections for visible 01 and 10, which have
black forced cells for ever). Within $X_4$ Cloud finds a black forced cell beyond depth 150 in every periodic visible
pattern of period at most 10 (204 patterns, both phases), so the claim stands as COMPUTED to period 10 and the general
argument is owed by the swarm's three agents or whoever supplies it. GC1092's finite bridge (an odd-period successor
over a forced-white parity interval is nilpotent in four ticks; Cloud-verified for q = 1, 3, 5) is the first piece of
such an argument.

**Outcome (Cloud, 2026-10-11 04:42 BST, after IN004 and IN005).** The plan's computations are done (Intel, probe FO;
Cloud replicated $R^F$ at depths 1 to 20 in the standard phase and 1 to 16 in the other exactly, including the jump to
53 at depth 20). Both phases, exact: over $X_4$ to depth 122 and 121, over the width-8, 12, 16 and 20 layer languages
and the twelve-absent-word class to the same depths, no forced-only orbit of any prefix reached the cap of $3m + 300$
steps, so the kill did not fire anywhere. The record grows linearly with slope 1.39, 0.48, 0.36, 0.32, 0.15 over the
widths 4, 8, 12, 16, 20 (other phase 1.34, 0.39, 0.26, 0.22, 0.16), within a factor 0.71 to 1.19 of $h/(1-h)$ at every
width: the counting law of this section in its forced-only form (one depth per visible bit, so $h/(1-h)$; the real
record's form is $h/(2-h)$, section 8.87), measured five times. The kill moves from 11 (86% of the $X_4$ deaths) to the
longer forbidden words (54% at width 20); 00000 stays near 14%. Consequence: over the true language
($h_{top} \le 0.1236$) the law puts the forced-only slope at or below 0.14 against the real record's 0.08, so the forced
cells would account for most of the killing and the checks for a factor near 1.75. Periodic case: computed to period 14
within $X_4$ by Intel's judge B (2,158 primitive words, both phases); the general argument is still owed. Next (CL282):
the forced-only records over the exact visible language, as deep as the length-40 word lists allow.

### 8.89 The room switch: from the forced-only door to the visible language's certified absent words (2026-10-11 07:56 BST)

**Decision (the owner, on Cloud's assessment).** The swarm's door is left as a main line and the main line moves to the
real visible language and its certified minimal absent words (cuts), with the strip form of 8.83 and KIMI-QUESTIONS-4
as its finite-width face. **Why.** (1) The forced-only door is fully measured (8.88): no orbit survives, the slope falls
with the layer width as the counting law says, and the kill moves to the longer absent words; as a proof route it has
reduced to characterising those words. (2) GPT's collar lane (GC1097 to GC1118, every block confirmed by Cloud's own
computation, CL273 to CL296) has produced a complete local theory of the delayed black-A resets: an immediate restart is
impossible from age 4 and possible at ages 0 and 2; a restart through one white SS block is real; the pure two-SS
chain is bounded, by Local's cake_lpr-certified cuts (LLSSS)^6 (114 bits) and (SSSLL)^6 S (117 bits), at 18 completed
macros and 672 ticks; the mixed two-SS/three-SS recurrence survives every sound refinement to strip width 36 and is
killed neither by periodic cuts nor by periodic-piece deadlines; and the forced left half carries the renewal choices
losslessly to columns -12, -20 and -22. The lane's own next step is a restrictive visible-language condition. (3) The
night's prize-relevant facts are all of one kind: exact values (R_real(132) = R_real(139) = 17), certified cuts, and the
exact visible language to length 40. **The decisive test** (CL297, Local): whether the visible words of the two closed
walks FE and EF of GC1106 (117 samples each) and their concatenations lie in the real language. Absent: the typed regime
closes by certified cuts. Present: an actual right half beside the wall repeats resets for ever with non-periodic
choices, and the period-two question becomes left-sided (finite support against a right half that never settles).
**Stopped:** strip widening, realization searches, the X_4 hand target. **Continuing:** SAT-200b, the phase-1 runs at
139 and 142, one exact-language forced-only run (Intel), then the strip thresholds L(W) for W = 6 to 10.

**Outcome (2026-10-11 08:14 BST, L630).** The membership test answered "absent": E's visible word contains SLC2's certified 69-bit
cut, FE and EF contain certified cuts of 54 and 61 bits, and every concatenation contains E; M1, M2 and M3 are present.
The mixed recurrence is a relaxation artefact and the typed regime closes by cuts; GPT maps the three cuts onto the
exact temporal grammar next (CL300). Containment re-checked by Cloud.

**Outcome 2 (2026-10-11 08:29 BST, IN006).** The forced-only record over the exact visible language to length 40 equals the width-20
layer's at 120 of 122 depths (phase 0), no orbit reaches the cap, and the slopes are 0.85 and 0.78 of h/(1-h): the
forced-only measure has converged and the checks account for the remaining factor of about 2.5 over the real record, so
the door stays closed by its own instrument. The strip form (8.83): L(W) = 3, 6, 6, 10, 10, 17, 20, 20, 20, 26, 30 for
W = 1..11 in the standard phase and 2, 7, 7, 11, 11, 14, 14, 19, 19, 23, 23, 23, 29, 29, 29 for W = 1..15 in the odd
phase (Intel, bit-sliced over all right halves; independent numpy enumeration to length 24 agrees); Conjecture S holds
at every width computed and is SHARP in the odd phase at W = 12 and 15, where L(W) = 2W - 1 exactly; the pairing
L(2k) = L(2k+1) is not a law; the extra traces of the two phases are one family under dropping the first symbol; and
the lemma w(f) <= |f| - 2 holds in the standard phase only (odd phase: L(1) = 2 through the trace 000).

**Outcome 3 (2026-10-11 08:54 BST, CL303).** The complete cut product over the whole width-28 strip graph of the collar
grammar (6,431 strip states, 870,080 labelled macro edges, two cyclic components: the 97-state mixed one with labels 1, 2,
3 and a 10-state pure-M2 one) with the Aho-Corasick automaton of the eleven certified cuts in hand (L631's nine, L627's
114, L628's 117) has exactly one cyclic component left: 62 product states and 1,073 edges, all of label 3 and branch 111,
the pure-M3 self-loops. L631's nine cuts alone leave pure M3 and pure M2; the 114- and 117-bit cuts remove pure M2. So
every infinite typed path of the width-28 relaxation that avoids the certified cuts is eventually pure M3, a visible
column of eventual period 22, which the reviewed eventual-periodicity theorem (GC706/707) excludes for finite left
support: the typed collar regime is closed by cuts at width 28, with the pure-M3 tail as its whole residue (Local's CC
decides whether even that word is absent). What this does not say: nothing about untyped traces or about R_real at any
depth. The nine cuts read as macro guards (each is a continued factor: 3,1; 1,2,1; 2,2,j>=3; 1,2,j>=3 with a predecessor;
3,1,2; 2,1,2; 1,2,2; 1,2,3), and on the component's successor relation (1 is followed only by 2; the realised pairs are
12, 21, 23, 31, 33) the same conclusion follows by hand: after the first 3 the path is pure 3 for ever, and before it only
a 2 may stand.

**Outcome 4 (2026-10-11 09:32 BST, CL305 and CL306).** Local's L632 finds the pure M3 word absent at every length-300
window, so the product's residue is itself cut and the typed collar regime is excluded under the period-2 wall alone,
with no finite-left-support condition (the minimal cut is pending). GPT's GC1126 found the omitted H-low route, a
58-tick macro N = S D H D H SS SS whose completed 30-bit visible word is present in both phases with its continuation
forced to S; confirmed here at widths 20 and 24 (exactly two SS, by exhaustion). At width 28, from all 98,304 A-type
rows, N has 96,029 origin/end pairs, 185 sources and 681 endpoints; no source lies in the macro graph, N lies on no
cycle, no N endpoint ever reaches an N source again, and the cut product with N edges included is unchanged: pure M3
only. N is a one-shot entrance into the typed components, and the closure stands with it.

**Outcome 5 (2026-10-11 10:29 BST, CL318 and CL319).** The typed graph's transient part at width 28 has no corridors: a
typed path enters a recurrent component within 2 macros (88 ticks) or has no typed continuation within 3 (246 ticks).
And with the eleven certified cuts and the certified absence of every 300-sample pure-M3 window (L632), the cut product
over the whole width-28 graph with N edges is acyclic: 71,852 product states, no cycle, longest typed path 13 macros and
686 ticks (twelve M3 returns, then one macro with 22 SS blocks). So under the period-2 wall every trace that follows the
typed collar grammar does so for at most 686 ticks, a bound resting on certified absences only; the pure-M3 minimal cut
will lower it. It says nothing about untyped traces, re-entries, or R_real.

**Outcome 6 (2026-10-11 14:06 BST, CL329 to CL336, GC1139 to GC1142).** The entrances to the typed region are accounted
for. GPT's certificates, each replayed here by an independent complete computation: the sixteen negative white-A high-LL
entrances admit the mixed core by 36 (GC1139, CL328); the twelve positive ones admit by 52 or exit through X at 26
(GC1140, a 1,512-leaf all-tail cover re-derived to the same digest, CL334); outside the 28-cylinder gate every white-A
origin admits C at 16 (3,392 of 4,068) or returns high 111 into a black-marker SS (676) (GC1141, CL334); and the first
SS after a high-111 origin never exits through unguarded B (GC1142, CL336, by a forward census of all 524,288 actual
high-111 cones). The X exit, which the typed grammar does not describe, was measured in real cones to tick 212 with 2^24
exteriors per cylinder (CL332 to CL335): X is fixed by the cylinder in ten cases of twelve; 3.2 percent of the X cones
reach the pin shape 1110011110100 at 66; 98.2 percent of those run one chain of white SS entrances at 94 and 100 to a
white-eleventh A at 106 (the white-A origin row itself in 58 percent); the returned origins carry ten rigid patterns
outside the gate and admit the C core at 122 by GC1141; and through 212 those cones show no A of either colour, no pin
and no SS entrance. The X exit renews nothing of this family. Open: the 676 black-marker SS entrances and admission
after an intervening white SS (GPT), and the sea's untyped admission, whose rates in X cones were 7.4 x 10^-4 black AP13
rows and 3.2 x 10^-5 white-A origin rows per cone per even tick. Scope: the certificates are all-tail; the X
measurements are sampled real cones, three draws, one seed each.

**Outcome 7 (2026-10-11 14:14 BST, L637, CL338, CL340).** Local certified pure M3's minimal cut: least absent length
178, exactly one minimal cut, cake_lpr-verified (CC10 held, CC1 refuted), so every recurrent object of the width-28
collar graph has a certified minimal cut (M2 at 114 and 117, M3 at 178, N at 49, the N/F splices at 39, CL301's cycles
at 54 and 56, the M2/M3 mixtures by containment). With that cut in place of the 300-sample windows the cut product is
acyclic and the longest typed path is 8 macros and 466 ticks (seven M3 returns, then the macro with 22 SS blocks), so
under the period-2 wall every trace that follows the typed collar grammar does so for at most 466 ticks, on certified
minimal cuts alone; Outcome 5's 686 is superseded. R_real(144) <= 17 is certified in both phases (L637).

**Outcome 8 (2026-10-11 15:30 BST, CL346, CL347, CL348, GC1150).** An actual renewal from a white-A entrance outside the
gate. The origin 1110100011011010010010000100100000000000000000000000000000000000 (64 cells, every farther tail; sites
14..25 = 010010010000, one of GC1141's 676 non-LL sources) runs high 111 at 16, a black-marker S at 26, SS at 32 and 38,
the unguarded B 11101001100101110101 at 44 (so no known guard admits it), white SS entrances at 60 and 66, the black
AP13 row 1110100011101 at 72, the low row at 78, the same high-111 image 1110011111110 at 88 and a black-marker S at 98,
all fixed by the 64 cells; the exterior first matters at tick 112. It was found by a carrier-pruned search over actual
origins after GC1146's displayed counters proved unliftable (neither is the tick-16 image of any white-A origin; the 29
actual non-LL image rows are listed in CL346), and GPT confirmed it by an unclamped full-row replay (GC1150). So the 676
black-marker SS entrances are not admitted by three SS, and a white-A entrance can renew the typed black collar 72 ticks
later; the typed stretch it enters is still bounded by the certified cuts (Outcome 7). Over 2^24 tails no mixed-core row
appears before tick 80 (CL347). In the same hour Cloud claimed to refute GPT's record-conditioned SS budget GC1148
(CL348); that claim was Cloud's orientation error and is withdrawn (15:47 BST, CL350): the record is the left row,
GC1148's determination step is exact, and GC1148 stands as a proof sketch.

**Lane closed (the owner, 2026-10-11 16:21 BST, CL355).** With Outcome 8 the admission-deadline route of the entrance
lane is CLOSED and the lane stopped; its results (GC1139 to GC1147, Outcomes 6 to 8) stand. GPT moves to the
finite-support record route (Q6): period 2 falls if R_real(d) is finite at every depth, and the left row determined by
the trace is the tool (GC1148, GC1151, GC1153, GC1154). The certified closure of the typed regime (Outcome 7) is a lemma
for that room.

### 8.90 The carry of Rule 30: the Gray correction is a two-time AND, and the column carry is exactly solvable (2026-10-11 10:06 BST)

The question is the owner's (2026-10-11, CONSTELLATION row 21, stated for a worker in KIMI-QUESTIONS-5.md): write the
rule as the two-cell Gray step plus a correction, x_{t+1}(i) = x_t(i-1) XOR x_t(i) XOR c_t(i) with c_t(i) = (1 - x_t(i))
x_t(i+1), in the way that multiplying by 3 is a Gray step plus carries, and ask whether the correction has the kind of
exact structure Holte found for arithmetic carries (a Markov chain with an explicit matrix and eigenvalues 1, 1/b,
1/b^2, ...). Intel took the lane (IN007, probe rule30_intel_carry.py, C with OpenMP on the Intel MacBook); the checks
here are Cloud's (CL308, CL310, CL313).

**The identity (Intel, PROVED; checked here on all sixteen windows).** c_t(i) = x_t(i+1) x_{t+1}(i+1). If x_t(i+1) = 1
the rule gives x_{t+1}(i+1) = x_t(i) XOR 1 = 1 - x_t(i), which is the correction; if x_t(i+1) = 0 both sides are 0. So
the Gray step's correction is the AND of the column to the right at two consecutive times, the run count K_t of a row is
the overlap of rows t and t+1, and the rule has the space-time form x_{t+1}(i) XOR x_t(i+1) x_{t+1}(i+1) = x_t(i-1) XOR
x_t(i).

**The column carry is exactly solvable (Intel, PROVED; checked here by exact enumeration of all 2^15 coin words).**
Under the coin measure on the whole line, which Rule 30 preserves, a column is a sequence of independent fair coins
(each x_t(0) contains the fresh cell x_0(-t)), so by the identity the column carry c_t(0) = x_t(1) x_{t+1}(1) is the
sliding AND of fair coins: a two-state hidden chain, not a Markov chain of any finite order (the exact conditional laws
differ at every order, the difference shrinking by a factor 1/phi^2 per step), with correlation 1/3 at lag 1 and exactly
0 at every larger lag, P(c = 1 after m zeros) = F(m+1) / (2 F(m+3)) with F the Fibonacci numbers (1/6, 1/5, 3/16, 5/26,
4/21, 13/68 for m = 1..6), and entropy rate h = 1 - (1/16) sum over g >= 1 of F(g) 2^(-g) log2 F(g) = 0.69924320338768
bits: given the carries the coins are fixed except in the gaps between runs of two or more ones, which arrive at rate
1/8 with length law F(g)/2^(g+1) and F(g) equally likely fillings. The block-entropy differences of the exact process
converge to 0.699243 by block length 7, and a sampled estimate of 0.69934 (10^5 rings of 4,096 cells, 2,000 steps) had
already pointed there. Along the leftward light-speed diagonal the carry is i.i.d. Bernoulli(1/4) (fresh cells); along
the rightward one it has long memory (correlations -1/3, 1/4, -0.146, 0.120, ...).

**Rings, exhaustive to n = 28 (Intel; n = 12, 14, 16 re-done here).** The run count K is not a Markov chain, and
corr(K_0, K_1) = 1/2 and corr(K_0, K_2) = 1/8 exactly at every n, with 1/32 at lag 3 and about 5/128 at lag 4 (CL310,
conjectured exact; Intel's IN008 is to decide them): there is no Holte matrix for the run count. The adjacent-black-pair
count D (the Rule 150 correction) and the black count B have spectra near the powers of -1/2 (D at n = 28: -0.5048,
0.2518, -0.1252, 0.0667), so a geometric ratio -1/2 does appear, for the three-XOR correction. K = 0 is absorbing and is
reachable from a live row exactly when 3 divides n, because a row maps to all-black only if it is a rotation of
(001)^(n/3) (a 1 at cell i forces 0, 0, 1 at i-1, i-2, i-3); the alternating row is fixed, so K = n/2 is absorbing for
even n. Quasi-stationary mean and variance are n/4 and n/16 to four decimals.

**The single cell to t = 65,536 (Intel).** The Pascal-mask identity x_t(0) = 1 XOR P_t holds at every t; the correction
density over the whole mask tends to 1/8, because half of the mask lies outside the light cone, and to 1/4 inside it;
the parity series has no autocorrelation above 0.011 at any lag to 64, powers of 2 included, and every window of 1,024
steps is within 0.46..0.53 of balanced.

**Scope.** None of this touches the centre column's periodicity directly: the exact solution lives under the coin
measure, where the prize questions are not asked, and the single-cell parity is coin-like without being proved so. What
the identity gives is a clean object, the two-time AND, in place of an ad hoc correction field, and the first exact
answer to the owner's question: the run count has no amazing matrix, the three-XOR count nearly does, and the column
carry is a solved hidden chain with a Fibonacci entropy rate.
