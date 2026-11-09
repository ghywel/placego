# E launches against the gate trap: the trap exclusion carried, the depletion measured, and two chaos tests (Cloud, CL758)

*Cloud, 9 November 2026, at the owner's word (CL758), after GPT's GC2774–GC2782. Status: COMPUTED (the carry, own-code replay) and MEASURED (the cohorts), self-tested, one host. Code: `tests/probes/swarm/sw02/block3/cloud_trap_replay.py`, `cloud_trap_measure.py`, `cloud_trap_measure2.py`, `cloud_shielding_test.py`, `cloud_speed_test.py`, with outputs beside them; the evidence tarball is in the shared store (digest in the ledger).*

## 1. The carry: no E launches from inside the gate trap

The kit's gate trap (`Rule30GateTrap`, data in `GateTrap.lean` at kit `6d2c0579`): 829 width-16 windows of the right half beside the alternating centre at odd times, bit i = column i + 1, closed under the double step for both values of column 17; after entry column 1 shows only gaps 3 and 5 (`gaps_of_entry`). GC2775 computed that the word 3353, the opening of E, has no path inside the trap. Own-code replay (`cloud_trap_replay.py`): all 3,316 transitions stay in the trap (1,647 distinct successor pairs); the 3353 path-set layers are 188, 191, 186, 68, 68, 69, 17, 21, 21, 18, 21, 29, 40, 41, 0, GPT's numbers; the whole E word dies at the same layer, A = 25 at the third sample. Convention control: the white right half placed at my tick 1 enters at tick 295 with window 49415, the kit's `entry_empty` at time 293; the two-tick offset is the kit's white row standing at an even time (its time-1 row is already 100…), so my tick t is the kit's time t − 2. GPT's two roots reproduce exactly in my frame (1045436333: E at 2693, entry 2729; 637749532: entry 19).

**Physical transfer (read, PROVED two-party, computer-assisted).** A real row's odd-time windows are `step2` images of each other with the actual two values of column 17, which the graph admits; the trap is closed; so a row in the trap follows the graph's edges and stays, and cannot realise any word the graph has no path for. Hence E_t ⇒ τ > t (an E launching at odd tick t means the row is outside the trap at t), the factorisation P(E_t) = P(τ > t)·P(E_t | τ > t) is exact counting on a cohort, and E A⁴ E needs no entry at any odd tick ≤ 125, the passage none ≤ 291, because entry is permanent. The prefix-projection item (a passage-consistent path restricted to its first 97 samples is a prefix-consistent path, so the prefix sets contain the passage sets and are nonempty through 62; a free 193-cell tick-1 root and an anchored tick-0 root are different premises) is carried in CL758.

## 2. The measurement: the same cohorts, conditioned on the trap

(PENDING-MEASUREMENT)

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

(PENDING-PREDICTIONS)

## 5. What this says about E, and what follows

(PENDING-DISCUSSION)
