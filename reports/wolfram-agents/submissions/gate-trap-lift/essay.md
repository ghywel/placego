---
Template: ComputationalEssay
Name: At Eighteen Columns the Gate Trap Forbids 3535353, and Q01GapWords Weakens to Q01GapCore
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-09
Description: Core Lean. The kit's gate trap, lifted by two columns, never shows the gap word 3535353 after entry, for every right half that enters; the sixteen-column graph does read it. So Q01GapWords weakens to Q01GapCore, which still gives CQ01 for trapped right halves and CQ01Empty. Open.
Abstract: For period 2 of rule 30 the kit drives a right half R with the alternating center and reads u R, column 1 at odd times. Its gate trap of 829 sixteen-column windows is closed under the double step. After entry, the kit module Rule30GateTrapWords excludes the gap words 333, 3353, 3533, 3553 and 5533; the trap's graph does read 3535353. We lift the trap by two columns: an 18-column window whose first sixteen cells are in the trap stays so under the double step. In that lift we prove in core Lean that after entry u R never reads 3535353, for every right half that enters the trap. The word is minimal for the lift, and an explicit path shows that the sixteen-column graph reads it. The kernel checks the path sets from all 752 black lift windows in chunks. The open Q01GapWords therefore weakens to Q01GapCore, which also excludes 3535353 and still gives CQ01 for trapped right halves and CQ01Empty. Separately, checked automata at widths 24, 26 and 28 have infinite minimal-forbidden bases; no all-width conclusion is claimed. Q01GapCore remains open.
Keywords: [rule 30, Rule 30 Prize, period two, gate trap, gap words, lift, right half, CQ01, Q01Gap, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[lhallee/rule30-open](https://github.com/lhallee/rule30-open)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261109-897fd1: the gate trap forbids five gap words](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261109-897fd1)", "[R30-20261030-60990f: an all-time forbidden return-gap pattern](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261030-60990f)"]
---

## 1. The statement

For period `2` the kit drives a right half `R` with the alternating center column and reads `u R s`, column `1` at the odd time `2 s + 1`. Its gate trap (`Rule30GateTrap`) is a set of `829` windows of the columns `1..16`, closed under the double step whatever column `17` does. After the window of `R` enters it, the black cells of `u R` come `3` or `5` steps apart (`gaps_of_entry`). The kit module `Rule30GateTrapWords` (submission R30-20261109-897fd1) adds five gap words that never occur after entry: `333`, `3353`, `3533`, `3553` and `5533`. By computation these form the complete minimal-forbidden basis of the trap's own graph. It also weakens the kit's open `Q01Gap` to `Q01GapWords`.

The sixteen-column graph does read `3535353`. This module looks two columns further and excludes it.

- `no_3535353_of_entry`: once the window of `R` is in the trap at an odd time `t0`, `u R` never reads the gap word `3, 5, 3, 5, 3, 5, 3` from a step `s` with `t0 ≤ 2 s + 1`.
- `trap_reads_3535353`: an explicit path of the sixteen-column trap graph reads it, so the trap alone cannot exclude it.
- `lift_minimal_paths`: it is minimal for the eighteen-column lift. Removing its first or its last gap gives `535353` or `353535`, and an explicit path of the lift reads each.
- `Q01GapCore` (open) is `Q01GapWords` with `3535353` excluded as well. `Q01GapWords` implies it (`Q01GapCore_of_Q01GapWords`). It still gives `¬ FinSupp (Psi R)` for every right half whose window enters the trap (`not_finSupp_Psi_of_Q01GapCore`), and so `CQ01Empty` (`CQ01Empty_of_Q01GapCore`).

## 2. The lift

An 18-column window at an odd time is the window of `Rule30GateTrap` followed by the columns `17` and `18` (`win18_eq`). From an odd time, the window two steps later is the kit's double step `step2` applied to the 18-column window, with the two values of column `19` as its exterior inputs (`win18_step2`). A window whose first sixteen cells lie in the trap keeps that property, because those sixteen cells move by the trap's own double step. So the lift (`829 × 4 = 3,316` windows) is closed. Every right half in the trap has its 18-column window in the lift at every later odd time. The lift sees more than the trap: column `17` is now part of the window rather than a free input.

## 3. The check

The method is that of `Rule30GateTrapWords`. For the `28` samples of `3535353`, the layer `Lₖ` holds the lift windows that can have read its first `k + 1` samples, starting from all `752` black lift windows. The layers have `752, 589, 563, 176, 192, 192, 147, 157, 202, 234, 247, 92, 92, 89, 90, 86, 116, 140, 150, 43, 48, 43, 37, 30, 33, 46, 58` and `0` windows. The kernel checks three facts (`wordCheck18`, `not_reads18_of_check`):
- every black lift window is in `L₀`;
- every double step from `Lₖ₋₁` that reads the next sample lands in `Lₖ`;
- the last layer is empty.

Each layer is split into chunks of at most `192` windows, and each chunk is its own kernel check. That keeps the kernel's caches small: the portal form builds in about a minute at under `1.5` GB on an M5.

In the sixteen-column trap the same word keeps `47` windows at its last sample. That is exactly where the trap alone stops seeing.

## 4. The wider picture, by computation

The lift can be repeated at every even width. The following is context, with each status as stated, and is not part of the Lean.

- **The long-run language at each width** is the gap language read from the lift's recurrent core: the black windows with arbitrarily long pasts. It was computed exactly at widths `16` to `30` by Local and replayed independently by GPT to `28` (COMPUTED). Its minimal forbidden words are exactly `33, 3553` at `16` and `33, 3553, 3535353` at `18` to `22`. At the checked widths `24`, `26` and `28` they are infinitely many: an explicit family `35553 (53535555355553)^k 535355553555353`, `k ≥ 0`, is minimal forbidden at `24` (PROVED by both workers, conditional on the computed automata). Those three gap languages are sofic but not of finite type; no classification at every larger width is claimed.
- **Its entropy** falls from `0.1325` (`16`) to `0.1271` (`18`–`22`), `0.1269` (`24`), `0.1255` (`26`), `0.1222` (`28`) and `0.1192` (`30`) bit per sample. GPT bracketed the values to `28` by exact integer inequalities; the value at `30` is a numerical estimate.
- **A conditional floor.** A minimal forbidden word other than `33` and `3553` always contains `353` exactly when every concatenation of the blocks `5` and `3555` is in the language (PROVED by both workers). If that holds at every width, every relaxed entropy is at least `log₂ λ ≈ 0.099056147` bit per sample, where `λ > 1` solves `λ⁻⁵ + λ⁻¹⁸ = 1`. All-width inclusion remains open. The code statement and this entropy bound are not proved by the present Lean module.

## 5. Worked numbers

The cell below reads the trap's `829` codes from the kit and builds the 18-column lift. It counts the double steps that stay inside, and gives the layer sizes of `3535353` in the trap and in the lift. It then lists the minimal forbidden gap words of up to eight gaps at both widths.

```wl
trapSource = Import[FileNameJoin[{Environment["RULE30PRIZE_KIT"], "lean", "Ruliology", "CellularAutomata", "Rule30Certificates", "GateTrap.lean"}], "Text"];
trap = ToExpression /@ StringCases[First[StringCases[trapSource, "def trapCodes : List Nat := [" ~~ Shortest[c__] ~~ "]" :> c]], DigitCharacter ..];
lift = Flatten[Table[BitOr[t, BitShiftLeft[h, 16]], {t, trap}, {h, 0, 3}]];
inLift = AssociationThread[lift -> True];
step[s_, c_, x_, w_] := With[{e = BitOr[s, BitShiftLeft[x, w]]}, BitAnd[BitXor[BitOr[BitShiftLeft[e, 1], c], BitOr[e, BitShiftRight[e, 1]]], 2^w - 1]];
succ[s_, w_] := Union[step[step[s, 0, #1, w], 1, #2, w] & @@@ Tuples[{0, 1}, 2]];
closed = Count[Flatten[Table[step[step[x, 0, a, 18], 1, b, 18], {x, lift}, {a, 0, 1}, {b, 0, 1}]], v_ /; KeyExistsQ[inLift, v]];
bits[g_] := Join[{1}, Flatten[Append[ConstantArray[0, # - 1], 1] & /@ g]];
sizes[start_, w_, word_] := Module[{S = Select[start, BitAnd[#, 1] == First[word] &], out}, out = {Length[S]}; Do[S = Select[Union[Flatten[succ[#, w] & /@ S]], BitAnd[#, 1] == y &]; AppendTo[out, Length[S]], {y, Rest[word]}]; out];
gap[S_, g_, w_] := Module[{T = S}, Do[T = Select[Union[Flatten[succ[#, w] & /@ T]], BitAnd[#, 1] == Boole[k == g] &], {k, g}]; T];
minimal[start_, w_, nmax_] := Module[{allowed = <|{} -> Select[start, OddQ]|>, forbidden = {}}, Do[Do[With[{T = gap[allowed[u], g, w]}, If[T === {}, AppendTo[forbidden, Append[u, g]], allowed[Append[u, g]] = T]], {u, Select[Keys[allowed], Length[#] == n - 1 &]}, {g, {3, 5}}], {n, nmax}]; SortBy[Select[forbidden, KeyExistsQ[allowed, Rest[#]] &], {Length, Identity}]];
word = bits[{3, 5, 3, 5, 3, 5, 3}];
{Length[lift], closed, sizes[trap, 16, word], sizes[lift, 18, word], minimal[trap, 16, 8], minimal[lift, 18, 8]}
```

## 6. Prior art and scope

The trap, `gaps_of_entry`, `Q01Gap` and the method are the kit's `Rule30GateTrap` and `Rule30Certificates.GateTrap` (R. Bosdure, R30-20261027-230bc7). The five words and `Q01GapWords` are the kit's `Rule30GateTrapWords` (R30-20261109-897fd1, ours).

- [R30-20261030-60990f](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261030-60990f) (J. Lee, with GPT and Claude) proves in Lean that `33`, `3553` and `3535353` never occur at any index for the trajectories of an invariant pool of `2,040` windows of `18` cells, among them the one-cell right seed. The premise here is entry into the kit's whole trap, whose transients can read `33` once; the two premises are different.
- Our own earlier computation (6 November) found that inside the kit's trap `3535353` never occurs. It named the weaker left statement that `Q01GapCore` formalizes here.
- [`lhallee/rule30-open`'s gate census](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/findings/period-two/gate-census.md) computes a gap trap of windows with a counter, which the kit's trap reaches at its next black sample.

What is new here is `3535353` in Lean for every right half that enters the kit's trap, its minimality for the lift, and `Q01GapCore` with its reductions. GPT found the infinite forbidden family and certified the entropy brackets. Claude found `3535353`'s death at eighteen columns, the equivalence with the block code, and wrote the module. Nothing here proves `Q01Gap`, `Q01GapWords`, `Q01GapCore`, `CQ01`, `CQ01Empty` or the absence of period `2`.

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the kit's `Rule30GateTrap`. Because the verifier's kit predates `Rule30GateTrapWords`, the module first repeats that module's reviewed source verbatim, then adds the eighteen-column lift.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30GateTrap

/-!
# The gate trap at eighteen columns: `3535353` never occurs after entry

The kit module `Rule30GateTrapWords` (Rule 30 Prize submission R30-20261109-897fd1) shows that
after the window of a right half `R` enters the gate trap of `Rule30GateTrap`, `u R` never reads
the gap words `333`, `3353`, `3533`, `3553` and `5533`.
These are all that the trap's own graph of sixteen-column windows forbids, and
that graph does read `3535353` (`trap_reads_3535353`). This module looks two columns further: an
18-column window whose first sixteen cells are a window of `trap` stays such a window under the
double step, with column `19` free (`win18_step2`), and in that lift no path reads `3535353`.

* `no_3535353_of_entry`: if the window of `R` is in `trap` at an odd time `t0`, then from every step
  `s` with `t0 ≤ 2 s + 1`, `u R` never reads `3, 5, 3, 5, 3, 5, 3`.
* `lift_minimal_paths`: it is minimal for the lift: `353535` and `535353` are read along explicit
  paths of the lift.
* `Q01GapCore` (**open**) is `Q01GapWords` with `3535353` excluded as well: it follows from
  `Q01GapWords` (`Q01GapCore_of_Q01GapWords`), and it still gives `¬ FinSupp (Psi R)` for every
  right half whose window enters the trap (`not_finSupp_Psi_of_Q01GapCore`), hence `CQ01Empty`
  (`CQ01Empty_of_Q01GapCore`).

The method is that of `Rule30GateTrapWords` (`wordCheck18`, `not_reads18_of_check`): the path sets
of the word in the lift, starting from every black lift window, are given as data, with one kernel
check per sample and per chunk of at most 192 windows. Nothing here decides `CQ01`, `Q01Gap`,
`Q01GapWords`, `Q01GapCore` or Problem 1.

The portal's verifier kit predates `Rule30GateTrapWords`, so this module first repeats that
module's reviewed source verbatim, and then adds the eighteen-column part.
-/

-- Sequential elaboration: the kernel checks would otherwise run in parallel and stack their memory.
set_option Elab.async false

namespace Rule30Submission

open Ruliology.CellularAutomata Rule30StripCertificates Rule30GateTrap Rule30ZeroBoundary

/-! ## Gap words -/

/-- The samples of a gap word: a black cell, then for each gap `g` the `g - 1` white cells and the
next black cell. So `gapWord [3, 5]` is `1, 0, 0, 1, 0, 0, 0, 0, 1`. -/
def gapWord : List Nat → List Bool
  | [] => [true]
  | g :: gs => true :: (List.replicate (g - 1) false ++ gapWord gs)

/-- `v` reads the word `w` from the step `s`. -/
def Reads (v : Nat → Bool) (s : Nat) (w : List Bool) : Prop :=
  ∀ i, i < w.length → v (s + i) = w.getD i false

theorem reads_take {v : Nat → Bool} {s : Nat} {w : List Bool} (h : Reads v s w) (n : Nat) :
    Reads v s (w.take n) := by
  intro i hi
  rw [List.length_take] at hi
  rw [h i (by omega), List.getD_eq_getElem?_getD, List.getD_eq_getElem?_getD,
    List.getElem?_take_of_lt (by omega)]

theorem reads_drop {v : Nat → Bool} {s : Nat} {w : List Bool} (h : Reads v s w) (k : Nat) :
    Reads v (s + k) (w.drop k) := by
  intro i hi
  rw [List.length_drop] at hi
  rw [Nat.add_assoc, h (k + i) (by omega), List.getD_eq_getElem?_getD, List.getD_eq_getElem?_getD,
    List.getElem?_drop]

/-! ## Windows by their codes -/

theorem seg_testBit_encList : ∀ (w : List Bool), seg (fun i => (encList w).testBit i) w.length = w
  | [] => rfl
  | x :: l => by
    have h0 : (encList (x :: l)).testBit 0 = x := by
      cases x <;> simp [encList] <;> omega
    have h1 : (fun i => (encList (x :: l)).testBit (i + 1)) = (fun i => (encList l).testBit i) := by
      funext i
      rw [Nat.testBit_succ]
      congr 1
      cases x <;> simp [encList] <;> omega
    show (encList (x :: l)).testBit 0 ::
      seg (fun i => (encList (x :: l)).testBit (i + 1)) l.length = x :: l
    rw [h0, h1, seg_testBit_encList l]

theorem decode_encList {w : List Bool} (hw : w.length = 16) : decode (encList w) = w := by
  have := seg_testBit_encList w
  rw [hw] at this
  exact this

/-- A list of codes as a bitmap: bit `n` is set for each code `n` of the list. -/
def maskN : List Nat → Nat
  | [] => 0
  | n :: rest => 2 ^ n ||| maskN rest

theorem maskN_spec : ∀ (L : List Nat) (n : Nat), (maskN L).testBit n = true → n ∈ L
  | [], n, h => by simp [maskN] at h
  | m :: rest, n, h => by
    simp only [maskN, Nat.testBit_or, Bool.or_eq_true] at h
    rcases h with h | h
    · rw [Nat.testBit_two_pow] at h
      have e : m = n := by simpa using h
      subst e
      exact List.mem_cons_self
    · exact List.mem_cons_of_mem _ (maskN_spec rest n h)

/-- A window whose code is set in the bitmap of a list of codes is in the decoded list. -/
theorem mem_of_maskN {LN : List Nat} {w : List Bool} (hw : w.length = 16)
    (h : inM (maskN LN) w = true) : w ∈ LN.map decode :=
  List.mem_map.2 ⟨encList w, maskN_spec LN _ h, decode_encList hw⟩

/-! ## The word check -/

/-- The windows of `trap` that read `b` in column `1` are in the layer `L`. -/
def startOK (b : Bool) (L : List Nat) : Bool :=
  trap.all (fun w => w.headD false != b || inM (maskN L) w)

/-- One layer: every double step from a window of the layer `S`, for all four values of column `17`,
either does not read `b` in column `1` or lands in the layer `L`. -/
def stepOK (S : List Nat) (b : Bool) (L : List Nat) : Bool :=
  (S.map decode).all (allSucc (fun w => w.headD false != b || inM (maskN L) w))

/-- Reading the letters `word` from the windows `S`. For each letter, every double step from a
window of `S`, for all four values of column `17`, either does not read the letter in column `1` or
lands in the next layer; after the last letter the layer is empty. -/
def readCheck : List Nat → List Bool → List (List Nat) → Bool
  | S, [], _ => S.isEmpty
  | S, b :: rest, L :: Ls => stepOK S b L && readCheck L rest Ls
  | _, _ :: _, [] => false

/-- **The word check.** The windows of `trap` that read the first letter of `word` in column `1`
are in the first layer, and `readCheck` holds from there for the other letters and layers. -/
def wordCheck : List Bool → List (List Nat) → Bool
  | b :: rest, L :: Ls => startOK b L && readCheck L rest Ls
  | _, _ => false

section Driven
variable (R : Nat → Bool)

theorem readCheck_spec : ∀ (word : List Bool) (S : List Nat) (Ls : List (List Nat)),
    readCheck S word Ls = true → ∀ t, t % 2 = 1 → win R t ∈ S.map decode →
      ¬ ∀ i, i < word.length → (win R (t + 2 * (i + 1))).headD false = word.getD i false
  | [], S, Ls, h, t, _, hw, _ => by
    simp only [readCheck, List.isEmpty_iff] at h
    subst h
    simp at hw
  | b :: rest, S, L :: Ls, h, t, ht, hw, hr => by
    simp only [readCheck, stepOK, Bool.and_eq_true] at h
    have hP := win_next R h.1 ht hw
    have hb : (win R (t + 2)).headD false = b := by simpa using hr 0 (by simp)
    rw [hb] at hP
    simp only [bne_self_eq_false, Bool.false_or] at hP
    refine readCheck_spec rest _ Ls h.2 (t + 2) (by omega) (mem_of_maskN (win_length R _) hP) ?_
    intro i hi
    have := hr (i + 1) (by simp; omega)
    rw [show t + 2 + 2 * (i + 1) = t + 2 * (i + 1 + 1) by omega]
    simpa using this
  | _ :: _, _, [], h, _, _, _, _ => by simp [readCheck] at h

/-- **A word check excludes its word after entry.** If `wordCheck word layers` holds and the window
of `R` is in `trap` at an odd time `t0`, then `u R` does not read `word` from any step `s` with
`t0 ≤ 2 s + 1`. -/
theorem not_reads_of_check {word : List Bool} {layers : List (List Nat)}
    (hc : wordCheck word layers = true) {t0 : Nat} (h0 : t0 % 2 = 1) (hw : win R t0 ∈ trap)
    (s : Nat) (hs : t0 ≤ 2 * s + 1) : ¬ Reads (Rule30PeriodTwoSideways.u R) s word := by
  intro hr
  have hw0 : win R (2 * s + 1) ∈ trap := by
    have := win_mem_trap R h0 hw ((2 * s + 1 - t0) / 2)
    rwa [show t0 + 2 * ((2 * s + 1 - t0) / 2) = 2 * s + 1 by omega] at this
  cases word with
  | nil => simp [wordCheck] at hc
  | cons b rest =>
    cases layers with
    | nil => simp [wordCheck] at hc
    | cons L Ls =>
      simp only [wordCheck, startOK, Bool.and_eq_true] at hc
      have hb : (win R (2 * s + 1)).headD false = b := by
        have := hr 0 (by simp)
        rw [u_eq_head] at this
        simpa using this
      have hP := List.all_eq_true.1 hc.1 _ hw0
      rw [hb] at hP
      simp only [bne_self_eq_false, Bool.false_or] at hP
      refine readCheck_spec R rest _ Ls hc.2 (2 * s + 1) (by omega)
        (mem_of_maskN (win_length R _) hP) ?_
      intro i hi
      have := hr (i + 1) (by simp; omega)
      rw [u_eq_head] at this
      rw [show 2 * s + 1 + 2 * (i + 1) = 2 * (s + (i + 1)) + 1 by omega]
      simpa using this

end Driven

/-! ## The layers of the five words -/

/-- The 188 windows of the trap that can have read the samples `1`. -/
def lay1 : List Nat := [103, 407, 679, 871, 1191, 1431, 1639, 1703, 2727, 3479, 3495, 3687, 3751,
    4055, 4503, 4775, 4967, 5527, 5735, 6055, 6103, 6247, 6567, 6823, 7271, 7591, 7847, 8039, 8599,
    8871, 9063, 9383, 9623, 9831, 10919, 11367, 11687, 12391, 12967, 13207, 13719, 13927, 13991,
    14247, 14439, 14759, 15015, 15975, 16039, 16791, 17063, 17255, 17575, 17815, 18023, 19111,
    19879, 20135, 21911, 22119, 22439, 22631, 22951, 23207, 24231, 24423, 24679, 24983, 25255,
    25447, 25767, 26279, 27303, 27751, 28055, 28263, 28631, 28775, 29079, 29351, 29543, 29591,
    29863, 30103, 30311, 30375, 31399, 31847, 32167, 32359, 32871, 33175, 33447, 33639, 33959,
    34199, 34407, 34471, 35495, 36247, 36263, 36455, 36519, 36823, 37271, 37543, 37735, 38295,
    38503, 38823, 38871, 39015, 39335, 39591, 40039, 40359, 40615, 40807, 41367, 41639, 41831,
    42151, 42391, 42599, 43687, 44135, 44455, 45159, 45735, 45975, 46487, 46695, 46759, 47015,
    47207, 47527, 47783, 48743, 48807, 49255, 49415, 49831, 50583, 50791, 50855, 51879, 52631,
    52647, 52839, 52903, 53207, 53655, 54119, 54439, 54679, 54887, 55719, 55975, 56423, 56743,
    56999, 57191, 57447, 57751, 58023, 58215, 58535, 59047, 60071, 60519, 60823, 61031, 61543,
    61847, 62119, 62311, 62359, 62631, 62871, 63079, 63143, 63399, 63591, 63911, 64167, 64615,
    65127, 65191]

/-- The 191 windows of the trap that can have read the samples `10`. -/
def lay10 : List Nat := [142, 398, 654, 1166, 1486, 1562, 1678, 1818, 2190, 2586, 2702, 3534, 3982,
    4238, 4750, 5582, 5914, 6030, 6286, 6362, 6542, 6798, 7310, 7706, 7822, 8334, 8846, 9678,
    10010, 10126, 10382, 10778, 10894, 11662, 12430, 12686, 13262, 13534, 13850, 13966, 14106,
    14222, 14554, 14734, 14990, 15502, 15822, 16014, 16270, 16526, 17038, 17870, 18202, 18970,
    19086, 19854, 20622, 21134, 21966, 22298, 22414, 22746, 22926, 23694, 24090, 24206, 24974,
    25230, 25550, 25742, 26138, 26254, 26510, 27278, 28110, 28558, 28814, 28890, 29326, 29646,
    29838, 30350, 30490, 30606, 30862, 31374, 32538, 32654, 32910, 33166, 33422, 33934, 34254,
    34330, 34446, 34586, 34958, 35354, 35470, 36302, 36750, 37006, 37518, 38350, 38682, 38798,
    39054, 39130, 39310, 39566, 40078, 40474, 40590, 41102, 41614, 42446, 42778, 42894, 43150,
    43546, 43662, 44430, 45198, 45274, 45454, 46030, 46222, 46302, 46618, 46734, 46874, 46990,
    47322, 47502, 47758, 48270, 48590, 48782, 48922, 49038, 49294, 49550, 49806, 50318, 50638,
    50714, 50830, 50970, 51738, 51854, 52622, 52686, 53134, 53390, 53902, 54734, 55066, 55182,
    55438, 55514, 55694, 55950, 56462, 56858, 56974, 57998, 58318, 58510, 58830, 59022, 59162,
    59278, 59930, 60046, 60814, 61326, 61582, 61658, 62094, 62414, 62606, 63118, 63258, 63374,
    63706, 63886, 64142, 64654, 65166, 65306, 65422]

/-- The 186 windows of the trap that can have read the samples `100`. -/
def lay100 : List Nat := [348, 604, 680, 1628, 1692, 2140, 2536, 2652, 3420, 3676, 3752, 4188,
    4700, 5212, 5496, 5788, 5980, 6492, 6632, 6748, 6824, 7848, 8284, 8796, 9308, 9592, 9884,
    10728, 10844, 11868, 11944, 12152, 12380, 12892, 13800, 13916, 13980, 14428, 14684, 14940,
    15016, 15964, 16220, 16476, 16988, 17500, 18076, 18920, 19036, 19804, 20060, 20136, 20836,
    21084, 22172, 22876, 23208, 24040, 24156, 24924, 25180, 25692, 25976, 26088, 26204, 26716,
    27112, 27228, 28316, 28764, 29020, 29276, 29788, 30072, 30184, 30300, 30364, 30812, 31208,
    31324, 32412, 32424, 32604, 32860, 33116, 33372, 33448, 34396, 34460, 34908, 35304, 35420,
    36188, 36444, 36520, 36956, 37468, 37980, 38264, 38556, 38748, 39260, 39400, 39516, 39592,
    40540, 40616, 41052, 41564, 42076, 42360, 42652, 43496, 43612, 44636, 44712, 44920, 45148,
    45404, 45660, 46568, 46684, 46748, 47196, 47452, 47708, 47784, 48732, 48796, 48988, 49244,
    49500, 49756, 49832, 50780, 50844, 51292, 51688, 51804, 52572, 52828, 52892, 52904, 53340,
    53604, 53852, 54364, 54648, 54940, 55644, 55784, 55900, 55976, 56808, 56924, 57000, 57692,
    57948, 58460, 58744, 58856, 58972, 59036, 59484, 59880, 59996, 61020, 61084, 61304, 61532,
    61788, 61796, 62044, 62556, 62840, 62952, 63068, 63132, 63580, 63836, 64092, 64168, 65000,
    65116, 65180, 65372]

/-- The 139 windows of the trap that can have read the samples `1000`. -/
def lay1000 : List Nat := [106, 618, 874, 1130, 1386, 1594, 1898, 2154, 2618, 3434, 4202, 4458,
    4714, 5482, 5994, 6250, 6506, 6714, 7018, 7274, 7738, 8298, 8554, 8810, 10090, 10346, 10602,
    10690, 10810, 11626, 12650, 12906, 13418, 13674, 14442, 15466, 15930, 16490, 17002, 18282,
    18538, 18882, 19002, 19818, 20586, 21098, 21866, 23402, 23658, 23914, 24122, 24938, 25450,
    25706, 25962, 26474, 26730, 29034, 29802, 30266, 30570, 30826, 31290, 32874, 33386, 33642,
    33898, 34154, 34362, 34666, 34922, 35386, 36202, 36970, 37226, 37482, 38250, 38762, 39018,
    39274, 39482, 39786, 40042, 40298, 40506, 41066, 41322, 41578, 42858, 43114, 43370, 43458,
    43578, 44394, 45418, 45674, 46186, 46442, 46650, 47210, 48234, 48698, 49258, 49770, 50026,
    50282, 50538, 50746, 51306, 51650, 51770, 52586, 53354, 53610, 53866, 55146, 55402, 55866,
    56170, 56426, 56682, 56890, 57450, 57706, 58218, 58474, 59242, 59498, 59754, 60778, 61802,
    62058, 62570, 62826, 63034, 63338, 63594, 64618, 65082]

/-- The 68 windows of the trap that can have read the samples `1001`. -/
def lay1001 : List Nat := [871, 1431, 1703, 2727, 3687, 4967, 5527, 6823, 7847, 9063, 10919, 13207,
    13719, 13927, 13991, 15015, 16039, 17255, 17815, 18023, 21911, 22119, 24231, 25447, 26279,
    27303, 28263, 29543, 29591, 30375, 31399, 33639, 34199, 34407, 34471, 35495, 36455, 37735,
    38295, 39591, 40615, 41831, 43687, 45975, 46487, 46695, 46759, 47783, 48807, 50583, 50791,
    50855, 51879, 54119, 54679, 54887, 55975, 58215, 59047, 60071, 61031, 62311, 62359, 62871,
    63079, 63143, 64167, 65191]

/-- The 148 windows of the trap that can have read the samples `10000`. -/
def lay10000 : List Nat := [168, 424, 952, 1400, 1960, 2216, 2424, 2536, 2728, 3496, 3560, 4072,
    4264, 4776, 5608, 6056, 6520, 6568, 7144, 7656, 8168, 8360, 8680, 8872, 9144, 9704, 10152,
    10616, 10728, 12264, 12712, 12968, 13688, 13800, 14504, 15016, 15336, 15736, 15848, 16552,
    17064, 17896, 18344, 18808, 18920, 19880, 20456, 21160, 21992, 22952, 23528, 24040, 25000,
    25064, 25976, 26536, 26792, 27000, 27304, 28136, 28648, 29352, 30072, 30184, 30632, 31096,
    31400, 32232, 32744, 32936, 33192, 33448, 33720, 34168, 34280, 34728, 34984, 35192, 35304,
    35496, 36264, 36328, 36840, 37032, 37544, 38376, 38824, 39288, 39336, 39912, 40424, 40936,
    41128, 41448, 41640, 41912, 42472, 42920, 43384, 43496, 45032, 45480, 45736, 46456, 46568,
    47272, 47784, 48104, 48504, 48616, 49320, 49576, 49832, 50552, 50664, 51368, 51688, 51880,
    52648, 52712, 53224, 53928, 54760, 55208, 55672, 55720, 56296, 56808, 57320, 57512, 57832,
    58744, 59304, 59768, 59880, 60072, 60904, 61416, 62120, 62840, 62952, 63400, 63864, 64168,
    64488, 64888, 65000, 65512]

/-- The 68 windows of the trap that can have read the samples `10010`. -/
def lay10010 : List Nat := [1486, 1678, 2702, 3534, 5582, 5914, 6798, 9678, 10010, 10382, 10894,
    13966, 14106, 15502, 15822, 16014, 17870, 18202, 19086, 21966, 22298, 23694, 24206, 26254,
    27278, 28110, 29838, 30350, 30490, 30862, 31374, 34254, 34446, 35470, 36302, 38350, 38682,
    39566, 42446, 42778, 43150, 43662, 46222, 46734, 46874, 48270, 48590, 48782, 50638, 50830,
    50970, 51854, 52686, 54734, 55066, 55950, 56462, 56974, 58830, 59022, 59162, 60046, 62606,
    63118, 63258, 64142, 64654, 65166]

/-- The 168 windows of the trap that can have read the samples `100001`. -/
def lay100001 : List Nat := [103, 407, 679, 871, 1191, 1639, 1703, 2727, 3479, 3495, 3687, 3751,
    4055, 4503, 4775, 5527, 5735, 6055, 6103, 6247, 6567, 6823, 7271, 7591, 8039, 8599, 8871, 9063,
    9383, 9623, 9831, 10919, 11367, 11687, 12391, 12967, 13719, 13927, 13991, 14247, 14439, 14759,
    15015, 15975, 16791, 17063, 17255, 17575, 17815, 19111, 19879, 20135, 21911, 22119, 22439,
    22631, 22951, 23207, 24231, 24423, 24679, 24983, 25255, 25447, 25767, 26279, 27303, 27751,
    28055, 28263, 28631, 28775, 29079, 29351, 29863, 30103, 30311, 31399, 31847, 32167, 32359,
    32871, 33175, 33447, 33639, 33959, 34199, 34407, 34471, 35495, 36247, 36263, 36455, 36519,
    36823, 37271, 37543, 38295, 38503, 38823, 38871, 39015, 39335, 39591, 40039, 40359, 40615,
    40807, 41367, 41639, 41831, 42151, 42391, 42599, 43687, 44135, 44455, 45159, 45735, 46487,
    46695, 46759, 47015, 47207, 47527, 47783, 48743, 49255, 49831, 50583, 50855, 51879, 52631,
    52647, 52839, 52903, 53207, 53655, 54439, 54679, 54887, 55719, 55975, 56423, 56743, 56999,
    57191, 57447, 57751, 58023, 58215, 58535, 60071, 60519, 60823, 61031, 61543, 61847, 62119,
    62631, 62871, 63079, 63399, 63591, 63911, 64167, 64615, 65127]

/-- The 69 windows of the trap that can have read the samples `100100`. -/
def lay100100 : List Nat := [1628, 1692, 2140, 2652, 3752, 5212, 5788, 6748, 6824, 9308, 9884,
    10844, 11944, 12380, 13980, 15016, 15964, 18076, 19036, 20136, 22172, 23208, 24156, 26204,
    26716, 27228, 28316, 30364, 31324, 32412, 34396, 34460, 34908, 35420, 36520, 37980, 38556,
    39516, 39592, 42076, 42652, 43612, 44712, 45148, 46748, 47784, 48732, 48796, 50780, 50844,
    51292, 51804, 52892, 52904, 54364, 54940, 55900, 55976, 56924, 58972, 59484, 59996, 61084,
    61532, 63132, 64092, 64168, 65116, 65180]

/-- The 171 windows of the trap that can have read the samples `1000010`. -/
def lay1000010 : List Nat := [142, 398, 654, 1166, 1562, 1818, 2190, 2586, 2702, 3534, 3982, 4238,
    4750, 5582, 5914, 6030, 6286, 6362, 6542, 6798, 7310, 7706, 7822, 8334, 8846, 10010, 10126,
    10778, 10894, 11662, 12430, 12686, 13262, 13850, 13966, 14106, 14222, 14554, 14734, 14990,
    15502, 15822, 16014, 16270, 16526, 17038, 18970, 19086, 19854, 20622, 21134, 21966, 22298,
    22414, 22746, 22926, 23694, 24090, 24206, 24974, 25230, 25550, 25742, 26138, 26254, 26510,
    27278, 28110, 28558, 28814, 28890, 29326, 29646, 29838, 30490, 30606, 30862, 31374, 32538,
    32654, 32910, 33166, 33422, 33934, 34330, 34586, 34958, 35354, 35470, 36302, 36750, 37006,
    37518, 38350, 38682, 38798, 39054, 39130, 39310, 39566, 40078, 40474, 40590, 41102, 41614,
    42778, 42894, 43546, 43662, 44430, 45198, 45274, 45454, 46030, 46222, 46618, 46874, 46990,
    47322, 47502, 47758, 48270, 48590, 48782, 48922, 49038, 49294, 49550, 49806, 50318, 50714,
    51738, 51854, 52622, 52686, 53134, 53390, 53902, 54734, 55066, 55182, 55438, 55514, 55694,
    55950, 56462, 56858, 56974, 57998, 58318, 58510, 59022, 59278, 59930, 60046, 60814, 61326,
    61582, 61658, 62094, 62414, 62606, 63258, 63374, 63706, 63886, 64142, 64654, 65166, 65306,
    65422]

/-- The 57 windows of the trap that can have read the samples `1001000`. -/
def lay1001000 : List Nat := [618, 1130, 1594, 1898, 2154, 2618, 4714, 6250, 6714, 7738, 10090,
    10346, 10810, 11626, 15930, 18282, 18538, 19818, 21098, 24122, 25706, 26474, 26730, 30266,
    30826, 31290, 33386, 33898, 34362, 34666, 34922, 35386, 37482, 39018, 39482, 40506, 42858,
    43114, 43578, 44394, 46650, 48698, 50282, 50746, 51306, 52586, 53866, 55402, 55866, 56890,
    58474, 59242, 59498, 60778, 63034, 63594, 65082]

/-- The 17 windows of the trap that can have read the samples `1001001`. -/
def lay1001001 : List Nat := [6823, 7847, 10919, 13991, 16039, 24231, 27303, 31399, 39591, 40615,
    43687, 46759, 48807, 55975, 60071, 64167, 65191]

/-- The 173 windows of the trap that can have read the samples `10000100`. -/
def lay10000100 : List Nat := [348, 604, 680, 1628, 2140, 2536, 2652, 3420, 3676, 3752, 4188, 4700,
    5212, 5496, 5788, 5980, 6492, 6632, 6748, 6824, 7848, 8284, 8796, 9308, 9592, 9884, 10728,
    10844, 11868, 12152, 12380, 12892, 13800, 13916, 13980, 14428, 14684, 14940, 15016, 16220,
    16476, 16988, 17500, 18076, 18920, 19036, 19804, 20060, 21084, 22172, 22876, 23208, 24040,
    24156, 24924, 25180, 25692, 25976, 26088, 26204, 26716, 27112, 27228, 28316, 28764, 29020,
    29276, 29788, 30072, 30184, 30300, 30812, 31208, 31324, 32412, 32424, 32604, 32860, 33116,
    33372, 33448, 34396, 34908, 35304, 35420, 36188, 36444, 36520, 36956, 37468, 37980, 38264,
    38556, 38748, 39260, 39400, 39516, 39592, 40540, 40616, 41052, 41564, 42076, 42360, 42652,
    43496, 43612, 44636, 44920, 45148, 45404, 45660, 46568, 46684, 46748, 47196, 47452, 47708,
    47784, 48796, 48988, 49244, 49500, 49756, 49832, 50780, 50844, 51292, 51688, 51804, 52572,
    52828, 52892, 53340, 53852, 54364, 54648, 54940, 55644, 55784, 55900, 55976, 56808, 56924,
    57000, 57692, 57948, 58460, 58744, 58856, 58972, 59036, 59484, 59880, 59996, 61020, 61084,
    61304, 61532, 61788, 62044, 62556, 62840, 62952, 63068, 63132, 63580, 63836, 64092, 64168,
    65000, 65180, 65372]

/-- The 67 windows of the trap that can have read the samples `10010000`. -/
def lay10010000 : List Nat := [168, 1400, 1960, 2216, 4072, 4776, 5608, 6056, 6520, 8168, 8872,
    10152, 10616, 12264, 13688, 15736, 15848, 16552, 17064, 18344, 18808, 20456, 25976, 26536,
    26792, 27000, 29352, 30072, 30632, 31096, 32232, 32744, 32936, 33448, 34168, 34728, 34984,
    36840, 37544, 38376, 38824, 39288, 40936, 41640, 42920, 43384, 45032, 46456, 48504, 48616,
    49320, 49832, 50552, 51368, 53224, 53928, 55208, 55672, 57320, 58744, 59304, 59768, 62840,
    63400, 63864, 64888, 65000]

/-- The 21 windows of the trap that can have read the samples `10010010`. -/
def lay10010010 : List Nat := [1678, 6798, 10894, 13966, 24206, 26254, 27278, 30350, 31374, 34446,
    39566, 43662, 46734, 50830, 55950, 56974, 59022, 60046, 63118, 64142, 65166]

/-- The 128 windows of the trap that can have read the samples `100001000`. -/
def lay100001000 : List Nat := [106, 618, 874, 1386, 1594, 1898, 2154, 2618, 3434, 4202, 4458,
    4714, 5482, 5994, 6250, 6506, 7018, 7274, 7738, 8298, 8554, 8810, 10090, 10346, 10602, 10810,
    11626, 12650, 12906, 13418, 13674, 14442, 15466, 15930, 16490, 17002, 18282, 18538, 19002,
    19818, 20586, 21098, 21866, 23402, 23658, 23914, 24122, 24938, 25450, 25706, 25962, 26474,
    26730, 29034, 29802, 30266, 30570, 30826, 32874, 33386, 33642, 34154, 34362, 34666, 34922,
    35386, 36202, 36970, 37226, 37482, 38250, 38762, 39018, 39274, 39786, 40042, 40298, 40506,
    41066, 41322, 41578, 42858, 43114, 43370, 43578, 44394, 45418, 45674, 46186, 46442, 46650,
    47210, 48234, 48698, 49258, 49770, 50026, 50538, 50746, 51306, 51770, 52586, 53354, 53610,
    53866, 55146, 55402, 56170, 56426, 56682, 56890, 57450, 57706, 58218, 58474, 59242, 59498,
    59754, 60778, 61802, 62058, 62570, 62826, 63034, 63338, 63594, 64618, 65082]

/-- The 92 windows of the trap that can have read the samples `100100001`. -/
def lay100100001 : List Nat := [103, 407, 679, 1191, 3479, 3495, 3687, 4503, 4775, 5527, 5735,
    6247, 6567, 7591, 8599, 8871, 9383, 9623, 11687, 12391, 12967, 13719, 14439, 14759, 15015,
    17063, 17575, 17815, 19879, 21911, 22119, 22631, 22951, 24679, 24983, 25255, 25767, 27303,
    28055, 28263, 28775, 29079, 30103, 32167, 32871, 33175, 33447, 33959, 34199, 36247, 36263,
    36455, 37271, 37543, 38295, 38503, 39015, 39335, 40359, 41367, 41639, 42151, 42391, 44455,
    45159, 45735, 46487, 47207, 47527, 47783, 49255, 49831, 50583, 52631, 52647, 52839, 53655,
    54679, 54887, 55719, 56743, 57447, 57751, 58023, 58535, 60823, 61031, 61543, 61847, 62871,
    63591, 63911]

/-- The 21 windows of the trap that can have read the samples `100100100`. -/
def lay100100100 : List Nat := [1628, 6748, 10844, 15964, 19036, 24156, 26204, 27228, 31324, 34396,
    35420, 39516, 43612, 48732, 51804, 55900, 56924, 58972, 59996, 64092, 65116]

/-- The 137 windows of the trap that can have read the samples `1000010000`. -/
def lay1000010000 : List Nat := [168, 424, 1400, 1960, 2216, 2424, 2536, 2728, 3496, 3560, 4072,
    4264, 5608, 6056, 6520, 6568, 7144, 7656, 8168, 8360, 8680, 9704, 10152, 10616, 10728, 12264,
    12712, 12968, 13688, 13800, 14504, 15016, 15336, 15736, 15848, 16552, 17064, 17896, 18344,
    18808, 18920, 19880, 20456, 21160, 21992, 22952, 23528, 24040, 25000, 25064, 25976, 26536,
    26792, 27304, 28136, 28648, 30072, 30184, 30632, 31096, 31400, 32232, 32744, 32936, 33192,
    33448, 34168, 34280, 34728, 34984, 35192, 35304, 35496, 36264, 36328, 36840, 37032, 38376,
    38824, 39288, 39336, 39912, 40424, 40936, 41128, 41448, 42472, 42920, 43384, 43496, 45032,
    45480, 45736, 46456, 46568, 47272, 47784, 48104, 48504, 48616, 49320, 49576, 49832, 50552,
    50664, 51368, 51688, 51880, 52648, 52712, 53224, 53928, 54760, 55208, 55672, 55720, 56296,
    56808, 57320, 57512, 57832, 58744, 59304, 59768, 59880, 60072, 60904, 61416, 62120, 62840,
    62952, 63400, 64168, 64488, 64888, 65000, 65512]

/-- The 110 windows of the trap that can have read the samples `1001000010`. -/
def lay1001000010 : List Nat := [142, 398, 654, 1562, 1818, 2586, 2702, 3982, 4238, 4750, 5914,
    6030, 7310, 7706, 8334, 8846, 10010, 10126, 10778, 11662, 12686, 14106, 14222, 14990, 15502,
    16270, 16526, 17038, 18970, 19854, 21134, 22298, 22414, 22926, 23694, 24090, 24974, 25230,
    26138, 26510, 27278, 28558, 28814, 29326, 29838, 30490, 30606, 31374, 32538, 32654, 32910,
    33166, 33422, 34330, 34586, 35354, 35470, 36750, 37006, 37518, 38682, 38798, 39310, 40078,
    40474, 41102, 41614, 42778, 42894, 43546, 43662, 44430, 45454, 46222, 46874, 46990, 47758,
    48270, 48922, 49038, 49294, 49550, 49806, 50714, 51738, 51854, 52622, 53134, 53390, 53902,
    55066, 55182, 55694, 55950, 56462, 56858, 57998, 59278, 59930, 60046, 60814, 61326, 62094,
    62606, 63258, 63374, 64142, 64654, 65306, 65422]

/-- The 18 windows of the trap that can have read the samples `1001001000`. -/
def lay1001001000 : List Nat := [1130, 2154, 6250, 10346, 18538, 25706, 26730, 30826, 33898, 34922,
    39018, 43114, 50282, 51306, 55402, 58474, 59498, 63594]

/-- The 160 windows of the trap that can have read the samples `10000100001`. -/
def lay10000100001 : List Nat := [103, 407, 679, 871, 1191, 1639, 1703, 2727, 3479, 3495, 3687,
    3751, 4503, 5527, 5735, 6055, 6247, 6567, 6823, 7271, 7591, 8039, 8599, 8871, 9063, 9383, 9623,
    9831, 10919, 11367, 11687, 12391, 12967, 13719, 13927, 13991, 14247, 14439, 14759, 15015,
    15975, 16791, 17063, 17255, 17575, 17815, 19111, 19879, 20135, 21911, 22119, 22439, 22631,
    22951, 23207, 24231, 24423, 24679, 24983, 25255, 25447, 25767, 26279, 27303, 27751, 28055,
    28263, 28775, 29079, 29351, 29863, 30103, 30311, 31399, 31847, 32167, 32359, 32871, 33175,
    33447, 33639, 33959, 34199, 34407, 34471, 35495, 36247, 36263, 36455, 36519, 37271, 38295,
    38503, 38823, 39015, 39335, 39591, 40039, 40359, 40615, 40807, 41367, 41639, 41831, 42151,
    42391, 42599, 43687, 44135, 44455, 45159, 45735, 46487, 46695, 46759, 47015, 47207, 47527,
    47783, 48743, 49255, 49831, 50583, 50855, 51879, 52631, 52647, 52839, 52903, 53655, 54439,
    54679, 54887, 55719, 55975, 56423, 56743, 56999, 57191, 57447, 57751, 58023, 58215, 58535,
    60071, 60519, 60823, 61031, 61543, 61847, 62119, 62631, 62871, 63079, 63399, 63591, 63911,
    64167, 64615, 65127]

/-- The 118 windows of the trap that can have read the samples `10010000100`. -/
def lay10010000100 : List Nat := [348, 604, 680, 1628, 2140, 2536, 2652, 3420, 3676, 3752, 4700,
    5980, 6492, 6632, 6748, 6824, 7848, 8796, 10728, 10844, 11868, 12380, 12892, 13800, 13916,
    14428, 14684, 14940, 15016, 16220, 16988, 18920, 19036, 19804, 20060, 21084, 22876, 23208,
    24156, 24924, 25180, 26088, 26204, 26716, 27112, 27228, 29020, 29276, 30184, 30812, 31208,
    31324, 32424, 32604, 33116, 33372, 33448, 34396, 34908, 35304, 35420, 36188, 36444, 36520,
    37468, 38748, 39260, 39400, 39516, 39592, 40540, 40616, 41564, 43496, 43612, 44636, 45148,
    45404, 45660, 46568, 46684, 47196, 47452, 47708, 47784, 48988, 49500, 49756, 49832, 50780,
    51292, 51688, 51804, 52572, 52828, 53852, 55644, 55784, 55900, 55976, 56924, 57000, 57692,
    57948, 58856, 59484, 59880, 59996, 61020, 61532, 61788, 62044, 62952, 63580, 63836, 64092,
    64168, 65372]

/-- The 21 windows of the trap that can have read the samples `10010010000`. -/
def lay10010010000 : List Nat := [1960, 4776, 6056, 8872, 10152, 17064, 18344, 26536, 29352, 30632,
    33448, 34728, 37544, 38824, 41640, 42920, 49832, 53928, 55208, 59304, 63400]

/-- The 159 windows of the trap that can have read the samples `100001000010`. -/
def lay100001000010 : List Nat := [142, 398, 1166, 1562, 1818, 2190, 2586, 2702, 3534, 3982, 4238,
    4750, 5582, 5914, 6030, 6286, 6542, 6798, 7310, 7706, 7822, 8334, 8846, 10010, 10126, 10778,
    10894, 11662, 12430, 12686, 13262, 13850, 13966, 14106, 14222, 14734, 14990, 15502, 15822,
    16014, 16270, 16526, 17038, 18970, 19086, 19854, 20622, 21134, 21966, 22298, 22414, 22926,
    23694, 24090, 24206, 24974, 25230, 25550, 25742, 26138, 26254, 26510, 27278, 28110, 28558,
    28814, 29326, 29646, 29838, 30490, 30606, 30862, 31374, 32538, 32654, 32910, 33166, 33934,
    34330, 34586, 34958, 35354, 35470, 36302, 36750, 37006, 37518, 38350, 38682, 38798, 39054,
    39310, 39566, 40078, 40474, 40590, 41102, 41614, 42778, 42894, 43546, 43662, 44430, 45198,
    45454, 46030, 46222, 46618, 46874, 46990, 47502, 47758, 48270, 48590, 48782, 48922, 49038,
    49294, 49550, 49806, 50318, 50714, 51738, 51854, 52622, 52686, 53134, 53390, 53902, 54734,
    55066, 55182, 55438, 55694, 55950, 56462, 56858, 56974, 57998, 58318, 58510, 59022, 59278,
    59930, 60046, 60814, 61326, 61582, 62094, 62414, 62606, 63258, 63374, 63886, 64142, 64654,
    65166, 65306, 65422]

/-- The 90 windows of the trap that can have read the samples `100100001000`. -/
def lay100100001000 : List Nat := [106, 874, 1386, 1898, 2154, 4202, 4458, 5482, 5994, 6250, 7018,
    7274, 8298, 8554, 10090, 10346, 10602, 11626, 13418, 13674, 14442, 15466, 16490, 18282, 18538,
    19818, 20586, 21866, 23402, 23658, 23914, 24938, 25450, 25706, 25962, 26474, 26730, 29034,
    29802, 30570, 30826, 32874, 33642, 34154, 34666, 34922, 36970, 37226, 38250, 38762, 39018,
    39786, 40042, 40298, 41066, 41322, 42858, 43114, 43370, 44394, 46186, 46442, 47210, 48234,
    49258, 50026, 50538, 51306, 52586, 53354, 53610, 55146, 55402, 56170, 56426, 56682, 57450,
    57706, 58218, 58474, 59242, 59498, 59754, 60778, 61802, 62570, 62826, 63338, 63594, 64618]

/-- The 47 windows of the trap that can have read the samples `100100001001`. -/
def lay100100001001 : List Nat := [871, 1703, 2727, 4967, 6823, 9063, 10919, 13927, 13991, 15015,
    16039, 17255, 18023, 22119, 24231, 25447, 26279, 27303, 29543, 30375, 31399, 33639, 34407,
    34471, 35495, 37735, 39591, 41831, 43687, 46695, 46759, 47783, 48807, 50791, 50855, 51879,
    54119, 54887, 55975, 58215, 59047, 60071, 62311, 63079, 63143, 64167, 65191]

/-- The 29 windows of the trap that can have read the samples `100100100001`. -/
def lay100100100001 : List Nat := [679, 3495, 4775, 6567, 7591, 8871, 11687, 14759, 15015, 17063,
    19879, 22951, 27303, 32167, 33447, 36263, 37543, 39335, 40359, 41639, 44455, 47527, 47783,
    49831, 52647, 55719, 56743, 58023, 63911]

/-- The 161 windows of the trap that can have read the samples `1000010000100`. -/
def lay1000010000100 : List Nat := [348, 604, 680, 1628, 2140, 2536, 2652, 3420, 3676, 3752, 4188,
    4700, 5212, 5788, 5980, 6492, 6632, 6748, 6824, 7848, 8284, 8796, 9308, 9884, 10728, 10844,
    11868, 12380, 12892, 13800, 13916, 13980, 14428, 14684, 14940, 15016, 16220, 16476, 16988,
    17500, 18076, 18920, 19036, 19804, 20060, 21084, 22172, 22876, 23208, 24040, 24156, 24924,
    25180, 25692, 26088, 26204, 26716, 27112, 27228, 28316, 28764, 29020, 29276, 29788, 30184,
    30300, 30812, 31208, 31324, 32412, 32424, 32604, 32860, 33116, 33372, 33448, 34396, 34908,
    35304, 35420, 36188, 36444, 36520, 36956, 37468, 37980, 38556, 38748, 39260, 39400, 39516,
    39592, 40540, 40616, 41052, 41564, 42076, 42652, 43496, 43612, 44636, 45148, 45404, 45660,
    46568, 46684, 46748, 47196, 47452, 47708, 47784, 48796, 48988, 49244, 49500, 49756, 49832,
    50780, 50844, 51292, 51688, 51804, 52572, 52828, 52892, 53340, 53852, 54364, 54940, 55644,
    55784, 55900, 55976, 56808, 56924, 57000, 57692, 57948, 58460, 58856, 58972, 59036, 59484,
    59880, 59996, 61020, 61084, 61532, 61788, 62044, 62556, 62952, 63068, 63132, 63580, 63836,
    64092, 64168, 65000, 65180, 65372]

/-- The 100 windows of the trap that can have read the samples `1001000010000`. -/
def lay1001000010000 : List Nat := [424, 1960, 2536, 2728, 3496, 3560, 4072, 5608, 6056, 6568,
    7144, 7656, 8168, 8680, 9704, 10152, 10728, 12264, 12712, 12968, 13800, 15016, 15336, 15848,
    17064, 17896, 18344, 18920, 19880, 20456, 21160, 21992, 22952, 23528, 24040, 25000, 25064,
    26536, 27304, 28136, 28648, 30184, 30632, 31400, 32232, 32744, 33192, 33448, 34280, 34728,
    35304, 35496, 36264, 36328, 36840, 38376, 38824, 39336, 39912, 40424, 40936, 41448, 42472,
    42920, 43496, 45032, 45480, 45736, 46568, 47784, 48104, 48616, 49576, 49832, 50664, 51688,
    51880, 52648, 52712, 53224, 53928, 54760, 55208, 55720, 56296, 56808, 57320, 57832, 59304,
    59880, 60072, 60904, 61416, 62120, 62952, 63400, 64168, 64488, 65000, 65512]

/-- The 48 windows of the trap that can have read the samples `1001000010010`. -/
def lay1001000010010 : List Nat := [1486, 1678, 2702, 3534, 5582, 6798, 9678, 10382, 10894, 15502,
    15822, 16014, 17870, 19086, 21966, 23694, 24206, 26254, 27278, 28110, 30862, 31374, 34254,
    34446, 35470, 36302, 38350, 39566, 42446, 43150, 43662, 48270, 48590, 48782, 50638, 50830,
    51854, 52686, 54734, 55950, 56462, 56974, 58830, 59022, 60046, 64142, 64654, 65166]

/-- The 40 windows of the trap that can have read the samples `1001001000010`. -/
def lay1001001000010 : List Nat := [654, 2702, 3982, 4750, 6030, 8846, 14222, 14990, 16270, 17038,
    21134, 22414, 25230, 27278, 28558, 29326, 31374, 32654, 33422, 35470, 36750, 37518, 38798,
    41614, 43662, 46990, 47758, 49038, 49806, 51854, 53134, 53902, 55950, 57998, 60046, 61326,
    62094, 63374, 64142, 65422]

/-- The 51 windows of the trap that can have read the samples `10000100001001`. -/
def lay10000100001001 : List Nat := [871, 1703, 2727, 3687, 4967, 6823, 9063, 10919, 13927, 13991,
    15015, 16039, 17255, 18023, 22119, 24231, 25447, 26279, 27303, 28263, 29543, 30375, 31399,
    33639, 34407, 34471, 35495, 36455, 37735, 39591, 41831, 43687, 46695, 46759, 47783, 48807,
    50791, 50855, 51879, 54119, 54887, 55975, 58215, 59047, 60071, 61031, 62311, 63079, 63143,
    64167, 65191]

/-- The 111 windows of the trap that can have read the samples `10010000100001`. -/
def lay10010000100001 : List Nat := [103, 871, 1639, 1703, 2727, 3495, 3687, 5735, 6055, 6247,
    6567, 6823, 7271, 7591, 8039, 8871, 9063, 9831, 10919, 11367, 11687, 12391, 13927, 13991,
    14247, 14439, 14759, 15015, 15975, 17063, 17255, 19111, 19879, 22119, 22439, 22631, 22951,
    24231, 24423, 24679, 25255, 25447, 26279, 27303, 27751, 28263, 28775, 29351, 30311, 31399,
    31847, 32167, 32359, 32871, 33639, 34407, 34471, 35495, 36263, 36455, 38503, 38823, 39015,
    39335, 39591, 40039, 40359, 40615, 40807, 41639, 41831, 42599, 43687, 44135, 44455, 45159,
    46695, 46759, 47015, 47207, 47527, 47783, 48743, 49255, 49831, 50855, 51879, 52647, 52839,
    54887, 55719, 55975, 56423, 56743, 56999, 57191, 57447, 58023, 58215, 60071, 60519, 61031,
    61543, 62119, 63079, 63399, 63591, 63911, 64167, 64615, 65127]

/-- The 48 windows of the trap that can have read the samples `10010000100100`. -/
def lay10010000100100 : List Nat := [1628, 1692, 2140, 2652, 5212, 5788, 6748, 9308, 9884, 10844,
    13980, 18076, 19036, 22172, 26204, 26716, 27228, 28316, 30364, 31324, 32412, 34396, 34460,
    34908, 35420, 37980, 38556, 39516, 42076, 42652, 43612, 46748, 48796, 50780, 50844, 51292,
    51804, 52892, 54364, 54940, 55900, 58972, 59484, 59996, 61084, 63132, 64092, 65180]

/-- The 41 windows of the trap that can have read the samples `10010010000100`. -/
def lay10010010000100 : List Nat := [348, 604, 2652, 4700, 6492, 6748, 8796, 10844, 14684, 14940,
    16988, 19036, 21084, 22876, 24924, 27228, 29020, 31324, 33116, 33372, 35420, 37468, 39260,
    39516, 41564, 43612, 45404, 47452, 47708, 49500, 49756, 51804, 53852, 55644, 55900, 57692,
    57948, 59996, 61788, 63836, 64092]

/-- The 51 windows of the trap that can have read the samples `100001000010010`. -/
def lay100001000010010 : List Nat := [1486, 1678, 2702, 3534, 5582, 6798, 9678, 10382, 10894,
    15502, 15822, 16014, 17870, 19086, 21966, 23694, 24206, 26254, 27278, 28110, 29838, 30862,
    31374, 34254, 34446, 35470, 36302, 38350, 39566, 42446, 43150, 43662, 46222, 48270, 48590,
    48782, 50638, 50830, 51854, 52686, 54734, 55950, 56462, 56974, 58830, 59022, 60046, 62606,
    64142, 64654, 65166]

/-- The 107 windows of the trap that can have read the samples `100100001000010`. -/
def lay100100001000010 : List Nat := [398, 1166, 2190, 2702, 3534, 3982, 4750, 5582, 6030, 6286,
    6542, 6798, 7310, 8846, 10126, 10894, 11662, 12686, 13262, 13966, 14222, 14734, 14990, 15502,
    15822, 16270, 19086, 19854, 21134, 21966, 22414, 22926, 23694, 24206, 24974, 25230, 25550,
    25742, 26254, 26510, 27278, 28110, 28558, 29326, 29646, 29838, 30606, 30862, 31374, 32654,
    33166, 33934, 34958, 35470, 36302, 36750, 37518, 38350, 38798, 39054, 39310, 39566, 40078,
    41614, 42894, 43662, 44430, 45454, 46030, 46222, 46990, 47502, 47758, 48270, 48590, 49038,
    49550, 50318, 51854, 52622, 52686, 53134, 53902, 54734, 55182, 55438, 55694, 55950, 56462,
    56974, 57998, 58318, 58510, 59022, 59278, 60046, 60814, 61326, 62094, 62414, 62606, 63374,
    63886, 64142, 64654, 65166, 65422]

/-- The 51 windows of the trap that can have read the samples `1000010000100100`. -/
def lay1000010000100100 : List Nat := [1628, 1692, 2140, 2652, 5212, 5788, 6748, 9308, 9884, 10844,
    12380, 13980, 18076, 19036, 22172, 26204, 26716, 27228, 28316, 30364, 31324, 32412, 34396,
    34460, 34908, 35420, 37980, 38556, 39516, 42076, 42652, 43612, 45148, 46748, 48796, 50780,
    50844, 51292, 51804, 52892, 54364, 54940, 55900, 58972, 59484, 59996, 61084, 61532, 63132,
    64092, 65180]

/-- The 111 windows of the trap that can have read the samples `1001000010000100`. -/
def lay1001000010000100 : List Nat := [348, 604, 1628, 2140, 2652, 3420, 4188, 4700, 5212, 5788,
    5980, 6492, 6748, 8284, 8796, 9308, 9884, 10844, 12380, 13916, 13980, 14428, 14684, 16220,
    16476, 16988, 17500, 18076, 19036, 19804, 21084, 22172, 22876, 24156, 24924, 25180, 25692,
    26204, 26716, 27228, 28316, 28764, 29020, 29276, 29788, 30812, 31324, 32412, 32604, 32860,
    33116, 33372, 34396, 34908, 35420, 36188, 36956, 37468, 37980, 38556, 38748, 39260, 39516,
    40540, 41052, 41564, 42076, 42652, 43612, 45148, 45404, 46684, 46748, 47196, 47452, 48796,
    48988, 49244, 49500, 49756, 50780, 50844, 51292, 51804, 52572, 52892, 53340, 53852, 54364,
    54940, 55644, 55900, 56924, 57692, 57948, 58460, 58972, 59036, 59484, 59996, 61084, 61532,
    61788, 62044, 62556, 63132, 63580, 63836, 64092, 65180, 65372]

/-- The layers of the gap word `333`, one per sample (188, 191, 186, 68, 68, 69, 17, 21, 21,
0); the last is empty. -/
def layers333 : List (List Nat) := [lay1, lay10, lay100, lay1001, lay10010, lay100100, lay1001001,
    lay10010010, lay100100100, []]

/-- The layers of the gap word `3353`, one per sample (188, 191, 186, 68, 68, 69, 17, 21, 21, 18,
21, 29, 40, 41, 0); the last is empty. -/
def layers3353 : List (List Nat) := [lay1, lay10, lay100, lay1001, lay10010, lay100100, lay1001001,
    lay10010010, lay100100100, lay1001001000, lay10010010000, lay100100100001, lay1001001000010,
    lay10010010000100, []]

/-- The layers of the gap word `3533`, one per sample (188, 191, 186, 68, 68, 69, 57, 67, 92, 110,
118, 47, 48, 48, 0); the last is empty. -/
def layers3533 : List (List Nat) := [lay1, lay10, lay100, lay1001, lay10010, lay100100, lay1001000,
    lay10010000, lay100100001, lay1001000010, lay10010000100, lay100100001001, lay1001000010010,
    lay10010000100100, []]

/-- The layers of the gap word `3553`, one per sample (188, 191, 186, 68, 68, 69, 57, 67, 92, 110,
118, 90, 100, 111, 107, 111, 0); the last is empty. -/
def layers3553 : List (List Nat) := [lay1, lay10, lay100, lay1001, lay10010, lay100100, lay1001000,
    lay10010000, lay100100001, lay1001000010, lay10010000100, lay100100001000, lay1001000010000,
    lay10010000100001, lay100100001000010, lay1001000010000100, []]

/-- The layers of the gap word `5533`, one per sample (188, 191, 186, 139, 148, 168, 171, 173, 128,
137, 160, 159, 161, 51, 51, 51, 0); the last is empty. -/
def layers5533 : List (List Nat) := [lay1, lay10, lay100, lay1000, lay10000, lay100001, lay1000010,
    lay10000100, lay100001000, lay1000010000, lay10000100001, lay100001000010, lay1000010000100,
    lay10000100001001, lay100001000010010, lay1000010000100100, []]

theorem start1 : startOK true lay1 = true := by decide +kernel
theorem step10 : stepOK lay1 false lay10 = true := by
  decide +kernel
theorem step100 : stepOK lay10 false lay100 = true := by
  decide +kernel
theorem step1000 : stepOK lay100 false lay1000 = true := by
  decide +kernel
theorem step1001 : stepOK lay100 true lay1001 = true := by
  decide +kernel
theorem step10000 : stepOK lay1000 false lay10000 = true := by
  decide +kernel
theorem step10010 : stepOK lay1001 false lay10010 = true := by
  decide +kernel
theorem step100001 : stepOK lay10000 true lay100001 = true := by
  decide +kernel
theorem step100100 : stepOK lay10010 false lay100100 = true := by
  decide +kernel
theorem step1000010 : stepOK lay100001 false lay1000010 = true := by
  decide +kernel
theorem step1001000 : stepOK lay100100 false lay1001000 = true := by
  decide +kernel
theorem step1001001 : stepOK lay100100 true lay1001001 = true := by
  decide +kernel
theorem step10000100 : stepOK lay1000010 false lay10000100 = true := by
  decide +kernel
theorem step10010000 : stepOK lay1001000 false lay10010000 = true := by
  decide +kernel
theorem step10010010 : stepOK lay1001001 false lay10010010 = true := by
  decide +kernel
theorem step100001000 : stepOK lay10000100 false lay100001000 = true := by
  decide +kernel
theorem step100100001 : stepOK lay10010000 true lay100100001 = true := by
  decide +kernel
theorem step100100100 : stepOK lay10010010 false lay100100100 = true := by
  decide +kernel
theorem step1000010000 : stepOK lay100001000 false lay1000010000 = true := by
  decide +kernel
theorem step1001000010 : stepOK lay100100001 false lay1001000010 = true := by
  decide +kernel
theorem step1001001000 : stepOK lay100100100 false lay1001001000 = true := by
  decide +kernel
theorem step1001001001 : stepOK lay100100100 true [] = true := by
  decide +kernel
theorem step10000100001 : stepOK lay1000010000 true lay10000100001 = true := by
  decide +kernel
theorem step10010000100 : stepOK lay1001000010 false lay10010000100 = true := by
  decide +kernel
theorem step10010010000 : stepOK lay1001001000 false lay10010010000 = true := by
  decide +kernel
theorem step100001000010 : stepOK lay10000100001 false lay100001000010 = true := by
  decide +kernel
theorem step100100001000 : stepOK lay10010000100 false lay100100001000 = true := by
  decide +kernel
theorem step100100001001 : stepOK lay10010000100 true lay100100001001 = true := by
  decide +kernel
theorem step100100100001 : stepOK lay10010010000 true lay100100100001 = true := by
  decide +kernel
theorem step1000010000100 : stepOK lay100001000010 false lay1000010000100 = true := by
  decide +kernel
theorem step1001000010000 : stepOK lay100100001000 false lay1001000010000 = true := by
  decide +kernel
theorem step1001000010010 : stepOK lay100100001001 false lay1001000010010 = true := by
  decide +kernel
theorem step1001001000010 : stepOK lay100100100001 false lay1001001000010 = true := by
  decide +kernel
theorem step10000100001001 : stepOK lay1000010000100 true lay10000100001001 = true := by
  decide +kernel
theorem step10010000100001 : stepOK lay1001000010000 true lay10010000100001 = true := by
  decide +kernel
theorem step10010000100100 : stepOK lay1001000010010 false lay10010000100100 = true := by
  decide +kernel
theorem step10010010000100 : stepOK lay1001001000010 false lay10010010000100 = true := by
  decide +kernel
theorem step100001000010010 : stepOK lay10000100001001 false lay100001000010010 = true := by
  decide +kernel
theorem step100100001000010 : stepOK lay10010000100001 false lay100100001000010 = true := by
  decide +kernel
theorem step100100001001001 : stepOK lay10010000100100 true [] = true := by
  decide +kernel
theorem step100100100001001 : stepOK lay10010010000100 true [] = true := by
  decide +kernel
theorem step1000010000100100 : stepOK lay100001000010010 false lay1000010000100100 = true := by
  decide +kernel
theorem step1001000010000100 : stepOK lay100100001000010 false lay1001000010000100 = true := by
  decide +kernel
theorem step10000100001001001 : stepOK lay1000010000100100 true [] = true := by
  decide +kernel
theorem step10010000100001001 : stepOK lay1001000010000100 true [] = true := by
  decide +kernel

theorem check333 : wordCheck (gapWord [3, 3, 3]) layers333 = true := by
  rw [show gapWord [3, 3, 3] =
    [true, false, false, true, false, false, true, false, false,
    true] from rfl]
  simp only [layers333, wordCheck, readCheck, start1, step10, step100, step1001, step10010,
    step100100, step1001001, step10010010, step100100100, step1001001001, List.isEmpty_nil,
    Bool.and_self]

theorem check3353 : wordCheck (gapWord [3, 3, 5, 3]) layers3353 = true := by
  rw [show gapWord [3, 3, 5, 3] =
    [true, false, false, true, false, false, true, false, false,
    false, false, true, false, false, true] from rfl]
  simp only [layers3353, wordCheck, readCheck, start1, step10, step100, step1001, step10010,
    step100100, step1001001, step10010010, step100100100, step1001001000, step10010010000,
    step100100100001, step1001001000010, step10010010000100, step100100100001001, List.isEmpty_nil,
    Bool.and_self]

theorem check3533 : wordCheck (gapWord [3, 5, 3, 3]) layers3533 = true := by
  rw [show gapWord [3, 5, 3, 3] =
    [true, false, false, true, false, false, false, false, true,
    false, false, true, false, false, true] from rfl]
  simp only [layers3533, wordCheck, readCheck, start1, step10, step100, step1001, step10010,
    step100100, step1001000, step10010000, step100100001, step1001000010, step10010000100,
    step100100001001, step1001000010010, step10010000100100, step100100001001001, List.isEmpty_nil,
    Bool.and_self]

theorem check3553 : wordCheck (gapWord [3, 5, 5, 3]) layers3553 = true := by
  rw [show gapWord [3, 5, 5, 3] =
    [true, false, false, true, false, false, false, false, true,
    false, false, false, false, true, false, false, true] from rfl]
  simp only [layers3553, wordCheck, readCheck, start1, step10, step100, step1001, step10010,
    step100100, step1001000, step10010000, step100100001, step1001000010, step10010000100,
    step100100001000, step1001000010000, step10010000100001, step100100001000010,
    step1001000010000100, step10010000100001001, List.isEmpty_nil, Bool.and_self]

theorem check5533 : wordCheck (gapWord [5, 5, 3, 3]) layers5533 = true := by
  rw [show gapWord [5, 5, 3, 3] =
    [true, false, false, false, false, true, false, false, false,
    false, true, false, false, true, false, false, true] from rfl]
  simp only [layers5533, wordCheck, readCheck, start1, step10, step100, step1000, step10000,
    step100001, step1000010, step10000100, step100001000, step1000010000, step10000100001,
    step100001000010, step1000010000100, step10000100001001, step100001000010010,
    step1000010000100100, step10000100001001001, List.isEmpty_nil, Bool.and_self]

/-! ## The gap words after entry -/

section Words
variable (R : Nat → Bool)

/-- **The trap never shows `3353`.** If the window of `R` is in `trap` at an odd time `t0`, then
`u R` never reads the gap word `3, 3, 5, 3` from a step `s` with `t0 ≤ 2 s + 1`. -/
theorem no_3353_of_entry {t0 : Nat} (h0 : t0 % 2 = 1) (hw : win R t0 ∈ trap) (s : Nat)
    (hs : t0 ≤ 2 * s + 1) : ¬ Reads (Rule30PeriodTwoSideways.u R) s (gapWord [3, 3, 5, 3]) :=
  not_reads_of_check R check3353 h0 hw s hs

/-- **The five gap words.** If the window of `R` is in `trap` at an odd time `t0`, then from every
step `s` with `t0 ≤ 2 s + 1`, `u R` reads none of the gap words `333`, `3353`, `3533`, `3553` and
`5533`. -/
theorem gap_words_of_entry {t0 : Nat} (h0 : t0 % 2 = 1) (hw : win R t0 ∈ trap) (s : Nat)
    (hs : t0 ≤ 2 * s + 1) :
    ¬ Reads (Rule30PeriodTwoSideways.u R) s (gapWord [3, 3, 3]) ∧
      ¬ Reads (Rule30PeriodTwoSideways.u R) s (gapWord [3, 3, 5, 3]) ∧
      ¬ Reads (Rule30PeriodTwoSideways.u R) s (gapWord [3, 5, 3, 3]) ∧
      ¬ Reads (Rule30PeriodTwoSideways.u R) s (gapWord [3, 5, 5, 3]) ∧
      ¬ Reads (Rule30PeriodTwoSideways.u R) s (gapWord [5, 5, 3, 3]) :=
  ⟨not_reads_of_check R check333 h0 hw s hs, not_reads_of_check R check3353 h0 hw s hs,
    not_reads_of_check R check3533 h0 hw s hs, not_reads_of_check R check3553 h0 hw s hs,
    not_reads_of_check R check5533 h0 hw s hs⟩

/-- **No `33535555` after entry**: it begins with `3353`. -/
theorem no_33535555_of_entry {t0 : Nat} (h0 : t0 % 2 = 1) (hw : win R t0 ∈ trap) (s : Nat)
    (hs : t0 ≤ 2 * s + 1) :
    ¬ Reads (Rule30PeriodTwoSideways.u R) s (gapWord [3, 3, 5, 3, 5, 5, 5, 5]) := by
  intro h
  have h' := reads_take h 15
  rw [show (gapWord [3, 3, 5, 3, 5, 5, 5, 5]).take 15 = gapWord [3, 3, 5, 3] by decide] at h'
  exact no_3353_of_entry R h0 hw s hs h'

/-- **Two gaps of `3` in a row only at the start.** If the window of `R` is in `trap` at an odd time
`t0`, then from a step `s` with `t0 ≤ 2 s + 1`, after any two gaps `x` and `y` (each `3` or `5`,
the only gaps of `gaps_of_entry`) the next two gaps are not both `3`. So from the third black cell
after entry on, no two consecutive gaps are both `3`. -/
theorem no_late_33 {t0 : Nat} (h0 : t0 % 2 = 1) (hw : win R t0 ∈ trap) (s : Nat)
    (hs : t0 ≤ 2 * s + 1) (x y : Nat) (hx : x = 3 ∨ x = 5) (hy : y = 3 ∨ y = 5) :
    ¬ Reads (Rule30PeriodTwoSideways.u R) s (gapWord [x, y, 3, 3]) := by
  intro h
  rcases hy with rfl | rfl
  · rcases hx with rfl | rfl
    · have h' := reads_drop h 3
      rw [show (gapWord [3, 3, 3, 3]).drop 3 = gapWord [3, 3, 3] by decide] at h'
      exact not_reads_of_check R check333 h0 hw (s + 3) (by omega) h'
    · have h' := reads_drop h 5
      rw [show (gapWord [5, 3, 3, 3]).drop 5 = gapWord [3, 3, 3] by decide] at h'
      exact not_reads_of_check R check333 h0 hw (s + 5) (by omega) h'
  · rcases hx with rfl | rfl
    · exact not_reads_of_check R check3533 h0 hw s hs h
    · exact not_reads_of_check R check5533 h0 hw s hs h

end Words

/-! ## A weaker form of `Q01Gap` -/

/-- At `s`, the bit sequence `g` is white, or black with the next black cell at distance `3` or
`5` (`GapOK`), and `g` reads none of the five gap words from `s`. -/
def WordsOK (g : Nat → Bool) (s : Nat) : Prop :=
  GapOK g s ∧ ¬ Reads g s (gapWord [3, 3, 3]) ∧ ¬ Reads g s (gapWord [3, 3, 5, 3]) ∧
    ¬ Reads g s (gapWord [3, 5, 3, 3]) ∧ ¬ Reads g s (gapWord [3, 5, 5, 3]) ∧
    ¬ Reads g s (gapWord [5, 5, 3, 3])

/-- **`Q01GapWords`** (**open**): no finitely supported constrained start of the zero-boundary left
half has free bits whose complement, from some step on, has each black cell followed by the next
one at distance `3` or `5` and reads none of the gap words `333`, `3353`, `3533`, `3553`, `5533`. -/
def Q01GapWords : Prop := ∀ L : Nat → Bool, FinSupp L → InX L →
  ¬ ∃ s0, ∀ s, s0 ≤ s → WordsOK (fun s => !zrow L (2 * s + 1) 1) s

/-- **`Q01Gap` implies `Q01GapWords`**: it excludes more free bits. -/
theorem Q01GapWords_of_Q01Gap (h : Q01Gap) : Q01GapWords := fun L hf hX ⟨s0, hs⟩ =>
  h L hf hX ⟨s0, fun s hs' => (hs s hs').1⟩

/-- **`Q01GapWords` gives `CQ01` for every right half whose window enters the trap**, as `Q01Gap`
does in `not_finSupp_Psi_of_Q01Gap`: the candidate left row `Psi R` has infinitely many black
cells. -/
theorem not_finSupp_Psi_of_Q01GapWords (hQ : Q01GapWords) (R : Nat → Bool) {t0 : Nat}
    (h0 : t0 % 2 = 1) (hw : win R t0 ∈ trap) :
    ¬ FinSupp (Rule30PeriodTwoSideways.Psi R) := by
  intro hfin
  refine hQ _ hfin (Rule30PeriodTwoSideways.Psi_inX R) ⟨t0, fun s hs => ?_⟩
  have e : (fun s => !zrow (Rule30PeriodTwoSideways.Psi R) (2 * s + 1) 1) =
      Rule30PeriodTwoSideways.u R := by
    funext s; rw [Rule30PeriodTwoSideways.Psi_free]; simp; rfl
  rw [e]
  exact ⟨gaps_of_entry R h0 hw s (by omega), gap_words_of_entry R h0 hw s (by omega)⟩

/-- **`CQ01Empty` follows from `Q01GapWords`.** -/
theorem CQ01Empty_of_Q01GapWords (hQ : Q01GapWords) : Rule30PeriodTwoSideways.CQ01Empty :=
  not_finSupp_Psi_of_Q01GapWords hQ _ (t0 := 293) (by decide) entry_empty

/-! ## The five words are minimal -/

/-- Along the double steps with the listed values of column `17`, the window `w` reads `word` in
column `1`, starting with its own. -/
def pathReads : List Bool → List (Bool × Bool) → List Bool → Bool
  | w, [], [b] => w.headD false == b
  | w, (x1, x2) :: xs, b :: rest => (w.headD false == b) && pathReads (step2 w x1 x2) xs rest
  | _, _, _ => false

/-- A path of the trap graph that reads `word`: a window of `trap`, coded by `c`, and values of
column `17`. By `trapClosed_ok` every window of the path is in `trap`. -/
def trapPath (c : Nat) (xs : List (Bool × Bool)) (word : List Bool) : Bool :=
  trapCodes.contains c && pathReads (decode c) xs word

def path33 : Nat × List (Bool × Bool) :=
  (6103, [(true, false), (false, false), (false, false), (false, false), (false, false),
    (false, false)])
def path335 : Nat × List (Bool × Bool) :=
  (28631, [(true, false), (false, false), (false, false), (false, false), (false, false),
    (false, false), (false, false), (false, false), (false, false), (false, true), (false, false)])
def path353 : Nat × List (Bool × Bool) :=
  (407, [(false, true), (false, false), (true, false), (false, false), (false, false),
    (false, false), (false, false), (true, false), (false, false), (true, false), (false, false)])
def path533 : Nat × List (Bool × Bool) :=
  (49415, [(false, false), (false, false), (false, false), (false, true), (false, true),
    (true, false), (false, false), (false, false), (false, false), (false, false), (false, false)])
def path355 : Nat × List (Bool × Bool) :=
  (16791, [(true, false), (false, false), (false, false), (true, false), (false, true),
    (false, false), (false, false), (false, true), (false, true), (false, false), (false, false),
    (false, false), (true, false)])
def path553 : Nat × List (Bool × Bool) :=
  (56743, [(false, true), (true, false), (true, false), (false, true), (false, true),
    (false, false), (true, false), (false, false), (false, false), (true, false), (false, false),
    (true, false), (false, false)])

/-- **The five words are minimal for the trap.** Removing the first or the last gap of any of them
gives one of `33`, `335`, `353`, `533`, `355`, `553`, and each of these is read along a path of
the trap graph. So no shorter word explains any of the five, as far as the trap alone can see. -/
theorem minimal_paths :
    trapPath path33.1 path33.2 (gapWord [3, 3]) = true ∧
    trapPath path335.1 path335.2 (gapWord [3, 3, 5]) = true ∧
    trapPath path353.1 path353.2 (gapWord [3, 5, 3]) = true ∧
    trapPath path533.1 path533.2 (gapWord [5, 3, 3]) = true ∧
    trapPath path355.1 path355.2 (gapWord [3, 5, 5]) = true ∧
    trapPath path553.1 path553.2 (gapWord [5, 5, 3]) = true := by
  decide +kernel

/-! # The eighteen-column lift -/

open Rule30Ether Rule30PeriodTwoCoupled

/-! ## Windows of eighteen columns -/

section Driven18
variable (R : Nat → Bool)

/-- The window of `R` of the columns `1..18` at time `t`. Its first sixteen cells are `win R t`. -/
def win18 (t : Nat) : List Bool := rowOf (drv altCol R) t 0 18

theorem win18_length (t : Nat) : (win18 R t).length = 18 := length_seg _ _

theorem win18_head (t : Nat) : (win18 R t).headD false = drv altCol R t 1 := rowOf_head _ t 0 17

theorem win18_eq (t : Nat) :
    win18 R t = win R t ++ [drv altCol R t 17, drv altCol R t 18] := by
  unfold win18 win rowOf
  rw [show (18 : Nat) = 16 + 1 + 1 from rfl, seg_succ, seg_succ]
  simp [List.append_assoc]

/-- From an odd time, the 18-column window two steps later is a double step of the window, with the
two values of column `19` as the exterior inputs. -/
theorem win18_step2 (t : Nat) (ht : t % 2 = 1) :
    ∃ x1 x2, win18 R (t + 2) = step2 (win18 R t) x1 x2 := by
  have h1 := rowOf_succ (drv_isR30 altCol R) t 0 18
  have h2 := rowOf_succ (drv_isR30 altCol R) (t + 1) 0 18
  rw [drv_col0] at h1 h2
  have a1 : altCol t = false := by unfold altCol; simp [ht]
  have a2 : altCol (t + 1) = true := by unfold altCol; simp; omega
  rw [a1] at h1
  rw [a2] at h2
  refine ⟨drv altCol R t 19, drv altCol R (t + 1) 19, ?_⟩
  unfold win18 step2
  rw [show t + 2 = t + 1 + 1 by omega, h2, h1]

theorem win18_next {L : List (List Bool)} {P : List Bool → Bool} (hc : L.all (allSucc P) = true)
    {t : Nat} (ht : t % 2 = 1) (hw : win18 R t ∈ L) : P (win18 R (t + 2)) = true := by
  obtain ⟨x1, x2, e⟩ := win18_step2 R t ht
  rw [e]
  exact allSucc_spec (List.all_eq_true.1 hc _ hw) x1 x2

end Driven18

/-- The 18-column window coded by `n`: bit `i` of `n` is column `i + 1`. -/
def decode18 (n : Nat) : List Bool := seg (fun i => n.testBit i) 18

theorem decode18_encList {w : List Bool} (hw : w.length = 18) : decode18 (encList w) = w := by
  have := seg_testBit_encList w
  rw [hw] at this
  exact this

theorem mem18_of_maskN {LN : List Nat} {w : List Bool} (hw : w.length = 18)
    (h : inM (maskN LN) w = true) : w ∈ LN.map decode18 :=
  List.mem_map.2 ⟨encList w, maskN_spec LN _ h, decode18_encList hw⟩

/-! ## The check in the 18-column lift -/

/-- Every 18-column window whose first sixteen cells are a window of `trap` (for all four values of
the columns `17` and `18`) and which reads `b` in column `1` is in the layer `L`. -/
def startOK18 (b : Bool) (L : List Nat) : Bool :=
  trap.all (fun w => [[false, false], [false, true], [true, false], [true, true]].all
    (fun e => (w ++ e).headD false != b || inM (maskN L) (w ++ e)))

/-- One layer of the lift: every double step from a window of `S`, for all four values of column
`19`, either does not read `b` in column `1` or lands in `L`. -/
def stepOK18 (S : List Nat) (b : Bool) (L : List Nat) : Bool :=
  (S.map decode18).all (allSucc (fun w => w.headD false != b || inM (maskN L) w))

theorem stepOK18_append (S1 S2 : List Nat) (b : Bool) (L : List Nat) :
    stepOK18 (S1 ++ S2) b L = (stepOK18 S1 b L && stepOK18 S2 b L) := by
  simp [stepOK18, List.map_append, List.all_append]

def readCheck18 : List Nat → List Bool → List (List Nat) → Bool
  | S, [], _ => S.isEmpty
  | S, b :: rest, L :: Ls => stepOK18 S b L && readCheck18 L rest Ls
  | _, _ :: _, [] => false

/-- **The word check in the lift.** -/
def wordCheck18 : List Bool → List (List Nat) → Bool
  | b :: rest, L :: Ls => startOK18 b L && readCheck18 L rest Ls
  | _, _ => false

section Driven18b
variable (R : Nat → Bool)

theorem readCheck18_spec : ∀ (word : List Bool) (S : List Nat) (Ls : List (List Nat)),
    readCheck18 S word Ls = true → ∀ t, t % 2 = 1 → win18 R t ∈ S.map decode18 →
      ¬ ∀ i, i < word.length → (win18 R (t + 2 * (i + 1))).headD false = word.getD i false
  | [], S, Ls, h, t, _, hw, _ => by
    simp only [readCheck18, List.isEmpty_iff] at h
    subst h
    simp at hw
  | b :: rest, S, L :: Ls, h, t, ht, hw, hr => by
    simp only [readCheck18, stepOK18, Bool.and_eq_true] at h
    have hP := win18_next R h.1 ht hw
    have hb : (win18 R (t + 2)).headD false = b := by simpa using hr 0 (by simp)
    rw [hb] at hP
    simp only [bne_self_eq_false, Bool.false_or] at hP
    refine readCheck18_spec rest _ Ls h.2 (t + 2) (by omega)
      (mem18_of_maskN (win18_length R _) hP) ?_
    intro i hi
    have := hr (i + 1) (by simp; omega)
    rw [show t + 2 + 2 * (i + 1) = t + 2 * (i + 1 + 1) by omega]
    simpa using this
  | _ :: _, _, [], h, _, _, _, _ => by simp [readCheck18] at h

/-- **A lift check excludes its word after entry.** If `wordCheck18 word layers` holds and the
window of `R` is in `trap` at an odd time `t0`, then `u R` does not read `word` from any step `s`
with `t0 ≤ 2 s + 1`. -/
theorem not_reads18_of_check {word : List Bool} {layers : List (List Nat)}
    (hc : wordCheck18 word layers = true) {t0 : Nat} (h0 : t0 % 2 = 1) (hw : win R t0 ∈ trap)
    (s : Nat) (hs : t0 ≤ 2 * s + 1) : ¬ Reads (Rule30PeriodTwoSideways.u R) s word := by
  intro hr
  have hw0 : win R (2 * s + 1) ∈ trap := by
    have := win_mem_trap R h0 hw ((2 * s + 1 - t0) / 2)
    rwa [show t0 + 2 * ((2 * s + 1 - t0) / 2) = 2 * s + 1 by omega] at this
  have hu : ∀ k, Rule30PeriodTwoSideways.u R k = (win18 R (2 * k + 1)).headD false := by
    intro k; rw [win18_head]; rfl
  cases word with
  | nil => simp [wordCheck18] at hc
  | cons b rest =>
    cases layers with
    | nil => simp [wordCheck18] at hc
    | cons L Ls =>
      simp only [wordCheck18, startOK18, Bool.and_eq_true] at hc
      have hb : (win18 R (2 * s + 1)).headD false = b := by
        have := hr 0 (by simp)
        rw [hu] at this
        simpa using this
      have he : [drv altCol R (2 * s + 1) 17, drv altCol R (2 * s + 1) 18] ∈
          [[false, false], [false, true], [true, false], [true, true]] := by
        cases drv altCol R (2 * s + 1) 17 <;> cases drv altCol R (2 * s + 1) 18 <;> simp
      have hP := List.all_eq_true.1 (List.all_eq_true.1 hc.1 _ hw0) _ he
      rw [← win18_eq, hb] at hP
      simp only [bne_self_eq_false, Bool.false_or] at hP
      refine readCheck18_spec R rest _ Ls hc.2 (2 * s + 1) (by omega)
        (mem18_of_maskN (win18_length R _) hP) ?_
      intro i hi
      have := hr (i + 1) (by simp; omega)
      rw [hu] at this
      rw [show 2 * s + 1 + 2 * (i + 1) = 2 * (s + (i + 1)) + 1 by omega]
      simpa using this

end Driven18b

/-! ## The layers of `3535353` -/

def lift0_0 : List Nat := [103, 407, 679, 871, 1191, 1431, 1639, 1703, 2727, 3479, 3495, 3687,
    3751, 4055, 4503, 4775, 4967, 5527, 5735, 6055, 6103, 6247, 6567, 6823, 7271, 7591, 7847, 8039,
    8599, 8871, 9063, 9383, 9623, 9831, 10919, 11367, 11687, 12391, 12967, 13207, 13719, 13927,
    13991, 14247, 14439, 14759, 15015, 15975, 16039, 16791, 17063, 17255, 17575, 17815, 18023,
    19111, 19879, 20135, 21911, 22119, 22439, 22631, 22951, 23207, 24231, 24423, 24679, 24983,
    25255, 25447, 25767, 26279, 27303, 27751, 28055, 28263, 28631, 28775, 29079, 29351, 29543,
    29591, 29863, 30103, 30311, 30375, 31399, 31847, 32167, 32359, 32871, 33175, 33447, 33639,
    33959, 34199, 34407, 34471, 35495, 36247, 36263, 36455, 36519, 36823, 37271, 37543, 37735,
    38295, 38503, 38823, 38871, 39015, 39335, 39591, 40039, 40359, 40615, 40807, 41367, 41639,
    41831, 42151, 42391, 42599, 43687, 44135, 44455, 45159, 45735, 45975, 46487, 46695, 46759,
    47015, 47207, 47527, 47783, 48743, 48807, 49255, 49415, 49831, 50583, 50791, 50855, 51879,
    52631, 52647, 52839, 52903, 53207, 53655, 54119, 54439, 54679, 54887, 55719, 55975, 56423,
    56743, 56999, 57191, 57447, 57751, 58023, 58215, 58535, 59047, 60071, 60519, 60823, 61031,
    61543, 61847, 62119, 62311, 62359, 62631, 62871, 63079, 63143, 63399, 63591, 63911, 64167,
    64615, 65127, 65191, 65639, 65943, 66215, 66407]

def lift0_1 : List Nat := [66727, 66967, 67175, 67239, 68263, 69015, 69031, 69223, 69287, 69591,
    70039, 70311, 70503, 71063, 71271, 71591, 71639, 71783, 72103, 72359, 72807, 73127, 73383,
    73575, 74135, 74407, 74599, 74919, 75159, 75367, 76455, 76903, 77223, 77927, 78503, 78743,
    79255, 79463, 79527, 79783, 79975, 80295, 80551, 81511, 81575, 82327, 82599, 82791, 83111,
    83351, 83559, 84647, 85415, 85671, 87447, 87655, 87975, 88167, 88487, 88743, 89767, 89959,
    90215, 90519, 90791, 90983, 91303, 91815, 92839, 93287, 93591, 93799, 94167, 94311, 94615,
    94887, 95079, 95127, 95399, 95639, 95847, 95911, 96935, 97383, 97703, 97895, 98407, 98711,
    98983, 99175, 99495, 99735, 99943, 100007, 101031, 101783, 101799, 101991, 102055, 102359,
    102807, 103079, 103271, 103831, 104039, 104359, 104407, 104551, 104871, 105127, 105575, 105895,
    106151, 106343, 106903, 107175, 107367, 107687, 107927, 108135, 109223, 109671, 109991, 110695,
    111271, 111511, 112023, 112231, 112295, 112551, 112743, 113063, 113319, 114279, 114343, 114791,
    114951, 115367, 116119, 116327, 116391, 117415, 118167, 118183, 118375, 118439, 118743, 119191,
    119655, 119975, 120215, 120423, 121255, 121511, 121959, 122279, 122535, 122727, 122983, 123287,
    123559, 123751, 124071, 124583, 125607, 126055, 126359, 126567, 127079, 127383, 127655, 127847,
    127895, 128167, 128407, 128615, 128679, 128935, 129127, 129447, 129703, 130151, 130663, 130727,
    131175, 131479, 131751, 131943, 132263, 132503, 132711, 132775]

def lift0_2 : List Nat := [133799, 134551, 134567, 134759, 134823, 135127, 135575, 135847, 136039,
    136599, 136807, 137127, 137175, 137319, 137639, 137895, 138343, 138663, 138919, 139111, 139671,
    139943, 140135, 140455, 140695, 140903, 141991, 142439, 142759, 143463, 144039, 144279, 144791,
    144999, 145063, 145319, 145511, 145831, 146087, 147047, 147111, 147863, 148135, 148327, 148647,
    148887, 149095, 150183, 150951, 151207, 152983, 153191, 153511, 153703, 154023, 154279, 155303,
    155495, 155751, 156055, 156327, 156519, 156839, 157351, 158375, 158823, 159127, 159335, 159703,
    159847, 160151, 160423, 160615, 160663, 160935, 161175, 161383, 161447, 162471, 162919, 163239,
    163431, 163943, 164247, 164519, 164711, 165031, 165271, 165479, 165543, 166567, 167319, 167335,
    167527, 167591, 167895, 168343, 168615, 168807, 169367, 169575, 169895, 169943, 170087, 170407,
    170663, 171111, 171431, 171687, 171879, 172439, 172711, 172903, 173223, 173463, 173671, 174759,
    175207, 175527, 176231, 176807, 177047, 177559, 177767, 177831, 178087, 178279, 178599, 178855,
    179815, 179879, 180327, 180487, 180903, 181655, 181863, 181927, 182951, 183703, 183719, 183911,
    183975, 184279, 184727, 185191, 185511, 185751, 185959, 186791, 187047, 187495, 187815, 188071,
    188263, 188519, 188823, 189095, 189287, 189607, 190119, 191143, 191591, 191895, 192103, 192615,
    192919, 193191, 193383, 193431, 193703, 193943, 194151, 194215, 194471, 194663, 194983, 195239,
    195687, 196199, 196263, 196711, 197015, 197287, 197479, 197799, 198039, 198247, 198311, 199335,
    200087, 200103, 200295]

def lift0_3 : List Nat := [200359, 200663, 201111, 201383, 201575, 202135, 202343, 202663, 202711,
    202855, 203175, 203431, 203879, 204199, 204455, 204647, 205207, 205479, 205671, 205991, 206231,
    206439, 207527, 207975, 208295, 208999, 209575, 209815, 210327, 210535, 210599, 210855, 211047,
    211367, 211623, 212583, 212647, 213399, 213671, 213863, 214183, 214423, 214631, 215719, 216487,
    216743, 218519, 218727, 219047, 219239, 219559, 219815, 220839, 221031, 221287, 221591, 221863,
    222055, 222375, 222887, 223911, 224359, 224663, 224871, 225239, 225383, 225687, 225959, 226151,
    226199, 226471, 226711, 226919, 226983, 228007, 228455, 228775, 228967, 229479, 229783, 230055,
    230247, 230567, 230807, 231015, 231079, 232103, 232855, 232871, 233063, 233127, 233431, 233879,
    234151, 234343, 234903, 235111, 235431, 235479, 235623, 235943, 236199, 236647, 236967, 237223,
    237415, 237975, 238247, 238439, 238759, 238999, 239207, 240295, 240743, 241063, 241767, 242343,
    242583, 243095, 243303, 243367, 243623, 243815, 244135, 244391, 245351, 245415, 245863, 246023,
    246439, 247191, 247399, 247463, 248487, 249239, 249255, 249447, 249511, 249815, 250263, 250727,
    251047, 251287, 251495, 252327, 252583, 253031, 253351, 253607, 253799, 254055, 254359, 254631,
    254823, 255143, 255655, 256679, 257127, 257431, 257639, 258151, 258455, 258727, 258919, 258967,
    259239, 259479, 259687, 259751, 260007, 260199, 260519, 260775, 261223, 261735, 261799]

/-- The 752 windows of the 18-column lift that can have read the first 1 samples of
`3535353`, in 4 chunks. -/
def lift0 : List Nat := lift0_0 ++ lift0_1 ++ lift0_2 ++ lift0_3

def lift1_0 : List Nat := [142, 398, 654, 1166, 1486, 1562, 1678, 1818, 2190, 2586, 2702, 3534,
    4238, 4750, 5582, 5914, 6030, 6286, 6362, 6542, 6798, 7310, 7706, 7822, 8334, 8846, 9678,
    10010, 10126, 10382, 10778, 10894, 11662, 12430, 13262, 13850, 13966, 14106, 14222, 14554,
    14734, 14990, 15502, 15822, 16014, 16270, 16526, 17038, 17870, 18202, 18970, 19086, 19854,
    21134, 21966, 22298, 22414, 22746, 22926, 23694, 24090, 24206, 24974, 25230, 25550, 25742,
    26138, 26254, 26510, 27278, 28110, 28814, 29326, 29646, 29838, 30350, 30490, 30606, 30862,
    31374, 32538, 32654, 32910, 33422, 34254, 34586, 34958, 35354, 35470, 37518, 38350, 38682,
    38798, 39130, 39310, 40078, 40474, 40590, 41614, 42778, 42894, 43150, 43662, 45274, 45454,
    46030, 46222, 46302, 46734, 47758, 48922, 49038, 49550, 49806, 50318, 50638, 50714, 50830,
    50970, 51738, 51854, 52622, 52686, 53134, 53390, 53902, 55066, 55182, 55438, 55694, 55950,
    56462, 56974, 57998, 58318, 58510, 58830, 59022, 59162, 59930, 60046, 60814, 61326, 61582,
    62094, 63258, 63374, 63706, 63886, 64142, 64654, 65166, 65678, 66190, 67022, 67354, 67726,
    68122, 68238, 70286, 71118, 71450, 71566, 71898, 72078, 72846, 73242, 73358, 73870, 74382,
    75546, 75662, 75918, 76430, 78222, 78798, 79070, 79386, 79502, 80526, 81358, 81806, 82574,
    83406, 83738, 84506, 84622, 85390, 86158, 87834, 87950, 88282]

def lift1_1 : List Nat := [88462, 89230, 89742, 90510, 91086, 91278, 91674, 91790, 92814, 93646,
    94094, 94350, 94862, 96026, 96142, 96398, 96910, 98446, 98702, 99470, 99866, 99982, 100122,
    100494, 101006, 101838, 102286, 102542, 103054, 103886, 104218, 104334, 104590, 104846, 105102,
    106010, 107150, 107982, 108314, 109082, 109198, 109966, 110734, 110810, 111758, 112410, 112526,
    112858, 113038, 113294, 113806, 114318, 114458, 114574, 114830, 115342, 115854, 116174, 116366,
    117274, 117390, 118670, 119438, 120270, 120602, 120718, 121050, 121230, 121486, 121998, 122394,
    123534, 124366, 124698, 124814, 125466, 125582, 126350, 127118, 127194, 127950, 128142, 128654,
    128794, 129422, 129678, 130190, 130702, 130842, 130958, 131214, 131470, 131726, 132238, 132558,
    132634, 132750, 132890, 133262, 133658, 133774, 134606, 135310, 135822, 136654, 136986, 137102,
    137358, 137434, 137614, 137870, 138382, 138778, 138894, 139406, 139918, 140750, 141082, 141198,
    141454, 141850, 141966, 142734, 143502, 144334, 144922, 145038, 145178, 145294, 145626, 145806,
    146062, 146574, 146894, 147086, 147342, 147598, 148110, 148942, 149274, 150042, 150158, 150926,
    152206, 153038, 153370, 153486, 153818, 153998, 154766, 155162, 155278, 156046, 156302, 156622,
    156814, 157210, 157326, 157582, 158350, 159182, 159886, 160398, 160718, 160910, 161422, 161562,
    161678, 161934, 162446, 163610, 163726, 163982, 164494, 165326, 165658, 166030, 166426, 166542,
    168590, 169422, 169754, 169870, 170202, 170382, 171150, 171546, 171662, 172686, 173850, 173966,
    174222]

def lift1_2 : List Nat := [174734, 176346, 176526, 177102, 177294, 177374, 177806, 178830, 179994,
    180110, 180622, 180878, 181390, 181710, 181786, 181902, 182042, 182810, 182926, 183694, 183758,
    184206, 184462, 184974, 186138, 186254, 186510, 186766, 187022, 187534, 188046, 189070, 189390,
    189582, 189902, 190094, 190234, 191002, 191118, 191886, 192398, 192654, 193166, 194330, 194446,
    194778, 194958, 195214, 195726, 196238, 197006, 197262, 197774, 198094, 198170, 198286, 199194,
    199310, 200142, 200846, 201358, 202522, 202638, 202894, 202970, 203150, 203406, 203918, 204430,
    204942, 205454, 206286, 206618, 206734, 206990, 207386, 207502, 208270, 209038, 209294, 209870,
    210142, 210458, 210574, 210714, 210830, 211162, 211342, 211598, 212110, 212430, 212622, 212878,
    213134, 213646, 214478, 215578, 215694, 217230, 217742, 218574, 218906, 219022, 219354, 219534,
    220302, 220698, 220814, 221582, 221838, 222158, 222746, 222862, 223118, 223886, 224718, 225166,
    225422, 225934, 226254, 226446, 226958, 227098, 227214, 227470, 227982, 229146, 229262, 229518,
    230542, 231054, 231194, 231566, 232078, 233358, 234126, 234958, 235290, 235406, 235738, 235918,
    236174, 236686, 237082, 237198, 238222, 239054, 239386, 239758, 240154, 240270, 241038, 241806,
    241882, 242062, 242830, 242910, 243482, 244110, 244366, 244878, 245390, 245530, 245646, 245902,
    246414, 246926, 247246, 247438, 247578, 248346, 248462, 249230, 249742, 249998, 250510, 251342,
    251674, 251790, 252302, 252558, 253070, 253466, 253582, 254606, 254926, 255118, 255438, 255630,
    255770, 256538, 256654]

def lift1_3 : List Nat := [257422, 257934, 258190, 258266, 258702, 259214, 259866, 259982, 260494,
    260750, 261262, 261774, 261914]

/-- The 589 windows of the 18-column lift that can have read the first 2 samples of
`3535353`, in 4 chunks. -/
def lift1 : List Nat := lift1_0 ++ lift1_1 ++ lift1_2 ++ lift1_3

def lift2_0 : List Nat := [348, 604, 680, 1628, 1692, 2140, 2536, 2652, 3420, 3752, 4188, 4700,
    5788, 5980, 6492, 6632, 6748, 6824, 7848, 8796, 9308, 9592, 9884, 10728, 10844, 11868, 11944,
    12152, 12380, 12892, 13800, 13916, 13980, 14428, 14684, 14940, 15016, 15964, 16220, 16476,
    16988, 17500, 18076, 18920, 19036, 19804, 20060, 20136, 20836, 21084, 22172, 22876, 23208,
    24040, 24156, 24924, 25180, 25692, 25976, 26088, 26204, 26716, 27112, 27228, 28316, 29020,
    29276, 30072, 30184, 30300, 30364, 30812, 31324, 32424, 32604, 32860, 33372, 34460, 35304,
    35420, 36188, 36444, 36520, 37468, 38556, 38748, 39260, 39516, 39592, 40540, 41052, 41564,
    42076, 42360, 42652, 43496, 43612, 44712, 45660, 46568, 46684, 47196, 47708, 48796, 48988,
    49500, 49756, 49832, 50780, 50844, 51804, 52828, 53340, 54364, 54940, 55644, 55784, 55900,
    55976, 56808, 56924, 57000, 57692, 57948, 58460, 58856, 58972, 59036, 59484, 59880, 59996,
    61020, 61084, 61304, 61532, 61796, 62044, 62840, 63132, 63836, 64092, 64168, 65116, 66140,
    67228, 68072, 68188, 68956, 69212, 69288, 70236, 71324, 71516, 72028, 72284, 72360, 73820,
    74332, 74844, 75128, 75420, 76264, 76380, 77480, 78428, 79336, 79452, 79964, 80476, 81756,
    82524, 83036, 83612, 84572, 85596, 87708, 88412, 88744, 89576, 89692, 90460, 90716, 91624,
    91740, 92252, 93852, 94300, 94812, 95324, 95608, 96744, 96860]

def lift2_1 : List Nat := [97960, 98396, 98652, 98908, 98984, 99932, 99996, 100444, 100840, 100956,
    101724, 102056, 102492, 103004, 103516, 103800, 104092, 104936, 105052, 106076, 106152, 107100,
    107612, 108188, 109032, 109148, 110172, 110684, 112284, 112988, 113320, 114268, 114332, 114524,
    114780, 115036, 115292, 115368, 116316, 116380, 116828, 117224, 117340, 118108, 118364, 118440,
    119388, 119900, 120184, 120476, 121180, 121436, 121512, 122460, 123484, 123996, 124280, 124572,
    125416, 125532, 126556, 126840, 127068, 127324, 127332, 128488, 128604, 129116, 129372, 129704,
    130652, 130716, 130908, 131420, 131676, 131752, 132700, 132764, 133212, 133608, 133724, 134492,
    134748, 134824, 135260, 135772, 136860, 137052, 137564, 137704, 137820, 137896, 138920, 139868,
    140380, 140664, 140956, 141800, 141916, 142940, 143016, 143224, 143452, 143964, 144872, 144988,
    145052, 145500, 145756, 146012, 146088, 147036, 147292, 147548, 148060, 148572, 149148, 149992,
    150108, 150876, 151132, 151208, 151908, 152156, 153244, 153948, 154280, 155112, 155228, 155996,
    156252, 156764, 157048, 157160, 157276, 157788, 158184, 158300, 159388, 159836, 160092, 160348,
    161144, 161256, 161372, 161436, 161884, 162280, 162396, 163496, 163676, 163932, 164444, 165532,
    166376, 166492, 167260, 167516, 167592, 168540, 169628, 169820, 170332, 170588, 170664, 171612,
    172124, 172636, 173148, 173432, 173724, 174568, 174684, 175784, 176732, 177640, 177756, 178268,
    178780, 179868, 180060, 180572, 180828, 180904, 181852, 181916, 182364, 182876, 183900, 184412,
    184924, 185436]

def lift2_2 : List Nat := [185720, 186012, 186716, 186856, 186972, 187048, 187880, 187996, 188072,
    188764, 189020, 189532, 189928, 190044, 190108, 190556, 190952, 191068, 192092, 192156, 192376,
    192604, 192868, 193116, 193912, 194204, 194908, 195164, 195240, 196188, 196956, 197212, 197288,
    198236, 198748, 199144, 199260, 200284, 200796, 201308, 202104, 202396, 202588, 203100, 203240,
    203356, 203432, 204456, 204892, 205404, 205916, 206200, 206492, 207336, 207452, 208476, 208552,
    208760, 208988, 209500, 210408, 210524, 210588, 211036, 211292, 211548, 211624, 212572, 213084,
    213596, 214108, 214684, 215644, 216412, 216668, 216744, 217692, 218780, 219484, 219816, 221788,
    222300, 222584, 222696, 222812, 223324, 223720, 223836, 225372, 225628, 225884, 226396, 226680,
    226792, 226908, 227420, 227816, 227932, 229032, 229212, 229468, 229724, 230056, 231004, 231068,
    231516, 231912, 232028, 232796, 233128, 234076, 234588, 234872, 235164, 235356, 235868, 236124,
    237148, 237660, 238172, 238684, 239260, 240104, 240220, 241244, 241320, 241756, 242268, 243292,
    244060, 244316, 244392, 245340, 245404, 245596, 245852, 246108, 246364, 246440, 247388, 247452,
    247900, 248296, 248412, 249180, 249436, 249512, 250460, 250972, 251256, 251548, 252252, 252508,
    252584, 253416, 253532, 254300, 254556, 255464, 255580, 255644, 256092, 256488, 256604, 257628,
    257692, 257912, 258140, 258396, 258404, 258652, 259164, 259448, 260444, 260700, 260776, 261724,
    261788, 261980]

/-- The 563 windows of the 18-column lift that can have read the first 3 samples of
`3535353`, in 3 chunks. -/
def lift2 : List Nat := lift2_0 ++ lift2_1 ++ lift2_2

/-- The 176 windows of the 18-column lift that can have read the first 4 samples of
`3535353`. -/
def lift3 : List Nat := [871, 1431, 2727, 6823, 7847, 9063, 10919, 13207, 13719, 13927, 13991,
    16039, 17255, 17815, 18023, 22119, 24231, 25447, 27303, 28263, 29591, 30375, 31399, 33639,
    34199, 34407, 38295, 40615, 41831, 43687, 45975, 46759, 47783, 50855, 51879, 54119, 54679,
    54887, 58215, 61031, 62871, 63079, 64167, 65191, 66407, 66967, 71063, 73383, 74599, 78743,
    79527, 80551, 82791, 87655, 89767, 91815, 92839, 93799, 95079, 96935, 99735, 99943, 100007,
    101031, 103271, 105127, 107367, 112023, 112231, 112295, 114343, 116119, 116327, 116391, 121511,
    123751, 125607, 127895, 128407, 128615, 128679, 131943, 132503, 133799, 136599, 137895, 138919,
    140135, 141991, 144279, 144791, 144999, 145063, 147111, 148327, 148887, 149095, 153191, 155303,
    156519, 158375, 159335, 160663, 161447, 162471, 164711, 165271, 165479, 169367, 171687, 172903,
    174759, 177047, 177831, 178855, 181927, 182951, 185751, 185959, 187047, 189287, 192103, 193943,
    194151, 195239, 196263, 197479, 199335, 202135, 203431, 204455, 205671, 210327, 210535, 210599,
    211623, 212647, 213863, 214423, 214631, 220839, 222055, 222887, 223911, 224871, 226151, 226199,
    226983, 228007, 230247, 230807, 231015, 231079, 234343, 236199, 237223, 238439, 242583, 243095,
    243303, 243367, 244391, 247191, 247399, 247463, 251287, 251495, 252583, 254823, 255655, 257639,
    258919, 258967, 259479, 259687, 260775]

/-- The 192 windows of the 18-column lift that can have read the first 5 samples of
`3535353`. -/
def lift4 : List Nat := [3534, 5582, 5914, 6798, 9678, 10010, 10382, 10894, 13966, 14106, 15502,
    15822, 16014, 18202, 19086, 21966, 22298, 23694, 24206, 26254, 27278, 28110, 29838, 30350,
    30490, 30862, 31374, 38350, 38682, 42778, 43150, 43662, 46222, 46734, 50970, 52686, 55066,
    55950, 56462, 56974, 59022, 59162, 60046, 64142, 65166, 67022, 68238, 71118, 75546, 75918,
    76430, 79502, 81358, 83406, 83738, 84622, 87834, 89230, 89742, 91790, 93646, 96026, 96398,
    96910, 99982, 101838, 103886, 104218, 105102, 107982, 108314, 109198, 111758, 112410, 113806,
    114318, 116366, 117390, 120270, 120602, 121486, 124698, 125582, 128142, 128654, 128794, 130190,
    130702, 132558, 134606, 136654, 136986, 137870, 140750, 141082, 141454, 141966, 145038, 145178,
    146574, 146894, 147086, 149274, 150158, 153038, 153370, 154766, 155278, 157326, 158350, 159182,
    160910, 161422, 161562, 161934, 162446, 169422, 169754, 173850, 174222, 174734, 177294, 177806,
    181902, 182042, 183758, 186138, 187022, 187534, 188046, 190094, 190234, 191118, 194330, 195214,
    195726, 196238, 198094, 198286, 199310, 200142, 202522, 203406, 206618, 206990, 207502, 210574,
    210714, 212110, 212430, 212622, 214478, 215694, 218574, 218906, 220302, 222862, 223886, 224718,
    226446, 226958, 227098, 227470, 227982, 231054, 232078, 234958, 236174, 239054, 239386, 239758,
    240270, 242830, 243482, 244878, 245390, 247438, 247578, 248462, 251342, 251674, 252558, 253070,
    253582, 255630, 255770, 256654, 259214, 259866, 260750, 261262, 261774]

/-- The 192 windows of the 18-column lift that can have read the first 6 samples of
`3535353`. -/
def lift5 : List Nat := [1628, 2140, 2652, 3752, 5788, 6748, 6824, 9308, 10844, 11944, 12380,
    13980, 15016, 15964, 19036, 20136, 22172, 23208, 24156, 26204, 26716, 27228, 28316, 34460,
    35420, 36520, 38556, 39592, 42076, 43612, 44712, 48796, 54364, 54940, 55900, 55976, 56924,
    58972, 59484, 59996, 61084, 61532, 63132, 64092, 64168, 65116, 67228, 68188, 69288, 71324,
    72360, 74844, 75420, 76380, 77480, 84572, 87708, 88744, 89692, 91740, 92252, 93852, 96860,
    99932, 99996, 100956, 102056, 103516, 104092, 105052, 107612, 109148, 110684, 112284, 113320,
    114268, 114332, 116316, 116828, 117340, 118440, 119900, 120476, 121436, 121512, 125532, 127068,
    129704, 130652, 130716, 132700, 133212, 133724, 134824, 136860, 137820, 137896, 140380, 141916,
    143016, 143452, 145052, 146088, 147036, 150108, 151208, 153244, 154280, 155228, 157276, 157788,
    158300, 159388, 162396, 165532, 166492, 167592, 169628, 170664, 173148, 174684, 175784, 179868,
    181852, 182364, 185436, 186012, 186972, 187048, 187996, 190044, 190556, 191068, 192156, 192604,
    194204, 195164, 195240, 196188, 198236, 198748, 199260, 202396, 203356, 203432, 206492, 207452,
    208552, 208988, 210588, 211624, 212572, 215644, 216744, 218780, 219816, 222812, 223324, 223836,
    227932, 231004, 231068, 232028, 233128, 234588, 235164, 236124, 238684, 240220, 241320, 241756,
    244392, 245340, 245404, 247388, 247900, 248412, 249512, 250972, 251548, 252508, 252584, 253532,
    255580, 256092, 256604, 257692, 258140, 260700, 260776, 261724, 261788]

/-- The 147 windows of the 18-column lift that can have read the first 7 samples of
`3535353`. -/
def lift6 : List Nat := [618, 1130, 1594, 2154, 2618, 6250, 7738, 10090, 10346, 11626, 18538,
    19818, 24122, 25706, 26474, 26730, 30266, 31290, 33386, 34666, 34922, 40506, 42858, 43114,
    46650, 50746, 52586, 53866, 55402, 55866, 56890, 58474, 59242, 59498, 63594, 66154, 67690,
    70250, 73274, 75882, 84074, 85354, 86634, 89658, 91242, 96362, 96826, 98922, 99434, 100458,
    104554, 108394, 108650, 109930, 112186, 114234, 115818, 116282, 116842, 122426, 124778, 125034,
    126314, 128570, 130618, 131690, 132202, 132666, 133226, 133690, 135786, 137322, 138810, 141162,
    141418, 142698, 149610, 150890, 155194, 156778, 157546, 157802, 161338, 161898, 162362, 164458,
    165738, 165994, 171578, 173930, 174186, 177722, 181354, 181818, 183658, 184938, 186474, 186938,
    187962, 189546, 190314, 190570, 191850, 194666, 196154, 197738, 198202, 198762, 201322, 202858,
    204346, 206698, 206954, 208234, 212538, 215146, 217706, 220730, 222314, 223082, 223338, 226874,
    227434, 227898, 229994, 230506, 231274, 231530, 235626, 239466, 239722, 241002, 243258, 245306,
    246890, 247354, 247914, 249194, 250474, 253498, 255082, 255850, 256106, 257386, 259642, 260202,
    261690]

/-- The 157 windows of the 18-column lift that can have read the first 8 samples of
`3535353`. -/
def lift7 : List Nat := [1400, 1960, 2216, 4072, 4776, 5608, 6056, 6520, 10152, 10616, 13688,
    15736, 15848, 17064, 18344, 20456, 25976, 26536, 26792, 30072, 32232, 32744, 32936, 33448,
    34728, 36840, 38376, 41640, 42920, 43384, 46456, 48616, 49320, 51368, 53928, 55208, 55672,
    58744, 59304, 64888, 67496, 69608, 71144, 75688, 76152, 81384, 82088, 83880, 91512, 92328,
    94888, 96168, 96632, 98280, 98984, 100520, 102376, 103080, 104360, 104824, 108456, 108920,
    114040, 114152, 114856, 115368, 116088, 118760, 121208, 124840, 128376, 130424, 132472, 133032,
    133288, 135144, 135848, 136680, 137128, 137592, 141224, 141688, 144760, 146808, 146920, 148136,
    149416, 151528, 157048, 157608, 157864, 160424, 161144, 163304, 163816, 164008, 164520, 165800,
    167912, 169448, 172712, 173992, 174456, 177528, 179688, 180392, 181624, 182440, 185000, 186744,
    189816, 190376, 195960, 198008, 198568, 198824, 201384, 202216, 202664, 203128, 206760, 207224,
    212344, 213160, 213672, 214952, 217064, 222584, 223144, 223400, 225960, 226680, 227240, 227704,
    228840, 229352, 230056, 231336, 233448, 234984, 235432, 235896, 238248, 239528, 239992, 245112,
    245224, 245928, 246440, 247160, 249832, 252280, 255352, 255912, 260008, 260472, 261496]

def lift8_0 : List Nat := [3479, 3495, 4503, 5527, 5735, 6247, 7591, 8599, 9383, 11687, 13719,
    14439, 14759, 15015, 17063, 17815, 19879, 22119, 22631, 22951, 24983, 25255, 27303, 28055,
    28263, 32167, 33447, 34199, 36263, 37543, 38503, 39015, 39335, 41367, 42151, 42391, 45735,
    47783, 49255, 52839, 54679, 56743, 58023, 58535, 60823, 61031, 61847, 62871, 63591, 66215,
    66727, 69031, 71271, 71783, 72103, 74135, 77223, 78503, 80551, 82599, 83111, 87447, 88167,
    88487, 92839, 93591, 93799, 94615, 97703, 98407, 99735, 101783, 101799, 101991, 102807, 103079,
    103831, 105895, 106903, 107175, 107687, 112023, 112743, 113063, 114791, 115367, 116119, 118167,
    118183, 118375, 120423, 121255, 123287, 124071, 128407, 131751, 134551, 134567, 135575, 136599,
    136807, 137319, 137639, 138663, 139671, 140455, 142759, 144791, 145511, 145831, 146087, 148135,
    148647, 148887, 150951, 153191, 153703, 154023, 156055, 156327, 158375, 159127, 159335, 163239,
    164519, 165271, 167335, 168615, 169575, 170087, 170407, 172439, 173223, 173463, 176807, 178855,
    180327, 183703, 183911, 185751, 187815, 189607, 191895, 192103, 192919, 193943, 194663, 197287,
    197799, 200087, 202135, 202343, 202855, 203175, 204199, 205207, 205991, 208295, 209575, 210327,
    211047, 211623, 213671, 214183, 214423, 216487, 218727, 219239, 219559, 221591, 223911, 225687,
    228775, 229479, 230567, 230807, 232855, 232871, 233063, 233879, 234151, 235623, 237975, 238247,
    238759, 238999, 242343, 243095, 244135, 244391, 245863, 246439]

def lift8_1 : List Nat := [247191, 249239, 249255, 249447, 251287, 255143, 257431, 257639, 258455,
    259479]

/-- The 202 windows of the 18-column lift that can have read the first 9 samples of
`3535353`, in 2 chunks. -/
def lift8 : List Nat := lift8_0 ++ lift8_1

def lift9_0 : List Nat := [142, 654, 6030, 7310, 7706, 8334, 8846, 10010, 10126, 10778, 14106,
    14222, 14990, 16270, 16526, 17038, 18970, 22298, 22414, 23694, 24090, 26510, 27278, 29326,
    29838, 30490, 30606, 31374, 32538, 32654, 32910, 34586, 37518, 38682, 38798, 40078, 40474,
    41614, 42778, 42894, 43662, 45454, 46222, 47758, 48922, 49038, 51854, 53134, 53390, 55066,
    55950, 56462, 57998, 62094, 63258, 63374, 64142, 65678, 66190, 68122, 71450, 71566, 72846,
    73242, 73870, 75546, 75662, 78222, 80526, 81806, 87834, 87950, 89230, 90510, 94094, 94350,
    94862, 96026, 96142, 96910, 98446, 100122, 101006, 102286, 103054, 104334, 106010, 109082,
    109198, 111758, 112410, 112526, 114458, 114830, 117274, 118670, 119438, 120602, 120718, 121486,
    121998, 122394, 123534, 124814, 125582, 128142, 128794, 130842, 130958, 131214, 131726, 133658,
    136986, 137102, 138382, 138778, 139918, 141082, 141198, 141850, 145178, 145294, 146062, 147342,
    147598, 148110, 150042, 153370, 153486, 154766, 155162, 156046, 157582, 158350, 160398, 160910,
    161562, 161678, 162446, 163610, 163726, 163982, 165658, 168590, 169754, 169870, 171150, 171546,
    172686, 173850, 173966, 174734, 176526, 177294, 178830, 179994, 180110, 182926, 184206, 184462,
    184974, 186138, 186254, 187022, 187534, 189070, 193166, 194330, 194446, 195214, 197262, 199194,
    202522, 202638, 203918, 204942, 206618, 206734, 207386, 209294, 210714, 210830, 211598, 212878,
    213134, 215578, 218906, 219022, 220302, 220698, 221582, 223118]

def lift9_1 : List Nat := [225166, 225422, 225934, 226446, 227098, 227214, 229146, 229262, 229518,
    231194, 233358, 234126, 235290, 235406, 236686, 237082, 239386, 240154, 240270, 242062, 242830,
    243482, 244366, 245530, 245646, 245902, 249742, 250510, 251674, 251790, 252558, 253070, 253466,
    254606, 256654, 257934, 258702, 259214, 259866, 259982, 260750, 261914]

/-- The 234 windows of the 18-column lift that can have read the first 10 samples of
`3535353`, in 2 chunks. -/
def lift9 : List Nat := lift9_0 ++ lift9_1

def lift10_0 : List Nat := [348, 604, 680, 2536, 2652, 3420, 3752, 6492, 6748, 6824, 8796, 10728,
    12380, 12892, 13800, 14428, 14684, 14940, 15016, 19036, 19804, 21084, 22876, 23208, 24924,
    25180, 26088, 26716, 27228, 29020, 30184, 30812, 31324, 32424, 35304, 36188, 36520, 37468,
    39260, 39516, 39592, 40540, 43496, 43612, 45660, 46568, 47196, 49500, 49756, 49832, 51804,
    55644, 55900, 55976, 57692, 57948, 58856, 59484, 59880, 59996, 61532, 63836, 64092, 64168,
    66140, 68072, 68188, 68956, 69288, 70236, 72028, 72360, 76264, 78428, 79336, 79964, 80476,
    84572, 85596, 88412, 88744, 90460, 90716, 91624, 92252, 96860, 97960, 98652, 98908, 98984,
    100956, 101724, 102056, 105052, 107100, 109032, 109148, 110172, 110684, 112988, 113320, 115036,
    115368, 118108, 119388, 121180, 121436, 121512, 122460, 123484, 125532, 127068, 127324, 128488,
    129116, 129372, 129704, 131420, 131676, 131752, 133608, 133724, 134492, 134824, 137564, 137820,
    137896, 139868, 141800, 143452, 143964, 144872, 145500, 145756, 146012, 146088, 150108, 150876,
    152156, 153948, 154280, 155996, 156252, 157160, 157788, 158300, 160092, 161256, 161884, 162396,
    163496, 166376, 167260, 167592, 168540, 170332, 170588, 170664, 174568, 174684, 176732, 177640,
    178268, 180572, 180828, 180904, 182876, 186716, 186972, 187048, 188764, 189020, 189928, 190556,
    190952, 191068, 192604, 194908, 195164, 195240, 196956, 197212, 197288, 199144, 199260, 203100,
    203356, 203432, 205404, 208988, 209500, 210408]

def lift10_1 : List Nat := [211036, 211292, 211548, 211624, 215644, 216412, 216668, 217692, 219484,
    219816, 221788, 222696, 223324, 223836, 226792, 227420, 227932, 229032, 229724, 230056, 231912,
    232028, 232796, 233128, 234076, 235868, 236124, 238172, 240104, 240220, 241244, 241756, 242268,
    244060, 244392, 246108, 246364, 246440, 249180, 249436, 250460, 252252, 252508, 252584, 253532,
    254300, 254556, 255464, 256092, 256604, 258140, 258396, 260444, 260700, 260776]

/-- The 247 windows of the 18-column lift that can have read the first 11 samples of
`3535353`, in 2 chunks. -/
def lift10 : List Nat := lift10_0 ++ lift10_1

/-- The 92 windows of the 18-column lift that can have read the first 12 samples of
`3535353`. -/
def lift11 : List Nat := [2727, 6823, 9063, 10919, 13927, 16039, 17255, 18023, 22119, 24231, 27303,
    31399, 34407, 41831, 43687, 47783, 50855, 51879, 54887, 58215, 63079, 64167, 65191, 74599,
    80551, 82791, 87655, 89767, 92839, 96935, 99943, 100007, 101031, 105127, 107367, 112231,
    114343, 116327, 116391, 121511, 123751, 125607, 128615, 133799, 137895, 140135, 141991, 144999,
    147111, 148327, 149095, 153191, 155303, 158375, 162471, 165479, 172903, 174759, 178855, 181927,
    182951, 185959, 187047, 189287, 194151, 195239, 196263, 199335, 203431, 205671, 210535, 211623,
    212647, 213863, 214631, 220839, 222055, 223911, 228007, 231015, 231079, 236199, 238439, 243303,
    244391, 247399, 247463, 251495, 252583, 254823, 259687, 260775]

/-- The 92 windows of the 18-column lift that can have read the first 13 samples of
`3535353`. -/
def lift12 : List Nat := [5582, 6798, 10382, 10894, 15502, 15822, 21966, 23694, 26254, 27278,
    30862, 31374, 38350, 43150, 43662, 55950, 56462, 59022, 60046, 64142, 68238, 71118, 75918,
    76430, 81358, 84622, 89230, 91790, 96398, 96910, 99982, 103886, 105102, 109198, 113806, 116366,
    120270, 121486, 125582, 130190, 136654, 137870, 141454, 141966, 146574, 146894, 150158, 153038,
    154766, 157326, 158350, 161934, 162446, 169422, 174222, 174734, 181902, 187022, 187534, 190094,
    191118, 195214, 195726, 198286, 199310, 203406, 206990, 207502, 212110, 212430, 215694, 218574,
    220302, 222862, 223886, 227470, 227982, 231054, 232078, 234958, 236174, 239758, 240270, 244878,
    247438, 251342, 252558, 253070, 255630, 256654, 260750, 261262]

/-- The 89 windows of the 18-column lift that can have read the first 14 samples of
`3535353`. -/
def lift13 : List Nat := [2140, 2652, 5788, 6748, 9308, 10844, 19036, 22172, 26716, 27228, 28316,
    35420, 38556, 42076, 43612, 54364, 54940, 55900, 59484, 59996, 61084, 64092, 68188, 71324,
    74844, 76380, 84572, 87708, 92252, 93852, 96860, 100956, 103516, 105052, 107612, 109148,
    116828, 117340, 119900, 120476, 121436, 125532, 133212, 136860, 137820, 140380, 141916, 150108,
    153244, 157788, 158300, 159388, 162396, 166492, 169628, 173148, 174684, 182364, 185436, 186012,
    186972, 190556, 191068, 192156, 195164, 198748, 199260, 202396, 203356, 207452, 215644, 218780,
    223324, 223836, 227932, 232028, 234588, 236124, 238684, 240220, 247900, 248412, 250972, 251548,
    252508, 256092, 256604, 257692, 260700]

/-- The 90 windows of the 18-column lift that can have read the first 15 samples of
`3535353`. -/
def lift14 : List Nat := [618, 2154, 6250, 7738, 10090, 10346, 18538, 24122, 26474, 26730, 30266,
    33386, 34666, 34922, 40506, 42858, 43114, 46650, 53866, 55402, 56890, 59242, 59498, 63594,
    66154, 67690, 70250, 75882, 84074, 86634, 89658, 96362, 98922, 104554, 108394, 108650, 112186,
    122426, 124778, 125034, 128570, 131690, 133226, 135786, 137322, 138810, 141162, 141418, 149610,
    155194, 157546, 157802, 161338, 164458, 165738, 165994, 171578, 173930, 174186, 177722, 184938,
    187962, 190314, 190570, 194666, 198762, 201322, 202858, 206698, 206954, 215146, 217706, 220730,
    223082, 223338, 226874, 227434, 229994, 231274, 231530, 235626, 239466, 239722, 243258, 250474,
    253498, 255850, 256106, 259642, 260202]

/-- The 86 windows of the 18-column lift that can have read the first 16 samples of
`3535353`. -/
def lift15 : List Nat := [1960, 2216, 4072, 6056, 10152, 13688, 15736, 18344, 20456, 25976, 26536,
    26792, 30072, 32744, 32936, 36840, 42920, 49320, 51368, 58744, 59304, 64888, 67496, 69608,
    75688, 82088, 83880, 91512, 92328, 96168, 98280, 100520, 102376, 104360, 108456, 114040,
    114856, 118760, 124840, 128376, 130424, 133032, 133288, 135144, 137128, 141224, 144760, 146808,
    149416, 151528, 157048, 157608, 157864, 161144, 163816, 164008, 167912, 173992, 180392, 182440,
    189816, 190376, 195960, 198568, 198824, 202664, 206760, 212344, 213160, 214952, 217064, 222584,
    223144, 223400, 226680, 227240, 229352, 233448, 235432, 239528, 245112, 245928, 249832, 255352,
    255912, 261496]

/-- The 116 windows of the 18-column lift that can have read the first 17 samples of
`3535353`. -/
def lift16 : List Nat := [3479, 3495, 6247, 7591, 9383, 11687, 13719, 14439, 17815, 19879, 22631,
    22951, 25255, 28055, 34199, 36263, 39015, 39335, 42151, 45735, 49255, 54679, 56743, 58535,
    60823, 62871, 63591, 66727, 69031, 71783, 72103, 77223, 78503, 83111, 87447, 88167, 93591,
    98407, 99735, 101783, 101799, 105895, 107687, 112023, 112743, 113063, 114791, 116119, 118167,
    118183, 121255, 124071, 128407, 134551, 134567, 137319, 137639, 138663, 140455, 142759, 144791,
    145511, 148647, 148887, 150951, 153703, 154023, 156327, 159127, 165271, 167335, 170087, 170407,
    173223, 176807, 180327, 183703, 185751, 187815, 189607, 191895, 193943, 194663, 197799, 200087,
    202855, 203175, 204199, 205991, 208295, 209575, 210327, 211047, 214183, 214423, 216487, 219239,
    219559, 229479, 230567, 230807, 232855, 232871, 235623, 238759, 242343, 243095, 244135, 245863,
    247191, 249239, 249255, 251287, 255143, 257431, 259479]

/-- The 140 windows of the 18-column lift that can have read the first 18 samples of
`3535353`. -/
def lift17 : List Nat := [142, 6030, 8334, 8846, 10010, 10126, 14106, 14222, 16270, 16526, 17038,
    22298, 22414, 26510, 29326, 30490, 30606, 32538, 32654, 32910, 37518, 38682, 38798, 41614,
    42778, 42894, 45454, 48922, 49038, 53390, 55066, 57998, 62094, 63258, 63374, 65678, 71566,
    73870, 75546, 75662, 78222, 81806, 87834, 87950, 90510, 94094, 94350, 94862, 96026, 96142,
    98446, 103054, 104334, 112410, 112526, 114458, 114830, 119438, 120718, 123534, 124814, 128794,
    130842, 130958, 131214, 137102, 139918, 141082, 141198, 145178, 145294, 147342, 147598, 148110,
    153370, 153486, 156046, 157582, 160398, 161562, 161678, 163610, 163726, 163982, 168590, 169754,
    169870, 172686, 173850, 173966, 176526, 179994, 180110, 184462, 184974, 186138, 186254, 189070,
    193166, 194330, 194446, 202638, 204942, 206618, 206734, 209294, 210714, 210830, 212878, 213134,
    218906, 219022, 221582, 223118, 225166, 225422, 225934, 227098, 227214, 229146, 229262, 229518,
    234126, 235290, 235406, 239386, 242062, 243482, 245530, 245646, 245902, 250510, 251674, 251790,
    254606, 257934, 258702, 259866, 259982, 261914]

/-- The 150 windows of the 18-column lift that can have read the first 19 samples of
`3535353`. -/
def lift18 : List Nat := [348, 604, 680, 3420, 3752, 6492, 6748, 6824, 8796, 12892, 14684, 14940,
    15016, 19036, 19804, 21084, 22876, 23208, 24924, 25180, 29020, 36188, 36520, 37468, 39260,
    39516, 40540, 45660, 49500, 49756, 49832, 55644, 55976, 57692, 57948, 59996, 63836, 64168,
    66140, 68956, 69288, 70236, 72028, 72360, 78428, 80476, 85596, 88412, 88744, 90460, 90716,
    98652, 98908, 98984, 101724, 102056, 107100, 110172, 112988, 113320, 115036, 115368, 118108,
    119388, 121180, 122460, 123484, 125532, 127324, 129372, 129704, 131420, 131676, 131752, 134492,
    134824, 137564, 137820, 137896, 139868, 143964, 145756, 146012, 146088, 150108, 150876, 152156,
    153948, 154280, 155996, 156252, 160092, 167260, 167592, 168540, 170332, 170588, 176732, 180572,
    180828, 180904, 186716, 187048, 188764, 189020, 191068, 194908, 195240, 196956, 197212, 197288,
    203100, 203432, 205404, 209500, 211292, 211548, 211624, 216412, 216668, 217692, 219484, 219816,
    221788, 229724, 230056, 232796, 233128, 234076, 236124, 238172, 241244, 242268, 244060, 244392,
    246108, 246364, 246440, 249180, 249436, 250460, 252252, 252584, 253532, 254300, 254556, 256604,
    258396, 260444, 260776]

/-- The 43 windows of the 18-column lift that can have read the first 20 samples of
`3535353`. -/
def lift19 : List Nat := [2727, 6823, 16039, 24231, 27303, 31399, 43687, 47783, 51879, 64167,
    65191, 80551, 89767, 92839, 96935, 101031, 105127, 114343, 121511, 125607, 133799, 137895,
    147111, 155303, 158375, 162471, 174759, 178855, 182951, 187047, 195239, 196263, 199335, 203431,
    211623, 212647, 220839, 223911, 228007, 236199, 244391, 252583, 260775]

/-- The 48 windows of the 18-column lift that can have read the first 21 samples of
`3535353`. -/
def lift20 : List Nat := [6798, 10894, 26254, 27278, 31374, 43662, 55950, 59022, 60046, 64142,
    68238, 76430, 84622, 91790, 99982, 105102, 109198, 116366, 121486, 125582, 137870, 141966,
    150158, 157326, 158350, 162446, 174734, 181902, 187022, 190094, 191118, 195214, 198286, 199310,
    203406, 207502, 215694, 222862, 223886, 231054, 232078, 236174, 240270, 247438, 252558, 255630,
    256654, 260750]

/-- The 43 windows of the 18-column lift that can have read the first 22 samples of
`3535353`. -/
def lift21 : List Nat := [2652, 6748, 10844, 19036, 27228, 35420, 43612, 55900, 59996, 64092,
    68188, 76380, 84572, 96860, 100956, 105052, 109148, 117340, 121436, 125532, 137820, 141916,
    150108, 158300, 162396, 166492, 174684, 186972, 191068, 195164, 199260, 203356, 207452, 215644,
    223836, 227932, 232028, 236124, 240220, 248412, 252508, 256604, 260700]

/-- The 37 windows of the 18-column lift that can have read the first 23 samples of
`3535353`. -/
def lift22 : List Nat := [2154, 6250, 10346, 18538, 26730, 34922, 43114, 55402, 59498, 63594,
    67690, 75882, 84074, 96362, 104554, 108650, 125034, 133226, 137322, 141418, 149610, 157802,
    165994, 174186, 190570, 194666, 198762, 202858, 206954, 215146, 223338, 227434, 231530, 235626,
    239722, 256106, 260202]

/-- The 30 windows of the 18-column lift that can have read the first 24 samples of
`3535353`. -/
def lift23 : List Nat := [1960, 6056, 10152, 18344, 26536, 42920, 59304, 67496, 75688, 83880,
    96168, 104360, 108456, 124840, 133032, 137128, 141224, 149416, 157608, 173992, 190376, 198568,
    202664, 206760, 214952, 223144, 227240, 235432, 239528, 255912]

/-- The 33 windows of the 18-column lift that can have read the first 25 samples of
`3535353`. -/
def lift24 : List Nat := [3495, 7591, 11687, 19879, 22951, 36263, 39335, 56743, 69031, 72103,
    77223, 101799, 105895, 113063, 118183, 121255, 134567, 137639, 138663, 142759, 150951, 154023,
    167335, 170407, 187815, 203175, 204199, 208295, 216487, 219559, 232871, 244135, 249255]

/-- The 46 windows of the 18-column lift that can have read the first 26 samples of
`3535353`. -/
def lift25 : List Nat := [6030, 8846, 14222, 16270, 22414, 29326, 32654, 38798, 41614, 49038,
    62094, 63374, 71566, 81806, 87950, 94094, 94862, 112526, 119438, 123534, 130958, 137102,
    139918, 145294, 147342, 153486, 160398, 163726, 169870, 172686, 180110, 184974, 193166, 194446,
    202638, 210830, 212878, 219022, 225166, 225934, 229262, 235406, 245646, 250510, 257934, 258702]

/-- The 58 windows of the 18-column lift that can have read the first 27 samples of
`3535353`. -/
def lift26 : List Nat := [348, 6492, 8796, 21084, 22876, 24924, 29020, 37468, 39260, 49500, 49756,
    55644, 57692, 57948, 70236, 72028, 88412, 90460, 98652, 107100, 112988, 115036, 121180, 123484,
    127324, 129372, 131420, 137564, 139868, 152156, 153948, 155996, 160092, 168540, 170332, 180572,
    180828, 186716, 188764, 189020, 194908, 196956, 203100, 205404, 211292, 217692, 219484, 229724,
    234076, 238172, 244060, 246108, 246364, 252252, 254300, 254556, 258396, 260444]

/-- The layers of `3535353` in the 18-column lift, one per sample (752, 589, 563, 176, 192, 192,
147, 157, 202, 234, 247, 92, 92, 89, 90, 86, 116, 140, 150, 43, 48, 43, 37, 30, 33, 46, 58,
0); the last is empty. -/
def liftLayers : List (List Nat) := [lift0, lift1, lift2, lift3, lift4, lift5, lift6, lift7, lift8,
    lift9, lift10, lift11, lift12, lift13, lift14, lift15, lift16, lift17, lift18, lift19, lift20,
    lift21, lift22, lift23, lift24, lift25, lift26, []]

theorem liftStart : startOK18 true lift0 = true := by decide +kernel
theorem liftStep1_0 : stepOK18 lift0_0 false lift1 = true := by
  decide +kernel
theorem liftStep1_1 : stepOK18 lift0_1 false lift1 = true := by
  decide +kernel
theorem liftStep1_2 : stepOK18 lift0_2 false lift1 = true := by
  decide +kernel
theorem liftStep1_3 : stepOK18 lift0_3 false lift1 = true := by
  decide +kernel
theorem liftStep1 : stepOK18 lift0 false lift1 = true := by
  simp only [lift0, stepOK18_append, liftStep1_0, liftStep1_1, liftStep1_2, liftStep1_3,
    Bool.and_self]
theorem liftStep2_0 : stepOK18 lift1_0 false lift2 = true := by
  decide +kernel
theorem liftStep2_1 : stepOK18 lift1_1 false lift2 = true := by
  decide +kernel
theorem liftStep2_2 : stepOK18 lift1_2 false lift2 = true := by
  decide +kernel
theorem liftStep2_3 : stepOK18 lift1_3 false lift2 = true := by
  decide +kernel
theorem liftStep2 : stepOK18 lift1 false lift2 = true := by
  simp only [lift1, stepOK18_append, liftStep2_0, liftStep2_1, liftStep2_2, liftStep2_3,
    Bool.and_self]
theorem liftStep3_0 : stepOK18 lift2_0 true lift3 = true := by
  decide +kernel
theorem liftStep3_1 : stepOK18 lift2_1 true lift3 = true := by
  decide +kernel
theorem liftStep3_2 : stepOK18 lift2_2 true lift3 = true := by
  decide +kernel
theorem liftStep3 : stepOK18 lift2 true lift3 = true := by
  simp only [lift2, stepOK18_append, liftStep3_0, liftStep3_1, liftStep3_2, Bool.and_self]
theorem liftStep4 : stepOK18 lift3 false lift4 = true := by
  decide +kernel
theorem liftStep5 : stepOK18 lift4 false lift5 = true := by
  decide +kernel
theorem liftStep6 : stepOK18 lift5 false lift6 = true := by
  decide +kernel
theorem liftStep7 : stepOK18 lift6 false lift7 = true := by
  decide +kernel
theorem liftStep8 : stepOK18 lift7 true lift8 = true := by
  decide +kernel
theorem liftStep9_0 : stepOK18 lift8_0 false lift9 = true := by
  decide +kernel
theorem liftStep9_1 : stepOK18 lift8_1 false lift9 = true := by
  decide +kernel
theorem liftStep9 : stepOK18 lift8 false lift9 = true := by
  simp only [lift8, stepOK18_append, liftStep9_0, liftStep9_1, Bool.and_self]
theorem liftStep10_0 : stepOK18 lift9_0 false lift10 = true := by
  decide +kernel
theorem liftStep10_1 : stepOK18 lift9_1 false lift10 = true := by
  decide +kernel
theorem liftStep10 : stepOK18 lift9 false lift10 = true := by
  simp only [lift9, stepOK18_append, liftStep10_0, liftStep10_1, Bool.and_self]
theorem liftStep11_0 : stepOK18 lift10_0 true lift11 = true := by
  decide +kernel
theorem liftStep11_1 : stepOK18 lift10_1 true lift11 = true := by
  decide +kernel
theorem liftStep11 : stepOK18 lift10 true lift11 = true := by
  simp only [lift10, stepOK18_append, liftStep11_0, liftStep11_1, Bool.and_self]
theorem liftStep12 : stepOK18 lift11 false lift12 = true := by
  decide +kernel
theorem liftStep13 : stepOK18 lift12 false lift13 = true := by
  decide +kernel
theorem liftStep14 : stepOK18 lift13 false lift14 = true := by
  decide +kernel
theorem liftStep15 : stepOK18 lift14 false lift15 = true := by
  decide +kernel
theorem liftStep16 : stepOK18 lift15 true lift16 = true := by
  decide +kernel
theorem liftStep17 : stepOK18 lift16 false lift17 = true := by
  decide +kernel
theorem liftStep18 : stepOK18 lift17 false lift18 = true := by
  decide +kernel
theorem liftStep19 : stepOK18 lift18 true lift19 = true := by
  decide +kernel
theorem liftStep20 : stepOK18 lift19 false lift20 = true := by
  decide +kernel
theorem liftStep21 : stepOK18 lift20 false lift21 = true := by
  decide +kernel
theorem liftStep22 : stepOK18 lift21 false lift22 = true := by
  decide +kernel
theorem liftStep23 : stepOK18 lift22 false lift23 = true := by
  decide +kernel
theorem liftStep24 : stepOK18 lift23 true lift24 = true := by
  decide +kernel
theorem liftStep25 : stepOK18 lift24 false lift25 = true := by
  decide +kernel
theorem liftStep26 : stepOK18 lift25 false lift26 = true := by
  decide +kernel
theorem liftStep27 : stepOK18 lift26 true [] = true := by
  decide +kernel
theorem check3535353 : wordCheck18 (gapWord [3, 5, 3, 5, 3, 5, 3]) liftLayers = true := by
  rw [show gapWord [3, 5, 3, 5, 3, 5, 3] =
    [true, false, false, true, false, false, false,
    false, true, false, false, true, false, false, false, false, true, false, false, true, false,
    false, false, false, true, false, false, true] from rfl]
  simp only [liftLayers, wordCheck18, readCheck18, liftStart, liftStep1, liftStep2, liftStep3,
    liftStep4, liftStep5, liftStep6, liftStep7, liftStep8, liftStep9, liftStep10, liftStep11,
    liftStep12, liftStep13, liftStep14, liftStep15, liftStep16, liftStep17, liftStep18, liftStep19,
    liftStep20, liftStep21, liftStep22, liftStep23, liftStep24, liftStep25, liftStep26, liftStep27,
    List.isEmpty_nil, Bool.and_self]

/-! ## `3535353` after entry -/

/-- **The trap never shows `3535353`.** If the window of `R` is in `trap` at an odd time `t0`, then
`u R` never reads the gap word `3, 5, 3, 5, 3, 5, 3` from a step `s` with `t0 ≤ 2 s + 1`. -/
theorem no_3535353_of_entry (R : Nat → Bool) {t0 : Nat} (h0 : t0 % 2 = 1) (hw : win R t0 ∈ trap)
    (s : Nat) (hs : t0 ≤ 2 * s + 1) :
    ¬ Reads (Rule30PeriodTwoSideways.u R) s (gapWord [3, 5, 3, 5, 3, 5, 3]) :=
  not_reads18_of_check R check3535353 h0 hw s hs

/-! ## Why the lift is needed, and minimality -/

def path16_3535353 : Nat × List (Bool × Bool) :=
  (407, [(false, true), (false, false), (true, false), (false, false), (false, false),
    (false, false), (false, false), (false, false), (false, true), (false, false), (true, false),
    (false, false), (false, false), (false, false), (false, false), (false, false), (false, true),
    (false, false), (true, false), (false, false), (false, false), (false, false), (false, false),
    (true, false), (false, false), (true, false), (false, false)])
def path18_353535 : Nat × List (Bool × Bool) :=
  (407, [(true, false), (false, false), (false, false), (false, true), (false, false),
    (true, false), (false, false), (false, false), (false, true), (false, false), (false, true),
    (false, false), (false, false), (false, false), (false, false), (false, false), (false, true),
    (true, false), (false, false), (false, false), (true, false), (false, true), (true, false),
    (false, false)])
def path18_535353 : Nat × List (Bool × Bool) :=
  (139111, [(false, false), (true, false), (false, false), (false, false), (false, false),
    (true, false), (false, false), (false, false), (false, true), (false, false), (true, false),
    (false, false), (false, true), (false, false), (true, false), (false, false), (false, false),
    (false, false), (false, true), (true, false), (false, false), (false, true), (true, false),
    (false, false)])

/-- **The sixteen columns of the trap cannot see it.** A path of the 16-column trap graph reads
`3535353`, so no check on the trap's own windows can exclude it. -/
theorem trap_reads_3535353 :
    trapPath path16_3535353.1 path16_3535353.2 (gapWord [3, 5, 3, 5, 3, 5, 3]) = true := by
  decide +kernel

/-- A path of the 18-column lift that reads `word`: an 18-column window whose first sixteen cells
are a window of `trap`, coded by `c`, and values of column `19`. -/
def liftPath (c : Nat) (xs : List (Bool × Bool)) (word : List Bool) : Bool :=
  trapCodes.contains (c % 65536) && pathReads (decode18 c) xs word

/-- **`3535353` is minimal for the lift.** Removing its first or its last gap gives `535353` or
`353535`, and a path of the 18-column lift reads each. -/
theorem lift_minimal_paths :
    liftPath path18_353535.1 path18_353535.2 (gapWord [3, 5, 3, 5, 3, 5]) = true ∧
      liftPath path18_535353.1 path18_535353.2 (gapWord [5, 3, 5, 3, 5, 3]) = true := by
  decide +kernel

/-! ## A weaker form of `Q01GapWords` -/

/-- At `s`, `g` satisfies `WordsOK` and does not read `3535353`. -/
def CoreOK (g : Nat → Bool) (s : Nat) : Prop :=
  WordsOK g s ∧ ¬ Reads g s (gapWord [3, 5, 3, 5, 3, 5, 3])

/-- **`Q01GapCore`** (**open**): `Q01GapWords` with `3535353` excluded as well. No finitely
supported constrained start of the zero-boundary left half has free bits whose complement, from some
step on, satisfies `CoreOK` at every step. -/
def Q01GapCore : Prop := ∀ L : Nat → Bool, FinSupp L → InX L →
  ¬ ∃ s0, ∀ s, s0 ≤ s → CoreOK (fun s => !zrow L (2 * s + 1) 1) s

/-- **`Q01GapWords` implies `Q01GapCore`**, which has fewer free bits to exclude. -/
theorem Q01GapCore_of_Q01GapWords (h : Q01GapWords) : Q01GapCore := fun L hf hX ⟨s0, hs⟩ =>
  h L hf hX ⟨s0, fun s hs' => (hs s hs').1⟩

/-- **`Q01GapCore` gives `CQ01` for every right half whose window enters the trap.** -/
theorem not_finSupp_Psi_of_Q01GapCore (hQ : Q01GapCore) (R : Nat → Bool) {t0 : Nat}
    (h0 : t0 % 2 = 1) (hw : win R t0 ∈ trap) :
    ¬ FinSupp (Rule30PeriodTwoSideways.Psi R) := by
  intro hfin
  refine hQ _ hfin (Rule30PeriodTwoSideways.Psi_inX R) ⟨t0, fun s hs => ?_⟩
  have e : (fun s => !zrow (Rule30PeriodTwoSideways.Psi R) (2 * s + 1) 1) =
      Rule30PeriodTwoSideways.u R := by
    funext s; rw [Rule30PeriodTwoSideways.Psi_free]; simp; rfl
  rw [e]
  exact ⟨⟨gaps_of_entry R h0 hw s (by omega), gap_words_of_entry R h0 hw s (by omega)⟩,
    no_3535353_of_entry R h0 hw s (by omega)⟩

/-- **`CQ01Empty` follows from `Q01GapCore`.** -/
theorem CQ01Empty_of_Q01GapCore (hQ : Q01GapCore) : Rule30PeriodTwoSideways.CQ01Empty :=
  not_finSupp_Psi_of_Q01GapCore hQ _ (t0 := 293) (by decide) entry_empty

end Rule30Submission
", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The theorems, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata", "Ruliology.CellularAutomata.Rule30GateTrap", "Ruliology.CellularAutomata.Rule30StripCertificates", "Ruliology.CellularAutomata.Rule30ZeroBoundary", "Ruliology.CellularAutomata.Rule30PeriodTwoSideways", "Ruliology.CellularAutomata.Rule30Ether"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
heads = {"not_reads18_of_check", "no_3535353_of_entry", "trap_reads_3535353", "lift_minimal_paths", "Q01GapCore_of_Q01GapWords", "not_finSupp_Psi_of_Q01GapCore", "CQ01Empty_of_Q01GapCore"};
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.CQ01Empty_of_Q01GapCore"]["KernelCheck"]
```
