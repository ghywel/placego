# When do E's launch in finite right halves? The transient measurement, and the hand-off of the witness search and the rank (Cloud, CL757)

*Cloud, 9 November 2026, at the owner's word (CL757), after the assessment CL756. Status: MEASURED (own code, self-tested), one host. Code: `tests/probes/swarm/sw02/block3/cloud_transient_scan.py` with `cloud_transient_selftest.py` and `cloud_transient_report.py`; outputs beside them; the evidence tarball is in the shared store (digest in the ledger).*

## 1. What is measured, and why

CL756 argued that the single physical 4→7 passage resists every tool because it is a Rule 30 preimage problem whose constraints are deep, and that the quantity we keep approaching is the information the initial row supplies to column 1. If E launches are paid for with that information, they are a transient: in a finite right half of support k, no E launches long after the information has arrived, and the universal theorem (finitely many E's; no E in an eventual period) is a speed-of-information argument rather than a search. If instead E's launch at times unrelated to the support, the dynamics sustains them and only a rank argument can close the question.

**The frame.** A finite right half beside the alternating centre (black at even ticks) is a row on cells 1..k at tick 1 with cell k black; k is the support. The row is evolved exactly (bit-packed, 64 cells a word, one cell of growth a tick; cells beyond are white). The sampled trace is column 1 at odd ticks. An E is the gap block 3,3,5,3,5,5,5,5 read as a 35-sample pattern (blacks at offsets 0, 3, 6, 11, 14, 19, 24, 29, 34, whites between); its launch tick is the tick of its first black. An A is the block 2,5. The lock time is the first sample from which the trace is periodic to the horizon with period 2, 5 or 7 samples, ten periods at least; a row that is not periodic by the horizon is counted unlocked. For rows with two or more E's the return word is the sequence of A-counts between consecutive E's. The passage is the 180-sample pattern E A⁴ E A⁷ E.

**Self-test (PASS).** The packed evolution agrees with a per-cell simulator on 300 random rows (supports to 39, horizons to 400 ticks); the E and passage detectors find the planted blocks at the right offsets in a synthetic trace; the lock detector finds a planted period 7.

**Runs.** All rows of support ≤ 20 (1,048,575 rows) to tick 2001; all rows of support 21 and 22 (3,145,728 rows) to tick 1501; 20,000 random rows for each support 21 to 40 to tick 4001. Substitute caps (4 GiB virtual a process).

## 2. Results

### 2a. Random rows, supports 21 to 40 (20,000 each, horizon 4001 ticks)

| support k | rows | rows with an E | most E's in a row | latest E launch (tick) | latest / k | unlocked at horizon | lock time mean (samples) | lock time max (samples) | max / k | periods (samples) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 21 | 20,000 | 1,536 | 2 | 2821 | 134.3 | 17585 | 1401.1 | 1951 | 92.9 | 2: 523, 5: 1749, 7: 143 |
| 22 | 20,000 | 1,522 | 2 | 2563 | 116.5 | 17582 | 1364.8 | 1951 | 88.7 | 2: 558, 5: 1706, 7: 154 |
| 23 | 20,000 | 1,547 | 2 | 3355 | 145.9 | 17603 | 1356.5 | 1951 | 84.8 | 2: 580, 5: 1680, 7: 137 |
| 24 | 20,000 | 1,444 | 2 | 2463 | 102.6 | 17601 | 1319.8 | 1951 | 81.3 | 2: 603, 5: 1637, 7: 159 |
| 25 | 20,000 | 1,471 | 2 | 2967 | 118.7 | 17573 | 1347.0 | 1951 | 78.0 | 2: 565, 5: 1689, 7: 173 |
| 26 | 20,000 | 1,539 | 1 | 2683 | 103.2 | 17628 | 1353.1 | 1951 | 75.0 | 2: 572, 5: 1662, 7: 138 |
| 27 | 20,000 | 1,529 | 2 | 2865 | 106.1 | 17569 | 1365.4 | 1951 | 72.3 | 2: 570, 5: 1717, 7: 144 |
| 28 | 20,000 | 1,476 | 2 | 2489 | 88.9 | 17610 | 1339.1 | 1951 | 69.7 | 2: 583, 5: 1656, 7: 151 |
| 29 | 20,000 | 1,469 | 2 | 2689 | 92.7 | 17684 | 1350.1 | 1951 | 67.3 | 2: 552, 5: 1617, 7: 147 |
| 30 | 20,000 | 1,477 | 2 | 3543 | 118.1 | 17565 | 1316.0 | 1951 | 65.0 | 2: 609, 5: 1655, 7: 171 |
| 31 | 20,000 | 1,482 | 2 | 2475 | 79.8 | 17540 | 1357.6 | 1951 | 62.9 | 2: 580, 5: 1727, 7: 153 |
| 32 | 20,000 | 1,470 | 2 | 2543 | 79.5 | 17661 | 1358.6 | 1951 | 61.0 | 2: 551, 5: 1645, 7: 143 |
| 33 | 20,000 | 1,457 | 2 | 2343 | 71.0 | 17563 | 1361.0 | 1951 | 59.1 | 2: 579, 5: 1714, 7: 144 |
| 34 | 20,000 | 1,500 | 2 | 2441 | 71.8 | 17653 | 1348.7 | 1951 | 57.4 | 2: 564, 5: 1636, 7: 147 |
| 35 | 20,000 | 1,504 | 2 | 2511 | 71.7 | 17649 | 1348.4 | 1951 | 55.7 | 2: 572, 5: 1639, 7: 140 |
| 36 | 20,000 | 1,522 | 2 | 2657 | 73.8 | 17647 | 1326.6 | 1951 | 54.2 | 2: 581, 5: 1613, 7: 159 |
| 37 | 20,000 | 1,384 | 2 | 3491 | 94.4 | 17649 | 1348.8 | 1951 | 52.7 | 2: 549, 5: 1640, 7: 162 |
| 38 | 20,000 | 1,480 | 2 | 2291 | 60.3 | 17585 | 1326.2 | 1951 | 51.3 | 2: 612, 5: 1656, 7: 147 |
| 39 | 20,000 | 1,449 | 2 | 2319 | 59.5 | 17644 | 1356.4 | 1951 | 50.0 | 2: 548, 5: 1652, 7: 156 |
| 40 | 20,000 | 1,512 | 2 | 2623 | 65.6 | 17613 | 1361.8 | 1951 | 48.8 | 2: 547, 5: 1682, 7: 158 |

Least-squares line through (k, latest E launch): slope −15.5 ticks per unit of support, intercept 3,181. The latest launch does not scale with the support; the ratio latest/k falls as 1/k because the launch times are the same at every support. About 7.5% of rows show an E at every support (1,384 to 1,547 of 20,000), no row more than two. In the 72 rows with two E's the return word is a single A-count between 7 and 77 (16 occurs five times, 9 and 12 four times each); **no return of 4, 5 or 6 occurs**, and no passage.

**A caveat on the lock columns.** The lock detector requires the trace to be periodic from the lock sample to the horizon with at least ten periods; §2b shows that almost all "locks" it reports fall in the last 200 samples before the horizon, where a chaotic trace can match a period of 2 or 5 by chance over a few dozen samples. The lock means and maxima above are therefore dominated by horizon noise; the genuine locks are the early ones (§2b).

### 2b. Support 30, horizon 8001 ticks (20,000 random rows, with time histograms)

| E launches by 200-tick bin | 0–199: 1,014 | 200–399: 229 | 400–599: 108 | 600–799: 76 | 800–999: 56 | 1000–1199: 15 | 1200–1399: 16 | 1400–1599: 7 | 1600–1799: 6 | 1800–1999: 2 | 2200–2799: 3 (one each in three bins) | 2800–8001: 0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

| locks by 100-sample bin | 0–99: 703 | 100–3699: 0 | 3700–3999: 1,690 (the last 300 samples before the 4001-sample horizon: detection noise) |
|---|---|---|---|

E's per row: 18,469 rows with none, 1,530 with one, 1 with two (return 13). So the E hazard decays fast, by a factor of about four from the first 200-tick bin to the second and roughly geometrically after, with a thin tail to tick 2,693 and nothing in ticks 2,800 to 8,001 across 20,000 rows. Genuine locks (periods 2, 5, 7) happen within the first 100 samples, 200 ticks, for 3.5% of rows, and for no row between sample 100 and the horizon: the other 96.5% are aperiodic in column 1 at tick 8001. Locking is not memoryless with a small hazard; it is an early event or, within this horizon, no event.

**Reading.** Column 1 beside the alternating centre has a short active transient, a few hundred ticks, in which almost all E's launch and the few short-period locks form, followed by a long aperiodic phase in which E's are rare and then absent. Neither phase scales with the support: the row's own width is irrelevant from the start, because the bulk beyond the first few cells is chaotic Rule 30 whatever the initial row, and it is the bulk's left edge that drives column 1. The information-transient hypothesis of CL756 is wrong in its mechanism and right in one consequence: E's are a transient. The quantity we keep approaching is better named the E hazard of the near-wall dynamics, which decays in time, and the absence of the compact returns 4 and 6 says the X grammar's cheapest moves are not taken by real rows.

### 2c. Exhaustive rows, supports ≤ 22

(PENDING-EXHAUSTIVE)

## 3. Predictions judged

- P-V1 (latest E launch below 10k + 100 for every support ≤ 40): **MISSED**. The latest launch is 2,291 to 3,543 ticks at every support 21 to 40, about a hundred times the support; it does not scale with k at all.
- P-V2 (no row with more than four E's): **HELD**, with room: no row has more than two (420,000 random rows; exhaustive rows in §2c).
- P-V3 (every row periodic by the horizon, lock time linear in k): **MISSED**. About 96.5% of rows are aperiodic at tick 8001; the genuine locks all happen within 200 ticks.
- P-V4 (no passage; returns obey the grammar): **HELD**, and more: no return of 4 or 6 at all, so the grammar's first rule is never tested by real rows.
- P-V5 (the E hazard decays): **HELD**. 1,526 launches in ticks 1 to 2000, 3 in 2001 to 4000, none in 4001 to 8000 (support 30).
- P-V6 (locking memoryless, about 24% by 8001): **MISSED**. Genuine locks are 3.5%, all within the first 100 samples; the apparent 12% at horizon 4001 was detection noise at the horizon.

## 4. Hand-off: the witness search and the rank (for GPT on the Intel host, at the owner's word)

**(a) The witness search for the single passage.** Object: a row at tick 1 (cells 1..360 free, the rest irrelevant to the 359 ticks) whose column 1 at odd ticks is E A⁴ E A⁷ E, beside the alternating centre; equivalently, by GC2709's reduction, a seam tail q < 2^360 whose reconstructed past and determined future pass the head filters. What exists: the original 359-tick CNF with GPT's derived clauses (4520 at both sources, source64, the quartet, the 28 units), and Cloud's passage sets, the exact width-W window sets at every phase of the passage (`cloud_passage_lift.py` regenerates them to width 62 in a few minutes; they are the strongest cheap pruning available: a partial row's determined windows must lie in the set of their phase and width). Suggested shape: either a solver run of hours, not thousands of conflicts, on the CNF with the derived clauses, or a depth-first extension of the tick-1 row cell by cell with the passage sets as the lookahead, from the seam outward if GPT prefers its seam coordinates. Outcome A: a witness, which settles realisability for arbitrary rows at once and gives GPT's joint-state work a concrete history. Outcome B: hours without a witness, which is the evidence CL756 asked for that the irreducible part is cryptographic, and the signal to stop paying for exclusion by search.

**(b) The rank.** Object: a function on (window, grammar state) that strictly decreases at every E launch and is bounded below on realisable windows, or an obstruction of the same uniformity; it would close the whole X language at once where the sweep closed fifty words at widths 43 to 65. Data: the deletion-rank certificates of the dead words (`cloud_cycle_lift_*.out`, checkpoints on request), which say which windows die first and why; the six-sample and five-sample supports (GC2770's certificates), which say what an E launch requires of the near past; and the measurement in §2, which says whether E's are a transient. A first probe: for each dead word, the windows deleted at the lowest ranks, read as cell patterns, and the quantity that separates them from the survivors (the position of the first black beyond column 1, the black count in cells 2..W, a parity along a diagonal).

**(c) Further measurement, if wanted:** the death width of (A⁴EAⁿE)^∞ for n = 16, 20 (the sweep stopped at resource caps with millions of windows at widths 35 to 38; Python-int continuation beyond 62 is in `cloud_cycle_lift_big.py`), and the latest E launch against the support at supports 41 to 60 by sampling, to extend §2's law.
