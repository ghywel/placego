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
  escape might give it, too, an ancestry front whose read history is never eventually periodic. *Corrected after
  GC2358:* that is a proposed extension, not a result; the lock's proof uses Rule 30's own read law (GC2353), which
  Rule 210 would need in its own form. Not pursued.

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
- P-A3 HELD, with a surprise. Of the other 32 edge rules, 24 fail: on the lone-edge prefix 1000… their marked
  front stays in band 0..1 for ever (§20.2 has the correct proof: a lone cell, or two rows of width one and two
  alternating, as Rule 6 does; GC2358 corrected an earlier "stays a single cell" here). **The remaining 8
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
  a statement about **genealogical merging through links with zero individual Boolean derivative** (GC2358's
  correction: the two black parents of an 011 child still matter jointly, since flipping both whitens it; "carry no
  information" was too strong). The edge's first-order path support (V1; the existence of a path of nonzero
  derivatives, not actual damage, L1282) does spread, at light speed and over every diagonal but the first, but it
  travels through white cells. The black genealogy and the first-order path support of the edge share nothing
  beyond the edge.
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

## 23. GPT's three questions about the centre (L1288)

GPT (1 November 2026, after L1287) proposes the next block: what allows a black centre cell to stay outside the
left founder's family. Three questions: (1) capture of the centre, with the benchmark T(j) ≤ j for large j, where
T(j) is the capture time of diagonal j; (2) the backward structure an unmarked black centre cell must bring with
it; (3) what centre capture forces the colours to do. Local's hand answers first, then a measurement.

### 23.1 The three questions by hand (PROOF-SKETCH where marked)

Facts in hand: the marked cells at time t are the black cells of [−t, B(t)] (§6, carried); the follower rule
B(t+1) = max{i ≤ B(t)+1 : black}; a non-advance retreats by L − 1, with L the black run ending at the front
(GC2353); a white gap of M cells gives ⌊M/2⌋ advances with the gap's interior white throughout (C3).

**Q1 is the sign of the drift.** Diagonal j is captured from T(j) iff D(t) = B(t) + t ≥ j at every t ≥ T(j) at
which diagonal j is black. So T(j) ≤ j for all large j ⇔ B(t) ≥ 0 at every large t at which the centre is black.
The benchmark is exactly "the front never again falls behind the centre". Measured, B(t) ≈ 0.047 t; proved,
only limsup D = ∞. So Q1 is the positive-speed question in a sharper form: not a rate, but a sign, for ever.

**Q2: the backward structure is the front, and nothing more.** A black cell is unmarked iff it lies right of
B(t); its black ancestry at time s lies right of B(s) for every s, and reaches time 1 only at the right founder
(1, 1) (T1b: the middle founder's family is inside the left founder's). There is no further restriction: every
black cell right of the front has such an ancestry. What the structure does say is **how the centre could be lost**
(PROOF-SKETCH):
- The front falls behind the centre only by a retreat, which needs a black run of length L ≥ B(t) + 2 ending at
  the front, that is a row black from position −1 or further left all the way to B(t). At the retreat step the
  centre turns white (it is inside the run).
- The gap then closes from both ends with its interior white (C3). The centre becomes black and unmarked only if
  the right boundary reaches it before the front does, which needs L > 2B(t) + 3.
- Otherwise the front reaches the centre first and the centre is marked when it next turns black.
So an unmarked black centre cell after time t needs, at some time t' ≥ t, a black run of more than 2B(t') + 3
cells ending at the front: with B(t') ≈ 0.047 t', a run of about a tenth of t'. The runs at the front look like fair-coin
runs (L1281: mean 2.01), so a heuristic sum Σ 2^(−0.094 t') converges: the centre should be lost only finitely
often. That is a CONJECTURE with a heuristic, not an argument; on the seed the runs are one fixed sequence.

**Q3: the front leaves the centre behind.** The collision history happens at the front, which drifts right of
the centre at about 0.047 cells a step (MEASURED). After the front passes, the centre is deep inside the left
family and the collisions happen ever farther away. So no implication from a repeating centre colour pattern to a
repeating collision history is expected through this front; they are decoupled in space. A bridge would have to
go through a different object, say the ancestry of the centre cells themselves rather than the family's boundary.

### 23.2 Predictions, written before the run (`genealogy_centre.py`)

- P9a: B(t) < 0 only at times t < 50; from then on the centre's black cells are all marked (none unmarked at any
  later time to 20,000).
- P9b: on t ∈ [1,000, 100,000], B(t) ≥ 30 throughout (the front never comes back near the centre).
- P9c: no retreat at a time t ≥ 100 has L > 2B(t) + 3; the largest ratio (L − 1)/(B(t) + 1) over t ≥ 1,000 is
  below 0.5.
- P9d: the capture benchmark: T(j) ≤ j for every j ≥ 100 up to 20,000, with margin j − T(j) ≥ 0.03 j for j ≥ 1,000.
- P9e: the black runs at the front have P(L ≥ ℓ) within a factor 1.5 of 2^(1−ℓ) for ℓ ≤ 10 (the fair-coin shape
  behind the heuristic).
- Counterfactual: a late retreat reaching the centre, or a margin that shrinks with j.

### 23.3 Results, and the reply to GPT (L1288)

Probe [`genealogy_centre.py`](../tests/probes/genealogy_centre.py), [output](../tests/probes/genealogy_centre.out),
a second on the M5. COMPUTED on the stated windows; the speed statements are MEASURED.
- P9a HELD: B(t) < 0 at four times only, the last t = 7. No black centre cell is unmarked at any time to 20,000.
- P9b HELD: on [1,000, 100,000] the front never comes below B = 66 (and never below 500 after 10,000);
  B(100,000) = 4,746.
- P9c HELD: no non-advance at t ≥ 100 has L > 2B + 3; the largest (L − 1)/(B + 1) at t ≥ 1,000 is 0.067 (a run of 7
  against B = 89). The longest run ever seen at the front is 13.
- P9d HELD: T(j) ≤ j for every j in [100, 20,000]; the margin j − T(j) is at least 65 for j ≥ 1,000, at least
  4.6% of j; T(20,000) = 19,075.
- P9e HELD: P(L ≥ ℓ) is within a factor 1.41 of 2^(1−ℓ) for ℓ ≤ 10.

**Reply to GPT.** Q1's benchmark holds on the orbit with a growing margin, and it is the sign of the drift in
disguise: T(j) ≤ j eventually ⇔ B(t) ≥ 0 eventually. Q2's backward structure is exactly the front: an unmarked
black cell is one right of B(t), and the only way the centre can be lost is a black run of more than 2B + 3 cells
ending at the front (§23.1). Nothing of that size occurs after t = 7; the largest late run is a tenth of what would
be needed, and the run lengths at the front look like fair-coin runs, which is the heuristic behind "lost only finitely
often" (CONJECTURE). Q3 is decoupled in space: the front drifts away from the centre. So the centre's capture is
not a new obstruction problem; it is the positive-speed problem, and GPT's own guard applies (two blocks on the same
open inference). The reusable content is the exact loss mechanism, which turns "B(t) ≥ 0 for ever" into "no black run
of length 2B + 4 ever ends at the front".

**GC2358 received.** Its carry of L1284–L1286 and its source review of Capture.lean are accepted, with the three
wording corrections applied above in §19 (first-order path support, not damage; zero individual derivatives, not
information-free; Rule 210 uncarried) and the §19.4 confinement correction. **Lean build provenance, as requested:**
formal-conjectures checkout at commit b3f26411f06b0b0ec1923da80b62585f23288d39, Mathlib revision 0df444a360ea,
Batteries 4488d40d070b, `lake env lean` with Lean 4.33.1 (commit 819816b2, arm64-apple-darwin), file SHA256 as in
§21; the raw run printed only the five `#print axioms` lines, each `[propext, Classical.choice, Quot.sound]`.

## 24. The arithmetic behind the front (L1290; Local's own pull)

The pull, noticed at L1283 and dropped until the owner caught it (INSTINCT.md, L1289): the cells behind the ancestry
front (the deep word w) run the right-edge map Φ and are read and shifted at each collision. That is a 2-adic
isometry followed by a digit-reading shift, the shape of the Collatz and Mahler maps. What does the arithmetic say?

Record searched: `record_find` for Terras, Syracuse, Bernstein, bit length, cycle equation, 2^b − 3^a, Anashin;
GC2355 already cites Bernstein and Lagarias (1996) for the residue-compatible isometry framework; COLLATZ-PRIZE.md
and G50/G51 for Mahler. Known: the Terras/Bernstein–Lagarias coding (parity vectors ↔ 2-adic integers) and its
analogue here, GPT's codec (GC2355).

### 24.1 By hand (PROOF-SKETCH, Local)

Write the deep word as a 2-adic integer, bit 0 the cell just behind the front. GPT's form (GC2356):
Φ(x) = x XOR ((x≪1) OR (x≪2) OR 3).
- **Syracuse form of the deep-side law.** L1283's law is, exactly,

      L = 1 + v_2(Φ^r(w) + 1),      w' = ⌊Φ^(r+1)(w) / 2^L⌋,

  since the scan reads the trailing ones of Φ^r(w) and the shift drops L digits. Compare the Syracuse map
  n ↦ (3n + 1) / 2^(v_2(3n+1)): an isometry of Z_2, then a shift by a valuation.
- **Exact growth.** For every natural number x ≥ 1, Φ adds exactly 2 to the bit length: the top bit m of x puts a 1
  at m + 2 through x≪2 and nothing above. So on a finite-left row the deep word's bit length D obeys, per episode,

      D' = D + 2(r + 1) − L,

  exactly. Collatz's analogue is log₂ n changing by log₂ 3 − v + log₂(1 + 1/(3n)) per Syracuse step: an irrational
  rate plus a correction. **Rule 30's deep side is a Syracuse-type map whose growth exponent is the integer 2 and
  whose size bookkeeping is exact.** This is why L1283's cycle lock worked: a periodic history must return the bit
  length exactly, ΣL = 2Σ(r+1), with no correction term. For Collatz the same bookkeeping gives the cycle equation
  n(2^b − 3^a) = c, which constrains but does not forbid.
- **Where ×3 lives, and how little.** Mod 4, Φ(x) = x XOR 3 = 3 − x ≡ 3x + 3. That is a two-bit accident (XOR with 11
  is subtraction from 3, and −1 ≡ 3 mod 4). Mod 8, Φ has the cycles (0 3 4 7), (1 6), (2 5); 3x + 3 has the same
  orbit of 0 but joins the rest into one 4-cycle (1 6 5 2).

### 24.2 Predictions, written before the run (`deep_arithmetic.py`)

- P10a: on the seed to t = 5,000, the Syracuse form reproduces the whole next deep word (as an exact integer, every
  bit) at every episode, and the bit length at each episode start equals B(u) + u.
- P10b: Φ adds exactly 2 to the bit length of every x in [1, 2^16).
- P10c: no affine map x ↦ ax + b (a odd) on Z/8 has cycle type (4, 2, 2). So Φ is not conjugate to any affine map of
  Z_2, already at level 3. Counterfactual: one does, and the ×3 resemblance could be a change of coordinates.
- P10d: Φ's orbit of 0 (the frozen ruler) agrees with 3x + 3's mod 8 for all n and first disagrees mod 16 or mod 32.
- P10e: Φ on Z/2^k, k ≤ 20: every cycle length is a power of 2; the longest is 2^⌈(2k−1)/3⌉ (G249's bound,
  attained by the orbit of 0); the number of cycles is at least 2^k / 2^⌈(2k−1)/3⌉. Beyond that bound I do not know
  how the count grows; that is the measurement.
- P10f: on the seed the mean per-episode change of D is about 2.2 bits and of B about 0.10, against Collatz's mean
  −0.415 bits per Syracuse step for random n.

### 24.3 Results (COMPUTED, [`deep_arithmetic.py`](../tests/probes/deep_arithmetic.py), [output](../tests/probes/deep_arithmetic.out), under a second)

- **P10a HELD.** On the seed to t = 4,991, the Syracuse form L = 1 + v_2(Φ^r(w) + 1), w' = ⌊Φ^(r+1)(w)/2^L⌋
  reproduces the whole next deep word, as an exact integer of up to about 5,000 bits, at all 2,409 episodes. The bit
  length at every episode start is B(u) + u.
- **P10b HELD.** Φ adds exactly 2 to the bit length of every x in [1, 2^16), as the hand argument says for all x.
- **P10c HELD.** No affine map x ↦ ax + b (a odd) on Z/8 has Φ's cycle type (4, 2, 2). The affine types are (8),
  (4, 4), (2, 2, 2, 2), (2, 2, 2, 1, 1), (2, 2, 1, 1, 1, 1) and (1⁸). So Φ is conjugate to no affine map of Z_2,
  already modulo 8. This complements GPT's GC2212, which showed Φ is nowhere uniformly differentiable modulo 16.
- **P10d HELD.** The orbit of 0 under Φ and under 3x + 3 first disagree modulo 32, at step 3 (55 against 39). Both
  are periodic modulo 16 with period 8 and agree on a whole period. So, **exactly and for all n, the four cells just
  below the seed's right edge at time n are the low four bits of (3^(n+1) − 3)/2** (PROVED by finite check of one
  period). The fifth cell breaks it. Cloud's COLLATZ-PRIZE §8 compared the edge's diagonal periods with the bits of
  3^t; this is an exact identity at four depths, and only there.
- **P10e: partly REFUTED.**
  - Held: every cycle length of Φ on Z/2^k (k ≤ 20) is a power of 2, and the cycle count is at least
    2^k / 2^⌈(2k−1)/3⌉.
  - Refuted: the longest cycle attains G249's bound 2^⌈(2k−1)/3⌉ only for k ≤ 9. From k = 10 it falls below
    (2,048 against 8,192 at k = 20).
  - Refuted: the orbit of 0 is not the longest cycle. Its period stalls at 64 for k = 9..14 and at 256 for
    k = 16..20, because at t = 2^m a white triangle opens below the right edge (§8.73's ruler). G249 is an upper
    bound and stays true; it is not tight beyond nine digits.
  - The measurement: cycle counts 1, 2, 3, 4, 6, 8, 10, 14, 20, 32, 52, 78, 114, 170, 252, 376, 578, 902, 1,396,
    2,180 for k = 1..20, growing by about 1.55 a level. Φ is far from transitive: the edge clock shatters into many
    short clocks.
  - Persistent short cycles (2, 2, 4, 8, 8, 8, 16, 16, then 64 of length 32 from k = 16 on) are 2-adic periodic
    points of Φ: configurations behind a black front that repeat exactly for ever.
- **P10f HELD.** Per episode on the seed, the bit length D grows by 2.18 on average and B by 0.109. A Syracuse step
  of the Collatz map on a random n changes log₂ n by log₂ 3 − 2 = −0.415.

### 24.4 What the arithmetic teaches

| | Syracuse (Collatz) | The deep side of the ancestry front |
|---|---|---|
| Isometry of Z_2 | n ↦ 3n + 1, affine | Φ, conjugate to no affine map; equals 3x + 3 only mod 4, and on the edge's own orbit mod 16 |
| Digit read | v = v_2(3n + 1) | L = 1 + v_2(Φ^r(w) + 1), r from the shallow side |
| Size change per step | log₂ 3 − v + log₂(1 + 1/3n), irrational, inexact | 2(r + 1) − L bits, exact integer |
| Coding theorem | Terras: parity vectors ↔ 2-adic integers | GPT's codec (GC2355) |
| Periodic histories | the cycle equation n(2^b − 3^a) = c | exact length lock: ΣL = 2Σ(r+1) (L1283), then killed by capture (GC2357) |

**The transfer lesson.** Rule 30's deep side is a Syracuse-type map whose growth exponent is the integer 2, so its
size bookkeeping is exact. That is precisely why its periodic histories could be locked and then excluded, while
Collatz's periodic orbits survive as the cycle equation. The obstruction for Collatz in this light is the inexact
size: log₂ 3 is irrational and 3n + 1 changes bit length by 1 or 2 depending on n. The ×3 in Rule 30 is a shallow
two- to four-digit coincidence, not a conjugacy. This is an explanation, not a Collatz result. It belongs with the
window principle of COLLATZ-PRIZE §5, which already says both problems repeat a trace block only if the state is
large enough.

## 25. The eternal cycles behind a black front (L1291; Local's own pull)

An **eternal cycle** is a 2-adic integer x with Φ^p(x) = x: an infinite configuration behind a permanently black
front cell that repeats exactly every p steps in the front's frame. As a configuration of the line it is a row with a
black rightmost cell, white beyond, that recurs at velocity +1: F^p x = σ^(−p) x.

Record searched: the kit's `Rule30FrozenRuler` (the edge map T, citing Coven, Pivato and Yassawi 2007) and
`Rule30Equivalents.PeriodicPoints` (kit ee2f421 locally, f1cb20be indexed). PeriodicPoints proves that a
configuration recurring at any velocity in [−1, 1) is spatially periodic, and that Rule 30 has exactly three fixed
points (white and the two phases of …0101…). **It excludes velocity +1, which is exactly the eternal-cycle case.**
GC808 (GPT, 9 October) carried the CPY odometer for the single seed's orbit closure and gave T's three-state decoder
(states 00, 01, and 10 or 11). `record_find` for eternal, periodic point, black-edge code: nothing on periodic points
of the edge map.

### 25.1 By hand (PROOF-SKETCH, Local)

- **Periods are powers of two.** Φ is triangular, so on Z/2^k every cycle length is a power of 2 (a cycle lifts to
  one cycle of twice the length or two of the same length). A 2-adic periodic point's period is the limit of its
  level periods, hence a power of 2. **So no row with a black rightmost cell recurs at light speed with a period
  that is not a power of two.** In particular the ring backgrounds of CL672 (time periods 28, 63, 57, 68) cannot sit
  exactly behind a black front.
- **No fixed point.** Bit 0 always flips.
- **Period 2 is the rain.** For x = …0101 (−1/3) and x = …1010 (−2/3), every OR from bit 2 on sees an alternating
  pair, so it is 1, and the two boundary bits flip too: Φ swaps them. These are the black front followed by the
  fixed point …0101… of PeriodicPoints, one cell in.
- **The light-speed condition is a constraint, not a determination.** For velocity in [−1, 1) the kit uses left
  permutivity to solve for the leftmost cell. At velocity +1 that cell cancels: F^p(x)_i = x_(i−p) XOR H(x_(i−p+1..i+p))
  must equal x_(i−p), so the condition is H = 0 on every window of 2p cells. The light-speed recurrers of period p are
  therefore a subshift of finite type, which may be finite or uncountable. That is the question.

### 25.2 Predictions, written before the run (`eternal_cycles.py`)

The solutions of Φ^p(x) ≡ x mod 2^k are found level by level. Both lifts of a solution survive or both die, since
bit k of Φ^p(x) is bit k of x XOR a function of the lower bits. Count the projections to level K of the solutions
that survive to level 60, for p = 1, 2, …, 128.
- P11a: period 1, none; period 2, exactly the rain orbit {−1/3, −2/3}.
- P11b: every eternal point has power-of-2 period (the hand argument).
- P11c: for p ≤ 32 the projections stabilize in K: finitely many eternal points, at most eight orbits of period at
  most 32 in all. Counterfactual: projections growing with K, an uncountable set of eternal configurations
  (light-speed recurrence with positive entropy).
- P11d: every eternal point found has eventually periodic digits: a spatially periodic interior behind the front.
  Counterfactual: an aperiodic eternal cycle, a configuration that is not spatially periodic yet repeats exactly at
  light speed, which PeriodicPoints shows cannot happen at any slower velocity.

**T11 follow-up, written after the first output and before its run.** Up to period 32, every solution surviving to
digit 60 agrees with the rain on its first 40 digits, so the rain is the only eternal cycle there. At period 64,
thousands of branches that leave the rain early survive to digit 60. To see whether they are eternal or long-lived
transients:
- count the period-64 survivors' projections to K = 8, 16, 24, 32 for survival depths 40, 48, 56 and 63;
- test the deepest survivors' digits for an eventual period.

Prediction: the projections at fixed K stay the same as the survival depth grows, so the branches are eternal; and
their digits are eventually periodic, so they are spatially periodic backgrounds with a permanently black column.
Counterfactual: the projections shrink with depth (transients), or the digits are aperiodic.

**T11 second follow-up, written after the 63-digit output and before its run.** The 63-digit survivors are mostly
rain for d digits and then a deviation. By hand (PROOF-SKETCH): inside rain the two cells any deeper cell reads are
complementary, so their OR is 1. The cell just past a rain stretch therefore sees a saturated OR, exactly as behind
a black front, and the cell after it sees a boundary that is black every other step. So a rain stretch acts as a
half-black front of period 2, the same at every depth up to parity. Hence the hypothesis: the period-64 eternal
points form a self-similar family "front, rain to depth d, then a core Y", one member for every admissible d,
accumulating at the rain point. The test, with 128-bit arithmetic:
- the projections to K = 16, 24, 32, 40 of period-64 survivors, for survival depths 63, 80, 100 and 127;
- the survivors that leave the rain at digit 1 or 2 (the cores), and whether their digits are eventually periodic.

Prediction: the projections stabilize by survival depth 100, so the family is genuinely eternal; there are
finitely many cores, at most eight; and their digits are eventually periodic. Counterfactual: projections still
shrinking at depth 127 (long-lived transients, no eternal period-64 points), or aperiodic cores.

### 25.3 Results (COMPUTED; probes [`eternal_cycles.py`](../tests/probes/eternal_cycles.py) and [`eternal_cycles_128.py`](../tests/probes/eternal_cycles_128.py), with outputs)

- **P11a HELD.** Φ has no fixed point, and the rain orbit {−1/3, −2/3} is an eternal 2-cycle.
- **P11b** is the hand argument; nothing contradicts it.
- **P11c HELD for p ≤ 32.** Every 2-adic solution of Φ^p(x) ≡ x that survives to digit 60 agrees with the rain on its
  first 40 digits. No other eternal cycle of period ≤ 32 leaves the rain within 40 digits.
- **Period 64, first prediction REFUTED (an eternal family), second prediction REFUTED (finitely many eternal cores
  with periodic digits).** At 63-digit precision, thousands of period-64 branches that leave the rain as early as
  digit 8 survive. At 127 digits they are gone. The projections to K = 16 fall from 776 (survival depth 63) to 456
  (depth 100) to 2 (depth 127), the rain alone. Every survivor at depth 127 agrees with the rain on at least 23
  digits, and no core leaves it within 2 digits.
  - So the family is long-lived transients. *Corrected in §26.1 (L1292):* an earlier sentence here said a branch
    survives "four to six times as many digits as it first followed the rain". That misread the data. What happens
    after a branch leaves the rain depends only on its first defect, not on the rain's length. The post-defect
    lifetime is a constant for each period, at most 104 digits at period 64 (§26.3). The rain prefix only delays the
    defect.
- **P11d:** the only eternal cycle found, the rain, has periodic digits.

**Conjecture (light-speed recurrence).** The black front followed by rain, in its two phases, is the only eternal
cycle of the edge map. Evidence: none other leaves the rain within 40 digits for any period ≤ 32, or within 23
digits for period 64.
- Combined with the kit's PeriodicPoints, which forbids non-periodic recurrence below light speed, it would say:
  **the only nonzero rows that are white beyond some cell and recur exactly, F^p x = σ^d x, are the two phases of
  rain behind a black cell. They move right at light speed with period 2.**
- That is a light-speed counterpart of the kit's classification of fixed points.
- It would also say why no exactly periodic background can ever sit behind a black front: only rain can.

**A route to a proof (my own pull).**
- A non-rain edge code has a first **defect**, two equal adjacent digits. Above it is rain, whose OR is saturated.
- At the defect the OR alternates in time, so the period doubles there. The equal pair itself persists, because both
  digits toggle together under the rain above.
- If the defect can be shown to propagate a doubling to ever deeper digits, every non-rain code has unbounded level
  periods, and so is not eternal.
- This is a finite induction on the defect's neighbourhood. The measured lifetimes suggest it is true but not
  immediate.

## 26. A proof attempt for the light-speed recurrence conjecture (L1292)

At the owner's go-ahead ("Yes, try the proof").

### 26.1 Reduction to a finite graph for each period (PROOF-SKETCH, Local)

Let x be an eternal point of period dividing p = 2^m. Each column c_k (digit k as a function of time) is then a
p-periodic binary sequence, a ring of length p, and the edge map reads, column by column,

    c_k(t+1) = c_k(t) XOR (c_(k−1)(t) OR c_(k−2)(t)),    with c_(−1) ≡ 1 (the front) and c_(−2) ≡ 0.

So c_k is the running XOR of the ring c_(k−1) OR c_(k−2), started from the free bit c_k(0). It is p-periodic exactly
when that OR ring has even weight. The pair (c_(k−1), c_k) is therefore a state in a finite graph: from (u, v) go to
(v, w), where w is one of the two integrals of u OR v, an edge existing only if u OR v has even weight. Eternal points
of period dividing p are exactly the infinite paths from the start (0, 1).
- Let a be the alternating ring (0101…) and ā its complement. The rain is the cycle (a, ā) ↔ (ā, a). From a rain
  state the OR is all ones, so the next column is a or ā: back into the rain, or into an in-phase pair (a, a) or
  (ā, ā), the **first defect**.
- Every non-rain point passes through a first defect, and (ā, ā) is (a, a) shifted by one step in time, which is a
  symmetry. So **what happens after a defect does not depend on how long the rain lasted above it.** That corrects
  §25.3: the period-64 transients do not survive "about five times their rain prefix". The data fit a constant
  post-defect lifetime of roughly 85 to 120 digits (survivors that diverged before digit 16 reach depth 100 but not
  127).
- The conjecture at period p is therefore equivalent to: **from the defect state (a, a), the reachable graph has no
  cycle and no edge back into the rain.** That is a finite check, and an exact proof for that p.

### 26.2 Predictions, written before the run (`eternal_proof.py`)

- P12a: for p = 2, 4, 8, 16, 32 and 64 the defect's reachable graph is acyclic and never re-enters the rain. So the
  black-edged rain is the only eternal cycle of period dividing p, for every p ≤ 64 (machine-checked).
- P12b: the longest path from the defect at p = 64 (the most digits a configuration can follow after its first
  defect while keeping period 64) lies between 85 and 120.
- P12c: the longest path grows about linearly in p, with ratio between 1 and 3.
- Counterfactual: a cycle in any of these graphs is a non-rain eternal cycle and refutes the conjecture.

### 26.3 Results (machine-checked; [`eternal_proof.py`](../tests/probes/eternal_proof.py), [output](../tests/probes/eternal_proof.out), 20 seconds)

| period p | states reachable from the defect | edges back into the rain | cycle | longest path after the defect |
|---:|---:|---:|---|---:|
| 2 | 2 | 0 | none | 1 |
| 4 | 6 | 0 | none | 2 |
| 8 | 30 | 0 | none | 4 |
| 16 | 62 | 0 | none | 5 |
| 32 | 2,110 | 0 | none | 15 |
| 64 | 171,774 | 0 | none | 104 |

- **P12a HELD.** **Theorem (machine-checked).** For every p dividing 64, the only rows with a black rightmost cell
  (white beyond it) that recur exactly at light speed with period p are the two phases of black-edged rain.
  Equivalently, the only periodic points of the right-edge map of period dividing 64 are −1/3 and −2/3.
  - The proof is the finite check of §26.1. The start state is asserted to reach both the rain and the defect.
  - Independent control: the state counts plus the two rain states equal the solution counts of L1291's separate
    computation (2,112 at p = 32 to 60 digits; 171,776 at p = 64 to 127 digits).
  - The 104-digit maximum explains L1291's observation that every survivor at digit 127 followed the rain for at
    least 23 digits.
- **P12b HELD:** 104 lies in [85, 120].
- **P12c REFUTED:** the longest path is 1, 2, 4, 5, 15, 104, neither linear nor smooth.
- **Period 128 is out of reach by brute force:** the search passed the 20-million-state cap.

**Two structural facts (COMPUTED for p = 8, 16, 32; exploration, not a recorded test).**
- The graph from the defect is a tree: no state is reached by two paths. That is also why the counts match L1291 one
  for one.
- The tree for p contains the tree for p/2 exactly, as its states of joint period ≤ p/2 (15 = 1 + 2 + 12 for p = 8;
  16 new states of period 16; 1,024 of period 32). The new states hang off the edges where the OR ring has odd weight
  over p/2, so the integral doubles its period.

**Status of the conjecture.** Proved for periods dividing 64; open in general. A uniform proof would show that the
exact-period-p part of the tree is finite for every p, presumably by an induction on p that halves a period-p state.
Routes:
1. Induction on the nesting T_(p/2) ⊂ T_p. Show that a state of exact period p has a successor of exact period 2p or
   none, never one that returns. The tree property suggests the depth recursion is injective on reachable states.
2. A counting identity on the time-depth torus. A cycle would be a doubly periodic pattern, and on it each column is
   black and white equally often at the times its driver fires. Find a contradiction away from the rain.
3. A C bitset search under `run_capped.py` to extend the machine check to p = 128.

## 27. GPT review of the alternative arithmetic and eternal-cycle work (GC2359)

Owner asks to update and review Local L1288–L1292. Taking the finite-graph carrying read and an
independent capped check through p=64 only. The main question is whether a non-alternating
right-edge code can support an infinite spatial continuation at fixed temporal period.
The period128 search is not repeated or enlarged.

Record searched: §§23–26 and the complete `deep_arithmetic.py`, `eternal_cycles.py`,
`eternal_cycles_128.py`, `eternal_proof.py` sources and retained outputs; the current actual kit
`Rule30Equivalents.PeriodicPoints` hypotheses and proof interface, and `Rule30FrozenRuler`.
External refresh completed 2026-11-02T00:46:00Z, kit93d98bbe049177d2c1546b6b0714aa33703ae13d,
15 open PRs. The velocity restriction in `PeriodicPoints` excludes +1 as Local says; its source
SHA256 is dd7e300baf996d52dabe789ce8537f1a5fb03c59504c233f37544bbd17843f57. This is a review of
existing work, not a novelty certificate. The new PR80–82 sources are a separate scoped read.

### Frozen independent finite check

Prediction: literal integration of each temporal ring and Kahn's indegree deletion reproduce
Local's six reachable-state counts2,6,30,62,2110,171774, with no return to rain and no cycle.
Retain a decreasing integer rank for every visited state, rather than just the word `False`.
Counterfactual: any successor mismatch, larger count, cycle, rain return or violated rank stops
the stage and requires revisiting the classification. Controls: every pair of rings at p=2,4,8
against the original packed integration; the rain is a positive cycle control, an odd driver
must fail closure, and an injected self-loop must be rejected. Unexpected structural check:
look for an exact-period-p state with an exact-period-p successor at p<=16, to test the literal
one-step doubling proposal. No automatic width/period increase.

Source `tests/probes/eternal_review.py`, SHA256
`aee252ca970bd6f6734399274ac423b3605a5255fde34f31b4107df17e6ae0f0`.
Local source SHA256 f6b155ecac74545c98400ea5fdbf93f746ecccadd71ba0cb004664835db02302.
One Intel job at nice10, one Python thread, no packages or children. Fixed p=2,4,8,16,32,64,
200000 states per graph;120 aggregate CPU seconds,90s child CPU guard,100s hard per-process
CPU,180s wall,768MiB tree RSS, max2 tracked processes,16MiB/file and128MiB stage disk.
Observed free+inactive6364MiB, load2.19; launch floor4096MiB, running floor3072MiB,
swap-growth stop64MiB. Use run_capped with tree tracking. Per-process limits do not enforce
aggregate CPU; retain child and supervisor receipts. No GPU or thermal measurement. A failed
pressure/monitor/resource stage is retained and not automatically retried.

My own pull: find what information a first defect retains when OR masks one of its inputs.
That may supply a decreasing rank or a rigorous period-halving relation. The observed nesting
alone does not supply that relation; I favour this local information question over period128.

### 27.1 Carrying verdict on the temporal-ring reduction

**L1292 §26.1 carries: PROVED two-party hand.** For a proposed return time p, the temporal
column equation is Delta(w)=u OR v, with Delta(w)(t)=w(t+1) XOR w(t), time modulo p.
Its solutions exist precisely when the driver has even parity, and are the two complementary
running sums. Thus a path from the boundary pair (0,1) constructs a complete space-time diagram
in the moving-edge frame, and conversely an edge code fixed by Phi^p supplies such a path.
This is an equivalence, not only a necessary local test.

For even p the first two generated columns give exactly the two alternating rain states or
the two in-phase defect states. While a path follows rain, its next choice stays in rain or
enters a defect. The two defects differ by a temporal rotation, which commutes with the rule.
Consequently any non-rain infinite path has an infinite tail reachable from a defect. In a
finite directed graph an infinite path exists exactly when a reachable directed cycle exists.
A return to rain supplies such a continuation as well. Checking both no cycle outside rain
and no return to rain is therefore sufficient and necessary for the classification at p.

The power-of-two statement also carries **for least periods**: finite-level cycle lengths
start at2 and can only stay unchanged or double when a bit is lifted. For a periodic infinite
code these lengths divide its least period and eventually stabilize; equality of all finite
prefixes then gives that stabilized value as the least period. A return time need not itself
be a power of two: the genuine two-cycle returns after6 steps too. Statements about background
periods must use the least period in this moving frame, not merely a laboratory-frame temporal
period or an arbitrary return time.

For a nonzero row white to the right of its rightmost black cell e, that edge is at e+p after
p updates. If F^p x=shift^d x in the kit's convention, its right edge is also e-d, forcing d=-p.
Thus right-finite exact recurrence already forces velocity+1 from the edge alone. A general
classification would be up to translation of e, and remains open beyond the checked periods.

### 27.2 Independent finite certificate: PASS through period64

Frozen source9907aa55 COMPLETED. The review uses literal time-by-time integration, checked
against the packed integration on all65808 ring pairs for p=2,4,8 and at every reachable state.
Kahn's indegree deletion replaces Local's depth-first cycle detector. The rain and an injected
self-loop are positive cycle controls; odd-parity drivers are rejected. Every generated edge
strictly decreases a retained integer rank.

| p | reachable defect states | return to rain | cycle | maximum vertices on a defect path |
|---:|---:|---:|---|---:|
| 2 | 2 | 0 | none | 1 |
| 4 | 6 | 0 | none | 2 |
| 8 | 30 | 0 | none | 4 |
| 16 | 62 | 0 | none | 5 |
| 32 | 2110 | 0 | none | 15 |
| 64 | 171774 | 0 | none | 104 |

The last column counts the initial defect vertex. It permits103 additional columns after
that vertex at p=64, or104 columns including the first defective digit. This convention makes
the depth127/divergence23 observation consistent; it should not be described as104 extra
transitions after the defect.

**Certified finite conclusion:** Fix(Phi^64) consists exactly of -1/3 and -2/3, the alternating
two-cycle. Hence there are no other points whose least period divides64. For p=1 the fixed set
is empty; for p=2,4,8,16,32,64 it is that same pair. This is a two-party mathematical reduction
with independently checked exhaustive computation and retained ranks, not Lean formalisation
and not the all-period conjecture. No period128 work was launched.

Intel child receipt:3.93 user +0.07 system CPU seconds,4.02 wall seconds,87,793,664-byte maximum
RSS; supervisor0.182 CPU seconds,4.40 wall seconds. Sampled tree RSS max66024KiB, launch free+
inactive6372MiB, observed minimum6308MiB, observed swap growth0. Stage size7,459,328 bytes;
no resource stop. Per-process caps are not general aggregate enforcement; measured receipts
are below the frozen stage budget. Data, rank files, both sources and raw receipts are in
`cited/gpt/gc2359-eternal-review-20261102.zip`,2,680,573 bytes, SHA256
`484221f10436214c5e94b1f5455ef05fd32ba7fc42ba72f886fbf51f4e7d3fa0`.
Verified raw-body upload and byte-exact TLS readback. The p64 rank file SHA256 is
`eef479565f20886484cf10043248b19d28e6dd08dec649afa6139b556384fb7a`.

**One-step doubling is too strong.** At p=8, time rings encoded with time0 as bit0 give the
reachable path (170,170)->(170,204)->(204,180)->(180,168). Both final states have exact joint
period8, so a state of exact period p need not double or die at the very next column. This
refutes that literal version of §26.3 route1, not an eventual-doubling argument. A useful repair
is a rank *within* each fixed-period stretch, followed by a proof that passing between stretches
cannot return. The retained finite ranks provide examples, not a uniform formula.

### 27.3 Arithmetic review and a stronger repair of the affine claim

L1290's valuation formula is the already carried deep-word law in arithmetic notation: the
number of trailing ones of y is v2(y+1), when y is not -1. For natural deep words this is finite
and floor division is literal integer division. For general2-adic words use digit deletion
(y-(y mod2^L))/2^L, and keep the all-ones infinite-scan case separate.
Phi adds exactly2 to a natural word's bit length, also at0 since Phi(0)=3. At actual collisions
the terminating zero ensures the deletion is within the evolved word, giving the stated exact
length balance. This is a driven return law: r still comes from the shallow side, so it has not
become an autonomous one-integer Collatz map. The four-bit orbit identity is consistent with
the full eight-state orbit modulo16; it is not a higher-precision multiplication law.

The mod8 cycle mismatch excludes affine conjugacy by a **residue-compatible bijection**. Alone
it does not exclude a conjugating bijection that mixes residue levels. There is, however, a
short stronger repair using actual infinite periodic points (**PROOF-SKETCH, GPT; Local read
requested**):

- The alternating pair is a genuine two-cycle of Phi: its saturated driver is all ones, so
  Phi(x)=-1-x on those two words, swapping -1/3 and -2/3.
- Suppose a bijection conjugated Phi to A(y)=a*y+b on Z_2. Its image y of a rain point would
  satisfy A^2(y)=y and A(y) not equal to y. But
  A^2(y)-y=(a+1)*(A(y)-y). The2-adic integers have no zero divisors, so a=-1.
- Then A^2 is the identity everywhere, forcing Phi^2 to be the identity everywhere. This is
  false: Phi^2(0)=12.

Thus the claimed non-affine conclusion has a proof without any continuity or isometry
assumption on the conjugating bijection. The proof uses a genuine infinite two-cycle; finite
level cycles alone would not suffice. In particular L1290's claim that short cycles persisting
through a finite number of levels are already2-adic periodic points must be withdrawn: compatible
lifts at every depth are required, and L1291's disappearing branches demonstrate the problem.
The elementary affine-period argument repairs the conclusion; no novelty is claimed for it.

### 27.4 Centre qualifications: preserve the question rather than equate it to speed

L1288 correctly identifies all unmarked black cells as lying to the right of the ancestry
front. This does not establish its claimed equivalence of capture-time and centre conditions.
T(j)<=j eventually is a sufficient condition for eventual capture of black centre cells, as
GPT proposed; it also constrains that diagonal at *all later* times, hence black cells left of
the centre. Centre capture samples only the point(t,j)=(j,j). An unmarked-free black left half
can coexist at an individual time with B<0 and a white gap from B+1 through0. Therefore neither
the missing converse nor eventual B>=0 follows just by substituting j=t. Eventual nonnegative
position is also weaker than positive linear speed. The stronger proved D(t)->infinity should
not be downgraded to only a limsup when stating what is known.

The retreat thresholds must likewise be separated. Starting from B=b>=0, the next front is
b-L+1, so it falls left of0 iff L>=b+2. Whether a later black centre cell becomes unmarked is
a different question. At the post-retreat row let p=b-L+1<0 and let q be the first black cell
to its right. In the ensuing white-gap episode, the right boundary can reach0 before the
marked front only if q<-p, equivalently L>b+q+1. Since q>=b+2, L>2b+3 is a **necessary** size
condition for this episode to lose a black centre cell. It is not equivalent to the front
never crossing0; and the extra shallow gap can make it insufficient. No probabilistic summation
is justified by the finite fair-coin-like run histogram.

Route around this obstacle: retain the exact pair(p,q), or its sum, when asking about centre
loss, and seek a root-compatible bound on its sign rather than infer one from run frequencies.
The arithmetic/defect route is currently the stronger pull, but the centre direction has not
been logically ruled out by identifying its boundary. This review launches no new centre run.

### 27.5 Fresh external information and next executable step

The00:46:00Z complete index refresh leaves kit main at93d98bbe, with15 open PRs. Newly listed
PR80/81/82 and their portal entries are partial results; none supplies the missing eternal-cycle
classification. Targeted actual-source reads (not full proof audits):

- PR80 head e2aa4179bb58: `tape_eq_init_of_head_ne` and scan-bound hypotheses concern Turing-machine
  tape invariance; source SHA256 c4c50cdf58f3816594deefca2bb49559d28aa5b0eb2508cd492d3cbc0fdd2b00.
- PR81 head069d33b6de89: `energy_forms_of_antiperiodic` assumes eventual antiperiodicity of the
  sequence; it does not prove it for the centre. Source SHA256
  16a44e82bf8a639d2cc97fb8c6227bb763e5cb7b21f4a7a4a38a2884c5bbf25f.
- PR82 head2a110b795e93: `pureScan_two_erase_b1`, prefix autonomy and `front_eq_terminal_FG`
  are for the auxiliary survival frontier. The last retains `Legal`, a successful `run`, and
  a cone-overlap inequality. It is not a theorem of actual-seed ancestry capture or unrestricted
  memory erasure. Source SHA256 dd17a4254a040ca21465da7d2ada5feec5dd2c714bea4b13cc9c86ff1a332bd6.

Next: Local's carrying read of27.3's affine repair; for the all-period conjecture, try to
recover a constrained predecessor from a reachable pair(v,w), knowing Delta(w)=u OR v.
At v=0 the preceding u is revealed; at v=1 it is masked. Determine which boundary-rooted
constraints recover those masked bits, and test the proposed invariant first on the explicit
period8 same-period path. A general uniqueness/rank theorem could explain the observed trees;
finite nesting and a longer period128 census do not yet do so. Independent alternative: the
exact centre-loss pair(p,q), then Mahler's4,11,6 threshold boundary. Schedules remain paused.
My own pull: a rank measuring what the first defect retains through the masked OR positions,
allowing several columns at one period before the next doubling. This is more specific than
assuming a halving map exists because the small trees nest.

## 28. Local's reply to GC2359, and the induction (L1293)

### 28.1 GC2359 received

- **Accepted with thanks:**
  - least periods, not return times;
  - the 104 counts the defect vertex (103 further columns);
  - the literal "double or die at the next column" form of route 1 is refuted by GPT's period-8 plateau path;
  - L1290's sentence that short cycles persisting through finitely many levels are 2-adic periodic points is
    withdrawn (L1291's vanishing branches are the counterexample);
  - the mod-8 cycle type excludes only residue-compatible affine conjugacy;
  - L1288's centre "equivalence" is only the sufficient direction, and L > 2b + 3 is a necessary size condition
    for losing a centre cell in one episode, not a characterization.
- **GPT's stronger affine argument carries (PROVED two-party; Local's read).** The rain is a genuine 2-cycle with
  Φ(x) = −1 − x on it. If a bijection conjugated Φ to A(y) = ay + b, the image y of a rain point would satisfy
  A²(y) = y ≠ A(y). Since A²(y) − y = (a + 1)(A(y) − y) and Z_2 has no zero divisors, a = −1, so A² is the identity,
  so Φ² is. But Φ²(0) = 12 (checked).

### 28.2 The induction: what holds, what fails, and the reduction (Local)

**A rank by fine period fails (COMPUTED, exploration).**
- Let R = GF(2)[z]/((1+z)^p). A time-ring w is an element of R, and its (1+z)-adic valuation v(w) refines its
  period: w has period dividing p/2^i iff v(w) ≥ p − p/2^i. Death is exactly v(OR) = 0, an odd-weight OR.
- For p = 8 and 16, v(OR) ≤ min(v(u), v(v)) on every edge, so the new column's valuation falls by at least one each
  step.
- At p = 32 this fails, with v(OR) − min(v(u), v(v)) up to +6. Columns of valuation 0 occur and the path continues.
  The longest path's column valuations are 30, 29, 27, 24, 23, 15, 6, 2, 0, 0, 0, 0, 0, 1, 3.
- No monotone valuation rank.

**The first doubled column is anti-periodic (PROOF-SKETCH, Local).**
- Let x be eternal with least period p ≥ 4, and let j_0 be the first column of least period p.
- The columns above j_0 have period dividing p/2, so c_(j_0)'s driver does too. Hence c_(j_0)(t + p/2) XOR
  c_(j_0)(t) is a sum over half a driver period, the same for every t. It is 1 because c_(j_0) is not p/2-periodic.
  So **c_(j_0)(t + p/2) = NOT c_(j_0)(t)**.
- The half-differences h_k(t) = c_k(t) XOR c_k(t + p/2) are the damage between x and Φ^(p/2)(x). They vanish
  above j_0, are all ones at j_0 (a black front for the damage), and are p/2-periodic. They obey L1282's exact
  damage law: Δh_(k+1) = h_(k−1)·NOT c_k XOR h_k·NOT c_(k−1) XOR h_(k−1)·h_k.
- First consequence: column j_0 + 1 is p-periodic iff column j_0 − 1 is white an even number of times per
  half-period.
- So T_p is T_(p/2) plus subtrees hung on its odd-half-weight edges. Each subtree starts with an anti-periodic
  column, a damage front. An induction would show those damage subtrees are finite, by a statement general enough to
  cover the damage law as well as Φ. Not done.

**Reduction to a unique-predecessor lemma (PROOF-SKETCH; COMPUTED for p ≤ 64).**
- If every state reachable from the defect has at most one predecessor among reachable states, and the defect state
  has none, then no cycle is reachable. Reason: the first state of a cycle that a path from the defect reaches would
  have one predecessor on the path and another on the cycle.
- So the conjecture at period p follows from **Lemma U(p)** (unique predecessors in the defect's graph) and R(p) (no
  edge into the rain).
- U holds for p ≤ 64: no state of the 171,774 at p = 64 has two predecessors (COMPUTED).
- U is an injectivity statement: the last two columns determine the one before. That holds outside the masked
  positions automatically, and the content is that the masked positions are also fixed among reachable states.
  This is the cleanest target for a proof covering all p.

### 28.3 T13: the machine check at p = 128 (predictions written before the run)

`eternal_dfs.c` enumerates every path from the defect state for a given p ≤ 128, with 128-bit rings and no visited
set, stopping any path deeper than 100,000 columns. Every path finite means no reachable cycle; the program also
counts edges into the rain. It runs under `run_capped.py` with CPU 900 s, wall 1,200 s, RSS 256 MiB, file 16 MiB,
disk 64 MiB, minimum free memory 2,048 MiB and swap growth 128 MiB.
- P13a: for p = 2..64 it reproduces the state counts 2, 6, 30, 62, 2,110 and 171,774 as path counts (consistent with
  the tree property) and the longest paths 1, 2, 4, 5, 15 and 104.
- P13b: at p = 128 every path is finite and none enters the rain, so the conjecture holds for every period dividing
  128. Path count between 10^6 and 10^9; longest path between 104 and 2,000.
- Counterfactual: a path reaching the cap or an edge into the rain, a candidate non-rain eternal point.

### 28.4 Lemma U as a statement about damage fronts (PROOF-SKETCH, Local; written while T13 ran)

- Take two valid prefixes from the front (all columns p-periodic) that first differ at column j. Since they have the
  same driver there and different free bits, c'_j = NOT c_j: the damage h = c XOR c' has a **front** h_j = all ones,
  with no damage above.
- The prefixes reach the same state exactly when h has two consecutive all-zero columns. After that they may
  diverge again through a free bit.
- So **Lemma U ⇔ a damage front, once created between two valid configurations, never has two consecutive zero
  columns below it.** That is the same kind of object as the anti-periodic column of §28.2, a damage front between x
  and Φ^(p/2)(x).
- A single damage-front lemma under L1282's exact damage law, Δh_(k+1) = h_(k−1)·NOT c_k XOR h_k·NOT c_(k−1) XOR
  h_(k−1)·h_k, would close the conjecture for every period.

**A first local step, by hand.** Suppose h_(i−1) = h_i = 0 and h_(i−2)(s) = 1, with c_(i−2)(s) = 1 and
c'_(i−2)(s) = 0.
- Equal i-th columns force equal drivers, so c_(i−1)(s) = 1. The damage is masked there.
- Equal (i−1)-th columns give c'_(i−3)(s) = 1.
- Since c_(i−1)(s+1) = 0, the (i−2)-th columns must agree at s + 1, which forces c_(i−3)(s) = c_(i−4)(s) = 0.
- So the damage at (i−2, s) climbs to (i−3, s), with the local pattern (0, 0, 1, 1) on columns i−4..i−1 in c, and
  (·, 1, 0, 1) on columns i−3..i−1 in c'.
- Climbing all the way to the front would give a contradiction there, because above the front there is no damage.
  The step does not iterate yet: after one climb there are no longer two zero columns below. This is where the next
  block should start.

### 28.5 T13 results (machine-checked; [`eternal_dfs.c`](../tests/probes/eternal_dfs.c), [output](../tests/probes/eternal_dfs.out))

- **P13a HELD.** For p = 2..64 the C enumeration reproduces the state counts 2, 6, 30, 62, 2,110 and 171,774 as path
  counts, and the longest paths 1, 2, 4, 5, 15 and 104. That agrees with Local's Python check (§26) and GPT's
  independent Kahn check (§27.2), and is consistent with the tree property.
- **P13b: the main clause HELD, the longest-path clause REFUTED.**
  - At p = 128 there are 143,381,758 paths from the defect, every one finite (none reached the 100,000-column cap),
    and no edge returns to the rain.
  - The longest path has 2,033 columns, just above the predicted 2,000. The path count is inside the predicted range.
  - **Theorem (machine-checked): for every period dividing 128, the only rows with a black rightmost cell that recur
    exactly at light speed are the two phases of black-edged rain.** Equivalently, Fix(Φ^128) = {−1/3, −2/3}.
- Run under `run_capped.py` (CPU 900 s, wall 1,200 s, RSS 256 MiB, file 16 MiB, disk 64 MiB, minimum free 2,048 MiB,
  swap growth 128 MiB): COMPLETED, 1.31 s user CPU, 1.35 s wall, 1.8 MB maximum RSS. Source SHA256
  `601766bb2c1dcdad9f4fb9b1b30745268d90d3ae9aff00f8a596a6b15a546877`.
- Growth: paths rise by factors of about 81 and 835 for p = 32 → 64 → 128; the longest path from 15 to 104 to
  2,033. Period 256 would need 256-bit rings and, at a similar factor, about 10^11 paths: some tens of minutes in C.
  That is a reasonable capped run if wanted, but no substitute for the damage-front lemma.

## 29. The damage-front lemma, the automaton group, and the defect map (L1294)

Record searched: `record_find` for automaton, Mealy, self-similar, Grigorchuk, Nekrashevych, contracting, Bondarenko,
odometer, T-function, Klimov; the kit's main and portal index through `known_find.py` (last complete refresh in §27.5);
the literature through the automaton atlas of Bondarenko, Grigorchuk, Kravchenko, Muntyan, Nekrashevych, Savchuk and
Šunić (*Classification of groups generated by 3-state automata over a 2-letter alphabet*, Algebra and Discrete
Mathematics 2008; arXiv math/0612178, with part II arXiv 0704.3876), and the T-function papers of Klimov and Shamir.

### 29.1 Prior art: Φ is generator a of automaton 2369 (known; Local's identification)

- L1291's decoder writes Φ as a 3-state invertible Mealy automaton. The state is the previous two input bits:
  **a** flips the bit and was entered after a 1; **b** flips and was entered after 10; **c** copies and was entered
  after 00. With sections indexed by the input letter, **a = σ(b, a), b = σ(c, a), c = (c, a)**, and Φ = a.
- This is automaton **2369** of the atlas (its minimal number over state orderings; the inverse automaton is 2407).
  The atlas entry reads the same recursion, and records: G2369 is not contracting, it is self-replicating, it has
  relations including a⁻¹ba⁻¹b, b⁻¹cb⁻¹c and (a⁻¹c)⁴, and a has infinite order because "the length of the non-zero
  prefix grows by 2 with each application of a".
- That last fact is L1290's "Φ adds exactly 2 to the bit length of a natural number" (§24): **known, reproved here**.
  Credit goes to the atlas, and `PRIOR-ART.md` gets the entry.
- In 2-adic form, with u≪k the shift towards higher bits:
  - a(z) = Φ(z) = z ⊕ ((z≪1) | (z≪2) | 3);
  - b(z) = z ⊕ ((z≪1) | (z≪2) | 1);
  - c(z) = z ⊕ ((z≪1) | (z≪2)), the deep-word map under two white cells, which fixes 0.

### 29.2 The defect map (PROOF, Local; hand)

**Claim.** The light-speed recurrence conjecture (the only periodic points of Φ on Z_2 are −1/3 and −2/3) is
equivalent to: **the 2-adic isometry ψ = Φ ∘ c has no periodic point at all.**

Proof.
- For g acting on binary words and a word v whose g-cycle at its level has length L, g^L maps the cylinder vZ_2 to
  itself as v·h with h = g^L|_v, the return section. A point of vZ_2 has a finite g-orbit iff its tail has a finite
  h-orbit, because the g-orbit is finite iff the g^L-orbit is.
- At level 1, a swaps 0 and 1, so L = 2 with return sections a²|_0 = a∘b and a²|_1 = b∘a (from a(0w) = 1·b(w) and
  a(1w) = 0·a(w)).
- Next, a∘b = (a∘c, b∘a) and b∘a = (a∘b, c∘a). Both copy the first letter, so the return sections one level down are
  their sections.
- So a point stays in the loop a∘b → b∘a → a∘b while its letters alternate, which is exactly the rain. At its first
  non-alternation it leaves to a∘c (from a∘b on reading 0) or to c∘a (from b∘a on reading 1).
- Hence a non-rain point has a finite Φ-orbit iff some tail of it has a finite orbit under a∘c or c∘a. Every z ∈ Z_2
  occurs as such a tail (put a rain prefix and the breaking letter in front of z).
- c∘a = a⁻¹(a∘c)a is conjugate to a∘c, so both have finite orbits or neither does. ∎

**Notes.**
- In Rule 30 terms, ψ is two steps of the deep word with the two driving cells white-white and then black-black. That
  is the defect state (a, a) of §26, the pair-graph root, now as a single map with no rain in it.
- The conjecture becomes a statement about one element of a known self-similar group: **a∘c acts on the binary
  tree's boundary without finite orbits.** A pair-graph node of depth n at period p = 2q is a point z mod 2^n with
  ψ^q(z) ≡ z (mod 2^n), one for each of the two defect phases.

### 29.3 Predictions (written before the runs)

T14, the defect map by cycle lifting. Lift the cycles of ψ level by level (a cycle of length L at level n doubles
or splits according to ψ^L of a representative mod 2^(n+1)), keeping cycles of length dividing q. Let F_q(n) be the
number of points z mod 2^n with ψ^q(z) ≡ z.
- P14a: Σ_n F_q(n) = 1, 3, 15, 31, 1,055 and 85,887 for q = 1, 2, 4, 8, 16 and 32 (half of the state counts 2, 6,
  30, 62, 2,110 and 171,774). The last level with F_q(n) > 0 is 0, 1, 3, 4, 14 and 103 (one less than the longest
  paths).
- P14b: c∘a gives the same numbers.
- Counterfactual: any difference means the reduction of §29.2 or the node–point correspondence is wrong. The
  algorithm differs from the pair graph's (2-adic arithmetic on ψ, not time-rings), so agreement is an independent
  check.

T15, the pair graph at p = 8, 16, 32 and 64 (Python).
- P15a (a sharper Lemma U): among states reachable from the defect, **the second column determines the first**. No two
  reachable states (s, u) ≠ (s', u). A merge needs this (§28.4), so P15a implies U. My lean is that it holds through
  p = 64, from the size of the state space, not from a mechanism.
- P15b (forced child; PROVED by hand, the run guards the code): the two children (v, w) and (v, NOT w) have ORs whose
  weights sum to p + |v|. So if |v| is odd, exactly one child continues. If |v| is even, both continue or neither.
- P15c (critical branching): over the nodes that continue, the mean number of children that continue lies in
  [0.9, 1.1] at p = 32 and 64. That is a critical branching process, which dies out but with heavy tails, matching
  the longest paths 15, 104 and 2,033.
- Counterfactual for P15c: a mean clearly below 1 would mean a subcritical process with a decay we could try to
  prove. A mean above 1 with finite trees would mean a hidden constraint.

T16, the orbit enumeration (predictions written before the program was run). Rotating time by two Φ-steps (one
ψ-step) maps the tree from the defect to itself. So it suffices to walk one node per orbit, carrying the history's
ψ-period H.
- At node (u, v, H), let s be the parity of u | v over one block of 2H times.
  - s = 0: the two children lie in different orbits and keep period H.
  - s = 1 and 2H < p: they are one orbit with period 2H.
  - s = 1 and 2H = p: the node dies.
- The point count is 2 Σ H over orbit nodes; the factor 2 is the two defect phases. This is cycle lifting carried out
  on time-rings, and it saves a factor of about H. The program is `defect_orbits.c`, with multiword rings up to
  p = 512.
- P16a: for p = 2..128 it reproduces `eternal_dfs.out` exactly: paths 2 Σ H = 2, 6, 30, 62, 2,110, 171,774 and
  143,381,758; longest paths 1, 2, 4, 5, 15, 104 and 2,033; no rain edge; no cap hit.
- P16b: at p = 256 every path is finite and none enters the rain, so Fix(Φ^256) = {−1/3, −2/3}.
  - Point count 2 Σ H between 10^10 and 10^14.
  - Longest path between 30,000 and 1,000,000. My central guess is 100,000 to 300,000, from the ratios 6.9 and 19.5
    of the last two steps.
  - The depth cap is 10^7 columns.
- Counterfactual: a cap hit or a rain edge at p = 256 would mark a candidate non-rain periodic point of period 256.
  It would be checked by extracting the path and testing Φ^256 on the 2-adic word it defines.
- The p = 256 run uses `defect_orbits.c` compiled with four-word rings (`-DMW=4`) under `run_capped.py`, with caps
  stated before the run: CPU 3,600 s, wall 4,000 s, RSS 2,048 MiB, file 16 MiB, disk 64 MiB, minimum free memory
  4,096 MiB and swap growth 256 MiB. Expected time: a few minutes, from 27 ns per orbit at p = 128 and an orbit
  growth factor of 400 to 5,000.
- **Change before any result (Local, during the run):** the single-threaded run had printed no progress line
  (one every 2^30 orbits) after 125 s of CPU, so it was slower than 116 ns per orbit, and it was stopped. The branching model below projects about 10^11 orbits.
  The replacement is `defect_orbits_par.c`: the same graph with word-wise integration and work sharing across 8
  threads. It reproduces p = 2..128 exactly, with 1 thread and with 8. Its caps, stated before the run: CPU 43,200 s
  in total, wall 7,200 s, RSS 4,096 MiB, file 16 MiB, disk 64 MiB, minimum free memory 4,096 MiB and swap growth
  256 MiB.

**A branching model, written during the run and before its result (HEURISTIC).** In the orbit tree, a node of period H
splits or doubles; only nodes at H = p/2 die.
- The tree identity forces deaths = splits + 1 per root. Doublings at p equal doublings plus deaths at p/2:
  1,381 = 39 + 1,342 (COMPUTED).
- So the H = p/2 layer of T_p is a forest whose roots are the deaths of T_(p/2). If each period-H node splits or
  doubles with even odds, each tree in the forest is a critical Galton–Watson tree with offspring 0 or 2. Its size
  has a tail like n^(−1/2).
- A sum of N such sizes grows like N², and the tallest tree has height about N. Checks: N = 33 gives a new layer of
  2,651 orbits against N² = 1,089. N = 1,342 gives 1,118,828 against 1.8 million. The longest paths 104 and 2,033 are
  about 3N and 1.5N.
- For p = 256, N = 560,085, so the model predicts on the order of 10^11 orbits (spread between about 3·10^10 and
  10^12 by the heavy tail). Deaths on the order of 10^11, and a longest path on the order of 5·10^5 to 10^6.
- The model also says p = 512 would need about 10^22 orbits. **p = 256 is the last period a machine check can
  reach.** All periods need the lemma.

T17, every cycle of the full pair graph (predictions written before the run). Take all pairs of p-periodic
time-rings, not only those reachable from the edge.
- A cycle of length m is a Rule 30 row on a ring of m cells with R30^p(x) = rotation of x by p: a **light-speed ring
  glider**, seen in the moving frame.
- An infinite path from the defect would have to end in such a cycle. White (0, 0) cannot be reached, since a reached
  column is never constant (§28). So if white and rain were the only cycles, the conjecture at p would reduce to "no
  edge back into the rain", with no reachability argument at all.
- P17a: at p = 8 there are cycles other than white and rain (lean 70%). Rule 30 has many cycles on rings, and the
  light-speed condition at p = 8 is a mild one.
- P17b: none of the other cycles is reachable from the edge state (0, 1). That is the machine theorem again, so this
  part is a consistency check.
- Counterfactual: no other cycles at p = 2, 4 and 8 would make the classification of ring gliders a candidate route
  to the whole conjecture, to be tested next at p = 16 in C.

T18, light-speed ring gliders by ring size (predictions written before the run).
- A cycle of length m in the full pair graph at period p is a periodic orbit, of length dividing p, of the cyclic map
  **c_m(y) = y ⊕ ((y≪1) | (y≪2))** on m-bit rings. That is c of §29.1 with the bits wrapped round: Rule 30 on m cells
  seen in the light-speed frame.
- So the cycles of every pair graph are the cycles of c_m of length 2^j, over all m.
- `ring_cycles.c` finds every cycle of c_m for m = 1..26 and reports those of length 2^j. A configuration that repeats
  a pattern of a smaller ring is a lift, not a new glider, so it reports the **primitive** ones (rotation period m).
- P18a: primitive cycles of length 2^j occur only for m = 1 (white), m = 2 (rain) and m = 4 (the two found by T17).
  Lean 50%; T17 sees only m ≤ 4 at p ≤ 8, but longer periods may bring larger rings.
- P18b: for odd m > 1, no cycle of c_m has length 2^j (lean 60%).
- Counterfactual: primitive 2^j-cycles at many sizes would make a classification of ring gliders look as hard as the
  conjecture. A sparse, structured list would make it a real route around the reachability problem.

T19, the 4-cell glider's own defect trees (predictions written before the run). Each state of the 8-periodic glider
cycle has two children, and one of them leaves the cycle. Follow everything that leaves, at p = 8, 16, 32 and 64.
- P19a: the glider's defect trees are finite at each p, as the rain's are (lean 85%).
- P19b: they never enter the rain, the glider again, or white (lean 85%). A path from the glider into the rain would
  show that the rain can be entered from a region other than white. That matters for part (B) of the route in §29.4.
- Counterfactual: an infinite glider-defect tree would mean a light-speed pattern with the glider above and something
  periodic below, a heteroclinic connection between gliders.

T20, every light-speed pattern of period dividing 16 (predictions written before the run). Trim the full pair graph
at p = 16 (2^32 states) to its **bi-infinite core**: repeatedly remove states with no successor, and states with no
predecessor, inside the remaining set.
- The core is every state on a two-sided path: every cycle, and every wall between two cycles. This is a complete
  classification at p = 16, for every ring size and every wall, with no reachability assumption.
- The program is `lightspeed_core.c`: bitsets laid out by first column, with transposes, so each pass reads one row
  at a time.
- P20a: the cyclic components are exactly white, the rain and the glider's two components. There is no glider on a
  ring of more than 28 cells (lean 75%).
- P20b: the core is those cycles plus two walls. One is the black edge white | rain: the states (0, 1), (1, a) and
  (1, NOT a). The other is the glider | rain junction of T19 (lean 65%).
- Counterfactual: any other cyclic component is a new light-speed glider. Any other core state is a new wall, and
  whether it can be reached from white would then be the question.
- Cross-check before the p = 16 run: compiled with p = 8, the program's core equals an independent Python fixed-point
  computation, 46 states. That is 11 cycle states (white 1, rain 2, glider 8), the 3 black-edge states and 32
  junction states (8 phases × 4), so the p = 8 analogue of P20a and P20b holds exactly.
- The p = 16 run's caps, stated before the run: CPU 3,600 s, wall 4,000 s, RSS 2,048 MiB (three 512 MiB bitsets),
  file 16 MiB, disk 64 MiB, minimum free memory 4,096 MiB and swap growth 256 MiB.

### 29.4 Results of T14, T15, T17, T18 and T19

**T14** ([`defect_map.py`](../tests/probes/defect_map.py), [output](../tests/probes/defect_map.out)).
- **P14a HELD exactly.** Σ_n F_q(n) = 1, 3, 15, 31, 1,055 and 85,887. The last levels with F_q(n) > 0 are 0, 1, 3, 4,
  14 and 103.
- **P14b HELD.** c∘a gives identical numbers.
- So the reduction of §29.2 and the correspondence between nodes and points mod 2^n are confirmed by a second
  algorithm: 2-adic arithmetic on ψ instead of time-rings.

**T15** ([`defect_tree.py`](../tests/probes/defect_tree.py), [output](../tests/probes/defect_tree.out)).
- **P15a HELD.** At p = 8, 16, 32 and 64, no reachable second column occurs with two different first columns.
  - The parent of a reachable state is reachable, so by induction **each reachable column determines its whole
    history back to the defect** (COMPUTED, p ≤ 64).
  - This Lemma U′ is stronger than Lemma U.
- **P15b HELD**, with no violations. Odd-weight columns occur at 416 nodes at p = 32 and 41,280 at p = 64, and at
  none for p = 8 or 16, where every column has period below p and so even weight.
- **P15c: no evidence either way, because the test was vacuous.**
  - The measured means are 0.857, 0.933, 0.998 and 1.000.
  - In any finite tree with two roots, leaves = binary nodes + 2. Together with the forced-child rule, that makes the
    mean exactly 1 − 2/N whatever the dynamics.
  - The counterfactual was badly designed: it could not have failed. Recorded as a failed test design.

**T17** ([`ring_gliders.py`](../tests/probes/ring_gliders.py), [output](../tests/probes/ring_gliders.out)).
- **P17a HELD, narrowly.** At p = 2 and 4 the only cyclic components are white and the rain. At p = 8 there are
  exactly two more, of 4 states each.
- **P17b HELD.** Neither is reachable from the edge.

**T18** ([`ring_cycles.c`](../tests/probes/ring_cycles.c), [output](../tests/probes/ring_cycles.out), m = 1..28).
- **P18a HELD.** The only primitive cycles of c_m whose length is a power of two are:
  - white (m = 1);
  - the rain (m = 2, length 2);
  - **one cycle of length 8 on 4 cells**, the orbit of a single black cell. c_4²(1000) = 0001 is a rotation by one
    cell, so c_4^8 is the identity on it.
- Call the last one **G8**, the 4-cell light-speed glider. It is Rule 30 on a 4-cell ring started from one black
  cell, and it accounts for T17's two extra components (two time phases).
- Every other cycle length is not a power of two: for example m = 20 has 49 cycles, and only 3 of them (all lifts)
  have power-of-two length.
- **P18b** held for primitive cycles. As written it is refuted by the white fixed point, which exists for every m; the
  statement should have excluded lifts of white.

**T19** ([`glider_defect.py`](../tests/probes/glider_defect.py), [output](../tests/probes/glider_defect.out)).
- **P19a HELD.** G8's defect trees are finite: 118, 1,894, 39,718 and 8,743,590 states at p = 8, 16, 32 and 64,
  with longest paths 8, 17, 47 and 455.
- **P19b REFUTED.** At every p tested, 8 edges lead from G8's defect trees into the rain. None leads into G8 or white.
- At p = 8 these are 8 paths of 6 states, one per time phase. So there is a **single wall G8 | rain up to time
  shift**. Depth runs down the page, time across (# black):

  ```
  depth 0  ##.#.#..   G8
  depth 1  .#.#..##   G8
  depth 2  #.##..#.   G8
  depth 3  .#.#...#   wall
  depth 4  #.#.###.   wall
  depth 5  .#.#.#.#   rain
  depth 6  #.#.#.#.   rain
  ```

- So the rain can be entered from a region that is not white. A proof that the defect never returns to the rain must
  use the defect's history, not a local fact about the rain.

### 29.5 The damage-front lemma: where it stands (Local)

**What is proved and what is computed.**
- The reduction to ψ (§29.2) is PROVED, pending GPT's read.
- Lemma U′ holds through p = 64 (COMPUTED). The tree property holds through p = 128, from the path counts. Neither
  has a hand proof.

**Why the local climb of §28.4 does not close.**
- A reachable column fixes its predecessor wherever its driver is white. Under its black cells the predecessor is
  masked, and the masked bits are recoverable only through the whole history.
- In a random model, N reachable states among 2^p columns collide with probability about N²/2^p. Here log₂ N is
  11.0, 17.4 and 27.1 at p = 32, 64 and 128, about 0.2p. So the random model predicts U′ at every large p with no
  mechanism behind it.
- Likewise, the branching model of §29.3 says the conjecture is that a critical process dies out. That is true almost
  surely in the model, and gives no proof.
- **This is the Collatz shape: true in the random model, mechanism unknown.** I said so as a finding, not as a reason
  to stop.

**Routes around.**
1. **The light-speed phase diagram** (§29.6). Classify the two-sided objects, gliders and walls, instead of the
   trees. The objects are rigid and so far tiny.
2. **The group.** The conjecture is equivalent to a continuous h: Z_2 → Z_2 with h(ψz) = h(z) + 1, a factor of ψ onto
   the odometer. Since ψ = a²xy with x = (y, 1), y = σ(xy, yx) of order 2, and a = σ(ax, a) (from the atlas
   relations; Local's computation), a cocycle built from the dihedral part ⟨x, y⟩ is the natural first try.
3. **Lean.** Formalise §29.2 and the finite check. The theorem for every period dividing 128 (or 256) is
   kernel-checkable only through a certificate, which suits GPT's Kahn-style audit.

### 29.6 The light-speed phase diagram (COMPUTED; CONJECTURE)

**What it contains.**
- A two-sided light-speed pattern of period p is a bi-infinite path in the pair graph. Both its ends lie in cycles.
- So it is a stack of **phases** (cycles) separated by **walls** (paths between cycles).
- Found so far:
  - phases: white, the rain and G8;
  - walls: white | rain (the black edge: states (0, 1), (1, a), (1, NOT a)) and G8 | rain (T19).
- At p = 8 the whole bi-infinite core is exactly these. T20's cross-check found 46 states: 11 in phases, 3 in the
  edge and 32 in the junction.

**Conjecture (Phase).** For every p = 2^j, the bi-infinite core of the pair graph is white, the rain, G8, the black
edge and the G8 | rain wall, with their time shifts.

**Phase implies the light-speed recurrence conjecture.**
- A non-rain periodic point is a bi-infinite path that starts in white beyond the edge and passes through the defect.
- Phase allows only one wall leaving white: the black edge, straight into the rain.

**Why it is a better target than the trees.**
- It has no boundary condition. It speaks about all two-sided patterns, closer to classical cellular-automaton
  questions such as Jen's adjacent periodic columns and Rule 30's cycles on rings.
- It splits into two parts:
  - (A) there are no other gliders: Rule 30 on rings, with periods a power of two;
  - (B′) there are no other walls.
- The random model still predicts only finitely many exceptions. But the objects are rigid, and every exception so
  far has at most 4 cells and period at most 8.
- An induction Phase(p) ⇒ Phase(2p) would take a new core state of least period 2p and its half-difference
  h = y ⊕ C^p(y), which is p-periodic and nonzero, and show that the walls force h onto a known core pattern. Not
  done.

### 29.7 T20 results: the complete light-speed core at period 16 ([`lightspeed_core.c`](../tests/probes/lightspeed_core.c), [core](../tests/probes/lightspeed_core16.out), [analysis](../tests/probes/lightspeed_core16_analysis.out))

The run: 31 trimming rounds, from 2,147,516,416 states with an even OR down to a core of **318 states**. Under
`run_capped.py` with the stated caps it COMPLETED in 77.7 s wall and 75.4 s CPU, with 1.61 GB maximum RSS.

**P20a REFUTED.** There are five cyclic components: white, the rain, G8's two, and **a new glider G16**.
- G16 is a single cycle of 128 states, all of least period 16.
- On a ring it is a primitive pattern of **128 cells**: c_128 has least period 16 on it and its rotation period is
  128 (confirmed directly on the ring).
- It is a **rigid rotator**. One step of c_128 rotates the ring by 56 cells, and 16 · 56 = 7 · 128.
- It lies outside T18's census (m ≤ 28), which is why T18 did not see it.
- Ring at time 0 (# black, 65 of 128 cells):
  `###..#.#.#####....#...##.##.######..#.###.#.##.##..##.##...####.#.....##..###.#.#..#......####...#.#..#..###.#..##.#...#.##...#.`

**P20b REFUTED, with a sharper pattern in its place.** The 179 acyclic core states form exactly four walls, and
**every wall ends in the rain**:
- white → rain, the black edge (3 states);
- G8 → rain, two phases (16 + 16 states);
- G16 → rain (144 states).

No wall leads into white, G8 or G16, and none leaves the rain.

**Consequences.**
- **COMPUTED, complete for p | 16, every ring size and every wall:** the only two-sided light-speed patterns of period
  dividing 16 are white, the rain, G8, G16, and the four walls into the rain. In particular, white's only wall is the
  black edge, so the conjecture at p | 16 is confirmed by a method with no reachability assumption at all.
- Phase (§29.6) is refuted as stated. More gliders appear as the period grows: G8 on 4 cells at period 8, G16 on 128
  cells at period 16.

**Revised conjecture (Sink).** For every p = 2^j:
- every wall in the light-speed core ends in the rain;
- the only wall leaving white is the black edge.

The second clause is the light-speed recurrence conjecture itself. The first is new structure: **the rain absorbs
every other light-speed phase.** In absolute coordinates, rain lies deeper (to the left), and each wall moves right at
light speed, so the rain invades white, G8 and G16 at the speed of light.

**A family to look for.** A rigid rotator by r on m cells is a periodic orbit of the feedback shift register
y_n = y_(n−r) ⊕ (y_(n−r−1) ∨ y_(n−r−2)) of order r + 2. It recurs at light speed with a power-of-two period exactly
when m / gcd(m, r) is a power of two.
- The rain is r = 1, m = 2. G16 is r = 56, m = 128.
- G8 is not rigid: c_4 rotates only after two steps, c_4² = rotation by one cell.
- So the gliders may be classifiable through shift registers. That is a concrete next step towards (A).
- Checked directly on the ring: c_128(y)_k = y_(k+56) for G16, and the shift-register recurrence holds at every cell.

### 29.8 The rain is terminal (PROOF, Local; hand)

**Claim.** The light-speed recurrence conjecture at period p is equivalent to: **no wall of the light-speed core leaves
the rain**. That is, no two-sided pattern of period p has rain above (shallower than) anything other than rain.

Proof.
- The successors of the rain state (NOT a, a) are (a, w) with w an integral of NOT a ∨ a = all ones, so w ∈ {a,
  NOT a}. They are the rain state (a, NOT a) and the defect (a, a). Symmetrically, (a, NOT a) leads to the rain or to
  (NOT a, NOT a).
- So every path that leaves the rain passes through a defect state. Conversely, a defect state is a successor of a
  rain state.
- Hence an infinite path from the defect exists iff a wall leaves the rain. The black edge reaches the defect from
  white via (0, 1) → (1, a) → (a, a), so a non-rain periodic point behind a black edge exists iff a wall leaves the
  rain. ∎

**What T20 adds.** At p = 16 the core is a **star**: four walls, all into the rain, none out. The conjecture is the
"none out" half. The "all into" half is the new observation, the rain absorbing every other light-speed phase. A
mechanism for either half would probably explain the other: some order on phases in which walls only go up, with the
rain at the top.

### 29.9 T21: an order on phases? (predictions written before the run)

The rain is the unique light-speed phase in which every cell flips at every step.
- In a two-sided pattern, let Z(u, v) = |NOT u ∧ NOT v| be the number of times in a period that both columns of a
  state are white. That is the number of steps on which the next column does not flip.
- If Z = 0 at every depth, every column alternates and consecutive columns differ, which is the rain.
- So if Z never increased with depth along walls, no wall could leave the rain. That is the conjecture (§29.8).
- L1293's search found the OR weight is not monotone along defect-tree edges. Those paths die, though; walls are
  two-sided, and they may behave differently.

Predictions:
- P21a: along every wall of the p = 8 and p = 16 cores, Z is non-increasing from shallow to deep (lean 45%).
- P21b: the phase values order as W = p > G8 > 0 = R and G16 > 0, with G8 and G16 strictly between.
- Counterfactual: a wall on which Z rises somewhere refutes this order. The next candidates would be quantities
  averaged over several columns, or the number of flips of a column (its driver's weight) rather than of a pair.

**T21 results** ([`lightspeed_order.py`](../tests/probes/lightspeed_order.py), [output](../tests/probes/lightspeed_order.out)).
- **P21a REFUTED.**
  - At p = 8, Z is non-increasing on all 10 wall paths.
  - At p = 16, 16 of the 26 wall paths, all leaving G16, have Z rising before it falls to 0. One path reads
    4, 4, 8, 6, 8, 8, 6, 6, 0, 0, 0.
- **P21b holds only on average.**
  - W = p, G8 = p/4 at both periods, R = 0.
  - G16 is not constant along its own cycle: Z takes the values 2, 4 and 6.
- So a per-state white-pair count is no order. If an order exists, it must be averaged over a phase's cycle, or be a
  different quantity.
- This is the first refuted candidate for the star's order. A second refuted candidate of the same kind (per-state
  weights) should end that kind of search, by the two-blocks rule.

### 29.10 T22: rigid rotators from shift registers (predictions written before the run)

`rotators.c` finds every cycle of the shift register y_n = y_(n−r) ⊕ (y_(n−r−1) ∨ y_(n−r−2)) for r = 1..22 (state:
the last r + 2 bits). Each cycle of period m is a rigid rotator on m cells: one step of c_m rotates it by r. It is a
light-speed glider of power-of-two period L = m / gcd(m, r) exactly when L is a power of two.
- P22a: besides the rain (r = 1, m = 2), at least one such glider exists for some r ≤ 22 (lean 60%). T20 is complete
  for periods dividing 16, so any glider found has L ≥ 32.
- P22b: G16 (m = 128, r = 56) does not appear, since 56 > 22. A glider with L ≤ 16 appearing would contradict T20 and
  so would point to a bug.
- What it teaches: whether new gliders keep appearing as the period grows (a rich phase diagram), or stop.

**T22 results** ([`rotators.c`](../tests/probes/rotators.c), [output](../tests/probes/rotators.out)). The run took
0.1 s for r = 1..22.
- **P22a REFUTED.** For every r ≤ 22, the only light-speed rigid rotators are white (m = 1, every r) and the rain
  (m = 2, odd r).
- The registers have 2 to 11 cycles each. Every other cycle has a period L = m / gcd(m, r) that is not a power of two.
- **P22b HELD.** Nothing with L ≤ 16 appears beyond white and the rain, consistent with T20. G16 (r = 56) lies outside
  the range searched.
- So rigid gliders are rare: none with a small rotation, and the one found by T20 rotates by 56 of 128 cells. Whether
  more gliders appear at periods 32 and above is open. A census of the period-32 core is out of reach (2^64 states),
  but the gliders on rings up to 28 cells (T18) and the rotators with r ≤ 22 (T22) are complete.

### 29.11 T23: G16's defect trees at p = 32 (predictions written before the run)

`glider16_defect.py` rebuilds G16's 128 states from its ring (§29.7), lifts them to p = 32, and follows every child
that leaves the cycle, as T19 did for G8.
- P23a: the trees are finite.
- P23b: their only exits into cycles are into the rain, the first clause of the Sink conjecture at p = 32 for G16
  (lean 75%).
- Counterfactual: an exit into G8, G16 or white, or an infinite tree, would be a new kind of wall.

**T23 results** ([`glider16_defect.py`](../tests/probes/glider16_defect.py), [output](../tests/probes/glider16_defect.out)).
- **P23a HELD.** The trees are finite: 1,310 states (longest 14) at p = 16, and 18,238 states (longest 41) at p = 32.
- **P23b HELD.** At both periods the only exits are 16 edges into the rain. None goes into G16, G8 or white.
- With T19 (G8 at p = 8..64), every glider tested sends walls only into the rain, at every period tested.

### 29.12 T24: the period-256 run stopped at its cap; the new layer root by root (predictions written before the run)

**The p = 256 run of §29.3 is INCOMPLETE.** `defect_orbits_par.c` ran on 8 threads until the 7,200 s wall cap
(exit `WALL_STOP`, maximum RSS 207 MB). It printed nothing, because it reports only at the end. So P16b is
untested, and the stopped run gives no count. That was a design fault: a long enumeration must leave a resumable
partial result.

The repair uses the layer structure of §29.3. T_256 is the copy of T_128 (nodes with H < 128; the 560,085 deaths of
T_128 become doublings), plus one subtree for each of those doublings. Every node of a subtree has H = 128, so it
splits if d = u | v has even weight over the whole ring and dies if the weight is odd. The subtrees are independent.
[`defect_layer.c`](../tests/probes/defect_layer.c) enumerates the copy, numbers the roots in DFS order, then runs each
root's subtree to completion or to a per-root node cap, on 8 threads. It can resume on a list of root numbers.

A two-type fact, found while writing the program (PROOF, Local; hand). In the H = p/2 layer, the children of a
splitting node (u, v) are (v, w) and (v, w̄), where w̄ is the complement on the ring. Then
|v ∨ w| + |v ∨ w̄| = |v| + p, so their parities satisfy s₀ + s₁ ≡ |v| (mod 2), since p is even. Also |w| + |w̄| = p, so
the two children have the same type |w| mod 2. A node whose v has odd weight therefore has exactly one splitting
child. When v has even weight, the two children both split or both die. So the layer is a two-type branching process,
not the independent 0-or-2 process of §29.3's model.

Record searched: `record_find.py Galton "subtree size" "new layer"` found no hit in the record, the kit (main
@93d98bbe), the portal or the open kit PRs. §29.3 holds the model.

Predictions:
- P24a: phase 1 at p = 256 finds 1,121,550 copy nodes and 560,085 roots. At p = 64 and p = 128 the same program
  reproduces the new layers 2,651 (33 roots) and 1,118,828 (1,342 roots) exactly.
- P24b: no split node violates s₀ + s₁ ≡ |v| (mod 2). This only checks the program; the fact is proved above.
- P24c: subtree sizes have a tail P(N ≥ n) ≈ C·n^(−1/2) for n from 10 to 10^6, with C between 0.4 and 1.6. The
  0-or-2 model gives C = √(2/π) ≈ 0.80.
- P24d: with a per-root cap of 10^8 nodes, about 45 roots hit the cap (range 15 to 120).
- P24e: no completed subtree enters the rain or reaches the depth cap of 10^7.
- P24f: the completed subtrees hold about 9·10^9 nodes in total (range 3·10^9 to 3·10^10).
- Counterfactuals. A steep tail with almost no capped roots would leave the stopped run unexplained, unless
  throughput is far below what is measured. Many more than 120 capped roots, or a tail flatter than n^(−1/2), would
  point to supercritical growth, and so to a candidate infinite path: the thing the conjecture forbids.
- The run reports nodes per second per thread. That turns the stopped run into an estimated lower bound on |T_256|.
  This is a MEASURED inference, not a count.
- Caps, stated before the run: CPU 3,600 s, wall 900 s, RSS 2,048 MiB, file 64 MiB, disk 64 MiB, minimum free memory
  4,096 MiB, swap growth 256 MiB. A second stage on the capped roots gets its own caps, written before it starts.

**T24 results** ([`defect_layer.c`](../tests/probes/defect_layer.c), source SHA256 at this commit in
`tests/probes/PROBES.md`; outputs [p ≤ 128](../tests/probes/defect_layer_small.out) and
[p = 256, stopped](../tests/probes/defect_layer256a.out)).

**Why both p = 256 runs stopped: the machine was asleep (MEASURED, from the system power log).**
- The laptop's lid was closed at 02:43:13 UTC ("Clamshell Sleep"). After that it ran only in dark-wake windows of a few
  seconds to a minute.
- The 2-hour run (01:25 to 03:25 UTC) therefore computed for about 78 minutes, not 120.
- The layer run started at 06:30:26 during such a window. 23 s later the system slept with reason
  **"Dark Wake Thermal Emergency"**: eight busy threads in a closed laptop overheated it. The run's own samples stop at
  24 s and resume at 944 s.
- Lesson, recorded: a heavy run needs the lid open and the machine awake. Check `AppleClamshellState` (ioreg) before
  launching. The layer program now measures throughput on `CLOCK_UPTIME_RAW`, which stops during sleep.

**Results.**
- **P24a HELD.**
  - At p = 256, phase 1 finds the copy of T_128: 1,121,550 nodes, 560,084 splits, 561,466 = 1,381 + 560,085
    doublings, no death, no rain edge, longest 2,033, and **560,085 roots**.
  - At p = 8..128 the program reproduces T_p exactly: 5, 7, 71, 2,722 and 1,121,550 orbits, longest 4, 5, 15, 104 and
    2,033. The layers are 2,651 nodes on 33 roots and 1,118,828 nodes on 1,342 roots.
- **P24b HELD for p ≤ 128.** No split node anywhere violates s₀ + s₁ ≡ |v|. A 3-second test at p = 256 (12,288
  completed roots) found none either.
- **P24c.**
  - At p = 128, C_k = (share of roots with N ≥ 2^k)·2^(k/2) lies between 0.48 and 0.98 for k = 2..14 (1,342 roots).
    That fits the 0-or-2 model's 0.80.
  - The two-type process with independent fair-coin types predicts the same constant. Its splitting nodes have 0, 1 or
    2 splitting children with probabilities 1/4, 1/2 and 1/4, which is exactly the law of the 0-or-2 model, so C is
    again 0.80. The data cannot tell the two models apart.
    - A first draft of this section claimed C ≈ 1.6 for the two-type model. That draft forgot the factor 1/2 for the
      root splitting. It was corrected before commit and is recorded here as a failed derivation.
  - At p = 256 only the cap point is measured: 43 roots over 10^8 among about 443,500 dispatched, so C(10^8) ≈ 0.97.
- **P24d HELD on the part run.** 43 capped roots among about 79% of the roots projects to about 54, inside 15 to 120.
  The capped roots are listed in the output, and each certainly has more than 10^8 nodes (COMPUTED).
- **P24e and P24f untested here; both HELD in the rerun of §29.13.** The summary was lost at the stop. The program now catches run_capped's SIGTERM, prints
  the summary for completed roots and names the roots to resume. Tested by a stop after 3 s.
- Throughput: 6.0·10^7 nodes per awake second on one thread, and at least 3.7·10^7 per thread on eight.

**What follows (COMPUTED lower bound; the rest INFERENCE).**
- |T_256| > 4.3·10^9, from the 43 capped roots alone.
- The 2-hour program ran about 78 awake minutes on 8 threads without finishing. At comparable throughput it walked
  on the order of 10^12 nodes, so |T_256| is probably above 10^12. That is the top of the branching model's range
  (3·10^10 to 10^12).
- Under the model's n^(−1/2) tail, the about 54 roots above 10^8 hold almost all of T_256. The largest is likely
  10^11 to 10^13 nodes, which is one to ten hours of 8-thread work with the lid open.
- One giant root cannot be parallelised by the root queue. Stage 2 must split a capped root at a fixed depth into its
  frontier nodes and queue those.

**Routes (each lands work, not a pause).**
1. **Finish p = 256 when the machine can run awake.**
   - First, all roots at cap 10^8 (about 40 awake seconds), for P24b, P24e and P24f.
   - Then the capped roots, split at depth, at caps 10^10 and 10^12. Each stage is resumable from the printed root
     list.
2. **The two-type process.** In the H = p/2 layer a node of odd |v| has exactly one splitting child. Criticality then
   rests on the even-|v| nodes alone: both children split or both die, at even odds.
   - Measure the type frequencies and the both-split share at p = 64 and 128; this is cheap.
   - Look for an involution on the even-|v| nodes that swaps "both split" with "both die". Such an involution would
     prove criticality, which is the model's one assumption.
3. **Lean.** The layer decomposition and the two-type fact are short and exact, so they are good first targets in
   the formalisation route of §29.5.

### 29.13 T25: every root at cap 10^8, then the 54 giants to completion (L1297; predictions written before the giant run)

With the lid open, all 560,085 roots of §29.12 were rerun at a per-root cap of 10^8, on 8 threads under
`run_capped.py` with the caps stated in §29.12. The run COMPLETED in 30.2 s wall (223 s CPU, 86 MB maximum RSS).
Output: [`defect_layer256b.out`](../tests/probes/defect_layer256b.out). The capped roots are listed in
[`defect_layer256_giants.txt`](../tests/probes/defect_layer256_giants.txt).

**Results for the predictions of §29.12 (COMPUTED).**
- 560,031 roots completed and 54 hit the cap.
- **P24b HELD**: no split node violates the two-type identity.
- **P24d HELD**: 54 capped roots, inside the predicted 15 to 120.
- **P24e HELD**: no completed subtree enters the rain or reaches the depth cap. The deepest completed node is at
  absolute depth 38,077.
- **P24f HELD**: the completed subtrees hold 4,565,012,021 nodes (2,282,786,026 deaths and 2,282,225,995 splits), inside
  3·10^9 to 3·10^10. Deaths minus splits is 560,031, one per completed root, as the tree identity requires.
- **P24c HELD, and sharply.** C_k (the share of roots with N ≥ 2^k, times 2^(k/2)) is 0.796, 0.803, 0.806, 0.810,
  0.807, 0.809, 0.809, 0.815 and 0.817 for k = 7..15. It then drifts between 0.80 and 0.88 for k = 16..25, where 85
  to 1,838 roots remain. The 0-or-2 critical model predicts √(2/π) = 0.798.
  - So over 18 binary orders of magnitude the subtree sizes follow the critical Galton–Watson law, including its
    constant. The process is critical, not just near it.

**T25: the giants.** [`defect_giants.c`](../tests/probes/defect_giants.c) runs the subtrees of a list of roots, sharing
work across threads. At the end of a chunk it writes every pending node, with the running totals, to a checkpoint,
and the next chunk resumes from there.
- Validation (COMPUTED):
  - The 1,342 roots of T_128's layer, run whole and run in eight chunks of about 10^5 nodes, give 1,118,828 nodes,
    560,085 deaths, 558,743 splits and longest path 2,033, exactly.
  - Three p = 256 roots, run in four chunks, give 45,243,961, 16,032,647 and 10,309,883 nodes and depth 16,418, as
    the per-root run does.

Predictions, written before the giant run. They use the measured tail: about 4.54·10^5·n^(−1/2) roots with at least
n nodes.
- **P25a (= P16b):** all 54 giant subtrees are finite, and none enters the rain. Then T_256 is finite with no rain
  edge, so Fix(Φ^256) = {−1/3, −2/3}, and the light-speed recurrence conjecture is machine-checked for every period
  dividing 256 (lean 95%).
- **P25b:** the largest giant has between 4·10^10 and 2·10^13 nodes. That is the 80% range of the maximum under the
  tail law, with median 4·10^11.
  - The giants together hold 1.5 to 3 times the largest.
  - My central guess is 3·10^12. The stopped 2-hour run (§29.12) suggests at least 10^12.
- **P25c:** the longest path is about 3.5·√(largest giant), within a factor of 2. The ratio is 2.9 at p = 128 and
  about 3.8 among the completed p = 256 roots.
- **P25d:** no two-type violation.
- Counterfactual: a rain edge, or a giant that grows without end (more than about 10^14 nodes, or a path deeper than
  10^8), would be a candidate non-rain periodic point of period 256. Its path would be extracted and Φ^256 tested on
  the 2-adic word it defines.
- **Caps per chunk, stated before the run:**
  - Budget: 10^12 nodes per chunk, about 50 minutes at the measured 3.3·10^8 nodes per second.
  - `run_capped.py`: CPU 32,000 s, wall 4,000 s, RSS 4,096 MiB, file 2,048 MiB (the checkpoint), disk 64 MiB,
    minimum free memory 4,096 MiB, swap growth 256 MiB.
  - Run under `caffeinate -i`. The lid state and the thermal log are checked between chunks.
  - At most 12 chunks (about 10 hours) without a new word from the owner.

**Chunks 1–3 and a memory stop (COMPUTED and MEASURED; 2 November, 08:14 to 10:35 GMT).**
- Chunks 1 and 2 each ran their full 10^12-node budget, in 3,624 and 3,689 awake seconds: 3.4·10^7 nodes per
  second per thread on 8 threads. No thermal or performance warning was logged.
- Chunk 3 ended after 1,135 s with PRESSURE_STOP: free plus inactive memory fell to 3,791 MiB, below the 4,096 MiB
  guard. The run itself held 0.37 GiB and swap did not grow; other programs had taken the memory. The stop signal made
  the program write its checkpoint, so nothing was lost. Chunk 4 was refused at launch (4,056 MiB free), and the
  driver stopped. The owner then closed some programs, freeing about 6 GiB.
- After three chunks: 2,307,930,832,706 nodes, no rain edge, no two-type violation, longest path 2,510,076.
- **51 of the 54 giants are complete**: 172,941,578,899 nodes, and deaths minus splits is 1 for each, as a finite
  binary tree requires. The largest is root 105847, with 107,710,643,975 nodes and longest path 693,230. Across the
  51, longest path / √nodes runs from 1.41 to 3.75 (median 2.39).
- Three are open:
  - root 130746: 1.21·10^12 nodes so far, 1,254,320 pending;
  - root 102229: 6.50·10^11 nodes, 737,457 pending;
  - root 76216: 2.72·10^11 nodes, 1,057,459 pending.
- P25b so far: the largest giant already exceeds 1.2·10^12, still inside the predicted range. **My central guess of
  3·10^12 for all the giants failed.** Meeting it would need the 3.05·10^6 pending nodes to finish within 7·10^11
  more nodes, which has probability 3·10^−4 under the law in P25e below.

**State repeats (COMPUTED, p ≤ 128).** A layer node's subtree depends only on (v, u ∨ v). The layer is also
equivariant under rotation of the ring: the split test is rotation-invariant, and rotating d rotates the pair
{w, w̄}. If states recurred, memoising subtrees would shorten the run. They do not recur. At p = 16, 32, 64 and 128,
every layer node has a different v, even up to rotation: 1,118,828 nodes at p = 128.
[`defect_repeats.py`](../tests/probes/defect_repeats.py), output
[`defect_repeats.out`](../tests/probes/defect_repeats.out), 20 s on one core. Memoising cannot help, so the run
continues as it is.

**P25e, written before the run resumes: the remaining work.** In a depth-first search, the pending nodes are the
roots of the unexplored subtrees. So the remaining work R is the size of a forest of k = 3,049,236 critical trees.
Take offspring 0 or 2, each with probability ½ (effective variance 1, which the tail constant 0.80 above confirms).
Then R is the first time a fair ±1 walk started at k reaches 0, and P(R ≤ t) = erfc(k/√(2t)).
- The median is 2.0·10^13 nodes, about 20 hours at 10^12 nodes per hour.
- P(R ≤ 9·10^12, the nine chunks left) = 0.31. P(R ≤ 2.4·10^13, about a day) = 0.53. P(R > 10^14) = 0.24.
- The pending counts already move like this walk. Root 130746 went from 1,336,130 to 1,698,155 to 1,254,320 pending
  over 6.6·10^11 and then 1.8·10^11 nodes, steps of about one walk standard deviation (8.1·10^5 and 4.2·10^5).
- Counterfactual: if these subtrees were subcritical, the run would end much sooner. Finishing within 10^12 more
  nodes has probability 0.002 under the walk law, so that would count against the critical model in this range.
  Growth without end is P25a's counterfactual.

**Resumption caps, stated before chunk 4.** The caps are as above, including the 4,096 MiB free-memory guard. The
driver now handles the guard differently:
- A refused launch waits 120 s and retries, at most 30 times.
- A pressure stop, which still writes its checkpoint, waits 120 s before the next chunk.
- Chunks 4 to 12 resume from checkpoint 3, so the limit of 12 chunks stands. Going beyond it needs the owner's word.

**Chunk 4 and the pause (COMPUTED; 2 November, 10:41 to 10:56 GMT).** At the owner's request the run was paused. The
owner wants the M5 free for general use: next comes the proof route, and the Intel host takes the run if a proof is
still lacking.
- The driver was stopped, then the program was sent SIGTERM. Chunk 4 had run 913 s (2.50·10^11 nodes); it wrote
  checkpoint 4 and exited.
- Totals: 2,558,276,805,828 nodes, no rain edge, no two-type violation, longest path 2,622,213. 51 giants are
  complete.
- The three open giants hold 3,261,652 pending nodes:
  - root 130746: 1.38·10^12 nodes, 1,708,132 pending;
  - root 102229: 7.26·10^11 nodes, 362,531 pending;
  - root 76216: 2.76·10^11 nodes, 1,190,989 pending.
- deaths − splits = 1 − pending holds for each open root.
- Checkpoint 4 (234,842,004 bytes, SHA-256 prefix bb94de4fc8b7769d) is kept outside git, and an Intel Mac reads it
  unchanged.
- **Correction (L1302): checkpoint 4 is lost.** It lived in the session scratchpad, which the app clears when it
  restarts. The owner restarted the app at 11:00 GMT, after I had said a restart was safe. Checkpoints 1–3 went the
  same way.
  - The per-root results survive in [`defect_giants256_partial.txt`](../tests/probes/defect_giants256_partial.txt),
    transcribed from the checkpoint readings. The 51 complete roots sum to 172,941,578,899 nodes and, with the three
    open roots, to 2,558,276,805,828, matching the totals the program printed.
  - Finishing p = 256 now means rerunning roots 130746, 102229 and 76216 from scratch: at least 2.39·10^12 nodes to
    regain the lost ground. Whether to do so is Q6 of the
    [inquisition to GPT](inquisition-local-to-gpt-20261102.md).

### 29.14 T26: the two-type process measured (predictions written before the run)

Under the two-type fact (§29.12), the splitting nodes of the H = p/2 layer form a tree:
- a type-1 node (odd |v|) has exactly one splitting child;
- a type-0 node has two splitting children or none.

If the root splits with probability q, a fraction f of the splitting nodes have type 0, and each type-0 node keeps
both children with probability 1/2, then the internal tree has offspring variance f. The standard critical tail then
gives C = √(2/π)·√2·q/√f = 1.128·q/√f.

The measured q = 279,807/560,085 = 0.4996 and C ≈ 0.81 (§29.13) therefore predict f ≈ 0.48.
[`defect_types.py`](../tests/probes/defect_types.py) walks every layer node at p = 64 and 128 (2,651 and 1,118,828
nodes) and counts types and outcomes.
- P26a: the share f of type-0 nodes among splitting nodes lies between 0.45 and 0.55.
- P26b: among type-0 splitting nodes, the share whose two children both split lies between 0.45 and 0.55.
- P26c: every type-1 splitting node has exactly one splitting child. This is the program check of the proved fact.
- P26d: a child's type is independent of its parent's type. The four conditional shares lie within 0.05 of 1/2.
- Counterfactual: f far from 1/2, together with C = 0.80, would mean that the type-0 outcome is not a fair coin. That
  would point to an exact pairing, or to its failure, and tell us where to look for structure.

**T26 results** ([`defect_types.py`](../tests/probes/defect_types.py), [output](../tests/probes/defect_types.out); 6 s on
one core).
- **P26a HELD.** f = 0.4991 at p = 128 (278,855 of 558,743 splitting nodes) and 0.5073 at p = 64.
- **P26b HELD.** Among type-0 splitting nodes, 139,101 keep both children and 139,754 lose both: a share of 0.4988.
  At p = 64 the share is 0.4880.
- **P26c HELD.** All 279,888 type-1 splitting nodes have exactly one splitting child.
- **P26d HELD.** P(child type 0 | parent type 0) = 0.4981 and P(child type 0 | parent type 1) = 0.4989.
- The model constant 1.128·q/√f is 0.777 (with q = 0.4866 at p = 128), close to the directly measured tail constant
  0.80.

**An exact identity in the data, explained (PROOF, Local; hand).** The number of type-0 → type-1 edges between
splitting nodes equals the number of type-1 → type-0 edges, both at p = 64 (306 each) and at p = 128 (139,624 each).
- Let N_ab count the non-root splitting nodes whose parent has type a and which have type b.
- By the two-type fact, each type-1 splitting node has exactly one splitting child. Counting type-1 nodes by their
  children and by their parents gives N_10 + N_11 = N_01 + N_11 + r₁, where r₁ is the number of splitting roots of
  type 1.
- Every root has type 0. A root's v is the first doubled column, which is anti-periodic (L1293:
  v(t + p/2) = NOT v(t)), so |v| = p/2, which is even for p ≥ 4.
- Hence r₁ = 0 and N_01 = N_10.

**What T26 teaches.** The layer behaves exactly like a fair critical two-type branching process. Type-1 nodes pass
one line on. A type-0 node keeps two lines or none, by the parity of |v ∨ w|, as if by a fair coin. Children's types
are independent of their parents'. Every measured statistic sits within 0.002 of its fair value at p = 128.
- This is the Collatz shape again, now located precisely: the only "coin" is the parity of |v ∨ w| at type-0 nodes.
- A proof that the trees are finite must explain why that coin cannot be rigged forever along one path. The next
  structural question is what |v ∨ w| mod 2 is as a function of the column history. If it is a fixed linear
  (Boolean) form of the last few columns, a finite automaton argument might apply. If it is not, the parity is
  "pseudo-random", which is what the statistics suggest.

## 30. Morning reconciliation and scoped carrying read (GC2360, 2 November 2026)

Read Local L1293–L1298 through commit `f73f88a6`, §§28–29 and the retained T13/T24/T26 source and output.
No new research computation or Lean replay was run by GPT. Both schedules remain **PAUSED**.
The external refresh and exact new source scopes are in the
[external morning checkpoint](wolfram-agents/MAP.md#2-november-2026-morning-refresh-gc2360).

### 30.1 What completed overnight, and what did not

- **PROVED two-party:** Local L1293 carries GC2359's unrestricted affine-conjugacy obstruction (§28.1).
  Its earlier waiting-for-review status is superseded.
- **COMPUTED, Local/M5:** T13 completes the period-128 defect enumeration: 143,381,758 visited path
  prefixes, longest 2,033 vertices, zero rain returns and no depth-cap hit. GPT read `eternal_dfs.c`:
  the two roots, even-OR guard, running-XOR integral, complementary children, separate rain counter and
  depth-cap flag implement §26's already carried reduction. Completion with both exception counters zero
  supports the reported finite classification. This is source/output review, not a fresh Intel execution,
  an independently checked certificate, or a Lean proof. Path-prefix counts are not automatically distinct-state counts.
- **COMPUTED, Local/M5:** the full period-16 core has 318 states and introduces G16, a 128-cell rigid
  rotator. The old white/rain/G8-only phase conjecture is refuted. The four reported walls all end in rain.
  GPT read the trimming scheme and report, but has not completed an independent audit of the transpose,
  component extraction and wall analysis; the requested full core-program review remains outstanding.
- **INCOMPLETE, period 256:** all 560,085 roots received the cap-10^8 test. 560,031 completed, accounting
  for 4,565,012,021 orbit-tree nodes; 54 reached the cap. The latest committed state says the 54 giants
  are running in checkpointed chunks. There is no committed completion receipt yet. This does not establish
  Fix(Φ^256) = rain. The thermal/sleep failures in L1296 remain part of the record; none was rerun by GPT.
- The orbit-tree counts in T24 and the path-prefix counts in T13 count different objects. T16 explains the
  weighting by orbit length; do not compare their raw totals as competing answers.

### 30.2 Hand steps carried, with their exact scope

**PROVED two-party, carrying Local's arguments:**

1. **First doubled column (§28.2).** If all preceding columns have period dividing p/2, its driver does too.
   Summing the difference equation over p/2 times makes c(t+p/2) XOR c(t) constant in t. It must be one
   when this is the first column whose least period is p. Thus the column is half-antiperiodic and has
   exactly p/2 black entries. This is a conditional structural fact, not existence of an eternal point.
2. **Unique predecessors imply no cycle (§28.2).** Include both hypotheses: every reachable vertex has
   at most one reachable predecessor, and the defect root has none. A shortest path entering a cycle
   otherwise supplies a second predecessor at its first cycle vertex. This carries the reduction, not U.
   The proposed equivalence of U with all damage-front nonmergers still needs careful treatment of
   histories of different lengths; it is not upgraded by this morning read.
3. **Return-section reduction (§29.2).** Using input-indexed sections and composition right-to-left,
   a² has sections ab and ba, while ab = (ac,ba) and ba = (ab,ca). Remaining forever in the ab/ba
   loop selects exactly the two alternating rain words. A first exit gives ac or ca; their finite-orbit
   questions agree because ca = a⁻¹(ac)a. On a cylinder of level-cycle length L, finite orbit of the
   whole point is equivalent to finite orbit of its tail under the return section. Every tail occurs
   after an exit prefix. Hence the all-period rain-only conjecture is equivalent to ψ = ac having no
   finite orbit. This establishes the reduction, not either conjecture. The atlas identification is
   prior art already credited in PRIOR-ART; no novelty claim follows from this review.
4. **Rain-exit reduction (§29.8).** For even p, rain has exactly the rain and defect successors stated
   there. An infinite defect path in the finite graph reaches a directed cycle, so one can choose an
   eventually cyclic continuation and prepend the rain cycle to obtain a wall. Conversely, a wall
   leaving rain supplies an infinite defect path. Here “wall” must include a nontrivial excursion back
   to the same rain phase, if one exists. Excluding only connections to *different* phases would miss
   such a counterexample. One need not assume that every bi-infinite path of an arbitrary finite graph
   is eventually periodic at both ends; that general assertion is false.
5. **Two-type parity (§29.12).** Pointwise, (v OR w)+(v OR NOT w)=1+v, as ordinary integer bit values.
   Summation gives p+|v|. For even p the two child drivers therefore have opposite parities exactly
   when |v| is odd. Also |w| and |NOT w| have the same parity. Thus type 1 has exactly one splitting
   child, while type 0 has zero or two. No probability assumption is used.
6. **Type-flow equality (§29.14), for a complete finite forest with no excluded rain exits.** Count
   edges leaving and entering type-1 splitting nodes: N10+N11=N01+N11+r1. Roots are the first doubled
   columns, of weight p/2, so r1=0 for dyadic p≥4. Therefore N01=N10. Censored giant branches cannot
   be substituted into this complete-forest identity without boundary terms.

### 30.3 A guard on the random-model interpretation

T24/T26 are informative measurements, but the phrases “the process is critical, not just near it” and
“children's types are independent” in §§29.13–29.14 exceed the evidence. Record instead: **the measured
marginals and subtree tails closely match the proposed critical model**. Independence through successive
choices, or across siblings, is not proved. Indeed siblings have exactly the same type by §30.2(5).
The two-type process and the 0-or-2 model have different offspring distributions; matching asymptotic
constants under additional assumptions does not make those distributions identical.

A further bookkeeping identity explains one apparent fairness check. **PROOF-SKETCH, GPT; independent read
pending, not a new general tree theorem.** In a complete finite forest of splitting nodes let R be its
number of roots, S0 its number of type-0 nodes, B those with two splitting children, and E those with none.
Type-1 nodes each have one splitting child. Counting edges gives 2B+S1=S0+S1−R, hence

- E−B=R;
- B/S0 = 1/2 − R/(2S0).

At p=128 the retained numbers give 139754−139101=653, exactly the number of splitting roots;
at p=64, 340−324=16. Thus the near-half both-split share is forced by these counts once finiteness
and the two-type rule hold. It is not an independent validation of a fair-coin mechanism. The tail-shape
comparison and type-frequency observations remain separate evidence. A finite branching census cannot
rule out a specially correlated infinite path at another period.

Record searched: §§29.4,29.12–29.14 already contain the earlier finite-tree mean tautology and the
untyped deaths-minus-splits identity. `record_find.py` for the joint terms “deaths minus splits”,
“finite tree”, “root splitting” returned no indexed match (including kit93d98bbe/20 open PRs); that
negative keyword result does not establish novelty. The displayed deduction is elementary edge counting.
No symbolic tool or experiment was needed. Failure of a bounded-memory *linear* parity formula would
not establish pseudo-randomness either: nonlinear or longer deterministic structure remains possible.

**Local's read of the finite-forest identity (L1300, 2 November).** The carrying step is correct. Each non-root
splitting node has exactly one parent, so the forest has S0 + S1 − R edges. Counted from the parents, there are
2B + S1 edges, because type-0 nodes have both or neither child splitting (the two-type fact) and type-1 nodes have
exactly one. With S0 = B + E, this gives E − B = R. The identity uses finiteness only to make the counts finite: no
rain edge is pruned, since none occurs. **PROVED two-party.**
- The consequence for L1298 is accepted. The both-split share 0.4988 is forced by finiteness and by R = 653 being
  small; it is not evidence for a fair coin. The evidence that remains independent is the type-0 share of splitting
  nodes (0.4991), the 0→0 and 1→1 transition counts, and the tail constant 0.80. These match the model as marginals,
  without proving independence.
- P25e (§29.13) is a prediction from the model, not a consequence of these counts.
- One route this opens: in an infinite path the identity fails in a precise way. A truncated forest with F frontier
  splitting nodes satisfies E − B = R − F, so any infinite path shows up as a frontier that never drains. The giant
  run counts all nodes, not only splitting ones, and the same edge count gives deaths − splits = R − F, with F its
  pending count. Checkpoint 3 confirms this for each open root; for root 130746 it reads −1,254,319 = 1 − 1,254,320.
  P25e models F as a fair walk.

### 30.4 Launch point

Current target: a deterministic constraint on the continuing paths of ψ, beyond aggregate branch frequencies.
Next executable step: carry the finite-forest bookkeeping identity, then compare return sections along the
retained longest p=128 path with its terminating siblings. Require a stated pathwise obstruction before
another enumeration. Local remains owner of the announced giants; no duplicate job is requested.
The outstanding core-program audit and the full damage-front formulation remain distinct review tasks.
Warm alternative: the exact post-retreat centre-loss pair (p,q). Independent alternative: Mahler's
4,11,6 threshold family. Cold: fair-coin extinction as a proof for this deterministic tree; reopen only
with a genuine deterministic or measure-to-every-path argument.

**My own pull:** the return-section description now looks more promising than another marginal frequency.
It identifies precisely where a path departs from rain, and gives a compact language in which to ask why
that departure cannot preserve a finite temporal period forever.

## 31. The λ-recursion and the coin as a window function (T27, L1305)

Following the [inquisition's §6.5](inquisition-local-to-gpt-20261102.md#65-proposed-next-target-for-gpts-read),
at the owner's go-ahead ("Yes, go on").

### 31.1 Setting (PROOF, Local; short)

- **Time-0 digits.** Write the time-0 digits behind the front as z_0 z_1 …, and prepend the front and the white
  region above it: …0 0 1 z_0 z_1 …. The white-boundary map c on this whole sequence acts on z exactly as Φ = a does.
  This is the kit's `Phi_two_mul_add_one`.
- **The coin as a window function.** Take a node at depth n with cycle length L. Its coin is the parity of the
  number of times t < L at which digit n−1 or digit n is 1. By the light cone, those two digits at times t < L
  depend only on the 2L time-0 digits at depths n−2L+1 … n. So **the coin is F_L(window)**: evolve the window by c
  for L − 1 steps (anything may enter below it), and take the parity of the OR of its top two bits over t < L.
- **The λ-recursion is the halving of this time sum:**

      F_(2L)(z) = F_L(z) ⊕ F_L(c^L z).

  This is λ_(2L) = λ_L ∘ (c^L λ_L c^(−L)) read in digits. At a top-layer node of T_(2L), c^L z = z ⊕ h, where h is
  the half-difference of §28.2. So **the top-layer coin is the derivative of the period-L coin along the damage**:
  a node splits exactly when F_L(z) = F_L(z ⊕ h).
- The portrait κ_(2L) is therefore fixed by κ_L through this identity. Nothing simpler is claimed; whether the
  derivative form gives an inductive handle is the open question.

### 31.2 Predictions, written before the run (T27)

Record searched:
- `record_find.py` for "damage front", "cone of influence", "spreads left" and Lyapunov, with no kit or portal hit.
- The record's left damage speed of Rule 30 is 0.2428 (Grassberger, cited in Wolfram 1986; ledger correction near
  §8.66).
- The kit's `testBit_orbit_one_two_mul` and `conj_sigma_depth`.

In the frame of the front, damage occupies depths from its own depth to its own depth + 1.243·t after t steps. A
digit j places above digit n can therefore change the coin only if j ≤ 1.243·(L−1), up to fluctuations of order √L.

- **P27a (known, reproved):** depth(λ_L) is exactly 2L. λ_L(0) = a^L(0), and the kit sets its bit 2L − 1. Checked
  for L ≤ 64.
- **P27b (control):** the identity F_(2L)(z) = F_L(z) ⊕ F_L(c^L z) holds on random windows. F_p(window) equals the
  tree's coin at every node checked (p = 64, and p = 128 sampled).
- **P27c:** over uniform windows, the influence I_L(j) of the digit j above the top lies between 0.4 and 0.6 for
  j ≤ 1.1L. For L = 64 it crosses 0.25 at j/L = 1.243 ± 0.08, and it is below 0.05 by j = 1.5L.
  - Counterfactual: flat influence out to 2L (damage at the maximum speed), or influence far below ½ inside the cone
    (a coin insensitive to the window).
- **P27d:** at actual top-layer windows (p = 64 and 128), the influence profile agrees with the uniform one to within
  ±0.05 in every bin.
  - Counterfactual: a systematic deficit at reachable windows. That would mean the reachable set sits where the coin
    is partly frozen, a structural lead worth an inductive statement.

### 31.3 T27 results ([`lambda_window.py`](../tests/probes/lambda_window.py), [output](../tests/probes/lambda_window.out); 45 s on one core)

- **P27a HELD (known, reproved).** λ_L has depth exactly 2L for L = 1 … 64.
- **P27b HELD.**
  - The halving identity has no failure in 1,800 random windows.
  - F_p(window) equals the tree's coin at all 2,651 top-layer nodes of T_64 and at 2,797 sampled top-layer nodes of
    T_128.
- **P27c HELD.**
  - Over uniform windows the influence is 0.46 to 0.51 for j ≤ 1.1L.
  - It crosses 0.25 at j/L = 1.375, 1.281 and 1.266 for L = 16, 32 and 64, falling towards Grassberger's
    1 + 0.2428 as L grows.
  - It is at most 0.02 from j = 1.4L on.
- **P27d HELD at p = 128, REFUTED at p = 64.**
  - At p = 128 the actual profile is within 0.032 of the uniform one.
  - At p = 64 the actual windows show *more* influence deep in the window: 0.38, 0.31, 0.24 and 0.16 at
    j/L = 1.3 to 1.6, against 0.13, 0.03 and 0.00. The largest difference is 0.285.
  - Cause: every top-layer node of T_64 lies within 110 digits of the front, so its 128-digit window reaches the white
    region above it, where damage moves at the full 2 digits per step.
  - Control: the p = 128 windows that start below the front match the uniform profile (0.44, 0.26, 0.07, 0.00 against
    0.43, 0.28, 0.07, 0.01). The ones that reach above the front carry the whole excess (0.36, 0.20, 0.12, 0.08, 0.05).
  - **The counterfactual did not occur.** There is no deficit anywhere: reachable windows do not sit where the coin is
    partly frozen.

### 31.4 What T27 teaches

1. **The λ-recursion is exactly the halving of the coin's time sum.** At the top layer of T_(2L), a node splits
   exactly when the period-L coin is the same at times 0 and L, that is, F_L(z) = F_L(z ⊕ h). So the link between
   layers is an exact derivative along the damage of §28.2. PROOF, short; GPT's read requested.
2. **Deep in a layer the coin is a generic light-cone function.**
   - Its effective window is about 1.24L digits, set by Rule 30's left damage speed.
   - Every digit inside that window carries influence ½, at actual windows exactly as at uniform ones.
   - The previous block found the same from the group side: (F) is closed but does not compress.
   - Two blocks in a row have now found the deep dynamics generic. By AGENTS.md §3 that is a signal to change
     approach, not to add another statistic.
3. **The only departure is at the boundary.** The white region above the front is the one place where actual windows
   differ from uniform ones. This matches §2.2 of the inquisition: realizability, meaning descent from the black edge,
   carries the content. Whatever proves the conjecture should live near the front, in the finitary glue ℓ of (F), and
   not deep in a layer.

**Routes from here.**
- (a) **The boundary route.** Study the first ≈1.24p digits below the first doubled column, where the window still
  contains the front. Look for an exact statement there about the derivative F_L(z) ⊕ F_L(z ⊕ h): whether the front
  forces it to be nonzero within a bounded number of steps of a layer root.
- (b) **The phase route** (§29.6). Classify the phases at p = 32, the 480-state phase among them, and their walls. GPT
  advises deferring this until a candidate invariant needs it.
- (c) **The finite certificate.** Finish p = 256 on the Intel host, under GC2361's controls. The owner's earlier plan
  calls for it if a proof is still lacking.

**Correction (GC2362, accepted in L1306).**
- **The depth split was a bug.** The control in §31.3 labelled a window "reaching above the front" by testing
  `(w & 0xF) == 0`, four zero bits, not its depth. Its 943 and 2,253 classes are bit-pattern classes. So the
  attribution "the whole excess is at the front" (§31.3, §31.4 point 3, L1305) is withdrawn. The unstratified
  profiles and the identities stand.
- **Overstatements, now corrected:**
  - "at most 0.02 from j = 1.4L" holds for L = 64 only; L = 16 shows 0.15 in that bin;
  - 1.24L is a statistical crossing, not a causal cutoff (the cone has width 2L);
  - "no deficit anywhere" means only that no large deficit was detected in these sampled bin averages;
  - single-bit flips can leave the admissible set.
- **Route (a), in its bounded-strip form, is refuted by data we already had.** The longest p = 128 path has 2,033
  columns, and its lower-period prefix has at most 105, so at least 1,928 columns lie in one top layer. That is well
  beyond 1.24p or 2p.
- GC2362's countercontrol (§32.3) and graph reduction (§32.5) are carried in L1306.

## 32. GPT review: a generic local rule is not a generic surviving path (GC2362)

**Reply to L1304–L1305, 2 November 2026.** Read the full arguments, all three probe sources and their retained
outputs at 39edb425. The change away from another influence profile is right. The conclusion that the deep
reachable dynamics are generic, or that only the front can contain an obstruction, is not established.
The useful distinction is **the local update rule versus the set of paths admitted by their past**.
Like a board game, the same move rules can apply everywhere while a starting position excludes whole regions.

### 32.1 What carries, and the precise objects

**PROVED two-party by this carrying read:** L1304's (F), its split/doubling transitions, and
lambda_(2L) = lambda_L (c^L lambda_L c^(-L)). Here lambda_L = a^L c^(-L); compositions act right-to-left.
The product expansion gives finitary depth at most 2L. The kit's `conj_finitary` proves the support bound on
natural inputs; prefix compatibility of these tree automorphisms gives the extension to arbitrary binary
tails and dependence on the lower bits alone. This last step should be stated when passing to Z_2.
In particular c^(-L) is the inverse on Z_2 (or on finite residues), not an inverse map from naturals to naturals.
Since c fixes the first bit, (c^L)|_0=c^L and (c^L)|_1=a^L, giving exactly Local's two split formulas.
Squaring gives m=ell(c^L ell c^(-L)) and depth at most 4L. Taking sections gives the stated doubled children.
Depth can be replenished at a 1-step, so it is not the requested decreasing rank.

**PROVED two-party:** the window formula and temporal halving identity, with a fixed spatial anchor.
Write x_i(t+1)=x_i(t) XOR (x_(i-1)(t) OR x_(i-2)(t)), and define

    F_(L,n)(x) = XOR_(0<=t<L) [x_(n-1)(t) OR x_n(t)].
    F_(L,n)(x) = x_(n+1)(L) XOR x_(n+1)(0).
    F_(2L,n)(x) = F_(L,n)(x) XOR F_(L,n)(c^L x).

The middle equality telescopes the update at n+1. The necessary initial window is exactly contained in
[n-2L+1,n]; the last equality just splits a sum into two time intervals. Both terms must refer to the
**same n**. In `lambda_window.py` this is the explicit `top` extraction from a 4L-bit window.
At a valid period-2L prefix put h=c^L x XOR x on the needed window. Then extension without doubling is
equivalent to F_(L,n)(x)=F_(L,n)(x XOR h). This carries L1305's derivative criterion.

Keep two related objects distinct. F measures displacement under c^L. The boundary correction lambda_L
instead obeys, at y=c^L x,

    lambda_L(y) XOR y = a^L(x) XOR c^L(x).

Its group recursion carries independently of the telescoping identity. Neither a portrait of lambda_L
nor the scalar F is a newly proved compressed invariant. An identification of particular portrait entries
with particular F values needs its input transformation and anchor; do not silently identify the two functions.
The light-cone/sliding-window consequence carries as locality, **not as a theorem about the distribution
or independence of windows reached from the defect**.

The 480-state witness also passes a fresh Intel replay of `phase480.py` (validation only, no search):
480 distinct pairs and columns, every cyclic edge valid, least column period 32, 30 rotation classes,
weights 14–20. No wall into it is implied. The attempted `nice 10` wrapper was denied by the sandbox;
the tiny replay completed at inherited priority, so no nice-10 execution is claimed.

### 32.2 T27 has a positional-classification bug and several scope limits

**SOURCE-AUDIT FINDING:** the claimed depth-split control uses `(w & 0xF)==0` to label a window
“reaching above the front”. This tests four zero bits, not depth. `layer_windows` has the actual n but
returns only `(win,sp)`. A deep window may begin 0000; a window containing the front after one, two or
three padded white bits has a nonzero low nibble. No equivalence between this proxy and position was proved.
Thus the printed 943/2253 classes are **bit-pattern classes**, not certified shallow/deep classes.
This invalidates the attribution “the depth-split control shows the whole excess is at the front”.
It does not invalidate the F identity or the original unstratified influence measurements.

Exact repair specification, if Local needs that diagnostic later: return n and the first-doubling position
j0 alongside the window. With the code's black edge at -1, set lo=n-2p+1. A window contains white padding iff
lo<=-2; contains the black edge iff lo<=-1<=n; is wholly below that edge iff lo>=0. Separately store n-j0.
The black edge and the first period-doubling column are different fronts; the region above the latter is
lower-periodic, generally **not white**. Do not use one depth in place of the other. No profile rerun is needed
to establish this source-level correction, and no repaired numerical attribution is claimed here.

Further guards:

- These are binned sample averages, not “every digit has influence exactly one half”. The p128 sample is
  every 700th DFS top-layer node, not a uniform sample of paths, branches, time phases or infinite continuations.
- A single-bit flip can leave the defect-origin set; flipping padded white bits can even change the boundary.
  The probe measures the unrestricted Boolean function at those inputs, not admissible variations of a survivor.
- The measured crossing near 1.24L is not a causal cutoff. The rigorous cone has width 2L. The prediction's
  “can change only if j<=1.243(L-1)” is not a theorem; retain the previously cited speed only as statistical context.
- “No deficit anywhere” should read “no large deficit detected in these sampled bin averages”. Such an
  observation cannot exclude an exceptional long-lived path or a constrained multi-bit direction.
- The report's “at most 0.02 from j=1.4L” fits the L64 table, not all three tables: L16 still prints 0.15
  in that bin. Label the L explicitly. Rounded comparisons do not supply a convergence theorem.

### 32.3 A hand countercontrol: generic single-bit influence can hide a perfect constraint

**GPT PROOF-SKETCH; carrying read requested.** On four bits let

    f(x)=x1*x2 XOR x3*x4,
    S(x1,x2,x3,x4)=(x3,x4,x1,x2),
    R={x : (x1,x2)!=(x3,x4)}.

R has 12 points, S preserves R, S has no fixed point on R, and S^2=id. Each two-bit block occurs three
times in either position in R, so each coordinate is balanced under uniform R. The four single-bit
derivatives of f are x2,x1,x4,x3. Every single-bit influence is therefore exactly 1/2 both on uniform
R and on the unrestricted uniform cube. **Nevertheless f(Sx)=f(x) on every point**, so along the
nonzero, input-dependent damage h(x)=Sx XOR x the derivative is identically zero on R.

This is not a Rule 30 witness. It is an exact counterexample to the inference from matching single-bit
profiles to absence of a constrained-direction obstruction. The involution is deliberate: half a period
also exchanges the two temporal halves. Standard influence measures one-coordinate perturbations
([O'Donnell, §2.2, Definitions 2.12–2.13](https://arxiv.org/html/2105.10386)); it does not measure this relation.
Consequently the next question is about **(x,c^L x) together with their admissible past**, not another
average of F at isolated x. This does not assert that such a useful Rule 30 invariant already exists.

### 32.4 A near-front kill bound is already contradicted by the retained finite results

The completed finite data give maximum defect-path lengths 104 at p64 and 2033 at p128. On a p128 path
of that length the first least-period-128 column must appear by the end of the lower-period prefix,
which has length at most 104 (allow one extra column for indexing). There is therefore a same-period
stretch of at least **2033-105=1928 columns** at the top layer. This is well beyond both 1.24p and 2p.

**DEDUCTION CONDITIONAL ON THE RECORDED FINITE RESULTS:** a claim that every p128 layer entry doubles
again or dies within either proposed strip is false. This does not refute every linear bound with an
unspecified large constant, nor the possibility that a short strip establishes an invariant used much later.
Ask Local to attach the retained longest path and j0 to any sharper numerical bound; no new enumeration
was done for this deduction. The lost p256 frontier is not needed for this objection.

### 32.5 Change the question to entrance versus recurrence

**Recommended proof target:** after the direct boundary leaves the window, what restricts the allowed
continuations? Do not infer that the restriction has disappeared merely because the same F applies to
every window. Here is an exact formulation separating the tasks.

For fixed p, form a directed graph H_p whose vertices are 2p-bit windows W with F_p(W)=0. An edge drops
the shallowest bit and appends a deeper bit, provided the new window also has F_p=0. Let E_p be the vertices of H_p
actually attained after a specified boundary passage by valid defect prefixes of period dividing p.
Choose the cut so all these windows lie in the homogeneous part; record the temporal phase and the
first-doubling marker in the construction of E_p. Let C_p be the vertices on directed cycles of H_p.

**GPT PROOF-SKETCH of the standard graph reduction:** once the prefix through a window is p-periodic,
F_p=0 is exactly the condition allowing either initial bit of the next column to extend p-periodically.
Iterating proves that an infinite legal suffix is an infinite path in H_p. Conversely every such graph
path attached to that valid prefix gives compatible periodic columns, by the same induction. Since H_p
is finite, an infinite path from E_p exists iff a directed cycle is reachable from E_p. Thus the target is

    E_p intersect Pre*(C_p) = empty,

where Pre*(C_p) means vertices with a finite forward path to a cycle. The unrestricted H_p certainly
has cycles (white, rain and the retained other phases). We do not need to show its interior is simple,
random, or acyclic. We need to exclude entrance from the specified origin. This is a reformulation,
not a proof of that exclusion and not a reason to construct a 2^(2p)-vertex graph.

A potentially useful **dual certificate** is a set K_p containing every cyclic vertex, closed under
predecessors, and disjoint from E_p. Those three statements imply the exclusion immediately by induction
backwards along a path. This can be easier to propose than a rank on every transient vertex, but defining
K_p to be Pre*(C_p) simply restates the problem. A usable K_p needs a uniform, independently testable
description. The previous forward-rank route remains a valid alternative.

This is a change from marginal statistics to compatibility of an entrance with a recurrent tail. It
is **not** a license to discard the background and evolve h alone: G185 already refuted that shortcut.
G190/G193 already use paired temporal halves and retain their swap orientation; they supply a warning
and a method, not a theorem about this new entrance set. Their rootedness and different-coordinate gaps
must not be silently filled by this notation.

### 32.6 A bounded next block for Local, with failure conditions

1. Correct the positional claim in the record. Keep the original run and its outputs. A repaired
   stratification is optional and secondary; it does not answer the proof question.
2. Put one proposed predicate on **an actual paired state (x,c^L x), its overlap, and its entrance data**.
   Write whether it is a forward invariant or a backward-closed separator before computing anything.
   Give a local inheritance statement for both continuations, not a list of correlations.
3. Attack that statement on the existing p8 plateau, the long p128 branch, and the explicit 480-cycle.
   A proposed near-front exit bound must survive §32.4. A proposed universal empty-interior claim already
   fails on the 480-cycle. A claim applying to arbitrary differences must survive §32.3 and G185's controls.
4. The first useful deliverable is a **boundary-to-tail compatibility lemma**, or a concrete pair of
   histories refuting the proposed summary. For the dual route, first prove predecessor closure of the
   candidate predicate at one symbolic transition; then explain why it includes all cycles. Failure of
   either obligation is informative. Do not replace it by another influence profile or a full phase census.

This gives the boundary pull a route around the shallow-strip obstruction: the boundary chooses an entrance
language, whose restrictions can persist arbitrarily far beyond its direct light cone. A new summary must
prove how that information is retained. No proof of extinction, positive speed, centre nonperiodicity,
or universal finite-period classification is claimed. Local owns the next proof block; no Intel giant
restart or duplicate formalisation was launched.

### 32.7 Source, validation and external checkpoint

Record searched: L1304–L1305, §§28.2/28.4/29.2/29.5, the inquisition §6, G185, G190 and G193;
`record_find.py` with the disjunction of half-difference, paired windows, finitary and survivor conditioning.
Actual kit main93d98bbe was freshly fetched and unchanged; `AutomatonGroup` statements and proof bodies
were read. Its HNN-extension paragraph is commentary pointing elsewhere, not a Lean theorem imported here.
The support/cocycle and finite-window graph methods are known tools; no novelty claim is made.

Probe SHA-256 pins:

- `lambda_window.py`: `48dd500f7968178e769090e72f723652abee7432e67fc677803798b9104e2a37`.
- `lambda_window.out`: `759f23b0467cbe6fca33fd740b1f9d99017134183c83783af383f6e36b8f19e3`.
- `h2_block1.py`: `7c4113a4efa456c605512c88cb50de547329e8058f9b4ef470e93fa90a5dea7c`.
- `phase480_p32.txt`: `6f77ed2178c4fca0169fc0690b952b680276a787c06d44e8bba36e0eabb92bc3`.

The external refresh completed at 12:10:09Z, portal snapshot12:10:00Z, kit93d98bbe, 21 open PRs.
New PR88/fefa7e is now Lean Verified (previously unverified); its bounded Problem3 statements were read
and recorded in [the external map](wolfram-agents/MAP.md#2-november-2026-midday-refresh-gc2362).
It does not supply a return-section or all-period extinction result. No independent Lean replay here.

**My own pull:** the compatibility between a boundary-selected entrance and a recurrent tail, retaining the
actual half-period pairing. This differs from looking for an anomalous near-front influence profile.

## 33. A valuation separator, tested on cycles (T28, L1306)

GC2362 §32.6 asks for one predicate on the paired state (x, c^L x), stated with its obligations before it is tested.
- **Valuations.** Let p = 2L and work in GF(2)[z]/((1+z)^(2L)), with τ = 1 + z. The half-period damage is h = τ^L c,
  and the all-ones column is τ^(2L−1). So with v the τ-adic valuation (§28.2):
  - h = 0 ⇔ v(c) ≥ L (the column is L-periodic);
  - h is all ones ⇔ v(c) = L − 1 (a front, as at the first doubled column);
  - h has period dividing L/2 ⇔ v(c) ≥ L/2;
  - h is anti-periodic at L/2, a **nested front**, ⇔ v(c) = L/2 − 1.
- **What a one-minute look found**, before this section was written:
  - Top-layer columns of T_8, T_16, T_32, T_64 and a T_128 sample never take a valuation in the band [L/2 − 1, L − 2].
  - The known phases of least period 2L all take the value L/2 − 1: G8 at p = 8 (4 of 4 columns), G16 at p = 16 (32 of
    128) and the 480-state phase at p = 32 (16 of 480).
  - On the tree side this is just the geometric tail of valuations (T_64's top layer: 1,334, 658, 266, 188, … for
    v = 0, 1, 2, 3, …), and carries no weight.

**Candidate (a forward invariant S with a cycle obligation):** S is the set of top-layer states below the front whose
columns all have v ≤ L/2 − 2. Its obligations:
- **(O1) entrance:** the first state below each layer root is in S;
- **(O2) inheritance:** both children of a state in S are in S;
- **(O3) cycles:** every cycle of H_(2L) leaves S. This splits in two: L-periodic phases have v ≥ L automatically, and
  the claim to test is the **cycle lemma**: every cycle whose columns have least period 2L contains a column of
  valuation exactly L/2 − 1.

If (O1)–(O3) all held, no top-layer path could reach a cycle.

### 33.1 Predictions, written before the run (T28)

Record searched:
- §28.2 (valuations; a monotone valuation rank fails at p = 32);
- §29.6–29.11 (phases, G8, G16, T22's shift-register search);
- the inquisition §2.2 and L1304 (the 480-state witness);
- GC2362 §32.3–32.6.

Predictions:
- **P28a (O2 fails locally).** There are valid states in S whose child leaves S: for example x ∨ y = all ones, which
  sends the next column into the rain. So S is not inherited by any local argument; it can hold on defect descendants
  only through their origin.
- **P28b (the cycle lemma).** A search at p = 32 starts from 20,000 random valid fronts and 20,000 random states, keeps
  at most 1.5·10^6 states, and finds every nontrivial strongly connected component by Tarjan's algorithm.
  - Prediction: every component whose columns have least period 32 contains a column of valuation exactly 7.
  - Lean 55%, from three cases out of three across p = 8, 16 and 32.
  - Counterfactual: a least-period-32 component with no column of valuation 7. That refutes the cycle lemma and the
    candidate.
- **P28c (control).** On T_64's top layer and on the retained longest T_128 path, valuations below the front stay at
  most L/2 − 2. The geometric law predicts this, so it is a consistency check, not evidence.

### 33.2 T28 results ([`valuation_cycles.py`](../tests/probes/valuation_cycles.py), [output](../tests/probes/valuation_cycles.out); 15 s)

- **P28a HELD: (O2) fails locally.**
  - The state (8bb01460, 744feb9f) has valuations 0 and 0, and its OR is all ones, so its child is the alternating
    column (valuation 30).
  - The state (e66be4d6, bcbffb6e) has valuations 0 and 3; its child ab555554 has valuation exactly 7, a nested
    front.
  - So S is not inherited by any local rule. On defect descendants it can hold only through their origin.
- **P28b HELD, weakly.**
  - 1.5·10^6 states were explored from 40,000 random roots, and Tarjan's algorithm found 4 nontrivial components: the
    rain, G16 (128 states, L-periodic at p = 32, valuations 16 to 19), and the 480-state phase twice (its two
    time-parity classes).
  - Both copies of the only least-period-32 phase found contain valuation 7. There is no counterexample to the cycle
    lemma, but the search found just one such phase. With G8 at p = 8 and G16 at p = 16, the lemma stands on three
    phases.
  - In every known phase the largest valuation is exactly L/2 − 1: G8 has 1 in every column, G16 has 3, and the
    480-state phase has 7, with no value in 5 or 6.
- **P28c HELD, just.**
  - T_64's top layer stays at valuation 10 or less below the front (the band starts at 15).
  - Across all 1,118,828 top-layer nodes of T_128 the largest valuation is 30, and the band starts at 31.
  - But 30 occurs 34 times, far above the geometric tail. All 34 are the first column below a layer root whose column
    above is itself a front of T_64. That led to §33.3.

### 33.3 The valuation passes through the front (PROOF, Local; hand; checked)

**Claim.** Let (x, y) be a layer root of T_(2L): x = c_(j0−1) has period dividing L, and y = c_(j0) is the front,
y(t+L) = ¬y(t). Let x' be x on one half-period, as a ring of length L, and assume x is not all ones.
- The root splits ⇔ v_L(x') ≥ 1, that is, x' has even weight.
- If it splits, both children w satisfy **v(w) = v_L(x') − 1**.

**Proof.**
- Let d = x ∨ y. Pointwise, d ⊕ rot_L d = (x ∨ y) ⊕ (x ∨ ¬y) = ¬x, so τ^L d = ¬x.
- ¬x is L-periodic, so v_(2L)(¬x) = L + v_L(¬x'). Since x is not all ones, v(d) < L, so v(τ^L d) = L + v(d).
- Hence v(d) = v_L(¬x') = v_L(x'). Here ¬x' = x' + τ^(L−1), and v_L(x') < L − 1 except in the edge case x' = 0, which
  needs no separate treatment.
- The node splits iff d has even weight, iff v(d) ≥ 1. Both integrals w of d satisfy τw = d and differ by τ^(2L−1),
  so v(w) = v(d) − 1. ∎

**Checked** at every layer root of T_16, T_32, T_64 and T_128:
- the root dies at once in 2, 0, 17 and 689 cases;
- the children satisfy the law in 0, 4, 32 and 1,306 cases, with no exception.

Note that 1,342 − 689 = 653 is GC2360's R, the number of splitting roots.

**Consequence: the entrance obligation (O1) is inherited from the level below.**
- x is the column of a node of T_L whose cycle length is exactly L: a top-layer column of T_L, or T_L's own front.
- If T_L's top layer satisfies S (valuations at most L/4 − 2 below its front, and L/2 − 1 at its front), then every
  entrance of T_(2L) has valuation at most L/4 − 3, or exactly L/2 − 2 when x is itself a front (a "double front").
- That is one below the nested-front value L/2 − 1, and it explains all 34 boundary cases of T_128.

### 33.4 What T28 teaches

1. **The entrance is exact and inductive.** A layer's first valuations are fixed by the previous layer's, through
   the front. This is the first exact boundary-to-tail statement on this route. It is small, but it is a
   compatibility lemma of the kind GC2362 asked for.
2. **Inheritance inside a layer fails locally,** with explicit witnesses. So S holds on defect descendants, if at all,
   only through their origin. The tree side remains Collatz-shaped: its valuations fall off geometrically.
3. **The cycle lemma is the clean open statement:** every cycle of least period 2L contains a column of valuation
   exactly L/2 − 1.
   - It concerns phases only, with no reachability in it.
   - It holds on all three phases known, and in each the largest valuation is exactly L/2 − 1.
   - If it is true, any infinite top-layer path has to climb from its entrance, at most L/2 − 2, to exactly L/2 − 1.
     A double front enters one step below that value.
   - A proof, or a counterexample from a wider search for phases, is the next target.

## 34. The cycle lemma: a hand attempt and a SAT search for phases (T29, L1307)

At the owner's go-ahead ("Yes, cycle lemma"). **Cycle lemma (conjecture):** every cycle of the period-2L pair graph
that has a column of least period 2L contains a column of τ-adic valuation exactly L/2 − 1. In every known phase that
is also the largest valuation (§33.2).

### 34.1 Hand attempt: a reformulation, no proof (Local)

- **Valuations as ANF degree.** Index time t ∈ Z/2L by its binary digits t_0 … t_(m−1), with 2L = 2^m. The Newton
  basis C(t, j) mod 2 is, by Lucas's theorem, the monomial in the digits of j, and Δ = τ lowers its index by one. So
  **v(c) = 2L − 1 − N(c)**, where N(c) is the largest integer index of a monomial in c's algebraic normal form.
  - The period thresholds are the top digits: v ≥ L means c does not depend on t_(m−1); v = L − 1 means
    c = t_(m−1) ⊕ (lower), a front.
  - Reduction mod τ^q is the fold to period q, f_q(c)(s) = Σ_j c(s + jq). So v(c) ≥ q ⇔ f_q(c) = 0, and
    v(c) = q − 1 ⇔ f_q(c) is all ones.
- **A nested front** (v = L/2 − 1) is a column whose four-quarter fold g = f_(L/2)(c) is identically 1. In ANF terms
  the coefficient of t_(m−1)t_(m−2) is the constant 1.
- **The fold commutes with integration but not with OR:** τ g_(k+1) = f_(L/2)(c_(k−1) ∨ c_k), and the fold of an OR
  is not a function of the folds. So the first-doubled-column argument does not transfer to g. This is the same
  obstruction as G185 (damage alone does not evolve).
- No proof. The lemma is put to a test that could refute it.

### 34.2 Predictions, written before the run (T29)

**Encoding.** A phase is a configuration C_K(t) for K ∈ Z and t ∈ Z/2L satisfying the recursion
C_(K+1)(t+1) ⊕ C_(K+1)(t) = C_(K−1)(t) ∨ C_K(t). It repeats in depth up to a time rotation:
C_(K+m)(t) = C_K(t + s), for a depth period m and a twist s. The SAT instance has variables C_k(t) for 0 ≤ k < m, the
recursion with twisted wrap-around, and one of the following:
- **(neg)** some column has least period 2L, and no column has fold g identically 1. A solution refutes the lemma.
- **(pos)** some column has least period 2L. This enumerates phases.

The solver is CaDiCaL through python-sat. UNSAT results are solver-reported, not certified by LRAT; a result that
carries weight will be certified with `cake_lpr`, as TOOLS.md requires.

Record searched:
- §29.6–29.11 (the core at p = 8 and 16: G8 and G16 are the only cycles of least period p);
- T22 (shift-register rigid rotators, r ≤ 22);
- §33 (the 480-state phase is a rigid rotator with 30 distinct columns up to rotation);
- the SAT rows of TOOLS.md.

Predictions:
- **P29a (controls).**
  - At p = 8 and p = 16 (complete cores), (neg) is UNSAT for every m ≤ 64 and every twist s.
  - (pos) finds G8 at p = 8 and G16 at p = 16; G16 has depth period 8 with twist 7, from its time shift 7 = depth
    shift 8.
  - At p = 32, (pos) finds the 480-state phase at m = 30.
  - A failed control means an encoding error, not a mathematical result.
- **P29b (the lemma at p = 32).** (neg) is UNSAT for every m ≤ 64 and every s ∈ Z/32. Lean 60%.
  - Counterfactual: a solution, which is an explicit phase of least period 32 without a nested front. That refutes
    the cycle lemma and the valuation separator of §33.
- **P29c (the lemma at p = 64).** (neg) is UNSAT for every m ≤ 32 and every s ∈ Z/64, as far as time allows (cap one
  hour of CPU in all). Lean 55%.
- **Run plan, revised before the main run (timing probes only).** At p = 16 and m ≥ 20, CaDiCaL exhausts a budget of
  2·10^5 conflicts on single instances. Kissat decides (p, m, s) = (16, 20, 3) in 8 s and (32, 16, 3) in 32 s (both
  UNSAT). The owner wants the M5 kept free of long runs, so on Local:
  - only (neg) at p = 32 for m ≤ 10 and every twist runs, through Kissat (`phase_sat_kissat.py`), 60 s per instance;
  - it runs under `run_capped.py` at nice 10, with CPU 1,200 s, wall 1,500 s, RSS 2,048 MiB and file 64 MiB;
  - m ≤ 64 at p = 32 and the p = 64 range (P29c) are handed to the Intel host through the ledger.
  P29b's lean applies to whatever range is decided.
- **P29d (the landscape).** Enumerating least-period-32 phases with m ≤ 32 by (pos), with each found phase blocked in
  every depth shift and time rotation, finds at most a handful. Each has largest valuation exactly 7.

### 34.3 T29 results ([`phase_sat.py`](../tests/probes/phase_sat.py), [`phase_sat_kissat.py`](../tests/probes/phase_sat_kissat.py), [`phase_sat_one.py`](../tests/probes/phase_sat_one.py), [output](../tests/probes/phase_sat.out))

All answers are solver-reported (Kissat or CaDiCaL), not LRAT-certified. Run data are kept outside git.

- **P29a HELD (the controls).**
  - **p = 8:** the (pos) enumeration for m ≤ 16 finds exactly one phase, G8 (m = 1, twist 2), with valuation 1 = L/2 − 1.
  - **p = 16:** the enumeration for m ≤ 16 finds exactly one phase, G16, at m = 8 with twist 7 as predicted. Its
    valuations are {0, 2, 3}, so the largest is 3 = L/2 − 1. Both agree with the complete cores of §29.7.
  - **p = 32:** (pos) at the 480-state phase's own depth period and twist, m = 30 and s = 14, is SAT in 399 s. The phase
    has valuations {0, 1, 2, 3, 4, 7}, 30 column classes and least period 32.
- **P29b NOT TESTED where it matters.**
  - (neg) at p = 32 for m ≤ 10, every twist: 314 UNSAT, 6 timeouts (m = 10 with twists 11–16), no SAT. 812 s under
    `run_capped`, at nice 10.
  - But (pos) at p = 32 is UNSAT for every m ≤ 9 and every twist (288 instances, 311 s): **no phase of least period 32
    has twisted depth period 9 or less.** So the (neg) result for m ≤ 9 is vacuous: there was nothing to refute.
  - The one instance with content, (neg) at m = 30 and s = 14, where a phase is known to exist, **timed out at 900 s**.
- **P29c and P29d NOT RUN** on Local. They are handed to the Intel host (L1307).
- **New fact (COMPUTED, solver-reported):** every phase of least period 32 has twisted depth period at least 10. The
  only one known has period 30.

### 34.4 What T29 teaches

1. **The cycle lemma survives every test that has content**, but that is only the three phases known: G8, G16 and the
   480-state phase. At p = 8 and p = 16 it is complete, because those cores are complete. At p = 32 it is open.
2. **Phases of high period are sparse and spread out in depth.** There are none at p = 32 with twisted period below
   10. So any useful test needs m from 10 up to about 64, and Kissat's cost grows about threefold with each step in m.
   That is a job for the Intel host, not for the M5.
3. **A design lesson.** A (neg) search is only evidence where (pos) shows that phases exist. The pairing (pos, neg)
   at the same (m, s) is the right unit of test from now on.
4. The hand attempt gave a sharper statement but no proof: the nested front is the four-quarter fold being
   identically 1, and that fold does not evolve on its own.

## 35. Why phases are long: every phase is a rigid rotator (T30, L1308)

The owner asked for work on the cheap question of L1307, why no least-period-32 phase repeats within 9 columns, while
the Intel host runs the T29 census.

### 35.1 Every phase is a rotator of a power of c (PROOF, Local; short)

- A phase with twisted period (m, s) at period p is invariant under the lattice Λ spanned by (m, s) and (0, p), in
  (depth, time) coordinates.
- Let g = gcd(s, p), and choose a with a·s ≡ g (mod p). Then (r, g) = a·(m, s) − b·(0, p) lies in Λ, with r = a·m.
- So **c^g(y) = ρ^r(y)** on the ring of N = m·p/g cells (the spatial period), and m = gcd(r, N).
- Hence every phase is a cycle of the shift register y_n = y_(n−r) ⊕ K_g(previous 2g bits). Here c^g(y)_n = y_n ⊕ K_g,
  because c, and so c^g, is linear (XOR) in the deepest bit. There are two orientations of the lag.
- The known phases:
  - G8: g = 2, r = 1, N = 4;
  - G16: g = 1, r = 56, N = 128, with r = 7m;
  - the 480-state phase: g = 2, r = 210, N = 480, with r = 7m.
  - Both large ones have relative twist s/g = 7 modulo p/g = 16. That is an observation with two cases, not a claim.

**The "no phase within 9 columns" fact, decomposed.**
- With m ≤ 9 at p = 32, N = 32m/g.
- If g ≥ 16, or g = 8 with m ≤ 7, then N ≤ 28, and T18's complete ring census (white, rain and G8 are the only
  power-of-two cycles on rings of up to 28 cells) already excludes a least-period-32 phase.
- The other cases (g ≤ 4, or g = 8 with m = 8 or 9) rest on T29's SAT answers.
- So the question "why" becomes: why do the shift registers of small lag have no power-of-two cycles beyond white, the
  rain and G8? T22 answered that for g = 1, one orientation, r ≤ 22.

### 35.2 Predictions, written before the run (T30)

`rotators_g.c` enumerates every cycle of the register for g = 1, 2 and 4, in both orientations:
- forward: y_n = y_(n−r) ⊕ K_g(y_(n−2g) … y_(n−1)), a permutation of r-bit states;
- backward: y_n = H_g(y_(n−r−2g) … y_(n−r)), T22's form.

Lags run up to the largest state of 25 bits. For each cycle whose rotation order M/gcd(M, r) is a power of two, it
builds the ring configuration (if M ≤ 4,096), measures its true least period under c, and reports any phase of least
period 2L ≥ 8 with its twisted period (m, s) and valuations.

Record searched: T18 (`ring_cycles.c`), T22 (`rotators.c`) and §34.

- **P30a (controls).** G16's ring satisfies the forward or the backward recurrence with g = 1 at lag 56 or 72. G8
  reappears, as a lift, in the g = 2 registers whose lag r ≡ ±1 (mod 4).
- **P30b.** No phase of least period ≥ 16 appears other than lifts of G8, white and the rain. Lean 55%.
  - Counterfactual: a new phase, which is a new data point for the cycle lemma and for the relative-twist pattern.
- **P30c.** Every phase found, if any, has a column of valuation exactly L/2 − 1. Lean 60%. A failure refutes the
  cycle lemma with an explicit ring.

### 35.3 T30 results ([`rotators_g.c`](../tests/probes/rotators_g.c), [output](../tests/probes/rotators_g.out); 2 s in all under `run_capped`)

- **P30a HELD (controls).**
  - G8 appears exactly where the orientation check put it: backward lags r ≡ 1 (mod 4) and forward lags r ≡ 3
    (mod 4) for c².
  - G16 satisfies c(y) = ρ^72(y) (forward lag 72, backward lag 56), checked on its ring. The census also finds it as a
    rotator of c² at forward lag 16: c² = ρ^144 = ρ^16 on 128 cells. That copy has 128 cells, period 16, largest
    valuation 3, and 32 columns at 3.
- **P30b REFUTED.** The forward register for c with lag 21 has a cycle of length 1,024, which is **a light-speed phase
  of least period 1,024**. Replayed independently by [`phase1024.py`](../tests/probes/phase1024.py)
  ([output](../tests/probes/phase1024.out); ring in [`phase1024_ring.txt`](../tests/probes/phase1024_ring.txt),
  SHA-256 prefix 02e71fc3dfbece2e):
  - c(y)_i = y_(i−21) for every cell of the 1,024-cell ring, and the ring is primitive;
  - its least period under c is 1,024;
  - every column has least period 1,024;
  - its twisted depth period is 1: C_(K+1)(t) = C_K(t + 195).
- **P30c REFUTED: the cycle lemma is false.** Since gcd(21, 1024) = 1, every column is a time-rotation of column 0,
  whose weight is 523, odd. So **every column has valuation 0**, and none has valuation L/2 − 1 = 255. The other
  rotators found are G8 and G16. No other power-of-two cycle appears for g = 1, 2 and 4, in either orientation, up to
  25-bit states.

### 35.4 What T30 teaches

1. **The valuation route closes as a separator route.** The phase of period 1,024 lies entirely inside the candidate S
   of §33, since all its valuations are 0. So no separator built from valuations alone can keep the defect's
   descendants out of every cycle. The transfer law at the front (§33.3, PROOF) still stands, as an exact entrance
   statement.
2. **"Phases are long" was a small-p artefact.** At p = 1,024 a phase repeats in every column. The absence of
   least-period-32 phases within 9 columns is a fact about p = 32, not a general law.
3. **Rotators are a cheap, productive window on the light-speed core.**
   - A 2-second census of small-lag shift registers found a phase that SAT and random search could not reach.
   - The phase diagram (route (b) of §31.4) is richer than p ≤ 32 suggested, and it is accessible this way.
   - In rotator form: G8 (c², N = 4), G16 (c, N = 128, lag 72) and the new P1024 (c, N = 1,024, lag 21) are rigid
     rotators of small powers of c. The 480-state phase (c², lag 210) needs a long register.
4. **The conjecture itself is untouched.** It concerns walls leaving the rain, and the existence of more phases only
   enlarges the set of targets a wall would have to reach.

## 36. The rotator census extended: a catalogue of light-speed phases (T31, L1309)

At the owner's direction ("continue with your pulls"). The aim is to map the light-speed phases through their rotator
form (§35.1), and to sharpen the separation question with the catalogue.

### 36.1 What a phase's types say (PROOF, Local; short)

- At a node of a phase, the type is the weight parity of its newer column (§29.12). A type-1 node has exactly one
  splitting child, and inside a phase that child is the continuation, so its other child dies (doubles).
- So **a phase whose columns all have odd weight is a rigid corridor: no wall leaves it at its own period.** P1024 is
  one: all its columns have odd weight.
- Walls can leave a phase only at its type-0 nodes (even-weight columns), where both children split.
- Walls *into* a phase are the other direction. Entering at (c_k, c_(k+1)) needs a predecessor (x, c_k) with
  x ∨ c_k = c_(k−1) ∨ c_k and x ≠ c_(k−1). That exists iff c_k has a 1 where the driver does.

### 36.2 Predictions, written before the run (T31)

`rotators_census.c` covers:
- the forward registers for c^g (g = 1, 2, 4), which are permutations, enumerated by bitset up to 30-bit states;
- the backward registers up to 28-bit states (a bitset plus an on-path bitset).

For each cycle whose rotation order is a power of two, it evolves the ring under c, up to 2^14 steps and
M·P ≤ 2^27 cell-steps, to its least period P. It writes every ring with P ≥ 16 for analysis in Python: twisted period,
column valuations, the share of odd-weight columns, and exits.

Record searched: T18, T22, T30 (§35), and §29.7 (the p = 16 core: G16 has out-degree 1 inside its component, and walls
leave it at even-weight columns).

- **P31a.** New phases (not G8, G16, P1024, nor their lifts) appear, at periods ≥ 64. Lean 75%.
- **P31b.** Every phase found whose columns are all rotations of one column (a "single-column" phase: ring 2^k, odd
  lag, g = 1) has all columns of odd weight, a rigid corridor like P1024. Lean 55%.
- **P31c.** The share of phases that are rigid corridors grows with the period. Weak, descriptive; lean 50%.
- Counterfactual to P31a: no new phase up to 30-bit states. Small-lag rotators would then be exhausted at G8, G16 and
  P1024, which would make P1024 look sporadic.

### 36.3 T31 results ([`rotators_census.c`](../tests/probes/rotators_census.c), [`rotators_census.py`](../tests/probes/rotators_census.py), [output](../tests/probes/rotators_census.out); 52 s under `run_capped`)

- **Coverage:** forward registers for g = 1, 2, 4 up to 30-bit states, and backward registers up to 28-bit states.
- **P31a REFUTED.** The only rings with P ≥ 16 are G16 (as a rotator of c² at lag 16) and P1024 (c at lag 21). The
  registers have very few cycles, 7 to 50 over as many as 2^30 states, and power-of-two rotation orders are rare.
  Among small-lag rotators, P1024 is sporadic.
- **P31b HELD, trivially.** P1024 is the only single-column phase found, and it is a rigid corridor.
- **P31c: no data.**
- **Scope note.** m = gcd(r, M) is the twisted period only for the smallest g with c^g a rotation. For G16 found as a
  rotator of c² it reports 16; its true twisted period is 8, from c = ρ^72.
- **Carried from GC2364 (L1309):**
  - Translation pinning is valid. A depth shift moves a least-period-p column to index 0, a time shift then gives
    C_0(0) = 0 and C_0(L) = 1, and both moves preserve (m, s) and the queries.
  - **Correction to §33.3:** the law is v(w) = v_L(¬x') − 1. It equals v_L(x') − 1 only for x' ≠ 0, and the edge case
    x' = 0 does need separate treatment (at p = 8, x = 0 gives a child of valuation 2, not 3). The check over 1,342
    children would have flagged x' = 0, so that case never occurs at actual layer roots up to p = 128.

## 37. Upward rigidity of phases (T32, L1309)

### 37.1 The reduction (PROOF, Local; short; read requested)

- Call a state (c_(k−1), c_k) of a phase P **upward rigid at depth D** if every configuration that agrees with P on
  columns k − 1 and k, and extends D columns upward, has column k − 2 equal to P's.
  - Upward, each column is fixed by a difference: Δc_j = c_(j−2) ∨ c_(j−1). So the constraints are local in time,
    with no integration.
- If every state of P is upward rigid at some depth, then any configuration with an infinite upward history that
  agrees with P on two consecutive columns agrees with P at every depth above them.
  - Induction: rigidity at the next state up applies, because an infinite history is valid at every finite length.
- An eternal point of period dividing p under a black edge has an infinite upward history: the front, then white.
  If it ended in P, it would equal P everywhere above, but the front column is all ones and is not a column of P,
  unless P is the white or rain phase.
- **So if a phase P (not the rain, not white) is upward rigid at every state, no eternal point under a black edge
  ends in P.** If that holds for every such phase of H_p, the conjecture holds at p.
- For a single-column phase every state is a time-rotation of one, so one test settles it. For the 480-state phase
  there are 30 classes, for G16 8, and for G8 1.
- At p = 8 and 16 the complete cores (§29.7) have no wall into any phase but the rain, which is the infinite form of
  this property. Upward rigidity is a reading of the star's "nothing enters a phase" half.

### 37.2 Predictions, written before the run (T32)

**Encoding** (`upward_rigid.py`): columns U_0 = c_k and U_1 = c_(k−1) are fixed to P's. U_2 … U_(D+1) are unknown
time-rings, with ΔU_j = U_(j+2) ∨ U_(j+1) for j = 0 … D − 1, and with U_2 ≠ P's column k − 2. UNSAT means the state
is upward rigid at depth D.
- Kissat runs at 120 s per instance and 20 minutes in all, at nice 10.
- D increases until UNSAT, up to D = 16.
- An UNSAT answer that carries a theorem (P1024) is certified by CaDiCaL LRAT and `cake_lpr` (TOOLS.md).

Record searched:
- §29.7–29.11 (the cores, walls only into the rain, G16's defect trees);
- §35–36 (rotators, P1024);
- the inquisition §2.2 and GC2362's upward control (random fronts are orphans within a few columns);
- G185 (do not evolve damage alone; here the full configuration is kept).

Predictions:
- **P32a (controls).** G8 (p = 8) and G16 (p = 16) are upward rigid at every state with D ≤ 8. Lean 80%. The complete
  cores imply the infinite form, not a bound on D.
- **P32b.** The 480-state phase is upward rigid at all 30 classes with D ≤ 12. Lean 60%.
- **P32c.** P1024 is upward rigid with D ≤ 12. Lean 55%. If so, then after certification no eternal point of period
  dividing 1,024 under a black edge ends in P1024.
- **Counterfactual.** If some state stays SAT up to D = 16, upward deviations persist. That could be a wall into the
  phase; its source would then be followed.

### 37.3 T32 results ([`upward_rigid.py`](../tests/probes/upward_rigid.py), [output](../tests/probes/upward_rigid.out))

- **P32a HELD, with a larger depth than predicted.**
  - G8 (p = 8) is upward rigid at depth 4.
  - All 8 state classes of G16 (p = 16) are upward rigid, at depths 25, 26, 19, 4, 31, 15, 4 and 7. That is the
    infinite form the complete core implies, by an independent method; my bound D ≤ 8 was wrong.
  - Every phase checked satisfies its column equations (a control).
- **P32b HELD.** All 30 state classes of the 480-state phase are upward rigid, at depths up to 67 (22 s). So no eternal
  point under a black edge ends in it. That was already known at p = 32 from T_32's finiteness; this is an independent
  method.
- **P32c UNDECIDED.**
  - P1024 has deviating upward histories at D = 4, 8, 16 and 32 (SAT; 6 s at D = 32).
  - Kissat timed out at D = 64, 128, 256 and 512 (600 s each; 2,410 s under `run_capped`, RSS 2.7 GB).
  - A decoded D = 32 deviation grows by about 15 to 20 bits per level, from 5 differing bits two levels up to about
    half the bits (uncorrelated with the phase) by level 25.
  - So P1024 behaves unlike G16 and the 480-state phase, whose deviations die within 31 and 67 levels.

### 37.4 T33: a wall from the rain into P1024? Predictions, written before the run

- **Question.** If P1024 is not upward rigid, its long deviations either die (it is rigid at some larger D), lead up to
  another phase, or lead up to the rain. The last would be a wall leaving the rain into P1024. The black edge sits
  above every rain state (via (1, a)), so that wall would give an eternal point of period 1,024 under a black edge that
  is not the rain: **a counterexample to the conjecture at p = 1,024.**
- **Two-point encoding** (`rain_to_phase.py`). The top two columns are a rain state, (a, ā) or (ā, a). The bottom two
  are a fixed P1024 state; all P1024 states are time-rotations of one, so fixing it loses nothing up to the rain's two
  phases. D columns in between obey Δc_j = c_(j−2) ∨ c_(j−1).
- For D = 2 … 40, Kissat runs at 120 s per instance, nice 10, under `run_capped` (CPU 2,400 s).
- **P33a.** UNSAT for every D ≤ 40 and both rain phases. Lean 90%.
  - Counterfactual: SAT, which is an explicit wall from the rain into P1024. It would be verified column by column,
    extended upward by the black edge and downward by P1024, and checked for least period, before any claim.
- What it teaches either way: whether the conjecture is threatened at p = 1,024 by short walls into this one rigid
  corridor. It says nothing about long walls or other phases.

**T33 results, first run** ([`rain_to_phase.py`](../tests/probes/rain_to_phase.py)).
- **Controls at p = 16, agreeing exactly with the complete core.**
  - Reversed (G16 above, rain below): SAT at D = 9, a wall from G16 into the rain, as the core says.
  - Forward (rain above, G16 below): UNSAT in all 80 instances (D = 1 … 40, both rain phases).
- **P33a HELD.** Rain above, P1024 below: UNSAT in all 78 instances (D = 2 … 40, both rain phases), each in at most
  2 s; 26 s under `run_capped`.
- **Monotonicity (PROOF, short).** A wall of D transition columns with rain state (a, ā) on top gives one of D + 1
  columns with (ā, a) on top, by adding the rain column ā above (Δā = all ones = ā ∨ a). The same padding works at the
  bottom with the phase. So, over both rain phases, existence is monotone in D, and UNSAT at D excludes every wall of
  length ≤ D.

**Predictions for the second run, written before it.**
- **P33b.** Rain above, P1024 below: UNSAT at D = 64, 128, 256, 512 and 1,024, both rain phases. Lean 85%.
- **P33c (the Sink conjecture for P1024).**
  - G8 (lifted to p = 1,024; all 8 of its time-rotations on top) above P1024: UNSAT at D = 64 and 256.
  - G16 (lifted; all 128 of its states on top) above P1024: UNSAT at D = 64.
  - Lean 80%.
  - Counterfactual: a wall from G8 or G16 into P1024. It would be the first wall seen between two non-rain phases,
    refuting the Sink conjecture, though not the light-speed recurrence conjecture.
- Caps: 600 s per instance, nice 10, `run_capped` with CPU 3,000 s and RSS 4 GiB.

**T33 results, second and third runs** ([output](../tests/probes/rain_to_phase.out)).
- **P33b NOT DECIDED.** Rain above, P1024 below, at D = 64: both rain phases timed out at 600 s. The owner chose to stop
  the run there and to put the source phases first, since longer D would also have timed out. Walls longer than 40
  are handed to the Intel host.
- **P33c HELD at D = 40** (the plan revised by the owner's choice; D = 64 and 256 not run). Walls into P1024 from all 8
  lifted G8 states and all 128 lifted G16 states are UNSAT, with no timeout, in 237 s. Padding with the source phase
  above makes this monotone too, so **no wall of length ≤ 40 leads into P1024 from G8 or G16.**
- **Certificates.** The two rain instances at D = 40 have CaDiCaL DRAT proofs (8.6 MB and 10.1 MB). `drat-trim` reports
  VERIFIED for both, in 0.6 s and 0.8 s. CNF SHA-256 prefixes are 47f4950ce4b2e29d and e27f6aad335bcf8c. The `cake_lpr`
  LRAT check is requested from GPT, on the Intel host where it is built.
- **Propagation.** At D = 10 Kissat refutes the rain-to-P1024 instance with no conflict and no decision: unit
  propagation from the two fixed ends alone. At D = 40 it needs about 20,000 conflicts. Part of the reason is
  elementary: from the defect, column periods at most double per column, so least period 1,024 needs at least 9
  doublings.

### 37.5 What T31–T33 teach

1. **The Sink conjecture is a property of each phase on its own.** "Every wall ends in the rain" holds iff every
   non-rain phase is upward rigid (§37.1). The light-speed recurrence conjecture follows from it together with "no
   excursion from the rain returns to the rain".
   - Upward rigidity has no reachability in it. It is checked phase by phase with local constraints.
   - G8, G16 and the 480-state phase are upward rigid, at depths up to 4, 31 and 67.
2. **P1024 is different.** It is a rigid corridor downward, with no exits at its own period. Upward it is loose: there
   are deviating histories at least 32 columns long, and their difference from the phase spreads by about 15 to 20
   bits per column.
   - Yet no wall of length ≤ 40 reaches it from the rain (DRAT-verified), from G8 or from G16.
   - So its long upward histories either die beyond depth 32, which makes it rigid at a larger depth, or come from
     somewhere not yet tested.
3. **The open questions are now sharp and finite at each length.** Is P1024 upward rigid, and at what depth? Is there
   any wall into it from the rain longer than 40? Both are Intel-scale SAT questions.
4. **A local question for a hand proof:** why do short walls from the rain fail by propagation alone? A hand version
   of that propagation would bound the wall length needed to reach any odd-weight rigid corridor.

## 38. Cloud's reading of the eternal-cycle line, a bridge to the episode line, and what a proof needs (CL676)

*Cloud, 2 November 2026, at the owner's request ("check in with Local and provide your analysis ... what is needed to
reach the proof intended"). Read: L1278–L1308, GC2351–GC2365, §§23–37 of this report, the inquisition of L1303, and the
T29 Intel report. Predictions for the two tests below were written first (Cloud's scratch, Blocks 16 and 17, copied in
§38.3 and §38.4). Probes `phase_family_sat.py` and `g16_episode.py` in `tests/probes/wolfram/`.*

### 38.1 The conjecture as I read it, and its standing

The light-speed recurrence conjecture (L1291): the only periodic points of the edge map Φ on Z_2 are the two phases of
black-edged rain. Equivalent forms the record has proved: ψ = Φ∘c has no finite orbit (§29.2, PROVED two-party);
at period p, no path from the defect state reaches a cycle of the pair graph H_p (§26.1, PROVED two-party); with the
kit's `PeriodicPoints`, every nonzero right-finite row that recurs exactly up to a shift is white or black-edged rain.

Standing: PROVED for every p dividing 128 (two independent implementations; GPT's third through 64); p = 256 has
560,082 of 560,085 subtrees complete and three giants open, so it is **not yet verified** (G26 applies: a run that stops
at a cap is not a verification). The tree is a critical two-type branching process whose only coin is |v ∨ w| mod 2
at type-0 nodes, fair to within 0.002, with the Galton–Watson tail constant 0.80 over eighteen binary orders (L1297,
L1298). Every phase (cycle of H_p) is a rigid rotator c^g = ρ^r (§35.1, PROOF). Known phases: the rain, G8, G16, the
480-state phase at p = 32, and P1024 (c = ρ^21 on 1,024 cells). G8, G16 and the 480-state phase are upward rigid
(T32), so no eternal point of period 8, 16 or 32 ends in them; P1024 is not upward rigid to D = 32, and no wall of
length ≤ 40 joins the rain to it at p = 1,024 (T33; both rain instances `cake_lpr` VERIFIED by GPT, GC2368; D = 64
unknown, with GC2369's thirty-minute Intel block running as I write). GC2368's caution that fixed-p rigidity need not
survive lifting is the same point as item 2 of §38.2 below.

Refuted on the way, and usefully: double-or-die (GPT's period-8 plateau); the valuation separator and the cycle lemma
(P1024, L1308); per-state orders (T21); bounded-window coins (T27, with GC2362's correction). These refutations
constrain the shape of any proof, which is the point of §38.5.

### 38.2 A bridge to the episode line (PROOF, hand, short; Cloud; read requested)

Take a phase E other than the rain, as a two-sided configuration in the edge frame (depth j ∈ Z, time t ∈ Z/p), and
the episode length M_E(k) of CL672: the longest time, over every row of depth k + 1 behind a black edge and every
alignment of E, for which the pair of columns (k, k+1) agrees with E from time 0.

**Claim.** No eternal point of any period has deep tail E ⇔ M_E(k) < ∞ for every k.

- (⇒, contrapositive) If M_E(k) = ∞ for some k, some prefix of depth k + 1 behind the black edge keeps its pair
  (k, k+1) equal to E's for ever. Every deeper cell, initialised to E, then stays E (it reads only the two cells above
  it, and E obeys the rule). The prefix [0, k+1] is autonomous (prefix autonomy), finite, hence eventually periodic in
  time, with a power-of-two period P because the finite edge map is triangular. From the first periodic time the whole
  row is periodic in the light frame with period lcm(P, p): an eternal point whose tail is E, and not the rain since
  E is not.
- (⇐, contrapositive) An eternal point with tail E beyond depth d gives, for every k ≥ d, a prefix (its first k + 2
  cells at any time) whose pair (k, k+1) agrees with E for ever: M_E(k) = ∞. ∎

**Consequences.**
1. For E = G8, which is PR69's ether (one black cell on a four-cell ring, period 8; CL672 reproduced PR69's law from
   it), the kit theorem `Rule30EtherEpisode` (R30-20261031-7c1f96, kit PR #71: M(k) = ⌊2k/3⌋ + 4 − [k ≡ 0, 2 mod 6]
   over all rows and alignments) says M_{G8}(k) < ∞ for every k. So **no eternal point of any period ends in G8**:
   PROVED, Lean, uniform in p. T32's rigidity of G8 and the p = 8, 16 cores are finite shadows of it. This is the first
   wall exclusion in the record that is uniform in the period.
2. The same method decides, for a given phase and a given wall depth, every period at once: M_E(k) for k ≤ K is one
   exhaustive computation (2^(k+1) prefixes, all alignments, horizon 3k + 3p + 24), where T32/T33 work at one period.
   It also covers eternal points whose wall has a longer period than the tail (period 2p with tail P1024, say), which
   the pair graph at p does not see, and where P1024 is no longer a rigid corridor (its columns have even weight at 2p).
3. The upper side of M_E, "every prefix's mismatch front reaches depth k by time f(k)", is exactly Proof 1's potential
   floor (L1258/L1263 for G8). So the uniform-in-p statement for a phase E is a front-potential theorem about E, of the
   kind the kit already holds for G8. CL674's negative result was about a non-phase background ((12, 68), period 68,
   where no eternal point can live by L1291's power-of-two lemma); for phases the front behaviour is a fresh question.

### 38.3 Test 1: the phase G16's episode law (Block 17; `g16_episode.py`)

Predictions, written first: P-F1 M_{G16}(k) finite at every k ≤ 14 (lean 90%; counterfactual, a prefix agreeing to the
horizon, to be run on and, if it never deviates, an eternal point with tail G16); P-F2 at most linear growth, slope in
[0.6, 1.6] on k = 6..14 (lean 60%); P-F3 the maximizers are not all pure inserted edges (lean 55%).

Result (COMPUTED, 128-cell ring with c = ρ^72, time period 16, all 2,048 alignments, horizon 3k + 72):

    k        : 1  2  3  4  5  6  7  8  9 10 11 12 13 14
    M_G16(k) : 8  8  9 11 12 13 13 16 17 19 19 21 21 22

All finite, far below the horizon (P-F1 HELD); slope 1.1 on k = 6..14 (P-F2 HELD); the maximizers at k = 4..7, 10, 12
and 13 are not inserted edges, at k = 1, 3, 8 and 9 all are (P-F3 HELD). So **no eternal point of any period ends in G16
with a wall of depth ≤ 14** (COMPUTED), and G16's law looks like the classic ether's (slope about 1, shields), not like
G8's (slope 2/3, no shield). The same computation is cheap for the 480-state phase (480 cells, period 32) and, with its
rotator symmetry collapsing the alignments to 1,024, for P1024 (horizon about 3,100); both are proposed below.

### 38.4 Test 2: is P1024 sporadic? Single-column phases by SAT (Block 16; `phase_family_sat.py`)

A single-column phase with odd twist is a ring y on N = 2^k cells with c(y) = ρ^r(y). T30/T31 enumerated the shift
registers for lags r ≤ 30 (forward) and ≤ 28 (backward) at every N. SAT tests every lag r < N at a fixed N: N variables,
7N clauses and a primitivity clause (y ≠ ρ^(N/2) y). Predictions: P-E1 further lags at N = 1,024 beyond 21 (lean 60%);
P-E2 a primitive solution with time period ≥ 16 at N = 2,048 (lean 65%); controls r = 72 at N = 128 (G16) and r = 21 at
N = 1,024.

Result (COMPUTED, CaDiCaL, conflict budgets stated; an undecided instance is neither SAT nor UNSAT):
At N = 64 no primitive solution; at N = 128 exactly one lag, r = 72, the phase G16 (control HELD). Beyond that the census
is **inconclusive**: at 300,000 conflicts per instance N = 256 did not finish its 255 lags in fifteen minutes; at 3,000
conflicts N = 256 decided 87 lags UNSAT with 168 undecided, N = 512 had 426 of 511 undecided, and at N = 1,024 the control
lag 21 itself was undecided (941 of 1,023 undecided), so that budget cannot find even the known phase. P-E1 and P-E2 are
NOT TESTED, not refuted. The lesson is about the tool: plain CDCL on these cyclic instances is far weaker than Local's
shift-register enumeration (2 s to lag 30) and than a structured (pos) query with (m, s) fixed; a census beyond lag 30
needs the register enumeration in C with bitsets (lags to about 40) or a SAT encoding with symmetry breaking.

### 38.5 What a proof needs: my perspective

1. **The quantifier is the whole difficulty.** At fixed p the conjecture is a finite statement, decided at cost about
   2^(0.16p) nodes (2^11, 2^17, 2^27, 2^41 at p = 32..256). Uniformity needs either an induction on p or a p-free
   invariant. The induction frame exists (T_{p/2} ⊂ T_p; the new content is the top layer, entered at anti-periodic roots
   of weight p/2; §28, §29.12), and inside the top layer the only unexplained event is the coin |v ∨ w| mod 2. A uniform
   rank would have to predict that coin along every path, and T27 (as corrected) shows the coin is a generic light-cone
   function deep in a layer; T21 and T28/T30 show no per-state or valuation rank exists. So the record's own refutations
   rule out every rank that is a function of a bounded window of the state. That is the Collatz shape named in L1294,
   and I would say it plainly: **no uniform proof by ranks is in sight**, and more separator candidates of the same
   kind will meet the same end. The heuristic that the conjecture is nevertheless true is strong (a critical tree is
   finite with probability one; a reachable cycle is a 2^(−Θ(p)) event), but a heuristic proves nothing.

2. **The phase-by-phase route is the one with proved pieces.** The Sink picture (§29.7) says the conjecture is "no
   wall from the edge into any phase". By §38.2 that is, per phase E, the episode statement M_E(k) < ∞ for all k, and
   for G8 it is already a Lean theorem. What is needed on this route: (a) for each phase, a front-potential theorem
   (Proof 1's kind) or at least the exhaustive M_E(k) to a depth that the wall's possible depth cannot exceed; (b) a
   handle on the *set* of phases: if phases are sporadic (G8, G16, the 480 phase, P1024 and nothing else to some large
   bound), the conjecture at every p whose phases are known reduces to finitely many episode theorems plus the
   classification; if they form infinite families, a family-wise episode theorem is needed. The classification of
   phases is a question about ring gliders of Rule 30 (rings y with c^g(y) = ρ^r(y)), a finite-ring object with no
   edge, which SAT and the shift-register census can map and which the kit's finite-ring machinery might reach. I think
   this is the most productive next question, because every answer is usable: a new phase is a new target with a cheap
   test, and a proved scarcity is half the theorem.

3. **What cannot be skipped.** p = 256 is not done until the three giants finish or the question is re-scoped; the
   record should say COMPUTED to p = 128 only. Solver-reported UNSAT answers (T29, T32) are not certificates;
   T33's two D = 40 rain instances now are (GC2368), and T32's rigidity of the 480 phase wants the same treatment, as
   TOOLS.md says. And eternal points with tail P1024 at periods 2,048 and beyond are outside T33's
   encoding; the episode test covers them for small wall depths.

4. **A realistic deliverable now.** The line already holds a coherent package of understanding: the reduction to the
   pair graph and to ψ (PROVED two-party); power-of-two periods (PROVED); the rotator form of phases (PROOF, Local);
   the episode bridge and the uniform G8 exclusion (this section, read wanted); the exact cores at p = 8, 16; the
   conjecture verified to p = 128 with the critical-branching structure measured; the catalogue of phases. That is a
   submission-grade statement of what light-speed recurrence in Rule 30 looks like, with the conjecture clearly
   labelled, and it is not on the board's prize path (none of Problems 1 to 3 follows from it or implies it, as far as
   I can see; L1283/L1284's non-periodic ancestry history was proved without it). The owner decides whether to spend
   the next days on the proof or to record the package and move on; my recommendation is to run the three cheap tests
   (480-phase and P1024 episodes, the phase census at N ≤ 4,096), then decide.

5. **Questions for Local and GPT.** Q1 Read §38.2 (both directions, the autonomy and power-of-two steps). Q2 Does
   Local's `ether_front_potential_certificate.py` method run on G16's 128-cell ring (a 16 × 128 phase table) and does a
   floor emerge? A machine floor for G16 would be the second uniform wall exclusion. Q3 For P1024, which of M_P1024(k)
   for k ≤ 8 and the p = 2,048 pair graph is the right next test? Q4 Is any phase other than a rotator of c or c²
   known, i.e. g ≥ 3 with no smaller g?

## 39. The front-potential method on G16 (T34, L1311)

At the owner's direction ("update, then continue with your warmest pulls"); Cloud's Q2 of CL676.

### 39.1 The method, transferred from the kit's ether proof (Local)

- **The mismatch.** Let E be a phase written two-sided in the edge frame (depth n ∈ Z, time t), and X a black-edge
  configuration. The mismatch D = X ⊕ E obeys
  D_n(t+1) = D_n(t) ⊕ [((E_(n−1) ⊕ D_(n−1)) ∨ (E_(n−2) ⊕ D_(n−2))) ⊕ (E_(n−1) ∨ E_(n−2))].
  - With background bits (E_(n−1), E_(n−2)) = (0,0), (1,0), (0,1), (1,1), the update F is a ∨ b, a ∧ ¬b, ¬a ∧ b or
    a ∧ b, with F(0,0) = 0. This is the kit's `D_step`, with E's own table in place of the ether's.
- **The front.** Let R(t) be the deepest mismatch. Below it D = 0, and the cells there stay clean until R reaches them.
  The next front is R + 2 if F_(R+2)(0, 1) = 1; else R + 1 if F_(R+1)(1, D_(R−1)) = 1; else R if
  D_R ⊕ F_R(D_(R−1), D_(R−2)) = 1; else a retreat. So a step depends on E's background at R … R + 2 and on the
  mismatch just above the front.
- **The consequence.** If R(t) ≥ v·t − C for every black-edge configuration, with v > 0, then M_E(k) < ∞ for every k,
  and by the bridge (§38.2) no eternal point of any period ends in E. For the ether, the kit proves this with
  v = 3/2 (potential 2R + g2(ψ) − 3t, no retreat after time 1).

### 39.2 Predictions, written before the run (T34)

**Part 1, exact fronts** (`front_g16.py`). Random black-edge prefixes of depth K = 40 have the clean G16 tail below,
over random alignments among G16's 2,048 (128 depths × 16 times). The row is evolved by Φ for 300 ticks, tracking
R(t), the retreats, and the longest stall (ticks without a new maximum of R).
- **P34a.** The front's mean speed is between 0.8 and 1.2 cells per tick, matching Cloud's slope of about 1.1 for
  M_G16. Lean 65%.
- **P34b.** Retreats occur after time 1, unlike the ether. Lean 60%.

**Part 2, a sound certificate.** The state is the front's class in G16's torus (R mod 128, t mod 16) together with a
window of w mismatch bits above the front. Bits beyond the window are treated as free (a nondeterministic
over-approximation), and a retreat out of the window counts as a failure. If no cycle of this finite automaton has
total advance ≤ 0, the front advances at a positive minimum mean speed for every configuration, which proves
M_G16(k) < ∞ for all k, uniformly in the period.
- **P34c.** A certificate exists for some w ≤ 10. Lean 35%: G16 is richer than the ether, and retreats may need an
  unbounded window.
- **Counterfactual.** A non-positive cycle for every w ≤ 10. Its exact replay would show either a real stall (a long
  episode) or an over-approximation artefact. Either answer is informative.

### 39.3 T34 results ([`front_g16.py`](../tests/probes/front_g16.py), [`front_cert.py`](../tests/probes/front_cert.py), [output](../tests/probes/front_cert.out))

- **P34a HELD.** Exact fronts against G16 (400 runs, K = 40, 300 ticks): R(T)/T is 1.06 to 1.39 (median 1.24). Net of the
  starting depth of about 37, that is 0.9 to 1.2 cells per tick, matching Cloud's slope of about 1.1 for M_G16.
- **P34b HELD.** Every run retreats after time 1 (7,526 retreats in 400 runs). The longest stall is 18 ticks. In a
  further 600 runs of 400 ticks, the largest single-step retreat is **8 cells**, also after tick 20.
- **Control: G8 is certified.**
  - At window 5 there is no FAIL edge, and every 7-tick path of the over-approximation advances.
  - This reproves the kit's ether theorem by an independent finite method: no eternal point of any period ends in G8.
    Known, reproved here.
- **P34c REFUTED, for a structural reason.**
  - FAIL edges remain at every window tried (224, 144 and 112 at W = 6, 8 and 10), as they must below W = 9 given real
    retreats of 8.
  - Even the non-FAIL part does not certify. Its least advance over length-k paths falls linearly, and **identically
    for W = 8, 9 and 10** (−54, −83, −140, −254 and −368 at k = 25, 50, 100, 200 and 300): a steady retreat of 1.14 cells
    per tick that does not depend on the window.

### 39.4 What T34 teaches

1. **The kit's front-potential method becomes a finite certificate for any phase.** For G8 it works at window 5,
   reproving the kit independently.
2. **For G16 a local window cannot work.**
   - The over-approximation lets bits above the window be chosen freely, and with them the front can retreat at a
     steady 1.14 cells per tick, however wide the window. That is the signature of a pattern above the front into
     which G16 would spread upward.
   - With a black edge on top the retreat is bounded, because the front cannot rise above the edge region. But the
     automaton tracks the front only modulo G16's period and cannot see that bound.
   - So **a uniform exclusion of G16 must use the black edge globally.** This is the same lesson as the orphan control
     of §2.2 and the boundary findings, met from the front side.
3. **The evidence that G16 is excluded stays strong, but computed rather than proved.**
   - Exact fronts advance at about 1 cell per tick, with stalls of at most 18 ticks.
   - Cloud's M_G16(k) is finite to k = 14.
   - G16 is upward rigid at its own period (T32).
4. **Next routes:**
   - (a) extract the steady-retreat cycle and test whether it is realised by a real pattern Q above G16, which would be
     a structure into which G16 spreads (curious in itself), or is an artefact of free bits;
   - (b) an edge-aware certificate that keeps the distance from the front to the edge, or a two-stage argument (the
     edge's mismatch emission, then the front);
   - (c) Cloud's episode laws for the 480-state phase and P1024, which are computations, not proofs.

## 40. Does G16 eat a prepared pattern? Drawdown of the mismatch front (T35, L1312)

At the owner's choice ("Test the pattern"), following §39.4 (a).

### 40.1 The top of a mismatch region is pinned (PROOF, Local; short)

- Rule 30 is left-permutive, so in absolute coordinates the rightmost cell where two rows differ moves right at
  exactly light speed. In the edge frame, **the shallowest mismatch keeps its depth for ever**: at that depth
  D(t+1) = 1 ⊕ F(0, 0) = 1, and above it D(t+1) = F(0, 0) = 0.
- So for two configurations that differ on a finite range of depths, the mismatch is supported on [top, R(t)] with
  the top fixed, and the front can never retreat above the top.
- The window automaton of §39 forgets the top. That is why it allowed an endless steady retreat. **An endless retreat
  is impossible in reality**, with or without a black edge; under a black edge the front also stays at depth −1 or
  below, since the edge region always mismatches G16.
- The real question is therefore finite-time: how far can a front retreat from a prepared mismatch region? Is the
  **drawdown**, max_(s ≤ t) R(s) − R(t), bounded uniformly, or does it grow with the width r of the region?

### 40.2 Predictions, written before the run (T35)

`drawdown.py`: no edge. E is G16, two-sided, at each of its 128 alignment classes; the classes are the cosets of
⟨(8, 7), (0, 16)⟩ in (depth, time), from the twist "depth shift 8 = time shift 7". The initial mismatch D(0) is
supported on depths 0 … r − 1 with both ends 1, over all 2^(r−2) interiors, for r = 6, 10, 14 and 18. Evolve
D(t+1) = D ⊕ F(D) exactly for 3r + 30 ticks, and record the largest drawdown. The same is done for G8 (8 classes) as a
control.
- **P35a.** For G16 the largest drawdown grows with r, roughly like r: G16 can eat a prepared region back towards its
  top. Lean 55%.
  - Counterfactual: the drawdown saturates near the 8 seen in random runs. Retreats would then be uniformly bounded,
    and a certificate would need only bounded drawdown plus "no indefinite hover".
- **P35b (control).** For G8 the drawdown stays small for every r (≤ 2), since the kit proves no retreat after time 1.
  Lean 80%.

### 40.3 T35 results ([`drawdown.py`](../tests/probes/drawdown.py), [output](../tests/probes/drawdown.out); 2 minutes in all)

- **P35a HELD: G16 eats prepared patterns.** Over all interiors and all 128 alignment classes, the largest drawdown is
  **11, 14, 19 and 22** for r = 6, 10, 14 and 18, about r + 4 to 5.
  - At r = 14 the extreme front comes all the way back to the pinned top: G16 absorbs the whole prepared region.
- **P35b REFUTED in its number, held in spirit.** For G8 the largest drawdown is **5 at every r** from 6 to 18:
  bounded, though above the predicted 2. Bounded retreat is why a local certificate works for G8 (T34).

### 40.4 What T35 teaches

1. **The window automaton's retreat is real for a finite time, impossible for ever.**
   - Prepared mismatch regions let G16 retreat by about their own width.
   - The pinned top (§40.1) forbids an endless retreat.
   - So the obstruction of §39 is half in the mathematics (finite retreats as long as the preparation) and half in the
     automaton (the endless version).
2. **The difference between G8 and G16 is a fuel law.**
   - G8: drawdown bounded by 5, independent of the preparation, and the kit proof uses exactly that.
   - G16: drawdown grows like the width of the prepared region, which is linear fuel.
   - This fits Cloud's M_G16(k) ≈ k + 7: a prefix of depth k can pay for about k ticks of hovering.
3. **What a uniform exclusion of G16 now needs.**
   - **(i) A fuel bound:** from any finite mismatch region of width r, drawdown ≤ r + C (C = 5 at r ≤ 18).
   - **(ii) No fuel from the edge:** the mismatch the black edge keeps emitting carries no stored retreat, so once the
     prefix's fuel is spent the front advances on average.
   - Both are statements a potential could carry: the kit's front potential, plus a fuel term charged to the mismatch
     region above the front.
   - (i) can be tested further at larger r by SAT. (ii) is the global ingredient that §39 and the orphan control both
     pointed to.

## 41. Does the black edge supply fuel? (T36, L1313)

At the owner's go-ahead ("Yes, go on"), step (ii) of §40.4.

### 41.1 Setting and predictions, written before the run

A black-edge row has white above depth −1, black at −1, and the digits below. Against G16 the mismatch above the edge
never ends, so there is no pinned top. The edge region keeps sending mismatch down towards the front. The question
is whether that stream carries retreat fuel, or whether all the fuel comes from the prepared prefix.

`edge_fuel.py`:
- **(a) Clean starts:** the prefix equals G16's own digits, so at time 0 the only mismatch is the edge region. All 128
  alignment classes run for 20,000 ticks, recording speed, largest drawdown and longest stall.
- **(b) Prepared prefixes:** random digits at depths 0 … K − 1 above the clean G16 tail, for K = 20, 40, 80 and 160 (300
  random prefixes each, random alignments), run for 8K + 200 ticks. The drawdown is split into early (before the front
  first passes depth 2K) and late (after).

Predictions:
- **P36a.** Clean starts at all 128 alignments advance at speed ≥ 0.8 over 20,000 ticks, with largest drawdown ≤ 10.
  Lean 75%.
- **P36b.** With prepared prefixes, the early drawdown grows with K, but the late drawdown stays ≤ 12 whatever K is.
  Lean 55%.
  - Counterfactual: a late drawdown that grows with K. The evolved prefix would then keep its fuel after the front has
    passed, and a fuel account would have to follow the region above the front over time.
- **What it teaches.** If P36a and P36b hold, the target is an **edge lemma for G16**: after a time proportional to the
  prefix depth, every black-edge front has bounded drawdown. That lemma, with a stall bound, gives the exclusion of
  G16 at every period.

**Results of (a) and (b)** ([`edge_fuel.py`](../tests/probes/edge_fuel.py), [output](../tests/probes/edge_fuel.out); 56 s).
- **P36a HELD.** Clean starts at all 128 alignment classes over 20,000 ticks have speed 1.191 to 1.223, a strikingly
  uniform value. The largest drawdown is 10 and the longest stall 18.
- **P36b half held.**
  - The late drawdown stays at 11, 14, 13 and 13 for K = 20, 40, 80 and 160, so bounded and independent of K.
  - The early drawdown does not grow with K (20, 7, 7, 13): random prefixes carry almost no fuel, and T35's long
    retreats need prepared regions. "Early drawdown grows with K" is REFUTED for random prefixes.
  - All 1,200 runs passed depth 2K. The slowest run averaged 0.98 cells per tick.

**P36c, written before the exhaustive run.** Under the black edge, take all 2^K prefixes for K = 8, 12 and 16 at all 128
alignment classes, for 6K + 60 ticks (`edge_fuel_exhaustive.py`).
- The largest total drawdown is ≤ K + 10, the fuel bound under the edge.
- The largest late drawdown (after the front first passes depth 2K) is ≤ 14, the same as for random prefixes.
- Lean 60%.
- Counterfactual: a late drawdown that grows with K. Prepared prefixes would then keep fuel after the front passes,
  and the edge lemma would need a dynamic fuel account.

**Results of (c)** ([`edge_fuel_exhaustive.py`](../tests/probes/edge_fuel_exhaustive.py), [output](../tests/probes/edge_fuel_exhaustive.out); 4.7 minutes at nice 10).
- **P36c half held.**
  - The fuel bound held: the largest total drawdown over all prefixes is **K + 6, K + 5 and K + 3** for K = 8, 12 and 16.
  - The late-drawdown bound of ≤ 14 is REFUTED in its number: **14, 17 and 17**. It does not grow from K = 12 to 16.
- Every one of the 2^K prefixes at every alignment reaches depth 2K, and the slowest R(T)/T is 0.76 to 0.82.

### 41.2 What T36 teaches

1. **The edge alone drives the front at a definite speed.** From a clean start, all 128 alignments advance at 1.19 to
   1.22 cells per tick over 20,000 ticks, with drawdown ≤ 10. The edge's mismatch stream behaves like a steady
   source, not a store of fuel.
2. **Fuel lives in the prefix and is bounded by its width.**
   - Random prefixes carry almost none.
   - The worst prefix of depth K pays for a retreat of at most K + 6 (K ≤ 16).
   - After the front has passed depth 2K, drawdown stays at most 17 at K = 12 and 16.
3. **So an edge lemma for G16 is now a precise, well-supported conjecture.**
   - Every black-edge front against G16 has total drawdown ≤ K + C.
   - After a time proportional to K, its drawdown is ≤ C′, and it advances at speed ≥ v > 0.
   - Evidence: exhaustive for K ≤ 16, sampled for K ≤ 160, and 20,000 ticks from clean starts.
   - With Cloud's bridge, that lemma excludes G16 at every period. No proof is in hand. A potential would need a fuel
     term charged to the region between the edge and the front, and that region grows.
4. **What this route has given.** The phase-by-phase programme now has:
   - one Lean theorem (G8, the kit's);
   - an independent finite certificate for G8;
   - a mechanism and strong evidence for G16, with the exact reason a local certificate fails (prepared fuel, the
     pinned top) and the shape of the global lemma that would succeed.

## 42. Which phases can be excluded at every period? Wake type and front certificates (T37, L1314)

At the owner's direction ("the proof is the target ... continue with your warm pulls, whilst considering the broader
structural questions Cloud is working on").

### 42.1 Connection to Cloud's speed law (M2, CL678), and the proposal

- Depth speed in the edge frame equals 1 + the lab leftward news speed of the leftmost mismatch.
  - Cloud's G16 value of 0.224 corresponds to my clean-start depth speed of 1.19 to 1.22 (T36).
  - G8's exact 1/2 corresponds to the kit's 3/2 (potential 2R − 3t).
  - The classic ether's exact 0 is a depth speed of exactly 1.
- Cloud's dichotomy (CL674, CL678): a periodic wake has a rational speed with an exact law; an odometer wake has no
  law.
- **Proposal (CONJECTURE, Local):** a finite front certificate (§39, with GC2374's correction) exists for a phase
  exactly when its black-edge wake is periodic.
  - G8 is periodic and certified at window 5. G16 is an odometer wake: its drawdown grows with preparation (T35), and
    no certificate exists at W ≤ 10.
  - If this holds, the phase-by-phase route proves exclusions for periodic-wake phases and meets the Collatz shape for
    odometer-wake phases. The wake dichotomy would be the boundary of what can be proved.
- **Test on the other known phases**, the 480-state phase (p = 32) and P1024 (p = 1,024). Neither is excluded at
  every period by any method so far. A certificate for either would be a new theorem, uniform in the period.

### 42.2 Predictions, written before the run (T37)

- **(a) Wake type** (`wake_type.py`). Clean starts: each phase directly below the edge, run for 4,000 ticks over
  alignments (all 30 × 32 for the 480-state phase, 64 values of θ for P1024). Measure speed, drawdown, and whether the
  window of 256 mismatch cells above the front recurs with a shift (a periodic wake).
- **(b) Certificates** (`front_cert.py`). Fixed so that CERTIFIED requires no FAIL edge (GC2374). Run it on the
  480-state phase (classes (n mod 480, t mod 32), W ≤ 6) and on P1024 (classes θ = t + 195n mod 1024, W ≤ 8).
- **P37a.** Both wakes are odometer-like (no periodic recurrence of the front window), with speeds strictly between 1
  and 1.5. Lean 65%. Both phases are richer than G8.
- **P37b.** Neither phase is certified at these windows. Lean 70%.
- **Counterfactual.** A periodic wake, or a certificate, for either phase. A certificate proves that no eternal point
  of any period ends in that phase. For P1024 that would be the first exclusion of it by any method.

### 42.3 T37 results ([`wake_type.py`](../tests/probes/wake_type.py), [output](../tests/probes/wake_type.out); [`front_cert.py`](../tests/probes/front_cert.py), [output](../tests/probes/front_cert_t37.out))

- **P37a REFUTED: three of the four known non-rain phases have periodic wakes.** From clean starts, 32 alignments
  each, 4,000 ticks:

  | phase | wake | speed (depth per tick) | largest drawdown |
  |---|---|---|---|
  | G8 (control) | periodic: period 64, advance 96 | exactly 3/2 | 0 |
  | G16 | no recurrence at any alignment (odometer) | 1.06 to 1.22 | 10 |
  | 480-state phase | periodic at every alignment: period 288, advance 480 | exactly **5/3** | 5 |
  | P1024 | periodic at every alignment: period 208, advance 272 | exactly **17/13** | 4 |

  Recurrence is tested on the 256 mismatch bits above the front together with the front's class. It is a heuristic
  for a periodic wake, but it is convincing at every alignment with one common (period, advance).
- **P37b HELD.** Neither phase is certified by the window automaton.
  - P1024 at W = 4, 6, 8: FAIL edges 165, 122, 85; at W = 8 the non-FAIL part retreats about 1.8 cells per tick.
  - The 480-state phase at W = 4, 5: FAIL edges 2,496 and 2,240; at W = 5 it retreats about 2.2 cells per tick.
  - Given the periodic wakes, these failures are more likely the over-approximation's coarseness (long wake periods
    need wide windows) than the dynamics.

### 42.4 What T37 teaches

1. **Cloud's wake dichotomy splits the known phases 3 to 1:**
   - periodic wakes with rational speeds, G8 3/2, the 480-state phase 5/3 and P1024 17/13 (lab news speeds 1/2, 2/3 and
     4/13);
   - an odometer wake, G16.
2. **Under the proposal of §42.1,** G8, the 480-state phase and P1024 belong to the class where a front-potential
   exclusion at every period should exist. G16 alone is in the Collatz-shaped class.
   - The kit proves G8. For the other two, the missing piece is a certificate fine enough for their long wakes.
   - The decisive test is whether prepared regions can fuel long retreats (T35 style). If the drawdown stays bounded,
     as for G8, a certificate at a moderate window should exist.
3. A rational speed of 17/13 for P1024's wake, with period 208 = 16 · 13, is curious in itself: the wake period
   carries the factor 13.

## 43. Fuel in the periodic-wake phases (T38, L1315)

### 43.1 Predictions, written before the run

`drawdown.py`, extended:
- the 480-state phase over all 960 alignment classes, the cosets of ⟨(30, 14), (0, 32)⟩;
- P1024 over its classes θ = t + 195n mod 1024 (all 1,024 for r ≤ 10, 256 sampled for r = 14).

The prepared mismatch regions of width r = 6, 10 and 14 are all enumerated, with no edge, exactly as in T35.
- **P38a.** For both phases the largest drawdown stays bounded (≤ 8) for every r: no fuel, as for G8 (5 at every r).
  Lean 60%.
- **Counterfactual.** A drawdown that grows like r, as for G16. A periodic wake from clean starts would then not imply
  freedom from fuel, and even periodic-wake phases would need a fuel term in their certificates. That would weaken the
  proposal of §42.1.

### 43.2 T38 results ([output](../tests/probes/drawdown_t38.out))

- **P38a REFUTED: both periodic-wake phases have fuel.**
  - The 480-state phase (all 960 classes): largest drawdown 12, 16 and 20 at r = 6, 10 and 14.
  - P1024 (all 1,024 classes at r ≤ 10, 256 sampled at r = 14): 11, 19 and 20; at r = 10 the front heals all the way
    back to the pinned top.
  - Like G16 (11, 14, 19, 22), unlike G8 (5 at every r).
- **So a periodic wake from a clean start does not mean freedom from fuel.** G8 is the only known phase without fuel,
  and a local front certificate needs exactly that. The proposal of §42.1 fails in its strong form: a periodic wake is
  not sufficient for a local certificate.
- *Correction (GC2384, L1317).* Three growing maxima refute the numerical bound ≤ 8; they do not prove that the
  drawdown is unbounded, nor that no window certificate of any kind exists. G8's all-period exclusion comes from the
  kit's certificate, not from the measured 5. §44.6 later gives a window certificate of a different kind, for fronts
  that already look clean.

**T39, predictions written before the run (`wake_attractor.py`).** For P1024, 200 random prefixes at each of K = 40
and 80 run at random θ for 6K + 2,000 ticks. After the front passes depth 3K, is the window above the front eventually
periodic with the clean-start wake's period and advance (208, 272), at speed exactly 17/13?
- **P39a.** Every run converges to the clean-start wake: the clean-start wake is a global attractor. Lean 55%.
- **What it teaches.** If P39a holds, a two-stage proof shape appears for P1024: the prefix's fuel is spent, then the
  front is captured by a periodic wake whose advance is a finite fact. If it fails (other periods, other speeds, or no
  recurrence), even periodic-wake phases have several or chaotic attractors.

### 43.3 T39 results, and the premise check (T40 part 1)

- **T39** ([`wake_attractor.py`](../tests/probes/wake_attractor.py), [output](../tests/probes/wake_attractor.out); P1024,
  200 random prefixes each at K = 40 and 80).
  - The late speed lies between 1.29 and 1.31 in every run, around 17/13 = 1.3077.
  - An exact recurrence of the clean-start wake (208, 272) appears in only 25 and 58 runs within the horizon, plus one
    at the half period (104, 136), which has the same speed. The rest show no recurrence within 2,240 or 2,480 ticks.
  - **P39a REFUTED for exact capture, held for the speed.**
  - *Correction (GC2384, L1317).* The half-period recurrence (104, 136) appeared once at each K, so twice in all, not
    once. Non-capture within 2,240 or 2,480 ticks is horizon-limited; it does not refute eventual capture, which §44.4
    then found in all 400 runs under a strict test.
- **Premise check** ([`wake_background.py`](../tests/probes/wake_background.py)). For G8, P1024 and the 480-state phase,
  the middle of the clean-start wake satisfies neither the moving-frame recurrence nor any depth period.
  - So the "periodic wake" of T37 is periodicity of the neighbourhood of the front, not a periodic background filling
    the wake.
  - The architecture's premise has to be stated as **decoupling**: no information from behind reaches the front.

### 43.4 T40, decoupling: predictions written before the run (`wake_decouple.py`)

Clean starts for G8, G16, the 480-state phase and P1024. At tick 600, flip 1 to 4 random bits at a distance d ∈ {50, 100,
200} behind the front (30 trials per d). Track the difference between the perturbed and unperturbed runs to tick 2,600:
its deepest point, and whether it reaches the front.
- **P40a.** For G8, P1024 and the 480-state phase, no perturbation reaches the front: the gap between the difference's
  deepest point and the front grows linearly. Lean 60%.
- **P40b.** For G16 some perturbations reach the front. Lean 60%: its front speed of 1.22 is below a typical damage
  depth speed of about 1.25.
- **What it teaches.** If P40a holds, the front of a periodic-wake phase depends only on a bounded window around it,
  so it is a finite object, and its advance under arbitrary perturbations becomes a finite question.

### 43.5 T40 results ([`wake_decouple.py`](../tests/probes/wake_decouple.py), [output](../tests/probes/wake_decouple.out))

| phase | front speed | perturbations reaching the front (of 90) | deepest-difference speed |
|---|---|---|---|
| G8 | 3/2 | 0 | at most 1.49, so it falls behind |
| G16 | 1.09 in this run | **85** (overtaking the front) | up to 1.23 |
| 480-state phase | 5/3 | 0 | up to **1.667**, riding at the front's speed (smallest final gap 45 from d = 50) |
| P1024 | 17/13 | 0 | up to **1.31**, riding at the front's speed (gaps 50 and 95 from d = 50 and 100) |

- **P40b HELD.** G16's front is not decoupled from its wake.
- **P40a: main claim held, detail refuted.** No perturbation reaches the front in the three periodic-wake phases. But
  for the 480-state phase and P1024, a perturbation close behind the front travels at exactly the front's speed and
  keeps its distance. Only those starting about 200 cells back fall behind.
- *Correction (GC2384, L1317).* The 1 to 4 flips were sampled with replacement, so some perturbations may have been
  null; a zero reported speed can be one. §44.4's census uses single flips at distinct gaps, and pairs at distinct gaps.

### 43.6 What T37–T40 teach: a proof architecture, and where it stands

1. **Front structures.**
   - **G8:** decoupled, fuel-free, and certified locally (the kit's theorem).
   - **The 480-state phase and P1024:** a comoving periodic boundary layer behind the front, about 100 to 250 cells
     deep; neutral modes inside it (perturbations ride along); decoupling beyond it; and fuel from prepared prefixes
     (T38).
   - **G16:** no boundary layer and no decoupling (an odometer wake).
2. **The architecture for the 480-state phase and P1024 (PROOF-SKETCH outline; read requested).**
   - (a) Decoupling: information more than L cells behind the front never reaches it.
   - (b) So the front and its layer form a closed finite dynamics on windows of width L.
   - (c) Every reachable window of that dynamics advances (no zero-advance cycle).
   - Then any black-edge row, once its prefix's fuel has passed into the decoupled wake, has a front driven by (b),
     which advances by (c). Hence M_E(k) < ∞ for every k, and by the bridge no eternal point of any period ends in E.
3. **The gaps, stated honestly.**
   - (a) is measured (90 trials each), not proved.
   - The layer width L of about 100 to 250 makes (b) and (c) far too large to check exhaustively without structure.
   - "Once the fuel has passed" needs the fuel to be finite and to leave the front, which T38's healing-to-the-top
     events make delicate.
   - Neutral modes inside the layer mean (b) has non-trivial invariant subsets, which (c) must also cover.
4. **G16 needs a different idea.** Its front is driven by the whole wake: the Collatz-shaped case of Cloud's dichotomy,
   now seen as "no decoupling".


## 44. The boundary layer: decoupling gap, riding particles and linearity (T41, L1316)

### 44.1 The algebra behind the test

The edge map is quadratic: F(x)_n = x_n ⊕ x_(n−1) ⊕ x_(n−2) ⊕ x_(n−1)x_(n−2). A disturbance δ of a base run X therefore
evolves by

δ_n(t+1) = δ_n ⊕ δ_(n−1)·¬X_(n−2) ⊕ δ_(n−2)·¬X_(n−1) ⊕ δ_(n−1)δ_(n−2),

a linear part with coefficients read from the base run (the tangent map), plus one quadratic term. Two consequences:
- **The deepest disturbed cell m obeys the mask lemma** (Cloud's P-K2, CL679): δ_(m+2)(t+1) = ¬X_(m+1)(t), so m
  advances by 2 exactly when the base cell ahead is white. The main front R is the same kind of object: it is the
  deepest cell of the disturbance D = X ⊕ E of the phase E, so R advances by 2 exactly when E_(R+1) = 0.
- **Two disturbances superpose exactly until their supports touch.** The second derivative of F is
  a_(n−1)b_(n−2) ⊕ a_(n−2)b_(n−1), so the interaction I = Δ_AB ⊕ Δ_A ⊕ Δ_B of two flips A and B is born only where
  the two responses are adjacent. This is G12.2's four-case test (the ab coefficient), applied to the layer.
- A disturbance changes the main front exactly when its deepest cell reaches the front (m ≥ R); before that,
  X ⊕ δ ⊕ E has the same deepest 1 as D.

So the questions of §43.6 become questions about damage fronts racing a front: (a) asks which disturbances never
catch R, and the "linear layer" asks whether the interaction of two riding disturbances is itself left behind.

### 44.2 Predictions, written before the run (`layer_linear.py`)

P1024 (wake period 208, advance 272) and the 480-state phase (288, 480), clean starts at one random alignment each.
Flips are made at eight comoving phases t0 = 5·period + j·period/8 (j = 0..7), at every gap g = 1..400 behind the front.
Each run lasts ten wake periods after the flip.
- **P41a (decoupling reaches down to a small gap).** For both phases, the gaps whose single flip ever changes the main
  front form a short initial set, all g ≤ 6; every flip at g ≥ 7 rides or falls behind. Lean 50%.
  - Counterfactual: flips at gaps of 20 to 200 sometimes change the front. Then the layer drives the front, the riding
    of T40 was sampling luck, and (a)'s L is the layer depth.
- **P41b (riding disturbances are a finite catalogue of particles).** Every flip still within 400 of the front at the
  end has an eventually periodic deep end. In the comoving frame, (the gap R − m, the 64 disturbance bits above m)
  recurs after one or two wake periods. At most 12 distinct riding gaps occur per phase. Lean 50%.
  - Counterfactual: deep ends that drift slowly, or aperiodic deep-end patterns; then "neutral modes" are not particles
    and (b) has no finite catalogue.
- **P41c (the layer is linear where it matters).** For 200 random pairs of riding flips (j = 0), the pair's run never
  changes the front. The interaction I is either zero or has its deepest cell at least as far behind the front as the
  deeper of the two single responses. Lean 45%.
  - Counterfactual: a pair of individually harmless flips changes the front, or its interaction rides closer to the
    front than either flip. The layer is then nonlinear exactly where (b) and (c) need it linear.
- **P41d (the tangent map is not enough).** For single flips, the purely linear tangent evolution (the quadratic term
  dropped) puts its deepest cell at a different place from the true disturbance within one wake period, for most
  gaps. Lean 75%. By §44.1, the two deep-end rules differ whenever δ_(m−1) = 1 and the cell ahead is black.
- **P41e (T39's missing captures are riding particles).** Rerun T39 (`wake_attractor.py`, the same 200 prefixes at
  K = 40 and 80) with the recurrence window cut from 256 cells to 32. Then at least 190 of 200 runs per K show the
  clean-start recurrence (208, 272), or a multiple of it. Lean 65%.
  - Counterfactual: still well under half. Then the front itself has other near-front orbits, and the two-stage shape
    (fuel, then capture) fails near the front, not only in the layer.

**What it would teach.** If P41a, P41c and P41e hold, then:
- the front's future is a function of a window of a few cells, the phase ahead, and the fuel still unspent;
- the layer's particles are bystanders;
- (b) and (c) shrink from windows of width 100 to 250 to a small window plus the fuel question.

If P41a fails, the layer is genuinely coupled, and the linear-algebra route (P41c) becomes the main hope.
Record searched: record and kit term by term (superposition, damage front, boundary layer, neutral, linearis): G12.2
(the four-case superposition test, at a hole), GC505 and Cloud's CL679 (damage-front bias and the mask lemma); no kit,
portal or open-PR hit for a boundary layer or a front-decoupling theorem (kit main @c42f6e51).

### 44.3 Part 2, predictions written before the run (`front_closure.py`)

The census (§44.4) found the clean fronts immune to single flips beyond a few cells. A sound version of that statement
can be checked finitely. Take the window automaton of §39, which branches over everything deeper than W behind the
front. Explore only its forward closure from the clean front's own states (front class, window) at ticks 600 to
600 + 4 wake periods. A FAIL-free closure in which every k-path advances proves: **any row whose front ever shows a
clean-front state advances for ever, whatever lies behind the window** (a ROBUST verdict).
- **P41f.** ROBUST for the 480-state phase at some W ≤ 16 (lean 45%), and for P1024 at some W ≤ 24 (lean 35%).
- **Control.** G8 is ROBUST at W = 5, where its whole automaton is certified (§39).
- **Counterfactual.** FAIL edges in the closure at every W tried. Then arbitrary content behind the window can pull
  the clean front back, and its measured immunity rests on the actual structure of the wake (the band of §44.4), not
  on the window alone. The proof would then need that band, which is Cloud's banding object in a new frame.

### 44.4 Results, part 1 ([`layer_linear.py`](../tests/probes/layer_linear.py), [output](../tests/probes/layer_linear.out); [`wake_attractor.py`](../tests/probes/wake_attractor.py) `--win=32`, [output](../tests/probes/wake_attractor_win32.out))

**Unexpected first: the wake behind P1024's front is a period-doubling band (COMPUTED).** This was found in the smoke
test, after the predictions. It is the least period of the W-cell window above the clean front:

| window W | P1024 (ticks, advance) | 480-state phase |
|---|---|---|
| 32 | (52, 68) from tick 400 | (288, 480) from tick 400 |
| 64 | (104, 136) from tick 400 | (288, 480) |
| 128 | (208, 272) from tick 800 | (288, 480) from tick 800 |
| 192 | (416, 544) from tick 1,600 | (288, 480) from tick 800 |
| 256 | (416, 544) from tick 2,400 | (288, 480) from tick 800 |
| 320 | none by tick 2,400 | (288, 480) from tick 1,440 |

- Behind P1024's front the period doubles three times within 192 cells. The ordered region widens with time.
- The 480-state phase keeps the one period 288 over a band that also widens with time.
- So T37's "periodic wake" (208, 272) was the 128-to-256-cell reading of a cascade, and §43.3's aperiodic middle is the
  part of the band not yet ordered.
- This is the shape of Cloud's banding on the single seed's left side: an ordered band behind a moving boundary,
  with period doubling across diagonals (CL679/CL680, atlas §9). The comoving frame of a phase front may be a fourth
  frame of that object. This is a CONJECTURE: the integration-parity law of CL680 has not been tested here.

**The predictions:**
- **P41a: substance HELD, the literal bound REFUTED by one gap.**
  - 480-state phase: no single flip at any gap 1 to 400, at any of the eight comoving phases, ever changes the front.
    That is stronger than predicted.
  - P1024: flips change the front only at gaps ≤ 7. At even j only gap 1 does; at odd j, gaps 1, 2, 3, 4, 6 and 7.
    Gap 7 breaks the predicted g ≤ 6.
- **P41b: HELD for the 480-state phase, REFUTED as stated for P1024.**
  - 480-state phase: every riding flip comes from a gap ≤ 45, and all 29 end at exactly gap 45, at every j; the other
    371 fall behind. **One slot**: a disturbance closer than 45 cells drifts back to 45 cells behind the front and
    rides there; anything farther back falls away.
  - P1024: at most five riding gaps at each final tick (near 47–50, 58–64, 87–99 and 171–177); 17 over the eight final
    ticks, because those fall at different comoving phases.
  - P1024: 116 to 164 flips per j neither recur within two wake periods nor fall steadily behind. Most end at the
    171-to-199 slot, whose 64-bit deep end reaches into the band that is not yet periodic.
- **P41c: the front part HELD, the linearity part REFUTED.**
  - No pair of riding flips (200 per phase) ever changes the front.
  - The interaction I is non-zero at the end in all 400 pairs. In 32 pairs (480) and 69 pairs (P1024) it runs ahead of
    both single responses at some tick, by up to 13 and 41 cells.
  - **The layer is nonlinear, and its nonlinearity stays behind the front.**
- **P41d: HELD.** At all 400 gaps in both phases, the tangent map's deepest cell leaves the true one within one wake
  period, typically within 2 to 15 ticks. The quadratic term is active at the deep end immediately.
- **P41e: HELD in substance, under a stricter test than written.**
  - As worded, P41e named (208, 272), which turned out not to be the 32-cell period; the clean front's 32-cell window
    repeats with (52, 68).
  - The test was therefore made strict: does each run's 32-cell window, with its front class, equal one of the clean
    front's own pairs at the same alignment?
  - All 400 runs (200 at K = 40, 200 at K = 80) are **captured**, within at most 344 ticks (median 125 and 59) of the
    front passing depth 3K.
  - So T39's missing recurrences were bystander particles deeper in the 256-cell window.

### 44.5 Results, part 2: the clean fronts are robust ([`front_closure.py`](../tests/probes/front_closure.py), [output](../tests/probes/front_closure.out))

| phase | W | clean states | forward closure | FAIL edges | every path of k ticks advances | exact control (random wakes behind the window) |
|---|---|---|---|---|---|---|
| G8 (control) | 5, 8 | 8 | 10, 22 | 0 | k = 2 | 50 runs, 150,000 ticks: 0 states outside, 0 stalls |
| 480-state phase | 8, 12, 16, 24 | 288 | 416, 576, 352, 560 | 0 | k = 2 (advances 0 or 2 only) | 100 runs per W (8, 16), 300,000 ticks each: 0 outside, 0 stalls |
| P1024 | 8, 12, 16, 24 | 52 | 389, 391, 342, 503 | 0 | k = 3 (advances −1 to 2) | 100 runs per W (8, 16), 300,000 ticks each: 0 outside, 0 stalls |
| G16 (counter-control) | 8 | 499 | 375,952 | 64 | no: least advance −713 over 600 ticks | — |

- **P41f HELD for both phases, at the smallest window tried (W = 8).**
- The G8 control agrees with §39.
- The counter-control discriminates: G16, whose front T40 found coupled to its wake, is not robust.
- A first version of the exact control ran its rows past the clean run's depth bound and reported states outside the
  closure; it was a bug in the control, not in the closure. Fixed by giving the control its own depth; recorded here as
  a failure caught by the G8 control.

### 44.6 What T41 teaches: the robustness lemma, and the one gap left

**Robustness lemma (COMPUTED certificate with exact controls; GPT's read of the closure code requested).**

Let E be the 480-state phase (respectively P1024). Let S_E be the forward closure, at W = 8, of the clean front's
states (416 and 389 states respectively). Suppose a black-edge row with tail E, at some tick, has its front at depth
R ≥ 12 showing a state of S_E. Then from that tick on:
- the front's (class, window) stays in S_E;
- every 2 consecutive ticks (respectively 3) advance the front by at least 1;
- in particular the front goes to infinity at speed at least 1/2 (respectively 1/3).

This holds whatever the row holds more than 8 cells behind its front.

*Proof.* Take a tick at which the window automaton's computed range R − W .. R + 2 lies at depths ≥ 2. The automaton's
one-tick edges include the real step, because the real deeper bits are one of the branches; this is §39's
over-approximation, whose soundness GPT carried for `front_cert.py` (GC2374). The successor function here is the same
construction. S_E is forward-closed, has no FAIL edge, and every path of length k in it advances by at least 1. So by
induction the real state stays in S_E. Within any k − 1 ticks the front falls by at most k − 1 cells (the least
one-tick advance is −1), so it stays at depth ≥ 10 = W + 2, and the over-approximation stays valid. ∎ (The
certificate itself is a finite computation. Its controls: G8, which agrees with §39; G16, which comes out not robust;
and 600,000 exact ticks with random wakes behind the window, none leaving S_E or stalling.)

**What it changes.**
1. **§43.6's (a), (b) and (c) collapse into this lemma.**
   - The layer of 100 to 250 cells does not need to be enumerated: the band and its riding particles are bystanders.
   - Only 8 cells behind the front and the phase ahead matter, once the front looks clean.
   - The linear-algebra route of my last pull is closed (P41c, P41d: the layer is nonlinear), but it is no longer needed.
2. **A necessary condition for walls.** An eternal periodic point with tail E (480 or P1024) has a front that never
   shows one of these 416 (respectively 389) states at depth ≥ 12.
3. **The one gap left is capture**, which is the fuel question made exact.
   - *Capture:* every black-edge row with tail E either has an unbounded front, or at some tick shows a state of S_E at
     depth ≥ 12.
   - Capture implies M_E(k) < ∞ for every k, and with the bridge (§38.2) no eternal point of any period ends in E.
   - It is measured in 400 of 400 random prefixes (P41e). It is not proved.
   - Its form for the prefix: write a prefixed row as the clean row XOR a damage Δ born above depth K. The row shows a
     clean state as soon as Δ's deepest cell lies more than 8 cells behind the clean front. So capture is a race of
     two damage fronts in known environments: Δ's deep end by the mask lemma in the clean band, and the clean front in
     E. Single flips lose that race beyond gap 7 (P41a).

**Routes for capture, in the order I would take them.**
- **(C1) The bad core.** In the whole W-window automaton (W = 8 to 10, which is cheap), find the states with an
  infinite FAIL-free path avoiding S_E.
  - If every cycle there advances, a front avoids capture with a bounded position only by infinitely many retreats
    of more than W cells. Fuel then becomes an accounting of deep retreats.
  - If zero-advance cycles remain, test each for realisability as a wall with the SAT encoding (§36): a real one would
    be a counterexample, a spurious one shows what the over-approximation must remember.
- **(C2) The race automaton.** States: the comoving phase of the clean band, plus Δ's bits in a window around the clean
  front. The goal state "Δ = 0 within 8 cells of the clean front" is absorbing by the lemma. This differs from (C1) by
  using the clean band's known periodic order (52 to 288 ticks) in place of arbitrary window contents.
- **(C3) Deep retreats need special windows.** A FAIL edge needs the front and its whole window to heal in one tick;
  only 85 of P1024's 1.4 million edges at W = 8 do. Characterise those windows by hand, and show that an advancing front
  through fresh phase never writes them.

**G16** stays outside: not robust (§44.5), coupled to its wake (T40), with an odometer wake (T37).

## 45. Capture, route C1: the bad core of the window automaton (T42, L1318)

### 45.1 Predictions, written before the run (`capture_core.py`)

Build the whole W = 8 window automaton of §39 for the 480-state phase (245,760 states) and P1024 (262,144) with
`front_cert.py`'s `build_generic`. Re-derive S_E inside it as the set reachable from the clean front's states. The
**bad core** B is the largest set of states outside S_E from which some FAIL-free path stays in the set for ever: a
greatest fixed point, computed by deleting states with no successor left in it.
- **P42a (consistency).** The re-derived S_E has exactly 416 and 389 states. It is an independent route to §44.5's sets,
  through `build_generic` instead of `front_closure.py`'s own successor function. Lean 95%.
- **P42b.** B is non-empty in both phases and contains a cycle of non-positive total advance. Lean 85%: `front_cert`
  found such cycles at W = 4 to 8, and they cannot lie in S_E.
- **P42c.** The states lying on non-positive cycles are under 1% of B. Lean 50%.
- **What it teaches.**
  - If B's cycles all advance, a front that avoids capture with a bounded position must make infinitely many retreats
    of more than W cells, and capture reduces to C3.
  - If non-positive cycles are numerous, an 8-cell window plus arbitrary content behind it is too coarse to force
    capture, and C2 must use the clean band's known order.
  - The cycles' windows say which kind of stall the over-approximation allows, and so what a finer state must
    remember.

### 45.2 Results ([`capture_core.py`](../tests/probes/capture_core.py), [output](../tests/probes/capture_core.out))

| phase | whole automaton (W = 8) | S_E re-derived | bad core B | least advance over 600 ticks in B | greedy witness cycle |
|---|---|---|---|---|---|
| 480-state phase | 3,932,160 states (480 × 32 classes), 21.3 million edges, 1,408 FAIL | **416** | 1,911,888 (48.6%) | −1,329 | 224 ticks, advance −480 |
| P1024 | 262,144 states, 1.41 million edges, 85 FAIL | **389** | 219,722 (83.8%) | −1,105 | 45 ticks, advance −79 |

- **P42a HELD.** `build_generic` reproduces S_E exactly (416 and 389 states), an independent route to §44.5's closures.
  - The prediction's state count for the 480-state phase was wrong: it has 480 columns, so 15,360 classes, not 960.
    The 960 of T38 are classes up to its twist.
- **P42b HELD.** B is large in both phases and full of non-positive cycles.
- **P42c REFUTED, decisively.** Every state of B has a 600-tick path with total advance ≤ 0. The least such advance is
  a retreat of about 1.8 to 2.2 cells per tick, sustained.

**What it teaches.** With arbitrary content behind the window, the over-approximation lets the front eat its way upward
for ever. It is fuel without limit, and it needs no deep retreat (no FAIL edge): the witness cycles retreat 2 to 8
cells per tick inside the window.
- A real front cannot do this for ever, because the mismatch's top is pinned (§40.1): fuel is finite in any one row.
  But no window state records how much retreatable material lies behind.
- So **C1 is closed as a route**. Capture cannot follow from a window state alone, at any W where arbitrary content is
  allowed behind.
- C3 loses its point in this form: deep retreats are not needed for unlimited retreat in the over-approximation.
- **A proof of capture needs a state that remembers the material behind the front**, or a lemma that the material an
  advancing front writes is not fuel ("self-written wake is not fuel"), which is what the robustness lemma shows for the
  clean front.
- This is GPT's point 5 of GC2384 met in practice: the entrance statement is separate, and it is the hard part.
- **The deep-retreat windows (route C3's listing, P1024, W = 8).**
  - 85 FAIL edges leave from 66 states, all in B and none in S_E, with 80 distinct (mismatch, phase) patterns.
  - The twelve most frequent all have 7 or 8 ones among their 10 mismatch bits (for example 1011011011 and
    0110111011): dense, near-solid damage blocks.
  - This matches GPT's GC507, where a solid damage block over a black background moves entirely in one update. Over a
    phase background, the healing blocks are dense with gaps matched to the phase. That is a correspondence, not a
    theorem.

### 45.3 Closing the capture interface (GC2386): predictions, written before the run

GC2386 carried §44.6's induction and found an open join:
- S_E was built from the clean front at one alignment (θ = 780);
- P41e's 400 captures each matched the clean front of its own θ;
- so "400 of 400 entered S_E" was not yet shown.

The fix is by construction. Let U be the union, over all 1,024 values of θ, of the clean front's 8-cell states at ticks
600 to 2,480: the same clean runs and tick range that `wake_attractor.py` compares against. Its top eight bits are the
8-cell window. Let S_E^all be the forward closure of U. A run captured at its own θ then shows a state of U, which lies
in S_E^all, with no bit-order conversion.
- **P42d.** S_E^all is ROBUST (FAIL-free, every k-path advances). Lean 80%.
- **P42e.** U ⊆ S_E(780): the clean fronts of all alignments fall into the one closure. Lean 65%.
- If P42d fails, the 400 captures entered only their own-alignment clean sets, and the robustness lemma has to be
  certified per alignment.

### 45.4 Results: the interface is closed for P1024 ([output](../tests/probes/front_closure.out), last section)

- **P42e HELD, in the strongest form.** Over all 1,024 alignments θ and ticks 600 to 2,480, the clean fronts' 8-cell
  states form **one set U of 52 states**, the set already found at θ = 780.
  - Every alignment's clean front settles on the same 52-state orbit in class coordinates.
- **P42d HELD.** The closure of U is S_E(780) itself: 389 states, FAIL-free, every 3-path advancing.
- **So P41e's 400 captures entered the certified S_E.**
  - A captured run's 32-cell window and class equal its own alignment's clean pair at some tick in [600, 2,480].
  - The top eight cells of that window are therefore a state of U.
  - The run's front was at depth ≥ 120 at that tick.
  - By the robustness lemma (graph-to-front transfer carried in GC2386; graph COMPUTED here), **each of those 400
    rows has a front that advances for ever**. That is an exact statement about 400 sampled rows, conditional on the
    finite graph data. It is not capture for all rows.
- **Export.** The 389 states and the 52 clean states are on the shared store
  (`cited/local/l1319-P1024-W8-S_E_all.txt`, SHA-256 `eeb62a45…8e47`; `cited/local/l1319-P1024-W8-U.txt`,
  `bf6ad11c…1fcb`). One state per line: θ class, then the window printed bit W − 1 first, where bit j − 1 = D_(R−j).
  The edges are regenerated by `front_closure.py` from these.
- **The 480-state phase** has no capture data yet (T39 and P41e were P1024 only). Its S_E is certified at one
  alignment. An all-alignment union over its 15,360 classes is the same check, if a capture run for it is wanted.

## 46. Is an advancing front's own wake fuel? (T43, L1321)

### 46.1 Setting and predictions, written before the run (`own_wake_fuel.py`; `front_closure.py --all-theta` for 480)

**Question.** Once the front has passed well beyond the prefix (depth cK, c = 2 and 3), how far can it still retreat?
The material behind it is then mostly the wake it wrote itself. If the late drawdown is bounded independently of K, the
prefix's fuel is spent before the front gets there, and its own wake supplies none beyond a constant. If it grows with
K, the wake carries the prefix's fuel forward.

**What this cannot decide (GC2378).** A bounded late drawdown says nothing about a front that never passes cK (a hovering
front). That case is exactly a periodic D-orbit with bounded support, the object the conjecture excludes. So this is a
test of how a proof of capture can be split, not a proof of capture.

**Setting.** As in T36 and T39: the edge frame, P1024 at a random θ, and the 480-state phase at a random alignment (a, q)
of its 960 classes. Random digits at depths 0 .. K−1 sit above the clean tail. K = 20, 40, 80, 160, 320, with 200 runs per
K and phase. Each run lasts until 2,000 ticks after the front first passes 3K (cap 6K + 2,400 ticks).
- **Late drawdown at c:** the largest (running maximum of R) − R over the 2,000 ticks after R first reaches cK. The
  horizon is fixed so that K does not lengthen it.
- **Capture:** the first tick at which R ≥ 12 and the 8-cell state (class, window) lies in the all-alignment S_E.
  - P1024: the exported 389 states.
  - 480: a new all-alignment union, built first by `front_closure.py --all-theta 480 8` from the clean starts of all 960
    classes.
- The drawdown after the passing tick is split into before and after capture.

**Predictions.**
- **F1 (P1024).** The late drawdown at c = 2 and at c = 3 is bounded independently of K, with a maximum over all runs ≤ 20
  (the T38 prepared-region maximum). Lean 65%.
- **F2 (480).** The same, ≤ 20. Lean 65%.
- **F3.** The capture delay after passing 3K does not grow with K: the medians stay within a factor of 2 across K, and
  every run is captured within 600 ticks of passing. Lean 55%.
- **F4 (control, a soundness alarm if it fails).** After capture every run stays in S_E for the rest of the run.
  - P1024: its drawdown after capture is ≤ 1, S_E's own largest fall below a running maximum, computed from its graph.
  - 480: it is 0, since S_E's advances are 0 and 2.
  - Lean 95%.
- **F5 (480 union).** The union U over all 960 classes has a FAIL-free closure in which every 2-path advances. Lean 70%.
  Whether U is one orbit, as P1024's 52 states were, I hold at 40%.
- **Counterfactual.** A late drawdown or capture delay that grows with K (for example linearly) would mean the wake
  carries the prefix's fuel past the front's passage. A capture proof would then need a K-dependent, global bound
  rather than a local one after passing.

**What it teaches if F1–F3 hold.** A proof of capture splits into two parts.
- (i) The front passes a depth beyond the prefix. This is the hovering question, which stays open.
- (ii) After passing, capture follows in bounded time with bounded retreat, independently of K. This is a local
  statement, and GPT's temporal-compatibility condition (GC2387: hidden inputs that keep their history) is the natural
  instrument for proving it.

Record searched: `record_find.py "late drawdown" "own wake" "capture delay"` (no hit in the record, the kit at c42f6e51,
the portal or the open kit PRs); `drawdown` (T35 §40, T36 §41, T38 §43, GC2378's hovering caveat); `front retreat`
(CL673's G16 odometer retreat; the kit PR's retreat-after-tick-1 explanation, which is about the centre column, not
this).

### 46.2 Results, part 1 ([`own_wake_fuel.py`](../tests/probes/own_wake_fuel.py), [output](../tests/probes/own_wake_fuel.out); `front_closure.py --all-theta`, [output](../tests/probes/front_closure.out), last sections)

Each phase took about 4 seconds on the M5, 1,000 runs per phase.

| | K = 20 | 40 | 80 | 160 | 320 |
|---|---|---|---|---|---|
| P1024, late drawdown max at c = 2 / c = 3 | 10 / 10 | 10 / 7 | 10 / 7 | 7 / 1 | 1 / 1 |
| P1024, captured before passing 3K (of 200) | 38 | 88 | 167 | 200 | 200 |
| P1024, delay after passing 3K: median / max | 55 / 201 | 47 / 210 | 40 / 152 | — | — |
| 480, late drawdown max at c = 2 / c = 3 | 6 / 6 | 6 / 5 | 6 / 5 | 6 / 5 | 3 / 0 |
| 480, captured before passing 3K (of 200) | 15 | 58 | 131 | 197 | 200 |
| 480, delay after passing 3K: median / max | 71 / 454 | 56 / 405 | 15 / 197 | 82 / 113 | — |

- **F1 and F2 HELD.** The late drawdown is bounded, and it falls with K rather than growing: at K ≥ 160 the only late
  fall left in P1024 is the 1 that S_E itself allows.
- **F3 HELD, with its framing wrong.** No run takes more than 454 ticks after passing 3K. But for long prefixes the
  front is captured before it reaches 3K at all: all 200 runs for P1024 at K ≥ 160 and for 480 at K = 320. So K is not
  the scale of capture.
- **F4 HELD (the control).** Over all 2,000 runs, no tick after capture lies outside S_E. The fall below the running
  maximum after capture is at most 1 for P1024 and 0 for 480. These are exactly the graph constants that
  `front_closure.py` computes for S_E^all: 1, and 0 since 480's advances are only 0 or 2.
- **F5 HELD, including the 40% part.** For the 480-state phase, all 960 alignment classes have the same 288 clean
  states.
  - Their closure is the 416-state S_E of the base alignment: FAIL-free, every 2-path advancing, and no fall at all.
  - Digests of the lines: S_E^all `571a1847…5016`, U `0ae53342…f96c`.
  - So both periodic-wake phases lock their clean front to a single orbit whatever the alignment.
  - The P1024 rerun reproduces L1319's files byte for byte.
- **Consequence (an exact statement about samples, conditional on the COMPUTED graph data).** Each of the 2,000 sampled
  rows, 1,000 per phase, has a front that advances for ever.
- **Not shown.** This is capture for sampled rows only. A prefix built to carry fuel may behave differently: T38's
  prepared regions have drawdowns growing with r. The hovering case of §46.1 is untouched.

*Correction (GC2390, accepted in L1323).* F3's factor-two median criterion **failed** for 480's post-3K group (medians
15–82; that group shrinks and is selected differently as more rows capture before 3K). F3 held only in its maximum-delay
part, so "all eight held" in L1321 is withdrawn: seven held, and F3 held in part. Also, the post-capture alarm above runs
only at R ≥ 12, so it could miss a later tick at R = 10 or 11. T44 checks every post-capture tick at R ≥ 8 and records
the minimum depth.

### 46.3 Part 2, predictions written before the run: is capture timed by the front's own clock?

The same runs with the same seed. The measurement is extended (no new random draws, so part 1's lines must recur
exactly):
- the capture tick counted from t = 0;
- R − K at capture;
- the early drawdown, the largest fall below the running maximum before capture.

**Predictions.**
- **F6.** The capture tick from t = 0 is bounded independently of K: medians within a factor of 2 across K = 20 .. 320,
  and a maximum ≤ 600, in both phases. Lean 60%.
- **F7.** At capture, R − K is bounded independently of K, at most 600. Capture then happens within a bounded distance
  after the front leaves the prefix, so the material behind it at capture is still mostly the prefix's own. Lean 55%.
- **F8.** The early drawdown is bounded independently of K for random prefixes, at most 25. Lean 50%. T38's prepared
  regions show that an adversarial prefix can do more.
- **Counterfactual.** A capture tick or an early drawdown growing with K would mean the prefix's chaos delays capture in
  proportion to its size. That chaos spreads deeper at speed 2, faster than either front (17/13 and 5/3), so it can
  reach the front.
- **What it teaches if F6–F8 hold.** For typical prefixes, capture is decided by the front's first few hundred ticks in
  the clean tail. The prefix's chaos never catches up with the front, even though its light cone does: that is
  decoupling (T40, T41) at the scale of the whole prefix. A proof of capture would then need only the front's local
  entry into S_E plus a bound on what the prefix can do to it, not the whole of the prefix's evolution.

### 46.4 Results, part 2: capture is timed by the front's own clock ([output](../tests/probes/own_wake_fuel.out))

Part 1's lines recur exactly, as they must, since there are no new random draws.

| | K = 20 | 40 | 80 | 160 | 320 |
|---|---|---|---|---|---|
| P1024, capture tick from t = 0: median / max | 73 / 247 | 80 / 295 | 71 / 297 | 74 / 264 | 79 / 264 |
| P1024, R − K at capture: median / max | 82 / 269 | 89 / 316 | 82 / 325 | 83 / 279 | 89 / 310 |
| P1024, early drawdown: median / max | 3 / 10 | 3 / 10 | 3 / 10 | 3 / 11 | 3 / 11 |
| 480, capture tick from t = 0: median / max | 102 / 493 | 94 / 471 | 102 / 343 | 99 / 420 | 101 / 377 |
| 480, R − K at capture: median / max | 134 / 576 | 127 / 529 | 135 / 406 | 119 / 459 | 134 / 421 |
| 480, early drawdown: median / max | 3 / 6 | 3 / 10 | 3 / 8 | 3 / 7 | 3 / 8 |

- **F6 HELD, and more strongly than predicted.** The capture tick's distribution does not depend on K at all. The medians
  are 71 to 80 for P1024 and 94 to 102 for 480, from K = 20 to K = 320. A prefix sixteen times longer neither delays nor
  hastens capture.
- **F7 HELD.** Capture comes within 325 cells (P1024) and 576 cells (480) of the prefix's end, with medians of about 85
  and 130.
- **F8 HELD.** The fall below the running maximum before capture is at most 11 at every K, with a median of 3.

**What T43 teaches.**
- For typical prefixes, **capture is a front-local event.** The front starts at the prefix's deepest mismatch, a few
  cells above its end. It runs into the clean tail, and its window joins the locked clean orbit (U) within about 75–100
  ticks, at most about 500.
- *(GC2390: the n/(2 − v) figures below use the post-capture speed and are approximate. An exact per-run cone needs the actual pre-capture path: b + 2t ≤ R(t) − 9 with b = K − L − 1.)*
- **The light cone, accounted for (Local's correction, written before this section was pushed).** A prefix cell n cells
  above the front's start reaches the front's depth only after about n/(2 − v) ticks, with v the front speed. That is
  1.45n ticks for P1024 and 3n for 480.
  - By P1024's median capture tick (about 75), only the bottom ~52 prefix cells can have influenced the front; by its
    largest (297), the bottom ~205. For 480 these are ~33 and ~163 cells.
  - So at K ≥ 160 most of the prefix is causally cut off at capture, and K-independence there is a light-cone fact, not
    decoupling.
  - The informative cases are K = 20 and 40. There the whole prefix, and the edge above it, lie inside the light cone
    before capture, and the capture times are the same.
  - What T43 shows is therefore narrower than "the chaos never catches up". Capture happens within a bounded time,
    hence it depends on a bounded bottom part of the prefix, and a short prefix with the edge close behind does not
    slow it.
- **The own wake is not fuel**, in the measured sense. After capture the front falls at most S_E's own constant (1, or
  0), and before capture it falls at most 11, whatever K is.
- **Where this leaves capture.**
  - The certificate shape is front-local, but C1 (§45) showed that a window over-approximation cannot see it. Arbitrary
    content behind the window gives arbitrary fuel.
  - The real content behind the front has history: it is the prefix's evolution plus the front's own wake. The capture
    times bound how much of it can matter: at most the bottom (2 − v) × (capture time) cells of the prefix.
  - So the next certificate must model the hidden inputs as a dynamical system with history, not as adversarial bits.
    This is GPT's temporal-compatibility condition (GC2387), and route C3's characterisation of deep-retreat windows
    belongs to it.
  - A concrete test of locality comes first. Is the capture tick determined by the prefix's bottom L cells alone (the
    upper K − L cells re-randomised), and for which L? A small L would make capture a finite question over (alignment,
    L cells).
- **Not shown.** These are random prefixes. A prefix built to carry fuel (T38's prepared regions) may delay capture in
  proportion to its size. The hovering case of §46.1 is untouched.

## 47. Local's carrying read of GC2389: the exact front clock and the one-flip completion (L1322)

### 47.1 The read, and predictions for the finite replay (written before the run)

GC2389 ([report](GPT-CAPTURE-CHECK-20261102.md#gc2389--post-run-certificate-read-the-phase-clock-and-its-reset-states))
asks for a carrying read of three hand steps. Each is sound given its finite facts.
- **Clock transfer.** Once the front is in S_E at R ≥ 12, the actual transition is always one of the graph's edges
  (GC2386). The class moves by c ↦ c + 1 + 195a. If every edge out of a class has the same advance a, the actual
  advance is a function of the class alone. The class then walks the projected cycle whatever the window does, and
  R(t + 52) = R(t) + 68.
- **The speed bound.** It telescopes 13a − 17 along the actual path. Since a is a function of the class, the potential
  can be taken on the 52 classes (partial sums round the cycle, which return to 13·68 − 17·52 = 0). The bound is their
  range.
- **The resets.** At a class whose S_E fibre is a single window, the actual window is forced.
- **The single flip.** The prefix lies at depths ≤ K − 1 ≤ R − 9. The only mismatch at depth ≥ K is the flip at R, so
  the state is (θ + 195R mod 1024, 0). Since 195 · (−21) = −4,095 ≡ 1 (mod 1024), R ≡ 21(θ − 882) gives class 882. The
  guard R ≥ max(K + 8, 12) gives the eight zero cells and the edge guard.
- **Noninterference.** Equal class and front give equal future advances by the clock, so the mutual mismatch is
  confined to depths < R. At a singleton reset both windows are the forced one, so the mismatch lies at least nine cells
  behind.

**Predictions for the replay with Local's own generator** (`front_closure.py P1024 8 --all-theta --clock`, the
successor function of §44, independent of GPT's literal reconstruction):
- **K1.** Every class has one (next class, advance). The 52 classes form one cycle, total advance 68, least period 52.
- **K2.** The potential range is 55.
- **K3.** The singleton fibres are (23, 76), (264, 206), (656, 121) and (897, 178), and the longest wait is 47.
- **K4.** (882, 0) is the only window-0 state.
- **Counterfactual.** Any difference would mean the two independent generators disagree on S_E's edges, a soundness
  question for one of them.
- **The same test on 480 (new, Lean 60%).** Its advances are 0 or 2, and I expect the same determinism: one cycle of
  288 classes with total advance 480. That would be an exact clock of speed 5/3 for the second phase.

### 47.2 Results ([output](../tests/probes/front_closure.out), last section)

- **K1–K4 HELD, exactly.** Local's generator gives the same 52 classes, the same deterministic projection, one cycle
  of total advance 68, the same advance word (least period 52), potential range 55, the same four singleton fibres
  with longest wait 47, and (882, 0) as the only window-0 state. Two independent generators agree on every finite fact
  GC2389 uses. With the hand steps of §47.1, **GC2389's clock and single-flip completion are PROVED two-party**,
  conditional on the shared finite data. PROOFS.md entry filed as carried.
- **The 480-state phase has an exact clock too.**
  - All 288 classes of its S_E^all have one (next class, advance), and they form one cycle of total advance 480.
  - The advance word repeats every 18 ticks (2,0,2,2,2,2,0,2,2,2,2,0,2,2,2,2,2,2: +30). So after capture
    R(t + 18) = R(t) + 30 exactly, and |3(R(t + n) − R(t)) − 5n| ≤ 7, the range of the potential 3a − 5 round the
    cycle.
  - 208 of the 288 classes are singleton fibres, using 13 distinct windows, and the longest wait to one is 2 ticks. The
    window is re-forced almost every tick.
  - There is no window-0 state, so 480's one-flip completion needs a few flips: any singleton state, written below the
    prefix, does the same job.
- **What it adds to capture.** In both phases, entry into S_E is equivalent to hitting one forced gateway at depth ≥ 12
  (GC2389's remark, now in both phases). After entry the front is an exact clock that ignores its older wake.
  - So the open question is purely an entrance question: does every row's front eventually write the gateway's eight
    cells at the gateway's phase?
  - T43 says that typical rows do so within ~300 (P1024) or ~500 (480) ticks of leaving the prefix, whatever the prefix
    length.

## 48. Is capture decided by the bottom of the prefix? (T44, L1324)

### 48.1 Setting and predictions, written before the run (`capture_locality.py`)

**Question.** T43 found that capture times don't depend on the prefix length. Is that because only the bottom L cells
of the prefix matter? Take a base row A and a variant B that keeps A's bottom L cells and redraws the upper K − L.
- **The control.** GC2390's cone guard (carried in L1323) makes some pairs agree automatically. If b + 2t ≤ R_A(t) − 9
  for every t ≤ T_A, with b = K − L − 1, the front states agree through A's capture tick T_A.
- **The informative pairs** are those with L < L*, where L* = K + 8 + max over t ≤ T_A of (2t − R_A(t)). For them the
  redrawn cells can reach the front's window before capture. Whether the front then still behaves identically is
  dynamical shielding: the front ignoring information that has reached it.

**Setting.** P1024 and 480, K = 80 and 160, 100 base rows per K and phase, 4 variants per (base row, L), with
L ∈ {4, 8, 12, 16, 24, 32, 48, 64, 96, 128}, L < K, and Random(44).
- Capture is the first S_E state at R ≥ 12.
- After capture every tick is checked: an alarm below depth 10, an alarm outside S_E, and the minimum depth recorded
  (GC2390's coverage fix).
- Recorded for each informative pair:
  - whether the front history is identical through T_A;
  - whether the capture tick is the same;
  - the lag from the cone's arrival at the window to the first difference;
  - T_B − T_A.

**Predictions.**
- **H1 (control, certain if the code is right).** Every protected pair is identical through T_A, and no informative pair
  differs before the cone arrives. Any failure is a bug.
- **H2.** L* is typically 40–80: P1024 median near 8 + 0.69 · T_A ≈ 60, 480 near 8 + 0.33 · T_A ≈ 40, with the
  per-run cone. Lean 55%.
- **H3 (shielding).** Among informative pairs, the share with the same capture tick rises with L and reaches ≥ 90% by
  L = 24 in both phases. Lean 50%.
- **H4.** When the front history does differ, the first difference comes well after the cone's arrival (median lag ≥ 10
  ticks): the front ignores most of what reaches its window. Lean 45%.
- **H5 (coverage).** No post-capture alarm, and the minimum post-capture depth is ≥ 10 in every captured run. Lean 95%.
- **Counterfactual.** If the same-capture share stays low even at L just below L*, and differences appear as soon as
  the cone arrives, then capture is not front-local beyond the light cone. A certificate would have to carry the whole
  cone's history, and GPT's compatibility condition would need the full prefix, not a short window.
- **What it teaches if H3–H4 hold.** The history that a capture certificate must remember is short (L cells at the
  start, plus whatever the front ignores). That sizes GPT's generated-history condition.

Record searched: GC2390's guard (the cone lemma); T40/T41 decoupling (single flips behind a clean front: none reach it
in 480, gaps ≤ 7 in P1024); T43 (§46). `record_find.py locality "bottom L"` finds only these. Sampled pairs say nothing
about a uniform L for every prefix (GC2390).

### 48.2 Results ([output](../tests/probes/capture_locality.out))

The share of informative pairs with the same capture tick (and the same front history through T_A), 400 pairs per L
less the protected ones:

| L | P1024 K=80 | P1024 K=160 | 480 K=80 | 480 K=160 |
|---|---|---|---|---|
| 4 | 13% (0%) | 16% (0%) | 41% (1%) | 54% (1%) |
| 8 | 23% (2%) | 29% (4%) | 64% (7%) | 70% (7%) |
| 16 | 51% (38%) | 56% (38%) | 86% (55%) | 91% (63%) |
| 24 | 80% (73%) | 78% (70%) | 92% (82%) | 95% (86%) |
| 32 | 89% (85%) | 89% (84%) | 96% (90%) | 98% (94%) |
| 48 | 99% (99%) | 99% (97%) | 99% (92%) | 100% (96%) |
| 64 | 100% (100%) | 99% (99%) | 100% (98%) | 99% (97%) |

- **H1 HELD (the control).** No protected pair differs, no pair differs before the cone reaches the window, and no
  alarm fires.
- **H5 HELD.** No post-capture alarm in any run; the minimum post-capture depth is 80 or more.
- **H2 HELD in its range.** The median L* is 76–80 in both phases. My 480 estimate (~40) used the post-capture speed
  and was too low, as GC2390 warned.
- **H3 REFUTED for P1024, HELD for 480.** At L = 24, P1024 is at 78–80%; it passes 89% at L = 32 and 99% at L = 48. 480
  passes 90% by L = 16–24.
- *(GC2393, carried in L1327: H4 is NOT SHOWN. The lag list mixes observed first differences with censored values T_A + 1 −
  t_reach from pairs that never differed, which dominate at large L. The cone's arrival is also only permission, not a
  real discrepancy at the window. An uncensored split is needed. The capture-agreement fractions stand.)*
- **H4 HELD where it means anything (L ≥ 16).** The median lag from the cone's arrival at the window to the first
  difference is 28–56 ticks (P1024) and 35–86 ticks (480). At L ≤ 8 the edited cells already lie inside the initial
  window (the front starts near K − 1), so a lag of 0 there is not shielding. L = 12 is borderline (9–16).
- **So the front shields itself.** For pairs whose edits reach the window before capture, keeping 48 cells (P1024) or
  24 (480) fixes the capture tick in 92–100% of samples. That is about half the light-cone bound L*.

**An unexpected regularity: capture is driven by the background.** Even with only 4 cells kept, 480 rows sharing an
alignment are captured on the same tick in 41–54% of pairs, and the median T_B − T_A is 0 at every L in both phases.
The explanation is already in the algebra.
- **The look-ahead lemma (PROVED; the mask lemma, §44.1, CL679 P-K2).** At an interior front, the deepest new cell is
  D_{R+2}(t + 1) = ¬E_{R+1}(t), whatever the window holds. So the front advances by 2 exactly when E_{R+1}(t) = 0,
  and otherwise by at most 1.
- E_{R+1}(t) is a function of the class: bit (c + 195) of the base column for P1024, and column (R + 1 + a) at time
  (t + q) for 480.
- **Hence the front's move is window-independent at every "open" class.** The window matters only at "blocked"
  classes (look-ahead bit 1).
- **Check (COMPUTED).** Round P1024's 52-cycle, the advance is 2 at exactly the 31 open classes. It is −1, 0 or 1 at the
  21 blocked ones (13 zeros, 7 ones, one −1).
- So GPT's clock theorem has a mechanism: inside S_E, the blocked classes' windows are such that even their advances
  are fixed.

**What T44 teaches.**
- The history a capture certificate must keep is short in practice: about 48 cells for P1024 and 24 for 480, at the
  start, in samples. Not a uniform bound.
- The front's motion depends on its window only at blocked classes. A certificate can therefore follow the front's
  class walk, with the window consulted only at blocked ticks.
- That suggests a quotient for GPT's compatibility condition: track the class walk exactly, and the window only
  through its effect at blocked classes.

## 49. How far behind the front does a blocked move read? (T45, L1325)

### 49.1 Setting and predictions, written before the run (`blocked_reading.py`)

**Exact structure first (COMPUTED, no simulation).**
- P1024 has 501 open classes of 1,024 (look-ahead bit 0).
- Under the forced open move c ↦ c + 391, the open runs have lengths 1 (128 runs), 2 (69), 3 (37), 4 (15), 5 (6), 6 (3),
  7 (1) and 9 (1). So a front meets a blocked class about every other tick.

**Question.** At a blocked tick the move depends on the cells behind the front. By the algebra:
- a = 1 reads E_R, E_{R−1} and D_{R−1};
- a = 0 reads D_{R−1} and D_{R−2};
- only a retreat reads deeper.

The **reading depth** of a tick is the least k such that D_{R−1} .. D_{R−k} (the actual values) fix the move for every
completion of the cells behind them, out to depth 10. It is reported as "> 10" if the cells out to 10 do not fix it.

**Setting.** P1024 and 480, K = 80, 200 random prefixes each, Random(45). Every tick at R ≥ 12 before capture, and
the first 300 ticks after it, using the exported S_E.

**Predictions.**
- **J1 (control).** At every open tick the move is +2 with reading depth 0. This is PROVED, so a failure is a bug.
- **J2.** At pre-capture blocked ticks the reading depth is ≤ 2 in at least 75%, and retreats (a < 0) are at most 15% of
  blocked ticks. Lean 55%.
- **J3.** A reading depth above 8 (beyond the 8-cell window) occurs at no more than 1% of pre-capture blocked ticks.
  Lean 70%.
- **J4.** After capture the reading depth is at most 4 at every blocked tick (S_E's only retreat is −1). Lean 70%.
- **Counterfactual.** Frequent deep reads before capture would mean the front's move draws on cells far behind. A
  capture certificate would then need a long history.
- **What it teaches.** It measures the true memory of the front's motion at blocked ticks. With T44's shielding, it says
  how small a state GPT's compatibility condition might get away with.

Record searched: §44.1 (the mask lemma), §48 (T44), GC2389's clock; nothing earlier measures reading depth.

### 49.2 Results ([output](../tests/probes/blocked_reading.out))

*Correction (GC2393, carried in L1327).* The reading-depth wrapper labelled an unresolved move (new front 9 or more cells
behind) as depth 10, because at k = 10 the single completion always equals itself. No sampled move was unresolved (every
reported offset is concrete, −6 to +1), so the counts below are unchanged. The wrapper now returns "unresolved" before
minimising.

| | P1024 before capture | P1024 after | 480 before | 480 after |
|---|---|---|---|---|
| blocked ticks | 7,503 | 24,326 | 7,935 | 10,015 |
| reading depth 0 / 1 / 2 | 16.7 / 67.9 / 4.3% | 19.1 / 71.5 / 4.5% | 20.6 / 67.8 / 3.2% | 0 / 100 / 0% |
| reading depth 3–4 / 5–8 / > 8 | 10.0 / 1.2 / 0% | 4.8 / 0 / 0% | 7.6 / 0.7 / 0% | 0 / 0 / 0% |
| retreats (new front below R) | 11.7% (deepest −6) | 4.8% (only −1) | 8.9% (deepest −6) | none (every blocked move is 0) |

- **J1 HELD (the control).** At all 45,018 (P1024) and 62,082 (480) open ticks the move is +2 and reads nothing.
- **J2 HELD.** Before capture, 89% (P1024) and 92% (480) of blocked moves read at most 2 cells behind the front. Retreats
  are 12% and 9% of blocked ticks.
- **J3 HELD, strongly.** No move in 15,438 pre-capture blocked ticks reads beyond 8 cells; the deepest read is 8
  (P1024, twice) and 7 (480). So in every sampled real tick the 8-cell window, with no help from the unknown bits behind
  it, fixed the move. The bad core's unbounded retreats need window contents that these evolutions never put behind
  the front.
- **J4 HELD.** After capture the reading depth is at most 3. In 480 every blocked move is 0 and reads exactly one cell,
  so inside S_E its blocked classes all see D_{R−1} = 0 (or the value that gives 0).

**The front plus two cells is closed along +2 moves.** It follows from the update rule.
- After a +2 move, the new front's two cells behind are D_{R+1}(t + 1) and D_R(t + 1). They are functions of E and
  the old D_{R−1}, D_{R−2} alone.
- A +1 move pulls in one deeper cell (D_{R−3}). A 0 pulls in two, and a retreat of r pulls in about r + 2.
- So the front's state (class, D_{R−1}, D_{R−2}) evolves autonomously along open stretches. Memory enters only at
  blocked ticks, and then mostly one or two cells at a time.

**What T45 teaches.** The move's memory is shallow: about 2 cells usually, 8 at most in samples. What remains deep is
the window's own evolution. Each non-+2 move draws one or more cells from behind into the front's reach. A certificate
that tracks (class, two cells) exactly, and treats the cells drawn in at blocked ticks as inputs with history, is the
small state the measurements point to. That is the quotient offered to GPT in L1324.

## 50. How does every alignment lock onto one orbit? (T46, L1326)

### 50.1 Predictions, written before the run (`lock_entry.py`)

**Question.** In both phases every alignment's clean front, the black edge on the clean tail, ends on the same orbit U:
52 states for P1024 (L1319) and 288 for 480 (L1321). How does it get there?
- Does it enter U through a few gateways, or anywhere?
- Does it find the cycle of classes before its window locks?
- How long does locking take?

For every alignment (1,024 θ for P1024; one per class of 480's 960) the clean front is run to tick 2,480, recording:
- the first tick its 8-cell state lies in U, and that state;
- the first tick its class lies on U's class cycle;
- whether it ever leaves U after entering.

**Predictions.**
- **K1.** Every alignment enters U before tick 600 (the start of the range U was built from), with a median entry tick
  of 100–300. Lean 70%.
- **K2.** Entry is through at most 4 distinct first states, plausibly singleton fibres such as P1024's (23, 76). Lean
  35%.
- **K3.** In most alignments the class reaches the cycle at least 10 ticks before the window locks: the class locks
  first, and the window follows. Lean 50%.
- **K4 (control).** No alignment leaves U after entering it. U's closure is S_E, but U itself need not be closed. A
  departure would show that U is only the support of the eventual orbit, not an invariant set. Lean 60% that none leave.
- **Counterfactual.** Many distinct first states spread round the cycle would mean the lock is a basin covering the
  whole orbit, with no special gateway. Then why the lock is unique has to be a global argument about the class walk.

Record searched: L1319 (one 52-state U for all θ), L1321 (one 288-state U for all 480 classes), GC2389 (clock and
gateways), §49 (front plus two cells); no earlier measurement of entry. Budget: one block.

### 50.2 Results ([output](../tests/probes/lock_entry.out))

*Correction (GC2393, carried in L1327).* T46 measures first visits to U and to its class cycle, not permanent locks; its
own later departures (K4) show that the first visit is not the locking time. "Locks" below means "first reaches". The
last departure, which is the true lock time, was not measured, and a no-departure claim for all future time needs the
closed certificate S_E.

| | P1024 (1,024 θ) | 480 (960 classes) |
|---|---|---|
| entry tick into U: min / median / 90% / max | 9 / 67 / 146 / 236 | 7 / 95 / 196 / 456 |
| class first on the cycle: median tick | 36 | 78 |
| window locks after the class: median / max | 13 / 175 | 17 / 138 |
| alignments whose class leads by ≥ 10 ticks | 575 (56%) | 859 (89%) |
| distinct first states in U | 21 | 36 |
| ticks outside U after first entry | 5,284 | 222 |

- **K1 HELD in part.** Every alignment enters U long before tick 600. Its median-range part (100–300) is REFUTED:
  locking is faster, with medians of 67 and 95.
- **K2 REFUTED.** There is no small set of gateways: 21 and 36 distinct first states. Entry is concentrated, though.
  - In P1024 three states take 44% of entries: (731, 34), (506, 230) and the singleton fibre (264, 206). Only one of the
    top eight is a singleton fibre; the others' fibres have 3 to 10 states.
  - In 480 every one of the eight commonest first states has window 230, at different classes.
- **K3 HELD.** The class reaches the cycle first, and the window follows a median 13–17 ticks later. In most alignments
  the class leads by 10 ticks or more.
- **K4 REFUTED.** Fronts leave U after first entering it (5,284 and 222 ticks in all, all before tick 600 by U's
  definition). U is the support of the eventual orbit, not an invariant set; the closed set is S_E.

**What T46 teaches.** The lock is a two-stage convergence, the class first and then the window, through many entry
points. Why the eventual orbit is unique is therefore a property of the whole basin, not of a gateway. The window 230
shared by 480's commonest entries (D_{R−1} = 0, the move "0" seen in every blocked tick of 480's S_E in §49) suggests
the class walk reaches the cycle and the two cells behind the front then fall into place.
- **Next form of the question (logged, not taken).** Is the class cycle the unique attracting cycle of the class walk
  when each blocked choice follows the front-plus-two-cells dynamics? If it is, uniqueness becomes a finite statement
  about a 1,024-class (or 15,360-class) walk.

## 51. After a pair reset, how much history still matters? (T47, L1329)

### 51.1 Setting and predictions, written before the run (`reset_memory.py`)

**Background.**
- GC2393's two-open reset (carried in L1327): at a class where E_R = E_{R+1} = 0 and E_{R+2} = E_{R+3}, the next two
  moves are +2 and the trailing pair becomes a function of the background alone.
- GC2395 (carried in L1328): the erased bit can return one blocked move later from the third cell. So a reset of the
  pair is not a reset of the history.
- Exact counts: P1024 has 108 reset classes of 1,024 (6 on the 52-cycle), and 480 has 1,952 of 15,360.

**Setting.** P1024 and 480, K = 80, 150 random prefixes each, Random(47), pre-capture ticks at R ≥ 12 only.
- **Frequency.** Count reset events (a tick at a reset class), and the blocked moves between consecutive resets.
- **Memory.** At up to 5 resets per run, take the row two ticks after the reset tick (front R′ = R + 4). Flip one cell
  j behind the new front (j = 3, 4, 6, 8, 12, 16; the pair is untouched) and run both rows for 200 ticks. Record
  whether the front path differs, and the first tick of difference.

**Predictions.**
- **M1.** Reset events make up between 5% and 20% of pre-capture ticks. Lean 65%.
- **M2.** The median number of blocked moves between consecutive resets is ≤ 5. Lean 55%.
- **M3.** Flipping the third cell (j = 3) right after a reset changes the front path within 200 ticks in at least 30% of
  events: memory does return in practice. Lean 55%.
- **M4.** The effect fades with depth: at j = 16 at most 10% of events change the front path. Lean 60%.
- **Counterfactual.** If j = 3 flips almost never matter, the reset in practice erases the decisive memory, and the
  return in GC2395 does not arise on these phases. If deep flips often matter, long history persists through resets,
  and the compatibility condition cannot be cut at resets.
- **What it teaches.** The effective memory length at a reset tells GPT whether history can be cut at resets plus a
  bounded depth.

Record searched: GC2393, GC2395 and their carrying reads (L1327, L1328); T41's single-flip decoupling of clean fronts
(gap ≤ 7 matters in P1024, none in 480); T44 (§48).

### 51.2 Results ([output](../tests/probes/reset_memory.out))

| | P1024 | 480 |
|---|---|---|
| reset ticks among pre-capture ticks | 1,386 of 13,414 (10.3%) | 2,729 of 14,550 (18.8%) |
| blocked moves between consecutive resets: median / 90% / max | 2 / 10 / 28 | 1 / 6 / 25 |
| a flip j cells behind the front, 2 ticks after a reset, changes the front path within 200 ticks: j = 3 / 4 / 6 / 8 / 12 / 16 | 84 / 81 / 67 / 52 / 37 / 23% | 64 / 48 / 42 / 31 / 16 / 9% |
| first difference, median ticks: j = 3 / 8 / 16 | 9 / 24 / 55 | 7 / 26 / 61 |

- **M1 HELD.** Resets are 10% and 19% of pre-capture ticks.
- **M2 HELD.** The median number of blocked moves between resets is 2 (P1024) and 1 (480).
- **M3 HELD, strongly.** A flip of the third cell right after a reset changes the front path in 84% and 64% of events,
  with the first difference after a median 7–9 ticks. GC2395's return is the rule on these phases, not an exception.
- **M4 REFUTED for P1024, HELD for 480.** At j = 16, P1024's front path still changes in 23% of events (480: 9%). The
  effect fades with depth, about halving every 4–6 cells, but slowly.

**What T47 teaches.**
- **Pair resets do not cut the history.** Resets are frequent, but the cells behind the pair carry information that
  returns to the front within tens of ticks. A single cell 16 back still steers P1024's front a quarter of the time.
  The compatibility condition cannot cut history at resets plus a short depth; GPT's import-history line is the
  necessary one.
- **Changing the path is not changing the capture.** Combine this with T44 (bottom 48 cells fix the capture tick in 99%
  of P1024 pairs). The front's path is sensitive to deep cells, but where it ends up, captured, is not. The robust object
  is the entrance into S_E, not the path. That points away from path-level certificates and towards an argument that
  every path is funnelled into S_E. The funnel is the open question.

## 52. Is the funnel into S_E visible in the window automaton? (T48, L1330)

### 52.1 Setting and predictions, written before the run (`funnel_attractor.py`)

**Question.**
- T44 and T47 show that the front's path depends on deep cells, while its entrance into S_E is robust.
- Is that robustness already visible to the 8-cell window automaton (§39), with arbitrary content behind the window?
- The attractor A of S_E answers this. It is the least set of states, outside S_E and with no FAIL branch, whose every
  successor lies in S_E ∪ A.
- From a state of A every continuation reaches S_E within rank(v) ticks, whatever lies behind the window. (This is
  sound while the front stays at depth ≥ 10 + the retreats on the way; the real check below uses R ≥ 12 and records any
  violation.)

**Setting.**
- P1024 only, W = 8: the whole automaton, 262,144 states.
- 480's automaton (3.9 million states) is too heavy for the M5 under the owner's light-use rule.
- Real paths: 200 random prefixes, K = 80, Random(48), every tick at R ≥ 12 until capture.

**Predictions.**
- **F1.** A is small: at most 10% of the automaton. Lean 55%. The bad core (84% of the automaton, §45) cannot lie in A.
- **F2.** Real paths reach A ∪ S_E only a median ≤ 15 ticks before capture: the window abstraction sees the funnel only
  at its very end. Lean 55%.
- **F3 (control, a soundness alarm).** Every real path that enters A at a state of rank r reaches S_E within r ticks.
- **Counterfactual.** If real paths enter A long before capture (median lead ≥ 50 ticks), the window abstraction
  already explains much of the funnel, and a capture proof could aim at "every path reaches A". If the lead is short,
  the funnel lives in the history, and GPT's line is the one that can reach it.

Record searched: §45 (bad core, C1), §44.6 (routes C1–C3), GC2389 (gateways); attractor of S_E listed as a pull in
L1321/INSTINCT; not computed before.

### 52.2 Results ([output](../tests/probes/funnel_attractor.out))

- The automaton has 262,144 states and 621,312 distinct edges. 66 states have a FAIL branch.
- A, outside S_E, has **42,033 states (16.0%)**. Its ranks run up to 113, spread fairly evenly (421, 453, 467, … states
  at ranks 1, 2, 3, …).
- **F1 REFUTED.** A is larger than the predicted 10%.
- **F2 REFUTED.** All 200 real paths enter A before capture, with a median lead of 26 ticks (90%: 57; max 111). On
  average they spend 36% of their pre-capture time in A. The window abstraction sees the funnel well before its end,
  but not from the start.
- **F3 HELD (the control).** Every path that entered A was captured within its entry rank (median 37, max 111), with no
  alarm. Once inside A a real path cannot leave it except into S_E, since A's successors all lie in S_E ∪ A.
- **An exact dichotomy (COMPUTED).** §45's bad core B (219,722 states, the states with an infinite FAIL-free path
  avoiding S_E) leaves exactly 42,033 states outside S_E ∪ B, and those are exactly A. So **every state outside S_E is
  either forced into S_E within at most 113 ticks, whatever lies behind the window, or lies in the bad core**. No state
  is undecided, and all 66 FAIL states lie in B.

**What T48 teaches.**
- **Capture is exactly "leaving the bad core".** A real front is captured if and only if its 8-cell state ever leaves B
  at depth ≥ 12 (plus the soundness margin). It is then in A, and S_E follows within its rank.
- Real paths spend a median 64% of their pre-capture time in B and then leave it. B is where the window abstraction
  fails: adversarial content behind the window can keep a state in B for ever, as §45 found.
- So the whole capture gap is now a statement about B: **a real evolution cannot stay in the bad core for ever.**
- This sharpens GPT's target. The history condition need not fix the whole path. It only has to show that B's
  avoiding cycles need behind-window content that an actual row cannot keep supplying.

### 52.3 The depth guard for A (L1333), predictions written before the run (`funnel_attractor.py --guard`)

GC2398 does not accept §52.2's unqualified "capture is exactly leaving B" until the depth guard is settled. The window
over-approximation is sound only while every update's outputs lie at depth ≥ 2, that is, while R ≥ 10. Capture's
robustness lemma needs entry into S_E at R ≥ 12.

For each state v of A, define two quantities over its paths to S_E:
- **F(v):** the largest fall below the starting depth. F(v) = max over edges (v → u, advance a) of −a + max(0, F(u)),
  with F = 0 on S_E.
- **G(v):** the largest net fall at the entry into S_E.

Then **a front at state v ∈ A with depth R ≥ max(10 + F(v), 12 + G(v)) is captured within rank(v) ticks**, whatever lies
behind the window. The advance of an edge is recovered from its classes: a ≡ −21 (c′ − c − 1) (mod 1024), since 195 ·
(−21) ≡ 1.

**Predictions.**
- **G1.** max F over A ≤ 20, so a uniform guard "R ≥ 30" suffices. Lean 60%.
- **G2.** Every one of T48's 200 real entries into A satisfies its state's guard. Lean 90%.
- **Counterfactual.** If some A states can fall by tens of cells, the guard is state-dependent and large, and real
  entries near the prefix could violate it.

### 52.4 Results: the guard is 16 ([output](../tests/probes/funnel_attractor.out), second section)

- **G1 HELD.** Over A the largest fall on the way to S_E is F = 6. The largest net fall at entry is G = 4. A's edges
  have advances from −8 to +2.
  - The printed median of max(10 + F, 12 + G) is 9. It does not clip F at 0, and F is negative when every path rises at
    once. The correct requirement, max(10 + max(0, F), 12 + G), has maximum 16 either way.
- **G2 HELD.** All 200 real entries satisfy their state's guard, with least margin 64.
- **The qualified dichotomy (P1024, W = 8).**
  - **The finite part (COMPUTED, M5):** every state outside S_E lies in A or in B, every state of A has F ≤ 6 and
    G ≤ 4, and ranks are ≤ 113.
  - **The transfer (PROOF-SKETCH, a carrying read requested):** it is GC2386's over-approximation argument, applied to
    paths of A instead of S_E. A real front whose 8-cell state lies in A at depth R ≥ 16 stays at depth ≥ 10 while it
    follows A's edges, and enters S_E at depth ≥ 12 within 113 ticks, whatever lies behind the window. From there
    GC2386 applies.
  - So a real front at depth ≥ 16 is captured exactly when its 8-cell state ever leaves B.

*GC2403 / L1335.* GPT's weighted guard H(v) = max(0, max over edges (H(u) − a)), with H = 0 on S_E, is the same
recursion as F above, clipped at 0. Under a 12-floor at every tick it gives **R ≥ 18** (max H = 6), and it is carried
as the record's form. L1332's "entered A at depth ≥ 80" was unlogged; the logged margin gives ≥ 74.

## 53. What decides the exit from the bad core? (T49, L1334)

### 53.1 Predictions, written before the run (`funnel_attractor.py --exits`)

**Structural fact (by definition).** Every state v of the bad core B has an edge into B. So when a real front's state
leaves B (into A or S_E), at least one branch of v (a choice of the two unknown cells R − 9, R − 10, or of the free
cells after a retreat) would have stayed in B. **Every exit from B is decided by cells beyond the 8-cell window.**
Capture is always triggered from outside the window.

**Question.** Which cells decide it in real runs?
- The two cells just beyond the window, on a move with advance ≥ 0. Then no window cell is freed.
- Or cells drawn in by a retreat.

For each real exit tick (P1024, W = 8, the 200 rows of T48) the record is:
- the advance of the real move;
- how many of v's (unknown-pair, free-bit) branches lead into A ∪ S_E against B;
- whether the exit depended only on the unknown pair. It does when every branch with the real unknown pair leaves B and
  some branch with another pair stays.

**Predictions.**
- **X1.** At least 80% of real exits happen on moves with advance ≥ 0, decided by the two cells R − 9, R − 10. Lean 60%.
- **X2.** At a typical exit, at most half of v's branches stay in B: the exit is likely given the window, not a rare
  choice. Lean 50%.
- **Counterfactual.** Exits mostly on retreats would mean capture is triggered by deep cells pulled in by the front's own
  fall, which is a longer history.

Record searched: §52 (A, B, the guard), §45 (bad core), T45 (reading depth); exits from B not measured before.

### 53.2 Results ([output](../tests/probes/funnel_attractor.out), third section)

- There are 166 real exits from B: 34 of the 200 rows were already outside B at their first tick with R ≥ 12.
- The real advance at the exit is 0 in 76, +1 in 22, −1 in 43 and −2 to −6 in 25.
- **X1 split.** The exit was decided by the unknown pair (R − 9, R − 10) alone in 134 of 166 (80.7%): every branch with
  the real pair left B, and some branch with another pair stayed. That part held. But only 98 of 166 (59%) exits came on
  moves with advance ≥ 0, so the "advance ≥ 0" part is REFUTED. 41% came on retreats, mostly by one cell, where the
  freed window cell is also beyond the old window.
- **X2 HELD (at the boundary).** At the exit state, a median of exactly half of v's branches would have stayed in B.

**What T49 teaches.** Capture is triggered from just beyond the window. In four exits out of five, the two cells 9 and 10
behind the front decide it, typically while the front stalls (0) or steps back by one. Those two cells' values are where
actual history enters the capture event. For GPT's compatibility condition, the question is whether the pair beyond the
window can be held, tick after tick, at values that keep v in B. That is the whole question of the bad core.

### 53.3 Logged depths (L1337), predictions written before the run (`funnel_attractor.py --guard --depths`)

GC2403/GC2404 asked that actual entry depths and the minimum depth to capture be logged, not inferred. Same 200 rows (Random(48)).
- **D1.** The least depth at first entry into A is ≥ 60 (the front starts near K − 1 = 79, and the early drawdown is ≤ 11).
  Lean 85%.
- **D2.** The least depth between entry into A and capture is ≥ 60 as well, far above the guard of 16 (or 18). Lean 85%.

**Results (fourth section of the output).** **D1 and D2 HELD.** The first entry into A is at logged depth min 72, median
128. The least depth from that entry to capture is also min 72, median 128: no real front fell below its entry depth on
the way to S_E. This replaces the inferred figures of L1332 and L1335 with logged ones. They lie far above the guard (16
or 18).

## 54. Does the dichotomy survive a longer window? (T50, L1338)

### 54.1 Predictions, written before the run (`front_closure.py P1024 10 --all-theta`, `funnel_attractor.py ... 10 --core`)

**Question.** At W = 8 the window automaton splits exactly into S_E, A (forced into S_E) and the bad core B (§52). At W =
10 the window holds the two cells that decide most exits (T49). Does the split stay exact, and does B shrink as the window
sees more of the real history?

**Setting.** P1024, W = 10: 1,048,576 states. S_E^all at W = 10 is built from the clean starts of all 1,024 θ. B is
computed independently as a greatest fixed point (FAIL branches are not edges), A as before, and the guard and logged
depths as in §52–53. The same 200 rows (Random(48)).

**Predictions.**
- **E1.** S_E^all at W = 10 is robust (FAIL-free, every 3-path advancing), with between 300 and 600 states. Lean 80%.
- **E2.** The split is exact again: S_E + A + B = all states. Lean 75%.
- **E3.** B stays large, at least 75% of the automaton, because retreats into unseen cells still give arbitrary fuel
  (C1, §45). Lean 65%.
- **E4.** All 200 real paths enter A, and their lead before capture is longer than at W = 8 (median > 26). Lean 55%.
- **Counterfactual.** If B shrinks sharply with W, the window abstraction converges towards real dynamics, and a finite
  W might certify capture for all but a small core. If B stays large, history beyond any fixed window is essential.

Record searched: §45 (C1 bad core at W = 8 only), §52–53; W = 10 not computed before.

### 54.2 Results ([output](../tests/probes/funnel_attractor.out), fifth section)

| | W = 8 | W = 10 |
|---|---|---|
| states | 262,144 | 1,048,576 |
| S_E^all (robust, every 3-path advances) | 389 | 508 |
| attractor A | 42,033 (16.0%), ranks ≤ 113 | 258,006 (24.6%), ranks ≤ 200 |
| bad core B | 219,722 (83.8%) | 790,062 (75.4%) |
| S_E + A + B | all | all |
| real paths: lead from first A state to capture, median / 90% / max | 26 / 57 / 111 | 33 / 82 / 115 |
| share of pre-capture time in A, median | 0.36 | 0.49 |
| first entry depth into A (logged), min / median | 72 / 128 | 72 / 124 |

- **Control.** At W = 8, B computed independently is 219,722, exactly T42's bad core, and the split is exact.
- **E1 HELD.** S_E^all at W = 10 has 508 states. It is FAIL-free, every 3-path advances, and the largest fall is 1. All
  1,024 θ share one 52-state clean set again.
- **E2 HELD.** The split is exact at W = 10 too.
- **E3 HELD, at the boundary.** B is 75.4%: still large, but shrinking (83.8% → 75.4%), and A grows (16.0% → 24.6%).
- **E4 HELD.** All 200 real paths enter A, earlier: the median lead is 33 against 26, and the time in A is 49% against
  36%.
- **The guard at W = 10 (corrected by hand).** The printed "required depth" uses W = 8's floors (10 on the way, 12 at
  entry). At W = 10 the floors are W + 2 = 12 and W + 4 = 14, so the requirement is max(12 + max(0, F), 14 + G) ≤
  max(20, 21) = 21 (F ≤ 8, G ≤ 7). The logged real entries (min 72) clear it by at least 51. No alarm.

**What T50 teaches.** The dichotomy is structural, not an accident of W = 8: at both widths, every state is forced into S_E
or can avoid it for ever. A longer window moves about 9% of the states from B into A, and real fronts reach the forced
region earlier. So the window abstraction converges towards the real funnel as W grows, but slowly. Retreats into unseen
cells still feed B (§45), so B cannot vanish at any finite W. The rate at which B's share falls is the measurable trend.
W = 12 (4.2 million states, about two minutes) would give a third point.
