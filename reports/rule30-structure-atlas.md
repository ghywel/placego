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

*(Run on 2 November at the owner's word; results in §8.)* Run M2 and M5 first: both are cheap, both decide between the theories, and both reuse code in hand (the healing
identity's factors from `rule30_damage_speed.py` and CL674's envelope; the coin list from the record). Then M1, which
is a day of Local's kind of work. M3 is bookkeeping with a guard. M4 and M6 are the long ones. None of this is prize
work; all of it is the structure the owner asked for, and each test has a prediction, a counterfactual and a kill.

## 8. First results of M2 and M5 (Blocks 19 and 20, run at the owner's word, 2 November 2026)

### 8.1 M2, the speed law (`speed_law.py`, lab frame, T = 6,000, five alignments per background)

Predictions written first (Block 19), then corrected twice before the run that counts: the first prediction conflated the
*current* damage front (8.66's object, which recedes when the deep wake heals) with the *first-arrival* front (the episode
theorem's object; guard G9), and the first two runs forced the array's end cells white, a defect whose damage travels right at
light speed and corrupted the backgrounds behind the wake (now guard G27). The G8 control, whose law is PROVED, exposed both.
The run below has a left margin of 2T + 100, T = 6,000, speeds over [T/2, T], five alignments; v is the lab leftward speed
of the leftmost mismatch; P(heal) and E[jump | heal] are the factors of the healing identity on the diagonal index.

| background | torus density ρ | 1 − 2ρ | v (current) | v (first arrival) | P(heal) | E[jump∣heal] | jumps seen | note |
|---|---|---|---|---|---|---|---|---|
| G8 (PR69's ether) | 0.500 | 0.000 | **0.5000** every alignment | 0.5000 | 1/4 | 2 | 2 only | the PROVED law, 3/2 in the frame; no retreat |
| classic ether (7, 28) | 0.464 | +0.071 | **0.0000** every alignment | 0.0000 | 3/8 | 8/3 | 2, 4 | an exact periodic law: the wake's left edge is pinned in the lab |
| (7, 63) | 0.524 | −0.048 | 0.136 (×4), 0.222 (×1) | same | 0.39 | 2.16 | 1–4 | alignment classes |
| (9, 57) | 0.509 | −0.018 | **0.2632** every alignment | 0.2632 | 7/19 | 2 | 2 only | an exact periodic law: 5/19 (period 19, CL672) |
| (12, 68) | 0.503 | −0.005 | 0.174 (0.16–0.19) | 0.174 | 0.40 | 2.07 | 1–5 | odometer wake, no law (CL674) |
| G16 | 0.508 | −0.016 | 0.224 (0.222–0.225) | 0.223 | 0.40 | 1.94 | 1–5 | odometer wake |
| uniform, inserted edge | 0.5 | 0.000 | 0.246 ± 0.008 | 0.246 | 0.409 | 1.84 | 1–5 | 8.30's 0.246, 8.74's 0.2437, Grassberger's 0.243 |
| uniform, single flip | 0.5 | 0.000 | 0.252 ± 0.005 | 0.251 | 0.403 | 1.86 | 1–5 | the same within error |

P-H1 HELD for the uniform background (edge and flip agree within error and with the record), for G8 (exactly 1/2), the
classic ether (exactly 0), (7, 63), (9, 57) and (12, 68); **REFUTED for G16** (0.224, predicted 0.03–0.17 from the
episode slope: M(k) is the *slowest* prefix's first arrival, and the inserted edge's own front is faster; the same
lesson as for the classic ether's slope, where the inserted edge happens to be the slowest). **P-H2's G8 clause
REFUTED and its failure clause HELD**: the mean-field law 1 − 2ρ is wrong everywhere (G8's torus density is 1/2, not
the 1/4 of its initial row; its front sees white ahead exactly a quarter of the time because it advances into white
cells), and P(heal) is never the density: 1/4, 3/8, 7/19, 0.40 against densities 0.46–0.52. **P-H3 HELD**: five
backgrounds with density within 0.02 of one half have speeds 0.17, 0.22, 0.25, 0.26 and 0.50.

What M2 teaches, in order of weight:
1. **The velocity spectrum is real and includes zero.** The leftward news speed of an inserted edge is a property of the
   pair (background, perturbation), not of the background's density: 0 on the classic ether, 5/19 on (9, 57), 1/2 on
   G8, about 0.17–0.25 on the odometer-wake backgrounds, 0.246–0.252 on a fair row. The classic ether's zero is the
   sharpest: a black edge inserted into the (7, 28) ether disturbs it only in a region whose left end never moves in
   the lab (P(heal) = 3/8 with jumps 2 and 4, exactly cancelling the light-speed drift). This is CL672's slope-1 episode
   law read in the lab, and it says the (7, 28) ether is rigid against the edge the way no other background tested is.
2. **Where the wake is periodic the speed is a rational with an exact law** (G8, the classic ether, (9, 57)); where the
   wake is the odometer the speed is a long-run average with no law (G16, (12, 68); CL674). So the speed law splits by
   the wake's type, and the type is decided by whether the front's retreats read the odometer, exactly the dichotomy of
   CL674 and §38 of the genealogy report.
3. **The healing identity's factors on a fair row are 0.405 and 1.85**, both stationary statistics of the news frame
   (M4): the front finds white ahead 40% of the time, not 50%, because it advanced into white; and heals in jumps of 1
   (38%), 2 (54%), 3 and more (8%). A closed form for 0.246 is a closed form for these two numbers, which is a
   renewal computation on the front's own Markov structure, not on the background. That is M4's object, now named.
4. **T1's first test is passed in the weak sense and failed in the strong sense**: the single seed's boundary speed
   equals the uniform value (8.74), so the core is uniform-like for this observable; but no low-order statistic of a
   background predicts its speed, so "a functional of the measure" means a functional of the front's stationary law,
   which is a different and harder object. T2 gains a datum: the backgrounds with exact laws have periodic wakes and
   those without have the odometer, i.e. the 2-adic algebra decides the class.

### 8.2 M5, the parity census (`parity_census.py`, single seed to t = 32,768)

Predictions written first (Block 20): P-I1 the centre column is coin-like (control); P-I2 the crystal parity P_c(t), the XOR
of the OR-events along the past diagonal over the settled samples e ≤ t/3, has density in [0.45, 0.55] but is *not* coin-like
(some run length deviates by more than 20% or some autocorrelation exceeds 0.05; lean 65%); P-I3 the news parity
x_0 ⊕ P_c is coin-like; P-I4 the core parity alone is coin-like.

Result (COMPUTED, 32,641 samples per column; one standard error 0.0028 on a density):

| column | density | largest autocorrelation, lags 1..8 | run law against 2^(−l), l ≤ 7 | longest run |
|---|---|---|---|---|
| the centre column x_0 | 0.4987 | 0.011 | within 4% | 15 |
| the crystal parity P_c (settled samples) | 0.5010 | 0.010 | within 6% | 15 |
| the news parity x_0 ⊕ P_c | 0.4989 | 0.006 | within 2% | 14 |
| the core parity alone (s ≥ 0.8 t) | 0.4991 | 0.007 | within 3% | 15 |
| the settling-zone parity alone | 0.4970 | 0.013 | within 6% | 13 |

P-I1, P-I3 and P-I4 HELD. **P-I2's second clause REFUTED**: the parity of the settled crystal, a sum of samples of
periodic strips of period at most 32, is indistinguishable from a fair coin by density, autocorrelation and run law.
That is the parity principle in its sharpest form: a parity over a growing set of periodic terms is coin-like although
every term is periodic (each term is a periodic function of t of period at most 64; the set of terms grows by about 21
every 64 steps, and that growth is what randomises the sum). Two consequences. First, "coin-like" tests cannot tell
deterministic order from the core: the crystal passes them. Second, the centre column's fairness (Problem 2's
measurements) is exactly what the parity principle predicts whatever the core does, so a proof of Problem 2 along this
line would have to show the *constraints* vanish, not that the core is random.

The census of the record's coins, with this result:

| coin | a parity of a long word? | measured | deviation from 1/2 | the constraint, if named |
|---|---|---|---|---|
| the centre column (Problem 2) | yes (OR-events along the past diagonal) | 0.4987 here; 8.34, 8.35 | none seen | none known |
| the crystal parity | yes | 0.5010 | none | none (the periodic terms are the structure, and the parity hides it) |
| the news and core parities | yes | 0.4989, 0.4991 | none | none |
| the type-0 coin of the defect tree, \|v ∨ w\| mod 2 (L1298) | yes | 0.4988–0.4991 | none | none (criticality follows) |
| the doubling bit of the right diagonals (DQ-024, CL642) | yes (weight parities of diagonals) | 0.41–0.43 | yes, 0.07–0.09 | `no_three` and the 101 shift law: two forced zeros; CL642's 3/7 is the first estimate and the exact law after 101 is open |
| `half_black` (kit) | not a coin: exact 1/2 on every newly doubling diagonal | exactly 1/2 | none | anti-periodicity: balance from order |
| the OR-event density per segment (Block 18) | no (a density) | 0.74–0.77 | from 3/4: none | a uniform-measure value in the crystal too |
| the run lengths at the ancestry front (L1288) | no (a distribution) | within 1.41 of 2^(1−l) | small | none |

So every coin in the record that is a parity is fair except the doubling bit, and the doubling bit is the one with a
named constraint. T3's prediction survives its first test, and M5's next step is CL642's open hand question: the exact
law of the doubling bit after the letters 101, which is where the constraint lives.

## 9. The banding investigations: M4 and M1 (Blocks 21 and 22, at the owner's word, 2 November 2026)

### 9.1 M4, the news frame as a renewal process (`band_edge.py`, `front_markov.py`)

Predictions written first (Block 21): P-K1 the single seed's band edge B(t) (8.74's exact curve, computed on the autonomous
left-frame system to t = 2^16 with lag 2^10) has the same step distribution as the fair-row damage front's jumps of the
diagonal index (Block 19) within 0.03 per bin (lean 55%); P-K2 the mask lemma as a control (the front advances iff the cell
ahead is white); P-K3 the jumps are nearly independent (lean 55%); P-K4 the bias "white ahead 59.5% of the time" comes from
the heals, not the advances (lean 60%).

Result (COMPUTED):

| step or jump | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | mean | P(move ∣ previous move) | P(move ∣ previous none) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| the band edge of the single seed, steps of B(t), t ∈ [2^14, 2^16] | 0.592 | 0.148 | 0.217 | 0.022 | 0.010 | 0.009 | 0.0014 | 0.0004 | 0.747 | 0.267 | 0.506 |
| the fair-row front, jumps of k_min, five rows, 45,005 steps | 0.591 | 0.145 | 0.219 | 0.023 | 0.011 | 0.009 | 0.0018 | 0.0005 | 0.758 | 0.265 | 0.509 |

**P-K1 HELD, far inside its tolerance: the two distributions agree within 0.004 in every bin, and so do their one-step
memories.** The single seed's boundary of order is, statistically, the damage front of a fair row: not only its speed (8.30,
8.74) but its whole step law and its Markov signature. This is T1's strongest evidence so far, for the one observable the
core shows the left side. (8.74's x/t = −0.2520 at 2^16 and the mean step 0.747 ↔ speed 0.253 agree with that section.)

**P-K2 HELD exactly** (45,000 steps: advance iff the cell ahead is white; the two exceptions in ten thousand are the four
junctions where one row's record meets the next, an artefact of concatenation). **P-K3 REFUTED**: the jumps have a strong
one-step memory, P(heal ∣ previous heal) = 0.265 against P(heal ∣ previous advance) = 0.509 (lag-1 autocorrelation −0.21 in the
band's steps); a two-state chain with these two numbers has stationary P(heal) = 0.409, the measured value. **P-K4 REFUTED in
its direction**: the bias is after the *advances*: P(white ahead ∣ previous advance) = 0.647, P(white ahead ∣ previous heal) =
0.510, while the cells two and three ahead are fair (0.495, 0.499): after the front steps into a white cell, the next two cells
ahead agree with each other 65% of the time. The jump size given a heal is nearly a deterministic function of the four
damaged cells at the front (patterns 0010, 0011, 1000, 1100 → jump 1; 0111, 1101 → 2; 0110, 1001 → 3, each within 0.02).

What M4 now is: **a finite object with one measured input.** The front's law is a Markov chain on (previous step type, the
four damaged cells, the cell ahead) with the mask lemma as its advance rule and a near-deterministic jump table; its one
non-trivial input is the stationary law of the cells ahead of a front that has just advanced (0.647 agreement where a fair
row would give 0.5), which is where the selection by the front's own history lives. A closed form for 0.246 is a closed form
for that one number. That is a hand question of the kind GPT and Local take: the stationary measure of a two-step-memory chain
driven by the mask lemma on a surjective CA's invariant uniform row (the unperturbed row is uniform at every time; the
conditioning on the front's position is what biases it).

### 9.2 M1, the left side's doubling law as a coincidence of consecutive diagonals (`band_coincidence.py`)

Hand (Block 22, elementary; Rowland's §5 and 8.27/8.31, known): from the left-frame rule L_e(t+1) = L_(e−2)(t) XOR (L_(e−1)(t) OR
L_e(t)), diagonal e is eventually white iff the two diagonals above it eventually coincide; then L_(e+1) is the running XOR of
L_(e−1), so the period doubles at e + 1 iff L_(e−1) has odd weight per period, else the integration constant is free (a branch).
That parity is the same **integration parity** as the right edge's doubling bit (kit `e_step`: a diagonal doubles iff the cell at
its return time is black, i.e. the weight parity of the diagonal two back, CL642) and the defect tree's type (L1296: the OR
column's weight parity decides whether both children split or both die). One object in three frames.

Predictions written first: P-J1 (control) the eventually-white diagonals to 10^6 are exactly 2, 7, 28, 399, 53,207, 58,286, 87,866
with doublings at the five and branches at the two by the parity; P-J2 the Hamming distance between consecutive settled words is
not binomial, with P(d ≤ 2) above Binomial(P, 1/2) by a factor over 1.5 in the period-16 regime (lean 55%); P-J3 no coincidence in
the period-32 regime and minimum distance at least 3 (lean 70%).

Result (COMPUTED; the band to depth 10^6 on the autonomous left-frame system run to t = 1.45 × 10^6; every diagonal 32-periodic
over the last 64 rows; the 64 settled rows kept as a checkpoint outside git, SHA-256 prefix d859972086b3dd17):

- **P-J1 HELD exactly.** The seven events, and only they; the weights of L_(e−1) per period are 1, 1, 3, 3, 5 at the doublings
  (odd) and 6, 10 at the branches (even). The integration parity decides every event in the record.
- **P-J2 REFUTED, cleanly.** In the period-16 regime (87,465 consecutive pairs) the Hamming distance between consecutive words is
  Binomial(16, 1/2) bin by bin: 0.0002/0.0002, 0.0016/0.0018, 0.009/0.0085, 0.028/0.028, 0.067/0.067, 0.123/0.122, 0.174/0.175,
  0.199/0.196 for d = 1..8 (observed/binomial), mean 7.98 against 8, and the cumulative ratios at d ≤ 1..4 are 0.97, 0.91, 1.02,
  1.02; the two coincidences in the regime (53,207 and 58,286) against 1.3 expected. In the period-32 regime (912,132 pairs) the
  mean is 16.007 against 16, the minimum distance is 3, and the ratios at d ≤ 3, 4 are 0.86, 0.91. **P-J3 HELD.**

What M1 now says: **consecutive words of the universal left side are, for the coincidence statistic, independent uniform
P-periodic words.** The 2^(−P) law is therefore a fair-coin law, not a constraint: the next eventually-white diagonal (and with
odd parity the next doubling, to period 64) is expected near 87,866 + c·2^32 with c of order one, about 4 × 10^9 diagonals, and
nothing in the words' statistics to 10^6 predicts where. This answers row 1's "where is the next doubling" in the only way the
statistics allow: it is a coincidence event with a known rate. It also puts the ordered band beside the crystal parity (§8.2):
a deterministic periodic structure whose words are pairwise indistinguishable from chance, with its order carried entirely by
the parity rule. The left edge's *algebraic* identity (which automaton the left wheel map is, and what its orbit closures are)
remains the open half of M1, for Local's kind of day.


## 10. The classic ether's exact zero is Lowry's trap entered (Block 23, CL681)

Full account in [round 11 of the inquisition tracker](inquisition-20261031.md#round-11-2026-11-02-cloud-cl681-the-classic-ethers-exact-zero-the-inserted-edge-enters-lowrys-ether-wall-trap-at-every-alignment-so-the-ether-is-never-disturbed-beyond-a-bounded-distance-news-speed-exactly-zero-proved-on-the-kits-trap_invariant).
The classic ether is the kit's `Rule30Ether` (lab period 4, spatial period 7). A black edge inserted into it enters, at every
one of the 196 alignments by t = 222, the kit's ether-wall trap (Lowry, PR65: 109 states of a 13-cell strip closed under every
right input), and `trap_invariant` keeps the ether to the left for ever: **the leftward news speed is exactly zero, PROVED**
(modulo a two-sided reading of the kit's induction, in the waiting room). Three things the atlas takes from it. (1) The velocity
spectrum's zero is a *wall*: eight period-8 columns beside the chaotic wake, not an ether phase, insulated by a closed set of
strip states, the same object as the kit's walls beside a periodic centre column, here entered naturally instead of excluded.
(2) The certificate shape for masked structures is a finite closed set of strip states under every outside input, not a
contiguous knowledge band: both band certificates fail at exactly speed 1, for stated reasons. (3) A universal healing bound
from the diagonal picture (the recruitment frontier, PROVED): the leftward damage speed of *any* perturbation at x ≥ 0 is at most
1 minus the frontier's climb rate, exact per background (1/2, 7/12, 2/9, 9/19, 6/17..15/34), attained by the inserted edge on G8
and (7, 63), not on the classic ether, (9, 57) or (12, 68). The spectrum table is in the tracker.

## 11. The closed-set certificate on the shadows (Block 24, CL682)

Full account in [round 12 of the tracker](inquisition-20261031.md#round-12-2026-11-02-cloud-cl682-the-closed-set-certificate-with-a-moving-anchor-passes-both-controls-g8s-lean-verified-law-lowrys-109-states-rediscovered-for-the-classic-ether-proves-the-9-7-law-of-7-63-at-28-alignments-and-fails-on-9-57s-519-at-every-window-to-32-although-that-law-holds-to-t--20000).
Lowry's trap generalised to a moving anchor passes both controls (G8's Lean-verified law; the classic ether, where it rediscovers
the 109 wall states), proves (7, 63)'s 2/9 law at 28 alignments as the first moving walls (70–74 states), and cannot certify
(9, 57)'s 5/19 at any window to 32, although that law holds to t = 20,000. The spectrum's exact laws therefore sort into
stationary walls, moving walls, and laws exact in fact but not adversarially robust at any tested window; the dividing question,
whether one period of the front is determined by a bounded strip under every outside input, is the same as upward rigidity in
the eternal-cycle line, and the tool is now one tool for both.
