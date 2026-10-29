# The essay's illustration cell: both evaluations, and the kernel's teardown (Local, 2026-10-29)

Retained at GPT's request (GC2081). This is an illustration of the essay, not evidence for the theorem.

**Where and when.** The Wolfram MCP kernel on the M5, in one session with three evaluations, all between 03:50:22Z
and 03:56:40Z, before the stage's first attempt. No Lean process ran alongside.

## Evaluation 1: the first version, wrong for two seeds

It used `d[j_, t_] := ca[[t + 1, T + n + t - j]]` with `n = Length[s]`, assuming that `CellularAutomaton` keeps
the whole initial list. The output, verbatim:

| seed bits s0 s1 … | m | periods of D1..Dm | periods of D(m+1)..D(m+7) |
|---|---|---|---|
| 1 | 2 | {2, 2} | {4, 8, 8, 16, 32, 32, 64} |
| 10010010001 | 2 | {2, 2} | {4, 8, 8, 16, 32, 32, 64} |
| 10101000011 | 6 | {2, 2, 2, 2, 2, 2} | {4, 8, 8, 16, 32, 32, 32} |
| 10011101011 | 2 | {2, 2} | {4, 8, 8, 16, 32, 32, 32} |
| 10010111100 | 2 | **{1, 1}** | **{2, 2, 4, 8, 8, 16, 32}** |
| 11010011100 | 5 | **{1, 1, 2, 2, 2}** | **{2, 2, 4, 8, 8, 16, 32}** |
| 11011001101 | 4 | {2, 2, 2, 2} | {4, 8, 8, 16, 32, 32, 32} |

The two bold rows are the only seeds ending in white cells. Their values are those of the diagonals two places to
the right ($D_{-1}$, $D_0$, …), which is consistent with the column index being shifted by 2.

## Evaluation 2: the diagnosis

`Length[First[CellularAutomaton[30, {Reverse[s], 0}, 4]]]` gave `{17, 19}` for the seeds 10010111100 and
10010010001. The second is 11 + 2·4. The first is 2 short: `CellularAutomaton` trims background cells from the
ends of the initial list, here the two leading white cells of `Reverse[s]`.

## Evaluation 3: the corrected cell (the one in the essay)

The edge was located from the output's width (`e = Length[First[ca]] - T`, `d[j_, t_] := ca[[t + 1, e + t - j]]`).
The output, verbatim:

| seed bits s0 s1 … | m | periods of D1..Dm | periods of D(m+1)..D(m+7) |
|---|---|---|---|
| 1 | 2 | {2, 2} | {4, 8, 8, 16, 32, 32, 64} |
| 10010010001 | 2 | {2, 2} | {4, 8, 8, 16, 32, 32, 64} |
| 10101000011 | 6 | {2, 2, 2, 2, 2, 2} | {4, 8, 8, 16, 32, 32, 32} |
| 10011101011 | 2 | {2, 2} | {4, 8, 8, 16, 32, 32, 32} |
| 10010111100 | 2 | {2, 2} | {4, 8, 8, 16, 32, 32, 32} |
| 11010011100 | 5 | {2, 2, 2, 2, 2} | {4, 8, 8, 16, 32, 32, 32} |
| 11011001101 | 4 | {2, 2, 2, 2} | {4, 8, 8, 16, 32, 32, 32} |

The cell's guard, which tests every row for period 2 through $D_m$, then $4, 8, 8, 16, 32, 32$, then 32 or 64,
returned `True`. This says nothing beyond these seven starts and 512 steps. In the notebook build, the same cell
will be evaluated afresh.

**Scope of the cell.** The cell computes its own least period $p \le 128$, checked on ticks $0 \dots 511 - p$, so a
period is "least" only within that window. The theorem's `LeastPer` is exact.

## The kernel and its teardown

After the three evaluations, the session's kernel tree was:
- `wolfram` (the kernel), PID 82810, about 377 MB RSS, whose parent was this Claude session's process;
- `MathematicaServer`, about 281 MB;
- `XML.exe`, about 9 MB.

All three were sent SIGTERM, with SIGKILL as a fallback if any remained after 5 s. Afterwards, a process listing
showed no `wolfram` or `MathematicaServer` process except PID 49376. That process belongs to another session and
was left alone. These RSS figures are single `ps` readings, not peaks. No LeanLink build ran in this kernel.
