import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30ZeroBoundaryBarriers
/-!
# A planted survivor: rule 30's survival table with one row added

`Q01` asks whether every finite start of the zero-boundary left half eventually turns depth `1`
white at an even time. Arbitrarily large finite portions of its survival table can also occur
for a different map with an immortal finite row. This module conjugates the kit's step by a
tree automorphism of the rows; the counts differ by the explicit zero-or-one term below.

For `L ≥ 1`, `psi L` flips the cell at every odd depth `k ≥ 2 L + 1` at which the row agrees with
the stripe `…10101` at all depths below `k` (`pf`, `site`). The flip at `k` reads only depths
below `k`, so `psi L` is a tree automorphism, with inverse `psiInv L` (`psi_psiInv`,
`psiInv_psi`), and it fixes the depths up to `2 L`. It sends the stripe to the finite row
`trunc (2 L - 1)` (`psi_stripe`). It keeps finite rows finite (`psi_fin`), and its inverse does not increase
the width of any finite row except `trunc (2 L - 1)` (`psiInv_fin`).

* `T L y = psi L (zrow (psiInv L y) 1)` is rule 30's zero-boundary step read through `psi L`, so
  `n` steps of `T L` are `psi L` of `n` steps of rule 30 (`Tn_eq`), and depth `1` is the same
  (`Tn_depth1`). `T L` maps finite rows to finite rows (`T_finite`), fixes the empty row
  (`T_zero`) and fixes the finite row `trunc (2 L - 1)` (`T_fixed`), whose depth `1` is black at
  every time (`fixed_survives`).
* `survival_table`: for every width bound `W` and time `t`, the rows of width at most `W` that
  pass every even check of depth `1` through `t` number the same under `T L` as under rule 30,
  plus one exactly when `2 L - 1 ≤ W` and `2 ⌈W / 2⌉ ≤ t`. Inside that range `psiInv L` is a
  bijection from the rows of width at most `W` other than `trunc (2 L - 1)` onto those other than
  `trunc (2 ⌈W / 2⌉ - 1)`, which dies at time `2 ⌈W / 2⌉` (`cnt_perm`, `pigeon`).

`T L` is not a cellular automaton and not rule 30. `psi L` and `psiInv L` read a row depth by
depth with a counter up to `2 L`, a parity bit and a prefix-match bit, so `T L` is rule 30's step
between two finite-state transducers. Survival counts of rule 30, however far they are computed,
are therefore also those of a map with an immortal row, up to one row per width. Nothing here
decides `Q01`.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata

open Rule30Jen Rule30ZeroBoundary Rule30ZeroBoundaryBarriers

/-! ### The tree automorphism -/

/-- `pf x k`: `x` agrees with the stripe at the depths `1, …, k - 1`. -/
def pf (x : Nat → Bool) : Nat → Bool
  | 0 => true
  | 1 => true
  | k + 2 => pf x (k + 1) && (x (k + 1) == stripe (k + 1))

/-- The depths where `psi L` may flip: odd and at least `2 L + 1`. -/
def site (L k : Nat) : Bool := decide (k % 2 = 1 ∧ 2 * L + 1 ≤ k)

/-- The automorphism: flip at a site when the row agrees with the stripe below it. -/
def psi (L : Nat) (x : Nat → Bool) (k : Nat) : Bool := xor (x k) (site L k && pf x k)

/-- The agreement flag of the inverse image, computed from the image. -/
def ipf (L : Nat) (y : Nat → Bool) : Nat → Bool
  | 0 => true
  | 1 => true
  | k + 2 => ipf L y (k + 1) && (xor (y (k + 1)) (site L (k + 1) && ipf L y (k + 1)) == stripe (k + 1))

/-- The inverse automorphism. -/
def psiInv (L : Nat) (y : Nat → Bool) (k : Nat) : Bool := xor (y k) (site L k && ipf L y k)

theorem pf_psiInv (L : Nat) (y : Nat → Bool) : ∀ k, pf (psiInv L y) k = ipf L y k
  | 0 => rfl
  | 1 => rfl
  | k + 2 => by simp only [pf, ipf]; rw [pf_psiInv L y (k + 1)]; rfl

theorem ipf_psi (L : Nat) (x : Nat → Bool) : ∀ k, ipf L (psi L x) k = pf x k
  | 0 => rfl
  | 1 => rfl
  | k + 2 => by
    simp only [pf, ipf]
    rw [ipf_psi L x (k + 1)]
    unfold psi
    cases x (k + 1) <;> cases site L (k + 1) <;> cases pf x (k + 1) <;> rfl

theorem psi_psiInv (L : Nat) (y : Nat → Bool) : psi L (psiInv L y) = y := by
  funext k
  unfold psi
  rw [pf_psiInv]
  unfold psiInv
  cases y k <;> cases site L k <;> cases ipf L y k <;> rfl

theorem psiInv_psi (L : Nat) (x : Nat → Bool) : psiInv L (psi L x) = x := by
  funext k
  unfold psiInv
  rw [ipf_psi]
  unfold psi
  cases x k <;> cases site L k <;> cases pf x k <;> rfl

theorem site_small (L k : Nat) (h : k ≤ 2 * L) : site L k = false := decide_eq_false (by omega)

theorem psi_low (L : Nat) (x : Nat → Bool) (k : Nat) (h : k ≤ 2 * L) : psi L x k = x k := by
  unfold psi; rw [site_small L k h]; cases x k <;> rfl

theorem pf_succ (x : Nat → Bool) (m : Nat) (hm : 1 ≤ m) : pf x (m + 1) = (pf x m && (x m == stripe m)) := by
  obtain ⟨j, rfl⟩ : ∃ j, m = j + 1 := ⟨m - 1, by omega⟩
  rfl

/-- `pf x k` is agreement with the stripe below `k`. -/
theorem pf_iff (x : Nat → Bool) : ∀ k, pf x k = true ↔ ∀ j, 1 ≤ j → j < k → x j = stripe j
  | 0 => by simp only [pf, true_iff]; intro j h1 h2; omega
  | 1 => by simp only [pf, true_iff]; intro j h1 h2; omega
  | k + 2 => by
    simp only [pf, Bool.and_eq_true, beq_iff_eq]
    rw [pf_iff x (k + 1)]
    constructor
    · rintro ⟨h, hk⟩ j h1 h2
      by_cases e : j = k + 1
      · subst e; exact hk
      · exact h j h1 (by omega)
    · intro h
      exact ⟨fun j h1 h2 => h j h1 (by omega), h (k + 1) (by omega) (by omega)⟩

theorem pf_congr {x x' : Nat → Bool} (h : ∀ j, 1 ≤ j → x j = x' j) (k : Nat) : pf x k = pf x' k := by
  rcases Bool.eq_false_or_eq_true (pf x k) with h1 | h1
  · rw [h1]; symm; exact (pf_iff x' k).2 fun j a b => by rw [← h j a]; exact (pf_iff x k).1 h1 j a b
  · rw [h1]; symm
    rcases Bool.eq_false_or_eq_true (pf x' k) with h2 | h2
    · exfalso
      have := (pf_iff x k).2 fun j a b => by rw [h j a]; exact (pf_iff x' k).1 h2 j a b
      rw [h1] at this; exact absurd this (by decide)
    · exact h2

theorem psi_congr (L : Nat) {x x' : Nat → Bool} (h : ∀ j, 1 ≤ j → x j = x' j) :
    ∀ k, 1 ≤ k → psi L x k = psi L x' k := by
  intro k hk
  unfold psi
  rw [h k hk, pf_congr h k]

theorem psiInv_congr (L : Nat) {y y' : Nat → Bool} (h : ∀ j, 1 ≤ j → y j = y' j) :
    ∀ k, 1 ≤ k → psiInv L y k = psiInv L y' k := by
  -- the inverse images agree at all depths at least 1, by induction on the depth
  have key : ∀ n, ∀ k, 1 ≤ k → k ≤ n → psiInv L y k = psiInv L y' k := by
    intro n
    induction n with
    | zero => intro k h1 h2; omega
    | succ n ih =>
      intro k h1 h2
      unfold psiInv
      rw [h k h1, ← pf_psiInv, ← pf_psiInv]
      have : pf (psiInv L y) k = pf (psiInv L y') k := by
        rcases Bool.eq_false_or_eq_true (pf (psiInv L y) k) with a | a
        · rw [a]; symm; exact (pf_iff _ k).2 fun j b c => by
            rw [← ih j b (by omega)]; exact (pf_iff _ k).1 a j b c
        · rw [a]; symm
          rcases Bool.eq_false_or_eq_true (pf (psiInv L y') k) with b | b
          · exfalso
            have := (pf_iff (psiInv L y) k).2 fun j c d => by
              rw [ih j c (by omega)]; exact (pf_iff _ k).1 b j c d
            rw [a] at this; exact absurd this (by decide)
          · exact b
      rw [this]
  intro k hk
  exact key k k hk (Nat.le_refl k)

theorem pf_stripe : ∀ k, pf stripe k = true
  | 0 => rfl
  | 1 => rfl
  | k + 2 => by simp only [pf]; rw [pf_stripe (k + 1)]; simp

/-- **The stripe goes to a finite row.** -/
theorem psi_stripe (L : Nat) : ∀ k, 1 ≤ k → psi L stripe k = trunc (2 * L - 1) k := by
  intro k hk
  unfold psi trunc truncate site
  rw [pf_stripe]
  unfold stripe
  by_cases h1 : k % 2 = 1
  · by_cases h2 : 2 * L + 1 ≤ k
    · rw [decide_eq_true ⟨h1, h2⟩, decide_eq_false (show ¬ k ≤ 2 * L - 1 by omega)]; simp [h1]
    · rw [decide_eq_false (show ¬ (k % 2 = 1 ∧ 2 * L + 1 ≤ k) by omega),
        decide_eq_true (show k ≤ 2 * L - 1 by omega)]; simp [h1]
  · rw [decide_eq_false (show ¬ (k % 2 = 1 ∧ 2 * L + 1 ≤ k) by omega)]; simp [h1]

theorem psiInv_trunc (L : Nat) : ∀ k, 1 ≤ k → psiInv L (trunc (2 * L - 1)) k = stripe k := by
  intro k hk
  have h := psiInv_congr L (y := psi L stripe) (y' := trunc (2 * L - 1)) (psi_stripe L) k hk
  rw [psiInv_psi] at h
  exact h.symm

/-! ### Finite rows -/

/-- A row of width at most `W`. -/
def Fin_ (W : Nat) (y : Nat → Bool) : Prop := ∀ k, W < k → y k = false

theorem pf_false_of_fin {x : Nat → Bool} {W : Nat} (hx : Fin_ W x) (k : Nat) (hk : W + 3 ≤ k) :
    pf x k = false := by
  rcases Bool.eq_false_or_eq_true (pf x k) with h | h
  · exfalso
    have hag := (pf_iff x k).1 h
    have hj : (if W % 2 = 0 then W + 1 else W + 2) % 2 = 1 := by split <;> omega
    have := hag (if W % 2 = 0 then W + 1 else W + 2) (by split <;> omega) (by split <;> omega)
    rw [hx _ (by split <;> omega), stripe_odd hj] at this
    exact absurd this (by decide)
  · exact h

/-- **`psi` keeps finite rows finite**, within two depths. -/
theorem psi_fin (L : Nat) {x : Nat → Bool} {W : Nat} (hx : Fin_ W x) : Fin_ (W + 2) (psi L x) := by
  intro k hk
  unfold psi
  rw [hx k (by omega), pf_false_of_fin hx k (by omega)]
  cases site L k <;> rfl

/-- **The inverse does not increase the width of a finite row, unless the row is the image of
the stripe.** -/
theorem psiInv_fin (L : Nat) {y : Nat → Bool} {W : Nat} (hy : Fin_ W y)
    (hne : ¬ ∀ k, 1 ≤ k → y k = trunc (2 * L - 1) k) : Fin_ W (psiInv L y) := by
  intro k hk
  refine Classical.byContradiction fun hk' => ?_
  have hxk : psiInv L y k = true := by simpa using hk'
  have hs : site L k = true ∧ pf (psiInv L y) k = true := by
    unfold psiInv at hxk
    rw [hy k hk, ← pf_psiInv] at hxk
    revert hxk; cases site L k <;> cases pf (psiInv L y) k <;> simp
  have hsite : k % 2 = 1 ∧ 2 * L + 1 ≤ k := by
    have := hs.1; unfold site at this; simpa using this
  have hall : ∀ n, pf (psiInv L y) (k + 1 + n) = true := by
    intro n
    induction n with
    | zero =>
      rw [Nat.add_zero, pf_succ _ k (by omega), hs.2, hxk, stripe_odd hsite.1]; rfl
    | succ n ih =>
      rw [show k + 1 + (n + 1) = (k + 1 + n) + 1 by omega, pf_succ _ _ (by omega), ih]
      unfold psiInv
      rw [hy _ (by omega), ← pf_psiInv, ih]
      unfold site stripe
      by_cases o : (k + 1 + n) % 2 = 1
      · rw [decide_eq_true ⟨o, by omega⟩]; simp [o]
      · rw [decide_eq_false (show ¬ ((k + 1 + n) % 2 = 1 ∧ 2 * L + 1 ≤ k + 1 + n) by omega)]; simp [o]
  have hx : ∀ j, 1 ≤ j → psiInv L y j = stripe j := by
    intro j hj
    exact (pf_iff _ (k + 1 + j)).1 (hall j) j hj (by omega)
  apply hne
  intro j hj
  have e := psi_congr L hx j hj
  rw [psi_psiInv, psi_stripe L j hj] at e
  exact e

/-! ### The conjugated map -/

/-- One step of the conjugated map: rule 30's zero-boundary step, read through `psi L`. -/
def T (L : Nat) (y : Nat → Bool) : Nat → Bool := psi L (zrow (psiInv L y) 1)

/-- `n` steps of the conjugated map. -/
def Tn (L : Nat) (y : Nat → Bool) : Nat → (Nat → Bool)
  | 0 => y
  | n + 1 => T L (Tn L y n)

/-- **Conjugacy**: `n` steps of `T L` are `psi L` of `n` steps of rule 30 on `psiInv L y`. -/
theorem Tn_eq (L : Nat) (y : Nat → Bool) : ∀ n k, 1 ≤ k → Tn L y n k = psi L (zrow (psiInv L y) n) k
  | 0, k, hk => by
    show y k = _
    have := psi_congr L (x := psiInv L y) (x' := zrow (psiInv L y) 0)
      (fun j hj => (zrow_zero_of_pos _ hj).symm) k hk
    rw [← this, psi_psiInv]
  | n + 1, k, hk => by
    show psi L (zrow (psiInv L (Tn L y n)) 1) k = psi L (zrow (psiInv L y) (n + 1)) k
    apply psi_congr L _ k hk
    intro j _
    have h1 : ∀ i, 1 ≤ i → psiInv L (Tn L y n) i = zrow (psiInv L y) n i := by
      intro i hi
      have := psiInv_congr L (y := Tn L y n) (y' := psi L (zrow (psiInv L y) n))
        (fun m hm => Tn_eq L y n m hm) i hi
      rw [this, psiInv_psi]
    rw [zrow_congr h1 1 j]
    exact (zrow_shift (psiInv L y) n 1 j).symm

/-- Depth `1` under `T L` is depth `1` under rule 30 from the inverse row. -/
theorem Tn_depth1 (L : Nat) (hL : 1 ≤ L) (y : Nat → Bool) (n : Nat) :
    Tn L y n 1 = zrow (psiInv L y) n 1 := by
  rw [Tn_eq L y n 1 (Nat.le_refl 1)]
  exact psi_low L _ 1 (by omega)

theorem zrow_false : ∀ t k, zrow (fun _ => false) t k = false
  | 0, k => by unfold zrow; split <;> rfl
  | t + 1, k => by
    unfold zrow
    split
    · rfl
    · rw [zrow_false t (k + 1), zrow_false t k, zrow_false t (k - 1)]; rfl

theorem trunc_one (L : Nat) (hL : 1 ≤ L) : trunc (2 * L - 1) 1 = true := by
  unfold trunc truncate stripe
  rw [decide_eq_true (show 1 ≤ 2 * L - 1 by omega)]; rfl

/-- **`T L` fixes the empty row.** -/
theorem T_zero (L : Nat) (hL : 1 ≤ L) : ∀ k, 1 ≤ k → T L (fun _ => false) k = false := by
  have hne0 : ¬ ∀ k, 1 ≤ k → (fun _ : Nat => false) k = trunc (2 * L - 1) k := by
    intro h
    have := h 1 (Nat.le_refl 1)
    rw [trunc_one L hL] at this
    exact absurd this (by decide)
  have hz : Fin_ 0 (psiInv L (fun _ => false)) := psiInv_fin L (fun k _ => rfl) hne0
  intro k hk
  unfold T
  rw [psi_congr L (x := zrow (psiInv L (fun _ => false)) 1) (x' := fun _ => false) (fun j _ => by
    rw [zrow_congr (L' := fun _ => false) (fun i hi => hz i (by omega)) 1 j, zrow_false]) k hk]
  by_cases h : k ≤ 2 * L
  · rw [psi_low L _ k h]
  · unfold psi
    rw [pf_false_of_fin (W := 0) (fun _ _ => rfl) k (by omega)]
    cases site L k <;> rfl

/-- **`T L` fixes the finite row `trunc (2 L - 1)`.** -/
theorem T_fixed (L : Nat) : ∀ k, 1 ≤ k → T L (trunc (2 * L - 1)) k = trunc (2 * L - 1) k := by
  intro k hk
  unfold T
  rw [psi_congr L (x := zrow (psiInv L (trunc (2 * L - 1))) 1) (x' := stripe) (fun j _ => by
    rw [zrow_congr (L' := stripe) (psiInv_trunc L) 1 j, zrow_stripe]) k hk, psi_stripe L k hk]

/-- **The fixed row survives for ever**: depth `1` is black at every time. -/
theorem fixed_survives (L : Nat) (hL : 1 ≤ L) (n : Nat) : Tn L (trunc (2 * L - 1)) n 1 = true := by
  rw [Tn_depth1 L hL, zrow_congr (L' := stripe) (psiInv_trunc L) n 1, zrow_stripe]; rfl

theorem zrow_one_fin {s : Nat → Bool} {W : Nat} (hs : Fin_ W s) : Fin_ (W + 1) (zrow s 1) := by
  intro k hk
  obtain ⟨j, rfl⟩ : ∃ j, k = j + 1 := ⟨k - 1, by omega⟩
  rw [zrow_succ, zrow_zero_of_pos _ (by omega), zrow_zero_of_pos _ (by omega),
    zrow_zero_of_pos _ (by omega), hs _ (by omega), hs _ (by omega), hs _ (by omega)]
  rfl

/-- **`T L` maps finite rows to finite rows.** -/
theorem T_finite (L : Nat) {y : Nat → Bool} {W : Nat} (hy : Fin_ W y) : ∃ W', Fin_ W' (T L y) := by
  by_cases h : ∀ k, 1 ≤ k → y k = trunc (2 * L - 1) k
  · refine ⟨2 * L - 1, fun k hk => ?_⟩
    have := T_fixed L k (by omega)
    have e : T L y k = T L (trunc (2 * L - 1)) k := by
      unfold T
      apply psi_congr L _ k (by omega)
      intro j _
      exact zrow_congr (psiInv_congr L h) 1 j
    rw [e, this]
    unfold trunc truncate
    rw [decide_eq_false (show ¬ k ≤ 2 * L - 1 by omega), Bool.and_false]
  · exact ⟨W + 3, psi_fin L (zrow_one_fin (psiInv_fin L hy h))⟩

/-! ### Rows as numbers, and counting -/

/-- The row of a number: bit `k - 1` at depth `k`. -/
def ofNat (Y : Nat) (k : Nat) : Bool := if k = 0 then false else Y.testBit (k - 1)

/-- The first `k` bits of a sequence, as a number. -/
def enc : Nat → (Nat → Bool) → Nat
  | 0, _ => 0
  | k + 1, c => (if c 0 then 1 else 0) + 2 * enc k (fun i => c (i + 1))

theorem testBit_enc : ∀ k (c : Nat → Bool) i, (enc k c).testBit i = (decide (i < k) && c i)
  | 0, c, i => by simp [enc]
  | k + 1, c, 0 => by
    rw [Nat.testBit_zero]
    simp only [enc]
    by_cases h : c 0 <;> simp [h] <;> omega
  | k + 1, c, i + 1 => by
    rw [Nat.testBit_succ]
    simp only [enc]
    have : ((if c 0 then 1 else 0) + 2 * enc k (fun i => c (i + 1))) / 2 = enc k (fun i => c (i + 1)) := by
      by_cases h : c 0 <;> simp [h] <;> omega
    rw [this, testBit_enc k (fun i => c (i + 1)) i]
    simp

theorem enc_lt : ∀ k (c : Nat → Bool), enc k c < 2 ^ k
  | 0, _ => by simp [enc]
  | k + 1, c => by
    have := enc_lt k (fun i => c (i + 1))
    simp only [enc, Nat.pow_succ]
    split <;> omega

/-- The number of a row of width at most `W`. -/
def toNat (W : Nat) (s : Nat → Bool) : Nat := enc W (fun i => s (i + 1))

theorem toNat_lt (W : Nat) (s : Nat → Bool) : toNat W s < 2 ^ W := enc_lt W _

theorem ofNat_fin {W Y : Nat} (h : Y < 2 ^ W) : Fin_ W (ofNat Y) := fun k hk => by
  unfold ofNat
  rw [ite_eq_right (show ¬ k = 0 by omega)]
  exact Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le h (Nat.pow_le_pow_right (by decide) (by omega)))

theorem ofNat_toNat {W : Nat} {s : Nat → Bool} (hs : Fin_ W s) : ∀ k, 1 ≤ k → ofNat (toNat W s) k = s k := by
  intro k hk
  unfold ofNat toNat
  rw [ite_eq_right (show ¬ k = 0 by omega), testBit_enc]
  by_cases h : k - 1 < W
  · simp [h, show k - 1 + 1 = k by omega]
  · simp [h]; exact hs k (by omega)

theorem toNat_ofNat {W Y : Nat} (h : Y < 2 ^ W) : toNat W (ofNat Y) = Y := by
  apply Nat.eq_of_testBit_eq
  intro i
  unfold toNat
  rw [testBit_enc]
  unfold ofNat
  by_cases hi : i < W
  · simp [hi]
  · have hb : Y.testBit i = false :=
      Nat.testBit_lt_two_pow (Nat.lt_of_lt_of_le h (Nat.pow_le_pow_right (by decide) (show W ≤ i by omega)))
    simp [hi, hb]

theorem toNat_congr {W : Nat} {s s' : Nat → Bool} (h : ∀ k, 1 ≤ k → s k = s' k) : toNat W s = toNat W s' := by
  unfold toNat
  congr 1
  funext i
  exact h (i + 1) (by omega)

/-- Passing every even check of depth `1` through time `t`, under rule 30. -/
def survZ (s : Nat → Bool) (t : Nat) : Bool := (List.range (t / 2 + 1)).all fun i => zrow s (2 * i) 1

/-- Passing every even check of depth `1` through time `t`, under `T L`. -/
def survT (L : Nat) (y : Nat → Bool) (t : Nat) : Bool := (List.range (t / 2 + 1)).all fun i => Tn L y (2 * i) 1

theorem survT_eq (L : Nat) (hL : 1 ≤ L) (y : Nat → Bool) (t : Nat) : survT L y t = survZ (psiInv L y) t := by
  unfold survT survZ
  congr 1
  funext i
  exact Tn_depth1 L hL y (2 * i)

theorem survZ_congr {s s' : Nat → Bool} (h : ∀ k, 1 ≤ k → s k = s' k) (t : Nat) : survZ s t = survZ s' t := by
  unfold survZ
  congr 1
  funext i
  exact zrow_congr h _ _

theorem survZ_stripe (t : Nat) : survZ stripe t = true :=
  List.all_eq_true.2 fun i _ => by rw [zrow_stripe]; rfl

theorem survZ_trunc (m : Nat) (hm : 1 ≤ m) (t : Nat) : survZ (trunc (2 * m - 1)) t = decide (t < 2 * m) := by
  have hn : (2 * m - 1) % 2 = 1 := by omega
  by_cases h : t < 2 * m
  · rw [decide_eq_true h]
    exact List.all_eq_true.2 fun i hi => by
      rw [List.mem_range] at hi
      exact (trunc_survives hn).1 _ (by omega)
  · rw [decide_eq_false h]
    apply List.all_eq_false.2
    refine ⟨m, List.mem_range.2 (by omega), ?_⟩
    have := (trunc_survives hn).2
    rw [show 2 * m - 1 + 1 = 2 * m by omega] at this
    rw [this]; decide

/-- The number of `Y < n` with `p Y`. -/
def cnt : Nat → (Nat → Bool) → Nat
  | 0, _ => 0
  | n + 1, p => cnt n p + (if p n then 1 else 0)

theorem cnt_congr {n : Nat} {p q : Nat → Bool} (h : ∀ i, i < n → p i = q i) : cnt n p = cnt n q := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [cnt]; rw [ih (fun i hi => h i (by omega)), h n (by omega)]

/-- Changing one value changes the count by the difference. -/
theorem cnt_update {n : Nat} {p q : Nat → Bool} (i0 : Nat) (hi0 : i0 < n) (h : ∀ i, i < n → i ≠ i0 → p i = q i) :
    cnt n p + (if q i0 then 1 else 0) = cnt n q + (if p i0 then 1 else 0) := by
  induction n with
  | zero => omega
  | succ n ih =>
    simp only [cnt]
    by_cases e : i0 = n
    · subst e
      rw [cnt_congr (fun i hi => h i (by omega) (by omega))]
      omega
    · have := ih (by omega) (fun i hi hne => h i (by omega) hne)
      rw [h n (by omega) (fun h' => e h'.symm)]
      omega

/-- Pigeonhole: an injective map from `N` numbers into `M` numbers needs `N ≤ M`. -/
theorem pigeon : ∀ (N M : Nat) (g : Nat → Nat), (∀ i, i < N → g i < M) →
    (∀ i j, i < N → j < N → g i = g j → i = j) → N ≤ M
  | 0, _, _, _, _ => Nat.zero_le _
  | N + 1, M, g, hg, hinj => by
    let g' : Nat → Nat := fun i => if g N < g i then g i - 1 else g i
    have hne : ∀ i, i < N → g i ≠ g N := fun i hi e => by have := hinj i N (by omega) (by omega) e; omega
    have h1 : ∀ i, i < N → g' i < M - 1 := by
      intro i hi
      have := hg i (by omega); have := hg N (by omega); have := hne i hi
      simp only [g']; split <;> omega
    have h2 : ∀ i j, i < N → j < N → g' i = g' j → i = j := by
      intro i j hi hj e
      have a1 := hne i hi; have a2 := hne j hj
      simp only [g'] at e
      apply hinj i j (by omega) (by omega)
      split at e <;> split at e <;> omega
    have := pigeon N (M - 1) g' h1 h2
    have := hg N (by omega)
    omega

/-- **Counting along an injective self-map of `0 .. n - 1`.** -/
theorem cnt_perm : ∀ (n : Nat) (f : Nat → Nat), (∀ i, i < n → f i < n) →
    (∀ i j, i < n → j < n → f i = f j → i = j) → ∀ p : Nat → Bool, cnt n (fun i => p (f i)) = cnt n p
  | 0, _, _, _, _ => rfl
  | n + 1, f, hf, hinj, p => by
    let a := f n
    let f' : Nat → Nat := fun i => if f i = n then a else f i
    have ha : a ≠ n → a < n := fun h => by have := hf n (by omega); omega
    have hf' : ∀ i, i < n → f' i < n := by
      intro i hi
      simp only [f']
      split
      · rename_i h
        apply ha
        intro e
        have := hinj i n (by omega) (by omega) (by rw [h]; exact e.symm)
        omega
      · rename_i h; have := hf i (by omega); omega
    have hinj' : ∀ i j, i < n → j < n → f' i = f' j → i = j := by
      intro i j hi hj e
      simp only [f'] at e
      split at e <;> split at e
      · rename_i h1 h2; exact hinj i j (by omega) (by omega) (by rw [h1, h2])
      · rename_i h1 h2; exfalso; have := hinj n j (by omega) (by omega) e; omega
      · rename_i h1 h2; exfalso; have := hinj i n (by omega) (by omega) e; omega
      · exact hinj i j (by omega) (by omega) e
    have ih := cnt_perm n f' hf' hinj' p
    show cnt n (fun i => p (f i)) + (if p (f n) then 1 else 0) = cnt n p + (if p n then 1 else 0)
    by_cases hex : ∃ i0, i0 < n ∧ f i0 = n
    · obtain ⟨i0, hi0, e0⟩ := hex
      have u := cnt_update (p := fun i => p (f i)) (q := fun i => p (f' i)) i0 hi0 (fun i hi hne => by
        simp only [f']
        rw [ite_eq_right (fun h => hne (hinj i i0 (by omega) (by omega) (by rw [h, e0])))])
      simp only [f', e0, ite_true] at u
      rw [ih] at u
      show cnt n (fun i => p (f i)) + (if p a then 1 else 0) = _
      omega
    · have hall : ∀ i, i < n → f i ≠ n := fun i hi e => hex ⟨i, hi, e⟩
      have e1 : cnt n (fun i => p (f i)) = cnt n (fun i => p (f' i)) :=
        cnt_congr fun i hi => by simp only [f']; rw [ite_eq_right (hall i hi)]
      by_cases han : a = n
      · rw [e1, ih]; show _ + (if p a then 1 else 0) = _; rw [han]
      · exfalso
        have := pigeon (n + 1) n f (fun i hi => by
          by_cases e : i = n
          · subst e; exact ha han
          · have := hf i hi; have := hall i (by omega); omega) hinj
        omega

/-! ### The survival table -/

/-- `uN j = (4 ^ j - 1) / 3`, the number of the truncated stripe `trunc (2 j - 1)`. -/
def uN : Nat → Nat
  | 0 => 0
  | j + 1 => 4 * uN j + 1

theorem testBit_uN : ∀ j i, (uN j).testBit i = decide (i % 2 = 0 ∧ i + 2 ≤ 2 * j)
  | 0, i => by
    rw [show uN 0 = 0 from rfl, Nat.zero_testBit, decide_eq_false (by omega)]
  | j + 1, 0 => by
    rw [Nat.testBit_zero, decide_eq_true (show (0 : Nat) % 2 = 0 ∧ 0 + 2 ≤ 2 * (j + 1) by omega)]
    show decide ((4 * uN j + 1) % 2 = 1) = true
    exact decide_eq_true (by omega)
  | j + 1, 1 => by
    rw [Nat.testBit_succ, Nat.testBit_zero, decide_eq_false (show ¬ ((1 : Nat) % 2 = 0 ∧ 1 + 2 ≤ 2 * (j + 1)) by omega)]
    show decide ((4 * uN j + 1) / 2 % 2 = 1) = false
    exact decide_eq_false (by omega)
  | j + 1, i + 2 => by
    rw [Nat.testBit_succ, Nat.testBit_succ]
    show ((4 * uN j + 1) / 2 / 2).testBit i = _
    rw [show (4 * uN j + 1) / 2 / 2 = uN j by omega, testBit_uN j i]
    exact decide_eq_decide.2 (by omega)

theorem ofNat_uN (j : Nat) : ∀ k, 1 ≤ k → ofNat (uN j) k = trunc (2 * j - 1) k := by
  intro k hk
  unfold ofNat trunc truncate stripe
  rw [ite_eq_right (show ¬ k = 0 by omega), testBit_uN]
  by_cases h1 : k % 2 = 1
  · by_cases h2 : k ≤ 2 * j - 1
    · rw [decide_eq_true (show (k - 1) % 2 = 0 ∧ k - 1 + 2 ≤ 2 * j by omega), decide_eq_true h2]; simp [h1]
    · rw [decide_eq_false (show ¬ ((k - 1) % 2 = 0 ∧ k - 1 + 2 ≤ 2 * j) by omega), decide_eq_false h2]; simp
  · rw [decide_eq_false (show ¬ ((k - 1) % 2 = 0 ∧ k - 1 + 2 ≤ 2 * j) by omega)]; simp [h1]

theorem uN_lt : ∀ j, 1 ≤ j → uN j < 2 ^ (2 * j - 1)
  | 0, h => absurd h (by omega)
  | 1, _ => by decide
  | j + 2, _ => by
    have ih := uN_lt (j + 1) (by omega)
    show 4 * uN (j + 1) + 1 < 2 ^ (2 * (j + 2) - 1)
    rw [show 2 * (j + 2) - 1 = (2 * (j + 1) - 1) + 2 by omega, Nat.pow_add]
    omega

theorem psi_trunc_top (L m : Nat) (hm : L ≤ m) : psi L (trunc (2 * m - 1)) (2 * m + 1) = true := by
  have hpf : pf (trunc (2 * m - 1)) (2 * m + 1) = true := by
    apply (pf_iff _ _).2
    intro j h1 h2
    unfold trunc truncate
    by_cases h : j ≤ 2 * m - 1
    · rw [decide_eq_true h, Bool.and_true]
    · rw [decide_eq_false h, Bool.and_false, stripe_even (show j % 2 = 0 by omega)]
  unfold psi
  rw [hpf, decide_eq_true (show (2 * m + 1) % 2 = 1 ∧ 2 * L + 1 ≤ 2 * m + 1 by omega) |> fun h => (show site L (2 * m + 1) = true from h)]
  unfold trunc truncate
  rw [decide_eq_false (show ¬ 2 * m + 1 ≤ 2 * m - 1 by omega)]
  simp

/-- **The survival table of `T L` is rule 30's with one row added.** For every width bound `W` and
time `t`, the rows of width at most `W` that pass every even check of depth `1` through `t` number
the same under `T L` as under rule 30, plus one exactly when `2 L - 1 ≤ W` and `2 ⌈W / 2⌉ ≤ t`. -/
theorem survival_table (L : Nat) (hL : 1 ≤ L) (W t : Nat) :
    cnt (2 ^ W) (fun Y => survT L (ofNat Y) t) =
      cnt (2 ^ W) (fun Y => survZ (ofNat Y) t) + (if 2 * L - 1 ≤ W ∧ 2 * ((W + 1) / 2) ≤ t then 1 else 0) := by
  by_cases hW : 2 * L - 1 ≤ W
  · have hm1 : L ≤ (W + 1) / 2 := by omega
    have huL : uN L < 2 ^ W :=
      Nat.lt_of_lt_of_le (uN_lt L hL) (Nat.pow_le_pow_right (by decide) (by omega))
    have hum : uN ((W + 1) / 2) < 2 ^ W :=
      Nat.lt_of_lt_of_le (uN_lt _ (by omega)) (Nat.pow_le_pow_right (by decide) (by omega))
    have hne : ∀ Y, Y < 2 ^ W → Y ≠ uN L → ¬ ∀ k, 1 ≤ k → ofNat Y k = trunc (2 * L - 1) k := by
      intro Y hY hY' h
      apply hY'
      rw [← toNat_ofNat hY, ← toNat_ofNat huL]
      apply toNat_congr
      intro k hk
      rw [h k hk, ofNat_uN L k hk]
    have hfin : ∀ Y, Y < 2 ^ W → Y ≠ uN L → Fin_ W (psiInv L (ofNat Y)) :=
      fun Y hY hY' => psiInv_fin L (ofNat_fin hY) (hne Y hY hY')
    let f : Nat → Nat := fun Y => if Y = uN L then uN ((W + 1) / 2) else toNat W (psiInv L (ofNat Y))
    have hf : ∀ i, i < 2 ^ W → f i < 2 ^ W := by
      intro i _
      simp only [f]
      split
      · exact hum
      · exact toNat_lt W _
    have key : ∀ Y, Y < 2 ^ W → Y ≠ uN L → toNat W (psiInv L (ofNat Y)) ≠ uN ((W + 1) / 2) := by
      intro Y hY hY' e
      have h1 : ∀ k, 1 ≤ k → psiInv L (ofNat Y) k = trunc (2 * ((W + 1) / 2) - 1) k := by
        intro k hk
        rw [← ofNat_toNat (hfin Y hY hY') k hk, e, ofNat_uN _ k hk]
      have h2 := psi_congr L h1 (2 * ((W + 1) / 2) + 1) (by omega)
      rw [psi_psiInv, psi_trunc_top L _ hm1, ofNat_fin hY _ (by omega)] at h2
      exact absurd h2 (by decide)
    have inj2 : ∀ Y Y', Y < 2 ^ W → Y' < 2 ^ W → Y ≠ uN L → Y' ≠ uN L →
        toNat W (psiInv L (ofNat Y)) = toNat W (psiInv L (ofNat Y')) → Y = Y' := by
      intro Y Y' hY hY' a b e
      have h1 : ∀ k, 1 ≤ k → psiInv L (ofNat Y) k = psiInv L (ofNat Y') k := by
        intro k hk
        rw [← ofNat_toNat (hfin Y hY a) k hk, ← ofNat_toNat (hfin Y' hY' b) k hk, e]
      have h2 : ∀ k, 1 ≤ k → ofNat Y k = ofNat Y' k := by
        intro k hk
        have := psi_congr L h1 k hk
        rwa [psi_psiInv, psi_psiInv] at this
      rw [← toNat_ofNat hY, ← toNat_ofNat hY', toNat_congr h2]
    have hinj : ∀ i j, i < 2 ^ W → j < 2 ^ W → f i = f j → i = j := by
      intro i j hi hj e
      simp only [f] at e
      by_cases a : i = uN L <;> by_cases b : j = uN L
      · rw [a, b]
      · rw [ite_eq_left a, ite_eq_right b] at e; exact absurd e.symm (key j hj b)
      · rw [ite_eq_right a, ite_eq_left b] at e; exact absurd e (key i hi a)
      · rw [ite_eq_right a, ite_eq_right b] at e; exact inj2 i j hi hj a b e
    have hpt : ∀ Y, Y < 2 ^ W → Y ≠ uN L → survT L (ofNat Y) t = survZ (ofNat (f Y)) t := by
      intro Y hY hY'
      simp only [f]
      rw [ite_eq_right hY', survT_eq L hL]
      exact survZ_congr (fun k hk => (ofNat_toNat (hfin Y hY hY') k hk).symm) t
    have hT0 : survT L (ofNat (uN L)) t = true := by
      rw [survT_eq L hL]
      have : ∀ k, 1 ≤ k → psiInv L (ofNat (uN L)) k = stripe k := by
        intro k hk
        rw [psiInv_congr L (y' := trunc (2 * L - 1)) (fun j hj => ofNat_uN L j hj) k hk, psiInv_trunc L k hk]
      rw [survZ_congr this, survZ_stripe]
    have hZ0 : survZ (ofNat (f (uN L))) t = decide (t < 2 * ((W + 1) / 2)) := by
      simp only [f, ite_true]
      rw [survZ_congr (fun k hk => ofNat_uN _ k hk), survZ_trunc _ (by omega)]
    have u := cnt_update (p := fun Y => survT L (ofNat Y) t) (q := fun Y => survZ (ofNat (f Y)) t)
      (uN L) huL (fun i hi hne' => hpt i hi hne')
    rw [hT0, hZ0] at u
    have hperm := cnt_perm (2 ^ W) f hf hinj (fun Y => survZ (ofNat Y) t)
    rw [hperm] at u
    by_cases ht : t < 2 * ((W + 1) / 2)
    · rw [decide_eq_true ht] at u
      rw [ite_eq_right (show ¬ (2 * L - 1 ≤ W ∧ 2 * ((W + 1) / 2) ≤ t) by omega)]
      simp at u; omega
    · rw [decide_eq_false ht] at u
      rw [ite_eq_left (show 2 * L - 1 ≤ W ∧ 2 * ((W + 1) / 2) ≤ t by omega)]
      simp at u; omega
  · rw [ite_eq_right (show ¬ (2 * L - 1 ≤ W ∧ 2 * ((W + 1) / 2) ≤ t) by omega), Nat.add_zero]
    apply cnt_congr
    intro Y hY
    rw [survT_eq L hL]
    apply survZ_congr
    intro k hk
    unfold psiInv
    by_cases hk2 : k ≤ 2 * L
    · rw [site_small L k hk2]; cases ofNat Y k <;> rfl
    · rw [← pf_psiInv]
      have hp : pf (psiInv L (ofNat Y)) k = false := by
        rcases Bool.eq_false_or_eq_true (pf (psiInv L (ofNat Y)) k) with h | h
        · exfalso
          have := (pf_iff _ k).1 h (2 * L - 1) (by omega) (by omega)
          unfold psiInv at this
          rw [site_small L _ (by omega), ofNat_fin hY _ (by omega), stripe_odd (by omega)] at this
          simp at this
        · exact h
      rw [hp]; cases site L k <;> cases ofNat Y k <;> rfl

end Rule30Submission
