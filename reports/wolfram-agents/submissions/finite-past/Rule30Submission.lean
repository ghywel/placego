module
public import Rule30PrizeKit
public import Ruliology.CellularAutomata.Rule30Realization

/-! Prepared single-file source, GC2292. UNCOMPILED; not a checker receipt. -/
@[expose] public section

/- BEGIN carrying body: Rule30FinitePastDraft.lean -/

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

/- BEGIN carrying body: FiniteParentCriterionDraft.lean -/

/-!
# The physical white-right parent's finite stopping test

UNCOMPILED source preparation, GC2288. This transcribes CL659/GC2261's
independently read test, with G121/G122 and current Preimages/ZeroBoundary
credited in GC2282. The parent is an actual physical predecessor with a fixed
white right tail, not a freely chosen wall-frame parent. Existence/construction
of that canonical parent is already provided by Preimages; no replacement
constructor or all-depth infinite-tail theorem is asserted here.
-/

namespace Ruliology.CellularAutomata.Rule30FinitePastDraft
open Rule30Jen Rule30Realization

/-- Under a white output half-line, two adjacent white parent cells propagate
white indefinitely to the left. This is the physical inverse stopping rule. -/
theorem white_left_from_pair {p y : Int → Bool} {l : Int}
    (he : evol p 1=y) (hy : ∀ i, i<l → y i=false)
    (h0 : p l=false) (h1 : p (l-1)=false) : ∀ i, i≤l → p i=false := by
  have down : ∀ n : Nat, p (l-n)=false ∧ p (l-n-1)=false := by
    intro n
    induction n with
    | zero => simpa using And.intro h0 h1
    | succ n ih =>
      have e : evol p 1 (l-n-1)=false := by
        rw [he]
        exact hy _ (by omega)
      change rule (p ((l-n-1)-1)) (p (l-n-1)) (p ((l-n-1)+1))=false at e
      rw [show (l-(n : Int)-1)+1=l-(n : Int) by omega,ih.2,ih.1] at e
      have next : p ((l-n-1)-1)=false := by simpa [rule] using e
      constructor
      · simpa only [show l-((n+1 : Nat) : Int)=l-(n : Int)-1 by omega] using ih.2
      · simpa only [show l-((n+1 : Nat) : Int)-1=(l-(n : Int)-1)-1 by omega] using next
  intro i hi
  have e := (down (l-i).toNat).1
  simpa only [show l-(((l-i).toNat : Nat) : Int)=i by omega] using e

/-- Exact finite-parent test, with the white-right boundary fixed explicitly.
The right boundary is at R, not at R+1; omitting that distinction changes the
parent problem. Width one/two and all internal zeroes are covered. -/
theorem finite_white_parent_iff {p y : Int → Bool} {l r : Int}
    (hy : Span y l r) (he : evol p 1=y)
    (hr : ∀ i, r≤i → p i=false) :
    FiniteNonzero p ↔ y (l+1)=true ∧ p (l+1)=true := by
  constructor
  · intro hp
    obtain ⟨a,b,sp⟩ := hp
    have ends := ancestor_endpoints sp hy he
    have hp1 : p (l+1)=true := by
      rw [← ends.1]
      exact sp.left_black
    refine ⟨?_,hp1⟩
    rw [← he]
    change rule (p ((l+1)-1)) (p (l+1)) (p ((l+1)+1))=true
    rw [sp.left_white _ (by omega),hp1]
    rfl
  · rintro ⟨hy1,hp1⟩
    have e1 := congrFun he (l+1)
    change rule (p ((l+1)-1)) (p (l+1)) (p ((l+1)+1))=y (l+1) at e1
    rw [show (l+1)-1=l by omega,hp1,hy1] at e1
    have hp0 : p l=false := by
      cases e:p l <;> simp_all [rule]
    have e0 := congrFun he l
    change rule (p (l-1)) (p l) (p (l+1))=y l at e0
    rw [hp0,hp1,hy.left_black] at e0
    have hpm : p (l-1)=false := by
      cases e:p (l-1) <;> simp_all [rule]
    have left := white_left_from_pair he hy.left_white hp0 hpm
    have rightBlack : p (r-1)=true := by
      have e := congrFun he r
      change rule (p (r-1)) (p r) (p (r+1))=y r at e
      rw [hr r (by omega),hr (r+1) (by omega),hy.right_black] at e
      simpa [rule] using e
    have ordered : l+1≤r-1 := by
      by_contra hn
      have z := hr (l+1) (by omega)
      rw [hp1] at z
      cases z
    exact ⟨l+1,r-1,⟨ordered,hp1,rightBlack,
      fun i hi => left i (by omega),fun i hi => hr i (by omega)⟩⟩

end Ruliology.CellularAutomata.Rule30FinitePastDraft

/- BEGIN carrying body: NormalizedFinitePastDraft.lean -/

/-!
# Normalized finite ancestors and their exact image

UNCOMPILED source preparation, GC2290. This is the translation interface for
the known G121/L077 finite-word counting argument. It uses physical evolution;
normalizing an n-step image translates it RIGHT by n. No cardinality, compiler
acceptance, independent source read or novelty is inferred merely from the map.
-/

namespace Ruliology.CellularAutomata.Rule30FinitePastDraft
open Rule30Jen Rule30Realization

def translate (a : Int) (x : Int → Bool) : Int → Bool := fun i => x (i-a)
def Normal (w : Nat) (x : Int → Bool) : Prop := Span x 0 ((w : Int)-1)
def Past (n : Nat) (y : Int → Bool) : Prop := ∃ p, FiniteNonzero p ∧ evol p n=y

def normalizedImage (n : Nat) (x : Int → Bool) : Int → Bool :=
  translate n (evol x n)

theorem translate_injective (a : Int) {x y : Int → Bool}
    (he : translate a x=translate a y) : x=y := by
  funext i
  have e := congrFun he (i+a)
  change x ((i+a)-a)=y ((i+a)-a) at e
  simpa only [show (i+a)-a=i by omega] using e

theorem translate_span (a : Int) {x : Int → Bool} {l r : Int}
    (hx : Span x l r) : Span (translate a x) (l+a) (r+a) := by
  refine ⟨by have := hx.ordered; omega,?_,?_,?_,?_⟩
  · change x ((l+a)-a)=true
    rw [show (l+a)-a=l by omega]
    exact hx.left_black
  · change x ((r+a)-a)=true
    rw [show (r+a)-a=r by omega]
    exact hx.right_black
  · intro i hi
    exact hx.left_white (i-a) (by omega)
  · intro i hi
    exact hx.right_white (i-a) (by omega)

theorem finite_translate (a : Int) {x : Int → Bool} (hx : FiniteNonzero x) :
    FiniteNonzero (translate a x) := by
  obtain ⟨l,r,h⟩ := hx
  exact ⟨l+a,r+a,translate_span a h⟩

/-- Spatial translation commutes with the actual physical evolution. -/
theorem evol_translate (a : Int) (x : Int → Bool) :
    ∀ n : Nat, evol (translate a x) n=translate a (evol x n)
  | 0 => rfl
  | n+1 => by
    funext i
    change rule (evol (translate a x) n (i-1)) (evol (translate a x) n i)
      (evol (translate a x) n (i+1)) =
      rule (evol x n ((i-a)-1)) (evol x n (i-a)) (evol x n ((i-a)+1))
    rw [evol_translate a x n]
    change rule (evol x n ((i-1)-a)) (evol x n (i-a)) (evol x n ((i+1)-a)) = _
    rw [show (i-1)-a=(i-a)-1 by omega,show (i+1)-a=(i-a)+1 by omega]

theorem normal_positive {w : Nat} {x : Int → Bool} (hx : Normal w x) : 0<w := by
  have := hx.ordered
  omega

theorem normal_finite {w : Nat} {x : Int → Bool} (hx : Normal w x) : FiniteNonzero x :=
  ⟨0,(w : Int)-1,hx⟩

/-- The normalized n-step map increases width by exactly2n. -/
theorem normalizedImage_normal {w n : Nat} {x : Int → Bool} (hx : Normal w x) :
    Normal (w+2*n) (normalizedImage n x) := by
  have h := translate_span (n : Int) (span_evol hx n)
  change Span (normalizedImage n x) (0-(n : Int)+n) (((w : Int)-1)+n+n) at h
  rw [show 0-(n : Int)+n=0 by omega,
    show ((w : Int)-1)+(n : Int)+n=((w+2*n : Nat) : Int)-1 by omega] at h
  exact h

theorem normalizedImage_injective {w n : Nat} {x y : Int → Bool}
    (hx : Normal w x) (hy : Normal w y)
    (he : normalizedImage n x=normalizedImage n y) : x=y := by
  exact finite_evol_injective (normal_finite hx) (normal_finite hy) n
    (translate_injective (n : Int) he)

/-- Normalization translates the ancestor as well; it does not lose a physical past. -/
theorem normalizedImage_past {w n : Nat} {x : Int → Bool} (hx : Normal w x) :
    Past n (normalizedImage n x) := by
  refine ⟨translate n x,finite_translate n (normal_finite hx),?_⟩
  exact evol_translate n x n

/-- Every normalized target with an n-step finite past comes from the unique
normalized width-w ancestor. This is the surjectivity needed for counting. -/
theorem normalizedImage_range (w n : Nat) (y : Int → Bool) :
    (∃ x, Normal w x ∧ normalizedImage n x=y) ↔ Normal (w+2*n) y ∧ Past n y := by
  constructor
  · rintro ⟨x,hx,rfl⟩
    exact ⟨normalizedImage_normal hx,normalizedImage_past hx⟩
  · rintro ⟨hy,p,hp,he⟩
    obtain ⟨a,b,sp⟩ := hp
    have ends := ancestor_endpoints sp hy he
    have hs := translate_span (-(n : Int)) sp
    have hl : a+(-(n : Int))=0 := by omega
    have hr : b+(-(n : Int))=(w : Int)-1 := by omega
    rw [hl,hr] at hs
    refine ⟨translate (-(n : Int)) p,hs,?_⟩
    funext i
    change evol (translate (-(n : Int)) p) n (i-(n : Int))=y i
    rw [evol_translate]
    change evol p n ((i-(n : Int))-(-(n : Int)))=y i
    rw [show (i-(n : Int))-(-(n : Int))=i by omega,he]

/-- Tiny targets have no positive finite past; no truncated subtraction is used. -/
theorem no_past_of_small_width {w n : Nat} {y : Int → Bool}
    (hy : Normal w y) (hsmall : w≤2*n) : ¬ Past n y := by
  rintro ⟨p,hp,he⟩
  have hb := ancestor_bound hp hy he
  have hw := normal_positive hy
  omega

end Ruliology.CellularAutomata.Rule30FinitePastDraft

/- BEGIN carrying body: FinitePastCountDraft.lean -/

/-!
# Counting normalized finite parents without a Mathlib cardinality import

UNCOMPILED source preparation, GC2290. Reuses Rule30Jen.allLists,
length_allLists and nodup_map_of_inj. Counts are lengths of proved-exhaustive,
duplicate-free enumerations of actual physical rows, not unproved multiset
lengths. The bijection and counts are the known G121/L077 argument. Width zero
is empty, width one is a singleton, and width at least two has free interior.
No compiler acceptance, official replay or independent source read is claimed.
-/

namespace Ruliology.CellularAutomata.Rule30FinitePastDraft
open Rule30Jen Rule30Realization

/-- A Boolean interior framed by black endpoints; all exterior cells are white. -/
def framedRow (bits : List Bool) (i : Int) : Bool :=
  if i=0 ∨ i=(bits.length : Int)+1 then true
  else if 0<i ∧ i<(bits.length : Int)+1 then bits.getD (i-1).toNat false else false

def samples (x : Int → Bool) (n : Nat) : List Bool :=
  List.ofFn fun i : Fin n => x ((i.val : Int)+1)

theorem length_samples (x : Int → Bool) (n : Nat) : (samples x n).length=n := by
  simp [samples]

theorem framedRow_span (bits : List Bool) : Span (framedRow bits) 0 ((bits.length : Int)+1) := by
  refine ⟨by omega,?_,?_,?_,?_⟩
  · simp [framedRow]
  · simp [framedRow]
  · intro i hi
    have h0 : ¬(i=0 ∨ i=(bits.length : Int)+1) := by omega
    have h1 : ¬(0<i ∧ i<(bits.length : Int)+1) := by omega
    simp [framedRow,h0,h1]
  · intro i hi
    have h0 : ¬(i=0 ∨ i=(bits.length : Int)+1) := by omega
    have h1 : ¬(0<i ∧ i<(bits.length : Int)+1) := by omega
    simp [framedRow,h0,h1]

theorem framedRow_interior (bits : List Bool) {i : Nat} (hi : i<bits.length) :
    framedRow bits ((i : Int)+1)=bits[i] := by
  have h0 : ¬((i : Int)+1=0 ∨ (i : Int)+1=(bits.length : Int)+1) := by omega
  have h1 : 0<(i : Int)+1 ∧ (i : Int)+1<(bits.length : Int)+1 := by omega
  simp only [framedRow,if_neg h0,if_pos h1,
    show (((i : Int)+1)-1).toNat=i by omega,List.getD_eq_getElem?_getD,
    List.getElem?_eq_getElem hi,Option.getD_some]

theorem framedRow_injective {a b : List Bool} (hl : a.length=b.length)
    (he : framedRow a=framedRow b) : a=b := by
  apply List.ext_getElem hl
  intro i hi hj
  have e := congrFun he ((i : Int)+1)
  rw [framedRow_interior a hi,framedRow_interior b hj] at e
  exact e

theorem framedRow_samples {x : Int → Bool} {n : Nat} (hx : Span x 0 ((n : Int)+1)) :
    framedRow (samples x n)=x := by
  have hf := framedRow_span (samples x n)
  simp only [length_samples] at hf
  funext i
  by_cases h0 : i=0
  · subst i; exact hf.left_black.trans hx.left_black.symm
  by_cases hn : i=(n : Int)+1
  · subst i; exact hf.right_black.trans hx.right_black.symm
  by_cases hl : i<0
  · exact (hf.left_white i hl).trans (hx.left_white i hl).symm
  by_cases hr : (n : Int)+1<i
  · exact (hf.right_white i hr).trans (hx.right_white i hr).symm
  have hi : (i-1).toNat<(samples x n).length := by
    rw [length_samples]
    omega
  have e := framedRow_interior (samples x n) hi
  have index : (((i-1).toNat : Nat) : Int)+1=i := by omega
  simpa only [samples,List.getElem_ofFn,index] using e

/-- Converse to the kit's membership lemma: its enumeration has only the stated length. -/
theorem length_of_mem_allLists : ∀ n : Nat, ∀ bits : List Bool,
    bits ∈ allLists n → bits.length=n
  | 0,bits,h => by
    simp only [allLists,List.mem_singleton] at h
    subst bits
    rfl
  | n+1,bits,h => by
    change bits ∈ (allLists n).map (false :: ·) ++ (allLists n).map (true :: ·) at h
    rcases List.mem_append.mp h with h | h
    · obtain ⟨b,hb,rfl⟩ := List.mem_map.mp h
      simp only [List.length_cons,length_of_mem_allLists n b hb]
    · obtain ⟨b,hb,rfl⟩ := List.mem_map.mp h
      simp only [List.length_cons,length_of_mem_allLists n b hb]

theorem allLists_nodup : ∀ n : Nat, (allLists n).Nodup
  | 0 => by simp [allLists]
  | n+1 => by
    rw [allLists,List.nodup_append]
    refine ⟨?_,?_,?_⟩
    · apply nodup_map_of_inj (false :: ·) (allLists_nodup n)
      intro a _ b _ he
      exact (List.cons.inj he).2
    · apply nodup_map_of_inj (true :: ·) (allLists_nodup n)
      intro a _ b _ he
      exact (List.cons.inj he).2
    · intro a ha b hb he
      obtain ⟨a',_,rfl⟩ := List.mem_map.mp ha
      obtain ⟨b',_,rfl⟩ := List.mem_map.mp hb
      simp at he

def singleRow (i : Int) : Bool := decide (i=0)

theorem singleRow_span : Span singleRow 0 0 := by
  refine ⟨by omega,by decide,by decide,?_,?_⟩
  · intro i hi; simp [singleRow]; omega
  · intro i hi; simp [singleRow]; omega

theorem span_zero_unique {x : Int → Bool} (hx : Span x 0 0) : x=singleRow := by
  funext i
  by_cases hi : i=0
  · subst i; simpa [singleRow] using hx.left_black
  · have hz : x i=false := by
      by_cases hl : i<0
      · exact hx.left_white i hl
      · exact hx.right_white i (by omega)
    simp [singleRow,hi,hz]

def allRows : Nat → List (Int → Bool)
  | 0 => []
  | 1 => [singleRow]
  | n+2 => (allLists n).map framedRow

def widthCount : Nat → Nat
  | 0 => 0
  | 1 => 1
  | n+2 => 2^n

theorem mem_allRows (w : Nat) (x : Int → Bool) : x ∈ allRows w ↔ Normal w x := by
  cases w with
  | zero =>
    change x ∈ [] ↔ Span x 0 (-1)
    constructor
    · intro h; cases h
    · intro h; have := h.ordered; omega
  | succ w =>
    cases w with
    | zero =>
      simp only [allRows,List.mem_singleton]
      change x=singleRow ↔ Span x 0 0
      constructor
      · intro h; rw [h]; exact singleRow_span
      · exact span_zero_unique
    | succ n =>
      change x ∈ (allLists n).map framedRow ↔ Normal (n+2) x
      constructor
      · intro h
        obtain ⟨bits,hb,rfl⟩ := List.mem_map.mp h
        have hs := framedRow_span bits
        rw [length_of_mem_allLists n bits hb] at hs
        change Span (framedRow bits) 0 (((n+2 : Nat) : Int)-1)
        simpa only [show (((n+2 : Nat) : Int)-1)=(n : Int)+1 by omega] using hs
      · intro hx
        have hs : Span x 0 ((n : Int)+1) := by
          simpa only [Normal,show (((n+2 : Nat) : Int)-1)=(n : Int)+1 by omega] using hx
        apply List.mem_map.mpr
        refine ⟨samples x n,?_,framedRow_samples hs⟩
        have h := mem_allLists (samples x n)
        simpa only [length_samples] using h

theorem allRows_nodup : ∀ w : Nat, (allRows w).Nodup
  | 0 => by simp [allRows]
  | 1 => by simp [allRows]
  | n+2 => by
    apply nodup_map_of_inj framedRow (allLists_nodup n)
    intro a ha b hb he
    exact framedRow_injective
      ((length_of_mem_allLists n a ha).trans (length_of_mem_allLists n b hb).symm) he

theorem allRows_length : ∀ w : Nat, (allRows w).length=widthCount w
  | 0 => rfl
  | 1 => rfl
  | n+2 => by simp [allRows,widthCount,length_allLists]

/-- Enumerate the normalized n-step images of all width-w words. -/
def ancestorImages (w n : Nat) : List (Int → Bool) :=
  (allRows w).map (normalizedImage n)

theorem mem_ancestorImages (w n : Nat) (y : Int → Bool) :
    y ∈ ancestorImages w n ↔ Normal (w+2*n) y ∧ Past n y := by
  rw [← normalizedImage_range w n y]
  constructor
  · intro h
    obtain ⟨x,hx,he⟩ := List.mem_map.mp h
    exact ⟨x,(mem_allRows w x).mp hx,he⟩
  · rintro ⟨x,hx,he⟩
    exact List.mem_map.mpr ⟨x,(mem_allRows w x).mpr hx,he⟩

theorem ancestorImages_nodup (w n : Nat) : (ancestorImages w n).Nodup := by
  apply nodup_map_of_inj (normalizedImage n) (allRows_nodup w)
  intro x hx y hy he
  exact normalizedImage_injective ((mem_allRows w x).mp hx) ((mem_allRows w y).mp hy) he

theorem ancestorImages_length (w n : Nat) : (ancestorImages w n).length=widthCount w := by
  simp only [ancestorImages,List.length_map,allRows_length]

/-- Actual width-w finite-parent words, including the empty width-one/two cases. -/
def parentRows (w : Nat) : List (Int → Bool) :=
  if 3≤w then ancestorImages (w-2) 1 else []

theorem mem_parentRows (w : Nat) (y : Int → Bool) :
    y ∈ parentRows w ↔ Normal w y ∧ Past 1 y := by
  by_cases hw : 3≤w
  · simp only [parentRows,if_pos hw,mem_ancestorImages,
      show w-2+2*1=w by omega]
  · simp only [parentRows,if_neg hw,List.not_mem_nil,false_iff]
    intro h
    exact no_past_of_small_width h.1 (by omega) h.2

theorem parentRows_nodup (w : Nat) : (parentRows w).Nodup := by
  by_cases hw : 3≤w
  · simp only [parentRows,if_pos hw]
    exact ancestorImages_nodup (w-2) 1
  · simp [parentRows,hw]

theorem parentRows_count (w : Nat) :
    (parentRows w).length=if 3≤w then widthCount (w-2) else 0 := by
  by_cases hw : 3≤w <;> simp [parentRows,hw,ancestorImages_length]

/-- The usual one-quarter numerator, with all subtraction justified by w>=4. -/
theorem parentRows_count_ge_four {w : Nat} (hw : 4≤w) :
    (parentRows w).length=2^(w-4) := by
  obtain ⟨n,rfl⟩ : ∃ n : Nat, w=n+4 := ⟨w-4,by omega⟩
  rw [parentRows_count,if_pos (by omega),show n+4-2=n+2 by omega]
  simp [widthCount]

theorem parentRows_count_small :
    (parentRows 1).length=0 ∧ (parentRows 2).length=0 ∧ (parentRows 3).length=1 := by
  simp [parentRows_count,widthCount]

end Ruliology.CellularAutomata.Rule30FinitePastDraft

/- BEGIN carrying body: SubmissionHeadlinesDraft.lean -/

/-!
UNCOMPILED public headline wrappers, GC2292. The four proof modules are local
preparation files, not verifier imports. A later self-contained assembly must
carry their full bodies and import the official Rule30PrizeKit statements.
Known G121/G122/L077 and Karttunen's 2016 OEIS ancestry records are credited.
No official replay, source acceptance, notebook build or posting is claimed.
-/
namespace Rule30Submission
open Ruliology.CellularAutomata.Rule30Realization
open Ruliology.CellularAutomata.Rule30FinitePastDraft

/-- Unique finite root and age, with the physical support-depth bound. -/
theorem finite_root_age {y : Int → Bool} {l r : Int} (hy : Span y l r) :
    ∃ x n, Root x ∧ evol x n=y ∧ 2*n ≤ (r-l).toNat ∧
      ∀ x' n', Root x' → evol x' n'=y → x'=x ∧ n'=n :=
  finite_root_decomposition hy

/-- A test for an actual predecessor with the stated white-right boundary. -/
theorem finite_parent_test {p y : Int → Bool} {l r : Int}
    (hy : Span y l r) (he : evol p 1=y)
    (hr : ∀ i, r≤i → p i=false) :
    FiniteNonzero p ↔ y (l+1)=true ∧ p (l+1)=true :=
  finite_white_parent_iff hy he hr

/-- Both injection and the exact range, so the image statement is a bijection. -/
theorem normalized_ancestor_bijection (w n : Nat) :
    (∀ x y : Int → Bool, Normal w x → Normal w y →
      normalizedImage n x=normalizedImage n y → x=y) ∧
    (∀ y : Int → Bool, (∃ x, Normal w x ∧ normalizedImage n x=y) ↔
      Normal (w+2*n) y ∧ Past n y) := by
  constructor
  · intro x y hx hy he
    exact normalizedImage_injective hx hy he
  · exact normalizedImage_range w n

/-- The normal-word enumeration is exhaustive and duplicate-free, with exact size. -/
theorem finite_word_enumeration (w : Nat) :
    (allRows w).Nodup ∧ (∀ y : Int → Bool, y ∈ allRows w ↔ Normal w y) ∧
      (allRows w).length=widthCount w :=
  ⟨allRows_nodup w,mem_allRows w,allRows_length w⟩

/-- Counts actual finite-parent words, with no unproved enumeration assumption. -/
theorem finite_parent_enumeration (w : Nat) :
    (parentRows w).Nodup ∧
    (∀ y : Int → Bool, y ∈ parentRows w ↔ Normal w y ∧ Past 1 y) ∧
    (parentRows w).length=(if 3≤w then widthCount (w-2) else 0) :=
  ⟨parentRows_nodup w,mem_parentRows w,parentRows_count w⟩

theorem finite_parent_count {w : Nat} (hw : 4≤w) :
    (parentRows w).length=2^(w-4) :=
  parentRows_count_ge_four hw

theorem finite_parent_small_widths :
    (parentRows 1).length=0 ∧ (parentRows 2).length=0 ∧ (parentRows 3).length=1 :=
  parentRows_count_small

end Rule30Submission
