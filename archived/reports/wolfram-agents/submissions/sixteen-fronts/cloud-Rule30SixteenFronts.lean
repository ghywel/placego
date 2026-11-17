module

public import Ruliology.CellularAutomata.Rule30SixteenFrontsStrip0
public import Ruliology.CellularAutomata.Rule30SixteenFrontsStrip1
public import Ruliology.CellularAutomata.Rule30SixteenFrontsStrip2
public import Ruliology.CellularAutomata.Rule30SixteenFrontsStrip3
public import Ruliology.CellularAutomata.Rule30SixteenFrontsStrip4
public import Ruliology.CellularAutomata.Rule30SixteenFrontsStrip5
public import Ruliology.CellularAutomata.Rule30SixteenFrontsStrip6
public import Ruliology.CellularAutomata.Rule30SixteenFrontsStrip7
public import Ruliology.CellularAutomata.Rule30SixteenFrontsStrip8
public import Ruliology.CellularAutomata.Rule30SixteenFrontsStrip9
public import Ruliology.CellularAutomata.Rule30SixteenFrontsStrip10
public import Ruliology.CellularAutomata.Rule30SixteenFrontsStrip11
public import Ruliology.CellularAutomata.Rule30SixteenFrontsStrip12
public import Ruliology.CellularAutomata.Rule30SixteenFrontsStrip13
public import Ruliology.CellularAutomata.Rule30SixteenFrontsStrip14
public import Ruliology.CellularAutomata.Rule30SixteenFrontsStrip15

/-!
# 16 left sides of rule 30 through wheel 894235, each with its settling tick

The tree of strips through wheel 894235: every configuration with a leftmost black cell carries one of 16 strips on
every wheel through 894235 from strip tick `F j`, at a shift of at most 31 (`forced_front_tree`), and from strip tick 1798243 on
all of them (`forced_front_tree_uniform`, `…_left_side`, `…_seed`); the 16 strips are realized by finite rows, no time
shift relates two of them, and each configuration is on exactly one (`exactly_left_sides`, `on_exactly_one`); every odd number
reaches one of the 16 rows under `v ↦ 4 v ⊕ (2 v ∨ v)` modulo `2 ^ 894236` (`odd_reaches_one`). Strip 0 is the single
black cell's; strip i > 0 is the child at a fork of its parent, with the fork's child wheel complemented; each strip's period
doubles once in the range. The proof is one lemma per strip, in post-order, carrying the time through the strip's events
(`extend_from`, `step_white`, `white_fork`, `white_shift`); the fronts come from the walk in the strip modules.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30SixteenFronts

open Rule30FiveFrontsBase
open Rule30AgedLeftDiagonals Rule30FiniteDiagonals Rule30Diagonals Rule30Realization
open Rule30UniversalLeftSide (rowAt rowAt_add_mul ofRow ofRow_left Ld_ofRow D_recurrence)
open Rule30SixteenFrontsStrip0 (K)

set_option autoImplicit false

abbrev V0 : Nat := Rule30SixteenFrontsStrip0.V
abbrev w0 : Nat → Nat := Rule30SixteenFrontsStrip0.w
abbrev V1 : Nat := Rule30SixteenFrontsStrip1.V
abbrev w1 : Nat → Nat := Rule30SixteenFrontsStrip1.w
abbrev V2 : Nat := Rule30SixteenFrontsStrip2.V
abbrev w2 : Nat → Nat := Rule30SixteenFrontsStrip2.w
abbrev V3 : Nat := Rule30SixteenFrontsStrip3.V
abbrev w3 : Nat → Nat := Rule30SixteenFrontsStrip3.w
abbrev V4 : Nat := Rule30SixteenFrontsStrip4.V
abbrev w4 : Nat → Nat := Rule30SixteenFrontsStrip4.w
abbrev V5 : Nat := Rule30SixteenFrontsStrip5.V
abbrev w5 : Nat → Nat := Rule30SixteenFrontsStrip5.w
abbrev V6 : Nat := Rule30SixteenFrontsStrip6.V
abbrev w6 : Nat → Nat := Rule30SixteenFrontsStrip6.w
abbrev V7 : Nat := Rule30SixteenFrontsStrip7.V
abbrev w7 : Nat → Nat := Rule30SixteenFrontsStrip7.w
abbrev V8 : Nat := Rule30SixteenFrontsStrip8.V
abbrev w8 : Nat → Nat := Rule30SixteenFrontsStrip8.w
abbrev V9 : Nat := Rule30SixteenFrontsStrip9.V
abbrev w9 : Nat → Nat := Rule30SixteenFrontsStrip9.w
abbrev V10 : Nat := Rule30SixteenFrontsStrip10.V
abbrev w10 : Nat → Nat := Rule30SixteenFrontsStrip10.w
abbrev V11 : Nat := Rule30SixteenFrontsStrip11.V
abbrev w11 : Nat → Nat := Rule30SixteenFrontsStrip11.w
abbrev V12 : Nat := Rule30SixteenFrontsStrip12.V
abbrev w12 : Nat → Nat := Rule30SixteenFrontsStrip12.w
abbrev V13 : Nat := Rule30SixteenFrontsStrip13.V
abbrev w13 : Nat → Nat := Rule30SixteenFrontsStrip13.w
abbrev V14 : Nat := Rule30SixteenFrontsStrip14.V
abbrev w14 : Nat → Nat := Rule30SixteenFrontsStrip14.w
abbrev V15 : Nat := Rule30SixteenFrontsStrip15.V
abbrev w15 : Nat → Nat := Rule30SixteenFrontsStrip15.w

/-- On one of the strips, wheel by wheel. -/
def OnTree (a : Nat → Nat → Bool) (s : Nat) : Prop :=
  AlignedFrom K a V0 s (F w0) 894235 ∨
  AlignedFrom K a V1 s (F w1) 894235 ∨
  AlignedFrom K a V2 s (F w2) 894235 ∨
  AlignedFrom K a V3 s (F w3) 894235 ∨
  AlignedFrom K a V4 s (F w4) 894235 ∨
  AlignedFrom K a V5 s (F w5) 894235 ∨
  AlignedFrom K a V6 s (F w6) 894235 ∨
  AlignedFrom K a V7 s (F w7) 894235 ∨
  AlignedFrom K a V8 s (F w8) 894235 ∨
  AlignedFrom K a V9 s (F w9) 894235 ∨
  AlignedFrom K a V10 s (F w10) 894235 ∨
  AlignedFrom K a V11 s (F w11) 894235 ∨
  AlignedFrom K a V12 s (F w12) 894235 ∨
  AlignedFrom K a V13 s (F w13) 894235 ∨
  AlignedFrom K a V14 s (F w14) 894235 ∨
  AlignedFrom K a V15 s (F w15) 894235

/-- On one of the strips from strip tick `T`. -/
def OnTreeFrom (a : Nat → Nat → Bool) (s T : Nat) : Prop :=
  OnStrip K a V0 s T 894235 ∨
  OnStrip K a V1 s T 894235 ∨
  OnStrip K a V2 s T 894235 ∨
  OnStrip K a V3 s T 894235 ∨
  OnStrip K a V4 s T 894235 ∨
  OnStrip K a V5 s T 894235 ∨
  OnStrip K a V6 s T 894235 ∨
  OnStrip K a V7 s T 894235 ∨
  OnStrip K a V8 s T 894235 ∨
  OnStrip K a V9 s T 894235 ∨
  OnStrip K a V10 s T 894235 ∨
  OnStrip K a V11 s T 894235 ∨
  OnStrip K a V12 s T 894235 ∨
  OnStrip K a V13 s T 894235 ∨
  OnStrip K a V14 s T 894235 ∨
  OnStrip K a V15 s T 894235

/-- On one of the strips, from some time on. -/
def OnTreeAligned (a : Nat → Nat → Bool) (s : Nat) : Prop :=
  Aligned K a V0 s 894235 ∨
  Aligned K a V1 s 894235 ∨
  Aligned K a V2 s 894235 ∨
  Aligned K a V3 s 894235 ∨
  Aligned K a V4 s 894235 ∨
  Aligned K a V5 s 894235 ∨
  Aligned K a V6 s 894235 ∨
  Aligned K a V7 s 894235 ∨
  Aligned K a V8 s 894235 ∨
  Aligned K a V9 s 894235 ∨
  Aligned K a V10 s 894235 ∨
  Aligned K a V11 s 894235 ∨
  Aligned K a V12 s 894235 ∨
  Aligned K a V13 s 894235 ∨
  Aligned K a V14 s 894235 ∨
  Aligned K a V15 s 894235

theorem inj0 {a : Nat → Nat → Bool} {s : Nat} (h : AlignedFrom K a V0 s (F w0) 894235) : OnTree a s := Or.inl h
theorem inj1 {a : Nat → Nat → Bool} {s : Nat} (h : AlignedFrom K a V1 s (F w1) 894235) : OnTree a s := Or.inr (Or.inl h)
theorem inj2 {a : Nat → Nat → Bool} {s : Nat} (h : AlignedFrom K a V2 s (F w2) 894235) : OnTree a s := Or.inr (Or.inr (Or.inl h))
theorem inj3 {a : Nat → Nat → Bool} {s : Nat} (h : AlignedFrom K a V3 s (F w3) 894235) : OnTree a s := Or.inr (Or.inr (Or.inr (Or.inl h)))
theorem inj4 {a : Nat → Nat → Bool} {s : Nat} (h : AlignedFrom K a V4 s (F w4) 894235) : OnTree a s := Or.inr (Or.inr (Or.inr (Or.inr (Or.inl h))))
theorem inj5 {a : Nat → Nat → Bool} {s : Nat} (h : AlignedFrom K a V5 s (F w5) 894235) : OnTree a s := Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl h)))))
theorem inj6 {a : Nat → Nat → Bool} {s : Nat} (h : AlignedFrom K a V6 s (F w6) 894235) : OnTree a s := Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl h))))))
theorem inj7 {a : Nat → Nat → Bool} {s : Nat} (h : AlignedFrom K a V7 s (F w7) 894235) : OnTree a s := Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl h)))))))
theorem inj8 {a : Nat → Nat → Bool} {s : Nat} (h : AlignedFrom K a V8 s (F w8) 894235) : OnTree a s := Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl h))))))))
theorem inj9 {a : Nat → Nat → Bool} {s : Nat} (h : AlignedFrom K a V9 s (F w9) 894235) : OnTree a s := Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl h)))))))))
theorem inj10 {a : Nat → Nat → Bool} {s : Nat} (h : AlignedFrom K a V10 s (F w10) 894235) : OnTree a s := Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl h))))))))))
theorem inj11 {a : Nat → Nat → Bool} {s : Nat} (h : AlignedFrom K a V11 s (F w11) 894235) : OnTree a s := Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl h)))))))))))
theorem inj12 {a : Nat → Nat → Bool} {s : Nat} (h : AlignedFrom K a V12 s (F w12) 894235) : OnTree a s := Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl h))))))))))))
theorem inj13 {a : Nat → Nat → Bool} {s : Nat} (h : AlignedFrom K a V13 s (F w13) 894235) : OnTree a s := Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl h)))))))))))))
theorem inj14 {a : Nat → Nat → Bool} {s : Nat} (h : AlignedFrom K a V14 s (F w14) 894235) : OnTree a s := Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl h))))))))))))))
theorem inj15 {a : Nat → Nat → Bool} {s : Nat} (h : AlignedFrom K a V15 s (F w15) 894235) : OnTree a s := Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (h)))))))))))))))

theorem onTreeFrom_of_onTree {a : Nat → Nat → Bool} {s : Nat} (h : OnTree a s) : OnTreeFrom a s 1798243 := by
  unfold OnTree at h
  rcases h with h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h
  · exact Or.inl (onStrip_of_alignedFrom (fun j hj => Nat.le_trans (Rule30SixteenFrontsStrip0.front_le j hj) (by decide)) h)
  · exact Or.inr (Or.inl (onStrip_of_alignedFrom (fun j hj => Nat.le_trans (Rule30SixteenFrontsStrip1.front_le j hj) (by decide)) h))
  · exact Or.inr (Or.inr (Or.inl (onStrip_of_alignedFrom (fun j hj => Nat.le_trans (Rule30SixteenFrontsStrip2.front_le j hj) (by decide)) h)))
  · exact Or.inr (Or.inr (Or.inr (Or.inl (onStrip_of_alignedFrom (fun j hj => Nat.le_trans (Rule30SixteenFrontsStrip3.front_le j hj) (by decide)) h))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (onStrip_of_alignedFrom (fun j hj => Nat.le_trans (Rule30SixteenFrontsStrip4.front_le j hj) (by decide)) h)))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (onStrip_of_alignedFrom (fun j hj => Nat.le_trans (Rule30SixteenFrontsStrip5.front_le j hj) (by decide)) h))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (onStrip_of_alignedFrom (fun j hj => Nat.le_trans (Rule30SixteenFrontsStrip6.front_le j hj) (by decide)) h)))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (onStrip_of_alignedFrom (fun j hj => Nat.le_trans (Rule30SixteenFrontsStrip7.front_le j hj) (by decide)) h))))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (onStrip_of_alignedFrom (fun j hj => Nat.le_trans (Rule30SixteenFrontsStrip8.front_le j hj) (by decide)) h)))))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (onStrip_of_alignedFrom (fun j hj => Nat.le_trans (Rule30SixteenFrontsStrip9.front_le j hj) (by decide)) h))))))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (onStrip_of_alignedFrom (fun j hj => Nat.le_trans (Rule30SixteenFrontsStrip10.front_le j hj) (by decide)) h)))))))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (onStrip_of_alignedFrom (fun j hj => Nat.le_trans (Rule30SixteenFrontsStrip11.front_le j hj) (by decide)) h))))))))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (onStrip_of_alignedFrom (fun j hj => Nat.le_trans (Rule30SixteenFrontsStrip12.front_le j hj) (by decide)) h)))))))))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (onStrip_of_alignedFrom (fun j hj => Nat.le_trans (Rule30SixteenFrontsStrip13.front_le j hj) (by decide)) h))))))))))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (onStrip_of_alignedFrom (fun j hj => Nat.le_trans (Rule30SixteenFrontsStrip14.front_le j hj) (by decide)) h)))))))))))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr ((onStrip_of_alignedFrom (fun j hj => Nat.le_trans (Rule30SixteenFrontsStrip15.front_le j hj) (by decide)) h))))))))))))))))

theorem onTreeAligned_of_onTree {a : Nat → Nat → Bool} {s : Nat} (h : OnTree a s) : OnTreeAligned a s := by
  unfold OnTree at h
  rcases h with h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h
  · exact Or.inl (aligned_of_alignedFrom h)
  · exact Or.inr (Or.inl (aligned_of_alignedFrom h))
  · exact Or.inr (Or.inr (Or.inl (aligned_of_alignedFrom h)))
  · exact Or.inr (Or.inr (Or.inr (Or.inl (aligned_of_alignedFrom h))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (aligned_of_alignedFrom h)))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (aligned_of_alignedFrom h))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (aligned_of_alignedFrom h)))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (aligned_of_alignedFrom h))))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (aligned_of_alignedFrom h)))))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (aligned_of_alignedFrom h))))))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (aligned_of_alignedFrom h)))))))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (aligned_of_alignedFrom h))))))))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (aligned_of_alignedFrom h)))))))))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (aligned_of_alignedFrom h))))))))))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (aligned_of_alignedFrom h)))))))))))))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr ((aligned_of_alignedFrom h))))))))))))))))

/-! ### The tree, strip by strip, in post-order -/

theorem done3 {a : Nat → Nat → Bool} (ha : Recurrence a) {s : Nat} (h : AlignedFrom K a V3 s (F w3) 72576) :
    ∃ s', s' ≤ s + 16 ∧ OnTree a s' := by
  have h0 : AlignedFrom K a V3 s (F w3) 72576 := h
  have h0e : AlignedFrom K a V3 s (F w3) 291256 :=
    extend_from ha Rule30SixteenFrontsStrip3.V_return Rule30SixteenFrontsStrip3.words (by omega) (by decide) (by omega) h0 Rule30SixteenFrontsStrip3.b_72576_291256
  rcases step_white ha Rule30SixteenFrontsStrip3.V_return Rule30SixteenFrontsStrip3.words (by decide) h0e Rule30SixteenFrontsStrip3.w_291256 with h0eL | h0eR
  · -- aligned through the doubled wheel 291257, same shift
    exact ⟨s, by omega, inj3 (extend_from ha Rule30SixteenFrontsStrip3.V_return Rule30SixteenFrontsStrip3.words (by omega) (by decide) (by omega) h0eL Rule30SixteenFrontsStrip3.b_291257_894235)⟩
  · -- the complement: a shift by 16
    have h0eS : AlignedFrom K a V3 (s + 16) (F w3) 291257 := white_shift h0e h0eR
      (strip_shift Rule30SixteenFrontsStrip3.V_return Rule30SixteenFrontsStrip3.per_291256 Rule30SixteenFrontsStrip3.anti_291256).1 (strip_shift Rule30SixteenFrontsStrip3.V_return Rule30SixteenFrontsStrip3.per_291256 Rule30SixteenFrontsStrip3.anti_291256).2
    exact ⟨(s + 16), by omega, inj3 (extend_from ha Rule30SixteenFrontsStrip3.V_return Rule30SixteenFrontsStrip3.words (by omega) (by decide) (by omega) h0eS Rule30SixteenFrontsStrip3.b_291257_894235)⟩

theorem done7 {a : Nat → Nat → Bool} (ha : Recurrence a) {s : Nat} (h : AlignedFrom K a V7 s (F w7) 243768) :
    ∃ s', s' ≤ s + 16 ∧ OnTree a s' := by
  have h0 : AlignedFrom K a V7 s (F w7) 243768 := h
  have h0e : AlignedFrom K a V7 s (F w7) 253536 :=
    extend_from ha Rule30SixteenFrontsStrip7.V_return Rule30SixteenFrontsStrip7.words (by omega) (by decide) (by omega) h0 Rule30SixteenFrontsStrip7.b_243768_253536
  rcases step_white ha Rule30SixteenFrontsStrip7.V_return Rule30SixteenFrontsStrip7.words (by decide) h0e Rule30SixteenFrontsStrip7.w_253536 with h0eL | h0eR
  · -- aligned through the doubled wheel 253537, same shift
    exact ⟨s, by omega, inj7 (extend_from ha Rule30SixteenFrontsStrip7.V_return Rule30SixteenFrontsStrip7.words (by omega) (by decide) (by omega) h0eL Rule30SixteenFrontsStrip7.b_253537_894235)⟩
  · -- the complement: a shift by 16
    have h0eS : AlignedFrom K a V7 (s + 16) (F w7) 253537 := white_shift h0e h0eR
      (strip_shift Rule30SixteenFrontsStrip7.V_return Rule30SixteenFrontsStrip7.per_253536 Rule30SixteenFrontsStrip7.anti_253536).1 (strip_shift Rule30SixteenFrontsStrip7.V_return Rule30SixteenFrontsStrip7.per_253536 Rule30SixteenFrontsStrip7.anti_253536).2
    exact ⟨(s + 16), by omega, inj7 (extend_from ha Rule30SixteenFrontsStrip7.V_return Rule30SixteenFrontsStrip7.words (by omega) (by decide) (by omega) h0eS Rule30SixteenFrontsStrip7.b_253537_894235)⟩

theorem done8 {a : Nat → Nat → Bool} (ha : Recurrence a) {s : Nat} (h : AlignedFrom K a V8 s (F w8) 350244) :
    ∃ s', s' ≤ s + 16 ∧ OnTree a s' := by
  have h0 : AlignedFrom K a V8 s (F w8) 350244 := h
  have h0e : AlignedFrom K a V8 s (F w8) 551909 :=
    extend_from ha Rule30SixteenFrontsStrip8.V_return Rule30SixteenFrontsStrip8.words (by omega) (by decide) (by omega) h0 Rule30SixteenFrontsStrip8.b_350244_551909
  rcases step_white ha Rule30SixteenFrontsStrip8.V_return Rule30SixteenFrontsStrip8.words (by decide) h0e Rule30SixteenFrontsStrip8.w_551909 with h0eL | h0eR
  · -- aligned through the doubled wheel 551910, same shift
    exact ⟨s, by omega, inj8 (extend_from ha Rule30SixteenFrontsStrip8.V_return Rule30SixteenFrontsStrip8.words (by omega) (by decide) (by omega) h0eL Rule30SixteenFrontsStrip8.b_551910_894235)⟩
  · -- the complement: a shift by 16
    have h0eS : AlignedFrom K a V8 (s + 16) (F w8) 551910 := white_shift h0e h0eR
      (strip_shift Rule30SixteenFrontsStrip8.V_return Rule30SixteenFrontsStrip8.per_551909 Rule30SixteenFrontsStrip8.anti_551909).1 (strip_shift Rule30SixteenFrontsStrip8.V_return Rule30SixteenFrontsStrip8.per_551909 Rule30SixteenFrontsStrip8.anti_551909).2
    exact ⟨(s + 16), by omega, inj8 (extend_from ha Rule30SixteenFrontsStrip8.V_return Rule30SixteenFrontsStrip8.words (by omega) (by decide) (by omega) h0eS Rule30SixteenFrontsStrip8.b_551910_894235)⟩

theorem done13 {a : Nat → Nat → Bool} (ha : Recurrence a) {s : Nat} (h : AlignedFrom K a V13 s (F w13) 482609) :
    ∃ s', s' ≤ s + 16 ∧ OnTree a s' := by
  have h0 : AlignedFrom K a V13 s (F w13) 482609 := h
  have h0e : AlignedFrom K a V13 s (F w13) 527723 :=
    extend_from ha Rule30SixteenFrontsStrip13.V_return Rule30SixteenFrontsStrip13.words (by omega) (by decide) (by omega) h0 Rule30SixteenFrontsStrip13.b_482609_527723
  rcases step_white ha Rule30SixteenFrontsStrip13.V_return Rule30SixteenFrontsStrip13.words (by decide) h0e Rule30SixteenFrontsStrip13.w_527723 with h0eL | h0eR
  · -- aligned through the doubled wheel 527724, same shift
    exact ⟨s, by omega, inj13 (extend_from ha Rule30SixteenFrontsStrip13.V_return Rule30SixteenFrontsStrip13.words (by omega) (by decide) (by omega) h0eL Rule30SixteenFrontsStrip13.b_527724_894235)⟩
  · -- the complement: a shift by 16
    have h0eS : AlignedFrom K a V13 (s + 16) (F w13) 527724 := white_shift h0e h0eR
      (strip_shift Rule30SixteenFrontsStrip13.V_return Rule30SixteenFrontsStrip13.per_527723 Rule30SixteenFrontsStrip13.anti_527723).1 (strip_shift Rule30SixteenFrontsStrip13.V_return Rule30SixteenFrontsStrip13.per_527723 Rule30SixteenFrontsStrip13.anti_527723).2
    exact ⟨(s + 16), by omega, inj13 (extend_from ha Rule30SixteenFrontsStrip13.V_return Rule30SixteenFrontsStrip13.words (by omega) (by decide) (by omega) h0eS Rule30SixteenFrontsStrip13.b_527724_894235)⟩

theorem done14 {a : Nat → Nat → Bool} (ha : Recurrence a) {s : Nat} (h : AlignedFrom K a V14 s (F w14) 603583) :
    ∃ s', s' ≤ s + 16 ∧ OnTree a s' := by
  have h0 : AlignedFrom K a V14 s (F w14) 603583 := h
  have h0e : AlignedFrom K a V14 s (F w14) 645654 :=
    extend_from ha Rule30SixteenFrontsStrip14.V_return Rule30SixteenFrontsStrip14.words (by omega) (by decide) (by omega) h0 Rule30SixteenFrontsStrip14.b_603583_645654
  rcases step_white ha Rule30SixteenFrontsStrip14.V_return Rule30SixteenFrontsStrip14.words (by decide) h0e Rule30SixteenFrontsStrip14.w_645654 with h0eL | h0eR
  · -- aligned through the doubled wheel 645655, same shift
    exact ⟨s, by omega, inj14 (extend_from ha Rule30SixteenFrontsStrip14.V_return Rule30SixteenFrontsStrip14.words (by omega) (by decide) (by omega) h0eL Rule30SixteenFrontsStrip14.b_645655_894235)⟩
  · -- the complement: a shift by 16
    have h0eS : AlignedFrom K a V14 (s + 16) (F w14) 645655 := white_shift h0e h0eR
      (strip_shift Rule30SixteenFrontsStrip14.V_return Rule30SixteenFrontsStrip14.per_645654 Rule30SixteenFrontsStrip14.anti_645654).1 (strip_shift Rule30SixteenFrontsStrip14.V_return Rule30SixteenFrontsStrip14.per_645654 Rule30SixteenFrontsStrip14.anti_645654).2
    exact ⟨(s + 16), by omega, inj14 (extend_from ha Rule30SixteenFrontsStrip14.V_return Rule30SixteenFrontsStrip14.words (by omega) (by decide) (by omega) h0eS Rule30SixteenFrontsStrip14.b_645655_894235)⟩

theorem done9 {a : Nat → Nat → Bool} (ha : Recurrence a) {s : Nat} (h : AlignedFrom K a V9 s (F w9) 445475) :
    ∃ s', s' ≤ s + 16 ∧ OnTree a s' := by
  have h0 : AlignedFrom K a V9 s (F w9) 445475 := h
  have h0e : AlignedFrom K a V9 s (F w9) 482608 :=
    extend_from ha Rule30SixteenFrontsStrip9.V_return Rule30SixteenFrontsStrip9.words (by omega) (by decide) (by omega) h0 Rule30SixteenFrontsStrip9.b_445475_482608
  rcases step_white ha Rule30SixteenFrontsStrip9.V_return Rule30SixteenFrontsStrip9.words (by decide) h0e Rule30SixteenFrontsStrip9.w_482608 with h0eL | h0eR
  · -- the same side at the fork 482608
    have h0eLe : AlignedFrom K a V9 s (F w9) 603582 :=
      extend_from ha Rule30SixteenFrontsStrip9.V_return Rule30SixteenFrontsStrip9.words (by omega) (by decide) (by omega) h0eL Rule30SixteenFrontsStrip9.b_482609_603582
    rcases step_white ha Rule30SixteenFrontsStrip9.V_return Rule30SixteenFrontsStrip9.words (by decide) h0eLe Rule30SixteenFrontsStrip9.w_603582 with h0eLeL | h0eLeR
    · -- the same side at the fork 603582
      have h0eLeLe : AlignedFrom K a V9 s (F w9) 634885 :=
        extend_from ha Rule30SixteenFrontsStrip9.V_return Rule30SixteenFrontsStrip9.words (by omega) (by decide) (by omega) h0eLeL Rule30SixteenFrontsStrip9.b_603583_634885
      rcases step_white ha Rule30SixteenFrontsStrip9.V_return Rule30SixteenFrontsStrip9.words (by decide) h0eLeLe Rule30SixteenFrontsStrip9.w_634885 with h0eLeLeL | h0eLeLeR
      · -- aligned through the doubled wheel 634886, same shift
        exact ⟨s, by omega, inj9 (extend_from ha Rule30SixteenFrontsStrip9.V_return Rule30SixteenFrontsStrip9.words (by omega) (by decide) (by omega) h0eLeLeL Rule30SixteenFrontsStrip9.b_634886_894235)⟩
      · -- the complement: a shift by 16
        have h0eLeLeS : AlignedFrom K a V9 (s + 16) (F w9) 634886 := white_shift h0eLeLe h0eLeLeR
          (strip_shift Rule30SixteenFrontsStrip9.V_return Rule30SixteenFrontsStrip9.per_634885 Rule30SixteenFrontsStrip9.anti_634885).1 (strip_shift Rule30SixteenFrontsStrip9.V_return Rule30SixteenFrontsStrip9.per_634885 Rule30SixteenFrontsStrip9.anti_634885).2
        exact ⟨(s + 16), by omega, inj9 (extend_from ha Rule30SixteenFrontsStrip9.V_return Rule30SixteenFrontsStrip9.words (by omega) (by decide) (by omega) h0eLeLeS Rule30SixteenFrontsStrip9.b_634886_894235)⟩
    · -- the other side: strip 14
      have h0eLeF : AlignedFrom K a V14 s (F w9) 603583 := white_fork h0eLe h0eLeR
        (fun j t hj => (Rule30SixteenFrontsStrip14.low_V' j t (by omega)))
        Rule30SixteenFrontsStrip14.comp_V
      have h0eLeG : AlignedFrom K a V14 s (F w14) 603583 :=
        alignedFrom_congr (fun j hj => F_congr j (fun i hi => Rule30SixteenFrontsStrip14.w_eq i (by omega))) h0eLeF
      exact done14 ha h0eLeG
  · -- the other side: strip 13
    have h0eF : AlignedFrom K a V13 s (F w9) 482609 := white_fork h0e h0eR
      (fun j t hj => (Rule30SixteenFrontsStrip13.low_V' j t (by omega)))
      Rule30SixteenFrontsStrip13.comp_V
    have h0eG : AlignedFrom K a V13 s (F w13) 482609 :=
      alignedFrom_congr (fun j hj => F_congr j (fun i hi => Rule30SixteenFrontsStrip13.w_eq i (by omega))) h0eF
    exact done13 ha h0eG

theorem done10 {a : Nat → Nat → Bool} (ha : Recurrence a) {s : Nat} (h : AlignedFrom K a V10 s (F w10) 485620) :
    ∃ s', s' ≤ s + 16 ∧ OnTree a s' := by
  have h0 : AlignedFrom K a V10 s (F w10) 485620 := h
  have h0e : AlignedFrom K a V10 s (F w10) 555812 :=
    extend_from ha Rule30SixteenFrontsStrip10.V_return Rule30SixteenFrontsStrip10.words (by omega) (by decide) (by omega) h0 Rule30SixteenFrontsStrip10.b_485620_555812
  rcases step_white ha Rule30SixteenFrontsStrip10.V_return Rule30SixteenFrontsStrip10.words (by decide) h0e Rule30SixteenFrontsStrip10.w_555812 with h0eL | h0eR
  · -- aligned through the doubled wheel 555813, same shift
    exact ⟨s, by omega, inj10 (extend_from ha Rule30SixteenFrontsStrip10.V_return Rule30SixteenFrontsStrip10.words (by omega) (by decide) (by omega) h0eL Rule30SixteenFrontsStrip10.b_555813_894235)⟩
  · -- the complement: a shift by 16
    have h0eS : AlignedFrom K a V10 (s + 16) (F w10) 555813 := white_shift h0e h0eR
      (strip_shift Rule30SixteenFrontsStrip10.V_return Rule30SixteenFrontsStrip10.per_555812 Rule30SixteenFrontsStrip10.anti_555812).1 (strip_shift Rule30SixteenFrontsStrip10.V_return Rule30SixteenFrontsStrip10.per_555812 Rule30SixteenFrontsStrip10.anti_555812).2
    exact ⟨(s + 16), by omega, inj10 (extend_from ha Rule30SixteenFrontsStrip10.V_return Rule30SixteenFrontsStrip10.words (by omega) (by decide) (by omega) h0eS Rule30SixteenFrontsStrip10.b_555813_894235)⟩

theorem done11 {a : Nat → Nat → Bool} (ha : Recurrence a) {s : Nat} (h : AlignedFrom K a V11 s (F w11) 537693) :
    ∃ s', s' ≤ s + 16 ∧ OnTree a s' := by
  have h0 : AlignedFrom K a V11 s (F w11) 537693 := h
  have h0e : AlignedFrom K a V11 s (F w11) 667051 :=
    extend_from ha Rule30SixteenFrontsStrip11.V_return Rule30SixteenFrontsStrip11.words (by omega) (by decide) (by omega) h0 Rule30SixteenFrontsStrip11.b_537693_667051
  rcases step_white ha Rule30SixteenFrontsStrip11.V_return Rule30SixteenFrontsStrip11.words (by decide) h0e Rule30SixteenFrontsStrip11.w_667051 with h0eL | h0eR
  · -- aligned through the doubled wheel 667052, same shift
    exact ⟨s, by omega, inj11 (extend_from ha Rule30SixteenFrontsStrip11.V_return Rule30SixteenFrontsStrip11.words (by omega) (by decide) (by omega) h0eL Rule30SixteenFrontsStrip11.b_667052_894235)⟩
  · -- the complement: a shift by 16
    have h0eS : AlignedFrom K a V11 (s + 16) (F w11) 667052 := white_shift h0e h0eR
      (strip_shift Rule30SixteenFrontsStrip11.V_return Rule30SixteenFrontsStrip11.per_667051 Rule30SixteenFrontsStrip11.anti_667051).1 (strip_shift Rule30SixteenFrontsStrip11.V_return Rule30SixteenFrontsStrip11.per_667051 Rule30SixteenFrontsStrip11.anti_667051).2
    exact ⟨(s + 16), by omega, inj11 (extend_from ha Rule30SixteenFrontsStrip11.V_return Rule30SixteenFrontsStrip11.words (by omega) (by decide) (by omega) h0eS Rule30SixteenFrontsStrip11.b_667052_894235)⟩

theorem done15 {a : Nat → Nat → Bool} (ha : Recurrence a) {s : Nat} (h : AlignedFrom K a V15 s (F w15) 760455) :
    ∃ s', s' ≤ s + 16 ∧ OnTree a s' := by
  have h0 : AlignedFrom K a V15 s (F w15) 760455 := h
  have h0e : AlignedFrom K a V15 s (F w15) 894234 :=
    extend_from ha Rule30SixteenFrontsStrip15.V_return Rule30SixteenFrontsStrip15.words (by omega) (by decide) (by omega) h0 Rule30SixteenFrontsStrip15.b_760455_894234
  rcases step_white ha Rule30SixteenFrontsStrip15.V_return Rule30SixteenFrontsStrip15.words (by decide) h0e Rule30SixteenFrontsStrip15.w_894234 with h0eL | h0eR
  · -- aligned through the doubled wheel 894235, same shift
    exact ⟨s, by omega, inj15 (extend_from ha Rule30SixteenFrontsStrip15.V_return Rule30SixteenFrontsStrip15.words (by omega) (by decide) (by omega) h0eL Rule30SixteenFrontsStrip15.b_894235_894235)⟩
  · -- the complement: a shift by 16
    have h0eS : AlignedFrom K a V15 (s + 16) (F w15) 894235 := white_shift h0e h0eR
      (strip_shift Rule30SixteenFrontsStrip15.V_return Rule30SixteenFrontsStrip15.per_894234 Rule30SixteenFrontsStrip15.anti_894234).1 (strip_shift Rule30SixteenFrontsStrip15.V_return Rule30SixteenFrontsStrip15.per_894234 Rule30SixteenFrontsStrip15.anti_894234).2
    exact ⟨(s + 16), by omega, inj15 (extend_from ha Rule30SixteenFrontsStrip15.V_return Rule30SixteenFrontsStrip15.words (by omega) (by decide) (by omega) h0eS Rule30SixteenFrontsStrip15.b_894235_894235)⟩

theorem done12 {a : Nat → Nat → Bool} (ha : Recurrence a) {s : Nat} (h : AlignedFrom K a V12 s (F w12) 563843) :
    ∃ s', s' ≤ s + 16 ∧ OnTree a s' := by
  have h0 : AlignedFrom K a V12 s (F w12) 563843 := h
  have h0e : AlignedFrom K a V12 s (F w12) 760454 :=
    extend_from ha Rule30SixteenFrontsStrip12.V_return Rule30SixteenFrontsStrip12.words (by omega) (by decide) (by omega) h0 Rule30SixteenFrontsStrip12.b_563843_760454
  rcases step_white ha Rule30SixteenFrontsStrip12.V_return Rule30SixteenFrontsStrip12.words (by decide) h0e Rule30SixteenFrontsStrip12.w_760454 with h0eL | h0eR
  · -- the same side at the fork 760454
    have h0eLe : AlignedFrom K a V12 s (F w12) 770531 :=
      extend_from ha Rule30SixteenFrontsStrip12.V_return Rule30SixteenFrontsStrip12.words (by omega) (by decide) (by omega) h0eL Rule30SixteenFrontsStrip12.b_760455_770531
    rcases step_white ha Rule30SixteenFrontsStrip12.V_return Rule30SixteenFrontsStrip12.words (by decide) h0eLe Rule30SixteenFrontsStrip12.w_770531 with h0eLeL | h0eLeR
    · -- aligned through the doubled wheel 770532, same shift
      exact ⟨s, by omega, inj12 (extend_from ha Rule30SixteenFrontsStrip12.V_return Rule30SixteenFrontsStrip12.words (by omega) (by decide) (by omega) h0eLeL Rule30SixteenFrontsStrip12.b_770532_894235)⟩
    · -- the complement: a shift by 16
      have h0eLeS : AlignedFrom K a V12 (s + 16) (F w12) 770532 := white_shift h0eLe h0eLeR
        (strip_shift Rule30SixteenFrontsStrip12.V_return Rule30SixteenFrontsStrip12.per_770531 Rule30SixteenFrontsStrip12.anti_770531).1 (strip_shift Rule30SixteenFrontsStrip12.V_return Rule30SixteenFrontsStrip12.per_770531 Rule30SixteenFrontsStrip12.anti_770531).2
      exact ⟨(s + 16), by omega, inj12 (extend_from ha Rule30SixteenFrontsStrip12.V_return Rule30SixteenFrontsStrip12.words (by omega) (by decide) (by omega) h0eLeS Rule30SixteenFrontsStrip12.b_770532_894235)⟩
  · -- the other side: strip 15
    have h0eF : AlignedFrom K a V15 s (F w12) 760455 := white_fork h0e h0eR
      (fun j t hj => (Rule30SixteenFrontsStrip15.low_V' j t (by omega)))
      Rule30SixteenFrontsStrip15.comp_V
    have h0eG : AlignedFrom K a V15 s (F w15) 760455 :=
      alignedFrom_congr (fun j hj => F_congr j (fun i hi => Rule30SixteenFrontsStrip15.w_eq i (by omega))) h0eF
    exact done15 ha h0eG

theorem done5 {a : Nat → Nat → Bool} (ha : Recurrence a) {s : Nat} (h : AlignedFrom K a V5 s (F w5) 174450) :
    ∃ s', s' ≤ s + 16 ∧ OnTree a s' := by
  have h0 : AlignedFrom K a V5 s (F w5) 174450 := h
  have h0e : AlignedFrom K a V5 s (F w5) 243767 :=
    extend_from ha Rule30SixteenFrontsStrip5.V_return Rule30SixteenFrontsStrip5.words (by omega) (by decide) (by omega) h0 Rule30SixteenFrontsStrip5.b_174450_243767
  rcases step_white ha Rule30SixteenFrontsStrip5.V_return Rule30SixteenFrontsStrip5.words (by decide) h0e Rule30SixteenFrontsStrip5.w_243767 with h0eL | h0eR
  · -- the same side at the fork 243767
    have h0eLe : AlignedFrom K a V5 s (F w5) 350243 :=
      extend_from ha Rule30SixteenFrontsStrip5.V_return Rule30SixteenFrontsStrip5.words (by omega) (by decide) (by omega) h0eL Rule30SixteenFrontsStrip5.b_243768_350243
    rcases step_white ha Rule30SixteenFrontsStrip5.V_return Rule30SixteenFrontsStrip5.words (by decide) h0eLe Rule30SixteenFrontsStrip5.w_350243 with h0eLeL | h0eLeR
    · -- the same side at the fork 350243
      have h0eLeLe : AlignedFrom K a V5 s (F w5) 445474 :=
        extend_from ha Rule30SixteenFrontsStrip5.V_return Rule30SixteenFrontsStrip5.words (by omega) (by decide) (by omega) h0eLeL Rule30SixteenFrontsStrip5.b_350244_445474
      rcases step_white ha Rule30SixteenFrontsStrip5.V_return Rule30SixteenFrontsStrip5.words (by decide) h0eLeLe Rule30SixteenFrontsStrip5.w_445474 with h0eLeLeL | h0eLeLeR
      · -- the same side at the fork 445474
        have h0eLeLeLe : AlignedFrom K a V5 s (F w5) 485619 :=
          extend_from ha Rule30SixteenFrontsStrip5.V_return Rule30SixteenFrontsStrip5.words (by omega) (by decide) (by omega) h0eLeLeL Rule30SixteenFrontsStrip5.b_445475_485619
        rcases step_white ha Rule30SixteenFrontsStrip5.V_return Rule30SixteenFrontsStrip5.words (by decide) h0eLeLeLe Rule30SixteenFrontsStrip5.w_485619 with h0eLeLeLeL | h0eLeLeLeR
        · -- the same side at the fork 485619
          have h0eLeLeLeLe : AlignedFrom K a V5 s (F w5) 537692 :=
            extend_from ha Rule30SixteenFrontsStrip5.V_return Rule30SixteenFrontsStrip5.words (by omega) (by decide) (by omega) h0eLeLeLeL Rule30SixteenFrontsStrip5.b_485620_537692
          rcases step_white ha Rule30SixteenFrontsStrip5.V_return Rule30SixteenFrontsStrip5.words (by decide) h0eLeLeLeLe Rule30SixteenFrontsStrip5.w_537692 with h0eLeLeLeLeL | h0eLeLeLeLeR
          · -- the same side at the fork 537692
            have h0eLeLeLeLeLe : AlignedFrom K a V5 s (F w5) 563842 :=
              extend_from ha Rule30SixteenFrontsStrip5.V_return Rule30SixteenFrontsStrip5.words (by omega) (by decide) (by omega) h0eLeLeLeLeL Rule30SixteenFrontsStrip5.b_537693_563842
            rcases step_white ha Rule30SixteenFrontsStrip5.V_return Rule30SixteenFrontsStrip5.words (by decide) h0eLeLeLeLeLe Rule30SixteenFrontsStrip5.w_563842 with h0eLeLeLeLeLeL | h0eLeLeLeLeLeR
            · -- the same side at the fork 563842
              have h0eLeLeLeLeLeLe : AlignedFrom K a V5 s (F w5) 575210 :=
                extend_from ha Rule30SixteenFrontsStrip5.V_return Rule30SixteenFrontsStrip5.words (by omega) (by decide) (by omega) h0eLeLeLeLeLeL Rule30SixteenFrontsStrip5.b_563843_575210
              rcases step_white ha Rule30SixteenFrontsStrip5.V_return Rule30SixteenFrontsStrip5.words (by decide) h0eLeLeLeLeLeLe Rule30SixteenFrontsStrip5.w_575210 with h0eLeLeLeLeLeLeL | h0eLeLeLeLeLeLeR
              · -- aligned through the doubled wheel 575211, same shift
                exact ⟨s, by omega, inj5 (extend_from ha Rule30SixteenFrontsStrip5.V_return Rule30SixteenFrontsStrip5.words (by omega) (by decide) (by omega) h0eLeLeLeLeLeLeL Rule30SixteenFrontsStrip5.b_575211_894235)⟩
              · -- the complement: a shift by 16
                have h0eLeLeLeLeLeLeS : AlignedFrom K a V5 (s + 16) (F w5) 575211 := white_shift h0eLeLeLeLeLeLe h0eLeLeLeLeLeLeR
                  (strip_shift Rule30SixteenFrontsStrip5.V_return Rule30SixteenFrontsStrip5.per_575210 Rule30SixteenFrontsStrip5.anti_575210).1 (strip_shift Rule30SixteenFrontsStrip5.V_return Rule30SixteenFrontsStrip5.per_575210 Rule30SixteenFrontsStrip5.anti_575210).2
                exact ⟨(s + 16), by omega, inj5 (extend_from ha Rule30SixteenFrontsStrip5.V_return Rule30SixteenFrontsStrip5.words (by omega) (by decide) (by omega) h0eLeLeLeLeLeLeS Rule30SixteenFrontsStrip5.b_575211_894235)⟩
            · -- the other side: strip 12
              have h0eLeLeLeLeLeF : AlignedFrom K a V12 s (F w5) 563843 := white_fork h0eLeLeLeLeLe h0eLeLeLeLeLeR
                (fun j t hj => (Rule30SixteenFrontsStrip12.low_V' j t (by omega)))
                Rule30SixteenFrontsStrip12.comp_V
              have h0eLeLeLeLeLeG : AlignedFrom K a V12 s (F w12) 563843 :=
                alignedFrom_congr (fun j hj => F_congr j (fun i hi => Rule30SixteenFrontsStrip12.w_eq i (by omega))) h0eLeLeLeLeLeF
              exact done12 ha h0eLeLeLeLeLeG
          · -- the other side: strip 11
            have h0eLeLeLeLeF : AlignedFrom K a V11 s (F w5) 537693 := white_fork h0eLeLeLeLe h0eLeLeLeLeR
              (fun j t hj => (Rule30SixteenFrontsStrip11.low_V' j t (by omega)))
              Rule30SixteenFrontsStrip11.comp_V
            have h0eLeLeLeLeG : AlignedFrom K a V11 s (F w11) 537693 :=
              alignedFrom_congr (fun j hj => F_congr j (fun i hi => Rule30SixteenFrontsStrip11.w_eq i (by omega))) h0eLeLeLeLeF
            exact done11 ha h0eLeLeLeLeG
        · -- the other side: strip 10
          have h0eLeLeLeF : AlignedFrom K a V10 s (F w5) 485620 := white_fork h0eLeLeLe h0eLeLeLeR
            (fun j t hj => (Rule30SixteenFrontsStrip10.low_V' j t (by omega)))
            Rule30SixteenFrontsStrip10.comp_V
          have h0eLeLeLeG : AlignedFrom K a V10 s (F w10) 485620 :=
            alignedFrom_congr (fun j hj => F_congr j (fun i hi => Rule30SixteenFrontsStrip10.w_eq i (by omega))) h0eLeLeLeF
          exact done10 ha h0eLeLeLeG
      · -- the other side: strip 9
        have h0eLeLeF : AlignedFrom K a V9 s (F w5) 445475 := white_fork h0eLeLe h0eLeLeR
          (fun j t hj => (Rule30SixteenFrontsStrip9.low_V' j t (by omega)))
          Rule30SixteenFrontsStrip9.comp_V
        have h0eLeLeG : AlignedFrom K a V9 s (F w9) 445475 :=
          alignedFrom_congr (fun j hj => F_congr j (fun i hi => Rule30SixteenFrontsStrip9.w_eq i (by omega))) h0eLeLeF
        exact done9 ha h0eLeLeG
    · -- the other side: strip 8
      have h0eLeF : AlignedFrom K a V8 s (F w5) 350244 := white_fork h0eLe h0eLeR
        (fun j t hj => (Rule30SixteenFrontsStrip8.low_V' j t (by omega)))
        Rule30SixteenFrontsStrip8.comp_V
      have h0eLeG : AlignedFrom K a V8 s (F w8) 350244 :=
        alignedFrom_congr (fun j hj => F_congr j (fun i hi => Rule30SixteenFrontsStrip8.w_eq i (by omega))) h0eLeF
      exact done8 ha h0eLeG
  · -- the other side: strip 7
    have h0eF : AlignedFrom K a V7 s (F w5) 243768 := white_fork h0e h0eR
      (fun j t hj => (Rule30SixteenFrontsStrip7.low_V' j t (by omega)))
      Rule30SixteenFrontsStrip7.comp_V
    have h0eG : AlignedFrom K a V7 s (F w7) 243768 :=
      alignedFrom_congr (fun j hj => F_congr j (fun i hi => Rule30SixteenFrontsStrip7.w_eq i (by omega))) h0eF
    exact done7 ha h0eG

theorem done6 {a : Nat → Nat → Bool} (ha : Recurrence a) {s : Nat} (h : AlignedFrom K a V6 s (F w6) 179400) :
    ∃ s', s' ≤ s + 16 ∧ OnTree a s' := by
  have h0 : AlignedFrom K a V6 s (F w6) 179400 := h
  have h0e : AlignedFrom K a V6 s (F w6) 271595 :=
    extend_from ha Rule30SixteenFrontsStrip6.V_return Rule30SixteenFrontsStrip6.words (by omega) (by decide) (by omega) h0 Rule30SixteenFrontsStrip6.b_179400_271595
  rcases step_white ha Rule30SixteenFrontsStrip6.V_return Rule30SixteenFrontsStrip6.words (by decide) h0e Rule30SixteenFrontsStrip6.w_271595 with h0eL | h0eR
  · -- aligned through the doubled wheel 271596, same shift
    exact ⟨s, by omega, inj6 (extend_from ha Rule30SixteenFrontsStrip6.V_return Rule30SixteenFrontsStrip6.words (by omega) (by decide) (by omega) h0eL Rule30SixteenFrontsStrip6.b_271596_894235)⟩
  · -- the complement: a shift by 16
    have h0eS : AlignedFrom K a V6 (s + 16) (F w6) 271596 := white_shift h0e h0eR
      (strip_shift Rule30SixteenFrontsStrip6.V_return Rule30SixteenFrontsStrip6.per_271595 Rule30SixteenFrontsStrip6.anti_271595).1 (strip_shift Rule30SixteenFrontsStrip6.V_return Rule30SixteenFrontsStrip6.per_271595 Rule30SixteenFrontsStrip6.anti_271595).2
    exact ⟨(s + 16), by omega, inj6 (extend_from ha Rule30SixteenFrontsStrip6.V_return Rule30SixteenFrontsStrip6.words (by omega) (by decide) (by omega) h0eS Rule30SixteenFrontsStrip6.b_271596_894235)⟩

theorem done4 {a : Nat → Nat → Bool} (ha : Recurrence a) {s : Nat} (h : AlignedFrom K a V4 s (F w4) 165749) :
    ∃ s', s' ≤ s + 16 ∧ OnTree a s' := by
  have h0 : AlignedFrom K a V4 s (F w4) 165749 := h
  have h0e : AlignedFrom K a V4 s (F w4) 174449 :=
    extend_from ha Rule30SixteenFrontsStrip4.V_return Rule30SixteenFrontsStrip4.words (by omega) (by decide) (by omega) h0 Rule30SixteenFrontsStrip4.b_165749_174449
  rcases step_white ha Rule30SixteenFrontsStrip4.V_return Rule30SixteenFrontsStrip4.words (by decide) h0e Rule30SixteenFrontsStrip4.w_174449 with h0eL | h0eR
  · -- the same side at the fork 174449
    have h0eLe : AlignedFrom K a V4 s (F w4) 179399 :=
      extend_from ha Rule30SixteenFrontsStrip4.V_return Rule30SixteenFrontsStrip4.words (by omega) (by decide) (by omega) h0eL Rule30SixteenFrontsStrip4.b_174450_179399
    rcases step_white ha Rule30SixteenFrontsStrip4.V_return Rule30SixteenFrontsStrip4.words (by decide) h0eLe Rule30SixteenFrontsStrip4.w_179399 with h0eLeL | h0eLeR
    · -- the same side at the fork 179399
      have h0eLeLe : AlignedFrom K a V4 s (F w4) 196188 :=
        extend_from ha Rule30SixteenFrontsStrip4.V_return Rule30SixteenFrontsStrip4.words (by omega) (by decide) (by omega) h0eLeL Rule30SixteenFrontsStrip4.b_179400_196188
      rcases step_white ha Rule30SixteenFrontsStrip4.V_return Rule30SixteenFrontsStrip4.words (by decide) h0eLeLe Rule30SixteenFrontsStrip4.w_196188 with h0eLeLeL | h0eLeLeR
      · -- aligned through the doubled wheel 196189, same shift
        exact ⟨s, by omega, inj4 (extend_from ha Rule30SixteenFrontsStrip4.V_return Rule30SixteenFrontsStrip4.words (by omega) (by decide) (by omega) h0eLeLeL Rule30SixteenFrontsStrip4.b_196189_894235)⟩
      · -- the complement: a shift by 16
        have h0eLeLeS : AlignedFrom K a V4 (s + 16) (F w4) 196189 := white_shift h0eLeLe h0eLeLeR
          (strip_shift Rule30SixteenFrontsStrip4.V_return Rule30SixteenFrontsStrip4.per_196188 Rule30SixteenFrontsStrip4.anti_196188).1 (strip_shift Rule30SixteenFrontsStrip4.V_return Rule30SixteenFrontsStrip4.per_196188 Rule30SixteenFrontsStrip4.anti_196188).2
        exact ⟨(s + 16), by omega, inj4 (extend_from ha Rule30SixteenFrontsStrip4.V_return Rule30SixteenFrontsStrip4.words (by omega) (by decide) (by omega) h0eLeLeS Rule30SixteenFrontsStrip4.b_196189_894235)⟩
    · -- the other side: strip 6
      have h0eLeF : AlignedFrom K a V6 s (F w4) 179400 := white_fork h0eLe h0eLeR
        (fun j t hj => (Rule30SixteenFrontsStrip6.low_V' j t (by omega)))
        Rule30SixteenFrontsStrip6.comp_V
      have h0eLeG : AlignedFrom K a V6 s (F w6) 179400 :=
        alignedFrom_congr (fun j hj => F_congr j (fun i hi => Rule30SixteenFrontsStrip6.w_eq i (by omega))) h0eLeF
      exact done6 ha h0eLeG
  · -- the other side: strip 5
    have h0eF : AlignedFrom K a V5 s (F w4) 174450 := white_fork h0e h0eR
      (fun j t hj => (Rule30SixteenFrontsStrip5.low_V' j t (by omega)))
      Rule30SixteenFrontsStrip5.comp_V
    have h0eG : AlignedFrom K a V5 s (F w5) 174450 :=
      alignedFrom_congr (fun j hj => F_congr j (fun i hi => Rule30SixteenFrontsStrip5.w_eq i (by omega))) h0eF
    exact done5 ha h0eG

theorem done1 {a : Nat → Nat → Bool} (ha : Recurrence a) {s : Nat} (h : AlignedFrom K a V1 s (F w1) 53208) :
    ∃ s', s' ≤ s + 16 ∧ OnTree a s' := by
  have h0 : AlignedFrom K a V1 s (F w1) 53208 := h
  have h0e : AlignedFrom K a V1 s (F w1) 72575 :=
    extend_from ha Rule30SixteenFrontsStrip1.V_return Rule30SixteenFrontsStrip1.words (by omega) (by decide) (by omega) h0 Rule30SixteenFrontsStrip1.b_53208_72575
  rcases step_white ha Rule30SixteenFrontsStrip1.V_return Rule30SixteenFrontsStrip1.words (by decide) h0e Rule30SixteenFrontsStrip1.w_72575 with h0eL | h0eR
  · -- the same side at the fork 72575
    have h0eLe : AlignedFrom K a V1 s (F w1) 165748 :=
      extend_from ha Rule30SixteenFrontsStrip1.V_return Rule30SixteenFrontsStrip1.words (by omega) (by decide) (by omega) h0eL Rule30SixteenFrontsStrip1.b_72576_165748
    rcases step_white ha Rule30SixteenFrontsStrip1.V_return Rule30SixteenFrontsStrip1.words (by decide) h0eLe Rule30SixteenFrontsStrip1.w_165748 with h0eLeL | h0eLeR
    · -- the same side at the fork 165748
      have h0eLeLe : AlignedFrom K a V1 s (F w1) 183183 :=
        extend_from ha Rule30SixteenFrontsStrip1.V_return Rule30SixteenFrontsStrip1.words (by omega) (by decide) (by omega) h0eLeL Rule30SixteenFrontsStrip1.b_165749_183183
      rcases step_white ha Rule30SixteenFrontsStrip1.V_return Rule30SixteenFrontsStrip1.words (by decide) h0eLeLe Rule30SixteenFrontsStrip1.w_183183 with h0eLeLeL | h0eLeLeR
      · -- aligned through the doubled wheel 183184, same shift
        exact ⟨s, by omega, inj1 (extend_from ha Rule30SixteenFrontsStrip1.V_return Rule30SixteenFrontsStrip1.words (by omega) (by decide) (by omega) h0eLeLeL Rule30SixteenFrontsStrip1.b_183184_894235)⟩
      · -- the complement: a shift by 16
        have h0eLeLeS : AlignedFrom K a V1 (s + 16) (F w1) 183184 := white_shift h0eLeLe h0eLeLeR
          (strip_shift Rule30SixteenFrontsStrip1.V_return Rule30SixteenFrontsStrip1.per_183183 Rule30SixteenFrontsStrip1.anti_183183).1 (strip_shift Rule30SixteenFrontsStrip1.V_return Rule30SixteenFrontsStrip1.per_183183 Rule30SixteenFrontsStrip1.anti_183183).2
        exact ⟨(s + 16), by omega, inj1 (extend_from ha Rule30SixteenFrontsStrip1.V_return Rule30SixteenFrontsStrip1.words (by omega) (by decide) (by omega) h0eLeLeS Rule30SixteenFrontsStrip1.b_183184_894235)⟩
    · -- the other side: strip 4
      have h0eLeF : AlignedFrom K a V4 s (F w1) 165749 := white_fork h0eLe h0eLeR
        (fun j t hj => (Rule30SixteenFrontsStrip4.low_V' j t (by omega)))
        Rule30SixteenFrontsStrip4.comp_V
      have h0eLeG : AlignedFrom K a V4 s (F w4) 165749 :=
        alignedFrom_congr (fun j hj => F_congr j (fun i hi => Rule30SixteenFrontsStrip4.w_eq i (by omega))) h0eLeF
      exact done4 ha h0eLeG
  · -- the other side: strip 3
    have h0eF : AlignedFrom K a V3 s (F w1) 72576 := white_fork h0e h0eR
      (fun j t hj => (Rule30SixteenFrontsStrip3.low_V' j t (by omega)))
      Rule30SixteenFrontsStrip3.comp_V
    have h0eG : AlignedFrom K a V3 s (F w3) 72576 :=
      alignedFrom_congr (fun j hj => F_congr j (fun i hi => Rule30SixteenFrontsStrip3.w_eq i (by omega))) h0eF
    exact done3 ha h0eG

theorem done2 {a : Nat → Nat → Bool} (ha : Recurrence a) {s : Nat} (h : AlignedFrom K a V2 s (F w2) 58287) :
    ∃ s', s' ≤ s + 16 ∧ OnTree a s' := by
  have h0 : AlignedFrom K a V2 s (F w2) 58287 := h
  have h0e : AlignedFrom K a V2 s (F w2) 229337 :=
    extend_from ha Rule30SixteenFrontsStrip2.V_return Rule30SixteenFrontsStrip2.words (by omega) (by decide) (by omega) h0 Rule30SixteenFrontsStrip2.b_58287_229337
  rcases step_white ha Rule30SixteenFrontsStrip2.V_return Rule30SixteenFrontsStrip2.words (by decide) h0e Rule30SixteenFrontsStrip2.w_229337 with h0eL | h0eR
  · -- aligned through the doubled wheel 229338, same shift
    exact ⟨s, by omega, inj2 (extend_from ha Rule30SixteenFrontsStrip2.V_return Rule30SixteenFrontsStrip2.words (by omega) (by decide) (by omega) h0eL Rule30SixteenFrontsStrip2.b_229338_894235)⟩
  · -- the complement: a shift by 16
    have h0eS : AlignedFrom K a V2 (s + 16) (F w2) 229338 := white_shift h0e h0eR
      (strip_shift Rule30SixteenFrontsStrip2.V_return Rule30SixteenFrontsStrip2.per_229337 Rule30SixteenFrontsStrip2.anti_229337).1 (strip_shift Rule30SixteenFrontsStrip2.V_return Rule30SixteenFrontsStrip2.per_229337 Rule30SixteenFrontsStrip2.anti_229337).2
    exact ⟨(s + 16), by omega, inj2 (extend_from ha Rule30SixteenFrontsStrip2.V_return Rule30SixteenFrontsStrip2.words (by omega) (by decide) (by omega) h0eS Rule30SixteenFrontsStrip2.b_229338_894235)⟩

theorem done0 {a : Nat → Nat → Bool} (ha : Recurrence a) {s : Nat} (h : AlignedFrom K a V0 s (F w0) 53207) :
    ∃ s', s' ≤ s + 16 ∧ OnTree a s' := by
  have h0 : AlignedFrom K a V0 s (F w0) 53207 := h
  rcases step_white ha Rule30SixteenFrontsStrip0.V_return Rule30SixteenFrontsStrip0.words (by decide) h0 Rule30SixteenFrontsStrip0.w_53207 with h0L | h0R
  · -- the same side at the fork 53207
    have h0Le : AlignedFrom K a V0 s (F w0) 58286 :=
      extend_from ha Rule30SixteenFrontsStrip0.V_return Rule30SixteenFrontsStrip0.words (by omega) (by decide) (by omega) h0L Rule30SixteenFrontsStrip0.b_53208_58286
    rcases step_white ha Rule30SixteenFrontsStrip0.V_return Rule30SixteenFrontsStrip0.words (by decide) h0Le Rule30SixteenFrontsStrip0.w_58286 with h0LeL | h0LeR
    · -- the same side at the fork 58286
      have h0LeLe : AlignedFrom K a V0 s (F w0) 87866 :=
        extend_from ha Rule30SixteenFrontsStrip0.V_return Rule30SixteenFrontsStrip0.words (by omega) (by decide) (by omega) h0LeL Rule30SixteenFrontsStrip0.b_58287_87866
      rcases step_white ha Rule30SixteenFrontsStrip0.V_return Rule30SixteenFrontsStrip0.words (by decide) h0LeLe Rule30SixteenFrontsStrip0.w_87866 with h0LeLeL | h0LeLeR
      · -- aligned through the doubled wheel 87867, same shift
        exact ⟨s, by omega, inj0 (extend_from ha Rule30SixteenFrontsStrip0.V_return Rule30SixteenFrontsStrip0.words (by omega) (by decide) (by omega) h0LeLeL Rule30SixteenFrontsStrip0.b_87867_894235)⟩
      · -- the complement: a shift by 16
        have h0LeLeS : AlignedFrom K a V0 (s + 16) (F w0) 87867 := white_shift h0LeLe h0LeLeR
          (strip_shift Rule30SixteenFrontsStrip0.V_return Rule30SixteenFrontsStrip0.per_87866 Rule30SixteenFrontsStrip0.anti_87866).1 (strip_shift Rule30SixteenFrontsStrip0.V_return Rule30SixteenFrontsStrip0.per_87866 Rule30SixteenFrontsStrip0.anti_87866).2
        exact ⟨(s + 16), by omega, inj0 (extend_from ha Rule30SixteenFrontsStrip0.V_return Rule30SixteenFrontsStrip0.words (by omega) (by decide) (by omega) h0LeLeS Rule30SixteenFrontsStrip0.b_87867_894235)⟩
    · -- the other side: strip 2
      have h0LeF : AlignedFrom K a V2 s (F w0) 58287 := white_fork h0Le h0LeR
        (fun j t hj => (Rule30SixteenFrontsStrip2.low_V' j t (by omega)))
        Rule30SixteenFrontsStrip2.comp_V
      have h0LeG : AlignedFrom K a V2 s (F w2) 58287 :=
        alignedFrom_congr (fun j hj => F_congr j (fun i hi => Rule30SixteenFrontsStrip2.w_eq i (by omega))) h0LeF
      exact done2 ha h0LeG
  · -- the other side: strip 1
    have h0F : AlignedFrom K a V1 s (F w0) 53208 := white_fork h0 h0R
      (fun j t hj => (Rule30SixteenFrontsStrip1.low_V' j t (by omega)))
      Rule30SixteenFrontsStrip1.comp_V
    have h0G : AlignedFrom K a V1 s (F w1) 53208 :=
      alignedFrom_congr (fun j hj => F_congr j (fun i hi => Rule30SixteenFrontsStrip1.w_eq i (by omega))) h0F
    exact done1 ha h0G

/-! ### The headlines -/

/-- **The forced front on the tree.** -/
theorem forced_front_tree {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) : ∃ s, s ≤ 31 ∧ OnTree a s := by
  obtain ⟨s, hs, h⟩ := low_from (by decide) ha ha0 Rule30SixteenFrontsStrip0.V_return Rule30SixteenFrontsStrip0.words Rule30SixteenFrontsStrip0.V_zero Rule30SixteenFrontsStrip0.V_one Rule30SixteenFrontsStrip0.hbw
    (strip_shift Rule30SixteenFrontsStrip0.V_return Rule30SixteenFrontsStrip0.per2 Rule30SixteenFrontsStrip0.anti2) (strip_shift Rule30SixteenFrontsStrip0.V_return Rule30SixteenFrontsStrip0.per7 Rule30SixteenFrontsStrip0.anti7)
    (strip_shift Rule30SixteenFrontsStrip0.V_return Rule30SixteenFrontsStrip0.per28 Rule30SixteenFrontsStrip0.anti28) (strip_shift Rule30SixteenFrontsStrip0.V_return Rule30SixteenFrontsStrip0.per399 Rule30SixteenFrontsStrip0.anti399)
    53207 (Nat.le_refl _)
  obtain ⟨s', hs', h'⟩ := done0 ha h
  exact ⟨s', by rw [lsum_53207] at hs; omega, h'⟩

theorem classification_bounded {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 31 ∧ OnTreeAligned a s :=
  let ⟨s, hs, h⟩ := forced_front_tree ha ha0
  ⟨s, hs, onTreeAligned_of_onTree h⟩

/-- **From strip tick 1798243**, that is from tick at most 1798274 of its own clock. -/
theorem forced_front_tree_uniform {a : Nat → Nat → Bool} (ha : Recurrence a) (ha0 : a 0 0 = true) :
    ∃ s, s ≤ 31 ∧ OnTreeFrom a s 1798243 :=
  let ⟨s, hs, h⟩ := forced_front_tree ha ha0
  ⟨s, hs, onTreeFrom_of_onTree h⟩

/-- **Every configuration with a leftmost black cell.** -/
theorem forced_front_tree_left_side {x : Int → Bool} {lo : Int} (hleft : ∀ p, p < lo → x p = false) (hlo : x lo = true) :
    ∃ s, s ≤ 31 ∧ OnTreeFrom (Ld x lo) s 1798243 :=
  forced_front_tree_uniform (Ld_recurrence hleft) (by simpa [Ld, evol] using hlo)

/-- The single black cell. -/
theorem forced_front_tree_seed : ∃ s, s ≤ 31 ∧ OnTreeFrom D s 1798243 :=
  forced_front_tree_uniform D_recurrence (D_zero 0)

theorem left_side_classification {x : Int → Bool} {lo : Int} (hleft : ∀ p, p < lo → x p = false) (hlo : x lo = true) :
    ∃ s, OnTreeAligned (Ld x lo) s :=
  let ⟨s, _, h⟩ := classification_bounded (Ld_recurrence hleft) (by simpa [Ld, evol] using hlo)
  ⟨s, h⟩

/-! ### Realization, distinctness, the arithmetic form -/

theorem Ld_row (v : Nat) {j : Nat} (hj : j ≤ 894235) (t : Nat) : Ld (ofRow v) 0 j t = Sp K v j t :=
  Ld_ofRow (K := K) (by decide) v t j (by show j < 894236; omega)

theorem realized (v : Nat) : Aligned K (Ld (ofRow v) 0) v 0 894235 :=
  fun _ hj => ⟨0, fun t _ => Ld_row v hj (t + 0)⟩

theorem comp_symm {v v' w : Nat} (h : ∀ t, Sp K v' w t = !Sp K v w t) : ∀ t, Sp K v w t = !Sp K v' w t := fun t => by
  rw [h t]; cases Sp K v w t <;> rfl

theorem distinct :
    ¬ Related K 894235 V0 V1 ∧
    ¬ Related K 894235 V0 V2 ∧
    ¬ Related K 894235 V0 V3 ∧
    ¬ Related K 894235 V0 V4 ∧
    ¬ Related K 894235 V0 V5 ∧
    ¬ Related K 894235 V0 V6 ∧
    ¬ Related K 894235 V0 V7 ∧
    ¬ Related K 894235 V0 V8 ∧
    ¬ Related K 894235 V0 V9 ∧
    ¬ Related K 894235 V0 V10 ∧
    ¬ Related K 894235 V0 V11 ∧
    ¬ Related K 894235 V0 V12 ∧
    ¬ Related K 894235 V0 V13 ∧
    ¬ Related K 894235 V0 V14 ∧
    ¬ Related K 894235 V0 V15 ∧
    ¬ Related K 894235 V1 V2 ∧
    ¬ Related K 894235 V1 V3 ∧
    ¬ Related K 894235 V1 V4 ∧
    ¬ Related K 894235 V1 V5 ∧
    ¬ Related K 894235 V1 V6 ∧
    ¬ Related K 894235 V1 V7 ∧
    ¬ Related K 894235 V1 V8 ∧
    ¬ Related K 894235 V1 V9 ∧
    ¬ Related K 894235 V1 V10 ∧
    ¬ Related K 894235 V1 V11 ∧
    ¬ Related K 894235 V1 V12 ∧
    ¬ Related K 894235 V1 V13 ∧
    ¬ Related K 894235 V1 V14 ∧
    ¬ Related K 894235 V1 V15 ∧
    ¬ Related K 894235 V2 V3 ∧
    ¬ Related K 894235 V2 V4 ∧
    ¬ Related K 894235 V2 V5 ∧
    ¬ Related K 894235 V2 V6 ∧
    ¬ Related K 894235 V2 V7 ∧
    ¬ Related K 894235 V2 V8 ∧
    ¬ Related K 894235 V2 V9 ∧
    ¬ Related K 894235 V2 V10 ∧
    ¬ Related K 894235 V2 V11 ∧
    ¬ Related K 894235 V2 V12 ∧
    ¬ Related K 894235 V2 V13 ∧
    ¬ Related K 894235 V2 V14 ∧
    ¬ Related K 894235 V2 V15 ∧
    ¬ Related K 894235 V3 V4 ∧
    ¬ Related K 894235 V3 V5 ∧
    ¬ Related K 894235 V3 V6 ∧
    ¬ Related K 894235 V3 V7 ∧
    ¬ Related K 894235 V3 V8 ∧
    ¬ Related K 894235 V3 V9 ∧
    ¬ Related K 894235 V3 V10 ∧
    ¬ Related K 894235 V3 V11 ∧
    ¬ Related K 894235 V3 V12 ∧
    ¬ Related K 894235 V3 V13 ∧
    ¬ Related K 894235 V3 V14 ∧
    ¬ Related K 894235 V3 V15 ∧
    ¬ Related K 894235 V4 V5 ∧
    ¬ Related K 894235 V4 V6 ∧
    ¬ Related K 894235 V4 V7 ∧
    ¬ Related K 894235 V4 V8 ∧
    ¬ Related K 894235 V4 V9 ∧
    ¬ Related K 894235 V4 V10 ∧
    ¬ Related K 894235 V4 V11 ∧
    ¬ Related K 894235 V4 V12 ∧
    ¬ Related K 894235 V4 V13 ∧
    ¬ Related K 894235 V4 V14 ∧
    ¬ Related K 894235 V4 V15 ∧
    ¬ Related K 894235 V5 V6 ∧
    ¬ Related K 894235 V5 V7 ∧
    ¬ Related K 894235 V5 V8 ∧
    ¬ Related K 894235 V5 V9 ∧
    ¬ Related K 894235 V5 V10 ∧
    ¬ Related K 894235 V5 V11 ∧
    ¬ Related K 894235 V5 V12 ∧
    ¬ Related K 894235 V5 V13 ∧
    ¬ Related K 894235 V5 V14 ∧
    ¬ Related K 894235 V5 V15 ∧
    ¬ Related K 894235 V6 V7 ∧
    ¬ Related K 894235 V6 V8 ∧
    ¬ Related K 894235 V6 V9 ∧
    ¬ Related K 894235 V6 V10 ∧
    ¬ Related K 894235 V6 V11 ∧
    ¬ Related K 894235 V6 V12 ∧
    ¬ Related K 894235 V6 V13 ∧
    ¬ Related K 894235 V6 V14 ∧
    ¬ Related K 894235 V6 V15 ∧
    ¬ Related K 894235 V7 V8 ∧
    ¬ Related K 894235 V7 V9 ∧
    ¬ Related K 894235 V7 V10 ∧
    ¬ Related K 894235 V7 V11 ∧
    ¬ Related K 894235 V7 V12 ∧
    ¬ Related K 894235 V7 V13 ∧
    ¬ Related K 894235 V7 V14 ∧
    ¬ Related K 894235 V7 V15 ∧
    ¬ Related K 894235 V8 V9 ∧
    ¬ Related K 894235 V8 V10 ∧
    ¬ Related K 894235 V8 V11 ∧
    ¬ Related K 894235 V8 V12 ∧
    ¬ Related K 894235 V8 V13 ∧
    ¬ Related K 894235 V8 V14 ∧
    ¬ Related K 894235 V8 V15 ∧
    ¬ Related K 894235 V9 V10 ∧
    ¬ Related K 894235 V9 V11 ∧
    ¬ Related K 894235 V9 V12 ∧
    ¬ Related K 894235 V9 V13 ∧
    ¬ Related K 894235 V9 V14 ∧
    ¬ Related K 894235 V9 V15 ∧
    ¬ Related K 894235 V10 V11 ∧
    ¬ Related K 894235 V10 V12 ∧
    ¬ Related K 894235 V10 V13 ∧
    ¬ Related K 894235 V10 V14 ∧
    ¬ Related K 894235 V10 V15 ∧
    ¬ Related K 894235 V11 V12 ∧
    ¬ Related K 894235 V11 V13 ∧
    ¬ Related K 894235 V11 V14 ∧
    ¬ Related K 894235 V11 V15 ∧
    ¬ Related K 894235 V12 V13 ∧
    ¬ Related K 894235 V12 V14 ∧
    ¬ Related K 894235 V12 V15 ∧
    ¬ Related K 894235 V13 V14 ∧
    ¬ Related K 894235 V13 V15 ∧
    ¬ Related K 894235 V14 V15 :=
  ⟨not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip0.per16 _ (by omega)) (Rule30SixteenFrontsStrip0.per16 _ (by omega))
      (Rule30SixteenFrontsStrip1.per16 _ (by omega)) (comp_symm (fun t => Rule30SixteenFrontsStrip1.comp_V t))
      (fun t => by rw [Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip0.prim,
   not_related (w := 58287) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip0.per16 _ (by omega)) (Rule30SixteenFrontsStrip0.per16 _ (by omega))
      (Rule30SixteenFrontsStrip2.per16 _ (by omega)) (comp_symm (fun t => Rule30SixteenFrontsStrip2.comp_V t))
      (fun t => by rw [Rule30SixteenFrontsStrip2.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip0.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip0.per16 _ (by omega)) (Rule30SixteenFrontsStrip0.per16 _ (by omega))
      (Rule30SixteenFrontsStrip3.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip3.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip3.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip0.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip0.per16 _ (by omega)) (Rule30SixteenFrontsStrip0.per16 _ (by omega))
      (Rule30SixteenFrontsStrip4.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip0.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip0.per16 _ (by omega)) (Rule30SixteenFrontsStrip0.per16 _ (by omega))
      (Rule30SixteenFrontsStrip5.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip0.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip0.per16 _ (by omega)) (Rule30SixteenFrontsStrip0.per16 _ (by omega))
      (Rule30SixteenFrontsStrip6.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip6.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip6.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip0.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip0.per16 _ (by omega)) (Rule30SixteenFrontsStrip0.per16 _ (by omega))
      (Rule30SixteenFrontsStrip7.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip7.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip7.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip0.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip0.per16 _ (by omega)) (Rule30SixteenFrontsStrip0.per16 _ (by omega))
      (Rule30SixteenFrontsStrip8.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip8.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip8.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip0.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip0.per16 _ (by omega)) (Rule30SixteenFrontsStrip0.per16 _ (by omega))
      (Rule30SixteenFrontsStrip9.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip9.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip0.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip0.per16 _ (by omega)) (Rule30SixteenFrontsStrip0.per16 _ (by omega))
      (Rule30SixteenFrontsStrip10.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip10.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip10.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip0.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip0.per16 _ (by omega)) (Rule30SixteenFrontsStrip0.per16 _ (by omega))
      (Rule30SixteenFrontsStrip11.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip11.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip11.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip0.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip0.per16 _ (by omega)) (Rule30SixteenFrontsStrip0.per16 _ (by omega))
      (Rule30SixteenFrontsStrip12.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip12.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip12.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip0.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip0.per16 _ (by omega)) (Rule30SixteenFrontsStrip0.per16 _ (by omega))
      (Rule30SixteenFrontsStrip13.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip13.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip9.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip13.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip0.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip0.per16 _ (by omega)) (Rule30SixteenFrontsStrip0.per16 _ (by omega))
      (Rule30SixteenFrontsStrip14.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip14.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip9.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip14.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip0.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip0.per16 _ (by omega)) (Rule30SixteenFrontsStrip0.per16 _ (by omega))
      (Rule30SixteenFrontsStrip15.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip15.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip12.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip15.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip0.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip1.per16 _ (by omega)) (Rule30SixteenFrontsStrip1.per16 _ (by omega))
      (Rule30SixteenFrontsStrip2.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip1.comp_V t, Rule30SixteenFrontsStrip2.low_V' 53208 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip1.low_V' 400 t (by omega), Rule30SixteenFrontsStrip2.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip1.prim,
   not_related (w := 72576) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip1.per16 _ (by omega)) (Rule30SixteenFrontsStrip1.per16 _ (by omega))
      (Rule30SixteenFrontsStrip3.per16 _ (by omega)) (comp_symm (fun t => Rule30SixteenFrontsStrip3.comp_V t))
      (fun t => by rw [Rule30SixteenFrontsStrip3.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip1.prim,
   not_related (w := 165749) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip1.per16 _ (by omega)) (Rule30SixteenFrontsStrip1.per16 _ (by omega))
      (Rule30SixteenFrontsStrip4.per16 _ (by omega)) (comp_symm (fun t => Rule30SixteenFrontsStrip4.comp_V t))
      (fun t => by rw [Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip1.prim,
   not_related (w := 165749) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip1.per16 _ (by omega)) (Rule30SixteenFrontsStrip1.per16 _ (by omega))
      (Rule30SixteenFrontsStrip5.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip5.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip4.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip1.prim,
   not_related (w := 165749) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip1.per16 _ (by omega)) (Rule30SixteenFrontsStrip1.per16 _ (by omega))
      (Rule30SixteenFrontsStrip6.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip6.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip4.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip6.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip1.prim,
   not_related (w := 165749) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip1.per16 _ (by omega)) (Rule30SixteenFrontsStrip1.per16 _ (by omega))
      (Rule30SixteenFrontsStrip7.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip7.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip5.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip4.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip7.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip1.prim,
   not_related (w := 165749) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip1.per16 _ (by omega)) (Rule30SixteenFrontsStrip1.per16 _ (by omega))
      (Rule30SixteenFrontsStrip8.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip8.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip5.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip4.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip8.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip1.prim,
   not_related (w := 165749) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip1.per16 _ (by omega)) (Rule30SixteenFrontsStrip1.per16 _ (by omega))
      (Rule30SixteenFrontsStrip9.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip9.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip5.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip4.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip1.prim,
   not_related (w := 165749) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip1.per16 _ (by omega)) (Rule30SixteenFrontsStrip1.per16 _ (by omega))
      (Rule30SixteenFrontsStrip10.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip10.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip5.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip4.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip10.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip1.prim,
   not_related (w := 165749) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip1.per16 _ (by omega)) (Rule30SixteenFrontsStrip1.per16 _ (by omega))
      (Rule30SixteenFrontsStrip11.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip11.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip5.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip4.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip11.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip1.prim,
   not_related (w := 165749) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip1.per16 _ (by omega)) (Rule30SixteenFrontsStrip1.per16 _ (by omega))
      (Rule30SixteenFrontsStrip12.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip12.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip5.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip4.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip12.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip1.prim,
   not_related (w := 165749) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip1.per16 _ (by omega)) (Rule30SixteenFrontsStrip1.per16 _ (by omega))
      (Rule30SixteenFrontsStrip13.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip13.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip9.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip5.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip4.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip13.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip1.prim,
   not_related (w := 165749) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip1.per16 _ (by omega)) (Rule30SixteenFrontsStrip1.per16 _ (by omega))
      (Rule30SixteenFrontsStrip14.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip14.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip9.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip5.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip4.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip14.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip1.prim,
   not_related (w := 165749) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip1.per16 _ (by omega)) (Rule30SixteenFrontsStrip1.per16 _ (by omega))
      (Rule30SixteenFrontsStrip15.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip15.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip12.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip5.low_V' 165749 t (by omega), Rule30SixteenFrontsStrip4.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip15.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip1.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip2.per16 _ (by omega)) (Rule30SixteenFrontsStrip2.per16 _ (by omega))
      (Rule30SixteenFrontsStrip3.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip3.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t, Rule30SixteenFrontsStrip2.low_V' 53208 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip2.low_V' 400 t (by omega), Rule30SixteenFrontsStrip3.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip2.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip2.per16 _ (by omega)) (Rule30SixteenFrontsStrip2.per16 _ (by omega))
      (Rule30SixteenFrontsStrip4.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t, Rule30SixteenFrontsStrip2.low_V' 53208 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip2.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip2.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip2.per16 _ (by omega)) (Rule30SixteenFrontsStrip2.per16 _ (by omega))
      (Rule30SixteenFrontsStrip5.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t, Rule30SixteenFrontsStrip2.low_V' 53208 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip2.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip2.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip2.per16 _ (by omega)) (Rule30SixteenFrontsStrip2.per16 _ (by omega))
      (Rule30SixteenFrontsStrip6.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip6.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t, Rule30SixteenFrontsStrip2.low_V' 53208 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip2.low_V' 400 t (by omega), Rule30SixteenFrontsStrip6.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip2.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip2.per16 _ (by omega)) (Rule30SixteenFrontsStrip2.per16 _ (by omega))
      (Rule30SixteenFrontsStrip7.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip7.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t, Rule30SixteenFrontsStrip2.low_V' 53208 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip2.low_V' 400 t (by omega), Rule30SixteenFrontsStrip7.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip2.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip2.per16 _ (by omega)) (Rule30SixteenFrontsStrip2.per16 _ (by omega))
      (Rule30SixteenFrontsStrip8.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip8.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t, Rule30SixteenFrontsStrip2.low_V' 53208 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip2.low_V' 400 t (by omega), Rule30SixteenFrontsStrip8.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip2.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip2.per16 _ (by omega)) (Rule30SixteenFrontsStrip2.per16 _ (by omega))
      (Rule30SixteenFrontsStrip9.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip9.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t, Rule30SixteenFrontsStrip2.low_V' 53208 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip2.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip2.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip2.per16 _ (by omega)) (Rule30SixteenFrontsStrip2.per16 _ (by omega))
      (Rule30SixteenFrontsStrip10.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip10.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t, Rule30SixteenFrontsStrip2.low_V' 53208 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip2.low_V' 400 t (by omega), Rule30SixteenFrontsStrip10.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip2.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip2.per16 _ (by omega)) (Rule30SixteenFrontsStrip2.per16 _ (by omega))
      (Rule30SixteenFrontsStrip11.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip11.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t, Rule30SixteenFrontsStrip2.low_V' 53208 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip2.low_V' 400 t (by omega), Rule30SixteenFrontsStrip11.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip2.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip2.per16 _ (by omega)) (Rule30SixteenFrontsStrip2.per16 _ (by omega))
      (Rule30SixteenFrontsStrip12.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip12.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t, Rule30SixteenFrontsStrip2.low_V' 53208 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip2.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip2.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip2.per16 _ (by omega)) (Rule30SixteenFrontsStrip2.per16 _ (by omega))
      (Rule30SixteenFrontsStrip13.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip13.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip9.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t, Rule30SixteenFrontsStrip2.low_V' 53208 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip2.low_V' 400 t (by omega), Rule30SixteenFrontsStrip13.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip2.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip2.per16 _ (by omega)) (Rule30SixteenFrontsStrip2.per16 _ (by omega))
      (Rule30SixteenFrontsStrip14.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip14.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip9.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t, Rule30SixteenFrontsStrip2.low_V' 53208 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip2.low_V' 400 t (by omega), Rule30SixteenFrontsStrip14.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip2.prim,
   not_related (w := 53208) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip2.per16 _ (by omega)) (Rule30SixteenFrontsStrip2.per16 _ (by omega))
      (Rule30SixteenFrontsStrip15.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip15.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip12.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip5.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip4.low_V' 53208 t (by omega), Rule30SixteenFrontsStrip1.comp_V t, Rule30SixteenFrontsStrip2.low_V' 53208 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip2.low_V' 400 t (by omega), Rule30SixteenFrontsStrip15.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega), Rule30SixteenFrontsStrip1.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip2.prim,
   not_related (w := 72576) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip3.per16 _ (by omega)) (Rule30SixteenFrontsStrip3.per16 _ (by omega))
      (Rule30SixteenFrontsStrip4.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip3.comp_V t, Rule30SixteenFrontsStrip4.low_V' 72576 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip3.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip3.prim,
   not_related (w := 72576) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip3.per16 _ (by omega)) (Rule30SixteenFrontsStrip3.per16 _ (by omega))
      (Rule30SixteenFrontsStrip5.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip3.comp_V t, Rule30SixteenFrontsStrip5.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip4.low_V' 72576 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip3.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip3.prim,
   not_related (w := 72576) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip3.per16 _ (by omega)) (Rule30SixteenFrontsStrip3.per16 _ (by omega))
      (Rule30SixteenFrontsStrip6.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip3.comp_V t, Rule30SixteenFrontsStrip6.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip4.low_V' 72576 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip3.low_V' 400 t (by omega), Rule30SixteenFrontsStrip6.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip3.prim,
   not_related (w := 72576) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip3.per16 _ (by omega)) (Rule30SixteenFrontsStrip3.per16 _ (by omega))
      (Rule30SixteenFrontsStrip7.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip3.comp_V t, Rule30SixteenFrontsStrip7.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip5.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip4.low_V' 72576 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip3.low_V' 400 t (by omega), Rule30SixteenFrontsStrip7.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip3.prim,
   not_related (w := 72576) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip3.per16 _ (by omega)) (Rule30SixteenFrontsStrip3.per16 _ (by omega))
      (Rule30SixteenFrontsStrip8.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip3.comp_V t, Rule30SixteenFrontsStrip8.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip5.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip4.low_V' 72576 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip3.low_V' 400 t (by omega), Rule30SixteenFrontsStrip8.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip3.prim,
   not_related (w := 72576) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip3.per16 _ (by omega)) (Rule30SixteenFrontsStrip3.per16 _ (by omega))
      (Rule30SixteenFrontsStrip9.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip3.comp_V t, Rule30SixteenFrontsStrip9.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip5.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip4.low_V' 72576 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip3.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip3.prim,
   not_related (w := 72576) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip3.per16 _ (by omega)) (Rule30SixteenFrontsStrip3.per16 _ (by omega))
      (Rule30SixteenFrontsStrip10.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip3.comp_V t, Rule30SixteenFrontsStrip10.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip5.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip4.low_V' 72576 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip3.low_V' 400 t (by omega), Rule30SixteenFrontsStrip10.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip3.prim,
   not_related (w := 72576) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip3.per16 _ (by omega)) (Rule30SixteenFrontsStrip3.per16 _ (by omega))
      (Rule30SixteenFrontsStrip11.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip3.comp_V t, Rule30SixteenFrontsStrip11.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip5.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip4.low_V' 72576 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip3.low_V' 400 t (by omega), Rule30SixteenFrontsStrip11.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip3.prim,
   not_related (w := 72576) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip3.per16 _ (by omega)) (Rule30SixteenFrontsStrip3.per16 _ (by omega))
      (Rule30SixteenFrontsStrip12.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip3.comp_V t, Rule30SixteenFrontsStrip12.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip5.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip4.low_V' 72576 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip3.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip3.prim,
   not_related (w := 72576) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip3.per16 _ (by omega)) (Rule30SixteenFrontsStrip3.per16 _ (by omega))
      (Rule30SixteenFrontsStrip13.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip3.comp_V t, Rule30SixteenFrontsStrip13.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip9.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip5.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip4.low_V' 72576 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip3.low_V' 400 t (by omega), Rule30SixteenFrontsStrip13.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip3.prim,
   not_related (w := 72576) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip3.per16 _ (by omega)) (Rule30SixteenFrontsStrip3.per16 _ (by omega))
      (Rule30SixteenFrontsStrip14.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip3.comp_V t, Rule30SixteenFrontsStrip14.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip9.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip5.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip4.low_V' 72576 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip3.low_V' 400 t (by omega), Rule30SixteenFrontsStrip14.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip3.prim,
   not_related (w := 72576) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip3.per16 _ (by omega)) (Rule30SixteenFrontsStrip3.per16 _ (by omega))
      (Rule30SixteenFrontsStrip15.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip3.comp_V t, Rule30SixteenFrontsStrip15.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip12.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip5.low_V' 72576 t (by omega), Rule30SixteenFrontsStrip4.low_V' 72576 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip3.low_V' 400 t (by omega), Rule30SixteenFrontsStrip15.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip4.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip3.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip4.per16 _ (by omega)) (Rule30SixteenFrontsStrip4.per16 _ (by omega))
      (Rule30SixteenFrontsStrip5.per16 _ (by omega)) (comp_symm (fun t => Rule30SixteenFrontsStrip5.comp_V t))
      (fun t => by rw [Rule30SixteenFrontsStrip5.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip4.prim,
   not_related (w := 179400) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip4.per16 _ (by omega)) (Rule30SixteenFrontsStrip4.per16 _ (by omega))
      (Rule30SixteenFrontsStrip6.per16 _ (by omega)) (comp_symm (fun t => Rule30SixteenFrontsStrip6.comp_V t))
      (fun t => by rw [Rule30SixteenFrontsStrip6.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip4.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip4.per16 _ (by omega)) (Rule30SixteenFrontsStrip4.per16 _ (by omega))
      (Rule30SixteenFrontsStrip7.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip7.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip5.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip7.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip4.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip4.per16 _ (by omega)) (Rule30SixteenFrontsStrip4.per16 _ (by omega))
      (Rule30SixteenFrontsStrip8.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip8.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip5.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip8.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip4.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip4.per16 _ (by omega)) (Rule30SixteenFrontsStrip4.per16 _ (by omega))
      (Rule30SixteenFrontsStrip9.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip9.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip5.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip4.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip4.per16 _ (by omega)) (Rule30SixteenFrontsStrip4.per16 _ (by omega))
      (Rule30SixteenFrontsStrip10.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip10.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip5.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip10.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip4.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip4.per16 _ (by omega)) (Rule30SixteenFrontsStrip4.per16 _ (by omega))
      (Rule30SixteenFrontsStrip11.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip11.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip5.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip11.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip4.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip4.per16 _ (by omega)) (Rule30SixteenFrontsStrip4.per16 _ (by omega))
      (Rule30SixteenFrontsStrip12.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip12.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip5.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip12.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip4.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip4.per16 _ (by omega)) (Rule30SixteenFrontsStrip4.per16 _ (by omega))
      (Rule30SixteenFrontsStrip13.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip13.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip9.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip5.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip13.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip4.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip4.per16 _ (by omega)) (Rule30SixteenFrontsStrip4.per16 _ (by omega))
      (Rule30SixteenFrontsStrip14.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip14.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip9.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip5.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip14.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip4.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip4.per16 _ (by omega)) (Rule30SixteenFrontsStrip4.per16 _ (by omega))
      (Rule30SixteenFrontsStrip15.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip15.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip12.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip5.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip15.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip4.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip5.per16 _ (by omega)) (Rule30SixteenFrontsStrip5.per16 _ (by omega))
      (Rule30SixteenFrontsStrip6.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip5.comp_V t, Rule30SixteenFrontsStrip6.low_V' 174450 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip5.low_V' 400 t (by omega), Rule30SixteenFrontsStrip6.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip5.prim,
   not_related (w := 243768) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip5.per16 _ (by omega)) (Rule30SixteenFrontsStrip5.per16 _ (by omega))
      (Rule30SixteenFrontsStrip7.per16 _ (by omega)) (comp_symm (fun t => Rule30SixteenFrontsStrip7.comp_V t))
      (fun t => by rw [Rule30SixteenFrontsStrip7.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip5.prim,
   not_related (w := 350244) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip5.per16 _ (by omega)) (Rule30SixteenFrontsStrip5.per16 _ (by omega))
      (Rule30SixteenFrontsStrip8.per16 _ (by omega)) (comp_symm (fun t => Rule30SixteenFrontsStrip8.comp_V t))
      (fun t => by rw [Rule30SixteenFrontsStrip8.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip5.prim,
   not_related (w := 445475) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip5.per16 _ (by omega)) (Rule30SixteenFrontsStrip5.per16 _ (by omega))
      (Rule30SixteenFrontsStrip9.per16 _ (by omega)) (comp_symm (fun t => Rule30SixteenFrontsStrip9.comp_V t))
      (fun t => by rw [Rule30SixteenFrontsStrip9.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip5.prim,
   not_related (w := 485620) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip5.per16 _ (by omega)) (Rule30SixteenFrontsStrip5.per16 _ (by omega))
      (Rule30SixteenFrontsStrip10.per16 _ (by omega)) (comp_symm (fun t => Rule30SixteenFrontsStrip10.comp_V t))
      (fun t => by rw [Rule30SixteenFrontsStrip10.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip5.prim,
   not_related (w := 537693) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip5.per16 _ (by omega)) (Rule30SixteenFrontsStrip5.per16 _ (by omega))
      (Rule30SixteenFrontsStrip11.per16 _ (by omega)) (comp_symm (fun t => Rule30SixteenFrontsStrip11.comp_V t))
      (fun t => by rw [Rule30SixteenFrontsStrip11.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip5.prim,
   not_related (w := 563843) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip5.per16 _ (by omega)) (Rule30SixteenFrontsStrip5.per16 _ (by omega))
      (Rule30SixteenFrontsStrip12.per16 _ (by omega)) (comp_symm (fun t => Rule30SixteenFrontsStrip12.comp_V t))
      (fun t => by rw [Rule30SixteenFrontsStrip12.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip5.prim,
   not_related (w := 445475) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip5.per16 _ (by omega)) (Rule30SixteenFrontsStrip5.per16 _ (by omega))
      (Rule30SixteenFrontsStrip13.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip13.low_V' 445475 t (by omega), Rule30SixteenFrontsStrip9.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip13.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip5.prim,
   not_related (w := 445475) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip5.per16 _ (by omega)) (Rule30SixteenFrontsStrip5.per16 _ (by omega))
      (Rule30SixteenFrontsStrip14.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip14.low_V' 445475 t (by omega), Rule30SixteenFrontsStrip9.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip14.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip5.prim,
   not_related (w := 563843) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip5.per16 _ (by omega)) (Rule30SixteenFrontsStrip5.per16 _ (by omega))
      (Rule30SixteenFrontsStrip15.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip15.low_V' 563843 t (by omega), Rule30SixteenFrontsStrip12.comp_V t]))
      (fun t => by rw [Rule30SixteenFrontsStrip15.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip5.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip6.per16 _ (by omega)) (Rule30SixteenFrontsStrip6.per16 _ (by omega))
      (Rule30SixteenFrontsStrip7.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip7.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip5.comp_V t, Rule30SixteenFrontsStrip6.low_V' 174450 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip6.low_V' 400 t (by omega), Rule30SixteenFrontsStrip7.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip6.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip6.per16 _ (by omega)) (Rule30SixteenFrontsStrip6.per16 _ (by omega))
      (Rule30SixteenFrontsStrip8.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip8.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip5.comp_V t, Rule30SixteenFrontsStrip6.low_V' 174450 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip6.low_V' 400 t (by omega), Rule30SixteenFrontsStrip8.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip6.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip6.per16 _ (by omega)) (Rule30SixteenFrontsStrip6.per16 _ (by omega))
      (Rule30SixteenFrontsStrip9.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip9.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip5.comp_V t, Rule30SixteenFrontsStrip6.low_V' 174450 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip6.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip6.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip6.per16 _ (by omega)) (Rule30SixteenFrontsStrip6.per16 _ (by omega))
      (Rule30SixteenFrontsStrip10.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip10.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip5.comp_V t, Rule30SixteenFrontsStrip6.low_V' 174450 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip6.low_V' 400 t (by omega), Rule30SixteenFrontsStrip10.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip6.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip6.per16 _ (by omega)) (Rule30SixteenFrontsStrip6.per16 _ (by omega))
      (Rule30SixteenFrontsStrip11.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip11.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip5.comp_V t, Rule30SixteenFrontsStrip6.low_V' 174450 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip6.low_V' 400 t (by omega), Rule30SixteenFrontsStrip11.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip6.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip6.per16 _ (by omega)) (Rule30SixteenFrontsStrip6.per16 _ (by omega))
      (Rule30SixteenFrontsStrip12.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip12.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip5.comp_V t, Rule30SixteenFrontsStrip6.low_V' 174450 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip6.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip6.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip6.per16 _ (by omega)) (Rule30SixteenFrontsStrip6.per16 _ (by omega))
      (Rule30SixteenFrontsStrip13.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip13.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip9.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip5.comp_V t, Rule30SixteenFrontsStrip6.low_V' 174450 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip6.low_V' 400 t (by omega), Rule30SixteenFrontsStrip13.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip6.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip6.per16 _ (by omega)) (Rule30SixteenFrontsStrip6.per16 _ (by omega))
      (Rule30SixteenFrontsStrip14.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip14.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip9.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip5.comp_V t, Rule30SixteenFrontsStrip6.low_V' 174450 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip6.low_V' 400 t (by omega), Rule30SixteenFrontsStrip14.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip6.prim,
   not_related (w := 174450) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip6.per16 _ (by omega)) (Rule30SixteenFrontsStrip6.per16 _ (by omega))
      (Rule30SixteenFrontsStrip15.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip15.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip12.low_V' 174450 t (by omega), Rule30SixteenFrontsStrip5.comp_V t, Rule30SixteenFrontsStrip6.low_V' 174450 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip6.low_V' 400 t (by omega), Rule30SixteenFrontsStrip15.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega), Rule30SixteenFrontsStrip5.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip6.prim,
   not_related (w := 243768) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip7.per16 _ (by omega)) (Rule30SixteenFrontsStrip7.per16 _ (by omega))
      (Rule30SixteenFrontsStrip8.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip7.comp_V t, Rule30SixteenFrontsStrip8.low_V' 243768 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip7.low_V' 400 t (by omega), Rule30SixteenFrontsStrip8.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip7.prim,
   not_related (w := 243768) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip7.per16 _ (by omega)) (Rule30SixteenFrontsStrip7.per16 _ (by omega))
      (Rule30SixteenFrontsStrip9.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip7.comp_V t, Rule30SixteenFrontsStrip9.low_V' 243768 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip7.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip7.prim,
   not_related (w := 243768) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip7.per16 _ (by omega)) (Rule30SixteenFrontsStrip7.per16 _ (by omega))
      (Rule30SixteenFrontsStrip10.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip7.comp_V t, Rule30SixteenFrontsStrip10.low_V' 243768 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip7.low_V' 400 t (by omega), Rule30SixteenFrontsStrip10.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip7.prim,
   not_related (w := 243768) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip7.per16 _ (by omega)) (Rule30SixteenFrontsStrip7.per16 _ (by omega))
      (Rule30SixteenFrontsStrip11.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip7.comp_V t, Rule30SixteenFrontsStrip11.low_V' 243768 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip7.low_V' 400 t (by omega), Rule30SixteenFrontsStrip11.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip7.prim,
   not_related (w := 243768) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip7.per16 _ (by omega)) (Rule30SixteenFrontsStrip7.per16 _ (by omega))
      (Rule30SixteenFrontsStrip12.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip7.comp_V t, Rule30SixteenFrontsStrip12.low_V' 243768 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip7.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip7.prim,
   not_related (w := 243768) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip7.per16 _ (by omega)) (Rule30SixteenFrontsStrip7.per16 _ (by omega))
      (Rule30SixteenFrontsStrip13.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip7.comp_V t, Rule30SixteenFrontsStrip13.low_V' 243768 t (by omega), Rule30SixteenFrontsStrip9.low_V' 243768 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip7.low_V' 400 t (by omega), Rule30SixteenFrontsStrip13.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip7.prim,
   not_related (w := 243768) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip7.per16 _ (by omega)) (Rule30SixteenFrontsStrip7.per16 _ (by omega))
      (Rule30SixteenFrontsStrip14.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip7.comp_V t, Rule30SixteenFrontsStrip14.low_V' 243768 t (by omega), Rule30SixteenFrontsStrip9.low_V' 243768 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip7.low_V' 400 t (by omega), Rule30SixteenFrontsStrip14.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip7.prim,
   not_related (w := 243768) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip7.per16 _ (by omega)) (Rule30SixteenFrontsStrip7.per16 _ (by omega))
      (Rule30SixteenFrontsStrip15.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip7.comp_V t, Rule30SixteenFrontsStrip15.low_V' 243768 t (by omega), Rule30SixteenFrontsStrip12.low_V' 243768 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip7.low_V' 400 t (by omega), Rule30SixteenFrontsStrip15.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip7.prim,
   not_related (w := 350244) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip8.per16 _ (by omega)) (Rule30SixteenFrontsStrip8.per16 _ (by omega))
      (Rule30SixteenFrontsStrip9.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip8.comp_V t, Rule30SixteenFrontsStrip9.low_V' 350244 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip8.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip8.prim,
   not_related (w := 350244) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip8.per16 _ (by omega)) (Rule30SixteenFrontsStrip8.per16 _ (by omega))
      (Rule30SixteenFrontsStrip10.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip8.comp_V t, Rule30SixteenFrontsStrip10.low_V' 350244 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip8.low_V' 400 t (by omega), Rule30SixteenFrontsStrip10.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip8.prim,
   not_related (w := 350244) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip8.per16 _ (by omega)) (Rule30SixteenFrontsStrip8.per16 _ (by omega))
      (Rule30SixteenFrontsStrip11.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip8.comp_V t, Rule30SixteenFrontsStrip11.low_V' 350244 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip8.low_V' 400 t (by omega), Rule30SixteenFrontsStrip11.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip8.prim,
   not_related (w := 350244) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip8.per16 _ (by omega)) (Rule30SixteenFrontsStrip8.per16 _ (by omega))
      (Rule30SixteenFrontsStrip12.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip8.comp_V t, Rule30SixteenFrontsStrip12.low_V' 350244 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip8.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip8.prim,
   not_related (w := 350244) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip8.per16 _ (by omega)) (Rule30SixteenFrontsStrip8.per16 _ (by omega))
      (Rule30SixteenFrontsStrip13.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip8.comp_V t, Rule30SixteenFrontsStrip13.low_V' 350244 t (by omega), Rule30SixteenFrontsStrip9.low_V' 350244 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip8.low_V' 400 t (by omega), Rule30SixteenFrontsStrip13.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip8.prim,
   not_related (w := 350244) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip8.per16 _ (by omega)) (Rule30SixteenFrontsStrip8.per16 _ (by omega))
      (Rule30SixteenFrontsStrip14.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip8.comp_V t, Rule30SixteenFrontsStrip14.low_V' 350244 t (by omega), Rule30SixteenFrontsStrip9.low_V' 350244 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip8.low_V' 400 t (by omega), Rule30SixteenFrontsStrip14.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip8.prim,
   not_related (w := 350244) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip8.per16 _ (by omega)) (Rule30SixteenFrontsStrip8.per16 _ (by omega))
      (Rule30SixteenFrontsStrip15.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip8.comp_V t, Rule30SixteenFrontsStrip15.low_V' 350244 t (by omega), Rule30SixteenFrontsStrip12.low_V' 350244 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip8.low_V' 400 t (by omega), Rule30SixteenFrontsStrip15.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip8.prim,
   not_related (w := 445475) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip9.per16 _ (by omega)) (Rule30SixteenFrontsStrip9.per16 _ (by omega))
      (Rule30SixteenFrontsStrip10.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip9.comp_V t, Rule30SixteenFrontsStrip10.low_V' 445475 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip10.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip9.prim,
   not_related (w := 445475) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip9.per16 _ (by omega)) (Rule30SixteenFrontsStrip9.per16 _ (by omega))
      (Rule30SixteenFrontsStrip11.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip9.comp_V t, Rule30SixteenFrontsStrip11.low_V' 445475 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip11.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip9.prim,
   not_related (w := 445475) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip9.per16 _ (by omega)) (Rule30SixteenFrontsStrip9.per16 _ (by omega))
      (Rule30SixteenFrontsStrip12.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip9.comp_V t, Rule30SixteenFrontsStrip12.low_V' 445475 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip9.prim,
   not_related (w := 482609) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip9.per16 _ (by omega)) (Rule30SixteenFrontsStrip9.per16 _ (by omega))
      (Rule30SixteenFrontsStrip13.per16 _ (by omega)) (comp_symm (fun t => Rule30SixteenFrontsStrip13.comp_V t))
      (fun t => by rw [Rule30SixteenFrontsStrip13.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip9.prim,
   not_related (w := 603583) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip9.per16 _ (by omega)) (Rule30SixteenFrontsStrip9.per16 _ (by omega))
      (Rule30SixteenFrontsStrip14.per16 _ (by omega)) (comp_symm (fun t => Rule30SixteenFrontsStrip14.comp_V t))
      (fun t => by rw [Rule30SixteenFrontsStrip14.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip9.prim,
   not_related (w := 445475) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip9.per16 _ (by omega)) (Rule30SixteenFrontsStrip9.per16 _ (by omega))
      (Rule30SixteenFrontsStrip15.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip9.comp_V t, Rule30SixteenFrontsStrip15.low_V' 445475 t (by omega), Rule30SixteenFrontsStrip12.low_V' 445475 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip15.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip9.prim,
   not_related (w := 485620) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip10.per16 _ (by omega)) (Rule30SixteenFrontsStrip10.per16 _ (by omega))
      (Rule30SixteenFrontsStrip11.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip10.comp_V t, Rule30SixteenFrontsStrip11.low_V' 485620 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip10.low_V' 400 t (by omega), Rule30SixteenFrontsStrip11.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip10.prim,
   not_related (w := 485620) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip10.per16 _ (by omega)) (Rule30SixteenFrontsStrip10.per16 _ (by omega))
      (Rule30SixteenFrontsStrip12.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip10.comp_V t, Rule30SixteenFrontsStrip12.low_V' 485620 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip10.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip10.prim,
   not_related (w := 445475) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip10.per16 _ (by omega)) (Rule30SixteenFrontsStrip10.per16 _ (by omega))
      (Rule30SixteenFrontsStrip13.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip13.low_V' 445475 t (by omega), Rule30SixteenFrontsStrip9.comp_V t, Rule30SixteenFrontsStrip10.low_V' 445475 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip10.low_V' 400 t (by omega), Rule30SixteenFrontsStrip13.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip10.prim,
   not_related (w := 445475) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip10.per16 _ (by omega)) (Rule30SixteenFrontsStrip10.per16 _ (by omega))
      (Rule30SixteenFrontsStrip14.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip14.low_V' 445475 t (by omega), Rule30SixteenFrontsStrip9.comp_V t, Rule30SixteenFrontsStrip10.low_V' 445475 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip10.low_V' 400 t (by omega), Rule30SixteenFrontsStrip14.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip10.prim,
   not_related (w := 485620) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip10.per16 _ (by omega)) (Rule30SixteenFrontsStrip10.per16 _ (by omega))
      (Rule30SixteenFrontsStrip15.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip10.comp_V t, Rule30SixteenFrontsStrip15.low_V' 485620 t (by omega), Rule30SixteenFrontsStrip12.low_V' 485620 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip10.low_V' 400 t (by omega), Rule30SixteenFrontsStrip15.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip10.prim,
   not_related (w := 537693) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip11.per16 _ (by omega)) (Rule30SixteenFrontsStrip11.per16 _ (by omega))
      (Rule30SixteenFrontsStrip12.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip11.comp_V t, Rule30SixteenFrontsStrip12.low_V' 537693 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip11.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip11.prim,
   not_related (w := 445475) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip11.per16 _ (by omega)) (Rule30SixteenFrontsStrip11.per16 _ (by omega))
      (Rule30SixteenFrontsStrip13.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip13.low_V' 445475 t (by omega), Rule30SixteenFrontsStrip9.comp_V t, Rule30SixteenFrontsStrip11.low_V' 445475 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip11.low_V' 400 t (by omega), Rule30SixteenFrontsStrip13.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip11.prim,
   not_related (w := 445475) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip11.per16 _ (by omega)) (Rule30SixteenFrontsStrip11.per16 _ (by omega))
      (Rule30SixteenFrontsStrip14.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip14.low_V' 445475 t (by omega), Rule30SixteenFrontsStrip9.comp_V t, Rule30SixteenFrontsStrip11.low_V' 445475 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip11.low_V' 400 t (by omega), Rule30SixteenFrontsStrip14.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip11.prim,
   not_related (w := 537693) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip11.per16 _ (by omega)) (Rule30SixteenFrontsStrip11.per16 _ (by omega))
      (Rule30SixteenFrontsStrip15.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip11.comp_V t, Rule30SixteenFrontsStrip15.low_V' 537693 t (by omega), Rule30SixteenFrontsStrip12.low_V' 537693 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip11.low_V' 400 t (by omega), Rule30SixteenFrontsStrip15.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip11.prim,
   not_related (w := 445475) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip12.per16 _ (by omega)) (Rule30SixteenFrontsStrip12.per16 _ (by omega))
      (Rule30SixteenFrontsStrip13.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip13.low_V' 445475 t (by omega), Rule30SixteenFrontsStrip9.comp_V t, Rule30SixteenFrontsStrip12.low_V' 445475 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip12.low_V' 400 t (by omega), Rule30SixteenFrontsStrip13.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip12.prim,
   not_related (w := 445475) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip12.per16 _ (by omega)) (Rule30SixteenFrontsStrip12.per16 _ (by omega))
      (Rule30SixteenFrontsStrip14.per16 _ (by omega)) (comp_symm (fun t => by rw [Rule30SixteenFrontsStrip14.low_V' 445475 t (by omega), Rule30SixteenFrontsStrip9.comp_V t, Rule30SixteenFrontsStrip12.low_V' 445475 t (by omega)]))
      (fun t => by rw [Rule30SixteenFrontsStrip12.low_V' 400 t (by omega), Rule30SixteenFrontsStrip14.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip12.prim,
   not_related (w := 760455) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip12.per16 _ (by omega)) (Rule30SixteenFrontsStrip12.per16 _ (by omega))
      (Rule30SixteenFrontsStrip15.per16 _ (by omega)) (comp_symm (fun t => Rule30SixteenFrontsStrip15.comp_V t))
      (fun t => by rw [Rule30SixteenFrontsStrip15.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip12.prim,
   not_related (w := 482609) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip13.per16 _ (by omega)) (Rule30SixteenFrontsStrip13.per16 _ (by omega))
      (Rule30SixteenFrontsStrip14.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip13.comp_V t, Rule30SixteenFrontsStrip14.low_V' 482609 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip13.low_V' 400 t (by omega), Rule30SixteenFrontsStrip14.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip13.prim,
   not_related (w := 445475) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip13.per16 _ (by omega)) (Rule30SixteenFrontsStrip13.per16 _ (by omega))
      (Rule30SixteenFrontsStrip15.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip13.low_V' 445475 t (by omega), Rule30SixteenFrontsStrip9.comp_V t, Rule30SixteenFrontsStrip15.low_V' 445475 t (by omega), Rule30SixteenFrontsStrip12.low_V' 445475 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip13.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip15.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip13.prim,
   not_related (w := 445475) (p := 400) (by omega) (by omega) (Rule30SixteenFrontsStrip14.per16 _ (by omega)) (Rule30SixteenFrontsStrip14.per16 _ (by omega))
      (Rule30SixteenFrontsStrip15.per16 _ (by omega)) (fun t => by rw [Rule30SixteenFrontsStrip14.low_V' 445475 t (by omega), Rule30SixteenFrontsStrip9.comp_V t, Rule30SixteenFrontsStrip15.low_V' 445475 t (by omega), Rule30SixteenFrontsStrip12.low_V' 445475 t (by omega)])
      (fun t => by rw [Rule30SixteenFrontsStrip14.low_V' 400 t (by omega), Rule30SixteenFrontsStrip9.low_V' 400 t (by omega), Rule30SixteenFrontsStrip15.low_V' 400 t (by omega), Rule30SixteenFrontsStrip12.low_V' 400 t (by omega)]) Rule30SixteenFrontsStrip14.prim⟩

theorem on_exactly_one {a : Nat → Nat → Bool} {s s' : Nat} :
    ¬ (Aligned K a V0 s 894235 ∧ Aligned K a V1 s' 894235) ∧
    ¬ (Aligned K a V0 s 894235 ∧ Aligned K a V2 s' 894235) ∧
    ¬ (Aligned K a V0 s 894235 ∧ Aligned K a V3 s' 894235) ∧
    ¬ (Aligned K a V0 s 894235 ∧ Aligned K a V4 s' 894235) ∧
    ¬ (Aligned K a V0 s 894235 ∧ Aligned K a V5 s' 894235) ∧
    ¬ (Aligned K a V0 s 894235 ∧ Aligned K a V6 s' 894235) ∧
    ¬ (Aligned K a V0 s 894235 ∧ Aligned K a V7 s' 894235) ∧
    ¬ (Aligned K a V0 s 894235 ∧ Aligned K a V8 s' 894235) ∧
    ¬ (Aligned K a V0 s 894235 ∧ Aligned K a V9 s' 894235) ∧
    ¬ (Aligned K a V0 s 894235 ∧ Aligned K a V10 s' 894235) ∧
    ¬ (Aligned K a V0 s 894235 ∧ Aligned K a V11 s' 894235) ∧
    ¬ (Aligned K a V0 s 894235 ∧ Aligned K a V12 s' 894235) ∧
    ¬ (Aligned K a V0 s 894235 ∧ Aligned K a V13 s' 894235) ∧
    ¬ (Aligned K a V0 s 894235 ∧ Aligned K a V14 s' 894235) ∧
    ¬ (Aligned K a V0 s 894235 ∧ Aligned K a V15 s' 894235) ∧
    ¬ (Aligned K a V1 s 894235 ∧ Aligned K a V2 s' 894235) ∧
    ¬ (Aligned K a V1 s 894235 ∧ Aligned K a V3 s' 894235) ∧
    ¬ (Aligned K a V1 s 894235 ∧ Aligned K a V4 s' 894235) ∧
    ¬ (Aligned K a V1 s 894235 ∧ Aligned K a V5 s' 894235) ∧
    ¬ (Aligned K a V1 s 894235 ∧ Aligned K a V6 s' 894235) ∧
    ¬ (Aligned K a V1 s 894235 ∧ Aligned K a V7 s' 894235) ∧
    ¬ (Aligned K a V1 s 894235 ∧ Aligned K a V8 s' 894235) ∧
    ¬ (Aligned K a V1 s 894235 ∧ Aligned K a V9 s' 894235) ∧
    ¬ (Aligned K a V1 s 894235 ∧ Aligned K a V10 s' 894235) ∧
    ¬ (Aligned K a V1 s 894235 ∧ Aligned K a V11 s' 894235) ∧
    ¬ (Aligned K a V1 s 894235 ∧ Aligned K a V12 s' 894235) ∧
    ¬ (Aligned K a V1 s 894235 ∧ Aligned K a V13 s' 894235) ∧
    ¬ (Aligned K a V1 s 894235 ∧ Aligned K a V14 s' 894235) ∧
    ¬ (Aligned K a V1 s 894235 ∧ Aligned K a V15 s' 894235) ∧
    ¬ (Aligned K a V2 s 894235 ∧ Aligned K a V3 s' 894235) ∧
    ¬ (Aligned K a V2 s 894235 ∧ Aligned K a V4 s' 894235) ∧
    ¬ (Aligned K a V2 s 894235 ∧ Aligned K a V5 s' 894235) ∧
    ¬ (Aligned K a V2 s 894235 ∧ Aligned K a V6 s' 894235) ∧
    ¬ (Aligned K a V2 s 894235 ∧ Aligned K a V7 s' 894235) ∧
    ¬ (Aligned K a V2 s 894235 ∧ Aligned K a V8 s' 894235) ∧
    ¬ (Aligned K a V2 s 894235 ∧ Aligned K a V9 s' 894235) ∧
    ¬ (Aligned K a V2 s 894235 ∧ Aligned K a V10 s' 894235) ∧
    ¬ (Aligned K a V2 s 894235 ∧ Aligned K a V11 s' 894235) ∧
    ¬ (Aligned K a V2 s 894235 ∧ Aligned K a V12 s' 894235) ∧
    ¬ (Aligned K a V2 s 894235 ∧ Aligned K a V13 s' 894235) ∧
    ¬ (Aligned K a V2 s 894235 ∧ Aligned K a V14 s' 894235) ∧
    ¬ (Aligned K a V2 s 894235 ∧ Aligned K a V15 s' 894235) ∧
    ¬ (Aligned K a V3 s 894235 ∧ Aligned K a V4 s' 894235) ∧
    ¬ (Aligned K a V3 s 894235 ∧ Aligned K a V5 s' 894235) ∧
    ¬ (Aligned K a V3 s 894235 ∧ Aligned K a V6 s' 894235) ∧
    ¬ (Aligned K a V3 s 894235 ∧ Aligned K a V7 s' 894235) ∧
    ¬ (Aligned K a V3 s 894235 ∧ Aligned K a V8 s' 894235) ∧
    ¬ (Aligned K a V3 s 894235 ∧ Aligned K a V9 s' 894235) ∧
    ¬ (Aligned K a V3 s 894235 ∧ Aligned K a V10 s' 894235) ∧
    ¬ (Aligned K a V3 s 894235 ∧ Aligned K a V11 s' 894235) ∧
    ¬ (Aligned K a V3 s 894235 ∧ Aligned K a V12 s' 894235) ∧
    ¬ (Aligned K a V3 s 894235 ∧ Aligned K a V13 s' 894235) ∧
    ¬ (Aligned K a V3 s 894235 ∧ Aligned K a V14 s' 894235) ∧
    ¬ (Aligned K a V3 s 894235 ∧ Aligned K a V15 s' 894235) ∧
    ¬ (Aligned K a V4 s 894235 ∧ Aligned K a V5 s' 894235) ∧
    ¬ (Aligned K a V4 s 894235 ∧ Aligned K a V6 s' 894235) ∧
    ¬ (Aligned K a V4 s 894235 ∧ Aligned K a V7 s' 894235) ∧
    ¬ (Aligned K a V4 s 894235 ∧ Aligned K a V8 s' 894235) ∧
    ¬ (Aligned K a V4 s 894235 ∧ Aligned K a V9 s' 894235) ∧
    ¬ (Aligned K a V4 s 894235 ∧ Aligned K a V10 s' 894235) ∧
    ¬ (Aligned K a V4 s 894235 ∧ Aligned K a V11 s' 894235) ∧
    ¬ (Aligned K a V4 s 894235 ∧ Aligned K a V12 s' 894235) ∧
    ¬ (Aligned K a V4 s 894235 ∧ Aligned K a V13 s' 894235) ∧
    ¬ (Aligned K a V4 s 894235 ∧ Aligned K a V14 s' 894235) ∧
    ¬ (Aligned K a V4 s 894235 ∧ Aligned K a V15 s' 894235) ∧
    ¬ (Aligned K a V5 s 894235 ∧ Aligned K a V6 s' 894235) ∧
    ¬ (Aligned K a V5 s 894235 ∧ Aligned K a V7 s' 894235) ∧
    ¬ (Aligned K a V5 s 894235 ∧ Aligned K a V8 s' 894235) ∧
    ¬ (Aligned K a V5 s 894235 ∧ Aligned K a V9 s' 894235) ∧
    ¬ (Aligned K a V5 s 894235 ∧ Aligned K a V10 s' 894235) ∧
    ¬ (Aligned K a V5 s 894235 ∧ Aligned K a V11 s' 894235) ∧
    ¬ (Aligned K a V5 s 894235 ∧ Aligned K a V12 s' 894235) ∧
    ¬ (Aligned K a V5 s 894235 ∧ Aligned K a V13 s' 894235) ∧
    ¬ (Aligned K a V5 s 894235 ∧ Aligned K a V14 s' 894235) ∧
    ¬ (Aligned K a V5 s 894235 ∧ Aligned K a V15 s' 894235) ∧
    ¬ (Aligned K a V6 s 894235 ∧ Aligned K a V7 s' 894235) ∧
    ¬ (Aligned K a V6 s 894235 ∧ Aligned K a V8 s' 894235) ∧
    ¬ (Aligned K a V6 s 894235 ∧ Aligned K a V9 s' 894235) ∧
    ¬ (Aligned K a V6 s 894235 ∧ Aligned K a V10 s' 894235) ∧
    ¬ (Aligned K a V6 s 894235 ∧ Aligned K a V11 s' 894235) ∧
    ¬ (Aligned K a V6 s 894235 ∧ Aligned K a V12 s' 894235) ∧
    ¬ (Aligned K a V6 s 894235 ∧ Aligned K a V13 s' 894235) ∧
    ¬ (Aligned K a V6 s 894235 ∧ Aligned K a V14 s' 894235) ∧
    ¬ (Aligned K a V6 s 894235 ∧ Aligned K a V15 s' 894235) ∧
    ¬ (Aligned K a V7 s 894235 ∧ Aligned K a V8 s' 894235) ∧
    ¬ (Aligned K a V7 s 894235 ∧ Aligned K a V9 s' 894235) ∧
    ¬ (Aligned K a V7 s 894235 ∧ Aligned K a V10 s' 894235) ∧
    ¬ (Aligned K a V7 s 894235 ∧ Aligned K a V11 s' 894235) ∧
    ¬ (Aligned K a V7 s 894235 ∧ Aligned K a V12 s' 894235) ∧
    ¬ (Aligned K a V7 s 894235 ∧ Aligned K a V13 s' 894235) ∧
    ¬ (Aligned K a V7 s 894235 ∧ Aligned K a V14 s' 894235) ∧
    ¬ (Aligned K a V7 s 894235 ∧ Aligned K a V15 s' 894235) ∧
    ¬ (Aligned K a V8 s 894235 ∧ Aligned K a V9 s' 894235) ∧
    ¬ (Aligned K a V8 s 894235 ∧ Aligned K a V10 s' 894235) ∧
    ¬ (Aligned K a V8 s 894235 ∧ Aligned K a V11 s' 894235) ∧
    ¬ (Aligned K a V8 s 894235 ∧ Aligned K a V12 s' 894235) ∧
    ¬ (Aligned K a V8 s 894235 ∧ Aligned K a V13 s' 894235) ∧
    ¬ (Aligned K a V8 s 894235 ∧ Aligned K a V14 s' 894235) ∧
    ¬ (Aligned K a V8 s 894235 ∧ Aligned K a V15 s' 894235) ∧
    ¬ (Aligned K a V9 s 894235 ∧ Aligned K a V10 s' 894235) ∧
    ¬ (Aligned K a V9 s 894235 ∧ Aligned K a V11 s' 894235) ∧
    ¬ (Aligned K a V9 s 894235 ∧ Aligned K a V12 s' 894235) ∧
    ¬ (Aligned K a V9 s 894235 ∧ Aligned K a V13 s' 894235) ∧
    ¬ (Aligned K a V9 s 894235 ∧ Aligned K a V14 s' 894235) ∧
    ¬ (Aligned K a V9 s 894235 ∧ Aligned K a V15 s' 894235) ∧
    ¬ (Aligned K a V10 s 894235 ∧ Aligned K a V11 s' 894235) ∧
    ¬ (Aligned K a V10 s 894235 ∧ Aligned K a V12 s' 894235) ∧
    ¬ (Aligned K a V10 s 894235 ∧ Aligned K a V13 s' 894235) ∧
    ¬ (Aligned K a V10 s 894235 ∧ Aligned K a V14 s' 894235) ∧
    ¬ (Aligned K a V10 s 894235 ∧ Aligned K a V15 s' 894235) ∧
    ¬ (Aligned K a V11 s 894235 ∧ Aligned K a V12 s' 894235) ∧
    ¬ (Aligned K a V11 s 894235 ∧ Aligned K a V13 s' 894235) ∧
    ¬ (Aligned K a V11 s 894235 ∧ Aligned K a V14 s' 894235) ∧
    ¬ (Aligned K a V11 s 894235 ∧ Aligned K a V15 s' 894235) ∧
    ¬ (Aligned K a V12 s 894235 ∧ Aligned K a V13 s' 894235) ∧
    ¬ (Aligned K a V12 s 894235 ∧ Aligned K a V14 s' 894235) ∧
    ¬ (Aligned K a V12 s 894235 ∧ Aligned K a V15 s' 894235) ∧
    ¬ (Aligned K a V13 s 894235 ∧ Aligned K a V14 s' 894235) ∧
    ¬ (Aligned K a V13 s 894235 ∧ Aligned K a V15 s' 894235) ∧
    ¬ (Aligned K a V14 s 894235 ∧ Aligned K a V15 s' 894235) :=
  ⟨fun h => distinct.1 (side_unique Rule30SixteenFrontsStrip1.V_return h.1 h.2),
   fun h => distinct.2.1 (side_unique Rule30SixteenFrontsStrip2.V_return h.1 h.2),
   fun h => distinct.2.2.1 (side_unique Rule30SixteenFrontsStrip3.V_return h.1 h.2),
   fun h => distinct.2.2.2.1 (side_unique Rule30SixteenFrontsStrip4.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip5.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip6.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip7.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip8.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip9.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip10.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip11.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip12.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip13.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip14.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip15.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip2.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip3.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip4.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip5.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip6.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip7.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip8.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip9.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip10.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip11.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip12.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip13.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip14.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip15.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip3.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip4.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip5.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip6.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip7.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip8.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip9.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip10.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip11.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip12.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip13.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip14.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip15.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip4.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip5.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip6.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip7.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip8.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip9.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip10.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip11.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip12.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip13.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip14.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip15.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip5.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip6.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip7.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip8.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip9.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip10.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip11.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip12.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip13.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip14.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip15.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip6.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip7.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip8.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip9.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip10.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip11.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip12.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip13.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip14.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip15.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip7.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip8.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip9.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip10.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip11.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip12.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip13.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip14.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip15.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip8.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip9.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip10.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip11.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip12.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip13.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip14.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip15.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip9.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip10.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip11.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip12.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip13.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip14.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip15.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip10.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip11.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip12.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip13.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip14.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip15.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip11.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip12.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip13.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip14.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip15.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip12.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip13.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip14.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip15.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip13.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip14.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip15.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip14.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1 (side_unique Rule30SixteenFrontsStrip15.V_return h.1 h.2),
   fun h => distinct.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2 (side_unique Rule30SixteenFrontsStrip15.V_return h.1 h.2)⟩

set_option exponentiation.threshold 894246 in
theorem rows_finite : (V0 < 2 ^ K ∧ V0.testBit 0 = true) ∧ (V1 < 2 ^ K ∧ V1.testBit 0 = true) ∧ (V2 < 2 ^ K ∧ V2.testBit 0 = true) ∧ (V3 < 2 ^ K ∧ V3.testBit 0 = true) ∧ (V4 < 2 ^ K ∧ V4.testBit 0 = true) ∧ (V5 < 2 ^ K ∧ V5.testBit 0 = true) ∧ (V6 < 2 ^ K ∧ V6.testBit 0 = true) ∧ (V7 < 2 ^ K ∧ V7.testBit 0 = true) ∧ (V8 < 2 ^ K ∧ V8.testBit 0 = true) ∧ (V9 < 2 ^ K ∧ V9.testBit 0 = true) ∧ (V10 < 2 ^ K ∧ V10.testBit 0 = true) ∧ (V11 < 2 ^ K ∧ V11.testBit 0 = true) ∧ (V12 < 2 ^ K ∧ V12.testBit 0 = true) ∧ (V13 < 2 ^ K ∧ V13.testBit 0 = true) ∧ (V14 < 2 ^ K ∧ V14.testBit 0 = true) ∧ (V15 < 2 ^ K ∧ V15.testBit 0 = true) :=
  ⟨Rule30SixteenFrontsStrip0.V_finite, Rule30SixteenFrontsStrip1.V_finite, Rule30SixteenFrontsStrip2.V_finite, Rule30SixteenFrontsStrip3.V_finite, Rule30SixteenFrontsStrip4.V_finite, Rule30SixteenFrontsStrip5.V_finite, Rule30SixteenFrontsStrip6.V_finite, Rule30SixteenFrontsStrip7.V_finite, Rule30SixteenFrontsStrip8.V_finite, Rule30SixteenFrontsStrip9.V_finite, Rule30SixteenFrontsStrip10.V_finite, Rule30SixteenFrontsStrip11.V_finite, Rule30SixteenFrontsStrip12.V_finite, Rule30SixteenFrontsStrip13.V_finite, Rule30SixteenFrontsStrip14.V_finite, Rule30SixteenFrontsStrip15.V_finite⟩

/-- **Exactly 16 left sides through wheel 894235.** -/
theorem exactly_left_sides :
    (∀ {x : Int → Bool} {lo : Int}, (∀ p, p < lo → x p = false) → x lo = true → ∃ s, OnTreeAligned (Ld x lo) s) ∧
    ((V0 < 2 ^ K ∧ V0.testBit 0 = true) ∧ (V1 < 2 ^ K ∧ V1.testBit 0 = true) ∧ (V2 < 2 ^ K ∧ V2.testBit 0 = true) ∧ (V3 < 2 ^ K ∧ V3.testBit 0 = true) ∧ (V4 < 2 ^ K ∧ V4.testBit 0 = true) ∧ (V5 < 2 ^ K ∧ V5.testBit 0 = true) ∧ (V6 < 2 ^ K ∧ V6.testBit 0 = true) ∧ (V7 < 2 ^ K ∧ V7.testBit 0 = true) ∧ (V8 < 2 ^ K ∧ V8.testBit 0 = true) ∧ (V9 < 2 ^ K ∧ V9.testBit 0 = true) ∧ (V10 < 2 ^ K ∧ V10.testBit 0 = true) ∧ (V11 < 2 ^ K ∧ V11.testBit 0 = true) ∧ (V12 < 2 ^ K ∧ V12.testBit 0 = true) ∧ (V13 < 2 ^ K ∧ V13.testBit 0 = true) ∧ (V14 < 2 ^ K ∧ V14.testBit 0 = true) ∧ (V15 < 2 ^ K ∧ V15.testBit 0 = true)) ∧
    (∀ v, Aligned K (Ld (ofRow v) 0) v 0 894235) ∧
    (¬ Related K 894235 V0 V1 ∧ ¬ Related K 894235 V0 V2 ∧ ¬ Related K 894235 V0 V3 ∧ ¬ Related K 894235 V0 V4 ∧ ¬ Related K 894235 V0 V5 ∧ ¬ Related K 894235 V0 V6 ∧ ¬ Related K 894235 V0 V7 ∧ ¬ Related K 894235 V0 V8 ∧ ¬ Related K 894235 V0 V9 ∧ ¬ Related K 894235 V0 V10 ∧ ¬ Related K 894235 V0 V11 ∧ ¬ Related K 894235 V0 V12 ∧ ¬ Related K 894235 V0 V13 ∧ ¬ Related K 894235 V0 V14 ∧ ¬ Related K 894235 V0 V15 ∧ ¬ Related K 894235 V1 V2 ∧ ¬ Related K 894235 V1 V3 ∧ ¬ Related K 894235 V1 V4 ∧ ¬ Related K 894235 V1 V5 ∧ ¬ Related K 894235 V1 V6 ∧ ¬ Related K 894235 V1 V7 ∧ ¬ Related K 894235 V1 V8 ∧ ¬ Related K 894235 V1 V9 ∧ ¬ Related K 894235 V1 V10 ∧ ¬ Related K 894235 V1 V11 ∧ ¬ Related K 894235 V1 V12 ∧ ¬ Related K 894235 V1 V13 ∧ ¬ Related K 894235 V1 V14 ∧ ¬ Related K 894235 V1 V15 ∧ ¬ Related K 894235 V2 V3 ∧ ¬ Related K 894235 V2 V4 ∧ ¬ Related K 894235 V2 V5 ∧ ¬ Related K 894235 V2 V6 ∧ ¬ Related K 894235 V2 V7 ∧ ¬ Related K 894235 V2 V8 ∧ ¬ Related K 894235 V2 V9 ∧ ¬ Related K 894235 V2 V10 ∧ ¬ Related K 894235 V2 V11 ∧ ¬ Related K 894235 V2 V12 ∧ ¬ Related K 894235 V2 V13 ∧ ¬ Related K 894235 V2 V14 ∧ ¬ Related K 894235 V2 V15 ∧ ¬ Related K 894235 V3 V4 ∧ ¬ Related K 894235 V3 V5 ∧ ¬ Related K 894235 V3 V6 ∧ ¬ Related K 894235 V3 V7 ∧ ¬ Related K 894235 V3 V8 ∧ ¬ Related K 894235 V3 V9 ∧ ¬ Related K 894235 V3 V10 ∧ ¬ Related K 894235 V3 V11 ∧ ¬ Related K 894235 V3 V12 ∧ ¬ Related K 894235 V3 V13 ∧ ¬ Related K 894235 V3 V14 ∧ ¬ Related K 894235 V3 V15 ∧ ¬ Related K 894235 V4 V5 ∧ ¬ Related K 894235 V4 V6 ∧ ¬ Related K 894235 V4 V7 ∧ ¬ Related K 894235 V4 V8 ∧ ¬ Related K 894235 V4 V9 ∧ ¬ Related K 894235 V4 V10 ∧ ¬ Related K 894235 V4 V11 ∧ ¬ Related K 894235 V4 V12 ∧ ¬ Related K 894235 V4 V13 ∧ ¬ Related K 894235 V4 V14 ∧ ¬ Related K 894235 V4 V15 ∧ ¬ Related K 894235 V5 V6 ∧ ¬ Related K 894235 V5 V7 ∧ ¬ Related K 894235 V5 V8 ∧ ¬ Related K 894235 V5 V9 ∧ ¬ Related K 894235 V5 V10 ∧ ¬ Related K 894235 V5 V11 ∧ ¬ Related K 894235 V5 V12 ∧ ¬ Related K 894235 V5 V13 ∧ ¬ Related K 894235 V5 V14 ∧ ¬ Related K 894235 V5 V15 ∧ ¬ Related K 894235 V6 V7 ∧ ¬ Related K 894235 V6 V8 ∧ ¬ Related K 894235 V6 V9 ∧ ¬ Related K 894235 V6 V10 ∧ ¬ Related K 894235 V6 V11 ∧ ¬ Related K 894235 V6 V12 ∧ ¬ Related K 894235 V6 V13 ∧ ¬ Related K 894235 V6 V14 ∧ ¬ Related K 894235 V6 V15 ∧ ¬ Related K 894235 V7 V8 ∧ ¬ Related K 894235 V7 V9 ∧ ¬ Related K 894235 V7 V10 ∧ ¬ Related K 894235 V7 V11 ∧ ¬ Related K 894235 V7 V12 ∧ ¬ Related K 894235 V7 V13 ∧ ¬ Related K 894235 V7 V14 ∧ ¬ Related K 894235 V7 V15 ∧ ¬ Related K 894235 V8 V9 ∧ ¬ Related K 894235 V8 V10 ∧ ¬ Related K 894235 V8 V11 ∧ ¬ Related K 894235 V8 V12 ∧ ¬ Related K 894235 V8 V13 ∧ ¬ Related K 894235 V8 V14 ∧ ¬ Related K 894235 V8 V15 ∧ ¬ Related K 894235 V9 V10 ∧ ¬ Related K 894235 V9 V11 ∧ ¬ Related K 894235 V9 V12 ∧ ¬ Related K 894235 V9 V13 ∧ ¬ Related K 894235 V9 V14 ∧ ¬ Related K 894235 V9 V15 ∧ ¬ Related K 894235 V10 V11 ∧ ¬ Related K 894235 V10 V12 ∧ ¬ Related K 894235 V10 V13 ∧ ¬ Related K 894235 V10 V14 ∧ ¬ Related K 894235 V10 V15 ∧ ¬ Related K 894235 V11 V12 ∧ ¬ Related K 894235 V11 V13 ∧ ¬ Related K 894235 V11 V14 ∧ ¬ Related K 894235 V11 V15 ∧ ¬ Related K 894235 V12 V13 ∧ ¬ Related K 894235 V12 V14 ∧ ¬ Related K 894235 V12 V15 ∧ ¬ Related K 894235 V13 V14 ∧ ¬ Related K 894235 V13 V15 ∧ ¬ Related K 894235 V14 V15) :=
  ⟨fun hl h0 => left_side_classification hl h0, rows_finite, realized, distinct⟩

theorem aligned_uniform {a : Nat → Nat → Bool} {u s : Nat} : ∀ J', Aligned K a u s J' →
    ∃ T, ∀ j, j ≤ J' → ∀ t, T ≤ t → a j (t + s) = Sp K u j t := by
  intro J'
  induction J' with
  | zero =>
    intro h
    obtain ⟨T, hT⟩ := h 0 (Nat.le_refl _)
    exact ⟨T, fun j hj t ht => by
      have e : j = 0 := by omega
      subst e
      exact hT t ht⟩
  | succ J' ih =>
    intro h
    obtain ⟨T1, h1⟩ := ih (fun j hj => h j (by omega))
    obtain ⟨T2, h2⟩ := h (J' + 1) (Nat.le_refl _)
    refine ⟨max T1 T2, fun j hj t ht => ?_⟩
    by_cases hc : j ≤ J'
    · exact h1 j hc t (by omega)
    · have e : j = J' + 1 := by omega
      subst e
      exact h2 t (by omega)

set_option exponentiation.threshold 894246 in
theorem rowAt_succ_lt (v n : Nat) : rowAt K v (n + 1) < 2 ^ K := by
  simp only [rowAt, Rule30UniversalLeftSide.stepK]
  exact Nat.mod_lt _ (Nat.pow_pos (by omega))

set_option exponentiation.threshold 894246 in
theorem eq_of_low_bits {x y : Nat} (hx : x < 2 ^ K) (hy : y < 2 ^ K) (h : ∀ j, j < K → x.testBit j = y.testBit j) : x = y := by
  apply Nat.eq_of_testBit_eq
  intro j
  by_cases hj : j < K
  · exact h j hj
  · have hp : 2 ^ K ≤ 2 ^ j := Nat.pow_le_pow_right (by omega) (by omega)
    rw [Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hx hp), Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le hy hp)]

set_option exponentiation.threshold 894246 in
theorem reaches {v u s : Nat} (hu : rowAt K u 32 = u) (hlt : u < 2 ^ K) (h : Aligned K (Ld (ofRow v) 0) u s 894235) :
    ∃ n, rowAt K v n = u := by
  obtain ⟨T, hT⟩ := aligned_uniform 894235 h
  obtain ⟨n, hn⟩ : ∃ n, (T + 1) * 32 + s = n + 1 := ⟨(T + 1) * 32 + s - 1, by omega⟩
  refine ⟨n + 1, eq_of_low_bits (rowAt_succ_lt v n) hlt fun j hj => ?_⟩
  have hj' : j < 894236 := hj
  have e := hT j (by omega) ((T + 1) * 32) (by omega)
  rw [hn, Ld_row v (by omega)] at e
  have base : rowAt K u (0 + (T + 1) * 32) = u := by
    rw [rowAt_add_mul hu]
    rfl
  rw [Nat.zero_add] at base
  simp only [Sp] at e
  rw [base] at e
  exact e

/-- **Every odd number reaches one of the 16 rows.** -/
theorem odd_reaches_one (v : Nat) (hv : v.testBit 0 = true) :
    ∃ n, rowAt K v n = V0 ∨ rowAt K v n = V1 ∨ rowAt K v n = V2 ∨ rowAt K v n = V3 ∨ rowAt K v n = V4 ∨ rowAt K v n = V5 ∨ rowAt K v n = V6 ∨ rowAt K v n = V7 ∨ rowAt K v n = V8 ∨ rowAt K v n = V9 ∨ rowAt K v n = V10 ∨ rowAt K v n = V11 ∨ rowAt K v n = V12 ∨ rowAt K v n = V13 ∨ rowAt K v n = V14 ∨ rowAt K v n = V15 := by
  have h0 : ofRow v 0 = true := by simpa [ofRow] using hv
  obtain ⟨s, h⟩ := left_side_classification (ofRow_left v) h0
  unfold OnTreeAligned at h
  rcases h with h | h | h | h | h | h | h | h | h | h | h | h | h | h | h | h
  · obtain ⟨n, e⟩ := reaches Rule30SixteenFrontsStrip0.V_return Rule30SixteenFrontsStrip0.V_finite.1 h
    exact ⟨n, Or.inl e⟩
  · obtain ⟨n, e⟩ := reaches Rule30SixteenFrontsStrip1.V_return Rule30SixteenFrontsStrip1.V_finite.1 h
    exact ⟨n, Or.inr (Or.inl e)⟩
  · obtain ⟨n, e⟩ := reaches Rule30SixteenFrontsStrip2.V_return Rule30SixteenFrontsStrip2.V_finite.1 h
    exact ⟨n, Or.inr (Or.inr (Or.inl e))⟩
  · obtain ⟨n, e⟩ := reaches Rule30SixteenFrontsStrip3.V_return Rule30SixteenFrontsStrip3.V_finite.1 h
    exact ⟨n, Or.inr (Or.inr (Or.inr (Or.inl e)))⟩
  · obtain ⟨n, e⟩ := reaches Rule30SixteenFrontsStrip4.V_return Rule30SixteenFrontsStrip4.V_finite.1 h
    exact ⟨n, Or.inr (Or.inr (Or.inr (Or.inr (Or.inl e))))⟩
  · obtain ⟨n, e⟩ := reaches Rule30SixteenFrontsStrip5.V_return Rule30SixteenFrontsStrip5.V_finite.1 h
    exact ⟨n, Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl e)))))⟩
  · obtain ⟨n, e⟩ := reaches Rule30SixteenFrontsStrip6.V_return Rule30SixteenFrontsStrip6.V_finite.1 h
    exact ⟨n, Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl e))))))⟩
  · obtain ⟨n, e⟩ := reaches Rule30SixteenFrontsStrip7.V_return Rule30SixteenFrontsStrip7.V_finite.1 h
    exact ⟨n, Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl e)))))))⟩
  · obtain ⟨n, e⟩ := reaches Rule30SixteenFrontsStrip8.V_return Rule30SixteenFrontsStrip8.V_finite.1 h
    exact ⟨n, Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl e))))))))⟩
  · obtain ⟨n, e⟩ := reaches Rule30SixteenFrontsStrip9.V_return Rule30SixteenFrontsStrip9.V_finite.1 h
    exact ⟨n, Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl e)))))))))⟩
  · obtain ⟨n, e⟩ := reaches Rule30SixteenFrontsStrip10.V_return Rule30SixteenFrontsStrip10.V_finite.1 h
    exact ⟨n, Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl e))))))))))⟩
  · obtain ⟨n, e⟩ := reaches Rule30SixteenFrontsStrip11.V_return Rule30SixteenFrontsStrip11.V_finite.1 h
    exact ⟨n, Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl e)))))))))))⟩
  · obtain ⟨n, e⟩ := reaches Rule30SixteenFrontsStrip12.V_return Rule30SixteenFrontsStrip12.V_finite.1 h
    exact ⟨n, Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl e))))))))))))⟩
  · obtain ⟨n, e⟩ := reaches Rule30SixteenFrontsStrip13.V_return Rule30SixteenFrontsStrip13.V_finite.1 h
    exact ⟨n, Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl e)))))))))))))⟩
  · obtain ⟨n, e⟩ := reaches Rule30SixteenFrontsStrip14.V_return Rule30SixteenFrontsStrip14.V_finite.1 h
    exact ⟨n, Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl e))))))))))))))⟩
  · obtain ⟨n, e⟩ := reaches Rule30SixteenFrontsStrip15.V_return Rule30SixteenFrontsStrip15.V_finite.1 h
    exact ⟨n, Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (e)))))))))))))))⟩

theorem fronts : F w0 894235 = 1792687 ∧ F w1 894235 = 1790969 ∧ F w2 894235 = 1792661 ∧ F w3 894235 = 1795680 ∧ F w4 894235 = 1793886 ∧ F w5 894235 = 1795740 ∧ F w6 894235 = 1795640 ∧ F w7 894235 = 1794531 ∧ F w8 894235 = 1795122 ∧ F w9 894235 = 1796664 ∧ F w10 894235 = 1795047 ∧ F w11 894235 = 1796866 ∧ F w12 894235 = 1797869 ∧ F w13 894235 = 1793976 ∧ F w14 894235 = 1796552 ∧ F w15 894235 = 1798243 :=
  ⟨Rule30SixteenFrontsStrip0.front, Rule30SixteenFrontsStrip1.front, Rule30SixteenFrontsStrip2.front, Rule30SixteenFrontsStrip3.front, Rule30SixteenFrontsStrip4.front, Rule30SixteenFrontsStrip5.front, Rule30SixteenFrontsStrip6.front, Rule30SixteenFrontsStrip7.front, Rule30SixteenFrontsStrip8.front, Rule30SixteenFrontsStrip9.front, Rule30SixteenFrontsStrip10.front, Rule30SixteenFrontsStrip11.front, Rule30SixteenFrontsStrip12.front, Rule30SixteenFrontsStrip13.front, Rule30SixteenFrontsStrip14.front, Rule30SixteenFrontsStrip15.front⟩

end Ruliology.CellularAutomata.Rule30SixteenFronts
