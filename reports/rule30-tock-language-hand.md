# The tock language: a hand notebook

Local (Claude on the M5), 25 October 2026, from about 23:20 GMT. L954. At the owner's word: "begin transcribing ideas to math, testing
hypothesis but without relying on compute."

**Status:** hand-derived working note, single party. No simulation program, algebra program, census, GPU or Lean run. Every equation,
case split and simulation below was done by hand. Section 1 is the targeted independent read GPT requested (GC1889). Sections 2 to 5
are new hand work awaiting GPT's targeted read. Most of it restates the record's own machinery in tock coordinates: the row is
determined by the trace ("the left image determined by the trace", PERIOD-TWO.md row Q6; GC1158's depth-k image presentation). No
prize, board or PROOFS status changes. **Critical path:** none directly. This is the owner-requested transcription of the DEEP-QUESTIONS
ideas into mathematics, with small hand facts.

## Conventions

GPT's, from [the Tick Tock note](rule30-tick-tock-hand-analysis.md). Zero-wall half-line:

    x(t,0) = 0,  x(t+1,j) = x(t,j+1) XOR (x(t,j) OR x(t,j-1)),  j >= 1.

A passing history has x(2n,1) = 1. Write:
- b_n = x(2n+1,1), the nth tock;
- E_j(n) = x(2n,j) and O_j(n) = x(2n+1,j);
- u, v, w, s = b_n, b_(n+1), b_(n+2), b_(n+3).

Write F_j(b) = E_j(0), the starting row as a function of the tocks. Shift invariance gives E_j(n) = F_j(b_n, b_(n+1), ...).

## 1. Targeted read of GC1889: the six-cell table, the discrepancy and the periodic-input step carry

**Independence.** I derived columns 1 to 6 by hand before opening GPT's note, while working the owner's request. I derived them from the
outward reading of the rule:

    E_(j+1)(n) = O_j(n) XOR (E_j(n) OR E_(j-1)(n)),
    O_(j+1)(n) = E_j(n+1) XOR (O_j(n) OR O_(j-1)(n)).

My forms were written differently, for example O_5 = (NOT w) XOR ((NOT u) OR v) and O_6 = NOT (w AND (u OR v)). Each equals GPT's
entry by De Morgan's law and NOT A XOR NOT B = A XOR B. All twelve entries agree.

**Discrepancy identity.** O_3 XOR O_5 = v XOR w XOR (u AND NOT v). Since v and u AND NOT v are never both black, their XOR is their OR,
u OR v. So d_n = w XOR (u OR v), and b_(n+2) = (b_n OR b_(n+1)) XOR d_n. Carries.

**Eventual stop.** With d = 0 from some point: a white pair stays white; (1,0) goes to (0,1) and then (1,1), which is fixed; (0,1) goes
to (1,1). So the tocks become constant. Carries.

**Periodic input.** If d has period p from N, then the triple (b_n, b_(n+1), n mod p), for n >= N, evolves deterministically through at
most 4p states. So it repeats, and b is eventually periodic. With the black ticks, the watched column is then eventually periodic, which
Jen's propagation and the moving edge exclude for a finite start. Carries, with GPT's hypotheses exactly as stated: the table needs no
finite support; the exclusion does.

**GC1890's run-length addendum.** Disagreement can occur only at tocks, at odd times 2n+1. Two disagreements at 2n+1 and 2n'+1
enclose agreement at times 2n+2 to 2n', which is 2(n'-n)-1 updates, an odd number. Eventually periodic gaps rebuild an eventually
periodic d by concatenating blocks. Carries.

**Horizons.** O_6(n) uses the trace from 2n+1 to 2n+6, so passing ticks through 2n+6 suffices, as GPT says.

**Unexpected checks, by hand simulation.** I evolved two starts with pencil-and-paper arithmetic, no program, and compared every cell
that the table covers within its valid horizon.
- **Width 8, start 10111110** (wall first). It is built from tocks (1,0,1,1) through F_1 to F_8 below. The trace read back as
  1,1,1,0,1,1,1,1, which is the input. Every covered cell at times 1 to 6 matched, including O_7(0) = 1. The start dies at tick 8.
  E_7(1) does not match, as it should not: E_7(1) assumes the tick at 8 is black.
- **Width 5, start 10111.** The rows at times 1 and 2 match O_1 to O_7 and E_1 to E_6. At time 6 the edge reads 1, 1, 0 from the
  outside, as GPT's stripes a_0, a_1, a_2 require.

GPT's own control (tocks 0,1,0, giving 110000 and then 01100) also checks by one application of the rule.

**Verdict: GC1889's six-cell table, the discrepancy identity and the periodic-input implication carry.** This is a targeted read of
the carrying steps, not a novelty judgement.

## 2. Two more cells, and the owner's metronome tested

Continuing the same recursion by hand:

    E_7(n) = w OR ((NOT u) AND v)
    O_7(n) = s XOR v XOR w XOR (u AND (NOT v) AND w)
    E_8(n) = (NOT s) XOR v XOR w XOR (u AND NOT v).

*Derivations, briefly:*
- **E_7.** It equals O_6 XOR (E_6 OR E_5). If u = 1 this is (NOT w) XOR 1 = w. If u = 0 it is NOT (v AND w) XOR NOT (v XOR w),
  which is v OR w.
- **O_7.** It equals E_6(n+1) XOR (O_6 OR O_5). The OR is black unless u = 1, v = 0 and w = 1.
- **E_8.** It equals O_7 XOR (E_7 OR E_6). That OR is black unless u = 1, v = 0 and w = 0. The two AND-terms are disjoint and together
  give u AND NOT v.

Each was cross-checked by the width-8 and width-5 simulations within their horizons.

**Hypothesis H1 (the owner's metronome): "the hold keeps swinging outward: each seat holds its colour across alternate half-beats."**
*Prediction, written from L951's fourth seat:* it breaks at seat 4.

- Seat 2 holds from tick to tock: E_2 = O_2 = NOT u.
- Seat 3 holds from tock to tick: O_3(n) = v = E_3(n+1).
- Seat 4, from tick to tock, compares NOT v with (NOT u) AND (NOT v). These are equal unless u = 1 and v = 0. **So seat 4 misses its
  beat exactly when the tock falls from black to white.**
- Seat 5, from tock to tick, compares O_5(n) = w XOR (u AND NOT v) with E_5(n+1) = v. These are equal exactly when w = u OR v, that
  is, when d_n = 0. **GPT's discrepancy is seat 5's missed beat.** (Equivalently, because E_5 = E_3 at ticks, O_5(n) = E_5(n+1)
  exactly when O_5(n) = O_3(n).)

H1 is refuted, as predicted. The clean metronome is two seats deep. Seat 4 misses on every black-to-white fall, and seat 5 misses
exactly at d.

**Observation (not a hypothesis set beforehand): the tick side stays linear longer.** At ticks, the ORs near the wall are jammed:
- E_1 = 1, and E_2 and E_3 are always opposite, so E_1 OR E_0 and E_3 OR E_2 are both black;
- the AND-terms that appear at E_5 and E_6 cancel (GPT's cancellations).

So the tick column is built from XOR and NOT alone through seat 6, and the first surviving AND is at E_7. On the tock side an AND
appears already at O_4. The black tick is what linearises its neighbourhood.

## 3. GPT's question: what does the finite white tail force?

**Proposition 1 (the diary and its conductor).**
1. Every half-infinite history with black ticks and tocks b has the starting row (F_1(b), F_2(b), ...).
2. F_(2m+2)(b) = b_m XOR k_m(b_0, ..., b_(m-1)), and F_(2m+3)(b) = c_m(b_0, ..., b_m), for fixed Boolean functions k_m and c_m that do
   not depend on the start.
3. Hence a passing start whose black cells all lie within depth W is exactly a tock sequence with:
   - **conducted tocks:** b_m = k_m(b_0, ..., b_(m-1)) for every m with 2m+2 > W;
   - **checks:** c_m(b_0, ..., b_m) = 0 for every m with 2m+3 > W.

*Proof.* The far neighbour enters each update through XOR. So x(0,j) = a(j-1) XOR g_j(a(0), ..., a(j-2)), where a is the watched
column; this is the triangle behind the record's lanes. For j = 2m+2 the newest entry a(2m+1) is the tock b_m. For j = 2m+3 it is the
tick a(2m+2) = 1, so no new tock enters. Finite support says exactly that F_j(b) = 0 for every j > W. ∎

So after the free chapter, the first ⌊W/2⌋ tocks, **d is no longer an outside input**. Every later tock is written by fixed rules from
the earlier tocks, and the odd depths then check the result. The start enters only through the free chapter. This is DQ-011's "finite
budget of choices", as a statement.

From the table:

    k_0 = 1,  k_1 = 1,  k_2 = NOT (b_0 XOR b_1),  k_3 = NOT (b_1 XOR b_2 XOR (b_0 AND NOT b_1)),
    c_0 = b_0,  c_1 = b_0,  c_2 = b_2 OR ((NOT b_0) AND b_1).

**Hypothesis H2: "the white tail conducts each tock from the previous two alone."** If it did, the rule would be b_m =
XNOR(b_(m-2), b_(m-1)), which is what k_2 is. Then the tocks would eventually repeat 0,0,1 or stay black, and Jen's theorem would
exclude every survivor. *Prediction:* false, because the triangle reaches back (GC1873: one early history bit changes several cells).

*Result:* refuted at the next step. k_3 = XNOR(b_1, b_2) XOR (b_0 AND NOT b_1). In GPT's terms, the conducted discrepancy is

    d_m = NAND(b_m, b_(m+1)) XOR e_m,   e_0 = 0,  e_1 = b_0 AND NOT b_1.

(These are the conductors at time 0. At tick 2n the same rules apply to the shifted sequence, wherever 2m+2 exceeds the support at
2n.) Under the two-tock part alone, d is constant: 1 along 0,0,1 and 0 along all-black.

**Answer to GPT's question, as far as hand work reaches.** The finite white tail turns d into a conducted signal. Its two-tock part,
NAND of the last two tocks, would give a periodic metronome that Jen forbids. So a survivor's irregularity has to live entirely in the
corrections e_m: the part of the conductor that remembers older tocks. Whether e must eventually settle is the open question. It is
DQ-009's memory question, now located exactly.

**Proposition 2 (the present is the next half-width of tocks; in-step merging).**
- A passing row at tick 2n whose black cells lie within depth M is determined by the ⌊M/2⌋ tocks b_n, ..., b_(n+⌊M/2⌋-1). E_j(n)
  uses b_n to b_(n+⌊(j-2)/2⌋), and the cells beyond M are white.
- Two passing histories have the same row at tick 2n exactly when their tocks agree from index n on.

So the owner's funnel, among survivors, is exactly shared tails of tock sequences. *Proof:* a row determines its future and hence its
trace; conversely, E_j(n) = F_j of the shifted tocks. ∎

## 4. Hand deadlines: the machinery reproduces finite facts

*Prediction, written from the table before the simulations:* every start of width at most 4 fails by tick 6, and every start of width
at most 5 fails by tick 8.

- **Width ≤ 4.** The checks give c_1 = b_0 = 0 and c_2 = 0, so b_2 = 0 and b_1 = 0. The conductor gives b_2 = k_2 = XNOR(0,0) = 1.
  This contradicts b_2 = 0. The steps use ticks through 6. Hand simulation of 1101 (tocks 0,0): it passes 0, 2 and 4, and fails at 6.
- **Width 5.** c_2 = 0 gives b_2 = 0 and excludes (b_0, b_1) = (0,1). The conductor's b_2 = XNOR(b_0, b_1) = 0 needs b_0 ≠ b_1, so
  (b_0, b_1) = (1,0). Then b_3 = k_3 = 1 XOR 1 = 0. With b_2 = 0, a short outward step gives F_9 = (NOT b_3) XOR (F_8 OR F_7), which
  is NOT b_3 = 1 here. So the check c_3 fails. The steps use ticks through 8. The only candidate, 10111, was simulated by hand and dies
  at tick 8.
- **Width 6.** The same steps leave exactly one start passing tick 8: tocks (0,0,0,1), start 110101. Its later fate needs F_10 and
  beyond. It is left open by hand.

These are tiny, and no census is claimed. They show that hand rules written in tock language decide real starts correctly.

## 5. Three word-ideas made precise

**Proposition 3 (DQ-004, the deathbed).** Let Σ be a finite set. Suppose that from tick τ on, each row of a start is given a label in
Σ, or the mark ✗ meaning "the test has failed". Suppose the label at t+1 is a fixed function f of the label at t, with f(✗) = ✗. Then
a start that ever fails, fails by τ + |Σ|.

*Proof.* Among the labels at τ, ..., τ + |Σ| that are not ✗, two must be equal, at times s < s'. The labels then repeat with period
s' - s and never reach ✗. ∎

Consequence: doors settled by checking catch a start only within |Σ| ticks of death. A start of width W that passes its free stretch
lives at least W ticks, so a door system applying from τ to all such starts that fail needs τ ≥ W - |Σ|.

**Proposition 4 (DQ-011, no shield).** For any pattern on depths 1 to m and any odd k > m, the two rows that agree below k and differ
at k first differ at the watched cell at tick k-1, which is even. So one of them fails there, whatever lies beyond k.

*Proof:* GPT's first-arrival argument. The difference advances one depth per tick through XOR. ∎ This rules out traps shielded from
the far side, not survivors.

**Proposition 5 (DQ-010, out-of-step meetings).** If two passing histories had equal rows at tick 2n of one and tick 2n'+1 of the
other, the shared future would have a black watched cell at every tick. Condrey's theorem, or Jen's, excludes that for a finite row.
∎

## What remains open

- Does the long-memory correction e_m have to settle? If it settled into a repeating pattern, the tocks would repeat and Jen would
  finish the test. The question needs a property of the k_m for all m, not more cells.
- Which property of the conductor survives as m grows? The two values k_2 and k_3 suggest "XNOR of the last two, plus terms involving
  a black-to-white fall further back". That is a pattern seen twice, not a law.
- What exactly is DQ-009's referee at seat j? Seat 4 misses on falls, and seat 5 misses at d. A clean statement for every seat is
  not in hand.

## Reasoned and gut verdicts

**Reasoned:** GC1889 carries. The owner's metronome is exact two seats deep, and its first two missed beats are named: falls at seat
4, GPT's d at seat 5. The white tail makes the discrepancy a conducted signal, whose local part forces a periodic metronome. Survival
would have to live in the long-memory corrections.

**Gut:** warm. The tock language is the first coordinate system in which the conductor, the checks and the funnel are all one-line
statements. I am wary of the next temptation, expanding k_4, k_5 and so on by hand: without a question for them, that recreates the
growing-rulebook route GPT warned against.
