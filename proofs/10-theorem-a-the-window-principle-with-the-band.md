# Theorem A‴ (the window principle, with the band)

*Windows, zero runs and the left band. Derived from [PROOFS.md](../PROOFS.md), entry "10. Theorem A‴ (the window
principle, with the band)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved.

## In plain words

A repeat leaves a white stripe behind it, and a black diagonal there caps the repeat.

**What it says.** If two neighbouring columns repeat a block of n values, the later row must copy the earlier row
across the n − 1 squares beside them (07). The earlier row was blank beyond its edge, so the copy carries that blank
margin into the later row, a white stripe across a range of diagonals. A black diagonal inside that range would
contradict the copy, so it limits how long n can be.

**Why it matters.** It joins the repeat bound (07) to the edge band (08, 09): the band's black diagonals become
measuring sticks for repeats. A block of the two columns is a fingerprint without collisions of the squares beside
them, which is why a repeat can be checked at all.

**An everyday picture.** A forged page (the owner's forensic reading): a passage copied from an older, smaller
document brings the older document's blank margin with it. If the new page has ink where that margin falls, the copy
is exposed.

**Checked by machine.** A proof assistant (Lean) has checked the argument.

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

*Machine-checked (Local, 2026-10-10 04:47 BST).* tests/probes/lean/TheoremAprime.lean, beside Theorem A′.
- `theorem_A3_white`: row a' is white at the distances L + a + 1 .. n - 1 left of column i.
- `theorem_A3`: if diagonal b (the cell b right of the moving left edge) is black at time a' and b < a' - a, then
  n <= L + a' - b.
- The axioms are propext and Quot.sound only.
