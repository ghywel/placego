# Lemma 3 (two local rules from the right side)

*The wall form. Derived from [PROOFS.md](../PROOFS.md), entry "3. Lemma 3 (two local rules from the right side)";
rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved; checked on random sequences.

## In plain words

Column 1 must obey two simple traffic rules, whatever lies further right.

**What it says.** When the middle is white and column 1 is black, column 1 stays black next tick. When the middle is
black and column 1 is black next tick, it must have been white this tick.

**Why it matters.** The right side cannot send just any signal: these two rules already rule out some patterns of
column 1, which is the first narrowing of the channel.

**An everyday picture.** One-way streets: some routes are simply not drivable, whatever the traffic is doing.

## The formal statement and proof

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
