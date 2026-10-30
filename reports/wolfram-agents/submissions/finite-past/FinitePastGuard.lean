module
public import Rule30FinitePastDraft

/-! UNCOMPILED development controls, not an official checker. -/
@[expose] public section
namespace FinitePastGuard
open Ruliology.CellularAutomata.Rule30FinitePastDraft

def one (i : Int) : Bool := decide (i=0)
def two (i : Int) : Bool := decide (i=0 ∨ i=1)

theorem one_span : Span one 0 0 := by
  constructor
  · omega
  · decide
  · decide
  · intro i hi; simp [one]; omega
  · intro i hi; simp [one]; omega

theorem two_span : Span two 0 1 := by
  constructor
  · omega
  · decide
  · decide
  · intro i hi; simp [two]; omega
  · intro i hi; simp [two]; omega

theorem one_root : Root one := small_span_root one_span (by decide)
theorem two_root : Root two := small_span_root two_span (by decide)
theorem seed_step_span : Span (Ruliology.CellularAutomata.Rule30Realization.evol one 1) (-1) 1 :=
  span_step one_span

#print axioms Ruliology.CellularAutomata.Rule30FinitePastDraft.finite_step_injective
#print axioms Ruliology.CellularAutomata.Rule30FinitePastDraft.ancestor_bound
#print axioms Ruliology.CellularAutomata.Rule30FinitePastDraft.root_exists
#print axioms Ruliology.CellularAutomata.Rule30FinitePastDraft.root_unique
#print axioms Ruliology.CellularAutomata.Rule30FinitePastDraft.finite_root_decomposition
#print axioms one_root
#print axioms two_root
#print axioms seed_step_span
end FinitePastGuard
