import Lean

/-!
# Recovering a dyadic-periodic word from the half-speed ray's probe times

For each fixed suffix length, the two probe alignments visit one residue
class modulo three. Every dyadic temporal phase occurs in that class.
-/

namespace RightRayProbeTime

def Period (f : Nat → Bool) (p : Nat) : Prop := ∀ t, f (t+p) = f t

theorem period_mul {f : Nat → Bool} {p : Nat} (h : Period f p) (t q : Nat) :
    f (t+q*p) = f t := by
  induction q with
  | zero => simp
  | succ q ih =>
    rw [Nat.succ_mul, ← Nat.add_assoc, h, ih]

theorem dyadic_mod_three (D : Nat) : 2^D % 3 = 1 ∨ 2^D % 3 = 2 := by
  induction D with
  | zero => decide
  | succ D ih =>
    rw [Nat.pow_succ, Nat.mul_mod]
    rcases ih with h | h <;> rw [h] <;> decide

/-- Any specified class modulo 3 is reached arbitrarily late by adding multiples
of p when p is prime to 3. -/
theorem hits_residue (t M p r : Nat) (hp : 0 < p) (hr : r < 3) (hp3 : p%3 = 1 ∨ p%3 = 2) :
    ∃ q, 6*M+6 ≤ t+q*p ∧ (t+q*p)%3 = r := by
  let a := 6*M+6
  have large : a ≤ a*p := by
    calc
      a = a*1 := by simp
      _ ≤ a*p := Nat.mul_le_mul_left a hp
  have hbig : 6*M+6 ≤ t+a*p := by change a ≤ t+a*p; omega
  by_cases hb : (t+a*p)%3 = r
  · exact ⟨a,hbig,hb⟩
  by_cases hc : (t+a*p+p)%3 = r
  · refine ⟨a+1, ?_, ?_⟩ <;> rw [Nat.add_mul, Nat.one_mul] <;> omega
  · refine ⟨a+2, ?_, ?_⟩ <;> rw [Nat.add_mul]
    · omega
    · rcases hp3 with h | h <;> omega

/-- A single suffix length already has an even and an odd sampler whose
offsets occupy the same class modulo 3; each predicate can be recovered separately. -/
theorem recover_at_k {u v : Nat → Bool} (D : Nat) (hu : Period u (2^D))
    (hv : Period v (2^D)) {M k : Nat} (hk : k=1 ∨ k=2)
    (ha : ∀ m, M≤m →
      u (2*(3*m-k-1)) = v (2*(3*m-k-1)) ∧
      u (2*(3*m-k)+1) = v (2*(3*m-k)+1)) (t : Nat) : u t = v t := by
  let r := if k=1 then 2 else 0
  have hr : r < 3 := by dsimp [r]; split <;> omega
  obtain ⟨q,hl,hcls⟩ := hits_residue t M (2^D) r (Nat.pow_pos (by omega)) hr (dyadic_mod_three D)
  let n := t+q*2^D
  let m := n/6+1
  have hn : 6*M+6 ≤ n := hl
  have hc : n%3 = r := hcls
  have hm : M≤m := by dsimp [m]; omega
  have hp := ha m hm
  have hef : n = 2*(3*m-k-1) ∨ n = 2*(3*m-k)+1 := by
    rcases hk with hk | hk
    · subst k
      have h : n%3 = 2 := by simpa [r] using hc
      dsimp [m]; omega
    · subst k
      have h : n%3 = 0 := by simpa [r] using hc
      dsimp [m]; omega
  have he : u n = v n := by
    rcases hef with e | e
    · exact (congrArg u e).trans (hp.1.trans (congrArg v e).symm)
    · exact (congrArg u e).trans (hp.2.trans (congrArg v e).symm)
  exact (period_mul hu t q).symm.trans (he.trans (period_mul hv t q))

end RightRayProbeTime
