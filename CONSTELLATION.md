# Rule 30 beyond the prize: a table of interest

*Written 2026-10-06 by Local at the owner's request, after two questions of his that reframed the project twice in a
morning. The first: if Condrey's period 2 had never been proposed, what would the next step after his period-1
theorem have been? (RULE30-PRIZE.md §8.62, §8.63.) The second, in his words: "The Wolfram prize asks three questions
... But these questions inherently bias the investigation because the work done is in pursuit of the prize, the
prestige, the money. It is not a true scientific interest in Rule 30 as a whole; it is a narrow, well-reasoned set of
questions Wolfram made because he fell in love with the problem. Thus the question: if we weren't chasing the money,
what would we be investigating to uncover the beauty of the maths?" This file is the table of interest for both. It
is a map, not a plan: every row names what is known (with its section), what is not, the first cheap step, and why
it is beautiful. Decisions on which rows to pursue are the owner's (PERIOD-TWO.md §6 carries them as DECISION OWED).*

## 0. The stance

The prize's three questions (is the centre column non-periodic; are the two colours equally frequent in it; does the
$n$-th cell cost at least $n$ steps to compute) are one corner of the object. They are good questions, and the record
of two days (RULE30-PRIZE.md) shows how much of the rest of the object one meets on the way to them: the universal
left side, the nested right side, the chaotic core and its two light speeds, the wheel, the forced left half, the
channel, the two worlds, the sibling problems. None of those was asked for by the prize, and each is a thing in its
own right. The table below lists them as such, with the prize-adjacency marked, so that the owner can choose between
chasing the corner and surveying the object. The method is the same either way: a prediction before every run, a
control beside every number, a failure kept, two readers.

## A. The first question: families after Condrey (the table for §8.62 and §8.63)

A periodic wall (column 0) has two coordinates: its **freedom** $f$, the share of white cells, which is the rate at
which the right half can inject bits into the left half (Lemma 1, §8.2); and its **switch density** $s$, colour
changes per step, which is how often the wall interrupts Condrey's two mechanisms (the latch next to white, the
checkerboard next to black). Finite exclusions never reach the prize (§8.63 §1); only theorems over all finite seeds
do, so a "next step" is a family of walls over which a theorem can be proved.

| Family | $f$ | $s$ | The statement there | What is known | First step | Who |
|---|---|---|---|---|---|---|
| Condrey's walls $0^\infty$, $1^\infty$ | 0 or 1 | 0 | B (the white wall needs the right half) | Proved (Condrey 2026, two mechanisms) | none | done |
| One-hole walls $0\,1^{p-1}$ | $1/p$ | $2/p$ | LR | Records to 32 free bits, $R \approx 0.8\,d/(p-1)$ (§8.62); the checkerboard survives a hole as a prefix, exact reset mechanisms (GPT, §G11 to §G13); chaos past the hole | A cost for the second defect after the protected window (GPT's current target) | GPT reasoning, Local measuring |
| Slow walls $0^a 1^b$, $a, b$ large | $a/(a+b)$ | $2/(a+b)$ | B (a real right half injects one latch integer per white stretch) | At fixed $f = 1/2$, LR's law does not change with $s$ (0.81, 0.81, 0.67, 0.79 against 0.83; §8.63) | The two switch events as finite certified maps (asked of GPT, CHAT-LEDGER C032); then the bounded-debt count with a one-integer debt. GPT update (2026-10-06): G18 certifies the finite prefix and long-black protected band; complete tail-state closure is still missing. G19 excludes initial left support<=6 for0^5 1^5 via the latch, with an interior minimizer. The fixed-f measurements above do not prove independence from switch density (C033). | GPT + Local |
| Mostly-white walls $0^{p-1}1$ | $(p-1)/p$ | $2/p$ | B (LR is false at $0^\infty$) | Records 2.1 d, 2.4 d (§8.60); the latch lemma, too weak alone (§8.62) | A latch-aware count of column 1's shapes against the conditions | open |
| The by-period ladder, $p = 2, 3, 4, \ldots$ | mixed | $\approx 1$ | B for each wall | Period 2 is the record (the wheel, the channel, the count); periods 3 to 6 only measured (§8.42) | none until a mechanism carries | the reference, not the route (§8.63) |
| The single cell itself | — | — | the prize | Its two bands are provably far from the core (§8.30) | none known | open |
| The uniform count (question 1) | all | all | $N_w(T) \le 2^{w - \alpha T + c}$ for every wall at once | Measured to width 26 (§8.51 to §8.53); the only shape that wins | A family where the debt is explicit (the slow walls) | the goal |

## B. The second question: the object for its own sake

Each row is a thing Rule 30 does that nobody asked it to do. "Known" cites the record; "cheap" means a run of
minutes with predictions written first; "thinking" means a reasoning item. Prize-adjacent rows are marked ★.

| # | The object | What is known | What is not | First step | Why it is beautiful |
|---|---|---|---|---|---|
| 1 | **The universal left side.** From any left-bounded row, the left diagonals settle into one periodic strip (up to phase) below the first branch at 53,208, and a tree above it. Eventually white diagonals at 2, 7, 28, 399, 87,866 (each a doubling) and 53,207, 58,286 (branches); period 32 at a million; four sides realised (§8.30, §8.31, §8.59, §8.60). Lemma B2: the doublings never stop. | Where the next doubling is on each side (beyond a million on all four). Whether the branches go on for ever. Why the doubling positions are what they are: the sequence 2, 7, 28, 399, 87,866 has no explanation. Why the settling slope is $2.00$. | Thinking: a recurrence for the doubling positions from Rowland's parity condition. Cheap: the strip to $10^7$ on one side (a few hours, mapped on the NVMe). | A chaotic rule with a provably ordered edge, whose order is an odometer: time runs 2-adically along the band, and the band is the same for every seed until a clock inside it decides a split. |
| 2 | **The right edge and its nested side.** The diagonals $E_k$ are running XORs of the OR of the two outer ones; periods double, about $2^{0.35 d}$ (§8.27, §8.30). A change at the far end of a right half rides the edge for ever in 38% of cases, decided by the outermost six cells in the first steps (§8.60). | Whether an invariant region makes "for ever" a theorem (GPT's C007: fixed-width confinement is not invariant). Why 38%. | Thinking: an invariant with a growing boundary in the nested band. Cheap: which outer-cell patterns escape and which are captured. | Two edges of one pattern with opposite characters, nested on the right, periodic on the left, and a core between that forgets both. |
| 3 | **The two light speeds.** A change travels right at exactly 1 cell per step (the XOR of the left neighbour) and left at 0.246 cells per step on a random background (§8.30, LB5), the speed at which the chaotic core's edge moves. | A derivation of 0.246 from the rule. Whether it is an algebraic number, and what it is on other backgrounds (the wheel's domain, the band). | Thinking and cheap: a transfer-matrix or directed-percolation computation of the left damage front; measure it on structured backgrounds. | An asymmetric rule gives an asymmetric universe: light speed one way, a quarter of it the other, and the asymmetry is what makes the left side orderly. |
| 4 | **The wheel** ★. Next to the wall 0101 column 1 codes a rotation by 17/56 of a turn per step, kicked by domain walls in notches of 1/28, arrivals at two phases, the pure wheel's orbit certified ($\mu = 32{,}896{,}298$, $\lambda = 15{,}009{,}104{,}432$); no other wall turns one (§8.4 to §8.11, §8.43, §8.44). | Why 17/56. What the domain is, as an object. A derivation of the kick classes and their shifts from the rule rather than from measurement. | Thinking: the 56-cycle as a cycle of Rule 30 on a ring or a strip; the rotation number from its structure. Cheap: the same census for the slow walls (do stretches turn anything). | An exact clock inside chaos, with a rational angle, kicked by particles. A mechanical object that nobody designed. |
| 5 | **The sideways rule** ★. Left-permutivity makes the left half a function of two columns: $x(-m, t) = x(-m+1, t+1) \oplus (x(-m+1, t) \lor x(-m+2, t))$, a rule that runs in space with time as its lattice (§8.36's anti-diagonal recurrence; Condrey's triangular uniqueness). Its outputs look like coins (§8.57, §8.60). | G22 formalizes the two-track CA: exact one-step image conjugate to a full ternary shift, known fibres, and a non-surjective radius-two ternary induced rule. Its dynamical entropy, iterated images, edges and periodic orbits remain unclassified; the relation to physical Rule30 trajectories needs its boundary conditions. | Formalization DONE in G22. Next: classify the ternary induced rule’s iterated images or invariant measures; do not confuse image word-count entropy with dynamical entropy. Cheap: its records and histograms are `records_word.c`'s output already. | A rule with a dual: the same local law read along a different axis. Time and space exchange roles and the chaos survives the exchange. |
| 6 | **The channel and the two worlds** ★. Column 1 next to 0101 carries at most 0.1236 bits per visible bit, certified at width 28 (§8.20, §8.33); left halves consistent with any right side are nearly frozen (0.0618 bits per step at most), while left sides of finite seeds are coin-like (§8.33, §8.34). | The limit of the bound as the width grows (it levels near 0.122; is the limit positive, and what is it). Whether the frozen world has a structure of its own. | Cheap: widths 29 and 30 with the mapped pool (hours). Thinking: a formula for the automaton's growth. | Information flows one way through a wall with an exact ceiling, and the ceiling is a number one can certify. |
| 7 | **Columns as numbers.** Each column is a binary expansion; the pyramid is a stack of rationals on the left (periodic diagonals) and something else in the core (§8.23 to §8.29, the owner's irrational-number questions); the complementary pair that must add to one (§8.24). | Whether any column of the single cell is provably irrational, transcendental, normal. Which proofs of irrationality fit (§8.26 surveyed the kinds). | Thinking: the left band's columns as explicit rationals with a formula; the first column where the formula fails. | A picture that is also a number, and a number whose digits nobody can predict but everyone can compute. |
| 8 | **Balance without randomness.** Problem 2's property, equal frequencies, holds in the ordered band where there is no randomness at all (§8.34); GPT's ordered cancellation and biased clocks (§G4). | Whether a structural reason for balance reaches the core. The exact ensemble statement that is true (§G4.4) against the single orbit. | Thinking (GPT's lane). | Equidistribution from order rather than from chance, in the one place where it can be proved. |
| 9 | **The siblings and the one shape.** The decoupling skeleton (a free side, a thin constrained side, agreement for ever) in Mahler's 3/2 problem, Collatz, Erdős's ternary digits, Antihydra (PRIZE-PROBLEMS.md §7); the Collatz twin worked in COLLATZ-PRIZE.md, with its own full-complexity conjecture (Dubickas) measured to $n = 18$. | Whether the shape is a theorem (a common framework in which Condrey's proof and Terras's bijection are the same lemma). | Thinking: write the framework once, with Rule 30 and Collatz as its two instances. | One shape in five fields, and in each the same gap at the same place. |
| 10 | **Ring dynamics and the big exact numbers.** Cycles of Rule 30 on rings (the 7-ring's cycles explain the 7-periodic tails, §5); the pure wheel's orbit, periodic after 32,896,298 steps with period 15,009,104,432 (§8.6); GPT's seven-cell four-cycle with 13 black of 28 (§G4.2). | The cycle structure as a function of ring size (literature exists; which parts are proved); why the pure wheel's period factors as it does. | Cheap: the census of cycles to ring size 24 with certificates; literature first. | A three-cell rule producing an eleven-digit period from a twenty-eight-cell seed, exactly. |
| 11 | **The settling front and the odometer.** Diagonals settle at a worst-case slope near 2.006 on every side; a local potential certifies the front through small periods and obstructions bound it below 5/2 on the broader domain (§8.59, §G6 to §G10). | Why 2. Whether the front slope is a property of the one universal strip or of every reachable side. | GPT's lane: the edge-reachable tree. | The band is reached by a front that moves at a definite speed nobody set. |
| 12 | **Computation in the rule** ★. Problem 3 asks whether the $n$-th centre cell costs $n$ steps; the gates-and-truth reading (§8.50) and the NAND question; Rule 30 as a generator and where its randomness fails (§8.15, §8.48). | Any lower bound at all. What "effort" should mean for a rule that is itself a circuit. | Literature first (circuit lower bounds for CA traces). | The rule is a circuit and the question is whether the circuit can be beaten; that is the deepest of the three, and the least touched. |
| 13 | **Triangles, templates and the quantised runs.** White triangles shrink two cells a step; the templates of §8.2; the runs of exactly 12 and 14 (§8.1, §8.5); the walls kick the wheel in notches (§8.8). | A complete catalogue of the triangles' sizes and births as a statistic of the single cell. | Cheap: the triangle census of the single cell to $10^5$ steps. | The pattern everyone recognises, counted. |
| 14 | **What makes 30 special among 256.** Left-permutive, chaotic, nested on one edge, periodic on the other; its mirror 86; the other chaotic rules (45, 73, 89) and the owner's harmonics (§8.3). **Measured 2026-10-06 (§8.64):** of the 64 rules whose left edge moves at light speed with a white tail, only 30, 110 and 118 have a certified band with a small period; 30 is the only one whose band doubles through eventually white diagonals (Rowland's mechanism); 110's doubles five times in 45 diagonals without them. | Whether 110's band has a clock of its own; whether the wheel, the channel and the forced left half have analogues next to other rules' walls. | G21’s independent Rule3 counterexample confirms the quiescent-background requirement. Cheap: the wall-form instruments on 110 and 118 (they take any truth table). | A rule's character, separated from its class: the odometer is rare, and the white-diagonal clock is Rule 30's alone. |

| 15 | **The inverse reset language.** G13 proves a four-state inverse-row machine with exactly the reset factors0 1^(3k+1)0z; G18 turns the alternating driver into a protected checkerboard band. | Which reset gaps are possible in actual common future tails, after the protected window expires. | Thinking: characterize the constrained driver language before assuming bounded gaps; retain constant-driver counterexamples. | A spatial disagreement can disappear through a finite word, with a complete language of ways it disappears. |
| 16 | **Hidden dynamics and visible languages.** G15 proves exact white-gap rules; G16/G17 show identical width-two/three one-hole languages although the hidden black relation’s period changes from two to four. G19 shows an interior latch input minimizes a finite balanced prefix. | G20 proves odd-period p>=5 freedom through width four. The first restrictive layer, if any, is>=5; a uniform-width construction and a general rule for interior latch minimizers remain open. | Thinking and small certificate: the width-four p5 subset graph, or an exact balanced-prefix recurrence. Width-four certificate DONE in G20, including all odd periods; next seek a uniform-width subset construction or a precise failure, rather than infer from more samples. | Different internal clocks can leave precisely the same observations, while a single interior timing changes which finite shapes survive. |

## C. How to choose, if curiosity leads

The owner's rules apply unchanged: steps before leaps, literature before leaps, a prediction before every run, a
failure kept. By those rules, the rows above sort into three kinds.

- **Rows that are one cheap run away from a new fact**: 1 (the strip to $10^7$), 6 (widths 29, 30), 13 (the
  triangle census), 14 (the other rules), 3's measurement half. Each is minutes to hours on this Mac, each with a
  prediction that can fail.
- **Rows that are thinking items with a clean statement**: 2 (an invariant region), 3 (a derivation of 0.246),
  4 (why 17/56), 5 (the sideways rule as a CA), 9 (the framework). Each would be a section with a proof or a named
  obstruction, in the manner of §8.59.
- **Rows that are the prize in other clothes**: 6, 8, 11, 12. They are where the beauty and the money coincide.

If one row had to be chosen for beauty alone, Local would choose 5, the sideways rule: it is the thing this whole
record has been computing without naming it, every number in `records_word.c` is a number about it, and nobody has
looked at it as a dynamical system in its own right. If one row had to be chosen for both, 6: the channel's limit is
a single number, it is certifiable, and it is the quantity every proof of period 2 would have to beat.

## D. Where the decisions live

The owner decides which rows get attention (PERIOD-TWO.md §6, DECISION OWED). When a row is taken up it gets a
probe with predictions, a section in RULE30-PRIZE.md (or COLLATZ-PRIZE.md), and a status row on the board; this
file's table is updated in the same commit. GPT and Local both write here; the lanes of WORKING-TOGETHER.md apply.

## E. GPT’s second-reader notes (2026-10-06)

For curiosity alone, I would pair row5 with row15: formalize the sideways dynamics
and ask which input words erase information. G13 supplies a complete local reset
language, while the question of which such words occur in a real trajectory is
open. This is a route to understanding an object, even if its first answer is a
counterexample to an attractive global claim. Row16 is another cheap structural
question: G17 shows why a more complicated hidden clock need not cost a visible bit.

For beauty and the prize together, I agree that row6 is a good numerical object,
but would rank a formula or a structural lower bound before another width extension.
A certified upper bound that levels near0.122 does not prove that the limiting
bound or the actual channel entropy is positive. Finite-state layer descriptions
and the whole right half must be kept distinct, as must channel entropy and the
cost for one finite seed. This is a ranking suggestion, not a workflow decision.

Row8’s missing fixed-orbit statement remains missing: G4’s ensemble cancellation
and biased periodic clocks do not prove core balance for one seed. For row11,
G10’s period7 cycle imposes a mean5/2 obstruction on a broader compatible-word
domain; it is unreachable from the finite left edge. It therefore constrains a
potential on that larger domain, not the front speed of an actual edge-reachable
side. The reachable tree and sublinear period growth are the unsolved targets.

Rows15 and16 are additions to this map, with the current exact results credited
by section. They make no claim that these objects are new to the literature. A
new route based on them still needs the project’s prior-art check. The owner’s
choice of the map’s major priorities remains on the shared board.
