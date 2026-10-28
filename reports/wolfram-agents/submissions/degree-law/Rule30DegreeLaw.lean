/-!
# The degree law for Rule 30: formal proof (in progress, L1074)

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

end Rule30DegreeLaw
