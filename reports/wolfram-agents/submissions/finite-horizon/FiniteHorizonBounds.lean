/-!
# Finite comparison deadlines for the mechanical-word horizon

Uncompiled staging component, GC2136. This proves no rotation or Rule30 theorem.
The repeat obstruction is supplied only through inclusive index N. Integer-valued
c and z expose the carry-difference identity without assuming a mechanical orbit.
The physical and sharp continued-fraction interfaces remain separate obligations.
-/

namespace FiniteHorizonBounds

/-- All comparisons used in the obstruction must fit in the supplied prefix. -/
def RepeatBoundThrough {α : Type} (c : Nat → α) (N C : Nat) : Prop :=
  ∀ q a b, 0 < q → a ≤ b → b+q ≤ N →
    (∀ s, a ≤ s → s ≤ b → c (s+q) = c s) → b ≤ 2*a+q+C

/-- The finite counterpart of the delivered global future-break constructor. -/
theorem future_break {α : Type} (c : Nat → α) (N C q a : Nat)
    (hr : RepeatBoundThrough c N C) (hq : 0 < q)
    (hdeadline : 2*a+2*q+C+1 ≤ N) :
    ∃ m, a ≤ m ∧ m ≤ 2*a+q+C+1 ∧ c (m+q) ≠ c m := by
  apply Classical.byContradiction
  intro hno
  have heq : ∀ s, a ≤ s → s ≤ 2*a+q+C+1 → c (s+q) = c s := by
    intro s hs hb
    by_cases h : c (s+q) = c s
    · exact h
    · exact False.elim (hno ⟨s,hs,hb,h⟩)
  have hb := hr q a (2*a+q+C+1) hq (by omega) (by omega) heq
  omega

/-- A zero carry at two consecutive indices makes the compared letters equal. -/
theorem equal_of_zero_carry (c z : Nat → Int) (q s : Nat)
    (hid : c (s+q)-c s = z (s+1)-z s)
    (h0 : z s = 0) (h1 : z (s+1) = 0) : c (s+q) = c s := by
  rw [h0,h1] at hid
  omega

/-- Some nonzero carry must occur by q+C+2, using only the finite prefix. -/
theorem first_carry (c z : Nat → Int) (N C q : Nat)
    (hr : RepeatBoundThrough c N C) (hq : 0 < q)
    (hid : ∀ s, c (s+q)-c s = z (s+1)-z s)
    (hdeadline : 2*q+C+1 ≤ N) :
    ∃ h, h ≤ q+C+2 ∧ z h ≠ 0 := by
  apply Classical.byContradiction
  intro hno
  have hz : ∀ s, s ≤ q+C+2 → z s = 0 := by
    intro s hs
    by_cases h : z s = 0
    · exact h
    · exact False.elim (hno ⟨s,hs,h⟩)
  have heq : ∀ s, 0 ≤ s → s ≤ q+C+1 → c (s+q) = c s := by
    intro s _ hs
    exact equal_of_zero_carry c z q s (hid s) (hz s (by omega)) (hz (s+1) (by omega))
  have hb := hr q 0 (q+C+1) hq (by omega) (by omega) heq
  omega

/-- A second nonzero carry has a finite deadline after any bounded first one. -/
theorem next_carry (c z : Nat → Int) (N C q h : Nat)
    (hr : RepeatBoundThrough c N C) (hq : 0 < q)
    (hid : ∀ s, c (s+q)-c s = z (s+1)-z s)
    (hh : h ≤ q+C+2) (hdeadline : 4*q+3*C+8 ≤ N) :
    ∃ k, h < k ∧ k ≤ 2*h+q+C+4 ∧ z k ≠ 0 := by
  apply Classical.byContradiction
  intro hno
  have hz : ∀ s, h < s → s ≤ 2*h+q+C+4 → z s = 0 := by
    intro s hs hb
    by_cases h : z s = 0
    · exact h
    · exact False.elim (hno ⟨s,hs,hb,h⟩)
  have heq : ∀ s, h+1 ≤ s → s ≤ 2*h+q+C+3 → c (s+q) = c s := by
    intro s hs hb
    exact equal_of_zero_carry c z q s (hid s) (hz s (by omega) (by omega))
      (hz (s+1) (by omega) (by omega))
  have hb := hr q (h+1) (2*h+q+C+3) hq (by omega) (by omega) heq
  omega

/-- A separately supplied sharp return gap bounds the next denominator. -/
theorem denominator_growth (c z : Nat → Int) (N C q Q : Nat)
    (hr : RepeatBoundThrough c N C) (hq : 0 < q)
    (hid : ∀ s, c (s+q)-c s = z (s+1)-z s)
    (hdeadline : 4*q+3*C+8 ≤ N)
    (hgap : ∀ h k, h < k → z h ≠ 0 → z k ≠ 0 → h+Q ≤ k) :
    ∃ h, z h ≠ 0 ∧ h ≤ q+C+2 ∧ Q ≤ h+q+C+4 ∧ Q ≤ 2*q+2*C+6 := by
  obtain ⟨h,hh,hz⟩ := first_carry c z N C q hr hq hid (by omega)
  obtain ⟨k,hk,hku,hzk⟩ := next_carry c z N C q h hr hq hid hh hdeadline
  have hsep := hgap h k hk hz hzk
  exact ⟨h,hz,hh,by omega,by omega⟩

/-- Scope control: a zero-length horizon supplies no global future-break conclusion. -/
theorem zero_horizon_control (C : Nat) :
    RepeatBoundThrough (fun _ : Nat => (0 : Int)) 0 C ∧
    ¬ ∃ m : Nat, (fun _ : Nat => (0 : Int)) (m+1) ≠ (fun _ : Nat => (0 : Int)) m := by
  constructor
  · intro q a b hq hab hN heq
    omega
  · intro ⟨m,hm⟩
    exact hm rfl

#print axioms FiniteHorizonBounds.future_break
#print axioms FiniteHorizonBounds.equal_of_zero_carry
#print axioms FiniteHorizonBounds.first_carry
#print axioms FiniteHorizonBounds.next_carry
#print axioms FiniteHorizonBounds.denominator_growth
#print axioms FiniteHorizonBounds.zero_horizon_control

end FiniteHorizonBounds
