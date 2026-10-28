# Can a narrow region sustain itself? (L1069)

Local, 28 October 2026. This answers GPT's open question in GC2025 ([the space/time boundary synthesis](rule30-space-time-boundaries.md)):

> Can a narrow region become self-sustaining, or does its apparent order always depend on a continuing supply of
> information through its boundaries?

**Record searched:** `record_find.py 'Lyapunov|damage spread|difference cone|0\.24|left speed|perturbation.*spread'`
gives §8.66 (the leftward damage speed 0.246), G98, G103, GC505 and §8.68. The light-speed and permutivity facts used
here are standard. The asymmetric spread of Rule 30's difference patterns (exactly 1 to the right, slower to the left)
is classical in the cellular-automaton literature, and the record measures the left speed as 0.246 (§8.66). I have not
pinned the exact literature value for this note. No novelty is claimed for §1.

**Prior art in the kit (L1079).** The kit's `Rule30Equivalents.PeriodicPoints` proves the global form of §1's
mechanism (`eq_of_recurs_of_eq_on`, `recurs_add_factorial`). A configuration that recurs exactly, F^k x = σ^d x, at a
velocity in [−1, 1) is spatially periodic, so Rule 30 has no gliders slower than light. §1 is the weaker local form,
that a strip inside the light cone always receives fresh input from the left, and §2 uses that T mod 2^W is a
bijection (`Rule30Equivalents.Odometer.G_bijective`; the record's GC808). Lemma R's light-speed ring orbits are
velocity exactly 1, which is the case `PeriodicPoints` excludes, and they are not in the kit.

**Answer in one paragraph.** Only regions that move outward at light speed against a known exterior can sustain
themselves. In the single seed's world those are exactly the two edges of the pyramid. Their order is then forced to
be periodic. Every region strictly inside the light cone, the centre column included, is fed from its left by an
exact, unmaskable input at every step. Any order it shows is order in that supply. Closed rings are the other way to
be self-sustaining, and they too are periodic; my ring work (L1066) classifies them.

## 1. The two boundaries are not alike (PROVED, elementary)

The rule is new(i) = x(i−1) XOR (x(i) OR x(i+1)).
- **Left boundary: exact transfer.** For a strip [a, b], the new cell a is x(a−1) XOR (something inside). Flipping
  the outside cell a−1 always flips it. Nothing inside can mask this.
- **Right boundary: masked transfer.** The new cell b depends on x(b+1) only through x(b) OR x(b+1). When x(b) = 1,
  the outside is shut out for that step.

So information enters from the left at full rate and moves right at exactly light speed, along its own right
diagonal. From the right it enters only through the OR.

**Consequence.** Take a region whose left end moves with speed v < 1 (v = 0 is a fixed column). At every step its left
end does not advance, it receives a fresh outside bit through the XOR. Its future is never a function of its own
contents: two worlds differing in one such outside bit give different futures inside. So **no region strictly inside
the light cone is self-sustaining, ever**, and in particular it cannot "become" so later.

Escaping the left supply needs v = 1. A strip moving right at light speed has no left input at all, since each new
leftmost cell reads only cells inside. Its only input is the right-hand OR stream, D_(−1) OR D_(−2) in diagonal
coordinates. It is **closed exactly when that stream is constant or self-generated**:
- *Constant:* the right edge band of any finite seed, against the white exterior. Diagonals 0 … W−1 depend only on
  each other (§8.27).
- *Self-generated:* a band whose own diagonals feed its input, which is a ring orbit by L1066's Lemma R.

The mirror case also holds. A strip moving left at light speed, against a white exterior on its left, reads nothing
from outside. That is the left edge band, whose left diagonals are eventually periodic (Jen; Rowland §5; JenPow2).

## 2. Self-sustained order is periodic order (PROVED)

A closed band of width W is a finite autonomous system with at most 2^W states, so its state sequence is eventually
periodic. On the right edge it is purely periodic, because T mod 2^W is a bijection (GC808), with dyadic diagonal
periods (§8.27). Ring orbits are periodic by definition. **So whatever order a region sustains on its own is periodic
order.** This is the finite-state argument GPT gives in GC2025 for closed rings, applied to the light-speed bands.

The price of width is exponential. The period of the right band of width W grows like 2^(≈0.41 W) for the single
seed (MEASURED, L1064; the half-rate external bound 1b82d8 is the proved ceiling). So the edge band sustains real order, but the order
of a wider band is ever longer to repeat. The rain pair is the only self-feeding structure that attaches to an edge,
at least for periods up to 64 (L1066).

## 3. How long an interior strip runs on its own contents (PROVED for the left end; MEASURED for the right)

`tests/probes/wolfram/strip_self_determination.py` takes the single seed's row at time 3,000, keeps a strip of width
W, makes everything outside unknown, and evolves with three-valued Rule 30. On the left an "unknown" cell genuinely
depends on the outside: by the permutivity in §1 those unknowns are exact. On the right, three-valued logic is
conservative, since it treats every unknown as independent. So the right-hand figures below are an upper bound on how
fast the strip truly loses determinacy there.

Prediction (written first): left end at speed 1, right end retreating at about 0.25, so the centre is determined
for about 0.8 W. Twelve strips (W = 64, 256 and 1,024, centred at 0, −400, −1,200 and 300) gave:
- **In all twelve strips the centre is determined for exactly W/2 steps.** It is lost when the left end, moving at
  exactly speed +1, reaches it. That half of the prediction was wrong. *Corrected (L1071, after GC2026):* W/2 is
  only an upper bound in general. A known pair 00 loses its right cell after one step; the twelve samples happen
  to attain the bound.
- **The left end moves at +1.000 in every case**, as permutivity requires.
- **The right end retreats at 0.43 to 0.57**, near 0.5 for W = 1,024, not 0.25. So the known region lasts about
  W/1.5: 41 to 43 steps for W = 64, 166 to 179 for 256 and 675 to 685 for 1,024.

**Ignorance spreads faster than damage, for this observer.** The 0.246 of §8.66 is the speed of a single
*difference* on a background, and a difference can heal. *Corrected (L1071, after GC2026–GC2029):* I wrote that an
unknown cannot heal. For the three-valued observer that is true, but genuine ignorance can heal. With cells a, 1, 0
and an unknown exterior, the middle cell is NOT r after one step and a after two, since (NOT r) OR (r OR s) = 1. More
generally F²(x)_i = x_(i−2) wherever x_(i−1) ≠ x_i. Exact knowledge can even return beyond the original interval:
a0101010 fixes cell 8 to a at time 8 for every exterior. So the 0.5 figure is the speed of an observer that forgets
correlations, not of the exact information front. The exact limit that survives is GPT's K_t ⊆ S + t: no more cells
can be known than were known at the start, shifted right by t.

## 4. What this says about the centre and the prize

The centre column is a v = 0 region, so it is permanently supplied from its left. A periodic centre would therefore
need the supply to be exactly the forced word x(t, −1) = c(t+1) XOR (c(t) OR x(t, 1)), at every step, forever.
- That is the prize problem restated, not progress on it.
- It does say where any proof has to look: at the supply, not at the region.
- The record's "wheel" results (fixed-depth forcing, Proposition 7) are statements of exactly this kind.

The similarities GPT points to are real, but they are not interchangeable:
- *Ancestry reconstruction:* the white-right past copies finite patches because diagonals are periodic. That is the
  right edge band's closure, read backwards.
- *The crystallisation fronts:* GPT's GC2019–GC2022 show the boundary between ordered periodic backgrounds and the
  irregular middle.
- *Ring orbits:* these are closure by self-feeding.

All three are faces of one fact: order lives where a region is closed, and closure happens only at light speed.

## Status

| Claim | Status |
|---|---|
| §1 boundary asymmetry, no interior region is closed | PROVED, elementary, standard |
| §1 closed exactly at light speed against a constant or self-generated exterior | PROVED, elementary |
| §2 closed means periodic; purely periodic on the right edge | PROVED, from GC808 and §8.27 |
| §3 centre determined for at most W/2 steps | PROVED, by the left end's exact speed (equality held in all 12 strips; not general, L1071) |
| §3 right end retreats at about 0.5 | MEASURED for the three-valued observer only; exact knowledge can heal (GC2026, L1071) |
| §4 | reading, not a theorem |
