# The structure atlas: what the ordered structures of Rule 30 have in common, what is visibly missing, and three candidate unifying theories

*Cloud, 2 November 2026, CL677, at the owner's question: "can we begin to piece together the structures we know about,
to either indicate structures we don't yet know about but are visibly missing in the gaps, or some unifying theory that
connects the structures to each other, rather than being isolated interesting cases." A synthesis, not a result: every
row cites where its status lives. It continues DQ-022 (the run rule and the universal ruler, L1000–L1002), the
29 October synthesis of the portal ([SYNTHESIS-20261029](wolfram-agents/SYNTHESIS-20261029.md)) and today's eternal-cycle
reading ([genealogy §38](rule30-genealogy.md#38-clouds-reading-of-the-eternal-cycle-line-a-bridge-to-the-episode-line-and-what-a-proof-needs-cl676)).
Convention: x′(i) = x(i−1) XOR (x(i) OR x(i+1)); the single seed at 0; "frame v" means coordinates moving at v cells
per step. One cheap check (Block 18, §5) was run with its predictions written first.*

## 1. One rule, two primitives, and the sentence everything else hangs on

Rule 30 is one lossless copy and one lossy mask: the left neighbour is copied (XOR, invertible, speed +1), and the
cell's own OR with its right neighbour is added to it. Every ordered structure in the record is a place where the mask
is *determined*: where the OR is forced to be 1 (a black cell beside anything, or a white pair's ends) or forced to be
0 (inside a white run), the rule is affine and the pattern is periodic or straight; where the OR's value is itself news
from the right, the pattern is the core. Local's run rule (DQ-022, Theorem R) is this sentence read on runs; the
agreement rule (Theorem P), the damage-front identity (8.66), the band bottom rule of the episode certificates (CL669),
the front lemma D_{R+2}(t+1) = NOT E_{R+1}(t) and the masking envelope (CL674, PROVED two-party, L1278) are the same
sentence read on differences: **a difference passes a cell exactly where the cell's nearer input is white.** That one
lemma, in four frames, is the first unification the record already holds, and it is proved in each.

## 2. The map: three frames, four kinds of object

The grid is frames (rows) against object types (columns). Each cell names the structure, its status and where it is.
A cell marked **gap** is empty or thin in the record although the symmetry of the grid says something should be there.

| frame | the map | its periodic points | its fronts and speeds | its counts and densities |
|---|---|---|---|---|
| **v = +1, the right edge** (the copy's own frame: everything arrives here) | the 2-adic edge map Φ: triangular, invertible, generator a of automaton 2369 (L1294, known); +2 bit length per step (atlas; L1290 reproved); column periods double, e_j ≤ ⌈j/2⌉ + 3 to j < 2^22 (kit `per_upper_half_explicit`) | the eternal cycles: PROVED power-of-two periods (L1291); rain the only one for p ∣ 128 (COMPUTED, three implementations); the phases of the two-sided map are rigid rotators c^g = ρ^r (L1308, PROOF); G8, G16, 480, P1024 known; **conjecture** (light-speed recurrence) open | the mismatch fronts of inserted edges: G8's law PROVED (Lean, PR #71); the envelope upper bound on every front PROVED; witness fronts for (7,28), (7,63), (9,57), (12,68) COMPUTED, and (12,68)'s law broken at t = 1590 by the odometer wake (CL674) | the doubling density of the diagonals: at most 1/2 in the limit (kit); measured 0.41–0.43 (DQ-024; CL642's 3/7 if the unforced parities were fair); the critical two-type branching with constant 0.80 = √(2/π) (L1297/L1298); the universal ruler (Theorem U, L1001) |
| **v = −1, the left edge** (the mask's frame: nothing from the core ever arrives, since news moves left at 0.246 < 1) | the left wheel map L_j′ = L_{j−2} XOR (L_{j−1} OR L_j): the copy comes from the edge side, the cell's own state is masked, hence amnesia (CL649 era); **gap**: its algebraic identity (is it in the automaton atlas? what are its orbit closures?) | the universal left side: one periodic strip below the first branch at 53,208 and a tree above it; doublings at 2, 7, 28, 399, 87,866; period 32 at a million (8.30, 8.31, 8.59, 8.60); Lemma B2 (doublings never stop, PROVED); the certified band of period 16 that makes 30 special among 64 rules (8.64); staircases end in clocks (DQ-021) | the settling front at slope ≈ 2.006 on every side (row 11; potentials certify it through small periods); the order/disorder boundary x = −0.25 t, a random walk about that line with the band edge advancing 0.755 diagonals per step (8.74); the crystal recedes from the column at 0.21–0.25 (DQ-025) | **gap**: the law of the doubling depths 2, 7, 28, 399, 87,866 (the left side's "ruler"); the left-side budget (how many free bits the strip carries per diagonal) |
| **v = 0, the centre and the walls** (where the prize lives) | the sideways rule: columns 0 and 1 determine the whole left half (8.36, Condrey's triangular uniqueness; G22's two-track CA); the four-state inverse reader (G13); Rule 30 = Rule 210 as its own time derivative (8.70, PROVED) | clock walls: period 1 excluded for every finite seed (Condrey, reproved 8.76); period 2 open, with Theorems A, A′, A⁗, E, E″, F and `no_finite_clock` excluding classes (PERIOD-TWO.md); the wheel 17/56 next to 0101 (8.4–8.11); finite rows keep a period-2 column for about w + 3 steps (CL656/CL657, COMPUTED) | the kicks and their arrival phases (8.43, 8.44); the channel: at most 0.1236 bits per visible bit beside the wall (8.20, 8.33, certified at width 28) and 0.0618 bits per step for left halves; the excess ≤ 6–8 steps after the row's news arrives (CL665) | the gate classes: affine gates logarithmic, choked gates, six odometer-like at 0.386–0.412 (CL661/CL662); balance in the ordered band without randomness (row 8); **gap**: a proved relation between any two of the budgets (edge doubling ≤ 1/2, the wall's free bits, the channel's 0.12, the branching's mean 1) |
| **v = −0.246, the news frame** (the frame in which the order/disorder boundary stands still) | **gap**: nobody has written the dynamics in this frame | **gap**: what is stationary there (the band edge's step law 0, 1, 2 diagonals, max 14, 8.74) | the leftward speed itself: 0.246 on a random background (8.30), 0.2437 on the single seed's boundary (8.74), Grassberger's 0.243; the identity v = 1 − P(heal)·E[jump ∣ heal] (8.66, PROVED as an identity); the first-order cone 0.40 against the true 0.25 (L1282); T27's influence crossing at 1.24–1.27 L (L1305) | **gap**: a closed form for 0.246, and the stationary statistics of the core seen from this frame |
| **rings and intermediate v** | the ring map on Z/n: complete to n = 24 (8.67); every cycle on a prime ring is a glider; turning rows (8.71) | periodic points of frame v ∈ [−1, 1) are spatially periodic (kit `PeriodicPoints`); so every space-time periodic pattern is a ring glider, and the velocity-1 ones are the rotators: **a complete classification is one theorem away** (the light-speed recurrence conjecture) | the witness fronts in the lab frame: G8's 3/2 is lab speed 1/2; (12,68)'s 1.235 is lab 0.235; the classic ether's slope 1 is lab 0; G16's 1.1 is lab 0.1 (CL672–CL676): **a velocity spectrum of backgrounds, with no law** | the triangle census: the core's triangles have the uniform measure's density 3·2^(−(L+4)) to three decimals (8.68) |

Third-party structures sit in the same cells: Condrey's period-1 theorem and his budget and mortality (PR75/76) at
v = 0; Lowry's PR69 ether and frozen ruler, AIOvernight's half-rate bound and Rowland's caps at v = +1; Quint's cascade
and left anti-periodicity at v = −1; the recent PRs on left inverses, idempotent period preservation and canonical
windows at v = 0 and −1 (MAP §23 onward). None of them occupies the gap cells.

## 3. The bridges already proved, read as one picture

1. **The mask lemma** (§1): one statement, proved in four frames.
2. **The odometer is everywhere.** The black front of the centre cell's family tree is a copy of the right edge
   (L1283's deep-side odometer law); every light-speed black front with white ahead runs Φ behind it; the triangles'
   right sides are local rulers; the universal ruler says every finite seed's edge is the single seed's, truncated.
   So the v = +1 column of the grid is not an edge phenomenon but the local law behind every light-speed black front
   in the picture, and the triangle census (uniform measure) is its statistical face.
3. **The episode bridge** (CL676): "no eternal point ends in the phase E" is "every episode on E ends"; the kit's G8
   theorem is a uniform wall exclusion. The eternal-cycle line (v = +1 periodic points) and the background line
   (v = +1 fronts) are one object.
4. **Rule 30 is a Gray step plus a correction** (8.70, PRIZE-PROBLEMS §7): the same linear skeleton as Collatz's
   3x+1 (Gray step plus carries) and Mahler's 3/2; Φ ≡ 3x + 3 mod 4 along the seed's edge (L1290). The Collatz shape
   of the defect tree (critical branching, no rank) is the same shape as Collatz's own difficulty.
5. **The centre column as a parity along its past diagonal** (hand, elementary; §5): x_0(t) is the XOR of the
   OR-events along the light-speed diagonal from the cone's left edge at time t/2 to the centre at time t. The path
   crosses, in order, white (nothing), the settled crystal (periodic strips, period ≤ 32 to depth 87,866), the
   settling zone, and the core. With 8.74's boundary and row 11's settling slope, those are the quarters
   t/2..2t/3, 2t/3..0.8t and 0.8t..t. This is the record's wall-and-kicks picture (8.5, 8.9) restated for the centre:
   the settled part is exactly periodic in the sample index, and the whole question of Problem 1 is whether the last
   fifth of the path can keep the parity from repeating.

## 4. What is visibly missing: the structures the grid predicts

Each is named with the cheapest test and what it would teach, in the order I would run them.

- **M1, the left edge as an algebraic object.** Φ has an atlas entry, a 2-adic form and a periodic-point theory; the
  left wheel map has none of these in the record. Its mirror questions are: which automaton it is; what its periodic
  points are (the band is one); why the doubling depths are 2, 7, 28, 399, 87,866 (a law like the ruler's would be
  the left side's "universal ruler"). Test: the shift-register and SAT censuses of §35–36, mirrored. Teaches: whether
  the two edges are one algebra read from two ends or two algebras.
- **M2, the velocity spectrum law.** The lab speeds of the mismatch fronts (0, 0.1, 0.235, 0.5 for the four
  backgrounds; 0.246 for the uniform background) all come from the healing identity v = 1 − P(heal)·E[jump]. Test: evaluate
  the identity's two factors on each background exactly (the wake is periodic for G8, odometer for (12,68)) and see
  whether the speeds are reproduced; then the closed form for the uniform value. Teaches: whether 0.246 is a property of
  the rule (a formula) or of the measure (a number).
- **M3, the budget dictionary.** Four "half a bit" statements live in four frames and nobody has proved two of them equal
  or unequal: the right edge's doubling density (≤ 1/2, measured 0.41–0.43), the wall's free bits (kit
  `free_bits_no00_no11111`), the channel (0.1236 per visible bit, 0.0618 per step), the critical branching (mean 1).
  G7 applies: these have different definitions. Test: write each as a rate per step of the same clock, on the same
  object (the single seed), and compare. Teaches: whether "the edge's memory and the wall's free bits are the same
  count in two frames" (DQ-024's hope) is true or a coincidence of magnitudes.
- **M4, the news frame.** The frame moving at −0.246 is the only one in which the boundary of order stands still; its
  stationary statistics (the step law of the band edge, the width of the settling zone) have never been written as a
  dynamics. Test: the renewal statistics of B(t) from 8.74's data, and the same for a random background. Teaches:
  whether the boundary is a renewal process with a finite-state description, which would make the settling zone a
  finite object.
- **M5, the parity principle.** Every exactly fair coin in the record is the parity of a long word: the type-0 coin
  of the defect tree (fair to 0.002), the doubling bit of a diagonal (the weight parity of the diagonal two back,
  CL642), and Problem 2's own density is a parity along a diagonal (§3.5). Parities of long weakly dependent words
  are fair whatever the local bias (the OR of two fair bits is black 3/4 of the time, yet its column parity is fair),
  and the measured deviations (0.41–0.43 against 1/2 at the edge) are then exactly the constraints. Test: for each
  coin in the record, say whether it is a parity and whether it deviates; the doubling bit's exact law after the letters
  101 (CL642's open hand question) is the first. Teaches: which fair-coin observations are theorems-in-waiting and
  which encode structure.
- **M6, the complete classification of space-time periodic patterns.** The kit's `PeriodicPoints` plus Local's rotator
  lemma plus the light-speed recurrence conjecture would classify every exactly recurring configuration. The missing
  piece is the conjecture; its cheapest content is the two episode tests (480-phase and P1024) and the phase census by
  register enumeration (CL676).

## 5. Block 18: the diagonal parity and its four segments (the one check run for this note)

Predictions written first (Cloud's scratch, Block 18): P-G1 the band samples at e ≤ t/3 are a function of (e, s mod 32)
in at least 99% of pairs; P-G2 the OR-event density is about 3/4 in the core segment and different in the crystal.
The first run used the wrong cell (one to the left) and the parity identity failed half the time; the slip is in the
scratch file and the corrected path is OR(x_{s−t+1}(s), x_{s−t+2}(s)) with sampled diagonal e = 2s − t + 1.

Result (COMPUTED, single seed to t = 8,192, `diagonal_segments.py`): the parity identity holds at every t from 64 to 8,192
(8,129 of 8,129). **P-G1 HELD outright**: 1,864,334 band samples at e ≤ t/3 fall into 86,368 keys (e, s mod 32) with no key
taking two values, so the settled part of the path is exactly a function of the diagonal and the sample time modulo 32.
**P-G2 half REFUTED**: the OR-event density is about 3/4 in every segment, 0.74–0.75 in the settled crystal, 0.72–0.77 in the
settling zone and 0.74–0.77 in the core (t = 1,024 to 8,192), the uniform value 3/4 everywhere; the crystal is balanced for this
observable although it is periodic (row 8's balance without randomness, seen again). So the segments differ in *determinism*,
not in density: the first is exactly periodic in the sample index, the last is not known to be anything.

## 6. Three candidate unifying theories, ranked, each with a kill test

**T1, the mask theorem with a uniform core (my first choice).** All ordered structure is the determined-mask locus;
the core is statistically the uniform measure for every local observable; every constant in the record that is not a
rational of the rule is a functional of that measure. Evidence: the triangle census to three decimals; the fair type-0
coin; the GW constant √(2/π); the boundary speed on the single seed equal to the random-background speed. What it
unifies: the speeds (M2), the densities, the critical branching. What it costs: proving any uniform-measure statement
for the single seed is at least Problem 2. Kill test: a local observable of the core whose single-seed value differs
from the uniform measure's beyond its sampling error (the doubling density 0.41–0.43 is the candidate: it is a
constrained parity, so T1 predicts the constraint explains the gap from 1/2, and CL642's 3/7 is the first estimate).

**T2, one 2-adic algebra at both ends.** Φ and the left wheel map are the same triangular algebra read from the two
ends of the copy; the right end keeps everything (odometer, periods 2^(j/2)), the left end keeps only what the mask
lets through (crystal, doublings at 2, 7, 28, 399, …); the walls at v = 0 are the periodic points of the intermediate
frames, which the kit already forces to be spatially periodic. Kill test: M1. If the left wheel map's periodic points
and doubling law have no 2-adic description, T2 is wrong as stated.

**T3, the parity principle.** The rule's hardness and its fairness are the same fact: the observables the prize asks
about are parities of long words along light-speed diagonals, parities are fair unless constrained, and the only
structure is in the constraints. Kill test: M5. If some exactly fair coin in the record is not a parity, or some
parity is measurably unfair with no constraint found, T3 is wrong.

The three are not exclusive: T1 is about measure, T2 about algebra, T3 about the observables; a complete theory
would say how the algebra (T2) produces the measure (T1) that the observables (T3) see. That sentence is, I think,
the honest statement of what a unifying theory of Rule 30 would have to be, and the record has pieces of all three
with no bridge between T2 and T1.

## 7. What this suggests for the programme

Run M2 and M5 first: both are cheap, both decide between the theories, and both reuse code in hand (the healing
identity's factors from `rule30_damage_speed.py` and CL674's envelope; the coin list from the record). Then M1, which
is a day of Local's kind of work. M3 is bookkeeping with a guard. M4 and M6 are the long ones. None of this is prize
work; all of it is the structure the owner asked for, and each test has a prediction, a counterfactual and a kill.
