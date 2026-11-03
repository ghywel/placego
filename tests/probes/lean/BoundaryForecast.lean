import Std

/-!
GC2564. Small algebraic components for a three-tick boundary forecast.
The a10 identity is known GC2026/L1143. No kit import, closure certificate,
whole-trajectory lift, or Prize claim is made by this file.
-/
namespace BoundaryForecast

def rule (a b c : Bool) : Bool := xor a (b || c)

def two (a b c d e : Bool) : Bool :=
  rule (rule a b c) (rule b c d) (rule c d e)

def three (a b c d e f g : Bool) : Bool :=
  rule (two a b c d e) (two b c d e f) (two c d e f g)

/-- Known local cancellation, GC2026/L1143. -/
theorem known_a10 (a u v : Bool) : two a true false u v = a := by
  cases a <;> cases u <;> cases v <;> rfl

/-- The right endpoint of 0011 is black after three ticks. -/
theorem force0011 (u v w : Bool) : three false false true true u v w = true := by
  cases u <;> cases v <;> cases w <;> rfl

/-- All six flags assert future black bits, at the stated relative coordinates. -/
structure Forecast where
  aNeg : Bool -- in two ticks, offset -1
  aZero : Bool -- in two ticks, offset 0
  aPos : Bool -- in two ticks, offset 1
  bZero : Bool -- in one tick, offset 0
  bPos : Bool -- in one tick, offset 1
  due : Bool -- now, offset 1
  deriving DecidableEq, Repr

structure Generated where
  negTwo : Bool -- in three ticks, offset -2
  negOne : Bool -- in three ticks, offset -1
  zero : Bool -- in three ticks, offset 0
  deriving DecidableEq, Repr

def Valid (p0 p1 p2 : Int → Prop) (s : Forecast) : Prop :=
  (s.aNeg = true → p2 (-1)) ∧
  (s.aZero = true → p2 0) ∧
  (s.aPos = true → p2 1) ∧
  (s.bZero = true → p1 0) ∧
  (s.bPos = true → p1 1) ∧
  (s.due = true → p0 1)

def GeneratedValid (p3 : Int → Prop) (g : Generated) : Prop :=
  (g.negTwo = true → p3 (-2)) ∧
  (g.negOne = true → p3 (-1)) ∧
  (g.zero = true → p3 0)

def stay (s : Forecast) (g : Generated) : Forecast :=
  ⟨g.negOne, g.zero, false, s.aZero, s.aPos, s.bPos⟩

def retreat (s : Forecast) (g : Generated) : Forecast :=
  ⟨g.negTwo, g.negOne, g.zero, s.aNeg, s.aZero, s.bZero⟩

def shift (p : Int → Prop) : Int → Prop := fun d => p (d - 1)

/-- Pure coordinate/deadline transport; generation soundness is an explicit premise. -/
theorem stay_valid (p0 p1 p2 p3 : Int → Prop) (s : Forecast) (g : Generated)
    (hs : Valid p0 p1 p2 s) (hg : GeneratedValid p3 g) :
    Valid p1 p2 p3 (stay s g) := by
  rcases hs with ⟨haN, ha0, haP, hb0, hbP, hc⟩
  rcases hg with ⟨hgN2, hgN1, hg0⟩
  exact ⟨hgN1, hg0, by simp [stay], ha0, haP, hbP⟩

/-- A retreat moves each fixed physical forecast one position right in relative coordinates. -/
theorem retreat_valid (p0 p1 p2 p3 : Int → Prop) (s : Forecast) (g : Generated)
    (hs : Valid p0 p1 p2 s) (hg : GeneratedValid p3 g) :
    Valid (shift p1) (shift p2) (shift p3) (retreat s g) := by
  rcases hs with ⟨haN, ha0, haP, hb0, hbP, hc⟩
  rcases hg with ⟨hgN2, hgN1, hg0⟩
  exact ⟨hgN2, hgN1, hg0, haN, ha0, hb0⟩

/-- An ignored canonical input is a wildcard, even when printed as false. -/
def allowed (due active canonical : Bool) : Bool := !due || !active || canonical

/-- The filter keeps exactly those edges having at least one compatible physical input. -/
theorem allowed_iff_exists (due active canonical : Bool) :
    allowed due active canonical = true ↔
      ∃ physical : Bool, (active = true → physical = canonical) ∧
        (due = true → physical = true) := by
  cases due <;> cases active <;> cases canonical <;> decide

theorem ignored_allowed (due canonical : Bool) : allowed due false canonical = true := by
  cases due <;> cases canonical <;> rfl

theorem active_zero_rejected : allowed true true false = false := rfl

/-- Same base successor, but an ignored printed zero must not be treated as a physical zero. -/
example : allowed true false false = true ∧ (!true || false) = false := by decide

/-- The retained t16 trigger survives retreat, stay, stay to the t19 input. -/
theorem saved_path_due (s : Forecast) (g17 g18 : Generated) :
    (stay (stay (retreat s ⟨false, false, true⟩) g17) g18).due = true := rfl

#print axioms known_a10
#print axioms force0011
#print axioms stay_valid
#print axioms retreat_valid
#print axioms allowed_iff_exists
#print axioms saved_path_due
end BoundaryForecast
