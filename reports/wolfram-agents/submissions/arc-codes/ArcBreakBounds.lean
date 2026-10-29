/-!
# Finite-colour bounds for a sequence of breaks

Core-Lean development component for a rotation-code argument. The geometric and Rule30 hypotheses are not
proved here: the final theorem assumes the break recurrence and same-label spacing. Finiteness is on a list
of r+1 labels in 0..r-1. The duplicate-map proof follows the kit's elementary Rule30Jen pigeonhole argument.
-/

namespace ArcBreakBounds

theorem nodup_map_of_inj {α β : Type} (f : α → β) : ∀ {l : List α}, l.Nodup →
    (∀ a ∈ l, ∀ b ∈ l, f a = f b → a = b) → (l.map f).Nodup
  | [], _, _ => List.nodup_nil
  | a :: l, hl, hinj => by
    rw [List.nodup_cons] at hl
    rw [List.map_cons, List.nodup_cons]
    refine ⟨?_, nodup_map_of_inj f hl.2 fun x hx y hy =>
      hinj x (by simp [hx]) y (by simp [hy])⟩
    intro hm
    obtain ⟨b, hb, hfb⟩ := List.mem_map.1 hm
    exact hl.1 (hinj a (by simp) b (by simp [hb]) hfb.symm ▸ hb)

/-- Among r+1 labels taking values below r, two agree. -/
theorem label_collision (r : Nat) (label : Nat → Nat) (hlabel : ∀ k, k ≤ r → label k < r) :
    ∃ i j, i < j ∧ j ≤ r ∧ label i = label j := by
  refine Classical.byContradiction fun hne => ?_
  have hinj : ∀ i ∈ List.range (r+1), ∀ j ∈ List.range (r+1), label i = label j → i = j := by
    intro i hi j hj he
    simp only [List.mem_range] at hi hj
    rcases Nat.lt_trichotomy i j with h | h | h
    · exact absurd ⟨i,j,h,by omega,he⟩ hne
    · exact h
    · exact absurd ⟨j,i,h,by omega,he.symm⟩ hne
  have hnd := nodup_map_of_inj label List.nodup_range hinj
  have hlen := hnd.length_le_of_subset (l₂ := List.range r) (by
    intro x hx
    obtain ⟨k,hk,rfl⟩ := List.mem_map.1 hx
    apply List.mem_range.2
    have hklt : k < r+1 := List.mem_range.1 hk
    exact hlabel k (by omega))
  simp only [List.length_map,List.length_range] at hlen
  omega

/-- The transformed recurrence has an exact power-of-two envelope. Index0 is the first break. -/
theorem break_envelope (q C : Nat) (d : Nat → Nat)
    (hfirst : d 0 ≤ q+C+1) (hnext : ∀ k, d (k+1) ≤ 2*d k+q+C+3) :
    ∀ k, d k+(q+C+2)+1 ≤ 2^(k+1)*(q+C+2) := by
  intro k
  induction k with
  | zero => simp only [Nat.zero_add,Nat.pow_one]; omega
  | succ k ih =>
    have hn := hnext k
    have he : 2^(k+1+1)*(q+C+2) = 2*(2^(k+1)*(q+C+2)) := by
      rw [Nat.pow_succ,Nat.mul_assoc,Nat.mul_left_comm]
    rw [show k+1+1 = (k+1)+1 by omega,he]
    omega

/-- Same-label spacing cannot exceed the finite-colour break envelope. -/
theorem spacing_bound (q C r spacing : Nat) (d label : Nat → Nat)
    (hfirst : d 0 ≤ q+C+1) (hnext : ∀ k, d (k+1) ≤ 2*d k+q+C+3)
    (hlabel : ∀ k, k ≤ r → label k < r)
    (hspacing : ∀ i j, i < j → j ≤ r → label i = label j → spacing ≤ d j-d i) :
    spacing < 2^(r+1)*(q+C+2) := by
  obtain ⟨i,j,hij,hjr,he⟩ := label_collision r label hlabel
  have hs := hspacing i j hij hjr he
  have hj := break_envelope q C d hfirst hnext j
  have hp : 2^(j+1) ≤ 2^(r+1) := Nat.pow_le_pow_right (by decide) (by omega)
  have hm := Nat.mul_le_mul_right (q+C+2) hp
  omega

#print axioms ArcBreakBounds.label_collision
#print axioms ArcBreakBounds.break_envelope
#print axioms ArcBreakBounds.spacing_bound

end ArcBreakBounds
