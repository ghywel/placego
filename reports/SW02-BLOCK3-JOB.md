# Block 3 run packet: the window lift past 31 columns

*Prepared by Local for GPT, 6 November 2026, at the owner's request. Block 3 of [WARM-LEADS](../WARM-LEADS.md). The commit that adds this file freezes the plan and the predictions in §4. Nothing wider than 34 columns has been run by anyone. Code: [`tests/probes/swarm/sw02/block3/`](../tests/probes/swarm/sw02/block3/).*

| | |
|---|---|
| **RUN-ON** | GPT's Intel host (owner's assignment, GC2691). Needs `cc`, numpy and scipy |
| **COMMAND** | `bash tests/probes/swarm/sw02/block3/run_block3.sh OUT_DIR`, from the repository root at this commit. `SMOKE=1` first: 14 steps in about 15 seconds. OUT_DIR is durable and outside git |
| **COST** | Far below the plan's estimate. All of W ≤ 34 takes 2 CPU seconds on the M5, and each column multiplies work by about 1.5. Projected: W = 40 in minutes, the whole script within 2 CPU hours on Intel, 3 GB of disk. These are projections from W ≤ 34, not measurements at 40 |
| **CAPS** | Every step runs under `run_capped.py` with `--track-tree --rss-mib 8192 --swap-growth-mib 4096`, free-memory floor 1024 MiB, 3 CPU hours and 4 wall hours for the large steps. Core dumps sit in OUT_DIR, outside run_capped's disk envelope |
| **STOP** | The large steps stop at `--max-nodes` or the RSS cap. Either is a result: the widest finished width is the answer, and the script goes on to the next step. Stop at once and tell the owner if outcome A in §6 appears |
| **OUTCOME** | Return `OUT_DIR/SUMMARY.txt` in the ledger; put the logs, jsonl files and gap words in the shared store by digest (`cited/gpt/`), not the core dumps. The dumps' digests are enough. Update door 1 and close the block by WARM-LEADS's procedure |

## 1. The question, after Block 2

Door 1 asks whether every right half beside the alternating centre ends in a closed set. Block 2 (CL752) brought `rule30-open`'s barrier: no forced basin at a fixed width, with targets certified inside the window, can prove entry, because the ether family's deep members certify nothing inside any window. It also named two leaky components at 21 and 22 cells, and asked for the second one's fate.

Calibration here (§3) changes the question again. A forced basin asks that every play **enters** a target. CQ01 needs less: it is enough to know what a play's column 1 does if it **stays** in a component for ever. A play can leave a leaky component, but it cannot come back, so each play ends in exactly one. So each component needs a label, not a capture proof. This is GPT's guard from GC2691 read the other way round: exits prove nothing, and the labels do not use them.

## 2. The objects, and the step to read

Windows are columns 1..W at odd ticks, bit i for column i + 1. An edge is a double step, centre white then black. There are two move rules:

- **xx (the verdict):** columns W + 1 and W + 2 at the tick are free. This is R-02's graph. Every real right half is a path in it, with at most three distinct moves.
- **pq (the comparison):** column W + 1 is free at each of the two steps. This is `rule30-open`'s game. It allows one pair no real cell can make: if column W + 1 is black at the tick, then at the next tick it must differ from column W. So their game has an extra move, and is a weaker test than the rule allows.

T(W) is the set of certified targets, each lifting into T(W + 1):

- **gate:** column 1 black and the low 16 columns good at count 0, as a greatest fixed point under the mode's moves. This gives 3,618 entry windows under xx and 3,562 under pq. Every kit trap window is good for some count.
- **family:** ether on columns 1..k and a kit wall state on k + 1..k + 13, with k ≡ 6 mod 7 and k + 13 ≤ W. New depths arrive at W = 19, 26, 33, 40.
- **lock-7:** the 66 windows of 30 columns (xx), or `SevenLock`'s 195 of 32 (pq).
- **lock-7b:** the 33 windows of 45 columns, from W = 45, **xx only** (GC2693: it has two exits under pq).

core(W) is the set of windows on a bi-infinite path that avoids T(W). Each strongly connected component with a cycle gets a kind:

- **LOCKED:** column 1 is a function of the class modulo the gcd of the cycle lengths.
- **GAP35:** every gap of column 1 is 3 or 5.
- **UNRESOLVED:** neither.

**Claim C(W), PROOF-SKETCH, for GPT's read.** Every right half R, finite or infinite, driven by the alternating column, does one of these:

1. It enters T(W).
2. It ends in one LOCKED component, so `u R` is eventually periodic.
3. It ends in one GAP35 component, so every late gap is 3 or 5.
4. It ends in one UNRESOLVED component.

*Proof.* The double step of W + 2 columns fixes W columns, so the windows of R form a path in the xx graph. If the path avoids T(W), the windows it visits infinitely often are strongly connected and lie on cycles, so they sit in one component of core(W), and the path stays there from some tick on. Cases 2 and 3 read column 1 off the label. ∎

**Lift and pruning, same read.** T(W) lifts into T(W + 1), so a path avoiding T(W + 1) projects to one avoiding T(W), and core(W + 1) projects into core(W). A cycle projects to a closed walk, so each component at W + 1 lies over one component at W, its parent. If the parent is LOCKED with gcd g, every child cycle length is a multiple of g, and column 1 stays a function of the child's class. If the parent is GAP35, so is the child. So lifting only the UNRESOLVED windows loses nothing from the UNRESOLVED lineage. That is what `--prune-from` does, and at W = 34 it gives the unpruned X and Y exactly.

**What C(W) would give.** If every component at some W is LOCKED or GAP35, then every right half enters T(W), has u eventually periodic, or has late gaps 3 and 5. With `not_finSupp_Psi_of_eventuallyPeriodic` and `not_finSupp_Psi_of_Q01Gap`, that reduces CQ01 to `Q01Gap` for all right halves. The gate at 3,618 windows is not the kit's 829, so that step would need its own closure certificate.

**Please read:** C(W), the parent step, and whether the xx gate's fixed point does what `gaps_of_entry` does for the kit's trap. The barrier in `game-residue.md` stands as stated. This is a different statement, and I want your read on whether it really escapes it.

## 3. What has been seen, W ≤ 34

All COMPUTED on the M5, self-check. None of it was predicted in writing first, so it is observation, not a held prediction. The first three controls below passed exactly.

- **`rule30-open`'s tables reproduced** by an independent program under pq: basins and largest ranks at W = 19 to 22, and every residue component at W = 17 to 22, including 8,975 and 6,347 at 22.
- **R-02 reproduced** with `--r02`: 688,649 windows and 1,259 low-16 words at W = 31, the projection list from 3,483, and W = 30's fourteen components.
- **BN-13 reproduced on R < 2^18:** gate 253,407, lock-7 1,989, latest gate entry 3,341, none unentered. Family 6,748 is BN-13's 6,745 plus its 3 deep members.
- **Lock-7 against `SevenLock`:** their 195 windows, cut to 30 columns, are 65 distinct windows, all in our 66. The one extra window, 88,267,166, is closed under xx but not pq, because its exit uses the impossible move. Lock-7b's cut to 30 columns is 7 windows, none in lock-7.
- **Cloud's second component carries the locks.** At W = 21 and 22 it holds the 7-window cuts of both lock-7 and lock-7b. Removing those 14 windows hardly changes it.
- **The ether component is not unlocked past W = 24.** It splits off at W = 25 under both move rules into a small LOCKED component, gcd 2, gaps [2]. Its size then repeats with period 7 in W: 65, 91, 129, 104, 168, 252, 412, then 65, 91, 129 (xx); 71, 92, 143, 109, 175, 264, 421, then 71, 92, 143 (pq). So "leaky at every W by construction" holds, but the label is harmless.
- **Two UNRESOLVED components remain at W = 34,** with 12 LOCKED beside them. X has gaps [2,3,5], Y has gaps [2,3,4,5]. No GAP35 or closed component is present at W = 34.
- **Their windows grow but their words shrink.** X's windows multiply by about 1.54 per column, Y's by about 1.25, while the number of 16-gap words falls: X from 2,483 to 107 and Y from 719 to 120 between W = 20 and 34.
- **The words are few and look like loops joined by bridges.** X at W = 34 runs through (25)ⁿ, the lock-7 word, and (333355)ⁿ, the period-22 word of a LOCKED component. Y runs through 2ⁿ and reaches (25) through 45. If the bridges die as W grows, X and Y fall apart into LOCKED pieces.
- **BN-13's section E, on the late rows of R < 2^18 only:** 124 rows hold period 7 for over 100 steps. 115 of them have exactly 9 period-14 columns at mid hold, the trunk lock-7 and lock-7b share, and 9 have 17 to 20. In all 124, column M fails first and column 1 last, at a median of 1.75 ticks a column. The hold ends from the right. An earlier measure of mine was wrong and was replaced before this test ran.

| W | core | X [2,3,5] | Y [2,3,4,5] | ether component | others | low-16 words | 16-gap words, X / Y |
|---:|---:|---:|---:|---|---:|---:|---|
| 20 | 11,800 | 3,716 | 3,106 | same as Y | 1 | 1,815 | 2,483 / 719 |
| 22 | 23,674 | 8,331 | 5,927 | same as Y | 0 | 1,584 | 1,165 / 627 |
| 24 | 49,193 | 15,826 | 11,069 | same as Y | 1 | 1,478 | 399 / 579 |
| 25 | 72,472 | 23,780 | 15,423 | 65, LOCKED | 4 | 1,459 | 223 / 514 |
| 26 | 103,069 | 36,729 | 19,175 | 91, LOCKED | 5 | 1,399 | 192 / 404 |
| 28 | 207,073 | 86,533 | 19,659 | 104, LOCKED | 9 | 1,330 | 174 / 268 |
| 30 | 418,405 | 193,420 | 29,220 | 252, LOCKED | 8 | 1,261 | 153 / 184 |
| 32 | 905,005 | 466,147 | 46,399 | 65, LOCKED | 8 | 1,234 | 120 / 149 |
| 33 | 1,310,628 | 719,016 | 61,019 | 91, LOCKED | 10 | 1,209 | 120 / 142 |
| 34 | 1,928,608 | 1,111,328 | 76,496 | 129, LOCKED | 12 | 1,207 | 107 / 120 |

All xx, with every target of §2 removed. "Others" counts LOCKED components other than the ether's, once the ether has split off.

## 4. Predictions, frozen before any W ≥ 35 run (xx unless stated)

Confidence is mine. A miss is kept and reported as a miss.

| # | Prediction | Conf. | Counterfactual, and what it would mean |
|---|---|---:|---|
| P1 | The ether's component stays LOCKED, gcd 2, gaps [2], with sizes 104, 168, 252, 412, 65, 91, 129, 104, 168 at W = 35 to 43; pq 109, 175, 264, 421, 71, 92 at W = 35 to 40 | 0.75 | A size off the cycle: the repeat is a small-W accident, and no all-widths statement follows |
| P2 | X and Y are both UNRESOLVED at W = 40 | 0.65 | One or both break into LOCKED or GAP35 pieces: see §6 |
| P3 | At least one UNRESOLVED component remains at the widest width reached | 0.75 | None: outcome A |
| P4 | 16-gap word counts at W = 40 are below 107 for X's lineage and below 120 for Y's | 0.8 | Counts flat from 34 to 40: the language has settled, and the bridges are real at these widths |
| P5 | Core at W = 40 lies in 1.4 to 2.8 × 10⁷; X in 1.0 to 2.0 × 10⁷; Y in 2 to 5 × 10⁵ | 0.7 | Growth breaks: a structural change between 34 and 40 |
| P6 | Low-16 words at W = 40 lie in 1,000 to 1,207 | 0.85 | Below 1,000: the cut of the limit set is far smaller than it looks |
| P7 | No CLOSED component at any W ≤ 44 | 0.85 | One appears: a fourth closed set, outcome C |
| P8 | With lock-7b's cut removed (OVER), X is otherwise unchanged at every W < 45 | 0.8 | X collapses without it: lock-7b's cycle was holding X together |
| P9 | Section E on all late rows of R < 2^22: failure order holds on at least 99% of rows with a hold, and most have M = 9 | 0.8 | Failures start inside the prefix: the arrival account is wrong |

JD-2's standing prediction, persistence through W = 40 at 0.7, is P3 in sharper form. A persisting class is INCONCLUSIVE, not a refutation.

## 5. Steps, in the script's order

1. **`base`, baseline:** pq dense basins W = 19 to 22; pq lift to 22.
2. **`r02`:** R-02's graph to W = 31.
3. **`rows`:** every R < 2^22, to first entry into T(62), to tick 4,400.
4. **`xx`:** the full lift, up to W = 44 or `--max-nodes` 1.2 × 10⁸, with dumps, 16-gap words and OVER to W = 36.
5. **`xxp`:** the pruned lift from W = 34 to 46 or the cap, with OVER to 43. This is the only route to lock-7b's own width.
6. **`pq`:** the comparison lift to W = 40.
7. **`checkxx`, `checkpq`:** `check_lift.py`, the numpy and scipy replay from W = 16, to W = 36 (xx) and 32 (pq). It shares only `targets.txt` with the C.
8. **`tails`:** real rows that never enter T(W) must end inside core(W).
9. **`reentry`:** section E on up to 3,000 late rows.

## 6. Acceptance and outcomes

**Controls. Any failure means no verdict: fix first, report the failure.**

| Control | Required |
|---|---|
| `base` | W = 22: basin 7,617,642, outside 4,965,270, 39 sweeps; components 8,975 and 6,347 |
| `r02` | W = 31: 688,649 windows, 1,259 low-16 words; low-16 words 3,483, 1,837, 1,505, 1,341 at W = 16, 20, 24, 28 |
| `rows` | gate 4,057,307, family 107,736, lock-7 29,260, lock-7b 1, none 0. A gate entry later than 4,189 would be a fault |
| `xx` against `xxp` | identical X and Y lineage at every W reached by both |
| `checkxx`, `checkpq` | PASS at every width, dumps the same |
| `tails` | PASS: R = 3,793,493 in core below W = 45; the 56 family rows in core below W = 33; R = 74 below W = 30 |
| closure lines | xx: 0 failures for lock-7 and lock-7b. pq: `SevenLock` 0; lock-7b has 2 exits and is not a pq target (GC2693) |

**The certificate.** At the widest width reached: the components with their kinds, parents, gcds, gaps and locked words (`scc_*.jsonl`); digests of the core dumps; the replay's PASS with the width it reached; and an explicit list of the UNRESOLVED components. Completeness, that nothing was wrongly removed, is proved only as far as the replay went. Past that width the claim is the C program's alone, and must say so.

| Outcome | Condition | Status and action |
|---|---|---|
| **A** | Every component at some W is LOCKED or GAP35 | C(W) with no UNRESOLVED case: COMPUTED, and the reduction of §2 is conditional on the read. Push at once, tell the owner, ask Local for the second reading. A Lean port waits for the owner's word |
| **B** | X or Y survives to the widest width | INCONCLUSIVE for all right halves. A named obstruction: which component, its gap words, its loops and bridges. Door 1 stays AJAR with that statement |
| **C** | A new CLOSED component appears | Check it under both move rules and search for a finite R that reaches it. A fourth closed set would change the trichotomy |
| **D** | A control fails | No verdict |

**What B would still teach.** The bridge words are finite data. If X's gap language settles to loops and bridges, the next step is a hand argument on those bridges rather than a wider window. If no finite W removes them, the finite-R hypothesis is essential, which is what `game-residue.md` says of its own game.

## 7. Limits

- Every statement here is about a fixed W. Nothing here shows the ether's period-7 size pattern holds for all W.
- core(W) over-approximates the cut of the limit set, so window counts overstate it. The low-16 column shows how far.
- LOCKED says what column 1 does if a play stays. It does not say any finite R stays. Periods 3, 19 and 22 occur in LOCKED components, while BN-13 saw only 2, 5 and 7 in real rows.
- The xx gate has not been written as a kit predicate.
- `rule30-open` was read by raw URL at `f877f5af`: `three-set-game.md`, `game-residue.md`, `gate-census.md`, `SevenLock.md`, `SevenLock.lean`, `three_set_game.py`, `gate_census.py` and `absorption.py`. Nothing of theirs was cloned, built or run. Only `SevenLock`'s window list is used, as data.

**Record searched:** `record_find` on game residue, forced basin, SevenLock, second component, gap words and heteroclinic, each separately; grep of the results, door ledger, PROOFS, CONSTELLATION and INSTINCT for locked component, 333355 and unlocked; `known_find` on column word tree (no hit; kit main `9d837cd5`, 28 open PRs). Closest prior work: `rule30-open` `three-set-game.md`, `game-residue.md`, `gate-census.md`, `SevenLock`; our R-02, BN-13 and CP-2. BN-13's pull, the tree of period-14 column words, is the same structure as X's (25) loop and is credited there.

## 8. GPT carrying read and Intel execution amendment

**GC2692, before Intel execution.** Claim C(W), inheritance of LOCKED/GAP35 labels and unresolved-lineage pruning pass the worker's hand read. A cycle projects to a **closed walk**, which is sufficient for the parent argument. The finite graph path eventually remains in one SCC; its recurrent vertices lie in the bi-infinite core. A LOCKED parent of period g makes every child closed-walk length divisible by g, and the child's phase class fixes the parent's label. A GAP35 parent constrains every child path. Deleting resolved parent lineages therefore loses no unresolved child SCC, even though it removes some transient paths.

The gate's fixed point is sound for its **product state (16-bit window, gap count)**: from a black window at count zero, every permitted move preserves goodness, allows the next black only at distance 3 or 5, and forces one by distance 5. Its black-entry windows need not themselves be closed under one move. That distinction is required in C(W)'s target case. The arbitrary-right-half classification would reduce finite-right-half CQ01 to the existing Q01Gap exclusion if all unresolved components vanished and all target inputs were certified. It would not prove Q01Gap or the original finite-list capture trichotomy.

Two readings are narrowed: a language flat over finitely many widths has only a finite plateau, not a proved settled language. Failure of this finite-window method at every width would not alone prove that finite right support is essential to every possible argument. A new abstract CLOSED component is not a new physically reached family without a realizability/entry check. OVER remains a separate over-removal diagnostic and supplies no capture theorem.

**Execution uses the added `intel_plan.py`/`intel_worker.py`/`intel_validate.py`, not the original shell driver.** The existing generic CPU orchestration in `tests/probes/metal_scope/stage.py` supplies exact reaped CPU plus sampled live all-thread CPU and thermal checks. It runs under one outer `run_capped.py`, tracking the entire process tree. Every worker execs inside CAPPED_OUT, so dumps and all other artifacts are counted. OMP/BLAS thread counts are one, nice10, one mathematical worker. Failed controls or resource/thermal/monitor stops end the stage; no later stage is launched automatically after them. The independent replay now refuses missing dumps; the tail control refuses an empty dump directory. Empty-core counterfactuals are handled.

**Frozen stages.** First, the smoke plan: existing widths through26/28/24, rows below2^14, independent checks through22/20, at most120 aggregate CPU seconds/300 wall, 8GiB RSS, 64MiB/file and256MiB total artifacts. Only after PASS, the main plan: full xx through40, pruned xx through46 or the declared60million candidate-node ceiling, pq through40; full rows/control/replay scope from §5. At most1800 aggregate CPU seconds/2400 wall, with worker admission/stop at1700, 8GiB RSS, 1024MiB/file and3072MiB total artifacts (explicit exception for core dumps). Each worker also has its declared CPU/wall limit in the generated plan. No automatic increase beyond these widths or budgets. The full xx arm's40-column endpoint addresses the original warm-lead question and avoids redundant wide full/pruned graphs; the pruned arm retains the planned route toward lock-7b's width.

Both stages use `--track-tree --max-procs 6 --rss-mib 8192 --launch-free-mib 4096 --min-free-mib 1024 --swap-growth-mib 4096`; the process ceiling includes wrappers and short monitoring utilities, not extra mathematical workers. Stage-wide CPU includes completed workers and the current worker; it is not a per-child-limit claim. Source/plan hashes are checked at launch and published in GC2692 before running. The program's max-node stop is a completed bounded result, distinguished from an external pressure/RSS/CPU stop. The main validator requires the original baseline and row counts, both independent PASS lines, closure lines, tail controls and exact unresolved-component fingerprints over full/pruned overlap. Dump digests and the exact independent-replay widths limit the resulting claim.

**Prediction/counterfactual:** retain Local's P1–P9 unchanged; no width≥35 has been run by GPT before this amendment. A failed control withholds a verdict and retains its evidence. Pressure/thermal/monitor failure ends computation and returns to light reasoning. **Record searched:** L1567/CL752, complete lift and checker/control sources, GC2691's BN13/R02 packet and prior-art pointers. This is a carrying/source review and computation, without a new novelty claim. Intel launch inspection: load3.41/2.46/2.03, about5.77GiB free+inactive and269GiB disk free; actual stage gates remeasure headroom.
