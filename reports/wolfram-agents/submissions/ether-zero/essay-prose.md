---
Template: ComputationalEssay
Name: The classic ether of rule 30 absorbs a black edge: front speed exactly zero
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-03
Description: A partial result proved in core Lean: a black cell inserted into the ether of the kit's Rule30Ether, at any of its 28 alignments, disturbs the ether only inside a fixed window from a finite time on, so the leftmost disturbance moves with speed exactly zero.
Abstract: See abstract.txt.
Keywords: [rule 30, Rule 30 Prize, ether, wall, trap, front, news speed, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[Kit pull request 65: Rule30Ether and its wall trap](https://github.com/WolframInstitute/Rule30PrizeKit/pull/65)"]
---

## The question

Rule 30 updates each cell from itself and its two neighbours: the new colour is *left* XOR (*centre* OR *right*). The
three Rule 30 Prize problems ask about the centre column of the pattern grown from a single black cell. This essay proves
nothing about that column. It is about how far news travels through a periodic background of rule 30.

Rule 30 has spatially and temporally periodic orbits, its **ethers**. The kit's `Rule30Ether` (Troy Lowry, kit pull
request 65) gives one with spatial period 7 and temporal period 4, the **classic ether**. Its seven columns at the four
phases are

$$B_1 = 0011,\ B_2 = 0110,\ B_3 = 1101,\ B_4 = 0101,\ B_5 = 0011,\ c = 0001,\ c = 0001.$$

```wl
etherTable = {{0,0,1,1},{0,1,1,0},{1,1,0,1},{0,1,0,1},{0,0,1,1},{0,0,0,1},{0,0,0,1}};
ether[j_, phi_] := etherTable[[Mod[j, 7] + 1, Mod[phi, 4] + 1]];
ArrayPlot[Table[ether[x, t], {t, 0, 27}, {x, 0, 41}], ImageSize -> 420]
```

Change one cell of the ether and the damage spreads. Rule 30 always passes news to the right at full speed, because the
new colour is an XOR with the left neighbour. To the left it can be masked: a black centre hides the right neighbour.
How fast does damage move leftwards into this ether?

## The experiment: insert a black edge

Take the ether at an alignment $(c_0, c_1)$: column $x$ at time $t$ is $\mathrm{ether}(x + c_0, t + c_1)$. Keep it for
$x < 0$, put a black cell at $x = 0$ and white to its right, and run rule 30. Compare with the undisturbed ether. The
leftmost cell where they differ is the **front** $F(t)$.

```wl
row[c0_, c1_, lo_, hi_] := Table[Which[x < 0, ether[x + c0, c1], x == 0, 1, True, 0], {x, lo, hi}];
evo = CellularAutomaton[30, row[4, 3, -700, 400], 300];
ref = Table[ether[x + 4, t + 3], {t, 0, 300}, {x, -700, 400}];
ArrayPlot[BitXor[evo, ref][[All, 600 ;; 760]], ImageSize -> 480]
```

The picture shows the difference from the ether near $x = 0$. (The plotted window stays far from the ends of the
finite row, which wrap around.) The damage spreads to the right at full speed. Its left end wanders for a while, then
stops for good.

## Why it stops: Lowry's ether-wall trap

`Rule30Ether` contains 109 states of a 13-cell strip lying to the right of a $B_3$ column, the **wall states**, with two
properties checked by the kernel (`wallOK_true`):

- **Closed under every right input.** If the strip is a wall state at phase $\varphi$, then whatever the cell to its
  right does, the strip is a wall state at phase $\varphi + 1$ one step later.
- **Masked head.** Whenever $B_3$ is white, the strip's first cell carries the ether's own $B_4$ value.

So "ether columns up to a $B_3$ column, then a wall state" is a trap. Each column left of the $B_3$ column reads three
ether cells. The $B_3$ column reads the wall's head only when it is white, and then sees the ether's value. When it is
black, the head is masked. The strip stays a wall state for any input from the right. The kit proves this with column 0
held to an ether column for all time (`trap_invariant`), and uses it to exclude ether walls beside a periodic centre
column. Here the whole left half-line is the ether, and the same induction runs with the prescribed column replaced by
the induction hypothesis:

```lean
theorem trap_two_sided {G : Nat → Int → Bool} (hG : IsR30Z G) (c xB : Int) (s t1 : Nat)
    (hk : (xB + c) % 7 = 2)
    (hE : ∀ x, x ≤ xB → G t1 x = etherZ c x (t1 + s))
    (hW : ((t1 + s) % 4, rowZ G t1 xB 13) ∈ wallStates) :
    ∀ n, (∀ x, x ≤ xB → G (t1 + n) x = etherZ c x (t1 + n + s)) ∧
      ((t1 + n + s) % 4, rowZ G (t1 + n) xB 13) ∈ wallStates
```

## The inserted edge enters the trap at every alignment

The ether has $7 \times 4 = 28$ alignments. For each, the evolution of the inserted edge reaches the trap: at some time
$t_1 \le 222$, the ether is intact at and left of a $B_3$ column $x_B$, and the next 13 cells form a wall state.

| $(c_0, c_1)$ | $t_1$ | $x_B$ | $(c_0, c_1)$ | $t_1$ | $x_B$ | $(c_0, c_1)$ | $t_1$ | $x_B$ | $(c_0, c_1)$ | $t_1$ | $x_B$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| (0,0) | 81 | −19 | (2,0) | 8 | 0 | (4,0) | 6 | −2 | (6,0) | 4 | −4 |
| (0,1) | 13 | −5 | (2,1) | 17 | −7 | (4,1) | 148 | −23 | (6,1) | 25 | −11 |
| (0,2) | 10 | 2 | (2,2) | 16 | −7 | (4,2) | 6 | −2 | (6,2) | 4 | −4 |
| (0,3) | 186 | −26 | (2,3) | 8 | 0 | (4,3) | 222 | −37 | (6,3) | 82 | −18 |
| (1,0) | 185 | −27 | (3,0) | 7 | −1 | (5,0) | 221 | −38 | | | |
| (1,1) | 17 | −6 | (3,1) | 7 | −1 | (5,1) | 148 | −24 | | | |
| (1,2) | 9 | 1 | (3,2) | 16 | −8 | (5,2) | 5 | −3 | | | |
| (1,3) | 9 | 1 | (3,3) | 7 | −1 | (5,3) | 5 | −3 | | | |

These 28 facts are checked by the kernel itself, not by an external program:

- **The light cone.** `G_left`: the columns $x < -t$ are still the ether at time $t$.
- **A finite simulation.** `iter3_G`: iterating the kit's `lin3` on a list agrees with the whole-line evolution on the
  list's range, via the kit's `lin3_seg`.
- **The check itself.** `checkEntry`, run by `decide` for each alignment. It simulates from $-2t_1$ to time $t_1$, and
  checks that the columns $-t_1, \dots, x_B$ are the ether, that $x_B$ is a $B_3$ column, and that the next 13 cells
  are one of the 109 wall states.

## The disturbance never heals

None of the 109 wall states equals the ether's own 13 cells after a $B_3$ column (`wall_ne_ref_all`, by `decide`). So
once trapped, the strip always differs from the ether somewhere, and the front stays inside it. Together:

```lean
theorem edge_pinned (c0 c1 : Nat) (h0 : c0 < 7) (h1 : c1 < 4) : ∃ xB : Int, ∃ t1 : Nat, ∀ t, t1 ≤ t →
    (∀ x, x ≤ xB → G c0 c1 t x = etherZ c0 x (t + c1)) ∧
    ∃ x, xB < x ∧ x ≤ xB + 13 ∧ G c0 c1 t x ≠ etherZ c0 x (t + c1)
```

**The front is pinned:** $x_B < F(t) \le x_B + 13$ for every $t \ge t_1$, at every alignment. Its leftward speed is
exactly zero.

## Scope and what is new

- **Frame.** The lab frame of the classic ether. Nothing here concerns the centre column of the single-cell pattern or
  the Prize problems themselves.
- **Prior art.** The ether and the wall trap are Lowry's (kit pull request 65), used there to exclude ether walls beside
  a periodic centre column. New here are the trap on the whole line, the entry of an inserted black edge at every
  alignment, and with them the exact zero of the edge's front speed.
- **Context.** Among the periodic backgrounds we examined, the classic ether is the one in which the inserted edge's left
  front is rigid. Elsewhere it moves at a positive rate below light speed.
- **Checking.** The Lean module builds on the verifier's kit (93d98bbe) in core Lean with standard axioms (propext,
  Classical.choice, Quot.sound), and passes the kit's `Check.lean` with the headlines `edge_pinned`, `trap_two_sided`
  and `wall_ne_ref_all`.
