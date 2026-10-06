# Proposition 7 (Jen)

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "17. Proposition 7 (Jen)"; rebuild
with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never
this file.*

**Status:** proved (Jen 1986, restated with proof).

## In plain words

If both the middle and column 1 eventually repeat, the left half cannot be finite (Jen's theorem).

**What it says.** Two neighbouring columns that both repeat from some point on force infinitely many black squares
on the left.

**Why it matters.** It settles every periodic column 1 at once. Since a finite seed makes column 1 irregular, the
open case is exactly the irregular one.

**An everyday picture.** Two drummers keeping steady beats cannot hush the whole crowd to their left.

## The formal statement and proof

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
