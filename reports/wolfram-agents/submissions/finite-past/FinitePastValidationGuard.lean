module
public import Rule30Submission

/-!
GC2295: UNCOMPILED development guards for the assembled finite-past source.
No compiler/replay outcome is claimed. Literal rows below are independent of
allRows/framedRow. The boundary counterexample is an actual infinite parent;
it detects omission of the white-right hypothesis. Keep this module outside
the submission. Compile only in a separately frozen compatible-toolchain stage.
-/
@[expose] public section
namespace FinitePastValidationGuard
open Ruliology.CellularAutomata.Rule30Jen
open Ruliology.CellularAutomata.Rule30Realization
open Ruliology.CellularAutomata.Rule30FinitePastDraft

def one (i : Int) : Bool := decide (i=0)
def two (i : Int) : Bool := decide (i=0 ∨ i=1)
def three (i : Int) : Bool := decide (i=0 ∨ i=1 ∨ i=2)
def gap (i : Int) : Bool := decide (i=0 ∨ i=2)
def word1001 (i : Int) : Bool := decide (i=0 ∨ i=3)
def word1011 (i : Int) : Bool := decide (i=0 ∨ i=2 ∨ i=3)
def word1101 (i : Int) : Bool := decide (i=0 ∨ i=1 ∨ i=3)
def word1111 (i : Int) : Bool := decide (0≤i ∧ i≤3)
def physicalThree (i : Int) : Bool := decide (i= -1 ∨ i=0 ∨ i=1)
def physicalPairImage (i : Int) : Bool := decide (i= -1 ∨ i=0 ∨ i=2)
def halfLine (i : Int) : Bool := decide (1≤i)

theorem one_span : Span one 0 0 := by
  refine ⟨by omega,by decide,by decide,?_,?_⟩
  · intro i hi; simp [one]; omega
  · intro i hi; simp [one]; omega

theorem two_span : Span two 0 1 := by
  refine ⟨by omega,by decide,by decide,?_,?_⟩
  · intro i hi; simp [two]; omega
  · intro i hi; simp [two]; omega

theorem three_span : Span three 0 2 := by
  refine ⟨by omega,by decide,by decide,?_,?_⟩
  · intro i hi; simp [three]; omega
  · intro i hi; simp [three]; omega

theorem gap_span : Span gap 0 2 := by
  refine ⟨by omega,by decide,by decide,?_,?_⟩
  · intro i hi; simp [gap]; omega
  · intro i hi; simp [gap]; omega

theorem word1001_span : Span word1001 0 3 := by
  refine ⟨by omega,by decide,by decide,?_,?_⟩
  · intro i hi; simp [word1001]; omega
  · intro i hi; simp [word1001]; omega

theorem word1011_span : Span word1011 0 3 := by
  refine ⟨by omega,by decide,by decide,?_,?_⟩
  · intro i hi; simp [word1011]; omega
  · intro i hi; simp [word1011]; omega

theorem word1101_span : Span word1101 0 3 := by
  refine ⟨by omega,by decide,by decide,?_,?_⟩
  · intro i hi; simp [word1101]; omega
  · intro i hi; simp [word1101]; omega

theorem word1111_span : Span word1111 0 3 := by
  refine ⟨by omega,by decide,by decide,?_,?_⟩
  · intro i hi; simp [word1111]; omega
  · intro i hi; simp [word1111]; omega

/-- The all-white fixed point is deliberately outside the root domain. -/
theorem white_control (n : Nat) :
    evol (fun _ => false) n=(fun _ => false) ∧ ¬ Root (fun _ => false) := by
  refine ⟨evol_zero n,?_⟩
  intro h
  exact zero_not_finite_nonzero h.1

theorem small_roots : Root one ∧ Root two :=
  ⟨small_span_root one_span (by decide),small_span_root two_span (by decide)⟩

/-- Inherited physical endpoint guard, distinct from normalization. -/
theorem seed_step_span : Span (evol one 1) (-1) 1 := span_step one_span

/-- Literal physical image, including the negative site. -/
theorem one_physical_step : evol one 1=physicalThree := by
  funext i
  by_cases hm : i= -1
  · subst i; decide
  by_cases hz : i=0
  · subst i; decide
  by_cases hp : i=1
  · subst i; decide
  have ha : i-1≠0 := by omega
  have hc : i+1≠0 := by omega
  simp [evol,rule,one,physicalThree,hm,hz,hp,ha,hc]

/-- A wrong normalization sign fails this literal equality. -/
theorem one_normalized_step : normalizedImage 1 one=three := by
  funext i
  change evol one 1 (i-1)=three i
  rw [one_physical_step]
  have h : (i-1= -1 ∨ i-1=0 ∨ i-1=1) ↔ (i=0 ∨ i=1 ∨ i=2) := by omega
  simp only [physicalThree,three,h]

theorem two_physical_step : evol two 1=physicalPairImage := by
  funext i
  by_cases hm : i= -1
  · subst i; decide
  by_cases hz : i=0
  · subst i; decide
  by_cases h1 : i=1
  · subst i; decide
  by_cases h2 : i=2
  · subst i; decide
  have ha : ¬(i-1=0 ∨ i-1=1) := by omega
  have hb : ¬(i=0 ∨ i=1) := by omega
  have hc : ¬(i+1=0 ∨ i+1=1) := by omega
  simp [evol,rule,two,physicalPairImage,hm,hz,h2,ha,hb,hc]

theorem two_normalized_step : normalizedImage 1 two=word1101 := by
  funext i
  change evol two 1 (i-1)=word1101 i
  rw [two_physical_step]
  have h : (i-1= -1 ∨ i-1=0 ∨ i-1=2) ↔ (i=0 ∨ i=1 ∨ i=3) := by omega
  simp only [physicalPairImage,word1101,h]

theorem zero_step_image (x : Int → Bool) : normalizedImage 0 x=x := by
  funext i
  simp [normalizedImage,translate,evol]

theorem zero_step_past (x : Int → Bool) : Past 0 x ↔ FiniteNonzero x := by
  constructor
  · rintro ⟨p,hp,he⟩
    change p=x at he
    rw [he] at hp
    exact hp
  · intro hx
    exact ⟨x,hx,rfl⟩

theorem zero_width_empty : allRows 0=[] ∧ ∀ x, ¬ Normal 0 x := by
  refine ⟨rfl,?_⟩
  intro x hx
  have := normal_positive hx
  omega

/-- An actual finite white-right predecessor exercises the conditional test. -/
theorem finite_boundary_control :
    evol (translate 1 one) 1=three ∧
    (∀ i : Int, 2≤i → translate 1 one i=false) ∧
    (FiniteNonzero (translate 1 one) ↔
      three 1=true ∧ translate 1 one 1=true) := by
  have he : evol (translate 1 one) 1=three :=
    (evol_translate 1 one 1).trans one_normalized_step
  have hr : ∀ i : Int, 2≤i → translate 1 one i=false := by
    intro i hi
    simp [translate,one]
    omega
  exact ⟨he,hr,Rule30Submission.finite_parent_test three_span he hr⟩

/-- The physical root of111 at0..2 is the singleton at1, with age exactly1. -/
theorem literal_root_age :
    Root (translate 1 one) ∧ evol (translate 1 one) 1=three ∧
    ∀ x n, Root x → evol x n=three → x=translate 1 one ∧ n=1 := by
  have hr : Root (translate 1 one) :=
    small_span_root (translate_span 1 one_span) (by decide)
  have he := finite_boundary_control.1
  refine ⟨hr,he,?_⟩
  intro x n hx hn
  exact root_unique hx hr hn he

/-- No arbitrary infinite parent can be smuggled in by dropping the right tail. -/
theorem halfLine_step : evol halfLine 1=two := by
  funext i
  by_cases hz : i=0
  · subst i; decide
  by_cases h1 : i=1
  · subst i; decide
  have cases : i<0 ∨ 1<i := by omega
  rcases cases with hi | hi
  · have ha : ¬1≤i-1 := by omega
    have hb : ¬1≤i := by omega
    have hc : ¬1≤i+1 := by omega
    simp [evol,rule,halfLine,two,ha,hb,hc,hz,h1]
  · have ha : 1≤i-1 := by omega
    have hb : 1≤i := by omega
    have hc : 1≤i+1 := by omega
    simp [evol,rule,halfLine,two,ha,hb,hc,hz,h1]

theorem halfLine_not_finite : ¬ FiniteNonzero halfLine := by
  rintro ⟨l,r,h⟩
  have hw := h.right_white (max (r+1) 1) (by omega)
  have hb : halfLine (max (r+1) 1)=true := by
    simp [halfLine] <;> omega
  rw [hb] at hw
  cases hw

theorem missing_boundary_countercontrol :
    evol halfLine 1=two ∧ two 1=true ∧ halfLine 1=true ∧
    ¬ FiniteNonzero halfLine ∧ ¬(∀ i : Int, 1≤i → halfLine i=false) := by
  refine ⟨halfLine_step,by decide,by decide,halfLine_not_finite,?_⟩
  intro h
  have := h 1 (by omega)
  change true=false at this
  cases this

/-- Width-three words really are the literal 101 and 111, both represented. -/
theorem width_three_control :
    gap ∈ allRows 3 ∧ three ∈ allRows 3 ∧
    (allRows 3).Nodup ∧ (allRows 3).length=2 ∧ parentRows 3=[three] := by
  refine ⟨(mem_allRows 3 gap).mpr gap_span,(mem_allRows 3 three).mpr three_span,
    allRows_nodup 3,?_,?_⟩
  · exact allRows_length 3
  · change [normalizedImage 1 one]=[three]
    rw [one_normalized_step]

/-- Independent literal width-four representatives all occur without duplicates. -/
theorem width_four_members :
    word1001 ∈ allRows 4 ∧ word1011 ∈ allRows 4 ∧
    word1101 ∈ allRows 4 ∧ word1111 ∈ allRows 4 ∧
    (allRows 4).Nodup ∧ (allRows 4).length=4 :=
  ⟨(mem_allRows 4 word1001).mpr word1001_span,
    (mem_allRows 4 word1011).mpr word1011_span,
    (mem_allRows 4 word1101).mpr word1101_span,
    (mem_allRows 4 word1111).mpr word1111_span,
    allRows_nodup 4,allRows_length 4⟩

theorem empty_frame_is_two : framedRow []=two := by
  funext i
  by_cases h0 : i=0
  · subst i; decide
  by_cases h1 : i=1
  · subst i; decide
  have hi : ¬(0<i ∧ i<1) := by omega
  simp [framedRow,two,h0,h1,hi]

/-- The sole width-four finite-parent word is 1101, not its reflection. -/
theorem width_four_parent_list : parentRows 4=[word1101] := by
  change [normalizedImage 1 (framedRow [])]=[word1101]
  rw [empty_frame_is_two,two_normalized_step]

theorem width_four_parent_iff (y : Int → Bool) :
    (Normal 4 y ∧ Past 1 y) ↔ y=word1101 := by
  rw [← mem_parentRows,width_four_parent_list,List.mem_singleton]

theorem gap_no_past : ¬ Past 1 gap := by
  intro h
  have hm := (mem_parentRows 3 gap).mpr ⟨gap_span,h⟩
  rw [width_three_control.2.2.2.2,List.mem_singleton] at hm
  have same := congrFun hm 1
  change false=true at same
  cases same

#print axioms Rule30Submission.finite_root_age
#print axioms Rule30Submission.finite_parent_test
#print axioms Rule30Submission.normalized_ancestor_bijection
#print axioms Rule30Submission.finite_word_enumeration
#print axioms Rule30Submission.finite_parent_enumeration
#print axioms Rule30Submission.finite_parent_count
#print axioms Rule30Submission.finite_parent_small_widths
#print axioms white_control
#print axioms small_roots
#print axioms one_physical_step
#print axioms one_normalized_step
#print axioms two_normalized_step
#print axioms zero_step_image
#print axioms zero_step_past
#print axioms zero_width_empty
#print axioms finite_boundary_control
#print axioms literal_root_age
#print axioms missing_boundary_countercontrol
#print axioms width_three_control
#print axioms width_four_members
#print axioms width_four_parent_list
#print axioms width_four_parent_iff
#print axioms gap_no_past
end FinitePastValidationGuard
