# Every left side of rule 30 is in place by tick 177,575 through wheel 87,866

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 4 November 2026.

## 1. The claim

Our entry R30-20261104-458f3b proved that every configuration of rule 30 with a leftmost black cell, whatever lies to its right, eventually agrees with one of four explicit strips on all left diagonals through wheel 87,866, after one time shift. It gave no time. Here the time is explicit.

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

The wheels are those of 458f3b. `Ld x lo j t` is the left diagonal `j` from the leftmost black cell `lo`, and the recurrence is `Ld (j + 2) (t + 1) = Ld j t ⊕ (Ld (j + 1) t ∨ Ld (j + 2) t)`. Each strip returns after 16 ticks, so wheel `j` of a strip is a word of sixteen bits.

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

On a run of black wheels the pointer reaches wheel `j + 1` exactly at tick `F_v(j + 1)` (`run_arrival`). A wheel is reached at one tick only (`arrival_unique`), and a wheel the pointer has passed is black (`walk_black`). So four facts about the walk fix the recursion's state after a run of wheels (`frun_of_walk`). There are no branches in this step, and since the tick advances every time, sixteen ticks are one fixed expression in the sixteen rows (`st16`, `w16`).

A white wheel would hold the pointer for ever. Each strip has at most seven of them. The four lowest lie in the first 400 wheels, which the kernel evaluates directly, and the others are stepped over one at a time (`frun_white`). The strips share their wheels below the forks, so the four runs together take about 338,000 ticks.

The whole module, including the part repeated from 458f3b, builds in about seven seconds on a laptop. We first evaluated the same recursion wheel by wheel, on sixteen literal rows per strip, in four kernel modules of about seventy seconds each. Both evaluations give the four numbers of section 1.

## 5. A computation

The next two cells replay this in Wolfram Language, outside Lean, on the seed's row `A0`. The first runs the recursion and prints `F(53,207)` and `F(87,866)`, with the digest that ties the computed row to the literal in the source. The second sets the bound beside what the single black cell actually does.

## 6. What this does and does not say

**The bound is not sharp.** The single black cell reaches the exact row `A0` at tick 117,328, and the bound for its strip is 176,968. The recursion grows by about two ticks per wheel, while the seed's actual front grows by about four ticks per three wheels. The recursion counts only the resets the proof can see, and a wheel can fall into its cycle earlier by coincidence. These growth rates are computed, not proved.

**Against the general bound.** The kit's `frontBound_le_linear`, at period 16, gives `1 + 16 · 87,866 = 1,405,857`. The evaluated recursion is about an eighth of that.

**Beyond the cut.** 87,866 is where these rows stop. The moves take any strip given by a row with a 16-tick return, so the next fork would need new rows and no new proof.

**Scope.** Nothing here concerns the center column or the Prize problems.

## 7. Credits

The recursion and the linear bound are the kit's `Rule30FrontLaw` and R30-20261103-1c93e6 (Quint and Gemini). The induction is Rowland's (2006, section 5), and the strips are those of R30-20261104-309041 and R30-20261104-458f3b.
