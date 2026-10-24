---
Template: ComputationalEssay
Name: Two right halves absorbed by the ether: explicit instances of the coupled question CQ01
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-24
Description: A partial result on the Rule 30 Prize kit's coupled question CQ01, proved in Lean against the official definitions: for the explicit right halves with black cells 1..5 and 1..4, 6..9, the driven right half enters the kit's ether-and-wall trap, its visible column is the parity of the step, and the kit's absorption route gives CQ01 for both; their sideways rows coincide although no chain of right-end moves joins them.
Abstract: The kit's coupled question CQ01 holds iff for every finite right half R the sideways row Psi R, the constrained start whose free bits complement column 1 of R driven by the alternating column, has infinitely many black cells; it holds for R whenever that column is eventually periodic (the kit's absorption route), and the milestone R = empty is open. For R31, black cells 1..5, and R495, black cells 1..4 and 6..9 (the row of R31 at time 4), the driven right half enters the kit's ether-and-wall trap: at time 9, respectively 5, columns 1..6 carry the kit's 7 x 4 ether with the alternating column as its column B4, and columns 7..19 are one of the kit's 109 wall states. The kit's trap invariant keeps the ether for ever, so the visible column is the parity of the step for both (u_R31). Hence CQ01 for R31 and R495 (CQ01_R31, CQ01_R495) and Psi R31 = Psi R495 (Psi_eq). The two are not joined by the right-end moves, the inverse of the kit's terminal rewrites 011 -> 01 and 101 -> 11 (not_move_equivalent). Nothing is claimed about CQ01 in general, the empty right half, or Problem 1.
Keywords: [rule 30, Rule 30 Prize, Problem 1, CQ01, period 2, sideways row, ether, trap, absorption, Lean 4, LeanLink]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)", "[Rule30PeriodTwoSideways in the kit](https://github.com/WolframInstitute/Rule30PrizeKit/blob/main/lean/Ruliology/CellularAutomata/Rule30PeriodTwoSideways.lean)"]
---

## The question

A period-2 center column of rule 30 would alternate black, white, black, white for ever. The kit reduces the exclusion of eventual period 2 to the coupled question `CQ01` (`Rule30PeriodTwoCoupled`): no configuration with finitely many black cells has center column `1, 0, 1, 0, ...` from time `0`. Its sideways form (`Rule30PeriodTwoSideways`) splits the line at the center. Drive a finite right half `R` (cells `1, 2, ...`) by the alternating column on its left; read column `1` at the white steps `2 s + 1`; the visible word `u R` determines one left row `Psi R`, the only candidate partner of `R`, and `CQ01` holds iff `Psi R` has infinitely many black cells for every finite `R` (`CQ01_iff_Psi`). The kit proves one sufficient condition, the absorption route `not_finSupp_Psi_of_eventuallyPeriodic`: if `u R` is eventually periodic, `Psi R` is infinite. The milestone for the empty right half, `CQ01Empty`, is open, and in the catalog entries we searched (the kit's README and the modules that state or use the trap and the absorption route) no explicit right half is shown to satisfy the condition. Here are two that do.

## Two right halves that settle into the ether

The visible columns of `R31` (black cells `1..5`) and `R495` (black cells `1..4` and `6..9`), at the first twelve white steps, and the row of `R31` at time `4`:

```wl
drive[cells_, T_] := Module[{w = Join[cells, ConstantArray[0, T + 3]], rows = {}}, AppendTo[rows, w]; Do[w = Table[BitXor[If[p == 1, If[EvenQ[t], 1, 0], w[[p - 1]]], BitOr[w[[p]], If[p < Length[w], w[[p + 1]], 0]]], {p, Length[w]}]; AppendTo[rows, w], {t, 0, T - 1}]; rows];
r31 = drive[{1, 1, 1, 1, 1}, 30]; r495 = drive[{1, 1, 1, 1, 0, 1, 1, 1, 1}, 30];
{Table[r31[[2 s + 2, 1]], {s, 0, 11}], Table[r495[[2 s + 2, 1]], {s, 0, 11}], Take[r31[[5]], 9]}
```

Both visible columns are `0, 1, 0, 1, ...`, and the row of `R31` at time `4` is `R495`. The rows at time `9` (for `R31`) and `5` (for `R495`), columns `1..19`, and the kit's ether columns `1..6` at phase `12`:

```wl
ether = {{0, 0, 1, 1}, {0, 1, 1, 0}, {1, 1, 0, 1}, {0, 1, 0, 1}, {0, 0, 1, 1}, {0, 0, 0, 1}, {0, 0, 0, 1}};
{Take[r31[[10]], 19], Take[r495[[6]], 19], Table[ether[[Mod[3 + p, 7] + 1, Mod[12, 4] + 1]], {p, 1, 6}]}
```

Both rows are the same: columns `1..6` read `0, 0, 0, 0, 0, 1`, the ether at that phase, and columns `7..19` read `0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0`, one of the kit's wall states.

## The idea of the proof

1. **The alternating column is an ether column.** The kit's ether (`Rule30Ether`) is a rule 30 orbit of spatial period `7` and temporal period `4`, columns `B1, B2, B3, B4, B5, c, c`. Its column `B4` reads `0, 1, 0, 1`: the alternating column is `ether 3 (t + 3)` (`altCol_ether`).
2. **The trap.** The kit's `trap_invariant`, for any rule 30 evolution on the columns `p >= 0`: if column `0` is the ether column `j0` from time `t1` on, columns `1..k` carry the ether at `t1` with column `k` a `B3`, and columns `k + 1..k + 13` form one of the `109` states of `wallStates`, then this stays true for ever. With `j0 = 3`, `k = 6`, phase `3`, the hypotheses at `t1 = 9` for `R31` and `t1 = 5` for `R495` are finite and decided by the kernel (`trap31_E`, `trap31_W`, `trap495_E`, `trap495_W`).
3. **The visible column.** From then on column `1` is the ether column `B5` at phase `t + 3` (`col1_R31`, `col1_R495`), which at the white steps `2 q + 1` is the parity of `q` (`ether4_parity`); the earlier values are decided. So `u R31 q = u R495 q = (q % 2 == 1)` for every `q` (`u_R31`, `u_R495`, `u_eq`).
4. **CQ01 for both.** The visible columns are periodic, so the kit's absorption route gives `CQ01_R31` and `CQ01_R495`; and since `Psi R` is built from `u R`, `Psi R31 = Psi R495` (`Psi_eq`). In fact the common row is the left half of the ether itself: by the kit's `etherLeft_zbl` and `Psi_unique` it is `etherLeft 3`, white at depth `0` and periodic beyond with period `1011111` (a hand application of kit theorems by GPT, not one of this module's headlines).
5. **Not a move.** The kit's `Rule30ControlledResponse` shows that the terminal rewrites `011 -> 01` and `101 -> 11` preserve column `1` for every driver. Their inverse, the right-end move `S`, written on cells read from the last black cell leftward, sends `1 0 r` to `1 1 0 r`, `1 1 r` to `1 0 1 r` and the single cell `1` to `1 0` (the black wall). Its inverse `P` undoes exactly these shapes, so the root of the chain through a right half (iterate `P` while it applies) is invariant under moves in either direction (`root_of_eqv`). The two roots are the two right halves themselves, so no chain of moves joins them (`not_move_equivalent`): their equal sideways rows come from the trap, not from the rewrites.

The chain of moves from the single cell, and the two roots:

```wl
moveS[w_] := Which[Take[w, UpTo[2]] === {1, 0}, Join[{1, 1}, Rest[w]], Take[w, UpTo[2]] === {1, 1}, Join[{1, 0}, Rest[w]], w === {1}, {1, 0}, True, w];
moveP[w_] := Which[Take[w, UpTo[3]] === {1, 1, 0}, Join[{1}, Drop[w, 2]], Take[w, UpTo[3]] === {1, 0, 1}, Join[{1, 1}, Drop[w, 3]], w === {1, 0}, {1}, True, None];
root[w_] := NestWhile[moveP, w, moveP[#] =!= None &];
{NestList[moveS, {1}, 4], root[{1, 1, 1, 1, 1}], root[Reverse[{1, 1, 1, 1, 0, 1, 1, 1, 1}]]}
```

## The formal proof

The module, built against the kit at the verifier's commit:

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["@@LEAN_SOURCE@@", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The headlines, as Lean prints them:

```wl
opens = {"Ruliology.CellularAutomata.Rule30PeriodTwoSideways", "Ruliology.CellularAutomata.Rule30ZeroBoundary", "Rule30Submission"};
thm = rule30Submission["Rule30Submission.CQ01_R31"];
{thm["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.CQ01_R495"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.Psi_eq"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.u_R31"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.not_move_equivalent"]["TypeForm", "Open" -> opens]}
```

The axioms of one headline, `CQ01_R31`, are the three standard ones and nothing else (the checker verifies all five headlines and replays the whole module):

```wl
thm["Axioms"]
```

The proof's structure, one level down from the headline:

```wl
thm["CallGraph", "Depth" -> 1]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
thm["KernelCheck"]
```

## What is not proved

- Nothing about `CQ01` in general, the empty right half (`CQ01Empty`), eventual period 2, or Problem 1. These are two right halves among infinitely many.
- The trap and the absorption route are the kit's; what this module adds is two explicit right halves that enter the trap after a short transient, which the catalog entries we searched do not exhibit, and the resulting collision of sideways rows outside the right-end moves. That is a statement about our search, not a global novelty determination.
- The collision is for the alternating driver only; it does not settle the kit's question whether the terminal rewrites account for every equality of responses over all drivers.
- The Wolfram Language computations above are illustrations; the theorems do not depend on them.

## Provenance

The question grew out of a census of the sideways rows on the Apple M5 (the record's L902 to L913): many right halves give the same sideways row, the right-end moves account for some of the collisions, and the right half `1..5` with `1..4, 6..9` was the smallest pair left unexplained. Claude (Anthropic) traced it, recognized the kit's ether in the block beside the wall and found the trap entries; GPT (OpenAI) proved that move classes never merge under evolution, found the smaller witnesses (the row of `R31` at time `4` is `R495`), read the proof and pointed to the kit's existing rewrites. The record is at github.com/ghywel/placego, reports/wolfram-agents/submissions/trap-pair.

## References

[1] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[2] Wolfram Institute, [*The Rule 30 Prize kit*](https://github.com/WolframInstitute/Rule30PrizeKit), 2026: `Rule30Ether.trap_invariant`, `Rule30Ether.wallStates`, `Rule30PeriodTwoSideways.not_finSupp_Psi_of_eventuallyPeriodic`, `Rule30PeriodTwoSideways.CQ01_iff_Psi`, `Rule30ControlledResponse.tail_011_drv`.
