module

public import Ruliology.CellularAutomata.Rule30ZeroBoundary

/-!
# The cone tip: a second derivative of the zero-boundary column

In the zero-boundary left half (`Rule30ZeroBoundary.zrow`), the cell at depth `1` and tick `t` is
a Boolean function of the start's cells at depths `1, …, t + 1`. This module computes its second
derivative in the two deepest directions that matter, for every row and every `t ≥ 2`.

Write `flip L d` for the row `L` with the cell at depth `d` flipped.

* `level_aff`: the cell at depth `k ≥ 1` and tick `s` depends on the start only through depths up
  to `k + s`, and on depth `k + s` with coefficient `1`.
* `diag`: if two rows differ only at depth `d`, the cells of level `d + 1` (depth plus tick) differ
  by the exclusive-or of the negated cells of level `d - 1` along the same anti-diagonal (`chain`).
* `cone_tip`: for every `t ≥ 2` and every row `L`,
  `zrow L t 1 + zrow (flip L t) t 1 + zrow (flip L (t-1)) t 1 + zrow (flip (flip L (t-1)) t) t 1`
  is `1` exactly when `t` is even. Flipping depth `t` changes the tip by `t` plus the `t - 1`
  cells of level `t - 1` (`diag`); each of those flips with depth `t - 1` (`level_aff`), while
  the wall cell at depth `0` stays white (`chain_flip`).
* `face_disagree`: for even `t`, every function whose second difference in the directions
  `t - 1` and `t` vanishes (every affine function in particular) disagrees with the tip somewhere
  on each such face of four rows. `tip_not_affine`: so for even `t ≥ 2` the tip is not affine.

The mechanism is the classical left-permutive derivative, as in
`Rule30Equivalents.AlgebraicDegree.deriv_evol_diag_succ` for the whole line; here it is carried
out in the row frame of the zero-boundary left half, with its white wall. Nothing here bears on
the single seed, and Problems 1 to 3 stay open.
-/

@[expose] public section

namespace Ruliology.CellularAutomata
namespace Rule30ConeTip

open Rule30ZeroBoundary

/-- The row `L` with the cell at depth `d` flipped. -/
def flip (L : Nat → Bool) (d : Nat) (k : Nat) : Bool := if k = d then !L k else L k

theorem flip_self (L : Nat → Bool) (d : Nat) : flip L d d = !L d := by
  unfold flip
  rw [ite_eq_left rfl]

theorem flip_ne (L : Nat → Bool) {d k : Nat} (h : k ≠ d) : flip L d k = L k := by
  unfold flip
  rw [ite_eq_right h]

theorem zrow_zero_succ (L : Nat → Bool) (k : Nat) : zrow L 0 (k + 1) = L (k + 1) := rfl

/-- **The newest depth enters with coefficient `1`.** If two rows agree at the depths from `1`
below `k + s`, then for `k ≥ 1` their cells at depth `k` and tick `s` differ exactly when the
rows differ at depth `k + s`. -/
theorem level_aff {L L' : Nat → Bool} :
    ∀ s k, 1 ≤ k → (∀ i, 1 ≤ i → i < k + s → L i = L' i) →
      xor (zrow L s k) (zrow L' s k) = xor (L (k + s)) (L' (k + s)) := by
  intro s
  induction s with
  | zero =>
    intro k hk _
    obtain ⟨k', rfl⟩ : ∃ k', k = k' + 1 := ⟨k - 1, by omega⟩
    rw [zrow_zero_succ, zrow_zero_succ]
  | succ s ih =>
    intro k hk h
    obtain ⟨k', rfl⟩ : ∃ k', k = k' + 1 := ⟨k - 1, by omega⟩
    rw [zrow_succ, zrow_succ]
    have e1 := ih (k' + 2) (by omega) (fun i hi1 hi2 => h i hi1 (by omega))
    have e2 : zrow L s (k' + 1) = zrow L' s (k' + 1) :=
      zrow_light_cone s (k' + 1) (fun i hi1 hi2 => h i hi1 (by omega))
    have e3 : zrow L s k' = zrow L' s k' :=
      zrow_light_cone s k' (fun i hi1 hi2 => h i hi1 (by omega))
    rw [e2, e3, show k' + 1 + (s + 1) = k' + 2 + s by omega, ← e1]
    generalize zrow L s (k' + 2) = p
    generalize zrow L' s (k' + 2) = q
    generalize (zrow L' s (k' + 1) || zrow L' s k') = r
    cases p <;> cases q <;> cases r <;> rfl

/-- The exclusive-or of the negated cells two levels back along an anti-diagonal: `chain L k s`
collects `!zrow L j (k + s - 2 - j)` for `j < s`. -/
def chain (L : Nat → Bool) : Nat → Nat → Bool
  | _, 0 => false
  | k, s + 1 => xor (chain L (k + 1) s) (!zrow L s (k - 1))

theorem chain_succ (L : Nat → Bool) (k s : Nat) :
    chain L k (s + 1) = xor (chain L (k + 1) s) (!zrow L s (k - 1)) := rfl

/-- **The derivative in one depth.** If `L` and `L'` differ only at depth `d ≥ 1`, then at every
cell of level `d + 1` the two runs differ by `chain`. -/
theorem diag {L L' : Nat → Bool} {d : Nat} (hd : 1 ≤ d) (hab : ∀ i, i ≠ d → L i = L' i)
    (hflip : xor (L d) (L' d) = true) :
    ∀ s k, 1 ≤ k → k + s = d + 1 → xor (zrow L s k) (zrow L' s k) = chain L k s := by
  intro s
  induction s with
  | zero =>
    intro k hk hks
    obtain ⟨k', rfl⟩ : ∃ k', k = k' + 1 := ⟨k - 1, by omega⟩
    rw [zrow_zero_succ, zrow_zero_succ, hab (k' + 1) (by omega)]
    show xor (L' (k' + 1)) (L' (k' + 1)) = false
    generalize L' (k' + 1) = x
    cases x <;> rfl
  | succ s ih =>
    intro k hk hks
    obtain ⟨k', rfl⟩ : ∃ k', k = k' + 1 := ⟨k - 1, by omega⟩
    rw [zrow_succ, zrow_succ, chain_succ, show k' + 1 - 1 = k' by omega]
    have e1 := ih (k' + 2) (by omega) (by omega)
    have e2 : xor (zrow L s (k' + 1)) (zrow L' s (k' + 1)) = true := by
      rw [level_aff s (k' + 1) (by omega) (fun i hi1 hi2 => hab i (by omega)),
        show k' + 1 + s = d by omega]
      exact hflip
    have e3 : zrow L s k' = zrow L' s k' :=
      zrow_light_cone s k' (fun i hi1 hi2 => hab i (by omega))
    rw [← e1, ← e3]
    revert e2
    generalize zrow L s (k' + 2) = p
    generalize zrow L' s (k' + 2) = q
    generalize zrow L s (k' + 1) = y
    generalize zrow L' s (k' + 1) = y'
    generalize zrow L s k' = z
    cases p <;> cases q <;> cases y <;> cases y' <;> cases z <;> decide

/-- **Flipping one level back flips every real cell of the chain.** If `M` and `M'` differ only at
depth `e ≥ 1`, then along level `e + 2` the chains differ by the number of their terms off the
wall, modulo `2`. -/
theorem chain_flip {M M' : Nat → Bool} {e : Nat} (hab : ∀ i, i ≠ e → M i = M' i)
    (hflip : xor (M e) (M' e) = true) :
    ∀ s k, 2 ≤ k → k + s = e + 2 → xor (chain M k s) (chain M' k s) = decide (s % 2 = 1) := by
  intro s
  induction s with
  | zero => intro k _ _; rfl
  | succ s ih =>
    intro k hk hks
    rw [chain_succ, chain_succ]
    have e1 := ih (k + 1) (by omega) (by omega)
    have e2 : xor (zrow M s (k - 1)) (zrow M' s (k - 1)) = true := by
      rw [level_aff s (k - 1) (by omega) (fun i hi1 hi2 => hab i (by omega)),
        show k - 1 + s = e by omega]
      exact hflip
    have key : xor (xor (chain M (k + 1) s) (!zrow M s (k - 1)))
        (xor (chain M' (k + 1) s) (!zrow M' s (k - 1))) =
        xor (xor (chain M (k + 1) s) (chain M' (k + 1) s)) true := by
      revert e2
      generalize zrow M s (k - 1) = y
      generalize zrow M' s (k - 1) = y'
      generalize chain M (k + 1) s = a
      generalize chain M' (k + 1) s = b
      cases a <;> cases b <;> cases y <;> cases y' <;> decide
    rw [key, e1]
    by_cases h : s % 2 = 1
    · rw [decide_eq_true h, decide_eq_false (by omega)]
      rfl
    · rw [decide_eq_false h, decide_eq_true (by omega)]
      rfl

theorem flip_only (L : Nat → Bool) (d : Nat) : ∀ i, i ≠ d → L i = flip L d i :=
  fun _ hi => (flip_ne L hi).symm

theorem flip_differs (L : Nat → Bool) (d : Nat) : xor (L d) (flip L d d) = true := by
  rw [flip_self]
  generalize L d = x
  cases x <;> rfl

/-- **The cone-tip law.** For every `t ≥ 2` and every row `L`, the second difference of the tip
`zrow L t 1` in the directions `t - 1` and `t` is `1` exactly when `t` is even. -/
theorem cone_tip (t : Nat) (ht : 2 ≤ t) (L : Nat → Bool) :
    xor (xor (zrow L t 1) (zrow (flip L t) t 1))
      (xor (zrow (flip L (t - 1)) t 1) (zrow (flip (flip L (t - 1)) t) t 1)) =
      decide (t % 2 = 0) := by
  have d1 := diag (L := L) (L' := flip L t) (d := t) (by omega) (flip_only L t) (flip_differs L t)
    t 1 (Nat.le_refl 1) (by omega)
  have d2 := diag (L := flip L (t - 1)) (L' := flip (flip L (t - 1)) t) (d := t) (by omega)
    (flip_only _ t) (flip_differs _ t) t 1 (Nat.le_refl 1) (by omega)
  rw [d1, d2]
  obtain ⟨u, rfl⟩ : ∃ u, t = u + 1 := ⟨t - 1, by omega⟩
  rw [chain_succ, chain_succ, show (1 : Nat) - 1 = 0 by rfl, zrow_wall, zrow_wall,
    show u + 1 - 1 = u by omega]
  have c := chain_flip (M := L) (M' := flip L u) (e := u) (flip_only L u)
    (flip_differs L u) u 2 (Nat.le_refl 2) (by omega)
  have key : xor (xor (chain L (1 + 1) u) (!false)) (xor (chain (flip L u) (1 + 1) u) (!false)) =
      xor (chain L 2 u) (chain (flip L u) 2 u) := by
    show xor (xor (chain L 2 u) true) (xor (chain (flip L u) 2 u) true) = _
    generalize chain L 2 u = a
    generalize chain (flip L u) 2 u = b
    cases a <;> cases b <;> rfl
  rw [key, c]
  exact decide_eq_decide.mpr (by omega)

/-- **Every vanishing-second-difference function misses the tip on every face**, for even `t`. -/
theorem face_disagree (t : Nat) (ht : 2 ≤ t) (heven : t % 2 = 0) (f : (Nat → Bool) → Bool)
    (hf : ∀ L, xor (xor (f L) (f (flip L t))) (xor (f (flip L (t - 1))) (f (flip (flip L (t - 1)) t)))
      = false) (L : Nat → Bool) :
    ∃ M, (M = L ∨ M = flip L t ∨ M = flip L (t - 1) ∨ M = flip (flip L (t - 1)) t) ∧
      zrow M t 1 ≠ f M := by
  have h1 := cone_tip t ht L
  rw [decide_eq_true heven] at h1
  have h2 := hf L
  by_cases a : zrow L t 1 = f L
  · by_cases b : zrow (flip L t) t 1 = f (flip L t)
    · by_cases c : zrow (flip L (t - 1)) t 1 = f (flip L (t - 1))
      · refine ⟨flip (flip L (t - 1)) t, Or.inr (Or.inr (Or.inr rfl)), fun d => ?_⟩
        rw [a, b, c, d] at h1
        rw [h1] at h2
        exact Bool.noConfusion h2
      · exact ⟨_, Or.inr (Or.inr (Or.inl rfl)), c⟩
    · exact ⟨_, Or.inr (Or.inl rfl), b⟩
  · exact ⟨L, Or.inl rfl, a⟩

/-- A function of the row is affine when it is a constant plus the exclusive-or of the cells at a
finite list of depths. -/
def affine (c : Bool) : List Nat → (Nat → Bool) → Bool
  | [], _ => c
  | d :: S, L => xor (L d) (affine c S L)

theorem affine_flip (c : Bool) (S : List Nat) (L : Nat → Bool) (d : Nat) :
    affine c S (flip L d) = xor (affine c S L) (decide (S.count d % 2 = 1)) := by
  induction S with
  | nil =>
    show c = xor c (decide (List.count d [] % 2 = 1))
    rw [List.count_nil]
    cases c <;> rfl
  | cons x S ih =>
    show xor (flip L d x) (affine c S (flip L d)) = xor (xor (L x) (affine c S L)) _
    rw [ih]
    by_cases hx : x = d
    · subst hx
      rw [flip_self, List.count_cons_self]
      have : decide ((S.count x + 1) % 2 = 1) = !decide (S.count x % 2 = 1) := by
        by_cases h : S.count x % 2 = 1
        · rw [decide_eq_true h, decide_eq_false (by omega)]; rfl
        · rw [decide_eq_false h, decide_eq_true (by omega)]; rfl
      rw [this]
      generalize affine c S L = A
      generalize decide (S.count x % 2 = 1) = B
      generalize L x = C
      cases A <;> cases B <;> cases C <;> rfl
    · rw [flip_ne L hx, List.count_cons_of_ne hx]
      generalize affine c S L = A
      generalize decide (S.count d % 2 = 1) = B
      generalize L x = C
      cases A <;> cases B <;> cases C <;> rfl

theorem affine_second (c : Bool) (S : List Nat) (L : Nat → Bool) (d e : Nat) :
    xor (xor (affine c S L) (affine c S (flip L d)))
      (xor (affine c S (flip L e)) (affine c S (flip (flip L e) d))) = false := by
  rw [affine_flip c S L d, affine_flip c S (flip L e) d, affine_flip c S L e]
  generalize affine c S L = A
  generalize decide (S.count d % 2 = 1) = B
  generalize decide (S.count e % 2 = 1) = C
  cases A <;> cases B <;> cases C <;> rfl

/-- **For even `t ≥ 2` the tip is not affine:** no constant plus an exclusive-or of finitely many
cells of the start equals `zrow L t 1` for every row `L`. -/
theorem tip_not_affine (t : Nat) (ht : 2 ≤ t) (heven : t % 2 = 0) (c : Bool) (S : List Nat) :
    ¬ ∀ L, zrow L t 1 = affine c S L := by
  intro h
  obtain ⟨M, -, hM⟩ := face_disagree t ht heven (affine c S)
    (fun L => affine_second c S L t (t - 1)) (fun _ => false)
  exact hM (h M)

end Rule30ConeTip
end Ruliology.CellularAutomata
