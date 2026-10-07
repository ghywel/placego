# Proposition 11 (proved): a pulse's three-edge window is worst at the pulse's own phase

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "24. Proposition 11 (proved): a
pulse's three-edge window is worst at the pulse's own phase"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** Local's proof; second-read by GPT (GC346) and filed out of the waiting room, 2026-10-07.

## In plain words

After a lone black cell drives the pattern, the three steps that follow cost the most when the clock arrives just after that cell.

**What it says.** The project keeps a reference clock and charges a "debt" when the pattern runs slower than that clock allows. When a driving row has a single black cell, the next two rows are forced into a known shape (GPT's GC340). This result shows that the debt over those three steps is largest when the clock arrives one step after the black cell, whatever the arrival time. So the worst case can be priced exactly, without the extra allowance that a general shift of the clock would add.

**Why it matters.** The open target is to show that the clock's debt stays bounded. Each lone-cell event can now be charged its exact worst case rather than a padded one, a saving of nearly a full period for each event. It does not yet say how many such events a history has, or how they overlap.

**An everyday picture.** A train that leaves once an hour: the longest you can wait is when you arrive just after it has gone. Whatever time you turn up, after it leaves you are on its timetable, so only your first wait depends on when you came.

## The formal statement and proof

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
