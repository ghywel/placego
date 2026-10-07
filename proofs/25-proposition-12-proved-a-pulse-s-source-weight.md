# Proposition 12 (proved): a pulse's source weight is set by its child's black runs

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "25. Proposition 12 (proved): a
pulse's source weight is set by its child's black runs"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

How heavy the row before a lone black cell is can be read off the row after it: count its black stretches.

**What it says.** Take a driving row with a single black cell, and the row it produces next. The row before the lone cell is fixed by that next row, and its number of black cells is twice the next row's number of black stretches, give or take one depending on what sits at and just after the lone cell. So a "heavy" earlier row, with more than three black cells, forces the next row to have at least two separate black stretches. It also fixes whether that earlier row has an odd or even number of black cells.

**Why it matters.** GPT's latest steps charge each lone-cell event a debt that depends on the lengths of the first gap and the first black stretch, and bound those lengths by the earlier row's weight. This identity explains where GPT's weight thresholds come from, and with GPT's bound it shows that one of the earlier caps is never reached. It does not count how many such events there are.

**An everyday picture.** A fence painted in stripes: the number of places where the paint changes colour is always twice the number of painted stretches. Knowing how many colour changes a painter made tells you how many stretches there are, and so how long any one stretch can be.

## The formal statement and proof

*Where:* chat L215; `tests/probes/lexicon/rule30_audit_g99_g100.py` S122, S123. *Bears on:* GC347 (RULE30-GPT.md,
"Heavy pulse windows share a period budget between their second and fourth delays"), and GC349, whose caps it explains
by parity; GC344's weight thresholds; PERIOD-TWO.md Q7. *Status:* Local's proof, awaiting GPT's second reading.

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
