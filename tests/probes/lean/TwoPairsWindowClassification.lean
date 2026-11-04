import TwoPairsSixAllLevels
import TwoPairsWindowExclusions

/-! An equal-top eleven-bit window forces perpetual +3 backward wall motion
on every anchored row with rain above it iff it forces that motion through
the first three backward steps. Exactly the 24 listed windows qualify. -/
namespace TwoPairs.WindowClassification

open Entrances WindowExclusions

def digits (w : Nat) : List Bool := (List.range 11).map (fun j => w.testBit j)

def Passage (i : Fin 1024) (r : Nat) : Prop :=
  ∀ (x : Row) (L : Nat), x 0 = true → seg x L 11 = digits (word i.val) →
    Top x (L+9) → Top (previousN x r) (L+9+3*r)

def ThroughThree (i : Fin 1024) : Prop := ∀ r, r ≤ 3 → Passage i r
def Forever (i : Fin 1024) : Prop := ∀ r, Passage i r

private theorem retained_cases : ∀ w, w ∈ retained →
    digits w ∈ B11 ∨ digits w ∈ Six.fast ∨ digits w ∈ Six.slow := by decide +kernel

private theorem previous_add (x : Row) (a b : Nat) :
    previousN x (a+b) = previousN (previousN x a) b := by
  induction a generalizing x with
  | zero => simp [previousN]
  | succ a ih =>
    rw [Nat.succ_add]
    exact ih (previous x)

private theorem front_many (r : Nat) {x : Row} {L : Nat} (h : Front x L) :
    Front (previousN x r) (L+3*r) := by
  induction r generalizing x L with
  | zero => simpa [previousN] using h
  | succ r ih =>
    have f := FrontPadding.front_back_all (step_previous x) h
    change Front (previousN (previous x) r) _
    rw [show L+3*(r+1)=(L+3)+3*r by omega]
    exact ih f

private theorem front_tops (r : Nat) {x : Row} {L : Nat} (h : Front x L) :
    Top (previousN x r) (L+9+3*r) := by
  have f := front_many r h
  have wall := chk_wall _ f.1
  rw [seg_getD _ 11 _ 9 (by decide), seg_getD _ 11 _ 10 (by decide)] at wall
  rw [show L+9+3*r=(L+3*r)+9 by omega]
  exact ⟨wall.symm, f.2⟩

private theorem fast_tops (x : Row) (L : Nat) (mem : seg x L 11 ∈ Six.fast)
    (wall : Top x (L+9)) (r : Nat) : Top (previousN x r) (L+9+3*r) := by
  have back : iter (previousN x 2) 2 = x := by simp [previousN, iter, step_previous]
  have h := Six.fast_passage (previousN x 2) L (by rw [back]; exact mem)
    (by rw [back]; exact wall.2)
  cases r with
  | zero => simpa [previousN] using wall
  | succ r =>
    cases r with
    | zero => simpa [previousN, iter, step_previous] using h.2.1
    | succ q =>
      rw [show q+1+1=2+q by omega, previous_add]
      rw [show L+9+3*(2+q)=(L+6)+9+3*q by omega]
      exact front_tops q h.2.2

private theorem slow_tops (x : Row) (L : Nat) (mem : seg x L 11 ∈ Six.slow)
    (wall : Top x (L+9)) (r : Nat) : Top (previousN x r) (L+9+3*r) := by
  have back : iter (previousN x 3) 3 = x := by simp [previousN, iter, step_previous]
  have h := Six.slow_passage (previousN x 3) L (by rw [back]; exact mem)
    (by rw [back]; exact wall.2)
  cases r with
  | zero => simpa [previousN] using wall
  | succ r =>
    cases r with
    | zero => simpa [previousN, iter, step_previous] using h.2.1
    | succ q =>
      cases q with
      | zero => simpa [previousN, iter, step_previous] using h.2.2.1
      | succ p =>
        rw [show p+1+1+1=3+p by omega, previous_add]
        rw [show L+9+3*(3+p)=(L+9)+9+3*p by omega]
        exact front_tops p h.2.2.2

theorem listed_forever (x : Row) (L : Nat) (mem : seg x L 11 ∈ B11 ++ Six.fast ++ Six.slow)
    (wall : Top x (L+9)) (r : Nat) : Top (previousN x r) (L+9+3*r) := by
  simp only [List.mem_append, or_assoc] at mem
  rcases mem with core | fast | slow
  · exact front_tops r ⟨core, wall.2⟩
  · exact fast_tops x L fast wall r
  · exact slow_tops x L slow wall r

theorem retained_forever (i : Fin 1024) (ret : word i.val ∈ retained) : Forever i := by
  intro r x L _ win wall
  rcases retained_cases _ ret with base | fast | slow
  · exact front_tops r ⟨win.symm ▸ base, wall.2⟩
  · exact fast_tops x L (win.symm ▸ fast) wall r
  · exact slow_tops x L (win.symm ▸ slow) wall r

theorem three_requires_retained (i : Fin 1024) (three : ThroughThree i) :
    word i.val ∈ retained := by
  apply Classical.byContradiction
  intro outside
  obtain ⟨x,L,r,_,hr,anchor,win,wall,fail⟩ := physical_exclusion i outside
  exact fail (three r hr x L anchor win wall)

theorem classification (i : Fin 1024) :
    (ThroughThree i ↔ Forever i) ∧ (Forever i ↔ word i.val ∈ retained) := by
  have restriction : Forever i → ThroughThree i := fun h r _ => h r
  exact ⟨⟨fun h => retained_forever i (three_requires_retained i h), restriction⟩,
    ⟨fun h => three_requires_retained i (restriction h), retained_forever i⟩⟩

theorem count : ((List.range 1024).filter (fun i => decide (word i ∈ retained))).length = 24 := by
  decide +kernel

theorem core_sizes : B11.length = 18 ∧ B11.Nodup ∧ (B11.filter (fun w => w.getD 0 false)).length = 6 := by
  decide +kernel

#print axioms count
#print axioms classification
end TwoPairs.WindowClassification
