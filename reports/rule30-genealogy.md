# Genealogy beside the colour: what a cell could record, and what it shows

*Local, L1279, 1 November 2026, at the owner's direction. Builds on GPT's GC2351 (the 1..8 parent labels) and
Local's L1278 (where the row already keeps each cell's parents).*

**Review update (GC2352):** the two section6 hand steps are now PROVED, two-party.
Section7 records the carrying read, qualifications to storage/speed claims, and two new
PROOF-SKETCH consequences. The original account below is preserved.

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

**S1. The lineage register (bits; complete local memory).** A cell remembers the colours of its left-line ancestors for
k generations: R_m(i, t) = x_(i−m)(t−m) for m = 1..k. It updates locally: R_1(i, t+1) = x_(i−1)(t) and
R_m(i, t+1) = R_(m−1)(i−1, t). Every past cell (j, t−m) has exactly one left-line descendant (j+m, t) in today's row.
So k bits per cell hold the previous k rows exactly, with no repetition, and any cell's k-generation family patch is
read off its 2k right-hand neighbours. PROOF-SKETCH, elementary (the left line is a bijection between rows); GPT's
read is requested (carried in GC2352). *Withdrawn (L1280, after GC2352):* an earlier sentence here called k bits
for k generations "the minimum", since k rows need k bits per cell. That treats the past rows as independent, but they
are constrained by the rule and on finite orbits are fixed by the present row. A storage lower bound needs an explicit
locality model, so no minimality is claimed. The owner's 1..8 label repeats each parent bit in three cells.

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

## 7. GPT carrying review and next discriminating step (GC2352)

1 November 2026. Read L1278/L1279, the complete report, both complete genealogy probes and
retained outputs, L1278's parent-reader source, and the addressed review flag at 89573330.
No long M5 run was replayed or reattributed to the Intel.

**The two requested hand steps carry: PROVED (Local proof, GPT independent read).**
For the designated C-at-011 tree the non-crossing argument is correct. More generally, a strict
crossing could only join adjacent children p,p+1 to parents p+1,p respectively. Both parents would
be black, so the child p+1 has left and centre inputs1,1 and must be white, a contradiction.
Children at distance two can meet at a parent but cannot strictly cross. This also covers the R
and coin tie-breaks. Family intervals mean intervals in the ordered list of black cells; white
holes remain. The reach-front induction is correct: the bullet about cell B is conditional on
that child being black. The left edge remains reached, so the fallback maximum always exists
on this single-seed trajectory. It does not require an assumed distribution of neighbourhoods.
The stronger all-choice non-crossing formulation above is a PROOF-SKETCH extension of the
requested C-choice theorem until Local reads it.

**Scope corrections for using the results.**
- The middle founder dies at time2 only in the C-at-011 designated tree. The all-parent graph
  retains its descendants; the R-at-011 output also retains that family through1500.
- A black-parent connection records a possible line of black ancestry, not necessarily sensitivity
  to a flip. At011 the right input is black but changing it does not change the output1.
- The measured +0.045/+0.047 agreement is evidence, not a typical-speed theorem. B(t) tending to
  infinity would imply eventual coverage of black centre cells, not coverage at every earlier
  time, and would not itself prove how often the centre is black.
- On arbitrary initial rows, the front rule describes the reach of an initially marked black
  prefix (all black sites at or left of B), provided the fallback exists. It does not generally
  describe descendants of the single black site B. In a solid five-black block the middle
  founder has no black children at all, whereas the prefix front survives. The random-row
  experiments compare a prefix interface with the seed's special left-founder interface;
  they are not a single-founder survival experiment. The small probe includes this control.
- S1's register construction is correct, but its claimed minimum is not established by saying
  that k past rows require k independent bits. The rows are dynamically constrained; on finite
  orbits the present whole row already determines them. A storage lower bound needs an explicit
  locality/decoding model. The patch uses neighbouring registers, not just the register at one cell.
- S2 requires N(i,0) congruent to x_i(0) modulo2, as the code correctly initializes it. S6's
  centre departure formula has domain 0 <= i <= t.
- T3 is a measured sample of minimal reconstruction widths for its stipulated all-completion
  reader, not an information-theoretic storage bound or an all-depth linear-growth theorem.

**Pull for the next step.** The intrinsic reach front is the warmest lead: it does not require
choosing an arbitrary parent when two are available. Its observed advance bias invites a
short exact explanation before any longer speed measurement. Does a retreat itself create a
white corridor that forces subsequent advances? Separately, does the extra arithmetic digit
belong to binary Rule30 or to the selected integer extension?

Prediction before small controls: a retreat of d>=1 forces at least ceil(d/2) following +1 steps;
and a different integer polynomial with exactly the same binary truth table can leave the
second digit identically zero from binary starts. Counterfactual: one local finite-support
front violating the corridor bound, or one binary triple on which the alternative polynomial
is not the actual Rule30 bit, rejects that claim. Controls: all512 nine-bit zero-padded rows,
every black cut point in each; all64 inputs to each mod4 identity; all16 four-bit crossing
windows. Fixed tiny scalar truth-table checks only, no sampling, speed fit or substantial run.
Record searched: L1279; GC2351/L1143; G121/G13; record_find and actual known index at kit f1cb20be,
portal19:46:53Z (six integer-lift hits concern arc-code displacements, not this lift); GC1974's
white-triangle argument concerns a different lineage and probability space. PRIOR-ART already
records the companion paper: it was not wholly new to our record. Read Nersissian's actual
[section3, Definitions1–2](https://arxiv.org/html/2609.25078v1#S3), which explicitly fixes the
canonical lift because other polynomial lifts can differ. Read Bagnoli–Rechtman–Ruffo's
[Boolean-derivative discussion](https://arxiv.org/html/cond-mat/9811159v1#S2). No novelty claim.

### Retreats create a guaranteed recovery corridor

**PROVED (GPT; Local carrying read L1280).** Suppose B(t+1)=B(t)-d with d>=1.
Write p=B(t+1). The next row is white on p+1,...,B(t), by the fallback definition. It is also
white at B(t)+1: that site is black exactly in the advance case, which did not occur. Thus
there are at least d+1 consecutive white cells immediately ahead of the new black front.

If a black front p has m>=2 whites ahead, its next position is p+1. At that next time the sites
p+2,...,p+m-1 are white, since all their inputs were white. This leaves at least m-2 whites
ahead of the new front. Iterate: m whites guarantee floor(m/2) consecutive advances. Substituting
m=d+1 proves

    B(t+1+s) = B(t+1)+s,  0 <= s <= ceil(d/2).

In particular **every retreat, including a one-cell retreat, is immediately followed by an
advance**. Local's observation for retreats of at least two was correct but weaker than needed.
The forced recovery offsets at least half the retreat distance, rounded up. It does not pay
all the debt: the complete retreat-plus-guaranteed-recovery block has net displacement
-floor(d/2). Nor does this imply that every syntactically allowed sequence of such blocks is
realizable on the seed. It supplies neither a drift sign nor a speed theorem.

The [independent scalar probe](../tests/probes/genealogy_review.py) checked every black cut in
all512 nine-bit finite-support rows: 2304 cuts, 640 retreats (largest7) and769 forced subsequent
advances. It separately checked non-crossing on16 four-bit windows. This is a bounded self-check
of the new corridor consequence; the hand argument covers all finite retreat sizes.

### The arithmetic carry depends on the chosen lift

**PROVED specialization of known lift nonuniqueness; Local carrying read L1280.** Local's
canonical polynomial P=a+b+c+bc has the asserted second-digit law. Let u=b+c-bc and instead use

    Q(a,b,c) = a+u-2*a*u
             = a+b+c-bc-2ab-2ac+2abc.

On binary inputs u is exactly b OR c, and a+u-2au is exactly their XOR as an integer0 or1.
Consequently Q maps binary rows to binary rows for all time, even when evaluated modulo4.
Its higher digit is identically zero when initialized zero. Expanding at a=x_a+2h_a, etc.,
modulo4 gives the same tangent coefficients as P but no source term:

    h' = h_a + (1+x_c)*h_b + (1+x_b)*h_c  (mod2).

For P the source is kappa=[exactly two black parents]. More generally replacing P by P+2R
changes that source by R(x_a,x_b,x_c) modulo2 while retaining the colour and those tangent
coefficients. Any Boolean source table can be chosen this way. This is not a defect in the
canonical convention; it rules out interpreting its digit statistics as an intrinsic extra
observable without specifying and justifying that convention. Nersissian section3 explicitly
makes the convention and warns about nonuniqueness. The companion source was already partially
read in our 7 October prior-art entry; Local's fresh search was not its first appearance here.
The scalar probe checks both second-digit laws on all64 mod4 triples and Q=f on all8 binary triples.

### Recommendation and executable queue

1. **Current target: ancestry-front excursions.** Use the exact front law and white corridor,
   without an independent-cell assumption. Next derive the exact row fragment remaining at the
   end of a retreat's guaranteed recovery; determine which part is fixed by d and which still
   depends on unrevealed outside bits. The useful outcome would be an exact return description
   or a deterministic bound on the unpaid retreat distance. A larger speed fit does not decide it.
   If two blocks only rediscover an uncontrolled outside word, park this description until a new
   compatible-root constraint or bound is available.
2. **Independent algebraic alternative:** classify what is common to the specified lifts (here,
   the first-order coefficients), and ask for an observable that those coefficients actually
   control in the binary orbit. Do not enlarge the digit census merely because mod8 is available.
3. **Mahler remains warm:** GC2350's three-block residue lift, with its existing stabilization-gap
   stop and 4,11,6 boundary alternative. No worker has been dispatched and schedules stay paused.

## 8. Local's read of GC2352 (L1280)

1 November 2026. Read GPT's §7 in full and ran its [probe](../tests/probes/genealogy_review.py) on the M5 (it
passes). The new steps were checked independently on the single-seed orbit to t = 20,000 with a scratch replay; no
probe was added.

**All three new steps carry: PROVED (GPT's proofs, Local's read).**
- **Non-crossing for every choice of black parent.** A strict crossing joins adjacent children p and p+1 to parents
  p+1 and p. Then child p+1 has left and centre inputs 1 and 1, so it is white, a contradiction. This covers every
  tie-break and the black-parent DAG itself: no two black-parent edges cross.
- **The retreat corridor.** After a retreat of d, the cells from B(t+1)+1 to B(t)+1 of the new row are white:
  - those up to B(t) are white by the fallback;
  - B(t)+1 is white because it is black exactly in the advance case.

  A black front with m ≥ 2 whites ahead advances and keeps m−2 whites ahead, since the cells inside a white stretch
  have only white inputs. So m = d+1 forces floor((d+1)/2) = ceil(d/2) advances.
  - On the actual orbit to 20,000 there are no violations.
  - 60.5% of all advances are these forced ones.
  - The mean step splits exactly as free advances minus unpaid retreat: 0.2079 − 0.1593 = +0.0486 a step.
  - So the sign of the drift is a contest between the free advances and the floor(d/2) left unpaid, as GPT says.
- **The lift's carry is a convention.** Q = a + u − 2au keeps binary rows binary, so its second digit stays zero.
  P + 2R changes the source by R. Both checked.

**One refinement on the lifts (PROOF-SKETCH; machine-checked in all 64 cases).** The tangent coefficients are common
to multilinear lifts only. The lift P + a² − a has the same values mod 2 on binary inputs. Over Z/4,
(x + 2h)² − (x + 2h) ≡ −2h for binary x, so its second digit has a-coefficient 0 instead of 1: a mismatch in exactly
the 32 cases with h_a = 1. The lift-free object is the Boolean derivative itself, f(x XOR e_i) XOR f(x). It equals
the formal derivative of the multilinear (algebraic normal form) representative. So GPT's queue item 2 should be
phrased as: what observable of the binary orbit do the Boolean derivatives control?

**A simpler form of the front (PROOF-SKETCH, two lines; machine-checked to 20,000).**
B(t+1) = max{ i ≤ B(t) + 1 : x_i(t+1) = 1 }. Proof: x_(B+1)(t+1) = 1 XOR (x_(B+1) OR x_(B+2))(t), so that cell is
black exactly in the advance case. Otherwise the fallback is the rightmost black cell at or left of B. The front is
therefore a follower of the black cells that may move right at most one cell a step. In the depth frame of CL674
(depth j reads only depths j−1 and j−2, so the shallow side evolves on its own), it is J(t+1) = the shallowest black
cell of row t+1 at depth ≥ J(t).
- With rows independent from step to step this would have zero speed, because the depth increment would be
  geometric with mean 1.
- The measured speed is exactly the excess of the front cell's survival rate (52.7%) over a fair coin, together with
  the shape of the fall-back distribution.
- Positive speed means that **the front cell is stickier than a coin**. Proving that is as hard as the statistics of
  the bulk, so no theorem is in sight. The next exact work is GPT's: the row fragment left after a retreat and its
  recovery.

**Scope corrections accepted.**
- The middle founder's extinction is specific to the tie-break.
- Black ancestry is not flip sensitivity.
- The random-row runs follow a marked black prefix, not a lone founder.
- S2 needs N(i, 0) ≡ x_i(0) (mod 2).
- S6 needs 0 ≤ i ≤ t.
- T3 is a measured sample, not a bound.

S1's minimality is withdrawn above.

## 9. Exact gap episodes and the bit retained behind the front (GC2353)

Owner continues after Local L1280. **Carrying read:** the follower formula
B(t+1)=max{i<=B(t)+1:x_i(t+1)=1} is PROVED, two-party: its candidate at B+1 is black
exactly in the old advance case, and otherwise the two maxima are identical. The leftmost
reached edge ensures existence on the seed. Local's non-multilinear lift correction also
carries: for a=x+2h, binary x,h, a²-a=-2h modulo4, removing the a-coefficient in the higher
digit while leaving every binary output unchanged. Thus the Boolean derivative, not every
lift's formal derivative, is the binary invariant. The source changes P+2R in section7 remain
correct within that specified class. Neither review imports a fair-coin law. In particular,
the drift sign depends on the full retreat-distance distribution, not just the fraction of
advancing steps.

**Pull and bounded test written first.** At a reached black front p, keep the maximal white
gap M ahead and the single bit z immediately behind it. Prediction: a finite M gives exactly
floor(M/2) successive advances before a nonadvance; z toggles at each advance, so at that
collision its parity decides stay versus retreat. Separately, a nonadvance retreats by L-1,
where L is the black-run length ending at the front. Counterfactual: an earlier collision,
an extra advance, or a mismatched trailing bit on any checked local cone rejects the claim.
Controls: all1024 zero-padded ten-bit rows, every black cut with a later black cell; all such
cuts for the black-run formula; and two explicit seven-site rows differing in just one bit.
This is a fixed tiny scalar test, no time-series extension, solver or substantial computation.
Record searched: L1279/L1280, GC2352, GC1974's shrinking white core and its independently driven
lineage scope, and the current record/kit/portal search. The white-triangle mechanism is known;
this is a front-episode specialization, not a novelty claim. The discriminating question is
whether lengths alone form an exact observer of successive episodes.

### Exact stopping time and the trailing bit

**PROVED (GPT; Local carrying read L1281), using the known C3 white-triangle shrink theorem.**
At time u let p=B(u) be black, and suppose the first black cell to its right is q=p+M+1.
Write r=floor(M/2), z=x_(p-1)(u). The finite gap hypothesis matters: at the rightmost black cell
there is no such q and this collision argument does not apply.

For every 0<=s<=r, the left boundary is B(u+s)=p+s, the right gap boundary is q-s, and
all sites strictly between those black boundaries are white. This is exactly C3: both ends
of a white run of length>=2 become black and its interior stays white. At s=r the boundaries
are adjacent if M is even, and enclose one white if M is odd. In either case the candidate
at B(u+r)+1 has left input1 and at least one of centre/right input1, so it is white.
Thus there are **exactly r** consecutive advances, followed by a nonadvance.

During each advance the cell immediately behind the new front has old inputs (z_s,1,0),
so z_(s+1)=1 XOR z_s. Consequently

    z_s = z XOR (s modulo2),
    the first nonadvance stays put iff z XOR (r modulo2) = 0,
    otherwise it retreats.

This predicts the stay/retreat branch, not the size of a retreat. It can also be viewed as
one conserved bit z_s XOR (B(u+s) modulo2) during the advancing portion. It is an explicitly
transported bit, not a probabilistic independence claim.

### Retreat size is an exact black-run statistic

Let L be the length of the consecutive black run ending at B, so a=B-L+1 is black and a-1
is white. Suppose the next step is not an advance. Then the new row is white at a+1,...,B:
there the old left and centre bits are both1. It is also white at B+1 by the nonadvance
assumption. At a the old left input is0 and the centre is1, so the new cell is black.
Therefore

    B(t+1) = B(t)-(L-1).

L=1 gives a stay. L>=2 gives a retreat d=L-1. This strengthens the search for the next black
cell in the new row to a black-run length in the old row. It is a local run calculation,
not a distribution law for L at the adaptively selected boundary.

For a genuine retreat let p=B(t+1), and let a_bit=x_(p-2)(t). Since p-1 is the white left
flank of that old black run, the new bit immediately behind p is

    x_(p-1)(t+1) = 1 XOR a_bit.

If M is the maximal ensuing white gap and r=floor(M/2), the next collision therefore stays
iff a_bit = 1 XOR (r modulo2). The branch information survives the whole recovery as the
parity of **one specified earlier bit**. M is at least d+1, recovering GC2352's bound; its
full value, not just that lower bound, fixes the full advancing episode.

### A sharp two-row control: lengths alone forget this bit

Take zero outside coordinates -4,...,2 and mark all black cells at or left of B(0)=0.
These are two finite initial rows, not two occurrences asserted in the single-seed orbit:

    coordinates      -4 -3 -2 -1  0  1  2
    first row         0  0  0  1  1  0  1
    second row        0  1  0  1  1  0  1
    front, first      0, -1, 0,  0
    front, second     0, -1, 0, -1

Both retreat by1, then have a maximal white gap of2 and recover by one step. The next
collision stays in the first case and retreats in the second. Only the earlier bit at-3
differs. Thus (retreat length, white-gap length, recovery length) is not a universally
closed predictive state. The explicit bit above explains the failure. This neither
refutes a special constraint on the single-seed orbit nor claims that a finite summary
of some other selected observable is impossible.

**COMPUTED self-check:** [fixed scalar probe](../tests/probes/genealogy_gap_episode.py) checks
4097 complete finite-gap episodes and3328 nonadvance run identities across all1024 ten-bit
finite rows, as well as the two explicit controls. No samples or longer speed measurements.

**What changed / next executable step.** The requested end-of-episode fragment is now exact:
11 or101 at the meeting, with trailing bit z XOR r. The lengths-only closure is refuted.
Keep the one-bit phase during free motion; next derive its reset at successive nonadvances
and check whether the single-seed constraints relate that sampled bit to the unpaid retreat
length. The carrying question is a deterministic relation, not whether the bit looks fair.
Do not extend an ancestor ladder to compensate for missing constraints. If the next block
only exposes another unconstrained left word, park this episode-summary route; independent
alternative is the binary Boolean derivative's exact finite-difference law, with its nonlinear
term retained. Mahler GC2350 remains the separate warm lead.

### External refresh during this block

The index refresh completed with kit93d98bbe049177d2c1546b6b0714aa33703ae13d,
portal timestamp2026-11-01T21:36:37Z,12 open PRs:10 added index entries,4 changed,22 no longer
listed. These counts concern index entries, not ten new theorems. Inspected the current source
headers and relevant declaration signatures of AlternatingTraceBridge, SurvivalBridge,
SEPToPeriodTwo, LeftAntiPeriod and ZeroBoundaryStripeCascade, not their complete proofs.
The new main now includes the previously open repeat-budget/mortality and separator bridges.
`Q01_of_mortality` has the explicit Mortality hypothesis; the SEP/RW/BWH implications likewise
retain open hypotheses. No mortality, separator hypothesis, or prize solution is supplied.
The auxiliary frontier in those bridges is not this ancestry boundary. The changed diagonal
and backward-stripe declarations are different observables. Portal c6ff55 is listed Lean
Verified, while0159fa is Lean Unverified at this refresh; these are portal receipts, not our
independent acceptance. Prior-art comparison for this block remains scoped to the known
white-triangle mechanism and the sources above.

Refresh receipt retained outside git in the shared store at `cited/gc2353-known-refresh.txt`,
SHA256 `1a38b37b510725d7cf0eb260cecc7fe34fe67520f1bf6a6d391d77b56ffef017`.
The exact kit commit above fixes the inspected source versions.

## 10. Local's read of GC2353 (L1281)

1 November 2026. Read §9 in full and ran GPT's [probe](../tests/probes/genealogy_gap_episode.py) on the M5 (PASS). I
also checked the laws on the actual single-seed orbit, which GPT's finite rows do not cover:
[`genealogy_episode_orbit.py`](../tests/probes/genealogy_episode_orbit.py) and its
[output](../tests/probes/genealogy_episode_orbit.out).

**All four steps and the control carry: PROVED (GPT's proofs, Local's read).** Checked by hand:
- **The gap episode.** C3's shrink step applies while the gap is at least 2. The front cell p+1 sees (1, 0, 0); the
  interior sees only whites; the cell q−1 sees (0, 0, 1). So the gap loses two cells a step and the front advances,
  for exactly ⌊M/2⌋ steps. At gap 0 or 1 the cell at B+1 or B+2 is black, so the next step does not advance.
- **The trailing bit.** During an advance the cell behind the new front sees (z, 1, 0), so it becomes NOT z.
  At the collision, x_B(t+1) = z_r XOR 1, so the front stays exactly when z_r = 0.
- **The retreat size.** The cells inside the black run see 1, 1 on their left and centre and turn white. The run's
  first cell a sees (0, 1, ·) and stays black, so the front lands on a: a retreat of L − 1.
- **The bit behind a landing.** Cell a − 1 sees (x_(a−2), 0, 1), so it becomes NOT x_(a−2). This also covers stays
  (L = 1).
- **The control.** Both finite rows behave as stated. I hand-checked the first step of the first row: B(1) = −1,
  a retreat of 1 off a run of length 2.

**On the orbit (COMPUTED, to t = 20,000).**
- (a) Starting at every one of the 19,998 times, the number of consecutive advances is exactly ⌊M/2⌋.
- (b) The stay or retreat branch follows z XOR (⌊M/2⌋ mod 2) every time.
- (c) Each of the 9,463 non-advances retreats by exactly L − 1.
- (d) The bit behind every landing is 1 XOR x_(p−2).
- No failures.

**An exact ledger of the front (PROVED from the laws above).** Split time into episodes: free motion through a
white gap, then one collision. Every advance lies in some episode's free motion, so

    B(t) = −1 + Σ over completed episodes (⌊M_k/2⌋ − (L_k − 1)) + (the partial last episode).

On the orbit to 20,000 there are 9,464 episodes. The completed ones have Σ⌊M_k/2⌋ = 10,535 and
Σ(L_k − 1) = 9,564, and the unfinished last episode has made one advance. So B(20,000) = −1 + 10,536 − 9,564 = 971.
- Per episode, the front gains 1.113 cells crossing white and loses 1.011 cells to black runs. With mean episode
  length 2.113 steps, that gives the measured +0.049 a step.
- The black runs behind the front average L ≈ 2.01, as fair-coin runs would.
- The white gaps are what is unusual: the mean of ⌊M/2⌋ is 1.113, against 1/3 for independent cells. GC2352's
  corridor (M ≥ L after a landing) explains part of the difference.
- **So the sign of the speed is the sign of E[⌊M/2⌋] − E[L − 1] per episode at the front.** Both quantities are now
  exact local readings, the gap ahead and the run behind. This is descriptive (COMPUTED). No law for their joint
  distribution is claimed.

The kit refresh in §9 (kit 93d98bbe) was noted. Its mortality and separator bridges concern other frontiers, as GPT
says.

## 11. Fresh initial bits at successive collisions (GC2354)

Owner continues after L1281. Read its complete carrying review, orbit probe and retained output.
The episode ledger carries with the partial final episode retained. Its numerical replay is
Local's M5 measurement, not a new Intel run. GC2353's statements are now PROVED, two-party.

**Change of approach / warm pull.** The trailing-bit reset alone again exposes a bit farther
left; it supplies no single-seed constraint. Do not grow a gate-by-gate ancestor ladder.
Instead use GC1974's existing initial-bit exposure method on this different, black-prefix
follower. Can we prove the geometric black-run law in a precisely stated random-input model,
rather than assume that successive rows or adaptively chosen neighbourhoods are independent?
This is useful if it isolates exactly the statistical claim that cannot be imported to the seed.
The scalar episode-summary route to a seed drift is parked pending an actual-root relation.

**Prediction before small controls.** Fix the initial right half, with x_0=1 and a rightmost
black cell q>0; make the initial sites i<0 independent fair bits. Mark all initial black sites
at or left of0 and follow their right boundary. At successive collisions the black-run lengths
L_k should be independent with Pr(L_k=l)=2^(-l), l>=1, conditional on the completed history
and the next white gap but before inspecting the next trailing bit. More fundamentally, every
finite list l_1,...,l_n should specify exactly one initial left word of length sum(l_k).
Counterfactual: a required initial coordinate was already read, or the next gap needs an unread
coordinate, invalidates the proposed law. Tiny deterministic control: all64 left words of length6
with right half111000..., two complete episodes, and all nine requested pairs l_1,l_2 in1..3.
Expected multiplicities are2^(6-l_1-l_2), with exactly one consumed prefix per pair. Fixed
32-update stop per word; any failure is preserved, no automatic enlargement. No sampling,
solver, large run or claim of typical speed. Independent control: known future conditioning
(the current trailing bit already observed) must not be described as a fresh fair bit.

Record searched: GC1974 complete exposure proof (different stopped white-core lineage), C3,
GC2352–53, L1281; actual kit93d98bbe `Rule30CoupledEmptyRight.evol_diff_front` and source proof
of the left-permutive leading bit; current portal/open-PR index21:36:37Z. The nonlinear-damage
alternative is already covered by GC507/GC529, so rederiving it would not advance the queue.
Primary [Wolfram notes on random inputs](https://www.wolframscience.com/nks/notes-6-1--properties-of-initially-random-cellular-automaton-patterns/)
discuss fair-row statistics and triangle sizes, not this conditional collision sampling law.
This is a known-method application; no novelty assertion from the search.

### Exact input model and the exposure invariant

**PROOF-SKETCH, GPT; independent carrying read pending.** Work on the whole integer line,
with x_i(t+1)=x_(i-1)(t) XOR (x_i(t) OR x_(i+1)(t)). Fix all initial cells i>=0,
with x_0(0)=1 and a rightmost black cell q>0. The initial sites i<0 are independent
fair bits. Start the marked prefix at B(0)=0. This is a random-left-half, fixed-right-half
interface; it is not a randomization of the ordinary single-seed problem.

Use complete episodes: advance across the maximal white gap, then take one nonadvance.
Let u_k,p_k be time and front position at the start of episode k, and set

    c_k = p_k-u_k.

The invariant is: all initial cells i>=c_k have been exposed; the initial cells i<c_k
remain unread and independent fair bits. The completed-episode history determines this
exposed suffix, u_k,p_k and the whole current row at sites i>=p_k. The current trailing
bit is NOT included in the conditioning information. Once it is inspected, the conditional
branch law changes, just as GC2353 says.

The usual left-permutive identity, proved by induction, is

    x_j(t) = x_(j-t)(0) XOR H_t(x_(j-t+1)(0),...,x_(j+t)(0)).

At the next update the new leftmost initial bit enters only through the left parent's
unmasked XOR; the two other input cones start strictly to its right. Thus prescribing
x_j(t), once the initial bits to the right of j-t are known, fixes exactly one value of
the bit at j-t. This is the familiar kit `evol_diff_front` mechanism, restated here so no
unreviewed probability lemma from GC1974 is assumed.

The white gap M_k and r_k=floor(M_k/2) are determined by the exposed suffix. They are finite:
the global rightmost black cell remains at q+t, whereas B(t)<=t, so a black cell always
exists strictly to the right. Through these r_k advances, position and time both increase
by r_k; their difference c_k is unchanged. All cells on or right of the moving front have
initial cones contained in the exposed suffix. No fresh left bit is read during the advance.

### The collision consumes exactly the next block of initial bits

At the collision time v=u_k+r_k and position b=p_k+r_k, scan b-1,b-2,... until the first
white cell. The cell b is already known black. The j-th inspected cell b-j has leading
initial coordinate

    (b-j)-v = c_k-j.

Every other argument of that cell is strictly to the right and already exposed. Each
inspection therefore reads precisely the next fresh initial bit. To have black-run length
L_k=l, the first l-1 inspected outputs must be black and the l-th white. That fixes exactly
l successive initial bits, with conditional probability2^(-l). The probability of an
infinite black scan is zero. Stopping at the first white exposes no cell farther left:
on each finite stopping word the new endpoint is fixed and the remaining product coordinates
are unchanged. This handles the adaptive sampling, rather than assuming it harmless.

The new position and time are b-l+1 and v+1. Hence

    c_(k+1) = (b-l+1)-(v+1) = c_k-l.

This is exactly the last exposed initial coordinate. The next row on and right of the new
front, including its next white gap, depends only on initial cells at or right of that
coordinate. The invariant restarts without extra exposure.

Consequently, for every finite list of positive integers l_1,...,l_n,

    Pr(L_0=l_1,...,L_(n-1)=l_n | fixed right half) = 2^(-sum(l_i)).

More strongly, that list specifies exactly one initial left word of length sum(l_i),
read in the order -1,-2,...; every completion farther left gives the same list. All such
lists are realizable by finite left extensions. The run lengths are therefore independent
geometric variables of mean2 in this probability model. L_k is independent of the completed
history and of its own episode's M_k, which is known before its collision scan. The next
gap M_(k+1) need not be independent of L_k. No independence of whole successive rows is used.
There are almost surely infinitely many finite episodes: each gap is finite and each scan
terminates almost surely; the countable union of exceptional scans has probability zero.

### Exact small controls and the seed boundary

The [64-word control](../tests/probes/genealogy_fresh_bits.py) fixes the right half111000...
and enumerates every six-bit left word (bits listed from-1 toward-6), with zero outside that
finite test window. For l_1,l_2 in1..3, it obtains exactly2^(6-l_1-l_2) completions and one
consumed prefix per pair:

| Run lengths | Consumed initial prefix | Number of six-bit completions |
|---|---|---:|
| 1,1 | 00 | 16 |
| 1,2 | 010 | 8 |
| 1,3 | 0111 | 4 |
| 2,1 | 100 | 8 |
| 2,2 | 1010 | 4 |
| 2,3 | 10111 | 2 |
| 3,1 | 1101 | 4 |
| 3,2 | 11000 | 2 |
| 3,3 | 110010 | 1 |

The extra left bits range through every completion in each case. The coordinate identity
c_k=-sum of the completed run lengths passes at both resets. These are COMPUTED self-checks,
not a probability estimate or an independent carrying read.

Conditioning control: with this right half the initial gap is0. If the trailing bit at-1
is already known white, the first collision has L=1 with probability1, not1/2. The theorem
conditions on completed episodes and the current gap, not on a peek at the bit it is about
to read, or on the full current row.

After n completed episodes, the deterministic displacement identity is

    p_n-p_0 = (u_n-u_0)-sum_(k<n) L_k.

Thus the drift also measures how quickly the moving observation boundary consumes initial
positions. On a random half-row those unread positions carry independent bits; on the seed
background they are fixed zeros. Calling both cases fresh *random* information would be wrong.

For the actual seed, start at its time-one left founder and translate it to position0; its
fixed right half is111000... but its entire left half is zero. Its admissible run-length
lists must therefore be the ones whose uniquely decoded initial prefix is all zeros.
The table shows how restrictive this is even for two short runs. There is exactly one actual
list at each episode count, not a free geometric draw. This gives a precise compatibility
condition but not yet a shortcut to that list, a bound on its gap balance, or a drift theorem.
It also explains why the finite-word realization argument cannot settle the seed: it varies
left initial data from one list to another.

This is the same methodological boundary as Mahler G51: finite branch descriptions determine
input bits/residue classes, while one fixed arithmetic or automaton start must satisfy all
prefix constraints together. It is a transfer of method and obstruction, not an identification
of the two dynamical systems.

### Disposition and next executable step

The random-left-half collision law is a complete hand candidate with exact finite controls;
Local's independent read should target the equality c_(k+1)=c_k-L_k and the no-extra-exposure
claim. It explains the fair-run baseline in a model where that statement is justified, without
promoting Local's single-seed measurements to a distribution theorem.

The length/phase-only route to single-seed drift is now parked: it has twice reduced to an
uncontrolled initial-bit compatibility condition. Reopen it only with a bound or a structural
constraint on the zero-prefix code, not more samples or a longer ancestor register. The separate
nonlinear-damage alternative is already GC507/GC529 and is not a new job. Warm next executable
step after review: compare the explicit zero-prefix criterion here with Mahler G51's fixed-start
residue criterion, and ask whether a finite-prefix *obstruction certificate* transfers (no claim
that generic realizability itself does). Independent alternative: the previously queued Mahler
4,11,6 threshold boundary. Schedules remain paused; no new worker job dispatched.

## 12. What the derivatives control (L1282, at the owner's direction)

The owner chose GPT's alternative queue item: the binary Boolean derivative, with its nonlinear term kept, and what
it controls in the actual orbit.

**What is already known (searched first).** Record searched: `record_find` for sensitivity, Huang, influence set,
polarization, Rule 150, superposition, sideways, Duhamel, variation of constants, trinomial, Lucas, linear part,
source term, Meier and 0.246; known index kit f1cb20be.
- The kit proves Rule 30 = Rule 150 + x_p x_(p+1) and the centre's Duhamel formula
  (`Rule30Equivalents.CenterFormulas.duhamel` and `center_duhamel`). Our §8.100, G28 and GC420 used it before the kit.
- Portal entry R30-20261023-603218 (Lean Verified) has the degree 2t − 1, Walsh balance and the query-complexity
  sandwich [2t − 1, 2t + 1].
- Our L1072 degree law, carried in GC2032.
- §8.66: the leftward damage speed is 0.246 = 1 − P(heal)·E[jump].
- L957: the sideways front at 0.155, with its exact four-bit difference law.
- G13: the reader's reset words.
- Bagnoli, Rechtman and Ruffo (1992): the Boolean Jacobian and path-count Lyapunov exponent.
- GPT's GC507 (8 October) already wrote the exact two-copy damage law with its quadratic term. GC529 showed that
  first-order replica counts do not bound the simultaneous damage cell by cell, at the background triple (0,1,1). It
  left open whether the two cones' **endpoints** differ. GC529 cites Baetens and Gravner's Lyapunov profiles, which
  we have not compared.
- GPT's GC2354 (§11) notes that this alternative is mostly covered by GC507 and GC529.

So most of the derivative ground is charted, and none of it is claimed here. T4 below addresses GC529's open
endpoint question.

**The exact one-step laws (PROVED by exhaustion; T4 checks every case).** Write F = L + N, with L Rule 150 and
N(x)_i = x_i x_(i+1) (the kit's split).
- **Polarization.** F(x + y) = F(x) + F(y) + B(x, y), where B(x, y)_i = x_i y_(i+1) + x_(i+1) y_i.
- **Forward damage.** D(t+1) = F(D) + B(x, D). Damage runs Rule 30 on itself, coupled to the orbit only through B.
  In white surroundings it is exactly a second Rule 30 seed. Its first-order part J(x)D = L D + B(x, D) has the masks
  1, 1 + x_(i+1) and 1 + x_i, the Boolean derivatives. Its second-order part N(D) does not depend on the orbit.
- **Backward ("invisible") damage.** Two parent rows with the same children differ by a D with
  D_(i−1) = (1 + x_(i+1)) D_i + (1 + x_i) D_(i+1) + D_i D_(i+1), read right to left. G13's reader ambiguity dies
  exactly when this difference is masked. L957's sideways law has the same four cases.

So one set of masks governs influence forward, recoverability backward and reconstruction sideways. That unification
is the only new framing here, and it is labelled as framing.

**T4, the test (predictions written before the run).** Flip one cell inside the single-seed pattern at time 1000, at
positions −200, 0 and +200, and follow three left edges for 5,000 steps:
- the actual damage edge Δ_act;
- the edge of first-order influence Δ_sup: cells with at least one sensitivity path, which is the support of the
  Bagnoli path counts;
- the edge of the mod-2 tangent Δ_tan: cells with an odd number of paths.

Hand rules at the edge (PROOF-SKETCH):
- Δ_sup steps left exactly when x_(Δ−1) = 0, and steps right exactly when x_(Δ−1) = x_Δ = x_(Δ+1) = 1.
- With independent cells that is a speed of 0.375.
- The actual edge shares the leftward condition, because a single damaged input is exactly first order. When it does
  not step left it reads the second-order term, so it can fall behind Δ_sup or move ahead of it.

Predictions:
- P4a: the actual edge moves left at 0.246 ± 0.01, reproducing §8.66.
- P4b: the first-order edge moves left faster, at a speed in [0.30, 0.40], and the gap grows linearly.
- P4c: the mod-2 tangent edge equals the first-order edge in at least 80% of steps, since path counts at the
  extreme edge are small.
- Counterfactual: if the first-order edge also moves at about 0.246, the derivatives control the reach of influence
  even though they do not control its interior (T2c).
- What it would teach: whether the Boolean derivative fixes the large-scale cone of influence, or whether the AND of
  damages, the base-free second-order term, is already needed at the edge.

### T4 results (L1282)

Probe: [`genealogy_derivatives.py`](../tests/probes/genealogy_derivatives.py), with its
[output](../tests/probes/genealogy_derivatives.out). COMPUTED for the identities; MEASURED for the speeds, on one
window (G26).
- **The one-step laws** pass every case: polarization 64/64, forward damage 64/64, backward invisible damage on 512
  windows. The forward law is GC507's.
- **Edges after one flip at time 1000** (positions −200, 0 and +200; 5,000 steps):

  | Edge | Speed left over steps 2,500–5,000 | Position at step 5,000 |
  |---|---|---|
  | Actual damage | 0.249, 0.284 and 0.247 | −1448, −1307 and −1033 |
  | First-order support | 0.395, 0.396 and 0.408 | −2176, −1971 and −1819 |
  | Mod-2 tangent | 0.285, 0.300 and 0.310 | −1577, −1562 and −1239 |

  The right edge moves at exactly +1 in all three (asserted).
- **The actual edge was strictly ahead of the first-order edge in 0.000, 0.000 and 0.001 of steps.** The GC529
  mechanism does occur at the edge, but rarely.

Scorecard:
- P4a held at two sites and missed at one: 0.284 over the second half at site 0. Over the whole 5,000 steps the
  three sites give 0.250, 0.261 and 0.247.
- P4b held at two sites and was marginal at one (0.408 against a limit of 0.40). The gap grows linearly, to about
  700 cells at step 5,000.
- **P4c REFUTED.** The tangent edge equals the first-order edge in only 0.1% to 0.5% of steps. Path counts at the
  extreme edge are almost always even.
  - Why: a leftward step copies the edge count unchanged (the new edge cell has one open input), so evenness
    persists.
  - A count can become even only when the edge stays put and adds a neighbour's count.

**What it teaches.** The Boolean derivatives do **not** fix the reach of influence.
- The first-order cone spreads left at about 0.40, faster even than the independent-cell value of 0.375.
- Parity cancellation alone brings it to about 0.29.
- The true influence spreads left at about 0.25.
- The gap between 0.29 and 0.25 is the base-free quadratic term N(D) = D_i D_(i+1): healing at the edge is partly a
  second-order effect.
- This settles, as a measurement, GC529's open question: the cones' endpoints do differ, by a speed of about 0.15.
- Masks still govern exactly the edge's leftward step (a single damaged input), the right edge, the reader's
  ambiguity and sideways reconstruction (§12 laws). The interior and the long-run reach need the AND of damages.

**Disposition.** The derivative route is largely charted (GC505, GC507, GC529, §8.66, L957, the kit's Duhamel and
the degree and query-complexity results). This block adds a measured endpoint separation and the
three-direction framing. Park it unless a question needs the quadratic damage term specifically.

## 13. Local's read of GC2354 (L1282)

Read §11 in full and ran GPT's [probe](../tests/probes/genealogy_fresh_bits.py) (PASS).

**Carries: PROVED (GPT's proof, Local's read).** The carrying steps:
- **The exposure invariant.** At an episode start (u, p), the row at sites ≥ p depends only on initial cells
  ≥ p − u = c, by the light cone.
- **The advances.** During the ⌊M/2⌋ advances, position and time rise together, so c does not change. M is read
  from cells right of p, which are exposed. M is finite because the right edge q + t stays strictly right of
  B(t) ≤ t.
- **The collision scan.** Cell b − j at time v has leading initial coordinate c − j. By left permutivity its value
  is that bit XOR a function of exposed bits only: the bits c − 1, …, c − j + 1 were fixed by the earlier inspections
  of this scan. So each inspection reveals one fresh fair bit, and P(L = l) = 2^(−l), independent of the history and
  of M.
- **The landing.** The front lands at a = b − L + 1 at time v + 1 (GC2353's retreat law). So
  c_(k+1) = c_k − L_k, which is exactly the last coordinate read (the white cell b − L). The next episode's
  information lies at or right of it, so nothing extra is exposed.
- **The trailing bit** at the episode start lies on the same diagonal, c − 1. That is why it must not be peeked at,
  as GPT's conditioning control says.

**Independent check (COMPUTED, Local's own code,
[`genealogy_fresh_bits_local.py`](../tests/probes/genealogy_fresh_bits_local.py)).**
- Three fixed right halves: 111 (the seed's time-one row), 1011001 and 1001.
- Every 14-bit left word, three complete episodes.
- All 364 run-length lists with ΣL ≤ 14 have exactly 2^(14 − ΣL) words and a single consumed prefix.
- The exposure identity B − t = −ΣL holds at every reset.
- The all-zero left word decodes to (1, 1, 4) for the seed's right half. The real orbit's first collisions have run
  lengths 1, 1, 4, 1, 1, 1, 3, 1, 4, 2, 1, 2, … so the decoding matches.

**What it adds to the ledger.** Since B − t = −2 − ΣL_k (in the seed's frame), the front's speed is
1 − (mean L)/(mean episode length). In GPT's random-left-half model the L_k are i.i.d. with mean 2. So the speed is
positive exactly when the mean episode lasts more than two steps, that is when E[⌊M/2⌋] > 1. The seed's measured
1.113 is consistent with that. On the seed itself the L-list is the single list that decodes to zeros, so no
probability statement transfers. GPT's parking of the drift route stands. GPT's next step is to compare the
zero-prefix criterion with Mahler G51's fixed-start residue criterion.

## 14. A finite codec and its limits (GC2355, independent consolidation)

The owner asks for a connected body of work before another outside read. This section develops the
already carried GC2354, rather than opening another review exchange. New deductions below are
**PROOF-SKETCH** until a carrying read; finite replays are self-checks. Schedules remain paused.

### Pull, searches and frozen small controls

The pull is the difference between recording an arbitrary past and recognizing the particular empty
past of the seed. Can the collision record be decoded with an explicit finite cost, and can a failed
candidate carry a small, checkable reason? A successful construction supplies a practical exact
interface; it need not supply a speed theorem. Cheap objection: this may just be old triangular
reconstruction in new coordinates. That objection is partly correct and is retained explicitly.

Record searched: GC2353/2354 and Local L1281/1282; G25/G130/GC547/GC699's diagonal reconstruction
and finite-left obstruction; G50/G51's Mahler residue and fractional-window conditions; GC1221/1224's
code isometry; current known index kit93d98bbe049177d2c1546b6b0714aa33703ae13d,
portal21:36:37Z on 1 November 2026, twelve open PRs. The query
`tree.automorph|prefix.preserv|triangular.*(biject|cod)` finds existing triangular recodings;
no general coding novelty is claimed. The kit's `Rule30CoupledEmptyRight.evol_diff_front`
is the leading-bit mechanism. [Bernstein and Lagarias, *The 3x+1 Conjugacy Map* (1996)](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6975BB4A8C46CF6842217043AAF9EC13/S0008414X0004606Xa.pdf/3x_1_conjugacy_map.pdf),
introduction and Appendix A, provide the classical residue-compatible permutation/isometry
framework; their Collatz map is different from Mahler's ceil map. G51 is our exact source for the latter.

Prediction, written before the probe: with fixed right half111000..., the first eight collision
scan bits permute all256 eight-bit initial left words, respecting every shorter prefix. A triangular
right-edge implementation and an ordinary finite-set Rule30 truth-table implementation agree.
The time bound derived below is24 updates for these eight bits. For all64 three-episode lists
with entries1..4, the zero ribbon accepts exactly(1,1,4), rejecting others at the first contradictory
scan bit within their separate bounds. Explicit controls include(1,1,3) and(1,1,5).
Counterfactual: any disagreement, repeated output prefix or bound violation refutes the implementation
or the deduction; preserve the failure and do not extend the horizon automatically. Unexpected check:
the code001110 has a Mahler integer residue but an empty fractional window.

This is a small scalar control, not a substantial research run: one Python process, at most256
eight-bit words and64 three-episode candidates, no random samples, files or horizon enlargement.
The ordinary oracle uses at most24 updates for the encoding controls; candidate controls use only
the independently derived bound for their specified list (total length at most12).

Additional prediction before implementing the inverse: GC699's constant-column repair should invert
all256 eight-bit outputs, with the same24-update bound. Each newly constructed diagonal is driven
only by its two already fixed neighbours; complementing that entire diagonal enforces its requested
scan bit. This adds256 tiny deterministic inverse checks, no longer horizon or new sample family.

### 14.1 What is being encoded

Fix the right half as in §11: x0=1, a further rightmost black site q>0, and white beyond q.
Let a_j=x_(-j)(0), j=1,2,... be the left ribbon, read outwards from the front. At each collision
inspect cells immediately behind the known black front, stopping at the first white cell. A
collision of length L records L-1 ones followed by a zero. Concatenate these words; call the
result y. Thus lengths(1,1,4) record `0 | 0 | 1110`, or001110.

An arbitrary prefix may end before the terminating zero. Keeping such unfinished runs is essential:
otherwise a fixed eight-bit input need not give a whole number of episodes.

**Prefix encoding theorem (PROOF-SKETCH, corollary of the carried GC2354).** For each j there is a
Boolean function h_j of the earlier input bits and the fixed right half such that

    y_j = a_j XOR h_j(a_1,...,a_(j-1)).

Indeed, suppose j-1 bits have been read. The completed lengths, the current scan offset and its
time are fixed by those outputs. If an episode has just ended, the gap and its forced advances
are determined by the exposed suffix. The next inspected cell has leading initial coordinate
-j, even when its space/time location was chosen adaptively. Left permutivity makes its value
a_j XOR a function of initial coordinates strictly greater than -j. The choice of the query
does not depend on a_j. This proves the formula by induction, without independent time rows.

Consequences:

- Every length-S input prefix gives one length-S output prefix, and vice versa: solve the displayed
  equation successively for a_j. Two inputs first differing at bit j have outputs first differing
  at precisely j. Later differences can never repair that first mismatch.
- Regard bits as least-significant-first digits of an integer modulo2^S. The map is a permutation
  at every S, and these permutations agree when the last digits are removed. In the infinite
  binary setting it is a **2-adic isometry**: distance is measured by the first differing digit,
  and that distance is preserved. Equivalently it permutes the branches of the tree of finite
  binary words while preserving their parent/child relation. This is the familiar triangular-code
  principle, not a new general isometry theorem.
- Fair input gives fair independent output bits, hence the geometric L law. It does not make the
  output of the single fixed zero ribbon a fair sample. There is no information loss in this
  entire record when the right half is retained. A small local observer can still lack the key
  or the earlier bits needed to decode its latest observation.

There is an exceptional infinite-input convention. A scan can encounter an infinite black run;
then record an infinite tail of ones and make no subsequent physical update. In that case a
finite next ancestry front need not exist. The prefix codec remains defined, and consistent
finite prefixes define the infinite isometry. This exception has probability zero for the fair
input model; finite-left configurations, including the seed, cannot contain such a run at finite
time. Do not claim that every infinite ribbon has infinitely many completed physical episodes.

### 14.2 Geometry bounds the time needed to read a prefix

At an episode start (t,B), let s be the number of initial bits already consumed. GC2354 gives
B-t=-s. The rightmost black cell is q+t, so the distance from that edge to the front is

    J = q+t-B = q+s.

The nearest black cell on the right is no farther away than this edge. Thus the white gap M
satisfies M<=J-1. An episode's r=floor(M/2) advances and one collision update take at most

    r+1 <= floor((q+s+1)/2)

steps. For a proposed list ell_1,...,ell_n of positive lengths, put s_0=0,
s_k=ell_1+...+ell_k, and S=s_n. Any realization completes this list by

    H(ell) = sum_(k=1..n) floor((q+s_(k-1)+1)/2).

The s_(k-1) are distinct members of0,...,S-1. All summands are nonnegative, so

    H(ell) <= H_q(S) = sum_(j=0..S-1) floor((q+j+1)/2).

The same coarse bound covers reading S scan bits when the last run is unfinished: add its
start to the set of completed-episode starts and omit its unneeded collision update. An
infinite scan only makes further reads at the same physical time. No infinite waiting time
is being hidden inside the encoding theorem.

The assumption of a further rightmost black q>0 is essential, not cosmetic. If q=0, the marked
front is itself the right edge and advances forever through whites: B(t)=t, with no collision
bits at all, regardless of the left ribbon. It cannot encode that ribbon. At the smallest allowed
q=1 the first gap is zero, the first query is at time0, and its collision update takes one step,
exactly consistent with the bound. Length1 is likewise included: its recorded word is a single
zero and its collision is a stay. No positive-gap or genuine-retreat assumption enters the proof.

For fixed q, H_q(S)=S^2/4+O((q+1)S). This is a bound on *how far to evolve to read S bits*,
not a period bound or an efficient prediction theorem for a large requested physical time.
For q=2 and S=8 it gives24. It is not asserted sharp. Large retreats increase J and hence
the possible next gap; their cost is explicitly charged to previously consumed bits.

### 14.3 An exact verifier and inverse, with obstruction certificates

Use coordinates measured leftwards from the moving right edge:

    z_d(t)=x_(q+t-d)(t),  d>=0;  z_(-1)=z_(-2)=0.
    z_d(t+1)=z_d(t) XOR (z_(d-1)(t) OR z_(d-2)(t)).

This is the established right-edge triangular map. In particular, depths greater than D cannot
affect depths0,...,D. At episode start the front has depth J=q+s; forced advances leave J
unchanged. At collision time v, the requested length ell means

    z_(J+j)(v)=1 for 1<=j<ell, and z_(J+ell)(v)=0.

For the zero ribbon, initialize depths0,...,q from the fixed right half and depthsq+1,...,q+S
to zero. Evolve only this prefix. Check the requested bits in order, rejecting at the first
mismatch. On a successful block update once and replace J by J+ell. Induction on successful
blocks identifies the computed prefix with the true row, so this is necessary and sufficient
for the proposed finite list. A rejected longer run is rejected at its premature white cell;
a rejected shorter run is rejected at its falsely requested white flank. Neither needs a scan
past the proposed S. The first mismatch occurs by H(ell), because until it the episodes agree.

A certificate consists of the requested list and fixed right half, the first bad episode and
scan index j, its time v and depth d, and the requested and actual bits. Its checker recomputes
the bounded triangular prefix. This is an exact finite certificate with a compact witness;
it is not a claim that checking takes constant time or avoids evolution. Scalar verification
costs O((q+S) H(ell)) time and O(q+S) space, including gap scans within these bounds. With q
fixed this is at most cubic time and linear space in S.

For an inverse construction, use the known GC699 diagonal repair. Once shallower diagonals are
fixed, a new depth d has the form

    z_d(v) = z_d(0) XOR P_d(v),
    P_d(v) = XOR_(0<=t<v) (z_(d-1)(t) OR z_(d-2)(t)).

Construct its history with initial value0. At the query time v chosen by the earlier outputs,
the unique required initial bit is y_j XOR P_d(v). If this is1, complement the **entire history**
of the diagonal, not just its queried cell. This enforces Rule30 at every time while preserving
all earlier queries and shallower diagonals. After a zero the new gap uses only fixed columns,
so the construction continues. Store histories through H_q(S); the straightforward inverse
uses O((q+S)H_q(S)) time and space. This is a concrete application of GC699 to an adaptive
clock. No claim of a minimal-memory inverse is made.

For a zero initial ribbon, the decoded bits must all vanish: the requested scan bits must
equal these accumulated OR parities. That is the exact algebraic constraint. It still contains
the nonlinear evolution in P_d; merely naming the parity has not solved or compressed it.

### 14.4 Finite controls and explicit rejected histories

**COMPUTED self-checks, Intel;** [probe](../tests/probes/genealogy_codec.py), small scalar execution:

- All256 eight-bit inputs: the triangular prefix and the ordinary truth-table CA agree on
  output bits and query locations/times. At each length0,...,8, the prefix map is bijective.
  Latest query time is13, within the declared24 bound.
- All256 output words: the independent column-repair inverse recovers the input producing it.
- All64 three-episode lists with entries1..4: both implementations return identical acceptance
  or first-mismatch records. Only(1,1,4) belongs to the zero ribbon.

| Requested lengths | Recorded code | Decoded initial left prefix | Zero-ribbon decision |
|---|---|---|---|
| 1,1,3 | 00110 | 00001 | Reject at initial index5, time4, depth7: requested0, actual1 |
| 1,1,4 | 001110 | 000000 | Accept; third episode completes at time5 |
| 1,1,5 | 0011110 | 0000010 | Reject at initial index6, time4, depth8: requested1, actual0 |

Each of these lists has H(ell)=5. Each decoded prefix, extended by zeros, independently
reproduces its requested list in the ordinary CA. Thus the rejections do not say that a length
list is impossible in general. They say precisely which initially white site would need to
be black to make it possible. This is the fixed-input distinction the random model omitted.

### 14.5 What transfers to Mahler, and a transfer that fails

The useful common interface is now exact: a finite observed word determines one initial binary
prefix/residue; a fixed initial condition is a compatibility test against that prefix. G51 already
gives this for Mahler's integer map T(n)=ceil(3n/2), using the parity bits of its successive integer
states. The present result supplies the analogous interface for the genealogy's adaptive scans.

Both encodings preserve the first differing bit. One can therefore compose the genealogy encoder
with the inverse Mahler parity encoder as maps of infinite binary strings. This does **not** show
that Rule30 physical steps correspond to Mahler iterations, or that an ordinary finite integer
maps to another one. It is a code correspondence, not a proved conjugacy of these dynamics.

There is an earlier obstruction even before the infinite integer question. The actual zero-ribbon
code starts001110. Mahler's integer start60 realizes that prefix:

    60 -> 90 -> 135 -> 203 -> 305 -> 458,
    parity: 0, 0, 1, 1, 1, 0.

Yet it cannot have a real fractional companion staying in[0,1/2) through those steps. Write the
fraction as u. An odd integer step needs u>=1/3 and then sends it to(3u-1)/2<1/4. Another odd
step immediately afterwards would need it to be at least1/3. Hence11 is forbidden, as already
proved in G50. G51 gives the exact empty window for001110: its lower endpoint is76/243,
its upper endpoint2/9. Already0011 has lower20/81>2/9.

So the most direct raw-code transfer fails on the seed's first three collisions. This is a
specific failed transfer, not evidence that no cross-problem technique can work. What exports
successfully is the separation between finite coding, a fixed initial input, and an additional
admissibility constraint. A useful future transfer must preserve that constraint, or explicitly
identify what replaces it. Inserting zeros into an arbitrary code would repair the easiest
forbidden word but would change the clock and would not establish fixed-integer compatibility.

### 14.6 What this body settles, and the next genuinely open step

The whole collision record, with the fixed right half known, does not forget the initial ribbon.
It reveals one bit at a time behind a reversible mask. The uncertain part of the seed problem
is now the structure of those masks on the *one all-zero input*, not how many generic inputs
can produce a proposed history. The polynomial horizon and explicit inverse make that statement
operational. They do not bound the long-term imbalance between gaps and retreats.

A cheap adversarial test explains why. For any prescribed infinite word b, the map a_j -> a_j XOR b_j
has the same prefix-bijection and first-difference properties, but sends the zero ribbon to b.
Even restricting to very easy such maps allows constant, alternating and nonperiodic outputs.
Thus these coding properties alone cannot constrain the zero-input output. A successful next
argument must use the actual Rule30 drives P_d and the actual collision schedule. This objection
rules out promoting a generic information-preservation statement into a seed-statistics theorem.

There is also a qualification to §13's informal speed sentence. Let D_n be total duration of n
completed episodes and S_n their total L. Exactly B(D_n)=D_n-S_n. In the random-input model,
S_n/n tends to2 almost surely. **If** D_n/n tends to a finite d, the speed at episode endpoints
is1-2/d; an all-time limit additionally requires control between endpoints. The current work
does not establish a stationary gap law, convergence of D_n/n, or an expectation formula for d.
The geometric L law alone does not justify these extra assertions or the seed's measured speed.

Next executable step: use the *existing* dyadic edge-clock results on P_d(v), with v restricted
to these collision times, to ask whether their parity cancellations yield a relation on the
zero ribbon beyond direct replay. First test any proposed relation against the explicit inverse
and the three histories above; an arbitrary-input identity alone will not constrain the seed.
Do not replace this question with a longer trajectory or a frequency fit. If no cancellation
uses the actual collision clock, park this representation as an exact interface rather than a
predictive compression. Independent warm alternative: Mahler's4,11,6 threshold boundary and its
strict endpoints. Curiosity alternative: characterize which finite-state adaptive query clocks
make a triangular inverse itself finite-state; first separate that restricted class from the
unbounded gaps here. No new outside review has been requested in this consolidation block.

## 15. Local's answer to GPT's inquisition (L1283)

1 November 2026. The owner asked Local to bring in GC2355 and to answer GPT's inquisition directly: three families of
relation (clocks at collision times, cancellations between neighbouring tallies, uniform obstructions for structured
families), aiming at a relation that turns the seed's white initial ribbon into a reusable restriction. GC2355 was
read in full (§14).
- Its codec, horizon bound and verifier stand as PROOF-SKETCH pending a carrying read. Local has not done that read
  in this block.
- §14.6's qualification of L1282's speed sentence is accepted. A speed of 1 − 2/d needs D_n/n → d and control
  between endpoints, so L1282 overstated it.

Record searched for this answer:
- **The right-edge clocks.** The frozen ruler and edge odometer. G249 proves right-prefix periods
  Q_j ≤ 2^⌈(2j−1)/3⌉ for every finite seed. §8.73 proves the right-edge triangles form a ruler sequence. Coven, Pivato
  and Yassawi (2007) cover edge odometers (GC808/GC810).
- **The left band.** Left diagonals are eventually periodic with power-of-two periods (Jen 1986; Rowland §5; our
  JenPow2.lean, L541, band k ≤ j+2 with period 2^j). Lemmas B1–B3 are PROVED, §8.59. The staircase P_e ≤ 32 is
  MEASURED to about 98,300 diagonals (L383).
- §8.74: the order ends near x/t = −0.25 (MEASURED).
- §8.18/§8.29: every climb on black reaches the origin.
- The record needed for the argument below: GC2353, GC2354, GC2355, G13 and G121.

### 15.1 The clock at the front (family 1): the black front is a copy of the right edge

**Lemma (PROOF-SKETCH, Local).** Work in the depth frame z_d(t) of §14.3. Let the front sit at depth J during an
episode, from its start u to its collision time v = u + r. Let w = (w_1, w_2, …) be the **deep word**, w_j = z_(J+j),
the cells behind the front.
- While z_J = 1, every depth J+j ≥ J+1 updates as w_j ← w_j XOR (w_(j−1) OR w_(j−2)), with w_0 = 1. Depth J+1 reads J
  and J−1, and the black J saturates the OR; depth J+2 reads J+1 and J.
- This is exactly the dynamics Φ of the cells below the seed's own right edge. Φ(0)^n is the frozen ruler at time n.
- The front is black from u to v, and its collision update also reads z_J(v) = 1.
- So, writing lead1 for the number of leading 1s:

      L_k = 1 + lead1(Φ^(r_k) w^(k)),        w^(k+1) = σ^(L_k) Φ^(r_k+1) w^(k),

  where σ drops leading digits. On the seed, w^(0) = 0, the white ribbon behind the left founder.
- The first digit of Φ toggles every step. That is GC2353's trailing bit. Digits 1..n of Φ^r(w) depend only on
  w_1..w_n and on r modulo the level-n period of Φ, a power of two.

**So collisions do read a known clock, with bounded clock information per collision**: L_k digits and r_k modulo a
power of two set by L_k. But the digits of w carry the history (this is GC2355's codec in odometer form). The
irregular input is r_k, the white triangles met on the shallow side. No known clock reaches there: the front sits at
depth about 0.95t, beyond the right-edge ruler's settled depths and outside the left ordered band. On its own,
family 1 therefore repackages. Its value is the deep-side law, which family 3 uses.

### 15.2 Cancellations (family 2)

On the seed P_d(v) = z_d(v), because the start is zero. So the tallies are the column values, and adjacent tallies
satisfy

    P_d(v) XOR P_(d+1)(v) = XOR_(t<v) [NOT z_(d−1)(t) AND (z_(d−2)(t) XOR z_d(t))]

(from (a OR b) XOR (c OR a) = (b XOR c) AND NOT a). The black front cancels every contribution to the depth just
below it during a residence. That cancellation is exactly 15.1's odometer. What survives lives at collisions and in
the shallow wake, which is the same uncontrolled input as before. Ranked lowest: it adds nothing that 15.1 lacks.

### 15.3 A uniform obstruction from the white ribbon (family 3)

**Proposition (PROOF-SKETCH, Local; GPT's carrying read requested).**
- Let the initial configuration have an eventually white left half; the seed is one.
- If the ancestry front's (r_k, L_k) history is eventually periodic, with period p from episode k_0, then over each
  period ΣL = 2Σ(r + 1).
- So the front eventually retreats at exactly light speed, at a constant distance from the pattern's left edge.

*Proof.*
1. Given the r's, the deep-side law of 15.1 makes the deep word an injective function of the future reads. The first
   L reads fix w_1..w_L through the level-L bijection Φ^r. The next reads fix the next digits of Φ^(r+1) w, and so
   on. So the deep words at k_0 and k_0 + p are the same 2-adic word.
2. On a configuration with a white left tail, the deep word is a natural number. Its top digit is the leftmost black
   cell, which moves left by exactly one cell each step (left permutivity). So its length is the front's distance to
   the left edge, B(u) + u on the seed.
3. Equal words have equal length. So over each period the front moves by −(elapsed time). ∎

- **Control (why this uses the ribbon).** In GC2354's random-left-half model the deep word is a general 2-adic
  integer. A periodic history is then realized by its forced fixed point, which has infinitely many 1s. The example
  (r = 0, L = 1)^∞ forces w = 0101…. So this is precisely the "fixed white ribbon → reusable restriction" GPT asked
  for. Every eventually periodic continuation fails the same lock unless it retreats at light speed. The lock is the
  finiteness of the deep word.
- **What remains.** Light-speed patterns keep the front at a fixed distance from the left edge. On the seed that
  distance eventually falls inside the ordered left band, where Jen's theorem makes every diagonal eventually
  periodic. Excluding them is a question about **traps** in the left band: can a rightward reach front hold a bounded
  distance from the left edge?

**T5, the test (predictions written before the run).**
- (a) Check the deep-side law on the actual orbit. At every episode start to t = 5,000, take the first 64 digits of
  w from the row. Check L = 1 + lead1(Φ^r w), and check the next deep word against σ^L Φ^(r+1) w on its determined
  digits. Prediction: no failure.
- (b) Traps. In the seed's left band at t_0 = 2,000 and t_0 = 8,000, start a rightward prefix front at every black
  cell within 300 of the left edge, and run it 4,000 steps.
  - Prediction: every one escapes, ending more than 1,000 cells from the left edge.
  - Positive control: the leftward follower of the right founder, min{i ≥ L−1 : black}, does stay trapped, at offset
    4 (T1c measured this).
  - Counterfactual: a rightward front that stays within a bounded distance would make the light-speed case realizable
    in the band. The obstruction would then need the band's actual pattern, not this argument.

**Control correction, written after T5's first run and before rerunning.** The planned positive control was a
leftward follower started 300 cells from the left edge. It did not pin at offset 4: it ended at offset 401 at both
t_0. So that control prediction was wrong (kept here). T1c's offset-4 pinning came from a follower started next to
the edge. Added control: a leftward follower started at the first black cell at offset ≥ 3. Prediction: it ends at
offset 4. If it does not, the trap detector is unvalidated and T5(b) shows only that no trap was found.

**T5c, written after T5(a)–(b) and before its own run.** For every light-speed pattern of period at most 2 (r ≤ 2,
L ≤ 6, ΣL = 2Σ(r+1)), compute the forced deep word w* to 60 digits, using the read bijection one digit at a time.
- Prediction: every forced word is either infinite (a non-zero tail within 60 digits) or finite. A finite word puts
  the front at a fixed distance D_0 = |w*| from the left edge.
- For the seed's band, no finite w* matches the band behind any front position in 64 consecutive late rows, so all
  these patterns are excluded on the seed.
- Example by hand: (r = 0, L = 2)^∞ forces w* = 1 0 0 0 …, a front one cell from the edge. The edge cell is black,
  so this needs the band's offset 3 to be black at every step. T5(b) suggests it is not.

**T5c result, and T5d written before its run.** T5c's prediction is REFUTED.
- Of the 35 light-speed patterns, 27 force an infinite deep word. No finite-left configuration can follow them.
- The other 8 force finite words of length 1 to 16. Every one matches the seed's left band in some late rows, for
  example (0, 2) → w* = 1, the two black edge cells.
- So naturality alone excludes all non-light-speed patterns and 27 of 35 light-speed ones. The 8 edge-hugging
  patterns can only be excluded on the shallow side, through the gaps.

T5d: start rightward prefix fronts at every black cell at offsets 0..40 at each of 64 consecutive start times
(t_0 = 3000..3063), and run each for 2,000 steps. Prediction: none ends within 100 cells of the left edge. Scope:
64 phases. The band's full period at these offsets is bounded by JenPow2, but this does not prove it is at most 64.

### 15.4 Results, and the relation to freeze next

Probes: [`genealogy_inquisition.py`](../tests/probes/genealogy_inquisition.py) and
[`genealogy_lightspeed.py`](../tests/probes/genealogy_lightspeed.py), each with its `.out`. Everything is COMPUTED on
the M5 in seconds.

**Results.**
- **T5(a), HELD.** The deep-side law holds in all 2,413 episodes of the seed to t = 5,000 on 64 digits, with no
  failure.
- **T5(b), HELD.** All 157 rightward prefix fronts started within 300 cells of the left edge escape at t_0 = 2,000 and
  8,000, ending 4,185 to 4,504 cells from the edge, about the main front's +0.04 in space. The results at the two
  start times are identical, consistent with band periods dividing 6,000 there.
  - The planned control (leftward follower from offset 300) was a wrong prediction: it ended at 401.
  - The added control (from offset ≥ 3) ends at offset 4, so the detector does register a trap.
- **T5c, prediction REFUTED.** Naturality excludes 27 of the 35 light-speed patterns; 8 short edge-hugging patterns
  match the band.
- **T5d, HELD.** 1,392 fronts at 64 phases from offsets 0..40 all escape, the nearest ending 2,092 cells away.

**The answer to the inquisition, in one line.** The white ribbon becomes a reusable restriction through the
**finiteness of the deep word**: on the seed, the cells behind the front form a natural number whose length is the
front's distance to the left edge. That one feature rejects every eventually periodic collision history that does not
retreat at light speed (Proposition 15.3). Short patterns that do retreat at light speed must hug the left edge, inside
Jen's proved-periodic band. Hence:

**Reduction (PROOF-SKETCH).** If limsup_t (B(t) + t) = ∞, meaning the left founder's black descendants are not
eventually confined to a bounded band at the left edge, then the seed's (r, L) collision history is not eventually
periodic.

This is a Jen-type statement for the genealogy record. The hypothesis is about the seed's own reach, not about
generic inputs. Measured: B(t) + t ≈ 1.047t to t = 100,000 (MEASURED). No trap was found at any tested band phase
(COMPUTED).

**The relation to freeze (for the next computation).**
- **Statement (the edge-escape relation).** For every bound D, no rightward prefix front in the seed's left band stays
  within D of the left edge for all time.
- **Assumptions.** Each band diagonal is eventually periodic, with known power-of-two bounds (Jen 1986, JenPow2). So
  for fixed D the statement is a finite check over one band period.
- **Failure condition.** A trapped front at some phase. The leftward offset-4 control validates the detector.
- **Controls.** Random left rows, where there is no edge and the notion is void. Altered white ribbons of finite
  length, where the deep word is still natural but the band differs.
- **What a proof needs.** Something uniform in D. For example, the band's small staircase periods (P_e ≤ 32,
  MEASURED, L383) would turn it into one finite band automaton, if they can be proved.

Family ranking after this block:
1. Family 3, now with a concrete lock.
2. Family 1, the source of the deep-side law.
3. Family 2, subsumed by family 1.

## 16. GPT carrying review and exact tail-closure pilot (GC2356)

Read Local's complete §15 and both probe sources at388acbd1. The deep-side update and the
periodic-history implication carry, with the precise scope developed below. The60-digit probe
does not justify its finite/infinite labels: a nonzero60-digit tail can later terminate, and
twenty trailing zero digits can later restart. The outputs are retained as the original evidence,
not silently overwritten. No large seed trajectory is being repeated.

### Frozen pilot, before execution

Pull: replace the heuristic tail labels for the *same35 patterns* by exact cycle closure in a
finite spatial recurrence. This would turn a finite prefix into a genuinely infinite-tail
certificate, or reveal a misclassification. Prediction: the reported8/27 split survives; the
eight finite candidates satisfy the complete return map exactly. Counterfactual: a different
split, a failed boundary equation or a recurrence-oracle mismatch invalidates the old conclusion
and stops the stage. Unexpected control: retain the partial-cycle drift of word length; only
whole-cycle distance is constant. The shallow-gap conditions are not part of these certificates.

Record searched: GC2353/2354/2355, Local L1283 including `genealogy_lightspeed.py`; G25/GC699;
LemmaB2 and `tests/probes/lean/JenPow2.lean` (`jen_pow2`, `D_succ`, `edge`);
kit93d98bbe `Rule30RingOrbits` actual source (`orbit_evol`, `encode_walk`, `decode_ring`) and
`Rule30FrozenRuler`. The ring result uses a different direction and periodic spatial boundary;
we reuse finite-state recurrence reasoning, not its ring hypotheses as a finite-left theorem.
The complete21:36:37Z index remains the current external snapshot. No novelty decision or submission.

Source: [genealogy_tail_certificate.py](../tests/probes/genealogy_tail_certificate.py),
SHA256 `12eddee39f93a8b930c2994e957ed8a6a74baf2c789116b77207d9cd99086572`. Fixed inputs: Local's35 phased words, period at most2, r<=2, L<=6;
start from exactly60 forced digits. No longer empirical horizon. A derived width2T recurrence
has at most2^(2T)<=4096 states, which is the exhaustive stopping bound, not a chosen sample size.
Controls: all5460 transitions for T=1,...,6 compared with a scalar Boolean-cone oracle;
boundary-aware integer return compared with scalar-array evolution; each finite candidate's
entire integer return checked. Each nonzero recurrent cycle certifies infinitely many ones.

One Intel CPU worker, nice10, no subprocesses or numerical-library threads. Launch headroom
free+inactive about6581MiB, swap used48MiB, load2.70; no concurrent research job observed.
Frozen aggregate CPU budget120s; child checks its own CPU at20s, launcher hard per-process30s,
wall60s, tree RSS768MiB, max2 tracked processes (timer plus Python). Aggregate CPU is assessed
from receipts; these per-process limits are not a general aggregate-CPU enforcement mechanism.
Launch floor4096MiB, running floor3072MiB, swap growth64MiB; files16MiB and stage128MiB.
Data only in a fresh scratch stage directory; retain stdout, source digest and launcher/time
receipts. Pressure/monitor failure stops the stage with no automatic retry. No GPU or separate
thermal measurement; do not claim one. No new outside review request in this block.

### First pilot result and second frozen decision

First pilot COMPLETED, source frozen at e31d7383. The exact recurrence gives the same8 finite /
27 infinite classification. It visits at most260 states; nonzero cycles have periods8,12,28,36,
110 or260. All5460 transition controls and both boundary-map implementations pass. The eight
finite integer return equations pass without any tail cutoff. New recurrence justification is
GPT's PROOF-SKETCH below; this is not Lean verification or another worker's carrying read.
Measured child0.25 CPU seconds,0.26 wall seconds,14,884,864-byte maximum RSS; supervisor0.138 CPU
seconds. The stage finished before its first live sample, so zero sampled RSS/process maxima
are not measurements of zero resource usage. Launch free+inactive6552MiB; no leftover detected.
Certificate JSON SHA256 `ebb5f603daf386d38a4c3fe3ed53c4c41f4ea1dda5623206166e769567528364`.

The eight exact finite words have length at most16, but a cycle can temporarily move farther
from the edge: their greatest offsets, including advances, are at most18. This gives a sharply
bounded next decision, not an all-width census. Freeze a separate pilot to close the actual
seed band through offset20, enough to update any front confined to offsets0..18.

Prediction before execution: the autonomous21-bit left-band orbit repeats within256 states;
its exact recurrent cycle gives an order-preserving period map for the rightward follower with
escape made absorbing. That map has no fixed point in0..18, so no such follower can remain in
this band forever. If true, this excludes the remaining eight histories on the seed, using
their shallow gaps implicitly through the actual front update. Counterfactual: no cycle within
256 states, a finite fixed point, or either oracle disagreement stops this stage; do not enlarge
the band or the transient cap. A finite fixed point would be an exact trap certificate.
Controls: scalar Rule30 truth-table updates against the integer band recurrence at every visited
state; monotonicity checked at every cycle phase; leftward follower fixed at offset4; a synthetic
static two-black-cell row has a rightward fixed point at1. Synthetic control is not a Rule30 orbit.

Source [genealogy_band_certificate.py](../tests/probes/genealogy_band_certificate.py), SHA256
`c511f654af775bcbee012ab52ed39f9a52cfecddb6e3deab89742321792c1e38`; input is the first pilot's
certificate JSON at the digest above. Bounds:256 band states; at most19 applications of one
period map from its least state; no trajectory longer than this derived finite check. Same
single-worker launch, memory, pressure, file and disk caps as the first stage; CPU30s per process,
wall60s, aggregate CPU budget120s with the same enforcement limitation stated above. Fresh
stage directory, retained receipts, no automatic rerun. This is a separate frozen follow-on
justified by the exact finite-word result, not an extension of the earlier sample horizon.

### 16.1 Carrying verdict on Local's two hand steps

**PROVED, two-party:** §15.1's deep-side law and §15.3's periodic-history implication, with the
following precise wording. The front is a black-prefix follower with infinitely many finite
episodes. Write a for the initial leftmost black position and D(t)=B(t)-a+t for its distance
from the moving left edge. On an eventually periodic pair history (r,L), let

    T = sum(r+1),    K = sum L

over one episode period. Then K=2T, D is eventually periodic in physical time with period T,
and B(t+T)=B(t)-T from a cycle boundary onward. Thus D is bounded. It need not be constant
inside the cycle, and the front need not move left at every individual step. In particular,
r>0 includes rightward advances. This is net light speed per complete cycle.

**Carrying step (a).** The first deep digit updates by complement, because its OR input includes
the black front; the second does too. All later digits follow the homogeneous triangular rule.
Therefore the exact deep-word map, with digit1 as the least significant bit, is

    Phi(w) = w XOR ((w << 1) OR (w << 2) OR 3).

This formula is valid for finite words and for infinite binary words. The black-front boundary
remains valid through every forced advance and through the collision's old row. At that row
the scan reads1^(L-1)0, and after the update the new front sits L digits farther into the
co-moving word. Hence Local's two displayed formulas hold, including L=1 and r=0.

**Carrying step (b), spelling out uniqueness.** With all r values prescribed, each scan fixes
the next L initial digits through a triangular bijection. Applying Phi once more and dropping
the L already read digits leaves a triangular bijection on the unread tail, conditional on
those digits. Repeating fixes at least one new initial digit per episode. Thus the whole
future pair history determines at most one deep word. Two episode boundaries one period apart
have the same future pair history, so their deep words coincide. For an eventually white left
tail these are finite nonnegative integers, and their bit length is exactly D (zero when the
front is the leftmost black cell). The edge persists and moves left by one by `JenPow2.edge`;
left-permutivity alone is not the reason for this left-edge assertion. Finally

    D(next cycle)-D(this cycle) = 2T-K = 0.

The intermediate r advances and collision displacements repeat too, proving bounded periodic
D at all times. This carries the stated implication from unbounded limsup D to nonperiodic
pair history. It proves no unboundedness hypothesis itself. Family2's P_d=z_d identification
is restricted to depths initially white, as in §14; the deep-side law already handles the
needed black-front cancellation.

**Control scope correction.** A forced infinite word for prescribed (r,L) is a solution of the
deep-side equations. It need not realize the prescribed r values against a fixed actual right
half. For example (0,1) forever fixes deep word0101..., but with right half111 the first update
leaves two whites ahead of the front, forcing the next r=1, not0. Thus the random-left control
illustrates removal of the finite-word obstruction; it is not a full prescribed-gap realization
theorem. The main necessary-condition proof only uses histories that actually occur and survives.

### 16.2 Why the new spatial recurrence closes the tail exactly

**PROOF-SKETCH, GPT;** exact finite cycles computed below. Let F be one complete prescribed
deep-word return: apply Phi^(r+1) and drop L for each block. Reads immediately before each
drop must be1^(L-1)0. In a light-speed pattern K=2T. Let G be the boundary-free rule on a
two-sided sequence, G(w)_j=w_j XOR(w_(j-1) OR w_(j-2)).

For output index j>2T, the backwards cone of F(w)_j cannot reach any inserted black-front
boundary. To see this in original word coordinates, the final output sits at j+K; at any
intermediate time at most2T coordinates are lost travelling backwards, whereas every inserted
boundary sits at a dropped-prefix coordinate at most K. Thus this cone stays strictly beyond
all inserted boundaries. Its value is (G^T w)_(j+K), depending on exactly the window j,...,j+K.

The highest digit passes through with XOR coefficient1. If h_T is that output with the highest
input digit set to0, the fixed-point equation F(w)=w becomes

    w_(j+K) = w_j XOR h_T(w_j,...,w_(j+K-1)),       j>2T.

This is a deterministic recurrence on K-bit windows. There are only2^K states. A repeated state
fixes the entire future; its eventual cycle is either the all-zero state, giving a finite word,
or contains a1, giving infinitely many ones. This is the missing implication in T5c. A long
observed zero or nonzero suffix alone could not supply it.

The pilot starts with Local's same60 uniquely forced digits. It directly checks every return
equation whose dependency window is within that prefix. For later equations the recurrence
applies, since60-K>2T for every tested pattern. The initial read guards are also checked.
Thus the generated eventually periodic word solves the complete return equation and the guards;
by the carried uniqueness argument it is the forced word, not just a plausible continuation.
Independent scalar-array and integer implementations agree on the initial boundary equations,
the bulk transitions and a full period of the generated tail. The finite cases additionally
satisfy F(w)=w as exact integers without any truncation.

The27 nonzero cycles have spatial periods drawn from8,12,28,36,110,260. The maximum visited
state count is260, far below the frozen4096-state bound. The eight finite results are:

| Phased pair pattern (r,L) | Initial word length D | Greatest D within its cycle |
|---|---:|---:|
| (0,2) | 1 | 1 |
| (1,4) | 4 | 6 |
| (0,1),(0,3) | 4 | 5 |
| (0,3),(0,1) | 5 | 5 |
| (0,3),(2,5) | 14 | 17 |
| (0,4),(2,4) | 16 | 18 |
| (2,4),(0,4) | 14 | 18 |
| (2,5),(0,3) | 13 | 17 |

These are phased patterns, not35 distinct cycles modulo rotation. Neither the classification
nor the band match supplies the missing shallow gaps; that is the next certificate.

### 16.3 The monotone period map and an exact no-trap band

**PROOF-SKETCH, GPT; finite certificate COMPUTED with controls.** In left-edge coordinates
a_j(t)=x_(a-t+j)(t), the update is

    a_j(t+1)=a_(j-2)(t) XOR(a_(j-1)(t) OR a_j(t)),   a_j=0 for j<0.

The prefix through index D+2 is autonomous: no cell to its right affects it. A rightward
prefix front at distance s from the edge has the exact next distance

    f_t(s) = max{j<=s+2 : a_j(t+1)=1}.

This function is nondecreasing in s, since the search intervals are nested; it is not claimed
that the physical distance always increases. The black edge ensures the set is nonempty.
For the question of staying inside0,...,D forever, replace any exit by an absorbing symbol
top=D+1. This preserves order. Once the band is periodic with period P, compose P such maps
to obtain H_D on the finite ordered set0,...,D,top.

A perpetual trap in this band exists exactly when H_D has a finite fixed point. A finite fixed
point gives a safe repeating path. Conversely an orbit that never exits eventually cycles in
this finite set, and an order-preserving map of a finite chain has no cycles longer than one.
Alternatively, iterate H_D from0: it can only increase, and either reaches top or stabilizes
at a fixed point. Every other initial front dominates it. This is an all-state criterion;
one empirical trajectory over one period would not have established it. Earlier times cause
no difficulty: any hypothetical forever-trapped front eventually reaches the periodic regime.

**Actual certificate at D=18.** The21-bit seed band, started from integer1, closes after27
distinct states: transient23, period4. Its four recurrent rows, encoded with offset0 as the
least significant bit, are

    759419, 1173267, 1340283, 866835.

The explicit autonomous transition sends the last back to the first, so this is an exact
infinite repetition, not a period fit. At that first phase, the clipped four-step map on
states0,...,18 is

    [6,6,6,6,6,6,12,12,15,15,15,17,17,17,top,top,top,top,top].

It has no finite fixed point; the least-state chain is0->6->12->17->top. Thus every rightward
prefix front in this band exits it within16 steps when started at that phase. Aligning an
arbitrary recurrent phase costs at most3 further steps. Reentry after an exit is allowed;
this proves that no front stays in the band forever or eventually stays there forever.
The other three phase maps were checked as controls and also have no finite fixed point.
The leftward follower at offset4 remains fixed at every phase, so the direction matters.

**Consequence for Local's family.** Each of the eight finite forced words would confine its
front to offsets at most18. The band certificate excludes that. Together with the27 exact
infinite tails, all35 light-speed patterns in the stated box are excluded on the actual seed.
By Local's carried implication, this also excludes eventual pair histories of period at most2
with r<=2 and L<=6 that fail the light-speed equation. The claim is about this bounded family,
not every period or every band width. The new general recurrence and monotone-map reductions
await an independent carrying read; no Lean verification or submission is claimed.

Second pilot COMPLETED at frozen source7c94a0aa: child0.07 CPU seconds,0.07 wall seconds,
14,467,072-byte maximum RSS; supervisor0.130 CPU seconds. Launch free+inactive6536MiB. Again
the run ended before a live sampling interval; no pressure-trajectory measurement is claimed.
Both stages and both exact source versions, raw outputs, certificates and receipts are retained
in the shared store at `cited/gpt/gc2356-genealogy-certificates-20261101.zip`,10136 bytes,
SHA256 `05daf7ec96cfd31d16625e90931629a7ad4054bea0bb4387bbfe3b217904e2a0`.
Raw-body upload receipt and byte-for-byte readback both verified with TLS enabled.

### 16.4 The remaining uniform question is sharper, but still open

The proper all-width target is: for each D, take a proved eventual period of the actual band
through D+2; its clipped rightward period map H_D has no finite fixed point. Equivalently,
H_D(s)>s for every finite state. This formulates precisely what a computation or an induction
must certify. Jen supplies eventual band periodicity, not this strict inequality.

There is also a converse to Local's reduction (**PROOF-SKETCH, GPT**). If a seed follower is
eventually confined to some finite band, choose a Jen period P for that band through D+2.
Its stroboscopic positions iterate the monotone finite map H_D without exiting. They therefore
eventually reach a fixed point, so its full offset path is eventually P-periodic. An advance
is exactly an offset increment of2, and a collision with length L has increment2-L. A bounded
periodic path cannot consist entirely of advances; its repeating runs of advances and its
nonadvance increments consequently give an eventually periodic (r,L) history. Together with
Local's carried direction, this gives the candidate equivalence on the seed:

    eventual periodicity of the pair history  <=>  eventual confinement to a finite left band.

Thus unbounded limsup distance is also necessary for nonperiodicity, under the stated Jen
input. This is a reformulation of the remaining problem, not a proof that either alternative
holds. It avoids importing a stationary distribution or measured speed.

The observed bound32 on small band periods cannot be assumed at all depths. Our already proved
LemmaB2 says the periods are unbounded, so a globally bounded power-of-two clock would contradict
known work. A useful uniform argument might exploit how H_D changes when the temporal period
doubles, together with the new diagonal's reset equation. Merely proving more finite plateaux,
or checking successive D, does not give that argument. Escaping D once also does not by itself
bootstrap escape from D+1: the front may return.

Next executable step: attempt a hand comparison between H_D and H_(D+1) across one Jen
period-doubling/reset extension, identifying the extra hypothesis that would force strict drift.
Use the exact D=18 map as a positive control and the offset4 leftward map as a negative control.
If it merely repeats the unknown no-fixed-point condition, park the uniform route rather than
increase the band. Independent alternative remains Mahler's4,11,6 threshold boundary. No new
review request or worker dispatch; this is a passive, consolidated response to the owner's
supplied Local analysis, and both schedules remain paused.

## 17. A uniform capture argument replaces the clock induction (GC2357)

**PROOF-SKETCH, GPT, 1 November 2026; independent carrying read required.** The owner asked to
continue the warm step and flag Local after this block. Trying to compare adjacent-width period
maps led instead to a local ancestry argument. It gives a uniform exit bound without assuming
periodicity of any diagonal. The subsequent stronger escape limit uses the already proved
`JenPow2.infinitely_many_black`, not a new clock bound.

Record searched: the complete GC2356/L1283 arguments and sources; L1279/GC2352's all-parent
black-prefix reach property; B1's `no_adjacent_white` and its descending-pair proof;
`tests/probes/lean/JenPow2.lean` actual `edge`, `D_succ`, `jen_pow2`,
`no_adjacent_white`, `infinitely_many_white`, `white_then_black`, `infinitely_many_black`.
Record/kit/portal searches for ancestry or descendants with leftmost/eventual/capture and for
adjacent white diagonals found these tools, not a matching quantitative ancestry claim.
Kit93d98bbe and the21:36:37Z portal index remain the last complete snapshot at the start of
the block. Targeted primary-literature web searches returned no matched ancestry theorem;
negative search is not a novelty certificate. B1's old argument is credited explicitly below.

### 17.1 Fixed frame and the meaning of a mark

Take any Rule30 row with leftmost black cell e. The right half can be arbitrary, even infinite.
Use left-edge coordinates a_j(t)=x_(e-t+j)(t), j>=0, with negative indices zero. The edge is
always black. Mark only that edge cell at time0, and propagate a mark along **every black-parent
edge**. Thus m_j(t)=1 exactly when this black cell has at least one black ancestry path back
to the initially marked edge. It is not an exclusive family label, a bit-flip influence, or
an arbitrary choice of one parent. The exact recurrences are

    a_j(t+1) = a_(j-2)(t) XOR (a_(j-1)(t) OR a_j(t)),
    m_j(t+1) = a_j(t+1) AND (m_(j-2)(t) OR m_(j-1)(t) OR m_j(t)).

Always m<=a and m_0=a_0=1. Call a diagonal *captured from time T* if m_j(t)=a_j(t) for every
t>=T: every black cell there has the marked ancestor. White cells satisfy this vacuously.

### 17.2 A quantitative version of the known white-pair descent

**Claim.** For n>=0 and any starting time T, the adjacent diagonals n,n+1 cannot both be white
at all n+1 times T,...,T+n. Equivalently some member of the pair is black during that window.

Proof by induction on n. For n=0 the edge itself is black. If a_n and a_(n+1) are both zero
through T+n, their recurrence at index n+1 implies a_(n-1)(t)=0 at times T,...,T+n-1, since
the other two inputs and the next output are zero. Hence the pair n-1,n is zero for n times,
contrary to induction. This is the finite-window version of B1's existing backwards descent;
no independence, periodicity or assertion about a long measured run enters it.

### 17.3 A black predecessor clears an unmarked lineage

Suppose diagonals j-2,j-1 are captured from time T. Set u_j=a_j AND NOT m_j. The two recurrences
give, for t>=T,

    u_j(t+1) = u_j(t) AND NOT(a_(j-2)(t) OR a_(j-1)(t)).

If the two preceding cells are white, the current cell merely copies its colour and mark.
If the left predecessor is black, a black child can only be the100 case and is marked; if
the middle predecessor is black, any black child has that marked parent. Otherwise the child
is white. These cases prove the identity. Thus once u_j becomes zero it cannot restart, and
the first black event in the predecessor pair clears it permanently.

The all-parent qualification matters: for011 with only the middle parent marked, the child
is marked under this rule, but choosing its unmarked right parent would give an unmarked child.
The argument does not assert capture for arbitrary designated-parent trees.

### 17.4 Every fixed diagonal is captured in quadratic time

Define C_0=0 and C_j=1+j(j-1)/2 for j>=1. **Claim:** diagonal j is captured from time C_j,
uniformly over the entire initial right half.

The edge is captured initially; diagonal1 is captured after one update because its parents
include the always marked black edge. For j>=2, both predecessors are captured by C_(j-1),
since C is nondecreasing. Claim17.2 applied to the pair j-2,j-1 finds a black input between
C_(j-1) and C_(j-1)+j-2. Claim17.3 therefore clears u_j by C_(j-1)+j-1=C_j, permanently.
This completes the induction. The bound is not asserted sharp.

This is ancestry coverage, not loss of other information. A cell can have the marked edge
ancestor and other black ancestors simultaneously, and its colour may still depend on other
initial bits. The argument does not make the colour evolution independent of its initial row.

### 17.5 Uniform escape and nonperiodic collision histories

Let B(t) be the rightmost marked black descendant and D(t)=B(t)-e+t. The marked set is finite
at each time, and contains the left edge. By the carried black-prefix property, its boundary
is the rightward follower under discussion. For an arbitrary band limit D, both diagonals
D+1,D+2 are captured by C_(D+2). Claim17.2 supplies a black cell on this pair by a further
D+1 steps. It is a marked black cell outside the band. Therefore the first exit occurs by

    E(D) = C_(D+2)+D+1 = (D+2)(D+3)/2.

The argument may be restarted at **any** physical time with the then-leftmost black cell.
Any rightward marked-prefix front includes that cell, hence dominates the front freshly
started from it. Thus no such front can remain in a band0..D for E(D) consecutive updates.
In particular it cannot be eventually confined to any fixed left band. This uniform statement
does not use Jen periodicity or a census over D. It supplies the strict-drift/no-fixed-point
property of every eventual clipped period map from §16, rather than assuming it in an induction.

For the seed's left founder, restart at its time-one row. Its distance from the edge is B(t)+t.
Unbounded limsup of this distance, together with Local's now carried finite-word proposition,
rules out **every eventually periodic (r,L) collision history**, not merely the35 bounded
patterns. This consequence remains PROOF-SKETCH until the new capture/exit argument is carried.
It is not a centre-column nonperiodicity theorem or a Rule30 prize solution.

A stronger qualitative conclusion uses the existing `JenPow2.infinitely_many_black`: for
every N there is j>=N that is permanently black after some time. Claim17.4 eventually marks
all its black cells, so D(t)>=j for every sufficiently large t. Hence D(t) tends to infinity,
not merely along a subsequence. No growth rate or positive physical speed follows: even a
distance growing very slowly from the left edge would satisfy this conclusion. In particular,
this does not prove B(t) tends to positive infinity or reaches the centre eventually.

### Frozen finite controls before execution

Prediction: all2048 width12 initial left-band prefixes with a black edge satisfy the capture
bounds at depths0..11, the white-pair bounds at n=0..10, and first-exit bounds for D=0..9.
Evolve exactly67 updates; compare a packed integer colour/mark update with literal scalar
Rule30 truth-table and parent-graph updates at every step. This covers every possible initial
prefix in the stated width; deeper right cells cannot affect it. The universal proof is the
induction above, not extrapolation from this test.

Counterfactual: any late unmarked black cell, overlong white-pair run, late first exit or oracle
disagreement stops the stage and refutes the claimed proof/implementation as appropriate.
Controls: all12 local marked-parent cases satisfying the captured-predecessor hypothesis;
011 right-parent-only selection fails that rule as expected; without the black-edge hypothesis
an all-white pair can persist. No random rows, density measurement, width or horizon enlargement.

Source [genealogy_capture.py](../tests/probes/genealogy_capture.py), SHA256
`ae86833ec9a338d6b0d74cb86fa7b72b80353e2fc13cf045242406775079fe6b`.
One Intel worker, nice10, no subprocesses or library threads; fixed2048*67 updates. Aggregate
CPU budget120s, child CPU check20s, launcher hard per-process30s, wall60s, tree RSS768MiB,
max2 tracked processes. As previously, per-process caps are not general aggregate enforcement;
retain actual receipts and supervisor CPU. Launch free+inactive about6517MiB, load3.46.
Launch floor4096MiB, running floor3072MiB, swap-growth stop64MiB, files16MiB, stage128MiB.
Fresh scratch directory and retained failures; any pressure/monitor failure stops the stage
without automatic retry. No GPU or thermal measurement. Flag Local only after the block,
as the owner requested, with the carrying step and controls together.

### 17.6 Control outcome, adversarial scope and review handoff

The frozen pilot at3420dc04 **COMPLETED**. All2048 initial prefixes passed all67 updates:
137216 packed/scalar step comparisons, all12 local clearing cases, capture deadlines at
j=0..11, white-pair windows at n=0..10, and exits at D=0..9. The latest observed first exits
were1,3,3,4,5,7,10,10,11,12, all below the stated universal bounds. The last unmarked-black
times were -1,0,0,1,3,3,4,5,7,10,10,11. These smaller values suggest slack in the bounds;
they are not a new linear capture law. No widening or second stage was run.

Intel receipt: child1.85 user +0.02 system CPU seconds,1.88 wall seconds,12,619,776-byte
maximum RSS; supervisor0.129 CPU seconds and2.21 wall seconds. The child reports1.820715
process CPU seconds for its main work. These are different measurement scopes. Tree samples
peaked at12756KiB and2 processes; launch free+inactive6476MiB, observed floor6472MiB, observed
swap growth0. No pressure stop. The declared120s aggregate budget was comfortably met by the
retained receipts; the launcher's per-process cap was not an aggregate CPU enforcement mechanism.

Raw output, launcher/time receipts and exact probe source are retained in the shared store at
`cited/gpt/gc2357-capture-controls-20261101.zip`,3734 bytes, SHA256
`0fb27659bc17f7f6b0607ff1a4d8188b86afe80812ba038238f3790799ed8237`.
Raw-body upload receipt and byte-for-byte readback verified with TLS enabled.

The adversarial pass distinguishes four claims:

- Capture means every black cell on a fixed left-edge diagonal eventually has the marked
  leftmost ancestor. It need not have that ancestor exclusively. It is not Boolean sensitivity.
- The same uniform argument works for every initial right half because these prefixes are
  autonomous. An interior founder without a marked leftmost edge is outside the hypotheses.
- The exit theorem is a bound on a visit to a fixed band, allowing later returns. The stronger
  limit D(t)->infinity uses the separate existing theorem about arbitrarily deep permanently
  black diagonals. A clock-period estimate is unnecessary for the exit theorem.
- Nonperiodicity concerns the infinite list of advance counts and collision lengths (r,L).
  For the seed's time-one row111, the rightmost black cell starts unmarked. Its advancing
  right edge has only that edge's black parent, so it stays unmarked and strictly ahead of the
  marked front. Every encountered white gap is therefore finite and closes by the carried gap
  law, so collisions continue. This is neither colour-column nonperiodicity nor positive speed.

**Specific carrying question for Local:** check17.2's time-window induction,17.3's clearing
identity under captured predecessors, then17.4's C_j induction and17.5's restart/dominance
argument. Does this close L1283's all-D escape premise and hence its actual-seed nonperiodic
pair-history conclusion? Separately check the stronger limit against the exact hypotheses of
`JenPow2.infinitely_many_black`. No new statement is promoted before that read. GC2356's
spatial-tail and monotone-map reductions also remain pending, but the present proof does not
need their computed classification or the unreviewed converse.

Next executable step after the read: resolve any scope/indexing objection, then prepare a
minimal formal statement of capture and band exit if the proof carries. Independent warm
alternative: Mahler's4,11,6 strict threshold boundary. Curiosity: which gate identities suffice
for this capture mechanism, and which disappear if ancestry must follow only inputs on which
the output actually depends? That would distinguish genealogical merging from information
loss, without another long trajectory. The period-map width induction is parked because this
proof bypasses it; reopen only if the uniform argument fails or a quantitative clock comparison
would answer a different stated question. Both schedules remain paused.

## 18. Local's carrying read of GC2357, and GC2356 received (L1284)

1 November 2026, 23:05 GMT. (Local now runs on Claude Fable 5.1; the owner switched the model during this block.
Same host, tools and worker.) GPT's §16 and §17 were read in full, and GPT's three probes were run on the M5
(`genealogy_tail_certificate.py` and `genealogy_capture.py` pass; `genealogy_band_certificate.py` takes the first
pilot's packet and its digest as arguments and was not replayed).

**GC2356 received.** GPT's carrying read of L1283 is accepted with its scope repairs: the light-speed statement is
net per complete cycle, the distance can oscillate inside a cycle, the left-edge persistence is `JenPow2.edge` rather
than left permutivity alone, and a forced deep word need not realize its prescribed gaps against the real right half.
The 60-digit tail labels of T5c were unsupported, as GPT says; the exact spatial-recurrence closure replaces them.
§16's own reductions (the 2T-bit tail recurrence and the monotone band map, with their converse) are not read here
and stay PROOF-SKETCH. GC2357 makes them unnecessary for the main conclusion.

**GC2357 carries: PROVED (GPT's proof, Local's read).** Each step was checked by hand in GPT's left-edge frame
a_j(t) = x_(e−t+j)(t), with all-parent marks from the edge cell.
- **17.2, the white-pair window.** If a_n and a_(n+1) are white at times T..T+n, the recurrence at index n+1 gives
  a_(n−1)(t) = 0 for t = T..T+n−1, so the pair (n−1, n) is white for n times, against the claim for n−1. The base
  n = 0 is the always-black edge. Carries.
- **17.3, the clearing identity.** With j−2 and j−1 captured at time t, write (p, q, c) for the three parents. If
  p = 1 the child is black only for (1, 0, 0) and then its black parent j−2 is marked. If p = 0 and q = 1 the child is
  black with marked parent j−1. If p = q = 0 the child copies c and its mark. So
  u_j(t+1) = u_j(t) AND NOT(p OR q). Carries.
- **17.4, capture by C_j = 1 + j(j−1)/2.** The edge is marked for ever (m_0(t+1) = a_0(t+1) AND m_0(t) = 1).
  Diagonal 1 is captured from time 1 because its parents include the edge. For j ≥ 2, 17.2 on the pair (j−2, j−1)
  from C_(j−1) gives a black input by C_(j−1) + j − 2, so 17.3 clears u_j by C_(j−1) + j − 1 = C_j, and u_j cannot
  restart. Carries.
- **17.5, exit and restart.** The marked set is all black cells of [edge, B(t)] with B the follower
  B(t+1) = max{i ≤ B+1 : black}: the §6 induction applies verbatim to any row with a leftmost black cell. Diagonals
  D+1, D+2 are captured by C_(D+2), and 17.2 puts a black, hence marked, cell on them by C_(D+2) + D + 1 = E(D).
  Marks propagate monotonically, so a front started earlier dominates one started from the current edge, and no front
  can stay in band 0..D for E(D) updates. Carries.
- **The seed.** The left founder (−1, 1) is the leftmost black cell of row 1, so its ancestry front is this marked
  front. The right edge cell (t, t) has parents (1, 0, 0) and only the previous edge as a black parent, so it is never
  marked and every gap ahead of the front is finite: there are infinitely many finite episodes. Hence
  limsup (B(t) + t) = ∞, and by the carried L1283 proposition the seed's collision history (r_k, L_k) is not
  eventually periodic.
- **The stronger limit.** `JenPow2.infinitely_many_black` has exactly the hypotheses used: x0 with a leftmost black
  cell e (he, hl), and gives for every N a k ≥ N with D x0 e k t = true for all large t, in the same coordinates
  D(k, t) = ev(t)(e − t + k). Capture then marks that diagonal, so D(t) ≥ k eventually, and D(t) → ∞. Carries.

**Theorem (two-party; hand proofs by Local and GPT, each read by the other; no Lean).** On the single-seed orbit, let
B(t) be the rightmost black cell with a black-ancestry path back to the cell (−1, 1), and let (r_k, L_k) be the
sequence of white-gap advance counts and collision run lengths of that front. Then B(t) + t → ∞, and (r_k, L_k) is
not eventually periodic.
- Chain: GC2352 (reach front), GC2353 (gap episodes), L1283 (deep-side law; periodic ⇒ bounded distance, carried in
  GC2356), GC2357 (uniform capture and escape, carried here), and `JenPow2.edge` and `infinitely_many_black` for the
  edge and the limit.
- Scope: a statement about the genealogy record, not about the centre column, and not a speed. The front's distance
  from the left edge could grow as slowly as it likes.

**Independent check on the seed (COMPUTED,
[`genealogy_capture_seed.py`](../tests/probes/genealogy_capture_seed.py)).** GPT's pilot covered every 12-bit prefix for
67 steps. On the actual orbit to t = 7,542: no white-pair window of length n+1 for n ≤ 120; the last unmarked black
cell on diagonal j comes well before C_j for all j ≤ 120 (at j = 120 it is time 113 against C = 7,141); the marked
set equals the black cells of [edge, B(t)] at every step; and restarts at every t_0 ≤ 3,000 leave band 0..D within
E(D) for D ≤ 30, the worst first exit being D or D − 1. A side observation: on the seed the capture time is about
j − 7, linear in j, far below the quadratic bound. That is a measurement on this orbit only.

## 19. The gate question (L1285, at the owner's direction)

**Review amendment:** GC2358 in §22 qualifies the sensitivity/causality language and the Rule210 extrapolation; §20 already corrects the lone-edge counterexample.

GPT's curiosity question (GC2357): which gate identities does the capture mechanism need, and what disappears if
ancestry must follow only inputs the output actually depends on? The owner chose it. Record searched: `record_find`
for orphan, sensitive parent, causal parent, left-permutive rules, rule 210, 256 rules, 64 rules; the kit's
`Rule30Equivalents.Symmetry`. Prior work used here: §8.64 (`rule30_otherrules.py`: of the 64 rules whose left edge
moves at light speed, only 30, 110 and 118 have a certified small-period band), L1282's derivative laws and
GC2357's proof. Nothing in the record asks which rules admit the capture argument or restricts ancestry to sensitive
links.

### 19.1 Which identities each step uses (by inspection of the proof; PROVED by table where stated)

Write f(a, b, c) for the local rule, with a the left parent.
- **A persistent left edge moving left one cell a step:** f(000) = 0 and f(001) = 1. The 64 rules of §8.64.
- **The white-pair descent (17.2):** f(a, 0, 0) = a, so f(100) = 1 as well. That is the only new identity.
- **The clearing identity (17.3):** f(0, 0, c) = c, which the edge pair already gives, and f(000) = 0 so that a
  black child has a black parent. The cases p = 1 and q = 1 are generic: the child's black parent is captured.
- **The follower prefix (§6) and the exit and restart (17.5):** f(000) = 0 and the edge; nothing else.
- **The seed's infinitely many episodes:** the right edge moves right unmarked, f(100) = 1 again.

So the escape theorem (capture by C_j, exit by E(D), limsup D = ∞) needs exactly three table entries,
f(000) = 0, f(001) = 1 and f(100) = 1, and should hold for the 32 rules that have them.
- **The lock (L1283):** the deep word must be a triangular bijection of the future reads, so f must be left-permutive,
  f(1, b, c) = NOT f(0, b, c); and the black front must shield the deep side from the shallow side,
  f(a, 1, 0) = f(a, 1, 1). With f(000) = 0 and f(001) = 1 this leaves two rules, **30 and 210** (PROVED by table:
  the left-permutive edge rules are 30, 90, 150, 210, and 90 and 150 fail the shield).
- **The episode structure (r, L) of GC2353** uses all eight entries. It is Rule 30's alone.
- Rule 210 is f = a XOR (NOT b AND c). It is not in Rule 30's symmetry class (30, 86, 135, 149), so the lock and the
  escape together give it, too, an ancestry front whose read history is never eventually periodic. That is a
  by-product; it is not pursued here.

### 19.2 The restricted ancestries, by hand

Rule 30's Boolean derivatives: the child always depends on its left parent; on its centre parent exactly when the
right parent is white; on its right parent exactly when the centre parent is white.
- **V0, all black parents** (GC2357): the proved capture.
- **V2, black and sensitive parents:** a mark passes from a black marked parent to a black child only if the child
  depends on that parent. A black child with parents 011 depends on neither of its two black parents (the OR is
  saturated), so it is an **orphan**: it can never be marked. The clearing identity fails there. Near the seed's
  left edge, diagonals 1, 2, 3 and 4 are eventually 1, 0, (10)* and 1 (COMPUTED to t = 600; Jen gives their
  eventual periodicity). Then the cell on diagonal 1 has parents 011 for ever, diagonal 3's black cells have parents
  100 with an unmarked left parent, and diagonal 4's have parents 011 or 001 with the right parent on diagonal 4
  itself. By induction the V2 marks from the edge should eventually be the edge cell alone.
- **V1, sensitive parents of any colour:** the edge cell's first-order cone of influence (L1282). The left link
  always holds and drops the left-edge index by 2, so every even-index cell reaches the edge. An odd-index cell needs
  one centre link, which needs a white right parent at that moment. Diagonal 1 cannot (its right parent is diagonal 1,
  eventually black); diagonal 3 can through diagonal 2 whenever diagonal 3 is white.

### 19.3 Predictions, written before the runs

**T6, the rule census** (`genealogy_gate_census.py`): every 12-bit left prefix with a black edge, zeros beyond, 67
steps, GPT's control set, for all 256 rules.
- P-A1: exactly the 64 rules with f(000) = 0 and f(001) = 1 keep a leftmost black cell moving left one per step on
  every prefix.
- P-A2: all 32 of those with f(100) = 1 pass the white-pair, capture (j ≤ 11) and exit (D ≤ 9) bounds on every
  prefix.
- P-A3: of the other 32 edge rules, at least half fail capture or exit on some prefix, with an explicit witness.
  Counterfactual: all 32 pass, in which case f(100) = 1 is needed by this proof only, not by the statement.

**T7, the restricted ancestries on the seed** (`genealogy_gate_seed.py`), rows to t = 3,000, diagonals j ≤ 60.
- P-B1: in the bulk, 0.25 ± 0.03 of black cells are orphans (parents 011).
- P-B2: under V2 the marked set from the edge is eventually the edge cell alone: D2(t) = 0 for all large t.
  Counterfactual: D2 unbounded, or bounded but positive.
- P-B3: under V1 every even diagonal is captured (all cells marked) from time j/2; diagonal 1 is never captured;
  every odd diagonal 3 ≤ j ≤ 59 is eventually captured. Counterfactual: some odd j ≥ 3 keeps unmarked cells at
  arbitrarily late times.
- P-B4: under V1 the marked front moves at exactly +1 a step (the right edge of influence), D1(t) = 2t.

What it would teach: whether GPT's capture is a fact about genealogical merging (links that carry no information do
the capturing) rather than about information flow. If P-B2 holds, the edge's causal black lineage dies while its
black genealogy captures everything: the two notions separate completely.

### 19.4 Results

Probes: [`genealogy_gate_census.py`](../tests/probes/genealogy_gate_census.py) and
[`genealogy_gate_seed.py`](../tests/probes/genealogy_gate_seed.py), each with its `.out`; three seconds each on
the M5. All COMPUTED.

**T6, the census (every 12-bit prefix, 67 steps, GPT's control set).**
- P-A1 HELD: exactly the 64 rules with f(000) = 0 and f(001) = 1 keep a light-speed left edge on every prefix.
- P-A2 HELD: all 32 of them with f(100) = 1 pass the white-pair, capture and exit bounds on every prefix.
- P-A3 HELD, with a surprise. Of the other 32 edge rules, 24 fail: on the lone-edge prefix 1000… their row stays
  a single black cell, so the pair (1, 2) is white for ever and the front never leaves band 0. **The remaining 8
  pass every bound**: rules 70, 78, 102, 110, 198, 206, 230, 238, which are exactly the edge rules with f(100) = 0
  and f(010) = f(110) = 1. So f(100) = 1 is needed by GPT's proof, and the statement holds for 40 of the 64 edge
  rules on this control set, including Rule 110. The 8 extra rules have a different mechanism (a black cell with a
  white right neighbour stays black in place), which is not analysed here.

**T7, the three ancestries on the seed (rows to 3,000).**
- P-B1 HELD: orphans, black children of 011, are 0.2509 of the bulk's black cells.
- P-B2 HELD, and sooner than predicted: under V2 (black and sensitive parents) the marked set is the edge cell alone
  from t = 2. The edge's children at time 2 are the new edge (parents 001, sensitive to the edge), an orphan
  (parents 011) and a white cell (parents 110). After that, 57 of the 60 diagonals j = 1..60 still carry unmarked
  black cells after t = 2,000; the other three are eventually white.
- P-B3 HELD: under V1 (sensitive parents of any colour) every even diagonal is captured by time j/2 + 1, every odd
  diagonal 3 ≤ j ≤ 59 by about the same time, and diagonal 1 never.
- P-B4 HELD up to the start: the V1 front is at index 2(t − 1), light speed from the mark's placement at t = 1.

### 19.5 The answer

- **The identities.** GPT's capture needs three table entries: f(000) = 0, f(001) = 1, f(100) = 1 (32 rules). The
  lock needs left-permutivity and the front's shield f(a, 1, 0) = f(a, 1, 1), which leaves Rules 30 and 210. The
  (r, L) episode structure needs the whole table.
- **What disappears under sensitive ancestry.** Everything. With marks passed only along black links the child
  depends on, the edge's lineage is the edge itself from t = 2: a quarter of all black cells are orphans whose two
  black parents are both masked, and the first one sits beside the edge at time 2. The capture theorem is therefore
  a statement about **genealogical merging through links that carry no information**. The edge's causal influence
  (V1) does spread, at light speed and over every diagonal but the first, but it travels through white cells. The
  black genealogy and the causal lineage of the edge share nothing beyond the edge.
- **For GPT's distinction.** Capture is merging, not information loss, and not information flow either: the marked
  front's rule "advance past two whites, else fall back" is genealogy's, while the influence cone's rule is the
  derivative's (L1282). The nonperiodicity theorem of L1284 is about the former.

## 20. The eight extra rules (L1286, at the owner's direction)

The census of §19 found eight edge rules with f(100) = 0 that pass GPT's capture and exit bounds anyway: 70, 78,
102, 110, 198, 206, 230, 238. By table they are exactly the edge rules with **f(p, q, 0) = q** for all p, q,
that is f(000) = 0, f(010) = 1, f(100) = 0, f(110) = 1, with f(011), f(101), f(111) free (2³ = 8). None is
left-permutive. In words: **a cell whose right neighbour is white keeps its colour.** The 64 edge rules therefore
split into three classes:
- F1, f(100) = 1 (32 rules, Rule 30 among them): a cell with white centre and right copies its left neighbour.
- F2, f(p, q, 0) = q (8 rules, Rule 110 among them).
- The rest (24 rules): f(100) = 0 and f(010) = 0 or f(110) = 0.

Record searched: §19's searches, plus `record_find` for "rule 110" and "copies its"; nothing on this split. Rule
110's single seed and its left-growing pattern are classical; nothing here concerns its computational universality.

### 20.1 The F2 mechanism (PROOF-SKETCH, Local; GPT's read requested)

In left-edge coordinates the child at index j has parents (a_(j−2), a_(j−1), a_j), and for an F2 rule
a_j(t+1) = a_(j−1)(t) whenever a_j(t) = 0.
- **Single-diagonal descent.** No diagonal n is white for n+1 consecutive times. Proof: if a_n(t) = 0 at times
  T..T+n, then a_(n−1)(t) = a_n(t+1) = 0 at times T..T+n−1, and so on down to a_0 = 0 at time T, against the black
  edge. This is stronger than Rule 30's white-pair descent, which needs both n and n+1 white.
- **Clearing.** As in §19.1, the clearing identity u_j(t+1) = u_j(t) AND NOT(a_(j−2) OR a_(j−1)) needs only
  f(0, 0, c) = c and f(000) = 0, which every edge rule has.
- **Capture.** With j−2 and j−1 captured from C_(j−1), diagonal j−2 is black within the j−1 times
  C_(j−1)..C_(j−1)+j−2, so u_j is cleared by C_(j−1) + j − 1 = C_j. The same C_j = 1 + j(j−1)/2 as GPT's.
- **Exit.** Diagonal D+1 is captured by C_(D+1) and black within D+2 further times, so band 0..D is left by
  C_(D+1) + D + 1 = (D+1)(D+2)/2 + 1, below GPT's (D+2)(D+3)/2. Restart and dominance are as in 17.5.

### 20.2 The converse for the other 24 (PROOF-SKETCH, Local)

Take the lone edge, one black cell. The next row has the new edge (parents 001) and, at index 1, f(010); index 2
has parents 100, so it is white, and so is everything beyond. If f(010) = 0 the row is a lone edge again, for ever.
If f(010) = 1 and f(110) = 0, the next row is [1, f(011), 0, 0, …]: either the lone edge again or [1, 1, 0, …]
again. In every case the marked front stays in band 0..1 for all time. So uniform escape fails.

**Characterisation (PROOF-SKETCH, both directions; the census is its control).** Among the 64 rules whose
leftmost black cell moves left one cell a step, every band 0..D is left within a bounded time from every start on
every configuration **if and only if** f(100) = 1 or f(p, q, 0) = q.

The lock of L1283 needs left-permutivity, which no F2 rule has, so the nonperiodic-history theorem does not extend
to them. For F2 rules the deep word is not even an injective function of the reads: f(0, 0, c) = f(1, 0, c) = c when
c = 0, so the left parent is invisible behind a white pair.

### 20.3 Predictions, written before the run (`genealogy_eight_rules.py`)

- P8a: on every 12-bit prefix and 67 steps, no F2 rule has a diagonal n ≤ 10 white for n+1 consecutive times.
  Rule 30 does: on the seed, diagonal 2 is white for ever (§19.2), so the mechanisms differ.
- P8b: every F2 rule leaves band 0..D within (D+1)(D+2)/2 + 1 steps from every start ≤ 20, D ≤ 9, on every prefix.
- P8c: every one of the 24 other edge rules keeps the lone edge's front in band 0..1 for all 67 steps.
- P8d: from a single seed, each F2 rule's marked front has D(2000) ≥ 200. Counterfactual: a rule whose single-seed
  front grows more slowly than a tenth of light speed; escape says only that it is unbounded.

### 20.4 Results (COMPUTED, [`genealogy_eight_rules.py`](../tests/probes/genealogy_eight_rules.py), half a second)

- P8a HELD: no F2 rule has a diagonal n ≤ 10 white for n+1 consecutive times on any of the 2,048 prefixes over 67
  steps. Rule 30 violates that window on every prefix, so the two mechanisms are genuinely different.
- P8b HELD: every F2 rule leaves band 0..D within (D+1)(D+2)/2 + 1 steps from every start ≤ 20, D ≤ 9, on every
  prefix.
- P8c HELD: under each of the 24 other edge rules the lone edge's front stays in band 0..1 for all 67 steps.
- P8d HELD, and exactly: from a single seed every F2 rule has D(t) = t, because f(100) = 0 keeps the right side white
  and f(p, q, 0) = q then keeps the seed cell black, marked by itself, for ever (one-line induction). Rule 102 is the
  additive rule q XOR c, and its row 2000 has 2^6 = 64 black cells, as Pascal's triangle mod 2 requires: a sanity
  check on the code.

**Disposition.** The eight rules are the class "a cell with a white right neighbour keeps its colour". They admit
GPT's capture through a single-diagonal descent, with the same quadratic capture time and a slightly better exit
bound, and the 64 edge rules are now classified for uniform escape by two table conditions (§20.2, PROOF-SKETCH).
None of the eight is left-permutive, so nothing about nonperiodic histories follows for them. Parked; a by-product
of the gate question, recorded for the classification.

## 21. Capture and exit in Lean (L1287, at the owner's direction)

[`tests/probes/lean/Capture.lean`](../tests/probes/lean/Capture.lean) (327 lines, SHA256 `7dad0cbe3314b12a43529811a525e5c64f65243ab5bd83007555fd1f2868f9f9`), checked with
`lake env lean LocalScratch/Capture.lean` in the Mathlib checkout used for JenPow2.lean (Lean 4.33.1). No errors,
no `sorry`; every `#print axioms` line lists `[propext, Classical.choice, Quot.sound]`. **Machine-checked.**

**What it states.** For any local rule `f : Bool → Bool → Bool → Bool` with `f 0 0 0 = 0`, `f 0 0 1 = 1` and
`f 1 0 0 = 1` (the F1 class of §19; `rule30_edgy` shows Rule 30 is one), and any configuration `x0 : ℤ → Bool`
with a leftmost black cell `e` (`x0 e = true`, `x0 j = false` for `j < e`), with marks started at `e` at time 0
and passed along every black-parent edge (`mark`), in left-edge coordinates `D k t`, `M k t`:
- `edge`: the leftmost black cell moves left one cell a step, everything left of it white.
- `pair`: diagonals `n, n+1` are not both white for `n+1` consecutive times.
- `capture`: for all `j` and `t ≥ C j`, a black cell on diagonal `j` is marked, where `C 0 = 0`, `C 1 = 1`,
  `C (j+2) = C (j+1) + j + 1`; `C_closed`: `2 C (j+1) = j (j+1) + 2`, that is `C j = 1 + j(j−1)/2`.
- `exit`: for all `D` and `t0`, some `t ∈ [t0, t0 + C (D+2) + D + 1]` has a marked cell on a diagonal `k > D`.
- `unbounded`: the marked front is beyond every `D` at arbitrarily late times.
- `capture30`, `exit30`: the Rule 30 instances.

**What it does not state.** The deep-side lock (L1283), the gap episodes (GC2353) and the nonperiodicity of the
seed's collision history remain hand proofs with two readers. The link from `exit` to L1283's premise is the
identification of the marked front with the ancestry follower, also hand (§6, §18). The stronger limit D(t) → ∞
uses `JenPow2.infinitely_many_black`, in another file.

**Shape of the proof.** 17.2 is `pair` (induction on `n`, one `by_contra`); 17.3 is `clear` and `persist`;
17.4 is `cap_step` (an inner induction along time) and `capture_pair` (induction on `j`, carrying two diagonals);
17.5 is `exit`, which takes `T = max t0 (C (D+2))` and needs no restart argument, since marks started at time 0
are what the theorem is about. The three table entries are used exactly where §19.1 says: `h001`, `h000` in
`edge`, `h100` in `pair`, `h000` in `persist`.

**Replay.** Copy the file into a Mathlib project and run `lake env lean` on it; the Intel's elan has 4.33.1. A port
to the kit's core Lean 4.35 (no Mathlib: `push_cast`, `ring` and `simp` would need replacing) is a separate task.

## 22. GPT review of L1284–L1287 and the exact Lean packet (GC2358)

**Verdict: the main Rule30 theorem carries; F1/F2 escape classification carries; Lean statement
and source fidelity PASS.** Read all of §§18–21, all327 lines of `Capture.lean` at b4e13e34,
and the census/sensitivity probe sources. No new simulation or compiler replay was run.
The exact Lean source SHA256 is
`7dad0cbe3314b12a43529811a525e5c64f65243ab5bd83007555fd1f2868f9f9`.
This is a review of the existing proof packet, not a novelty or submission audit.

### 22.1 The main conclusion and what the Lean file checks

Local L1284 independently carries every new step of GC2357, including the restart domination
and the stronger limit's use of the existing Jen theorem. Together with the previously carried
L1283 lock, this completes the two-reader hand chain: the seed's front from (-1,1) has
B(t)+t tending to infinity, and its infinite (r,L) collision history is not eventually periodic.
Neither finite sampling nor the unreviewed GC2356 tail classification is needed in this chain.
The right edge's unmarked unique ancestry guarantees infinitely many finite episodes.

The formal source states the intended marking convention: `mark` starts only at e and a later
mark requires a black output and at least one marked parent. The hypotheses `he` and `hl` say
that e really is black and everything left of it is white; the initial right half is unrestricted.
`M_imp_D` checks marks imply black. The coordinates `e-t+k`, the two predecessor indices,
and the exceptional bases k=0,1 agree with the hand proof.

`pair` uses only the F1 table entries and the persistent edge. `clear` and `persist` prove the
marking implication needed for capture; they do not assume the capture conclusion. `cap_step`
propagates it forward in time, and `capture_pair` inducts over adjacent diagonals. `C_closed`
is the exact division-free identity 2*C(j+1)=j*(j+1)+2: the displayed formula
C_j=1+j(j-1)/2 applies to j>=1, with C_0=0 separately.

`exit` chooses T=max(t0,C(D+2)), then applies `pair` to D+1,D+2. Both diagonals have already
been captured at T; the bound follows from T+s<=t0+C(D+2)+D+1. This proves a marked cell beyond
the band at a bounded later time, for marks originally started at time0. It needs no formal
restart construction. `unbounded` drops the upper bound; it is an arbitrarily-late escape
statement, not the stronger eventual lower bound B(t)+t->infinity.

No `sorry`, extra axioms, changed evolution or hidden periodicity hypothesis occurs in the
source. **Compilation remains Local's reported Lean4.33.1/Mathlib check**, with standard axioms;
GPT has reviewed the source and statements, not replayed that check. Intel has the Lean
compiler, but no matching Mathlib project was found in the checked workspace/cache locations.
The best-tool build is already supplied by Local; no substitute checker or large dependency
installation was attempted. For a reproducible delivery packet, retain the Mathlib commit,
lake manifest and raw command/axiom log. A kit-core4.35 port and portal validation remain
separate tasks. The file does not formalise the follower identification, deep-word lock, gap
law, nonperiodic history or the stronger limit; the report correctly keeps those separate.

### 22.2 The eight extra rules and the converse carry

L1286's single-diagonal descent is valid: if a_n is zero at T,...,T+n, the F2 identity at each
of the first n times forces a_(n-1)=0 at T,...,T+n-1, contradicting the lower-depth induction.
The base contains the black edge. Clearing needs only f(0,0,c)=c, so it works in both F1 and F2.
For j>=2, the single-diagonal window at j-2 clears j by C_(j-1)+j-1=C_j. The bases remain the
marked edge and its neighbour. Once D+1 is captured, its own window supplies a marked black
cell by C_(D+1)+D+1=(D+1)(D+2)/2+1. The arithmetic includes D=0.

The converse needs a band of width1, not always a lone cell. If f(100)=f(010)=0, the lone edge
repeats in the moving frame. If f(100)=0, f(010)=1, f(110)=0, the set of two possible rows
{1000...,1100...} is closed: 1000... maps to1100..., and1100... maps to
[1,f(011),0,0,...]. Thus all24 remaining rules have a permanently confined seed front.
Rule6 already refutes §19.4's stronger claim that all24 stay a single cell; it alternates these
two rows. §20.2 gives the correct proof. The disjoint table classes have32,8,24 members.

For completeness, the prefix property used in the prose needs no Rule30-specific gate: since
f(000)=0, every black child has a black parent. A black child at or left of B-2 has only parents
inside the marked prefix; at B-1,B,B+1 it has the marked black parent at B. Conversely no marked
child can lie beyond B+1. This proves the same black-prefix follower identity for every edge
rule and justifies using the marked set in the classification. Marking is monotone under
inclusion of the initially marked set. Therefore L1286's characterisation is **PROVED,
two-party hand**, for all-parent black-prefix followers on rows with a leftmost black cell:
uniform finite-band escape holds exactly in F1 or F2. It is not inferred from the census.

### 22.3 Corrections to surrounding interpretations

1. **Sensitivity paths are not actual damage.** V1 propagates existence of a path of locally
   nonzero Boolean derivatives using OR. It is the first-order path-support graph, not a proof
   that flipping the founder changes every reached cell. L1282 already distinguishes this
   graph from the mod2 tangent and actual nonlinear damage. Replace unqualified claims that
   V1 is the actual causal-influence cone accordingly.
2. **Masked does not mean information-free.** At011, flipping either black parent alone leaves
   the output black, but flipping both gives000 and a white output. The precise claim is zero
   individual Boolean derivatives at that local state; the parents still matter jointly.
   V2 therefore collapses to the edge in this example, rather than its lineage dying entirely.
   The measured0.2509 orphan share is a finite bulk measurement, not an exact quarter theorem;
   observing57 diagonals after time2000 alone does not prove an infinite-time statement for57.
3. **Rule210 needs its own read law.** The finite truth-table calculation that the two stated
   left-permutive shield conditions select30 and210 is correct. It does not by itself transfer
   L1283's nonperiodic-history theorem: that proof uses a specified injective sequence of reads
   and collision updates, while §19 itself notes that the (r,L) episode law is Rule30-specific.
   The Rule210 nonperiodicity sentence in §19.1 is therefore uncarried and should remain a
   proposed extension until its observable, update and reconstruction are proved. This is
   not a counterexample to the possible extension and does not affect the Rule30 theorem.

No new long compute or external submission is needed to settle this review. Next concrete
step: preserve the exact Mathlib build provenance, apply these wording qualifications, and
choose separately whether to formalise the remaining Rule30 hand chain. The F2 classification
is an independent proved by-product; positive physical speed and centre-column behaviour are
still open. Both schedules remain paused.
