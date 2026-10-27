# Must the notebook grow? The mathematics of GC1976's question, and a test design

Local, 27 October 2026, at the owner's request: take L1026's positive question further, consider its mathematical
implications, and design a compute test with a counterfactual before flow returns to GPT. **Design only: nothing is
run until GPT has reviewed it.**

## 1. The question, made precise

GPT's question (GC1976): when a traveller returns to "the same room", what must its notebook hold so that the same
exits are guaranteed? Call a notebook (a function N of the configuration) **complete** for an observation O under
the dynamics when equal N gives equal N one step later and equal O.

## 2. Mathematical implications

These are hand statements, labelled. None is new as mathematics; the point is how they line up.

1. **One orbit (elementary).** A complete notebook with finitely many values along one orbit makes O eventually
   periodic: a deterministic sequence of finitely many states cycles. Conversely, an eventually periodic O has
   one, namely the phase in its period. For the centre column of the single seed, *a finite complete notebook
   exists if and only if Problem 1 fails.*
2. **Two columns (from the kit's Jen theorem, `Rule30FiniteConfigs.jen`).** No two different columns of a finite
   nonzero row are both eventually periodic, so **no traveller carries a finite complete notebook for two
   columns**. This is a one-line consequence, for GPT to read (L1026).
3. **The two extremes already in the record.**
   - At the moving right edge, k cells are a complete notebook for ever (S1: T closes mod 2^k).
   - Beside a static wall, none of fixed size is complete (L1013: F = ⌊T/2⌋ reads one new deep bit per step).
   - Theorem S (S2) is the template "complete bounded notebook plus forced encounter with a known edge". It cannot
     reach the centre, because the notebook needed there grows like t, and it repeats only after p_(t+2) ≈ 2^(0.4t)
     steps.
4. **At the level of sets: the period-two problem splits into two notebooks** (PERIOD-TWO §5, RULE30-PRIZE §8.86).
   - *Delivery side* (the right half beside the 0101 wall). The notebook is the follower-set automaton of the
     visible language L. If L were sofic (finitely many follower sets), the period-two question for left-finite
     configurations would become a finite-automaton check (§8.86). The proved **death criterion**: if L is sofic,
     the sets L^(j) of words still occurring from visible time j on are eventually constant in j. So *deaths at
     arbitrarily late visible times prove that the delivery-side notebook must grow without bound.*
   - *Cost side* (the left half). Board item Q1: keeping the wall's conditions costs information at a positive
     rate, N(T+k) ≤ 2^(c − αk) N(T). This is open, and parked since the fifth triage. A uniform linear deadline
     T ≤ cj + b gives Q1 with α = 1/c (PROVED, L345/CL161).
5. **Where the notebook question becomes testable.** The positive question ("the needed notebook must grow at a
   positive rate") is Q1 on the cost side, and non-soficity of L on the delivery side. The delivery side has a
   proved, one-directional, finitely testable criterion: late deaths. The cost side has no such test. So the test
   goes on the delivery side.

## 3. What is known about late deaths (record)

Sources: §8.86 with the skeptic's correction and Cloud's correction of 2026-10-11, and Intel's door D5, two
independent SAT encodings with DRAT.
- *Minimal death times:* 0 to 6, 8, 9, 11, 12, 14 and 16.
- *Later deaths:* 0010001 at visible time 32, 1000101 at 34, and a length-20 word at 43.
- *Latest death by length:* 34 for every length from 7 to 19.
- *A gap:* no word of length 7 or 8 dies between visible times 35 and 100.

So short words appear to stop dying, while a longer word dies later. The notebook picture predicts the second
pattern in general: a death at visible time j needs information from about depth 2j of the right half (light cone),
so constraints that kill longer words should keep arriving later.

## 4. The test: does the latest death time keep rising with word length?

**Quantity.** Let D*(n) be the latest visible time at which some word of length at most n dies (leaves L^(j)), within
a fixed visible-time horizon J. D*(n) is nondecreasing in n by definition. Known so far: D*(n) = 34 for 7 ≤ n ≤ 19,
and D*(20) ≥ 43.

**Hypothesis G (the notebook must grow).** D*(n) is unbounded. Concretely:
- **P1.** For each n from 20 to 24 there is a death later than 43 with J = 160; that is, D*(24) > 43.
- **P2.** The new late deaths step up with length, not all at one time: at least two distinct new death times
  above 43 appear among lengths 20 to 24.

**Counterfactual H0 (a finite delivery notebook).** D*(n) = 43 for every n from 20 to 24, up to J = 160, with no word
of length at most 24 dying in (43, 160]. That is evidence, not proof, for soficity of L. If L were sofic, the
period-two question for left-finite configurations would reduce to a finite-automaton check, which would be a very
large positive step, and H0 would be the first sign to pursue it.

**Either outcome is informative.**
- *P1 holds:* the death criterion's question gets a new data point against soficity. Any family of late deaths with
  a pattern in n is a candidate for the infinite family that a non-soficity proof needs, and that the §8.86 lane
  could not find.
- *H0 holds:* the cheap prize-relevant route (a finite automaton) becomes the next block.
- *Neither cleanly* (deaths above 43 but only at one time, or only at n = 20): reported as inconclusive. No
  extension of n or J without a fresh design.

**Unexpected check (before the main run).** Rerun the method on the two known deaths, 0010001 at 32 and 1000101 at
34, and on the length-20 death at 43. It must reproduce all three (a positive control). It must also report no
death of a length-7 or length-8 word in (35, 100] (a negative control from D5). If either control fails, the
instrument is wrong and the main run does not start.

**Method.** Reuse D5's SAT encoding: the right half beside the clamped 0101 column, a finite right row, and the
visible word w required at visible times j .. j + |w| − 1.
- *Occurrence profile.* For each word w ∈ L_n (n ≤ 24, from the record's exact L_n tables to 26) and each visible
  time j ≤ J, ask whether w can occur at time j. A death at j means occurrences before j and none at any time from j
  to J.
- *Pruning (correct by factoriality).* Extensions of an already-dead word need no search, since they die no later.
- *Size.* L_24 holds at most a few thousand words. Each instance has about (2J)²/2 ≈ 51,000 cells at J = 160.

**Caps.**
- Each SAT call gets 30 s. A timeout is recorded as UNKNOWN, never as a death or a survival.
- The whole stage gets 4 CPU-hours, as 8 parallel kissat processes on the M5 under `run_capped.py`, with 4 GiB of
  memory and 1 GiB of disk.
- If the caps bind before n = 24, the stage stops at the last complete length and reports that length.
- No GPU, and no rerun without a fresh agreement.

**Retention.** Every death claim keeps its witness rows (the last occurrence) and its UNSAT certificate (DRAT) for
the absence window, in the shared store's `cited/`. Counts alone are not evidence.

**Record searched:** "Myhill", "follower set", "sofic", "death criterion", "entropy.{0,40}survivor",
"free bits.{0,40}entropy", "coupled language". The relevant prior work is §8.86 and D5 (late deaths), PERIOD-TWO §5
(Q1 and the channel bound), and GC1976 and L1026 (the notebook framing).

## 5. What the test cannot do

- It cannot prove non-soficity: deaths up to J are finite evidence. A proof needs an infinite family with
  membership proved for all lengths. The test's value is to find the family's pattern, or to see that none appears.
- It says nothing about the cost side (Q1), the single seed's centre column, or Problem 1 directly.
- It is a test of the delivery-side notebook only. The coupling with the left side remains the CQ01 question.

## 6. For GPT's review

1. Is D*(n), defined over L^(j) with horizon J, the right operational form of the death criterion? Does D5's
   definition of "dies" match it exactly?
2. Are the controls sufficient, and is J = 160 enough to separate P1 from H0?
3. Is there a cheaper hand route first? For example, a proof that some specific word family dies at visible times
   that grow linearly in its length.
4. Which host runs the stage: D5's encoding lives with Intel's earlier swarm.
