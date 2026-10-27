# Every staircase in the single cell's picture ends

Local (Claude on the M5), 27 October 2026, L1007. Answers DQ-021's open question (L999 §6, item 1) for the prize's own
seed.

**Status.** A hand theorem from three known ingredients:
- the front lemma (GC847, L999; carried by GPT in GC1935);
- the light cone;
- the periodicity of the single seed's edge code modulo 2^k (GC808; L1001).

The replay `tests/probes/wolfram/staircase_end_check.py` checks its ingredients and its explicit bound where the bound
is small: ALL CHECKS PASS. This is single-party work, awaiting GPT's read. No novelty is claimed; no prior statement of
it was found in the record (searches in the script's header).

## The theorem

> **Theorem S.** In the single black cell's picture, every staircase ends. Precisely, let a maximal alternating stretch
> (a patch of the 0101 "rain") of length at least 3 have its left end, the front, at distance W from the right edge at
> time t0.
> - If W ≥ 2, the stretch is dead (its continuation has length below 3) by the first time t1 ≥ t0 that p_(W+2) divides.
>   Here p_k is the period of the single seed's edge code modulo 2^k: 1, 2, 2, 4, 8, 8, 16, 32, 32, 64, …
> - If W ≤ 1, it is the pattern 0,1,0 around the edge cell at an emission, and it dies on the next step.

**Proof.**
1. *The front moves at light speed.* While the stretch has length at least 3, its front advances exactly one cell per
   row (the front lemma). The right edge also advances exactly one cell per row (Theorem E). So the front's distance from
   the edge stays exactly W for the stretch's whole life.
2. *The stretch is pinned to the edge.* Beyond the edge every cell is white, so an alternating stretch reaches at most
   one cell past the edge. While it lives it therefore lies within distances −1..W of the edge.
3. *The edge region goes blank.* p_(W+2) is the period of T^s(1) modulo 2^(W+2), so at every multiple t1 of it,
   T^t1(1) ≡ 1. Then the cells at distances 1..W+1 are all white.
4. *So it cannot be alive at t1.* If W ≥ 2, a stretch of length at least 3 within distances −1..W with its front at W
   contains two adjacent cells at distances 1 or more. Those are both white at t1, so they do not alternate.
5. *The edge case.* If W ≤ 1, the only possibility is 0,1,0 at distances 1, 0, −1, an emission time with the edge black
   run of length 1. On the next step the edge black run has length at least 2 (Theorem E), so the old edge cell and the
   new one are both black and the stretch is broken. ∎

## What it means

- **For the owner's question.** Every staircase you can see in the single cell's picture finishes. Its eating front runs
  at the same speed as the picture's right edge, so a staircase can never get away from the edge. And the edge region is
  wiped white each time the edge emits a big triangle.
- **The same argument is wider.** By the patch rule P, the left end of any patch of at least two cells moves right at
  exactly one cell per row, so every patch is pinned within a fixed distance of the right edge. Hence, in the single
  cell's picture, every patch of any history whose rows have no two adjacent white cells is finite-lived. Rain is the
  main example. Patches of all-white, the triangles, die on their own schedule.
- **Other seeds.** For a finite seed of depth k* (L1001), the edge emits width k* − 1 in its deep slots. So stretches
  with W ≤ k* − 2 die by the same argument. Stretches further from the edge are not controlled; that case is open. Seeds
  of infinite depth behave like the single cell.
- **The bound is real but loose.** For stretches near the edge it is small and observable: all 4,438 with W from 2 to 20
  died by it. For stretches in the core, W is of order t and p_(W+2) is astronomically large. They die much sooner in
  practice; in the window the longest lasted 43 rows. The theorem gives finiteness, not a useful lifetime.

## What it does not do

It says nothing about the centre column. And it concerns rain patches, not the period-two clock: a clock is a property
of one column, not an alternating stretch along a row.
