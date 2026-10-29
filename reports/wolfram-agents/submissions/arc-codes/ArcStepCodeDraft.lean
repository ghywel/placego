import ArcCoverDraft

/-!
# Constructing the lifted mismatch cover from finite-step constancy

UNCOMPILED draft. A periodic binary function is specified by finitely many possible jump points modulo1 and
constancy on intervals crossing none of their integer translates. That explicit property is the StepCode
interface, not a theorem about an imported general StepFunction object. The signed crossing argument then
constructs LiftCover, removing it as a separate hypothesis of the one-scale theorem. Continued fractions and
the Rule30 physical interface remain to be connected.
-/

namespace ArcStepCode

/-- Right-continuous finite-step constancy, with possible jump locations given modulo integers.
Endpoints may be redundant or repeated; r counts the supplied labels. -/
structure StepCode (r : Nat) where
  value : ℝ → Bool
  endpoint : Nat → ℝ
  periodic : ∀ x : ℝ, ∀ z : ℤ, value (x+z) = value x
  constant_between : ∀ x y : ℝ, x ≤ y →
    (∀ i : Nat, i < r → ∀ z : ℤ, ¬ (x < endpoint i+z ∧ endpoint i+z ≤ y)) → value x = value y

def orbit {r : Nat} (S : StepCode r) (alpha theta : ℝ) (s : Nat) : Bool :=
  S.value (theta+(s : ℝ)*alpha)

/-- A change of colour crosses a possible jump, including its upper endpoint but excluding its lower one. -/
theorem crossing {r : Nat} (S : StepCode r) (x y : ℝ) (hxy : x ≤ y)
    (hne : S.value x ≠ S.value y) :
    ∃ i : Nat, i < r ∧ ∃ z : ℤ, x < S.endpoint i+z ∧ S.endpoint i+z ≤ y := by
  refine Classical.byContradiction fun hno => ?_
  apply hne
  apply S.constant_between x y hxy
  intro i hi z hz
  exact hno ⟨i,hi,z,hz⟩

/-- A genuine orbit mismatch has a label and an integer lift inside one common signed-displacement interval. -/
theorem break_has_lift {r : Nat} (S : StepCode r) (alpha theta : ℝ) (q : Nat) (p : ℤ)
    (hepsilon : 0 < |(q : ℝ)*alpha-p|) (s : Nat)
    (hb : orbit S alpha theta (s+q) ≠ orbit S alpha theta s) :
    ∃ i : Nat, i < r ∧ ∃ z : ℤ,
      S.endpoint i-max ((q : ℝ)*alpha-p) 0 ≤ theta+(s : ℝ)*alpha-z ∧
      theta+(s : ℝ)*alpha-z < S.endpoint i-max ((q : ℝ)*alpha-p) 0+|(q : ℝ)*alpha-p| := by
  let x := theta+(s : ℝ)*alpha
  let delta := (q : ℝ)*alpha-p
  have hshift : S.value (x+delta) = S.value (theta+((s+q : Nat) : ℝ)*alpha) := by
    calc
      S.value (x+delta) = S.value ((x+delta)+(p : ℝ)) := (S.periodic (x+delta) p).symm
      _ = S.value (theta+((s+q : Nat) : ℝ)*alpha) := by
        congr 1
        dsimp [x,delta]
        push_cast
        ring
  have hmis : S.value x ≠ S.value (x+delta) := by
    intro h
    apply hb
    change S.value (theta+((s+q : Nat) : ℝ)*alpha) = S.value x
    rw [← hshift]
    exact h.symm
  change 0 < |delta| at hepsilon
  change ∃ i : Nat, i < r ∧ ∃ z : ℤ,
    S.endpoint i-max delta 0 ≤ x-z ∧ x-z < S.endpoint i-max delta 0+|delta|
  by_cases hd : 0 < delta
  · obtain ⟨i,hi,z,hlo,hhi⟩ := crossing S x (x+delta) (by linarith) hmis
    refine ⟨i,hi,z,?_,?_⟩
    · rw [max_eq_left hd.le]
      linarith
    · rw [max_eq_left hd.le,abs_of_pos hd]
      linarith
  · have hdle : delta ≤ 0 := le_of_not_gt hd
    have ha : |delta| = -delta := abs_of_nonpos hdle
    have hdneg : delta < 0 := by rw [ha] at hepsilon; linarith
    obtain ⟨i,hi,z,hlo,hhi⟩ := crossing S (x+delta) x (by linarith) (Ne.symm hmis)
    refine ⟨i,hi,z,?_,?_⟩
    · rw [max_eq_right hdle]
      linarith
    · rw [max_eq_right hdle,ha]
      linarith

/-- Classical labels/lifts are chosen only for genuine breaks; nonbreaks receive unused defaults. -/
theorem lift_cover {r : Nat} (S : StepCode r) (alpha theta : ℝ) (q : Nat) (p : ℤ)
    (hepsilon : 0 < |(q : ℝ)*alpha-p|) :
    ∃ label : Nat → Nat, ∃ lift : Nat → ℤ,
      ArcCover.LiftCover (orbit S alpha theta) q r alpha theta |(q : ℝ)*alpha-p|
        (fun i => S.endpoint i-max ((q : ℝ)*alpha-p) 0) label lift := by
  have hw : ∀ s : Nat, ∃ i : Nat, ∃ z : ℤ,
      orbit S alpha theta (s+q) ≠ orbit S alpha theta s →
      i < r ∧ S.endpoint i-max ((q : ℝ)*alpha-p) 0 ≤ theta+(s : ℝ)*alpha-z ∧
        theta+(s : ℝ)*alpha-z < S.endpoint i-max ((q : ℝ)*alpha-p) 0+|(q : ℝ)*alpha-p| := by
    intro s
    by_cases hb : orbit S alpha theta (s+q) ≠ orbit S alpha theta s
    · obtain ⟨i,hi,z,hlo,hhi⟩ := break_has_lift S alpha theta q p hepsilon s hb
      exact ⟨i,z,fun _ => ⟨hi,hlo,hhi⟩⟩
    · exact ⟨0,0,fun h => False.elim (hb h)⟩
  let label : Nat → Nat := fun s => Classical.choose (hw s)
  let lift : Nat → ℤ := fun s => Classical.choose (Classical.choose_spec (hw s))
  refine ⟨label,lift,?_⟩
  intro s hb
  exact (Classical.choose_spec (Classical.choose_spec (hw s))) hb

/-- The one-scale exclusion now needs the explicit finite-step interface, not an assumed mismatch cover. -/
theorem no_repeat_bound {r : Nat} (S : StepCode r) (alpha theta : ℝ) (q C : Nat) (p u v : ℤ)
    (hq : 0 < q) (hbezout : u*p+v*(q : ℤ) = 1)
    (hepsilon : 0 < |(q : ℝ)*alpha-p|)
    (hscale : (((2^(r+1)*(q+C+2) : Nat) : ℝ)+q)*|(q : ℝ)*alpha-p| ≤ 1) :
    ¬ ArcBreakSequence.RepeatBound (orbit S alpha theta) q C := by
  obtain ⟨label,lift,hc⟩ := lift_cover S alpha theta q p hepsilon
  exact ArcCover.no_repeat_of_cover (orbit S alpha theta) q C r alpha theta p u v
    (fun i => S.endpoint i-max ((q : ℝ)*alpha-p) 0) label lift hq hbezout hepsilon hc hscale

#print axioms ArcStepCode.crossing
#print axioms ArcStepCode.break_has_lift
#print axioms ArcStepCode.lift_cover
#print axioms ArcStepCode.no_repeat_bound

end ArcStepCode
