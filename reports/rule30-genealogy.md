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
