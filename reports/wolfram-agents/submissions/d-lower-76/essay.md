---
Template: ComputationalEssay
Name: A death-time lower bound at width 76, with a witness from a complete GPU census
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-24
Description: A partial result on the kit's Q01 (the zero-boundary reduction of the period-2 question, Problem 1 of the Rule 30 Prize), proved in Lean against the kit's own definitions: an explicit start gives the lower bound D(76) >= 138 on the death time, at a width where the kit, at its pinned commit cc1e0e0, has no statement.
Abstract: Write D(W) for the largest, over zero-boundary starts supported at depths at most W, of the first even time at which the depth-1 cell is white. At the pinned kit commit cc1e0e0, the kit proves D(52) <= 96 and has no statement above width 52; our submissions R30-20261024-b16332 and R30-20261024-a129c3 proved D(64) >= 116 to D(74) >= 134. A complete numerical GPU census of the 2^38 reconstructed starts surviving the even times below width 76 found the maximum D(76) = 138, attained by 64 starts; earlier deaths cannot exceed the exhibited value, which is greater than the width. This module proves the lower bound in Lean: an explicit start, one of the census maximizers, is black at depth 1 at every even time below 138 and white at it, by the kit's prun and run_toFun (headline Rule30Submission.width76_lower). Maximality and the maximizer count are numerical, not proved here.
Keywords: [rule 30, Rule 30 Prize, Problem 1, Q01, zero boundary, death time, lower bound, witness, GPU census, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record, CHAT-LEDGER.md L889 to L895](https://github.com/ghywel/placego/blob/main/CHAT-LEDGER.md)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[wolframcollatzmahler.com](https://www.wolframcollatzmahler.com)", "[Submission R30-20261024-b16332, D(64) >= 116 to D(72) >= 130](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261024-b16332)", "[Submission R30-20261024-a129c3, D(74) >= 134](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261024-a129c3)"]
---

## The question

The kit reduces the period-2 question of Problem 1 to `Q01`: every finite start of the zero-boundary left half, driven by the clock at column 0, has a white cell at depth 1 at some even time. Write `D(W)` for the largest, over starts supported at depths 1 to `W`, of the first even time at which the depth-1 cell is white; `Q01` says `D(W)` is finite for every `W`. The kit at the pinned commit cc1e0e0 proves `D(52) <= 96` by 256 kernel-checked chunk computations and has nothing above width 52. Our earlier submissions proved `D(52) = 96` and `D(56) = 100` exactly, and lower bounds at widths 64 to 74. This essay proves one more: `D(76) >= 138`.

## The zero-boundary half-line

A start is a row of cells at depths `1, 2, 3, …`; depth `k` sits at position `-k`, so depth `k + 1` is the left neighbour of depth `k` and the wall at depth 0, always white, is the right neighbour of depth 1. Rule 30 then reads `new(k) = old(k + 1) xor (old(k) or old(k - 1))` for `k >= 1`, with `new(0) = false`. The kit's `Rule30ZeroBoundarySmall` packs a row into a natural number (bit `j` is depth `j + 1`) and steps it by `pstep r = (r >>> 1) xor (r ||| (r <<< 1))`; its theorem `run_toFun` says this packed orbit is the physical evolution `zrow`. The same step in the Wolfram Language:

```wl
pstep[r_] := BitXor[BitShiftRight[r, 1], BitOr[r, BitShiftLeft[r, 1]]];
orbit[r_, n_] := NestList[pstep, r, n];
depth1[r_, n_] := BitAnd[#, 1] & /@ orbit[r, n];
```

The witness, as a number whose bits are the depths, and its bit length (at most the width):

```wl
w76 = 16^^5bf46e334109c62aaab;
BitLength /@ {w76}
```

The first even time at which depth 1 is white:

```wl
firstEvenWhite[r_, n_] := First[Select[Range[0, n, 2], depth1[r, n][[# + 1]] == 0 &]];
firstEvenWhite[#, 138] & /@ {w76}
```

The orbit of `w76` for 140 steps, depth 1 at the left:

```wl
rows = Reverse[IntegerDigits[#, 2, 224]] & /@ orbit[w76, 140];
ArrayPlot[rows, ImageSize -> 600, Frame -> False]
```

## The Lean module

LeanLink and the kit:

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

The module imports the kit, defines the witness, proves it is below `2^76` (so supported at depths at most 76), evaluates its packed orbit at every even time below the bound by `decide +kernel` and at the bound itself, and bridges to `zrow` by the kit's `run_toFun`:

```wl
rule30Submission = LeanImportString["import Rule30PrizeKit
import Ruliology.CellularAutomata.Rule30ZeroBoundarySmall

/-!
# A death-time lower bound at width 76: an explicit witness from a complete GPU census

**Partial result on the kit's `Q01` (the period-2 question, Problem 1 of the Rule 30 Prize), proved against the kit's own
definitions.** Write `D(W)` for the largest, over zero-boundary starts supported at depths at most `W`, of the first even time at
which the depth-1 cell is white. The kit at the pinned commit cc1e0e0 proves `D(52) <= 96` (`Rule30ZeroBoundaryWidth52`) and has no
statement at any width above 52; submissions R30-20261024-b16332 and R30-20261024-a129c3 proved `D(64) >= 116` to `D(74) >= 134`. This module proves
`D(76) >= 138`: an explicit start, supported at depths at most 76, is black at depth 1 at every even time below the bound and white
at the bound, by the kit's packed evaluator `prun` and its bridge `run_toFun` (`width76_lower`).

**Where the witness comes from.** A complete numerical census on a GPU of every reconstructed start of width 76 that survives the
even times below 76 (every maximizer lies among them, since the value exceeds 76) found this value to be the maximum, the witness
attaining it. The engine is an exact lane engine in Metal; a batch of 2^24 starts and every chunk holding a maximizer were checked
against an independent CPU evaluation of the kit's lane check, and samples of further starts and every maximizer were re-simulated by
a scalar evaluator. The census is numerical; this module proves only the lower bound.

**The argument** is a kernel computation and the kit's own lemmas: `w < 2 ^ W` by `decide`; `toFun w k = false` beyond the width
by the kit's `testBit_ge_of_lt`; the packed orbit `prun w (2 s)` tested at depth 1 for every `s < D / 2` by `decide +kernel`;
`zrow (toFun w) t 1 = (prun w t).testBit 0` by the kit's `run_toFun`.

**Provenance.** The Wolfram · Collatz · Mahler record (github.com/ghywel/placego, CHAT-LEDGER.md L889 to L895, 2026-10-24).
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

/-! ## Width 76: `D(76) >= 138` -/

/-- The width-76 witness (75 bits; bits are depths 1 .. 76). -/
def w76 : Nat := 0x5bf46e334109c62aaab

theorem w76_lt : w76 < 2 ^ 76 := by decide

/-- Black at depth 1 at every even time below 138: 69 packed orbits. -/
theorem w76_black : ∀ s, s < 69 → (prun w76 (2 * s)).testBit 0 = true := by decide +kernel

/-- White at 138: the physical death of `w76`. -/
theorem w76_white : (prun w76 138).testBit 0 = false := by decide +kernel

theorem w76_survives : ∀ t, t < 138 → t % 2 = 0 → zrow (toFun w76) t 1 = true :=
  survives_of_black w76_black rfl

theorem w76_dies : zrow (toFun w76) 138 1 = false := by
  rw [zrow_packed]; exact w76_white

/-- **A lower bound at width 76:** a start supported at depths at most 76 with no even white time below 138. -/
theorem width76_lower :
    ∃ x : Nat → Bool, (∀ k, 76 < k → x k = false) ∧ (∀ t, t < 138 → t % 2 = 0 → zrow x t 1 = true) :=
  ⟨toFun w76, toFun_width w76_lt, w76_survives⟩

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

The environment loads:

```wl
Head[rule30Submission]
```

## The headline theorem

The lower bound:

```wl
opens = {"Ruliology.CellularAutomata.Rule30ZeroBoundary", "Ruliology.CellularAutomata.Rule30ZeroBoundarySmall", "Rule30Submission"};
thm = rule30Submission["Rule30Submission.width76_lower"];
rule30Submission["Rule30Submission." <> #]["TypeForm", "Open" -> opens] & /@ {"width76_lower"}
```

The axioms behind the headline, which must be standard:

```wl
rule30Submission["Rule30Submission." <> #]["Axioms"] & /@ {"width76_lower"}
```

The witness's survival and death, as the kernel evaluated them (black at every even time below 138; white at 138):

```wl
{rule30Submission["Rule30Submission.w76_survives"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.w76_dies"]["TypeForm", "Open" -> opens]}
```

The module's two bridge lemmas, from the kit's `run_toFun` and `testBit_ge_of_lt`:

```wl
{rule30Submission["Rule30Submission.zrow_packed"]["TypeForm", "Open" -> opens], rule30Submission["Rule30Submission.toFun_width"]["TypeForm", "Open" -> opens]}
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
thm["KernelCheck"]
```

## Where the witness comes from: a complete GPU census (numerical)

Every start of width at most 76 that survives the even times below 76 is fixed by its 38 odd trace bits (the kit's free bits), and every maximizer of `D(76)` is among them, because the value found exceeds 76 and a start dying earlier cannot reach it. The exact lane engine on the GPU (Metal, 32 starts per machine word) of our width-64 to width-74 submissions reconstructed and evolved all `2^38` (274.9 billion) of these surviving starts, about 79 minutes of GPU, not all `2^76` bit strings, which the reduction makes unnecessary. A batch of 16,777,216 starts was compared lane for lane with an independent CPU evaluation of the kit's own lane check (`Rule30ZeroBoundaryLanes.check`), with 64 further starts per batch of 2^24 re-simulated by a scalar evaluator; the 40 maximizers at width 64 and the 178 at width 74, carried to width 76, each died at its known time (116 and 134). Every maximizer was re-simulated by the scalar evaluator, and the CPU evaluation of the kit's check was run on every chunk holding one, finding exactly the same maximizers there. The remaining starts rest on the GPU engine and those samples; they did not each receive an independent CPU replay.

| width W | census maximum | starts attaining it | proved here |
|---|---|---|---|
| 76 | 138 | 64 | D(76) >= 138 |

With the exact values of earlier submissions (`D(52) = 96`, `D(56) = 100`), our width-60 certificate (`D(60) = 114`) and our lower bounds at widths 64 to 74, the table reads 96, 100, 114, 116, 120, 122, 124, 130, 134, 138 at widths 52 to 76: `D(W)/W` stays between 1.77 and 1.90. The maximizers at width 76 lie in 3 blocks of 4,096 consecutive indices.

## What is not proved

- Only the lower bound is proved here. That the witness is a maximum, the count of maximizers, and the upper bound are numerical results of the census, not kernel-checked; an upper-bound certificate at this width would need `2^20` chunk checks.
- Nothing about any other width; `Q01` for every width is untouched. No law of `D(W)` is claimed.

## Provenance

The GPU lane engine (P1) and the width-76 census (P1c) of the Wolfram · Collatz · Mahler record, an open research record kept on GitHub by Gareth Herbert with Claude and GPT (CHAT-LEDGER.md L889 to L895, 2026-10-24). GPT (OpenAI) reviewed the engine's source and the census runner, and accepted the width-76 census before it ran; Claude ran it on the M5. The module passes the kit's `Check.lean` on commit cc1e0e0 with Lean v4.35.0 on the M5: the headline found and correct, standard axioms only, no new axioms, N constants replayed.

## References

[1] S. Wolfram, [*Announcing the Rule 30 Prizes*](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), Wolfram Writings, 2019.

[2] Wolfram Institute, [*Rule30PrizeKit*](https://github.com/WolframInstitute/Rule30PrizeKit), the reference Lean environment, commit cc1e0e0, 2026: `Rule30ZeroBoundary`, `Rule30ZeroBoundarySmall`, `Rule30ZeroBoundaryLanes`, `Rule30ZeroBoundaryWidth52`.

[3] The Wolfram · Collatz · Mahler record, [github.com/ghywel/placego](https://github.com/ghywel/placego): `tests/probes/wolfram/p1_engine/`, `p1_lane_engine.py`, `p1c_census.py`, `d5_lower_submission.py`, `d7_lower_submission.py` and CHAT-LEDGER.md L889 to L895, 2026.
