# An Immortal Frontier Is a Finite Row: Q01, Mortality and All-Length Repeat Budgets Are One Statement

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 6 November 2026.

## 1. The statements

`Q01` says that no finitely supported start of the zero-boundary left half keeps column `-1` black at every even step (`Rule30ZeroBoundary.Q01`). As integers, it says that every natural number reaches an even number under iterates of `G = F ∘ F`, with `F Y = (Y >>> 1) ^^^ (Y ||| (Y <<< 1))` (`Q01_iff_integer`). It excludes period two of the center column, and it is open.

The kit has a second statement of the same kind. A *frontier* is a finite word of bit pairs `(a, b)`, legal when its first high bit is `1`. The update `Z` scans a frontier from left to right with a zero memory. It succeeds exactly when the two final memories `u` and `v` agree; it then emits their common value `s` as a scalar and appends the birth symbol `(1, !s)`. `run` iterates `Z` and stops at the first failed guard. *Mortality* says that every legal frontier eventually fails a guard. A *repeat budget at length `r`* is one bound on the number of equal adjacent scalars over every successful tape of every legal frontier of length `r`.

The kit proves that a repeat budget at every length is mortality (`budget_iff_mortality`) and that mortality implies `Q01` (`Q01_of_mortality`). It records the converse as not known, because mortality quantifies over every legal frontier, including ones not read off any left half.

This module proves the converse (`mortality_of_Q01`). So the three statements are one: `mortality_iff_Q01` and `budget_iff_Q01`.

## 2. The chart

Suppose a legal frontier never fails a guard. It has successive frontiers `fr n`, with `Z (fr n) = some (fr (n + 1), s n)`. Count depth `e` inward from the terminal end, and write `hi n e` and `lo n e` for the high and low bit of `fr n` at depth `e`, white past the far end. Place these bits in a space-time chart at time `τ` and depth `e + 1`:

| bit | where |
|---|---|
| `hi n e` | `τ + e = 2 n` |
| `lo n e` | `τ + e + 1 = 2 n` |

Every cell of the chart is filled exactly once, by the parity of `τ + e`. Time is counted from the frontier's own length, so the chart has no other parameter.

One update gives two recurrences at every depth (`Z_rec`):

```
hi (n + 1) (e + 2) = hi (n + 1) (e + 1)  xor  (lo (n + 1) (e + 1)  or  hi n e)
lo (n + 1) (e + 2) = lo (n + 1) (e + 1)  xor  (hi n (e + 1)  or  lo n e)
```

Inside the frontier these are the kit's `Z_depth`. Past the far end they still hold: at the first such depth they read the scan's zero memory, which cancels, and beyond it every cell is white. This extension is the only new fact about `Z` that the proof needs.

Read at the chart's positions, each recurrence is the Rule 30 recurrence, solved for the cell on the left. The first covers `τ + e` even and the second covers `τ + e` odd. So every cell of depth at least two obeys the rule (`chart_interior`):

```
C (τ + 1) (e + 1) = C τ (e + 2)  xor  (C τ (e + 1)  or  C τ e)
```

## 3. The wall

Depth one is where the guard does its work. After an update, the last two symbols of `fr (n + 1)` are the birth symbol `(1, !s n)` and the emitted `(s n, s n)`. That gives the two wall cases:

| time | depth one | depth two | depth one, one tick later |
|---|---|---|---|
| `τ = 2 n`, `n ≥ 1` | `1` | `s n` | `!s n` |
| `τ = 2 n + 1` | `!s n` | `s n` | `1` |

In both rows the last entry is depth two xor depth one, which is the rule with a white cell at depth zero (`chart_wall`). The guard is what makes this work: the two final memories agree, so one value sits at depth two in both rows.

The wall holds from time one on, and not always at time zero, because the first frontier's terminal high bit need not be `1`. So the proof starts at time two, which also puts the black terminal cells on even steps.

## 4. The proof

Let `start` be the row of the chart at time two. Then:

- `zrow_chart`: the chart from time two is the zero-boundary evolution of `start`. This is an induction on time, using `chart_wall` at depth one and `chart_interior` below it.
- `inX_start`: column `-1` is black at every even step, because the cell at time `2 k + 2` and depth one is the terminal high bit of `fr (k + 1)`, a birth symbol.
- `finSupp_start`: `start` is finitely supported. Frontiers grow by one symbol per update, so depth `e` at time two reads a frontier of length about `|fr 0| + e / 2`, which is past its far end once `e` is large.

That contradicts `Rule30ZeroBoundary.Q01`, which gives `mortality_of_Q01`. `Legal` is used only to know that the first frontier is nonempty. The reverse arrow is `Q01_of_mortality`, through `Q01_iff_staged`, and `budget_iff_Q01` adds `budget_iff_mortality`.

The proof does not show that the immortal frontier was read off this row. It only needs the row.

## 5. A worked example

No immortal frontier is known, so the chart can only be watched on frontiers that die. The cell below implements `scan`, `Z` and `run` directly. It takes all 10,922 legal frontiers of length at most 7, keeps those that pass at least three updates, and checks the rule at every chart cell whose frontiers all exist, at the interior and at the wall from time one. All 28,560 interior cells and 5,208 wall cells agree.

It then follows the longest run. The frontier `(1,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,1)` passes 10 updates with tape `0001101011`. Its chart's row at time two is the natural 28469, of width 15. Evolved on its own, that row keeps column `-1` black at the even ticks 0 to 18 and first shows white at tick 20, twice the number of updates. That last equality is one instance; the module does not prove a finite bound of this kind.

## 6. Prior art and scope

`Rule30SurvivalBridge` and `Rule30AlternatingTraceBridge`, contributed by David Condrey, define the frontier and prove the arrows used here. `immortalFromHistory` there is the direction from a history to a frontier; this module goes the other way. R30-20261102-b8e784, by G.P.J.W. Quint and Gemini, unifies the two modules' definitions and discharges their reconstruction statements, and `FG` and `Reconstruction` read a frontier's bits from its scalars, which is close in spirit to the chart. The kit's catalogue, at main `9d837cd5`, and its docstrings say the converse is not known, and the external repository `lhallee/rule30-open` lists it among its open arrows at commit `f877f5af`. We found no converse in the kit, on the portal, in the open pull requests, or in closed pull requests 75, 76 and 85, where these modules were added and reviewed.

Nothing here proves `Q01`, mortality or a budget, and Problems 1 to 3 stay open. The equivalence is logical: it says nothing about which form is easier to prove. A budget at one fixed length is a weaker statement; the equivalence is for budgets at every length.
