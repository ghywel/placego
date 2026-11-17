/-!
# The degree law for Rule 30: formal proof (complete, L1077)

`degree_law` (t ≥ 3: among sets of at least 2t − 1 cells, coefficient 1 exactly on the cells −t+2 … t),
`degree_bound` (t ≥ 2: every set of at least 2t cells has coefficient 0) and `degree_attained`.

**Known result, reproved here.** The kit's `equivalents/Rule30Equivalents/AlgebraicDegree.lean` (Mathlib) already
proves the degree law (`isGreatest_card_coef_center`, `eq_Icc_of_coef_ne_zero`); this file is an independent proof by
another route, not a submission.

Core Lean only (the Rule30PrizeKit is Mathlib-free). Rows are `Int → Bool`. The coefficient of the monomial
`∏_{j ∈ S} y_j` in the algebraic normal form of a row functional `F` is the XOR of `F` over all rows supported
in `S` (Möbius formula); `sumOver S F` computes it recursively by discrete derivatives.
-/

namespace Rule30DegreeLaw

/-! ## Rule 30 -/

/-- One step of Rule 30: `new i = x (i-1) XOR (x i OR x (i+1))`. -/
def step (x : Int → Bool) : Int → Bool := fun i => xor (x (i - 1)) (x i || x (i + 1))

/-- The row after `t` steps. -/
def evo : Nat → (Int → Bool) → (Int → Bool)
  | 0, x => x
  | t + 1, x => step (evo t x)

theorem evo_succ (t : Nat) (x : Int → Bool) (i : Int) :
    evo (t + 1) x i = xor (evo t x (i - 1)) (evo t x i || evo t x (i + 1)) := rfl

/-- Light cone: cell `p` after `k` steps depends only on initial cells in `[p - k, p + k]`. -/
theorem evo_cone (k : Nat) (x y : Int → Bool) (p : Int)
    (h : ∀ i, p - k ≤ i → i ≤ p + k → x i = y i) : evo k x p = evo k y p := by
  induction k generalizing p with
  | zero => exact h p (by omega) (by omega)
  | succ k ih =>
    rw [evo_succ, evo_succ]
    rw [ih (p - 1) (fun i h1 h2 => h i (by omega) (by omega)),
        ih p (fun i h1 h2 => h i (by omega) (by omega)),
        ih (p + 1) (fun i h1 h2 => h i (by omega) (by omega))]

/-! ## Setting one cell, independence, derivatives -/

/-- The row `x` with cell `j` set to `b`. -/
def setCell (x : Int → Bool) (j : Int) (b : Bool) : Int → Bool := fun i => if i = j then b else x i

theorem setCell_same (x : Int → Bool) (j : Int) (b : Bool) : setCell x j b j = b := by
  simp [setCell]

theorem setCell_other (x : Int → Bool) (j i : Int) (b : Bool) (h : i ≠ j) : setCell x j b i = x i := by
  simp [setCell, h]

theorem setCell_setCell (x : Int → Bool) (j : Int) (a b : Bool) :
    setCell (setCell x j a) j b = setCell x j b := by
  funext i; by_cases h : i = j <;> simp [setCell, h]

theorem setCell_comm (x : Int → Bool) (j k : Int) (a b : Bool) (h : j ≠ k) :
    setCell (setCell x j a) k b = setCell (setCell x k b) j a := by
  funext i
  by_cases hk : i = k
  · subst hk; simp [setCell, Ne.symm h]
  · by_cases hj : i = j
    · subst hj; simp [setCell, hk]
    · simp [setCell, hk, hj]

/-- `F` does not read cell `j`. -/
def Indep (F : (Int → Bool) → Bool) (j : Int) : Prop := ∀ x b, F (setCell x j b) = F x

/-- Discrete derivative in cell `j`. -/
def deriv (j : Int) (F : (Int → Bool) → Bool) : (Int → Bool) → Bool :=
  fun x => xor (F (setCell x j true)) (F (setCell x j false))

theorem deriv_indep_self (j : Int) (F : (Int → Bool) → Bool) : Indep (deriv j F) j := by
  intro x b; simp [deriv, setCell_setCell]

theorem deriv_of_indep {F : (Int → Bool) → Bool} {j : Int} (h : Indep F j) (x : Int → Bool) :
    deriv j F x = false := by
  simp only [deriv]; rw [h x true, h x false]; cases F x <;> rfl

theorem indep_deriv {F : (Int → Bool) → Bool} {j k : Int} (h : Indep F k) (hjk : j ≠ k) :
    Indep (deriv j F) k := by
  intro x b
  simp only [deriv]
  rw [setCell_comm x k j b true (Ne.symm hjk), setCell_comm x k j b false (Ne.symm hjk), h, h]

theorem deriv_comm (j k : Int) (F : (Int → Bool) → Bool) (x : Int → Bool) :
    deriv j (deriv k F) x = deriv k (deriv j F) x := by
  by_cases h : j = k
  · subst h; rfl
  · simp only [deriv]
    rw [setCell_comm x j k true true h, setCell_comm x j k true false h,
        setCell_comm x j k false true h, setCell_comm x j k false false h]
    cases F (setCell (setCell x k true) j true) <;> cases F (setCell (setCell x k false) j true) <;>
      cases F (setCell (setCell x k true) j false) <;> cases F (setCell (setCell x k false) j false) <;> rfl

theorem deriv_xor (j : Int) (F G : (Int → Bool) → Bool) (x : Int → Bool) :
    deriv j (fun y => xor (F y) (G y)) x = xor (deriv j F x) (deriv j G x) := by
  simp only [deriv]
  cases F (setCell x j true) <;> cases F (setCell x j false) <;>
    cases G (setCell x j true) <;> cases G (setCell x j false) <;> rfl

/-- A functional of the form `x j XOR G x` with `G` not reading `j` has derivative `true` in `j`. -/
theorem deriv_linear {F G : (Int → Bool) → Bool} {j : Int} (hG : Indep G j)
    (hF : ∀ x, F x = xor (x j) (G x)) (x : Int → Bool) : deriv j F x = true := by
  simp only [deriv, hF, setCell_same]
  rw [hG x true, hG x false]
  cases G x <;> rfl

/-! ## XOR-sums over rows supported in a list of cells -/

/-- XOR of `F` over all rows whose black cells lie in `S` (the ANF coefficient of `∏_{j∈S} y_j`). -/
def sumOver : List Int → ((Int → Bool) → Bool) → Bool
  | [], F => F (fun _ => false)
  | j :: js, F => sumOver js (deriv j F)

theorem sumOver_congr (S : List Int) {F G : (Int → Bool) → Bool} (h : ∀ x, F x = G x) :
    sumOver S F = sumOver S G := by
  have : F = G := funext h
  rw [this]

theorem sumOver_xor (S : List Int) (F G : (Int → Bool) → Bool) :
    sumOver S (fun y => xor (F y) (G y)) = xor (sumOver S F) (sumOver S G) := by
  induction S generalizing F G with
  | nil => rfl
  | cons j js ih =>
    simp only [sumOver]
    rw [sumOver_congr js (deriv_xor j F G)]
    exact ih (deriv j F) (deriv j G)

theorem sumOver_false (S : List Int) : sumOver S (fun _ => false) = false := by
  induction S with
  | nil => rfl
  | cons j js ih =>
    simp only [sumOver]
    rw [sumOver_congr js (fun x => deriv_of_indep (F := fun _ => false) (j := j) (fun _ _ => rfl) x)]
    exact ih

/-- Swapping the first two cells does not change the sum. -/
theorem sumOver_swap (j k : Int) (S : List Int) (F : (Int → Bool) → Bool) :
    sumOver (j :: k :: S) F = sumOver (k :: j :: S) F := by
  simp only [sumOver]
  exact sumOver_congr S (fun x => (deriv_comm k j F x))

/-- Pull any listed cell to the front. -/
theorem sumOver_pull (S : List Int) (j : Int) (hj : j ∈ S) (F : (Int → Bool) → Bool) :
    ∃ T, (∀ i, i ∈ T → i ∈ S) ∧ sumOver S F = sumOver T (deriv j F) := by
  induction S generalizing F with
  | nil => cases hj
  | cons a S ih =>
    by_cases ha : j = a
    · subst ha; exact ⟨S, fun i hi => List.mem_cons_of_mem _ hi, rfl⟩
    · have hjS : j ∈ S := by
        cases hj with
        | head => exact absurd rfl ha
        | tail _ h => exact h
      obtain ⟨T, hT, hsum⟩ := ih hjS (deriv a F)
      refine ⟨a :: T, ?_, ?_⟩
      · intro i hi
        cases hi with
        | head => exact List.mem_cons_self
        | tail _ h => exact List.mem_cons_of_mem _ (hT i h)
      · simp only [sumOver] at hsum ⊢
        rw [hsum]
        exact sumOver_congr T (fun x => deriv_comm j a F x)

/-- If `F` ignores a listed cell, its sum vanishes. -/
theorem sumOver_indep (S : List Int) (j : Int) (hj : j ∈ S) (F : (Int → Bool) → Bool)
    (h : Indep F j) : sumOver S F = false := by
  obtain ⟨T, -, hsum⟩ := sumOver_pull S j hj F
  rw [hsum, sumOver_congr T (deriv_of_indep h)]
  exact sumOver_false T

/-! ## Lemma 1: the derivative in the rightmost cell is a white anti-diagonal -/

theorem xor_false_iff (a b : Bool) : xor a b = false ↔ a = b := by
  cases a <;> cases b <;> decide

/-- `aw t x k`: through time `k`, the anti-diagonal ahead of cell `t` (cells `t - 1 - k'` at times `k' < k`)
is white. -/
def aw (t : Nat) (x : Int → Bool) : Nat → Bool
  | 0 => true
  | k + 1 => aw t x k && !(evo k x ((t : Int) - 1 - k))

/-- Cells left of `t` at time `k` (within the cone) do not see cell `t`. -/
theorem evo_setCell_left (t : Nat) (x : Int → Bool) (b : Bool) (k : Nat) (p : Int)
    (hp : p + k < t) : evo k (setCell x t b) p = evo k x p := by
  apply evo_cone
  intro i _ h2
  exact setCell_other x t i b (by omega)

/-- The damage invariant for a flip of cell `t`. -/
theorem damage (t : Nat) (x : Int → Bool) (k : Nat) (hk : k ≤ t) :
    ∀ p : Int, p ≤ (t : Int) - k →
      xor (evo k (setCell x t true) p) (evo k (setCell x t false) p)
        = (decide (p = (t : Int) - k) && aw t x k) := by
  induction k with
  | zero =>
    intro p hp
    simp only [evo, aw, Bool.and_true]
    by_cases h : p = (t : Int)
    · subst h; simp [setCell]
    · simp [setCell, h]
  | succ k ih =>
    intro p hp
    have ih' := ih (by omega)
    have d1 := ih' (p - 1) (by omega)
    have d2 := ih' p (by omega)
    have d3 := ih' (p + 1) (by omega)
    have e1 : decide (p - 1 = (t : Int) - k) = false := by simp; omega
    have e2 : decide (p = (t : Int) - k) = false := by simp; omega
    rw [e1, Bool.false_and, xor_false_iff] at d1
    rw [e2, Bool.false_and, xor_false_iff] at d2
    rw [evo_succ, evo_succ, d1, d2]
    simp only [aw]
    by_cases hpe : p = (t : Int) - (k + 1 : Nat)
    · -- the front: p + 1 = t - k, and p is the anti-diagonal cell at time k
      have h3 : decide (p + 1 = (t : Int) - k) = true := by simp; omega
      have h0 : decide (p = (t : Int) - (k + 1 : Nat)) = true := by simp; omega
      rw [h3, Bool.true_and] at d3
      have ek : evo k (setCell x t false) p = evo k x ((t : Int) - 1 - k) := by
        rw [evo_setCell_left t x false k p (by omega)]
        congr 1; omega
      rw [h0, Bool.true_and, ek]
      revert d3
      generalize evo k (setCell x t true) (p + 1) = c1
      generalize evo k (setCell x t false) (p + 1) = c0
      generalize evo k (setCell x t false) (p - 1) = a
      generalize evo k x ((t : Int) - 1 - k) = e
      generalize aw t x k = w
      cases c1 <;> cases c0 <;> cases a <;> cases e <;> cases w <;> decide
    · -- strictly behind the front: no damage
      have h3 : decide (p + 1 = (t : Int) - k) = false := by simp; omega
      have h0 : decide (p = (t : Int) - (k + 1 : Nat)) = false := by simp; omega
      rw [h3, Bool.false_and, xor_false_iff] at d3
      rw [d3, h0, Bool.false_and]
      generalize evo k (setCell x t false) (p + 1) = c
      generalize evo k (setCell x t false) p = b
      generalize evo k (setCell x t false) (p - 1) = a
      cases a <;> cases b <;> cases c <;> decide

/-- **Lemma 1.** The derivative of the apex `evo t · 0` in the rightmost cell `t` is the indicator that the
anti-diagonal `x_k(t-1-k)`, `k < t`, is white. -/
theorem deriv_apex (t : Nat) (x : Int → Bool) :
    deriv (t : Int) (fun y => evo t y 0) x = aw t x t := by
  have h := damage t x t (Nat.le_refl t) 0 (by omega)
  simp only [deriv]
  rw [h]
  simp

/-! ## Left permutivity: the leftmost cone input enters by exact XOR -/

/-- A flip of cell `j` damages, at time `k`, exactly the cell `j + k` among cells `≥ j + k`. -/
theorem right_damage (j : Int) (x : Int → Bool) (k : Nat) :
    ∀ q : Int, j + k ≤ q →
      xor (evo k (setCell x j true) q) (evo k (setCell x j false) q) = decide (q = j + k) := by
  induction k with
  | zero =>
    intro q hq
    simp only [evo]
    by_cases h : q = j
    · subst h; simp [setCell]
    · simp [setCell, h]
  | succ k ih =>
    intro q hq
    have d1 := ih (q - 1) (by omega)
    have d2 := ih q (by omega)
    have d3 := ih (q + 1) (by omega)
    have e2 : decide (q = j + k) = false := by simp; omega
    have e3 : decide (q + 1 = j + k) = false := by simp; omega
    rw [e2, xor_false_iff] at d2
    rw [e3, xor_false_iff] at d3
    have e1 : decide (q - 1 = j + k) = decide (q = j + (k + 1 : Nat)) := by
      by_cases h : q = j + (k + 1 : Nat)
      · rw [decide_eq_true h]; simp; omega
      · rw [decide_eq_false h]; simp; omega
    rw [e1] at d1
    rw [evo_succ, evo_succ, d2, d3]
    revert d1
    generalize evo k (setCell x j true) (q - 1) = a1
    generalize evo k (setCell x j false) (q - 1) = a0
    generalize decide (q = j + (k + 1 : Nat)) = r
    generalize evo k (setCell x j false) q = b
    generalize evo k (setCell x j false) (q + 1) = c
    cases a1 <;> cases a0 <;> cases r <;> cases b <;> cases c <;> decide

theorem setCell_self (x : Int → Bool) (j : Int) : setCell x j (x j) = x := by
  funext i; by_cases h : i = j
  · subst h; simp [setCell]
  · simp [setCell, h]

/-- **Left permutivity.** `evo k x (j + k) = x j XOR (the same cell with cell j cleared)`. -/
theorem left_permutive (j : Int) (k : Nat) (x : Int → Bool) :
    evo k x (j + k) = xor (x j) (evo k (setCell x j false) (j + k)) := by
  have d := right_damage j x k (j + k) (Int.le_refl _)
  rw [decide_eq_true rfl] at d
  cases hx : x j
  · rw [← setCell_self x j, hx]; simp [setCell_setCell]
  · have : evo k x (j + k) = evo k (setCell x j true) (j + k) := by rw [← hx, setCell_self]
    rw [this]
    revert d
    cases evo k (setCell x j true) (j + k) <;> cases evo k (setCell x j false) (j + k) <;> decide

/-! ## The pivot derivative -/

/-- Eliminating a pivot: if `g` and `R` do not read `p`, then `∂_p ((¬(x p ⊕ g x)) ∧ R x) = R x`. -/
theorem deriv_pivot {g R : (Int → Bool) → Bool} {p : Int} (hg : Indep g p) (hR : Indep R p)
    (x : Int → Bool) : deriv p (fun y => !(xor (y p) (g y)) && R y) x = R x := by
  simp only [deriv, setCell_same]
  rw [hg x true, hg x false, hR x true, hR x false]
  cases g x <;> cases R x <;> rfl

/-- A functional that reads only cells in `[lo, hi]` is independent of every cell outside. -/
def ReadsIn (F : (Int → Bool) → Bool) (lo hi : Int) : Prop :=
  ∀ x y : Int → Bool, (∀ i, lo ≤ i → i ≤ hi → x i = y i) → F x = F y

theorem ReadsIn.indep {F : (Int → Bool) → Bool} {lo hi j : Int} (h : ReadsIn F lo hi)
    (hj : j < lo ∨ hi < j) : Indep F j := by
  intro x b
  apply h
  intro i h1 h2
  exact setCell_other x j i b (by omega)

theorem evo_readsIn (k : Nat) (p : Int) : ReadsIn (fun x => evo k x p) (p - k) (p + k) :=
  fun x y h => evo_cone k x y p h

/-! ## Triangular elimination of the anti-diagonal pivots -/

/-- The pivot of the `k`-th anti-diagonal cell: its leftmost input `t - 1 - 2k`. -/
def piv (t k : Nat) : Int := (t : Int) - 1 - 2 * (k : Int)

/-- The anti-diagonal cell ahead of a flip of `t`, at time `k`. -/
def ad (t k : Nat) (x : Int → Bool) : Bool := evo k x ((t : Int) - 1 - k)

/-- The anti-diagonal cell with its pivot cleared. -/
def adRest (t k : Nat) (x : Int → Bool) : Bool := evo k (setCell x (piv t k) false) ((t : Int) - 1 - k)

theorem ad_decomp (t k : Nat) (x : Int → Bool) : ad t k x = xor (x (piv t k)) (adRest t k x) := by
  have h := left_permutive (piv t k) k x
  have hp : piv t k + (k : Int) = (t : Int) - 1 - k := by simp [piv]; omega
  rw [hp] at h
  exact h

theorem adRest_indep_piv (t k : Nat) : Indep (adRest t k) (piv t k) := by
  intro x b; simp [adRest, setCell_setCell]

/-- The anti-diagonal cell at time `k` reads only cells in `[piv t k, t - 1]`. -/
theorem ad_readsIn (t k : Nat) : ReadsIn (ad t k) (piv t k) ((t : Int) - 1) := by
  intro x y h
  apply evo_cone
  intro i h1 h2
  exact h i (by simp [piv]; omega) (by omega)

theorem aw_succ_eq (t k : Nat) (x : Int → Bool) : aw t x (k + 1) = (aw t x k && !(ad t k x)) := rfl

/-- The product of the first `k` white conditions reads only cells in `[t + 1 - 2k, t - 1]`. -/
theorem aw_readsIn (t k : Nat) : ReadsIn (fun x => aw t x k) ((t : Int) + 1 - 2 * (k : Int)) ((t : Int) - 1) := by
  induction k with
  | zero => intro x y _; rfl
  | succ k ih =>
    intro x y h
    have h1 : aw t x k = aw t y k := ih x y (fun i h1 h2 => h i (by omega) h2)
    have h2 : ad t k x = ad t k y := ad_readsIn t k x y (fun i h1 h2 => h i (by simp [piv] at h1; omega) h2)
    show (aw t x k && !(ad t k x)) = (aw t y k && !(ad t k y))
    rw [h1, h2]

/-- One elimination step: `∂_{piv t k} (aw t · (k+1)) = aw t · k`. -/
theorem deriv_aw_step (t k : Nat) (x : Int → Bool) :
    deriv (piv t k) (fun y => aw t y (k + 1)) x = aw t x k := by
  have hR : Indep (fun y => aw t y k) (piv t k) :=
    (aw_readsIn t k).indep (by simp [piv]; omega)
  have heq : (fun y => aw t y (k + 1)) = (fun y => !(xor (y (piv t k)) (adRest t k y)) && aw t y k) := by
    funext y; rw [aw_succ_eq, ad_decomp, Bool.and_comm]
  rw [heq]
  exact deriv_pivot (adRest_indep_piv t k) hR x

/-- The pivots `piv t (m+n-1), …, piv t m`, leftmost first. -/
def pivRange (t m : Nat) : Nat → List Int
  | 0 => []
  | n + 1 => piv t (m + n) :: pivRange t m n

/-- **Elimination.** Summing out the pivots `piv t (m+n-1), …, piv t m` (leftmost first) turns the product of
the first `m + n` white conditions into the product of the first `m`. -/
theorem sumOver_elim (t m n : Nat) (L : List Int) :
    sumOver (pivRange t m n ++ L) (fun x => aw t x (m + n)) = sumOver L (fun x => aw t x m) := by
  induction n with
  | zero => rfl
  | succ n ih =>
    simp only [pivRange, List.cons_append, sumOver]
    exact (sumOver_congr _ (fun x => deriv_aw_step t (m + n) x)).trans ih

theorem sumOver_true_cons (j : Int) (L : List Int) : sumOver (j :: L) (fun _ => true) = false := by
  simp only [sumOver]
  rw [sumOver_congr L (fun x => deriv_of_indep (F := fun _ => true) (j := j) (fun _ _ => rfl) x)]
  exact sumOver_false L

/-! ## Permutation invariance -/

theorem sumOver_perm {L₁ L₂ : List Int} (h : L₁.Perm L₂) (F : (Int → Bool) → Bool) :
    sumOver L₁ F = sumOver L₂ F := by
  induction h generalizing F with
  | nil => rfl
  | cons x _ ih => simp only [sumOver]; exact ih _
  | swap x y l => exact sumOver_swap y x l F
  | trans _ _ ih1 ih2 => exact (ih1 F).trans (ih2 F)

/-! ## Coefficient lemmas -/

/-- The apex functional `x ↦ evo t x 0`. -/
def apex (t : Nat) : (Int → Bool) → Bool := fun x => evo t x 0

theorem sumOver_erase (S : List Int) (j : Int) (hj : j ∈ S) (F : (Int → Bool) → Bool) :
    sumOver S F = sumOver (S.erase j) (deriv j F) := by
  rw [sumOver_perm (List.perm_cons_erase hj) F]
  rfl

theorem sumOver_true_ne_nil (L : List Int) (hL : L ≠ []) : sumOver L (fun _ => true) = false := by
  cases L with
  | nil => exact absurd rfl hL
  | cons j L => exact sumOver_true_cons j L

/-- A functional linear in cell `j` (`x j XOR g`, `g` not reading `j`), summed over a list containing `j` and at
least one other cell, gives `false`. -/
theorem sumOver_linear (S : List Int) (j : Int) (hj : j ∈ S) (hS : S.erase j ≠ [])
    {F G : (Int → Bool) → Bool} (hG : Indep G j) (hF : ∀ x, F x = xor (x j) (G x)) :
    sumOver S F = false := by
  rw [sumOver_erase S j hj F, sumOver_congr _ (deriv_linear hG hF)]
  exact sumOver_true_ne_nil _ hS

/-- **(A)** The apex is linear in its leftmost input `-t`. -/
theorem apex_linear_left (t : Nat) (x : Int → Bool) :
    apex t x = xor (x (-(t : Int))) (evo t (setCell x (-(t : Int)) false) 0) := by
  have h := left_permutive (-(t : Int)) t x
  have hp : -(t : Int) + (t : Int) = 0 := by omega
  rw [hp] at h
  exact h

theorem coeff_with_left_cell (t : Nat) (S : List Int) (hj : -(t : Int) ∈ S) (hS : S.erase (-(t : Int)) ≠ []) :
    sumOver S (apex t) = false :=
  sumOver_linear S _ hj hS (G := fun x => evo t (setCell x (-(t : Int)) false) 0)
    (fun x b => by simp only [setCell_setCell]) (apex_linear_left t)

/-- **(B)** For a monomial containing the rightmost cell `t`, the coefficient is the sum of the white
anti-diagonal over the remaining cells. -/
theorem coeff_with_right_cell (t : Nat) (S : List Int) (hj : (t : Int) ∈ S) :
    sumOver S (apex t) = sumOver (S.erase (t : Int)) (fun x => aw t x t) := by
  rw [sumOver_erase S _ hj]
  exact sumOver_congr _ (deriv_apex t)

/-- **(C1)** If the remaining cells are all `t` pivots plus a nonempty list, the coefficient vanishes. -/
theorem coeff_all_pivots (t : Nat) (T L : List Int) (hT : T.Perm (pivRange t 0 t ++ L)) (hL : L ≠ []) :
    sumOver T (fun x => aw t x t) = false := by
  rw [sumOver_perm hT]
  have h := sumOver_elim t 0 t L
  rw [Nat.zero_add] at h
  rw [h]
  exact sumOver_true_ne_nil L hL

/-- **(C2)** If pivot `piv t m` is missing but the pivots left of it are present, and some listed cell lies
strictly left of `piv t m`, the coefficient vanishes. -/
theorem coeff_missing_pivot (t m : Nat) (hm : m + 1 ≤ t) (T L : List Int)
    (hT : T.Perm (pivRange t (m + 1) (t - (m + 1)) ++ L)) (f : Int) (hf : f ∈ L) (hfl : f < piv t m) :
    sumOver T (fun x => aw t x t) = false := by
  rw [sumOver_perm hT]
  have h := sumOver_elim t (m + 1) (t - (m + 1)) L
  have ht : m + 1 + (t - (m + 1)) = t := by omega
  rw [ht] at h
  rw [h]
  apply sumOver_indep L f hf
  apply (aw_readsIn t (m + 1)).indep
  left; simp [piv] at hfl; omega

/-- Product rule against a factor that ignores the cell. -/
theorem deriv_and_indep (j : Int) {F G : (Int → Bool) → Bool} (hG : Indep G j) (x : Int → Bool) :
    deriv j (fun y => F y && G y) x = (deriv j F x && G x) := by
  simp only [deriv]
  rw [hG x true, hG x false]
  cases F (setCell x j true) <;> cases F (setCell x j false) <;> cases G x <;> rfl

/-- Linearity of a cone cell in its leftmost input, at an arbitrary apex. -/
theorem evo_linear (k : Nat) (j p : Int) (hp : j + k = p) (x : Int → Bool) :
    evo k x p = xor (x j) (evo k (setCell x j false) p) := by
  have h := left_permutive j k x
  rw [hp] at h; exact h

theorem indep_clear (k : Nat) (j p : Int) : Indep (fun x => evo k (setCell x j false) p) j := by
  intro x b; simp only [setCell_setCell]

/-- **(D)** The monomial over `[-t+1, t-1]` (here `t = s + 1`, no `t` and no `-t`) has coefficient 0. -/
theorem coeff_without_ends (s : Nat) (hs : 1 ≤ s) (S : List Int)
    (h1 : -(s : Int) ∈ S) (h2 : -(s : Int) + 1 ∈ S) (h3 : (s : Int) ∈ S) :
    sumOver S (apex (s + 1)) = false := by
  have hsplit : ∀ x, apex (s + 1) x =
      xor (xor (evo s x (-1)) (xor (evo s x 0) (evo s x 1))) (evo s x 0 && evo s x 1) := by
    intro x
    show evo (s + 1) x 0 = _
    rw [evo_succ]
    have e1 : (0 : Int) - 1 = -1 := by omega
    have e2 : (0 : Int) + 1 = 1 := by omega
    rw [e1, e2]
    cases evo s x (-1) <;> cases evo s x 0 <;> cases evo s x 1 <;> rfl
  rw [sumOver_congr S hsplit, sumOver_xor, sumOver_xor, sumOver_xor]
  -- h = evo s · (-1) ignores the listed cell s
  have hh : sumOver S (fun x => evo s x (-1)) = false :=
    sumOver_indep S _ h3 _ ((evo_readsIn s (-1)).indep (by omega))
  -- u = evo s · 0 is linear in -s
  have hne : S.erase (-(s : Int)) ≠ [] := by
    intro h
    have : (s : Int) ∈ S.erase (-(s : Int)) := (List.mem_erase_of_ne (by omega)).2 h3
    rw [h] at this; cases this
  have hu : sumOver S (fun x => evo s x 0) = false :=
    sumOver_linear S _ h1 hne (indep_clear s _ 0) (evo_linear s _ 0 (by omega))
  -- v = evo s · 1 ignores the listed cell -s
  have hv : sumOver S (fun x => evo s x 1) = false :=
    sumOver_indep S _ h1 _ ((evo_readsIn s 1).indep (by omega))
  -- u ∧ v: differentiate in -s, then v is linear in -s + 1
  have huv : sumOver S (fun x => evo s x 0 && evo s x 1) = false := by
    rw [sumOver_erase S _ h1]
    have hvI : Indep (fun x => evo s x 1) (-(s : Int)) := (evo_readsIn s 1).indep (by omega)
    rw [sumOver_congr _ (fun x => deriv_and_indep (-(s : Int)) (F := fun y => evo s y 0) hvI x)]
    rw [sumOver_congr _ (fun x => by
      rw [deriv_linear (indep_clear s (-(s : Int)) 0) (evo_linear s _ 0 (by omega)) x, Bool.true_and])]
    have h2' : -(s : Int) + 1 ∈ S.erase (-(s : Int)) := (List.mem_erase_of_ne (by omega)).2 h2
    have hne' : (S.erase (-(s : Int))).erase (-(s : Int) + 1) ≠ [] := by
      intro h
      have : (s : Int) ∈ (S.erase (-(s : Int))).erase (-(s : Int) + 1) :=
        (List.mem_erase_of_ne (by omega)).2 ((List.mem_erase_of_ne (by omega)).2 h3)
      rw [h] at this; cases this
    exact sumOver_linear _ _ h2' hne' (indep_clear s _ 1) (evo_linear s _ 1 (by omega))
  rw [hh, hu, hv, huv]; rfl

/-! ## (E) preparation: XOR accumulators, damage behind the front, shifts -/

/-- `xorUpTo f k = f 0 ⊕ f 1 ⊕ ⋯ ⊕ f (k-1)`. -/
def xorUpTo (f : Nat → Bool) : Nat → Bool
  | 0 => false
  | k + 1 => xor (xorUpTo f k) (f k)

theorem and_xorUpTo (a : Bool) (f : Nat → Bool) (k : Nat) :
    (a && xorUpTo f k) = xorUpTo (fun i => a && f i) k := by
  induction k with
  | zero => cases a <;> rfl
  | succ k ih =>
    simp only [xorUpTo]; rw [← ih]
    cases a <;> cases xorUpTo f k <;> cases f k <;> rfl

theorem deriv_xorUpTo (j : Int) (G : Nat → (Int → Bool) → Bool) (k : Nat) (x : Int → Bool) :
    deriv j (fun y => xorUpTo (fun i => G i y) k) x = xorUpTo (fun i => deriv j (G i) x) k := by
  induction k with
  | zero => simp [deriv, xorUpTo]
  | succ k ih =>
    simp only [xorUpTo]
    rw [deriv_xor j (fun y => xorUpTo (fun i => G i y) k) (G k) x, ih]

theorem sumOver_xorUpTo (S : List Int) (G : Nat → (Int → Bool) → Bool) (k : Nat) :
    sumOver S (fun y => xorUpTo (fun i => G i y) k) = xorUpTo (fun i => sumOver S (G i)) k := by
  induction k with
  | zero => exact sumOver_false S
  | succ k ih =>
    simp only [xorUpTo]
    rw [sumOver_xor S (fun y => xorUpTo (fun i => G i y) k) (G k), ih]

theorem deriv_not (j : Int) (F : (Int → Bool) → Bool) (x : Int → Bool) :
    deriv j (fun y => !(F y)) x = deriv j F x := by
  simp only [deriv]; cases F (setCell x j true) <;> cases F (setCell x j false) <;> rfl

theorem deriv_indep_and (j : Int) {R F : (Int → Bool) → Bool} (hR : Indep R j) (x : Int → Bool) :
    deriv j (fun y => R y && F y) x = (R x && deriv j F x) := by
  simp only [deriv]; rw [hR x true, hR x false]
  cases R x <;> cases F (setCell x j true) <;> cases F (setCell x j false) <;> rfl

/-- Two factors linear in the same cell combine: `∂_p (R ∧ ¬(x_p ⊕ g) ∧ (x_p ⊕ h)) = R ∧ (g ⊕ h)`. -/
theorem deriv_two_linear {R g h : (Int → Bool) → Bool} {p : Int} (hR : Indep R p) (hg : Indep g p)
    (hh : Indep h p) (x : Int → Bool) :
    deriv p (fun y => (R y && !(xor (y p) (g y))) && xor (y p) (h y)) x = (R x && xor (g x) (h x)) := by
  simp only [deriv, setCell_same]
  rw [hR x true, hR x false, hg x true, hg x false, hh x true, hh x false]
  cases R x <;> cases g x <;> cases h x <;> rfl

/-- **Damage behind the front.** Flipping cell `q` changes the cell just behind the light-speed front at time
`k` by the XOR of the NOTs of the cells just ahead of the front at earlier times. -/
theorem behind_front (q : Int) (x : Int → Bool) (k : Nat) :
    deriv q (fun y => evo k y (q + k - 1)) x = xorUpTo (fun i => !(evo i x (q + 1 + i))) k := by
  induction k with
  | zero =>
    simp only [deriv, evo, xorUpTo]
    have h : q + ((0 : Nat) : Int) - 1 ≠ q := by omega
    rw [setCell_other x q _ true h, setCell_other x q _ false h]
    cases x (q + ((0 : Nat) : Int) - 1) <;> rfl
  | succ k ih =>
    have hpos : q + ((k + 1 : Nat) : Int) - 1 = q + k := by omega
    simp only [deriv] at ih ⊢
    rw [hpos, evo_succ, evo_succ]
    have hb := right_damage q x k (q + k) (Int.le_refl _)
    rw [decide_eq_true rfl] at hb
    have hc := right_damage q x k (q + k + 1) (by omega)
    rw [decide_eq_false (by omega), xor_false_iff] at hc
    have hc0 : evo k (setCell x q false) (q + k + 1) = evo k x (q + 1 + k) := by
      have e : q + 1 + (k : Int) = q + k + 1 := by omega
      rw [e]; apply evo_cone; intro i h1 _; exact setCell_other x q i false (by omega)
    have hm : q + (k : Int) - 1 = q + ((k : Nat) : Int) - 1 := rfl
    simp only [xorUpTo]
    rw [← ih, hc, hc0]
    revert hb
    generalize evo k (setCell x q true) (q + k) = b1
    generalize evo k (setCell x q false) (q + k) = b0
    generalize evo k (setCell x q true) (q + k - 1) = a1
    generalize evo k (setCell x q false) (q + k - 1) = a0
    generalize evo k x (q + 1 + k) = c
    cases b1 <;> cases b0 <;> cases a1 <;> cases a0 <;> cases c <;> decide

/-- Shift a row one cell to the right. -/
def shiftR (y : Int → Bool) : Int → Bool := fun j => y (j - 1)

theorem evo_shift (k : Nat) (y : Int → Bool) (p : Int) : evo k (shiftR y) (p + 1) = evo k y p := by
  induction k generalizing p with
  | zero => simp [evo, shiftR]
  | succ k ih =>
    rw [evo_succ, evo_succ]
    have e1 : p + 1 - 1 = (p - 1) + 1 := by omega
    have e2 : p + 1 + 1 = (p + 1) + 1 := rfl
    rw [e1, ih (p - 1), ih p, ih (p + 1)]

theorem setCell_shift (y : Int → Bool) (j : Int) (b : Bool) :
    setCell (shiftR y) (j + 1) b = shiftR (setCell y j b) := by
  funext i
  simp only [setCell, shiftR]
  by_cases h : i = j + 1
  · simp [h]
  · have h' : ¬ (i - 1 = j) := by omega
    simp [h, h']

theorem shiftR_white : shiftR (fun _ => false) = (fun _ => false) := rfl

/-- Translation of sums. -/
theorem sumOver_shift (S : List Int) (F : (Int → Bool) → Bool) :
    sumOver (S.map (· + 1)) F = sumOver S (fun y => F (shiftR y)) := by
  induction S generalizing F with
  | nil => rfl
  | cons a S ih =>
    simp only [List.map_cons, sumOver]
    rw [ih]
    apply sumOver_congr
    intro y
    simp only [deriv]
    rw [setCell_shift, setCell_shift]

/-- Clearing a cell outside the summed list changes nothing. -/
theorem sumOver_clear (S : List Int) (j : Int) (hj : j ∉ S) (F : (Int → Bool) → Bool) :
    sumOver S F = sumOver S (fun x => F (setCell x j false)) := by
  induction S generalizing F with
  | nil =>
    simp only [sumOver]
    congr 1; funext i; by_cases h : i = j <;> simp [setCell, h]
  | cons a S ih =>
    have haj : a ≠ j := fun h => hj (h ▸ List.mem_cons_self)
    have hjS : j ∉ S := fun h => hj (List.mem_cons_of_mem _ h)
    simp only [sumOver]
    rw [ih hjS]
    apply sumOver_congr
    intro x
    simp only [deriv]
    rw [setCell_comm x a j true false haj, setCell_comm x a j false false haj]

/-! ## (E) the families A and B -/

/-- The cells `[-t+2, t-1]`, listed as: leftmost free cell, leftmost pivot, then the instance `t-1` list shifted
one cell right. -/
def T0 : Nat → List Int
  | 0 => []
  | 1 => []
  | 2 => [0, 1]
  | n + 3 => (-(n : Int) - 1) :: (-(n : Int)) :: (T0 (n + 2)).map (· + 1)

theorem mem_T0 (n : Nat) (i : Int) : i ∈ T0 (n + 2) ↔ (-(n : Int) ≤ i ∧ i ≤ (n : Int) + 1) := by
  induction n generalizing i with
  | zero =>
    simp only [T0, List.mem_cons, List.not_mem_nil, or_false]
    omega
  | succ n ih =>
    show i ∈ (-(n : Int) - 1) :: (-(n : Int)) :: (T0 (n + 2)).map (· + 1) ↔ _
    simp only [List.mem_cons, List.mem_map]
    constructor
    · rintro (h | h | ⟨a, ha, rfl⟩)
      · omega
      · omega
      · have := (ih a).1 ha; omega
    · intro h
      by_cases h1 : i = -(n : Int) - 1
      · exact Or.inl h1
      · by_cases h2 : i = -(n : Int)
        · exact Or.inr (Or.inl h2)
        · exact Or.inr (Or.inr ⟨i - 1, (ih (i - 1)).2 (by omega), by omega⟩)

/-- The main quantity: the coefficient over `[-s+2, s-1]` of the white anti-diagonal. -/
def A (s : Nat) : Bool := sumOver (T0 s) (fun y => aw s y s)

/-- The companion quantity along the speed-2 line from the cell `-s+1`. -/
def B (s i : Nat) : Bool := sumOver (T0 s) (fun y => aw s y (s - 1) && evo i y (-(s : Int) + 1 + i))

theorem aw_shift (s n : Nat) (y : Int → Bool) : aw (s + 1) (shiftR y) n = aw s y n := by
  induction n with
  | zero => rfl
  | succ n ih =>
    simp only [aw]
    rw [ih]
    have e : ((s + 1 : Nat) : Int) - 1 - (n : Int) = ((s : Int) - 1 - n) + 1 := by omega
    rw [e, evo_shift]

theorem B_zero (m : Nat) : B (m + 2) 0 = false := by
  unfold B
  have hj : (-((m + 2 : Nat) : Int) + 1 + ((0 : Nat) : Int)) ∉ T0 (m + 2) := by
    intro h; have := (mem_T0 m _).1 h; omega
  rw [sumOver_clear _ _ hj]
  rw [sumOver_congr _ (fun x => by
    show (aw (m + 2) (setCell x _ false) (m + 2 - 1) && evo 0 (setCell x _ false) _) = false
    simp only [evo, setCell_same, Bool.and_false])]
  exact sumOver_false _

/-! ## (E) the recursions -/

theorem piv_m (m : Nat) : piv (m + 3) (m + 1) = -(m : Int) := by simp [piv]; omega

theorem mem_R_left (m : Nat) : -(m : Int) + 1 ∈ (T0 (m + 2)).map (· + 1) :=
  List.mem_map.2 ⟨-(m : Int), (mem_T0 m _).2 (by omega), rfl⟩

theorem p_not_mem_R (m : Nat) : -(m : Int) ∉ (T0 (m + 2)).map (· + 1) := by
  intro h
  obtain ⟨a, ha, hae⟩ := List.mem_map.1 h
  have := (mem_T0 m a).1 ha
  omega

/-- The bare anti-diagonal product of instance `m+2` up to `m+1` sums to zero over `T0 (m+2)`. -/
theorem sum_aw_prev_zero (m : Nat) : sumOver (T0 (m + 2)) (fun y => aw (m + 2) y (m + 1)) = false :=
  sumOver_indep _ (-(m : Int)) ((mem_T0 m _).2 (by omega)) _
    ((aw_readsIn (m + 2) (m + 1)).indep (by omega))

/-- `A (m+2)` in terms of the last condition. -/
theorem A_as_last (m : Nat) :
    A (m + 2) = sumOver (T0 (m + 2)) (fun y => aw (m + 2) y (m + 1) && evo (m + 1) y 0) := by
  unfold A
  have h : (fun y => aw (m + 2) y (m + 2)) =
      (fun y => xor (aw (m + 2) y (m + 1)) (aw (m + 2) y (m + 1) && evo (m + 1) y 0)) := by
    funext y
    rw [aw_succ_eq]
    have e : ad (m + 2) (m + 1) y = evo (m + 1) y 0 := by
      unfold ad; congr 1; omega
    rw [e]; cases aw (m + 2) y (m + 1) <;> cases evo (m + 1) y 0 <;> rfl
  rw [h, sumOver_xor, sum_aw_prev_zero, Bool.false_xor]

/-- The inner term: peeling the leftmost pivot from one summand. -/
theorem core_term (m i : Nat) :
    sumOver ((T0 (m + 2)).map (· + 1))
      (deriv (-(m : Int)) (fun x => aw (m + 3) x (m + 2) && !(evo i x (-(m : Int) - 1 + 1 + i))))
      = xor (A (m + 2)) (B (m + 2) i) := by
  have hpos : -(m : Int) - 1 + 1 + (i : Int) = -(m : Int) + i := by omega
  rw [hpos]
  have hsplit : (fun x => aw (m + 3) x (m + 2) && !(evo i x (-(m : Int) + i))) =
      (fun x => xor (aw (m + 3) x (m + 2)) (aw (m + 3) x (m + 2) && evo i x (-(m : Int) + i))) := by
    funext x; cases aw (m + 3) x (m + 2) <;> cases evo i x (-(m : Int) + i) <;> rfl
  rw [hsplit, sumOver_congr _ (deriv_xor _ _ _), sumOver_xor]
  -- part 1: the bare product
  have hp1 : sumOver ((T0 (m + 2)).map (· + 1)) (deriv (-(m : Int)) (fun x => aw (m + 3) x (m + 2))) = false := by
    rw [← piv_m m, sumOver_congr _ (deriv_aw_step (m + 3) (m + 1))]
    exact sumOver_indep _ _ (mem_R_left m) _ ((aw_readsIn (m + 3) (m + 1)).indep (by omega))
  rw [hp1, Bool.false_xor]
  -- part 2: two factors linear in the pivot
  have hfun : (fun x => aw (m + 3) x (m + 2) && evo i x (-(m : Int) + i)) =
      (fun x => (aw (m + 3) x (m + 1) && !(xor (x (-(m : Int))) (adRest (m + 3) (m + 1) x))) &&
        xor (x (-(m : Int))) (evo i (setCell x (-(m : Int)) false) (-(m : Int) + i))) := by
    funext x
    rw [aw_succ_eq, ad_decomp, piv_m, evo_linear i (-(m : Int)) (-(m : Int) + i) rfl x]
  have hRI : Indep (fun x => aw (m + 3) x (m + 1)) (-(m : Int)) :=
    (aw_readsIn (m + 3) (m + 1)).indep (by omega)
  have hgI : Indep (adRest (m + 3) (m + 1)) (-(m : Int)) := by
    have := adRest_indep_piv (m + 3) (m + 1); rw [piv_m] at this; exact this
  rw [hfun, sumOver_congr _ (deriv_two_linear hRI hgI (indep_clear i (-(m : Int)) (-(m : Int) + i)))]
  have hsplit2 : (fun x => aw (m + 3) x (m + 1) &&
      xor (adRest (m + 3) (m + 1) x) (evo i (setCell x (-(m : Int)) false) (-(m : Int) + i))) =
      (fun x => xor (aw (m + 3) x (m + 1) && adRest (m + 3) (m + 1) x)
        (aw (m + 3) x (m + 1) && evo i (setCell x (-(m : Int)) false) (-(m : Int) + i))) := by
    funext x
    cases aw (m + 3) x (m + 1) <;> cases adRest (m + 3) (m + 1) x <;>
      cases evo i (setCell x (-(m : Int)) false) (-(m : Int) + i) <;> rfl
  rw [hsplit2, sumOver_xor]
  have hRI' : ∀ x b, aw (m + 3) (setCell x (-(m : Int)) b) (m + 1) = aw (m + 3) x (m + 1) := fun x b => hRI x b
  congr 1
  · -- 2a: the A part
    have hc : (fun x => aw (m + 3) x (m + 1) && adRest (m + 3) (m + 1) x) =
        (fun x => aw (m + 3) (setCell x (-(m : Int)) false) (m + 1) &&
          ad (m + 3) (m + 1) (setCell x (-(m : Int)) false)) := by
      funext x
      rw [hRI' x false]
      congr 1
      unfold adRest ad; rw [piv_m]
    have hclear := sumOver_clear ((T0 (m + 2)).map (· + 1)) (-(m : Int)) (p_not_mem_R m)
      (fun z => aw (m + 3) z (m + 1) && ad (m + 3) (m + 1) z)
    rw [hc, ← hclear, sumOver_shift, A_as_last]
    apply sumOver_congr
    intro y
    rw [aw_shift]
    congr 1
    unfold ad
    have e : ((m + 3 : Nat) : Int) - 1 - ((m + 1 : Nat) : Int) = 0 + 1 := by omega
    rw [e, evo_shift]
  · -- 2b: the B part
    have hc : (fun x => aw (m + 3) x (m + 1) && evo i (setCell x (-(m : Int)) false) (-(m : Int) + i)) =
        (fun x => aw (m + 3) (setCell x (-(m : Int)) false) (m + 1) &&
          evo i (setCell x (-(m : Int)) false) (-(m : Int) + i)) := by
      funext x
      rw [hRI' x false]
    have hclear := sumOver_clear ((T0 (m + 2)).map (· + 1)) (-(m : Int)) (p_not_mem_R m)
      (fun z => aw (m + 3) z (m + 1) && evo i z (-(m : Int) + i))
    rw [hc, ← hclear, sumOver_shift]
    unfold B
    apply sumOver_congr
    intro y
    rw [aw_shift]
    have e : -(m : Int) + (i : Int) = (-((m + 2 : Nat) : Int) + 1 + i) + 1 := by omega
    rw [e, evo_shift]
    rfl

/-- Differentiating the first two layers: after the leftmost free cell, a product against any cell on the
line `-(m+3)+1+k` becomes a XOR over the right diagonal. -/
theorem deriv_first (m k : Nat) :
    deriv (-(m : Int) - 1) (fun y => aw (m + 3) y (m + 2) && evo k y (-(m : Int) - 1 + k - 1)) =
      (fun x => xorUpTo (fun i => aw (m + 3) x (m + 2) && !(evo i x (-(m : Int) - 1 + 1 + i))) k) := by
  funext x
  have hR : Indep (fun y => aw (m + 3) y (m + 2)) (-(m : Int) - 1) :=
    (aw_readsIn (m + 3) (m + 2)).indep (by omega)
  rw [deriv_indep_and _ hR, behind_front, and_xorUpTo]

/-- **Recursion for A.** -/
theorem recA (m : Nat) : A (m + 3) = xorUpTo (fun i => xor (A (m + 2)) (B (m + 2) i)) (m + 2) := by
  show sumOver ((-(m : Int) - 1) :: (-(m : Int)) :: (T0 (m + 2)).map (· + 1)) (fun y => aw (m + 3) y (m + 3)) = _
  simp only [sumOver]
  have hfun : (fun y => aw (m + 3) y (m + 3)) =
      (fun y => aw (m + 3) y (m + 2) && !(evo (m + 2) y (-(m : Int) - 1 + ((m + 2 : Nat) : Int) - 1))) := by
    funext y
    rw [aw_succ_eq]
    congr 2
    unfold ad; congr 1; omega
  have hR : Indep (fun y => aw (m + 3) y (m + 2)) (-(m : Int) - 1) :=
    (aw_readsIn (m + 3) (m + 2)).indep (by omega)
  have hq : deriv (-(m : Int) - 1) (fun y => aw (m + 3) y (m + 3)) =
      (fun x => xorUpTo (fun i => aw (m + 3) x (m + 2) && !(evo i x (-(m : Int) - 1 + 1 + i))) (m + 2)) := by
    funext x
    rw [hfun, deriv_indep_and _ hR, deriv_not, behind_front, and_xorUpTo]
  rw [hq]
  rw [sumOver_congr _ (deriv_xorUpTo (-(m : Int))
    (fun i y => aw (m + 3) y (m + 2) && !(evo i y (-(m : Int) - 1 + 1 + i))) (m + 2))]
  rw [sumOver_xorUpTo _ (fun i => deriv (-(m : Int))
    (fun y => aw (m + 3) y (m + 2) && !(evo i y (-(m : Int) - 1 + 1 + i)))) (m + 2)]
  congr 1
  funext i
  exact core_term m i

/-- **Recursion for B.** -/
theorem recB (m k : Nat) : B (m + 3) k = xorUpTo (fun i => xor (A (m + 2)) (B (m + 2) i)) k := by
  show sumOver ((-(m : Int) - 1) :: (-(m : Int)) :: (T0 (m + 2)).map (· + 1))
    (fun y => aw (m + 3) y (m + 2) && evo k y (-((m + 3 : Nat) : Int) + 1 + k)) = _
  simp only [sumOver]
  have hpos : (fun y => aw (m + 3) y (m + 2) && evo k y (-((m + 3 : Nat) : Int) + 1 + k)) =
      (fun y => aw (m + 3) y (m + 2) && evo k y (-(m : Int) - 1 + k - 1)) := by
    funext y; congr 2; omega
  rw [hpos, deriv_first]
  rw [sumOver_congr _ (deriv_xorUpTo (-(m : Int))
    (fun i y => aw (m + 3) y (m + 2) && !(evo i y (-(m : Int) - 1 + 1 + i))) k)]
  rw [sumOver_xorUpTo _ (fun i => deriv (-(m : Int))
    (fun y => aw (m + 3) y (m + 2) && !(evo i y (-(m : Int) - 1 + 1 + i)))) k]
  congr 1
  funext i
  exact core_term m i

theorem A_two : A 2 = true := by decide
theorem B_two_one : B 2 1 = true := by decide

theorem xorUpTo_first (f : Nat → Bool) (h0 : f 0 = true) :
    ∀ k, 1 ≤ k → (∀ i, 1 ≤ i → i < k → f i = false) → xorUpTo f k = true := by
  intro k
  induction k with
  | zero => intro h; exact absurd h (by omega)
  | succ k ih =>
    intro _ hf
    simp only [xorUpTo]
    by_cases hk : k = 0
    · subst hk; simp [xorUpTo, h0]
    · rw [ih (by omega) (fun i h1 h2 => hf i h1 (by omega)), hf k (by omega) (by omega)]; rfl

/-- **The joint induction.** -/
theorem AB_true (m : Nat) : A (m + 2) = true ∧ ∀ i, 1 ≤ i → i ≤ m + 1 → B (m + 2) i = true := by
  induction m with
  | zero =>
    refine ⟨A_two, fun i h1 h2 => ?_⟩
    have : i = 1 := by omega
    subst this; exact B_two_one
  | succ m ih =>
    obtain ⟨hA, hB⟩ := ih
    have h0 : xor (A (m + 2)) (B (m + 2) 0) = true := by rw [hA, B_zero]; rfl
    have hi : ∀ i, 1 ≤ i → i ≤ m + 1 → xor (A (m + 2)) (B (m + 2) i) = false := by
      intro i h1 h2; rw [hA, hB i h1 h2]; rfl
    refine ⟨?_, fun k h1 h2 => ?_⟩
    · rw [recA]
      exact xorUpTo_first _ h0 (m + 2) (by omega) (fun i h1 h2 => hi i h1 (by omega))
    · rw [recB]
      exact xorUpTo_first _ h0 k h1 (fun i h1' h2' => hi i h1' (by omega))

/-- **(E) The main parity.** For every `t ≥ 2`, the white anti-diagonal summed over `[-t+2, t-1]` is odd. -/
theorem main_parity (t : Nat) (ht : 2 ≤ t) : A t = true := by
  obtain ⟨m, rfl⟩ : ∃ m, t = m + 2 := ⟨t - 2, by omega⟩
  exact (AB_true m).1

/-! ## (F) Assembly: list tools -/

theorem nodup_map_inj {α β : Type} {f : α → β} (hf : ∀ a b, f a = f b → a = b) :
    ∀ l : List α, l.Nodup → (l.map f).Nodup
  | [], _ => List.nodup_nil
  | a :: l, h => by
    rw [List.nodup_cons] at h
    rw [List.map_cons, List.nodup_cons]
    refine ⟨?_, nodup_map_inj hf l h.2⟩
    intro hm
    obtain ⟨b, hb, hfb⟩ := List.mem_map.1 hm
    exact h.1 (hf b a hfb ▸ hb)

theorem nodup_filter (p : Int → Bool) : ∀ l : List Int, l.Nodup → (l.filter p).Nodup
  | [], _ => List.nodup_nil
  | a :: l, h => by
    rw [List.nodup_cons] at h
    rw [List.filter_cons]
    split
    · rw [List.nodup_cons]
      exact ⟨fun hm => h.1 (List.mem_filter.1 hm).1, nodup_filter p l h.2⟩
    · exact nodup_filter p l h.2

/-- The integers `lo, lo+1, …, lo+n-1`. -/
def intList (lo : Int) (n : Nat) : List Int := (List.range n).map (fun k : Nat => lo + (k : Int))

theorem mem_intList (lo : Int) (n : Nat) (i : Int) : i ∈ intList lo n ↔ lo ≤ i ∧ i < lo + n := by
  unfold intList
  rw [List.mem_map]
  constructor
  · rintro ⟨k, hk, rfl⟩; rw [List.mem_range] at hk; omega
  · intro h; exact ⟨(i - lo).toNat, List.mem_range.2 (by omega), by omega⟩

theorem length_intList (lo : Int) (n : Nat) : (intList lo n).length = n := by
  simp [intList]

theorem nodup_intList (lo : Int) (n : Nat) : (intList lo n).Nodup :=
  nodup_map_inj (fun a b h => by omega) _ List.nodup_range

/-- A Nodup list inside `U` is no longer than `U`. -/
theorem length_le_of_sub : ∀ (T U : List Int), T.Nodup → (∀ a ∈ T, a ∈ U) → T.length ≤ U.length
  | [], _, _, _ => Nat.zero_le _
  | a :: T, U, hT, hs => by
    rw [List.nodup_cons] at hT
    have haU : a ∈ U := hs a List.mem_cons_self
    have ih := length_le_of_sub T (U.erase a) hT.2 (fun b hb => by
      have hba : b ≠ a := fun h => hT.1 (h ▸ hb)
      exact (List.mem_erase_of_ne hba).2 (hs b (List.mem_cons_of_mem _ hb)))
    rw [List.length_erase_of_mem haU] at ih
    have : 0 < U.length := List.length_pos_of_mem haU
    simp only [List.length_cons]; omega

/-- A Nodup list inside `U` of at least `U`'s length contains all of `U`. -/
theorem all_mem_of_length (T U : List Int) (hT : T.Nodup) (hsub : ∀ a ∈ T, a ∈ U)
    (hlen : U.length ≤ T.length) : ∀ a ∈ U, a ∈ T := by
  intro a ha
  by_cases hm : a ∈ T
  · exact hm
  · exfalso
    have h := length_le_of_sub T (U.erase a) hT (fun b hb => by
      have hba : b ≠ a := fun h => hm (h ▸ hb)
      exact (List.mem_erase_of_ne hba).2 (hsub b hb))
    rw [List.length_erase_of_mem ha] at h
    have : 0 < U.length := List.length_pos_of_mem ha
    omega

/-- If a Nodup list inside `U` falls short of `U` by at most one and misses `c`, it contains every other member. -/
theorem all_but_one (T U : List Int) (hT : T.Nodup) (hsub : ∀ a ∈ T, a ∈ U) (c : Int) (hc : c ∈ U)
    (hcT : c ∉ T) (hlen : U.length ≤ T.length + 1) : ∀ a ∈ U, a ≠ c → a ∈ T := by
  intro a ha hac
  have h := all_mem_of_length T (U.erase c) hT (fun b hb => by
      have hbc : b ≠ c := fun h => hcT (h ▸ hb)
      exact (List.mem_erase_of_ne hbc).2 (hsub b hb))
    (by rw [List.length_erase_of_mem hc]; omega)
  exact h a ((List.mem_erase_of_ne hac).2 ha)

theorem mem_pivRange (t m n : Nat) (i : Int) :
    i ∈ pivRange t m n ↔ ∃ k, m ≤ k ∧ k < m + n ∧ i = piv t k := by
  induction n with
  | zero =>
    simp only [pivRange, List.not_mem_nil, false_iff]
    rintro ⟨k, h1, h2, _⟩; omega
  | succ n ih =>
    simp only [pivRange, List.mem_cons]
    rw [ih]
    constructor
    · rintro (h | ⟨k, h1, h2, h3⟩)
      · exact ⟨m + n, by omega, by omega, h⟩
      · exact ⟨k, h1, by omega, h3⟩
    · rintro ⟨k, h1, h2, h3⟩
      by_cases hk : k = m + n
      · subst hk; exact Or.inl h3
      · exact Or.inr ⟨k, h1, by omega, h3⟩

theorem nodup_pivRange (t m n : Nat) : (pivRange t m n).Nodup := by
  induction n with
  | zero => exact List.nodup_nil
  | succ n ih =>
    simp only [pivRange]
    rw [List.nodup_cons]
    refine ⟨fun h => ?_, ih⟩
    obtain ⟨k, _, h2, h3⟩ := (mem_pivRange t m n _).1 h
    simp only [piv] at h3; omega

/-- Split a Nodup list into a listed Nodup part and the rest. -/
theorem perm_split (T P : List Int) (hT : T.Nodup) (hP : P.Nodup) (hPT : ∀ a ∈ P, a ∈ T) :
    T.Perm (P ++ T.filter (fun i => !decide (i ∈ P))) := by
  have hnd : (P ++ T.filter (fun i => !decide (i ∈ P))).Nodup := by
    rw [List.nodup_append]
    refine ⟨hP, nodup_filter _ T hT, ?_⟩
    intro a ha b hb hab
    subst hab
    have := (List.mem_filter.1 hb).2
    simp [ha] at this
  rw [List.perm_ext_iff_of_nodup hT hnd]
  intro a
  rw [List.mem_append, List.mem_filter]
  constructor
  · intro ha
    by_cases hp : a ∈ P
    · exact Or.inl hp
    · exact Or.inr ⟨ha, by simp [hp]⟩
  · rintro (h | ⟨h, _⟩)
    · exact hPT a h
    · exact h

theorem mem_split_rest (T P : List Int) (f : Int) (hf : f ∈ T) (hfP : f ∉ P) :
    f ∈ T.filter (fun i => !decide (i ∈ P)) :=
  List.mem_filter.2 ⟨hf, by simp [hfP]⟩

theorem nodup_T0 (n : Nat) : (T0 (n + 2)).Nodup := by
  induction n with
  | zero => decide
  | succ n ih =>
    show ((-(n : Int) - 1) :: (-(n : Int)) :: (T0 (n + 2)).map (· + 1)).Nodup
    rw [List.nodup_cons, List.nodup_cons]
    refine ⟨?_, ?_, nodup_map_inj (fun a b h => by omega) _ ih⟩
    · intro h
      rcases List.mem_cons.1 h with h | h
      · omega
      · obtain ⟨a, ha, hae⟩ := List.mem_map.1 h
        have := (mem_T0 n a).1 ha; omega
    · intro h
      obtain ⟨a, ha, hae⟩ := List.mem_map.1 h
      have := (mem_T0 n a).1 ha; omega

/-! ## (F) The headline theorems -/

/-- **Top monomial.** For `t ≥ 2`, the monomial over the cells `-t+2 … t` has coefficient 1. -/
theorem coeff_top (t : Nat) (ht : 2 ≤ t) (S : List Int) (hnd : S.Nodup)
    (hmem : ∀ i, i ∈ S ↔ (-(t : Int) + 2 ≤ i ∧ i ≤ t)) : sumOver S (apex t) = true := by
  obtain ⟨m, rfl⟩ : ∃ m, t = m + 2 := ⟨t - 2, by omega⟩
  have htS : ((m + 2 : Nat) : Int) ∈ S := (hmem _).2 (by omega)
  rw [coeff_with_right_cell _ S htS]
  have hperm : (S.erase ((m + 2 : Nat) : Int)).Perm (T0 (m + 2)) := by
    rw [List.perm_ext_iff_of_nodup (hnd.erase _) (nodup_T0 m)]
    intro a
    rw [mem_T0, List.Nodup.mem_erase_iff hnd, hmem]
    omega
  rw [sumOver_perm hperm]
  exact main_parity (m + 2) ht

/-- **Outside the light cone.** A monomial containing a cell outside `[-t, t]` has coefficient 0. -/
theorem coeff_outside (t : Nat) (S : List Int) (j : Int) (hj : j ∈ S)
    (hout : j < -(t : Int) ∨ (t : Int) < j) : sumOver S (apex t) = false :=
  sumOver_indep S j hj _ ((evo_readsIn t 0).indep (by omega))

/-- **Every other monomial of high degree.** For `t ≥ 3`, a set of at least `2t - 1` cells of the light cone that
contains a cell left of `-t+2` (i.e. is not the top monomial) has coefficient 0. -/
theorem coeff_not_top (t : Nat) (ht : 3 ≤ t) (S : List Int) (hnd : S.Nodup)
    (hsub : ∀ i ∈ S, -(t : Int) ≤ i ∧ i ≤ t) (hlen : 2 * t - 1 ≤ S.length)
    (hlow : ∃ i ∈ S, i < -(t : Int) + 2) : sumOver S (apex t) = false := by
  by_cases hneg : -(t : Int) ∈ S
  · -- (A) the leftmost cell with another cell
    apply coeff_with_left_cell t S hneg
    intro h
    have := List.length_erase_of_mem hneg
    rw [h] at this; simp at this; omega
  · obtain ⟨i0, hi0, hi0l⟩ := hlow
    have hi0b := hsub i0 hi0
    have hm1 : -(t : Int) + 1 ∈ S := by
      have : i0 = -(t : Int) + 1 := by
        by_cases h : i0 = -(t : Int)
        · exact absurd (h ▸ hi0) hneg
        · omega
      exact this ▸ hi0
    by_cases htS : (t : Int) ∈ S
    · -- the monomial contains t: reduce to the white anti-diagonal over T = S \ {t}
      rw [coeff_with_right_cell t S htS]
      have hTnd : (S.erase (t : Int)).Nodup := hnd.erase _
      have hTmem : ∀ a, a ∈ S.erase (t : Int) ↔ a ≠ (t : Int) ∧ a ∈ S := fun a => List.Nodup.mem_erase_iff hnd
      let U := intList (-(t : Int) + 1) (2 * t - 1)
      have hU : ∀ a, a ∈ U ↔ (-(t : Int) + 1 ≤ a ∧ a ≤ (t : Int) - 1) := by
        intro a; rw [mem_intList]; omega
      have hTsub : ∀ a ∈ S.erase (t : Int), a ∈ U := by
        intro a ha
        obtain ⟨h1, h2⟩ := (hTmem a).1 ha
        have := hsub a h2
        have hna : a ≠ -(t : Int) := fun h => hneg (h ▸ h2)
        exact (hU a).2 (by omega)
      have hTlen : U.length ≤ (S.erase (t : Int)).length + 1 := by
        rw [length_intList, List.length_erase_of_mem htS]; omega
      have hpivU : ∀ k, k < t → piv t k ∈ U := fun k hk => (hU _).2 (by simp only [piv]; omega)
      by_cases hmiss : ∃ c, c ∈ U ∧ c ∉ S.erase (t : Int)
      · obtain ⟨c, hcU, hcT⟩ := hmiss
        have hoth := all_but_one _ U hTnd hTsub c hcU hcT hTlen
        have hc1 : c ≠ -(t : Int) + 1 := by
          intro h; subst h
          exact hcT ((hTmem _).2 ⟨by omega, hm1⟩)
        have hcb := (hU c).1 hcU
        by_cases hpar : ∃ k, k < t ∧ c = piv t k
        · -- (C2) a missing pivot `piv t m`, `m ≤ t - 2`
          obtain ⟨m, hm, hcm⟩ := hpar
          have hmt : m + 2 ≤ t := by
            have : m ≠ t - 1 := by
              intro h; subst h; simp only [piv] at hcm; omega
            omega
          let P := pivRange t (m + 1) (t - (m + 1))
          have hPT : ∀ a ∈ P, a ∈ S.erase (t : Int) := by
            intro a ha
            obtain ⟨k, h1, h2, h3⟩ := (mem_pivRange t (m + 1) (t - (m + 1)) a).1 ha
            exact hoth a (h3 ▸ hpivU k (by omega)) (by subst h3; rw [hcm]; simp only [piv]; omega)
          have hperm := perm_split _ P hTnd (nodup_pivRange _ _ _) hPT
          apply coeff_missing_pivot t m (by omega) _ _ hperm (c - 1)
          · apply mem_split_rest
            · exact hoth (c - 1) ((hU _).2 (by rw [hcm]; simp only [piv]; omega)) (by omega)
            · intro h
              obtain ⟨k, h1, h2, h3⟩ := (mem_pivRange t (m + 1) (t - (m + 1)) _).1 h
              rw [hcm] at h3; simp only [piv] at h3; omega
          · rw [← hcm]; omega
        · -- (C1) a missing free cell: every pivot is present
          have hnp : ∀ k, k < t → piv t k ≠ c := fun k hk h => hpar ⟨k, hk, h.symm⟩
          let P := pivRange t 0 t
          have hPT : ∀ a ∈ P, a ∈ S.erase (t : Int) := by
            intro a ha
            obtain ⟨k, h1, h2, h3⟩ := (mem_pivRange t 0 t a).1 ha
            exact hoth a (h3 ▸ hpivU k (by omega)) (h3 ▸ hnp k (by omega))
          have hperm := perm_split _ P hTnd (nodup_pivRange _ _ _) hPT
          apply coeff_all_pivots t _ _ hperm
          -- a free cell other than c survives: t - 2 or t - 4
          have hfree : ∃ f, f ∈ U ∧ f ≠ c ∧ ∀ k, k < t → piv t k ≠ f := by
            by_cases hc2 : c = (t : Int) - 2
            · exact ⟨(t : Int) - 4, (hU _).2 (by omega), by omega, fun k _ h => by simp only [piv] at h; omega⟩
            · exact ⟨(t : Int) - 2, (hU _).2 (by omega), fun h => hc2 h.symm, fun k _ h => by simp only [piv] at h; omega⟩
          obtain ⟨f, hfU, hfc, hfp⟩ := hfree
          intro hnil
          have hmem := mem_split_rest _ P f (hoth f hfU hfc) (fun h => by
            obtain ⟨k, h1, h2, h3⟩ := (mem_pivRange t 0 t f).1 h
            exact hfp k (by omega) h3.symm)
          rw [hnil] at hmem; cases hmem
      · -- (C1) nothing missing: every pivot and the free cell t - 2 are present
        have hall : ∀ a ∈ U, a ∈ S.erase (t : Int) := by
          intro a ha
          by_cases h : a ∈ S.erase (t : Int)
          · exact h
          · exact absurd ⟨a, ha, h⟩ hmiss
        let P := pivRange t 0 t
        have hPT : ∀ a ∈ P, a ∈ S.erase (t : Int) := by
          intro a ha
          obtain ⟨k, h1, h2, h3⟩ := (mem_pivRange t 0 t a).1 ha
          exact hall a (h3 ▸ hpivU k (by omega))
        have hperm := perm_split _ P hTnd (nodup_pivRange _ _ _) hPT
        apply coeff_all_pivots t _ _ hperm
        intro hnil
        have hmem := mem_split_rest _ P ((t : Int) - 2) (hall _ ((hU _).2 (by omega))) (fun h => by
          obtain ⟨k, h1, h2, h3⟩ := (mem_pivRange t 0 t _).1 h
          simp only [piv] at h3; omega)
        rw [hnil] at hmem; cases hmem
    · -- (D) neither end: S is all of [-t+1, t-1]
      obtain ⟨s, rfl⟩ : ∃ s, t = s + 1 := ⟨t - 1, by omega⟩
      let U := intList (-(s : Int)) (2 * s + 1)
      have hU : ∀ a, a ∈ U ↔ (-(s : Int) ≤ a ∧ a ≤ (s : Int)) := by
        intro a; rw [mem_intList]; omega
      have hSU : ∀ a ∈ S, a ∈ U := by
        intro a ha
        have := hsub a ha
        have h1 : a ≠ -((s + 1 : Nat) : Int) := fun h => hneg (h ▸ ha)
        have h2 : a ≠ ((s + 1 : Nat) : Int) := fun h => htS (h ▸ ha)
        exact (hU a).2 (by omega)
      have hall := all_mem_of_length S U hnd hSU (by rw [length_intList]; omega)
      exact coeff_without_ends s (by omega) S (hall _ ((hU _).2 (by omega)))
        (hall _ ((hU _).2 (by omega))) (hall _ ((hU _).2 (by omega)))

/-- **The degree law.** For `t ≥ 3`, among sets of at least `2t - 1` cells, the apex has coefficient 1 exactly on the
top monomial `-t+2 … t`. -/
theorem degree_law (t : Nat) (ht : 3 ≤ t) (S : List Int) (hnd : S.Nodup) (hlen : 2 * t - 1 ≤ S.length) :
    sumOver S (apex t) = true ↔ (∀ i, i ∈ S ↔ (-(t : Int) + 2 ≤ i ∧ i ≤ t)) := by
  constructor
  · intro h
    have hsub : ∀ i ∈ S, -(t : Int) ≤ i ∧ i ≤ t := by
      intro i hi
      by_cases hc : -(t : Int) ≤ i ∧ i ≤ t
      · exact hc
      · rw [coeff_outside t S i hi (by omega)] at h; cases h
    have hin : ∀ i ∈ S, -(t : Int) + 2 ≤ i ∧ i ≤ t := by
      intro i hi
      by_cases hl : i < -(t : Int) + 2
      · rw [coeff_not_top t ht S hnd hsub hlen ⟨i, hi, hl⟩] at h; cases h
      · exact ⟨by omega, (hsub i hi).2⟩
    have hall := all_mem_of_length S (intList (-(t : Int) + 2) (2 * t - 1)) hnd
      (fun i hi => (mem_intList _ _ _).2 (by have := hin i hi; omega)) (by rw [length_intList]; omega)
    intro i
    exact ⟨hin i, fun hr => hall i ((mem_intList _ _ _).2 (by omega))⟩
  · exact coeff_top t (by omega) S hnd

/-- **The degree bound.** For `t ≥ 2`, every monomial with at least `2t` cells has coefficient 0. -/
theorem degree_bound (t : Nat) (ht : 2 ≤ t) (S : List Int) (hnd : S.Nodup) (hlen : 2 * t ≤ S.length) :
    sumOver S (apex t) = false := by
  by_cases hsub : ∀ i ∈ S, -(t : Int) ≤ i ∧ i ≤ t
  · have hlow : ∃ i ∈ S, i < -(t : Int) + 2 := by
      by_cases h : ∃ i ∈ S, i < -(t : Int) + 2
      · exact h
      · exfalso
        have := length_le_of_sub S (intList (-(t : Int) + 2) (2 * t - 1)) hnd (fun i hi => by
          rw [mem_intList]
          have h1 := hsub i hi
          have h2 : ¬ i < -(t : Int) + 2 := fun hl => h ⟨i, hi, hl⟩
          omega)
        rw [length_intList] at this; omega
    by_cases h3 : 3 ≤ t
    · exact coeff_not_top t h3 S hnd hsub (by omega) hlow
    · obtain rfl : t = 2 := by omega
      by_cases hneg : -((2 : Nat) : Int) ∈ S
      · apply coeff_with_left_cell 2 S hneg
        intro h
        have := List.length_erase_of_mem hneg
        rw [h] at this; simp at this; omega
      · have hall := all_mem_of_length S (intList (-1) 4) hnd (fun i hi => by
            rw [mem_intList]
            have h1 := hsub i hi
            have h2 : i ≠ -((2 : Nat) : Int) := fun h => hneg (h ▸ hi)
            omega) (by rw [length_intList]; omega)
        have hc : ∀ i : Int, -1 ≤ i → i ≤ 2 → i ∈ S := fun i h1 h2 => hall i ((mem_intList _ _ _).2 (by omega))
        have h2S : ((2 : Nat) : Int) ∈ S := hc _ (by omega) (by omega)
        rw [coeff_with_right_cell 2 S h2S]
        have hTmem : ∀ a, a ∈ S.erase ((2 : Nat) : Int) ↔ a ≠ ((2 : Nat) : Int) ∧ a ∈ S :=
          fun a => List.Nodup.mem_erase_iff hnd
        have hPT : ∀ a ∈ pivRange 2 0 2, a ∈ S.erase ((2 : Nat) : Int) := by
          intro a ha
          obtain ⟨k, h1, h2, h3⟩ := (mem_pivRange 2 0 2 a).1 ha
          subst h3
          exact (hTmem _).2 ⟨by simp only [piv]; omega, hc _ (by simp only [piv]; omega) (by simp only [piv]; omega)⟩
        have hperm := perm_split _ _ (hnd.erase _) (nodup_pivRange _ _ _) hPT
        apply coeff_all_pivots 2 _ _ hperm
        intro hnil
        have hmem := mem_split_rest _ (pivRange 2 0 2) 0
          ((hTmem 0).2 ⟨by omega, hc 0 (by omega) (by omega)⟩) (fun h => by
            obtain ⟨k, h1, h2, h3⟩ := (mem_pivRange 2 0 2 0).1 h
            simp only [piv] at h3; omega)
        rw [hnil] at hmem; cases hmem
  · have hout : ∃ i ∈ S, ¬ (-(t : Int) ≤ i ∧ i ≤ t) := by
      by_cases h : ∃ i ∈ S, ¬ (-(t : Int) ≤ i ∧ i ≤ t)
      · exact h
      · exact absurd (fun i hi => by
          by_cases hc : -(t : Int) ≤ i ∧ i ≤ t
          · exact hc
          · exact absurd ⟨i, hi, hc⟩ h) hsub
    obtain ⟨i, hi, hc⟩ := hout
    exact coeff_outside t S i hi (by omega)

/-- **The degree is attained.** For `t ≥ 2`, the monomial over `-t+2 … t` (of `2t - 1` cells) has coefficient 1. -/
theorem degree_attained (t : Nat) (ht : 2 ≤ t) :
    (intList (-(t : Int) + 2) (2 * t - 1)).length = 2 * t - 1 ∧
      sumOver (intList (-(t : Int) + 2) (2 * t - 1)) (apex t) = true :=
  ⟨length_intList _ _, coeff_top t ht _ (nodup_intList _ _) (fun i => by rw [mem_intList]; omega)⟩

end Rule30DegreeLaw
