private def blocker (shift width value : Nat) : List Nat :=
  (List.range width).map fun i => mkLit (shift + i) (!value.testBit i)

private noncomputable def occurrenceBlocker (entry : Nat × Nat) : List Nat :=
  blocker entry.1 (factorWidth entry.2) (factorValue entry.2)

private theorem blocker_models (x : Int → Bool) (origin : Int) {shift width value : Nat}
    (hm : ¬ Matches x (origin + (shift : Int)) width value) :
    Models (fun j => x (origin + (j : Int))) (blocker shift width value) := by
  classical
  have hd : ∃ i, i < width ∧ x (origin + (shift : Int) + (i : Int)) ≠ value.testBit i := by
    apply Classical.byContradiction
    intro h
    apply hm
    intro i hi
    apply Classical.byContradiction
    intro hv
    exact h ⟨i, hi, hv⟩
  rcases hd with ⟨i, hi, hd⟩
  refine ⟨mkLit (shift+i) (!value.testBit i), ?_, ?_⟩
  · exact List.mem_map.mpr ⟨i, List.mem_range.mpr hi, rfl⟩
  · apply (lit_mk _ _ _).mpr
    change x (origin + ((shift+i : Nat) : Int)) = !value.testBit i
    have he : origin + ((shift+i : Nat) : Int) = origin + (shift : Int) + (i : Int) := by omega
    rw [he]
    cases hx : x (origin + (shift : Int) + (i : Int)) <;> cases hb : value.testBit i <;> simp_all
