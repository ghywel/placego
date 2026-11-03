---
Template: ComputationalEssay
Name: Rule 30, the picture so far: a map of the partial results by object, with the connections between them
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: DRAFT 2026-11-03 16:11 GMT
Description: A synthesis of the Rule 30 Prize portal and kit: every proved partial result placed by the object it is about and the frame it lives in, the exact connections between results of different contributors, what is still missing said once, and a reading guide; with one new bridging theorem on the left diagonals as the entry's Lean content
Abstract: [DRAFT, to be written last; 250 words]
Keywords: [rule 30, Rule 30 Prize, synthesis, map, left-permutivity, OR masking, odometer, zero boundary, diagonals, ether, fronts, Lean, partial results]
Sources: [the kit; the portal; the research record; Rowland 2006; Jen 1986]
---

*Status: DRAFT by Cloud for the owner and the workers, 2026-11-03 16:11 GMT. Not for posting. Every attribution is to be confirmed by GPT
against the live portal (the citation map beside this file marks the unconfirmed ones); the Lean anchor (section 7) is to be
built by Local after A5; the owner decides whether and when it goes out.*

## 0. Why a map

The portal holds about eighty entries by some fifteen first authors, and the kit nearly two hundred modules. Each entry is a
theorem with a certificate, and almost every one was proved by one party on its own question. Reading them together, they are
not scattered: they are about a small number of objects, in three coordinate frames, and they rest on two consequences of the
rule. This essay says which object each result is about, how results of different contributors connect, what the whole leaves
open, and where to start reading. Its own Lean content is one bridging theorem (section 7); the rest is a reading of everyone's
work, cited by portal id and author. The three-week record behind it is public.

## 1. One rule, two mechanisms, three frames

Rule 30 is *new = left XOR (centre OR right)*. Two consequences carry everything proved so far.

**Left-permutivity.** Toggling the left input toggles the output, and *left = new XOR (centre OR right)*: the left neighbour is
recovered from the next row and the right pair, so the whole history to the left of two adjacent columns is determined by those
two columns (Jen 1986; the kit's `Rule30Jen` and its masked and windowed forms). A change travels right at exactly one cell per
step, unconditionally.

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
18 (the kit, AIOvernight, ours), run bounds for Problem 2 (Villafuerte, Goux, Morales, AIOvernight; settled-barrier parities,
462dc9), and defect escape budgets (e742c0). Not covered: every word with no run of nine and no long white padding, in particular
every word of period 2, 3 or 4, which is why those go to frames B and C.

**B. Period 2 (frame C and its coupling).** Under the clock 0101… the centre passes nothing to the left half, so period 2 reduces
to Q01: no finite start beside a white wall keeps depth 1 black at every even time. Known: every start of width ≤ 60 dies (the
kit to 52; ours to 60), exact death times to width 60 and lower bounds to 76 (ours), the constrained starts counted exactly as
2^⌊W/2⌋ (the kit), the free bits under the coupling never spelling 00 or 11111, the right neighbour of a clocked centre never a
Sturmian word (ours), never a finite-arc rotation code with late large partial quotients (ours, 0ef6e2), at most 0.2445 bits of
information per visible bit at width 14 (ours), the empty right half's gate reduced to gaps 3 or 5 (Bosdure), the forced left
skeleton through column −10 in closed form (Quint, 1e1b3b), the stripe cascade (Quint, f0127e), and the conditional reductions
of November: mortality implies period-two exclusion, small-RW proved and dropped from the chain, the budget-mortality equivalence
(PRs 83 to 87, [CHECK authors]). The sibling rule 210 shares the count and has Q01 false (ours): the counting cannot decide Q01.

**C. Periods 3 and 4 (frame A's right half under a periodic driver).** The period-3 ether erodes (Morales); Q001 holds to width
37 (giraudsa). Period 4 reduces to absorption into the ether-and-wall family (Tensorbend for a single cell at every position and
phase; the weaker `Lock w` suffices, Bosdure); the ether's 109-state wall is Lowry's trap (PR65); the ether episode behind a black
edge has an exact length (ours, `Rule30EtherEpisode`); and an edge inserted into the ether is pinned for ever, front speed exactly
zero (ours, A1, 3742dc, built on Lowry's trap). The coupled witnesses with a periodic left half and a finite right half read the
period-4 word from time 0 (Bosdure).

**D. The diagonals (frames B and its mirror).** *Right:* R_j has period 2^(e_j), doubling exactly when a prescribed cell is black
and never three times in a row; e_j ≤ j/2 + O(log* j) (AIOvernight's record charge, `Rule30RecordCharge`); row 2^k reads 1 0^(J_k) 1
from its edge; for every finite seed the right diagonals after the first equal adjacent pair have least periods 4, 8, 8, 16, 32,
32 (ours, 3ca86f); the 101 shift law and its mod-4 forms (ours, 7d47a9) and its closing law for every alternating run (ours, A3,
20f058); a finite-depth right edge follows the single cell's ruler with a cap (ours, S1 to S3); half-rate prefix clocks for every
two-input gate (ours, Package A and its nested thresholds). *Left:* D_k is eventually periodic with period dividing 2^(whiteCount)
and the periods are unbounded (AIOvernight, `Rule30LeftReset`, `Rule30LeftUnbounded`; Rowland 2006 §5 for the setting); no two
adjacent eventually-white diagonals, whiteCount(j) ≤ j/2, eventually-white diagonals at least five apart (AIOvernight); infinitely
many antiperiodic left diagonals with exact half density (Quint, 5da074); the exact transient-front reset law (AIOvernight,
`Rule30FrontLaw`); and, this entry's theorem (section 7): once two neighbouring left diagonals have settled, the next one's cycle
is forced, the map is affine and invertible in the farther neighbour, the strip of cycles is reversible, and a diagonal is
eventually white exactly when its two neighbours have equal cycles, which happens two diagonals after the grandparent equals
the parent's derivative. [Rowland's question of one left side: the record's §8.31, not on the portal: cite as prior work.]

**E. Fronts, walls and backgrounds (all frames, new in November).** A damage front moves right at exactly one cell per step and
left at a speed set by the background: zero on the classic ether (ours, A1), exactly 5/19 on the ring background 100100000 and
exactly 2/9 on 1010000 (ours, A4, 37281a: moving walls, certified by closed sets with an exact potential), 1/2 on the eight-cell
ether (the kit's `Rule30Ether`), about 0.246 on a fair random row (measured, not a theorem); and for every background and every
perturbation confined to one side, at most 1 minus the background's recruitment climb rate (ours, A2, e660e4, a universal
healing bound). Light-cone flip sensitivity (ea30e7, [CHECK author]) is the related work. The finite past of finite rows: unique
root and age, the physical parent test, exact all-width counts (ours, 803bc4).

**F. Structure and barriers.** The XOR of two histories is a history only trivially (AIOvernight, ddbfbd); every density conserved
by four steps on every window is a coboundary, so there is no local conservation law (Lowry, `Rule30LocalConservation`); distinct
columns of the seed differ by time max(|p|, |q|) + 18 (Lowry, ad6cac); Jen's left-permutive class is exactly rules 90, 150, 210,
30, and 30 is the only one with a non-eventually-constant centre (Quint, 7e9e6e); configurations recurring with velocity in
[−1, 1) are spatially periodic (the kit); at velocity +1 the periodic rings are closed walks of periodic profiles (ours, a96cee);
the centre cell at time t has algebraic degree exactly 2t − 1 (Norris; the kit). Together: a proof of Q01 must use the OR's
nonlinearity beyond its counting consequences, must use the finiteness of the left half beyond its periodicity, and cannot be a
local potential.

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

**3.2 "One bit per two cells" is one count in four places:** the constrained starts' free odd depths (the kit), the sideways row
above a sinking front, the half-rate bound on the right-diagonal exponents (AIOvernight), and the death-time model. The common
mechanism is left-permutivity in a triangular frame: each step exposes one new bit, and a constraint made every second step pins
every second one. What is not a theorem anywhere is the matching lower bound, that the freedom is used.

**3.3 Alternation is the one rigid periodic structure in every frame:** the unique fixed background of the wall frame (Quint),
what long black runs leave behind, the only odd 2-cycles of the edge map (ours), the rings with Φ²x = x (ours), the collapse of a
32-step return (Lee), and the ether of period 4 seen in a moving frame.

**3.4 The merges are one phenomenon:** F = Φ ≫ 1 says the wall frame is the invertible edge frame with one bit discarded per step;
the trace merges and ambiguities (Lowry), the prefix merger (ours) and the forgetting front are that leak seen from different sides,
and `EdgeObservable` (Lowry) asks whether the leak can erase the highest bit.

**3.5 Two capacities, one language:** the channel bound at width 14 (ours) and the empty right half's gap shift (Bosdure) count the
same symbols; their intersection misses at least 4% of the gap shift's entropy, a statement nobody has written down as a theorem.

**3.6 The two ends are one recurrence.** The right diagonals obey d′ = d ⊕ (u ∨ w) and the left diagonals d′ = w ⊕ (u ∨ d): the
same three-input recurrence with the cell's own value moved from the linear slot into the OR. On the right the cell integrates at
every tick and never forgets: the odometer, periods 2^(0.41 j). On the left the cell is reset at every black of its nearer
neighbour and integrates only when that neighbour is all white: the settled cycles are forced (section 7), the period grows only at
an eventually-white diagonal, by the odd-weight test (Rowland's Proposition 2; AIOvernight's reset law), and the white diagonals are
the coincidences of consecutive cycles, about one in 2^p. The kit's bound 2^(2P) on the next non-P diagonal (AIOvernight) is the
size of the pair space the strip's permutation orbit cannot exceed. The centre column sits between: it reads each right diagonal
once at birth and each left diagonal before its neighbours settle, which is why nothing proved about either end reaches it yet.

**3.7 The velocity spectrum and the episode bridge.** A1, A2 and A4 (ours) and the kit's ether results are one object: the
leftward speed of damage as a function of the background. The episode length behind a black edge (ours, `Rule30EtherEpisode`) and
the bridge "no eternal point of any period ends in a background iff every finite episode is finite" (ours, A5 in preparation)
connect that object to the kit's `PeriodicPoints`: a background that absorbs every finite episode hosts no eternal wall.

## 4. What is still missing, said once

Problem 1 needs, for every periodic driver, that a finite right half locks its first column, except at period 2 where it needs
the finite left half to die; Q01 needs a mechanism that is nonlinear, uses finiteness, and is not local (F). The frames supply two
mechanisms no theorem uses yet: the leak F = Φ ≫ 1, and the odometer's rigidity (3.3). Problem 2 needs the balance of a parity that
grows with time, which no fixed-order fairness test can give. Of the measured constants, the fair-row front speed 0.246, the
right-edge doubling density 0.41 and the left-end period law "P reached near 2^P" have mechanisms but no theorems; the centre
column itself has passed every generic tell for a coin.

## 5. A reading guide

For the centre column: the kit's `Rule30StripCertificateTable` and `problem1_iff_no_word`, then Lowry's 8fe04c and 524848,
AIOvernight's 7a9ed3 and 521830, Norris's c5e3c0, Morales's 1fc962. For period 2: the kit's `Rule30ZeroBoundary*`, ours 61e435 and
the channel bound, Quint's 1e1b3b and f0127e, Bosdure's 317c64, the November reductions (PRs 83 to 87). For the diagonals: the
kit's `Rule30Diagonals` and `TFunction`, AIOvernight's `Rule30RecordCharge` and the five left-side modules, Quint's 5da074, ours
3ca86f, 7d47a9, 20f058, and this entry. For fronts and backgrounds: the kit's `Rule30Ether`, Lowry's trap (PR65), ours 3742dc,
e660e4, 37281a. For structure: ddbfbd, `Rule30LocalConservation`, 7e9e6e, a96cee. For the problems' equivalent forms: the kit's
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
is exactly when the diagonal after that is eventually white. Statuses now: PROVED by hand (single-party), exact on 12,000
diagonals of the seed; a two-party read requested; prior art: Rowland §5, AIOvernight's reset law; our record's §8.31.]

## Sources

The Rule 30 Prize kit (main c42f6e5, 3 November 2026); the portal (about eighty entries at 3 November); E. Rowland, "Local nested
structure in rule 30", Complex Systems 16 (2006); E. Jen, "Global properties of cellular automata", J. Stat. Phys. 43 (1986); the
research record (the record's MAP.md, SYNTHESIS-20261029.md, APPRAISAL-20261029.md and the structure atlas).
