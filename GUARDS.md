# GUARDS: mistakes made, and the rules that stop them being made again

*Started 2026-10-30 by Cloud at the owner's request: "where a mistake was made in your original propositions (not a failed
prediction, but an unguarded mistake in your thinking) construct some memory rules that guard against such a mistake".
A failed prediction is good science and stays in the record as it is. An unguarded mistake is a step taken without the
check that would have caught it; each one below names the step, the entry, and the rule. Cloud reads this file at the
start of every session, after `NOW.md`. Any worker may add a guard; keep the pairing of mistake and rule.*

## The guards

| | The mistake (entry) | The rule |
|---|---|---|
| G1 | Parity rules stated without their smallest cases: the reversal law needed "prefix period even" (P = 1 fails, GC2256); the one-line Case A needed P >= 4 (P = 2 fails, GC2261). Made twice in one day (CL650, CL654). | **Smallest cases first.** Every statement about periods, parities or lifting is checked by hand at the two smallest periods (1 and 2) and the guard is written into the statement before anything else is written. |
| G2 | "Exactly 2^(w-3) of the 2^(w-2) rows, one quarter" (CL659): the words and the formula disagree, and the table in front of me said 2^(w-4). | **A closed form is read back against two rows of its own table before it is written.** If the words give a fraction, multiply it out. |
| G3 | Ratios printed to three decimals named as 1/4, 3/8, 7/16 and called a "law" (CL654): the retained integers are 125/512, 12057/32768, 28397/65536, none of them the named fractions (GC2261). | **No fraction is named from a decimal.** Print numerator and denominator, test the named fraction exactly, and call anything that fails that test a pattern, never a law. |
| G4 | The sixteen-gate probe inherited "wheel 0 is constant" from the OR map; for gates with g(0,0) = 1 wheel 0 toggles, and the NOR and "b OR NOT s" densities were wrong (CL654; GC2261's audit; corrected CL662). | **Generalising a probe to a family: list the original's implicit invariants** (which cells never change, the wall, the seed region, the base period) **and re-verify each for every member with a literal brute-force control on tiny cases** before any census is read. |
| G5 | "The leftward recursion is a T-function in space, so each step keeps or doubles the period" (CL660), written in the same entry as the data 1 -> 3 that contradicts it; the recursion is a four-state transducer and the constant-one driver has a 3-cycle (GC2261/GC2270). | **A theorem transferred by analogy is transferred with its hypotheses:** write them, check each in the new frame, and check the transferred law against every data point already in hand. |
| G6 | The wall frame's death times compared with physical finite rows as if the wall-frame starts were rows with a white wall beside them (CL655, CL656 P32): the wall frame is the sideways transform of Q01, a frame of column profiles (GC2266 gives the exact bridge T(r) = (r mod 2) + 2 Psi(r)). | **Before comparing two censuses, write both frames' definitions and the map between them.** If no map is written, no comparison is made. |
| G7 | "Longest plateaus 14 wheels at P = 32 and 103 at P = 64" quoted from L1066 as plateau maxima; those count stretches above period 2, a different statistic; the maxima are 10 and 92 (GC2264). | **A number cited from the record carries the exact definition of its statistic.** When my question uses another definition, say so or recompute. |
| G8 | The classifier "a black bottom wheel always ticks the next" proposed for the six odometer-like gates without checking it against the six: AND fails it (GC2261). Candidate monotones (fill, own parity, overlap) proposed without a small-seed check: seed 5 refutes all three. | **A classifier or a monotone is tested against every row of the table it is meant to explain, and against the smallest seeds, before it is posed.** |
| G9 | "The left wheels' exponents are Theta(log j)" (CL654, F3): our own delivered theorem `seed_infinitely_many_white/black` gives infinitely many left wheels of period 1; only a running maximum can grow. | **Pointwise against running maximum.** For a sequence with infinitely many trivial terms, growth is stated as a running maximum; and our own kit modules are checked before stating what grows. |
| G10 | L(w) <= w + C for the finite-row head start called "a small theorem" (CL658 A6): a uniform finite bound settles the open CQ01 reduction (`CQ01_iff_no_finite_period_two`). | **Before calling a target small, test whether it implies a known open statement** (CQ01_iff, Q01_iff_Theta, the realization barrier, the all-width bound) **and say so.** |
| G11 | The left-wheel transient scanned only from t >= j, so tau_1 = 0 where the right value is 1 (CL654; GC2264). | **A measured statistic is defined so that its smallest cases give sensible values, and those cases are printed and read.** |
| G12 | The owner's question on the past of a finite row answered beside §8.19 (5 October) when the study he meant was GC2015 to GC2024 (28 October) (CL659; corrected CL660). | **When the owner refers to recent work, find it in the ledger by date before answering.** |
| G13 | Blocks closed without separating the two kinds of error. | **Every block's closing note lists failed predictions and unguarded mistakes under separate headings**, and any new mistake gets a row here. |

## How to use this file

- At session start: read the table once; it is short on purpose.
- Before posting a hand rule: G1, G2, G3, G5.
- Before running or reading a census: G4, G6, G7, G11.
- Before posing a question or a classifier to another worker: G8, G9, G10.
- Before answering the owner about earlier work: G12.
- At the end of a block: G13.
