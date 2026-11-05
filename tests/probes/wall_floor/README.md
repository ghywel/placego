# The reset word, floors and the cloud (Local, L1532–L1533)

Probes for [genealogy §63.7](../../../reports/rule30-genealogy.md). All are short runs. Compile the C files with `cc -O2`.

| File | What it does |
|---|---|
| `wall_eventual.c` | E(w) for every width: windows that survive arbitrarily many settled ticks, and the strongly connected parts of their graph. Output `wall_eventual92.out`. `./wall_eventual 92 45 52 60` also writes `E45.txt`, `E52.txt`, `E60.txt`, which the Python below reads. |
| `wall_floors.c` | Exact time-periodic solutions below a letter word, searched for a floor of the reset word's shape. Outputs `wall_floors_small.out` (periods up to 9, with the last relation) and `wall_floors_big.out` (primitive words of periods 10 to 16, without it). |
| `wall_closure.c` | Closure of a window under all four lower states, for windows up to 190 cells. |
| `wall_member.c` | Real rows against E(w): which class they enter, when, and whether they leave. Outputs `wall_member45.out`, `wall_member52.out`. |
| `wall_try.c` | A word at the top of a row, random cells below, until the letters leave their cycle. Outputs `wall_try_aab136.out`, `wall_try_quiet.out`. |
| `lockperiodic.py`, `dumpleaves.py`, `aab136.py` | The period-3 search that found the `AAB` lock; output `lockperiodic_p3.out`, `aab136.out`. |
| `parts.py`, `partcheck.py`, `lockin.py`, `cloudletters.py` | The parts of E(w), their letters on every edge, where the `AAB` lock's top cells sit, and the letters on the cloud. |
| `markov.py`, `killrate.py`, `killed.py` | The cloud as a chain with fair lower states: letter statistics, the rate at which `AAB` breaks (`killrate.py TICKS WIDTH ...`; `killrate.out` is from its first form, with 900 ticks fixed), and the windows that can hold `AAB`. |
| `decide.py`, `shield.py`, `rechk29.py` | The one free choice; the state sets up a window; the recheck of L1531's width-29 line. |
| `obdd.py`, `langset.py`, `reachlib.py`, `reach3.py` | Sets of rows as decision diagrams; the letter language by sets; forced letters by width. |
| `clos.py`, `eventual.py`, `locklib.py` | Window closure and E(w) in Python, the first versions. |
| `gen_lock_lean.py`, `gen_cloud_lean.py`, `cloud_*.txt` | Generators of `TwoPairsWallLockAAB.lean` and `TwoPairsWallCloud.lean`; each writes to `lean/` beside it, so run them from a folder that has one. |
| `lean_axioms.out` | The axioms of the four Lean modules. `TwoPairsWallCloud` built in 57 s with 1.5 GB (M5, 8 GiB cap); a single check over all 798 windows passed that cap, so the check is split into chunks of 40. |
