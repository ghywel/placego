/-!
# Noncircular four-step denominator budget

UNCOMPILED staging component, GC2139. This is the arithmetic part of the G135
hand proof carried in L1151. It constructs no continued fraction or carry arc.
Each growth implication is used only after its INPUT comparison deadline fits.
-/

namespace DenominatorBootstrap

/-- One application: only the current denominator's deadline must fit in N. -/
def GrowthAt (N C q next : Nat) : Prop :=
  4*q+3*C+8 ≤ N → next ≤ 2*q+2*C+6

/-- Four guarded applications, with the exact conservative budget retained. -/
theorem four_steps (C q0 q1 q2 q3 q4 : Nat)
    (h0 : q0 ≤ 2*C+8)
    (h1 : GrowthAt (251*(C+4)) C q0 q1)
    (h2 : GrowthAt (251*(C+4)) C q1 q2)
    (h3 : GrowthAt (251*(C+4)) C q2 q3)
    (h4 : GrowthAt (251*(C+4)) C q3 q4) :
    q1 ≤ 6*C+22 ∧ q2 ≤ 14*C+50 ∧ q3 ≤ 30*C+106 ∧ q4 ≤ 62*C+218 ∧
    4*q4+3*C+8+124 ≤ 251*(C+4) := by
  have hg1 := h1 (by omega)
  have hb1 : q1 ≤ 6*C+22 := by omega
  have hg2 := h2 (by omega)
  have hb2 : q2 ≤ 14*C+50 := by omega
  have hg3 := h3 (by omega)
  have hb3 : q3 ≤ 30*C+106 := by omega
  have hg4 := h4 (by omega)
  have hb4 : q4 ≤ 62*C+218 := by omega
  exact ⟨hb1,hb2,hb3,hb4,by omega⟩

/-- In particular the final target scale is usable without an additional growth premise. -/
theorem final_deadline (C q0 q1 q2 q3 q4 : Nat)
    (h0 : q0 ≤ 2*C+8)
    (h1 : GrowthAt (251*(C+4)) C q0 q1)
    (h2 : GrowthAt (251*(C+4)) C q1 q2)
    (h3 : GrowthAt (251*(C+4)) C q2 q3)
    (h4 : GrowthAt (251*(C+4)) C q3 q4) :
    4*q4+3*C+8 < 251*(C+4) := by
  have hb := (four_steps C q0 q1 q2 q3 q4 h0 h1 h2 h3 h4).2.2.2.2
  omega

/-- Three bounded visits with the two exact shifts contradict a sufficiently large prior denominator. -/
theorem final_visit_contradiction (C previous q qNext qAfter h0 h1 h2 : Nat)
    (hprevious : 2*C+8 < previous)
    (hrecurrence : qAfter = qNext+q)
    (hlo : previous ≤ h0+C+4)
    (hupper : h2 ≤ qAfter+C+2)
    (hshift1 : h1 = h0+q) (hshift2 : h2 = h1+qNext) : False := by
  omega

#print axioms DenominatorBootstrap.four_steps
#print axioms DenominatorBootstrap.final_deadline
#print axioms DenominatorBootstrap.final_visit_contradiction

end DenominatorBootstrap
