/-!
Pulse-profile contribution under development (GC2044).
Core Lean; no imports. This file proves local algebra and the exact interval budget.
The cyclic weight/run count and periodic hole/delay bridge are not yet formalized.
No finite-seed ancestry, settling bound, novelty clearance or portal submission is claimed.
-/
namespace Rule30PulseProfiles

def bit (b : Bool) : Int := if b then 1 else 0

def source (next pulse current : Bool) : Bool := xor next (pulse || current)

theorem source_solves (next pulse current : Bool) :
    xor (source next pulse current) (pulse || current) = next := by
  cases next <;> cases pulse <;> cases current <;> rfl

theorem source_unique (a next pulse current : Bool)
    (h : next = xor a (pulse || current)) : a = source next pulse current := by
  cases a <;> cases next <;> cases pulse <;> cases current <;> simp_all [source]

theorem source_without_pulse (next current : Bool) :
    source next false current = xor next current := rfl

theorem source_black_current (next pulse : Bool) :
    source next pulse true = xor next true := by cases pulse <;> rfl

theorem source_white_pulse (next : Bool) :
    source next true false = !(xor next false) := by cases next <;> rfl

/-- Pointwise signed weight correction; cyclic summation will be a separate theorem. -/
theorem source_bit_correction (next pulse current : Bool) :
    bit (source next pulse current) = bit (xor next current) +
      (if pulse then (if current then 0 else if next then -1 else 1) else 0) := by
  cases next <;> cases pulse <;> cases current <;> decide

/-- The six nonempty intervals and the empty interval of delays (k,l,1), slope5/2, doubled. -/
def intervalDebt2 (k l : Int) : Int :=
  max 0 (max (2*k-5) (max (2*l-5) (max (-3)
    (max (2*k+2*l-10) (max (2*l-8) (2*k+2*l-13))))))

def reducedDebt2 (k l : Int) : Int :=
  max 0 (max (2*k-5) (max (2*k+2*l-10) (2*l-5)))

theorem intervalDebt2_reduce (k l : Int) :
    intervalDebt2 k l = reducedDebt2 k l := by
  unfold intervalDebt2 reducedDebt2
  omega

theorem reducedDebt2_monotone (k k' l : Int) (h : k ≤ k') :
    reducedDebt2 k l ≤ reducedDebt2 k' l := by
  unfold reducedDebt2
  omega

theorem intervalDebt2_monotone (k k' l : Int) (h : k ≤ k') :
    intervalDebt2 k l ≤ intervalDebt2 k' l := by
  rw [intervalDebt2_reduce, intervalDebt2_reduce]
  exact reducedDebt2_monotone k k' l h

theorem intervalDebt2_at_pulse (q l : Int) (hq : 4 ≤ q) (hl : l ≤ q-1) :
    intervalDebt2 q l = 2*q-5 + max 0 (2*l-5) := by
  rw [intervalDebt2_reduce]
  unfold reducedDebt2
  omega

/-- Conditional arithmetic budget: the actual cyclic delay identification is still to be formalized. -/
theorem pulse_window_bound (q k l : Int) (hq : 4 ≤ q) (hk : k ≤ q) (hl : l ≤ q-1) :
    intervalDebt2 k l ≤ 2*q-5 + max 0 (2*l-5) := by
  rw [← intervalDebt2_at_pulse q l hq hl]
  exact intervalDebt2_monotone k q l hk

/-- Literal Rule30 and its left-diagonal coordinates for arbitrary initial rows. -/
def step (x : Int → Bool) (i : Int) : Bool := xor (x (i-1)) (x i || x (i+1))
def evol : Nat → (Int → Bool) → Int → Bool
  | 0, x => x
  | t+1, x => step (evol t x)
def leftDiag (x : Int → Bool) (j : Int) (t : Nat) : Bool := evol t x (j-t)

theorem leftDiag_step (x : Int → Bool) (j : Int) (t : Nat) :
    leftDiag x (j+2) (t+1) =
      xor (leftDiag x j t) (leftDiag x (j+1) t || leftDiag x (j+2) t) := by
  simp only [leftDiag, evol, step]
  congr 1
  · congr 1; omega
  · congr 1 <;> congr 1 <;> omega

end Rule30PulseProfiles

#print axioms Rule30PulseProfiles.source_bit_correction
#print axioms Rule30PulseProfiles.pulse_window_bound
#print axioms Rule30PulseProfiles.leftDiag_step
