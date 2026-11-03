---
Template: ComputationalEssay
Name: Moving walls in Rule 30: exact front speeds 5/19 and 2/9
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-03
Description: A partial result proved in core Lean: an inserted black edge on the Rule 30 ring backgrounds 100100000 (temporal period 57) and 1010000 (temporal period 63) has a front that moves left at exactly 5/19 and 2/9 cell per tick, with explicit all-time bounds from t = 300, for every right tail beyond a fixed cutoff; the proof is a kernel-checked closed set of window states with a moving anchor and an exact potential.
Abstract: See abstract.txt.
Keywords: [rule 30, Rule 30 Prize, background orbit, ether, front speed, moving wall, closed set, potential, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261103-3742dc: the classic ether absorbs a black edge](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-3742dc)", "[R30-20261103-e660e4: the universal healing bound](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-e660e4)"]
---

## The question

Rule 30 has many spatially periodic orbits, **ring backgrounds**: a word $w$ of length $N$, repeated along the whole line,
evolves into a periodic space-time pattern. Insert a single black cell into such a background, with white cells to its
right, and follow the leftmost cell where the evolution differs from the background: the **front**. How fast does it move?

On the kit's classic ether the answer is zero: the inserted edge is absorbed by a wall and the front stays in a fixed
window for ever. On other backgrounds the front keeps moving. This essay proves exact nonzero speeds for two of them:

| ring word | temporal period | alignment | front speed |
|---|---|---|---|
| `100100000` | 57 | $(0, 0)$ | exactly $5/19$ |
| `1010000` | 63 | $(0, 4)$ | exactly $2/9$ |

The background is $E(t, x) = \mathrm{orb}[(t + s) \bmod q][(t - x) \bmod N]$, with the ring orbit `orb` of period $q$ and
alignment $(0, s)$.

## A window with a moving anchor

Keep an **anchor** $A$ with the background intact at and left of $A$, and remember the $W$ cells right of it: $W = 24$ for
the first background, $16$ for the second. At each tick the new cells of the window follow from Rule 30, with one unknown
cell, the one just beyond the window, entering from the right. The anchor moves one column left exactly when its own cell
becomes a difference; otherwise it stays. A state is the pair of phases $(t \bmod q, (t - A) \bmod N)$ and the window's
cells, as a bit mask.

`step_sound` proves that one tick of this window is sound on **every** Rule 30 evolution of the whole line, whatever the
cell beyond the window is. From the inserted edge's state at $t = 300$, all states reachable under both values of the
unknown cell form a finite **closed set**: 498 states for the first background, 74 for the second. The kernel checks
closure by `decide` on bit masks (`closure_ok`), and checks that every state's window still holds a difference.

## An exact potential

Give each tick the weight $P\cdot\text{motion} + (P - S)$, with motion $-1$ for a retreat and $0$ otherwise, and
$(P, S) = (19, 14)$ or $(9, 7)$. On these closures every edge satisfies $\psi(s') - \psi(s) = $ weight for one integer
potential $\psi$; the kernel checks all edges. Summing along any path, $P\,(A(t) - A(300)) + (P - S)(t - 300)$ equals
$\psi$ of the current state, and $\psi$ takes values in $[-14, 22]$ and $[-20, 4]$ respectively.

**Theorems (`Ring57.edge_law`, `Ring63.edge_law`).** For every $t \ge 300$ there is an anchor $A$ with the background
intact at and left of $A$, a difference within the $W$ cells right of $A$, and

$$-14 \le 19(A + 72) + 5(t - 300) \le 22, \qquad -20 \le 9(A + 55) + 2(t - 300) \le 4 .$$

The front $F$ lies in $(A, A + W]$, so $5 \le 19(F + 72) + 5(t - 300) \le 478$ and $-11 \le 9(F + 55) + 2(t - 300) \le 148$:
the front stays within 26 cells, respectively 17 cells, of the lines of slopes $-5/19$ and $-2/9$. The speeds are
exactly $5/19$ and $2/9$; they are statements about the long run, not about each tick.

Because the closed set contains every successor under both values of the cell beyond the window, the speed is a property
of the front and the background. Whatever the disturbed region behind the window does, it cannot change the speed; it
only selects which state of the closure occurs.

## Any right tail

Rule 30 has radius one, so two rows that agree at time $0$ on $x \le c$ agree at time $t$ on $x \le c - t$ (`agree_cone`).
At $t = 300$ the start invariant involves only $x \le A + W$, which is $-48$ and $-39$. Hence (`edge_law_tail`) the same
laws hold for every Rule 30 evolution whose initial row agrees with the inserted edge's at $x \le 252$, respectively
$x \le 261$, whatever its cells further right. These cutoffs are sufficient, not claimed to be sharp.

## A picture

The front of the inserted edge, simulated directly on both backgrounds to $t = 1200$, minus the theorem's line:

```wl
ringOrbit[w_List] := NestWhileList[BitXor[#, BitOr[RotateRight[#, 1], RotateRight[#, 2]]] &, w, Unequal[#, w] &, {2, 1}] // Most;
frontTrack[w_List, s_Integer, tmax_Integer] := Module[{orb = ringOrbit[w], n = Length[w], q, bg, lo, hi, row0, ref0, ev, rf},
  q = Length[orb]; bg[t_, x_] := orb[[Mod[t + s, q] + 1, Mod[t - x, n] + 1]];
  lo = -2 tmax - 20; hi = tmax + 20;
  ref0 = Table[bg[0, x], {x, lo, hi}];
  row0 = Table[If[x < 0, bg[0, x], Boole[x == 0]], {x, lo, hi}];
  ev = CellularAutomaton[30, row0, tmax]; rf = CellularAutomaton[30, ref0, tmax];
  Table[{t, lo - 1 + First[Select[Range[t + 2, hi - lo - t], ev[[t + 1, #]] != rf[[t + 1, #]] &, 1]]}, {t, 300, tmax}]];
f57 = frontTrack[{1, 0, 0, 1, 0, 0, 0, 0, 0}, 0, 1200];
f63 = frontTrack[{1, 0, 1, 0, 0, 0, 0}, 4, 1200];
d57 = {#[[1]], (19 (#[[2]] + 72) + 5 (#[[1]] - 300))/19.} & /@ f57;
d63 = {#[[1]], (9 (#[[2]] + 55) + 2 (#[[1]] - 300))/9.} & /@ f63;
Column[{
  Row[{"ring 100100000: 19 (F + 72) + 5 (t - 300) ranges over ", MinMax[19 (#[[2]] + 72) + 5 (#[[1]] - 300) & /@ f57], " (theorem: within [5, 478])"}],
  Row[{"ring 1010000: 9 (F + 55) + 2 (t - 300) ranges over ", MinMax[9 (#[[2]] + 55) + 2 (#[[1]] - 300) & /@ f63], " (theorem: within [-11, 148])"}],
  ListLinePlot[{d57, d63}, PlotLegends -> {"100100000: F + 72 + 5 (t - 300)/19", "1010000: F + 55 + 2 (t - 300)/9"},
    AxesLabel -> {"t", "cells"}, ImageSize -> 480, PlotRange -> All]}]
```

Both curves stay in a flat band, inside the theorem's bounds; the lower bounds $5$ and $-11$ are attained in this range.
The simulated row is wide enough on the left that its truncated end never reaches the front.

## Related work and what is new

- **The kit.** `Rule30Ether` proves that the classic ether's 109 wall states are closed under every input from the right
  (`trap_invariant`): a stationary wall. Here the wall moves, and the closed set carries a moving anchor and an exact
  potential, so it gives an exact nonzero speed rather than speed zero.
- **The portal.** [R30-20261103-3742dc](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-3742dc)
  proves that on the classic ether an inserted edge has front speed exactly zero.
  [R30-20261103-e660e4](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-e660e4) proves a
  universal upper bound on the leftward speed of any change confined to the right half-line, whose periodic table lists
  $1/2$ for `100100000` and $2/9$ for `1010000`. On `1010000` the inserted edge attains that bound; on `100100000` it moves
  strictly slower.
- **New here.** Exact nonzero front speeds of an inserted edge on two ring backgrounds, with all-time explicit bounds,
  for every right tail beyond a cutoff, kernel-checked. The closed-set method with a moving anchor was developed in the
  record linked above; it generalizes the kit's stationary trap.
- **Scope.** Two backgrounds, one alignment each. Other alignments and other ring backgrounds are not covered here; a
  census of alignments is computed in the record but not formalized. The theorems bound the anchor and hence the front;
  they do not assert an exact periodic recurrence of the front itself. Nothing here concerns the centre column of the
  single-cell pattern or the Prize problems themselves.
