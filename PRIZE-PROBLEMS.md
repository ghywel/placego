# Prize problems a GPU might reach

*Written 2026-10-04 by Cloud at the owner's request: "identify the open mathematics problems with outstanding cash
prizes that may be discoverable inside GPU shader compute". Status checked the same day against the sources linked
in §1, because this field moved in 2026. The notation comes from [LEXICON.md](LEXICON.md). The first experiment's
script, [tests/probes/lexicon/rule30_periodic.py](tests/probes/lexicon/rule30_periodic.py), states its predictions
in its header, written before it ran. On 2026-10-05, at the owner's request, the Rule 30 work (sections 5, 7 and 8,
and the Rule 30 rungs of section 6) moved to [RULE30-PRIZE.md](RULE30-PRIZE.md), with its section numbers
unchanged; this document keeps the prizes as a whole.*

## The honest summary

**Update, 2026-10-05, evening.** §7 records what the Rule 30 work carries to the other prizes. The strongest
transfer is Collatz: the same counting structure, measured to 30 bits, plus the arithmetic that Rule 30 lacks (§7.1
to §7.3).
§8 (2026-10-06) maps the proofs collected in PROOFS.md onto this pool: strong reach for Rule 30 Problem 1 at
other periods and for Collatz, moderate for Problem 2 and some Erdős problems, none for the five other Clay
problems.

No open prize problem is one computation away. The one where heavy computation was the leading line of attack,
Navier–Stokes, was claimed on 2026-09-08, for the case with a smooth external force, and Clay is evaluating the
claim. For the rest, a computer can win in only two ways:

- **Find a counterexample.** This is a finite computation, and it would be decisive (Beal, Collatz, Riemann). For
  each of these, the best heuristics say no counterexample lies within any reachable search.
- **Check the finitely many cases that a theorem has reduced the problem to.** That needs the theorem that does the
  reducing: the idea, which no amount of hardware supplies.

The problem where this project's tools fit best is **Rule 30 Problem 1** ($10,000).
- Its arithmetic is exact bits, so there is no rounding to argue about.
- Its evolution is literally a shader.
- Its frontier moved one step on 2026-09-08, to exactly the case this project's first experiment examines.

That experiment ran on 2026-10-04. Its controls reproduce the published theorem exactly. It found no finite
configuration with a periodic column for periods 2 to 6, over every right half up to 18 cells (27,262,976 cases,
[RULE30-PRIZE.md](RULE30-PRIZE.md) §5 and §6). That is evidence, not a proof, and a proof is what the prize pays for.

**The Rule 30 work has its own document.** Everything done on Rule 30 since then (left-side rigidity, the right side
as a complement, the wheel, the records, the wall form, and where period 2 stands) is in
[RULE30-PRIZE.md](RULE30-PRIZE.md), with its own honest summary. [PERIOD-TWO.md](PERIOD-TWO.md) is the standalone
handover of the period-2 work.

---

## 1. The prizes, as of 2026-10-04

| Problem | Prize | Status | What wins it | Sources |
|---|---|---|---|---|
| Navier–Stokes existence and smoothness | $1M (Clay) | **"Active"**. OpenAI announced finite-time blowup with a smooth external force on 2026-09-08 (Clay's alternatives C and D, with a Lean formalisation). Clay said on 2026-09-11 that the problem "has apparently been settled", with evaluation to follow its rules. A priority dispute has been raised. | Either direction counts (rules §5b) | [Clay](https://www.claymath.org/millennium-problems/), [Wikipedia](https://en.wikipedia.org/wiki/Millennium_Prize_Problems) |
| Riemann hypothesis | $1M (Clay) | Unsolved. Rigorously verified up to height $3 \cdot 10^{12}$ by interval arithmetic (Platt and Trudgian, 2021) | A proof; or a counterexample that "effectively resolves the Problem" (rules §5c) | [Platt–Trudgian](https://arxiv.org/abs/2004.09765), [Clay rules](https://www.claymath.org/wp-content/uploads/2022/03/millennium_prize_rules_0.pdf) |
| P vs NP | $1M (Clay) | Unsolved | Either direction | Clay |
| Yang–Mills existence and mass gap | $1M (Clay) | Unsolved | A proof | Clay |
| Hodge conjecture | $1M (Clay) | Unsolved | A proof, or a resolving counterexample | Clay |
| Birch and Swinnerton-Dyer | $1M (Clay) | Unsolved | A proof, or a resolving counterexample | Clay |
| Beal conjecture | $1M (held by the AMS) | Unclaimed | A proof, or a counterexample, published in a respected refereed journal and approved by an AMS committee | [Andrew Beal](https://www.andrewbeal.com/beal-conjecture), [UNT](https://sites.itservices.cas.unt.edu/~mauldin/beal.html) |
| Collatz conjecture | ¥120M (Bakuage, 2021) | Open. Verified by computer for every start below $2^{71}$ | A proof or a disproof, under the company's rules | [Bakuage](https://en.antaranews.com/news/178694/bakuage-offers-prize-of-120-million-jpy-to-whoever-solves-collatz-conjecture-math-problem-unsolved-for-84-years), [Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture) |
| Rule 30 Problems 1, 2, 3 | $10,000 each (Wolfram) | All open. Partial result 2026-09-08: no column of a nonzero finite configuration is eventually constant (Condrey) | "A full proof ... to the satisfaction of the Prize Committee" | [rule30prize.org](https://rule30prize.org/), [arXiv:2609.09431](https://arxiv.org/abs/2609.09431) |
| Erdős problems | from tens of dollars to a few thousand | 586 of 1,220 solved on erdosproblems.com (2026-09-11), many by AI systems since 2025 | Per problem | [Quanta, 2026-08-03](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/), [erdosproblems wiki](https://github.com/teorth/erdosproblems/wiki/Notable-cases-of-AI-contributions-to-Erd%C5%91s-problems) |

The OpenAI claim is after this assistant's training data. It is reported here as the sources state it, not as a
fact checked by reading the proof.

*Update, 2026-10-05 (from the sources, not from reading the proof).* The Navier–Stokes claim is a construction: a
smooth external force and initial data with finite-time blowup, found by a run of about 10,000 agents over 88 hours
and formalised in Lean. OpenAI says it will not claim the prize. Clay keeps the problem "active" until peer review
([Wikipedia, Navier–Stokes priority controversy][ns-pc]). OpenAI has made no claim on the Riemann hypothesis. It is
reported to be aiming the same system at Riemann and P vs NP. Separately, an Anthropic model raised a proven lower
bound on the share of zeta zeros on the critical line, reported at 67%. It was checked by two mathematicians and
formalised in Lean, and it is not a proof of the hypothesis ([TechCrunch, 2026-08-11][tc-rh]; the figure from
[Live Science][ls-rh]).

[ns-pc]: https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_priority_controversy
[tc-rh]: https://techcrunch.com/2026/08/11/an-unreleased-anthropic-model-made-progress-on-one-of-maths-biggest-unsolved-problems/
[ls-rh]: https://www.livescience.com/technology/artificial-intelligence/this-is-what-happened-with-claude-and-me-ais-failed-attempt-to-crack-the-riemann-hypothesis-led-mathematician-to-a-breakthrough

---

## 2. Two ways a computer can win a prize

**A counterexample** is a finite object that can be checked: three numbers with $A^x + B^y = C^z$, a Collatz cycle, a
zeta zero off the critical line. Finding one is pure search, the kind of work GPUs do best. The question is whether
any lies within reach, and the evidence is heuristic:

- **Beal.** Many exponent patterns are already proved to have no primitive solution by modular methods, for example
  $x^n + y^n = z^2$ and $z^3$ (Darmon and Merel, 1997). The conjectured finiteness of all such solutions (the
  Fermat–Catalan conjecture) leaves very little room.
- **Collatz.** A divergent orbit can never be shown by a finite computation. A cycle would have to be astronomically
  long, and every start below $2^{71}$ is already checked. Tao (2019) proved that almost all orbits attain almost
  bounded values.
- **Riemann.** Every zero up to height $3 \cdot 10^{12}$ is on the line. The statistics of the zeros match random
  matrix theory with no hint of a defect.

None of these is impossible. Each is a lottery ticket.

**A reduction plus a finite check** is how the famous computer proofs worked:
- the four-colour theorem (Appel and Haken, 1976);
- the Kepler conjecture (Hales; formally verified by Flyspeck, 2014);
- the Busy Beaver value $BB(5)$ (2024, checked in Coq);
- the rigorous zero counts behind the Riemann record.

In each case a human idea turned an infinite question into finitely many cases, and the computer checked them.

---

## 3. Ranked for this project

What this project is good at:
- exact GPU programs;
- measurement with controls and counterfactuals;
- determinism across devices (MOLTENVK-NONDETERMINISM-INVESTIGATED.md);
- writing code as mathematics (LEXICON.md).

| Rank | Problem | Prize | Path | Fit | Odds, in words |
|---|---|---|---|---|---|
| 1 | Rule 30 Problem 1 (no eventual period) | $10k | Prove "no finite configuration has an eventually $p$-periodic column", period by period, computing the structure first and then proving it, as Condrey did for $p = 1$. A uniform argument over all $p$ would win. | **Best.** Exact bits; a cellular automaton is a shader; left-permutivity gives an exact inverse construction | Each period is a realistic, publishable target. The uniform argument is the open idea. |
| 2 | Beal | $1M | A GPU modular sieve beyond the published search bounds | Good: exact integer arithmetic, embarrassingly parallel | Lottery. The public record of searched bounds is the sure output. |
| 3 | Collatz | ¥120M | Cycle search, or extending the verified bound past $2^{71}$ | Good: integer, parallel, and already done on GPUs by others | Lottery |
| 4 | Riemann | $1M | Rigorous zero verification beyond $3 \cdot 10^{12}$ | Needs rigorous floating point on the GPU (§4, job G1) | A counterexample is not expected. A new record is a publishable result with no prize. |
| — | Navier–Stokes | $1M | — | — | Claimed, and under evaluation |
| — | P vs NP, Yang–Mills, Hodge, BSD | $1M each | No computational path is known | — | — |
| — | Rule 30 Problems 2 and 3 | $10k each | Problem 2 is a statement about averages, Problem 3 about complexity | Computation gives evidence only | Proof-type problems |

---

## 4. The magician's trick: how a computer takes part in a proof

The owner asked for "the magician's tricks that make maths work". Computer-assisted proofs rest on three, and each
has a word in LEXICON.md.

1. **Exactness.** Integers and bits are exact on a GPU. Rule 30 is a polynomial over $\mathbb F_2$ (LEXICON.md §3.5),
   so a Rule 30 computation either is correct or has a bug. The defence against bugs is the one this project already
   uses: a known-answer control (here, OEIS A051023 and Condrey's theorem), a counterfactual that must fail, two
   independent implementations that must agree, and, at the end, a proof assistant (Lean or Coq).
2. **Enclosure.** Floats are not exact, but the rounding can be bounded or undone. TwoSum recovers the error of an
   addition exactly (LEXICON.md §3.7, check C7). Interval arithmetic carries a guaranteed lower and upper bound
   through every step. That is how the Riemann record was proved. On a GPU the risk is the compiler: a "fast-math"
   rewrite silently destroys TwoSum (C7's counterfactual). So before any float result can count, each GPU must be
   measured (job G1, §6).
3. **Reduction.** A theorem turns "for every $p$" or "for every configuration" into finitely many cases. The lift
   (LEXICON.md §3.6) is the reduction's natural language. "Is this column eventually periodic?" becomes "does this
   operator have an eigenvalue on the unit circle?", a question about the program's loops. Finding the reduction is
   the idea, and it is the part nobody can schedule.


## 5. The Rule 30 work (moved)

Sections 5, 7 and 8 of this document, the Rule 30 work, moved on 2026-10-05 to [RULE30-PRIZE.md](RULE30-PRIZE.md),
with their numbers unchanged. A reference to "PRIZE-PROBLEMS.md §5", "§7" or "§8.x" written before then means that
section of RULE30-PRIZE.md. So do the Rule 30 rungs of §6 (rungs 1 to 3), which moved with them.

---

## 6. The rungs from here

Each rung is a result on its own, whether or not the next one succeeds.

| Rung | What | Who | Status |
|---|---|---|---|
| 0 | The lexicon, machine-checked (LEXICON.md, `lexicon_check.py`) | Cloud, CPU | done 2026-10-04 |
| G1 | Does an error-free transformation (TwoSum, FMA-based TwoProd) survive each GPU's compiler? The prerequisite for any float-based proof on the GPU. Prediction to be written with the job. | Local, Arc and M5, minutes | to be written |
| 4 | Beal: a GPU modular sieve beyond the published bounds; publish the bounds | Cloud writes, Local runs | optional |
| 1 to 3 | Rule 30: the search, the period-2 structure, then periods 3 to 6 | Cloud, Local | in [RULE30-PRIZE.md](RULE30-PRIZE.md) §6 |

The GPU is not needed for rungs 1 to 3 at these sizes. A CPU does them exactly in minutes. It enters if the search
must go much further, or for G1 and rung 4. The project's real advantage is not the hardware. It is the method: a
prediction before every run, a known answer beside every new one, and a counterfactual that must fail.

---

## 7. What the Rule 30 work carries to the other prizes (2026-10-05)

*The owner's question, after a day on Rule 30 Problem 1, period 2: "We don't have a proof but we have lots of clues,
and a huge amount of evidence. Does anything we have learnt here translate over to any one of the other open cash
prize math problems, worthy of study by future fresh eyes?"*

**Where the Rule 30 work ended up** (RULE30-PRIZE.md, the evening update; PERIOD-TWO.md). Every restatement of
period 2 converged on one missing statement: keeping the wall's conditions costs real information. The work took
it to a precise and measured form. The number of configurations on $w$ cells whose centre follows 0101 for $T$ steps
falls by one bit per condition. The bits of the seed's left part pay exactly, which is proved. The right part pays
1.002 bits per condition on average, with a debt that does not grow with width, measured to total widths beyond
100. A count of finite objects that falls below one is zero, so a proof of that bound would close period 2. What
blocks it is the same thing that blocks every relative surveyed: the theorems available are about sets of cases,
and the prize is about every single case.

**Four lessons that are not about Rule 30:**
1. **The decoupling skeleton.** A free side in bijection with the seed, a constrained side of low entropy, and
   agreement for ever. Mahler's 3/2 problem, Collatz, Erdős's ternary digits of $2^n$ and the busy beaver cryptid
   Antihydra all have it. In each, the solved cases are those where the constrained side is eventually periodic,
   and the open case is positive entropy.
2. **Sets against single cases.** Probabilistic and information-theoretic theorems (Tao's "almost all" for
   Collatz; zero-density estimates for the zeta function; data-rate theorems in control) prove statements about
   sets. Single-case theorems come from finiteness or from exact counting of finite objects.
3. **Turn a maximum into a count.** A record ("the longest run is about $w$") cannot be proved by sampling. A count
   ("at most $2^{w - \alpha T}$ seeds survive $T$ conditions") can be, and when the objects are finite a count
   below one is a proof. Split the count by where the free bits come from: the part that pays exactly
   (permutivity, a bijection) is provable at once, and what remains is a precise statement about the rest.
4. **The method.** Predictions committed before runs, a control with a known answer beside every new number, and a
   counterfactual that must fail. Over a day it caught a dozen wrong guesses of mine, each recorded.

**The prizes, by how much carries over:**

- **Collatz (¥120M): strong.** The same skeleton. Terras's theorem (the first $k$ parity steps of $n$ are a
  bijection with $n \bmod 2^k$) is the left part's exact payment. Past the free bits the question is open, as on
  Rule 30's right part. The counting form: if fewer than $2^{w - \alpha T + c}$ numbers of $w$ bits stay above
  their start for $T$ steps, every stopping time is finite and the conjecture follows. Tested in §7.1.
- **Rule 30 Problems 2 and 3 ($10k each): strong for tools, nothing yet for a proof.** The same system and every
  instrument: the wall form, the forced left half, the channel bound, the exact counts. Problem 2 asks for the
  centre column's density, and the counts already measure the pattern statistics of forced left halves.
- **Erdős problems (tens to thousands of dollars): moderate, problem by problem.** Many concern finite structures,
  where an exact count can reach zero. The method suits the kind that fell to AI-assisted search since 2025.
- **Riemann ($1M): weak.** Cramér's model is our coin model, and zero-density theorems are set theorems. The gap is
  the same, and nothing here crosses it.
- **Navier–Stokes ($1M): a lesson, not a route.** A construction with a freely designed force is the analogue of
  refuting LR, not B (RULE30-PRIZE.md §8.47).
- **P vs NP ($1M): a lesson, not a route.** Gates against truth (RULE30-PRIZE.md §8.50): finite checks against
  for-ever statements, with certificates as the bridge.
- **Beal ($1M): weak.** Its objects are finite, so a count could in principle reach zero, but its partial results
  come from modular methods.

**The Collatz sections (7.1 to 7.5) moved on 2026-10-06, at the owner's request, to [COLLATZ-PRIZE.md](COLLATZ-PRIZE.md)**, as its sections 1 to 5, unchanged. That file has its own honest
summary, board of leads and reproduction table. Every reference in the record now points there.

---

## 8. The grimoire against the pool: where PROOFS.md's proofs may apply (2026-10-06)

*The owner's request: a big-picture look at the problem pool of §1, asking where the proofs collected in
[PROOFS.md](PROOFS.md) may have applications. This is an assessment by Cloud from the statements in PROOFS.md (its
sections A to G as of 2026-10-06 midday), not a new result. The proofs themselves were not re-checked here, and
every "applies" below is a lead to test, not a claim.*

**The proofs fall into six families of tools.** Grouping them by method, not by topic, shows where they can travel:
1. **Permutivity and exact bijections.** Lemma 4 (the newest bit enters once, as an XOR), C.4 (the leftward speed
   of information is an identity), C.7 (the first three columns are affine in column 1), and on the Collatz side
   F.1 (the remainder lemma) and G45 (actual-start survival is a residue class cut by a ceiling). Each says that some
   new input enters bijectively, so it can be counted exactly.
2. **Windows of periodicity cannot outlast an edge.** Theorems A, B, A′, A‴, A⁗, Corollary F, Lemmas B1 to B3,
   Jen (Proposition 7) and GPT's half-line form of the periodic-pair obstruction (E.7). These are Jen's mechanism
   with a clock: a periodic stretch must end before the information from the edge arrives.
3. **Rotation-coded inputs are excluded.** Theorems E and E″ (no Sturmian column 1 works, for any arcs at a typical
   rotation number). On the Collatz side, GPT's G34 and G35 exclude Beatty-like parity sequences for rational orbits.
   These are the same kind of theorem in two problems.
4. **Certified counting of constrained languages.** The squeeze (B′ 19), with its spectral-radius bound certified
   in integer arithmetic by a Collatz–Wielandt vector, and the all-period width relaxations (E.3, E.6).
5. **Exact statistics of the uniform measure.** C.3 (the shrink theorem for white triangles), C.5 (the triangle
   law), C.6 (gliders on prime rings, by pigeonhole), and the linear siblings (Proposition 5, by Lucas's theorem;
   the parity invariant for Rule 210).
6. **Collatz survival and Fourier structure.** G39 to G47, all second-read except G47:
   - G39 to G41: survival conditioning, the skeleton phase product, and linearly many free pairs;
   - G42: primitive characters can stay resonant;
   - G43: the exact ternary spectrum of a binary reader;
   - G44: resolution of a finite residue ensemble;
   - G46 and G47: formal ceilings are unbounded, and the first-deficit family realises only by a return.
   Add Dubickas's external bound on divergent orbits (F.2).

**The pool, ranked by how far the grimoire reaches:**
- **Rule 30 Problem 1 at other periods ($10k): strong, already partly reached.** Families 2 and 4 are stated for
  general periodic walls: E.3 holds for every $p \ge 2$ and E.6 for every odd $p \ge 5$, in width relaxations.
  Theorems A, B and Jen with a clock do not use $p = 2$ specially. The record works on period 2, but the grimoire is
  already a period-by-period programme. *Lead:* list which entries in A and B hold for every primitive word as
  written, and which use 0101. Any entry that is fully general narrows Problem 1 to the cases it leaves out.
- **Collatz (¥120M): strong.** Families 1 and 6 were built for it. Family 3 is a bridge: Theorem E's argument
  (rotation-coded drivers are excluded) and G34/G35 (Beatty-like parity sequences are excluded) should be compared
  line by line. One general theorem may cover both, roughly: a permutive finiteness constraint excludes every
  rotation-coded input.
- **Rule 30 Problem 2 ($10k): moderate.** Family 5 proves statements "of Problem 2's kind" for the uniform measure:
  the triangle law, matched on a random row to 0.006% and on the single cell's core to about 0.05%. Problem 2 asks
  the same for the one orbit from a single cell, which is the sets-against-one-case gap again (§7). *Lead:* C.5
  locates where the single cell's statistics already agree with the uniform measure. A proof would need to transfer
  that agreement into the region where it is measured, perhaps with family 2's edge clock.
- **Rule 30 Problem 3 ($10k): weak.** Family 1 gives dependency bounds: the centre cell at time $n$ depends on the
  cell $n$ places to the left, through an XOR (C.4). That is a statement about information flow, not about the cost
  of computing. Problem 3 asks for a computational lower bound, which is P versus NP territory.
- **Erdős problems: moderate, problem by problem.** Three families travel to specific kinds of problem:
  - *Base interplay.* G43 (the ternary spectrum of a binary reader) and G44 (resolving a residue ensemble mod
    $3^a$) are exactly the objects in Erdős's question about the ternary digits of $2^n$ (Lagarias, PRIOR-ART).
    Multiplication by 2 in base 3 is a permutive automaton of Kopra's class, so families 1 and 2 apply as well.
  - *Beatty and Sturmian sequences:* family 3.
  - *Pattern-avoidance and density questions with a finite-automaton structure:* family 4's certified
    transfer-matrix bounds.
  *Before starting, check erdosproblems.com for which of these are open and carry a prize; that was not done here.*
- **Beal ($1M): weak.** Family 1's residue-class arguments are elementary modular arithmetic. Beal's partial results
  come from deeper modular methods, and nothing here reaches them.
- **Riemann ($1M): weak.** G42 and G43 are character sums modulo powers of 3 in a dynamical setting. They say nothing
  about zeros of L-functions. The only link is the coin model (§7).
- **Navier–Stokes, Yang–Mills, Hodge, Birch and Swinnerton-Dyer, P vs NP ($1M each): none.** The proofs are about
  discrete permutive systems and their counts; none of these problems has that structure. The method lessons of §7
  stand, but no proof here transfers.

**Two neighbours with no cash prize, but the best test beds for the tools.**
- **Mahler's 3/2 problem.** Kari and Kopra made it a trace problem of a permutive automaton (PRIOR-ART), so families
  1 to 3 apply as written.
- **The busy beaver cryptid Antihydra.** It iterates $\lfloor 3n/2 \rfloor$, which is the Collatz machinery of
  family 6 with a different constant.

A tool that proves something about either is tested on a problem of the same shape before it is trusted on a prize.

**What to do with this.** The cheapest high-value step is the generality audit of the first lead: for each entry in
PROOFS.md A, B and E, record "general word", "every period $p$" or "0101 only". That turns the grimoire's reach
across Rule 30's periods from an impression into a table, and it needs no new run, only reading.


**GPT scope correction, 2026-10-06 (G49; append to the assessment).** G34/G35 exclude lacunary/geometrically
spaced zero positions, not Beatty-coded rotations; they do not establish the proposed common rotation-coded
bridge. For Antihydra's floor(3n/2) reduction, the parity bijection and residue tools transfer, while the actual
counter barrier has a fair-bit survival probability bounded away from0. The Collatz stopping-time decay target
does not transfer. The selected start8's counter and the original machine remain unresolved. These are analytic
scope qualifications with preregistered controls pending; see RULE30-GPT.md G49. Mahler's automaton transfer
still requires a separate hypothesis audit.

### 8.1 The Erdős space, scoped (2026-10-06, by Cloud, from erdosproblems.com's prize pages)

*Cloud's claimed item from the split proposed in CLOUD-LOCAL.md. Method: the open-problem lists at the $1,000, $500,
$250, $100 and $50 prize tiers of https://www.erdosproblems.com/prizes were read (50 of the site's 57 open prize
problems; the $10,000, $5,000, $78, $44 and $25 tiers, seven problems, were not). Each problem was checked against
the grimoire's tool families of §8.*

- **One direct hit: Erdős Problem #1135 is the Collatz conjecture, with a $500 prize**
  (https://www.erdosproblems.com/prizes/500/open). So the Erdős space does not open a third front for the Collatz
  tools. It is the same front, with a second prize beside the ¥120M one, and anything COLLATZ-PRIZE.md proves bears
  on both.
- **Base interplay: no prize found.** Erdős's question on the ternary digits of $2^n$ (only 1, 4 and 256 omit the
  digit 2?) appears in none of the tiers read. It is active, though. Lagarias's survey (arXiv:math/0512006, PRIOR-ART)
  is still the reference. Ren's "Ternary digits of powers of two" (arXiv:2511.03861) and a repunit reformulation
  (arXiv:2610.03789, October 2026) are recent, and one public repository records a failed attempt of January 2026 with
  a post-mortem. It is the strongest test bed for G43 and G44 (the ternary spectrum of a binary reader), but it is a
  test bed, not a prize.
- **Beatty and Sturmian sequences: no match** in the tiers read. Family 3's exclusions have no Erdős prize target
  found here.
- **Pattern avoidance and densities: many prizes, a loose tether.** The candidates are Sidon sets (#30, #39, #1191),
  sunflowers (#20), van der Waerden numbers (#138), distinct triple sums (#41, #241) and others. These are asymptotic
  statements in additive combinatorics and Ramsey theory. Family 4's certified transfer-matrix counts give exact
  numbers for finite sizes, which can test conjectured constants but cannot prove an asymptotic.

**Revised rating.** §8 rated the Erdős space "moderate". On this reading it is better described as one strong prize
(#1135, in the Collatz lane), one strong but prize-free test bed (the ternary digits of $2^n$), and a loose tether to
the many combinatorial prizes. The seven unread problems in the other tiers should be checked before the rating is
final.

**GPT Mahler scope audit (G50, 2026-10-06).** The base-six multiplication rule depends on the left digit only through parity and is not left-permutive on all six symbols. Binary wall inversion therefore needs adaptation. The fractional half-interval condition also requires simultaneous realization by a nonnegative integer ceil-map itinerary; the formal periodic100 word obeys the fractional condition but misses every such integer start. Families1 to3 do not apply as written. See G50 for proof and limited primary-source reading scope; the general coupling question remains open.
