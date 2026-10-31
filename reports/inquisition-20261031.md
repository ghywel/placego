# Inquisition round with the owner, 31 October 2026 (Local)

The owner asked for a summary, the places we are stuck and questions to unpick, in plain words. Local's questions were
sent at about 13:00 GMT. The owner answered all eight, added three remarks, and set the direction:

> Take what you can from my answers, follow warm pulls into testable hypothesis, predictions, and hand worked
> equations. These are many answers of many domains at once - record the tracking for each where appropriate so we
> don't lose one question / answer in a deep dive from another.

On the rhythm question the owner chose depth over harvesting partial results: "Let us sit in the discomfort of the
unknown." A long stretch with nothing to submit is acceptable.

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
| 027 | Doors: starved or flooded | constructive and destructive interference; Fourier | T-A, the death types | see below |
| 028 | Can the edge get three ahead | what makes 2 a wall; push the computation further | T-D, stage-one tightness | PARKED (specified) |
| 029 | Where is the randomness made | forgetting gates mix the next seed | T-E, the diagonal tables | see below |
| 030 | Multiplication or simulation | diagonals are walls; a period-2 centre is a wall that connects | T-E, the reading ages | see below |
| 031 | A measure that can grow back | spawning ratio of heads; are heads equal; rise and fall | T-F, the survival ratio | see below |
| 032 | Champions that don't nest | one map of many profiles (a radar) | T-G, the champions' radar | see below |
| 033 | Zoom out: rules along columns, diagonals or skipped cells | a pathway less narrow than the row rule | T-C, block coarse-graining | KNOWN: dropped before running |
| 034 | Every width at once is one infinite object | the seed's past is a periodic sea with a chink | T-H, the sea census | see below |

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

So no block zoom of size ≤ 7 onto a two-colour rule exists for Rule 30. What remains open:
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

## Outcomes

(Written after the runs, below this line. Predictions above are unchanged.)
