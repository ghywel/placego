#!/usr/bin/env python3
"""SW-02 builder: Wave 4 bench. Most bench seeds were answered inside Wave 2 (BN-01 AM-4; BN-03 AM-2; BN-04 XP-1, LN-02; BN-05 CT-3;
BN-06 XP-4; BN-07 AM-5; BN-08 BR-6; BN-09 XP-5; BN-10 BR-3). What remains: BN-02, BN-11, and two tests the attack wave asked for."""
import json
from build_common import *

COMMONB = """
**Rules for this test.** Write your prediction and counterfactual in `prereg.txt` in your folder before you run anything; the freeze below already fixes the main one. Include the controls named. Run through the queue with `--lane bench`, one job at a time, with `--cpu` and `--wall` as stated. Keep every output, and report failures and refuted predictions as they are. Put your account in the manifest's `report` field; other files by Bash heredoc in your folder.
"""

BN11 = """# SW-02 task {{ID}}: bench, the rate off A0

**Test (design BN-11, Cloud).** Run a census of random left-finite rows (P = 1, meaning only the first cell is shared with the seed) through the seed path's two forks, 53,207 and 58,286, cleared by about tick 80,000, and record the branch at each. The instrument is `{{REC}}/tests/probes/wolfram/prefix_race.py` with its output format; copy what you need into your folder. Also record, as R-04 asked, for each row: the strip phase of the edge's last black before each fork, and whether wheel j - 1 is still in error there (the seed decides fork 53,207 at phase 11 with its parent in error and an edge jump of 3).

**Frozen prediction (P15).** At most 5% of 300 rows leave A0 at either fork. A higher rate is the finding, and the switching rows are kept for the branch law. Prior data: 0 of 12 free rows at P = 1 in `prefix_race.out`; §8.31's 0 of 59 on shorter rows.

**Controls.** Positive: a chink at a fork's child switches the branch (8 of 8, CL748 addendum 2). Negative: an early chink far below the fork does not (64 of 64, wheels up to 5,000, ticks 1,000 to 1,007). Use rows from `chink.py`'s setup.

Budget: 1,500 CPU seconds in all through the queue, at most 500 per job; about 50 tool calls. If 300 rows do not fit, run what fits and say so.
""" + COMMONB

BN12 = """# SW-02 task {{ID}}: bench, reset chains on the sixteen strips

**Test (requested by AM-3).** AM-3's report at `{{DATA}}/out/AM-3/report.txt` defines reset chains and measures them on the kit's four strips through wheel 87,866: chain minima 7,997, 7,979, 7,929, 7,911, largest reset gap 84, mean gap about 10. Its conditional amplification rests on the hypothesis H(rho): a reset chain of at least rho t levels at every late tick. Measure the same quantities on the sixteen strips through wheel 894,235 (the tree of atlas §21.10; find how `chink_tree.py` and the atlas build them; R-04 and CL748 to CL750 have the data path), and on the seed's own rows at a few late ticks.

**Frozen prediction.** Largest reset gap stays below 200 and wheels per chain level stay within 10% of 11 through 894,235. **Counterfactual:** a gap that grows with the wheel index would bear against H(rho).

**Controls.** Reproduce AM-3's numbers at 87,866 first (the kit's literals, `final.py`, `band.py` in its folder).

Budget: 900 CPU seconds, at most 450 per job; about 50 tool calls.
""" + COMMONB

BN02 = """# SW-02 task {{ID}}: bench, matrix interpretations

**Test (design BN-02; requested by BR-2, LN-06).** §8.61 closed matrix interpretations by argument, GPT's G5 objected, and they were never run. L-6 found that an arctic proof implies a linear deadline, and LN-06 shut one-shot arctic and match-bound proofs in its class, leaving relative arctic open. Run the open case. Take LN-06's system `R_Q.srs` in `{{DATA}}/out/LN-06/` (read its report for what the rules mean) and search by SAT or SMT (python-sat or z3 in Python; both are installed) for: (a) relative termination: the three tick rules strict, the rest weak, with arctic matrices; (b) the same with natural matrices. Dimensions 1 to 3, then 4 if time allows, entries of at most 3 bits. Also run L-6's recommended target, the Q01Gap restriction, if it can be encoded in the same system.

**Frozen prediction.** The control is proved and the target is not, in every box. **Counterfactual:** an interpretation for the target would be a checkable termination proof: replay it exactly before anything else, and assume first that the encoding is wrong.

**Controls.** Positive: the same encoder proves a sibling statement known to be true, such as the period-1 column or rule 90's check, or a known terminating string rewriting system of similar shape. Negative: a known non-terminating system must return no interpretation. A failed search in a box is INCONCLUSIVE, not a barrier: report the box.

Budget: 1,200 CPU seconds, at most 400 per job; about 60 tool calls.
""" + COMMONB

BNL = """# SW-02 task {{ID}}: bench, a Lean check of a refutation

**Test.** Agent PE-1 claims that the kit's open statement `AbsorptionT t001` is false, with an explicit certificate, and screener SC-4 replayed it from the kit's packed table. Lean should settle it. Read `{{DATA}}/out/PE-1/report.txt` section 3, `t015_ptrap.txt`, `verify15.py`, and `{{KIT}}/lean/Ruliology/CellularAutomata/Rule30EtherThreeTrap.lean` (`PTrap`, `PTrap.check`, `PTrap.invariant`, `EncF`, `AbsorptionT`, `t001`).

Write a core-Lean module in your folder, importing the kit's module, that defines the table `t015 : PTrap`, proves its check by `decide` as the kit does for `t001`, and proves `¬ AbsorptionT t001`, with the right half `x0 = 266113541000008`. Compile it with:

    PATH=$HOME/.elan/bin:$PATH LEAN_PATH={{KITLIB}} lean {{OUT}}/File.lean

run through the queue with `--lane bench --cpu 600 --wall 900 --rss-mib 8192 --max-procs 4`. This is the one Lean task in the swarm; run nothing else in Lean. Print the axioms with `#print axioms`: standard axioms only.

**Frozen prediction.** It compiles. **Counterfactual:** a failed check means an error in the table or in the reading of `EncF`. Say exactly which.

**Controls.** Positive: `t001`'s own check at the pin. Negative: the same disjointness argument run with `t001` against itself must fail.

If the kit's compiled library lacks a module or differs from the pin, say so. Budget: 900 CPU seconds in all, about 70 tool calls.
""" + COMMONB


BN13 = """# SW-02 task {{ID}}: bench, the right-half census

**Test (requested by BR-5, CP-2, R-02, R-08).** The survey and attack wave found that every finite right half R tested enters the 829-window gate trap or has u R eventually periodic, with periods 2, 5, 7 and 14 seen, and closed locks inside and outside the trap. Whether this dichotomy (TrapOrPeriodic) holds for every finite R is open. Extend the census: every R < 2^22, and at least 2,000 random R at each width 64, 128, 256, 512, driven by the alternating column, to a horizon of at least 30,000 ticks. Classify each R by entry into the trap, by eventual period, and by which closed lock it enters (`{{DATA}}/out/R-02/`, `{{DATA}}/out/BR-5/`, `{{DATA}}/out/CP-2/`, `{{DATA}}/out/PE-1/` hold scripts and tables; write C if Python is too slow). Report the latest entry times, any R in no class by the horizon, and the distribution of absorption times.

**Frozen prediction.** No R outside the known classes; the latest entry time grows slowly with width. **Counterfactual:** a row in no class by the horizon is the finding: keep it and follow it longer.

**Controls.** Reproduce R-08's counts for R < 2^11 first: 1,971 enter the trap by tick 2,400 and 77 do not, of which 52 have period 2 and 25 period 7.

Budget: 1,500 CPU seconds, at most 500 per job; about 60 tool calls.
""" + COMMONB

BN14 = """# SW-02 task {{ID}}: bench, the trap catalogue

**Test (requested by PE-1).** PE-1's `chain.c` found the second trap for 001 (period 15) and period-14 and period-10 traps for the alternating driver, but stopped at period 24 for 011 and 21 for 001 at full depth. Finish the catalogue: 001 at m = 30, 36, 39, 42, 45, 48; 011 at m = 27, 30, 33, 36; the alternating word at every even m up to 40; B = 10, all depths. C3w(011) is the bottleneck for period 3: a trap for 011 would be the first. Copy `{{DATA}}/out/PE-1/chain.c` to your folder and read PE-1's report for its use.

**Frozen prediction.** More traps for 001 and the alternating word; none for 011. **Counterfactual:** a trap for 011 would change the status of C3w(011).

**Controls.** m = 21, B = 9 returns exactly t001 at depth 38; m = 8 returns the kit's period-8 wall; m = 3 returns nothing (`no_wall`).

Budget: 1,500 CPU seconds, at most 500 per job; about 50 tool calls.
""" + COMMONB

BN15 = """# SW-02 task {{ID}}: bench, gate-past closing

**Test (requested by LN-07).** `Closing(n)` for every n is PR52's hypothesis, and LN-07 verified it through past length 19 with cutoff about 29.4 n. Extend it to n = 20 to 26 with `{{DATA}}/out/LN-07/j14.py`'s method in C, printing M(n), the node count and the worst future. Read LN-07's report first.

**Frozen prediction.** Closing holds through n = 26 and the cutoff stays within 10% of 29.4 n. **Counterfactual:** a failure would refute the hypothesis of PR52's reduction.

**Controls.** Reproduce n <= 19 first.

Budget: 900 CPU seconds, at most 450 per job; about 50 tool calls.
""" + COMMONB

BN16 = """# SW-02 task {{ID}}: bench, one sequence further

**Test (requested by CP-1).** Extend CP-1's box: u(empty) and Psi(empty) to s = 2,000,000 and depth 2,000,000, in C with a word-packed row if needed. Report the minimal period of the tails, the gap census, the counts of 3,3 and 3,5,5,3, the white-run histogram of Psi(empty), and the longest white run against the coin's prediction. CP-1's scripts are in `{{DATA}}/out/CP-1/`.

**Frozen prediction.** No eventual period; exactly one 3,3; no 3,5,5,3; longest white run within 3 of log2 of the depth. **Counterfactual:** an eventual period of u(empty) would give CQ01Empty by the kit's absorption route: replay it at once and assume first that it is an artefact.

**Controls.** Reproduce CP-1's numbers at 150,000 first.

Budget: 1,500 CPU seconds, at most 500 per job; about 50 tool calls.
""" + COMMONB

def main():
    lib = os.path.join(DATA, "kit-build", "lean", ".lake", "build", "lib", "lean")
    write_task("BN-11", BN11, REC_FULL)
    write_task("BN-12", BN12, REC_FULL)
    write_task("BN-02", BN02, REC_FULL)
    write_task("BN-L1", BNL.replace("{{KITLIB}}", lib), REC_FULL)
    write_task("BN-13", BN13, REC_FULL)
    write_task("BN-14", BN14, REC_FULL)
    write_task("BN-15", BN15, REC_FULL)
    write_task("BN-16", BN16, REC_FULL)
    b = {"BN-L1": 900, "BN-12": 900, "BN-11": 1500, "BN-13": 1500, "BN-14": 1500, "BN-02": 1200, "BN-15": 900, "BN-16": 1500}
    p = os.path.join(DATA, "queue", "budgets.json")
    cur = json.load(open(p)) if os.path.exists(p) else {}
    cur.update(b)
    json.dump(cur, open(p, "w"))
    write_batch("w4", [{"id": i, "effort": "high"} for i in b], 2)
    print("ok")

if __name__ == "__main__":
    main()
