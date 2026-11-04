import TwoPairs

/-! At a depth of at least five, the six original cells ending at a wall
that retreats three places must read `#...##` from shallow to deep. -/
namespace TwoPairs.Retreat

/-- An alternating tail above one wall excludes every higher wall. -/
private theorem excludes_higher {x : Row} {d e : Nat} (h : Top x d) (lt : d < e) : ¬Top x e := by
  intro upper
  have alt := h.2 e (by omega)
  rw [upper.1] at alt
  cases b : x e <;> simp [b] at alt

private theorem both_false {u v : Bool} (h : (u || v) = false) : u = false ∧ v = false := by
  cases u <;> cases v <;> simp_all

theorem marker {x : Row} (k : Nat) (a : Top x (k+5)) (b : Top (step x) (k+2)) :
    seg x (k+1) 6 = [true,false,false,false,true,true] := by
  have h5 : x (k+5) = true := by
    cases h : x (k+5) with
    | true => rfl
    | false => exact False.elim (excludes_higher b (by omega) (top_up a h).1)
  have white : (x (k+4) || x (k+3)) = false := by
    cases h : x (k+4) || x (k+3) with
    | false => rfl
    | true => exact False.elim (excludes_higher b (by omega) (top_stay a h5 h).1)
  obtain ⟨h4,h3⟩ := both_false white
  have h2 : x (k+2) = false := by
    cases h : x (k+2) with
    | false => rfl
    | true => exact False.elim (excludes_higher b (by omega) (top_minus_one a h5 h4 h3 h).1)
  have h1 : x (k+1) = true := by
    cases h : x (k+1) with
    | true => rfl
    | false => exact False.elim (excludes_higher b (by omega) (top_minus_two a h5 h4 h3 h2 h).1)
  have h6 : x (k+6) = true := a.1.trans h5
  change [x (k+1), x (k+2), x (k+3), x (k+4), x (k+5), x (k+6)] = _
  rw [h1,h2,h3,h4,h5,h6]

#print axioms marker
end TwoPairs.Retreat
