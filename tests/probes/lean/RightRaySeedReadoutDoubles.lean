import RightRaySeedReadout

/-! The half-speed white readout applied to a full return of the lower
singleton register. The familiar period-lift criterion credits the kit's
TFunctionCycles.lift_iff. The new conclusion concerns a word on the moving
ray rather than a direct inspection of the newly retained bit. -/

namespace RightRaySeedReadoutDoubles
open RightRayWhiteCone RightRayProbe RightRayRooted RightRayFollowerProbe RightRaySeedReadout

def Returns (D t : Nat) : Prop := AgreesBelow single (orbit single t) (D : Int)

private theorem exterior : ∀ i : Int, i < 0 → single i = false := by
  intro i hi; simp [single,show i ≠ 0 by omega]

private theorem multiples {D P : Nat} (h : Returns D P) (q : Nat) : Returns D (P*q) := by
  induction q with
  | zero => rw [Nat.mul_zero]; exact fun _ _ => rfl
  | succ q ih =>
    intro i hi
    rw [Nat.mul_succ,orbit_add]
    exact ((agreed_orbit ih P) i hi).trans (h i hi)

private theorem late (D P T : Nat) : ∃ s,
    AgreesBelow (orbit single P) (orbit single (s+T)) (D:Int) := by
  have hpos : 0 < 2^D := Nat.pow_pos (by omega)
  have hT : T ≤ T*2^D := by
    calc
      T = T*1 := by simp
      _ ≤ T*2^D := Nat.mul_le_mul_left T hpos
  refine ⟨P+T*2^D-T,?_⟩
  intro i hi
  rw [show P+T*2^D-T+T = P+T*2^D by omega]
  exact RightRayProbeTime.period_mul
    (f := fun t => orbit single t i)
    (fun t => RightRayPeriodBridge.low_period single exterior D t i hi) P T

/-- P is a positive return time characterizing precisely all returns of
the lower 4m-bit register. The optional final white occurs for some genuine
singleton launch exactly when the next coordinate is black at this return. -/
theorem extra_white_iff (m P : Nat) (hm : 0<m) (_hpos : 0<P)
    (hP : ∀ t, Returns (4*m) t ↔ P ∣ t) :
    (∃ s, ∀ r, r ≤ 2*m → sample s m r = false) ↔
      orbit single P ((4*m:Nat):Int) = true := by
  have retP : Returns (4*m) P := (hP P).mpr (Nat.dvd_refl _)
  constructor
  · rintro ⟨s,hw⟩
    have hshort : ∀ r, r<2*m → sample s m r=false := fun r hr => hw r (by omega)
    have ret : Returns (4*m) (s+6*m) := (block_iff_return s m hm).mp hshort
    have hon := (next_record s m hm hshort).mp (hw (2*m) (by omega))
    cases hbit : orbit single P ((4*m:Nat):Int) with
    | true => rfl
    | false =>
      have big : Returns (4*m+1) P := by
        intro i hi
        by_cases hlt : i<((4*m:Nat):Int)
        · exact retP i hlt
        · have he : i=((4*m:Nat):Int) := by omega
          rw [he,hbit]
          simp [single,show ((4*m:Nat):Int) ≠ 0 by omega]
      obtain ⟨q,hq⟩ := (hP _).mp ret
      have allret : Returns (4*m+1) (s+6*m) := by rw [hq]; exact multiples big q
      have ho := allret ((4*m:Nat):Int) (by omega)
      change orbit single (s+6*m) ((4*m:Nat):Int) = true at hon
      rw [ho] at hon
      simp [single,show ((4*m:Nat):Int) ≠ 0 by omega] at hon
  · intro hb
    obtain ⟨s,h⟩ := late (4*m+1) P (6*m)
    have hs : Returned s m := fun i hi => (h i (by omega)).trans (retP i hi)
    have hshort := (block_iff_return s m hm).mpr hs
    have hnew : cut s m ((4*m:Nat):Int) = true := (h _ (by omega)).trans hb
    refine ⟨s,fun r hr => ?_⟩
    by_cases hlt : r < 2*m
    · exact hshort r hlt
    · rw [show r = 2*m by omega]
      exact (next_record s m hm hshort).mpr hnew

#print axioms extra_white_iff
end RightRaySeedReadoutDoubles
