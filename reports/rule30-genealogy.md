# Genealogy beside the colour: what a cell could record, and what it shows

*Local, L1279, 1 November 2026, at the owner's direction. Builds on GPT's GC2351 (the 1..8 parent labels) and
Local's L1278 (where the row already keeps each cell's parents).*

## 1. The owner's question

The owner, 1 November 2026: "what extra information can we encode alongside a cell's color which enriches our
information space, relieves forgetting and provides numeric/algebraic pathways that can be independent of or
combined with the ameliorating logic gates. ... Too much information and the cell becomes bloated, too little and it
becomes less useful." And: "the problem space is algebra not a fixed rule automaton ... is there algebra that we are
missing, and a cell recording it's ancestral state gives us a basis to make runs and observations without solely
considering logic gates."

Orientation throughout: x_i(t+1) = x_(i−1)(t) XOR (x_i(t) OR x_(i+1)(t)), the single seed at 0. In algebraic normal
form over GF(2), Rule 30 is f(a, b, c) = a + b + c + bc, where a, b and c are the left, centre and right parents.

## 2. Where we start (L1278)

The single-seed row never loses its past, because a finite row determines every earlier row (G121). The parents of
a cell are written in the children to its right, and G13's four-state reader recovers them. On the actual orbit they
are fixed within a median of 8 cells, the same as for fair-coin rows. So a record kept beside the colour adds no
information to the whole row. It can add **locality**: what is known at the cell itself. It can also add **algebra**:
arithmetic the gates do not show.

## 3. Six schemas

Each schema is a rule run alongside Rule 30, so the extra record is updated locally, like the colour.

**S1. The lineage register (bits; the least bloat).** A cell remembers the colours of its left-line ancestors for
k generations: R_m(i, t) = x_(i−m)(t−m) for m = 1..k. It updates locally: R_1(i, t+1) = x_(i−1)(t) and
R_m(i, t+1) = R_(m−1)(i−1, t). Every past cell (j, t−m) has exactly one left-line descendant (j+m, t) in today's row.
So k bits per cell hold the previous k rows exactly, with no repetition, and any cell's k-generation family patch is
read off its 2k right-hand neighbours. PROOF-SKETCH, elementary (the left line is a bijection between rows); GPT's
read is requested. This answers the bloat
question for complete local memory: k bits for k generations is the minimum, since k rows need k bits per cell. The
owner's 1..8 label repeats each parent bit in three cells.

**S2. The flip counter (numbers).** Every cell either copies its left parent (centre and right white) or flips it
(the OR fires). The cell counts the flips on its left line:
N(i, t+1) = N(i−1, t) + (x_i(t) OR x_(i+1)(t)). Then x = N mod 2, by induction (PROOF-SKETCH, elementary;
checked on the orbit). The higher binary digits of N are
slower clocks along the lineage: an odometer driven by the OR gate.

**S3. The lift to Z/4 (algebra: the derivative is the carry digit).** Evaluate the algebraic normal form
a + b + c + bc in Z/4, with each cell holding x + 2h. The colour is still Rule 30, and the second digit obeys

    h' = h_a + (1 + x_c) h_b + (1 + x_b) h_c + κ(x_a, x_b, x_c)   (mod 2),

where κ = 1 exactly when two of the three parents are black (the carry of 1 + 1). The coefficients 1, 1 + x_c and
1 + x_b are Rule 30's Boolean derivatives. So the higher digit is driven by the tangent map (damage propagation) plus a
carry source. Over the dual numbers GF(2)[ε]/(ε²) the same calculation gives the tangent map with no κ. PROVED
(by exhaustion: the identity concerns one step, and T2 checks all 64 cases). The Boolean derivative as a tangent map, and its
Lyapunov exponent, are known (Bagnoli, Rechtman and Ruffo, Phys. Lett. A 172 (1992) 34, arXiv cond-mat/9811159).
Integer lifts of the algebraic normal form modulo N are studied in arXiv 2609.25078, which we have not read. We
found no source for the carry decomposition.

**S4. Sensitivity path counts (numbers).** P(i, t+1) = P(i−1, t) + [x_(i+1)(t) = 0] P(i, t) + [x_i(t) = 0] P(i+1, t)
counts the ways an ancestor can still influence a cell, through the inputs that are not masked. Its parity is the S3
tangent, and its growth rate is the maximal Lyapunov exponent of Bagnoli, Rechtman and Ruffo. Known.

**S5. The black family tree (genealogy proper).** Every black cell has a black parent: the four black outputs
100, 010, 011 and 001 each contain a 1. Designate one parent: L for 100, C for 010 and 011, R for 001. The black
cells then form one tree rooted at the seed, and each black cell has a single line of descent and a "surname" (its
ancestor in a chosen generation).

**S6. The wheel stamp (owner's suggestion).** Every cell right of the centre has a left line that leaves the centre
column at time t − i. Iterating the left-parent identity gives

    x_i(t) = x_0(t−i) XOR (the parity of the flips on that line).

So each right-half cell is a centre cell "printed" at time t − i and then enciphered by OR flips. S1 with k = i
carries the stamp. Every left-half cell (−d, t) is forced by columns 0 and 1 over times t..t+d (Jen's leftward
reading), so it refers to the wheel's state over that window. PROOF-SKETCH, elementary (left permutivity, iterated);
checked on sampled cells in T0.

## 4. Tests, with predictions written before the runs

Probe: [`genealogy_schemas.py`](../tests/probes/genealogy_schemas.py). Single-seed orbit to t = 1500 on the M5, a
few seconds per part.

Record searched: `record_find` for kicked wheel, Boolean derivative, damage spreading, Lyapunov, Jacobian,
dual number, Bagnoli, 2-adic lift, Z/4, flip count, family tree, coalesc, path count, plus L1278's searches. Hits:
- the wheel is §8.4–§8.57 and Theorem E, the column-1 rotation in the period-two world;
- Boolean derivatives in GC2258 and the degree law L1071;
- the moving-frame flip laws G97 and G106;
- Bagnoli is in PRIOR-ART as a survey entry only;
- DQ-010, "different pasts, one present".

No family tree of black cells and no Z/4 lift appear in the record. Known index: kit f1cb20be and the portal at
20:23Z returned no hit for "dual number", "Z/4", "2-adic lift", "damage spreading" or "Bagnoli". Literature:
Bagnoli, Rechtman and Ruffo (1992) for S3 and S4; arXiv 2609.25078 for integer lifts (search summary only).

**T1, the family tree (S5).**
- P1a: in the bulk the designated steps are L 0.25 ± 0.03, C 0.50 ± 0.03 and R 0.25 ± 0.03.
- P1b: all three founders at t = 1, the cells (−1, 1), (0, 1) and (1, 1), still have descendants at t = 1500. The
  middle founder holds between 5% and 90% of the black cells (a weak prediction).
- P1c: the distinct ancestors of the black cells in the central window |i| ≤ 100 of row 1500 thin out roughly like
  s^(−1/2), as coalescing random walks do. They reach one ancestor before the seed.
- P1d: centre-column lineages diffuse. The spread at lag s is c·√s with c in [0.5, 1.2], and the mean drift is under
  0.2 of the spread.
- Counterfactual: strongly unequal step shares, or a lineage spread that grows linearly, mean the tree hugs an edge
  and is degenerate. No thinning means lines never meet.

**T2, the lifts (S2, S3, S4).**
- P2a: the Z/4 and dual-number identities hold in all 64 cases (this is algebra; the test is a check).
- P2b: the sensitivity paths grow at a rate λ with 0.60 ≤ λ ≤ 0.72. The mean-field value is ln 2 ≈ 0.693.
- P2c: the tangent (mod 2) agrees with the actual damage from one flipped cell on the whole right-edge diagonal. In
  the bulk of the damage region they agree on 40% to 60% of cells.
- P2d: the Z/4 lift from the single seed has second-digit density 0.5 ± 0.05 in the bulk. The four (colour, digit)
  pairs each occur 0.25 ± 0.03 of the time on the centre column.
- P2e: the same holds for the flip counter's second digit.
- Counterfactual: a skewed pair frequency, or a digit that is a function of nearby colours, would be hidden structure
  in the algebra. That is the interesting outcome.

**T3, the cost of a k-generation patch.** d_k(i, t) is the least w such that the row on [i, i+w] fixes every ancestor
of (i, t) up to generation k, over all completions (exact, by the composed 4^k-state reader).
- P3: the mean of d_k grows linearly in k, with slope between 8 and 14, and the mean of d_1 is 9.9 ± 1, as in L1278.
- Counterfactual: a bounded d_k would mean deep ancestry is written locally, which would be a surprise. Superlinear
  growth would mean ancestry recedes faster than the reader's reset length.

**T1b, a follow-up written after T1's first output and before its own run.** T1 found that the middle founder's
family dies before t = 250. Every row has exactly one boundary between the left-edge and right-edge families, and it
drifts right at about +0.064 a step. Centre lineages drift left going back. The designated parent has one free choice,
pattern 011, where both the centre and the right parent are black, and T1 took C.
- P1e: with R chosen for 011, the boundary drifts left at a similar speed and the centre column belongs entirely to
  the right family. With a fair-coin choice (seeded), the mean drift is under 0.02 a step in size, and the centre's
  family changes at least once by t = 1500. If the drift survives every choice, it is intrinsic to Rule 30.
- P1f: with no choice made at all, every black parent counts (the black-parent DAG). Then over 90% of the black cells
  in row 1500 descend from all three founders. Counterfactual: a clean split would give the DAG dynasties of its own.

**T1c, written after T1b's output and before its own run.** T1b found the following. With no tie-break, the black
cells of row 1500 reachable through black parents from the left founder (−1, 1) are the left 53%. The cells reachable
from the right founder (1, 1) are 99.9%. The right edge of the left founder's reach sits at about +96, the same place
as the boundary under the C tie-break. That tie-break picks the leftmost black parent, so the two should coincide
exactly.
- P1g: B(t), the rightmost black cell reachable from (−1, 1), equals the C-tie-break boundary on every row to 1500.
  It grows linearly to t = 20,000, with B(t)/t settling in [0.04, 0.09]. The right founder's reach misses only a
  bounded strip at the left edge. Counterfactual: B(t)/t falling towards 0 (sublinear growth) would mean the 53% share
  tends to one half and the asymmetry is transient.

**T1d, written after T1c's output and before its own run.** A hand induction (section 5) gives an exact rule for the
reach front. Write B for B(t).
- If cells B+1 and B+2 of row t are both white, then B(t+1) = B + 1.
- Otherwise B(t+1) is the rightmost black cell of row t+1 at or left of B.
- Every black cell of [−t, B(t)] is reached from (−1, 1).

Predictions:
- P1h: the rule reproduces B(t) on every row to 20,000.
- P1i: per step, the front advances in more than 40% of steps. The naive estimate from independent cells is 25%
  advances, 37.5% stays and 37.5% retreats of mean 2, a drift of −0.5. The measured drift is +0.05, so advances must
  be far more frequent or retreats far shorter.
- P1j: computed with packed bits to t = 100,000, B(t)/t lies in [0.03, 0.06]. Below 0.03 would favour sublinear
  growth.

**T1e, written after T1d's output and before its own run.** The front rule makes sense in any Rule 30 evolution:
start from a black cell and apply it.
- P1k: from fair-coin initial rows (width 60,001, seeded, ten runs, 20,000 steps, front starting at a black cell
  near the middle, measured only while it stays at least 1,000 cells inside the region the edges have not reached), the
  mean step is within ±0.01 of the single-seed value 0.049.
- Counterfactual: a clearly different speed means the front's speed belongs to the single-seed orbit, not to Rule 30's
  typical behaviour.

## 5. Results

Probes: [`genealogy_schemas.py`](../tests/probes/genealogy_schemas.py) with
[output](../tests/probes/genealogy_schemas.out), and [`genealogy_front.py`](../tests/probes/genealogy_front.py)
with [output](../tests/probes/genealogy_front.out). All runs are COMPUTED on the M5 and take seconds.

**Scorecard.**
- Held: P1a, P1g on its window, P1h, P1i, P1j, P1k, P2a to P2e, and P3.
- Refuted:
  - P1b: the middle founder's family dies at t = 2.
  - P1c: lines thin out more slowly than s^(−1/2), and the central window never comes down to one ancestor.
  - P1d, its drift clause.
  - P1e: the boundary depends on the tie-break, and even a fair coin gives a drift.
  - P1f: the DAG splits instead of mixing.
- The refutations led to the main finding below.

**The black family tree (T1 to T1e).**
- In the bulk the designated steps are L 0.250, C 0.501 and R 0.249.
- Lines of descent never cross (section 6), so families are intervals of the row. The two edge lines are their own
  ancestors for ever. Every row therefore holds the left-edge family, the right-edge family and the boundary between
  them. Of the 11 black cells at t = 10, only 3 have descendants at t = 1500.
- Where that boundary sits depends on the tie-break at 011:
  - with C chosen, it ends near +96 at t = 1500;
  - with R chosen, the right family takes 99.9%;
  - with a fair coin, it drifts left at about −0.11 a step.
- **With no tie-break at all**, count every black parent. The black cells reachable from the seed's left child (−1, 1)
  are exactly the black cells of [−t, B(t)]. Those reachable from the right child (1, 1) are every black cell except
  a strip of four cells at the left edge. The middle child reaches the left child's set less the edge cell.
- The front B(t) moves by an exact local rule (section 6): **advance one if the next two cells ahead are white;
  otherwise drop to the rightmost black cell of the next row at or behind the front.**
- Steps: +1 in 52.7% of steps, 0 in 23.4%, −k with frequencies 0.119, 0.060, 0.031, … (ratio about one half).
  The mean is +0.049.
- B(t)/t is 0.0508 at t = 10,000 and 0.0475 at t = 100,000, with a log-log slope of 0.961. From fair-coin rows the
  same rule averages +0.045 ± 0.002 a step. MEASURED on these windows only (G26). Linear growth is suggested, not
  established.
- **What it shows.** Rule 30's chirality appears in its genealogy. A black lineage steps right only if both cells
  ahead are white (the OR must be off). It steps left whenever the one cell beyond is white (the XOR's left input).
  So black descent spreads left freely and right slowly, at about 0.046 cells a step on these windows. That speed is
  a property of typical Rule 30 evolution, not of the seed. It is new to our record. Every black centre cell to t = 1500
  lies in both children's reach (T1b), so it has black ancestry back to both of them.
- Independent-cell reasoning predicts a drift of −0.5. The front advances twice as often as that predicts, because a
  stay leaves the next cell white and a retreat of two or more leaves two whites ahead. The front reads a correlated
  neighbourhood, as Cloud's masking fronts do (CL674).

**The algebraic lifts (T2).**
- The Z/4 second digit is the Boolean-derivative tangent plus the carry κ = [exactly two parents black], and over the
  dual numbers it is the tangent alone. Both hold in all 64 cases.
- Sensitivity paths grow at 0.656 to 0.663 per step from five starting cells, below ln 2 = 0.693.
- The mod-2 tangent matches the actual damage of one flip on 46% to 54% of the damage region after 300 steps, and
  exactly on the right-edge diagonal.
- From the single seed, the Z/4 lift's second digit has density 0.4998 in the middle half of rows 1000 to 1500. On
  the centre column the (colour, digit) pairs are 0.255, 0.267, 0.227 and 0.251. The flip counter gives 0.273, 0.249,
  0.223 and 0.255. Both are within ±0.03 of a quarter: no hidden bias at this length (COMPUTED, t ≤ 1500).
- What it shows: the lifts are exact algebra, and the derivative appears as the carry digit's linear part. But on the
  centre column the extra digits look independent of the colour, as the counterfactual hoped they would not.

**The cost of a k-generation patch (T3).**
- Exact means over 150 interior cells: d_1 = 10.0, d_2 = 21.1, d_3 = 29.8, d_4 = 40.8 and d_5 = 49.8.
- The slope is 9.93, about one reset length per generation. So the row keeps k generations within about 10k cells to
  the right, while the S1 register keeps them in k bits at the cell itself.

## 6. Hand arguments (PROOF-SKETCH; GPT's read requested)

**Lines of descent never cross.** Take adjacent black cells p and p+1 in row t. For their designated parents to swap
sides, p must take R (pattern 001, so x_p(t−1) = 0) and p+1 must take L (pattern 100, so x_p(t−1) = 1).
That is a contradiction. Cells two apart that step towards each other share a parent and merge. So families are
intervals. The left edge cell has pattern 001 and the right edge cell 100, so each edge descends from the previous
edge cell.

**The reach front.** Let B = B(t), and suppose the left child's reach at time t is all the black cells of [−t, B].
- A black cell j ≤ B−1 at time t+1 has its black parents in [j−1, j+1], which lies in [−t−1, B]. Cells left of −t
  are white, so its black parents are reached.
- Cell B at time t+1 has the black, reached cell B among its parents.
- Cell B+1 at time t+1 has parents (1, x_(B+1), x_(B+2)), so it is black exactly when x_(B+1) = x_(B+2) = 0, and then
  its parent B is reached.
- Every black cell right of B+1 has all its parents right of B, so none is reached.

Induction from B(1) = −1 gives the rule and the interval property. Section 5 checks both on every row to 20,000.
The mirror argument for a leftmost front needs only x_(L−2) = 0, one white cell instead of two. That is the asymmetry
in two lines.
