# Night tasks, 3 November 2026: a suggested list for GPT and Local (Cloud, at the owner's word)

*The owner, 2026-11-03, shortly after 00:04 GMT: "As we head into the long night GPT and Local have heartbeats and will continue
to work ... I really want to wake up to some movement on the unifying theories or missing structures, some sort of
pathway towards the difficult prize problems, some useful proofs ready for submission. Without overly disrupting their
autonomy, please can you produce a suggested task list the workers can refer to."*

**How to use this page.** It is a menu, not a queue. Your own pulls stay yours (AGENTS §1, §3): take what fits, say in
the ledger what you take, and give the task a board row (PERIOD-TWO §6.5) before its first run. Every task below names
its object, the step, a prediction or kill test, the status it can reach tonight, and who is best placed by tool
(TOOLS §10: Lean builds and Wolfram on Local; SAT, LRAT and long Intel runs on GPT). "One block" means thirty to sixty
minutes. Prize-level or carrying steps need the other worker's read before any status rises (AGENTS §4). Portal
submissions go on the standing permission only after that read and a prior-art read of the matching kit and portal
statements (G24, G29); kit pull requests only on the owner's word.

**If you take only one each.** Local: A1 (the classic ether's exact zero, packaged for the portal). GPT: C2 (do our
theorems discharge a hypothesis of the kit's new conditional reductions?). Shared, if there is a spare block: C4 (the
balanced-letter census, the one place the algebra can produce a measure and be checked tonight).

## A. Proofs ready, or nearly ready, for submission

Ranked by distance from the portal. Each has a two-party read already; what is missing is the package.

**A1. The classic ether absorbs a black edge: front speed exactly zero** (nearest). Statement: a black edge inserted
into the kit's `Rule30Ether` has its leftmost mismatch F(t) pinned, x_B + 1 ≤ F(t) ≤ x_B + 13 for every t ≥ 222, at every
one of the 196 alignments, so F(t)/t → 0. Pieces, all in hand: the kit's own trap (Lowry's 109 wall states, `wallOK_true`,
`trap_invariant`); Local's `trap_two_sided` and `news_bounded` (`tests/probes/lean/EtherTwoSided.lean`, standard axioms,
built against kit main c42f6e5, L1320); the entry at all 196 alignments by t = 222 (`ether_trap_check.py`, COMPUTED) and
the upper bound (none of the 109 states equals its 13-cell reference strip, a finite table), both read by GPT (GC2404).
Step: Local turns the two finite checks into kernel-checked lemmas in the kit's style (as the closed sets were), adds the
three headlines and the essay; GPT gives the final source read and the prior-art line (Lowry's PR65 proves the trap, not the
inserted edge's speed; say exactly that). Reach tonight: submission package built and checked on the M5. One Local block
plus one GPT read.

**A2. The universal healing bound** (smallest). Statement: for any spatially and temporally periodic background E and any
perturbation confined to x ≥ 0 at t = 0, the leftmost damaged cell never lies below the recruitment frontier
K(t+1) = K(t) + 1 iff E(K − t, t) is black, initialised at the last known diagonal x = −1, so the leftward damage speed is at
most 1 minus the frontier's climb rate: 1/2 (G8), 7/12 (classic), 2/9 ((7, 63)), 1/2 ((9, 57)), 7/17 ((12, 68)), exact per
background (`healing_bound.py`, corrected in CL687). GPT accepted the proof with the initialisation (GC2404). Step: Local
writes the induction in Lean on the matching half-line (the shape of `trap_two_sided`), GPT reads; the rates are a replay
of a finite walk. It is a statement about an infinite family of backgrounds, which is the kit's criterion for a contribution.
One Local block.

**A3. The alternating-closing law** (short if submission 32's lemmas carry). Statement (CL645, GC2201, GC2205; two-party
hand): after a double doubling 11 with prefix period 4q0, an alternating run (10)^m 1 has m ≤ q0 − 1 and closes with 1 iff
m = q0 − 1; so 1(10)^m 11 occurs only when m + 1 is a power of two, 1101011 is forbidden, 11011 closes with 1 only at the
universal start, and every five consecutive prefix-growth letters hold at most three doublings. Step: check first whether
the portal's gate-clocks-nested module (R30-20261031-9861e5: `no_three`, `after01_double_iff`, `after11_order`) and our
PR51 shift law (`E_mod4`, `eta_*`) already give the closing step as a short corollary; if so, Local adds the corollary
and the forbidden word as headlines in that language. Prior art to name: GC2007's five-step bound (ours, unsubmitted),
Rowland 2006 §5. One Local block for the check, one more for the module if it carries.

**A4. The moving-wall theorem for the ring backgrounds** (most novel). Statement: on the background (9, 57), at every one
of its 513 alignments, the inserted edge's front satisfies the bounded-error law |F(t + 19m) − F(t) + 5m| ≤ 23 for t ≥ 4733
(GPT's conditional form, GC2402), hence limiting speed 5/19; on (7, 63), 28 alignments with the (9, 7) law and bound 15.
Soundness of the moving-anchor closed set is PROVED two-party (CL682 with GC2394's amendment, GC2404); the closures are
COMPUTED (`closed_set.py`, 498 to 4,433 states per alignment). Step: Local ports the closed-set check to a kernel-checked
Lean certificate for one alignment per background at W = 24 (the 109-state ether trap is the template; 498 states is the
smallest (9, 57) closure), the essay carries the full census as the computed complement and the velocity spectrum as the
object (0, 1/2, 2/9, 5/19 exact; 0.224 and 0.17 to 0.24 measured). Two Local blocks; GPT reads the start witnesses
(now asserted in the script) and the soundness statement in the essay.

**A5. The episode bridge as a theorem in the kit's vocabulary** (most valuable, longest). Statement: no eternal point of
any period ends in the phase E iff M_E(k) < ∞ for every k (PROVED two-party, L1310); with the exact tables M_G16(1..14),
M_P1024(1..8), M_480(1..10) it gives wall exclusions uniform in the period at bounded depth, and for G8 it is the kit's own
`episode_bound`. Step tonight: write the statement and the two directions in the kit's objects (black-edge codes, the
one-sided update, the autonomous prefix), decide what is a `decide`-free finite check and what is a hand induction; the
Lean build is a day, not a night. Local, with GPT's read of the statement.

## B. The unifying theories and the missing structures (the atlas)

The atlas's reading after GPT's reviews: T1's mask half is PROVED and its core is *conditioned*, T2's algebra is at both
ends with the asymmetry named, T3 holds as "a parity is fair unless the algebra forces it", with the forced part two-party
and the free part only measured. Each task below moves one cell with a kill test.

**B1. Two deterministic jump facts of the fair-row front.** CL687 found, exact in 45,005 steps: after a heal of 2 the cell
ahead of the front is white (9,867 of 9,867), after a heal of 3 it is black (1,021 of 1,021); the pattern table in
`front_markov.out` says which damaged pairs give which jump. Step: derive both from the mask lemma by hand (one or two
lines each, I expect), then test them on the ring backgrounds' fronts ((7, 63), (9, 57), G16) with predictions first.
Prediction: they hold on every background (lean 60%); counterfactual: a background where a heal of 2 is followed by a
black cell, which would make them a fair-row artefact. What it teaches: part of T1's "conditioned core" is algebra, and
the measured residue shrinks to the jumps of 1 and 4. One block, anyone; a hand step for GPT or Local, the test for Local.

**B2. The 00-led functional with its actual prefix history** (GPT's own pull, GC2405). The one free leaf of the
doubling-letter calculus is F_c(R_(j−5) OR R_(j−6); q) after the letters 00, where both diagonals have the same period and the
pairing moves stop. Step: write its value through the kit's `R_step` for the actual seed's history (the two diagonals share
their ancestry through g), name the constraint CL645 called "the 00 transition", and test any candidate law against the
retained data, where it must reproduce the individual values, not the frequencies: `edge_shift_tree64.out` holds every
free leaf with its full context (1,655 after 0; 440 after 001; 88 after 00101; 15 after 0010101). Kill: a candidate that
fits the pooled frequencies and misses one leaf is dead. No new seed census (GC2164, GC2405). GPT, hand first.

**B3. M4, the front's state: what selects the incoming bit?** GPT's corrected question (GC2404). Step: with
`front_markov.py`'s contemporaneous fields and trial ids, report the complete conditional distribution of the next jump
given the proposed state (jump just made, a[x..x+2], b[x..x+2]) and test whether adding the previous jump changes it
(a conditional-independence test on counts, not on means). Prediction: the previous jump still matters at the 1 and 4
jumps (lean 55%); if it does not, the state is closed and the 0.246 has a finite-chain closed form; if it does, the memory
is deeper and B1's facts say which part is algebra. Local or Cloud, one block; pairs with B1.

**B4. M6, the classification's two missing clauses, stated exactly.** GPT (GC2405): a finite pair graph does not by itself
make every bi-infinite path a wall between simple cycles (a branching strongly connected component can carry a nonperiodic
itinerary), and "no wall leaves the rain" is weaker than "every wall ends in the rain". Step: write both clauses as theorems
to prove: (i) in H_p every bi-infinite path is eventually inside one strongly connected component at each end, and that
component is a simple cycle (does §35.1's rotator proof extend from cyclic phases to every SCC? that is the hand question);
(ii) the Sink clause for one phase, P1024, as M_P1024(k) < ∞ for all k. No run; a page in the genealogy with the exact
statements and what is proved of each (p | 16 cores exact). Local, one block; GPT's read of (i).

**B5. Are the phases sporadic?** (§38.5 item 2(b), my question Q4.) A phase is a ring y with c^g(y) = ρ^r(y); the known ones
are the rain, G8, G16, the 480 phase and P1024, all rotators of c or c². Step: a complete enumeration, not one model per
lag: for N ≤ 4,096 and g ≤ 2, every lag r, all models up to rotation by blocking clauses, with undecided lags reported as
UNKNOWN (GC2404's rule). Prediction: nothing new below 4,096 beyond the known phases and their rotations (lean 50%).
Either answer is usable: a new phase is a new target with the cheap episode test; scarcity to a bound is half of the
classification. GPT's Intel SAT, one or two blocks under caps; Local's census as the control for small N.

## C. Pathways toward the prize problems

Nothing here claims progress on a prize problem. Each is a statement whose truth or falsity, decided tonight, would say
where the difficulty lives or discharge a hypothesis someone else has already made rigorous.

**C1. The centre column as two parities.** CL677 (two-party): c(t) is the parity of the OR-events along its past diagonal,
and the samples at e ≤ t/3 (the settled crystal) are an exact function of (e, s mod 32) (P-G1, 8,129 of 8,129 rows). So
c(t) = P_c(t) ⊕ P_rest(t) exactly, with P_c a line-sum through a known table and P_rest the samples in the settling zone
and the core (the last fifth of the diagonal). Step: compute P_c(t) to t = 2^16 from the table and test it for eventual
periodicity (exact period search and autocorrelation to lag 2^14). Prediction: not eventually periodic (lean 70%).
Counterfactual: a period Q found; then Problem 1 reduces exactly to "P_rest is not eventually periodic", a theorem-shaped
reduction with a finite object (the crystal table) that Lean can hold. Either way it names the samples Problem 1 is about.
Local (the table is in `diagonal_segments.py`), one block; GPT reads the reduction if it appears.

**C2. The kit's new conditional reductions against our theorems** (the most direct prize pathway in the record). The board
(PERIOD-TWO §6.5) has PR75/76 as "open hypotheses; comparison pending": mortality implies period-two exclusion; BWH plus
SmallRW implies RW, which gives constant-tail separators, which exclude period two. Step: read their exact hypotheses at
the current heads and ask of each whether one of ours discharges it: `no_finite_clock` (PROOFS 32, Lean), the rule 210
two-sided theorem, Theorem E for every intercept, the channel bound at width 14, the uniform recoding horizon (dc3d17), the
finite past (803bc4). Prediction: no hypothesis is discharged outright but one is reduced to a finite census we can run
(lean 50%). Kill: every hypothesis is about an object none of our theorems touches. A discharged hypothesis is a joint
statement and a submission. GPT, one read block; Local runs any finite census it names.

**C3. The balanced-letter census: the algebra producing a measure, in the one place it can be checked.** T1 says the
constants are functionals of the uniform measure; T2 gives the odometer's algebra; the bridge between them has never been
tested where both are computable. Statement to test: over *all* odd seeds below 2^20, at each depth n = 5..22, the doubling
letter d_n is exactly balanced in every free context (the forced contexts give 0 by the algebra), i.e. the kit-style
uniform-seed count (the shape of its `measure_diag_eq`) is 1/2 exactly, not approximately. Prediction: exact balance in
the unconditional count at every depth (lean 55%); conditional on the free contexts, balance to within 2^(−n/2) (lean 45%).
Kill: one depth where the unconditional count is off by more than its own granularity. If it holds, it is a theorem about
an infinite family (every depth) to prove by counting, which is T1's measure produced by T2's algebra and a submission; if
it fails, the deviation is the first exact unfair parity in the record and the next object. Local in C (`edge_lift.c` over
2^19 seeds to depth 22 is minutes), GPT the counting proof if it holds.

**C4. Problem 2 as T3 reads it, stated honestly.** The free parities of the right edge measure fair; GPT is right that this
is not proved equivalent to centre-column fairness. Step: write the one-page statement of what *would* make it equivalent
(a mixing or independence statement for the core samples of C1), and the weakest form that is still a theorem about the
single seed. No run. GPT, half a block; it is the frame for B2 and C3.

## D. The capture line (Local's) and the guarded walls (GPT's): the inference that is missing

Both workers have said it in their own words (L1339, GC2406); I put it here so the night does not spend itself on a fourth
width. The window automata at W = 8, 10, 12 prove, each, a finite statement: capture from the attractor within a bound, and
an episode bound M_P1024(k) for k up to the window. Their bad cores B_W cannot vanish at finite W (C1, §45), and a path that
stays in B_W for every W with compatible entering cells *is* an eternal configuration with a wall, so "B's share → 0" can
never close the question by itself: the all-width statement is the conjecture. The missing inference is one of two
lemmas, and both are statable now: **a state that remembers the material behind the front** (GPT's history line: the pair
resets of GC2393 and the finite contradiction horizon of L1332 are its proved pieces), or **"self-written wake is not fuel"**
(the material an advancing front writes behind it cannot feed a retreat beyond a bound; T47 measured how much history
matters after a reset). Suggested step: write the exact lemma, with the window and history lengths it needs, and its finite
verification plan, before any W = 14 run; then run the smallest instance that could refute it. Local and GPT together, in
the ledger, one block each.

## E. Do not

- No W = 14 or larger window without the projection or history argument written first (L1339, GC2406 agree).
- No larger seed census to settle a density limit (GC2164, GC2405); finite data are heuristics there.
- No kit pull request without the owner's word; portal submissions only after the two-party read and the prior-art read.
- Predictions, counterfactual and a `Record searched:` line before every run; multi-term `record_find.py` is an AND (G29).
- Caps through `run_capped.py`; the M5 is for general use, long compute goes to the Intel host (CLOUD-LOCAL, 2 November).
- Privacy (AGENTS §7) on every push; `ledger_check.py` and `doc_links.py` before it.

## F. What the owner would like to wake up to

1. One submission package built and checked (A1 or A2), with GPT's source read in the ledger.
2. One atlas cell with a two-party status change (B1 the likeliest), recorded in the atlas and the board.
3. One pathway statement written as a theorem with its kill test run (C1, C2 or C3), whichever way it came out.
4. The ledger's "My own pull" lines kept, NOW.md's state current, nothing in the record above its status.

Cloud's own queue, if kept running: B1's hand derivation, the G16 strip graph with a replay control, and reading whatever
the night produces. Otherwise every task here is open to either worker.
