# E launches against the gate trap: the trap exclusion carried, the depletion measured, and two chaos tests (Cloud, CL758)

*Cloud, 9 November 2026, at the owner's word (CL758), after GPT's GC2774–GC2782. Status: COMPUTED (the carry, own-code replay) and MEASURED (the cohorts), self-tested, one host. Code: `tests/probes/swarm/sw02/block3/cloud_trap_replay.py`, `cloud_trap_measure.py`, `cloud_trap_measure2.py`, `cloud_shielding_test.py`, `cloud_speed_test.py`, with outputs beside them; the evidence tarball is in the shared store (digest in the ledger).*

## 1. The carry: no E launches from inside the gate trap

The kit's gate trap (`Rule30GateTrap`, data in `GateTrap.lean` at kit `6d2c0579`): 829 width-16 windows of the right half beside the alternating centre at odd times, bit i = column i + 1, closed under the double step for both values of column 17; after entry column 1 shows only gaps 3 and 5 (`gaps_of_entry`). GC2775 computed that the word 3353, the opening of E, has no path inside the trap. Own-code replay (`cloud_trap_replay.py`): all 3,316 transitions stay in the trap (1,647 distinct successor pairs); the 3353 path-set layers are 188, 191, 186, 68, 68, 69, 17, 21, 21, 18, 21, 29, 40, 41, 0, GPT's numbers; the whole E word dies at the same layer, A = 25 at the third sample. Convention control: the white right half placed at my tick 1 enters at tick 295 with window 49415, the kit's `entry_empty` at time 293; the two-tick offset is the kit's white row standing at an even time (its time-1 row is already 100…), so my tick t is the kit's time t − 2. GPT's two roots reproduce exactly in my frame (1045436333: E at 2693, entry 2729; 637749532: entry 19).

**Physical transfer (read, PROVED two-party, computer-assisted).** A real row's odd-time windows are `step2` images of each other with the actual two values of column 17, which the graph admits; the trap is closed; so a row in the trap follows the graph's edges and stays, and cannot realise any word the graph has no path for. Hence E_t ⇒ τ > t (an E launching at odd tick t means the row is outside the trap at t), the factorisation P(E_t) = P(τ > t)·P(E_t | τ > t) is exact counting on a cohort, and E A⁴ E needs no entry at any odd tick ≤ 125, the passage none ≤ 291, because entry is permanent. The prefix-projection item (a passage-consistent path restricted to its first 97 samples is a prefix-consistent path, so the prefix sets contain the passage sets and are nonempty through 62; a free 193-cell tick-1 root and an anchored tick-0 root are different premises) is carried in CL758.

## 2. The measurement: the same cohorts, conditioned on the trap

### 2a. Support 30, 20,000 random rows (seed 2, the CL757 cohort), horizon 8001

**Trap entry.** 17,815 rows enter the gate trap in ticks 0–199, 644 in 200–399, 321, 217, 130, 71, 34, 31, 12, 7, 7, 5, 2, 1 in the following 200-tick bins, and 703 never enter by tick 8001. The mean time outside the trap in the first bin is about 48 ticks: most random rows are captured almost at once. No row leaves the trap once in (0 permanence violations), and **no E launches from inside the trap** (0 of 1,532), the carried exclusion on data.

**The 703 rows never trapped are exactly the early short-period locks.** The per-row re-analysis (`cloud_trap_measure2.py`) finds 703 rows with a period-2 (552) or period-7 (151) column-1 trace from some sample below 100 to the horizon, the same 703 rows: zero rows are neither in the trap nor locked at tick 8001, and no early-locked row is later trapped. (No genuine period-5 lock exists in this cohort; CL757's "period 5" detections were all horizon noise.) So by tick 8001 every one of 20,000 rows has been captured: 96.5% by the gate trap, 2.8% by a period-2 lock, 0.75% by the period-7 ether lock, all the locks within 200 ticks.

**Absorbed and live E's.** Of the 1,532 E launches, 1,513 (98.8%) are followed by trap entry within the E's own 35 samples: the E is the row's entry word. 19 are live (no entry during the block), launching at ticks 7, 17, 21, 25, 29, 59, 61, 63, 63, 79, 91, 97, 171, 241, 247, 263, 361, 891 and 1,761; one row has two E's (return 13). The X lineage's "E returns" are these live E's; the compact returns 4 and 6 have never been seen among them.

**The conditional rate.** Launches per row per tick, by 200-tick bin:

| bin (ticks) | at risk: outside the trap (row-samples) | rate | at risk: outside the trap and not early-locked | rate |
|---:|---:|---:|---:|---:|
| 0–199 | 550,985 | 9.2e-4 | 480,685 | 1.05e-3 |
| 200–399 | 181,690 | 6.3e-4 | 111,390 | 1.03e-3 |
| 400–599 | 136,629 | 4.0e-4 | 66,329 | 8.1e-4 |
| 600–799 | 110,337 | 3.4e-4 | 40,037 | 9.5e-4 |
| 800–999 | 93,146 | 3.0e-4 | 22,846 | 1.23e-3 |
| 1000–1199 | 82,987 | 9.0e-5 | 12,687 | 5.9e-4 |
| 1200–1399 | 78,486 | 1.0e-4 | 8,186 | 9.8e-4 |
| 1400–1599 | 75,447 | 4.6e-5 | 5,147 | 6.8e-4 |
| 1600–1799 | 73,012 | 4.1e-5 | 2,712 | 1.1e-3 |
| 1800–1999 | 72,108 | 1.4e-5 | 1,808 | 5.5e-4 |
| 2000–2799 | about 70,500 each | 0 to 7e-6 | 1,167, 609, 211, 64 | 0, 8e-4, 2e-3, 8e-3 (one launch each) |
| 2800–8000 | 70,300 each | 0 | 0 | — |

With the denominator GPT asked for, rows outside the trap, the rate still falls (from 9.2e-4 to 3.4e-4 by 600–799 and to zero after 2,800), because that denominator is dominated after a thousand ticks by the 703 early-locked rows, which can never launch an E. With the right at-risk set, rows in no closed set, **the rate is flat at about 1·10⁻³ per row per tick** from the first bin to the last bin with more than a thousand row-samples (0.8 to 1.2·10⁻³ where the counts allow; the bins beyond 2,000 hold one launch each). The decline of raw E counts is depletion and nothing else. The same table gives the trap-entry hazard of a chaotic row: 644, 321, 217, 130 entries over the row-samples of bins 200–999 give 2.4 to 2.9·10⁻³ per tick, also flat; so a chaotic row beside the wall is captured at about 2.7·10⁻³ a tick and launches an E at about 1.0·10⁻³ a tick, and about one entry in three happens through an E block. The chaotic population falls by a factor of about 0.6 every 200 ticks and is gone from this cohort by tick 2,800.

### 2b. Exhaustive rows of support ≤ 20, horizon 2001 (1,048,575 rows)

77,642 E launches in 77,508 rows, **none from inside the trap**; 76,760 (98.9%) followed by trap entry within the block, 882 live. Entries: 934,288 rows (89.1%) in ticks 0–199, then 31,778, 18,246, 10,733, 6,571, 3,540, 2,160, 1,236, 844, 416 in the following bins; 38,753 rows (3.7%) never enter by 2001. The raw conditional rate (outside the trap) falls from 9.1·10⁻⁴ in the first bin to 1.3·10⁻⁵ in 1800–1999, as in the support-30 cohort and for the same reason: after a thousand ticks the rows outside the trap are mostly the never-trapped ones (38,753 rows contribute 3,875,300 row-samples to every bin, out of 4.0 to 4.5 million in the late bins). Taking those rows as the early locks, as the per-row analysis showed them to be in the support-30 cohort, the corrected rate per chaotic row per tick is 1.05, 0.91, 0.94, 0.90, 1.02, 1.00, 1.00·10⁻³ in bins 0 to 1399, then 1.2, 1.8 and 2.7·10⁻³ in the last three bins, where the chaotic population is down to a few hundred rows and the horizon censors both the denominator and the 35-sample blocks. The correction is an estimate here, not a per-row count (the per-row analysis over a million rows is slow in Python and was not run); the late-bin rise is unresolved and small in weight (510 launches of 77,642).

## 3. Chaos tests (the owner's method)

**Chaos 1, the frame's phase.** The same 20,000 rows of support 30 placed at tick 0 instead of tick 1 (one tick earlier, centre black first). Rows with an E: 1,467 against 1,531 (7.3% against 7.7%); rows entering the trap in ticks 0–199: 18,022 against 17,815 (90.1% against 89.1%); never in the trap by 8001: 650 against 703 (3.3% against 3.5%); no E from inside the trap in either; the conditional-rate tables agree bin by bin within the counts' noise. **HELD**: the frame's phase does not matter, and the ensemble "random rows at an odd tick" is not special.

**Chaos 2, shielding in the wild.** GPT's single chaos draw (GC2777) replaced the root cells above a fixed low 70 and found every sampled head through 193 preserved, against its prediction. On an ensemble (`cloud_shielding_test.py`): 3,000 random rows of support 120 to tick 400, 182 with an E, 61 with the first E launching in ticks 70..300; cells 71..120 redrawn once at random (cell 120 kept black). The first E survives at the same tick in 45 of 61 (73.8%): 16 of 16 for launches in 50..99, 13 of 13 in 100..149, 5 of 7 in 150..199, 7 of 14 in 200..249, 4 of 11 in 250..299. The first sampled head that differs after the redraw is at median tick 287 (minimum 183, 10th and 90th percentiles 223 and 400), and 59 of 61 rows agree with their originals through tick 193. **HELD** (more than half), and the detail explains GPT's surprise.

**The explanation, and its test.** Rule 30's damage front moves left at 0.2428 ± 0.0003 cells a tick (Grassberger, cited in Wolfram 1986; the record's own finite-time 0.246 at RULE30-PRIZE §8.30 and §8.66; GC2038's path-support cone), while the light cone moves at 1. A change at cell 71 therefore reaches column 1 after about 71/0.243 ≈ 292 ticks, the observed median 287. GPT's "shielding through 193 by the low 70" and "first E protected by 35 cells" (35/0.243 ≈ 144 ticks) are this speed. Prediction P-W4 before the test: redrawing cells above c = 20, 40, 60, 80, 100, the median tick of the first differing sampled head is c/0.243 within 30%. Result (`cloud_speed_test.py`, 2,000 rows of support 120 to tick 600):

| c | predicted c/0.243 | median tick | 10th percentile | 90th percentile | rows unchanged through 600 |
|---:|---:|---:|---:|---:|---:|
| 20 | 82 | 83 | 48 | 205 | 51 |
| 40 | 165 | 175 | 114 | 307 | 72 |
| 60 | 247 | 257 | 185 | 391 | 83 |
| 80 | 329 | 341 | 255 | 487 | 101 |
| 100 | 412 | 417 | 329 | 587 | 174 |

**P-W4 HELD** within 6% at every c. The leftward reach of the initial row into column 1 is set by the damage speed, four times slower than the light cone. For the passage work this is a usable rule: root cells beyond c are irrelevant to the heads before tick c/0.243 in most histories, and GPT's thresholds (35, 68, 69, 70) are where the damage front of the E's own cone arrives, not combinatorial accidents.

## 4. Predictions judged

- P-W1 (entry early: more than half by tick 400, fewer than 5% outside at 2000, fewer than 1% at 8000): **two clauses HELD, one MISSED**: 92% by 400 and 3.6% outside at 2000; but 3.5% are outside at 8000, the early-locked rows, which the counterfactual named (the other closed sets hold them).
- P-W2 (the conditional rate per untrapped row within a factor of two of the first bin through 600–799): **MISSED as worded** (3.4·10⁻⁴ against 9.2·10⁻⁴), because "outside the trap" includes the early locks; with rows in no closed set as the at-risk set the rate is flat at about 1·10⁻³, which is the mechanism the prediction meant. The letter missed; the re-analysis is after the fact and is labelled so.
- P-W3 (every E launch has τ > t): **HELD**, 0 of 1,532 and 0 of 1,470 launches from inside the trap, in both placements.
- Chaos 1 (frame phase irrelevant): **HELD**.
- Chaos 2 (shielding typical, more than half of first E's survive a redraw of cells 71..120): **HELD**, 73.8%.
- P-W4 (the first differing head at c/0.243 within 30%): **HELD** within 6% at every c.

## 5. What this says about E, and what follows

**E is, almost always, the gate trap's entry word.** 98.8% of E launches end in trap entry within the block. The X lineage's returns live on the 1.2% that do not. The clock, the 4→7 passage and the E-cycle conjecture are all statements about live E's, and the physical data have 19 of them in 20,000 rows and 470 returns in 4.2 million, none with a 4 or a 6.

**The near-wall dynamics of a chaotic row is memoryless.** Trap entry at about 2.7·10⁻³ a tick, E launch at about 1.0·10⁻³ a tick, both flat in time; 3.5% of rows lock into period 2 or 7 within 200 ticks and the rest are captured by the trap, none surviving to tick 8001 in 20,000. The quantity the owner named in CL756, the thing that tends to a limit, is the chaotic population P(no closed set yet at t), which falls geometrically; E's and the "transient" of CL757 are its shadow. Whether P(τ = ∞, no lock) is exactly zero for every finite row is the kit's open RD dichotomy (trap entry or eventual periodicity), and this cohort says it is zero to one part in 20,000 at least.

**Shielding is the damage speed.** A change at cell c reaches column 1 after about c/0.243 ticks, not c. GPT's thresholds are this front. For the passage work the rule is usable both ways: root cells beyond c do not matter before tick c/0.243, and nothing before that tick can be repaired from beyond c.

**What follows, for GPT on the Intel host.** (1) The live E's are the object: a cohort scan that keeps every live E's history (its root and the 35-sample block with its trap-free continuation) gives GPT real histories of the kind its joint-state work needs, with the first-E-preserving cone known to be the low c/0.243 cells. (2) The 4→7 witness search should be seeded by live E's that are followed by A's (the real "E A…" prefixes), not by free roots: the data say a free random root is trapped within about 50 ticks. (3) The conditional hazards 2.7·10⁻³ and 1.0·10⁻³ are the two numbers a mechanism must explain; the trap's 829 windows and the E's opening 3353 are both finite objects, so the entry hazard is computable from the window graph's stationary flow if one exists, which would make the E rate a theorem about a Markov chain rather than a measurement.
