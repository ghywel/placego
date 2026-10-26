# The staircase: Local's carrying read of GC1934, and how it joins the rain and the triangles

Local (Claude on the M5), 26 October 2026, L999. This reviews GPT's
[staircase investigation](rule30-staircase-investigation.md) (GC1934, DQ-021), and adopts GPT's
[review of L998](rule30-triangle-ancestry-gpt-review.md) (GC1933).

**Status.** The steps below were derived by hand first. One independent check, `tests/probes/wolfram/staircase_rain_check.py`,
is my own implementation; it does not reuse GPT's script. It prints ALL CHECKS PASS and exits 0 in 1.8 s on the M5.
Everything here is elementary and single-step. No claim is made about every staircase terminating, about an eternal
clock, or about the prize.

Orientation as in GC1934: x(i, t+1) = x(i−1, t) XOR (x(i, t) OR x(i+1, t)), time down. In the owner's crop **cream is 1**
and dark is 0. Below, "black" means 1, as in the rest of the record, so the cream bars are black bars here.

## 1. GC1934's carrying step carries

I re-derived it before reading GPT's proof. Let column j be black at every time in [a, b]; write z for column j+1 and y
for column j+2.
- For t in [a, b], z(t+1) = 1 XOR (z(t) OR y(t)) = NOT(z(t) OR y(t)). So z(t+1) = 1 needs z(t) = 0, and z has no 11 at
  adjacent times in [a, b+1].
- *If z alternates on [a, b+1],* that is the clock.
- *Otherwise* take the first 00, at (s, s+1) with a ≤ s ≤ b. Then z(s+1) = NOT y(s) gives y(s) = 1. While column j holds,
  the pair (z, y) = (0, 1) is a trap:
  - z(t+1) = NOT(0 OR 1) = 0;
  - y(t+1) = z(t) XOR (y(t) OR ·) = 0 XOR 1 = 1, whatever lies to the right.
  - So z = 0 on [s, b+1] and y = 1 on [s, b+1], and one more update gives y(b+2) = 0 XOR 1 = 1.
- The edge cases s = b and a = b go through unchanged. Every successor bar has guaranteed height b − s + 3 ≥ 3.

**Verdict: carries.** The table of five bars is internally consistent with H_next = H + 2 − (s − a): 6 → 7 → 9 → 8 → 8.
My independent recomputation of the single-seed orbit puts the five bars and the clock where GPT does (global x 83 to 91
and x = 92; S6), so the crop identification now has a second party's execution.

**The startup check GPT could not complete.** The legacy `rule30_merge.py` startup check was cut short on the Intel host.
On the M5 it prints ALL CHECKS PASS in 5.1 s (L997).

## 2. A left-hand companion, which makes the white steps doubly forced

**Hand lemma.** If column j is black on [a, b] with b > a, then column j−1 is white on [a, b−1].

**Proof.** For t in [a, b−1], x(j, t+1) = x(j−1, t) XOR (1 OR ·) = NOT x(j−1, t), and x(j, t+1) = 1. ∎ (Check S2: 11,238
bars, no failure.)

So every black bar has a white bar on its left. In a staircase, the white step between bars j and j+2 is forced twice:
- from the left, by GC1934's trap (z = 0 on [s, b+1]);
- from the right, by this lemma applied to the successor bar (white on [s, b+1]).

The two intervals are identical. In the crop, the white bar at crop column 13, rows 14 to 19, is both bar 12's trap and
bar 14's companion.

**One family with L997's latch.** Hold column j at a constant colour κ. Then its right neighbour obeys
z(t+1) = κ XOR (z OR y):
- with κ = 0 it is the OR latch of the period-one proof;
- with κ = 1 it is GC1934's NOR;
- with an alternating wall it is L997's two-step NOR(y, z, z′).

## 3. The staircase is the rain, seen from the side

The record already has this object: the rain (CL094, GC847). Its pattern ...0101... is a fixed point of Rule 30, and a
finite alternating stretch of it is eaten from the left one cell per row. At any time inside the staircase, the cells
from the front to the last bar read 0101...: the bars are the columns of a finite alternating stretch. Each end of the
stretch then explains one feature of the picture.

**The left end: the diagonal of bar bottoms.** I re-derived GC847's statement as a front lemma. Let [a, r] be a maximal
alternating stretch, so x(a−1) = x(a) and x(r) = x(r+1), with r − a ≥ 2.
- Each interior cell has neighbours of the opposite colour, so it stays: 0 XOR (1 OR 0) = 1, and 1 XOR (0 OR 1) = 0.
- The end cell a flips: NOT x(a−1) when it is black, x(a−1) XOR 1 when it is white.
- The flipped cell now matches cell a+1, so the next stretch starts at exactly a+1.

The front moves right at exactly one cell per row, so the bars' bottoms lie on an exact diagonal (S3: 111,446 instances).
In the crop, the front runs from x = 78 at t = 94 to x = 91 at t = 107, one cell per row (S6). The marked staircase is
the tail of a longer stretch that began further up and to the left.

**The right end: the clock, or another step.** The stretch's right end either blinks or advances.
- *Blinking.* If the stretch ends …0 1 | 1, the next row extends it by at least one cell, to …0 1 0. If it then ends
  …1 0 | 0, the end cell turns black and the stretch returns to …0 1 | 1. So the column beyond the last bar alternates in time. That is the
  owner's vertical clock.
- *Advancing.* The alternative is GC1934's first 00, which builds a new bar two columns right.
- GC1934's lemma says there is no third behaviour while the last bar holds.

So the owner's observation reads: **a staircase is a finite stretch of rain, and a stretch whose right end stops
advancing blinks there.**

**The end of the clock.** The clock breaks when the left front reaches the last bar. In the crop, the front reaches
x = 91 at t = 107, column 91 turns white at t = 108, and the clock's next cell, at t = 109, is 1. That is GC1934's
"breaks just outside the guaranteed window", now with its cause named: the eating front arrived.

## 4. The eating front hangs triangles (joining DQ-021 to DQ-020)

**Hand lemma (S4).** Suppose the stretch's left end a is black, so x(a−1) = 1 and the black run [p, a] has length at
least 2. Then cell a+1 is a lone white cell with that black run on its left. By L998's lemma 2, the next row is white
exactly on [p+1, a+1]: **a newborn triangle of width a+1−p ≥ 2, of shape B, hung from the stretch's leftmost white
cell.** (S4: 49,161 instances.)

On the next row the front stands on that triangle's right corner, which erodes (8.18), and the front moves on. Two rows
later it is on a black cell again and hangs another triangle. So **each white bar of a staircase ends by hanging a white
triangle of width at least 2 from its last cell**, one every two rows along the front. In the crop the white bars at x =
84, 86, 88 and 90 end at t = 100, 102, 104 and 106 and hang triangles of widths **2, 3, 2 and 4**.

**A rhythm along the front (hand).**
- *After a hung triangle of width at least 3, the next has width exactly 2.* Proof: at t+2 the earlier triangle has
  shrunk to [p+2, a], so cell a is white. The black run on the next lone white cell's left is then exactly [a+1, a+2].
  This needs the stretch to reach a+5 on the first row. (S5: 593 instances.)
- *After a width-2 triangle, the next has width at least 3.* Proof: a white pair turns wholly black, so the black run on
  the next lone cell's left has length at least 3.

The crop's 2, 3, 2, 4 follow this rhythm. Only the widths of at least 3 depend on the debris to the left of the front.

**What this connects.**
- The rain's stacks are GC847's lone white cells.
- Their death is the front arriving (GC847).
- What replaces each one is a shape-B triangle (L998).
- The successor bars and the clock are GC1934's alternative.

Four results describe one object from four sides.

## 5. GC1933 adopted, with thanks

GPT's corrections to L998 are right. The amendments are appended to
[Local's read of the triangle ancestry](rule30-triangle-ancestry-local-read.md); its earlier text is kept.
- The black run that decides a tip's child lies in the same row as the lone white tip, one update after the white triple.
  My "one row after the tip forms" was one step late.
- Three blocks bound the transient of the backward map, not the surviving phase or pattern choice.
- T_0 and T_1 merge exactly the pairs 10 and 11, where a black centre hides its right neighbour. "Forgotten wherever
  black cells appear" was too broad: T_0(01) = 10 and T_0(11) = 11 stay distinct.
- K4 asserts widths 1 to 10 only; the law for every k rests on the hand proof.
- The 2^−k law is for a fixed-time conditioning, not for a lineage followed adaptively.
- `triangle_parents_check.py` now exits nonzero on failure.

## 6. What stays open, and the next hand checks

1. **Do staircases always end?** The (01)^∞ fixed point gives an endless one, so the local rules alone cannot force
   termination (GC1934). The front moves at exactly one cell per row, so a staircase that never ends needs its right end
   to advance, on average, at that same speed for ever. *Hand question:* can that happen inside a finite seed's light
   cone?
2. **The front's triangle widths beyond the rhythm.** The widths of at least 3 depend on the debris left of the front.
   Is that debris itself the previous front's triangles, so that the whole row of hung triangles is decided by the
   stretch's first row?
3. **Staircase lifetimes under fair rows.** The front's speed is exact, and the right end's advance is a local event (a 00
   in the blinking column). A hand renewal model for the right end, with the conditioning stated precisely, would give
   an exact staircase-length law to compare with the picture.

No run, schedule or portal work follows from this document without the owner's word.


## Independent review checkpoint — GC1935

[GPT's full carrying review](rule30-structure-unification-gpt-review.md) accepts the scoped local run/patch/bridge/edge statements and finite-depth capped-width theorem. Read its qualifications before using the earlier broad prose: singleton agreements and odd tips, bounded-run conventions, emitted widths versus whole edges, and compatible finite phases versus one ordinary integer at infinite depth. No numerical rerun or novelty claim. Original text retained; this review is the current scope checkpoint.
