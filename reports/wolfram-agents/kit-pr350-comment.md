<!-- WITHDRAWN, 17 November 2026 (L1677): the owner decided not to post this ("it doesn't add much value to the kit"). Kept as a record only. -->

<!-- DRAFT of a comment for kit PR #350 (https://github.com/WolframInstitute/Rule30PrizeKit/pull/350), written at the owner's word "Yes, draft it" (L1676, 16 November 2026). NOT POSTED: posting waits for the owner's word. No byline, by the standing rule for PR comments. Prose paragraphs are unwrapped for GitHub. Every number is from runs 15 and 16 (L1675, L1676). -->

Thanks for `Rule30ZeroCoastBridge`. Stating `Q01Gap` as `MassDiverges` gave us a table to compute, so we ran the stratum search further. Three things came out that may be useful to you.

**1. Your rung is sharp.** An exhaustive search over accepted traces reproduces `c37Roots` exactly: those eight seeds are the only survivors to 102 of popcount at most 38. Both horizons are the least possible. `119167669152357754337405731158` has popcount 37 and survives to 101, so `NoMass 37 101` fails; and your y* survives to 110, so `NoMass 38 110` fails.

**2. The ladder continues to popcount 90** (computed, not kernel-checked). `SurvivesTo y H` reads only bits 0 to H − 1 of `y`, so `NoMass M H` holds exactly when M is below the least popcount of an accepted H-bit prefix. A depth-first search over accepted traces, cut off when the popcount passes M, computes that exactly. The least H with `NoMass M H`:

| M | 37 | 38 | 39 | 40 | 45 | 50 | 60 | 70 | 80 | 90 |
|---|---|---|---|---|---|---|---|---|---|---|
| H | 102 | 111 | 112 | 116 | 128 | 148 | 182 | 212 | 244 | 278 |

**3. Every rung has a short list of roots, as yours does.** For each M let H_M be that least horizon. The accepted H_M-bit prefixes of popcount exactly M + 1 play the part of `c37Roots`: a seed of popcount at most M + 1 that survives to H_M must be one of them, so the next horizon is one more than the longest survival among them. From M = 1 to M = 89 every rung has between 1 and 15 such roots. The rung after yours has one: `1298417747832963886802729684664662` (popcount 39) is the only survivor to 111 of popcount at most 39, and it does not survive to 112. The [ladder file](https://github.com/ghywel/placego/blob/c61170a421f90fb440d7fdd501aa7b79d753ec50/tests/probes/sepgap/local_q01gap_mass_ladder.out) lists H_M and the number of roots for every rung, and the roots themselves from M = 30 on.

If you want more rungs in Lean: the popcount-bounded search visits 63,489 trace nodes for M = 50 and 407,950 for M = 60.

**How it was checked.** Python with exact integers. The acceptor is a literal copy of `accept` and `gateNext`. For 3 ≤ H ≤ 18 the accepted prefixes equal `{z < 2^H : SurvivesTo z H}` by brute force. Every root was run forward under that acceptor, and "next horizon = 1 + longest root survival" holds at every rung. An independent Wolfram implementation reproduces the horizons for M = 37, 38, 50 and 60 and your eight seeds. None of this is kernel-checked.

**One measurement.** Over all accepted traces the row bits behave like fair coins: for H up to 162, the popcount of an H-bit prefix has mean 0.5005·H and variance 0.256·H. The least popcount is about 0.307·H + 5 up to H = 277. That is where the minimum of a branching random walk of fair coins would sit, on a language of this entropy. We see no sparse periodic family of the kind `Rule30PeriodTwoMass.sharp_86` gives for the G language. So on this evidence `MassDiverges` holds, with the horizon growing by about three per unit of mass. That is a measurement, not a proof.

Write-up: [report](https://github.com/ghywel/placego/blob/c61170a421f90fb440d7fdd501aa7b79d753ec50/reports/LOCAL-Q01GAP-MASS-TABLE-20261116.md). Code: [search](https://github.com/ghywel/placego/blob/c61170a421f90fb440d7fdd501aa7b79d753ec50/tests/probes/sepgap/local_q01gap_mass_table.py), [ladder dump](https://github.com/ghywel/placego/blob/c61170a421f90fb440d7fdd501aa7b79d753ec50/tests/probes/sepgap/local_q01gap_mass_ladder.py), [Wolfram replay](https://github.com/ghywel/placego/blob/c61170a421f90fb440d7fdd501aa7b79d753ec50/tests/probes/wolfram/q01gap_mass_table_replay.wl).

You are welcome to use any of it. If the roots would be more useful in another form, for instance as Lean lists, tell us.
