# Rule 30 beside an alternating wall: the strip form of the right half

Fourth set, self-contained like the second and third. Same rule, wall and notation as KIMI-QUESTIONS-2.md
(x_{t+1}(i) = x_t(i-1) XOR (x_t(i) OR x_t(i+1)); wall x_t(0) = t mod 2). This set looks to the **right** of the wall.
Mark every assertion **proved**, **computed** or **conjectured**; give computations in a rerunnable form; state what
would refute each claim before you test it.

## Definitions

- A **right half** is a configuration x_0(1), x_0(2), ... on the sites 1, 2, ... beside the wall. It evolves by the
  rule with x_t(0) = t mod 2 as its left boundary; the sites to the right are unbounded.
- Its **trace** is the sequence tau(x) = (x_0(1), x_1(1), x_2(1), ...): column 1 at every time. (The earlier sets used
  only the even times, the "visible sequence"; here all times count.) T(l) is the set of traces of length l over all
  right halves. A trace of length l depends only on sites 1 .. l (light cone), so T(l) is a finite computation on 2^l
  rows.
- The **strip of width W** keeps only the cells 1 .. W. It evolves by the same rule with the wall on its left and a
  **freely chosen input bit** e_t at site W+1 at every step t: x_{t+1}(W) = x_t(W-1) XOR (x_t(W) OR e_t). T^W(l) is the
  set of its traces of length l over all initial strips and all input sequences.
- A trace f is **absent** if f is not in T(|f|); it is **minimal absent** if every proper factor of it (every shorter
  window, at any offset) is in T. For an absent trace f, its **least excluding width** w(f) is the least W with f not in
  T^W(|f|).

Facts you may take as given (proved elsewhere; prove them yourself first, it is quick):
- T(l) is a subset of T^{W+1}(l), which is a subset of T^W(l): a real right half is a strip with the true exterior as
  its input, and a strip of width W+1 is a strip of width W whose input is itself computed.
- Traces are closed under taking windows at **even** offsets (shift time by 2 and the wall phase is unchanged), so an
  absent trace contains a minimal absent factor at an even offset or at offset 0.
- w(f) <= |f| - 2 for every absent trace f (a merger argument on the first exterior constraint).
- Every trace of length l is produced by some strip of width l (trivially), so T^W(l) = T(l) whenever W >= l.

## The strip form (the statement to prove or refute)

**Conjecture S.** For every W >= 1, T^W(2W-1) = T(2W-1): the strip of width W reproduces exactly the real traces of
length 2W-1. Equivalently: every absent trace f has w(f) <= ceil(|f|/2).
(Equivalence of the two forms, and of either with "T^V(2V-1) = T^{V+1}(2V-1) for every V", is proved.)

**What is known (computed, by three independent engines).**
- Conjecture S holds for every W <= 18, in this wall phase and in the other phase (wall x_t(0) = (t+1) mod 2).
- All 938 minimal absent traces of length at most 84 have w(f) <= ceil(|f|/2). The bound is attained (w(f) =
  ceil(|f|/2)) exactly at the lengths 2, 4, 7, 11, 35, 36, 61 among those 938; at every other length some smaller width
  already excludes every minimal absent trace of that length.
- |T(84)| = 17,651.
- **A local proof route is closed.** The natural attack, "repair a strip history into a real history one time step at
  a time", works at times 0 and 1 and first fails at time 2 for widths >= 5. Real lifts of strip histories of width 15
  on the background (100)^m rewrite up to 11 of the 15 initial cells, opening a white region through which exterior
  information runs at speed 1. A proof must be multi-step or global; "no bounded repair radius exists" is conjectured.
- **The light cone is not the mechanism.** Two histories that first differ at site s differ at site s-1 one step later
  only if the cell there was white (a one-step fact about the rule). So a flipped input at (t, W+1) reaches column 1 at
  time t+W exactly along an all-zero anti-diagonal of length W (a "zero lane"). Zero lanes ending at column 1 exist up
  to length 28 and not beyond (computed, exhaustive). Hence the earliest arrival time of an input at column 1 is W for
  every even W <= 28, W+1 for odd W from 5 to 27, and W+4 or W+5 for W from 29 to 40 (computed). In particular "an
  input cannot reach column 1 before time 2W" is false, and no counting of the light cone alone gives the half.

## Calibration (recompute these before anything else)

- |T(l)| for l = 1 .. 16: 2, 3, 4, 5, 7, 8, 10, 12, 15, 18, 22, 26, 32, 36, 44, 49.
- Exactness of the strip: |T^W(l)| against |T(l)| at the first lengths where they can differ.
  W = 1: equal to l = 3. W = 2 and 3: equal to l = 6, and 11 against 10 at l = 7. W = 4 and 5: equal to l = 10, and
  23 against 22 at l = 11. W = 6: equal to l = 17 (corrected 2026-10-11; an earlier draft said 5, 9 and 13 here).
- The minimal absent traces of length at most 14 with their least excluding widths: 10 (1); 011 (1); 111 (1); 0000 (2);
  0101 (2); 0001000 (4); 11001101001 (6); 001101001100 (5); 00110011001101 (6). Note 0001000 has w = 4 = ceil(7/2) and
  11001101001 has w = 6 = ceil(11/2): these are the tight cases at 7 and 11.
- The exactness threshold L(W) = max { l : T^W(l) = T(l) } is L(1) = 3, L(2) = 6, L(3) = 6, L(4) = 10, L(5) = 10 and
  L(6) >= 15 (W = 2: 8 against 8 at l = 6, 11 against 10 at l = 7; W = 4: 18 against 18 at 10, 23 against 22 at 11;
  W = 6: equal at 14 and 15). Conjecture S is the statement L(W) >= 2W - 1 for all W; the data say more, see Q1.

## Questions

**Q1 (the threshold).** Compute L(W) exactly for W = 1 .. 10, both phases. The first values pair up, L(2) = L(3) = 6
and L(4) = L(5) = 10: is L(2k) = L(2k+1) always, and what is the growth (4k + 2 so far)? Prove whatever regularity you
find; a pairing lemma "the strip of width 2k+1 adds nothing to the strip of width 2k for traces" would be a real result.
Describe the traces in T^W(L(W)+1) minus T(L(W)+1): at W = 2, 3 and W = 4, 5 there is exactly one each (0001000 and
11001101001); what are they for W = 6 .. 10, and do they form a family?

**Q2 (prove or refute Conjecture S).** A proof must explain why **half** the trace length in width always suffices,
although the local repair fails from time 2. Candidate shapes, in the order we would try them: (a) a two-step or
k-step repair lemma, with k depending on W but the repaired region bounded; (b) a global argument, e.g. that any strip
history of width W whose trace of length 2W-1 is not real must contain a zero lane of length > W, which the zero-lane
bound forbids for W <= 28 and which would need a hand proof for all W; (c) an inductive argument on W using the
equivalent form T^V(2V-1) = T^{V+1}(2V-1). A refutation is a single absent trace f with w(f) > ceil(|f|/2): give it
with its strip witness (initial strip and input sequence) and show by exhaustion that no right half produces it.

**Q3 (the tight lengths).** The lengths 2, 4, 7, 11, 35, 36, 61 are where some minimal absent trace needs the full width
ceil(l/2). Find the minimal absent traces of lengths 35, 36 and 61 that attain the bound (compute them; they exist),
and look for a construction: is there an infinite family of absent traces with w(f) = ceil(|f|/2)? If so, Conjecture S
cannot be improved; if the family stops, say what a sharper form would be.

**Q4 (zero lanes).** Prove by hand, or compute with a proof-shaped argument, that no zero lane ending at column 1 has
length greater than 28. (A zero lane of length W ending at column 1 at time t is an all-white anti-diagonal
x_{t-j}(1+j) = 0 for j = 0 .. W-1 in a real history.) What property of the real right halves stops the lanes at 28,
and does the same property bound the earliest arrival time of an input at column 1 by W + c for a constant c?

**Q5 (the other phase).** With the wall x_t(0) = (t+1) mod 2, Conjecture S again holds to W = 18. But for the
**even-time** subsequence of the trace (the visible word of the earlier sets) the strip of width n is not exact for
visible words of length n at n = 15 in that phase: the word 101000101010100 is produced by the width-15 strip and by no
right half there (its least excluding width is 16), although it is a real visible word in the standard phase. Explain
the asymmetry between the two phases, and whether the full trace can ever show it.

## How to answer

Prove, compute or conjecture, and say which. Recompute the calibration first and report any disagreement before
anything else. For every computation give the code and its exact output; for every proof give it in full, not a sketch.
If a question is beyond reach, say so and give the strongest partial result you can establish, with its exact scope.
Do not quote the known facts above as evidence for a claim; they are the shared starting point. Put failed attempts
in, briefly: a refuted approach is worth recording.

## Addendum (2026-10-11 08:30 BST; optional to hand over, written after the questions above)

Computed since the questions were set, by an independent engine over all right halves (bit-sliced, 2^32 rows), with a
numpy enumeration to length 24 agreeing:
- L(W) for W = 1..11 in this wall phase: 3, 6, 6, 10, 10, 17, 20, 20, 20, 26, 30; and L(12), L(13), L(14) >= 32.
- L(W) for W = 1..15 in the other phase: 2, 7, 7, 11, 11, 14, 14, 19, 19, 23, 23, 23, 29, 29, 29.
- So Conjecture S holds at every width computed and is sharp in the other phase at W = 12 and 15 (L(W) = 2W - 1). The
  pairing of Q1 is not a law: it fails here at W = 6/7 and 10/11 and in the other phase at 12/13; L(2k) = L(2k+1)
  holds exactly when the extra trace at L(2k) + 1 has least excluding width 2k + 2 or more.
- The extra traces of the two phases are one family: dropping the first symbol (one time step, which swaps the
  phase) carries 0000 to 000, 0001000 to 10001000, 11001101001 to 011001101001, and 110100110100010011000 to
  10100110100010011000.
- The lemma w(f) <= |f| - 2 of the facts above is a statement about this wall phase. In the other phase the trace 000
  is produced by the width-1 strip and by no right half, so L(1) = 2 there and the lemma fails at |f| = 3.
Q1 is therefore answered to W = 11 and 15; Q2 to Q5 stand, and the other phase at W = 12 is the smallest case where
the bound 2W - 1 is attained.

## Second addendum (2026-10-11, after the first two answer rounds; optional to hand over)

Confirmed on this side by independent computation, all exact: |T(l)| for l = 17..24 is 59, 64, 78, 86, 102, 112, 133,
144 (and 172, 184 at 25, 26 are consistent with the engine that produced them); the extra traces at the exactness
thresholds are exactly as reported, in this wall phase 0000 and 0101 (W = 1), 0001000 (W = 2, 3), 11001101001 (W = 4,
5), 001100110001001100 and 110100110001001101 (W = 6, l = 18), 000100110100010011000 and 110100110100010011000 (W = 7,
8, 9, l = 21), and in the other phase 011010011001101 (W = 6, 7, l = 15) and 10100110100010011000 (W = 8, 9, l = 20).
The calibration line above had three stale numbers (5, 9, 13); it now reads 6, 10, 17, which is what every engine finds.

Two of the derivations are worth keeping as proved facts. (1) The anti-diagonal pair automaton never merges: from the
pair (D_t, D_{t+1}) the earlier diagonal is recovered cell by cell, D_{t-1}[j-1] = D_{t+1}[j] XOR (D_t[j] OR
D_{t+1}[j+1]) (XOR is invertible), so every earlier diagonal and hence every initial cell x_0(i) = D_{i-1}[i] is
determined by the pair at any later step: the state map from initial prefixes is injective, and all compression of the
trace language lies in the output map. (2) The column-tableau correspondence: f is in T^W(l) exactly when a consistent
tableau of W columns exists with column 1 equal to f, so the least excluding width w(f) is the largest death column over
the search branches, and Conjecture S is equivalent to: every word of length l that admits a tableau through column
ceil(l/2) admits a complete one. That is the form in which a proof of S should be attempted: a failed check beyond the
halfway column must be repairable by changing free choices before it.

What to do next, in order: Q2 in the tableau form (a proof or a counterexample to the halfway statement; the tight
minimal absent traces of Q3 are where the last repair freedom is exhausted); Q4 to length 42 and beyond (the parity
observation, lanes at odd t only, should be proved or refuted on the way); Q3's list of tight words. Q1 and Q5 are
answered; do not spend time on them.

## Third addendum (2026-10-11, later; optional to hand over)

Computed since by a second engine over all right halves (traces to length 40, both wall phases). In the other phase L(W)
= 29, 33, 35, 37 at W = 15..18 and at least 40 at W = 19 and 20, so the bound 2W - 1 is attained at W = 12 and 15 only,
L(W) = 2W + 1 holds at W = 16, 17, 18 and fails at 19 (slack at least 3); in this phase L(W) = 3, 6, 6, 10, 10, 17, 20,
20, 20, 26, 30, 32, 34, 34, 34, 34, 34 for W = 1..17 and at least 38 from 18, tightest at W = 17 (slack 1, the extra
being the tight trace of length 35). Conjecture S holds at every width determined.

For Q2 and Q3, the shape of the column search (the tableau form of S) on all 16 tight or above-half extra traces of
lengths 3 to 38 in both phases: the deepest death column equals the least excluding width w(f) in every case; the
deepest branch is a single forced column pair from column 1 to column 7..13 (one length-36 trace carries two parallel
deepest branches from column 2); in the last three or four columns before w(f) it fans out into tens to hundreds of
distinct column pairs (the length-35 trace of this phase has 2, 12, 21, 84, 360 branches at columns 13..17; the
length-34 trace of the other phase has 577 at column 16), and every branch dies at column w(f); every final failure is
at a time at most 9, near the initial row, inside a check range of up to 19 times; the last repair column is w(f) - 2
for every trace; only 1.4 to 3.7 percent of branches are dead by column 3. Real traces of lengths 22 to 34 admit
complete tableaux (the positive control); at 36 and 38 the search hit its cap. So a proof of the halfway statement
should explain why a forced spine followed by a short burst of freedom always ends in a contradiction near the top of
the column, exactly at the halfway width.
