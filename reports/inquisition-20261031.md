# Inquisition round with the owner, 31 October 2026 (Local)

The owner asked for a summary, the places we are stuck and questions to unpick, in plain words. Local's questions were
sent at about 13:00 GMT. The owner answered all eight, added three remarks, and set the direction:

> Take what you can from my answers, follow warm pulls into testable hypothesis, predictions, and hand worked
> equations. These are many answers of many domains at once - record the tracking for each where appropriate so we
> don't lose one question / answer in a deep dive from another.

On the rhythm question the owner chose depth over harvesting partial results: "Let us sit in the discomfort of the
unknown." A long stretch with nothing to submit is acceptable.

The round summary of both rounds is at [the end](#round-summary-both-rounds); the handover to GPT is
[reports/HANDOVER-GPT-20261031.md](HANDOVER-GPT-20261031.md).

Each thread below is a deep question, DQ-026 to DQ-034 in [DEEP-QUESTIONS.md](../DEEP-QUESTIONS.md), which points
back here. Every thread has the owner's answer verbatim, what Local takes from it, its hand equations, and a test with
its prediction written before the run. GPT is halted, so every new hand step here is a solo PROOF-SKETCH unless the
record already proves it.

Status key: PROVED (in the record or standard), PROOF-SKETCH (Local solo), COMPUTED, CONJECTURE, KNOWN (prior art),
PARKED (specified, not run, waiting on a steer or a cheaper route).

## The tracker

| DQ | Thread | The owner's pull | First test | State |
|---|---|---|---|---|
| 026 | OR or AND: which colour is lumped | Turing's bombe: chained machines cancel the unknown middle | none run; a bombe reading of Q01 | read; loops test PARKED |
| 027 | Doors: starved or flooded | constructive and destructive interference; Fourier | T-A, the death kinds | COMPUTED: a fair coin, exactly before the news (PROOF-SKETCH) |
| 028 | Can the edge get three ahead | what makes 2 a wall; push the computation further | T-D, stage-one tightness | PARKED (specified) |
| 029 | Where is the randomness made | forgetting gates mix the next seed | T-E, the diagonal tables | COMPUTED; the left forgets itself, the right remembers itself |
| 030 | Multiplication or simulation | diagonals are walls; a period-2 centre is a wall that connects | T-E, the reading ages | COMPUTED: the crystal covers the centre to about t = 20, then falls behind |
| 031 | A measure that can grow back | spawning ratio of heads; are heads equal; rise and fall | T-F, T-P | COMPUTED: a fair cull, then real plateaus carried by the far bits; potential PARKED |
| 032 | Champions that don't nest | one map of many profiles (a radar) | T-G, the champions' radar | COMPUTED: no shared shape; never nested from W = 5 |
| 033 | Zoom out: rules along columns, diagonals or skipped cells | skew the stamp 00011110 onto diagonals or columns | T-S, T-S2, T-C | COMPUTED: left diagonals free (coordinates), right diagonal has a grammar; T-C known, reproved here |
| 034 | Every width at once is one infinite object | the seed's past is a periodic sea with a chink | T-H, T-H2, the sea census | COMPUTED: the checkerboard is the only home; champions do not imitate it |

## Corrections and confirmations from the owner's answers

**C1. The seed has two parents (owner right; my summary was wrong).** I wrote "every finite row has exactly one
finite ancestor". The record's statement is narrower:
- every finite row has **at most one** finite parent;
- so its finite past is one chain back to a **root** (a row with no finite parent), and its age is well defined;
- the single black cell is a root of age 0, and it has **exactly two parents, both infinite** (RECORD-MAP: "a single
  1 has no finite past, and exactly two parents", §8.19, PROVED).

The two parents, checked cell by cell against the rule (new = left XOR (centre OR right)):
- **A, the half wall:** black at every cell left of 0 (cells ≤ −1), white from 0 on. Cell 0 sees (1, 0, 0) and turns
  black; every other cell sees 111, 110 or 000 and is white.
- **B, the chinked wall:** black everywhere except a white cell at −1. Cell 0 sees (0, 1, 1) and turns black; cell −1
  sees (1, 0, 1) and turns white; everything else sees 111 or 110 and is white.

Why there are no others (standard, since the rule is left-permutive). Far to the right the child is white, so a
parent must satisfy x(j−1) = x(j) OR x(j+1) there. Read rightwards, that sequence never rises. A last black cell
followed by two whites would break the equation. So the parent's right tail is all white or all black, and then the
left side is forced cell by cell. One step further back the tree keeps branching: a child whose right tail is black
needs x(j−1) = NOR(x(j), x(j+1)), whose only infinite solutions are the three phases of 100100…, so it has three
parents (PROOF-SKETCH, Local solo). This is the "backward ocean" of the record (CL668 credits Quint's backward
cascade as prior art).

**C2. The crystal recedes at about a quarter of light speed, not a fifth.** The record (DQ-025, CL665): left
diagonal j settles at about 1.27 j to 1.33 j, so the settled band's front sits near −0.23 t and moves away from the
column at about a quarter of light speed.

**C3. "A period-2 centre column is a wall in its own right" is the record's own name for it.** The wall form (§8.39)
and the kit's `Rule30ZeroBoundary` both treat the alternating column as a wall and run Rule 30 on the left against
it. The owner's distinction between a wall that connects and one that does not is the record's split between
**Q01** (one-sided: the right neighbour column is left free, so the right side drops out) and **CQ01** (two-sided:
the right half must be real too). Q01 alone already excludes period 2 (`not_eventually_period_two_of_Q01`), so the
uncrossable version of the wall is enough for the prize's period-2 case.

## DQ-026 — Forgetful, but in which direction? (OR or AND, and the bombe)

**Owner:** "Here is an interesting (or not) thought. To conquer enigma, Turing used a trick of arranging the wheels of
different enigma machines one after the other as a way to cancel out the middle. Can we construct an odd sequence of
gates, let us say the OR gate, which starts and ends with the input and output we expect, but in the middle contains
some unknown fuzz ORin -> ? -> ? -> ORout. If we can, does the fuzz encode useful information. This is a very hazy
pull and might not make any sense - see if you can unpick it."

**The colour, first (PROVED, two lines).** Swap black and white everywhere. Rule 30 becomes Rule 135,
new = NOT(left XOR (centre AND right)). So "OR on a white sea" is the same machine as "AND on a black sea". What
matters is whether the gate's lumped class contains the sea's own pattern:
- OR keeps (white, white) on its own and lumps every case with a black in it. On a white sea the quiet passes
  through exactly, and any disturbance is heard.
- AND lumps every case with a white in it, including (white, white). On a white sea it is stuck at white. Rule 120
  (new = left XOR (centre AND right)) from one black cell is that cell sliding right forever; the centre column reads
  1, 0, 0, …
So for a single seed the colour decides everything. Record: `rule30_siblings.py` ran all sixteen siblings
l XOR g(c, r) on the wall problem (2026-10-04); CL652/CL654 found that Rule 120's right-edge map doubles at Rule 30's
density. So the colour matters at the seed but not at the right edge.

**The bombe, unpicked.** How the bombe worked. Encryption is plugboard, then rotors, then plugboard: c = S R S (p),
where S (the plugboard) is unknown and R (the rotors) is known for each trial setting. A crib (a guessed piece of
plaintext) gives letter pairs. When the pairs form a loop, a → b → c → a, S appears at both ends of every link and
cancels around the loop. That leaves a test of the rotor setting that does not depend on most of S. Two things made
it work:
1. the unknown entered as a **permutation** (it can be undone);
2. the crib had **loops**.

The Rule 30 version:
- **The crib** is the hypothesised clock: column 0 reads 0101… from some time on.
- **The plugboard** is the unknown right neighbour column. The left world can be undone because it enters by XOR, a
  permutation. That is the sideways reconstruction, and it is exactly Meier and Staffelbach's 1991 break of the
  Rule 30 cipher (PRIOR-ART.md).
- **The bombe's run** is our death search: it tries every setting (every start of width W) and stops at a
  contradiction (the death).

**What the fuzz is.** Under the clock crib, everything left of the wall is fixed by the free bits, one per two steps
(the kit's `Theta`, a bijection between constrained starts and free bits). So the fuzz is the start itself, bit for
bit. It encodes everything and compresses nothing.

**Where the analogy breaks, and why that teaches something.**
- **No loops in Q01.** In the one-sided problem every cell of the left world is derived exactly once, from the two
  cells to its right. The derivation is a tree. Nothing inside can contradict itself, and the only stop condition is
  at the far edge, where the left world must turn into the white sea. That is why every death we see is news
  arriving from the far edge (CL665).
- **Loops in CQ01.** Loops appear only in the two-sided problem, where column 1 must also come from a real right
  half.
- **Infinitely many settings.** The bombe had finitely many settings and we have infinitely many widths (DQ-034).

**Test, PARKED.** Count the loops (cells reached by two derivation paths) in CQ01 at small widths, and whether they
cancel the unknown right half the way the plugboard cancelled. I need a steer: is the owner's pull about loops (this),
or about a fixed middle stretch of gates whose ends are known?

## DQ-027 — Doors: starved or flooded? (interference, Fourier)

**Owner:** "sets me in mind of constructive / destructive interference. We essentially have a set of amplitudes which
could be normalized to plus or minus, or above base line zero. A Fourier transformation here could be useful to
extract the frequencies."

**Hand equations (PROOF-SKETCH, Local solo; machine-checked on every start by T-A).** The kit's normal form: the wall
is depth 0, the left world is depths 1, 2, … , rule 30 gives x_k(t+1) = x_(k+1)(t) XOR (x_k(t) OR x_(k−1)(t)), the wall
counts as white, and the clock lives while depth 1 is black at every even time. At an even time t, while alive
(x_1(t) = 1):
- x_1(t+1) = NOT x_2(t);
- x_2(t+1) = NOT x_3(t), because the OR with x_1(t) = 1 is 1;
- x_1(t+2) = x_2(t+1) XOR x_1(t+1).

So the clock survives the next tick exactly when **the two cells beside the wall differ at the odd time**, which is
exactly when **depths 2 and 3 differ at the even time before**. A death therefore has two kinds:
- **starved:** both cells white, (x_2, x_1) = (0, 0); no black arrives;
- **cancelled:** both black, (1, 1); two blacks meet in the XOR and cancel. This is the owner's destructive
  interference, literally.

The kind flips one step back: starved at t+1 means (x_3, x_2) = (1, 1) at t, and cancelled means (0, 0). So "starving
or flooding" is not a fixed property of a death. It depends on which step you read.

In the one-sided problem the right side never kills the clock. When the centre is white the door is open, and the
clock then needs the right neighbour to differ from the left. Since column 1 is free in Q01, it always can. Every Q01
death is of the left's making.

**The owner's ± picture is the Walsh–Fourier picture (PROVED, a computation).** Write black as −1 and white as +1.
XOR becomes multiplication. Rule 30's local rule is

  f(a, b, c) = (−a + ab + ac + abc) / 2,

four waves of equal weight 1/4 (a = left, b = centre, c = right). Rule 90 is the single wave ac and Rule 150 the single
wave abc. They pass one wave on unchanged and have no interference; Rule 30 splits every wave into four. Survival
beside the wall reads σ_2 σ_1 = −1 at every odd time: the two cells must stay in antiphase. A death is the pair coming
into phase, both white or both black.

**Test T-A: the death census.** Every start of width W ≤ 20 (supported on depths 1..W), the kit's convention.
Record searched: "death type|cause of death|death.*(starv|flood)" → no hit in the record, the kit, the portal or the
open PRs; "Fourier|Walsh" → used throughout the record (G23, G.GPT43), never for the death kind; D(2..24) from
`d1_engine.py`'s docstring as the control.
- P-A1 (control): D(2..20) = 6, 6, 6, 8, 10, 12, 12, 18, 18, 30, 30, 30, 32, 32, 32, 32, 32, 38, 38.
- P-A2 (hand law): at every death at an even time t ≥ 2, x_2 = x_1 at t − 1, and that pair is the complement of
  (x_3, x_2) at t − 2. Asserted on every start.
- P-A3 (the split): among deaths at t ≥ 2, starved and cancelled are each 40–60 % at every W ≥ 8.
- P-A4 (champions): the kinds of the champions' deaths are mixed across W = 8..20; neither kind wins at every width.
- Counterfactual: a split outside 30–70 % at large W, or one kind for every champion, would mark a mechanism and pick
  one picture.

Fourier proper is not tested here. A surviving window is at most about W samples, too short for a spectrum to mean
anything. The long signals (the centre column itself) already have the record's spectral and Walsh tests.

## DQ-028 — Can the edge get three ahead?

**Owner:** "what makes 2 ahead a seeming wall. Can we apply some optimized computation to push well beyond the 2000
steps tested - a counterexample would be illuminating, none would imply the same indescribable relationship as the
center column itself."

**What makes 2 a wall: two countdown timers in a row** (the last-visit argument of R30-20261031-9861e5, PROVED by
machine). Read the edge in pairs of layers. A pair is 11 (both layers double the period), 10 or 01 (one does) or 00
(neither). The excess (how far ahead of half pace we are) rises only at a 11.
- **Timer 1.** After the 11 that lifts the excess to 2, at pair K, the period is M = 2^(K+1) ≥ 8. The next layer
  starts with a "resource" of at least M − 2. The resource is how many differences you must take before the layer's
  pattern vanishes, a countdown that ticks at most one per pair. No further 11 can come until it reaches 0. That takes
  at least M − 1 pairs of type 01.
- **Timer 2.** After the last 01 pair, at index ℓ ≥ 9, the timer is reset to 2^(ℓ+2) − 1. Only 10 pairs can follow,
  each ticking at most one. So the final 11 needs N ≥ ℓ + 1 + 2^(ℓ+2) ≥ 9 + 1 + 2^11 = 2058.

Excess 2 is cheap: it is attained at its first chance, pair 3. Excess 3 needs the second timer, which is exponentially
longer than the first. Our hand sketch puts the next level near 2^2058 (T_(q+1) = A_q + 2^(A_q+q−1), not claimed).

**Why the computation cannot simply be pushed.** Nothing ran for 2000 steps. 2058 is a proved lower bound in pairs of
layers. At pair N the period is 2^(N+2) time steps, so one period at N = 2058 is 2^2060 steps, which no simulation can
run. The exact search reached 9 layers and the beam search 38 (19 pairs). A counterexample search has to be
**symbolic**: track the timers (difference orders), not the time series.

**Test T-D: stage-one tightness, PARKED (specified).** Can a designer run timer 1 at full speed, M − 1 consecutive 01
pairs each lowering the resource by exactly one, from K = 2 (M = 8, about 20 layers, simulable)? If yes, the first
timer of the bound is sharp. The question then shrinks to whether timer 2 can tick at every pair, which is a statement
about a few gates and can perhaps be proved by hand. Prediction, written now: stage one is tight at K = 2 (the designer
has 256 gate choices per pair). Record searched: `gate_clock_beam2.py` and reports/rule30-gate-clock-sharpness.md
(excess 2 attained at pair 3; no excess 3 to 38 layers); no stage-one record.

## DQ-029 — Where is the randomness made?

**Owner:** "the inherent property of the forgetting OR/AND gates, that cannot recover the input state with certainty
based on the output state (except 11 for AND has certain input, 00 for OR has certain input). Where the input is known,
the next seed is effectively fixed. Where the input is uncertain, the seed has effectively become random - it is no
longer a product of the previous inputs but a kind of average. Each forgetting mixes the seed of the next link in the
chain."

**What Local takes from it.** The OR forgets, but the XOR remembers. From (new, centre, right) you can always recover
the left. So Rule 30 destroys no information on the whole line (it is onto, and its rule is balanced); it moves
information leftwards. The real forgetting happens in the sideways direction: rebuilding leftwards, the right
neighbour is lost exactly at the times the centre is black (the door is shut).

**The diagonal frame makes the owner's idea exact.** Number the diagonals from each edge.
- Right diagonals: D_k(t) = x(t − k, t) and D_k(t+1) = **D_k(t)** XOR (D_(k−1)(t) OR D_(k−2)(t)). A right diagonal
  sees **itself through the XOR**. It remembers itself.
- Left diagonals: L_k(t) = x(−t + k, t) and L_k(t+1) = L_(k−2)(t) XOR (L_(k−1)(t) OR **L_k(t)**). A left diagonal
  sees **itself through the OR**. It forgets itself.

The consequences, both PROVED:
- **Right, an odometer.** The map on the first n right diagonals can be undone bit by bit from the edge inwards, so it
  is a permutation of a finite set and every right diagonal is periodic from time 0, with no transient. The periods
  are powers of 2 that double at most every other diagonal (the kit's half rate; our nested result).
- **Left, a crystal.** Every left diagonal k ≥ 2 settles after a transient, with period dividing 2^(k−2) (Jen 1986;
  the record's `JenPow2.lean`).

So the left forgets itself and crystallises; the right remembers itself and counts with ever longer periods. The
random-looking region is everything the two have not tamed yet:
- on the left, cells whose diagonal is still in its transient (right of the front near −0.23 t);
- on the right, diagonals whose period (about 2^(k/2)) is longer than the time elapsed, that is all but the last
  2 log2 t or so.

The centre column is diagonal t from both edges at time t: c(t) = D_t(t) = L_t(t).

**Test T-E: the diagonal tables.** Exact periods of the right diagonals (k ≤ 36), and settle times and periods of
the left diagonals (k ≤ 60), from the two recursions; direct simulation as the control. Record searched: "left
diagonal" → Jen's theorem PROVED (`JenPow2.lean`, L541, §8.27), settle times about 1.27–1.33 j (CL654, GC2266); right
periods via the kit's half-rate law; no table of the centre's reading positions.
- P-E1 (control): both recursions agree with direct Rule 30 for t < 64; c(t) = D_t(t) = L_t(t); D_3 reads 0011 with
  period 4, as the owner found.
- P-E2: every right diagonal is periodic from t = 0, periods powers of 2; D_4 has period 8.
- P-E3: left periods divide 2^(k−2); the settle time τ(k) > k for every k ≥ 3, so the centre always reads a left
  diagonal mid-transient; τ(k)/k lies in 1.2–1.4 for k ≥ 30.
- P-E4: the period of D_k exceeds k for every k ≥ 8, so the centre reads each right diagonal inside its first period.
- Counterfactual: a left diagonal settled by t = k, or a right diagonal of period at most k for large k, would put
  settled information under the centre.

## DQ-030 — Long multiplication or full simulation? (the diagonals and the walls)

**Owner:** "the right edge tends to be the more interesting edge and the diagonals have interesting properties. The
right most diagonal is period 0, a wall of 1. The next left diagonal is period 2. The next left diagonal from that is
period 2. The next left diagonal from that is 00110011. I am unsure if the next diagonal is periodic or not. All of
this falls out because the bounding diagonal wall of 1 on either side of the pyramid are the same hard wall as the
seed's past state of a horizontal row of 1 to infinity, only rotated 45 degrees. Period 1 walls are endemic to the
bounding edges of the problem space. Holding the center column to period 2 is therefore a wall in it's own right - the
puzzle is implicit that any periodic pattern is a kind of fixed wall, the difference with the center column being it is
a strange wall that connects what is left and right of it, not an uncross-able boundary."

**What Local takes from it.**
- **The diagonals.** The owner's diagonals are exactly our right-edge odometer: the gate-clock edge map is the
  diagonal recursion with g = OR. Every right diagonal is periodic (DQ-029), so the next one is too; T-E prints them.
- **The rotation, made exact (PROVED, one line).** The seed's half-wall past A is black on every cell left of 0. In
  the diagonal frame, at time −1, that is every right diagonal black. One step of the odometer from all-black gives
  (1, 0, 0, …), the seed: Φ(1, 1, 1, …) = (1, 1 ⊕ 1, 1 ⊕ 1, …). So the half wall lies on the right edge's own cycle,
  one tick before the seed. The horizontal wall and the diagonal wall are one object seen in two frames.
- **The connecting wall.** See C3: Q01 is the uncrossable wall and is already enough for period 2.
- **The shortcut question in this language.** Each fixed diagonal has a shortcut. A right diagonal is periodic, so
  D_k(t) needs only t mod its period; a left one is periodic after its transient. The centre needs diagonal k = t, a
  moving target, so no fixed-diagonal shortcut applies. A shortcut for c(t) would be a formula for D_k(t) uniform in
  both k and t, which is what Lucas's theorem gives Rule 90 (C(t, k) mod 2). T-E's tables are the first look.

## DQ-031 — A measure that can grow back (Hydra)

**Owner:** "questions that fall out, such as the spawning ratio of new heads per old heads cut off, are all heads
equal or are some more deleterious/profligate than others. Any rise and fall again a wave function worthy of further
study."

**What Local takes from it.** In the forward wall form nothing grows back: each start is one history. So the heads
are the surviving starts, and the spawning ratio is the fraction that survive each tick.
- **The halving line.** If each tick passes with chance 1/2, the survivors at even time t number about
  2^(W−1−t/2). That reaches one at t ≈ 2W − 2, which is the observed D(W) ≈ 2W. So the Hydra here is a dying
  population with a spawning ratio of 1/2 and no regrowth.
- **The known part.** The halving is exact to t = W (CL666's "early halving law").
- **The open part.** The stretch from W to D(W) is not covered by that law; the far edge's news arrives there.

**Test T-F: the survival ratio and unequal heads.** The same census as T-A. Record searched: "early halving" →
CL666; no survival curve past W in the record.
- P-F1 (control): survivors halve exactly at each tick for t ≤ W.
- P-F2: for W < t < D(W) the tick ratio stays within 0.4–0.6 while at least 16 survive.
- P-F3: the champions outlive the halving line t* = 2W − 2 by at most 8 steps at every W ≤ 20 (D(12) = 30 against
  22 is the known stretch).
- P-F4 (unequal heads): among starts alive at t = 4, the mean death time by near-wall pattern (depths 1–4) varies by
  at most 2 steps.
- Counterfactual: a ratio drifting from 1/2 after W, or a near-wall pattern that lives much longer, would mean
  profligate heads and something worth a potential.

The Hydra potential itself (a quantity that always falls, even while the pattern recovers) is PARKED. A candidate
needs T-F's curve first.

## DQ-032 — Champions that don't nest (the radar)

**Owner:** "one strategy would be convenient if true, however many strategies are one relationship map when regarded
as a whole. This is analogous to a StatsBomb Radar - each edge known is the defined quantity of some stat a champion
poses, each graph is unique per champion, but each champion having a graph at all is the unifying theory."

**Test T-G: a radar for every champion at W ≤ 20.** The spokes are:
- true width (deepest black cell);
- black density;
- number of black runs;
- longest white run;
- the near-wall four bits;
- the death kind (T-A);
- D − (2W − 2).

Record searched: "maximizers not nested" (widths 64–76) and CL666's relay reading of the three maximal-excess rows; no
small-width radar. The record's candidate unifying law is GC1772/GC1773's D(W) = W + the longest white run of a forced
row after W.
- P-G1: no single near-wall four-bit pattern is shared by the champions of every width (many styles).
- P-G2: where D rises from W − 1 to W, most new champions restricted to depths 1..W−1 are not champions of W − 1
  (the non-nesting is visible already at small widths).
- Counterfactual: a shared near-wall pattern, or nesting, would point to one style.

## DQ-033 — Zoom out: a rule along columns, diagonals or skipped cells

**Owner:** "in general we think of rule 30 in terms of rows, because that is what the rule does in a state tick adding
the next row. But can we think of the problem in terms of columns. Can we construct a logic gate sequence / rule that
works vertically, or a combination of horizontal and vertical, or skips elements of a row. Can we 'zoom out' and find a
logic gate structured pathway and that isn't as narrow in scope as the general rule."

**What exists.** Three of the owner's zooms are already in use:
- **Vertical:** the sideways rule x(j−1, t) = x(j, t+1) XOR (x(j, t) OR x(j+1, t)), our wall form and Q01.
- **Diagonal:** the two edge recursions of DQ-029.
- **Skipping a step:** the two-step identity F²(x)_j = x_(j−2) XOR ([x_(j−1) = x_j] AND (x_(j+1) OR x_(j+2)))
  (GC2313).

**Zooming out by blocks: KNOWN, so T-C was dropped before running.** The planned test was an exhaustive search for a
lumping of N-cell blocks into one bit that turns N steps of Rule 30 into one step of an elementary rule. The
literature has it:
- Israeli and Goldenfeld, "Coarse-graining of cellular automata, emergence, and the predictability of complex
  systems" (PRE 2006, arXiv nlin/0508033): "The 16 elementary CA which we could not coarse-grain are rules 30, 45, 106,
  154 and their symmetries."
- Song and Aaron (arXiv 2012.12153) pushed the same search to blocks of 7 and found 20 rules with none: the 16, plus
  the classes [37, 91] and [164, 218].

So no block zoom of size ≤ 7 onto a two-colour rule exists for Rule 30.

*Correction (owner, round 2):* dropping this test as "already known" broke one of the owner's earliest rules: a known result is worth proving, because an unproved assumption can waste later time. T-C was reinstated and run (round 2, below): reproduced to N = 4. What remains open:
- zooms onto targets with more colours or wider reach (not searched in those papers, as far as the summaries go);
- zooms along a moving frame: the centre is a moving point in the diagonal frame.
Neither is tested.

## DQ-034 — Every width at once is one infinite object

**Owner:** "The problem here is the width is infinite. Even a finite width is 'finite' in the sense the width
alternates black and white. The left and right edges are still 0 infinitely. So when we say every width, we really
mean the infinite width that alternates black and white forever. The closest we have got to this is the single seeds
past state which infinitely repeats beyond the 1 wall with a 0 chink that starts the pyramid pattern."

**What Local takes from it.** Q01 asks about a finite patch in a white sea beside the wall. With an infinite left half
every wall trace can be kept: G130 realises every trace, the alternating wall included, with a finite right tail and
a possibly infinite left word. So the whole content of Q01 is the **white sea far away**. The owner's analogy, a
periodic sea with a chink (the seed's past B), suggests the experiment: replace the white sea by a periodic sea
(a word u repeated forever to the left) and ask for which seas some finite patch keeps the wall. White is the sea of
period 1.

**Test T-H: the sea census.** Every word u of length 1–6 (each rotation), every patch on depths 1..8, sea u beyond;
the wall form run to K = 160, recording the longest life. Record searched: G128.1 (NKS notes to p. 267: the wall
cannot be closed by giving every column period 2); GC720 (the five-cycle shift orbit has temporal period 5); G130;
GC2270's periodic backgrounds are for the backward ocean, not the wall. No forward sea census beside the wall.
- P-H1 (control): u = 0 reproduces D(1..8).
- P-H2: no sea of period ≤ 6 keeps the wall to K = 160 with any patch of width ≤ 8. The obstruction is not special to
  white; lives stay near 2 × (patch width + period).
- Counterfactual: a sea that keeps the wall to the cap would show that Q01's obstruction belongs to the white sea
  itself. Its patch would be a pattern to study beside the seed's past.

**T-H2, added after T-H (prediction written before this run).** T-H found that the checkerboard sea, and only it,
hosts the clock. The record explains why: Condrey's fixed checkerboard keeps column −1 black for ever and masks any
wall (G11.1, G128.1). The next question is whether white-sea champions live by imitating the checkerboard near the
wall. For every champion at W ≤ 20 and every even time of its life, take the fraction of depths 2..6 agreeing with
the checkerboard phase that has depth 1 black (depth d black iff d is odd). Compare with all starts alive at t = 4.
- P-H3: the champions' mean agreement is at most 60 %, about as for random survivors (CL666 reads them as relays of
  lone cells, not as checkerboards).
- Counterfactual: 80 % or more would mean the clock lives by local imitation of the checkerboard and dies when the
  white sea's news breaks it.

## Round 2 (owner, 31 October afternoon): the late plateaus, and no skipping of known results

The owner's reply to the first write-up:

> "Already known to fail - A caution preposition and one of my earliest rules to guard against. Already known is well
> worth proving, because nothing in science is beyond scrutiny and assumption can creep in without a sound bases. An
> assumption unproved can waste future time if later found to be faulty."

> "Run the late plateaus first, then make sure this round of questioning is well written up. We will hand the torch to
> GPT after this prompted round of work."

So T-C (the block coarse-graining search) is reinstated as a reproduction of known prior art (below), and the late
plateaus of T-F come first.

### T-P: what do the starts that pass a late plateau share? (DQ-031, DQ-032)

**The lens from the record.** GC1772 (hand, from the kit's reconstruction identities): every finite start L of width W
is the truncation of an eternal row Θ f, the infinite row that keeps the clock for ever with L's own odd-time trace.
L dies when the news of the first black cell of Θ f beyond W reaches the wall, and D(W) = W + the longest white run of
such a row after W. So the late regime is about those eternal rows beyond W. A plateau is a stretch where most
survivors' eternal rows keep being white. The question is whether the survivors pass a plateau **together** (one
shared near-wall state, one fate) or **separately** (many states that happen to pass).

Hand fact used below (from T-A): the 3-word on depths 1..3 at an even time t decides survival at t + 2 exactly
(x_2 ≠ x_3). A k-word decides the next (k − 1)/2 ticks. Survivors sharing a long near-wall word share a fate.

Record searched: "plateau|stair" with "survivor|death" → the stairs of D(W) (§8.3) and GC1772/GC1773 (the white-run
identity, the move lemma for CQ01 right halves); CL666 (maximal-excess rows as relays of lone cells); no study of
which starts pass a late tick together. known_find: no hit for plateau survivors in the kit, portal or open PRs.

Predictions, for W = 14..20, late ticks t ≥ W − 2 with at least 16 alive. A plateau tick is t → t + 2 with ratio
≥ 0.75; a cliff is ratio ≤ 0.35.
- P-L1 (shared states): at plateau ticks the survivors occupy at most half as many distinct 7-words (depths 1..7) as
  there are survivors, and the largest 7-word holds at least 20 % of them. At the other late ticks the distinct
  7-words exceed half the survivors.
- P-L2 (near-copies): within the largest 7-word cluster at a plateau tick, the members' starting rows are near-copies:
  the mean pairwise Hamming distance is at most W/4, and the disagreements sit in the deepest third of the support.
- P-L3 (cliffs are clusters dying together): at a cliff, at least half of the deaths come from one 7-word cluster at t.
- Counterfactual: no difference in sharing between plateau and other late ticks would mean plateaus are not shared
  fates. Unrelated cluster members (mean distance near W/2) would mean distinct heads converge to one near-wall state,
  an attractor, which is itself worth knowing.

### T-S: the owner's stamp, skewed onto columns and diagonals (DQ-033)

The owner, mid-round (their message did not get through in its first form):

> "I am not thinking about an application of gates as the role affixes them. I am thinking more generally in terms of
> horizontal, diagonal or vertical traces. Ie, can we skew the entire rule 30 template itself, 00011110, where the
> stamp of each cell is the central cell of the 3 cells above it, with a different complementary stamp shape that
> works on the diagonals."

**Hand answer (PROOF-SKETCH, Local solo; checked by T-E's controls).** Every Rule 30 spacetime obeys one four-cell
relation, the stamp: with a, b, c the left, centre and right cells of a row and d the cell under b,

  d = a XOR (b OR c).

The XOR can be solved for a (a = d XOR (b OR c)); the OR cannot be solved for b or c. Reading the same stamp in
other coordinates gives the other rules:
- **Rows (the usual rule).** Output d from the row above: the table 00011110 (Rule 30).
- **Columns (the sideways rule).** Output a from the column to its right and that column's right neighbour: the same
  four cells, with the output in the other corner. It is the stamp turned on its side. Used by Q01 and Meier–Staffelbach.
- **Left diagonals.** In left-diagonal coordinates the stamp is L_k(t+1) = L_(k−2)(t) XOR (L_(k−1)(t) OR L_k(t)),
  one-sided on diagonals k − 2, k − 1, k. Read in that order its table is **00011110 again**: Rule 30 itself on a
  one-sided neighbourhood.
- **Right diagonals.** D_k(t+1) = D_k(t) XOR (D_(k−1)(t) OR D_(k−2)(t)). In the order (k − 2, k − 1, k) its table
  is **01010110, Rule 86**, the mirror image of Rule 30, on the same one-sided neighbourhood.

So skewing the template onto the diagonals gives back Rule 30 on the left and its mirror on the right. The new
information is in what each direction **forbids**.

**Test T-S: the trace grammar.** Count every pattern that two adjacent lines can carry over n steps: two rows, two
columns, two right diagonals, two left diagonals; single lines as controls. Exact: Rule 30 is onto, so every finite
row has a past, and the valid patches of a window are exactly the images of every base row wide enough to cover its
light cone. The growth rate per step, N(n + 1)/N(n), measures how much freedom the pair of traces has in that
direction. 4 is no constraint; 2 is one line fixing the other.

Hand predictions:
- **Two left diagonals are free.** L_(k−2) is solved from L_(k−1) and L_k, and so on leftwards, so nothing constrains
  the pair.
- **Two right diagonals and two columns are constrained.**
  - Right diagonals: when D_(k−1)(t) is black, D_k must flip, D_k(t+1) = NOT D_k(t).
  - Columns: when x(j+1, t) is black, x(j+1, t+1) = NOT x(j, t). This is Meier–Staffelbach's "10 forces a 1 to its
    left".
  - Each forced flip alone gives growth 3. The forced values then cascade into the next line and add more
    constraints.

Record searched: "directional entropy|Milnor|expansive direction" → Milnor 1988 (Example 6.2, the causal cone of a
left-permutive map), Sablik (Rule 30 is left-expansive with no expansive direction; overlooked-ca-survey), Kopra 2023
(rapid left expansivity); §8.38 counts pairs of anti-diagonals along forced walks, a different object. No two-line
census by direction in the record, the kit or the portal.
- P-S1 (controls): two rows give N(n) = 2^(n+2) exactly; a single row, column or diagonal gives 2^n (every trace
  occurs).
- P-S2: two adjacent left diagonals give N(n) = 4^n exactly.
- P-S3: two adjacent right diagonals and two adjacent columns both have N(n)/4^n → 0, with growth between 2 and 3,
  strictly below 3 by n = 8.
- Counterfactual: free right diagonals, or columns growing at exactly 3, would mean the forced flips do not cascade
  and the hand picture is wrong.

### T-C reinstated: block coarse-graining, reproduced (DQ-033)

Israeli and Goldenfeld's definition (PRE 2006): a projection P of N-cell blocks to one bit is a coarse-graining of
Rule 30 onto an elementary rule g if P(F^N(abc)) = g(P(a), P(b), P(c)) for all blocks a, b, c (N steps of Rule 30
are one step of g). Constant P is excluded. Exhaustive for N ≤ 4: 2^(2^N) projections.
Record searched: as for T-C above; Israeli–Goldenfeld 2006 (rule 30 among the 16 they could not coarse-grain),
Song–Aaron 2020 (none to N = 7).
- P-C1 (controls): Rule 90 and Rule 150 coarse-grain onto themselves at N = 2 with P = the first cell of a block
  (their even sublattice runs on its own). The search must find these.
- P-C2: Rule 30 has no non-constant coarse-graining for N = 2, 3, 4, and neither have its mirror and complement images
  86, 135 and 149 (a consistency check by symmetry).
- Counterfactual: any consistent P for Rule 30 would contradict both papers, and would be a zoom with a shortcut for
  the projected quantity.

**T-S2, added after T-S (prediction written before this run).** T-S's control P-S1 failed in two places: a single
right diagonal cannot carry every sequence, and two rows carry 3 · 2^n patterns, not 2^(n+2). Hand reason for the
diagonal: along a right diagonal s(t) = x(t, t), the flips are f(t) = s(t+1) XOR s(t) = x(t+1, t) OR x(t+2, t). Every
flip depends only on cells to the diagonal's right, and s(0) does not affect them. So the diagonal's language is
"either starting value, then a flip word that the OR of the next two diagonals can produce".
- P-R1: every forbidden diagonal word comes with its complement (same flips); the first forbidden words have length
  5, one flip word of length 4 (32 − 30 = 2).
- P-R2 (independent control): along every right diagonal of 2,000 steps of Rule 30 from random rows of width 6,001,
  no minimal forbidden word occurs, and every allowed word of length ≤ 8 occurs.

## Outcomes of round 1

(Written after the runs, below this line. Predictions above are unchanged.)

All runs are on Local's M5 under `run_capped`, every one COMPLETED. Outputs are kept outside git, in the
inquisition-20261031 folder of the local scratch area, cited by SHA256 prefix:

| Test | Probe (source) | Output | Caps (CPU s / wall s / RSS MiB) |
|---|---|---|---|
| T-A, T-F, T-G | `inquisition_wall_census.py` (`a954b322`) | `21045f31` | 900 / 1200 / 6000 |
| T-E | `inquisition_diagonals.py` (`b59b2006`) | `c132337e` | 300 / 400 / 3000 |
| T-H | `inquisition_sea_census.py` (`3273f5be`) | `781c126e` | 600 / 800 / 3000 |
| T-H2 | `inquisition_checker_imitation.py` (`af5bc0a5`) | `a3081850` | 900 / 1200 / 6000 |

### T-A (DQ-027): the death kind is a fair coin

- **P-A1 held.** The census reproduces D(2..20) exactly (asserted).
- **P-A2 held.** The hand law held on every start of every width to 20 (asserted).
- **P-A3 held.** Starved deaths are 50.0 % at W = 20 (262,158 starved, 262,130 cancelled), and 46.9–50.6 % at every
  W ≥ 6.
- **P-A4 held.** The champions' kinds are mixed: starved at W = 2, 3, 5, 7–13, 19, 20; cancelled at W = 6 and 14–18;
  both at W = 4.

**An exact symmetry explains the even split (PROOF-SKETCH, Local solo; COMPUTED exact at every death time t ≤ W − 1,
W ≤ 20).** For an even death time t with 2 ≤ t ≤ W − 1, exactly half of the starts dying at t are starved. The proof
uses the edge of the light cone: the deepest cell a value depends on enters by XOR. So x_1(t − 1) depends on depth t
by XOR, x_1(t) depends on depth t + 1 by XOR, and depth-1 values at times ≤ t − 2 do not see depths t or t + 1.

The pairing σ:
1. flip depth t;
2. if that made x_1(t) black, flip depth t + 1 as well.

What σ does:
- It leaves the life up to t − 2 unchanged.
- It keeps the death at t.
- It flips x_1(t − 1), which is the kind.
- It is an involution without fixed points.

The early halving law is the same argument with depth t + 1 alone. From t = W on, there are no fresh bits and the
counts differ: at W = 20 and t = 20 they are 256 against 270.

**Lesson.** In Q01, "starved or flooded" carries no information about why the clock dies. Before the news from the far
edge arrives, the kind is a fresh coin, exactly. After it arrives, the split stays near even (late deaths at W = 20:
526 starved, 498 cancelled). The owner's two kinds of interference happen equally often: the two cells beside the wall
come into phase both white as often as both black.

### T-F (DQ-031): the Hydra culls fairly until the news, then in plateaus and cliffs

- **P-F1 held only up to t ≤ W − 1, and failed at t = W.** The survivors halve exactly at each even t ≤ W − 1, at
  every W. At even W the tick at t = W is not a halving: 0.25 at W = 8, 0.531 at W = 10, 0.594 at W = 12. The cone
  argument above needs depth t + 1 ≤ W, so the exact law stops one tick before my prediction said.
- **P-F2 REFUTED.** After W the tick ratio with at least 16 alive ranges over 0.14–0.88. There are **plateaus**, where
  most survivors pass (0.84 and 0.81 at W = 16, t = 24 and 26; 0.83 at W = 19, t = 26). There are **cliffs** (0.136
  at W = 18, t = 30).
- **P-F3 REFUTED.** D(11) = 30 is 10 above the halving line 2W − 2 = 20; I predicted at most 8. It was a slip against
  a value already in the control table.
- **P-F4 held.** Heads are equal on average: among starts alive at t = 4, the mean death time by near-wall pattern
  spreads by at most 0.02 at W ≥ 14. Only four near-wall patterns survive to t = 4: 1100, 1010, 1101 and 1011.

**Lesson for the Hydra.** Before the news there is no regrowth and the cull is exactly fair, half the heads per tick.
The rises and falls the owner pictured are real, but they live only in the late regime, from W to D(W). There, groups
of starts survive together over plateaus and then fall off cliffs. These are the stairs of D(W). A potential, if one
exists, has to describe this late regime; the early regime is pure coin-flipping.

### T-G (DQ-032): the radar

- **P-G1 held.** The nine champions of W = 19 between them use all four near-wall patterns that survive to t = 4.
  Their spokes:
  - density 0.53–0.68;
  - black runs 5–9;
  - longest white run 1–4.
- **P-G2 held, more strongly than predicted.** At every width where D rises (W = 5, 6, 7, 9, 11, 14, 19), **none** of
  the new champions restricted to depths 1..W−1 is a champion of W − 1. The non-nesting starts at the smallest widths.
- **Champions persist across widths.** The champion set is constant along each stair: 1493 and 1507 for W = 11–13;
  11083, 11165 and 11307 for W = 14–18; nine starts for W = 19–20.

So the owner's radar picture fits: champions are many profiles with no shared near-wall shape. What unites them is a
graph, not a style. The record's candidate for that graph is GC1772/GC1773's D(W) = W + the longest white run of a
forced row after W.

### T-E (DQ-029, DQ-030): the diagonals

- **P-E1 held.** Both recursions match direct Rule 30 for t < 64, and c(t) = D_t(t) = L_t(t). D_3 reads 0011.
- **P-E2 held.** Every right diagonal is periodic from t = 0, with power-of-2 periods. D_4 = 00101101…, period 8,
  which answers the owner's open question. The periods, D_0 to D_35:
  1, 2, 2, 4, 8, 8, 16, 32, 32, 64 (six diagonals, D_9–D_14), 128, 256 (eight, D_16–D_23), 512, 1024, 1024, 2048,
  2048, 4096 (five), 8192, 8192.
  Doubling comes in irregular bursts, with long plateaus.
- **P-E4 held, more strongly.** Every right diagonal from k = 3 on has period greater than k, so the centre reads each
  one inside its first period.
- **P-E3 REFUTED in two parts.**
  - Left diagonals settle **before** the centre reads them for every k ≤ 19 except 18. For example L_10 settles at
    t = 6 and L_17 at t = 15.
  - From k = 20 to 59, τ(k) > k at every k. The ratio τ/k rises from about 1.03 near k = 30 to 1.44 at k = 59; it is
    not within 1.2–1.4 throughout.

  So **the left crystal covers the centre column for about its first 20 steps and then falls behind for good**. The
  record's "the crystal recedes" (DQ-025) is the late behaviour. The crossing at about t = 20 is new to the record, as
  far as the search went.

**Lesson.** In the diagonal frame the centre is a moving reader. It reads the crystal while the crystal still covers
it (t ≲ 20), and after that only diagonals that are mid-transient on the left and inside their first period on the
right. Every fixed diagonal has a shortcut; the reader never stays on one.

### T-H and T-H2 (DQ-034): the clock has one periodic home

- **P-H1 held.** The white sea reproduces D(2..8).
- **P-H2 REFUTED, for a known reason.** Of all 126 seas of period ≤ 6, exactly the two phases of the checkerboard
  (…0101…) keep the wall to the cap K = 160. In phase 10 three patches of the 256 survive; in phase 01, one. Every
  other sea, white included, kills the clock by t = 30. The next best was 011001, at 30.

The mechanism is in the record. The checkerboard is a fixed point of Rule 30. With black at depth 1 it keeps column −1
black for ever, which masks the wall entirely (Condrey's universal fixed checkerboard, G11.1, G128.1). The
checkerboard also heals damage (§8.66). The surviving patches 99 and 125 heal into the pure checkerboard by t = 2 and
t = 4. Patch 171 in phase 01 heals into the checkerboard except at depth 1, which then alternates, black at every even time.

What is new is the census itself: no other periodic sea of period ≤ 6 hosts the clock even briefly.

- **P-H3 held (T-H2).** White-sea champions do **not** imitate the checkerboard. Their mean agreement with it on
  depths 2..6 over their lives is 0.42–0.57, against exactly 0.500 for all starts alive at t = 4 and 0.49–0.51 for
  starts dying at t ≥ W.

**Lesson for the owner's infinite object.**
- The clock has one periodic home among small seas, the checkerboard, which keeps it trivially.
- Q01 asks whether a finite patch in the white sea can keep it for ever.
- The longest-lived white-sea starts get no help from imitating that home: they look like coin flips near the wall.

So "every width at once" is not approached by imitating the one infinite object that works. Any proof must explain
why the white sea, specifically, cannot be a home, when its only periodic neighbour in the census, the checkerboard,
is one. The two are the two spatially periodic fixed points of Rule 30 of period ≤ 2: white (period 1) and the
checkerboard (period 2).

### Threads not run

- **DQ-026** (the bombe's loops in CQ01) waits on a steer about which of two readings the owner meant. *Round 2: the
  owner's pull was about traces, the skewed stamp (T-S); the loops stay a Local curiosity.*
- **DQ-028** (stage-one tightness) is specified with its prediction.
- **DQ-033**'s block zoom is KNOWN (Israeli–Goldenfeld; Song–Aaron). *Round 2: reinstated on the owner's rule and
  reproved to N = 4 (T-C).*
- **DQ-031**'s potential waits on a description of the late plateaus.

### Next warm leads, ranked

1. **The late plateaus (DQ-031 with DQ-032).** What do the groups that pass a plateau share? It is a finite question
   at W ≤ 20, and the first place where the Hydra's rise and fall can be seen in detail. *Round 2 (T-P): the deep
   bits, not near-wall states.*
2. **The white sea against the checkerboard (DQ-034).** Both are fixed points; one hosts the clock and the other is
   conjectured not to. A hand comparison of what a finite patch does at the boundary of each sea might name the
   obstruction.
3. **Stage-one tightness (DQ-028).** Simulable, and it would halve the open part of "can the edge get three ahead".

## Outcomes of round 2

Every run is on Local's M5 under `run_capped`, and every one COMPLETED. Outputs are kept outside git, cited by
SHA256 prefix:

| Test | Probe (source) | Output | Caps (CPU s / wall s / RSS MiB) |
|---|---|---|---|
| T-P | `inquisition_plateaus.py` (`86a96b1e`) | `b51325b5` | 1200 / 1500 / 6000 |
| T-S | `inquisition_trace_grammar.py` (`7c150e81`) | `87c809d9` | 1800 / 2400 / 6000 |
| T-S2 | `inquisition_right_diagonal_words.py` (`91794c52`, with the control fix) | `4d78d340` | 3000 / 3600 / 6000 |
| T-C | `inquisition_coarse_grain.py` (`3ccf5fe9`) | `a542b5c3` | 1800 / 2400 / 8000 |

### T-P: the plateaus are real, but not shared near-wall states

Plateau ticks with at least 16 alive: W = 16 at t = 22 and 24; W = 17 at t = 24; W = 18 and 19 at t = 24. One cliff:
W = 18, t = 28 → 30, ratio 0.136.

The plateaus are not chance. Under fair halving, 67 of 81 passing at W = 19, t = 24 is z ≈ 5.9, and 16 of 19 at
W = 16, t = 22 has probability about 0.002.

- **P-L1 REFUTED.** Plateau survivors are no more concentrated than at other late ticks: distinct 7-words per
  survivor 0.40 against 0.31, and the largest 7-word holds 0.15 against 0.12.
- **P-L2 split.** The largest plateau cluster's members are near-copies at W = 16 and 17 (mean Hamming 0.21 W), but
  not at W = 18 and 19 (0.32–0.34 W). Their disagreements are **not** deep: 0.00–0.18 of them fall in the deepest
  third of the support. The members **share their deep bits and differ near the wall**.
- **P-L3 REFUTED.** At the one cliff, the largest 7-word cluster accounts for 0.42 of the deaths, not half.

**Lesson.** The heads that pass a plateau together are different starts that have converged near the wall while
carrying the same far news (the same deep bits). By GC1772, a start's late fate is the white run of its eternal row
beyond W, which the deep bits govern. So the plateaus belong to the eternal rows, not to near-wall states. The next
test is direct: compute Θ f for the survivors and read their white runs (handed to GPT, below).

### T-S: the trace grammar, by direction

N(n) is the number of patterns a strip of n steps can carry in any Rule 30 spacetime. Growth is N(n)/N(n−1):

| Strip | N(n) | Growth at the largest n | Free? |
|---|---|---|---|
| one row | 2^n | 2 | yes |
| one column | 2^n (n ≤ 13) | 2 | yes |
| one left diagonal | 2^n (n ≤ 9) | 2 | yes |
| **one right diagonal** | 2, 4, 8, 16, **30**, 54, 96, 170, 302, 536 (n ≤ 10) | 1.775 | **no** |
| two rows | **3 · 2^n** (n ≥ 2) | 2 | the second row is fixed except at its right end |
| two columns | 4, 12, 32, 80, 200, 496, …, 207,544 (n = 13) | 2.31, falling | no |
| two right diagonals | 4, 10, 22, 50, 104, 208, 406, 774, 1466 (n = 9) | 1.89, falling | no |
| **two left diagonals** | **4^n exactly** (n ≤ 9) | 4 | **yes, completely** |

- **P-S1 REFUTED in two places.**
  - Two rows carry 3 · 2^n, not 2^(n+2). The bottom row's right end is free only when the top row's last cell is
    white, because the OR with the unseen cell masks it otherwise. The OR's asymmetry shows even in the simplest
    strip.
  - A single right diagonal is **not** free.
- **P-S2 held.** Two adjacent left diagonals carry every pair of sequences.
- **P-S3 held.** Columns and right diagonals are constrained, with growth below 3 by n = 8.

Hand results (PROOF-SKETCH, Local solo):
- **Two adjacent left diagonals are coordinates.** The strip of two left diagonals over n steps is a bijective image
  of a row segment of 2n cells. Cell (−t, t) depends on base cells −2t..0, and on base cell −2t by XOR (the left edge
  of its cone). Cell (−t+1, t) depends on −2t+1..1, with −2t+1 entering by XOR. The 2n "leftmost inputs" are distinct
  and fill −2n+2..1. Solving from the right recovers the base row, so the map is triangular and invertible. This is
  why N(n) = 4^n exactly, and why three left diagonals cannot be free (3n cells from 2n + 1 inputs). Two adjacent
  columns are also a function of 2n base cells, but not onto, so the OR loses information there.
- **A right diagonal never carries 00100 (or 11011).** Along s(t) = x(t, t), the flips are
  f(t) = x(t+1, t) OR x(t+2, t). Write a_t, b_t, c_t, d_t for x(t+1, t), x(t+2, t), x(t+3, t), x(t+4, t). The word
  00100 means flips 0, 1, 1, 0. Flip 0 at t = 0 and t = 3 gives a_0 = b_0 = a_3 = b_3 = 0. Then:
  - a_1 = c_0 and b_1 = c_0 OR d_0, so f(1) = 1 forces c_0 OR d_0 = 1 and b_1 = 1.
  - So a_2 = NOT c_0, and b_2 = NOT(c_1 OR d_1).
  - a_3 = 0 needs b_2 OR c_2 = NOT c_0; b_3 = 0 needs c_2 OR d_2 = b_2.

  Two cases:
  - **c_0 = 1.** Then a_2 = 0, so f(2) = 1 needs b_2 = 1. But b_2 OR c_2 must equal 0. Contradiction.
  - **c_0 = 0.** Then d_0 = 1, and c_1 = c_0 XOR (d_0 OR e_0) = 1, so b_2 = 0 and a_2 = 1. Now b_2 OR c_2 = 1 gives
    c_2 = 1, while c_2 OR d_2 = b_2 = 0 gives c_2 = 0. Contradiction.

**T-S2: the minimal forbidden words of one right diagonal, to length 10 (COMPUTED, exact).** In complement pairs:
- 00100 / 11011 (flips 0110);
- 111000 / 000111 (flips 00100);
- 111110010 / 000001101 (flips 00001011);
- 0010100000 / 1101011111 (flips 011110000);
- 1110010100 / 0001101011 (flips 001011110).

- **P-R1 held.** The words are complement-closed, and the first come at length 5 with one flip word, 0110.
- **P-R2 held (after a fix).** The first control run scanned only one diagonal, because of a range bug in its loop.
  That run counted for nothing and was rerun. In the rerun, none of the ten words occurs anywhere along the about
  6,000 right diagonals of 2,000 steps in three random spacetimes. All 170 allowed words of length 8 occur, and no
  disallowed one.

**Prior art.** The record has directional entropy (Milnor 1988; Sablik: Rule 30 is left-expansive, with no expansive
direction; Kopra 2023). A web search for Rule 30's diagonal trace subshift found nothing specific. The nearest
framework is Guillon and Zinoviadis on diagonal determinism. So this is COMPUTED here, with prior art possible and not
found.

**Lesson for the owner's stamp question.** Skewing the stamp onto the diagonals gives back Rule 30 (left) and its
mirror Rule 86 (right). The directions differ completely in what they forbid:
- the left diagonals are **coordinates**: two of them carry anything, and together they are the row;
- columns lose information to the OR;
- a single right diagonal already has a grammar, which begins with "never 00100".

In the owner's words: the left-diagonal trace is the free one, and the right diagonal is the one with rules.

### T-C: block coarse-graining, known and reproved here

- **P-C1 held.** Rules 90 and 150 each have 6 non-constant coarse-grainings at N = 2, including the first-cell
  projection onto themselves.
- **P-C2 held.** Rule 30, 86, 135 and 149 have none at N = 2, 3, 4 (all 2^(2^N) projections).

This reproduces Israeli and Goldenfeld (2006) and agrees with Song and Aaron (2020, to N = 7) in the range checked.
Filed in PRIOR-ART.md as known, reproved here.

## Round summary (both rounds)

The owner's eight answers and two later remarks became nine threads and nine tests. The new structure, in plain words:
1. **How the clock dies is a coin toss.** The two cells beside the wall come into step, both white or both black,
   exactly half each until the news from the far edge arrives (an exact pairing), and about half after.
2. **The Hydra culls fairly, then in stairs.** Exactly half the heads go each tick until step W − 1. Then come
   plateaus and cliffs that are not chance and not shared near-wall states. Starts that pass together share their
   far bits: the plateaus belong to the eternal rows.
3. **Champions are many styles.** They never nest, at any width where the record rises, and use every possible
   near-wall shape.
4. **The diagonals.**
   - Every right diagonal of the seed repeats from the start (D_4 has period 8).
   - The left crystal covers the centre for about 20 steps and then falls behind.
   - In diagonal coordinates the rule is Rule 30 on the left and its mirror Rule 86 on the right.
   - Two left diagonals are coordinates (they carry anything), and a single right diagonal has a grammar (never
     00100).
5. **The clock has one periodic home.** Of 126 small repeating seas, only the checkerboard keeps the clock, for a
   known reason, and white-sea champions do not imitate it.
6. **Known results, reproved.** No block zoom of Rule 30 to N = 4; the seed's two infinite parents.

Five predictions were refuted outright: P-F2, P-F3, P-L1, P-L3 and P-H2. P-F1, P-E3, P-S1 and P-L2 were refuted in
part. All are kept above. One control (P-R2) had a bug that was caught and rerun.

## Round 3 (31 October, after GPT's block GC2325–GC2329): Local's read of GPT's ether episodes

The owner passed back GPT's [block report](GPT-INQUISITION-20261031.md). It carries my three hand steps and corrects
three of my claims. It also adds two new solo PROOF-SKETCHes that need my carrying read: an upper window (GC2327) and
a lower family (GC2328) for the longest ether-pair episode M(k) behind a moving black edge.

### GPT's corrections, checked and accepted

- **The right-diagonal words were already in the record.** [G258](../proofs/G258-four-forbidden-words-in-every-forward-right-moving.md)
  (9 October) proves 00100, 11011, 000111 and 111000 absent from every right-moving trace, and its five-tick proof is
  my own (L426). My T-S2 list agrees with it. My `Record searched:` line missed it because the record calls a right
  diagonal a "right-moving G trace": `record_find.py "right diagonal" forbidden` does not reach G258, and `00100`
  alone gives 991 hits. Fix: RECORD-MAP now names the alias. Known, reproved here.
- **My sea CONJECTURE is REFUTED twice.** I conjectured that every finite patch beside the wall in a periodic sea other
  than white and the checkerboards dies within a bound depending only on the sea. First, a checkerboard patch of
  width H + 1 keeps the clock to time H, whatever the sea beyond (and `complete_near_wall` permits any finite depth-1
  trace). Second, the kit's own `Rule30PeriodTwoCoupled.etherLeft_zbl` and `ether_col1_black` (kit 842b756f; read
  here at lines 1–60 and 100–200) prove that the left half of the 7 × 4 ether is a wall orbit whose depth 1 is black
  at every even time: the period-seven sea 1100001 hosts the clock forever. My census stopped at period 6, and the
  kit search I ran for T-H looked for the checkerboard, not the ether. "The checkerboard is the clock's only periodic
  home" holds only within that census. Checked numerically below (P-E5).
- **The period-three test was empty.** Every 3-periodic row is white within three steps, so it sends no news forever.
- **The first 2058 timer is already exhibited** in our delivered nested essay (executed notebook, GC2322). Not rerun.
- **Left diagonals with the wall:** fixing L_0(0) = 0 leaves 2n − 1 free bits, and the wall moves across the frame.
  Accepted.

### T-M: the exact longest ether episode, independently (prediction before the run)

GPT's sketches give ceil(2k/3) ≤ M(k) ≤ floor(2k/3) + 4. M(k) is the longest run of ticks in which depths k and k + 1
behind a black right edge match PR69's one-in-four ether, over every row, onset and phase. GPT's pilot checked the
weaker `good` predicate (initial runs, k ≤ 8), not exact matches, and preceded the lower family. Prefix autonomy makes
M(k) an exact finite computation: every onset is an initial run from some prefix X_1..X_(k+1), so the maximum is over
2^(k+1) prefixes and 32 phases. Probe `tests/probes/ether_episode_exact.py` (SHA256 08c50fd4…), my own implementation,
k ≤ 20.

- **P-E1 (both sketches).** ceil(2k/3) ≤ M(k) ≤ floor(2k/3) + 4 for every k ≤ 20; no run reaches floor(2k/3) + 5.
  Counterfactual: a longer run refutes the upper sketch (then find the failing table row); M(k) < ceil(2k/3)
  refutes the lower family.
- **P-E2 (witness).** The GC2328 witness (X_j(0) = ether(j + 3, 1), phase i = k + 3, q = 1) runs at least ceil(2k/3)
  for every k, and exactly ceil(2k/3) for at least two thirds of k ≤ 20: the masking front is an upper bound on the
  disturbance, and I expect it to be nearly tight.
- **P-E3 (the additive constant).** M(k) − ceil(2k/3) is 0, 1 or 2 for every 1 ≤ k ≤ 20. Exact matching fixes both
  bits every tick, where `good` leaves the second bit free at odd phases, so exact episodes should sit well below
  the predicate's ceiling. Counterfactual: M(k) ≥ floor(2k/3) + 3 for some k means the upper window is nearly tight
  even for exact matches.
- **P-E4 (control).** My `good`-predicate maximal initial runs for k = 0..8 equal GPT's 3, 4, 5, 6, 6, 7, 7, 8, 9.
- **P-E5 (the kit's sea).** In the wall form, depths 1.. = 1100001 repeated gives the depth-1 trace 1011 repeated for
  400 steps. Counterfactual: an even-time white means GPT's or my reading of `etherLeft 1` is off.

Controls: PR69's `ether_step` and `ether_pair` tables, and the edge map against a literal Rule 30 row (200 random rows,
40 steps). Caps: run_capped (c8c58b49…), CPU 300 s, wall 600 s, RSS 2048 MiB, files 16 MiB, disk 64 MiB, one process.

Record searched: GPT's report GC2325–GC2329 (in full); PR69 head fcffbaa9 `Rule30EtherGrounding.lean` (in full,
SHA256 538c906a…, matching GPT's citation); kit 842b756f `Rule30PeriodTwoCoupled.lean` (the ether theorems);
`record_find.py` "ether" "episode" (only GPT's GC2327–GC2328 entries) and "masking front" (none); G258. No literature
search beyond GPT's (Brummitt–Rowland 2012; Phillips 2004 still to be compared by figure).

## Outcomes of round 3

(Written after the run, below this line. Predictions above are unchanged.)

### Local's carrying read of GC2327 and GC2328: PROVED, two-party hand

I read both steps against PR69's actual source (head fcffbaa9, `good`, `local_descent`, `pair_descends`,
`ether`, `ether_step`, `ether_pair`), not against GPT's paraphrase.

**The upper window (GC2327).** Frame: u = X_(j+2), v = X_(j+1), w = X_j, with Δu = v OR w and w = 1 ⇒ Δv = 1 (also at
j = 0, since X_1(t+1) = X_1(t) XOR X_0(t)). Each row of the dependency table checks by hand:
- h = 0: source phases 2, 3 give f = 0 and Δu = 1, so y = 1.
- h = 1 and h = 7: Δu = 1 = f OR y, with g = 0; if y = 1 then f = 1 XOR g = 1. So f = 1.
- h = 2: f = 0 and y = 1 − g; y = 1 would give g = 1 and so y = 0. So y = 0.
- h = 3: the past step. u(t−1) = v(t−1) = 0 and u(t) = 1 − f give w(t−1) = 1 − f; w(t−1) = 1 would force f = 1.
  So f = 1.
- h = 4: f = 0 and Δu = 0, so y = 0.
- h = 5: Δu = 1 and g = 1; y = 1 forces f = 0. So f = 1 − y.
- h = 6: g = 0 would make w(t+1) = 1 and then v(t+2) = 1, against phase 2. So g = 1 = f, Δv = 0, and y = 0.

All 17 edges satisfy 3d − 2 ≤ P(h) − P(h′) for P = (0, 5, 2, −1, 4, 1, 6, 3), with slack 8 only at (1, 0) and (6, 0).
The telescope gives the offset bound floor((2k + P(h) + 1)/3). It is at most m + 1, m + 2 and m + 3 at edge phases 2,
4 and 6 (checked for each residue of 2k mod 3). In every row of the edge-phase table, delay plus offset is at most
m + 4.

The parity guard is sound: phase parity equals offset parity from an even start, and the one d = −1 step sits at
odd phase 3. The leaf phase is h + 2k + a ≡ t + p + a, since h ≡ t + p + 6k. The ether reaches `good` through
`ether_pair` with p = q + 2i. No gap. The 2/3 cycle 0 → 3 → 5 → 0 (offsets 1, 0, 1) is reachable from 2, 4 and 6,
and the potential caps every cycle's mean at 2/3.

**The lower family (GC2328).** E_j(t) = ether(j + 3, t + 1) solves the edge recurrence (`ether_step` with i = j + 3),
and E(0) = 0, 1, 1, 1, 0, 1, 1, 1, …. The masking-front lemma is right: it uses only updates at depth ≥ R + 2 ≥ 2.
Its four reference bits E_(3n+1)(2n) are ether(0, 1), ether(3, 3), ether(2, 5) and ether(1, 7), all 1. The
table's second column (all 0) is not needed for the bound. The truncation is sound by prefix autonomy, and
k > floor(3t/2) ⟺ t < 2k/3 gives ceil(2k/3) ticks. Both steps are PROVED (GPT's proof, Local's read). Scope as GPT
states it: a moving black edge, not the fixed wall or centre.

### T-M results

All under run_capped on Local's M5, COMPLETED: CPU 1.60 s, wall 1.68 s, maximum RSS 436 MB. Output `3dd3599b` (out.txt,
in the inquisition-20261031 scratch folder, t-m-ether-episode).

| k | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ceil(2k/3) | 1 | 2 | 2 | 3 | 4 | 4 | 5 | 6 | 6 | 7 | 8 | 8 | 9 | 10 | 10 | 11 | 12 | 12 | 13 | 14 |
| **M(k)** | 4 | 4 | 6 | 6 | 7 | 7 | 8 | 8 | 10 | 10 | 11 | 11 | 12 | 12 | 14 | 14 | 15 | 15 | 16 | 16 |
| floor(2k/3)+4 | 4 | 5 | 6 | 6 | 7 | 8 | 8 | 9 | 10 | 10 | 11 | 12 | 12 | 13 | 14 | 14 | 15 | 16 | 16 | 17 |

- **P-E1 held.** Every M(k) is inside GPT's bounds.
- **P-E2 REFUTED.** The GC2328 witness is not near ceil(2k/3): it **attains M(k) for every k ≤ 20**. The witness is
  optimal; the masking-front proof undercounts its run by 2 to 4 ticks.
- **P-E3 REFUTED.** M(k) − ceil(2k/3) is 2 to 4, and M(k) ≥ floor(2k/3) + 3 for every k. Exact matches sit at the top
  of the window, not near its floor. I was wrong that fixing both bits every tick costs much: for k ≤ 8 the
  `good`-predicate maximum (P-E4) and the exact M(k) differ by at most 1 (at k = 2 and 8).
- **P-E4 held.** My `good`-predicate runs for k = 0..8 are 3, 4, 5, 6, 6, 7, 7, 8, 9, as in GPT's pilot (an independent
  implementation). Controls passed: `ether_step`, `ether_pair`, and the edge map against literal Rule 30.
- **P-E5 held.** The sea 1100001 gives the depth-1 trace 1011 repeated for 400 steps, with no even-time white.

**COMPUTED (k ≤ 20), CONJECTURE beyond:** M(k) = floor(2k/3) + 4 − [k ≡ 0 or 2 (mod 6)]. Equivalently,
M(2n − 1) = M(2n) = ceil((4n + 8)/3). The maximum is attained by 4 (prefix, phase) pairs for odd k, 8 for even
k ≢ 2 (mod 6), and 12 for k ≡ 2 (mod 6).

### A sharper lower bound by hand (Local, PROOF-SKETCH)

Why the witness beats ceil(2k/3): its first disturbance is masked at once. With X the witness (edge black) and E the
reference:
- **t = 1.** X_1(1) = 1 XOR 1 = 0 = E_1(1), because E_(−1)(0) = ether(2, 1) = 1 fills the OR. X_2(1) = 1 XOR (1 OR 1)
  = 0 = E_2(1). E_0(1) = ether(3, 2) = 1 = X_0. So X(1) = E(1) at every depth j ≥ 0.
- **t = 2.** X(1) = E(1) includes the edge digit, so every update from t = 1 agrees. At depth 1, E_0(1) = 1 fills
  E's OR, just as X_0 does. With E_0(2) = ether(3, 3) = 1, again X(2) = E(2) at every j ≥ 0.
- **t = 3.** E_0(3) = ether(3, 4) = 0 ≠ X_0. The edge disagrees again, but X_1(3) = 0 = E_1(3) because E_0(2) = 1. So
  at t = 3 they agree for every j > 0.

Run the masking-front lemma from R_3 = 0. At odd t = 3 + 2n the front may advance two layers. At even t = 4 + 2n it
advances one, because E_(3n+3)(4 + 2n) = ether((3n + 2) mod 4, (2n + 5) mod 8) is ether(2, 5), ether(1, 7),
ether(0, 1) and ether(3, 3) for n ≡ 0, 1, 2, 3 (mod 4), all 1. So R_(3+2n) = 3n and R_(4+2n) = 3n + 2, that is
R_t = ceil(3(t − 3)/2) for t ≥ 3. The pair (k, k + 1) matches at t = 0, 1, 2 and whenever ceil(3(t − 3)/2) ≤ k − 1,
that is t ≤ 3 + floor(2(k − 1)/3). After truncation by prefix autonomy, as in GC2328:

    M(k) ≥ floor(2(k − 1)/3) + 4  (k ≥ 1).

With GPT's upper window this gives **M(k) = floor(2k/3) + 4 exactly for k ≡ 1 (mod 3)** (PROOF-SKETCH, needs GPT's
read). For k ≡ 0 or 2 (mod 3) the gap is now 1, and T-M shows how it splits:
- **k ≡ 3, 5 (mod 6).** M(k) is GPT's upper value. The witness reaches it through a finer mismatch set than an
  interval front.
- **k ≡ 0, 2 (mod 6).** M(k) is already my lower value floor(2(k − 1)/3) + 4, so the upper window is one too generous
  there and needs a sharper potential.

### What round 3 changes

- GPT's ether-episode theorem is two-party: M(k)/k → 2/3, PROVED.
- The additive question GPT left open is nearly closed. M(k) is exact for k ≡ 1 (mod 3), from my PROOF-SKETCH plus
  GPT's window. It is within 1 for the rest, with a COMPUTED conjecture (k ≤ 20) for the exact value.
- The masking-front lemma loses a constant because it ignores early healing (E's own OR masks the black edge at
  t = 0 to 2). A front that tracks the exact mismatch set may give the exact formula. That is the next hand step,
  not run here.
- My sea conjecture is withdrawn (REFUTED by the kit's period-seven ether), and the record map now names "right
  diagonal" as an alias of the G traces, so the G258 miss does not recur.


## Round 4 (2026-10-31, Cloud, CL669): the exact mismatch front of the witness, the final tick for k ≡ 3, 5 (mod 6), and why the even residues are different

Picking up GC2330's two named next steps. Everything below is in PR69's frame as Local's `ether_episode_exact.py`
defines it (E_j(t) = ether(j+3, t+1); the witness X_j(0) = E_j(0) for j ≥ 1 with X_0 ≡ 1; M(k) the longest initial
ether-pair episode at depths (k, k+1) over all prefixes and phases). Local's M(k) table was replicated here first.

### The witness's front is exactly periodic (Cloud, PROOF-SKETCH with a machine-checked finite certificate)

Let D(t) be the witness's set of mismatched depths and R*(t) its maximum. **Claim:** R*(0) = 0, D(1) = D(2) = ∅,
R*(3) = 0, and for every t ≥ 4

    R*(t) = 2 floor((3t − 8)/4),

so the front sits on an even depth always and advances by 2, 0, 2, 2 over each four ticks from t = 3 (pausing at
t ≡ 1 mod 4). Certificate: `tests/probes/wolfram/ether_witness_front.py` (output `.out`).
- (A) For t ≤ 12 the claim is an exact finite computation (prefix autonomy: X_j(t) depends on X_0..X_j(0) only).
- (B) For t ≥ 12, induction on a band. Take the band B(t) of depths [b(t), R*(t)+1]; at t = 12 it is depths 7..15
  with content 111010111. The band evolves on its own: X_j(t+1) needs X_(j−2)(t) only when X_(j−1)(t) = 0, so the
  bottom rises by 1 when the bottom cell is black and by 2 otherwise, and no cell below the band is ever read;
  cells above the band are E by the two-party front lemma (D_j(t) = 0 for j > ceil(3(t−3)/2), and
  ceil(3(t−3)/2) ≤ R*(t)+1 for every t ≥ 4, checked to 10,000 and true by the four residues of t mod 4). After eight
  ticks the band equals its t = 12 content shifted by 12 depths, and E is invariant under (j, t) → (j+12, t+8) by
  ether(i+2, t+4) = ether(i, t). So the eight-tick evolution repeats for ever, and at each of the eight ticks the
  band's maximal mismatch was R*(t). The mismatch pulse inside the band has period four: {R−2, R} at t ≡ 0, 1
  (mod 4), {R−4, R−3, R−1, R} at t ≡ 2, {R−6, R−5, R−3, R−2, R−1, R} at t ≡ 3, then the deep part heals and the
  front jumps by 2. Interior mismatches do sit on odd depths; only the front is always even.
- (C) Corollary. The episode at (k, k+1) ends at the first t with R*(t) ≥ k, and since the front moves from even
  depths by 0 or 2 it then lands on k or k+1, so the witness's episode has length exactly

    L_w(k) = min{t : R*(t) ≥ k} = ceil((4 ceil(k/2) + 8)/3) = floor(2k/3) + 4 − [k ≡ 0 or 2 (mod 6)]   (k ≥ 1),

  checked symbolically for k < 400 and equal to Local's M(k) for k ≤ 20. Hence M(k) ≥ L_w(k) for every k, and with
  GC2327 (M(k) ≤ floor(2k/3)+4, two-party):

    **M(k) = floor(2k/3) + 4 for every k ≢ 0, 2 (mod 6)**, i.e. for k ≡ 1, 3, 4, 5 (mod 6).

  This carries GC2330's "extra witness tick for k ≡ 3, 5 (mod 6)" and re-derives k ≡ 1 (mod 3). The structural
  reason the even depths 2n gain nothing over 2n − 1 on the witness is (B): the front never rests on an odd depth.
  Status: PROOF-SKETCH (Cloud, solo) resting on a finite certificate and the two-party lemma; a carrying read is
  requested (the masking rule for the band bottom, the lemma inequality, the eight-tick return).

### The even residues: two different reasons, neither reachable from the eight-row table alone (Cloud, COMPUTED)

For k ≡ 0, 2 (mod 6) the remaining question is the upper bound M(k) ≤ floor(2k/3)+3. Two computations locate it.
- **GPT's proof tree is already exact for its table.** Replacing the potential telescoping by the exact max-plus
  recursion F(h, 0) = 0, F(h, j) = max over d in D(h) of d + F(h+2+d mod 8, j−1) on the eight dependency rows of
  GC2327, and taking max over the prospective edge phase r of min over the contradictory edge phases h ∈ {2, 4, 6}
  of (delay + F(h, k)), gives exactly floor(2k/3)+4 for every k from 1 to 24. So the potential loses nothing; the
  slack is in the AND-tree itself (its leaves need not be simultaneously realisable), not in the arithmetic.
- **The good predicate is exact at k ≡ 0 (mod 6) and loose at k ≡ 2 (mod 6).** Exhaustive maximal initial runs of
  the predicate, G(k), against the exact ether runs M(k), all 2^(k+1) prefixes:

| k mod 6 | k | G(k) | M(k) | floor(2k/3)+4 |
|---|---|---|---|---|
| 0 | 6, 12, 18 | 7, 11, 15 | 7, 11, 15 | 8, 12, 16 |
| 2 | 2, 8, 14, 20 | 5, 9, 13, 17 | 4, 8, 12, 16 | 5, 9, 13, 17 |
| 1, 3, 4, 5 | all to 20 | = M(k) | = floor(2k/3)+4 | |

  So the missing tick at k ≡ 0 (mod 6) is a finer-tree question for the same predicate (some branch combination of
  GPT's tree cannot be realised), while at k ≡ 2 (mod 6) the predicate genuinely permits one tick more than the
  ether does, and the exact pair values must enter the descent (the first descent step from an exact ether pair
  gives X_(k−1)(t) = E_(k−1)(t) at every tick with E_k(t) = 0 and (X_(k−1) OR X_(k−2))(t) = (E_(k−1) OR E_(k−2))(t)
  at every tick t ≤ L−2, which `good` forgets at phases 1, 3, 5, 7).

### What round 4 changes

- M(k) is now exact for two thirds of the depths (k ≢ 0, 2 mod 6), from the exact front law of the witness plus
  GC2327; the all-residue formula M(k) = floor(2k/3)+4 − [k ≡ 0, 2 (mod 6)] is PROVED on those residues and
  remains COMPUTED (k ≤ 20) on the other third, where only the upper bound is open.
- The "finer mismatch set than an interval front" of Local's round 3 is now explicit: a pulse of width at most seven
  behind an even front, healing from behind, period four in time and six in depth (the certificate uses twelve and
  eight).
- Next hand steps: (i) a second read of the certificate; (ii) for k ≡ 0 (mod 6), a realisability argument on GPT's
  tree (which leaf sets of the m+4 branch conflict); (iii) for k ≡ 2 (mod 6), a one-step exact descent before the
  predicate tree. Neither is a census question; the tables above are their finite tests.

## Round 5 (31 October, Local, L1259): the last third of the depths, k ≡ 0, 2 (mod 6)

The owner passed the torch back after GC2330, CL669 and GC2331. Two-party state: m + 3 ≤ M(k) ≤ m + 4 with m =
floor(2k/3), and M(k) = m + 4 exactly for k ≡ 1, 3, 4, 5 (mod 6). Only the upper bound M(k) ≤ m + 3 at k ≡ 0, 2
(mod 6) is open. Cloud's diagnosis: for k ≡ 0 (mod 6) the `good` predicate alone suffices (G(k) = M(k)); for
k ≡ 2 (mod 6) it does not (G(k) = M(k) + 1), so exact pair values must enter. GPT's guard: an exact-pair consequence
needs t ≤ L − 2.

### T-SAT: the conjecture far beyond k = 20 (prediction before the run)

A finite window of an ether episode is a small CNF: digits 1..k+1 on ticks 0..L−1, the edge recurrence, and the
exact pair (or `good`) at depth k. The first row is free, and every onset is an initial prefix. So M(k) ≥ L iff
some phase class is satisfiable. Probe `tests/probes/ether_episode_sat.py` (SHA256 ba3397da…) uses kissat, and cadical
re-decides every UNSAT on an open residue. Every SAT model is re-simulated forward.

- **P-S1 (the conjecture).** For every k ≤ 150 with k ≡ 0, 2 (mod 6), L = m + 4 is UNSAT in all 16 exact phase
  classes, under both solvers: M(k) = m + 3. Counterfactual: one SAT model, confirmed by re-simulation, refutes the
  conjecture at that k.
- **P-S2 (Cloud's split persists).** G(k) = m + 3 at every k ≡ 0 (mod 6) and m + 4 at every k ≡ 2 (mod 6), to
  k = 150. Counterfactual: if G(k) = m + 3 at some k ≡ 2 (mod 6), the good predicate suffices there after all.
- **P-S3 (controls).** For k ≤ 40: L = m + 3 SAT and L = m + 5 UNSAT in both modes, and L = m + 4 SAT at
  residues 1, 3, 4, 5. For k ≤ 20 the 32 phases agree with the 16 glide classes. Everything to k = 20 matches the
  exhaustive M(k) of L1258 and Cloud's G(k).
- **P-S4 (weak, about the shape of a proof).** The UNSAT refutations stay easy: under a second each to k = 150. That
  is what a short, local chain of inferences would give. Counterfactual: solve times growing fast with k would
  suggest the contradiction is global, which would make a finite periodic certificate less likely.

Caps (run_capped, c8c58b49…): wall 3600 s; CPU 3600 s per process (one Python driver, at most six solver processes
at a time); RSS 6144 MiB summed over the tree; files 64 MiB; disk 512 MiB; launch gate 3072 MiB free;
pressure stop 2048 MiB; swap growth 256 MiB; at most 12 processes.

Record searched: L1258, GC2330, GC2331 and CL669 in full; `known_find.py --new` at 17:2x UTC (kit 842b756f, portal
17:20:19Z, 23 open PRs). The only changes are PR69's and PR68's already-read items, with no new ether-episode
statement. PR69's head is still fcffbaa9. No literature search: this is a finite extremal count in PR69's frame.

### T-SAT results

(Written after the run, below this line. Predictions above are unchanged.)

On Local's M5 under run_capped, COMPLETED: wall 82 s, CPU 241 s over all processes, maximum sampled tree RSS 346 MiB,
at most 8 processes. Output `699257fa` (out.txt, t-sat-ether-episode in the inquisition-20261031 scratch folder).

- **P-S1 held.** At every one of the 50 depths k ≤ 150 with k ≡ 0, 2 (mod 6), L = m + 4 is UNSAT in all 16 exact
  phase classes, and cadical agrees on every class. **M(k) = floor(2k/3) + 3 there (COMPUTED, k ≤ 150).** With the
  two-party results this makes M(k) = floor(2k/3) + 4 − [k ≡ 0, 2 (mod 6)] exact for every k ≤ 150, and PROVED for
  all k in four residues.
- **P-S2 held.** G(k) = m + 3 at all 25 depths k ≡ 0 (mod 6) to 150 (UNSAT in all 8 phases under both solvers). At
  all 25 depths k ≡ 2 (mod 6) to 146, G(k) = m + 4 (SAT, model re-simulated). Cloud's split is not a small-k effect.
- **P-S3 held.** For k ≤ 40, L = m + 3 is SAT and L = m + 5 UNSAT in both modes, and L = m + 4 is SAT at residues
  1, 3, 4, 5. For k ≤ 20 the 32 phases fall into the 16 glide classes, and every value matches L1258's exhaustive
  M(k) and Cloud's G(k). Every SAT model re-simulated correctly.
- **P-S4 held, weakly.** The whole run took 82 s, so the refutations are easy, but individual solve times were not
  recorded.

### T-K: where the extra tick comes from (prediction before the run)

A structural point first. The ether's phase pattern ψ = t + 2j (mod 8) is invariant under (j, t) → (j + 3, t + 2),
and GPT's dependency graph has cycle length 3. So every argument built from depth-homogeneous local inference, the
top window and the edge contradiction gives a bound depending on k mod 3 only. Yet G(6) = m + 3 while G(9) = m + 4.

Under the shift, the instance for k + 3 is the instance for k with three more levels and **two extra early top
ticks** (the window [0, L + 1] maps to [−2, L − 1]). So the period-6 effect must come from one of two places. One
is the knowledge front's profile (the last ticks before nothing is known, at each depth). The other is the **start
corner**: knowledge near t = 0, which propagates down along d = 0 steps whose phase has period 4 in depth. GPT's
tree for the one hard edge phase (r = 7, target at tick 3) never uses top ticks 0, 1, 2.

Probes: `ether_knowledge_map.py` (SHA256 334bd886…) computes, by SAT, the exact set of values each pair
(X_(j+1)(t), X_j(t)) can take. `ether_core_ticks.py` (49b863d9…) finds deletion-minimal sets of top ticks that keep
L = m + 4 UNSAT at r = 7.

- **P-K1 (symmetry check, near-certain).** Without the edge, the map for K = 27 (L = 22, good, p = 5) agrees with the
  map for K = 24 (L = 20, p = 7) at every distance d ≤ 24 from the top, after a 2-tick shift, except where K = 27's
  two extra early ticks add knowledge.
- **P-K2 (the front, about 50%).** In the steady state the knowledge front's profile has period 3 in depth (row
  d + 3 equals row d shifted by 2 ticks near the front). Counterfactual: period 6 at the front means the front
  itself carries the parity.
- **P-K3 (the start corner, about 60%).** At k ≡ 0 (mod 6), good top, r = 7, every deletion-minimal tick set
  contains at least one of ticks 0, 1, 2. At k ≡ 2 (mod 6), exact top, the minimal sets contain the last tick
  L − 1 = m + 3. Counterfactual: no early tick in any minimal set means the start corner is not where the parity
  enters.

Caps (run_capped): wall 1800 s, CPU 1800 s per process, RSS 2048 MiB, files 64 MiB, disk 256 MiB, at most 4
processes; one kissat at a time.

Record searched: as for T-SAT, plus GPT's GC2327 table (r = 7 is the only edge phase needing m + 4 for k ≢ 1 (mod 3)).

### T-K results

(Written after the run, below this line. Predictions above are unchanged.)

On Local's M5 under run_capped, COMPLETED: wall 56 s, RSS 18 MB. Output `fc64d88d` (out.txt, t-k-knowledge in the
inquisition-20261031 scratch folder). Nibble code: bit 2u + v is set when (u, v) = (X_(j+1)(t), X_j(t)) is
possible. So 1, 2, 4, 8 are the four exact values, f is "nothing known", and a, c, 3, e, b, 7 and so on are partial.

- **A good window forces the exact ether below it, not just `good`.** At distance d from the top, every pair on
  ticks 0..e_d is the exact ether pair, even where `good` leaves a bit free. One example (phase 7, good allows
  (1,0) and (1,1)) is excluded by a three-tick, two-level local argument: (1,1) forces X_(K−2)(t−1) = 1 and then
  X_(K−1)(t) = 1, against ΔX_K(t) = 0. Only a front at most four ticks wide is partial. This is why exact and good
  tops agree except near the window's end.
- **P-K1 held in part.** After the 2-tick shift, the K = 24 and K = 27 maps agree cell for cell at distances
  d = 0..5 and 9..18 from the top. They differ at three front cells at d = 6, 7, 8 (ticks 16 to 18 in K = 24's
  frame), and near K = 24's free bottom (d ≥ 19). K = 27's two extra early ticks add knowledge only at its own
  ticks 0 and 1. So the knowledge at the front also depends on how far below the bottom is: knowledge flows up
  along the front from the free bottom, about 18 levels in K = 24. I did not foresee this. A top-down certificate
  must not rely on it, and need not: anything a local top-down argument derives is sound whatever lies below.
- **P-K2 REFUTED.** The front has **period 6 in depth (moving 4 ticks), not 3**. For K = 48 the exact region ends at
  e_d = 35, 33, 33, 32, 32, 31, then 31, 29, … and drops 2, 0, 1, 0, 1, 0 over each six depths. Far from both
  boundaries (d = 30..42) the front words are:

| d mod 6 | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| front after e_d | b | c3b | a7 | 3c | e | 3 |

  Nearer the top (d = 6..21) the words are longer (bdb, c3a7, a7c, 3c, eb, 3e). The rows near the free bottom
  (no edge in this map) lose knowledge. So the front itself carries the parity, and the k mod 6 split is built into
  the knowledge that reaches the edge.
- **P-K3 held.** Every deletion-minimal set of top ticks for the hard edge phase (r = 7) contains an early tick
  (1 in every good set; 0 or 1 in every exact set) and the last tick L − 1, in both modes. The sets are sparse and
  spread over the whole window. For good, k = 12: {1, 3, 5, 7, 9, 11}, exactly the ticks where `good` pins both
  bits (even phases). Sizes grow about k/3.6: 4, 6, 7, 8, 10, 10 ticks at k = 6..36. GPT's tree for r = 7 needs
  only ticks from 3 on; the refutation of the extra tick does not.

What this changes: the proof of the last third is not a better tree on `good`. It is an **exact-ether rigidity
statement with a period-6 front**. A top-down local propagation whose front state is periodic under (6, 4), plus
one finite check at the edge per residue, would cover every k.

### T-L: a sound top-down local sweep (prediction before the run)

`tests/probes/ether_local_sweep.py` (SHA256 172779b4…) keeps, for every depth j and tick t, a set A(j, t) of possible
values of the pair (X_(j+1)(t), X_j(t)). It starts from the top constraint and refines depth by depth from the top
down. A value is removed when a local CSP is UNSAT. The local CSP covers depths j − B..j + U + 1 and ticks t − A..t + Bt,
with every recurrence inside the window, the edge where depth 0 is inside, and the sets already derived at depths ≥ j.
Each local CSP is a relaxation of the full instance, so every removal is sound and an empty set is a refutation.
Windows (U, B, A, Bt) = (3, 4, 3, 4). The same local rules apply at every depth away from the top and the edge, so a
sweep whose state becomes periodic is the core of a certificate for all k.

- **P-L1 (soundness, certain if the code is right).** No SAT instance is refuted. The controls: k = 12, L = m + 3, good,
  p = 7; k = 9, L = m + 4, good, p = 1; k = 8, L = m + 4, good, p = 7 (G(8) = 9); k = 14, L = m + 3, exact, (0, 3).
- **P-L2 (local reach).** Every hard instance at L = m + 4 (edge phase r = 7) is refuted by these windows. These are
  good for k = 6, 12, 18, 24, 30, 36, and exact for k = 2, 8, 14, 20, 26, 32. Counterfactual: if one survives, either
  the windows are too small or the refutation needs non-local reasoning. Then enlarge the windows once, and if it
  still survives, record the obstruction.
- **P-L3 (periodic state).** For K = 48, L = 36, good, p = 7, the per-depth state (end of exact run, front word) in the
  middle depths repeats under (j, t) → (j − 6, t − 4). Its front words are no stronger than the global map's (T-K),
  because the local CSP is a relaxation.

Caps (run_capped): wall 3600 s; CPU 3600 s per process; RSS 2048 MiB; files 64 MiB; disk 256 MiB; at most 10
processes (the driver and up to four kissat at a time).

### T-L results

(Written after the run, below this line. Predictions above are unchanged.)

On Local's M5 under run_capped, COMPLETED: wall 102 s, RSS 17 MB. Output `d375e6b5` (t-l-sweep folder).
- **P-L1 held.** None of the four SAT controls was refuted.
- **P-L2 held.** All twelve hard instances (good k = 6..36, exact k = 2..32, edge phase 7) were refuted, as was K = 48.
  The empty set is always at depth 4, tick 3 (k = 2: depth 2, tick 0).
- **P-L3 held.** For K = 48 every middle row (depths 44 down to 12) satisfies R_(j−6)(t) = R_j(t + 4) for every tick
  t ≥ 1, cell for cell. The tick-0 cell has period 4 in absolute depth (j mod 4 = 0, 1, 2, 3 → c, 8, 9, 6). The rows
  are tick-0 cell, then the exact ether on [1, e_j], then a front word that cycles with the depth from the top mod 6
  (b, c3, a7, c3c, 6e, 3). The local front is one cell weaker than the global map's in places, as it must be.

### T-R: rigidity six depths down (prediction before the run)

T-K's K = 48 map shows depths K − 5 and K − 6 exact on exactly [0, L′ − 5] below a window of length L′. If that is
forced by a bounded region, then any episode of length L + 4 at depth k + 6 contains an episode of length L at depth k
(same row, same reference, by the (6, 4) symmetry). That gives **M(k + 6) ≤ M(k) + 4**, and with the exhaustive base
cases M(2) = 4 and M(6) = 7 it would settle every k ≡ 0, 2 (mod 6). `tests/probes/ether_rigidity.py` (SHA256 42d3795c…)
tests the forcing by SAT in a region with no edge and only B depths below K − 6. That region is weaker than any real
row, so a forcing there holds in every real instance whose region lies at depths ≥ 2.

- **P-R1.** Rigidity holds (every target cell forced) for B = 6 at K = 12, 14, 18, 20, 24, 26 with L′ = m(K) + 4,
  in both modes.
- **P-R2 (locality in depth).** B = 2 already suffices. Counterfactual: if rigidity fails at tick 0 or at tick L′ − 5
  for every small B, the induction loses a tick and the proof must go through the periodic sweep certificate.
- **P-R3 (any window length).** It holds for every L′ from 9 to 30 at K = 20 and 26 (exact mode, B = 6). The lemma
  must not depend on L′ = m + 4.

Caps (run_capped): wall 1800 s; CPU 1800 s per process; RSS 2048 MiB; files 64 MiB; disk 256 MiB; at most 4
processes.

### T-R results

(Written after the run, below this line. Predictions above are unchanged.)

The first launch stopped on the process cap after K = 12 (PROCESS_STOP): my launch line piped through grep, which
pushed the tree past 4 processes. It was rerun unchanged with a cap of 10, COMPLETED. Output in t-r-rigidity-2.
- **P-R1 held in part.**
  - Exact mode at L′ = m(K) + 4 is rigid at every K tested: with B = 6 at K = 12, 20, 24, and with B = 8 at
    K = 14, 18, 26. Tick 0 is what needs the extra depth, and K mod 4 decides which B is needed.
  - Good mode is rigid at K = 12, 18, 24 (B = 8). At K = 14, 20, 26 (≡ 2 mod 6) it is never rigid, even at B = 10:
    the last target tick L′ − 5 at depth K − 6 stays free. That is consistent with G(k) = m + 4 at k ≡ 2 (mod 6).
- **P-R2 REFUTED.** B = 2 never suffices. Tick 0 needs B ≥ 6 or 8, and some interior ticks need B ≥ 4.
- **P-R3 REFUTED.** Rigidity is not a lemma for every window length. At K = 20 it fails at the right end when
  L′ ≡ 3 (mod 8) (L′ = 11, 19, 27) and at L′ = 9. At K = 26 with B = 6, tick 0 fails for every L′. It holds at the
  length the induction needs, L′ = m(K) + 4, with B = 8.

What survives is the route that matters. Each induction step needs only the exact mode, edge phase 7 and
L′ = m(K) + 4. There the right end has a fixed phase within each residue class: (L′ − 1) + 2K + 7 changes by 16 when
K → K + 6. The left end has one of two phases (K mod 12).

### T-R2: is the rigidity local in time? (prediction before the run)

`tests/probes/ether_rigidity_local.py` (SHA256 42dad7fd…) asks, for every target cell, the smallest half-width w of a time
window (ticks t − w..t + w, clipped to the instance) that forces it, with B = 8 levels below.

- **P-R4.** Rigidity holds with the full window at K = 48, 50, 54, 56, covering both residues and both K mod 12
  classes in each.
- **P-R5.** Every target is forced with w ≤ 12, and the needed w is bounded independently of K. The interior ticks
  need w ≤ 4. Counterfactual: if an end cell's needed w grows with K, the rigidity is not a finite local check and
  the proof must use the periodic sweep certificate.

Caps (run_capped): wall 3600 s; CPU 3600 s per process; RSS 2048 MiB; files 64 MiB; disk 256 MiB; at most 10
processes.

### T-R2 results

(Written after the run, below this line. Predictions above are unchanged.)

On Local's M5 under run_capped, COMPLETED (t-r2-local folder).
- **P-R4 held.** Rigidity holds with the full window at K = 48, 50, 54, 56: every target cell is forced.
- **P-R5 held, with a correction to its detail.** The needed half-width is at most 10 everywhere and does not grow
  with K. Ticks 0 needs 10 (8 at depth K − 5 for K ≡ 2 mod 4). The right end needs at most 6. Interior ticks need 4
  or 6, not "≤ 4": ticks ≡ 0, 4, 6 (mod 8) relative to the phase need 6. The whole profile has period 8 in t and
  depends only on K mod 4.

### T-RC: the finite certificate (prediction before the run)

T-R2 makes the proof an induction, **M(k + 6) ≤ M(k) + 4**, with a finite local lemma as its step.
`tests/probes/ether_rigidity_certificate.py` (SHA256 1bf1d5d8…) runs every check the argument needs:
- **TREE:** GC2327's exact max-plus, per edge phase r, with its period F(h, n + 3) = F(h, n) + 2.
- **BASE:** exhaustive M(2), M(6), M(8), M(12).
- **DIRECT:** the rigidity at K = 14, 18, 20, 24, 26, 30.
- **ABSTRACT:** the 80 K-free local CSPs that give the rigidity for every K ≥ 32.
- **CONTROLS:** abstract equals concrete at K = 48, 50; non-vacuity; one tick past the right end is free; the step's
  arithmetic.

- **P-C1.** Every check passes under both solvers.
- **P-C2.** TREE confirms the per-phase table: for k ≡ 0, 2 (mod 6) every edge phase r ≠ 7 fits in m + 4 ticks, and
  r = 7 needs exactly m + 5. Counterfactual: if some r ≠ 7 needs m + 5, rigidity must cover that class too.
- **P-C3.** The right-end control shows tick L′ − 4 is free at one of the two depths for both end phases. So the
  lemma is tight, and the checker does answer SAT.

Caps (run_capped): wall 3600 s; CPU 3600 s per process; RSS 2048 MiB; files 64 MiB; disk 256 MiB; at most 10
processes.

### T-RC results, first run, and the proof-checked rerun (prediction before the rerun)

(Written after the first run, below this line. Predictions above are unchanged.)

First run (SHA256 of the probe at a0c756b3), COMPLETED in 1.9 s, output `2a1c49a6` (t-rc-certificate folder).
**P-C1, P-C2 and P-C3 held.**
- TREE: F(h, n + 3) = F(h, n) + 2 from n0 = 4. The needed delay + max offset − m(k) by edge phase is r = 0: 3,
  1: 2, 2: 1, 3: 3, 4: 2, 5: 3, 6: 2, 7: 4, exactly my hand table, so only r = 7 needs m + 5.
- BASE: exhaustive M(2), M(6), M(8), M(12) = 4, 7, 8, 11.
- DIRECT: rigidity holds at K = 14, 18, 20, 24, 26, 30.
- ABSTRACT: all 80 local CSPs are UNSAT under both solvers.
- CONTROLS: all pass. At tick L′ − 4, both depths are free for both right-end phases.

The rerun adds independent proof checking. The probe is now SHA256 a71741ba…. Every UNSAT in DIRECT and ABSTRACT also
gets a cadical LRAT proof, checked by a 40-line RUP checker in the probe. The checker is tested by rejecting a
proof with a dropped hint, and a proof replayed against a different CNF.
- **P-C4.** Every proof checks, and both corruption controls are rejected. Counterfactual: a failed proof check
  means a solver's UNSAT is not trusted there.

### T-RC rerun results

(Written after the run, below this line.)

Rerun COMPLETED in 2.9 s, output `ceafd787` (t-rc-certificate-lrat folder). **P-C4 held.** All 254 LRAT refutations
check: 174 in DIRECT, 2·(L′ − 4) targets per K, and 80 in ABSTRACT. The checker rejects the proof with a dropped hint
and the proof replayed against another CNF. Every earlier line of output is unchanged.

### The theorem and its proof (Local, PROOF-SKETCH with a machine certificate; carrying read requested)

**Theorem.** For every k ≥ 1, the longest ether-pair episode at depths (k, k + 1) behind a black right edge is

    M(k) = floor(2k/3) + 4 − [k ≡ 0 or 2 (mod 6)].

Moving black edge, PR69's frame and invariant; not the fixed wall, the centre column or any density.

**Proof.** Write m = floor(2k/3), and let r be the ether's phase at depth 0, tick 0, so E_j(t) = e(t + 2j + r)
with e = (1,1,0,1,0,1,0,0).
- **Residues 1, 3, 4, 5 and the lower bound** are two-party PROVED: GC2327 (upper), and CL669 + GC2331 (the
  witness, whose episode has length m + 4 − [k ≡ 0, 2 (mod 6)]).
- **Remaining:** M(k) ≤ m + 3 for k ≡ 0, 2 (mod 6).
- **(T) Every phase but one is settled by GPT's tree.** For k ≡ 0, 2 (mod 6) and r ≠ 7, the GC2327 tree whose root
  is the cheapest contradictory edge phase needs leaves only in ticks 0..m + 3. Its delay + max offset − m is
  3, 2, 1, 3, 2, 3, 2 for r = 0..6, by the exact max-plus recursion, whose period F(h, n + 3) = F(h, n) + 2 holds
  from n = 4 and so for all n. So no episode of length m + 4 exists for r ≠ 7. (GC2327's parity guard keeps every
  leaf at offset ≥ 0.)
- **(R) Rigidity, for r = 7.** Let K ≡ 0, 2 (mod 6), K ≥ 14 and L′ = m(K) + 4. If a row has X_K = E_K and
  X_(K+1) = E_(K+1) on ticks 0..L′ − 1, then X = E at depths K − 6 and K − 5 on ticks 0..L′ − 5. Each target cell is
  forced by a local system: depths K − 14..K + 1, ticks t − 10..t + 10 clipped to 0..L′ − 1, the recurrence
  (valid in every real row at depths ≥ 2), and the top pair. That system is UNSAT with the target's value flipped.
  For K = 14..30 this is checked directly. For K ≥ 32 each local system is, clause for clause up to renaming, one
  of 80 systems indexed by the target's phase (t + 2K + 7) mod 8, its two clip lengths and its depth. Within each
  residue the end phases are fixed: tick 0 has phase 7 or 3, and tick L′ − 1 has phase 2 (K ≡ 0) or 7 (K ≡ 2). For
  L′ ≥ 25 no window is clipped on both sides. All 254 systems are UNSAT under kissat and cadical, with checked LRAT
  proofs.
- **Induction.** The base is exhaustive: M(2) = 4, M(6) = 7, M(8) = 8, M(12) = 11, each m + 3. For K = k + 6 ≥ 14
  in the class, suppose a row had an episode of length m(K) + 4 at depth K.
  - If r ≠ 7, (T) excludes it.
  - If r = 7, (R) gives the same row an episode of length m(K) + 4 − 4 = m(k) + 4 at depth k, with the same
    reference. That contradicts M(k) ≤ m(k) + 3.
  So M(K) ≤ m(K) + 3. The chains 6 → 12 → 18 → … and 2, 8 → 14 → 20 → … cover every k ≡ 0, 2 (mod 6). ∎

**Status.** The finite checks are a machine certificate with controls: `ether_rigidity_certificate.py`, output
`ceafd787`. The reduction from the theorem to those checks is a hand argument by Local, solo, so the whole is a
PROOF-SKETCH until GPT reads two steps:
1. that (T)'s per-phase table follows from GC2327's tree;
2. that the 80 abstract systems cover every target of every K ≥ 32 (the parametrisation and the clip cases).

The computation agrees independently: SAT to k = 150 (T-SAT) and exhaustive to k = 20 (L1258).

(Superseded in presentation by [the outcomes of round 5](#outcomes-of-round-5-mk-for-every-k), which give two further
independent proofs and the verification; this section is kept as written.)

**What it teaches.** The extra tick is not lost to a better tree. It is lost because an exact window is **rigid**:
it forces the exact ether six depths down, on a window exactly four ticks shorter, so the problem at k + 6 contains
the problem at k. The parity effect the trees cannot see is just the base case M(6) = 7 against M(9) = 10,
transported by that rigidity.

### T-RD: direct cross-check of the abstraction (prediction before the run)

- **P-D1.** `ether_rigidity.py` in exact mode with the full window and B = 8 finds rigidity at K = 36, 38, 60, 62 with
  L′ = m(K) + 4. These K are covered only by the abstract systems, never checked directly. Counterfactual: any
  unforced target means the abstract coverage argument has a hole.

Caps (run_capped): wall 1800 s; CPU 1800 s per process; RSS 2048 MiB; files 64 MiB; disk 256 MiB; at most 10
processes.

### T-RD results

(Written after the run.) COMPLETED in 1.4 s (t-rd-direct folder). **P-D1 held.** Rigidity holds directly at K = 36, 38,
60 and 62: every target at depths K − 6 and K − 5 on ticks 0..L′ − 5 is forced, agreeing with the abstract coverage.

## Outcomes of round 5: M(k) for every k

(Written after every run above. Predictions above are unchanged.)

**Theorem (PROOF-SKETCH by Local, with three machine certificates; carrying read requested from GPT).** For every
k ≥ 1, the longest ether-pair episode at depths (k, k + 1) behind a black right edge is

    M(k) = floor(2k/3) + 4 − [k ≡ 0 or 2 (mod 6)].

The episode is taken over any row (finite or not), any onset and any phase. At edge phase 7 the GC2328 witness is the
**unique** optimal prefix: every other prefix has an episode at least one tick shorter. Scope: a moving black edge in
PR69's frame and invariant. There is no fixed-wall, centre-column or density claim.

Three independent proofs exist. Each was found or checked in this round and each has its own certificate.

### Proof 1: a front potential (the shortest to read)

Found by a sub-agent of Local (route "mismatch comparison"). Local then read every step and checked it by hand and
by an independent simulation. Certificate: `tests/probes/ether_front_potential_certificate.py`.

1. **Two-sided frame.** Put X_j = 0 for j < 0. The black-edge row then obeys X_j(t+1) = X_j(t) XOR
   (X_(j−1)(t) OR X_(j−2)(t)) at every integer j. So does the reference wave E_j(t) = e(t + 2j + c), because
   e(p + 1) = e(p) XOR (e(p − 2) OR e(p − 4)). The mismatch D = X XOR E then satisfies
   D_j(t+1) = D_j(t) XOR F_φ(D_(j−1)(t), D_(j−2)(t)) with φ = t + 2j + c. F_φ is OR at φ ∈ {0, 6}, (NOT a) AND b at
   {1, 4}, a AND (NOT b) at {2, 3}, and AND at {5, 7}; always F(0, 0) = 0.
2. **Front moves (Lemma A).** Let the front be R(t) = max{j : D_j(t) = 1}, with phase ψ = t + 2R + 2 + c (mod 8).
   At ψ ∈ {2, 4, 6, 7} the front moves +2, and at ψ = 0 it moves +1. At ψ = 3 it moves +1 if D_(R−1) = 0, else
   stays. At ψ = 5 it moves +1 if D_(R−1) = 1, else stays. At ψ = 1 it stays, unless D_(R−1) = D_(R−2) = 1, when it
   retreats. All 32 configurations are checked against the literal update.
3. **Potential.** Φ = R + g(ψ) − 3t/2, with g = (−3/2, 0, 3/2, −1, 1/2, −2, −1/2, 1), is unchanged by all ten
   non-retreat moves.
4. **No retreat after tick 0 (Lemma B).** This holds for rows whose initial mismatch has finite support, so that the
   front exists. ψ = 1 is entered only from ψ = 4, by the forced +2 move, and that move leaves
   D_(R−1) = F_4(1, ·) = 0. A retreat lands on an even phase. So R never decreases from t = 1 on, and Φ(t) = Φ(1)
   for every t ≥ 1.
5. **Floor at t = 1.** The cells j ≤ 0 are fixed, so Φ(1) ≥ Φ_c. The floor is −5/2, −1, 1/2, −2, −1/2, −3, −3/2
   for c = 0..6. At c = 2 and 4 the one row that heals at t = 1 has infinite support, so it is excluded. This
   exclusion is load-bearing: without it the comparison fails, with Rmin(2, 4) = 1 < R_w(4) = 2. At c = 6 the
   healing row is also infinite, but there the floor is the same either way. At c = 7 the healing row is exactly
   the witness (Φ = −4), and every other row has Φ(1) ≥ 0. These two places, the finite-support exclusion at
   c = 2, 4 and the dichotomy at c = 7, are where the k mod 6 effect is decided.
6. **Front comparison.** For t ≥ 1, R(t) ≥ R_w(t) for every row with a finite initial mismatch and every phase,
   where R_w(t) = 6n − 4, 6n − 4, 6n − 2, 6n at t = 4n..4n + 3 (t ≥ 1) is the witness's front. At c = 7, every other row has
   R(t) ≥ R_w(t) + 3. This follows from the floors through the (4, 6) periodicity of the potential.
7. **Episodes.** Replace the row beyond depth k + 1 by the ether. Prefix autonomy keeps the pair, the mismatch stays
   below depth k throughout the episode, and front comparison ends the episode by tick L_w(k) = min{t : R_w(t) ≥ k}.
   That equals floor(2k/3) + 4 − [k ≡ 0, 2 (mod 6)].

This reproves, as corollaries, the exact-pair half of GC2327's bound (M(k) ≤ floor(2k/3) + 4) and the CL669/GC2331
witness front (known, reproved here). It does not reach GC2327's bound on the `good` predicate, which equals m + 4 at
k ≡ 2 (mod 6). It also
explains the parity. The potential has period 3 in k, except along the witness's lane, whose front stands only on
even depths. The (3, 2)-shifted lane has the same Φ but cannot be entered: at t = 1 only the witness reaches
Φ = −4, and no retreat can change lanes.

### Proof 2: a six-depth descent (the cleanest certificate)

Found by a sub-agent of Local (route "alternative certificate") and read in full by Local. Certificate:
`tests/probes/ether_six_depth_descent_certificate.py`. In the generic two-sided model, black-edge rows are the initial
states …0001x₁x₂…. **If the pair at depth j is the exact ether on ticks 0..L − 1 with L ≥ 11, then the pair at depth
j − 6 is the exact ether on 0..L − 5**, for every phase. Time and depth translation reduce this to 56 windows (seven
shapes × eight phases). The light cone limits each window to at most 22 initial digits. All 56 are checked by two
exhaustive enumerators and by kissat and cadical. As a control, with one tick less of look-ahead each shape fails for
some phase (shown by the two enumerators and kissat). The descent loses at most 4 ticks, and exactly 4 in five of
the eight phase classes. So an episode of length L ≥ 11 at depth k contains one of length L − 4 at depth k − 6. The exhaustive bases M(1..8) =
4, 4, 6, 6, 7, 7, 8, 8 finish the induction. The worst look-ahead over D depths is 2, 2, 3, 3, 4, 4, 6, 6, 7, 7, 8, 8
for D = 1..12. That equals 2D/3 only at D ≡ 0 (mod 6), which is why the step is six.

### Proof 3: Local's rigidity with LRAT proofs

T-R, T-R2 and T-RC above. GPT's GC2327 tree settles every edge phase r ≠ 7. For r = 7 a free-column region of 16
depths forces the exact ether six depths down. Its 254 local systems carry cadical LRAT proofs, checked in
`ether_rigidity_certificate.py`. This is weaker than Proof 2 (one phase, one window length, free bottom), but the only
one whose SAT refutations are proof-checked.

Two further routes reached the same theorem by descents: "hand-k2" (a sliding 11-tick Lemma D on black-edge rows) and
"hand-k0". The latter proves the `good` version G(6n) = 4n + 3 = floor(2k/3) + 3 by a 15-digit strip with DRAT-checked
proofs. Their files stay in the scratch store.

### Verification

Two workflows of independent agents were run. Each agent was told to default to "refuted" when a step is
unjustified. All of these are self-checks under AGENTS.md §4, because they are sub-agents of Local.
- **Proof attempts.** Four routes (the good predicate at k ≡ 0, the exact pair at k ≡ 2, an alternative certificate,
  and mismatch comparison) each returned a proof. Each attempt then got three verifiers: logic, coverage and
  reproduction. **12 of 12 verdicts were "not refuted", with no fatal issue.** The verifiers rebuilt the checks in
  their own code: a C enumerator, a BFS, independent SAT encodings with drat-trim-checked proofs, exhaustive
  enumeration to k = 23 and 24, and exact-fraction tables. Every number matched; the certificate outputs reproduced
  byte for byte.
- **Their minor points, now taken into the text above:**
  - the front statements need a finite initial mismatch, so that the front exists;
  - the corollary is only the exact-pair half of GC2327;
  - the theorem needs k ≥ 1 (M(0) = 2 ≠ 3);
  - the controls of Proof 2 use three checkers, not four;
  - the record status is PROOF-SKETCH until GPT reads the hand steps.
- **Local's own checks.** I read both certificates line by line and reran each under run_capped: the front potential
  gave output `f22e97bb`, the same as the coverage verifier's, and the descent `7f7b930c`. I also simulated 6000
  random rows in my own code (every phase, up to 60 ticks, including the witness and near-witness rows): 0 violations
  of no-retreat after tick 0, of constant Φ, or of R(t) ≥ R_w(t). My first run of that simulation cut the scan at
  depth hi − 2t, which this frame does not need, and reported spurious violations. It is kept as a refuted control.
- **Proof 3's four-lens verification** (a second workflow, applied to the theorem section and its certificate):
  - **Logic lens: not refuted, no fatal issue.** It rebuilt GC2327's eight dependency rows by brute force and checked
    the 17 potential edges and the parity guard. Its corrections, accepted:
    - **The phase classes number 8, not 16.** Since ether(i+1, t) = ether(i, t+2), the 32 PR69 phases (i, q) give
      E_j(t) = e(t + 2j + c) with c = q + 2i − 2k, so 8 classes. T-SAT's "16 classes by the glide" was redundant,
      checking each class twice; its conclusions stand.
    - The (T) values 3, 2, 1, 3, 2, 3, 2 are maxima over both residues. By residue they are 3, 2, 1, 2, 1, 3, 2
      (k ≡ 0 mod 6) and at most those maxima (k ≡ 2 mod 6).
    - (T) needs only GC2327's own potential bound, evaluated by k mod 3, not the exact max-plus.
    - DIRECT checks the full tick range, not the 21-tick windows. That is a larger sound relaxation, and the
      windowed form was also checked.
    - L′ ≥ 20 already prevents two-sided clipping (25 is conservative).
    - (R)'s hypothesis should name the r = 7 reference E_j(t) = e(t + 2j + 7).
  - **Independent lens: not refuted, no fatal issue.** It wrote its own encoder from PR69's definitions and rechecked
    the rigidity at K = 32..62 with SAT (556 agreeing UNSAT verdicts) and a solver-free exact transfer-set
    computation over the 2^16 column states. Both agree cell for cell. The rigidity also holds directly at
    K = 14..30 and K = 1200..3008, and the bound is tight: ticks L′ − 4..L′ − 1 are free. It also gave a proof of (R)
    for every K that does not use the 80 systems. The forward and backward transfer sets become periodic, with
    period 8 in t, after 9 to 11 ticks, so the targets meet the same finite set of pairs in each class K mod 12.
    It enumerated every target of every K = 32..1000 in both residues: exactly 40 (phase, left, right) triples times
    two depths, matching the 80 systems. Its wording points are the logic lens's, plus one: counted over the 8
    classes, the maximiser counts are 1, 2, 3, not 4, 8, 12.
  - **Definitions lens: not refuted, no fatal issue.** It matched the frame, the pair orientation and the phases
    against PR69's source (fcffbaa9) and against GC2327, GC2328, L1258 and CL669. It made two points of its own:
    - **"What it teaches" in the theorem section says more than Proof 3 shows.** Proof 3's rigidity holds only at
      L′ = m(K) + 4, edge phase 7 and K ≡ 0, 2 (mod 6); T-R's P-R3 shows the free-column form failing elsewhere.
      The general statement, that an exact window forces the exact ether six depths down on a window four ticks
      shorter, is **Proof 2's descent** (every phase, every L ≥ 11, exact light cone). Along each residue chain it
      carries the base cases, including M(6) = 7 against M(9) = 10. Read that paragraph with this attribution.
    - **The chain wording.** In the induction, 6 → 12 is not a step, because (R) needs K ≥ 14. M(12) is a base case,
      so there is no gap.
    It also flagged two wordings of mine. The rigidity certificate's docstring title ("for every k = 0, 2 (mod 6)")
    should read k ≥ 2, since M(0) = 2. I leave the file unchanged so its cited digests stay valid. NOW.md's "solved"
    is now "has a proof". Its exhaustive side check (k ≤ 18) agrees that the witness is the unique optimum at
    phase 7.
  - **Code lens: not refuted, no fatal issue.** It audited every clause, convention, loop and the LRAT checker. It
    fuzzed the checker (24 crafted attacks, about 3.3 million random steps; no unimplied lemma accepted, no
    satisfiable replay accepted), and re-refuted all 254 systems three ways, including drat-trim. Its substantive
    point was right. **Every check in `ether_rigidity_certificate.py` was an `assert`.** Under `python3 -O` the
    abstract stage silently did not run and the script still printed PASS; only "PROOFS: 174" instead of 254 gave
    it away. The recorded runs used plain `python3` and their 254 count shows every check ran, so no result changes.
    But a certificate must not depend on that. Its other points: the dropped-hint control tested a single mutant, the
    non-vacuity control was trivially satisfiable, and two facts true for every K were checked only on finite ranges
    (the algebra is now in the docstring). The rest is wording, matching the other lenses.

**Hardening after the code lens (prediction before the rerun).** Every `assert` in `ether_rigidity_certificate.py`
(now SHA256 af0b4d00…) and in `ether_six_depth_descent_certificate.py` (now 267efc47…) is an explicit `require()`, rewritten
mechanically from the parse tree with the conditions and messages unchanged. The rigidity certificate adds two
controls on every one of its 254 refutations. The system with the target unit negated must be satisfiable (the
ether is a model), and the LRAT proof replayed on it must be rejected.
- **P-H1.** Both certificates pass, with output unchanged apart from the new PROOFS line.
- **P-H2.** Under `python3 -O` both still run every check: 254 proofs and 254 rejected replays.


### Prior art

The method of Proof 1 (a front state with a potential certified on local patterns) is the kit's
`Rule30EtherThreeErosion` (Luis Perez Morales and Claude, R30-20261024-1fc962, period-three ether erosion and no
wall) and its white-tail extension. PR69 (Troy Lowry) is the source of the invariant and of eventual exclusion.
The exact-pair half of GC2327 (M(k) ≤ floor(2k/3) + 4) and CL669/GC2331 (the witness front) are known, reproved
here. No kit, portal or PR statement gives M(k)
(`known_find.py`, kit 842b756f, portal 17:20:19Z, 23 open PRs; "episode", "ether pair", "front potential").

### For GPT's carrying read

Either proof alone makes the theorem two-party. The machine parts need no second read (AGENTS.md §4). The steps that
carry each proof:

- **Proof 1 (front potential)** checks against the literal update of `ether_front_potential_certificate.py`, parts
  1–5. Read these:
  - (i) the two-sided frame and the mismatch rule F_φ (four Boolean forms by phase);
  - (ii) Lemma B: retreats land on even phases, and the only predecessor of ψ = 1 is ψ = 4 by +2, which leaves
    D_(R−1) = F_4(1, ·) = 0;
  - (iii) the t = 1 floors, above all that the healing row at c = 2, 4 has infinite support (the exclusion carries
    weight) and that at c = 7 it is the witness;
  - (iv) the modified-row reduction (prefix autonomy; the mismatch stays below depth k during an episode) and the
    step from R(L_w(k)) ≥ k to the bound.
- **Proof 2 (six-depth descent)** has its windows certified by exhaustive enumeration in
  `ether_six_depth_descent_certificate.py`. Read these:
  - (i) black-edge rows are the generic configurations …0001x₁x₂…;
  - (ii) the light cone X_j(t) ← X_(j−2t..j)(0);
  - (iii) translation in time (every state is an initial state) and in depth, with the phase bookkeeping;
  - (iv) the window containments for s ≤ 5 and s ≥ 6;
  - (v) the induction from the bases M(2) = 4, M(6) = 7, M(8) = 8.

**Hardening results.** (Written after the runs.)
- **P-H1 held.** Both hardened certificates pass. Rigidity output `fc93a027`: "PROOFS: 254 LRAT refutations checked …
  (254 replays)", every other line as before. Descent output `f0eaabf5`: identical to the earlier run below its first
  line, which prints the file's own hash.
- **P-H2 held.** Under `python3 -O` both outputs are byte-identical to the plain runs (`fc93a027`, `f0eaabf5`), so every
  check now runs regardless of the interpreter flag.
- **A launch error of mine, kept on record.** The first `-O` launch passed "python3 -O" as one word, because zsh
  does not split an unquoted variable. The child exited 127 before running anything (CHILD_FAILED, empty output).
  It was rerun with the arguments written out.

**Verification complete: 16 of 16 independent verdicts "not refuted", none fatal.** That is twelve on the four
proof routes and four lenses on Proof 3. All are same-worker self-checks; the theorem stays PROOF-SKETCH until
GPT's carrying read of Proof 1 or Proof 2.

## Round 6 (31 October, Local, L1261): after GC2333, toward the wall

GPT carried Proof 1 in GC2333, so M(k) is PROVED, two-party. Its scope notes: the mismatch must be bounded above, not
finitely supported on ℤ, and uniqueness holds only for the prefix, only at edge phase 7. A Lean formalization of
Proof 1 is running as a separate workflow; it is not a delivery decision. Here I turn to GC2333's curiosity and to
GC2329's open question: which periodic backgrounds the clock beside the fixed white wall can use, and whether the
long-lived white-sea starts use them.

### T-W: do champions imitate the period-seven ether? (prediction before the run)

T-H2 found that champions do not imitate the checkerboard. The kit's other eternal clock host is the left half of the
7 × 4 ether: the sea 1100001 repeated, with depth-1 trace 1011 and time period 4. In the wall form the rule is
permutive in its deeper input, so the white tail's news reaches depth 1 at exactly t = W. A long life must come from
what happens after that. `tests/probes/inquisition_ether_imitation.py` (SHA256 e5468a4b…).

- **P-W1 (no imitation).** Over their lives the champions' agreement with the ether is within 0.05 of the baseline
  (all starts alive at t = 4), on depths 2..6 and on 2..14, for every W ≤ 20. Each start takes its better alignment.
  Counterfactual: champions above the baseline by more than 0.1 means long lives come from approaching the ether.
- **P-W2 (ether patches die soon after the news).** An exact ether patch of width W (white beyond) has death time
  D_e(W) with D_e(W) − W ≤ 30 for every W ≤ 300, while the champions' D(W) − W grows (about 0.8W). Counterfactual:
  D_e(W) − W growing with W would make the ether a candidate skeleton for champions.
- **P-W3 (controls).** The checkerboard numbers reproduce T-H2 (champions 0.42–0.57 on 2..6, baseline about 0.500).
  The recomputed D(2..18) equals the known 6, 6, 6, 8, 10, 12, 12, 18, 18, 30, 30, 30, 32, 32, 32, 32, 32.

Caps (run_capped): wall 2400 s; CPU 2400 s per process; RSS 6144 MiB; files 64 MiB; disk 256 MiB; at most 4 processes.

Record searched: T-H, T-H2, GC2329 (the period-seven correction), DQ-034, GC1772 (eternal rows), the kit's
Rule30PeriodTwoCoupled (etherLeft, ether_col1_black) and Rule30WhiteTailErosion (period-three ether erosion with a
white tail; a different ether and frame). `record_find.py` "ether" "champion" gives 12 hits. Besides T-H2/DQ-034,
they are GC1168 (fitted champions' clock deadline in the left-horizon game) and `rule30_leftside_jump.py` (left-horizon
jumps). They concern champions of other games; none measures agreement with the 7 × 4 ether. (Corrected after the
search: the first version of this line, committed with the predictions, said "no hit beyond T-H2" before I had read
the hits.)

### T-G: which periodic backgrounds can follow a black edge, and for how long? (prediction before the run)

GC2333's curiosity, and PR69's open "general same-edge rigidity", in census form. In the edge frame a periodic
background is a cycle of the ring map R_j(t+1) = R_j(t) XOR (R_(j−1)(t) OR R_(j−2)(t)) on ℤ/p, the kit's
`Rule30RingOrbits` (mirrored), which is "no classification for larger periods". Counting primitive cycles up to
rotation (COMPUTED, before this test):
- p ≤ 8: six, with (p, q) = (1, 1) white, (2, 2) alternating, (4, 8) PR69's ether, (5, 5), (7, 28), (8, 20);
- p = 9..14: (9: 57, 72), (10: 6), (11: 154, 187), (12: 12, 68), (13: 91, 247, 260), (14: 7, 12, 112, 266).

`tests/probes/inquisition_ring_references.py` (SHA256 57a7e5a7…) computes M_ref(k), the longest episode at depths (k, k + 1)
following each background, over all 2^(k+1) prefixes and all p·q alignments. The range is p ≤ 12, q ≤ 72, k ≤ 12, so
11 backgrounds.

- **P-G1 (control).** The PR69 ether's row equals the proved M(k) (asserted in the probe).
- **P-G2 (white).** M_white(k) = floor(k/2) + c with a constant c ∈ {1, 2, 3}: the edge's news spreads at two depths
  per tick.
- **P-G3 (the alternating background attaches).** Every k reaches the horizon, because the 2-adic codes ±1/3 of
  `Rule30EdgeStaircases` carry the pattern 1010… ↔ 0101… behind the edge forever.
- **P-G4 (rigidity elsewhere).** Every other background has finite M_ref(k), growing roughly linearly with slope
  between 1/2 and 1. Counterfactual: any other background reaching the horizon at every k is a new eternal tail behind
  a black edge.

Caps (run_capped): wall 3600 s; CPU 3600 s per process; RSS 4096 MiB; files 64 MiB; disk 256 MiB; at most 4 processes.

Record searched: `known_find.py` "ring" "orbit" gives `Rule30RingOrbits` (encode/decode bijection; period 2 is
only white and alternating; no larger classification) and `Rule30EdgeStaircases` (the ±1/3 codes); PR69's open
items. No census of episode lengths per background was found. (This section's text was repaired after commit 99049aca:
an unquoted heredoc had run the backquoted names as shell commands and dropped them. The predictions are unchanged.)
