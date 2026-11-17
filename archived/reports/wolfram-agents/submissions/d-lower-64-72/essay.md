---
Template: ComputationalEssay
Name: Death-time lower bounds at widths 64 to 72, with witnesses from a complete GPU census
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-24
Description: A partial result on the kit's Q01 (the zero-boundary reduction of the period-2 question, Problem 1 of the Rule 30 Prize), proved in Lean against the kit's own definitions: explicit starts give the lower bounds D(64) >= 116, D(66) >= 120, D(68) >= 122, D(70) >= 124 and D(72) >= 130 on the death time, at widths where the kit, at its pinned commit cc1e0e0, has no statement.
Abstract: Write D(W) for the largest, over zero-boundary starts supported at depths at most W, of the first even time at which the depth-1 cell is white. At the pinned kit commit cc1e0e0, the kit proves D(52) <= 96 and has no statement above width 52. A complete numerical GPU census of the reconstructed starts surviving the even times below each width found the maxima D(64) = 116, D(66) = 120, D(68) = 122, D(70) = 124 and D(72) = 130; earlier deaths cannot exceed the exhibited values, which are greater than their widths. This module proves the lower bounds in Lean: for each width an explicit start, one of the census maximizers, is black at depth 1 at every even time below the bound and white at it, by the kit's prun and run_toFun (headlines Rule30Submission.width64_lower to width72_lower). Maximality and the maximizer counts are numerical, not proved here.
Keywords: [rule 30, Rule 30 Prize, Problem 1, Q01, zero boundary, death time, lower bound, witness, GPU census, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record, CHAT-LEDGER.md L863 to L868](https://github.com/ghywel/placego/blob/main/CHAT-LEDGER.md)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)", "[Submission R30-20261023-8e6bd3, D(52) = 96 exact](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-8e6bd3)"]
---

## The question

The kit reduces the period-2 question of Problem 1 to `Q01`: every finite start of the zero-boundary left half, driven by the clock at column 0, has a white cell at depth 1 at some even time. Write `D(W)` for the largest, over starts supported at depths 1 to `W`, of the first even time at which the depth-1 cell is white; `Q01` says `D(W)` is finite for every `W`. The kit at the pinned commit cc1e0e0 proves `D(52) <= 96` by 256 kernel-checked chunk computations and has nothing above width 52. Our earlier submissions proved `D(52) = 96` and `D(56) = 100` exactly. This essay proves lower bounds at five larger widths: `D(64) >= 116`, `D(66) >= 120`, `D(68) >= 122`, `D(70) >= 124`, `D(72) >= 130`.

## The zero-boundary half-line

A start is a row of cells at depths `1, 2, 3, …`; depth `k` sits at position `-k`, so depth `k + 1` is the left neighbour of depth `k` and the wall at depth 0, always white, is the right neighbour of depth 1. Rule 30 then reads `new(k) = old(k + 1) xor (old(k) or old(k - 1))` for `k >= 1`, with `new(0) = false`. The kit's `Rule30ZeroBoundarySmall` packs a row into a natural number (bit `j` is depth `j + 1`) and steps it by `pstep r = (r >>> 1) xor (r ||| (r <<< 1))`; its theorem `run_toFun` says this packed orbit is the physical evolution `zrow`. The same step in the Wolfram Language:

```wl
pstep[r_] := BitXor[BitShiftRight[r, 1], BitOr[r, BitShiftLeft[r, 1]]];
orbit[r_, n_] := NestList[pstep, r, n];
depth1[r_, n_] := BitAnd[#, 1] & /@ orbit[r, n];
```

The five witnesses, as numbers whose bits are the depths, and their bit lengths (each at most its width):

```wl
w64 = 16^^88b46d66afc2fbd5; w66 = 16^^1f2401d1c7d2b42ab; w68 = 16^^46f44349be325d4ab; w70 = 16^^3f6591177592c2aaab; w72 = 16^^d464cc8c0b5f0562ab;
BitLength /@ {w64, w66, w68, w70, w72}
```

The first even time at which depth 1 is white, for each:

```wl
firstEvenWhite[r_, n_] := First[Select[Range[0, n, 2], depth1[r, n][[# + 1]] == 0 &]];
firstEvenWhite[#, 300] & /@ {w64, w66, w68, w70, w72}
```

The orbit of `w72` for 132 steps, depth 1 at the left:

```wl
rows = Reverse[IntegerDigits[#, 2, 210]] & /@ orbit[w72, 132];
ArrayPlot[rows, ImageSize -> 600, Frame -> False]
```

## The Lean module

LeanLink and the kit:

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

The module imports the kit, defines the five witnesses, proves each is below `2^W` (so supported at depths at most `W`), evaluates its packed orbit at every even time below the bound by `decide +kernel` and at the bound itself, and bridges to `zrow` by the kit's `run_toFun`:

```wl
rule30Submission = LeanImportString["import Rule30PrizeKit
import Ruliology.CellularAutomata.Rule30ZeroBoundarySmall

/-!
# Death-time lower bounds at widths 64, 66, 68, 70, 72: explicit witnesses from a complete GPU census

**Partial result on the kit's `Q01` (the period-2 question, Problem 1 of the Rule 30 Prize), proved against the kit's own
definitions.** Write `D(W)` for the largest, over zero-boundary starts supported at depths at most `W`, of the first even time at
which the depth-1 cell is white. The kit at the pinned commit cc1e0e0 proves `D(52) <= 96` (`Rule30ZeroBoundaryWidth52`) and has no
statement at any width above 52. This module proves the lower bounds `D(64) >= 116`, `D(66) >= 120`, `D(68) >= 122`, `D(70) >= 124`, `D(72) >= 130`: for each width an explicit start,
supported at depths at most `W`, is black at depth 1 at every even time below the bound and white at the bound, by the kit's
packed evaluator `prun` and its bridge `run_toFun` (`width64_lower`, `width66_lower`, `width68_lower`, `width70_lower`, `width72_lower`).

**Where the witnesses come from.** A complete numerical census on a GPU of every reconstructed start of each width that
survives the even times below `W` (every maximizer lies among them, since the values exceed `W`) found these values to be the
maxima, each witness attaining its width's census maximum. The engine is an exact lane engine in Metal; at each width a batch of
2^24 starts, a sample of further starts, every maximizer and every chunk holding one were checked against an independent CPU
evaluation of the kit's lane check. The census is numerical; this module proves only the lower bounds.

**The argument** is a kernel computation and the kit's own lemmas: `w < 2 ^ W` by `decide`; `toFun w k = false` beyond the width
by the kit's `testBit_ge_of_lt`; the packed orbit `prun w (2 s)` tested at depth 1 for every `s < D / 2` by `decide +kernel`;
`zrow (toFun w) t 1 = (prun w t).testBit 0` by the kit's `run_toFun`.

**Provenance.** The Wolfram · Collatz · Mahler record (github.com/ghywel/placego, CHAT-LEDGER.md L863 to L868, 2026-10-24).
Nothing is claimed for maximality, for the number of maximizers, or for any upper bound.
-/

set_option Elab.async false

namespace Rule30Submission

open Ruliology.CellularAutomata
open Ruliology.CellularAutomata.Rule30ZeroBoundary
open Ruliology.CellularAutomata.Rule30ZeroBoundarySmall

/-- `toFun r` is false beyond the width of `r`. -/
theorem toFun_width {r W : Nat} (h : r < 2 ^ W) (k : Nat) (hk : W < k) : toFun r k = false := by
  unfold toFun
  have h1 : k ≠ 0 := by omega
  simp only [h1, ite_false]
  exact testBit_ge_of_lt h (by omega)

/-- The physical depth-1 cell of the start `toFun r` at time `t` is bit `0` of the packed orbit (the kit's `run_toFun`). -/
theorem zrow_packed (r t : Nat) : zrow (toFun r) t 1 = (prun r t).testBit 0 := by
  rw [run_toFun]; rfl

theorem survives_of_black {r D : Nat} (hb : ∀ s, s < D / 2 → (prun r (2 * s)).testBit 0 = true) (hD : D % 2 = 0) :
    ∀ t, t < D → t % 2 = 0 → zrow (toFun r) t 1 = true := by
  intro t ht he
  rw [zrow_packed]
  obtain ⟨s, rfl⟩ : ∃ s, t = 2 * s := ⟨t / 2, by omega⟩
  exact hb s (by omega)

/-! ## Width 64: `D(64) >= 116` -/

/-- The width-64 witness (64 bits; bits are depths 1 .. 64). -/
def w64 : Nat := 0x88b46d66afc2fbd5

theorem w64_lt : w64 < 2 ^ 64 := by decide

/-- Black at depth 1 at every even time below 116: 58 packed orbits. -/
theorem w64_black : ∀ s, s < 58 → (prun w64 (2 * s)).testBit 0 = true := by decide +kernel

/-- White at 116: the physical death of `w64`. -/
theorem w64_white : (prun w64 116).testBit 0 = false := by decide +kernel

theorem w64_survives : ∀ t, t < 116 → t % 2 = 0 → zrow (toFun w64) t 1 = true :=
  survives_of_black w64_black rfl

theorem w64_dies : zrow (toFun w64) 116 1 = false := by
  rw [zrow_packed]; exact w64_white

/-- **A lower bound at width 64:** a start supported at depths at most 64 with no even white time below 116. -/
theorem width64_lower :
    ∃ x : Nat → Bool, (∀ k, 64 < k → x k = false) ∧ (∀ t, t < 116 → t % 2 = 0 → zrow x t 1 = true) :=
  ⟨toFun w64, toFun_width w64_lt, w64_survives⟩

/-! ## Width 66: `D(66) >= 120` -/

/-- The width-66 witness (65 bits; bits are depths 1 .. 66). -/
def w66 : Nat := 0x1f2401d1c7d2b42ab

theorem w66_lt : w66 < 2 ^ 66 := by decide

/-- Black at depth 1 at every even time below 120: 60 packed orbits. -/
theorem w66_black : ∀ s, s < 60 → (prun w66 (2 * s)).testBit 0 = true := by decide +kernel

/-- White at 120: the physical death of `w66`. -/
theorem w66_white : (prun w66 120).testBit 0 = false := by decide +kernel

theorem w66_survives : ∀ t, t < 120 → t % 2 = 0 → zrow (toFun w66) t 1 = true :=
  survives_of_black w66_black rfl

theorem w66_dies : zrow (toFun w66) 120 1 = false := by
  rw [zrow_packed]; exact w66_white

/-- **A lower bound at width 66:** a start supported at depths at most 66 with no even white time below 120. -/
theorem width66_lower :
    ∃ x : Nat → Bool, (∀ k, 66 < k → x k = false) ∧ (∀ t, t < 120 → t % 2 = 0 → zrow x t 1 = true) :=
  ⟨toFun w66, toFun_width w66_lt, w66_survives⟩

/-! ## Width 68: `D(68) >= 122` -/

/-- The width-68 witness (67 bits; bits are depths 1 .. 68). -/
def w68 : Nat := 0x46f44349be325d4ab

theorem w68_lt : w68 < 2 ^ 68 := by decide

/-- Black at depth 1 at every even time below 122: 61 packed orbits. -/
theorem w68_black : ∀ s, s < 61 → (prun w68 (2 * s)).testBit 0 = true := by decide +kernel

/-- White at 122: the physical death of `w68`. -/
theorem w68_white : (prun w68 122).testBit 0 = false := by decide +kernel

theorem w68_survives : ∀ t, t < 122 → t % 2 = 0 → zrow (toFun w68) t 1 = true :=
  survives_of_black w68_black rfl

theorem w68_dies : zrow (toFun w68) 122 1 = false := by
  rw [zrow_packed]; exact w68_white

/-- **A lower bound at width 68:** a start supported at depths at most 68 with no even white time below 122. -/
theorem width68_lower :
    ∃ x : Nat → Bool, (∀ k, 68 < k → x k = false) ∧ (∀ t, t < 122 → t % 2 = 0 → zrow x t 1 = true) :=
  ⟨toFun w68, toFun_width w68_lt, w68_survives⟩

/-! ## Width 70: `D(70) >= 124` -/

/-- The width-70 witness (70 bits; bits are depths 1 .. 70). -/
def w70 : Nat := 0x3f6591177592c2aaab

theorem w70_lt : w70 < 2 ^ 70 := by decide

/-- Black at depth 1 at every even time below 124: 62 packed orbits. -/
theorem w70_black : ∀ s, s < 62 → (prun w70 (2 * s)).testBit 0 = true := by decide +kernel

/-- White at 124: the physical death of `w70`. -/
theorem w70_white : (prun w70 124).testBit 0 = false := by decide +kernel

theorem w70_survives : ∀ t, t < 124 → t % 2 = 0 → zrow (toFun w70) t 1 = true :=
  survives_of_black w70_black rfl

theorem w70_dies : zrow (toFun w70) 124 1 = false := by
  rw [zrow_packed]; exact w70_white

/-- **A lower bound at width 70:** a start supported at depths at most 70 with no even white time below 124. -/
theorem width70_lower :
    ∃ x : Nat → Bool, (∀ k, 70 < k → x k = false) ∧ (∀ t, t < 124 → t % 2 = 0 → zrow x t 1 = true) :=
  ⟨toFun w70, toFun_width w70_lt, w70_survives⟩

/-! ## Width 72: `D(72) >= 130` -/

/-- The width-72 witness (72 bits; bits are depths 1 .. 72). -/
def w72 : Nat := 0xd464cc8c0b5f0562ab

theorem w72_lt : w72 < 2 ^ 72 := by decide

/-- Black at depth 1 at every even time below 130: 65 packed orbits. -/
theorem w72_black : ∀ s, s < 65 → (prun w72 (2 * s)).testBit 0 = true := by decide +kernel

/-- White at 130: the physical death of `w72`. -/
theorem w72_white : (prun w72 130).testBit 0 = false := by decide +kernel

theorem w72_survives : ∀ t, t < 130 → t % 2 = 0 → zrow (toFun w72) t 1 = true :=
  survives_of_black w72_black rfl

theorem w72_dies : zrow (toFun w72) 130 1 = false := by
  rw [zrow_packed]; exact w72_white

/-- **A lower bound at width 72:** a start supported at depths at most 72 with no even white time below 130. -/
theorem width72_lower :
    ∃ x : Nat → Bool, (∀ k, 72 < k → x k = false) ∧ (∀ t, t < 130 → t % 2 = 0 → zrow x t 1 = true) :=
  ⟨toFun w72, toFun_width w72_lt, w72_survives⟩

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

The environment loads:

```wl
Head[rule30Submission]
```

## The headline theorems

The five lower bounds, one per width:

```wl
opens = {"Ruliology.CellularAutomata.Rule30ZeroBoundary", "Ruliology.CellularAutomata.Rule30ZeroBoundarySmall", "Rule30Submission"};
thm = rule30Submission["Rule30Submission.width72_lower"];
rule30Submission["Rule30Submission." <> #]["TypeForm", "Open" -> opens] & /@ {"width64_lower", "width66_lower", "width68_lower", "width70_lower", "width72_lower"}
```

The axioms behind each headline, which must be standard:

```wl
rule30Submission["Rule30Submission." <> #]["Axioms"] & /@ {"width64_lower", "width66_lower", "width68_lower", "width70_lower", "width72_lower"}
```

The width-72 witness's survival and death, as the kernel evaluated them (black at every even time below 130; white at 130):

```wl
{rule30Submission["Rule30Submission.w72_survives"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.w72_dies"]["TypeForm", "Open" -> opens]}
```

The module's two bridge lemmas, from the kit's `run_toFun` and `testBit_ge_of_lt`:

```wl
{rule30Submission["Rule30Submission.zrow_packed"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.toFun_width"]["TypeForm", "Open" -> opens]}
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
thm["KernelCheck"]
```

## Where the witnesses come from: a complete GPU census (numerical)

Every start of width at most `W` that survives the even times below `W` is fixed by its `W/2` odd trace bits (the kit's free bits), and every maximizer of `D(W)` is among them, because the values found exceed `W` and a start dying earlier cannot reach them. An exact lane engine on the GPU (Metal, 32 starts per machine word) reconstructed and evolved all `2^(W/2)` of these surviving starts at each width (not all `2^W` bit strings, which the reduction makes unnecessary): `2^32` starts at width 64 up to `2^36` (68.7 billion) at width 72, about 18 minutes of GPU at width 72. The engine was validated before it was trusted: exhaustive agreement with brute force over all starts at widths 10 to 14; a cell-by-cell comparison of the evolution at the moving edge; a deliberately broken build (the edge cell not computed) detected; and, at every width, a batch of 16,777,216 starts compared lane for lane with an independent CPU evaluation of the kit's own lane check (`Rule30ZeroBoundaryLanes.check`), with 64 further starts per batch of 2^24 re-simulated by a scalar evaluator. Every maximizer was re-simulated by the scalar evaluator, and the CPU evaluation of the kit's check was run on every chunk holding one, finding exactly the same maximizers there. The remaining starts rest on the GPU engine and those samples; they did not each receive an independent CPU replay. At width 64 the value 116 also agrees with an earlier complete CPU census.

| width W | census maximum | starts attaining it | proved here |
|---|---|---|---|
| 64 | 116 | 40 | D(64) >= 116 |
| 66 | 120 | 112 | D(66) >= 120 |
| 68 | 122 | 32 | D(68) >= 122 |
| 70 | 124 | 156 | D(70) >= 124 |
| 72 | 130 | 252 | D(72) >= 130 |

With the exact values of earlier submissions (`D(52) = 96`, `D(56) = 100`) and our width-60 certificate (`D(60) = 114`), the table reads 96, 100, 114, 116, 120, 122, 124, 130 at widths 52 to 72: `D(W)/W` stays between 1.77 and 1.90, and the step from 70 to 72 is the largest since 60.

## What is not proved

- Only the five lower bounds are proved here. That each witness is a maximum, the counts of maximizers, and the upper bounds are numerical results of the census, not kernel-checked; an upper-bound certificate at these widths would need `2^14` to `2^18` chunk checks.
- Nothing about any other width; `Q01` for every width is untouched. No law of `D(W)` is claimed.

## Provenance

The GPU lane engine (P1) and the censuses (P1b, P1c) of the Wolfram · Collatz · Mahler record, an open research record kept on GitHub by Gareth Herbert with Claude and GPT (CHAT-LEDGER.md L863 to L868, 2026-10-24). GPT (OpenAI) reviewed the engine's source and its controls before the width-64 census and the census runner afterwards; the censuses at widths 66 to 72 were run by Claude on the owner's direction. The module passes the kit's `Check.lean` on commit cc1e0e0 with Lean v4.35.0 on the M5: five headlines found and correct, axioms `propext` and `Quot.sound` only, no new axioms, 52 constants replayed.

## References

[1] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[2] Wolfram Institute, [*Rule30PrizeKit*](https://github.com/WolframInstitute/Rule30PrizeKit), the reference Lean environment, commit cc1e0e0, 2026: `Rule30ZeroBoundary`, `Rule30ZeroBoundarySmall`, `Rule30ZeroBoundaryLanes`, `Rule30ZeroBoundaryWidth52`.

[3] The Wolfram · Collatz · Mahler record, [github.com/ghywel/placego](https://github.com/ghywel/placego): `tests/probes/wolfram/p1_engine/`, `p1_lane_engine.py`, `p1b_census64.py`, `p1c_census.py`, `d5_lower_submission.py` and CHAT-LEDGER.md L863 to L868, 2026.
