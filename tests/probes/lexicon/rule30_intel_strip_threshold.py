#!/usr/bin/env python3
"""rule30_intel_strip_threshold.py: SX, the exactness threshold L(W) of the strip form for full traces, both phases
(KIMI-QUESTIONS-4, Q1; the swarm's door D4; assigned to Intel in CL297, section 8.89).

RUN-ON:     the Intel MacBook (16 logical cores); C with OpenMP (rule30_intel_strip_trace.c beside this file)
COMMAND:    python3 tests/probes/lexicon/rule30_intel_strip_threshold.py build
            python3 tests/probes/lexicon/rule30_intel_strip_threshold.py run PHASE N WMIN WMAX
            python3 tests/probes/lexicon/rule30_intel_strip_threshold.py report N
COST:       the real traces of length N from all 2^N rows (N = 32: 2^26 bit-sliced blocks, 0.5 GB, about a minute on
            16 threads); the strip walks take seconds to W = 14. Logs in NP_SCRATCH_SX (default ~/np-scratch/rule30-sx).

The object (KIMI-QUESTIONS-4). The wall is x_t(0) = (t + phase) mod 2. T(l) is the set of traces (column 1 at EVERY
time, y_0 .. y_{l-1}) of length l over all right halves; T^W(l) the traces of the width-W strip (sites 1..W, a free
input at site W+1 at every step). T(l) is contained in T^W(l). The exactness threshold is L(W) = max {l : T^W(l) =
T(l)}; Conjecture S is L(W) >= 2W - 1 for every W. Q1 asks for L(W) for W <= 10 in both phases, whether L(2k) =
L(2k+1), and what the traces of T^W(L(W)+1) outside T(L(W)+1) are.

Engine (rule30_intel_strip_trace.c, Intel's own code). Real traces: all rows of sites 1..N, 64 at a time bit-sliced,
the light cone run N steps; T(l) is the set of length-l prefixes of the length-N traces (a trace of length l depends
only on sites 1..l). Strip traces: a depth-first walk over trace bits whose state is the set of possible strip rows
(a bitset over 2^W rows); only real prefixes are extended, so at every length the walk counts the real strip traces
(the containment control) and the fresh extra traces (real prefix, not real). L(W) is the last length with no fresh
extra; extensions of an extra are extras, so the first failure is the threshold. This script's report adds, for every
extra trace f, its least excluding width w(f) by a separate subset walk (numpy) at widths W+1, W+2, ...

Record searched: `record_find.py 'Conjecture S'` -> KIMI-QUESTIONS-4 and older unrelated uses (8.36's R(d) <= d + 4,
GC746); `'exactness threshold'` -> KIMI-QUESTIONS-4 only (the calibration L(1..5) = 3, 6, 6, 10, 10, L(6) >= 15);
`'strip form'` -> 8.89 (the decision), KIMI-QUESTIONS-4; `'L.2k.'` -> KIMI-QUESTIONS-4's Q1 only. 8.83 holds
the 938 minimal absent traces to length 84 with w(f) <= ceil(|f|/2), tight at 2, 4, 7, 11, 35, 36, 61. Disclosed
third-party knowledge, read before this header: the swarm's door D4 report (outside git, an agent's output, unverified
until this probe), whose claims are SX-C1 below.

PREDICTIONS, registered 08:15 BST before the runs. Run before this header: only the published calibration (standard
phase, N = 16, W = 1..5), which the engine reproduces exactly: |T(1..16)| = 2 3 4 5 7 8 10 12 15 18 22 26 32 36 44 49,
L(1..5) = 3, 6, 6, 10, 10, the extra traces 0000 and 0101 (W = 1), 0001000 (W = 2, 3), 11001101001 (W = 4, 5),
each minimal absent, and 11 against 10 at W = 3, l = 7, 23 against 22 at W = 5, l = 11.
  SX-C0 (controls, must hold): at every W and l the walk finds every real trace (containment); L(W) is
         non-decreasing in W (T^{W+1} is contained in T^W); L(W) >= W + 2 (the proved w(f) <= |f| - 2).
  SX-C1 (third-party claims to reproduce): standard phase, T^W(2W) = T(2W) for every W reached and T^W(2W+1) differs
         from T(2W+1) exactly at W = 3 and 5 among W <= 15; odd phase, T^W(2W+1) differs at W = 1, 7 and 12 among
         W <= 13, and T^W(2W) at W = 12 among W <= 15. These give standard L(W) >= 2W + 1 for W = 6..15 and odd L(1) =
         2, L(7) = 14, L(12) = 23.
  SX-P1 (blind, 0.35): the standard phase pairs at k = 3, 4, 5: L(6) = L(7), L(8) = L(9), L(10) = L(11).
  SX-P2 (blind, 0.7): the odd phase breaks the pairing at least once among k = 1..5.
  SX-P3 (blind, 0.5): standard phase, L(W) <= 2W + 4 for every W = 6..10.
  SX-P4 (blind, 0.4): standard phase, at most two fresh extra traces at L(W) + 1 for every W = 6..10.
  SX-P5 (blind, 0.3): wherever L(2k) = L(2k+1), the two widths have the same extra traces, as at 2/3 and 4/5.
  SX-P6 (blind, 0.6): every fresh extra trace at L(W) + 1 is minimal absent (without its first two symbols it is real),
         for W = 1..14 in both phases.
  Counterfactual: a containment failure, a decrease of L in W, or an extra at a length <= W + 2 contradicts a proved
  fact and would refute the instrument, not the conjecture; so would a calibration value that moves.
  Unexpected check: the least excluding width w(f) of every extra trace, and whether it is tight (w(f) = ceil(|f|/2),
  the case that would make Conjecture S sharp at that length). Not predicted.
  Scope: N = 32 in both phases (traces to length 32), W = 1..14; L(W) is exact where L(W) + 1 <= 32 and is reported as
  a lower bound otherwise.

OUTCOME (2026-10-11 08:21 BST). Both phases, N = 32 (2^32 rows each, 8 s on 16 threads), W = 1..14. Tables, extra
traces and their least excluding widths: rule30_intel_strip_threshold.txt beside this file. All COMPUTED.
  L(W), W = 1..14, standard phase: 3, 6, 6, 10, 10, 17, 20, 20, 20, 26, 30, >= 32, >= 32, >= 32.
  L(W), W = 1..14, odd phase:      2, 7, 7, 11, 11, 14, 14, 19, 19, 23, 23, 23, 29, 29; and L(15) = 29 follows (below).
  Cross-check: an independent numpy enumeration of all 2^24 rows gives the same |T(l)| for l = 1..24 in both phases,
         and confirms every extra trace to length 24 absent, its prefix and its two-step suffix real, and its least
         excluding width (width w(f) - 1 produces it, w(f) does not).
  SX-C0: containment PASS at every W and l in both phases; L non-decreasing in W. The third clause, L(W) >= W + 2,
         holds at every W in the standard phase and FAILS in the odd phase at W = 1: L(1) = 2, because the trace 000
         is produced by the width-1 strip and by no right half. Checked by hand from the rule: with x_0(0) = 1,
         y_0 = y_1 = 0 forces x_0(2) = 1, so x_1(2) = 1 and y_2 = x_1(2) = 1; the strip takes e_0 = 1, e_1 = 0. The
         instrument is right; the registration was wrong to assume the lemma w(f) <= |f| - 2 in both phases. It is a
         standard-phase lemma (KIMI-QUESTIONS-4's setting) and false in the odd phase at |f| = 3.
  SX-C1 REPRODUCED in full: standard T^W(2W) = T(2W) for W <= 15 and T^W(2W+1) differs only at W = 3, 5 (W <= 15;
         W = 12..15 by L(12) >= 32 and monotonicity); odd T^W(2W+1) differs at W = 1, 7, 12 (W <= 13) and T^W(2W)
         at W = 12 and 15. The last follows from computed facts: L(15) >= L(14) = 29, and the length-30 extra trace
         below has w(f) = 16, so the width-15 strip produces it and L(15) <= 29.
  SX-P1 REFUTED: the standard phase pairs at k = 4 (20, 20) and not at k = 3 (17 against 20) or k = 5 (26 against 30).
  SX-P2 REFUTED: the odd phase pairs at every k = 1..5 (7, 11, 14, 19, 23) and first breaks at k = 6 (23 against 29).
  SX-P3 REFUTED: L(6) = 17, L(7) = 20 and L(10) = 26 exceed 2W + 4; held at W = 8, 9.
  SX-P4 HELD (2, 2, 2, 2, 1 extra traces at W = 6..10). SX-P5 HELD (every equal pair shares its extra traces).
  SX-P6 HELD: every extra trace at L(W) + 1 is minimal absent, both phases, every W reached.
  Unexpected check, the least excluding widths. Standard phase: w(f) = ceil(l/2) at l = 4, 7, 11 (w = 2, 4, 6) and
         well below it at l = 18, 21, 27, 31 (w = 7, 10, 11, 12 against 9, 11, 14, 16). Odd phase: w(f) = ceil(l/2)
         at l = 3, 8, 12, 15, 20, and ABOVE it at l = 24 and 30: 001000100110001001101000 has w = 13 > 12 and
         011001100010011001100110011000 has w = 16 > 15. So the per-trace form w(f) <= ceil(|f|/2) fails in the odd
         phase (the record has this from the swarm's agent and skeptic, STRATEGY-PLAN.md; here by Intel's own code,
         with the two shortest witnesses), while L(W) >= 2W - 1 holds there with no slack at W = 12 and 15
         (L = 23, 29). KIMI-QUESTIONS-4's "equivalently" between the two forms holds for odd lengths only.
  Reading (Q1). The pairing is not a law. L is a step function: L(W) + 1 is the length of the shortest absent trace
         that width W does not exclude, and a plateau ends exactly at the least excluding width of its extra traces
         (standard W = 7, 8, 9 share 000100110100010011000 and 110100110100010011000, both w = 10, and L jumps at 10).
         Plateaus of two widths come from extras whose w(f) is the next even width (standard w = 4, 6; odd w = 4, 6, 8,
         10); the odd plateaus of three widths (10..12, 13..15) come from the two extras with w = 13 and 16, the ones
         above ceil(l/2). So L(2k) = L(2k+1) fails exactly when an extra trace at L(2k) + 1 has w(f) = 2k + 1: standard
         k = 3 and 5 (w = 7, 11), odd k = 6 (w = 13); everywhere else to W = 14 the extras' w(f) is at least 2k + 2.
         The slack L(W) - (2W - 1)
         grows in the standard phase (2, 3, 1, 3, 1, 6, 7, 5, 3, 7, 9, then >= 9) and stays at most 4 in the odd
         phase (1, 4, 2, 4, 2, 3, 1, 4, 2, 4, 2, 0, 4, 2, 0). So if Conjecture S fails anywhere, the odd phase is
         where to look, and in the odd phase it cannot be improved to 2W. The extra traces form one family across
         the phases: dropping the first symbol (one time step, which swaps the phase) takes a threshold extra of one
         phase to a threshold extra of the other at four pairs: 0000 and 000, 0001000 and 10001000, 11001101001 and
         011001101001, 110100110100010011000 and 10100110100010011000. Six of the nine extra traces of length 18 or
         more end in 10011000.

SX-P7, registered 2026-10-11 09:30 BST before the extension runs (CL302 (a): push the odd phase beyond W = 15). The
engine now keeps the real traces in per-thread hash sets instead of a 2^N bitmap (output identical at N = 32 in both
phases), so N is bounded by time only: N = 38 (2^38 rows), odd phase first, then the standard phase, W = 1..20.
Disclosed third-party claims (the swarm's door D4, SAT with DRAT-checked UNSATs, unverified by Intel beyond W = 15):
in the odd phase T^W(2W-1) = T(2W-1) for W <= 18 and T^W(2W) = T(2W) except at W = 12, 15; that is, L(W) >= 2W at
W = 16, 17, 18.
  (a, blind 0.85) Conjecture S holds at every odd-phase width whose L(W) the run determines (L(W) >= 2W - 1).
  (b, blind 0.7) no zero slack at W = 16, 17, 18 in the odd phase (it rests on the door's claims).
  (c, blind 0.5) odd L(16) >= 33 (slack at least 2).
  (d, blind 0.5) standard L(12) >= 34.
  (e, blind 0.4) every new threshold extra trace is minimal absent and has a partner under first-symbol dropping
         among the other phase's threshold extras, as four of the earlier ones do.
  Counterfactual: an L(W) < 2W - 1 refutes Conjecture S in that phase; it would be reported with a strip witness and
  re-checked by SAT on the light cone before any claim.

OUTCOME of SX-P7 (2026-10-11 09:59 BST). Both phases, traces to length 38 (2^38 right halves each; 912 s odd, 746 s
standard, 16 threads), W = 1..20. Containment PASS at every width and length; the results at W <= 14 (odd) and
W <= 11 (standard) are identical to the length-32 run. Tables: rule30_intel_strip_threshold.txt; the extra traces
with least widths, partners and strip witnesses: rule30_intel_strip_extras.txt (CL302 (b)). All COMPUTED.
  L(W), W = 1..20, odd phase:      2 7 7 11 11 14 14 19 19 23 23 23 29 29 29 33 35 37, and >= 38 at 19, 20.
  L(W), W = 1..20, standard phase: 3 6 6 10 10 17 20 20 20 26 30 32 34 34 34 34 34, and >= 38 at 18..20.
  (a) HELD: Conjecture S holds at every width determined (odd W <= 18, standard W <= 17). (b) HELD: the odd slack
         L(W) - (2W - 1) is 2 at W = 16, 17, 18; zero slack occurs only at W = 12 and 15. (c) HELD: odd L(16) = 33.
  (d) REFUTED: standard L(12) = 32. (e) REFUTED: all nine new extra traces are minimal absent, but only four have a
         first-symbol partner (two new pairs: odd 0110001001100010011000100110011001 with standard
         00110001001100010011000100110011001, odd 100010011010001001101000100110011000 with standard
         00010011010001001101000100110011000); five have none.
  The swarm door's claims are reproduced to the widths they name: standard T^W(2W+1) differs from T(2W+1) exactly
         at W = 3, 5, 17 (W <= 17) and T^W(2W) = T(2W) to W = 17; odd T^W(2W-1) = T(2W-1) to W = 18.
  Reading. The standard slack rises to 9 at W = 11..13 and then falls along the plateau L = 34 (W = 13..17) to 1 at
         W = 17, where the extra is 8.83's tight trace of length 35 (w = 18). In the odd phase every extra from W = 16
         on is tight (w = ceil(l/2) at lengths 34, 36, 36, 38), with L(W) = 2W + 1 at W = 16, 17, 18; the two odd
         extras above ceil(l/2) (lengths 24 and 30) are the only ones of their kind to length 38 in either phase. So
         the odd phase has a run of tight cases at every length 34..38 of its thresholds, the material Q3 of
         KIMI-QUESTIONS-4 asks for. Every extra of length 20 or more ends in 0011000 or 0011001 except the odd one of
         length 24 (ending 1101000). The run of tight cases is evidence for an infinite tight family, not a proof.

SX-P8 and SX-P9, registered 2026-10-11 10:28 BST before their runs (CL314: Intel's lane is the strip form again).
SX-P8: the odd phase with real traces to length 40 (2^40 right halves, about an hour on 16 threads), W = 1..20.
  (a, control) containment PASS everywhere, and every result at W <= 18 identical to the length-38 run.
  (b, 0.7) Conjecture S holds at W = 19 (L(19) >= 37). (c, 0.5) L(19) = 39, so the odd run L(W) = 2W + 1 continues.
  (d, 0.5) the extra traces at L(19) + 1 are tight (w(f) = 20). (e, 0.6) L(20) is not determined at length 40.
SX-P9: the column tableau of every tight extra trace and of the two above ceil(l/2) (rule30_intel_strip_extras.txt,
lengths up to 38, both phases). Column 0 is the wall and column 1 the trace; column i+1 is forced where column i is
white (x_t(i+1) = x_{t+1}(i) XOR x_t(i-1)) and free where it is black; column i passes its check when every black
x_t(i) has x_{t+1}(i) XOR x_t(i-1) = 1. A branch is one choice of all free entries; it dies at the first column whose
check fails, and w(f) is the deepest death column (CL309's correspondence). The search merges identical pairs of
adjacent columns, so branch counts are exact integers. Measured per trace: the number of branches dying at each
column; the number of distinct surviving column pairs per column; and the last repair column, the deepest column
with a state whose free choices lead to subtrees of different maximal death column.
  (a, control) the deepest death column equals w(f) of the family file for every trace, and sampled real traces of
         length 30 to 38 have a branch passing every check.
  (b, 0.6) for every trace more than 90% of all branches die by column 3.
  (c, 0.5) for every tight trace the last repair column is at most ceil(l/2) - 2: the freedom is spent at least two
         columns before the halfway column, and the deepest branches are forced from there to their death.
  (d, 0.5) on the deepest branches a single column pair survives at every column from the last repair column on.
  Unexpected check (not predicted): whether the two traces above ceil(l/2) (odd, lengths 24 and 30) spend their last
  freedom later than the tight ones.

OUTCOME of SX-P9 (2026-10-11 11:02 BST): all 16 tight or above-half extra traces of the family file, lengths 3 to 38,
both phases, 8.6 minutes in Python (tableau_profile; table in rule30_intel_strip_tableau.txt). All COMPUTED exactly.
  (a) HELD to length 34, undetermined beyond: the deepest death column equals w(f) for all 16 traces; sampled real
         traces of lengths 22, 24, ..., 34 admit complete tableaux; at 36 and 38 the search reached its cap of five
         million column pairs per column before completing, so those controls are undetermined, not passed.
  (b) REFUTED: the share of branches dead by column 3 is 1.4 to 3.7% for the long traces (lengths 34..38), 9 to 12%
         for the two above-half traces, and above 90% only for 000, 0000 and 0101; most branches die in columns 4..13.
  (c) HELD, with a caveat: the last repair column is w(f) - 2 for every trace, so ceil(l/2) - 2 for every tight one
         (none for the three traces with w(f) = 2). Under this definition that is close to automatic (at column
         w(f) - 2 some choices die at once and others reach w(f)), so it is weak evidence. Unexpected check: the two
         above-half traces spend it one column later (11 and 14), as their w(f) is one more than ceil(l/2).
  (d) REFUTED: the deepest branch is a single column pair from column 1 to column 7..13 for the long traces (one
         length-36 trace carries two parallel deepest branches from column 2), and then fans out in the last three or
         four columns: 2, 12, 21, 84, 360 deepest pairs at columns 13..17 for the standard length-35 trace, 577 at
         column 16 for the odd length-34 trace. Every one of them dies at column w(f).
  Reading for the tableau form of Conjecture S: a forced spine, a short burst of freedom just before the halfway
         column, and then a contradiction for every alternative. Every final failure of a deepest branch is at time
         t <= 9, inside a check range of up to 19 times: the contradiction appears near the initial row, in the early
         half of the last column, not at its light-cone edge.

OUTCOME of SX-P8 (2026-10-11 11:23 BST): the odd phase with real traces to length 40, 2^40 right halves, 3,260 s on 14
threads; 842 real traces of length 40. All COMPUTED.
  (a) HELD: containment PASS at every width 1..20, and every threshold and extra trace at W <= 18 identical to the
         length-38 run. (b) HELD: Conjecture S holds at W = 19. (c) REFUTED: L(19) >= 40, not 39, so the odd run
         L(W) = 2W + 1 (W = 16, 17, 18) stops at W = 18, and the slack at W = 19 is at least 3. (d) not testable: no
         extra trace at W = 19 within length 40. (e) HELD: L(20) >= 40, not determined.

SX-P10, registered 2026-10-11 13:47 BST before its runs (CL326: the standard phase's L(18) and beyond, and the death
columns of the standard tight traces). The brute force stops near length 40, so a second engine (mode grow, pysat
1.9 with CaDiCaL): T(l) grown level by level, a candidate g + b (g in T(l), b in {0, 1}, its two-step suffix in
T(l - 1)) tested for realness by one incremental SAT solver on the length-64 light cone with the trace assumed; the
candidates that are absent are the minimal absent traces (prefix and two-step suffix real), and each gets its least
excluding width w(f) by bisection over strip widths, each width one more incremental solver (the strip's cells with
a free input beyond). Since the shortest absent trace a width-W strip produces is itself minimal absent, L(W) + 1 is
the least length of a minimal absent trace with w(f) > W, determined wherever that length is reached. Target length
61 in both phases (8.83's tight length), further if time allows.
  (a, control) |T(l)| equals the exhaustive counts at every l <= 38 (standard) and l <= 40 (odd); the thresholds and
         extra traces reproduce the brute force for W <= 17 (standard) and W <= 18 (odd), and every w(f) of the
         family file.
  (b, 0.85) Conjecture S, L(W) >= 2W - 1, holds at every W determined in both phases.
  (c, 0.6) standard phase: every minimal absent trace reached has w(f) <= ceil(l/2) (8.83's lane, to 84); the tight
         lengths are among 2, 4, 7, 11, 35, 36, 61 and include 7, 11, 35 and 61.
  (d, 0.5) odd phase: at least one more trace above ceil(l/2) beyond length 38.
  (e, 0.6) standard L(18) lies in 38..42.
  (f, 0.5) the standard tight traces of length 36 and 61, when found, have SX-P9's death-column shape: a forced spine,
         a fan-out in the last three or four columns, every final failure at time t <= 12.
  Counterfactual: an L(W) < 2W - 1 refutes Conjecture S; a standard w(f) > ceil(l/2) refutes 8.83's per-trace claim.
  Unexpected check (not predicted): how the number of minimal absent traces grows with l in each phase.

OUTCOME of SX-P10 (2026-10-11 15:17 BST). Both phases grown to length 90 (85 minutes each, seven worker processes;
length 64 took 80 s); results in rule30_intel_minimal_absent_traces.txt (the counts, L(W), the tight and above-half
traces, and all 1,245 standard and 1,623 odd minimal absent traces with w(f)). All COMPUTED (SAT, no proof logs).
  (a) HELD: |T(l)| equals the exhaustive counts at every l <= 38 (standard) and <= 40 (odd); every threshold the
         brute force determined is reproduced; all 26 w(f) of the family file agree. Two second-party agreements with
         the record: |T(84)| = 17,651 (KIMI-QUESTIONS-4) and 938 standard minimal absent traces to length 84 (8.83's
         lane, the same count under this minimality convention).
  Standard L(W), W = 18..39: 40 42 42 49 52 52 54 56 56 59 60 60 60 72 72 74 76 80 84 84 84 84; at least 90 from 40.
  Odd L(W), W = 19..39:          43 43 46 46 53 53 57 57 58 61 61 61 71 71 73 73 73 81 81 81 81; at least 90 from 40.
  (b) HELD: Conjecture S holds at every W <= 39 in both phases; the slack is 1 at standard W = 30 (L = 60) and at
         least 7 from W = 31 on; in the odd phase zero slack occurs only at W = 12 and 15, and the slack is at least 4
         from W = 31 on.
  (c) HELD: every standard minimal absent trace to length 90 has w(f) <= ceil(l/2); the tight lengths are exactly 2,
         4, 7, 11, 35, 36, 61 (eight traces). So 8.83's "equality only at 7, 11, 35, 61" omits 10 (2), 0000 and 0101
         (4) and 010001001100010011000100110001001100 (36), which KIMI-QUESTIONS-4's list has.
  (d) REFUTED: no odd-phase trace above ceil(l/2) beyond length 30, to length 90; the only two remain those of
         lengths 24 and 30. Odd tight lengths: 2, 3, 8, 12, 15, 20, 34, 36, 38, 62.
  (e) HELD: standard L(18) = 40.
  (f) REFUTED for the length-36 trace as worded, undetermined at 61: the standard tight trace of length 36 has its
         deepest branch unique only through column 5 and then widening gradually (2, 4, 5, 10, 16, 24, 51, 360 deepest
         pairs at columns 6..17), with every final failure at time t <= 3; the length-61 search reached its cap of eight
         million column pairs at column 5 (2.8 million there).
  Unexpected check: the minimal absent counts alternate with the parity of l, in opposite senses in the two phases
         (standard: 48 to 83 at odd l = 75..89 against 15 to 31 at even l = 76..90; odd phase the reverse), as the
         first-symbol map between the phases (one time step, a change of length by one) implies. The long tight words
         pair across the phases the same way: the odd tight trace of length 62 is 0 followed by the standard one of
         length 61, and the odd one of length 36 is 1 followed by the standard one of length 35.

SX-P11, registered 2026-10-11 16:12 BST before its runs: a certificate for SX-P10, so that the census can be adopted on
sight under the owner's two-tier-review rule (CL354) and Q10's caveat "SAT without proof logs" (GC1150.1) can go.
Method. (1) Realness: every real trace of length l is a prefix of a real trace of length 90 (a right half that makes
it makes a length-90 trace too), so one witness row per trace of T(90) certifies every T(l), l <= 90; each row is
re-simulated directly, and the prefix sets must reproduce every |T(l)|. (2) Completeness: the candidates at length
l + 1 (extensions g + b of T(l) whose two-step suffix is in T(l - 1)) that are not prefixes of T(90) must be exactly
the listed minimal absent traces; each one's absence gets a DRAT proof from the cadical binary, checked by drat-trim.
(3) Widths: each w(f) gets a strip witness at width w(f) - 1 (an initial strip and its inputs, re-simulated) and a
DRAT proof, checked by drat-trim, that width w(f) does not produce f. Certificate data in scratch; the verdicts and
SHA-256 digests of the trace lists, the witness rows and the CNFs in git. The CNF encoding is the one SX-P10 used; its
independent control remains the exhaustive brute force to lengths 38 and 40. Registered with jobctl.py at priority 3.
  (a, 0.95, control) the regrown census equals SX-P10's line for line.
  (b, 0.95) every length-90 witness row re-simulates to its trace, and the prefix sets reproduce |T(l)| for l <= 90.
  (c, 0.9) every listed absence (1,245 standard, 1,623 odd) has a DRAT proof that drat-trim verifies, and the
         candidates outside the prefix sets are exactly the listed traces.
  (d, 0.9) every w(f) is confirmed by a re-simulated strip witness at w(f) - 1 and a verified DRAT proof at w(f).
  Counterfactual: any failure withdraws the thresholds that depend on it until they are recomputed.
SX-P11 OUTCOME (run 2026-10-11 16:14 to 18:01 BST, six workers a phase; the owner's halt of 17:54 that day, CL365,
  held it in scratch until the owner gave the word on 2026-10-14). All COMPUTED, single-party (Intel).
  Phase 0: 24,383 witness rows (one per trace of T(90)); 1,245 minimal absent traces; 1,242 strip witnesses (every
         w(f) >= 2; the other three have w(f) = 1); 2,490 refutations (1,245 absences, 1,245 widths) by cadical
         3.0.1, every DRAT proof verified by drat-trim; the certification stage took 203 s.
  Phase 1: 25,975 witness rows; 1,623 minimal absent traces; 1,621 strip witnesses; 3,246 refutations, every proof
         verified; 243 s.
  (a) HELD: the regrown census equals SX-P10's line for line in both phases.
  (b) HELD: every witness row re-simulates to its trace, and the prefix sets reproduce |T(l)| for l = 1..90.
  (c) HELD: the candidates outside the prefix sets are exactly the listed traces (1,245 and 1,623), and every absence
         has a verified DRAT proof.
  (d) HELD: every w(f) >= 2 has a re-simulated strip witness at w(f) - 1, and every w(f) a verified refutation at
         width w(f).
  SHA-256 digests (the files stay in scratch; proof files were deleted after checking, as the module says):
         phase 0 grow log     1bb55f62d4725d884c6be9e715a4aa12773c78b59f3cae839a36cd7dec82aab8
         phase 0 witnesses    53eaad35da039bcd7e8851703c0aadc1e99a5650c0ff771df628d66e2750dd5f
         phase 0 CNFs (2,490) a359db8ee73e2328706e8ed50225fda93a4091f8260c5d9e130552cc9e8c6507
         phase 1 grow log     cbf0f11c0b389a1686fb9ed51415fc11ea48f3d9935df6dbd77d3c1598ee4f5f
         phase 1 witnesses    19136ceea170ba671642b78fba1a01a694427ef90585deecc1adec0f6458f317
         phase 1 CNFs (3,246) 53261cdf759d7bc47ece72b05aea367e95cbebbaf246f7d0bdddf2016c2c778e
  The CNF digest is the SHA-256 of the sorted lines "kind trace cnf-sha256" (rule30_intel_trace_cert.py), so a reader
  who regenerates the CNFs from the committed trace list (rule30_intel_minimal_absent_traces.txt) and _cone_clauses
  reproduces it without our files. Scope: this certifies SX-P10's trace census and the thresholds L(W) to W = 39 that
  follow from it (IN010; the caveat "SAT without proof logs" in 8.83's IN010 paragraph and PERIOD-TWO.md Q10). It does
  not touch 8.83's earlier caveat on the 1,612 minimal absent words to 48 (lane q3's). The caveat stays until another
  party re-checks the refutations and a second read follows (Cloud's sequence, relayed by the owner on 2026-10-14).

SX-P11 replay, registered 2026-10-14 17:22 BST before its runs: a dig under the instinct rule (INSTINCT.md, Intel,
  17:16). The certification stage is rerun three days on, on copies of the stored grow logs and witness files, with a
  negative control. It is not a second read (same party, same code). It takes under ten minutes, so it is not
  registered with jobctl.py.
  Record searched: SX-P11; "proof logs"; drat-trim reject; negative control DRAT -> the SX-P11 registration, the
  caveats above, and rule30_kick_bite_drat.py's control (a satisfiable formula has no refutation; a cut-down proof
  is not a fair control because a trivial formula verifies from a single lemma). No control of this kind for SX-P11.
  (R1, 0.95) the stored files' SHA-256 equal those above; the rerun's verdict lines equal 11 October's apart from
         times; its per-CNF digest files equal the stored ones line for line (5,736 lines), every proof regenerated by
         cadical 3.0.1 and verified by drat-trim.
  (R2, 0.95; the unexpected check: can the checker say no?) for every 120th minimal absent trace f of each phase's
         sorted list, with g a real trace of the same length (a prefix of a witness trace): g's absence CNF is
         satisfiable (cadical exit 10); drat-trim rejects f's DRAT proof when checked against g's CNF (a satisfiable
         formula has no valid refutation, so an acceptance would mean the check is unsound); and when w(f) >= 2,
         f's strip CNF at width w(f) - 1 is satisfiable.
  Counterfactual: a digest mismatch is traced to its cause (a tool version or a changed file) before the census is
  offered for adoption; an accepted borrowed proof withdraws every SX-P11 DRAT verdict until it is explained.
"""
import os, re, subprocess, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'rule30_intel_strip_trace.c')
SCRATCH = os.environ.get('NP_SCRATCH_SX', os.path.join(os.path.expanduser('~'), 'np-scratch', 'rule30-sx'))
BIN = os.path.join(SCRATCH, 'rule30_intel_strip_trace')
OMP = ['-Xpreprocessor', '-fopenmp', '-I/usr/local/opt/libomp/include', '-L/usr/local/opt/libomp/lib', '-lomp'] \
    if sys.platform == 'darwin' else ['-fopenmp']
OUT = os.path.join(HERE, 'rule30_intel_strip_threshold.txt')


def build():
    os.makedirs(SCRATCH, exist_ok=True)
    subprocess.run(['cc', '-O2', *OMP, SRC, '-o', BIN], check=True)
    print('built', BIN)


def run(phase, n, wmin, wmax):
    os.makedirs(SCRATCH, exist_ok=True)
    log = os.path.join(SCRATCH, f'sx_p{phase}_n{n}_w{wmin}-{wmax}.log')
    t0 = time.time()
    with open(log, 'w') as fh:
        subprocess.run([BIN, str(phase), str(n), str(wmin), str(wmax)], stdout=fh, check=True)
    print(f'{log}: {time.time() - t0:.0f} s')
    return log


def parse(log):
    T, LW, X, contain, real, extra = {}, {}, {}, {}, {}, {}
    for line in open(log):
        p = line.split()
        if not p: continue
        if p[0] == 'T': T[int(p[1])] = int(p[2])
        elif p[0] == 'LW': LW[int(p[1])] = p[2]
        elif p[0] == 'X': X.setdefault(int(p[1]), []).append((int(p[2]), p[3], p[4]))
        elif p[0] == 'CONTAIN': contain[int(p[1])] = p[2]
        elif p[0] == 'W':
            w, l = int(p[1]), int(p[3].rstrip(':')); real[(w, l)] = int(p[5]); extra[(w, l)] = int(p[10])
    return T, LW, X, contain, real, extra


def strip_produces(f, V, phase):
    """True when the width-V strip (free input at site V+1) produces the trace f (string, y_0 first)."""
    n = np.arange(1 << V, dtype=np.int64); mask = (1 << V) - 1; S = np.ones(1 << V, dtype=bool)
    for t, ch in enumerate(f):
        S &= ((n & 1) == int(ch))
        if not S.any(): return False
        if t == len(f) - 1: return True
        wall = (t + phase) & 1; idx = np.flatnonzero(S); S2 = np.zeros(1 << V, dtype=bool)
        for e in (0, 1):
            c = idx; R = (c >> 1) | (e << (V - 1)); S2[((((c << 1) | wall) & mask) ^ (c | R)) & mask] = True
        S = S2
    return True


def least_width(f, phase, start, cap=22):
    for V in range(start, cap + 1):
        if not strip_produces(f, V, phase): return V
    return None


def report(n):
    out = ['# SX: exactness thresholds L(W) of the strip form, full traces (KIMI-QUESTIONS-4, Q1). Intel, 2026-10-11.',
           '# Engine rule30_intel_strip_trace.c; see rule30_intel_strip_threshold.py. Traces are written y_0 first.']
    LWall = {}
    for phase in (0, 1):
        log = os.path.join(SCRATCH, f'sx_p{phase}_n{n}_w1-{14 if n <= 32 else 20}.log')
        T, LW, X, contain, real, extra = parse(log); LWall[phase] = LW
        out += ['', f'## phase {phase} (wall x_t(0) = (t + {phase}) mod 2), traces to length {n}',
                '|T(l)|, l = 1..%d: %s' % (n, ' '.join(str(T[l]) for l in range(1, n + 1)))]
        for w in sorted(LW):
            out.append(f'W = {w}: L(W) = {LW[w]}; containment {contain[w]}')
            for (l, f, mn) in X.get(w, []):
                wf = least_width(f, phase, w + 1)
                out.append(f'    extra at l = {l}: {f} ({mn}); w(f) = {wf}, ceil(l/2) = {(l + 1) // 2}'
                           f'{" TIGHT" if wf == (l + 1) // 2 else ""}')
    import textwrap
    out = [w for l in out for w in (textwrap.wrap(l, 118, subsequent_indent='    ') if len(l) > 118 else [l])]
    open(OUT, 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))


def strip_witness(f, V, phase):
    """an initial strip row (sites 1..V, site 1 first) and inputs e_0..e_{l-2} with which the width-V strip produces
    the trace f, by forward subset sets and a backward choice; verified by direct simulation"""
    n = np.arange(1 << V, dtype=np.int64); mask = (1 << V) - 1; l = len(f); S = []
    cur = (n & 1) == int(f[0])
    for t in range(l):
        S.append(cur)
        if t == l - 1: break
        wall = (t + phase) & 1; idx = np.flatnonzero(cur); nxt = np.zeros(1 << V, dtype=bool)
        for e in (0, 1):
            nxt[((((idx << 1) | wall) & mask) ^ (idx | ((idx >> 1) | (e << (V - 1))))) & mask] = True
        cur = nxt & ((n & 1) == int(f[t + 1]))
        if not cur.any(): return None
    state = int(np.flatnonzero(S[-1])[0]); inputs = []
    for t in range(l - 2, -1, -1):
        wall = (t + phase) & 1; idx = np.flatnonzero(S[t]); found = None
        for e in (0, 1):
            img = ((((idx << 1) | wall) & mask) ^ (idx | ((idx >> 1) | (e << (V - 1))))) & mask
            hit = np.flatnonzero(img == state)
            if hit.size: found = (int(idx[hit[0]]), e); break
        state, e = found; inputs.append(e)
    row, inputs = state, inputs[::-1]
    x = row; tr = ''
    for t in range(l):                                   # verification by direct simulation
        tr += str(x & 1)
        if t < l - 1:
            x = ((((x << 1) | ((t + phase) & 1)) & mask) ^ (x | ((x >> 1) | (inputs[t] << (V - 1))))) & mask
    assert tr == f, (f, tr)
    return ''.join(str((row >> i) & 1) for i in range(V)), ''.join(map(str, inputs))


def extras(n_by_phase):
    """CL302 (b): the extra traces at L(W) + 1 for both phases, with least excluding widths, the first-symbol map
    between the phases and a strip witness at width w(f) - 1, written to rule30_intel_strip_extras.txt"""
    out = ['# SX extras: the traces of T^W(L(W)+1) outside T(L(W)+1), both phases (KIMI-QUESTIONS-4 Q1, CL302 (b)).',
           '# Intel, 2026-10-11, rule30_intel_strip_threshold.py. Traces are written y_0 first (column 1 at every',
           '# time t >= 0); the wall is x_t(0) = (t + phase) mod 2. Per threshold: the widths W sharing it, L, the',
           '# trace, its least excluding width w(f) against ceil(l/2), and "minimal" when the trace without its first',
           '# two symbols is real. The partner is a threshold extra of the other phase equal to the trace without its',
           '# first symbol, or one whose own first-symbol drop is the trace. The witness, at width w(f) - 1, is the',
           '# initial strip (sites 1..w(f)-1, site 1 first) and the inputs e_0 .. e_(l-2) fed at site w(f); every',
           '# witness is re-simulated to the trace.']
    found = {}
    for phase in (0, 1):
        T, LW, X, contain, real, extra = parse(os.path.join(SCRATCH, f'sx_p{phase}_n{n_by_phase[phase]}_w1-20.log'))
        found[phase] = (LW, X)
    allx = {p: {f for w in found[p][1] for (_, f, _) in found[p][1][w]} for p in (0, 1)}
    for phase in (0, 1):
        LW, X = found[phase]; groups = {}
        for w in sorted(X):
            key = tuple(sorted(f for (_, f, _) in X[w])); groups.setdefault(key, []).append(w)
        out += ['', f'## phase {phase}, traces to length {n_by_phase[phase]}; thresholds L(W): '
                + ' '.join(f'{w}:{LW[w]}' for w in sorted(LW))]
        for key, ws in groups.items():
            out.append(f'W = {ws[0]}..{ws[-1]}: L = {LW[ws[0]]}')
            for f in key:
                l = len(f); wf = least_width(f, phase, ws[-1] + 1, cap=24)
                mn = [m for (_, g, m) in X[ws[0]] if g == f][0]
                other = 1 - phase
                part = [g for g in allx[other] if g == f[1:]] + [g for g in allx[other] if g[1:] == f]
                wit = strip_witness(f, wf - 1, phase)
                out += [f'  {f}  (l = {l}) w(f) = {wf}, ceil(l/2) = {(l + 1) // 2}'
                        f'{" TIGHT" if wf == (l + 1) // 2 else (" ABOVE" if wf > (l + 1) // 2 else "")}, {mn}; '
                        f'partner in phase {other}: {", ".join(part) if part else "none"}',
                        f'    witness at width {wf - 1}: strip {wit[0]}, inputs {wit[1]}']
    import textwrap
    wrapped = []
    for l in out:
        wrapped += textwrap.wrap(l, 118, subsequent_indent='      ', break_long_words=True) if len(l) > 118 else [l]
    open(os.path.join(HERE, 'rule30_intel_strip_extras.txt'), 'w').write('\n'.join(wrapped) + '\n')
    print('\n'.join(wrapped))


def tableau_profile(f, phase, cap_states=5_000_000):
    """SX-P9: the column tableau of trace f (column 0 the wall, column 1 the trace). Column i+1 is forced where column
    i is white and free where it is black; column i passes its check when every black x_t(i), t <= l-i-1, has
    x_{t+1}(i) XOR x_t(i-1) = 1. Layers merge identical pairs of adjacent columns; branch counts are exact."""
    l = len(f)
    wall = sum((((t + phase) & 1) << t) for t in range(l)); col1 = sum(int(c) << t for t, c in enumerate(f))
    bit = lambda x, t: (x >> t) & 1

    def check(prev, cur, i):
        for t in range(0, l - i):
            if bit(cur, t) and not (bit(cur, t + 1) ^ bit(prev, t)): return t
        return None

    def children(prev, cur, i, all_candidates=False):
        n = l - i; forced = [None if bit(cur, t) else bit(cur, t + 1) ^ bit(prev, t) for t in range(n)]
        free = sum(1 for v in forced if v is None); out = []

        def dfs(t, val, last):
            if t == n: out.append(val); return
            for v in ((0, 1) if forced[t] is None else (forced[t],)):
                if not all_candidates and t > 0 and last == 1 and v != (1 ^ bit(cur, t - 1)): continue
                dfs(t + 1, val | (v << t), v)
        dfs(0, 0, 0)
        return out, free
    if check(wall, col1, 1) is not None:
        return dict(l=l, wmax=1, death={1: 1}, layers=[], deep=[], last_repair=None, freebits=[], fail_times=[])
    death = {}; edges = []; cur = {(wall, col1): 1}; i = 1; complete = False
    while True:
        if i >= l - 1: complete = True; break
        nxt = {}; E = {}
        for (prev, c), cnt in cur.items():
            ch, free = children(prev, c, i)
            dead = (1 << free) - len(ch)
            if dead: death[i + 1] = death.get(i + 1, 0) + dead * cnt
            E[(prev, c)] = [(c, x) for x in ch]
            for x in ch: nxt[(c, x)] = nxt.get((c, x), 0) + cnt
        edges.append(E)
        if not nxt: break
        if len(nxt) > cap_states: return dict(l=l, capped=True, layers=[len(e) for e in edges])
        cur = nxt; i += 1
    layers = [len(e) for e in edges]
    if complete: return dict(l=l, wmax=None, complete=True, death=death, layers=layers)
    maxd = {}
    for k in range(len(edges) - 1, -1, -1):
        col = k + 1
        for st, ch in edges[k].items():
            maxd[(col, st)] = max((maxd[(col + 1, c)] for c in ch), default=col + 1)
    wmax = max(death); last = None; deep = []; freebits = []; fail_times = set()
    for k in range(len(edges)):
        col = k + 1; ds_states = [st for st in edges[k] if maxd[(col, st)] == wmax]
        deep.append(len(ds_states))
        freebits.append(sorted({bin(st[1] & ((1 << (l - col)) - 1)).count('1') for st in ds_states}))
        for st in ds_states:
            ch = edges[k][st]; free = bin(st[1] & ((1 << (l - col)) - 1)).count('1')
            outcomes = {maxd[(col + 1, c)] for c in ch}
            if len(ch) < (1 << free): outcomes.add(col + 1)
            if len(outcomes) > 1: last = col
            if col == wmax - 1:                       # the deepest states: where does column wmax fail?
                cands, _ = children(st[0], st[1], col, all_candidates=True)
                for x in cands:
                    t = check(st[1], x, wmax)
                    if t is not None: fail_times.add(t)
    tot = sum(death.values())
    return dict(l=l, wmax=wmax, death=death, layers=layers, deep=deep, last_repair=last, freebits=freebits,
                fail_times=sorted(fail_times), share3=sum(v for c, v in death.items() if c <= 3) / tot,
                range_wmax=l - wmax + 1)


def tableau_report(samples=6, seed=11):
    """SX-P9 over every tight or above-half extra trace of rule30_intel_strip_extras.txt, plus sampled real traces"""
    import random, re
    rx = re.compile(r'^  ([01]+)  \(l = (\d+)\) w\(f\) = (\d+), ceil\(l/2\) = (\d+) (TIGHT|ABOVE)')
    words = []; phase = None
    for line in open(os.path.join(HERE, 'rule30_intel_strip_extras.txt')):
        m = re.match(r'^## phase (\d)', line)
        if m: phase = int(m.group(1))
        m = rx.match(line)
        if m and (m.group(1), phase) not in [(w[0], w[1]) for w in words]:
            words.append((m.group(1), phase, int(m.group(3)), m.group(5)))
    out = ['# SX-P9: the column tableau of every tight extra trace and of the two above ceil(l/2), both phases.',
           '# Intel, 2026-10-11, rule30_intel_strip_threshold.py (tableau_profile). Per trace: deaths = branches dying',
           '# at each column (exact); layers = distinct surviving column pairs per column; deep = deepest states per',
           '# column; free = free bits on the deepest states per column; last repair = the deepest column where a free',
           '# choice changes the maximal death column; fail t = the times at which the deepest branches fail their',
           '# last check, with the check range of that column.']
    for f, ph, wf, kind in sorted(words, key=lambda w: (w[1], len(w[0]))):
        r = tableau_profile(f, ph)
        ok = r.get('wmax') == wf
        out += ['', f'phase {ph} {f} (l = {len(f)}, w(f) = {wf}, {kind}): deepest death column {r.get("wmax")} '
                    f'({"matches" if ok else "DIFFERS"}); last repair column {r["last_repair"]}, ceil(l/2) - 2 = '
                    f'{(len(f) + 1) // 2 - 2}; share dead by column 3: {r["share3"]:.4f}',
                f'  deaths: ' + ' '.join(f'{c}:{v}' for c, v in sorted(r['death'].items())),
                f'  layers: {" ".join(map(str, r["layers"]))}',
                f'  deep:   {" ".join(map(str, r["deep"]))}',
                f'  free:   ' + ' '.join('/'.join(map(str, x)) for x in r['freebits']),
                f'  fail t at column {r["wmax"]} (its check range 0..{r["range_wmax"] - 2}): {r["fail_times"]}']
    rnd = random.Random(seed)
    out += ['', '# control: sampled real traces (random rows), each must admit a complete tableau']
    for k in range(samples):
        l = 22 + 2 * k; ph = k % 2; row = [rnd.randint(0, 1) for _ in range(l)]; tr = ''
        x = row[:]
        for t in range(l):
            tr += str(x[0]); w = (t + ph) & 1
            x = [(w if i == 0 else x[i - 1]) ^ (x[i] | (x[i + 1] if i + 1 < l else 0)) for i in range(l)]
        r = tableau_profile(tr, ph)
        out.append(f'  phase {ph} l = {l} {tr}: complete tableau {r.get("complete", False)}'
                   + (' (capped)' if r.get('capped') else ''))
    import textwrap
    out = [w for line in out
           for w in (textwrap.wrap(line, 118, subsequent_indent='    ', break_long_words=True)
                     if len(line) > 118 else [line])]
    open(os.path.join(HERE, 'rule30_intel_strip_tableau.txt'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'report'
    if mode == 'build': build()
    elif mode == 'run': run(*[int(a) for a in sys.argv[2:6]])
    elif mode == 'report': report(int(sys.argv[2]) if len(sys.argv) > 2 else 32)
    elif mode == 'extras': extras({0: int(sys.argv[2]), 1: int(sys.argv[3])})
    elif mode == 'tableau': tableau_report()
