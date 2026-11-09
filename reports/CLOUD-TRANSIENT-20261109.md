# When do E's launch in finite right halves? The transient measurement, and the hand-off of the witness search and the rank (Cloud, CL757)

*Cloud, 9 November 2026, at the owner's word (CL757), after the assessment CL756. Status: MEASURED (own code, self-tested), one host. Code: `tests/probes/swarm/sw02/block3/cloud_transient_scan.py` with `cloud_transient_selftest.py` and `cloud_transient_report.py`; outputs beside them; the evidence tarball is in the shared store (digest in the ledger).*

## 1. What is measured, and why

CL756 argued that the single physical 4→7 passage resists every tool because it is a Rule 30 preimage problem whose constraints are deep, and that the quantity we keep approaching is the information the initial row supplies to column 1. If E launches are paid for with that information, they are a transient: in a finite right half of support k, no E launches long after the information has arrived, and the universal theorem (finitely many E's; no E in an eventual period) is a speed-of-information argument rather than a search. If instead E's launch at times unrelated to the support, the dynamics sustains them and only a rank argument can close the question.

**The frame.** A finite right half beside the alternating centre (black at even ticks) is a row on cells 1..k at tick 1 with cell k black; k is the support. The row is evolved exactly (bit-packed, 64 cells a word, one cell of growth a tick; cells beyond are white). The sampled trace is column 1 at odd ticks. An E is the gap block 3,3,5,3,5,5,5,5 read as a 35-sample pattern (blacks at offsets 0, 3, 6, 11, 14, 19, 24, 29, 34, whites between); its launch tick is the tick of its first black. An A is the block 2,5. The lock time is the first sample from which the trace is periodic to the horizon with period 2, 5 or 7 samples, ten periods at least; a row that is not periodic by the horizon is counted unlocked. For rows with two or more E's the return word is the sequence of A-counts between consecutive E's. The passage is the 180-sample pattern E A⁴ E A⁷ E.

**Self-test (PASS).** The packed evolution agrees with a per-cell simulator on 300 random rows (supports to 39, horizons to 400 ticks); the E and passage detectors find the planted blocks at the right offsets in a synthetic trace; the lock detector finds a planted period 7.

**Runs.** All rows of support ≤ 20 (1,048,575 rows) to tick 2001; all rows of support 21 and 22 (3,145,728 rows) to tick 1501; 20,000 random rows for each support 21 to 40 to tick 4001. Substitute caps (4 GiB virtual a process).

## 2. Results

(PENDING-RESULTS)

## 3. Predictions judged

(PENDING-PREDICTIONS)

## 4. Hand-off: the witness search and the rank (for GPT on the Intel host, at the owner's word)

**(a) The witness search for the single passage.** Object: a row at tick 1 (cells 1..360 free, the rest irrelevant to the 359 ticks) whose column 1 at odd ticks is E A⁴ E A⁷ E, beside the alternating centre; equivalently, by GC2709's reduction, a seam tail q < 2^360 whose reconstructed past and determined future pass the head filters. What exists: the original 359-tick CNF with GPT's derived clauses (4520 at both sources, source64, the quartet, the 28 units), and Cloud's passage sets, the exact width-W window sets at every phase of the passage (`cloud_passage_lift.py` regenerates them to width 62 in a few minutes; they are the strongest cheap pruning available: a partial row's determined windows must lie in the set of their phase and width). Suggested shape: either a solver run of hours, not thousands of conflicts, on the CNF with the derived clauses, or a depth-first extension of the tick-1 row cell by cell with the passage sets as the lookahead, from the seam outward if GPT prefers its seam coordinates. Outcome A: a witness, which settles realisability for arbitrary rows at once and gives GPT's joint-state work a concrete history. Outcome B: hours without a witness, which is the evidence CL756 asked for that the irreducible part is cryptographic, and the signal to stop paying for exclusion by search.

**(b) The rank.** Object: a function on (window, grammar state) that strictly decreases at every E launch and is bounded below on realisable windows, or an obstruction of the same uniformity; it would close the whole X language at once where the sweep closed fifty words at widths 43 to 65. Data: the deletion-rank certificates of the dead words (`cloud_cycle_lift_*.out`, checkpoints on request), which say which windows die first and why; the six-sample and five-sample supports (GC2770's certificates), which say what an E launch requires of the near past; and the measurement in §2, which says whether E's are a transient. A first probe: for each dead word, the windows deleted at the lowest ranks, read as cell patterns, and the quantity that separates them from the survivors (the position of the first black beyond column 1, the black count in cells 2..W, a parity along a diagonal).

**(c) Further measurement, if wanted:** the death width of (A⁴EAⁿE)^∞ for n = 16, 20 (the sweep stopped at resource caps with millions of windows at widths 35 to 38; Python-int continuation beyond 62 is in `cloud_cycle_lift_big.py`), and the latest E launch against the support at supports 41 to 60 by sampling, to extend §2's law.
