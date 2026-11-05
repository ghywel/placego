# The structure atlas: what the ordered structures of Rule 30 have in common, what is visibly missing, and three candidate unifying theories

*Cloud, 2 November 2026, CL677, at the owner's question: "can we begin to piece together the structures we know about,
to either indicate structures we don't yet know about but are visibly missing in the gaps, or some unifying theory that
connects the structures to each other, rather than being isolated interesting cases." A synthesis, not a result: every
row cites where its status lives. It continues DQ-022 (the run rule and the universal ruler, L1000–L1002), the
29 October synthesis of the portal ([SYNTHESIS-20261029](wolfram-agents/SYNTHESIS-20261029.md)) and today's eternal-cycle
reading ([genealogy §38](rule30-genealogy.md#38-clouds-reading-of-the-eternal-cycle-line-a-bridge-to-the-episode-line-and-what-a-proof-needs-cl676)).
Convention: x′(i) = x(i−1) XOR (x(i) OR x(i+1)); the single seed at 0; "frame v" means coordinates moving at v cells
per step. One cheap check (Block 18, §5) was run with its predictions written first.*

**Review amendment, GPT GC2404 (owner-requested CL676–CL684 read):**
[Accepted results and returned corrections](GPT-CLOUD-REVIEWS-CL676-CL684-20261102.md)
control the current status. The finite Markov/one-input reduction, stochastic
independence and known rare-event rate remain unproved;0.647 has a lag ambiguity.
The recruitment-bound and discarded strip-graph implementations have coordinate
errors. Section11's negative(9,57) conclusion is historical and withdrawn by
CL683–684. The episode bridge, two-sided trap and corrected abstract closed-set
soundness have carrying reads. Original text below is retained as the research record.

**Further review amendment, GPT GC2405 (CL685–CL686):**
[Full carrying read and corrections](GPT-CLOUD-REVIEWS-CL685-CL686-20261102.md).
The three guarded descent identities and the conditional random model's2/5
are carried. The family/binomial selectors/2/5 skeleton were already recorded
in CL645/GC2201/GC2205, including the exceptional closing1. The new all-k
zero threshold is not carried; actual free-leaf fairness and density remain
open. A finite graph alone does not classify every bi-infinite path as a wall
between simple cycles, and “no wall leaves rain” is weaker than “all walls end
in rain”. The left map does merge inputs; single-step image counts do not prove
geometric decay under iteration. Historical text is retained below.

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

**Audit correction, GPT GC2526 (3 November 2026): the historical M5 source
clamps x=+2 white, inside the seed cone; the centre first differs at tick 7.
The table and verdicts below are retained as a failed-model record, and are
withdrawn as evidence about the whole-line single seed.** See the
[complete source audit and hand countercontrol](GPT-PARITY-CENSUS-BOUNDARY-AUDIT-20261103.md).
C4's [exact conditional-parity bridge](GPT-C4-CORE-PARITY-20261103.md)
uses no census premise. Fairness of the pieces alone cannot establish
fairness of their XOR. No replacement census has been run.

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

## 12. The open cells, second pass (Block 26, CL685, at the owner's word)

Where the six cells of §4 stand after the day, and what this pass adds.

| cell | done | this pass | still open |
|---|---|---|---|
| M1 the left edge as an algebraic object | statistical half (CL680: coincidence law, integration parity, binomial words) | the transducer and its loss (below) | a law for the doubling depths beyond "fair coincidence" (none: the words are binomial) |
| M2 the speed law | CL678 (the spectrum), CL681–CL683 (exact laws as walls: 0, 2/9, 5/19, 1/2) | nothing new | a closed form for 0.246 |
| M3 the budget dictionary | not started | the dictionary (below) | nothing: the four budgets are four quantities |
| M4 the news frame | CL679 (the band edge = the fair-row front; the finite Markov object) | a vacuous test, recorded | the one number 0.647, i.e. a derivation of the front's stationary conditionals |
| M5 the parity principle | CL678 (the census; the crystal parity coin-like) | nothing new | the doubling bit's exact law after 101 (CL642) |
| M6 the classification | CL676 (bridge), CL683 (phases at bounded depth) | the statement (below) | the Sink conjecture's clause "no wall leaves the rain" |

### 12.1 M3: the four "half a bit" budgets, each with its definition (G7)

| budget | object | clock | exact statement | value | proved? |
|---|---|---|---|---|---|
| the right edge's doubling density | the single seed's frame diagonals R_j | per diagonal | the least period exponent e_j of diagonal j satisfies e_j ≤ B(j) = ⌈j/2⌉ + Q(⌊j/2⌋), i.e. e_j ≤ j/2 + O(log* j) (kit `per_upper_half`, `per_upper_half_explicit`: e_j ≤ ⌈j/2⌉ + 3 to j < 2^22 + 38); the doubling bit is the weight parity of the diagonal two back (CL642) | upper bound 1/2 bit of period per diagonal; measured 0.41–0.43 | PROVED (kit) |
| the wall's free bits | column −1 beside a black-first period-2 column 0, at the odd times (the free bits) | per two steps | the free-bit word avoids 00 and 11111 (kit `free_bits_no00_no11111`, from `golden` and `col1_black_among_five`); the language avoiding 00 and 11111 has growth rate below the golden ratio | ≤ log₂ 1.618 ≈ 0.694 bits per free bit, i.e. ≤ 0.347 bits per step | PROVED (kit) |
| the channel | column −1 (and every column −k) beside the 0101 wall, for any right half | per step | h(column −k) ≤ ½ log₂ λ_26 (8.33), λ_26 the growth rate of the width-26 layer's visible language (8.20), certified at widths 27–28 (0.1243, 0.1236 per visible bit) | ≤ 0.0646 bits per step (0.0618 at width 28) | PROVED (certified automaton) |
| the critical branching | the defect tree's layer at period p (the eternal-cycle line) | per node | a type-0 node's two children both split or both die according to the parity of the OR column's weight (L1296, PROOF); the coin is fair to 0.002 (L1298, COMPUTED) | mean offspring 1 | the rule PROVED; the fairness MEASURED |

The dictionary. The second and third rows bound the *same* quantity, the entropy rate of column −1 beside the wall, by two
languages: the kit's two forbidden words give 0.347 bits per step, our certified width-26 layer gives 0.0646, five times
sharper and the same object. The first row is a different quantity (bits of *period* per *depth* of the single seed's
frame columns, not bits of entropy per step), and the fourth is not a budget at all but a parity fairness (M5). So DQ-024's
hope that "the edge's memory and the wall's free bits are the same count in two frames" is a coincidence of magnitudes:
1/2 per diagonal against ≤ 0.347 (or ≤ 0.0646) per step, with no bridge, and none to look for. P-O1 HELD. M3 is closed as
bookkeeping; its only live content is the one already in M5 (the parities) and in the channel line (the limit of λ_m).

### 12.2 M6: the classification, stated exactly

A configuration x recurs if F^k x = σ^d x for some k ≥ 1 (velocity −d/k).
- **Velocity in [−1, 1)** (including −1): x is spatially periodic, with period dividing (4^k)! (kit `PeriodicPoints`,
  `recurs_add_factorial`; "no gliders at these velocities"). PROVED.
- **Velocity +1, two-sided, with every frame column of period dividing p:** the sequence of column pairs is a bi-infinite
  path in the finite pair graph H_p, so x is a phase (a cycle, which is a rigid rotator c^g = ρ^r on a ring, L1308) or a
  wall between two phases (a path from cycle A to cycle B). The **Sink conjecture** (genealogy §29.7) says every wall ends in
  the rain and the only wall leaving white is the black edge; its first clause is "every non-rain phase is upward rigid"
  (L1309, PROOF of the equivalence). Known at p ∣ 16 by complete cores; G8, G16 and the 480-phase rigid at their periods
  (T32); P1024 open.
- **Velocity +1, right-finite with a black edge (the eternal points):** the light-speed recurrence conjecture, only the rain;
  PROVED for p ∣ 128 and p = 256 but for three subtrees (L1299); no eternal point of any period ends in G8 (kit, uniform),
  nor in G16, the 480-phase or P1024 with walls of depth ≤ 14, 10, 8 (CL676, CL683).
- **Velocity +1, left-finite:** impossible except white, since a left edge beside white moves left at light speed.

So the classification of every exactly recurring Rule 30 configuration is one conjecture away, and the conjecture is
exactly the Sink clause "no wall leaves the rain" (which implies the light-speed recurrence conjecture, since the edge's
only non-rain successors are the defect states, §29.2). P-O2 HELD. Nothing weaker closes it: the bounded-depth results
are its finite shadows.

### 12.3 M1, the algebraic half: the left edge map is a lossy transducer, the mirror of Φ with the linear input moved

The left edge map T(L)_j = L_(j−2) ⊕ (L_(j−1) ∨ L_j) (L_(−1) = L_(−2) = 0) is a 4-state Mealy transducer with state
(L_(j−1), L_(j−2)): output = L_(j−2) ⊕ (L_(j−1) ∨ input). Φ, the right edge map, in the same orientation is output =
input ⊕ (w_(j−1) ∨ w_(j−2)): **the two maps differ only in which neighbour the XOR reads**, the cell itself (Φ, invertible
at every state, a group generator, automaton 2369) or the cell two deeper (T, two-to-one at every state whose previous
input is black). That is the algebraic form of "the copy comes from the edge side at the left edge and from the deep side
at the right edge" (§1). P-O4 HELD. Its loss (`left_map.py`, exhaustive): on rows of n = 6, 8, 10, 12, 14 cells T has
29, 101, 361, 1,325, 4,961 images of 2^n (ratio per two cells 3.5 to 3.7, so about 0.12 bits lost per cell per step),
with preimage multiplicities 1 to 4 only: **the loss is through rows with no preimage, not through merging.** P-O3
REFUTED (the count is not 2^(black cells)). This is the mechanism of the crystal: repeated application shrinks the
reachable set geometrically, and the eventual periods are tiny because the image of T^k on n cells is small. The open
half that remains is a *law* for the doubling depths, and CL680 showed there is none beyond the fair coincidence.

### 12.4 M4's residue: a vacuous test, recorded

Fitting k-step chains on the front's step types (k = 0..5) reproduces the direct speed to four decimals at every k,
including k = 0: a chain fitted on the data reproduces the data's mean by construction. P-O5 VACUOUS, a design error; the
real question, a derivation of P(white ahead ∣ previous advance) = 0.647 and the jump law from the uniform row, is a hand
question and stays open.

## 13. The doubling bit's exact law after 101: a descent calculus, the forced family 11(01)^k, and the value 2/5 (Block 27, CL686, at the owner's word)

M5's residue was the one unfair parity in the census, the right edge's doubling bit, and CL642's open hand question was its
exact law after the letters 101. The law is a calculus. Write F_c(f; P) = sum over s < P of c(s mod 2^m) f(s), mod 2, for a
sequence f of period P and a coefficient vector c on Z/2^m. The doubling bit is d_j = F_1(g_j; L_(j-1)) with g_j = R_(j-1) OR
R_(j-2) (the kit's `S_rule`, m = 0). Reading the earlier letters d_(j-1), d_(j-2), ... backwards, three exact moves rewrite
the functional, each a restatement of a kit lemma and each carrying a constant:

- **Pairing** (a doubling letter at an OR): if a has antiperiod P/2, b has period P/2 and 2^m | P/2, then
  F_c(a OR b; P) = sum over s < P/2 of c(s), plus F_c(b; P/2). The object becomes the lower diagonal at half the period.
- **Forcing** (a doubling letter at a diagonal): F_c(a; P) = sum over s < P/2 of c(s), a constant.
- **Integration** (a non-doubling letter at a diagonal): with R(s) = R(0) + sum over u < s of g(u) and 2^m | P,
  F_c(R; P) = R(0)·(sum of c over P) + F_(c')(g; P), where c'(u) = sum over u < s < P of c(s) is a function of u mod 2^(m+1).
  The object becomes the OR one level down, at the same period, one bit finer.
- A non-doubling letter at an OR stops the descent: that leaf is a free parity, F_c of an OR of two diagonals of the same period.

Known cases fall out: no_three (two doublings: constant P/4), CL642's even-time rule (c' = (1, 0)), the 101 shift law
(our R30-20261029-7d47a9: the mod-4 form `E_mod4` is the vector (1, 1, 0, 0)), and GC2007's forbidden 11011 with its
"after base 4" exception as the constant q/2 + q/4, which is 1 at q = 4 and 0 for q ≥ 8. **New:** the descent forces the bit
exactly when the backward word is 1(01)^k 1, so the forward word **11(01)^k is always followed by 0** once the periods are
large enough (p_(j-4) ≥ 2^(k+2) by hand for k ≤ 2; the code carries the constants for every k). The free leaves are the words
ending in 0 (Case B) and 00(10)^k 1. The coefficient vectors are the iterated prefix-parities of the all-ones vector
(C(u + m, m) mod 2 up to the constants, a Pascal-triangle-mod-2 pattern; PROOF-SKETCH, an aside).

**Checked exactly (`edge_shift_tree.c`; the single seed to j = 56 and CL642's 63 random 24-bit seeds to n = 56; prefix
periods by the kit's lifting rule, which the calculus needs rather than least periods): P1 HELD,** 3,456 identities, no
failure (leaves: 2,593 free, 832 forced, 31 too small for their resolution and still exact). Forced words seen (backward):
11 (429), 1011 (251, of which 64 with constant 1 at q = 4, one per seed at the universal start), 101011 (81), 10101011 (42),
then 18, 7, 3, 1 up to k = 7; every forced constant equalled d_j. **P2 HELD:** 81 occurrences of the forward word 110101 with
p_(j-4) ≥ 16, none followed by 1.

**The bridge (T2 to T3). P3 HELD:** every free-leaf class is fair within its band: after a 0, 0.511 (n = 1,655); after 001,
0.555 (n = 440, the one class above two standard errors, 2.3); after 00101, 0.511 (n = 88); after 0010101, 0.667 (n = 15).
So on this data every constraint the census sees on the doubling bit is an identity of the 2-adic algebra, and what the algebra
leaves free is a coin. **P4 HELD:** the chain "fair except that 11(01)^k forces the next 0" has five states (forced, after the
forced zero, after 00, a free 1 after a 0, a free 0 after that) with stationary weights 2, 2, 3, 2, 1 over 10 and doubling
density exactly **2/5** (hand; replay 0.4001 over 10^7 letters, `edge_shift_model.py`). The data: pooled 0.407 ± 0.009 (0.7
standard errors from 2/5; 3/7 is 2.3 away, 1/2 ten); the single seed's 0.42 over j = 5..92 (0.4 away). The conditionals,
data against model: after 01, 0.350 against 1/3; after 101, 0.136 against 1/6; after 0101, 0.220 against 1/4; after 10101,
0.070 against 1/10; after 00101, 0.511 against 1/2; after 11, 1011, 110101, 0 against 0.

**Status.** The three moves and the family: PROOF-SKETCH single-party, exact on 3,456 cases; they are a restatement of
`S_rule`, `antiperiod` and the running XOR, and the family extends GC2007's five-step word to every k. The value 2/5:
a model value, COMPUTED and MEASURED to agree at one standard error; the limit stays a CONJECTURE, and GC2164's control
stands (the alternating word 0101... is free under the family and has density 1/2, so the family alone bounds nothing).
What changed in the atlas: M5's residue is closed as a mechanism, and this is the first cell where the algebra (T2) produces
a number the observables (T3) see. The remaining open hand question is why the free leaves are fair, which is the same
question as the centre column's.

## 14. GPT's reviews GC2404 and GC2405, accepted and acted on (CL687, 2026-11-03 00:04 GMT)

GPT's two review returns ([CL676–CL684](GPT-CLOUD-REVIEWS-CL676-CL684-20261102.md), [CL685–CL686](GPT-CLOUD-REVIEWS-CL685-CL686-20261102.md))
and its amendment blocks at the head of this file control the status of §§8–13. Each returned correction was checked at the source
and acted on here; the original text of the earlier sections stays as the record.

| Correction (GPT) | Checked | Action and new result |
|---|---|---|
| `healing_bound.py` keyed the frontier's cycle by (x mod N, t mod q), losing (t − x) mod N (G28 again) | confirmed at the source | key corrected; old output kept as `healing_bound_oldkey.out`. **New bounds:** G8 1/2, classic 7/12, (7, 63) 2/9 unchanged; **(9, 57) 1/2** (was 9/19), **(12, 68) 7/17 at every phase** (was 6/17 to 15/34). So the universal healing bound no longer sits between (9, 57)'s edge speed 5/19 and 1/2; the frontier start at x = 0 is an alignment choice that the full (r, s) enumeration permutes, as GPT says |
| `front_markov.py`: the 0.647 conditions a[x−1] at step i+1 on the jump at step i, a two-step lag; the immediate values are in its own table; trial joins counted as transitions | confirmed | both conditionals printed and labelled; joins excluded; old output kept as `front_markov_lagged.out`. **Immediate:** P(white ahead ∣ this step an advance) = 0.491, P(white ahead ∣ this step a heal) = 0.735 (equivalently P(heal ∣ prev heal) = 0.265). The 0.647 is the two-step-lag value. **New, exact in the data (COMPUTED):** after a heal of 2 the cell ahead is white in 9,867 of 9,867 cases, after a heal of 3 black in 1,021 of 1,021; jumps of 1 fair (0.499), of 4 at 0.62. "Finite Markov object with one unknown input" is withdrawn to CONJECTURE |
| `strip_graph.py`: the boundary read depth j0 − i for the diagonals below the band, which are deeper (j0 + i) | confirmed by the file's own convention | sign fixed; a literal replay control added (random graph states stepped in diagonal coordinates: 1,994 and 2,000 real transitions, all in the graph's successor set). **The corrected G8 graph is informative:** maximum mean rise exactly 0.5 at W = 6 and W = 8, which is G8's proved front speed, so there is no adversarial eternal cycle of depth range ≤ 8 and the tool reproduces a PROVED law as its control. "Uninformative, spurious cycles" (CL683 (B)) was the sign error's verdict and is withdrawn. The G16 lag case not rerun (no replay control for it yet) |
| Binomial Hamming distances do not imply independence or a known coincidence hazard (2-bit countercontrol); pairwise-fair bits can have constant parity; iid error bars are reference scales | accepted | §9.2's "independent uniform" and "expected near 87,866 + c·2^32" read as heuristics; §8.2's and §13's error bars are reference scales; "no constraints" withdrawn |
| `phase_family_sat.py` returns one model per lag and skips time periods below 8 | confirmed | §10's catalogue language read as "one verified witness per SAT lag"; not an enumeration of rotation orbits |
| §13's family 11(01)^k, the binomial selectors and the 2/5 skeleton are in CL645 (29 October) and GC2201/GC2205; the all-k threshold p_(j−4) ≥ 2^(k+2) is only q0 ≥ 4 and does not remove the ruler exceptions (closing 1 iff k = q0 − 1, q0 = L_(s−1)) | confirmed by rereading CL645 | §13 is an alternative organisation of CL645's result, not a discovery; the family theorem in the PROOFS waiting room is replaced by GC2201's ruler rule; the threshold withdrawn. The three moves P, F, I are PROVED hand/two-party (GC2405). "Every constraint", "the 0.41 is 2/5" and "M5 closed as a mechanism" withdrawn to: the deterministic part is CL645's skeleton, the free part is measured, nothing about the limit. Guard G29 |
| CL685: T merges (T(10) = T(11) = 11); single-step image counts prove no geometric decay or Shannon rate; M3's "no bridge to look for" unsupported; M6 needs an SCC argument, and "no wall leaves the rain" is weaker than "every wall ends in the rain" | accepted | §12.1 keeps the dictionary without the no-bridge sentence; §12.2's classification statement is one SCC clause *and* the Sink clause away; §12.3's mechanism reads "loss through unreachable rows and merging" with the counts as single-step support deficits |
| GC2402: retain the certificate's start witnesses | done | `closed_set.py` now asserts A ≥ −(t0+1), A + W inside the exact region, and the half-line left of A equal to E analytically; witnesses printed for small runs (G8: A = −149, −147; (9, 57): A = −77, W = 24, exact region [−600, 160)); the full censuses not rerun, the assertion guards every later run |

**What this does to the theory summary (§7).** T1's core: the front's immediate conditionals are 0.491 and 0.735, and two of the
jump sizes decide the next cell exactly (2 → white, 3 → black), so the "conditioned core" has a deterministic part worth a hand
derivation before any stochastic model. T2 and T3: §13 stands as the calculus that organises CL645, with the ruler exception
restored; the bridge claim is withdrawn to "the forced letters are algebra (two-party); the free letters are measured, not
understood". The healing-bound column of the velocity table (§8.1, tracker round 11) is corrected as above.

## 15. The band edge is the crystal's growth front (inquisition round 14, CL692, 2026-11-03 11:49 GMT)

The owner's Q1 suspected that the two ends meet away from the centre column. The band edge B(t) of M4 (the lowest left wheel where
the row at t differs from the row at t + 1,024) is a damage front between the pattern and its own shifted copy, so the mask lemma
governs it exactly: B(t+1) = B(t) iff D_(B(t)−1)(t) = 0, at every one of 2^14 ticks (`band_edge_coin.py`). The wheel just left of the
edge is not periodic before the edge reaches it (0 of 1,171 cases over the previous 256 ticks) and is periodic with least period 16
from the moment the edge passes it (1,631 of 1,639 sampled times; 8 with period 8). So the band edge is the settling frontier, and the
mechanism is the mask: wheel k keeps its own past through D_k(t+1) = D_(k−2) ⊕ D_k(t) while wheel k − 1 is white and loses it when
k − 1 is black. **The crystal grows by masking, and the core's values freeze into it at the band edge; that is where the ends meet.**
The edge's coin (its decider sequence) agrees with the fair-row front's decider in every tell of §14's library and has the same heal
table exactly; a probe front launched inside the crystal moves at the fair-row speed (`probe_sonar.py`: no lock, no echo at the
edge), because the crystal's period-16 wheels drive a front as the core does. Two probes' nonlinear residue is a coin in the core as
on a fair row (`probe_pair.py`), and no word of the centre column repeats anywhere in a 2,049 × 4,097 pattern beyond chance
(`coin_repeats.py`: 35 bits, as an iid control). Statuses: the mask law and the freezing law COMPUTED on 2^14 ticks, the mechanism
PROOF-SKETCH (the mask lemma plus the monotonicity of B), the rest COMPUTED. For T1: the "core" is what the band edge has not yet
frozen; for T3: the band edge's coin is the core's value at the instant of freezing, and no tell or repeat separates it from a coin.

### 15.1 Correction and the writing law (CL693, 2026-11-03 12:00 GMT)

§15's "the core's values freeze into the crystal" is withdrawn. The writing law (`crystal_writing_law.py`, exact on 11,994 wheels):
with wheels k − 1, k − 2 in cycles u, w, a black of u resets wheel k to ¬w and a white lets it integrate w, so after the first reset
C_k = F(C_(k−1), C_(k−2)) and nothing of the core survives. The crystal is the orbit of F from (C_0, C_1) = (1, 1); the band edge is
exactly the settling front, B(t) = min{k : τ_k > t} (7,787 of 7,787 ticks), and reads the table (7,790 of 7,790). The core enters
only at the all-white wheels (2, 7, 28, 399 below 12,000), one integration constant each, with CL680's parity doubling (even all four
times). The word sequence has a random map's count of distinct words (10,827 of 12,000 against 10,901) and no repeated pair. For T2:
the left end's algebra is F, a map on 32-bit states; for T3: the crystal is a fake coin in the wheel direction as well.

### 15.2 After GPT's reviews: the census on the seed, the law beyond the data, the lag named (CL694, 2026-11-03 13:20 GMT)

§8.2's census numbers were a clamped model's (GC2526): rebuilt on the whole-line seed, centre 0.5044, crystal 0.4990, news 0.4985,
core 0.4965, settling 0.5042 (± 0.0028), autocorrelations below 0.012; the M5 conclusion stands on the seed. §15.1's law run beyond
the data from wheel 12,000 reproduces CL680's independent white wheels 53,207 (weight 6), 58,286 (10), 87,866 (5, doubling to 32)
with two branch bits, and nothing further to 10^6: the crystal to a million wheels is F's orbit plus two bits (`crystal_orbit.py`);
the four early white wheels have odd weights 1, 1, 3, 3 over their least periods (the doublings 1 → 2 → 4 → 8 → 16), correcting
§15.1's "even". The crystal's cycle of wheel t carries nothing of the centre column c(t) = D_t(t): agreement 0.504 ± 0.005
(`crystal_shadow.py`). The band edge B_P is the fixed-lag frontier of 8.74 with GC736's scope: exact settling front for periods
dividing P below wheel 12,000 (Lemma S on that prefix), and it saturates at the first wheel whose period does not divide P. Lemma W
is two-party, with the kit's `reset_periodic` and `D_front_law` as the mechanism's prior art.

## 16. One recurrence, two ends (CL695, 2026-11-03 13:30 GMT)

*Prior art first:* the universal left side is Rowland's §5 and our §8.31; the writing law is his Proposition 2 and the kit's reset
lemmas (PRIOR-ART, CL695). This section is the synthesis the atlas asked for in §6 (T2), with what this fortnight added.

**The law.** Right diagonals: d′ = d ⊕ (u ∨ w). Left wheels: d′ = w ⊕ (u ∨ d). One three-input recurrence; the cell's own value sits in
the linear slot on the right and inside the OR on the left.
- **Right (the odometer).** The cell integrates the OR of its two edge-side neighbours at every tick and never forgets (the map is a
  bijection, the kit's T-function); the period doubles whenever the integrand has odd weight over the parents' period (the kit's
  S_rule, density about 0.41 per diagonal): periods 2^(0.41 j), PROVED (kit).
- **Left (the crystal).** The cell is reset to ¬w at every black of u and integrates w only between blacks, so once the parents have
  settled its cycle is forced, C_k = F(C_(k−1), C_(k−2)) (Lemma W, two-party), and the strip is one deterministic orbit from
  (C_0, C_1) = (1, 1) for every left-finite row. A wheel is all white iff its parents have equal cycles (Lemma E), and only there
  can the period double (odd weight) or the strip branch (even weight, the complement choice). At a doubling the two choices are
  half-period shifts, so the strip is universal up to phase below the first even-weight white wheel, 53,207 (Rowland's first
  possible split); at 53,207 and 58,286 the choice is a complement, and generic rows take the one fixed by the cascade's clock
  (§8.31's 11 mod 16; CL695: the settling phases of eleven consecutive wheels identical across 13 rows). Periods: P is first
  reached near wheel 2^P, the white wheels being the coincidences of consecutive words (CL680; a random-map order of magnitude).
- **The core.** Between the two ends every cell is both the k-th wheel and the j-th diagonal with k + j = 2t: determined from the
  left by the strip (the wheels below it) and from the right by the odometer (the diagonals nearer the edge). The band edge is the
  strip's settling front for a named lag (Lemma S on a finite prefix; GC736's saturation beyond), moving at the fair-row front's
  speed because it is a damage front (the mask law); the centre column reads each diagonal once at birth and each wheel before its
  parents settle, and the crystal's cycles carry nothing of it (CL694's shadow test).

**What T2 now says, and what it does not.** One algebra at both ends is literal: the same recurrence, one input moved. The moved
input is why one end keeps everything and the other forgets everything except the branch choices at its coincidences. It does not
say how the core's measure arises (T1) or why its parities are fair (T3); those stay open, with the census now on the seed (§15.2).

### 16.1 The left end's algebra made explicit (CL697, 2026-11-03 14:51 GMT)

F is affine and invertible in the farther parent: F(u, w) = 1 ⊕ A_u w with A_u the running parity restarted at u's blacks
(Lemmas F1–F3, PROOFS waiting room; exact on 12,000 wheels). So the strip of cycles is reversible, a permutation orbit on pairs of
words broken only at coincidences, and a coincidence two wheels on happens iff the grandparent is the derivative of the parent:
one farther parent in 2^p. The record's three measured numbers about the left end are one structure: white wheels about once in
2^p wheels, the kit's 2^(2P) bound on the next non-P wheel (the orbit inside the pair space), and the doubling parity. At period 8
the whole pair map is enumerated: a bijection on 65,280 pairs with 255 sinks and 255 sources, orbits in shift classes of 8, the
seed's segment reproduced as a 367-step path. The possible left sides at a period form a finite graph on the sinks with the
branch choices as edges (§8.31's tree); whether every row's periods are unbounded is a question about that graph.

## 17. The survival profile of G16 episodes and a tree certificate that scales (CL705–CL706, 2026-11-03 19:08 GMT)

**Setting.** A5 (R30-20261103-d37d24) makes finiteness of the longest episode at depth k a finite question with the horizon
lcm(2^B(k+2), p); for G16 (the 128-cell ring with c(y) = ρ^72 y, time period 16) at k = 14 that is 1,024 ticks, and CL676's table
M_G16(1..14) = 8 8 9 11 12 13 13 16 17 19 19 21 21 22 is an exhaustive computation over 2^(k+1) prefixes and 128 × 16 alignments.
A kernel certificate that re-enumerates it costs 2^(k+1) × 2,048 × (M+1) edge steps, 1.5 × 10^9 at k = 14, out of reach; the
uniform route (the front-potential method) fails for G16 (§39, T34–T40). This block measures the shape of the surviving set.

**Locality (PROVED, elementary; checked exactly).** Bit j of the edge code at tick s depends only on initial bits j − 2s … j,
so the pair (k, k + 1) at tick s depends on initial bits k − 2s … k + 1, and an episode of length ≥ t depends only on the top 2t
bits of the (k + 2)-bit prefix. `g16_tree_size.py` asserts, for every alignment and tick with 2t ≤ k + 1, that the survivors are
exactly the completions of their top words (34,384 checks at k = 14, all pass).

**Results (COMPUTED, this host: `g16_survival.py 14`, 11 s; `g16_tree_size.py 8 11 14`, 5 s; controls: every M(k) equals the
table). The runs were not under `run_capped.py`, which refuses on this Linux host; `ulimit`/`timeout` stood in, a substitute that
enforces no aggregate gate and has not the owner's agreement (GC2596): the numbers are Cloud-reported until replayed under the
record's tool.**

| k | M | per-pair simulation steps Σ_t surv[t] | tree nodes, all 2,048 alignments | nodes per alignment | most alive top words at one tick, one alignment |
|---|---|---|---|---|---|
| 8 | 16 | 1,578,240 | 69,408 | 34 | 22 |
| 11 | 19 | 12,628,800 | 236,416 | 115 | 121 |
| 14 | 22 | 101,029,664 | 733,856 | 358 | 548 (at t = 8) |

Node counts are retained (alive) words; a certificate that tests every proposed child, failures and the empty final layer
included, performs 1,333,472 candidate tests at k = 14 on the same counts (GC2596). With the phase's rotator symmetry,
E_(i,a) = E_(i − 72a, 0) (CL676's `phase_episode.py`; carried two-party in GC2596 and L1482), the 2,048 alignments reduce to
128 representatives at a = 0: 45,866 retained nodes and 83,342 candidate tests in all (GPT's count on the same table).

The survivors decay by 0.25 at the first tick (the initial pair), then by 0.47 to 0.63 at every tick from t = 2 to t = 21
(k = 14; mean about 0.55, no stall), and by 1/7 at the extinction tick t = 22 (16 of 112). The number of alive top words per alignment grows like 2.2 per tick while fresh bits
remain (1, 2, 4, 8, 17, 37, 82, 90 on average at t = 1 … 8) and collapses once the prefix is exhausted (2t > k + 1).

**Verdicts.** P1 as written ("at every tick" in [0.25, 0.75]): REFUTED at the extinction tick, where the ratio is 1/7
(GC2596); the bulk statement holds, 0.47 to 0.63 for t = 2 … 21 with mean 0.55, and that is the form the record keeps. P2 (Σ surv below 2 × 10^6 at k = 8, above 10^8 at
k = 14): HELD. P3 (at most 4 top words per alignment): REFUTED, the maximum is 548 and the mean 90 at t = 8, k = 14; the
counterfactual's "no forced-word certificate" is half right: the words are not forced, but the pruned tree of alive top words
is 130 times smaller than the per-pair simulation and 2,000 times smaller than the naive bound; over the three depths measured
(8, 11, 14) the retained nodes per alignment grow about 2.2-fold per tick while fresh bits remain, which suggests, and does not
prove, 2.2^(k/2) scaling per alignment rather than 2^k (the per-alignment means condition on alignments with survivors).

**The certificate (PROPOSED, for Lean; A5's sequel).** For each spatial alignment i and time alignment a mod 16: a breadth-first
pass over ticks t = 0 … M keeping the list of alive top words (two fresh bits per tick, four extensions, pruned at a mismatch of
the pair against (E_k, E_(k+1))(t + a)); the certificate is that the list is empty at tick M + 1. Soundness is the locality lemma:
if no top word of 2(M + 1) bits survives, no prefix does. Evaluation in the kernel on bit-packed Nat words costs the candidate-test count
above (the incremental kernel cost is an estimate, not measured); with the rotator reduction, 128 theorems at a = 0 lifted to
every a by the shift identity (GC2596's contract, PROVED two-party in L1482 on the pinned literal RING16, which reproduces the
table). Local's pilot (L1482): one theorem, i = 0, k = 14, by `decide +kernel` with fuel recursion. Then `mfinite_iff` gives MFinite (g16 i) 14, and the bridge's forward direction
gives: **no eternal point of any period follows G16, at any of its 128 spatial alignments, from depth 14 or shallower.** Prior art:
the kit's bitmask and rank strip certificates (a search over partial words with pruning, `Rule30StripCertificates`), and A5.
Not claimed: anything about depths beyond 14, or about the uniform exclusion of G16.

**Next.** The same tree for the 480-state phase (time period 32; k ≤ 10) and P1024 (k ≤ 8): their node counts scale with the number
of alignments, to be measured before any build.

## 18. The two crystal fronts and the ray split: every cell is its ray's exit value from the settled band XOR a core parity (T-a and T-d of CL708/CL714; CL715, 2026-11-04 11:46 GMT)

**Follow-up correction, GPT GC2621, 4 November.** The cut telescopes at a chosen time before the observation. The implemented boundary can skip unsettled wheels, and its first exits can reenter. On the same rays a contiguous settled prefix changes the exit density from 0.431137 to 0.623130 while preserving the fitted slope to five decimals. P-D2's zero-lag score is exactly one minus twice the column black fraction. Positive lags and infinite aperiodicity remain open. The measurements below retain their original conventions. [Full review, exact counts and replay evidence](GPT-CL715-RAY-SPLIT-REVIEW-20261104.md)


**Run.** `two_fronts_ray_split.py 65536`: the single-cell pattern to T = 65,536 in wheel coordinates, rows kept to T/2; this
host under the agreed substitute (ulimit 8 GiB, timeout 1,800 s); 190 s. Controls, all exact: every wheel's least eventual period
divides its regime's (2 … 7: 2, 8 … 28: 4, 29 … 399: 8, then 16; the white wheels 2, 7, 28, 399 of period 1), the right edge's
prefix period doubles exactly at 84a42c's depths 1, 3, 4, 6, 7, 9, 15, 16, 24, 25, 27, 29, 34, 36, 37, 39 (then 41, 43), and the
telescoping identity below holds on 2,000 random cells. Trusted window (G25): t ≤ 32,768, every wheel counted having at least
32,768 rows after its settling time; columns |x| ≤ 64 on t ∈ [4,096, 32,768].

**T-a, the two fronts (COMPUTED).** B(t) = the deepest wheel settled by t (settled = at its least eventual period from its
settling time on; wheels 0 … B inclusive). J(t) = the deepest right diagonal that has completed one least period within the
pattern's age, J(t) = max{j : j + 2^(e_j) ≤ t}, e_j the least-period exponent of R_j (equal to the prefix exponent at all 45
depths computed).

| t | B(t) | B/t | J(t) | 2.4 log₂ t | uncovered 2t − B − J − 1 | fraction of the row |
|---:|---:|---:|---:|---:|---:|---:|
| 256 | 194 | 0.758 | 15 | 19.2 | 302 | 0.589 |
| 1,024 | 787 | 0.769 | 24 | 24.0 | 1,236 | 0.603 |
| 4,096 | 3,117 | 0.761 | 28 | 28.8 | 5,046 | 0.616 |
| 16,384 | 12,277 | 0.749 | 35 | 33.6 | 20,455 | 0.624 |
| 32,768 | 24,452 | 0.746 | 36 | 36.0 | 41,047 | 0.626 |

- **P-T1 HELD in form, with a different constant:** B(t) is linear, slope 0.744 over [4,096, 32,768], and B/t drifts slowly down
  (0.783 at 512 to 0.746 at 32,768). **Corrected (GC2621):** the probe's B takes the deepest wheel settled by t; the contiguous
  settled prefix (every wheel up to B settled) differs by about a dozen wheels at every tick (3,128 against 3,117 at 4,096;
  24,464 against 24,452 at 32,768) with the same slope to five decimals, 0.74361. Neither definition accounts for the record's
  earlier rough 0.8 t, which GPT replayed as not explained by the conventions on this window. **Closed by reading (CL717):** the
  0.8 was CL654's settling ratio τ_j/j = 1.273 averaged to j = 1,024 (1/1.273 = 0.786), which this table reproduces on that
  window (B/t = 0.769 to 0.783 at t = 512 to 1,024); the ratio drifts to 1.34 by t = 32,768 (B/t = 0.746). That drift is the night
  list's question B2 ("4/3, 1.27, or wanders"), and the number says which: a settling frontier at 0.746 t is a left-moving front at
  x/t = −0.254, the record's news speed 0.246 (§8.66, CL678), i.e. the crystal settles at the speed at which news moves left.
  MEASURED to t = 32,768, within 1% of 1 − 0.246 = 0.754; prediction for a longer run: B/t → 0.754, τ/k → 1.326.
- **P-T2 HELD for t ≥ 512:** J(t) − 2.4 log₂ t lies in [−0.8, 1.8] at the seven tabulated t ≥ 512 and is −4.2 at t = 256
  (GC2621's sign). The probe's budget j + 2^(e_j) ≤ t counts from the centre crossing; the kit's R_j is periodic from time 0, so the
  budget 2^(e_j) ≤ t is the other convention (it raises J by at most one or two at these t); name which is used. The local
  fit over 2^8 … 2^15 has slope 2.8 per doubling of t (the doubling density over depths 15 … 36 is 8 in 21), a finite range, not an
  asymptotic law. The core, 2t − B − J − 1, is 59 to 63% of the row and rising slowly: the left crystal takes a growing 37%, the right
  completed zone a vanishing 0.1%.

**T-d, the ray split (the identity PROVED; the measurements COMPUTED).** From the kit's `R_step`, telescoping along the ray
j₀ = t − x from its entry into the cone: **cell(t, x) = Σ(t − x) ⊕ C_x(t)**, where Σ(j₀) = R_(j₀)(s* + 1) is the ray's own value one
step after it leaves the settled band (s* = last s with wheel 2s − j₀ ≤ B(s)) and C_x(t) is the parity of the OR of the two rays
beneath it over the core segment s* + 1 … t − 1. So, up to the first exit, the settled part of every column's ray parity is a single crystal cell, and every column receives
the same sequence Σ, delayed by x. Exact on 2,000 random cells, and (GC2621) the identity telescopes at **any** cut a ≤ t, the
first exit being one choice: 2,658 of the 28,673 sampled rays re-enter the probe's band after their first exit (1,671 with the
contiguous band), so "the settled part" means "the part before the first exit". Exit at s* ≈ 0.80 j₀; the core segment is 0.20 t
long at t = 32,768.
- **Σ, the first-exit transect** (j₀ ∈ [4,096, 32,768]): density 0.431 with the probe's boundary, **0.623 with the contiguous
  prefix on the same rays** (GC2621's replay: 12,362 and 17,867 black of 28,673). **The density is a convention artefact, not a
  property of the crystal's edge:** a ray advances two wheels per tick while the boundary is nondecreasing, so a first exit lands
  one or two wheels beyond the boundary; the offset-one exits are 50% black under either boundary (8,101 of 16,127; 8,030 of
  16,022) and the offset-two stratum carries the whole bias and flips with the convention (34% against 78%). My "new unexplained
  observable" is withdrawn. Maximum |autocorrelation| over lags 1 … 64 is 0.062 (noise 0.012) under the probe's boundary, to be
  re-read under the contiguous one. **P-D1 REFUTED on the windows tested:** no period at or below a quarter of each window
  ([10, 42), [42, 598), [598, 4,096), [4,096, 32,768), lags through 4,096); that is a finite exclusion, not aperiodicity. The
  telescoping shows why the prediction's mechanism was wrong: Σ is one cell per ray along the moving boundary, not a growing sum of
  periodic terms.
- **P-D2 VOID (GC2621):** with C = cell ⊕ Σ the zero-lag sign product is identically (2Σ − 1)(2C − 1) = 1 − 2·cell, so the
  reported 0.0185 is the largest departure of a column's black fraction from one half on the window and says nothing about Σ;
  any transect would give the same numbers. The test I wrote could not detect what it was written to detect. The per-column
  content is the column's own lag-P behaviour: for a nominated P, the two lag-P differences C_x(t + P) ⊕ C_x(t) and
  Σ(t + P − x) ⊕ Σ(t − x) must agree at every t, and a differing pair is an exact witness against P; counting and localizing them
  is the right test, not run.
- **P-D3 HELD (control):** no column has a period ≤ 4,096 on the window [4,096, 32,768]; a finite-window statement.

**What it teaches.** (1) The wall reaches every column through one sequence along the rays, the first-exit transect Σ, the same for all columns up to
delay, with the core adding a parity over the last fifth of the ray; on the windows tested Σ has no period through lag 4,096, and
its density is a sampling convention, not a signal. (2) A periodic column x would need C_x(t) = Σ(t − x) ⊕ p(t)
with p periodic: the core's OR-parity along the ray would have to reproduce the crystal's transect exactly up to a periodic word.
That is the general claim in one line, per column, and it is where a proof would have to work. (3) Forgetting makes the left
crystal grow at 0.74 t; remembering keeps the right completed zone logarithmic. Not claimed: any asymptotic law, any aperiodicity beyond the windows, any dependence between the core and the transect (the
test was void), anything about Problems 1 to 3. GC2621 carried the identity, replayed both frontiers (slopes equal to five
decimals) and the exit counts on the same rays, and found the stratification; adopted in CL716.

## 19. The news frame: the band edge's dynamics as a transducer, the step's determination horizon, and a stationary three-wheel boundary (T-c, CL718–CL719, 2026-11-04 12:57 GMT)

**GPT follow-up, GC2624.** The 54 and 5 collisions are visits across nine and four ambiguous keys. Width parameter seven is already consistent on this sample. Bias in the two halves is an empirical sensitivity check. The held-out tests and stall/heal strata are in the [follow-up review](GPT-CL721-CROSSING-REVIEW-20261104.md).

**GPT follow-up, GC2635.** All twenty fixed shifts have permanent agreement through the moving lag edge after their last listed disagreement. On the same 20,060 visits, uniformizing the entry phase at each visited parent changes the immediate-heal rate from 0.26675 to 0.50313. For arbitrary higher bits, fixing the original seed’s low 39,089 bits suffices through wheel 87,867 at tick 122,880 and thereafter. The two observed cells at 60,549–60,550 identify the future branch under the aligned prefix-return guard. [Kernel theorems, numerical hypotheses and exact scopes](GPT-WHITE-PARENT-OBSTRUCTION-20261104.md)


**The frame.** The atlas grid's row v = −0.246, "nobody has written the dynamics in this frame". Written now from exact pieces:
the state is the pair of rows (t, t + 16) on wheels around the lag-16 band edge B(t) (CL692's object; on the certified prefix
B(t) − 1 is the contiguous least-period settling frontier, GC2621, confirmed here at 24,577 of 24,577 ticks); one tick is a shift
by Δ_t = B(t + 1) − B(t) followed by the rule (GC2602's equation Z_(t+1)(h) = Z_t(h + Δ − 2) ⊕ (Z_t(h + Δ − 1) ∨ Z_t(h + Δ))); Δ_t is 0
iff the decider wheel B − 1 is white at t (the mask law, CL692 H1a, 0 violations here), else the jump set by the pattern above (CL692
H1d); and cells enter from the deep side every tick. So the frame's dynamics is a **transducer**: a finite window driven by an
incoming stream, never a closed automaton (GC2602). PROVED as a restatement of exact facts; nothing new is asserted in it.

**Run.** `news_frame.py 65536`: the left-frame system as a big integer to T = 65,536; trusted window t ∈ [8,192, 32,768], every wheel
used inside the prefix certified 16-periodic (wheels 0 … 42,899 agree at T − W and T − W + 16, the autonomous prefix propagating the
equality for ever); 14 s on this host under the agreed substitute (ulimit 8 GiB, timeout 1,800 s).

**The step law (controls against §8.74 and §8.66, all HELD).** Mean Δ = 0.7449 (CL715's 0.744 on the same window; §8.74's 0.755 on
[2^16, 2^19], within its diffusive wander); P(heal) = 0.4097, E[jump | heal] = 1.818, product 0.7449 = the mean exactly, against
§8.66's fair-row factors 0.410 × 1.839: the band edge's heal statistics are the fair-row damage front's. Distribution of Δ over
24,577 ticks: 0 at 59.0%, 1 at 15.1%, 2 at 21.8%, 3 at 2.1%, 4 at 1.0%, 5 at 0.8%, 6 … 12 at 0.2% together; jumps of 2 outnumber jumps of
1; the largest is 12 (§8.74: never more than 14).

**C2, the determination horizon (GC2602's collision test).** State = (decider bit; rows t and t + 16 on wheels B … B + w); a
collision is a repeated state with a different Δ.

| w | 0 | 1 | 2 | 4 | 6 | 8 | 10 | 14 | 18 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| distinct states | 4 | 16 | 64 | 972 | 8,591 | 21,103 | 24,210 | 24,574 | 24,577 |
| collisions | 5,581 | 1,384 | 781 | 54 | 5 | 0 | 0 | 0 | 0 |

The 54 collisions at w = 4 and the 5 at w = 6 are exact witnesses that the step reads beyond six wheels; from w = 8 every one of
the 3,474 repeated states is consistent. **Prediction C2 half refuted:** collisions were to persist through w = 8 and vanish by 16;
they vanish at 8. Absence of collisions is consistency on finite data, not closure: at w ≥ 18 every tick is its own state, and the
five jumps longer than 8 all sit in states that never repeat.

**C3–C6, the boundary layer (HELD).** The mismatch density ρ(h) = P(row_t ⊕ row_(t+16) = 1 at wheel B + h): ρ(0) = 1 by definition,
**ρ(1) = 0.458, ρ(2) = 0.580**, then within 0.02 of the bulk from h = 3 on; bulk (h = 32 … 64) 0.5003; the two halves of the window
agree within 0.0143 at every h ≤ 32. The row's own black density across the frontier is 0.50 everywhere except a **dipole at the
edge: 0.41 at h = −1 (the decider; CL692's 0.404), 0.50 at h = 0, 0.59 at h = 1**; the settled side averages 0.494, the news side
0.500. So in its own frame the order/disorder boundary is a stationary structure two wheels thick, a dipole in the row's density
and in the mismatch density, riding at the news speed on a decider gate that is black 41% of the time.

**Reading, PROOF-SKETCH.** The decider's 0.41 is §8.66's selection effect in a new place: the edge waits while the decider is
white and leaves when it is black, so the decider is sampled white-rich; P(heal) is that density by the mask law, 0.410. The
enrichment at h = 1 (0.59 black, mismatch 0.58 at h = 2) is the heal-size structure of H1d (patterns with a black at B + 1 heal by
exactly 2); not derived here. What is new: the transducer statement, the horizon table with its exact witnesses, and the
stationary profile with its thickness. Not claimed: closure, a Markov structure of Δ, or any asymptotic statement.

**Next, if wanted:** the entropy rate of the step process Δ_t and its memory (H(Δ_t | Δ_(t−1), …)), and the stationary measure on
the eight-wheel window: the quantitative "what is stationary there"; and the same frame for a random left-finite row (CL696's
sixty rows), to see whether the dipole is universal.

## 20. The step process and the one walk: entropy ladder, heal clock, universality of the band edge's walk across left-finite rows, the merge of orbits, and the row 101 (CL720–CL721, 2026-11-04)

**GPT follow-up, GC2624.** A four-row XOR gives the last-crossing rule. The ordinary sample splits into eight overtakes during seed-edge stalls and nine jumps from an equal starting wheel, at six exact ticks. The fixed lag eventually saturates. Proposition 20 already proves the 101 shapes and checkerboard fringe family. [Full proof, controls and pointwise converse counterexample](GPT-CL721-CROSSING-REVIEW-20261104.md)


*Cloud, 2026-11-04, after §19. Probes `step_entropy.py`, `news_frame_rows.py`, `walk_align.py`, `walk_merge.py`,
`seed101_cone.py` (substitute caps ulimit 8 GiB, timeout 1,800 s, this Linux host). Predictions P-F1 … P-F8 in CL720, its
addendum and CL721, each written and pushed before its run. Statuses as labelled; nothing here is a theorem beyond the one-line
restatements marked so.*

**Frame and two restatements (PROVED, §8.31/§8.74 restated).** Wall frame: bit j of row t is the cell x = j − t, bit 0 the left
edge; bit j at tick t + 1 reads bits j − 2, j − 1, j at tick t. Hence (i) two configurations agreeing on bits 0 … J at one tick
agree there at every later tick, and (ii) the lag-16 band edge B(t) = the lowest bit where rows t and t + 16 differ never
retreats. The settled band is the universal strip's cycles (§8.31, CL695); its edge is the settling front of §19.

**20.1 The step process of the single seed (`step_entropy.py 17`; trusted window [16,384, 65,536], 49,153 ticks, certified
16-periodic prefix to wheel 87,866, where the strip's period doubles; at T = 2^18 the edge passed that wheel and the assertion
stopped the run).** Steps 0 / 1 / 2 at 59.2% / 14.8% / 21.7%, mean 0.7474; mask law 0 violations.

| quantity | value (bits) | halves | plug-in bias gauge |
|---|---|---|---|
| H₀ = H(Δ) | 1.6053 | | |
| H₁ = H(Δ_t \| last 1) | 1.2981 | 1.2968, 1.2975 | +0.0010 |
| H₂ (last 2) | 1.2264 | 1.2231, 1.2251 | +0.0024 |
| H₃ (last 3) | 1.1952 | 1.1906, 1.1910 | +0.0044 |
| H₄ (last 4) | 1.1755 | 1.1683, 1.1685 | +0.0072 |

P-F1 HELD. P-F2's first two clauses HELD and its third REFUTED: H₄ = H₂ − 0.051 against a gauge of 0.007; the decrements
0.307, 0.072, 0.031, 0.020 shrink but have not reached the gauge at k = 4. The step process remembers beyond two ticks
(COMPUTED). Waiting times between heals: mean 2.450 = 1/P(heal); hazard h(1) = 0.267, h(2) = 0.518, h(3 … 7) = 0.49 … 0.50
(n from 7,091 to 463), h(8) = 0.455 on 233: one refractory tick, then a hazard near one half (P-F3 HELD, COMPUTED). *Corrected reading (CL722, from GC2635):* every one of the 20,060 waits is determined by the phase word of the new parent (one plus the whites before its next black); the hazard near one half is the parents' black density under the visit mixture, not a coin, and the refractory tick is CL691/GC521's forced stall after a two-wheel jump. The smallest consistent width of the step is w = 7, eight cells from B plus the decider (GC2624), not eight.
The mismatch pattern M on wheels B … B + 4 (16 states, bit 0 always set, entropy 3.94 bits): H(M′ | M) = 3.346,
H(M′ | M, M_prev) = 2.330, Markov gap 1.016 bits (P-F4 REFUTED): the pattern is a lossy projection; the pair of rows
(t, t + 16) around the edge is the state (reading, CONJECTURE, consistent with P-F2's refutation and §19's horizon of eight).

**20.2 Universality on twenty random left-finite rows (`news_frame_rows.py 20 16`; CL696's construction, rng 606, widths
2 … 62, each on [8,192, 32,768], certified prefix checked on every row).** P-F5, P-F6 HELD far inside tolerance: mean step
0.7447 … 0.7455 (seed 0.7449), P(heal) 0.4096 … 0.4099, E[jump | heal] 1.817 … 1.819, ρ(1) 0.4577 … 0.4579, ρ(2)
0.5805 … 0.5813, densities 0.410 / 0.500 / 0.593 at h = −1, 0, 1 on every row; B(32,768) from 24,444 to 24,564 (seed 24,465).
Explained by 20.3: the same walk read on windows displaced by at most 148 ticks.

**20.3 The one walk (P-F7, `walk_align.py 20 16`; COMPUTED).** For every one of the twenty rows there is a time shift
s ∈ [−148, 24] at which the step sequences agree on 100% of the window and B_row(t + s) − B_seed(t) = 0 at every tick (not
merely constant). Every left-finite row's settling-time sequence τ_k is the seed's plus one constant, exactly, over wheels about
6,100 … 24,465 (18,000 wheels, twenty rows, no exception). Prior art in the record: CL695's corollary up to phase (the eventual
cycles of every left-finite row below the first even-weight white wheel are the universal strip's up to a time shift;
PROOF-SKETCH) and CL696's synchronisation (τ_k mod 16 agrees with the seed's beyond wheel 3,498 on 60 rows); §8.36–8.38's merges
of lead 1's forced walks. New here: the agreement is of the whole sequence with one constant and includes the front itself.

**20.4 The merge of orbits (P-F8, `walk_merge.py 20 16`; COMPUTED).** With s from 20.3, let J(t) be the lowest bit where the
seed's row t and the row's row t + s differ (the merge front).
- (a) J(t) > B_seed(t) at every tick of the window on every row (least margin 3), and on all eighteen rows that differ from the
  seed, the last tick with J ≤ B_seed is the last tick with B_row(t + s) ≠ B_seed(t). *Corrected (CL722):* this is the last-time identity of GC2624's four-row rule, PROVED; "never before" was wrong, equal edges at a single tick can coexist with a difference below them (seed 1 against row 7 at tick 2). The one walk is one orbit on the settled band, the edge and a margin beyond. All twenty crossings are final for all time (GPT's certificate, GC2635).
- (b) The margin J − B_seed drifts: the merge front moves at 0.7538 wheel per tick (0.7496 … 0.7596), the lag-16 edge at 0.7435,
  difference 0.0104 (0.0061 … 0.0162); half-window means 87 … 244 then 225 … 390. The merge front's speed is §8.74's lag-1,024
  figure 0.755 (one minus the news speed 0.2437); the lag-16 settling front is slower on this window and rises with t (0.7449
  on [8,192, 32,768]; 0.7474 on [16,384, 65,536]). *Corrected reading (CL722):* for a fixed lag of 16 the edge saturates at K = 87,867, the first wheel whose eventual period does not divide 16 (GC736; B(t) = K from tick 117,324 on, CL722), so the lag-16 asymptotic speed is zero and the 0.0104 gap is a pre-saturation, finite-window comparison that does not decide drift against √t; the observable with a limit is a growing-lag or least-period frontier (§8.74, §18).
- (c) The transient ends at one of four universal events: last discrepancy at tick 2,646 (one row), 3,309 … 3,323 (eight),
  5,389 (four), 5,917 (four), that is at the seed's wheels 2,021, 2,548 … 2,556, 4,093, 4,481. The discrepant offsets
  B_row − B_seed before the end are runs of consecutive values (−21 … −14, −64 … −57, −127 … −120): the row's edge trails
  the seed's by a gap that closes slowly and then at once. What the four events are in the strip is open. No conflict with
  CL696's wheel 3,498 (CL722): its run ended at wheel 3,999, a horizontal offset is not a phase mod 16, and the printed offsets were sorted values, not a history.

**20.5 The row 101 (`seed101_cone.py 15`; COMPUTED to 32,768 ticks). Known: this is the r = 2 case of Proposition 20 (PROOFS §33, 9 October, PROVED hand/two-party, GC641), the invisible checkerboard fringe, which covers 11, 101, 1011, 10101 and the whole alternating family; PRIOR-ART entry by GPT (GC2624); the sketch below is a wall-frame rederivation (CL722).** The row with cells 0 and 2 has the seed's
orbit on every cell left of the seed's right edge at every tick t ≥ 0, with J(t) − 2t ∈ {0, 2} alternating. Shapes: at even t
the row is the seed's row S_t with bits 2t + 1, 2t + 2 = 0, 1; at odd t it is S_t with bit 2t cleared and bits 2t + 1, 2t + 2 = 1, 1.
*Sketch.* Even t: bits ≤ 2t + 1 of the next rows read bits ≤ 2t + 1, equal in both (bit 2t + 1 is 0 in both); bit 2t + 2 becomes
1 ⊕ (0 ∨ 1) = 0 against the seed's 1, bits 2t + 3, 2t + 4 become 1, 1: the odd shape. Odd t: bits ≤ 2t − 1 agree; bit 2t reads
(V_(2t−2), V_(2t−1), V_(2t)) with V_(2t) = 0 against the seed's 1, and the OR masks the difference iff V_(2t−1) = R₁(t) = 1, which
holds at odd t since R₁(t) = t mod 2 (the kit's ruler at the first right diagonal; checked to 2^15); bits 2t + 1 … 2t + 3 then
agree (0, 1, 0 in both) and bit 2t + 4 is 1 against 0: the even shape. ∎ (The ruler step is the one to read.) Two finite rows that
are one object with different edges: the owner's transmutation in miniature.

**What is claimed.** The measurements, the identities of 20.3–20.4(a) on twenty rows, the shapes of 20.5. Not claimed: any
asymptotic statement, the mechanism of the four events, or that every left-finite row's transient is an edge decoration moving in (the
speed-gap reading is withdrawn, 20.4(b)).

**Next, if wanted.** Identify the four events in the strip (CL695's reset law at a black the cascade cannot defer?). (The 101
family is Proposition 20; the lag-16 speed question is void by saturation; both struck in CL722.)

**20.6 The completion test (CL722, from GC2635's handoff; `white_parent_witness.py`; COMPUTED on 43 completions, this host).**
Setting: K = 87,867 (the first wheel whose eventual period is 32), T = 122,880; the prefix 0 … K evolves on its own. GPT's guard
(`reset_path`, PROVED; the path COMPUTED): every row agreeing with the seed on bits 0 … 39,088 agrees through K at T and forever;
with bits 0 … 39,087 only, through K − 1, the bit at K then pinned forever either way since K − 1 is white from T. Question:
does any completion of the 39,088-bit prefix show the opposite colour at K at T? Race criterion (PROVED from `heals_iff` and
autonomy): a flip needs the merge front to pass K − 1 for good only after τ, the seed's last black at K − 1 before T. Replayed
seed facts: B(T) = K, the two lag-16 hits at K, the lag-32 return, t_K = 117,324, τ = 117,323. Results: no flip on the
two-black-cell seed 1 + 2^39088 (t₁ = 84,061), on fifteen single-bit completions (t₁ from 83,472 at j = 39,089 down to 43,934 at
j = 87,866 and 0 at j = K), on twenty random completions with bit 39,088 = 1 and two structured ones (t₁ ∈ {84,033; 84,061;
84,065}), and the five controls with bit 39,088 = 0 agree through K (the guard replayed). The margin against a witness is
33,000 ticks of merge-front travel. Not predicted: the final passage of K − 1 takes only six seed-set ticks over the 27
completions free from bit 39,088, CL721's universal moments at a second wheel. Open: the existential question (a lower bound on
the merge front's speed beyond one-wheel transport would close it); which strip resets set the moments.

**Closed and explained (CL723, from GC2647).** The completion question is closed: GPT's two-update rule (a common suffix 010
forces two more wheels in two updates, `double010`, PROVED) gives agreement through 87,867 by tick 105,136 for every completion
of the 39,088-bit prefix, 12,190 ticks before the last black at 87,866; 29,329 bits suffice by 116,977 (minima for that path
rule, not physical bounds). The six passage ticks are the incoming packet's pre-contact phase at its gap (four values by phase
mod 8 at gap 39,088; the other two at gaps 39,089 and 40,000), certified by a transfer at the tick before the passage. The
destination's clock is the parent's actual trace, not its eventual word (the eventual word misses 1,701 of 2,266 resets on the
last 129 wheels), so "set by the seed's resets at the parent" holds with the actual trace. The half-cycle reduction is
geometric: phases r and r + 8 merge at gap 39,088 and separate at 39,089 (tick 39,837).


### 20.7 GPT follow-up on the passage clock and arbitrary completions (GC2647, 4 November 2026)

At gap 39,088 the right packet's phase at tick 19,543 predicts the passage through wheel 87,866. The 16 canonical phases give 83,769 / 84,033 / 84,061 / 84,065; three incoming probe bits select them under a verified deeper matching guard. All 23 rows starting at that gap pass the transfer, including both structured controls. With the measured geometry the other 20 named cases also follow (one at time zero). The eventual phase word of the *left* seed’s parent is white at all six actual late resets in the 32-row near-gap cohort. A half-cycle difference stays at least 11 wheels ahead at gap 39,088. At 39,089, phases 0 and 8 first give different front positions at tick 39,837. A common 010 suffix also closes §20.6’s open completion question: all higher tails over the original 39,088 fixed bits match through 87,867 by 105,136. A 29,329-bit sufficient guard is certified by a separate path. [Complete result, precise scopes, certificates and CL721 comparison](GPT-CL722-PASSAGE-PHASE-20261104.md)

## 21. The forced front: the kit's settling recursion on the universal strip bounds every configuration's transient; the actual front is that plus the coincidences (CL730, 2026-11-04)

*Cloud, after the universal-left-side theorem (R30-20261104-309041). Probe `settling_bounds.py`; predictions in CL730.*

**Setting (PROVED in the kit for the seed, COROLLARY for every configuration, PROOF-SKETCH until read).** The kit's
`Rule30FrontLaw.frontBound` is CL695's cascade recursion: wheel j + 2 is in its cycle from one tick after the first black of
wheel j + 1 at or after the time both parents are, or from that time when wheel j + 1 is white. Run on the universal strip at
phase s it gives F_s(j); by the universal-left-side induction with the time carried, every configuration with a leftmost
black cell carries the strip on wheel j from F_s(j) at its own phase s (PROOFS waiting room, CL730). The phase-free bound
U(j) = max_s F_s(j).

**Numbers (COMPUTED).** F_0(53,207) = 107,310; U(53,207) = 107,312 (the sixteen phases differ by at most 7 ticks at any
wheel); the kit-style linear bound 1 + 16 j = 851,313. The forced front's increment over the last 40,000 wheels is 2.0154 ticks
per wheel (speed 0.4962); the actual seed front's is 1.3370 (speed 0.7479, τ(53,207) = 71,116). τ_k ≤ F_0(k) at every wheel;
the recursion's lag reaches 36,195 ticks at wheel 53,202. Five random rows: phases read exactly, no violation, the same
increment 1.3370 and the same τ(53,207) within 92 ticks, the one walk of §20 in the settling times.

**The coincidences (COMPUTED, the statistic chosen after the first run, labelled).** With the actual parents' settling times,
G_k = 1 + the first black of C_(k−1) at or after max(τ_(k−2), τ_(k−1)); local violations 0 on 53,206 wheels; local
coincidences τ_k < G_k on 45.50% of wheels; slack G_k − τ_k of mean 0.9115, distribution 0: 54.5%, 1: 21.8%, 2: 12.6%,
3: 5.5%, 4: 2.8%, near a geometric law of ratio one half; identical on the five rows (0.4550 … 0.4555). A cumulative
comparison with F_0 is ill-posed (100% once the actual front is ahead) and was the statistic of the refuted prediction P-S2.

**Reading (CONJECTURE).** The settling front of every configuration is the forced front at one half, which is what binomially
fair strip words give (increment one plus a geometric wait of mean one; CL680's P-J3), plus the news: 45.5% of wheels are
already in their cycle when the forced reset would arrive. The actual 0.748 is the record's 4/3 ticks per wheel (CL717). The
share 0.455 is close to the boundary density ρ(1) = 0.458 of §19; whether it is that number is open.

**What is claimed.** The corollary (PROOF-SKETCH), the values of the kit's recursion on the strip, the local statistics on six
rows. Not claimed: an asymptotic law, anything beyond the cut, or the identification 0.455 = ρ(1).

**Next, if wanted.** The number 107,312 as a kernel theorem (the recursion evaluated on the sixteen rows, Local's certificate
layer); the same recursion on Local's four strips through 87,866; the coincidence share against ρ(1) on a longer window.

**21.1 The four strips and the long range (CL733; COMPUTED).** The same recursion on L1513's four strips through wheel
87,866, all sixteen phases: F_0(87,866) = 176,968 (A0), 177,229 (A1), 177,170 (B0), 177,560 (B1), phase spreads 15, forced
increments 2.01 … 2.03 ticks per wheel; so **177,562 ticks** bounds the transient of every configuration with a leftmost black
cell through 87,866, on whichever strip it is (corollary of L1513's classification with the time carried; the linear bound
at period 16, 1 + 16 · 87,866 = 1,405,857, about eight times the front: corrected in CL735 from "2,811,713, sixteen times", which had counted the forks as doublings of the period). The seed reaches 87,866 at 117,324 with no violation. The coincidence share holds beyond
the cut (0.452 on wheels 53,208 … 87,866; 0.454 on all 87,865 wheels, s.e. 0.0017), while ρ(1) on the matching long range is
0.462 (s.e. 0.0015): two quantities, 0.008 apart, not one. The four strips' white wheels below 87,867 as L1513 lists them.

**21.2 The bound as a kernel theorem (CL733 part C; PROVED, Lean kernel on Cloud's host, Local's build of record pending).**
Two Lean modules on kit main 2b62338 (`cloud-Rule30ForcedFrontCore.lean`, `cloud-Rule30ForcedFront.lean` in the
universal-left-side package) state the phase-0 front recursion F on the strip as a state machine on the pair (F j, F (j + 1)),
evaluate it by `decide +kernel` in eleven chunks of at most 5,000 wheels (the sixteen cycle rows as literals, each checked
against `rowAt 53209 B r`), and carry the time through the universal-left-side induction (`aligned_from`: `child_same` at a
black parent, `child_white` with `strip_shift` at a white one). Headlines, all passing the kit's `Check` with the standard
axioms: `forced_front` (some s ≤ 15 with a j (t + s) = C j t for j ≤ 53,207 and t ≥ F j, for every array with the recurrence
and a black start), `forced_front_uniform` (t ≥ 107,310; `F_53207 : F 53207 = 107310`), `forced_front_left_side` (every
configuration with a leftmost black cell) and `forced_front_seed`. So every such configuration is on the strip through
53,207 from tick 107,325 of its own clock at the latest: §21's 107,312 is the per-phase recursion's number, the theorem's
107,310 + s the phase-0 recursion's with the phase as the shift. Two facts of the kernel for the next such module: tactics
touching the 53,209-bit literals time out in the elaborator, so the word lemmas are stated with sixteen Bool variables and
instantiated after; and letting the kernel unfold the recursion at 53,207 in one step overflows its stack ("deep recursion
detected"), which forces the chunking. Core module 124 s and 2.7 GB; proof module 3 s.

**21.3 The four-strip bound as a kernel theorem (CL734; PROVED, Lean kernel on Cloud's host, Local's build of record
pending).** Six modules on kit main 8cf1bd4 (`cloud-Rule30FourFrontsBase.lean`, `cloud-Rule30FourFronts.lean` in the
four-fronts package; the four kernel modules in the shared store, `cited/four-fronts/`, regenerated by
`four_fronts_gen.py`). The settling recursion as a state machine over a word function, L1513's two moves with the time
carried (`step_black`, `step_white`, `white_shift`, `white_fork`, `extend_from`), the fronts carried across a fork by
`F_congr` (the strips agree below the fork, so do their fronts), and each strip's sixteen rows as literals with eighteen
block equations by `decide +kernel`. Headlines, all passing the kit's `Check` with the standard axioms: `forced_front_four`
(some s ≤ 15 and a strip v with a j (t + s) = Sp v j t for j ≤ 87,866 and t ≥ F_v j), `forced_front_four_uniform`
(t ≥ 177,560; the fronts at 87,866 are 176,968, 177,229, 177,170, 177,560), `forced_front_four_left_side` (every
configuration with a leftmost black cell), `forced_front_four_seed`, and `classification_bounded` (L1513's classification
with s ≤ 15). So every such configuration is on its strip through 87,866 from tick 177,575 of its own clock at the latest;
§21.1's 177,562 is the per-phase number. Kernel work: 317–356 s and 5.8–6.3 GB per strip on four cores, one Lean thread.

**21.4 Five left sides through wheel 165,749, with their ticks (CL736; PROVED, Lean kernel on Cloud's host, Local's build of
record pending).** The tree of PROOFS Proposition 8 (computed) through its fourth branch node, as a theorem with the time
carried. On 165,750 wheels at period 32: the seed's strip A0 doubles its period at 87,867 (its white wheel 87,866 has a
farther word of odd parity; the complement of the child is the child's rotation by 16, a shift the wheels below do not see);
A1 and B1 have no white wheel from 87,867 to 165,749; B0 forks at 165,748 (even parity), its second child B2 being B0 with
bit 165,749 complemented. Two modules (`cloud-Rule30FiveFrontsBase.lean`, generic in the width at period 32, with Local's
walk and `not_related` on per-wheel periods; `cloud-Rule30FiveFronts.lean`, five literals of 165,750 bits and the walk's
segments, generated by `five_fronts_gen.py`): `forced_front_five_left_side`, every configuration with a leftmost black cell
on one of the five strips through 165,749 from tick 334,150 + s of its own clock, s ≤ 31; `exactly_five_left_sides`
(realized by the five rows, pairwise unrelated); `odd_reaches_one_of_five`; the fronts at 165,749: 333,333, 333,257,
333,503 (B0 and B2), 334,150; the seed's own settling through 165,749 by tick 220,307 (COMPUTED). Fifteen names pass the
kit's `Check` with the standard axioms. With one kernel fact per black run the data module took 56 s and 8.3 GB (the
kernel's cache of the shifted rows); with the walk in blocks of 128 rounds (CL737) it builds in 29 s at 2.5 GB, within the
kit's limit.

**21.5 Sixteen left sides through wheel 894,235, with their ticks: Proposition 8 as a theorem (CL738; PROVED, Lean kernel on
Cloud's host, Local's build of record pending).** The period-16 stage of the rooted tree (PROOFS §21, Prop. 8, computed) realized
as rows on 894,236 wheels (`tree16_data.py`, 13 minutes): the fork wheels are its fifteen branch depths and the doubling
wheels its sixteen exits, nothing else; the fronts at 894,235 lie between 1,790,969 and 1,798,243 (2.006 ticks a wheel); the
single cell is settled by 1,180,062 (1.320). The generic generator `tree_gen.py` emits one kit-form module per strip and a
final module; all seventeen build on Cloud's host (strips 52–198 s, the final 327 s), and the final module's nine names pass
the kit's `Check` with the standard axioms: `forced_front_tree_left_side` (every configuration with a leftmost black cell on
one of the sixteen strips through 894,235 from tick 1,798,243 + s of its own clock, s ≤ 31), `exactly_left_sides`,
`odd_reaches_one`, `fronts`. Memory grows with the length of a strip's walk (14.2 GB on the root strip), retained across the
kernel facts within one module; splitting the long walks over several modules is the route to the kit's limit.

**21.6 The measured actual front through 894,235 and its exact local update (CL739; reviewed GC2680).** The single-cell finite-window slopes are 1.3326, 1.3272, 1.3188, 1.3180, 1.3113, 1.3189, 1.3176, 1.3163 and 1.3155. The post-100,000 windows lie below 4/3; their first-to-last drift is −0.0117, so P-C1 passed its range condition and missed its 0.01 trend condition. These finite observations do not settle B2’s asymptotic question, exclude a limiting 4/3, or prove configuration-independent speed. The fifteen tested fork perturbations have similar slopes, 1.315–1.331. A periodic strip row itself starts settled on the observed prefix.

The probe’s `tau` is the upper time in the comparison `x(t) = x(t−32)`. At the endpoint, 1,180,062 is the last unequal upper tick, 1,180,063 the first equal one, and **1,180,031 the corresponding entry into the periodic orbit**. The finite prefix evolves autonomously, so its first 32-step return certifies entry 32 ticks earlier. Subtracting 32 preserves the measured window slopes and, above the detector’s startup floor, its increments and phases modulo 32. The absolute gap from the forced 1,792,687 is therefore **612,656**. The preceding §21.5 value 1,180,062 remains a safe upper bound on entry, but is not its exact onset.

The five sampled doublings have zero detector increment; this refutes the proposed immediate extra jump at those wheels, not every possible asymptotic role of doubling. The output records 894,234 tested wheels, zero negative slack, coincidence share 0.4565, mean slack 0.9146, and gap growth 0.6858 ticks a wheel. Zero increment and positive slack have the same displayed proportion; white-parent wheels prevent treating them as identical events everywhere.

**Carried hand step (PROVED two-party, CL739/GC2680).** With a fixed final strip and phase, once both parents align, the child error satisfies `d_k(t+1) = d_k(t) AND NOT C_(k−1)(t)`. Thus its prefix-arrival increment is zero if it already agrees at the parent-prefix arrival, otherwise one plus the wait to the next black parent. A permanently white parent has no such waiting time: eventual alignment to the selected branch forces zero error already at arrival. The full strip-driven error recurrence in CL739 is an exact Boolean identity; a universal limiting extinction speed is conjectural.

The universal theorem’s exact spatial guard is **`F_v(j) + s <= t`**, or `max_v F_v(j) + 31 <= t` without knowing the strip and phase, through wheel 894,235. CL739’s exact half-speed wedge does not follow from it: the maximum endpoint front 1,798,243 exceeds `2 * 894235`. The classification and its stated finite deadlines remain intact. [Full review](GPT-MORNING-REVIEW-20261105.md).
