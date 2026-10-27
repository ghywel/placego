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

**Inside the kit's reconstruction.** For free-bit sequences `f`, `g` that agree from index `1` on, with
bits `1` and `2` black, `Theta f` reads the rewrite's prefix at depths `1 .. 7` with `a = f 0`
(`theta_prefix`), `Theta f` and `Theta g` agree at every depth `k ≥ 7` (`theta_first_edit_local`), and
their truncations at every common depth `W ≥ 7` merge at time `2` (`theta_truncate_merge`). The
untruncated merger is the kit's `two_step_shift`; what is added is the localization, which survives a
common finite cut.

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

/-! ### The rewrite inside the kit's reconstruction `Theta` -/

/-- The column-`1` window of `alt f` up to time `8`, with `f 1 = f 2 = true`. -/
def win (c e : Bool) (t : Nat) : Bool := if t = 1 then c else if t = 7 then e else true

theorem alt_eq_win (f : Nat → Bool) (h1 : f 1 = true) (h2 : f 2 = true) (t : Nat) (ht : t ≤ 8) :
    alt f t = win (f 0) (f 3) t := by
  have e : t = 0 ∨ t = 1 ∨ t = 2 ∨ t = 3 ∨ t = 4 ∨ t = 5 ∨ t = 6 ∨ t = 7 ∨ t = 8 := by omega
  rcases e with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;> simp [alt, win, h1, h2]

theorem recon_win (f : Nat → Bool) (h1 : f 1 = true) (h2 : f 2 = true) (k t : Nat)
    (hkt : t + k ≤ 9) : recon (alt f) k t = recon (win (f 0) (f 3)) k t :=
  recon_local k t (fun j hj => alt_eq_win f h1 h2 (t + j) (by omega))

/-- **The prefix of `Theta f`.** With free bits `1` and `2` black, `Theta f` reads the rewrite's
prefix at depths `1 .. 7`: `1 1 0 0 0 1 1` when `f 0` is white, `1 0 1 0 1 0 1` when it is black. -/
theorem theta_prefix (f : Nat → Bool) (h1 : f 1 = true) (h2 : f 2 = true) :
    ∀ k, 1 ≤ k → Theta f k = mergePrefix (f 0) (fun j => Theta f (j + 8)) k := by
  intro k hk
  by_cases h8 : 8 ≤ k
  · obtain ⟨j, rfl⟩ : ∃ j, k = j + 8 := ⟨k - 8, by omega⟩
    rfl
  · show recon (alt f) k 0 = _
    rw [recon_win f h1 h2 k 0 (by omega)]
    have e : k = 1 ∨ k = 2 ∨ k = 3 ∨ k = 4 ∨ k = 5 ∨ k = 6 ∨ k = 7 := by omega
    rcases e with rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
      cases f 0 <;> cases f 3 <;> simp only [mergePrefix] <;> decide

/-- **Changing free bit `0` changes only depths `1 .. 6`.** If two free-bit sequences agree from
index `1` on and their bits `1` and `2` are black, their reconstructed starts agree at every depth
`k ≥ 7`. -/
theorem theta_first_edit_local (f g : Nat → Bool) (hrest : ∀ j, 1 ≤ j → f j = g j)
    (h1 : f 1 = true) (h2 : f 2 = true) : ∀ k, 7 ≤ k → Theta f k = Theta g k := by
  have g1 : g 1 = true := by rw [← hrest 1 (by omega)]; exact h1
  have g2 : g 2 = true := by rw [← hrest 2 (by omega)]; exact h2
  have late : ∀ k t, 2 ≤ t → recon (alt f) k t = recon (alt g) k t := by
    intro k t ht
    apply recon_local k t
    intro j _
    simp only [alt]
    split
    · rfl
    · exact hrest _ (by omega)
  have base : ∀ k t, 7 ≤ k → k ≤ 8 → t ≤ 1 → recon (alt f) k t = recon (alt g) k t := by
    intro k t hk7 hk8 ht
    rw [recon_win f h1 h2 k t (by omega), recon_win g g1 g2 k t (by omega), ← hrest 3 (by omega)]
    have ek : k = 7 ∨ k = 8 := by omega
    have et : t = 0 ∨ t = 1 := by omega
    rcases ek with rfl | rfl <;> rcases et with rfl | rfl <;>
      cases f 0 <;> cases g 0 <;> cases f 3 <;> decide
  have step : ∀ m,
      (recon (alt f) (7 + m) 0 = recon (alt g) (7 + m) 0 ∧
        recon (alt f) (7 + m + 1) 0 = recon (alt g) (7 + m + 1) 0 ∧
        recon (alt f) (7 + m) 1 = recon (alt g) (7 + m) 1 ∧
        recon (alt f) (7 + m + 1) 1 = recon (alt g) (7 + m + 1) 1) := by
    intro m
    induction m with
    | zero => exact ⟨base 7 0 (by omega) (by omega) (by omega), base 8 0 (by omega) (by omega) (by omega),
        base 7 1 (by omega) (by omega) (by omega), base 8 1 (by omega) (by omega) (by omega)⟩
    | succ n ih =>
      obtain ⟨a0, b0, a1, b1⟩ := ih
      have e : 7 + (n + 1) = 7 + n + 1 := by omega
      have e2 : 7 + n + 1 + 1 = (7 + n) + 2 := by omega
      rw [e, e2]
      refine ⟨b0, ?_, b1, ?_⟩
      · rw [recon_two, recon_two, b1, b0, a0]
      · rw [recon_two, recon_two, late (7 + n + 1) 2 (by omega), b1, a1]
  intro k hk
  obtain ⟨m, rfl⟩ : ∃ m, k = 7 + m := ⟨k - 7, by omega⟩
  exact (step m).1

/-- **Common truncations of `Theta` starts merge.** If two free-bit sequences agree from index `1`
on and their bits `1` and `2` are black, then for every common depth `W ≥ 7` the finitely supported
truncations of their reconstructed starts have equal rows at time `2`. -/
theorem theta_truncate_merge (f g : Nat → Bool) (hrest : ∀ j, 1 ≤ j → f j = g j)
    (h1 : f 1 = true) (h2 : f 2 = true) (W : Nat) (hW : 7 ≤ W) :
    zrow (truncate (Theta f) W) 2 = zrow (truncate (Theta g) W) 2 := by
  have g1 : g 1 = true := by rw [← hrest 1 (by omega)]; exact h1
  have g2 : g 2 = true := by rw [← hrest 2 (by omega)]; exact h2
  have htail : (fun j => Theta f (j + 8)) = (fun j => Theta g (j + 8)) :=
    funext fun j => theta_first_edit_local f g hrest h1 h2 (j + 8) (by omega)
  have tf : ∀ k, 1 ≤ k → truncate (Theta f) W k =
      truncate (mergePrefix (f 0) (fun j => Theta f (j + 8))) W k := by
    intro k hk; simp only [truncate]; rw [theta_prefix f h1 h2 k hk]
  have tg : ∀ k, 1 ≤ k → truncate (Theta g) W k =
      truncate (mergePrefix (g 0) (fun j => Theta f (j + 8))) W k := by
    intro k hk; simp only [truncate]; rw [theta_prefix g g1 g2 k hk, ← htail]
  rw [zrow_congr_pos tf, zrow_congr_pos tg]
  cases hf0 : f 0 <;> cases hg0 : g 0
  · rfl
  · exact mergePrefix_truncate _ W hW
  · exact (mergePrefix_truncate _ W hW).symm
  · rfl

end Ruliology.CellularAutomata.Rule30PrefixMerger
