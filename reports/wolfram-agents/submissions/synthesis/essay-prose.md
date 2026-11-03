---
Template: ComputationalEssay
Name: Rule 30, the picture so far: a map of the partial results by object, with the connections between them
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: DRAFT 2026-11-03 16:11 GMT, revised 2026-11-03 16:54 GMT after GC2565
Description: A synthesis of the Rule 30 Prize portal and kit: every proved partial result placed by the object it is about and the frame it lives in, the exact connections between results of different contributors, what is still missing said once, and a reading guide; with one new bridging theorem on the left diagonals as the entry's Lean content
Abstract: [DRAFT, to be written last; 250 words]
Keywords: [rule 30, Rule 30 Prize, synthesis, map, left-permutivity, OR masking, odometer, zero boundary, diagonals, ether, fronts, Lean, partial results]
Sources: [the kit; the portal; the research record; Rowland 2006; Jen 1986]
---

*Status: DRAFT by Cloud for the owner and the workers, first 2026-11-03 16:11 GMT, revised 2026-11-03 16:54 GMT with GC2565's corrections.
Not for posting. The twenty November attributions are confirmed against the live portal (GPT, GC2565; the citation map beside
this file holds the checked rows); the older attributions are as the record's map recorded them when first read, to be
re-confirmed at source level before posting; Lemmas F1–F3 are PROVED two-party under GC2550's guards (section 7); A5 is at its
gate (CL699); the Lean anchor is to be built by Local after A5; the owner decides whether and when it goes out.*

## 0. Why a map

At 3 November 2026 (16:18 GMT) the portal listed 114 entries by some fifteen first authors, 112 of them Lean Verified, and the
kit's main had 195 modules. The portal collects submissions at different stages of verification; this essay cites entries that
are Lean Verified, or kit modules, by id and author. Almost every one was proved by one party on its own question. Reading them together, they are
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
(Bosdure), which is Φ with one bit discarded per step; Q01, the period-2 case of Problem 1, lives here. A fourth coordinate
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
runs 1^r u with 9⌈(P − r)/4⌉ ≤ r (Bosdure), 11 0^q for q ≥ 8 (Norris), white-padded tails 0^r u for r beyond a bound singly
exponential in |u| (Lowry; AIOvernight), the white end 1 0^q for q ≥ 10 in every column of every leftmost-black row (ours,
c27323, ported to the kit as `Rule30WhiteEnd`) and from q = 9 for the seed by one pumped certificate (AIOvernight,
`Rule30WhiteEndNine`, on top of ours), grammars of run categories and mixtures (AIOvernight), explicit word lists of lengths 8 to
18 (the kit, AIOvernight, ours), run bounds for Problem 2 (Villafuerte, Goux, Morales, AIOvernight), single-pair parity
barriers for white centre runs and constant diagonals (Quint, 462dc9, extending AIOvernight), sublinear windows that contain both
centre colours (Quint, 1c93e6), parity-resolved boundary collisions with black-run erosion bounds (Quint, 1a6e64), and defect
escape budgets (Quint, e742c0, on Lowry's `Rule30DefectClockBudget`). Not covered: every word with no run of nine and no long white padding, in particular
every word of period 2, 3 or 4, which is why those go to frames B and C.

**B. Period 2 (frame C and its coupling).** Under the clock 0101… the centre passes nothing to the left half, so period 2 reduces
to Q01: no finite start beside a white wall keeps depth 1 black at every even time. Known: every start of width ≤ 60 dies (the
kit to 52; ours to 60), exact death times to width 60 and lower bounds to 76 (ours), the constrained starts counted exactly as
2^⌊W/2⌋ (the kit), the free bits under the coupling never spelling 00 or 11111, the right neighbour of a clocked centre never a
Sturmian word (ours), never a finite-arc rotation code with late large partial quotients (ours, 0ef6e2), at most 0.2445 bits of
information per visible bit at width 14 (ours), the empty right half's gate reduced to gaps 3 or 5 (Bosdure), the forced left
skeleton through column −10 in closed form (Quint, 1e1b3b), the stripe cascade (Quint, f0127e), and Quint's conditional reductions
of November: the frontier-to-left-diagonal conjugacy (121ada), small-RW proved and dropped from the chain while the period-two
conclusion still assumes BWH (f48894, PR 84, open), the budget-mortality equivalence with its all-budget premise (b8e784), a left
inverse of the stream map (bf1582) made two-sided with separators for words of length at most 3 (bfefea, PR 101), period
preservation under an idempotent block on a finite interval (924d87), the all-step terminal pin (d6e898) and two-step absorbing
preservation (e1cb85). PRs 83, 85, 86 and 87 are closed unmerged as pull requests, but their modules are on the kit's main and
their entries carry the kit-contribution tag: adopted source, not pending work. The sibling rule 210 shares the count and has Q01 false (ours): the counting cannot decide Q01.

**C. Periods 3 and 4 (frame A's right half under a periodic driver).** The period-3 ether erodes (Morales); Q001 holds to width
37 (giraudsa). Period 4 reduces to absorption into the ether-and-wall family (Tensorbend for a single cell at every position and
phase; the weaker `Lock w` suffices, Bosdure); the ether's 109-state wall is Lowry's trap (PR65); the ether episode behind a black
edge has an exact length (ours, `Rule30EtherEpisode`); and an edge inserted into the ether is pinned for ever, front speed exactly
zero (ours, A1, 3742dc, built on Lowry's trap). The coupled witnesses with a periodic left half and a finite right half read the
period-4 word from time 0 (Bosdure); the coupled driven half-line's even germs, corridors and drought bounds are Quint's (75bd53).

**D. The diagonals (frames B and its mirror).** *Right:* R_j has period 2^(e_j), doubling exactly when a prescribed cell is black
and never three times in a row; e_j ≤ j/2 + O(log* j) (AIOvernight's record charge, `Rule30RecordCharge`); row 2^k reads 1 0^(J_k) 1
from its edge; for every finite seed the right diagonals after the first equal adjacent pair have least periods 4, 8, 8, 16, 32,
32 (ours, 3ca86f); the 101 shift law and its mod-4 forms (ours, 7d47a9) and its closing law for every alternating run (ours, A3,
20f058); a finite-depth right edge follows the single cell's ruler with a cap (ours, S1 to S3); half-rate prefix clocks for every
two-input gate (ours, Package A and its nested thresholds). *Left:* D_k is eventually periodic with period dividing 2^(whiteCount)
and the periods are unbounded (AIOvernight, `Rule30LeftReset`, `Rule30LeftUnbounded`; Rowland 2006 §5 for the setting); no two
adjacent eventually-white diagonals, eventually-white diagonals at least five apart (AIOvernight); the exact transient-front reset
law (AIOvernight, `Rule30FrontLaw`); on those modules, Quint's November extensions: infinitely many antiperiodic left diagonals
with exact half density (5da074), complement discrepancy and odd-stride half density (750fd6), whiteCount(j) ≤ j/2 with eventual
period dividing 2^(j/2) (0ad6ff), quantitative whiteCount and next-settled-diagonal bounds (0a9bde), the gap-five white-pair
classification (0d8a71) and small-depth front bounds (050b68; its public abstract states an onset of −10 and the PR head a
stronger −27 for k ≥ 5, so cite the declaration, not the title); on the right, stroboscopic alternation and synchronized wall
returns (Quint, efd2bd). This entry's theorem (section 7): once two neighbouring left diagonals have settled with a common period
and the nearer one is not all white, the next one's cycle is forced, the map is affine and invertible in the farther neighbour,
two consecutive settled cycles determine the one before, and a diagonal is eventually white exactly when its two neighbours have
equal cycles, which happens two diagonals after the grandparent equals the parent's derivative. [Rowland's question of one left
side: the record's §8.31, not on the portal: cite as prior work.]

**E. Fronts, walls and backgrounds (all frames, new in November).** The rightmost cell of a difference moves right at exactly one cell per step, and
the leftmost at a speed set by the background: zero on the classic ether (ours, A1, 3742dc: kernel-checked locally; the portal's
public check timed out and the maintainer's rerun is pending), exactly 5/19 on the ring background 100100000 and exactly 2/9 on
1010000 (ours, A4, 87ba7a, superseding 37281a: moving walls, certified by closed sets with an exact potential, at the entry's
stated alignments and under its closure-entry and arbitrary-tail guards), 1/2 on the eight-cell ether (the kit's `Rule30Ether`),
about 0.246 on a fair random row (measured, not a theorem); and for every background and every perturbation confined to one side,
at most 1 minus the background's recruitment climb rate (ours, A2, e660e4, a universal healing bound). Triangular
left-permutivity with guarded light-cone sensitivity (Quint, ea30e7) is the related prior work for A2. The finite past of finite rows: unique
root and age, the physical parent test, exact all-width counts (ours, 803bc4).

**F. Structure and barriers.** The XOR of two histories is a history only trivially (AIOvernight, ddbfbd); every density conserved
by four steps on every window is a coboundary, so there is no additive local conservation law of that kind (Lowry,
`Rule30LocalConservation`; the excluded class is additive window densities conserved by the stated steps, and monotone ranks,
non-additive and clock-dependent potentials stay open, as Lowry's own `Rule30DefectClockBudget` uses such a rank); distinct
columns of the seed differ by time max(|p|, |q|) + 18 (Lowry, ad6cac); Jen's left-permutive class is exactly rules 90, 150, 210,
30, and 30 is the only one with a non-eventually-constant centre (Quint, 7e9e6e); configurations recurring with velocity in
[−1, 1) are spatially periodic (the kit); at velocity +1 the periodic rings are closed walks of periodic profiles (ours, a96cee);
the centre cell at time t has algebraic degree exactly 2t − 1 (Norris; the kit). Together: a proof of Q01 must use the OR's
nonlinearity beyond its counting consequences, must use the finiteness of the left half beyond its periodicity, and cannot rest
on an additive local conservation law; whether a non-additive or clocked potential exists is open.

**G. Problems 2 and 3.** Problem 2 is equivalent to its limit, Abel-mean and simple-normality forms (the kit's `equivalents/`),
to one nearly geometric sequence of nearly balanced scales (Tensorbend), and to the balance of the centre's OR-event parities
split by the settled part of its past diagonal [the record's C4 bridge, not on the portal]. Problem 3 has its three formal forms
(the kit), the degree and query bounds (Norris), and scans-below / right-span bounds with a halting collapse (Quint, 18ba2f).

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

**3.3 Alternation is the one rigid periodic structure in every frame:** the unique fixed background of the wall frame (Quint),
what long black runs leave behind, the only odd 2-cycles of the edge map (ours), the rings with Φ²x = x (ours), the collapse of a
32-step return (Lee), and the ether of period 4 seen in a moving frame.

**3.4 The merges are one phenomenon:** F = Φ ≫ 1 says the wall frame is the invertible edge frame with one bit discarded per step;
the trace merges and ambiguities (Lowry), the prefix merger (ours) and the forgetting front are that leak seen from different sides,
and `EdgeObservable` (Lowry) asks whether the leak can erase the highest bit.

**3.5 Two capacities, not yet one language:** the channel bound at width 14 (ours: a finite upper bound of 0.2445 bits per
visible bit at that width, not an all-width rate) and the empty right half's gap shift (Bosdure) count related symbols; the
width-14 bound sits about 4% below the gap shift's entropy, a comparison of two numbers. Whether the two describe one language,
and what the gap means, nobody has written down as a theorem.

**3.6 The two ends are one recurrence.** The right diagonals obey d′ = d ⊕ (u ∨ w) and the left diagonals d′ = w ⊕ (u ∨ d): the
same three-input recurrence with the cell's own value moved from the linear slot into the OR. On the right the cell integrates at
every tick and never forgets: the odometer, with periods observed to grow like 2^(0.41 j) (the doubling density 0.41 is measured; the proved
bound is e_j ≤ j/2 + O(log* j)). On the left the cell is reset at every black of its nearer
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
depth is finite", with its finite criterion at the horizon lcm(2^B(k+2), p) (ours, A5, prepared and at its gate; the bridge was
proposed in the record, CL676), connect that object to the eternal points of the edge map: a background that ends every episode
hosts no eternal wall.

## 4. What is still missing, said once

Problem 1 needs, for every periodic driver, that a finite right half locks its first column, except at period 2 where it needs
the finite left half to die; Q01 needs a mechanism that is nonlinear, uses finiteness, and is not an additive local conservation law (F). The frames supply two
mechanisms no theorem uses yet: the leak F = Φ ≫ 1, and the odometer's rigidity (3.3). Problem 2 needs the balance of a parity that
grows with time, which no fixed-order fairness test can give. Of the measured constants, the fair-row front speed 0.246, the
right-edge doubling density 0.41 and the left-end period law "P reached near 2^P" (measured on the seed's first 12,000 left
diagonals and on random finite seeds; conjectures, each with its stated sample) have mechanisms but no theorems; the centre
column itself passed the five generic tells we ran on its first 8,192 cells (block entropy to order 10, linear complexity of a
2,048-bit window, the 2-kernel, autocorrelation to lag 64, residues mod 8), as did random finite seeds, while Thue–Morse,
Rudin–Shapiro and a 31-bit LFSR failed them.

## 5. A reading guide

For the centre column: the kit's `Rule30StripCertificateTable` and `problem1_iff_no_word`, then Lowry's 8fe04c and 524848,
AIOvernight's 7a9ed3 and 521830, Norris's c5e3c0, Morales's 1fc962. For period 2: the kit's `Rule30ZeroBoundary*`, ours 61e435 and
the channel bound, Quint's 1e1b3b and f0127e, Bosdure's 317c64, Quint's November reductions (121ada, f48894, b8e784, bf1582,
924d87, bfefea). For the diagonals: the
kit's `Rule30Diagonals` and `TFunction`, AIOvernight's `Rule30RecordCharge` and the five left-side modules, Quint's 5da074, 750fd6, 0ad6ff, 0a9bde, 0d8a71 and 050b68,
ours 3ca86f, 7d47a9, 20f058, and this entry. For fronts and backgrounds: the kit's `Rule30Ether`, Lowry's trap (PR65), ours 3742dc,
e660e4, 87ba7a. For structure: ddbfbd, `Rule30LocalConservation`, 7e9e6e, a96cee. For the problems' equivalent forms: the kit's
`equivalents/` and Tensorbend's entries. [ids to be completed from the citation map]

## 6. How to add to the picture

A new entry can place itself in one line: the object (A to G), the frame, the two nearest entries it extends or contrasts with,
and what it leaves open. The record behind this essay will keep this map current; contributors who tell us where their result
sits will be cited by it.

## 7. The entry's own theorem: the settled left diagonals form a reversible recurrence

[To be stated in the kit's vocabulary (`Rule30LeftReset.reset_periodic`, `Rule30Diagonals`) and built by Local after A5. Content:
for a left-finite row whose diagonals k − 1 and k − 2 are eventually periodic with cycles u (having a black) and w of a common
period, diagonal k is eventually periodic with the unique cycle d(t+1) = ¬ ⊕_{s=β_u(t)}^{t} w(s), where β_u(t) is the last black of
u at or before t; the map w ↦ d is affine with an invertible linear part, with inverse w(t) = ¬d(t+1) ⊕ ¬u(t) ¬d(t); hence two
consecutive settled cycles determine the one before; and the next diagonal's cycle equals u exactly when w = u ⊕ shift(u), which
is exactly when the diagonal after that is eventually white. Statuses now: PROVED by hand, two-party (GPT, GC2550 and GC2565), under
these guards: a positive common period, time-labelled cycles with cyclic wrap, and the nearer cycle u containing a black; at a
black of u the reset value is e(t+1) = w(t), which the inclusive parity formula counts; backward recovery holds for any actual
triple even when u is all white, while the unique forward cycle and the coincidence criterion need the nonwhite guard; the pair
map is a partial bijection from pairs whose second member has a black onto pairs whose first member has one, not a permutation.
Exact on 12,000 diagonals of the seed (COMPUTED). Prior art: Rowland §5, AIOvernight's reset law; our record's §8.31. Adding the
family theorem in Lean establishes none of the measured statements of 3.6 and 4.]

## Sources

The Rule 30 Prize kit (main c42f6e5, 3 November 2026); the portal (114 entries at 3 November 16:18 GMT, 112 Lean Verified); E. Rowland, "Local nested
structure in rule 30", Complex Systems 16 (2006); E. Jen, "Global properties of cellular automata", J. Stat. Phys. 43 (1986); the
research record (the record's MAP.md, SYNTHESIS-20261029.md, APPRAISAL-20261029.md and the structure atlas).
