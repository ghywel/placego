import ArcBreakBounds

/-!
# Constructing bounded successive breaks from a repeat obstruction

A core-Lean component of the arc-code argument. The repeat obstruction is an explicit hypothesis, not a
Rule30 theorem proved here. Classical choice selects a break in a bounded interval. No least-witness,
adaptive-search or efficient observer claim is made. Geometry, integer return spacing and the actual
Rule30/continued-fraction interfaces remain separate obligations.
-/

namespace ArcBreakSequence

/-- A matching window from a to b must end by 2a+q+C. -/
def RepeatBound (c : Nat → Bool) (q C : Nat) : Prop :=
  ∀ a b, a ≤ b → (∀ s, a ≤ s → s ≤ b → c (s+q) = c s) → b ≤ 2*a+q+C

/-- There is a genuine break in every explicitly bounded forward window. -/
theorem future_break (c : Nat → Bool) (q C : Nat) (hr : RepeatBound c q C) (a : Nat) :
    ∃ m, a ≤ m ∧ m ≤ 2*a+q+C+1 ∧ c (m+q) ≠ c m := by
  refine Classical.byContradiction fun hno => ?_
  have heq : ∀ s, a ≤ s → s ≤ 2*a+q+C+1 → c (s+q) = c s := by
    intro s hs ht
    by_cases h : c (s+q) = c s
    · exact h
    · exact False.elim (hno ⟨s,hs,ht,h⟩)
  have h := hr a (2*a+q+C+1) (by omega) heq
  omega

noncomputable def nextBreak (c : Nat → Bool) (q C : Nat) (hr : RepeatBound c q C) (a : Nat) : Nat :=
  Classical.choose (future_break c q C hr a)

theorem nextBreak_spec (c : Nat → Bool) (q C : Nat) (hr : RepeatBound c q C) (a : Nat) :
    a ≤ nextBreak c q C hr a ∧ nextBreak c q C hr a ≤ 2*a+q+C+1 ∧
      c (nextBreak c q C hr a+q) ≠ c (nextBreak c q C hr a) :=
  Classical.choose_spec (future_break c q C hr a)

noncomputable def sequence (c : Nat → Bool) (q C : Nat) (hr : RepeatBound c q C) : Nat → Nat
  | 0 => nextBreak c q C hr 0
  | k+1 => nextBreak c q C hr (sequence c q C hr k+1)

theorem sequence_break (c : Nat → Bool) (q C : Nat) (hr : RepeatBound c q C) (k : Nat) :
    c (sequence c q C hr k+q) ≠ c (sequence c q C hr k) := by
  cases k with
  | zero => exact (nextBreak_spec c q C hr 0).2.2
  | succ k => exact (nextBreak_spec c q C hr (sequence c q C hr k+1)).2.2

theorem sequence_increasing (c : Nat → Bool) (q C : Nat) (hr : RepeatBound c q C) (k : Nat) :
    sequence c q C hr k < sequence c q C hr (k+1) := by
  change sequence c q C hr k < nextBreak c q C hr (sequence c q C hr k+1)
  have h := (nextBreak_spec c q C hr (sequence c q C hr k+1)).1
  omega

theorem sequence_strict (c : Nat → Bool) (q C : Nat) (hr : RepeatBound c q C)
    {i j : Nat} (hij : i < j) : sequence c q C hr i < sequence c q C hr j := by
  obtain ⟨n,rfl⟩ := Nat.exists_eq_add_of_le (Nat.succ_le_of_lt hij)
  induction n with
  | zero => simpa using sequence_increasing c q C hr i
  | succ n ih => exact Nat.lt_trans (ih (by omega)) (sequence_increasing c q C hr (i+1+n))

theorem sequence_first (c : Nat → Bool) (q C : Nat) (hr : RepeatBound c q C) :
    sequence c q C hr 0 ≤ q+C+1 := by
  simpa [sequence] using (nextBreak_spec c q C hr 0).2.1

theorem sequence_step_bound (c : Nat → Bool) (q C : Nat) (hr : RepeatBound c q C) (k : Nat) :
    sequence c q C hr (k+1) ≤ 2*sequence c q C hr k+q+C+3 := by
  change nextBreak c q C hr (sequence c q C hr k+1) ≤ _
  have h := (nextBreak_spec c q C hr (sequence c q C hr k+1)).2.1
  omega

/-- Every genuine break belongs to one of r labels, with a lower bound on same-label gaps. -/
def LabelSpacing (c : Nat → Bool) (q r spacing : Nat) : Prop :=
  ∃ colour : Nat → Nat,
    (∀ s, c (s+q) ≠ c s → colour s < r) ∧
    (∀ s t, s < t → c (s+q) ≠ c s → c (t+q) ≠ c t →
      colour s = colour t → spacing ≤ t-s)

/-- The physical repeat obstruction and labelled break spacing imply the numerical arc bound. -/
theorem labelled_spacing_bound (c : Nat → Bool) (q C r spacing : Nat)
    (hr : RepeatBound c q C) (hl : LabelSpacing c q r spacing) :
    spacing < 2^(r+1)*(q+C+2) := by
  obtain ⟨colour,hcolour,hgap⟩ := hl
  apply ArcBreakBounds.spacing_bound q C r spacing (sequence c q C hr)
    (fun k => colour (sequence c q C hr k))
    (sequence_first c q C hr) (sequence_step_bound c q C hr)
  · intro k _
    exact hcolour _ (sequence_break c q C hr k)
  · intro i j hij _ he
    exact hgap _ _ (sequence_strict c q C hr hij)
      (sequence_break c q C hr i) (sequence_break c q C hr j) he

#print axioms ArcBreakSequence.future_break
#print axioms ArcBreakSequence.sequence_break
#print axioms ArcBreakSequence.sequence_strict
#print axioms ArcBreakSequence.labelled_spacing_bound

end ArcBreakSequence
