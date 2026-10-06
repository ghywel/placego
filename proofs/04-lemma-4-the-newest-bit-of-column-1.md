# Lemma 4 (the newest bit of column 1 enters once, as an XOR)

*The wall form. Derived from [PROOFS.md](../PROOFS.md), entry "4. Lemma 4 (the newest bit of column 1 enters once,
as an XOR)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved; checked (P2).

## In plain words

Each new bit from column 1 reaches the left exactly once, either as a clean flip or not at all.

**What it says.** The square at depth k on the left depends on column 1's first k bits, and on the newest one in a
very simple way: at a white beat it flips the answer (an exclusive-or), and at a black beat it does nothing.

**Why it matters.** This makes the information exactly countable. Many later results, including the "one bit per
condition" counting, rest on this clean bookkeeping.

**An everyday picture.** A light switch on a long corridor: each new switch either flips the light or is
disconnected; it never does anything in between.

## The formal statement and proof

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
