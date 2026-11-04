import MergePassage

namespace WhiteParentPin

def splice (j : Nat) (l r : Row) : Row := fun k => if k<j then l k else r k

/-- The isolated input rows are in the same spatial coordinates. If their
supports are still separated by the update cone, join first or evolve first. -/
theorem splice_update {j : Nat} {l r : Row} (hj : 2 ≤ j)
    (left : ∀ k, j ≤ k+2 → l k = false) (right : ∀ k, k<j → r k = false) :
    wall (splice j l r) = splice j (wall l) (wall r) := by
  funext k
  by_cases hk : k<j
  · have low : Agree j (splice j l r) l := by
      intro v hv
      simp [splice,hv]
    simpa [splice,hk] using (wall_causal low k hk)
  · have near (v : Nat) (hv : j ≤ v+2) : splice j l r v = r v := by
      by_cases h : v<j
      · simp [splice,h,left v hv,right v h]
      · simp [splice,h]
    simp only [splice,if_neg hk]
    cases k with
    | zero => omega
    | succ k =>
      cases k with
      | zero => omega
      | succ k =>
        change xor (splice j l r k) ((splice j l r (k+1)) || (splice j l r (k+2))) =
          xor (r k) (r (k+1) || r (k+2))
        rw [near k (by omega),near (k+1) (by omega),near (k+2) (by omega)]

theorem before_contact {a l r : Nat → Row} (ha : Runs wall a) (hl : Runs wall l)
    (hr : Runs wall r) {j c : Nat} (hj : 2 ≤ j) (initial : a 0 = splice j (l 0) (r 0))
    (left : ∀ t, t<c → ∀ k, j ≤ k+2 → l t k = false)
    (right : ∀ t, t<c → ∀ k, k<j → r t k = false) :
    ∀ t, t≤c → a t = splice j (l t) (r t) := by
  intro t ht
  induction t with
  | zero => exact initial
  | succ t ih =>
    rw [ha t,hl t,hr t,ih (by omega)]
    exact splice_update hj (left t (by omega)) (right t (by omega))

/-- Protect the canonical row only up to the tick preceding its passage.
Causality transfers its subsequent hit and prevents any earlier hit. -/
theorem transfer_hit {a v y : Nat → Row} (ha : Runs wall a) (hv : Runs wall v)
    (hy : Runs wall y) {k t : Nat} (canonical : Hit a v k (t+1))
    (join : Agree (k+1) (v t) (y t)) : Hit a y k (t+1) := by
  have after := propagate wall_causal hv hy join 1
  refine ⟨fun i hi => (canonical.1 i hi).trans (after i hi), ?_⟩
  intro s hs h
  have at_t := propagate wall_causal ha hy h (t-s)
  rw [show s+(t-s)=t by omega] at at_t
  exact canonical.2 t (by omega) (fun i hi => (at_t i hi).trans (join i hi).symm)

/-- In a binary row, two alternatives have the same first difference from
the reference exactly when they also agree with one another at that wheel. -/
theorem same_front {a v y : Row} {j : Nat} (h : First j a v) :
    First j a y ↔ Agree (j+1) v y := by
  constructor
  · intro g
    apply agree_succ (fun i hi => (h.1 i hi).symm.trans (g.1 i hi))
    have d := h.2
    have e := g.2
    cases aa : a j <;> cases vv : v j <;> cases yy : y j <;> simp_all
  · intro g
    refine ⟨fun i hi => (h.1 i hi).trans (g i (by omega)), ?_⟩
    intro e
    exact h.2 (e.trans (g j (by omega)).symm)

#print axioms before_contact
#print axioms transfer_hit
#print axioms same_front
end WhiteParentPin
