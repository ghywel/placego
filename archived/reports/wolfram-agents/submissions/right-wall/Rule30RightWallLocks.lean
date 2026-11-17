module

public import Ruliology.CellularAutomata.Rule30RightWall

/-!
# Rule 30: three locks at the wall of a rain-tailed edge code

A *lock* is a set of windows at the wall, in phases, closed under the backward tick for every pair of lower cells. A code showing one
of its windows shows them at every backward tick for ever, whatever lies below, and its letters follow the phases (`Lock.letters`).

* `LockAB`: four windows of 45 cells, letters `A`, `B` for ever. Each window starts with a reset word.
* `LockAAB`: six windows of 136 cells, letters `A`, `A`, `B`. Each window starts with a reset word.
* `LockThird`: forty windows of 175 cells in six phases, letters `B`, `A`, `A`, `B`, `A`, `A`. Apart from the wall's own word, no reset
  word stands at one depth in all forty windows (`no_floor`).

Each lock has a witness on an anchored row, and no code in a lock is periodic under the edge map. Nothing here concerns the center column.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30RightWall

open WindowClosed

set_option autoImplicit false
set_option maxRecDepth 100000

/-! ## The letters `A`, `B`: four windows of 45 cells -/

namespace LockAB

/-- The phases, as window numbers, low cell first. -/
def Ph : List (List Nat) := [[27432157596204, 27432157596202],
  [27391699171004, 27391699171002]]

/-- All the windows, as numbers. -/
def All : List Nat := Ph.flatten

/-- All the windows. -/
def Win : List (List Bool) := All.map (dec 45)

/-- The letter of each phase. -/
def lc (r : Nat) : List Bool := if r = 1 then wordB else wordA

/-- **The lock.** -/
theorem lock : Lock 45 2 Ph All :=
  ⟨by decide, by decide, by decide +kernel, by decide +kernel, by decide +kernel⟩

theorem closed : Closed 45 Win := lock.closed

/-- **For ever.** Every row `n` ticks before a held row is held `3 n` cells higher, whatever lies below the window. -/
theorem held {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held 45 Win x L) :
    ∀ n z, iter z n = x → Held 45 Win z (L + 3 * n) := held_forever closed hL h

theorem chk_letters : ∀ r, r < 2 → ∀ n, n ∈ Ph.getD r [] → dec 11 (n >>> 34) = lc r := by decide +kernel

/-- **The letters.** There is a phase `r` such that the wall of every row `n` ticks before the row reads the letter of phase `r + n`. -/
theorem letters {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held 45 Win x L) :
    ∃ r, r < 2 ∧ ∀ n z, iter z n = x → seg z (L + 3 * n + 34) 11 = if (r + n) % 2 = 1 then wordB else wordA := by
  obtain ⟨r, hr, f⟩ := lock.letters lc chk_letters hL h
  exact ⟨r, hr, fun n z hz => by simpa [lc] using f n z hz⟩

theorem chk_wall : ∀ n, n ∈ All → n >>> 34 = 1596 ∨ n >>> 34 = 1594 := by decide +kernel

/-- **A row in the lock is not periodic.** -/
theorem not_periodic {x : Row} {L P : Nat} (hL : 2 ≤ L) (h : Held 45 Win x L) (hP : 0 < P) : iter x P ≠ x := by
  refine held_not_periodic closed (by decide) (fun w hw => ?_) hL h hP
  obtain ⟨n, hn, rfl⟩ := List.mem_map.1 hw
  exact wall_of_letter (by decide) (chk_wall n hn)

/-- **An anchored row in the lock.** -/
theorem witness : anchor 45 27432157596204 0 = true ∧ Held 45 Win (anchor 45 27432157596204) 2 :=
  anchor_held (by decide) (by decide +kernel) (by decide +kernel)

/-- **The shield of the lock.** Each window starts with a reset word. -/
theorem floor : ∀ n, n ∈ All → ∃ b u v, (dec 45 n).take 10 = Reset.F b u v := by decide +kernel

end LockAB

/-! ## The letters `A`, `A`, `B`: six windows of 136 cells -/

namespace LockAAB

/-- The phases, as window numbers, low cell first. -/
def Ph : List (List Nat) := [[67918664933144423441542139865466147588794, 67918664933144423441542139865466147588796],
  [67908875212190969569599336687020282132138, 67908875212190969569599336687020282132140],
  [67819754217029842684664044888796937824810, 67819754217029842684664044888796937824812]]

/-- All the windows, as numbers. -/
def All : List Nat := Ph.flatten

/-- All the windows. -/
def Win : List (List Bool) := All.map (dec 136)

/-- The letter of each phase. -/
def lc (r : Nat) : List Bool := if r = 2 then wordB else wordA

/-- **The lock.** -/
theorem lock : Lock 136 3 Ph All :=
  ⟨by decide, by decide, by decide +kernel, by decide +kernel, by decide +kernel⟩

theorem closed : Closed 136 Win := lock.closed

/-- **For ever.** Every row `n` ticks before a held row is held `3 n` cells higher, whatever lies below the window. -/
theorem held {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held 136 Win x L) :
    ∀ n z, iter z n = x → Held 136 Win z (L + 3 * n) := held_forever closed hL h

theorem chk_letters : ∀ r, r < 3 → ∀ n, n ∈ Ph.getD r [] → dec 11 (n >>> 125) = lc r := by decide +kernel

/-- **The letters.** There is a phase `r` such that the wall of every row `n` ticks before the row reads the letter of phase `r + n`. -/
theorem letters {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held 136 Win x L) :
    ∃ r, r < 3 ∧ ∀ n z, iter z n = x → seg z (L + 3 * n + 125) 11 = if (r + n) % 3 = 2 then wordB else wordA := by
  obtain ⟨r, hr, f⟩ := lock.letters lc chk_letters hL h
  exact ⟨r, hr, fun n z hz => by simpa [lc] using f n z hz⟩

theorem chk_wall : ∀ n, n ∈ All → n >>> 125 = 1596 ∨ n >>> 125 = 1594 := by decide +kernel

/-- **A row in the lock is not periodic.** -/
theorem not_periodic {x : Row} {L P : Nat} (hL : 2 ≤ L) (h : Held 136 Win x L) (hP : 0 < P) : iter x P ≠ x := by
  refine held_not_periodic closed (by decide) (fun w hw => ?_) hL h hP
  obtain ⟨n, hn, rfl⟩ := List.mem_map.1 hw
  exact wall_of_letter (by decide) (chk_wall n hn)

/-- **An anchored row in the lock.** -/
theorem witness : anchor 136 67918664933144423441542139865466147588794 0 = true ∧ Held 136 Win (anchor 136 67918664933144423441542139865466147588794) 2 :=
  anchor_held (by decide) (by decide +kernel) (by decide +kernel)

/-- **The shield of the lock.** Each window starts with a reset word. -/
theorem floor : ∀ n, n ∈ All → ∃ b u v, (dec 136 n).take 10 = Reset.F b u v := by decide +kernel

end LockAAB

/-! ## A third lock, with no fixed shield: forty windows of 175 cells -/

namespace LockThird

/-- The phases, as window numbers, low cell first. -/
def Ph : List (List Nat) := [[37284303768780549450216512176333106322617512176932327, 37284303768780549450216512176333106322617512176932363, 37284303768780549450216512176333106322617512176932362, 37284303768780549450216512176333106322617512176932305, 37284303768780549450216512176333106322617512176932360],
  [37338680436793518946018258025312893609782730154505572, 37338680436793518946018258025312893609782730154505555, 37338680436793518946018258025312893609782730154505790, 37338680436793518946018258025312893609782730154505573, 37338680436793518946018258025312893609782730154505574, 37338680436793518946018258025312893609782730154505791],
  [37333299180212662931848950068353642697240989240174933, 37333299180212662931848950068353642697240989240174934, 37333299180212662931848950068353642697240989240177210, 37333299180212662931848950068353642697240989240174913, 37333299180212662931848950068353642697240989240174947, 37333299180212662931848950068353642697240989240174932, 37333299180212662931848950068353642697240989240177212],
  [37284303528463190167104685405439550272830198693161685, 37284303528463190167104685405439550272830198693161686, 37284303528463190167104685405439550272830198693161687, 37284303528463190167104685405439550272830198693161688, 37284303528463190167104685405439550272830198693163452, 37284303528463190167104685405439550272830198693161699, 37284303528463190167104685405439550272830198693161684, 37284303528463190167104685405439550272830198693163450],
  [37338680284242987720315585462861809216178240387134149, 37338680284242987720315585462861809216178240387134150, 37338680284242987720315585462861809216178240387134120, 37338680284242987720315585462861809216178240387133964, 37338680284242987720315585462861809216178240387133962, 37338680284242987720315585462861809216178240387134131, 37338680284242987720315585462861809216178240387134148],
  [37333299375615735401535943766818242528686808079618503, 37333299375615735401535943766818242528686808079618472, 37333299375615735401535943766818242528686808079618475, 37333299375615735401535943766818242528686808079618474, 37333299375615735401535943766818242528686808079618494, 37333299375615735401535943766818242528686808079618481, 37333299375615735401535943766818242528686808079618496]]

/-- All the windows, as numbers. -/
def All : List Nat := Ph.flatten

/-- All the windows. -/
def Win : List (List Bool) := All.map (dec 175)

/-- The letter of each phase. -/
def lc (r : Nat) : List Bool := if r % 3 = 0 then wordB else wordA

/-- **The lock.** -/
theorem lock : Lock 175 6 Ph All :=
  ⟨by decide, by decide, by decide +kernel, by decide +kernel, by decide +kernel⟩

theorem closed : Closed 175 Win := lock.closed

/-- **For ever.** Every row `n` ticks before a held row is held `3 n` cells higher, whatever lies below the window. -/
theorem held {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held 175 Win x L) :
    ∀ n z, iter z n = x → Held 175 Win z (L + 3 * n) := held_forever closed hL h

theorem chk_letters : ∀ r, r < 6 → ∀ n, n ∈ Ph.getD r [] → dec 11 (n >>> 164) = lc r := by decide +kernel

/-- **The letters.** There is a phase `r` such that the wall of every row `n` ticks before the row reads the letter of phase `r + n`. -/
theorem letters {x : Row} {L : Nat} (hL : 2 ≤ L) (h : Held 175 Win x L) :
    ∃ r, r < 6 ∧ ∀ n z, iter z n = x → seg z (L + 3 * n + 164) 11 = if (r + n) % 6 % 3 = 0 then wordB else wordA := by
  obtain ⟨r, hr, f⟩ := lock.letters lc chk_letters hL h
  exact ⟨r, hr, fun n z hz => by simpa [lc] using f n z hz⟩

theorem chk_wall : ∀ n, n ∈ All → n >>> 164 = 1596 ∨ n >>> 164 = 1594 := by decide +kernel

/-- **A row in the lock is not periodic.** -/
theorem not_periodic {x : Row} {L P : Nat} (hL : 2 ≤ L) (h : Held 175 Win x L) (hP : 0 < P) : iter x P ≠ x := by
  refine held_not_periodic closed (by decide) (fun w hw => ?_) hL h hP
  obtain ⟨n, hn, rfl⟩ := List.mem_map.1 hw
  exact wall_of_letter (by decide) (chk_wall n hn)

/-- **An anchored row in the lock.** -/
theorem witness : anchor 175 37284303768780549450216512176333106322617512176932327 0 = true ∧ Held 175 Win (anchor 175 37284303768780549450216512176333106322617512176932327) 2 :=
  anchor_held (by decide) (by decide +kernel) (by decide +kernel)

/-- **No fixed shield.** Below the wall's own word, no depth carries a reset word in all forty windows. -/
theorem no_floor : ∀ d, d < 164 → ¬ ∀ n, n ∈ All → ∃ b u v, ((dec 175 n).drop d).take 10 = Reset.F b u v := by decide +kernel

end LockThird

end Ruliology.CellularAutomata.Rule30RightWall
