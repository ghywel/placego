# The ruler is universal: every finite seed's right edge is the single seed's ruler, cut off at one depth

Local (Claude on the M5), 27 October 2026, L1001. This continues [One rule behind the map](rule30-run-rule.md) (L1000),
and was led by the warm pull from its Theorem E: the first level of the owner's ruler holds for every seed. Do all the
levels?

**Status.** Theorem U below is proved by hand for every finite nonzero row. Its ingredients are:
- GC808's 2-adic edge map, credited there to Coven, Pivato and Yassawi (2007);
- 8.73's Proposition 23, proved by hand and second-read (PROOFS.md entry 36);
- one new lifting step.

The exact guard `tests/probes/wolfram/universal_ruler_check.py` replays Theorem U on all 16,383 seeds of width up to
14, at every emission over 1,200 steps: ALL CHECKS PASS, exit 0, 8.3 s. Two exploratory looks, run with predictions
written first, led to it: `edge_levels_look.py` and `edge_hierarchy_look.py`. This is single-party work, awaiting GPT's
carrying read. CPY's paper was not re-read for this note, so no novelty is claimed; the truncation statement was not
found in the record.

## 1. In words

At the right edge of any finite starting row, Rule 30 emits a white triangle every two steps (L1000, Theorem E). For
the single black cell, the triangles' widths form the owner's ruler, 2, 3, 2, 5, 2, 3, 2, 6, …, with the width at time
t set by how many times 2 divides t (8.73).

**Every other finite starting row does the same thing, until it stops.** Its edge emits exactly the single cell's
ruler, shifted in time, up to some depth. From then on, wherever the single cell would emit a triangle that wide or
wider, it emits one of a fixed width instead. That width always falls in a gap of the ruler: 1, 4, 7, 9, 10, 11, 12,
13, 16, … are possible, while 2, 3, 5, 6, 8, 14, 15, … are the single cell's own values.
- *Rain edges (L1000)* are the first cut: every width is 1.
- *The single cell's ruler is the longest edge there is.* Every other edge is a truncated copy of it.

The depth at which a row stops is a number read from its own edge cells: how far the row's edge code agrees with the
single cell's cycle (section 2).

## 2. Setting (GC808)

For a finite nonzero row x with rightmost black cell e, define its edge code
R(x) = Σ_(k ≥ 0) x(e − k) 2^k, an odd positive integer, so bit k is the cell at distance k from the edge.
- *One step.* The edge advances one cell per step (Theorem E), so R(F(x)) = T(R(x)) with T(R) = R XOR (2R OR 4R).
  Proof: the new bit k is old bit k XOR (old bit k−1 OR old bit k−2), which is the rule read at distance k.
- *Readout (Theorem E).* An emission happens at time t exactly when bit 1 of R_(t−1) is 1. Its width ω(R_t) is the
  number of zero bits between bit 0 and the next 1.
- *The single seed's cycle.* Its code is R = 1. Let p_k be the period of T^s(1) mod 2^k and
  C_k = {T^s(1) mod 2^k : s ≥ 0} its cycle; p_1 to p_40 are
  1, 2, 2, 4, 8, 8, 16, 32, 32, 64, 64, 64, 64, 64, 64, 128, 256, …. These are A094605's diagonal periods, with
  p_k the period of diagonal k−1.
- *Doubling levels.* Call k a doubling level when p_k > p_(k−1). Below 40 they are 2, 4, 5, 7, 8, 10, 16, 17, 25, 26,
  28, 30, 35, 37, 38 and 40.
- *Depth.* For an odd R0 let k*(R0) be the largest k with R0 mod 2^k in C_k, or ∞. Every odd residue mod 4 is in
  C_2 = {1, 3}, so k* ≥ 2.

## 3. Theorem U and its proof

> **Theorem U.** Let x be a finite nonzero row with edge code R0 and depth k* < ∞. Then k*+1 is not a doubling level.
> Take s0 with T^s0(1) ≡ R0 (mod 2^k*). For every t ≥ 1:
> - x emits at time t exactly when the single seed emits at time t + s0;
> - when it does, its width is the single seed's width at t + s0 if that is less than k* − 1, and exactly k* − 1
>   otherwise.
>
> If k* = ∞, its widths are the single seed's, shifted by s0.

**Lemma U0 (triangularity; the isometry of GC808).** If R and S agree on bits 0 to k−1 and differ at bit k, then so do
T(R) and T(S).

*Proof.* Bit j of T(·) depends only on bits j, j−1 and j−2. Below k they agree, and at bit k the XOR passes the
difference straight through. ∎

**Proof of U.**
1. *k*+1 is not a doubling level, and R0 ≡ T^s0(1) XOR 2^k* (mod 2^(k*+1)).*
   - T mod 2^(k*+1) is a bijection that maps the 2·p_k* lifts of C_k* among themselves, and the single seed's orbit
     mod 2^(k*+1) has length p_k* or 2·p_k*.
   - If 2·p_k*, it covers every lift, so R0 mod 2^(k*+1) would lie in C_(k*+1), contrary to the definition of k*. So
     k*+1 is not a doubling level, and the orbit takes exactly one lift of each point of C_k*.
   - T^s0(1) mod 2^(k*+1) is one lift of R0 mod 2^k* and lies on that orbit. R0 does not, so it is the other lift,
     differing at bit k* alone.
2. *For every t ≥ 0, R_t ≡ T^(t+s0)(1) XOR 2^k* (mod 2^(k*+1)).* This is Lemma U0, applied step by step.
3. *Timing.* Since k* ≥ 2, bit 1 of R_(t−1) equals bit 1 of T^(t−1+s0)(1), so the two emit at the same times.
4. *Width.* Write ω′ for the single seed's width at t + s0.
   - *If ω′ < k* − 1,* the single seed's next 1 after bit 0 lies below bit k*, where the two codes agree, so the widths
     are equal.
   - *If ω′ ≥ k*,* bits 1 to k* of the single seed are 0. The row's bits 1 to k*−1 are therefore 0 and its bit k* is
     1, so its width is exactly k* − 1.
   - *ω′ = k* − 1 never happens.* Proposition 23 (8.73) gives the single seed's widths as
     w(v) = min{j : p′_j > 2^v} − 1, with p′_j the period of diagonal j, which is p_(j+1) here. So every width the single
     seed emits is (a doubling level) − 2, and k* − 1 = (k*+1) − 2 with k*+1 not doubling. ∎

**Corollaries.**
- *The rain edge is k* = 2.* The level-3 split is GC808's two cycles mod 8: {1, 7} is the single seed's, {3, 5} its
  twin. That is L1000's one-bit rule (Theorem E, item 5), now explained.
- *Every frozen width is realized.* The possible depths are k* ∈ {2, 5, 8, 10, 11, 12, 13, 14, 17, …}, one less than
  each non-doubling level. Each is the depth of a finite seed, because every odd residue is a finite seed's edge code.
  The frozen widths are therefore exactly {1, 4, 7, 9, 10, 11, 12, 13, 16, …}: the gaps of the single seed's ruler.
- *Levels 2 and 3 by hand (L1000's draft, consistent).*
  - Among widths of at least 3, a 3 follows every width of at least 4, and a width of at least 4 follows every 3. In
    U's terms, every half-ruler has k* ≥ 5.
  - The stream of widths of at least 4 is either constantly 4 (k* = 5) or always at least 5 (k* ≥ 8).
- *Rows of the single seed's own picture have k* = ∞.* Any later row of the single cell has the code T^τ(1). The guard
  found 56 seeds of width up to 14 that agree to 40 bits.

## 4. What this means for the map

The owner's founding observation, the ruler on the right edge, is a general law. **Every finite starting row of Rule 30
has the same edge as the single black cell, truncated.** The truncation depth is a single number read from the row's
own edge cells. The variety among right edges is exactly one integer, k*, together with a phase.

It does not touch the centre column. The centre sits ever deeper behind the edge (8.73's closing caution), and nothing
here says what happens there.

## 5. Next, by warm pull

1. **The left edge.** The left side is the XOR side, Jen's band with power-of-2 periods. Is there the same statement:
   every finite seed's left edge equals the single seed's band, cut off at one depth? The left strip is autonomous too
   (a cell at distance d depends only on distances d−2 to d).
2. **Rain edges inside the picture.** Rain edges (k* = 2) emit lone white cells for ever. What does the region behind
   such an edge look like? Is it a rain patch, a staircase whose front never catches up?
3. **Where k* comes from.** Can k* be read directly from a seed's cells by a short rule, as k* = 2 is read from two of
   them?


## Independent review checkpoint — GC1935

[GPT's full carrying review](rule30-structure-unification-gpt-review.md) accepts the scoped local run/patch/bridge/edge statements and finite-depth capped-width theorem. Read its qualifications before using the earlier broad prose: singleton agreements and odd tips, bounded-run conventions, emitted widths versus whole edges, and compatible finite phases versus one ordinary integer at infinite depth. No numerical rerun or novelty claim. Original text retained; this review is the current scope checkpoint.

## 6. Amendments after GPT's review (GC1935), and the infinite-depth question (L1002)

[GPT's review](rule30-structure-unification-gpt-review.md) carries Theorem U for every finite depth k*, with its
lifting step and the permanent cap.
- **GPT's direct gap proof is the better one; adopted.** At time u, let j be the first set bit of T^u(1) above bit 0.
  Then p_j divides u and p_(j+1) does not. So level j+1 doubles, and the width j − 1 is (doubling level) − 2. This
  needs no translation of Proposition 23's diagonal indices.
- **Periodicity.** With a finite cap the emitted sequence depends only on bits 0..k*. It is purely periodic, with period
  dividing p_k*, and has no transient.
- **What "the same edge" means.** The theorem classifies the emission timing and widths, not the whole edge region:
  bits above k* are unconstrained.
- **Counts.** The 16,383 inputs are presentations, not distinct codes: zeros padded on the left repeat a code. The 56
  cases at KMAX are depth at least 40, not certified infinite. GPT's accounting shows they are exactly the
  presentations of T^tau(1) for tau = 0..6: 14 + 12 + … + 2 = 56. U3 checks observed exclusions only; the hand proof
  covers the rest.
- **Infinite depth: section 3's last sentence is restated.** When k* = ∞ the proof gives compatible phases s_k mod p_k
  at every depth, an inverse-limit phase. It does not give one ordinary time shift. The corrected statement: every
  finite window of the edge agrees for ever with the single seed's history at the corresponding phase s_k. The
  ordinary-shift form needs the assertion below.

**Assertion A (GC1935's obligation), open.** Every finite edge code in the closure Ω of the single seed's orbit is
T^tau(1) for some tau ≥ 0.

What L1002 adds, all by hand except the last item:
- **The predecessor of a finite code.** If R is finite with top bit d, then T^−1(R) is either finite with top bit d − 2,
  or all ones from bit d+1 on at the latest. Above d the backward recurrence is q_j = q_(j−1) OR q_(j−2), so it is
  finite exactly when q_(d−1) = 0 and q_(d−2) = 1.
- **The single seed's past is the tower.** T^−1(1) = −1, the all-black row: the cap. T^−2(1) = …1001001, the
  001-periodic row (GC1932's bridge layer). T^−3(1) is 1 followed by 110 repeated, so only its tail has period 3, with
  two 1s per period (the 101 layer; GC1936's correction). So GC1932's backward
  tower is the single seed's 2-adic past, visible at the edge at the times p_k − j.
- **Cap formula (the dual of GPT's gap proof).** The edge black run at time u has length at least L exactly when p_L
  divides u + 1, because T(−1) = 1.
- **Reduction.** Descending T^−1 from a finite point of Ω either reaches 1 or enters an eventually-all-ones point. So A
  holds if and only if −1 is the only eventually-all-ones point of Ω. In the picture: in the single seed's rows, a long
  black run near the right edge always touches the edge cell. By compactness, black runs that start at a fixed distance
  without touching it must then have bounded length.
- **Evidence** (`tests/probes/wolfram/closure_finite_look.py`):
  - all 8,388,608 odd codes below 2^24 were tested to depth 44, and only T^0(1) to T^11(1) pass;
  - over 131,071 rows no non-edge black run starting within distance 41 of the edge reaches bit 63;
  - the longest such runs are at most 19 cells.
  - A finite search, not a proof.


## Independent review of L1002 — GC1936

[GPT carrying review](rule30-finite-closure-gpt-review.md) accepts the finite-predecessor dichotomy, both directions of the reduction, fixed-offset compactness equivalent and cap formula. A remains open. The third predecessor is an initial1 followed by110 repeated when read low-bit-first; it is eventually period3, with a boundary defect. Each fixed offset needs its own all-time bound, not one bound for all offsets. A/B numerical predicates are printed only in the current source; a zero exit certifies the C predicates, not all reported outcomes. No rerun.
