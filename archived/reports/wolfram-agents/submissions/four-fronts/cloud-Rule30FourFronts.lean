module

public import Ruliology.CellularAutomata.Rule30FourFrontsA0
public import Ruliology.CellularAutomata.Rule30FourFrontsA1
public import Ruliology.CellularAutomata.Rule30FourFrontsB0
public import Ruliology.CellularAutomata.Rule30FourFrontsB1

/-!
# The forced front on the four strips: every configuration with a leftmost black cell is on its strip through wheel 87,866 by an explicit tick

`Rule30FourLeftSides` placed every configuration with a leftmost black cell on one of four strips through wheel 87,866, after
a time shift and from some time on. This module makes the time explicit, as `Rule30ForcedFront` did below the first fork. The
settling recursion of `Rule30FrontLaw` (`frontBound`), run in strip time on each strip's sixteen-row cycle, gives a tick
`F j` for every wheel; the induction of `Rule30FourLeftSides` with the time carried (`Rule30FourFrontsBase`) shows that wheel
`j` of every array with the recurrence and a black start carries its strip from `F j` on, at a shift of at most `15`
(`forced_front_four`). The recursion's values are kernel facts in `Rule30FourFrontsA0` … `Rule30FourFrontsB1`, in blocks of
five thousand wheels: at wheel 87,866 the fronts are 176,968 (A0), 177,229 (A1), 177,170 (B0) and 177,560 (B1). Since the
fronts are monotone, every such array carries the whole of its strip through wheel 87,866 from strip tick 177,560, that is from
tick at most 177,575 of its own clock (`forced_front_four_uniform`, `forced_front_four_left_side`, `forced_front_four_seed`).
The kit-style linear bound with five white wheels below 87,866 is 2,811,713. Across a fork the front is carried by
`F_congr`: the two strips agree below the fork wheel, so their recursions agree through it. Cloud (CL734), after
`Rule30FourLeftSides` (L1513), `Rule30ForcedFront` (CL733) and the kit's `Rule30FrontLaw`.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30FourFronts

open Rule30FourFrontsBase
open Rule30AgedLeftDiagonals Rule30FiniteDiagonals Rule30Diagonals Rule30Realization
open Rule30UniversalLeftSide (rowAt)
open Rule30FourLeftSides (Sp A0 A1 B0 B1 A0_return A1_return B0_return B1_return A0_zero A0_one black_or_white
  strip_shift per2 anti2 per7 anti7 per28 anti28 per399 anti399 white_53207 white_58286 white_72575
  low_B0 low_A1 low_B1 top_B0 top_A1 top_B1 wA0_low wA0_high wA1_high wB0_low wB0_high wB1_high
  low_of_phase comp_of_phase Aligned)

set_option autoImplicit false

/-! ### The words of the four strips -/

/-- The word functions of the four kernel modules. -/
abbrev wdA0 : Nat → Nat := Rule30FourFrontsA0.wd
abbrev wdA1 : Nat → Nat := Rule30FourFrontsA1.wd
abbrev wdB0 : Nat → Nat := Rule30FourFrontsB0.wd
abbrev wdB1 : Nat → Nat := Rule30FourFrontsB1.wd

theorem wdA0_bit (j : Nat) : ∀ r, r < 16 → (wdA0 j).testBit r = Sp A0 j r := fun r hr => by
  show (word16 (fun r => (Rule30FourFrontsA0.R r).testBit j)).testBit r = Sp A0 j r
  rw [word16_bit _ r hr]
  show (Rule30FourFrontsA0.R r).testBit j = Sp A0 j r
  rw [Rule30FourFrontsA0.R_eq r hr]
  rfl

theorem wordsA0 : Words A0 wdA0 := ⟨fun _ => word16_lt _, wdA0_bit⟩

theorem wdA1_bit (j : Nat) : ∀ r, r < 16 → (wdA1 j).testBit r = Sp A1 j r := fun r hr => by
  show (word16 (fun r => (Rule30FourFrontsA1.R r).testBit j)).testBit r = Sp A1 j r
  rw [word16_bit _ r hr]
  show (Rule30FourFrontsA1.R r).testBit j = Sp A1 j r
  rw [Rule30FourFrontsA1.R_eq r hr]
  rfl

theorem wordsA1 : Words A1 wdA1 := ⟨fun _ => word16_lt _, wdA1_bit⟩

theorem wdB0_bit (j : Nat) : ∀ r, r < 16 → (wdB0 j).testBit r = Sp B0 j r := fun r hr => by
  show (word16 (fun r => (Rule30FourFrontsB0.R r).testBit j)).testBit r = Sp B0 j r
  rw [word16_bit _ r hr]
  show (Rule30FourFrontsB0.R r).testBit j = Sp B0 j r
  rw [Rule30FourFrontsB0.R_eq r hr]
  rfl

theorem wordsB0 : Words B0 wdB0 := ⟨fun _ => word16_lt _, wdB0_bit⟩

theorem wdB1_bit (j : Nat) : ∀ r, r < 16 → (wdB1 j).testBit r = Sp B1 j r := fun r hr => by
  show (word16 (fun r => (Rule30FourFrontsB1.R r).testBit j)).testBit r = Sp B1 j r
  rw [word16_bit _ r hr]
  show (Rule30FourFrontsB1.R r).testBit j = Sp B1 j r
  rw [Rule30FourFrontsB1.R_eq r hr]
  rfl

theorem wordsB1 : Words B1 wdB1 := ⟨fun _ => word16_lt _, wdB1_bit⟩

/-! ### White wheels, black windows and the agreement below the forks -/

theorem wdA0_53207 : wdA0 53207 = 0 := word_zero_of_white wordsA0 white_53207
theorem wdA0_58286 : wdA0 58286 = 0 := word_zero_of_white wordsA0 white_58286
theorem wdB0_72575 : wdB0 72575 = 0 := word_zero_of_white wordsB0 white_72575

theorem hbwA0 : ∀ m, m < 53207 → wdA0 m ≠ 0 ∨ m = 2 ∨ m = 7 ∨ m = 28 ∨ m = 399 := fun m hm => by
  rcases black_or_white hm with ⟨r, hr, hb⟩ | h
  · exact Or.inl (word_ne_of_black wordsA0 hr hb)
  · exact Or.inr h

set_option exponentiation.threshold 90000 in
theorem bA0_low : ∀ m, 53208 ≤ m → m < 58286 → wdA0 m ≠ 0 := fun m h1 h2 => by
  obtain ⟨r, hr, hb⟩ := black_window_phase wA0_low h1 (by omega)
  exact word_ne_of_black wordsA0 hr hb
set_option exponentiation.threshold 90000 in
theorem bA0_high : ∀ m, 58287 ≤ m → m < 87866 → wdA0 m ≠ 0 := fun m h1 h2 => by
  obtain ⟨r, hr, hb⟩ := black_window_phase wA0_high h1 (by omega)
  exact word_ne_of_black wordsA0 hr hb
set_option exponentiation.threshold 90000 in
theorem bA1_high : ∀ m, 58287 ≤ m → m < 87866 → wdA1 m ≠ 0 := fun m h1 h2 => by
  obtain ⟨r, hr, hb⟩ := black_window_phase wA1_high h1 (by omega)
  exact word_ne_of_black wordsA1 hr hb
set_option exponentiation.threshold 90000 in
theorem bB0_low : ∀ m, 53208 ≤ m → m < 72575 → wdB0 m ≠ 0 := fun m h1 h2 => by
  obtain ⟨r, hr, hb⟩ := black_window_phase wB0_low h1 (by omega)
  exact word_ne_of_black wordsB0 hr hb
set_option exponentiation.threshold 90000 in
theorem bB0_high : ∀ m, 72576 ≤ m → m < 87866 → wdB0 m ≠ 0 := fun m h1 h2 => by
  obtain ⟨r, hr, hb⟩ := black_window_phase wB0_high h1 (by omega)
  exact word_ne_of_black wordsB0 hr hb
set_option exponentiation.threshold 90000 in
theorem bB1_high : ∀ m, 72576 ≤ m → m < 87866 → wdB1 m ≠ 0 := fun m h1 h2 => by
  obtain ⟨r, hr, hb⟩ := black_window_phase wB1_high h1 (by omega)
  exact word_ne_of_black wordsB1 hr hb

/-- Below a fork the two strips have the same words, so the same fronts. -/
theorem wB0_eq_A0 : ∀ i, i + 2 ≤ 53208 → wdA0 (i + 1) = wdB0 (i + 1) := fun i hi =>
  (word_eq_of_low wordsA0 wordsB0 (fun r _ => low_of_phase A0_return B0_return low_B0 (i + 1) r (by omega))).symm
theorem wA1_eq_A0 : ∀ i, i + 2 ≤ 58287 → wdA0 (i + 1) = wdA1 (i + 1) := fun i hi =>
  (word_eq_of_low wordsA0 wordsA1 (fun r _ => low_of_phase A0_return A1_return low_A1 (i + 1) r (by omega))).symm
theorem wB1_eq_B0 : ∀ i, i + 2 ≤ 72576 → wdB0 (i + 1) = wdB1 (i + 1) := fun i hi =>
  (word_eq_of_low wordsB0 wordsB1 (fun r _ => low_of_phase B0_return B1_return low_B1 (i + 1) r (by omega))).symm

/-! ### The tree, with the time carried -/

/-- **The forced front on the four strips.** Every array with the left-diagonal recurrence and a black wheel 0 carries one of
the four strips on every wheel `j ≤ 87,866` from strip tick `F j` on, at a shift of at most `15`. -/
theorem forced_front_four {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 15 ∧ (AlignedFrom a A0 s (F wdA0) 87866 ∨ AlignedFrom a A1 s (F wdA1) 87866 ∨
      AlignedFrom a B0 s (F wdB0) 87866 ∨ AlignedFrom a B1 s (F wdB1) 87866) := by
  obtain ⟨s, hs, h⟩ := low_from ha ha0 A0_return wordsA0 A0_zero A0_one hbwA0
    (strip_shift (m := 2) per2 anti2) (strip_shift (m := 7) per7 anti7) (strip_shift (m := 28) per28 anti28)
    (strip_shift (m := 399) per399 anti399) 53207 (Nat.le_refl _)
  refine ⟨s, by rw [lsum_53207] at hs; exact hs, ?_⟩
  rcases step_white ha A0_return wordsA0 (by omega) h wdA0_53207 with hA | hB
  · -- the A side: on A0 through the first fork
    have h2 : AlignedFrom a A0 s (F wdA0) 58286 :=
      extend_from ha A0_return wordsA0 (by omega) (by omega) (by omega) hA bA0_low
    rcases step_white ha A0_return wordsA0 (by omega) h2 wdA0_58286 with hA0 | hA1
    · exact Or.inl (extend_from ha A0_return wordsA0 (by omega) (by omega) (by omega) hA0 bA0_high)
    · have h3 : AlignedFrom a A1 s (F wdA0) 58287 := white_fork h2 hA1
        (fun j t hj => low_of_phase A0_return A1_return low_A1 j t (by omega))
        (comp_of_phase A0_return A1_return top_A1)
      have h4 : AlignedFrom a A1 s (F wdA1) 58287 :=
        alignedFrom_congr (fun j hj => F_congr j (fun i hi => wA1_eq_A0 i (by omega))) h3
      exact Or.inr (Or.inl (extend_from ha A1_return wordsA1 (by omega) (by omega) (by omega) h4 bA1_high))
  · -- the B side: the complement at 53,208 is B0's word
    have h3 : AlignedFrom a B0 s (F wdA0) 53208 := white_fork h hB
      (fun j t hj => low_of_phase A0_return B0_return low_B0 j t (by omega))
      (comp_of_phase A0_return B0_return top_B0)
    have h4 : AlignedFrom a B0 s (F wdB0) 53208 :=
      alignedFrom_congr (fun j hj => F_congr j (fun i hi => wB0_eq_A0 i (by omega))) h3
    have h5 : AlignedFrom a B0 s (F wdB0) 72575 :=
      extend_from ha B0_return wordsB0 (by omega) (by omega) (by omega) h4 bB0_low
    rcases step_white ha B0_return wordsB0 (by omega) h5 wdB0_72575 with hB0 | hB1
    · exact Or.inr (Or.inr (Or.inl (extend_from ha B0_return wordsB0 (by omega) (by omega) (by omega) hB0 bB0_high)))
    · have h6 : AlignedFrom a B1 s (F wdB0) 72576 := white_fork h5 hB1
        (fun j t hj => low_of_phase B0_return B1_return low_B1 j t (by omega))
        (comp_of_phase B0_return B1_return top_B1)
      have h7 : AlignedFrom a B1 s (F wdB1) 72576 :=
        alignedFrom_congr (fun j hj => F_congr j (fun i hi => wB1_eq_B0 i (by omega))) h6
      exact Or.inr (Or.inr (Or.inr (extend_from ha B1_return wordsB1 (by omega) (by omega) (by omega) h7 bB1_high)))

/-- The classification of `Rule30FourLeftSides`, recovered with its shift bounded by `15`. -/
theorem classification_bounded {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 15 ∧ (Aligned a A0 s 87866 ∨ Aligned a A1 s 87866 ∨ Aligned a B0 s 87866 ∨ Aligned a B1 s 87866) := by
  obtain ⟨s, hs, h⟩ := forced_front_four ha ha0
  refine ⟨s, hs, ?_⟩
  rcases h with h | h | h | h
  · exact Or.inl (aligned_of_alignedFrom h)
  · exact Or.inr (Or.inl (aligned_of_alignedFrom h))
  · exact Or.inr (Or.inr (Or.inl (aligned_of_alignedFrom h)))
  · exact Or.inr (Or.inr (Or.inr (aligned_of_alignedFrom h)))

/-! ### The numbers, from the kernel -/

theorem SA0 : S wdA0 87866 = (176968, 176968) :=
  (frun_chain _ 0 5000 82866 _ _ _ Rule30FourFrontsA0.chunk0
    (frun_chain _ 5000 5000 77866 _ _ _ Rule30FourFrontsA0.chunk1
    (frun_chain _ 10000 5000 72866 _ _ _ Rule30FourFrontsA0.chunk2
    (frun_chain _ 15000 5000 67866 _ _ _ Rule30FourFrontsA0.chunk3
    (frun_chain _ 20000 5000 62866 _ _ _ Rule30FourFrontsA0.chunk4
    (frun_chain _ 25000 5000 57866 _ _ _ Rule30FourFrontsA0.chunk5
    (frun_chain _ 30000 5000 52866 _ _ _ Rule30FourFrontsA0.chunk6
    (frun_chain _ 35000 5000 47866 _ _ _ Rule30FourFrontsA0.chunk7
    (frun_chain _ 40000 5000 42866 _ _ _ Rule30FourFrontsA0.chunk8
    (frun_chain _ 45000 5000 37866 _ _ _ Rule30FourFrontsA0.chunk9
    (frun_chain _ 50000 5000 32866 _ _ _ Rule30FourFrontsA0.chunk10
    (frun_chain _ 55000 5000 27866 _ _ _ Rule30FourFrontsA0.chunk11
    (frun_chain _ 60000 5000 22866 _ _ _ Rule30FourFrontsA0.chunk12
    (frun_chain _ 65000 5000 17866 _ _ _ Rule30FourFrontsA0.chunk13
    (frun_chain _ 70000 5000 12866 _ _ _ Rule30FourFrontsA0.chunk14
    (frun_chain _ 75000 5000 7866 _ _ _ Rule30FourFrontsA0.chunk15
    (frun_chain _ 80000 5000 2866 _ _ _ Rule30FourFrontsA0.chunk16
    Rule30FourFrontsA0.chunk17)))))))))))))))))

theorem FA0_87866 : F wdA0 87866 = 176968 := F_of_S SA0

theorem SA1 : S wdA1 87866 = (177229, 177232) :=
  (frun_chain _ 0 5000 82866 _ _ _ Rule30FourFrontsA1.chunk0
    (frun_chain _ 5000 5000 77866 _ _ _ Rule30FourFrontsA1.chunk1
    (frun_chain _ 10000 5000 72866 _ _ _ Rule30FourFrontsA1.chunk2
    (frun_chain _ 15000 5000 67866 _ _ _ Rule30FourFrontsA1.chunk3
    (frun_chain _ 20000 5000 62866 _ _ _ Rule30FourFrontsA1.chunk4
    (frun_chain _ 25000 5000 57866 _ _ _ Rule30FourFrontsA1.chunk5
    (frun_chain _ 30000 5000 52866 _ _ _ Rule30FourFrontsA1.chunk6
    (frun_chain _ 35000 5000 47866 _ _ _ Rule30FourFrontsA1.chunk7
    (frun_chain _ 40000 5000 42866 _ _ _ Rule30FourFrontsA1.chunk8
    (frun_chain _ 45000 5000 37866 _ _ _ Rule30FourFrontsA1.chunk9
    (frun_chain _ 50000 5000 32866 _ _ _ Rule30FourFrontsA1.chunk10
    (frun_chain _ 55000 5000 27866 _ _ _ Rule30FourFrontsA1.chunk11
    (frun_chain _ 60000 5000 22866 _ _ _ Rule30FourFrontsA1.chunk12
    (frun_chain _ 65000 5000 17866 _ _ _ Rule30FourFrontsA1.chunk13
    (frun_chain _ 70000 5000 12866 _ _ _ Rule30FourFrontsA1.chunk14
    (frun_chain _ 75000 5000 7866 _ _ _ Rule30FourFrontsA1.chunk15
    (frun_chain _ 80000 5000 2866 _ _ _ Rule30FourFrontsA1.chunk16
    Rule30FourFrontsA1.chunk17)))))))))))))))))

theorem FA1_87866 : F wdA1 87866 = 177229 := F_of_S SA1

theorem SB0 : S wdB0 87866 = (177170, 177173) :=
  (frun_chain _ 0 5000 82866 _ _ _ Rule30FourFrontsB0.chunk0
    (frun_chain _ 5000 5000 77866 _ _ _ Rule30FourFrontsB0.chunk1
    (frun_chain _ 10000 5000 72866 _ _ _ Rule30FourFrontsB0.chunk2
    (frun_chain _ 15000 5000 67866 _ _ _ Rule30FourFrontsB0.chunk3
    (frun_chain _ 20000 5000 62866 _ _ _ Rule30FourFrontsB0.chunk4
    (frun_chain _ 25000 5000 57866 _ _ _ Rule30FourFrontsB0.chunk5
    (frun_chain _ 30000 5000 52866 _ _ _ Rule30FourFrontsB0.chunk6
    (frun_chain _ 35000 5000 47866 _ _ _ Rule30FourFrontsB0.chunk7
    (frun_chain _ 40000 5000 42866 _ _ _ Rule30FourFrontsB0.chunk8
    (frun_chain _ 45000 5000 37866 _ _ _ Rule30FourFrontsB0.chunk9
    (frun_chain _ 50000 5000 32866 _ _ _ Rule30FourFrontsB0.chunk10
    (frun_chain _ 55000 5000 27866 _ _ _ Rule30FourFrontsB0.chunk11
    (frun_chain _ 60000 5000 22866 _ _ _ Rule30FourFrontsB0.chunk12
    (frun_chain _ 65000 5000 17866 _ _ _ Rule30FourFrontsB0.chunk13
    (frun_chain _ 70000 5000 12866 _ _ _ Rule30FourFrontsB0.chunk14
    (frun_chain _ 75000 5000 7866 _ _ _ Rule30FourFrontsB0.chunk15
    (frun_chain _ 80000 5000 2866 _ _ _ Rule30FourFrontsB0.chunk16
    Rule30FourFrontsB0.chunk17)))))))))))))))))

theorem FB0_87866 : F wdB0 87866 = 177170 := F_of_S SB0

theorem SB1 : S wdB1 87866 = (177560, 177563) :=
  (frun_chain _ 0 5000 82866 _ _ _ Rule30FourFrontsB1.chunk0
    (frun_chain _ 5000 5000 77866 _ _ _ Rule30FourFrontsB1.chunk1
    (frun_chain _ 10000 5000 72866 _ _ _ Rule30FourFrontsB1.chunk2
    (frun_chain _ 15000 5000 67866 _ _ _ Rule30FourFrontsB1.chunk3
    (frun_chain _ 20000 5000 62866 _ _ _ Rule30FourFrontsB1.chunk4
    (frun_chain _ 25000 5000 57866 _ _ _ Rule30FourFrontsB1.chunk5
    (frun_chain _ 30000 5000 52866 _ _ _ Rule30FourFrontsB1.chunk6
    (frun_chain _ 35000 5000 47866 _ _ _ Rule30FourFrontsB1.chunk7
    (frun_chain _ 40000 5000 42866 _ _ _ Rule30FourFrontsB1.chunk8
    (frun_chain _ 45000 5000 37866 _ _ _ Rule30FourFrontsB1.chunk9
    (frun_chain _ 50000 5000 32866 _ _ _ Rule30FourFrontsB1.chunk10
    (frun_chain _ 55000 5000 27866 _ _ _ Rule30FourFrontsB1.chunk11
    (frun_chain _ 60000 5000 22866 _ _ _ Rule30FourFrontsB1.chunk12
    (frun_chain _ 65000 5000 17866 _ _ _ Rule30FourFrontsB1.chunk13
    (frun_chain _ 70000 5000 12866 _ _ _ Rule30FourFrontsB1.chunk14
    (frun_chain _ 75000 5000 7866 _ _ _ Rule30FourFrontsB1.chunk15
    (frun_chain _ 80000 5000 2866 _ _ _ Rule30FourFrontsB1.chunk16
    Rule30FourFrontsB1.chunk17)))))))))))))))))

theorem FB1_87866 : F wdB1 87866 = 177560 := F_of_S SB1

/-- Every front through wheel 87,866 is at most 177,560, the B1 front there. -/
theorem fronts_le : (∀ j, j ≤ 87866 → F wdA0 j ≤ 177560) ∧ (∀ j, j ≤ 87866 → F wdA1 j ≤ 177560) ∧
    (∀ j, j ≤ 87866 → F wdB0 j ≤ 177560) ∧ ∀ j, j ≤ 87866 → F wdB1 j ≤ 177560 :=
  ⟨fun j hj => Nat.le_trans (F_mono wdA0 hj) (by rw [FA0_87866]; omega),
   fun j hj => Nat.le_trans (F_mono wdA1 hj) (by rw [FA1_87866]; omega),
   fun j hj => Nat.le_trans (F_mono wdB0 hj) (by rw [FB0_87866]; omega),
   fun j hj => Nat.le_trans (F_mono wdB1 hj) (by rw [FB1_87866]; omega)⟩

/-! ### The headlines -/

/-- **From strip tick 177,560**, that is from tick at most 177,575 of its own clock, every array with the recurrence and a
black start carries the whole of one of the four strips through wheel 87,866. -/
theorem forced_front_four_uniform {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 15 ∧ (OnStrip a A0 s 177560 87866 ∨ OnStrip a A1 s 177560 87866 ∨
      OnStrip a B0 s 177560 87866 ∨ OnStrip a B1 s 177560 87866) := by
  obtain ⟨s, hs, h⟩ := forced_front_four ha ha0
  refine ⟨s, hs, ?_⟩
  rcases h with h | h | h | h
  · exact Or.inl (onStrip_of_alignedFrom fronts_le.1 h)
  · exact Or.inr (Or.inl (onStrip_of_alignedFrom fronts_le.2.1 h))
  · exact Or.inr (Or.inr (Or.inl (onStrip_of_alignedFrom fronts_le.2.2.1 h)))
  · exact Or.inr (Or.inr (Or.inr (onStrip_of_alignedFrom fronts_le.2.2.2 h)))

/-- **Every configuration with a leftmost black cell**, whatever lies to its right: on one of the four strips through wheel
87,866 from tick 177,560 + s of its own clock, s ≤ 15. -/
theorem forced_front_four_left_side {x : Int → Bool} {lo : Int} (hleft : ∀ p, p < lo → x p = false)
    (hlo : x lo = true) :
    ∃ s, s ≤ 15 ∧ (OnStrip (Ld x lo) A0 s 177560 87866 ∨ OnStrip (Ld x lo) A1 s 177560 87866 ∨
      OnStrip (Ld x lo) B0 s 177560 87866 ∨ OnStrip (Ld x lo) B1 s 177560 87866) :=
  forced_front_four_uniform (Ld_recurrence hleft) (by simpa [Ld, evol] using hlo)

/-- The single black cell. The proof does not say which strip. -/
theorem forced_front_four_seed :
    ∃ s, s ≤ 15 ∧ (OnStrip D A0 s 177560 87866 ∨ OnStrip D A1 s 177560 87866 ∨
      OnStrip D B0 s 177560 87866 ∨ OnStrip D B1 s 177560 87866) :=
  forced_front_four_uniform Rule30FourLeftSides.D_recurrence (D_zero 0)

end Ruliology.CellularAutomata.Rule30FourFronts
