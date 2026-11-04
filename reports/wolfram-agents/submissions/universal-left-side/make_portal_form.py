#!/usr/bin/env python3
"""make_portal_form.py KIT_MODULE OUT: the portal form of Rule30UniversalLeftSide.lean (L1504).

The portal's verifier runs an older kit (c42f6e51) with no Rule30LeftCoincidence, so the form imports Rule30Prize,
Rule30LeftReset and Rule30FiniteDiagonals, uses the namespace Rule30Submission, and carries F2 (solutions_agree) inline.
"""
import sys
kit = open(sys.argv[1]).read()
END = 'end Ruliology.CellularAutomata.Rule30UniversalLeftSide\n'
out_portal = sys.argv[2]

# Portal form: core imports of the verifier's kit, the namespace Rule30Submission, F2 carried inline.
p = kit
p = p.replace('module\n\npublic import Ruliology.CellularAutomata.Rule30LeftCoincidence\npublic import Ruliology.CellularAutomata.Rule30FiniteDiagonals\n',
              'import Ruliology.CellularAutomata.Rule30Prize\nimport Ruliology.CellularAutomata.Rule30LeftReset\nimport Ruliology.CellularAutomata.Rule30FiniteDiagonals\n')
p = p.replace('@[expose] public section\n\nnamespace Ruliology.CellularAutomata.Rule30UniversalLeftSide\n',
              'namespace Rule30Submission\n\nopen Ruliology.CellularAutomata\n')
p = p.replace('open Rule30Jen Rule30Realization Rule30Diagonals Rule30LeftReset Rule30LeftCoincidence Rule30FiniteDiagonals\n',
              '''open Rule30Jen Rule30Realization Rule30Diagonals Rule30LeftReset Rule30FiniteDiagonals

/-- **F2** (`Rule30LeftCoincidence.solutions_agree` on kit main, carried here because the verifier's kit predates it). Two
children of the same farther and nearer words agree from `s0 + 1` on once `b s0` is black. -/
theorem solutions_agree {x x' a b : Nat → Bool} (hx : ∀ t, x (t + 1) = xor (a t) (b t || x t))
    (hx' : ∀ t, x' (t + 1) = xor (a t) (b t || x' t)) {s0 : Nat} (hs : b s0 = true) :
    ∀ t, s0 + 1 ≤ t → x t = x' t := by
  intro t ht
  obtain ⟨n, rfl⟩ : ∃ n, t = s0 + 1 + n := ⟨t - (s0 + 1), by omega⟩
  clear ht
  induction n with
  | zero => rw [Nat.add_zero, hx, hx', hs]; simp
  | succ n ih => rw [show s0 + 1 + (n + 1) = (s0 + 1 + n) + 1 by omega, hx, hx', ih]
''')
p = p.replace(END, 'end Rule30Submission\n')
assert 'LeftCoincidence\n' not in p.split('/-!')[0]
open(out_portal, 'w').write(p)
