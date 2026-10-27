module

public import Ruliology.CellularAutomata.Rule30Prize
public import Ruliology.CellularAutomata.Rule30ZeroBoundary

/-!
# Rule 30 beside a white wall: a seven-cell prefix rewrite that merges after two steps, for every tail

The zero-boundary left half (`Rule30ZeroBoundary.zrow`): depth `0` is a white wall, and depth `k ≥ 1`
updates by rule 30. Two starts that differ only in the seven cells next to the wall,

  `1 1 0 0 0 1 1` and `1 0 1 0 1 0 1` (read from the wall outward, depths `1 .. 7`),

followed by the **same** arbitrary tail at depths `8, 9, …`, have equal rows at time `2`
(`mergePrefix_two`), and therefore equal rows at every later time (`mergePrefix_future`). The same
holds for their truncations at any common depth `W ≥ 7` (`mergePrefix_truncate`), so finitely
supported starts of every width `W ≥ 7` merge. The depth-7 cell is needed: with it white and the
tail white, the two starts do not merge at time `2` (`mergePrefix_needs_seven`).

General facts used to read such mergers (`trace_tail_iff_row`, `merge_preserves_last_black`): two
starts whose rows agree at time `T` have the same column `1` from `T` on and conversely; and rows
that merge have their last black cells at the same depth.

Contributed by Gareth Herbert with Claude (Anthropic) and GPT (OpenAI). The equal-width statement is
a short application of the kit's `zrow_det` and `zrow_edge`. Nothing here bounds a death time or
decides `Q01`.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30PrefixMerger

open Rule30ZeroBoundary

/-- The prefix `a`-word at depths `1 .. 7` and a common tail from depth `8` on. With `a = false`
the prefix reads `1 1 0 0 0 1 1`, with `a = true` it reads `1 0 1 0 1 0 1`. -/
def mergePrefix (a : Bool) (tail : Nat → Bool) : Nat → Bool
  | 0 => false
  | 1 => true
  | 2 => !a
  | 3 => a
  | 4 => false
  | 5 => a
  | 6 => !a
  | 7 => true
  | k + 8 => tail k

theorem zrow_zero_eq (L : Nat → Bool) (k : Nat) (hk : 1 ≤ k) : zrow L 0 k = L k := by
  match k, hk with
  | j + 1, _ => rfl

theorem zrow_succ_eq (L : Nat → Bool) (t k : Nat) (hk : 1 ≤ k) :
    zrow L (t + 1) k = xor (zrow L t (k + 1)) (zrow L t k || zrow L t (k - 1)) := by
  match k, hk with
  | j + 1, _ => rfl

/-- One step of locality: rows that agree on depths `a .. b` (with `a ≥ 1`) agree one step later
on depths `a + 1 .. b - 1`. -/
theorem step_local {L M : Nat → Bool} {t a b : Nat} (ha : 1 ≤ a)
    (h : ∀ i, a ≤ i → i ≤ b → zrow L t i = zrow M t i) :
    ∀ i, a + 1 ≤ i → i + 1 ≤ b → zrow L (t + 1) i = zrow M (t + 1) i := by
  intro i h1 h2
  rw [zrow_succ_eq L t i (by omega), zrow_succ_eq M t i (by omega),
    h (i + 1) (by omega) (by omega), h i (by omega) (by omega), h (i - 1) (by omega) (by omega)]

theorem mergePrefix_tail (a : Bool) (tail : Nat → Bool) (j : Nat) :
    mergePrefix a tail (j + 8) = tail j := rfl

/-- **The two starts merge after two steps, for every common tail.** -/
theorem mergePrefix_two (tail : Nat → Bool) :
    zrow (mergePrefix false tail) 2 = zrow (mergePrefix true tail) 2 := by
  funext k
  -- far from the wall only the common tail matters
  by_cases hk : 10 ≤ k
  · have h0 : ∀ i, 8 ≤ i → i ≤ k + 2 →
        zrow (mergePrefix false tail) 0 i = zrow (mergePrefix true tail) 0 i := by
      intro i hi _
      obtain ⟨j, rfl⟩ : ∃ j, i = j + 8 := ⟨i - 8, by omega⟩
      rw [zrow_zero_eq _ _ (by omega), zrow_zero_eq _ _ (by omega)]
      rfl
    have h1 := step_local (t := 0) (a := 8) (b := k + 2) (by omega) h0
    exact step_local (t := 1) (a := 9) (b := k + 1) (by omega) (fun i ha hb => h1 i ha (by omega))
      k (by omega) (by omega)
  · -- near the wall: depths 0 .. 9 read the start up to depth 11, i.e. the tail cells 0 .. 3
    have e : k = 0 ∨ k = 1 ∨ k = 2 ∨ k = 3 ∨ k = 4 ∨ k = 5 ∨ k = 6 ∨ k = 7 ∨ k = 8 ∨ k = 9 := by
      omega
    rcases e with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
    · simp [zrow, mergePrefix] <;>
      cases tail 0 <;> cases tail 1 <;> cases tail 2 <;> cases tail 3 <;> simp

/-- After the merger the two starts have the same rows for ever. -/
theorem mergePrefix_future (tail : Nat → Bool) (t : Nat) :
    zrow (mergePrefix false tail) (2 + t) = zrow (mergePrefix true tail) (2 + t) := by
  funext k
  rw [zrow_shift, zrow_shift, mergePrefix_two]

theorem truncate_mergePrefix (a : Bool) (tail : Nat → Bool) (W : Nat) (hW : 7 ≤ W) (k : Nat)
    (hk : 1 ≤ k) :
    truncate (mergePrefix a tail) W k = mergePrefix a (fun j => tail j && decide (j + 8 ≤ W)) k := by
  match k, hk with
  | 1, _ => simp [truncate, mergePrefix]; omega
  | 2, _ => simp [truncate, mergePrefix]; omega
  | 3, _ => simp [truncate, mergePrefix]; omega
  | 4, _ => simp [truncate, mergePrefix]
  | 5, _ => simp [truncate, mergePrefix]; omega
  | 6, _ => simp [truncate, mergePrefix]; omega
  | 7, _ => simp [truncate, mergePrefix]; omega
  | j + 8, _ => simp [truncate, mergePrefix]

theorem zrow_congr_pos {L M : Nat → Bool} (h : ∀ k, 1 ≤ k → L k = M k) : zrow L = zrow M := by
  funext t k
  induction t generalizing k with
  | zero =>
    cases k with
    | zero => rfl
    | succ j => exact h (j + 1) (by omega)
  | succ t ih =>
    cases k with
    | zero => rfl
    | succ j => simp only [zrow]; rw [ih (j + 1 + 1), ih (j + 1), ih (j + 1 - 1)]

/-- **Finite starts of every width `W ≥ 7` merge too.** The truncations at a common depth `W ≥ 7`
merge at time `2`. -/
theorem mergePrefix_truncate (tail : Nat → Bool) (W : Nat) (hW : 7 ≤ W) :
    zrow (truncate (mergePrefix false tail) W) 2 = zrow (truncate (mergePrefix true tail) W) 2 := by
  rw [zrow_congr_pos (truncate_mergePrefix false tail W hW),
    zrow_congr_pos (truncate_mergePrefix true tail W hW)]
  exact mergePrefix_two _

/-- The truncated starts are finitely supported. -/
theorem mergePrefix_truncate_fin (a : Bool) (tail : Nat → Bool) (W : Nat) :
    FinSupp (truncate (mergePrefix a tail) W) := ⟨W, truncate_fin _ W⟩

/-- **The depth-7 cell is needed.** With depth `7` white and a white tail the two six-cell starts
do not merge at time `2`. -/
theorem mergePrefix_needs_seven :
    zrow (truncate (mergePrefix false (fun _ => false)) 6) 2 ≠
      zrow (truncate (mergePrefix true (fun _ => false)) 6) 2 := by
  intro h
  have := congrFun h 8
  revert this
  decide

/-! ### Reading a merger -/

/-- Rows equal at time `T` give equal column `1` from `T` on, and conversely. -/
theorem trace_tail_iff_row (L M : Nat → Bool) (T : Nat) :
    (∀ t, T ≤ t → zrow L t 1 = zrow M t 1) ↔ zrow L T = zrow M T := by
  constructor
  · intro h
    funext k
    exact zrow_det L M k T (fun i _ => h (T + i) (by omega))
  · intro h t ht
    obtain ⟨u, rfl⟩ : ∃ u, t = T + u := ⟨t - T, by omega⟩
    rw [zrow_shift L T u 1, zrow_shift M T u 1, h]

/-- The rightmost black cell of a start. -/
def LastBlack (L : Nat → Bool) (m : Nat) : Prop := 1 ≤ m ∧ L m = true ∧ ∀ k, m < k → L k = false

/-- Starts whose rows merge have their last black cells at the same depth. -/
theorem merge_preserves_last_black (L M : Nat → Bool) (m n T : Nat)
    (hL : LastBlack L m) (hM : LastBlack M n) (hmerge : zrow L T = zrow M T) : m = n := by
  have eL := zrow_edge hL.1 hL.2.1 hL.2.2 T
  have eM := zrow_edge hM.1 hM.2.1 hM.2.2 T
  apply Classical.byContradiction
  intro hne
  rcases Nat.lt_or_gt_of_ne hne with h | h
  · have a := eL.2 (n + T) (by omega)
    have b := eM.1
    rw [hmerge] at a
    rw [a] at b
    exact Bool.false_ne_true b
  · have a := eM.2 (m + T) (by omega)
    have b := eL.1
    rw [hmerge, a] at b
    exact Bool.false_ne_true b

/-- **Guarded merge.** Two starts have equal column `1` at every time from `T` on and at every
earlier even time exactly when their rows agree at time `T` and their earlier even observations
agree. A common future alone does not give the earlier checks. -/
theorem odd_edits_iff_guarded_merge (L M : Nat → Bool) (T : Nat) :
    (∀ t, T ≤ t ∨ t % 2 = 0 → zrow L t 1 = zrow M t 1) ↔
      (zrow L T = zrow M T ∧ ∀ t, t < T → t % 2 = 0 → zrow L t 1 = zrow M t 1) := by
  constructor
  · intro h
    exact ⟨(trace_tail_iff_row L M T).1 (fun t ht => h t (Or.inl ht)),
      fun t _ he => h t (Or.inr he)⟩
  · rintro ⟨hrow, hearly⟩ t ht
    by_cases hT : T ≤ t
    · exact (trace_tail_iff_row L M T).2 hrow t hT
    · rcases ht with ht | ht
      · exact absurd ht hT
      · exact hearly t (by omega) ht

end Ruliology.CellularAutomata.Rule30PrefixMerger
