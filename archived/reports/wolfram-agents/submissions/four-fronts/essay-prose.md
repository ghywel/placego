# Every configuration of rule 30 with a leftmost black cell is on its strip by tick 177,575, through wheel 87,866

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 4 November 2026.

## 1. The claim

Our entry R30-20261104-458f3b proved that every configuration of rule 30 with a leftmost black cell, whatever lies to its right, eventually agrees with one of four explicit strips on all left diagonals through wheel 87,866, after one time shift. Its classification theorem gave an eventual agreement time. Here we give a numerical deadline on each strip.

**Theorem (`forced_front_four_left_side`).** Let `x` be a configuration with a leftmost black cell. There are a shift `s ≤ 15` and a strip `v` among `A0`, `A1`, `B0`, `B1` such that wheel `j` of `x` at tick `t + s` equals wheel `j` of `v` at tick `t`, for every wheel `j ≤ 87,866` and every tick `t ≥ 177,560`.

So from tick 177,575 of its own clock at the latest, every such configuration carries one of the four strips on all of its first 87,867 wheels.

**Below the first fork (`forced_front_low_left_side`).** The same holds with wheel 53,207 and tick 107,310 in place of 87,866 and 177,560. The strip there is `A0`, because the four strips agree below wheel 53,208.

**Wheel by wheel (`forced_front_four`).** Each wheel has its own time. Wheel `j` is on the strip `v` from strip tick `F_v(j)`, the settling recursion of section 2, and this holds for every array with the left-diagonal recurrence and a black start. At wheel 87,866 the four fronts are as follows.

| strip | `F_v(87,866)` | Lean |
|---|---|---|
| `A0` | 176,968 | `FA0_87866` |
| `A1` | 177,229 | `FA1_87866` |
| `B0` | 177,170 | `FB0_87866` |
| `B1` | 177,560 | `FB1_87866` |

`forced_front_four_seed` is the single black cell. `classification_bounded` is the classification of 458f3b with its time shift bounded by 15, which 458f3b did not bound.

## 2. The settling recursion

The wheels are those of 458f3b. Write `a(j,t) = Ld x lo j t` for the cell at position `lo − t + j` at tick `t`, with `lo` the initial leftmost black cell. The two edge equations are `a(0,t+1) = a(0,t)` and `a(1,t+1) = a(0,t) ∨ a(1,t)`. In the interior, `a(j+2,t+1) = a(j,t) ⊕ (a(j+1,t) ∨ a(j+2,t))`. These are also the three equations required of an abstract array. Each strip returns after 16 ticks, so each wheel has a word of sixteen bits. A white wheel has an all-white word. A black wheel has at least one black phase.

Put `F_v(0) = 0` and `F_v(1) = 1`. Then `F_v(j + 2)` is defined from `m = max(F_v(j), F_v(j + 1))`.

- If wheel `j + 1` is white on the strip, `F_v(j + 2) = m`.
- Otherwise `F_v(j + 2)` is one more than the first tick at or after `m` at which wheel `j + 1` is black on the strip.

This is the recursion `frontBound` of the kit's `Rule30FrontLaw`, read on a strip's cycle instead of on the seed's history. It is non-decreasing (`F_mono`).

## 3. Why it bounds every configuration

The two moves of 458f3b, with the time carried.

**A black nearer wheel (`step_black`).** Suppose wheels `j` and `j + 1` of an array are aligned with the strip from strip tick `m`, and wheel `j + 1` is black at a tick `u ≥ m`. At the next tick both children take the complement of the same farther bit (`child_same`). They then have identical inputs, so the child is aligned from tick `u + 1`.

**A white nearer wheel (`step_white`).** If wheel `j + 1` is white on the strip, both children integrate the same farther word from tick `m` on, so their difference is constant from `m` (`child_white`). If it is zero, the child is aligned from `m`. If it is one, the array carries the complement of the strip's word. At a doubling wheel the complement is a time shift by the lower period (`white_shift`). At a fork it is the other strip's word (`white_fork`).

Below the first fork there are four doubling wheels, at 2, 7, 28 and 399, with shifts of 1, 2, 4 and 8, so the total shift is at most 15 (`low_from`). The white wheels 53,207, 58,286 and 72,575 are the forks, and they change the strip and not the shift. Two strips agree below their fork, so their recursions agree through it (`F_congr`). That is the proof of `forced_front_four`. The uniform statements follow because `F_v` is monotone and its largest value at wheel 87,866 is 177,560.

## 4. The recursion as a walk

A strip has 87,867 wheels, and the recursion has to be evaluated on all of them. Because `F_v` is monotone, it can be read another way. Put a pointer on a wheel `j` at a tick `t`. At each tick, move the pointer to the next wheel if the strip's cell at wheel `j` and tick `t` is black, and leave it if the cell is white. With `R_0, …, R_15` the strip's rows, that is

`j ← j + ((R_(t mod 16) >> j) & 1)`.

Start a run on wheel `j` at its known front tick `F_v(j)`. If the wheel has a black phase, the pointer first enters wheel `j + 1` at tick `F_v(j + 1)` (`run_arrival`). That first entry has a unique tick (`arrival_unique`), even when the pointer waits on the wheel. Every wheel it has passed has a black phase (`walk_black`). So four facts about the walk fix the recursion's state after a run of wheels (`frun_of_walk`). The individual pointer update is branch-free, and since the tick advances every time, sixteen ticks are one fixed expression in the sixteen rows (`st16`, `w16`).

A white wheel would hold the pointer for ever. Each strip has at most seven of them. The four lowest lie in the first 400 wheels, which the kernel evaluates directly, and the others are stepped over one at a time (`frun_white`). The strips share their wheels below the forks, so the four runs together take about 338,000 ticks.

The whole module, including the part repeated from 458f3b, builds in about seven seconds on a laptop. We first evaluated the same recursion wheel by wheel, on sixteen literal rows per strip, in four kernel modules of about seventy seconds each on the M5. Both evaluations give the four numbers of section 1.

## 5. A computation

The next two cells replay this in Wolfram Language, outside Lean, on the seed's row `A0`. The first runs the recursion and prints `F(53,207)` and `F(87,866)`. Its running value `t` stands for `max(F(j − 1), F(j))`, because `F` is monotone (`F_mono`). It waits for black on a nonwhite wheel and skips an all-white wheel at zero extra cost. It also prints the digest of the computed row, which should be that of the literal `A0` in the source, `0dc9e1db3e968ceb8e12cac61d61ca1f7fd6b749422681ae53d5f842b64d1e3c`. The second cell sets the bound beside what the single black cell actually does.

## 6. What this does and does not say

**The single seed settles earlier.** Its first exact match to the phase-zero row `A0` on these 87,867 wheels occurs at tick 117,328. The bound for its strip is 176,968. Over the measured range the recursion grows by about two ticks per wheel, while the seed’s actual front grows by about four ticks per three wheels. A wheel can already agree with the strip before the next reset. Determining the worst settling time over all configurations would require a separate argument.

**Against the general bound.** A nonwhite wheel advances after at most fifteen waiting ticks and one move. A white wheel adds zero to the recursion. Thus the same recursion has the linear bound `1 + 16 j`. That is the form of the kit's `frontBound_le_linear` at period 16, a lemma about the recursion on the seed's own history. At wheel 87,866 it is 1,405,857, about eight times the evaluated front.

**Beyond the cut.** 87,866 is where these rows stop. Extending the four-strip theorem requires proofs of the wider rows’ returns and branch conditions. The measured single-seed period doubles to 32 at wheel 87,867. Following that branch also requires a period-32 version of the walk.

**Scope.** Nothing here concerns the center column or the Prize problems.

## 7. Credits

Troy Lowry with OpenAI Codex proved an explicit clock in the kit for every configuration white to the left of an anchor. At wheel `j`, `Ld_uniform_period` gives a period of `2^j` from tick `2^j − 1`. Our earlier settling-front calculation in §8.59 measured a worst-phase bound on the common prefix. Here the proof follows a single phase through the forks and gives the settling tick for each of the four named strips. [General left-diagonal clock](https://github.com/WolframInstitute/Rule30PrizeKit/blob/96b4f2a4e91a0e2488e8c9c29e872040aa9f86b5/lean/Ruliology/CellularAutomata/Rule30FiniteDiagonals.lean#L211-L216) · [Earlier settling-front calculation](https://github.com/ghywel/placego/blob/fa5eddc0b4e9bd5a52a1e676be751c90af451fa6/reports/rule30-prize/RULE30-PRIZE-8.2.md#L221-L229)

The seed recursion and its linear bound appear in the kit’s `Rule30FrontLaw`, contributed by @AIOvernight with OpenAI Codex and Claude. Their R30-20261027-e324b6 uses settling times as barriers for center runs. Quint and Gemini sharpen the seed’s onset bounds in R30-20261103-050b68 and give exact white-count witnesses for center-color windows in R30-20261103-1c93e6. The induction follows Rowland (2006, section 5). The strips come from R30-20261104-309041 and R30-20261104-458f3b.
