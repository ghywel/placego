# The latch

*Short proofs restated from the running text. Derived from [PROOFS.md](../PROOFS.md), entry "C.2 The latch
(RULE30-PRIZE.md §8.62; 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this
summary in [summaries.md](summaries.md), never this file.*

**Status:** proved.

## In plain words

While the middle column stays white, column 1 can switch on but never off.

**What it says.** When the middle square is white, column 1's next value is "column 1 or column 2". So across a
white stretch of the wall, once column 1 turns black it stays black until the stretch ends.

**Why it matters.** It turns column 1 into a one-way switch during white stretches, which sharply limits what the
right side can say there. Walls with long white and long black stretches ("slow walls") are studied with this tool.

**An everyday picture.** A set-reset latch (the owner's picture): column 2 can press "set", and pressing it again
changes nothing; only a black beat of the wall, a button the right side cannot reach, resets it. Proof 03 is the
same latch with its reset written in.

## The formal statement and proof

*Where:* §8.62, the white Condrey end. *Bears on:* Conjecture B next to white stretches; the slow walls (§8.63). *Status:* proved.

**Lemma.** If column 0 is white at time $t$, then $x_{t+1}(1) = x_t(1) \vee x_t(2)$. Hence across a white stretch of
the wall column 1 is non-decreasing: once black it stays black until the stretch ends.

*Proof.* Rule 30 at column 1 reads $x_{t+1}(1) = x_t(0) \oplus (x_t(1) \vee x_t(2))$, and $x_t(0) = 0$. $\square$
