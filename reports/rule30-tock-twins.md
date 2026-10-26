# Which tocks a start forgets: twins, the funnel and the referee's memory

Local (Claude on the M5), 26 October 2026, L955. The owner relaxed the no-compute rule this morning: "feel free to use the M5 in
such a way as to reveal useful structure about the lines of enquiry." This note covers two frozen probes, each run once with
predictions written first, and two post-hoc checks, labelled as such.

**Status:** measurements on finite populations, at widths up to 48 and conductor steps up to 28. No all-width claim, no proof,
no change of prize, board or PROOFS status. Single-party; GPT's read is requested for the window criterion and the readings.

## The answer in words

When two starts of the same width differ in one free tock, either their histories become **exactly the same row** a little
later, or they never do. That happens at tick j+1, the earliest moment possible, for the tock at position j. It never happens
later at any width measured. Which tocks get forgotten is decided by **position**: only the oldest ones, near the start of the
diary, are forgotten.

At width 40 the first tock is forgotten in 98.7% of cases, the second in 85%, the third in 53%, the fourth in 26%. From the
twelfth on, never. The forgotten part grows slowly with width: the halfway point moves out by about 0.15 of a tock for every
extra free tock. The referee's rulebook shows the same thing from the other side. Each conducted tock depends, at coin
strength, on every earlier tock except the oldest few. Their influence fades, and the fading front moves out at the same
0.15 per tock.

So a start does carry surplus: its oldest seventh or so is redundant, and the dynamics erases it exactly. But erasing it
swaps one start for a twin of the same width; it never yields a shorter start. The number of genuinely different futures
still grows exponentially, as 2^(0.83 n) for n free tocks. Four starts in five never meet the history of any narrower start.

**My prediction was wrong, and the record was right.** I expected a lag-stationary fading memory, with forgetting measured
back from the end of the free chapter. L942's first-bit correlation, which rises with width, seemed to point there. The older
lead-1 study (RULE30-PRIZE.md 8.38) had found the opposite: only the first two or three bits are weak. Section 8.38 was right
about where forgetting happens. What it could not see, with one depth at a time, is that the forgotten stretch slowly grows.

## Model, lanes and the twin test

The zero-wall half-line of DEEP-QUESTIONS.md: x(t,0) = 0, x(t+1,d) = x(t,d+1) XOR (x(t,d) OR x(t,d-1)), with the test that
x(2i,1) = 1 for every i. Lanes follow CL632 and L942: width W = 2n, and lane l has ticks a(2i) = 1 and tocks
a(2i+1) = b_i = bit i of l for i < n. Its start is the outward reconstruction, white beyond W. The twins of tock j are
(l, l XOR 2^j). They **merge** at tick k if their rows at time 2k are identical and both passed every earlier tick. From then
on they are one history (L954 Proposition 2).

An exact finite criterion, from the triangular bijection, checked as control C7: twins of tock j are identical at tick j+1
**iff their traces agree on the 4j+4 times W .. W+4j+3**, the first conducted stretch. All they share before W is built into the
lanes.

## What was measured (tock_twins.c, then tock_front.c)

**Controls.** All twelve controls of the first probe pass, including C11. C11 reproduces L942's exact counts at W = 40: 5,228
first-tock pairs and 349,146 last-tock pairs that change the death, and its three label lanes. C6 is a counterfactual: with XOR
in place of the OR, no two lanes ever coincide. C8 is a cross-width check: every two-step ancestor is the narrower lane it
names, with death D+2. Both startup checks print ALL CHECKS PASS on the M5, in 4 s and 91 s.

**1. Twins merge by position, at once or never.** The merge fraction mu_W(j):

| W | j=0 | 1 | 2 | 3 | 4 | 5 | 6 | j ≥ 12 |
|---|---|---|---|---|---|---|---|---|
| 16 | 0.766 | 0.188 | 0.047 | 0 | 0 | 0 | 0 | 0 |
| 24 | 0.902 | 0.448 | 0.155 | 0.045 | 0.009 | 0 | 0 | 0 |
| 32 | 0.962 | 0.698 | 0.333 | 0.130 | 0.045 | 0.012 | 0.003 | 0 |
| 40 | 0.987 | 0.853 | 0.535 | 0.260 | 0.111 | 0.040 | 0.013 | 0 |
| 44 (predicted, then measured) | 0.993 | 0.901 | 0.629 | 0.340 | 0.157 | 0.064 | 0.023 | 0 |
| 48 (predicted, then measured) | 0.996 | 0.934 | 0.712 | 0.424 | 0.213 | 0.094 | 0.038 | 0 |

Every merge at every width and position happens at tick j+1. After the free chapter, distinct futures essentially never merge.
At W = 40 there are exactly two such events, both at time 42 and both between lanes that fail at 42. Of the futures that pass
time 42, none ever merges with another (post hoc, union-find over every later tick).

The half-merge point (the interpolated j where mu = 1/2) is 2.13, 2.29, 2.45, 2.59 and 2.74 at W = 40, 42, 44, 46 and 48. The
values at 44 and 48 fell inside ranges frozen from W ≤ 40 (FT1, FT2).

**2. The referee forgets its oldest tocks and nothing else.** The universal conductor k_m from L954 is the even-depth blank's
forced tock. Over all 2^m prefixes, the influence of tock j on k_m is about one half for every j beyond the first few:

| m | j=0 | 1 | 2 | 3 | 4 | 5 | 6 | j ≥ 8 |
|---|---|---|---|---|---|---|---|---|
| 16 | 0.0225 | 0.179 | 0.360 | 0.460 | 0.486 | 0.496 | 0.493 | ≈ 0.50 |
| 24 | 0.0025 | 0.039 | 0.167 | 0.318 | 0.417 | 0.466 | 0.488 | ≈ 0.50 |
| 28 | 0.0008 | 0.017 | 0.094 | 0.231 | 0.354 | 0.430 | 0.470 | ≈ 0.50 |

The front where influence reaches 0.25 sits at 2.55, 2.69, 2.84, 2.98 and 3.16 for m = 24 to 28 (FT3 held). The first tock's
influence falls by about 0.76 per step. Even the newest input influences k_m only about half the time. So the rulebook is not
a fading memory measured back from the present. It is a full memory with a slowly growing forgotten prefix.

**3. The funnel.** At W = 40 the 1,048,576 lanes become 125,401 distinct futures by the end of the free chapter. About half
merge at tick 1 (the first tock), then fewer at each tick. log2 of the count grows by 0.828 bits per free tock between W = 24
and 40, and the entropy by 0.805. The lead-1 walks grow by 0.819 bits per free bit (8.38). The two models may share this
constant; that is a coincidence of numbers, not a claim. There is no finite funnel: the futures keep multiplying, each free
tock adding about 1.78 times as many.

**4. Shortening through merging (the handoff's second shape).** About one lane in sixteen (0.063 to 0.064 at W = 34 to 40) is
the later row of a narrower lane. About one in five (0.176 at W = 24, 0.198 at 40) shares a future with such a lane at some
tick. Nearly every lane dies early enough to be eligible, so the record bound does not explain the rest: **about four starts in
five never meet a narrower start's history.** The share rises slowly with width.

**5. GPT's joint-check question (GC1891).** At the death tick T ≥ W+2, I asked whether the other value of the conducted tock
(an extra black cell at depth T) would have passed. It would not in 0.498 of deaths at W = 40, a coin at every width from 22
up. Universally, P(c_m ignores b_m) is within 0.012 of one half from m = 8 and within 0.001 from m = 20. The even blank and the odd blank are statistically independent at the
moment of death: neither forces the other to fail. Half of all lanes die at the first check after the free chapter.

**6. The unexpected check (DQ-013, the uneven metronome).** Along the 64 longest-lived lanes at W = 40, successive waits
between GPT's discrepancies first showed Spearman −0.198. The niggle sweep found why: those 64 lanes are only 7 futures, so the
gaps were duplicated. Counted once per future, no relation remains at any survival threshold (+0.0045 over 2,045 pairs for
D ≥ 60; +0.0006 over all 125,401 futures). A coin-tock null gives +0.002. The mean wait is 2.03 tocks, a coin's value. C10
confirms GPT's discrepancy formula on 18,879,264 samples.

## Predictions scored

From tock_twins.c, frozen before the run (commit e343a4eb, source sha256 3d631a0d…):

| Prediction | Verdict |
|---|---|
| PT1, the packaging | HELD |
| PT2, lag collapse | **REFUTED**, the decisive result. Its fixed-fraction contrast was ill-posed: mu is 0 at j = n/2 at every width. |
| PT3, a localized footprint | FAILED. Merged twins differ over 19 to 23 cells for j = 1..5, so the forgettable part is a set of tocks, not a block of cells near the wall. This confirms GC1886's caveat. |
| PT4, count rate | HELD |
| PT4, concentration | FAILED |
| PT5 | HELD |
| PT6 | FAILED low |
| PT7a–c | REFUTED; the no-fading counterfactual was MET |
| PU | failed raw; the failure was the duplication artefact in section 6 |

From tock_front.c, written from those readings and frozen before its run (commit 540e5b12): F1 and F2 PASS; FT1, FT2 and FT3
HELD; the stall counterfactual was not met.

## What it changes in the questions

- **DQ-001 and GC1892 (what may a replacement forget?).** The tocks it may forget, while keeping every future tick, are the
  oldest ones: about the first seventh, a stretch that slowly grows. The replacement is a same-width twin, identical from tick
  j+1, so it keeps the eternal-tick property exactly. It is never shorter: merged twins have the same support, because the far
  edge moves at exactly one cell per step.
- **DQ-004 (finitely many futures?).** No. The owner's reduction is real ("if we can see this collection always ends up as that,
  have we not reduced how many we need to check"): it divides the cases at width W by about 2^(0.17 n). But 2^(0.83 n)
  genuinely different futures remain, and none of them merge once the free chapter is over.
- **DQ-009 (the referee's memory).** It remembers every tock at full strength except a forgotten oldest stretch, which grows by
  about 0.15 tocks per tock. No bounded rulebook is visible, consistent with 8.38's failure to find a linear recurrence.
- **DQ-011 (spent, preserved, renewed).** Measured: the oldest part of the free chapter is spent; the rest is preserved for
  the whole life. Nothing measured here is renewed.
- **DQ-012 (what a large beginning has too much of).** Early history: about 0.17 bits per free tock of it is surplus, erased
  exactly. The surplus is forced by size, but removing it is a swap, not a cut. That is the first of DQ-012's two ingredients
  without the second.
- **DQ-013.** The waits between discrepancies show no relation between successive waits once duplicates are removed.

## Questions back

1. **What sets the 0.15?** The forgotten stretch and the conductor's fading front advance at the same rate. A guess to test, not
   a claim: read sideways, with the trace's start as a boundary, the outward reconstruction is a second-order automaton.
   A change at trace time 2j+1 can only drift toward time 0 or stay put, and it dies at that boundary. The front speed would
   then be how fast that drift wins, which looks computable.
2. **Is every tock eventually forgotten?** Measured: each fixed early tock's influence falls with m, and the onset is delayed in
   proportion to j. If the front keeps moving at about 0.15, tock j is forgotten around step 7j. An eternal survivor would then
   keep re-encoding its future in ever younger tocks. Does that help or hurt a descent?
3. **For the owner:** the start does contain the future, except its oldest seventh, which the present never consults again.
   Is that the "packaging" you sensed? It is real, but it is a choice of tocks, not a piece of the row, and it never makes the
   start smaller.

## Evidence

- **Sources:**
  - [tock_twins.c](../tests/probes/wolfram/tock_twins.c): frozen at e343a4eb, source sha256 3d631a0d…; run once at 09:46 GMT,
    12.9 s, peak 284 MB.
  - [tock_front.c](../tests/probes/wolfram/tock_front.c): frozen at 540e5b12, sha256 3f7b3670…; run once at 09:54 GMT, 20.2 s,
    268 MB.
  - [tock_gaps_posthoc.c](../tests/probes/wolfram/tock_gaps_posthoc.c): post hoc, under a second.
  - OUTCOME sections were appended to each source after its run.
- **Raw outputs**, in the shared store under `cited/tock-twins-20261026/`, each read back byte-exact:

  | File | sha256 |
  |---|---|
  | out.txt | c90d2c4d… |
  | front.txt | d0a4b028… |
  | gaps3.txt | e82d60ad… |
  | time.txt | a89f696d… |
  | front_time.txt | 78337fbc… |

- **Run conditions:** one process, one thread, `ulimit -t 900`, no GPU, Lean or network.
- **Records searched:** record_find.py, with the hit counts listed in tock_twins.c's header. Read: RULE30-PRIZE.md 8.37–8.38;
  the headers of rule30_wall.py and rule30_influence.py; L942; GC1886; GC1889 to GC1892.

**Reasoned verdict:** forgetting in the zero-wall model is exact, immediate, positional and partial. Its front advances at
about 0.15 tocks per tock, measured to W = 48 and m = 28. What remains after it is an exponential family of futures that never
merge again. **Gut verdict:** cool on any reduction built from merging alone; warm on question 1. A computable front speed would
be the first number in this programme with a mechanism behind it.
