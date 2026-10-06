# Theorem A‴ (the window principle, with the band)

*Windows, zero runs and the left band. Derived from [PROOFS.md](../PROOFS.md), entry "10. Theorem A‴ (the window
principle, with the band)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved.

## In plain words

A repeat leaves a white stripe behind it, and a black diagonal there caps the repeat.

**What it says.** If two neighbouring columns repeat a block of n values, the row at the second occurrence is white
across a whole range of diagonals. So a black diagonal inside that range limits how long n can be.

**Why it matters.** It joins the repeat bound (07) to the edge band (08, 09): the band's black diagonals become
measuring sticks for repeats.

**An everyday picture.** A fingerprint left on glass: a repeat leaves a mark you can check for later.

## The formal statement and proof

*Where:* RULE30-PRIZE.md, "8.59 The window principle meets the band of stripes: a repeat is a white run, and the left side is never white for long (2026-10-05)". *Bears on:* the window principle with the band. *Status:* proved.

**Theorem A‴ (the window principle, with the band).** Let the leftmost black cell at time 0 be $L$ cells left of
column $i$, and let the pair of columns $(i, i+1)$ show the same block of $n$ values from the times $a$ and $a' > a$.
Then row $a'$ is white on its diagonals $L + a' - n + 1$ to $a' - a - 1$. Hence, if diagonal $b$ is black at time $a'$
and $b < a' - a$, then $n \le L + a' - b$.

*Proof.* By §8.58 the rows at $a$ and $a'$ agree on the $n - 1$ cells left of column $i$. Row $a$ is white beyond
distance $L + a$, so row $a'$ is white at the distances $L + a + 1$ to $n - 1$. Its leftmost black cell is at distance
$L + a'$, so those distances are its diagonals $L + a' - n + 1$ to $a' - a - 1$. A black diagonal $b$ in that range
contradicts this; so either $b \ge a' - a$ or $b \le L + a' - n$. $\square$
