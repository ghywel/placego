---
Template: ComputationalEssay
Name: Rule 30, the picture so far: a map of the partial results by object, with the connections between them
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-03
Description: A synthesis of the Rule 30 Prize portal and kit: every proved partial result placed by the object it is about and the frame it lives in, the exact connections between results of different contributors, what is still missing said once, and a reading guide; with one new bridging theorem on the left diagonals as the entry's Lean content
Abstract: See abstract.txt.
Keywords: [rule 30, Rule 30 Prize, synthesis, map, left-permutivity, OR masking, odometer, zero boundary, diagonals, ether, fronts, Lean, partial results]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)", "[Rowland, Local nested structure in rule 30](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf)", "[Jen, Global properties of cellular automata](https://doi.org/10.1007/BF01010579)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[The kit's Rule30LeftReset](https://github.com/WolframInstitute/Rule30PrizeKit/blob/c42f6e5133f61a47e99289fd4b6e0536fd8a0453/lean/Ruliology/CellularAutomata/Rule30LeftReset.lean)"]
---

## 0. Why a map

At 3 November 2026 (18:49 GMT) the portal listed 119 entries by some fifteen first authors, 117 of them Lean Verified, and the
kit's main had 195 modules. The portal collects submissions at different stages of verification; this essay cites entries by id and
author, saying for each whether it is Lean Verified on the portal, a kit module, a locally checked result whose public check is
pending, a computation, or a result of the record not on the portal; the appendix places every entry of the listing. Almost
every one was proved by one party on its own question. Reading them together, they are
not scattered: they are about a small number of objects, in three coordinate frames, and they rest on two consequences of the
rule. This essay says which object each result is about, how results of different contributors connect, what the whole leaves
open, and where to start reading. Its own Lean content is one bridging theorem (section 7); the rest is a reading of everyone's
work, cited by portal id and author. The three-week record behind it is public.

## 1. One rule, two mechanisms, three frames

Rule 30 is *new = left XOR (centre OR right)*. Two consequences carry everything proved so far.

**Left-permutivity.** Toggling the left input toggles the output, and *left = new XOR (centre OR right)*: the left neighbour is
recovered from the next row and the right pair, so the whole history to the left of two adjacent columns is determined by those
two columns (Jen 1986; the kit's `Rule30Jen` and its masked and windowed forms). A difference between two rows that has a
rightmost cell travels right at exactly one cell per step, unconditionally: the rightmost discrepancy moves one cell right every
tick, because at that cell only the left input differs. A difference with no rightmost cell has no such edge.

**OR-masking.** The right neighbour enters only through *centre OR right*: a black centre masks it, a white centre passes it. A
change travels left only through white cells. The portal's names for this are the nine-black shield, the ether-and-wall traps,
the vacuum and strip certificates, and the forced bits of every sideways front.

**Three frames.** (A) The lab frame: the centre column and its neighbours; Problems 1 and 2 live here, and every word exclusion
and run bound. (B) The right-edge frame: a finite row read from its rightmost black cell is an integer, one step is the
T-function Φ(a) = a XOR (2a OR 4a), a permutation of Z/2^n for every n, the 2-adic odometer; the right diagonals R_j are its
coordinates, each periodic with period 2^(e_j). (C) The wall frame: the left half beside a white wall, F(Y) = ⌊Y/2⌋ XOR (Y OR 2Y)
(Bosdure, 317c64; the kit's `Q01_iff_integer`), which is Φ with one bit discarded per step; Q01, the period-2 case of Problem 1, lives here. A fourth coordinate
system, the left-edge frame of the left diagonals D_k (Rowland), is the mirror of (B) and is where this essay's own theorem sits:
the same three-input recurrence as the odometer's with the cell's own value moved from the linear slot into the OR, which is why
one end keeps everything and the other forgets everything but a few branch choices (section 3.6).

## 2. The map of statements, by object

Each paragraph names the object, then the results about it with their authors and ids, in the order a reader should take them.
Our own entries are marked "ours"; the full list of ours is in the record's map; the appendix (section 8) places every entry of
the portal, one line each.

**A. The centre column (frame A).** Problem 1 is equivalent to "no word is an eventual tail" (the kit's `problem1_iff_no_word`),
and every exclusion on the portal has one shape: a periodic centre forces, through a finite relaxation of the cells to its right
that is closed under the word's steps, the next column to be periodic at some phases, and Jen forbids it. Closed families: black
runs 1^r u with 9⌈(P − r)/4⌉ ≤ r (Bosdure, 317c64), 11 0^q for q ≥ 8 (Norris, c5e3c0), white-padded tails 0^r v 011 for
r ≥ 10|v| + 41 and all sixteen six-bit black-ended cores at r ≥ 74 (Lowry, 8fe04c, 524848), 0^q 10111 for q ≥ 9, 0^9 1 and
0^7 1011 (AIOvernight, 7a9ed3, 521830), the white end 1 0^q for q ≥ 10 in every column of every leftmost-black row (ours,
c27323, ported to the kit as `Rule30WhiteEnd`) and from q = 9 for the seed by one pumped certificate (AIOvernight,
c389d5, `Rule30WhiteEndNine`, on top of ours), a four-category block grammar and mixtures of short blocks before long white runs
(AIOvernight, d611aa, 4d375d, 196859), explicit word lists (the kit's strip certificate table; AIOvernight's 87 words of lengths
12 to 16, 7a9ed3; ours of lengths 11 to 18 beyond the kit's table, 5e2b66, f7ace9), run bounds for Problem 2 (Morales, 03b551:
a black run from time a has length at most a, a white one at most a − 3; Goux, 0554f7: 5L ≤ 3a + 10; Villafuerte, e34744:
L ≤ a − 2 for a ≥ 4; AIOvernight, e324b6: explicit log log margins; the black centre times growing at least like log base 8/5, improving the kit's
log₂, AIOvernight, 452bbf), an exact cylinder count for the white centre times with a black right neighbour (AIOvernight,
b476c1), white runs of a row beside two periodic columns at most two
periods long (ours, 8131b1), single-pair parity
barriers for white centre runs and constant diagonals (Quint, 462dc9, extending AIOvernight), sublinear windows that contain both
centre colours (Quint, 1c93e6), parity-resolved boundary collisions with black-run erosion bounds (Quint, 1a6e64), and defect
escape budgets (Quint, e742c0, on Lowry's `Rule30DefectClockBudget`). Not covered: every word with no run of nine and no long white padding, in particular
every word of period 2, 3 or 4, which is why those go to frames B and C.

**B. Period 2 (frame C and its coupling).** Under the clock 0101… the centre passes nothing to the left half, so period 2 reduces
to Q01: no finite start beside a white wall keeps depth 1 black at every even time (the kit's `Rule30PeriodTwo` and
`Rule30ZeroBoundary`, with `Q01` in its integer form from Bosdure, 317c64). Known: every start of width ≤ 56 dies, with exact
death times 96 at width 52 and 100 at width 56 (the kit's `Rule30ZeroBoundaryWidth52`; ours, 8e6bd3, ac3898), the same at width
60 with death time 114 (ours, 71f858, kernel-checked locally, public check unverified), and lower bounds to width 76 (ours,
b16332, a129c3, 4dcf69); the constrained starts of width W counted exactly as 2^⌊W/2⌋ (the kit's `count_constrained`) and, separately, under an
eventual alternating centre, the odd-time column −1 bits avoiding 00 and 11111 (the kit's `free_bits_no00_no11111`); a width-d death bound forcing a black cell in every row whose column −1
matches a pattern (e67465, "Partial structural results toward Rule 30 Problem 1", whose byline is garbled on the portal); four-cell stripe tails after an alternating stripe reaching a white depth-1 even time at most 31 steps after their first
deviation, except the tail 1011 with odd stripe length (yingy, 81df0e; Quint's later unconditional mortality, 017d83, is a
separate result); the stripe-tail mortalities, backward wave cascades, clone rays and transducer hierarchies of the zero-boundary
half (Quint, 017d83, 1910d0, 5beddc, a4691a, c6ff55, 8abb51, 715db1; the stripe cascade, f0127e); the right neighbour of a
clocked centre never a Sturmian word (ours, 8084e6), never a finite-arc rotation code with late large partial quotients (ours,
0ef6e2), never a mechanical word beyond an explicit horizon (ours, dc3d17), and never with near-squares at unbounded scales
(ours, 91b0b0); at most 0.2445 bits of information per visible bit at width 14 (ours, 4767e0, 4d1a54); the empty right half's
gate with gaps 3 or 5 from step 146 on (Bosdure, 230bc7; the kit's `Rule30GateTrap`), the one-cell right half's gate with gaps 3
or 5 at all times and the seven-gap word 3535353 excluded (Lee, 60990f), two infinite families of right halves absorbed by the
ether (ours, 8d7751), white corridors and drought clocks of recurring right germs (Quint, 6824d5, 75bd53, on the kit's
`Rule30CoupledGerms`); a centre alternating from time zero needing a left prefix of weight at least 17 (AIOvernight, 60d213),
and finite-support exclusions for eventually simple adjacent columns (Elbaz, 99db76, 23ac1b). Quint's conditional reductions of
November: the frontier-to-left-diagonal conjugacy (121ada), small-RW proved and dropped from the chain while the period-two
conclusion still assumes BWH (f48894, PR 84, open), the budget-mortality equivalence with its all-budget premise (b8e784), a
left inverse of the stream map (bf1582) made two-sided with separators for words of length at most 3 (bfefea, PR 101), period
preservation under an idempotent block on a finite interval (924d87), the all-step terminal pin (d6e898) and two-step absorbing
preservation (e1cb85). PRs 83, 85, 86 and 87 are closed unmerged as pull requests, but their modules are on the kit's main and
their entries carry the kit-contribution tag: adopted source, not pending work. The sibling rule 210 shares the count and has
Q01 false (ours, 920c1b, 1bf4dc): the counting cannot decide Q01.

**C. Periods 3 and 4 (frame A's right half under a periodic driver).** The period-3 ether erodes, so it has no wall of any width
(Morales, 1fc962, in the kit as `Rule30EtherThreeErosion`); Q001 holds to width 37 and its period-5 analogue to width 28
(giraudsa, 0cac94); the truncated period-3 ether breaks the 011 pattern for an infinite family of left starts (Jiménez Martínez,
29bcb9); CQEmpty holds for the three period-4 words and for 001 (Villafuerte, e34744). Period 4 reduces to absorption into the
ether-and-wall family (the 7×4 ether, its 109-state wall and the traps are the kit's `Rule30Ether`; Absorption is open): the
single-cell right half at every position and phase, and every right half supported above 30, are absorbed (Elbaz, b572b3,
a02087); the weaker `Lock w` suffices and is in the kit (Bosdure, c137e0, kit PR 65); the ether episode behind a black edge has
an exact length (ours, 7c1f96, `Rule30EtherEpisode`, on Lowry's eight-tick ether, which no black-edge code follows eventually,
Lowry's `Rule30EtherGrounding`); and an edge inserted into the classic ether is pinned for ever, front speed exactly zero (ours,
A1, 3742dc, built on the kit's trap). The coupled witnesses with a periodic left half and a finite right half read the period-4
word from time 0, so the finiteness of the left half cannot be weakened to periodicity (Bosdure, c137e0).

**D. The diagonals (frames B and its mirror).** *Right:* R_j has period 2^(e_j) from the start, doubling exactly when a
prescribed cell is black (the kit's `Rule30Diagonals` and `Rule30RightPeriods`, with the rows at powers of two); e_j ≤ j/2 +
O(log* j) (AIOvernight, 1b82d8, in the kit as `per_upper_half` and `Rule30RecordCharge`); the doubling word's forbidden factors
and closing law (ours, 20f058); for every finite seed the right diagonals after the first equal adjacent pair have least periods
4, 8, 8, 16, 32, 32 (ours, 3ca86f); the 101 shift law and its mod-4 forms (ours, 7d47a9); periodic temporal profiles (ours,
a94f21); a finite-depth right edge follows the single cell's ruler with a cap, and staircases near it end (ours, 61e435, 196370);
half-rate prefix clocks for every two-input gate and their nested thresholds (ours, 7b0d12, 9861e5); stroboscopic alternation,
half-black balance and synchronized wall returns (Quint, efd2bd); the fresh digit at each doubling depth is equidistributed,
the binary cube inside the cone (AIOvernight, 84a42c). *Left:* D_k is eventually periodic with period dividing 2^k
(the kit's `Rule30Diagonals`); the periods are unbounded, with infinitely many eventually white and eventually black diagonals
and no two adjacent eventually white, for every configuration with a leftmost black cell (ours, 0616de, 22 October, after
Rowland 2006 §5; for the seed, by a different encoding, AIOvernight's `Rule30LeftUnbounded`, 28 October); the period divides
2^(whiteCount) by the reset law (AIOvernight, `Rule30LeftReset`); eventually-white diagonals at least five apart (AIOvernight,
`Rule30WhiteSpacing`); the exact transient-front reset law (AIOvernight, `Rule30FrontLaw`); a settled band of diagonals admits
no long white run, and a centre repeat cannot put its white run inside it (ours, 0616de, 1d5070); on those modules, Quint's
November extensions: infinitely many antiperiodic left diagonals with exact half density (5da074), complement discrepancy and
odd-stride half density (750fd6), whiteCount(j) ≤ j/2 with eventual period dividing 2^(j/2) (0ad6ff), quantitative whiteCount
and next-settled-diagonal bounds (0a9bde), the gap-five white-pair classification (0d8a71), small-depth front bounds (050b68; its
public abstract states an onset of −10 and the PR head a stronger −27 for k ≥ 5, so cite the declaration, not the title),
two-diagonal period descent and the nine-diagonal white-reset neighbourhood (0f0c09), and twin-diagonal conservation after a
white with the right-diagonal discrepancy (0f4b7a); exact defect spectra of the first left diagonals (Villafuerte, e34744). This
entry's theorem (section 7): once two neighbouring left diagonals have settled with a common period and the nearer one is not
all white, the next one's cycle is forced, the map is affine and invertible in the farther neighbour, two consecutive settled
cycles determine the one before, and a diagonal is eventually white exactly when its two neighbours have equal cycles, which
happens two diagonals after the grandparent equals the parent's derivative. [Rowland's question of one left side: the record's
§8.31, not on the portal: cite as prior work.]

**E. Fronts, walls and backgrounds (all frames, new in November).** The rightmost cell of a difference moves right at exactly
one cell per step, and the leftmost at a speed set by the background: zero on the classic ether (ours, A1, 3742dc:
kernel-checked locally; the portal's public check timed out and the maintainer's rerun is pending), exactly 5/19 on the ring
background 100100000 and exactly 2/9 on 1010000 (ours, A4, 87ba7a, superseding 37281a: moving walls, certified by closed sets
with an exact potential, at the entry's stated alignments and under its closure-entry and arbitrary-tail guards), exactly 1/2
on the eight-tick ether G8 (COMPUTED, not a theorem: the record's CL678, five alignments of 6,000 steps), about 0.246 on the
recorded fair-row samples (measured: 0.2468 in eight 8,192-step single-flip trials, the record's §8.66, and 0.2457 ± 0.0084 in
five 6,000-step inserted-edge trials, CL678, the error being the script's standard error over five samples, not a proven bound;
the damage-spreading speed of the physics literature); for every background and every perturbation confined to one
side, at most 1 minus the background's recruitment climb rate (ours, A2, e660e4, a universal healing bound); and behind a black
edge, a periodic background's episodes are finite at every depth exactly when no eternal point follows it from some depth on
(ours, A5, d37d24, section 3.7). Triangular left-permutivity with guarded light-cone sensitivity (Quint, ea30e7) is the related
prior work for A2, and defect escape budgets from a bounded rank (Lowry, `Rule30DefectClockBudget`; Quint, e742c0) the related
work for the moving walls.

**F. Structure and barriers.** The XOR of two histories is a history only trivially (AIOvernight, ddbfbd, in the kit as
`Rule30XorRigidity`); every density conserved by four steps on every window is a coboundary, so there is no additive local
conservation law of that kind (Lowry, `Rule30LocalConservation`; the excluded class is additive window densities conserved by
the stated steps, and monotone ranks, non-additive and clock-dependent potentials stay open, as Lowry's own
`Rule30DefectClockBudget` uses such a rank); distinct columns of the seed differ by time max(|p|, |q|) + 18 (Lowry, ad6cac);
two rows with edge −3 that differ at −1 have identical centre traces and merge after one step, so no horizon depending on the
left depth alone recovers the left half, while `EdgeObservable`, that equal infinite traces of finite rows imply equal left
edges, is open and would give Problem 1 (Lowry, `Rule30TraceMerge`, `Rule30TraceAmbiguity`, `Rule30TraceEdge`, with the
observer and gauge criteria of `Rule30DividedDifference` and `Rule30CommonGauge`); three edge pairs told apart from the centre
column by exact deadlines (ours, 991a71); Jen's left-permutive class is exactly rules 90, 150, 210, 30, and 30 is the only one
with a non-eventually-constant centre (Quint, 7e9e6e); the periodic points of every frame with velocity in [−1, 1) are the
kit's `equivalents/PeriodicPoints`, and at velocity +1 the periodic rings are closed walks of periodic profiles (ours, a96cee);
the finite past of finite rows has a unique root and age, a parent test and exact parent counts (ours, 803bc4); for t ≥ 2 the
t-step centre map, as a Boolean function of its initial cone, has degree 2t − 1 (the kit's `equivalents/AlgebraicDegree`;
Norris, 603218, packages degree, the unique top monomial and Walsh balance for t ≥ 3), and Condrey's `Rule30TopCoefficient`
gives a separate parameterized top-coefficient identity for quadratic left-permutive rules; the rule's causal logic as an ANF
census (Quint, 075afb); an eight-cycle obstruction rules out nonzero nonnegative rewards on proper subsets of the four-cell 1001
window in a rational 16-cell potential inequality, and a separate return of the seed's 16-cell state excludes an exact
coboundary for that indicator (AIOvernight, 4b2a58). Together: a proof of Q01 must
use the OR's nonlinearity beyond its counting consequences, must use the finiteness of the left half beyond its periodicity,
and cannot rest on an additive local conservation law; whether a non-additive or clocked potential exists is open.

**G. Problems 2 and 3.** Problem 2 is equivalent to its Cesàro, Abel-mean and simple-normality forms (Norris, 603218; the kit's
`equivalents/`), to one nearly geometric sequence of nearly balanced scales (Elbaz, 5105a7), and to the balance of the centre's
OR-event parities split by the settled part of its past diagonal [the record's C4 bridge, not on the portal]; diagonal energy
bridges and conservation laws for it (Quint, a2fefb, eb2e05). Problem 3 has its formal forms (the kit's `equivalents/`), the
degree, Walsh and query bounds (Norris, 603218), and Quint's series: head-cone locality and step lower bounds (b58e66, 781b70),
scans-below / right-span bounds with a halting collapse (18ba2f), tape invariance on dyadic rays (c646f6), canonical-window
bounds and light-cone triangles (fefa7e, a535cf), and trajectory injectivity with periodic deciders (fee9ad).

## 3. The connections

**3.1 Problem 1 is one implication chain.** A periodic centre makes the left half a function of columns 0 and 1 (left-permutivity),
so column 1 must be non-periodic (Jen), so the right half driven by the periodic centre must keep its first column non-periodic
for ever. Every exclusion in A and C shows the opposite for one family of drivers. The open cases are one question: for which
periodic drivers does a finite right half always lock its first column? Period 2 is the exception: under the clock the right
half's first column is starved, not forced, and the finite left half must die, which is Q01 (B).

**3.2 "One bit per two cells" is one number in four places, not yet one theorem:** the constrained starts' free odd depths (the
kit), the sideways row above a sinking front, the half-rate bound on the right-diagonal exponents (AIOvernight) and the death-time
model share the rate one half. They are four different quantities (a count of starts, a row's free cells, an exponent bound, a
fitted model), and no map identifying them is written down. The mechanism we can name in each is left-permutivity in a triangular
frame: each step exposes one new bit, and a constraint made every second step pins every second one. What is not a theorem
anywhere is the matching lower bound, that the freedom is used, nor any identification of the four.

**3.3 Alternation is the one rigid periodic structure in every frame:** the fixed stripe of the zero-driven left half (the kit's
`Rule30PeriodTwo.stripe_fixed`), what long black runs leave behind (the kit's `black_shield`; Bosdure, 317c64; Norris, c5e3c0),
the only odd 2-cycles of the edge map (ours, 196370), the rings with Φ²x = x (ours, a96cee), the collapse of a gated 32-step
return to a 2-step one (Lee, 0ef9c8), and the ether of period 4 seen in a moving frame.

**3.4 The merges are one phenomenon:** F = Φ ≫ 1 says the wall frame is the invertible edge frame with one bit discarded per step;
the trace merges and ambiguities (Lowry, `Rule30TraceMerge`, `Rule30TraceAmbiguity`), the prefix merger beside the wall (ours,
352e5d) and the forgetting front are that leak seen from different sides, and `EdgeObservable` (Lowry, `Rule30TraceEdge`) asks
whether the centre trace of a finite row still determines its left edge.

**3.5 Two capacities, not yet one language:** the channel bound at width 14 (ours: a finite upper bound of 0.2445 bits per
visible bit at that width, not an all-width rate) and the empty right half's gap shift (Bosdure) count related symbols; the
width-14 bound sits about 4% below the gap shift's entropy, a comparison of two numbers. Whether the two describe one language,
and what the gap means, nobody has written down as a theorem.

**3.6 The two ends are one recurrence.** The right diagonals obey d′ = d ⊕ (u ∨ w) and the left diagonals d′ = w ⊕ (u ∨ d): the
same three-input recurrence with the cell's own value moved from the linear slot into the OR. On the right the cell integrates at
every tick and never forgets: the odometer, with periods observed to grow like 2^(0.41 j) (the doubling density is measured: about 0.42 on the seed's right diagonals
through j = 92, 0.407 ± 0.009 for the prefix block-exponent increments of 64 odd 24-bit seeds at n = 13 to 56 (CL642, CL645),
and the kit's own note e_j ≈ 0.43 j; finite scopes, not an asymptotic law; the proved bound is e_j ≤ j/2 + O(log* j)). On the left the cell is reset at every black of its nearer
neighbour and integrates only when that neighbour is all white: the settled cycles are forced (section 7, under its guards: a
common period and a nearer cycle that is not all white), the period grows only at an eventually-white diagonal, by the odd-weight
test (Rowland's Proposition 2; AIOvernight's reset law), and a white diagonal is a coincidence of consecutive cycles (section 7).
How often that coincidence occurs along the seed is measured, not proved: for a fixed nearer cycle exactly one of the 2^p farther
words produces it, a count in the pair space, not a law of the seed's path. The kit's bound 2^(2P) on the next non-P diagonal
(AIOvernight) is the size of that pair space; the pair map itself is a partial bijection between pairs whose second member has a
black and pairs whose first member has one, not a permutation. The centre column sits between: it reads each right diagonal
once at birth and each left diagonal before its neighbours settle, which is why nothing proved about either end reaches it yet.

**3.7 The velocity spectrum and the episode bridge.** A1, A2 and A4 (ours) and the kit's ether results are one object: the
leftward speed of damage as a function of the background. The episode length behind a black edge (ours, `Rule30EtherEpisode`) and
the bridge "no eternal point of any period follows a periodic background from some depth on iff the longest episode at every
depth is finite", with its finite criterion at the horizon lcm(2^B(k+2), p) (ours, A5, d37d24, `Rule30EpisodeBridge` in kit PR 116; the
bridge was proposed in the record, CL676), connect that object to the eternal points of the edge map: a background that ends every episode
hosts no eternal wall.

## 4. What is still missing, said once

Problem 1 needs, for every periodic driver, that a finite right half locks its first column, except at period 2 where it needs
the finite left half to die; Q01 needs a mechanism that is nonlinear, uses finiteness, and is not an additive local conservation law (F). The frames supply two
mechanisms no theorem uses yet: the leak F = Φ ≫ 1, and the odometer's rigidity (3.3). Problem 2 needs the balance of a parity that
grows with time, which no fixed-order fairness test can give. Of the measured constants, the fair-row front speed about 0.246 (0.2468 in eight 8,192-step single-flip trials, §8.66; 0.2457 ± 0.0084
in five 6,000-step inserted-edge trials, CL678), the right-edge doubling density about 0.42 (the seed through j = 92; the prefix
block-exponent increments of 64 seeds, CL642 and CL645; the kit's note) and the left-end period law "P reached near 2^P" (the seed's first 12,000 left diagonals and random finite
seeds) are conjectures with stated samples: they have mechanisms but no theorems; the centre
column itself passed the five generic tells we ran on its first 8,192 cells (block entropy to order 10, linear complexity of a
2,048-bit window, the 2-kernel, autocorrelation to lag 64, residues mod 8), as did random finite seeds, while Thue–Morse,
Rudin–Shapiro and a 31-bit LFSR failed them.

## 5. A reading guide

For the centre column: the kit's `Rule30StripCertificates` (`problem1_iff_no_word`) and its certificate table, then Lowry's
8fe04c and 524848, AIOvernight's 7a9ed3, 521830 and d611aa, Norris's c5e3c0, Bosdure's 317c64, Morales's 03b551, Villafuerte's
e34744. For period 2: the kit's `Rule30PeriodTwo`, `Rule30ZeroBoundary` and `Rule30PeriodTwoSideways`, ours 8e6bd3, 4767e0 and
8084e6, Bosdure's 230bc7, Lee's 60990f, Quint's 5beddc, f0127e and the November reductions (121ada, f48894, b8e784, bf1582,
924d87, bfefea). For periods 3 and 4: Morales's 1fc962, giraudsa's 0cac94, Elbaz's b572b3 and a02087, Bosdure's c137e0,
Jiménez Martínez's 29bcb9. For the diagonals: the kit's `Rule30Diagonals` and `Rule30RightPeriods`, ours 0616de, 3ca86f, 7d47a9
and 20f058, AIOvernight's 1b82d8 and the five left-side modules, Quint's 5da074, 0ad6ff and efd2bd, and this entry. For fronts
and backgrounds: the kit's `Rule30Ether`, Lowry's `Rule30EtherGrounding`, ours 7c1f96, 3742dc, e660e4, 87ba7a and d37d24. For
structure: ddbfbd, `Rule30LocalConservation`, `Rule30TraceEdge`, 7e9e6e, 603218, a96cee, 803bc4. For the problems' equivalent
forms: the kit's `equivalents/`, Elbaz's 5105a7 and Norris's 603218; for Problem 3, Quint's 18ba2f. Every entry of the listing is
placed in the appendix (`entries-by-object.md`).

## 6. How to add to the picture

This map is one reading of the catalog and the portal, offered to their contributors. The catalog remains the authority on what
is proved, and what belongs in it is its maintainers' judgement, not ours. A new entry can place itself in one line: the object
(A to G), the frame, the two nearest entries it extends or contrasts with, and what it leaves open. The record behind this essay
keeps this map current and will cite contributors who tell us where their result sits; corrections to any placement or
attribution here are welcome and will be made.

## 7. The entry's own theorem: the settled left diagonals form a reversible recurrence

Built in our record (L1474, L1476) as `Rule30LeftCoincidence` on the kit's `Rule30LeftReset`: 180 lines of core Lean with
standard axioms and ten headline theorems; the kit's Check and the portal Check pass (37 constants), and GPT read the
actual source (GC2583, GC2587). The portal form and its checks follow this section. For any three words with x(t + 1) = a(t) ⊕ (b(t) ∨ x(t)),
a child x driven by a nearer word b and a farther word a, in natural time:

- **F1, the closed form** (`closed_form`): after a black of b at r and a white run of b on (r, t], x(t + 1) = ¬(a(r) ⊕ ⋯ ⊕ a(t)).
  With r the last black of b at or before t this is the record's cyclic statement for periodic words; the reset value at a black
  is x(r + 1) = ¬a(r).
- **F2, recovery and uniqueness** (`farther_of_child`, `farther_unique`, `solutions_agree`): a(t) = x(t + 1) ⊕ (b(t) ∨ x(t)) for
  every t, so the farther word is determined by the child and the nearer word, for any triple; and two children of the same a
  and b agree from s + 1 on once b(s) is black. The kit's `reset_periodic` proves that a child of periodic farther and nearer words is
  itself periodic from the first black of the nearer word on; with it, the hand argument of the record (GC2550) gives the
  bijection between periodic farther words and periodic children whenever the nearer word has a black. The module has no
  standalone cyclic-bijection theorem: its results are arbitrary-word statements in natural time, and the D instances are for
  the single cell's diagonals.
- **F3, the coincidence criterion** (`coincidence_iff`): if b(s) is black, then x = b from s + 1 on if and only if
  a = b ⊕ shift(b) from s on. No periodicity is needed; the cyclic form follows.
- **On the left diagonals** (`D_closed_form`, `D_farther_of_child`, `D_coincidence_iff`, `D_white_of_coincidence`,
  `D_evwhite_iff_eventually_eq`, through the kit's `D_step` with child
  D(j + 2), nearer D(j + 1), farther D j): after a black of D(j + 1), D(j + 2) coincides with D(j + 1) exactly when D j is the
  difference of D(j + 1). A white diagonal forces its two parents to coincide (the kit's `D_white_of_eq`), and coinciding
  parents force a white child from the next black of the nearer diagonal on (`D_white_of_coincidence`); so the criterion
  decides which farther diagonal makes the next one white: one farther diagonal for each nearer one.
- **Lemma E** (`white_of_coincidence`, `evwhite_iff_eventually_eq`): if a = b from s on and b(s1) is black for some
  s1 ≥ s, then x is white from s1 + 1 on (once a = b the recurrence is x(t + 1) = ¬b(t) ∧ x(t)). So, when the nearer word
  has blacks arbitrarily late (as a periodic word with a black does), the child is eventually white if and only if its
  parents eventually coincide; the forward direction is the kit's `white_forces_eq`.

Guards and statuses: PROVED two-party by hand (GC2550, GC2565) and in core Lean (L1474, L1476; GPT's source reads GC2583, GC2587). The guards are a
black of the nearer word and, for the periodic forms, a positive common period; backward recovery holds for any actual triple
even when the nearer word is all white, while the unique forward child and the coincidence criterion need the black; Lemma E's white child needs a black of the
nearer word at or after the onset of coincidence, and its equivalence needs blacks arbitrarily late. The pair map
is a partial bijection from pairs whose second member has a black onto pairs whose first member has one, not a permutation.
Exact on 12,000 diagonals of the seed (COMPUTED). Prior art: Rowland §5, AIOvernight's reset law and `D_white_of_eq`; our
record's §8.31. The family theorem establishes none of the measured statements of 3.6 and 4.

**A computation.** The first white diagonals of the single-cell pattern, read on the last 1,024 of 4,096 ticks, and the two
facts the module connects there: a white diagonal D w has coinciding parents D(w − 2) = D(w − 1) (the kit's `D_white_of_eq`),
and that coincidence, after a black of D(w − 2), is equivalent to D(w − 3) being the difference of D(w − 2)
(`D_coincidence_iff`). This is a finite window, an illustration: it does not show that these diagonals stay white.

```wl
T = 4096; L = 1024; ca = CellularAutomaton[30, {{1}, 0}, T];
diag[j_] := diag[j] = Table[ca[[t + 1, T + 1 + j - t]], {t, 0, T}];
win[v_] := Take[v, {T - L + 1, T}];
diff[v_] := BitXor[Most[v], Rest[v]];
white = Select[Range[0, 47], Max[win[diag[#]]] == 0 &]
```

```wl
Grid[Prepend[Table[{w, win[diag[w - 2]] == win[diag[w - 1]],
     If[w >= 3, win[diag[w - 3]] == win[diff[diag[w - 2]]], "(no D(w - 3))"], Max[win[diag[w - 2]]] == 1}, {w, white}],
  {"white D w", "D(w - 2) = D(w - 1)", "D(w - 3) = difference of D(w - 2)", "D(w - 2) has a black"}], Frame -> All]
```


## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30LeftReset`, whose
recurrence, reset step and accumulation it builds on, with `Rule30Diagonals.D_step` for the left diagonals, at the verifier's
kit commit 93d98bbe.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30LeftReset

/-!
# The farther parent and the coincidence criterion of the left reset recurrence (F1–F3)

`Rule30LeftReset` studies the recurrence `x (t + 1) = a t ⊕ (b t ∨ x t)`: a child `x` driven by a nearer word `b` and a
farther word `a`. The left diagonals of the single-cell pattern obey it (`Rule30Diagonals.D_step`: the child `D (j + 2)`,
the nearer `D (j + 1)`, the farther `D j`). This module adds three facts about it, for arbitrary words in natural time.

* `closed_form` (F1): after a black nearer bit at `r` and a white run of the nearer word on `(r, t]`, the child is the
  complemented parity of the farther word over `r … t`: `x (t + 1) = ¬ par a r (t + 1 - r)`. This packages the kit's reset
  step with `accum` on a bounded run.
* `farther_of_child`, `farther_unique`, `solutions_agree` (F2): the farther word is recovered from the child and the
  nearer word, `a t = x (t + 1) ⊕ (b t ∨ x t)`, for any triple; and two children of the same farther and nearer words
  agree from `s0 + 1` on once `b s0` is black. With the kit's `reset_periodic` this is the bijection between periodic
  farther words and periodic children whenever the nearer word has a black.
* `coincidence_iff` (F3): if `b s0` is black, the child equals the nearer word from `s0 + 1` on iff the farther word is the
  nearer word's difference `b t ⊕ b (t + 1)` from `s0` on. No periodicity is needed.
* `white_of_coincidence`, `evwhite_iff_eventually_eq` (Lemma E): if the farther word equals the nearer word from some
  time on, the child falls to white at the next black of the nearer word; so, when the nearer word has blacks arbitrarily
  late, the child is eventually white iff its parents eventually coincide (the forward way is the kit's `white_forces_eq`).
* `D_closed_form`, `D_farther_of_child`, `D_coincidence_iff`, `D_white_of_coincidence`, `D_evwhite_iff_eventually_eq`:
  the same for the left diagonals. With the kit's
  `D_white_of_eq`, a white diagonal `D (j + 3)` forces `D (j + 1) = D (j + 2)`, and that coincidence holds after a black of
  `D (j + 1)` iff `D j` is the difference of `D (j + 1)` there: one farther diagonal for each nearer one.

The statements and their hand proofs are Cloud's (the contributors' record, CL697), read two-party (GC2550); the reset and
the accumulation are the kit's. Nothing here concerns the centre column or the Prize problems.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata

set_option autoImplicit false

open Rule30LeftReset Rule30Diagonals

section Generic
variable {x a b : Nat → Bool}

/-- The parity of `a r, …, a (r + n)` peeled from the front. -/
theorem par_cons (a : Nat → Bool) (r : Nat) : ∀ n, par a r (n + 1) = xor (a r) (par a (r + 1) n)
  | 0 => by simp [par]
  | n + 1 => by
    have ih := par_cons a r n
    show xor (par a r (n + 1)) (a (r + (n + 1))) = xor (a r) (xor (par a (r + 1) n) (a (r + 1 + n)))
    rw [ih, show r + (n + 1) = r + 1 + n by omega]
    cases a r <;> cases par a (r + 1) n <;> cases a (r + 1 + n) <;> rfl

/-- One reset step: a black nearer bit sets the child to the complement of the farther bit. -/
theorem reset_step (hx : ∀ t, x (t + 1) = xor (a t) (b t || x t)) {r : Nat} (hr : b r = true) :
    x (r + 1) = !a r := by
  rw [hx, hr]
  cases a r <;> rfl

/-- Accumulation of the farther word over a bounded white run of the nearer word. -/
theorem accum_upto (hx : ∀ t, x (t + 1) = xor (a t) (b t || x t)) (r : Nat) :
    ∀ n, (∀ k, r < k → k ≤ r + n → b k = false) → x (r + 1 + n) = xor (x (r + 1)) (par a (r + 1) n)
  | 0, _ => by simp [par]
  | n + 1, hw => by
    have ih := accum_upto hx r n (fun k h1 h2 => hw k h1 (by omega))
    rw [show r + 1 + (n + 1) = (r + 1 + n) + 1 by omega, hx, hw (r + 1 + n) (by omega) (by omega), ih]
    simp only [par, Bool.false_or]
    cases a (r + 1 + n) <;> cases x (r + 1) <;> cases par a (r + 1) n <;> rfl

/-- **F1, the closed form.** After a black nearer bit at `r` and a white run of the nearer word on `(r, t]`, the child at
`t + 1` is the complemented parity of the farther word over `r … t`. -/
theorem closed_form (hx : ∀ t, x (t + 1) = xor (a t) (b t || x t)) {r t : Nat} (hrt : r ≤ t) (hr : b r = true)
    (hw : ∀ k, r < k → k ≤ t → b k = false) : x (t + 1) = !(par a r (t + 1 - r)) := by
  obtain ⟨n, rfl⟩ : ∃ n, t = r + n := ⟨t - r, by omega⟩
  have h := accum_upto hx r n (fun k h1 h2 => hw k h1 h2)
  rw [show r + n + 1 = r + 1 + n by omega, h, reset_step hx hr, show r + 1 + n - r = n + 1 by omega, par_cons]
  cases a r <;> cases par a (r + 1) n <;> rfl

/-- **F2, recovery.** The farther word is determined by the child and the nearer word, for any triple. -/
theorem farther_of_child (hx : ∀ t, x (t + 1) = xor (a t) (b t || x t)) (t : Nat) :
    a t = xor (x (t + 1)) (b t || x t) := by
  rw [hx]
  cases a t <;> cases (b t || x t) <;> rfl

/-- Two farther words with the same child and the same nearer word are equal. -/
theorem farther_unique {a' : Nat → Bool} (hx : ∀ t, x (t + 1) = xor (a t) (b t || x t))
    (hx' : ∀ t, x (t + 1) = xor (a' t) (b t || x t)) : a = a' := by
  funext t
  rw [farther_of_child hx t, farther_of_child hx' t]

/-- **F2, uniqueness.** Two children of the same farther and nearer words agree from `s0 + 1` on once `b s0` is black. -/
theorem solutions_agree {x' : Nat → Bool} (hx : ∀ t, x (t + 1) = xor (a t) (b t || x t))
    (hx' : ∀ t, x' (t + 1) = xor (a t) (b t || x' t)) {s0 : Nat} (hs : b s0 = true) :
    ∀ t, s0 + 1 ≤ t → x t = x' t := by
  intro t ht
  obtain ⟨n, rfl⟩ : ∃ n, t = s0 + 1 + n := ⟨t - (s0 + 1), by omega⟩
  clear ht
  induction n with
  | zero => rw [Nat.add_zero, reset_step hx hs, reset_step hx' hs]
  | succ n ih => rw [show s0 + 1 + (n + 1) = (s0 + 1 + n) + 1 by omega, hx, hx', ih]

/-- **F3, the coincidence criterion.** If `b s0` is black, the child equals the nearer word from `s0 + 1` on iff the
farther word is the nearer word's difference `b t ⊕ b (t + 1)` from `s0` on. -/
theorem coincidence_iff (hx : ∀ t, x (t + 1) = xor (a t) (b t || x t)) {s0 : Nat} (hs : b s0 = true) :
    (∀ t, s0 + 1 ≤ t → x t = b t) ↔ (∀ t, s0 ≤ t → a t = xor (b t) (b (t + 1))) := by
  constructor
  · intro h t ht
    rw [farther_of_child hx t, h (t + 1) (by omega)]
    rcases Nat.lt_or_eq_of_le ht with hlt | heq
    · rw [h t (by omega)]
      cases b t <;> cases b (t + 1) <;> rfl
    · subst heq
      rw [hs]
      cases b (s0 + 1) <;> rfl
  · intro h t ht
    obtain ⟨n, rfl⟩ : ∃ n, t = s0 + 1 + n := ⟨t - (s0 + 1), by omega⟩
    clear ht
    induction n with
    | zero =>
      rw [Nat.add_zero, reset_step hx hs, h s0 (Nat.le_refl _), hs]
      cases b (s0 + 1) <;> rfl
    | succ n ih =>
      rw [show s0 + 1 + (n + 1) = (s0 + 1 + n) + 1 by omega, hx, ih, h (s0 + 1 + n) (by omega)]
      cases b (s0 + 1 + n) <;> cases b (s0 + 1 + n + 1) <;> rfl

/-- **Lemma E, the converse direction.** If the farther word equals the nearer word from `s` on, then each step reads
`x (t + 1) = ¬ b t ∧ x t`, so the child can only fall, and it is white from `s1 + 1` on after a black `b s1` with `s ≤ s1`. -/
theorem white_of_coincidence (hx : ∀ t, x (t + 1) = xor (a t) (b t || x t)) {s s1 : Nat}
    (heq : ∀ t, s ≤ t → a t = b t) (hs : s ≤ s1) (h1 : b s1 = true) : ∀ t, s1 + 1 ≤ t → x t = false := by
  intro t ht
  obtain ⟨n, rfl⟩ : ∃ n, t = s1 + 1 + n := ⟨t - (s1 + 1), by omega⟩
  clear ht
  induction n with
  | zero => rw [Nat.add_zero, hx, heq s1 hs, h1]; rfl
  | succ n ih =>
    rw [show s1 + 1 + (n + 1) = (s1 + 1 + n) + 1 by omega, hx, heq _ (by omega), ih]
    cases b (s1 + 1 + n) <;> rfl

/-- **Lemma E both ways.** If the nearer word has blacks arbitrarily late, the child is eventually white iff the farther
word eventually equals the nearer word. The forward direction is the kit's `white_forces_eq`. -/
theorem evwhite_iff_eventually_eq (hx : ∀ t, x (t + 1) = xor (a t) (b t || x t))
    (hb : ∀ T, ∃ t, T ≤ t ∧ b t = true) : EvWhite x ↔ ∃ s, ∀ t, s ≤ t → a t = b t := by
  constructor
  · rintro ⟨T, hT⟩
    exact ⟨T, white_forces_eq hx hT⟩
  · rintro ⟨s, heq⟩
    obtain ⟨s1, hs, h1⟩ := hb s
    exact ⟨s1 + 1, white_of_coincidence hx heq hs h1⟩

end Generic

/-! ### The left diagonals -/

/-- F1 for the left diagonals. -/
theorem D_closed_form {j r t : Nat} (hrt : r ≤ t) (hr : D (j + 1) r = true)
    (hw : ∀ k, r < k → k ≤ t → D (j + 1) k = false) : D (j + 2) (t + 1) = !(par (D j) r (t + 1 - r)) :=
  closed_form (x := D (j + 2)) (a := D j) (b := D (j + 1)) (D_step j) hrt hr hw

/-- F2 for the left diagonals: each diagonal is recovered from the next two. -/
theorem D_farther_of_child (j t : Nat) : D j t = xor (D (j + 2) (t + 1)) (D (j + 1) t || D (j + 2) t) :=
  farther_of_child (x := D (j + 2)) (a := D j) (b := D (j + 1)) (D_step j) t

/-- Lemma E's converse for the left diagonals: if `D j = D (j + 1)` from `s` on and `D (j + 1)` is black at `s1 ≥ s`, then
`D (j + 2)` is white from `s1 + 1` on. -/
theorem D_white_of_coincidence {j s s1 : Nat} (heq : ∀ t, s ≤ t → D j t = D (j + 1) t) (hs : s ≤ s1)
    (h1 : D (j + 1) s1 = true) : ∀ t, s1 + 1 ≤ t → D (j + 2) t = false :=
  white_of_coincidence (x := D (j + 2)) (a := D j) (b := D (j + 1)) (D_step j) heq hs h1

/-- Lemma E both ways for the left diagonals, when `D (j + 1)` has blacks arbitrarily late. -/
theorem D_evwhite_iff_eventually_eq {j : Nat} (hb : ∀ T, ∃ t, T ≤ t ∧ D (j + 1) t = true) :
    EvWhite (D (j + 2)) ↔ ∃ s, ∀ t, s ≤ t → D j t = D (j + 1) t :=
  evwhite_iff_eventually_eq (x := D (j + 2)) (a := D j) (b := D (j + 1)) (D_step j) hb

/-- F3 for the left diagonals: after a black of `D (j + 1)` at `s0`, `D (j + 2)` coincides with `D (j + 1)` iff `D j` is
the difference of `D (j + 1)`. -/
theorem D_coincidence_iff {j s0 : Nat} (hs : D (j + 1) s0 = true) :
    (∀ t, s0 + 1 ≤ t → D (j + 2) t = D (j + 1) t) ↔
      (∀ t, s0 ≤ t → D j t = xor (D (j + 1) t) (D (j + 1) (t + 1))) :=
  coincidence_iff (x := D (j + 2)) (a := D j) (b := D (j + 1)) (D_step j) hs

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

F1 to F3, as Lean prints them, for any triple and on the left diagonals:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30LeftReset", "Ruliology.CellularAutomata.Rule30Diagonals"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = {"closed_form", "farther_of_child", "solutions_agree", "coincidence_iff", "D_closed_form", "D_coincidence_iff",
   "white_of_coincidence", "evwhite_iff_eventually_eq", "D_white_of_coincidence", "D_evwhite_iff_eventually_eq"};
show[Take[heads, 6], "TypeForm"]
```

Lemma E, both ways:

```wl
show[Take[heads, -4], "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it
resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.coincidence_iff"]["KernelCheck"]
```

## 8. Appendix: every portal entry placed by object

One row per entry of the portal index (3 November 2026, refreshed 18:49Z, 119 entries). Object letters are the essay's
sections (a second letter after a slash is a secondary placement); author is the first listed author as the portal shows it, "ours" as in section 2; status is
Lean Verified (LV) or Lean Unverified (LU), with Human Verified (HV) and kit-contribution tags. The placement is a reading
of each title and abstract by Cloud, the record's Claude (Anthropic) worker, reviewed by GPT (GC2585: two moves adopted). Rows are by date within a section.

| object | entries |
|---|---|
| A. The centre column | 24 |
| B. Period 2 | 42 |
| C. Periods 3 and 4 | 6 |
| D. The diagonals | 22 |
| E. Fronts, walls and backgrounds | 7 |
| F. Structure and barriers | 9 |
| G. Problems 2 and 3 | 9 |

### A. The centre column

| date | id | object | author | status | title |
|---|---|---|---|---|---|
| 2026-10-22 | [c27323](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-c27323) | A | ours | LV, HV, kit | The white end: no column of rule 30 settles into 1 0^q, for any q ≥ 10 |
| 2026-10-23 | [521830](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-521830) | A | @AIOvernight | LV, HV | Two More Eventual Words Excluded from the Center Column of Rule 30 |
| 2026-10-23 | [524848](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-524848) | A | Troy Lowry | LV, HV, kit | Six-bit core exclusions at padding 74 by backward vacuum certificates |
| 2026-10-23 | [603218](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-603218) | A/G | Andy Norris | LV, HV | Right-sealed shield cascades, multi-parameter strip fixed points, Kleene block absorption, and Problem 2/3 degree-density bridges for Rule 30 |
| 2026-10-23 | [7a9ed3](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-7a9ed3) | A | @AIOvernight | LV, HV, kit | White Padding before 10111 and Eighty-Seven Periodic Words in Rule 30 |
| 2026-10-23 | [8fe04c](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-8fe04c) | A | Troy Lowry | LV, HV, kit | Forbidden suffixes and arbitrary-length tail families for Rule 30 |
| 2026-10-23 | [c5e3c0](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-c5e3c0) | A | Andy Norris | LV, HV | Right-sealed shield cascades, multi-parameter strip fixed points, and Kleene block absorption for Rule 30 |
| 2026-10-24 | [03b551](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261024-03b551) | A | Luis Perez Morales | LV, HV, kit | Every Run of the Center Column Is Shorter Than Its Start Time |
| 2026-10-25 | [0554f7](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261025-0554f7) | A | Jean-Pierre Goux | LV, HV, kit | A three-fifths bound on black runs in the rule 30 center column |
| 2026-10-26 | [196859](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261026-196859) | A | @AIOvernight | LV, HV, kit | Long White Runs in the Center Column of Rule 30 |
| 2026-10-26 | [4d375d](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261026-4d375d) | A | @AIOvernight | LV, HV, kit | Short Blocks Before Long White Runs in the Center Column of Rule 30 |
| 2026-10-26 | [c389d5](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261026-c389d5) | A | @AIOvernight | LV, HV, kit | The White End of Rule 30 from q = 9, by One Pumped Certificate |
| 2026-10-26 | [d611aa](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261026-d611aa) | A | @AIOvernight | LV, HV, kit | A Four-Category Block Grammar for the Center Column of Rule 30 |
| 2026-10-27 | [317c64](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-317c64) | A/B | Renaud Bosdure | LV, HV, kit | Rule 30: Self-Shielded Black Runs, Sharper White-Run Bounds, and Q01 as an Integer Iteration |
| 2026-10-27 | [e324b6](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-e324b6) | A | @AIOvernight | LV, HV, kit | Explicit log log margins for constant runs of the Rule 30 center |
| 2026-10-28 | [e34744](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261028-e34744) | A/C | Emerson Villafuerte | LV, HV | Left-Diagonal Defect Spectra, Sublinear Monochromatic Run Bounds, and Semigroup Saturation in Rule 30 |
| 2026-10-29 | [5e2b66](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261029-5e2b66) | A | ours | LV, HV | Excluded column words of length 11 to 16, beyond the kit's table |
| 2026-10-29 | [8131b1](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261029-8131b1) | A | ours | LV, HV, kit | White runs beside two periodic columns of rule 30 are at most two periods long |
| 2026-10-29 | [f7ace9](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261029-f7ace9) | A | ours | LV, HV | Excluded column words of length 17 and 18, beyond the kit's table |
| 2026-11-03 | [1a6e64](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-1a6e64) | A | G.P.J.W. Quint | LV | Parity-Resolved D 0 / D 1 Boundary Collisions and Strengthened Erosion Bounds in Rule30BlackRunErosion |
| 2026-11-03 | [1c93e6](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-1c93e6) | A/D | G.P.J.W. Quint | LV | Exact Bounded whiteCount Witnesses and Sub-Linear Window Existence of Both Center Colors in Rule30SettledBarrierEffective |
| 2026-11-03 | [452bbf](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-452bbf) | A/G | @AIOvernight | LV | Black Cells of the Center Column Grow at Least Like Log Base Eight Fifths |
| 2026-11-03 | [462dc9](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-462dc9) | A/D | G.P.J.W. Quint | LV | Single-Pair Parity Obstruction for White Center Runs and Constant-Diagonal Barriers in Rule30SettledBarrier |
| 2026-11-03 | [b476c1](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-b476c1) | A/G | @AIOvernight | LV | An Exact Cylinder Count for the White Center Times of Rule 30 |

### B. Period 2

| date | id | object | author | status | title |
|---|---|---|---|---|---|
| 2026-10-20 | [81df0e](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261020-81df0e) | B | yingy | LV, HV, kit | Four-cell tails after an alternating stripe in Rule 30 |
| 2026-10-22 | [91b0b0](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-91b0b0) | B | ours | LV, HV | Under a period-2 center column, a right neighbour that starts with near-squares has no left edge |
| 2026-10-22 | [920c1b](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-920c1b) | B | ours | LV, HV | Rule 210 beside the period-2 clock: the one-sided question is false and the left half is linear |
| 2026-10-23 | [0c4a33](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-0c4a33) | B | ours | LV, HV | Every characteristic Sturmian word is excluded as the right neighbour of a period-2 center column |
| 2026-10-23 | [1bf4dc](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-1bf4dc) | B | ours | LV, HV | Rule 210, the two-sided statement: no finite configuration keeps the period-2 clock on its center column |
| 2026-10-23 | [4767e0](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-4767e0) | B | ours | LV, HV | The channel bound, certified: how much a clocked center column lets its right neighbour say |
| 2026-10-23 | [4d1a54](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-4d1a54) | B | ours | LV, HV | The channel bound at width 14: explicit automaton states, one kernel check per state |
| 2026-10-23 | [60d213](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-60d213) | B/A | @AIOvernight | LV, HV | Sparse16: A Finite Obstruction to an Alternating Center in Rule 30 |
| 2026-10-23 | [8084e6](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-8084e6) | B | ours | LV, HV | Every Sturmian word, of every slope and every intercept, is excluded as the right neighbour of a period-2 center column |
| 2026-10-23 | [8e6bd3](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-8e6bd3) | B | ours | LV, HV | The death time at width 52 is exactly 96, with witnesses at widths 56 and 60 |
| 2026-10-23 | [ac3898](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-ac3898) | B | ours | LV, HV | The death time at width 56 is exactly 100: a complete chunk certificate and its witness |
| 2026-10-24 | [4dcf69](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261024-4dcf69) | B | ours | LV, HV | A death-time lower bound at width 76, with a witness from a complete GPU census |
| 2026-10-24 | [71f858](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261024-71f858) | B | ours | LU | The death time at width 60 is exactly 114: a complete chunk certificate and its witness |
| 2026-10-24 | [8d7751](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261024-8d7751) | B | ours | LV, HV | Two infinite families of right halves absorbed by the ether: CQ01 for every right half with one of two prefixes |
| 2026-10-24 | [a129c3](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261024-a129c3) | B | ours | LV, HV | A death-time lower bound at width 74, with a witness from a complete GPU census |
| 2026-10-24 | [b16332](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261024-b16332) | B | ours | LV, HV | Death-time lower bounds at widths 64 to 72, with witnesses from a complete GPU census |
| 2026-10-25 | [017d83](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261025-017d83) | B | G.P.J.W. Quint | LV, HV, kit | Unconditional Four-Cell and Five-Cell Stripe-Tail Mortality in Zero-Boundary Rule 30 |
| 2026-10-26 | [e67465](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261026-e67465) | B/C | byline garbled on the portal | LV | Partial structural results toward Rule 30 Problem 1: a truncation bridge, first kernel-checked Q001 instances, and a coupled golden-mean source constr |
| 2026-10-27 | [1910d0](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-1910d0) | B | G.P.J.W. Quint | LV, HV | Unconditional Six-Cell and Seven-Cell Stripe-Tail Mortality and Sparse Return-Map Completion of (97, 0) in Zero-Boundary Rule 30 |
| 2026-10-27 | [230bc7](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-230bc7) | B | Renaud Bosdure | LV, HV, kit | Rule 30, Period 2: a Closed Trap for the Right Half Driven from the Empty Row |
| 2026-10-27 | [352e5d](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-352e5d) | B | ours | LV, HV, kit | A seven-cell rewrite beside the white wall that merges in two steps, for every tail and every finite cut |
| 2026-10-28 | [8abb51](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261028-8abb51) | B | G.P.J.W. Quint | LV, HV, kit | Clone-Ray Transfer Laws, the Backward 00 <-> 1^infty Avalanche Dichotomy, and Survivor Pullback Characterization for Zero-Boundary Stripe Front Window |
| 2026-10-29 | [0ef6e2](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261029-0ef6e2) | B | ours | LV | Finite-arc rotation codes beside a Rule 30 clock |
| 2026-10-29 | [23ac1b](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261029-23ac1b) | B | Eric Elbaz (Tensorbend.ai) | LV, HV | A period-free finite-defect elimination for Rule 30 |
| 2026-10-29 | [99db76](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261029-99db76) | B | Eric Elbaz (Tensorbend.ai) | LV, HV | Finite-support exclusions for eventually simple traces in Rule 30 |
| 2026-10-29 | [a4691a](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261029-a4691a) | B | G.P.J.W. Quint | LV, kit | Constructive Backward Operators, the Period-3 NOR Wave Trichotomy, and Projective Orbit Laws for Zero-Boundary Stripe Primitive Roots |
| 2026-10-29 | [dc3d17](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261029-dc3d17) | B | ours | LV | An explicit finite horizon for mechanical words beside a Rule 30 clock |
| 2026-10-30 | [5beddc](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261030-5beddc) | B | G.P.J.W. Quint | LV, HV, kit | The Universal Backward Wave Cascade, Clone-Ray Disjointness, and 16-Ray All-Length Mortality for Zero-Boundary Stripe Prefixes |
| 2026-10-30 | [60990f](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261030-60990f) | B | Jeongseop Lee | LV, HV | An All-Time Forbidden Return-Gap Pattern in the Alternating-Driven Rule 30 Right Orbit |
| 2026-11-01 | [c6ff55](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261101-c6ff55) | B | G.P.J.W. Quint | LV, HV, kit | The 3-Level Backward Transducer State-Collapse Hierarchy: 010 Causal Firewalls, 00 Period-Doubling, and Universal 6L Period Bounds |
| 2026-11-01 | [f0127e](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261101-f0127e) | B | G.P.J.W. Quint | LV, HV, kit | Universal 010-Synchronizing Complement Waves, 2-Step Period-Doubling, and Mod-3 Shift-Template Laws in Rule30ZeroBoundaryStripeCascade |
| 2026-11-02 | [121ada](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261102-121ada) | B/D | G.P.J.W. Quint | LV, HV, kit | Exact Conjugacy Between Rule30SurvivalBridge Frontier Scans and Rule 30 Left Diagonals |
| 2026-11-02 | [6824d5](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261102-6824d5) | B | G.P.J.W. Quint | LV, HV, kit | White-Corridor Transmission of Recurring Right Germs, Germ Factorization of u R, and Drought Clock Bounds for CQ01 |
| 2026-11-02 | [715db1](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261102-715db1) | B | G.P.J.W. Quint | LV, HV, kit | Left-Prefix Causality, 1-Step Memory Erasure, and Left-Front / Right-Terminal Causal Cone Collision in Rule30SurvivalBridge |
| 2026-11-02 | [75bd53](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261102-75bd53) | B | G.P.J.W. Quint | LV | Universal 11-Freeness of Even Right Germs, Dual Even-Step White Corridors, and u R Pulse-Drought Bounds |
| 2026-11-02 | [924d87](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261102-924d87) | B | G.P.J.W. Quint | LV, HV, kit | Universal Idempotent Period Preservation, Stages 6 to 9 of the Backward Wave Cascade, and the Stage-8 Attractor Bifurcation |
| 2026-11-02 | [b8e784](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261102-b8e784) | B | G.P.J.W. Quint | LV, HV, kit | Unifying Rule30AlternatingTraceBridge and Rule30SurvivalBridge: Universal Frontier Pin, Logarithmic Column-(-2) Repeat Growth, and Spacetime Field Rec |
| 2026-11-02 | [bf1582](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261102-bf1582) | B | G.P.J.W. Quint | LV, HV, kit | Global Invertibility of the Inverse Cone, Complete 4-Symbol Peel-Rank Exclusion, and Unconditional Small-Word Orbit Separators |
| 2026-11-02 | [f48894](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261102-f48894) | B | G.P.J.W. Quint | LV, HV | Unconditional Proof of SmallRW, Small-Length MaxHorizon Bounds, and Discharging SmallRW from BWH to PeriodTwoExcluded |
| 2026-11-03 | [bfefea](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-bfefea) | B | G.P.J.W. Quint | LV | Two-Sided Bijectivity of the Wedge Inverse Operator and Unconditional OrbitSeparator Through Word Length 3 |
| 2026-11-03 | [d6e898](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-d6e898) | B | G.P.J.W. Quint | LV | Universal Terminal Pin at All Steps, Shifted-Window Repeat Growth, and Closed-Form Depth-2/3/4 FG Readout in Rule30AlternatingTraceBridge |
| 2026-11-03 | [e1cb85](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-e1cb85) | B | G.P.J.W. Quint | LV | 2-Step Absorbing Period Preservation on (001111)^inf and Involutive Period-Doubling to Period 12 on (011111)^inf in Rule30ZeroBoundaryStripeCascade |

### C. Periods 3 and 4

| date | id | object | author | status | title |
|---|---|---|---|---|---|
| 2026-10-22 | [0cac94](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-0cac94) | C | giraudsa | LV, HV, kit | Q001 up to Width 37, and the Words 0^(P-1)1 of Rule 30 |
| 2026-10-24 | [1fc962](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261024-1fc962) | C | Luis Perez Morales | LV, HV, kit | The Period-3 Ether Erodes: No Period-3 Wall of Any Width |
| 2026-10-25 | [a02087](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261025-a02087) | C | Eric Elbaz (Tensorbend.ai) | LV, HV, kit | All finite right halves supported above 30 are absorbed by the period-4 ether-and-wall family |
| 2026-10-25 | [b572b3](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261025-b572b3) | C | Eric Elbaz (Tensorbend.ai) | LV, HV, kit | Single-cell period-4 absorption for the word 0001 |
| 2026-10-27 | [c137e0](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-c137e0) | C | Renaud Bosdure | LV, HV, kit | Least Period 4 of Rule 30: a Weaker Sufficient Condition, and Why the Left Half Must Be Finite |
| 2026-11-03 | [29bcb9](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-29bcb9) | C | Leonardo Jiménez Martínez | LV | The truncated ether breaks the 011 pattern: an infinite family for the all-times form of C3w(011) |

### D. The diagonals

| date | id | object | author | status | title |
|---|---|---|---|---|---|
| 2026-10-22 | [0616de](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-0616de) | D | ours | LV, HV | The left diagonals of rule 30: their periods are unbounded, and the settled band has no long white run |
| 2026-10-22 | [1d5070](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-1d5070) | D/A | ours | LV, HV | A repeat on the center column cannot put its white run inside the settled band of left diagonals |
| 2026-10-26 | [1b82d8](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261026-1b82d8) | D | @AIOvernight | LV, HV, kit | A Half-Rate Exponent Bound for Right-Diagonal Periods in Rule 30 |
| 2026-10-27 | [196370](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-196370) | D | ours | LV, HV, kit | Staircases near the single cell's right edge end; the rain rows keep a two-step edge patch for ever |
| 2026-10-27 | [61e435](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-61e435) | D | ours | LV, HV, kit | A finite-depth right edge follows the single-cell ruler with a fixed cap |
| 2026-10-29 | [3ca86f](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261029-3ca86f) | D | ours | LV, HV, kit | The universal start of the right diagonals of rule 30 |
| 2026-10-29 | [7d47a9](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261029-7d47a9) | D | ours | LV, HV, kit | The 101 shift law for the right diagonals of rule 30, with its mod-4 forms |
| 2026-10-29 | [a94f21](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261029-a94f21) | D | ours | LV, HV, kit | Periodic temporal profiles of rule 30: pulse holes, source weights and rooted returns |
| 2026-10-30 | [7b0d12](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261030-7b0d12) | D | ours | LV, kit | Half-rate prefix clocks for every two-input gate |
| 2026-10-31 | [9861e5](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261031-9861e5) | D | ours | LV | Nested record thresholds for every two-input gate clock |
| 2026-11-01 | [0f0c09](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261101-0f0c09) | D | G.P.J.W. Quint | LV, HV, kit | Two-Diagonal Period Descent, the 9-Diagonal White-Reset Neighborhood, Sharp White-Gap 5 Bounds, and Right-Diagonal Density 1/2 |
| 2026-11-01 | [5da074](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261101-5da074) | D | G.P.J.W. Quint | LV, HV, kit | Left-Diagonal Anti-Periodicity and Unbounded Asymptotic Density-1/2 Diagonals for Prize Problem 2 |
| 2026-11-01 | [a2fefb](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261101-a2fefb) | D/G | G.P.J.W. Quint | LV, HV, kit | Antiperiodic Spin-Momentum Annihilation, Block-Energy Vanishing, and Diagonal Energy Bridges for Prize Problem 2 |
| 2026-11-02 | [0f4b7a](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261102-0f4b7a) | D | G.P.J.W. Quint | LV, HV, kit | Post-White Twin-Diagonal Conservation, HalfDensity Invariance, Multiplex Balance, and Right-Diagonal Discrepancy Bounds |
| 2026-11-03 | [050b68](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-050b68) | D | G.P.J.W. Quint | LV | Exact Small-Depth Front Bounds (k <= 5) and Sharpened 2^k - 27 Periodicity Onset in Rule30FrontLaw |
| 2026-11-03 | [0a9bde](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-0a9bde) | D | G.P.J.W. Quint | LV | Explicit Quantitative Bounds on whiteCount and the Next Settled Diagonals in Rule30LeftUnbounded |
| 2026-11-03 | [0ad6ff](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-0ad6ff) | D | G.P.J.W. Quint | LV | Half-Depth Bound on whiteCount and 2^(j / 2) Eventual Periodicity in Rule30LeftReset |
| 2026-11-03 | [0d8a71](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-0d8a71) | D | G.P.J.W. Quint | LV | Exact Realization of the Unique Gap-Five White Pair (D 2, D 7) and Sharp whiteCount Evaluation Through Index 12 |
| 2026-11-03 | [20f058](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-20f058) | D | ours | LV | The closing law of prefix doublings on Rule 30's right edge |
| 2026-11-03 | [750fd6](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-750fd6) | D | G.P.J.W. Quint | LV | Complement Discrepancy Symmetry, Odd-Multiple Antiperiodicity, and Odd-Stride Subsampling Density 1/2 on Rule 30 Diagonals |
| 2026-11-03 | [84a42c](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-84a42c) | D/G | @AIOvernight | LV | The Binary Cube Inside the Rule 30 Cone |
| 2026-11-03 | [efd2bd](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-efd2bd) | D | G.P.J.W. Quint | LV | Stroboscopic Alternation, Multi-Period Half-Black Conservation, and Synchronized Wall Returns on Rule 30 Right Diagonals |

### E. Fronts, walls and backgrounds

| date | id | object | author | status | title |
|---|---|---|---|---|---|
| 2026-10-26 | [0ef9c8](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261026-0ef9c8) | E/B | Jeongseop Lee | LV, HV | Period-32 two-phase shielding rigidity for finite Rule 30 moving-front states |
| 2026-10-31 | [7c1f96](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261031-7c1f96) | E | ours | LV, HV, kit | The longest ether-pair episode behind a black right edge of rule 30 |
| 2026-11-03 | [3742dc](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-3742dc) | E | ours | LU | The classic ether of rule 30 absorbs a black edge: front speed exactly zero |
| 2026-11-03 | [87ba7a](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-87ba7a) | E | ours | LV | Moving walls in Rule 30: exact front speeds 5/19 and 2/9 |
| 2026-11-03 | [d37d24](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-d37d24) | E | ours | LV | Episodes and eternal tails behind Rule 30's black edge: a finite criterion |
| 2026-11-03 | [e660e4](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-e660e4) | E | ours | LV | The universal healing bound for rule 30 |
| 2026-11-03 | [e742c0](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-e742c0) | E/D | G.P.J.W. Quint | LV | Six-Window Four-Layer Defect Escape and Five-Window Isolated-Defect Bounds in Rule30DefectClockBudget |

### F. Structure and barriers

| date | id | object | author | status | title |
|---|---|---|---|---|---|
| 2026-10-23 | [7e9e6e](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-7e9e6e) | F | G.P.J.W. Quint | LV, HV | Left-Cone Reconstruction Lemmas and Complete Classification of Jen's Left-Permutive Class in Rule30Realization |
| 2026-10-24 | [991a71](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261024-991a71) | F | ours | LV, HV | Telling left edges apart from the center column: exact deadlines for three edge pairs |
| 2026-10-24 | [ad6cac](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261024-ad6cac) | F | Troy Lowry | LV, HV, kit | Distinct spatial column traces with an explicit uniform bound |
| 2026-10-24 | [ddbfbd](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261024-ddbfbd) | F | @AIOvernight | LV, HV, kit | Exact XOR Superposition Rigidity for Rule 30 |
| 2026-10-29 | [a96cee](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261029-a96cee) | F/E | ours | LV, HV, kit | Light-speed periodic rings of rule 30 as closed walks of periodic profiles |
| 2026-10-30 | [803bc4](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261030-803bc4) | F | ours | LV, HV | Finite ancestors of Rule 30 rows: roots, boundary tests and exact counts |
| 2026-11-02 | [075afb](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261102-075afb) | F | G.P.J.W. Quint | LV | Fundamental Causal Logic of Rule 30: ANF Decomposition, Marginal Causal Influence Census, and Spacetime Retrodiction |
| 2026-11-03 | [4b2a58](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-4b2a58) | F/G | @AIOvernight | LV | No Smaller Observable Certifies the Word 1001 in Rule 30 |
| 2026-11-03 | [ea30e7](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-ea30e7) | F/E | G.P.J.W. Quint | LV | Triangular Left-Permutivity, Right-Edge White-Corridor Sensitivity, and Left-Parent Injectivity of the Rule 30 Block Tree |

### G. Problems 2 and 3

| date | id | object | author | status | title |
|---|---|---|---|---|---|
| 2026-10-25 | [5105a7](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261025-5105a7) | G | Eric Elbaz (Tensorbend.ai) | LV, HV, kit | Problem 2 is exactly one nearly-geometric sequence of nearly-balanced scales |
| 2026-10-31 | [781b70](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261031-781b70) | G | G.P.J.W. Quint | LV, HV, kit | Word-Level Dyadic Ray Verification (k <= 10) and Finite Canonical-Window Step Lower Bounds for Prize Problem 3 |
| 2026-10-31 | [b58e66](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261031-b58e66) | G | G.P.J.W. Quint | LV, HV, kit | Head-Cone Locality, 2-Adic Transient Elimination, and Unconditional Step Lower Bounds for Prize Problem 3 |
| 2026-11-01 | [18ba2f](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261101-18ba2f) | G | G.P.J.W. Quint | LV, HV, kit | Right-Head Horizon (ScansBelow), Input-Scan Span (RightSpan), and Canonical-Root Time-Space Collapse for Prize Problem 3 |
| 2026-11-01 | [c646f6](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261101-c646f6) | G | G.P.J.W. Quint | LV, HV, kit | Finite-Vessel Tape Invariance, Box-Repeat Periodicity, and Non-Halting Propagation on Dyadic Rays |
| 2026-11-02 | [a535cf](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261102-a535cf) | G | G.P.J.W. Quint | LV | Prize Problem 3: Finite Inverse Light-Cone Triangles, Cherenkov Residual-Time Wavefront Bounds, and Write-Energy Coupling |
| 2026-11-02 | [eb2e05](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261102-eb2e05) | G | G.P.J.W. Quint | LV | Prize Problem 2: Spin-Shield Negotiation Conservation Laws, Cross-Correlation Orthogonality, and All-Energy-Forms Transfer |
| 2026-11-02 | [fee9ad](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261102-fee9ad) | G | G.P.J.W. Quint | LV, HV | Write-Energy Trajectory Injectivity, Constructive 1-Pass Periodic Deciders, and Core-Lean-4 Reduction of Problem 1 to Problem 3 |
| 2026-11-02 | [fefa7e](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261102-fefa7e) | G | G.P.J.W. Quint | LV | Prize Problem 3: Unconditional Canonical-Window RightSpan Bounds for the Center Column and Bidirectional Excursion Turnaround Inequalities |

## Sources

The Rule 30 Prize kit (main c42f6e5, 3 November 2026); the portal (119 entries at 3 November 18:49 GMT, 117 Lean Verified); E. Rowland, "Local nested
structure in rule 30", Complex Systems 16 (2006); E. Jen, "Global properties of cellular automata", J. Stat. Phys. 43 (1986); the
research record (the record's MAP.md, SYNTHESIS-20261029.md, APPRAISAL-20261029.md and the structure atlas; CL645, CL678 and
§8.66 for the measured constants); the portal index of 3 November, refreshed at 18:49Z, and the kit's catalog at c42f6e5 for the check.
