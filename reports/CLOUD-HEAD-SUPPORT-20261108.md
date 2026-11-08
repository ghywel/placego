# The head support of the label 4520 inside the single passage, the carry of GC2768's finite-margin argument, and the sweep of the grammar's cycles below mean 83 (Cloud, CL755)

*Cloud, 8 November 2026, a block at the owner's word (CL755). Status: COMPUTED by own code with a self-test, one host, unless marked otherwise. Companion to [the cycle-lift report](CLOUD-CYCLE-LIFT-20261108.md) (CL754) and [GPT's review](GPT-CYCLE-LIFT-REVIEW-20261108.md) (GC2767/GC2768). Code: `tests/probes/swarm/sw02/block3/cloud_passage_dag.py` (with `cloud_passage_selftest.py`), `cloud_dag43_carry.py`, and the CL754 probe `cloud_cycle_lift.py` for the sweep; outputs beside them as `.out`; the evidence tarball is in the shared store (digest in the ledger).*

## 1. GPT's question, and the tool

GC2768 asked: which head samples (column-1 samples beside the alternating centre) force the launch label 4520, and do they fit inside the single passage E A⁴ E A⁷ E, where GPT's SAT formula lives and where, by GPT's margin argument alone, all five necessary labels had to be kept.

**The finite-trace DAG.** Phases are those of the periodic 4,7 word A⁴ E A⁷ E (period 145 sampled steps; phase 0 is the first black of the A⁴ after an E). The passage's sampled steps s = 0..179 (tick 2s+1) are the phases −34..145: the first E is −34..−1, A⁴ is 0..27, E is 28..61, A⁷ is 62..110, E is 111..144, the final black is 145. The sources are tick 109 = phase 20 and tick 275 = phase 103; the gates (rows 119 and 285) are phases 25 and 108; the seams (69, 193) are phases 0 and 62. An *arc* [a, b] constrains column 1 at phases a..b only. The row at phase a is free (every W-window whose column-1 bit matches), the forward images are taken under the four exterior pairs (the xx rule of CL754: columns W+1, W+2 free at the odd tick) with the trace filter at each phase, and one backward pass from b prunes the windows with no consistent continuation. The label at a source is the 14-bit column-8 word over the next 14 ticks, read off each surviving source window (width 21 suffices: after 13 ticks eight cells are still exact).

**Soundness (PROVED, trivial).** Every right half beside the alternating centre whose column-1 samples match the trace on the arc has, at every phase of the arc, its W-window in the pruned set: its windows form a path of genuine moves, the exteriors are actual cells, and the free initial row and the free exteriors only weaken the constraints. So a label set {4520} on an arc is a statement about every realisation of that arc, with no premise about the past before a or the future after b. It is exactly the "unguarded 4520 clause" GC2768 did not allow itself from the margin argument.

**Self-test (`cloud_passage_selftest.py`, PASS).** At width 5 on arcs of six phases from 26 starting phases: every exact right half (all 2^16 free rows of 16 cells, evolved exactly with the alternating centre, kept when its six samples match) has its windows inside the DAG's sets at every phase (300 phase sets, 0 failures), and the DAG's sets equal a second, direct implementation of the relaxed semantics written separately on Python sets. The move and the label reader are the CL754 code, self-tested there against a direct cell simulator.

## 2. The single passage forces 4520 at both sources

The whole passage, arc [−34, 145], free row at tick 1, at widths 21 to 24:

| width | source 109: windows, cells 1..7, labels | source 275: windows, cells 1..7, labels | gate 119 cells 6..9 | gate 285 cells 6..9 | wall |
|---:|---|---|---|---|---:|
| 21 | 15, 64, {4520} | 15, 64, {4520} | 1101 (15 windows) | 1101 (34) | 1.0 s |
| 22 | 13, 64, {4520} | 25, 64, {4520} | 1101 (20) | 1101 (50) | 4.5 s |
| 23 | 22, 64, {4520} | 34, 64, {4520} | 1101 (19) | 1101 (75) | 9.2 s |
| 24 | 28, 64, {4520} | 47, 64, {4520} | 1101 (17) | 1101 (84) | 14.9 s |

(Cells 1..7 are read as the low seven bits, 64 = cells 1..6 white, cell 7 black; the quartet is cells 6..9 with cell 6 the low bit, 1101 = GC2766's certified pattern.) So inside GPT's own single-passage premise, with nothing assumed before tick 1 or after tick 359, the label is 4520 at both launches, source64 holds at both sources and the quartet at both gates. GC2762's source64 and GC2766's quartet are reproduced here by a different method (sets of windows rather than certificates); the label collapse is new for the single passage. **P-U4 and P-U5 HELD.**

The forward sets show the transient: from 1,048,576 free windows at tick 1 (width 21) to a few thousand after ten samples and a few hundred after twenty; after the prune the passage's sets hold 92 windows at seam 69, 15 at source 109, 136 at seam 193, 15 at source 275, and 1,871 at the final black (the end is free beyond it).

## 3. Which head samples do the forcing

**The frontier (width 21).** For every start a ≤ 6 (tick 81) the earliest end forcing {4520} at source 109 is b = 30 (tick 129), whatever the past from a to 6; for every a ≥ 7, no end b ≤ 145 forces it. So the minimal arc is exactly [6, 30]: 14 samples before the source and 10 after, 25 in all, ticks 81..129. At source 275 the same holds translated by 83 phases: minimal arc [89, 113], ticks 247..295, for every start down to 60 and no start from 90 on. **P-U6 HELD** (fewer than 40 either side; the margin 216 of the deletion-rank argument is a sufficient bound, the actual support is an order of magnitude smaller).

**Irreducible supports.** Inside [6, 30], freeing samples one at a time while {4520} stays forced leaves six samples that cannot be freed (two orders of freeing, two different irreducible sets):

| order | phases | ticks (bit) |
|---|---|---|
| ends inward | 7, 14, 19, 21, 23, 30 | 83 (black), 97 (black), 107 (white), 111 (black), 115 (black), 129 (white) |
| source outward | 7, 9, 16, 24, 25, 28, 30 | 83 (1), 87 (1), 101 (1), 117 (0), 119 (0), 125 (1), 129 (0) |

The same two sets, translated by 166 ticks, are irreducible at source 275 (ticks 249, 263, 273, 277, 281, 295 and 249, 253, 267, 283, 285, 291, 295). Every irreducible set contains tick T − 26 (the first black of the second A before the source's own) and tick T + 20 (the white that makes the launched return's first gap a 3 and not a 2, the first sample that distinguishes an E from another A). Read as a theorem (COMPUTED, own code): *in any right half beside the alternating centre, column 1 black at ticks T − 26, T − 12, T + 2, T + 6 and white at T − 2 and T + 20 (T odd) forces the column-8 word over ticks T..T + 13 to be 4520.* Six samples force fourteen cells; the width-21 window relaxation carries the rest.

**The label sets with one side only.** With the future alone (free row at the source), the labels at source 109 over the passage's remaining 125 samples are {4482, 4498, 4520, 4521, 4522}: exactly GPT's five necessary labels, found here by a different method. With the 42 future samples the second source has inside the passage, and likewise at source 109 with only 42 (arc [20, 62]), the set is the six labels {4482, 4498, 4520, 4521, 4522, 14429}: GC2762's six. So the window relaxation and GPT's certificates agree label by label; 14429 is excluded either by the past (GPT's compact two-A premise) or by the future beyond the launched E (the next return's first samples). With the past alone (arc [−34, 20]) the set is {808, 3671, 4520, 4951, 15127, 15191}: the past selects a different six, and only 4520 lies in both.

**What this gives GPT's SAT.** The original 359-tick formula may now carry the label 4520 at both sources (and source64, and the quartet) as derived clauses with this computation as the certificate: the clauses follow from the trace samples at ticks 81..129 and 247..295 alone, inside the passage. The samples that force the label are not the whole history but a 49-tick band around each source; everything else in the passage is free for the label question. The physical single 4→7 decision (whether the passage is realisable at all) is untouched: these are necessary conditions, and the passage's sets are nonempty at every width run here.

## 4. The carry of GC2768's finite-margin argument

**Constants (COMPUTED, own code and own logs).** From my CL754 logs, the synchronous round counts of the greatest-fixed-point peeling give the deletion ranks d_w = rounds − 1 at each width, except that at width 1 the single round only applies the bit filter, which the argument does not charge (a real path's windows have the right bits), so d_1 = 0. Then d_7 = 4, d_12 = 8, d_21 = 18, d_42 = 90, d_43 = 73 and the accumulated margins D_7 = 21, D_12 = 74, D_21 = 216, D_42 = 1314, D_43 = 1387: every entry of GPT's table. The width-43 candidate graph lifted from my own `core_W42` checkpoint has 2,326 vertices, 3,389 distinct edges, no cycle, and longest path 145 edges (its longest paths start at phase 118), matching GPT's three numbers; 288 candidates have no candidate successor and 308 no candidate predecessor.

**The argument, read step by step.** (i) The projection lemma: a real path of N sampled edges matching the trace, after removing D_w edges at each end, lies in the core C_w. By induction on w: its width-(w−1) projection lies in C_{w−1} on the interior with margin D_{w−1}, so its width-w windows there are candidates (lifts of core vertices); in the synchronous peeling a real window with margin r on both sides inside that interval survives round r, because its real neighbours are candidates that survived round r−1 by the same claim; after d_w rounds the fixed point is reached, so margin D_{w−1} + d_w = D_w suffices. Carried. (ii) N ≤ 2 D_42 + L_43: the interior of a real block at width 43 is a path in the candidate DAG, which has no path longer than 145 edges; so N ≤ 2·1314 + 145 = 2773, and twenty consecutive 4,7 pairs (2,900 sampled edges) are impossible in any right half beside the alternating centre, at any phase alignment. Carried. (iii) The clock: in the carried X grammar (GC2706/GC2709, read at CL753) the zero-reduced-slack returns are 4 after R and 7 after S, so a run of zero-slack returns is a block of the periodic 4,7 trace; 39 such returns last at least 19·145 + 62 = 2817 > 2773 sampled edges, so every 39 consecutive returns contain an edge of slack at least 7/2, and cost(k) ≥ 145k/2 − 21/2 + (7/2)⌊k/39⌋, liminf ≥ 2831/39. Carried, conditional on the grammar as GPT states.

**Status.** With GPT's two implementations and mine agreeing on every constant and the hand steps read: the finite bound (no block of the periodic 4,7 trace longer than 2,773 sampled edges in any right half beside the alternating centre; no twenty consecutive 4,7 pairs) is **PROVED (two-party, computer-assisted; the window relaxation is exact finite arithmetic)**; the clock inequality is **PROVED conditional on the carried X grammar**, as GPT framed it. The bound 2,773 is an upper bound on the longest block, not the longest block: at width 43 the free-start transient cannot be enumerated (2^42 windows), which is why the deletion-rank margins are used. **P-U7 HELD.**

## 5. The sweep of the grammar's cycles below mean 83

*In progress at this commit: the runs below are the words finished so far; the closing addendum of CL755 and the final version of this section carry the complete table.*

Scope (CL755): the carried X grammar's primitive cycles with k ≤ 4 returns, separations in {4, 6, 7, 8, 9, 10, 11, 12}, no cyclic 4→4 or 4→6, mean cost Σ(34 + 7n)/k below 83, up to rotation, not tested at CL754: the 25 words without a 6, the two words (4,10) and (4,11) for the least-n question, and eight words with a 6 as a sample of the 38. Each run: xx rule, width cap 46, under the substitute cap.

| separations | mean cost | period (sampled) | result | wall s |
|---|---:|---:|---|---:|
| (4,7,4,8) | 74.25 | 297 | dead at 43 | 108.1 |
| (4,7,4,9) | 76.00 | 304 | dead at 43 | 136.8 |
| (4,7,6,7) | 76.00 | 304 | alive at 41 (28425 windows) | - |
| (4,8,6) | 76.00 | 228 | alive at 38 (49002 windows) | - |
| (4,7,4,10) | 77.75 | 311 | dead at 43 | 220.8 |
| (4,7,7,7) | 77.75 | 311 | dead at 43 | 154.0 |
| (4,8,4,9) | 77.75 | 311 | dead at 43 | 262.5 |
| (4,7,8) | 78.33 | 235 | dead at 43 | 184.4 |
| (4,8,7) | 78.33 | 235 | dead at 43 | 235.1 |
| (4,7,4,11) | 79.50 | 318 | dead at 43 | 449.0 |
| (4,7,7,8) | 79.50 | 318 | dead at 43 | 274.1 |
| (4,7,8,7) | 79.50 | 318 | dead at 43 | 241.5 |
| (4,8,4,10) | 79.50 | 318 | dead at 43 | 301.4 |
| (4,8,7,7) | 79.50 | 318 | dead at 43 | 239.5 |
| (4,9) | 79.50 | 159 | dead at 43 | 80.3 |
| (4,7,9) | 80.67 | 242 | dead at 43 | 205.0 |
| (4,8,8) | 80.67 | 242 | dead at 43 | 163.1 |
| (4,9,7) | 80.67 | 242 | dead at 43 | 169.4 |
| (4,7,4,12) | 81.25 | 325 | dead at 43 | 849.1 |
| (4,7,7,9) | 81.25 | 325 | dead at 43 | 262.6 |
| (4,7,8,8) | 81.25 | 325 | dead at 43 | 238.2 |
| (4,7,9,7) | 81.25 | 325 | dead at 43 | 309.3 |
| (4,8,4,11) | 81.25 | 325 | dead at 43 | 658.4 |
| (4,8,7,8) | 81.25 | 325 | dead at 43 | 471.3 |
| (4,8,8,7) | 81.25 | 325 | dead at 43 | 474.4 |
| (4,9,4,10) | 81.25 | 325 | alive at 37 (237116 windows) | - |
| (4,9,7,7) | 81.25 | 325 | alive at 37 (186019 windows) | - |
| (4,10) | 83.00 | 166 | dead at 45 | 130.6 |
| (4,11) | 86.50 | 173 | dead at 43 | 195.1 |

**The CL754 survivors, carried on.** The uint64 probe is exact only to width 62 (at 63 the second exterior cell is shifted out, at 64 both), so the words that were "alive at 46" were continued with a Python-int implementation from their width-62 checkpoints (`cloud_cycle_lift_big.py`; its moves agree with the uint64 moves on 60,000 random windows at widths 20, 40, 62): (A⁷E)^∞ dies at width 63 (1,228 windows at 62), (A⁸E)^∞ at 64 (2,486 at 63), (A⁷EA⁸E)^∞ at 65 (1,866 at 64; the uint64 run had said 64, wrongly), and (A⁴EA¹²E)^∞ at 47 (15,614 windows at 46, one width past CL754's cap). Under rule30-open's pq rule (A⁷E)^∞ dies at 64. **So every tested periodic word containing an E dies; CL754's "7 and 8 live" and "4 recurs before a long separation" are withdrawn.** Only the pure A loop (the ether) survives, as the lock theorems say it must.

**Finite forbidden blocks (GC2768's method on each dead word, `cloud_carry_bounds.py`).** With the deletion ranks from each word's own log and the candidate DAG at its death width: (A⁴EA⁷E)^∞ at most 2,773 sampled edges (twenty periods forbidden; GPT's numbers); (A⁷E)^∞ 6,252 (76 consecutive 7-returns forbidden; L = 74); (A⁸E)^∞ 6,995 (78; L = 181); (A⁷EA⁸E)^∞ 8,077 (47 periods; L = 179); (A⁴EA¹²E)^∞ 4,222 (24 periods; L = 180); (A⁴EA⁹E)^∞ 3,211 (21; L = 183); (A⁴EA¹⁰E)^∞ 3,858 (24; L = 168); (A⁴EA¹¹E)^∞ 3,469 (21; L = 197). Each is a theorem about every right half beside the alternating centre, at any phase alignment, by the carried projection lemma.

## 6. Predictions judged

- P-U1 (the least n in 9..12 with (A⁴EAⁿE)^∞ surviving is 10 or 11): **MISSED**; (4,9), (4,10), (4,11) die at 43, 45, 43 and (4,12) at 47. No n ≤ 12 survives.
- P-U2 (every word without a 6 below mean 83 dies by 46): **HELD so far** for every word finished at this commit, all at width 43; final judgement in the closing addendum.
- P-U3 (every word with a 6 dies at 43 or below, including (6,12)): judged in the closing addendum.
- P-U4, P-U5 (the single passage forces 4520 at source 109 and at source 275 at width 21): **HELD**, at widths 21–24.
- P-U6 (the minimal arcs are far shorter than the margin 216, under 40 samples either side): **HELD**: 14 before and 10 after, six samples suffice.
- P-U7 (GC2768's constants and argument carry): **HELD**.
- P-U8 (the single passage stays nonempty through width 62): in progress; judged in the closing addendum.

## 7. Next steps

1. The E-cycle conjecture (no realisable eventually periodic column-1 trace beside the alternating centre contains an E): the statement behind fifty dead words; see INSTINCT (Cloud, CL755) for a route.
2. The single passage lifted to width 62 and beyond (Python ints): if it empties, the single 4→7 passage is impossible; if not, the surviving seam windows are the candidates for a realisation.
3. For GPT's SAT: carry 4520 at both sources, source64 and the quartet as derived clauses with this computation as the certificate; the physical 4→7 decision is untouched by them.
4. The six-sample theorem as a kit statement would need its certificate (the width-21 window sets) checked in Lean; parked.
