/-!
# The degree law for Rule 30 (statement draft in core Lean, L1073)

Rule 30's `t`-step local rule `f_t`, as a Boolean function of the `2t+1` initial cells of the light cone, has
algebraic degree `2t - 1` for `t ≥ 2`; for `t ≥ 3` its unique top-degree monomial is the product of all cells
except the two leftmost.

Rows are bit masks over the light cone: bit `k` is the initial cell at position `k - t`. By the Möbius formula,
the algebraic-normal-form coefficient of the monomial over a mask `s` is the parity of the number of sub-masks
`m ⊆ s` whose `t`-step evolution is black at the apex.
-/

namespace Rule30DegreeLaw

/-- Rule 30's local rule: left XOR (centre OR right). -/
def rule (a b c : Bool) : Bool := xor a (b || c)

/-- One step on a finite window; the window loses one cell at each end. -/
def stepList : List Bool → List Bool
  | a :: b :: c :: rest => rule a b c :: stepList (b :: c :: rest)
  | _ => []

/-- The apex value after `t` steps of a window (meaningful for windows of length `2t+1`). -/
def apex (t : Nat) (l : List Bool) : Bool := (Nat.repeat stepList t l).headD false

/-- The light-cone window of a mask: bit `k` for `k = 0 … 2t`. -/
def window (t m : Nat) : List Bool := (List.range (2 * t + 1)).map (fun k => m.testBit k)

/-- ANF coefficient of the monomial over mask `s` in the `t`-step rule (Möbius formula). -/
def coeff (t s : Nat) : Bool :=
  ((List.range (2 ^ (2 * t + 1))).filter
      (fun m => (m &&& s) == m && apex t (window t m))).length % 2 == 1

/-- Number of cells in a mask (within the light cone). -/
def cells (t s : Nat) : Nat := (window t s).count true

/-- The claimed top monomial: cells `-t+2 … t`, i.e. bits `2 … 2t`. -/
def topMask (t : Nat) : Nat := 2 ^ (2 * t + 1) - 4

/-- **Degree law.** For `t ≥ 3` the top monomial has coefficient 1, and every other monomial with at least
`2t - 1` cells in the light cone has coefficient 0. -/
theorem degree_law (t : Nat) (ht : 3 ≤ t) :
    coeff t (topMask t) = true ∧
    ∀ s, s < 2 ^ (2 * t + 1) → 2 * t - 1 ≤ cells t s → s ≠ topMask t → coeff t s = false := by
  sorry

/-- Kernel sanity check at `t = 3` (128 masks). -/
example : coeff 3 (topMask 3) = true := by decide +kernel

/-- Kernel sanity check at `t = 3`: the degree-6 monomial (all but the leftmost cell) has coefficient 0. -/
example : coeff 3 (2 ^ 7 - 2) = false := by decide +kernel

end Rule30DegreeLaw

