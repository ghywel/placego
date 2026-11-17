# The field on real bodies: predictions, written before any score (2026-09-27, 16:40)

The first real content with an independent answer key: two hours of children playing, the shipped recommendation's
field (FLOW_H_AB, 2-px cells) beside Apple Vision's 2D skeleton on the same frames (partydata.py has the recording).
Vision is a neural pose detector with no block matching in it, so where the two agree it is not by shared failure.
Its own noise is the floor of the comparison, and is measured first (P0).

Every figure below comes from synthetic scenes with an analytic answer (NFRAME-LIMITS.md; WHAT-IT-CAN-MEASURE.md).
These are the transfers to real content that were assumed and never shown.

- **P0 (the instrument).** Vision's frame-to-frame joint jitter, taken where the field says the region is still
  (|f| < 0.3 px), is 1-3 px RMS at 1280x960. Below about twice that, a comparison measures Vision, not the field.
- **P1 (velocity, the middle band).** At 4-16 px/frame, the field sampled at a joint and projected on Vision's
  displacement:
  - torso joints: gain 0.85-1.0 (the synthetic textured rigid reads 0.97-1.0; clothes have less texture);
  - wrists: gain 0.6-0.9 (a hand is a few cells, moves fastest, blurs and deforms).
- **P2 (fast).** At 24-48 px/frame, wrist gain falls below 0.6. It degrades gradually: there is no snap to zero,
  because the fast pan's snap at 36 px was fine PERIODIC texture at the coarse level's Nyquist, and bodies are not
  that.
- **P3 (occlusion).** During a crossing (two torsos overlap), the joints of the child behind carry at least twice the
  gross error rate of joints outside crossings. At an occlusion the field follows the front surface.
- **P4 (depth: the tensor's first real score).** The field's divergence pooled over a child's torso (a robust affine
  fit) against Vision's scale rate, 2 d ln(ruler)/dt:
  - correlation of at least 0.5 over approaches and retreats;
  - gain 0.7-1.1 (THREEDIMENSIONAL.md 2.2: div = 2 sigma, sigma = -Z'/Z; the synthetic tensor read 93%).

A refuted prediction is kept, with the reason, beside the result.

## Scored (2026-09-27, evening; NFRAME-LIMITS.md "The field on real bodies", THREEDIMENSIONAL.md 9.8)

- **P0: MET in the median.** Median 0.8-1.1 px, p90 2.4-3.2 px, with a heavy tail (left/right swaps, lost
  detections). On bone midpoints the floor is 0.4 px.
- **P1.**
  - Torso: REFUTED, 0.69-0.72. The bench's exact truth on rendered children reads 0.86-0.90; the gap is real
    content plus the answer key's noise.
  - Forearms: MET, 0.71-0.75.
  - **The joints were the wrong points.** A joint sits at a limb's end or edge, so the scoring moved to bone
    midpoints.
- **P2: MET on the gain** (0.62 at 24-28 falling to 0.31 at 42-50 px/frame). **REFUTED on the mechanism:** the loss is
  a growing share SNAPPING to near zero (22% -> 42%, 84% by 64-90), as on the fast pan, not a gradual shrink.
- **P3: re-posed.** Whose motion the field reports where two torsos overlap: the front child's, 70-73% of the time.
  The 2x joint ratio was not scored.
- **P4.**
  - Sign: MET (divergence 79%, curl 90%, on clear motion).
  - Divergence gain: REFUTED (0.54 pooled, 0.55-0.64 raw).
  - Curl gain: MET on the raw field (0.89-0.91).
  - The first truth, the body ruler's log rate, failed as an instrument: it moves when an arm rises. depth.py is
    kept to show it.
- **Hypotheses added while scoring, with their verdicts.**
  - H1: the gain rises with a child's size (the coarse search's thin-limb blind spot). REFUTED: flat over rulers of
    90-2000 px.
  - The halo dilutes small bodies' tensors. Only under 110 px.
