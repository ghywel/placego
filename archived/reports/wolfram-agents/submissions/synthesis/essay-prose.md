---
Template: ComputationalEssay
Name: Rule 30, the picture so far: a map of the partial results by object, with the connections between them
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: DRAFT 2026-11-03 16:11 GMT, revised 2026-11-03 18:52 GMT (GC2585 applied)
Description: A synthesis of the Rule 30 Prize portal and kit: every proved partial result placed by the object it is about and the frame it lives in, the exact connections between results of different contributors, what is still missing said once, and a reading guide; with one new bridging theorem on the left diagonals as the entry's Lean content
Abstract: see abstract.txt (draft, CL703)
Keywords: [rule 30, Rule 30 Prize, synthesis, map, left-permutivity, OR masking, odometer, zero boundary, diagonals, ether, fronts, Lean, partial results]
Sources: [the kit; the portal; the research record; Rowland 2006; Jen 1986]
---

*Status: DRAFT by Cloud for the owner and the workers, first 2026-11-03 16:11 GMT, revised 2026-11-03 18:52 GMT after GPT's live review (GC2585). Not for posting. Every
portal id below was checked against the portal index of 3 November (113 entries at 13:23Z; 119 at 18:49Z) and every kit module
against the kit's catalog at c42f6e5 (CL702); the twenty November attributions were confirmed live by GPT (GC2565), and GPT's
live review of the check (GC2585) is applied. Two ids of our earlier
map are no longer on the portal and are not cited (1e1b3b; 9d92a2, superseded by e34744). Where the essay cites a locally
checked result whose public check is pending, a computation, or the record itself, it says so. The owner has decided the three
design questions (anchor in, whole portal, the ask kept as an offer; CL701). Lemmas F1–F3 are PROVED two-party under GC2550's
guards (section 7); the Lean anchor is to be built by Local, with GPT's independent read of the actual module; A5 is posted
(d37d24). The owner decides whether and when this goes out.*

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
Our own entries are marked "ours"; the full list of ours is in the record's map; the citation map beside this draft has one line
per entry.

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
census (Quint, 075afb); and no observable smaller than a sixteen-cell window certifies the word 1001 with a bounded potential
(AIOvernight, 4b2a58). Together: a proof of Q01 must
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

Built by Local (L1474) as `Rule30LeftCoincidence` on the kit's `Rule30LeftReset`: 142 lines of core Lean with standard axioms;
the kit's Check and the portal Check pass; GPT's source read is pending. For any three words with x(t + 1) = a(t) ⊕ (b(t) ∨ x(t)),
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
- **On the left diagonals** (`D_closed_form`, `D_farther_of_child`, `D_coincidence_iff`, through the kit's `D_step` with child
  D(j + 2), nearer D(j + 1), farther D j): after a black of D(j + 1), D(j + 2) coincides with D(j + 1) exactly when D j is the
  difference of D(j + 1). A white diagonal forces its two parents to coincide (the kit's `D_white_of_eq`), and coinciding
  parents with a black force a white child (one step of the recurrence, x(t + 1) = ¬b(t) ∧ x(t), to be added to the module);
  so the criterion decides which farther diagonal makes the next one white: one farther diagonal for each nearer one.

Guards and statuses: PROVED two-party by hand (GC2550, GC2565) and in core Lean (L1474; GPT's read pending). The guards are a
black of the nearer word and, for the periodic forms, a positive common period; backward recovery holds for any actual triple
even when the nearer word is all white, while the unique forward child and the coincidence criterion need the black. The pair map
is a partial bijection from pairs whose second member has a black onto pairs whose first member has one, not a permutation.
Exact on 12,000 diagonals of the seed (COMPUTED). Prior art: Rowland §5, AIOvernight's reset law and `D_white_of_eq`; our
record's §8.31. The family theorem establishes none of the measured statements of 3.6 and 4.

## Sources

The Rule 30 Prize kit (main c42f6e5, 3 November 2026); the portal (119 entries at 3 November 18:49 GMT, 117 Lean Verified); E. Rowland, "Local nested
structure in rule 30", Complex Systems 16 (2006); E. Jen, "Global properties of cellular automata", J. Stat. Phys. 43 (1986); the
research record (the record's MAP.md, SYNTHESIS-20261029.md, APPRAISAL-20261029.md and the structure atlas; CL645, CL678 and
§8.66 for the measured constants); the portal index of 3 November, refreshed at 18:49Z, and the kit's catalog at c42f6e5 for the check.
