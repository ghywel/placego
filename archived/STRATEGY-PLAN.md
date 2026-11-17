# STRATEGY-PLAN.md: the strategy swarm's ranked plan, for the owner to decide on

> **Superseded on 2026-10-11 by RULE30-PRIZE.md 8.89 and CL297: read NOW.md first.**

*Written by Intel (the Claude session on the Intel MacBook) on 2026-10-11, after the one-round strategy swarm
that CLAUDE-INTEL-HANDOVER.md asked for finished at 01:58 BST; committed at 02:06, pushed at 02:07, this preamble
rewrapped at 02:08 BST. Nothing here is an instruction to GPT, Local or Cloud: it is a proposal, and Cloud assesses
it (the owner, 2026-10-10 22:45). Status words are the record's:
PROVED (a proof with a second reader; here the agent's proof read by its skeptic and by me), COMPUTED (exact, the
instrument named), MEASURED (statistics), CONJECTURED, REFUTED. "Agent only" marks a computation I did not rerun.
Every agent's code and data are outside git, in the swarm's scratch folder on the Intel MacBook; my own instruments
are there too. The record searches named below were run with `tests/probes/record_find.py`.*

## 1. The plan, in the owner's words

**Try this first.** The check-free conjecture. Over the shift X_4 = {visible sequences with no 11 and no 00000},
which contains the real language in both wall phases (COMPUTED by two agents: X_4 is exactly the width-4 layer
language), no sequence keeps every FORCED cell of row 0 white from some depth on. The forced cells are the odd
depths (standard phase) or the even depths (other phase); the checks are ignored. If this holds, period 2 is
impossible for every finite configuration (PROVED, two lines: a white run of row 0 makes its forced cells white,
and a counterexample's visible sequence lies in X_4). It is a statement about a shift of finite type with two
forbidden words and one deterministic orbit per prefix, and each depth is an exact finite computation.
- First week: the exact forced-only records R^F(d) over X_4, over the width-8 and width-12 layer languages and
  over the twelve-absent-word class, both phases, to depth 120 (two days on this machine; the orbits are
  independent per prefix); a periodic-sequence search to period 22; the decay of the forced-only survivor counts
  along the longest runs on the exact real language to length 30. Then a written attempt at one sub-family (orbits
  through long periodic stretches, where the periodicity theorems already apply).
- Kill: a forced-white orbit that never leaves X_4 (a periodic witness, or a cycle of walk states) kills the X_4
  form and moves the conjecture to the width-8 language; survivors at the cap in the width-12 language with no
  decay over 20 steps kill the check-free route altogether. Then only the full cost lemma is left, which no data
  can kill, and the honest expectation becomes an almost-all theorem, not period 2.
- Convention (PROVED by doors D1 and D2, replicated by Cloud in 8.88): row 0's depth j is site -j; in the standard
  phase (wall white at even times) the visible bits are v_k = x_{2k}(1), depth 2k+1 is affine in v_k (the forced
  cell) and depth 2k+2 is a check on v_0..v_k; in the other phase (wall black at even times) depth 1 is always
  black, depth 2k+2 is affine in u_k = x_{2k+1}(1) (forced) and depth 2k+3 is a check. A forced-only run ends at
  a black forced cell or when the forced bit leaves the language, never at a check.
- What is known: for eventually periodic visible sequences the three agents' Jen-type proofs cover the FULLY
  white tail only; the forced-only periodic case is COMPUTED (judge B: every primitive periodic word in X_4 to
  period 14, both phases; Cloud: to period 10) and its general argument is owed (corrected 2026-10-11 after
  GC1092 and CL268; the first draft of this line said PROVED). From depth 60 every forced-only orbit in X_4 dies
  by depth 154 (COMPUTED by the D2 agent and its skeptic); my
  own run gives the forced-only records 9 8 7 6 5 4 7 6 15 14 17 16 15 14 23 22 at depths 1..16 in the other phase
  and 2 17 16 15 14 13 12 11 10 at 1..9 in the standard phase, finite where exact, with the golden-mean control
  (no 11 alone) infinite in the other phase as it must be. The heuristic predicts these records grow like 1.6 d:
  finite at every depth, never bounded.

**If that fails, this.** The record-ancestry census. The only exact structure any agent saw where the records live:
the record black runs of the free problem stand on clean periodic stretches of period 3, 6, 12, one level of
Rule 30's nilpotent tower per step back, up to level 17, and then dissolve (COMPUTED by the D3 skeptic at depths
13, 32 and 58). Trace every record run (free to 89, real to 152 and the sampled deep witnesses) back in time and
record the longest clean periodic stretch, its period, its tower level and its length relative to the run.
- Cost: four days; the engine exists.
- Kill: on depths 40..89 the clean stretch covers less than half the run at the first step not forced by the
  ones-run lemma, or the level reached does not grow with the run length. Then the tail is structureless and the
  structural route closes too.

**In parallel, at no cost to a decision (instrument changes, mostly Local's to accept or refuse).**
- Lower bounds by sampling. Plain random right halves, about 2 x 10^8 per phase in five minutes at two threads,
  reproduce the exact real record at 100 of the 101 depths 20..120 and give R_real(125) >= 21, (133) >= 23,
  (185) >= 22, (280) >= 26, (435) >= 29, (657) >= 30, (766) >= 33, (1232) >= 29, (1552) >= 31. I verified five of
  these witnesses with my own forward simulation of the whole row without clamping (COMPUTED). So SAT hours should
  go to upper bounds only, and lower bounds come from sampling with a sample-size curve.
- One pre-registered SAT upper bound, at depth 200, both phases, two-day cap. Decision moved: R_real(200) <= 18
  refutes the counting heuristic from above; R_real(200) >= 24 refutes its falling-slope version. No other deep
  upper bounds: they cannot prove finiteness at every depth, and "bounded" cannot come back below 33.
- Pre-aging. Prepend 2J walled steps (J = 34, 44, 64) to the record instances at depths 20..200, both phases, and
  compare. Decision moved: a mean drop under one cell closes the soficity door for the prize (judge B's own check
  at depths to 35: a drop of 0.27 cell on average).
- The odd phase in CUT. The free-exterior strip of width n is NOT exact for odd-phase visible words of length n
  at n = 15 (COMPUTED, DRAT-checked, by the D4 agent and its skeptic): width n + 1, or the predecessor constraint,
  is needed there. Any odd-phase computation that set width equal to visible length was a relaxation at n = 15.

**Write up and close (two days of writing, no computation).** D7's two non-transfer sentences and the locks as the
width-2 layer; the freezing cylinder theorem; D6's diagonal-causality theorem; the exact counts |L_n| to 26 in
both phases; the death table; the trace-form census to width 18. Candidates for a record section and for the
outside-review note that both critics ask for.

**Drop.** D6 (closed by a proof); D1 as a door (its product, the data verdict and the lemma's form, is in hand);
D3's closure route (keep only the ancestry census); soficity as a goal (pre-aging only); the Rule 30-squared
route in its naive form (judge A's exhaustive check: Condrey's latch step fails for the squared rule through the
black tick, 16 of 64 windows).

**The main line's own kill criterion** (the swarm's, not mine alone): if the check-free conjecture dies at the
width-12 language, the counting route needs the checks, for which nobody has a mechanism, and the right output is
the write-up, the exact intermediate theorems and an almost-all statement for the free walk.

## 2. What the swarm settled, and what it corrected in the handover's analysis

1. **The real record grows.** The ceiling 17 was already dead; sampling now gives verified records of 26 to 33 at
   depths 280 to 766. A constant level from depth 30 on is rejected (block permutation, p between 5e-5 and 2e-3
   by block length and seed; a record-model likelihood ratio of 31 nats never reached under its null). "Bounded"
   as such cannot be killed by finite data, and no finite strip or automaton certificate can close the problem.
   A proof must work depth by depth.
2. **The counting heuristic's slope is h/(2-h), not h/(1-h).** Four agents derived it independently, as did I,
   and the record's own ladder law of 8.14 ("the record is about log2 of the number of distinct prefixes") is this
   form. The handover's h/(1-h) gives an infinite slope at h = 1 and is refuted by the free calibration. With the
   asymptotic rates the slope is 0.042 (h = 0.080) or at most 0.066 (h = 0.1236); the measured 0.080 on depths
   30..120 is matched only with the finite-length growth of |L_n| (about 0.2 bits per visible bit at lengths
   20..48) and a merging factor fitted at 0.72 (0.82 in the free case). The D8b skeptic tested the form on eight
   toy languages of known entropy: record slopes 0.66..0.99 of h/(2-h) and 0.27..0.42 of h/(1-h).
3. **The typicality lemma, stated so that it gives finiteness, is the target restated** (PROVED by the D2 agent,
   read by its skeptic and me): the survival fraction decays at rate h/2 for free because survivor counts never
   increase, and for each depth "a constant exists" is equivalent to "the record is finite". Relaxing the real
   language to a regular layer language cannot make it easier, because the real language lies inside every layer
   language, so a relaxed proof is a full proof. The content lies only in a uniform rate c > h/2 with a constant
   independent of the depth (a linear bound), and the finite-state step that a regular-language proof would use
   fails for every language, because the check at depth j depends on about 7j/16 earlier bits. Nobody is working
   on that lemma, as the handover said, and the swarm says why: there is nothing to work on until a mechanism is
   named. The check-free conjecture of section 1 is the mechanism-shaped form the swarm converged on.
4. **The single cell's regular half cannot help** (PROVED in substance): the left band is a function of the centre
   column itself (for t >= e, diagonal e at time t depends only on c_0..c_e; the whole left half is the empty
   half-line evolved with the centre column as its boundary, 0 mismatches in my own check to 3,000 rows), and its
   qualitative laws hold for every driving column. A periodic centre would leave the band as observed.
5. **The two phases are one system, but the coupling does not close:** zero records are black-run births decayed
   by 3 per depth (PROVED algebra), the recursion needs a new object at every level, and the record peaks of the
   free problem (R°(12) = 19, R(13) = 17) sit on a visible word containing 11, so they are not real.
6. **Deaths do not stop at 16** (corrects 8.86's summary): 0010001 dies at visible time 32, 1000101 at 34 (I
   verified 34 with my own SAT encoding: alive at 33, dead at 34 and 40), and a length-20 word dies at 43 (also
   verified by me: alive at 42, dead at 43). Lengths 7 to 19 all have their latest death at 34; nothing of length
   at most 8 dies between 35 and 100 (the D5 skeptic, direct SAT). Whether the deaths ever stop is open.
7. **Problems 2 and 3 were not touched** by any door; no agent used a property the single cell has and a general
   finite configuration lacks, and D6 closed the one candidate.

## 3. How the swarm ran

Nine door agents (D1 to D7, two D8 critics), one skeptic per door, two judges with different lenses: 20 agents,
none failed, about three hours of wall clock, every agent at two threads per process. Each door was briefed only
with a common definitions-and-data file (the records, the channel bound, my own counts of the visible language to
length 13) and its door file; agents could not read the record or the web, and a scan of every tool call in every
transcript found no access to either. Six door reports and both judges' files were written by the agents; three
reports (D5, D6, D7) came back only as structured returns because the harness refused their file writes, and I
transcribed those verbatim into their folders. Grading: I read every report and every skeptic, and reran with my
own code what section 4 names.

Pre-registered before launch (CLOUD-LOCAL.md row of 22:52 BST on 2026-10-10):

| prediction | outcome |
|---|---|
| SW-P1 (control): D1's slope fit lies in 0.065..0.095 | HELD: 0.0802 (D1, me and the record's TR agree) |
| SW-P2: a critic ranks D2 first or second | HELD: D8b second; D8a third |
| SW-P3: D5 finds a death past time 16 at lengths 13..16 | HELD: deaths after 16 at those lengths: 31, 38, 48, 59 |
| SW-P4: D3 proves a birth bound for a nonempty class | HELD in letter; the class is bounded better by Theorem B |
| SW-P5: D4 confirms exactness to width 10, settles nothing in general | HELD, and to width 18 in both phases |
| SW-P6: the two judges' top doors differ | HELD: ancestry census (A) against the check-free conjecture (B) |
| SW-P7: D1 concludes the form is not h/(1-h) | HELD |
| counterfactual: D1's shuffle slope below 0.04 | as required (sd 0.0099; my own maximum 0.034) |

Two errors in my briefs, found by the agents: I defined the 1100 wall's record R'(d) as the free record over every
column 1, where KIMI-QUESTIONS-2 and 8.85 define it as the real record over all configurations, maximised over
rotations (section 4, D7); and I copied GC479's "agree on 10 of 16 patches" as a statement about the pair update,
where it is true of the marker update (the pair updates agree on 4 of 16; COMPUTED by D7, its skeptic and me).

## 4. The doors: what survived, and what I verified

### D1, the slope

- MEASURED (agent and me): OLS slope of R_real on depths 30..120 is 0.0802, intercept 5.69; shuffled values give
  slopes with sd 0.0099 and maximum 0.034 over 2,000 shuffles; a constant level from depth 30 is rejected as in
  section 2. Under least squares every ceiling 16..30 fits better than the line, so the ceiling tests are
  model-dependent (skeptic).
- PROVED (agent, skeptic, me): the forced-row structure (standard phase: odd depths are affine in the newest
  visible bit, even depths are checks on the earlier bits; a word of length n decides depths 1..2n; the other
  phase swaps the parities and has depth 1 black), and the h/(2-h) derivation under the typicality assumption.
- COMPUTED (agent; word sets reproduced by the skeptic with a different algorithm to length 18): |L_n| for
  n = 14..19 in the standard phase 199, 251, 316, 393, 487, 596; the other phase's language is a subset of the
  standard one (PROVED by the skeptic: run the system from time 1), with n = 13..17 counts 148, 188, 237, 296, 365.
- CONJECTURED: Lemma A, the cost lemma, in the form its skeptic corrected: at the least length n deciding depths
  d..d+r-1, the number of real words of length n whose row 0 is white there is at most 2^(C - theta r) |L_n| with
  theta > h_top/2 (0.0618 suffices); it implies R_real(d) <= A d + B (PROVED, two lines). It holds on the finite
  languages with theta = 0.47, C = 0.3 at the minimal length only; as worded "for every n" it fails (skeptic's
  counterexample at n = 12, d = 10, r = 5).
- Trimmed by the skeptic: the p-value's stability, the ceiling test, the forecast intervals at 200 and 300
  (conditional on independent jumps, which the cluster of 18s at 125..136 contradicts; D8b's witnesses of 21 and
  23 there say the cluster is a few long runs), and the forecast's falling slope (the two fitting methods
  disagree on the sign of the curvature). The asymptotic growth rate of L is not identified by the counts to 26
  plus the one count at 48; three functional forms fit equally and give rates from -0.10 to 0.16.

### D2, the typicality lemma

- PROVED (agent; every step read by the skeptic and by me): the parity structure; survivor counts never increase
  with the run length (so the survival fraction decays at rate h/2 for free); for each depth the lemma with a
  depth-dependent constant is equivalent to finiteness of the record (a restatement); with a uniform rate c > h/2
  and a constant independent of depth it gives R_real(d) <= h d/(2c - h) + B; the real language lies inside every
  layer language, so a relaxed proof is a full proof; no eventually periodic visible sequence has row 0 white from
  some depth on, so a finite walk state is impossible (the exact state is two anti-diagonals, 2n bits at depth n).
- COMPUTED (agent; the skeptic rebuilt every set with its own SAT encoding and a different solver): the exact
  real language to length 26 in both phases; standard phase n = 19..26: 596, 721, 875, 1054, 1255, 1493, 1780,
  2111; other phase n = 18..26: 452, 549, 668, 807, 976, 1162, 1382, 1646, 1947; the layer languages of widths 1
  to 3 are the golden-mean shift, width 4 is exactly {no 11, no 00000}, with growth 0.694, 0.617, 0.509, 0.441,
  0.356, 0.258 at widths 1, 4, 5, 6, 8, 12. (The record's certified rates 0.3577 and 0.2593 sit 0.0015 above
  these radii: they are safe upper bounds from the integer certificate, as 8.33's counterfactual implies.)
- MEASURED (agent, skeptic): past depth 36 the real survivors pass checks at 0.49 and their forced bits are allowed
  exactly as often as a random bit; at depths 10..36 the checks pass at 0.53..0.55. The skeptic's stratification:
  these are bulk averages dominated by runs of length 0..2; along the record walks the survivor count is flat for
  nine or ten steps (an effective rate of 0.47), so the in-range data do not measure the exponent that matters.
  The agent's bracket "P = 1 is consistent up to c = 0.53" is REFUTED by the skeptic with the exact counts.
- The door's product: the property FD (forced-bit decorrelation: the forced-only survivor count decays
  exponentially), which avoids the checks entirely, and its check-free, finite-type form in section 1. The door's
  own verdict on a week for the lemma as stated is "no", and the skeptic agrees for the right reason.

### D3, the coupled system

- COMPUTED (agent to depth 60; its skeptic identically; mine to 13 entry for entry): the black-run end records
  Q and P in both phases and the coupling identity of 8.82 at every depth 2..60.
- PROVED (read): record ends are forced depths, so the two phases' constants differ by an odd amount; the ones-run
  lemma (a run of ones sits under a period-3 pattern one step earlier); the leaky-max form
  Psi(d) = max(-d, Psi(d-1) - 3, b(d)) with Psi = max(E, E°) - 2d, so the coupled system is bounded iff the birth
  sequence b is.
- REFUTED (COMPUTED): closure of the recursion in one inequality form with any constant c <= 12 on depths <= 60
  (births jump 9 to 14 cells above every earlier zero-run end at 12, 32, 58). "Does not close, for a proved
  reason" is an overclaim (skeptic): the predecessor structure (period-3 runs, then the nilpotent tower, computed
  complete to depth 40,141 on a ring of 48 by the skeptic) does not by itself prevent a closing inequality, and
  the records to 60 use only levels up to 17.
- PROVED but known better: for eventually periodic visible sequences no row has an infinite run, with a bound
  16^q + 1 for pure period q; the record's Theorem B gives 2P - 2.
- COMPUTED and confirmed blind by me: the class avoiding the twelve minimal absent words of lengths 2..12 has
  zero records equal to R_real at every known depth from 1 to 31 (maximum over phases) and first exceeds it at
  depth 32 (9 against 8). Record searched: "absent-word class" -> no hit; Local's relaxed records with forbidden
  words to length 16 and 18 (RLK) are the deeper form of the same fact.
- The skeptic's unexpected check is the ancestry structure of section 1's second item.

### D4, the trace form

- COMPUTED (agent by SAT with DRAT-checked UNSATs and re-simulated witnesses; the skeptic by its own census to
  length 31 and its own SAT to width 18; mine to width 8): the trace form T^W(2W-1) = T(2W-1) holds for
  W = 1..18 in both phases; in the standard phase the 2W form holds to 18 and the 2W+1 form fails exactly at
  W = 3, 5, 17 (the tight lengths 7, 11, 35 of 8.83); in the other phase the 2W+1 form fails at W = 1, 7, 12 and
  the 2W form at W = 12 and 15.
- REFUTED (COMPUTED, DRAT-verified; the skeptic's own exhaustive bitmap over 2^30 rows and 2^30 strip histories):
  the inequality w_min(f) <= ceil(|f|/2) in the other phase, and the exactness of the width-n strip for odd-phase
  visible words at n = 15: the word 101000101010100 is produced by the width-15 strip and by no odd-phase real
  right half (visible w_min = 16), while it is a standard-phase real word. Mechanism: the odd-phase language is
  the standard one restricted to rows with a predecessor, which the strip does not see. Exact again at n = 16.
- PROVED (read): the all-W trace form is equivalent to T^V(2V-1) = T^(V+1)(2V-1) for all V; w_min(f) <= |f| - 2
  for traces by a merger lift of the first exterior constraint.
- REFUTED (COMPUTED): the local proof route. The skeptic corrected the step: one-step repairs work at times 0 and
  1 and first fail at time 2 for widths >= 5; the real lifts of strip histories rewrite up to 11 of 15 initial
  cells at width 15 on the period-3 background (100)^m, which opens a white region through which exterior
  information runs at speed 1. A proof must be multi-step or global. "No bounded radius exists" is CONJECTURED.

### D5, the death criterion

- COMPUTED (agent; the skeptic re-solved all 316 length-16 values and the late deaths with its own encoder and
  DRAT; two of the deaths verified by me): the death table for lengths 13..16 to visible time 56; deaths after
  16 at those lengths 31, 38, 48, 59; for every length 7..19 the latest death is at 34 (carried by 1000101);
  at length 20 the word 00101010001000010101 dies at 43 and is primitive; at length 21 three die (37, 42, 43);
  no word of length 7 or 8 dies between 35 and 100 (skeptic, direct SAT); the other phase's short words stop
  dying at 16.
- PROVED (read): the identity last(w) = 1 + max over a of last(aw) (so the death times of shorter words follow from
  a length-16 table); a death at time d forces at least d + 1 vertices on any labelled graph presenting L with all
  vertices initial and accepting (weaker than 8.86's fooling set of 51).
- REFUTED by the skeptic: the agent's claim that a counterexample's visible sequence lies in the stable language
  (the intersection of all L^(j)); only the shift by 2J into L^(J) holds, with the white run 2J deeper. That is
  enough for pre-aging as an exact tightening of the instrument, and nothing more.
- Corrections to the record and to my brief: 8.86's "none of length at most 12 after 16" was a horizon effect;
  L stops being left-extendable at length 6 (100101), not 7.

### D6, the single cell's regular half

- PROVED (agent; the induction read by the skeptic and me; the fact checked numerically by me): diagonal
  causality, as in section 2 item 4; left self-consistency; B1 to B3 and the power-of-two periods hold for every
  driving column with c_0 = 1; the eternal band is fixed by one bit per eventually white diagonal.
- MEASURED (agent) and corrected by the skeptic: driving the left half with a clock from 20,000 or 60,000 leaves
  every settle time below diagonal 98,113 bit-identical to 2^17 rows; but clocks substituted at times 500..800 do
  enter the settled band by 2^19 rows, and clocks from 230..380 flip the integration bit at diagonal 87,866. So
  "decided by the first 300 centre values" is false, and the screening lemma is probably false as stated. The
  verdict is unchanged: a band that reacts to late centre values is still a function of the centre.
- PROVED (agent): the single cell's visible bits are not eventually periodic for any period; Theorem A''' with the
  band gives only constants; the only regions both diagonal-periodic and column-2-periodic are Rule 30 rings with
  F^2 = id (three of them to size 64).
- Door closed. Small corrections to my brief: diagonal 17 is periodic from row 15, and the single cell's
  diagonals 4 and 9 are black from times 2 and 5 (4 and 11 are the universal bounds).

### D7, Condrey and Rule 210

- PROVED (agent, skeptic's wording): period 1 works through the OR latch (column 1 eventually constant beside a
  white wall) and then the two-column theorem; beside 0101 every black tick undoes the latch (lock L2: a 1 at a
  black tick is followed by 0), and nothing local derives "column 1 eventually periodic". Rule 210's clearing
  front rests on the marker identity M' = (1-U)(B XOR M); the Rule 30 pair update creates a marker under a black
  U on three of the eight (B, P, Q) patches, and the patch (U, B, P, Q) = (1, 1, 0, 0) occurs at time 1 above a
  single black cell beside the clock.
- COMPUTED (agent, skeptic, me): the two rules' pair updates agree on 4 of 16 patches, the marker updates on 10 of
  16 (GC479's number).
- PROVED (agent, skeptic): the locks L1 to L5 for every periodic wall; they are the width-2 layer's forbidden
  words, so they add nothing beyond that layer (growth log2 of the golden ratio); the 1100 lock of 8.85 reproved.
- The 1100 record conflict is resolved by my own instrument: the agent computed the FREE record of the 1100 wall
  over every column 1 (my engine gives its values 4 3 2 2 5 4 6 5 4 3 7 10 9 11 10 at depths 1..15), while the
  record's R'(d) is the REAL record over all configurations, maximised over rotations; my free values bound it
  from above at every depth and equal it at depths 1 and 2. 8.85 stands.
- Freezing: about 4% of random right halves lock column 1 into period 4 or 14 within 79 steps and stay locked
  to 8,000 (MEASURED by the agent); the skeptic proved it on a cylinder, and so did I by exact closure: every
  right half beginning 10011001010110011000 beside the standard clock has column 1 = 1100 repeated for ever
  (188 reachable states, none violating; a one-cell change violates). Frozen halves are never counterexamples (a
  periodic visible tail forces an infinite left half, PROVED by three agents), but any uniform lower bound on the
  kick rate is false. Record searched: the record's GC1020 (the finite right half 1001 keeps the two-gap train for
  ever) is the same kind of object.

### D8a, the critic (mathematician's lens)

- Survived: the diagnosis that no step in the plan crosses from finitely many depths or typical statistics to
  every depth, and that "entropy against demand for one orbit" has no method anywhere; the unit error; the Rule
  30-squared reduction (period 2 at column 0 is an eventually constant column of the radius-2 left-permutive
  composite rule: PROVED, one line; record searched: no hit); the line cascade (every diagonal of every finite
  seed eventually periodic with period dividing 2^(c-a), the scope of the record's B2); the ANF facts (check cells
  of row 0 have full degree and density about 1/2 in both coordinate systems; no linear or sparse structure to
  depth 40).
- REFUTED by its skeptic: the headline that 4 to 21 times more prefixes survive at the tail than coins predict (the
  tail clusters are one or two merged walks; counted by distinct walks, 2^(0.40 d), the records sit inside the
  coin model's extreme-value scatter), "late real sequences use only the blocks 10000 and 100" (7% of random
  halves use 10 as well), and the inference that finite rows are atypical.
- Its ranking (D7 > D6 > D2 > D5 > D4 > D3 > D1, drop D1) rests on the Rule 30-squared route, which judge A's check
  closes in its naive form, and on the band, which D6 closed. Its "LR first" proposal (the free problem, with an
  almost-all theorem as the realistic output) is the fallback of section 1.

### D8b, the critic (experimentalist's lens)

- COMPUTED (agent; its skeptic reproduced the sampling match with fresh seeds and all 18 witnesses with a
  forward-only verifier; five witnesses verified by me): the sampling result of section 1. The skeptic's caveats:
  about 50 of the 101 matched depths are inherited from a parent record; depth 105 is never hit in 3.8 x 10^8
  samples; deep bounds lag by 2 to 3 cells per tenfold increase in samples at depths 600..800; sampling could be
  known to reach the records only because SAT supplied the upper bounds.
- MEASURED (agent, skeptic): the offset c(d) = log2(2|L_n|) - R_real(d) has mean 3.0 and sd 1.3 on depths 30..120
  (the record's 8.14 law seen on the real record); its drift's sign is not determined; in measure the real column
  passes the forced-walk checks at chance for four or five cells and worse than chance after; white-clamped
  strips of width n + 2 reproduce L_n exactly to length 17 (and judge A found them equal to the exact SAT counts
  to 25).
- Its ranking (counting-and-sampling first, then D2, D5, D1, D4, D7, D6; drop D3) and its five experiments are
  largely adopted in section 1, with the skeptic's corrections (the measure-level pass rates cannot falsify the
  counting picture; the stall criterion for sampling is confounded by sample size).

## 5. Where the judges disagreed, and what I decided

Both judges agree that growth is real, that the counting routes all end at the same unproved cost statement, that
D6 is closed, D7 is a write-up, D5 is pre-aging only, D4 is a tool with a cheap counterexample hunt, and that no
SAT time should go to deep upper bounds except as a pre-registered test. They disagree on the first step. Judge A
(lens: probability of a proof in a year) puts the record-ancestry census first, as the only exact structure seen at
the tail, with the check-free conjecture second. Judge B (lens: information per week) puts the check-free
conjecture first and gives the census no week.

I put the check-free conjecture first and the census second, for three reasons. The conjecture is a sufficient
condition for period 2 with a kill that can fire within the week; the census is structure-finding whose kill is
softer and whose own discoverer found the structure dissolving at level 17 for the depths computed. The conjecture
is new to the record (record searched: forced-only, "no 11, no 00000", "demanded bit" -> only 8.14's reading of the
layer ladder, which is its measured shadow). And if the conjecture dies, the census is exactly what is left, so the
order costs nothing. Where the judges agree with each other and with the skeptics against a door, I have followed
them throughout section 4.

## 6. What the swarm could not settle

- The mechanism. No door found a reason why holding the clock costs information at the tail. The channel bound
  gives the supply side; the demand side, a uniform decay above h_top/2 per cell, is measured at 0.47 to 1 on words
  to length 26 and proved nowhere. The check-free conjecture moves the open part off the checks and onto the forced
  orbit of one prefix inside a finite-type shift; it is still a single-orbit statement.
- The asymptotic growth rate of the real language, hence the slope of the real record beyond depth 150, and
  whether the merging factor can be derived rather than fitted.
- Whether the deaths ever stop; whether the trace form holds for all widths (no local proof route is left);
  whether the record ancestry keeps climbing the tower with depth.
- Whether the 18s at depths 125..136 are one run or several: cheap, and left unanswered by two doors.
- Anything about Problems 2 and 3, and anything that uses the single cell's specialness.

## 7. New to the record (all third-party unless marked, with their status), and corrections

New facts: the sampled lower bounds of section 1 (COMPUTED, five Intel-verified); |L_n| to length 26 in both
phases and the layer-language identities of section 4 (COMPUTED, two independent rebuilds); the trace form to
width 18 in both phases and the odd-phase visible failure at n = 15 (COMPUTED, DRAT); the death table and the
deaths at 32, 34, 37, 42, 43 (COMPUTED, DRAT; 34 and 43 Intel-verified); diagonal causality (PROVED); the
leaky-max form of the coupling and the ones-run lemma (PROVED); the twelve-word class equal to R_real to depth 31
(COMPUTED, Intel-verified); the freezing cylinder (PROVED, Intel-verified); the free record of the 1100 wall
(COMPUTED, Intel-verified to 15); the Rule 30-squared reduction (PROVED); the h/(2-h) form and its toy-language
test (PROVED as algebra, COMPUTED); the record-ancestry levels 2..17 (COMPUTED, agent only).

Corrections: 8.86's "none of length at most 12 dies after 16" (deaths at 17, 32, 34); the handover's h/(1-h);
GC479's "10 of 16" is the marker count; 8.74's "diagonal 17 from row 16" reads 15 in the agent's and its skeptic's
site-frame code (unverified by me); the certified layer rates are upper bounds 0.0015 above the radii (expected).

## 8. Proposals to the workers (not orders)

- **Local:** adopt sampling for lower bounds, with a sample-size curve, and spend SAT on upper bounds only; the one
  pre-registered test at depth 200; the odd-phase width n + 1 in CUT; the pre-aging test; the exact counts |L_n|
  to 26 are a cheap replay if the record wants its own (the method: extend L_(n-1) by one bit, filter by the
  width-12 layer automaton, decide by SAT, re-simulate every witness).
- **GPT:** the check-free conjecture as a hand target, starting from what is proved (no eventually periodic
  sequence) toward orbits with long periodic stretches; the two non-transfer sentences for the record; the freezing
  cylinder beside GC1020.
- **Cloud:** the assessment the owner asked for; the corrections of section 7 propagated where the record states
  the old forms; the record map's compression, which this plan's line pushes further past 40 KB.

## 9. Provenance

My own instruments, all outside git: a visible-language census that reproduced the record's seven minimal absent
words to length 10 blind and gave the counts to 13 used in the briefs; a forced-left-half engine for both phases
(R and R° to 13, the black-run tables, the coupling to 13); a general-wall free-record engine (the 1100 question);
a strip-trace census (both phases, three lengths, to width 8); a SAT membership encoder for the deaths; a forward
simulator for the sampled witnesses; an exact closure for the freezing cylinder; the twelve-word and forced-only
class records; and a transcript scan for independence. Nothing in this file is a prize claim. The owner decides
whether the main line moves.

*Since then (Cloud, 2026-10-22, spring clean; added at the end so that the line numbers SW01-OBJECTS.md quotes stay
put):* the plan's first target, the check-free conjecture of §1, was replicated in RULE30-PRIZE.md 8.88 and closed as
a main line in 8.89; §6's question about the 18s at depths 125 to 138 is answered in 8.96. "The handover" in §2 and
elsewhere means archive/CLAUDE-INTEL-HANDOVER.md §3.
