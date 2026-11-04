module

public import Ruliology.CellularAutomata.Rule30ForcedFrontCore

/-!
# The forced front: every configuration with a leftmost black cell carries the universal strip by an explicit tick

`Rule30UniversalLeftSide` proved that every configuration with a leftmost black cell carries the universal strip on every
wheel through 53,207 after one time shift, from some time on. This module makes the time explicit. The kit's settling
recursion (`Rule30FrontLaw.frontBound`), run on the strip's sixteen-row cycle in strip time, gives for each wheel `j` a tick
`F j` such that wheel `j` of every such configuration carries the strip from `F j` on, at the configuration's shift
(`forced_front`): at a nearer word with a black, both the configuration's child and the strip's word are reset at the first
black of the nearer word at or after the time the two parents are aligned, and agree from the next tick on (`child_same`);
at a white nearer word (wheels 2, 7, 28, 399) the two children differ by a constant, and if the constant is one the
antiperiod of the child turns the complement into a shift by `L = 1, 2, 4, 8`, which the `L`-periodic lower strip does not
see (`child_white`, `strip_shift`). The shift therefore never exceeds `1 + 2 + 4 + 8 = 15`. The recursion's values are kernel
facts in `Rule30ForcedFrontCore`, in blocks of five thousand wheels: `F 53207 = 107310`. Since `F` is monotone, every
configuration carries the whole strip through wheel 53,207 from strip tick 107,310, that is from tick at most 107,325 of its
own clock (`forced_front_uniform`, `forced_front_left_side`, `forced_front_seed`). The kit's linear bound,
`frontBound w ≤ 1 + w · 2^N`, gives 851,313 here; the single cell itself settles wheel 53,207 at tick 71,116 (a replay, not a
Lean statement); the gap between the forced front and the actual one is the share of wheels already in their cycle when
the forced reset arrives. Cloud (CL733), after the kit's `Rule30FrontLaw` (@AIOvernight), R30-20261103-1c93e6 and the
contributors' CL695; the reset lemmas are `Rule30UniversalLeftSide`'s.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30ForcedFront

open Rule30UniversalLeftSide Rule30ForcedFrontCore Rule30AgedLeftDiagonals Rule30FiniteDiagonals Rule30Diagonals
  Rule30Realization

set_option autoImplicit false

/-! ### The word's bits are the strip's values -/

theorem horner_zero (b : Bool) (n : Nat) : (b.toNat + 2 * n).testBit 0 = b := by
  cases b <;> simp only [Nat.testBit_zero, Bool.toNat_true, Bool.toNat_false, decide_eq_true_eq,
    decide_eq_false_iff_not] <;> omega

theorem horner_div (b : Bool) (n : Nat) : (b.toNat + 2 * n) / 2 = n := by
  cases b <;> simp only [Bool.toNat_true, Bool.toNat_false] <;> omega

theorem horner_last (b : Bool) : b.toNat.testBit 0 = b := by
  cases b <;> rfl

theorem h16_bit_0 (b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool) : (b0.toNat + 2 * (b1.toNat + 2 * (b2.toNat + 2 * (b3.toNat + 2 * (b4.toNat + 2 * (b5.toNat + 2 * (b6.toNat + 2 * (b7.toNat + 2 * (b8.toNat + 2 * (b9.toNat + 2 * (b10.toNat + 2 * (b11.toNat + 2 * (b12.toNat + 2 * (b13.toNat + 2 * (b14.toNat + 2 * (b15.toNat)))))))))))))))).testBit 0 = b0 := by
  rw [horner_zero]
theorem h16_bit_1 (b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool) : (b0.toNat + 2 * (b1.toNat + 2 * (b2.toNat + 2 * (b3.toNat + 2 * (b4.toNat + 2 * (b5.toNat + 2 * (b6.toNat + 2 * (b7.toNat + 2 * (b8.toNat + 2 * (b9.toNat + 2 * (b10.toNat + 2 * (b11.toNat + 2 * (b12.toNat + 2 * (b13.toNat + 2 * (b14.toNat + 2 * (b15.toNat)))))))))))))))).testBit 1 = b1 := by
  rw [Nat.testBit_succ, horner_div, horner_zero]
theorem h16_bit_2 (b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool) : (b0.toNat + 2 * (b1.toNat + 2 * (b2.toNat + 2 * (b3.toNat + 2 * (b4.toNat + 2 * (b5.toNat + 2 * (b6.toNat + 2 * (b7.toNat + 2 * (b8.toNat + 2 * (b9.toNat + 2 * (b10.toNat + 2 * (b11.toNat + 2 * (b12.toNat + 2 * (b13.toNat + 2 * (b14.toNat + 2 * (b15.toNat)))))))))))))))).testBit 2 = b2 := by
  rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
theorem h16_bit_3 (b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool) : (b0.toNat + 2 * (b1.toNat + 2 * (b2.toNat + 2 * (b3.toNat + 2 * (b4.toNat + 2 * (b5.toNat + 2 * (b6.toNat + 2 * (b7.toNat + 2 * (b8.toNat + 2 * (b9.toNat + 2 * (b10.toNat + 2 * (b11.toNat + 2 * (b12.toNat + 2 * (b13.toNat + 2 * (b14.toNat + 2 * (b15.toNat)))))))))))))))).testBit 3 = b3 := by
  rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
theorem h16_bit_4 (b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool) : (b0.toNat + 2 * (b1.toNat + 2 * (b2.toNat + 2 * (b3.toNat + 2 * (b4.toNat + 2 * (b5.toNat + 2 * (b6.toNat + 2 * (b7.toNat + 2 * (b8.toNat + 2 * (b9.toNat + 2 * (b10.toNat + 2 * (b11.toNat + 2 * (b12.toNat + 2 * (b13.toNat + 2 * (b14.toNat + 2 * (b15.toNat)))))))))))))))).testBit 4 = b4 := by
  rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
theorem h16_bit_5 (b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool) : (b0.toNat + 2 * (b1.toNat + 2 * (b2.toNat + 2 * (b3.toNat + 2 * (b4.toNat + 2 * (b5.toNat + 2 * (b6.toNat + 2 * (b7.toNat + 2 * (b8.toNat + 2 * (b9.toNat + 2 * (b10.toNat + 2 * (b11.toNat + 2 * (b12.toNat + 2 * (b13.toNat + 2 * (b14.toNat + 2 * (b15.toNat)))))))))))))))).testBit 5 = b5 := by
  rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
theorem h16_bit_6 (b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool) : (b0.toNat + 2 * (b1.toNat + 2 * (b2.toNat + 2 * (b3.toNat + 2 * (b4.toNat + 2 * (b5.toNat + 2 * (b6.toNat + 2 * (b7.toNat + 2 * (b8.toNat + 2 * (b9.toNat + 2 * (b10.toNat + 2 * (b11.toNat + 2 * (b12.toNat + 2 * (b13.toNat + 2 * (b14.toNat + 2 * (b15.toNat)))))))))))))))).testBit 6 = b6 := by
  rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
theorem h16_bit_7 (b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool) : (b0.toNat + 2 * (b1.toNat + 2 * (b2.toNat + 2 * (b3.toNat + 2 * (b4.toNat + 2 * (b5.toNat + 2 * (b6.toNat + 2 * (b7.toNat + 2 * (b8.toNat + 2 * (b9.toNat + 2 * (b10.toNat + 2 * (b11.toNat + 2 * (b12.toNat + 2 * (b13.toNat + 2 * (b14.toNat + 2 * (b15.toNat)))))))))))))))).testBit 7 = b7 := by
  rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
theorem h16_bit_8 (b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool) : (b0.toNat + 2 * (b1.toNat + 2 * (b2.toNat + 2 * (b3.toNat + 2 * (b4.toNat + 2 * (b5.toNat + 2 * (b6.toNat + 2 * (b7.toNat + 2 * (b8.toNat + 2 * (b9.toNat + 2 * (b10.toNat + 2 * (b11.toNat + 2 * (b12.toNat + 2 * (b13.toNat + 2 * (b14.toNat + 2 * (b15.toNat)))))))))))))))).testBit 8 = b8 := by
  rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
theorem h16_bit_9 (b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool) : (b0.toNat + 2 * (b1.toNat + 2 * (b2.toNat + 2 * (b3.toNat + 2 * (b4.toNat + 2 * (b5.toNat + 2 * (b6.toNat + 2 * (b7.toNat + 2 * (b8.toNat + 2 * (b9.toNat + 2 * (b10.toNat + 2 * (b11.toNat + 2 * (b12.toNat + 2 * (b13.toNat + 2 * (b14.toNat + 2 * (b15.toNat)))))))))))))))).testBit 9 = b9 := by
  rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
theorem h16_bit_10 (b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool) : (b0.toNat + 2 * (b1.toNat + 2 * (b2.toNat + 2 * (b3.toNat + 2 * (b4.toNat + 2 * (b5.toNat + 2 * (b6.toNat + 2 * (b7.toNat + 2 * (b8.toNat + 2 * (b9.toNat + 2 * (b10.toNat + 2 * (b11.toNat + 2 * (b12.toNat + 2 * (b13.toNat + 2 * (b14.toNat + 2 * (b15.toNat)))))))))))))))).testBit 10 = b10 := by
  rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
theorem h16_bit_11 (b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool) : (b0.toNat + 2 * (b1.toNat + 2 * (b2.toNat + 2 * (b3.toNat + 2 * (b4.toNat + 2 * (b5.toNat + 2 * (b6.toNat + 2 * (b7.toNat + 2 * (b8.toNat + 2 * (b9.toNat + 2 * (b10.toNat + 2 * (b11.toNat + 2 * (b12.toNat + 2 * (b13.toNat + 2 * (b14.toNat + 2 * (b15.toNat)))))))))))))))).testBit 11 = b11 := by
  rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
theorem h16_bit_12 (b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool) : (b0.toNat + 2 * (b1.toNat + 2 * (b2.toNat + 2 * (b3.toNat + 2 * (b4.toNat + 2 * (b5.toNat + 2 * (b6.toNat + 2 * (b7.toNat + 2 * (b8.toNat + 2 * (b9.toNat + 2 * (b10.toNat + 2 * (b11.toNat + 2 * (b12.toNat + 2 * (b13.toNat + 2 * (b14.toNat + 2 * (b15.toNat)))))))))))))))).testBit 12 = b12 := by
  rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
theorem h16_bit_13 (b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool) : (b0.toNat + 2 * (b1.toNat + 2 * (b2.toNat + 2 * (b3.toNat + 2 * (b4.toNat + 2 * (b5.toNat + 2 * (b6.toNat + 2 * (b7.toNat + 2 * (b8.toNat + 2 * (b9.toNat + 2 * (b10.toNat + 2 * (b11.toNat + 2 * (b12.toNat + 2 * (b13.toNat + 2 * (b14.toNat + 2 * (b15.toNat)))))))))))))))).testBit 13 = b13 := by
  rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
theorem h16_bit_14 (b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool) : (b0.toNat + 2 * (b1.toNat + 2 * (b2.toNat + 2 * (b3.toNat + 2 * (b4.toNat + 2 * (b5.toNat + 2 * (b6.toNat + 2 * (b7.toNat + 2 * (b8.toNat + 2 * (b9.toNat + 2 * (b10.toNat + 2 * (b11.toNat + 2 * (b12.toNat + 2 * (b13.toNat + 2 * (b14.toNat + 2 * (b15.toNat)))))))))))))))).testBit 14 = b14 := by
  rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_zero]
theorem h16_bit_15 (b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool) : (b0.toNat + 2 * (b1.toNat + 2 * (b2.toNat + 2 * (b3.toNat + 2 * (b4.toNat + 2 * (b5.toNat + 2 * (b6.toNat + 2 * (b7.toNat + 2 * (b8.toNat + 2 * (b9.toNat + 2 * (b10.toNat + 2 * (b11.toNat + 2 * (b12.toNat + 2 * (b13.toNat + 2 * (b14.toNat + 2 * (b15.toNat)))))))))))))))).testBit 15 = b15 := by
  rw [Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, Nat.testBit_succ, horner_div, horner_last]

theorem h16_lt (b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 : Bool) : b0.toNat + 2 * (b1.toNat + 2 * (b2.toNat + 2 * (b3.toNat + 2 * (b4.toNat + 2 * (b5.toNat + 2 * (b6.toNat + 2 * (b7.toNat + 2 * (b8.toNat + 2 * (b9.toNat + 2 * (b10.toNat + 2 * (b11.toNat + 2 * (b12.toNat + 2 * (b13.toNat + 2 * (b14.toNat + 2 * (b15.toNat))))))))))))))) < 2 ^ 16 := by
  have h0 := Bool.toNat_le b0
  have h1 := Bool.toNat_le b1
  have h2 := Bool.toNat_le b2
  have h3 := Bool.toNat_le b3
  have h4 := Bool.toNat_le b4
  have h5 := Bool.toNat_le b5
  have h6 := Bool.toNat_le b6
  have h7 := Bool.toNat_le b7
  have h8 := Bool.toNat_le b8
  have h9 := Bool.toNat_le b9
  have h10 := Bool.toNat_le b10
  have h11 := Bool.toNat_le b11
  have h12 := Bool.toNat_le b12
  have h13 := Bool.toNat_le b13
  have h14 := Bool.toNat_le b14
  have h15 := Bool.toNat_le b15
  omega

theorem wd_bit_0 (j : Nat) : (wd j).testBit 0 = C j 0 :=
  (h16_bit_0 (R0.testBit j) (R1.testBit j) (R2.testBit j) (R3.testBit j) (R4.testBit j) (R5.testBit j) (R6.testBit j) (R7.testBit j) (R8.testBit j) (R9.testBit j) (R10.testBit j) (R11.testBit j) (R12.testBit j) (R13.testBit j) (R14.testBit j) (R15.testBit j)).trans (by rw [R0_eq]; rfl)
theorem wd_bit_1 (j : Nat) : (wd j).testBit 1 = C j 1 :=
  (h16_bit_1 (R0.testBit j) (R1.testBit j) (R2.testBit j) (R3.testBit j) (R4.testBit j) (R5.testBit j) (R6.testBit j) (R7.testBit j) (R8.testBit j) (R9.testBit j) (R10.testBit j) (R11.testBit j) (R12.testBit j) (R13.testBit j) (R14.testBit j) (R15.testBit j)).trans (by rw [R1_eq]; rfl)
theorem wd_bit_2 (j : Nat) : (wd j).testBit 2 = C j 2 :=
  (h16_bit_2 (R0.testBit j) (R1.testBit j) (R2.testBit j) (R3.testBit j) (R4.testBit j) (R5.testBit j) (R6.testBit j) (R7.testBit j) (R8.testBit j) (R9.testBit j) (R10.testBit j) (R11.testBit j) (R12.testBit j) (R13.testBit j) (R14.testBit j) (R15.testBit j)).trans (by rw [R2_eq]; rfl)
theorem wd_bit_3 (j : Nat) : (wd j).testBit 3 = C j 3 :=
  (h16_bit_3 (R0.testBit j) (R1.testBit j) (R2.testBit j) (R3.testBit j) (R4.testBit j) (R5.testBit j) (R6.testBit j) (R7.testBit j) (R8.testBit j) (R9.testBit j) (R10.testBit j) (R11.testBit j) (R12.testBit j) (R13.testBit j) (R14.testBit j) (R15.testBit j)).trans (by rw [R3_eq]; rfl)
theorem wd_bit_4 (j : Nat) : (wd j).testBit 4 = C j 4 :=
  (h16_bit_4 (R0.testBit j) (R1.testBit j) (R2.testBit j) (R3.testBit j) (R4.testBit j) (R5.testBit j) (R6.testBit j) (R7.testBit j) (R8.testBit j) (R9.testBit j) (R10.testBit j) (R11.testBit j) (R12.testBit j) (R13.testBit j) (R14.testBit j) (R15.testBit j)).trans (by rw [R4_eq]; rfl)
theorem wd_bit_5 (j : Nat) : (wd j).testBit 5 = C j 5 :=
  (h16_bit_5 (R0.testBit j) (R1.testBit j) (R2.testBit j) (R3.testBit j) (R4.testBit j) (R5.testBit j) (R6.testBit j) (R7.testBit j) (R8.testBit j) (R9.testBit j) (R10.testBit j) (R11.testBit j) (R12.testBit j) (R13.testBit j) (R14.testBit j) (R15.testBit j)).trans (by rw [R5_eq]; rfl)
theorem wd_bit_6 (j : Nat) : (wd j).testBit 6 = C j 6 :=
  (h16_bit_6 (R0.testBit j) (R1.testBit j) (R2.testBit j) (R3.testBit j) (R4.testBit j) (R5.testBit j) (R6.testBit j) (R7.testBit j) (R8.testBit j) (R9.testBit j) (R10.testBit j) (R11.testBit j) (R12.testBit j) (R13.testBit j) (R14.testBit j) (R15.testBit j)).trans (by rw [R6_eq]; rfl)
theorem wd_bit_7 (j : Nat) : (wd j).testBit 7 = C j 7 :=
  (h16_bit_7 (R0.testBit j) (R1.testBit j) (R2.testBit j) (R3.testBit j) (R4.testBit j) (R5.testBit j) (R6.testBit j) (R7.testBit j) (R8.testBit j) (R9.testBit j) (R10.testBit j) (R11.testBit j) (R12.testBit j) (R13.testBit j) (R14.testBit j) (R15.testBit j)).trans (by rw [R7_eq]; rfl)
theorem wd_bit_8 (j : Nat) : (wd j).testBit 8 = C j 8 :=
  (h16_bit_8 (R0.testBit j) (R1.testBit j) (R2.testBit j) (R3.testBit j) (R4.testBit j) (R5.testBit j) (R6.testBit j) (R7.testBit j) (R8.testBit j) (R9.testBit j) (R10.testBit j) (R11.testBit j) (R12.testBit j) (R13.testBit j) (R14.testBit j) (R15.testBit j)).trans (by rw [R8_eq]; rfl)
theorem wd_bit_9 (j : Nat) : (wd j).testBit 9 = C j 9 :=
  (h16_bit_9 (R0.testBit j) (R1.testBit j) (R2.testBit j) (R3.testBit j) (R4.testBit j) (R5.testBit j) (R6.testBit j) (R7.testBit j) (R8.testBit j) (R9.testBit j) (R10.testBit j) (R11.testBit j) (R12.testBit j) (R13.testBit j) (R14.testBit j) (R15.testBit j)).trans (by rw [R9_eq]; rfl)
theorem wd_bit_10 (j : Nat) : (wd j).testBit 10 = C j 10 :=
  (h16_bit_10 (R0.testBit j) (R1.testBit j) (R2.testBit j) (R3.testBit j) (R4.testBit j) (R5.testBit j) (R6.testBit j) (R7.testBit j) (R8.testBit j) (R9.testBit j) (R10.testBit j) (R11.testBit j) (R12.testBit j) (R13.testBit j) (R14.testBit j) (R15.testBit j)).trans (by rw [R10_eq]; rfl)
theorem wd_bit_11 (j : Nat) : (wd j).testBit 11 = C j 11 :=
  (h16_bit_11 (R0.testBit j) (R1.testBit j) (R2.testBit j) (R3.testBit j) (R4.testBit j) (R5.testBit j) (R6.testBit j) (R7.testBit j) (R8.testBit j) (R9.testBit j) (R10.testBit j) (R11.testBit j) (R12.testBit j) (R13.testBit j) (R14.testBit j) (R15.testBit j)).trans (by rw [R11_eq]; rfl)
theorem wd_bit_12 (j : Nat) : (wd j).testBit 12 = C j 12 :=
  (h16_bit_12 (R0.testBit j) (R1.testBit j) (R2.testBit j) (R3.testBit j) (R4.testBit j) (R5.testBit j) (R6.testBit j) (R7.testBit j) (R8.testBit j) (R9.testBit j) (R10.testBit j) (R11.testBit j) (R12.testBit j) (R13.testBit j) (R14.testBit j) (R15.testBit j)).trans (by rw [R12_eq]; rfl)
theorem wd_bit_13 (j : Nat) : (wd j).testBit 13 = C j 13 :=
  (h16_bit_13 (R0.testBit j) (R1.testBit j) (R2.testBit j) (R3.testBit j) (R4.testBit j) (R5.testBit j) (R6.testBit j) (R7.testBit j) (R8.testBit j) (R9.testBit j) (R10.testBit j) (R11.testBit j) (R12.testBit j) (R13.testBit j) (R14.testBit j) (R15.testBit j)).trans (by rw [R13_eq]; rfl)
theorem wd_bit_14 (j : Nat) : (wd j).testBit 14 = C j 14 :=
  (h16_bit_14 (R0.testBit j) (R1.testBit j) (R2.testBit j) (R3.testBit j) (R4.testBit j) (R5.testBit j) (R6.testBit j) (R7.testBit j) (R8.testBit j) (R9.testBit j) (R10.testBit j) (R11.testBit j) (R12.testBit j) (R13.testBit j) (R14.testBit j) (R15.testBit j)).trans (by rw [R14_eq]; rfl)
theorem wd_bit_15 (j : Nat) : (wd j).testBit 15 = C j 15 :=
  (h16_bit_15 (R0.testBit j) (R1.testBit j) (R2.testBit j) (R3.testBit j) (R4.testBit j) (R5.testBit j) (R6.testBit j) (R7.testBit j) (R8.testBit j) (R9.testBit j) (R10.testBit j) (R11.testBit j) (R12.testBit j) (R13.testBit j) (R14.testBit j) (R15.testBit j)).trans (by rw [R15_eq]; rfl)

theorem wd_bit (j : Nat) : ∀ r, r < 16 → (wd j).testBit r = C j r
  | 0, _ => wd_bit_0 j
  | 1, _ => wd_bit_1 j
  | 2, _ => wd_bit_2 j
  | 3, _ => wd_bit_3 j
  | 4, _ => wd_bit_4 j
  | 5, _ => wd_bit_5 j
  | 6, _ => wd_bit_6 j
  | 7, _ => wd_bit_7 j
  | 8, _ => wd_bit_8 j
  | 9, _ => wd_bit_9 j
  | 10, _ => wd_bit_10 j
  | 11, _ => wd_bit_11 j
  | 12, _ => wd_bit_12 j
  | 13, _ => wd_bit_13 j
  | 14, _ => wd_bit_14 j
  | 15, _ => wd_bit_15 j
  | n + 16, h => absurd h (by omega)

theorem wd_lt (j : Nat) : wd j < 2 ^ 16 := h16_lt (R0.testBit j) (R1.testBit j) (R2.testBit j) (R3.testBit j) (R4.testBit j) (R5.testBit j) (R6.testBit j) (R7.testBit j) (R8.testBit j) (R9.testBit j) (R10.testBit j) (R11.testBit j) (R12.testBit j) (R13.testBit j) (R14.testBit j) (R15.testBit j)

/-- A white word is a white wheel at every tick. -/
theorem white_of_wd {m : Nat} (h : wd m = 0) (t : Nat) : C m t = false := by
  rw [C_mod, ← wd_bit m (t % 16) (Nat.mod_lt _ (by decide)), h, Nat.zero_testBit]

/-- A nonzero word has a set bit below 16. -/
theorem bit_of_wd_ne {j : Nat} (h : wd j ≠ 0) : ∃ r, r < 16 ∧ (wd j).testBit r = true := by
  apply Classical.byContradiction
  intro hno
  apply h
  apply Nat.eq_of_testBit_eq
  intro r
  rw [Nat.zero_testBit]
  rcases Nat.lt_or_ge r 16 with hr | hr
  · cases hb : (wd j).testBit r
    · rfl
    · exact absurd ⟨r, hr, hb⟩ hno
  · exact Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le (wd_lt j) (Nat.pow_le_pow_right (by decide) hr))

/-! ### The search finds a black -/

theorem srch_spec (w m : Nat) : ∀ fuel, fuel ≤ 16 →
    (∃ k, 16 - fuel ≤ k ∧ k < 16 ∧ w.testBit ((m + k) % 16) = true) →
    w.testBit ((m + srch w m fuel) % 16) = true
  | 0, _, ⟨k, hk1, hk2, _⟩ => absurd hk2 (by omega)
  | fuel + 1, hf, ⟨k, hk1, hk2, hk⟩ => by
    simp only [srch]
    split
    · assumption
    · rename_i hw
      apply srch_spec w m fuel (by omega)
      refine ⟨k, ?_, hk2, hk⟩
      rcases Nat.lt_or_ge k (16 - fuel) with hlt | hge
      · have e : k = 16 - (fuel + 1) := by omega
        subst e
        exact absurd hk hw
      · exact hge

theorem srch_black (w m : Nat) (hw : ∃ r, r < 16 ∧ w.testBit r = true) :
    w.testBit ((m + srch w m 16) % 16) = true := by
  obtain ⟨r, hr, hb⟩ := hw
  refine srch_spec w m 16 (Nat.le_refl _) ⟨(r + 16 - m % 16) % 16, by omega, Nat.mod_lt _ (by decide), ?_⟩
  rw [show (m + (r + 16 - m % 16) % 16) % 16 = r by omega]
  exact hb

/-! ### The recursion, wheel by wheel -/

theorem frun_add (i a b : Nat) (st : Nat × Nat) : frun i (a + b) st = frun (i + a) b (frun i a st) := by
  induction a generalizing i st with
  | zero => rw [Nat.zero_add]; rfl
  | succ a ih =>
    rw [show i + (a + 1) = (i + 1) + a by omega, show a + 1 + b = (a + b) + 1 by omega]
    rw [frun, frun]
    exact ih (i + 1) (fstep i st)

theorem frun_chain (i a b : Nat) (st st' st'' : Nat × Nat) (h1 : frun i a st = st')
    (h2 : frun (i + a) b st' = st'') : frun i (a + b) st = st'' := by
  rw [frun_add, h1, h2]

/-- The state after `j` wheels: `(F j, F (j + 1))`. -/
def S (j : Nat) : Nat × Nat := frun 0 j (0, 1)

/-- The forced settling tick of wheel `j`. -/
def F (j : Nat) : Nat := (S j).1

theorem S_succ (j : Nat) : S (j + 1) = fstep j (S j) := by
  unfold S
  rw [frun_add 0 j 1 (0, 1), Nat.zero_add]
  rfl

theorem fstep_fst (j : Nat) (st : Nat × Nat) : (fstep j st).1 = st.2 := by
  unfold fstep
  split <;> rfl

theorem fstep_snd (j : Nat) (st : Nat × Nat) : (fstep j st).2 =
    if wd (j + 1) = 0 then max st.1 st.2 else max st.1 st.2 + srch (wd (j + 1)) (max st.1 st.2) 16 + 1 := by
  unfold fstep
  split <;> rfl

theorem S_snd (j : Nat) : (S j).2 = F (j + 1) := by
  show (S j).2 = (S (j + 1)).1
  rw [S_succ, fstep_fst]

theorem F_zero : F 0 = 0 := rfl
theorem F_one : F 1 = 1 := rfl

theorem F_succ_succ (j : Nat) : F (j + 2) =
    if wd (j + 1) = 0 then max (F j) (F (j + 1))
    else max (F j) (F (j + 1)) + srch (wd (j + 1)) (max (F j) (F (j + 1))) 16 + 1 := by
  have h : F (j + 2) = (fstep j (S j)).2 := by
    show (S (j + 2)).1 = _
    rw [S_succ, fstep_fst, S_succ]
  rw [h, fstep_snd, S_snd]
  rfl

theorem F_step_le (j : Nat) : F (j + 1) ≤ F (j + 2) := by
  rw [F_succ_succ]
  split <;> omega

theorem F_mono {j k : Nat} (h : j ≤ k) : F j ≤ F k := by
  induction k with
  | zero =>
    have e : j = 0 := by omega
    subst e
    exact Nat.le_refl _
  | succ k ih =>
    rcases Nat.lt_or_ge j (k + 1) with hlt | hge
    · have hk := ih (by omega)
      cases k with
      | zero => exact Nat.le_trans hk (by rw [F_zero, F_one]; omega)
      | succ k => exact Nat.le_trans hk (F_step_le k)
    · have e : j = k + 1 := by omega
      subst e
      exact Nat.le_refl _

/-! ### The induction in strip time, with the shift budget -/

/-- The shift budget through wheel `n`: `1, 2, 4, 8` become available at wheels `3, 8, 29, 400`. -/
def lsum (n : Nat) : Nat := min 1 (n / 3) + 2 * min 1 (n / 8) + 4 * min 1 (n / 29) + 8 * min 1 (n / 400)

/-- The white case at a doubling wheel: a shift by the lower strip's period absorbs the complement. -/
theorem white_case {a : Nat → Nat → Bool} (ha : Recurrence a) {n s L : Nat}
    (hC : ∀ t, C (n + 2) (t + 1) = xor (C n t) (C (n + 1) t || C (n + 2) t))
    (ih : ∀ j, j ≤ n + 1 → ∀ t, F j ≤ t → a j (t + s) = C j t)
    (hw : ∀ t, C (n + 1) t = false)
    (hper : ∀ j, j ≤ n + 1 → ∀ t, C j (t + L) = C j t) (hanti : ∀ t, C (n + 2) (t + L) = !C (n + 2) t)
    (hF : F (n + 2) = max (F n) (F (n + 1))) :
    (∀ j, j ≤ n + 2 → ∀ t, F j ≤ t → a j (t + s) = C j t) ∨
    (∀ j, j ≤ n + 2 → ∀ t, F j ≤ t → a j (t + (s + L)) = C j t) := by
  rcases child_white (k := n) (s := s) (T := max (F n) (F (n + 1))) ha hC
    (fun t ht => ih n (by omega) t (by omega)) (fun t ht => ih (n + 1) (by omega) t (by omega))
    (fun t _ => hw t) with h | h
  · left
    intro j hj t ht
    rcases Nat.lt_or_ge j (n + 2) with hlt | hge
    · exact ih j (by omega) t ht
    · have e : j = n + 2 := by omega
      subst e
      exact h t (by omega)
  · right
    intro j hj t ht
    rcases Nat.lt_or_ge j (n + 2) with hlt | hge
    · rw [show t + (s + L) = (t + L) + s by omega, ih j (by omega) (t + L) (by omega), hper j (by omega) t]
    · have e : j = n + 2 := by omega
      subst e
      rw [show t + (s + L) = (t + L) + s by omega, h (t + L) (by omega), hanti t]
      cases C (n + 2) t <;> rfl

theorem aligned_from {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∀ n, n ≤ 53207 → ∃ s, s ≤ lsum n ∧ ∀ j, j ≤ n → ∀ t, F j ≤ t → a j (t + s) = C j t
  | 0, _ => ⟨0, by simp [lsum], fun j hj t _ => by
      have e : j = 0 := by omega
      subst e
      rw [rec_zero ha ha0, C_zero]⟩
  | 1, _ => ⟨0, by simp [lsum], fun j hj t ht => by
      rcases Nat.lt_or_ge j 1 with h0 | h1
      · have e : j = 0 := by omega
        subst e
        rw [rec_zero ha ha0, C_zero]
      · have e : j = 1 := by omega
        subst e
        have ht1 : 1 ≤ t := by rw [F_one] at ht; exact ht
        obtain ⟨u, rfl⟩ : ∃ u, t = u + 1 := ⟨t - 1, by omega⟩
        rw [rec_one ha ha0 u, C_one]⟩
  | n + 2, hn => by
    obtain ⟨s, hs, ih⟩ := aligned_from ha ha0 (n + 1) (by omega)
    have hC : ∀ t, C (n + 2) (t + 1) = xor (C n t) (C (n + 1) t || C (n + 2) t) :=
      fun t => C_step n t (by omega)
    have hlsum : lsum (n + 1) ≤ lsum (n + 2) := by simp only [lsum]; omega
    by_cases hw : wd (n + 1) = 0
    · -- white nearer word: one of the four doubling wheels
      have hwhite : ∀ t, C (n + 1) t = false := white_of_wd hw
      have hF : F (n + 2) = max (F n) (F (n + 1)) := by
        simp [F_succ_succ, hw]
      have hnoblack : ¬ ∃ r, r < 16 ∧ C (n + 1) r = true := fun ⟨r, _, hr⟩ => by
        rw [hwhite r] at hr
        exact Bool.false_ne_true hr
      rcases black_or_white (m := n + 1) (by omega) with hb | h2 | h7 | h28 | h399
      · exact absurd hb hnoblack
      · have e : n = 1 := by omega
        subst e
        obtain ⟨hper, hanti⟩ := strip_shift (m := 2) (L := 1) per2 anti2
        rcases white_case ha hC ih hwhite hper hanti hF with h | h
        · exact ⟨s, by simp only [lsum] at hs ⊢; omega, h⟩
        · exact ⟨s + 1, by simp only [lsum] at hs ⊢; omega, h⟩
      · have e : n = 6 := by omega
        subst e
        obtain ⟨hper, hanti⟩ := strip_shift (m := 7) (L := 2) per7 anti7
        rcases white_case ha hC ih hwhite hper hanti hF with h | h
        · exact ⟨s, by simp only [lsum] at hs ⊢; omega, h⟩
        · exact ⟨s + 2, by simp only [lsum] at hs ⊢; omega, h⟩
      · have e : n = 27 := by omega
        subst e
        obtain ⟨hper, hanti⟩ := strip_shift (m := 28) (L := 4) per28 anti28
        rcases white_case ha hC ih hwhite hper hanti hF with h | h
        · exact ⟨s, by simp only [lsum] at hs ⊢; omega, h⟩
        · exact ⟨s + 4, by simp only [lsum] at hs ⊢; omega, h⟩
      · have e : n = 398 := by omega
        subst e
        obtain ⟨hper, hanti⟩ := strip_shift (m := 399) (L := 8) per399 anti399
        rcases white_case ha hC ih hwhite hper hanti hF with h | h
        · exact ⟨s, by simp only [lsum] at hs ⊢; omega, h⟩
        · exact ⟨s + 8, by simp only [lsum] at hs ⊢; omega, h⟩
    · -- a black in the nearer word: the child is forced from the first black at or after the parents' time
      have hF : F (n + 2) = max (F n) (F (n + 1)) + srch (wd (n + 1)) (max (F n) (F (n + 1))) 16 + 1 := by
        simp [F_succ_succ, hw]
      have hblack : C (n + 1) (max (F n) (F (n + 1)) + srch (wd (n + 1)) (max (F n) (F (n + 1))) 16) = true := by
        rw [C_mod, ← wd_bit (n + 1) _ (Nat.mod_lt _ (by decide))]
        exact srch_black (wd (n + 1)) _ (bit_of_wd_ne hw)
      have hnew := child_same (k := n) (s := s) (T := max (F n) (F (n + 1))) ha hC
        (fun t ht => ih n (by omega) t (by omega)) (fun t ht => ih (n + 1) (by omega) t (by omega))
        (Nat.le_add_right _ _) hblack
      refine ⟨s, Nat.le_trans hs hlsum, fun j hj t ht => ?_⟩
      rcases Nat.lt_or_ge j (n + 2) with hlt | hge
      · exact ih j (by omega) t ht
      · have e : j = n + 2 := by omega
        subst e
        exact hnew t (by omega)

/-! ### The numbers, from the kernel -/

theorem S_53207 : S 53207 = (107310, 107310) :=
  (frun_chain 0 5000 48207 _ _ _ chunk0
      (frun_chain 5000 5000 43207 _ _ _ chunk1
      (frun_chain 10000 5000 38207 _ _ _ chunk2
      (frun_chain 15000 5000 33207 _ _ _ chunk3
      (frun_chain 20000 5000 28207 _ _ _ chunk4
      (frun_chain 25000 5000 23207 _ _ _ chunk5
      (frun_chain 30000 5000 18207 _ _ _ chunk6
      (frun_chain 35000 5000 13207 _ _ _ chunk7
      (frun_chain 40000 5000 8207 _ _ _ chunk8
      (frun_chain 45000 5000 3207 _ _ _ chunk9
      chunk10))))))))))

/-- Read the front off a computed pair. Stated with variables, so that instantiating it at `53207` asks the
kernel for no unfolding. -/
theorem F_of_S {j a b : Nat} (h : S j = (a, b)) : F j = a := by
  show (S j).1 = a
  rw [h]

theorem F_53207 : F 53207 = 107310 := F_of_S S_53207

theorem lsum_53207 : lsum 53207 = 15 := by decide

/-! ### The headlines -/

/-- **The forced front.** Every array with the recurrence and a black start carries the strip on wheel `j ≤ 53207` from strip
tick `F j` on, at a shift of at most `15`. -/
theorem forced_front {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 15 ∧ ∀ j, j ≤ 53207 → ∀ t, F j ≤ t → a j (t + s) = C j t := by
  obtain ⟨s, hs, h⟩ := aligned_from ha ha0 53207 (Nat.le_refl _)
  exact ⟨s, by rw [lsum_53207] at hs; exact hs, h⟩

/-- From strip tick `107,310`, that is from tick at most `107,325` of its own clock, every such array carries the whole strip
through wheel `53,207`. -/
theorem forced_front_uniform {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 15 ∧ ∀ j, j ≤ 53207 → ∀ t, 107310 ≤ t → a j (t + s) = C j t := by
  obtain ⟨s, hs, h⟩ := forced_front ha ha0
  exact ⟨s, hs, fun j hj t ht => h j hj t (Nat.le_trans (by rw [← F_53207]; exact F_mono hj) ht)⟩

/-- Every configuration with a leftmost black cell. -/
theorem forced_front_left_side {x : Int → Bool} {lo : Int} (hleft : ∀ p, p < lo → x p = false)
    (hlo : x lo = true) :
    ∃ s, s ≤ 15 ∧ ∀ j, j ≤ 53207 → ∀ t, 107310 ≤ t → Ld x lo j (t + s) = C j t := by
  have ha0 : Ld x lo 0 0 = true := by
    show evol x 0 (lo - ((0 : Nat) : Int) + ((0 : Nat) : Int)) = true
    rw [show lo - ((0 : Nat) : Int) + ((0 : Nat) : Int) = lo by omega]
    exact hlo
  exact forced_front_uniform (Ld_recurrence hleft) ha0

/-- The single black cell. -/
theorem forced_front_seed : ∃ s, s ≤ 15 ∧ ∀ j, j ≤ 53207 → ∀ t, 107310 ≤ t → D j (t + s) = C j t :=
  forced_front_uniform D_recurrence (D_zero 0)

end Ruliology.CellularAutomata.Rule30ForcedFront
