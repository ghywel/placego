module
public import Ruliology.CellularAutomata.Rule30Realization

/-!
# Finite physical ancestry: endpoint descent and a unique root

UNCOMPILED source preparation, GC2286. This packages known hand results
G121/G122 (independently read in L077, 6 October 2026). No novelty is claimed
for endpoint growth or finite injectivity. The latter is a specialization of
Rule30Equivalents.Preimages.eq_of_evol_one_eq_of_right; its elementary
right-to-left proof is included here to keep the dependency closure core-only.
The endpoint arguments likewise specialize the existing FiniteConfigs and
FrozenRuler edge theorems. The evolution below is the kit's actual physical
Rule30Realization.evol, not a decoration, stripe-front or wall-frame map.

The all-white row is excluded by Span's black endpoints. Canonical inverse
construction, the explicit finite-parent criterion, normalized counting and
backward infinite-tail period families are not included in this first module.
No compiler result, independent source acceptance or official replay yet.
-/

@[expose] public section
namespace Ruliology.CellularAutomata.Rule30FinitePastDraft
open Rule30Jen Rule30Realization

/-- Exact finite nonempty support interval, including internal white cells. -/
structure Span (x : Int → Bool) (lo hi : Int) : Prop where
  ordered : lo ≤ hi
  left_black : x lo = true
  right_black : x hi = true
  left_white : ∀ i, i < lo → x i = false
  right_white : ∀ i, hi < i → x i = false

def FiniteNonzero (x : Int → Bool) : Prop := ∃ lo hi, Span x lo hi

def Root (x : Int → Bool) : Prop :=
  FiniteNonzero x ∧ ∀ p, FiniteNonzero p → evol p 1 ≠ x

theorem span_unique {x : Int → Bool} {l r l' r' : Int}
    (h : Span x l r) (h' : Span x l' r') : l = l' ∧ r = r' := by
  have hl : ¬ l < l' := by
    intro e; have z := h'.left_white l e; rw [h.left_black] at z; cases z
  have hl' : ¬ l' < l := by
    intro e; have z := h.left_white l' e; rw [h'.left_black] at z; cases z
  have hr : ¬ r' < r := by
    intro e; have z := h'.right_white r e; rw [h.right_black] at z; cases z
  have hr' : ¬ r < r' := by
    intro e; have z := h.right_white r' e; rw [h'.right_black] at z; cases z
  omega

/-- The zero row is not in the finite-nonzero domain. -/
theorem zero_not_finite_nonzero : ¬ FiniteNonzero (fun _ => false) := by
  rintro ⟨l, r, h⟩
  have z := h.left_black
  cases z

theorem evol_zero : ∀ n : Nat, evol (fun _ => false) n = (fun _ => false)
  | 0 => rfl
  | n+1 => by
    funext i
    change rule (evol (fun _ => false) n (i-1)) (evol (fun _ => false) n i)
      (evol (fun _ => false) n (i+1)) = false
    rw [evol_zero n]
    rfl

/-- Endpoint growth, included as a small core-only wrapper of known edge facts. -/
theorem span_step {x : Int → Bool} {l r : Int} (h : Span x l r) :
    Span (evol x 1) (l-1) (r+1) := by
  refine ⟨by have := h.ordered; omega, ?_, ?_, ?_, ?_⟩
  · change rule (x ((l-1)-1)) (x (l-1)) (x ((l-1)+1)) = true
    rw [show (l-1)+1=l by omega, h.left_white _ (by omega),
      h.left_white _ (by omega), h.left_black]
    rfl
  · change rule (x ((r+1)-1)) (x (r+1)) (x ((r+1)+1)) = true
    rw [show (r+1)-1=r by omega, h.right_black,
      h.right_white _ (by omega), h.right_white _ (by omega)]
    rfl
  · intro i hi
    change rule (x (i-1)) (x i) (x (i+1)) = false
    rw [h.left_white _ (by omega), h.left_white _ (by omega), h.left_white _ (by omega)]
    rfl
  · intro i hi
    change rule (x (i-1)) (x i) (x (i+1)) = false
    rw [h.right_white _ (by omega), h.right_white _ (by omega), h.right_white _ (by omega)]
    rfl

/-- Standard evolution composition, without importing additional package modules. -/
theorem evol_add (x : Int → Bool) (a : Nat) :
    ∀ b : Nat, evol (evol x a) b = evol x (a+b)
  | 0 => rfl
  | b+1 => by
    funext i
    change rule (evol (evol x a) b (i-1)) (evol (evol x a) b i)
      (evol (evol x a) b (i+1)) =
      rule (evol x (a+b) (i-1)) (evol x (a+b) i) (evol x (a+b) (i+1))
    rw [evol_add x a b]

theorem span_evol {x : Int → Bool} {l r : Int} (h : Span x l r) :
    ∀ n : Nat, Span (evol x n) (l-n) (r+n)
  | 0 => by simpa [evol] using h
  | n+1 => by
    have hs := span_step (span_evol h n)
    rw [evol_add] at hs
    simpa only [show l-(n : Int)-1=l-((n+1 : Nat) : Int) by omega,
      show r+(n : Int)+1=r+((n+1 : Nat) : Int) by omega] using hs

theorem finite_evol {x : Int → Bool} (h : FiniteNonzero x) (n : Nat) :
    FiniteNonzero (evol x n) := by
  obtain ⟨l,r,hs⟩ := h
  exact ⟨l-n,r+n,span_evol hs n⟩

/-- Equal images and an equal right tail force equal whole configurations.
Known Preimages theorem, with the same two-cell backward reconstruction. -/
theorem injective_of_right {x y : Int → Bool} {k : Int}
    (he : evol x 1 = evol y 1) (hr : ∀ i, k ≤ i → x i = y i) : x=y := by
  have left : ∀ n : Nat, x (k-n)=y (k-n) ∧ x (k-n+1)=y (k-n+1) := by
    intro n
    induction n with
    | zero => simpa using And.intro (hr k (by omega)) (hr (k+1) (by omega))
    | succ n ih =>
      have e := congrFun he (k-n)
      change xor (x (k-n-1)) (x (k-n) || x (k-n+1)) =
        xor (y (k-n-1)) (y (k-n) || y (k-n+1)) at e
      rw [ih.1,ih.2] at e
      have prior : x (k-n-1)=y (k-n-1) := by
        cases a:x (k-n-1) <;> cases b:y (k-n-1) <;>
          cases c:(y (k-n) || y (k-n+1)) <;> simp_all
      constructor
      · simpa only [show k-((n+1 : Nat) : Int)=k-(n : Int)-1 by omega] using prior
      · simpa only [show k-((n+1 : Nat) : Int)+1=k-(n : Int) by omega] using ih.1
  funext i
  by_cases hki : k ≤ i
  · exact hr i hki
  · have e := (left (k-i).toNat).1
    simpa only [show k-(((k-i).toNat : Nat) : Int)=i by omega] using e

theorem finite_step_injective {x y : Int → Bool}
    (hx : FiniteNonzero x) (hy : FiniteNonzero y) (he : evol x 1=evol y 1) : x=y := by
  obtain ⟨lx,rx,sx⟩ := hx
  obtain ⟨ly,ry,sy⟩ := hy
  apply injective_of_right (k := max rx ry+1) he
  intro i hi
  rw [sx.right_white i (by omega),sy.right_white i (by omega)]

theorem finite_evol_injective {x y : Int → Bool}
    (hx : FiniteNonzero x) (hy : FiniteNonzero y) :
    ∀ n : Nat, evol x n=evol y n → x=y
  | 0, he => he
  | n+1, he => by
    apply finite_evol_injective hx hy n
    apply finite_step_injective (finite_evol hx n) (finite_evol hy n)
    simpa only [evol_add] using he

/-- Every finite ancestor shrinks the two endpoints by its age. -/
theorem ancestor_endpoints {x y : Int → Bool} {l r a b : Int} {n : Nat}
    (hx : Span x a b) (hy : Span y l r) (he : evol x n=y) :
    a=l+n ∧ b=r-n := by
  have hs := span_evol hx n
  rw [he] at hs
  have := span_unique hs hy
  omega

/-- In particular, no nonzero finite row has an unbounded finite past. -/
theorem ancestor_bound {x y : Int → Bool} {l r : Int} {n : Nat}
    (hx : FiniteNonzero x) (hy : Span y l r) (he : evol x n=y) :
    2*n ≤ (r-l).toNat := by
  obtain ⟨a,b,hs⟩ := hx
  have ends := ancestor_endpoints hs hy he
  have := hs.ordered
  have := hy.ordered
  omega

/-- Width one and width two rows are roots; this also guards small-period arithmetic. -/
theorem small_span_root {x : Int → Bool} {l r : Int}
    (hx : Span x l r) (hsmall : r-l < 2) : Root x := by
  refine ⟨⟨l,r,hx⟩,?_⟩
  intro p hp he
  have bound := ancestor_bound hp hx he
  have := hx.ordered
  omega

/-- Descent by the support diameter terminates at a finite root. -/
theorem root_exists {y : Int → Bool} (hy : FiniteNonzero y) :
    ∃ x n, Root x ∧ evol x n=y := by
  classical
  have descend : ∀ d : Nat, ∀ y : Int → Bool, ∀ l r : Int,
      Span y l r → (r-l).toNat=d → ∃ x n, Root x ∧ evol x n=y := by
    intro d
    induction d using Nat.strongRecOn with
    | ind d ih =>
      intro y l r hs hd
      by_cases hp : ∃ p, FiniteNonzero p ∧ evol p 1=y
      · obtain ⟨p,hp,he⟩ := hp
        obtain ⟨a,b,sp⟩ := hp
        have ends := ancestor_endpoints sp hs he
        have less : (b-a).toNat < d := by
          have := sp.ordered
          have := hs.ordered
          omega
        obtain ⟨x,n,hroot,hxn⟩ := ih (b-a).toNat less p a b sp rfl
        refine ⟨x,n+1,hroot,?_⟩
        rw [← evol_add x n 1,hxn,he]
      · refine ⟨y,0,⟨⟨l,r,hs⟩,?_⟩,rfl⟩
        intro p hp' he
        exact hp ⟨p,hp',he⟩
  obtain ⟨l,r,hs⟩ := hy
  exact descend (r-l).toNat y l r hs rfl

theorem root_ancestor_time_zero {x y : Int → Bool} (hx : Root x)
    (hy : FiniteNonzero y) {n : Nat} (he : evol y n=x) : n=0 := by
  cases n with
  | zero => rfl
  | succ n =>
    have impossible := hx.2 (evol y n) (finite_evol hy n)
    apply False.elim
    apply impossible
    simpa only [evol_add] using he

/-- A root cannot be reached later than another root along the same finite ray. -/
theorem root_age_eq_of_le {x y z : Int → Bool} {a b : Nat}
    (hx : Root x) (hy : Root y) (ha : evol x a=z) (hb : evol y b=z)
    (hab : a ≤ b) : a=b := by
  have same : evol x a=evol (evol y (b-a)) a := by
    rw [evol_add,show b-a+a=b by omega,ha,hb]
  have ex : x=evol y (b-a) :=
    finite_evol_injective hx.1 (finite_evol hy.1 (b-a)) a same
  have := root_ancestor_time_zero hx hy.1 ex.symm
  omega

/-- Root and age are simultaneously unique in the physical finite-nonzero domain. -/
theorem root_unique {x y z : Int → Bool} {a b : Nat}
    (hx : Root x) (hy : Root y) (ha : evol x a=z) (hb : evol y b=z) :
    x=y ∧ a=b := by
  have age : a=b := by
    by_cases hab : a ≤ b
    · exact root_age_eq_of_le hx hy ha hb hab
    · exact (root_age_eq_of_le hy hx hb ha (by omega)).symm
  refine ⟨?_,age⟩
  apply finite_evol_injective hx.1 hy.1 a
  rw [ha,age,hb]

/-- Complete finite-root decomposition, with its endpoint depth bound. -/
theorem finite_root_decomposition {y : Int → Bool} {l r : Int} (hy : Span y l r) :
    ∃ x n, Root x ∧ evol x n=y ∧ 2*n ≤ (r-l).toNat ∧
      ∀ x' n', Root x' → evol x' n'=y → x'=x ∧ n'=n := by
  obtain ⟨x,n,hroot,he⟩ := root_exists ⟨l,r,hy⟩
  refine ⟨x,n,hroot,he,ancestor_bound hroot.1 hy he,?_⟩
  intro x' n' hx' he'
  exact root_unique hx' hroot he' he

end Ruliology.CellularAutomata.Rule30FinitePastDraft
