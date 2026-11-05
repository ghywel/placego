# The reset word, floors and the cloud (Local, L1532–L1533)

Probes for [genealogy §63.7](../../../reports/rule30-genealogy.md). All are short runs. Compile the C files with `cc -O2`.

| File | What it does |
|---|---|
| `wall_eventual.c` | E(w) for every width: windows that survive arbitrarily many settled ticks, and the strongly connected parts of their graph. Output `wall_eventual92.out`. `./wall_eventual 92 45 52 60` also writes `E45.txt`, `E52.txt`, `E60.txt`, which the Python below reads. |
| `wall_floors.c` | Exact time-periodic solutions below a letter word, searched for a floor of the reset word's shape. Outputs `wall_floors_small.out` (periods up to 9, with the last relation) and `wall_floors_big.out` (primitive words of periods 10 to 16, without it). |
| `wall_closure.c` | Closure of a window under all four lower states, for windows up to 190 cells. |
| `wall_member.c` | Real rows against E(w): which class they enter, when, and whether they leave. Outputs `wall_member45.out`, `wall_member52.out`. |
| `wall_try.c` | A word at the top of a row, random cells below, until the letters leave their cycle. Outputs `wall_try_aab136.out`, `wall_try_quiet.out`. |
| `lockperiodic.py`, `dumpleaves.py`, `aab136.py`, `break135.py` | The period-3 search that found the `AAB` lock, its six windows, and the path that leaves at width 135; outputs `lockperiodic_p3.out`, `aab136.out`, `break135.out`. |
| `parts.py`, `partcheck.py`, `lockin.py`, `cloudletters.py` | The parts of E(w), their letters on every edge, where the `AAB` lock's top cells sit, and the letters on the cloud. |
| `markov.py`, `killrate.py`, `killed.py` | The cloud as a chain with fair lower states: letter statistics, the rate at which `AAB` breaks (`killrate.py TICKS WIDTH ...`; `killrate.out` is from its first form, with 900 ticks fixed), and the windows that can hold `AAB`. |
| `decide.py`, `shield.py`, `rechk29.py` | The one free choice; the state sets up a window; the recheck of L1531's width-29 line. |
| `obdd.py`, `langset.py`, `reachlib.py`, `reach3.py` | Sets of rows as decision diagrams; the letter language by sets; forced letters by width. |
| `clos.py`, `eventual.py`, `locklib.py` | Window closure and E(w) in Python, the first versions. |
| `gen_lock_lean.py`, `gen_cloud_lean.py`, `cloud_*.txt` | Generators of `TwoPairsWallLockAAB.lean` and `TwoPairsWallCloud.lean`; each writes to `lean/` beside it, so run them from a folder that has one. |
| `lean_axioms.out` | The axioms of the four Lean modules. `TwoPairsWallCloud` built in 57 s with 1.5 GB (M5, 8 GiB cap); a single check over all 798 windows passed that cap, so the check is split into chunks of 40. |

## Added in L1535

| File | What it does |
|---|---|
| `wall_births.c` | E(w) with each part's parent: every cycle that splits off the cloud. Output `wall_births92.out`. |
| `wall_lockscan.c`, `wall_holds.c`, `wall_closure2.c` | Closure with no assumption on shape, on periodic trees, on one word, or for wide windows. Outputs `scans.out`, `lockscan_*.out`. |
| `deep6.py`, `deepread.py`, `lock175.py`, `phases175.py`, `lock6in.py`, `break_at.py`, `entrances.py`, `scar.py` | The deep period-6 words, the third lock's phases, where it sits in E(w), and the quotient of the three locks. Outputs `lock175.out`, `phases175.out`, `lock6in.out`, `lock136in.out`, `scar.out`. |
| `gen_lock6_lean.py` | Generator of `TwoPairsWallLockSix.lean`. |
| `wall_chain.c`, `wall_chainlags.c`, `wall_spec.c`, `wall_quietwins.c`, `wall_capture.c`, `wall_hazard.c`, `wall_lags.c` | The window chain: the top W cells with fair lower states, at constant cost a tick. Long-time fates, lag rates by offset, the lag spectrum, quiet windows, capture, and the break rate by depth of agreement with the third lock. Outputs `chain_long.out`, `chainlags.out`, `wall_spec.out`, `quietwins36.out`, `quietwins60.out`, `capture1.out`, `hazard.out`, `wall_lags.out`. `wall_lags.c` uses real rows, not the chain. |

## Added in L1537

| File | What it does |
|---|---|
| `wall_past.c` | Exhaustive search on rows for a settled past before a step into a window set. "dead" is exact; "capped" says nothing. Output `wall_past.out`; inputs `lock45.txt`, `lock136.txt`, `lock175.txt`, `quiet60.txt`. |
| `backset.py` | The same question with whole sets of pasts as diagrams. Too slow even at width 52; kept as a failed attempt. |

## Added in L1539

| File | What it does |
|---|---|
| `handcheck.py` | Checks the counts 2·4^n and the column formulas against both floored locks. |
| `wall_upfloors.c`, `wall_upexact.c` | Every floor word, by following its columns up; the second adds cycle detection. Outputs `upfloors1.out`, `upfloors19.out`, `upfloors23.out`, `upexact.out`. |
| `sat_past.py`, `sat_break.py`, `sat_lock6.py` | The entrance question by SAT on actual rows (kissat). Outputs `sat_bounds.out`, `sat_control.out`, `sat_break.out`. `sat_break.py` overwrites its witness file, so run it for S = 56, L = 110 last. |
| `sat_edges.py`, `edgegraph.py`, `wall_edges.c` | Every edge of the free graph on actual rows, and the graph that remains. Output `edges_summary.out`. |
| `verify_witness.py`, `witness_break_175_56.json` | Checks the witness row by plain ticks. Outputs `verify_witness.out`, `entrytick.out`. Dots past tick 83 in its line mean the known cells ran out. |

## Added in L1541

| File | What it does |
|---|---|
| `wall_entry.c` | Entry time of a closed set from inside it: `./wall_entry SETFILE N NMAX SEED`. Outputs `entry45.out`, `entry136.out`, `entry175.out`. `wall_smc.c` is the first form, which keeps rows still inside the set and loses them to rows that left. |
| `wall_chain2.c` | The chain from a random letter, the law `wall_entry` uses. Output `direct_ab.out`. |
| `wall_split.c`, `wall_splitb.c` | Splitting on the chain, on the six-tick minimum and on single-tick agreement. Output `split_big.out`. Kept as a failure: see genealogy §64.5a. |
| `witness_track.py`, `arrive_track.py` | Agreement with the third lock along the witness and along chain arrivals at 145. |
| `sat_entry136.out` | Entry to the full 136-cell lock with L settled rows. |

## Added in L1543

| File | What it does |
|---|---|
| `climb.py` | The climb from floor to wall under the rise rule, from the strips alone. Output `climb.out`. |
| `wall_arrive.c` | Arrival rows and rises on random rows, with the rule checked at every step. Output `arrive_all.out`. For the third lock run with `KEEP=1`, because its first forward image differs only in cells that are not strip cells. |
| `tailcheck.py` | The estimates of `wall_entry` against the formula with sampled arrivals. Reads `run_entry2/out.txt` and `run_entry3/out.txt`, saved here as `entry175.out` and `entry136.out`. Output `tailcheck.out`. |
| `ab_exit.py` | The longest entries to the `AB` lock, row by row, by SAT. Output `ab_exit.out`. |

## Added in L1545

| File | What it does |
|---|---|
| `wall_dev.c` | The deviation automaton: `./wall_dev CYCFILE SETFILE M fair N SEED T` or `./wall_dev CYCFILE SETFILE M free ROUNDS`. Outputs `dev45.out`, `dev136.out`, `dev175.out`, `dev45_free.out`. Inputs `cyc45.txt`, `cyc136.txt`, `cyc175.txt`. |
| `wall_entry_id2.c` | `wall_entry` with an ancestor count from tick `IDN`. Outputs `lineage136.out`, `lineage175.out`. **Read these before trusting `entry136.out` or `entry175.out` past m = 34 and m = 45.** |
| `fairzone.py` | Checks that cells at offset K − 3s are fair. Output `fairzone.out`. |

## Added in L1547

| File | What it does |
|---|---|
| `wall_capture2.c` | The direct run: `./wall_capture2 256 SECONDS SEED lock175.txt ref6.txt`. Saves any row that enters or goes quiet. Output of the four processes, seeds 301 to 304: `capture_run.out`. |
| `cyclecheck.py`, `branches6.py` | Where exact periodic solutions leave the lock strips. Outputs `cyclecheck.out`, `branches6.out`. |

