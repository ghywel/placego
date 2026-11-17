# The periodic 4,7 word lifted alone: no right half repeats the sharp cycle for ever — Cloud, CL754, 8 November 2026

*A block on GPT's bridge pull at the owner's word, opened in CL754 with its predictions pushed before the run. GPT's current
object (GC2766) is one physical passage E A⁴ E A⁷ E, studied as a joint predicate on the seam row at tick 193. This block
takes the complementary finite object named in CL753 and in L1569's question 1: the periodic word (A⁴ E A⁷ E)^∞, the sharp
cycle of GPT's clock (GC2706, carried CL753), lifted alone on the window graph, width by width. Own code
(`tests/probes/swarm/sw02/block3/cloud_cycle_lift.py`, self-test `cloud_cycle_lift_selftest.py`, logs as `.out`); no DFA table,
CNF or code of GPT's or Local's used. Status of every number below: **COMPUTED, self-check**, Cloud's host, with the
soundness lemma of §1 PROVED by hand. Evidence: shared store `cited/cloud/cycle-lift/cloud-cycle-lift-20261108.tar.gz`,
SHA256 `dbdab7f43fbc56312225211169390132649eec8c0391237120779c43152d6e85`, 1,091,251 bytes (source, logs, every width's core of
the 4,7 word as a compressed array file, the seam windows at 41 and 42), readback verified.*

**GPT review/update GC2768:** all43 saved4,7 cores now independently replayed
on Intel; empty-core transfer carried. The source64 threshold is corrected
below to7. The clock and finite-survival interpretations are narrowed below;
[finite-margin continuation](GPT-CYCLE-LIFT-REVIEW-20261108.md#outcome--gc2768)
gives a new, still carrying-read-pending20-pair bound and guarded five-pair
label result. Historical predictions remain in CL754's ledger entries.

## 1. The object and why its death is a theorem about right halves

Windows are the Block 3 packet's: columns 1..W at odd ticks, cell i as bit i − 1, the centre column 0 white at odd ticks and
black at even ones. A move is the double step, centre white then black, with columns W + 1 and W + 2 at the odd tick free (the xx
rule; the pq rule, column W + 1 free at each of the two ticks, is a superset of moves and is run as a check). A gap word fixes
the sampled column-1 trace u(s) at the odd ticks: black at s = 0 and after each gap. For a periodic gap word of period P
sampled steps, the phase graph has vertices (s mod P, window) and the moves as edges, and the **core** is the set of vertices
on bi-infinite paths whose column-1 bit equals u(s) at every step: the greatest fixed point of "right column-1 bit, some
successor in the next phase's set, some predecessor in the previous phase's set", computed by lifting from width 1: the
candidates at W + 1 are the core windows at W with either bit in the new column, then the fixed point again. The lift is sound
because a move at W + 1 projects to a move at W.

**Lemma (PROVED, hand).** If the core at width W is empty, no right half, finite or infinite, has a column-1 trace that
is eventually the periodic word. *Proof.* Such a right half gives, from the tick where the periodic trace begins, a
forward-infinite sequence of W-windows, consecutive ones related by an xx move with the actual cells W + 1, W + 2 as the
exterior, and with the right column-1 bits. The phase graph is finite, so some vertex (phase, window) recurs infinitely often;
the stretch between two visits is a closed walk following the periodic trace at its own phases; so the vertex lies on a cycle
and has bi-infinite continuations. It is in the core. ∎ The converse fails: a nonempty core is an abstraction with the
exterior chosen freely at every move, not a realisation.

The move and the label reader were checked against a direct cell-by-cell Rule 30 simulator on 3,000 and 2,000 random cases
(`cloud_cycle_lift_selftest.py`: no mismatch). The trace convention (a gap is the distance between consecutive blacks, so
E = 33535555 is 34 sampled steps and A = 25 is 7) is GPT's and the kit's; its alignment is confirmed below by three
independent certified facts appearing at exactly the predicted phases.

## 2. The 4,7 word: alive through 42, dead at 43

| W | core, total over 145 phases | largest phase | seam phase (tick 193) | rounds |
|---:|---:|---:|---:|---:|
| 24 | 13,968 | 561 | 279 | 30 |
| 30 | 16,929 | 578 | 537 | 66 |
| 35 | 29,542 | 897 | 777 | 41 |
| 37 | 34,136 | 995 | 921 | 63 |
| 38 | 9,731 | 318 | 187 | 92 |
| 39 | 4,597 | 108 | 92 | 75 |
| 40 | 3,268 | 100 | 95 | 50 |
| 41 | 1,965 | 49 | 42 | 52 |
| 42 | 1,163 | 39 | 13 | 91 |
| **43** | **0** | 0 | 0 | 74 |

The core grows by about 1.07 a column from
24 to 37 and then collapses: it loses two thirds at 38, half again at 39, and is empty at 43. By the lemma, **no right half,
finite or infinite, has a column-1 trace that is eventually (A⁴ E A⁷ E)^∞.** The whole run took 43 seconds.

**Consequences for the clock (GC2706, CL753).** The minimum cycle mean145/2 in the X grammar is attained by4,7. Its zero reduced-slack edges, under GC2706's potential,
are exactly R→S at4 and S→R at7; raw cost83 also occurs on R→R at7. Periodic death alone does not exclude sparse defects
whose mean approaches145/2. GC2768 supplies the missing uniform finite-repetition bound, leading to the stronger conditional
liminf bound2831/39; that new hand refinement awaits a carrying read. The physical infimum remains open; finite-width
periodic candidates are listed in §4.

**Consequences for GPT's one passage.** None directly: one passage E A⁴ E A⁷ E is a weaker demand than repeating it, and
the DFA factor E A⁴ E A⁷ E is present at 38 to 41 (CL753). What this block supplies to the joint pullback is the full list of
seam-row prefixes consistent with the periodic context: 42 windows of 41 cells and 13 of 42 cells at the seam phase, in the
evidence packet, and the fact that at 43 cells none survives.

## 3. GPT's certified finite facts, read off the live windows

Three facts GPT proved with native SAT certificates on finite cones appear on the periodic word's live windows at the
phases where they must, by a method that shares nothing with those certificates:

| Fact (GPT) | Where it should show | What the lift shows | From width |
|---|---|---|---|
| source64: a source row 16 ticks before an E launch has cells 1..7 = 0000001 (GC2719, GC2762) | the two source phases, ticks 109 and 275 of the passage | every live window has low 7 cells = 64 | 7 |
| the quartet: row 119 (and 285) cells 6..9 = 1101 (GC2766, 57-tick cone, forced for any window path from width 58) | the two gate phases | every live window has cells 6, 7, 8, 9 = 1, 1, 0, 1 | 12, far below 58 |
| the six and then five launch labels: the 14-bit column-8 word at the source is one of 4482, 4498, 4520, 4521, 4522 (14429 excluded by the compact two-A premise) (GC2724, GC2762) | the two source phases, readable from 21 cells | **one label only, 4520**, at both launches, the one after A⁴ and the one after A⁷ | 21 |

The third line is the new fact: on the periodic history the launch label is not merely one of five, it is forced to 4520 at
both kinds of launch, from width 21 on and therefore at every larger width while the core lives (the label is a function of
the first 21 cells, and live sets project into live sets). 4520 is one of the three whole-E labels GPT found sharing the
eight-bit gate interface (GC2765). P-S2 held and was sharper than written; P-S3 held with W* = 12.

## 4. Controls and the other short cycles

The same code on other periodic words, each run to death or to its budget (results from the batch logs; the pq rule is a
superset of xx moves, so a pq death implies the xx death):

| Word | separations n | period (sampled steps) | mean cost per excursion | moves | verdict |
|---|---|---:|---:|---|---|
| (A4EA7E)^∞ | 4,7 | 145 | 72.50 | xx | **dead at 43** |
| (A4EA7E)^∞ | 4,7 | 145 | 72.50 | pq | **dead at 43** |
| (A4EA7EA6E)^∞ | 4,7,6 | 221 | 73.67 | xx | **dead at 43** |
| (A4EA7EA6EA6E)^∞ | 4,7,6,6 | 297 | 74.25 | xx | **dead at 43** |
| (A6E)^∞ | 6 | 76 | 76.00 | xx | **dead at 43** |
| (A6E)^∞ | 6 | 76 | 76.00 | pq | **dead at 43** |
| (A4EA8E)^∞ | 4,8 | 152 | 76.00 | xx | **dead at 43** |
| (A4EA7EA7E)^∞ | 4,7,7 | 228 | 76.00 | xx | **dead at 43** |
| (A6EA7E)^∞ | 6,7 | 159 | 79.50 | xx | **dead at 43** |
| (A7E)^∞ | 7 | 83 | 83.00 | xx | alive at 46: 70,088 windows (width cap) |
| (A8E)^∞ | 8 | 90 | 90.00 | xx | alive at 46: 68,359 windows (width cap) |
| (A4EA12E)^∞ | 4,12 | 180 | 90.00 | xx | alive at 46: 15,614 windows (width cap) |
| (A6EA10E)^∞ | 6,10 | 180 | 90.00 | xx | **dead at 43** |
| (A7EA8E)^∞ | 7,8 | 173 | 86.50 | xx | alive at 46: 147,239 windows (width cap) |
| (A4E)^∞ | 4 | 62 | 62.00 | xx | **dead at 38** |
| (A4EA6E)^∞ | 4,6 | 138 | 69.00 | xx | **dead at 39** |
| (A5E)^∞ | 5 | 69 | 69.00 | xx | **dead at 37** |
| (A1)^∞ | no E (the pure A loop) | 7 | — | xx | alive at 38: 5,480,962 windows (budget) |

**The pattern, and the bounded prediction it refutes.** Addendum 1 of CL754 guessed from the first eleven words that neither 4 nor 6 can recur
in a periodic context. The three test words settle the death-by43 predictions, not physical nonrecurrence: (A⁶EA¹⁰E)^∞ dies at 43 (P-S7 HELD), (A⁷EA⁸E)^∞ lives at 46 (P-S8 HELD), but
(A⁴EA¹²E)^∞ lives at 46 (P-S6 MISSED). So every tested word containing a 6 dies, while a word with4 survives the finite-width test with a longer following separation: 4,7 and 4,8 die, 4,12 lives, and the least surviving n between 9 and 12 is the first question of the next sweep. The
death is not a function of the mean cost: (6,10) and (4,12) both cost 90 a excursion and one dies, one lives.

The three negative controls land exactly on GPT's DFA findings: (A⁴E)^∞ dies at 38, where GC2698 found E A⁴ E A⁴ E forbidden
at every width 38 to 41; (A⁴EA⁶E)^∞ dies at 39, where GC2698's counterword E A⁴ E A⁶ E is present at 38 and absent from 39;
(A⁵E)^∞ dies at 37, since 5 is never an allowed separation. The pure A loop, which includes the known period-7 lock, remains live through38
(5480962 windows at the budget stop). So the method kills what the record says must die and
keeps what must live, and it reproduces GC2698's two thresholds to the exact width.

## 5. Scoped carry of GC2766's three requests to Local

GPT asked Local to carry three hand items; the owner put this block in Local's place, and they are short.

1. **The quartet's mechanism, phase and lookahead.** Under any of the five labels the seven-cell trunk from 64 gives row 119
   cells 6, 7, 8 = 1, 1, 0; column 8 at tick 120 is white, and the rule there reads 0 = b ⊕ (c ∨ d) with b = 1, c = 0, so
   d = cell 9 = 1; and b ≠ c puts the known two-tick identity in its copy branch, Q = column 8 at 121 = a = 1 independently
   of cell 10. The certificate's premise 25253353 is two A blocks and the first four gaps of E in a 57-tick cone whose last
   premise sample lies 34 ticks after the asserted row: a compatibility implication, not a forward law. PROVED hand/two-party;
   and the lift shows the quartet on every live window from width 12 (§3), with the free exterior, which is a second,
   independent confirmation on the periodic object.
2. **The same-row observer indices.** An event at (tick t, cell p) is read by the inverse scan of the tick-193 row at
   j = 193 − t + p: the label bits (ticks 109..122, column 8) at 92..79; the source prefix (tick 109, cells 1..7) at 85..91;
   the gate (tick 119, cells 6..9) at 80..83; the older pulse (111, 1) at 83; Q (121, 8) at 80. The pending pairs are two per
   live row: rows 91..192 give 204 before cell 102, 158 after reading 102..80 (23 cells), 156 after 79. PROVED hand/two-party
   as index bookkeeping; it is the convention L1592 already carried for GC2741.
3. **The 103-cell support.** The 21-cell source prefix at tick 275 depends on the seam row's cells 1..103 (21 + 82); the 14
   label bits at 275..288 on cells 1..103 as well (8 + 95); so the pullback of the five 21-cell fibres is a predicate on
   M₁..₁₀₃, while the past observer is fed by cells 103..79 and the high-tail-derived state before 103 (206 pending bits for
   rows 90..192). 103 cells are label support only; the complete future A⁷E still needs 167 (CL753 §4). PROVED hand/two-party.

## 6. Predictions judged, and what is not claimed

- **P-S1 (0.6):** HELD through 41; the core is empty at 43. The counterfactual's content, a finite death, occurred two columns
  beyond the DFAs' reach.
- **P-S2 (0.6):** HELD and sharper: source64 at every live source window from width 7, and one label, 4520, from width 21.
- **P-S3 (0.75):** HELD, W* = 12 against the certificate's 58.
- **P-S4 (0.5):** MISSED in the interesting direction: the lift never needed width 60; the word died at 43 in 43 seconds.
- **P-S5 (0.6):** HELD where it applies: growth was about 1.07 a column from 24 to 37, well under 1.5; the collapse after 37 is the finding, not a growth rate.

Not claimed: anything about one passage (GPT's question); any minimum of the mean return cost; realisability of the
survivors in §4 (a nonempty core is an abstraction); independence of the three finite-cone facts from the trace conventions
(their appearance at the predicted phases is the check of those conventions, and vice versa). All numbers are one host's
Python; a second implementation or host has not replayed them. The pq runs are a check by a superset of moves, not an
independent implementation.

## 7. Next steps this leaves

- **The infimum of the clock.** The periodic candidates between 72.5 and 83 and their deaths or survivals (§4) suggest a
  finite question: which periodic words of the X grammar have a nonempty core at the widths the lift reaches, and does any
  with mean below the cheapest survivor's exist? The lift costs seconds per word; a systematic sweep of cycles by increasing
  mean is one block.
- **Consecutive repetitions.** At width 43 the longest path following the 4,7 trace is finite; its length bounds how many
  consecutive 4,7 pairs any realisable history can contain, which supplies the missing uniformity for a quantitative
  clock improvement. GC2768 obtains a conservative bound in Python from the saved cores, retaining all earlier-width transient margins. A longest path in the last lifted candidate graph alone is insufficient for arbitrary finite histories.
- **For GPT's joint pullback.** The 13 seam prefixes at width 42 are the only M₁..₄₂ consistent with the periodic past and
  future; their 14-bit future labels (readable from cell 103 on, so not at 42) and their inverse-scan words are the concrete
  joint data the periodic case offers, in the evidence packet.
