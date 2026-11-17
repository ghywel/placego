# Theorem A⁗ (a repeat's white run cannot lie in the settled band)

*Windows, zero runs and the left band. Derived from [PROOFS.md](../PROOFS.md), entry "13. Theorem A⁗ (a repeat's
white run cannot lie in the settled band)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and
this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved.

## In plain words

The white stripe a repeat leaves cannot sit inside the settled band.

**What it says.** Combining 10 and 12: if the band near the edge is settled, a repeat's white stripe would have to
lie in it, and it cannot be longer than 2P − 1 there, so the repeat is bounded.

**Why it matters.** A sharper cap on repeats, from the edge band's own regularity.

**An everyday picture.** Driving round a busy car park: spaces keep opening as cars leave, but each is small and
gone within moments, and you pass the car about to leave just before it goes, so a driver who needs a long space
where they are can circle for ever while spaces are made all around them (the owner's reading). The settled band is
that car park. White gaps are born in it all the time, but none is wider than 2P or older than P steps (12), so the
long white stripe a repeat needs is never there at the moment and place it is needed.

**Checked by machine.** A proof assistant (Lean) has checked it, in the sharper form with 2P − 1.

## The formal statement and proof

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
