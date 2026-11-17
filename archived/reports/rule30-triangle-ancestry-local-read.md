# Triangle ancestry: Local's read of GC1932, and the first hand checks between the patterns

Local (Claude on the M5), 26 October 2026, L998. This answers GPT's handoff in
[rule30-triangle-ancestry-handoff.md](rule30-triangle-ancestry-handoff.md) (GC1932, DQ-020).

**Status.** Everything below was derived by hand first. One exhaustive guard,
`tests/probes/wolfram/triangle_parents_check.py` (2.3 s on the M5), replays the finite statements: ALL CHECKS PASS. It is
single-party work awaiting GPT's targeted read. Every statement is elementary, about local Rule 30 steps and about the
uniform (fair-coin) row measure, which Rule 30 preserves (8.68, C5). Nothing here is a statement about the single seed's
orbit, a bound for all depths, or a prize step. No novelty is claimed; section 1 says what the record already had.

Convention as in GC1932: space left to right, time down, white = 0, black = 1, f(L,C,R) = L XOR (C OR R).

## 1. GC1932 carries

I re-derived each carrying step before comparing with GPT's text.

- **Erosion and the tip (GC1932 §2).** A maximal white run of length n ≥ 2 loses one cell at each end: x'(a) = 1 XOR 0 = 1,
  x'(b) = 0 XOR 1 = 1, and the interior keeps three white parents. An isolated white cell has neighbourhood 101 and stays
  white. *Carries*, including GPT's correction of its own shorthand. The persistence is already in the record (GC847, rain
  stacks), and section 3 below gives its general form.
- **The cap windows (§3).** Above a white run [a, b], y(k) = 0 means x(k−1) = x(k) OR x(k+1), so the parent is driven
  right to left by the pair (x(b), x(b+1)), which leaves three shapes (section 2). The two non-inherited nine-cell
  windows 111111110 and 111111101 over 100000001, the outside zero on the left, the extra outside zero on the right for
  the first window only, and the impossibility of nine upper ones (its last cell has 11 above it, so it outputs 0) all
  check. *Carries.* Prior record: 8.82's lemma "what lies above a zero run" is the same three shapes in wall coordinates.
- **Black runs (§3).** The triples that output 1 are 001, 010, 011 and 100. As pair edges they are 00→01, 01→10, 01→11 and
  10→00, and 11 has no outgoing edge that outputs 1. So the parent of a black run is 001-periodic, with at most one
  departure (011) at its right end. *Carries.* Prior record: 8.82 ("black runs to period-3 patterns one phase over").
- **Pair maps and block maps (§4).** I recomputed T_0 and T_1 entry by entry and composed the block maps:
  001: (00, 01, 10, 11) → (11, 00, 11, 11); 101: → (01, 10, 01, 01); 101000: everything → 01. *Carries.* The reconstructed
  interiors also carry: 101 under a 001 strip, the period-6 pair 101000 / 000101 under a 101 strip, and 101110 under
  101000.
- **The chain (§5).** I re-listed all eighteen parent neighbourhoods of the first three transitions, then checked
  001001 → 111111 → 000000. *Carries.*
- **What I could not find in the record:** the §4 block-map tables and the §5 chain words. The record searches for
  101110, 110010 and 011100 hit only unrelated words. They are the in-tree of the all-white row on period-6 rings,
  which 8.67's ring census enumerated without naming it.

## 2. Hand lemma 1: every white run has one of three parents, in the ratio 1 : 1 : 2

**Statement.** Let [a, b] be a maximal white run of length L ≥ 1 in the row y = F(x), black at a−1 and b+1. Then the
row above has exactly one of three shapes:

| Shape | Row above, on the cells shown | What it is | Fair-row probability |
|---|---|---|---|
| **C** | 1 0^(L+2) 1 on [a−2, b+2] | continuation: a run two cells wider, shrinking | 2^−(L+4) |
| **A** | 0 1^(L+1) 0 0 on [a−2, b+2] | a new cap: a black run one cell wider than the triangle | 2^−(L+4) |
| **B** | 0 1^L 0 1 on [a−2, b+1] | hung: a lone white cell sits above b, with a black run of length L on its left | 2^−(L+3) |

**Proof.** The zero condition gives the three shapes on [a−1, b+1], according to (x(b), x(b+1)) = 00, 1·, 01. The two
black ends then fix the rest:
- y(a−1) = x(a−2) XOR (x(a−1) OR x(a)) = 1 forces x(a−2) = 1 in C, and x(a−2) = 0 in A and B;
- y(b+1) = x(b) XOR (x(b+1) OR x(b+2)) = 1 forces x(b+2) = 1 in C, x(b+1) = x(b+2) = 0 in A, and nothing more in B.

The three windows are disjoint. Under the fair measure each has the probability of its specified cells, and the three
sum to 2^−(L+2), the probability of the run itself. That is a consistency check on invariance. ∎

**What it connects.**
- *The owner's cap observation.* The cap "ends above its rightmost cell" is shape A; "ends one cell earlier" is shape B.
  The lemma says these are the only two ways a triangle is born, and that **B is exactly twice as common as A at every
  width** under fair rows. That is a prediction anyone can check by eye on a picture. Note that in B the cell above the
  triangle's right corner is white.
- *The 8.68 triangle law.* 8.68's "tops" are A and B together: 2^−(L+4) + 2^−(L+3) = 3·2^−(L+4) per cell. That is 8.68's
  law, now with its two parts named. 8.68 derived it as "maximal run minus continuation". The lemma derives the same
  number from the parents, so the two derivations agree.
- *GC847's width-1 distinction is the case L = 1.* There, B with L = 1 is a persisting singleton, which GC847 counts as
  the same stack. That is why GC847 found stack births at 1/16 but width-1 tops at 3/32.

**Consequence for GC1932's item 2, the counting convention.** With white cells joined vertically and horizontally
(4-connectivity), only in shape A does the new run have no white cell above it. **Two thirds of 8.68's tops of every
width are not new objects.** They hang from a lone white cell of an earlier structure. A census of "independent triangles" must count A
alone (2^−(L+4) per cell), or else say that it counts A and B together.

## 3. Hand lemma 2: how one triangle hangs the next

**Statement (every row).** Suppose x(c) = 0 is a lone white cell, x(c−1) = x(c+1) = 1, and the black run ending at c−1
is [p, c−1], with x(p−1) = 0. Then the next row is white exactly on [p+1, c], and black at p and at c+1. *A lone white
cell turns the black run on its left into a white run of the same length, which ends below the lone cell.*

**Proof.**
- y(c) = 1 XOR (0 OR 1) = 0, and y(c+1) = 0 XOR (1 OR ·) = 1.
- For p+1 ≤ k ≤ c−1, y(k) = 1 XOR (1 OR ·) = 0, because x(k−1) = x(k) = 1.
- y(p) = 0 XOR (1 OR ·) = 1. ∎

GC847 has the one-cell case, its left neighbour becoming the complement of the cell two to the left. More generally,
any black run of length m produces a white run of length at least m − 1 below it, shifted one cell right, because 11
above a cell always gives 0.

**The life cycle, in words.** A white triangle of odd width ends in a single white cell. That cell never dies at once:
on the next row it becomes the right corner of a new triangle, as wide as the black run on its left. A triangle of even
width ends in a pair, and the pair turns black, so its line ends there. So white triangles come in lineages through
their odd tips. That is the owner's "older triangles in the ancestry", in exact form: in shape B the older structure's
tip *is* the new triangle's top-right parent.

**Hand lemma 3: the child's width, first generation (fair rows).** Condition on an odd tip: a white triple flanked by
black, 1 0 0 0 1 on [c−2, c+2], with every other cell fair. Then **the child hung at c has width k with probability
exactly 2^−k**.
- *Proof.* At the next row, cell c−1 is black. Cell c−2 is NOT x(c−3), cell c−3 is NOT x(c−4), and each cell further
  left takes in a fresh fair bit through the XOR, by left permutivity. So the black run's length past c−1 is
  geometric. ∎
- *Check.* K4 counts 16384, 8192, 4096, … over all 2^15 left parts, exactly.
- *What it means.* Half the time the child is a single cell again (GC847's stack continues). A quarter of the time it is
  a pair, and the lineage ends. In all, the child is even, and ends the lineage, with probability 1/3. **Independence
  across generations is not proved:** a second generation's left cells overlap the first generation's conditioning.

**GC1932's item 4 answered for the simplest description: no.** A triangle's own visible geometry (width, position,
phase, flanking black cells) does not predict its next event. Hand pair, verified by replay; cells c−5 … c+4 at time s:

    H1:  0 0 1 1 0 0 0 1 1 1    child of the tip: width 1 (a lone cell again)
    H2:  0 0 0 1 0 0 0 1 1 1    child of the tip: width 3

The two rows have the same triple at [c−1, c+1], the same black cells at c−2 and c+2, and the same tip at s+1. They
differ only at c−3, two cells left of the white run. **The quantity that decides is exact and lies outside the
triangle:** the length of the black run on the tip's left, one row after the tip forms. A compressed description that
keeps the triangles and drops their left neighbours is refuted by this pair.

## 4. How much of an ancestral row is forced (GC1932 item 3)

**The general accounting (hand).** Under a periodic target strip w repeated k times, the row above is reconstructed
right to left. It is the orbit of the unknown right-end pair under the block map B_w, a self-map of the four pairs.
- Every orbit of a self-map of four points enters a cycle within three steps. So the uncertain right margin is at most
  three blocks of the current period.
- The interior row above is one of the cycle points' templates: a cycle of length l gives l templates of period l·|w|,
  shifted from one another.
- The interior is forced only when B_w has a single fixed point that attracts everything. The left end of the strip
  gains one cell, because reconstruction needs no input from the left.

Both T_0 and T_1 send the pairs 10 and 11 to the same pair. When the reconstructed cell is black, the OR hides the bit
on its right. So the backward forgetting of the right boundary is 8.38's OR-mask merging, read in reverse: the boundary
is forgotten exactly where black cells appear.

**The chain, two levels further back than GC1932, and its first branching (hand; K1):**

| Target row w | B_w on (00, 01, 10, 11) | Cycle points | Row(s) above, interior | Transient (blocks) |
|---|---|---|---|---|
| 001 | 11, 00, 11, 11 | {11} | 101 | ≤ 2 |
| 101 | 01, 10, 01, 01 | {01, 10}, a 2-cycle | 101000 or 000101 (a phase bit) | ≤ 1 |
| 101000 | 01, 01, 01, 01 | {01} | 101110 | 1 |
| 101110 | 10, 01, 01, 01 | {01} | 110010 | ≤ 2 |
| 110010 | 00, 00, 00, 00 | {00} | 011100 | 1 |
| 011100 | 00, 11, 11, 11 | {00}, {11} | 001000 or 100111 (a pattern bit) | ≤ 1 |

So, read forward:

    001000 or 100111 → 011100 → 110010 → 101110 → 101000 → 101101 → 001001 → 111111 → 000000

On the 6-ring this is the whole in-tree along that branch. 011100 has exactly the two preimages shown, and 101000,
101110 and 110010 have one each (K1).

**The cap itself.** Take the cap window of shape A, 0 1^(L+1) 0 0. Reading it right to left, the two zeros send every
pair into {00, 11}, and then T_1 runs the 001 cycle. **So the row above the cap is 001-periodic across the cap's whole
width, in one of two phases.** The phase is decided by one boundary bit: whether cells b+2 and b+3 of that upper row
are both white. In the other phase the strip ends with the 011 departure.

**Reading.** Above a large shape-A triangle sits a tower of periodic templates. Each template is forced on a strip that
loses at most three blocks of its period on the right and gains one cell on the left at each level up. Its only
freedom is a bit at the levels whose block map has two cycle points: a phase bit at the 101 level and a pattern bit at
the 011100 level. How high the forced tower reaches for a triangle of width L is a finite hand computation from the
table. I have not packaged it as a bound.

## 5. The cap as an alignment: the owner's resonance image in exact words

In the chain the large white run's ancestry runs, from oldest to newest:
- *101000:* white triples and lone white cells.
- *101101:* the triples have become lone cells (shape C tips), and the old lone cells persist (shape B, L = 1).
- *001001:* each lone cell has hung a white pair from the length-2 black run on its left (shape B, L = 2).
- *111111:* every pair ends together, leaving a solid black row.
- *000000:* that black row is the cap of a triangle as wide as the strip.

This is general, not peculiar to the chain. The row above any black run is 001-periodic. Its white cells come in pairs
three cells apart, each pair a run of width 2 that dies on the next row. So **a black cap is a lattice of small white
triangles all ending in even pairs on the same row.** An odd ending would leave lone white cells, and those persist
(lemma 2). The alignment is literal: synchronised even endings. It is not a wave, and no energy is involved.

## 6. Hand checks proposed for the next round (for GPT and the owner)

1. **Second-generation independence (lemma 3).** Is the lineage's sequence of child widths an exact renewal process
   under fair rows, or do the overlapping left cells correlate consecutive generations? A hand light-cone argument
   first.
2. **The forced tower's height.** For a shape-A triangle of width L, compute the forced height from section 4's
   transients by hand, for one L, perhaps 12. Then decide whether a small exhaustive check is worth it.
3. **Continue the in-tree beyond the branching.** Take 001000 and 100111 two levels further back. Is the period doubling
   at the 101 level a one-off, or does it recur?
4. **Where 8.68's single-seed deficit lives.** Its −0.09 % deficit of width-1 tops in the left part of the core is
   either in shape A (new singletons) or in shape B (persisting ones). That needs data, and it would be a measurement
   with predictions written first, not a hand check. Proposal only.
5. **A description that does predict (item 4, the positive side).** Lemma 2 says the triangle plus the black run on its
   tip's left decides the next event exactly. What is the smallest left neighbourhood, at the triangle's birth row, that
   decides its whole lineage for g generations? A hand count for g = 1 and 2.

No experiment, run or schedule follows from this document without the owner's word.

## 7. Amendments after GPT's review (GC1933, adopted in L999)

[GPT's review](rule30-triangle-ancestry-gpt-review.md) carries sections 2 to 4 at their stated scope. The text above is
kept as written; these amendments govern where they differ.
- **The deciding black run, section 3.** It lies in the same row as the lone white tip, one update after the white triple.
  "One row after the tip forms" was one step late.
- **The margin, section 4.** Three blocks bound the transient of the backward map. They do not bound the phase or
  pattern choice that survives across the whole interior when B_w has more than one cycle point.
- **The masking, section 4.** T_0 and T_1 merge exactly the pairs 10 and 11: a black centre hides its right neighbour.
  "The boundary is forgotten exactly where black cells appear" was too broad; T_0(01) = 10 and T_0(11) = 11 remain
  different.
- **The scope of K4.** K4 asserts widths 1 to 10 only, and censors children that run off its window. The law for every k
  rests on the hand proof in section 3.
- **The 2^−k law.** It is for the fixed-time conditioning stated, a 10001 window with every other cell fair. It is not
  yet a law for a tip reached by following a lineage. The 1 : 1 : 2 split is an exact fair-row count, not a measured
  frequency in the single seed's picture.
- **The cap and the band, sections 4 and 5.** The cap's endpoints and the 011 departure stay part of the statement. A
  black band's parent is a periodic lattice of white pairs in its interior, not in every bit of the actual row.
- **Exit status.** `triangle_parents_check.py` now exits nonzero on failure. Its totals and runtime remain this worker's
  report; GPT did not rerun it.
