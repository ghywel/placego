# Rule 30 Prize Problem 1: the work

*Split of 2026-10-28 (Local, at the owner's request).* This file had reached 760 KB, almost all of it section 8,
so section 8's sub-sections (8.1 onwards) moved unchanged into three volumes in
[reports/rule30-prize/](reports/rule30-prize/). Section 8 below is now their table, one row and one link per
sub-section. The honest summary, the contents and sections 1 to 7 are unchanged and still here.

*Split out of [PRIZE-PROBLEMS.md](PRIZE-PROBLEMS.md) on 2026-10-05, at the owner's request. That document keeps the
open prizes as a whole (§1 to §4 there: the prizes, how a computer can win one, the ranking, and the tricks that let
a computer take part in a proof). This one holds the Rule 30 work, with its section numbers unchanged, so a
reference to "PRIZE-PROBLEMS.md §8.36" written before the split means §8.36 here. For the period-2 work in one place,
with its reading order and how to reproduce it, see [PERIOD-TWO.md](PERIOD-TWO.md).*

## Contents

*Added 2026-10-22 in the spring clean. Section numbers start at 5 because sections 1 to 4 stayed in
PRIZE-PROBLEMS.md. The Rule 30 work in this file stopped on 15 October 2026 (see "Where this stands"); the current
state is NOW.md.*

- [The three questions, as a coin](#the-three-questions-as-a-coin) · [Where this stands (2026-10-22)](#where-this-stands-2026-10-22) ·
  [The honest summary](#the-honest-summary) (dated updates, newest first)
- [5. The first experiment](#5-the-first-experiment-periodic-columns-in-rule-30) · [6. The rungs from here](#6-the-rungs-from-here) (the plan of 4 October) ·
  [7. Rung 2: left-side rigidity](#7-rung-2-first-progress-left-side-rigidity-2026-10-04) · [8. The right side as a complement](#8-the-right-side-as-a-complement-2026-10-04),
  whose sections 8.1 to 8.116 are the work:
  - **4 October**, [8.1](reports/rule30-prize/RULE30-PRIZE-8.1.md#81-the-four-arms-the-owners-design-2026-10-04) to 8.6: the four arms, the templates, Rule 30's siblings, column 1 as a turning wheel.
  - **5 October**, [8.7](reports/rule30-prize/RULE30-PRIZE-8.1.md#87-a-slip-is-one-particle-2026-10-05) to 8.59: the wheel's kicks and the channel bound (8.7 to 8.21); the owner's
    questions, from columns as numbers to the entropy squeeze and the coin (8.22 to 8.35); the records, the wall form,
    the counting form, Mahler and the wide survey (8.36 to 8.53); Jen's theorem with a clock and the window principle
    (8.54 to 8.59).
  - **6 October**, [8.60](reports/rule30-prize/RULE30-PRIZE-8.2.md#860-the-small-items-the-wall-never-sees-the-far-end-the-mostly-zero-words-and-the-left-side-to-a-million-2026-10-06) to 8.70: the small items, Question 3, what period 1 means, Rule 30's siblings, rings,
    triangles and velocity.
  - **9 October**, [8.71](reports/rule30-prize/RULE30-PRIZE-8.2.md#871-turning-rows-the-all-s-ring-turns-14-cells-a-step-rows-outrunning-light-are-rings-and-pattern-speed-is-not-signal-speed-2026-10-09) to 8.77: turning rows, the tiles, the right edge's ruler, where the left side's
    order ends, period 1 proved again (8.76), the entropy of the trace.
  - **10 October**, [8.80](reports/rule30-prize/RULE30-PRIZE-8.2.md#880-the-pattern-as-one-chain-and-the-chain-split-at-the-front-the-owners-lead-2026-10-10) to 8.87: the owner's chain leads and the first swarm round.
  - **11 October**, [8.88](reports/rule30-prize/RULE30-PRIZE-8.2.md#888-the-check-free-conjecture-and-the-forced-only-records-the-strategy-swarms-first-target-cloud-replicated-2026-10-11-0222-bst) to 8.90: the check-free conjecture, the room switch to the visible language, the
    carry of Rule 30.
  - **13 October**, [8.92](reports/rule30-prize/RULE30-PRIZE-8.3.md#892-the-fair-coin-question-and-the-pair-and-price-table-2026-10-13-1132-bst) to 8.98: the fair-coin question, the left horizon, the 18s at depths 125 to 138,
    history-restricted records.
  - **14 October**, [8.99](reports/rule30-prize/RULE30-PRIZE-8.3.md#899-mixed-sl-residences-no-small-constant-record-budget-a-uniform-one-remains-open-2026-10-14-0003-bst) to 8.113: the owner's foundations questions, the rigidity hunt and the doors
    across four problems, the record comb (8.104, 8.106, 8.108), Mahler's pair results (8.109 to 8.112), the swarm
    SW-01 (8.113).
  - **15 October**, [8.114](reports/rule30-prize/RULE30-PRIZE-8.3.md#8114-the-coins-shape-and-the-owners-primes-hunch-2026-10-15-1156-bst-cloud) to 8.116: the coin's shape, first principles, the thesis.
  - The status board's history, archived at the third, fourth and fifth triages: [8.78](reports/rule30-prize/RULE30-PRIZE-8.2.md#878-the-status-boards-history-archived-at-the-third-triage-2026-10-09),
    [8.79](reports/rule30-prize/RULE30-PRIZE-8.2.md#879-the-status-boards-history-archived-at-the-fourth-triage-2026-10-10), [8.91](reports/rule30-prize/RULE30-PRIZE-8.3.md#891-the-status-boards-history-archived-at-the-fifth-triage-2026-10-11-1440-bst).

## The three questions, as a coin

*Added 2026-10-08 at the owner's request, from a conversation about coin flips. It restates the problems in plain
words and adds no result.* Start Rule 30 from one black cell and read its centre column one cell per step, as a
coin: black is heads, white is tails. Wolfram's three prize problems ([rule30prize.org](https://rule30prize.org/),
official wording quoted) then ask:

1. **Does the coin ever fall into a repeating pattern forever?** Officially: "Does the center column always remain
   non-periodic?" Open. Taken one cycle length at a time:
   - *the same face forever* (period 1): no. Condrey proved it for every finite starting row (arXiv:2609.09431);
   - *heads, tails, heads, tails, forever* (period 2): open. This is the case the record works on
     ([PERIOD-TWO.md](PERIOD-TWO.md));
   - *any longer cycle* (period 3 and up): open, parked behind period 2.
2. **Is the coin fair in the long run?** Officially: "Does each color of cell occur on average equally often in the
   center column?" Open. Every measurement agrees with a fair coin (§8.34, §8.35); nothing is proved.
3. **Is there a shortcut to the n-th flip, or must you in effect make every flip before it?** Officially: "Does
   computing the nth cell of the center column require at least O(n) computational effort?" Open, and untouched
   here. A coin that repeats has a shortcut, since you can look its cycle up, so proving there is no shortcut
   would settle Problem 1 too (§8.34).

Three things make this coin unusual.
- **It is not chance.** Every flip is fixed by the rule, so each question has a true-or-false answer. A measurement
  can only make an answer look likely, and the prizes pay for proofs. For a truly random coin, "the same face
  forever" has probability zero but is not impossible. For Rule 30's coin it is impossible, because it is proved.
- **The endless grid matters.** A simulation on a finite grid has finitely many states, so its coin must eventually
  repeat. Mathematica used this column for random numbers for years (§8.15). The prizes ask about the endless grid,
  where the pattern keeps growing and that argument does not apply.
- **The record asks more than the prize.** It works one period at a time for every finite starting row, not only
  the single black cell (PERIOD-TWO.md §1).

## Where this stands (2026-10-22)

*Added in the spring clean, in plain words; nothing below it changed.* There is no proof of any of the three Rule 30
problems, and nothing to submit. The work recorded here ran from 4 to 15 October 2026. The owner switched the room to
Mahler's problem on 14 October (the Rule 30 room paused at L706), and the work stopped at the second halt, at the
owner's word, on 15 October at 14:58 BST. The last section is 8.116. Since then the main line has been eight streets
(L₈ = 68, proved) and four-bin partitions (FOUR-BIN-PARTITIONS.md). For the state of the work today read NOW.md; for
period 2's leads and closed routes, PERIOD-TWO.md sections 6 and 4. The honest summary below is a stack of dated
updates, newest first, each kept as it was written.

## The honest summary

**Update, 2026-10-11 16:21 BST (Cloud; read this first).** Still no proof of period 2 and nothing to submit. The owner
stopped the entrance lane this afternoon (its admission-deadline route is closed by Outcome 8's witness, and it was
circling) and put GPT on the finite-support record route: the left row beside the alternating wall is determined by the
trace, the prize configuration's left row is white beyond its support, so period 2 falls if R_real(d) is finite at every
depth (not bounded: the certified and sampled values grow slowly with d). GC1148, GC1151, GC1153 and GC1154 are the
route's first blocks, Local's exact record values and witnesses its data, the exact visible language to 44 its oracle,
and the 466-tick closure of the typed regime a lemma. Honest distance: more exact knowledge of the object today, the
same proof distance, one lane stopped, one lane with a line to the real instance. The one-page state is NOW.md; then
RECORD-MAP.md and PERIOD-TWO.md section 6. The earlier dated updates below are kept as they were written.

**Update, 2026-10-11 15:30 BST (Cloud; read this first).** Still no proof of period 2 and nothing to submit. Since the
14:06 update: (i) with Local's certified 178-bit pure-M3 cut every recurrent object of the collar lane is cut by
certificate and every typed path at width 28 lasts at most 466 ticks, 8 macros (Outcome 7). (ii) An actual renewal
exists (Outcome 8): a white-A origin outside the gate, of the 676 black-marker class, is not admitted by tick 44 (an
unguarded B, after three SS) and produces a typed black A row at tick 72 and its own high-111 image again at 88, for
every exterior; so the 676-class admission conjecture is false as a deadline, and the entrance question becomes how
often and how long such laps continue (sampled: no mixed core before 80, most tails admitted by 180). (iii) GPT's GC1148
record-conditioned SS budget was reported refuted (CL348); that report is withdrawn (15:47 BST, CL350), Cloud had the
orientation wrong and GC1148 stands as a proof sketch. (iv) Intel's strip form: Conjecture S holds to W = 39 in both
phases (IN010, 8.83 corrected). The board was triaged to two active rows (L639). The one-page state is NOW.md; then
RECORD-MAP.md and PERIOD-TWO.md section 6. The earlier dated updates below are kept as they were written.

**Update, 2026-10-11 14:06 BST (Cloud; read this first).** Still no proof of period 2 and nothing to submit. Since the
12:35 update the entrance question of the collar lane has been answered for the white-A high-LL family and its exit:
GPT's four certificates (GC1139 to GC1142) are all second-read by complete independent computation, so every white-A
high-LL entrance admits the mixed core by 52 or exits X at 26, every white-A origin outside the gate admits C at 16 or
enters a black-marker SS whose first SS cannot exit through unguarded B, and the X exit, measured in real cones to tick
212 (201 million exteriors per run), returns to a white-A origin at tick 106 in 1.8 percent of its cones, a return that
admits the core at 122 and renews nothing (8.89, Outcome 6). The typed collar regime therefore closes by cuts (at most
686 ticks, Outcome 5) and its named entrances close by certificates; what remains open there is the 676 black-marker SS
entrances, admission after an intervening white SS, and the sea's untyped admission, measured in X cones at about twice
the fair-coin rate for black A rows. The pure-M3 minimal cut has least absent length 178 and is certified (Local, L637);
with it the typed duration bound is 466 ticks, 8 macros (CL340, 14:14 BST). R_real at every depth is untouched by all of
this. The one-page state is NOW.md; then RECORD-MAP.md and PERIOD-TWO.md section 6. The earlier dated updates below are
kept as they were written.

**Update, 2026-10-11 12:35 BST (Cloud; read this first).** Still no proof of period 2 and nothing to submit. Since the
morning's room switch (8.89) the new room has paid out in one direction: the collar lane's typed black-A regime is now
excluded under the period-2 wall by certified absent words alone. The cut product over the whole width-28 strip graph
with the eleven certified cuts leaves only the pure-M3 self-loops (CL303), the pure-M3 word is itself absent at every
300-sample window (L632, its minimal cut being searched in 152..226), the omitted routes GPT found (the N macro, the
second D111, the X selector, the white-A restart) all begin in the transient part and none leaves a recurrent component
(CL306 to CL316), and with the 300-sample windows as cuts the product is acyclic: every path that follows the typed
grammar lasts at most 686 ticks (CL319, Outcome 5). What remains for that lane is how a trace enters the typed region:
GPT's entrance work (GC1134 to GC1139, all second-read) has so far closed the sixteen negative white-A entrances by 36
ticks and bounded every white-A entrance to one high LL per ordinary run; the twelve positive entrances and general
untyped admission are open, as is R_real at every depth. Beside the main line, the owner's carry question was answered
and recorded (8.90): the Gray correction is the two-time AND, the column carry is an exactly solved hidden chain with a
Fibonacci entropy rate, and the run count has no Holte matrix. The strip form (8.83) holds to W = 18 in the odd phase
with its tight run ending at 18. Exact values beyond the RR3 table: R_real(132) = R_real(139) = R_real(142) = R_real(143) = 17
(132 and 143 cake_lpr in both phases, 8.96), R_real(125) = 21 (cake_lpr); 145..150 are open at 18 after the capped solves. The one-page state is NOW.md; then RECORD-MAP.md and PERIOD-TWO.md
section 6. The earlier dated updates below are kept as they were written.

**Update, 2026-10-11 08:14 BST (Cloud; read this first).** Still no proof of period 2 and nothing to submit. The main line moved
this morning (8.89): from the swarm's forced-only door, now fully measured (8.88), to the real visible language and its
certified absent words. The first decisive test in the new room is settled (L630): the mixed-recurrence bridge of the
collar lane is absent from the real language by a certified 69-bit cut, so the recurrence that survived every strip
relaxation is an artefact, and the typed black-A regime closes by cuts (GPT's mapping is the open step). Exact values
beyond the RR3 table: R_real(132) = R_real(139) = R_real(142) = 17. The one-page state is NOW.md; then RECORD-MAP.md
and PERIOD-TWO.md section 6. The earlier dated updates below are kept as they were written.

**Update, 2026-10-08, night (Cloud; read this first).** Still no proof of period 2 and nothing to submit. The
counting statement (§5, Q1) has not moved since 2026-10-05. Around it, three days of work closed more than a dozen
routes, each with its reason, and added more than 200 statements with a proof and a second reader. The newest are:
- **The sibling Rule 210 is settled for period 2.** No finite seed keeps the full 0101 clock (PROOFS.md entry 32,
  Proposition 19). It does not transfer verbatim (GC479).
- **What a counterexample's frontier would have to do.** This is Q6's ray route, from the owner's red-object idea.
  The inside must pay the frontier's Fibonacci-parity beat with ever older, restarting events, never in a long
  streak (GC585 to GC601). The open step is whether the actual clock allows that at every depth.
- **The wheel's two readings of a kick are reconciled** (G248). Edge events obey three local rules (CL055).
For the full picture read STATE-OF-THE-PROOF.md (§4 has the 2026-10-08 frontier), then PERIOD-TWO.md §6, the status
board. The dated updates below are kept as they were written.

**Update, 2026-10-05, night (Local as lead; read this first).** Still no proof of period 2 and nothing to submit.
Three theorems were added, each elementary and each checked by a pre-registered probe:
- **Theorem A (§8.54), Jen's theorem with a clock.** Two adjacent columns cannot both be $P$-periodic on a time
  window $[a, b]$ unless $b \le 2a + L + 2P - 1$, where $L$ is the distance to the left edge. So in any period-2
  counterexample the wheel's kicks cannot thin out faster than geometrically.
- **Theorem B (§8.54).** With $P$-periodic columns 0 and 1, no zero run of the forced left half is longer than
  $2P - 2$. The bound is attained at visible period 2.
- **Theorem E (§8.57).** If column 1 is any Sturmian sequence (a coding of an irrational rotation), the forced
  left half is never finite. With Jen's theorem: no pure wheel works, rational or irrational. These are the first
  columns 1 beyond the eventually periodic ones for which Conjecture LR is proved.
Also: question 4 is closed (§8.55: Kari and Kopra's argument is about rows, not columns), and the Collatz twin's
state after the free bits is exactly a least residue modulo a power of 3 (COLLATZ-PRIZE.md §4). None of this
reaches the real case, where kicks come at a steady rate. §8.54 explains why the method stops there.
- **The Collatz transfer (§8.58, COLLATZ-PRIZE.md §5).** Both problems obey one exact statement, the window
  principle: a block of the trace can repeat only if it is no longer than the state is large. It gives Theorem A′
  here and, on the Collatz side, that no rational has a Sturmian parity sequence (found afterwards to be known:
  Dubickas 2009 for integer orbits, and three 2026 notes; COLLATZ-PRIZE.md §5). It also names what is missing
  here: a counterexample must keep the $2n$ cells beside its centre within $2^{0.13\,n}$ contents for ever, and
  the edge certifies only about $n$.
- **The band of stripes, brought in (§8.59).** The left end of every row has infinitely many diagonals that are
  black for ever (Lemma B2: the diagonals' periods are unbounded), so a repeat of the trace, which is a white run
  in the later row, must stay a growing distance below Theorem A′ (Theorem A‴). Corollary F: a column 1 that
  begins with near-squares at larger and larger periods is excluded with any left half (the period-doubling
  word, Chacon's word, every substitution fixed point starting with a double letter). The settled band has no
  white run longer than twice its period (Lemma B3), so a repeat's white run cannot lie in it (Theorem A⁗):
  with the universal strip certified to 53,200 diagonals, Thue–Morse and paperfolding are excluded for every
  left edge up to about 15,870 cells. For every left edge, their case reduces to one question about the left
  side of Rule 30 alone: does it settle at a bounded rate.

**Update, 2026-10-05, evening.** Still no proof and nothing to submit. The day's work moved
the problem to one precise statement:
- **Where it sits** (§8.45, §8.47, §8.49). Period 2 has the structure of Mahler's 3/2 problem: a free left side, a
  thin constrained right side (the wheel and its kicks), agreement at the wall for ever. A survey of eight fields
  found the same gap everywhere: theorems that holding a chaotic system costs information are about sets of cases,
  never one case. Here the gap can be crossed by an exact count, because seeds are finite.
- **The counting form** (§8.51). The number of configurations on $w$ cells whose centre follows 0101 for $T$ steps
  falls by about $2^{1.05}$ per step, exactly counted to $w = 24$. Proved: the conditions paid by the seed's left
  part halve the count exactly (left-permutivity).
- **The open part** (§8.52). The right part pays in lumps, never more than 3 free steps in a row to $w = 26$. The
  statement that would close period 2: $N_{w,j}(T+k) \le 2^{c(w) - \alpha k} N_{w,j}(T)$ for some $\alpha > 0$, with
  $c(w) = O(\log w)$. PERIOD-TWO.md §7 lists it with the other questions for whoever continues.
- **Local's records**: $R(85) = 73$ and $R(89) = 75$ (14 hours), as predicted blind from the merging census (§8.38); no right half up to 34
  cells is a counterexample.

**Where the work stands (2026-10-05, early morning).** There is no proof and nothing to submit. Period 1 was closed
by Condrey; period 2 is the open case, and the work concentrates there. What exists:

- **Evidence.**
  - No counterexample: every right half up to 18 cells for periods 2 to 6 (27 million cases, §5, §6), and for period
    2 every right half up to 32 cells, 4.3 billion: no finite configuration with a right half of at most
    32 cells and a left half of at most 108 has a period-2 column (§8.21).
  - The search can see a counterexample where one exists: in Rule 60, a sibling rule (§8.3).
- **Proved, or known and restated.**
  - Lemmas 1 to 4, about where the right side's bits enter the left half.
  - Proposition 5: in the sibling Rule 90, no period-2 column is possible, by Lucas' theorem.
  - Proposition 7 (Jen, 1990): no eventually periodic column 1 can make the left half finite. So in a finite
    configuration with column 0 eventually 0101…, column 1 is never eventually periodic, and the wheel must slip
    for ever (§8.13).
  - Every white triangle of Rule 30 is exact (§8.18). Run backwards, the pyramid is infinite and one-sided, and
    the backward step is the forced-left-half equation read in time (§8.19).
- **Computed facts.**
  - Proposition 6: the pure wheel's left half has an exact tail and period in depth (§8.6).
  - **The channel bound:** next to 0101…, column 1 carries at most 0.128 bits per visible bit, whatever the right
    side, from an exact automaton (§8.20). The bound is levelling off near 0.12. Typical right sides use 0.08, about
    3.5 bits per kick. A random sequence carries 1. The bound is now certified exactly (0.1292 at $m = 26$; 0.1236 at
    $m = 28$ since 2026-10-06), and it
    forces every column to the left of a period-2 column 0 below 0.0646 bits per step (§8.33; 0.0618 since the
    certificate reached $m = 28$ on 2026-10-06).
- **The picture.**
  - The right side runs a universal wheel, a rotation by 17/56 of a turn per step, kicked in whole notches by
    domain walls (§8.5 to §8.11). Next to column 0 the white triangles form a lattice in the wheel's frame, and a kick
    moves it rigidly. Walls that kick the wheel forward carry large white triangles along their path, and every
    kick sends a wake of them outwards (§8.18).
  - Every zero run of the left half costs about one bit per cell, paid from the distinct histories of column 1: the
    adversary does no better than coin flips (§8.14, §8.16).
  - A seed's information reaches column 1 slowly, at about 0.2 cells per step. So at a fixed depth the longest
    real zero run is set by the channel, not the seed: 8 cells from depth 41 for every seed width from 16 to 28
    (§8.17).
  - The owner's morning questions (§8.22 to §8.37). Read as a binary number, a column is rational exactly when it
    repeats, so the prize asks for one number's irrationality. A period-2 counterexample would need two irrational
    numbers adding to exactly 1, and a finite seed keeps them complementary for at most about $(w + 9)/2$ digits. The
    pyramid's diagonals are all rational, and the centre column is their Cantor diagonal. The diagonals' periods and
    the striped left side were known already (Jen; Rowland; Wolfram), and were re-derived here before the sources
    were read. As a conductor, Rule 30 channels lightning three times less than a random material, because of its
    handedness. As a maze it has no dead ends going up.
- **Routes closed.**
  - Bounded runs, at every layer width computed (up to 16): the adversary's runs keep growing with depth (§8.14).
  - Periodic columns 1, already a theorem (§8.13).
  - "Structured families" beating chance: they were luck (§8.16).
  - The entropy squeeze as a reduction (§8.33): it restates the problem. A proof along it needs a lower bound on a
    column's entropy in a finite configuration, which has never been proved for Rule 30.
- **The sharpest open target (§8.36).** The doubling conjecture: in the forced left half for 0101…, a zero run that
  starts at depth $d$ ends by depth $2d + 4$, for every column 1. It holds at every depth computed (to 81, with
  growing slack), and it would settle period 2 for every finite configuration. §8.38 explains the slack. The forced
  walks merge, about 6% at every step, so there are about $2^{0.41\,d}$ distinct walks rather than $2^{d/2}$. The
  coin's best of them lasts about $0.82\,d$ cells, which is what the records show.
- **The gap.** The kicks must happen for ever. A proof must show they can never steer the left half to zero and
  keep it there. Every statistic says they cannot: coin flips paid through a narrow channel. Nothing structural
  yet says why. §8.38 to §8.41 reduce every form of the question to one statement. In the wall form (§8.39), the
  conditions at a 0101 wall cost real information. The delivery side is a theorem (§8.20). The cost side holds
  exactly next to a white wall, where the channel's entropy is 0 (Condrey's case), and only as a coin model next to
  0101 (§8.41). The prime-gap parallel (PRIOR-ART) suggests the proof's likely shape: a size argument, as for
  Bertrand's postulate, rather than a proof of randomness. The structural levers found so far are listed in §8.15:
  - the tie between neighbouring columns;
  - the wheel;
  - the notched kicks;
  - Jen's leftward flow of periodicity;
  - the bottleneck and its exact bound.

The night's three main measurements are drawn in one figure, [rule30_night.svg](tests/probes/lexicon/rule30_night.svg):
- the adversary's runs against depth;
- the channel bound against layer width;
- the real runs against seed width.

Several of these results had been reached by others first: Condrey's triangular uniqueness, his "no bounded law" at
period 2, Hanson and Crutchfield's domain filter, Jen's theorem for periodic columns 1, and Meier and Staffelbach's
reconstruction of the left half from two columns (1991, §8.15). PRIOR-ART.md records them.

---

## 5. The first experiment: periodic columns in Rule 30

**The setup.** In $\mathbb F_2$, Rule 30 is $x'_i = x_{i-1} + x_i + x_{i+1} + x_i x_{i+1}$, which is linear in the
left cell. So for any column-0 trace $\tau$ and any right half $R$, the left half is forced, cell by cell:

```math
x_t(-1) = \tau(t+1) + \big(\tau(t) \vee x_t(1)\big), \qquad
x_t(-k) = x_{t+1}(-k+1) + \big(x_t(-k+1) \vee x_t(-k+2)\big) \pmod 2 .
```

A finite configuration whose column is eventually $p$-periodic, shifted in time, is a finite configuration whose
column is exactly $p$-periodic from $t = 0$. So the question for each $p$ is this: for some primitive word of length
$p$ and some finite $R$, is the forced left half eventually zero? Condrey proved the answer is no for $p = 1$. Jen
(1990) proved that two *adjacent* columns are never both eventually periodic. The prize asks about *one* column.

**The run** (2026-10-04, Cloud, one CPU core, 4m38s; predictions in the script header, written first):

| Check | Result |
|---|---|
| A. Published control: Condrey's sharp constant-prefix maxima $2\lceil w/2\rceil + 1$ and $2\lfloor w/2\rfloor + 2$, overall $w + 2$, with $2^w$ or $2^w - 1$ maximisers | **reproduced exactly** for $w = 1$ to $7$ (maximisers $1, 4, 7, 16, 31, 64, 127$) |
| B. Control: constant traces force left halves that are eventually alternating, never zero; the same for every $R$ when $\tau \equiv 1$ | **as predicted**: 32,767 cases |
| C. The construction: forced configurations reproduce their trace forwards; one flipped cell at depth $k$ breaks it at exactly $t = k$ | **66 of 66, and 66 of 66 caught** |
| D. Periods $2$ to $6$, every primitive word, every right half in $[1, 14]$, depth $192$: a forced left half that is eventually zero? | **none**, in 1,703,936 cases |
| E. Brute force over every configuration with support in $[-w, w]$: the longest stretch of a trace that follows its first $p$ values | grows slowly with $w$, at most $16$ at $w = 7$ (table in the run output) |

**An observation nobody predicted, and its explanation.** For periods $3$, $5$ and $6$, every forced left half is
aperiodic over its last 64 cells. For periods $2$ and $4$, a minority have tails of period exactly $7$, $14$ or $28$
(period 2: 773 of 32,768; period 4: 74,027 of 196,608). Some are periodic from the very first cell: the alternating
trace with the right half "cells 1 and 4 black" forces a left half that is exactly 7-periodic.

The lexicon's lift explains it (LEXICON.md §3.6: a finite program's loops are its spectrum). A spatially $n$-periodic
configuration is Rule 30 on a ring of $n$ cells, a finite program. Its cycles say which temporal periods its columns
can have. Computed for every ring up to 18 cells (all 524,286 states visited; the 7-ring's cycle lengths $1$,
$4 \times 7$ and $63$ as a known answer):

| Column period | Ring sizes (up to 18) where a Rule 30 orbit has it |
|---|---|
| $1$ | every size |
| $2$, $4$ | $7$, $14$ |
| $3$ | $12$ |
| $5$ | $5$, $10$, $15$ |
| $6$ | none |
| $7$, $9$ | $15$ |
| $8$ | $4$, $8$, $12$, $16$ |

The 7-ring has seven cycles of length 4, on which one cell repeats with period 4 or 2. So the 7-, 14- and 28-periodic
left halves are the left half settling into a copy of a 7-ring or 14-ring orbit, which is possible only for periods 2
and 4. For period 6, no ring up to 18 cells has such an orbit at all. A finite configuration needs its left half to
settle into the zero orbit instead. This is the first structural handle on the $p = 2$ case, and it is where rung 2
starts.

**What this is and is not.** It is evidence for a conjecture: *no nonzero finite Rule 30 configuration has an
eventually periodic column of period $2$ to $6$.* It is not a proof. The right halves were bounded, and "eventually
zero" was tested over 64 cells at depth 192. If the conjecture holds for every period, it implies Rule 30 Problem 1,
because the single black cell is a finite configuration.


## 6. The rungs from here

The Rule 30 rungs. The project-wide rungs (the lexicon, the GPU float check G1, Beal) are in
[PRIZE-PROBLEMS.md](PRIZE-PROBLEMS.md) §6.

| Rung | What | Who | Status |
|---|---|---|---|
| 1 | Rule 30, periods 2 to 6, exhaustive over small right halves, with the published control | Cloud, CPU | done: right support 14 at depth 192 (1,703,936 cases, 4m38s on one core), then right support 18 at depth 256 (27,262,976 cases, 4 cores); the control holds to $w = 8$ (256 maximisers); no eventually-zero left half anywhere |
| 2 | **The $p = 2$ structure.** The 7-periodic tails are explained (§5: 7-ring orbits). Next: find the forced left half's form for both period-2 traces, as Condrey did for constant traces; whether every forced left half eventually settles into some ring orbit was asked first and answered no: at depth 768, 1,999 of 2,048 period-2 right halves up to 10 cells show no period up to 128 over their last 256 cells, and the other 49 have periods 7, 14 or 28 (`rule30_rings.py`). So the argument must handle aperiodic left halves, and prove from their form that they are never eventually zero. Formalise in Lean. | Cloud | next |
| 3 | Periods $3$ to $6$ the same way, then look for the pattern across $p$: the uniform argument, which is the prize | Cloud | open |

The GPU is not needed for rungs 1 to 3 at these sizes. A CPU does them exactly in minutes. It enters if the search
must go much further, or for G1 and rung 4. The project's real advantage is not the hardware. It is the method: a
prediction before every run, a known answer beside every new one, and a counterfactual that must fail.

---

## 7. Rung 2, first progress: left-side rigidity (2026-10-04)

Working the period-2 case turned up a reduction that covers every period at once. Its proof needs an idea that has
not been found yet. Its evidence is exhaustive but finite.

**Lemma 1 (where column 1 is invisible).** With column 0's trace $\tau$ fixed, the forced left half depends on column
1 only at the times $t$ with $\tau(t) = 0$.

*Proof.* The only place column 1 enters is
$x_t(-1) = \tau(t+1) + \big(\tau(t) \vee x_t(1)\big) \bmod 2$. Where $\tau(t) = 1$, the "or" is 1 whatever $x_t(1)$
is. Every further left column is built from columns $-1$ and $0$ and those to their left. $\square$

*Checked:* `rule30_rigidity.py`, check R1: 880 of 880 random cases. For the alternating trace it gives explicit
columns (check R0, 2,000 random columns 1): column $-1$ is 1 at every odd time and $\lnot\sigma(2s)$ at time $2s$; column $-2$ is $\sigma(2s)$ at times
$2s$ and $\sigma(2s+2)$ at times $2s+1$. Here $\sigma$ is column 1. So $x_0(-1) + x_0(-2) = 1$, always.

**Lemma 2 (rotations are equivalent).** A finite configuration whose column is exactly periodic from $t = 0$, with
word $w$, is still finite one step later, and its column is then periodic with $w$ rotated by one place. So a finite
configuration exists for one rotation of a cyclic word exactly when it exists for all of them, and ruling out one
rotation per class is enough. $\square$

**Conjecture LR (left-side rigidity).** For every primitive word of period $p \ge 2$ and *every* column 1, not only
one made by a finite right half, the forced left half contains infinitely many ones.

**What LR would prove.** Suppose a finite configuration has a column that is eventually $p$-periodic. Shifting time
makes it exactly periodic, and the configuration stays finite, so its left half must be eventually zero. For
$p \ge 2$ that contradicts LR, and Condrey's theorem covers $p = 1$. So no column of any nonzero finite configuration
is eventually periodic, and in particular not the centre column from a single black cell. **LR implies Rule 30 Prize
Problem 1.** It is a statement about the left side alone, and it is stronger than the problem needs.

**Why it might be true: counting.** A word with $z$ zeros in its period leaves $z/p$ free bits of column 1 per left
cell (Lemma 1), and $z/p < 1$ for every primitive word with $p \ge 2$. The two extremes match what is known:
- the word "1" has no free bits, and its left half is Condrey's universal fibre;
- the word "0" has one free bit per cell, and column 1 $= 000\ldots$ gives the zero configuration, which is why
  Condrey's proof needed the right half for it.

Counting alone cannot prove LR. A single special column 1 could still make the left half vanish.

**Evidence** (`rule30_rigidity.py`, exhaustive over every column 1, from each starting depth whose earlier free bits
number at most 10; predictions written before the run):

| Check | Result |
|---|---|
| R1 control: column 1 is invisible where $\tau = 1$ | 880 of 880 |
| R2 control: for $\tau = 000\ldots$ the search reaches its cap from every depth, so it can see an infinite run | depths 1 to 11 |
| R3 control: for $\tau = 111\ldots$ the longest zero run is 1 | 1 |
| R4, main claim: every zero run ends (none reaches 400 cells), for all 26 primitive words of period 2 to 4 | **held**, every word, every depth tested (up to 44) |
| R4, bound: every run ends before depth $3d + 12$ | **refuted** for 0010 and 0100: a run from depth 14 ends at 62 |
| R5 (post hoc): longest run per word | grows with the starting depth for every word, peaking at the deepest depths tested (14 to 49) |

The deeper run (14 free bits, periods 2 to 5, the same predictions, Cloud on 4 cores) gives:

| Check | Result |
|---|---|
| R1 to R3 controls | all pass (R2 from depths 1 to 15) |
| R4, main claim: every zero run ends | **held for all 50 primitive words of period 2 to 5**, at every depth tested (up to 72) |
| R4, bound $3d + 12$ | **refuted** for 10 words: every rotation of 0001 and of 00001, and 100 |
| R5 (post hoc) | words with one zero per period are the most rigid. The longest runs of 01, 011, 0111 and 01111 stay between 17 and 23, even from depth 72. Words with mostly zeros allow the longest: 54 to 58 for the rotations of 0001, 45 to 66 for those of 00001. Rigidity grows as column 1's freedom $z/p$ falls, as the counting argument suggests. |

A first look for the rescaling found nothing yet (`rule30_witness.py`, recorded as a null result). The record runs
for the alternating trace from depths 9, 13 and 33 are 9, 17 and 33 cells long. Each is set by roughly the last
$d/2$ bits of column 1, and the earlier bits do not matter: 1, 3 and 21 prefixes reach the record. No substitution
mapping one depth's record column 1 to the next is visible by eye.

The single-zero words may not stay bounded either: the alternating trace's longest run jumps to 32 at depth 33
(exploration with 18 free bits, beyond this run's range). The words with mostly zeros are where LR is most at risk.

So the zero runs are not uniformly bounded. A run starting deeper can last longer: for the alternating trace, runs
from depth $d$ end near twice $d$. A proof of LR therefore needs a growth argument, of the form "a run from depth $d$
ends by $c \cdot d$". A local identity forbidding a fixed window of zeros is not enough. The self-similar endpoints
(runs ending near 16, 28-30, 64-68) suggest a renormalisation, mapping a long run at depth $d$ to a shorter one at
depth about $d/2$. That is the next thing to look for.

**What is open.** LR for any single word, as a theorem. Whether LR holds for long words that are mostly zeros
($0\ldots01$), which leave column 1 almost free. Whether the right half must be used after all, for some words.


## 8. The right side as a complement (2026-10-04)

The owner's suggestion, after §7: rather than ignore the right side, use it to complement the left. It works. The
left side alone leaves column 1 free, and then zero runs grow with depth (§7). But column 1 is not free: it is part of
the right side, and Rule 30 constrains it heavily.

**Lemma 3 (two local rules from the right side).** At column 1, Rule 30 reads
$\sigma(t+1) = \tau(t) + \big(\sigma(t) \vee x_t(2)\big) \bmod 2$, where $\tau$ is column 0 and $\sigma$ is column 1.
So, whatever column 2 does:

```math
\tau(t) = 0:\quad \sigma(t) = 1 \;\Rightarrow\; \sigma(t+1) = 1, \qquad\qquad
\tau(t) = 1:\quad \sigma(t+1) = 1 \;\Rightarrow\; \sigma(t) = 0 .
```

For the alternating trace, this means the part of column 1 that the left side sees, $e(s)$, never has two ones in a
row. $\square$ *Checked:* `rule30_twosided.py` T1 and T2 (every right half tried; random sequences violate the rules,
so they are not vacuous).

**How much the right side constrains column 1** (T3: every right half of width $n$ against the rules and against
everything):

| Column 1 prefixes, length $n$, trace 0101… | $n = 6$ | $n = 10$ | $n = 14$ | $n = 20$ |
|---|---|---|---|---|
| produced by some right half | 8 | 18 | 36 | **86** |
| allowed by Lemma 3's two rules | 17 | 99 | 577 | 8,119 |
| all sequences | 64 | 1,024 | 16,384 | 1,048,576 |

So the right side leaves column 1 almost no freedom: 86 sequences out of a million at length 20, growing roughly like
the square of the length rather than exponentially. Long columns 1 (T5, 3000 steps) are not eventually periodic. They
have very few distinct patterns: 95 distinct 64-cell patterns in 2000 cells, where a random sequence would have about
2000. They are not one universal sequence either: 13 to 17 of 39 random right halves give a tail found inside the
first one's.

**Lemma 3 alone is not enough** (T4, pre-registered). Searching only columns 1 that obey the two local rules, the
longest zero run is shorter than with a free column 1, but it still grows with depth: 18 for 0101… and 20 for
1010… by depth 40. The prediction that it would stay at or below 16 is **refuted**. The constraint that matters is
the exact one, the 86 sequences, not the two rules.

**Both sides exactly** (`rule30_twosided_exact.py`). Here column 1 comes from a real right half, and the left half is
forced from columns 0 and 1. This is a measurement, made before any prediction about it:

| Exact width of the right half | 8 | 10 | 12 | 14 | 16 | 18 | 20 |
|---|---|---|---|---|---|---|---|
| Longest zero run, trace 0101… (depth up to 192) | 14 | 15 | 15 | 20 | 20 | 20 | 20 |
| Longest zero run, trace 0001… (depth up to 192) | 13 | 13 | 17 | 17 | 17 | 17 | 17 |

At depth 192 the run length levels off with width, and over every right half up to 16 cells it shows no trend with
depth up to 256. (X3, below, shows that this plateau does not survive a deeper search.) Compare §7: with column 1
free, runs from depth $d$ reach about $d$ cells, 54 for 0001 from depth 18.

**Conjecture B (two-sided rigidity).** For each primitive word $w$ of period at least 2 and every finite right half,
every zero run in the forced left half ends. It was first stated with a constant bound: a number $B(w)$ such that the
forced left half never has more than $B(w)$ zeros in a row. The data at depth up to 192 suggested $B(01) = 20$ and
$B(0001) = 17$. The deeper search below refutes both values (X3: 24 and 26 by depth 384), so the constant-bound
form is dropped.

**What B would prove.** A left half in which every zero run ends is never eventually zero (with a constant bound,
it would have a one in every $B(w) + 1$ cells). So no finite configuration has a column periodic with $w$; together
with Lemma 2 (rotations) and Condrey's $p = 1$ theorem, the statement for every $w$ implies Rule 30 Prize Problem 1.
B is weaker than LR (§7) because it uses the right side. That is why it can hold where LR may fail.

**Why B looked like the better target, and what is left of that.** With a constant bound it would be a *bounded*
statement: no window of $B + 1$ cells is all zero. Bounded statements are the kind a finite check can prove, provided
the two-sided system has a finite-state description, and the 86 sequences, with their very low complexity, pointed
that way. X3 (below) removes the constant bound, and T6 (below) shows column 1 is not 2-automatic. What survives is
the slow growth: two-sided runs grow far more slowly than one-sided ones, so the right side still does most of the
work.

**Pre-registered X3, refuted.** The prediction was that the plateau holds further: $B$ still 20 (0101…) and 17
(0001…) for right halves of width 22 and 24 (about 33 million), at depth up to 384. It does not:

| Exact width of the right half | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 | 24 |
|---|---|---|---|---|---|---|---|---|---|
| Longest zero run, trace 0101…, depth up to 192 | 14 | 15 | 15 | 20 | 20 | 20 | 20 | 20 | 20 |
| Longest zero run, trace 0101…, depth up to 384 | 15 | 15 | 18 | 20 | 20 | 20 | 22 | 24 | 24 |
| Longest zero run, trace 0001…, depth up to 192 | 13 | 13 | 17 | 17 | 17 | 17 | 17 | 19 | 19 |
| Longest zero run, trace 0001…, depth up to 384 | 13 | 14 | 17 | 17 | 19 | 26 | 26 | 26 | 26 |

Both controls passed: the search reproduces the recorded values (X1), and with a free column 1 the same window holds
runs of 33 cells for 0101… and 54 for 0001…, so long runs fit and can be seen (X2). So $B(01) = 20$ and
$B(0001) = 17$ were artefacts of stopping at depth 192. The runs keep growing with depth, slowly: 24 and 26 by depth
384, against runs of about $d$ from depth $d$ with column 1 free. At depth 384 the runs level off with width again,
at 24 for widths 22 and 24 (0101…) and at 26 from width 18 to 24 (0001…). That is the same shape as at depth 192, so
the longest run looks like a function of the depth searched, not of the width. **Conjecture B is weakened
accordingly**: not a constant bound, but *every two-sided zero run ends* (the forced left half is never eventually
zero). That weaker statement is all that Prize Problem 1 needs. It is no longer a finite check by itself, which is why
§8.2 looks at where the long runs come from.

**A first look at column 1's structure** (T6, a measurement). Column 1 is locally rigid but globally chaotic.
- **Locally it is tightly constrained.** Over 61,440 steps it contains only 13 distinct 8-cell patterns and 21
  distinct 16-cell patterns; a random sequence would contain 256 and about 61,000.
- **Globally it is not simple.** At 256 cells there are about 20,000 distinct patterns, and the count is still growing
  about 16-fold per doubling of the length.
- **It is not generated by a finite automaton in base 2.** Its 2-kernel grows almost like a random sequence's (492 of
  512 at $k = 9$; Thue–Morse, the control, has 2).
- **One exception fits §5.** A right half of width 18 gives a column 1 that becomes exactly 14-periodic: a copy of a
  14-ring orbit, next to a 2-periodic column 0. That is not a counterexample to Jen, because the left half it forces
  is infinite.

So the simplest route to a finite proof, "column 1 is generated by an automaton", is closed (recorded as a null
result). The zero runs are local events, though, and so are column 1's constraints.

**Next.** Describe column 1's *local* language: the set of patterns it can contain, of each length. Then find whether
the forced left half's zero runs depend only on that local language. If they do, B becomes a finite check.

*Moved to volumes on 2026-10-28 (Local, at the owner's request).* Section 8's sub-sections, 723 KB in all, now live
unchanged in three volumes in [reports/rule30-prize/](reports/rule30-prize/). The table lists every one, in order, with a
link straight to it. New sub-sections can be added here until this section passes about 250 KB again, then rotate
the same way.

| Sub-section | Volume |
|---|---|
| [8.1 The four arms (the owner's design, 2026-10-04)](reports/rule30-prize/RULE30-PRIZE-8.1.md#81-the-four-arms-the-owners-design-2026-10-04) | 1 |
| [8.2 Why runs of 13 were missing: templates, and where Fibonacci really is (2026-10-04)](reports/rule30-prize/RULE30-PRIZE-8.1.md#82-why-runs-of-13-were-missing-templates-and-where-fibonacci-really-is-2026-10-04) | 1 |
| [8.3 What was already known, Rule 30's siblings, and the owner's harmonics (2026-10-04)](reports/rule30-prize/RULE30-PRIZE-8.1.md#83-what-was-already-known-rule-30s-siblings-and-the-owners-harmonics-2026-10-04) | 1 |
| [8.4 Column 1 is a turning wheel: the owner's complex-number lead (2026-10-04)](reports/rule30-prize/RULE30-PRIZE-8.1.md#84-column-1-is-a-turning-wheel-the-owners-complex-number-lead-2026-10-04) | 1 |
| [8.5 The universal wheel (2026-10-04)](reports/rule30-prize/RULE30-PRIZE-8.1.md#85-the-universal-wheel-2026-10-04) | 1 |
| [8.6 Order in, noise out: the left side churns the wheel (2026-10-04)](reports/rule30-prize/RULE30-PRIZE-8.1.md#86-order-in-noise-out-the-left-side-churns-the-wheel-2026-10-04) | 1 |
| [8.7 A slip is one particle (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#87-a-slip-is-one-particle-2026-10-05) | 1 |
| [8.8 The walls kick the wheel in notches; orbits and jumps (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#88-the-walls-kick-the-wheel-in-notches-orbits-and-jumps-2026-10-05) | 1 |
| [8.9 Where the long runs come from, and kicking the drive (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#89-where-the-long-runs-come-from-and-kicking-the-drive-2026-10-05) | 1 |
| [8.10 Does the wheel turn at a constant rate? (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#810-does-the-wheel-turn-at-a-constant-rate-2026-10-05) | 1 |
| [8.11 Is the wheel chaotic? A flywheel kicked by a chaotic machine (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#811-is-the-wheel-chaotic-a-flywheel-kicked-by-a-chaotic-machine-2026-10-05) | 1 |
| [8.12 The ladder's first rungs: a thin layer tames the adversary (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#812-the-ladders-first-rungs-a-thin-layer-tames-the-adversary-2026-10-05) | 1 |
| [8.13 Jen's theorem settles every periodic column 1: a correction (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#813-jens-theorem-settles-every-periodic-column-1-a-correction-2026-10-05) | 1 |
| [8.14 At depth the runs keep growing: a zero run costs about one bit (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#814-at-depth-the-runs-keep-growing-a-zero-run-costs-about-one-bit-2026-10-05) | 1 |
| [8.15 Rule 30 as a random-number generator: where its randomness fails (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#815-rule-30-as-a-random-number-generator-where-its-randomness-fails-2026-10-05) | 1 |
| [8.16 Luck, not structure; and a bottleneck, not a cost (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#816-luck-not-structure-and-a-bottleneck-not-a-cost-2026-10-05) | 1 |
| [8.17 The bottleneck, measured: the channel, not the seed (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#817-the-bottleneck-measured-the-channel-not-the-seed-2026-10-05) | 1 |
| [8.18 White triangles and the kicks: the owner's lead (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#818-white-triangles-and-the-kicks-the-owners-lead-2026-10-05) | 1 |
| [8.19 Upwards and sideways: the owner's two pyramid questions (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#819-upwards-and-sideways-the-owners-two-pyramid-questions-2026-10-05) | 1 |
| [8.20 How much information column 1 can carry: exact bounds (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#820-how-much-information-column-1-can-carry-exact-bounds-2026-10-05) | 1 |
| [8.21 The search widened: every right half up to 32 cells (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#821-the-search-widened-every-right-half-up-to-32-cells-2026-10-05) | 1 |
| [8.22 Two half-lines, one column 0: chaos on the left, a channel on the right (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#822-two-half-lines-one-column-0-chaos-on-the-left-a-channel-on-the-right-2026-10-05) | 1 |
| [8.23 Columns as numbers: the owner's irrational-number question (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#823-columns-as-numbers-the-owners-irrational-number-question-2026-10-05) | 1 |
| [8.24 The complementary pair: two irrational numbers that must add up to one (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#824-the-complementary-pair-two-irrational-numbers-that-must-add-up-to-one-2026-10-05) | 1 |
| [8.25 The owner's lightning (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#825-the-owners-lightning-2026-10-05) | 1 |
| [8.26 How irrational numbers are proved, and which way might fit (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#826-how-irrational-numbers-are-proved-and-which-way-might-fit-2026-10-05) | 1 |
| [8.27 The pyramid as a stack of rational numbers (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#827-the-pyramid-as-a-stack-of-rational-numbers-2026-10-05) | 1 |
| [8.28 Does the lightning gravitate to certain paths? (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#828-does-the-lightning-gravitate-to-certain-paths-2026-10-05) | 1 |
| [8.29 The pyramid as a maze (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#829-the-pyramid-as-a-maze-2026-10-05) | 1 |
| [8.30 The band of stripes, and where the chaos stops (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#830-the-band-of-stripes-and-where-the-chaos-stops-2026-10-05) | 1 |
| [8.31 One left side or many? Rowland's question, answered both ways (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#831-one-left-side-or-many-rowlands-question-answered-both-ways-2026-10-05) | 1 |
| [8.32 The wheel on the grid: the owner's square peg (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#832-the-wheel-on-the-grid-the-owners-square-peg-2026-10-05) | 1 |
| [8.33 The entropy squeeze: a period-2 counterexample must be almost frozen (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#833-the-entropy-squeeze-a-period-2-counterexample-must-be-almost-frozen-2026-10-05) | 1 |
| [8.34 Where Problems 1 and 2 meet (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#834-where-problems-1-and-2-meet-2026-10-05) | 1 |
| [8.35 Does Rule 30's coin tip? The owner's matter–antimatter question (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#835-does-rule-30s-coin-tip-the-owners-matterantimatter-question-2026-10-05) | 1 |
| [8.36 Lead 1: the records to depth 65, and a sharp conjecture (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#836-lead-1-the-records-to-depth-65-and-a-sharp-conjecture-2026-10-05) | 1 |
| [8.37 Local's depths 69 to 81, and the owner's Enigma lead (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#837-locals-depths-69-to-81-and-the-owners-enigma-lead-2026-10-05) | 1 |
| [8.38 Why the records stop at 0.8 d: the walks merge (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#838-why-the-records-stop-at-08-d-the-walks-merge-2026-10-05) | 1 |
| [8.39 The same problem as Rule 30 against a wall (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#839-the-same-problem-as-rule-30-against-a-wall-2026-10-05) | 1 |
| [8.40 Black, white, both: the owner's three games, for every word up to period 4 (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#840-black-white-both-the-owners-three-games-for-every-word-up-to-period-4-2026-10-05) | 1 |
| [8.41 The information race, counted (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#841-the-information-race-counted-2026-10-05) | 1 |
| [8.42 One law for every word: total width plus a logarithm (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#842-one-law-for-every-word-total-width-plus-a-logarithm-2026-10-05) | 1 |
| [8.43 What sets a kick's size? The owner's drifting hole (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#843-what-sets-a-kicks-size-the-owners-drifting-hole-2026-10-05) | 1 |
| [8.44 The kick game: the wheel's rigidity is a constraint, not a bound (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#844-the-kick-game-the-wheels-rigidity-is-a-constraint-not-a-bound-2026-10-05) | 1 |
| [8.45 Mahler's 3/2 problem has the same structure, and stops in the same place (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#845-mahlers-32-problem-has-the-same-structure-and-stops-in-the-same-place-2026-10-05) | 1 |
| [8.46 Is it unresolvable? The owner's Turing question (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#846-is-it-unresolvable-the-owners-turing-question-2026-10-05) | 1 |
| [8.47 The wide survey: nature, the other disciplines, and OpenAI's claim (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#847-the-wide-survey-nature-the-other-disciplines-and-openais-claim-2026-10-05) | 1 |
| [8.48 The owner's MoltenVK question: randomness that only one platform showed (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#848-the-owners-moltenvk-question-randomness-that-only-one-platform-showed-2026-10-05) | 1 |
| [8.49 Addendum to §8.47: philosophy and logic (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#849-addendum-to-847-philosophy-and-logic-2026-10-05) | 1 |
| [8.50 Gates and truth: the owner's NAND question (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#850-gates-and-truth-the-owners-nand-question-2026-10-05) | 1 |
| [8.51 The counting form, measured, and the tetralemma's fourth game (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#851-the-counting-form-measured-and-the-tetralemmas-fourth-game-2026-10-05) | 1 |
| [8.52 What the right part pays: in lumps, with bounded debt (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#852-what-the-right-part-pays-in-lumps-with-bounded-debt-2026-10-05) | 1 |
| [8.53 The debt, at total widths beyond 100: flat, and paid at the wheel's formation (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#853-the-debt-at-total-widths-beyond-100-flat-and-paid-at-the-wheels-formation-2026-10-05) | 1 |
| [8.54 Jen's theorem with a clock: a window of periodicity cannot outlast the left edge (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#854-jens-theorem-with-a-clock-a-window-of-periodicity-cannot-outlast-the-left-edge-2026-10-05) | 1 |
| [8.55 Question 4, closed: what Kari and Kopra's argument gives for Rule 30 (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#855-question-4-closed-what-kari-and-kopras-argument-gives-for-rule-30-2026-10-05) | 1 |
| [8.56 What is excluded outright: the left edge is at least 249 cells away (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#856-what-is-excluded-outright-the-left-edge-is-at-least-249-cells-away-2026-10-05) | 1 |
| [8.57 No pure rotation works: every Sturmian column 1 is excluded (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.1.md#857-no-pure-rotation-works-every-sturmian-column-1-is-excluded-2026-10-05) | 1 |
| [8.58 The window principle: Theorem A′, and what the Collatz twin shows is missing (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.2.md#858-the-window-principle-theorem-a-and-what-the-collatz-twin-shows-is-missing-2026-10-05) | 2 |
| [8.59 The window principle meets the band of stripes: a repeat is a white run, and the left side is never white for long (2026-10-05)](reports/rule30-prize/RULE30-PRIZE-8.2.md#859-the-window-principle-meets-the-band-of-stripes-a-repeat-is-a-white-run-and-the-left-side-is-never-white-for-long-2026-10-05) | 2 |
| [8.60 The small items: the wall never sees the far end, the mostly-zero words, and the left side to a million (2026-10-06)](reports/rule30-prize/RULE30-PRIZE-8.2.md#860-the-small-items-the-wall-never-sees-the-far-end-the-mostly-zero-words-and-the-left-side-to-a-million-2026-10-06) | 2 |
| [8.61 Question 3 assessed: the certificate it asks for is question 1 in another costume (2026-10-06)](reports/rule30-prize/RULE30-PRIZE-8.2.md#861-question-3-assessed-the-certificate-it-asks-for-is-question-1-in-another-costume-2026-10-06) | 2 |
| [8.62 The owner's question: what "period 1" means, whether period 2 had to follow, and the ladder by freedom (2026-10-06)](reports/rule30-prize/RULE30-PRIZE-8.2.md#862-the-owners-question-what-period-1-means-whether-period-2-had-to-follow-and-the-ladder-by-freedom-2026-10-06) | 2 |
| [8.63 If period 2 had never been proposed: the next steps after Condrey, and a reframing of the work (2026-10-06)](reports/rule30-prize/RULE30-PRIZE-8.2.md#863-if-period-2-had-never-been-proposed-the-next-steps-after-condrey-and-a-reframing-of-the-work-2026-10-06) | 2 |
| [8.64 What makes 30 special among the 256: the left band of every rule (2026-10-06)](reports/rule30-prize/RULE30-PRIZE-8.2.md#864-what-makes-30-special-among-the-256-the-left-band-of-every-rule-2026-10-06) | 2 |
| [8.65 Rule 210, the one sibling: conjecture LR is false there (2026-10-06)](reports/rule30-prize/RULE30-PRIZE-8.2.md#865-rule-210-the-one-sibling-conjecture-lr-is-false-there-2026-10-06) | 2 |
| [8.66 The leftward light speed is the background's: $0.246 = 1 - 0.41 \times 1.84$; the checkerboard heals, the band locks (2026-10-06)](reports/rule30-prize/RULE30-PRIZE-8.2.md#866-the-leftward-light-speed-is-the-backgrounds-0246--1---041-times-184-the-checkerboard-heals-the-band-locks-2026-10-06) | 2 |
| [8.67 Rule 30 on rings to $n = 24$, complete: cycle counts, transients longer than cycles, and every cycle a glider on prime rings (2026-10-06)](reports/rule30-prize/RULE30-PRIZE-8.2.md#867-rule-30-on-rings-to-n--24-complete-cycle-counts-transients-longer-than-cycles-and-every-cycle-a-glider-on-prime-rings-2026-10-06) | 2 |
| [8.68 The triangle census of the single cell: the core's triangles are the uniform measure's to three decimals, $3 \cdot 2^{-(L+4)}$ per cell (2026-10-06)](reports/rule30-prize/RULE30-PRIZE-8.2.md#868-the-triangle-census-of-the-single-cell-the-cores-triangles-are-the-uniform-measures-to-three-decimals-3-cdot-2-l4-per-cell-2026-10-06) | 2 |
| [8.69 The slow walls from the left: the left half's own conditions stop every seed of width 16 within one period (2026-10-06)](reports/rule30-prize/RULE30-PRIZE-8.2.md#869-the-slow-walls-from-the-left-the-left-halfs-own-conditions-stop-every-seed-of-width-16-within-one-period-2026-10-06) | 2 |
| [8.70 Rule 30's velocity is Rule 210: time derivatives of the rule, and the prize as a difference equation (2026-10-06)](reports/rule30-prize/RULE30-PRIZE-8.2.md#870-rule-30s-velocity-is-rule-210-time-derivatives-of-the-rule-and-the-prize-as-a-difference-equation-2026-10-06) | 2 |
| [8.71 Turning rows: the all-S ring turns 14 cells a step, rows outrunning light are rings, and pattern speed is not signal speed (2026-10-09)](reports/rule30-prize/RULE30-PRIZE-8.2.md#871-turning-rows-the-all-s-ring-turns-14-cells-a-step-rows-outrunning-light-are-rings-and-pattern-speed-is-not-signal-speed-2026-10-09) | 2 |
| [8.72 Interlocking shapes: Rule 30 is eight jigsaw tiles, its periodic histories are single-brick walls, and next to the wall a periodic column 1 crystallises the left half (2026-10-09)](reports/rule30-prize/RULE30-PRIZE-8.2.md#872-interlocking-shapes-rule-30-is-eight-jigsaw-tiles-its-periodic-histories-are-single-brick-walls-and-next-to-the-wall-a-periodic-column-1-crystallises-the-left-half-2026-10-09) | 2 |
| [8.73 The triangles on the right edge are a ruler sequence (2026-10-09)](reports/rule30-prize/RULE30-PRIZE-8.2.md#873-the-triangles-on-the-right-edge-are-a-ruler-sequence-2026-10-09) | 2 |
| [8.74 Where the left side's order ends: an exact boundary, a random walk about a quarter of light speed (2026-10-09)](reports/rule30-prize/RULE30-PRIZE-8.2.md#874-where-the-left-sides-order-ends-an-exact-boundary-a-random-walk-about-a-quarter-of-light-speed-2026-10-09) | 2 |
| [8.75 Triangle ladders: descending from triangle to triangle (2026-10-09)](reports/rule30-prize/RULE30-PRIZE-8.2.md#875-triangle-ladders-descending-from-triangle-to-triangle-2026-10-09) | 2 |
| [8.76 Period 1, proved again here: an audit of Condrey's theorem (2026-10-09 14:17 BST)](reports/rule30-prize/RULE30-PRIZE-8.2.md#876-period-1-proved-again-here-an-audit-of-condreys-theorem-2026-10-09-1417-bst) | 2 |
| [8.77 Rule 30's entropy is its width-2 trace's, and the 2-adic frame second-read (2026-10-09 16:29 BST)](reports/rule30-prize/RULE30-PRIZE-8.2.md#877-rule-30s-entropy-is-its-width-2-traces-and-the-2-adic-frame-second-read-2026-10-09-1629-bst) | 2 |
| [8.78 The status board's history, archived at the third triage (2026-10-09)](reports/rule30-prize/RULE30-PRIZE-8.2.md#878-the-status-boards-history-archived-at-the-third-triage-2026-10-09) | 2 |
| [8.79 The status board's history, archived at the fourth triage (2026-10-10)](reports/rule30-prize/RULE30-PRIZE-8.2.md#879-the-status-boards-history-archived-at-the-fourth-triage-2026-10-10) | 2 |
| [8.80 The pattern as one chain, and the chain split at the front (the owner's lead, 2026-10-10)](reports/rule30-prize/RULE30-PRIZE-8.2.md#880-the-pattern-as-one-chain-and-the-chain-split-at-the-front-the-owners-lead-2026-10-10) | 2 |
| [8.81 The triangle law integrates to one half; the white area of each side, split at the front (the owner's lead, 2026-10-10)](reports/rule30-prize/RULE30-PRIZE-8.2.md#881-the-triangle-law-integrates-to-one-half-the-white-area-of-each-side-split-at-the-front-the-owners-lead-2026-10-10) | 2 |
| [8.82 The two wall phases' records are coupled exactly through black runs (swarm lane q2, graded; 2026-10-10)](reports/rule30-prize/RULE30-PRIZE-8.2.md#882-the-two-wall-phases-records-are-coupled-exactly-through-black-runs-swarm-lane-q2-graded-2026-10-10) | 2 |
| [8.83 Every minimal absent word to length 48 is excluded by a strip no wider than itself; the trace form is tight (swarm lane q3, graded; 2026-10-10)](reports/rule30-prize/RULE30-PRIZE-8.2.md#883-every-minimal-absent-word-to-length-48-is-excluded-by-a-strip-no-wider-than-itself-the-trace-form-is-tight-swarm-lane-q3-graded-2026-10-10) | 2 |
| [8.84 The free record to depth 73, the (10)^k family bounded, and a Jen-type theorem for finite patterns (swarm lane q1, graded; 2026-10-10)](reports/rule30-prize/RULE30-PRIZE-8.2.md#884-the-free-record-to-depth-73-the-10k-family-bounded-and-a-jen-type-theorem-for-finite-patterns-swarm-lane-q1-graded-2026-10-10) | 2 |
| [8.85 The 1100 wall to depth 100: the record stays small, the lock structure of column 1, no proof (swarm lane q4, graded; 2026-10-10)](reports/rule30-prize/RULE30-PRIZE-8.2.md#885-the-1100-wall-to-depth-100-the-record-stays-small-the-lock-structure-of-column-1-no-proof-swarm-lane-q4-graded-2026-10-10) | 2 |
| [8.86 Is the right-half language sofic? Evidence against, a certified entropy ceiling, and a death criterion (swarm lane q5, graded; 2026-10-10)](reports/rule30-prize/RULE30-PRIZE-8.2.md#886-is-the-right-half-language-sofic-evidence-against-a-certified-entropy-ceiling-and-a-death-criterion-swarm-lane-q5-graded-2026-10-10) | 2 |
| [8.87 The first swarm round, summarised: what held, what fell, what it changes (2026-10-10, 23:16 BST)](reports/rule30-prize/RULE30-PRIZE-8.2.md#887-the-first-swarm-round-summarised-what-held-what-fell-what-it-changes-2026-10-10-2316-bst) | 2 |
| [8.88 The check-free conjecture and the forced-only records: the strategy swarm's first target, Cloud-replicated (2026-10-11, 02:22 BST)](reports/rule30-prize/RULE30-PRIZE-8.2.md#888-the-check-free-conjecture-and-the-forced-only-records-the-strategy-swarms-first-target-cloud-replicated-2026-10-11-0222-bst) | 2 |
| [8.89 The room switch: from the forced-only door to the visible language's certified absent words (2026-10-11 07:56 BST)](reports/rule30-prize/RULE30-PRIZE-8.2.md#889-the-room-switch-from-the-forced-only-door-to-the-visible-languages-certified-absent-words-2026-10-11-0756-bst) | 2 |
| [8.90 The carry of Rule 30: the Gray correction is a two-time AND, and the column carry is exactly solvable (2026-10-11 10:06 BST)](reports/rule30-prize/RULE30-PRIZE-8.2.md#890-the-carry-of-rule-30-the-gray-correction-is-a-two-time-and-and-the-column-carry-is-exactly-solvable-2026-10-11-1006-bst) | 2 |
| [8.91 The status board's history, archived at the fifth triage (2026-10-11 14:40 BST)](reports/rule30-prize/RULE30-PRIZE-8.3.md#891-the-status-boards-history-archived-at-the-fifth-triage-2026-10-11-1440-bst) | 3 |
| [8.92 The fair-coin question, and the pair and price table (2026-10-13 11:32 BST)](reports/rule30-prize/RULE30-PRIZE-8.3.md#892-the-fair-coin-question-and-the-pair-and-price-table-2026-10-13-1132-bst) | 3 |
| [8.93 The cheating coin one level up: fairness levels, simple and deep cheats, and where cheats come from (2026-10-13 12:05 BST)](reports/rule30-prize/RULE30-PRIZE-8.3.md#893-the-cheating-coin-one-level-up-fairness-levels-simple-and-deep-cheats-and-where-cheats-come-from-2026-10-13-1205-bst) | 3 |
| [8.94 The left horizon to width 32: neither the edge law nor the coin law; the bulk pays like a coin, the champions in lumps (2026-10-13 12:40 BST)](reports/rule30-prize/RULE30-PRIZE-8.3.md#894-the-left-horizon-to-width-32-neither-the-edge-law-nor-the-coin-law-the-bulk-pays-like-a-coin-the-champions-in-lumps-2026-10-13-1240-bst) | 3 |
| [8.95 The black-run records in git: 8.82's coupling exact to depth 40, and the zero records are black runs born one step earlier (2026-10-13 13:22 BST)](reports/rule30-prize/RULE30-PRIZE-8.3.md#895-the-black-run-records-in-git-882s-coupling-exact-to-depth-40-and-the-zero-records-are-black-runs-born-one-step-earlier-2026-10-13-1322-bst) | 3 |
| [8.96 The 18s at depths 125 .. 138 are several runs, split at the exact 17s (STRATEGY-PLAN.md section 6) (2026-10-13 13:39 BST)](reports/rule30-prize/RULE30-PRIZE-8.3.md#896-the-18s-at-depths-125--138-are-several-runs-split-at-the-exact-17s-strategy-planmd-section-6-2026-10-13-1339-bst) | 3 |
| [8.97 GC1176's extremal P corner is empty beyond r = 1: its open residues 9 and 13 close with a ten-cell core (2026-10-13 16:10 BST)](reports/rule30-prize/RULE30-PRIZE-8.3.md#897-gc1176s-extremal-p-corner-is-empty-beyond-r--1-its-open-residues-9-and-13-close-with-a-ten-cell-core-2026-10-13-1610-bst) | 3 |
| [8.98 History-restricted records: an equivalent target; record witnesses without a real past; the kick-game containment withdrawn (2026-10-13 23:06 BST)](reports/rule30-prize/RULE30-PRIZE-8.3.md#898-history-restricted-records-an-equivalent-target-record-witnesses-without-a-real-past-the-kick-game-containment-withdrawn-2026-10-13-2306-bst) | 3 |
| [8.99 Mixed S/L residences: no small constant record budget; a uniform one remains open (2026-10-14 00:03 BST)](reports/rule30-prize/RULE30-PRIZE-8.3.md#899-mixed-sl-residences-no-small-constant-record-budget-a-uniform-one-remains-open-2026-10-14-0003-bst) | 3 |
| [8.100 Code, unwritable numbers and time: the owner's three foundations questions (2026-10-14 15:52 BST, Cloud)](reports/rule30-prize/RULE30-PRIZE-8.3.md#8100-code-unwritable-numbers-and-time-the-owners-three-foundations-questions-2026-10-14-1552-bst-cloud) | 3 |
| [8.101 The rigidity hunt: what a counterexample builds on the far side of each fold (2026-10-14 16:11 BST, Cloud)](reports/rule30-prize/RULE30-PRIZE-8.3.md#8101-the-rigidity-hunt-what-a-counterexample-builds-on-the-far-side-of-each-fold-2026-10-14-1611-bst-cloud) | 3 |
| [8.102 Door (d): kicks are not born where cr fires at the wall; the echo picture is exact but not local (2026-10-14 16:30 BST, Cloud)](reports/rule30-prize/RULE30-PRIZE-8.3.md#8102-door-d-kicks-are-not-born-where-cr-fires-at-the-wall-the-echo-picture-is-exact-but-not-local-2026-10-14-1630-bst-cloud) | 3 |
| [8.103 Compounded shortcuts, and the kick's echoes as interference (2026-10-14 16:45 BST, Cloud)](reports/rule30-prize/RULE30-PRIZE-8.3.md#8103-compounded-shortcuts-and-the-kicks-echoes-as-interference-2026-10-14-1645-bst-cloud) | 3 |
| [8.104 The record comb: the record checked with today's tools (2026-10-14 16:54 BST, Cloud)](reports/rule30-prize/RULE30-PRIZE-8.3.md#8104-the-record-comb-the-record-checked-with-todays-tools-2026-10-14-1654-bst-cloud) | 3 |
| [8.105 INSTINCT-CLOUD S7: the kick's coherence revivals are correlations, carried by class-split rigidity (2026-10-14 17:24 BST, Cloud)](reports/rule30-prize/RULE30-PRIZE-8.3.md#8105-instinct-cloud-s7-the-kicks-coherence-revivals-are-correlations-carried-by-class-split-rigidity-2026-10-14-1724-bst-cloud) | 3 |
| [8.106 The record comb: Intel's swarm (2026-10-14 17:55 BST, Intel)](reports/rule30-prize/RULE30-PRIZE-8.3.md#8106-the-record-comb-intels-swarm-2026-10-14-1755-bst-intel) | 3 |
| [8.107 S8 certified: the kick's local alphabet four and ten rows back (2026-10-14 18:03 BST, Cloud)](reports/rule30-prize/RULE30-PRIZE-8.3.md#8107-s8-certified-the-kicks-local-alphabet-four-and-ten-rows-back-2026-10-14-1803-bst-cloud) | 3 |
| [8.108 The record comb, lane B: the stored certificates (2026-10-14 18:46 BST, Local)](reports/rule30-prize/RULE30-PRIZE-8.3.md#8108-the-record-comb-lane-b-the-stored-certificates-2026-10-14-1846-bst-local) | 3 |
| [8.109 Door (c): Mahler's admissible set meets its doubles and triples only at 0 (2026-10-14 20:02 BST, Cloud)](reports/rule30-prize/RULE30-PRIZE-8.3.md#8109-door-c-mahlers-admissible-set-meets-its-doubles-and-triples-only-at-0-2026-10-14-2002-bst-cloud) | 3 |
| [8.110 Door (a): the lifting table (2026-10-14 20:28 BST, Cloud)](reports/rule30-prize/RULE30-PRIZE-8.3.md#8110-door-a-the-lifting-table-2026-10-14-2028-bst-cloud) | 3 |
| [8.111 S13's kill test: no periodic witness for Mahler's sign +1 multipliers, and the pull tips to halt (2026-10-14 22:10 BST, Cloud)](reports/rule30-prize/RULE30-PRIZE-8.3.md#8111-s13s-kill-test-no-periodic-witness-for-mahlers-sign-1-multipliers-and-the-pull-tips-to-halt-2026-10-14-2210-bst-cloud) | 3 |
| [8.112 S14's kill test: 13 is anti-invariant despite its sign, and the sign rule's converse fails for Mahler (2026-10-14 22:17 BST, Cloud)](reports/rule30-prize/RULE30-PRIZE-8.3.md#8112-s14s-kill-test-13-is-anti-invariant-despite-its-sign-and-the-sign-rules-converse-fails-for-mahler-2026-10-14-2217-bst-cloud) | 3 |
| [8.113 The swarm at full burn: map the wall, propose crossings, refute them (2026-10-14 22:47 BST, Cloud)](reports/rule30-prize/RULE30-PRIZE-8.3.md#8113-the-swarm-at-full-burn-map-the-wall-propose-crossings-refute-them-2026-10-14-2247-bst-cloud) | 3 |
| [8.114 The coin's shape, and the owner's primes hunch (2026-10-15 11:56 BST, Cloud)](reports/rule30-prize/RULE30-PRIZE-8.3.md#8114-the-coins-shape-and-the-owners-primes-hunch-2026-10-15-1156-bst-cloud) | 3 |
| [8.115 First principles: what Wolfram set out to do, why Rule 30 is sticky, and the wall's name in complexity theory (2026-10-15 12:29 BST, Cloud)](reports/rule30-prize/RULE30-PRIZE-8.3.md#8115-first-principles-what-wolfram-set-out-to-do-why-rule-30-is-sticky-and-the-walls-name-in-complexity-theory-2026-10-15-1229-bst-cloud) | 3 |
| [8.116 Thesis: the prize is a question about observers, and the record is a catalogue of which observers the column defeats (2026-10-15 12:57 BST, Cloud)](reports/rule30-prize/RULE30-PRIZE-8.3.md#8116-thesis-the-prize-is-a-question-about-observers-and-the-record-is-a-catalogue-of-which-observers-the-column-defeats-2026-10-15-1257-bst-cloud) | 3 |
| [8.117 The death time at width 52 is exactly 96, kernel-checked (2026-10-23 21:15 BST, Local)](reports/rule30-prize/RULE30-PRIZE-8.3.md#8117-the-death-time-at-width-52-is-exactly-96-kernel-checked-2026-10-23-2115-bst-local) | 3 |

[8.118 Finite-prefix repeat-obstruction transfer, formal delivery GC2095](reports/rule30-prize/RULE30-PRIZE-8.3.md#8118-formal-delivery-finite-prefix-changes-preserve-repeat-obstructions-gc2095-29-october2026).

[8.119 Periodic-driver masking and the two remaining driver classes, GC2214](reports/rule30-prize/RULE30-PRIZE-8.3.md#8119-periodic-driver-masking-and-the-two-remaining-driver-classes-gc2214-30-october-2026).

[8.120 Synchronizing carriers and the remaining finite-history guard, GC2226](reports/rule30-prize/RULE30-PRIZE-8.3.md#8120-synchronizing-carriers-and-the-remaining-finite-history-guard-gc2226-30-october-2026).


[8.121 Local group transport and the boundary needed for profile decoding, GC2229–GC2230](reports/rule30-prize/RULE30-PRIZE-8.3.md#8121-local-group-transport-and-the-boundary-needed-for-profile-decoding-gc2229gc2230-30-october-2026).


**Finite-past side-result pointer, GC2290–GC2291 (30 October2026):** [source preparation, attribution and low-mass classification](reports/GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#live-checkpoint-gc2290gc2291). Physical finite-parent/root/age objects already occur in Karttunen's2016 OEIS records; B packages credited structure, with four modules prepared but UNCOMPILED. A separate solo hand classification bounds the age of every four-black row by4, sharply; independent carrying read pending. The general fixed-mass question belongs to CONSTELLATION, not the prize board. No centre-column exclusion or new submission follows.
