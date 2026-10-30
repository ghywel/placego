module
public import Rule30FinitePastDraft

/-!
# Normalized finite ancestors and their exact image

UNCOMPILED source preparation, GC2290. This is the translation interface for
the known G121/L077 finite-word counting argument. It uses physical evolution;
normalizing an n-step image translates it RIGHT by n. No cardinality, compiler
acceptance, independent source read or novelty is inferred merely from the map.
-/

@[expose] public section
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
