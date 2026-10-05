# Rule 30, Prize Problem 1, period 2: where it stands

*A handover, written 2026-10-05 so that the work survives a move of compute, a new machine, or an outage. For a
person, or for an assistant given this file: read it, then the documents it names in the order given, run the
checks at the end, and stop. Do not start an experiment you were not asked for. Run `git log --since=2026-10-05` to
see what moved after this was written.*

## 1. The question

Wolfram's Rule 30 Prize Problem 1 asks whether the centre column of Rule 30, started from one black cell, ever
becomes periodic. The work here attacks it **period by period, for every finite starting configuration**, which is
stronger than the prize needs.
- **Period 1 is closed.** Condrey proved that no nonzero finite configuration has an eventually constant centre
  column (arXiv:2609.09431, 2026-09-08).
- **Period 2 is open.** That is the case worked on here: can a finite configuration's centre column be 0101...
  from some time on? Condrey's own conclusion names it as the next unresolved case.

Rule 30 is $x_{t+1}(i) = x_t(i-1) \oplus (x_t(i) \lor x_t(i+1))$. It is permutive in its left neighbour, so it can be
run sideways: given columns 0 and 1 for all times, every column to the left is determined (the *forced left half*,
RULE30-PRIZE.md §5).

## 2. The chain of statements

Each line implies the one above it. Section numbers are in RULE30-PRIZE.md.

| Statement | Where |
|---|---|
| **Prize Problem 1, period 2**: no finite configuration has its centre column eventually 0101... | §1, §8 |
| **B**: no finite right half makes the forced left half for 0101... eventually zero | §8, §8.11 |
| **LR_m** for some layer width $m$: no input to a width-$m$ layer next to column 0 makes it eventually zero | §8.11 |
| **LR (= LR_0)**: no column 1 at all makes the forced left half eventually zero | §7 |
| **R(d) is finite for every d** (equivalent to LR, by König's lemma) | §8.36, PRIOR-ART |
| **The doubling conjecture**: R(d) <= d + 4 | §8.36 |

R(d) is the longest zero run of the forced left half that starts at depth d, over every column 1.

The same question has several exact forms, each checked against the others by a probe:
- **The forced walk** (§8.37). A zero run from depth d is one deterministic walk per prefix of column 1: at every
  other cell, column 1's newest bit is forced.
- **The wall form** (§8.39). Run Rule 30 on the half-line $x \le -1$ against a wall at $x = 0$ that alternates
  white and black. The forced left halves are exactly the evolutions in which the cell beside the wall is black at
  every odd time.
- **Black, white and both** (§8.40). At the wall's black times the condition involves the left half alone. At its
  white times it couples the left and right halves. A finite configuration must keep both.

Known theorems used:
- **Jen (1990), via Kopra**: two adjacent columns of a configuration with an eventually zero left half are never
  both eventually periodic. So no eventually periodic column 1 can work (Proposition 7, §8.13).
- **The channel bound**. Next to 0101..., column 1 carries at most about 0.13 bits per visible bit (0.064 per step),
  whatever the right half. The figure is 0.128 by power iteration (§8.20), certified as 0.1292 in integer
  arithmetic (§8.33).

Proved here (2026-10-05, Local; each is elementary and has a pre-registered check):
- **Theorem A, Jen with a clock** (§8.54). Two adjacent columns cannot both be $P$-periodic on a window $[a, b]$
  unless $b \le 2a + L + 2P - 1$, with $L$ the distance to the left edge. Jen's theorem is $b = \infty$.
- **Theorem B** (§8.54). With $P$-periodic columns 0 and 1 ($P \ge 2$), no zero run of the forced left half is
  longer than $2P - 2$.
- **Theorem E** (§8.57). If column 1's visible bits are a Sturmian sequence, the forced left half is never
  finite. So LR holds for every pure rotation, rational (Jen) or irrational.
- **Theorem A′, the window principle** (§8.58). A block of two adjacent columns recurs at time $a'$ only if its
  length is at most $L + a'$. It contains Theorem A and has a two-line proof. Its Collatz twin is Terras's
  bijection (PRIZE-PROBLEMS.md §7.5).

## 3. What has been measured

All numbers come from probes whose predictions were committed before they ran. Each probe's header records its
OUTCOME.

- **R(d), exact** at depths 1 to 61, 65, 69, 73, 77 and 81 (§8.36, §8.37). R(81) = 65, R(d) <= d + 4 at every
  depth, and R(d) - d is about -0.18 d.
- **Distinct forced walks** at depth d (§8.38): about $2^{0.41 d}$. Each free bit multiplies them by 1.764, not 2,
  because about 6% merge at every step.
- **The record is the best of those walks** under coin flips (§8.38): $R(d) \approx 0.826\,d + 0.8$. This
  predicts depths 49 to 81 within 4.1 cells.
- **Column 1 next to 0101..., from a real right half** (§8.4 to §8.11): the wheel $U$, an exact coding of the
  rotation by 17/56, kicked by domain walls in notches of 1/28 turn.
- **The best finite seed for 0101** (§8.24): its total width plus at most 9 steps, for right halves up to 32 cells.
- **The same for every word up to period 4**, and for a random word (§8.42): total width plus +6 to +10, growing
  like a logarithm of the depth.

## 4. Routes closed (do not reopen without new evidence)

- **Bounded runs from a thin layer**: at every layer width up to 16 the zero runs still grow with depth (§8.14).
  So no local rule of column 1 bounds them (§8.41).
- **Periodic column 1**: settled by Jen's theorem (§8.13). The 550,201 periodic words searched were a check of the
  instrument, not evidence.
- **"Structured families" beating chance**: luck (§8.16).
- **The entropy squeeze as a reduction** (§8.33). It restates the problem. It needs a lower bound on a column's
  entropy that nobody has.
- **The SAT crib** (§8.37): correct, but slower than enumeration.
- **A merging lemma as the easy half** (§8.38, corrected). A merge needs black cells, so it is the original
  problem's flavour again.
- **A Chebyshev-type exact identity in the survivor counts** (§8.41): none is visible.
- **"Periodic words hold deep zero runs down"** (§8.42): refuted.
- **The wheel's rigidity as a bound** (§8.44). The kick game's runs grow like the coin's. The timing cuts them, but
  does not stop them.
- **Self-similarity between depths d and 2d** (§8.36, RC5): none beyond chance.

## 5. The one missing statement

Every form of the problem ends at the same sentence: **keeping the wall's conditions costs real information.** The
delivery side is a theorem (the channel bound). The cost side holds exactly only next to a constant wall. There
column 1 can only turn black once, and that is Condrey's proof. Next to 0101 it holds only as a coin model: each
condition costs about one bit, and luck adds a logarithm, as in Cramér's model of prime gaps (PRIOR-ART, the owner's
zeta note).

**Why it is hard.** The measured law holds for a random centre word as well as for periodic ones (§8.42), so a proof
cannot come from properties every word shares. It must use what is special about periodic words, as Jen's theorem
and Condrey's proof do. The one structure found that exists only next to the 0101 wall is **the wheel**: no other
trace tried turns a wheel of its own (§8.8). The likely shape of a proof is a size argument, like Chebyshev's
proof of Bertrand's postulate, and not a proof that Rule 30 is random.

**Where it sits** (§8.45). The problem has the structure of Mahler's 3/2 problem: the left half is a free full
shift, column 1 is a thin constrained language, and the two must agree at the wall for ever. Mahler's method
proves emptiness only when the constrained side is finite, which is our Jen and Condrey cases. It stops where the
constrained side has positive entropy, as next to 0101. That is where Mahler's own conjecture has been open since
1968.

**What the other fields offer** (§8.47). A survey across biology, physics, chemistry, molecular machinery,
mathematics, computing, the long shots and the Game of Life found no field that holds the missing statement.
It found the same gap everywhere: theorems that holding a chaotic system costs information are about sets of
cases, and the prize is about every single case. The gap has been crossed only by finiteness and by extremal
arguments for single trajectories. §7 turns that into questions.

## 6. Live leads (2026-10-05)

1. **The wheel's kicks** (§8.43, §8.44). A kick's size comes from the interior, not from the wall's origin, its
   width, or the cells at arrival. Its timing and alphabet are rigid. The kick game, a wheel kicked only at its
   arrival phases, still has the coin's growing runs. So the wheel narrows the cost-side statement to a kicked
   rotation, but does not prove it.
2. **Local's depths 85 and 89** (CLOUD-LOCAL.md, lead M4). Depth 85 is in: R(85) = 73, and the blind prediction
   (65 to 75, MG8 in `rule30_merge.py`) held. Depth 89 is pending, predicted between 69 and 79.
3. **Job M3** (CLOUD-LOCAL.md): the channel bound at layer widths 27 and 28, and the counterexample search to 34
   cells.
4. **The wide survey's imports** (§8.47): Flatto, Lagarias and Pollington's move to a finite window, a
   machine-found certificate, and a weaker single-seed theorem by an extremal argument. They are written
   out as questions in §7.

## 7. Questions for fresh eyes (2026-10-05)

Written after the wide survey (RULE30-PRIZE.md §8.47), for a person or a system meeting the problem for the first
time. Each question is precise enough to start on, and none is known to be easy.

The survey's one finding frames them. Every theorem found in any field of the form "a low-information drive cannot
hold a chaotic system in a fixed state" is about sets of cases: sets of positive measure, or with interior. The
prize needs a statement about every single finite configuration. The questions are ways across that gap.

1. **The counting form of the uniform law.** Let $N_w(T)$ be the number of configurations supported on $w$ cells
   whose centre column reads 0101... (either phase) at times $0$ to $T - 1$. Prove that
   $N_w(T) \le 2^{w - \alpha T} \cdot \mathrm{poly}(w, T)$ for some $\alpha > 0$. Fewer than one configuration is
   none, so this exact count over a finite family would close period 2. Counting crosses the gap here because the
   seeds are finite. The measured horizon, about $w$ plus a logarithm (§8.24, §8.42), is what $\alpha = 1$
   predicts. Measured (§8.51, `rule30_count.py`): to $w = 24$ the count falls by about $2^{1.05}$ per step, so
   $\alpha$ is near 1 and the bound looks true. Proved there: the conditions paid by the seed's left part halve
   the count exactly; only those paid by the right part, after the left part runs out, are open. The right part
   pays in lumps, with at most 3 free steps in a row and any 8 steps costing 8.3 bits or more (§8.52), so the
   form to prove is a bounded debt: $N_{w,j}(T+k) \le 2^{c(w) - \alpha k} N_{w,j}(T)$, with $c(w)$ allowed to grow
   like $\log w$ (measured to $w = 26$: at most 5 for $\alpha = 0.5$). Past the hull widths that enumeration
   reaches, §8.53 counts right parts instead (an exact identity) to total widths beyond 100. There the constant
   is flat in width even at $\alpha = 1$ (about 10), and it comes from one shallow, structured window where the
   wheel forms; deeper it is about 4.5. The bound
   cannot hold for every centre word: a word
   that is some configuration's own centre column has $N_w(T) \ge 1$ for every $T$. So a proof must use the
   periodicity of 0101, as §5 says.
2. **Flatto, Lagarias and Pollington's move** (§8.45, §8.47). Their partial result on Mahler's problem never beats
   positive entropy. It moves to a nearby window where the constrained side is finite, and then uses pigeonhole.
   Find a condition implied by the 0101 wall under which every admissible column 1 is eventually periodic, then
   apply Jen's theorem. Every local layer language of column 1, up to width 16, has positive entropy (§8.14, §8.20).
   So such a condition, if it exists, is not local in column 1.
3. **A machine-found certificate.** Encode the forced walk inside a zero run as a string rewriting system, and
   search with SAT for an arctic (max-plus) matrix interpretation, or for an automaton invariant with a ranking
   function, that proves the runs end. That is how Yolcu, Aaronson and Heule proved weakenings of Collatz. The
   encoding decides whether a proof exists. Condrey's $H(2, w) \ge w$ rules out any fixed-depth induction, so the
   certificate must scale with the seed's width.
4. **Kari and Kopra's partial result, for Rule 30.** For the automata that multiply by $p/q$ they prove, without
   constructing it, that some set of windows covering almost everything holds no Z-number orbit. The analogue
   would be a set of centre-column words, of measure near 1, that no nonzero finite configuration's centre column
   keeps to for ever. That would be a new theorem about Rule 30's centre columns, short of the prize. It needs
   Rule 30 to be ergodic and mixing for the uniform measure. Checked (2026-10-05): Shereshevsky,
   Monatsh. Math. 114 (1992) 305-316, proves Bernoulli and K natural extensions for surjective one-sided
   permutive automata under conditions on the neighbourhood's ends. Whether Rule 30's neighbourhood (-1, 0, +1)
   meets them was settled from his thesis (Warwick, 1992, Theorem 1.3.3, read): a left-permutative rule whose
   neighbourhood reaches left of the cell ($l < 0$) is $k$-mixing for every $k$ for the uniform measure. Rule 30
   qualifies. So Kari and Kopra's hypotheses of ergodicity and mixing hold.
   **Closed (§8.55).** Their argument was read in full. It applies to Rule 30 at once, but it is about windows of a
   row; for centre columns it is true and empty. It cannot separate a finite seed from any other configuration.
5. **A weaker theorem about every single seed.** Langton's ant's highway is unproved, but every trajectory is
   proved unbounded, by reversibility and an extremal cell. Rule 30 is not reversible, but left-permutivity solves
   it sideways. Is there a statement weaker than B, about every single finite configuration with a 0101 centre,
   that an extremal argument proves?
   **One found (§8.54, Theorem A).** Two adjacent columns cannot both be $P$-periodic on a time window $[a, b]$
   unless $b \le 2a + L + 2P - 1$, where $L$ is the distance to the left edge. Jen's theorem is $b = \infty$.
6. **LR by construction.** A system strong at construction and search could try to refute Conjecture LR: a column
   1, not necessarily from a finite right half, whose forced left half is eventually zero. The exact records make
   it unlikely ($R(d)$ is finite at every depth computed, about $0.8\,d$). A refutation would still teach
   something: any proof of B would have to use the right half's finiteness.
7. **The regime between.** Columns 1 with zero entropy that are not eventually periodic: kicks that come for ever,
   but ever more rarely. Does the forced walk's law stay bounded, as next to a white wall, or grow like the
   logarithm of the number of histories, as the coin says? This separates "zero entropy" from "finiteness" in this
   problem (the correction to §8.45).
   **Partly answered (§8.54).** Kicks cannot thin out faster than geometrically: with $P$-periodic stretches
   between kicks at times $\tau_n$, a finite left half needs $\tau_{n+1} \le 2\tau_n + L + 2P + 2$. Slower thinning,
   and the steady rate of real right halves, stay open.
   **Answered for one class (§8.57, Theorem E).** Every Sturmian column 1 has zero entropy and is never eventually
   periodic, and for every one of them the left half is never finite. Open next: codings by an arc whose ends are
   not on one orbit, rotations of a torus, and Toeplitz sequences.
8. **The fourth game** (§8.49, from the tetralemma). Count the seeds that survive the black, white, both and
   neither games, and measure $N_\text{both} N_\text{neither} / (N_\text{black} N_\text{white})$. A ratio near 1
   confirms the coin model's independence. One well below 1 would be an obstruction a proof could use.
   Measured (§8.51): between 0.66 and 1.34 at $w = 24$, with no trend. Independent up to a constant factor.

9. **The Collatz twin** (PRIZE-PROBLEMS.md §7.1 to §7.3). Through Bernstein and Lagarias's conjugacy, Collatz asks
   the same question as period 2: a bijection permutive in its newest input, fed an input of finite support, and
   whether the output past the free part behaves like coins. Measured to 30 bits: the free bits pay exactly
   (Terras), the count past them follows the coin to 0.5%, and the excess stays below 3.7 bits. Collatz has what
   Rule 30 lacks, arithmetic: after the free bits the state is the explicit integer $3^a + T^{w-1}(r)$, and the
   question becomes bounding exponential sums $\sum_v e(h\,y_v / 2^j)$ over the parity vectors that stay up (the
   2-adic counterpart of Tao's 2019 estimate). The measured Fourier structure fades with width. A proof there would
   show what a Rule 30 proof must replace.
   **Sharpened (PRIZE-PROBLEMS.md §7.4).** For $r < 2^k$, $T^k(r)$ is exactly the least residue of the Syracuse
   offset modulo $3^a$ (proved, checked to $k = 18$). So the twin statement is about the binary digits of a
   remainder modulo a power of 3: Tao's object itself, read in the other base.
   **Carried both ways (PRIZE-PROBLEMS.md §7.5, RULE30-PRIZE.md §8.58).** One exact statement holds in both
   problems, the window principle: a block of the trace can repeat only if it is no longer than the state is
   large. For Collatz it gives, in three lines from Terras, that the parity sequence of an infinite orbit has
   complexity at least $1.71\,n$, so no rational has a Sturmian parity sequence. For Rule 30 it gives Theorem A′
   and only $p(n) \ge n - L$, because a configuration grows a cell a step. Exponential sums cannot reach a single
   case on either side: their error is at least the square root of the population. What would close Rule 30
   period 2 is a lower bound, for one orbit, on the number of contents of the $2n$ cells beside the centre:
   more than $2^{0.13\,n}$.

## 8. Reading order

1. This file.
2. `WORKFLOW-SAVED-MEMORY.md`: the working rules. Predictions are written before runs, failures are recorded,
   prior art is surveyed before leaps, and every script that produced a recorded number is kept.
3. `CLOUD-LOCAL.md`: how Cloud and Local split work, and the ledger (start from main and the ledger, never from
   memory).
4. `RULE30-PRIZE.md`: the honest summary at the top, then §5, §7, §8.4 to §8.14, §8.20, §8.36 to §8.42, and
   §8.45 to §8.47 (where the problem sits among its relatives).
5. `PRIOR-ART.md`: the dated surveys, especially Condrey, Jen and Kopra, Rowland, the prime-gap parallel, the
   siblings in arithmetic, and the owner's wide survey.
6. `tests/probes/PROBES.md`: the index of every probe (row `lexicon/`).

## 9. How to reproduce the core numbers

Everything is in `tests/probes/lexicon/`. Each script's header gives its command, cost and predictions. Pure
Python 3 scripts need nothing else, and the C engines need a C compiler with OpenMP.

| Script | What it computes | Cost |
|---|---|---|
| `records.c`, `rule30_records.py` | exact R(d), the forced walk over every prefix | seconds to depth 61 |
| `records_bits.c`, `records_fast.c` | the same, 64 prefixes per machine word (Local's engines) | 12 times faster |
| `rule30_merge.py` (and mode `recur`) | the distinct walks D(d) and the merge rate | a minute |
| `rule30_wall.py` | the wall form, checked against `records.c` | seconds |
| `rule30_words.py` | black, white and both, for every word up to period 4 | 25 minutes |
| `rule30_race.py` | the information race in the combined game | seconds |
| `rule30_uniform.py` (modes `deep`, `horizon`, `windows`) | total width plus a constant or a logarithm | 15 minutes |
| `rule30_complement.py` | the best finite seed for 0101 (§8.24) | 5 minutes |
| `ladder.c`, `rule30_ladder_deep.py` | the ladder R(m, s) | minutes |
| `entropy.c`, `entropy2.c` | the channel bound | minutes to hours by width |
| `wheel_orbit.c` | Proposition 6's certificate for the pure wheel | minutes per phase |
| `rule30_jenclock.py`, `jenclock.c` | Jen's theorem with a clock (§8.54): Theorems A and B, checked | seconds |
| `rule30_sturmian.py` | Theorem E (§8.57): every Sturmian column 1 is excluded | 2 minutes |
| `rule30_window.py` | Theorem A′ (§8.58): the window principle | 20 seconds |
| `ladder_deep.c`, `rule30_ladder_local.py` | the layer ladder to depth 318, in parallel (§8.56) | minutes to hours |
| `rule30_walls.py`, `rule30_slips.py` | the wheel's domain walls and kicks | minutes |

**The math check.** After any edit of a document with TeX in it, run `python3 tests/probes/mathcheck/check.py
RULE30-PRIZE.md` once `npm install` has been run in that folder. It must report 0 TeX errors and no stray dollar
signs.

## 10. Checks before you start

- `git log --oneline -5` on main and on the working branch. Read the ledger's last rows.
- `python3 tests/probes/lexicon/rule30_wall.py` must print ALL CHECKS PASS (4 seconds). It ties the wall form to
  `records.c`.
- `python3 tests/probes/lexicon/rule30_merge.py` must print ALL CHECKS PASS (14 seconds).
- Then stop, and ask what to do.
