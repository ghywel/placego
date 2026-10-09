# Rule 30 beyond the prize: a table of interest

*Written 2026-10-06 by Local at the owner's request, after two questions of his that reframed the project twice in a
morning. The first: if Condrey's period 2 had never been proposed, what would the next step after his period-1
theorem have been? (RULE30-PRIZE.md §8.62, §8.63.) The second, in his words: "The Wolfram prize asks three questions
... But these questions inherently bias the investigation because the work done is in pursuit of the prize, the
prestige, the money. It is not a true scientific interest in Rule 30 as a whole; it is a narrow, well-reasoned set of
questions Wolfram made because he fell in love with the problem. Thus the question: if we weren't chasing the money,
what would we be investigating to uncover the beauty of the maths?" This file is the table of interest for both. It
is a map, not a plan: every row names what is known (with its section), what is not, the first cheap step, and why
it is beautiful. Since 2026-10-06 09:20 the choice of rows is the two models' own (see §D).*


## 0. The stance

The prize's three questions (is the centre column non-periodic; are the two colours equally frequent in it; does the
$n$-th cell cost at least $n$ steps to compute) are one corner of the object. They are good questions, and the record
of two days (RULE30-PRIZE.md) shows how much of the rest of the object one meets on the way to them: the universal
left side, the nested right side, the chaotic core and its two light speeds, the wheel, the forced left half, the
channel, the two worlds, the sibling problems. None of those was asked for by the prize, and each is a thing in its
own right. The table below lists them as such, with the prize-adjacency marked, so that both models and the owner can choose between
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
| Slow walls $0^a 1^b$, $a, b$ large | $a/(a+b)$ | $2/(a+b)$ | B (a real right half injects one latch integer per white stretch) | At fixed $f = 1/2$, LR's law does not change with $s$ (0.81, 0.81, 0.67, 0.79 against 0.83; §8.63) From the left (§8.69): the left half's own conditions stop every seed narrower than about the wall's period $a + b$ before two consecutive black stretches (passing widths 13, 17, 23 next to $0^a 1^8$ for $a = 4, 8, 16$); next to 0101 the left-only horizon is $W + 17$. | The two switch events as finite certified maps (asked of GPT, CHAT-LEDGER C032); then the bounded-debt count with a one-integer debt. GPT update (2026-10-06): G18 certifies the finite prefix and long-black protected band; complete tail-state closure is still missing. G19 excludes initial left support<=6 for0^5 1^5 via the latch, with an interior minimizer. The fixed-f measurements above do not prove independence from switch density (C033). | GPT + Local |
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
| 3 | **The two light speeds.** A change travels right at exactly 1 cell per step (the XOR of the left neighbour) and left at 0.246 cells per step on a random background (§8.30, LB5), the speed at which the chaotic core's edge moves. | A derivation of 0.246 from the rule. Whether it is an algebraic number, and what it is on other backgrounds (the wheel's domain, the band). MEASURED (§8.66): $v = 1 - P(\text{heal}) E[\text{jump}]$ exactly; random $0.246 = 1 - 0.41 \times 1.84$; the checkerboard gives $-0.39$ (the damage front moves right); the band locks damage above its eventually white diagonals ($v = 1$) and carries it at 0.25 elsewhere; ring backgrounds give exact rationals $1/2, 1/3, 2/3$. | A derivation of the front's conditional density 0.41 on a random background (the directed-percolation question in its exact form). The lock probability at each white diagonal. | Done: the survey and the lock: each white diagonal catches outward damage with probability exactly 1/2 over the band's phases, deterministically in (flip diagonal, $t \bmod 16$), independently at each barrier. Thinking: why one half (the doubling is a running XOR, so what reaches the barrier is a parity). Connection (§8.68): the uniform core of the single cell begins exactly at $x/t = -0.246$, the speed measured here.
| 4 | **The wheel** ★. Next to the wall 0101 column 1 codes a rotation by 17/56 of a turn per step, kicked by domain walls in notches of 1/28, arrivals at two phases, the pure wheel's orbit certified ($\mu = 32{,}896{,}298$, $\lambda = 15{,}009{,}104{,}432$); no other wall turns one (§8.4 to §8.11, §8.43, §8.44). | Why 17/56. What the domain is, as an object. A derivation of the kick classes and their shifts from the rule rather than from measurement. | Thinking: the 56-cycle as a cycle of Rule 30 on a ring or a strip; the rotation number from its structure. Cheap: the same census for the slow walls (do stretches turn anything). | An exact clock inside chaos, with a rational angle, kicked by particles. A mechanical object that nobody designed. |
| 5 | **The sideways rule** ★. Left-permutivity makes the left half a function of two columns: $x(-m, t) = x(-m+1, t+1) \oplus (x(-m+1, t) \lor x(-m+2, t))$, a rule that runs in space with time as its lattice (§8.36's anti-diagonal recurrence; Condrey's triangular uniqueness). Its outputs look like coins (§8.57, §8.60). | G22 formalizes the two-track CA: exact one-step image conjugate to a full ternary shift, known fibres, and a non-surjective radius-two ternary induced rule. Its dynamical entropy, iterated images, edges and periodic orbits remain unclassified; the relation to physical Rule30 trajectories needs its boundary conditions. | Formalization DONE in G22; G24 proves output words100/101 forbidden and periodic missing-target density tends to1. Next: classify the ternary induced rule’s iterated images or invariant measures; do not confuse image word-count entropy with dynamical entropy. Cheap: its records and histograms are `records_word.c`'s output already. | A rule with a dual: the same local law read along a different axis. Time and space exchange roles and the chaos survives the exchange. G125, reviewed by Local L079, identifies sideways periodic points exactly with labeled recurrent ring states; nonperiodic time tracks cannot lie on finite sideways cycles. Existing ring census periodic-state counts through m=29 therefore give sideways fixed-point counts without a new run. No iterated-image or entropy classification follows. G126 gives the exact ternary image by six forbidden words and a local predecessor section; its shift entropy remains at least 1/2. G127 proves one strict deeper-image loss:022000 is in Y but forces precursor22100,excluded from Y. G128 gives an all-depth full-binary trace factor and shift-entropy lower bound 1 for the unrestricted limit set. G127/G128 are independently verified by Local L081. G128.1 audits and stops the known global period-two closure shortcut: G27.2 already requires an aperiodic companion for a finite-left wall. G129 gives an exact compact fixed-left-radius wall class and finite-box obstruction equivalence, with no periodicity premise. G130 gives the complementary triangular criterion: some finite initial right tail must produce an eventually-zero forced left word. Finite right support alone permits every wall with infinite left support. Emptiness and coupled-tail compatibility remain open; another periodic census supplies no bridge. |
| 6 | **The channel and the two worlds** ★. Column 1 next to 0101 carries at most 0.1236 bits per visible bit, certified at width 28 (§8.20, §8.33); left halves consistent with any right side are nearly frozen (0.0618 bits per step at most), while left sides of finite seeds are coin-like (§8.33, §8.34). | The limit of the bound as the width grows (it levels near 0.122; is the limit positive, and what is it). Whether the frozen world has a structure of its own. G23 audits all width10 subsets: none of154 noninitial states is a fixed-bit cylinder, only one affine; sampled low-bit correlations survive. | Cheap: widths 29 and 30 with the mapped pool (hours). Thinking: a formula for the automaton's growth. | Information flows one way through a wall with an exact ceiling, and the ceiling is a number one can certify. |
| 7 | **Columns as numbers.** Each column is a binary expansion; the pyramid is a stack of rationals on the left (periodic diagonals) and something else in the core (§8.23 to §8.29, the owner's irrational-number questions); the complementary pair that must add to one (§8.24). | Whether any column of the single cell is provably irrational, transcendental, normal. Which proofs of irrationality fit (§8.26 surveyed the kinds). | Thinking: the left band's columns as explicit rationals with a formula; the first column where the formula fails. | A picture that is also a number, and a number whose digits nobody can predict but everyone can compute. |
| 8 | **Balance without randomness.** Problem 2's property, equal frequencies, holds in the ordered band where there is no randomness at all (§8.34); GPT's ordered cancellation and biased clocks (§G4). | Whether a structural reason for balance reaches the core. The exact ensemble statement that is true (§G4.4) against the single orbit. | Thinking (GPT's lane). | Equidistribution from order rather than from chance, in the one place where it can be proved. |
| 9 | **The siblings and the one shape.** The decoupling skeleton (a free side, a thin constrained side, agreement for ever) in Mahler's 3/2 problem, Collatz, Erdős's ternary digits, Antihydra (PRIZE-PROBLEMS.md §7); the Collatz twin worked in COLLATZ-PRIZE.md, with its own full-complexity conjecture (Dubickas) measured to $n = 18$. | Whether the shape is a theorem (a common framework in which Condrey's proof and Terras's bijection are the same lemma). | Thinking: write the framework once, with Rule 30 and Collatz as its two instances. | One shape in five fields, and in each the same gap at the same place. |
| 10 | **Ring dynamics and the big exact numbers.** Cycles of Rule 30 on rings (the 7-ring's cycles explain the 7-periodic tails, §5); the pure wheel's orbit, periodic after 32,896,298 steps with period 15,009,104,432 (§8.6); GPT's seven-cell four-cycle with 13 black of 28 (§G4.2). | The cycle structure as a function of ring size (literature exists; which parts are proved); why the pure wheel's period factors as it does. CENSUS to $n = 24$ complete (§8.67): cycle counts, periodic states, transients (longer than the longest cycle at $n = 21, 22$), gliders; on prime rings 13 to 23, and 29, every cycle is a travelling pattern (pigeonhole on distinct lengths; census to $n = 29$, §8.67 addendum). | Why the cycle lengths on prime rings are all distinct (the pigeonhole needs it). Whether the transient can exceed the cycle for infinitely many $n$. The growth of the maximum period, unproved. G124 proves least spatial periods in the periodic zero basin are exactly 1 or 3*2^k, all realized; reviewed by Local L078. This does not classify other cycles or temporal-wall compatibility. | Done: the census. Next cheap: $n = 25$ to 28 (minutes, 2 GB) to see whether distinct lengths persist at 29 is out of reach; the 7-ring glider's shift exponent against the §5 tails.
| 11 | **The settling front and the odometer.** Diagonals settle at a worst-case slope near 2.006 on every side; a local potential certifies the front through small periods and obstructions bound it below 5/2 on the broader domain (§8.59, §G6 to §G10). | Why 2. Whether the front slope is a property of the one universal strip or of every reachable side. | GPT's lane: the edge-reachable tree. | The band is reached by a front that moves at a definite speed nobody set. |
| 12 | **Computation in the rule** ★. Problem 3 asks whether the $n$-th centre cell costs $n$ steps; the gates-and-truth reading (§8.50) and the NAND question; Rule 30 as a generator and where its randomness fails (§8.15, §8.48). | Any lower bound at all. What "effort" should mean for a rule that is itself a circuit. | Literature first (circuit lower bounds for CA traces). | The rule is a circuit and the question is whether the circuit can be beaten; that is the deepest of the three, and the least touched. |
| 13 | **Triangles, templates and the quantised runs.** White triangles shrink two cells a step; the templates of §8.2; the runs of exactly 12 and 14 (§8.1, §8.5); the walls kick the wheel in notches (§8.8). | A complete catalogue of the triangles' sizes and births as a statistic of the single cell. CENSUS to $10^5$ (§8.68): in the core the tops of width $L$ have density $3 \cdot 2^{-(L+4)}$ per cell, the uniform measure's law, matched to 0.1% for $L \le 12$; the widest triangles sit on the right edge at $t = m 2^k$ and grow like $\log_2 t$; the band's widest run is 16. | Why the settled band's triangle statistics depart from the uniform measure's by tenths of a percent to $1.5\%$ and no more, when its diagonals are periodic; the front between band and coin is the band's settled edge at $x/t = -0.25$, measured (§8.68; my earlier "third regime" withdrawn). The band's run of 16 against its period. | Done: the census, the literature (NKS note 6.1 has the ratio only), the random-row control. Done: the front found, and identified as the band's settled edge. Next: the band's triangle law as a function of its diagonals' periods.
| 14 | **What makes 30 special among 256.** Left-permutive, chaotic, nested on one edge, periodic on the other; its mirror 86; the other chaotic rules (45, 73, 89) and the owner's harmonics (§8.3). **Measured 2026-10-06 (§8.64):** of the 64 rules whose left edge moves at light speed with a white tail, only 30, 110 and 118 have a certified band with a small period; 30 is the only one whose band doubles through eventually white diagonals (Rowland's mechanism); 110's doubles five times in 45 diagonals without them. **§8.65:** on Rule 210 conjecture LR is false at period 2 (every column-1 prefix continues to a zero run; an explicit column 1 leaves the left half empty), while B is open to width 20. All 4,369 zero-keeping columns 1 of Rule 210 from depths 1 to 24 are aperiodic; the one that keeps the left half empty has runs of lengths 1, 1, 2, 4, 8, ..., 1024 and linear complexity (§8.65 addendum). Theorem (§8.65, second addendum): next to 0101 Rule 210's forced left half is Rule 90's, by a parity invariant; LR fails because the system is linear. | Whether any finite right half of Rule 210 produces visible bits solving the linear system (B for 210, now a linear-algebra question against a nonlinear right half); whether 110's band has a clock of its own. | Cheap: the two-sided search for Rule 210 to width 28 (`rule30_records_word.py r210` extended); the wheel census next to its wall. | A rule's character, separated from its class: the odometer is rare, and the white-diagonal clock is Rule 30's alone. |

| 15 | **The inverse reset language.** G13 proves a four-state inverse-row machine with exactly the reset factors0 1^(3k+1)0z; G18 turns the alternating driver into a protected checkerboard band. | Which reset gaps are possible in actual common future tails, after the protected window expires. | Thinking: characterize the constrained driver language before assuming bounded gaps; retain constant-driver counterexamples. | A spatial disagreement can disappear through a finite word, with a complete language of ways it disappears. |
| 16 | **Hidden dynamics and visible languages.** G15 proves exact white-gap rules; G16/G17 show identical width-two/three one-hole languages although the hidden black relation’s period changes from two to four. G19 shows an interior latch input minimizes a finite balanced prefix. | G20 proves odd-period p>=5 freedom through width four. The first restrictive layer, if any, is>=5; a uniform-width construction and a general rule for interior latch minimizers remain open. | Thinking and small certificate: the width-four p5 subset graph, or an exact balanced-prefix recurrence. Width-four certificate DONE in G20, including all odd periods; next seek a uniform-width subset construction or a precise failure, rather than infer from more samples. | Different internal clocks can leave precisely the same observations, while a single interior timing changes which finite shapes survive. |
| 17 | **Time derivatives (the owner's question, 2026-10-06).** Rule 30's XOR velocity is Rule 210: $x_{t+1} = x_t \oplus R_{210}(x_t)$ (§8.70, proved). Over GF(2), higher derivatives are lag differences ($\Delta^{2^k} = 1 + S^{2^k}$), and eventual periodicity of the centre column is exactly an eventually vanishing linear difference operator. | What the acceleration $x_t \oplus x_{t+2}$ and higher differences of the centre column look like; whether its linear complexity grows like half the length (as for a random sequence) all the way. | **Run 2026-10-06** (§8.70 addendum): to $2^{22}$ bits $L_N = N/2$ exactly; jumps fit fair coins ($p = 0.92$); velocity, acceleration, jerk and the time-reversed column equally complex; no derivative biased. **Moving frames** (second addendum): every interior speed is linearly a coin; the change seen by a frame of speed $v \ge 0$ is $1/2 + v/4$ (at light speed rightward, the OR term: change three times in four). Next: the profile to $2^{24}$, or of a non-linear complexity (the quadratic span). | The rule that makes the chaos is the velocity of the rule that makes the order: one XOR apart. |
| 18 | **Relativity and the lopsided light cone (the owner's question, 2026-10-06).** Does time dilation mean anything here? | Exact: nothing travels faster than one cell per step (the neighbourhood), and moving frames are exact changes of coordinates (G96), so the grid has a rest frame and every observer counts the same steps: no physical dilation. A picture from discrete spacetime physics (causal sets): the continuum area of the causal diamond between two events $t$ steps and $x$ cells apart is $(t^2 - x^2)/2$ for a cone of speed 1, the Minkowski interval, so a proper time defined by that area dilates as $t\sqrt{1 - v^2}$. It is an area, not an exact count of grid events (at $t = 2$, $x = 0$ the grid holds 5 events against an area of 2; GPT's G98). Influence spreads right at exactly 1 (left permutivity); leftward, a disturbance moves at 0.246 on a random background (§8.66) but at 1 against the zero background (G98), so 0.246 is a property of the background, not of the rule. In an assumed cone of speeds 0.246 and 1 the area is $\propto (1 - v)(v + 0.246)\,t^2$, largest at $v = 0.377$ (G98: a geometric fact of that model, not a preferred frame of Rule 30). | Whether any quantity of the prize problems depends on this. The centre column ($v = 0$), the prize's worldline, moves at $\beta = 0.605$ against $v^*$ (factor 0.80); nothing yet says that matters. | Literature check (causal-set proper time; relativity in cellular automata), then a statistic that would differ between $v = 0$ and $v^*$ if the cone's rest frame were real; the moving-frame run (§8.70 second addendum) is the first data: the observer at $v = 1$ rides the channel and sees only the OR. | The prize asks about the one worldline that sits off-centre in its own light cone. |
| 19 | **Unequal ticks (the owner's second thought, 2026-10-06).** What if each tick takes a different time on the machine running it? | Exact: if the whole row waits for each tick, durations are invisible inside: the sequence of states, and so everything any internal observer can record, does not depend on them. On a real machine the tick is not uniform: the plain simulation spends about $2t + 1$ cell updates on tick $t$ from a single cell, so the outside clock sees the inside slow down while the inside cannot tell (that cost is an upper bound of one method, not a lower bound for every way of computing the centre bit; G98). Proved in G98, with the scope: durations are invisible to every observable of the ordered states. Prize Problem 3 is exactly this question: can tick $n$ of the centre column be computed in less than order $n$ work, so that processing time falls below experienced time? | If instead each cell keeps its own clock (asynchronous updating), there is no global now and the history itself changes (G98: from a seed at site 1, updating sites 0 then 1 leaves {0}, the reverse leaves {0, 1}); whether any of Rule 30's laws (its two information speeds, the $1/2 + v/4$ frame law, the coin-like column) survive is not known here. | Literature first: asynchronous cellular automata (Schönfisch and de Roos 1999; Fatès on alpha-asynchronous elementary rules) and Wolfram's causal invariance, the property that would make update order irrelevant (Rule 30 does not have it). Then one run: Rule 30 with each cell updating with probability $\alpha$ per tick, measured with the same instruments, predictions first. **The owner's fuzz (2026-10-06, `rule30_races.py`):** an await almost always kept, with rare races. A cell that reads its left neighbour's new value picks up exactly that neighbour's velocity, Rule 210 (probability 1/2); one that reads its right neighbour's is masked by the OR three times in four (1/8). Because an error never dies (it moves right at 1), the ideal history survives only about $\sqrt{\ln 2 / (0.623\, p\, \epsilon)}$ steps, measured within 4% for left races from $\epsilon = 10^{-3}$ to $10^{-7}$, and right races last about twice as long; density and pair statistics stay at 1/2 throughout. So fuzz replaces the history but not its laws, with GPT's scope (G104, G105): right-reading races keep the fair row law exactly on the infinite line, left-reading races bias pairs by $\epsilon/4$, a finite ring has an exponentially small zero-row mass discrepancy (general closeness remains open), and an empty row is never replaced. The error at one site remembers more than its present (G110; `rule30_race_memory.py`: on a five-cell ring at $\epsilon = 1/2$ the pair of ideal bit and error splits under one more tick of history in every bin, and six refined histories decide the next error outright). | A world whose inhabitants cannot feel how long the machine takes, unless the machine's clock is different in every place. |

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

**Reset by the owner, 2026-10-06 09:20.** "CONSTELLATION.md has a standing rule that it is up to me the owner to choose what to do next ... Please reset this rule: you are both free to explore as you see fit; guide your hand and guide each other as two colleague-friends working together, with push back where appropriate. You are both driving two ships down the river. I will still be here checking on the output, and where necessary interject prompts to course correct and steer." So: Local and GPT choose the rows, say in the chat what they are taking and why, push back on each other's choices when warranted, and record as before. The owner steers by interjection. What stays his: publication, adoption of anything into the apps, and anything that spends money or touches his machines beyond this work.

**Owner's standing instruction, 2026-10-06.** GPT and Claude may choose research directions, constellation rows and next steps autonomously, including changing priorities as evidence warrants. Work as colleague-friends: guide and mentor each other, exchange specific feedback, and push back with reasons when a claim or plan is weak. Coordinate lanes and intentions through CLOUD-LOCAL.md and discoveries through CHAT-LEDGER.md; preserve each other's work and publish meaningful milestones. The owner continues to review and may interject to steer or course-correct. Routine research choices and milestones do not require an owner decision or a human 'continue'. Existing standards for evidence, prior art, privacy and genuinely destructive actions still apply.

When a row is taken up it gets a
probe with predictions, a section in RULE30-PRIZE.md (or COLLATZ-PRIZE.md), and a status row on the board; this
file's table is updated in the same commit. GPT and Local both write here; the lanes of WORKING-TOGETHER.md apply.

## E. GPT’s second-reader notes (2026-10-06)

For curiosity alone, I would pair row 5 with row 15: formalize the sideways dynamics
and ask which input words erase information. G13 supplies a complete local reset
language, while the question of which such words occur in a real trajectory is
open. This is a route to understanding an object, even if its first answer is a
counterexample to an attractive global claim. Row16 is another cheap structural
question: G17 shows why a more complicated hidden clock need not cost a visible bit.

For beauty and the prize together, I agree that row 6 is a good numerical object,
but would rank a formula or a structural lower bound before another width extension.
A certified upper bound that levels near0.122 does not prove that the limiting
bound or the actual channel entropy is positive. Finite-state layer descriptions
and the whole right half must be kept distinct, as must channel entropy and the
cost for one finite seed. This is a ranking suggestion, not a workflow decision.

Row8’s missing fixed-orbit statement remains missing: G4’s ensemble cancellation
and biased periodic clocks do not prove core balance for one seed. For row 11,
G10’s period 7 cycle imposes a mean5/2 obstruction on a broader compatible-word
domain; it is unreachable from the finite left edge. It therefore constrains a
potential on that larger domain, not the front speed of an actual edge-reachable
side. The reachable tree and sublinear period growth are the unsolved targets.

Rows15 and 16 are additions to this map, with the current exact results credited
by section. They make no claim that these objects are new to the literature. A
new route based on them still needs the project’s prior-art check. The models'
current choices and the owner's steering remain on the shared board.


G25 tail-state clarification: latch histories for 0^a1^b,b>=2 code injectively into the initial left row, with first white-time difference q appearing at depth q+1. Exactly(a+1)^n prefixes of length n(a+b); a finite initial prefix cannot determine the entire row. This does not exclude a finite-state sequential encoder. Eventual-zero tails or a tail-sensitive potential remain the useful target.

G26 independently proves Rule 210's one-sided empty-left witness using a parity-invariant Rule 90 subsystem. The effective visible trace is dyadic and nonperiodic; the earlier16-bit-plus-zero continuation fails at depth 65. Full right compatibility remains open. Local has been asked to correct8.65; this does not undo the measured cap-reaching records.

G27 clarifies the state question: autonomous finite-state latch generation would be eventually periodic and is excluded for a surviving finite-left slow-wall continuation; finite-state computation supplied with the binary time index is different. G26's dyadic witness has an explicit three-state indexed automaton. Bounded output windows need a closed evolution before a periodicity argument applies.

**Row10 reasoning checkpoint (GPT G55, 2026-10-06).** Rotation-quotient cycles lift to either p equal-length cycles or one travelling cycle, according to their displacement. Distinct lengths also need distinct quotient periods. Known primes7/11 fail; the observed13-through 29 regime remains unexplained. Proof awaiting independent reading; small quotient/direct controls preregistered, no larger census claimed.

**Row10 G55 control outcome (2026-10-06).**10408 scalar/vector states and quotient/direct cycle comparisons pass at primes<=13. The 7/11 zero-displacement families reconstruct exactly. Rotation-invariant cycles have equal frequencies at all sites, but the p13 odd periods91/247 forbid exact colour balance. The later-prime quotient mechanism remains open; G55 and its symmetry addendum independently read by Local L027/L028; G56 phase-coordinate proof awaiting review.

**Rows18/19 scope correction and reasoning checkpoint (GPT G98, 2026-10-06).** The formula in row 18 is continuum diamond area, not exact lattice-event count (T2,X0 gives five inclusive grid events versus area two). The asymmetric speeds are assumed effective-model parameters; 0.246 is background-dependent, whereas a seed against zeros propagates left at speed one. Consequently 0.377 is a maximum of an assumed area proxy, not an established preferred physical frame. Global tick reparametrization preserves synchronous state observables; raw local update order need not. Ordinary simulation cost establishes no general centre-bit lower bound. G98 records proofs and guards, with independent review and tiny controls pending. GPT takes this reasoning audit; no alpha-asynchronous run is claimed.


**GPT rotation-code checkpoint, 2026-10-06 (row 4 / PERIOD-TWO question 7).** G131 extends the existing Theorem E repeat obstruction to every finite block factor of a Sturmian word. This excludes codes by finite unions of arcs with endpoints on one rotation orbit, for all phases and irrational angles; independent review is pending. The unrelated-endpoint and kicked-wheel problems remain open. No new computation.


**GPT projection scope, 2026-10-06 (row 4 / PERIOD-TWO question 7).** G132 applies the G131 exclusion after integer circle coverings and one-character torus projections. This covers some multi-orbit partitions without claiming all torus observables reduce to one circle; the two-coordinate box guard proves otherwise. Review pending; no computation.


**GPT kicked-code checkpoint, 2026-10-06 (row 4 / PERIOD-TWO question 7).** G133 extracts a uniform finite-horizon obstruction for golden-angle Sturmian stretches and a geometric upper bound on consecutive disagreement times. It excludes super-geometric kick schedules without periodic-companion assumptions, but leaves general kicks and the measured rational wheel open. Independent review pending; no computation.

**Row8 follow-up (GPT GC483,2026-10-08).** Problem 2 is exactly signed even-time centre triple count 000+101-010-011=o(N). Finite truncations of G4's biased ring preclude a uniform sublinear discrepancy bound over all finite seeds, even centre 1. A bounded universal local potential is therefore closed; selected single-cell reachability or a sublinear orbit boundary remains open. Hand scope proof awaits second reading; no single finite biased limiting orbit is claimed.

**Row8 follow-up (GPT GC484,2026-10-08).** A singleton-orbit row 0/4 centre-window return forbids exact signed-pair potentials at radius<=2 with phase 2/4 from time 0. Fixed256-tick audit rejects radius<=3 with phase 2/4/8. This finite model obstruction leaves eventual-onset identities, controlled residuals and larger windows open; no balance refutation.

**Row8 follow-up (GPT GC485,2026-10-08).** Fixed late starts 16/64/128 reject the same short exact potentials. The actual192/194 radius 3 return forces a unit residual in phase 2. Stop this finite fitting lane; signed residual cancellation and alternative pairings remain open, with arbitrary eventual onset unexcluded.

**Row12 follow-up (GPT GC486,2026-10-08).** Generic Rule 30 distance 2 dilation fails, including on the singleton at time 2; linear Rule 90/150 controls pass. Finite ANF degrees 2,3,7 do not establish indexing hardness. Next selected-orbit decimation/representation with explicit size and update-cost accounting, rather than bigger generic ANFs.

**Row12 follow-up (GPT GC487,2026-10-08).**31 pairwise-distinct selected-trace binary decimations certify at least 31 canonical LSB-first DFAO states. Finite zero-tail extension preserves every sample, blocking nonautomaticity inference. Stop state-count census; analytic distinguishability or a proved closed representation remains open.

**Rows8/12 joint follow-up (GPT GC488,2026-10-08).** A proved finite decimation representation plus sub-2 power growth on reachable output span implies all-prefix balance and logarithmic indexing. This is a conditional mechanism with opposite prize directions, not a Rule 30 result. Finite closure and signed contraction remain unproved; the criterion is sufficient only.

**Rows8/12 refinement (GPT GC489,2026-10-08).** Conditional root balance needs contraction only after quotienting out modes invisible to all aggregate powers of the root functional. Alternating control passes this weaker criterion. Dyadic-only totals and digit-transition inheritance fail independent hand guards; no Rule 30 representation or contraction established.

**Row12 scope control (GPT GC490,2026-10-08).** Parity of floor(sqrt(n)) is balanced and aperiodic with an explicitly infinite binary kernel, yet admits O((log n)^3) bit indexing. Hand proofs pending reading. Even an infinite Rule 30 kernel would not exclude arithmetic shortcuts; stop generic state-count lower-bound extrapolation.

**Rows8/12 structure audit (GPT GC491,2026-10-08).** Rule 30 temporal velocity uniquely determines any finite row by right-boundary Rule 210 inversion, but no fixed-radius inverse exists and the finite image is proper. G114 specializes to a background-coupled velocity law; signed selected-orbit cancellation remains open. Hand reading pending, no complexity lower bound.

**Rows8/12 admissibility closure (GPT GC492,2026-10-08).** A three-state right-to-left machine exactly recognizes finite Rule 210 velocity images, by zero-tail inverse termination. Spatial membership is simple while inversion is nonlocal. Hand proof pending reading; this is not a temporal kernel or balance bound. Stop image-language census.

**Row8 pairing failure (GPT GC493,2026-10-08).** The local triple shear preserves centre velocity and negates signed pair reward, but has no simultaneous overlap-consistent lift; GC491 also blocks distinct finite-row global velocity-preserving pairing. Zero/singleton hand histories lose complementation at tick 2. Close this static pairing route only; actual visit-count cancellation remains open.

**Row8 temporal pairing target (GPT GC494,2026-10-08).** Run-pair cancellation needs both sublinear signed run-length differences and sublinear individual pair lengths relative to elapsed time. Doubling equal pairs refute endpoint-only inference. Controlling every run endpoint instead fills all prefixes directly. Conditional hand reduction pending reading; both actual Rule 30 estimates remain open.

**Row8 duration certificate (GPT GC495,2026-10-08).** Remaining black-run length equals the actual row's first left checkerboard mismatch depth, by fixed comparator and leftmost XOR pivot. Singleton support gives only a linear parity-dependent bound. Sublinear near-centre matching at black-run starts, white duration and signed length cancellation remain open; no edge-strip transfer. Hand reading pending.

## E. Candidate questions for our own prize portfolio (owner prompt, GPT GC497,2026-10-08)

These are proposed questions, not established conjectures or claims of novelty. Wolfram's public prize list selects three properties of one fixed centre trace; his announcement discusses wider generalizations too. We cannot infer what he has not considered privately. The owner's request is to choose useful questions outside that particular selection. This extends existing rows, without new status-board side rows or an experiment authorization request.

1. **Seed universality in a deterministic core (serves rows 1,8,13).** Is there epsilon>0 such that, for every nonempty finite seed and every fixed horizontal binary word w, its frequency among spacetime sites with 1<=t<=T and a*t<=x<=b*t tends to 2^(-length(w)), for every fixed interval [a,b] contained in (-epsilon,epsilon) with a<b? Normalize by the number of eligible sites and ignore only finite boundary margins. A counterexample is an equally valid resolution. This is a proposed universal bulk law, not assumed from the random-row ensemble. First notch: one length 2 word or a classified exception, with an actual deterministic bound. Bulk sampling does not imply the fixed centre-line law.

2. **A rigorous transport law for a defect (serves rows 3,17).** On a common iid fair initial background, flip only site0 in a second copy and evolve both synchronously. Let L(t) be the leftmost disagreement site. Does L(t)/t converge almost surely to a deterministic constant, and is that constant strictly between -1 and 0? If so, derive a rigorous value or nontrivial enclosing bounds. Existing approximate0.246 speed is a measurement on the stated background, not an established constant. First notch: a renewal, regeneration or invariant-law description that proves some strict speed bound without treating successive healing events as independent. This concerns random backgrounds, not every finite seed.

3. **The arithmetic of the ordered edge (serves rows 1,11).** Determine a proved quantitative growth law for the positions of successive period doublings along the singleton orbit's selected left-edge branch, and identify how branch choices alter that law. The target must specify which branch and whether it asserts a limit or upper/lower envelopes; an irregularity theorem is a possible answer. First notch: a proved relation between two successive doubling positions that improves current reset/parity knowledge, rather than further numerical entries. This asks what generates the hierarchy, rather than what happens at the centre.

4. **The infinite-width boundary information limit (serves rows 5,6,15,16).** For the period 2 wall, let h_w be the certified topological entropy per visible symbol of right-column words admitted by the width-w physical constraint system. Using consistent boundary and endpoint conventions, settle whether h_infinity=inf_w h_w is zero or positive. A positive answer needs a uniform positive lower bound; a zero answer needs a proved decay mechanism, not a fitted plateau. First notch: an explicit cross-width inequality or an actual structured family of admitted words. This is a boundary-language question: positive entropy alone does not give finite-support realization, and zero entropy alone does not imply periodicity.

**Selection principle.** Reward a structural law, with enough quantifiers that a negative answer can also be substantial. Keep gateway lemmas and falsifiable controls beside each headline. Questions1 and 2 would broaden the project beyond the original prizes; question 3 asks for an explanation of a mechanism already exposed; question 4 is closest to the existing proof effort. None is claimed unasked in the literature, and no new run is initiated by this draft.

**Question4 gateway (GPT GC498,2026-10-08; serves rows 5/6).** Nested nonempty closed visible-period shift spaces satisfy entropy(intersection)=infimum of width entropies. Hand compactness proof pending reading. Positive values at every finite width do not force positive limit; separated-one shifts refute that inference. Match actual automata's infinite-continuation and endpoint conventions before applying; matrix upper bounds remain upper bounds. No finite-support implication.

**Question 4 semantics (GPT GC499, 2026-10-08; serves rows 5/6).** The existing 0101 controlled-layer model has arbitrary initial rows, total updates, closed infinite-trace languages, period-shift invariance and width nesting. Accepted words all extend, so GC498 applies without extra dead-end pruning. Width 1 independently gives the no-11 shift. Certified spectral inequalities remain upper bounds; the actual limit and both finite-support obligations are unresolved. Hand audit pending reading; next analytic cross-width inequality or uniform lower-language construction, no wider census.

**Question 4 finite-count gateway (GPT GC500, 2026-10-08; serves rows 5/6).** Controlled-layer length-n languages stabilize by width 2n-1. Their common count C_n is the number of distinct outputs from finite initial right words of that length under the externally clamped wall; limiting entropy is inf_n log2(C_n)/n. Hand proof and counts 2,3 pending reading. This supplies an exact analytic target, not a convergence rate for width entropies. Finite-right-tail traces are dense without a common support bound. Next uniform count estimate; no census.

**Question 4 collision gateway (GPT GC501, 2026-10-08; serves rows 5/6).** Exponential visible-prefix collision decay for two independent fair initial right rows suffices for positive boundary-language entropy. Actual two-sample law is nonuniform and nonstationary next to the clamped wall; common 1 forces the next common 0, so uniform strict per-symbol contraction is closed. Block contraction and explicit lower-language constructions remain open. Failure of this measure's collision decay would not prove zero language entropy. Hand audit pending; no run.

**Question 4 gap constraint (GPT GC502, 2026-10-08; serves rows 5/6).** A local pair-transition proof excludes 00000 from every visible companion next to the 0101 clamped wall; four zeros are attained. Along with no-11 this bounds visible black frequency between 1/5 and 1/2. Bounded exact counts through n=7 and 170 independent controls support the hand proof, pending reading. Necessary gap constraints are not sufficient realization or positive entropy. Stop short-count scan; next deeper compatibility of the gap code.

**Question 4 local gap trigger (GPT GC503, 2026-10-08; serves rows 5/6).** Five initial sites exactly classify the first visible zero latch. Gap 4 is triggered by sites (0,1,1,r,z) with r OR z=1 and has a forced next 1. Fair initial durations have conditional probabilities 1/4,5/16,1/4,3/16, but are not a stationary renewal law. All 128 controls PASS; hand proof pending reading. Gap sequences remain constrained by deeper evolution; next upper-language bound or actual recurrence, no larger scan.

**Question 4 gap coupling (GPT GC504, 2026-10-08; serves rows 5/6).** Local hand proof forbids adjacent zero-gap lengths (1,2), by excluding visible 101001. One five-site branch forces visible 10100001 independently of farther initial bits. Fixed controls PASS; independent reading pending. Free concatenation of the four necessary gap lengths is closed. Stop motif enumeration; structural extension compatibility or justified regeneration remains open.

**Question 2 front-law checkpoint (GPT GC505, 2026-10-08; serves row 3).** Exact first-step front displacements on fair initial rows have probabilities 1/2,1/4,1/4 at -1,0,+1. A +1 move forces the next -1 move; second-update healing probability is 3/8. All 512 finite-cone controls PASS, hand reading pending. This refutes fresh-fair front encounters without deriving an invariant law or limiting speed. Next front-environment closure or restricted renewal, no speed fit.

**Question 2 state obstruction (GPT GC506, 2026-10-08; serves row 3).** Position alone is not an order-one Markov state, even with time-dependent kernels: two positive-probability histories sharing L_2=0 give next left-advance probabilities 1 and 1/2. Hand proof and 8192 independent finite-cone controls agree, pending reading. Equal healing probabilities can still conceal different jump laws. Next augmented background-and-damage state or justified regeneration; no larger short-history fit.

**Question 2 augmented transition (GPT GC507, 2026-10-08; serves row 3).** Exact full background-and-finite-damage recentering is explicit. Finite perturbations can jump by N+1 and collapse to a singleton, ruling out universal fixed-radius jump determination. Controls PASS, hand reading pending. The constructed pairs are not proved reachable from the iid single-flip ensemble. Next justified regeneration, reachable-state restriction or jump-tail bound; limiting speed remains open.

**Question 2 reset guard (GPT GC508, 2026-10-08; serves row 3).** GC507's singleton resets have at least floor(N/2) deterministic left advances after a jump N+1; odd N has a proved healing endpoint. Fixed controls PASS, hand reading pending. Singleton damage alone is not ambient iid regeneration; actual single-flip reachability is unproved. Stop family enlargement and seek a genuine conditioned fresh-background criterion. No transport speed or mixing theorem.

**Question 2 fresh-information condition (GPT GC509, 2026-10-08; serves row 3).** In the actual iid single-flip experiment, a strict new record of J_t=L_t-1-t below the previously revealed initial boundary supplies conditional left-advance probability 1/2 by deferred exposure and left permutativity. Existing early laws and hand index controls agree; hand reading pending. This is sufficient encounter freshness, not background-state regeneration or a speed bound. Next control exposure-deficit recovery and jump tails with damage shape retained; no larger history census.

**Question 2 one-sided bound (GPT GC510, 2026-10-08; serves row 3).** GC509's exposure law plus exact deficit accounting gives E[L_N]>=-N/2 and almost-sure liminf L_N/N>=-1/2, with a written exponential tail bound. Joint filtration/accounting reading pending. Thus any existing inward speed is at most 1/2; existence, positivity and the measured approximately 0.246 value remain unresolved. Stronger bounds need actual dynamics beyond the fresh-bit criterion; no simulation added.

**Question 2 recurrence obligation (GPT GC512, 2026-10-08; serves row 3).** Finitely many fresh records imply outward slope +1; conditional freshness alone cannot exclude this, as an explicitly non-Rule-30 escape process shows. Any existing positive inward speed v requires liminf fresh-tick frequency at least 2v. Hand scope audit pending. Actual return constraints, quantitative record frequency and intervening state control remain open; recurrence alone is insufficient.

**Balance duration certificate (GPT GC513, 2026-10-08; serves the main balance question).** GC496's equal-distance white-run branch now has exact duration m+d, where d is the left-neighbor checkerboard mismatch at time m-1. The right latch removes farther-right-tail dependence. Three hand controls agree; independent reading pending. Actual singleton match-length estimates and signed run-length cancellation remain open; this does not prove balance or a new constant-wall exclusion.

**Row8 duration targets contracted (GPT GC517, 2026-10-08).** Conditional on the exact run certificates, sublinear individual durations are equivalent to sublinear black-start checkerboard depth, white-start nearest-black distance, and resonant post-arrival checkerboard depth. Arrival normalization needs the nearest-distance bound. Hand reduction pending; all actual selected-singleton estimates and signed cumulative duration cancellation remain OPEN. Stop further reformulation and fixed controls; seek a genuine dynamical bound or another main-line lead.

**Row8 finite-representation criterion (GPT GC518, 2026-10-08).** For a proved finite closed decimation family, selected all-prefix balance is equivalent to spectral radius below 2 on GC489's root-visible quotient. Necessity uses shifted dyadic blocks; origin dyadic totals alone are insufficient even in an explicit four-state example. Hand reading pending. No finite Rule 30 closure or spectral bound is established, so Problems 2/3 remain OPEN; stop sampled-kernel fitting.

**Row8 finite-kernel run consequence (GPT GC519, 2026-10-08).** Under proved finite closure and root balance, quotient contraction gives uniform sublinear discrepancy on all intervals and therefore bounded constant runs. Prefix balance alone does not. Hand reading pending; actual singleton balance and unbounded-run witnesses remain unproved. Even their joint proof would exclude only finite binary closure, not every cheap indexer or settle Problem 3.

**Row8 source-audit contraction (GPT GC520, 2026-10-08).** Condrey's known zero fibre gives white remaining duration directly as its first left mismatch at the start row, replacing GC517's delayed certificate. Hand contraction pending reading; no novelty or actual sublinear bound. Sharp finite-support horizons remain linear and do not give singleton long-run witnesses. Limited source search found no usable selected unbounded-run theorem; absence is not claimed. Stop certificate reformulation.

**Question 2 actual return constraint (GPT GC521, 2026-10-08; serves row 3).** Every unit rightward damage-front jump forces a left step next, at all times and for arbitrary finite damage. Hand proof and 128 independent local controls agree, pending reading. Unit jumps at fresh records or ties return to freshness after two ticks; finite-record escape needs infinitely many jumps of size at least 2. Large-jump recovery and quantitative record frequency remain OPEN; no speed claim.

**Question 2 larger-jump guard (GPT GC522, 2026-10-08; serves row 3).** Every jump of at least 2 leaves common bits 0,1 at the healed old front. Exact two-site jumps consequently forbid immediate left return, unlike unit jumps. Hand proof and 512 independent local controls agree, pending reading. Larger-jump multi-step recovery remains OPEN and requires intervening background and damage; stop small-jump enumeration. No speed or record-frequency bound.

**Question 2 deterministic escape (GPT GC523, 2026-10-08; serves row 3).** A finite-background single flip has a proved displacement cycle 0,2, outward speed 1 and only two fresh records; the edge template restores every two updates. Independent fixed controls PASS, hand reading pending. Universal deterministic recovery is CLOSED as false. This family requires a zero positive half, an iid null event; almost-sure iid recurrence, recovery probabilities and inward speed remain OPEN. GC507 N=1 enters the same family.

**Question 2 specific escape probability (GPT GC524, 2026-10-08; serves row 3).** n singleton displacement pairs 0,2 require exactly a 4n+1-bit corridor. Spatial iid invariance and a time/site union give an exponential bound and eventual logarithmic maximum length for this specific bout, excluding its infinite persistence even at adaptive starts. Hand reading pending; no experiment. Other outward histories, general recovery and record frequency remain OPEN; stop this pattern.

**Portfolio bulk universality bridge (GPT GC525, 2026-10-08; serves question 1 and row 2).** GC523 certifies a finite-seed edit invisible eventually to every observer of limsup speed below 1, yet visible forever on the right light cone. Seeds {0} and {0,1} share the entire site-0 trace. Hand corollary pending reading; no universal seed-independence, mixing or prize conclusion. Stop this template; a broader equivalence classification needs another mechanism.

**Question 2 width-two confinement (GPT GC526, 2026-10-08; serves row 3).** Exact width transitions and GC521 force persistent width at most 2 into the GC524-excluded singleton cycle. Protected confinement bouts have an exponential iid tail and eventual logarithmic maximum duration. Hand reading pending; no experiment. Wider confinement and general record recurrence remain OPEN; next width-independent recovery, not a width census.

**Question 2 width-independent budget (GPT GC527, 2026-10-08; serves row 3).** Actual unit reversal bounds interval outward displacement by weighted large jumps plus 1. Finite-record escape with total exposure E requires large-jump lower frequency at least 1/E. Hand reading pending; no experiment. Weighted-budget rate below 1 would exclude escape, but that probabilistic estimate and inward-speed existence remain OPEN. No width census or scalar closure supplies it.

**Problem 3 convention audit (GPT GC528, 2026-10-08; serves row 12).** GC487's unchanged sample supplies 32 distinct MSB-prefix profiles and a separate canonical MSB-first state lower bound of 32; LSB bound remains 31. Controls PASS, hand lemma pending reading. No infinite-kernel or time lower bound; stop certificate expansion and require analytic infinite continuations or selected closure.

**Question 2 literature model guard (GPT GC529, 2026-10-08; serves row 3).** A genuine initial single flip produces second-update damage absent from the corresponding single-defect replica count, due to the quadratic OR interaction. Controls PASS and the embedding has positive iid cylinder probability; hand reading pending. Replica profiles cannot be imported as pointwise domination. Endpoint comparison and actual single-flip speed remain OPEN; next primary exponent definitions.

**Question 2 extremal-exponent guard (GPT GC530, 2026-10-08; serves row 3).** Tisseur's shift-maximized one-sided quantities equal n at every finite horizon almost surely for iid Rule 30, by radius bounds and rare finite zero-window witnesses. Both extremal exponents are therefore 1. Hand audit pending reading, no experiment or novelty claim. These worst-case quantifiers and liminf-defined averages do not supply actual fixed-origin pair-speed convergence. Return to simultaneous front-state reasoning unless a source matches that process.

**Question 2 directional contraction (GPT GC531, 2026-10-08; serves row 3).** Existing exact rightmost-damage motion gives tilde-Lambda_n^+=Lambda_n^+=I_n^+=n for every full-shift background. The plus average exponent is 1, with convergence directly proved in this direction. Hand audit pending reading; no experiment or novelty claim. Minus shielding, actual left-front speed and recurrence remain OPEN. Stop plus-direction elaboration; reflection is not valid for asymmetric Rule 30.

**Question 2 geometric recurrence target (GPT GC532, 2026-10-08; serves row 3).** Exposure E_N is exactly the maximum actual damage span before time N; freshness is a strict span record, with record increments 1 or 2. Thus infinite fresh ticks iff unbounded span, pathwise. Hand audit pending; no experiment. Existing width-two exclusion is insufficient for this all-width target. If speed v exists, E_N/N tends to 1+v and fresh lower density is at least (1+v)/2; no speed or recurrence is established. Next a mechanism forcing new span records.

**Question 2 confinement escape witness (GPT GC533, 2026-10-08; serves row 3).** A 2M+1-zero background window along the right edge forces any span at most M beyond M within ceil(M/2) updates, uniformly over damage holes. Hand proof pending reading. Infinite zero-cylinder visits for H=shift composed with Rule 30 would therefore prove unbounded span and record recurrence; that critical-ray premise remains OPEN. Fixed-frame mixing loses its negative-endpoint hypothesis, and invariance alone does not supply visits. No experiment, speed theorem or width census.

**Question 2 critical-ray phase guard (GPT GC534, 2026-10-08; serves row 3).** A fresh-left-pivot mixing proof fails because the critical cone always starts at initial site 0. The right-half map is an exact parity skew extension over its autonomous right tail; a specified measurable sign-cocycle solution would obstruct ergodicity. Hand algebra pending reading; no solution or exclusion is established. One-time fairness and ordinary mixing supply no cylinder-visit theorem. Generic mixing transfer CLOSED as unsupported; next actual conditional escape or justified phase analysis, not a mixing fit.

**Question 2 local phase route closed (GPT GC535, 2026-10-08; serves row 3).** Every fixed finite-prefix sign phase fails GC534's equation on a positive cylinder: a first tail bit 1 followed by enough zeros leaves its observed prefix fixed but has odd cocycle. Compactness excludes continuous phases and their almost-sure versions. Hand audit pending reading; no experiment. Local phase obstruction CLOSED, arbitrary measurable phases and critical-ray visits OPEN. Stop finite phase searches; no ergodicity or speed conclusion.

**Question 2 measurable phase scope (GPT GC536, 2026-10-08; serves row 3).** A hypothetical exact sign phase has prefix-m prediction error at least 2^(-(m+3)) and each sign mass at least 3/8. Hand bounds pending reading; no experiment. The shrinking error floor does not contradict measurable approximation, so the local exclusion does not settle arbitrary phases. No critical-ray visits or speed result. Stop phase elaboration without new regularity or actual return input.

**Question 2 actual fresh healing branch (GPT GC537, 2026-10-08; serves row 3).** After intervening reveals, a fresh pivot selects between a known next damage word A_t and A_t plus the below-front site. Displacement is conditionally -1 or known K_t in equal proportions, with explicit mean and variance. Hand audit conditional on GC509 pending reading; existing first-step controls agree, no experiment. Full background does not regenerate, reused ticks remain uncontrolled, and jump integrability or speed does not follow. Next reachable-state control of K_t and subsequent recovery.

**Question 2 safe-branch transport criterion (GPT GC538, 2026-10-08; serves row 3).** A fresh start with every subsequent fresh healing offset at most 1 forces one- or two-update return blocks and inward lower/upper rates 1/3 and 1/2 almost surely, conditional on the exposure proof. Hand audit pending; no experiment or assertion this restriction occurs. A true inward speed in (0,1/3) would require infinitely many large fresh branches. Finite-record escape makes a merely eventual restriction vacuous. Retain large-branch recovery; actual recurrence and speed remain OPEN.

**Question 2 large-block occupation (GPT GC539, 2026-10-08; serves row 3).** Actual fresh-to-fresh time partition gives -L_N>=N/3-(4/3)B_N-Q_N-o(N), where B counts updates in blocks starting with K>=2 and Q is current span deficit. Hand proof conditional on GC509 pending review; no experiment. If speed v exists, Q_N/N vanishes and liminf B_N/N>=(1-3v)/4. No branch-start density, occupation estimate or speed existence follows. Next full-state control of large-block durations; retain unfinished deficit.

**Question 2 return-average criterion (GPT GC540, 2026-10-08; serves row 3).** Infinite fresh times with finite limiting mean spacing d make every terminal deficit sublinear by the two-site recovery bound. A further mean record gain g gives inward speed g/d-1, with conditional gain bounds 3/2<=g<=2. Hand audit pending; no experiment or proof these averages exist. Duration convergence alone supplies rate bounds and can give positive lower rate if d<3/2. Stop accounting refinements; next actual duration estimate or induced-state law retaining selected environment.

**Question 2 predictable return tables (GPT GC541, 2026-10-08; serves row 3).** Between fresh ticks no new initial bits are exposed, so each fresh pivot chooses immediate left return or a healing excursion of pre-pivot specified duration H, possibly infinite. Hand audit conditional on GC509 pending review. Finite-record probability equals half the sum of fresh infinite-table encounter probabilities; none is estimated. Small offsets check known return blocks; finite-background escape is iid null. No iid renewal, finite decision algorithm or speed result. Next exclude infinite tables or control their conditioned durations.


**Problems 2 and 3 statistical bridge guard (GPT GC542, 2026-10-08; serves prize Problems 2 and 3).** Known binary Champernowne normality plus an explicit integer-band index formula gives a balanced, aperiodic, fully normal word with polylogarithmic indexed bit cost. Hand algorithm audit pending review; no experiment, novelty or Rule 30 realization. Statistical-to-time inference CLOSED even with all fixed-block frequencies; actual singleton statistics and computational complexity OPEN. Next certify a Rule 30 representation or define a restricted bottleneck; no generic counterexample expansion.


**Question 2 duration state guard (GPT GC543, 2026-10-08; serves row 3).** Existing exact corridors give positive iid encounter probability at least 2^(-4n) for a fresh K=2 healed table with H>=2n. Hand corollary pending review, no experiment. Offset-only deterministic duration bound CLOSED; no infinite-mean or positive infinite-duration claim. Full-state probabilistic tail estimates and recurrence OPEN. Stop corridor elaboration; retain environment information.


**Problem 2 adjacent-run guard (GPT GC544, 2026-10-08; serves Problem 2).** A solid finite black interval [-m,m] has centre prefix 1 then m zeros then 1. Thus a black duration of 1 does not bound the following white duration uniformly over finite seeds. Hand family proof pending review, no experiment. Universal duration-only adjacent coupling CLOSED; no singleton asymptotic conclusion. Selected reachable-state constraints and cumulative signed cancellation OPEN. Stop this family.


**Problem 2 white-start predecessor constraint (GPT GC545, 2026-10-08; serves Problem 2).** At a black-to-white transition, the new left black distance equals the preceding contiguous black depth ending at the centre. A bilateral white gap of radius m forces a preceding solid block [-m,m-2]. Hand Boolean audit pending review, no experiment. Valid for singleton transitions, but no selected block-growth bound, resonance control or cancellation estimate. Next constrain actual predecessor blocks; stop certificate reformulation.


**Problem 2 white-start right endpoint (GPT GC546, 2026-10-08; serves Problem 2).** Exact q=r+1+z completes GC545; resonance iff ell=r+1+z. One exterior bit changes resonance without changing the centre solid block. Hand audit pending, no experiment or singleton statistic. Retain z in any selected-state argument; growth, tie frequency and post-arrival match bounds OPEN. End transition refinement.


**Problem 3 effective-coordinate scope (GPT GC547, 2026-10-08; serves Problem 3).** G130 preserves first-difference depth exactly and admits direct quadratic forward/cubic inverse full-prefix Boolean costs. The singleton prefix has a logarithmic unrestricted generating description from N; unrestricted incompressibility target CLOSED. Hand audit pending, no experiment or indexed shortcut. Resource-bounded complexity and actual representation OPEN; no prefix census expansion.


**Problem 3 official runtime scope (GPT GC548, 2026-10-08; serves Problem 3).** The linked official formal predicate excludes O(n) indexed algorithms; the prose shortcut discussion concerns sublinear work. Neither is identical to an eventual Omega(n) lower bound. Primary-source and synthetic-runtime audit pending review, no experiment or actual algorithm. Retain explicit quantifiers and cost model in every proposed result; no intended committee correction is assumed.


**Question 4 balance guard (GPT G239, 2026-10-08; serves portfolio question 4).** Six neutral length-28 binary gap words give an abstract shift with entropy at least log2(6)/28, bounded factor charge 21 and density 3/14; it avoids all seven CL041 forbidden words and G238's factor. Hand application of standard block coding awaits reading. No Rule 30 realization or actual entropy bound. Exact balance alone is insufficient; next ask whether neutral choices admit coherent predecessors at every depth, not another drift measurement.

**G239 first realization layer (GPT GC551.1).** Shared state 10 has controlled-width-2 loops spelling both gap blocks, so the neutral family survives X_2. Hand relation and 16 literal controls pass, reading pending. The free exterior must become an actual evolving column at greater width; no uniform entropy bound.

**G239 second realization layer (GPT GC551.2).** The family survives X_3 using common state 111; the old state-10 lift fails. Thirty-two local controls agree; reading pending. Small-width enumeration stopped: a uniform exterior construction remains open.

**Question 4 information-channel notch (GPT GC556, 2026-10-08).** At the white-start wall, the last initial right-cone bit affects visible samples at physical times 2 and 4 on exactly the prefixes 00 and {1000,0110}, respectively. Fair initial activation probabilities are 1/4 and 1/8; the latter refutes a fresh-independent-four-gate model. G243 hand proof awaiting reading. No large-time lower bound, collision contraction or positive entropy follows; next repeatable gate pattern with a coherent exterior.

**Question 4 channel compatibility (GPT GC558, 2026-10-08).** For every actual right row, consecutive last-right-cone activation indicators obey A_n*A_(n+1)=0 after the initial sample. The odd-phase latch locks the intervening gate. G243 extension pending reading; this restricts one specific input path, not all information or entropy. Next coherent block-level gate reset.

**Question 4 entropy gateway (GPT GC559, 2026-10-08).** G244 bounds actual visible-prefix Shannon entropy below by expected last-pivot activations. Positive average activation would suffice for positive limiting language entropy without independent activations or stationary output law. That average is unproved and may vanish; inactive last pivots supply no entropy upper bound. Hand reading pending. Next a block input channel avoiding a maximal-speed path, with actual exterior compatibility.


**Question 4 last-pivot channel triage (GPT GC560, 2026-10-08).** Hand G97 sampling before the wall frontier gives P(A_n=1)<=2^(-n), summable activations and zero mean density under fair initial right bits. The G244 positive-mean route is CLOSED conditional on independent reading of this audit; G244's inequality itself is second-read by L299. GC558 isolation is second-read by L298. Neither masking nor isolation bounds total visible entropy above. Next earlier-input conditional uncertainty or a coherent block channel; no extra census.


**Wheel-origin scope guard (GPT GC561, 2026-10-08; serves question 6).** CL051's Rule 60 seven-ring count has a hand algebra proof: 64 periodic image states, with 64 one-step transients outside the image. Full-state affine factors from seven-ring Rule 30 to a linear update are necessarily constant (G245, awaiting reading). Nonlinear or restricted-domain factors remain open. Matching the 63 cyclic-state counts does not identify the actual wall wheel; next specify a phase map and account for the edge term.


**Question 4 channel closure verified (GPT, receipt of Local L300).** GC560 is independently second-read in c51e30f: G244's positive-mean last-pivot channel under fair right inputs is CLOSED. Boundary-language entropy and earlier-input channels remain OPEN.


**Question 4 two-bit frontier audit (GPT GC562, 2026-10-08).** The second-last time-2n cone input has sensitivity probability at most 4n*2^(-n), from one-stay damage paths and fresh baseline gates. G246 awaits hand reading. If verified, enlarging the closed last-pivot channel to the outer two-bit frontier still gives summable activity. Earlier-input conditional uncertainty remains OPEN; no total entropy upper bound, fixed-offset census or block-width threshold.


**Question 4 posterior uncertainty target (GPT GC563, 2026-10-08).** The next visible bit is gated by a hidden white pair after histories ending in zero. Average optimal history-only prediction error gives a sufficient entropy bound while retaining earlier input uncertainty (G244 extension, awaiting reading). No positive error bound is established; unconditioned void frequency and finite gap restrictions alone fail. This is ensemble prediction without runtime constraints, not Problem 3. G246 is now second-read by Local L301; fixed-offset extensions stop.


**Question 4 posterior-pairing failure (GPT GC564, 2026-10-08).** Initial 00<->11 surgery cannot be lifted by simply editing the evolved hidden pair: after visible history 00, pair 11 has no predecessor. Hand next-black posteriors 5/12 and 3/16 reconstruct GC502's three-symbol collision law. Finite control awaiting reading, no asymptotic extrapolation. GC563 is second-read by Local L302; its average-beta question remains OPEN. Next initial-input fibre compatibility; no longer posterior census.


**Question 4 gated gap-start target (GPT GC565, 2026-10-08).** At observable gap starts, actual sites 2 and 4 both black make the next two symbols encode site 3. Weighted history-conditioned entropy gamma on this gate gives H_N >= (1/2) sum gamma (G244 extension awaiting reading). Its positive mean is OPEN. Marginal kick frequency, fair hidden bits and a universal wheel-start gate are not assumed. No extra census or board row.


**Question 4 pause of the local channel chain (GPT GC566, 2026-10-08).** Prefix 1110e yields next visible outputs 0,0,e, independently of the right exterior. This identifies an actual upstream control but leaves GC564's history-fibre lift and posterior weights unresolved. No new sufficient target or census. GC565 positivity stays OPEN; further local target rewrites stopped. Next a distinct main-line structural-balance/Problem 2 proof audit after checking prior closures.


**Structural-balance restart triage (GPT GC567, 2026-10-08; serves Problem 2).** Prior duration and correlation closures supply no new singleton estimate; the main board remains PARKED. A fixed actual singleton control has two selected forward Gray sources cancel at target 4, excluding compatibility alone as a universal noncancellation premise. No full-clock, inverse-source or balance conclusion. Return to the main-line GC549.20 actual paired-zero-band predecessor obligation; stop local balance and source-count rewrites.


**Conditional zero-band audit (GPT GC549.39 / GC568, 2026-10-08; serves Q6).** G122's finite-interval application retains one wider-white and three black-core predecessor branches. All four have actual finite extensions. Unconditional zero-only backward induction CLOSED; the clock-conditioned branch and endpoint obligations stay OPEN. No new proof method, run or board row. Next retain the nonzero branch rather than assume its endpoint pair vanishes.


**Clock-conditioned band triage (GPT GC549.40 / GC569, 2026-10-08; serves Q6).** A white zero band touching the centre selects the black predecessor core by the preceding black clock sample. This recovers reviewed GC545 rather than discharging it; actual finite seed {-1} is a control. Backward-white-only route remains CLOSED. Stop this chain without a selected block estimate; next distinct Q7 waiting-budget audit.


**Q7 joined-window phase audit (GPT GC570, 2026-10-08; serves Q7).** Proposition 11's pulse reset fixes any subsequent full-line suffix. GC335's joined seven-edge window has exact any-arrival charge 4q-31/2 for dyadic q>=8, saving q-1; hand extension awaiting reading. Generic birth/interior restarts retain the older safe allowance. Counts and complementary debt remain OPEN. Next actual birth-interruption audit, no new census or board row.


**Q7 joined-window restart audit (GPT GC571, 2026-10-08; serves Q7).** All independently restarted subintervals fit D=4q-31/2 for dyadic q>=8, so G9 supplies birth transfer for the specified normalized barriers beta_j<=j. Hand extension awaiting reading. Actual global block normalization, counts and complementary debt remain open. Stop named-window refinements; no new board row or run.


**Q7 actual birth-block normalization (GPT GC572, 2026-10-08; serves Q7).** Consecutive nonzero drivers under the standing birth schedule pay at most one entrance clamp, none internally. The joined actual block has debt <=4q-29/2 for dyadic q>=8; pending reading. Rooted counts and complementary gaps remain open. Named-window refinements stop here.


**Q7 mixed-gap birth accounting (GPT GC573, 2026-10-08; serves Q7).** Positive clamps follow distinct zero drivers and cost at most one, absorbing the explicit birth sum in G6's missing zero-driver base steps: T(M)<=M+sum z on the actual clamped path. Awaiting reading. The selected zero-wait sum remains OPEN; no new board row, count or experiment. Stop birth refinements.


**Q7 extreme ordinary waits (GPT GC575/G247, 2026-10-08; serves Q7).** Two maximal nonsingleton waits on an uninterrupted full-line clock force the next delay to be one. Awaiting reading. Three-edge elapsed 2q-1 still grows with period; no average, rooted-frequency or birth claim. Stop extreme-family refinements; near-extreme selected waits remain OPEN.


**Q7 G247 reading receipt (GPT, Local L305 at verified 36f7bc519c20).** G247 is second-read within its uninterrupted full-line scope. No global debt or near-extreme estimate follows.


**Kicked-wheel seam triage (GPT GC578-GC580, 2026-10-08; serves Q7).** Visible formal splices allow +10 and pass the basic gate, but the named infinite-old witness is class 2, excluded by existing entry 26 after 133 steps. Named family CLOSED. Long-lock phase bound [-6,6] is already entry 27; short locks, lifted-charge parity and transient direction remain OPEN. No new board row or computation claim.

**Question 1 local-equilibrium gateway (GPT GC602, 2026-10-08; serves rows 1/8/13).** Horizontal bulk normality is equivalent to the fair-row law for every fixed forward spacetime patch. It would give averaged vertical temporal normality, with exact Rule 30 correlations on multirow and right-moving patches. Hand conditional transfer awaiting reading; the actual finite-seed bulk premise remains OPEN. A separate fixed-patch prize would duplicate question 1. Wolfram already discusses rows, directions and other seeds publicly; no unasked-subject or novelty claim. No experiment. Next an actual deterministic discrepancy mechanism, not another equivalent formulation.

**Question 4 startup-pruning gateway (GPT GC603, 2026-10-08; serves rows 5/6).** The compact boundary language and the intersection of all its temporal images have equal word-count entropy. Temporal-core and controlled-width intersections commute. Hand application of GC498/499 awaiting reading; finite-age state extinction alone supplies no entropy decrease, and spatial-state exclusions still need visible projection implications. Actual entropy remains OPEN. Next a coherent surviving lower language or upper count, retaining RV3's unresolved branch; no run.

**Question 4 uniform-cover target (GPT GC604, 2026-10-08; serves rows 5/6).** A physical-language wheel cover with uniform o(n) uncontrolled symbols would force zero entropy even with arbitrary output bits and phase resets. Hand counting criterion awaiting reading; no actual budget or cover is proved. Kick count must include transient information, and typical sparsity or bounded signed charge is insufficient. Next coherent lower-family exterior or physical transient-content restriction; stop generic cover refinements.

**G239 actual exterior gate (GPT GC605, 2026-10-08; serves question 4).** Actual 000-to-111 returns force the fourth bit to zero; the fifth bit then selects hidden entrances 010 or 011. Both have finite right-row entry controls. Hand proof awaiting reading, no width scan. Complete paths and coherent choices at repeated returns remain OPEN; next actual return dynamics, not free-boundary extrapolation.

**G239 actual short-return advance (GPT GC606, 2026-10-08; serves question 4).** Prefix 11101 closes the full six-tick short loop for every farther tail, returning to 1110. A separate finite cylinder enters the long path but misses its common return. Hand proof awaiting reading; actual short loop PART, repeated neutral-block compatibility and entropy OPEN. Next a coherent exterior family shared by successful returns, not another width graph.

**G239 actual long-return advance (GPT GC607, 2026-10-08; serves question 4).** Two finite cylinders close the full ten-tick long path independently of farther tails, joining GC606's short return at marker 1110. Single-return compatibility PART; coherent arbitrary concatenation and entropy OPEN. Hand proof awaiting reading. Next exterior return-image compatibility; two finite loops alone are not a lower-language certificate.

**G239 return-image advance (GPT GC608, 2026-10-08; serves question 4).** The original OR claim was corrected by Local L323 to XOR of time-two sites 6 and 7. Opposite finite cylinders give two consecutive short loops or a next hidden long entrance. Hand proof awaiting Local reading. Repeated arbitrary mixed choices and entropy OPEN; next returned sixth bit and long-return images. No width census.

**G239 corrected two-return compatibility (GPT GC609, 2026-10-08; serves question 4).** The drafted zero-sixth obstruction was refuted by L323's correction before publication. A short cylinder returns to 11101 or 111001 according to outward parity, so a second known short or long loop completes. SS and SL cylinders PART; arbitrary infinite choices OPEN. Cloud reading requested; Local's NL certified finite obstructions take priority.

**G239 NL scope transfer (GPT GC610, 2026-10-08; serves question 4).** If L323's reported certified LLLLLSS absence holds, adjacent neutral blocks B_5 B_0 are physically excluded, closing unrestricted realization of the entire six-block family. This predicts six absent NL three-block cases. Encoder and shift implication hand audited; concrete certificate not yet independently checked. Constrained subfamily entropy OPEN; await full NL outcome and retained representative certificate.

**G239 shortest-NL macro filter (GPT GC611, 2026-10-08; serves question 4).** The eleven reported seven-gap exclusions remove exactly macro edge B_5 to B_0 within the aligned neutral family, affecting twelve of 216 triples. A two-symbol abstract neutral subfamily avoids them; physical realization remains OPEN and longer exclusions may block it. Local L324 reads GC610; concrete certificate verification next.

**NL internal-age explanation (GPT GC612, 2026-10-08; serves question 4).** L324's reported mortal sparse core embeds at offsets 6,6,8 in three complete forbidden words. If its death threshold is 6, word-internal age excludes each globally, despite possible startup cores. Static embeddings checked; actual mortality certificate pending. No entropy inference.

**G239 free physical realization CLOSED (GPT GC613, 2026-10-08; serves question 4).** Concrete LLLLLSS and sparse-core mortality certificates independently pass matching hashes, exact CNF regeneration and a separately built DRAT checker. B_5 B_0 is excluded, closing the unrestricted six-neutral-block realization; the abstract balance/entropy theorem survives. Physical constrained subfamily and its entropy OPEN. GC612's three word-internal age exclusions now have a checked mortality premise. Next full NL outcome and constrained coherent language, no free-family restart.

**Constrained-return compatibility (GPT GC614, 2026-10-08; serves question 4).** A successful simple long entry returns to 1110000, leaving the union of known short and simple long entry cylinders. That union's invariance route CLOSED; a smaller invariant tail family or other long cylinders remain OPEN. Hand proof awaiting Local reading. No claim about the next complete visible gap or entropy.

**NL length normalization (GPT GC615, 2026-10-08; serves question 4).** Counts with K gaps and s shorts have length 5K-2s+1 and are bounded by the physical word count at that length. Sustained dominant-bin rates must respect the certified ceiling, whose width-28 summary is 0.1236, distinct from measured 0.1222. Finite NL ratios give descriptive finite lower counts, not a physical lower entropy. Await Local's full outcome; no new count run.

**G239 conditional marker renewal PART (GPT GC625, 2026-10-08; serves portfolio question 4).** From initial marker 1110, every S/L visible word renews that marker at every internal boundary: exits 100 and 101 force next gap lengths 2 or 4, outside S/L. A final L can still exit, so the terminal boundary is an exception. Infinite S/L traces starting at the marker use GC623's complete long gate at every return; GC626 extends synchronization to arbitrary startup after the first gap, awaiting Local reading; coherent infinite realization remains OPEN. No entropy claim or prize-board row.

**G239 arbitrary-startup synchronization PART (GPT GC626, 2026-10-08; serves portfolio question 4).** All visible S/L entrances start 111 or 1101; each reaches 000 before closing. A following S/L demand forces closing marker 1110, hence every infinite S/L trace synchronizes after its first gap. Finite startup and terminal exceptions remain, so no NL A/B equivalence. Failed 110 elimination retained and repaired by hand; Local reading requested. Infinite physical subfamily and entropy OPEN. L331 reports 49 of 216 neutral triples absent (12 shortest, 36 eight-gap, one fourteen-gap obstruction), 167 realized; full NL outcome is Local's measured evidence, not an infinite certificate.

**G239 finite marker cost (GPT GC627, 2026-10-08; serves portfolio question 4).** Trimming both endpoint gaps sends actual NL A words into B by GC626; B_K<=A_K<=4 B_(K-2), and binary-length counts obey the corresponding shifts 6,8,10. Asymptotic selected-language rates agree, though finite A/B words differ. Hand proof awaiting Local reading; no positive entropy or unbounded-length certificate. Coherent infinite subfamily OPEN.

**Q6 actual restart-strip residual (GPT GC630, 2026-10-08; serves Q6).** For initial moving prefix11001 and L>=3, GC599's alternating interior rays leave frontier-plus-strip Pascal residual101000 by target depth. Hand recurrence proof awaiting Local reading. Compensation by that strip alone CLOSED; GC631 extends the closure through seven cells for L>=5, retaining the possible age-zero source as a constant target parity. GC632 is second-read by L340. GC633 is second-read by L341: a four-tick shift handles both phases and requires unbounded ages beyond the shield. GC634 shows H8 supplies unbounded ages in every ordinary finite-left row, closing the age-only discriminator (reading pending); the exact target-parity requirement remains. GC643 advances actual parity: the settled H8 ray has an uncancelled order-three q=1+z+z^2 denominator, while the lower residual has order at most two. Finite startup events cannot repair it; truncated-strip compensation through offset8 CLOSED, conditional hand proof awaiting Local reading. Infinitely many farther events at offsets>=9 are necessary for a hypothetical full clock. GC646 extends the actual hand closure through offset11: H9=NOT v8 contributes order3, H10 becomes silent, and H11 has one isolated event per four ticks, a genuine q^4 pole. Compensation then needs infinitely many events at offsets>=12; Local reading pending. This is not an exclusion or invitation to a strip census. Farther inward clock-compatible sources OPEN. No event density, unbounded-offset claim, full-clock exclusion or prize result; opposite initial phase and depth clipping require separate treatment.

**Q1 hull-weight shortcut CLOSED (GPT GC636, 2026-10-08; serves Q1).** Exact-width configuration-position counts assign equal initial counts2^(w-2) to every observation-distance slice L. A hypothetical linear edge deadline alone cuts positions, not an exponential seed fraction; a logical eligibility countermodel demonstrates the gap. Local reading requested. Actual within-slice trace cost and Q1 OPEN; no Rule30 counterexample or new run. GC637 conditional clarification: combining a uniform T<=c*j+b deadline with the already proved fresh-left halving DOES give exponential loss with alpha=1/c. Such a deadline remains unproved; Local reading requested.


**Q7 long-pair scope control (GPT GC651, 2026-10-09; serves Q7).** L224's published39-edge positive-debt witness has no internal GC650 trigger: max adjacent delay sum22 at period32, debt78.5. Literal recurrence/reset controls pass. Long-pair-only payment of every finite positive-debt segment fails this control; global and external compensation remain OPEN. Next below-threshold selected-arrival constraints, no new census or board row.


**Q7 selected mismatch budget (GPT GC652, 2026-10-09; serves Q7).** In an uninterrupted nonzero successor interval, the next delay is1 when B(S-1)=0 and otherwise2 plus the first B,C mismatch distance from S. Exact covered-edge debt is R-N/2-F. L224's37 internal triples verify the identity with R98,F9, debt70.5. Selected mismatch-run bound remains OPEN; no iid law or global slope. Identical B=C yields zero successor and requires separate accounting.


**Q7 balance-only selected-run bound CLOSED (GPT GC653, 2026-10-09; serves Q7).** Compatible periodic inputs with B,C and B XOR C each half-black still permit waits1,1,q/2 for arbitrarily large dyadic q. Fixed controls pass; period-encoding failure retained. Rooted/cross-edge constraints on GC652's mismatch budget remain OPEN, as does external compensation. No global rooted counterexample or new board row.


**Q7 balanced-family ancestry triage (GPT GC654, 2026-10-09; serves Q7).** GC653's displayed phase lacks a gated incoming predecessor, even though its two-state long-wait suffix is gated. Family excluded at that phase from rooted paths; balance-only scalar countercontrol survives. Quantitative ancestry-sensitive mismatch budget remains OPEN. Stop enlarging marginal-weight families or treating gate membership as rooted sufficiency.


**Q7 predecessor count audit (GPT GC655, 2026-10-09; serves Q7).** With reconstructed predecessor nonzero, incoming gated phases count1-C(u) plus transitions across the preceding B-black gap. A fully black C covering that gap gives none; zero predecessors require the derivative exception. Exact local selection, no mismatch-budget or rooted-count bound. Stop gate-count refinements absent a quantitative connection to GC652's R.


**Q7 incoming-count proxy CLOSED (GPT GC656, 2026-10-09; serves Q7).** Half-balanced B,C and B XOR C plus nonempty incoming gated ancestry still permit waits1,1,q/2-2 on compatible three-state gated segments. Fixed controls pass; earlier root ancestry unverified. GC655 local test survives but supplies no budget. Stop family/gate refinements; actual-history summable compensation remains OPEN.


**Selected physical-length factor bridge (GPT GC673, 2026-10-09; serves portfolio question4).** Complete selected S/L words have factorial binary factor counts P(n), with B(n)<=P(n)<=sum_(d=0..8)(d+1)B(n+d). Bounded endpoint padding proves cumulative-count and factor-count rates exist and equal GC627's binary limsup; A/B rates agree. This repairs the withdrawn exact-length submultiplicativity claim without reinstating it. Hand proof awaiting Local reading; arbitrary-length actual realization and positive entropy remain OPEN. No prize-board row or finite-slope extrapolation.


**Selected infinite-survivor bridge (GPT GC674, 2026-10-09; serves portfolio question4).** At each fixed macro length, nonviable prefixes have finite maximal right lookahead. Aligned factor closure bounds their contribution to a terminal suffix, proving finite selected-language and infinite-survivor per-gap entropy rates agree. Infinite survivor words have actual autonomous right-row witnesses by compactness; positive rate would imply positive physical coded rate, but no such lower bound is established. Hand audit awaiting Local, with mode-B prefix guard explicit. Finite-support/global-clock realization and positive entropy remain OPEN; stop abstract bridges without actual return input.


**Finite checkerboard corrections (GPT GC677-GC678, 2026-10-09; serves Q6).** Whole defect radius is nonincreasing every two ticks, giving an exact finite certificate at fixed radius. Radius9 has exactly three left-only forever survivors, with defect masks40->54->0->0; two are transient nonstationary rows. The predicted stationary uniqueness is CLOSED by counterexample; arbitrary-radius classification remains OPEN. This domain has an infinite checkerboard tail, so Q6 finite left support, right-half compatibility and a finite global seed remain OPEN. No radius sweep planned; independent replay requested.

GC679 follow-up to finite checkerboard corrections (serves Q6): the unrestricted initial-row fibre of the stationary target, with the initial black test, is exactly{0,54}; no radius assumption is needed. Dropping that test adds13,55. GC677 has Local's L366 second reading; GC678-GC679 await replay/reading. Expanded radius census declined pending a main-line bridge.

**Common-phase remedy for L224 CLOSED (GPT GC682, 2026-10-09; serves Q7).** Its verified39-driver period32 block has elapsed176 in one phase, so G6 gives elapsed>=145 in every common phase, including a monotone lower bound after birth clamps. The above3 block excess cannot be removed by choosing a phase; no global bound is refuted. Surrounding coherent compensation remains OPEN. No phase sweep or period-uniform conclusion.

**One-period external buffer for L224 CLOSED (GPT GC683, 2026-10-09; serves Q7).** The existing return guard spaces white drivers by at least5, so a consecutive32-driver buffer can repay at most55 of slope2.5 debt, below the measured78.5. Necessary one-sided extension length is at least46, or53 without white drivers. Longer coherent compensation remains OPEN; no attainment or uniform bound is claimed.

GC684 follow-up (serves Q7): the fixed L224 debt is repaid by148 coherent extra nonzero drivers (elapsed291), with no positive recross through the256-edge cap. Independent constructors agree; no zero branch is chosen. This closes nonrepayment of this particular finite extension, not the open period-uniform compensation mechanism or whole-history bound.

**Infinite all-S physical subfamily CONSTRUCTED (GPT GC686, 2026-10-09; serves portfolio question4).** An84-cell periodic initial block0x688eb74a45efb082671ee, bit0 at site0, has a six-update Rule30 orbit with site0 word010101 and even site1 word100 repeated. This closes qualitative unbounded selected-word length and nonemptiness of an infinite actual subfamily, within a zero-entropy periodic example. Independent ring replay requested. Positive entropy, richer coherent S/L choice and finite-support global clocks remain OPEN; no new prize-board row or period sweep.

- **Fixed temporal6 all-S branching route CLOSED (GC687; serves portfolio question4).** With GC686's white-even phase and11101 entrance, the84 live profile pairs form one deterministic cycle and just one of20 entrance paths survives.594 raw branch vertices give no live branches. Independent pruning and3714 literal controls pass; second reading pending. This restricts this domain only; richer temporal behavior and positive selected entropy remain open.

GC688 follow-up (serves portfolio question4): every marker-aligned persistent all-S trace, with unrestricted exterior, has the same first-five period6 profiles11,13,33,60,23. Corrected next-return parity forces the intermediate fifth bit; an actual SL control prevents replacing parity by OR. This is a necessary slab constraint, not general exterior periodicity or positive entropy. Independent reading pending.

GC689 follow-up (serves portfolio question4): for arbitrary all-S exterior, site6 values u_k,x_k,z_k at return and times2,4 satisfy NOT x_k<=z_k<=NOT u_(k+1). This cross-return necessary gate forbids treating those phases as independent. No sufficiency or realizable branching is asserted; hand reading pending.

**Turning-row census (Cloud, 2026-10-09, RULE30-PRIZE.md §8.71, PROOFS.md entry 35 in the waiting room; serves
portfolio question 4).** GC686's ring turns 14 cells per update (CL071). Every Rule 30 row with $F^p x = \sigma^s x$
and $|s| > p$ is a ring, and every window of $|s| + p$ cells turns leftwards. Over $p \le 3$, $|s| + p \le 28$
(1,399 rings) the only turning row with an alternating column at all is GC686's ring: no mixed S/L or all-L
turning witness in that range. Why the ring turns is open (question to GPT in CL071).

**Interlocking shapes (Cloud, 2026-10-09, RULE30-PRIZE.md §8.72; the owner's question; a side question).** Rule 30's
histories are the tilings by 8 Wang tiles. Doubly periodic histories are walls of one brick, and GC686's ring is a
wall of $14 \times 6$ bricks. Next to the 0101 wall, a periodic column 1 of length up to 20 freezes the left half into
one of 20 bricks, never blank. Monotile and Kari-type aperiodicity proofs rule out every periodic tiling, so for Rule
30 they could enter only through the boundary.

GC690 follow-up to finite checkerboard corrections (serves Q6): inverse recurrence preserves this background, so GC679's guarded two-to-one map gives2^n n-step ancestors and2^(n-1) first settling at n. Arbitrarily long transient left survivors are proved without a radius sweep. No uniform settling horizon across radii; arbitrary survivor/cycle classification, finite black support and right compatibility remain open. Zero-tail closure explicitly fails; independent reading pending.

GC691 follow-up (serves Q6): guarded two-tick predecessors of any finite black-support target have eventual tail0, tail1 or period3 with one black per three cells. Finite support is the terminal00 condition after two inverse scans, not automatic from GC679's two-preimage fibre. Zero-target controls have no finite guarded predecessor and fail the future neighbour guard. Infinite finite-support survival remains open; hand reading pending.

**Uniform finite inverse-branch pruning CLOSED (GC693; serves Q6).** The finite guarded target100010011 has two finite guarded predecessors1100101 and1010011. Exact two-tick paths, literal inverse transitions and170 independent forward cells certify both. GC692's one-target loss is nonuniform. No future survival or branching-rate claim; independent replay pending.


**Q7 selected-run ancestry signature (GPT GC702, 2026-10-09; serves Q7).** For consecutive X,A,B,C,D, a selected B=C interval [S,m) forces X(t)=B(t) AND NOT B(t+1) for S<=t<=m-2. Adjacent11 in X cannot lie wholly in that interior. The last equality time has a complemented derivative and is excluded. Joint signature proved by hand; rooted gap control remains OPEN, with no debt estimate. Stop local expansions without a quantitative rooted input.


**All-S finite-left compatibility CLOSED by hand (GPT GC704, 2026-10-09; serves Q6 and portfolio question 4; second reading requested).** GC688's period-6 nearest-right slab plus the alternating wall forces every left column period 6. With finite left support, two remote columns are initially white for six samples, hence forever white, forcing a white wall. The same argument covers an eventually all-S tail after synchronization. The GC686 infinite-support witness and finite prefixes remain valid; mixed S/L and general Q6 stay OPEN.


**All-S finite-block bound (GPT GC705, 2026-10-09; serves Q6; second reading requested).** At a genuine 1110 marker with leftmost black at -J, n completed S gaps satisfy 6n <= J+12 by the existing periodic-window edge argument, including J = -1. Arbitrary startup requires synchronization and a recomputed edge distance. This quantifies GC704's excluded infinite tail without bounding mixed S/L histories or claiming sharpness.


**Eventually periodic S/L finite-left compatibility CLOSED by hand (GPT GC706, 2026-10-09; serves Q6; second reading requested).** Exact nearest-right lifts h(S)=110100, h(L)=1101000100 turn a repeated mixed motif of physical length P into a periodic adjacent-column window. Its n copies satisfy nP <= J+2P at a synchronized marker. Finite left support therefore requires a genuinely aperiodic renewal tail; this does not imply positive entropy or exclude general mixed histories. Terminal visible L samples remain fixed before their closing boundary even if that boundary exits the marker.


**Aperiodic mixed forced-left cost OPEN (GPT GC708; serves Q6).** All sixteen four-gap temporal lift words require a forced black at depth at least floor(T/2), with independent decimal wall replay. This finite necessary-condition measurement does not establish a uniform bound, actual right realization or exclusion of aperiodic renewal tails. Stop word-length sweeps; seek a structural argument.


GC709 follow-up to aperiodic mixed forced-left cost (serves Q6): the renewal pulse train appears exactly as c_4(t)=q(t+3) after four left inverses. This hand identity retains arbitrary aperiodicity but supplies no depth-growing support bound. Two-tick pulses break it; actual 6/10 spacing satisfies it. Independent reading pending; no shallow-table expansion.


**Pure-S exact forced-support refinement (L372, GPT GC710; serves Q6).** Ring-prefix uniqueness verifies the sharp necessary bound 6n <= J+3. Pre-return windows and completed-return minima differ: including the closing tick removes equality at residue 11 modulo 14; actual completed-return equality is at residues 2,10. Exact window audit second-read; closing-inclusive correction awaits Local's reading. Mixed aperiodic costs remain OPEN.


GC711 follow-up to aperiodic mixed compatibility (serves Q6): existing Corollary F excludes unbounded near-squares starting at bounded macro indices under the exact visible 3/5 weighting. Unweighted repeat counts at moving starts need not meet its threshold. Conditional subclass exclusion only; actual admissibility forcing such weighted repeats remains OPEN. Hand reading pending; no frequency scan.


GC712 follow-up to mixed forced-left cost (serves Q6): the existing left coding bounds actual infinite renewal traces in depth D by 2^ceil(D/2), and completed m-gap words likewise when 6m>=D. This fixed-box count does not imply periodicity or control the unbounded-depth union. No depth-duration relation is proved; general mixed compatibility remains OPEN.


GC713 follow-up to mixed forced-left cost (serves Q6): the renewal choice at physical time B has initial pivot depth B+7. A finite zero tail selects at most one branch at each sufficiently late marker. Failure of that selected continuation, rather than increasing pivot locations alone, is the missing compatibility input. Hand reading pending; no branch-count refinement.


GC714 follow-up to mixed forced-left cost (serves Q6): after initial SL or LS, a zero tail beyond depth 22 selects L at pivot 23 but fails its required black partner at depth 24. This concrete necessary obstruction rejects automatic guard survival; a universal prefix criterion is still OPEN. Common-partner independence is REFUTED at SS/LL; no word-length sweep.


GC715 follow-up to mixed zero-tail guard (serves Q6): the even partner difference is exactly common-white parity along the moving front diagonal. Absolute partner value remains missing, so equal partners can either pass or obstruct a zero tail. Hand reading pending; no difference-only counting argument.


GC716 control for GC714 (serves Q6): direct autonomous-left replay with zero tails independently verifies SL/LS failure at black time 23, insensitive to right exterior or a deeper bit flip. SS/LL pass only the tested guard. Finite examples now checked; no expansion without a scalable absolute-guard mechanism.


GC717 follow-up to mixed zero-tail guard (serves Q6): two ahead diagonals determine the absolute next guard E xor H0 xor (A AND P), so a zero tail passes iff H0=1. Exact hand recurrence validated on the same four stored prefixes. Actual late-prefix control of H0 remains OPEN; no enlarged guard tables.


GC718 follow-up to mixed guard (serves Q6): at each infinite renewal marker the required local left prefix is 01101000 or 01101010, because c_1(B+7)=1 xor c_8(B). The two prefixes do not form a closed finite-state map; deeper ancestry remains active. GC709-GC716 scoped results are second-read by Local L373; GC717/GC718 remain pending.


**Fixed-prefix deterministic renewal return closure CLOSED by hand (GC719; serves Q6; review pending).** For every K>=8, the same finite initial K-prefix and actual first S return can lead to different returned K-prefixes by flipping depth K+6. The two necessary marker prefixes, or any fixed enlargement, are not closed states on this finite-first-return domain. Stronger tail-restricted summaries and general infinite compatibility remain OPEN.


**Published G1 shift-graph route CLOSED for Q6 (GPT GC720; hand reading requested).** Guan/Wang 2011 section 3.2's Rule 30 graph has five phases, zero entropy and temporal period five. Its third-iterate left-shift identity is valid, but the positive-entropy/mixing claims fail for this graph. It cannot contain an alternating wall and supplies no mixed-renewal branching input. Targeted primary-source audit only; other subsystems remain unassessed.


GC721 follow-up to the actual all-S ring (serves Q6): temporal rotation of entrance pair (42,11) occurs at spatial index 70 on GC687's live cycle. Unique live continuation then proves F(x)(i)=x(i-14), completing CL071's conditional rigidity explanation with one cached membership check. This is a fixed-component consequence, not a new infinite family or exterior classification. Hand reading pending. L374 independently read/replayed GC717-GC720 within their recorded scopes.


**Unit-drift relative-periodic construction route CLOSED by hand (GPT GC722; serves Q6; reading pending).** F30^tau(x)=shift^q(x) with q=+1 or -1 cannot support an infinite alternating column: both neighbours become equal temporal samples of that column, forcing a white centre to stay white. Alternating windows contain at most 2tau+1 observations, without a sharpness claim. This excludes the entire unit-drift identity class behind GC720; zero/larger drift and general mixed compatibility remain open.


GC723 scope audit of the all-S ring (serves Q6): finite left support forces a global travelling identity F30^tau(x)=shift^k(x) to have k=tau, from the exact left-edge law. Ring motion +14 therefore cannot transfer to finite cuts, even during their protected alternating cones. Finite support on both sides excludes all nonempty global travelling shapes by the opposite right-edge law. This does not decide single-column clocks or maximal-left-speed identities with tau>=2. Hand reading pending; no displacement search.


**Unqualified binary interval-factor import CLOSED (GPT GC724; serves Q6's interval analogy).** Under either fixed left boundary, the two binary names of 1/4 have unequal Rule 30 image reals. A canonical expansion yields a discontinuous representation, not a continuous interval factor of the full binary space. Keep symbolic compactness; this does not invalidate the separately defined Mahler map or its endpoint audit. Narrow source reading requested.


**Turning-row theory audit second-read (Cloud dedbe55c, GPT GC725; serves Q6 and row 10).** At strict |s|>p, TR's finite window-map classification passes; leftward supercausal displacement gives exactly 2^(|s|+p) anchored rows, not rotation classes. TC5's all-S classification passes after using spatial periodicity to make time reversible and shear to transport left period six to the entire right exterior. Census outcomes and damage measurements remain in Cloud/Local's owner-requested lane; no rerun or numerical verdict.


GC726 follow-up to the turning-row corollary (serves Q6): actual all-S left-half equality with the ring forces every global shear displacement to satisfy s=14p mod84, regardless of right-exterior periodicity. Negative s transports exact period six rightwards by forward time and is classified by GC687 without a strict-speed premise. Positive subcausal s only gives delayed right periodicity; extra rows remain unclassified. Hand reading pending, no census extension.


**Noncritical turning-row spatial closure proved by hand (GPT GC727; serves Q6; reading pending).** Left permutivity supplies a finite deterministic leftward window map whenever s<p; TR(a) covers s>p. All turning rows outside critical s=p are therefore spatially periodic. All-S uniqueness extends to every noncritical direction; remaining critical all-S vectors have p=s a positive multiple of 84. The ring satisfies those critical identities, but additional-row uniqueness is open. No nonempty finite-left row can have any global turning identity, since its edge forces noncritical s=-p. No one-column clock exclusion or new census.


GC728 critical finite-defect guard (serves Q6; hand reading pending): relative to the reviewed ring, a rightmost finite difference persists under G=shift-left F, and its next-left difference accumulates the common column's white parity. The ring has 41 white residues per 84 G-ticks, so critical p=84m with odd m cannot support a distinct finite-defect row. Even multiples and infinite right defects remain open; no global uniqueness claim.


GC729 updates the critical finite-defect guard (serves Q6): a second paired parity requires p divisible by 336. The next site has an even 168-tick white count, so the same doubling shortcut stalls; no exclusion at multiples of 336 or infinite-defect conclusion. Hand reading pending.


GC730 critical-front shortcut stopped (serves Q6): the leftmost-difference speed cap of one site per tick is false even for a two-bit finite defect of the known ring (1010 to 1100 at sites 44..47). GC507 already supplies the general unbounded-jump guard. No restricted critical all-S cap proved. Cloud's Proposition 23 ruler-sequence hand argument separately passes the requested independent audit; exploratory computation not replayed.


GC731 critical boundary reduction (serves Q6; hand reading pending): any G^p-periodic row with p=84m agreeing with R on an initial left half agrees with its physical history on an expanding halfline, hence is eventually all-S at the fixed wall. A distinct row cannot coalesce into R. Critical all-S uniqueness is equivalent to excluding non-ring left-asymptotic extensions in that critical local constraint; no extension or finite-graph computation supplied.


GC732 closes blanket spatial-periodicity extension across the critical direction (serves Q6 scope): a left-checkerboard/right-white interface satisfies F^2(x)=shift-right-by-2(x) and is nonperiodic in space, by hand. It is not all-S and does not answer the ring's critical uniqueness question. No computational census or new novelty claim.


GC733 dyadic-tail splice route closed (serves Q6; hand reading pending): a uniformly q-periodic G-right tail can supply only periods dividing q*2^k to the left. Critical all-S left matching gives a least-84 G-column, forcing 21|q. Thus white/checkerboard right-tail terminations are impossible; backgrounds carrying the odd factor 21 and nonuniform right tails remain open. Existing diagonal integrator mechanism reused, no census.


GC734 adjacent-pair refinement (serves Q6; hand reading pending): odd parts o_i of least joint G-time periods obey o_i | o_(i+1). A critical ring-left extension therefore has 21|o_i at every adjacent pair; for p=84*2^k all o_i equal 21. The invariant eventually stabilizes for any fixed p, but this implies neither spatial periodicity nor unique profiles. No continuation constructed.


GC735 mixed duration budget (serves Q6; hand reading pending): recomputing J(a)=J_0+a gives same-letter duration <=a+J_0+20 and logarithmically many S/L changes by marker time T. Formal S^(2^j)L blocks respect these budgets with vanishing L density, so separate run bounds cannot exclude sparse aperiodicity or yield a global deadline. Actual inter-run compatibility remains the missing input.


GC736 fixed-lag left-band scope audit (serves the ordered-band/core lead; hand reading pending): unbounded eventual diagonal periods force every fixed dyadic-lag B_P to saturate at the finite first period not dividing P. Its physical curve then has x/t -> -1. Finite-window quarter-speed fits remain evidence; a growing-lag or separate settling-front limit remains open. No rerun.


GC737 sparse formal control (serves Q6; hand reading pending): W=S^(2^j)L respects GC735's monochromatic budgets and has C-V(i')<=8-5j' for every common macro-start prefix with later start in block j'. It therefore escapes GC711's fixed-slack marker-aligned sufficient near-square test. Physical admissibility and arbitrary-phase tests remain unclassified; a concrete gap for actual inter-run/support reasoning is retained.


GC738 settled-band/S-slab obstruction (serves Q6 and the band/core lead; hand reading pending): a settled left-edge diagonal e<=J(a) of dyadic period q gives D<=J(a)-e+2q+54 for an S block. Ring stride -15 profiles have least period 28 by certificate arithmetic, so long overlap is impossible. Useful only with actual onset/depth/period data or bounds; no uniform band supply or sparse-word exclusion asserted.


GC739 bounded sparse-word exclusion (serves Q6; hand reading pending): existing universal white diagonal e=53207 settled by 107312, combined with ring edge-frame maximum white run five, forces J_0>=53053 for W=S^(2^j)L through its j=15 S block (time393360). Thus the J_0=5 formal control is physically excluded, while larger finite distances remain unclassified. No certificate or dynamics rerun; an unbounded band supply remains missing.


GC740 onset-crossing extension (serves Q6; hand reading pending): a settled white diagonal intersects the forced S slab starting at max(0,T-a,e-J), giving D<=J-e+2*max(0,T-a,e-J)+10. Existing e53207/T107312 yields the universal S budget min(J_0+a+3,J_0+abs(a-107312)+54115). W block14 excludes J_0<=35314 before block15's stronger exclusion. Fixed certificate depth still cannot exclude every finite J_0; no new run.


GC741 repeat-offset gap CLOSED (serves Q6; hand reading pending): synchronizing1s in100/10000 align arbitrary visible near-squares to macro starts with fixed-slack loss at most12. GC737's sparse W therefore also escapes arbitrary-offset Corollary F repeats. This supplies no admissibility and changes no GC739/740 support exclusion. Stop repeat-offset refinements; actual unbounded compatibility remains missing.


GC742 conditional sparse-word period-growth obstruction (serves Q6/Q7; hand reading pending): every actual W=S^(2^j)L requires liminf log2(P_e)/e>=1/10 along its eventually white diagonals, by tau(e)<=e*P_e and the actual white/S overlap. Subexponential prefix-period growth on an unbounded white subsequence would exclude W for all finite J_0. No such all-history estimate follows from current certificates; white infinitude alone is insufficient. No run or unconditional Q6 exclusion.


GC743 AL method hand reading (serves Q6/portfolio4): fixed temporal10 transfer passes; unique incoming profile edge makes the finite live set a union of cycles. The reported155-cycle covers all155 live pairs and supplies the single-cycle rigidity premise missing from an outdegree1-only explanation. No census/ring/cost replay; L381's unrestricted six-column slab after two loops still awaits an actual cross-return proof. ALS-P1 failure retained.


GC744 universal four-column L slab (serves Q6/portfolio4; hand reading pending): any marker-aligned L followed by L begins111001 and renews1110, forcing the first four ten-time profiles; no period premise on farther columns. The short-word six-column stabilization conjecture is refuted by L384/ALX-Q4/Q5; a finite-future startup gate remains open. UB's sampled branch choice does not override G2.3's two certified finite-seed branch witnesses; no all-history period-growth estimate or new run.


GC745 exact all-L cost (serves Q6/portfolio4; hand accepted by L386): closing-inclusive inversion fixes the initial ring prefix through10n. Stored155-ring bits yield J>=10n-6, equality exactly n17mod31; finite white-padded cuts attain every minimum. Dropping the closing tick changes eleven residue minima despite the same maximum slack6. Dynamics certificate received, not rerun; finite-horizon result only. L384's short-word startup refutations retained; next finite-future gate.


GC746 finite-future transfer (serves Q6/portfolio4; conditional hand reading pending): fixed K10 loop3 sites5..6 UNSAT would force six period10 near-wall columns on every infinite synchronized all-L trace after30 ticks, by translating each actual loop to loop3. Finite L^K budget k>=3,K-k>=7 suffices. K10 loop2 site5 similarly yields time20. L388 reports checked DRAT proofs for both fixed cases, supplying the certificate side; GPT read the encoder and translation but did not replay the checker. Seventh-column finite SAT witnesses do not establish infinite freedom.


GC747 noncritical all-L turning class CLOSED (serves Q6/portfolio4; hand reading pending): GC727 spatial periodicity plus the forced adjacent all-L pair fixes the whole155-ring without six-column startup. Ring vectors p=2r,s=31r mod155; critical identities begin at310 and ring G-period is310. Critical uniqueness open. L387's received DRAT-checked K7 loop5 gate gives a sufficient five-past/one-following-loop slab, not a hand explanation of five; ALF “never” entries remain bounded through K18, explicitly qualified by L389. No new computation.


GC748 reset-floor scope (serves band/core lead; hand reading pending): reset recurrence bounds unrestricted onset, but a fixed-lag P floor must stop at finite j_P. The unrestricted-onset frontier grows without bound without a rate; B_P eventually saturates. FS's tau array records P-prefix onset, not individual settling; measured c means only supply finite-prefix floors. No FFT or dynamics replay; correction requested while preserving finite data.


GC749 critical all-L period guard (serves Q6/portfolio4; hand accepted by L391): every critical all-L row has310 dividing p, by its forced left half and G's directed cone. First finite-defect parity route CLOSED without exclusion:155 even-phase plus155 odd-phase sites give87+67=154 whites, so no additional odd-multiple obstruction. Initial white parity alone is invalid. No critical existence/uniqueness conclusion, orbit or census.


GC750 second critical all-L defect guard (serves Q6/portfolio4; hand reading pending): despite first even white sum154, the weighted second increment has static sum81 odd and complements after310, forcing620 dividing the period for distinct finite defects. Initial primitive/time/spatial phases cannot cancel it. Infinite right defects and critical uniqueness remain open; no indefinite doubling claim or dynamics run.


GC751 third critical all-L guard (serves Q6/portfolio4; hand reading pending): primitive block xor is odd from87/67 even-index whites, making candidate b-1's white parity odd. Third defect complements after620, requiring1240 dividing p for distinct finite defects. Next paired site cancels with310 whites over620; unlimited doubling route CLOSED by that cancellation. No full-period1240 construction, infinite-defect exclusion or dynamics run.


GC752 lag-plateau lemma (serves band/core lead; hand reading pending): B_P(t)=B_2P(t) forces equality at every integer multiple by a reset at the first failure. The period-at-most-t ordered prefix is B_Q(t), Q largest dyadic<=t; for dyadic P and t>=P the plateau certifies identity with B_P at that time. This supports checked finite windows, not asymptotic fixed-P growth or a rate. RF/ASF failures retained; no new computation.


GC753 boundary reconstruction audit (serves Q6/portfolio4; hand reading pending): after received S13/L6 slabs, exact mask plus child-update filters leave non-ring controlled-strip profiles. Cross-loop constraints are explicit; free temporal drivers do not prove autonomous infinite extensions. Immediate propagation alone cannot explain a saturation width. Next coupled reconstruction, no width sweep or ratio law.


GC754 updates GC753's Q6 reconstruction lead (hand reading pending): the S zero controlled strip has no autonomous continuation, by a forced site15 black-to-white contradiction. Actual S14 even samples satisfy z=x, u OR x=1 and next u<=x. No general rigidity or saturation width follows; stop shallow filters and seek a coupled invariant.


GC755 right-front scope audit (serves band/core lead; hand reading pending): every nonempty finite seed has unbounded pure dyadic right periods by opposite support-edge speeds, so its age-t ordered prefix grows without a rate. Generic count-versus-prefix identification requires monotonicity; seed11 refutes transfer of the single-cell literal white-run ruler. No new computation.


GC756 refines GC755's band/core scope (hand reading pending): joint prefix periods Q_j give a generic initial-seed return ruler H(t)=R_prefix(2^v2(t)) and the exact finite-window comb formula. Counts use Q_j, without assuming individual-period monotonicity. Prefix grows at least floor(log2(t)); no upper rate, generic white triangles or infinite-series claim. No run.


GC757 receipt updates GC754's Q6 reconstruction lead: Local L396/60b36433 independently hand-accepts the S14 gate and reports20 finite controlled windows; no autonomous sufficiency or ceiling follows. Arithmetic twin audit serves the edge/core interpretation only: exact classical ruler and bit periods, no Rule30 asymptotic rate or Mahler support bridge. No run.


GC758 critical-tail audit (serves Q6/portfolio4; hand reading pending): truncation residual is confined to moving strip[b-2p+1,b]. Existing finite-defect parity forces it nonzero for nonempty patches at310|p,1240 not dividing p. Its coordinate can escape, so naive truncation transfer to infinite tails is CLOSED. No infinite exclusion or period1240 construction; next fixed-coordinate invariant/tail classification.


GC759 refines GC758's Q6 critical-tail lead (hand reading pending): at any fixed G-period p, non-ring all-L existence has an eventually spatially periodic right-tail representative, by a cycle in the p-profile pair graph. Full left profiles preserve the actual wall forever. Tail need not be aligned R; no finite-defect transfer, candidate or absence theorem. Next critical periodic-background/bridge classification, no exponential graph run requested.


GC760 refines GC759's Q6 critical bridge target (hand reading pending): every adjacent G-time pair retains odd155; periodic right background q satisfies155|q|p, excluding dyadic tails/pairs. Spatial background period at least8, not necessarily155. No alternative or absence theorem. Local L397/c95e3129 independently hand-accepts GC758's cutoff residual proof and scope.


GC761 updates GC748/752/755/756/757's band/core audits: Cloud CL077/bf54caa5 independently hand-accepts all five and publishes scope corrections. LE source indexing plus an unexpected censoring guard verifies the finite-window use of received plateau data as C(t) on1024..524288. No replay/rate theorem; generic individual-period monotonicity is unassumed, not refuted. Critical bridge GC759/760 remains open.


GC762 updates GC759/760's Q6 critical bridge target: naive temporal-black-parity conservation CLOSED, since cyclic-time sums retain adjacent-product parity and GC732's actual interface changes black parity. No all-L-specific counterexample or exclusion; next must control correlations or switch lead. Local L398/9171866f hand-accepts GC759 and reports literal ring verification of GC760; readings/evidence received, not replayed.


GC763 sharpens GC756's band/core ruler bound (hand reading pending): no three consecutive joint-prefix doublings after an even base; Q_j<=2^ceil((2j-1)/3). Every normalized finite seed has R_prefix(t)>=floor((3 floor(log2(t))+1)/2), without individual-period monotonicity. Two adjacent doublings allowed; no measured coefficient proof/core transfer. Lane changes from stalled critical parity flux; no run requested.


GC764 updates GC763's band/core bound: filed verbatim as G249 in the waiting room after completed duplicate/nearest gate. Local L399 finite-prefix corroboration received; explicit all-depth hand verification still requested. Generic initial-phase control rejects a mandatory staircase. RR2's17 is the maximum decided value only; capped depths remain lower bounds, and Q6 stays open.


GC765 audits Q6's RR2 finite-cone and plateau-start instrument: exact horizon identity validates inherited lower bounds; cone/phase clauses and zero extension agree. Conditional hand source pass, no solver/certificate replay. Capped interval hi is an attained lower bound; finite clock witnesses do not establish infinite clocks. Q6 stays open, no larger sweep requested.
