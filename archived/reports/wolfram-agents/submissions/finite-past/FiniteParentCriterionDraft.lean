module
public import Rule30FinitePastDraft

/-!
# The physical white-right parent's finite stopping test

UNCOMPILED source preparation, GC2288. This transcribes CL659/GC2261's
independently read test, with G121/G122 and current Preimages/ZeroBoundary
credited in GC2282. The parent is an actual physical predecessor with a fixed
white right tail, not a freely chosen wall-frame parent. Existence/construction
of that canonical parent is already provided by Preimages; no replacement
constructor or all-depth infinite-tail theorem is asserted here.
-/

@[expose] public section
namespace Ruliology.CellularAutomata.Rule30FinitePastDraft
open Rule30Jen Rule30Realization

/-- Under a white output half-line, two adjacent white parent cells propagate
white indefinitely to the left. This is the physical inverse stopping rule. -/
theorem white_left_from_pair {p y : Int → Bool} {l : Int}
    (he : evol p 1=y) (hy : ∀ i, i<l → y i=false)
    (h0 : p l=false) (h1 : p (l-1)=false) : ∀ i, i≤l → p i=false := by
  have down : ∀ n : Nat, p (l-n)=false ∧ p (l-n-1)=false := by
    intro n
    induction n with
    | zero => simpa using And.intro h0 h1
    | succ n ih =>
      have e : evol p 1 (l-n-1)=false := by
        rw [he]
        exact hy _ (by omega)
      change rule (p ((l-n-1)-1)) (p (l-n-1)) (p ((l-n-1)+1))=false at e
      rw [show (l-(n : Int)-1)+1=l-(n : Int) by omega,ih.2,ih.1] at e
      have next : p ((l-n-1)-1)=false := by simpa [rule] using e
      constructor
      · simpa only [show l-((n+1 : Nat) : Int)=l-(n : Int)-1 by omega] using ih.2
      · simpa only [show l-((n+1 : Nat) : Int)-1=(l-(n : Int)-1)-1 by omega] using next
  intro i hi
  have e := (down (l-i).toNat).1
  simpa only [show l-(((l-i).toNat : Nat) : Int)=i by omega] using e

/-- Exact finite-parent test, with the white-right boundary fixed explicitly.
The right boundary is at R, not at R+1; omitting that distinction changes the
parent problem. Width one/two and all internal zeroes are covered. -/
theorem finite_white_parent_iff {p y : Int → Bool} {l r : Int}
    (hy : Span y l r) (he : evol p 1=y)
    (hr : ∀ i, r≤i → p i=false) :
    FiniteNonzero p ↔ y (l+1)=true ∧ p (l+1)=true := by
  constructor
  · intro hp
    obtain ⟨a,b,sp⟩ := hp
    have ends := ancestor_endpoints sp hy he
    have hp1 : p (l+1)=true := by
      have ea : a=l+1 := by have := ends.1; omega
      rw [← ea]
      exact sp.left_black
    refine ⟨?_,hp1⟩
    rw [← he]
    change rule (p ((l+1)-1)) (p (l+1)) (p ((l+1)+1))=true
    rw [sp.left_white _ (by omega),hp1]
    rfl
  · rintro ⟨hy1,hp1⟩
    have e1 := congrFun he (l+1)
    change rule (p ((l+1)-1)) (p (l+1)) (p ((l+1)+1))=y (l+1) at e1
    rw [show (l+1)-1=l by omega,hp1,hy1] at e1
    have hp0 : p l=false := by
      cases e:p l <;> simp_all [rule]
    have e0 := congrFun he l
    change rule (p (l-1)) (p l) (p (l+1))=y l at e0
    rw [hp0,hp1,hy.left_black] at e0
    have hpm : p (l-1)=false := by
      cases e:p (l-1) <;> simp_all [rule]
    have left := white_left_from_pair he hy.left_white hp0 hpm
    have rightBlack : p (r-1)=true := by
      have e := congrFun he r
      change rule (p (r-1)) (p r) (p (r+1))=y r at e
      rw [hr r (by omega),hr (r+1) (by omega),hy.right_black] at e
      simpa [rule] using e
    have ordered : l+1≤r-1 := by
      by_cases hn : l+1≤r-1
      · exact hn
      · have z := hr (l+1) (by omega)
        rw [hp1] at z
        cases z
    exact ⟨l+1,r-1,⟨ordered,hp1,rightBlack,
      fun i hi => left i (by omega),fun i hi => hr i (by omega)⟩⟩

end Ruliology.CellularAutomata.Rule30FinitePastDraft
