import TwoPairsWindowTransport

/-! Exact finite inverse histories for the six exceptional eleven-bit rain
windows in L1521. Words and contexts both list cells from low to high. At
horizon `r`, the `2*r` bits immediately below the window on the *earliest*
row determine the two lower inputs to every backward step. -/

namespace TwoPairs.Six
open TwoPairs.WindowTransport (shrinkN)

/-- `##...#...##`, `##...#.#.##`, in increasing depth. -/
def fast : List (List Bool) := [
  [true,true,false,false,false,true,false,false,false,true,true],
  [true,true,false,false,false,true,false,true,false,true,true]]

/-- `.#...##.###`, `..#..##.###`, `#.#..##.###`, `##.#.##.###`. -/
def slow : List (List Bool) := [
  [false,true,false,false,false,true,true,false,true,true,true],
  [false,false,true,false,false,true,true,false,true,true,true],
  [true,false,true,false,false,true,true,false,true,true,true],
  [true,true,false,true,false,true,true,false,true,true,true]]

def screens : List (List Bool) := fast ++ slow

def contexts : Nat → List (List Bool)
  | 0 => [[]]
  | n+1 => (contexts n).map (false :: ·) ++ (contexts n).map (true :: ·)

theorem mem_contexts (c : List Bool) : c ∈ contexts c.length := by
  induction c with
  | nil => simp [contexts]
  | cons b bs ih =>
    change b :: bs ∈ (contexts bs.length).map (false :: ·) ++ (contexts bs.length).map (true :: ·)
    cases b with
    | false => exact List.mem_append_left _ (List.mem_map.mpr ⟨bs,ih,rfl⟩)
    | true => exact List.mem_append_right _ (List.mem_map.mpr ⟨bs,ih,rfl⟩)

/-- The supplied latest row consists of the word and its continuing rain. -/
def target (w : List Bool) (r : Nat) : List Bool :=
  w.take 10 ++ alt (w.getD 10 false) (3*r+4)

/-- The inverse scan at the fixed spatial cut. A forward shrink of the one
shared earliest context supplies the preimage boundary at each time. -/
def decode (ctx : List Bool) : Nat → List Bool → List Bool
  | 0, w => w
  | r+1, w =>
    let c := shrinkN ctx r
    decode ctx r (back (c.getD (c.length-1) false) (c.getD (c.length-2) false) w)

def output (w ctx : List Bool) (r : Nat) : List Bool := decode ctx r (target w r)

/-- Equal pair at the predicted top. The infinite alternating tail above
it is supplied by `TwoPairs.back_rain_tail` on physical rows. -/
abbrev Wall (w ctx : List Bool) (r : Nat) : Prop :=
  (output w ctx r).getD (10+3*r) false = (output w ctx r).getD (9+3*r) false

abbrev Arrived (w ctx : List Bool) (r : Nat) : Prop :=
  ((output w ctx r).drop (3*r)).take 11 ∈ B11

theorem wall_one : ∀ w, w ∈ screens → ∀ c, c ∈ contexts 2 → Wall w c 1 := by decide +kernel
theorem wall_two : ∀ w, w ∈ screens → ∀ c, c ∈ contexts 4 → Wall w c 2 := by decide +kernel
theorem wall_three : ∀ w, w ∈ screens → ∀ c, c ∈ contexts 6 → Wall w c 3 := by decide +kernel

theorem fast_two : ∀ w, w ∈ fast → ∀ c, c ∈ contexts 4 → Arrived w c 2 := by decide +kernel
theorem slow_three : ∀ w, w ∈ slow → ∀ c, c ∈ contexts 6 → Arrived w c 3 := by decide +kernel

/-- Each group needs its last tick for at least one finite context per word. -/
theorem fast_miss_one : ∀ w, w ∈ fast → ∃ c, c ∈ contexts 2 ∧ ¬Arrived w c 1 := by decide +kernel
theorem slow_miss_two : ∀ w, w ∈ slow → ∃ c, c ∈ contexts 4 ∧ ¬Arrived w c 2 := by decide +kernel

#print axioms wall_three
#print axioms fast_two
#print axioms slow_three
end TwoPairs.Six
